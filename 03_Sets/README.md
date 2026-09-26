# 03_Sets — what is this collection, exactly?

**Level:** 101 · for anyone who has written a pair of coordinates

Before a chapter can talk about how long a set is, or how many points it holds, it has to be clear what a set *is* and how new ones are built from old ones. This chapter is that groundwork: the constructions that every later page takes for granted, each one checked on real sets by a program that runs.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [The Cartesian product](cartesian_product/README.md) | What is ℝ², and why is A × B not the same set as B × A? |

## The through-line

A set forgets everything except membership: {2, 5} and {5, 2} are one set. Almost all of mathematics needs more than that. A point in the plane has a first coordinate and a second, a function has an input and an output, a database row has columns in a fixed order. The **ordered pair** is the smallest object that remembers order, and the **Cartesian product** is the set of all of them. Everything from the coordinate plane to the definition of a function is built on it.

## A note on the code

Python has both objects natively: a `tuple` is an ordered pair and a `set` is a set. So the programs in this chapter do not simulate the definitions, they check them: `(2, 5) == (5, 2)` is asked directly and the interpreter answers `False`.
