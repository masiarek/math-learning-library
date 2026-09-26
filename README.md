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
| [Roots of unity](03_Complex_Numbers/roots_of_unity/README.md) | Multiplying a unit point by itself walks around the circle in equal steps, so zⁿ = 1 has exactly n solutions: the twelve marks of a clock face, with √3 carried exactly |
[**04_Sets/**](04_Sets/README.md) — *What is this collection, exactly?*

The fourth chapter is groundwork: the constructions every other page takes for granted, checked on real sets. It needs nothing from chapters 1 or 2.

| Lesson | What it teaches |
|---|---|
| [The Cartesian product](04_Sets/cartesian_product/README.md) | What ℝ² is, why (2, 5) is not (5, 2), why A × B is not B × A, and why (1, 1) counts |
| [Cardinality of sets](04_Sets/cardinality/README.md) | What \|A\| means, why size is defined by matching, and where it shows up in types, databases and computability |

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
