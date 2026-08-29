#!/usr/bin/env python3
"""Catastrophic cancellation: subtraction is where significant figures go to die.

Run:  python3 catastrophic_cancellation.py

Every other operation loses a digit or two. Subtracting two nearly equal numbers
can destroy almost all of them at once -- and it does so silently, leaving an
answer that still LOOKS precise. This is the point where measurement error and
machine error stop being two subjects.
"""

from decimal import Decimal, getcontext
from math import sqrt


def main() -> None:
    getcontext().prec = 50

    print("1. ON PAPER, WITH NO COMPUTER INVOLVED")
    a, b = Decimal("1.2345"), Decimal("1.2344")
    sa = sb = Decimal("0.00005")            # half the last place of each
    diff = a - b
    s_diff = (sa * sa + sb * sb).sqrt()     # independent errors, in quadrature
    print(f"     A = {a}   5 s.f.   +/- {sa}   = {sa / a * 100:.4f}% relative")
    print(f"     B = {b}   5 s.f.   +/- {sb}   = {sb / b * 100:.4f}% relative")
    print(f"     A - B = {diff}                        1 s.f.")
    print(f"     uncertainty +/- {s_diff:.7f}  =  {s_diff / diff * 100:.0f}% relative")
    print(f"     Ten significant figures went in. About one came out.")
    print(f"     Relative error was amplified {(s_diff / diff) / (sa / a):,.0f}x.")
    print()
    print("     Nothing was done wrong. The information simply was not there:")
    print("     both measurements were consistent with a difference of zero.")
    print()

    print("2. THE SAME THING TO A COMPUTER")
    print("   Cancellation does not CREATE error. It removes the large leading")
    print("   digits that were hiding error already there.")
    total = 0.1 + 0.2
    err = Decimal(total) - Decimal("0.3")
    print(f"     0.1 + 0.2 is stored as  {Decimal(total)}")
    print(f"     0.3       is stored as  {Decimal(0.3)}")
    print(f"     the sum is wrong by     {err:.3E}")
    print(f"     which is                {err / Decimal('0.3') * 100:.3E} %  -- invisible")
    print()
    print("   Now subtract. The true answer is exactly zero:")
    print(f"     (0.1 + 0.2) - 0.3  =  {total - 0.3!r}")
    print("     The absolute error did not change. The 0.3 that was masking it")
    print("     is gone, so a rounding artifact is now 100% of the answer.")
    print()

    print("3. THE CLASSIC: THE QUADRATIC FORMULA")
    print("   x^2 + bx + c = 0, with b enormous and c small.")
    b_, c_ = 1e8, 1.0
    disc = sqrt(b_ * b_ - 4 * c_)
    naive = (-b_ + disc) / 2                       # cancels: -b and +disc nearly equal
    stable = -2 * c_ / (b_ + disc)                 # same root, conjugate form, no cancellation

    bd, cd = Decimal(b_), Decimal(c_)
    exact = (-bd + (bd * bd - 4 * cd).sqrt()) / 2

    print(f"     b = {b_:.0e}   c = {c_:.0f}")
    print(f"     sqrt(b^2 - 4c) = {disc!r}")
    print(f"       ...which is b itself to every digit a float can hold.")
    print()
    print(f"     naive   (-b + sqrt(b^2-4c)) / 2   = {naive!r}")
    print(f"     stable  -2c / (b + sqrt(b^2-4c))  = {stable!r}")
    print(f"     exact   (50-digit arithmetic)     = {exact:.17e}")
    rel_naive = abs(Decimal(naive) - exact) / abs(exact) * 100
    rel_stable = abs(Decimal(stable) - exact) / abs(exact) * 100
    print()
    print(f"     naive  is off by {rel_naive:>8.4f}%")
    print(f"     stable is off by {rel_stable:>8.4f}%")
    print("     Same formula, same inputs, same hardware. One subtraction moved.")
    print()

    print("4. CONDITIONING vs STABILITY -- two different faults")
    print("   ill-CONDITIONED problem : small input change -> large output change.")
    print("                             The problem's fault. No algorithm escapes it.")
    print("   un-STABLE algorithm     : the problem is fine; this route through it")
    print("                             is not. Section 3 is this kind, and the fix")
    print("                             was free.")
    print("   Section 1 is the first kind: no cleverness recovers digits that were")
    print("   never measured. Knowing which one you have is the whole skill.")
    print()

    print("5. THE PRACTICAL RULE")
    print("   Whenever you subtract two quantities that are close, stop and ask")
    print("   what the difference is RELATIVE to its own uncertainty. If the")
    print("   answer is 'not much', the digits on your screen are decoration.")


if __name__ == "__main__":
    main()
