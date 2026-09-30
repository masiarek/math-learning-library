#!/usr/bin/env python3
"""Metacognition, measured: how well does a learner judge their own learning?

Run:  python3 metacognition.py

John Flavell's 1976 definition of metacognition lists four abilities: to think
about your own thinking, to be aware of yourself as a problem solver, to
monitor, plan and control your mental processing, and to judge accurately how
much you have learned. The last one is a claim that can be checked. Before
answering each question, write down how sure you are; after answering, mark
it right or wrong. A learner whose 90% answers are right 9 times in 10 is
calibrated. One whose 90% answers are right 5 times in 10 does not know what
they know, and will stop studying too soon.

The two learners below are invented, and say so. Their pattern is the one the
research reports: rereading makes material feel familiar, and familiarity
feels like knowing. Replace ANSWERS_AFTER_REREADING with your own
(confidence, right) pairs to score yourself.

Every score is computed in exact fractions, so the output never depends on
the machine.
"""

from fractions import Fraction

# (confidence in percent, answered correctly?) for 20 questions from this
# library, such as "is the converse of a true statement true?" or "how many
# significant figures does 0.0520 have?". Invented data.
ANSWERS_AFTER_REREADING = [
    (100, True), (100, False), (90, True), (90, False), (100, True),
    (90, True), (90, False), (100, True), (80, False), (90, True),
    (100, False), (90, True), (80, True), (90, False), (100, True),
    (90, False), (80, True), (100, False), (90, True), (80, False),
]

# The same learner after a week of answering flashcards before looking.
ANSWERS_AFTER_SELF_TESTING = [
    (100, True), (100, True), (90, True), (60, False), (100, True),
    (90, True), (50, False), (100, True), (70, True), (90, True),
    (80, True), (60, True), (90, False), (50, True), (100, True),
    (70, False), (80, True), (60, False), (90, True), (70, True),
]


def pct(x: Fraction) -> str:
    return f"{float(x) * 100:5.1f}%"


def brier(answers) -> Fraction:
    """Mean of (confidence - outcome)^2, outcome 1 if right and 0 if wrong. 0 is perfect."""
    return sum((Fraction(c, 100) - int(ok)) ** 2 for c, ok in answers) / len(answers)


def summary(name, answers) -> None:
    n = len(answers)
    conf = Fraction(sum(c for c, _ in answers), 100 * n)
    acc = Fraction(sum(ok for _, ok in answers), n)
    print(f"   {name}")
    print(f"     mean confidence {pct(conf)}   share right {pct(acc)}   gap {pct(conf - acc)}")
    print(f"     {'said':>9} | {'answers':>7} | {'right':>5} | {'share right':>11}")
    for level in sorted({c for c, _ in answers}, reverse=True):
        group = [ok for c, ok in answers if c == level]
        share = Fraction(sum(group), len(group))
        bar = "#" * round(share * 20)
        print(f"     {level:>8}% | {len(group):>7} | {sum(group):>5} | {pct(share):>11}  {bar}")
    print(f"     Brier score {float(brier(answers)):.3f}   (0 is perfect; saying 50% every time scores 0.250)")
    print()


def main() -> None:
    print("1. FLAVELL'S FOUR ABILITIES, AND THE ONE A PROGRAM CAN CHECK")
    abilities = [
        ("think about your own thinking", "ask: what exactly don't I get?"),
        ("be aware of yourself as a problem solver", "ask: which strategies do I have for this?"),
        ("monitor, plan and control your mental processing", "ask: is this working, and what now?"),
        ("accurately judge your level of learning", "measure it: confidence against results"),
    ]
    for i, (ability, practice) in enumerate(abilities, 1):
        print(f"   {i}. {ability:50} -> {practice}")
    print("   The first three are habits. The fourth is a claim, so it can be tested:")
    print("   say how sure you are before you answer, then compare.")
    print()

    print("2. ONE LEARNER, TWENTY QUESTIONS, TWO WAYS OF STUDYING (invented data)")
    summary("after rereading the notes twice", ANSWERS_AFTER_REREADING)
    summary("after a week of self-testing with flashcards", ANSWERS_AFTER_SELF_TESTING)
    print("   After rereading, the learner says 90-100% and is right about half the time:")
    print("   the page felt familiar, and familiar felt like known. After self-testing,")
    print("   the shares right climb with the confidence, and the gap all but closes.")
    print("   The score improved on both counts: more answers right, and better judged.")
    print()

    print("3. WHY HONEST CONFIDENCE IS THE BEST STRATEGY")
    p = Fraction(7, 10)
    print(f"   Suppose you will in fact get a kind of question right {pct(p).strip()} of the time.")
    print("   The expected Brier score of reporting q is  p(1 - q)^2 + (1 - p)q^2:")
    for q_pct in range(50, 101, 10):
        q = Fraction(q_pct, 100)
        expected = p * (1 - q) ** 2 + (1 - p) * q ** 2
        mark = "  <- smallest" if q == p else ""
        print(f"     report {q_pct:3}%   expected score {float(expected):.3f}{mark}")
    print("   Its derivative, -2p(1 - q) + 2(1 - p)q = 2(q - p), is zero only at q = p.")
    print("   Neither bravado nor modesty pays: the score is lowest for the truth. A rule")
    print("   with that property is called proper, and it is what makes the fourth")
    print("   ability measurable rather than a matter of opinion.")
    print()

    print("4. WHAT MISJUDGING COSTS: WHEN DOES A LEARNER STOP STUDYING?")
    print("   A learner stops a topic once they feel 90% sure. Their real chance of")
    print("   answering right when they feel that sure is the 90% row above:")
    for name, answers in [("after rereading", ANSWERS_AFTER_REREADING),
                          ("after self-testing", ANSWERS_AFTER_SELF_TESTING)]:
        group = [ok for c, ok in answers if c >= 90]
        share = Fraction(sum(group), len(group))
        print(f"     {name:20} feels >= 90% sure on {len(group):2}, right on {sum(group):2}: {pct(share)}")
    print("   The rereader walks into the exam sure of sixteen answers and gets nine.")
    print("   That is the returned paper covered in red ink that McGuire describes, and")
    print("   only a test taken before the exam could have warned of it.")


if __name__ == "__main__":
    main()
