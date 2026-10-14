# Datenbericht

Erzeugt von `scripts/validate.py` am 2026-10-14. Die Dateien in `data/` wurden nur gelesen. Korrekturen macht das Team in Oxygen.

- Dateien: 12
- Wohlgeformt: 12 von 12
- Schema: kein Schema unter `schema/zbz_hersch.rng`, nur Wohlgeformtheit geprüft

## Übersicht

| Datei | ID | Titel | Jahr | Sprache | Werktyp | Gattung | Schlagwörter | Schema | Probleme |
|---|---|---|---|---|---|---|---|---|---|
| 90.xml | 90 | Monique Saint-Hélier | 1944 | fra | text | article | literatur | – | 0 |
| 730.xml | 730 | Die Frau heute – Gerede und ernste Verantwortung | 1966 | deu | text | speech | frau-und-frauenrechte | – | 1 |
| 760.xml | 760 | Chagall à travers quelques toiles | 1967 | fra | text | article | bildende-kuenste | – | 0 |
| 770.xml | 770 | La Suisse et l’Europe | 1967 | fra | text | article | europa-und-die-schweiz | – | 0 |
| 790.xml | 790 | Der Mensch ist nicht planbar | 1967 | deu | text | interview | schule | – | 0 |
| 830.xml | 830 | En regardant l’Eve d’Autun | 1968 | fra | text | article | bildende-kuenste | – | 0 |
| 870.xml | 870 | Is the Declaration of Human Rights a Western Concept? | 1970 | eng | text | article | menschenrechte | – | 0 |
| 880.xml | 880 | Der Lehrer in der heutigen Krise | 1970 | deu | text | speech | unterricht | – | 0 |
| 890.xml | 890 | Die Demokratisierung der Schule | 1970 | deu | text | speech | schule | – | 0 |
| 900.xml | 900 | Jaspers (Karl) 1883-1969 | 1971 | fra | text | entry | karl-jaspers | – | 0 |
| 910.xml | 910 | Sur le sens de l'histoire | 1971 | fra | text | article | geschichtsphilosophie | – | 0 |
| 1540.xml | 1540 | Mein Judentum | 1978 | deu | text | article | judentum-und-religion, gespraeche-ueber-leben-und-werk | – | 1 |

## Abweichungen

### 90.xml

- Hinweis: GND-Refs uneinheitlich: 25× mit «GND-», 1× ohne (z. B. 118815679)

### 730.xml

- **Problem:** ungültige GND-Ref «GND-GND_id» (3×)
- Hinweis: GND-Refs uneinheitlich: 16× mit «GND-», 1× ohne (z. B. 118815679)

### 760.xml

- Hinweis: Kategorie «bildende-kuenste» (hersch_keywords) hat in der Hersch-App kein Label (Entwurf)
- Hinweis: GND-Refs uneinheitlich: 56× mit «GND-», 1× ohne (z. B. 118815679)

### 770.xml

- Hinweis: GND-Refs uneinheitlich: 10× mit «GND-», 1× ohne (z. B. 118815679)

### 790.xml

- Hinweis: GND-Refs uneinheitlich: 86× mit «GND-», 1× ohne (z. B. 118815679)

### 830.xml

- Hinweis: Kategorie «bildende-kuenste» (hersch_keywords) hat in der Hersch-App kein Label (Entwurf)
- Hinweis: GND-Refs uneinheitlich: 10× mit «GND-», 1× ohne (z. B. 118815679)

### 870.xml

- Hinweis: GND-Refs uneinheitlich: 23× mit «GND-», 1× ohne (z. B. 118815679)

### 880.xml

- Hinweis: GND-Refs uneinheitlich: 15× mit «GND-», 1× ohne (z. B. 118815679)

### 890.xml

- Hinweis: GND-Refs uneinheitlich: 18× mit «GND-», 1× ohne (z. B. 118815679)

### 900.xml

- Hinweis: GND-Refs uneinheitlich: 47× mit «GND-», 1× ohne (z. B. 118815679)

### 910.xml

- Hinweis: GND-Refs uneinheitlich: 24× mit «GND-», 1× ohne (z. B. 118815679)

### 1540.xml

- **Problem:** ungültige GND-Ref «GND-GND_id» (3×)
- Hinweis: GND-Refs uneinheitlich: 44× mit «GND-», 1× ohne (z. B. 118815679)

## Werte im Vergleich

