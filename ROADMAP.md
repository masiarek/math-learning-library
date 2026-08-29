# Roadmap

What exists, and what is deliberately not written yet. A topic listed here has **no page and no example** — it is a claim about direction, not a stub.

## Written

**[01_Precision](01_Precision/README.md)** — how much of this number is real. Four lessons: [exact vs approximate](01_Precision/exact_vs_approximate/README.md), [significant figures](01_Precision/significant_figures/README.md), [uncertainty propagation](01_Precision/uncertainty_propagation/README.md), [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

## The rest of the precision chapter

The four lessons close one argument, but they leave three doors open:

- **What a float actually stores** — the binary mechanics under lesson 4. The Rust library already has [a thorough page on this ↗](https://masiarek.github.io/rust-learning-library/19_Numbers/what_a_float_stores/index.html); linked from [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md) and the [glossary](GLOSSARY.md) rather than reproduced here. The open question is whether this library ever needs its own — a *math* treatment would be about representable sets and rounding as a function, not about one language's floats. Duplicating the Rust page would be the wrong instinct.
- **Summation algorithms** — Kahan and Neumaier compensated summation, and pairwise summation. The natural sequel to "error accumulates over ten terms": here is how to add a million of them without it. Nothing in any sibling library covers compensated summation, so this one is genuinely open — though the Rust library's [letting the compiler reorder a float sum ↗](https://masiarek.github.io/rust-learning-library/19_Numbers/letting_the_compiler_reorder/index.html) already owns the adjacent half, that `a + b + c` means `(a + b) + c` and reassociating changes the answer.
- **Interval arithmetic** — carrying a lower and upper bound through every operation instead of a value and a sigma. The uncompromising version of this whole chapter. The Rust library got there first ([Did the rounding decide it? ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/interval_arithmetic/index.html)), and its angle is a good one — because interval error is one-sided, a verdict of *decided* is a proof. A page here would need a different one, or no page.

## Candidate chapters

Not started, and listed in rough order of how likely they are to earn a place:

- **Probability** — the other discipline built entirely on "how much do you know?", and the natural sequel to uncertainty propagation. Bayes, distributions, and why an interval is a better answer than a number.
- **Proof** — induction, contradiction, construction. The part of mathematics that has nothing to do with computation, included precisely because everything else here does.
- **Discrete** — counting, graphs, recurrences. Best served by runnable examples of anything in this library.
- **Linear algebra** — worth doing only with a strong angle. Conditioning of a matrix connects it straight back to chapter 1, which is the angle.

## Rules for adding a chapter

A chapter earns its place by having an **argument**, not a syllabus. `01_Precision` is four lessons long because that is how many it took to get from "is this just rounding?" to "the textbook quadratic formula is 25% wrong"; it is not four because four is a nice number.

Every lesson needs a program. If an idea cannot be demonstrated by something that runs and prints, it may still be a good idea — but it belongs somewhere other than this library.
