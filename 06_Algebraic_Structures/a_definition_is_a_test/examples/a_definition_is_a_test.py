#!/usr/bin/env python3
"""A definition is a test: the vector-space axioms, run against five candidates.

Run:  python3 a_definition_is_a_test.py

A school book states a + b = b + a as a fact about the integers. Axler's
Linear Algebra Done Right, definition 1.20, states u + v = v + u as a condition:
any set with an addition and a scalar multiplication that meets all of its
conditions is called a vector space. The same sentence has become a test.

The program writes the test once and runs it on five candidates. Two pass that
look nothing like arrows: functions, and the positive numbers with "addition"
meaning multiplication. Then it takes two theorems that are proved once, from
the axioms alone, and shows what they say in each space that passed, where
nobody had to prove them again. Last, it shows what happens to a theorem in a
space that fails one axiom.

Exact fractions throughout, except in the one candidate that is floats on
purpose. A sample can refute an axiom but cannot prove one; the page says why
the passing candidates pass everywhere.
"""

from fractions import Fraction as Q
from itertools import product

SCALARS = [Q(-2), Q(-1), Q(0), Q(1), Q(3)]


class Space:
    """A candidate: a set, an addition, a scalar multiplication, a zero, a negation."""

    def __init__(self, name, means, samples, add, smul, zero, neg, show):
        self.name, self.means, self.samples = name, means, samples
        self.add, self.smul, self.zero, self.neg, self.show = add, smul, zero, neg, show


def scaled(a, V, v):
    """Axler's notation for a times v: 3(1, 2), (-1)(1/3, 2), 0(2)."""
    head = f"({a})" if a < 0 else f"{a}"
    body = V.show(v)
    return head + (body if body[0] in "({" else f"({body})")


def failures(V: Space):
    """Axler 1.20, written once. Each failure comes with the values that break it."""
    add, smul, show, out = V.add, V.smul, V.show, {}

    def fail(law, where, left, right):
        out.setdefault(law, [where, left, right])

    for u, v in product(V.samples, repeat=2):
        if add(u, v) != add(v, u):
            fail("commutativity", f"u = {show(u)}, v = {show(v)}",
                 f"u + v = {show(add(u, v))}", f"v + u = {show(add(v, u))}")
    for u, v, w in product(V.samples, repeat=3):
        left, right = add(add(u, v), w), add(u, add(v, w))
        if left != right:
            fail("associativity", f"u = {show(u)}, v = {show(v)}, w = {show(w)}",
                 f"(u + v) + w = {show(left)}", f"u + (v + w) = {show(right)}")
    for a, b, v in product(SCALARS, SCALARS, V.samples):
        if smul(a * b, v) != smul(a, smul(b, v)):
            fail("associativity", f"a = {a}, b = {b}, v = {show(v)}",
                 f"(ab)v = {show(smul(a * b, v))}", f"a(bv) = {show(smul(a, smul(b, v)))}")
    for v in V.samples:
        if add(v, V.zero) != v:
            fail("additive identity", f"v = {show(v)}", f"v + 0 = {show(add(v, V.zero))}", "")
        if add(v, V.neg(v)) != V.zero:
            fail("additive inverse", f"v = {show(v)}", f"v + (-v) = {show(add(v, V.neg(v)))}", "")
        if smul(1, v) != v:
            fail("multiplicative identity", f"v = {show(v)}", f"1v = {show(smul(1, v))}", "")
    for a, u, v in product(SCALARS, V.samples, V.samples):
        left, right = smul(a, add(u, v)), add(smul(a, u), smul(a, v))
        if left != right:
            fail("distributive", f"a = {a}, u = {show(u)}, v = {show(v)}",
                 f"a(u + v) = {show(left)}", f"au + av   = {show(right)}")
    for a, b, v in product(SCALARS, SCALARS, V.samples):
        left, right = smul(a + b, v), add(smul(a, v), smul(b, v))
        if left != right:
            fail("distributive", f"a = {a}, b = {b}, v = {show(v)}",
                 f"(a + b)v = {show(left)}", f"av + bv  = {show(right)}")
    return out


# ---- five candidates --------------------------------------------------------

def pair_add(u, v):
    return (u[0] + v[0], u[1] + v[1])


def pair_smul(a, v):
    return (a * v[0], a * v[1])


def pair_neg(v):
    return (-v[0], -v[1])


def show_pair(v):
    return f"({v[0]}, {v[1]})"


def show_function(f):
    return "{" + ", ".join(f"{k}: {f[k]}" for k in sorted(f)) + "}"


R2 = Space("R^2", "pairs of numbers, added entry by entry",
           [(Q(1, 3), Q(2)), (Q(-5), Q(1, 7)), (Q(0), Q(-1))],
           pair_add, pair_smul, (Q(0), Q(0)), pair_neg, show_pair)

FUNCTIONS = Space("functions {a, b, c} -> Q", "(f + g)(x) = f(x) + g(x),  (af)(x) = a f(x)",
                  [{"a": Q(1), "b": Q(-2), "c": Q(1, 2)}, {"a": Q(0), "b": Q(3), "c": Q(-1)},
                   {"a": Q(2, 5), "b": Q(0), "c": Q(0)}],
                  lambda f, g: {k: f[k] + g[k] for k in f},
                  lambda a, f: {k: a * f[k] for k in f},
                  {"a": Q(0), "b": Q(0), "c": Q(0)},
                  lambda f: {k: -f[k] for k in f}, show_function)

