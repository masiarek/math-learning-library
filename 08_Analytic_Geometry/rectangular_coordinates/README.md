# Rectangular coordinates

**Level:** 101 · for anyone starting precalculus, or anyone who has ever read a point off a graph

**One line:** A point of the plane is two signed distances, x from the y-axis and y from the x-axis, and a quadrant is nothing but the pair of signs; the axes belong to no quadrant because 0 has no sign, and that is exactly what makes the word useful.

## The idea

Two number lines, one horizontal and one vertical, crossing at right angles where both read 0. That is the whole apparatus, and it is Descartes' idea: once the lines are there, every point of the plane is one ordered pair of real numbers, and every ordered pair is one point. A question about points has become a question about numbers, which is why the subject is called *analytic* geometry and why the coordinate system carries his name.

[The Cartesian product](../../04_Sets/cartesian_product/README.md) built the set of pairs, ℝ² = {(x, y) | x, y ∈ ℝ}, and left it as a set. This page is the other half of the bargain: how one pair finds its point, and what the four pieces the axes cut the plane into are for. The textbook it follows is the opening of the chapter on graphs in Michael Sullivan's *Precalculus*; Ron Larson's *Precalculus* opens the same way with different words for the same things, and the page uses both. The questions at the end start from Sullivan's exercises.

## Symbol by symbol

| Piece | Say it | What it means |
|---|---|---|
| x-axis | "the x axis" | the horizontal number line. Positive to the right of O, negative to the left; the arrowhead marks the positive direction. |
| y-axis | "the y axis" | the vertical number line. Positive above O, negative below. |
| O | "the origin" | the point where the two axes cross. It reads 0 on both, so O = (0, 0). |
| xy-plane | "the x y plane" | the plane the two axes lie in; the **coordinate axes** are the two lines themselves. |
| (x, y) | "the point x, y" | an **ordered pair**: the **coordinates** of a point P. The book writes P = (x, y) and then just says "the point (x, y)". |
| x | "the x coordinate", or **abscissa** | the **signed distance** of P from the *y*-axis: how far right (x > 0) or left (x < 0) of the vertical line. |
| y | "the y coordinate", or **ordinate** | the signed distance of P from the *x*-axis: how far up (y > 0) or down (y < 0) from the horizontal line. |
| (x, 0), (0, y) | | the shape of a point on the x-axis, and of a point on the y-axis. |
| I, II, III, IV | "quadrant one" to "quadrant four" | the four regions the axes cut the plane into, numbered counterclockwise from the upper right. Points on the axes are in none of them. |

Two of these rows hide the two mistakes everyone makes once.

**Which axis a coordinate measures from.** The x-coordinate is the distance from the *y*-axis. It sounds backwards until you say what x measures: how far right or left. Right or left of what? Of the vertical line, and the vertical line is the y-axis. Section 2 of the program prints both distances for the four points of the book's figure, with the axis each one is measured from. Larson's page calls the same number the *directed distance* and draws it as an arrow from the y-axis to the point, labelled x; Wikipedia's figure draws it as an arrow along the x-axis from the point's foot back to the origin. Both arrows are the same length, because they are opposite sides of the rectangle the dotted lines make, so "distance along the x-axis" and "distance from the y-axis" are one number, and *directed* and *signed* are one word.

**Same scale, or not.** In mathematics the two axes usually carry the same scale, so that a unit right is as long on the page as a unit up. In an application, years along one axis and dollars along the other, each axis takes whatever scale suits it. The coordinates are numbers and do not change; only the picture does.

## One plane, three names

Sullivan says *rectangular coordinate system* and *xy-plane*; Larson and Wikipedia say *Cartesian plane*; other books say *coordinate plane*. They are one thing. *Rectangular* says how the axes meet, at right angles; *Cartesian* says who had the idea; *xy-plane* names the axes, and earns its keep later, when a z-axis is added and the xy-plane is one of three coordinate planes. What all three add to *the plane* of school geometry is the pair of axes: the same points, now with names.

