# Herkunft der übernommenen Dateien

Quelle aller Bausteine: lokale Hersch-App unter `C:\Users\krey\Downloads\hersch-png\zbz-hersch-app-main` (im Folgenden `APP/`). Kopiert am 2026-10-14 (Phase 1), unverändert.

## TEI-Daten

| Im Projekt | Herkunft |
|---|---|
| `data/*.xml` (12 Dateien: 90, 730, 760, 770, 790, 830, 870, 880, 890, 900, 910, 1540) | von Elias bereitgestellt, Dateinamen unverändert |
| `schema/zbz_hersch.rng` | **fehlt.** Die TEI-Dateien verweisen per `<?xml-model href="../oxygen_framework/schema/zbz_hersch.rng"?>` darauf, die Datei ist aber weder in der App noch bei Elias vorhanden. Vermutlich liegt sie im Oxygen-Framework des Redaktionsteams. |

## ODD

| Im Projekt | Herkunft | Bemerkung |
|---|---|---|
| `odd/hersch.odd` | `APP/resources/odd/hersch.odd` | `schemaSpec source="teipublisher.odd"` |
| `odd/teipublisher.odd` | `APP/resources/odd/teipublisher.odd` | referenziert `tp.css` |
| `odd/tp.css` | `APP/resources/odd/tp.css` | von `teipublisher.odd` referenziert |

Weitere `source`-Verweise gibt es nicht.

## CSS (Rohmaterial für Phase 3)

| Im Projekt | Herkunft |
|---|---|
| `assets/css/vorlage/hersch.css` | `APP/resources/css/hersch.css` |
| `assets/css/vorlage/landing-page.css` | `APP/resources/css/landing-page.css` |
| `assets/css/vorlage/jinks-variables.css` | `APP/resources/css/jinks-variables.css` |
| `assets/css/vorlage/theme.json` | `APP/config.json`, Abschnitt `theme` |

Hinweise: `landing-page.css` verweist auf `../images/typewriter1.jpg` und `typewriter3.jpg`, die in der App **nicht vorhanden** sind. Die TEI-Publisher-Logos in `hersch.css` wurden nicht übernommen. `theme.json` nennt `'ES Rebond Grotesque'` als Überschriftenschrift (siehe unten).

## Schriften

| Im Projekt | Herkunft | Lizenz |
|---|---|---|
| `assets/fonts/eb-garamond-*.woff2` (4) | `APP/resources/fonts/` | SIL OFL 1.1, `LICENSE-garamond` liegt bei |
| `assets/fonts/inter-v19-*.woff2` (6) | `APP/resources/fonts/` | SIL OFL 1.1, **Lizenzdatei fehlt in der App** |
| `assets/fonts/JunicodeVF-*.woff2` (2) | `APP/resources/fonts/` | SIL OFL 1.1, **Lizenzdatei fehlt in der App** |
| `assets/fonts/font.css` | `APP/resources/fonts/font.css` | enthält noch `@font-face` für ES Rebond Grotesque (Dateien fehlen absichtlich), wird in Phase 3 bereinigt |

**Nicht kopiert:** `ESRebondGrotesque-*.woff2` (kommerzielle Lizenz, Freigabe für github.io durch Elias ausstehend).

## UI-Texte und Taxonomie

| Im Projekt | Herkunft |
|---|---|
| `assets/i18n/vorlage/de.json`, `fr.json`, `en.json` | `APP/resources/i18n/app/` (`ita.json` nicht übernommen) |
| `assets/i18n/taxonomy.json` | abgeleitet aus den Schlüsseln `hersch_worktype`, `hersch_genre`, `hersch_keywords` in `APP/resources/i18n/app/{de,fr,en}.json` |

Die eigentlichen Taxonomie-Definitionen (`hersch_taxonomy.xml` mit `category`/`catDesc`) liegen im Datenverzeichnis der laufenden App (`$config:register-root`) und sind **nicht im App-Paket**. Deshalb fehlt auch die Hierarchie der Schlagwörter (Ober-/Unterkategorien, vgl. `APP/modules/custom-api.xql`). `bildende-kuenste` kommt in den Daten vor, hat aber kein Label und ist als `"_entwurf": true` markiert.

## Bilder

| Im Projekt | Herkunft | verwendet in |
|---|---|---|
| `assets/img/favicon.ico`, `favicon-{16,24,32,48,64}.png`, `icon.svg` | `APP/resources/images/` | `hersch-base.html` |
| `assets/img/logo-wide-transparent.svg` | `APP/resources/images/` | Kopfzeile (`hersch-base.html`) |
| `assets/img/logo-wide-home.svg`, `logo-square-transparent.svg` | `APP/resources/images/` | Startseite |
| `assets/img/logo-zb-bw.svg` | `APP/resources/images/` | Fusszeile |
| `assets/img/portrait.jpg` | `APP/resources/images/` | Startseite (`hersch-home-base.html`); **Bildrechte vor Veröffentlichung klären** |
| `assets/img/arrow-*.svg`, `but-menu-*.svg`, `ico-glass.svg`, `eye-*.svg`, `cc-icons.svg` | `APP/resources/images/` | Menü, Navigation, Lizenzhinweis |

## Templates (nur Referenz, TEI-Publisher-Syntax)

`templates/vorlage/`: `hersch-base.html`, `hersch-content.html`, `hersch-home-base.html` aus `APP/templates/layouts/`; `home.html`, `about-hersch.html`, `project.html`, `imprint.html`, `people.html`, `person.html`, `hersch-menu.html`, `footer.html` aus `APP/templates/`.
