# 02_Measure_Zero — how can infinitely many points take up no room?

**Level:** 201 → 301 · for anyone who has met a limit

A single point has no length. That much is easy. The surprise is how far it goes. The rational numbers are infinitely many, crowded into every stretch of the line, and together they still have no length. The Cantor set has as many points as the whole interval [0, 1], and it still has no length. **Measure zero** is the name for this kind of thinness: a set so thin that it has zero length, area or volume, however many points it holds — infinitely many, even uncountably many.

The chapter is one argument in five steps. Each lesson answers a question the previous one raises, so they are worth reading in order.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [What measure zero means](what_measure_zero_means/README.md) | How do you say a set has no length, without measuring it? |
| 2 | [Countable sets](countable_sets/README.md) | Can a set that is everywhere on the line have no length? |
| 3 | [The Cantor set](cantor_set/README.md) | Can a set with as many points as [0, 1] have no length? |
| 4 | [The fat Cantor set](fat_cantor_set/README.md) | If a set has no interval anywhere inside it, must it have no length? |
| 5 | [Probability zero](probability_zero/README.md) | If an event has probability zero, can it still happen? |

## The through-line

**How many points** and **how much room** are different questions. The first has answers like *finite*, *countable*, *uncountable*; the second has answers like *0*, *1/2*, *1*. Lessons 2 and 3 show that having few points is not what makes a set thin: countably many points can take no room, and so can uncountably many. Lesson 4 closes the other door. The fat Cantor set is as riddled with gaps as the Cantor set — no interval anywhere inside it — and it still fills half of [0, 1].

So measure zero is an idea of its own, and a precise one. It is the exact meaning of *negligible* in analysis: a function has a Riemann integral precisely when the places it jumps have measure zero, which is what lesson 4 shows failing. And it is the exact meaning of *negligible* in probability, where lesson 5 turns it into *almost surely* — and then asks what becomes of all this on a computer, which only ever draws from a finite set.

## A note on the code

The examples compute with exact fractions (`fractions.Fraction`), so a printed total is the true total, not a floating-point estimate of it. A chapter about lengths too small to see cannot afford rounding.

But a program only ever checks finitely many things, and measure zero is about infinitely many. So the pages keep a clear line between the two. Where a program checks the first 5,000 intervals, the page says 5,000, and then gives the short proof that covers the rest. The program is the evidence that the pattern is real; the proof is why it never stops.