The word *rectangular* also points at the one real alternative. Polar coordinates name the same point of the same plane by a different pair, its distance from the origin and its angle from the x-axis, so (1, 1) in rectangular coordinates is (√2, 45°) in polar. That is what "different from Cartesian" means when it means anything: not a different plane, a different way of naming its points, and the conversion between the two is a trigonometry chapter. Until then, rectangular, Cartesian and xy are three names for one plane, the way abscissa and x-coordinate are two names for one number.

## Two names for one number

The table gives x a second name, *abscissa*, and y a second name, *ordinate*, and the natural reaction is that a second name for a thing that already has one is silly. It is the other way round: these are the old names, and x and y are the newcomers. Both words are Latin, from the century in which coordinates were invented and before any letters were fixed for the axes. *Abscissa* is "cut off": the piece of the axis cut off between the origin and the foot of the perpendicular dropped from the point. *Ordinata* is "applied in order": that perpendicular itself, one of the family of parallel lines drawn in order to the axis in the Latin editions of Apollonius' work on conics. Leibniz used both in the 1690s, and coined *coordinates* for the pair. So a book that says "the x-coordinate, or abscissa" gives the modern name first and the original second.

In English the letters won, and a reader can go a lifetime saying x-coordinate. In most other languages the old words are the only ones: Polish *odcięta* and *rzędna*, French *abscisse* and *ordonnée*, German *Abszisse* and *Ordinate*, Russian *абсцисса* and *ордината*, each the Latin word translated or borrowed, and the axes are named after them, *oś odciętych* and *oś rzędnych* in Polish. The words also name the role rather than the letter, so they still mean something when the axes are called t and s. The concept is one and the names are two, which is why the [glossary](../../GLOSSARY.md) lists the second pair as synonyms of the first and nothing more.

One caution about a whiteboard that turns up everywhere: the abscissa is the number x, not the horizontal line. The line is the x-axis, or in the languages above the axis *of abscissas*.

## Plotting

To plot (−3, 1): go 3 units along the x-axis to the left of O, then straight up 1 unit, and put a dot there. The instructions come in the order of the pair, first entry then second, and that order is the whole content of the word *ordered*: (−3, 1) is 3 left and 1 up, while (1, −3) is 1 right and 3 down, a different point in a different quadrant. Section 3 checks it, and [the Cartesian product](../../04_Sets/cartesian_product/README.md) is the page on why a pair remembers which entry is first.

Section 1 draws the book's figure as a grid of cells: the four points (−3, 1), (3, 2), (3, −2) and (−2, −3), the y-axis as a column of `|`, the x-axis as a row of `-`, and the origin as `O`.

The grid lines are a reading aid, not a rule. (−1.5, −2.5) is as much a point as (−2, −3), in quadrant III by the same two signs, and so is (√2, 1/3): the plane is every pair of real numbers, all of ℝ², and the integer points are the ones with a grid line through them. The checker below takes decimals and fractions and draws them at the nearest cell.

## One notation, two meanings

Larson ends his page with a warning worth its own card: (x, y) means a point in the plane, and (x, y) also means an open interval on the number line, every real number t with x < t < y. Two objects, one notation, and only the context says which. The point (2, 5) is an ordered pair, a member of ℝ²; the interval (2, 5) is a set of numbers, and 3 is in it. Section 9 of the program keeps them apart in the one way Python can: a tuple `(2, 5)` holds the numbers 2 and 5 and nothing else, so `3 in (2, 5)` is false, while the interval is the test `2 < t < 5`, which 3 passes. There is one sure sign: an interval (a, b) needs a < b, so (5, 2) can only be a point. Intervals are the tool of [what measure zero means](../../02_Measure_Zero/what_measure_zero_means/README.md), where every length is a length of intervals, and none of them is a point.

## What a quadrant is, and why the word earns its keep

