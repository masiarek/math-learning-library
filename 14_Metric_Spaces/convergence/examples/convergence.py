#!/usr/bin/env python3
"""Convergence: a limit is a statement about every ball.

Run:  python3 convergence.py

A sequence converges to L when every ball around L, however small,
contains the whole tail of the sequence from some index on. The program
finds that index for 1/n and three radii; shows why (-1)^n has no limit
at all (a ball of radius 1 around any candidate misses half the terms);
proves a limit is unique with two disjoint balls; runs one sequence in
the plane under three metrics and gets three different N and the same
limit; and shows that under the discrete metric 1/n does not converge,
because convergence depends on the metric. All arithmetic is exact.
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
    print("1. x_n = 1/n CONVERGES TO 0: FOR EVERY RADIUS, A TAIL INSIDE THE BALL")
    for eps in [Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)]:
        N = int(1 / eps) + 1
        tail_ok = all(Fraction(1, n) < eps for n in range(N, 10 * N))
        last_bad = N - 1
        print(f"   eps = {str(eps):<7} N = {N:>5}: 1/n < eps for n = N..{10 * N - 1}: {tail_ok};  1/{last_bad} = {Fraction(1, last_bad)} is not < eps, so N cannot be smaller.")
    print("   The N works for ALL n >= N, not only the ones checked: 1/n < eps exactly when n > 1/eps,")
    print("   and every n >= floor(1/eps) + 1 is bigger than 1/eps. The loop checks the arithmetic.")
    print()

    print("2. x_n = (-1)^n HAS NO LIMIT: THE BALL OF RADIUS 1 AROUND ANY CANDIDATE MISSES HALF THE TERMS")
    for L in [Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(1), Fraction(3)]:
        far = max(abs(1 - L), abs(-1 - L))
        which = "+1" if abs(1 - L) >= abs(-1 - L) else "-1"
        print(f"   L = {str(L):<4} max(d(1, L), d(-1, L)) = {str(far):<4} >= 1: the terms equal to {which} all lie outside B(L, 1).")
    print("   For every L: d(1, -1) = 2 <= d(1, L) + d(L, -1), so one of the two distances is >= 1.")
    print("   One radius with no tail inside, for every candidate: that is the negation of convergence.")
    print()

    print("3. A LIMIT IS UNIQUE: TWO CANDIDATES, TWO DISJOINT BALLS")
    L, M = Fraction(0), Fraction(1, 5)
    r = abs(L - M) / 2
    print(f"   Suppose x_n -> L = {L} and x_n -> M = {M}. Let r = d(L, M)/2 = {r}.")
    cands = [Fraction(k, 100) for k in range(-50, 71)]
    both = [x for x in cands if abs(x - L) < r and abs(x - M) < r]
    print(f"   Points within r of both L and M, on a grid of step 1/100: {both}")
    print("   None, and none anywhere: a point in both balls would give d(L, M) <= d(L, x) + d(x, M) < 2r = d(L, M).")
    print("   A tail of the sequence cannot lie in two disjoint balls, so L = M.")
    print()

    print("4. ONE SEQUENCE IN THE PLANE, THREE METRICS, THREE N, ONE LIMIT")
    seq = lambda n: (Fraction(1, n), Fraction((-1) ** n, n))
    eps = Fraction(1, 10)
    print(f"   x_n = (1/n, (-1)^n / n), limit (0, 0), eps = {eps}.")
    metrics = [("Euclidean", lambda p, q: eucl2(p, q) < eps * eps),
               ("taxicab", lambda p, q: taxi(p, q) < eps),
               ("Chebyshev", lambda p, q: cheb(p, q) < eps)]
    for name, inside in metrics:
        N = next(n for n in range(1, 1000) if all(inside(seq(m), (0, 0)) for m in range(n, n + 200)))
        print(f"   {name:<10} first N with the tail inside the ball: N = {N:>3}   (checked 200 terms on)")
    print("   Three different N, because the balls have three sizes; one limit, because the balls nest:")
    print("   a tail inside the taxicab ball is inside the Euclidean and Chebyshev balls of the same radius,")
    print("   and a tail inside the Chebyshev ball of radius r/2 is inside the taxicab ball of radius r.")
    print("   Equivalent metrics have the same convergent sequences and the same limits.")
    print()

    print("5. UNDER THE DISCRETE METRIC, 1/n DOES NOT CONVERGE TO 0")
    disc = lambda p, q: 0 if p == q else 1
    terms = [Fraction(1, n) for n in range(1, 8)]
    print("   d(1/n, 0) for n = 1..7: " + ", ".join(str(disc(t, 0)) for t in terms))
    print("   Every term is at distance 1 from 0, so the ball B(0, 1/2) contains no term at all.")
    print("   Under this metric a sequence converges only if it is eventually constant. Same points,")
    print("   same sequence, a different metric, a different answer: convergence belongs to the metric.")
    print()

    print("6. IN THE PLANE, CONVERGENCE IS COORDINATE BY COORDINATE")
    print("   Under Chebyshev, cheb(x_n, L) < eps means |x-part| < eps AND |y-part| < eps: a point is")
    print("   in the square ball exactly when each coordinate is in its interval. So x_n -> L in the plane")
    print("   exactly when both coordinate sequences converge, and by section 4 that holds for all three metrics.")
    xs = [seq(n)[0] for n in range(1, 6)]
    ys = [seq(n)[1] for n in range(1, 6)]
    print(f"   x-parts: {', '.join(map(str, xs))}, ...  -> 0")
    print(f"   y-parts: {', '.join(map(str, ys))}, ...  -> 0")


if __name__ == "__main__":
    main()
