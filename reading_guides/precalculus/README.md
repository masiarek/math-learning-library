# Precalculus: a reading guide

**Level:** reference · for anyone deciding whether they need precalculus, what to know before it, and which book to learn it from

**One line:** Precalculus is a checklist rather than a subject, the functions calculus is about to take apart and the algebra it will assume, so its textbooks differ in writing and price more than in content; Glencoe's is a sound classroom book and a poor one to read alone.

Every other page in this library is a lesson: one idea, backed by a program. This page is a reading guide for a course the library does not teach, and what it says about books is opinion, not a test result. The one worked example on it, the doubling time of money at compound interest, is backed by a program like everything else.

## Where it sits

The name misleads in both directions. *Pre-algebra* is the course before algebra, taken at about twelve; *precalculus* is the course before calculus, taken at about seventeen. They share a prefix and nothing else, and a book with one name is no use for the other course. The usual sequence in American schools, which is the one the books below are written for:

| Order | Course | What it adds |
|---|---|---|
| 1 | Pre-algebra | negative numbers, fractions, ratios and percents, first equations |
| 2 | Algebra 1 | linear equations and their graphs, systems, exponents, quadratics |
| 3 | Geometry | proof, triangles, circles, right-triangle trigonometry |
| 4 | Algebra 2 | functions, polynomials, exponentials and logarithms, complex numbers |
| 5 | **Precalculus** | the same functions in depth, trigonometry as functions, and the rest of the list below |
| 6 | Calculus | limits, derivatives, integrals |

Precalculus is roughly the second half of Algebra 2 again, slower and deeper, with a full course of trigonometry added and a few chapters that belong to nothing else: conic sections, polar coordinates, vectors, sequences and series. Schools also call it *Algebra 3*, *Trigonometry and analytic geometry*, or *Advanced mathematical concepts*, which was the earlier title of Glencoe's book and is why online listings still tag it that way.

## What the course is for

Ask a calculus teacher what their students struggle with, and the answer is rarely calculus. It is algebra: exponent rules, fractions with variables in them, factoring, and trigonometric identities, all needed fast while a new idea is being explained. Precalculus exists so that none of that is new on the day the derivative arrives. That is why the course has no theorem of its own to head for, and why the table of contents is the same in every book:

