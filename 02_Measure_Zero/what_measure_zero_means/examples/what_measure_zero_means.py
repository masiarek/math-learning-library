#!/usr/bin/env python3
"""What "measure zero" means: a set that fits inside intervals of almost no total length.

Run:  python3 what_measure_zero_means.py

Measure zero is defined BEFORE length is. You never have to say what the
"length" of a strange set is. You only have to show that it fits inside
ordinary intervals whose lengths add up to as little as anyone asks.

All arithmetic is exact (fractions.Fraction), so every total printed here is
the true total, not a floating-point approximation of it.
"""

from fractions import Fraction as F


def cover(center: F, length: F) -> str:
    """An open interval of the given length, centred on a point, as text."""
    return f"({center - length / 2}, {center + length / 2})"


def main() -> None:
    print("1. ONE POINT")
    print("   Cover the point 1/2 with an interval as long as the budget allows:")
    point = F(1, 2)
    for budget in [F(1, 10), F(1, 1000), F(1, 10**6)]:
        print(f"     budget {str(budget):<9}   interval {cover(point, budget):<34}  length {budget}")
    print("   The point's length is at most 1/10, at most 1/1000, at most any")
    print("   positive number you care to name. Only one length qualifies: 0.")
    print()

    print("2. FINITELY MANY POINTS")
    points = [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]
    budget = F(1, 100)
    share = budget / len(points)
    print(f"   Five points, a budget of {budget}. Split it evenly: each point gets {share}.")
    for p in points:
        print(f"     {str(p):<4}  inside {cover(p, share)}")
    total = sum((share for _ in points), F(0))
    assert total <= budget
    print(f"   total length: 5 x {share} = {total}, within the budget.")
    print("   Any finite list of points works the same way: split the budget evenly.")
    print()

    print("3. THE DEFINITION")
    print("   A set has MEASURE ZERO if, for every budget eps > 0, it fits inside")
    print("   a list of intervals -- finitely many, or an infinite list -- whose")
    print("   lengths add up to at most eps.")
    print()
    print("   Only the lengths of INTERVALS are ever added. Nobody has to say what")
    print("   the 'length' of the set itself is, and that is the whole trick: the")
    print("   definition works on sets far too ragged to measure directly.")
    print()

    print("4. ONE SET OF POINTS, TWO ROOMS")
    print("   The points of [0,1], cut into n equal pieces, each piece covered.")
    print("   On a line a piece needs an interval. In the plane it needs a square.")
    print()
    print(f"     {'n':>9}   {'each interval':<14}  {'total length':<13}  {'each square':<16}  total area")
    for n in [1, 10, 100, 1000, 10**6]:
        side = F(1, n)
        print(
            f"     {n:>9,}   {str(side):<14}  {str(n * side):<13}  "
            f"{str(side * side):<16}  {n * side * side}"
        )
    print()
    print("   On the line these covers total 1 for every n. In the plane the total")
    print("   shrinks like 1/n, because a square's SECOND side shrinks too:")
    print("   n x (1/n)^2 = 1/n.")
    print()
    print("   So [0,1] has area 0 and length 1. 'Measure zero' always means measure")
    print("   zero IN some space: thin compared with the room around it.")
    print()

    print("5. THE QUESTION THIS LEAVES")
    print("   Section 4 had help: a segment is thin in the plane because it has one")
    print("   dimension fewer than the plane. Can a set with infinitely many points")
    print("   have length zero INSIDE the line itself?")
    print("     countably many points     the rationals     (next lesson)")
    print("     uncountably many points   the Cantor set    (the one after)")


if __name__ == "__main__":
    main()
