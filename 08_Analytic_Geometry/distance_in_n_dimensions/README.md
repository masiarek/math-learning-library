# Distance in n dimensions, and the length of a vector

**Level:** 101 → 201 · for anyone who has the distance formula in the plane and wonders what happens with a third coordinate, or why √(v·v) is called a length

**One line:** In space the distance formula is Pythagoras twice, the floor diagonal then the box diagonal, and with n axes it is Pythagoras n − 1 times, one square per axis; the length of a vector is that distance measured from the origin, which is why √(v·v) is a length and not a definition pulled from the air.

## Pythagoras twice

A box 3 by 4 by 12. How long is its diagonal, corner to opposite corner? Two right triangles. The first lies in the floor: legs 3 and 4, so the floor diagonal is f = √(9 + 16) = 5. The second stands up: one leg is that floor diagonal, the other is the vertical edge 12, and the angle between them is right because the vertical edge is perpendicular to every line in the floor. So d² = f² + 12² = 25 + 144 = 169 and d = 13. Substitute f² and the two steps collapse into one formula:

> **d² = 3² + 4² + 12²**

For two points P₁ = (x₁, y₁, z₁) and P₂ = (x₂, y₂, z₂), the box has edges |x₂ − x₁|, |y₂ − y₁|, |z₂ − z₁|, and the same two triangles give

> **d(P₁, P₂) = √((x₂ − x₁)² + (y₂ − y₁)² + (z₂ − z₁)²)**

This is the proof of [the distance formula](../distance_formula/README.md) with one more line, and it costs one more given: that the z-axis is perpendicular to both the x-axis and the y-axis, which is what makes the second angle right. The lemma |t|² = t² removes the bars as before, and the no-box cases (two points sharing a coordinate) reduce to the plane formula, which is already proved.

## Two ways to write a point

The formula below changes spelling, and the change is worth a paragraph because every book makes it without saying so. Sullivan writes two points as (x₁, y₁) and (x₂, y₂): the letter names the axis and the subscript numbers the point, so x₂ is "the x of the second point". Wikipedia and every linear algebra book write them as p = (p₁, p₂) and q = (q₁, q₂): the letter names the point and the subscript numbers the axis, so q₁ is "the first coordinate of q". The key between them:

| Sullivan | Wikipedia | Meaning |
|---|---|---|
| x₁ | p₁ | first point, first axis |
| y₁ | p₂ | first point, second axis |
| x₂ | q₁ | second point, first axis |
| y₂ | q₂ | second point, second axis |

The trap is the 2: it means "second point" in one convention and "second axis" in the other, so Sullivan's x₂ is Wikipedia's q₁ and not q₂. The second convention is the one that scales. Letters for axes run out after x, y, z; subscripts for axes go on forever, and a point in n dimensions is p = (p₁, …, pₙ) with nothing new to invent. A bold or arrowed letter, 𝐩 or p⃗, says "this is a whole point or vector, not a number", for the same reason linear algebra writes v for a vector and v₁ for its first entry. Sullivan's convention is the one that reads aloud in a plane, where the figure shows an x and a y, and this library keeps it in the plane and switches here, where the axes are numbered because they have to be.

## One square per axis

Nothing in the argument used that three is three. With n coordinates, the distance between two points is the square root of the sum of n squared differences:

> **d(P, Q) = √((q₁ − p₁)² + (q₂ − p₂)² + ⋯ + (qₙ − pₙ)²)**

The proof is by [induction](../../11_Logic/induction/README.md) on n: the formula in n dimensions is the formula in n − 1 dimensions, applied in the "floor" spanned by the first n − 1 axes, plus Pythagoras once more with the n-th axis as the vertical edge. Section 3 of the program shows the same two points seen in one, two, three, four and five dimensions, and each extra axis adds exactly one square. Nobody can draw the fourth axis, and nobody needs to: the formula is a sum, and a sum does not care how many terms it has.

## The length of a vector