- Lizenz: https://creativecommons.org/licenses/by-sa/4.0/ (12×)
- Sprache: fra (6×); deu (5×); eng (1×)
- `hersch_genre`: article (7×), entry (1×), interview (1×), speech (3×)
- `hersch_worktype`: text (12×)
- `hersch_keywords`: bildende-kuenste (2×), europa-und-die-schweiz (1×), frau-und-frauenrechte (1×), geschichtsphilosophie (1×), gespraeche-ueber-leben-und-werk (1×), judentum-und-religion (1×), karl-jaspers (1×), literatur (1×), menschenrechte (1×), schule (2×), unterricht (1×)

## Elemente in `<text>`

| Name | Total | 90 | 730 | 760 | 770 | 790 | 830 | 870 | 880 | 890 | 900 | 910 | 1540 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `lb` | 5236 | 139 | 460 | 908 | 173 | 523 | 219 | 381 | 675 | 631 | 405 | 358 | 364 |
| `hi` | 627 | 1 | 5 | 11 | 6 | 43 | 4 | 12 | 185 | 154 | 136 | 38 | 32 |
| `p` | 453 | 11 | 23 | 80 | 28 | 71 | 18 | 37 | 39 | 46 | 20 | 43 | 37 |
| `persName` | 176 | 8 | 4 | 24 |  | 75 |  | 2 | 5 | 2 | 20 | 14 | 22 |
| `pb` | 120 | 4 | 9 | 38 | 5 | 17 | 4 | 9 | 6 | 6 | 3 | 10 | 9 |
| `sp` | 68 |  |  |  |  | 68 |  |  |  |  |  |  |  |
| `speaker` | 68 |  |  |  |  | 68 |  |  |  |  |  |  |  |
| `bibl` | 58 | 7 |  | 11 |  |  |  |  |  | 2 | 34 |  | 4 |
| `title` | 45 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 15 | 12 | 8 | 1 | 1 |
| `div` | 44 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 13 | 12 | 9 | 1 | 1 |
| `head` | 44 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 13 | 12 | 9 | 1 | 1 |
| `orgName` | 40 |  | 2 | 11 |  | 1 |  | 11 |  | 4 | 3 |  | 8 |
| `figure` | 35 |  |  | 33 |  |  | 2 |  |  |  |  |  |  |
| `graphic` | 35 |  |  | 33 |  |  | 2 |  |  |  |  |  |  |
| `body` | 12 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `text` | 12 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `anchor` | 10 |  |  | 10 |  |  |  |  |  |  |  |  |  |
| `space` | 10 |  |  | 3 |  |  | 1 |  |  |  |  | 6 |  |
| `foreign` | 7 | 7 |  |  |  |  |  |  |  |  |  |  |  |
| `front` | 7 |  | 1 |  | 1 |  |  | 1 | 1 | 1 |  | 1 | 1 |
| `item` | 3 |  |  |  |  |  |  |  |  | 3 |  |  |  |
| `note` | 3 |  | 3 |  |  |  |  |  |  |  |  |  |  |
| `listBibl` | 2 |  |  |  |  |  |  |  |  |  | 2 |  |  |
| `back` | 1 |  |  |  |  |  | 1 |  |  |  |  |  |  |
| `list` | 1 |  |  |  |  |  |  |  |  | 1 |  |  |  |
| `quote` | 1 |  |  |  |  |  |  |  |  |  |  | 1 |  |
| `ref` | 1 |  |  |  |  |  | 1 |  |  |  |  |  |  |

## Attribute in `<text>`

