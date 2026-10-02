#!/usr/bin/env python3
"""The power set axiom: the subsets of a set form a set, and it is bigger.

Run:  python3 power_set.py

∀v0 ∃v1 ∀v2 (v2 ∈ v1 ⇔ ∀v3 (v3 ∈ v2 ⇒ v3 ∈ v0)): for every set a there is a
set 𝒫(a) whose members are exactly the subsets of a. The program builds
𝒫(a) for small a and counts 2^n, shows that the stages V_n are power sets of
each other, finds the sets of V_4 whose power set V_4 lacks, and checks
Cantor's inequality |𝒫(a)| > |a| on every set of V_4.
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


def power(a):
    """𝒫(a): every subset, by choosing each member in or out."""
    items = sorted(a, key=lambda s: (len(show(s)), show(s)))
    return frozenset(frozenset(c) for r in range(len(items) + 1) for c in combinations(items, r))


def is_subset(z, a):
    """∀v3 (v3 ∈ z ⇒ v3 ∈ a), the formula inside the axiom."""
    return all((w not in z) or (w in a) for w in z | a)


def main() -> None:
    V3, V4 = cumulative(3), cumulative(4)
    zero = frozenset()
    one = frozenset({zero})
    two = frozenset({zero, one})

    print("1. THE AXIOM, AND 2^n")
    print("   ∀v0 ∃v1 ∀v2 (v2 ∈ v1 ⇔ ∀v3 (v3 ∈ v2 ⇒ v3 ∈ v0))")
    print("   for every a there is a b whose members are exactly the sets z with")
    print("   'every member of z is a member of a', the subsets of a. b is 𝒫(a).")
    for a in [zero, one, two, frozenset({zero, one, two})]:
        p = power(a)
        print(f"   a = {show(a):<18} |a| = {len(a)}   𝒫(a) = {show(p) if len(a) < 3 else '(8 sets)':<34} |𝒫(a)| = {len(p)} = 2^{len(a)}")
    print("   Each member is in or out, independently: 2 choices, n times.")
    print()

    print("2. THE STAGES ARE POWER SETS OF EACH OTHER: V_{n+1} = 𝒫(V_n)")
    for n in range(1, 4):
        vn, vn1 = frozenset(cumulative(n)), frozenset(cumulative(n + 1))
        print(f"   𝒫(V_{n}) == V_{n + 1}: {power(vn) == vn1}   ({len(vn)} sets -> {len(vn1)} sets)")
    print("   So V_5 has 2^16 = 65,536 sets and V_6 has 2^65536, more than the")
    print("   atoms in the universe; the axiom is the engine of that growth.")
    print()

    print("3. WHERE V_4 RUNS OUT")
    inside = set(V4)
    missing = [a for a in V4 if power(a) not in inside]
    print(f"   of the {len(V4)} sets in V_4, {len(V4) - len(missing)} have their power set in V_4 and")
    print(f"   {len(missing)} do not; every one of those has rank {sorted({rank(a) for a in missing})},")
    print(f"   e.g. a = {show(missing[0])}: rank(𝒫(a)) = {rank(power(missing[0]))}, and V_4 stops at 3.")
    print("   Like pairs, the axiom asks for a set one rank up, and every V_n fails it.")
    print()

    print("4. THE INNER FORMULA IS ⊆, AND PYTHON HAS IT")
    ok = all(is_subset(z, a) == (z <= a) for a in V3 for z in V3)
    print(f"   ∀v3 (v3 ∈ z ⇒ v3 ∈ a) agrees with Python's z <= a for every z, a in V_3: {ok}")
    print()

    print("5. CANTOR: THE POWER SET IS ALWAYS STRICTLY BIGGER")
    ok = all(len(power(a)) > len(a) for a in V4)
    print(f"   |𝒫(a)| > |a| for every a in V_4: {ok}  (2^n > n)")
    print("   For infinite a counting fails and the diagonal argument takes over:")
    print("   no map a -> 𝒫(a) is onto (the reading guide's program runs it). So")
    print("   𝒫(ω) is uncountable, and that is where the real numbers live.")


if __name__ == "__main__":
    main()
