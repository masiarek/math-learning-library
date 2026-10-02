#!/usr/bin/env python3
"""The replacement scheme: the image of a set under a definable function is a set.

Run:  python3 replacement.py

If F[x, y] is functional (each x has at most one y), then for every set a
the values {y : ∃x ∈ a F[x, y]} form a set. Python: {f(x) for x in a}. The
program shows what 'functional' means, computes images, finds the images
that V_4 lacks, shows that replacement gives comprehension for free, and
runs the finite version of the reason the axiom exists: the function
n ↦ V_n on a universe that is itself a stage.
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


def functional(relation):
    """∀x ∀y ∀z ((F[x, y] ∧ F[x, z]) ⇒ y ≃ z): each x has at most one partner."""
    return all(y == z for x, y in relation for x2, z in relation if x == x2)


def main() -> None:
    V3, V4 = cumulative(3), cumulative(4)
    inside = set(V4)
    zero = frozenset()
    one = frozenset({zero})

    print("1. 'FUNCTIONAL' FIRST: EACH INPUT HAS AT MOST ONE OUTPUT")
    square = {(n, n * n) for n in range(4)}
    roots = {(n * n, n) for n in range(-3, 4)}
    print(f"   F = 'y = x²' on 0..3:         {sorted(square)}   functional: {functional(square)}")
    print(f"   F = 'x = y²', y in -3..3:     {sorted(roots)}")
    print(f"                                 functional: {functional(roots)}   (4 has partners 2 and -2)")
    print("   Only a functional F defines a φ_F, and only then does the scheme apply.")
    print()

    print("2. THE SCHEME, AND THE IMAGE IN PYTHON")
    print("   if F is functional:  ∀a ∃b ∀y (y ∈ b ⇔ ∃x (x ∈ a ∧ F[x, y]))")
    print("   b = {φ_F(x) : x ∈ a}, the image of a; Python: {f(x) for x in a}.")
    a = frozenset(V3)
    print(f"   a = V_3 = {show(a)}")
    print(f"   {{ {{x}} : x ∈ a }}  = {show(frozenset(frozenset({x}) for x in a))}")
    print(f"   {{ ∪x  : x ∈ a }}  = {show(frozenset(frozenset(z for w in x for z in w) for x in a))}   smaller: the image can merge")
    print()

    print("3. WHERE V_4 RUNS OUT: IMAGES THAT GO A RANK UP")
    singleton = lambda x: frozenset({x})
    big_union = lambda x: frozenset(z for w in x for z in w)
    for name, f in [("x ↦ {x}", singleton), ("x ↦ ∪x", big_union)]:
        missing = [b for b in V4 if frozenset(f(x) for x in b) not in inside]
        print(f"   F = {name:<9} image of a in V_4 for all 16 a: {not missing}"
              + (f"   fails for {len(missing)} sets, e.g. a = {show(missing[0])}" if missing else ""))
    print("   Like pairs and power set, a function that lifts rank asks for a set")
    print("   the finite universe lacks; one that lowers rank never does.")
    print()

    print("4. COMPREHENSION FOR FREE (PAGE 116)")
    print("   H[x, y] = (y ≃ x ∧ F[x]) is functional, and its image of a is {x ∈ a : F[x]}:")
    F = lambda x: len(x) == 1
    via_h = frozenset(y for x in a for y in [x] if F(x))
    direct = frozenset(x for x in a if F(x))
    print(f"   {{x ∈ V_3 : x has one member}}: via H = {show(via_h)}, directly = {show(direct)}, equal: {via_h == direct}")
    print()

    print("5. WHY THE AXIOM EXISTS: THE FUNCTION n ↦ V_n")
    stages = [frozenset(cumulative(n)) for n in range(4)]
    for n, v in enumerate(stages):
        print(f"   V_{n} = {show(v):<40} rank {rank(v)}")
    image = frozenset(stages)
    print(f"   the image {{V_0, V_1, V_2, V_3}} has rank {rank(image)}, so it is not in V_4: {image not in inside}")
    print("   V_4 has every V_n for n < 4 and not the set of them. Zermelo's axioms")
    print("   without replacement are in the same position at V_(ω+ω): they prove")
    print("   each V_(ω+n) exists and cannot collect them, so ω + ω, ℵ_ω and every")
    print("   construction 'by recursion on the ordinals' need Fraenkel's axiom.")


if __name__ == "__main__":
    main()
