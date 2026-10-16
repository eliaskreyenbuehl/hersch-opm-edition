"""Metadaten aller Werke aus den teiHeadern → _site/data/works.json

Aufruf:  uv run python scripts/extract_metadata.py
(build.py ruft das Skript auf.) Die TEI-Dateien werden nur gelesen.

Pro Datei ein Eintrag. Fehlt ein Feld, bleibt es leer ("" bzw. []), das Skript
bricht nicht ab. Schlagwörter mit `_alias` in taxonomy.json werden aufgelöst
(Entscheid 2026-10-14: bildende-kuenste → kuenste + malerei).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'
TAXONOMY = ROOT / 'assets' / 'i18n' / 'taxonomy.json'
OUT = ROOT / '_site' / 'data' / 'works.json'

NS = {'tei': 'http://www.tei-c.org/ns/1.0'}
GND_RE = re.compile(r'^(?:GND-)?(\d[\dX-]*)$')


def text(tree, xpath: str) -> str:
    """Erster Treffer als normalisierter Text, sonst ''."""
    res = tree.xpath(xpath, namespaces=NS)
    if not res:
        return ''
    val = res[0] if isinstance(res[0], str) else ''.join(res[0].itertext())
    return ' '.join(val.split())


def categories(tree, scheme: str) -> list[str]:
    """Schlüssel aus catRef[@scheme]/@target, ohne '#'."""
    targets = tree.xpath(f"//tei:teiHeader//tei:catRef[@scheme = '{scheme}']/@target", namespaces=NS)
    return [t.lstrip('#') for v in targets for t in v.split() if t.lstrip('#')]


def resolve_aliases(keys: list[str], scheme: dict) -> list[str]:
    out: list[str] = []
    for key in keys:
        for k in scheme.get(key, {}).get('_alias', [key]):
            if k not in out:
                out.append(k)
    return out


def normalize_gnd(ref: str) -> str | None:
    """'GND-118557106' und '118557106' → '118557106'; Platzhalter → None."""
    m = GND_RE.match(ref.strip())
    return m.group(1) if m else None


def extract(path: Path, taxonomy: dict) -> dict:
    tree = etree.parse(str(path))
    bibl = '//tei:teiHeader//tei:sourceDesc//tei:biblStruct'
    doi = text(tree, "//tei:publicationStmt/tei:idno[@type = 'DOI']")
    pages = text(tree, f"{bibl}//tei:biblScope[@unit = 'page' or @unit = 'pp']").replace('-', '–')

    persons: list[str] = []
    for ref in tree.xpath('//tei:text//tei:persName/@ref', namespaces=NS):
        for part in ref.split():
            gnd = normalize_gnd(part)
            if gnd and gnd not in persons:
                persons.append(gnd)

    return {
        'id': path.stem,
        'projectId': text(tree, "//tei:publicationStmt/tei:idno[@type = 'hersc:projectID']"),
        'title': text(tree, "//tei:titleStmt/tei:title[@type = 'item'][1]"),
        'subtitle': text(tree, f"{bibl}//tei:title[@subtype = 'sub']"),
        'year': text(tree, f"{bibl}//tei:imprint/tei:date/@when")[:4],
        # Erschienen in: nur bei Beiträgen (analytic), sonst ist monogr das Werk selbst
        'container': text(tree, f"{bibl}[tei:analytic]/tei:monogr/tei:title"),
        'containerLevel': text(tree, f"{bibl}[tei:analytic]/tei:monogr/tei:title/@level"),
        'volume': text(tree, f"{bibl}//tei:biblScope[@unit = 'volume' or @unit = 'vol']"),
        'issue': text(tree, f"{bibl}//tei:biblScope[@unit = 'issue']"),
        'pages': pages,
        'lang': text(tree, f"{bibl}//tei:textLang/@mainLang"),
        'genre': next(iter(categories(tree, 'hersch_genre')), ''),
        'worktype': next(iter(categories(tree, 'hersch_worktype')), ''),
        'keywords': resolve_aliases(categories(tree, 'hersch_keywords'), taxonomy.get('hersch_keywords', {})),
        'mla': text(tree, "//tei:publicationStmt/tei:idno[@type = 'MLA-9']"),
        'doi': '' if doi == 'DOI_COMING' else doi,
        'swisscovery': text(tree, "//tei:publicationStmt/tei:idno[@type = 'URI'][@subtype = 'swisscovery']"),
        # relativ zur Site-Wurzel; Seiten in Unterordnern setzen ihr Präfix davor
        'href': f'edition/{path.name}/001.html',
        'persons': persons,
    }


def main() -> int:
    taxonomy = json.loads(TAXONOMY.read_text(encoding='utf-8'))
    works = []
    for path in sorted(DATA.glob('*.xml'), key=lambda p: (len(p.stem), p.stem)):
        try:
            works.append(extract(path, taxonomy))
        except etree.XMLSyntaxError as err:
            print(f'Übersprungen (nicht wohlgeformt): {path.name}: {err}', file=sys.stderr)
    works.sort(key=lambda w: (w['year'] or '9999', w['title']))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(works, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'{len(works)} Werke → {OUT.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
