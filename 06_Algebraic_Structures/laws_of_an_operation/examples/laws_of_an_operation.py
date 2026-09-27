#!/usr/bin/env python3
"""The laws of an operation: the same four, in every book, on every set.

Run:  python3 laws_of_an_operation.py

A school book lists a + b = b + a for the integers. A linear-algebra book lists
u + v = v + u for vectors, and again for products of linear maps, minus the
commutativity. It is one short list every time: an operation can be
commutative, associative, have an identity, and have inverses. The names
semigroup, monoid and group are only which of the four hold.

The program writes the four checks once and runs them on ten sets. Where a law
fails it prints the witness, the actual values that break it, because the
missing law is the only news in any book's list. Then it adds a second
operation and one more law, distributivity, which is what the names ring and
field add.

A sample can refute a law but cannot prove one. Every "yes" below is a theorem
about the whole set, proved in the book that defines it; the program only shows
that nothing in the samples contradicts it. Section 4 shows a sample getting
it wrong.
"""

from fractions import Fraction as Q
from itertools import product


# ---- the four laws, written once --------------------------------------------

def comm_witness(xs, op):
    """A pair with a.b != b.a, or None."""
    return next(((a, b) for a, b in product(xs, repeat=2) if op(a, b) != op(b, a)), None)


def assoc_witness(xs, op):
    """A triple with (a.b).c != a.(b.c), or None."""
    return next(((a, b, c) for a, b, c in product(xs, repeat=3)
                 if op(op(a, b), c) != op(a, op(b, c))), None)


def ident_witness(xs, op, e):
    """An a with a.e != a or e.a != a, or None. e is the identity the book names."""
    return next((a for a in xs if not (op(a, e) == a == op(e, a))), None)


def inverse_witness(xs, op, e):
    """An a with no b among the samples such that a.b = b.a = e, or None."""
    return next((a for a in xs if not any(op(a, b) == e == op(b, a) for b in xs)), None)


NO_IDENTITY = object()   # marks "no identity at all", so inverses mean nothing


def verdicts(xs, op, e):
    c, a = comm_witness(xs, op), assoc_witness(xs, op)
    i = NO_IDENTITY if e is None else ident_witness(xs, op, e)
    v = NO_IDENTITY if i is not None else inverse_witness(xs, op, e)
    return c, a, i, v


def name(c, a, i, v):
    if a is not None:
        return "no name: not even associative"
    kind = "group" if v is None else "monoid" if i is None else "semigroup"
    return ("commutative " if c is None else "") + kind


# ---- ten sets, each with one operation --------------------------------------

def mat(a, b, c, d):
    return ((a, b), (c, d))


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def matadd(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(2)) for i in range(2))


def show_mat(A):
    return f"[[{A[0][0]}, {A[0][1]}], [{A[1][0]}, {A[1][1]}]]"


def cmul(z, w):
    """Complex multiplication, the pair rule of 03_Complex_Numbers."""
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + w[0] * z[1])


def show_pair(z):
    return f"({z[0]}, {z[1]})"


I2 = mat(1, 0, 0, 1)
R = mat(0, -1, 1, 0)        # quarter turn
R_INV = mat(0, 1, -1, 0)
S = mat(1, 1, 0, 1)         # shear
S_INV = mat(1, -1, 0, 1)

INTS = [1, 2, 3, 0, -1, -2, -3]

