# Phase 3 – Seitenrahmen und Leseansicht im Hersch-Design

## Ziel
Jeder Text hat eine eigene Leseseite, die aussieht wie auf edition-jeanne-hersch.org: Kopf, Menü, Lesetext, Metadatenbox und Fuss. Gebaut wird mit `opm chunk`.

## Vorher lesen
- https://opm.e-editiones.org/guide/chunking/
- https://opm.e-editiones.org/guide/templates-and-css/
- OPM-Beispiel `serafin` (`opm init --example serafin` in einem Temp-Ordner): wie `templates/*.j2`, Assets und Index zusammenspielen.
- `templates/vorlage/` und `assets/css/vorlage/` aus Phase 1.

## Aufgaben

### CSS-Architektur (für das spätere Agentur-Redesign)
- `assets/css/tokens.css`: **nur** CSS-Variablen für Farben, Schriftfamilien, Schriftgrössen, Zeilenhöhen, Abstände und Breiten. Werte aus `vorlage/theme.json` und `vorlage/hersch.css`.
- `assets/css/layout.css`: Seitenrahmen (Kopf, Menü, Spalten, Fuss, mobile Ansicht), nutzt nur Variablen aus `tokens.css`.
- `assets/css/text.css`: Lesetext (Seitenzahlen am Rand, Korrekturen, Leerraum, Personen). Ergänzt die ODD-CSS von OPM.
- `assets/fonts/fonts.css`: lokale `@font-face` für die OFL-Schriften.
- Aus `hersch.css` nur übernehmen, was wirklich gebraucht wird. Kein Jinks- oder Pico-Ballast.

### Templates (Jinja2)
- `templates/base.html.j2`: HTML-Gerüst, Kopf mit Logo und Menü (Start, Werke, Personen, Suche, Über), Sprachumschalter DE/FR/EN (Funktion in Phase 6, jetzt nur Markup mit `data-i18n`), Fuss mit Impressum, Lizenz CC BY-SA 4.0 und «Zentralbibliothek Zürich».
- `templates/chunk.html.j2` erbt von base:
  - Hauptspalte: `{{ content_html | safe }}`, ODD-CSS über `<style>{{ odd_css }}</style>`
  - Seitenleiste «Zum Text»: Zitiervorschlag (MLA aus `idno[@type='MLA-9']`), Erschienen in (Zeitschrift, Jg., Heft, Seiten), Sprache, Gattung, swisscovery-Link, DOI (falls nicht `DOI_COMING`), Lizenz, **Download TEI-XML** (die Quelldatei mit nach `_site/edition/xml/` kopieren)
  - Vor/Zurück, falls ein Text mehrere Chunks hat
- Metadaten für die Seitenleiste per Fragment aus dem `teiHeader` holen oder (einfacher) aus `works.json`. Entscheide, was mit OPM sauberer geht, und begründe es kurz.

### `opm.toml` – Chunking
```toml
[chunking]
xpath = "//text"              # kurze Texte: ein Chunk pro Werk; prüfen, ob lange Texte nach div geteilt werden sollen
output_dir = "_site/edition"
template = "templates/chunk.html.j2"
link_pattern = "{doc_stem}/{stem}.html"   # RELATIV – keine führenden Schrägstriche!
assets = ["assets/css/*.css", "assets/fonts", "assets/img"]
```
Werte mit `opm chunk --help` und der Doku abgleichen, nicht blind übernehmen.

### `scripts/build.py` (erste Version)
Ruft `validate.py` auf, dann `opm chunk data -o _site/edition --force` und kopiert die XML-Quellen. Weitere Schritte folgen in späteren Phasen.

## Abnahme
- [ ] `uv run python scripts/build.py` erzeugt 12 Leseseiten.
- [ ] 60.xml lokal und Live-Seite nebeneinander: Schrift, Farben, Abstände, Seitenzahlen und Korrekturen stimmen weitgehend überein. Screenshots Desktop (1280 px) und Handy (375 px) in `docs/screenshots/` ablegen.
- [ ] Keine Datei lädt etwas von externen Servern (in der Netzwerkansicht prüfen).
- [ ] Alle Links relativ.
- [ ] Commit.
