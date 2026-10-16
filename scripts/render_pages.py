"""Jinja-Seiten rendern: Startseite, Werkliste, Jeanne Hersch, Projekt, Impressum, Datenschutz.

Aufruf:  uv run python scripts/render_pages.py
(build.py ruft das Skript nach extract_metadata.py und opm chunk auf.)

Liest _site/data/works.json, assets/i18n/taxonomy.json und die Textbausteine in
content/. Schreibt nach _site/ (index.html, works.html, about.html, project.html,
imprint.html, privacy.html). Die gemeinsamen Assets legt `opm chunk` unter _site/edition/assets/ ab.
"""

from __future__ import annotations

import html
import json
import sys
from collections import Counter
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / '_site'
CONTENT = ROOT / 'content'
TAXONOMY = ROOT / 'assets' / 'i18n' / 'taxonomy.json'

# Kacheln auf der Startseite (Entscheid Elias, 2026-10-16): Querschnitt über
# Jahrzehnte und Sprachen. Reihenfolge = Anzeige.
FEATURED = ['90', '730', '870', '1540']

# Weg von den Seiten in _site/ zu den gemeinsamen Assets
ASSETS = 'edition/assets'

LANGUAGES = {  # aus assets/i18n/vorlage/de.json → languages
    'deu': ('Deutsch', 'de'),
    'fra': ('Französisch', 'fr'),
    'eng': ('Englisch', 'en'),
    'ita': ('Italienisch', 'it'),
}

# Symbol je Publikationsform, wie ext-odd.xql der Hersch-App
GENRE_ICONS = {'book': 'ico-book.svg', 'tv': 'ico-video.svg', 'radio': 'ico-audio.svg'}

FACETS = [  # Name in works.json, Schema in taxonomy.json, Überschrift (i18n facets.*)
    ('worktype', 'hersch_worktype', 'Werktyp'),
    ('genre', 'hersch_genre', 'Publikationsform'),
    ('lang', None, 'Sprache'),
    ('keywords', 'hersch_keywords', 'Themen'),
]

NS = {'tei': 'http://www.tei-c.org/ns/1.0'}


def make_label(taxonomy: dict, warnings: set):
    def label(scheme: str, key: str) -> str:
        entry = taxonomy.get(scheme, {}).get(key)
        value = entry.get('de') if isinstance(entry, dict) else None
        if not value:
            warnings.add(f'{scheme}/{key}')
            return key
        return value
    return label


def lang_label(code: str) -> str:
    return LANGUAGES.get(code, (code, code))[0]


def build_facets(works: list[dict], taxonomy: dict, label) -> list[dict]:
    facets = []
    for name, scheme, title in FACETS:
        counts = Counter(v for w in works for v in (w[name] if isinstance(w[name], list) else [w[name]]) if v)
        if scheme:
            order = list(taxonomy.get(scheme, {}))
            keys = sorted(counts, key=lambda k: (order.index(k) if k in order else len(order), k))
            if name == 'keywords':  # Themen alphabetisch
                keys = sorted(counts, key=lambda k: label(scheme, k).casefold())
        else:
            keys = sorted(counts, key=lambda k: (-counts[k], k))
        options = []
        for key in keys:
            text = label(scheme, key) if scheme else lang_label(key)
            options.append({
                'key': key,
                'label': text,
                'count': counts[key],
                'missing': text == key and scheme is not None,
                'icon': (GENRE_ICONS.get(key, 'ico-doc.svg') if name == 'genre' else None),
            })
        facets.append({'name': name, 'label': title, 'options': options})
    return facets


def content(name: str) -> str:
    path = CONTENT / f'{name}.html'
    return path.read_text(encoding='utf-8') if path.exists() else ''


