#!/usr/bin/env python3
"""Circles: the distance formula held fixed.

Run:  python3 circles.py                        the page
      python3 circles.py 1 1 -4 6 -3            is x^2 + y^2 - 4x + 6y - 3 = 0 a circle?

A circle is every point at one distance r, the radius, from one point (h, k),
the center. Write that with the distance formula and square both sides:

    (x - h)^2 + (y - k)^2 = r^2          standard form

Multiply it out and it becomes x^2 + y^2 + a x + b y + c = 0, the general
form, which hides the center and radius; completing the square brings them
back, or shows that there is no circle at all. Numbers are fractions, and
inside/on/outside is decided by squared distances, so every verdict is exact.
"""

import sys
from fractions import Fraction as F


def fmt(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def minus(var: str, v: F) -> str:
    if v == 0:
        return var
    return f"{var} - {fmt(v)}" if v > 0 else f"{var} + {fmt(-v)}"


def standard(h: F, k: F, r2: F) -> str:
    sq = lambda var, v: f"{var}^2" if v == 0 else f"({minus(var, v)})^2"
    return f"{sq('x', h)} + {sq('y', k)} = {fmt(r2)}"


def expand(h: F, k: F, r2: F) -> tuple[F, F, F]:
    """(x - h)^2 + (y - k)^2 = r^2  ->  x^2 + y^2 + a x + b y + c = 0."""
    return -2 * h, -2 * k, h * h + k * k - r2


def general(a: F, b: F, c: F) -> str:
    out = "x^2 + y^2"
    for v, var in ((a, "x"), (b, "y"), (c, "")):
        if v:
            mag = fmt(abs(v)) if (abs(v) != 1 or not var) else ""
            out += f" {'+' if v > 0 else '-'} {mag}{var}"
    return out + " = 0"


def complete(a: F, b: F, c: F) -> tuple[F, F, F]:
    """x^2 + a x = (x + a/2)^2 - (a/2)^2, and the same for y."""
    h, k = -a / 2, -b / 2
    return h, k, h * h + k * k - c


def root(n: F) -> str:
    num, den = n.numerator * n.denominator, n.denominator
    out, inside, j = 1, num, 2
    while j * j <= inside:
        while inside % (j * j) == 0:
            inside //= j * j
            out *= j
        j += 1
    c = F(out, den)
    if inside == 1:
        return fmt(c)
    return ("" if c == 1 else f"{fmt(c)} ") + f"sqrt({inside})"


def verdict(a: F, b: F, c: F) -> str:
    h, k, r2 = complete(a, b, c)
    if r2 > 0:
        return f"a circle: {standard(h, k, r2)}, center ({fmt(h)}, {fmt(k)}), radius {root(r2)}"
    if r2 == 0:
        return f"only the point ({fmt(h)}, {fmt(k)}): {standard(h, k, r2)}, radius 0"
    return f"no points at all: {standard(h, k, r2)}, and a sum of squares is never {fmt(r2)}"


def plot(h: int, k: int, r: int, R: int = 6) -> list[str]:
    rows = []
    for y in range(R, -R - 1, -1):
        cells = []
        for x in range(-R, R + 1):
            d2 = (x - h) ** 2 + (y - k) ** 2
            if d2 == r * r:
                cells.append("*")
            elif (x, y) == (h, k):
                cells.append("C")
            elif x == 0 and y == 0:
                cells.append("+")
            elif x == 0:
                cells.append("|")
            elif y == 0:
                cells.append("-")
            else:
                cells.append(".")
        rows.append(f"   {y:>3} " + "".join(f"{c:>3}" for c in cells))
    rows.append("       " + "".join(f"{x:>3}" for x in range(-R, R + 1)) + "   x")
    return rows


def main() -> None:
    print("1. A CIRCLE IS ONE DISTANCE FROM ONE POINT: x^2 + y^2 = 25")
    for line in plot(0, 0, 5):
        print(line)
    pts = [(x, y) for x in range(-5, 6) for y in range(-5, 6) if x * x + y * y == 25]
    print(f"   {len(pts)} whole-number points are exactly 5 from the origin:")
    print("   " + " ".join(f"({x},{y})" for x, y in pts))
    print("   They come from 3-4-5 and 0-5-5: each is a right triangle's hypotenuse of 5.")
    print()

    print("2. STANDARD FORM FROM CENTER AND RADIUS, THEN THE GENERAL FORM")
    for h, k, r in [(F(0), F(0), F(1)), (F(-2), F(3), F(4)), (F(3), F(-1), F(1, 2))]:
        a, b, c = expand(h, k, r * r)
        print(f"   center ({fmt(h)}, {fmt(k)}), r = {fmt(r)}:")
        print(f"      {standard(h, k, r * r):30}  ->  {general(a, b, c)}")
    print("   The sign flips: center (-2, 3) is written (x + 2) and (y - 3).")
    print()

    print("3. BACK AGAIN: COMPLETE THE SQUARE")
    a, b, c = F(4), F(-6), F(12)
    print(f"   {general(a, b, c)}")
    print("   group:     (x^2 + 4x) + (y^2 - 6y) = -12")
    print("   complete:  (x^2 + 4x + 4) + (y^2 - 6y + 9) = -12 + 4 + 9    add (half the coefficient)^2")
    print(f"   so:        {standard(*complete(a, b, c))}")
    print("   center (-2, 3), radius 1. Whatever is added on the left is added on the right.")
    print()

    print("4. NOT EVERY x^2 + y^2 + ax + by + c = 0 IS A CIRCLE")
    for a, b, c in [(F(4), F(-6), F(12)), (F(4), F(-6), F(13)), (F(4), F(-6), F(14)), (F(-1), F(0), F(0))]:
        print(f"   {general(a, b, c):28}  {verdict(a, b, c)}")
    print("   The right side after completing the square is r^2. Positive: a circle.")
    print("   Zero: a single point. Negative: nothing, since squares cannot add to less than 0.")
    print()

    print("5. INSIDE, ON OR OUTSIDE? COMPARE THE SQUARED DISTANCE WITH r^2")
    h, k, r2 = F(-2), F(3), F(16)
    print(f"   circle {standard(h, k, r2)}")
    for x, y in [(2, 3), (0, 0), (1, 6), (-2, 3), (3, 5)]:
        d2 = (x - h) ** 2 + (y - k) ** 2
        where = "on" if d2 == r2 else "inside" if d2 < r2 else "outside"
        print(f"   ({x:>2}, {y}):  (x + 2)^2 + (y - 3)^2 = {fmt(d2):>2}   {where}")
    print()

    print("6. INTERCEPTS OF A CIRCLE: (x - 1)^2 + (y + 2)^2 = 5")
    h, k, r2 = F(1), F(-2), F(5)
    xs = sorted({F(x) for x in range(-10, 11) if (x - h) ** 2 + k * k == r2})
    ys = sorted({F(y) for y in range(-10, 11) if h * h + (y - k) ** 2 == r2})
    print(f"   y = 0: (x - 1)^2 + 4 = 5, (x - 1)^2 = 1, x = {', '.join(fmt(x) for x in xs)}")
    print(f"   x = 0: 1 + (y + 2)^2 = 5, (y + 2)^2 = 4, y = {', '.join(fmt(y) for y in ys)}")
    print("   0 is in both lists, so the circle passes through the origin, since 1 + 4 = 5.")
    print("   A circle can meet an axis twice, once (touching it), or never.")
    print()

    print("7. THE UNIT CIRCLE: CENTER (0, 0), RADIUS 1, x^2 + y^2 = 1")
    for x, y in [(F(1), F(0)), (F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13)), (F(0), F(-1))]:
        print(f"   ({fmt(x):>5}, {fmt(y):>5}):  x^2 + y^2 = {fmt(x * x + y * y)}")
    print("   Every Pythagorean triple a, b, c gives the point (a/c, b/c) on it.")
    print("   Trigonometry will name its points (cos t, sin t).")
    print()

    print("8. A CIRCLE IS A SET OF POINTS, AND A CONTINUOUS ONE")
    on = lambda x, y: x * x + y * y == 1
    print("   membership is a test, like any set builder: (x, y) ∈ circle iff x^2 + y^2 = 1")
    for x, y in [(F(3, 5), F(4, 5)), (F(1, 2), F(1, 2)), (F(0), F(1))]:
        print(f"      ({fmt(x)}, {fmt(y)}) ∈ unit circle: {on(x, y)}")
    print("   a rational point for every fraction t: ((1 - t^2)/(1 + t^2), 2t/(1 + t^2))")
    pts = {((F(1) - t * t) / (F(1) + t * t), 2 * t / (F(1) + t * t)) for t in
           [F(m, n) for n in range(1, 7) for m in range(0, n + 1)]}
    print(f"      {len(pts)} distinct points with t = m/n, n ≤ 6, all on the circle:",
          all(on(x, y) for x, y in pts))
    print("   between any two points of the circle there is a third, so no point has a")
    print("   next point; the fractions t do that on their own:")
    lo, hi = F(0), F(1)
    for _ in range(5):
        mid = (lo + hi) / 2
        x = (F(1) - mid * mid) / (F(1) + mid * mid)
        print(f"      t = {mid}: x = {x} lies between the x's for t = {lo} and t = {hi}")
        hi = mid
    print("   'Continuous' is not a feeling about the drawing but two facts about the set:")
    print("   no gaps (between any two points a third, as above, and every limit of points")
    print("   of the circle is on the circle) and one piece (it cannot be split into two")
    print("   nonempty parts with no point of either touching the other). Both are")
    print("   statements about which points are members. The set is uncountable: t runs")
    print("   through all reals in [0, 1] and so cannot be listed (see cardinality).")


def check(args: list[str]) -> None:
    A, C2, a, b, c = (F(v) for v in args)
    if A != C2 or A == 0:
        sys.exit("x^2 and y^2 must have the same nonzero coefficient, or it is no circle")
    a, b, c = a / A, b / A, c / A
    print(general(a, b, c))
    print(verdict(a, b, c))


if __name__ == "__main__":
    if len(sys.argv) == 6:
        check(sys.argv[1:])
    elif len(sys.argv) == 1:
        main()
    else:
        sys.exit("usage: python3 circles.py [A B a b c]  for  A x^2 + B y^2 + a x + b y + c = 0")
