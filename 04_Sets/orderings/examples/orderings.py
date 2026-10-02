#!/usr/bin/env python3
"""Orderings: the six properties a relation can have, and what each combination is called.

Run:  python3 orderings.py

A relation on a finite set is a set of pairs, so reflexive, symmetric,
antisymmetric, asymmetric, transitive and irreflexive are each a loop
that can be run. The program classifies all 512 relations on {a, b, c}
by the names the books give (equivalence, partial order, strict order,
linear order), runs André's four examples and Mortimer's ancestors,
finds maximal, minimal, maximum, minimum, chains and antichains in a
divisibility order, shows the lexicographic order on pairs, and ends
with the partition of real analysis, which is the other meaning of the
word.
"""

from itertools import combinations, product

BASE = ("a", "b", "c")
PAIRS = [(x, y) for x in BASE for y in BASE]
RELATIONS = [frozenset(p for p, keep in zip(PAIRS, bits) if keep) for bits in product((True, False), repeat=9)]


def props(r, base):
    """The six properties of Definition 6.1, each as a loop over the base set."""
    return {
        "reflexive": all((x, x) in r for x in base),
        "irreflexive": all((x, x) not in r for x in base),
        "symmetric": all((y, x) in r for x, y in r),
        "antisymmetric": all((y, x) not in r or x == y for x, y in r),
        "asymmetric": all((y, x) not in r for x, y in r),
        "transitive": all((x, z) in r for x, y in r for y2, z in r if y == y2),
    }


def comparable(r, base):
    return all((x, y) in r or (y, x) in r or x == y for x in base for y in base)


def names(r, base):
    """Every name that applies; the identity relation earns two."""
    p = props(r, base)
    out = []
    if p["reflexive"] and p["symmetric"] and p["transitive"]:
        out.append("equivalence")
    if p["reflexive"] and p["antisymmetric"] and p["transitive"]:
        out.append("linear order" if comparable(r, base) else "partial order")
    if p["irreflexive"] and p["transitive"]:
        out.append("strict linear order" if comparable(r, base) else "strict partial order")
    return out


def name(r, base):
    return ", ".join(names(r, base)) or "none of these"


def show(r):
    return "{" + ", ".join(f"({x}, {y})" for x, y in sorted(r)) + "}" if r else "∅"


