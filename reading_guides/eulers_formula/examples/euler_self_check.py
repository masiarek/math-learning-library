#!/usr/bin/env python3
"""The answers to the self-check in "Euler's formula: a lesson plan".

Run:  python3 euler_self_check.py

Nine questions, one or two per step of the plan. Try each one before reading
its answer. The first you cannot do names the step to start from.

Exact answers are fractions or integers; the rest are floats printed to six
places.
"""

import math
from fractions import Fraction as F


def mul(z1, z2):
    """The complex-number rule on pairs: (x1 x2 - y1 y2, x1 y2 + x2 y1)."""
    x1, y1 = z1
    x2, y2 = z2
    return (x1 * x2 - y1 * y2, x1 * y2 + x2 * y1)


def fixed(x: float) -> str:
    return f"{round(x, 6) + 0.0:.6f}"


def main() -> None:
    print("1. EXPONENTS (step 1)")
    print(f"   2^3 . 2^4 = {2**3} . {2**4} = {2**3 * 2**4} = 2^7: adding exponents multiplies.")
    print(f"   2^0 . 2^3 must be 2^(0+3) = 2^3, so 2^0 is the number that changes")
    print(f"   nothing when it multiplies: 2^0 = {2**0}.")
    print()

    print("2. THE NUMBER e (step 2)")
    print("   1 in a bank at 100% a year, paid in n instalments of 1/n:")
    for label, n in (("monthly", 12), ("daily", 365), ("every second", 365 * 24 * 3600)):
        print(f"     paid {label:<14} n = {n:<10} (1 + 1/n)^n = {(1 + 1 / n) ** n:.6f}")
    print(f"     {'paid ever more often, the limit':<45}e = {math.e:.6f}")
    print()

    print("3. A COMPLEX NUMBER IS A POINT (steps 3 to 5)")
    z = (3, 2)
    print(f"   3 + 2i is the point {z}. Times i, the point (0, 1): {mul(z, (0, 1))},")
    print("   which is -2 + 3i: the same arrow turned a quarter turn counterclockwise.")
    print()

    print("4. POWERS OF i (step 5)")
    w = (1, 0)
    for k in range(1, 5):
        w = mul(w, (0, 1))
        print(f"   i^{k} = {w}")
    print("   Four quarter turns make a whole turn, back to 1. Two make a half turn: i^2 = -1.")
    print()

    print("5. RADIANS (step 6)")
    print(f"   a quarter turn = pi/2 = {math.pi / 2:.6f} radians, a half turn = pi = {math.pi:.6f}")
    print(f"   From 1 to -1 round the unit circle is half of its length 2 pi: {math.pi:.6f}.")
    print()

    print("6. A VELOCITY AT AN INSTANT (step 7)")
    for h in (F(1, 10), F(1, 1000), F(1, 10**6)):
        print(f"   x = t^2, average velocity over [3, 3 + {h}] = {((3 + h) ** 2 - 9) / h}")
    print("   The averages are exactly 6 + h, and they settle on 6: the velocity at t = 3.")
    print()

    print("7. VELOCITY = 2 . POSITION (step 8)")
    n = 10**5
    stepped = 1.0
    for _ in range(n):
        stepped += 2 * stepped * (0.5 / n)
    print(f"   Start at 1, step to t = 1/2 in {n} steps: position {stepped:.6f}; e = {math.e:.6f}.")
    print("   Exactly e in the limit: twice the velocity is the motion e^t on a clock")
    print("   running twice as fast, so time 1/2 here is time 1 there. d/dt e^(2t) = 2 e^(2t):")
    h = 1e-6
    t = 0.5
    v = (math.exp(2 * (t + h)) - math.exp(2 * t)) / h
    print(f"   measured at t = 1/2, velocity / position = {v / math.exp(2 * t):.6f}")
    print()

    print("8. VELOCITY = POSITION TURNED A QUARTER TURN (step 9)")
    print("   At the start the position is (1, 0) and the velocity is i . (1, 0) =")
    print(f"   {mul((0, 1), (1, 0))}: straight up, length 1. Stepping the motion, 10^6 steps:")
    for label, t in (("pi/2", math.pi / 2), ("pi", math.pi)):
        z = (1.0, 0.0)
        n = 10**6
        dt = t / n
        for _ in range(n):
            v = mul((0.0, 1.0), z)
            z = (z[0] + v[0] * dt, z[1] + v[1] * dt)
        print(f"   t = {label:<5} position ({fixed(z[0])}, {fixed(z[1])})")
    print("   Speed 1 round the circle: a quarter of it, pi/2, reaches i, and half,")
    print("   pi, reaches -1. (The straight steps drift outward by a few millionths.)")
    print()

    print("9. THE SERIES (step 10)")
    terms = [F(1, math.factorial(k)) for k in range(4)]
    print(f"   e^x = 1 + x + x^2/2 + x^3/6 + ...; at x = 1 the first four terms add to")
    print(f"   {' + '.join(str(t) for t in terms)} = {sum(terms)} = {float(sum(terms)):.6f}, already near e = {math.e:.6f}.")


if __name__ == "__main__":
    main()
