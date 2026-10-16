# Entscheidungen

Editorische und gestalterische Entscheidungen von Elias, damit spätere Phasen sie berücksichtigen.

| Datum | Thema | Entscheidung | Folgen für spätere Phasen |
|---|---|---|---|
| 2026-10-14 | Datenbefunde aus `datenbericht.md` (Platzhalter `GND-GND_id`, Schlagwort `bildende-kuenste` ohne Label, Autorin-Ref ohne `GND-`) | Werden für den Proof of Concept **ignoriert**, keine Korrektur in den Daten. | Phase 5: Refs ohne gültige GND-Nummer (`GND-GND_id`) beim Register überspringen, nicht bei lobid abfragen. Phase 4: Kategorien ohne Label mit dem Schlüssel als Ersatz anzeigen. |
| 2026-10-14 | Schrift ES Rebond Grotesque | Webfont-Lizenz gilt für github.io, Schrift wird eingebunden. | Phase 3: als Überschriftenschrift gemäss `theme.json` verwenden. |
| 2026-10-14 | Verschachtelte `<bibl>` (1540.xml), `title/@type="2"` (880.xml) | Gewollt. | Phase 2: in der ODD so darstellen, wie es kodiert ist. |
| 2026-10-14 | Bildrechte `portrait.jpg` | Liegen bei der ZB, darf verwendet werden. | – |
| 2026-10-14 | Schlagwort `bildende-kuenste` (760.xml, 830.xml) | Wird auf der Website als «Künste» **und** «Malerei» angezeigt und gefiltert; TEI bleibt unverändert. | In `taxonomy.json` als `"_alias": ["kuenste", "malerei"]`. Phase 4: `extract_metadata.py` löst Aliase auf. |
| 2026-10-15 | Zitiervorschlag in der Leseansicht | **Wie live:** «Empfohlene Zitierweise» zitiert die Edition (Autor, Titel, Publikationsdatum, Edition Jeanne Hersch, DOI, Zugriffsdatum). Das MLA-9 aus `idno[@type='MLA-9']` steht unter «Originalpublikation». | Zugriffsdatum setzt ein kleines Skript (heutiges Datum). DOI erst, wenn nicht `DOI_COMING`. |
| 2026-10-15 | Aufbau der Seitenleiste | **Aufklappbar wie live:** Export/Download (nur TEI-XML), Empfohlene Zitierweise (offen), Originalpublikation, Lizenz. Auf dem Handy hinter der Leiste «•••». | Phase 5 ergänzt den Abschnitt «Register». |
| 2026-10-15 | Abbildungen (Scans, 225 MB) | **Webfassungen einchecken:** `scripts/prepare_images.py` rechnet einmalig auf max. 2000 px (JPEG, Qualität 82) nach `assets/img/edition/` (zusammen 24 MB). Originale bleiben lokal. | Neue Bilder: Original nach `assets/images/edition/`, dann `uv run python scripts/prepare_images.py`. Pillow ist Entwicklungs-Abhängigkeit. |
| 2026-10-15 | Bildordner | `assets/img/` ist massgeblich (was online geht). `assets/images/` ist Elias' lokales Rohmaterial und steht in `.gitignore`. | Benötigte Bilder von dort nach `assets/img/` kopieren. |
