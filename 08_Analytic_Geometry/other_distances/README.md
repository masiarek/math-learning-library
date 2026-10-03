# Distance is the four properties: taxicab, Chebyshev, Hamming, and the one that fails

**Level:** 201 · for anyone who has the distance formula and asks what else could count as a distance, and why Pythagoras is the one geometry picked

**One line:** What makes a function a distance is four properties, not a formula: never negative, zero only between a point and itself, the same both ways, and no detour shorter than the straight route; the Euclidean formula is one function with them, the taxicab and Chebyshev distances are others with square and diamond "circles", the Hamming distance has them on strings with no coordinates at all, and the formula with p = ½ looks like one of the family and is not, because one triple of points breaks the fourth property.

## Four numbers for one pair of points

From (1, 3) to (5, 6) is 4 across and 3 up. The [distance formula](../distance_formula/README.md) says 5. But a taxi in a city grid cannot cut the corner and drives 4 + 3 = 7. A chess king, which moves one square in any of eight directions, needs max(4, 3) = 4 moves. And the expression (√4 + √3)², built like the Euclidean formula with square roots in place of squares, gives about 13.9. Four numbers, one pair of points, and the question this page answers: which of them deserve the word *distance*?

The answer mathematics settled on is that a distance is anything with four properties, called the axioms of a **metric**, and [the page on n dimensions](../distance_in_n_dimensions/README.md) already met them for the Euclidean formula:

| Property | Says | In words |
|---|---|---|
| non-negative | d(P, Q) ≥ 0 | no negative lengths |
| zero only for one point | d(P, Q) = 0 exactly when P = Q | distinct points are apart |
| symmetric | d(P, Q) = d(Q, P) | the same both ways |
| triangle inequality | d(P, R) ≤ d(P, Q) + d(Q, R) | no detour is shorter than the straight route |

A function with the four is a distance; without any one of them it is not, however much it looks like one. The formula is replaceable; the properties are the definition. That is the whole page, and the rest is evidence.

## Three distances and their circles

**Taxicab** distance, |x₂ − x₁| + |y₂ − y₁|, is the Euclidean formula with the squares and the root taken away: the legs of the right triangle added instead of combined by Pythagoras. **Chebyshev** distance, max(|x₂ − x₁|, |y₂ − y₁|), keeps only the longer leg. Both have the four properties, which section 5 of the program checks on every pair and every triple of a grid of points, and each is a case of the same family, (|Δx|ᵖ + |Δy|ᵖ)^(1/p): p = 1 is taxicab, p = 2 is Euclidean, and letting p grow without bound gives Chebyshev, because the largest term takes over.

A circle is the set of points at one distance from a centre, and the [circle](../circles/README.md) you know is the Euclidean one. Change the distance and the circle changes shape, as section 2 draws on lattice points: a disc for Euclidean, a diamond for taxicab, a square for Chebyshev. The shape of a circle is a fact about the distance, not about the plane.

## The one that fails

