#!/usr/bin/env python3
"""Area and volume formulas: the exponent of a formula is its dimension.

Run:  python3 area_and_volume_formulas.py

Every formula in the book's box multiplies lengths. A perimeter multiplies
none together, an area multiplies two, a volume three. So if every length is
scaled by k, a perimeter grows by k, an area by k^2 and a volume by k^3, and a
formula that fails that test is misremembered before a single number goes in.
That one check separates the two sphere formulas, 4 pi r^2 and (4/3) pi r^3,
that everyone mixes up.

Answers are kept exact as a + b pi with fractions a and b, the form the book's
answer key prints them in, and rounded only at the end.
"""

import math
from fractions import Fraction as F


class PiNum:
    """An exact number a + b pi, with a and b fractions."""

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, other):
        other = other if isinstance(other, PiNum) else PiNum(other)
        return PiNum(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __sub__(self, other):
        other = other if isinstance(other, PiNum) else PiNum(other)
        return PiNum(self.a - other.a, self.b - other.b)

    def __rsub__(self, other):
        return PiNum(other) - self

    def __mul__(self, k):
        return PiNum(self.a * k, self.b * k)

    __rmul__ = __mul__

    def __float__(self):
        return float(self.a) + float(self.b) * math.pi

    def __str__(self):
        def f(x):
            return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
        const = f(self.a) if self.a else ""
        if not self.b:
            return const or "0"
        coef = "" if self.b == 1 else "-" if self.b == -1 else f(self.b) + " "
        term = f"{coef}pi"
        if not self.a:
            text = term
        elif self.a < 0:
            text = f"{term} - {f(-self.a)}"
        else:
            text = f"{const} + {term}".replace("+ -", "- ")
        return f"{text} = {float(self):.2f}"


PI = PiNum(0, 1)

FORMULAS = [
    # name, what it measures, dimension, function of the lengths
    ("rectangle", "perimeter 2l + 2w", 1, lambda l=4, w=3: 2 * l + 2 * w),
    ("rectangle", "area lw", 2, lambda l=4, w=3: PiNum(l * w)),
    ("triangle", "area bh/2", 2, lambda b=4, h=6: PiNum(F(b * h, 2))),
    ("circle", "circumference 2 pi r", 1, lambda r=2: 2 * r * PI),
    ("circle", "area pi r^2", 2, lambda r=2: r * r * PI),
    ("box", "surface 2lh + 2wh + 2lw", 2, lambda l=4, w=3, h=2: PiNum(2 * l * h + 2 * w * h + 2 * l * w)),
    ("box", "volume lwh", 3, lambda l=4, w=3, h=2: PiNum(l * w * h)),
    ("sphere", "surface 4 pi r^2", 2, lambda r=2: 4 * r * r * PI),
    ("sphere", "volume (4/3) pi r^3", 3, lambda r=2: F(4, 3) * r ** 3 * PI),
    ("cylinder", "surface 2 pi r^2 + 2 pi r h", 2, lambda r=2, h=5: 2 * r * r * PI + 2 * r * h * PI),
    ("cylinder", "volume pi r^2 h", 3, lambda r=2, h=5: r * r * h * PI),
]


def scaled(fn, k):
    """Call fn with every default length multiplied by k."""
    defaults = fn.__defaults__
    return fn(*[d * k for d in defaults])


def main() -> None:
    print("1. DOUBLE EVERY LENGTH, AND EACH FORMULA SAYS ITS OWN DIMENSION")
    print(f"   {'shape':10}{'formula':30}{'at size 1':>20}{'at size 2':>20}{'ratio':>7}")
    for shape, name, dim, fn in FORMULAS:
        one, two = fn(), scaled(fn, 2)
        ratio = F(float(two) / float(one)).limit_denominator(100)
        print(f"   {shape:10}{name:30}{float(one):>20.4f}{float(two):>20.4f}{str(ratio):>7}")
    print("   Perimeters and circumferences double, areas and surfaces grow 4 = 2^2,")
    print("   volumes grow 8 = 2^3. The ratio is 2 raised to the number of lengths")
    print("   multiplied together, whatever the constant in front.")
    print()

    print("2. WHAT THE TEST CATCHES, AND WHAT IT CANNOT: PROBLEMS 6 AND 9")
    print("   'The surface area of a sphere of radius r is (4/3) pi r^2.'")
    wrong = lambda r=2: F(4, 3) * r * r * PI
    print(f"   At r = 2 it gives {wrong()}; at r = 4, {scaled(wrong, 2)}.")
    print("   Ratio 4: it has the shape of an area, so far so good.")
    print("   The dimension test cannot see a constant. The right one is 4, not 4/3:")
    print("   a sphere of radius 1 fits in a cylinder of radius 1 and height 2, whose")
    print(f"   side has area 2 pi r h = {4 * PI}, and Archimedes showed that the")
    print("   sphere's surface is exactly that. False.")
    print("   For the volume, 4 pi r^2 and 4 pi r^3 (choices d and c of problem 6): the first")
    print("   is an area, so the test rejects it. The second passes the test, but a sphere")
    print("   inside a cube of side 2r must hold less than the cube's 8 r^3,")
    print(f"   and 4 pi = {4 * math.pi:.2f} is more than 8. Only (4/3) pi = {4 / 3 * math.pi:.2f} fits.")
    print()

    print("3. THE SURFACE IS WHAT THE VOLUME GAINS PER UNIT OF RADIUS")
    print("   Put a skin of thickness t on a sphere of radius 3 and weigh the skin:")
    V = lambda r: F(4, 3) * r ** 3 * PI
    for t in [F(1), F(1, 10), F(1, 100), F(1, 1000)]:
        skin = V(3 + t) - V(3)
        print(f"     t = {str(t):7} skin volume / t = {float(skin) / float(t):10.4f}")
    print(f"   The skin per unit thickness settles on 4 pi 3^2 = {4 * 9 * math.pi:.4f}, the surface area.")
    print("   The same for a circle: a ring of width t has area about 2 pi r t,")
    print("   the circumference times the width. Each formula is the rate of the next one up.")
    print()

    print("4. THE BOOK'S PROBLEMS 27-38, EXACT FIRST, ROUNDED LAST")
    problems = [
        ("27", "rectangle 6 by 7 in, area", PiNum(6 * 7)),
        ("28", "rectangle 9 by 4 cm, area", PiNum(9 * 4)),
        ("29", "triangle h 14, b 4 in, area", PiNum(F(14 * 4, 2))),
        ("30", "triangle h 9, b 4 cm, area", PiNum(F(9 * 4, 2))),
        ("31", "circle r 5 m, area", 25 * PI),
        ("31", "circle r 5 m, circumference", 10 * PI),
        ("32", "circle r 2 ft, area", 4 * PI),
        ("32", "circle r 2 ft, circumference", 4 * PI),
        ("33", "box 6 x 8 x 5 ft, volume", PiNum(6 * 8 * 5)),
        ("33", "box 6 x 8 x 5 ft, surface", PiNum(2 * 6 * 5 + 2 * 8 * 5 + 2 * 6 * 8)),
        ("34", "box 9 x 4 x 8 in, volume", PiNum(9 * 4 * 8)),
        ("34", "box 9 x 4 x 8 in, surface", PiNum(2 * 9 * 8 + 2 * 4 * 8 + 2 * 9 * 4)),
        ("35", "sphere r 5 cm, volume", F(4, 3) * 125 * PI),
        ("35", "sphere r 5 cm, surface", 4 * 25 * PI),
        ("36", "sphere r 3 ft, volume", F(4, 3) * 27 * PI),
        ("36", "sphere r 3 ft, surface", 4 * 9 * PI),
        ("37", "cylinder r 9, h 8 in, volume", 81 * 8 * PI),
        ("37", "cylinder r 9, h 8 in, surface", 2 * 81 * PI + 2 * 9 * 8 * PI),
        ("38", "cylinder r 8, h 9 in, volume", 64 * 9 * PI),
        ("38", "cylinder r 8, h 9 in, surface", 2 * 64 * PI + 2 * 8 * 9 * PI),
    ]
    for num, what, val in problems:
        print(f"     {num}  {what:32} {val}")
    print("   Problem 32 is a coincidence worth noticing: at r = 2 the area 4 pi and the")
    print("   circumference 4 pi are the same number, in different units. Area/circumference")
    print("   is r/2, so it happens only at r = 2, and only because units were dropped.")
    print("   37 and 38 swap r and h: the volumes differ (648 pi against 576 pi), because")
    print("   r is squared and h is not.")
    print()

    print("5. SHADED REGIONS: PROBLEMS 39-42, A SQUARE OF SIDE 2 AND A CIRCLE")
    print("   Inscribed circle: radius 1. Circumscribed circle: radius = half the diagonal,")
    print("   and the diagonal of a 2 by 2 square is sqrt(2^2 + 2^2) = sqrt(8), so r^2 = 2.")
    for num, what, val in [
        ("39", "circle inside the square", 1 * PI),
        ("40", "square minus the circle inside it", 4 - PI),
        ("41", "circle around the square", 2 * PI),
        ("42", "circle minus the square inside it", 2 * PI - 4),
    ]:
        print(f"     {num}  {what:36} {val}")
    print("   The whole region is always a sum or difference of pieces with formulas.")
    print()

    print("6. APPLICATIONS: EXAMPLE 4 AND PROBLEMS 47-51")
    print(f"     Ex 4  ornament: triangle b 4, h 6, plus semicircle r 2   {PiNum(12) + F(1, 2) * 4 * PI} cm^2")
    print(f"     47    wheel, diameter 16 in, 4 turns: 4 * 16 pi          {4 * 16 * PI} in")
    print(f"     48    disk, diameter 4 ft, rolled 20 ft: 20 / (4 pi)     {20 / (4 * math.pi):.2f} turns")
    print(f"     49    border: outer square 6 + 2 + 2 = 10, minus inner   {PiNum(100 - 36)} ft^2")
    print(f"     50    squares of area 100 and 16: legs 10 - 4 = 6 and 4   {PiNum(F(6 * 4, 2))} ft^2")
    print(f"     51    Norman window 4 by 6 plus semicircle r 2, area      {PiNum(24) + F(1, 2) * 4 * PI} ft^2")
    print(f"     51    its frame: 6 + 4 + 6 plus the arc, half of 4 pi    {PiNum(16) + 2 * PI} ft")
    print("   A turn of a wheel moves it one circumference, pi d, not 2 pi d: the")
    print("   diameter is given, so the circumference is pi d.")


if __name__ == "__main__":
    main()
