# Beweisprotokoll

Behauptung: Eine digitale Edition lässt sich mit Open Processing Model und Claude Code in-house und schnell hochziehen, ohne Datenbank, ohne Server und ohne Programmierkenntnisse.

Pro Phase ausfüllen (Claude trägt am Ende der Sitzung einen Entwurf ein, Elias ergänzt).

| Phase | Datum | Dauer (Std.) | Sitzungen / Prompts | Was Claude allein schaffte | Wo es hakte | Wo menschliches Urteil nötig war |
|---|---|---|---|---|---|---|
| 0 Setup | 2026-10-14 | ca. 0,5 (22:03–22:35) | 1 Sitzung, ca. 10 Prompts | uv-Projekt, Abhängigkeiten, Git-Repo, Test-Transformation von 60.xml mit Standard-ODD, Browserprüfung | `winget install` scheiterte an fehlenden Admin-Rechten → `gh` und `uv` als portable ZIPs nach `%USERPROFILE%\.local\bin`; `opm transform -o` legt Zielordner nicht selbst an | GitHub-Anmeldung (Elias); Fundort der TEI-Dateien |
| 1 Daten & Design | 2026-10-14 | ca. 0,75 | 1 Sitzung, ca. 5 Prompts | validate.py mit Datenbericht (Pflichtfelder, GND-Format, Taxonomie-Abgleich, Element-/Attributstatistik); ODD inkl. referenzierter tp.css, CSS, Schriften, i18n, Bilder, Templates kopiert; taxonomy.json aus i18n abgeleitet; herkunft.md | Lesezugriff auf die Hersch-App musste erst mit `/add-dir` freigegeben werden (erster Versuch mit falschem Pfad); `zbz_hersch.rng` und `hersch_taxonomy.xml` nicht im App-Paket; Lizenzdateien für Inter/Junicode fehlen | Platzhalter `GND-GND_id`, Schlagwort `bildende-kuenste` ohne Label, Lizenz ES Rebond Grotesque, Bildrechte portrait.jpg |
| 2 ODD | 2026-10-14 | ca. 1 (22:55–23:55) | gleiche Sitzung wie Phase 1 (auf Wunsch von Elias), ca. 3 Prompts | Ursache des leeren Textbereichs gefunden (XQuery-Elementkonstruktor in `div`), `hersch-opm.odd` mit 5 Elementen, alle 12 Dateien fehlerfrei (`--strict`), Coverage ohne Lücken, 5 Stichproben per Prüfsumme textgleich mit der Live-Edition | Erste Ausgabe war fast leer (nur Titel); Live-Seite im Browser für Screenshots zu schwer, deshalb Textvergleich per JavaScript; Windows-Konsole braucht `PYTHONIOENCODING=utf-8` | Nachlieferung der Abbildungen (Elias) |
| 3 Leseansicht | 2026-10-15/16 | ca. 3 (15.10. ab ca. 07:20; Abschluss 16.10.) | 1 Sitzung, ca. 5 Prompts | Live-Seite per JavaScript vermessen (Schriftgrössen, Abstände, Farben) und Desktop/Handy nachgebaut; CSS in tokens/layout/text getrennt; Metadaten der Seitenleiste als OPM-Fragmente direkt aus dem teiHeader; Abbildungen von 225 auf 24 MB verkleinert; build.py; Prüfung auf externe Quellen, absolute und tote Links | ODD-Klasse `.center` zentrierte den ganzen Text (von Elias im Browser bemerkt, schon behoben); OPM schreibt Fragmente zusätzlich als Einzeldateien (build.py räumt auf); Chrome lässt Fenster nicht unter ~500 px → Handy-Vergleich im 375-px-Rahmen; Chrome reagierte zwischendurch nicht | Zitierweise wie live, Aufbau der Seitenleiste, Umgang mit den Bildscans, Bildordner |
| 4 Werkliste | 2026-10-16 | ca. 2 | 1 Sitzung, ca. 4 Prompts | Live-Startseite und -Werkliste angesehen und vermessen; `extract_metadata.py` (works.json, Aliase, GND normalisiert); Werkliste mit kombinierbaren Filtern, Zahlen pro Option, Zustand in der Adresse, ohne JavaScript vollständige Liste; Startseite, Jeanne Hersch, Projekt, Impressum; `check_links.py`; Handy-Prüfung im 375-px-Rahmen | Texte für Einführung, Biografie, Projekt und Impressum fehlen im App-Paket (`auxiliary/content-webpages/`) → Platzhalter; Browser zeigte zuerst altes CSS aus dem Cache; lxml kennt nur XPath 1.0 | Aufbau der Startseite (ohne Aphorismen/Themen), Werkliste als eigene Seite, Kacheln, Wortlaut Prototyp-Hinweis, Lieferung der Seitentexte |
| 5 Register | – | – | – | übersprungen (Entscheid 2026-10-16), Platzhalterseite | | |
| 6 Suche & Sprachen | – | – | – | übersprungen (Entscheid 2026-10-16), Platzhalterseite | | |
| 7 Veröffentlichen | 2026-10-16 | ca. 0,75 | gleiche Sitzung wie Phase 4, ca. 4 Prompts | Workflow mit fest verankerten Action-Versionen, 404-Seite für Unterordner, README/LICENSE, Test unter Unterpfad, Repo angelegt, Pages aktiviert, erster Lauf grün (Build 22 s, Deploy 10 s), Prüfung der öffentlichen Site (20 Seiten, 91 Dateien) | fehlende Abbildung `fig28.jpg` hätte den Link-Check blockiert → als Datenhinweis eingestuft | Freigabe zur Veröffentlichung, Lizenzfrage der kommerziellen Schrift im öffentlichen Repo; Verzicht auf Barrierefreiheitsprüfung |
| **Total** | 14.–16.10.2026 | ca. 8 | 4 Sitzungen, ca. 30 Prompts | ohne Phase 5 und 6 | | |