Take p = ½ in the family: d = (√|Δx| + √|Δy|)². It is non-negative, zero only for a point and itself, and symmetric, three properties out of four. Section 3 finds the triple that breaks the fourth: P = (0, 0), Q = (1, 0), R = (1, 1). Straight from P to R costs (1 + 1)² = 4; through Q it costs 1 + 1 = 2. The detour is shorter, so this is not a distance, and one triple settles it, the way [one counterexample](../../11_Logic/converse_and_contrapositive/README.md#examples-prove-nothing-one-counterexample-disproves) settles any universal claim. Every p ≥ 1 gives a metric and every p < 1 fails this way; the proof for p ≥ 1 is Minkowski's inequality, which this page uses and does not prove.

The same section makes a second point in passing: the *squared* Euclidean distance also fails the triangle inequality, since 0, 1, 2 on a line give 4 > 1 + 1. The square root in the distance formula is not decoration. The plane and n-dimensional pages compared squared distances freely, which is fine for "which is closer"; it is the root that makes the triangle inequality true.

## Why geometry chose Pythagoras

If three functions are all distances, why does every geometry book use the Euclidean one? Section 4 gives the reason in one experiment: rotate the plane and measure again. The rotation uses cos θ = 3/5 and sin θ = 4/5, a [3-4-5 triangle](../../10_Geometry/pythagorean_theorem/README.md), so every coordinate stays an exact fraction. The Euclidean distance between two points comes out the same before and after; the taxicab and Chebyshev distances both change. A ruler does not care which way it is held, and among the three only the Euclidean distance passes that test. The deeper fact, not proved here, is that it is the *only* distance of the whole p-family that does: Pythagoras is the one choice under which turning the paper changes nothing.

## A distance with no coordinates

The **Hamming** distance between two strings of the same length is the number of positions where they differ: d(011, 110) = 2. No coordinates, no plane, no Pythagoras. Section 5 checks the four properties on all eight strings of three bits, every pair and every triple, 512 of them, and they all hold. So it is a distance, in exactly the sense the Euclidean one is, and it is the distance that error-correcting codes are built on: a code that keeps every two codewords at Hamming distance 3 or more can repair any single flipped bit, because the damaged word is still closer to its original than to any other codeword. That sentence only means something because the triangle inequality holds.

## What the program prints

<!-- output:other_distances -->
*Verified output of [`other_distances.py`](examples/other_distances.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. ONE PAIR OF POINTS, MEASURED FOUR WAYS
   P = (1, 3), Q = (5, 6): the changes are 4 across and 3 up.
   Euclidean  sqrt(dx^2 + dy^2)   = sqrt(25) = 5      the straight line
   taxicab    |dx| + |dy|          = 7              along the streets of a grid
   Chebyshev  max(|dx|, |dy|)      = 4              moves of a chess king
   p = 1/2    (sqrt|dx| + sqrt|dy|)^2 = (2 + sqrt 3)^2 = 13.93    a formula of the same family
   Four numbers, one pair of points. Which of them deserve the word distance?

2. THE CIRCLE OF RADIUS 3 AROUND THE ORIGIN, UNDER EACH DISTANCE
   Lattice points (x, y) with -4 <= x, y <= 4; # marks a point at distance at most 3.
   Euclidean     taxicab       Chebyshev
   .........     .........     .........
   ....#....     ....#....     .#######.
   ..#####..     ...###...     .#######.
   ..#####..     ..#####..     .#######.
   .#######.     .#######.     .#######.
   ..#####..     ..#####..     .#######.
   ..#####..     ...###...     .#######.
   ....#....     ....#....     .#######.
   .........     .........     .........
   Points inside: 29, 25, 49. A disc, a diamond, a square: the shape of
   a circle is a fact about the distance, not about the plane.

3. THE ONE THAT FAILS: p = 1/2 BREAKS THE TRIANGLE INEQUALITY
   P = (0, 0), Q = (1, 0), R = (1, 1).
   d(P, Q) = (sqrt 1)^2 = 1,  d(Q, R) = (sqrt 1)^2 = 1,  d(P, R) = (sqrt 1 + sqrt 1)^2 = 4.
   Going straight from P to R costs 4; going through Q costs 2. The detour is shorter.
   One triple is enough: the formula is not a distance. The other three properties hold
   and do not save it. (Every p >= 1 gives a distance; every p < 1 fails this way.)

4. TURN THE PLANE: ONLY THE EUCLIDEAN DISTANCE DOES NOT NOTICE
   Rotate by the angle with cos = 3/5, sin = 4/5 (exact), and measure the same two points.
   Before: (1, 0) and (5, 3)
   After:  (3/5, 4/5) and (3/5, 29/5)
   Euclidean^2  before 25     after 25       unchanged
   taxicab      before 7      after 5        changed
   Chebyshev    before 4      after 5        changed
   A ruler does not care which way it is held. Among the three, only the Euclidean
   distance passes that test, which is why geometry chooses Pythagoras.

5. THE FOUR PROPERTIES, CHECKED EXHAUSTIVELY
   On the 25 lattice points with coordinates in -2..2 (15625 triples):
   squared Euclidean  non-negative: True   zero only for one point: True   symmetric: True   triangle inequality: False
   taxicab            non-negative: True   zero only for one point: True   symmetric: True   triangle inequality: True
   Chebyshev          non-negative: True   zero only for one point: True   symmetric: True   triangle inequality: True
   (Squared Euclidean distance fails the triangle inequality: 0-1-2 on a line gives 4 > 1 + 1.
    The root is not decoration; the plane page checked the inequality with the root in place.)
   Hamming distance on the 8 strings of three bits (512 triples):
   non-negative: True   zero only for one point: True   symmetric: True   triangle inequality: True
   d(011, 110) = 2: the number of positions that differ. No coordinates, no Pythagoras,
   and still a distance, because the four properties are the definition.
```
<!-- /output -->

## Questions

**1. Taxicab distance from (1, 3) to (5, 6), and from (5, 6) to (1, 3)?**

<details><summary>Answer</summary>

7 both ways: |5 − 1| + |6 − 3| = 4 + 3. The absolute values make it symmetric, the way the squares do for the Euclidean formula.

</details>

**2. Draw, or describe, the set of points at taxicab distance exactly 3 from the origin.**

<details><summary>Answer</summary>

A diamond with corners (3, 0), (0, 3), (−3, 0), (0, −3): the four segments where |x| + |y| = 3. Section 2 shows its lattice points. Under the Chebyshev distance the same set is a square with corners (±3, ±3).

</details>

**3. Which of the four properties does (√|Δx| + √|Δy|)² fail, and how many points does it take to show it?**

<details><summary>Answer</summary>

The triangle inequality, and three points: (0, 0), (1, 0), (1, 1). Straight costs 4, the detour costs 2. One triple is a proof that the formula is not a metric, because the property is a claim about every triple.

</details>

**4. The squared Euclidean distance is non-negative, zero only for a point and itself, and symmetric. Is it a distance?**

<details><summary>Answer</summary>

No. On a line, the points 0, 1, 2 give d(0, 2) = 4 and d(0, 1) + d(1, 2) = 2. Three properties out of four is not a distance. The square root is what makes the fourth hold.

</details>

**5. Why do geometry books use the Euclidean distance and not the taxicab one, if both are metrics?**

<details><summary>Answer</summary>

Because only the Euclidean distance is unchanged by rotation. Section 4 rotates two points by the 3-4-5 angle: the Euclidean distance stays 5, the taxicab distance goes from 7 to 5 and the Chebyshev from 4 to 5. A geometry in which turning the paper changes lengths is a geometry of the grid, not of the plane.

</details>

**6. How is the Hamming distance a distance when there are no coordinates to subtract?**

<details><summary>Answer</summary>

Because a distance is the four properties, and counting differing positions has them: never negative, zero only for identical strings, the same in either order, and changing s into u position by position through t never needs fewer changes than going straight. The program checks all 512 triples of 3-bit strings.

</details>

**7. A code keeps every two codewords at Hamming distance at least 3. Why can it correct one flipped bit?**

<details><summary>Answer</summary>

A received word with one flipped bit is at distance 1 from its original. Any other codeword is at distance at least 3 from the original, so by the triangle inequality at least 3 − 1 = 2 from the received word. The original is the unique nearest codeword, and the decoder picks it.

</details>

**8. In the family (|Δx|ᵖ + |Δy|ᵖ)^(1/p), which p are distances?**

<details><summary>Answer</summary>

Every p ≥ 1, including the limit p → ∞, which is the Chebyshev distance. For p < 1 the triangle inequality fails, as p = ½ shows. The proof that p ≥ 1 works is Minkowski's inequality, which this page cites and does not prove.

</details>

## How to practise

1. **Test, then name.** Given a candidate distance, check the four properties before using the word; the triangle inequality is the one that fails, so try it first with three points on a line and three at a corner.
2. **Draw its circle.** The set of points at distance 1 from the origin tells you more about a metric than its formula does.
3. **Rotate.** If a quantity changes when the axes turn, it is a fact about the grid, not the plane.

## Flashcards

The page as a deck of Anki cards: [`other_distances.txt`](anki/other_distances.txt). Import with File → Import. Tags: `what`, `why`, `trap`, `problems`.

## Where this goes next

A set with a distance on it is a *metric space*, the setting of analysis: limits, continuity and completeness are all defined from d(P, Q) alone, which is why the four properties matter more than any formula. The Euclidean choice leads to inner products and the Cauchy–Schwarz inequality, in the [linear algebra reading guide](../../reading_guides/linear_algebra/README.md); the Hamming choice leads to coding theory. And the question "what does a distance look like when the surface is curved?" is where the Euclidean formula survives only in the small, as ds² = dx² + dy², the start of differential geometry.

## Po polsku, w skrócie

Odległością jest każda funkcja o czterech własnościach: nieujemna, zerowa tylko między punktem a nim samym, symetryczna i spełniająca nierówność trójkąta, czyli: żaden objazd nie jest krótszy od drogi prostej. Wzór euklidesowy to jedna taka funkcja. Odległość taksówkowa, |Δx| + |Δy|, i odległość Czebyszewa, max(|Δx|, |Δy|), to inne, i każda ma swój „okrąg": koło, romb, kwadrat. Kształt okręgu jest faktem o odległości, nie o płaszczyźnie.

Wzór (√|Δx| + √|Δy|)² wygląda jak członek tej samej rodziny i odległością nie jest: dla punktów (0, 0), (1, 0), (1, 1) droga prosta kosztuje 4, a objazd 2. Jedna trójka punktów wystarczy, bo nierówność trójkąta jest twierdzeniem o wszystkich trójkach. Z tego samego powodu kwadrat odległości euklidesowej nie jest odległością: pierwiastek we wzorze nie jest ozdobą.

Dlaczego geometria wybrała Pitagorasa? Bo po obrocie płaszczyzny tylko odległość euklidesowa się nie zmienia; program obraca punkty o kąt z trójkąta 3-4-5, dokładnie, i taksówkowa oraz Czebyszewa zmieniają wartość. Linijka nie dba o to, jak ją trzymamy. Na koniec odległość Hamminga między ciągami bitów, liczba pozycji, na których się różnią: bez współrzędnych i bez Pitagorasa, a program sprawdza wszystkie cztery własności na wszystkich 512 trójkach ciągów trzybitowych. To na niej opierają się kody korekcyjne.

## See also

- [The distance formula](../distance_formula/README.md) — the Euclidean member of the family, and its cross-reference table
- [Distance in n dimensions, and the length of a vector](../distance_in_n_dimensions/README.md) — where the four properties were first checked
- [Circles: standard form and general form](../circles/README.md) — the Euclidean circle, one of the three drawn here
- [If A then B: converse, contrapositive and inverse](../../11_Logic/converse_and_contrapositive/README.md) — why one triple of points disproves a metric
- [The Pythagorean theorem and its converse](../../10_Geometry/pythagorean_theorem/README.md) — the 3-4-5 triangle that makes the rotation exact
- [Metric space ↗](https://en.wikipedia.org/wiki/Metric_space) — Wikipedia, with the four axioms and many more examples
- [Taxicab geometry ↗](https://en.wikipedia.org/wiki/Taxicab_geometry) — Wikipedia, with the diamond circle drawn
- [Hamming distance ↗](https://en.wikipedia.org/wiki/Hamming_distance) — Wikipedia, with its use in error-correcting codes
