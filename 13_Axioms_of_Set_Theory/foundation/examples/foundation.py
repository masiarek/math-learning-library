#!/usr/bin/env python3
"""The axiom of foundation: every nonempty set has a member that shares nothing with it.

Run:  python3 foundation.py

∀a (a ≠ ∅ ⇒ ∃x (x ∈ a ∧ x ∩ a = ∅)): every nonempty set has an ∈-minimal
member. The program checks it on V_4, derives 'no set is a member of
itself' and 'no two sets are members of each other' as the book's
exercises do, builds universes that break it (a set that is its own only
member, a two-cycle), and shows that in a well-founded universe every set
has a rank, the stage V_n where it first appears.
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


def foundation(u):
    """On a universe u (point -> set of members): every nonempty point has a
    member disjoint from it."""
    return all((not u[a]) or any(not (u[x] & u[a]) for x in u[a]) for a in u)


def witness(u):
    for a in u:
        if u[a] and not any(not (u[x] & u[a]) for x in u[a]):
            return a
    return None


def main() -> None:
    V4 = cumulative(4)
    u = {s: set(s) for s in V4}
    print("1. THE AXIOM ON V_4")
    print("   ∀v0 (¬v0 ≃ ∅ ⇒ ∃v1 (v1 ∈ v0 ∧ v1 ∩ v0 ≃ ∅))")
    print("   every nonempty set a has a member x with no member in common with a.")
    print(f"   checked for all {len(V4)} sets: {foundation(u)}")
    a = frozenset({frozenset(), frozenset({frozenset()}), frozenset({frozenset({frozenset()})})})
    mins = [x for x in a if not (x & a)]
    print(f"   e.g. a = {show(a)}: the members sharing nothing with a: {[show(x) for x in mins]}")
    print("   The disjoint member is the ∈-minimal one: nothing in a is below it.")
    print()

    print("2. WHAT FOLLOWS: NO x ∈ x, NO x ∈ y ∈ x (CUNNINGHAM, EXERCISES 1.5)")
    print("   If x ∈ x, look at {x}: its only member x shares x with it. Foundation")
    print("   says some member of {x} is disjoint from {x}, so x ∉ x.")
    print("   If x ∈ y and y ∈ x, look at {x, y}: x shares y with it, y shares x.")
    print(f"   in V_4, sets with x ∈ x: {sum(1 for x in V4 if x in x)};  pairs with x ∈ y ∈ x: "
          f"{sum(1 for x in V4 for y in V4 if x in y and y in x)}")
    print()

    print("3. UNIVERSES THAT BREAK IT")
    quine = {"q": {"q"}}
    cycle = {"a": {"b"}, "b": {"a"}}
    cycle_pair = {"a": {"b"}, "b": {"a"}, "p": {"a", "b"}}
    for name, uu in [("q = {q}, a set that is its own only member", quine),
                     ("a = {b}, b = {a}, and nothing else", cycle),
                     ("a = {b}, b = {a}, and p = {a, b}", cycle_pair)]:
        w = witness(uu)
        where = (f"failing at {w}: its members are {sorted(uu[w])}, each sharing a member with it"
                 if w else "no point fails: a = {b} has the member b, and b ∩ a = {a} ∩ {b} = ∅")
        print(f"   {name}: foundation {foundation(uu)}, {where}")
    print("   The two-cycle breaks the axiom only once the pair {a, b} is in the")
    print("   universe, which is why the exercise says 'consider {x, y}'.")
    print("   Such universes satisfy extensionality and can satisfy the rest; Aczel's")
    print("   anti-foundation axiom (1988) studies them, and computer science uses")
    print("   them for streams and processes that contain themselves.")
    print()

    print("4. WITH FOUNDATION, EVERY SET HAS A RANK")
    counts = {}
    for s in V4:
        counts[rank(s)] = counts.get(rank(s), 0) + 1
    print("   rank(s) = 1 + max rank of its members, rank(∅) = 0: the stage where s appears")
    for r in sorted(counts):
        print(f"     rank {r}: {counts[r]:>2} sets   (appear in V_{r + 1})")
    print("   Going down by ∈ must stop at ∅, which is foundation; so every set is")
    print("   built in stages, V = ∪ V_α, and a proof 'by induction on rank' covers")
    print("   every set there is. Cori and Lascar introduce the axiom for exactly")
    print("   that hierarchy, and show ZF cannot decide it either way.")


if __name__ == "__main__":
    main()
