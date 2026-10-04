# Continuity by ε and δ: a ball around the output, a ball around the input

**Level:** 201 · for anyone who was told a continuous function is one you can draw without lifting the pen, and now has functions with no graph to draw

**One line:** f is continuous at p when for every ball of radius ε around f(p) there is a ball of radius δ around p that f sends entirely inside it; the program finds δ for x² at 3, shows the step function has one ε that defeats every δ with a witness for each, proves the distance to a fixed point is continuous with δ = ε from the triangle inequality, and shows that every function out of a discrete space is continuous, so continuity is a property of the map together with both metrics.

## The definition

Let f map a metric space X to a metric space Y, each with its own distance. f is **continuous at p** when

> for every ε > 0 there is a δ > 0 such that d(x, p) < δ implies d(f(x), f(p)) < ε.

In balls: f sends B(p, δ) inside B(f(p), ε). The ε is a target drawn around the output, the δ is the room allowed around the input, and the order is the same ∀ε ∃δ as for [convergence](../convergence/README.md): δ may depend on ε, and on p. f is continuous when it is continuous at every point.

Section 1 runs the definition on f(x) = x² at p = 3. The δ that works is min(1, ε/7), and the reason is two lines: |x² − 9| = |x − 3| · |x + 3|, and when |x − 3| < 1 the second factor is below 7, so |x² − 9| < 7 · |x − 3| < 7 · (ε/7) = ε. The program checks 1 999 points within δ of 3 for four values of ε, which tests the arithmetic; the two lines are what make the δ work for every x and not only for those.

## Not continuous: one ε, a witness for every δ

Negate the definition, flipping each quantifier as [predicates and quantifiers](../../11_Logic/predicates_and_quantifiers/README.md) prescribes: f is not continuous at p when there is one ε > 0 such that for every δ > 0 some x has d(x, p) < δ and d(f(x), f(p)) ≥ ε. Section 2 does it for the step function s(x) = 0 for x < 0, s(x) = 1 for x ≥ 0, at p = 0, with ε = ½. For any δ the point x = −δ/2 is within δ of 0 and has s(x) = 0, a full 1 away from s(0) = 1. One ε and a formula for the witness, and the proof is complete; the program prints the witness for four values of δ as the picture. A jump of height 1 cannot be squeezed inside a ball of radius ½, however close to the jump you stay.

