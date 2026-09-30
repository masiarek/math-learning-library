# Roadmap

What exists, and what is deliberately not written yet. A topic listed here has **no page and no example** — it is a claim about direction, not a stub.

## Written

**[01_Precision](01_Precision/README.md)** — how much of this number is real. Six lessons: [exact vs approximate](01_Precision/exact_vs_approximate/README.md), [significant figures](01_Precision/significant_figures/README.md), [relative error and correct digits](01_Precision/relative_error/README.md), [uncertainty propagation](01_Precision/uncertainty_propagation/README.md), [machine numbers](01_Precision/machine_numbers/README.md), [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**[02_Measure_Zero](02_Measure_Zero/README.md)** — how infinitely many points can take up no room. Six lessons: [what measure zero means](02_Measure_Zero/what_measure_zero_means/README.md), [countable sets](02_Measure_Zero/countable_sets/README.md), [the Cantor set](02_Measure_Zero/cantor_set/README.md), [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md), [the Cantor function](02_Measure_Zero/cantor_function/README.md), [probability zero](02_Measure_Zero/probability_zero/README.md).

**[03_Complex_Numbers](03_Complex_Numbers/README.md)** — what a complex number is, before anyone says √−1. Five lessons: [multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md), [multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md), [multiplication can be undone](03_Complex_Numbers/multiplication_can_be_undone/README.md), [roots of unity](03_Complex_Numbers/roots_of_unity/README.md), [Euler's identity](03_Complex_Numbers/eulers_identity/README.md).

**[04_Sets](04_Sets/README.md)** — what a collection is, exactly. Two lessons so far: [the Cartesian product](04_Sets/cartesian_product/README.md), [cardinality of sets](04_Sets/cardinality/README.md).

**[05_Statistics](05_Statistics/README.md)** — what one number says about many. Two lessons so far: [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md), [a share above a cutoff](05_Statistics/share_above_a_cutoff/README.md).

**[06_Algebraic_Structures](06_Algebraic_Structures/README.md)** — why every book lists the same laws. Four lessons: [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md), [a definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md), [subsets inherit the laws](06_Algebraic_Structures/subsets_inherit_the_laws/README.md), [maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md).

**[07_Linear_Systems](07_Linear_Systems/README.md)** — what it means to solve a system of equations. One lesson so far: [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md).

**[08_Analytic_Geometry](08_Analytic_Geometry/README.md)** — what it means to draw a number. Six lessons, the whole first chapter of Sullivan's *Precalculus*: [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md), [the distance formula](08_Analytic_Geometry/distance_formula/README.md), [the midpoint formula](08_Analytic_Geometry/midpoint_formula/README.md), [graphs, intercepts and symmetry](08_Analytic_Geometry/graphs_intercepts_symmetry/README.md), [lines and slope](08_Analytic_Geometry/lines_and_slope/README.md), [circles](08_Analytic_Geometry/circles/README.md).

**[09_Calculus](09_Calculus/README.md)** — what a velocity is, and which motion is its own. Four lessons: [the derivative is a velocity](09_Calculus/derivative_as_velocity/README.md), [velocity equals position](09_Calculus/velocity_equals_position/README.md), [radians](09_Calculus/radians/README.md), [power series](09_Calculus/power_series/README.md). [Euler's formula: a lesson plan](reading_guides/eulers_formula/README.md) threads them into a path to e^{iπ} = −1.

**[10_Geometry](10_Geometry/README.md)** — how few numbers fix a shape. Three lessons, the precalculus review of geometry: [the Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md), [area and volume formulas](10_Geometry/area_and_volume_formulas/README.md), [congruent and similar triangles](10_Geometry/congruent_and_similar_triangles/README.md).

**[11_Logic](11_Logic/README.md)** — what "if A then B" claims. One lesson so far: [if A then B: converse, contrapositive and inverse](11_Logic/converse_and_contrapositive/README.md).

**[12_Learning_to_Learn](12_Learning_to_Learn/README.md)** — how do you know that you know? Four lessons, after McGuire's *Teach Yourself How to Learn*, chapters 3 and 4: [metacognition](12_Learning_to_Learn/metacognition/README.md), [count the vowels](12_Learning_to_Learn/count_the_vowels/README.md), [studying vs learning](12_Learning_to_Learn/studying_vs_learning/README.md), [spaced retrieval](12_Learning_to_Learn/spaced_retrieval/README.md). The book's chapter 5, the ten metacognitive learning strategies, is the obvious next lesson, if each strategy can be given a program; interleaving (mixing problem types instead of practising one at a time) is the one most clearly worth a page. McGuire's chapter 6, Dweck's fixed and growth mindsets, is not planned as a lesson: no program can demonstrate a belief without invented data, and the effect sizes are disputed, so it stays on the [resources](RESOURCES.md) page. The books are gathered on the [resources](RESOURCES.md) page.

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

Five lessons define the object, say what it does, say why it is this rule, cash the geometry in for the roots of unity, and put the exponential on the plane. The doors they leave open:

- **The exponential itself** — [Euler's identity](03_Complex_Numbers/eulers_identity/README.md) closed the door the first four lessons had left open, the angle as a number, by taking e^{it} to be the limit of compounding, (1 + it/n)ⁿ, and letting lesson 2's "stretches multiply, turns add" do the rest. [09_Calculus](09_Calculus/README.md) now gives the real exponential its own pages, as the motion whose velocity is its position, with the radian and the power series beside it. What is still taken on trust is listed under that chapter below.
- **The siblings** — split-complex numbers (change the minus to a plus), dual numbers (drop the y₁y₂ term, and get automatic differentiation for free), and quaternions (do the pair construction twice). [Roots of unity](03_Complex_Numbers/roots_of_unity/README.md) already uses one more member of the family, the rule with +3 in place of −1, which is how it carries a + b√3 exactly. The same program shape as the first lesson, with a different rule each time, and a demonstration of which laws each one loses.
- **Complex floats** — Python's `complex` is two doubles, so every warning in [01_Precision](01_Precision/README.md) applies twice over, and the naive product formula overflows on inputs that the true product does not. Connects the chapter back to chapter 1.
## The rest of the sets chapter

Two lessons are a start, not an argument. The natural next steps, each with an obvious program:

- **Relations and functions** — a function is a subset of A × B with one pair per first entry. The product page builds the pairs; this one would pick out which subsets are functions, and check injective and surjective on finite sets by brute force.
- **Power sets** — every subset of a set, and why there are 2ⁿ of them. The counting argument is the same grid idea as |A × B| = |A| · |B|, one dimension per member. For an infinite set it is Cantor's theorem, |P(A)| > |A|, the diagonal argument from [cardinality](04_Sets/cardinality/README.md) run once more.

## The rest of the statistics chapter

One lesson settles the names, and a second reads a percentile off a headline. The next steps each have an obvious program:

- **What the median minimises** — the mean is the number that makes the sum of *squared* distances smallest, and the median makes the sum of plain distances as small as it can be. That is the real reason one outlier drags the mean and not the median, and a program can find both minimums by trying every candidate.
- **Weighted means** — a grade-point average, a price index, NumPy's `average` with its `weights`. The arithmetic mean is the special case with every weight equal, and [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md) already met one in disguise: the harmonic mean of two speeds is their mean weighted by time.
- **Spread** — variance and standard deviation, and another pair of names for nearly the same thing: dividing by n or by n − 1, which Python's `statistics` module splits into `pvariance` and `variance`. The quadratic mean from the first lesson is the standard deviation's shape.

## The rest of the algebraic-structures chapter

Four lessons follow the repetition from the list of laws to the maps that carry them. The doors they leave open:

- **Quotients** — the integers modulo n, where 12 + 1 = 1 on a clock. A quotient is the image of a homomorphism, the "images" in Birkhoff's theorem, which [maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md) names but never builds; and ℤ modulo n is a field exactly when n is prime. A program can build the addition and multiplication tables and run lesson 1's checks for each n, which is an obvious page.
- **Products** — ℝ² as ℝ × ℝ with the operations done in each coordinate. It would join this chapter to [the Cartesian product](04_Sets/cartesian_product/README.md), and it is the one construction of Birkhoff's three that the chapter has not touched.
- **Groups of symmetries** — the rotations and reflections of a square, eight of them, composed like the maps of lesson 4 and not commutative. The first group most algebra books draw, and a small enough table to print whole.

## The rest of the linear-systems chapter

One lesson says what a solution is. The rest of Hefferon's first section says how to find one, and each step has an obvious program:

- **Gauss's method keeps the solutions** — swapping two equations, multiplying one by a nonzero number, and adding a multiple of one to another never change the set of solutions. That is the theorem that makes solving legal. A program can check it on tuples before and after each step, and show why multiplying by zero is banned: it turns an equation into 0 = 0 and lets tuples through that failed before. The [reading guide's balance example](reading_guides/linear_algebra/README.md#what-a-first-problem-looks-like) already runs the method once.
- **One, none, or infinitely many** — every linear system has exactly one of three kinds of solution set, and elimination shows which: a single tuple, nothing, or a family like (t, 6 − 2t, t) from the first lesson. Two lines can cross, be parallel, or be the same line, and that picture is the whole proof in two unknowns.
- **Conditioning** — how many significant figures the answer to a system keeps when it is solved in floats. This is the angle the candidate entry below names, and it connects the chapter back to [01_Precision](01_Precision/README.md).

## The rest of the analytic-geometry chapter

Six lessons cover the book's first chapter. The doors they leave open:

- **Graphing utilities** — Sullivan's section 1.1 also teaches a graphing calculator's viewing window. A program could show how a badly chosen window hides intercepts, which is a real argument, but it is about a tool rather than the mathematics.
- **Functions** — the book's chapter 2, and the gap listed under candidate chapters below: the circle is the first graph here that is not the graph of a function, and even and odd functions are the symmetries of lesson 4 renamed.

## Candidate chapters

Not started, and listed in rough order of how likely they are to earn a place:

- **Probability** — the other discipline built entirely on "how much do you know?", and the natural sequel to uncertainty propagation. Bayes, distributions, and why an interval is a better answer than a number. [Probability zero](02_Measure_Zero/probability_zero/README.md) already opens the door from the continuous side, and the expected value would be [the mean](05_Statistics/mean_vs_average/README.md) once more, with probabilities as the weights.
- **Proof** — induction, contradiction, construction; [11_Logic](11_Logic/README.md) has started with the statements proofs are about. The part of mathematics that has nothing to do with computation, included precisely because everything else here does.
- **Discrete** — counting, graphs, recurrences. Best served by runnable examples of anything in this library.
- **Linear algebra, beyond systems** — worth doing only with a strong angle. Conditioning of a matrix connects it straight back to chapter 1, which is the angle, and it is planned as part of [07_Linear_Systems](07_Linear_Systems/README.md). The definitions of a vector space, a subspace and a linear map are already in [06_Algebraic_Structures](06_Algebraic_Structures/README.md), as examples of structures. Until more exists, [a reading guide](reading_guides/linear_algebra/README.md) says why the subject is useful, what to know first, and which book to learn it from.
- **Functions and trigonometry** — the two halves of precalculus, and the widest gap here: every page uses functions and none says what one is, and angles appear only as [radians](09_Calculus/radians/README.md), which calculus needed. A function as a subset of A × B is listed under the sets chapter above. Until more exists, [a reading guide](reading_guides/precalculus/README.md) says what the course is for, where it sits, what to know first, and which book to learn it from.

## Rules for adding a chapter

A chapter earns its place by having an **argument**, not a syllabus. `01_Precision` began as four lessons because that is how many it took to get from "is this just rounding?" to "the textbook quadratic formula is 25% wrong"; it was not four because four is a nice number, and each lesson added since had to answer a question the argument had left open.

Every lesson needs a program. If an idea cannot be demonstrated by something that runs and prints, it may still be a good idea — but it belongs somewhere other than this library.
