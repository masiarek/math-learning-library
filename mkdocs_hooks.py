"""Build-time fixes that would otherwise cost a pinned plugin dependency.

Three jobs, all about finding your way around:

1. **Clean chapter labels.** MkDocs derives a section label from the folder name
   on disk, so `01_Precision/` reads as "01 Precision". The numeric prefix exists
   to set reading order in a file listing; it should not be visible in the nav.
   Only *prefixed* folders are relabelled — a lesson folder takes its label from
   its page's own H1, which is already written the way it should read.

2. **Order the sections.** `NAV_ORDER` states the intended reading order per
   folder, keyed by folder path, listing children by their on-disk name. At the
   top level the chapters are the exception: they sort by name, A to Z, wherever
   the `CHAPTERS` marker sits, because the owner looks a subject up by name. The
   numbers still give the suggested reading order, which Start Here spells out.
   Inside a chapter the lessons keep their reading order, because each chapter
   is one argument and its steps depend on the ones before.

3. **Keep the topic map complete.** `TOPICS.md` groups every lesson by subject.
   A lesson missing from it is logged as a warning, and `mkdocs build --strict`
   (what CI runs) fails on a warning, so a new lesson cannot ship without a
   place on the map.

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

import logging
import re
from pathlib import Path

PREFIX = re.compile(r"^(\d+)[_-]")

# Where the numbered chapters go in the top-level order: all of them, A to Z by
# the name shown in the sidebar, so a new chapter needs no edit here.
CHAPTERS = "*chapters*"

# A lesson page: <numbered chapter>/<lesson>/README.md. Start Here is not one.
LESSON = re.compile(r"^(?!00_)\d+_[^/]+/[^/]+/README\.md$")
TOPIC_MAP = "TOPICS.md"
LINK = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")

log = logging.getLogger("mkdocs.hooks.topic_map")

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
        "TOPICS.md",
        CHAPTERS,
        "GLOSSARY.md",
        "RESOURCES.md",
        "reading_guides",
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
    # pairs; the square root of -1 is a consequence, not an assumption, and
    # e^(i pi) = -1 is the same half turn with a name for every point on it.
    "03_Complex_Numbers": [
        "README.md",
        "multiplication_as_pairs",
        "multiplication_rotates",
        "multiplication_can_be_undone",
        "roots_of_unity",
        "eulers_identity",
    ],
    # Groundwork the other chapters take for granted: how a set that
    # remembers order is built from ones that do not.
    "04_Sets": [
        "README.md",
        "what_is_a_set",
        "python_sets",
        "algebra_of_sets",
        "reading_set_expressions",
        "cartesian_product",
        "cardinality",
    ],
    # One number standing in for many: what each kind of average keeps, and
    # why the names for them nest instead of meaning the same thing.
    "05_Statistics": [
        "README.md",
        "mean_vs_average",
        "share_above_a_cutoff",
    ],
    # Why every book lists the same laws: one menu of four, the list as a test
    # a set can pass, subsets that need only closure, and maps that carry the
    # operations from one set to another.
    "06_Algebraic_Structures": [
        "README.md",
        "laws_of_an_operation",
        "a_definition_is_a_test",
        "subsets_inherit_the_laws",
        "maps_that_keep_the_laws",
    ],
    # What a system of linear equations is, then how to solve one without
    # changing its solutions: the first section of Hefferon's book.
    "07_Linear_Systems": [
        "README.md",
        "linear_equations",
    ],
    # Descartes' idea, in the order a precalculus book takes it: a point is a
    # pair of signed distances, a quadrant is the pair of signs, distance is
    # Pythagoras on the differences, and then the graph of an equation, lines
    # and circles: the whole of the book's first chapter.
    "08_Analytic_Geometry": [
        "README.md",
        "rectangular_coordinates",
        "distance_formula",
        "midpoint_formula",
        "graphs_intercepts_symmetry",
        "lines_and_slope",
        "circles",
    ],
    # The geometry the precalculus book assumes, in its review appendix's
    # order: when three lengths make a right angle, why a formula's power of
    # length is its dimension, and which three measurements fix a triangle.
    # What "if A then B" claims, and which rewordings of it need their own proof.
    "11_Logic": [
        "README.md",
        "converse_and_contrapositive",
    ],
    "10_Geometry": [
        "README.md",
        "pythagorean_theorem",
        "area_and_volume_formulas",
        "congruent_and_similar_triangles",
    ],
    # Calculus as motion, the four pieces Euler's formula leans on: a velocity
    # at an instant, the motion whose velocity is its position, the unit in
    # which turning is walking, and the series that motion forces.
    # How to know that you know, then how to learn so that it stays: the
    # fourth of Flavell's abilities measured, the task deciding what is kept,
    # Bloom's levels climbed on one theorem, and spacing that keeps it cheaply;
    # then the cutoff hidden under a confident yes-or-no, and the belief that
    # stops you trying and so never meets the evidence; last, the planning
    # fallacy, and the hour a schedule needs in reserve; and cognitive load,
    # where the weight of a page depends on the chunks its reader has built;
    # and interleaving, the step a blocked practice sheet lets you skip;
    # and focused and diffuse thinking, why small steps stop on the nearest hill.
    "12_Learning_to_Learn": [
        "README.md",
        "metacognition",
        "count_the_vowels",
        "studying_vs_learning",
        "spaced_retrieval",
        "day_or_night",
        "learned_helplessness",
        "the_buffer_hour",
        "cognitive_load",
        "interleaving",
        "focused_and_diffuse",
    ],
    "09_Calculus": [
        "README.md",
        "derivative_as_velocity",
        "velocity_equals_position",
        "radians",
        "power_series",
        "related_rates",
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
    if CHAPTERS in listed and PREFIX.match(name):
        return (listed.index(CHAPTERS), _label(name).lower())
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


def on_files(files, config):
    """Warn about every lesson that TOPICS.md does not link to."""
    docs = Path(config["docs_dir"])
    topic_map = docs / TOPIC_MAP
    if not topic_map.exists():
        log.warning("%s is missing: it should list every lesson by subject", TOPIC_MAP)
        return files
    linked = {
        (topic_map.parent / target).resolve()
        for target in LINK.findall(topic_map.read_text(encoding="utf-8"))
    }
    for page in files.documentation_pages():
        if LESSON.match(page.src_uri) and (docs / page.src_uri).resolve() not in linked:
            log.warning("%s has no place in %s; add it to the tree", page.src_uri, TOPIC_MAP)
    return files
