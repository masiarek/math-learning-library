#!/usr/bin/env python3
"""The distance formula: Pythagoras, with the legs read off the coordinates.

Run:  python3 distance_formula.py              the page
      python3 distance_formula.py 1,3 5,6      the distance between your two points

Two points P1 = (x1, y1) and P2 = (x2, y2), and a third, P3 = (x2, y1), at the
corner where a horizontal line through P1 meets a vertical line through P2.
The legs of that right triangle are |x2 - x1| and |y2 - y1|, and the
Pythagorean theorem gives the rest:

    d(P1, P2) = sqrt((x2 - x1)^2 + (y2 - y1)^2)

The squares do two jobs: they are Pythagoras, and they throw away the signs,
which is why the order of the points does not matter and the absolute values
can be dropped. Coordinates are fractions, so d^2 is exact; d itself is
printed in simplest radical form, 2 sqrt(5) rather than 4.4721.
"""

import math
import sys
from fractions import Fraction as F

Point = tuple[F, F]


def d2(p: Point, q: Point) -> F:
    """The squared distance: exact, and all the comparisons need."""
    return (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2


def fmt(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def pt(p: Point) -> str:
    return f"({fmt(p[0])}, {fmt(p[1])})"


def root(n: F) -> str:
    """sqrt(n) exactly when it can be, else in simplest radical form with a decimal."""
    num, den = n.numerator * n.denominator, n.denominator  # sqrt(p/q) = sqrt(pq)/q
    outside, inside, k = 1, num, 2
    while k * k <= inside:
        while inside % (k * k) == 0:
            inside //= k * k
            outside *= k
        k += 1
    coef = F(outside, den)
    if inside == 1:
        return fmt(coef)
    front = "" if coef == 1 else f"{fmt(coef)} "
    return f"{front}sqrt({inside}) = {math.sqrt(n):.4f}"


def main() -> None:
    print("1. EXAMPLE 1: THE CORNER POINT MAKES A RIGHT TRIANGLE")
    p1, p2 = (F(1), F(3)), (F(5), F(6))
    p3 = (p2[0], p1[1])
    print(f"   P1 = {pt(p1)}, P2 = {pt(p2)}; the corner P3 = (x2, y1) = {pt(p3)}.")
    print(f"   Horizontal leg P1P3: |5 - 1| = 4.   Vertical leg P3P2: |6 - 3| = 3.")
    print(f"   d^2 = 4^2 + 3^2 = {fmt(d2(p1, p2))}, d = {root(d2(p1, p2))}.")
    print()

    print("2. THE ORDER OF THE POINTS DOES NOT MATTER")
    for a, b in [(p1, p2), (p2, p1)]:
        dx, dy = b[0] - a[0], b[1] - a[1]
        print(f"   from {pt(a)} to {pt(b)}: x2 - x1 = {fmt(dx):>2}, y2 - y1 = {fmt(dy):>2}, "
              f"squares {fmt(dx*dx)} + {fmt(dy*dy)} = {fmt(d2(a, b))}")
    print("   Swapping the points flips both signs, and squaring cannot see a sign.")
    print("   So (x2 - x1)^2 = (x1 - x2)^2 and no absolute value is needed.")
    print()

    print("3. HORIZONTAL AND VERTICAL: THE FORMULA STILL WORKS")
    for a, b in [((F(-2), F(4)), (F(5), F(4))), ((F(3), F(-1)), (F(3), F(-7)))]:
        print(f"   {pt(a)} to {pt(b)}: d = sqrt({fmt(d2(a, b))}) = {root(d2(a, b))}")
    print("   One leg is 0, so d = sqrt(t^2) for a single difference t, and sqrt(t^2) = |t|,")
    print("   not t: going down from y = -1 to y = -7, t = -6, and the distance is 6.")
    print()

    print("4. MOST DISTANCES ARE NOT WHOLE NUMBERS")
    for a, b in [((F(-4), F(5)), (F(3), F(2))), ((F(0), F(0)), (F(1), F(1))),
                 ((F(1, 2), F(0)), (F(0), F(1, 2))), ((F(-1), F(-2)), (F(2), F(2)))]:
        print(f"   {pt(a):12} to {pt(b):10}  d^2 = {fmt(d2(a, b)):>4}   d = {root(d2(a, b))}")
    print("   d^2 is always exact. d is exact only when d^2 is a perfect square;")
    print("   otherwise the book asks for the radical in simplest form, and so does this.")
    print()

    print("5. THE CONVERSE AT WORK: IS A = (-2, 1), B = (2, 3), C = (3, 1) A RIGHT TRIANGLE?")
    A, B, C = (F(-2), F(1)), (F(2), F(3)), (F(3), F(1))
    ab, bc, ac = d2(A, B), d2(B, C), d2(A, C)
    print(f"   d(A,B)^2 = {fmt(ab)}, d(B,C)^2 = {fmt(bc)}, d(A,C)^2 = {fmt(ac)}")
    print(f"   {fmt(ab)} + {fmt(bc)} = {fmt(ab + bc)} = d(A,C)^2, so yes: the right angle is at B,")
    print(f"   opposite the longest side AC. Area = (1/2) sqrt({fmt(ab)}) sqrt({fmt(bc)}) = (1/2) sqrt({fmt(ab*bc)}) = {fmt(F(1, 2) * math.isqrt(int(ab * bc)))}.")
    print("   Squared distances are enough to decide; no square root was taken until the area.")
    print()

    print("6. THREE POINTS ON A LINE: THE TWO SHORT DISTANCES ADD UP")
    P, Q, R = (F(0), F(0)), (F(3), F(4)), (F(6), F(8))
    print(f"   P = {pt(P)}, Q = {pt(Q)}, R = {pt(R)}:  d(P,Q) = {root(d2(P, Q))}, d(Q,R) = {root(d2(Q, R))}, d(P,R) = {root(d2(P, R))}")
    Q2 = (F(3), F(5))
    print(f"   Move Q to {pt(Q2)}: d(P,Q) + d(Q,R) = {math.sqrt(d2(P, Q2)) + math.sqrt(d2(Q2, R)):.4f} > {math.sqrt(d2(P, R)):.4f} = d(P,R).")
    print("   A detour is always longer: the triangle inequality, with equality only on the line.")


def check(args: list[str]) -> None:
    a, b = (tuple(F(v) for v in s.strip("()").split(",")) for s in args)
    print(f"d({pt(a)}, {pt(b)}):")
    print(f"  (x2 - x1)^2 + (y2 - y1)^2 = ({fmt(b[0] - a[0])})^2 + ({fmt(b[1] - a[1])})^2 = {fmt(d2(a, b))}")
    print(f"  d = {root(d2(a, b))}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        check(sys.argv[1:])
    elif len(sys.argv) == 1:
        main()
    else:
        sys.exit("usage: python3 distance_formula.py [x1,y1 x2,y2]")
