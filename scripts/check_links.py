"""Tote und unerlaubte Links in _site/ finden.  Aufruf:  uv run python scripts/check_links.py

Prüft in allen HTML- und CSS-Dateien:
  - relative Verweise (href, src, url(...)) zeigen auf eine vorhandene Datei
  - keine absoluten Pfade («/edition/…»), die unter github.io/<repo>/ brechen
  - keine Skripte, Stylesheets oder Schriften von fremden Servern (Datenschutz)
Externe Links in <a href> (z. B. swisscovery, Creative Commons) sind erlaubt
und werden nicht abgerufen. Fehlende Abbildungen unter assets/img/edition/ sind
Datenprobleme (siehe docs/datenbericht.md) und werden als Hinweis gemeldet, nicht
als Fehler; sie werden in Oxygen bzw. durch Nachlieferung der Scans behoben.
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / '_site'
LATER: dict[str, str] = {}  # Seite → Phase, falls eine Seite noch fehlen darf
CSS_URL = re.compile(r'url\(\s*[\'"]?([^\'")]+)[\'"]?\s*\)')


class Refs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs: list[tuple[str, str, str]] = []  # (tag, attr, value)

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value and name in ('href', 'src', 'action'):
                self.refs.append((tag, name, value))


def check(page: Path, tag: str, value: str, errors: list, later: set):
    parts = urlsplit(value)
    where = page.relative_to(SITE).as_posix()
    if parts.scheme in ('http', 'https') or value.startswith('//'):
        if tag in ('script', 'link', 'img', 'iframe', 'source') or page.suffix == '.css':
            errors.append(f'{where}: externe Quelle {value}')
        return
    if parts.scheme or value.startswith('#') or not parts.path:
        return  # mailto:, data:, Anker auf derselben Seite
    if value.startswith('/'):
        errors.append(f'{where}: absoluter Pfad {value}')
        return
    target = (page.parent / unquote(parts.path)).resolve()
    if target.is_dir():
        target = target / 'index.html'
    if not target.exists():
        name = Path(parts.path).name
        if '/img/edition/' in parts.path:
            later.add(f'Abbildung {name} fehlt ({where}, siehe datenbericht.md)')
        elif name in LATER:
            later.add(f'{name} ({LATER[name]})')
        else:
            errors.append(f'{where}: tot {value}')


def main() -> int:
    if not SITE.exists():
        sys.exit('_site/ fehlt – zuerst bauen: uv run python scripts/build.py')
    errors: list[str] = []
    later: set[str] = set()
    pages = sorted(SITE.rglob('*.html'))
    styles = sorted(SITE.rglob('*.css'))
    for page in pages:
        parser = Refs()
        parser.feed(page.read_text(encoding='utf-8'))
        for tag, _attr, value in parser.refs:
            check(page, tag, value, errors, later)
    for css in styles:
        for value in CSS_URL.findall(css.read_text(encoding='utf-8')):
            check(css, 'css', value, errors, later)

    print(f'{len(pages)} HTML- und {len(styles)} CSS-Dateien geprüft')
    for item in sorted(later):
        print(f'  Hinweis: {item}')
    for err in errors:
        print(f'  FEHLER {err}')
    print('Keine toten Links.' if not errors else f'{len(errors)} Fehler')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
