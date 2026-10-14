# Edition Jeanne Hersch – OPM-Pilot

Prototyp der Zentralbibliothek Zürich: eine statische digitale Edition mit 12 Texten von Jeanne Hersch. Gebaut ist sie mit [Open Processing Model](https://opm.e-editiones.org) und Claude Code, veröffentlicht auf GitHub Pages. **Kein offizielles Angebot der ZB.** Die offizielle Edition: https://edition-jeanne-hersch.org

## Worum es geht

Das Projekt soll zeigen, dass sich eine TEI-Edition ohne Datenbank und Server in wenigen Tagen in-house umsetzen lässt. Die Hersch-ODD und das Design der offiziellen Edition (TEI Publisher 10) werden wiederverwendet. Zum Vergleich: Die Jinntec-Edition «When the Wall Came Down» entstand mit TEI Publisher 11 auf eXist.

- Vorgehen für Menschen: [ANLEITUNG.md](ANLEITUNG.md)
- Regeln für Claude Code: [CLAUDE.md](CLAUDE.md)
- Phasen: [docs/](docs/)
- Ergebnis und Aufwand: [docs/beweisprotokoll.md](docs/beweisprotokoll.md)

## Status

Phase 0 (Setup) abgeschlossen. Als Nächstes: Phase 1 (Daten & Design).

## Technik

| Werkzeug | Version |
|---|---|
| Python | 3.12.10 |
| open-processing-model (opm) | 0.9.0 |
| pagefind (extended) | 1.5.2 |
| uv | 0.13.1 |
| GitHub CLI (gh) | 2.102.0 |

Die genauen Versionen aller Python-Pakete hält `uv.lock` fest. `gh` und `uv` liegen ohne Admin-Rechte als portable Programme in `%USERPROFILE%\.local\bin`.

## Lizenzen

Texte in `data/`: CC BY-SA 4.0 · Code: MIT · Schriften: SIL Open Font License
