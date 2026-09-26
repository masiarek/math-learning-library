#!/usr/bin/env python3
"""The roots of unity: the unit points that come back to (1, 0).

Run:  python3 roots_of_unity.py

Multiplying by a unit point turns the plane by the point's angle, so
multiplying by it n times turns n times as far:

    (cos A, sin A)^n = (cos nA, sin nA)        de Moivre's formula

A unit point at 1/n of a turn is therefore back at (1, 0) after n steps. It
is an n-th root of unity, a solution of z^n = 1, and there are exactly n of
them, evenly spaced around the circle.

Everything below is exact, and no angle is ever computed. Coordinates are
fractions, or fractions with a sqrt(3) in them carried as a symbol, so that
h^12 = (1, 0) is an equality and not a float within 1e-16 of one. The last
section does it in floats, to show why that matters.
"""

import math
from fractions import Fraction as F


class Root3:
    """An exact number a + b sqrt(3), with a and b fractions.

    (a + b r)(c + d r) = (ac + 3bd) + (ad + bc) r,   because r r = 3.
    """

    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def of(x):
        return x if isinstance(x, Root3) else Root3(x)

    def __add__(self, o):
        o = Root3.of(o)
        return Root3(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        o = Root3.of(o)
        return Root3(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return Root3.of(o) - self

    def __mul__(self, o):
        o = Root3.of(o)
        return Root3(self.a * o.a + 3 * self.b * o.b, self.a * o.b + self.b * o.a)

    __radd__ = __add__
    __rmul__ = __mul__

    def __neg__(self):
        return Root3(-self.a, -self.b)

    def __eq__(self, o):
        o = Root3.of(o)
        return (self.a, self.b) == (o.a, o.b)

    def __hash__(self):
        return hash((self.a, self.b))

    def __str__(self):
        a, b = self.a, self.b
        if b == 0:
            return str(a)
        if a == 0:
            return root_part(b)
        return f"{a} {'-' if b < 0 else '+'} {root_part(abs(b))}"


def root_part(b: F) -> str:
    """b sqrt(3), written the way a person would: sqrt(3)/2, -sqrt(3), 2sqrt(3)/3."""
    sign = "-" if b < 0 else ""
    b = abs(b)
    num = "" if b.numerator == 1 else str(b.numerator)
    den = "" if b.denominator == 1 else f"/{b.denominator}"
    return f"{sign}{num}sqrt(3){den}"


R = Root3


def mul(z1, z2):
    """The pair rule, unchanged from the previous lessons: (x1 x2 - y1 y2, x1 y2 + x2 y1).

    It only asks that the coordinates add, subtract and multiply, so it works
    on fractions, on numbers with a sqrt(3) in them, and on floats.
    """
    x1, y1 = z1
    x2, y2 = z2
    return (x1 * x2 - y1 * y2, x1 * y2 + x2 * y1)


def add(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])


def power(z, n):
    w = ONE
    for _ in range(n):
        w = mul(w, z)
    return w


def length_squared(z):
    x, y = z
    return x * x + y * y


def show(z) -> str:
    return f"({z[0]}, {z[1]})"


ONE = (F(1), F(0))
ZERO = (F(0), F(0))


def main() -> None:
    print("1. THE POWERS OF A UNIT POINT STAY ON THE CIRCLE")
    print("   z = (3/5, 4/5), the 3-4-5 point, sits at some angle A that is never")
    print("   computed. Multiply it by itself:")
    z = (F(3, 5), F(4, 5))
    for n in range(7):
        w = power(z, n)
        print(f"     z^{n} = {show(w):<32} |z^{n}|^2 = {length_squared(w)}")
    print("   Angles add, so z^n sits at angle nA: de Moivre's formula,")
    print("   (cos A, sin A)^n = (cos nA, sin nA). For n = 2 and 3 the right-hand")
    print("   side has a formula in cos A = 3/5 and sin A = 4/5, checked exactly:")
    c, s = z
    double = (2 * c * c - 1, 2 * s * c)
    triple = (4 * c**3 - 3 * c, 3 * s - 4 * s**3)
    print(f"     (2 cos^2 A - 1, 2 sin A cos A)             = {show(double):<20} = z^2: {double == power(z, 2)}")
    print(f"     (4 cos^3 A - 3 cos A, 3 sin A - 4 sin^3 A) = {show(triple):<20} = z^3: {triple == power(z, 3)}")
    print("   Clear the denominators and every power is a Pythagorean triple:")
    for n in (2, 3, 4):
        x, y = power(z, n)
        a, b = abs(x.numerator), abs(y.numerator)
        print(f"     z^{n}:  {a}^2 + {b}^2 = {a * a + b * b} = {5**n}^2")
    print()

    print("2. THIS POINT NEVER COMES BACK")
    print("   In lowest terms the denominators of z^n are exactly 5^n:")
    for n in (1, 6, 12, 24):
        x, y = power(z, n)
        assert x.denominator == y.denominator
        print(f"     n = {n:>2}   5^{n:<2} = {x.denominator}")
    both = all(
        power(z, n)[0].denominator == 5**n and power(z, n)[1].denominator == 5**n
        for n in range(1, 25)
    )
    print(f"   Both coordinates have denominator 5^n for every n from 1 to 24: {both}.")
    print("   A fraction with denominator 5^n is not 1, so z^n is never (1, 0). The")
    print("   3-4-5 point turns by A at every step and never completes a whole")
    print("   number of turns: A is not 1/12 of a turn, or 5/17, or any fraction.")
    print()

    print("3. CARRYING sqrt(3) EXACTLY")
    print("   The point at 1/12 of a turn is (cos 30, sin 30) = (sqrt(3)/2, 1/2),")
    print("   and sqrt(3) is not a fraction. So the program keeps numbers of the")
    print("   form a + b sqrt(3), a and b fractions, and multiplies them by")
    print("     (a + b sqrt(3)) . (c + d sqrt(3)) = (ac + 3bd) + (ad + bc) sqrt(3)")
    r = R(0, 1)
    print(f"     sqrt(3) . sqrt(3)               = {r * r}")
    print(f"     (1 + sqrt(3)) . (1 - sqrt(3))   = {R(1, 1) * R(1, -1)}")
    print(f"     (1/2 + sqrt(3)/2)^2             = {R(F(1, 2), F(1, 2)) * R(F(1, 2), F(1, 2))}")
    h = (R(0, F(1, 2)), R(F(1, 2)))
    print(f"     (sqrt(3)/2)^2 + (1/2)^2         = {length_squared(h)}     so {show(h)} is a unit point")
    print("   Nothing is rounded. The pair rule mul() is the same four lines as in")
    print("   the previous lessons: it only asks that coordinates add, subtract and")
    print("   multiply, and these do.")
    print()

    print("4. THE TWELVE MARKS OF A CLOCK FACE")
    print("   h = (sqrt(3)/2, 1/2), one twelfth of a turn, multiplied by itself:")
    marks = [power(h, k) for k in range(12)]
    for k in range(13):
        w = power(h, k)
        line = f"     k = {k:>2}   h^{k:<2} = {show(w):<24}"
        if k == 12:
            line += "   back at the start, exactly"
        print(line.rstrip())
    print(f"   Every |h^k|^2 is 1: {all(length_squared(m) == 1 for m in marks)}. Twelve steps of a twelfth of")
    print("   a turn is one turn, so h^12 = 1: h is a 12th root of unity. The four")
    print("   compass points are among the marks, at k = 0, 3, 6 and 9.")
    print()

    print("5. z^n = 1 HAS EXACTLY n SOLUTIONS")
    print("   Each mark raised to the powers 2, 3, 4, 6 and 12. A 1 means the result")
    print("   is (1, 0); a dot means it is not.")
    ns = (2, 3, 4, 6, 12)
    print(f"      k   {'mark':<22}" + "".join(f"{'z^' + str(n):>5}" for n in ns) + "   first return")
    counts = dict.fromkeys(ns, 0)
    for k, m in enumerate(marks):
        cells = ""
        for n in ns:
            hit = power(m, n) == ONE
            counts[n] += hit
            cells += f"{'1' if hit else '.':>5}"
        first = next(n for n in range(1, 13) if power(m, n) == ONE)
        print(f"     {k:>2}   {show(m):<22}{cells}   {first:>6}")
    print(f"     solutions of z^n = 1:      " + "".join(f"{counts[n]:>5}" for n in ns))
    print("   The solutions of z^n = 1 are the marks k that are multiples of 12/n:")
    print("   n of them, evenly spaced. A degree-n equation has at most n solutions")
    print("   in a field, so these are all of them. The marks that need all twelve")
    print("   steps, k = 1, 5, 7 and 11, are the primitive 12th roots of unity, and")
    print("   they are exactly the k with no factor in common with 12.")
    print()

    print("6. THE CUBE ROOTS OF UNITY, AND WHERE sqrt(-3) LIVES")
    w = marks[4]
    print(f"   Mark 4 is w = {show(w)}. Its powers:")
    print(f"     w^1 = {show(w)}")
    print(f"     w^2 = {show(power(w, 2)):<24} which is mark 8: {power(w, 2) == marks[8]}")
    print(f"     w^3 = {show(power(w, 3))}")
    print("   z^3 - 1 = (z - 1)(z^2 + z + 1), so a cube root of 1 other than 1 must")
    print("   solve z^2 + z + 1 = 0:")
    print(f"     w^2 + w + 1 = {show(add(add(power(w, 2), w), ONE))}")
    print("   The quadratic formula says z = (-1 +/- sqrt(-3)) / 2. In pairs, sqrt(-3)")
    print("   is the point (0, sqrt(3)):")
    root_minus_3 = (R(0), R(0, 1))
    formula = mul(add((R(-1), R(0)), root_minus_3), (R(F(1, 2)), R(0)))
    print(f"     (0, sqrt(3)) . (0, sqrt(3))           = {show(mul(root_minus_3, root_minus_3))}")
    print(f"     ((-1, 0) + (0, sqrt(3))) . (1/2, 0)   = {show(formula):<20} which is w: {formula == w}")
    print("   And the roots of unity always add up to nothing:")
    for label, ks in [("the 3 cube roots,   marks 0, 4, 8:   ", (0, 4, 8)),
                      ("the 4 fourth roots, marks 0, 3, 6, 9:", (0, 3, 6, 9)),
                      ("all 12 marks:                        ", range(12))]:
        total = ZERO
        for k in ks:
            total = add(total, marks[k])
        print(f"     {label}  sum = {show(total)}")
    print()

    print("7. THE SAME THING IN FLOATS")
    print("   Build the same points from math.sqrt(3) / 2, the nearest double to")
    print("   sqrt(3)/2, and multiply with the same mul():")
    s = math.sqrt(3) / 2
    wf = (-0.5, s)
    hf = (s, 0.5)
    w3 = mul(mul(wf, wf), wf)
    h12 = power(hf, 12)
    print(f"     w         = {show(wf)}")
    print(f"     w . w . w = {show(w3)}")
    print(f"                 off (1, 0) by ({w3[0] - 1}, {w3[1]})")
    print(f"     h         = {show(hf)}")
    print(f"     h^12      = {show(h12)}")
    print(f"                 off (1, 0) by ({h12[0] - 1}, {h12[1]})")
    print("   Neither is (1, 0). The rule is exact; the coordinates were rounded")
    print("   once, at the start, and every multiplication carried the error along.")
    print("   Exactly, w^3 = (1, 0) and h^12 = (1, 0), as sections 4 and 6 found.")


if __name__ == "__main__":
    main()
