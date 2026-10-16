# Leseansicht (Phase 3)

## Aufbau

| Teil | Datei | Bemerkung |
|---|---|---|
| Seitengerüst | `templates/base.html.j2` | Kopf mit Logo und Menü (Start, Werke, Personen, Suche, Über), Sprachwahl DE/FR/EN (nur Markup, `data-lang`/`data-i18n`, Funktion in Phase 6), Fuss mit Impressum, CC BY-SA 4.0, ZB |
| Leseseite | `templates/chunk.html.j2` | erbt von base; Seitenleiste, Lesetext (`content_html`), Vor/Zurück bei mehreren Chunks |
| vorläufige Übersicht | `templates/edition-index.html.j2` | `_site/edition/index.html`, einfache Liste, wird in Phase 4 durch die Werkliste ersetzt |
| CSS | `assets/css/tokens.css`, `layout.css`, `text.css`, `assets/fonts/fonts.css` | Reihenfolge auf der Seite: tokens → layout → ODD-CSS → text |
| Konfiguration | `opm.toml` `[chunking]` | `xpath = "//text"`, Assets, Metadaten-Fragmente |
| Build | `scripts/build.py` | validate → `opm chunk` → XML-Kopien nach `_site/edition/xml/` |

Ausgabe: `_site/edition/<datei>.xml/001.html`, gemeinsame Dateien in `_site/edition/css/` (ODD-CSS) und `_site/edition/assets/`.

**Chunking:** ein Chunk pro Werk. Die 12 Texte haben je nur ein `div n="1"` ohne Unterkapitel; eine Teilung nach `div` brächte nichts. `link_pattern` ist nicht gesetzt: Bei einem Chunk pro Werk gibt es keine Verweise zwischen Chunks, und ohne Muster schreibt OPM relative Links.

## Metadaten der Seitenleiste: Fragmente statt works.json

Die Angaben (Zitierweise, MLA-9, Erschienen in, Sprache, Gattung, swisscovery, DOI, Lizenz) kommen aus `[[chunking.fragments]]` in `opm.toml`. Jedes Fragment ist ein XPath-Ausdruck auf den `teiHeader`, der reinen Text liefert; das Template maskiert ihn.

Begründung:
- **Eine Quelle, ein Durchlauf:** Jede Leseseite holt ihre Angaben direkt aus ihrer TEI-Datei, im selben `opm chunk`-Lauf. `works.json` entsteht erst in Phase 4 und wäre eine zweite Pipeline, von der die Leseseiten abhängen.
- **Für Nicht-Programmierer lesbar:** Was wo herkommt, steht als XPath in `opm.toml` (z. B. `idno[@type = 'MLA-9']`), nicht in Python-Code.
- **Gattungs-Bezeichnung:** `tp:taxonomy_label()` (`extensions/hersch_functions.py`) liest `assets/i18n/taxonomy.json`; so gibt es die Bezeichnungen nur an einer Stelle.
- swisscovery-Link: `idno[@subtype='swisscovery']`, sonst aus `ALMA-MMSID` gebildet (nur 1 von 12 Dateien hat den Link ausgeschrieben).

Nebenwirkung: OPM schreibt jedes globale Fragment zusätzlich als `<name>.html` neben die Seite. `build.py` entfernt diese Dateien wieder.

## Abbildungen

`graphic/@url` (`resources/images/edition/figN.jpg`) wird in `hersch-opm.odd` auf `{prefix}assets/img/edition/figN.jpg` umgeschrieben. Die Webfassungen erzeugt `scripts/prepare_images.py` aus Elias' Scans (225 MB → 24 MB).

## Vergleich mit edition-jeanne-hersch.org (2026-10-15)

Gemessen an 1540 bei 1280 px, Vergleich auch 760, 880, 900, 730. Screenshots in `docs/screenshots/`.

**Übereinstimmend:** Schriften (ES Rebond Grotesque, EB Garamond), Lesetext `clamp(17px, 1rem + 0.281vw, 21px)` / 1.35, Titel `clamp(24px, …, 32px)`, Zwischentitel fett, Farben, Spaltenraster 1 : 2 : 1, Abstände, Seitenzahlen rechts in Grau, gepunktet unterstrichene Personen, Gattungs-Icon und Jahr, mitlaufende Titelzeile, Handy-Ansicht mit Leiste «•••».

**Bewusste Unterschiede:**
| Live | Pilot | Grund |
|---|---|---|
| Fussnoten als Einblendung beim Darüberfahren (730) | Fussnoten am Textende, mit Rücksprung | ohne JavaScript, auch gedruckt und auf dem Handy lesbar; OPM-Standard |
| Export: EPUB, PDF, TEI XML | nur TEI XML | Briefing Phase 3 |
| Abschnitt «Register» | fehlt noch | Phase 5 |
| Abschnitt «Lizenz» fehlt | vorhanden | Briefing Phase 3 |
| DOI `DOI_COMING` wird als Link angezeigt | Platzhalter wird weggelassen | Briefing Phase 3 |
| Personen mit Popover und Link | nur gepunktet unterstrichen | Phase 5 |

**Gleich wie live, aber auffällig:** 900.xml hat keine Titelzeile und keine Seitenzahl 402 (siehe `odd-anpassungen.md`).

## Prüfungen

- 12 Leseseiten, Build ohne Fehler.
- Keine externen Ressourcen: kein `src`/`href` auf `link`, `script`, `img` mit `http(s)://`, kein `url(http…)` und kein `@import` in CSS (Skriptprüfung über `_site/`). Externe Ziele gibt es nur als normale Links (swisscovery, Creative Commons).
- Keine absoluten Pfade (`/…`) in HTML oder CSS.
- Tote Links: nur die Seiten späterer Phasen (`index.html`, `works.html`, `people.html`, `search.html`, `about.html`, `imprint.html`) und `fig28.jpg` (fehlt in den Daten).
