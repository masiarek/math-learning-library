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
| O | "the origin" | the point where the two axes cross: the one chosen as 0 on both when the axes were laid down, so O = (0, 0), one 0 per axis. On a number line the origin is the single point 0. Its coordinates are (0, 0) by definition; *which* point of the plane gets them is a choice, not a feature of the plane: draw the axes elsewhere and another point is the origin, and every coordinate changes, while the points and the distances between them do not. It is the centre of the picture, because that is where the axes are drawn, and not of the plane, which has none. |
| xy-plane | "the x y plane" | the plane the two axes lie in; the **coordinate axes** are the two lines themselves. |
| (x, y) | "the point x, y" | an **ordered pair**: the **coordinates** of a point P, plural, one coordinate per axis. On a number line a point has one coordinate; in the plane it has two; in space, three. The book writes P = (x, y) and then just says "the point (x, y)". |
| x | "the x coordinate", or **abscissa** | the **signed distance** of P from the *y*-axis: how far right (x > 0) or left (x < 0) of the vertical line. |
| y | "the y coordinate", or **ordinate** | the signed distance of P from the *x*-axis: how far up (y > 0) or down (y < 0) from the horizontal line. |
| (x, 0), (0, y) | | the shape of a point on the x-axis, and of a point on the y-axis. |
| I, II, III, IV | "quadrant one" to "quadrant four" | the four regions the axes cut the plane into, numbered counterclockwise from the upper right. Points on the axes are in none of them. |

Two of these rows hide the two mistakes everyone makes once.

**Which axis a coordinate measures from.** The x-coordinate is the distance from the *y*-axis. It sounds backwards until you say what x measures: how far right or left. Right or left of what? Of the vertical line, and the vertical line is the y-axis. Section 2 of the program prints both distances for the four points of the book's figure, with the axis each one is measured from. Larson's page calls the same number the *directed distance* and draws it as an arrow from the y-axis to the point, labelled x; Wikipedia's figure draws it as an arrow along the x-axis from the point's foot back to the origin. Both arrows are the same length, because they are opposite sides of the rectangle the dotted lines make, so "distance along the x-axis" and "distance from the y-axis" are one number, and *directed* and *signed* are one word.

**Same scale, or not.** In mathematics the two axes usually carry the same scale, so that a unit right is as long on the page as a unit up. In an application, years along one axis and dollars along the other, each axis takes whatever scale suits it. The coordinates are numbers and do not change; only the picture does.

## One plane, three names

Sullivan says *rectangular coordinate system* and *xy-plane*; Larson and Wikipedia say *Cartesian plane*; other books say *coordinate plane*. They are one thing. *Rectangular* says how the axes meet, at right angles; *Cartesian* says who had the idea; *xy-plane* names the axes, and earns its keep later, when a z-axis is added and the xy-plane is one of three coordinate planes. What all three add to *the plane* of school geometry is the pair of axes: the same points, now with names.

The plane before the axes has a property with a name, and it is the reason the origin is a choice: it is *homogeneous*. Every point looks exactly like every other, and sliding the whole plane carries any point onto any other without changing a single distance, so nothing in the plane itself can pick out a centre or a zero. The axes do the picking. That is the whole of the origin's specialness: it is special relative to the coordinate system drawn over the plane, and (0, 0) by definition, not by any property of the point.

The word *rectangular* also points at the one real alternative. Polar coordinates name the same point of the same plane by a different pair, its distance from the origin and its angle from the x-axis, so (1, 1) in rectangular coordinates is (√2, 45°) in polar. That is what "different from Cartesian" means when it means anything: not a different plane, a different way of naming its points, and the conversion between the two is a trigonometry chapter. Until then, rectangular, Cartesian and xy are three names for one plane, the way abscissa and x-coordinate are two names for one number.

## Which way is positive, and who cares

The arrowhead on an axis marks its positive direction, and it is fair to ask whether that is worth a card. Some books draw arrowheads on both ends of each axis, and that is fine: there the arrows mean "the line goes on forever both ways", and the numbers along the axis say which way is positive. The split does not follow subjects, whatever a tidy answer says: Sullivan, Larson and Wikipedia's number line draw one arrowhead, at the positive end, while much school graph paper and many geometry books draw two, so a reader meets both conventions in the same year. Either way, something has to say it, because which way is positive is not decoration. It is the *orientation* of the plane, and a surprising amount hangs on it.

