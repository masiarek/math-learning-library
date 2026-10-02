#!/usr/bin/env python3
"""What is a set? Check each rule of the definition on real sets.

Run:  python3 what_is_a_set.py

A set is one object determined by its members: *set* and *member of* are
the undefined words, two sets with the same members are one set, a set can
be a member of another set, and a rule picks members out of a set already
in hand. Each section takes one rule and checks it: that equality and
subset can be defined through membership alone, that a set forgets order,
repeats and the rule that built it, that {∅} is not ∅ and that ∈ looks one
level down, and that Russell's rule, cut from a set A, gives a harmless set
that is never a member of A.
"""

from itertools import product


def same_members(a: frozenset, b: frozenset) -> bool:
    """Equality written in membership alone: each member of either is in the other."""
    return all(x in b for x in a) and all(x in a for x in b)


def is_subset(a: frozenset, b: frozenset) -> bool:
    """Subset written in membership alone."""
    return all(x in b for x in a)


def main() -> None:
    print("1. MEMBERSHIP IS THE ONLY PRIMITIVE")
    print("   Define A = B as: every member of A is in B, and every member of B is in A.")
    print("   Define A ⊆ B as: every member of A is in B.")
    universe = [0, 1, 2]
    subsets = [frozenset(x for x, keep in zip(universe, bits) if keep)
               for bits in product([0, 1], repeat=len(universe))]
    pairs = [(a, b) for a in subsets for b in subsets]
    eq_agree = all(same_members(a, b) == (a == b) for a, b in pairs)
    sub_agree = all(is_subset(a, b) == (a <= b) for a, b in pairs)
    print(f"   subsets of {{0, 1, 2}}: {len(subsets)}; pairs of them: {len(pairs)}")
    print(f"   same_members(A, B) == (A == B) on every pair:  {eq_agree}")
    print(f"   is_subset(A, B) == (A <= B) on every pair:     {sub_agree}")
    print("   Python's == and <= on sets add nothing to 'in'. 'Set' and 'member of'")
    print("   are the undefined words; equality and subset are written in them.")
    print()

    print("2. EXTENSIONALITY: A SET IS ITS MEMBERS AND NOTHING ELSE")
    by_square = {n for n in range(-5, 6) if n * n < 10}
    by_range = set(range(-3, 4))
    no_negative_squares = {n for n in range(10) if n * n < 0}
    no_long_words = {w for w in ["set"] if len(w) > 5}
    rows = [
        ("{2, 5} == {5, 2}", {2, 5} == {5, 2}, "order is not recorded"),
        ("{1, 1, 2} == {1, 2}", {1, 1, 2} == {1, 2}, "repeats are not recorded"),
        ("{n in -5..5 : n*n < 10} == {-3..3}", by_square == by_range, "the rule is not recorded"),
        ("{n in 0..9 : n*n < 0} == {w in [set] : len(w) > 5}", no_negative_squares == no_long_words, ""),
    ]
    for text, holds, note in rows:
        print(f"   {text:<52} is {holds!s:<6} {note}".rstrip())
    distinct_empties = len({frozenset(no_negative_squares), frozenset(no_long_words)})
    print(f"   distinct empty sets among the two:  {distinct_empties}")
    print("   Two rules that select nothing select the same set: THE empty set.")
    print()

    print("3. A SET IS ONE OBJECT, SO A SET CAN BE A MEMBER")
    empty = frozenset()
    box = frozenset({empty})
    print(f"   len(∅) = {len(empty)},  len({{∅}}) = {len(box)},  ∅ == {{∅}} is {empty == box}")
    one = frozenset({1})
    one_one = frozenset({one})
    print(f"   1 ∈ {{1}}: {1 in one},  {{1}} ∈ {{{{1}}}}: {one in one_one},  1 ∈ {{{{1}}}}: {1 in one_one}")
    print("   ∈ looks exactly one level down: a member of a member is not a member.")
    homes = [s for s in subsets if 1 in s]
    print(f"   subsets of {{0, 1, 2}} that have 1 as a member:  {len(homes)} of {len(subsets)}")
    print("   One object is a member of many sets at once: a set is not a box it sits in.")
    print()

    print("4. SEPARATION: A RULE PICKS FROM A SET YOU ALREADY HAVE")
    a = frozenset({empty, box, frozenset({box})})
    r = frozenset(x for x in a if x not in x)
    print(f"   A = {{∅, {{∅}}, {{{{∅}}}}}}, {len(a)} members")
    print(f"   R = {{x ∈ A : x ∉ x}} has {len(r)} members;  R == A is {r == a}")
    print(f"   R ∈ A is {r in a}")
    print("   Russell's rule, cut from A, is a harmless set, and it is never a member of")
    print("   the set it was cut from. So no set has every set as a member.")


if __name__ == "__main__":
    main()
