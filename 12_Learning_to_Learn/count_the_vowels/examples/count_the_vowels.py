#!/usr/bin/env python3
"""Count the vowels: the task you are given decides what you remember.

Run:  python3 count_the_vowels.py

An exercise from chapter 3 of Saundra McGuire's *Teach Yourself How to Learn*
(Figure 3.3). Fifteen phrases; 45 seconds to count their vowels; then, without
warning, write down as many phrases as you can remember. Workshop groups
recall about 3 of 15. Then the reader is told to look for the organising
principle and given 45 seconds to memorise the list, and the average becomes
12 of 15, with many at 15.

This program does the first task (it counts the vowels, which is the answer
key) and then the second: it finds the principle, checks it, and measures how
much less there is to remember once you know it.

Do the exercise on the page first. Section 2 gives the principle away.
"""

import math

# Figure 3.3, read column by column, top to bottom.
PHRASES = [
    "Dollar bill", "Dice", "Tricycle", "Four-leaf clover", "Hand",
    "Six-pack", "Seven-Up", "Octopus",
    "Cat lives", "Bowling pins", "Football team", "Dozen eggs",
    "Unlucky Friday", "Valentine's Day", "Quarter hour",
]

# What each phrase has one, two, three... of.
NUMBER = {
    "Dollar bill": (1, "one dollar"),
    "Dice": (2, "a pair of dice"),
    "Tricycle": (3, "three wheels"),
    "Four-leaf clover": (4, "four leaves"),
    "Hand": (5, "five fingers"),
    "Six-pack": (6, "six cans"),
    "Seven-Up": (7, "seven, in the name"),
    "Octopus": (8, "eight arms"),
    "Cat lives": (9, "nine lives"),
    "Bowling pins": (10, "ten pins"),
    "Football team": (11, "eleven players on the field"),
    "Dozen eggs": (12, "twelve eggs"),
    "Unlucky Friday": (13, "Friday the 13th"),
    "Valentine's Day": (14, "February 14th"),
    "Quarter hour": (15, "fifteen minutes"),
}

VOWELS = "aeiou"


def vowels(phrase: str) -> int:
    return sum(ch in VOWELS for ch in phrase.lower())


def main() -> None:
    print("1. THE TASK YOU WERE GIVEN: COUNT THE VOWELS (a, e, i, o, u; y not counted)")
    total = 0
    for phrase in PHRASES:
        n = vowels(phrase)
        total += n
        print(f"   {phrase:18} {n:2}   running total {total:3}")
    with_y = sum(ch in VOWELS + "y" for p in PHRASES for ch in p.lower())
    print(f"   Total: {total} vowels ({with_y} if y counts, as in 'Tricycle' and 'Friday').")
    print("   The task never needed the meaning of a single phrase. Letters are all it")
    print("   asked the eyes for, so letters are all the memory was given to keep. In")
    print("   McGuire's workshops the average recall afterwards is 3 phrases of 15: 20%.")
    print()

    print("2. THE ORGANISING PRINCIPLE (spoiler)")
    for phrase in PHRASES:
        n, why = NUMBER[phrase]
        print(f"   {n:2}  {phrase:18} {why}")
    order = [NUMBER[p][0] for p in PHRASES]
    print(f"   Read down the columns and the numbers go {order[0]}, {order[1]}, {order[2]}, ..., {order[-1]}:")
    print(f"   in order, with nothing missing: {order == list(range(1, 16))}.")
    print()

    print("3. COULD THAT ORDER BE AN ACCIDENT?")
    arrangements = math.factorial(15)
    print(f"   15 phrases can be listed in 15! = {arrangements:,} orders.")
    print(f"   Only one of them counts 1 to 15, so a list shuffled at random would do it")
    print(f"   with probability 1/15! = {1 / arrangements:.1e}. The order is a principle, and")
    print("   finding it is the point of looking again.")
    print()

    print("4. HOW MUCH THERE IS TO REMEMBER, BEFORE AND AFTER")
    print("   Without the principle, recall has to find 15 unrelated phrases, and nothing")
    print("   says which one comes next or whether one is missing. With it, recall is a")
    print("   walk through 1, 2, 3, ..., 15, asking at each step 'what comes in n?':")
    for n in [1, 7, 12, 15]:
        phrase = next(p for p in PHRASES if NUMBER[p][0] == n)
        print(f"     what comes in {n:2}?  ->  {phrase}")
    print("   The counting numbers are already in memory, so they cost nothing to store,")
    print("   and each one is a cue for exactly one phrase. A gap shows up at once: if")
    print("   you reach 11 and find nothing, you know that you forgot, and what to search")
    print("   for. That is metacognition inside the recall itself: you can check your")
    print("   own answer, because the principle tells you what a complete answer is.")
    print()

    print("5. THE WORKSHOP'S ARITHMETIC (McGuire's averages)")
    for label, recalled in [("first try, counting vowels", 3), ("second try, knowing goal and rule", 12)]:
        print(f"   {label:35} {recalled:2} / 15 x 100 = {recalled * 100 / 15:3.0f}%")
    print("   Same people, same list, same 45 seconds, and nobody became smarter in")
    print("   between. Two things changed: they knew the goal was to remember, not to")
    print("   count, and they had a principle that organised what they saw.")

if __name__ == "__main__":
    main()
