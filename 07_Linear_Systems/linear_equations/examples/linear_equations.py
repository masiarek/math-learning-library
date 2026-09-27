#!/usr/bin/env python3
"""Linear equations and their solutions: Hefferon's Definition 1.1, checked.

Run:  python3 linear_equations.py

Definition 1.1 of Jim Hefferon's *Linear Algebra* packs five terms into one
box: linear combination, coefficient, linear equation, solution, and system.
Each one is a small thing to check, so the program checks them one at a time
on a system you can picture: the two balances from the first page of the
book, where h and c are two unknown masses in kg.

An equation is stored the way the definition writes it, as its coefficients
a1, ..., an and its constant d. Every number is a fractions.Fraction, so a
tuple satisfies an equation when the two sides are equal, not nearly equal.
"""

from fractions import Fraction as F

SUBSCRIPT = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def sub(n: int) -> str:
    """1 -> ₁, so a name like a₁,₂ prints the way the book writes it."""
    return str(n).translate(SUBSCRIPT)


def tup(values) -> str:
    """(1, 4) and (5/2, 0), not (Fraction(1, 1), Fraction(4, 1))."""
    return "(" + ", ".join(str(v) for v in values) + ")"


def combination(coeffs, names) -> str:
    """a₁x₁ + a₂x₂ + ... written out: 40h + 15c, -50h + 25c, x₁ + 0x₂ - x₃."""
    out = ""
    for a, x in zip(coeffs, names):
        size = "" if abs(a) == 1 else f"{abs(a)}"
        if not out:
            out = f"{'-' if a < 0 else ''}{size}{x}"
        else:
            out += f" {'-' if a < 0 else '+'} {size}{x}"
    return out


def value(coeffs, point) -> F:
    """a₁s₁ + a₂s₂ + ... + aₙsₙ: substitute the tuple into the combination."""
    return sum((a * s for a, s in zip(coeffs, point)), F(0))


def satisfies(equation, point) -> bool:
    """The definition of a solution: substituting gives a true statement."""
    coeffs, d = equation
    return value(coeffs, point) == d


def yes_no(flag: bool) -> str:
    return "yes" if flag else "no"


# The two balances: 40h + 15c = 100 and -50h + 25c = 50.
NAMES = ("h", "c")
BALANCES = [
    ((F(40), F(15)), F(100)),
    ((F(-50), F(25)), F(50)),
]


