#!/usr/bin/env python3
"""Set katas: Cunningham's first exercises, checked on every subset of {1, 2, 3}.

Run:  python3 set_katas.py

The exercises of section 1.1 of Cunningham's Set Theory: A First Course are
of three kinds: statements about arbitrary sets A, B, C, which the program
checks on all 512 choices of subsets of {1, 2, 3}; truth sets, which it
computes; and intervals of real numbers, which it computes exactly with
rational endpoints, or checks on a grid of sample points where the
exercise asks for an algebraic solution. A check is not a proof, and the
page says which move each proof needs.
"""

from fractions import Fraction
from itertools import combinations, product

BASE = (1, 2, 3)
SUBSETS = [frozenset(c) for r in range(4) for c in combinations(BASE, r)]
INF = float("inf")


def braces(s) -> str:
    return "{" + ", ".join(str(x) for x in sorted(s)) + "}" if s else "∅"


# ---------------------------------------------------------------------------
# Intervals with rational endpoints: just enough for the exercises
# ---------------------------------------------------------------------------

class Interval:
    def __init__(self, lo, lo_closed, hi, hi_closed):
        self.lo, self.lo_closed, self.hi, self.hi_closed = lo, lo_closed, hi, hi_closed

    def contains(self, x) -> bool:
        above = x > self.lo or (self.lo_closed and x == self.lo)
        below = x < self.hi or (self.hi_closed and x == self.hi)
        return above and below

    def empty(self) -> bool:
        return self.lo > self.hi or (self.lo == self.hi and not (self.lo_closed and self.hi_closed))

    def __str__(self) -> str:
        def end(v):
            return "∞" if v == INF else ("−∞" if v == -INF else str(v))
        return ("[" if self.lo_closed else "(") + f"{end(self.lo)}, {end(self.hi)}" + ("]" if self.hi_closed else ")")


def intersect(a, b):
    if a.lo > b.lo or (a.lo == b.lo and not a.lo_closed):
        lo, lo_c = a.lo, a.lo_closed
    else:
        lo, lo_c = b.lo, b.lo_closed
    if a.hi < b.hi or (a.hi == b.hi and not a.hi_closed):
        hi, hi_c = a.hi, a.hi_closed
    else:
        hi, hi_c = b.hi, b.hi_closed
    return Interval(lo, lo_c, hi, hi_c)


def union(a, b):
    """The union when it is one interval (the two overlap or touch)."""
    if intersect(a, b).empty() and not (a.hi == b.lo and (a.hi_closed or b.lo_closed)) \
            and not (b.hi == a.lo and (b.hi_closed or a.lo_closed)):
        return None
    lo, lo_c = (a.lo, a.lo_closed) if a.lo < b.lo else (b.lo, b.lo_closed) if b.lo < a.lo else (a.lo, a.lo_closed or b.lo_closed)
    hi, hi_c = (a.hi, a.hi_closed) if a.hi > b.hi else (b.hi, b.hi_closed) if b.hi > a.hi else (a.hi, a.hi_closed or b.hi_closed)
    return Interval(lo, lo_c, hi, hi_c)


def difference(a, b):
    """a ∖ b as the list of pieces: a ∩ (left of b) and a ∩ (right of b)."""
    left = Interval(-INF, False, b.lo, not b.lo_closed)
    right = Interval(b.hi, not b.hi_closed, INF, False)
    return [p for p in (intersect(a, left), intersect(a, right)) if not p.empty()]


