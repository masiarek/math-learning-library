# Roadmap

What exists, and what is deliberately not written yet. A topic listed here has **no page and no example** — it is a claim about direction, not a stub.

## Written

**[01_Precision](01_Precision/README.md)** — how much of this number is real. Six lessons: [exact vs approximate](01_Precision/exact_vs_approximate/README.md), [significant figures](01_Precision/significant_figures/README.md), [relative error and correct digits](01_Precision/relative_error/README.md), [uncertainty propagation](01_Precision/uncertainty_propagation/README.md), [machine numbers](01_Precision/machine_numbers/README.md), [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**[02_Measure_Zero](02_Measure_Zero/README.md)** — how infinitely many points can take up no room. Six lessons: [what measure zero means](02_Measure_Zero/what_measure_zero_means/README.md), [countable sets](02_Measure_Zero/countable_sets/README.md), [the Cantor set](02_Measure_Zero/cantor_set/README.md), [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md), [the Cantor function](02_Measure_Zero/cantor_function/README.md), [probability zero](02_Measure_Zero/probability_zero/README.md).

**[03_Complex_Numbers](03_Complex_Numbers/README.md)** — what a complex number is, before anyone says √−1. Three lessons: [multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md), [multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md), [roots of unity](03_Complex_Numbers/roots_of_unity/README.md).
**[04_Sets](04_Sets/README.md)** — what a collection is, exactly. Two lessons so far: [the Cartesian product](04_Sets/cartesian_product/README.md), [cardinality of sets](04_Sets/cardinality/README.md).

## The rest of the precision chapter

The six lessons close one argument, but they leave three doors open:

- **Sequences that converge to the wrong limit** — two examples from chapter 1 of the *Handbook of Floating-Point Arithmetic*. Muller's recurrence uₙ = 111 − 1130/uₙ₋₁ + 3000/(uₙ₋₁uₙ₋₂), started at 2 and −4, converges to 6, and computed in floating point heads for 100 instead. The "Chaotic Bank Society" account aₙ = n·aₙ₋₁ − 1, started at e − 1, tends to 0, but e − 1 rounds up to the nearest double and the balance after 25 years comes out as 1.2 × 10⁹ rather than about 0.04. Both are ill-conditioned problems, the kind [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md) says no algorithm escapes. They also carry an argument about reproducibility: on an x86-64 machine, the book's own Table 1.1 matches plain binary64 in rows 3–16 and 80-bit extended intermediates in rows 17–31, so no single run reproduces all of it. The page would need a program that shows the sensitivity, not just the wrong answer.
- **Summation algorithms** — Kahan and Neumaier compensated summation, and pairwise summation. The natural sequel to "error accumulates over ten terms": here is how to add a million of them without it. Nothing in any sibling library covers compensated summation, so this one is genuinely open — though the Rust library's [letting the compiler reorder a float sum ↗](https://masiarek.github.io/rust-learning-library/19_Numbers/letting_the_compiler_reorder/index.html) already owns the adjacent half, that `a + b + c` means `(a + b) + c` and reassociating changes the answer.
- **Interval arithmetic** — carrying a lower and upper bound through every operation instead of a value and a sigma. The uncompromising version of this whole chapter. The Rust library got there first ([Did the rounding decide it? ↗](https://masiarek.github.io/rust-learning-library/09_Advanced/interval_arithmetic/index.html)), and its angle is a good one — because interval error is one-sided, a verdict of *decided* is a proof. A page here would need a different one, or no page.

## The rest of the measure-zero chapter

The six lessons close their argument, and leave two doors open:

- **Two meanings of small** — measure zero is one way to call a set negligible; *meagre*, built from nowhere dense sets, is another. The [fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md) is where they first disagree, and they can disagree completely: the line splits into a meagre set and a set of measure zero. The page would need a program that makes that visible, which is the hard part.
- **Sets with no length at all** — the Vitali set, which cannot be given a length consistently, and so the reason measure theory has to decide which sets get one. Measure zero sidesteps the question, since it only ever measures intervals. But the Vitali set needs the axiom of choice and no program can build it, so by this library's own rule it may never get a page.

## The rest of the complex-numbers chapter

Three lessons define the object, say what it does, and cash the geometry in for the roots of unity. The doors they leave open:

- **The angle itself** — three lessons, and not one angle computed. [Roots of unity](03_Complex_Numbers/roots_of_unity/README.md) got de Moivre's formula and the twelve marks of a clock without one, by carrying √3 as a symbol. Writing z = r(cos θ, sin θ) with θ as a *number* means `atan2`, a float, and every warning in [01_Precision](01_Precision/README.md); and Euler's formula e^{iθ} = cos θ + i sin θ, the reason the polar form is usually written re^{iθ}, needs the power series of the exponential, which is calculus. The chapter's exact-fractions rule has nothing to check there, so a page would need a different angle on the angle.
- **The siblings** — split-complex numbers (change the minus to a plus), dual numbers (drop the y₁y₂ term, and get automatic differentiation for free), and quaternions (do the pair construction twice). [Roots of unity](03_Complex_Numbers/roots_of_unity/README.md) already uses one more member of the family, the rule with +3 in place of −1, which is how it carries a + b√3 exactly. The same program shape as the first lesson, with a different rule each time, and a demonstration of which laws each one loses.
- **Complex floats** — Python's `complex` is two doubles, so every warning in [01_Precision](01_Precision/README.md) applies twice over, and the naive product formula overflows on inputs that the true product does not. Connects the chapter back to chapter 1.
## The rest of the sets chapter

Two lessons are a start, not an argument. The natural next steps, each with an obvious program:

- **Relations and functions** — a function is a subset of A × B with one pair per first entry. The product page builds the pairs; this one would pick out which subsets are functions, and check injective and surjective on finite sets by brute force.
- **Power sets** — every subset of a set, and why there are 2ⁿ of them. The counting argument is the same grid idea as |A × B| = |A| · |B|, one dimension per member. For an infinite set it is Cantor's theorem, |P(A)| > |A|, the diagonal argument from [cardinality](04_Sets/cardinality/README.md) run once more.

## Candidate chapters

Not started, and listed in rough order of how likely they are to earn a place:

- **Probability** — the other discipline built entirely on "how much do you know?", and the natural sequel to uncertainty propagation. Bayes, distributions, and why an interval is a better answer than a number. [Probability zero](02_Measure_Zero/probability_zero/README.md) already opens the door from the continuous side.
- **Proof** — induction, contradiction, construction. The part of mathematics that has nothing to do with computation, included precisely because everything else here does.
- **Discrete** — counting, graphs, recurrences. Best served by runnable examples of anything in this library.
- **Linear algebra** — worth doing only with a strong angle. Conditioning of a matrix connects it straight back to chapter 1, which is the angle.

## Rules for adding a chapter

A chapter earns its place by having an **argument**, not a syllabus. `01_Precision` began as four lessons because that is how many it took to get from "is this just rounding?" to "the textbook quadratic formula is 25% wrong"; it was not four because four is a nice number, and each lesson added since had to answer a question the argument had left open.

Every lesson needs a program. If an idea cannot be demonstrated by something that runs and prints, it may still be a good idea — but it belongs somewhere other than this library.
