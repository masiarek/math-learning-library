#!/usr/bin/env python3
"""Probability zero is not impossible -- and a computer never draws a real number.

Run:  python3 probability_zero.py

In the model, a uniform random number X in [0,1] lands in an interval with
probability equal to the interval's length. So a set of measure zero is an
event of probability zero -- including events that happen.

The last sections leave the model for the machine. The generator is seeded,
and random() is documented to produce the same sequence from the same seed
across Python versions, so the draws below are the same on every run.
"""

import math
import random
import struct
from fractions import Fraction as F


def main() -> None:
    print("1. THE MODEL: PROBABILITY IS LENGTH")
    print("   X is a uniform random number in [0,1]. For any interval,")
    print("   P(X lands in it) = the interval's length.")
    for lo, hi in [(F(0), F(1, 3)), (F(1, 4), F(3, 4)), (F(9, 10), F(1))]:
        print(f"     P({lo} <= X <= {hi}) = {hi - lo}")
    print()

    print("2. ONE EXACT VALUE")
    print("   If X = 1/2, then X is inside every interval around 1/2:")
    for d in [F(1, 10), F(1, 1000), F(1, 10**6), F(1, 10**12)]:
        print(f"     P(X = 1/2)  <=  P(X within {str(d):<15} of 1/2) = {2 * d}")
    print("   P(X = 1/2) is at most every one of these numbers, so it is 0.")
    print("   Nothing about 1/2 was special: every single value has probability 0.")
    print()

    print("3. BUT X HAS TO LAND SOMEWHERE")
    print("   Every value has probability 0, and every draw produces one of them.")
    print("   So an event of probability 0 happens on every single draw:")
    print("     probability 0   does not mean   impossible")
    print("     probability 1   does not mean   certain -- it means ALMOST SURELY")
    print()
    print("   It is also why probabilities add up over a LIST of events and no")
    print("   further: [0,1] is made of its points, every point has probability 0,")
    print("   and the whole of [0,1] has probability 1.")
    print()

    print("4. MEASURE ZERO MEANS PROBABILITY ZERO")
    print("   A set inside intervals of total length eps has probability at most")
    print("   eps. A measure-zero set does that for EVERY eps, so:")
    print("     X is rational            measure 0   probability 0")
    print("     X is in the Cantor set   measure 0   probability 0")
    print("     X is irrational          measure 1   probability 1: almost surely")
    print("   Yet 1/2 is rational, 1/4 is in the Cantor set, and both are possible.")
    print()

    print("5. WHAT A COMPUTER ACTUALLY DRAWS")
    rng = random.Random(2026)
    steps = 2**53
    print("   Five draws from random.random(), seeded, as exact multiples of 2^-53:")
    for _ in range(5):
        x = rng.random()
        k = F(x) * steps
        assert k.denominator == 1
        print(f"     {x!r:<20} = {k.numerator:>21,} / 2^53")
    print(f"   Every draw is a whole number of 2^-53 steps, so random() has exactly")
    print(f"   2^53 = {steps:,} possible values. A finite set.")
    print()
    below_one = struct.unpack("<Q", struct.pack("<d", 1.0))[0]
    assert below_one == 1023 * 2**52
    print(f"   Doubles in [0, 1): {below_one:,} = 1023 x 2^52.")
    print("   random() can return 2^53 of them -- 2 in every 1023. The rest are")
    print("   never drawn, and 0.1 is one of the rest:")
    for text, v in [("0.5", 0.5), ("0.1", 0.1)]:
        k = F(v) * steps
        on_grid = k.denominator == 1
        print(f"     {text} is stored as {F(v)!s:<35} a multiple of 2^-53? {'yes' if on_grid else 'no'}")
    print()

    print("6. THE SAME QUESTIONS, ON THE MACHINE")
    p = F(1, steps)
    repeat = math.sqrt(math.pi / 2 * steps)
    print(f"     P(random() == 0.5)          = 1/2^53 = {float(p):.3e}   not 0")
    print(f"     P(two draws are equal)      = 1/2^53 = {float(p):.3e}   not 0")
    print(f"     P(random() == 0.1)          = 0, and here 0 IS impossible")
    print(f"     P(random() is rational)     = 1, and certain: every float is a fraction")
    print(f"     draws until a repeat        about {round(repeat / 1e6)} million on average")
    print()

    print("7. TWO WORLDS, BOTH RIGHT")
    print("   the model:    X is almost surely irrational, and P(X = 0.5) = 0")
    print("   the machine:  every draw is rational, and P(random() == 0.5) = 1/2^53")
    print("   With finitely many outcomes, probability 0 means impossible again --")
    print("   the subtlety needs a continuum. And since every finite set has measure")
    print("   zero, the model gives 'X is a float' probability 0. The machine lives")
    print("   entirely inside an event of probability zero.")


if __name__ == "__main__":
    main()