The definition is four lines of inequalities: quadrant I is x > 0 and y > 0, II is x < 0 and y > 0, III is x < 0 and y < 0, IV is x > 0 and y < 0. Read them once more and notice what is *not* in them: the sizes of x and y. A quadrant is the pair of signs and nothing else. (1, 1) and (1000, 5) are both in quadrant I; section 4 of the program lists the sign of each coordinate next to the quadrant and the third column never looks at anything but the first two.

That is why the word is useful. It is a name for the coarsest thing you can know about a point without knowing its numbers, and a great deal of later mathematics runs on exactly that much:

- **Trigonometry**, where the word does the most work. An angle's terminal side lies in one quadrant, and that quadrant fixes the sign of its sine, cosine and tangent before any value is computed. Solving sin θ = −1/2 starts with "the sine is negative, so θ is in quadrant III or IV", and the reference-angle method is a rule for each quadrant.
- **Angles from coordinates.** The tangent of an angle is y/x, and y/x is the same number for (3, 2) and (−3, −2), which are half a turn apart. The quadrant is what tells them apart; the two-argument arctangent, `atan2(y, x)` in every programming language, exists to read it.
- **Complex numbers.** A complex number is a point (x, y), so it has a quadrant, and [multiplication rotates](../../03_Complex_Numbers/multiplication_rotates/README.md) says multiplying by i turns a point a quarter turn counterclockwise: one quadrant on, I to II to III to IV and back. Section 8 runs the four points of the figure through it. The quadrants are numbered in the direction a turn goes, which is why the numbering is counterclockwise and not clockwise.
- **Symmetry of a graph.** Replacing x by −x reflects a point across the y-axis, and section 6 shows what that does to quadrants: I and II swap, III and IV swap, whatever the numbers. So a graph symmetric about the y-axis is known everywhere once it is known in quadrants I and IV, and a book's test for symmetry, "replace x by −x and see if the equation survives", is a statement about quadrants.
- **The sign of a product.** xy > 0 exactly in quadrants I and III, xy < 0 exactly in II and IV; section 7 checks it. "The graph of y = 1/x lies in quadrants I and III" is a fact about the sign of xy, and so is the sign of a correlation: plot every observation relative to the two means and the covariance is positive when the points in quadrants I and III outweigh those in II and IV.
- **Inequalities in two variables.** x > 0 and y > 0 is the simplest system of two inequalities, and its solution set is a quadrant. Every shaded region in a linear-programming picture is described the same way, and "the feasible region lies in the first quadrant" is the usual first constraint.

And why the axes are in no quadrant. Zero is neither positive nor negative, so a point with a 0 coordinate has no pair of signs to be sorted by. The book could have written ≥ instead of > and put the axes in; section 5 shows what that costs on the 25 points with coordinates from −2 to 2. With strict signs the counts are 4, 4, 4, 4 and 9 on the axes, 25 in all, every point counted once. With ≥ the counts are 9, 9, 9, 9, which is 36 memberships for 25 points: the origin is in all four quadrants and every other axis point in two. The four quadrants are meant to be a *partition* of the plane off the axes, each point in exactly one, and that is what the strict inequalities buy.

## What the program prints

The program stores each point as a Python tuple, which is an ordered pair, and sorts it into a quadrant by looking at the two signs and nothing else. Every number is an integer, so every claim is exact.

