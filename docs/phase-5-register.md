# Phase 5 – Personenregister (GND)

## Ziel
Ein Personenregister aus den `persName/@ref` aller Texte, angereichert mit Normdaten aus der GND (über lobid). Jede Person in einem Lesetext ist anklickbar.

**Lehre aus der Wall-Edition:** Ein Register «soweit wir sehen konnten» genügt für eine zitierfähige Edition nicht. Darum gibt es hier ein explizites Prüfverfahren.

## Aufgaben

### 1. `scripts/build_register.py`
- Alle `persName[@ref]` in `text` (nicht im Header) einsammeln, dazu Dateiname, Seitenzahl (vorangehendes `pb/@n`) und Schreibweise im Text.
- Refs normalisieren: `GND-118557106` → `118557106`. Auch die Varianten ohne Präfix erkennen.
- Für jede GND-ID einmal `https://lobid.org/gnd/{id}.json` abfragen (Timeout, 1 Anfrage/Sek.). Speichern in `registers/gnd-cache.json`: `preferredName`, `dateOfBirth`, `dateOfDeath`, `professionOrOccupation[].label`, `sameAs` (Wikidata, HLS, falls vorhanden). Steht eine ID schon im Cache, wird nichts abgefragt.
- Mit `--offline` wird nur der Cache verwendet. Diesen Modus nutzt `build.py` in der CI.
- Ausgabe `registers/people.json`: pro Person die Normdaten und die Fundstellen (Werk, Seite, Schreibweise).

### 2. Prüfbericht `docs/register-pruefung.md`
- GND-IDs ohne lobid-Treffer oder mit Typ ≠ Person
- Personen, deren Schreibweise im Text stark vom GND-Namen abweicht (zum Nachsehen, kein Fehler)
- `persName` ohne `@ref` (Liste mit Datei und Seite)
- `@ref`, die gar keine GND-Nummer sind
- **Keine TEI-Datei ändern.** Korrekturen macht das Team in Oxygen.

### 3. Seiten
- `templates/people.html.j2` → `_site/personen/index.html`: alphabetisch nach Nachname, A–Z-Sprungleiste, Suchfeld (Vanilla-JS), Anzahl Erwähnungen. Vorlage: `templates/vorlage/people.html`.
- `templates/person.html.j2` → `_site/personen/{gnd}.html`: Name, Lebensdaten, Beruf, Links (GND, Wikidata, HLS), Liste der Werke mit Seitenangaben und Link zur Stelle.
- **In der Leseansicht:** `persName[@ref]` wird zum Link auf die Personenseite. Das geht als ODD-Änderung in `odd/hersch-opm.odd` (`behaviour="link"`, relativer Pfad) mit Eintrag in `docs/odd-anpassungen.md`. Anker im Lesetext setzen, damit die Personenseite direkt zur Stelle springt.

## Abnahme
- [ ] `registers/people.json` und `gnd-cache.json` eingecheckt. Der Build läuft offline.
- [ ] Elias prüft 20 Personen gegen die GND (Claude stellt die Liste mit Links zusammen).
- [ ] Kein Personen-Link in einem Lesetext führt ins Leere.
- [ ] `docs/register-pruefung.md` liegt vor.
- [ ] Commit.
