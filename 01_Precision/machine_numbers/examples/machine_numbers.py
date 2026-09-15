#!/usr/bin/env python3
"""Machine numbers: a computer swaps the real line for a finite set.

Run:  python3 machine_numbers.py

Four parameters choose the set -- the radix, the precision, and the smallest
and largest exponent -- and every operation is the exact real operation
followed by a jump to the nearest member. Sections 1-4 build a system small
enough to print whole, and test the laws of arithmetic against every member of
it. Sections 5-7 show that the float in front of you is the same construction
with bigger parameters.

The toy system is computed with Fractions, so it is exact. The float results
are correctly rounded by IEEE 754, so they are the same on every machine.
"""

from __future__ import annotations

import decimal
import math
import struct
import sys
from bisect import bisect_left
from decimal import ROUND_DOWN, ROUND_HALF_EVEN, Context, Decimal
from fractions import Fraction as F


class System:
    """The number system F(beta, p, emin, emax), rounding to nearest, ties to even.

    A positive member is M x beta^(e - p + 1) for a whole-number significand M.
    Normal members use all p digits, beta^(p-1) <= M < beta^p, at every
    exponent from emin to emax. Subnormal members are the shorter significands
    0 < M < beta^(p-1), allowed at emin only: they fill the hole at zero.
    """

    def __init__(self, beta: int, p: int, emin: int, emax: int, subnormals: bool = True):
        significand = {F(0): 0}
        for e in range(emin, emax + 1):
            for m in range(beta ** (p - 1), beta**p):
                significand[m * F(beta) ** (e - p + 1)] = m
        if subnormals:
            for m in range(1, beta ** (p - 1)):
                significand[m * F(beta) ** (emin - p + 1)] = m
        self.significand = significand
        self.positive = sorted(significand)  # zero and up
        self.members = sorted({-x for x in significand} | set(significand))
        self.largest = self.positive[-1]
        self.top_gap = F(beta) ** (emax - p + 1)

    def round(self, x: F, mode: str = "RN_even") -> F | None:
        """x rounded into the set by one of the five IEEE 754 rounding functions.

        RD toward -infinity, RU toward +infinity, RZ toward zero, and the two
        round-to-nearest functions, which differ only on a tie: RN_even takes
        the even significand, RN_away the larger magnitude. None means the
        result is an infinity, with the sign of x.
        """
        if x < 0:
            r = self.round(-x, {"RD": "RU", "RU": "RD"}.get(mode, mode))
            return None if r is None else -r
        if x > self.largest:
            lo, hi = self.largest, None
        else:
            i = bisect_left(self.positive, x)
            hi = self.positive[i]
            if hi == x:
                return x
            lo = self.positive[i - 1]
        if mode in ("RD", "RZ"):
            return lo
        if mode == "RU":
            return hi
        # Past the largest member, "nearest" is measured against beta^(emax+1),
        # the first number that is not there -- which is where infinity takes over.
        hi_value = self.largest + self.top_gap if hi is None else hi
        if x - lo != hi_value - x:
            return lo if x - lo < hi_value - x else hi
        if mode == "RN_away":
            return hi
        return lo if self.significand[lo] % 2 == 0 else hi


def show(x: F | None) -> str:
    """A fraction as a terminating decimal when it has one, else as p/q."""
    if x is None:
        return "overflow"
    d = x.denominator
    if d & (d - 1):
        return f"{x.numerator}/{d}"
    return format(Decimal(x.numerator) / Decimal(d), "f")


def ruler(system: System) -> str:
    """Every multiple of 1/8 from 0 to 7: '|' where a member sits, '.' where none does."""
    return "".join("|" if F(k, 8) in system.significand else "." for k in range(57))


