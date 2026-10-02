#!/usr/bin/env python3
"""An equivalence relation, a partition and the kernel of a function are one object three ways.

Run:  python3 equivalence_and_partitions.py

A partition of S cuts it into disjoint blocks that cover it; an
equivalence relation on S is reflexive, symmetric and transitive; the
kernel of a function f on S relates the inputs that f sends to the same
value. The program lists every partition of a small set, turns each into
an equivalence and back, finds the equivalences among all 512 relations
on {1, 2, 3}, shows that every equivalence is the kernel of a function
and that every function factors through its kernel, and runs the one
everyone uses: congruence mod m.
"""

from itertools import product


def partitions(items):
    """Every partition of a list, as a list of blocks (frozensets)."""
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for smaller in partitions(rest):
        for i, block in enumerate(smaller):
            yield smaller[:i] + [block | {first}] + smaller[i + 1:]
        yield [frozenset({first})] + smaller


def show_partition(p):
    return "{" + ", ".join("{" + ", ".join(map(str, sorted(b))) + "}" for b in sorted(p, key=lambda b: sorted(b))) + "}"


def relation_of(partition):
    """ρ_π: x ρ y when x and y share a block."""
    return frozenset((x, y) for block in partition for x in block for y in block)


def partition_of(rho, base):
    """U/ρ: the set of equivalence classes [u]."""
    return sorted({frozenset(y for y in base if (u, y) in rho) for u in base}, key=lambda b: sorted(b))


def is_equivalence(rho, base):
    refl = all((x, x) in rho for x in base)
    sym = all((y, x) in rho for x, y in rho)
    trans = all((x, z) in rho for x, y in rho for y2, z in rho if y == y2)
    return refl and sym and trans


def kernel(f, base):
    return frozenset((u, v) for u in base for v in base if f(u) == f(v))


