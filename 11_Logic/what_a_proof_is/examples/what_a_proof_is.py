#!/usr/bin/env python3
"""What a proof is: from what you assume to what you claim, one checked step at a time.

Run:  python3 what_a_proof_is.py

A theorem is a claim about every case in some range. To prove it is to
write a chain of statements from what is given to the claim, each with
its reason: a given, a definition, an earlier line, or a rule that holds
for every value of the letters. The program shows why a loop over cases
is not that (Fermat's five primes; sqrt(t^2) = t on positive t only),
then writes the distance formula as such a chain, checks the chain's
shape (every citation points backwards, no given is the claim, the last
line is the claim), breaks it in three ways to see which checks catch
which, and tries each line that has something to compute on six pairs
of points, exactly.
"""

from fractions import Fraction
from math import isqrt


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def smallest_factor(n):
    return next(d for d in range(2, isqrt(n) + 1) if n % d == 0)


# ---------------------------------------------------------------------------
# A proof as data: what is given, what is claimed, and the lines between.
# A reason is a given's label, an earlier line's number, or one of two words:
# "names", for a line that only introduces letters, and "cases", for a line
# that carries its own argument by cases.
# ---------------------------------------------------------------------------

CLAIM = "d = sqrt((x2 - x1)^2 + (y2 - y1)^2)"

GIVEN = {
    "A1": "Pythagoras: a right triangle with legs a, b and hypotenuse c has c^2 = a^2 + b^2.",
    "A2": "Two points on one horizontal line, (x1, y) and (x2, y), are |x2 - x1| apart; on a vertical line, |y2 - y1|.",
    "A3": "The axes are perpendicular, so a horizontal line and a vertical line meet at a right angle.",
    "D1": "A horizontal line is the set of points with one fixed y, the line y = c; a vertical line has one fixed x.",
    "D2": "sqrt(s) is the non-negative number whose square is s, and a distance is never negative.",
}

WORDS = {"names", "cases"}

LINES = [
    ("Let P1 = (x1, y1), P2 = (x2, y2) be any two points, d their distance, and P3 = (x2, y1).", ["names"]),
    ("P1 and P3 share y1, so P1P3 is horizontal; P3 and P2 share x2, so P3P2 is vertical.", [1, "D1"]),
    ("|P1P3| = |x2 - x1| and |P3P2| = |y2 - y1|.", [2, "A2"]),
    ("Case 1, x1 != x2 and y1 != y2: P1, P2, P3 are three points, and the angle at P3 is right.", [2, "A3"]),
    ("In case 1, d^2 = |x2 - x1|^2 + |y2 - y1|^2.", [3, 4, "A1"]),
    ("For every real t, |t|^2 = t^2: if t >= 0, |t| = t; if t < 0, |t| = -t and (-t)^2 = t^2.", ["cases"]),
    ("In case 1, d^2 = (x2 - x1)^2 + (y2 - y1)^2.", [5, 6]),
    ("Case 2, y1 = y2: P3 = P2, so d = |x2 - x1|, and (x2 - x1)^2 + (y2 - y1)^2 = (x2 - x1)^2 = d^2.", [1, "A2", 6]),
    ("Case 3, x1 = x2: P3 = P1, so d = |y2 - y1|, and (x2 - x1)^2 + (y2 - y1)^2 = (y2 - y1)^2 = d^2.", [1, "A2", 6]),
    ("The cases cover every pair, so d^2 = (x2 - x1)^2 + (y2 - y1)^2; d >= 0, so " + CLAIM + ".", [7, 8, 9, "D2"]),
]


def check_shape(given, lines, claim):
    """The checks a reader makes with a pencil: where does each line point?"""
    problems = []
    for n, (text, reasons) in enumerate(lines, 1):
        if not reasons:
            problems.append(f"line {n} gives no reason")
        for r in reasons:
            if isinstance(r, int):
                if r >= n:
                    problems.append(f"line {n} cites line {r}, which is not established yet")
            elif r not in given and r not in WORDS:
                problems.append(f"line {n} cites {r!r}, which is neither a given nor an earlier line")
    for label, text in given.items():
        if claim in text:
            problems.append(f"given {label} is the claim itself")
    if claim not in lines[-1][0]:
        problems.append("the last line does not state the claim")
    return problems


