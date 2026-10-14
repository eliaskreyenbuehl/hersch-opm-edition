# Phase 2 – Hersch-ODD mit OPM zum Laufen bringen

**Kernrisiko des ganzen Projekts.** Hier zeigt sich, ob die ODD aus TEI Publisher 10 in OPM funktioniert.

## Ziel
Alle 12 Texte werden mit der Hersch-ODD über OPM korrekt in HTML umgewandelt. Inhaltlich entspricht das der Live-Edition. Das Styling folgt erst in Phase 3.

## Vorher lesen
- https://opm.e-editiones.org/guide/odd-files/
- https://opm.e-editiones.org/guide/coverage/
- https://opm.e-editiones.org/guide/xpath-extensions/
- https://opm.e-editiones.org/guide/configuration/
- `docs/datenbericht.md` (Element-Statistik aus Phase 1)

## Aufgaben
1. `opm.toml` anlegen (Startpunkt: `uv run opm init` in einem Temp-Ordner, dann nur das Nötige übernehmen):
   ```toml
   [transform]
   odd = "odd/hersch.odd"
   ```
2. `uv run opm transform data/1540.xml -o _site/test/1540.html` und die Fehlermeldungen lesen. Typische Probleme:
   - Die ODD erbt über `source=` von einer ODD, die fehlt. Dann kopieren oder umbiegen.
   - XQuery-Funktionen in `@predicate` oder `param`, die es nur in eXist gibt (z. B. `pm-config:`, `doc()` auf Datenbankpfade, `collection()`), müssen durch XPath 3.1 oder eine OPM-XPath-Extension ersetzt werden.
   - Behaviours: hersch.odd verwendet `alternate, block, document, heading, inline, link, listItem, metadata, omit, pass-through, section`. Prüfen, ob OPM alle kennt.
3. **Nicht `hersch.odd` umschreiben.** Eine eigene `odd/hersch-opm.odd` anlegen, die von `hersch.odd` erbt und nur die nötigen `elementSpec mode="change"` enthält. `opm.toml` zeigt dann auf `hersch-opm.odd`. Jede Abweichung mit Grund in `docs/odd-anpassungen.md` dokumentieren.
4. Prüfen und ggf. regeln, Referenz ist https://edition-jeanne-hersch.org/edition/1540.xml:
   - `head/title[@type='main']` und `[@type='sub']`: Titel und Untertitel
   - `pb/@n`: Seitenzahl am Rand, z. B. «38» / «44» (Format mit der Live-Seite abgleichen)
   - `lb` und `lb break="no"`: Zeilenumbruch und Silbentrennung ohne Leerzeichen
   - `choice/sic/corr`: corr anzeigen, sic als Tooltip oder `alternate`
   - `space dim="vertical"`: Leerraum
   - `persName/@ref`: vorerst als `<span class="person" data-gnd="…">`, der Link folgt in Phase 5
   - `back/div[@type='reprint']`: Block «Nachdruck» mit Link
   - `teiHeader`: in der Leseansicht nicht als Fliesstext anzeigen (der Metadatenblock kommt in Phase 3)
5. Coverage über alle 12 Dateien laufen lassen. Elemente ohne Regel auflisten und entscheiden: Regel ergänzen oder bewusst Standard. In `docs/odd-anpassungen.md` festhalten.
6. 5 Stichproben wählen (kurz, lang, FR, DE, mit vielen `persName`), transformieren, im eingebauten Browser neben die Live-Seite legen und Unterschiede notieren.

## Abnahme
- [ ] Alle 12 Dateien transformieren ohne Fehler.
- [ ] 5 Stichproben inhaltlich gleich wie auf der Live-Edition (Text, Seitenzahlen, Korrekturen, Absätze).
- [ ] `docs/odd-anpassungen.md` erklärt jede Abweichung von hersch.odd.
- [ ] Commit.

## Wenn es nicht geht
Nach ca. 2 Stunden ohne Fortschritt: anhalten und Elias einen kurzen Bericht geben (was geht, was nicht, Optionen). Ein solches Ergebnis gehört auch zum Beweis.
