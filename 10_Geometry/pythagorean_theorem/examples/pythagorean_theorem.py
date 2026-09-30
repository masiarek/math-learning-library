#!/usr/bin/env python3
"""The Pythagorean theorem, its converse, and what c^2 against a^2 + b^2 says.

Run:  python3 pythagorean_theorem.py            the page, with the book's problems
      python3 pythagorean_theorem.py 7 24 25    your own three sides, judged

The theorem goes one way: a right angle forces c^2 = a^2 + b^2. The converse
goes the other: c^2 = a^2 + b^2 forces a right angle. Together they make the
equation a test that three lengths pass or fail, and the test has a third
outcome the book does not print: if c^2 is smaller than a^2 + b^2 the largest
angle is acute, and if larger, obtuse.

Every length is an integer or a fraction, so every comparison is exact. Only
section 6 needs a square root that is not whole, and it says so.
"""

import math
import sys
from decimal import Decimal, getcontext
from fractions import Fraction


def judge(sides: tuple) -> str:
    """Sort the sides, then compare the square of the longest with the rest."""
    a, b, c = sorted(Fraction(s) for s in sides)
    if a <= 0:
        return "not a triangle: a side must be positive"
    if a + b <= c:
        return f"not a triangle: {fmt(a)} + {fmt(b)} = {fmt(a + b)} does not exceed {fmt(c)}"
    lhs, rhs = c * c, a * a + b * b
    if lhs == rhs:
        return f"right: {fmt(c)}^2 = {fmt(lhs)} = {fmt(a * a)} + {fmt(b * b)}, hypotenuse {fmt(c)}"
    word = "acute" if lhs < rhs else "obtuse"
    sign = "<" if lhs < rhs else ">"
    return f"{word}: {fmt(c)}^2 = {fmt(lhs)} {sign} {fmt(a * a)} + {fmt(b * b)} = {fmt(rhs)}"


