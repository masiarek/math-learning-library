#!/usr/bin/env python3
"""Related rates: two quantities tied by an equation have velocities tied by its derivative.

Run:  python3 related_rates.py

If r and V are tied at every instant by V = (4/3) pi r^3, then as time runs
both move, and their velocities are tied too: dV/dt = 4 pi r^2 dr/dt. Every
related-rates problem is that step and nothing else: write the equation that
holds at every instant, differentiate it in t, and only then put the numbers
of the one instant you were asked about.

Each answer here is computed twice. Once from the differentiated formula, and
once without any calculus at all: the program lets the motion run, measures
the asked-for quantity a millionth of a second either side of the instant,
and divides, which is what a velocity is (lesson 1 of this chapter). When the
two agree to six figures, the formula was right.
"""

import math

H = 1e-6  # the time step for measured velocities, as in lesson 1


def measured(f, t=0.0):
    """Velocity of f at time t, measured: (f(t + H) - f(t - H)) / 2H."""
    return (f(t + H) - f(t - H)) / (2 * H)


def row(label, formula_value, measured_value, unit):
    ok = abs(formula_value - measured_value) <= 1e-6 * max(1.0, abs(formula_value))
    return f"   {label:44}{formula_value:>13.6f}{measured_value:>13.6f}  {unit:9}{'agree' if ok else 'DIFFER'}"


HEADER = f"   {'':44}{'formula':>13}{'measured':>13}  {'unit':9}"


