#!/usr/bin/env python3
"""The Cantor function: a staircase that climbs from 0 to 1 while standing still almost everywhere.

Run:  python3 cantor_function.py

Also called the devil's staircase. It stretches the Cantor set's "halve the
digits" map across all of [0,1]: read x in base 3, cut everything after the
first 1, turn 2s into 1s, and read what is left in base 2. It is continuous,
it rises from 0 to 1, and its slope is 0 on gaps of total length 1 -- so the
whole climb happens on the Cantor set, which has length 0.

Exact arithmetic throughout (fractions.Fraction). The function is built two
independent ways -- by the digit rule, and as a limit of ramps -- and the
program stops if they ever disagree.
"""

import math
from bisect import bisect_right
from fractions import Fraction as F

THIRD, TWO_THIRDS, HALF = F(1, 3), F(2, 3), F(1, 2)
TO_BINARY = str.maketrans("2", "1")


def expansion(x: F, base: int) -> tuple[str, str]:
    """Digits of 0 <= x < 1 after the point, as (prefix, block that repeats forever)."""
    assert 0 <= x < 1
    den, r = x.denominator, x.numerator
    seen: dict[int, int] = {}
    digits: list[str] = []
    while r not in seen:
        seen[r] = len(digits)
        r *= base
        digits.append(str(r // den))
        r %= den
    cut = seen[r]
    return "".join(digits[:cut]), "".join(digits[cut:])


def value(prefix: str, block: str, base: int) -> F:
    """The number 0.prefix block block block ... in the given base."""
    whole = int(prefix + block, base)
    head = int(prefix, base) if prefix else 0
    return F(whole - head, base ** len(prefix) * (base ** len(block) - 1))


def written(prefix: str, block: str, shown: int = 10) -> str:
    if block == "0":
        return "0." + (prefix or "0")
    digits = prefix
    while len(digits) < shown:
        digits += block
    return "0." + digits[:shown] + "..."


def digit_rule(x: F) -> tuple[str, F]:
    """The Cantor function by its digit rule: (the base-2 digits it reads, F(x))."""
    if x == 1:
        return "0.111...", F(1)
    prefix, block = expansion(x, 3)
    first_one = (prefix + block).find("1")
    if first_one == -1:
        p, b = prefix.translate(TO_BINARY), block.translate(TO_BINARY)
        return written(p, b), value(p, b, 2)
    kept = (prefix + block)[: first_one + 1].translate(TO_BINARY)
    return "0." + kept, value(kept, "0", 2)


def cantor(x: F) -> F:
    return digit_rule(x)[1]


def ramps(n: int, x: F) -> F:
    """F_n: F_0(x) = x, and F_n squeezes F_(n-1) into the outer thirds at half height."""
    if n == 0:
        return x
    if x <= THIRD:
        return ramps(n - 1, 3 * x) / 2
    if x < TWO_THIRDS:
        return HALF
    return HALF + ramps(n - 1, 3 * x - 2) / 2


def next_pieces(pieces: list[tuple[F, F]]) -> list[tuple[F, F]]:
    """Delete the open middle third of every closed piece."""
    return [q for a, b in pieces for q in ((a, a + (b - a) / 3), (b - (b - a) / 3, b))]


def cantor_gaps(step: int) -> list[tuple[F, F]]:
    """The open gaps the Cantor construction deletes at the given step."""
    pieces = [(F(0), F(1))]
    for _ in range(step - 1):
        pieces = next_pieces(pieces)
    return [(a + (b - a) / 3, b - (b - a) / 3) for a, b in pieces]


def main() -> None:
    print("1. THE RULE")
    print("   Read x in base 3. Cut everything after the first 1. Turn 2s into 1s.")
    print("   Read what is left in base 2.")
    print(f"     {'x':<8} {'base 3':<15}  {'after the rule':<15}  F(x)")
    examples = [F(1, 4), F(3, 4), F(1, 5), F(1, 2), F(5, 9), F(200, 243), F(1, 13), F(7, 10)]
    for x in examples:
        prefix, block = expansion(x, 3)
        binary, y = digit_rule(x)
        print(f"     {str(x):<8} {written(prefix, block):<15}  {binary:<15}  {y}")
    print("   A number with no 1 is in the Cantor set, and the rule just halves its")
    print("   digits -- lesson 3's map. A number that cannot be written without a 1")
    print("   lies in a gap, and cutting at the first 1 gives the whole gap one value.")
    print()

    print("2. THE STAIRCASE")
    width, height = 81, 16
    rows = [[" "] * width for _ in range(height)]
    previous = None
    for i in range(width):
        level = min(height - 1, math.floor(cantor(F(2 * i + 1, 2 * width)) * height))
        low, high = (level, level) if previous is None else sorted((previous, level))
        for r in range(low, high + 1):
            rows[r][i] = "#"
        previous = level
    for r in reversed(range(height)):
        label = "1" if r == height - 1 else "0" if r == 0 else " "
        print(f"   {label} |{''.join(rows[r])}".rstrip())
    print(f"     +{'-' * width}")
    print(f"      x = 0{' ' * (width - 9)}x = 1")
    print()

    print("3. FLAT ON EVERY GAP")
    print("   Each gap the Cantor set deletes becomes one tread of the staircase:")
    print(f"     {'step':>4}   {'gap':<16} F on the whole gap")
    for step in [1, 2, 3]:
        for a, b in cantor_gaps(step):
            y = cantor(a)
            inside = [a + (b - a) * j / 51 for j in range(1, 51)]
            assert cantor(b) == y and all(cantor(t) == y for t in inside)
            print(f"     {step:>4}   {f'({a}, {b})':<16} {y}")
    print("   Checked at both ends and at 50 points inside every gap.")
    print("   The gaps have total length 1 (lesson 3), so the slope of F is 0")
    print("   everywhere except on the Cantor set, a set of length 0. F is flat")
    print("   ALMOST EVERYWHERE.")
    print()

    print("4. THE SAME FUNCTION, BUILT FROM RAMPS")
    print("   Start with the diagonal F_0(x) = x. For F_n, squeeze F_(n-1) into")
    print("   [0,1/3] and [2/3,1] at half height, and hold 1/2 across the middle.")
    print(f"     {'n':>2}   {'largest change from F_(n-1)':<28} digit rule agrees on the 3^n grid?")
    for n in range(1, 9):
        grid = [F(k, 3**n) for k in range(3**n + 1)]
        change = max(abs(ramps(n, x) - ramps(n - 1, x)) for x in grid)
        assert change == F(1, 6) / 2 ** (n - 1)
        agrees = all(ramps(n, x) == cantor(x) for x in grid)
        assert agrees
        print(f"     {n:>2}   {str(change):<28} {'yes' if agrees else 'NO'}")
    for n in range(1, 5):
        fine = [F(k, 3 ** (n + 4)) for k in range(3 ** (n + 4) + 1)]
        assert all(abs(cantor(x) - ramps(n, x)) <= F(1, 3) / 2**n for x in fine)
    print("   The largest change halves every time, so the ramps close in on one")
    print("   function at a steady rate (checked on grids 81 times finer: F stays")
    print("   within (1/3)(1/2)^n of F_n). A limit of continuous functions that")
    print("   converges like that is continuous. The staircase never jumps.")
    print()

    print("5. WHERE THE CLIMB HIDES")
    print("   F_n has 2^n ramps, each rising 1/2^n over a run of 1/3^n: slope (3/2)^n.")
    print("   In the limit the ramps are gone, and so is any finite slope. The slope")
    print("   of F just to the left of 1/3, over a run of 1/3^n:")
    print(f"     {'n':>2}   {'run':<14} {'rise':<10} slope")
    for n in [1, 2, 3, 5, 10, 20]:
        run = F(1, 3**n)
        rise = cantor(THIRD) - cantor(THIRD - run)
        assert rise / run == F(3, 2) ** n
        run_text = f"1/{3**n}" if n <= 10 else f"1/3^{n}"
        rise_text = f"1/{2**n}" if n <= 10 else f"1/2^{n}"
        print(f"     {n:>2}   {run_text:<14} {rise_text:<10} {float(rise / run):,.2f}")
    assert all(cantor(THIRD + F(1, 3**n)) == cantor(THIRD) for n in range(1, 21))
    print("   To the right of 1/3 the slope is 0 (it is the start of a gap). To the")
    print("   left it grows without bound. F has no derivative at 1/3.")
    print()
    print("   So where does the rise of 1 happen? Not on the gaps: they contribute")
    print("   nothing. The pieces left at step n have total length (2/3)^n, and F")
    print("   climbs 1/2^n across each of the 2^n of them -- all 1 of the rise,")
    print("   packed into a length that goes to 0:")
    pieces = [(F(0), F(1))]
    for n in range(1, 11):
        pieces = next_pieces(pieces)
        if n in (1, 3, 5, 10):
            rises = [cantor(b) - cantor(a) for a, b in pieces]
            length = sum((b - a for a, b in pieces), F(0))
            assert all(r == F(1, 2**n) for r in rises) and length == F(2, 3) ** n
            print(
                f"     step {n:>2}: {len(pieces):>5,} pieces, total length {float(length):.3e},"
                f" total rise {sum(rises, F(0))}"
            )
    print()

    print("6. THE GRAPH IS AS LONG AS AN L")
    print("   Length of the graph of F_n = its flat parts + its 2^n ramps:")
    print(f"     {'n':>2}   {'flat parts':<11} {'ramps':<11} total")
    for n in [0, 1, 2, 5, 10, 20, 50]:
        flat = 1 - F(2, 3) ** n
        ramp = math.sqrt(float(F(4, 9) ** n) + 1)
        if n <= 5:
            grid = [F(k, 3**n) for k in range(3**n + 1)]
            walked = sum(
                math.hypot(float(b - a), float(ramps(n, b) - ramps(n, a))) for a, b in zip(grid, grid[1:])
            )
            assert abs(walked - (float(flat) + ramp)) < 1e-12
        print(f"     {n:>2}   {float(flat):.6f}    {ramp:.6f}    {float(flat) + ramp:.6f}")
    print("   Walking right 1 and then up 1 is a path of length 2. The staircase's")
    print("   graph closes in on exactly that: all of its run on the flat treads,")
    print("   and all of its rise over a set of length zero.")
    print()

    print("7. A RANDOM NUMBER WITH NO DENSITY")
    digits = 16
    values = [0]
    for _ in range(digits):
        values = [3 * v for v in values] + [3 * v + 2 for v in values]
    values.sort()
    total = len(values)
    print("   Build Y by flipping a fair coin for each base-3 digit: heads 2, tails 0.")
    print("   Y always lands in the Cantor set. Counting all 2^16 ways the first 16")
    print("   flips can go, exactly:")
    print(f"     {'x':<6} {'P(Y <= x) is between':<24} F(x)")
    for x in [F(1, 4), F(1, 5), F(1, 2), F(7, 10), F(9, 10)]:
        scaled = x * 3**digits
        at_most = bisect_right(values, math.floor(scaled)) / total
        at_least = bisect_right(values, math.floor(scaled - 1)) / total
        assert at_least <= cantor(x) <= at_most
        print(f"     {str(x):<6} {at_least:.6f} and {at_most:.6f}    {cantor(x)}")
    print("   P(Y <= x) is the Cantor function. It has no jumps, so no single value")
    print("   of Y has positive probability. Yet all of Y's probability sits on the")
    print("   Cantor set, length 0 -- so no density function could describe Y: it")
    print("   would give a set of length 0 probability 0.")


if __name__ == "__main__":
    main()
