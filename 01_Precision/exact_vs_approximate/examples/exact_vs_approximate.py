#!/usr/bin/env python3
"""Exact numbers vs measured numbers — and why only one kind has significant figures.

Run:  python3 exact_vs_approximate.py

The whole chapter rests on this split. Significant figures are bookkeeping for
what an *instrument* could resolve. A number that came from counting, or from a
definition, was never measured, so there is nothing to keep books about.
"""

from decimal import Decimal


def sig_figs(text: str) -> int:
    """How many digits Decimal keeps — which is exactly the sig-fig count."""
    return len(Decimal(text).as_tuple().digits)


def half_width(text: str) -> Decimal:
    """Half of the last kept place: the +/- the notation implies."""
    d = Decimal(text)
    return Decimal(1).scaleb(d.as_tuple().exponent) / 2


def main() -> None:
    print("1. COUNTED THINGS ARE EXACT")
    print("   Nobody 'measures' a ballot. You either have it or you don't.")
    for label, value in [
        ("ballots cast", "1_284"),
        ("inches in a foot", "12"),
        ("trials run", "3"),
    ]:
        print(f"     {label:<20} {value.replace('_', ','):>8}   sig figs: infinite")
    print("   No instrument could refine any of these. There is no last")
    print("   uncertain digit, because there is no uncertain digit at all.")
    print()

    print("2. MEASURED THINGS CARRY THEIR INSTRUMENT")
    print("   The same physical length, three rulers:")
    for text, ruler in [
        ("2.5", "a school ruler, marked in mm"),
        ("2.54", "a vernier caliper"),
        ("2.5400", "a micrometer"),
    ]:
        n = sig_figs(text)
        h = half_width(text)
        lo, hi = Decimal(text) - h, Decimal(text) + h
        span = f"{lo} to {hi}"
        print(f"     {text:>7} cm   {n} s.f.   means {span:<22} ({ruler})")
    print("   Same object. The digits describe the RULER, not the object.")
    print()

    print("3. THE TEST")
    print("   Ask: could a better instrument change this digit?")
    print("     yes -> the digit is measured, and sig figs apply")
    print("     no  -> the number is exact, and sig figs do not")
    print()

    print("4. WHY IT MATTERS IN ARITHMETIC")
    print("   Three measured lengths, averaged. The 3 is a COUNT, so it is")
    print("   exact and does not limit the answer:")
    lengths = ["2.51", "2.47", "2.54"]
    total = sum(Decimal(x) for x in lengths)
    print(f"     ({' + '.join(lengths)}) / 3")
    print(f"     = {total} / 3")
    print(f"     = {total / 3}")
    print(f"     -> 2.51 cm      3 s.f., limited by the RULER, never by the 3")
    print()
    print("   Had the 3 been treated as 1 significant figure, the answer would")
    print("   collapse to 3 cm -- throwing away two digits that were really there.")
    print()

    print("5. THE TRAP")
    print("   A census figure looks counted and is not:")
    print("     '3,200,000 people'  is an ESTIMATE, 2 s.f., +/- 50,000")
    print("     '3,200,002 people'  would be a COUNT, 7 s.f., exact")
    print("   Same units, same object, same digits. Only the method differs,")
    print("   and the method is the entire question.")


if __name__ == "__main__":
    main()
