#!/usr/bin/env python3
"""The Cantor set: uncountably many points, and total length zero.

Run:  python3 cantor_set.py

Start with [0,1]. Delete the open middle third. Delete the middle third of
each piece that is left, and repeat forever. What survives has length zero --
and still has as many points as the whole interval you started with.

Exact arithmetic throughout (fractions.Fraction). Membership is checked two
independent ways -- by the base-3 digits, and by running the construction --
and the program stops if they ever disagree.
"""

import math
from fractions import Fraction as F

THIRD, TWO_THIRDS = F(1, 3), F(2, 3)


def next_step(pieces: list[tuple[F, F]]) -> list[tuple[F, F]]:
    """Delete the open middle third of every closed piece."""
    out = []
    for a, b in pieces:
        w = (b - a) / 3
        out += [(a, a + w), (b - w, b)]
    return out


def picture(pieces: list[tuple[F, F]], width: int = 81) -> str:
    cells = []
    for i in range(width):
        lo, hi = F(i, width), F(i + 1, width)
        cells.append("#" if any(a <= lo and hi <= b for a, b in pieces) else " ")
    return "".join(cells)


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


def written(prefix: str, block: str, shown: int = 12) -> str:
    if block == "0":
        return "0." + (prefix or "0")
    digits = prefix
    while len(digits) < shown:
        digits += block
    return "0." + digits[:shown] + "..."


def base3_for_cantor(x: F) -> tuple[str, str]:
    """x's base-3 digits, choosing 0.xyz0222... over 0.xyz1 when both exist."""
    prefix, block = expansion(x, 3)
    if block == "0" and prefix.endswith("1"):
        prefix, block = prefix[:-1] + "0", "2"
    return prefix, block


def only_0s_and_2s(x: F) -> bool:
    prefix, block = base3_for_cantor(x)
    return set(prefix + block) <= {"0", "2"}


def removed_at(x: F, steps: int = 60) -> int | None:
    """The construction step that deletes x, or None if it survives every step run."""
    y = x
    for n in range(1, steps + 1):
        if THIRD < y < TWO_THIRDS:
            return n
        y = 3 * y if y <= THIRD else 3 * y - 2
    return None


def halve_digits(x: F) -> F:
    """Cantor point (base-3 digits 0 and 2) -> the number with digits 0 and 1 in base 2."""
    prefix, block = base3_for_cantor(x)
    half = str.maketrans("02", "01")
    return value(prefix.translate(half), block.translate(half), 2)


def double_digits(y: F) -> F:
    """Any number in [0,1) -> a Cantor point, by writing it in base 2 and doubling digits."""
    prefix, block = expansion(y, 2)
    double = str.maketrans("01", "02")
    return value(prefix.translate(double), block.translate(double), 3)


