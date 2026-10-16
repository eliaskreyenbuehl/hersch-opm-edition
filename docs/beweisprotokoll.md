# Beweisprotokoll

Behauptung: Eine digitale Edition lässt sich mit Open Processing Model und Claude Code in-house und schnell hochziehen, ohne Datenbank, ohne Server und ohne Programmierkenntnisse.

Pro Phase ausfüllen (Claude trägt am Ende der Sitzung einen Entwurf ein, Elias ergänzt).

| Phase | Datum | Dauer (Std.) | Sitzungen / Prompts | Was Claude allein schaffte | Wo es hakte | Wo menschliches Urteil nötig war |
|---|---|---|---|---|---|---|
| 0 Setup | 2026-10-14 | ca. 0,5 (22:03–22:35) | 1 Sitzung, ca. 10 Prompts | uv-Projekt, Abhängigkeiten, Git-Repo, Test-Transformation von 60.xml mit Standard-ODD, Browserprüfung | `winget install` scheiterte an fehlenden Admin-Rechten → `gh` und `uv` als portable ZIPs nach `%USERPROFILE%\.local\bin`; `opm transform -o` legt Zielordner nicht selbst an | GitHub-Anmeldung (Elias); Fundort der TEI-Dateien |
| 1 Daten & Design | 2026-10-14 | ca. 0,75 | 1 Sitzung, ca. 5 Prompts | validate.py mit Datenbericht (Pflichtfelder, GND-Format, Taxonomie-Abgleich, Element-/Attributstatistik); ODD inkl. referenzierter tp.css, CSS, Schriften, i18n, Bilder, Templates kopiert; taxonomy.json aus i18n abgeleitet; herkunft.md | Lesezugriff auf die Hersch-App musste erst mit `/add-dir` freigegeben werden (erster Versuch mit falschem Pfad); `zbz_hersch.rng` und `hersch_taxonomy.xml` nicht im App-Paket; Lizenzdateien für Inter/Junicode fehlen | Platzhalter `GND-GND_id`, Schlagwort `bildende-kuenste` ohne Label, Lizenz ES Rebond Grotesque, Bildrechte portrait.jpg |
| 2 ODD | 2026-10-14 | ca. 1 (22:55–23:55) | gleiche Sitzung wie Phase 1 (auf Wunsch von Elias), ca. 3 Prompts | Ursache des leeren Textbereichs gefunden (XQuery-Elementkonstruktor in `div`), `hersch-opm.odd` mit 5 Elementen, alle 12 Dateien fehlerfrei (`--strict`), Coverage ohne Lücken, 5 Stichproben per Prüfsumme textgleich mit der Live-Edition | Erste Ausgabe war fast leer (nur Titel); Live-Seite im Browser für Screenshots zu schwer, deshalb Textvergleich per JavaScript; Windows-Konsole braucht `PYTHONIOENCODING=utf-8` | Nachlieferung der Abbildungen (Elias) |
| 3 Leseansicht | 2026-10-15/16 | ca. 3 (15.10. ab ca. 07:20; Abschluss 16.10.) | 1 Sitzung, ca. 5 Prompts | Live-Seite per JavaScript vermessen (Schriftgrössen, Abstände, Farben) und Desktop/Handy nachgebaut; CSS in tokens/layout/text getrennt; Metadaten der Seitenleiste als OPM-Fragmente direkt aus dem teiHeader; Abbildungen von 225 auf 24 MB verkleinert; build.py; Prüfung auf externe Quellen, absolute und tote Links | ODD-Klasse `.center` zentrierte den ganzen Text (von Elias im Browser bemerkt, schon behoben); OPM schreibt Fragmente zusätzlich als Einzeldateien (build.py räumt auf); Chrome lässt Fenster nicht unter ~500 px → Handy-Vergleich im 375-px-Rahmen; Chrome reagierte zwischendurch nicht | Zitierweise wie live, Aufbau der Seitenleiste, Umgang mit den Bildscans, Bildordner |
| 4 Werkliste | | | | | | |
| 5 Register | | | | | | |
| 6 Suche & Sprachen | | | | | | |
| 7 Veröffentlichen | | | | | | |
| **Total** | | | | | | |

## Vergleich

| | Hersch (TEI Publisher 10, Jinntec) | Pilot (OPM, Claude Code) |
|---|---|---|
| Zeit Frontend | | |
| Externe Kosten | | |
| Hosting | eXist-Server | GitHub Pages (statisch) |
| Wer kann es warten? | | |

## Fazit (5–10 Sätze, am Ende)

