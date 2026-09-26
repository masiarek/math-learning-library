# 00_Start_Here

**Level:** 101 · for anyone

## What this library is

One idea per page, and every claim backed by a program that runs. The pages are short, the programs are stdlib-only Python, and the output printed on any page came from an actual run that CI re-checks on every push.

It is not a textbook and does not try to be. A textbook covers a syllabus; this covers the handful of ideas that turned out to be worth writing down carefully, in the order that made them click.

## What to read first

[**01_Precision/**](../01_Precision/README.md) — *How much of this number is real?* Six lessons, in order, on measurement, significant figures, relative error, uncertainty, the finite set a machine keeps instead of the real line, and where digits go when a subtraction destroys them.

It begins with a question that sounds settled and is not: **are significant figures just rounding?** The answer is no, and unpacking why takes you from a blackboard example about a population estimate all the way to why the textbook quadratic formula returns an answer that is 25% wrong.

[**02_Measure_Zero/**](../02_Measure_Zero/README.md) — *How can infinitely many points take up no room?* Six lessons on sets so thin that they have no length, area or volume: the rationals, the Cantor set, the fat Cantor set (full of gaps, and still length 1/2), and the Cantor function, a staircase that climbs from 0 to 1 while standing still almost everywhere. It stands on its own; the one thing it assumes is the idea of a limit.

[**03_Complex_Numbers/**](../03_Complex_Numbers/README.md) — *What is a complex number, before anyone says √−1?* Two lessons: a complex number is a pair of reals and multiplication is a rule on pairs, so i² = −1 is what the rule does to the pair (0, 1); then the geometry, in which multiplying scales and turns the plane and i² = −1 is two quarter turns making a half turn. It needs nothing but school algebra.
[**04_Sets/**](../04_Sets/README.md) — *What is this collection, exactly?* Groundwork the other chapters lean on, starting with the Cartesian product: what ℝ² is, why an ordered pair is not a two-element set, and why A × B and B × A can share no member at all. Then cardinality: what |A| means, why it is defined by matching rather than counting, and how the same idea sizes a type, a database column, and the set of all programs.

## How to run anything here

Every lesson folder has an `examples/` directory with a `.py` file and a `.out` answer key. Every command on these pages is written to be run from the root of a clone, so start there:

```bash
git clone https://github.com/masiarek/math-learning-library.git
```

```bash
cd math-learning-library
```

Then run any program directly:

```bash
python3 01_Precision/significant_figures/examples/significant_figures.py
```

Each program also runs from its own `examples/` folder, as `python3 significant_figures.py`: the examples read no files, so they do not care where they are started.

No virtual environment, no install step, no dependencies. If you have `python3`, you are ready.

To verify the whole library the way CI does:

```bash
python3 tools/run_examples.py --check
```

## Reading it as a website

<https://masiarek.github.io/math-learning-library/> — same content, with search. Built by MkDocs Material straight from this repo's Markdown; there is no separate `docs/` copy, so what GitHub renders and what the site serves are the same files.

To preview it locally:

```bash
uv run --group docs mkdocs serve
```

## Sibling libraries

- [rust-learning-library ↗](https://masiarek.github.io/rust-learning-library/) — same format, for Rust
- [star-voting-library ↗](https://masiarek.github.io/star-voting-library/) — voting methods, with a tabulation engine behind every example
- [biology-learning-library ↗](https://masiarek.github.io/biology-learning-library/) — high-school biology, bilingual EN/PL