With x positive to the right and y positive upward, the turn from the positive x-axis toward the positive y-axis is counterclockwise. That one fact is why the quadrants are numbered counterclockwise, why angles are measured counterclockwise, why [multiplying by i](../../03_Complex_Numbers/multiplication_rotates/README.md) is a counterclockwise quarter turn, and why a line through the origin and (2, 2) "rises". Flip one axis and every one of those turns the other way. Nobody does that on paper, but every computer screen does: pixel coordinates put the origin at the top left with y positive *downward*, so the mathematician's counterclockwise is the screen's clockwise, the visible screen is what the book would call quadrant IV, and a rotation formula copied from a textbook turns the wrong way. That is the most common sign bug in graphics code, and it is exactly the arrow.

That is also the whole answer to why the quadrants are numbered counterclockwise. An angle in standard position starts on the positive x-axis and opens toward the positive y-axis, and with the usual axes that is counterclockwise. Its first quarter turn, 0° to 90°, sweeps the region above the positive x-axis and to the right of the positive y-axis, where both coordinates are positive; that is quadrant I, first because the sweep starts there. The next quarter turns sweep II, III and IV in order, so the numbers on the quadrants are the order a growing angle visits them. Nothing about the plane prefers counterclockwise. The axes do: draw y downward and the same rule numbers the quadrants clockwise on the page, as the two pictures below show.

Section 10 of the program draws the same four points twice, once with y upward and once with y downward, not one coordinate changed. The quarter turn visits them in the order 1, 2, 3, 4 in both pictures, counterclockwise in the first and clockwise in the second. The same choice decides the sign of a slope, of an angle, of an area computed by a determinant, of a physics equation for a falling object where "up is positive" or "down is positive" flips the sign of g, and of a compass bearing, measured clockwise from north where mathematics measures counterclockwise from east. So who cares: anyone who has ever had a rotation come out backwards. The arrow is the one mark on the figure that says which way is around.

## Two names for one number

The table gives x a second name, *abscissa*, and y a second name, *ordinate*, and the natural reaction is that a second name for a thing that already has one is silly. It is the other way round: these are the old names, and x and y are the newcomers. Both words are Latin, from the century in which coordinates were invented and before any letters were fixed for the axes. *Abscissa* is "cut off": the piece of the axis cut off between the origin and the foot of the perpendicular dropped from the point. *Ordinata* is "applied in order": that perpendicular itself, one of the family of parallel lines drawn in order to the axis in the Latin editions of Apollonius' work on conics. Leibniz used both in the 1690s, and coined *coordinates* for the pair. So a book that says "the x-coordinate, or abscissa" gives the modern name first and the original second.

In English the letters won, and a reader can go a lifetime saying x-coordinate. In most other languages the old words are the only ones: Polish *odcięta* and *rzędna*, French *abscisse* and *ordonnée*, German *Abszisse* and *Ordinate*, Russian *абсцисса* and *ордината*, each the Latin word translated or borrowed, and the axes are named after them, *oś odciętych* and *oś rzędnych* in Polish. The third coordinate has a name of the same kind, *applicate*, rare in English but alive in Polish as *kota* and in French as *cote*, so the three coordinates of a point in space are odcięta, rzędna, kota. The words also name the role rather than the letter, so they still mean something when the axes are called t and s. The concept is one and the names are two, which is why the [glossary](../../GLOSSARY.md) lists the second pair as synonyms of the first and nothing more.

One caution about a whiteboard that turns up everywhere: the abscissa is the number x, not the horizontal line. The line is the x-axis, or in the languages above the axis *of abscissas*.

For a reader who learned this in Polish, or is about to, the page's vocabulary in that language. *Współrzędna* is the Latin word rebuilt from Polish parts, *współ-* for "co-" and *rzędna* for "ordinate", so the etymology above is visible in the word itself.

