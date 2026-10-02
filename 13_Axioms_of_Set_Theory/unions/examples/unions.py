#!/usr/bin/env python3
"""The axiom of unions: the members of the members form a set.

Run:  python3 unions.py

∀v0 ∃v1 ∀v2 (v2 ∈ v1 ⇔ ∃v3 (v3 ∈ v0 ∧ v2 ∈ v3)): for every set a there is a
set ∪a whose members are the members of the members of a. The program
computes ∪a for small sets, shows why the axiom never fails in a universe
V_n (a union has lower rank than its argument), builds a ∪ b and {a, b, c}
from pairs and unions the way the book does, and shows why the dual
operation, intersection, needs a non-empty argument.
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


def rank(s) -> int:
    return 0 if not s else 1 + max(rank(x) for x in s)


def big_union(a):
    """∪a: every member of every member of a."""
    return frozenset(z for x in a for z in x)


def pair(a, b):
    return frozenset({a, b})


def main() -> None:
    V4 = cumulative(4)
    zero = frozenset()
    one = frozenset({zero})
    two = frozenset({zero, one})
    three = frozenset({zero, one, two})

    print("1. THE AXIOM, AND WHAT ∪a IS")
    print("   ∀v0 ∃v1 ∀v2 (v2 ∈ v1 ⇔ ∃v3 (v3 ∈ v0 ∧ v2 ∈ v3))")
    print("   for every a there is a b such that z is in b exactly when z is in")
    print("   some member of a. That b is ∪a, the union of the family a.")
    for a in [zero, one, frozenset({one}), frozenset({one, frozenset({one})}), three]:
        print(f"   a = {show(a):<22} ∪a = {show(big_union(a))}")
    print("   ∪3 = 2: for a von Neumann number, ∪(n + 1) = n.")
    print()

    print("2. WHY IT NEVER FAILS IN V_n: A UNION HAS LOWER RANK")
    inside = set(V4)
    ok = all(big_union(a) in inside for a in V4)
    drop = all(rank(big_union(a)) <= max(rank(a) - 1, 0) for a in V4)
    print(f"   ∪a is in V_4 for all {len(V4)} sets a of V_4: {ok}")
    print(f"   and rank(∪a) ≤ rank(a) - 1 for every non-empty a: {drop}")
    print("   Pairs and power sets go one rank up and break V_n; unions go")
    print("   one rank down and never do.")
    print()

    print("3. a ∪ b AND {a, b, c} FROM PAIRS AND UNIONS, THE BOOK'S WAY")
    a, b, c = one, frozenset({one}), two
    print(f"   a = {show(a)},  b = {show(b)},  c = {show(c)}")
    print(f"   {{a, b}}            = {show(pair(a, b))}")
    print(f"   a ∪ b = ∪{{a, b}}   = {show(big_union(pair(a, b)))}")
    abc = big_union(pair(pair(a, b), pair(c, c)))
    print(f"   {{a, b, c}} = {{a, b}} ∪ {{c}} = {show(abc)}")
    print("   Python: a | b is a ∪ b, and set().union(*a) is ∪a.")
    print(f"   a | b == ∪{{a, b}}: {(a | b) == big_union(pair(a, b))}")
    print()

    print("4. THE TRAP: ∪a IS NOT a")
    fam = frozenset({frozenset({1, 2}), frozenset({3})})
    print("   a = {{1, 2}, {3}}   has 2 members, both sets")
    print(f"   ∪a = {sorted(big_union(fam))}   has 3 members, the numbers")
    print("   ∪ opens every member one level. Applied to {1, 2, 3} it would")
    print("   open the numbers, which in set theory are sets too.")
    print()

    print("5. THE DUAL, ∩a, NEEDS a ≠ ∅")
    fam = frozenset({frozenset({1, 2, 3}), frozenset({2, 3, 4}), frozenset({3, 4, 5})})
    inter = frozenset.intersection(*fam)
    print(f"   a = {{{{1,2,3}}, {{2,3,4}}, {{3,4,5}}}}:  ∩a = {{x : x is in every member of a}} = {sorted(inter)}")
    print("   For a = ∅ the condition 'x is in every member of a' holds for every x,")
    print("   because there is no member to fail it, so ∩∅ would be the set of all")
    print("   sets, which does not exist. ∩a comes from comprehension inside one")
    print("   member of a, and that needs a member.")
    print(f"   x in every member of ∅, for x = 7: {all(7 in m for m in frozenset())}")


if __name__ == "__main__":
    main()