def main() -> None:
    print("1. BUILD IT")
    print("   Each step deletes the open middle third of every piece left.")
    pieces = [(F(0), F(1))]
    for n in range(5):
        print(f"     {n} |{picture(pieces)}|")
        pieces = next_step(pieces)
    print()
    print(f"     {'step':>4}   {'pieces':>6}   {'each piece':<11}  length left")
    for n in [0, 1, 2, 3, 4, 5, 10, 20, 50]:
        left = F(2, 3) ** n
        removed = sum((F(2 ** (k - 1), 3**k) for k in range(1, n + 1)), F(0))
        assert removed == 1 - left
        count = f"{2**n:,}" if n <= 10 else f"2^{n}"
        each = "1" if n == 0 else f"1/{3**n}" if n <= 10 else f"1/3^{n}"
        exact = f"= {left}" if 1 <= n <= 5 else ""
        print(f"     {n:>4}   {count:>6}   {each:<11}  {float(left):.3e}   {exact}".rstrip())
    print("   Removed after n steps: exactly 1 - (2/3)^n. Removed in the limit:")
    print("   exactly 1, the entire length of the interval we started with.")
    print()

    print("2. SO IT HAS MEASURE ZERO")
    print("   Whatever the budget, stop at a step where the pieces left fit in it:")
    for budget in [F(1, 100), F(1, 10**6), F(1, 10**12)]:
        n = next(n for n in range(1000) if F(2, 3) ** n <= budget)
        pieces_text = f"2^{n} pieces,"
        print(f"     budget {str(budget):<15}  step {n:>2}: {pieces_text:<13} total length {float(F(2, 3) ** n):.3e}")
    print("   The pieces at every step cover everything that will ever survive.")
    print()

    print("3. WHAT SURVIVES? THE ENDPOINTS, FOR A START")
    ends = [F(0), F(1, 9), F(2, 9), F(1, 3), F(2, 3), F(7, 9), F(8, 9)]
    for e in ends:
        assert removed_at(e) is None
    print("     " + ", ".join(str(e) for e in ends) + ", 1 ...")
    print("   A piece's endpoints are never deleted. But endpoints are fractions")
    print("   with a power of 3 underneath, so there are only countably many. If")
    print("   nothing else survived, this would be one more countable set.")
    print()

    print("4. THE BASE-3 TEST")
    print("   Deleting a middle third deletes the numbers whose next base-3 digit")
    print("   is 1. So x survives exactly when it can be written with only 0s and 2s.")
    print(f"     {'x':<5}  {'base 3':<17}  {'only 0 and 2?':<14} construction says")
    for x in [F(1, 4), F(3, 4), F(1, 10), F(1, 13), F(1, 3), F(1, 2), F(1, 5), F(5, 9)]:
        prefix, block = base3_for_cantor(x)
        by_digits = only_0s_and_2s(x)
        step = removed_at(x)
        assert by_digits == (step is None), x
        verdict = "survives 60 steps" if step is None else f"deleted at step {step}"
        print(f"     {str(x):<5}  {written(prefix, block):<17}  {'yes' if by_digits else 'no':<14} {verdict}")
    print("   1/4 survives, and it is no endpoint -- its denominator is 4, not a")
    print("   power of 3. (1/3 = 0.1 in base 3, but also 0.0222..., so it passes.)")
    print()

    print("5. HALVE THE DIGITS")
    print("   Turn every 2 into a 1 and read the result in base 2:")
    print(f"     {'point':<5}  {'base 3':<17}   {'digits halved, base 2':<22} {'is'}")
    for x in [F(1, 4), F(3, 4), F(1, 10), F(1, 13), F(1, 3), F(2, 3)]:
        prefix, block = base3_for_cantor(x)
        half = str.maketrans("02", "01")
        y = halve_digits(x)
        print(
            f"     {str(x):<5}  {written(prefix, block):<17} -> "
            f"{written(prefix.translate(half), block.translate(half)):<22} {y}"
        )
    print()
    print("   Now run it backwards. Pick ANY number, write it in base 2, double")
    print("   the digits, and read base 3. The result is always in the Cantor set:")
    for y in [F(1, 3), F(1, 7), F(5, 8), F(7, 10), F(99, 100)]:
        c = double_digits(y)
        assert only_0s_and_2s(c) and removed_at(c) is None and halve_digits(c) == y
        print(f"     {str(y):<6} -> {str(c):<14} which halves back to {y}")
    print("   Every number in [0,1] is hit, so the Cantor set has at least as many")
    print("   points as [0,1] itself: UNCOUNTABLY many. (1/3 and 2/3 both land on")
    print("   1/2, so some numbers are hit twice -- which costs the argument nothing.)")
    print()

    print("6. HOW BIG IS IT?")
    print("     total length          0")
    print("     number of points      as many as the whole interval [0,1]")
    print("     contains an interval  no -- every piece gets cut at the next step")
    print(f"     dimension             log 2 / log 3 = {math.log(2) / math.log(3):.4f}")
    print("                           more than a point's 0, less than a line's 1")


if __name__ == "__main__":
    main()
