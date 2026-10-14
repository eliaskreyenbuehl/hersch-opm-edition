# Phase 7 – Veröffentlichung auf GitHub Pages

## Ziel
Die Edition ist öffentlich unter `https://<konto>.github.io/hersch-opm-edition/` erreichbar. Bei jedem Push baut sie sich automatisch neu.

## Aufgaben

### 1. Qualitätscheck vor der Veröffentlichung
- `scripts/check_links.py`: alle `href`/`src` in `_site` prüfen. Interne Links müssen auf existierende Dateien zeigen, absolute Pfade (`/…`) gelten als Fehler.
- Lokal mit einem Unterpfad testen, damit sich GitHub Pages simulieren lässt: `_site` nach `_test/hersch-opm-edition/` kopieren, `python -m http.server -d _test`, dann `http://localhost:8000/hersch-opm-edition/` durchklicken.
- Lighthouse oder eine Barrierefreiheits-Stichprobe auf Start, Werkliste und Leseseite (Kontraste, Alt-Texte, Überschriften-Hierarchie, Tastaturbedienung).
- `404.html` im Hersch-Stil.

### 2. Repo-Dateien
- `README.md`: Was ist das? Einordnung OPM vs. TEI Publisher 11. Live-Link, Build-Anleitung (3 Befehle), Projektstruktur, Herkunft der Bausteine (Verweis auf `docs/herkunft.md`), Hinweis «Prototyp, kein offizielles Angebot der ZB».
- `LICENSE`: Code MIT. Hinweis im README: Daten in `data/` unter CC BY-SA 4.0, Schriften unter OFL.
- `.github/workflows/pages.yml`:
  - Trigger: Push auf `main` und manuell (`workflow_dispatch`)
  - Schritte: `actions/checkout`, `astral-sh/setup-uv`, `uv sync`, `uv run python scripts/build.py --offline`, `actions/configure-pages`, `actions/upload-pages-artifact` (Pfad `_site`), `actions/deploy-pages`
  - Rechte: `pages: write`, `id-token: write`
- Action-Versionen fixieren, alle aktuell und mindestens zwei Wochen alt.

### 3. Veröffentlichen – NUR nach ausdrücklichem OK von Elias
Elias fragen: «Darf ich das Repo jetzt öffentlich auf GitHub anlegen und pushen?» Erst nach seinem Ja:
```bash
gh repo create hersch-opm-edition --public --source . --push
gh api -X POST repos/{owner}/hersch-opm-edition/pages -f build_type=workflow
```
Dann den Actions-Lauf verfolgen (`gh run watch`), bis er grün ist.

### 4. Abschluss
- Live-URL auf Laptop und Handy prüfen (Elias).
- `docs/beweisprotokoll.md` vervollständigen: Gesamtdauer, Anzahl Sitzungen, wo Claude scheiterte, wo menschliches Urteil nötig war. Dazu ein Fazit von 5–10 Sätzen für die interne Kommunikation.

## Abnahme
- [ ] Der GitHub-Actions-Lauf ist grün.
- [ ] Die öffentliche URL funktioniert: Start, Werkliste mit Filtern, alle 12 Leseseiten, Register, Suche, Sprachwechsel.
- [ ] Der Link-Check meldet 0 tote interne Links.
- [ ] Accessibility-Stichprobe ohne schwere Mängel.
- [ ] Beweisprotokoll ausgefüllt.
