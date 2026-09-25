#!/usr/bin/env python3
"""Complex multiplication is a rule on pairs of real numbers -- nothing more.

Run:  python3 multiplication_as_pairs.py

Define a complex number as a pair (x, y) of reals, and define

    (x1, y1) . (x2, y2) = (x1*x2 - y1*y2,  x1*y2 + x2*y1)

No square root of -1 is ever taken. Below, that rule is written out by hand
with exact fractions and checked: it gives (0, 1) . (0, 1) = (-1, 0), it obeys
the laws of arithmetic, it is what the symbol i makes automatic, and it is
the same thing Python's own complex type does.
"""

from fractions import Fraction as F
from itertools import product

Pair = tuple[F, F]


def mul(z1: Pair, z2: Pair) -> Pair:
    """The definition, verbatim: (x1 x2 - y1 y2, x1 y2 + x2 y1)."""
    x1, y1 = z1
    x2, y2 = z2
    return (x1 * x2 - y1 * y2, x1 * y2 + x2 * y1)


def add(z1: Pair, z2: Pair) -> Pair:
    x1, y1 = z1
    x2, y2 = z2
    return (x1 + x2, y1 + y2)


def show(z: Pair) -> str:
    x, y = z
    return f"({x}, {y})"


def as_x_plus_iy(z: Pair) -> str:
    """The same pair in the usual notation, written by hand from the components."""
    x, y = z
    sign = "-" if y < 0 else "+"
    return f"{x} {sign} {abs(y)}i"


ONE: Pair = (F(1), F(0))
I: Pair = (F(0), F(1))


