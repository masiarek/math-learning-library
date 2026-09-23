#!/usr/bin/env python3
"""Relative error, and what "p correct significant digits" can and cannot mean.

Run:  python3 relative_error.py

Every claim on the page is a line below, run. The pairs 1.00000/1.00499,
9.00000/8.99899, 0.9949/0.9951 and 0.123/0.127 are the textbook's own; the
rest are grids chosen so that a false claim would fail here.
"""

import math
from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal, localcontext
from fractions import Fraction

D = Decimal
F = Fraction


# --- the definitions -------------------------------------------------------

def rel_error(x: Fraction, xhat: Fraction) -> Fraction:
    """E_rel = |x - xhat| / |x|.  Undefined at x = 0."""
    return abs(x - xhat) / abs(x)


def rho(x: Fraction, xhat: Fraction) -> Fraction:
    """The signed relative error: xhat = x(1 + rho)."""
    return xhat / x - 1


def sig_digits(text: str) -> int:
    """The first nonzero digit and everything after it."""
    return len(D(text).as_tuple().digits)


def round_sd(d: Decimal, p: int, rounding=ROUND_HALF_EVEN) -> Decimal:
    """Round to p significant digits."""
    with localcontext() as ctx:
        ctx.prec, ctx.rounding = p, rounding
        return +d


def agree_a(x: Decimal, xhat: Decimal, p: int) -> bool:
    """Definition A: x and xhat round to the same number to p significant digits."""
    return round_sd(x, p) == round_sd(xhat, p)


def half_unit(x: Decimal, p: int) -> Decimal:
    """Half a unit in the p-th significant digit of x."""
    return D(5).scaleb(x.adjusted() - p)


def agree_b(x: Decimal, xhat: Decimal, p: int) -> bool:
    """Definition B: |x - xhat| is less than half a unit in the p-th significant digit of x."""
    return abs(x - xhat) < half_unit(x, p)


def digits_b(x: Decimal, xhat: Decimal) -> int:
    """Definition B is monotone, so it yields a single count."""
    p = 0
    while agree_b(x, xhat, p + 1):
        p += 1
    return p


def yn(flag: bool) -> str:
    return "yes" if flag else "no"


# --- high-precision helpers for the tablemaker's dilemma ---------------------

def dec_pi(prec: int) -> Decimal:
    """Machin: pi = 16 arctan(1/5) - 4 arctan(1/239)."""
    with localcontext() as ctx:
        ctx.prec = prec + 10

        def arctan_inv(n: int) -> Decimal:
            x = D(1) / n
            x2, term, total, k, sign = x * x, x, x, 1, 1
            eps = D(10) ** -(prec + 8)
            while abs(term) > eps:
                term *= x2
                k += 2
                sign = -sign
                total += sign * term / k
            return total

        pi = 16 * arctan_inv(5) - 4 * arctan_inv(239)
    return round_sd(pi, prec)


def dec_sin(x: Decimal, prec: int) -> Decimal:
    """Taylor series, summed with guard digits and rounded once."""
    with localcontext() as ctx:
        ctx.prec = prec + 10
        x2, term, total, k = x * x, x, x, 1
        eps = D(10) ** -(prec + 8)
        while abs(term) > eps:
            k += 2
            term = -term * x2 / ((k - 1) * k)
            total += term
    return round_sd(total, prec)


def digits_needed_to_round(digits: tuple, p: int) -> int:
    """How many digits past the p-th must be read before rounding to p is decided.

    A tail starting 0-3 or 6-9 decides at once. A 5 followed by zeros, or a 4
    followed by nines, has to be read until the run breaks.
    """
    tail = digits[p:]
    first = tail[0]
    if first not in (4, 5):
        return 1
    filler = 0 if first == 5 else 9
    run = 0
    for d in tail[1:]:
        if d != filler:
            break
        run += 1
    return 2 + run


def leading_exponent(x: Fraction) -> int:
    """e such that 10^e <= |x| < 10^(e+1)."""
    x, e = abs(x), 0
    while x >= 10:
        x /= 10
        e += 1
    while x < 1:
        x *= 10
        e -= 1
    return e


def digits_b_exact(x: Fraction, xhat: Fraction) -> int:
    """Definition B on exact fractions: x need not be a finite decimal."""
    e, p = leading_exponent(x), 0
    while abs(x - xhat) < F(5) * F(10) ** (e - p - 1):
        p += 1
    return p


