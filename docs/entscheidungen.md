# Entscheidungen

Editorische und gestalterische Entscheidungen von Elias, damit spätere Phasen sie berücksichtigen.

| Datum | Thema | Entscheidung | Folgen für spätere Phasen |
|---|---|---|---|
| 2026-10-14 | Datenbefunde aus `datenbericht.md` (Platzhalter `GND-GND_id`, Schlagwort `bildende-kuenste` ohne Label, Autorin-Ref ohne `GND-`) | Werden für den Proof of Concept **ignoriert**, keine Korrektur in den Daten. | Phase 5: Refs ohne gültige GND-Nummer (`GND-GND_id`) beim Register überspringen, nicht bei lobid abfragen. Phase 4: Kategorien ohne Label mit dem Schlüssel als Ersatz anzeigen (z. B. «bildende-kuenste»). |
| 2026-10-14 | Schrift ES Rebond Grotesque | Webfont-Lizenz gilt für github.io, Schrift wird eingebunden. | Phase 3: als Überschriftenschrift gemäss `theme.json` verwenden. |
| 2026-10-14 | Verschachtelte `<bibl>` (1540.xml), `title/@type="2"` (880.xml) | Gewollt. | Phase 2: in der ODD so darstellen, wie es kodiert ist. |
| 2026-10-14 | Bildrechte `portrait.jpg` | Liegen bei der ZB, darf verwendet werden. | – |
