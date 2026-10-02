#!/usr/bin/env python3
"""Make an Anki deck from the symbol index at the end of GLOSSARY.md.

    python3 tools/symbol_index_anki.py            # write the deck
    python3 tools/symbol_index_anki.py --check    # write nothing, fail if it is stale

The index table is the source: one row per symbol group, with how to read it
and where it is explained. Each row becomes two cards, symbol to reading and
reading to symbol, so the deck can never drift from the table. The deck lives
under the lesson about reading notation and is folded into the chapter's
combined deck by tools/combine_anki.py.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "GLOSSARY.md"
DECK = ROOT / "04_Sets" / "reading_set_expressions" / "anki" / "symbol_index.txt"
HEAD = "#separator:tab\n#html:false\n#notetype:Basic\n#deck:Math::Sets::Symbol index\n"


def rows():
    text = GLOSSARY.read_text(encoding="utf-8")
    start = text.index("## Symbol index")
    out = []
    for line in text[start:].splitlines():
        if not line.startswith("| ") or line.startswith("| Symbol |"):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        if len(cells) != 3:
            sys.exit(f"symbol index row has {len(cells)} cells: {line}")
        symbol, reading, where = cells
        symbol = symbol.replace("\\|", "|")
        m = re.match(r"\[(.+?)\]\((.+?)\)", where)
        label = m.group(1) if m else where
        label = label.replace("glossary: ", "glossary entry: ")
        out.append((symbol, reading, label))
    if not out:
        sys.exit("no rows found under '## Symbol index'")
    return out


def build() -> str:
    lines = [HEAD.rstrip("\n")]
    for symbol, reading, label in rows():
        front = f"Read the symbol: {symbol}"
        back = f"{reading}. Explained under: {label}."
        lines.append("\t".join([front, back, "symbol"]))
        front = f"Which symbol says: {reading}?"
        back = f"{symbol} (explained under: {label})"
        lines.append("\t".join([front, back, "symbol reverse"]))
    for line in lines[1:]:
        if '"' in line or line.count("\t") != 2:
            sys.exit(f"bad card: {line}")
    return "\n".join(lines) + "\n"


def main() -> None:
    deck = build()
    n = deck.count("\n") - HEAD.count("\n")
    if "--check" in sys.argv:
        if not DECK.exists() or DECK.read_text(encoding="utf-8") != deck:
            sys.exit(f"{DECK.relative_to(ROOT)} is stale: run python3 tools/symbol_index_anki.py")
        print(f"{DECK.relative_to(ROOT)}: up to date, {n} cards")
    else:
        DECK.write_text(deck, encoding="utf-8")
        print(f"wrote {DECK.relative_to(ROOT)}: {n} cards from the symbol index")


if __name__ == "__main__":
    main()
