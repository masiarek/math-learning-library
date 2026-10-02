#!/usr/bin/env python3
"""Function katas: Hrbacek and Jech's exercises on functions, checked before they are proved.

Run:  python3 function_katas.py

Exercises 3.1 to 3.7 and 3.12 of chapter 2 of Hrbacek and Jech's
Introduction to Set Theory. The three concrete functions of 3.2 and 3.3,
2x - 1, sqrt(x) and 1/x, are composed and inverted exactly on rational
points (perfect squares where a square root is taken); every statement
about arbitrary functions is checked on all partial functions on
{1, 2, 3}, 64 of them, and all pairs where the statement needs two. A
check is evidence that the claim was read correctly; the page has the
proofs.
"""

from fractions import Fraction as Fr
from itertools import combinations, product

BASE = (1, 2, 3)
PAIRS = [(x, y) for x in BASE for y in BASE]
RELATIONS = [frozenset(p for p, k in zip(PAIRS, bits) if k) for bits in product((True, False), repeat=9)]
SUBSETS = [frozenset(c) for r in range(4) for c in combinations(BASE, r)]


def is_function(r):
    return all(y == z for x, y in r for x2, z in r if x == x2)


def one_to_one(r):
    return all(x == x2 for x, y in r for x2, y2 in r if y == y2)


FUNCS = [r for r in RELATIONS if is_function(r)]
INJ = [f for f in FUNCS if one_to_one(f)]


def dom(r):
    return {x for x, y in r}


def ran(r):
    return {y for x, y in r}


def inv(r):
    return frozenset((y, x) for x, y in r)


def comp(g, f):
    """g ∘ f: first f, then g."""
    return frozenset((x, z) for x, y in f for y2, z in g if y == y2)


def image(r, a):
    return {y for x, y in r if x in a}


def restrict(f, a):
    return frozenset((x, y) for x, y in f if x in a)


def ident(a):
    return frozenset((x, x) for x in a)


def show(r):
    return "{" + ", ".join(f"({x}, {y})" for x, y in sorted(r)) + "}" if r else "∅"


