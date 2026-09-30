#!/usr/bin/env python3
"""Learned helplessness: a belief that stops you trying never meets the evidence.

Run:  python3 learned_helplessness.py

In Hiroto and Seligman's experiment (1975) one group of students could stop a
loud noise with a button and another group had a button that did nothing.
Later, in a room where a lever stopped the noise, the first group found the
lever and the second mostly did not try.

This program gives a learner the simplest honest rule for judging whether
trying works, Laplace's rule of succession, and a second rule for deciding
whether to try: try when the chance of success is worth the cost. Nothing
else. The helplessness then follows by arithmetic, and so do the book's two
remedies, starting small and watching someone similar succeed, and its three
forms of pessimism read as three ways of counting evidence.

The learner is a model, not a person, and its numbers are not measurements.
All the arithmetic is in exact fractions.
"""

from fractions import Fraction as F

BIG_COST = F(3, 10)     # try a real task when the chance of success is at least this
SMALL_COST = F(1, 20)   # a small step is cheap: worth trying at a much lower chance


def chance(successes, tries):
    """Laplace's rule of succession: after s successes in n tries, (s + 1) / (n + 2)."""
    return (successes + 1) / (F(tries) + 2)


def show(x):
    return f"{str(x):>6} = {float(x):.2f}"


print("1. Judging from a record: the rule of succession")
print()
print("   After s successes in n tries, estimate the chance of success as")
print("   (s + 1) / (n + 2). No evidence gives 1/2; each try moves it.")
print()
print("   record            estimate")
for s, n in [(0, 0), (1, 1), (0, 1), (10, 10), (0, 10), (5, 10)]:
    print(f"   {s:>2} of {n:<2} worked   {show(chance(s, n))}")
print()
print("   One failure gives 1/3, not 0. Ten failures in a row give 1/12.")
print()

print("2. The experiment: ten button presses, then twenty rounds at a lever")
print()
print(f"   Both learners try the lever only if their estimate is at least {BIG_COST}.")
print("   The lever always works. What differs is what the button taught them.")
print()
for name, button_works in [("A, whose button worked", True), ("B, whose button did nothing", False)]:
    s, n = (10 if button_works else 0), 10
    tried = 0
    for _ in range(20):
        if chance(s, n) >= BIG_COST:
            tried += 1
            s, n = s + 1, n + 1        # the lever works whenever it is pulled
    print(f"   {name}")
    print(f"     estimate after the button:  {show(chance(10 if button_works else 0, 10))}")
    print(f"     rounds in which it tried:   {tried} of 20")
    print(f"     estimate after 20 rounds:   {show(chance(s, n))}")
    print()
print("   B's estimate never moves, because only a try produces evidence.")
print("   The lever works every round, and B never finds out. Nothing in B's")
print("   reasoning is wrong: 1/12 is the right conclusion from B's record.")
print("   What is wrong is that the record stopped growing.")
print()

print("3. Remedy one: start small")
print()
print(f"   A small step is worth trying at a chance of {SMALL_COST}, and 1/12 is above")
print("   that, so B tries small steps. Each succeeds and joins the record.")
print()
s, n = 0, 10
step = 0
print("   small successes   estimate      worth a real task?")
while True:
    e = chance(s, n)
    print(f"   {step:>8}          {show(e)}   {'yes' if e >= BIG_COST else 'no'}")
    if e >= BIG_COST:
        break
    s, n, step = s + 1, n + 1, step + 1
print()
print(f"   {step} small successes undo ten failures enough to try the real thing.")
print()

print("4. Remedy two: watch someone similar succeed")
print()
print("   Another person's success counts as evidence in proportion to how much")
print("   like you they are: weight 1 for a classmate in your situation, less")
print("   for someone you do not identify with.")
print()
print("   weight   successes watched before a real try is worth it")
for w in [F(1), F(1, 2), F(1, 4), F(1, 10)]:
    k = 0
    while chance(w * k, 10 + w * k) < BIG_COST:
        k += 1
    print(f"   {str(w):>6}   {k}")
print()
print("   Study Tip 2.2 in numbers: ask someone like you to show you.")
print()

print("5. Two forms of pessimism as two ways of counting")
print()
print("   Pervasiveness: filing the button's ten failures under 'trying never")
print("   works', so they count against the lever too. Kept apart, the lever")
print(f"   starts with no record, estimate {chance(0, 0)}, and B tries it at once.")
print()
print("   Permanence: treating old evidence as if the world never changes. Let")
print("   each round shrink the old record by a factor of 9/10 instead:")
print()
old = F(10)
rounds = 0
print("   round   old failures still counted   estimate")
while True:
    e = 1 / (old + 2)                  # zero successes, 'old' failures
    if rounds % 5 == 0 or e >= BIG_COST:
        print(f"   {rounds:>5}   {float(old):>12.2f}                {float(e):.2f}")
    if e >= BIG_COST:
        break
    old *= F(9, 10)
    rounds += 1
print()
print(f"   Believing 'this is how it will always be', B waits forever; letting")
print(f"   the past fade, B tries the lever after {rounds} rounds, without any new")
print("   success at all.")
print()

print("6. The ABC example: one flunked biology exam")
print()
print("   Belief: 'I am stupid, and I might as well drop out of college.'")
print("   That is a claim about every subject, for ever, with chance 0.")
print(f"   The record is one biology exam, 0 of 1:  biology estimate {chance(0, 1)}.")
print(f"   After help and one passed retake, 1 of 2: biology estimate {chance(1, 2)}.")
print("   Reframed: 'I am not doing well on biology exams right now, and could")
print("   use some help.' That is the belief the evidence supports.")