def main() -> None:
    print("1. TWO MEASURES OF ERROR")
    print("   x is the truth, xhat the approximation.")
    pairs = [("1.00000", "1.00499"), ("9.00000", "8.99899"), ("100", "101"),
             ("0.001", "0.002"), ("-2", "-1.9")]
    print(f"     {'x':<10} {'xhat':<10} {'|x - xhat|':<12} {'|x - xhat| / |x|':<18} rho, where xhat = x(1 + rho)")
    all_equal = True
    for xs, hs in pairs:
        x, xh = F(xs), F(hs)
        e_abs, e_rel, r = abs(x - xh), rel_error(x, xh), rho(x, xh)
        all_equal &= e_rel == abs(r)
        print(f"     {xs:<10} {hs:<10} {str(D(e_abs.numerator) / D(e_abs.denominator)):<12} "
              f"{float(e_rel):<18.2e} {float(r):+.2e}")
    print(f"   |rho| equals E_rel in every row (checked with exact fractions): {all_equal}")
    try:
        rel_error(F(0), F("0.001"))
    except ZeroDivisionError:
        print("   At x = 0 the relative error is undefined:  rel_error(0, 0.001) -> ZeroDivisionError")
    print("   Higham's own convention for a signed quantity is 'the error x - xhat', which is -rho times x.")
    print()

    print("2. RELATIVE ERROR DOES NOT CARE ABOUT THE UNITS")
    x, xh = F("1.00000"), F("1.00499")
    base_abs, base_rel = abs(x - xh), rel_error(x, xh)
    print("   x = 1.00000 and xhat = 1.00499, both multiplied by the same alpha:")
    print(f"     {'alpha':<12} {'|x - xhat|':<16} E_rel")
    rel_same = abs_scaled = True
    for label, alpha in [("1", F(1)), ("1000", F(1000)), ("1/7", F(1, 7)), ("1e-9", F(1, 10**9))]:
        ax, axh = alpha * x, alpha * xh
        rel_same &= rel_error(ax, axh) == base_rel
        abs_scaled &= abs(ax - axh) == alpha * base_abs
        print(f"     {label:<12} {float(abs(ax - axh)):<16.3e} {float(rel_error(ax, axh)):.2e}")
    print(f"   E_rel unchanged by every alpha: {rel_same}    absolute error scaled by exactly alpha: {abs_scaled}")
    print("   Metres or kilometres, dollars or cents: the relative error is the same number.")
    print()

    print("3. COUNTING CORRECT DIGITS GIVES ONLY p + 1 POSSIBLE ANSWERS")
    print("   Significant digits: the first nonzero digit and everything after it.")
    for text in ("1.7320", "0.0491"):
        print(f"     {text:<8} {sig_digits(text)} significant digits")
    print("   An approximation written with 5 significant digits can have 0, 1, 2, 3, 4 or 5")
    print("   of them correct: six possible answers. Relative error is a continuous scale.")
    print()
    print("   Two approximations, each correct to 3 digits but not 4, by either definition:")
    print(f"     {'x':<10} {'xhat':<10} {'E_rel':<10} A: p=3  p=4    B: p=3  p=4")
    rels = []
    for xs, hs in pairs[:2]:
        x, xh = D(xs), D(hs)
        e = rel_error(F(xs), F(hs))
        rels.append(e)
        print(f"     {xs:<10} {hs:<10} {float(e):<10.2e} {yn(agree_a(x, xh, 3)):<6} {yn(agree_a(x, xh, 4)):<7}"
              f"{yn(agree_b(x, xh, 3)):<6} {yn(agree_b(x, xh, 4))}")
    print(f"   Same digit count; the relative errors differ by a factor of {float(rels[0] / rels[1]):.1f}.")
    print()

    print("4. DEFINITION A: p CORRECT DIGITS IF x AND xhat ROUND TO THE SAME p-DIGIT NUMBER")
    x, xh = D("0.9949"), D("0.9951")
    print("   x = 0.9949, xhat = 0.9951")
    print(f"     {'p':<4} {'x rounds to':<14} {'xhat rounds to':<16} agree?")
    for p in range(1, 5):
        print(f"     {p:<4} {str(round_sd(x, p)):<14} {str(round_sd(xh, p)):<16} {yn(agree_a(x, xh, p))}")
    print("   One and three correct digits, but not two. A count that is not monotone is not a count.")
    print()

    print("5. DEFINITION B: |x - xhat| IS LESS THAN HALF A UNIT IN THE p-TH SIGNIFICANT DIGIT OF x")
    x, xh = D("0.123"), D("0.127")
    print(f"   x = 0.123, xhat = 0.127, |x - xhat| = {abs(x - xh)}")
    print(f"     {'p':<4} {'unit in digit p':<17} {'half':<9} agree?")
    for p in range(1, 4):
        print(f"     {p:<4} {str(2 * half_unit(x, p)):<17} {str(half_unit(x, p)):<9} {yn(agree_b(x, xh, p))}")
    print("   'Agree to two significant digits', although they round to 0.12 and 0.13.")
    print()
    grid_x = [D(s) for s in ("1.000", "1.234", "2.500", "4.999", "5.000", "7.777", "9.990")]
    grid_rho = [D(m).scaleb(-k) * sign for k in range(1, 8) for m in (1, 2, 5) for sign in (1, -1)]
    grid = [(gx, gx * (1 + gr)) for gx in grid_x for gr in grid_rho]
    monotone = all(not agree_b(gx, gxh, p) or agree_b(gx, gxh, p - 1)
                   for gx, gxh in grid for p in range(2, 9))
    print(f"   Definition B is monotone (p digits implies p - 1 digits), on {len(grid)} pairs: {monotone}")
    x, xh = D("0.9949"), D("0.9951")
    verdicts = ", ".join(f"p={p} {yn(agree_b(x, xh, p))}" for p in range(1, 6))
    print(f"   ...so it has no anomaly:  0.9949 vs 0.9951:  {verdicts}  ->  {digits_b(x, xh)} correct digits")
    print("   Neither definition implies the other:")
    print(f"     0.123  vs 0.127    B: {digits_b(D('0.123'), D('0.127'))} digits;  A at p=2: {yn(agree_a(D('0.123'), D('0.127'), 2))}")
    x, xh = D("0.9946"), D("0.9954")
    print(f"     0.9946 vs 0.9954   A at p=3: {yn(agree_a(x, xh, 3))} (both round to {round_sd(x, 3)});  "
          f"B at p=3: {yn(agree_b(x, xh, 3))} (|x - xhat| = {abs(x - xh)}, half a unit = {half_unit(x, 3)})")
    print()

    print("6. DEFINITION B IS A BAND OF RELATIVE ERROR, ONE DECADE WIDE")
    print(f"   On the same {len(grid)} pairs xhat = x(1 + rho), for p = 1..8:")
    fail_1 = fail_2 = 0
    for gx, gxh in grid:
        e = rel_error(F(str(gx)), F(str(gxh)))
        for p in range(1, 9):
            if e <= F(5, 10 ** (p + 1)) and not agree_b(gx, gxh, p):
                fail_1 += 1
            if agree_b(gx, gxh, p) and not e < F(5, 10 ** p):
                fail_2 += 1
    print(f"     E_rel <= 0.5 x 10^-p   implies   B holds at p        failures: {fail_1}")
    print(f"     B holds at p          implies   E_rel < 5 x 10^-p    failures: {fail_2}")
    print("   The same absolute error under two leading digits:")
    for xs in ("1.000", "9.999"):
        x = D(xs)
        xh = x + D("0.004")
        print(f"     x = {xs}, |x - xhat| = 0.004:  B gives {digits_b(x, xh)} digits,  E_rel = {float(rel_error(F(xs), F(str(xh)))):.1e}")
    print("   '3 correct digits' spans a factor of 10 in relative error. The relative error itself does not.")
    print()

    print("7. VECTORS: A NORM HIDES THE SMALL COMPONENTS")
    vx, vxh = [1.0, 0.001], [1.0001, 0.0011]
    diff = [a - b for a, b in zip(vx, vxh)]
    norms = {
        "inf": (max(abs(d) for d in diff), max(abs(a) for a in vx)),
        "1": (sum(abs(d) for d in diff), sum(abs(a) for a in vx)),
        "2": (math.hypot(*diff), math.hypot(*vx)),
    }
    print("   x = (1, 0.001)   xhat = (1.0001, 0.0011)")
    print(f"     {'norm':<6} ||x - xhat|| / ||x||")
    for name, (num, den) in norms.items():
        print(f"     {name:<6} {num / den:.2e}")
    print("   About four correct digits, says every norm. Component by component:")
    print(f"     {'i':<3} {'x_i':<8} {'xhat_i':<8} {'|x_i - xhat_i|':<16} |x_i - xhat_i| / |x_i|")
    for i, (a, b) in enumerate(zip(vx, vxh), start=1):
        note = "   <- 10% wrong, and invisible above" if i == 2 else ""
        print(f"     {i:<3} {a:<8} {b:<8} {abs(a - b):<16.4g} {abs(a - b) / abs(a):.1e}{note}")
    cw = max(abs(a - b) / abs(a) for a, b in zip(vx, vxh))
    print(f"   componentwise relative error = max_i |x_i - xhat_i| / |x_i| = {cw:.1e}")
    print("   A normwise bound of 1e-4 promises the small component only an ABSOLUTE error")
    print("   of about 1e-4 x ||x||, which is 10% of that component.")
    print()

    print("8. PYTHON'S math.isclose IS A RELATIVE-ERROR TEST")
    print("   isclose(a, b, rel_tol=r) is  |a - b| <= r x max(|a|, |b|)   (abs_tol defaults to 0)")
    for a, b, r in [(1.00000, 1.00499, 5e-3), (1.00000, 1.00499, 4e-3), (9.00000, 8.99899, 4e-3)]:
        print(f"     isclose({a:.5f}, {b:.5f}, rel_tol={r:.0e})   {str(math.isclose(a, b, rel_tol=r)):<6} "
              f"|a - b| / max = {abs(a - b) / max(abs(a), abs(b)):.2e}")
    print("   It divides by the larger of the two, so it cannot tell which one is the truth.")
    print("   E_rel divides by the truth, and the two can differ (section 11, kata 1).")
    print()

    print("9. ROUNDING INTO A FLOAT IS A RELATIVE ERROR, AND A BOUNDED ONE")
    u = F(1, 2**53)
    print("   binary64 keeps 53 significant bits. Rounding a real x to the nearest float gives")
    print("   fl(x) = x(1 + rho) with |rho| <= u = 2^-53 = 1.11e-16, the unit roundoff.")
    reals = [F(k, 7) for k in range(1, 1001)] + [F(k, 1000) for k in range(1, 1001)]
    worst = max(abs(rho(r, F(float(r)))) for r in reals)
    print(f"   Checked exactly on {len(reals):,} values k/7 and k/1000:")
    print(f"     largest |rho| seen  {float(worst):.2e}     <= 2^-53: {worst <= u}")
    print("   And every single operation:  fl(a op b) = (a op b)(1 + delta),  |delta| <= u.")
    floats = [k / 7 for k in range(1, 21)] + [k / 10 for k in range(1, 21)] + [3.0 ** k for k in range(-10, 11)]
    ops = {"+": (lambda a, b: a + b), "-": (lambda a, b: a - b),
           "x": (lambda a, b: a * b), "/": (lambda a, b: a / b)}
    checks, worst_delta = 0, F(0)
    for a in floats:
        for b in floats:
            fa, fb = F(a), F(b)
            for sym, op in ops.items():
                exact = op(fa, fb)
                if exact == 0:
                    continue
                checks += 1
                worst_delta = max(worst_delta, abs(rho(exact, F(op(a, b)))))
    print(f"     checked +, -, x, / on {len(floats)}^2 pairs of floats ({checks:,} results; exact zeros skipped):")
    print(f"     largest |delta| seen  {float(worst_delta):.2e}     <= 2^-53: {worst_delta <= u}")
    inexact = [r for r in reals if F(float(r)) != r]
    counts = [digits_b_exact(r, F(float(r))) for r in inexact]
    print(f"   Correct decimal digits of fl(x), by definition B, over the {len(inexact):,} inexact values:")
    print(f"     fewest {min(counts)}, most {max(counts)}.  "
          f"Section 6 promised at least 15, since u <= 0.5 x 10^-15.")
    print()

    print("10. THE TABLEMAKER'S DILEMMA")
    print("   Tabulate y = exp(pi x sqrt(163)) to t significant digits")
    print("   (computed with five guard digits, then rounded to nearest):")
    print(f"     {'t':<5} y")
    for t in (10, 15, 20, 25, 30, 35, 40):
        with localcontext() as ctx:
            ctx.prec = t + 5
            y = (dec_pi(t + 5) * D(163).sqrt()).exp()
        print(f"     {t:<5} {round_sd(y, t):f}")
    print("   Is the last digit before the point a 4 or a 3? Every table up to t = 25 says 4.")
    print("   It is 3, followed by twelve 9s. Rounded to the nearest integer the entry is ...744,")
    print("   but a table that prints the integer part cannot settle it with fewer than 30 digits,")
    print("   and nothing about the number said in advance how many digits that would take.")
    print()
    x = D("0.01550025")
    print("   An exact tie needs an algebraic value:")
    print(f"     sqrt({x}) = {x.sqrt()} exactly, so to 3 digits it is "
          f"{round_sd(x.sqrt(), 3)} (ties to even) or {round_sd(x.sqrt(), 3, ROUND_HALF_UP)} (ties away):")
    print("     more digits will never settle it; only the tie rule does.")
    print()
    print("   A transcendental value is never exactly a tie, but it can sit as close as it likes.")
    print("   Tabulating sin(k/1000) for k = 1..1000 to 4 significant digits, the digits past the")
    print("   fourth were read until the rounding was decided:")
    histogram: dict[int, int] = {}
    hardest = (0, 0, None)
    for k in range(1, 1001):
        s = dec_sin(D(k).scaleb(-3), 40)
        digits = s.as_tuple().digits
        digits = digits + (0,) * (40 - len(digits))
        needed = digits_needed_to_round(digits, 4)
        histogram[needed] = histogram.get(needed, 0) + 1
        if needed > hardest[0]:
            hardest = (needed, k, digits)
    print(f"     {'digits read':<13} entries")
    for needed in sorted(histogram):
        print(f"     {needed:<13} {histogram[needed]}")
    needed, k, digits = hardest
    shown = "".join(map(str, digits[:4])) + "|" + "".join(map(str, digits[4:4 + needed + 2]))
    print(f"   Hardest entry: sin({D(k).scaleb(-3)}) = 0.{shown}...  needed {needed} digits past the cut.")
    print("   One entry in five needs a second digit, and each digit after that is needed about")
    print("   one time in ten. No entry comes with a bound in advance.")
    print()

    print("11. PRACTICE, SOLVED")
    print("   Kata 1 (Higham, problem 1.1). Measuring against xhat instead of x:")
    print("     E = |x - xhat| / |x|,  E' = |x - xhat| / |xhat|.  With xhat = x(1 + rho):  E' = E / |1 + rho|,")
    print("     so  E / (1 + E) <= E' <= E / (1 - E)  whenever E < 1.")
    holds = True
    for m in range(1, 100):
        for sign in (1, -1):
            r = F(sign * m, 100)
            x = F(3)
            xh = x * (1 + r)
            e, e2 = rel_error(x, xh), rel_error(xh, x)
            holds &= e / (1 + e) <= e2 <= e / (1 - e)
    print(f"     checked for rho = -0.99 .. 0.99 in steps of 0.01: {holds}")
    for r in (F(1, 2), F(-1, 2)):
        x = F(3)
        xh = x * (1 + r)
        print(f"     rho = {float(r):+.1f}:  E = {float(rel_error(x, xh)):.3f}   E' = {float(rel_error(xh, x)):.3f}")
    print("     Small errors: the two agree to first order. Large ones: it matters what you divide by.")
    print()
    print("   Kata 2. Truth x = 3,213,468 (a count), estimate xhat = 3,200,000:")
    x, xh = D("3213468"), D("3200000")
    e = rel_error(F(3213468), F(3200000))
    a_digits = max(p for p in range(0, 8) if p == 0 or agree_a(x, xh, p))
    print(f"     E_abs = {abs(x - xh):,}     E_rel = {float(e):.2e}")
    print(f"     A: {a_digits} correct digits ({round_sd(x, 2)} vs {round_sd(xh, 2)}; at p=3, {round_sd(x, 3)} vs {round_sd(xh, 3)})")
    print(f"     B: {digits_b(x, xh)} correct digits (half a unit in the 2nd digit is {half_unit(x, 2):,f}; in the 3rd, {half_unit(x, 3):,f})")
    print()
    print("   Kata 3. x = (1000, 1, 0.001), xhat = (1000.1, 1.001, 0.0011):")
    vx, vxh = [1000.0, 1.0, 0.001], [1000.1, 1.001, 0.0011]
    diff = [a - b for a, b in zip(vx, vxh)]
    normwise = max(abs(d) for d in diff) / max(abs(a) for a in vx)
    per = [abs(a - b) / abs(a) for a, b in zip(vx, vxh)]
    print(f"     normwise (inf-norm)   {normwise:.1e}")
    print(f"     per component         {', '.join(f'{v:.1e}' for v in per)}")
    print(f"     componentwise         {max(per):.1e}")
    print("     The normwise 1e-4 certifies four digits of the first component only; the third is 10% off.")


if __name__ == "__main__":
    main()
