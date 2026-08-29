#!/usr/bin/env python3
"""Significant figures: what the notation claims, and the two arithmetic rules.

Run:  python3 significant_figures.py

Significant figures are not rounding. Rounding is the action; sig figs are the
rule that decides where the action must stop. Every number below is written the
way a scientist would write it, and the program prints what that writing claims.
"""

from decimal import Decimal, localcontext


def sig_figs(text: str) -> int:
    return len(Decimal(text).as_tuple().digits)


def implied_span(text: str) -> tuple[Decimal, Decimal]:
    """The range a written measurement actually claims."""
    d = Decimal(text)
    half = Decimal(1).scaleb(d.as_tuple().exponent) / 2
    return d - half, d + half


def round_sf(d: Decimal, n: int) -> Decimal:
    """Round to n significant figures. Unary plus applies the context precision."""
    with localcontext() as ctx:
        ctx.prec = n
        return +d


def last_place(text: str) -> int:
    """Power of ten of the last significant digit."""
    return Decimal(text).as_tuple().exponent


def main() -> None:
    print("1. WHAT THE NOTATION CLAIMS")
    census = "3.2E+6"
    lo, hi = implied_span(census)
    print(f"   written        3,200,000 people   (as 3.2 x 10^6)")
    print(f"   sig figs       {sig_figs(census)}")
    print(f"   really means   {int(lo):,} to {int(hi):,}")
    print(f"   uncertainty    +/- {int(Decimal(1).scaleb(last_place(census)) / 2):,}")
    print("   The five zeros are placeholders. They say 'millions', not 'zero'.")
    print()

    print("2. ADDING ONE PERSON TO A POPULATION ESTIMATE")
    print("   3,200,000 + 2 = 3,200,002 exactly. But 'exactly' is not the")
    print("   question -- the question is what you KNOW:")
    place = int(Decimal(1).scaleb(last_place(census)))
    print(f"     known to the {place:>7,} place   (the estimate)")
    print( "     known to the       1 place   (the 2 people, a count)")
    print( "   The sum can be no better than the worse of the two, so it stops")
    print( "   at the hundred-thousands place:")
    with localcontext() as ctx:
        ctx.prec = 2
        print(f"     Decimal('3.2E+6') + Decimal('2')  ->  {Decimal('3.2E+6') + Decimal('2')}")
    print("   The +2 is real, and it is invisible. A window 100,000 wide")
    print("   cannot resolve a step of 2.")
    print()

    print("3. COUNTING THEM")
    rules = [
        ("47.3",    "non-zero digits always count"),
        ("4007",    "zeros BETWEEN digits count"),
        ("0.0052",  "leading zeros never count"),
        ("5.200",   "trailing zeros after a decimal point count"),
        ("2.54",    "an ordinary measurement"),
    ]
    for text, why in rules:
        print(f"     {text:>8}   {sig_figs(text)} s.f.   {why}")
    print()
    print("   And the ambiguous case, which is why scientists stopped writing it:")
    for text, reading in [("3200000", "as written, 7 s.f. -- claims 7 known digits"),
                          ("3.2E+6",  "2 s.f. -- no ambiguity, ever")]:
        print(f"     {text:>8}   {sig_figs(text)} s.f.   {reading}")
    print()

    print("4. MULTIPLY AND DIVIDE: FEWEST SIG FIGS WINS")
    a, b = Decimal("4.56"), Decimal("1.4")
    n = min(sig_figs("4.56"), sig_figs("1.4"))
    print(f"     4.56 x 1.4 = {a * b}        <- what a calculator shows")
    print(f"     inputs have {sig_figs('4.56')} and {sig_figs('1.4')} s.f., so the answer gets {n}")
    print(f"     4.56 x 1.4 = {round_sf(a * b, n)}           <- what you may claim")
    print()

    print("5. ADD AND SUBTRACT: PLACE VALUE WINS (not sig-fig count)")
    print("   This is the rule most people never learn, and it is a different rule.")
    x, y = "12.11", "0.3"
    s = Decimal(x) + Decimal(y)
    stop = max(last_place(x), last_place(y))
    print(f"     {x} + {y} = {s}         <- what a calculator shows")
    print(f"     {x} is known to 10^{last_place(x)}, {y} only to 10^{last_place(y)}")
    print(f"     so the answer stops at 10^{stop}:  {s.quantize(Decimal(1).scaleb(stop))}")
    print(f"     note 12.11 has {sig_figs(x)} s.f. and the answer has {sig_figs(str(s.quantize(Decimal(1).scaleb(stop))))} --")
    print( "     counting sig figs here would have given the wrong answer.")
    print()

    print("6. THE SAME DISTINCTION, IN PYTHON'S FORMAT SPEC")
    v = 3200002
    print(f"     f\"{{v:.2f}}\"   ->  {v:.2f}      2 DECIMAL PLACES (a fixed spot)")
    print(f"     f\"{{v:.2g}}\"   ->  {v:.2g}         2 SIGNIFICANT FIGURES (relative)")
    w = 0.000123456
    print(f"     f\"{{w:.3g}}\"   ->  {w:.3g}     3 s.f. -- correct")
    print(f"     f\"{{w:.3f}}\"   ->  {w:.3f}        3 d.p. -- the number is gone")


if __name__ == "__main__":
    main()
