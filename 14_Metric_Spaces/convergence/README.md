# Convergence: a limit is a statement about every ball

**Level:** 201 · for anyone who has written "x_n → 0" and been asked what, exactly, that claims

**One line:** x_n → L says that every ball around L, however small, contains the whole tail of the sequence from some index on; the program finds that index for each radius, shows why (−1)ⁿ has no limit by one ball that misses half the terms, proves a limit is unique with two disjoint balls, gets three different N and one limit from three equivalent metrics, and shows 1/n stop converging under the discrete metric, because convergence belongs to the metric and not to the points.

## The definition, in balls and in symbols

A sequence x₁, x₂, x₃, … in a metric space **converges** to L, written x_n → L, when

> for every ε > 0 there is an index N such that d(x_n, L) < ε for every n ≥ N.

In the language of the [previous page](../open_balls/README.md): every open ball B(L, ε) contains a tail of the sequence, all the terms from x_N on. The ε is the challenge, the N is the answer, and the order of the quantifiers is the whole content: ∀ε ∃N, the N may depend on ε and usually does. [Predicates and quantifiers](../../11_Logic/predicates_and_quantifiers/README.md) is the page about why that order cannot be swapped.

Section 1 runs the definition on x_n = 1/n with L = 0. For ε = 1/10 the answer is N = 11, for 1/100 it is 101, for 1/1000 it is 1001, and each is the smallest that works: 1/10 is not less than 1/10. The program checks a window of terms after N, which is a test of the arithmetic; the reason N works for *all* n ≥ N is one line of algebra, 1/n < ε exactly when n > 1/ε, and every n ≥ ⌊1/ε⌋ + 1 is bigger than 1/ε. That line is the proof, and it is what a loop cannot do, as [what a proof is](../../11_Logic/what_a_proof_is/README.md) argues.

## Not converging: one ball that misses half the terms

The negation of ∀ε ∃N ∀n ≥ N is ∃ε ∀N ∃n ≥ N: there is one radius for which no tail fits, which means that outside the ball there are terms arbitrarily far along. Section 2 does this for x_n = (−1)ⁿ, whose terms are 1, −1, 1, −1, …, against every candidate limit L at once. The two values 1 and −1 are at distance 2, so by the triangle inequality d(1, L) + d(L, −1) ≥ 2, so one of them is at least 1: the ball B(L, 1) misses either all the odd terms or all the even ones, infinitely many either way. The program prints the far one for six candidates; the triangle-inequality sentence covers every candidate at once. The sequence has no limit, under this metric.

## A limit is unique

Could a sequence converge to two different points? Section 3 says no, with two balls. If L ≠ M, let r = d(L, M)/2 and look at B(L, r) and B(M, r). They are disjoint: a point x in both would give d(L, M) ≤ d(L, x) + d(x, M) < r + r = d(L, M). A tail of the sequence would have to lie inside both balls, which no point does, so there is no second limit. The program confirms on a grid of step 1/100 that no point is within 1/10 of both 0 and 1/5, which is the picture; the inequality is the proof. This is the first theorem of analysis that uses nothing but the triangle inequality, and it is why "the limit" has a definite article.

## Three metrics, three N, one limit

Section 4 takes the sequence x_n = (1/n, (−1)ⁿ/n) in the plane, which spirals in to (0, 0) alternating above and below the axis, and asks for the N that puts the tail inside the ball of radius 1/10 under each of the three metrics. The answers are 15, 21 and 11, for Euclidean, taxicab and Chebyshev, because the three balls of radius 1/10 are three different sizes. The limit is the same under all three, and the reason is the nesting from the previous page: a tail inside the taxicab ball of radius ε is inside the Euclidean and Chebyshev balls of radius ε, and a tail inside the Chebyshev ball of radius ε/2 is inside the taxicab ball of radius ε. So **equivalent metrics have the same convergent sequences and the same limits**, with different N. Convergence is a property of the open sets, which is the same thing as saying it is a topological property.

Section 6 adds the useful consequence: under the Chebyshev metric a point is in the square ball exactly when each coordinate is within ε of the limit's coordinate, so a sequence in the plane converges exactly when both coordinate sequences converge, and by equivalence that holds for the Euclidean and taxicab metrics too. Limits in ℝⁿ are limits in ℝ taken n at a time.

## Under the discrete metric, 1/n stops converging

Section 5 is the control experiment. Under the metric with d(p, q) = 1 for p ≠ q, every term 1/n is at distance exactly 1 from 0, so the ball B(0, ½) contains no term at all, and the sequence does not converge to 0, or to anything: the only sequences that converge under the discrete metric are those that are eventually constant, since a tail inside a ball of radius ½ is a tail of one repeated point. Same points, same sequence, a different metric and a different answer. The discrete metric is not equivalent to the Euclidean one, and this is what that failure costs.

## What the program prints

