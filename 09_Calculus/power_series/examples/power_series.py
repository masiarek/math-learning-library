#!/usr/bin/env python3
"""Power series: the sum that is its own derivative, and where cos and sin come from.

Run:  python3 power_series.py

Suppose e^x can be written as a0 + a1 x + a2 x^2 + a3 x^3 + ..., a polynomial
that never ends. Its derivative, term by term, is a1 + 2 a2 x + 3 a3 x^2 + ...,
and the rule "velocity = position" says the two lists must match:

    a1 = a0,   2 a2 = a1,   3 a3 = a2,   ...    so   ak = a(k-1) / k

With e^0 = 1, a0 = 1 and every coefficient is forced: ak = 1/k!. Put an
imaginary number in, and the terms split into the series for cos and sin.

Coefficients and the partial sums at x = 1 are exact fractions. The rest
compares with math.exp, math.cos and math.sin, printed to six places.
"""

import math
from fractions import Fraction as F


def exp_coefficients(n):
    """a0 = 1 and ak = a(k-1) / k: the only list that is its own derivative."""
    a = [F(1)]
    for k in range(1, n + 1):
        a.append(a[-1] / k)
    return a


def derivative(coeffs):
    """Term by term: the derivative of ak x^k is k ak x^(k-1)."""
    return [k * c for k, c in enumerate(coeffs)][1:]


def evaluate(coeffs, x):
    total = 0
    for c in reversed(coeffs):
        total = total * x + c
    return total


def poly(coeffs, var="x") -> str:
    terms = []
    for k, c in enumerate(coeffs):
        if c == 0:
            continue
        mag = F(abs(c))
        power = "" if k == 0 else var if k == 1 else f"{var}^{k}"
        if not power:
            body = str(mag)
        else:
            num = "" if mag.numerator == 1 else f"{mag.numerator} "
            den = "" if mag.denominator == 1 else f"/{mag.denominator}"
            body = f"{num}{power}{den}"
        terms.append(("-" if c < 0 else "+", body))
    out = ("-" if terms[0][0] == "-" else "") + terms[0][1]
    for sign, body in terms[1:]:
        out += f" {sign} {body}"
    return out


def main() -> None:
    print("1. THE COEFFICIENTS ARE FORCED")
    print("   Matching f = a0 + a1 x + a2 x^2 + ... with its derivative, term by")
    print("   term, gives ak = a(k-1) / k. Starting from e^0 = a0 = 1:")
    a = exp_coefficients(8)
    for k, c in enumerate(a):
        print(f"     a{k} = {str(c):<8} = 1/{k}!")
    print("   So e^x = 1 + x + x^2/2 + x^3/6 + x^4/24 + ... + x^k/k! + ...")
    print()

    print("2. EACH TERM'S DERIVATIVE IS THE TERM BEFORE IT")
    s6 = exp_coefficients(6)
    print(f"     S6(x)  = {poly(s6)}")
    print(f"     S6'(x) = {poly(derivative(s6))}")
    print(f"     S5(x)  = {poly(exp_coefficients(5))}")
    print(f"   S6' = S5: {derivative(s6) == exp_coefficients(5)}. The derivative of the sum up to x^6")
    print("   is the sum up to x^5: every term moves down one place. The sum that")
    print("   never stops is its own derivative.")
    print()

    print("3. AT x = 1 THE SUMS REACH e, FAST")
    total = F(0)
    for k in range(13):
        total += F(1, math.factorial(k))
        if k <= 6 or k % 3 == 0:
            print(f"     terms 0..{k:<2}  sum = {str(total):<22} = {float(total):.10f}")
    print(f"     {'e':<41} = {math.e:.10f}")
    print("   Thirteen terms give nine correct decimals: the term 1/k! shrinks")
    print("   faster than any power of 10. Compounding, (1 + 1/n)^n, needed")
    print("   n = 10^5 steps for four.")
    print()

    print("4. OTHER x: THE TERMS MAY GROW BEFORE THEY SHRINK")
    print(f"     {'x':<6} {'largest term':<20} {'sum of 40 terms':<18} e^x, from math.exp")
    for x in (2, -1, 5, 10):
        terms = [x**k / math.factorial(k) for k in range(40)]
        k_big = max(range(40), key=lambda k: abs(terms[k]))
        print(f"     {x:<6} {'x^%d/%d! = %.3f' % (k_big, k_big, terms[k_big]):<20} {sum(terms):<18.6f} {math.exp(x):.6f}")
    print("   Each term is the one before times x/k, so the terms grow while k is")
    print("   less than x and shrink after. The sum still settles, for every x.")
    print()

    print("5. PUT IN it: THE TERMS SPLIT INTO cos AND sin")
    print("   (it)^k cycles through 1, i, -1, -i as k counts up, so the even terms")
    print("   are real and the odd ones imaginary:")
    n = 12
    cos_c = [a if k % 4 == 0 else -a if k % 4 == 2 else 0 for k, a in enumerate(exp_coefficients(n))]
    sin_c = [a if k % 4 == 1 else -a if k % 4 == 3 else 0 for k, a in enumerate(exp_coefficients(n))]
    print(f"     real part       {poly(cos_c[:9], 't')} ...")
    print(f"     imaginary part  {poly(sin_c[:8], 't')} ...")
    print("   Summed with 30 terms, they are the cosine and the sine, in radians:")
    cos30 = [F(0)] * 30
    sin30 = [F(0)] * 30
    for k, a in enumerate(exp_coefficients(29)):
        if k % 2 == 0:
            cos30[k] = a if k % 4 == 0 else -a
        else:
            sin30[k] = a if k % 4 == 1 else -a
    print(f"     {'t':<6} {'cos series':<12} {'math.cos':<12} {'sin series':<12} math.sin")
    for label, t in (("1", 1.0), ("pi/2", math.pi / 2), ("pi", math.pi), ("2", 2.0)):
        cs = float(evaluate(cos30, t))
        sn = float(evaluate(sin30, t))
        print(f"     {label:<6} {cs + 0.0:<12.6f} {math.cos(t) + 0.0:<12.6f} {sn + 0.0:<12.6f} {math.sin(t) + 0.0:.6f}")
    print("   So e^(it) = cos t + i sin t, Euler's formula, as a fact about")
    print("   coefficients.")
    print()

    print("6. THE DERIVATIVES OF sin AND cos, TERM BY TERM")
    print(f"     d/dt sin t = {poly(derivative(sin_c[:10]), 't')} ...")
    print(f"     cos t      = {poly(cos_c[:9], 't')} ...")
    print(f"   equal: {derivative(sin_c[:10]) == cos_c[:9]}")
    neg_sin = [-c for c in sin_c[:8]]
    print(f"     d/dt cos t = {poly(derivative(cos_c[:9]), 't')} ...")
    print(f"     -sin t     = {poly(neg_sin, 't')} ...")
    print(f"   equal: {derivative(cos_c[:9]) == neg_sin}")
    print("   The same facts the radians lesson measured, now read off the lists.")
    print("   The series speak radians: t in them is the arc length.")


if __name__ == "__main__":
    main()