| English | Polish |
|---|---|
| coordinate, coordinates | współrzędna, współrzędne |
| coordinate system; rectangular or Cartesian | układ współrzędnych; prostokątny or kartezjański układ współrzędnych |
| number line | oś liczbowa |
| x-axis, y-axis | oś x and oś y; oś odciętych and oś rzędnych; also oś OX and oś OY |
| origin | początek układu współrzędnych |
| x-coordinate, abscissa | współrzędna x, odcięta |
| y-coordinate, ordinate | współrzędna y, rzędna |
| z-coordinate, applicate | współrzędna z, kota |
| ordered pair | para uporządkowana |
| to plot a point | zaznaczyć punkt |
| quadrant; quadrant I | ćwiartka; pierwsza ćwiartka |
| plane | płaszczyzna |

## Names on the number line

Everything on this page happens first in one dimension, and the number line has its own names. The book's word for the number is *coordinate*: the real number associated with a point. The other direction has a name in most algebra books: the point associated with a number is the *graph* of the number, so the coordinate of the graph of 3 is 3, and "graph the number −2" means put a dot there. The number is also the point's *signed distance* from 0, which Larson calls its *directed distance*; 0 is the *origin*; and older books call the point 1 the *unit point*, because choosing it fixes the scale. *Position* is what physics calls the coordinate of a moving point, and *address* is a classroom metaphor. Three words that circulate for this and do not fit: a *locus* is the set of all points meeting a condition, a line or a curve rather than one point; a *tick mark* is a scale mark drawn at every unit whether or not a point is plotted there; and *abscissa* belongs to the plane, where it is the x-coordinate of a point that has two, and on a lone number line nobody uses it.

What the number line says is this page's idea one dimension down: each point is exactly one real number and each real number exactly one point, so "the point 3" and "the number 3" are the same phrase. The plane does it twice. Wikipedia's definition of the one-dimensional system says all three things in three sentences: "an arbitrary point O (the origin) is chosen on a given line"; "the coordinate of a point P is defined as the signed distance from O to P"; and "each point is given a unique coordinate and each real number is the coordinate of a unique point". One coordinate per point, singular, the origin chosen, and the identification both ways.

Why not just say "the x-axis number", or "the x-axis address"? You can, and "the x-value" is what most people say aloud, including mathematicians. The word *coordinate* earns its keep in three ways, none of them a rule against plain speech. It works everywhere: for any axis, for the three coordinates of a point in space, and for polar coordinates, whose two numbers lie on no axis at all, so one word covers what "x-axis number" would need a new phrase for each time. It avoids a misreading: "a number on the x-axis" names a point of the axis, (3, 0), while the x-coordinate of (3, 5) is a number the point is not on; the coordinate is read off the axis, it does not live there. And it is the word in every book and every language, *współrzędna* in Polish, so it is the one you need in order to read. *Address* is a fine metaphor for the whole pair, and the book's own phrase "the coordinates of P" means exactly that. Say what you like; learn the standard word to read.

There is one more way to put the objection, and it is the sharpest: why not call the x-coordinate of P "the point on the x-axis under P"? That point exists and has a name, the *foot* of the perpendicular from P to the axis, and the picture is exactly right: drop a line from P = (3, 5) straight down and it lands on (3, 0). But (3, 0) is a point, with two coordinates of its own, and 3 is a number, and the whole subject rests on not confusing the two. Wikipedia's first paragraph on coordinate systems ends with the reason: a coordinate system lets "problems in geometry be translated into problems about numbers and vice versa". The foot is still on the geometry side of that translation. The coordinate is the number side, and it is the side the equations live on: y = 2x + 1 takes the number 3 and gives 7, and there is nothing it can do with the point (3, 0). Section 11 of the program makes Python say it: the foot is not equal to the number, doubling the number gives 6 and doubling the point gives nonsense, and the one thing the point and P share is their x-coordinate, which is what the perpendicular was for. Wikipedia's article on the abscissa says the same thing in its technical sentence: "the abscissa of a point is the signed measure of its projection on the primary axis". The projection is the foot, a point; the signed measure is the number; and the abscissa is the second, taken from the first.