def main() -> None:
    first = BALANCES[0]

    print("1. A LINEAR COMBINATION: MULTIPLY EACH VARIABLE BY A FIXED NUMBER, THEN ADD")
    coeffs = first[0]
    print(f"   coefficients a₁ = {coeffs[0]}, a₂ = {coeffs[1]};  variables x₁ = h, x₂ = c")
    print(f"   the combination {combination(coeffs, NAMES)}, worked out at a few (h, c):")
    for point in [(F(1), F(4)), (F(4), F(1)), (F(0), F(0)), (F(1, 2), F(2))]:
        steps = " + ".join(f"{a}·{s}" for a, s in zip(coeffs, point))
        print(f"     {tup(point):<9} {steps} = {value(coeffs, point)}")
    print("   The coefficients stay fixed. Only the numbers put in for h and c change.")
    print()

    print("2. A LINEAR EQUATION IS A TEST THAT A TUPLE PASSES OR FAILS")
    print(f"   equation:  {combination(coeffs, NAMES)} = {first[1]}   (the constant d is {first[1]})")
    print(f"     {'(h, c)':<11} {'left side':>9}   = {first[1]}?")
    candidates = [(F(1), F(4)), (F(4), F(1)), (F(5, 2), F(0)), (F(0), F(20, 3)), (F(1, 4), F(6))]
    for point in candidates:
        note = "   the same two numbers, in the other order" if point == (F(4), F(1)) else ""
        print(f"     {tup(point):<11} {str(value(coeffs, point)):>9}   {yes_no(satisfies(first, point))}{note}")
    passed = sum(satisfies(first, p) for p in candidates)
    print(f"   {passed} of these {len(candidates)} tuples pass. One equation in two unknowns has")
    print("   infinitely many solutions, and together they fill a line.")
    print("   A tuple is ordered: its first entry is always h and its second is c.")
    print()

    print("3. THE DOUBLE SUBSCRIPTS: aᵢ,ⱼ IS EQUATION i, VARIABLE j")
    print("   the system of the two balances:")
    for i, (row, d) in enumerate(BALANCES, start=1):
        print(f"     equation {i}:  {combination(row, NAMES):>11} = {d}")
    print("   the same numbers, each with its name from the definition:")
    print(f"     {'':<9} {'x₁ = h':<13} {'x₂ = c':<13} constant")
    for i, (row, d) in enumerate(BALANCES, start=1):
        cells = [f"a{sub(i)},{sub(j)} = {a}" for j, a in enumerate(row, start=1)]
        print(f"     {'row ' + str(i):<9} {cells[0]:<13} {cells[1]:<13} d{sub(i)} = {d}")
    print(f"   m = {len(BALANCES)} equations, n = {len(NAMES)} unknowns.")
    print("   The first subscript says which equation, the second which variable:")
    print(f"   a₂,₁ = {BALANCES[1][0][0]} is the number in front of x₁ in equation 2.")
    print()

    print("4. A SOLUTION OF THE SYSTEM PASSES EVERY EQUATION")
    print(f"     {'(h, c)':<11} {'equation 1':<12} {'equation 2':<12} system")
    for point in [(F(1), F(4)), (F(5, 2), F(0)), (F(0), F(20, 3)), (F(0), F(2)), (F(2), F(6))]:
        each = [satisfies(eq, point) for eq in BALANCES]
        print(f"     {tup(point):<11} {yes_no(each[0]):<12} {yes_no(each[1]):<12} {yes_no(all(each))}")
    print("   Each equation alone has infinitely many solutions. The system keeps only")
    print("   the tuples that pass both, and of these five only (1, 4) does.")
    print("   Finding it without guessing is the job of Gauss's method.")
    print()

    print("5. THE SAME DEFINITION FOR ANY m AND n")
    names = ("x₁", "x₂", "x₃")
    system = [
        ((F(1), F(1), F(1)), F(6)),
        ((F(1), F(0), F(-1)), F(0)),
    ]
    for i, (row, d) in enumerate(system, start=1):
        print(f"     equation {i}:  {combination(row, names)} = {d}")
    print(f"   m = {len(system)} equations, n = {len(names)} unknowns, so a solution is a triple.")
    print(f"   a₂,₂ = {system[1][0][1]}: a zero coefficient is allowed, and x₂ still has its slot.")
    print(f"     {'(x₁, x₂, x₃)':<15} {'equation 1':<12} {'equation 2':<12} system")
    for point in [(F(1), F(4), F(1)), (F(2), F(2), F(2)), (F(1), F(2), F(3)), (F(6), F(0), F(0))]:
        each = [satisfies(eq, point) for eq in system]
        print(f"     {tup(point):<15} {yes_no(each[0]):<12} {yes_no(each[1]):<12} {yes_no(all(each))}")
    print("   Equation 2 says x₃ = x₁. Put that into equation 1 and x₂ = 6 - 2x₁.")
    print("   So every triple (t, 6 - 2t, t) should pass both. Checking some t:")
    ts = [F(0), F(1), F(3), F(7, 2), F(-5)]
    family = [(t, 6 - 2 * t, t) for t in ts]
    for t, point in zip(ts, family):
        print(f"     t = {str(t):<4}  {tup(point):<15} system: {yes_no(all(satisfies(eq, point) for eq in system))}")
    print("   Fewer equations than unknowns, and a whole line of solutions again.")
    print()

    print("6. WHY 'LINEAR': THE LEFT SIDE KEEPS SUMS AND MULTIPLES")
    s, t = (F(1), F(4)), (F(5, 2), F(0))
    both = tuple(x + y for x, y in zip(s, t))
    triple = tuple(3 * x for x in s)

    def linear_side(p):
        return value(coeffs, p)

    def squared_side(p):
        return p[0] ** 2 + 15 * p[1]

    for label, f in [(f"{combination(coeffs, NAMES)}", linear_side), ("h² + 15c", squared_side)]:
        print(f"   L(h, c) = {label}")
        print(f"     L{tup(s)} = {f(s)},  L{tup(t)} = {f(t)},  their sum = {f(s) + f(t)}")
        print(f"     L{tup(both)} = {f(both)}   sum kept: {yes_no(f(both) == f(s) + f(t))}")
        print(f"     3·L{tup(s)} = {3 * f(s)},  L{tup(triple)} = {f(triple)}   multiple kept: {yes_no(f(triple) == 3 * f(s))}")
    print("   A linear combination keeps both, for every pair of tuples. One squared")
    print("   variable breaks both, and so does h·c, √h or 1/h.")


if __name__ == "__main__":
    main()
