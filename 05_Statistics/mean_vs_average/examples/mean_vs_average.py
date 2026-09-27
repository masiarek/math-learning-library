#!/usr/bin/env python3
"""Mean, average, arithmetic mean: several names, one calculation, and where they part.

Run:  python3 mean_vs_average.py

In a classroom every one of these names means one thing: add the numbers up and
divide by how many there are. They are still different sizes of word. "Average"
covers any single value that stands for the set, "mean" is one family of
averages, and "arithmetic" picks out the member of that family that adds. A mean
keeps some total unchanged, and the adjective says which total.

Every number is an int or a Fraction, so each "kept" and "not kept" below is an
exact comparison, not a float that happens to look right.
"""

import sqlite3
import statistics
from fractions import Fraction


def arithmetic_mean(xs: list[Fraction]) -> Fraction:
    return sum(xs, Fraction(0)) / len(xs)


def exact_root(x: Fraction, n: int) -> Fraction:
    """The n-th root of x. The examples are chosen so that it is a fraction."""
    root = Fraction(round(x.numerator ** (1 / n)), round(x.denominator ** (1 / n)))
    assert root**n == x, f"{x} has no exact {n}-th root"
    return root


def geometric_mean(xs: list[Fraction]) -> Fraction:
    product = Fraction(1)
    for x in xs:
        product *= x
    return exact_root(product, len(xs))


def harmonic_mean(xs: list[Fraction]) -> Fraction:
    return len(xs) / sum(1 / x for x in xs)


def line(left: str, note: str = "") -> None:
    """One indented line, with an optional note in a column of its own."""
    print(f"     {left:<38}{note}".rstrip())


def money(x: Fraction) -> str:
    return f"{float(x):,.2f}"


def percent(factor: Fraction) -> str:
    return f"{float((factor - 1) * 100):+.0f}%"


def hours(t: Fraction) -> str:
    whole = int(t)
    minutes = (t - whole) * 60
    return f"{whole} h" if minutes == 0 else f"{whole} h {minutes} min"


def main() -> None:
    scores = [72, 85, 90, 64, 79]

    print("1. ONE CALCULATION, SEVERAL NAMES")
    print(f"   Five test scores: {', '.join(map(str, scores))}")
    total = sum(scores)
    mean = arithmetic_mean([Fraction(s) for s in scores])
    print(f"     add them up           {' + '.join(map(str, scores))} = {total}")
    print(f"     divide by how many    {total} / {len(scores)} = {mean}")
    print("   The same five scores, handed to software under its own names:")
    print(f"     Python  statistics.mean(scores)        {statistics.mean(scores)}")
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE scores (score INTEGER)")
    db.executemany("INSERT INTO scores VALUES (?)", [(s,) for s in scores])
    (avg,) = db.execute("SELECT AVG(score) FROM scores").fetchone()
    print(f"     SQL     SELECT AVG(score) FROM scores  {avg}")
    print("   Average, mean, arithmetic mean, arithmetic average, x-bar:")
    print(f"   on these scores every one of them is this calculation, and gives {mean}.")
    print(f"   Nobody scored {mean}. The mean is calculated, not picked from the list.")
    print()

    print("2. WHAT THE ARITHMETIC MEAN KEEPS: THE SUM")
    print(f"   Give every student {mean} instead of their own score:")
    line(f"{' + '.join([str(mean)] * len(scores))} = {mean * len(scores)}",
         f"the total is still {total}")
    print("   That is what the mean is: the one number that can stand in for every")
    print("   value without changing the total. So the distances from it cancel:")
    for s in scores:
        d = s - mean
        line(f"{s} - {mean} = {str(d) if d < 0 else '+' + str(d):>3}")
    line(f"sum of the distances = {sum(s - mean for s in scores)}",
         "above and below balance exactly")
    print('   That balance is the "central" in "central value".')
    print()

    print('3. WHY "ARITHMETIC": GROWTH KEEPS THE PRODUCT')
    start = Fraction(1000)
    factors = [Fraction(2), Fraction(1, 2)]
    print(f"   Invest {money(start)}. Year 1: {percent(factors[0])}."
          f" Year 2: {percent(factors[1])}.")
    balance = [start]
    for f in factors:
        balance.append(balance[-1] * f)
    line(" -> ".join(money(b) for b in balance), "back where it started")
    a = arithmetic_mean(factors)
    print(f"   Arithmetic mean of the two returns: {percent(a)} a year")
    line(f"{money(start)} x {float(a)} x {float(a)} = {money(start * a * a)}",
         f"WRONG: the account holds {money(balance[-1])}")
    g = geometric_mean(factors)
    print("   Growth multiplies, so the mean has to keep the PRODUCT of the factors:")
    line(f"geometric mean of x{factors[0]} and x{factors[1]}"
         f" = square root of ({factors[0]} x {factors[1]}) = {g}")
    line(f"a factor of {g} is {percent(g)} a year")
    line(f"{money(start)} x {g} x {g} = {money(start * g * g)}", "right")
    print()

    print('4. WHY "ARITHMETIC": SPEED KEEPS THE TIME')
    leg = Fraction(60)
    speeds = [Fraction(30), Fraction(60)]
    print(f"   Drive {leg} km at {speeds[0]} km/h, and the {leg} km back"
          f" at {speeds[1]} km/h.")
    times = [leg / v for v in speeds]
    took = sum(times)
    distance = leg * len(speeds)
    line(f"{leg}/{speeds[0]} + {leg}/{speeds[1]} = {times[0]} + {times[1]}"
         f" = {took} hours for {distance} km")
    line(f"{distance} km in {took} hours is {distance / took} km/h")
    a = arithmetic_mean(speeds)
    print(f"   Arithmetic mean of the speeds: ({speeds[0]} + {speeds[1]}) / 2"
          f" = {a} km/h")
    line(f"at {a} km/h, {distance} km takes {hours(distance / a)}",
         f"WRONG: it took {hours(took)}")
    h = harmonic_mean(speeds)
    print("   Time is distance / speed, so the mean has to keep the sum of 1/speed:")
    line(f"harmonic mean = 2 / (1/{speeds[0]} + 1/{speeds[1]}) = {h} km/h")
    line(f"at {h} km/h, {distance} km takes {hours(distance / h)}", "right")
    print()

    print('5. "AVERAGE" IS A WIDER WORD THAN "MEAN"')
    salaries = [32_000, 34_000, 34_000, 34_000, 36_000,
                38_000, 40_000, 42_000, 45_000, 400_000]
    print("   Ten salaries at a small firm; the last one is the owner's:")
    for row in (salaries[:5], salaries[5:]):
        print("     " + "  ".join(f"{s:>7,}" for s in row))
    mean = arithmetic_mean([Fraction(s) for s in salaries])
    median = statistics.median(salaries)
    mode = statistics.mode(salaries)
    print('   Three numbers, each of them honestly called "the average salary":')
    print(f"     mean     {int(mean):>7,}    the payroll shared out equally")
    print(f"     median   {int(median):>7,}    the middle: half earn less, half earn more")
    print(f"     mode     {mode:>7,}    the salary the most people are paid")
    below = sum(s < mean for s in salaries)
    print(f"   {below} of the {len(salaries)} earn less than the mean."
          ' "Average" alone did not say which.')


if __name__ == "__main__":
    main()
