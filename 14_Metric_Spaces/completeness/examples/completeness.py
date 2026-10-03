#!/usr/bin/env python3
"""Cauchy sequences and completeness: the rationals have holes, the reals do not.

Run:  python3 completeness.py

A sequence is Cauchy when its terms eventually stay within any given
distance of EACH OTHER; a space is complete when every Cauchy sequence
converges to a point of the space. The program shows 1/n is Cauchy with
an explicit N for each eps; runs Newton's iteration for sqrt 2 in exact
fractions, shows it is Cauchy in Q and that no rational is its limit;
shows that in R it converges, to twelve decimals of sqrt 2 computed
exactly with isqrt; shows that completeness is not a matter of open
sets, since (0, 1) and R have the same open sets and only one is
complete; and ends with the two easy complete spaces, the discrete
metric and the integers. All arithmetic is exact.
"""

from fractions import Fraction
from math import isqrt


def main() -> None:
    print("1. x_n = 1/n IS CAUCHY: THE TERMS GET CLOSE TO EACH OTHER")
    for eps in [Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)]:
        N = int(1 / eps) + 1
        ok = all(abs(Fraction(1, m) - Fraction(1, n)) < eps for m in range(N, N + 60) for n in range(N, N + 60))
        print(f"   eps = {str(eps):<7} N = {N:>5}: |1/m - 1/n| < eps for m, n in N..N+59: {ok}")
    print("   For all m, n >= N: both 1/m and 1/n lie in (0, 1/N], so |1/m - 1/n| < 1/N <= eps.")
    print("   A Cauchy sequence need not mention a limit: the condition is about pairs of terms.")
    print()

    print("2. NEWTON'S ITERATION FOR sqrt 2, IN EXACT FRACTIONS: CAUCHY IN Q, NO LIMIT IN Q")
    x = Fraction(1)
    xs = [x]
    for _ in range(5):
        x = (x + 2 / x) / 2
        xs.append(x)
    print("   x_0 = 1, x_{n+1} = (x_n + 2/x_n)/2")
    for n, x in enumerate(xs):
        e = x * x - 2
        gap = abs(xs[n] - xs[n - 1]) if n else None
        print(f"   x_{n} = {str(x):<28} x_n^2 - 2 = {str(e):<32} |x_n - x_(n-1)| = {gap if gap is not None else '-'}")
    print("   Writing e_n = x_n^2 - 2 (positive from n = 1 on): e_(n+1) = e_n^2 / (4 x_n^2) <= e_n^2 / 8,")
    print("   so e_n -> 0 faster than any geometric sequence, and |x_m - x_n| <= (e_m + e_n)/2 since")
    print("   |x_m - x_n| = |x_m^2 - x_n^2| / (x_m + x_n) and x_m + x_n > 2. So the sequence is Cauchy,")
    print("   with every step of that argument inside Q.")
    bad = [Fraction(p, q) for q in range(1, 301) for p in range(1, 2 * q) if Fraction(p, q) ** 2 == 2]
    print(f"   Rationals p/q with q <= 300 whose square is 2: {bad}")
    print("   None, and none at all: if p^2 = 2 q^2 in lowest terms then p is even, p = 2k, 4k^2 = 2q^2,")
    print("   2k^2 = q^2, q is even too, and p/q was not in lowest terms. (Proof by contradiction.)")
    print("   A Cauchy sequence in Q with no limit in Q: the rationals are NOT complete.")
    print()

    print("3. THE SAME SEQUENCE IN R: IT CONVERGES, AND R IS COMPLETE BY CONSTRUCTION")
    root = isqrt(2 * 10 ** 24)
    s = str(root)
    print(f"   sqrt 2 to 12 decimals, from isqrt(2 * 10^24) = {root}: {s[0]}.{s[1:]}")
    x4 = xs[4]
    num = x4.numerator * 10 ** 12 // x4.denominator
    t = str(num)
    print(f"   x_4 = {x4} = {t[0]}.{t[1:]}... to 12 decimals")
    agree = 0
    for a, b in zip(s, t):
        if a != b:
            break
        agree += 1
    print(f"   The two agree in the first {agree} digits. The real number sqrt 2 is what the sequence")
    print("   was heading for all along; R is Q with a limit supplied for every Cauchy sequence.")
    print("   That is one construction of R, and 'complete' is the property it is built to have.")
    print()

    print("4. COMPLETENESS IS NOT A MATTER OF OPEN SETS: (0, 1) AND R")
    print("   f(x) = (2x - 1) / (x (1 - x)) maps (0, 1) onto R, continuously and with a continuous inverse,")
    print("   so the two spaces have the same open sets and the same convergent sequences. (Not proved here.)")
    print("   The sequence 1/n is Cauchy in (0, 1) and has no limit there: its only candidate, 0, is missing.")
    f = lambda x: (2 * x - 1) / (x * (1 - x))
    vals = [f(Fraction(1, n)) for n in range(2, 11)]
    print("   Its image f(1/n) for n = 2..10: " + ", ".join(str(v) for v in vals))
    gaps = [abs(vals[i + 1] - vals[i]) for i in range(len(vals) - 1)]
    print("   Gaps between consecutive images: " + ", ".join(str(g) for g in gaps))
    print("   The gaps approach 1 and never 0: the image is not Cauchy in R, and f(1/n) -> -infinity.")
    print("   Being Cauchy depends on the metric, not only on the open sets; so does being complete.")
    print()

    print("5. TWO SPACES THAT ARE COMPLETE FOR A CHEAP REASON")
    disc = lambda p, q: 0 if p == q else 1
    seq = ["a", "b", "c", "c", "c", "c", "c"]
    print(f"   Discrete metric, the sequence {seq}:")
    print(f"   from index 2 on every two terms are at distance {disc('c', 'c')}, which is < 1/2. Being Cauchy with")
    print("   eps = 1/2 forces 'eventually constant', and a constant tail converges to its constant.")
    print("   The integers with |m - n|: the same argument, since two different integers are 1 apart.")
    print("   And [0, 1] is complete while (0, 1) is not: the one missing point is the whole difference.")


if __name__ == "__main__":
    main()
