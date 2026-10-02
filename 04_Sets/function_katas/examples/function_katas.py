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

    print()
    print("S1   SULLIVAN 2.1, PROBLEMS 19 TO 30: IS THE RELATION A FUNCTION?")
    rels = [
        ("19 person → birthday", {("Elvis", "Jan. 8"), ("Colleen", "Mar. 15"), ("Kaleigh", "Mar. 15"), ("Marissa", "Sept. 17")}),
        ("20 father → daughter", {("Bob", "Beth"), ("Bob", "Diane"), ("John", "Linda"), ("Chuck", "Marcia")}),
        ("21 education → income", {("< 9th", 18120), ("9th–12th", 23251), ("HS graduate", 36055), ("some college", 45810), ("college graduate", 67165)}),
        ("22 hours → salary", {("20 h", 200), ("20 h", 300), ("30 h", 350), ("40 h", 425)}),
        ("23", {(2, 6), (-3, 6), (4, 9), (2, 10)}),
        ("24", {(-2, 5), (-1, 3), (3, 7), (4, 12)}),
        ("25", {(0, -2), (1, 3), (2, 3), (3, 7)}),
        ("26", {(1, 3), (2, 3), (3, 3), (4, 3)}),
        ("27", {(-4, 4), (-3, 3), (-2, 2), (-1, 1), (-4, 0)}),
        ("28", {(3, 3), (3, 5), (0, 1), (-4, 6)}),
        ("29", {(-2, 16), (-1, 4), (0, 3), (1, 4)}),
        ("30", {(-1, 8), (0, 3), (2, -1), (4, 3)}),
    ]
    for name, r in rels:
        d, rn = sorted(map(str, dom(r))), sorted(ran(r), key=str)
        why = ""
        if not is_function(r):
            rs = sorted(r, key=lambda pair: (str(pair[0]), str(pair[1])))
            x = next(x for x, y in rs for x2, z in rs if x == x2 and y != z)
            why = f"   {x} is paired twice"
        print(f"     {name:<24} dom {len(d)}, ran {len(rn)}   function: {str(is_function(r)):<5}{why}")
    print("     One test for a diagram and for a set of pairs: no first member twice.")
    print()

    print("S2   SULLIVAN 2.1, PROBLEMS 31 TO 42: DOES THE EQUATION DEFINE y AS A FUNCTION OF x?")
    grid = [Fr(k, 4) for k in range(-16, 17)]

    def solutions(eq, x):
        return {y for y in grid if eq(x, y)}

    eqs = [
        ("31 y = x³", lambda x, y: y == x ** 3),
        ("32 y = 2x² − 3x + 4", lambda x, y: y == 2 * x * x - 3 * x + 4),
        ("33 y = |x|", lambda x, y: y == abs(x)),
        ("34 y = 1/x", lambda x, y: x != 0 and y == 1 / x),
        ("35 y = ±√(1 − 2x)", lambda x, y: y * y == 1 - 2 * x),
        ("36 x² = 8 − y²", lambda x, y: x * x == 8 - y * y),
        ("37 x = y²", lambda x, y: x == y * y),
        ("38 x + y² = 1", lambda x, y: x + y * y == 1),
        ("39 y = (3x − 1)/(x + 2)", lambda x, y: x != -2 and y == (3 * x - 1) / (x + 2)),
        ("40 y = ∛x", lambda x, y: y ** 3 == x),
        ("41 x² − 4y² = 1", lambda x, y: x * x - 4 * y * y == 1),
        ("42 |y| = 2x + 3", lambda x, y: abs(y) == 2 * x + 3),
    ]
    for name, eq in eqs:
        bad = next(((x, solutions(eq, x)) for x in grid if len(solutions(eq, x)) > 1), None)
        if bad is None:
            print(f"     {name:<24} every x on the grid has at most one y: a function of x")
        else:
            x, ys = bad
            print(f"     {name:<24} x = {x} has y ∈ {{{', '.join(str(y) for y in sorted(ys))}}}: not a function of x")
    print("     The grid is quarter-integers from −4 to 4; a second y refutes, a single y on")
    print("     the grid is evidence, and the solutions say why it holds for every real x.")
    print()

    print("S3   SULLIVAN 2.1, EXAMPLE 9 AND PROBLEMS 51 TO 58: THE DOMAIN OF f DEFINED BY AN EQUATION")

    def exists(f, x):
        try:
            v = f(x)
        except ZeroDivisionError:
            return False
        except ValueError:
            return False
        return v is not None

    def root(q):
        if q < 0:
            raise ValueError
        return q  # only its existence matters here

    cases = [
        ("9(a) x² + 5x", lambda x: x * x + 5 * x, lambda x: True, "all reals"),
        ("9(b) 3x/(x² − 4)", lambda x: 3 * x / (x * x - 4), lambda x: x not in (-2, 2), "x ≠ −2, x ≠ 2"),
        ("9(c) √(4 − 3t)", lambda t: root(4 - 3 * t), lambda t: t <= Fr(4, 3), "t ≤ 4/3"),
        ("9(d) √(3x + 12)/(x − 5)", lambda x: root(3 * x + 12) / (x - 5), lambda x: x >= -4 and x != 5, "x ≥ −4, x ≠ 5"),
        ("51 x² + 2", lambda x: x * x + 2, lambda x: True, "all reals"),
        ("52 −5x + 4", lambda x: -5 * x + 4, lambda x: True, "all reals"),
        ("53 x²/(x² + 1)", lambda x: x * x / (x * x + 1), lambda x: True, "all reals: x² + 1 > 0"),
        ("54 (x + 1)/(2x² + 8)", lambda x: (x + 1) / (2 * x * x + 8), lambda x: True, "all reals: 2x² + 8 > 0"),
        ("55 x/(x² − 16)", lambda x: x / (x * x - 16), lambda x: x not in (-4, 4), "x ≠ −4, x ≠ 4"),
        ("56 2x/(x² − 4)", lambda x: 2 * x / (x * x - 4), lambda x: x not in (-2, 2), "x ≠ −2, x ≠ 2"),
        ("57 (x + 4)/(x³ − 4x)", lambda x: (x + 4) / (x ** 3 - 4 * x), lambda x: x not in (-2, 0, 2), "x ≠ −2, 0, 2"),
        ("58 (x − 2)/(x³ + x)", lambda x: (x - 2) / (x ** 3 + x), lambda x: x != 0, "x ≠ 0: x² + 1 > 0"),
    ]
    probe = [Fr(k, 3) for k in range(-18, 19)] + [Fr(-4), Fr(4, 3), Fr(5)]
    for name, f, claimed, words in cases:
        agree = all(exists(f, x) == claimed(x) for x in probe)
        excluded = sorted({x for x in probe if not exists(f, x)})
        shown = ", ".join(str(x) for x in excluded) if excluded else "none"
        print(f"     {name:<26} {words:<24} f(x) exists iff claimed, on {len(probe)} points: {agree}   excluded: {shown}")
    print("     Two reasons only, as the book's box says: a zero denominator and a negative radicand.")


def is_square(q: Fr) -> bool:
    n, d = q.numerator, q.denominator
    return n >= 0 and int(n ** 0.5 + 0.5) ** 2 == n and int(d ** 0.5 + 0.5) ** 2 == d


if __name__ == "__main__":
    main()