# name, samples, operation, symbol, identity the book names (None: no identity),
# and how to print one member.
ROWS = [
    ("integers, +", INTS, lambda a, b: a + b, "+", 0, str),
    ("vectors in R^2, +", [(1, 2), (0, 0), (-1, -2), (3, 0), (-3, 0)],
        lambda u, v: (u[0] + v[0], u[1] + v[1]), "+", (0, 0), show_pair),
    ("integers, x", INTS, lambda a, b: a * b, "x", 1, str),
    ("fractions except 0, x", [Q(1), Q(2), Q(1, 2), Q(-1), Q(-3), Q(-1, 3)],
        lambda a, b: a * b, "x", Q(1), str),
    ("fourth roots of unity, x", [(1, 0), (0, 1), (-1, 0), (0, -1)], cmul, "x", (1, 0), show_pair),
    ("integers, -", INTS, lambda a, b: a - b, "-", 0, str),
    ("integers, max", INTS, max, "max", None, str),
    ("strings, concatenation", ["ab", "c", ""], lambda s, t: s + t, "+", "", repr),
    ("invertible 2x2 matrices, x", [I2, R, R_INV, S, S_INV], matmul, "x", I2, show_mat),
    ("floats, +", [0.1, 0.2, 0.3, 0.0, -0.1, -0.2, -0.3], lambda a, b: a + b, "+", 0.0, repr),
]


def expr(a, sym, b, show):
    return f"max({show(a)}, {show(b)})" if sym == "max" else f"{show(a)} {sym} {show(b)}"


