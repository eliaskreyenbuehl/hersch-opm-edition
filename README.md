# Edition Jeanne Hersch – OPM-Pilot

Prototyp der Zentralbibliothek Zürich: eine statische digitale Edition mit 12 Texten von Jeanne Hersch, gebaut mit [Open Processing Model (OPM)](https://opm.e-editiones.org) und Claude Code, veröffentlicht auf GitHub Pages.

**Prototyp – kein offizielles Angebot der ZB.** Die offizielle Edition: https://edition-jeanne-hersch.org

- Prototyp ansehen: https://eliaskreyenbuehl.github.io/hersch-opm-edition/

> **Vorläufige Veröffentlichung (preliminary release).** Dieser Stand dient zum Testen und wird später wieder gelöscht. Einige geplante Teile sind noch nicht umgesetzt:
>
> - **Personenregister** (Phase 5): Die Seite «Personen» ist ein Platzhalter, Personen im Lesetext sind noch nicht verlinkt.
> - **Volltextsuche** (Phase 6): Die Seite «Suche» ist ein Platzhalter. Filtern geht bereits in der Werkliste.
> - **Mehrsprachige Oberfläche** (Phase 6): Die Oberfläche ist nur deutsch, der Sprachumschalter im Menü hat noch keine Funktion.
> - **Biografie und Projektbeschreibung**: Die Texte stehen noch aus und sind als Platzhalter markiert.
> - **Barrierefreiheit**: Sie wurde für diesen Testaufbau nicht geprüft.
> - Eine Abbildung in «Chagall à travers quelques toiles» (`fig28.jpg`) fehlt, siehe [docs/datenbericht.md](docs/datenbericht.md).

## Worum es geht

Das Projekt soll zeigen, dass sich eine TEI-Edition ohne Datenbank und ohne Server in wenigen Tagen in-house umsetzen lässt.

- **OPM statt TEI Publisher:** Die offizielle Edition läuft auf TEI Publisher 10 mit einer eXist-Datenbank. Die Jinntec-Edition «When the Wall Came Down» nutzt TEI Publisher 11. OPM ist ein eigenständiges Python-Werkzeug (`pip install open-processing-model`), braucht keine Datenbank und kann ODDs verwenden, die mit TEI Publisher kompatibel sind.
- **Wiederverwendung:** Die Hersch-ODD (`odd/hersch.odd`, ergänzt durch `odd/hersch-opm.odd`) und das Design der offiziellen Edition werden übernommen. Was woher stammt, steht in [docs/herkunft.md](docs/herkunft.md).
- **Ergebnis:** Statisches HTML mit Startseite, Werkliste mit Filtern und 12 Leseansichten, dazu der TEI-Download.

Weitere Dokumente:

- Vorgehen für Menschen: [ANLEITUNG.md](ANLEITUNG.md)
- Regeln für Claude Code: [CLAUDE.md](CLAUDE.md)
- Phasen, Entscheidungen, Berichte: [docs/](docs/)
- Aufwand und Erfahrungen: [docs/beweisprotokoll.md](docs/beweisprotokoll.md)

## Bauen und ansehen

Voraussetzung ist [uv](https://docs.astral.sh/uv/). Es installiert Python und alle Pakete in der Version aus `uv.lock`.

```bash
uv sync                                  # Abhängigkeiten installieren
uv run python scripts/build.py           # ganze Site nach _site/ bauen
uv run opm serve -d _site                # ansehen unter http://127.0.0.1:8080
```

`uv run python scripts/check_links.py` findet tote Links. Bei jedem Push auf `main` baut GitHub Actions die Site neu und veröffentlicht sie (`.github/workflows/pages.yml`).

## Aufbau

```
data/              TEI-Dateien (nur lesen, Korrekturen in Oxygen)
odd/               hersch.odd, teipublisher.odd, hersch-opm.odd (Anpassungen für OPM)
opm.toml           OPM-Konfiguration (Leseansicht, Metadaten der Seitenleiste)
templates/         Jinja2-Vorlagen: Seitengerüst, Leseansicht, Start, Werkliste, Textseiten
content/           Texte der Seiten Start, Jeanne Hersch, Projekt, Impressum, Datenschutz
assets/css/        tokens.css (nur Gestaltungswerte), layout.css, text.css, pages.css
assets/js/         works-filter.js (Filter der Werkliste)
assets/fonts/      Schriften, assets/img/ Bilder und Symbole
scripts/           build.py, validate.py, extract_metadata.py, render_pages.py, check_links.py
docs/              Phasen-Briefings, Entscheidungen, Datenbericht, Beweisprotokoll
_site/             Build-Ausgabe (nicht eingecheckt)
```

Ein neues Design muss nur `assets/css/tokens.css` und die Templates ersetzen.

## Technik

| Werkzeug | Version |
|---|---|
| Python | 3.12 |
| open-processing-model (opm) | 0.9.0 |
| uv | 0.13.1 |

Die genauen Versionen aller Python-Pakete hält `uv.lock` fest.

## Lizenzen

- **Code** (Skripte, Templates, CSS, JavaScript): MIT, siehe [LICENSE](LICENSE)
- **Texte** in `data/`: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.de)
- **Schriften:** EB Garamond, Inter und Junicode unter SIL Open Font License (Lizenzdateien in `assets/fonts/`). **ES Rebond Grotesque ist kommerziell lizenziert** (Webfont-Lizenz der ZB für diese Website). Sie fällt nicht unter die MIT-Lizenz und darf nicht weiterverwendet werden.
- **Bilder:** Porträt und Faksimiles: Zentralbibliothek Zürich
