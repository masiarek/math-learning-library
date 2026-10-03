#!/usr/bin/env python3
"""Continuity by epsilon and delta: a ball around the output, a ball around the input.

Run:  python3 continuity.py

f is continuous at p when for every ball of radius eps around f(p)
there is a ball of radius delta around p that f sends inside it. The
program finds a delta for x^2 at 3 and four values of eps and checks it
on a grid; shows the step function has one eps for which every delta
fails, with a witness point for each; proves that the distance to a
fixed point is itself continuous, with delta = eps, from the triangle
inequality; shows the identity map between two equivalent metrics is
continuous both ways; and shows that out of a discrete space every
function is continuous. All arithmetic is exact.
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
    print("1. f(x) = x^2 IS CONTINUOUS AT 3: FOR EVERY eps, A delta")
    p = Fraction(3)
    for eps in [Fraction(1), Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)]:
        delta = min(Fraction(1), eps / 7)
        xs = [p + delta * Fraction(k, 1000) for k in range(-999, 1000)]
        ok = all(abs(x * x - 9) < eps for x in xs)
        print(f"   eps = {str(eps):<6} delta = min(1, eps/7) = {str(delta):<7} |x^2 - 9| < eps on 1999 points within delta of 3: {ok}")
    print("   Why delta = min(1, eps/7) works for EVERY x, not only the grid:")
    print("     |x^2 - 9| = |x - 3| |x + 3|, and |x - 3| < 1 gives 2 < x < 4, so |x + 3| < 7,")
    print("     so |x^2 - 9| < 7 |x - 3| < 7 (eps/7) = eps.")
    print()

    print("2. THE STEP FUNCTION IS NOT CONTINUOUS AT 0: ONE eps DEFEATS EVERY delta")
    step = lambda x: 0 if x < 0 else 1
    eps = Fraction(1, 2)
    print(f"   s(x) = 0 for x < 0 and 1 for x >= 0; s(0) = 1. Take eps = {eps}.")
    for delta in [Fraction(1), Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)]:
        x = -delta / 2
        print(f"   delta = {str(delta):<7} witness x = {str(x):<8} |x - 0| = {str(abs(x)):<7} < delta, and |s(x) - s(0)| = {abs(step(x) - step(0))} >= eps")
    print("   The witness x = -delta/2 works for every delta > 0, so no delta works for eps = 1/2.")
    print("   'Not continuous' is: there EXISTS an eps such that for ALL delta some x breaks it;")
    print("   the negation of a for-all-exists is an exists-for-all, and the witness is the proof.")
    print()

    print("3. THE DISTANCE TO A FIXED POINT IS CONTINUOUS, WITH delta = eps")
    print("   Claim: |d(x, p) - d(y, p)| <= d(x, y). Proof: d(x, p) <= d(x, y) + d(y, p) is the triangle")
    print("   inequality, so d(x, p) - d(y, p) <= d(x, y); swap x and y for the other sign.")
    grid = list(product(range(-3, 4), repeat=2))
    p2 = (1, 2)
    ok = all(abs(taxi(x, p2) - taxi(y, p2)) <= taxi(x, y) for x in grid for y in grid)
    print(f"   Checked with the taxicab metric on {len(grid) ** 2} pairs around p = {p2}: {ok}")
    print("   So if d(x, y) < eps then |d(x, p) - d(y, p)| < eps: delta = eps, in every metric space.")
    print()

    print("4. THE IDENTITY MAP BETWEEN TWO EQUIVALENT METRICS IS CONTINUOUS BOTH WAYS")
    print("   From (plane, taxicab) to (plane, Euclidean): eucl <= taxi, so delta = eps.")
    print("   From (plane, Euclidean) to (plane, taxicab): taxi <= 2 cheb <= 2 eucl, so delta = eps/2.")
    ok1 = all(eucl2(x, y) <= taxi(x, y) ** 2 for x in grid for y in grid)
    ok2 = all(taxi(x, y) ** 2 <= 4 * eucl2(x, y) for x in grid for y in grid)
    print(f"   eucl^2 <= taxi^2 on all pairs: {ok1};  taxi^2 <= 4 eucl^2 on all pairs: {ok2}")
    print("   A map that is continuous both ways, with a continuous inverse, is a homeomorphism:")
    print("   the two metric spaces have the same open sets and the same convergent sequences.")
    print()

    print("5. OUT OF A DISCRETE SPACE, EVERY FUNCTION IS CONTINUOUS")
    points = ["a", "b", "c", "d", "e"]
    f = {"a": 0, "b": 100, "c": -7, "d": 100, "e": 3}
    disc = lambda x, y: 0 if x == y else 1
    delta = Fraction(1, 2)
    for p in points:
        near = [x for x in points if disc(x, p) < delta]
        print(f"   p = {p}: points within delta = 1/2 of p: {near}; |f(x) - f(p)| there is 0, below every eps.")
    print("   The condition 'd(x, p) < delta implies d(f(x), f(p)) < eps' has only x = p to satisfy,")
    print("   and it does. Continuity is a property of the map AND the two metrics, never of the map alone.")


if __name__ == "__main__":
    main()
