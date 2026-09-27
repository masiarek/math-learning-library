#!/usr/bin/env python3
"""Two ways for money to grow, and the question only a logarithm answers.

Run:  python3 doubling_time.py

Every precalculus book has a chapter on exponential and logarithmic
functions, and the example every one of them reaches for is money. Simple
interest adds the same amount every year: a linear function. Compound
interest multiplies by the same factor every year: an exponential function.
The course asks two questions about any function, "what does it do as the
input grows?" and "which input gives this output?", and for the exponential
the second question has no answer among the operations of arithmetic. The
logarithm is the name of that answer.

Every balance is a fractions.Fraction, so every comparison below is exact.
The only floats are in section 3, where the logarithm itself is computed,
and the program says so when it gets there.
"""

from fractions import Fraction
from math import log

START = Fraction(100)
RATE = Fraction(5, 100)
FACTOR = 1 + RATE  # 21/20: what one year of compound interest multiplies by


def simple(t: int, rate: Fraction = RATE) -> Fraction:
    """Balance after t years of simple interest: the same amount added each year."""
    return START + START * rate * t


def compound(t: int, rate: Fraction = RATE) -> Fraction:
    """Balance after t years of compound interest: the same factor each year."""
    return START * (1 + rate) ** t


def cents(x: Fraction) -> str:
    """A fraction shown to the cent. Only the display rounds; the arithmetic is exact."""
    return f"{float(x):.2f}"


def main() -> None:
    print("1. TWO WAYS TO GROW: A LINE AND A CURVE")
    print(f"   Start with {cents(START)} at {RATE * 100}% a year.")
    print(f"   simple interest:    balance after t years = {START} + {START * RATE}·t        (add {cents(START * RATE)} every year)")
    print(f"   compound interest:  balance after t years = {START} · ({FACTOR})^t   (multiply by {FACTOR} every year)")
    print()
    print(f"     {'t':>3}  {'simple':>8}  {'compound':>9}  {'compound gained that year':>26}")
    for t in (0, 1, 2, 3, 5, 10, 14, 15, 20, 30, 50):
        gained = compound(t) - compound(t - 1) if t > 0 else Fraction(0)
        print(f"     {t:>3}  {cents(simple(t)):>8}  {cents(compound(t)):>9}  {cents(gained):>26}")
    print("   Simple interest gains the same 5.00 every year, so its graph is a")
    print("   straight line. Compound interest gains 5% of a balance that has")
    print("   already grown, so the gains grow too, and the graph bends upward.")
    print()

    print("2. WHICH YEAR DOES THE MONEY DOUBLE?")
    target = 2 * START
    print(f"   simple:    {START} + {START * RATE}·t = {target}")
    print(f"              {'subtract ' + str(START) + ':':<16}{START * RATE}·t = {target - START}")
    print(f"              {'divide by ' + str(START * RATE) + ':':<16}t = {(target - START) / (START * RATE)}")
    print("              Each step undoes one operation of arithmetic.")
    print()
    print(f"   compound:  {START} · ({FACTOR})^t = {target}")
    print(f"              {'divide by ' + str(START) + ':':<16}({FACTOR})^t = {target / START}")
    print(f"              ...and now t is an exponent. No operation of arithmetic")
    print(f"              undoes 'raise {FACTOR} to a power', so try values of t:")
    print(f"                {'t':>3}  {'(' + str(FACTOR) + ')^t':>10}  {'doubled?':>8}")
    first = None
    for t in range(12, 17):
        ratio = FACTOR ** t
        doubled = ratio >= 2
        if doubled and first is None:
            first = t
        print(f"                {t:>3}  {float(ratio):>10.4f}  {str(doubled):>8}")
    below, above = first - 1, first
    print(f"   The balance first doubles in year {first}: ({FACTOR})^{below} < 2 ≤ ({FACTOR})^{above}.")
    print(f"   The exact moment, the t with ({FACTOR})^t = 2, is between {below} and {above},")
    print("   and it is not a fraction at all: (21/20)^(p/q) = 2 would mean")
    print("   21^p = 2^q · 20^p, an odd number equal to an even one.")
    print()

    print("3. THE LOGARITHM IS THE NAME OF THE ANSWER")
    print(f"   The number t with ({FACTOR})^t = 2 is written log base {FACTOR} of 2.")
    print("   It has no exact decimal, so this section, alone in the program, uses floats:")
    base = float(FACTOR)
    t_exact = log(2) / log(base)
    print(f"     t = ln 2 / ln {base}  =  {log(2):.6f} / {log(base):.6f}  =  {t_exact:.6f}")
    print(f"     check:  {base}^{t_exact:.6f} = {base ** t_exact:.10f}")
    years = int(t_exact)
    days = round((t_exact - years) * 365)
    print(f"     that is {years} years and about {days} days, in the year-{above} row of the table")
    print("   Dividing one natural logarithm by another is the change-of-base formula,")
    print("   and it is why a calculator needs only one log key.")
    print()
    rule = 72 / float(RATE * 100)
    print(f"   The rule of 72 says the doubling time is about 72 / rate = 72 / {float(RATE * 100):g} = {rule:.1f} years,")
    print(f"   because ln 2 = {log(2):.3f} and ln(1 + r) is close to r when r is small,")
    print("   so t is close to 0.693 / r, and 72 divides more evenly than 69.3.")
    print()

    print("4. THE EXPONENTIAL WINS EVENTUALLY, WHATEVER THE RATES")
    low = Fraction(1, 100)
    print(f"   {float(low * 100):g}% compound against {float(RATE * 100):g}% simple. The line is ahead for a long time:")
    print(f"     {'t':>3}  {'simple 5%':>10}  {'compound 1%':>12}")
    for t in (0, 10, 50, 100, 200, 300):
        print(f"     {t:>3}  {cents(simple(t)):>10}  {cents(compound(t, low)):>12}")
    t = 0
    while compound(t, low) <= simple(t):
        t += 1
    print(f"   The curve passes the line in year {t}:  compound {cents(compound(t, low))} > simple {cents(simple(t))},")
    print(f"   and in year {t - 1} it had not:          compound {cents(compound(t - 1, low))} < simple {cents(simple(t - 1))}.")
    print("   No logarithm finds that year. A logarithm undoes an exponential when")
    print("   the other side is a number, as in section 2, not when it is another")
    print("   function of t. Trying values is the only method here, and it works")
    print("   because an exponential with base above 1 outgrows every line, and")
    print("   every polynomial, in the end. The books call this end behaviour.")
    t = 2  # at t = 2 the polynomial takes the lead: 2^2 = 4 against 2^10 = 1024
    while 2 ** t <= t ** 10:
        t += 1
    print(f"   Even 2^t against t^10: t^10 takes the lead at t = 2, keeps it through t = {t - 1},")
    print(f"   and 2^t passes it at t = {t}.")


if __name__ == "__main__":
    main()