def section_1(toy_n: System) -> None:
    print("1. FOUR NUMBERS PICK A SET")
    print("   A toy system, small enough to print whole:")
    print("     radix beta = 2    precision p = 3 digits    exponent e from -1 to 2")
    print("   A member is  d0.d1d2 (in binary) x 2^e,  with d0 = 1:")
    print()
    print("     significand  " + "".join(f"{'e = ' + str(e):>9}" for e in range(-1, 3)))
    for m in range(4, 8):
        bits = format(m, "b")
        label = f"{bits[0]}.{bits[1:]} = {show(F(m, 4))}"
        row = "".join(f"{show(m * F(2) ** (e - 2)):>9}" for e in range(-1, 3))
        print(f"       {label:<11}{row}")
    positive = len(toy_n.positive) - 1
    print()
    print(f"   {positive} positive, {positive} negative and zero: {len(toy_n.members)} members.")
    print(f"   Per sign: (beta - 1) x beta^(p-1) x (number of exponents) = 1 x 4 x 4 = {1 * 4 * 4}.")
    print(f"   Largest {show(toy_n.largest)}, smallest positive {show(toy_n.positive[1])}.")
    print("   Every other real number -- 0.1, 1/3, 0.51, pi -- is simply not in the set.")
    print()


def section_2(toy_n: System, toy: System) -> None:
    print("2. THE GAPS GROW WITH THE NUMBERS")
    print("   Every multiple of 1/8 from 0 to 7, marked where a member sits:")
    print()
    print("     " + "".join(f"{n:<8}" for n in range(8)).rstrip())
    print("     " + ruler(toy_n))
    print()
    print("   Between one power of 2 and the next, the members are evenly spaced:")
    for e in range(-1, 3):
        lo = F(2) ** e
        hi = min(2 * lo, toy_n.largest)
        print(f"     from {show(lo):>3} to {show(hi):<3}   gap {show(F(2) ** (e - 2))}")
    normal = toy_n.positive[1:]
    relative = [(b - a) / a for a, b in zip(normal, normal[1:])]
    lo_r, hi_r = min(relative), max(relative)
    print("   The gap doubles when the number doubles, so the gap RELATIVE to the")
    print(f"   number stays between {lo_r.numerator}/{lo_r.denominator} and "
          f"{hi_r.numerator}/{hi_r.denominator} everywhere. A float keeps a fixed")
    print("   number of significant digits, never a fixed number of decimal places.")
    print()
    print("   THE HOLE AT ZERO. Below 0.5 there is nothing but 0. So two different")
    print("   members can have a difference too small to be a member:")
    print(f"     0.625 (-) 0.5  =  round(0.125)  =  {show(toy_n.round(F(1, 8)))}"
          "      although 0.625 != 0.5")
    print("   IEEE 754 fills the hole with SUBNORMALS: d0 = 0 is allowed at e = -1.")
    print()
    print("     " + ruler(toy))
    print()
    print(f"     0.625 (-) 0.5  =  round(0.125)  =  {show(toy.round(F(1, 8)))}")
    positive = len(toy.positive) - 1
    print(f"   From here on the toy system has them: {positive} per sign, {len(toy.members)} members.")
    print()


MODES = ["RD", "RU", "RZ", "RN_even", "RN_away"]


