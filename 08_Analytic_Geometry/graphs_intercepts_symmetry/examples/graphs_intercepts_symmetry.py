#!/usr/bin/env python3
"""Graphs of equations: the graph is a set of points, intercepts and symmetry are tests on it.

Run:  python3 graphs_intercepts_symmetry.py

The graph of an equation in x and y is the set of all points (x, y) whose
coordinates make the equation true. Everything on this page follows from that
one sentence:

    on the graph?      substitute the point and see if the equation holds
    x-intercepts       the graph's points with y = 0, so set y = 0 and solve
    y-intercepts       the graph's points with x = 0, so set x = 0 and solve
    symmetry           a mirror image of every point is also on the graph

Each equation is written as F(x, y) = 0. Numbers are fractions, so "the
equation holds" means exactly. The pictures show only the points with whole
number coordinates that satisfy the equation exactly as *; between them the graph
is a smooth curve, and the grid marks each square it passes through.
"""

from fractions import Fraction as F

EQUATIONS = [
    # name, F(x, y) with the graph as F = 0
    ("y = x^2 - 4", lambda x, y: x * x - 4 - y),
    ("x = y^2", lambda x, y: y * y - x),
    ("y = x^3 - x", lambda x, y: x ** 3 - x - y),
    ("x^2 + 4y^2 = 16", lambda x, y: x * x + 4 * y * y - 16),
    ("y = x + 2", lambda x, y: x + 2 - y),
    ("y = x^2 + 1", lambda x, y: x * x + 1 - y),
]

R = 6  # the grid runs from -R to R
SAMPLES = [F(n, d) for n in range(-7, 8) for d in (1, 2, 3)]


def crosses(f, x: int, y: int) -> bool:
    """Does the curve F = 0 pass through the unit cell centred on (x, y)?

    It does if F is 0 somewhere on the cell's corners or centre, or takes both
    signs among them: F is a polynomial, so it cannot change sign without
    passing through 0 in between.
    """
    h = F(1, 2)
    vals = [f(F(x) + dx, F(y) + dy) for dx in (-h, 0, h) for dy in (-h, 0, h)]
    return 0 in vals or (min(vals) < 0 < max(vals))


def plot(f) -> list[str]:
    rows = []
    for y in range(R, -R - 1, -1):
        cells = []
        for x in range(-R, R + 1):
            if f(F(x), F(y)) == 0:
                cells.append("*")
            elif crosses(f, x, y):
                cells.append("o")
            elif x == 0 and y == 0:
                cells.append("+")
            elif x == 0:
                cells.append("|")
            elif y == 0:
                cells.append("-")
            else:
                cells.append(".")
        rows.append(f"   {y:>3} " + "".join(f"{c:>3}" for c in cells))
    rows.append("       " + "".join(f"{x:>3}" for x in range(-R, R + 1)) + "   x")
    return rows


def roots(g) -> list[F]:
    """Solutions of g(t) = 0 among fractions with small numerator and denominator."""
    found = {F(n, d) for n in range(-20, 21) for d in (1, 2, 3, 4) if g(F(n, d)) == 0}
    return sorted(found)


def symmetric(f, mirror) -> bool:
    """Replacing (x, y) by its mirror image gives an equivalent equation: F' = F or F' = -F."""
    same = all(f(*mirror(x, y)) == f(x, y) for x in SAMPLES for y in SAMPLES)
    flip = all(f(*mirror(x, y)) == -f(x, y) for x in SAMPLES for y in SAMPLES)
    return same or flip


MIRRORS = [
    ("x-axis", "replace y by -y", lambda x, y: (x, -y)),
    ("y-axis", "replace x by -x", lambda x, y: (-x, y)),
    ("origin", "replace both", lambda x, y: (-x, -y)),
]


def fmt(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    name, f = EQUATIONS[0]
    print(f"1. A GRAPH IS A SET OF POINTS: {name}")
    for line in plot(f):
        print(line)
    print("   * is a whole-number point (x, y) that makes the equation true exactly;")
    print("   o is a square the curve passes through between such points.")
    print()

    print("2. IS THE POINT ON THE GRAPH? SUBSTITUTE AND SEE")
    for p in [(2, 0), (1, -3), (1, -2), (-3, 5), (0, 4)]:
        x, y = F(p[0]), F(p[1])
        lhs, rhs = y, x * x - 4
        verdict = "on the graph" if lhs == rhs else "not on it"
        print(f"   ({p[0]:>2}, {p[1]:>2}):  y = {fmt(lhs):>2},  x^2 - 4 = {fmt(rhs):>2}   {verdict}")
    print("   (0, 4) fails although (0, -4) passes: a sign is a different point.")
    print()

    print("3. INTERCEPTS: SET THE OTHER COORDINATE TO 0, THEN SOLVE")
    print(f"   {'equation':18}{'x-intercepts (y = 0)':>24}{'y-intercepts (x = 0)':>24}")
    for name, f in EQUATIONS:
        xs = roots(lambda t: f(t, F(0)))
        ys = roots(lambda t: f(F(0), t))
        show = lambda v: ", ".join(fmt(t) for t in v) if v else "none"
        print(f"   {name:18}{show(xs):>24}{show(ys):>24}")
    print("   An intercept is a single number, a coordinate: the x-intercepts of")
    print("   y = x^2 - 4 are -2 and 2, and the points are (-2, 0) and (2, 0).")
    print("   y = x^2 + 1 never reaches the x-axis: x^2 = -1 has no real solution.")
    print("   x = y^2 has 0 as both: the graph goes through the origin.")
    print()

    print("4. SYMMETRY: DOES THE MIRROR IMAGE OF THE EQUATION SAY THE SAME THING?")
    print(f"   {'equation':18}" + "".join(f"{m[0]:>10}" for m in MIRRORS))
    for name, f in EQUATIONS:
        print(f"   {name:18}" + "".join(f"{('yes' if symmetric(f, m[2]) else 'no'):>10}" for m in MIRRORS))
    print("   x-axis: replace y by -y.  y-axis: replace x by -x.  origin: replace both.")
    print("   If the new equation is equivalent to the old one, the graph has that symmetry.")
    print()

    print("5. THE TEST, BY HAND, ON y = x^3 - x")
    print("   origin: -y = (-x)^3 - (-x) = -x^3 + x; multiply by -1: y = x^3 - x.  Same: symmetric.")
    print("   y-axis:  y = (-x)^3 - (-x) = -x^3 + x.  Different equation: not symmetric.")
    f = EQUATIONS[2][1]
    print("   A witness for 'not': (2, 6) is on the graph, its y-axis mirror (-2, 6) is not:",
          f"F(2, 6) = {fmt(f(F(2), F(6)))}, F(-2, 6) = {fmt(f(F(-2), F(6)))}.")
    print()

    print("6. ANY TWO SYMMETRIES FORCE THE THIRD")
    print("   Reflecting in the x-axis and then the y-axis is a half turn about the origin:")
    print("   (x, y) -> (x, -y) -> (-x, -y). So x^2 + 4y^2 = 16, with both axis symmetries,")
    print("   gets origin symmetry for free. The ellipse:")
    for line in plot(EQUATIONS[3][1]):
        print(line)
    print()

    print("7. A GRAPH OF y = f(x) WITH x-AXIS SYMMETRY IS FLAT")
    print("   If (x, y) and (x, -y) are both on it, one x has two y's unless y = 0.")
    print("   So among graphs of functions, only y = 0 is symmetric about the x-axis;")
    print("   x = y^2 is symmetric about it precisely because y is not a function of x there.")


if __name__ == "__main__":
    main()
