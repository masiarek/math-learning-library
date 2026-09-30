#!/usr/bin/env python3
"""Studying vs learning: Bloom's six levels, climbed on one theorem.

Run:  python3 studying_vs_learning.py

Saundra McGuire asks students the difference between studying and learning.
One answer she quotes: "Studying is focusing on the 'whats,' but learning is
focusing on the 'hows,' 'whys,' and 'what ifs.' ... when I focus on the
'hows,' 'whys,' and 'what ifs,' even if I forget the 'whats,' I can re-create
them."

Bloom's taxonomy, as revised by Anderson and Krathwohl in 2001, names six
levels of working with an idea: remembering, understanding, applying,
analyzing, evaluating, creating. This program does each of them, in turn, to
the Pythagorean theorem, so that the difference between the levels is a
difference in what the code has to do. At the top it re-creates the "whats"
a student at the bottom would have had to memorise.
"""

from math import gcd, isqrt


def is_right(a: int, b: int, c: int) -> bool:
    a, b, c = sorted((a, b, c))
    return a * a + b * b == c * c


def main() -> None:
    print("1. REMEMBERING: recall the fact")
    memorised = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
    print("   'In a right triangle, a^2 + b^2 = c^2.' Common triples, as flashcards:")
    print("   " + ", ".join(str(t) for t in memorised))
    print("   Enough to answer 'state the theorem'. Nothing more.")
    print()

    print("2. UNDERSTANDING: say why it holds, in your own terms")
    a, b = 3, 4
    big = (a + b) ** 2
    four_triangles = 4 * (a * b // 2)
    print(f"   Put four copies of the ({a}, {b}) triangle inside a square of side {a} + {b}.")
    print(f"   The big square has area {big}; the four triangles take {four_triangles};")
    print(f"   the tilted square left in the middle has area {big} - {four_triangles} = {big - four_triangles} = 5^2.")
    print(f"   In letters: (a + b)^2 - 2ab = a^2 + b^2, and the middle square is c^2.")
    print()

    print("3. APPLYING: use it on a new problem")
    ladder, foot = 13, 5
    print(f"   A {ladder} m ladder stands {foot} m from a wall. How high does it reach?")
    print(f"   sqrt({ladder}^2 - {foot}^2) = sqrt({ladder * ladder - foot * foot}) = {isqrt(ladder * ladder - foot * foot)} m.")
    print()

    print("4. ANALYZING: take the claim apart; what does each piece do?")
    for t in [(5, 12, 13), (5, 12, 12), (5, 12, 14)]:
        a, b, c = t
        s, c2 = a * a + b * b, c * c
        kind = "right" if s == c2 else ("acute" if s > c2 else "obtuse")
        print(f"   {t}: a^2 + b^2 = {s:3}, c^2 = {c2:3}  ->  {kind}")
    print("   The comparison does more than the theorem said: it sorts every triangle")
    print("   into three kinds, and it only works if c is the longest side.")
    print()

    print("5. EVALUATING: judge a claim, with evidence")
    claim = "every right triangle with whole sides is a multiple of 3-4-5"
    counter = next((a, b, c) for c in range(1, 50) for b in range(1, c) for a in range(1, b + 1)
                   if is_right(a, b, c) and not (a * 4 == b * 3 and a * 5 == c * 3))
    print(f"   Claim: '{claim}'.")
    print(f"   Verdict: false. First counterexample: {counter}.")
    print()

    print("6. CREATING: build something new that produces the facts")
    print("   Euclid's formula: for m > n > 0, coprime, not both odd,")
    print("   (m^2 - n^2, 2mn, m^2 + n^2) is a right triangle with no common factor.")
    made = []
    for m in range(2, 10):
        for n in range(1, m):
            if gcd(m, n) == 1 and (m - n) % 2 == 1 and m * m + n * n <= 85:
                a, b = sorted((m * m - n * n, 2 * m * n))
                c = m * m + n * n
                assert is_right(a, b, c)
                made.append((c, a, b, m, n))
    for c, a, b, m, n in sorted(made):
        tag = "  <- was a flashcard" if (a, b, c) in memorised else ""
        print(f"   m = {m}, n = {n}:  ({a:2}, {b:2}, {c:2}){tag}")
    brute = sorted((a, b, c) for c in range(1, 86) for b in range(1, c) for a in range(1, b)
                   if is_right(a, b, c) and gcd(a, gcd(b, c)) == 1)
    same = sorted((a, b, c) for c, a, b, _, _ in made) == brute
    print(f"   {len(made)} triples with hypotenuse up to 85, every one checked, from one formula.")
    print(f"   A brute-force search finds {len(brute)} with no common factor; the same ones: {same}.")
    print()

    print("7. WHERE STUDENTS SAY THEY WORKED, AND WHERE THEY SAY THEY MUST")
    print("   McGuire's Figure 4.5: 250 general chemistry students, 2013, after hearing")
    print("   about Bloom's (1956 names). Percent choosing each level:")
    names = ["Knowledge", "Comprehension", "Application", "Analysis", "Synthesis", "Evaluation"]
    school = [21, 35, 25, 13, 3, 3]    # to make As or Bs in high school
    college = [7, 6, 14, 35, 23, 15]   # to make an A in college
    print(f"   {'level':18} {'high school':>11}   {'college':>7}")
    for i, name in enumerate(names):
        print(f"   {i + 1}. {name:15} {school[i]:>10}%  {college[i]:>7}%   {'#' * (school[i] // 2):18} {'#' * (college[i] // 2)}")
    for label, dist in [("high school", school), ("college", college)]:
        mean = sum((i + 1) * p for i, p in enumerate(dist)) / 100
        high = sum(dist[3:])
        print(f"   {label:11}  average level {mean:.2f}, at level 4 or above: {high}%")
    print("   Two questions moved the answer by one and a half levels: most had done well")
    print("   by remembering and understanding, and saw that they would now need to analyze.")
    print()

    print("WHAT CHANGED ON THE WAY UP")
    print("   Level 1 stored three triples. Level 6 stores one formula and re-creates")
    print(f"   those three and {len(made) - len(memorised)} more, on demand. A student who forgets the 'whats'")
    print("   at level 6 can rebuild them; one who forgets them at level 1 has nothing.")


if __name__ == "__main__":
    main()