So the definition that holds everywhere is this: a coordinate is one of the numbers in a tuple that, together, fix a position, and the axis label only says which slot of the tuple is meant. Whether the slot has an axis of its own varies from system to system:

| Coordinate system | The coordinates | Does each one lie on an axis? |
|---|---|---|
| Rectangular, in the plane or in space | x, y, and z | yes, one axis each |
| Polar | r and θ | no: r is a distance from the origin and θ is an angle |
| The complex plane | Re z and Im z | yes, two real coordinates with two axes; a complex number is a point with two real coordinates, not a point with one complex coordinate |
| ℂ², and the "coordinates may be complex numbers" of the encyclopedia | z₁ and z₂, each a complex number | no axis in the ordinary sense: each slot holds a whole complex number, so a point has two complex coordinates and four real ones |

One usage does need watching, because it is common enough to feel like the definition. In everyday speech and in software, "a coordinate" often means a whole location: a GPS coordinate, a `Coordinate` class holding a latitude and a longitude. Textbooks and Wikipedia do not use the word that way, though informal and machine-written glossaries sometimes hedge, "a number (or set of numbers)", which is the everyday sense leaking in. In the books, one coordinate is one number, one per axis, and the location is the *coordinates*, plural: the word was coined in the plural, *co-ordinatae*, the numbers "ordered together", and each of them is one of the co-ordinates. So (x, y) is two coordinates, a point on a line has one, and a point in space has three.

## Plotting

To plot (−3, 1): go 3 units along the x-axis to the left of O, then straight up 1 unit, and put a dot there. The instructions come in the order of the pair, first entry then second, and that order is the whole content of the word *ordered*: (−3, 1) is 3 left and 1 up, while (1, −3) is 1 right and 3 down, a different point in a different quadrant. Section 3 checks it, and [the Cartesian product](../../04_Sets/cartesian_product/README.md) is the page on why a pair remembers which entry is first.

Section 1 draws the book's figure as a grid of cells: the four points (−3, 1), (3, 2), (3, −2) and (−2, −3), the y-axis as a column of `|`, the x-axis as a row of `-`, and the origin as `O`.

The grid lines are a reading aid, not a rule. (−1.5, −2.5) is as much a point as (−2, −3), in quadrant III by the same two signs, and so is (√2, 1/3): the plane is every pair of real numbers, all of ℝ², and the integer points are the ones with a grid line through them. The checker below takes decimals and fractions and draws them at the nearest cell.

## One notation, three meanings

Larson ends his page with a warning worth its own card: (x, y) means a point in the plane, and (x, y) also means an open interval on the number line, every real number t with x < t < y. Two objects, one notation, and only the context says which. The point (2, 5) is an ordered pair, a member of ℝ²; the interval (2, 5) is a set of numbers, and 3 is in it. Section 9 of the program keeps them apart in the one way Python can: a tuple `(2, 5)` holds the numbers 2 and 5 and nothing else, so `3 in (2, 5)` is false, while the interval is the test `2 < t < 5`, which 3 passes. There is one sure sign: an interval (a, b) needs a < b, so (5, 2) can only be a point. Intervals are the tool of [what measure zero means](../../02_Measure_Zero/what_measure_zero_means/README.md), where every length is a length of intervals, and none of them is a point.

The third reading is a vector. The point (3, 1) is a location, one place in the plane. The vector (3, 1) is a displacement, three right and one up, and a displacement can start anywhere: drawn from (2, 3) it ends at (5, 4), drawn from (−3, −4) it ends at (0, −3), and it is the same vector each time, because a vector remembers the trip and not the starting point. Drawn from the origin O, its tip lands exactly on the point (3, 1), which is why the two share a notation and why linear algebra treats ℝ² as both at once: the vector from P = (2, 3) to Q = (5, 4) has components (5 − 2, 4 − 3), the coordinates of Q minus those of P. So a vector has no origin of its own, only an initial point, and O is special to it only as the starting point that makes tip and point coincide. [A definition is a test](../../06_Algebraic_Structures/a_definition_is_a_test/README.md) runs the vector-space axioms on exactly these pairs.

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

