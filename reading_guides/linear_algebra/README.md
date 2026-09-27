# Linear algebra: a reading guide

**Level:** reference · for anyone deciding whether to learn linear algebra, what to know first, and which book to learn it from

**One line:** Linear algebra is the part of mathematics that can be solved completely, which is why so much else gets turned into it; it needs little more than school algebra, and *Linear Algebra Done Right* is an excellent second book and a hard first one.

Every other page in this library is a lesson: one idea, backed by a program. This page is a reading guide for a subject the library does not teach yet, and what it says about books is opinion, not a test result. The one worked example on it, the first problem in Hefferon's textbook, is backed by a program like everything else.

## Why linear algebra is useful

Because linear problems are the kind mathematics can solve completely, and a surprising amount of the world can be turned into one.

1. **Linear problems can be solved.** For a system of linear equations we know exactly when a solution exists, how many there are, and fast, reliable algorithms to find them, even with millions of unknowns. Nonlinear problems rarely have any of that.
2. **Anything smooth looks linear up close.** That is what a derivative is: the best linear approximation at a point. So the standard way to attack a hard nonlinear problem is to approximate it by a linear one, solve that, and repeat. Newton's method, a GPS position fix and training a neural network all work this way.
3. **Data already is a matrix.** A spreadsheet, a photo (a grid of pixels), a list of users and the films they rated. Linear algebra is the language for doing one thing to all those numbers at once.
4. **Computers are built for it.** GPUs, and the chips that run AI, are essentially machines for multiplying matrices quickly. When a problem can be phrased as linear algebra, the hardware is already optimised for it.

### Where you meet it

| Field | What linear algebra does there |
|---|---|
| **3D graphics and games** | Every rotation, scaling and camera projection is a 4×4 matrix. Each frame is millions of matrix–vector multiplications. |
| **AI and machine learning** | A neural network layer is a matrix multiplication followed by a simple nonlinear function. Large language models are mostly huge matrix multiplications. Words and images become vectors, and "similar" means a large dot product. |
| **Search** | Google's original PageRank is an eigenvector of the matrix of links between pages. |
| **Statistics and data science** | Least-squares regression is a projection onto a subspace. PCA finds the most important directions in data using eigenvectors (the SVD). |
| **Recommendations** | Recommending films or products by approximating a huge ratings table with a low-rank matrix. This was the core idea behind the winning Netflix Prize approaches. |
| **Compression** | JPEG changes the basis of each 8×8 block of pixels and throws away the small coefficients. |
| **Engineering** | Electrical circuits, bridge and aircraft simulations (finite element methods) and heating or airflow models all end up as very large systems of linear equations. |
| **Vibrations and stability** | A structure's natural frequencies are eigenvalues. Whether a system settles down or blows up depends on the signs of its eigenvalues. |
| **Probability** | A Markov chain's long-run behaviour is an eigenvector with eigenvalue 1. |
| **Physics** | In quantum mechanics, states are vectors and measurable quantities are operators. The spectral theorem, the high point of Axler's book, is the mathematics underneath it. |
| **Error correction** | QR codes, and error-correcting codes for storage and data transmission, are linear algebra over finite number systems instead of the real numbers. |

### Two ideas do most of the work

- **Solving Ax = b**, or when there is no exact solution, finding the closest one (least squares). This covers circuits, simulations, curve fitting and regression.
- **Eigenvectors and the SVD.** An eigenvector is a direction a matrix only stretches, never turns. This one idea gives PageRank, PCA, vibration frequencies, Markov chains, compression and quantum mechanics.

Once you see a matrix as a *function* that moves space around, and not just a grid of numbers, most of these applications become the same few ideas over and over.

## What a first problem looks like