A vector v = (v₁, …, vₙ) is drawn as an arrow from the origin to the point (v₁, …, vₙ). Its length |v| is therefore the distance from the origin to that point, which by the formula is √(v₁² + ⋯ + vₙ²). The dot product of v with itself, v·v = v₁v₁ + ⋯ + vₙvₙ, is exactly that sum of squares, so

> **|v| = √(v·v)**

That line appears in every linear algebra book as a definition. It is a definition there, of the *Euclidean norm*, and the reason it deserves the name "length" is the distance formula: the number it defines is the geometric distance from 0 to the arrow's tip. The distance between two points is the length of the vector from one to the other, d(u, w) = |w − u|, because the differences of coordinates are the coordinates of the difference. The AI-written list of "proofs" sorted in [what a proof is](../../11_Logic/what_a_proof_is/README.md) offered √((v₂ − v₁)·(v₂ − v₁)) as a proof of the distance formula; it is the formula written in vector notation, and this page is the direction the dependence runs.

## What a distance must do

Four properties, called the axioms of a *metric*, which any function worth calling a distance has to satisfy, and the Euclidean formula does:

| Property | Says | Why the formula has it |
|---|---|---|
| non-negative | d(P, Q) ≥ 0 | a sum of squares is never negative, and √ is the non-negative root |
| zero only for one point | d(P, Q) = 0 exactly when P = Q | a sum of squares is 0 only when every square is 0, so every coordinate agrees |
| symmetric | d(P, Q) = d(Q, P) | squaring forgets the sign of each difference |
| [triangle inequality](../../GLOSSARY.md#triangle-inequality) | d(P, R) ≤ d(P, Q) + d(Q, R) | the one with a real proof behind it, the Cauchy–Schwarz inequality, which this page does not give |

Section 5 of the program checks all four on every pair, and the fourth on 91 125 triples, of a grid in three dimensions, exactly, with the root never taken: the triangle inequality on squared distances is c² ≤ a² + b² + 2ab, and the cross term is compared by squaring once more. The first three checks are the proofs, run on numbers; the fourth is a check and not a proof, and the page says so.

## What the program prints

<!-- output:distance_in_n_dimensions -->
*Verified output of [`distance_in_n_dimensions.py`](examples/distance_in_n_dimensions.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. A BOX 3 BY 4 BY 12: PYTHAGORAS TWICE
   Floor diagonal: a right triangle with legs 3 and 4, so f^2 = 3^2 + 4^2 = 25, f = 5.
   Box diagonal: a right triangle with legs f = 5 and the height 12,
   so d^2 = f^2 + 12^2 = 25 + 144 = 169, d = 13.
   Substituting f^2: d^2 = 3^2 + 4^2 + 12^2. Each axis adds one square.
   The second right angle is between the floor diagonal and the vertical edge,
   which is perpendicular to everything in the floor: that is what the z-axis being
   perpendicular to the x- and y-axes buys.

2. TWO POINTS IN SPACE, THE SAME FORMULA WITH THREE DIFFERENCES
   P1 = (1, 3, 2), P2 = (5, 6, 14): differences [4, 3, 12], squares [16, 9, 144],
   d^2 = 169, d = 13.
   Swapped: d(P2, P1)^2 = 169. Order does not matter, for the same reason as in the plane.

3. ONE SQUARE PER AXIS: THE SAME TWO POINTS SEEN IN 1, 2, 3, 4, 5 DIMENSIONS
   n = 1: d^2 = 16                     =   16, d = 4
   n = 2: d^2 = 16 + 9                 =   25, d = 5
   n = 3: d^2 = 16 + 9 + 144           =  169, d = 13
   n = 4: d^2 = 16 + 9 + 144 + 4       =  173, d = sqrt(173) = 13.1529
   n = 5: d^2 = 16 + 9 + 144 + 4 + 9   =  182, d = sqrt(182) = 13.4907
   Dropping to n - 1 dimensions drops one square; adding an axis adds one. That is the
   induction: the n-dimensional formula is the (n - 1)-dimensional one plus Pythagoras once more.

4. THE LENGTH OF A VECTOR IS THE DISTANCE FROM THE ORIGIN
   v = (3, 4)           v . v = 25     |v| = sqrt(v . v) = 5                  d(0, v)^2 = 25
   v = (1, 1)           v . v = 2      |v| = sqrt(v . v) = sqrt(2) = 1.4142   d(0, v)^2 = 2
   v = (3, 4, 12)       v . v = 169    |v| = sqrt(v . v) = 13                 d(0, v)^2 = 169
   v = (1, 1, 1, 1)     v . v = 4      |v| = sqrt(v . v) = 2                  d(0, v)^2 = 4
   v = (1/2, 1/2)       v . v = 1/2    |v| = sqrt(v . v) = sqrt(1/2) = 0.7071 d(0, v)^2 = 1/2
   v . v is the sum of the squares of the coordinates, which is d(0, v)^2 by the formula.
   So sqrt(v . v) is a length because the distance formula says so, not by decree.
   And the distance between two points is the length of their difference: w - u = (4, 3, 12),
   |w - u|^2 = 169 = d(u, w)^2 = 169.

5. THE FOUR PROPERTIES OF A DISTANCE, CHECKED ON A GRID IN 3 DIMENSIONS
   Points: every (x, y, z) with coordinates in -2..2, 125 of them.
   d(P, Q) >= 0 for all pairs:                   True
   d(P, Q) = 0 exactly when P = Q:               True
   d(P, Q) = d(Q, P):                            True
   d(P, R) <= d(P, Q) + d(Q, R) on 27x125x27 triples: True
   The first three follow from the formula in a line each: squares are never negative,
   a sum of squares is 0 only when every square is, and squaring forgets the sign.
   The fourth is the one with a real proof behind it (the Cauchy-Schwarz inequality),
   which this page checks and does not prove.
```
<!-- /output -->

## Questions

**1. How far is (1, 2, 3) from the origin? From (4, 6, 15)?**

<details><summary>Answer</summary>

√(1 + 4 + 9) = √14 ≈ 3.74. And √(9 + 16 + 144) = √169 = 13: the differences are 3, 4, 12, the box of section 1.

</details>

**2. Where, exactly, does the three-dimensional formula use that the z-axis is perpendicular to the floor?**

<details><summary>Answer</summary>

In the second right triangle, whose legs are the floor diagonal and the vertical edge. The angle between them is right only because the vertical edge is perpendicular to every line in the floor, the floor diagonal included. Without it, Pythagoras does not apply the second time and the formula fails, the same way the plane formula fails on skewed axes.

</details>

**3. Why is √(v·v) a length and not just a number someone decided to call one?**

<details><summary>Answer</summary>

Because v·v = v₁² + ⋯ + vₙ² is the squared distance from the origin to the point (v₁, …, vₙ), by the distance formula. The norm is defined as √(v·v) in the algebra, and the geometry is what makes the definition deserve the word.

</details>

**4. Is "the distance formula follows from |v| = √(v·v)" a proof?**

<details><summary>Answer</summary>

No. It runs the dependence backwards: √(v·v) is a length because of the distance formula, not the other way round. Written as a proof of the formula it assumes its conclusion in vector notation.

</details>

**5. Which of the four metric properties is not proved on this page?**

<details><summary>Answer</summary>

The triangle inequality. The program checks it on a grid, which is evidence; the proof goes through the Cauchy–Schwarz inequality, (u·w)² ≤ (u·u)(w·w), and is not given here.

</details>

**6. Two points in four dimensions share their last coordinate. What does the formula reduce to?**

<details><summary>Answer</summary>

The three-dimensional formula: the fourth square is 0² and drops out. Sharing a coordinate removes one axis, exactly as the plane formula reduces to |x₂ − x₁| for two points on one horizontal line.

</details>

**7. Nobody can picture a fourth perpendicular axis. Why is the formula still justified for n = 4?**

<details><summary>Answer</summary>

Because the justification is not the picture but the induction: the n-dimensional formula is the (n − 1)-dimensional one plus Pythagoras once more, and that step is algebra on a sum of squares, which has no idea how many terms it holds. The picture stops at three; the proof does not.

</details>

## How to practise

1. **Draw the box.** For three dimensions, write the two right triangles before using the formula, once. After that, add the squares.
2. **Find the vector first.** For two points, write w − u, then take its length; the subtraction is where sign mistakes happen, the squares erase them.
3. **Squared distances to compare, roots to report**, as in the plane. The metric properties are all statements about sums of squares.

## Flashcards

The page as a deck of Anki cards: [`distance_in_n_dimensions.txt`](anki/distance_in_n_dimensions.txt). Import with File → Import. Tags: `formula`, `why`, `trap`.

## Where this goes next

[Distance is the four properties](../other_distances/README.md) turns the table above around: the four properties are the definition of a distance, the formula is one function that has them, and taxicab, Chebyshev and Hamming distances are others. The dot product in general, u·w = |u||w| cos θ, and the Cauchy–Schwarz inequality behind the triangle inequality, belong to linear algebra; the [reading guide](../../reading_guides/linear_algebra/README.md) says which book to learn them from. Back in the plane, [circles](../circles/README.md) is the distance formula held fixed, and in three dimensions the same equation with a third square is a sphere.

## Po polsku, w skrócie

W przestrzeni wzór na odległość to Pitagoras dwa razy: najpierw przekątna podłogi pudełka, potem przekątna samego pudełka, w trójkącie prostokątnym, którego jedną przyprostokątną jest przekątna podłogi, a drugą pionowa krawędź. Kąt jest prosty, bo pionowa krawędź jest prostopadła do wszystkiego, co leży w podłodze; to jedyne nowe założenie. Po podstawieniu dwa kroki zwijają się w jeden wzór: d² = Δx² + Δy² + Δz². Dla n współrzędnych jest tak samo, przez indukcję: wzór w n wymiarach to wzór w n − 1 wymiarach plus Pitagoras jeszcze raz, więc każda oś dodaje jeden kwadrat. Program pokazuje te same dwa punkty widziane w jednym, dwóch, trzech, czterech i pięciu wymiarach.

Długość wektora to odległość od początku układu do jego końca, więc |v| = √(v·v): iloczyn skalarny wektora z samym sobą to suma kwadratów współrzędnych, czyli kwadrat odległości. W algebrze liniowej to definicja normy; geometria tłumaczy, dlaczego zasługuje na słowo „długość". Odległość między punktami to długość wektora różnicy.

Odległość musi spełniać cztery warunki: jest nieujemna, zerowa tylko dla jednego punktu, symetryczna i spełnia nierówność trójkąta. Trzy pierwsze wynikają ze wzoru w jednej linii każdy; czwarty ma prawdziwy dowód (nierówność Cauchy'ego–Schwarza), którego ta strona nie podaje. Program sprawdza wszystkie cztery na siatce punktów, dokładnie, bez pierwiastków.

## See also

- [The distance formula](../distance_formula/README.md) — the plane case this page extends, and its cross-reference table
- [The Pythagorean theorem and its converse](../../10_Geometry/pythagorean_theorem/README.md) — used twice here
- [What a proof is](../../11_Logic/what_a_proof_is/README.md) — the plane proof as a chain, and the vector "proof" sorted
- [Induction](../../11_Logic/induction/README.md) — the step from n − 1 axes to n
- [Linear algebra: a reading guide](../../reading_guides/linear_algebra/README.md) — where the dot product and the norm are learned properly
- [Multiplication rotates](../../03_Complex_Numbers/multiplication_rotates/README.md) — the length of a complex number, the n = 2 case of the norm
- [Euclidean distance ↗](https://en.wikipedia.org/wiki/Euclidean_distance) — Wikipedia, with the formula in any number of dimensions
