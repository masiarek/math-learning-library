#!/usr/bin/env python3
"""The comprehension scheme: a property picks a subset, out of a set you already have.

Run:  python3 comprehension.py

For every formula F: ∀a ∃b ∀x (x ∈ b ⇔ (x ∈ a ∧ F[x])). The set is written
{x ∈ a : F[x]} and Python writes it {x for x in a if F(x)}. The program
builds such sets, shows the scheme is a different axiom for each F, shows
what the 'x ∈ a' buys by dropping it (Russell's paradox, and a set that is
not in the universe), and derives ∅, a ∩ b, a − b and ∩a as the book does.
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


def main() -> None:
    V3, V4 = cumulative(3), cumulative(4)
    inside = set(V4)

    print("1. ONE AXIOM PER FORMULA")
    print("   ∀v1 ∀v2 ... ∀v(n+1) ∃v(n+2) ∀v0 (v0 ∈ v(n+2) ⇔ (v0 ∈ v(n+1) ∧ F[v0, v1, ..., vn]))")
    print("   for every set a there is a set b whose members are the members x of a")
    print("   that satisfy F. The book writes {x ∈ a : F[x]}; Python writes")
    print("   {x for x in a if F(x)}. There is one axiom for each formula F:")
    properties = [
        ("x is empty", lambda x: not x),
        ("x has exactly one member", lambda x: len(x) == 1),
        ("x ∉ x", lambda x: x not in x),
        ("∅ ∈ x", lambda x: frozenset() in x),
    ]
    a = frozenset(V3)
    print(f"   a = V_3 = {show(a)}")
    for name, prop in properties:
        print(f"     {{x ∈ a : {name}}}".ljust(38) + f" = {show(frozenset(x for x in a if prop(x)))}")
    ok = all(frozenset(x for x in b if prop(x)) in inside for b in V4 for _, prop in properties)
    print(f"   each such set is in V_4, for every a in V_4 and these four F: {ok}")
    print("   A subset never has higher rank than the set, so no V_n lacks one.")
    print()

    print("2. WHAT 'x ∈ a' BUYS: DROP IT AND THE UNIVERSE IS NOT ENOUGH")
    R = frozenset(x for x in V4 if x not in x)
    print(f"   {{x : x ∉ x}} over all of V_4 has {len(R)} members (no set here is its own member),")
    print(f"   and that set is in V_4: {R in inside}.  It has rank {rank(R)}; V_4 stops at 3.")
    print("   Unrestricted comprehension demands a set the universe does not have.")
    print()

    print("3. AND WORSE: RUSSELL'S CONTRADICTION, AS A TRUTH TABLE")
    print("   Suppose a set r with  ∀x (x ∈ r ⇔ x ∉ x).  Put x = r:  r ∈ r ⇔ r ∉ r.")
    print("     r ∈ r    r ∉ r    r ∈ r ⇔ r ∉ r")
    for v in (True, False):
        print(f"     {str(v):<8} {str(not v):<8} {v == (not v)}")
    print("   No row makes it true, so no such r exists in any universe. The")
    print("   scheme with 'x ∈ a' only ever gives {x ∈ a : x ∉ x} = a, and a ∉ a.")
    print(f"   for every a in V_4, {{x ∈ a : x ∉ x}} == a: {all(frozenset(x for x in b if x not in x) == b for b in V4)}")
    print()

    print("4. WHAT THE BOOK DERIVES FROM IT (PAGE 114)")
    a = frozenset({1, 2, 3, 4})
    b = frozenset({3, 4, 5, 6})
    fam = frozenset({frozenset({1, 2, 3}), frozenset({2, 3, 4}), frozenset({2, 3, 7})})
    print(f"   ∅     = {{x ∈ a : x ≠ x}}             = {show(frozenset(x for x in a if x != x))}   (any a will do)")
    print(f"   a ∩ b = {{x ∈ a : x ∈ b}}             = {sorted(x for x in a if x in b)}")
    print(f"   a − b = {{x ∈ a : x ∉ b}}             = {sorted(x for x in a if x not in b)}")
    c = next(iter(fam))
    inter = sorted(x for x in c if all(x in m for m in fam))
    print(f"   ∩fam  = {{x ∈ c : x ∈ every m ∈ fam}} = {inter}   for any one member c of fam")
    print("   Each is a comprehension inside a set already in hand, which is why")
    print("   a ∩ b and a − b never need an axiom of their own, and why ∩fam needs")
    print("   fam ≠ ∅: there must be a c to comprehend inside.")


if __name__ == "__main__":
    main()
