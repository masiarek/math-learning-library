#!/usr/bin/env python3
"""Multiplication can be undone: why the complex rule, and not entry by entry.

Run:  python3 multiplication_can_be_undone.py

The obvious way to multiply pairs is entry by entry, (x1 x2, y1 y2). It lets two
nonzero pairs multiply to (0, 0), and after that nothing can be divided. The
complex rule (x1 x2 - y1 y2, x1 y2 + x2 y1) never does, so every pair except
(0, 0) has a reciprocal: the set C* = C \\ {(0, 0)} of Andreescu and Andrica,
Complex Numbers from A to ... Z, section 1.1.1, is exactly the set of pairs
you can divide by.

Every pair is a tuple of exact fractions (fractions.Fraction). A program can
only check finitely many pairs; the page gives the algebra that covers the rest.
"""

from fractions import Fraction as F


def mul(z1, z2):
    """The complex rule: (x1 x2 - y1 y2, x1 y2 + x2 y1)."""
    (x1, y1), (x2, y2) = z1, z2
    return (x1 * x2 - y1 * y2, x1 * y2 + x2 * y1)


def mul_entrywise(z1, z2):
    """The obvious rule: (x1 x2, y1 y2)."""
    (x1, y1), (x2, y2) = z1, z2
    return (x1 * x2, y1 * y2)


def add(z1, z2):
    (x1, y1), (x2, y2) = z1, z2
    return (x1 + x2, y1 + y2)


def reciprocal(z):
    """1/z = (x / (x^2 + y^2), -y / (x^2 + y^2)), for z other than (0, 0)."""
    x, y = z
    n = x * x + y * y
    return (x / n, -y / n)


def pair(x, y):
    return (F(x), F(y))


def show(z):
    return f"({z[0]}, {z[1]})"


def op(a, sign, b):
    """'a - b', with b in brackets when it is negative: -5 - (-12)."""
    return f"{a} {sign} {b}" if b >= 0 else f"{a} {sign} ({b})"


ZERO, ONE = pair(0, 0), pair(1, 0)
MINUS_ONE = pair(-1, 0)

# The test values: negatives, zero, fractions with different denominators,
# and the 0, 1 and -1 the lesson turns on. 49 pairs are made from them.
G = [F(-2), F(-1), F(-1, 2), F(0), F(1, 3), F(1), F(3, 2)]
PAIRS = [(x, y) for x in G for y in G]
NONZERO = [z for z in PAIRS if z != ZERO]


