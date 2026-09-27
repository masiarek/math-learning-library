#!/usr/bin/env python3
"""Maps that keep the laws: linear maps, and the same shape everywhere else.

Run:  python3 maps_that_keep_the_laws.py

Axler defines a linear map by two equations, T(u + v) = Tu + Tv and
T(av) = aTv: the map carries the operations of one space over to the other.
The same shape turns up far outside linear algebra: len(s + t) = len(s) +
len(t) for strings, det(AB) = det(A) det(B) for matrices, 2**(a + b) =
2**a * 2**b. A map with that shape is a homomorphism, and a homomorphism that
can be undone shows that two sets are one structure written two ways.

Then the laws for products of linear maps: composition is associative and has
an identity for any functions at all, one distributive law needs linearity,
and commutativity is missing.

Exact fractions throughout. The logarithms are taken only of powers of 2, where
they are whole numbers, so they are computed exactly too.
"""

from fractions import Fraction as Q
from itertools import product

SCALARS = [Q(-2), Q(-1), Q(0), Q(1, 2), Q(3)]
WHOLE_SCALARS = [Q(-2), Q(-1), Q(0), Q(1), Q(3)]   # for v**a, which must stay exact


def add(u, v):
    return (u[0] + v[0], u[1] + v[1])


def smul(a, v):
    return (a * v[0], a * v[1])


def show(v):
    if isinstance(v, tuple) and isinstance(v[0], tuple):
        return f"[[{v[0][0]}, {v[0][1]}], [{v[1][0]}, {v[1][1]}]]"
    if isinstance(v, tuple):
        return f"({v[0]}, {v[1]})"
    return repr(v) if isinstance(v, str) else str(v)


def log2(q):
    """log2 of a power of 2, exactly: 8 -> 3, 1/4 -> -2."""
    n, d = q.numerator, q.denominator
    assert n & (n - 1) == 0 and d & (d - 1) == 0, q
    return Q(n.bit_length() - d.bit_length())


def linearity_witnesses(T, xs, add_V, smul_V, add_W, smul_W, scalars=SCALARS):
    """Axler's two conditions for a linear map, each with a witness if it fails."""
    out = []
    u, v = next(((u, v) for u, v in product(xs, repeat=2)
                 if T(add_V(u, v)) != add_W(T(u), T(v))), (None, None))
    if u is not None:
        out.append(f"additivity:   T({show(u)} + {show(v)}) = {show(T(add_V(u, v)))},"
                   f"  but T({show(u)}) + T({show(v)}) = {show(add_W(T(u), T(v)))}")
    a, v = next(((a, v) for a, v in product(scalars, xs)
                 if T(smul_V(a, v)) != smul_W(a, T(v))), (None, None))
    if a is not None:
        out.append(f"homogeneity:  T({a} * {show(v)}) = {show(T(smul_V(a, v)))},"
                   f"  but {a} * T({show(v)}) = {show(smul_W(a, T(v)))}")
    return out


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + w[0] * z[1])


def as_matrix(z):
    """The complex number (x, y) as the matrix [[x, -y], [y, x]]."""
    return ((z[0], -z[1]), (z[1], z[0]))


P = lambda x, y: (Q(x), Q(y))
VECTORS = [P(1, 2), P(3, -1), P(Q(1, 2), 0)]
NUMBERS = [Q(1), Q(-3), Q(2, 5)]
POWERS_OF_2 = [Q(2), Q(8), Q(1, 4)]

turn = lambda v: (-v[1], v[0])            # multiply by i: a quarter turn
flatten = lambda v: (v[0], Q(0))          # project onto the x-axis
shear = lambda v: (v[0] + v[1], v[1])
identity = lambda v: v
plus = lambda f, g: (lambda v: add(f(v), g(v)))
after = lambda f, g: (lambda v: f(g(v)))  # f after g, Axler's product fg


def same(f, g, xs=VECTORS):
    return all(f(v) == g(v) for v in xs)


