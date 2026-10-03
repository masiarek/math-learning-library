#!/usr/bin/env python3
"""Distance is the four properties: taxicab, Chebyshev, Hamming, and the one that fails.

Run:  python3 other_distances.py

The Euclidean formula is one distance among many. What makes a function
a distance is four properties (a metric): non-negative, zero only for
one point, symmetric, triangle inequality. The program measures one pair
of points four ways, draws the "circle" of each distance on a grid of
lattice points, finds the one counterexample that disqualifies the
p = 1/2 formula, shows that only the Euclidean distance survives a
rotation, and checks all four properties, exhaustively, for the Hamming
distance on 3-bit strings, a distance between things that are not points.
Everything is exact: squared Euclidean distances, integer taxicab and
Chebyshev distances, and a rotation with cos = 3/5, sin = 4/5.
"""

from fractions import Fraction
from itertools import product


def euclid2(p, q):
    """Squared Euclidean distance, exact."""
    return sum((b - a) ** 2 for a, b in zip(p, q))


def taxicab(p, q):
    return sum(abs(b - a) for a, b in zip(p, q))


def chebyshev(p, q):
    return max(abs(b - a) for a, b in zip(p, q))


def hamming(s, t):
    return sum(a != b for a, b in zip(s, t))


def rotate(p):
    """Rotate by the angle with cos = 3/5 and sin = 4/5: a 3-4-5 triangle, so exact."""
    c, s = Fraction(3, 5), Fraction(4, 5)
    x, y = p
    return (c * x - s * y, s * x + c * y)


def fmt(p):
    return "(" + ", ".join(str(c) for c in p) + ")"


def check_metric(points, d):
    """The four properties on every pair and every triple. Returns four booleans."""
    nonneg = all(d(p, q) >= 0 for p in points for q in points)
    zero = all((d(p, q) == 0) == (p == q) for p in points for q in points)
    sym = all(d(p, q) == d(q, p) for p in points for q in points)
    tri = all(d(p, r) <= d(p, q) + d(q, r) for p in points for q in points for r in points)
    return nonneg, zero, sym, tri


def main() -> None:
    print("1. ONE PAIR OF POINTS, MEASURED FOUR WAYS")
    p, q = (1, 3), (5, 6)
    dx, dy = 4, 3
    print(f"   P = {p}, Q = {q}: the changes are {dx} across and {dy} up.")
    print(f"   Euclidean  sqrt(dx^2 + dy^2)   = sqrt({dx * dx + dy * dy}) = 5      the straight line")
    print(f"   taxicab    |dx| + |dy|          = {dx + dy}              along the streets of a grid")
    print(f"   Chebyshev  max(|dx|, |dy|)      = {max(dx, dy)}              moves of a chess king")
    print(f"   p = 1/2    (sqrt|dx| + sqrt|dy|)^2 = (2 + sqrt 3)^2 = {(2 + 3 ** 0.5) ** 2:.2f}    a formula of the same family")
    print("   Four numbers, one pair of points. Which of them deserve the word distance?")
    print()

    print("2. THE CIRCLE OF RADIUS 3 AROUND THE ORIGIN, UNDER EACH DISTANCE")
    print("   Lattice points (x, y) with -4 <= x, y <= 4; # marks a point at distance at most 3.")
    metrics = [("Euclidean", lambda a, b: euclid2(a, b) <= 9),
               ("taxicab", lambda a, b: taxicab(a, b) <= 3),
               ("Chebyshev", lambda a, b: chebyshev(a, b) <= 3)]
    print(("   " + "".join(f"{name:<14}" for name, _ in metrics)).rstrip())
    for y in range(4, -5, -1):
        row = ""
        for _, inside in metrics:
            row += "".join("#" if inside((0, 0), (x, y)) else "." for x in range(-4, 5)) + "     "
        print(("   " + row).rstrip())
    counts = [sum(inside((0, 0), pt) for pt in product(range(-4, 5), repeat=2)) for _, inside in metrics]
    print(f"   Points inside: {counts[0]}, {counts[1]}, {counts[2]}. A disc, a diamond, a square: the shape of")
    print("   a circle is a fact about the distance, not about the plane.")
    print()

    print("3. THE ONE THAT FAILS: p = 1/2 BREAKS THE TRIANGLE INEQUALITY")
    half = lambda a, b: (sum(abs(y - x) ** 0.5 for x, y in zip(a, b))) ** 2
    P, Q, R = (0, 0), (1, 0), (1, 1)
    print(f"   P = {P}, Q = {Q}, R = {R}.")
    print(f"   d(P, Q) = (sqrt 1)^2 = {half(P, Q):.0f},  d(Q, R) = (sqrt 1)^2 = {half(Q, R):.0f},  d(P, R) = (sqrt 1 + sqrt 1)^2 = {half(P, R):.0f}.")
    print(f"   Going straight from P to R costs {half(P, R):.0f}; going through Q costs {half(P, Q) + half(Q, R):.0f}. The detour is shorter.")
    print("   One triple is enough: the formula is not a distance. The other three properties hold")
    print("   and do not save it. (Every p >= 1 gives a distance; every p < 1 fails this way.)")
    print()

    print("4. TURN THE PLANE: ONLY THE EUCLIDEAN DISTANCE DOES NOT NOTICE")
    print("   Rotate by the angle with cos = 3/5, sin = 4/5 (exact), and measure the same two points.")
    pts = [(Fraction(1), Fraction(0)), (Fraction(5), Fraction(3))]
    rot = [rotate(pt) for pt in pts]
    print(f"   Before: {fmt(pts[0])} and {fmt(pts[1])}")
    print(f"   After:  {fmt(rot[0])} and {fmt(rot[1])}")
    for name, d in [("Euclidean^2", euclid2), ("taxicab", taxicab), ("Chebyshev", chebyshev)]:
        before, after = d(*pts), d(*rot)
        verdict = "unchanged" if before == after else "changed"
        print(f"   {name:<12} before {str(before):<6} after {str(after):<8} {verdict}")
    print("   A ruler does not care which way it is held. Among the three, only the Euclidean")
    print("   distance passes that test, which is why geometry chooses Pythagoras.")
    print()

    print("5. THE FOUR PROPERTIES, CHECKED EXHAUSTIVELY")
    grid = list(product(range(-2, 3), repeat=2))
    names = ["non-negative", "zero only for one point", "symmetric", "triangle inequality"]
    print(f"   On the {len(grid)} lattice points with coordinates in -2..2 ({len(grid) ** 3} triples):")
    for name, d in [("squared Euclidean", euclid2), ("taxicab", taxicab), ("Chebyshev", chebyshev)]:
        res = check_metric(grid, d)
        print((f"   {name:<18} " + "  ".join(f"{n}: {str(r):<5}" for n, r in zip(names, res))).rstrip())
    print("   (Squared Euclidean distance fails the triangle inequality: 0-1-2 on a line gives 4 > 1 + 1.")
    print("    The root is not decoration; the plane page checked the inequality with the root in place.)")
    strings = ["".join(bits) for bits in product("01", repeat=3)]
    res = check_metric(strings, hamming)
    print(f"   Hamming distance on the {len(strings)} strings of three bits ({len(strings) ** 3} triples):")
    print(("   " + "  ".join(f"{n}: {str(r):<5}" for n, r in zip(names, res))).rstrip())
    print("   d(011, 110) = 2: the number of positions that differ. No coordinates, no Pythagoras,")
    print("   and still a distance, because the four properties are the definition.")


if __name__ == "__main__":
    main()