def main() -> None:
    print("3.1  IF ran f ⊆ dom g THEN dom(g ∘ f) = dom f")
    cases = [(f, g) for f in FUNCS for g in FUNCS if ran(f) <= dom(g)]
    print(f"     pairs of partial functions on {{1, 2, 3}} with ran f ⊆ dom g: {len(cases)};"
          f" dom(g ∘ f) == dom f in all: {all(dom(comp(g, f)) == dom(f) for f, g in cases)}")
    bad = next((f, g) for f in FUNCS for g in FUNCS if not ran(f) <= dom(g) and dom(comp(g, f)) != dom(f))
    print(f"     without the hypothesis it fails, e.g. f = {show(bad[0])}, g = {show(bad[1])}: dom(g ∘ f) = {dom(comp(*reversed(bad))) or '∅'}")
    print()

    print("3.2  THE FOUR COMPOSITIONS OF f1 = 2x − 1, f2 = √x (x > 0), f3 = 1/x (x ≠ 0)")
    f1 = lambda x: 2 * x - 1
    f2 = lambda x: Fr(int(x.numerator ** 0.5 + 0.5), int(x.denominator ** 0.5 + 0.5)) if x > 0 and is_square(x) else None
    f3 = lambda x: 1 / x if x != 0 else None
    rows = [("f2 ∘ f1", lambda x: f2(f1(x)), "√(2x − 1)", "x ≥ 1/2", "[0, ∞)"),
            ("f1 ∘ f2", lambda x: None if f2(x) is None else f1(f2(x)), "2√x − 1", "x > 0", "(−1, ∞)"),
            ("f3 ∘ f1", lambda x: f3(f1(x)), "1/(2x − 1)", "x ≠ 1/2", "ℝ ∖ {0}"),
            ("f1 ∘ f3", lambda x: None if f3(x) is None else f1(f3(x)), "2/x − 1", "x ≠ 0", "ℝ ∖ {−1}")]
    sample = [Fr(1, 2), Fr(5, 2), Fr(1), Fr(4), Fr(9, 4), Fr(0), Fr(-1), Fr(1, 4)]
    print(f"     {'':<9} {'formula':<12} {'domain':<9} {'range':<10} values at x = " + ", ".join(str(s) for s in sample))
    for name, h, formula, d, r in rows:
        vals = []
        for x in sample:
            try:
                v = h(x)
            except ZeroDivisionError:
                v = None
            vals.append("—" if v is None else str(v))
        print(f"     {name:<9} {formula:<12} {d:<9} {r:<10} " + ", ".join(vals))
    print("     — marks a point outside the domain: dom(g ∘ f) = {x ∈ dom f : f(x) ∈ dom g} (Theorem 3.5).")
    print()

    print("3.3  f1, f2, f3 ARE ONE-TO-ONE; THEIR INVERSES")
    inv1 = lambda y: (y + 1) / 2
    inv2 = lambda y: y * y
    inv3 = lambda y: 1 / y
    xs = [Fr(-3), Fr(-1, 2), Fr(1, 4), Fr(1), Fr(9, 4), Fr(4), Fr(25)]
    ok1 = all(inv1(f1(x)) == x and f1(inv1(x)) == x for x in xs)
    ok2 = all(inv2(f2(x)) == x and f2(inv2(x)) == x for x in xs if x > 0 and is_square(x))
    ok3 = all(inv3(f3(x)) == x and f3(inv3(x)) == x for x in xs)
    print(f"     f1⁻¹(y) = (y + 1)/2 on ℝ:        f1⁻¹∘f1 = id and f1∘f1⁻¹ = id on samples: {ok1}")
    print(f"     f2⁻¹(y) = y² on (0, ∞):          same, on perfect squares: {ok2}")
    print(f"     f3⁻¹(y) = 1/y on ℝ ∖ {{0}}:       same (f3 is its own inverse): {ok3}")
    print("     dom f_i = ran f_i⁻¹ and ran f_i = dom f_i⁻¹: ℝ and ℝ; (0, ∞) and (0, ∞); ℝ∖{0} twice.")
    print()

    print("3.4  INVERTIBLE MEANS A TWO-SIDED INVERSE; A ONE-SIDED ONE IS NOT ENOUGH")
    a = all(comp(inv(f), f) == ident(dom(f)) and comp(f, inv(f)) == ident(ran(f)) for f in INJ)
    print(f"     (a) for every one-to-one f ({len(INJ)} of them): f⁻¹∘f = Id_dom f and f∘f⁻¹ = Id_ran f: {a}")
    b = all(one_to_one(f) and restrict(g, ran(f)) == inv(f)
            for f in FUNCS for g in FUNCS if comp(g, f) == ident(dom(f)) and dom(f))
    print(f"     (b) g∘f = Id_dom f forces f one-to-one and g↾ran f = f⁻¹, all pairs: {b}")
    f, h = next((f, h) for f in FUNCS for h in FUNCS if comp(f, h) == ident(ran(f)) and ran(f) and not one_to_one(f))
    print(f"         but f∘h = Id_ran f does not: f = {show(f)}, h = {show(h)}, f∘h = {show(comp(f, h))}, f not one-to-one")
    print()

    print("3.5  COMPOSITION OF ONE-TO-ONE FUNCTIONS, AND (g∘f)⁻¹ = f⁻¹∘g⁻¹")
    c = all(one_to_one(comp(g, f)) and inv(comp(g, f)) == comp(inv(f), inv(g)) for f in INJ for g in INJ)
    print(f"     all {len(INJ) ** 2} pairs of one-to-one f, g: {c}   (the order reverses: socks on, shoes on; shoes off, socks off)")
    print()

    print("3.6  INVERSE IMAGES UNDER A FUNCTION RESPECT ∩ AND −  (RELATIONS ONLY RESPECT ∪)")
    pre = lambda f, b: image(inv(f), b)
    a6 = all(pre(f, A & B) == pre(f, A) & pre(f, B) for f in FUNCS for A in SUBSETS for B in SUBSETS)
    b6 = all(pre(f, A - B) == pre(f, A) - pre(f, B) for f in FUNCS for A in SUBSETS for B in SUBSETS)
    rel = all(image(inv(r), A & B) == image(inv(r), A) & image(inv(r), B) for r in RELATIONS for A in SUBSETS for B in SUBSETS)
    print(f"     (a) f⁻¹[A ∩ B] = f⁻¹[A] ∩ f⁻¹[B]: {a6}   (b) f⁻¹[A − B] = f⁻¹[A] − f⁻¹[B]: {b6}   ({len(FUNCS) * 64} cases each)")
    print(f"     the same with an arbitrary relation in place of f: {rel}   — a function sends x to ONE value, a relation may not")
    print()

    print("3.7  f ∩ A² VERSUS f ↾ A")
    f, A = next((f, A) for f in FUNCS for A in SUBSETS if (f & frozenset(product(A, A))) != restrict(f, A))
    print(f"     f = {show(f)}, A = {set(A)}: f ↾ A = {show(restrict(f, A))} but f ∩ A² = {show(f & frozenset(product(A, A)))}")
    print("     the restriction keeps a pair whose value lies outside A; the intersection with A² does not.")
    print()

    print("3.12 IMAGES AND INVERSE IMAGES OF UNIONS AND INTERSECTIONS")
    fam = [(A, B) for A in SUBSETS for B in SUBSETS]
    u = all(image(f, A | B) == image(f, A) | image(f, B) for f in FUNCS for A, B in fam)
    pu = all(pre(f, A | B) == pre(f, A) | pre(f, B) for f in FUNCS for A, B in fam)
    i = all(image(f, A & B) <= image(f, A) & image(f, B) for f in FUNCS for A, B in fam)
    pi = all(pre(f, A & B) == pre(f, A) & pre(f, B) for f in FUNCS for A, B in fam)
    inj = all(image(f, A & B) == image(f, A) & image(f, B) for f in INJ for A, B in fam)
    print(f"     f[∪] = ∪f[]: {u}   f⁻¹[∪] = ∪f⁻¹[]: {pu}   f[∩] ⊆ ∩f[]: {i}   f⁻¹[∩] = ∩f⁻¹[]: {pi}")
    print(f"     f[∩] = ∩f[] when f is one-to-one: {inj}; in general not, e.g. f = {{(1, 1), (2, 1)}}, A = {{1}}, B = {{2}}:")
    f = frozenset({(1, 1), (2, 1)})
    print(f"     f[A ∩ B] = {image(f, frozenset()) or '∅'}, f[A] ∩ f[B] = {image(f, {1}) & image(f, {2})}")
    print()

    print("4.1  REFLEXIVE, SYMMETRIC, TRANSITIVE? SIX RELATIONS, CHECKED ON A FINITE PIECE")
    Z = list(range(-4, 5))
    N = list(range(0, 8))
    PA = [frozenset(c) for r in range(3) for c in combinations((1, 2), r)]
    tests = [
        ("(a) x > y on ℤ", Z, lambda x, y: x > y),
        ("(b) n divides m on ℤ", [z for z in Z if z], lambda n, m: m % n == 0),
        ("(c) x ≠ y on ℕ", N, lambda x, y: x != y),
        ("(d) ⊆ on 𝒫({1, 2})", PA, lambda x, y: x <= y),
        ("(d) ⊂ on 𝒫({1, 2})", PA, lambda x, y: x < y),
        ("(e) ∅ in ∅", [], lambda x, y: False),
        ("(f) ∅ in {1, 2}", [1, 2], lambda x, y: False),
    ]
    print(f"     {'relation':<22} {'reflexive':>9} {'symmetric':>9} {'transitive':>10}   note")
    for name, base, rel in tests:
        refl = all(rel(x, x) for x in base)
        sym = all(not rel(x, y) or rel(y, x) for x in base for y in base)
        trans = all(not (rel(x, y) and rel(y, z)) or rel(x, z) for x in base for y in base for z in base)
        note = {"(e) ∅ in ∅": "all three hold vacuously: no element to fail them",
                "(f) ∅ in {1, 2}": "1 is not related to 1, so not reflexive; the other two are vacuous",
                "(b) n divides m on ℤ": "not antisymmetric on ℤ: 1 | −1 and −1 | 1"}.get(name, "")
        print(f"     {name:<22} {str(refl):>9} {str(sym):>9} {str(trans):>10}   {note}")
    print("     A finite piece can refute a property, never confirm it; the page gives the arguments.")


def is_square(q: Fr) -> bool:
    n, d = q.numerator, q.denominator
    return n >= 0 and int(n ** 0.5 + 0.5) ** 2 == n and int(d ** 0.5 + 0.5) ** 2 == d


if __name__ == "__main__":
    main()
