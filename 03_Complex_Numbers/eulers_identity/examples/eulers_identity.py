#!/usr/bin/env python3
"""Euler's identity: what e^(i pi) = -1 means, why it must hold, and what it is for.

Run:  python3 eulers_identity.py

Once the exponent stops being a whole number, e^x is no longer "e multiplied
by itself x times". It is compounding, (1 + x/n)^n with n growing without
bound, and the one law that survives from repeated multiplication is

    e^(a + b) = e^a . e^b          adding inputs multiplies outputs.

Compound an imaginary number and nothing new is needed: 1 + i t/n is the pair
(1, t/n), and multiplying by it turns the plane by a small angle and stretches
it by almost nothing. Do it n times and the stretches fade while the turns add
up to t. So e^(i t) is the unit point at angle t, in radians,

    e^(i t) = (cos t, sin t)       Euler's formula,

and the point half a turn from (1, 0) is (-1, 0): e^(i pi) = -1.

Section 3 is the same thing as motion, the way Grant Sanderson's talk
"Designing Math" (Config 2026) tells it: e^(kt) is a position whose velocity
is k times itself, and for k = i the velocity is the position turned a
quarter turn, so the point goes round the circle. One small step of that
motion is one factor of the compounding.

The pair rule mul() is the one from the previous lessons. pi is not a
fraction, so the compounding runs in floats; the half turn itself is reached
exactly in section 5, with fractions and a symbolic sqrt(3), by cutting it
into quarter, sixth, eighth and twelfth turns. Sections 4, 6 and 7 use cmath,
the standard library's complex exponential, and section 8 the power series.
"""

import cmath
import math
from decimal import Decimal
from fractions import Fraction as F

# pi to 40 digits, for section 6, where the question is how far math.pi is from it.
PI_40 = "3.141592653589793238462643383279502884197"


