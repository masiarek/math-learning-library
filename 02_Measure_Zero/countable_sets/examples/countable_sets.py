#!/usr/bin/env python3
"""Countable sets have measure zero -- even the rationals, which are everywhere.

Run:  python3 countable_sets.py

The rationals in [0,1] are dense: every interval, however narrow, contains
some. Yet they fit inside intervals whose lengths add up to 1/10, or to any
other positive number. The trick is to list them, and give the n-th one an
interval of length (1/10) / 2^n.

Exact arithmetic throughout -- Fraction for the intervals, and squaring
instead of square roots for sqrt(2) -- so "not covered" below is a fact about
the numbers, not the outcome of some rounding.
"""

import math
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import islice

BUDGET = F(1, 10)


def rationals():
    """Every rational in [0,1] exactly once: by denominator, lowest terms only."""
    yield F(0)
    yield F(1)
    q = 2
    while True:
        for p in range(1, q):
            if math.gcd(p, q) == 1:
                yield F(p, q)
        q += 1


def length(n: int) -> F:
    """Length of the interval given to the n-th rational (n counts from 1)."""
    return BUDGET / 2**n


def index_of(target: F) -> int:
    for n, r in enumerate(rationals(), start=1):
        if r == target:
            return n
    raise AssertionError("unreachable: every rational in [0,1] is listed")


def simplest_between(lo: F, hi: F) -> F:
    """The rational with the smallest denominator strictly between lo and hi."""
    q = 1
    while True:
        p = math.floor(lo * q) + 1
        if F(p, q) < hi:
            return F(p, q)
        q += 1


def below_sqrt2(r: F) -> bool:
    return r < 0 or r * r < 2


def above_sqrt2(r: F) -> bool:
    return r > 0 and r * r > 2


def holds_sqrt2_minus_1(center: F, half: F) -> bool:
    """Is sqrt(2) - 1 inside the open interval (center - half, center + half)?"""
    return below_sqrt2(center - half + 1) and above_sqrt2(center + half + 1)


def main() -> None:
    print("1. EVERY RATIONAL IN [0,1] GETS A PLACE IN LINE")
    print("   Order them by denominator, and skip anything not in lowest terms:")
    first = list(islice(rationals(), 20))
    for row in range(0, 20, 5):
        cells = [f"{n:>2}: {str(r):<5}" for n, r in enumerate(first[row:row + 5], start=row + 1)]
        print(("     " + "   ".join(cells)).rstrip())
    for target in [F(5, 12), F(99, 100)]:
        print(f"   {target} is number {index_of(target):,}.")
    print("   Every rational in [0,1] has a finite place in this list. A set that")
    print("   can be listed like this is COUNTABLE.")
    print()

    print("2. AND THEY ARE EVERYWHERE")
    print("   Between any two different numbers sits a rational. The simplest one")
    print("   in some ever-narrower windows:")
    for lo, hi in [("0.41", "0.42"), ("0.414", "0.415"), ("0.4142", "0.4143"),
                   ("0.41421", "0.41422"), ("0.414213", "0.414214")]:
        r = simplest_between(F(lo), F(hi))
        print(f"     between {lo:<8} and {hi:<8}   {str(r):<9} = {float(r):.9f}")
    print("   No window is too narrow to hold one. That is what DENSE means.")
    print()

    print("3. GIVE THE n-TH RATIONAL AN INTERVAL OF LENGTH (1/10) / 2^n")
    print(f"     {'n':>2}   {'rational':<9} {'length':<8} interval around it")
    for n, r in enumerate(first[:8], start=1):
        half = length(n) / 2
        print(f"     {n:>2}   {str(r):<9} {str(length(n)):<8} ({r - half}, {r + half})")
    print("   Every rational sits inside its own interval, so every one is covered.")
    print()

    print("4. ADD UP THE LENGTHS")
    print("   1/20 + 1/40 + 1/80 + ... halves each time. After N intervals the")
    print("   total is exactly 1/10 - 1/(10 x 2^N):")
    print(f"     {'N':>5}   below 1/10 by")
    running, done = F(0), 0
    for N in [10, 100, 1000]:
        while done < N:
            done += 1
            running += length(done)
        assert running == BUDGET - BUDGET / 2**N
        print(f"     {N:>5}   {float(BUDGET - running):.3e}")
    print("   The total creeps toward 1/10 and never passes it, so the whole")
    print("   infinite cover has total length at most 1/10. Every rational is")
    print("   covered, and 9/10 of [0,1] is not. Swap 1/10 for any budget at all")
    print("   and the same list works, so the rationals have measure zero.")
    print()

    print("5. SO WHAT IS NOT COVERED?")
    N = 5000
    print("   At least 9/10 of [0,1] -- all of it irrational. One such number is")
    print(f"   sqrt(2) - 1 = 0.41421356... Checked exactly against the first {N:,}:")
    listed = list(islice(rationals(), N))
    hits = [n for n, r in enumerate(listed, start=1) if holds_sqrt2_minus_1(r, length(n) / 2)]
    with localcontext() as ctx:
        ctx.prec = 60
        x = Decimal(2).sqrt() - 1
        best = None
        for n, r in enumerate(listed, start=1):
            gap = abs(x - Decimal(r.numerator) / r.denominator)
            half = Decimal(1) / (20 * 2**n)
            if best is None or gap / half < best[0]:
                best = (gap / half, n, r, gap, half)
        ratio, n, r, gap, half = best
        for label, shown in [
            ("intervals containing it", f"{len(hits)}"),
            ("closest call", f"interval {n}, around {r}"),
            (f"  distance from {r}", f"{gap:.8f}"),
            ("  half that interval", f"{half:.8f}"),
            ("  misses by a factor of", f"{ratio:.1f}"),
        ]:
            print(f"     {label + ':':<27} {shown}")
    print("   That check stops at 5,000. The page proves the miss for all of them.")
    print()

    print("6. WHY 'AN INFINITE LIST', NOT JUST 'FINITELY MANY'")
    cut = 1000
    print(f"   Stop after the first {cut:,} intervals, and look at the next rationals:")
    kept = listed[:cut]
    for k, r in enumerate(islice(rationals(), cut, cut + 4), start=cut + 1):
        inside = next(
            (n for n, c in enumerate(kept, start=1) if abs(r - c) < length(n) / 2), None
        )
        where = f"covered anyway, by interval {inside} around {kept[inside - 1]}" if inside else "NOT covered"
        print(f"     number {k:,}: {str(r):<5}  {where}")
    print("   Every finite stopping point leaves rationals out. Only the whole")
    print("   infinite list covers them all -- and the page shows why no finite")
    print("   cover of the rationals in [0,1] can total less than 1.")


if __name__ == "__main__":
    main()