This is the shape of every "not continuous" proof: a universal claim is refuted by one counterexample, here one ε, and the ∀δ inside it is handled by a rule that produces the witness, exactly as [one counterexample](../../11_Logic/converse_and_contrapositive/README.md#examples-prove-nothing-one-counterexample-disproves) ends an "if A then B".

## The distance itself is continuous

Fix a point p and consider the function x ↦ d(x, p), from the space to the real line. Section 3 proves it continuous with δ = ε, in every metric space, from the triangle inequality alone: d(x, p) ≤ d(x, y) + d(y, p) gives d(x, p) − d(y, p) ≤ d(x, y), and swapping x and y gives the other sign, so

> **|d(x, p) − d(y, p)| ≤ d(x, y)**

Then d(x, y) < ε forces |d(x, p) − d(y, p)| < ε. The program checks the inequality on 2 401 pairs under the taxicab metric, where everything is an integer. This is the first continuous function of the chapter that comes with the space itself, and it is why "the set of points at distance less than r from p" is open: it is the preimage of an open interval under a continuous map, which the next remark explains.

**Continuity and open sets.** f is continuous on all of X exactly when the preimage f⁻¹(V) of every open set V in Y is open in X. One direction: if V is open and f(p) ∈ V, some B(f(p), ε) ⊆ V; continuity gives a δ with f(B(p, δ)) ⊆ B(f(p), ε) ⊆ V, so B(p, δ) ⊆ f⁻¹(V). The other direction takes V = B(f(p), ε) itself. So continuity, like convergence, is a statement about open sets, and equivalent metrics have the same continuous functions.

## The identity map between equivalent metrics

Section 4 makes that last sentence concrete. The identity map from the plane with the taxicab metric to the plane with the Euclidean metric is continuous with δ = ε, because eucl ≤ taxi; the identity in the other direction is continuous with δ = ε/2, because taxi ≤ 2 · cheb ≤ 2 · eucl. Both are checked on the grid through squared distances. A map that is continuous, one-to-one and onto, with a continuous inverse, is a **homeomorphism**, and two spaces joined by one have the same open sets, the same convergent sequences and the same continuous functions. Equivalent metrics on the same set are the simplest case: the identity is the homeomorphism.

## Out of a discrete space, everything is continuous

Section 5 is the control experiment again. Let X carry the discrete metric and f be any function at all from X to anywhere. Take δ = ½. The only x with d(x, p) < ½ is p itself, and d(f(p), f(p)) = 0 < ε for every ε. The condition is satisfied by having nothing to satisfy, so f is continuous at every point, whatever its values. The program shows it for a function whose values jump between 0, 100, −7 and 3 across five points.

The lesson of the control: continuity is not a property of a function alone. It is a property of a function together with the metric on its source and the metric on its target. Change either and the answer can change. The step function is discontinuous on the real line with its usual metric and continuous on the real line with the discrete metric, and both statements are true.

## What the program prints

<!-- output:continuity -->
*Verified output of [`continuity.py`](examples/continuity.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. f(x) = x^2 IS CONTINUOUS AT 3: FOR EVERY eps, A delta
   eps = 1      delta = min(1, eps/7) = 1/7     |x^2 - 9| < eps on 1999 points within delta of 3: True
   eps = 1/10   delta = min(1, eps/7) = 1/70    |x^2 - 9| < eps on 1999 points within delta of 3: True
   eps = 1/100  delta = min(1, eps/7) = 1/700   |x^2 - 9| < eps on 1999 points within delta of 3: True
   eps = 1/1000 delta = min(1, eps/7) = 1/7000  |x^2 - 9| < eps on 1999 points within delta of 3: True
   Why delta = min(1, eps/7) works for EVERY x, not only the grid:
     |x^2 - 9| = |x - 3| |x + 3|, and |x - 3| < 1 gives 2 < x < 4, so |x + 3| < 7,
     so |x^2 - 9| < 7 |x - 3| < 7 (eps/7) = eps.

2. THE STEP FUNCTION IS NOT CONTINUOUS AT 0: ONE eps DEFEATS EVERY delta
   s(x) = 0 for x < 0 and 1 for x >= 0; s(0) = 1. Take eps = 1/2.
   delta = 1       witness x = -1/2     |x - 0| = 1/2     < delta, and |s(x) - s(0)| = 1 >= eps
   delta = 1/10    witness x = -1/20    |x - 0| = 1/20    < delta, and |s(x) - s(0)| = 1 >= eps
   delta = 1/100   witness x = -1/200   |x - 0| = 1/200   < delta, and |s(x) - s(0)| = 1 >= eps
   delta = 1/1000  witness x = -1/2000  |x - 0| = 1/2000  < delta, and |s(x) - s(0)| = 1 >= eps
   The witness x = -delta/2 works for every delta > 0, so no delta works for eps = 1/2.
   'Not continuous' is: there EXISTS an eps such that for ALL delta some x breaks it;
   the negation of a for-all-exists is an exists-for-all, and the witness is the proof.

3. THE DISTANCE TO A FIXED POINT IS CONTINUOUS, WITH delta = eps
   Claim: |d(x, p) - d(y, p)| <= d(x, y). Proof: d(x, p) <= d(x, y) + d(y, p) is the triangle
   inequality, so d(x, p) - d(y, p) <= d(x, y); swap x and y for the other sign.
   Checked with the taxicab metric on 2401 pairs around p = (1, 2): True
   So if d(x, y) < eps then |d(x, p) - d(y, p)| < eps: delta = eps, in every metric space.

4. THE IDENTITY MAP BETWEEN TWO EQUIVALENT METRICS IS CONTINUOUS BOTH WAYS
   From (plane, taxicab) to (plane, Euclidean): eucl <= taxi, so delta = eps.
   From (plane, Euclidean) to (plane, taxicab): taxi <= 2 cheb <= 2 eucl, so delta = eps/2.
   eucl^2 <= taxi^2 on all pairs: True;  taxi^2 <= 4 eucl^2 on all pairs: True
   A map that is continuous both ways, with a continuous inverse, is a homeomorphism:
   the two metric spaces have the same open sets and the same convergent sequences.

5. OUT OF A DISCRETE SPACE, EVERY FUNCTION IS CONTINUOUS
   p = a: points within delta = 1/2 of p: ['a']; |f(x) - f(p)| there is 0, below every eps.
   p = b: points within delta = 1/2 of p: ['b']; |f(x) - f(p)| there is 0, below every eps.
   p = c: points within delta = 1/2 of p: ['c']; |f(x) - f(p)| there is 0, below every eps.
   p = d: points within delta = 1/2 of p: ['d']; |f(x) - f(p)| there is 0, below every eps.
   p = e: points within delta = 1/2 of p: ['e']; |f(x) - f(p)| there is 0, below every eps.
   The condition 'd(x, p) < delta implies d(f(x), f(p)) < eps' has only x = p to satisfy,
   and it does. Continuity is a property of the map AND the two metrics, never of the map alone.
```
<!-- /output -->

## Questions

**1. Find a δ that works for f(x) = 2x + 1 at p = 5 and a given ε.**

<details><summary>Answer</summary>

δ = ε/2: |f(x) − f(5)| = |2x − 10| = 2 · |x − 5| < 2 · (ε/2) = ε. For a linear function the δ does not depend on p.

</details>

**2. Why did the δ for x² at 3 need the min(1, …)?**

<details><summary>Answer</summary>

To bound the other factor: |x² − 9| = |x − 3| · |x + 3|, and |x + 3| is only bounded once x is kept near 3. Capping δ at 1 keeps x in (2, 4), where |x + 3| < 7. Without the cap, a huge ε would allow a huge δ and the bound 7 would fail.

</details>

**3. Write the negation of "f is continuous at p" with the quantifiers in order.**

<details><summary>Answer</summary>

There exists ε > 0 such that for every δ > 0 there exists x with d(x, p) < δ and d(f(x), f(p)) ≥ ε. One ε, then a witness x for each δ. The step function's witness is x = −δ/2.

</details>

**4. Is the step function continuous at p = 1?**

<details><summary>Answer</summary>

Yes. Near 1 the function is constantly 1: take δ = 1, and every x with |x − 1| < 1 is positive, so |s(x) − s(1)| = 0 < ε. Continuity is checked point by point, and the step fails only at 0.

</details>

**5. Where does the proof that x ↦ d(x, p) is continuous use the triangle inequality?**

<details><summary>Answer</summary>

In the only step there is: d(x, p) ≤ d(x, y) + d(y, p). Rearranged it bounds d(x, p) − d(y, p) by d(x, y), and the symmetric case bounds the other sign. No other metric property is needed.

</details>

**6. The identity from (plane, Euclidean) to (plane, taxicab) is continuous with δ = ε/2. Would δ = ε work?**

<details><summary>Answer</summary>

No. The points (0, 0) and (0.6, 0.6) are at Euclidean distance about 0.85 < 1 = ε but at taxicab distance 1.2 ≥ 1. The factor 2 in taxi ≤ 2 · cheb ≤ 2 · eucl is needed, and δ = ε/√2 would be the sharpest.

</details>

**7. Give a function that is continuous on ℝ with the discrete metric and not with the usual one.**

<details><summary>Answer</summary>

The step function, or any function at all with a jump. Out of a discrete space every function is continuous, since δ = ½ isolates the point. Continuity is a property of the function and the two metrics together.

</details>

## How to practise

1. **Factor the difference.** For a polynomial, write |f(x) − f(p)| as |x − p| times something, bound the something near p, and read δ off.
2. **To disprove, find the jump.** Pick ε smaller than half the jump and write the witness as a formula in δ.
3. **Say which metrics.** "Continuous" is incomplete until the source and target metrics are named; the discrete metric is the reminder.

## Flashcards

The page as a deck of Anki cards: [`continuity.txt`](anki/continuity.txt). Import with File → Import. Tags: `what`, `why`, `trap`, `problems`.

## Where this goes next

[Cauchy sequences and completeness](../completeness/README.md) is the one idea in the chapter that is not about open sets, and the page shows a homeomorphism, which preserves everything on this page, failing to preserve it.

## Po polsku, w skrócie

Funkcja f jest ciągła w punkcie p, gdy dla każdej kuli o promieniu ε wokół f(p) istnieje kula o promieniu δ wokół p, którą f wysyła do środka tamtej: dla każdego ε istnieje δ takie, że d(x, p) < δ pociąga d(f(x), f(p)) < ε. Program znajduje δ dla x² w punkcie 3, δ = min(1, ε/7), a dwie linijki algebry pokazują, dlaczego działa dla każdego x. Zaprzeczenie ciągłości to jedno ε, dla którego żadne δ nie wystarcza: funkcja schodkowa w zerze ma skok wysokości 1, więc dla ε = ½ i każdego δ punkt x = −δ/2 jest świadkiem. Jedno ε i wzór na świadka to cały dowód.

Odległość od ustalonego punktu jest ciągła z δ = ε, bo z nierówności trójkąta |d(x, p) − d(y, p)| ≤ d(x, y). Ciągłość da się też wyrazić zbiorami otwartymi: przeciwobraz zbioru otwartego jest otwarty, więc metryki równoważne mają te same funkcje ciągłe, a identyczność między metryką taksówkową i euklidesową jest ciągła w obie strony, czyli jest homeomorfizmem. Z przestrzeni dyskretnej każda funkcja jest ciągła, bo δ = ½ izoluje punkt i warunek nie ma czego sprawdzać. Wniosek: ciągłość to własność funkcji razem z obiema metrykami, nigdy samej funkcji.

## Auf Deutsch: Stichwörter

Stetigkeit mit ε und δ: eine Kugel um den Ausgabewert, eine Kugel um den Eingabewert, die hineinpasst; geprüft für ε = 1/10, 1/100, 1/1000.

**Stichwörter:** Stetigkeit, ε-δ-Definition, Kugel um f(a), Kugel um a, stetig in einem Punkt, unstetig, Sprungstelle, gleichmäßig stetig.

## See also

- [Convergence](../convergence/README.md) — the same ∀ε ∃ shape, with N in place of δ
- [Open balls](../open_balls/README.md) — the balls this definition sends into each other, and the chain that makes the identity continuous
- [Predicates and quantifiers](../../11_Logic/predicates_and_quantifiers/README.md) — negating ∀ε ∃δ
- [If A then B](../../11_Logic/converse_and_contrapositive/README.md) — one counterexample disproves, which is what one ε does here
- [Velocity equals position](../../09_Calculus/velocity_equals_position/README.md) — the exponential, a continuous function the calculus chapter built without this definition
- [Continuous function ↗](https://en.wikipedia.org/wiki/Continuous_function) — Wikipedia, with the ε-δ, sequence and open-set definitions side by side
