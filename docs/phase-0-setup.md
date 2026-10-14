# Phase 0 – Werkzeuge einrichten

## Ziel
Auf Elias' Windows-11-Rechner laufen Git, die GitHub-CLI (`gh`), `uv` und OPM. Das Projekt ist ein Git-Repo mit `pyproject.toml`.

## Ausgangslage
- Python 3.12.10 ist installiert, Git und ein GitHub-Konto sind vorhanden.
- Im Projektordner liegen nur `CLAUDE.md`, `ANLEITUNG.md`, `README.md` und `docs/`.

## Aufgaben
1. Prüfen, was schon da ist: `python --version`, `git --version`, `gh --version`, `uv --version`.
2. Fehlendes installieren, und zwar nur das: `winget install --id GitHub.cli` bzw. `winget install --id astral-sh.uv`. Nach der Installation ist eventuell ein neues Terminal nötig. Erkläre Elias das.
3. **Elias selbst** meldet sich bei GitHub an. Gib ihm den Befehl `gh auth login` zum Ausführen in einem eigenen Terminal und erkläre die Auswahl (GitHub.com → HTTPS → Login with a web browser). Führe ihn nicht selbst aus.
4. Im Projektordner:
   - `git init -b main`
   - `uv init --bare` (oder `uv init` und überflüssige Beispieldateien wieder entfernen), Projektname `hersch-opm-edition`, Python `>=3.12`
   - `uv add open-processing-model "pagefind[extended]" lxml jinja2 requests`
   - `.gitignore` mit `_site/`, `.venv/`, `__pycache__/`, `*.pyc`
5. Funktionstest mit einer Beispieldatei aus der Hersch-App oder aus Elias' Ordner:
   `uv run opm transform <pfad>/60.xml -o _site/test.html` (ohne `--preview`). Danach `_site/test.html` im eingebauten Browser öffnen.
6. Installierte Versionen (opm, pagefind, Python) in `README.md` unter «Technik» notieren.
7. Commit: «Projekt eingerichtet: uv, OPM, Pagefind».

## Abnahme
- [ ] `uv run opm --help` zeigt die Befehle.
- [ ] `gh auth status` zeigt Elias' Konto. Elias führt das aus und meldet es.
- [ ] 60.xml wurde mit der Standard-ODD in HTML umgewandelt und ist lesbar.
- [ ] Erster Commit vorhanden.

## Nicht in dieser Phase
Keine ODD-Anpassung, kein Design, kein GitHub-Repo anlegen.
