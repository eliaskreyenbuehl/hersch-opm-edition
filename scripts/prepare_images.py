"""Webfassungen der Abbildungen erzeugen.

Die Scans in assets/images/edition/ (lokal, nicht eingecheckt) sind für das Web
zu gross. Dieses Skript rechnet sie einmalig auf höchstens MAX_SIDE Pixel
(längste Seite) herunter und legt sie nach assets/img/edition/. Nur diese
Fassungen werden eingecheckt und veröffentlicht.

Aufruf:  uv run python scripts/prepare_images.py [--force]
Ohne --force werden bereits vorhandene Webfassungen übersprungen.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'assets' / 'images' / 'edition'
TARGET = ROOT / 'assets' / 'img' / 'edition'
MAX_SIDE = 2000
QUALITY = 82

# Scans mit bis zu 30 Megapixeln sind gewollt, keine "Dekompressionsbombe".
Image.MAX_IMAGE_PIXELS = None


def main() -> int:
    force = '--force' in sys.argv
    if not SOURCE.is_dir():
        print(f'Kein Quellordner {SOURCE.relative_to(ROOT)} – nichts zu tun.')
        return 0
    TARGET.mkdir(parents=True, exist_ok=True)
    total_in = total_out = 0
    for src in sorted(SOURCE.glob('*.jpg')):
        dst = TARGET / src.name
        total_in += src.stat().st_size
        if dst.exists() and not force:
            total_out += dst.stat().st_size
            continue
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im)
            if im.mode not in ('RGB', 'L'):
                im = im.convert('RGB')
            im.thumbnail((MAX_SIDE, MAX_SIDE), Image.Resampling.LANCZOS)
            im.save(dst, 'JPEG', quality=QUALITY, optimize=True, progressive=True)
        total_out += dst.stat().st_size
        print(f'{src.name}: {src.stat().st_size // 1024} KB -> {dst.stat().st_size // 1024} KB')
    print(f'Gesamt: {total_in / 1e6:.1f} MB -> {total_out / 1e6:.1f} MB')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
