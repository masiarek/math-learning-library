"""Build-time fixes that would otherwise cost a pinned plugin dependency.

Two jobs, both about the sidebar:

1. **Clean chapter labels.** MkDocs derives a section label from the folder name
   on disk, so `01_Precision/` reads as "01 Precision". The numeric prefix exists
   to set reading order in a file listing; it should not be visible in the nav.
   Only *prefixed* folders are relabelled — a lesson folder takes its label from
   its page's own H1, which is already written the way it should read.

2. **Order the sections.** `NAV_ORDER` states the intended reading order per
   folder, keyed by folder path, listing children by their on-disk name.

Why order here rather than by renaming files: a filename is a permanent URL.
Renumbering `03_` to `04_` to insert a lesson would move every page after it and
break any link anyone saved. Ordering is presentation, so it belongs in the
presentation layer. Unlisted pages keep their alphabetical slot at the bottom, so
adding a page needs no edit here.

One structural note that is easy to get wrong: the top-level object MkDocs hands
`on_nav` is a `Navigation`, whose children live on `.items`. Only `Section` has
`.children`. A hook that reaches for `.children` at the top level silently does
nothing at all — the build still succeeds, and the sidebar is simply never
touched.
"""

from __future__ import annotations

import re

PREFIX = re.compile(r"^(\d+)[_-]")

# Words the naive title-caser gets wrong.
FIXUPS = {
    "Vs": "vs",
    "And": "and",
    "Or": "or",
    "The": "the",
    "To": "to",
    "A": "a",
    "In": "in",
    "Of": "of",
}

# Reading order per folder path. Children named by on-disk name; anything not
# listed sorts alphabetically after the listed ones.
NAV_ORDER: dict[str, list[str]] = {
    "": [
        "index.md",
        "00_Start_Here",
        "01_Precision",
        "02_Measure_Zero",
        "03_Complex_Numbers",
        "04_Sets",
        "GLOSSARY.md",
        "ROADMAP.md",
    ],
    # One argument, in six steps: what kind of number is this, what does the
    # notation claim, how good is an approximation when a digit count cannot
    # say, what is the rigorous version of that claim, what the machine does to
    # a number it cannot hold, and where does the claim collapse.
    "01_Precision": [
        "README.md",
        "exact_vs_approximate",
        "significant_figures",
        "relative_error",
        "uncertainty_propagation",
        "machine_numbers",
        "catastrophic_cancellation",
    ],
    # One argument, in six steps: what "no length" means without measuring,
    # two sets that have no length despite infinitely many points (countable,
    # then uncountable), the set that looks just as thin and is not, a function
    # whose whole climb happens on a set of length zero, and what zero then
    # means for chance.
    "02_Measure_Zero": [
        "README.md",
        "what_measure_zero_means",
        "countable_sets",
        "cantor_set",
        "fat_cantor_set",
        "cantor_function",
        "probability_zero",
    ],
    # A complex number is a pair of reals and multiplication is a rule on
    # pairs; the square root of -1 is a consequence, not an assumption.
    "03_Complex_Numbers": [
        "README.md",
        "multiplication_as_pairs",
        "multiplication_rotates",
        "multiplication_can_be_undone",
    ],
    # Groundwork the other chapters take for granted: how a set that
    # remembers order is built from ones that do not.
    "04_Sets": [
        "README.md",
        "cartesian_product",
        "cardinality",
    ],
}


def _label(name: str) -> str:
    """Folder name on disk -> sidebar label."""
    words = PREFIX.sub("", name).replace("_", " ").replace("-", " ").split()
    out = [FIXUPS.get(w.capitalize(), w.capitalize()) for w in words]
    if out:
        out[0] = out[0][0].upper() + out[0][1:]
    return " ".join(out)


def _is_section(item) -> bool:
    return getattr(item, "children", None) is not None


def _first_src(item) -> str:
    """Source path of `item`, or of the first page anywhere beneath it."""
    page_file = getattr(item, "file", None)
    if page_file is not None:
        return page_file.src_uri
    for child in getattr(item, "children", None) or []:
        found = _first_src(child)
        if found:
            return found
    return ""


def _on_disk_name(item, depth: int) -> str:
    """The name NAV_ORDER lists this child by: a filename, or a folder segment."""
    src = _first_src(item)
    if not src:
        return (getattr(item, "title", "") or "").lower()
    parts = src.split("/")
    if not _is_section(item):
        return parts[-1]
    return parts[depth] if depth < len(parts) - 1 else parts[-1]


def _order_key(path: str, name: str) -> tuple[int, str]:
    listed = NAV_ORDER.get(path, [])
    if name in listed:
        return (listed.index(name), "")
    return (len(listed), name.lower())


def _readme_h1(section) -> str:
    """The H1 of a section's own README.md, read from disk ("" if it has none)."""
    for child in section.children:
        page_file = getattr(child, "file", None)
        if page_file is None or page_file.src_uri.rsplit("/", 1)[-1] != "README.md":
            continue
        with open(page_file.abs_src_path, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("# "):
                    return line[2:].strip()
    return ""


def _visit(items: list, path: str, depth: int) -> None:
    for child in items:
        if not _is_section(child):
            continue
        name = _on_disk_name(child, depth)
        # A numbered chapter folder is relabelled from its name. A lesson folder
        # takes its page's H1, which is authored prose. Left alone, MkDocs titles
        # a section from its folder name, and that only looks right while the two
        # happen to agree: `fat_cantor_set` came out "Fat cantor set", losing the
        # capital on a proper noun and the article in the H1. Title-casing the
        # folder name instead would fight the page just as badly
        # ("Significant Figures").
        if PREFIX.match(name):
            child.title = _label(name)
        else:
            child.title = _readme_h1(child) or child.title

    items.sort(key=lambda c: _order_key(path, _on_disk_name(c, depth)))

    for child in items:
        if not _is_section(child):
            continue
        name = _on_disk_name(child, depth)
        _visit(child.children, f"{path}/{name}".lstrip("/"), depth + 1)


def on_nav(nav, config, files):
    """Relabel numbered chapters and apply NAV_ORDER, depth-first."""
    _visit(nav.items, "", 0)
    return nav
