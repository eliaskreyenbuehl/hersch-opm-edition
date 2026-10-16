# ODD-Anpassungen für OPM

`hersch.odd` bleibt unverändert. Alle Anpassungen stehen in `odd/hersch-opm.odd`, die per `source="hersch.odd"` erbt; `opm.toml` zeigt auf `hersch-opm.odd`. Kette: `hersch-opm.odd` → `hersch.odd` → `teipublisher.odd` (+ `tp.css`).

Wichtig: In OPM ersetzt ein `elementSpec mode="change"` **alle** Modelle des Elements. Deshalb wird jedes geänderte Element vollständig neu deklariert. Modelle, die nur in der eXist-App gebraucht werden (Register-Modi, Browse-Suche, Zitiervorschlag), sind dabei weggelassen.

## Geänderte Elemente

| Element | Problem in OPM | Lösung | Bezug zur Live-Edition |
|---|---|---|---|
| `div` | Das Web-Modell für `div[@n='1']` baut den Inhalt mit einem XQuery-Elementkonstruktor (`<div type="front">{…}</div>`) und ruft `ext:create-icon-year()` auf. OPM kann beides nicht, der **ganze Textbereich blieb leer**. | `pb:template` mit eigenen Parametern: `front` = `ancestor::text/front/node()` in `<div class="front">`, `content` = alles nach `head`, `genre` und `year` aus dem teiHeader. | Text identisch. Das Gattungs-Icon wird nicht als `<img>` erzeugt, sondern als `data-genre="article"` am `div.icon-year`; das Icon setzt Phase 3 per CSS (vermeidet absolute Pfade). Weggelassen: Browse-Suche (`ext:div-*`), Register-Modus, epub/print-Varianten. |
| `persName` | Popover-Inhalt per `collection($global:register-root)` (eXist-Register, `let`-Kette): nicht ausführbar. | `<span class="person" data-gnd="172155800">`, GND-Präfix entfernt. Refs ohne gültige Nummer (`GND-GND_id`) erhalten nur die Klasse `person`, kein `data-gnd`. | Text identisch; Popover und Link folgen in Phase 5. |
| `orgName` | wie `persName` | `<span class="org" data-gnd="…">` | wie oben |
| `bibl` | wie `persName`, dazu `ext:citation()`, `ext:mentions()` | `<span class="work" data-gnd="…">`; verschachtelte `bibl` (1540) ergeben verschachtelte Spans | wie oben |
| `space` | keine Regel in hersch.odd/teipublisher.odd | `space[@dim='vertical']` → leerer Block `.space-vertical`, sonst Leerzeichen | live ohne sichtbare Wirkung, Text identisch |
| `text` (Phase 3) | `teipublisher.odd` gibt `<body>` aus; in der Leseseite steht der Text in `<article>`, ein zweites `<body>` ist ungültiges HTML | `behaviour="block"` → `<div class="tei-text …">` | Darstellung unverändert |
| `graphic` (Phase 3) | `@url` zeigt auf `resources/images/edition/` der eXist-App; 760 hat einmal `fig26.jpg/` mit Schrägstrich | Schrägstrich am Ende entfernen; mit Parameter `image-base` (opm.toml: `{prefix}assets/img/edition/`) nur den Dateinamen übernehmen | Bilder wie live, als verkleinerte Webfassungen |

## Bewusst unverändert übernommen (geprüft)

| Element | Verhalten | Ergebnis |
|---|---|---|
| `pb` | `inline`, Inhalt `@n`, rechts schwebend | Seitenzahlen exakt wie live, z. B. «38», «3.33», «[7.52]» |
| `lb` | `inline` (leerer Span), also kein sichtbarer Zeilenumbruch | wie live; `lb break="no"` verbindet ohne Leerzeichen, weil die Daten an diesen Stellen kein Leerzeichen haben |
| `head`/`title` | Haupttitel `h1` in `div.fixed`, Untertitel/Zwischentitel als `heading` bzw. inline | wie live. `title[@type='sub']` kommt in den 12 Dateien nicht vor; `title/@type="2"` (880) wird wie jeder Zwischentitel behandelt (gewollt, siehe `entscheidungen.md`) |
| `back/div[@type='reprint']` | `back` als Block `.back`, darin Überschrift «Nachdruck» und `ref` als Link | 830 identisch mit live |
| `teiHeader` | `metadata`, also nicht im Fliesstext | wie live; Metadatenblock folgt in Phase 3 |
| `note` | `note`-Behaviour (Fussnoten, nur 730) | Text vorhanden; Darstellung prüft Phase 3 |
| `figure`/`graphic` | `graphic` mit `@url` | Bilder fehlen noch (siehe unten) |
| `choice`/`sic`/`corr` | — | kommt in den 12 Dateien **nicht vor**, keine Regel nötig |

