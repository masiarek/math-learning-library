#!/usr/bin/env python3
"""The derivative is a velocity: what average velocities settle on.

Run:  python3 derivative_as_velocity.py

A point moves along a number line, and x(t) is where it is at time t. Its
average velocity between t and t + h is the distance covered over the time
taken, (x(t + h) - x(t)) / h. The velocity AT the instant t is the number
those averages settle on as h shrinks. That number is the derivative,
written d/dt x or x'(t).

Sections 1 to 4 compute with exact fractions, so "settles on" can be seen
exactly: for x = t^2 the average over [3, 3 + h] is 6 + h, not nearly but
exactly. Section 5 does the same in floats, where h cannot shrink forever.
"""

from fractions import Fraction as F


def average_velocity(x, t, h):
    return (x(t + h) - x(t)) / h


def steady(t):
    return 5 + 3 * t


def square(t):
    return t * t


def main() -> None:
    print("1. A STEADY MOTION: x(t) = 5 + 3t")
    print("   The average velocity over any stretch of time, long or short:")
    print(f"     {'from t':<8} {'to t + h':<10} {'distance':<10} {'time':<8} average velocity")
    for t, h in ((F(0), F(1)), (F(2), F(1, 2)), (F(7), F(1, 1000))):
        d = steady(t + h) - steady(t)
        print(f"     {str(t):<8} {str(t + h):<10} {str(d):<10} {str(h):<8} {d / h}")
    print("   Always 3. A steady motion has one velocity, and every average finds it.")
    print()

    print("2. A MOTION THAT SPEEDS UP: x(t) = t^2")
    print("   The averages over [3, 3 + h] depend on h:")
    for h in (F(1), F(1, 10), F(1, 100), F(1, 1000), F(1, 10**6)):
        print(f"     h = {str(h):<10} average velocity = {str(average_velocity(square, 3, h)):<14} = 6 + {h}")
    print("   Algebra says why: ((3 + h)^2 - 9) / h = (6h + h^2) / h = 6 + h,")
    print("   exactly. The averages settle on 6, and no single h gives 6 itself:")
    print("   the velocity at the instant t = 3 is 6. At other instants:")
    h = F(1, 1000)
    for t in range(5):
        v = average_velocity(square, t, h)
        print(f"     t = {t}   average over [t, t + 1/1000] = {str(v):<10} settles on {2 * t} = 2t")
    print("   The velocity of t^2 at time t is 2t: the derivative of t^2 is 2t.")
    print()

    print("3. THE NOTATION")
    print("   d/dt x, x'(t) and dx/dt all name the velocity of x at time t, the")
    print("   number the averages (x(t + h) - x(t)) / h settle on as h shrinks:")
    print("     d/dt (5 + 3t) = 3          d/dt t^2 = 2t")
    print("   'd' is for difference: dx is a small change in position, dt a small")
    print("   change in time, and dx/dt their ratio when both are very small.")
    print()

    print("4. STEPPING WITH A VELOCITY")
    print("   Knowing the velocity lets you step forward: over a short time dt the")
    print("   position moves by about velocity . dt. Start x = t^2 at x = 0 and")
    print("   step to t = 3 using only the velocity 2t:")
    for n in (3, 30, 300, 3000):
        dt = F(3, n)
        x = F(0)
        for k in range(n):
            x += 2 * (k * dt) * dt
        print(f"     {n:>5} steps of dt = {str(dt):<7} x reaches {str(x):<12} = {float(x):.4f}")
    print("   The true position is 3^2 = 9. Each step uses the velocity at its")
    print("   start, which is a little too low for a motion that speeds up, and")
    print("   the shortfall is exactly 9/n: smaller steps, smaller error.")
    print()

    print("5. IN FLOATS, THE STEP CANNOT SHRINK FOREVER")
    print("   The same average for t^2 at t = 3, in floating point:")
    print(f"     {'h':<8} {'average velocity':<22} off 6 by")
    for k in range(1, 16):
        h = 10.0**-k
        v = ((3 + h) ** 2 - 9) / h
        print(f"     {'1e-' + str(k):<8} {v:<22.15f} {abs(v - 6):.1e}")
    print("   The error falls with h, then rises again. (3 + h)^2 and 9 agree in")
    print("   more and more leading digits, and subtracting them leaves only the")
    print("   rounding: catastrophic cancellation. Exactly, the error is h; in")
    print("   floats the best h is near 1e-8, and no h gives more than about half")
    print("   the digits of a double.")


if __name__ == "__main__":
    main()
