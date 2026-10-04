# 07_Linear_Systems — what does it mean to solve a system of equations?

**Level:** 101 · for anyone who has solved two equations in two unknowns at school

At school a system of equations is something you solve by a trick: substitute, or add the equations, until one unknown is left. A linear algebra book starts the same place, but first it says exactly what is being looked for. A system is a list of tests, a solution is a list of numbers that passes every test, and solving means replacing the system by a simpler one with exactly the same solutions. This chapter follows that start, in the order of the first section of Jim Hefferon's *Linear Algebra*.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [Linear equations and their solutions](linear_equations/README.md) | What do the coefficients, constants, tuples and double subscripts in the first definition actually say? |

## The through-line

Lesson 1 reads the definition. A linear combination is a recipe of fixed coefficients, a linear equation is a test that a tuple passes or fails, and a solution of a system passes every one of its tests. One equation in two unknowns has a whole line of solutions, and a second equation can cut that down to one point. The name *linear* comes from the two things a linear combination keeps, sums and multiples, which is the link to [maps that keep the laws](../06_Algebraic_Structures/maps_that_keep_the_laws/README.md).

What comes next is on the [roadmap](../ROADMAP.md): why the three steps of Gauss's method never change the set of solutions, and why the three possible answers are one solution, none, or infinitely many.

## Where this is taught

The first section of [Jim Hefferon, *Linear Algebra* ↗](https://hefferon.net/linearalgebra/), free to download with answers to every exercise. Gilbert Strang's *Introduction to Linear Algebra* covers the same ground in its chapter on solving linear equations, with more pictures and fewer definitions. For which book to read first, and what to know before starting, see [Linear algebra: a reading guide](../reading_guides/linear_algebra/README.md).

## A note on the code

Every number is a `fractions.Fraction`, so a tuple satisfies an equation when the two sides are equal, not nearly equal. Solving a system in floating point is a different question, how many digits the answer keeps, and it is the one [01_Precision](../01_Precision/README.md) prepares for.

## Auf Deutsch: Stichwörter

Was es heißt, ein Gleichungssystem zu lösen: eine Gleichung ist ein Test, eine Lösung besteht jeden.

**Stichwörter:** lineares Gleichungssystem, Lösung, Lösungsmenge, Unbekannte, Gauß-Verfahren, Hefferon.
