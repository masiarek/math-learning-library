#!/usr/bin/env python3
"""Lines: slope is one number for the whole line, and every equation of a line says so.

Run:  python3 lines_and_slope.py               the page
      python3 lines_and_slope.py 2,3 -4,5      the line through your two points

The slope of the line through (x1, y1) and (x2, y2), with x1 != x2, is

    m = (y2 - y1) / (x2 - x1)          rise over run

and the claim that makes it useful is that it does not depend on which two
points of the line are used: any two make a right triangle with the same
angles, the triangles are similar, and similar triangles have the same ratio
of sides. Every form of the equation of a line is that one fact rearranged:

    point-slope       y - y1 = m (x - x1)
    slope-intercept   y = m x + b
    general           A x + B y = C          (A and B not both 0)

Parallel lines have equal slopes; perpendicular lines have slopes whose
product is -1. Everything is exact fractions.
"""

import sys
from fractions import Fraction as F

Point = tuple[F, F]


def fmt(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def pt(p: Point) -> str:
    return f"({fmt(p[0])}, {fmt(p[1])})"


def par(x: F) -> str:
    """A number as it goes into a difference: negatives in brackets."""
    return f"({fmt(x)})" if x < 0 else fmt(x)


def coef(m: F) -> str:
    """A coefficient in front of a variable: 1 and -1 vanish, fractions get brackets."""
    if m == 1:
        return ""
    if m == -1:
        return "-"
    return f"({fmt(m)})" if m.denominator != 1 else fmt(m)


def minus(var: str, v: F) -> str:
    """var - v, written the way a person would: x - 2, x + 2, x."""
    if v == 0:
        return var
    return f"{var} - {fmt(v)}" if v > 0 else f"{var} + {fmt(-v)}"


def slope(p: Point, q: Point):
    if p[0] == q[0]:
        return None
    return (q[1] - p[1]) / (q[0] - p[0])


def slope_intercept(m: F, b: F) -> str:
    if m == 0:
        return f"y = {fmt(b)}"
    mx = f"{coef(m)}x"
    if b == 0:
        return f"y = {mx}"
    return f"y = {mx} {'+' if b > 0 else '-'} {fmt(abs(b))}"


def general(p: Point, q: Point) -> str:
    """A x + B y = C with whole numbers, A >= 0, and no common factor."""
    from math import gcd
    A, B = q[1] - p[1], p[0] - q[0]
    C = A * p[0] + B * p[1]
    den = 1
    for v in (A, B, C):
        den = den * v.denominator // gcd(den, v.denominator)
    A, B, C = (int(v * den) for v in (A, B, C))
    g = gcd(gcd(A, B), C) or 1
    A, B, C = A // g, B // g, C // g
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    parts = []
    if A:
        parts.append("x" if A == 1 else f"{A}x")
    if B:
        term = "y" if abs(B) == 1 else f"{abs(B)}y"
        parts.append(("- " if B < 0 else "+ ") + term if parts else ("-" if B < 0 else "") + term)
    return f"{' '.join(parts)} = {C}"


def describe(p: Point, q: Point) -> list[str]:
    m = slope(p, q)
    out = [f"through {pt(p)} and {pt(q)}:"]
    if m is None:
        out.append(f"  run x2 - x1 = 0: slope undefined, a vertical line, x = {fmt(p[0])}")
    else:
        b = p[1] - m * p[0]
        out.append(f"  slope m = ({fmt(q[1])} - {par(p[1])}) / ({fmt(q[0])} - {par(p[0])}) = {fmt(m)}")
        rhs = "0" if m == 0 else f"{coef(m)}({minus('x', p[0])})" if p[0] else f"{coef(m)}x"
        out.append(f"  point-slope:     {minus('y', p[1])} = {rhs}")
        out.append(f"  slope-intercept: {slope_intercept(m, b)}")
    out.append(f"  general form:    {general(p, q)}")
    return out


def main() -> None:
    print("1. RISE OVER RUN, AND THE ORDER OF THE POINTS")
    p, q = (F(1), F(2)), (F(5), F(-3))
    print(f"   P = {pt(p)}, Q = {pt(q)}")
    print(f"   (y2 - y1)/(x2 - x1), P first:  (-3 - 2)/(5 - 1) = {fmt(slope(p, q))}")
    print(f"   (y2 - y1)/(x2 - x1), Q first:  (2 - (-3))/(1 - 5) = {fmt(slope(q, p))}")
    print(f"   mixed order, wrong:            (-3 - 2)/(1 - 5) = {fmt(F(-5, -4))}")
    print("   Either point may come first, as long as both differences start from the same one.")
    print()

    print("2. ONE SLOPE FOR THE WHOLE LINE: ANY TWO POINTS OF 2x - 3y = 6")
    pts = [(F(x), (F(2 * x) - 6) / 3) for x in (-3, 0, 3, 6, 9)]
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            a, b = pts[i], pts[j]
            print(f"   {pt(a):9} to {pt(b):8}  rise {fmt(b[1] - a[1]):>2}, run {fmt(b[0] - a[0]):>2}, slope {fmt(slope(a, b))}")
    print("   Ten pairs, ten right triangles of different sizes, all similar: one ratio, 2/3.")
    print()

    print("3. WHAT THE NUMBER SAYS")
    for m, words in [(F(3), "rises steeply: up 3 for each 1 across"),
                     (F(1, 3), "rises gently: up 1 for each 3 across"),
                     (F(0), "horizontal: no rise at all"),
                     (F(-2), "falls: down 2 for each 1 across")]:
        print(f"   m = {fmt(m):>4}   {words}")
    print("   vertical: the run is 0 and rise/0 is not a number. Undefined, not 0,")
    print("   and not infinity: 'no slope' means the formula has nothing to divide by.")
    print()

    print("4. THE SAME LINE IN EVERY FORM")
    for a, b in [((F(1), F(2)), (F(5), F(-3))), ((F(-2), F(4)), (F(3), F(4))),
                 ((F(3), F(-1)), (F(3), F(7))), ((F(0), F(0)), (F(2), F(1)))]:
        for line in describe(a, b):
            print("   " + line)
    print("   Only the general form covers the vertical line: y = mx + b needs a slope.")
    print()

    print("5. INTERCEPTS OF A LINE: 2x - 3y = 6")
    print("   y = 0: 2x = 6, x-intercept 3.   x = 0: -3y = 6, y-intercept -2.")
    print("   Solved for y: y = (2/3)x - 2. The b in y = mx + b is the y-intercept.")
    print()

    print("6. PARALLEL: SAME SLOPE, DIFFERENT INTERCEPT")
    print("   y = 2x + 1 and y = 2x - 3 never meet: 2x + 1 = 2x - 3 means 1 = -3.")
    print("   y = 2x + 1 and 4x - 2y = -2: the second is y = 2x + 1 again, the same line.")
    print()

    print("7. PERPENDICULAR: SLOPES MULTIPLY TO -1")
    print("   A quarter turn sends the step (run, rise) = (a, b) to (-b, a):")
    for a, b in [(F(1), F(2)), (F(3), F(1)), (F(2), F(-5))]:
        m1, m2 = b / a, a / -b
        o, u, v = (F(0), F(0)), (a, b), (-b, a)
        d_uv = (u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2
        leg = a * a + b * b
        print(f"   ({fmt(a)}, {fmt(b):>2}) -> ({fmt(-b):>2}, {fmt(a)}):  slopes {fmt(m1):>4} and {fmt(m2):>4},"
              f"  product {fmt(m1 * m2)};  Pythagoras check {fmt(leg)} + {fmt(leg)} = {fmt(d_uv)}")
    print("   The two steps are the legs of a right triangle at the origin, and the")
    print("   converse of Pythagoras confirms the right angle: leg^2 + leg^2 = hypotenuse^2.")
    print("   Negative reciprocal: flip the fraction and change its sign. 2 -> -1/2, -5/2 -> 2/5.")
    print("   A horizontal and a vertical line are perpendicular too, but 0 has no reciprocal:")
    print("   the product rule needs both slopes to exist.")


def check(args: list[str]) -> None:
    a, b = (tuple(F(v) for v in s.strip("()").split(",")) for s in args)
    if a == b:
        sys.exit("two different points are needed: through one point pass infinitely many lines")
    for line in describe(a, b):
        print(line)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        check(sys.argv[1:])
    elif len(sys.argv) == 1:
        main()
    else:
        sys.exit("usage: python3 lines_and_slope.py [x1,y1 x2,y2]")
