# Cauchy sequences and completeness: the rationals have holes, the reals do not

**Level:** 201 · for anyone who has heard that ℝ is "complete" and ℚ is not, and wants the sentence that says so and a sequence that shows it

**One line:** A Cauchy sequence is one whose terms eventually stay within any given distance of each other, a condition that never mentions a limit; a space is complete when every Cauchy sequence has one; Newton's iteration for √2 is Cauchy in ℚ with no rational limit, so ℚ has holes, ℝ is ℚ with the holes filled, and because (0, 1) and ℝ share their open sets and differ in completeness, this is the one idea of the chapter that is not about open sets.

## Close to each other, not to a limit

The definition of [convergence](../convergence/README.md) names the limit: d(x_n, L) < ε. Often there is no L in sight and the question is whether the sequence is *behaving* as if there were one. The condition that captures that is Cauchy's:

> for every ε > 0 there is an N such that d(x_m, x_n) < ε for all m, n ≥ N.

The terms, from some point on, are all within ε of *each other*. Every convergent sequence is Cauchy, by the triangle inequality: if both x_m and x_n are within ε/2 of L they are within ε of each other. Section 1 shows 1/n is Cauchy directly, with N = ⌊1/ε⌋ + 1: all terms from N on lie in (0, 1/N], an interval of length below ε.

The converse is the whole question. A **complete** metric space is one in which every Cauchy sequence converges, to a point of the space. "Of the space" is the clause that matters.

## A Cauchy sequence of rationals with no rational limit

Section 2 runs Newton's iteration for the square root of 2, x₀ = 1 and x_{n+1} = (x_n + 2/x_n)/2, in exact fractions: 1, 3/2, 17/12, 577/408, 665857/470832, … Every term is rational, because the rule only adds and divides rationals. Write e_n = x_n² − 2, the amount by which the square overshoots; the program prints it, 1/4, 1/144, 1/166464, 1/221682772224, shrinking faster than any geometric sequence. Two facts, each one line and each inside ℚ, make the sequence Cauchy:

- e_{n+1} = e_n² / (4x_n²) ≤ e_n² / 8, since x_n² ≥ 2 from n = 1 on; so e_n → 0.
- |x_m − x_n| = |x_m² − x_n²| / (x_m + x_n) ≤ (e_m + e_n)/2, since x_m + x_n > 2; so the terms approach each other.

Now suppose the sequence had a limit L in ℚ. The function x ↦ x² is continuous, so x_n² → L², and x_n² = 2 + e_n → 2, so L² = 2 by uniqueness of limits. No rational has square 2, by the oldest proof by contradiction there is: if p² = 2q² with p/q in lowest terms, then p² is even, so p is even, p = 2k, so 4k² = 2q², so q² = 2k² is even, so q is even, and p/q was not in lowest terms. The program checks every q up to 300 as the picture; the parity argument is the proof. So the sequence is Cauchy in ℚ and converges to nothing in ℚ: **the rationals are not complete.** There is a hole where √2 should be, and the sequence is pointing at it.

The same hole breaks the intermediate value theorem in ℚ: x² − 2 is negative at 1 and positive at 2 and has no rational root between them. Every theorem of calculus that says "therefore there is a point where…" is using completeness, which is why the subject is done over ℝ.

## The reals are complete, by construction

Section 3 runs the same sequence as a sequence of real numbers. Its limit is √2, and x₄ already agrees with √2 to twelve decimals, which the program computes exactly as the integer square root of 2 · 10²⁴. The limit exists because ℝ is complete, and ℝ is complete because that is what it was built to be: one standard construction of the real numbers takes the Cauchy sequences of rationals and declares two of them the same real number when their difference tends to 0. The reals are the rationals with a limit supplied for every Cauchy sequence, and "complete" is the property the construction was for. This page uses that fact and does not prove it; [the Cantor set](../../02_Measure_Zero/cantor_set/README.md) and the rest of that chapter live inside ℝ and use it on every page.

## Completeness is not about open sets