def show(given, lines, claim, title):
    print(f"   {title}")
    print("   Given:")
    for label, text in given.items():
        print(f"     {label}  {text}")
    print(f"   Claim: {claim}, for every P1 = (x1, y1) and P2 = (x2, y2).")
    for n, (text, reasons) in enumerate(lines, 1):
        because = ", ".join(f"line {r}" if isinstance(r, int) else r for r in reasons)
        print(f"   {n:2}. {text}")
        print(f"       because: {because}")


def verdict(problems):
    if not problems:
        return "OK"
    return "NOT A PROOF\n" + "\n".join(f"     - {p}" for p in problems)


# ---------------------------------------------------------------------------
# What each line says about numbers, when it says anything. A line that only
# applies a given or a definition has nothing to compute: its reason is its
# check. Each function returns True, False, or None for "nothing to compute".
# ---------------------------------------------------------------------------

def numeric_checks(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    p3 = (x2, y1)
    dx, dy = x2 - x1, y2 - y1
    case1 = dx != 0 and dy != 0
    return {
        2: p3[1] == p1[1] and p3[0] == p2[0],
        4: (p3 != p1 and p3 != p2 and p1 != p2) if case1 else None,
        6: abs(dx) ** 2 == dx ** 2 and abs(dy) ** 2 == dy ** 2,
        7: abs(dx) ** 2 + abs(dy) ** 2 == dx ** 2 + dy ** 2,
        8: (dx ** 2 + dy ** 2 == abs(dx) ** 2) if dy == 0 else None,
        9: (dx ** 2 + dy ** 2 == abs(dy) ** 2) if dx == 0 else None,
    }


def fmt(p):
    return "(" + ", ".join(str(c) for c in p) + ")"


def main() -> None:
    print("1. CHECKING CASES IS NOT PROVING: FERMAT'S CLAIM")
    print("   Fermat claimed that 2^(2^n) + 1 is prime for every n. The first cases:")
    for n in range(6):
        f = 2 ** (2 ** n) + 1
        if is_prime(f):
            print(f"   n = {n}: {f:>10}  prime")
        else:
            q = smallest_factor(f)
            print(f"   n = {n}: {f:>10}  = {q} x {f // q}   (Euler found this in 1732)")
    print("   Five cases, each true; the claim about every n is false.")
    print("   No number of cases proves a claim about all n. One case disproves it.")
    print()

    print("2. A LOOP OVER t = 1..1000, AND THE TWO CASES THAT COVER EVERY t")
    loop = all(isqrt(t * t) == t for t in range(1, 1001))
    print(f"   Claim: sqrt(t^2) = t.   Holds for t = 1, 2, ..., 1000: {loop}")
    t = -3
    print(f"   t = {t}: sqrt({t * t}) = {isqrt(t * t)}, not {t}. The loop never reached a negative t.")
    print("   Theorem: sqrt(t^2) = |t| for every real t. Proof, by cases:")
    print("     t >= 0: t^2 has the non-negative root t, and |t| = t.")
    print("     t <  0: t^2 = (-t)^2 and -t > 0, so the root is -t, and |t| = -t.")
    print("   Two cases, and every real t is in one of them: that is what covers all t.")
    both = all(isqrt(t * t) == abs(t) for t in range(-1000, 1001))
    print(f"   Tried on t = -1000..1000, as a check that the cases were copied right: {both}")
    print()

    print("3. THE DISTANCE FORMULA AS A CHAIN: EVERY LINE WITH ITS REASON")
    show(GIVEN, LINES, CLAIM, "The proof, as a list of lines.")
    print("   Shape check: every citation is a given or an earlier line, no given is")
    print(f"   the claim, and the last line states the claim: {verdict(check_shape(GIVEN, LINES, CLAIM))}")
    print("   Do the three cases cover every pair? A truth table over the two tests:")
    print("     x1 = x2   y1 = y2   lands in")
    for ex in (False, True):
        for ey in (False, True):
            cases = []
            if not ex and not ey:
                cases.append("case 1")
            if ey:
                cases.append("case 2")
            if ex:
                cases.append("case 3")
            print(f"     {str(ex):<9} {str(ey):<9} {' and '.join(cases)}")
    print("   Four rows, each in a case: the split is exhaustive, and the table is the proof of that.")
    print()

    print("4. THREE BROKEN CHAINS, AND WHICH CHECK CATCHES EACH")
    circular = list(LINES)
    circular[4] = ("In case 1, d^2 = |x2 - x1|^2 + |y2 - y1|^2.", [3, 4, 7])
    print("   (a) Line 5 cites line 7 instead of A1, and line 7 cites line 5: a circle.")
    print(f"       Shape check: {verdict(check_shape(GIVEN, circular, CLAIM))}")
    assumed = dict(GIVEN)
    assumed["A4"] = "The distance formula: " + CLAIM + "."
    short = [("Let P1 = (x1, y1), P2 = (x2, y2) be any two points and d their distance.", ["names"]),
             ("Then " + CLAIM + ".", ["A4"])]
    print("   (b) Two lines, the second citing a new given A4, which is the distance formula.")
    print(f"       Shape check: {verdict(check_shape(assumed, short, CLAIM))}")
    wrong = list(LINES)
    wrong[6] = ("In case 1, d^2 = (|x2 - x1| + |y2 - y1|)^2.", [5, 6])
    print("   (c) Line 7 reads 'd^2 = (|x2 - x1| + |y2 - y1|)^2', citing lines 5 and 6 as before.")
    print(f"       Shape check: {verdict(check_shape(GIVEN, wrong, CLAIM))}")
    p1, p2 = (Fraction(1), Fraction(3)), (Fraction(5), Fraction(6))
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    five = abs(dx) ** 2 + abs(dy) ** 2
    seven = (abs(dx) + abs(dy)) ** 2
    print(f"       On P1 = (1, 3), P2 = (5, 6): line 5 says d^2 = {five}, the new line 7 says d^2 = {seven}.")
    print("       A line that disagrees with the line it cites, on one example, is wrong: caught by numbers.")
    print("   The shape check reads arrows and knows nothing about numbers. The number check")
    print("   can refute a line and never confirm one. What confirms a line is its reason.")
    print()

    print("5. EACH LINE WITH SOMETHING TO COMPUTE, ON SIX PAIRS OF POINTS")
    pairs = [
        ((1, 3), (5, 6)),
        ((5, 6), (1, 3)),
        ((-2, 4), (5, 4)),
        ((3, -1), (3, -7)),
        ((2, 2), (2, 2)),
        ((Fraction(1, 2), 0), (0, Fraction(1, 2))),
    ]
    computable = sorted(numeric_checks((Fraction(0), Fraction(0)), (Fraction(1), Fraction(1))))
    header = "   P1            P2            " + "  ".join(f"line {n}" for n in computable)
    print(header)
    for a, b in pairs:
        p1 = tuple(Fraction(c) for c in a)
        p2 = tuple(Fraction(c) for c in b)
        results = numeric_checks(p1, p2)
        cells = "  ".join(f"{'-' if results[n] is None else str(results[n]):<6}" for n in computable)
        print(f"   {fmt(a):<13} {fmt(b):<13} {cells}".rstrip())
    print("   A dash: the line's case does not apply to that pair. Lines 1, 3, 5 and 10")
    print("   apply a given or a definition and compute nothing: their reason is the check.")
    print("   Six passes are evidence that the lines were written down right. The proof is the reasons.")


if __name__ == "__main__":
    main()
