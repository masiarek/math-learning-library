#!/usr/bin/env python3
"""The fat Cantor set: no interval inside it, like the Cantor set -- and length 1/2.

Run:  python3 fat_cantor_set.py

Also called the Smith-Volterra-Cantor set. Both sets come from one recipe with
one dial: at step n, delete an open gap of length a^n from the middle of every
piece that is left. a = 1/3 deletes middle thirds and gives the Cantor set.
a = 1/4 gives the fat one, whose gaps shrink so fast they add up to only 1/2.

Exact arithmetic throughout (fractions.Fraction).
"""

import math
from fractions import Fraction as F

CANTOR, FAT = F(1, 3), F(1, 4)


def steps(a: F):
    """Yield the closed pieces left after step 0, 1, 2, ... of the recipe with dial a."""
    pieces = [(F(0), F(1))]
    n = 0
    while True:
        yield pieces
        n += 1
        gap = a**n
        nxt = []
        for lo, hi in pieces:
            assert gap < hi - lo, "the gap must fit inside the piece"
            mid = (lo + hi) / 2
            nxt += [(lo, mid - gap / 2), (mid + gap / 2, hi)]
        pieces = nxt


def pieces_at(a: F, n: int) -> list[tuple[F, F]]:
    for k, pieces in enumerate(steps(a)):
        if k == n:
            return pieces
    raise AssertionError("unreachable: steps() never ends")


def picture(pieces: list[tuple[F, F]], width: int = 81) -> str:
    """One character per cell: # when more than half of the cell survives."""
    cells = []
    for i in range(width):
        lo, hi = F(i, width), F(i + 1, width)
        kept = sum((max(F(0), min(hi, b) - max(lo, a)) for a, b in pieces), F(0))
        cells.append("#" if 2 * kept > hi - lo else " ")
    return "".join(cells)


def length_left(a: F, n: int) -> F:
    """Length surviving n steps: step k deletes 2^(k-1) gaps of length a^k."""
    return 1 - sum((2 ** (k - 1) * a**k for k in range(1, n + 1)), F(0))


def upper_sum(a: F, cells: int) -> F:
    """Total length of the cells, out of `cells` equal closed ones, that touch the set.

    Uses the pieces from the first step at which every piece is shorter than a
    cell. From then on, a cell that touches a piece must contain one of its
    endpoints -- and endpoints are never deleted -- so the count is exact.
    """
    for pieces in steps(a):
        lo, hi = pieces[0]  # every piece at a step has the same length
        if hi - lo < F(1, cells):
            break
    touched = bytearray(cells)
    for lo, hi in pieces:
        for i in range(max(0, math.ceil(lo * cells) - 1), min(cells - 1, math.floor(hi * cells)) + 1):
            touched[i] = 1
    return F(sum(touched), cells)


