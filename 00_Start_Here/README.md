# 00_Start_Here

**Level:** 101 · for anyone

## What this library is

One idea per page, and every claim backed by a program that runs. The pages are short, the programs are stdlib-only Python, and the output printed on any page came from an actual run that CI re-checks on every push.

It is not a textbook and does not try to be. A textbook covers a syllabus; this covers the handful of ideas that turned out to be worth writing down carefully, in the order that made them click.

## What to read first

[**01_Precision/**](../01_Precision/README.md) — *How much of this number is real?* Six lessons, in order, on measurement, significant figures, relative error, uncertainty, the finite set a machine keeps instead of the real line, and where digits go when a subtraction destroys them.

It begins with a question that sounds settled and is not: **are significant figures just rounding?** The answer is no, and unpacking why takes you from a blackboard example about a population estimate all the way to why the textbook quadratic formula returns an answer that is 25% wrong.

[**02_Measure_Zero/**](../02_Measure_Zero/README.md) — *How can infinitely many points take up no room?* Six lessons on sets so thin that they have no length, area or volume: the rationals, the Cantor set, the fat Cantor set (full of gaps, and still length 1/2), and the Cantor function, a staircase that climbs from 0 to 1 while standing still almost everywhere. It stands on its own; the one thing it assumes is the idea of a limit.

[**03_Complex_Numbers/**](../03_Complex_Numbers/README.md) — *What is a complex number, before anyone says √−1?* Five lessons: a complex number is a pair of reals and multiplication is a rule on pairs, so i² = −1 is what the rule does to the pair (0, 1); then the geometry, in which multiplying scales and turns the plane and i² = −1 is two quarter turns making a half turn; then why the rule is this one and not entry by entry: only this one can be undone, so every pair except (0, 0) can be divided by; then the payoff, in which a unit point multiplied by itself walks around the circle in equal steps, so zⁿ = 1 has exactly n solutions, the roots of unity, found exactly with √3 carried as a symbol; and then Euler's identity, in which e^{iπ} = −1 turns out to be that same half turn, because the exponential turns adding into multiplying and an imaginary input can only turn. It needs nothing but school algebra and the unit circle, and for the last lesson, eˣ on a calculator.

[**04_Sets/**](../04_Sets/README.md) — *What is this collection, exactly?* Groundwork the other chapters lean on, starting with the Cartesian product: what ℝ² is, why an ordered pair is not a two-element set, and why A × B and B × A can share no member at all. Then cardinality: what |A| means, why it is defined by matching rather than counting, and how the same idea sizes a type, a database column, and the set of all programs.

[**05_Statistics/**](../05_Statistics/README.md) — *What does one number say about many?* It starts with a question about words: why is "add them up and divide by how many" called the average, the mean, the arithmetic mean and the arithmetic average? Because they are not quite synonyms. *Average* covers the median and the mode too, and *arithmetic* tells the everyday mean apart from the geometric and harmonic means, which are the right answers for growth rates and speeds. It needs nothing but school arithmetic.

[**06_Algebraic_Structures/**](../06_Algebraic_Structures/README.md) — *Why does every book list the same laws?* Four lessons on the repetition every reader of mathematics notices. The rules for the integers and the axioms for vectors are the same four laws, and names like *group* and *field* only say which ones hold. Stated as a definition, the list becomes a test: a theorem proved from it holds in every set that passes, so 0v = 0 in a vector space becomes x⁰ = 1 among the positive numbers. A subspace needs only three of the eight checks, because the "for all" laws come free. And a map that keeps the operations, such as a linear map, a logarithm or a determinant, carries theorems across, so 2⁰ = 1, log 1 = 0, T(0) = 0 and det I = 1 are one proof. It needs school algebra, and a first look at vectors helps from lesson 2 on.

[**07_Linear_Systems/**](../07_Linear_Systems/README.md) — *What does it mean to solve a system of equations?* It starts where a linear algebra book starts, with the definition before the method: a linear combination is a recipe of fixed coefficients, a linear equation is a test that a list of numbers passes or fails, and a solution of a system passes every test at once. The first lesson reads Hefferon's Definition 1.1 symbol by symbol, on the two balances from the page before it. It needs nothing but school algebra.

[**08_Analytic_Geometry/**](../08_Analytic_Geometry/README.md) — *What does it mean to draw a number?* The first page of every precalculus book, read the way this library reads pages: a point is two signed distances, x from the y-axis and y from the x-axis, and a quadrant is nothing but the pair of signs, which is why the axes belong to none and why the word reaches into trigonometry, complex numbers and the symmetry of graphs. Then the rest of the book's first chapter, one lesson per objective: the distance formula (Pythagoras on the differences), the midpoint, the graph of an equation with its intercepts and symmetry, lines and slope, and circles. Each lesson ends with the book's questions, answers folded away, and a deck of Anki flashcards. It needs nothing but a number line, and from the distance formula on, the Pythagorean theorem of chapter 10.

[**09_Calculus/**](../09_Calculus/README.md) — *What is a velocity, and which motion is its own velocity?* Four lessons of calculus, told as motion the way Grant Sanderson's talk tells it: a velocity at an instant is what average velocities settle on; the motion whose velocity is its position is e^t, and the law of exponents comes out of it; in radians an angle is the distance walked round the circle; and "velocity = position" forces the power series of e^x, with cos and sin inside it. It needs school algebra and the patience to watch a number settle.

**Lost in the 3Blue1Brown talk on e^{iπ} = −1?** [Euler's formula: a lesson plan](../reading_guides/eulers_formula/README.md) lists the ten ideas it assumes, in the order to learn them, with a self-check to find where to start and a table that maps each screen of the talk to the lesson that explains it.

[**10_Geometry/**](../10_Geometry/README.md) — *How few numbers fix a shape?* The geometry a precalculus book assumes, from its review appendix: the Pythagorean theorem and its converse as a test that three lengths pass or fail, the area and volume formulas told apart by one check on their dimension, and which three measurements fix a triangle, which fix only its shape, and why side-side-angle is missing from every list. Read it just in time, when the distance formula asks for it; each lesson has the book's questions and a deck of flashcards. It needs nothing but arithmetic.

[**11_Logic/**](../11_Logic/README.md) — *What does "if A then B" actually claim?* The language every theorem here is written in: the one case in which "if A then B" is false, why the contrapositive says the same thing and the converse does not, what "if and only if" adds, and why a thousand examples prove nothing while one counterexample settles it. Read it whenever a book says "the converse is also true". It needs nothing but school arithmetic.

[**12_Learning_to_Learn/**](../12_Learning_to_Learn/README.md) — *How do you know that you know?* Four lessons about learning itself, after Saundra McGuire's *Teach Yourself How to Learn*: judging what you know, measured with confidence and a score that rewards honesty; McGuire's count-the-vowels exercise, where recall goes from 3 of 15 to 12 of 15 with nothing changed but the goal and a principle; studying versus learning, with Bloom's six levels climbed on one theorem; and spaced retrieval, the reason the pages here come with flashcards. Read it first if you want to get more out of everything else, or whenever a test goes worse than you expected. The books are listed on the [resources](../RESOURCES.md) page.

The sidebar lists the chapters A to Z. The numbers above are the suggested order, and the [topic map](../TOPICS.md) groups every lesson by subject, for when you know what you want but not where it is.

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

## Reading beyond this library

[**Linear algebra: a reading guide**](../reading_guides/linear_algebra/README.md) — why linear algebra is useful, what to know before starting it, and which book to learn it from, including an honest verdict on *Linear Algebra Done Right*. It is a reference page, not a lesson; its one worked example, the first problem in Hefferon's textbook, is backed by a program like everything else.

[**Precalculus: a reading guide**](../reading_guides/precalculus/README.md) — what the course before calculus is for, where it sits (it is not pre-algebra, which comes four years earlier), what to know before starting it, and which book to learn it from, with a verdict on Glencoe's classroom textbook. A reference page, not a lesson; its one worked example, the doubling time of money at compound interest, is backed by a program like everything else.

## Sibling libraries

- [rust-learning-library ↗](https://masiarek.github.io/rust-learning-library/) — same format, for Rust
- [star-voting-library ↗](https://masiarek.github.io/star-voting-library/) — voting methods, with a tabulation engine behind every example
- [biology-learning-library ↗](https://masiarek.github.io/biology-learning-library/) — high-school biology, bilingual EN/PL
