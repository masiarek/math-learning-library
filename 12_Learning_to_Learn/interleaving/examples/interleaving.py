#!/usr/bin/env python3
"""Interleaving: a blocked practice sheet skips the step the exam tests.

Run:  python3 interleaving.py

Four volume formulas, twelve practice problems, two ways to order them:
blocked (all the cylinders, then all the cones, ...) or interleaved (mixed).
The exam mixes them, as exams do. The program counts how often each sheet
makes you decide which formula a problem needs, and scores a student who
never decides: they reuse the formula from the problem before.

Nothing here is random or measured. The sheets are fixed lists, the answers
are exact multiples of pi, and the student is a rule.
"""

from fractions import Fraction as F

# volume / pi for each solid, from its measurements
FORMULAS = {
    "cylinder": lambda r, h: r * r * h,             # pi r^2 h
    "cone":     lambda r, h: F(1, 3) * r * r * h,   # (1/3) pi r^2 h
    "sphere":   lambda r, h: F(4, 3) * r ** 3,      # (4/3) pi r^3
    "hemisphere": lambda r, h: F(2, 3) * r ** 3,    # (2/3) pi r^3
}
SIZES = [(3, 4), (2, 6), (6, 1)]                   # (radius, height) for each problem of a kind
KINDS = list(FORMULAS)

blocked = [(k, r, h) for k in KINDS for r, h in SIZES]
interleaved = [(KINDS[(i + j) % 4], r, h) for j, (r, h) in enumerate(SIZES) for i in range(4)]
exam = [("cone", 5, 3), ("sphere", 3, 0), ("sphere", 1, 0), ("cylinder", 1, 7),
        ("hemisphere", 6, 0), ("cone", 2, 9), ("cylinder", 4, 2), ("hemisphere", 3, 0)]


def choices(sheet):
    """Problems where the kind differs from the one before: a formula must be chosen."""
    return 1 + sum(1 for a, b in zip(sheet, sheet[1:]) if a[0] != b[0])


def shortcut_score(sheet):
    """Read the first problem properly; after that, reuse the previous problem's formula."""
    right = 1
    for before, now in zip(sheet, sheet[1:]):
        kind, r, h = now
        if FORMULAS[before[0]](r, h) == FORMULAS[kind](r, h):
            right += 1
    return right


def show(sheet):
    return ", ".join(k for k, _, _ in sheet)


print("1. The two practice sheets and the exam")
print()
print(f"   blocked:     {show(blocked)}")
print()
print(f"   interleaved: {show(interleaved)}")
print()
print(f"   exam:        {show(exam)}")
print()

print("2. How often each sheet makes you choose the formula")
print()
print("   sheet          problems   a new kind of problem, so a choice to make")
for name, sheet in [("blocked", blocked), ("interleaved", interleaved), ("exam", exam)]:
    c = choices(sheet)
    print(f"   {name:<13}{len(sheet):>9}   {c:>4}  ({c / len(sheet):.0%})")
print()
print("   On the blocked sheet the formula is chosen 4 times in 12 problems; the")
print("   other 8 are the same as the problem before. The exam asks for a choice")
print("   on every problem but one. Interleaved practice rehearses what the exam")
print("   tests; blocked practice rehearses using a formula already chosen.")
print()

print("3. A student who never chooses: 'use the formula from the last problem'")
print()
print("   They work out the first problem properly and then stop choosing.")
print()
print("   sheet          right   of   score")
scores = {}
for name, sheet in [("blocked", blocked), ("interleaved", interleaved), ("exam", exam)]:
    k = shortcut_score(sheet)
    scores[name] = (k, len(sheet))
    print(f"   {name:<13}{k:>6}   {len(sheet):>2}   {k / len(sheet):>5.0%}")
b, e = scores["blocked"], scores["exam"]
print()
print(f"   On the blocked sheet the shortcut scores {b[0]} of {b[1]} without ever telling")
print("   a cone from a cylinder, so the sheet feels easy and the score looks good.")
print(f"   On the interleaved sheet it gets only the first problem, and on the exam")
print(f"   {e[0]} of {e[1]}. A blocked sheet's score predicts the exam badly: it measures")
print("   using a formula, and the exam measures choosing one. The interleaved")
print("   sheet's low score is the honest one, and it is low in practice, where")
print("   it costs nothing.")
print()

print("4. The answers, exact")
print()
print("   kind         r   h   volume")
for kind, r, h in exam:
    v = FORMULAS[kind](r, h)
    hs = str(h) if kind in ("cylinder", "cone") else "-"
    print(f"   {kind:<11}{r:>3}{hs:>4}   {v} pi")
