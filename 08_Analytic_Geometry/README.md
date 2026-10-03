# 08_Analytic_Geometry — what does it mean to draw a number?

**Level:** 101 · for anyone starting precalculus, or anyone who has ever plotted a point

Descartes' idea, and the first section of every precalculus book: two number lines at right angles turn every point of the plane into a pair of numbers and every pair of numbers into a point. After that a question about a picture is a question about arithmetic, and a question about an equation has a picture. This chapter follows that idea in the order the books take it, one page of the book at a time, with the book's own questions at the end of each lesson and a deck of flashcards beside it.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [Rectangular coordinates](rectangular_coordinates/README.md) | What do the two numbers of a point measure, what is a quadrant, and why is the word worth having? |
| 2 | [The distance formula](distance_formula/README.md) | How far apart are two points, and why does the formula not care which one comes first? |
| 3 | [The midpoint formula](midpoint_formula/README.md) | Which point is halfway, and why is "equally far from both ends" not enough to say so? |
| 4 | [Graphs of equations: intercepts and symmetry](graphs_intercepts_symmetry/README.md) | What is the graph of an equation, and how do intercepts and symmetry follow from that definition? |
| 5 | [Lines: slope, equations, parallel and perpendicular](lines_and_slope/README.md) | Why does a line have one slope, and why do perpendicular slopes multiply to −1? |
| 6 | [Circles: standard form and general form](circles/README.md) | Why is a circle's equation the distance formula, and when is x² + y² + ax + by + c = 0 not a circle? |
| 7 | [Distance in n dimensions, and the length of a vector](distance_in_n_dimensions/README.md) | What happens to the distance formula with a third coordinate, and why is √(v·v) a length? |
| 8 | [Distance is the four properties](other_distances/README.md) | What else counts as a distance, what shape is its circle, and why did geometry pick Pythagoras? |

## The through-line

Lesson 1 sets up the plane. A point is two signed distances, x from the y-axis and y from the x-axis, so [the Cartesian product](../04_Sets/cartesian_product/README.md) ℝ² is not just a set of pairs but the plane itself. A quadrant is the pair of signs and nothing more, which is why the axes belong to none and why the word carries so far: the sign of a trigonometric function, the quarter turn that [multiplying by i](../03_Complex_Numbers/multiplication_rotates/README.md) performs, and the symmetry of a graph are all statements about quadrants.

Lesson 2 measures in it. The distance between two points is the hypotenuse of a right triangle whose legs are the differences of their coordinates, so the formula is [the Pythagorean theorem](../10_Geometry/pythagorean_theorem/README.md), and the squares in it erase the signs that lesson 1 took such care over: distance has no direction.

Lesson 3 finds the point halfway, one [average](../05_Statistics/mean_vs_average/README.md) per coordinate, and uses the distance formula to check both halves of "halfway". Lesson 4 turns an equation into a picture: its graph is the set of points that pass it, the same object as the solution set of [a linear equation](../07_Linear_Systems/linear_equations/README.md), and intercepts and symmetry are that definition applied. Lessons 5 and 6 are the two families of graphs the chapter ends with. A line has one slope because [similar triangles](../10_Geometry/congruent_and_similar_triangles/README.md) share their ratios, and a circle's equation is the distance formula held fixed. That is the whole of the first chapter of Sullivan's *Precalculus*; the book's next chapter is functions.

## All the flashcards in one file

[`precalculus_chapter_1_anki.txt`](precalculus_chapter_1_anki.txt) holds every card of this chapter and of the geometry it assumes, [10_Geometry](../10_Geometry/README.md): 370 cards in nine decks, one per lesson. In Anki choose File → Import, pick the file, and click Import; the header lines put each card in its lesson's deck, under *Math*, with its tags. On a phone or a machine without a clone, download it from [this link ↗](https://raw.githubusercontent.com/masiarek/math-learning-library/master/08_Analytic_Geometry/precalculus_chapter_1_anki.txt) with the browser's "Save as".

## Where this is taught

The opening section of the chapter on graphs in any precalculus book; the lessons here follow Michael Sullivan's *Precalculus*, but Stewart, Larson, Blitzer and the free Stitz and Zeager cover the same page in the same order. For which book to read, see [Precalculus: a reading guide](../reading_guides/precalculus/README.md).

## Po polsku, w skrócie

Pomysł Kartezjusza: dwie osie liczbowe pod kątem prostym zamieniają każdy punkt płaszczyzny w parę liczb, a każdą parę liczb w punkt. Od tej chwili pytanie o rysunek jest pytaniem o arytmetykę, a równanie ma swój obraz. Potem odległość i środek odcinka, wykres równania jako zbiór punktów, które je spełniają, prosta i jej nachylenie, okrąg jako wzór na odległość ze stałym r. Rozdział idzie w kolejności podręcznika do precalculusu, strona po stronie, z pytaniami z książki na końcu każdej lekcji i talią fiszek Anki obok.

## A note on the code

Every point is a Python tuple of integers, so "is in quadrant II" is a check on two signs and every count is exact. Nothing is drawn: the one picture in the chapter is a grid of text cells, which is enough to see where four points land.