def section_3(toy: System) -> None:
    print("3. ROUNDING IS A FUNCTION, AND IEEE 754 DEFINES FIVE")
    print("   Each one sends every real number to a member, or to an infinity:")
    print("     RD toward -inf    RU toward +inf    RZ toward zero")
    print("     RN to nearest, a tie going to the EVEN significand or AWAY from zero")
    print()
    print("     x          " + "".join(f"{m:<10}" for m in MODES).rstrip())
    for x in [F(1, 10), F(1, 3), F(13, 8), F(-13, 8), F(29, 4), F(15, 2), F(1, 32)]:
        cells = []
        for mode in MODES:
            r = toy.round(x, mode)
            cells.append(("-inf" if x < 0 else "+inf") if r is None else show(r))
        print(f"     {show(x):<11}" + "".join(f"{c:<10}" for c in cells).rstrip())
    print()
    print("   1.625 is a tie: 1.5 = 1.10 ends in 0 and 1.75 = 1.11 does not.")
    print("   7.5 is half a gap past the largest member, so both RNs overflow.")
    print()

    grid = [F(k, 64) for k in range(-8 * 64, 8 * 64 + 1)]

    def value(r: F | None, sign: int):
        return sign * math.inf if r is None else r

    sandwich = nearest_is_a_side = toward_zero = True
    for x in grid:
        rd, ru, rz = toy.round(x, "RD"), toy.round(x, "RU"), toy.round(x, "RZ")
        sandwich &= value(rd, -1) <= x <= value(ru, 1)
        nearest_is_a_side &= all(toy.round(x, m) in (rd, ru) for m in ("RN_even", "RN_away"))
        toward_zero &= rz == (rd if x >= 0 else ru)
    print(f"   Checked on every multiple of 1/64 from -8 to 8 ({len(grid):,} values):")
    print(f"     RD(x) <= x <= RU(x)                                {sandwich}")
    print(f"     both RNs always return RD(x) or RU(x)              {nearest_is_a_side}")
    print(f"     RZ(x) is RD(x) when x >= 0, and RU(x) when x < 0   {toward_zero}")
    print()

    print("   Python's float only ever uses RN even. Its decimal module has all five:")
    decimal_modes = [("FLOOR", "RD"), ("CEILING", "RU"), ("DOWN", "RZ"),
                     ("HALF_EVEN", "RN_even"), ("HALF_UP", "RN_away")]
    print("     x      " + "".join(f"{'ROUND_' + name:<16}" for name, _ in decimal_modes).rstrip())
    for text in ["2.5", "-2.5", "2.4"]:
        cells = [str(Decimal(text).quantize(Decimal(1), rounding=getattr(decimal, "ROUND_" + name)))
                 for name, _ in decimal_modes]
        print(f"     {text:<7}" + "".join(f"{c:<16}" for c in cells).rstrip())
    print("   (ROUND_HALF_UP is the decimal module's name for ties away from zero.)")
    print()
    print("   An operation is the exact result, then a rounding function:")
    print("     a (+) b = RN(a + b),  and the same for (-), (x) and (/).")
    print(f"     1.25 (+) 0.625 = RN(1.875) = {show(toy.round(F(15, 8)))}"
          f"      0.125 (x) 0.25 = RN(0.03125) = {show(toy.round(F(1, 32)))}")
    print("   From here on, every operation rounds to nearest, ties to even.")
    print()