def main() -> None:
    print("1. THE OBVIOUS RULE: MULTIPLY ENTRY BY ENTRY")
    print("   entry by entry:    (x1, y1)(x2, y2) = (x1 x2, y1 y2)")
    print("   the complex rule:  (x1, y1)(x2, y2) = (x1 x2 - y1 y2, x1 y2 + x2 y1)")
    print(f"   Test values: G = {{{', '.join(str(v) for v in G)}}}, making {len(PAIRS)} test pairs (x, y).")
    print()
    squares = all(mul_entrywise(z, z) == (z[0] ** 2, z[1] ** 2) for z in PAIRS)
    roots_e = [z for z in PAIRS if mul_entrywise(z, z) == MINUS_ONE]
    roots_c = [z for z in PAIRS if mul(z, z) == MINUS_ONE]
    print(f"   Entry by entry, z z = (x^2, y^2), on all {len(PAIRS)} test pairs: {squares}")
    print(f"     {'':<44}{'entry by entry':<17}the complex rule")
    print(f"     {'pairs z with z z = (-1, 0)':<44}{len(roots_e):<17}{len(roots_c)}")
    print("   Neither entry of (x^2, y^2) can be negative, so the obvious rule has no")
    print("   square root of -1. The complex rule has two: " + ", ".join(show(z) for z in sorted(roots_c)))
    print()

    print("2. TWO NONZERO PAIRS, PRODUCT ZERO")
    e1, e2 = pair(1, 0), pair(0, 1)
    print(f"   entry by entry:    {show(e1)}{show(e2)} = {show(mul_entrywise(e1, e2))}")
    print(f"   the complex rule:  {show(e1)}{show(e2)} = {show(mul(e1, e2))}")
    zero_e = sum(mul_entrywise(z, w) == ZERO for z in NONZERO for w in NONZERO)
    zero_c = sum(mul(z, w) == ZERO for z in NONZERO for w in NONZERO)
    print(f"     {'':<44}{'entry by entry':<17}the complex rule")
    print(f"     {'pairs of nonzero z, w with z w = (0, 0)':<44}{zero_e:<17}{zero_c}")
    print("   A nonzero pair that multiplies some other nonzero pair to (0, 0) is a ZERO DIVISOR.")
    print("   Entry by entry, (1, 0) is one, and it can never be divided by:")
    print("     (1, 0)(0, 1) = (0, 0) = (1, 0)(0, 0), so dividing both sides by (1, 0)")
    print("     would make (0, 1) = (0, 0).")
    one_e = pair(1, 1)
    no_inverse = all(mul_entrywise(e1, w) != one_e for w in PAIRS)
    identity_e = all(mul_entrywise(z, one_e) == z for z in PAIRS)
    print(f"   Entry by entry the 1 is (1, 1): z (1, 1) = z for all {len(PAIRS)} test pairs: {identity_e}")
    print(f"   and (1, 0) w is (w_x, 0), never (1, 1): no test pair w solves (1, 0) w = (1, 1): {no_inverse}")
    print()

    print("3. WHY THE COMPLEX RULE NEVER DOES THAT")
    identity = all(
        (x1 ** 2 + y1 ** 2) * (x2 ** 2 + y2 ** 2)
        == (x1 * x2 - y1 * y2) ** 2 + (x1 * y2 + x2 * y1) ** 2
        for (x1, y1) in PAIRS for (x2, y2) in PAIRS
    )
    print("     (x1^2 + y1^2)(x2^2 + y2^2) = (x1 x2 - y1 y2)^2 + (x1 y2 + x2 y1)^2")
    print(f"   checked on all {len(PAIRS) ** 2:,} products of test pairs: {identity}")
    print("   If neither factor is (0, 0), the left side is positive, so the product is not (0, 0).")
    print()

    print("4. C* = C \\ {(0, 0)}: THE PAIRS YOU CAN DIVIDE BY")
    print("   The backslash is set difference: C* is every pair except (0, 0).")
    print(f"   Of the {len(PAIRS)} test pairs, C* keeps {len(NONZERO)}.")
    identity_one = all(mul(z, ONE) == z for z in PAIRS)
    print(f"   (1, 0) is the 1 of C:  z (1, 0) = z for all {len(PAIRS)} test pairs: {identity_one}")
    print("   Every z = (x, y) in C* has a reciprocal:  1/z = (x / (x^2 + y^2), -y / (x^2 + y^2))")
    print(f"     {'z':<10} {'x^2 + y^2':<11} {'1/z':<17} z (1/z)")
    for z in [pair(0, 1), pair(1, 1), pair(3, -4), pair(-5, 6)]:
        r = reciprocal(z)
        print(f"     {show(z):<10} {str(z[0] ** 2 + z[1] ** 2):<11} {show(r):<17} {show(mul(z, r))}")
    inverses = all(mul(z, reciprocal(z)) == ONE for z in NONZERO)
    print(f"   z (1/z) = (1, 0) for all {len(NONZERO)} test pairs in C*: {inverses}")
    zero_absorbs = all(mul(ZERO, w) == ZERO for w in PAIRS)
    print(f"   (0, 0) has no reciprocal: (0, 0) w = (0, 0) for all {len(PAIRS)} test pairs w,"
          f" never (1, 0): {zero_absorbs}")
    undo = all(mul(mul(z, w), reciprocal(w)) == z for z in PAIRS for w in NONZERO)
    print("   Division z / w means z (1/w), for w in C*, and it undoes multiplication:")
    print(f"     (z w)(1/w) = z for all {len(PAIRS)} x {len(NONZERO)} = {len(PAIRS) * len(NONZERO):,}"
          f" choices of z and w: {undo}")
    print()

    print("5. PRACTICE, SOLVED")
    print("   Kata 1. The book's two examples (Andreescu and Andrica, section 1.1.1)")
    examples = [
        (pair(-5, 6), pair(1, -2), pair(-4, 4), pair(7, 16)),
        (pair(F(-1, 2), 1), pair(F(-1, 3), F(1, 2)), pair(F(-5, 6), F(3, 2)), pair(F(-1, 3), F(-7, 12))),
    ]
    for z1, z2, book_sum, book_product in examples:
        (x1, y1), (x2, y2) = z1, z2
        p = mul(z1, z2)
        print(f"     z1 = {show(z1)},  z2 = {show(z2)}")
        print(f"       z1 + z2 = ({op(x1, '+', x2)}, {op(y1, '+', y2)}) = {show(add(z1, z2))}")
        print(f"       first entry:   x1 x2 - y1 y2 = ({x1})({x2}) - ({y1})({y2})"
              f" = {op(x1 * x2, '-', y1 * y2)} = {p[0]}")
        print(f"       second entry:  x1 y2 + x2 y1 = ({x1})({y2}) + ({x2})({y1})"
              f" = {op(x1 * y2, '+', x2 * y1)} = {p[1]}")
        agree = add(z1, z2) == book_sum and p == book_product
        print(f"       z1 z2 = {show(p)}      the book: {show(book_sum)} and {show(book_product)}"
              f"   same: {agree}")
    print()
    print("   Kata 2. Every (x, y) with (x, y)(x, y) = (-1, 0)")
    print("     (x, y)(x, y) = (x^2 - y^2, 2xy), so  x^2 - y^2 = -1  and  2xy = 0.")
    print("     2xy = 0 means x = 0 or y = 0. y = 0 needs x^2 = -1: impossible. x = 0 needs y^2 = 1.")
    squares_match = all(mul(z, z) == (z[0] ** 2 - z[1] ** 2, 2 * z[0] * z[1]) for z in PAIRS)
    assert squares_match and sorted(roots_c) == [pair(0, -1), pair(0, 1)]
    print(f"     Exactly two: (0, -1) and (0, 1). Among the {len(PAIRS)} test pairs the search finds: "
          + ", ".join(show(z) for z in sorted(roots_c)))
    print()
    print("   Kata 3. Find z with z (1, 2) = (5, 0)")
    w, target = pair(1, 2), pair(5, 0)
    by_hand = pair(1, -2)
    x, y = by_hand
    assert x - 2 * y == 5 and 2 * x + y == 0
    print("     z = (x, y) gives (x - 2y, 2x + y) = (5, 0): x - 2y = 5 and 2x + y = 0, so z = (1, -2).")
    divided = mul(target, reciprocal(w))
    print(f"     Or divide: z = {show(target)}(1 / {show(w)}) = {show(target)}{show(reciprocal(w))}"
          f" = {show(divided)}")
    print(f"     check: {show(by_hand)}{show(w)} = {show(mul(by_hand, w))}:"
          f" {mul(by_hand, w) == target and divided == by_hand}")
    no_solution = all(mul(z, ZERO) != target for z in PAIRS)
    print("     z (0, 0) = (5, 0) has no solution: z (0, 0) = (0, 0) for every z.")
    print(f"     No test pair solves it: {no_solution}")


if __name__ == "__main__":
    main()
