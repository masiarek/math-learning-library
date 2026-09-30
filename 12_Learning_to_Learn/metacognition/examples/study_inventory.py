#!/usr/bin/env python3
"""Saundra McGuire's behavior inventory: eleven true-or-false statements about
how you study, and the grade they predict.

Run:  python3 study_inventory.py              the inventory, and an example
      python3 study_inventory.py TFTTFFTTFTT  your own answers, in order

Every statement is something you do, not something you are. That is the
point McGuire makes about it: "you can change your predicted grade at any
point by changing your behavior such that more of the statements are true."
The scale is her rule of thumb, not a validated test, and the statements
are shortened from the book's.
"""

import sys

STATEMENTS = [
    "I always preview the material before I go to class.",
    "I go over my lecture notes as soon as possible after lecture.",
    "I do homework without example problems or copying from notes or book.",
    "I regularly go to office hours or tutoring about the homework.",
    "I rework all of the homework problems before the test or quiz.",
    "I study for this class at least five days per week, outside class.",
    "I make mnemonics to help me remember facts and equations.",
    "I make diagrams or mental pictures of the concepts from class.",
    "I am in a study group where we do homework and quiz ourselves.",
    "I rework every missed quiz and test item before the next class.",
    "I can still do well even if I have done poorly so far.",
]

# (fewest true answers for this grade, grade)
SCALE = [(9, "A"), (6, "B"), (4, "C"), (2, "D"), (0, "F")]

# Where each statement is explained in this library's chapter.
WHY = {
    0: "study cycle: preview", 1: "study cycle: review",
    2: "metacognition: answer without looking", 4: "spaced retrieval",
    5: "spaced retrieval: spread out", 9: "metacognition: analyse the gap",
    10: "attribute results to behavior",
}


def grade(trues: int) -> str:
    return next(g for least, g in SCALE if trues >= least)


def score(answers: str) -> int:
    marks = [ch == "T" for ch in answers.upper()]
    for i, (text, mark) in enumerate(zip(STATEMENTS, marks), 1):
        note = f"   <- {WHY[i - 1]}" if not mark and i - 1 in WHY else ""
        print(f"   {i:2}. {'T' if mark else 'F'}  {text}{note}")
    trues = sum(marks)
    print(f"   {trues} true: predicted grade {grade(trues)}")
    return trues


def main() -> None:
    if len(sys.argv) > 1:
        answers = sys.argv[1].upper()
        if len(answers) != len(STATEMENTS) or set(answers) - {"T", "F"}:
            sys.exit(f"give {len(STATEMENTS)} letters, T or F, e.g. TFTTFFTTFTT")
        score(answers)
        return

    print("1. THE SCALE")
    for trues in range(len(STATEMENTS), -1, -1):
        print(f"   {trues:2} true  ->  {grade(trues)}")
    print()

    print("2. AN EXAMPLE STUDENT, BEFORE AND AFTER (invented answers)")
    print("   Before: crams, reworking the homework and making mnemonics the night before.")
    before = score("FFFFTFTFFFF")
    print()
    print("   After: the study cycle and self-testing (the arrows above).")
    after = score("TTTFTTTFFTT")
    print()
    print(f"   Same student, {after - before} behaviors changed, {grade(before)} -> {grade(after)}.")
    print("   Nothing on the list asks how clever you are.")


if __name__ == "__main__":
    main()