def main() -> None:
    print("1. WHAT A LINEAR MAP KEEPS")
    print("   additivity    T(u + v) = Tu + Tv     adding then mapping = mapping then adding")
    print("   homogeneity   T(av) = aTv            scaling then mapping = mapping then scaling")
    print()

    print("2. FIVE MAPS, TWO CHECKS")
    num_add, num_mul = (lambda a, b: a + b), (lambda a, v: a * v)
    maps = [
        ("multiply by i:  (x, y) -> (-y, x)", turn, VECTORS, add, smul, add, smul),
        ("flatten:        (x, y) -> (x, 0)", flatten, VECTORS, add, smul, add, smul),
        ("log2: positive numbers -> R", log2, POWERS_OF_2,
            lambda u, v: u * v, lambda a, v: v ** int(a), num_add, num_mul, WHOLE_SCALARS),
        ("x -> x + 1", lambda x: x + 1, NUMBERS, num_add, num_mul, num_add, num_mul),
        ("x -> x * x", lambda x: x * x, NUMBERS, num_add, num_mul, num_add, num_mul),
    ]
    for name, T, xs, *ops in maps:
        bad = linearity_witnesses(T, xs, *ops)
        print(f"   {name:36} {'linear' if not bad else 'not linear'}")
        for line in bad:
            print(f"       {line}")
    print("   log2 is linear from lesson 2's positive numbers, where '+' is * and 'av'")
    print("   is v**a, to the ordinary numbers:")
    print(f"     log2(8 * 1/4) = {log2(Q(8) * Q(1, 4))} = log2 8 + log2 1/4 = {log2(Q(8))} + ({log2(Q(1, 4))})")
    print(f"     log2(8**3) = {log2(Q(8) ** 3)} = 3 log2 8 = 3 * {log2(Q(8))}")
    print()

    print("3. THE SAME SHAPE, WITH OTHER OPERATIONS")
    strings = ["ab", "c", ""]
    ints = [Q(3), Q(-2), Q(0)]
    pairs = [P(1, 2), P(3, -1), P(0, 1)]
    mats = [((Q(1), Q(2)), (Q(3), Q(4))), ((Q(0), Q(-1)), (Q(1), Q(0))), ((Q(2), Q(0)), (Q(1), Q(1, 2)))]
    norm2 = lambda z: z[0] ** 2 + z[1] ** 2
    shapes = [
        ("len(s + t) = len(s) + len(t)", ("strings, +", "whole numbers, +"), strings,
            lambda s, t: len(s + t), lambda s, t: len(s) + len(t)),
        ("2**(a + b) = 2**a * 2**b", ("integers, +", "fractions, *"), ints,
            lambda a, b: Q(2) ** int(a + b), lambda a, b: Q(2) ** int(a) * Q(2) ** int(b)),
        ("det(AB) = det(A) det(B)", ("2x2 matrices, *", "numbers, *"), mats,
            lambda A, B: det(matmul(A, B)), lambda A, B: det(A) * det(B)),
        ("|zw|^2 = |z|^2 |w|^2", ("complex pairs, *", "numbers, *"), pairs,
            lambda z, w: norm2(cmul(z, w)), lambda z, w: norm2(z) * norm2(w)),
        ("M(zw) = M(z) M(w)", ("complex pairs, *", "2x2 matrices, *"), pairs,
            lambda z, w: as_matrix(cmul(z, w)), lambda z, w: matmul(as_matrix(z), as_matrix(w))),
        ("|z + w|^2 = |z|^2 + |w|^2", ("complex pairs, +", "numbers, +"), pairs,
            lambda z, w: norm2(add(z, w)), lambda z, w: norm2(z) + norm2(w)),
    ]
    print(f"   {'the law':30} {'from':17}    {'to':17} on every sample pair")
    for law, (frm, to), xs, left, right in shapes:
        bad = next(((a, b) for a, b in product(xs, repeat=2) if left(a, b) != right(a, b)), None)
        print(f"   {law:30} {frm:17} -> {to:17} {'holds' if bad is None else 'FAILS'}")
        if bad is not None:
            a, b = bad
            print(f"       at {show(a)} and {show(b)}:  {show(left(a, b))} on the left,"
                  f" {show(right(a, b))} on the right")
    print("   M sends (x, y) to [[x, -y], [y, x]]. Squared length keeps multiplication")
    print("   but not addition: a map keeps a particular operation, not every one.")
    print()

    print("4. A MAP THAT CAN BE UNDONE: ONE STRUCTURE, TWO NOTATIONS")
    back = lambda n: Q(2) ** int(n)
    print("   log2 and 2**n undo each other:")
    for v in POWERS_OF_2:
        print(f"     log2 {v} = {log2(v)},   2**{log2(v)} = {back(log2(v))}")
    u, v = Q(8), Q(1, 4)
    print(f"   Multiply in one world, or add in the other:")
    print(f"     {u} * {v} = {u * v}")
    print(f"     log2: {log2(u)} + ({log2(v)}) = {log2(u) + log2(v)},  and 2**{log2(u) + log2(v)} = {back(log2(u) + log2(v))}")
    print("   The positive numbers under * are the numbers under + with every member")
    print("   renamed. That is why they passed lesson 2's test: they are R in disguise.")
    print()

    print("5. PRODUCTS OF LINEAR MAPS: WHICH LAWS, AND WHY")
    print("   Here ST means S after T, and S + T means v -> Sv + Tv.")
    f, g, h = turn, flatten, shear
    print("   S, T, U are turn, flatten and shear, checked on the sample vectors:")
    rows = [
        ("associative", "(ST)U = S(TU)", same(after(after(f, g), h), after(f, after(g, h))),
            "any functions: both sides send v to S(T(U(v)))"),
        ("identity", "TI = IT = T", same(after(f, identity), f) and same(after(identity, f), f),
            "any functions"),
        ("distributive", "(S + T)U = SU + TU", same(after(plus(f, g), h), plus(after(f, h), after(g, h))),
            "any functions: both sides are S(U(v)) + T(U(v))"),
        ("distributive", "S(T + U) = ST + SU", same(after(f, plus(g, h)), plus(after(f, g), after(f, h))),
            "needs S to be additive"),
        ("commutative", "ST = TS", same(after(f, g), after(g, f)), ""),
    ]
    for law, eq, ok, why in rows:
        print(f"     {law:13} {eq:20} {str(ok):6} {why}".rstrip())
    bump = lambda v: (v[0] + 1, v[1])
    lhs, rhs = after(bump, plus(g, h)), plus(after(bump, g), after(bump, h))
    v = VECTORS[0]
    print(f"   With S = (x, y) -> (x + 1, y), which is not additive, the second distributive")
    print(f"   law fails: at v = {show(v)}, S(T + U) gives {show(lhs(v))} and ST + SU gives {show(rhs(v))}.")
    ft, tf = after(f, g), after(g, f)
    print(f"   And order matters: turn after flatten sends {show(v)} to {show(ft(v))},")
    print(f"   flatten after turn sends it to {show(tf(v))}.")
    print("   Associative with an identity is lesson 1's monoid; with + and distributivity")
    print("   it is a ring: the linear maps from a space to itself are one, and not a")
    print("   commutative one.")


if __name__ == "__main__":
    main()