def section_4(toy: System, toy_n: System) -> None:
    print("4. WHICH LAWS OF ARITHMETIC SURVIVE")
    xs = toy.members
    n = len(xs)
    r = toy.round

    def table(system: System, op) -> list[list[int | None]]:
        where = {x: i for i, x in enumerate(system.members)}
        rows = []
        for a in system.members:
            row = []
            for b in system.members:
                c = system.round(op(a, b))
                row.append(None if c is None else where[c])
            rows.append(row)
        return rows

    add = table(toy, lambda a, b: a + b)
    mul = table(toy, lambda a, b: a * b)
    sub = table(toy, lambda a, b: a - b)
    at = {x: i for i, x in enumerate(xs)}
    zero, one = at[F(0)], at[F(1)]
    pairs = [(i, j) for i in range(n) for j in range(n)]
    triples = [(i, j, k) for i in range(n) for j in range(n) for k in range(n)]

    print(f"   Tested on every member ({n}), every pair ({len(pairs):,}) and every triple")
    print(f"   ({len(triples):,}) of the toy system. Cases where a step overflows are skipped.")
    print()

    def report(law: str, fails: int, checked: int, what: str, example: str) -> None:
        print(f"   {law}")
        word = "holds" if fails == 0 else "FAILS"
        print(f"       {word}: {fails:,} failures in {checked:,} {what}")
        if fails:
            print(f"       {example}")

    def tally(outcomes) -> tuple[int, int]:
        """(failures, checked) from a stream of True/False, None meaning skipped."""
        seen = [o for o in outcomes if o is not None]
        return seen.count(False), len(seen)

    def commutes(t):
        for i, j in pairs:
            yield None if t[i][j] is None else t[i][j] == t[j][i]

    report("a (+) b  =  b (+) a", *tally(commutes(add)), "pairs", "")
    report("a (x) b  =  b (x) a", *tally(commutes(mul)), "pairs", "")

    def monotone():
        for i, j in pairs:
            if i <= j:
                for k in range(n):
                    left, right = add[i][k], add[j][k]
                    yield None if left is None or right is None else left <= right

    report("a <= b   implies   a (+) c <= b (+) c", *tally(monotone()), "triples", "")

    def zero_difference(system: System, t):
        z = system.members.index(F(0))
        size = len(system.members)
        for i in range(size):
            for j in range(size):
                yield None if t[i][j] is None else (t[i][j] != z or i == j)

    report("a (-) b = 0   implies   a = b", *tally(zero_difference(toy, sub)), "pairs", "")
    sub_n = table(toy_n, lambda a, b: a - b)
    fails_n, checked_n = tally(zero_difference(toy_n, sub_n))
    print(f"       ...but without subnormals: {fails_n:,} failures in {checked_n:,} pairs,"
          f" e.g. 0.625 (-) 0.5 = {show(toy_n.round(F(1, 8)))}")

    def sterbenz(system: System):
        positive = system.positive[1:]
        for a in positive:
            for b in positive:
                if b / 2 <= a <= 2 * b:
                    yield abs(a - b) in system.significand

    report("b/2 <= a <= 2b   implies   a (-) b is exact  (Sterbenz)",
           *tally(sterbenz(toy)), "pairs", "")
    fails_n, checked_n = tally(sterbenz(toy_n))
    print(f"       ...but without subnormals: {fails_n:,} failures in {checked_n:,} pairs")
    print()

    def associates():
        for i, j, k in triples:
            ab, bc = add[i][j], add[j][k]
            if ab is None or bc is None:
                yield None
                continue
            left, right = add[ab][k], add[i][bc]
            yield None if left is None or right is None else left == right

    a, b = F(1), F(1, 8)
    report("(a (+) b) (+) c  =  a (+) (b (+) c)", *tally(associates()), "triples",
           f"(1 (+) 0.125) (+) 0.125 = {show(r(r(a + b) + b))},"
           f"  but  1 (+) (0.125 (+) 0.125) = {show(r(a + r(b + b)))}")

    def distributes():
        for i, j, k in triples:
            bc, ab, ac = add[j][k], mul[i][j], mul[i][k]
            if bc is None or ab is None or ac is None:
                yield None
                continue
            left, right = mul[i][bc], add[ab][ac]
            yield None if left is None or right is None else left == right

    a, b, c = F(3, 2), F(1), F(1, 8)
    report("a (x) (b (+) c)  =  (a (x) b) (+) (a (x) c)", *tally(distributes()), "triples",
           f"1.5 (x) (1 (+) 0.125) = {show(r(a * r(b + c)))},"
           f"  but  (1.5 (x) 1) (+) (1.5 (x) 0.125) = {show(r(r(a * b) + r(a * c)))}")

    def no_absorption():
        for i, j in pairs:
            if j != zero:
                yield None if add[i][j] is None else add[i][j] != i

    report("b != 0   implies   a (+) b != a", *tally(no_absorption()), "pairs",
           f"4 (+) 0.125 = {show(r(F(4) + F(1, 8)))}")

    def inverts():
        for i in range(n):
            if i == zero:
                continue
            inverse = r(1 / xs[i])
            product = None if inverse is None else mul[i][at[inverse]]
            yield None if product is None else product == one

    report("a (x) (1 (/) a)  =  1", *tally(inverts()), "members",
           f"7 (x) (1 (/) 7) = 7 (x) {show(r(F(1, 7)))} = {show(r(7 * r(F(1, 7))))}")
    print()
    print("   The survivors each compare one exact result with itself: a + b and")
    print("   b + a are the same real number before any rounding happens. The")
    print("   failures compare two ROUTES, and each route rounds in different places.")
    print()


