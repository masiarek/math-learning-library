#!/usr/bin/env python3
"""Subsets inherit the laws: why a subspace needs three checks, not eight.

Run:  python3 subsets_inherit_the_laws.py

A vector space must pass eight conditions. A subset U of a vector space V needs
only three: 0 is in U, and U is closed under addition and under scalar
multiplication. The other laws are "for all" equations, already true for every
vector of V, so they are true for the vectors in U with nothing to check. The
only thing that can go wrong is an answer landing outside U.

The program runs the eight equations and the three conditions on five subsets
of R^2. The equations pass on every one of them, subspace or not; only the
closure conditions tell them apart. Then it shows where the two "there exists"
axioms come from, and why the same test for a group needs a fourth condition.

Exact fractions throughout. A sample can refute a condition but not prove one;
the page proves the passing ones.
"""

from fractions import Fraction as Q
from itertools import product

SCALARS = [Q(-2), Q(-1), Q(0), Q(1, 2), Q(3)]
ZERO = (Q(0), Q(0))


def add(u, v):
    return (u[0] + v[0], u[1] + v[1])


def smul(a, v):
    return (a * v[0], a * v[1])


def neg(v):
    return (-v[0], -v[1])


def show(v):
    return f"({v[0]}, {v[1]})"


def scaled(a, v):
    return (f"({a})" if a < 0 else f"{a}") + show(v)


def equations_hold(xs):
    """The eight vector-space conditions, computed with the arithmetic of R^2."""
    ok = all(add(u, v) == add(v, u) for u, v in product(xs, repeat=2))
    ok &= all(add(add(u, v), w) == add(u, add(v, w)) for u, v, w in product(xs, repeat=3))
    ok &= all(smul(a * b, v) == smul(a, smul(b, v)) for a, b, v in product(SCALARS, SCALARS, xs))
    ok &= all(add(v, ZERO) == v and add(v, neg(v)) == ZERO and smul(1, v) == v for v in xs)
    ok &= all(smul(a, add(u, v)) == add(smul(a, u), smul(a, v)) for a, u, v in product(SCALARS, xs, xs))
    ok &= all(smul(a + b, v) == add(smul(a, v), smul(b, v)) for a, b, v in product(SCALARS, SCALARS, xs))
    return ok


def closure_witnesses(xs, inside):
    """The three conditions for a subspace, each with a witness if it fails."""
    out = {}
    if not inside(ZERO):
        out["0 in U"] = "(0, 0) is not in U"
    for u, w in product(xs, repeat=2):
        if not inside(add(u, w)):
            out.setdefault("addition", f"{show(u)} + {show(w)} = {show(add(u, w))} is outside U")
    for a, u in product(SCALARS, xs):
        if not inside(smul(a, u)):
            out.setdefault("scalar multiplication", f"{scaled(a, u)} = {show(smul(a, u))} is outside U")
    return out


P = lambda x, y: (Q(x), Q(y))

SUBSETS = [
    ("the line y = 2x", [P(1, 2), P(-3, -6), P(Q(1, 2), 1)], lambda v: v[1] == 2 * v[0]),
    ("just the origin {(0, 0)}", [P(0, 0)], lambda v: v == ZERO),
    ("the half-plane x >= 0", [P(1, 2), P(3, -1), P(0, 5)], lambda v: v[0] >= 0),
    ("the line y = 2x + 1", [P(0, 1), P(1, 3), P(-1, -1)], lambda v: v[1] == 2 * v[0] + 1),
    ("the two axes together", [P(1, 0), P(0, 1), P(-2, 0)], lambda v: v[0] == 0 or v[1] == 0),
]


def main() -> None:
    print("1. THREE CONDITIONS INSTEAD OF EIGHT")
    print("   U, a subset of a vector space V, is a subspace when:")
    print("     additive identity                    0 is in U")
    print("     closed under addition                u, w in U  implies  u + w in U")
    print("     closed under scalar multiplication   a a scalar, u in U  implies  au in U")
    print()

    print("2. FIVE SUBSETS OF R^2")
    print(f"   {'subset U':26} {'8 equations':>11}   3 conditions")
    for name, xs, inside in SUBSETS:
        assert all(inside(v) for v in xs), name
        eq = "hold" if equations_hold(xs) else "FAIL"
        bad = closure_witnesses(xs, inside)
        print(f"   {name:26} {eq:>11}   {'a subspace' if not bad else 'not a subspace'}")
        for law, text in bad.items():
            print(f"       {law + ':':23}{text}")
    print("   The eight equations hold on every sample of every subset, because they")
    print("   are computed with the arithmetic of R^2. They cannot tell a subspace from")
    print("   a subset that is not one. Only the closure conditions can.")
    print()

    print("3. WHERE THE TWO 'THERE EXISTS' AXIOMS COME FROM")
    print("   Six of the eight say 'for all': true for every vector of R^2, so true for")
    print("   every vector of U. Two say 'there exists', and the witness must be IN U:")
    print("     additive identity:  0 must be in U                -> condition 1")
    print("     additive inverse:   -u must be in U, for each u   -> (-1)u = -u, and")
    print("                         U is closed under scalar multiplication")
    for name, xs, inside in SUBSETS[:1] + SUBSETS[2:3]:
        u = xs[0]
        m = smul(-1, u)
        print(f"   {name}:  -{show(u)} = {scaled(-1, u)} = {show(m)},  in U: {inside(m)}")
    print("   The inverse of (1, 2) exists in R^2 either way. In the half-plane it is")
    print("   outside U, so U has no inverse for (1, 2) of its own.")
    print()

    print("4. THE SAME TEST FOR A GROUP NEEDS A FOURTH CONDITION")
    ints = range(-6, 7)
    groups = [
        ("multiples of 3", lambda n: n % 3 == 0),
        ("natural numbers 0, 1, 2, ...", lambda n: n >= 0),
    ]
    print(f"   {'subset U of the integers':30} {'0 in U':>6} {'closed under +':>15} {'closed under -':>15}")
    for name, inside in groups:
        xs = [n for n in ints if inside(n)]
        has0 = inside(0)
        plus = all(inside(a + b) for a, b in product(xs, repeat=2))
        bad_neg = next((a for a in xs if not inside(-a)), None)
        yn = lambda ok: "yes" if ok else "no"
        verdict = "a subgroup" if has0 and plus and bad_neg is None else "not a subgroup"
        print(f"   {name:30} {yn(has0):>6} {yn(plus):>15} {yn(bad_neg is None):>15}   {verdict}")
        if bad_neg is not None:
            print(f"       the inverse of {bad_neg} is {-bad_neg}, which is outside U")
    print("   A vector space gets inverses from the scalar -1. A group has no scalars,")
    print("   so its subgroup test has to ask for inverses separately.")


if __name__ == "__main__":
    main()
