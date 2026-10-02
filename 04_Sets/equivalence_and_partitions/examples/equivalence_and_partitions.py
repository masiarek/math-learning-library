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


if __name__ == "__main__":
    main()