Everything before this page was a statement about open sets: [equivalent metrics](../open_balls/README.md) have the same convergent sequences and the same continuous functions, and a [homeomorphism](../continuity/README.md) preserves both. Section 4 shows what a homeomorphism does not preserve. The open interval (0, 1) and the whole line ℝ are homeomorphic: f(x) = (2x − 1)/(x(1 − x)) maps one onto the other continuously with a continuous inverse, which the page states and does not prove. The sequence 1/n is Cauchy in (0, 1), being Cauchy in ℝ, and has no limit in (0, 1), because its only candidate is 0 and 0 is not there. So (0, 1) is not complete, and ℝ is, and the two have exactly the same open sets.

What happened to the sequence under f shows why: the program prints f(1/n) for n = 2 to 10, which is 0, −3/2, −8/3, −15/4, …, with gaps between consecutive terms that approach 1 and never 0. The image of a Cauchy sequence is not Cauchy. Being Cauchy depends on the actual distances, not only on which sets are open, and so does being complete. Analysis needs this distinction: topology can say whether a sequence converges, and only a metric can say whether it ought to.

## Two spaces that are complete for a cheap reason

Section 5 closes with the control experiment. Under the discrete metric a Cauchy sequence with ε = ½ has all its terms from N on at distance 0 from each other, that is, equal; an eventually constant sequence converges to its constant, so the discrete metric is complete. The integers with |m − n| are complete for the same reason, two different integers being at least 1 apart. And the closed interval [0, 1] is complete while (0, 1) is not: a Cauchy sequence in [0, 1] converges in ℝ, and its limit cannot escape a closed set. The one missing point is the whole difference, which is the definition of a closed set seen from the inside.

## What the program prints

