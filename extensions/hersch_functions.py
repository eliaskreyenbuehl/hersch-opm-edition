"""Projekteigene XPath-Funktionen für OPM, im ODD und in opm.toml als ``tp:`` erreichbar.

Jede öffentliche Funktion dieses Moduls wird registriert (siehe
``[transform] xpath_extensions`` in opm.toml). Hilfsfunktionen beginnen deshalb
mit einem Unterstrich.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from opm.runtime.xpath_extensions import expect_string as _expect_string

_TAXONOMY = Path(__file__).resolve().parent.parent / 'assets' / 'i18n' / 'taxonomy.json'


@lru_cache(maxsize=1)
def _taxonomy() -> dict:
    return json.loads(_TAXONOMY.read_text(encoding='utf-8'))


def taxonomy_label(scheme: Any, key: Any, lang: Any) -> str:
    """Bezeichnung einer Kategorie aus assets/i18n/taxonomy.json.

    ``tp:taxonomy_label('hersch_genre', 'article', 'de')`` → ``Artikel``.
    Fehlt die Bezeichnung, kommt der Schlüssel selbst zurück (Entscheid
    2026-10-14: Kategorien ohne Label mit dem Schlüssel anzeigen).
    """
    scheme_s = _expect_string(scheme, arg_name='taxonomy_label(scheme)').strip()
    key_s = _expect_string(key, arg_name='taxonomy_label(key)').strip().lstrip('#')
    lang_s = _expect_string(lang, arg_name='taxonomy_label(lang)').strip()
    entry = _taxonomy().get(scheme_s, {}).get(key_s, {})
    return entry.get(lang_s) or key_s if isinstance(entry, dict) else key_s
