#!/usr/bin/env python3
"""The axiom of extensionality: a set is its members, and only one set is.

Run:  python3 extensionality.py

∀v0 ∀v1 (∀v2 (v2 ∈ v0 ⇔ v2 ∈ v1) ⇒ v0 ≃ v1): two sets with the same members
are the same set. The program checks the formula on the universe V_4 of
sixteen small sets, shows it as the proof method "a ⊆ b and b ⊆ a, so
a = b", counts how many candidates each other axiom's set has (always one,
which is what "unique by extensionality" means), and builds a universe with
two memberless points, where the axiom fails.
"""

from itertools import combinations


def cumulative(n):
    """V_n, the hereditarily finite sets of rank below n: V_1 = {∅}, V_4 has 16 sets."""
    level = [frozenset()] if n >= 1 else []
    for _ in range(n - 1):
        level = [frozenset(c) for r in range(len(level) + 1) for c in combinations(level, r)]
    return level


def show(s) -> str:
    if not s:
        return "∅"
    return "{" + ", ".join(sorted((show(x) for x in s), key=lambda t: (len(t), t))) + "}"


def same_members(u, x, y):
    """∀v2 (v2 ∈ x ⇔ v2 ∈ y), on the universe u (a dict: point -> set of members)."""
    return all((z in u[x]) == (z in u[y]) for z in u)


def extensionality(u):
    return all((not same_members(u, x, y)) or x == y for x in u for y in u)


def main() -> None:
    V4 = cumulative(4)
    u = {s: set(s) for s in V4}

    print("1. THE AXIOM ON V_4")
    print("   ∀v0 ∀v1 (∀v2 (v2 ∈ v0 ⇔ v2 ∈ v1) ⇒ v0 ≃ v1)")
    print("   for every a and b: if every set is in a exactly when it is in b,")
    print("   then a and b are the same set.")
    print(f"   {len(V4)} sets, {len(V4) ** 2} pairs (a, b) checked: {extensionality(u)}")
    print()

    print("2. HOW IT IS USED: TO PROVE a = b, PROVE a ⊆ b AND b ⊆ a")
    a = frozenset({1, 2, 3, 4, 6, 12})
    b = frozenset(d for d in range(1, 13) if 12 % d == 0)
    print(f"   a = {{1, 2, 3, 4, 6, 12}}, written out;  b = {{d : 1 ≤ d ≤ 12 and d divides 12}}")
    print(f"   every member of a is in b: {all(x in b for x in a)}")
    print(f"   every member of b is in a: {all(x in a for x in b)}")
    print(f"   so a = b: {a == b}   (Python's == on sets is the axiom)")
    print("   Order and repetition are not members, so they do not count:")
    print(f"   {{2, 5}} == {{5, 2}}: {frozenset({2, 5}) == frozenset({5, 2})}   "
          f"{{1, 1, 1}} == {{1}}: {frozenset({1, 1, 1}) == frozenset({1})}")
    print()

    print("3. 'UNIQUE BY EXTENSIONALITY': EACH AXIOM'S SET HAS EXACTLY ONE CANDIDATE")
    V3 = cumulative(3)
    counts = set()
    for x in V3:
        for y in V3:
            candidates = [z for z in V4 if z == frozenset({x, y})]
            counts.add(len(candidates))
    print(f"   for every a, b in V_3, the number of sets in V_4 whose members are")
    print(f"   exactly a and b: {sorted(counts)}.  The pair exists (the axiom of pairs),")
    print("   and extensionality says two candidates would have to be equal,")
    print("   so 'the pair {a, b}' names one set. The same sentence follows")
    print("   every other axiom in the book.")
    print()

    print("4. A UNIVERSE WHERE IT FAILS: TWO POINTS WITH NO MEMBERS")
    atoms = {"a": set(), "b": set(), "c": {"a"}}
    print("   points a, b, c with a, b memberless and c = {a}")
    print(f"   extensionality: {extensionality(atoms)}")
    for x, y in [("a", "b")]:
        print(f"   witness: a and b have the same members ({same_members(atoms, x, y)}),"
              f" and a ≃ b is {x == y}")
    print("   Such points are called atoms or urelements. ZF has none: by")
    print("   extensionality there is exactly one memberless set, ∅, and every")
    print("   other set is built from it.")


if __name__ == "__main__":
    main()
