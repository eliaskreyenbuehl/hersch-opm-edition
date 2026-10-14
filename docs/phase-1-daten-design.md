# Phase 1 – Daten und Design-Bausteine übernehmen

## Ziel
Die 12 TEI-Dateien und alle wiederverwendbaren Teile der Hersch-App liegen im Projekt. Ein Datenbericht zeigt, was in den Dateien fehlt oder uneinheitlich ist.

## Aufgaben

### 1. TEI-Daten
- Elias nach dem Quellordner der 12 TEI-Dateien fragen und sie nach `data/` kopieren. Dateinamen bleiben gleich, z. B. `1540.xml`.
- Falls Elias das Schema `zbz_hersch.rng` hat, nach `schema/` kopieren.

### 2. Aus der Hersch-App kopieren
Quelle: `C:\Users\krey\Downloads\hersch-png\zbz-hersch-app-main`

| Von | Nach |
|---|---|
| `resources/odd/hersch.odd`, `teipublisher.odd` (+ was hersch.odd per `source` referenziert, prüfen!) | `odd/` |
| `resources/css/hersch.css`, `landing-page.css`, `jinks-variables.css` | `assets/css/vorlage/` (Rohmaterial, wird in Phase 3 verarbeitet) |
| `config.json` → Abschnitt `theme` | `assets/css/vorlage/theme.json` |
| `resources/fonts/` (EB Garamond, Inter, Junicode + Lizenzdateien) | `assets/fonts/` |
| `resources/i18n/app/de.json`, `fr.json`, `en.json` | `assets/i18n/vorlage/` |
| Logo, Favicon (`resources/images/`, im Layout-Template suchen, wo das Logo herkommt) | `assets/img/` |
| `templates/layouts/hersch-base.html`, `hersch-content.html`, `hersch-home-base.html`, `home.html`, `about-hersch.html`, `project.html`, `imprint.html`, `people.html`, `person.html`, `hersch-menu.html`, `footer.html` | `templates/vorlage/` (nur als Referenz) |

- **ES Rebond Grotesque NICHT kopieren**, solange Elias die Lizenz nicht bestätigt hat. Frag ihn, ob sie für github.io gilt.
- In `docs/herkunft.md` festhalten, welche Datei woher kommt.

### 3. Taxonomien finden
Die TEI-Dateien verweisen mit `catRef @scheme="hersch_genre|hersch_worktype|hersch_keywords" @target="#…"` auf Kategorien. Suche die Definitionen (`taxonomy`/`category`/`catDesc`) in der Hersch-App: `grep -r "hersch_genre"` und `catDesc` in `data`, `modules`, `templates`, `resources`. Gefundenes nach `assets/i18n/taxonomy.json` übertragen (Schlüssel = ID, Werte = Label de/fr/en). Was fehlt, als Entwurf markieren (`"_entwurf": true`).

### 4. `scripts/validate.py`
- Prüft jede Datei in `data/`: Wohlgeformtheit (lxml). Falls ein Schema vorhanden ist, gegen das RNG.
- Pflichtfelder: Haupttitel (`titleStmt/title[@type='item'][@subtype='main']`), Jahr (`sourceDesc//imprint/date/@when`), Projekt-ID (`idno[@type='hersc:projectID']`), Sprache (`textLang/@mainLang`), mindestens ein `catRef` je Schema, Lizenz.
- Statistik: welche Elemente und Attribute in `text` vorkommen (Anzahl je Datei). Die braucht Phase 2.
- Ausgabe: `docs/datenbericht.md` (Tabelle je Datei, Liste der Abweichungen, Element-Statistik). Exit-Code 1 nur bei nicht wohlgeformtem XML.

## Abnahme
- [ ] 12 Dateien in `data/`, alle wohlgeformt.
- [ ] Bausteine kopiert, `docs/herkunft.md` vorhanden.
- [ ] `docs/datenbericht.md` vorhanden und Elias vorgelegt. Er entscheidet über Abweichungen, Claude korrigiert nichts.
- [ ] `assets/i18n/taxonomy.json` vorhanden (ggf. als Entwurf).
- [ ] Commit.