class Root3:
    """An exact number a + b sqrt(3), with a and b fractions.

    (a + b r)(c + d r) = (ac + 3bd) + (ad + bc) r,   because r r = 3.
    """

    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def of(x):
        return x if isinstance(x, Root3) else Root3(x)

    def __add__(self, o):
        o = Root3.of(o)
        return Root3(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        o = Root3.of(o)
        return Root3(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return Root3.of(o) - self

    def __mul__(self, o):
        o = Root3.of(o)
        return Root3(self.a * o.a + 3 * self.b * o.b, self.a * o.b + self.b * o.a)

    __radd__ = __add__
    __rmul__ = __mul__

    def __eq__(self, o):
        o = Root3.of(o)
        return (self.a, self.b) == (o.a, o.b)

    def __hash__(self):
        return hash((self.a, self.b))

    def __str__(self):
        a, b = self.a, self.b
        if b == 0:
            return str(a)
        if a == 0:
            return root_part(b)
        return f"{a} {'-' if b < 0 else '+'} {root_part(abs(b))}"


def root_part(b: F) -> str:
    """b sqrt(3), written the way a person would: sqrt(3)/2, -sqrt(3)."""
    sign = "-" if b < 0 else ""
    b = abs(b)
    num = "" if b.numerator == 1 else str(b.numerator)
    den = "" if b.denominator == 1 else f"/{b.denominator}"
    return f"{sign}{num}sqrt(3){den}"


R = Root3


def mul(z1, z2):
    """The pair rule, unchanged from the previous lessons: (x1 x2 - y1 y2, x1 y2 + x2 y1).

    It only asks that the coordinates add, subtract and multiply, so it works
    on integers, fractions, numbers with a sqrt(3) in them, and floats.
    """
    x1, y1 = z1
    x2, y2 = z2
    return (x1 * x2 - y1 * y2, x1 * y2 + x2 * y1)


def add(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])


def power(z, n):
    """z multiplied by itself n times, by repeated squaring so that n = 10^6 is quick."""
    result = (1, 0)
    while n:
        if n & 1:
            result = mul(result, z)
        z = mul(z, z)
        n >>= 1
    return result


def length_squared(z):
    x, y = z
    return x * x + y * y


def show(z) -> str:
    """An exact pair, as it is."""
    return f"({z[0]}, {z[1]})"


def fixed(x: float, d: int) -> str:
    """A float to d decimals, with -0.0000 written as 0.0000."""
    return f"{round(x, d) + 0.0:.{d}f}"


def showf(z, d: int) -> str:
    """A float pair, rounded to d decimals."""
    return f"({fixed(z[0], d)}, {fixed(z[1], d)})"


def main() -> None:
    print("1. e ON THE REAL LINE IS COMPOUNDING")
    print("   e^3 is e . e . e, and e^(1/2) or e^pi is not e multiplied by itself")
    print("   some number of times; e^(pi i) even less. What defines e^x for every x")
    print("   is compounding,")
    print("   (1 + x/n)^n with n growing without bound. At x = 1:")
    for n in (1, 2, 3, 4):
        v = (1 + F(1, n)) ** n
        print(f"     n = {n:<8} {f'(1 + 1/{n})^{n}':<18} = {str(v):<12} = {float(v):.9f}")
    for n, label in ((12, "12"), (365, "365"), (10**6, "10^6")):
        v = (1 + 1 / n) ** n
        print(f"     n = {label:<8} {f'(1 + 1/{label})^{label}':<18}   {'':<12} = {v:.9f}")
    print(f"     {'e':<46} = {math.e:.9f}")
    print("   The one thing repeated multiplication leaves behind is its law,")
    print("   e^(a + b) = e^a . e^b: adding inputs multiplies outputs.")
    e = [math.exp(k) for k in range(4)]
    print("     " + "   ".join(f"e^{k} = {e[k]:.6f}" for k in range(4)))
    print("   Add 1 to the input and the output is multiplied by e, every time:")
    print("     " + "   ".join(f"e^{k + 1} / e^{k} = {e[k + 1] / e[k]:.6f}" for k in range(3)))
    print("   The question of this page: what should adding i to the input do?")
    print()

    print("2. COMPOUNDING AN IMAGINARY NUMBER")
    print("   1 + i t/n is the pair (1, t/n), and raising it to the n-th power")
    print("   needs nothing but the pair rule. At t = 1, exactly in fractions:")
    for n in range(1, 5):
        z = power((F(1), F(1, n)), n)
        print(f"     n = {n}   (1 + i/{n})^{n} = {show(z):<22} |z|^2 = {length_squared(z)}")
    print("   The squared length is (1 + 1/n^2)^n, a little above 1 and falling")
    print("   toward it, and the points are heading somewhere: (cos 1, sin 1) is")
    print(f"   ({math.cos(1):.6f}, {math.sin(1):.6f}). At t = pi, which is not a fraction, in floats:")
    print(f"     {'n':<10} {'(1 + i pi/n)^n':<32} {'length':<12} angle / pi")
    for n in (1, 2, 3, 4, 10, 100, 10**4, 10**6):
        z = power((1.0, math.pi / n), n)
        r = math.sqrt(length_squared(z))
        a = math.atan2(z[1], z[0]) / math.pi
        print(f"     {n:<10} {showf(z, 7):<32} {r:<12.6f} {a:.8f}")
    print("   The length falls to 1 and the angle climbs to pi: the point is")
    print("   settling on (-1, 0). Each factor (1, pi/n) is a small stretch and a")
    print("   small turn, and lesson 2 says what n of them do: the stretches")
    print("   multiply and the turns add.")
    n = 10**6
    t = math.pi / n
    print(f"     one factor, n = 10^6:  stretch sqrt(1 + (pi/n)^2)   = {math.sqrt(1 + t * t):.13f}")
    print(f"                            turn    atan(pi/n)           = {math.atan(t):.13f} rad")
    print(f"     all n of them:         stretch (1 + (pi/n)^2)^(n/2) = {(1 + t * t) ** (n / 2):.8f}   -> 1")
    print(f"                            turn    n atan(pi/n)         = {n * math.atan(t):.8f}   -> pi")
    print()

    print("3. THE SAME THING AS MOTION: VELOCITY IS k TIMES POSITION")
    print("   Read e^(kt) as a point that moves as the time t runs, starting at")
    print("   e^0 = 1. Its velocity, d/dt e^(kt), is k times its position, and k")
    print("   says what that does to the arrow:")
    print("     k = 1      velocity = position               grows")
    print("     k = 2      velocity = 2 . position           doubled: grows faster")
    print("     k = -0.5   velocity = -0.5 . position        flipped and squished: shrinks")
    print("     k = i      velocity = i . position           turned 90 degrees")
    print("   Multiplying by i is lesson 2's quarter turn. On a + bi, the a becomes")
    print("   ai and the bi becomes bi . i = -b:")
    print(f"     (3, 2) . i = {show(mul((3, 2), (0, 1)))}          and (1, 0) . i = {show(mul((1, 0), (0, 1)))}")
    print("   Move in small steps. Over a time dt the point moves by velocity . dt:")
    print("     z  ->  z + (k z) dt  =  z (1 + k dt)")
    print("   so n steps of dt = t/n multiply the start by (1 + k t/n)^n. That is")
    print("   the compounding of sections 1 and 2: each factor is one small step of")
    print("   motion. With n = 10^6 steps, at the moments the talk stops on:")
    n = 10**6
    print(f"     {'k':<6} {'t':<6} {'n small steps':<30} e^(kt), from exp")
    for label, k, t in (("1", 1.0, 1.0), ("2", 2.0, 0.29), ("-0.5", -0.5, 0.60)):
        stepped = (1 + k * t / n) ** n
        print(f"     {label:<6} {t:<6.2f} {stepped:<30.6f} {math.exp(k * t):.6f}")
    for t in (3.14, math.pi):
        stepped = power((1.0, t / n), n)
        exact = cmath.exp(1j * t)
        tl = "pi" if t == math.pi else f"{t:.2f}"
        print(f"     {'i':<6} {tl:<6} {showf(stepped, 6):<30} {showf((exact.real, exact.imag), 6)}")
    print("   The talk's screen shows 1.78..., 0.74... and -1.00 + 0.00i at these")
    print("   moments, with t rounded to two decimals. For k = i the velocity is")
    print("   the position turned a quarter turn, so it is always at right angles")
    print("   to it and exactly as long:")
    print(f"     {'t':<6} {'position':<24} {'velocity = i . position':<26} {'position . velocity':<21} |velocity|")
    for tl, t in (("0", 0.0), ("pi/4", math.pi / 4), ("pi/2", math.pi / 2),
                  ("3pi/4", 3 * math.pi / 4), ("pi", math.pi)):
        w = cmath.exp(1j * t)
        z = (w.real, w.imag)
        v = mul((0, 1), z)
        dot = z[0] * v[0] + z[1] * v[1]
        print(f"     {tl:<6} {showf(z, 6):<24} {showf(v, 6):<26} {fixed(dot, 6):<21} {math.sqrt(length_squared(v)):.6f}")
    print("   A velocity at right angles to the position moves the point round the")
    print("   origin and never toward it or away. A velocity of length 1 covers a")
    print("   distance of 1 per unit of time. So at time t the point has walked a")
    print("   distance t around the unit circle, and at t = pi it has walked half")
    print("   of it, 2 pi / 2, to (-1, 0). Each straight step cuts the corner of the")
    print("   circle a little, which is the stretch section 2 measured, and the")
    print("   cut vanishes as the steps shrink.")
    print()

    print("4. WHY pi, AND NOT 180: THE UNIT OF ANGLE")
    print("   The turn that n factors add up to is n atan(t/n), and it tends to t")
    print("   itself. A point of the unit circle turned through an angle t travels")
    print("   a distance t along the circle exactly when angles are measured in")
    print("   radians, so that is the unit e^(i t) comes in: e^(i t) is the unit")
    print("   point at t radians, e^(i t) = (cos t, sin t). Python's cmath agrees:")
    for label, t in (("1", 1.0), ("2", 2.0), ("pi", math.pi), ("10", 10.0)):
        w = cmath.exp(1j * t)
        same = w == complex(math.cos(t), math.sin(t))
        print(f"     t = {label:<4} cmath.exp(1j t) = {showf((w.real, w.imag), 10):<32} = (cos t, sin t): {same}")
    print("   Half a turn is pi radians, a full turn 2 pi, and 180 is 180 radians,")
    print(f"   which is {180 / (2 * math.pi):.2f} turns and lands nowhere special:")
    for label, t, note in (
        ("e^(i pi/2)", math.pi / 2, "a quarter turn:  i"),
        ("e^(i pi)  ", math.pi, "a half turn:    -1"),
        ("e^(2 pi i)", 2 * math.pi, "a full turn:     1"),
        ("e^(180 i) ", 180.0, f"180 radians, {180 / (2 * math.pi):.2f} turns"),
    ):
        w = cmath.exp(1j * t)
        print(f"     {label} = {showf((w.real, w.imag), 10):<32} {note}")
    print()

    print("5. THE HALF TURN, EXACTLY")
    print("   Euler's formula says e^(i t) is the unit point at angle t radians, so")
    print("   e^(i pi) is the point half a turn from (1, 0). A half turn can be cut")
    print("   into equal turns that are exact, and the pair rule does the rest with")
    print("   no float in sight:")
    quarter = (F(0), F(1))
    sixth = (R(F(1, 2)), R(0, F(1, 2)))
    eighth_times_root2 = (1, 1)
    twelfth = (R(0, F(1, 2)), R(F(1, 2)))
    e4 = power(eighth_times_root2, 4)
    print(f"     {'the turn':<19} {'e^(i pi/k), exactly':<22} taken k times")
    print(f"     {'2 quarter turns':<19} {show(quarter):<22} {show(quarter)}^2 = {show(power(quarter, 2))}")
    print(f"     {'3 sixth turns':<19} {show(sixth):<22} {show(sixth)}^3 = {show(power(sixth, 3))}")
    print(f"     {'4 eighth turns':<19} {'(1, 1) / sqrt(2)':<22} (1, 1)^4 / (sqrt(2))^4 = {show(e4)} / 4 = {show((F(e4[0], 4), F(e4[1], 4)))}")
    print(f"     {'6 twelfth turns':<19} {show(twelfth):<22} {show(twelfth)}^6 = {show(power(twelfth, 6))}")
    print(f"     {'12 twelfth turns':<19} {show(twelfth):<22} {show(twelfth)}^12 = {show(power(twelfth, 12))}   a full turn: e^(2 pi i) = 1")
    print("   Every half turn is (-1, 0) exactly. e^(i pi) = -1 is i^2 = -1 with")
    print("   the quarter turn cut finer: the point (0, 1) is e^(i pi/2), the twelve")
    print("   marks of the clock face are e^(i pi k/6), and the n-th roots of unity")
    print("   of the previous lesson are e^(2 pi i k/n).")
    print()

    print("6. HOW IT IS USED: EVERY POINT IS r e^(i theta)")
    print("   A nonzero pair has a length r and an angle theta, so it is r times the")
    print("   unit point at theta: r e^(i theta), the polar form. cmath.polar reads")
    print("   r and theta off a point and cmath.rect puts them back:")
    a, b = complex(3, 4), complex(5, 12)
    ra, ta = cmath.polar(a)
    rb, tb = cmath.polar(b)
    rab, tab = cmath.polar(a * b)
    print(f"     {'z':<14} {'r':<8} theta")
    print(f"     {'(3, 4)':<14} {ra:<8.1f} {ta:.10f}")
    print(f"     {'(5, 12)':<14} {rb:<8.1f} {tb:.10f}")
    print(f"     {'(-33, 56)':<14} {rab:<8.1f} {tab:.10f}   their product")
    print(f"     {ra:.0f} x {rb:.0f} = {ra * rb:.0f}, and {ta:.10f} + {tb:.10f} = {ta + tb:.10f}")
    back = cmath.rect(rab, tab)
    print(f"     cmath.rect({rab:.0f}, {tab:.10f}) = {showf((back.real, back.imag), 10)}")
    print("   Lengths multiply and angles add, the two halves of lesson 2, and")
    print("   they are now one line, the law of exponents:")
    print("     r1 e^(i a) . r2 e^(i b) = r1 r2 e^(i (a + b))")
    print("   De Moivre's formula is the same line n times over, (e^(i t))^n =")
    print("   e^(i n t), and the angle-addition formulas for cos(a + b) and")
    print("   sin(a + b) are its two coordinates.")
    print()

    print("7. IN A PROGRAM THE ANSWER IS NOT -1, AND THE ERROR IS pi - math.pi")
    w = cmath.exp(1j * math.pi)
    print(f"     cmath.exp(1j * math.pi)       = {w!r}")
    print(f"     cmath.exp(1j * math.pi) == -1 : {w == -1}")
    print(f"     cmath.exp(1j * math.pi) + 1   = {w + 1!r}")
    print("   The identity is exact and the program is not wrong. math.pi is a")
    print("   double, and the double nearest pi falls a little short of it:")
    pi_exact = Decimal(PI_40)
    pi_double = Decimal(math.pi)
    print(f"     math.pi        = {str(pi_double)[:26]}...   the double, written out")
    print(f"     pi             = {PI_40[:26]}...")
    print(f"     pi - math.pi   = {pi_exact - pi_double:.16e}")
    print(f"     sin(math.pi)   = {math.sin(math.pi)!r}")
    print("   e^(i math.pi) stops 1.22e-16 radians before the half turn, and at")
    print("   that distance along the circle it sits 1.22e-16 above the axis. The")
    print("   whole error is in the input, and none of it in the exponential.")
    print(f"     cmath.isclose(cmath.exp(1j * math.pi), -1): {cmath.isclose(w, -1)}")
    print()

    print("8. THE SERIES, THE WAY A COURSE PROVES IT")
    print("   Calculus writes e^x = 1 + x + x^2/2! + x^3/3! + ... and puts x = i pi")
    print("   in. The powers of i cycle through the four compass points, (1, 0),")
    print("   (0, 1), (-1, 0), (0, -1), so the even terms are real with alternating")
    print("   signs, the series of cos pi, and the odd terms are imaginary, the")
    print("   series of sin pi. Each term is the one before it times pi i / k:")
    print("   turned a quarter turn, and scaled by pi/k. Laid end to end, the terms")
    print("   are the talk's spiral of arrows:")
    directions = ("right", "up", "left", "down")
    print(f"     {'k':>2}   {'term (pi i)^k / k!':<20} {'length pi^k/k!':<16} {'points':<8} sum of terms 0 to k")
    term = (1.0, 0.0)
    total = (0.0, 0.0)
    for k in range(25):
        if k > 0:
            term = mul(term, (0.0, math.pi / k))
        total = add(total, term)
        if k <= 10 or k % 4 == 0:
            name = {0: "1", 1: "pi i"}.get(k, f"(pi^{k}/{k}!) i^{k}")
            length = math.pi**k / math.factorial(k)
            print(f"     {k:>2}   {name:<20} {length:<16.6f} {directions[k % 4]:<8} {showf(total, 6)}")
    print("   The arrows grow while pi/k is more than 1, up to the term k = 3, and")
    print("   shrink ever faster after it, so the spiral winds in, onto (-1, 0):")
    print("   the same point the compounding found, reached by a different road.")


if __name__ == "__main__":
    main()
