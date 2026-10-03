#!/usr/bin/env python3
"""Open balls: three metrics, the same open sets.

Run:  python3 open_balls.py

An open ball B(p, r) is the set of points closer than r to p, and an open
set is one in which every point has a ball around it that fits inside.
The program draws the three balls of the plane's three everyday metrics,
checks the two-sided inequalities between the metrics exactly on a grid,
shows the balls nested one inside the next, verifies on one open set
that each of its points keeps a ball of every kind inside the set, and
ends with the discrete metric, whose balls are a single point or
everything. Everything is exact: squared Euclidean distances and
integer taxicab and Chebyshev distances.
"""

from fractions import Fraction
from itertools import product


def eucl2(p, q):
    return sum((b - a) ** 2 for a, b in zip(p, q))


def taxi(p, q):
    return sum(abs(b - a) for a, b in zip(p, q))


def cheb(p, q):
    return max(abs(b - a) for a, b in zip(p, q))


def main() -> None:
    print("1. THE OPEN BALL OF RADIUS 2 AROUND THE ORIGIN, UNDER THREE METRICS")
    print("   Lattice points with -3 <= x, y <= 3; # marks a point at distance LESS THAN 2.")
    balls = [("Euclidean", lambda q: eucl2((0, 0), q) < 4),
             ("taxicab", lambda q: taxi((0, 0), q) < 2),
             ("Chebyshev", lambda q: cheb((0, 0), q) < 2)]
    print(("   " + "".join(f"{n:<12}" for n, _ in balls)).rstrip())
    for y in range(3, -4, -1):
        row = "".join("".join("#" if inside((x, y)) else "." for x in range(-3, 4)) + "     " for _, inside in balls)
        print(("   " + row).rstrip())
    print("   Strict inequality: the boundary is not in the ball. (2, 0) is at Euclidean distance")
    print("   exactly 2 from the origin and is left out of all three.")
    print()

    print("2. THE THREE METRICS ARE WITHIN A FACTOR OF 2 OF EACH OTHER, ON EVERY PAIR")
    grid = list(product(range(-3, 4), repeat=2))
    ok = all(cheb(p, q) ** 2 <= eucl2(p, q) <= taxi(p, q) ** 2 <= 4 * cheb(p, q) ** 2 for p in grid for q in grid)
    print(f"   cheb <= eucl <= taxi <= 2 cheb, compared as squares on {len(grid) ** 2} pairs: {ok}")
    print("   The proof is three lines, with a = |dx| and b = |dy|:")
    print("     max(a, b)^2 <= a^2 + b^2            one square is at most the sum of both;")
    print("     a^2 + b^2 <= (a + b)^2               the cross term 2ab is not negative;")
    print("     a + b <= 2 max(a, b)                 each of a, b is at most the max.")
    print("   The grid is a check that the lines were copied right; the lines hold for every a, b.")
    print()

    print("3. THE BALLS NEST: B_taxi(p, r) inside B_eucl(p, r) inside B_cheb(p, r) inside B_taxi(p, 2r)")
    r = Fraction(5, 2)
    big = list(product(range(-5, 6), repeat=2))
    bt = {q for q in big if taxi((0, 0), q) < r}
    be = {q for q in big if eucl2((0, 0), q) < r * r}
    bc = {q for q in big if cheb((0, 0), q) < r}
    bt2 = {q for q in big if taxi((0, 0), q) < 2 * r}
    print(f"   r = {r}, lattice points in each: taxi {len(bt)}, eucl {len(be)}, cheb {len(bc)}, taxi with 2r {len(bt2)}")
    print(f"   taxi <= eucl <= cheb <= taxi(2r) as sets: {bt <= be <= bc <= bt2}")
    print("   Each inclusion is one line of section 2 read as a statement about balls:")
    print("   taxi(p, q) < r forces eucl(p, q) < r, because eucl <= taxi; and so on round.")
    print()

    print("4. ONE OPEN SET, ONE OF ITS POINTS, AND A BALL OF EACH KIND THAT FITS")
    print("   U = the Euclidean open disc x^2 + y^2 < 9. Take p = (2, 1), which is in U: 4 + 1 = 5 < 9.")
    p = (Fraction(2), Fraction(1))
    rad = Fraction(7, 10)
    print(f"   The Euclidean distance from p to the edge is 3 - sqrt(5), about 0.764; choose r = {rad}.")
    step = Fraction(1, 20)
    offsets = [Fraction(k, 20) for k in range(-16, 17)]
    pts = [(p[0] + dx, p[1] + dy) for dx in offsets for dy in offsets]
    for name, d, bound in [("taxi", taxi, rad), ("Chebyshev", cheb, rad / 2), ("Euclidean", None, rad)]:
        if d is None:
            ball = [q for q in pts if eucl2(p, q) < bound * bound]
        else:
            ball = [q for q in pts if d(p, q) < bound]
        inside = all(q[0] ** 2 + q[1] ** 2 < 9 for q in ball)
        print(f"   B_{name}(p, {bound}): {len(ball):>4} grid points of step {step}, all inside U: {inside}")
    print("   One point of one set, checked on a grid: evidence. The theorem is section 3:")
    print("   a ball of one kind inside U contains a ball of each other kind, so 'open' means the")
    print("   same thing under all three metrics. They are EQUIVALENT metrics.")
    print()

    print("5. THE DISCRETE METRIC: d(p, q) = 1 FOR p != q, AND 0 FOR p = q")
    pts5 = ["a", "b", "c", "d", "e"]
    disc = lambda p, q: 0 if p == q else 1
    for rr in [Fraction(1, 2), Fraction(1), Fraction(2)]:
        ball = [q for q in pts5 if disc("a", q) < rr]
        print(f"   B(a, {rr}) = {ball}")
    print("   A ball is one point or everything, so every subset is open: every point of any set")
    print("   has the ball of radius 1/2 around it inside the set. This metric is a metric (the")
    print("   four properties hold; the triangle inequality is 1 <= 1 + 1 at worst) and it is NOT")
    print("   equivalent to the Euclidean one: no Euclidean ball of positive radius is a single point,")
    print("   since B_eucl(p, r) contains p + (r/2, 0).")


if __name__ == "__main__":
    main()