10. THE ARROW DECIDES WHICH WAY IS AROUND
   the quarter turn (x, y) -> (-y, x), applied three times from (3, 2):
     (3, 2) -> (-2, 3) -> (-3, -2) -> (2, -3),  quadrants I II III IV
   the four positions, numbered 1 to 4, with y positive UPWARD (the book):
     4   .  .  .  .  |  .  .  .  .
     3   .  .  2  .  |  .  .  .  .
     2   .  .  .  .  |  .  .  1  .
     1   .  .  .  .  |  .  .  .  .
     0   -  -  -  -  O  -  -  -  -
    -1   .  .  .  .  |  .  .  .  .
    -2   .  3  .  .  |  .  .  .  .
    -3   .  .  .  .  |  .  4  .  .
    -4   .  .  .  .  |  .  .  .  .
        -4 -3 -2 -1  0  1  2  3  4   x
   the same four points, same numbers, with y positive DOWNWARD (a computer screen):
    -4   .  .  .  .  |  .  .  .  .
    -3   .  .  .  .  |  .  4  .  .
    -2   .  3  .  .  |  .  .  .  .
    -1   .  .  .  .  |  .  .  .  .
     0   -  -  -  -  O  -  -  -  -
     1   .  .  .  .  |  .  .  .  .
     2   .  .  .  .  |  .  .  1  .
     3   .  .  2  .  |  .  .  .  .
     4   .  .  .  .  |  .  .  .  .
        -4 -3 -2 -1  0  1  2  3  4   x
   1 -> 2 -> 3 -> 4 runs counterclockwise in the first picture and clockwise in
   the second. Not one coordinate changed; only which way the y-axis points.
   The same flip turns the line through (0, 0) and (2, 2) from rising to falling.
   Which direction is positive is a choice, and the arrow records it.

11. A COORDINATE IS A NUMBER, NOT THE POINT ON THE AXIS BELOW IT
   P = (3, 5);  the foot of the perpendicular from P to the x-axis is F = (3, 0);
   the x-coordinate of P is the number the axis reads at F:  x = 3
     F == x                 is False      a point with two coordinates is not a number
     2 * x                  is 6          arithmetic works on the number
     2 * F                  is (3, 0, 3, 0)   what Python does when a point is treated as one
     y = 2x + 1 at P:  2 * 3 + 1 = 7   the equation takes the number, never the point
     F's own x-coordinate   is 3          P and its foot share it; that is the relationship
   Geometry to numbers and back: the foot is the geometry side, the
   coordinate is the number side, and the equations live on the number side.
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

**16. A vector is drawn from (2, 3) to (5, 4). What are its components, and where does it end if drawn from the origin instead?**

<details><summary>Answer</summary>

Its components are (5 − 2, 4 − 3) = (3, 1): three right and one up. Drawn from O it ends at the point (3, 1). Same vector, different starting point; the origin is only the starting point that makes the vector's tip and the point with the same numbers coincide.

</details>

**17. A screen puts the origin at the top left with y positive downward. Where on the screen is the book's quadrant I, and which way does a counterclockwise rotation formula turn there?**

<details><summary>Answer</summary>

Quadrant I, x > 0 and y > 0, is below and to the right of the origin, which is the visible screen; the book's picture has it above. A formula that turns counterclockwise with y upward turns clockwise on that screen, because the y-axis points the other way. Section 10 shows the same four points both ways.

</details>

**18. Why are the quadrants numbered counterclockwise rather than clockwise?**

<details><summary>Answer</summary>

Because an angle is measured from the positive x-axis toward the positive y-axis, and with x to the right and y upward that turn is counterclockwise. The first quarter turn, 0° to 90°, sweeps the region where both coordinates are positive, so it is quadrant I, and II, III and IV follow the turn. The rule is "from the first axis toward the second"; it is the axes, not the plane, that make it counterclockwise.

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

The same page as a deck of 73 Anki cards, one fact per card and one or two short sentences on the back, with the reasons left on this page: [`rectangular_coordinates.txt`](anki/rectangular_coordinates.txt). In Anki choose File → Import, pick the file, and the header lines inside it set the separator, the note type (Basic), the deck name and the tags, so nothing needs changing in the dialog. Each card carries a tag for its kind, `definition`, `quadrants`, `plotting` and so on, for studying one kind at a time.