def fmt(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def surd(n: int) -> str:
    """sqrt(n) in simplest form: pull out the largest square factor."""
    outside, inside = 1, n
    k = 2
    while k * k <= inside:
        while inside % (k * k) == 0:
            inside //= k * k
            outside *= k
        k += 1
    if inside == 1:
        return str(outside)
    return f"sqrt({inside})" if outside == 1 else f"{outside} sqrt({inside})"


def main() -> None:
    print("1. THE THEOREM: TWO LEGS GIVE THE HYPOTENUSE")
    print("   Example 1 and problems 13-18: c^2 = a^2 + b^2, then c = sqrt(c^2).")
    legs = [("Ex 1", 4, 3), ("13", 5, 12), ("14", 6, 8), ("15", 10, 24),
            ("16", 4, 3), ("17", 7, 24), ("18", 14, 48)]
    print(f"     {'':6}{'a':>4}{'b':>5}{'a^2 + b^2 = c^2':>20}{'c':>7}")
    for name, a, b in legs:
        c2 = a * a + b * b
        print(f"     {name:6}{a:>4}{b:>5}{f'{a*a} + {b*b} = {c2}':>20}   {surd(c2):>4}")
    print("   Every answer is a whole number, because the book picked the legs so.")
    print("   Legs 1 and 2 give c^2 = 5 and c = " + surd(5) + " = %.4f..., which no ruler reads." % math.sqrt(5))
    print()

    print("2. WHY IT IS TRUE: THE SAME SQUARE CUT TWO WAYS")
    print("   A square of side a + b holds four copies of the triangle (each ab/2)")
    print("   and a tilted square of side c in the middle. So (a + b)^2 = 4(ab/2) + c^2.")
    print(f"     {'a':>3}{'b':>4}{'(a+b)^2':>10}{'4 * ab/2':>10}{'left over':>11}{'a^2 + b^2':>11}")
    for a, b in [(3, 4), (5, 12), (1, 2), (2, 7)]:
        big, four = (a + b) ** 2, 2 * a * b
        print(f"     {a:>3}{b:>4}{big:>10}{four:>10}{big - four:>11}{a*a + b*b:>11}")
    print("   The left-over area is c^2 and it always equals a^2 + b^2: expand")
    print("   (a+b)^2 = a^2 + 2ab + b^2 and take away the 2ab. No measuring needed.")
    print()

    print("3. THE CONVERSE AS A TEST: PROBLEMS 19-26")
    print("   Sort the sides; the longest is the only candidate for the hypotenuse.")
    for name, sides in [("19", (3, 4, 5)), ("20", (6, 8, 10)), ("21", (4, 5, 6)),
                        ("22", (2, 2, 3)), ("23", (7, 24, 25)), ("24", (10, 24, 26)),
                        ("25", (6, 4, 3)), ("26", (5, 4, 7))]:
        print(f"     {name}  {str(sides):13} {judge(sides)}")
    print("   Only 19, 20, 23, 24 are right. 25 is listed 6, 4, 3: testing 3^2 against")
    print("   6^2 + 4^2 would be the wrong question, because 3 is not the longest side.")
    print()

    print("4. THE TRAP: THE THEOREM NEEDS THE RIGHT SIDE ON THE LEFT")
    a, b, c = 5, 12, 13
    print(f"   For 5, 12, 13: 13^2 = {c*c} and 5^2 + 12^2 = {a*a + b*b}: right.")
    print(f"   But 5^2 = {a*a} is not 12^2 + 13^2 = {b*b + c*c}, and 12^2 = {b*b} is not 5^2 + 13^2 = {a*a + c*c}.")
    print("   The equation names the side opposite the right angle. Put a leg there")
    print("   and a true right triangle fails the test.")
    print()

    print("5. MORE THAN YES OR NO: THE LONGEST SIDE AGAINST THE OTHER TWO")
    print("   Hold two sides at 3 and 4, and let the third one grow.")
    for c in [4, 5, 6, 7]:
        print(f"     3, 4, {c}   {judge((3, 4, c))}")
    print("   Bigger than 5 opens the angle past 90 degrees; smaller closes it.")
    print("   At 7 the triangle has gone flat: 3 + 4 = 7 is a line segment.")
    print()

    print("6. EXAMPLE 3: HOW FAR CAN YOU SEE FROM THE BURJ KHALIFA?")
    R, h = Fraction(3960), Fraction(1483, 5280)
    print("   The line of sight touches the Earth at a right angle to the radius, so")
    print("   (R + h)^2 = R^2 + d^2 with R = 3960 miles and h = 1483 feet = 1483/5280 mile.")
    d2 = (R + h) ** 2 - R ** 2
    print(f"   d^2 = (R + h)^2 - R^2 = 2Rh + h^2 = {float(d2):.4f}, so d = {math.sqrt(d2):.4f} miles.")
    print(f"   The h^2 term is {float(h*h):.4f} of that; d is about sqrt(2Rh) = {math.sqrt(2*R*h):.4f}.")
    getcontext().prec = 6
    Rd, hd = Decimal(3960), Decimal(1483) / Decimal(5280)
    naive = (Rd + hd) * (Rd + hd) - Rd * Rd
    safe = 2 * Rd * hd + hd * hd
    print("   A calculator keeping 6 significant figures, the two ways:")
    print(f"     (R + h)^2 - R^2 = {naive}     2Rh + h^2 = {safe}")
    print("   The first subtracts two numbers near 15.7 million that agree in")
    print("   their leading digits, and the difference keeps almost none of them.")
    print()


def check(args: list[str]) -> None:
    sides = tuple(Fraction(s) for s in args)
    print(f"sides {', '.join(args)}: {judge(sides)}")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        check(sys.argv[1:])
    elif len(sys.argv) == 1:
        main()
    else:
        sys.exit("usage: python3 pythagorean_theorem.py [a b c]")
