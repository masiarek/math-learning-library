#!/usr/bin/env python3
"""Ordinals: transitive sets well-ordered by ∈, and the proof they make possible.

Run:  python3 ordinals.py

Cori and Lascar's Definition 7.12: α is an ordinal when α is transitive
(every member is a subset) and ∈ well-orders α. The program finds the
transitive sets and the ordinals among the sixteen sets of V_4, checks the
book's remarks on them, and then runs Goodstein sequences: numbers that
climb astronomically while the ordinal attached to each step strictly
falls, so the sequence must stop. That theorem about natural numbers has
no proof without ordinals (Kirby and Paris, 1982).
"""

from itertools import combinations


def cumulative(n):
    level = [frozenset()] if n >= 1 else []
    for _ in range(n - 1):
        level = [frozenset(c) for r in range(len(level) + 1) for c in combinations(level, r)]
    return level


def show(s) -> str:
    if not s:
        return "∅"
    return "{" + ", ".join(sorted((show(x) for x in s), key=lambda t: (len(t), t))) + "}"


def transitive(a):
    """∀x ∀y ((x ∈ a ∧ y ∈ x) ⇒ y ∈ a): every member is a subset."""
    return all(x <= a for x in a)


def ordinal(a):
    """Transitive, and ∈ is a strict total order on it (for finite sets that
    is a well-ordering): irreflexive, transitive as a relation, total."""
    if not transitive(a):
        return False
    irreflexive = all(x not in x for x in a)
    trans_rel = all((not (x in y and y in z)) or x in z for x in a for y in a for z in a)
    total = all(x in y or y in x or x == y for x in a for y in a)
    return irreflexive and trans_rel and total


# ---------------------------------------------------------------------------
# Goodstein sequences
# ---------------------------------------------------------------------------

def hereditary(n, b):
    """n in hereditary base b: a list of (digit, exponent) with the exponents
    themselves in hereditary base b, highest power first."""
    terms, power = [], 0
    while n:
        n, digit = divmod(n, b)
        if digit:
            terms.append((digit, hereditary(power, b)))
        power += 1
    return terms[::-1]


def value(terms, b):
    return sum(d * b ** value(e, b) for d, e in terms)


def ordinal_name(terms):
    """The same expression with ω in place of the base: Cantor normal form."""
    if not terms:
        return "0"
    parts = []
    for d, e in terms:
        en = ordinal_name(e)
        if en == "0":
            parts.append(str(d))
        else:
            base = "ω" if en == "1" else (f"ω^{en}" if en.isdigit() or en == "ω" else f"ω^({en})")
            parts.append(base if d == 1 else f"{base}·{d}")
    return " + ".join(parts)


def goodstein(n, steps):
    """The first steps of the Goodstein sequence of n, with the ordinal of each."""
    b, rows = 2, []
    for k in range(steps):
        terms = hereditary(n, b)
        rows.append((k, b, n, ordinal_name(terms)))
        if n == 0:
            break
        n = value(terms, b + 1) - 1
        b += 1
    return rows


def main() -> None:
    V4 = cumulative(4)
    print("1. TRANSITIVE SETS IN V_4: EVERY MEMBER IS ALSO A SUBSET")
    trans = [a for a in V4 if transitive(a)]
    print(f"   {len(trans)} of the {len(V4)} sets are transitive:")
    for a in sorted(trans, key=lambda s: (len(s), len(show(s)))):
        print(f"     {show(a):<34} ordinal: {ordinal(a)}")
    not_trans = next(a for a in V4 if not transitive(a) and len(a) == 1)
    print(f"   not transitive, e.g. {show(not_trans)}: its member {show(next(iter(not_trans)))} is not a subset.")
    print()

    print("2. ORDINALS: TRANSITIVE AND WELL-ORDERED BY ∈ (DEFINITION 7.12)")
    ords = [a for a in V4 if ordinal(a)]
    print(f"   the ordinals in V_4 are the von Neumann numbers {[len(a) for a in sorted(ords, key=len)]}:")
    print(f"   {', '.join(show(a) for a in sorted(ords, key=len))}")
    v3 = frozenset(cumulative(3))
    print(f"   {show(v3)} is transitive but not an ordinal:")
    one, one1 = frozenset({frozenset()}), frozenset({frozenset({frozenset()})})
    print(f"   {show(one)} and {show(one1)} are members, and neither is a member of the other,")
    print("   so ∈ does not order it totally (Proposition 7.17 needs that).")
    print()

    print("3. THE BOOK'S REMARKS, CHECKED ON THESE ORDINALS")
    ords = sorted(ords, key=len)
    print(f"   7.13  α ∉ α for every ordinal: {all(a not in a for a in ords)}")
    print(f"   7.14  every member of an ordinal is an ordinal: {all(ordinal(b) for a in ords for b in a)}")
    print(f"   7.16  α ⊆ β iff α ≤ β (α ∈ β or α = β): {all((a <= b) == (a in b or a == b) for a in ords for b in ords)}")
    print(f"   7.19  α ∪ {{α}} is an ordinal: {all(ordinal(a | frozenset({a})) for a in ords)}")
    print(f"   7.22  for ordinals α, β exactly one of α ∈ β, β ∈ α, α = β: "
          f"{all((a in b) + (b in a) + (a == b) == 1 for a in ords for b in ords)}")
    print()

    print("4. WHAT ORDINALS ARE FOR: A DECREASING SEQUENCE OF THEM MUST STOP")
    print("   Goodstein (1944): write n in hereditary base 2 (exponents in base 2 too),")
    print("   change every 2 to 3 and subtract 1; write that in hereditary base 3,")
    print("   change 3 to 4, subtract 1; and so on. Replace the base by ω and each")
    print("   step's ordinal is strictly smaller, though the numbers explode.")
    for start in (3, 4):
        print(f"   G({start}):")
        print(f"     {'step':>4} {'base':>4} {'value':>6}   ordinal")
        for k, b, n, name in goodstein(start, 9):
            print(f"     {k:>4} {b:>4} {n:>6}   {name}")
    print("   G(3) reaches 0 in 5 steps. G(4) grows for 3·2^402653211 − 2 steps and")
    print("   then reaches 0, and so does every G(n), because its ordinals decrease")
    print("   and a decreasing sequence of ordinals is finite: that is what 'well-")
    print("   ordered' means. Kirby and Paris (1982) proved this statement about")
    print("   natural numbers cannot be proved in Peano arithmetic at all: the")
    print("   ordinals are not decoration here, they are the only known road.")


if __name__ == "__main__":
    main()