def main() -> None:
    print("1. ONE RECIPE, ONE DIAL")
    print("   At step n, delete an open gap of length a^n from the middle of every")
    print("   piece that is left. (# marks a character more than half still there.)")
    for name, a in [("a = 1/3, the Cantor set", CANTOR), ("a = 1/4, the fat Cantor set", FAT)]:
        print(f"   {name}:")
        for n, pieces in zip(range(4), steps(a)):
            print(f"     {n} |{picture(pieces)}|")
    print("   With a = 1/3 the step-n gap is 1/3^n, exactly the middle third of every")
    print("   piece: lesson 3's set. With a = 1/4 every gap after the first is a")
    print("   smaller share of its piece, and the share keeps shrinking.")
    print()

    print("2. ADD UP THE GAPS")
    print(f"     {'step':>4}   {'Cantor deletes':<15} fat deletes")
    for k in range(1, 7):
        print(f"     {k:>4}   {str(2 ** (k - 1) * CANTOR**k):<15} {2 ** (k - 1) * FAT**k}")
    print("   Step by step, the Cantor column shrinks by 2/3 and the fat column halves.")
    for n in [10, 50]:
        c, f = 1 - length_left(CANTOR, n), 1 - length_left(FAT, n)
        assert c == 1 - F(2, 3) ** n and f == F(1, 2) - F(1, 2 ** (n + 1))
        print(f"     deleted in {n:>2} steps:  Cantor 1 - {float(1 - c):.3e}    fat 1/2 - {float(F(1, 2) - f):.3e}")
    print("     deleted in the limit: Cantor 1                fat 1/2")
    print()

    print("3. HOW MUCH IS LEFT, FOR ANY SETTING OF THE DIAL")
    print("   Summing the gaps gives a formula: length left = (1 - 3a) / (1 - 2a).")
    print(f"     {'a':<6} {'formula':<9} left after 100 steps")
    for a in [F(1, 3), F(1, 4), F(1, 5), F(1, 10), F(1, 100)]:
        formula = (1 - 3 * a) / (1 - 2 * a)
        left = length_left(a, 100)
        assert left - formula == a * (2 * a) ** 100 / (1 - 2 * a)
        print(f"     {str(a):<6} {str(formula):<9} {float(left):.12f}")
    a = F(2, 5)
    n = 0
    while a ** (n + 1) < length_left(a, n) / 2**n:
        n += 1
    print(f"   Past 1/3 the recipe breaks. With a = {a}, the gap for step {n + 1} is")
    print(f"   {a ** (n + 1)} long, but each piece left after step {n} is only {length_left(a, n) / 2**n}.")
    print("   So a = 1/3 is the one setting that deletes everything; every smaller")
    print("   setting leaves a set of positive length.")
    print()

    print("4. STILL NO INTERVAL INSIDE")
    print("   Every piece is cut again at the next step. After step n, each fat piece")
    print("   is 1/2^(n+1) + 1/2^(2n+1) long:")
    for n in [1, 2, 5, 10, 20, 40]:
        each = F(1, 2 ** (n + 1)) + F(1, 2 ** (2 * n + 1))
        if n <= 10:
            lo, hi = pieces_at(FAT, n)[0]
            assert hi - lo == each
        print(f"     after step {n:>2}:  {'2^' + str(n) + ' pieces,':<13} each {float(each):.3e} long")
    print("   Name any interval, however short. From some step on it is longer than")
    print("   every piece, so it cannot fit inside the set. The fat Cantor set, like")
    print("   the Cantor set, contains no interval: there is a gap in every stretch.")
    print()

    print("5. AND YET IT IS NOT MEASURE ZERO")
    print("   The pieces at step n cover it with total length 1/2 + 1/2^(n+1):")
    for n in [1, 5, 10, 20]:
        left = length_left(FAT, n)
        assert left == F(1, 2) + F(1, 2 ** (n + 1))
        print(f"     step {n:>2}:  total {float(left):.9f}")
    print("   That never drops below 1/2 -- and the page shows why no cover of any")
    print("   kind can. No interval inside it, and still length 1/2.")
    print()

    print("6. WHY ANYONE CARES: RIEMANN SUMS")
    print("   Let f(x) = 1 on the set and 0 off it, and cut [0,1] into N equal cells.")
    print("   The LOWER sum is 0 for both sets: every cell holds points of a gap.")
    print("   The UPPER sum is the total length of the cells that touch the set:")
    print(f"     {'N':>6}   {'Cantor':<8} fat Cantor")
    for N in [10, 100, 1000, 10000]:
        print(f"     {N:>6,}   {float(upper_sum(CANTOR, N)):.4f}   {float(upper_sum(FAT, N)):.4f}")
    print("   Cantor: the upper sum sinks toward 0, the lower sum is 0, and the two")
    print("   squeeze together. f has a Riemann integral, and it is 0.")
    print("   Fat Cantor: the upper sum never goes below 1/2. The sums never meet,")
    print("   and f has no Riemann integral at all.")


if __name__ == "__main__":
    main()