def main() -> None:
    print("1. ONE EQUATION AT EVERY INSTANT, SO ONE EQUATION BETWEEN VELOCITIES")
    print("   Each formula, differentiated in t, checked at r = 3 (or a = 3, x = 3, y = 4)")
    print("   with every length growing at 1 unit per second:")
    print(HEADER)
    checks = [
        ("A = pi r^2        ->  2 pi r r'", lambda t: math.pi * (3 + t) ** 2, 2 * math.pi * 3, "per sec"),
        ("V = (4/3) pi r^3  ->  4 pi r^2 r'", lambda t: 4 / 3 * math.pi * (3 + t) ** 3, 4 * math.pi * 9, "per sec"),
        ("S = 4 pi r^2      ->  8 pi r r'", lambda t: 4 * math.pi * (3 + t) ** 2, 8 * math.pi * 3, "per sec"),
        ("V = a^3           ->  3 a^2 a'", lambda t: (3 + t) ** 3, 27.0, "per sec"),
        ("C = 2 pi r        ->  2 pi r'", lambda t: 2 * math.pi * (3 + t), 2 * math.pi, "per sec"),
        ("z = sqrt(x^2+y^2) ->  (x x' + y y')/z", lambda t: math.hypot(3 + t, 4 + t), (3 + 4) / 5, "per sec"),
        ("theta = atan(y/x) ->  (x y' - y x')/(x^2+y^2)", lambda t: math.atan2(4 + t, 3 + t), (3 - 4) / 25, "rad/sec"),
    ]
    for label, f, exact, unit in checks:
        print(row(label, exact, measured(f), unit))
    print("   Each factor in front of r' is what the quantity gains per unit of r:")
    print("   4 pi r^2 is the sphere's surface, 2 pi r the circle's circumference.")
    print()

    print("2. CIRCLES, SPHERES AND CUBES")
    print(HEADER)
    probs = [
        # label, formula value, the motion (quantity asked, as a function of t), unit
        ("circle r=5, r'=2: A' = 2 pi r r'", 2 * math.pi * 5 * 2,
         lambda t: math.pi * (5 + 2 * t) ** 2, "m^2/s"),
        ("circle r=6, r'=-1: A' = 2 pi r r'", 2 * math.pi * 6 * -1,
         lambda t: math.pi * (6 - t) ** 2, "ft^2/s"),
        ("balloon V'=2, r=3: r' = V'/(4 pi r^2)", 2 / (4 * math.pi * 9),
         lambda t: (3 * (4 / 3 * math.pi * 27 + 2 * t) / (4 * math.pi)) ** (1 / 3), "cm/s"),
        ("balloon V'=100, r=10: r' = V'/(4 pi r^2)", 100 / (4 * math.pi * 100),
         lambda t: (3 * (4 / 3 * math.pi * 1000 + 100 * t) / (4 * math.pi)) ** (1 / 3), "cm/s"),
        ("snowball V'=-5, r=4: r' = V'/(4 pi r^2)", -5 / (4 * math.pi * 16),
         lambda t: (3 * (4 / 3 * math.pi * 64 - 5 * t) / (4 * math.pi)) ** (1 / 3), "cm/min"),
        ("cube a=4, a'=1/2: V' = 3 a^2 a'", 3 * 16 * 0.5,
         lambda t: (4 + 0.5 * t) ** 3, "m^3/s"),
        ("cube V'=-10, a=2: a' = V'/(3 a^2)", -10 / 12,
         lambda t: (8 - 10 * t) ** (1 / 3), "m/s"),
        ("cube a=5, a'=-2: V' = 3 a^2 a'", 3 * 25 * -2,
         lambda t: (5 - 2 * t) ** 3, "cm^3/s"),
        ("sphere r=10, r'=-3: S' = 8 pi r r'", 8 * math.pi * 10 * -3,
         lambda t: 4 * math.pi * (10 - 3 * t) ** 2, "m^2/s"),
        ("circle r=7, r'=4: C' = 2 pi r'", 2 * math.pi * 4,
         lambda t: 2 * math.pi * (7 + 4 * t), "cm/s"),
    ]
    for label, value, f, unit in probs:
        print(row(label, value, measured(f), unit))
    r = 1 / (2 * math.sqrt(math.pi))
    print("   Sphere with r' = 9: when do V and r grow at the same numerical rate?")
    print(f"   4 pi r^2 * 9 = 9 gives r^2 = 1/(4 pi), r = {r:.6f} cm; there V' = {4 * math.pi * r * r * 9:.6f} = r'.")
    print("   Negative answers mean decreasing: the snowball's radius shrinks.")
    print()

    print("3. WHY THE NUMBERS GO IN LAST")
    print("   Balloon, r = 3. Put r = 3 in first: V = (4/3) pi 3^3 = 36 pi, a constant,")
    print("   and the derivative of a constant is 0. So 2 = 0: nonsense, not a small error.")
    print("   r = 3 is true at one instant only. An equation that holds for one instant")
    print("   has no velocity in it; only an equation that holds at every instant can be")
    print("   differentiated. Differentiate first, then freeze the instant.")
    print()

    print("4. LADDERS AND TWO TRAVELLERS")
    print("   x^2 + y^2 = L^2 at every instant, so 2x x' + 2y y' = 0, and y' = -x x'/y.")
    print(HEADER)
    lad = [
        ("ladder 25, pushed in at 1, x=15 (y=20)", -15 * -1 / 20, lambda t: math.sqrt(625 - (15 - t) ** 2), "ft/s"),
        ("ladder 13, slides out at 2, x=5 (y=12)", -5 * 2 / 12, lambda t: math.sqrt(169 - (5 + 2 * t) ** 2), "ft/s"),
        ("ladder 10, slides out at 1, x=6 (y=8)", -6 * 1 / 8, lambda t: math.sqrt(100 - (6 + t) ** 2), "ft/s"),
    ]
    for label, value, f, unit in lad:
        print(row(label, value, measured(f), unit))
    print("   For two travellers leaving one point at right angles, z^2 = x^2 + y^2:")
    trav = [
        ("cyclists E 16, N 12 mph, after 1 h", 16, 12, 1),
        ("cars S 30, W 40 mph, after 2 h", 30, 40, 2),
        ("planes E 250, N 300 mi/h, after 1 h", 250, 300, 1),
    ]
    for label, u, v, T in trav:
        x, y = u * T, v * T
        z = math.hypot(x, y)
        value = (x * u + y * v) / z
        print(row(label, value, measured(lambda t: math.hypot(u * t, v * t), T), "per hour"))
    print()

    print("5. WHICH RATE STAYS THE SAME? THE WORKSHEET'S 'COMPARE' QUESTION")
    print("   Ladder 25 pushed in at 1 ft/s from x = 20 (t in seconds), and the cyclists")
    print("   (t in hours, distance in miles):")
    print(f"     {'t':>4}{'ladder x':>10}{'top speed':>11}   {'cyclists apart':>15}{'rate':>7}")
    for t in [0, 2, 5, 10, 14]:
        x = 20 - t
        y = math.sqrt(625 - x * x)
        print(f"     {t:>4}{x:>10}{x / y:>11.4f}   {20 * t if t else 0:>15}{20:>7}")
    print("   The ladder's length is fixed, so as x shrinks the top slows: x/y falls from")
    print("   4/3 to 0.23. The cyclists' triangle keeps its shape (16t, 12t, 20t, always")
    print("   similar to 4-3-5), so the distance is 20t and its rate is 20 at every moment.")
    print()

    print("6. ANGLES")
    print("   theta' = (x y' - y x')/(x^2 + y^2), the angle's velocity seen from the corner.")
    print(HEADER)
    ang = [
        ("ladder 20, x=12, x'=2 (y=16)", 12, 16, 2, -12 * 2 / 16,
         lambda t: math.acos((12 + 2 * t) / 20)),
        ("ladder 15, x=9, x'=1 (y=12)", 9, 12, 1, -9 * 1 / 12,
         lambda t: math.acos((9 + t) / 15)),
        ("kite 80 up, x=60, x'=5", 60, 80, 5, 0, lambda t: math.atan2(80, 60 + 5 * t)),
        ("kite 50 up, x=120, x'=3", 120, 50, 3, 0, lambda t: math.atan2(50, 120 + 3 * t)),
        ("balloon 30 away, y=40, y'=4", 30, 40, 0, 4, lambda t: math.atan2(40 + 4 * t, 30)),
        ("balloon 40 away, y=30, y'=6", 40, 30, 0, 6, lambda t: math.atan2(30 + 6 * t, 40)),
    ]
    for label, x, y, dx, dy, f in ang:
        value = (x * dy - y * dx) / (x * x + y * y)
        print(row(label, value, measured(f), "rad/s"))
    print("   Exactly: the ladders -1/8 and -1/12, the kites -1/25 and -3/338,")
    print("   the balloons 6/125 and 12/125 radians per second. Radians, because")
    print("   lesson 3 showed that only in radians is the derivative of sin cos.")
    print()

    print("7. WHERE THE MODEL BREAKS: THE TOP OF A SLIDING LADDER")
    print("   Ladder 13 sliding out at 2 ft/s. The top's speed 2x/y, as y goes to 0:")
    for x in [5, 12, 12.9, 12.99, 12.999]:
        y = math.sqrt(169 - x * x)
        print(f"     x = {x:<7} y = {y:8.4f}   top falls at {2 * x / y:10.2f} ft/s")
    print("   The formula promises unbounded speed at the floor. A real ladder leaves the")
    print("   wall before then; the equation x^2 + y^2 = 169 stops describing it.")


if __name__ == "__main__":
    main()