## Ausdrücke, die OPM überspringt (27)

`opm coverage` meldet 27 Ausdrücke, die OPM nicht ausführen kann. Alle betreffen Modi, die die statische Leseansicht nicht verwendet: Register (`person`, `org`, `TEI` mit `mode='register'`), Zitiervorschlag (`teiHeader`, `ext:retrieve-reference`), Browse-Ansicht (`titleStmt`, `ext:type-icon`), Briefnavigation (`correspContext`), Datumsformatierung mit `try/catch` (`date`, `birth`, `death`, nur Popover/Register), `biblStruct` (nur für Auftritte, Werktyp ≠ text) sowie MEI. Kein einziger davon greift beim Lesetext.

## Coverage über alle 12 Dateien

- 12 von 12 Dateien transformieren ohne Fehler, auch mit `--strict`.
- Elemente ohne Regel: 0. Verworfene Elemente: 0.
- Bericht neu erzeugen: `uv run opm coverage data/ --all`

## Stichproben gegen die Live-Edition

Verglichen wurde der normalisierte Text des Lesebereichs (`div.tei-body`, Leerraum zusammengefasst, Popover-Vorlagen entfernt) per SHA-256 sowie die Folge der Seitenzahlen. Hilfsskript: `scripts/compare_text.py`.

| Text | Auswahl | Zeichen | Text | Seitenzahlen |
|---|---|---|---|---|
| 830 «En regardant l’Eve d’Autun» | kurz, FR, mit Nachdruck | 8 503 | identisch | identisch (3.33–3.35) |
| 880 «Der Lehrer in der heutigen Krise» | lang, DE, viele Zwischentitel | 32 752 | identisch | identisch (1106–1111) |
| 760 «Chagall à travers quelques toiles» | FR, 33 Abbildungen | 29 019 ohne Leerzeichen | identisch ohne Leerraum; 3 Leerzeichen mehr zwischen direkt aufeinanderfolgenden `pb` («7.23 7.24» statt «7.237.24») | identisch (7.16–[7.52]) |
| 1540 «Mein Judentum» | DE, Referenztext | 20 840 | identisch | identisch (38–46) |
| 790 «Der Mensch ist nicht planbar» | Interview, 75 Personen | 28 407 | identisch | identisch (60–75) |

Ein visueller Vergleich mit Screenshots war nicht möglich (die Live-Seite reagierte im Browser nicht auf Screenshot-Anfragen) und gehört ohnehin zu Phase 3 (Styling).

## Offene Punkte für spätere Phasen

- ~~Abbildungen~~ und ~~Gattungs-Icons~~: in Phase 3 erledigt (siehe Tabelle oben und `docs/leseansicht.md`). `fig28.jpg` fehlt weiterhin (siehe `datenbericht.md`).
- **900.xml ohne Titelzeile:** `head type="lemma"` hat kein `title[@type='main']`, deshalb bleibt `h1` leer, und die Seitenzahl 402 (vor dem `head`) fällt weg. Live ist es genau gleich; Hinweis für die Redaktion.
- **Unsichtbares Zeichen:** In 880.xml steht vor der Seitenzahl `1110` ein BOM-Zeichen (U+FEFF). Live und OPM zeigen es gleich (unsichtbar); Hinweis für die Redaktion.
- `div.front` wird auch bei leerem `<front/>` erzeugt; seit Phase 3 per CSS (`.front:empty`) ausgeblendet.