def section_5() -> None:
    print("5. THE FLOAT YOU ALREADY USE IS THE SAME CONSTRUCTION")
    fi = sys.float_info
    p, emin, emax = fi.mant_dig, fi.min_exp - 1, fi.max_exp - 1
    print(f"   Read off this machine:  beta = {fi.radix},  p = {p},  e from {emin} to {emax}")
    per_sign = 1 * 2 ** (p - 1) * (emax - emin + 1) + (2 ** (p - 1) - 1)
    members = 2 * per_sign + 1
    print(f"     members              {members:,}")
    print(f"       equal to 2^64 - 2^53 - 1?      {members == 2**64 - 2**53 - 1}")
    largest_formula = (2 - F(2) ** (1 - p)) * F(2) ** emax
    print(f"     largest              {fi.max!r}")
    print(f"       equal to (2 - 2^-52) x 2^1023? {F(fi.max) == largest_formula}")
    print(f"     smallest normal      {fi.min!r}  = 2^{emin}: {F(fi.min) == F(2) ** emin}")
    print(f"     smallest subnormal   {math.ulp(0.0)!r}  = 2^{emin - p + 1}:"
          f" {F(math.ulp(0.0)) == F(2) ** (emin - p + 1)}")
    for x in [1.0, 1e16, 1e308]:
        print(f"     gap above {x!r:<10} {math.ulp(x)!r}")
    print()
    print("   The laws of section 4, on real floats:")
    rows = [
        ("0.1 + 0.2 == 0.2 + 0.1", repr(0.1 + 0.2 == 0.2 + 0.1)),
        ("(0.1 + 0.2) + 0.3", repr((0.1 + 0.2) + 0.3)),
        ("0.1 + (0.2 + 0.3)", repr(0.1 + (0.2 + 0.3))),
        ("100.0 * (0.1 + 0.2)", repr(100.0 * (0.1 + 0.2))),
        ("100.0 * 0.1 + 100.0 * 0.2", repr(100.0 * 0.1 + 100.0 * 0.2)),
        ("2.0**53 + 1.0 == 2.0**53", repr(2.0**53 + 1.0 == 2.0**53)),
        ("49.0 * (1.0 / 49.0)", repr(49.0 * (1.0 / 49.0))),
        ("(0.1 + 0.2) - 0.3", repr((0.1 + 0.2) - 0.3)),
    ]
    for expr, value in rows:
        print(f"     {expr:<28} {value}")
    exact = F(0.1 + 0.2) - F(0.3) == F((0.1 + 0.2) - 0.3)
    print(f"       ...exactly the difference of the two stored values? {exact}")
    print()
    print("   Which fractions can be members at ANY precision? In radix beta, a")
    print("   fraction in lowest terms can be, only if every prime factor of its")
    print("   denominator also divides beta:")
    print()
    radixes = [2, 10, 3]
    print(("                " + "".join(f"{'radix ' + str(b):<10}" for b in radixes)).rstrip())
    for fr in [F(1, 10), F(1, 3), F(3, 8), F(1, 6)]:
        cells = "".join(f"{'yes' if terminates(fr, b) else 'no':<10}" for b in radixes)
        print(f"     {str(fr):<11}{cells}".rstrip())
    print()


def terminates(fr: F, beta: int) -> bool:
    """True when fr has a finite expansion in radix beta."""
    d = fr.denominator
    g = math.gcd(d, beta)
    while g > 1:
        while d % g == 0:
            d //= g
        g = math.gcd(d, beta)
    return d == 1


def section_6() -> None:
    print("6. OFF THE ENDS OF THE RANGE")
    product = 1.0
    as_float = {}
    for k in range(1, 1002):
        product *= k
        as_float[k] = product
    print("   The largest float is about 1.8e308. Factorials outrun it quickly:")
    print(f"     170!  as a float  = {as_float[170]!r}")
    print(f"     171!  as a float  = {as_float[171]!r}")
    print(f"     1000! has {len(str(math.factorial(1000))):,} digits,"
          f" 1001! has {len(str(math.factorial(1001))):,}")
    print()
    print("   1001! / 1000! is exactly 1001. With floats:")
    print(f"     1001! -> {as_float[1001]!r}    1000! -> {as_float[1000]!r}"
          f"    inf / inf = {as_float[1001] / as_float[1000]!r}")
    print("   If overflow stopped at the largest float instead of going to inf:")
    print(f"     largest / largest = {sys.float_info.max / sys.float_info.max!r}"
          "     a quiet, plausible, wrong answer")
    print()
    print("   Three ways to stay inside the set:")
    print("     cancel first      1001! / 1000!  =  1001 x 1000! / 1000!  =  1001")
    exact = math.factorial(1001) // math.factorial(1000)
    print(f"     exact integers    factorial(1001) // factorial(1000)  =  {exact}")
    logs = math.exp(math.lgamma(1002) - math.lgamma(1001))
    print(f"     logarithms        exp(lgamma(1002) - lgamma(1001))  =  {logs:.9g}   to 9 s.f.")
    print()
    tiny = math.ulp(0.0)
    print("   And off the bottom, where the smallest subnormal is 5e-324:")
    print(f"     5e-324 / 2  =  {tiny / 2!r}     a tie between 0 and 5e-324, and 0 is even")
    print()


def binary(fmt: str, x: float) -> float | None:
    """x rounded into a binary16 ('e') or binary32 ('f') float; None on overflow."""
    try:
        return struct.unpack("<" + fmt, struct.pack("<" + fmt, x))[0]
    except OverflowError:
        return None


