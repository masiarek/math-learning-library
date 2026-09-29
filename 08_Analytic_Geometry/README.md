# 08_Analytic_Geometry — what does it mean to draw a number?

**Level:** 101 · for anyone starting precalculus, or anyone who has ever plotted a point

Descartes' idea, and the first section of every precalculus book: two number lines at right angles turn every point of the plane into a pair of numbers and every pair of numbers into a point. After that a question about a picture is a question about arithmetic, and a question about an equation has a picture. This chapter follows that idea in the order the books take it, one page of the book at a time, with the book's own questions at the end of each lesson and a deck of flashcards beside it.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [Rectangular coordinates](rectangular_coordinates/README.md) | What do the two numbers of a point measure, what is a quadrant, and why is the word worth having? |

## The through-line

Lesson 1 sets up the plane. A point is two signed distances, x from the y-axis and y from the x-axis, so [the Cartesian product](../04_Sets/cartesian_product/README.md) ℝ² is not just a set of pairs but the plane itself. A quadrant is the pair of signs and nothing more, which is why the axes belong to none and why the word carries so far: the sign of a trigonometric function, the quarter turn that [multiplying by i](../03_Complex_Numbers/multiplication_rotates/README.md) performs, and the symmetry of a graph are all statements about quadrants.

What comes next is on the [roadmap](../ROADMAP.md): the distance between two points, the midpoint, and the graph of an equation as the set of points that pass it.

## Where this is taught

The opening section of the chapter on graphs in any precalculus book; the lessons here follow Michael Sullivan's *Precalculus*, but Stewart, Larson, Blitzer and the free Stitz and Zeager cover the same page in the same order. For which book to read, see [Precalculus: a reading guide](../reading_guides/precalculus/README.md).

## A note on the code

Every point is a Python tuple of integers, so "is in quadrant II" is a check on two signs and every count is exact. Nothing is drawn: the one picture in the chapter is a grid of text cells, which is enough to see where four points land.
