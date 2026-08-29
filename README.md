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

The first chapter is a single argument in four steps, and it starts from a question that sounds like it has an obvious answer and does not: **are significant figures just rounding?**

| Lesson | What it teaches |
|---|---|
| [Exact vs approximate](01_Precision/exact_vs_approximate/README.md) | Which numbers have significant figures at all — and why a counted thing has infinitely many |
| [Significant figures](01_Precision/significant_figures/README.md) | What the notation claims, and why the rule for `+` is a *different rule* from the rule for `×` |
| [Uncertainty propagation](01_Precision/uncertainty_propagation/README.md) | The rigorous version those rules approximate, and the two places they lie |
| [Catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md) | The one operation that destroys ten significant figures at once, silently |

Read them in that order; each one answers a question the previous one raises.

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
