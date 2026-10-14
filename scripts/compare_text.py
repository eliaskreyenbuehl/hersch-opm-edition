"""Hilfsskript Phase 2: Text des Lesebereichs (div.tei-body) aus einer OPM-Ausgabe
normalisieren und Prüfsumme, Länge und Seitenzahlen ausgeben, für den Vergleich mit der
Live-Edition (gleiche Normalisierung im Browser)."""
import hashlib
import re
import sys

from lxml import html


def body_text(path):
    doc = html.parse(path)
    body = doc.xpath("//div[contains(concat(' ', @class, ' '), ' tei-body ')]")[0]
    for t in body.xpath(".//template|.//style|.//script"):
        t.drop_tree()
    # ﻿ zählt in JavaScript zu \s, in Python nicht
    text = re.sub(r"[\s﻿]+", " ", body.text_content()).strip()
    pbs = [e.text_content().strip() for e in body.xpath(".//*[contains(concat(' ', @class, ' '), ' pb ')]")]
    return text, pbs


if __name__ == "__main__":
    for p in sys.argv[1:]:
        text, pbs = body_text(p)
        print(p, len(text), hashlib.sha256(text.encode()).hexdigest()[:16], ",".join(pbs))