| Name | Total | 90 | 730 | 760 | 770 | 790 | 830 | 870 | 880 | 890 | 900 | 910 | 1540 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `lb/@break` | 991 | 26 | 75 | 85 | 17 | 125 | 26 | 62 | 162 | 169 | 63 | 61 | 120 |
| `hi/@rendition` | 627 | 1 | 5 | 11 | 6 | 43 | 4 | 12 | 185 | 154 | 136 | 38 | 32 |
| `persName/@ref` | 176 | 8 | 4 | 24 |  | 75 |  | 2 | 5 | 2 | 20 | 14 | 22 |
| `pb/@facs` | 120 | 4 | 9 | 38 | 5 | 17 | 4 | 9 | 6 | 6 | 3 | 10 | 9 |
| `pb/@n` | 120 | 4 | 9 | 38 | 5 | 17 | 4 | 9 | 6 | 6 | 3 | 10 | 9 |
| `title/@type` | 45 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 15 | 12 | 8 | 1 | 1 |
| `div/@xml:id` | 44 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 13 | 12 | 9 | 1 | 1 |
| `div/@n` | 42 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 13 | 12 | 8 | 1 | 1 |
| `orgName/@ref` | 40 |  | 2 | 11 |  | 1 |  | 11 |  | 4 | 3 |  | 8 |
| `bibl/@ref` | 38 | 7 |  | 11 |  |  |  |  |  | 2 | 14 |  | 4 |
| `figure/@xml:id` | 35 |  |  | 33 |  |  | 2 |  |  |  |  |  |  |
| `graphic/@url` | 35 |  |  | 33 |  |  | 2 |  |  |  |  |  |  |
| `div/@type` | 26 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 13 | 1 | 2 | 1 | 1 |
| `title/@xml:id` | 24 | 1 |  | 1 |  | 1 | 1 |  |  | 12 | 8 |  |  |
| `anchor/@xml:id` | 10 |  |  | 10 |  |  |  |  |  |  |  |  |  |
| `space/@dim` | 10 |  |  | 3 |  |  | 1 |  |  |  |  | 6 |  |
| `foreign/@xml:lang` | 7 | 7 |  |  |  |  |  |  |  |  |  |  |  |
| `note/@place` | 3 |  | 3 |  |  |  |  |  |  |  |  |  |  |
| `note/@xml:id` | 3 |  | 3 |  |  |  |  |  |  |  |  |  |  |
| `pb/@break` | 3 |  |  |  | 1 |  |  |  | 1 |  |  |  | 1 |
| `note/@type` | 2 |  | 2 |  |  |  |  |  |  |  |  |  |  |
| `head/@type` | 1 |  |  |  |  |  |  |  |  |  | 1 |  |  |
| `quote/@source` | 1 |  |  |  |  |  |  |  |  |  |  | 1 |  |
| `ref/@target` | 1 |  |  |  |  |  | 1 |  |  |  |  |  |  |

## Attributwerte in `<text>` (für die ODD)

| Name | Total | 90 | 730 | 760 | 770 | 790 | 830 | 870 | 880 | 890 | 900 | 910 | 1540 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `lb/@break="no"` | 991 | 26 | 75 | 85 | 17 | 125 | 26 | 62 | 162 | 169 | 63 | 61 | 120 |
| `hi/@rendition="#i"` | 488 |  |  | 11 | 6 | 43 | 4 | 12 | 119 | 115 | 108 | 38 | 32 |
| `hi/@rendition="#b"` | 105 |  |  |  |  |  |  |  | 66 | 39 |  |  |  |
| `title/@type="main"` | 43 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 13 | 12 | 8 | 1 | 1 |
| `hi/@rendition="#k"` | 29 |  | 1 |  |  |  |  |  |  |  | 28 |  |  |
| `div/@type="div_attr"` | 12 |  |  |  |  |  |  |  | 12 |  |  |  |  |
| `space/@dim="vertical"` | 10 |  |  | 3 |  |  | 1 |  |  |  |  | 6 |  |
| `div/@type="article"` | 7 | 1 |  | 1 | 1 |  | 1 | 1 |  |  |  | 1 | 1 |
| `foreign/@xml:lang="fra"` | 7 | 7 |  |  |  |  |  |  |  |  |  |  |  |
| `hi/@rendition="#g"` | 5 | 1 | 4 |  |  |  |  |  |  |  |  |  |  |
| `div/@type="speech"` | 3 |  | 1 |  |  |  |  |  | 1 | 1 |  |  |  |
| `note/@place="foot"` | 3 |  | 3 |  |  |  |  |  |  |  |  |  |  |
| `pb/@break="no"` | 3 |  |  |  | 1 |  |  |  | 1 |  |  |  | 1 |
| `note/@type="footnote"` | 2 |  | 2 |  |  |  |  |  |  |  |  |  |  |
| `title/@type="2"` | 2 |  |  |  |  |  |  |  | 2 |  |  |  |  |
| `div/@type="bibliography"` | 1 |  |  |  |  |  |  |  |  |  | 1 |  |  |
| `div/@type="entry"` | 1 |  |  |  |  |  |  |  |  |  | 1 |  |  |
| `div/@type="interview"` | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  |
| `div/@type="reprint"` | 1 |  |  |  |  |  | 1 |  |  |  |  |  |  |
| `head/@type="lemma"` | 1 |  |  |  |  |  |  |  |  |  | 1 |  |  |
