# 10_Geometry — how few numbers fix a shape?

**Level:** 101 · for anyone reviewing geometry before precalculus, or coming back to it after many years

The geometry every precalculus book assumes, in the order Sullivan's review appendix gives it (Section A.2, *Geometry Essentials*): the Pythagorean theorem and its converse, the formulas for area and volume, and congruent and similar triangles. It is a prerequisite chapter, meant to be read just in time: the first section of the book proper, the [distance formula](../08_Analytic_Geometry/distance_formula/README.md), opens by sending the reader here. Each lesson ends with the book's questions and some of its own, answers folded away, and a deck of Anki flashcards whose `trap` cards are built around the tempting wrong answer.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [The Pythagorean theorem and its converse](pythagorean_theorem/README.md) | When do three lengths make a right angle, and why must the longest side go on the left? |
| 2 | [Area and volume formulas](area_and_volume_formulas/README.md) | How do you tell eleven formulas apart without memorising them, and catch a wrong one before using it? |
| 3 | [Congruent and similar triangles](congruent_and_similar_triangles/README.md) | Which three measurements fix a triangle, which fix only its shape, and why is SSA missing? |

## The through-line

A shape is decided by a few lengths, and everything else follows from them. Lesson 1: in a right triangle, two sides decide the third, and three sides decide whether the angle is right at all. Lesson 2: an area is two lengths multiplied and a volume three, so scaling every length by k scales area by k² and volume by k³, a test that catches a misremembered formula. Lesson 3: three well-chosen measurements decide a whole triangle, while three angles decide only its shape, and the shapes that match are the similar ones, related by one scale factor k, which is lesson 2's k again. The distance formula then puts lesson 1 into coordinates, and every later page of the book measures with it.

## Where this is taught

Every classroom precalculus book has a geometry review: Sullivan's Appendix A.2, Stewart's and Larson's appendices, Blitzer's inside covers. For which book to read, and when to read its review appendix, see [Precalculus: a reading guide](../reading_guides/precalculus/README.md).

## Po polsku, w skrócie

Rozdział z geometrii, którą zakłada każdy podręcznik do precalculusu: twierdzenie Pitagorasa i twierdzenie do niego odwrotne, wzory na pola i objętości, trójkąty przystające i podobne. Wspólna myśl: kształt wyznacza kilka długości, a reszta z nich wynika. Dwa boki trójkąta prostokątnego wyznaczają trzeci; pole to dwie długości pomnożone, objętość trzy, więc przy skali k pole rośnie k², a objętość k³; trzy dobrze wybrane pomiary wyznaczają cały trójkąt, a trzy kąty tylko jego kształt. To rozdział „do przeczytania w porę": wraca się do niego, gdy wzór na odległość w rozdziale 1 podręcznika tego wymaga. Powrót do podstaw nie jest porażką, tylko zwykłą drogą każdego, kto uczy się matematyki.

## A note on the code

Lengths are whole numbers or fractions wherever they can be, so "equal" in the Pythagorean test means equal, and answers with π are carried exactly as a + bπ until the last step. Only the construction of a triangle from an angle, in lesson 3, needs sines and cosines, and there the output is rounded to two decimals.
