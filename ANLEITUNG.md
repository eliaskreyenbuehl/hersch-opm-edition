# Anleitung für Elias

So setzt du die Edition Phase für Phase mit Claude Code um. Du brauchst nur die Claude-Desktop-App (Code-Tab) und einen Browser.

## Grundablauf (für jede Phase gleich)

1. In der Claude-App eine **neue Sitzung** starten und als Ordner `C:\Users\krey\large_files\claude\hersch-opm-edition` wählen.
2. Den Satz aus der Tabelle unten einfügen und abschicken.
3. Claude arbeitet. Wenn es um Erlaubnis fragt, lies kurz, was es tun will, und gib frei.
4. Am Ende bekommst du eine Liste **«Bitte prüfen»**. Arbeite sie im Browser ab.
5. Passt etwas nicht, schreibst du es in derselben Sitzung, zum Beispiel: «Die Seitenzahlen fehlen bei 1540.xml.»
6. Wenn alles passt: Startzeit, Endzeit und Notizen in `docs/beweisprotokoll.md` eintragen bzw. prüfen. Das ist der Beweis.

Eine neue Sitzung pro Phase hält den Kontext klein und spart Tokens. Alles Wichtige steht in `CLAUDE.md` und in den Briefings.

## Die Phasen

| Phase | Satz für Claude | Dauer (Schätzung) | Was du prüfst |
|---|---|---|---|
| 0 Setup | «Lies docs/phase-0-setup.md und setze die Phase um.» | 30 Min. | Claude meldet: opm läuft, GitHub-Konto verbunden |
| 1 Daten & Design | «Lies docs/phase-1-daten-design.md und setze die Phase um.» | 1 Std. | `docs/datenbericht.md`: Stimmen die Lücken? |
| 2 ODD | «Lies docs/phase-2-odd.md und setze die Phase um.» | 2–3 Std. | 5 Texte inhaltlich gleich wie auf der Live-Edition |
| 3 Leseansicht | «Lies docs/phase-3-leseansicht.md und setze die Phase um.» | 2–3 Std. | 1540.xml sieht aus wie die Hersch-Edition (auch auf dem Handy) |
| 4 Werkliste | «Lies docs/phase-4-werkliste.md und setze die Phase um.» | 2 Std. | Filter, Startseite, Kategorie-Namen |
| 5 Register | «Lies docs/phase-5-register.md und setze die Phase um.» | 2–3 Std. | 20 Personen gegen die GND prüfen |
| 6 Suche & Sprachen | «Lies docs/phase-6-suche-sprachen.md und setze die Phase um.» | 1–2 Std. | Suche «Jaspers», Sprachwechsel FR/EN |
| 7 Veröffentlichen | «Lies docs/phase-7-launch.md und setze die Phase um.» | 1 Std. | Öffentliche URL auf Laptop und Handy |

## Was du vor dem Start bereitlegen solltest

- [ ] Den Ordner mit den **12 TEI-Dateien** (Claude fragt in Phase 1 nach dem Pfad)
- [ ] Deinen **GitHub-Kontonamen** und einen Namen für das Repo (Vorschlag: `hersch-opm-edition`)
- [ ] Antwort auf die Frage: Gilt die Webfont-Lizenz für **ES Rebond Grotesque** auch für eine github.io-Adresse? Falls nicht, nimmt Claude Inter.
- [ ] Falls vorhanden: das RNG-Schema `zbz_hersch.rng` (aus dem Oxygen-Framework)

## Wenn etwas schiefgeht

- **Claude hängt oder dreht sich im Kreis:** Sitzung beenden, neue Sitzung, gleicher Satz plus «Wir waren bei …, Problem war …».
- **Etwas ist kaputt, das vorher ging:** Schreib «Mach den letzten Commit rückgängig und erkläre mir, was passiert ist.» Weil alles in Git liegt, geht nichts verloren.
- **Datenfehler in einem TEI-Text:** Claude ändert keine TEI-Dateien. Du korrigierst in Oxygen, kopierst die Datei neu nach `data/` und lässt neu bauen.
