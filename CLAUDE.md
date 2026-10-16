# CLAUDE.md – Hersch-Edition mit Open Processing Model (OPM)

Diese Datei gilt für jede Claude-Code-Sitzung in diesem Ordner. Lies sie vollständig, bevor du etwas tust.

## Ziel

Eine **statische** digitale Edition mit 12 Texten von Jeanne Hersch (Pilot, später 100+), gebaut mit **Open Processing Model (OPM)** und veröffentlicht auf **GitHub Pages**. Das Projekt soll beweisen, dass die ZB eine Edition in-house mit Claude Code in wenigen Tagen hochziehen kann, ohne Datenbank und ohne Server.

Zur Einordnung: Die Jinntec-Edition «When the Wall Came Down» lief auf TEI Publisher 11 mit eXist. OPM ist ein eigenständiges Python-Werkzeug (`pip install open-processing-model`). Es braucht keine Datenbank, und seine ODDs sind mit TEI Publisher kompatibel.

## Wer mit dir arbeitet

Elias (ZB Zürich, Projektleitung Hersch-Edition) ist **kein Programmierer**. Er kennt TEI und das Editionsgeschäft sehr gut.
- Erkläre vor jedem Befehl, den Elias selbst ausführen muss, in einem Satz, was er tut. Gib ihn in einem eigenen Codeblock aus.
- Anmeldungen (`gh auth login`, Passwörter, Tokens) macht **immer Elias selbst**.
- Fachbegriffe aus der Programmierung kurz erklären, TEI-Begriffe nicht.
- Antworten auf Deutsch.

## Arbeitsweise

- Pro Sitzung genau **eine Phase** aus `docs/phase-N-*.md`. Arbeite sie ab, bis die Abnahmekriterien erfüllt sind, und hör dann auf. Mit der nächsten Phase fängst du nicht an.
- Prüfe deine Arbeit selbst: Build laufen lassen, Seiten im eingebauten Browser öffnen, Screenshots vergleichen.
- Am Ende jeder Phase:
  1. `git add` + `git commit` mit deutscher, verständlicher Nachricht.
  2. In `docs/beweisprotokoll.md` die Zeile der Phase ausfüllen: Dauer, was gut ging, wo es hakte.
  3. Elias eine kurze Liste **«Bitte prüfen»** geben (konkrete URLs und worauf achten).
- Wenn eine Entscheidung editorisch oder gestalterisch ist, fragst du. Nicht selbst entscheiden.

## Quellen (nicht raten)

- **OPM-Doku:** https://opm.e-editiones.org (Guides: Chunking, Configuration, Templates & CSS, ODD files, ODD coverage, Search indexing), dazu `uv run opm --help` und `uv run opm <befehl> --help`. Bei Unklarheiten den Quellcode lesen: https://github.com/eeditiones/open-processing-model, die Beispiele unter `examples/` (v. a. `serafin`).
- **Design und ODD:** ausschliesslich die lokale Hersch-App unter `C:\Users\krey\Downloads\hersch-png\zbz-hersch-app-main`. Daraus kopieren und anpassen, nichts neu erfinden.
  - ODD: `resources/odd/hersch.odd` (erbt von `teipublisher.odd`)
  - CSS: `resources/css/hersch.css`, `landing-page.css`, `jinks-variables.css`; Theme-Werte in `config.json` → `theme`
  - Schriften: `resources/fonts/`
  - UI-Texte: `resources/i18n/app/{de,fr,en}.json`
  - Seitenaufbau: `templates/layouts/hersch-*.html`, `templates/home.html`, `about-hersch.html`, `project.html`, `imprint.html`, `people.html`, `person.html`. Übernommen werden Struktur und Texte, nicht die TEI-Publisher-Templating-Syntax.
- **Referenz für das Aussehen:** https://edition-jeanne-hersch.org/edition/1540.xml. Nur ansehen und vergleichen, nichts herunterladen oder scrapen.

## Architektur

```
hersch-opm-edition/
├─ CLAUDE.md, ANLEITUNG.md, README.md, LICENSE
├─ pyproject.toml          Abhängigkeiten (uv), Versionen fixiert
├─ opm.toml                OPM-Konfiguration
├─ data/                   TEI-Dateien – NUR LESEN
├─ odd/                    hersch.odd, teipublisher.odd, hersch-opm.odd (eigene Anpassungen)
├─ templates/              Jinja2: base, chunk, works, home, about, imprint, people, person, search
├─ assets/
│  ├─ css/                 tokens.css (nur Variablen), layout.css, hersch.css (übernommen)
│  ├─ fonts/               nur OFL-Schriften (+ Lizenzdateien)
│  ├─ js/                  works-filter.js, i18n.js
│  └─ i18n/                de.json, fr.json, en.json, taxonomy.json
├─ scripts/                build.py, validate.py, extract_metadata.py, build_register.py, check_links.py
├─ registers/              gnd-cache.json (eingecheckt), people.json
├─ docs/                   Phasen-Briefings, Berichte, Beweisprotokoll
├─ .github/workflows/pages.yml
└─ _site/                  Build-Ausgabe – NICHT einchecken, nie von Hand bearbeiten
```

**Ein Befehl baut alles:** `uv run python scripts/build.py`
1. `validate.py`: Wohlgeformtheit + Pflichtfelder → Bericht
2. `extract_metadata.py` → `_site/data/works.json`
3. `build_register.py` → `registers/people.json` (lobid-gnd, mit Cache)
4. `opm chunk data -o _site/edition --force`: Leseansichten
5. Jinja-Seiten rendern: Start, Werkliste, Personen, Über, Impressum, Suche
6. `python -m pagefind --site _site`: Suchindex

## Verbote

- **Keine TEI-Datei in `data/` verändern.** Datenprobleme kommen in einen Bericht unter `docs/`, korrigiert wird in Oxygen vom Team.
- Keine generierten Dateien in `_site/` von Hand bearbeiten.
- Keine externen CDNs (Schriften, JS, CSS). Alles liegt lokal, aus Datenschutzgründen.
- Kein Node.js, kein Frontend-Framework. Reines HTML/CSS und kleines Vanilla-JS.
- Keine neue Abhängigkeit ohne Eintrag in `pyproject.toml` (`uv add …`).
- **Schrift ES Rebond Grotesque** ist kommerziell lizenziert. Elias hat am 2026-10-14 bestätigt, dass die Webfont-Lizenz für github.io gilt; sie darf eingebunden werden. Die Dateien nicht an andere Orte weitergeben.
- Nichts veröffentlichen (`git push`, `gh repo create`, Pages aktivieren) ohne ausdrückliches OK von Elias im Chat.

## Technische Leitplanken

- **Relative Links überall.** Die Site liegt unter `https://<konto>.github.io/<repo>/`, absolute Pfade wie `/edition/…` brechen dort. In OPM-Templates `{prefix}` verwenden.
- GND-Refs normalisieren: `GND-118557106` und `118557106` meinen dieselbe Person.
- lobid-Abfragen nur über den Cache `registers/gnd-cache.json`. Jede ID wird einmal abgefragt, danach nie wieder. Die CI fragt nichts ab.
- CSS so aufteilen, dass ein späteres Agentur-Design (hermanngermann.ch) nur `tokens.css` und die Templates tauschen muss.

## Befehle

```bash
uv run python scripts/build.py          # alles bauen
uv run opm serve -d _site               # lokal ansehen (http://127.0.0.1:8080)
uv run opm transform data/1540.xml --preview   # einzelnen Text testen
uv run python scripts/check_links.py    # tote Links finden
```
