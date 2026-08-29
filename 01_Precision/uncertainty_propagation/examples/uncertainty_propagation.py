#!/usr/bin/env python3
"""Uncertainty propagation: the rule significant figures are an approximation of.

Run:  python3 uncertainty_propagation.py

Significant figures compress "how well do I know this?" into a digit count. That
is one number where the honest answer needs two, so the compression is lossy in
both directions -- and this program shows it overstating and understating the
same day.
"""

from math import floor, log10, sqrt


def rel(value: float, sigma: float) -> float:
    return sigma / value


def fmt(value: float, sigma: float) -> str:
    """Show the value only as far as its uncertainty justifies."""
    places = max(0, -int(floor(log10(sigma))) + 1)
    return (f"{value:.{places}f} +/- {sigma:.{places}f}"
            f"  ({rel(value, sigma) * 100:.2f}%)")


def main() -> None:
    print("1. SIG FIGS QUANTIZE UNCERTAINTY VERY COARSELY")
    print("   Two numbers, both written with 2 significant figures:")
    for v in (1.0, 9.9):
        sigma = 0.05                      # half of the last written place
        print(f"     {v:>4}  ->  +/- {sigma}  =  {rel(v, sigma) * 100:>5.2f}% relative")
    print("   Same sig-fig count, a ten-fold difference in what is actually known.")
    print("   Sig figs can only step by factors of 10; reality does not.")
    print()

    print("2. THE REAL RULES")
    print("   For independent random errors, add in QUADRATURE (not linearly):")
    print("     sum / difference   sigma = sqrt(sa^2 + sb^2)          absolute")
    print("     product / quotient  rel  = sqrt(ra^2 + rb^2)          relative")
    print("   Linear addition is the worst case -- correct only if the errors")
    print("   are perfectly correlated, which independent measurements are not.")
    print()

    print("3. A RECTANGLE")
    a, sa = 12.3, 0.1
    b, sb = 4.5, 0.1
    area = a * b
    r = sqrt(rel(a, sa) ** 2 + rel(b, sb) ** 2)
    print(f"     side a   {fmt(a, sa)}")
    print(f"     side b   {fmt(b, sb)}")
    print(f"     area     {fmt(area, area * r)}")
    print(f"     sig-fig answer:  {a} x {b} -> 2 s.f. -> {area:.2g}")
    print("     Here the two roughly agree: the propagated 55.4 +/- 1.3 and the")
    print("     sig-fig '55' make about the same claim. They do not always.")
    print()

    print("4. WHERE SIG FIGS UNDERSTATE -- ACCUMULATION")
    print("   Ten independent measurements, each 1.0 +/- 0.05, added up:")
    n, each, s_each = 10, 1.0, 0.05
    total = n * each
    s_total = sqrt(n) * s_each
    print(f"     sig figs   every term known to the 0.1 place, so the sum is too")
    print(f"                -> {total:.1f}          which CLAIMS +/- {s_each}")
    print(f"     truth      sigma = sqrt({n}) x {s_each} = {s_total:.3f}")
    print(f"                -> {fmt(total, s_total)}")
    print(f"     sig figs claims {s_total / s_each:.1f}x more precision than is there.")
    print("     Error accumulates; the place-value rule cannot see that it has.")
    print()

    print("5. WHERE SIG FIGS OVERSTATE -- A LUCKY LAST DIGIT")
    print("   One measurement, 1.0 +/- 0.05, squared:")
    v, sv = 1.0, 0.05
    sq = v * v
    s_sq = sq * sqrt(2 * rel(v, sv) ** 2)
    print(f"     sig figs   2 s.f. in, 2 s.f. out -> {sq:.1f}   which CLAIMS +/- 0.05")
    print(f"     truth      {fmt(sq, s_sq)}")
    print(f"     the real spread is {s_sq / 0.05:.2f}x wider than the notation admits.")
    print()

    print("6. WHAT TO ACTUALLY DO")
    print("   Sig figs are fine for a one-step classroom calculation and for")
    print("   reporting a single measurement. The moment a value passes through")
    print("   several steps, carry the uncertainty explicitly and round ONCE,")
    print("   at the end -- rounding at every step is itself a source of error.")


if __name__ == "__main__":
    main()