| Precalculus topic | What calculus does with it |
|---|---|
| **Functions**: domain and range, composition, inverses, shifting and stretching a graph | Everything in calculus is done to a function. The chain rule is composition, and the derivative of an inverse function is a reciprocal slope. |
| **Polynomial and rational functions**: zeros, factoring, long division, asymptotes | Curve sketching, limits at infinity, and partial fractions, which is how a rational function gets integrated. |
| **Exponentials and logarithms** | eˣ is [the function that is its own derivative](../../09_Calculus/velocity_equals_position/README.md), and ln x is the integral of 1/x. Every growth and decay model is one of the two. |
| **Trigonometry**: the unit circle, [radians](../../09_Calculus/radians/README.md), the graphs, identities, inverse functions | The derivative of sin is cos only in radians. Identities are what make trigonometric integrals possible. |
| **Analytic geometry**: conics, parametric equations, polar coordinates | Motion along a curve, arc length, and area in polar coordinates. |
| **Sequences, series and Σ notation** | Riemann sums, and the [Taylor series](../../09_Calculus/power_series/README.md) that make sin, cos and eˣ computable. |
| **Complex numbers in polar form** | [Euler's formula](../eulers_formula/README.md), and the roots that a polynomial has and the real numbers cannot supply. |
| **Systems, matrices and vectors** | Multivariable calculus and [linear algebra](../linear_algebra/README.md), more than calculus itself. |
| **Limits**, informally, in the last chapter | The first chapter of the calculus book, seen once before. |

The list is long, and the point of it is fluency rather than coverage. A student who can do the algebra of the first four rows without thinking is ready for calculus; one who has met every row once and can do none of them quickly is not.

## What a precalculus problem looks like

Every book below has a chapter on exponential and logarithmic functions, and every one of them reaches for money. Put 100 in an account at 5% a year. *Simple* interest adds the same 5 every year, so the balance is 100 + 5t after t years: a linear function. *Compound* interest multiplies by the same factor 21/20 every year, so the balance is 100 · (21/20)ᵗ: an exponential function. The course asks two questions about any function, *what does it do as the input grows?* and *which input gives this output?*, and for the exponential the second question has no answer among the operations of arithmetic.

The program keeps every balance as an exact fraction, so every comparison is exact, and it says so at the one point where it has to use a float.

<!-- output:doubling_time -->
*Verified output of [`doubling_time.py`](examples/doubling_time.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. TWO WAYS TO GROW: A LINE AND A CURVE
   Start with 100.00 at 5% a year.
   simple interest:    balance after t years = 100 + 5·t        (add 5.00 every year)
   compound interest:  balance after t years = 100 · (21/20)^t   (multiply by 21/20 every year)

       t    simple   compound   compound gained that year
       0    100.00     100.00                        0.00
       1    105.00     105.00                        5.00
       2    110.00     110.25                        5.25
       3    115.00     115.76                        5.51
       5    125.00     127.63                        6.08
      10    150.00     162.89                        7.76
      14    170.00     197.99                        9.43
      15    175.00     207.89                        9.90
      20    200.00     265.33                       12.63
      30    250.00     432.19                       20.58
      50    350.00    1146.74                       54.61
   Simple interest gains the same 5.00 every year, so its graph is a
   straight line. Compound interest gains 5% of a balance that has
   already grown, so the gains grow too, and the graph bends upward.

2. WHICH YEAR DOES THE MONEY DOUBLE?
   simple:    100 + 5·t = 200
              subtract 100:   5·t = 100
              divide by 5:    t = 20
              Each step undoes one operation of arithmetic.

   compound:  100 · (21/20)^t = 200
              divide by 100:  (21/20)^t = 2
              ...and now t is an exponent. No operation of arithmetic
              undoes 'raise 21/20 to a power', so try values of t:
                  t   (21/20)^t  doubled?
                 12      1.7959     False
                 13      1.8856     False
                 14      1.9799     False
                 15      2.0789      True
                 16      2.1829      True
   The balance first doubles in year 15: (21/20)^14 < 2 ≤ (21/20)^15.
   The exact moment, the t with (21/20)^t = 2, is between 14 and 15,
   and it is not a fraction at all: (21/20)^(p/q) = 2 would mean
   21^p = 2^q · 20^p, an odd number equal to an even one.

3. THE LOGARITHM IS THE NAME OF THE ANSWER
   The number t with (21/20)^t = 2 is written log base 21/20 of 2.
   It has no exact decimal, so this section, alone in the program, uses floats:
     t = ln 2 / ln 1.05  =  0.693147 / 0.048790  =  14.206699
     check:  1.05^14.206699 = 2.0000000000
     that is 14 years and about 75 days, in the year-15 row of the table
   Dividing one natural logarithm by another is the change-of-base formula,
   and it is why a calculator needs only one log key.

   The rule of 72 says the doubling time is about 72 / rate = 72 / 5 = 14.4 years,
   because ln 2 = 0.693 and ln(1 + r) is close to r when r is small,
   so t is close to 0.693 / r, and 72 divides more evenly than 69.3.

4. THE EXPONENTIAL WINS EVENTUALLY, WHATEVER THE RATES
   1% compound against 5% simple. The line is ahead for a long time:
       t   simple 5%   compound 1%
       0      100.00        100.00
      10      150.00        110.46
      50      350.00        164.46
     100      600.00        270.48
     200     1100.00        731.60
     300     1600.00       1978.85
   The curve passes the line in year 269:  compound 1453.62 > simple 1445.00,
   and in year 268 it had not:          compound 1439.22 < simple 1440.00.
   No logarithm finds that year. A logarithm undoes an exponential when
   the other side is a number, as in section 2, not when it is another
   function of t. Trying values is the only method here, and it works
   because an exponential with base above 1 outgrows every line, and
   every polynomial, in the end. The books call this end behaviour.
   Even 2^t against t^10: t^10 takes the lead at t = 2, keeps it through t = 58,
   and 2^t passes it at t = 59.
```
<!-- /output -->

Section 2 is the idea of an inverse function, which is the real content of the chapter. Subtraction is defined as the answer to "what do I add?", the square root as the answer to "what do I square?", and the logarithm as the answer to "what exponent?". None of the three is a new kind of arithmetic; each is a question, given a name so that it can be written down and worked with. The change-of-base step in section 3 rests on the fact that logarithms turn multiplication into addition, which [maps that keep the laws](../../06_Algebraic_Structures/maps_that_keep_the_laws/README.md) states as: a logarithm is a linear map.

Section 4 is what the books call *end behaviour*, and it is the other question the course asks of every function. It also shows the limit of the chapter's method. A logarithm solves bᵗ = c and nothing else; against a line, trying values is the only tool a precalculus student has, and it is an honest one. Calculus supplies a better one later, Newton's method, and the reason it works is the derivative.

The floats in section 3 are the only ones in the program. A course that leans on a graphing calculator uses them everywhere, and [01_Precision](../../01_Precision/README.md) is about what that costs.

## What you need first

Algebra 1, Algebra 2 and geometry, but not all of them. What precalculus will not re-teach slowly:

| You need | Why precalculus uses it |
|---|---|
| **The rules of exponents**, including negative and fractional exponents, and fractions with letters in them | An exponential function is the exponent rules with the exponent as the variable, and a logarithm is those rules read backwards. The doubling example above is nothing else. |
| **Solving linear and quadratic equations**: factoring, completing the square, the quadratic formula | Finding the zeros of a function and where two graphs meet. [Completing the square](../../08_Analytic_Geometry/circles/README.md) is how a conic is recognised from its equation. |
| **[Lines](../../08_Analytic_Geometry/lines_and_slope/README.md)**: slope, intercepts, the equation of the line through two points | Slope is what the derivative will generalise, and every other graph is compared with lines. |
| **Function notation** f(x), and reading a graph | The whole course is about functions, and the notation is assumed from the first page. |
| **Geometry**: [Pythagoras](../../10_Geometry/pythagorean_theorem/README.md), [similar triangles](../../10_Geometry/congruent_and_similar_triangles/README.md), the [circumference and area of a circle](../../10_Geometry/area_and_volume_formulas/README.md) | Trigonometry is similar triangles with names attached. The unit circle needs Pythagoras, and [radians](../../09_Calculus/radians/README.md) need circumference. |
| **Right-triangle trigonometry**: sine, cosine and tangent as ratios of sides | Usually taught in geometry. Precalculus extends it to every angle and turns the ratios into functions with graphs. |

### What you don't need

- **Calculus.** The last chapter of Glencoe, and of Stewart, introduces limits. It is a preview, not a prerequisite for anything before it.
- **Proofs.** The standard course states results and practises them. Art of Problem Solving and Lang, below, are the exceptions, and say so.
- **A graphing calculator**, despite the calculator labs in every classroom book. [Desmos ↗](https://www.desmos.com/calculator) is free and runs in a browser, and Python's `math` module does the rest.

### A quick self-check

If you can do all three of these, start any book below:

1. Solve x² − 5x + 6 = 0, and say where the graph of y = x² − 5x + 6 crosses the x-axis.
2. Simplify (2x³)² / x⁴, and write √x · x² as a single power of x.
3. A right triangle has legs 3 and 4. Find its hypotenuse, and the sine of its smallest angle.

The answers are 2 and 3, at the points (2, 0) and (3, 0); 4x² and x^(5/2); and 5 and 3/5. If number 2 is the shaky one, do the exponents chapter of an Algebra 2 book first: it is the prerequisite that causes the most trouble in the exponential chapter, and again in calculus.

## Which book

### *Glencoe Precalculus* (McGraw Hill, 2011)

A standard American high-school classroom textbook, from the same series as Glencoe's Algebra 1, Geometry and Algebra 2, and the successor to the older *Advanced Mathematical Concepts*.

**What it is.** A complete course. Its chapters run from a review of prerequisites through functions, polynomial and rational functions, exponentials and logarithms, two chapters of trigonometry, systems and matrices, conics and parametric equations, vectors, polar coordinates with complex numbers, sequences and series, a chapter of statistics, and a closing chapter on limits and derivatives. Every topic in the table above is in it.

**Strengths**

- **Nothing is missing.** Whatever a precalculus syllabus lists, it is here, and the review chapter at the front covers the prerequisites above.
- **A large exercise bank**, graded from routine to harder, with worked examples of each type just before them, and answers to the odd-numbered exercises at the back.
- **Cheap used.** School districts retire these by the thousand, so a used copy costs little, and nothing in the subject has changed since it was printed.

**Weaknesses**

- **Written for a classroom, not a reader.** It assumes a teacher, a pacing guide and a term. Its explanations are procedures with worked examples, and it rarely says why a method works. Read alone, it is a reference with exercises.
- **Heavy and wide.** Every chapter is padded with "real-world" applications and calculator labs, tied to a TI-84, that are there for the curriculum rather than the mathematics.
- **Half the answers are elsewhere.** Solutions to the even-numbered exercises are in a teacher's edition sold separately, so a self-learner cannot check half the practice.

**Verdict.** If it is the book your school uses, or you can get it for a few dollars, it is a fine source of practice, and its coverage is not in question. It is not the best book for precalculus, because there is no such book: the content is fixed and uncontroversial, and the books differ in how they are written and what they cost. For someone reading alone, a book written to be read, below, is a better main text, with Glencoe's exercises on the side.

### Michael Sullivan, *Precalculus*, 11th edition (Pearson, 2020; Global Edition 2023)

The college counterpart of Glencoe: one of the four classroom books that between them cover most American precalculus courses, with Stewart, Larson and Blitzer, and the one whose apparatus for self-checking is the most complete. The Global Edition is the same book with some exercises reset outside the United States and a lower price.

**What it is.** A complete course in fourteen chapters, from graphs and functions through polynomial, rational, exponential and logarithmic functions, three chapters of trigonometry, polar coordinates and vectors, conics, systems and matrices, sequences and induction, counting and probability, and a preview of calculus, with an eleven-section review appendix at the back. About eleven hundred pages. Every topic in the table above is in it, and the [rectangular coordinates](../../08_Analytic_Geometry/rectangular_coordinates/README.md) lesson in this library follows its first section.

**Strengths**

- **Every example has a matching exercise.** Each worked example ends with "Now Work Problem n", pointing at the exercise that practises exactly that skill, so a reader can check understanding one example at a time instead of at the end of the section.
- **It tells you what to review, and when.** Each section opens with *Preparing for this section*, naming the appendix sections it needs with page numbers, and each exercise set opens with *Are You Prepared?*, a few problems that test them. That is the just-in-time route through the appendix described below, built into the book.
- **Exercise sets in layers.** Concepts and Vocabulary, fill-in-the-blank and true or false, which make ready flashcards; Skill Building; Applications and Extensions; Explaining Concepts; and, new in this edition, *Retain Your Knowledge*, problems from earlier sections placed later so that they come back after an interval. A book that does its own spaced repetition. Answers to the odd-numbered exercises are at the back.
- **Reliable.** Eleven editions have removed the errors, and the boxed procedures are exact enough to follow blind.

**Weaknesses**

- **Written for a classroom, not a reader.** The explanations are procedures with worked examples; the book says how far more often than why, and it has no voice. It is a reference with a very good exercise bank, not a text to read through.
- **Heavy.** Eleven hundred pages, with graphing-calculator screens, "real-world" applications and MyLab pointers that serve the course rather than the mathematics, and nothing marks which of it matters most.
- **Expensive new.** Well over a hundred dollars in the American edition; the Global Edition and any recent used copy cost a fraction, and the content has not changed in a way that matters for years.

**Verdict.** If you have it, keep it, and use it the way it is built to be used: for the exercises and the self-checks, working each section's *Now Work* pairs and *Are You Prepared?* problems rather than reading it front to back. It is the best of the classroom books for someone checking their own work, because its apparatus was designed for exactly that. For understanding why a method works, read the same section in Axler or Stitz and Zeager first, then do Sullivan's problems; the two together are a better course than either alone.

### James Stewart, Lothar Redlin and Saleem Watson, *Precalculus: Mathematics for Calculus*, 7th edition (Cengage, 2016)

The other usual college choice, and the precalculus book of the author of the most-used calculus text, written to feed it. Reviewed from memory of the book and from the two pages the owner sent (section 1.9), not from a copy at hand.

**What it is.** A complete course in about a thousand pages, twelve chapters plus a *Focus on Modeling* essay after most chapters, in the same order as Sullivan with two differences: the algebra review is chapter 1, not an appendix, and the book is openly aimed at calculus, with a closing chapter on limits and *Discovery Projects* that look ahead.

**Strengths**

- **It explains before it drills.** The derivations are on the page, not in the exercises: the midpoint formula from congruent triangles, the distance formula from the number-line distance, and the text says why a step is allowed. Of the four classroom books, it reads the most like a book.
- **Proof appears early.** Examples prove things (Example 3 of section 1.9 proves a parallelogram by its diagonals), and the modeling essays ask the reader to set up a problem, not only to solve one.
- **Built for calculus.** Chapter and section choices track what a calculus course will assume; the trigonometry is introduced with the unit circle first, which is the form calculus uses.
- **Cheap used.** Editions from the fourth on are interchangeable for self-study and cost a few dollars.

**Weaknesses**

- **Thinner self-checking.** Each section ends with *Concepts* and *Skills* exercises and odd answers at the back, but there is no *Now Work* pair after every example, no *Are You Prepared?* opener, and no built-in spaced review. The reader has to make the checks.
- **It sometimes takes the long way.** Example 2 of section 1.9 compares √41 with √45 instead of 41 with 45; the book is exact but not always economical.
- **Review up front.** Chapter 1 is a hundred pages of algebra review placed first, where a reader is tempted to start; the just-in-time route below is not marked for you the way Sullivan marks it.

**Verdict.** For reading, Stewart; for practising, Sullivan. If one book only: Stewart for someone teaching themselves toward calculus, Sullivan for someone in a course who needs to check every step of their own work. The content is the same, so neither choice costs anything but the price of the book.

### Sullivan and Stewart side by side

| | Sullivan | Stewart, Redlin and Watson |
|---|---|---|
| **Written for** | the course and the exercise set | the reader on the way to calculus |
| **Explanations** | procedures and worked examples; "how" more than "why" | derivations on the page; the "why" is usually there |
| **Self-checking** | the best of any classroom book: *Now Work*, *Are You Prepared?*, *Retain Your Knowledge* | ordinary: exercise sets with odd answers |
| **Proof** | computed examples; proofs mostly in the exercises | some examples prove; modeling essays |
| **Algebra review** | Appendix A, pointed to just in time by every section | Chapter 1, up front |
| **Length** | about 1 100 pages | about 1 000 pages |
| **Price** | high new; the Global Edition is cheap | high new; used copies of any edition are cheap |
| **Best use** | the problem bank beside another book | the main text, with Sullivan's or Khan Academy's problems beside it |

How sure: Sullivan's apparatus and Stewart's section 1.9 are from pages the owner sent; the rest of the Stewart review is from memory of the book and could be off in detail (edition counts, chapter numbers).

**Sullivan against Stewart, on one section.** The owner sent the two pages of Stewart, Redlin and Watson's section 1.9 (*The Coordinate Plane; Graphs of Equations; Circles*, pages 93–94) that cover the distance and midpoint formulas, the same ground as Sullivan's section 1.1, so the two books can be compared where this library has lessons to check them against. On the explanation, Stewart does the better job. It derives the distance formula from the number-line distance |b − a| of its first section, writes the legs as |x₂ − x₁| and |y₂ − y₁| and then shows the absolute values drop under the square, which is the point the [distance formula](../../08_Analytic_Geometry/distance_formula/README.md) lesson makes too; Sullivan writes the squares straight away. It derives the midpoint formula on the page from two congruent triangles (its Figure 6), the argument the [midpoint formula](../../08_Analytic_Geometry/midpoint_formula/README.md) lesson gives; Sullivan states the formula and leaves the reasoning thinner. And its Example 3 uses the midpoint to prove something, that a quadrilateral whose diagonals share a midpoint is a parallelogram, where Sullivan's examples compute. One mark against Stewart: its Example 2 decides which of two points is nearer by taking both square roots, √41 against √45, where comparing d² needs no roots at all, as the distance lesson explains. On the practice, Sullivan does the better job, for the reasons in the review above: *Now Work* after every example, *Are You Prepared?* before every exercise set, and *Retain Your Knowledge* later. Reading order for this topic: Stewart's pages 93–94 for the two derivations, the two lessons here for what the books skip, then Sullivan's exercise set 1.1. How sure: the comparison of the derivations is read from the pages themselves; the description of Sullivan's section is from the owner's earlier screenshots and the lessons that follow them; the claim that the two books agree on the content of the rest of the course is from memory of both.

### Alternatives, by goal

| If you want… | Read |
|---|---|
| **A book written to be read alone** | Sheldon Axler, *Precalculus: A Prelude to Calculus* (Wiley). Short sections, explanations of why, and it stops at what calculus needs. Fewer drill exercises than a classroom book. |
| **A free, complete textbook** | Carl Stitz and Jeff Zeager, [*Precalculus* ↗](https://www.stitz-zeager.com/) (free PDF), written by two community-college teachers with more voice than most; or [OpenStax, *Precalculus 2e* ↗](https://openstax.org/details/books/precalculus-2e) (free online and PDF), plainer and closer to the classroom books. |
| **The other classroom books** | James Stewart, Lothar Redlin and Saleem Watson, *Precalculus: Mathematics for Calculus* (Cengage), the usual college choice and the one whose sequel is the most-used calculus book. Larson and Blitzer are interchangeable with it and with Glencoe; Sullivan, reviewed above, has the best self-checking apparatus of the four. Any edition from the last twenty years is fine, and the older ones cost nothing. |
| **Video and checked practice** | [Khan Academy, *Precalculus* ↗](https://www.khanacademy.org/math/precalculus) (free), with exercises that grade themselves; and 3Blue1Brown's *Lockdown Math* series (free), starting with [complex numbers ↗](https://www.3blue1brown.com/lessons/ldm-complex-numbers/), for logarithms, trigonometry and Euler's formula with pictures. |
| **A fast review before calculus** | George Simmons, *Precalculus Mathematics in a Nutshell*, about 120 pages of geometry, algebra and trigonometry for someone who once knew them; or the algebra and trigonometry review in [Paul's Online Math Notes ↗](https://tutorial.math.lamar.edu/) (free). |
| **One rigorous book from arithmetic up** | Serge Lang, *Basic Mathematics* (Springer). Terse and proof-flavoured, and it covers everything from pre-algebra to precalculus in one volume. |
| **More than the course** | [Art of Problem Solving, *Precalculus* ↗](https://artofproblemsolving.com/store/book/precalculus) (Richard Rusczyk): trigonometry, complex numbers, vectors and matrices, with problems from routine to olympiad. For a strong student who finds the standard course slow. |

### Suggested paths

- **In a school course** with Glencoe or a book like it: use it for the exercises, and keep Axler or Stitz and Zeager beside it for the explanations when a worked example is not enough.
- **Teaching yourself, calculus next:** Axler or Stitz and Zeager cover to cover, Khan Academy for practice, and skip nothing in the trigonometry chapters. That is where calculus students most often find a gap.
- **Returning after years away:** Simmons or Paul's Online Notes, then straight into a calculus book with a review chapter, and back to a precalculus book only for what gives trouble.
- **Strong and impatient:** Art of Problem Solving, with Lang alongside.

## The review appendix: read it just in time

Every classroom precalculus book opens with a review of algebra, and the temptation is to read it first. Do not. In Sullivan's *Precalculus* the review is Appendix A, eleven sections and about ninety pages, and the book itself says which parts each section needs: every section opens with a *Preparing for this section* box naming the appendix sections to review, with page numbers, and every exercise set opens with *Are You Prepared?*, a few problems that test exactly those, each with a page reference. So the working order is: open the section you are on, do its *Are You Prepared?* problems cold, and read only the appendix section each miss points to. Before section 1.1 that means A.1 and A.2, and A.2 mostly for the Pythagorean theorem. Stewart, Larson and Blitzer have the same device under other names.

What the appendix sections are for, when they are first needed, and what this library already has on each:

| Section | Reviews | First needed by | In this library |
|---|---|---|---|
| A.1 Algebra Essentials | sets, the real number line, absolute value as distance, exponent laws, scientific notation | 1.1 | [the Cartesian product](../../04_Sets/cartesian_product/README.md) for sets; [01_Precision](../../01_Precision/README.md) for scientific notation; the number line in [rectangular coordinates](../../08_Analytic_Geometry/rectangular_coordinates/README.md) |
| A.2 Geometry Essentials | Pythagoras, area and volume, similar triangles | 1.1, the distance formula | all of [10_Geometry](../../10_Geometry/README.md): [the Pythagorean theorem](../../10_Geometry/pythagorean_theorem/README.md), [area and volume formulas](../../10_Geometry/area_and_volume_formulas/README.md), [congruent and similar triangles](../../10_Geometry/congruent_and_similar_triangles/README.md); then [the distance formula](../../08_Analytic_Geometry/distance_formula/README.md) |
| A.3 to A.7 | polynomials, factoring, synthetic division, rational expressions, roots and rational exponents | chapters 2 to 4, as they arise | [a definition is a test](../../06_Algebraic_Structures/a_definition_is_a_test/README.md) proves the exponent laws A.7 states |
| A.8 Solving Equations | linear, quadratic and radical equations | 1.2, intercepts | [catastrophic cancellation](../../01_Precision/catastrophic_cancellation/README.md), on what the quadratic formula does to a calculator |
| A.9 Problem Solving | interest, mixture and motion problems | optional | the doubling-time example above |
| A.10 Interval Notation; Inequalities | intervals, solving inequalities | 2.1, domains | the interval reading of (x, y) in [rectangular coordinates](../../08_Analytic_Geometry/rectangular_coordinates/README.md) |
| A.11 Complex Numbers | i, arithmetic, complex roots of quadratics | chapter 4, zeros of polynomials | all of [03_Complex_Numbers](../../03_Complex_Numbers/README.md), built without √−1 |

The section numbers are the 10th and 11th editions'; an older edition shifts them by one or two, and the *Preparing for this section* boxes are the reliable map in any of them.

## What this library already covers

Pieces of the course, from an angle the books do not take:

- [03_Complex_Numbers](../../03_Complex_Numbers/README.md) — the complex-numbers chapter of any precalculus book, built without √−1. [Multiplication rotates](../../03_Complex_Numbers/multiplication_rotates/README.md) is the polar form and de Moivre's formula as geometry, and [roots of unity](../../03_Complex_Numbers/roots_of_unity/README.md) is the unit circle's twelve marks with √3 carried exactly. A precalculus course does the same work with angles, and [Euler's identity](../../03_Complex_Numbers/eulers_identity/README.md) is where the chapter finally computes one: e^{iθ} as the limit of compounding, the polar form r e^{iθ}, and why the answer a program gives for e^{iπ} is not quite −1.
- [Maps that keep the laws](../../06_Algebraic_Structures/maps_that_keep_the_laws/README.md) — the logarithm as the map that turns multiplication into addition, which is the fact under the change-of-base formula in section 3 above, and the slide rule built on it. [A definition is a test](../../06_Algebraic_Structures/a_definition_is_a_test/README.md) proves x⁰ = 1 and x⁻¹ = 1/x from the exponent laws, where a school book declares them.
- [Linear equations and their solutions](../../07_Linear_Systems/linear_equations/README.md) — systems of equations, a chapter in every precalculus book, taken apart symbol by symbol. [Linear algebra: a reading guide](../linear_algebra/README.md) is this page's twin for the course after.
- [The Cartesian product](../../04_Sets/cartesian_product/README.md) — ℝ² as ordered pairs: the coordinate plane that every graph in the course is drawn in.
- [Rectangular coordinates](../../08_Analytic_Geometry/rectangular_coordinates/README.md) — the first page of the course's chapter on graphs, read line by line: which axis each coordinate measures from, why a quadrant is only a pair of signs, and where the word goes on to do its work in trigonometry. With the book's questions and a deck of flashcards.
- The rest of that chapter, one lesson per section: [the distance formula](../../08_Analytic_Geometry/distance_formula/README.md), [the midpoint formula](../../08_Analytic_Geometry/midpoint_formula/README.md), [graphs, intercepts and symmetry](../../08_Analytic_Geometry/graphs_intercepts_symmetry/README.md), [lines and slope](../../08_Analytic_Geometry/lines_and_slope/README.md) and [circles](../../08_Analytic_Geometry/circles/README.md); and the geometry it assumes, Appendix A.2, in [10_Geometry](../../10_Geometry/README.md).
- [Catastrophic cancellation](../../01_Precision/catastrophic_cancellation/README.md) — the quadratic formula as every precalculus book prints it, the inputs on which a calculator gets it badly wrong, and the free fix; with [machine numbers](../../01_Precision/machine_numbers/README.md) for what the calculator is doing to the numbers in the first place.
- [09_Calculus](../../09_Calculus/README.md) — the course this one prepares for, in the four lessons Euler's formula needs. [Radians](../../09_Calculus/radians/README.md) is the trigonometry chapter's definition of the radian, and the reason calculus insists on it; [velocity equals position](../../09_Calculus/velocity_equals_position/README.md) is the exponential chapter's compound interest turned into a motion.
- [Euler's formula: a lesson plan](../eulers_formula/README.md) — a path from the exponent laws to e^{iπ} = −1 in ten steps, six of them precalculus.

What the library does not cover are the two halves of the course itself: functions as objects, with domain, composition and inverses, and trigonometry beyond [radians](../../09_Calculus/radians/README.md). The [roadmap](../../ROADMAP.md) lists both.

## Po polsku, w skrócie

„Precalculus" to nie osobny przedmiot, tylko lista kontrolna przed analizą: funkcje, które analiza zaraz rozłoży na części, i algebra, którą będzie zakładać. Dlatego podręczniki różnią się bardziej stylem i ceną niż treścią. Przykład z pieniędzmi pokazuje, o co w kursie chodzi: odsetki proste dodają co roku tyle samo i dają funkcję liniową, a składane mnożą co roku przez ten sam czynnik i dają funkcję wykładniczą; pytanie „po ilu latach kwota się podwoi?" nie ma odpowiedzi w samej arytmetyce, i tę odpowiedź nazywa się logarytmem. Najczęstsza luka przed kursem to prawa potęg, a przed analizą trygonometria. Dodatku z powtórką algebry nie czyta się na początku, tylko wtedy, gdy konkretna sekcja go wymaga. Rozdział 09_Calculus i plan lekcji o wzorze Eulera pokazują, dokąd ten kurs prowadzi.
