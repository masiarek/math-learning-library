# The triangle inequality proved: Cauchy–Schwarz from a quadratic with no roots

**Level:** 201 · for anyone who has used "the Euclidean distance is a metric" and noticed that the fourth property was checked on a grid and never proved

**One line:** For any two vectors, |u + tw|² is a quadratic in t that is never negative, so its discriminant is at most zero, and that one sentence is the Cauchy–Schwarz inequality (u·w)² ≤ |u|²|w|²; the triangle inequality for the Euclidean distance then follows in three lines, so the chapter's main example is a metric on the strength of nothing but "a square is never negative".

## The debt

[Distance in n dimensions](../../08_Analytic_Geometry/distance_in_n_dimensions/README.md) listed the four properties of a metric and proved three of them for the Euclidean formula in a line each; the fourth, d(P, R) ≤ d(P, Q) + d(Q, R), it checked on 91 125 triples and marked as not proved. [Distance is the four properties](../../08_Analytic_Geometry/other_distances/README.md) and every page of this chapter then used the Euclidean metric as the main example. This page is the proof.

Write points as vectors and distances as lengths: with u = Q − P and w = R − Q, the segment from P to R is u + w, and the claim is |u + w| ≤ |u| + |w|. Lengths come from the dot product, |v|² = v·v, so the claim is about dot products, and one inequality about dot products is all it takes.

## A quadratic that is never negative

Fix two vectors u and w and let t be a real number. The vector u + tw has a length, and its squared length is

> **q(t) = |u + tw|² = |w|² t² + 2(u·w) t + |u|²**

by expanding (u + tw)·(u + tw) with the dot product's rules, which are the ordinary rules of multiplying out brackets. Section 1 computes q for u = (1, 2) and w = (3, 4): q(t) = 25t² + 22t + 5, and tabulates it at five values of t, all positive. It is positive at every t, not only those five, because it is a squared length, a sum of squares.

Now the one fact about quadratics: a quadratic At² + Bt + C with A > 0 that is never negative cannot have two distinct real roots, since between two roots it would dip below zero; so its discriminant B² − 4AC is at most 0. Here A = |w|², B = 2(u·w), C = |u|², and B² − 4AC ≤ 0 reads 4(u·w)² ≤ 4|w|²|u|². Divide by 4:

> **(u·w)² ≤ |u|² |w|²**

the **Cauchy–Schwarz inequality**. For the sample vectors the discriminant is 22² − 4 · 25 · 5 = −16, and the inequality is 121 ≤ 125. (If w = 0 the quadratic is constant and the inequality is 0 ≤ 0.)

## Equality, and what it means

Section 2 takes w = 2u. Now q(t) = 20t² + 20t + 5 has discriminant 0 and a double root at t = −½, where u + tw is the zero vector, and (u·w)² = 100 = |u|²|w|². The discriminant is 0 exactly when q has a root, which is exactly when some u + tw = 0, which is exactly when u is a multiple of w, or w = 0. So Cauchy–Schwarz is an equality precisely for parallel vectors, and strict otherwise. That is also where the triangle inequality is an equality: three points on a line with the middle one between, the case [the distance formula](../../08_Analytic_Geometry/distance_formula/README.md) used as a test for collinearity.

Section 3 checks the inequality on all 15 625 pairs of integer vectors in a 5 × 5 × 5 grid, and counts the pairs with equality. The check is evidence that the inequality was copied right; the discriminant argument is the proof, and it never used how many coordinates the vectors have, so it holds in every dimension, including the infinitely many of the [roadmap](../../ROADMAP.md)'s Hilbert spaces.

## The triangle inequality in three lines

Section 4 finishes the debt. For any u and w,

| Line | Because |
|---|---|
| \|u + w\|² = \|u\|² + 2(u·w) + \|w\|² | expand the dot product |
| ≤ \|u\|² + 2\|u\|\|w\| + \|w\|² | u·w ≤ \|u·w\| ≤ \|u\|\|w\|, the square root of Cauchy–Schwarz |
| = (\|u\| + \|w\|)², so \|u + w\| ≤ \|u\| + \|w\| | both sides are non-negative, so taking roots keeps the order |

With u = Q − P and w = R − Q the last line is d(P, R) ≤ d(P, Q) + d(Q, R). The program checks it on the same grid without ever taking a square root: |u + w|² ≤ (|u| + |w|)² reduces to u·w ≤ |u||w|, which holds when u·w ≤ 0 and otherwise is Cauchy–Schwarz again. The Euclidean distance now has all four properties with a proof beside each, which is what [what a proof is](../../11_Logic/what_a_proof_is/README.md) asks of a claim before it is used.

## What was used