## Where this goes next

The next page in every precalculus book is the distance between two points, which is Pythagoras written in coordinates, and after it the midpoint. Then the book's real subject: the graph of an equation in x and y is the set of all points whose coordinates pass the equation, so a line of solutions in [linear equations and their solutions](../../07_Linear_Systems/linear_equations/README.md) becomes a line on the page. The [roadmap](../../ROADMAP.md) lists all three.

## Po polsku, w skrócie

Dwie osie liczbowe, pozioma i pionowa, przecinają się pod kątem prostym w punkcie, który na obu odczytujemy jako 0. To cały aparat. Odtąd każdy punkt płaszczyzny jest jedną parą uporządkowaną liczb rzeczywistych (x, y), a każda para jest jednym punktem. Pierwsza liczba, x, to odległość punktu od osi y ze znakiem: na prawo dodatnia, na lewo ujemna. Druga, y, to odległość od osi x ze znakiem: w górę dodatnia, w dół ujemna. Pułapka: x mierzy się od osi *y*, bo mówi, jak daleko w prawo lub w lewo, a „w prawo lub w lewo" liczy się od linii pionowej. Każda z tych liczb to jedna współrzędna; para to współrzędne punktu, w liczbie mnogiej.

Ćwiartka to nic więcej niż para znaków. Pierwsza: x > 0 i y > 0; druga: x < 0 i y > 0; trzecia: obie ujemne; czwarta: x > 0 i y < 0. Wielkość liczb nie ma znaczenia: (1, 1) i (1000, 5) leżą w tej samej ćwiartce. Punkty na osiach nie należą do żadnej ćwiartki, bo zero nie ma znaku; gdyby definicja używała ≥ zamiast >, początek układu leżałby we wszystkich czterech naraz. Ćwiartki numeruje się przeciwnie do ruchu wskazówek zegara, bo w tę stronę biegnie kąt od dodatniej osi x ku dodatniej osi y. Ta jedna umowa decyduje o znaku kątów, nachyleń i obrotów: ekran komputera odwraca oś y i ten sam wzór na obrót kręci w drugą stronę.

Programy na tej stronie sprawdzają każde z tych twierdzeń na konkretnych punktach, a `plot_points.py` rysuje dowolne punkty i podaje dla każdego ćwiartkę albo oś, więc można nim sprawdzić własny rysunek.

## See also

- [The Cartesian product](../../04_Sets/cartesian_product/README.md) — ℝ² as a set of pairs, and why (2, 5) is not (5, 2)
- [Multiplication as pairs](../../03_Complex_Numbers/multiplication_as_pairs/README.md) — a complex number is a point (x, y) of this plane
- [Multiplication rotates](../../03_Complex_Numbers/multiplication_rotates/README.md) — multiplying by i is the quarter turn of section 8, one quadrant on
- [Linear equations and their solutions](../../07_Linear_Systems/linear_equations/README.md) — one equation in x and y has a whole line of solutions, and those solutions are points here
- [A definition is a test](../../06_Algebraic_Structures/a_definition_is_a_test/README.md) — the same pairs read as vectors, and the axioms they pass
- [Mean, average, arithmetic mean](../../05_Statistics/mean_vs_average/README.md) — the two means that a scatter plot's quadrants are drawn from
- [Precalculus: a reading guide](../../reading_guides/precalculus/README.md) — where this sits in the course, and which book to read it in
- [Cartesian coordinate system ↗](https://en.wikipedia.org/wiki/Cartesian_coordinate_system) — Wikipedia, with the history and the higher-dimensional version
- [Coordinate system ↗](https://en.wikipedia.org/wiki/Coordinate_system) — Wikipedia; its number-line paragraph is the one-dimensional case quoted above, and the rest is the polar and higher-dimensional systems this page only names
- Michael Sullivan, *Precalculus* (Pearson), the section "Rectangular Coordinates" that opens the chapter on graphs; this page follows it
- Ron Larson, *Precalculus* (Cengage), section 1.1, the same page with *directed distance* for signed distance and the warning about (x, y) as an interval
