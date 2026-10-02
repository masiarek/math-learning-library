#!/usr/bin/env python3
"""A relation is a set of pairs, a function is a relation with one property, a graph is a relation drawn.

Run:  python3 relations_and_functions.py

Everything here is a set of ordered pairs. 'Divides' on {1, ..., 6} is
one; its domain and range are read off the pairs; 'is a function' is a
property a set of pairs has or lacks; composition is a product of
relations; a graph is a relation drawn as arrows. The program builds each
object as a Python set of tuples and checks the textbook claims on every
relation over a small base set, where the check is a proof.
"""

from itertools import product

BASE = (1, 2, 3)
PAIRS = [(x, y) for x in BASE for y in BASE]
RELATIONS = [frozenset(p for p, keep in zip(PAIRS, bits) if keep) for bits in product((True, False), repeat=9)]
TWO = [(x, y) for x in (1, 2) for y in (1, 2)]
RELATIONS2 = [frozenset(p for p, keep in zip(TWO, bits) if keep) for bits in product((True, False), repeat=4)]


def dom(r):
    return {x for x, y in r}


def ran(r):
    return {y for x, y in r}


def inverse(r):
    return frozenset((y, x) for x, y in r)


def compose(r, s):
    """The relation product ρσ of Simovici and Djeraba: first ρ, then σ.
    Jech and Kunen write the same thing as σ ∘ ρ."""
    return frozenset((x, z) for x, y in r for y2, z in s if y == y2)


def is_function(r):
    """Jech, Kunen, Simovici: (x, y) ∈ f and (x, z) ∈ f imply y = z."""
    return all(y == z for x, y in r for x2, z in r if x == x2)


def one_to_one(r):
    return all(x == x2 for x, y in r for x2, y2 in r if y == y2)


def show(r):
    return "{" + ", ".join(f"({x}, {y})" for x, y in sorted(r)) + "}" if r else "∅"


def main() -> None:
    print("1. A RELATION IS A SET OF ORDERED PAIRS")
    six = range(1, 7)
    divides = frozenset((m, n) for m in six for n in six if n % m == 0)
    print(f"   'm divides n' on {{1, ..., 6}} is the set of {len(divides)} pairs")
    print("   " + show(divides))
    print(f"   2 divides 6?  (2, 6) ∈ δ: {(2, 6) in divides}     4 divides 6?  (4, 6) ∈ δ: {(4, 6) in divides}")
    print(f"   dom(δ) = {sorted(dom(divides))}   ran(δ) = {sorted(ran(divides))}")
    print("   'x ρ y' is just a way of writing (x, y) ∈ ρ; the relation IS the set.")
    print()

    print("2. A FUNCTION IS A RELATION WITH ONE PROPERTY")
    sq = frozenset((x, x * x) for x in range(-3, 4))
    root = inverse(sq)
    print(f"   square = {show(sq)}")
    print(f"   is a function: {is_function(sq)}   (each x has one square)")
    print(f"   root = square⁻¹ = {show(root)}")
    print(f"   is a function: {is_function(root)}   (4 has partners 2 and -2)")
    print("   f(x) means 'the unique y with (x, y) ∈ f'; a Python dict is the same")
    print(f"   object:  dict(square) = {dict(sorted(sq))}")
    print()

    print("3. FUNCTIONS, ONE-TO-ONE RELATIONS, INVERSES: EVERY RELATION ON {1, 2, 3}")
    funcs = [r for r in RELATIONS if is_function(r)]
    total = [r for r in funcs if dom(r) == set(BASE)]
    inj = [r for r in total if one_to_one(r)]
    sur = [r for r in total if ran(r) == set(BASE)]
    bij = [r for r in inj if ran(r) == set(BASE)]
    print(f"   relations on {{1, 2, 3}}: {len(RELATIONS)}   functions (partial): {len(funcs)}   with domain all of {{1, 2, 3}}: {len(total)} = 3^3")
    print(f"   injections: {len(inj)}   surjections: {len(sur)}   bijections: {len(bij)} = 3!   (on a finite set, injective = surjective = bijective: {inj == sur})")
    thm = all(is_function(r) == one_to_one(inverse(r)) for r in RELATIONS)
    print(f"   ρ is a function  iff  ρ⁻¹ is one-to-one, all {len(RELATIONS)} relations: {thm}   (Simovici–Djeraba, Theorem 1.37)")
    inv = all(inverse(inverse(r)) == r and dom(inverse(r)) == ran(r) for r in RELATIONS)
    print(f"   (ρ⁻¹)⁻¹ = ρ and dom(ρ⁻¹) = ran(ρ): {inv}")
    print()

    print("4. COMPOSITION IS A PRODUCT OF RELATIONS")
    r = frozenset({(1, 2), (2, 3)})
    s = frozenset({(2, 10), (3, 20)})
    print(f"   ρ = {show(r)}, σ = {show(s)}:  ρσ = {show(compose(r, s))}   ('first ρ, then σ')")
    assoc = all(compose(compose(a, b), c) == compose(a, compose(b, c)) for a in RELATIONS2 for b in RELATIONS2 for c in RELATIONS2)
    invp = all(inverse(compose(a, b)) == compose(inverse(b), inverse(a)) for a in RELATIONS2 for b in RELATIONS2)
    fn = all((not (is_function(a) and is_function(b))) or is_function(compose(a, b)) for a in RELATIONS2 for b in RELATIONS2)
    print(f"   on all {len(RELATIONS2)} relations on {{1, 2}}:  (ρσ)τ = ρ(στ): {assoc}   (ρσ)⁻¹ = σ⁻¹ρ⁻¹: {invp}   product of functions is a function: {fn}")
    print("   Jech and Kunen write σ ∘ ρ for Simovici's ρσ: same set, letters swapped.")
    print()

    print("5. A GRAPH IS A RELATION DRAWN AS ARROWS")
    likes = frozenset({("a", "a"), ("b", "c"), ("c", "b"), ("d", "c")})
    print(f"   'x likes y' from the quantifiers lesson: {show(likes)}")
    for x in "abcd":
        out = sorted(y for x2, y in likes if x2 == x)
        print(f"     {x} → {', '.join(out) if out else '(nobody)'}")
    sym = likes == inverse(likes)
    print(f"   symmetric (an undirected graph): {sym};  an undirected graph is a relation equal to its inverse,")
    print("   or a set of two-element sets {x, y}. A membership table x ∈ y is a directed graph too:")
    print("   Kunen's Exercise I.2.1 draws seven of them, and the axiom katas page evaluates the axioms on each.")
    print()

    print("6. A FUNCTION IS ITS PAIRS, NOT ITS FORMULA")
    f = frozenset((x, x * x) for x in range(-2, 3))
    g = frozenset((x, abs(x) ** 2) for x in range(-2, 3))
    h = frozenset((x, (x * x) % 7) for x in range(-2, 3))
    print(f"   y = x² and y = |x|² on {{-2, ..., 2}}: same set of pairs: {f == g}   so one function, by extensionality")
    print(f"   y = x² and y = x² mod 7 on {{-2, ..., 2}}: {f == h}   (they differ nowhere here) ")
    print("   Two formulas that agree on every input define one function; a function")
    print("   is the table of its values, which is why a table in a database is one.")


if __name__ == "__main__":
    main()