def main() -> None:
    base = [1, 2, 3]
    print("1. THE PARTITIONS OF {1, 2, 3}, AND THE RELATION EACH ONE IS")
    print("   a partition: nonempty blocks, pairwise disjoint, with union the whole set.")
    for p in sorted(partitions(base), key=lambda p: (-len(p), show_partition(p))):
        rho = relation_of(p)
        print(f"   π = {show_partition(p):<26} ρ_π has {len(rho):>2} pairs; equivalence: {is_equivalence(rho, base)}")
    print("   Bell numbers: a set of 1, 2, 3, 4, 5 members has",
          ", ".join(str(sum(1 for _ in partitions(list(range(n))))) for n in range(1, 6)), "partitions.")
    print()

    print("2. EQUIVALENCES AMONG ALL 512 RELATIONS ON {1, 2, 3}")
    pairs = [(x, y) for x in base for y in base]
    rels = [frozenset(p for p, keep in zip(pairs, bits) if keep) for bits in product((True, False), repeat=9)]
    eqs = [r for r in rels if is_equivalence(r, base)]
    print(f"   reflexive and symmetric and transitive: {len(eqs)} of {len(rels)}, the same number as partitions.")
    back = all(relation_of(partition_of(r, base)) == r for r in eqs)
    forth = all(partition_of(relation_of(p), base) == sorted(p, key=lambda b: sorted(b)) for p in partitions(base))
    print(f"   partition -> relation -> partition is the identity: {forth}")
    print(f"   equivalence -> classes -> equivalence is the identity: {back}")
    print("   So EQ(S) and PART(S) are in bijection (Simovici–Djeraba, Corollary 1.114).")
    tol = frozenset({(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2)})
    print(f"   a tolerance that is not an equivalence: 1~2, 2~3, but 1~3? {(1, 3) in tol}: transitivity fails,")
    print("   and 'has a block' fails with it: the classes [1] = {1, 2} and [3] = {2, 3} overlap.")
    print()

    print("3. EVERY FUNCTION HAS A KERNEL, AND EVERY EQUIVALENCE IS ONE")
    words = ["set", "map", "pair", "class", "block", "ring", "field"]
    length = len
    ker = kernel(length, words)
    classes = partition_of(ker, words)
    print("   f = length, on", words)
    print("   ker(f) = {(u, v) : f(u) = f(v)} has classes:")
    for c in classes:
        print(f"     length {length(next(iter(c)))}: {sorted(c)}")
    print(f"   ker(f) is an equivalence: {is_equivalence(ker, words)}")
    back_all = all(kernel(lambda x, r=r: next(i for i, b in enumerate(partition_of(r, base)) if x in b), base) == r for r in eqs)
    print(f"   conversely every equivalence on {{1, 2, 3}} is ker of 'which class am I in': {back_all}")
    print()

    print("4. THE DECOMPOSITION THEOREM: f = (inclusion) ∘ (bijection) ∘ (quotient)")
    g = lambda u: next(c for c in classes if u in c)            # U -> U/ker f, onto
    h = lambda c: length(next(iter(c)))                        # U/ker f -> f(U), bijection
    k = lambda y: y                                            # f(U) -> V, one-to-one
    same = all(k(h(g(w))) == length(w) for w in words)
    image = sorted({length(w) for w in words})
    print(f"   U/ker(f) has {len(classes)} classes and f(U) = {image} has {len(image)} values: h is a bijection: {len(classes) == len(image)}")
    print(f"   k(h(g(w))) == f(w) for every w: {same}   (Theorem 1.116)")
    print("   Every function is a surjection onto its classes, then a relabelling, then an inclusion.")
    print()

    print("5. THE ONE EVERYONE USES: CONGRUENCE MOD m")
    m = 5
    Z = range(-7, 8)
    mod = frozenset((p, q) for p in Z for q in Z if (p - q) % m == 0)
    print(f"   p ≡ q (mod {m}) when {m} divides p − q; on −7..7 it is an equivalence: {is_equivalence(mod, list(Z))}")
    for c in partition_of(mod, list(Z)):
        print(f"     [{min(x for x in c if x >= 0)}] = {sorted(c)}")
    print(f"   {len(partition_of(mod, list(Z)))} classes, which are the {m} possible remainders: ℤ/{m}ℤ.")
    print(f"   It is ker(r) for r(n) = n mod {m}: {mod == kernel(lambda n: n % m, list(Z))}")
    print()

    print("6. COMPARING EQUIVALENCES: FINER, COARSER, MEET AND JOIN (ANDRÉ, EXERCISES 7.1 AND 7.4)")
    base3 = [1, 2, 3]
    pairs3 = [(x, y) for x in base3 for y in base3]
    eqs3 = [frozenset(p for p, k in zip(pairs3, bits) if k) for bits in product((True, False), repeat=9)]
    eqs3 = [r for r in eqs3 if is_equivalence(r, base3)]
    meet_ok = all(is_equivalence(r & t, base3) for r in eqs3 for t in eqs3)
    union_ok = sum(1 for r in eqs3 for t in eqs3 if is_equivalence(r | t, base3))
    nested = sum(1 for r in eqs3 for t in eqs3 if r <= t or t <= r)
    print(f"   R ∩ T is an equivalence for all {len(eqs3) ** 2} pairs of equivalences on {{1, 2, 3}}: {meet_ok}")
    print(f"   R ∪ T is one in {union_ok} of {len(eqs3) ** 2} pairs, exactly the {nested} pairs where one contains the other: {union_ok == nested}")
    print("   e.g. {{1, 2}, {3}} ∪ {{1}, {2, 3}} has 1 ~ 2 and 2 ~ 3 but not 1 ~ 3: transitivity fails.")
    print("   R is finer than T (R ⊆ T) when every block of R sits inside a block of T. The")
    print("   equivalences on a set form a lattice under ⊆: meet = intersection, join = the")
    print("   smallest equivalence containing the union (section 7), bottom = Id, top = all pairs.")
    print()

    print("7. THE EQUIVALENCE GENERATED BY A RELATION: CLOSE IT UP")
    base6 = list(range(1, 7))
    R0 = frozenset({(1, 2), (2, 3), (5, 6)})

    def closure(r, base):
        r = set(r) | {(x, x) for x in base} | {(y, x) for x, y in r}
        steps = 0
        while True:
            new = {(x, z) for x, y in r for y2, z in r if y == y2} - r
            if not new:
                return frozenset(r), steps
            r |= new
            steps += 1

    gen, steps = closure(R0, base6)
    print(f"   R = {sorted(R0)} on 1..6 is not an equivalence: {is_equivalence(R0, base6)}")
    print(f"   add the diagonal, the reversed pairs, then shortcuts until none appear ({steps} round):")
    print(f"   classes {show_partition(partition_of(gen, base6))}, {len(gen)} pairs. It is the smallest equivalence containing R:")
    diag = frozenset((x, x) for x in base6)
    minimal = not any(is_equivalence(gen - {p}, base6) and R0 <= gen - {p} for p in gen - diag)
    print(f"   removing any one off-diagonal pair breaks it: {minimal}. The classes are the connected components of the graph of R.")
    print()

    print("8. WELL-DEFINED ON CLASSES: + ON ℤ/5ℤ IS, 'n MOD 3' IS NOT")
    reps = {c: [n for n in range(-10, 11) if n % 5 == c] for c in range(5)}
    ok = all((a + b) % 5 == (a2 + b2) % 5 for c in reps for d in reps for a in reps[c] for b in reps[d] for a2 in reps[c] for b2 in reps[d])
    print(f"   [a] + [b] := [a + b]: the result is the same whichever representatives are picked, all choices in -10..10: {ok}")
    bad = next((a, a2) for c in reps for a in reps[c] for a2 in reps[c] if a % 3 != a2 % 3)
    print(f"   f([n]) := n mod 3 on ℤ/5ℤ is not well defined: {bad[0]} and {bad[1]} are the same class mod 5 and give {bad[0] % 3} and {bad[1] % 3}.")
    print("   A function on classes must give one answer per class; a map from representatives")
    print("   that respects the relation is the only kind that descends to the quotient.")
    print()

    print("9. ORBITS OF A GROUP ACTION ARE AN EQUIVALENCE: A FOUR-BEAD NECKLACE")
    beads = ["".join(b) for b in product("xo", repeat=4)]
    rot = lambda s, k: s[k:] + s[:k]
    same = frozenset((s, rot(s, k)) for s in beads for k in range(4))
    print(f"   {len(beads)} colourings of 4 beads in 2 colours; 'is a rotation of' is an equivalence: {is_equivalence(same, beads)}")
    orbits = partition_of(same, beads)
    print(f"   its classes, the orbits, number {len(orbits)}: {[sorted(o)[0] for o in sorted(orbits, key=lambda o: sorted(o)[0])]} as representatives")
    fixed = [sum(1 for s in beads if rot(s, k) == s) for k in range(4)]
    print(f"   Burnside's count: (fixed by each rotation {fixed}) / 4 = {sum(fixed) // 4}, the same number.")
    print("   Every group acting on a set partitions it into orbits; 'congruent' and 'similar'")
    print("   triangles are the orbits of the rigid motions and of the similarities of the plane.")
    print()

    print("10. COUNTING PARTITIONS: STIRLING NUMBERS, BELL NUMBERS, THE BELL TRIANGLE, NON-CROSSING")
    from functools import lru_cache
    from math import comb

    @lru_cache(None)
    def stirling2(n, k):
        if n == k == 0:
            return 1
        if n == 0 or k == 0:
            return 0
        return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)

    print("   S(n, k), partitions of an n-set into exactly k blocks, S(n, k) = k·S(n−1, k) + S(n−1, k−1):")
    print("   n \\ k " + "".join(f"{k:>5}" for k in range(1, 7)) + "   Bell")
    for n in range(1, 7):
        row = [stirling2(n, k) for k in range(1, 7)]
        print(f"   {n:>5} " + "".join(f"{v:>5}" if v else "    ." for v in row) + f"   {sum(row):>4}")
    counted = {}
    for p in partitions(list(range(5))):
        counted[len(p)] = counted.get(len(p), 0) + 1
    print(f"   the 52 partitions of a 5-set by number of blocks, enumerated: {[counted[k] for k in range(1, 6)]} = S(5, k);")
    print("   the Wikipedia picture draws them in that order: one five-block partition, then 10, 25, 15, 1.")
    tri = [[1]]
    for _ in range(5):
        prev = tri[-1]
        row = [prev[-1]]
        for v in prev:
            row.append(row[-1] + v)
        tri.append(row)
    print("   Bell triangle: start each row with the end of the row above, add the number above to the left:")
    for row in tri:
        print("     " + " ".join(f"{v:>3}" for v in row))
    print("   its left edge 1, 1, 2, 5, 15, 52 is the Bell numbers.")

    def crossing(p):
        blocks = {x: i for i, b in enumerate(p) for x in b}
        pts = sorted(blocks)
        return any(blocks[a] == blocks[c] != blocks[b] == blocks[d]
                   for a in pts for b in pts for c in pts for d in pts if a < b < c < d)

    nc = sum(1 for p in partitions(list(range(5))) if not crossing(p))
    print(f"   non-crossing partitions of 5 points on a circle (no a < b < c < d with a, c in one block and b, d in another): {nc},")
    print(f"   the Catalan number C(10, 5)/6 = {comb(10, 5) // 6}; the picture's crossed pairs of lines are the {52 - nc} crossing ones.")


if __name__ == "__main__":
    main()