[Jim Hefferon's *Linear Algebra* ↗](https://hefferon.net/linearalgebra/) opens with a problem from high-school statics. A meter stick rests on a pivot with three objects on it: one of 2 kg, and two whose masses, h and c, are unknown. The stick balances when the moments on the two sides are equal, where an object's moment is its mass times its distance from the pivot. Two experiments put the objects in different places:

| | Left of the pivot | Right of the pivot | Equation |
|---|---|---|---|
| Balance 1 | h at 40 cm, c at 15 cm | 2 kg at 50 cm | 40h + 15c = 100 |
| Balance 2 | c at 25 cm | 2 kg at 25 cm, h at 50 cm | 25c = 50 + 50h |

The program builds both equations from where the objects sit, shows why one balance is not enough, solves the pair by Gauss's method, and puts the answer back on both sticks. Every number is an exact fraction, so "balanced" means equal.

<!-- output:balance_masses -->
*Verified output of [`balance_masses.py`](examples/balance_masses.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. EACH BALANCE IS ONE LINEAR EQUATION
   balance 1
     left of the pivot:    h at 40 cm, c at 15 cm
     right of the pivot:   2 kg at 50 cm
     left moments = right moments:   40h + 15c = 50 · 2
     unknowns on the left:           40h + 15c = 100
   balance 2
     left of the pivot:    c at 25 cm
     right of the pivot:   2 kg at 25 cm, h at 50 cm
     left moments = right moments:   25c = 25 · 2 + 50h
     unknowns on the left:           -50h + 25c = 50
   Every unknown appears only multiplied by a number and added up.
   No h², no h·c, no √h: that is what makes the equations linear.

2. ONE BALANCE IS NOT ENOUGH
   Balance 1 alone says 40h + 15c = 100. Try some masses for h:
         h  c from balance 1  balance 2 holds?
         0              20/3             False
       1/4                 6             False
         1                 4              True
       5/2                 0             False
   Every row balances stick 1, and there are infinitely many more:
   the solutions of one equation in two unknowns fill a whole line.
   A second, different balance is a second line, and two lines that
   are not parallel cross at exactly one point.

3. GAUSS'S METHOD: REMOVE h FROM ONE ROW, THEN SOLVE
   row 1:   40h + 15c = 100
   row 2:  -50h + 25c = 50
   Add 5/4 times row 1 to row 2, because -50 + 5/4 · 40 = 0:
     the c term:      25 + 5/4 · 15 = 175/4
     the right side:  50 + 5/4 · 100 = 175
   row 2 is now:   (175/4)c = 175
   so c = 175 / (175/4) = 4
   Put c = 4 into row 1:   40h + 15 · 4 = 100,  so 40h = 40  and  h = 1
   With a thousand unknowns the steps are the same, only more of them.

4. PUT THE ANSWER BACK ON BOTH STICKS
   h = 1 kg,  c = 4 kg
   balance 1:  left 40 · 1 + 15 · 4 = 100   right 50 · 2 = 100   balanced: True
   balance 2:  left 25 · 4 = 100   right 25 · 2 + 50 · 1 = 100   balanced: True
```
<!-- /output -->

Section 2 is the whole subject in miniature. One equation in two unknowns does not pin anything down: its solutions fill a line. Each new equation that says something new cuts the possibilities down, and two independent equations in two unknowns leave exactly one answer. Asking *how many* equations are really independent, and what the solutions look like when they are not enough, is what the words *rank*, *dimension* and *null space* are for.

Section 3 is Gauss's method, the algorithm every first course starts with. Nothing in it needs more than school algebra, which is the point of the next section.

## What you need first

Less than most subjects. **High-school algebra is the only hard requirement.** What else you need depends on which kind of course you take: a computational one (Strang) or a proof-based one (Axler).

### The essentials, for either route

| You need | Why linear algebra uses it |
|---|---|
| **Solving linear equations**, including a system of two equations in two unknowns by substitution or elimination | This is where linear algebra starts, as in the balance problem above. Gaussian elimination is the same method scaled up. |
| **Working with algebraic expressions**, subscripts like aᵢⱼ, and **Σ notation** | Every formula for matrix multiplication and dot products is written this way. |
| **Coordinates in the plane**, Pythagoras, and basic sin and cos | Vectors as arrows, length, angles, the dot product, rotations and projections. |
| **Functions**: what composition and an inverse function are | A matrix *is* a function, and multiplying matrices is composing those functions. |

### Extra for a proof-based book (Axler, Friedberg, Treil)

| You need | Why |
|---|---|
| **Reading and writing proofs**: quantifiers, contrapositive, contradiction, induction | This is the real barrier. Most people who get stuck in Axler are stuck on proofs, not on linear algebra. |
| **Sets and functions**: one-to-one, onto, bijection | "Injective" and "surjective" appear on almost every page. |
| **Complex numbers** | Axler works over ℂ from chapter 1. A rotation of the plane has no real eigenvalues, so you need ℂ for eigenvalues to always exist. |
| **Polynomials**: factoring, roots, division with remainder | Axler builds eigenvalue theory on polynomials. The book proves the theory itself, but you need to be fluent with the algebra. |

For proofs, the usual bridge books are Richard Hammack's [*Book of Proof* ↗](https://richardhammack.github.io/BookOfProof/) (free online) and Daniel Velleman's *How to Prove It*. A few weeks with either one makes Axler far easier.

### What you don't need

- **Calculus.** Many universities list it as a prerequisite, but mostly as a sign of maturity. Linear algebra barely uses it. Axler's examples only need you to know how to differentiate and integrate a polynomial, for example "differentiation is a linear map".
- **Statistics, measure theory or numerical precision.** These matter later, for applications and numerical linear algebra, not for the basics.

### A quick self-check

If you can do all three of these, you are ready for Strang now:

1. Solve 2x + 3y = 7 and x − y = 1.
2. Prove that the sum of two odd numbers is even.
3. Explain why f(x) = x² is not one-to-one on the real numbers, but f(x) = 2x + 1 is.

If number 2 feels uncomfortable, do a proof book before Axler.

## Which book

### *Linear Algebra Done Right* (Sheldon Axler)

A very good book, aimed at a particular reader.

**Strengths**

- **Clear and carefully written.** The proofs are short, and people who work through it often come away understanding *why* linear algebra works, not just how to use it.
- **Built around linear maps, not matrices.** It works with abstract vector spaces and operators, and heads for eigenvalues, the spectral theorem and Jordan form.
- **Determinants come last.** It proves that eigenvalues exist without using determinants. This is the book's best-known feature, and people are split on it.
- **Free.** The fourth edition (2024) is open access under a Creative Commons licence, with a legal PDF at [linear.axler.net ↗](https://linear.axler.net/).

**Weaknesses**

- **Not a good first course for most people.** It assumes you are comfortable reading and writing proofs.
- **Light on computation.** It spends little time on row reduction, matrix algorithms, applications or numerical questions.
- **Delaying determinants has a cost.** It can leave you less fluent with a tool that every other course and field uses constantly.

It works best as a **second course**, taken after a computational first pass, or as a first course only if you already have some proof experience.

### Alternatives, by goal

| If you want… | Read |
|---|---|
| **Intuition first** | 3Blue1Brown, [*Essence of Linear Algebra* ↗](https://www.3blue1brown.com/lessons/eola-preview/) (free videos). Watch it before or alongside any book. |
| **A standard first course** | Gilbert Strang, *Introduction to Linear Algebra*, with his [MIT 18.06 lectures ↗](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) (free on OpenCourseWare). It is computational and full of applications. |
| **A free first course with proofs** | Jim Hefferon, [*Linear Algebra* ↗](https://hefferon.net/linearalgebra/) (free, with answers to the exercises), or Margalit and Rabinoff, [*Interactive Linear Algebra* ↗](https://textbooks.math.gatech.edu/ila/) (free online). |
| **Axler's level with determinants and matrices kept in** | Sergei Treil, [*Linear Algebra Done Wrong* ↗](https://sites.google.com/a/brown.edu/sergei-treil-homepage/linear-algebra-done-wrong) (free). The title is a friendly reply to Axler. |
| **A more complete proof-based text** | Friedberg, Insel and Spence, *Linear Algebra*. The standard rigorous course book, with more exercises and full canonical forms. |
| **The classics** | Halmos, *Finite-Dimensional Vector Spaces* (Axler's model; very concise), or Hoffman and Kunze, *Linear Algebra* (dense and more algebraic). |
| **Applied work, data or machine learning** | Boyd and Vandenberghe, [*Introduction to Applied Linear Algebra* ↗](https://web.stanford.edu/~boyd/vmls/) (VMLS, free), or Strang, *Linear Algebra and Learning from Data*. |
| **Numerical work: conditioning and stability** | Trefethen and Bau, *Numerical Linear Algebra*. |

### Suggested paths

- **New to linear algebra:** 3Blue1Brown, then Strang (or Hefferon), then Axler.
- **Comfortable with proofs:** Axler, with Treil or Friedberg next to it for determinants and matrix work.
- **Mainly want to compute:** Strang or Boyd, then Trefethen and Bau.

## What this library already covers

One chapter already teaches the opening of a proof-based course, and several other pages are its ingredients:

- [06_Algebraic_Structures](../../06_Algebraic_Structures/README.md) — the first definitions of any linear algebra course taught from axioms. [A definition is a test](../../06_Algebraic_Structures/a_definition_is_a_test/README.md) is the definition of a vector space, [subsets inherit the laws](../../06_Algebraic_Structures/subsets_inherit_the_laws/README.md) is why a subspace needs only three checks, and [maps that keep the laws](../../06_Algebraic_Structures/maps_that_keep_the_laws/README.md) is what a linear map is. They follow Axler's sections 1B, 1C and 3A, so they are a good way to try his style before starting the book.
- [The Cartesian product](../../04_Sets/cartesian_product/README.md) — ℝ² as ordered pairs. A vector in ℝⁿ is the same idea with n entries.
- [Multiplication as pairs](../../03_Complex_Numbers/multiplication_as_pairs/README.md) and [multiplication rotates](../../03_Complex_Numbers/multiplication_rotates/README.md) — complex multiplication as a rotation and scaling of the plane. That is a 2×2 matrix in disguise, and the natural way into rotation matrices.
- [Multiplication can be undone](../../03_Complex_Numbers/multiplication_can_be_undone/README.md) — zero divisors, and which elements you can divide by. Matrices have both problems, and that is exactly what *invertible* is about.
- [Roots of unity](../../03_Complex_Numbers/roots_of_unity/README.md) — useful later for the eigenvalues of rotations.
- [Relative error and correct digits](../../01_Precision/relative_error/README.md) and [catastrophic cancellation](../../01_Precision/catastrophic_cancellation/README.md) — the errors a computer makes when it solves Ax = b in floating point. A matrix's *condition number* says roughly how many significant digits the answer loses, which is the angle the [roadmap](../../ROADMAP.md) names for a linear algebra chapter here.

What the library does not cover yet are three of the prerequisites above: proofs, functions (one-to-one and onto) and systems of linear equations. The [roadmap](../../ROADMAP.md) lists the first two.
