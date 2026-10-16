"""Baut die ganze Site nach _site/.  Aufruf:  uv run python scripts/build.py

Phase 3 (erste Version):
  1. validate.py        Wohlgeformtheit, Pflichtfelder, Abbildungen → docs/datenbericht.md
  2. opm chunk          Leseansichten → _site/edition/<datei>.xml/001.html
  3. XML-Quellen        data/*.xml → _site/edition/xml/ (Download «TEI XML»)
Weitere Schritte (works.json, Register, Jinja-Seiten, Suchindex) folgen in späteren Phasen.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'
SITE = ROOT / '_site'
EDITION = SITE / 'edition'


def step(title: str) -> None:
    print(f'\n== {title}', flush=True)


def run(*args: str) -> None:
    """Befehl im Projektordner ausführen; bei Fehler abbrechen."""
    env = {**os.environ, 'PYTHONIOENCODING': 'utf-8'}
    result = subprocess.run(args, cwd=ROOT, env=env)
    if result.returncode != 0:
        sys.exit(f'Abbruch: {" ".join(args)} endete mit Code {result.returncode}')


def remove_fragment_files() -> None:
    """Nebenprodukte von `opm chunk` entfernen.

    OPM schreibt jedes globale Fragment zusätzlich als <name>.html neben die
    Leseseite (für pb-view gedacht). Die Metadaten-Fragmente aus opm.toml sind
    schon in 001.html eingesetzt und werden sonst nicht gebraucht.
    """
    config = tomllib.loads((ROOT / 'opm.toml').read_text(encoding='utf-8'))
    names = {f['name'] for f in config.get('chunking', {}).get('fragments', [])}
    removed = 0
    for doc_dir in EDITION.glob('*.xml'):
        for name in names:
            path = doc_dir / f'{name}.html'
            if path.is_file():
                path.unlink()
                removed += 1
    print(f'{removed} Fragment-Einzeldateien entfernt')


def main() -> int:
    # _site/ wird immer vollständig neu erzeugt, keine Reste früherer Läufe
    if SITE.exists():
        shutil.rmtree(SITE)

    step('1/3 TEI-Dateien prüfen')
    run(sys.executable, 'scripts/validate.py')

    step('2/3 Leseansichten mit OPM')
    # Konfiguration in opm.toml ([chunking]); --force leert _site/edition vorher.
    # Das opm-Programm liegt neben dem Python der uv-Umgebung (.venv/Scripts bzw. .venv/bin).
    opm = shutil.which('opm', path=str(Path(sys.executable).parent)) or 'opm'
    run(opm, 'chunk', 'data', '-o', EDITION.relative_to(ROOT).as_posix(), '--force')
    remove_fragment_files()

    step('3/3 TEI-Quellen zum Herunterladen kopieren')
    xml_dir = EDITION / 'xml'
    xml_dir.mkdir(parents=True, exist_ok=True)
    sources = sorted(DATA.glob('*.xml'))
    for src in sources:
        shutil.copy2(src, xml_dir / src.name)
    print(f'{len(sources)} Dateien nach {xml_dir.relative_to(ROOT)}')

    pages = sorted(EDITION.glob('*.xml/*.html'))
    print(f'\nFertig: {len(pages)} Leseseiten in {EDITION.relative_to(ROOT)}')
    print('Ansehen: uv run opm serve -d _site   →   http://127.0.0.1:8080/edition/')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
