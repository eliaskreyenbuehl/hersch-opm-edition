# Phase 4 – Werkliste mit Filtern, Startseite, Über-Seite

## Ziel
Besucher:innen finden die Texte über eine filterbare Werkliste. Die Startseite führt in die Edition ein.

## Aufgaben

### 1. `scripts/extract_metadata.py` → `_site/data/works.json`
Pro Datei ein Eintrag:
- `id` (Dateiname ohne .xml), `projectId` (`idno[@type='hersc:projectID']`)
- `title`, `subtitle` (aus `sourceDesc//analytic/title`)
- `year` (`imprint/date/@when`), `container` (`monogr/title`), `volume`, `issue`, `pages`
- `lang` (`textLang/@mainLang`)
- `genre`, `worktype`, `keywords[]` (aus `catRef`, ohne `#`)
- `mla`, `doi` (leer, wenn `DOI_COMING`), `swisscovery` (`idno[@type='URI'][@subtype='swisscovery']`)
- `href`: relativer Link zur Leseseite
- `persons[]`: GND-IDs (für Phase 5)

Felder, die fehlen, bleiben leer. Kein Absturz. Aufruf in `build.py` einbauen.

### 2. Werkliste `templates/works.html.j2` → `_site/werke/index.html`
- Liste aller Werke: Titel, Untertitel, Jahr, Zeitschrift, Sprache, Gattung. Sortierbar nach Jahr und Titel.
- Filter: Jahr (von/bis), Gattung, Werktyp, Schlagwort, Sprache. Kombinierbar, mit Trefferzahl pro Option.
- Labels der Kategorien aus `assets/i18n/taxonomy.json`. Fehlt ein Label, wird die ID angezeigt und in der Konsole gewarnt.
- `assets/js/works-filter.js`: Vanilla-JS, lädt `works.json`, filtert clientseitig und schreibt den Filterzustand in die URL (`?genre=article&lang=fra`), damit Links teilbar sind.
- Ohne JavaScript steht die vollständige Liste trotzdem als HTML auf der Seite (serverseitig gerendert).
- Gestaltung nach `templates/vorlage/` (Werkübersicht der Hersch-App) und `tokens.css`.

### 3. Startseite `templates/home.html.j2` → `_site/index.html`
- Aufbau nach `templates/vorlage/home.html` und `landing-page.css`.
- Kennzahlen aus works.json: Anzahl Werke, Zeitspanne (frühestes bis spätestes Jahr), Sprachen.
- Die neuesten bzw. ausgewählten Texte als Kacheln. Elias fragen, welche.
- Hinweis-Banner: «Prototyp – kein offizielles Angebot der ZB». Elias bestätigt den Wortlaut.

### 4. Über-Seite und Impressum
- `templates/about.html.j2` mit Texten aus `about-hersch.html` und `project.html` der Vorlage.
- `templates/imprint.html.j2` aus `imprint.html`. Datenschutz: keine Cookies, kein Tracking.

## Abnahme
- [ ] works.json enthält 12 Einträge, Stichprobe von 3 gegen die TEI-Dateien geprüft.
- [ ] Filter kombinierbar, Trefferzahlen stimmen mit `docs/datenbericht.md` überein.
- [ ] URL mit Filterparametern lädt den richtigen Zustand.
- [ ] Startseite, Über und Impressum im Hersch-Stil, mobil brauchbar.
- [ ] Commit.
