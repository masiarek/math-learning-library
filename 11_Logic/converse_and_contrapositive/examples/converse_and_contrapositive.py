#!/usr/bin/env python3
"""If A then B: the converse, the inverse and the contrapositive, tested.

Run:  python3 converse_and_contrapositive.py

A statement "if A then B" makes one claim: whenever A is true, B is true too.
From it come three others by swapping and negating:

    statement        if A then B
    converse         if B then A           swap
    inverse          if not A then not B   negate both
    contrapositive   if not B then not A   swap and negate

The program checks, with a truth table and then by brute force on whole
numbers and triangles, which of these always agree: the statement with its
contrapositive, and the converse with the inverse. The statement and its
converse are independent: either can be true while the other is false.
"""

import math
from itertools import product

T, F = True, False


def implies(a: bool, b: bool) -> bool:
    """'If a then b' fails only when a is true and b is false."""
    return (not a) or b


def word(x: bool) -> str:
    return "T" if x else "F"


def counterexamples(world, A, B):
    """The members of the world where 'if A then B' fails: A holds, B does not."""
    return [x for x in world if A(x) and not B(x)]


def report(name, world, A, B, show=3):
    bad = counterexamples(world, A, B)
    verdict = "true" if not bad else f"FALSE, e.g. {', '.join(map(str, bad[:show]))}"
    print(f"     {name:58} {verdict}")


def main() -> None:
    print("1. THE TRUTH TABLE: WHEN DOES 'IF A THEN B' FAIL?")
    print("      A  B | if A then B | converse | inverse | contrapositive")
    for a, b in product([T, F], repeat=2):
        s, c = implies(a, b), implies(b, a)
        i, cp = implies(not a, not b), implies(not b, not a)
        print(f"      {word(a)}  {word(b)} |      {word(s)}      |    {word(c)}     |    {word(i)}    |       {word(cp)}")
    print("   The statement fails in one row only: A true, B false.")
    print("   Its column matches the contrapositive's in every row: they are one claim.")
    print("   The converse's column matches the inverse's, and differs from the statement's.")
    print()

    nums = range(1, 31)
    div4 = lambda n: n % 4 == 0
    even = lambda n: n % 2 == 0
    print("2. ON THE NUMBERS 1 TO 30: A = 'n is divisible by 4', B = 'n is even'")
    report("statement:      if div by 4, then even", nums, div4, even)
    report("converse:       if even, then div by 4", nums, even, div4)
    report("inverse:        if not div by 4, then odd", nums, lambda n: not div4(n), lambda n: not even(n))
    report("contrapositive: if odd, then not div by 4", nums, lambda n: not even(n), lambda n: not div4(n))
    print("   The counterexamples to the converse and to the inverse are the same numbers:")
    print("   even but not divisible by 4. Each claim is true exactly when its partner is.")
    print()

    triples = [(a, b, c) for c in range(1, 31) for b in range(1, c) for a in range(1, b + 1) if a + b > c]
    right = lambda t: t[0] ** 2 + t[1] ** 2 == t[2] ** 2
    is345 = lambda t: t[0] * 4 == t[1] * 3 and t[0] * 5 == t[2] * 3
    print(f"3. ON {len(triples)} TRIANGLES WITH WHOLE SIDES UP TO 30 (sorted, longest last)")
    report("if sides are 3k, 4k, 5k, then right", triples, is345, right)
    report("converse: if right, then sides are 3k, 4k, 5k", triples, right, is345)
    print("   The first is true and its converse false: 5, 12, 13 is right and not 3-4-5.")
    print("   ('Right' is tested here with a^2 + b^2 = c^2, which the converse of the")
    print("   Pythagorean theorem entitles us to do.)")
    print()

    print("4. BOTH DIRECTIONS AT ONCE: 'IF AND ONLY IF'")
    square = lambda n: math.isqrt(n) ** 2 == n
    odd_divisors = lambda n: sum(1 for d in range(1, n + 1) if n % d == 0) % 2 == 1
    report("if n is a perfect square, it has an odd number of divisors", nums, square, odd_divisors)
    report("if n has an odd number of divisors, it is a perfect square", nums, odd_divisors, square)
    print("   Both true, so: n is a perfect square IF AND ONLY IF it has an odd number of")
    print("   divisors. The Pythagorean theorem with its converse is the same kind of pair:")
    print("   a triangle is right if and only if a^2 + b^2 = c^2, with c the longest side.")
    print()

    print("5. A FALSE 'IF' MAKES THE STATEMENT TRUE: THE ROWS WHERE A FAILS")
    print("   'If n is divisible by 4 then n is even', checked at n = 3, 6, 8:")
    for n in [3, 6, 8]:
        a, b = div4(n), even(n)
        print(f"     n = {n}:  A {word(a)}, B {word(b)}  ->  {word(implies(a, b))}")
    print("   At n = 3 and n = 6 the statement makes no promise, so it cannot be broken.")
    print("   Only a number that is divisible by 4 and odd could refute it, and there is none.")
    print()

    print("6. MANY EXAMPLES PROVE NOTHING; ONE COUNTEREXAMPLE DISPROVES")
    prime = lambda n: n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))
    for p in [2, 3, 5, 7, 11, 13]:
        m = 2 ** p - 1
        print(f"     p = {p:>2} (prime):  2^p - 1 = {m:>4}   prime: {prime(m)}")
    print("   'If p is prime then 2^p - 1 is prime' survives four tests and dies at 11:")
    print("   2047 = 23 x 89. The converse is a different claim, so it gets its own test:")
    report("if 2^n - 1 is prime, then n is prime (n = 1 to 30)", range(1, 31),
           lambda n: prime(2 ** n - 1), prime)
    print("   True here, and true for every n: if n = ab, then 2^a - 1 divides 2^n - 1.")
    print()

    print("7. THE TWO CLASSIC MISTAKES, AS TRUTH-TABLE ROWS")
    print("   Known: if A then B.  Observed: B.  Conclude A?   'Affirming the consequent'.")
    print("     The row A = F, B = T keeps 'if A then B' true, so A may be false. Invalid.")
    print("   Known: if A then B.  Observed: not A.  Conclude not B?   'Denying the antecedent'.")
    print("     The same row: A false, B true. Invalid.")
    print("   Known: if A then B.  Observed: not B.  Conclude not A?   The contrapositive. Valid.")


if __name__ == "__main__":
    main()
