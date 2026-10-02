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

from itertools import combinations, permutations, product
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

    print()
    print("6. THE EQUIVALENT FORMS, ON A FINITE SET WHERE EACH IS A THEOREM")
    divisors = [d for d in range(1, 13) if 12 % d == 0]
    le = lambda x, y: y % x == 0
    chains = [c for r in range(1, len(divisors) + 1) for c in combinations(divisors, r)
              if all(le(x, y) or le(y, x) for x, y in combinations(c, 2))]
    bounded = all(any(all(le(x, u) for x in c) for u in divisors) for c in chains)
    maximal = [x for x in divisors if not any(le(x, y) and y != x for y in divisors)]
    print(f"   the divisors of 12 under 'divides': chains: {len(chains)}, every chain has an")
    print(f"   upper bound: {bounded}; maximal elements: {maximal}   (Zorn's lemma holds)")
    antichains = [a for r in range(1, len(divisors) + 1) for a in combinations(divisors, r)
                  if not any(le(x, y) or le(y, x) for x, y in combinations(a, 2))]
    max_anti = [a for a in antichains
                if not any(set(a) < set(b) for b in antichains)]
    print(f"   antichains: {len(antichains)}; maximal antichains: {len(max_anti)},"
          f" e.g. {max_anti[0]} and {max_anti[-1]}   (Kurepa's principle holds)")
    vectors = [v for v in product((0, 1), repeat=3) if any(v)]

    def independent(vs):
        sums = {tuple(sum(v[i] for v in c) % 2 for i in range(3))
                for r in range(1, len(vs) + 1) for c in combinations(vs, r)}
        return (0, 0, 0) not in sums

    family = [frozenset(c) for r in range(0, 4) for c in combinations(vectors, r) if independent(c)]
    finite_character = all(
        all(frozenset(sub) in family for r in range(len(f) + 1) for sub in combinations(f, r))
        for f in family)
    maximal_sets = [f for f in family if not any(f < g for g in family)]
    print(f"   the 7 nonzero vectors of GF(2)³: linearly independent subsets: {len(family)};")
    print(f"   the family has finite character: {finite_character}; maximal members: {len(maximal_sets)},")
    print(f"   all of size {set(len(f) for f in maximal_sets)}: the bases   (Teichmüller's principle holds)")
    spanning = [frozenset(c) for r in range(1, 8) for c in combinations(vectors, r)
                if len({tuple(sum(v[i] for v in sub) % 2 for i in range(3))
                        for k in range(1, len(c) + 1) for sub in combinations(c, k)}) == 7]
    contains_basis = all(any(b <= s for b in maximal_sets) for s in spanning)
    print(f"   generating sets: {len(spanning)}; each contains a basis: {contains_basis}"
          f"   (downward basis principle holds)")
    print(f"   well-orderings of a 4-set: {len(list(permutations(range(4))))}, the orderings of its")
    print("   members in a row   (well-ordering principle holds)")
    print("   On a finite set every form is a theorem. Halbeisen's chapter 6 proves that on")
    print("   arbitrary sets each is equivalent to the axiom: AC ⇔ Zorn ⇔ Teichmüller ⇔")
    print("   downward basis ⇔ well-ordering ⇔ trichotomy of cardinals ⇔ m² = m, and, with")
    print("   foundation, ⇔ Kurepa ⇔ every vector space has a basis ⇔ multiple choice.")
    print()

    print("7. A BOOLEAN ALGEBRA, WHERE THE WEAKER FORM LIVES")
    base = frozenset({1, 2, 3})
    members = [frozenset(c) for r in range(4) for c in combinations(sorted(base), r)]
    axioms = {
        "commutativity": lambda u, v, w: u | v == v | u and u & v == v & u,
        "associativity": lambda u, v, w: u | (v | w) == (u | v) | w and u & (v & w) == (u & v) & w,
        "distributivity": lambda u, v, w: u & (v | w) == (u & v) | (u & w) and u | (v & w) == (u | v) & (u | w),
        "absorption": lambda u, v, w: u & (u | v) == u and u | (u & v) == u,
        "complementation": lambda u, v, w: u | (base - u) == base and u & (base - u) == frozenset(),
        "De Morgan": lambda u, v, w: base - (u | v) == (base - u) & (base - v),
    }
    for name, law in axioms.items():
        ok = all(law(u, v, w) for u in members for v in members for w in members)
        print(f"   {name:<16} on all {len(members)**3} triples of subsets of {{1, 2, 3}}: {ok}")
    ideals = [frozenset(I) for r in range(1, len(members) + 1) for I in combinations(members, r)
              if frozenset() in frozenset(I)
              and all(x | y in I for x in I for y in I)
              and all(z in I for x in I for z in members if z <= x)]
    prime = [I for I in ideals if base not in I
             and all(x in I or y in I for x in members for y in members if x & y in I)]
    print(f"   ideals of this algebra (down-closed, closed under ∪): {len(ideals)}; prime ideals: {len(prime)}:")
    for I in prime:
        missing = sorted(base - set().union(*I))
        print(f"      the sets avoiding {missing[0]}, {len(I)} of them")
    print("   The prime ideal theorem, 'every Boolean algebra has a prime ideal', follows")
    print("   from choice and is strictly weaker than it (Halpern and Lévy 1971): the")
    print("   first of the weaker forms, with countable choice and dependent choice.")


if __name__ == "__main__":
    main()