<!-- output:convergence -->
*Verified output of [`convergence.py`](examples/convergence.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. x_n = 1/n CONVERGES TO 0: FOR EVERY RADIUS, A TAIL INSIDE THE BALL
   eps = 1/10    N =    11: 1/n < eps for n = N..109: True;  1/10 = 1/10 is not < eps, so N cannot be smaller.
   eps = 1/100   N =   101: 1/n < eps for n = N..1009: True;  1/100 = 1/100 is not < eps, so N cannot be smaller.
   eps = 1/1000  N =  1001: 1/n < eps for n = N..10009: True;  1/1000 = 1/1000 is not < eps, so N cannot be smaller.
   The N works for ALL n >= N, not only the ones checked: 1/n < eps exactly when n > 1/eps,
   and every n >= floor(1/eps) + 1 is bigger than 1/eps. The loop checks the arithmetic.

2. x_n = (-1)^n HAS NO LIMIT: THE BALL OF RADIUS 1 AROUND ANY CANDIDATE MISSES HALF THE TERMS
   L = -1   max(d(1, L), d(-1, L)) = 2    >= 1: the terms equal to +1 all lie outside B(L, 1).
   L = -1/2 max(d(1, L), d(-1, L)) = 3/2  >= 1: the terms equal to +1 all lie outside B(L, 1).
   L = 0    max(d(1, L), d(-1, L)) = 1    >= 1: the terms equal to +1 all lie outside B(L, 1).
   L = 1/2  max(d(1, L), d(-1, L)) = 3/2  >= 1: the terms equal to -1 all lie outside B(L, 1).
   L = 1    max(d(1, L), d(-1, L)) = 2    >= 1: the terms equal to -1 all lie outside B(L, 1).
   L = 3    max(d(1, L), d(-1, L)) = 4    >= 1: the terms equal to -1 all lie outside B(L, 1).
   For every L: d(1, -1) = 2 <= d(1, L) + d(L, -1), so one of the two distances is >= 1.
   One radius with no tail inside, for every candidate: that is the negation of convergence.

3. A LIMIT IS UNIQUE: TWO CANDIDATES, TWO DISJOINT BALLS
   Suppose x_n -> L = 0 and x_n -> M = 1/5. Let r = d(L, M)/2 = 1/10.
   Points within r of both L and M, on a grid of step 1/100: []
   None, and none anywhere: a point in both balls would give d(L, M) <= d(L, x) + d(x, M) < 2r = d(L, M).
   A tail of the sequence cannot lie in two disjoint balls, so L = M.

4. ONE SEQUENCE IN THE PLANE, THREE METRICS, THREE N, ONE LIMIT
   x_n = (1/n, (-1)^n / n), limit (0, 0), eps = 1/10.
   Euclidean  first N with the tail inside the ball: N =  15   (checked 200 terms on)
   taxicab    first N with the tail inside the ball: N =  21   (checked 200 terms on)
   Chebyshev  first N with the tail inside the ball: N =  11   (checked 200 terms on)
   Three different N, because the balls have three sizes; one limit, because the balls nest:
   a tail inside the taxicab ball is inside the Euclidean and Chebyshev balls of the same radius,
   and a tail inside the Chebyshev ball of radius r/2 is inside the taxicab ball of radius r.
   Equivalent metrics have the same convergent sequences and the same limits.

5. UNDER THE DISCRETE METRIC, 1/n DOES NOT CONVERGE TO 0
   d(1/n, 0) for n = 1..7: 1, 1, 1, 1, 1, 1, 1
   Every term is at distance 1 from 0, so the ball B(0, 1/2) contains no term at all.
   Under this metric a sequence converges only if it is eventually constant. Same points,
   same sequence, a different metric, a different answer: convergence belongs to the metric.

6. IN THE PLANE, CONVERGENCE IS COORDINATE BY COORDINATE
   Under Chebyshev, cheb(x_n, L) < eps means |x-part| < eps AND |y-part| < eps: a point is
   in the square ball exactly when each coordinate is in its interval. So x_n -> L in the plane
   exactly when both coordinate sequences converge, and by section 4 that holds for all three metrics.
   x-parts: 1, 1/2, 1/3, 1/4, 1/5, ...  -> 0
   y-parts: -1, 1/2, -1/3, 1/4, -1/5, ...  -> 0
```
<!-- /output -->

## Questions

**1. For x_n = 1/n² and ε = 1/100, find the smallest N with d(x_n, 0) < ε for all n ≥ N.**

<details><summary>Answer</summary>

1/n² < 1/100 exactly when n > 10, so N = 11; 1/10² = 1/100 is not less than ε. For a general ε the answer is ⌊1/√ε⌋ + 1.

</details>

**2. Write out the negation of "x_n → L" with the quantifiers in order, and say what each one is.**

<details><summary>Answer</summary>

There exists ε > 0 such that for every N there exists n ≥ N with d(x_n, L) ≥ ε. The ε is one fixed radius, the N is any proposed start of a tail, and the n is the witness past it that lies outside the ball. Each ∀ became ∃ and each ∃ became ∀, as negation always does.

</details>

**3. Does x_n = (−1)ⁿ/n converge? Find N for ε = 1/50.**

<details><summary>Answer</summary>

Yes, to 0: d(x_n, 0) = 1/n regardless of the sign, so N = 51 as for 1/n. The sign changes are invisible to the distance.

</details>

**4. Where in the uniqueness proof is the triangle inequality used, and what would go wrong without it?**

<details><summary>Answer</summary>

In showing the two balls of radius d(L, M)/2 are disjoint: a common point x would give d(L, M) ≤ d(L, x) + d(x, M) < d(L, M). Without the triangle inequality two balls around different centres could overlap however small the radius, and a sequence could have two limits.

</details>

**5. The N for the spiral sequence was 15 under the Euclidean metric and 11 under Chebyshev. Why is the Chebyshev N the smallest?**

<details><summary>Answer</summary>

Because the Chebyshev ball of a given radius is the largest of the three, the square that contains the disc that contains the diamond, so the tail falls into it first. Taxicab, the smallest ball, needs the largest N, 21.

</details>

**6. Under the discrete metric, which sequences converge?**

<details><summary>Answer</summary>

Exactly the eventually constant ones. A tail inside B(L, ½) is a tail of terms equal to L. So 1/n does not converge, and a sequence that is 3, 3, 3, … from some point on converges to 3.

</details>

**7. A sequence in the plane has x-coordinates converging to 2 and y-coordinates converging to −1. Does it converge, and to what?**

<details><summary>Answer</summary>

To (2, −1), under any of the three metrics. Under Chebyshev the ball of radius ε around (2, −1) is the set where both coordinates are within ε, so take N as the larger of the two coordinate N's; equivalence carries it to the other two metrics.

</details>

## How to practise

1. **Answer the challenge.** Given ε, write the inequality d(x_n, L) < ε, solve it for n, and name N; then say why every larger n also works.
2. **To disprove, pick the ε.** Then show that for every N some later term escapes the ball. One ε and a rule for the witness is the whole proof.
3. **Change the metric and ask again.** If the answer changes, you have learned what the metric was doing; if not, you have learned the fact was topological.

## Flashcards

The page as a deck of Anki cards: [`convergence.txt`](anki/convergence.txt). Import with File → Import. Tags: `what`, `why`, `trap`, `problems`.

## Where this goes next

[Continuity](../continuity/README.md) is the same sentence with a function in the middle: a ball around f(p) in the target, a ball around p in the source that f sends inside it. Then [Cauchy sequences](../completeness/README.md) ask what a sequence is doing when it behaves like a convergent one and no limit is in sight.

## Po polsku, w skrócie

Ciąg zbiega do L, gdy każda kula wokół L, choćby najmniejsza, zawiera cały ogon ciągu od pewnego miejsca: dla każdego ε istnieje N takie, że d(x_n, L) < ε dla wszystkich n ≥ N. Kolejność kwantyfikatorów jest całą treścią: ε jest wyzwaniem, N odpowiedzią, i N zwykle zależy od ε. Program liczy to N dla ciągu 1/n i trzech promieni, a jedna linijka algebry, 1/n < ε dokładnie wtedy, gdy n > 1/ε, jest dowodem, że działa dla wszystkich n, nie tylko sprawdzonych.

Zaprzeczenie zbieżności to jedno ε, dla którego żaden ogon nie mieści się w kuli. Dla ciągu (−1)ⁿ kula o promieniu 1 wokół dowolnego kandydata L omija połowę wyrazów, bo z nierówności trójkąta d(1, L) + d(L, −1) ≥ 2. Granica jest jedyna: wokół dwóch różnych kandydatów można narysować dwie rozłączne kule, znów z nierówności trójkąta, a ogon nie zmieści się w obu. Ten sam ciąg na płaszczyźnie pod trzema równoważnymi metrykami ma trzy różne N (15, 21, 11 dla ε = 1/10) i jedną granicę, bo kule są zagnieżdżone. Pod metryką dyskretną ciąg 1/n przestaje zbiegać: każdy wyraz jest w odległości 1 od zera, więc kula o promieniu ½ nie zawiera żadnego. Zbieżność należy do metryki, nie do punktów.

## See also

- [Open balls](../open_balls/README.md) — the balls this definition quantifies over, and why equivalent metrics share them
- [Predicates and quantifiers](../../11_Logic/predicates_and_quantifiers/README.md) — ∀ε ∃N against ∃N ∀ε, and what negating a quantifier does
- [What a proof is](../../11_Logic/what_a_proof_is/README.md) — why the algebra line is the proof and the checked window is not
- [The derivative is a velocity](../../09_Calculus/derivative_as_velocity/README.md) — the limit that chapter took on trust, now defined
- [Countable sets](../../02_Measure_Zero/countable_sets/README.md) — sequences as the way to list, before they are the way to approach
- [Limit of a sequence ↗](https://en.wikipedia.org/wiki/Limit_of_a_sequence) — Wikipedia, with the definition in metric spaces and its history
