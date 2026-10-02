#!/usr/bin/env python3
"""The axiom of choice: a product of nonempty sets is nonempty.

Run:  python3 choice.py

For every family (a_i) of nonempty sets there is a choice function f with
f(i) ∈ a_i for every i. The program counts choice functions for finite
families (there are always some, and the count is the product of the
sizes), shows that a definable rule makes the axiom unnecessary (least
element of a set of numbers), shows Russell's shoes and socks, and lists
what the axiom is equivalent to and what it buys.
"""

from itertools import combinations, product
from math import prod


def main() -> None:
    print("1. THE AXIOM, THREE WAYS")
    print("   Cori and Lascar: the product ∏ a_i of a family of nonempty sets is nonempty.")
    print("   Choice function:  for every set a of nonempty sets there is f with f(x) ∈ x for x ∈ a.")
    print("   Zermelo 1904:     for pairwise disjoint nonempty sets there is a set meeting each in one point.")
    print("   A member of the product IS a choice function: a tuple with one entry per index.")
    print()

    print("2. FOR FINITE FAMILIES IT IS A THEOREM: COUNT THE CHOICE FUNCTIONS")
    base = (1, 2, 3)
    nonempty = [frozenset(c) for r in range(1, 4) for c in combinations(base, r)]
    print(f"   the {len(nonempty)} nonempty subsets of {{1, 2, 3}}, and every family drawn from them:")
    families = [frozenset(f) for r in range(0, len(nonempty) + 1) for f in combinations(nonempty, r)]
    total_ok = 0
    shown = 0
    for fam in families:
        members = sorted(fam, key=lambda s: (len(s), sorted(s)))
        count = len(list(product(*members))) if members else 1
        assert count == prod(len(s) for s in members)
        total_ok += count > 0
        if len(members) in (2, 3) and shown < 4:
            shown += 1
            desc = ", ".join("{" + ", ".join(map(str, sorted(s))) + "}" for s in members)
            first = next(iter(product(*members)))
            print(f"     family {desc:<30} choice functions: {count:>2}   e.g. pick {first}")
    print(f"   families checked: {len(families)}; with at least one choice function: {total_ok}")
    print("   The count is the product of the sizes, never zero. For a finite family")
    print("   the proof is by induction on its size and needs no axiom.")
    print()

    print("3. WHEN A RULE EXISTS, NO AXIOM IS NEEDED")
    fam = [frozenset({5, 9, 2}), frozenset({7, 3}), frozenset({8})]
    print("   a family of nonempty sets of natural numbers:",
          ", ".join("{" + ", ".join(map(str, sorted(s))) + "}" for s in fam))
    print(f"   rule 'take the least':  {[min(s) for s in fam]}")
    print("   ℕ is well-ordered, so 'the least member' is a formula, and the choice")
    print("   function exists by replacement. The same for any well-ordered set.")
    print()

    print("4. RUSSELL'S SHOES AND SOCKS")
    print("   infinitely many pairs of shoes:  pick the left one   (a rule: no axiom)")
    print("   infinitely many pairs of socks:  the two are alike    (no rule: the axiom)")
    print("   With finitely many pairs of socks you point at one from each; with")
    print("   infinitely many, 'point at one from each' is exactly what the axiom grants.")
    print()

    print("5. WHAT IT BUYS, AND WHAT IT COSTS")
    rows = [
        ("Zermelo 1904", "every set can be well-ordered"),
        ("Zorn's lemma", "a chain-bounded poset has a maximal element"),
        ("linear algebra", "every vector space has a basis"),
        ("analysis", "Hahn–Banach; a non-measurable set of reals (Vitali)"),
        ("Banach–Tarski 1924", "one ball cut into five pieces reassembles as two"),
        ("Gödel 1938", "AC cannot be refuted from ZF (true in L)"),
        ("Cohen 1963", "AC cannot be proved from ZF either"),
    ]
    for who, what in rows:
        print(f"   {who:<22} {what}")
    print("   The first three are equivalent to the axiom over ZF, not consequences")
    print("   of it: assume any one and you have assumed choice.")


if __name__ == "__main__":
    main()
