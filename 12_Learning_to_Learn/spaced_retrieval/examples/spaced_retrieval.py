#!/usr/bin/env python3
"""Spaced retrieval: why the flashcards here come back at growing intervals.

Run:  python3 spaced_retrieval.py

Two findings from a century of memory research drive every flashcard program.
Memory fades, fast at first and then slowly (Ebbinghaus, 1885). And pulling a
fact out of memory strengthens it more than looking at it again does, most of
all when the fact was half forgotten (the testing effect, and the spacing
effect). This program puts both into a toy model, then shows the arithmetic
that makes spacing affordable: when every gap is a fixed multiple of the one
before, the number of reviews grows with the logarithm of how long you want
to remember.

The model's constants are invented to have the right shape; its numbers are
not measurements. The schedule in section 3 is SuperMemo's SM-2, the
algorithm Anki's scheduler started from, as Piotr Wozniak published it in 1987.
"""

import math

FORGET_AT_START = 1.0  # days: the first memory keeps 1/e of its strength after a day
BOOST = 6.0            # how much a review strengthens memory, per unit forgotten


def recall(t: float, stability: float) -> float:
    """The forgetting curve: the chance of recalling a fact t days after the last review."""
    return math.exp(-t / stability)


def study(review_days, test_days):
    """Review at the given days; return the chance of recall on each test day."""
    stability, last = FORGET_AT_START, review_days[0]
    for day in review_days[1:]:
        r = recall(day - last, stability)
        # A review barely helps when the fact is still fresh (r near 1) and
        # helps most when it had nearly slipped: the desirable difficulty.
        stability *= 1 + BOOST * (1 - r)
        last = day
    return [recall(t - last, stability) for t in test_days], stability


def main() -> None:
    print("1. THE FORGETTING CURVE: R = e^(-t/S), WITH S = 1 DAY")
    for t in [0, 1, 2, 3, 7, 30]:
        r = recall(t, FORGET_AT_START)
        print(f"   after {t:2} days  recall {r * 100:5.1f}%  {'#' * round(r * 40)}")
    print("   Half is gone in less than a day. Without a review, a fact met once is")
    print("   as good as lost within a week.")
    print()

    print("2. FOUR REVIEWS EACH, THE SAME EFFORT, DIFFERENT TIMING (toy model)")
    plans = [
        ("crammed: four times on day 0, an hour apart", [0, 1 / 24, 2 / 24, 3 / 24]),
        ("spaced: days 0, 1, 3 and 7", [0, 1, 3, 7]),
        ("spaced wider: days 0, 2, 7 and 16", [0, 2, 7, 16]),
    ]
    tests = [1, 7, 30, 90]
    print(f"   {'plan':46} " + " ".join(f"day {t:>2}" for t in tests) + "   stability")
    for name, days in plans:
        rs, s = study(days, [t + days[-1] for t in tests])
        cells = " ".join(f"{r * 100:5.1f}%" for r in rs)
        print(f"   {name:46} {cells}   {s:6.1f} days")
    print("   (Each test day is counted from the last review, so no plan gets credit for")
    print("   having reviewed later.) Cramming feels productive because every re-read")
    print("   succeeds, and that is exactly why it teaches the memory little: it was never")
    print("   in danger. Spacing lets a fact fade a little before each review.")
    print()

    print("3. HOW A FLASHCARD PROGRAM SPACES REVIEWS: SM-2 (Wozniak, 1987)")
    print("   First gap 1 day, second gap 6 days, then each gap is the last one x 2.5,")
    print("   rounded up, for a card you keep answering right.")
    gaps, day = [1, 6], 7
    while day < 3650:
        gaps.append(math.ceil(gaps[-1] * 2.5))
        day += gaps[-1]
    day = 0
    for n, gap in enumerate(gaps, 1):
        day += gap
        print(f"   review {n:2}   gap {gap:5} days   on day {day:5}  (year {day / 365:4.1f})")
    print()

    print("4. THE COST OF REMEMBERING GROWS LIKE A LOGARITHM")
    print("   After the first two reviews the gaps grow by a factor 2.5, so the days")
    print("   covered form a geometric series: 7 + 15 + 37.5 + ... ~ 7 + 15(2.5^k - 1)/1.5.")
    print("   Keeping a card for T days therefore takes about log(T) / log(2.5) reviews:")
    print(f"   {'keep it for':>11} | {'SM-2 reviews':>12} | {'one review a week':>17}")
    counts = {}
    for years in [1, 2, 5, 10]:
        target, day, count = 365 * years, 0, 0
        for gap in gaps:
            if day >= target:
                break
            day += gap
            count += 1
        counts[years] = count
        label = f"{years} year" + ("s" if years > 1 else "")
        print(f"   {label:>11} | {count:>12} | {math.ceil(target / 7):>17}")
    print("   Keeping a fact 2.5 times as long costs one more review, not 2.5 times as many.")
    print(f"   For a deck of 1000 cards kept a year: {counts[1] * 1000 / 365:.0f} reviews a day on SM-2,")
    print(f"   {math.ceil(365 / 7) * 1000 / 365:.0f} a day on a weekly round. That is the arithmetic behind the Anki")
    print("   decks in this library.")


if __name__ == "__main__":
    main()
