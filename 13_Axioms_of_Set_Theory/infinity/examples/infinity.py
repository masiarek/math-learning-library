#!/usr/bin/env python3
"""The axiom of infinity: some set contains ∅ and every successor of its members.

Run:  python3 infinity.py

∃I (∅ ∈ I ∧ ∀x (x ∈ I ⇒ x ∪ {x} ∈ I)): an inductive set exists. The program
shows the successor operation, checks that no set in the finite universe
V_4 is inductive (and why no finite set can be), builds the first members
every inductive set must hold, shows that ω is what all inductive sets have
in common, and states Cori and Lascar's form, 'a limit ordinal exists'.
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


def successor(x):
    """x ∪ {x}: the set x with x itself added as a member."""
    return x | frozenset({x})


def inductive(s):
    return frozenset() in s and all(successor(x) in s for x in s)


def main() -> None:
    print("1. THE SUCCESSOR x ∪ {x}, AND THE AXIOM")
    print("   ∃v0 (∅ ∈ v0 ∧ ∀v1 (v1 ∈ v0 ⇒ v1 ∪ {v1} ∈ v0))   (Cunningham's form)")
    print("   there is a set I that contains ∅ and, with each member x, contains")
    print("   x ∪ {x}. Such a set is called inductive.")
    x = frozenset()
    chain = [x]
    for _ in range(4):
        x = successor(x)
        chain.append(x)
    for k, s in enumerate(chain):
        print(f"   {k} = {show(s)}")
    print("   Each is the set of the ones before it: the von Neumann numbers.")
    print()

    print("2. NO SET IN V_4 IS INDUCTIVE, AND NO FINITE SET CAN BE")
    V4 = cumulative(4)
    found = [s for s in V4 if inductive(s)]
    print(f"   inductive sets among the {len(V4)} sets of V_4: {len(found)}")
    best = max(V4, key=lambda s: sum(1 for c in chain if c in s))
    held = [k for k, c in enumerate(chain) if c in best]
    print(f"   the set holding the longest run of the chain is {show(best)}: it has {held},")
    print(f"   so it needs {max(held) + 1} = {show(chain[max(held) + 1])}, which has rank {max(held) + 1}, outside V_4.")
    print("   An inductive set must hold 0, then 1, then 2, ... with no end, so it")
    print("   is infinite; a finite universe has no infinite set; the axiom fails in")
    print("   every V_n, and in V_ω, the union of them all, which satisfies every")
    print("   other axiom of ZFC. That is why infinity is an axiom and not a theorem.")
    print()

    print("3. ω IS WHAT ALL INDUCTIVE SETS SHARE")
    numbers = {k: c for k, c in enumerate(chain)}
    junk1 = frozenset({"apple", "pear"})
    junk2 = frozenset({"pear", "plum"})
    I1 = frozenset(chain) | junk1
    I2 = frozenset(chain) | junk2
    common = I1 & I2
    print("   Two sets that hold 0..4 plus some junk (standing in for inductive sets):")
    print(f"   I1 = {{0, 1, 2, 3, 4, apple, pear}},  I2 = {{0, 1, 2, 3, 4, pear, plum}}")
    kept = sorted(k for k, c in numbers.items() if c in common)
    print(f"   I1 ∩ I2 keeps the numbers {kept} and the junk {sorted(x for x in common if isinstance(x, str))}")
    print("   The intersection of ALL inductive sets keeps only what every one")
    print("   of them must hold: 0, 1, 2, ... and nothing else. That set is ω,")
    print("   the smallest inductive set, and it exists by comprehension inside")
    print("   any one inductive set the axiom provides.")
    print()

    print("4. ω IS INFINITE IN DEDEKIND'S SENSE")
    print("   n ↦ n ∪ {n} is one-to-one on ω and never hits 0:")
    print("   " + "  ".join(f"{k}->{k + 1}" for k in range(6)) + "  ...")
    print("   so ω matches a proper part of itself, which no finite set does.")
    print()

    print("5. CORI AND LASCAR'S FORM: A LIMIT ORDINAL EXISTS")
    print("   ∃v0 (On[v0] ∧ ¬v0 ≃ ∅ ∧ ∀v1 ¬v0 ≃ v1 ∪ {v1})")
    print("   there is an ordinal that is not ∅ and not the successor of anything.")
    print("   ω is that ordinal: every member n has a successor n + 1 in ω, and ω")
    print("   itself is n + 1 for no n. The two forms are equivalent once ordinals")
    print("   are defined, which the ordinals page does.")


if __name__ == "__main__":
    main()
