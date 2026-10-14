"""Prüft die TEI-Dateien in data/ und schreibt docs/datenbericht.md.

- Wohlgeformtheit (lxml), optional RelaxNG-Validierung gegen schema/zbz_hersch.rng
- Pflichtfelder im teiHeader
- Element- und Attributstatistik für <text>

Exit-Code 1 nur, wenn eine Datei nicht wohlgeformt ist.
Die TEI-Dateien werden nur gelesen, nie verändert.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SCHEMA = ROOT / "schema" / "zbz_hersch.rng"
REPORT = ROOT / "docs" / "datenbericht.md"
TAXONOMY = ROOT / "assets" / "i18n" / "taxonomy.json"

NS = {"tei": "http://www.tei-c.org/ns/1.0"}
TEI = "{http://www.tei-c.org/ns/1.0}"
XML = "{http://www.w3.org/XML/1998/namespace}"
VALUE_ATTRS = {"rendition", "type", "subtype", "place", "break", "dim", "unit", "rend", "xml:lang"}
SCHEMES = ("hersch_genre", "hersch_worktype", "hersch_keywords")


def localname(tag: str) -> str:
    if tag.startswith(TEI):
        return tag[len(TEI):]
    if tag.startswith(XML):
        return "xml:" + tag[len(XML):]
    return tag


def first(tree, xpath: str) -> str | None:
    res = tree.xpath(xpath, namespaces=NS)
    if not res:
        return None
    val = res[0] if isinstance(res[0], str) else res[0].text
    val = " ".join((val or "").split())
    return val or None


def load_taxonomy() -> dict:
    if not TAXONOMY.exists():
        return {}
    import json
    return json.loads(TAXONOMY.read_text(encoding="utf-8"))


def check_file(path: Path, rng, taxonomy: dict):
    info = {"datei": path.name, "probleme": [], "hinweise": []}
    try:
        tree = etree.parse(str(path))
    except etree.XMLSyntaxError as e:
        info["wohlgeformt"] = False
        info["probleme"].append(f"nicht wohlgeformt: {e}")
        return info, None, None
    info["wohlgeformt"] = True

    if rng is not None:
        if rng.validate(tree):
            info["schema"] = "gültig"
        else:
            errs = rng.error_log.filter_from_errors()
            info["schema"] = f"{len(errs)} Fehler"
            for err in errs[:10]:
                info["probleme"].append(f"Schema, Zeile {err.line}: {err.message}")
            if len(errs) > 10:
                info["probleme"].append(f"Schema: … und {len(errs) - 10} weitere Fehler")
    else:
        info["schema"] = "–"

    h = "/tei:TEI/tei:teiHeader"
    info["titel"] = first(tree, f"{h}/tei:fileDesc/tei:titleStmt/tei:title[@type='item'][@subtype='main']")
    info["jahr"] = first(tree, f"{h}/tei:fileDesc/tei:sourceDesc//tei:imprint/tei:date/@when")
    info["id"] = first(tree, f"{h}//tei:idno[@type='hersc:projectID']")
    info["sprache"] = first(tree, f"{h}//tei:textLang/@mainLang")
    lic = tree.xpath(f"{h}//tei:availability/tei:licence", namespaces=NS)
    info["lizenz"] = (lic[0].get("target") or " ".join("".join(lic[0].itertext()).split())) if lic else None

    labels = {"titel": "Haupttitel", "jahr": "Jahr (imprint/date/@when)",
              "id": "Projekt-ID", "sprache": "Sprache (textLang/@mainLang)", "lizenz": "Lizenz"}
    for key, label in labels.items():
        if not info[key]:
            info["probleme"].append(f"Pflichtfeld fehlt: {label}")

    if info["jahr"] and not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", info["jahr"]):
        info["probleme"].append(f"Jahr hat unerwartetes Format: «{info['jahr']}»")
    if info["id"] and info["id"] != path.stem:
        info["hinweise"].append(f"Projekt-ID «{info['id']}» weicht vom Dateinamen ab")

    cats = {}
    for s in SCHEMES:
        targets = []
        for cr in tree.xpath(f"{h}//tei:catRef[@scheme='{s}']", namespaces=NS):
            targets += [t.lstrip("#") for t in (cr.get("target") or "").split()]
        cats[s] = targets
        if not targets:
            info["probleme"].append(f"kein catRef mit scheme «{s}»")
        for t in targets:
            entry = taxonomy.get(s, {}).get(t) if taxonomy else {}
            if entry is None:
                info["probleme"].append(f"Kategorie «{t}» ({s}) ist in taxonomy.json nicht definiert")
            elif entry.get("_entwurf"):
                info["hinweise"].append(f"Kategorie «{t}» ({s}) hat in der Hersch-App kein Label (Entwurf)")
    other = {cr.get("scheme") for cr in tree.xpath(f"{h}//tei:catRef", namespaces=NS)} - set(SCHEMES)
    for s in sorted(o for o in other if o):
        info["hinweise"].append(f"unbekanntes catRef-Schema «{s}»")
    info["kategorien"] = cats

    # GND-Schreibweisen (Hinweis, keine Korrektur)
    refs = [e.get("ref") for e in tree.iter() if isinstance(e.tag, str) and e.get("ref")]
    plain = [r for r in refs if re.fullmatch(r"\d[\dX-]*", r)]
    prefixed = [r for r in refs if r.startswith("GND-")]
    gnd_ok = re.compile(r"(GND-)?\d[\d-]*[\dX]")
    bad = Counter(r for r in refs if not gnd_ok.fullmatch(r))
    for r, n in sorted(bad.items()):
        info["probleme"].append(f"ungültige GND-Ref «{r}» ({n}×)")
    if plain and prefixed:
        info["hinweise"].append(
            f"GND-Refs uneinheitlich: {len(prefixed)}× mit «GND-», {len(plain)}× ohne (z. B. {plain[0]})")

    text = tree.find(f"{TEI}text")
    elements, attributes, values = Counter(), Counter(), Counter()
    if text is None:
        info["probleme"].append("kein <text>-Element")
    else:
        for el in text.iter():
            if not isinstance(el.tag, str):
                continue
            name = localname(el.tag)
            elements[name] += 1
            for att in el.attrib:
                attributes[f"{name}/@{localname(att)}"] += 1
                if localname(att) in VALUE_ATTRS:
                    for v in el.get(att).split():
                        values[f"{name}/@{localname(att)}=\"{v}\""] += 1
    info["werte"] = values
    return info, elements, attributes


def md_escape(s) -> str:
    return (str(s) if s else "–").replace("|", "\\|")


def write_report(results, el_stats, att_stats, schema_note):
    files = [r["datei"] for r in results]
    lines = [
        "# Datenbericht",
        "",
        f"Erzeugt von `scripts/validate.py` am {date.today().isoformat()}. "
        "Die Dateien in `data/` wurden nur gelesen. Korrekturen macht das Team in Oxygen.",
        "",
        f"- Dateien: {len(results)}",
        f"- Wohlgeformt: {sum(r['wohlgeformt'] for r in results)} von {len(results)}",
        f"- Schema: {schema_note}",
        "",
        "## Übersicht",
        "",
        "| Datei | ID | Titel | Jahr | Sprache | Werktyp | Gattung | Schlagwörter | Schema | Probleme |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        if not r["wohlgeformt"]:
            lines.append(f"| {r['datei']} | – | – | – | – | – | – | – | – | nicht wohlgeformt |")
            continue
        c = r["kategorien"]
        lines.append(
            f"| {r['datei']} | {md_escape(r['id'])} | {md_escape(r['titel'])} | {md_escape(r['jahr'])} "
            f"| {md_escape(r['sprache'])} | {md_escape(', '.join(c['hersch_worktype']))} "
            f"| {md_escape(', '.join(c['hersch_genre']))} | {md_escape(', '.join(c['hersch_keywords']))} "
            f"| {r['schema']} | {len(r['probleme'])} |")

    lines += ["", "## Abweichungen", ""]
    any_issue = False
    for r in results:
        if r["probleme"] or r["hinweise"]:
            any_issue = True
            lines.append(f"### {r['datei']}")
            lines.append("")
            lines += [f"- **Problem:** {p}" for p in r["probleme"]]
            lines += [f"- Hinweis: {p}" for p in r["hinweise"]]
            lines.append("")
    if not any_issue:
        lines += ["Keine Abweichungen gefunden.", ""]

    # Lizenzen und Sprachen auf einen Blick (Uneinheitlichkeit sichtbar machen)
    lines += ["## Werte im Vergleich", ""]
    for key, label in (("lizenz", "Lizenz"), ("sprache", "Sprache")):
        vals = Counter(r.get(key) or "fehlt" for r in results if r["wohlgeformt"])
        lines.append(f"- {label}: " + "; ".join(f"{v} ({n}×)" for v, n in vals.most_common()))
    cats_all = {s: Counter() for s in SCHEMES}
    for r in results:
        for s in SCHEMES:
            cats_all[s].update(r.get("kategorien", {}).get(s, []))
    for s in SCHEMES:
        lines.append(f"- `{s}`: " + (", ".join(f"{k} ({n}×)" for k, n in sorted(cats_all[s].items())) or "–"))
    lines.append("")

    def stat_table(title, stats):
        out = [f"## {title}", "",
               "| Name | Total | " + " | ".join(Path(f).stem for f in files) + " |",
               "|---|---|" + "---|" * len(files)]
        total = Counter()
        for s in stats.values():
            total.update(s)
        for name, n in sorted(total.items(), key=lambda x: (-x[1], x[0])):
            out.append(f"| `{name}` | {n} | " + " | ".join(str(stats[f].get(name, "")) for f in files) + " |")
        return out + [""]

    lines += stat_table("Elemente in `<text>`", el_stats)
    lines += stat_table("Attribute in `<text>`", att_stats)
    lines += stat_table("Attributwerte in `<text>` (für die ODD)",
                        {r["datei"]: r.get("werte", Counter()) for r in results})
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rng, schema_note = None, "kein Schema unter `schema/zbz_hersch.rng`, nur Wohlgeformtheit geprüft"
    if SCHEMA.exists():
        rng = etree.RelaxNG(etree.parse(str(SCHEMA)))
        schema_note = "gegen `schema/zbz_hersch.rng` validiert"

    taxonomy = load_taxonomy()
    results, el_stats, att_stats = [], {}, {}
    for path in sorted(DATA.glob("*.xml"), key=lambda p: (len(p.stem), p.stem)):
        info, els, atts = check_file(path, rng, taxonomy)
        results.append(info)
        el_stats[path.name] = els or Counter()
        att_stats[path.name] = atts or Counter()
        status = "OK" if info["wohlgeformt"] else "NICHT WOHLGEFORMT"
        print(f"{path.name}: {status}, {len(info['probleme'])} Probleme, {len(info['hinweise'])} Hinweise")

    write_report(results, el_stats, att_stats, schema_note)
    print(f"Bericht: {REPORT.relative_to(ROOT)}")
    return 0 if all(r["wohlgeformt"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