<!-- output:rectangular_coordinates -->
*Verified output of [`rectangular_coordinates.py`](examples/rectangular_coordinates.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. THE PLANE, AND THE FOUR POINTS OF THE FIGURE
   y
     4   .  .  .  .  |  .  .  .  .
     3   .  .  .  .  |  .  .  .  .
     2   .  .  .  .  |  .  .  B  .
     1   .  A  .  .  |  .  .  .  .
     0   -  -  -  -  O  -  -  -  -
    -1   .  .  .  .  |  .  .  .  .
    -2   .  .  .  .  |  .  .  C  .
    -3   .  .  D  .  |  .  .  .  .
    -4   .  .  .  .  |  .  .  .  .
        -4 -3 -2 -1  0  1  2  3  4   x
   A = (-3, 1)
   B = (3, 2)
   C = (3, -2)
   D = (-2, -3)
   The y-axis is the column of |, the x-axis the row of -, O the origin.

2. EACH COORDINATE IS A SIGNED DISTANCE, AND FROM THE OTHER AXIS
     point      x: from the y-axis     y: from the x-axis     to plot it
     (-3, 1)    3 left  of it         1 up   from it        3 left, then 1 up
     (3, 2)     3 right of it         2 up   from it        3 right, then 2 up
     (3, -2)    3 right of it         2 down from it        3 right, then 2 down
     (-2, -3)   2 left  of it         3 down from it        2 left, then 3 down
   x says how far right or left, which is distance from the vertical
   line, the y-axis. The sign says which side; the size says how far.

3. THE PAIR IS ORDERED: (-3, 1) IS NOT (1, -3)
     (-3, 1) == (1, -3)   is False
     (-3, 1)   3 left, 1 up      quadrant II
     (1, -3)   1 right, 3 down   quadrant IV
   Same two numbers, different point. The first entry is always x.

4. A QUADRANT IS NOTHING BUT THE PAIR OF SIGNS
     point        sign of x   sign of y   quadrant
     (3, 2)           +           +       I
     (-3, 1)          -           +       II
     (-2, -3)         -           -       III
     (3, -2)          +           -       IV
     (1, 1)           +           +       I
     (1000, 5)        +           +       I
     (-1, 1000)       -           +       II
     (0, 0)           0           0       none: on an axis
     (4, 0)           +           0       none: on an axis
     (0, -2)          0           -       none: on an axis
   (1, 1) and (1000, 5) share a quadrant: the sizes never enter into it.
   A 0 has no sign, so a point with a 0 coordinate has no quadrant.

5. WHY THE AXES MUST BELONG TO NO QUADRANT
   every point with integer coordinates from -2 to 2, 5 x 5 = 25 points:
     quadrant I: 4   II: 4   III: 4   IV: 4   on an axis: 9
     4 + 4 + 4 + 4 + 9 = 25: each point counted exactly once.
   the same 25 points if the quadrants were defined with >= and <= instead:
     quadrant I: 9   II: 9   III: 9   IV: 9
     9 + 9 + 9 + 9 = 36 memberships for 25 points: the origin would be in
     all four and every other axis point in two. Strict signs make the
     four quadrants a partition: every point off the axes is in exactly one.

6. WHAT THE WORD BUYS YOU: A SIGN CHANGE IS A CHANGE OF QUADRANT
     point        (-x, y)          (x, -y)          (-x, -y)
                  across y-axis    across x-axis    through O
     (-3, 1)   II   (3, 1)    I      (-3, -1)  III    (3, -1)   IV
     (3, 2)    I    (-3, 2)   II     (3, -2)   IV     (-3, -2)  III
     (3, -2)   IV   (-3, -2)  III    (3, 2)    I      (-3, 2)   II
     (-2, -3)  III  (2, -3)   IV     (-2, 3)   II     (2, 3)    I
   Negating x swaps I with II and III with IV, whatever the numbers are.
   That is why a graph's symmetry can be checked one quadrant at a time.

7. THE SIGN OF A PRODUCT NAMES TWO QUADRANTS
     point        x * y    sign   quadrant
     (3, 2)          6     +      I
     (-3, 1)        -3     -      II
     (-2, -3)        6     +      III
     (3, -2)        -6     -      IV
     (5, 5)         25     +      I
     (-5, 5)       -25     -      II
   xy > 0 exactly in I and III, xy < 0 exactly in II and IV. So 'the graph
   of y = 1/x lies in quadrants I and III' is a fact about the sign of xy.

8. A QUARTER TURN MOVES A POINT ONE QUADRANT ON
   the rule (x, y) -> (-y, x), which is multiplication by i in 03_Complex_Numbers:
     (-3, 1)   quadrant II   ->  (-1, -3)  quadrant III
     (3, 2)    quadrant I    ->  (-2, 3)   quadrant II
     (3, -2)   quadrant IV   ->  (2, 3)    quadrant I
     (-2, -3)  quadrant III  ->  (3, -2)   quadrant IV
   I -> II -> III -> IV -> I: the quadrants are numbered in the direction
   a quarter turn goes, counterclockwise, which is why the numbering is
   the one it is and not clockwise.

9. THE SAME SYMBOLS, TWO OBJECTS: THE POINT (2, 5) AND THE INTERVAL (2, 5)
   as a point, (2, 5) is a pair, 2 right and 5 up, quadrant I:
     len((2, 5)) = 2;   3 in (2, 5) is False   a tuple holds 2 and 5, not 3
   as an open interval, (2, 5) is a test, 2 < t < 5:
     t = 3:  2 < 3 < 5  is True
     t = 2:  2 < 2 < 5  is False
     t = 5:  2 < 5 < 5  is False
     t = 7:  2 < 7 < 5  is False
   the endpoints fail: open means the ends are left out.
   (5, 2) as a point is 5 right and 2 up, quadrant I. As an interval:
     t = 3:  5 < 3 < 2  is False;   no t passes, the interval (5, 2) is empty,
     so when a < b fails the notation can only mean the point.
```
<!-- /output -->

## Questions

Try each one before opening the answer. The first few are from the page, the later ones ask what the page implies.

**1. Which quadrant, or which axis, is each point in: (−4, 2), (5, −1), (0, −3), (−2, −2), (7, 0), (0, 0)?**

<details><summary>Answer</summary>

(−4, 2) is in quadrant II; (5, −1) in IV; (0, −3) on the y-axis; (−2, −2) in III; (7, 0) on the x-axis; (0, 0) is the origin, on both axes. The three with a 0 coordinate are in no quadrant.

</details>

**2. The x-coordinate of a point is its signed distance from which axis? Why that one?**

<details><summary>Answer</summary>

From the y-axis. x measures how far right or left the point is, and "right or left" is measured from the vertical line, which is the y-axis. Likewise y, how far up or down, is measured from the x-axis.

</details>

**3. Are (2, 5) and (5, 2) the same point? Where is each?**

<details><summary>Answer</summary>

No. (2, 5) is 2 right and 5 up; (5, 2) is 5 right and 2 up. Both are in quadrant I, so this time the quadrant does not tell them apart; the order of the pair does. Compare (−3, 1) and (1, −3) in section 3, which land in different quadrants.

</details>

**4. Give the coordinates of the point 4 units to the left of the y-axis and 3 units below the x-axis. Which quadrant is it in?**

<details><summary>Answer</summary>

(−4, −3), in quadrant III: left means x < 0, below means y < 0. It is 5 units from the origin, by the 3-4-5 triangle, which is the distance formula of the next lesson.

</details>

**5. P = (x, y) is in quadrant II. Which quadrant is each of these in: (−x, y), (x, −y), (−x, −y), (y, x)?**

<details><summary>Answer</summary>

In quadrant II, x < 0 and y > 0. So (−x, y) has both entries positive: quadrant I. (x, −y) has both negative: III. (−x, −y) has first positive, second negative: IV. (y, x) has first positive, second negative: IV as well. Section 6 checks the first three on (−3, 1).

</details>

**6. Why do the axes belong to no quadrant? What would go wrong if quadrant I were defined by x ≥ 0 and y ≥ 0?**

<details><summary>Answer</summary>

Because 0 has no sign, and a quadrant is a pair of signs. With ≥ the origin would be in all four quadrants and every other point on an axis in two, so the quadrants would overlap instead of partitioning the plane. Section 5 counts it: 36 memberships for 25 points.

</details>

**7. The product xy of a point's coordinates is negative. Which quadrants could the point be in?**

<details><summary>Answer</summary>

II or IV: the two where x and y have opposite signs. If xy is positive, I or III. If xy = 0, the point is on an axis. Section 7.

</details>

**8. Is x + y > 0 for every point in quadrant I? In quadrant II?**

<details><summary>Answer</summary>

In quadrant I yes: both are positive, so their sum is. In quadrant II it depends on the sizes, (−1, 5) gives 4 and (−5, 1) gives −4, so the quadrant alone cannot say. That is the limit of the word: it knows signs and nothing about sizes, and x + y depends on sizes.

</details>

**9. Count the points with integer coordinates from −3 to 3 in each quadrant and on the axes.**

<details><summary>Answer</summary>

7 × 7 = 49 points. Off the axes, each quadrant holds the 3 × 3 = 9 points with both coordinates nonzero and of the right signs, 36 in all; the axes hold the other 13: 7 on the x-axis and 7 on the y-axis, minus the origin counted twice. 36 + 13 = 49. Section 5 does the same count for −2 to 2 and gets 16 + 9 = 25.

</details>

**10. A graph is drawn with years along the x-axis and dollars along the y-axis, so the two axes have different scales. Does the point (3, 3) still lie on the line through O at 45°?**

<details><summary>Answer</summary>

Its coordinates are still (3, 3) and it is still in quadrant I, 3 units right and 3 units up in each axis's own scale. But on the page it will not be at 45° unless a unit of each axis has the same length. A coordinate is a number; the angle on the paper belongs to the drawing.

</details>

**11. The complex number (3, −2), which the book would write 3 − 2i, is a point. Which quadrant? Which quadrant after multiplying it by i?**

<details><summary>Answer</summary>

Quadrant IV. Multiplying by i sends (x, y) to (−y, x), so (3, −2) goes to (2, 3), in quadrant I: one quadrant on, counterclockwise. Section 8, and [multiplication rotates](../../03_Complex_Numbers/multiplication_rotates/README.md) for why the rule is a quarter turn.

</details>

**12. The book says "the point (x, y)" instead of "the point whose coordinates are (x, y)". What is it identifying with what, and what page in this library is about that identification?**

<details><summary>Answer</summary>

A point of the plane with an ordered pair of real numbers, each point with exactly one pair. That is the claim that ℝ² *is* the plane, and [the Cartesian product](../../04_Sets/cartesian_product/README.md) is the page on what ℝ² is as a set.

</details>

**13. Is (2, 5) a point or an open interval? Is (5, 2)? Is 3 in (2, 5)?**

<details><summary>Answer</summary>

(2, 5) could be either, and only the sentence around it says which. (5, 2) can only be a point, because an interval (a, b) needs a < b. Whether 3 is in (2, 5) depends on the reading: 3 is in the interval, since 2 < 3 < 5, and it is not in the point, which holds only the numbers 2 and 5. Section 9.

</details>

**14. Which quadrant, or which axis, is each of these in: (−1.5, −2.5), (−1.5, 0), (√2, 1/3)?**

<details><summary>Answer</summary>

(−1.5, −2.5) is in quadrant III, (−1.5, 0) on the x-axis, and (√2, 1/3) in quadrant I. The signs decide, and the grid lines have nothing to do with it. Run `plot_points.py -1.5,-2.5 -1.5,0` to see the first two drawn at their nearest cells.

</details>

**15. Sullivan says *rectangular coordinate system* and Larson says *Cartesian plane*. What is the difference?**

<details><summary>Answer</summary>

None in what they name: the same plane with the same two axes. *Rectangular* describes the right angle between the axes, *Cartesian* credits Descartes. The one system that is genuinely different is polar coordinates, which name the same points of the same plane by distance and angle instead.

</details>


## Plot it yourself, and let the program check it

The book's own exercise after this section is to plot six points and say which quadrant or axis each lies on, and a drawing is a poor thing to check: the check is a pair of numbers, and a pencil dot is neither. So the second program, [`plot_points.py`](examples/plot_points.py), does the checking. Run with no arguments it plots the two exercises, problems 15 and 16, and that is its recorded output:

<!-- output:plot_points -->
*Verified output of [`plot_points.py`](examples/plot_points.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
PROBLEM 15: plot each point; state which quadrant or coordinate axis it lies on
     y
     6   .  .  .  .  .  .  |  .  .  .  .  .  .
     5   .  .  .  .  .  .  |  .  .  .  .  .  D
     4   .  .  .  .  .  .  |  .  .  .  .  .  .
     3   .  .  .  .  .  .  |  .  .  .  .  .  .
     2   .  .  .  A  .  .  |  .  .  .  .  .  .
     1   .  .  .  .  .  .  |  .  .  .  .  .  .
     0   -  -  -  -  -  -  O  -  -  -  -  -  B
    -1   .  .  .  .  .  .  |  .  .  .  .  .  .
    -2   .  .  .  .  C  .  |  .  .  .  .  .  .
    -3   .  .  .  .  .  .  E  .  .  .  .  .  F
    -4   .  .  .  .  .  .  |  .  .  .  .  .  .
    -5   .  .  .  .  .  .  |  .  .  .  .  .  .
    -6   .  .  .  .  .  .  |  .  .  .  .  .  .
        -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6   x
   A = (-3, 2)    quadrant II
   B = (6, 0)     on the x-axis
   C = (-2, -2)   quadrant III
   D = (6, 5)     quadrant I
   E = (0, -3)    on the y-axis
   F = (6, -3)    quadrant IV

PROBLEM 16: plot each point; state which quadrant or coordinate axis it lies on
     y
     6   .  .  .  .  .  .  |  .  .  .  .  .  .
     5   .  .  .  .  .  .  |  .  .  .  .  .  .
     4   .  .  .  C  .  .  |  A  .  .  .  .  .
     3   .  .  .  .  .  .  |  .  .  .  .  .  .
     2   .  .  .  .  .  .  |  .  .  .  .  .  .
     1   .  .  .  .  .  .  E  .  .  .  D  .  .
     0   -  -  -  F  -  -  O  -  -  -  -  -  -
    -1   .  .  .  .  .  .  |  .  .  .  .  .  .
    -2   .  .  .  .  .  .  |  .  .  .  .  .  .
    -3   .  .  .  .  .  .  |  .  .  .  .  .  .
    -4   .  .  .  B  .  .  |  .  .  .  .  .  .
    -5   .  .  .  .  .  .  |  .  .  .  .  .  .
    -6   .  .  .  .  .  .  |  .  .  .  .  .  .
        -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6   x
   A = (1, 4)     quadrant I
   B = (-3, -4)   quadrant III
   C = (-3, 4)    quadrant II
   D = (4, 1)     quadrant I
   E = (0, 1)     on the y-axis
   F = (-3, 0)    on the x-axis

To check a plot of your own:  python3 plot_points.py -3,2 6,0 0,-3
For eight points to practise on:  python3 plot_points.py --drill 3
```
<!-- /output -->

Do the two problems on paper first, then compare. To check points of your own, type them after the program name as `x,y`, integers, decimals or fractions, and it draws them and states the quadrant or axis of each:

```bash
python3 08_Analytic_Geometry/rectangular_coordinates/examples/plot_points.py -3,2 6,0 0,-3
```

That path starts at the root of a clone, like every command in this library, so first `git clone https://github.com/masiarek/math-learning-library.git` and `cd math-learning-library`; typed from any other folder, Python answers "No such file or directory". The program needs nothing but itself, so the other route is to fetch the one file and run it where it lands:

```bash
curl -O https://raw.githubusercontent.com/masiarek/math-learning-library/master/08_Analytic_Geometry/rectangular_coordinates/examples/plot_points.py
python3 plot_points.py -3,2 6,0 0,-3
```

Unlabelled points are called A, B, C in order; `P=2,5` names one yourself. A point between grid lines, such as `-1.5,-2.5`, is drawn at the nearest cell with a lowercase letter and its quadrant stated exactly. Two points in one cell print as `*` and are named below the grid, which is how the program tells you that (2, 5) written twice is one point and (2, 5) and (5, 2) are two.

## How to practise

The skill is two-way and small, so practise both directions until neither needs thought:

1. **Coordinates to a dot, dot to coordinates.** Take a drill, `python3 plot_points.py --drill 1`, and change the number for a fresh set: it prints eight points, then a line to cover, then the grid and the answers. Plot the eight on squared paper and name the quadrant or axis of each before uncovering. Then the other way: put a dot anywhere on the grid, read its coordinates off, and confirm with the program.
2. **Signs before sizes.** Cover the numbers of a pair and look only at the signs; name the quadrant. Then uncover and plot. The quadrant should be known before the pencil moves, because that is all the word is.
3. **The two traps, once a day.** Plot (−3, 1) and (1, −3) together, and (2, 5) and (5, 2) together, and say aloud which axis x is measured from. Both mistakes are made once by everyone and never again by anyone who says the reason out loud.
4. **The cards.** The Anki deck below, five minutes a day; the review schedule does the spacing, and the tags let you study only `quadrants` or only `signed-distance` when one kind keeps slipping.
5. **The questions above**, once, for the reasoning: they ask what the page implies, which is what the next pages of the book assume.

## Flashcards

The same page as a deck of 57 Anki cards, one fact per card: [`rectangular_coordinates.txt`](anki/rectangular_coordinates.txt). In Anki choose File → Import, pick the file, and the header lines inside it set the separator, the note type (Basic), the deck name and the tags, so nothing needs changing in the dialog. Each card carries a tag for its kind, `definition`, `quadrants`, `plotting` and so on, for studying one kind at a time.

## Where this goes next

The next page in every precalculus book is the distance between two points, which is Pythagoras written in coordinates, and after it the midpoint. Then the book's real subject: the graph of an equation in x and y is the set of all points whose coordinates pass the equation, so a line of solutions in [linear equations and their solutions](../../07_Linear_Systems/linear_equations/README.md) becomes a line on the page. The [roadmap](../../ROADMAP.md) lists all three.

## See also

- [The Cartesian product](../../04_Sets/cartesian_product/README.md) — ℝ² as a set of pairs, and why (2, 5) is not (5, 2)
- [Multiplication as pairs](../../03_Complex_Numbers/multiplication_as_pairs/README.md) — a complex number is a point (x, y) of this plane
- [Multiplication rotates](../../03_Complex_Numbers/multiplication_rotates/README.md) — multiplying by i is the quarter turn of section 8, one quadrant on
- [Linear equations and their solutions](../../07_Linear_Systems/linear_equations/README.md) — one equation in x and y has a whole line of solutions, and those solutions are points here
- [Mean, average, arithmetic mean](../../05_Statistics/mean_vs_average/README.md) — the two means that a scatter plot's quadrants are drawn from
- [Precalculus: a reading guide](../../reading_guides/precalculus/README.md) — where this sits in the course, and which book to read it in
- [Cartesian coordinate system ↗](https://en.wikipedia.org/wiki/Cartesian_coordinate_system) — Wikipedia, with the history and the higher-dimensional version
- Michael Sullivan, *Precalculus* (Pearson), the section "Rectangular Coordinates" that opens the chapter on graphs; this page follows it
- Ron Larson, *Precalculus* (Cengage), section 1.1, the same page with *directed distance* for signed distance and the warning about (x, y) as an interval
