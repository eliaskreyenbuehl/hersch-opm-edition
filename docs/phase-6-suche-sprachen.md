# Phase 6 – Volltextsuche und Benutzeroberfläche DE/FR/EN

## Ziel
Volltextsuche über alle Texte ohne Server (Pagefind) und eine Oberfläche in Deutsch, Französisch und Englisch. Die Editionstexte bleiben in der Originalsprache.

## Aufgaben

### 1. Suche mit Pagefind
- In `chunk.html.j2` den Lesetext mit `data-pagefind-body` markieren. Kopf, Menü und Seitenleiste werden nicht indexiert.
- Filter: `data-pagefind-filter="gattung"`, `"sprache"`, `"jahr"`. Sortierung nach Jahr: `data-pagefind-sort="jahr"`.
- `<html lang="fr|de">` nach `textLang` setzen, damit Pagefind die richtige Wortstammbildung nutzt.
- Personenseiten indexieren (Name), Startseite und Werkliste nicht.
- `build.py`: als letzten Schritt `uv run python -m pagefind --site _site`.
- `templates/search.html.j2` → `_site/suche/index.html` mit der Pagefind-UI (liegt lokal in `_site/pagefind/`). Gestaltung über `tokens.css` an das Hersch-Design anpassen (CSS-Variablen der Pagefind-UI).
- Suchfeld im Kopf leitet auf die Suchseite weiter (`?q=`).

### 2. Mehrsprachige Oberfläche
- `assets/i18n/de.json`, `fr.json`, `en.json` aus den Vorlagen der Hersch-App ableiten. Nur die Schlüssel übernehmen, die die Site braucht; neue Schlüssel ergänzen (Filterlabels, Seitenleiste, Register).
- In allen Templates feste Texte mit `data-i18n="schluessel"` markieren. Der deutsche Text steht als Standard im HTML.
- `assets/js/i18n.js`: Sprache aus `localStorage` (mit try/catch) bzw. aus dem Browser; die Texte ersetzen; der Sprachumschalter im Kopf ändert die Sprache. Die Kategorie-Labels kommen aus `taxonomy.json`.
- Französische und englische Neuübersetzungen als Entwurf markieren. Elias lässt sie prüfen.

## Abnahme
- [ ] Die Suche nach «Jaspers» findet 1540.xml (und 900.xml) und springt zur Stelle.
- [ ] Die Suche nach einem deutschen und einem französischen Wort mit Flexion (z. B. «Freiheiten», «libertés») liefert Treffer.
- [ ] Die Filter Gattung und Sprache wirken in der Suche.
- [ ] Ein Sprachwechsel übersetzt Menü, Filter, Seitenleiste und Fuss. Die Wahl bleibt beim Neuladen erhalten.
- [ ] Commit.
