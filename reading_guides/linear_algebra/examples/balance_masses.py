#!/usr/bin/env python3
"""Two unknown masses from two balances: the first problem in Hefferon's book.

Run:  python3 balance_masses.py

Jim Hefferon's *Linear Algebra* opens with a statics problem. A meter stick
rests on a pivot with three objects on it: one of 2 kg, and two whose masses
h and c are unknown. The stick balances when the moments on the two sides are
equal, where an object's moment is its mass times its distance from the
pivot. One arrangement gives one equation, which is not enough; a second
arrangement gives a second equation, and two are enough for two unknowns.

The program builds each equation from where the objects sit rather than
having it typed in, solves the pair by Gauss's method, and puts the answer
back on both sticks. Every number is a fractions.Fraction, so every step is
exact and "balanced" means equal, not equal to fifteen digits.
"""

from fractions import Fraction

KNOWN = {"2 kg": Fraction(2)}
UNKNOWNS = ("h", "c")

# Where each object sits, in cm from the pivot: negative is left, positive right.
BALANCES = {
    "balance 1": {"h": -40, "c": -15, "2 kg": 50},
    "balance 2": {"c": -25, "2 kg": 25, "h": 50},
}


def moment(name: str, dist: int) -> str:
    """One object's moment, as written before anything is solved."""
    if name in KNOWN:
        return f"{dist} · {KNOWN[name]}"
    return f"{dist}{name}"


def linear(coeffs: dict[str, Fraction]) -> str:
    """a·h + b·c written the way a textbook writes it: 40h + 15c, -50h + 25c."""
    out = ""
    for name in UNKNOWNS:
        a = coeffs[name]
        if a == 0:
            continue
        size = f"({abs(a)})" if a.denominator != 1 else f"{abs(a)}"
        if not out:
            out = f"{'-' if a < 0 else ''}{size}{name}"
        else:
            out += f" {'-' if a < 0 else '+'} {size}{name}"
    return out


def equation(stick: dict[str, int]) -> tuple[dict[str, Fraction], Fraction]:
    """Left moments = right moments, rearranged to (coefficients of h, c) = number."""
    coeffs = {name: Fraction(0) for name in UNKNOWNS}
    rhs = Fraction(0)
    for name, dist in stick.items():
        if name in KNOWN:
            rhs += KNOWN[name] * dist
        else:
            coeffs[name] -= dist
    return coeffs, rhs


def moments_total(side: list[tuple[str, int]], values: dict[str, Fraction]) -> tuple[str, Fraction]:
    """The moments on one side with every mass known, and their sum."""
    masses = {**KNOWN, **values}
    terms = [f"{abs(d)} · {masses[n]}" for n, d in side]
    return " + ".join(terms), sum(abs(d) * masses[n] for n, d in side)


def main() -> None:
    print("1. EACH BALANCE IS ONE LINEAR EQUATION")
    rows = []
    for label, stick in BALANCES.items():
        left = [(n, d) for n, d in stick.items() if d < 0]
        right = [(n, d) for n, d in stick.items() if d > 0]
        coeffs, rhs = equation(stick)
        rows.append((coeffs, rhs))
        print(f"   {label}")
        print(f"     left of the pivot:    {', '.join(f'{n} at {-d} cm' for n, d in left)}")
        print(f"     right of the pivot:   {', '.join(f'{n} at {d} cm' for n, d in right)}")
        lhs_text = " + ".join(moment(n, -d) for n, d in left)
        rhs_text = " + ".join(moment(n, d) for n, d in right)
        print(f"     left moments = right moments:   {lhs_text} = {rhs_text}")
        print(f"     unknowns on the left:           {linear(coeffs)} = {rhs}")
    print("   Every unknown appears only multiplied by a number and added up.")
    print("   No h², no h·c, no √h: that is what makes the equations linear.")
    print()

    print("2. ONE BALANCE IS NOT ENOUGH")
    (a1, r1), (a2, r2) = rows
    print(f"   Balance 1 alone says {linear(a1)} = {r1}. Try some masses for h:")
    print(f"     {'h':>5}  {'c from balance 1':>16}  {'balance 2 holds?':>16}")
    for h in (Fraction(0), Fraction(1, 4), Fraction(1), Fraction(5, 2)):
        c = (r1 - a1["h"] * h) / a1["c"]
        holds = a2["h"] * h + a2["c"] * c == r2
        print(f"     {str(h):>5}  {str(c):>16}  {str(holds):>16}")
    print("   Every row balances stick 1, and there are infinitely many more:")
    print("   the solutions of one equation in two unknowns fill a whole line.")
    print("   A second, different balance is a second line, and two lines that")
    print("   are not parallel cross at exactly one point.")
    print()

    print("3. GAUSS'S METHOD: REMOVE h FROM ONE ROW, THEN SOLVE")
    print(f"   row 1:   {linear(a1)} = {r1}")
    print(f"   row 2:  {linear(a2)} = {r2}")
    m = -a2["h"] / a1["h"]
    print(f"   Add {m} times row 1 to row 2, because {a2['h']} + {m} · {a1['h']} = 0:")
    a22 = a2["c"] + m * a1["c"]
    r22 = r2 + m * r1
    print(f"     the c term:      {a2['c']} + {m} · {a1['c']} = {a22}")
    print(f"     the right side:  {r2} + {m} · {r1} = {r22}")
    print(f"   row 2 is now:   ({a22})c = {r22}")
    c = r22 / a22
    print(f"   so c = {r22} / ({a22}) = {c}")
    h = (r1 - a1["c"] * c) / a1["h"]
    print(f"   Put c = {c} into row 1:   {a1['h']}h + {a1['c']} · {c} = {r1},  so {a1['h']}h = {r1 - a1['c'] * c}  and  h = {h}")
    print("   With a thousand unknowns the steps are the same, only more of them.")
    print()

    print("4. PUT THE ANSWER BACK ON BOTH STICKS")
    values = {"h": h, "c": c}
    print(f"   h = {h} kg,  c = {c} kg")
    for label, stick in BALANCES.items():
        left_text, left_sum = moments_total([(n, d) for n, d in stick.items() if d < 0], values)
        right_text, right_sum = moments_total([(n, d) for n, d in stick.items() if d > 0], values)
        print(f"   {label}:  left {left_text} = {left_sum}   right {right_text} = {right_sum}   balanced: {left_sum == right_sum}")


if __name__ == "__main__":
    main()
