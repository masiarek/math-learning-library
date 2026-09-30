#!/usr/bin/env python3
"""Congruent and similar triangles: which three measurements fix a triangle.

Run:  python3 congruent_and_similar_triangles.py

A triangle has six measurements, three sides and three angles, and the book's
three congruence cases say that three of them are enough, if they are the
right three. This program builds the triangle from each set of three, the way
a ruler and protractor would, and counts how many different triangles fit:

    SSS, SAS, ASA        exactly one      so equal data means congruent
    AAA                  infinitely many  one shape, any size: similar
    SSA                  sometimes two    which is why no book lists it

Building a triangle from an angle needs cosines and sines, which the book
reaches in its trigonometry chapters; here they are only the machinery. Every
triangle is named by its sides a, b, c and the angles A, B, C opposite them,
and printed to two decimals. The similarity ratios in sections 4-6 are exact
fractions.
"""

import math
from fractions import Fraction as F


def deg(x: float) -> float:
    return math.degrees(x)


def rad(x: float) -> float:
    return math.radians(x)


def from_sss(a, b, c):
    """Three sides: each angle from the law of cosines, c^2 = a^2 + b^2 - 2ab cos C."""
    A = deg(math.acos((b * b + c * c - a * a) / (2 * b * c)))
    B = deg(math.acos((a * a + c * c - b * b) / (2 * a * c)))
    return (a, b, c, A, B, 180 - A - B)


def from_sas(b, C, a):
    """Two sides and the angle between them: the third side, then SSS."""
    c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(rad(C)))
    return from_sss(a, b, c)


def from_asa(A, c, B):
    """Two angles and the side between them: the third angle, then the law of sines."""
    C = 180 - A - B
    k = c / math.sin(rad(C))
    return (k * math.sin(rad(A)), k * math.sin(rad(B)), c, A, B, C)


def from_ssa(a, b, A):
    """Sides a and b and the angle A opposite a, not between them. Zero, one or two triangles."""
    s = b * math.sin(rad(A)) / a
    if s > 1:
        return []
    out = []
    for B in {round(deg(math.asin(s)), 12), round(180 - deg(math.asin(s)), 12)}:
        C = 180 - A - B
        if C > 0:
            c = a * math.sin(rad(C)) / math.sin(rad(A))
            out.append((a, b, c, A, B, C))
    return sorted(out)


def show(t) -> str:
    a, b, c, A, B, C = t
    return f"sides {a:6.2f} {b:6.2f} {c:6.2f}   angles {A:6.2f} {B:6.2f} {C:6.2f}"