DECIMAL64 = Context(prec=16, Emax=384, Emin=-383, rounding=ROUND_HALF_EVEN)


def section_7() -> None:
    print("7. CHOOSING THE FOUR NUMBERS IS THE COMPROMISE")
    fi = sys.float_info
    formats = [
        # name, bits, beta, p, emin, emax, largest
        ("binary16", 16, 2, 11, -14, 15, struct.unpack("<e", bytes.fromhex("ff7b"))[0]),
        ("binary32", 32, 2, 24, -126, 127, struct.unpack("<f", bytes.fromhex("ffff7f7f"))[0]),
        ("binary64", 64, 2, 53, fi.min_exp - 1, fi.max_exp - 1, fi.max),
        ("decimal64", 64, 10, 16, DECIMAL64.Emin, DECIMAL64.Emax,
         Decimal("9.999999999999999E+384")),
    ]
    three = Context(prec=3, rounding=ROUND_DOWN)
    print(f"     {'':<10}{'bits':>5}{'radix':>7}{'p':>5}{'emin':>8}{'emax':>7}   {'largest':<11} members")
    for name, bits, beta, p, emin, emax, largest in formats:
        per_sign = (beta - 1) * beta ** (p - 1) * (emax - emin + 1) + beta ** (p - 1) - 1
        count = 2 * per_sign + 1
        big = str(three.create_decimal(Decimal(largest)))
        print(f"     {name:<10}{bits:>5}{beta:>7}{p:>5}{emin:>8}{emax:>7}   {big:<11} {count:.3g}")
    patterns = {struct.unpack("<e", struct.pack("<H", b))[0] for b in range(1 << 16)}
    finite = sum(1 for x in patterns if math.isfinite(x))
    per_sign = 2**10 * 30 + 2**10 - 1
    print(f"   Brute force on binary16: its 65,536 bit patterns give {finite:,} distinct")
    print(f"   finite values. The count formula gives {2 * per_sign + 1:,}.")
    print()
    print("   What each one stores for a few numbers, as a relative error:")
    columns = [("1/10", F(1, 10)), ("1/3", F(1, 3)), ("2^24 + 1", F(2**24 + 1)), ("70,000", F(70000))]
    print(("                " + "".join(f"{label:<12}" for label, _ in columns)).rstrip())
    for name, *_ in formats:
        cells = []
        for _, value in columns:
            if name == "decimal64":
                stored = DECIMAL64.divide(Decimal(value.numerator), Decimal(value.denominator))
            elif name == "binary64":
                stored = value.numerator / value.denominator
            else:
                stored = binary("e" if name == "binary16" else "f",
                                value.numerator / value.denominator)
            if stored is None:
                cells.append("overflow")
            elif F(stored) == value:
                cells.append("exact")
            else:
                cells.append(f"{float((F(stored) - value) / value):+.1e}")
        print(f"     {name:<11}" + "".join(f"{c:<12}" for c in cells).rstrip())
    print()
    print("   Relative gap just above 1, and just below the next power of the radix:")
    below_2 = math.nextafter(2.0, 0.0)
    b_low, b_high = math.ulp(1.0) / 1.0, math.ulp(below_2) / below_2
    print(f"     binary64    {b_low:.1e}  and  {b_high:.1e}    varies {b_low / b_high:.0f}x")
    one = Decimal(1)
    below_10 = DECIMAL64.next_minus(Decimal(10))
    d_low = (DECIMAL64.next_plus(one) - one) / one
    d_high = (DECIMAL64.next_plus(below_10) - below_10) / below_10
    print(f"     decimal64   {d_low:.1e}  and  {d_high:.1e}    varies {d_low / d_high:.0f}x")
    print()
    print("   More bits buy precision and range, and cost memory and speed. Radix 10")
    print("   makes 1/10 exact, but its gaps wobble 10x instead of 2x, and the same")
    print("   64 bits give fewer distinct values. Every choice gives something up.")


def main() -> None:
    toy_n = System(2, 3, -1, 2, subnormals=False)
    toy = System(2, 3, -1, 2)
    section_1(toy_n)
    section_2(toy_n, toy)
    section_3(toy)
    section_4(toy, toy_n)
    section_5()
    section_6()
    section_7()


if __name__ == "__main__":
    main()