POSITIVE = Space("positive numbers", "'u + v' is u*v,  'av' is v**a,  the zero is 1",
                 [Q(2), Q(3, 5), Q(7)],
                 lambda u, v: u * v, lambda a, v: v ** int(a), Q(1), lambda v: 1 / v, str)

FLOATS = Space("R^2 in floats", "pairs of floats, added entry by entry",
               [(0.1, 0.2), (0.2, 0.3), (0.3, 0.1)],
               pair_add, pair_smul, (0.0, 0.0), pair_neg, show_pair)

FLATTENED = Space("R^2, a(x, y) = (ax, 0)", "the usual addition, a scalar product that drops y",
                  [(Q(1), Q(2)), (Q(3), Q(-1)), (Q(0), Q(5))],
                  pair_add, lambda a, v: (a * v[0], Q(0)), (Q(0), Q(0)), pair_neg, show_pair)

CANDIDATES = [R2, FUNCTIONS, POSITIVE, FLOATS, FLATTENED]


def main() -> None:
    print("1. THE DEFINITION, WRITTEN ONCE AS A CHECK")
    print("   commutativity            u + v = v + u")
    print("   associativity            (u + v) + w = u + (v + w)   and   (ab)v = a(bv)")
    print("   additive identity        some 0 has v + 0 = v")
    print("   additive inverse         every v has a w with v + w = 0")
    print("   multiplicative identity  1v = v")
    print("   distributive             a(u + v) = au + av          and   (a + b)v = av + bv")
    print(f"   Scalars tried: {', '.join(str(a) for a in SCALARS)}")
    print()

    print("2. FIVE CANDIDATES, ONE TEST")
    passed = []
    for V in CANDIDATES:
        bad = failures(V)
        verdict = "a vector space" if not bad else "fails " + ", ".join(bad)
        print(f"   {V.name:26} {verdict}")
        print(f"   {'':26} ({V.means})")
        for law, (where, left, right) in bad.items():
            print(f"     {law}, at {where}:")
            for line in (left, right):
                if line:
                    print(f"       {line}")
        if not bad:
            passed.append(V)
    print()

    print("3. PROVED ONCE: 0v = 0 IN EVERY VECTOR SPACE")
    print("   Proof, from the axioms only:  0v = (0 + 0)v = 0v + 0v;  add -(0v) to both sides.")
    for V in passed:
        v = V.samples[0]
        print(f"   {V.name:26} {scaled(0, V, v)} = {V.show(V.smul(0, v))}")
        print(f"   {'':26} is that the zero vector of this space?  {V.smul(0, v) == V.zero}")
    print("   In the positive numbers the zero vector is 1, so the theorem says")
    print("   2**0 = 1. Once the exponent laws hold, x**0 = 1 is forced, by the same")
    print("   proof as 0v = 0, and nobody has to prove it a second time.")
    print()

    print("4. PROVED ONCE: (-1)v = -v IN EVERY VECTOR SPACE")
    print("   Proof:  v + (-1)v = 1v + (-1)v = (1 + (-1))v = 0v = 0,  and inverses are unique.")
    for V in passed:
        v = V.samples[0]
        print(f"   {V.name:26} {scaled(-1, V, v)} = {V.show(V.smul(-1, v))}")
        print(f"   {'':26} is that -v, the additive inverse?  {V.smul(-1, v) == V.neg(v)}")
    print("   In the positive numbers the inverse of 2 is 1/2, because 2 'plus' 1/2")
    print("   is 2 * 1/2 = 1, the zero. So the theorem says 2**-1 = 1/2.")
    print()

    print("5. FAIL ONE AXIOM, LOSE THE THEOREMS THAT USE IT")
    v = FLATTENED.samples[0]
    minus = FLATTENED.smul(-1, v)
    print(f"   {FLATTENED.name}:  multiplicative identity fails, {scaled(1, FLATTENED, v)}"
          f" = {show_pair(FLATTENED.smul(1, v))}")
    print(f"     {scaled(-1, FLATTENED, v)} = {show_pair(minus)},  but -{show_pair(v)} = {show_pair(pair_neg(v))}")
    print(f"     {show_pair(v)} + {show_pair(minus)} = {show_pair(pair_add(v, minus))}, not (0, 0)")
    print("     The proof in section 4 began with v = 1v. Here that step is false,")
    print("     and so is the theorem.")
    u, w = FLOATS.samples[0], FLOATS.samples[1]
    back = pair_add(pair_add(u, w), pair_neg(w))
    print(f"   {FLOATS.name}:  associativity fails, so cancellation (u + v) - v = u is unproved")
    print(f"     ({show_pair(u)} + {show_pair(w)}) - {show_pair(w)} = {show_pair(back)}")
    print(f"     not {show_pair(u)}")
    zero_ok = all(pair_smul(0, x) == FLOATS.zero for x in FLOATS.samples)
    neg_ok = all(pair_smul(-1, x) == pair_neg(x) for x in FLOATS.samples)
    print(f"     0v = 0 on these samples: {zero_ok};  (-1)v = -v: {neg_ok}")
    print("     Those two survive, but not because of the proofs: multiplying a float")
    print("     by 0 or -1 happens to be exact. A failed axiom does not make every")
    print("     theorem false. It makes every theorem that used it unproved.")

if __name__ == "__main__":
    main()