def ratio(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    print("1. THREE MEASUREMENTS THAT FIX A TRIANGLE: FIGURE 18")
    print("   Each set of three is fed to the construction; one triangle comes out.")
    print("     (a) ASA: angles 80 and 40, side 10 between them")
    print("         " + show(from_asa(80, 10, 40)))
    print("     (b) SSS: sides 15, 20, 8")
    print("         " + show(from_sss(15, 20, 8)))
    print("     (c) SAS: sides 7 and 8, angle 40 between them")
    print("         " + show(from_sas(7, 40, 8)))
    print("   The other three measurements are forced. Two triangles with the same")
    print("   three data are therefore the same triangle in two places: congruent.")
    print()

    print("2. THREE ANGLES DO NOT FIX A TRIANGLE: PROBLEM 5")
    print("   Angles 30, 50, 100 (Figure 17), with the side between 30 and 50 set to 1, 2, 5:")
    for c in [1, 2, 5]:
        print("         " + show(from_asa(30, c, 50)))
    print("   Same angles, sides in the ratio 1 : 2 : 5. The angles fix the shape and")
    print("   nothing else, so Angle-Angle-Angle is the answer to problem 5: it is not a")
    print("   case for congruence. It is the first case for similarity.")
    print("   And the third angle is never news: it is 180 minus the other two, so AAA")
    print("   is really only two measurements.")
    print()

    print("3. TWO SIDES AND AN ANGLE NOT BETWEEN THEM: THE CASE THAT IS MISSING")
    print("   Side a = 8 opposite a 40 degree angle A, and side b = 10:")
    for t in from_ssa(8, 10, 40):
        print("         " + show(t))
    print("   Two different triangles fit the same three data: side a can swing to")
    print("   meet the base in two places. So Side-Side-Angle is not a congruence case,")
    print("   unless the angle is 90 degrees, where the swing has one place to land:")
    for t in from_ssa(13, 5, 90):
        print("         " + show(t))
    print("   That special case is Pythagoras: two sides of a right triangle fix the third.")
    print("   With a = 5 too short to reach, no triangle fits at all:")
    print(f"         {len(from_ssa(5, 10, 40))} triangles")
    print()

    print("4. SIMILAR MEANS ONE RATIO FOR EVERY PAIR OF SIDES: FIGURES 19 AND 20")
    for name, pairs in [
        ("Figure 19  d/a, e/b, f/c", [(F(2), F(1)), (F(2), F(1)), (F(2), F(1))]),
        ("Figure 20b 10/30, 5/15, 6/18", [(F(10), F(30)), (F(5), F(15)), (F(6), F(18))]),
        ("Figure 20c 4/6, 12/18 (SAS)", [(F(4), F(6)), (F(12), F(18))]),
    ]:
        rs = [ratio(p / q) for p, q in pairs]
        print(f"     {name:30} ratios {', '.join(rs)}")
    print("   Every ratio is the same number, the scale factor. Lengths multiply by it.")
    print()

    print("5. EXAMPLE 5 AND PROBLEMS 43-46: FIND x AND THE ANGLES")
    print("   Match the sides by the angles they sit between, then one ratio gives x.")
    rows = [
        # name, a side of the first triangle, its match in the second, the
        # first triangle's side that matches x, and the angles A, B, C
        ("Ex 5", F(3), F(5), F(6), (90, 60, 30)),
        ("43", F(4), F(8), F(2), (90, 60, 30)),
        ("44", F(12), F(6), F(16), (30, 75, 75)),
        ("45", F(20), F(30), F(45), (60, 95, 25)),
        ("46", F(10), F(8), F(50), (50, 125, 5)),
    ]
    print(f"     {'':6}{'known pair':>12}{'scale k':>9}{'matches x':>11}{'x = k * side':>14}   A, B, C")
    for name, first, second, other, (A, B, C) in rows:
        k = second / first
        x = other * k
        xs = ratio(x) if x.denominator == 1 else f"{ratio(x)} = {float(x)}"
        print(f"     {name:6}{f'{ratio(first)} -> {ratio(second)}':>12}{ratio(k):>9}{ratio(other):>11}{xs:>14}   {A}, {B}, {C}")
    print("   The angles are copied, not computed: similar triangles have equal angles.")
    print("   Only a length needs the scale factor.")
    print()

    print("6. TRUE OR FALSE: PROBLEMS 10-12")
    print("     10  sides 30, 29, 10 and 30, 29, 10: all three equal, SSS: congruent. True.")
    print("     11  angles 25 and 100 in both: two equal angles, AA: similar. True.")
    r1, r2 = F(4, 3), F(3, 2)
    print(f"     12  120 between 3 and 2, and between 4 and 3: ratios 4/3 = {float(r1):.4f}")
    print(f"         and 3/2 = {float(r2):.4f} differ, so SAS fails: not similar. False.")
    print("         Try the other pairing, 4/2 and 3/3: 2 and 1, worse.")
    print()

    print("7. A SCALE FACTOR k MULTIPLIES AREA BY k^2")
    for k in [F(2), F(3), F(1, 2)]:
        a, b = F(3), F(4)  # legs of a 3-4-5 right triangle, area ab/2
        area, big = a * b / 2, (k * a) * (k * b) / 2
        print(f"     legs 3, 4 scaled by {ratio(k):>3}: area {ratio(area)} -> {ratio(big):>3}, ratio {ratio(big / area)}")
    print("   Similar triangles with sides in the ratio 1 : 3 have areas in the ratio 1 : 9.")


if __name__ == "__main__":
    main()