def project_from_tei() -> str:
    """Abschnitte aus dem teiHeader des ersten Textes (gleich in allen Dateien)."""
    files = sorted((ROOT / 'data').glob('*.xml'))
    if not files:
        return ''
    tree = etree.parse(str(files[0]))
    e = html.escape
    out = []
    paras = [' '.join(''.join(p.itertext()).split()) for p in tree.xpath('//tei:encodingDesc/tei:projectDesc/tei:p', namespaces=NS)]
    if paras:
        out.append('<h2>Arbeitsweise</h2>')
        out += [f'<p>{e(p)}</p>' for p in paras]
    resps = tree.xpath('//tei:editionStmt/tei:respStmt', namespaces=NS)
    if resps:
        out.append('<h2>Beteiligte</h2>\n<dl class="people-list">')
        for r in resps:
            resp = ' '.join(''.join(r.xpath('tei:resp', namespaces=NS)[0].itertext()).split())
            names = [' '.join(''.join(n.itertext()).split()) for n in r.xpath('tei:persName | tei:orgName', namespaces=NS)]
            out.append(f'<dt>{e(resp)}</dt>' + ''.join(f'<dd>{e(n)}</dd>' for n in names))
        out.append('</dl>')
    funders = [' '.join(''.join(f.itertext()).split()) for f in tree.xpath('//tei:titleStmt/tei:funder', namespaces=NS)]
    if funders:
        out.append('<h2>Förderung</h2>\n<ul>' + ''.join(f'<li>{e(f)}</li>' for f in funders) + '</ul>')
    return '\n'.join(out)


def main() -> int:
    works = json.loads((SITE / 'data' / 'works.json').read_text(encoding='utf-8'))
    taxonomy = json.loads(TAXONOMY.read_text(encoding='utf-8'))
    warnings: set[str] = set()
    label = make_label(taxonomy, warnings)

    for w in works:
        w['lang_code'] = LANGUAGES.get(w['lang'], ('', w['lang']))[1]

    years = sorted(int(w['year']) for w in works if w['year'].isdigit())
    langs = [k for k, _ in Counter(w['lang'] for w in works if w['lang']).most_common()]
    by_id = {w['id']: w for w in works}
    featured = [by_id[i] for i in FEATURED if i in by_id]
    for i in FEATURED:
        if i not in by_id:
            print(f'Warnung: Kachel {i} – kein Werk mit dieser ID', file=sys.stderr)

    env = Environment(loader=FileSystemLoader(ROOT / 'templates'), undefined=StrictUndefined,
                      autoescape=True, keep_trailing_newline=True)
    env.filters['lang_label'] = lang_label
    common = {'root': '', 'assets': ASSETS, 'label': label, 'lang_label': lang_label,
              'genre_icon': lambda g: GENRE_ICONS.get(g, 'ico-doc.svg')}

    pages = {
        'index.html': ('home.html.j2', {
            'stats': {'count': len(works), 'year_min': years[0] if years else '',
                      'year_max': years[-1] if years else '', 'langs': langs},
            'featured': featured,
            'content': {'intro': content('intro')},
        }),
        '404.html': ('404.html.j2', {}),
        'works.html': ('works.html.j2', {
            'works': works,
            'facets': build_facets(works, taxonomy, label),
            'years': {'min': years[0] if years else 0, 'max': years[-1] if years else 0},
        }),
    }

    about_nav = [{'href': 'about.html', 'label': 'Biografie'}]
    project_nav = [{'href': 'project.html', 'label': 'Projektbeschreibung'},
                   {'href': 'works.html', 'label': 'Werke'}]
    for name, title, crumbs, nav, body, theme in [
        ('about', 'Jeanne Hersch', ['Jeanne Hersch', 'Biografie'], about_nav, content('about'), 'about'),
        ('project', 'Projekt', ['Projekt', 'Projektbeschreibung'], project_nav,
         content('project') + '\n' + project_from_tei(), 'project'),
        ('imprint', 'Impressum', ['Impressum'], [], content('imprint'), 'imprint'),
        ('privacy', 'Datenschutz', ['Datenschutz'], [], content('privacy'), 'imprint'),
        # Platzhalter, bis Phase 5 (Register) und Phase 6 (Suche) sie ersetzen
        ('people', 'Personen', ['Personen'], [], content('people'), 'works'),
        ('search', 'Suche', ['Suche'], [], content('search'), 'works'),
    ]:
        pages[f'{name}.html'] = ('content.html.j2', {'page': {
            'name': name, 'title': title, 'crumbs': crumbs, 'nav': nav, 'html': body, 'theme': theme}})

    for out, (template, ctx) in pages.items():
        (SITE / out).write_text(env.get_template(template).render(**common, **ctx), encoding='utf-8')
        print(f'{out:13} ← templates/{template}')

    for w in sorted(warnings):
        print(f'Warnung: keine Bezeichnung in taxonomy.json für {w}, Schlüssel wird angezeigt', file=sys.stderr)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
