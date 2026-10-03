#!/usr/bin/env python3
"""Three school curricula as sets of topics, compared with set operations.

Run:  python3 curriculum_sets.py

An American precalculus or calculus syllabus, the Polish podstawa programowa
for liceum, and the German KMK standards for the Abitur all name their topics
differently and cut the years differently. Written as sets, they can be
compared exactly: which topics all three teach, which one system teaches
alone, where the American "precalculus" year lands in the other two, and
how far each system gets into calculus itself.

The data is a reading of the three documents from memory (the page says how
sure each row is). The program's job is to make every claim on the page a
set operation that can be re-run when a row is corrected.

Codes for the courses:
    US-PRE   American precalculus (grade 11 or 12)
    US-AB    AP Calculus AB
    US-BC    AP Calculus BC, beyond AB
    PL-P     Polish liceum, zakres podstawowy (matura, compulsory level)
    PL-R     Polish liceum, zakres rozszerzony (matura, extended level)
    PL-SP    Polish szkoła podstawowa, classes 7 and 8, before liceum
    DE-I     German Sekundarstufe I, classes 5 to 10, before the Oberstufe
    DE-G     German Oberstufe, grundlegendes Anforderungsniveau (Grundkurs)
    DE-E     German Oberstufe, erhöhtes Anforderungsniveau (Leistungskurs)
A topic listed under PL-P is also taught at PL-R; one under DE-G also at DE-E;
one under US-AB also in US-BC. The sets below list the lowest course only,
and the program closes them upward.
"""

# topic -> set of course codes where it is first taught
WHERE_TAUGHT: dict[str, set[str]] = {
    # the algebra behind precalculus
    "exponent laws, roots, rational exponents": {"US-PRE", "PL-P", "DE-I"},
    "quadratic equations and the quadratic formula": {"US-PRE", "PL-P", "DE-I"},
    "polynomials: zeros, factoring, division": {"US-PRE", "PL-R", "DE-G"},
    "rational functions and asymptotes": {"US-PRE", "PL-R", "DE-E"},
    "absolute value and intervals": {"US-PRE", "PL-P", "DE-I"},
    # functions
    "functions: domain, range, graph, composition": {"US-PRE", "PL-P", "DE-I"},
    "inverse functions": {"US-PRE", "PL-R", "DE-G"},
    "shifting and stretching a graph": {"US-PRE", "PL-P", "DE-I"},
    "exponential functions": {"US-PRE", "PL-P", "DE-I"},
    "logarithms and logarithmic functions": {"US-PRE", "PL-P", "DE-G"},
    # trigonometry
    "right-triangle trigonometry": {"US-PRE", "PL-P", "DE-I"},
    "unit circle, radians, trigonometric functions of any angle": {"US-PRE", "PL-R", "DE-G"},
    "trigonometric identities and equations": {"US-PRE", "PL-R", "DE-E"},
    "law of sines and law of cosines": {"US-PRE", "PL-P", "DE-I"},
    # analytic geometry and algebra beyond functions
    "lines, slope, distance and midpoint in coordinates": {"US-PRE", "PL-P", "DE-I"},
    "the circle in coordinates": {"US-PRE", "PL-P", "DE-G"},
    "conic sections: parabola, ellipse, hyperbola": {"US-PRE"},
    "parametric equations": {"US-PRE", "DE-E"},
    "polar coordinates": {"US-PRE"},
    "complex numbers, polar form, de Moivre": {"US-PRE"},
    "systems of linear equations": {"US-PRE", "PL-P", "DE-I"},
    "matrices and determinants": {"US-PRE", "DE-E"},
    "vectors in the plane": {"US-PRE", "PL-P", "DE-G"},
    "vectors in space, lines and planes, dot product": {"DE-G"},
    "sequences and series, Σ notation": {"US-PRE", "PL-P", "DE-I"},
    "limit of a sequence, sum of a geometric series": {"US-PRE", "PL-R", "DE-G"},
    "mathematical induction": {"US-PRE", "PL-R"},
    "binomial theorem": {"US-PRE", "PL-R", "DE-G"},
    "combinatorics: permutations and combinations": {"US-PRE", "PL-P", "DE-G"},
    "probability: events, conditional probability": {"US-PRE", "PL-P", "DE-I"},
    "binomial distribution, expected value": {"PL-R", "DE-G"},
    "hypothesis tests and the normal distribution": {"DE-G"},
    "descriptive statistics: mean, median, deviation": {"PL-SP", "DE-I"},
    "solid geometry: prisms, pyramids, spheres, volumes": {"PL-SP", "DE-I"},
    "plane geometry with proof: triangles, circles, similarity": {"PL-P", "DE-I"},
    "Pythagorean theorem, similar triangles, area and volume formulas": {"US-PRE", "PL-SP", "DE-I"},
    # calculus
    "limit of a function, continuity": {"US-AB", "PL-R", "DE-G"},
    "the derivative and its rules": {"US-AB", "PL-R", "DE-G"},
    "chain rule": {"US-AB", "PL-R", "DE-G"},
    "curve sketching, extrema, optimisation": {"US-AB", "PL-R", "DE-G"},
    "related rates": {"US-AB"},
    "derivatives of exponential and trigonometric functions": {"US-AB", "DE-G"},
    "antiderivative, definite integral, fundamental theorem": {"US-AB", "DE-G"},
    "area between curves, volumes": {"US-AB", "DE-G"},
    "integration by substitution": {"US-AB", "DE-E"},
    "integration by parts, partial fractions": {"US-BC", "DE-E"},
    "differential equations: separable, growth and decay": {"US-AB", "DE-E"},
    "Taylor and power series": {"US-BC"},
    "parametric, polar and vector-valued functions in calculus": {"US-BC"},
}