def main() -> None:
    print("1. STATEMENTS ABOUT SETS: EXERCISES 1.1, 1 TO 7, ON EVERY A, B, C ⊆ {1, 2, 3}")
    katas = [
        ("1", "if a ∉ A ∖ B and a ∈ A, then a ∈ B",
         lambda A, B, C, a: a not in (A - B) and a in A, lambda A, B, C, a: a in B),
        ("2", "if A ⊆ B, then C ∖ B ⊆ C ∖ A",
         lambda A, B, C, a: A <= B, lambda A, B, C, a: (C - B) <= (C - A)),
        ("3", "if A ∖ B ⊆ C, then A ∖ C ⊆ B",
         lambda A, B, C, a: (A - B) <= C, lambda A, B, C, a: (A - C) <= B),
        ("4", "if A ⊆ B and A ⊆ C, then A ⊆ B ∩ C",
         lambda A, B, C, a: A <= B and A <= C, lambda A, B, C, a: A <= (B & C)),
        ("5", "if A ⊆ B and B ∩ C = ∅, then A ⊆ B ∖ C",
         lambda A, B, C, a: A <= B and not (B & C), lambda A, B, C, a: A <= (B - C)),
        ("6", "A ∖ (B ∖ C) ⊆ (A ∖ B) ∪ C",
         lambda A, B, C, a: True, lambda A, B, C, a: (A - (B - C)) <= ((A - B) | C)),
        ("7", "if A ∖ B ⊆ C and A ⊄ C, then A ∩ B ≠ ∅",
         lambda A, B, C, a: (A - B) <= C and not (A <= C), lambda A, B, C, a: bool(A & B)),
        ("1.2, problem 5", "x ∉ A ∖ B  iff  x ∉ A or x ∈ B",
         lambda A, B, C, a: True, lambda A, B, C, a: (a not in (A - B)) == (a not in A or a in B)),
    ]
    cases = [(A, B, C, a) for A in SUBSETS for B in SUBSETS for C in SUBSETS for a in BASE]
    for num, text, hyp, concl in katas:
        applicable = [c for c in cases if hyp(*c)]
        ok = all(concl(*c) for c in applicable)
        print(f"   {num:<15} {text}")
        print(f"   {'':<15} holds in all {len(applicable)} cases where the hypothesis holds (of {len(cases)}): {ok}")
    print("   Every one is proved by taking an arbitrary x and unpacking the")
    print("   definitions of ∖, ∩, ∪ and ⊆; the page names the move for each.")
    print()

    print("2. TRUTH SETS: PROBLEM 1 AND EXERCISES 8, 10, 12")
    print(f"   {{x ∈ ℕ : 3 < x < 11}}         = {braces(x for x in range(0, 30) if 3 < x < 11)}")
    print(f"   {{y ∈ ℤ : y² = 4}}             = {braces(y for y in range(-30, 30) if y * y == 4)}")
    print(f"   {{z ∈ ℕ : z is a multiple of 3}} = {braces(z for z in range(0, 16) if z % 3 == 0)[:-1]}, ...}}   (Cunningham's ℕ starts at 0)")
    P = lambda x: x > 1 / x
    print("   exercise 8, P(x): x > 1/x:  " + "  ".join(f"P({x}) {P(Fraction(x))}" for x in ("2", "-2", "1/2", "-1/2")))
    print("   exercise 10: {1, 4, 9, 16, 25, ...} = {x ∈ ℕ : x = n² for some n ≥ 1};")
    print("                {..., -10, -5, 0, 5, 10, ...} = {y ∈ ℤ : 5 divides y}")
    print(f"   exercise 12(a) {{x ∈ ℕ : 0 < x² < 24}}        = {braces(x for x in range(0, 30) if 0 < x * x < 24)}")
    print(f"   exercise 12(b) {{y ∈ ℤ : y divides 12}}       = {braces(y for y in range(-13, 14) if y and 12 % y == 0)}")
    print(f"   exercise 12(c) {{z ∈ ℕ : 4 divides z}}        = {braces(z for z in range(0, 17) if z % 4 == 0)[:-1]}, ...}}")
    print()

    print("3. INTERVALS: EXERCISE 9 EXACTLY, EXERCISES 11 AND 12(d) ON A GRID")
    a9 = intersect(Interval(-3, False, 2, False), Interval(1, False, 3, False))
    b9 = union(Interval(-3, False, 4, False), Interval(0, False, INF, False))
    c9 = difference(Interval(-3, False, 2, False), Interval(1, True, 3, False))
    print(f"   9(a) (−3, 2) ∩ (1, 3)    = {a9}")
    print(f"   9(b) (−3, 4) ∪ (0, ∞)    = {b9}")
    print(f"   9(c) (−3, 2) ∖ [1, 3)    = {' ∪ '.join(str(p) for p in c9)}")
    grid = [Fraction(k, 8) for k in range(-40, 41)]
    checks = [
        ("11(a)", "{x ∈ ℝ : x² − 1 ≤ 3}", lambda x: x * x - 1 <= 3, Interval(-2, True, 2, True)),
        ("11(b)", "{x ∈ ℝ : x > 0 and (x − 1)² < 1}", lambda x: x > 0 and (x - 1) ** 2 < 1, Interval(0, False, 2, False)),
        ("12(d)", "{y ∈ ℝ⁻ : 1 ≤ y² ≤ 4}", lambda y: y < 0 and 1 <= y * y <= 4, Interval(-2, True, -1, True)),
    ]
    for num, text, pred, claim in checks:
        agree = all(pred(x) == claim.contains(x) for x in grid)
        print(f"   {num} {text:<34} = {str(claim):<10} agrees on {len(grid)} sample points in [−5, 5]: {agree}")
    print("   The grid check is evidence, not proof: solving x² − 1 ≤ 3 is the kata.")


if __name__ == "__main__":
    main()