def main() -> None:
    print("1. SIX PROPERTIES, EACH A LOOP (ANDRÉ, DEFINITION 6.1)")
    S = ("a", "b", "c", "d")
    examples = {
        "R1 = {(a,a),(b,b),(c,c),(d,d),(a,b)}": frozenset({("a", "a"), ("b", "b"), ("c", "c"), ("d", "d"), ("a", "b")}),
        "R2 = {(a,a),(b,b),(d,d),(a,b)}": frozenset({("a", "a"), ("b", "b"), ("d", "d"), ("a", "b")}),
        "R3 = R1 + (b,a),(b,c),(c,b)": frozenset({("a", "a"), ("b", "b"), ("c", "c"), ("d", "d"), ("a", "b"), ("b", "a"), ("b", "c"), ("c", "b")}),
        "Id_S": frozenset((x, x) for x in S),
        "∅, the empty relation": frozenset(),
    }
    keys = ["reflexive", "irreflexive", "symmetric", "antisymmetric", "asymmetric", "transitive"]
    print(f"   {'relation on {a, b, c, d}':<34}" + "".join(f"{k[:7]:>8}" for k in keys) + "   name")
    for label, r in examples.items():
        p = props(r, S)
        print(f"   {label:<34}" + "".join(f"{str(p[k])[0]:>8}" for k in keys) + f"   {name(r, S)}")
    print("   R1 is a partial order (reflexive, antisymmetric, transitive). R2 is neither reflexive")
    print("   nor irreflexive. ∅ is irreflexive, symmetric, antisymmetric, asymmetric and transitive,")
    print("   all vacuously, so a strict partial order. And R3, which the book calls transitive,")
    print(f"   is not: it has (a, b) and (b, c) but (a, c) ∈ R3 is {('a', 'c') in examples['R3 = R1 + (b,a),(b,c),(c,b)']}. The loop catches what the eye missed.")
    print("   The trap on page 57: symmetric + transitive does not give reflexive; R2 is the witness.")
    sib = frozenset((x, y) for x in "xyz" for y in "xyz" if x != y)
    p = props(sib, "xyz")
    print(f"   'distinct siblings' on three siblings: symmetric {p['symmetric']}, transitive {p['transitive']}:")
    print("   x T y and y T x would need x T x, and nobody is their own distinct sibling. The book")
    print("   calls T transitive on page 56; its H on page 58, 'siblings or the same person', is.")
    print()

    print("2. ALL 512 RELATIONS ON {a, b, c}, SORTED BY NAME")
    counts = {}
    for r in RELATIONS:
        for n in names(r, BASE) or ["none of these"]:
            counts[n] = counts.get(n, 0) + 1
    for k in ["equivalence", "partial order", "linear order", "strict partial order", "strict linear order", "none of these"]:
        print(f"   {k:<22} {counts.get(k, 0):>4}")
    po = {r for r in RELATIONS if any(n.endswith("order") and not n.startswith("strict") for n in names(r, BASE))}
    strict = {r for r in RELATIONS if any(n.startswith("strict") for n in names(r, BASE))}
    ident = frozenset((x, x) for x in BASE)
    to_strict = all((r - ident) in strict for r in po)
    to_nonstrict = all((r | ident) in po for r in strict)
    print(f"   non-strict orders {len(po)} (13 partial, the identity among them, + 6 linear),")
    print(f"   strict orders {len(strict)}; remove the diagonal {to_strict}, add it back {to_nonstrict}: a one-to-one match.")
    print("   equivalences: 5, the Bell number B(3); linear orders: 6 = 3!; partial orders on 3 labelled")
    print("   points: 19, the third term of OEIS A001035 (1, 1, 3, 19, 219, ...).")
    print()

    print("3. MORTIMER'S ANCESTORS: A STRICT PARTIAL ORDER WITH MINIMUM, NO MAXIMUM, TWO MAXIMALS")
    parent = {"M": {"F", "Mo"}, "F": {"GF1", "GM1"}, "Mo": {"GF2", "GM2"},
              "GF1": {"A", "E"}, "GM1": {"A", "E"}, "GF2": {"A", "E"}, "GM2": {"A", "E"}, "A": set(), "E": set()}
    people = list(parent)
    anc = set()
    for x in people:
        stack = list(parent[x])
        while stack:
            y = stack.pop()
            if (x, y) not in anc:
                anc.add((x, y)); stack += list(parent[y])
    anc = frozenset(anc)
    p = props(anc, people)
    print(f"   'a is a descendant of b', {len(anc)} pairs: irreflexive {p['irreflexive']}, asymmetric {p['asymmetric']}, transitive {p['transitive']} -> {name(anc, people)}")
    below = lambda x: {y for y, z in anc if z == x}
    above = lambda x: {z for y, z in anc if y == x}
    minimal = [x for x in people if not below(x)]
    maximal = [x for x in people if not above(x)]
    minimum = [x for x in people if all((x, y) in anc for y in people if y != x)]
    maximum = [x for x in people if all((y, x) in anc for y in people if y != x)]
    print(f"   minimal: {minimal}  minimum: {minimum}  maximal: {maximal}  maximum: {maximum or 'none'}")
    print("   A and E are not comparable, so there are two maximal elements and no maximum;")
    print(f"   M is below everyone, so it is the minimum. Is (A, E) comparable? {('A', 'E') in anc or ('E', 'A') in anc}")
    print()

    print("4. DIVISIBILITY ON 1..12: A POSET WITH CHAINS, ANTICHAINS, MAXIMALS AND A MINIMUM")
    N = range(1, 13)
    div = frozenset((m, n) for m in N for n in N if n % m == 0)
    p = props(div, list(N))
    print(f"   m | n: reflexive {p['reflexive']}, antisymmetric {p['antisymmetric']}, transitive {p['transitive']}, comparable {comparable(div, list(N))} -> {name(div, list(N))}")
    maximal = [n for n in N if not any((n, k) in div for k in N if k != n)]
    print(f"   minimum: 1 (divides everything); maximal: {maximal} (divide nothing else in 1..12); maximum: none")
    chain = [1, 2, 4, 8]
    print(f"   a chain: {chain}, every pair comparable: {all((x, y) in div for x, y in zip(chain, chain[1:]))}")
    primes = [n for n in N if n > 1 and all(n % d for d in range(2, n))]
    print(f"   an antichain: the primes {primes}, no two comparable: {all((x, y) not in div for x in primes for y in primes if x != y)}")
    print("   The subset order ⊆ on P({1, 2, 3}) is the other standard poset; both are drawn as Hasse diagrams.")
    print()

    print("5. LEXICOGRAPHIC ORDER ON PAIRS (ANDRÉ, EXERCISE 7.8, FOR SUBSETS OF {1, 2})")
    subs = [frozenset(c) for r in range(3) for c in combinations((1, 2), r)]
    L = [(A, B) for A in subs for B in subs]
    lex = frozenset(((A, B), (C, D)) for A, B in L for C, D in L if (A < C) or (A == C and B <= D))
    p = props(lex, L)
    print(f"   ((A, B), (C, D)) ∈ R iff A ⊂ C, or A = C and B ⊆ D, on {len(L)} pairs:")
    print(f"   reflexive {p['reflexive']}, antisymmetric {p['antisymmetric']}, transitive {p['transitive']} -> {name(lex, L)}")
    print("   Dictionary order: compare first entries, and only on a tie compare the second.")
    print()

    print("6. A RELATION AS A LOGICAL MATRIX: EACH PROPERTY IS A SHAPE")
    S5 = "abcde"

    def matrix(r, base, mark="1", blank="."):
        return ["".join(mark if (x, y) in r else blank for y in base) for x in base]

    def side_by_side(named):
        rows = [[*m] for _, m in named]
        print("   " + "    ".join(f"{n:<{len(S5)}}" for n, _ in named))
        for i in range(len(S5)):
            print("   " + "    ".join(m[i] for m in rows))

    eq = frozenset({(x, y) for x in "abc" for y in "abc"} | {(x, y) for x in "de" for y in "de"})
    po = frozenset({(x, y) for x in S5 for y in S5 if S5.index(x) <= S5.index(y)})
    strict = frozenset((x, y) for x, y in po if x != y)
    cyc = frozenset(zip(S5, S5[1:] + S5[0]))
    side_by_side([("equiv", matrix(eq, S5)), ("≤", matrix(po, S5)), ("<", matrix(strict, S5)), ("cycle", matrix(cyc, S5))])
    print("   row x, column y holds 1 when x R y. Reflexive: the diagonal is full. Symmetric: the")
    print("   grid is its own mirror image across the diagonal. Antisymmetric: no 1 faces a 1 across")
    print("   it except on the diagonal. Transitive: M·M, with or for + and and for ×, stays inside M.")
    print("   An equivalence is blocks of ones along the diagonal, one block per class; a linear")
    print("   order, with the points listed in order, is a triangle; a strict one has an empty diagonal.")
    print("   The matrix of R⁻¹ is the transpose; of T ∘ R, the Boolean product.")

    def bool_product(a, b, base):
        return frozenset((x, z) for x in base for z in base if any((x, y) in a and (y, z) in b for y in base))

    def is_transitive(r, base):
        return bool_product(r, r, base) <= r

    print(f"   transitive by M·M ⊆ M:  equivalence {is_transitive(eq, S5)}   ≤ {is_transitive(po, S5)}   cycle {is_transitive(cyc, S5)}")
    pairs5 = [(x, y) for x in S5 for y in S5]

    def refl_sym(bits):
        r = frozenset(p for p, keep in zip(pairs5, bits) if keep)
        return r

    from itertools import product as prod
    count = 0
    upper = [(x, y) for x in S5 for y in S5 if x < y]
    for bits in prod((True, False), repeat=len(upper)):
        r = {(x, x) for x in S5} | {p for p, keep in zip(upper, bits) if keep} | {(y, x) for (x, y), keep in zip(upper, bits) if keep}
        if is_transitive(r, S5):
            count += 1
    print(f"   equivalence relations on 5 points, counted as symmetric reflexive matrices that are")
    print(f"   transitive: {count}, the Bell number B(5), which the Wikipedia picture draws as 52 grids;")
    print(f"   {2 ** 25} logical 5 × 5 matrices in all, one per relation.")
    print()

    print("7. THE OTHER 'PARTITION': REAL ANALYSIS CUTS AN INTERVAL, NOT A SET")
    from fractions import Fraction as Fr
    pts = [Fr(0), Fr(1, 2), Fr(1), Fr(2)]
    cells = [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    f = lambda x: x * x
    lower = sum((b - a) * min(f(a), f(b)) for a, b in cells)
    upper = sum((b - a) * max(f(a), f(b)) for a, b in cells)
    print(f"   a partition of [0, 2] in the Riemann sense is a finite list of points {[str(q) for q in pts]},")
    print(f"   cutting it into subintervals {[(str(a), str(b)) for a, b in cells]}, which overlap at endpoints.")
    print(f"   lower sum of x² over it = {lower}, upper sum = {upper}; the integral 8/3 lies between: {lower <= Fr(8, 3) <= upper}")
    fine = [Fr(k, 100) for k in range(0, 201)]
    cells = list(zip(fine, fine[1:]))
    lower = sum((b - a) * min(f(a), f(b)) for a, b in cells)
    upper = sum((b - a) * max(f(a), f(b)) for a, b in cells)
    print(f"   with 200 cells: lower {float(lower):.4f}, upper {float(upper):.4f}, gap {float(upper - lower):.4f}; the gap goes to 0 as the mesh does.")
    print("   Same word, two objects: a set-theory partition is a family of disjoint blocks, and the")
    print("   half-open cells [0, 1/2), [1/2, 1), [1, 2] make it one; the Riemann partition is the")
    print("   list of cut points, and the refinement order on those lists is itself a poset.")


if __name__ == "__main__":
    main()
