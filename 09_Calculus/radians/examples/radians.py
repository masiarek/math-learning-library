#!/usr/bin/env python3
"""Radians: the unit in which an angle is the distance walked round the circle.

Run:  python3 radians.py

On the unit circle, the point at angle t is (cos t, sin t). Measure t in
radians and t is also the length of the arc from (1, 0) to that point, so a
point that walks round the circle at speed 1 is at angle t at time t. Every
other unit breaks that, by a constant factor: in degrees the factor is
pi/180, and it turns up in every velocity and every derivative.

Section 1 measures the circle with Archimedes' polygons and no pi at all;
the rest uses math.cos and math.sin, printed to six places.
"""

import math


def polygon_perimeters(doublings):
    """Perimeters of regular 6, 12, 24, ... -gons inscribed in the unit circle.

    The hexagon's side is 1, the radius. Halving the angle of a side gives
    the side of the polygon with twice as many: s' = s / sqrt(2 + sqrt(4 - s^2)),
    the form that does not subtract nearly equal numbers.
    """
    n, s = 6, 1.0
    out = []
    for _ in range(doublings + 1):
        out.append((n, n * s))
        s = s / math.sqrt(2 + math.sqrt(4 - s * s))
        n *= 2
    return out


def arc_by_chords(t, n):
    """Walk from angle 0 to angle t in n equal steps along chords, and add up the steps."""
    total = 0.0
    x0, y0 = 1.0, 0.0
    for k in range(1, n + 1):
        x1, y1 = math.cos(t * k / n), math.sin(t * k / n)
        total += math.hypot(x1 - x0, y1 - y0)
        x0, y0 = x1, y1
    return total


def fixed(x: float) -> str:
    """Six decimals, with -0.000000 written as 0.000000."""
    return f"{round(x, 6) + 0.0:.6f}"


def pair(z) -> str:
    return f"({fixed(z[0])}, {fixed(z[1])})"


def main() -> None:
    print("1. HOW LONG IS THE CIRCLE? ARCHIMEDES' POLYGONS")
    print("   Regular polygons inside the circle of radius 1, sides doubled each")
    print("   time, starting from the hexagon, whose side is the radius:")
    for n, p in polygon_perimeters(10):
        if n <= 96 or n == 6 * 2**10:
            print(f"     {n:>5} sides   perimeter = {p:.6f}   half of it = {p / 2:.6f}")
    print(f"   The perimeters settle on 2 pi = {2 * math.pi:.6f}. The whole circle is")
    print("   2 pi long, half of it pi, a quarter pi/2.")
    print()

    print("2. A RADIAN IS THE ANGLE WHOSE ARC IS ONE RADIUS LONG")
    print("   Measure an angle by the length of arc it cuts from the unit circle:")
    print(f"     {'turn':<12} {'degrees':<9} {'radians':<9} as a number")
    for name, frac in (("a quarter", 0.25), ("a half", 0.5), ("a whole", 1.0)):
        rad = {0.25: "pi/2", 0.5: "pi", 1.0: "2 pi"}[frac]
        print(f"     {name:<12} {360 * frac:<9g} {rad:<9} {2 * math.pi * frac:.6f}")
    print(f"     {'1 radian':<12} {math.degrees(1):<9.4f} {'1':<9} 1.000000")
    print("   One radian is a little under 60 degrees: the arc as long as the")
    print("   radius. It is not a round number of degrees because 2 pi is not")
    print("   a round number.")
    print()

    print("3. IN RADIANS, THE ANGLE IS THE DISTANCE WALKED")
    print("   Walk from (1, 0) to the point at angle t in n straight steps along")
    print("   the circle, and add up the steps:")
    print(f"     {'n':<6} {'t = 1':<12} {'t = pi/2':<12} t = pi")
    for n in (1, 2, 4, 10, 100, 1000):
        a, b, c = (arc_by_chords(t, n) for t in (1.0, math.pi / 2, math.pi))
        print(f"     {n:<6} {a:<12.6f} {b:<12.6f} {c:.6f}")
    print(f"     {'t':<6} {1.0:<12.6f} {math.pi / 2:<12.6f} {math.pi:.6f}")
    print("   The walk settles on t itself. That is what radians are for: the")
    print("   point at angle t has walked a distance t from (1, 0).")
    print()

    print("4. THE VELOCITY OF A TURNING POINT")
    print("   Let the point be at angle t at time t: position (cos t, sin t). Its")
    print("   velocity, measured over the time from t - 0.000001 to t + 0.000001:")
    h = 1e-6
    print(f"     {'t':<6} {'position':<24} {'velocity':<24} {'|velocity|':<12} position . velocity")
    for label, t in (("0", 0.0), ("1", 1.0), ("pi/2", math.pi / 2), ("pi", math.pi)):
        p = (math.cos(t), math.sin(t))
        v = ((math.cos(t + h) - math.cos(t - h)) / (2 * h),
             (math.sin(t + h) - math.sin(t - h)) / (2 * h))
        dot = p[0] * v[0] + p[1] * v[1]
        print(f"     {label:<6} {pair(p):<24} {pair(v):<24} {math.hypot(*v):<12.6f} {fixed(dot)}")
    print("   The velocity is (-sin t, cos t): the position turned a quarter turn,")
    print("   at right angles to it, and of length 1. In radians,")
    print("     d/dt cos t = -sin t        d/dt sin t = cos t")
    print("   Measure the same turning in degrees, the point at angle d degrees at")
    print("   time d, and every velocity shrinks by the same factor:")
    d = 30.0
    v = ((math.cos(math.radians(d + h)) - math.cos(math.radians(d - h))) / (2 * h),
         (math.sin(math.radians(d + h)) - math.sin(math.radians(d - h))) / (2 * h))
    print(f"     at d = 30:  |velocity| = {math.hypot(*v):.6f}    pi/180 = {math.pi / 180:.6f}")
    print("   so in degrees d/dd sin = (pi/180) cos, with a constant that radians")
    print("   make 1.")
    print()

    print("5. sin(x) / x FOR A SMALL ANGLE")
    print(f"     {'x':<10} {'in radians':<14} x in degrees")
    for x in (0.1, 0.01, 0.001):
        rad = math.sin(x) / x
        deg = math.sin(math.radians(x)) / x
        print(f"     {x:<10} {rad:<14.6f} {deg:.6f}")
    print(f"   In radians a small sine is its angle, and the ratio settles on 1;")
    print(f"   in degrees it settles on pi/180 = {math.pi / 180:.6f}. A small arc is almost")
    print("   straight, and its height is its length, only when the angle IS the")
    print("   length.")


if __name__ == "__main__":
    main()
