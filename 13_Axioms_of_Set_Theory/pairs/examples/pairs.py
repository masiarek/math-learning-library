#!/usr/bin/env python3
"""The axiom of pairs: any two sets fit in a set together.

Run:  python3 pairs.py

∀v0 ∀v1 ∃v2 ∀v3 (v3 ∈ v2 ⇔ (v3 ≃ v0 ∨ v3 ≃ v1)): for any a and b there is a
set whose members are exactly a and b. The program builds the pairs of the
universe V_4, finds the ones V_4 lacks (which is why the axiom fails there),
takes a = b to get singletons, checks the book's remark on when two pairs are
equal, and builds Kuratowski's ordered pair from three pairs.
"""

from itertools import combinations, product


def cumulative(n):
    level = [frozenset()] if n >= 1 else []
    for _ in range(n - 1):
        level = [frozenset(c) for r in range(len(level) + 1) for c in combinations(level, r)]
    return level


def show(s) -> str:
    if not s:
        return "∅"
    return "{" + ", ".join(sorted((show(x) for x in s), key=lambda t: (len(t), t))) + "}"


def rank(s) -> int:
    return 0 if not s else 1 + max(rank(x) for x in s)


def pair(a, b):
    return frozenset({a, b})


def ordered(a, b):
    """Kuratowski's (a, b) = {{a}, {a, b}}: the axiom of pairs used three times."""
    return pair(pair(a, a), pair(a, b))


def main() -> None:
    V3, V4 = cumulative(3), cumulative(4)
    print("1. THE AXIOM, AND WHAT IT BUILDS")
    print("   ∀v0 ∀v1 ∃v2 ∀v3 (v3 ∈ v2 ⇔ (v3 ≃ v0 ∨ v3 ≃ v1))")
    print("   for any a and b there is a c whose members are exactly a and b: {a, b}.")
    for a, b in [(V3[0], V3[1]), (V3[1], V3[2]), (V3[3], V3[0])]:
        print(f"   a = {show(a):<10} b = {show(b):<10} {{a, b}} = {show(pair(a, b))}")
    print()

    print("2. WHERE V_4 RUNS OUT: PAIRS OF SETS FROM THE TOP RANK")
    inside = set(V4)
    have = sum(1 for a, b in product(V4, repeat=2) if pair(a, b) in inside)
    lack = [(a, b) for a, b in product(V4, repeat=2) if pair(a, b) not in inside]
    print(f"   of the {len(V4) ** 2} pairs (a, b) of sets in V_4, {have} have their {{a, b}} in V_4")
    print(f"   and {len(lack)} do not, e.g. a = {show(lack[0][0])}, b = {show(lack[0][1])}:")
    print(f"   rank(a) = {rank(lack[0][0])}, rank(b) = {rank(lack[0][1])}, rank({{a, b}}) = {rank(pair(*lack[0]))},"
          f" and V_4 stops at rank 3.")
    print("   So the axiom fails in every V_n: it asks for a set one rank up.")
    print("   A universe that satisfies it has no top rank.")
    print()

    print("3. a = b GIVES THE SINGLETON {a}")
    for a in V3[:3]:
        print(f"   {{a, a}} with a = {show(a):<10} is {show(pair(a, a))}, one member, not two")
    print()

    print("4. WHEN ARE TWO PAIRS EQUAL? THE BOOK'S REMARK, CHECKED")
    print("   {a, b} = {a', b'}  iff  (a = a' and b = b') or (a = b' and b = a')")
    ok = all((pair(a, b) == pair(c, d)) == ((a == c and b == d) or (a == d and b == c))
             for a, b, c, d in product(V3, repeat=4))
    print(f"   for every a, b, a', b' in V_3 ({len(V3) ** 4} cases): {ok}")
    print(f"   so a pair forgets order: {{a, b}} = {{b, a}} always.")
    print()

    print("5. THREE PAIRS MAKE AN ORDERED PAIR (KURATOWSKI 1921)")
    print("   (a, b) := {{a}, {a, b}}, so (a, b) = (c, d) iff a = c and b = d:")
    ok = all((ordered(a, b) == ordered(c, d)) == (a == c and b == d)
             for a, b, c, d in product(V3, repeat=4))
    print(f"   for every a, b, c, d in V_3: {ok}")
    a, b = V3[0], V3[1]
    print(f"   (∅, {{∅}}) = {show(ordered(a, b))}")
    print(f"   ({{∅}}, ∅) = {show(ordered(b, a))}   different sets, so order is kept")
    print(f"   (∅, ∅)   = {show(ordered(a, a))}   the pair collapses, and still decodes")
    print("   Pairs, then, are enough for order; the Cartesian product page")
    print("   builds the plane from them.")
    print()

    print("6. HAUSDORFF'S PAIR WORKS TOO: (a, b) := {{a, ∅}, {b, {∅}}}")
    zero, one = frozenset(), frozenset({frozenset()})
    haus = lambda a, b: pair(pair(a, zero), pair(b, one))
    ok = all((haus(a, b) == haus(c, d)) == (a == c and b == d) for a, b, c, d in product(V3, repeat=4))
    print(f"   (a, b) = (c, d) iff a = c and b = d, for every a, b, c, d in V_3: {ok}")
    print(f"   Kuratowski (∅, {{∅}}) = {show(ordered(zero, one))}   Hausdorff (∅, {{∅}}) = {show(haus(zero, one))}")
    print("   Different sets with the same property; any set with the property will do,")
    print("   and nobody ever unpacks one. The ∅ and {∅} are tags for 'first' and 'second'.")


if __name__ == "__main__":
    main()