def main() -> None:
    print("1. THE RULE, APPLIED TO TWO PAIRS")
    z1, z2 = (F(3), F(2)), (F(1), F(4))
    x1, y1 = z1
    x2, y2 = z2
    print(f"   z1 = {show(z1)}    z2 = {show(z2)}")
    print(f"   first  = x1*x2 - y1*y2 = {x1}*{x2} - {y1}*{y2} = {x1 * x2} - {y1 * y2} = {x1 * x2 - y1 * y2}")
    print(f"   second = x1*y2 + x2*y1 = {x1}*{y2} + {x2}*{y1} = {x1 * y2} + {x2 * y1} = {x1 * y2 + x2 * y1}")
    print(f"   z1 . z2 = {show(mul(z1, z2))}")
    print("   Four real multiplications, one subtraction, one addition. That is all.")
    print()

    print("2. THE PAIR (0, 1) SQUARES TO (-1, 0)")
    sq = mul(I, I)
    print(f"   (0, 1) . (0, 1) = (0*0 - 1*1, 0*1 + 0*1) = {show(sq)}")
    print("   Nothing was taken the square root of. The rule has this property")
    print("   because of the minus sign in its first component, and for no other")
    print("   reason. Calling (0, 1) by the name i is a choice of notation.")
    print()

    print("3. THE REAL NUMBERS SIT INSIDE, AS THE PAIRS (x, 0)")
    for a, b in [(F(2), F(3)), (F(-5), F(7)), (F(1, 2), F(4, 3))]:
        za, zb = (a, F(0)), (b, F(0))
        print(f"   {show(za):<9} . {show(zb):<9} = {show(mul(za, zb)):<10} and {a} x {b} = {a * b}")
    print("   On pairs with second part 0, the rule is ordinary multiplication,")
    print("   so the reals were not replaced by something new; they were kept.")
    print()

    print("4. WHAT (x, 0) . (0, 1) DOES: SCALES THE SECOND AXIS")
    for a in [F(2), F(-3), F(1, 2)]:
        print(f"   {show((a, F(0))):<10} . (0, 1) = {show(mul((a, F(0)), I))}")
    print("   So every pair splits: (x, y) = (x, 0) + (y, 0) . (0, 1), which in")
    print("   the usual notation reads x + y i.")
    for z in [(F(3), F(2)), (F(-1), F(-5))]:
        x, y = z
        rebuilt = add((x, F(0)), mul((y, F(0)), I))
        print(f"   {show(z)} = {show((x, F(0)))} + {show((y, F(0)))} . (0, 1) = {show(rebuilt)}   [{as_x_plus_iy(z)}]")
    print()

    print("5. THE LAWS OF ARITHMETIC HOLD (checked on a grid of pairs)")
    coords = [F(-2), F(-1), F(0), F(1, 2), F(1), F(3)]
    pairs = [(x, y) for x in coords for y in coords]
    checks = {
        "commutative   z1.z2 = z2.z1": 0,
        "associative   (z1.z2).z3 = z1.(z2.z3)": 0,
        "distributive  z1.(z2+z3) = z1.z2 + z1.z3": 0,
        "identity      (1, 0).z = z": 0,
    }
    for z1, z2 in product(pairs, repeat=2):
        assert mul(z1, z2) == mul(z2, z1)
        checks["commutative   z1.z2 = z2.z1"] += 1
    for z1, z2, z3 in product(pairs, repeat=3):
        assert mul(mul(z1, z2), z3) == mul(z1, mul(z2, z3))
        checks["associative   (z1.z2).z3 = z1.(z2.z3)"] += 1
        assert mul(z1, add(z2, z3)) == add(mul(z1, z2), mul(z1, z3))
        checks["distributive  z1.(z2+z3) = z1.z2 + z1.z3"] += 1
    for z in pairs:
        assert mul(ONE, z) == z
        checks["identity      (1, 0).z = z"] += 1
    print(f"   {len(pairs)} pairs, coordinates from {{{', '.join(str(c) for c in coords)}}}, exact fractions:")
    for law, n in checks.items():
        print(f"     {law:<42} {n:>7,} cases, 0 failures")
    print("   A finite check; the page gives the two-line algebra that covers all.")
    print()

    print("6. AND EVERY NON-ZERO PAIR HAS A RECIPROCAL")
    for z in [(F(3), F(4)), (F(0), F(1)), (F(1, 2), F(-1, 3))]:
        x, y = z
        d = x * x + y * y
        inv = (x / d, -y / d)
        print(f"   {show(z):<14} inverse {show(inv):<20} product {show(mul(z, inv))}")
    print("   The inverse is (x, -y) / (x^2 + y^2), and x^2 + y^2 is 0 only for (0, 0).")
    print("   Those are the field axioms: the pairs with this rule are a FIELD,")
    print("   the complex numbers, built from the reals with no new symbol.")
    print()

    print("7. THE SAME RULE, AS PYTHON'S complex TYPE")
    samples = [((3, 2), (1, 4)), ((0, 1), (0, 1)), ((2, -1), (2, 1)), ((0.5, 1.5), (-2, 0.25))]
    for (a, b), (c, d) in samples:
        ours = mul((F(a), F(b)), (F(c), F(d)))
        theirs = complex(a, b) * complex(c, d)
        same = (float(ours[0]), float(ours[1])) == (theirs.real, theirs.imag)
        print(f"   {show((F(a), F(b))):<12} . {show((F(c), F(d))):<12} = {show(ours):<14}"
              f" complex: {theirs}   {'same' if same else 'DIFFERENT'}")
    print("   The built-in type stores exactly a pair (z.real, z.imag) and applies")
    print("   this rule. The 'j' it prints is the name it gives the pair (0, 1).")
    print()

    print("8. THE SAME RULE, WHERE NOBODY SAYS 'COMPLEX'")
    print("   a. Rotating the plane. Multiplying by the unit pair (cos t, sin t)")
    print("      turns every point through the angle t. Take t = 90 degrees:")
    quarter = (F(0), F(1))
    pt = (F(3), F(1))
    for k in range(1, 5):
        pt = mul(pt, quarter)
        print(f"      after {k} quarter turn{'s' if k > 1 else ' '}: {show(pt)}")
    print("      Four quarter turns come back to (3, 1). This is the 2x2 matrix")
    print("      [[x, -y], [y, x]] acting on a column vector, written on one line.")
    print()
    print("   b. Adding angles. For unit pairs (cos a, sin a) . (cos b, sin b) the")
    print("      rule reads (cos a cos b - sin a sin b, cos a sin b + cos b sin a):")
    print("      the two angle-addition formulas at once, cos(a+b) and sin(a+b).")
    print("      With 3-4-5 and 5-12-13 triangles the check is exact:")
    a = (F(3, 5), F(4, 5))
    b = (F(5, 13), F(12, 13))
    ab = mul(a, b)
    print(f"      {show(a)} . {show(b)} = {show(ab)}")
    print(f"      and ({ab[0]})^2 + ({ab[1]})^2 = {ab[0] ** 2 + ab[1] ** 2}, still on the unit circle.")
    print()
    print("   c. Sums of two squares. The rule proves the identity")
    print("      (x1^2 + y1^2)(x2^2 + y2^2) = (x1x2 - y1y2)^2 + (x1y2 + x2y1)^2,")
    print("      so a product of two sums of two squares is again one:")
    for z1, z2 in [((F(1), F(2)), (F(2), F(3))), ((F(3), F(4)), (F(5), F(12)))]:
        z = mul(z1, z2)
        n1 = z1[0] ** 2 + z1[1] ** 2
        n2 = z2[0] ** 2 + z2[1] ** 2
        print(f"      {n1} x {n2} = {n1 * n2} = ({z[0]})^2 + ({z[1]})^2 = {z[0] ** 2 + z[1] ** 2}")
    print("      Multiply by the mirror image (x2, -y2) instead and the signs swap:")
    print("      (x1^2 + y1^2)(x2^2 + y2^2) = (x1x2 + y1y2)^2 + (x1y2 - x2y1)^2,")
    print("      a second way to write the same product as two squares:")
    for z1, z2 in [((F(1), F(2)), (F(2), F(3))), ((F(3), F(4)), (F(5), F(12)))]:
        z = mul(z1, (z2[0], -z2[1]))
        n1 = z1[0] ** 2 + z1[1] ** 2
        n2 = z2[0] ** 2 + z2[1] ** 2
        print(f"      {n1} x {n2} = {n1 * n2} = ({z[0]})^2 + ({z[1]})^2 = {z[0] ** 2 + z[1] ** 2}")
    print("      Brahmagupta wrote both forms in the 7th century, a thousand")
    print("      years before anyone wrote the symbol i.")


if __name__ == "__main__":
    main()