## Vergleich

| | Hersch (TEI Publisher 10, Jinntec) | Pilot (OPM, Claude Code) |
|---|---|---|
| Zeit Frontend | (Elias ergänzt) | ca. 8 Std. bis zur öffentlichen Vorabversion (ohne Register, Suche, Mehrsprachigkeit) |
| Externe Kosten | (Elias ergänzt) | keine für Hosting; Claude-Code-Abo |
| Hosting | eXist-Server | GitHub Pages (statisch) |
| Wer kann es warten? | (Elias ergänzt) | wer TEI kennt und Python-Befehle nach Anleitung ausführt; Texte in `content/`, Gestaltung in `tokens.css` |

## Fazit (5–10 Sätze, am Ende)

*Entwurf von Claude, von Elias zu prüfen und zu ergänzen:*

In rund acht Stunden über drei Tage ist aus 12 TEI-Dateien und den Bausteinen der bestehenden Hersch-App eine öffentlich erreichbare, statische Edition entstanden: Startseite, filterbare Werkliste und Leseansichten im Design der offiziellen Edition, ohne Datenbank und ohne Server. Die Hersch-ODD liess sich mit wenigen Anpassungen in OPM weiterverwenden; die Texte sind in Stichproben textgleich mit der Live-Edition. Claude Code hat Programmierung, Gestaltung nach Messung der Live-Seite, Prüfung im Browser und Veröffentlichung weitgehend selbständig erledigt. Menschliches Urteil war bei editorischen und gestalterischen Fragen nötig (Aufbau der Startseite, Zitierweise, Umgang mit Datenfehlern), bei Rechtsfragen (Schriftlizenz, Bildrechte, Impressum) und bei der Freigabe zur Veröffentlichung. Gehakt hat es vor allem an fehlenden Quellen (Inhaltsdateien der Seiten, Schema, eine Abbildung) und an Eigenheiten der Windows-Umgebung. Personenregister, Volltextsuche und Mehrsprachigkeit sind vorbereitet, aber zurückgestellt; sie wären die nächsten Schritte, um die Vorabversion zu einer vollständigen Edition auszubauen.