<!-- output:completeness -->
*Verified output of [`completeness.py`](examples/completeness.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. x_n = 1/n IS CAUCHY: THE TERMS GET CLOSE TO EACH OTHER
   eps = 1/10    N =    11: |1/m - 1/n| < eps for m, n in N..N+59: True
   eps = 1/100   N =   101: |1/m - 1/n| < eps for m, n in N..N+59: True
   eps = 1/1000  N =  1001: |1/m - 1/n| < eps for m, n in N..N+59: True
   For all m, n >= N: both 1/m and 1/n lie in (0, 1/N], so |1/m - 1/n| < 1/N <= eps.
   A Cauchy sequence need not mention a limit: the condition is about pairs of terms.

2. NEWTON'S ITERATION FOR sqrt 2, IN EXACT FRACTIONS: CAUCHY IN Q, NO LIMIT IN Q
   x_0 = 1, x_{n+1} = (x_n + 2/x_n)/2
   x_0 = 1                            x_n^2 - 2 = -1                               |x_n - x_(n-1)| = -
   x_1 = 3/2                          x_n^2 - 2 = 1/4                              |x_n - x_(n-1)| = 1/2
   x_2 = 17/12                        x_n^2 - 2 = 1/144                            |x_n - x_(n-1)| = 1/12
   x_3 = 577/408                      x_n^2 - 2 = 1/166464                         |x_n - x_(n-1)| = 1/408
   x_4 = 665857/470832                x_n^2 - 2 = 1/221682772224                   |x_n - x_(n-1)| = 1/470832
   x_5 = 886731088897/627013566048    x_n^2 - 2 = 1/393146012008229658338304       |x_n - x_(n-1)| = 1/627013566048
   Writing e_n = x_n^2 - 2 (positive from n = 1 on): e_(n+1) = e_n^2 / (4 x_n^2) <= e_n^2 / 8,
   so e_n -> 0 faster than any geometric sequence, and |x_m - x_n| <= (e_m + e_n)/2 since
   |x_m - x_n| = |x_m^2 - x_n^2| / (x_m + x_n) and x_m + x_n > 2. So the sequence is Cauchy,
   with every step of that argument inside Q.
   Rationals p/q with q <= 300 whose square is 2: []
   None, and none at all: if p^2 = 2 q^2 in lowest terms then p is even, p = 2k, 4k^2 = 2q^2,
   2k^2 = q^2, q is even too, and p/q was not in lowest terms. (Proof by contradiction.)
   A Cauchy sequence in Q with no limit in Q: the rationals are NOT complete.

3. THE SAME SEQUENCE IN R: IT CONVERGES, AND R IS COMPLETE BY CONSTRUCTION
   sqrt 2 to 12 decimals, from isqrt(2 * 10^24) = 1414213562373: 1.414213562373
   x_4 = 665857/470832 = 1.414213562374... to 12 decimals
   The two agree in the first 12 digits. The real number sqrt 2 is what the sequence
   was heading for all along; R is Q with a limit supplied for every Cauchy sequence.
   That is one construction of R, and 'complete' is the property it is built to have.

4. COMPLETENESS IS NOT A MATTER OF OPEN SETS: (0, 1) AND R
   f(x) = (2x - 1) / (x (1 - x)) maps (0, 1) onto R, continuously and with a continuous inverse,
   so the two spaces have the same open sets and the same convergent sequences. (Not proved here.)
   The sequence 1/n is Cauchy in (0, 1) and has no limit there: its only candidate, 0, is missing.
   Its image f(1/n) for n = 2..10: 0, -3/2, -8/3, -15/4, -24/5, -35/6, -48/7, -63/8, -80/9
   Gaps between consecutive images: 3/2, 7/6, 13/12, 21/20, 31/30, 43/42, 57/56, 73/72
   The gaps approach 1 and never 0: the image is not Cauchy in R, and f(1/n) -> -infinity.
   Being Cauchy depends on the metric, not only on the open sets; so does being complete.

5. TWO SPACES THAT ARE COMPLETE FOR A CHEAP REASON
   Discrete metric, the sequence ['a', 'b', 'c', 'c', 'c', 'c', 'c']:
   from index 2 on every two terms are at distance 0, which is < 1/2. Being Cauchy with
   eps = 1/2 forces 'eventually constant', and a constant tail converges to its constant.
   The integers with |m - n|: the same argument, since two different integers are 1 apart.
   And [0, 1] is complete while (0, 1) is not: the one missing point is the whole difference.
```
<!-- /output -->

## Questions

**1. Show that a convergent sequence is Cauchy.**

<details><summary>Answer</summary>

If x_n → L, take N with d(x_n, L) < ε/2 for n ≥ N. For m, n ≥ N, d(x_m, x_n) ≤ d(x_m, L) + d(L, x_n) < ε/2 + ε/2 = ε. The triangle inequality, once.

</details>

**2. Why does being Cauchy never mention a limit, and why is that the point?**

<details><summary>Answer</summary>

It compares terms with each other, not with a point outside the sequence, so it can be checked inside the space the terms live in. That lets it detect a limit that the space is missing: in ℚ, Newton's sequence is Cauchy, and the only thing it could converge to is not rational.

</details>

**3. Give the first three terms of Newton's iteration for √2 and the first three values of x_n² − 2.**

<details><summary>Answer</summary>

1, 3/2, 17/12; and −1, 1/4, 1/144. From n = 1 on the overshoot is positive and squares at each step, divided by 4x_n² ≥ 8.

</details>

**4. Where does the proof that √2 is irrational use "lowest terms"?**

<details><summary>Answer</summary>

At the end: having shown p and q are both even, the contradiction is with the assumption that p/q had no common factor. Without that assumption the argument shows only that p and q share a factor 2, which is no contradiction.

</details>

**5. Is ℚ with the discrete metric complete?**

<details><summary>Answer</summary>

Yes. Every Cauchy sequence is eventually constant and converges. Completeness is a property of the metric, not of the set: ℚ with the usual metric is not complete and ℚ with the discrete one is.

</details>

**6. (0, 1) and ℝ are homeomorphic. Name one property they share and one they do not.**

<details><summary>Answer</summary>

They share every property defined from open sets: the same convergent sequences, the same continuous functions, connectedness. They differ in completeness, and also in boundedness, both of which are defined from distances. 1/n is Cauchy in both and converges only in ℝ.

</details>

**7. Why is [0, 1] complete when (0, 1) is not?**

<details><summary>Answer</summary>

A Cauchy sequence in [0, 1] is Cauchy in ℝ, so it converges in ℝ to some L. Every term is in [0, 1], so L is at most 1 and at least 0: the limit cannot leave a closed set. In (0, 1) it can: 1/n leaves through the open end.

</details>

## How to practise

1. **Bound the gap, not the error.** To show a sequence is Cauchy, bound d(x_m, x_n) by something that tends to 0; you may not know the limit, and that is the point.
2. **To show a space is not complete, point at the hole.** A Cauchy sequence plus a reason its limit would have to be a point the space lacks.
3. **Ask which properties a homeomorphism keeps.** Open-set properties yes; distance properties, completeness and boundedness, no.

## Flashcards

The page as a deck of Anki cards: [`completeness.txt`](anki/completeness.txt). Import with File → Import. Tags: `what`, `why`, `trap`, `problems`.

## Where this goes next

[The triangle inequality proved](../cauchy_schwarz/README.md) pays the chapter's one outstanding debt: every use of "the Euclidean distance is a metric" on these pages rested on an inequality that was checked and not proved. Beyond the chapter, a complete metric space with a norm is a Banach space, and with an inner product a Hilbert space, the setting of [the linear algebra reading guide](../../reading_guides/linear_algebra/README.md)'s next steps.

## Po polsku, w skrócie

Ciąg Cauchy'ego to ciąg, którego wyrazy od pewnego miejsca leżą dowolnie blisko siebie: dla każdego ε istnieje N takie, że d(x_m, x_n) < ε dla wszystkich m, n ≥ N. Definicja nie wspomina granicy i to jest jej sens: można ją sprawdzić wewnątrz przestrzeni, w której żyją wyrazy, i wykryć granicę, której tej przestrzeni brakuje. Przestrzeń jest zupełna, gdy każdy ciąg Cauchy'ego ma granicę w tej przestrzeni.

Iteracja Newtona dla √2, x₀ = 1, x_{n+1} = (x_n + 2/x_n)/2, daje same liczby wymierne: 1, 3/2, 17/12, 577/408, … Program liczy je dokładnie i pokazuje, że x_n² − 2 maleje szybciej niż geometrycznie, więc ciąg jest ciągiem Cauchy'ego, z każdym krokiem dowodu wewnątrz ℚ. Gdyby miał granicę wymierną L, to L² = 2, a żadna liczba wymierna nie ma kwadratu 2, co pokazuje najstarszy dowód nie wprost: z p² = 2q² wynika, że p i q są parzyste, wbrew nieskracalności. Więc ℚ nie jest zupełne: w miejscu √2 jest dziura. ℝ powstaje przez wypełnienie takich dziur, a zupełność jest własnością, dla której zbudowano liczby rzeczywiste.

Zupełność nie jest sprawą zbiorów otwartych. Przedział (0, 1) i cała prosta ℝ są homeomorficzne, mają te same zbiory otwarte, te same ciągi zbieżne i te same funkcje ciągłe, a tylko ℝ jest zupełna: ciąg 1/n jest ciągiem Cauchy'ego w (0, 1) bez granicy w (0, 1), a jego obraz pod homeomorfizmem w ℝ nie jest nawet ciągiem Cauchy'ego. Bycie ciągiem Cauchy'ego zależy od samych odległości. Metryka dyskretna jest zupełna z taniego powodu: ciąg Cauchy'ego z ε = ½ jest od pewnego miejsca stały.

## See also

- [Convergence](../convergence/README.md) — the definition that names a limit, which this one deliberately does not
- [Continuity](../continuity/README.md) — the homeomorphism that preserves everything except this
- [Open balls](../open_balls/README.md) — equivalent metrics, which share convergence but need not share completeness
- [Induction](../../11_Logic/induction/README.md) — proof by contradiction, used here for √2
- [The Cantor set](../../02_Measure_Zero/cantor_set/README.md) — a construction that lives on the completeness of ℝ
- [Machine numbers](../../01_Precision/machine_numbers/README.md) — the floats, a finite set with no limits at all, which is why none of this page is done in them
- [Complete metric space ↗](https://en.wikipedia.org/wiki/Complete_metric_space) — Wikipedia, with the construction of ℝ from Cauchy sequences
