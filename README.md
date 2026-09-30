# Math — Learning Library

<!-- --8<-- [start:hero] -->

A learning library for mathematics, built the same way as its siblings [rust-learning-library ↗](https://github.com/masiarek/rust-learning-library) and [star-voting-library ↗](https://github.com/masiarek/star-voting-library): **one idea per page, and every claim backed by a program that actually runs.**

No page here hand-types what a program prints. Each lesson links a real `.py` file; a tool runs it, checks the output against a recorded answer key, and pastes that verified output into the page. CI fails if any of the three drift apart. So when a page says *"this prints `3.2E+6`"*, that is not a promise — it is a test result.

The examples are **stdlib-only, on purpose**. A library about how much of a number is real should not open with a dependency-resolution failure. If you have `python3`, you can run every page in this repo.

📖 **Read it as a site:** <https://masiarek.github.io/math-learning-library/>

<!-- --8<-- [end:hero] -->

<!-- --8<-- [start:below-hero] -->

## Start here

[**01_Precision/**](01_Precision/README.md) — *How much of this number is real?*

The first chapter is a single argument in six steps, and it starts from a question that sounds like it has an obvious answer and does not: **are significant figures just rounding?**

| Lesson | What it teaches |
|---|---|
| [Exact vs approximate](01_Precision/exact_vs_approximate/README.md) | Which numbers have significant figures at all — and why a counted thing has infinitely many |
| [Significant figures](01_Precision/significant_figures/README.md) | What the notation claims, and why the rule for `+` is a *different rule* from the rule for `×` |
| [Relative error and correct digits](01_Precision/relative_error/README.md) | Why "correct to three digits" has no definition that behaves, and the one number to report instead |
| [Uncertainty propagation](01_Precision/uncertainty_propagation/README.md) | The rigorous version those rules approximate, and the two places they lie |
| [Machine numbers](01_Precision/machine_numbers/README.md) | What a float really is — an exact member of a finite set — the five ways to round into it, and which laws of arithmetic survive |
| [Catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md) | The one operation that destroys ten significant figures at once, silently |

Read them in that order; each one answers a question the previous one raises.

[**02_Measure_Zero/**](02_Measure_Zero/README.md) — *How can infinitely many points take up no room?*

The second chapter is about sets so thin that they have zero length, area or volume, even when they hold infinitely many points — even uncountably many. It does not need chapter 1. On the way it meets a set that is full of gaps and still fills half the room, and a staircase that climbs from 0 to 1 while standing still almost everywhere.

| Lesson | What it teaches |
|---|---|
| [What measure zero means](02_Measure_Zero/what_measure_zero_means/README.md) | The definition, which never measures the set itself — and why a segment has no area but does have length |
| [Countable sets](02_Measure_Zero/countable_sets/README.md) | Why the rationals, found inside every interval, still have measure zero |
| [The Cantor set](02_Measure_Zero/cantor_set/README.md) | Uncountably many points, and total length zero |
| [The fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md) | No interval inside it, yet length 1/2 — and why that breaks the Riemann integral |
| [The Cantor function](02_Measure_Zero/cantor_function/README.md) | The devil's staircase: continuous, flat almost everywhere, and still climbing from 0 to 1 |
| [Probability zero](02_Measure_Zero/probability_zero/README.md) | Why probability zero is not impossible, and why on a computer it is |

[**03_Complex_Numbers/**](03_Complex_Numbers/README.md) — *What is a complex number, before anyone says √−1?*

The third chapter builds the complex numbers the way Hamilton did: a complex number is a pair (x, y) of reals, and multiplication is the rule (x₁, y₁) · (x₂, y₂) = (x₁x₂ − y₁y₂, x₁y₂ + x₂y₁). The number whose square is −1 is a consequence of that rule, not an assumption behind it.

| Lesson | What it teaches |
|---|---|
| [Multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md) | The rule, why (0, 1) squares to (−1, 0), why x + yi is the same thing, and where the same rule appears with no complex numbers in sight |
| [Multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md) | Multiplying scales by a length and turns by an angle, so i² = −1 is two quarter turns making a half turn |
| [Multiplication can be undone](03_Complex_Numbers/multiplication_can_be_undone/README.md) | Why pairs are not multiplied entry by entry: zero divisors, and ℂ* as the pairs you can divide by |
| [Roots of unity](03_Complex_Numbers/roots_of_unity/README.md) | Multiplying a unit point by itself walks around the circle in equal steps, so zⁿ = 1 has exactly n solutions: the twelve marks of a clock face, with √3 carried exactly |
| [Euler's identity](03_Complex_Numbers/eulers_identity/README.md) | What e^{iπ} = −1 means, why the exponential can do nothing with an imaginary input but turn, and what the formula is for: the half turn reached exactly, the polar form, and why Python's answer is −1 + 1.2 × 10⁻¹⁶ i |

[**04_Sets/**](04_Sets/README.md) — *What is this collection, exactly?*

The fourth chapter is groundwork: the constructions every other page takes for granted, checked on real sets. It needs nothing from chapters 1 or 2.

| Lesson | What it teaches |
|---|---|
| [The Cartesian product](04_Sets/cartesian_product/README.md) | What ℝ² is, why (2, 5) is not (5, 2), why A × B is not B × A, and why (1, 1) counts |
| [Cardinality of sets](04_Sets/cardinality/README.md) | What \|A\| means, why size is defined by matching, and where it shows up in types, databases and computability |

[**05_Statistics/**](05_Statistics/README.md) — *What does one number say about many?*

The fifth chapter is about the single number that stands in for a list: the average score, the average salary, the average speed. It starts with the names. *Average*, *mean* and *arithmetic mean* are one calculation in a classroom and three different sizes of word outside it. It needs nothing from the other chapters.

| Lesson | What it teaches |
|---|---|
| [Mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md) | Why one calculation has so many names, what the adjective *arithmetic* is for, and why "the average salary" can honestly be three different numbers |

[**06_Algebraic_Structures/**](06_Algebraic_Structures/README.md) — *Why does every book list the same laws?*

The sixth chapter starts from a complaint: a school book lists a + b = b + a for the integers, a linear-algebra book lists u + v = v + u for vectors, and then lists the same laws again for linear maps. The answer is that there are only four laws to list, and the chapter follows the tools that stop the repetition: a definition that any set can pass, subsets that inherit the laws, and maps that carry them across. It needs school algebra; lessons 2 to 4 are easier after a first look at vectors.

| Lesson | What it teaches |
|---|---|
| [The laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md) | The four laws every book reprints, the names for their combinations, and a witness for every law that fails, from subtraction to floats |
| [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) | The vector-space axioms run against five candidates, and why 0v = 0, proved once, says x⁰ = 1 in a space where adding means multiplying |
| [Subsets inherit the laws](06_Algebraic_Structures/subsets_inherit_the_laws/README.md) | Why a subspace needs three checks instead of eight, and why a subgroup needs a fourth |
| [Maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md) | Linear maps, logarithms, determinants and string length as one shape; 2⁰ = 1, log 1 = 0, T(0) = 0 and det I = 1 as one proof; and the slide rule as an isomorphism |

[**07_Linear_Systems/**](07_Linear_Systems/README.md) — *What does it mean to solve a system of equations?*

The seventh chapter follows the first section of Jim Hefferon's *Linear Algebra*. Before any method, it says what is being looked for: a linear equation is a test that a list of numbers passes or fails, and a solution of a system passes every test at once. It needs nothing but school algebra.

| Lesson | What it teaches |
|---|---|
| [Linear equations and their solutions](07_Linear_Systems/linear_equations/README.md) | Hefferon's Definition 1.1 symbol by symbol: coefficients, constants, tuples and the double subscripts aᵢ,ⱼ, checked on two balances and a system in three unknowns, and why *linear* means keeping sums and multiples |

[**08_Analytic_Geometry/**](08_Analytic_Geometry/README.md) — *What does it mean to draw a number?*

The eighth chapter is the first page of every precalculus book: two number lines at right angles turn each point of the plane into a pair of numbers, and each pair into a point. Every lesson ends with the book's questions, answers folded away, and a deck of Anki flashcards. It needs nothing but a number line.

| Lesson | What it teaches |
|---|---|
| [Rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md) | A point is two signed distances, and from the other axis than you expect; a quadrant is the pair of signs and nothing more, so the axes belong to none; and why that one word runs through trigonometry, complex numbers and the symmetry of graphs |

[**09_Calculus/**](09_Calculus/README.md) — *What is a velocity, and which motion is its own velocity?*

The ninth chapter is calculus as motion, the four pieces the talk behind [Euler's identity](03_Complex_Numbers/eulers_identity/README.md) leans on. Lost in that talk? [Euler's formula: a lesson plan](reading_guides/eulers_formula/README.md) says what to learn first, step by step, and which lesson here teaches each step.

| Lesson | What it teaches |
|---|---|
| [The derivative is a velocity](09_Calculus/derivative_as_velocity/README.md) | The velocity at an instant is what average velocities settle on, exactly 6 + h for t² at t = 3; and why a float derivative cannot shrink its step for ever |
| [Velocity equals position](09_Calculus/velocity_equals_position/README.md) | Start at 1 and always move as fast as your position: that is e^t, e is where you are at time 1, and the law of exponents, "double" and "flip and squish" follow |
| [Radians](09_Calculus/radians/README.md) | Archimedes' polygons measure the circle, a radian is one radius of arc, and in radians the angle is the distance walked, so d/dt sin t = cos t |
| [Power series](09_Calculus/power_series/README.md) | "Velocity = position" forces every coefficient of e^x to be 1/k!, and with an imaginary input the terms split into cos and sin |

**Looking for a subject rather than a chapter?** The [topic map](TOPICS.md) sorts every lesson into branches and follows the threads that run between chapters.

## Why a math library and not a Python one

The code here is the *illustration*, never the subject. Mathematics is exact — `1/3` is exactly one third, forever — and that is precisely why a chapter on significant figures has to explain that they are **not** a mathematical idea but a measurement one, living in the gap between the world and the arithmetic.

Python earns its place because it happens to encode several of these distinctions in syntax you can run: `:.2f` versus `:.2g` is decimal places versus significant figures, and `decimal.getcontext().prec` is the only knob in the standard library that counts significant digits. Those are good teaching instruments. They are not the lesson.

## How the library works

```
01_Precision/
  significant_figures/
    README.md                          the lesson  (prose + a generated output block)
    examples/
      significant_figures.py           the program a reader can run
      significant_figures.out          its recorded output — the answer key
```

A lesson page never pastes output by hand. It marks the spot:

```markdown
<!-- output:significant_figures -->
<!-- /output -->
```

and `tools/run_examples.py` fills it from a real run. Inside the markers is generated; outside is yours.

```bash
python3 tools/run_examples.py            # verify, and refill the pages
python3 tools/run_examples.py --update   # accept current output as the answer key
python3 tools/run_examples.py --check    # write nothing, fail on drift (what CI runs)
```

There is a second block kind, `source:`, which pastes the program itself for pages where the code *is* the lesson.

Conventions for anyone writing a page: [CONTRIBUTING.md](CONTRIBUTING.md). What is planned and deliberately not written yet: [ROADMAP.md](ROADMAP.md).

<!-- --8<-- [end:below-hero] -->