The whole argument rests on three things: the dot product distributes over addition like ordinary multiplication; a sum of squares is never negative; and a quadratic that is never negative has discriminant at most zero, which is the quadratic formula read backwards. No geometry was used, no angle, no picture, and that is why the same proof gives the triangle inequality for vectors with a thousand coordinates or for functions with ∫ f² in place of Σ fᵢ². The inequality is named for Cauchy, who proved it for sums in 1821, and Schwarz, who proved it for integrals in 1888, with Bunyakovsky between them in 1859; those dates are from memory.

## What the program prints

<!-- output:cauchy_schwarz -->
*Verified output of [`cauchy_schwarz.py`](examples/cauchy_schwarz.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. q(t) = |u + t w|^2 IS A QUADRATIC IN t THAT IS NEVER NEGATIVE
   u = (1, 2), w = (3, 4): q(t) = |w|^2 t^2 + 2 (u.w) t + |u|^2 = 25 t^2 + 22 t + 5
   t = -2: u + t w = (-5, -6)   q(t) = 61
   t = -1: u + t w = (-2, -2)   q(t) = 8
   t =  0: u + t w = (1, 2)     q(t) = 5
   t =  1: u + t w = (4, 6)     q(t) = 52
   t =  2: u + t w = (7, 10)    q(t) = 149
   q(t) is a sum of squares, so q(t) >= 0 for every real t. A quadratic with positive
   leading coefficient that is never negative has no two distinct real roots, so its
   discriminant is at most 0: B^2 - 4AC = 22^2 - 4 * 25 * 5 = -16 <= 0.
   Divide by 4: (u.w)^2 <= |u|^2 |w|^2, here 121 <= 125. That is Cauchy-Schwarz.

2. EQUALITY EXACTLY WHEN ONE VECTOR IS A MULTIPLE OF THE OTHER
   u = (1, 2), w = (2, 4) = 2u: q(t) = 20 t^2 + 20 t + 5, discriminant 0.
   q has the double root t = -1/2: u + (-1/2) w = (0, 0), and (u.w)^2 = 100 = |u|^2 |w|^2 = 100.
   The discriminant is 0 exactly when some u + t w is the zero vector, i.e. u is a multiple of w
   (or w = 0). That is the equality case, and it is where the triangle inequality is an equality too.

3. CAUCHY-SCHWARZ ON EVERY PAIR OF A GRID IN THREE DIMENSIONS
   (u.w)^2 <= |u|^2 |w|^2 on 15625 pairs: True;  pairs with equality: 601
   The check is evidence that the inequality was copied right; section 1 is the proof, and it
   used nothing about the number of coordinates, so it holds in every dimension.

4. THE TRIANGLE INEQUALITY, IN THREE LINES AND WITHOUT A SQUARE ROOT
   |u + w|^2 = |u|^2 + 2 (u.w) + |w|^2                      expand the dot product
            <= |u|^2 + 2 |u| |w| + |w|^2                     u.w <= |u.w| <= |u| |w|, Cauchy-Schwarz
            = (|u| + |w|)^2,  so |u + w| <= |u| + |w|          both sides non-negative, take roots
   With u = Q - P and w = R - Q, u + w = R - P, and the line reads d(P, R) <= d(P, Q) + d(Q, R).
   |u + w| <= |u| + |w| on the same 15625 pairs, compared through squares: True
   The Euclidean distance has all four properties of a metric, every one of them now proved,
   and the chapter's main example rests on nothing but 'a square is never negative'.
```
<!-- /output -->

## Questions

**1. Compute q(t) = |u + tw|² for u = (1, 0) and w = (0, 1), and read off Cauchy–Schwarz.**

<details><summary>Answer</summary>

q(t) = t² + 0 · t + 1, discriminant 0 − 4 = −4 ≤ 0, so (u·w)² = 0 ≤ 1 = |u|²|w|². Perpendicular vectors are the farthest from equality: the discriminant is as negative as it can be for unit vectors.

</details>

**2. Why does a quadratic with positive leading coefficient that is never negative have discriminant at most 0?**

<details><summary>Answer</summary>

A positive discriminant means two distinct real roots, and a parabola opening upward is negative strictly between its roots. So "never negative" rules out a positive discriminant. Zero is allowed: a double root, where the parabola touches the axis.

</details>

**3. For which u and w is (u·w)² = |u|²|w|²?**

<details><summary>Answer</summary>

Exactly when one is a multiple of the other, including the zero vector. Then some u + tw = 0, q has a root, and the discriminant is 0. For u = (1, 2), w = (2, 4): 100 = 5 · 20.

</details>

**4. Where in the three-line proof is the square root of Cauchy–Schwarz taken, and why is that allowed?**

<details><summary>Answer</summary>

In the middle line: from (u·w)² ≤ |u|²|w|² to |u·w| ≤ |u||w|. Both sides are non-negative, and the square root keeps the order of non-negative numbers. Then u·w ≤ |u·w| is the absolute value.

</details>

**5. The program checks the triangle inequality without square roots. How?**

<details><summary>Answer</summary>

|u + w|² ≤ (|u| + |w|)² expands to 2(u·w) ≤ 2|u||w|. If u·w ≤ 0 that is immediate; if u·w > 0, square both sides, which keeps the order of positives, and it is (u·w)² ≤ |u|²|w|². Every comparison is between integers.

</details>

**6. Does the proof need the vectors to have two or three coordinates?**

<details><summary>Answer</summary>

No. It used only that the dot product distributes, that a sum of squares is non-negative, and the discriminant fact. Any number of coordinates, or infinitely many with the sum convergent, or an integral, gives the same proof word for word.

</details>

**7. The taxicab and Chebyshev distances also satisfy the triangle inequality. Does this page prove that?**

<details><summary>Answer</summary>

No. Their proofs are easier and different: |a + b| ≤ |a| + |b| coordinate by coordinate for the taxicab distance, and max(|a + b|) ≤ max(|a|) + max(|b|) for Chebyshev. Cauchy–Schwarz is specific to the dot product, which is why it is the Euclidean distance that needed it.

</details>

## How to practise

1. **Expand |u + tw|² once by hand**, with letters, until the three coefficients are automatic; the inequality is just the discriminant of that expansion.
2. **Check equality cases.** Parallel vectors should give discriminant 0; if yours does not, the expansion is wrong.
3. **Prove the taxicab triangle inequality** in one line from |a + b| ≤ |a| + |b|, to see why Euclid's needed more.

## Flashcards

The page as a deck of Anki cards: [`cauchy_schwarz.txt`](anki/cauchy_schwarz.txt). Import with File → Import. Tags: `what`, `why`, `trap`, `problems`.

## Where this goes next

A vector space with a dot product is an inner product space, and the length √(v·v) makes it a metric space by this page; complete, it is a Hilbert space, where Fourier series are Pythagoras with infinitely many legs. The [linear algebra reading guide](../../reading_guides/linear_algebra/README.md) says which book to learn that from.

## Po polsku, w skrócie

Rozdział traktował odległość euklidesową jako metrykę, a jej czwarta własność, nierówność trójkąta, była dotąd tylko sprawdzona na siatce punktów. Ta strona ją dowodzi. Dla dwóch wektorów u i w kwadrat długości |u + tw|² jest trójmianem kwadratowym zmiennej t: |w|² t² + 2(u·w) t + |u|². Jako suma kwadratów nigdy nie jest ujemny, więc nie może mieć dwóch różnych pierwiastków rzeczywistych, więc jego wyróżnik jest co najwyżej zero. To jedno zdanie, po podzieleniu przez 4, to nierówność Cauchy'ego–Schwarza: (u·w)² ≤ |u|²|w|². Równość zachodzi dokładnie wtedy, gdy wektory są równoległe, bo wtedy trójmian ma pierwiastek.

Nierówność trójkąta wynika z niej w trzech linijkach: |u + w|² = |u|² + 2(u·w) + |w|² ≤ |u|² + 2|u||w| + |w|² = (|u| + |w|)², a obie strony są nieujemne, więc można wyciągnąć pierwiastek. Z u = Q − P i w = R − Q to jest d(P, R) ≤ d(P, Q) + d(Q, R). Program liczy trójmian dokładnie dla przykładowych wektorów, pokazuje przypadek równości, sprawdza nierówność na 15 625 parach wektorów całkowitych w trzech wymiarach i wyprowadza nierówność trójkąta bez ani jednego pierwiastka. Dowód nie używa liczby współrzędnych, więc działa w każdym wymiarze i dla całek; cała odległość euklidesowa spoczywa na tym, że kwadrat nigdy nie jest ujemny.

## Auf Deutsch: Stichwörter

Die Dreiecksungleichung bewiesen: Cauchy–Schwarz aus einer quadratischen Funktion ohne Nullstellen, und damit ist die euklidische Metrik eine Metrik.

**Stichwörter:** Cauchy-Schwarz-Ungleichung, Dreiecksungleichung, Skalarprodukt, Norm, Diskriminante, quadratische Funktion ohne reelle Nullstelle.

## See also

- [Distance in n dimensions](../../08_Analytic_Geometry/distance_in_n_dimensions/README.md) — where the four properties were checked and this one left open
- [Distance is the four properties](../../08_Analytic_Geometry/other_distances/README.md) — the other metrics, whose triangle inequalities are easier
- [Open balls](../open_balls/README.md) — the chapter this proof underwrites
- [What a proof is](../../11_Logic/what_a_proof_is/README.md) — a checked claim is not a proved one
- [Multiplication rotates](../../03_Complex_Numbers/multiplication_rotates/README.md) — |zw| = |z||w|, the complex case where the inequality is an equation
- [Cauchy–Schwarz inequality ↗](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality) — Wikipedia, with several proofs and the inner-product form
