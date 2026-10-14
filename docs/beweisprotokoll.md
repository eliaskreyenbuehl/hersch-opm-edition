# Beweisprotokoll

Behauptung: Eine digitale Edition lässt sich mit Open Processing Model und Claude Code in-house und schnell hochziehen, ohne Datenbank, ohne Server und ohne Programmierkenntnisse.

Pro Phase ausfüllen (Claude trägt am Ende der Sitzung einen Entwurf ein, Elias ergänzt).

| Phase | Datum | Dauer (Std.) | Sitzungen / Prompts | Was Claude allein schaffte | Wo es hakte | Wo menschliches Urteil nötig war |
|---|---|---|---|---|---|---|
| 0 Setup | 2026-10-14 | ca. 0,5 (22:03–22:35) | 1 Sitzung, ca. 10 Prompts | uv-Projekt, Abhängigkeiten, Git-Repo, Test-Transformation von 60.xml mit Standard-ODD, Browserprüfung | `winget install` scheiterte an fehlenden Admin-Rechten → `gh` und `uv` als portable ZIPs nach `%USERPROFILE%\.local\bin`; `opm transform -o` legt Zielordner nicht selbst an | GitHub-Anmeldung (Elias); Fundort der TEI-Dateien |
| 1 Daten & Design | | | | | | |
| 2 ODD | | | | | | |
| 3 Leseansicht | | | | | | |
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

