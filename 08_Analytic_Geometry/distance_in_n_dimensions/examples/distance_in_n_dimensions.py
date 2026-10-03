#!/usr/bin/env python3
"""Distance in n dimensions, and the length of a vector.

Run:  python3 distance_in_n_dimensions.py

The distance formula in the plane is Pythagoras once. In space it is
Pythagoras twice: the floor diagonal of a box, then the box diagonal.
With n axes it is Pythagoras n - 1 times, and the squares just keep
adding up. The length of a vector is the same formula measured from
the origin, which is why sqrt(v . v) is a length and not a definition
pulled from the air. The program builds the 3D formula from two right
triangles, checks that every extra axis adds one square, measures
vectors, and tests the four properties a distance must have, exactly.
"""

from fractions import Fraction
from itertools import product
from math import isqrt


def sq_dist(p, q):
    """The squared distance: exact for rational coordinates."""
    return sum((b - a) ** 2 for a, b in zip(p, q))


def root(s):
    """sqrt(s) when s is a perfect square (as a Fraction), else a decimal string."""
    n, d = s.numerator, s.denominator
    if isqrt(n) ** 2 == n and isqrt(d) ** 2 == d:
        return str(Fraction(isqrt(n), isqrt(d)))
    return f"sqrt({s}) = {float(s) ** 0.5:.4f}"


def fmt(p):
    return "(" + ", ".join(str(c) for c in p) + ")"


def main() -> None:
    print("1. A BOX 3 BY 4 BY 12: PYTHAGORAS TWICE")
    a, b, c = 3, 4, 12
    floor = a * a + b * b
    print(f"   Floor diagonal: a right triangle with legs {a} and {b}, so f^2 = {a}^2 + {b}^2 = {floor}, f = {isqrt(floor)}.")
    print(f"   Box diagonal: a right triangle with legs f = {isqrt(floor)} and the height {c},")
    print(f"   so d^2 = f^2 + {c}^2 = {floor} + {c * c} = {floor + c * c}, d = {isqrt(floor + c * c)}.")
    print(f"   Substituting f^2: d^2 = {a}^2 + {b}^2 + {c}^2. Each axis adds one square.")
    print("   The second right angle is between the floor diagonal and the vertical edge,")
    print("   which is perpendicular to everything in the floor: that is what the z-axis being")
    print("   perpendicular to the x- and y-axes buys.")
    print()

    print("2. TWO POINTS IN SPACE, THE SAME FORMULA WITH THREE DIFFERENCES")
    p, q = (1, 3, 2), (5, 6, 14)
    diffs = [b - a for a, b in zip(p, q)]
    print(f"   P1 = {fmt(p)}, P2 = {fmt(q)}: differences {diffs}, squares {[d * d for d in diffs]},")
    print(f"   d^2 = {sq_dist(p, q)}, d = {root(Fraction(sq_dist(p, q)))}.")
    print(f"   Swapped: d(P2, P1)^2 = {sq_dist(q, p)}. Order does not matter, for the same reason as in the plane.")
    print()

    print("3. ONE SQUARE PER AXIS: THE SAME TWO POINTS SEEN IN 1, 2, 3, 4, 5 DIMENSIONS")
    p5, q5 = (1, 3, 2, 0, 7), (5, 6, 14, 2, 4)
    for n in range(1, 6):
        d2 = sq_dist(p5[:n], q5[:n])
        terms = " + ".join(f"{(b - a) ** 2}" for a, b in zip(p5[:n], q5[:n]))
        print(f"   n = {n}: d^2 = {terms:<22} = {d2:>4}, d = {root(Fraction(d2))}")
    print("   Dropping to n - 1 dimensions drops one square; adding an axis adds one. That is the")
    print("   induction: the n-dimensional formula is the (n - 1)-dimensional one plus Pythagoras once more.")
    print()

    print("4. THE LENGTH OF A VECTOR IS THE DISTANCE FROM THE ORIGIN")
    for v in [(3, 4), (1, 1), (3, 4, 12), (1, 1, 1, 1), (Fraction(1, 2), Fraction(1, 2))]:
        o = (0,) * len(v)
        dot = sum(x * x for x in v)
        print(f"   v = {fmt(v):<16} v . v = {str(dot):<6} |v| = sqrt(v . v) = {root(Fraction(dot)):<18} d(0, v)^2 = {sq_dist(o, v)}")
    print("   v . v is the sum of the squares of the coordinates, which is d(0, v)^2 by the formula.")
    print("   So sqrt(v . v) is a length because the distance formula says so, not by decree.")
    u, w = (1, 3, 2), (5, 6, 14)
    diff = tuple(b - a for a, b in zip(u, w))
    print(f"   And the distance between two points is the length of their difference: w - u = {fmt(diff)},")
    print(f"   |w - u|^2 = {sum(x * x for x in diff)} = d(u, w)^2 = {sq_dist(u, w)}.")
    print()

    print("5. THE FOUR PROPERTIES OF A DISTANCE, CHECKED ON A GRID IN 3 DIMENSIONS")
    grid = list(product(range(-2, 3), repeat=3))
    print(f"   Points: every (x, y, z) with coordinates in -2..2, {len(grid)} of them.")
    nonneg = all(sq_dist(p, q) >= 0 for p in grid for q in grid)
    zero = all((sq_dist(p, q) == 0) == (p == q) for p in grid for q in grid)
    sym = all(sq_dist(p, q) == sq_dist(q, p) for p in grid for q in grid)
    print(f"   d(P, Q) >= 0 for all pairs:                   {nonneg}")
    print(f"   d(P, Q) = 0 exactly when P = Q:               {zero}")
    print(f"   d(P, Q) = d(Q, P):                            {sym}")
    # Triangle inequality on squared distances: d(P,R) <= d(P,Q) + d(Q,R)
    # <=> d(P,R)^2 <= d(P,Q)^2 + d(Q,R)^2 + 2 d(P,Q) d(Q,R), and the cross term
    # is compared by squaring once more, all in exact integers.
    def triangle(p, q, r):
        a2, b2, c2 = sq_dist(p, q), sq_dist(q, r), sq_dist(p, r)
        lhs = c2 - a2 - b2
        return lhs <= 0 or lhs * lhs <= 4 * a2 * b2
    small = [p for p in grid if all(-1 <= c <= 1 for c in p)]
    tri = all(triangle(p, q, r) for p in small for q in grid for r in small)
    print(f"   d(P, R) <= d(P, Q) + d(Q, R) on {len(small)}x{len(grid)}x{len(small)} triples: {tri}")
    print("   The first three follow from the formula in a line each: squares are never negative,")
    print("   a sum of squares is 0 only when every square is, and squaring forgets the sign.")
    print("   The fourth is the one with a real proof behind it (the Cauchy-Schwarz inequality),")
    print("   which this page checks and does not prove.")


if __name__ == "__main__":
    main()
