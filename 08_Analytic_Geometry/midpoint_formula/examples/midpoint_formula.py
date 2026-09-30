#!/usr/bin/env python3
"""The midpoint formula: the average of the x's, the average of the y's.

Run:  python3 midpoint_formula.py              the page
      python3 midpoint_formula.py -5,5 3,1     the midpoint of your two points

The midpoint M of the segment from P1 = (x1, y1) to P2 = (x2, y2) is

    M = ((x1 + x2)/2, (y1 + y2)/2)

one arithmetic mean per coordinate. Being "halfway" is two claims, and the
program checks both with the distance formula: M is the same distance from
each end, and M is on the segment. The first alone is not enough.

Coordinates are fractions and distances are compared by their squares, so
every check is exact.
"""

import sys
from fractions import Fraction as F

Point = tuple[F, F]


def mid(p: Point, q: Point) -> Point:
    return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)


def d2(p: Point, q: Point) -> F:
    return (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2


def on_segment(p: Point, m: Point, q: Point) -> bool:
    """m is on segment pq exactly when the two short distances add up to the long one.

    With squares only: sqrt(a) + sqrt(b) = sqrt(c) iff c = a + b + 2 sqrt(ab),
    i.e. (c - a - b)^2 = 4ab with c - a - b >= 0.
    """
    a, b, c = d2(p, m), d2(m, q), d2(p, q)
    return c - a - b >= 0 and (c - a - b) ** 2 == 4 * a * b


def fmt(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def par(x: F) -> str:
    """A number as it goes into a sum: negatives in brackets."""
    return f"({fmt(x)})" if x < 0 else fmt(x)


def pt(p: Point) -> str:
    return f"({fmt(p[0])}, {fmt(p[1])})"


def main() -> None:
    print("1. THE FORMULA: ONE AVERAGE PER COORDINATE")
    p1, p2 = (F(-5), F(5)), (F(3), F(1))
    m = mid(p1, p2)
    print(f"   P1 = {pt(p1)}, P2 = {pt(p2)}")
    print(f"   x: (-5 + 3)/2 = {fmt(m[0])}     y: (5 + 1)/2 = {fmt(m[1])}     M = {pt(m)}")
    print()

    print("2. HALFWAY IS TWO CLAIMS, AND BOTH HOLD")
    print(f"   d(P1, M)^2 = {fmt(d2(p1, m))}, d(M, P2)^2 = {fmt(d2(m, p2))}: equal distances.")
    print(f"   d(P1, P2)^2 = {fmt(d2(p1, p2))} = 4 * {fmt(d2(p1, m))}: M is half the length from each end.")
    print(f"   On the segment: {on_segment(p1, m, p2)}")
    print()

    print("3. EQUAL DISTANCES ALONE ARE NOT ENOUGH")
    for q in [(F(1), F(7)), (F(-3), F(-1)), m]:
        eq = d2(p1, q) == d2(q, p2)
        print(f"   {pt(q):9}  d(P1,Q)^2 = {fmt(d2(p1, q)):>3}  d(Q,P2)^2 = {fmt(d2(q, p2)):>3}  "
              f"equidistant: {str(eq):5}  on segment: {on_segment(p1, q, p2)}")
    print("   Every point of a whole line, the perpendicular bisector, is as far from P1")
    print("   as from P2. Only one of them is on the segment: the midpoint.")
    print()

    print("4. THE TRAP: HALF THE DIFFERENCE IS NOT THE MIDPOINT")
    wrong = ((p2[0] - p1[0]) / 2, (p2[1] - p1[1]) / 2)
    print(f"   ((x2 - x1)/2, (y2 - y1)/2) = {pt(wrong)}: that is half of the trip, a displacement,")
    print(f"   not a place. Added to the start it lands on the midpoint: P1 + {pt(wrong)} = "
          f"{pt((p1[0] + wrong[0], p1[1] + wrong[1]))}.")
    print()

    print("5. WORKING BACKWARDS: ONE END AND THE MIDPOINT GIVE THE OTHER END")
    p, m2 = (F(1), F(2)), (F(4), F(-1))
    q = (2 * m2[0] - p[0], 2 * m2[1] - p[1])
    print(f"   P1 = {pt(p)}, M = {pt(m2)}:  x2 = 2*4 - 1 = {fmt(q[0])}, y2 = 2*(-1) - 2 = {fmt(q[1])}, P2 = {pt(q)}")
    print(f"   Check: midpoint of {pt(p)} and {pt(q)} is {pt(mid(p, q))}.")
    print("   The midpoint is the average, so the far end is as far past M as P1 is short of it.")
    print()

    print("6. NOT JUST HALFWAY: THE POINT A FRACTION t OF THE WAY")
    print("   P1 + t (P2 - P1); t = 1/2 is the midpoint, and t = 0 and t = 1 are the ends.")
    for t in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1), F(2)]:
        q = (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))
        print(f"     t = {fmt(t):3}  {pt(q):12}  on segment: {on_segment(p1, q, p2)}")
    print("   t = 2 is on the same line but past P2: t between 0 and 1 is the segment.")


def check(args: list[str]) -> None:
    a, b = (tuple(F(v) for v in s.strip("()").split(",")) for s in args)
    m = mid(a, b)
    print(f"midpoint of {pt(a)} and {pt(b)}:")
    print(f"  x = ({fmt(a[0])} + {par(b[0])})/2 = {fmt(m[0])},  y = ({fmt(a[1])} + {par(b[1])})/2 = {fmt(m[1])}")
    print(f"  M = {pt(m)}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        check(sys.argv[1:])
    elif len(sys.argv) == 1:
        main()
    else:
        sys.exit("usage: python3 midpoint_formula.py [x1,y1 x2,y2]")