# Each course includes everything taught at a lower course of the same system.
INCLUDES: dict[str, set[str]] = {
    "US-PRE": {"US-PRE"},
    "US-AB": {"US-PRE", "US-AB"},
    "US-BC": {"US-PRE", "US-AB", "US-BC"},
    "PL-SP": {"PL-SP"},
    "PL-P": {"PL-SP", "PL-P"},
    "PL-R": {"PL-SP", "PL-P", "PL-R"},
    "DE-I": {"DE-I"},
    "DE-G": {"DE-I", "DE-G"},
    "DE-E": {"DE-I", "DE-G", "DE-E"},
}

SYSTEM_OF = {code: code.split("-")[0] for code in INCLUDES}


def taught_by(course: str) -> set[str]:
    """Every topic a student finishing `course` has met."""
    lower = INCLUDES[course]
    return {t for t, codes in WHERE_TAUGHT.items() if codes & lower}


def show(title: str, topics: set[str]) -> None:
    print(f"   {title} ({len(topics)})")
    for t in sorted(topics):
        print(f"      - {t}")
    if not topics:
        print("      (none)")


def main() -> None:
    all_topics = set(WHERE_TAUGHT)
    us_pre = taught_by("US-PRE")
    us_ab = taught_by("US-AB")
    us_bc = taught_by("US-BC")
    pl_p = taught_by("PL-P")
    pl_r = taught_by("PL-R")
    de_g = taught_by("DE-G")
    de_e = taught_by("DE-E")

    print("1. THE COURSES AS SETS")
    print(f"   {len(all_topics)} topics in the table. How many each school-leaving course has met:")
    for code, name in (
        ("US-PRE", "US precalculus"),
        ("US-AB", "US precalculus + AP Calculus AB"),
        ("US-BC", "US precalculus + AP Calculus BC"),
        ("PL-P", "Polish matura, zakres podstawowy"),
        ("PL-R", "Polish matura, zakres rozszerzony"),
        ("DE-G", "German Abitur, Grundkurs"),
        ("DE-E", "German Abitur, Leistungskurs"),
    ):
        print(f"      {code:7} {len(taught_by(code)):>3}   {name}")
    print()

    print("2. THE COMMON CORE: taught to every school leaver on the stronger track")
    show("US-BC ∩ PL-R ∩ DE-E", us_bc & pl_r & de_e)
    print()

    print("3. TAUGHT BY ONE SYSTEM ONLY (strongest track of each)")
    show("US only: US-BC − (PL-R ∪ DE-E)", us_bc - (pl_r | de_e))
    show("Poland only: PL-R − (US-BC ∪ DE-E)", pl_r - (us_bc | de_e))
    show("Germany only: DE-E − (US-BC ∪ PL-R)", de_e - (us_bc | pl_r))
    print()

    print("4. WHERE THE AMERICAN PRECALCULUS YEAR LANDS")
    print("   Of the topics American precalculus teaches, how many the other systems")
    print("   teach before the final two years, in them, or not at all:")
    for system, early, late in (("Poland", "PL-SP", "PL-R"), ("Germany", "DE-I", "DE-E")):
        before = {t for t in us_pre if WHERE_TAUGHT[t] & INCLUDES[early]}
        inside = {t for t in us_pre if WHERE_TAUGHT[t] & INCLUDES[late]} - before
        never = us_pre - before - inside
        print(f"   {system}: {len(before)} before, {len(inside)} during, {len(never)} never, of {len(us_pre)}")
    print("   Precalculus is not a course anywhere but America: its content is")
    print("   spread over the years before the Oberstufe or the liceum, and the")
    print("   rest is either in the final years or absent.")
    print()

    print("5. HOW FAR EACH SYSTEM GETS INTO CALCULUS")
    calculus = {t for t, codes in WHERE_TAUGHT.items() if codes & {"US-AB", "US-BC"}}
    for code in ("PL-P", "PL-R", "DE-G", "DE-E", "US-AB", "US-BC"):
        have = taught_by(code) & calculus
        print(f"      {code:7} {len(have):>2} of {len(calculus)} AP Calculus topics")
    show("in AP Calculus AB but not in the Polish rozszerzony", us_ab - pl_r)
    show("in the Polish rozszerzony or German Grundkurs calculus but not in AP AB", (pl_r | de_g) & calculus - us_ab)
    show("Poland rozszerzony has, Germany Grundkurs has not", pl_r - de_g)
    show("Germany Grundkurs has, Poland rozszerzony has not", de_g - pl_r)
    print()

    print("6. CHECKS")
    bad_codes = {c for codes in WHERE_TAUGHT.values() for c in codes} - set(INCLUDES)
    print(f"   every code in the table is a known course: {not bad_codes}")
    orphan = {t for t, codes in WHERE_TAUGHT.items() if not codes}
    print(f"   every topic is taught somewhere: {not orphan}")
    closed = us_pre <= us_ab <= us_bc and pl_p <= pl_r and de_g <= de_e
    print(f"   each system's tracks nest, lower inside higher: {closed}")
    # The identity behind section 3: the three "only" sets and the pairwise
    # overlaps partition the union, so their sizes add up to the union's size.
    union = us_bc | pl_r | de_e
    only = (us_bc - (pl_r | de_e)) | (pl_r - (us_bc | de_e)) | (de_e - (us_bc | pl_r))
    shared = union - only
    print(f"   |only one| + |shared by two or more| = |union|: {len(only)} + {len(shared)} = {len(union)}: {len(only) + len(shared) == len(union)}")


if __name__ == "__main__":
    main()