def main() -> None:
    print("1. FOUR LAWS, ONE OPERATION")
    print("   commutative   a.b = b.a")
    print("   associative   (a.b).c = a.(b.c)")
    print("   identity      there is an e with a.e = e.a = a for every a")
    print("   inverses      every a has a b with a.b = b.a = e")
    print("   Every book's list of 'rules' is these four, for its own set and its own '.'.")
    print()

    print("2. TEN SETS, ONE CHECK")
    print(f"   {'set, operation':28} {'comm':>5} {'assoc':>6} {'ident':>6} {'inv':>5}   the name for that combination")
    mark = lambda w: "yes" if w is None else " - "
    results = []
    for row in ROWS:
        label, xs, op, sym, e, show = row
        v = verdicts(xs, op, e)
        results.append((row, v))
        print(f"   {label:28} {mark(v[0]):>5} {mark(v[1]):>6} {mark(v[2]):>6} {mark(v[3]):>5}   {name(*v)}")
    print("   The integers under + and the vectors under + fill the same row: the")
    print("   school book and the linear-algebra book are listing the same four laws.")
    print()

    print("3. THE MISSING LAW IS THE NEWS: A WITNESS FOR EVERY '-'")
    for (label, xs, op, sym, e, show), (c, a, i, v) in results:
        if (c, a, i, v) == (None, None, None, None):
            continue
        print(f"   {label}")
        if c is not None:
            x, y = c
            print(f"     not commutative:  {expr(x, sym, y, show)} = {show(op(x, y))}")
            print(f"                       {expr(y, sym, x, show)} = {show(op(y, x))}")
        if a is not None:
            x, y, z = a
            left, right = op(op(x, y), z), op(x, op(y, z))
            print(f"     not associative:  ({expr(x, sym, y, show)}) {sym} {show(z)} = {show(left)}")
            print(f"                       {show(x)} {sym} ({expr(y, sym, z, show)}) = {show(right)}")
        if i is NO_IDENTITY:
            print("     no identity:      see section 4")
        elif i is not None:
            print(f"     no identity:      {expr(i, sym, e, show)} = {show(op(i, e))},"
                  f"  but {expr(e, sym, i, show)} = {show(op(e, i))}")
        if v is NO_IDENTITY:
            print("     no inverses:      with no identity there is nothing to get back to")
        elif v is not None:
            print(f"     no inverses:      nothing {sym} {show(v)} gives {show(e)}")
    print()

    print("4. A SAMPLE CAN REFUTE A LAW, NOT PROVE ONE")
    looks_like = [e for e in INTS if all(max(a, e) == a for a in INTS)]
    e = looks_like[0]
    print(f"   integers, max, on the samples {INTS}:")
    print(f"     members that act as an identity on every sample: {looks_like}")
    print(f"     but max({e}, {e - 1}) = {max(e, e - 1)}, not {e - 1}")
    print("   An identity for max would have to be at most every integer, and no")
    print("   integer is. The smallest sample passed only because nothing smaller")
    print("   was tried. That is why every 'yes' above is a theorem about the")
    print("   whole set, and every '-' is a witness you can check by hand.")
    print()

    print("5. TWO OPERATIONS, AND THE LAW THAT LINKS THEM")
    print("   distributive  a x (b + c) = a x b + a x c,  and  (a + b) x c = a x c + b x c")
    P = mat(1, 0, 0, 0)
    rings = [
        ("integers", [0, 1, -1, 2, -2, 3, -3], lambda a, b: a + b, lambda a, b: a * b, 0, 1, str),
        ("fractions", [Q(0), Q(1), Q(-1), Q(2), Q(-2), Q(1, 2), Q(-1, 2)],
            lambda a, b: a + b, lambda a, b: a * b, Q(0), Q(1), str),
        ("2x2 matrices", [mat(0, 0, 0, 0), I2, mat(-1, 0, 0, -1), R, R_INV, P, mat(-1, 0, 0, 0)],
            matadd, matmul, mat(0, 0, 0, 0), I2, show_mat),
        ("floats", [0.0, 0.1, -0.1, 0.2, -0.2, 0.3, -0.3],
            lambda a, b: a + b, lambda a, b: a * b, 0.0, 1.0, repr),
    ]
    print(f"   {'set':14} {'+ comm. group':>13} {'x assoc, ident':>15} {'distrib':>8}"
          f" {'x comm':>7} {'x inverses':>11}   name")
    notes = []
    for label, xs, add, mul, zero, one, show in rings:
        plus_group = verdicts(xs, add, zero) == (None, None, None, None)
        m_assoc, m_ident = assoc_witness(xs, mul), ident_witness(xs, mul, one)
        d = next(((a, b, c) for a, b, c in product(xs, repeat=3)
                  if mul(a, add(b, c)) != add(mul(a, b), mul(a, c))), None)
        ring = plus_group and m_assoc is None and m_ident is None and d is None
        yn = lambda ok: "yes" if ok else "-"
        if ring:
            m_comm = comm_witness(xs, mul)
            m_inv = inverse_witness([x for x in xs if x != zero], mul, one)
            called = "field" if m_comm is None and m_inv is None else \
                     "commutative ring" if m_comm is None else "ring"
            tail = f" {yn(m_comm is None):>7} {yn(m_inv is None):>11}   {called}"
            if m_comm is not None:
                x, y = m_comm
                notes.append(f"{label}: {show(x)} x {show(y)} = {show(mul(x, y))}")
                notes.append(f"{'':{len(label)}}  {show(y)} x {show(x)} = {show(mul(y, x))}")
            if m_inv is not None:
                notes.append(f"{label}: nothing x {show(m_inv)} gives {show(one)}")
        else:
            tail = f" {'':>7} {'':>11}   none: not a ring"
            if not plus_group:
                notes.append(f"{label}: + is not associative (section 3)")
            if m_assoc is not None:
                x, y, z = m_assoc
                notes.append(f"{label}: ({show(x)} x {show(y)}) x {show(z)} = {show(mul(mul(x, y), z))}")
                notes.append(f"{'':{len(label)}}  {show(x)} x ({show(y)} x {show(z)}) = {show(mul(x, mul(y, z)))}")
            if d is not None:
                x, y, z = d
                notes.append(f"{label}: {show(x)} x ({show(y)} + {show(z)}) = {show(mul(x, add(y, z)))}")
                notes.append(f"{'':{len(label)}}  {show(x)} x {show(y)} + {show(x)} x {show(z)} = {show(add(mul(x, y), mul(x, z)))}")
        print(f"   {label:14} {yn(plus_group):>13} {yn(m_assoc is None and m_ident is None):>15}"
              f" {yn(d is None):>8}{tail}")
    print("   The witnesses:")
    for n in notes:
        print(f"     {n}")
    print("   A field is two rows of section 2, a commutative group under + and")
    print("   another under x once 0 is set aside, joined by distributivity. That")
    print("   is the whole list of field axioms, and the F in 'a vector space over F'.")

if __name__ == "__main__":
    main()
