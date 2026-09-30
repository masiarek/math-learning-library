#!/usr/bin/env python3
"""e^t is the motion whose velocity always equals its position.

Run:  python3 velocity_equals_position.py

Start a point at 1 on the number line and let it move so that its velocity
is always equal to its position: at 1 it moves at speed 1, at 2 at speed 2.
Where is it at time t? That position is e^t, and e itself is where the
point is at t = 1. Everything else follows from the rule:

    velocity = position              e^t, and e^0 = 1
    velocity = k . position          e^(kt), the same motion on a clock k times as fast
    start twice as far               every position twice as far, so e^(a+b) = e^a . e^b

Steps of the motion are computed with exact fractions; e^t itself is not a
fraction, so the comparisons with math.exp are floats, printed to six places.
"""

import math
from fractions import Fraction as F


def step(x0, k, t, n):
    """n small steps of time t/n, each moving the position by k . position . dt."""
    x = x0
    dt = t / n
    for _ in range(n):
        x = x + k * x * dt
    return x


def measured_velocity(f, t, h=1e-6):
    return (f(t + h) - f(t)) / h


def main() -> None:
    print("1. START AT 1, AND ALWAYS MOVE AS FAST AS YOUR POSITION")
    print("   Over a short time dt the point moves by velocity . dt = position . dt,")
    print("   so each step multiplies the position by (1 + dt). Steps of 1/n up")
    print("   to t = 1 multiply 1 by (1 + 1/n), n times:")
    for n in (1, 2, 3, 4):
        x = step(F(1), 1, F(1), n)
        print(f"     {n:>7} steps   position {str(x):<10} = {float(x):.6f}")
    for n in (10, 100, 1000, 10**5):
        x = (1 + 1 / n) ** n
        print(f"     {n:>7} steps   position {'':<10} = {x:.6f}")
    print(f"     {'e':>7}         {'':<19} = {math.e:.6f}")
    print("   The steps are compounding, (1 + 1/n)^n, and they settle on e: e is")
    print("   where the point is at time 1. Its position at time t is called e^t.")
    print()

    print("2. THE POSITION AT OTHER TIMES")
    print(f"     {'t':<6} {'10^5 steps':<14} e^t, from math.exp")
    for t in (0.0, 0.5, 1.0, 2.0, -1.0):
        print(f"     {t:<6} {step(1.0, 1, t, 10**5):<14.6f} {math.exp(t):.6f}")
    print("   At t = 0 the point has not moved: e^0 = 1. For t = -1 the steps run")
    print("   backwards in time and the point is at 1/e.")
    print()

    print("3. MEASURED: THE VELOCITY OF e^t IS e^t")
    print("   The average velocity over [t, t + 0.000001], and the position:")
    print(f"     {'t':<6} {'velocity':<12} {'position':<12} velocity / position")
    for t in (0.0, 1.0, 2.0, 3.0):
        v = measured_velocity(math.exp, t)
        print(f"     {t:<6} {v:<12.6f} {math.exp(t):<12.6f} {v / math.exp(t):.6f}")
    print("   d/dt e^t = e^t. That is the whole definition, with e^0 = 1.")
    print()

    print("4. THE LAW OF EXPONENTS, FROM THE MOTION")
    print("   Every step multiplies the position by the same factor, wherever the")
    print("   point is, so a start twice as far gives a position twice as far at")
    print("   every time. Run for a time a, and the point is at e^a. The rest of")
    print("   the motion is the motion from 1, scaled by e^a, so after a further")
    print("   time b it is at e^a . e^b. It has run for a + b: e^(a+b) = e^a . e^b.")
    a, b = F(3, 10), F(5, 10)
    whole = step(F(1), 1, a + b, 8)
    first = step(F(1), 1, a, 3)
    rest = step(first, 1, b, 5)
    print(f"   Exactly, in steps of 1/10: 8 steps from 1 reach {whole},")
    print(f"   3 steps then 5 more reach {rest}: equal: {whole == rest}.")
    print(f"   With math.exp: e^0.3 . e^0.5 = {math.exp(0.3) * math.exp(0.5):.6f}, e^0.8 = {math.exp(0.8):.6f}.")
    print("   Adding times multiplies positions. That is why e^x can be given")
    print("   inputs that are not whole numbers, and, in the complex-numbers")
    print("   chapter, inputs that are not real.")
    print()

    print("5. VELOCITY = k . POSITION: DOUBLE, OR FLIP AND SQUISH")
    print("   Let the velocity be k times the position. The motion is the same")
    print("   motion with the clock running k times as fast, so its position at")
    print("   time t is e^(kt), and every velocity is k times as large:")
    print(f"     {'k':<6} {'t':<6} {'position e^(kt)':<17} {'measured velocity':<19} velocity / position")
    for k, t in ((2.0, 0.29), (2.0, 1.0), (-0.5, 0.60), (-0.5, 2.0)):
        f = lambda s, k=k: math.exp(k * s)
        v = measured_velocity(f, t)
        print(f"     {k:<6g} {t:<6.2f} {f(t):<17.6f} {v:<19.6f} {v / f(t):.6f}")
    print("   k = 2 doubles the velocity: the point runs away twice as fast. k = -0.5")
    print("   flips the velocity to point back toward 0 and squishes it to half the")
    print("   position: the point creeps toward 0 and never reaches it. The factor")
    print("   k in d/dt e^(kt) = k e^(kt) is the chain rule: speeding up the clock")
    print("   by k multiplies every velocity by k.")


if __name__ == "__main__":
    main()
