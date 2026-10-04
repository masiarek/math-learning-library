# Open balls: three metrics, the same open sets

**Level:** 201 · for anyone who has met a second distance besides the Euclidean one and wants to know what changes

**One line:** A distance has one job in analysis, to draw the ball of radius r around every point; a set is open when each of its points keeps a ball inside it; and because every Euclidean ball contains a taxicab ball and a Chebyshev ball and is contained in one, the three metrics draw different balls but agree on every open set, which is what makes them equivalent, while the discrete metric, whose balls are a point or everything, is not.

## The ball

In a [metric space](../../GLOSSARY.md#metric-space), the **open ball** of radius r around p is the set of points closer than r to p:

> **B(p, r) = {x : d(p, x) < r}**

Strict inequality: the edge is not in the ball. In the plane the Euclidean ball is a disc without its rim, the [taxicab](../../GLOSSARY.md#taxicab-distance) ball a diamond and the [Chebyshev](../../GLOSSARY.md#chebyshev-distance) ball a square, the three circles of [distance is the four properties](../../08_Analytic_Geometry/other_distances/README.md) with their insides. Section 1 of the program draws all three on lattice points, and the point (2, 0), at Euclidean distance exactly 2 from the origin, is left out of the ball of radius 2 by all of them.

Everything the chapter defines, a limit, a continuous function, a Cauchy sequence, is a sentence about balls. So the first question is which facts about balls depend on the metric and which do not.

## Open sets

A set U is **open** when every point of U has some ball around it that lies inside U: for every p in U there is an r > 0 with B(p, r) ⊆ U. The open disc x² + y² < 9 is open; the closed disc x² + y² ≤ 9 is not, because a point on the rim has every ball around it poking outside. A ball is itself open, which takes the triangle inequality to prove: if x is in B(p, r) then B(x, r − d(p, x)) fits inside B(p, r).

The definition quantifies over balls, so it looks as if it depends on which balls the metric draws. Section 4 takes one open set, the Euclidean disc of radius 3, and one of its points, (2, 1), and finds a ball of each of the three kinds that fits inside, checked on a grid of step 1/20. That is one point of one set; the theorem behind it is the next section.

## Within a factor of 2

Write a = |x₂ − x₁| and b = |y₂ − y₁| for the two changes between two points. Then the three distances are max(a, b), √(a² + b²) and a + b, and three one-line inequalities hold for every a, b ≥ 0:

| Inequality | Because |
|---|---|
| max(a, b)² ≤ a² + b² | one square is at most the sum of both |
| a² + b² ≤ (a + b)² | the cross term 2ab is not negative |
| a + b ≤ 2 max(a, b) | each of a and b is at most the larger |

So **cheb ≤ eucl ≤ taxi ≤ 2 · cheb** on every pair of points. Section 2 checks the chain on 2 401 pairs with the Euclidean distance compared through its square, so nothing is rounded; the three lines are the proof and the grid is the check that they were copied right.

Read as statements about balls, the chain says the balls nest, section 3:

> **B_taxi(p, r) ⊆ B_eucl(p, r) ⊆ B_cheb(p, r) ⊆ B_taxi(p, 2r)**

A point closer than r in taxicab distance is closer than r in Euclidean distance, because eucl ≤ taxi; and so on round the chain. Now the theorem: if U is open under one of the three metrics it is open under the others. Say U is Euclidean-open and p ∈ U, so some B_eucl(p, r) ⊆ U. Then B_taxi(p, r) ⊆ B_eucl(p, r) ⊆ U, so U is taxicab-open; and B_cheb(p, r/2) ⊆ B_taxi(p, r) ⊆ U, so U is Chebyshev-open. The other directions are the same chain read from a different link. Two metrics that give the same open sets are called **equivalent**, and the nesting is the standard way to prove it: each ball of one kind contains a ball of the other kind around the same centre.

Nothing in that argument used the number 2. Any two metrics with c · d₁ ≤ d₂ ≤ C · d₁ for constants c, C > 0 are equivalent, which covers the whole family (|Δx|ᵖ + |Δy|ᵖ)^(1/p) for p ≥ 1 and every norm on ℝⁿ.

## The discrete metric, which is not equivalent

Section 5 is the metric with d(p, q) = 1 for p ≠ q and d(p, p) = 0. Its ball of radius ½ around p is {p} and its ball of radius 2 is the whole space; there is nothing in between. So every subset is open: each point has the ball of radius ½, which is the point itself, inside any set that contains it. Under the Euclidean metric no set consisting of one point is open, because every Euclidean ball of positive radius contains other points, p + (r/2, 0) for one. The two metrics disagree on an open set, so they are not equivalent, and no constants c, C can relate them: 1 ≤ C · eucl(p, q) fails as q approaches p.

The discrete metric is the chapter's control experiment. It has the four properties, the triangle inequality being 1 ≤ 1 + 1 at worst, and every later lesson will run its definition on it to see what a metric can do when it draws no interesting balls at all.

## What the program prints

<!-- output:open_balls -->
*Verified output of [`open_balls.py`](examples/open_balls.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. THE OPEN BALL OF RADIUS 2 AROUND THE ORIGIN, UNDER THREE METRICS
   Lattice points with -3 <= x, y <= 3; # marks a point at distance LESS THAN 2.
   Euclidean   taxicab     Chebyshev
   .......     .......     .......
   .......     .......     .......
   ..###..     ...#...     ..###..
   ..###..     ..###..     ..###..
   ..###..     ...#...     ..###..
   .......     .......     .......
   .......     .......     .......
   Strict inequality: the boundary is not in the ball. (2, 0) is at Euclidean distance
   exactly 2 from the origin and is left out of all three.

2. THE THREE METRICS ARE WITHIN A FACTOR OF 2 OF EACH OTHER, ON EVERY PAIR
   cheb <= eucl <= taxi <= 2 cheb, compared as squares on 2401 pairs: True
   The proof is three lines, with a = |dx| and b = |dy|:
     max(a, b)^2 <= a^2 + b^2            one square is at most the sum of both;
     a^2 + b^2 <= (a + b)^2               the cross term 2ab is not negative;
     a + b <= 2 max(a, b)                 each of a, b is at most the max.
   The grid is a check that the lines were copied right; the lines hold for every a, b.

3. THE BALLS NEST: B_taxi(p, r) inside B_eucl(p, r) inside B_cheb(p, r) inside B_taxi(p, 2r)
   r = 5/2, lattice points in each: taxi 13, eucl 21, cheb 25, taxi with 2r 41
   taxi <= eucl <= cheb <= taxi(2r) as sets: True
   Each inclusion is one line of section 2 read as a statement about balls:
   taxi(p, q) < r forces eucl(p, q) < r, because eucl <= taxi; and so on round.

4. ONE OPEN SET, ONE OF ITS POINTS, AND A BALL OF EACH KIND THAT FITS
   U = the Euclidean open disc x^2 + y^2 < 9. Take p = (2, 1), which is in U: 4 + 1 = 5 < 9.
   The Euclidean distance from p to the edge is 3 - sqrt(5), about 0.764; choose r = 7/10.
   B_taxi(p, 7/10):  365 grid points of step 1/20, all inside U: True
   B_Chebyshev(p, 7/20):  169 grid points of step 1/20, all inside U: True
   B_Euclidean(p, 7/10):  609 grid points of step 1/20, all inside U: True
   One point of one set, checked on a grid: evidence. The theorem is section 3:
   a ball of one kind inside U contains a ball of each other kind, so 'open' means the
   same thing under all three metrics. They are EQUIVALENT metrics.

5. THE DISCRETE METRIC: d(p, q) = 1 FOR p != q, AND 0 FOR p = q
   B(a, 1/2) = ['a']
   B(a, 1) = ['a']
   B(a, 2) = ['a', 'b', 'c', 'd', 'e']
   A ball is one point or everything, so every subset is open: every point of any set
   has the ball of radius 1/2 around it inside the set. This metric is a metric (the
   four properties hold; the triangle inequality is 1 <= 1 + 1 at worst) and it is NOT
   equivalent to the Euclidean one: no Euclidean ball of positive radius is a single point,
   since B_eucl(p, r) contains p + (r/2, 0).
```
<!-- /output -->

## Questions

**1. Is (1, 1) in the Euclidean ball of radius 3/2 around the origin? In the taxicab ball? In the Chebyshev ball?**

<details><summary>Answer</summary>

Euclidean: 1 + 1 = 2 < 9/4, yes. Taxicab: 1 + 1 = 2 < 3/2, no. Chebyshev: max(1, 1) = 1 < 3/2, yes. The three balls are different sets; what they share is the open sets they generate.

</details>

**2. Why is the open ball itself an open set?**

<details><summary>Answer</summary>

Take x in B(p, r) and let s = r − d(p, x) > 0. If d(x, y) < s then d(p, y) ≤ d(p, x) + d(x, y) < d(p, x) + s = r, so B(x, s) ⊆ B(p, r). The triangle inequality is the whole proof, and it is the first place the fourth metric property earns its keep.

</details>

**3. Is the set {(x, y) : x² + y² ≤ 9} open?**

<details><summary>Answer</summary>

No. The point (3, 0) is in it, and every ball around (3, 0), of any radius r, contains (3 + r/2, 0), which is not. One point with no ball inside is enough, since "open" says every point has one.

</details>

**4. The chain says taxi ≤ 2 · cheb. Which pair of points makes it an equality?**

<details><summary>Answer</summary>

Any pair with a = b, such as (0, 0) and (1, 1): taxicab 2, Chebyshev 1. The factor 2 cannot be improved, which is why the Chebyshev ball needs radius r/2 to fit inside the taxicab ball of radius r.

</details>

**5. Prove that if U is open under the taxicab metric it is open under the Chebyshev metric.**

<details><summary>Answer</summary>

Let p ∈ U with B_taxi(p, r) ⊆ U. Since taxi ≤ 2 · cheb, a point with cheb(p, x) < r/2 has taxi(p, x) < r, so B_cheb(p, r/2) ⊆ B_taxi(p, r) ⊆ U. Every point of U has a Chebyshev ball inside U.

</details>

**6. Under the discrete metric on the plane, is the single point {(0, 0)} an open set? Under the Euclidean metric?**

<details><summary>Answer</summary>

Discrete: yes, B((0, 0), ½) = {(0, 0)}. Euclidean: no, every ball around the origin contains (r/2, 0). The two metrics disagree on this set, so they are not equivalent.

</details>

**7. Two metrics satisfy d₂ ≤ 5 · d₁ but there is no constant with d₁ ≤ C · d₂. Can they be equivalent?**

<details><summary>Answer</summary>

Not by the chain argument, and in general no: a d₁-open set need not be d₂-open. The one-sided bound gives only that every d₂-open set is d₁-open. The discrete metric against the Euclidean one is an example: eucl ≤ C · disc holds on a bounded region, and the reverse fails.

</details>

## How to practise

1. **Draw the ball first.** For a new metric, sketch B(0, 1) before anything else; the shape tells you most of what the metric will do.
2. **Nest the balls to prove equivalence.** Two inequalities, c · d₁ ≤ d₂ ≤ C · d₁, and the chain argument above does the rest.
3. **To show a set is not open, find the one point.** A point on the rim with a ball that pokes out is a complete proof.

## Flashcards

The page as a deck of Anki cards: [`open_balls.txt`](anki/open_balls.txt). Import with File → Import. Tags: `what`, `why`, `trap`, `problems`.

## Where this goes next

[Convergence](../convergence/README.md) is the first definition written with balls: a tail of the sequence inside every ball around the limit. The nesting of this page is why equivalent metrics have the same limits, and the discrete metric is why 1/n can stop converging.

## Po polsku, w skrócie

Kula otwarta o promieniu r wokół p to zbiór punktów odległych od p o mniej niż r; brzeg do niej nie należy. Zbiór jest otwarty, gdy każdy jego punkt ma wokół siebie jakąś kulę zawartą w zbiorze. Trzy metryki płaszczyzny rysują trzy różne kule: koło, romb i kwadrat. Mimo to zgadzają się co do zbiorów otwartych, bo zachodzi łańcuch cheb ≤ eucl ≤ taxi ≤ 2·cheb, udowodniony trzema linijkami i sprawdzony przez program na 2401 parach punktów dokładnie, przez kwadraty odległości. Łańcuch czytany jako zdanie o kulach mówi, że kule są zagnieżdżone: taksówkowa w euklidesowej, euklidesowa w kuli Czebyszewa, ta w taksówkowej o podwójnym promieniu. Jeśli więc punkt ma w zbiorze kulę jednego rodzaju, ma też kulę każdego innego, i „otwarty" znaczy to samo pod każdą z trzech metryk. Takie metryki nazywamy równoważnymi.

Metryka dyskretna, d = 1 dla różnych punktów, ma kule będące jednym punktem albo wszystkim, więc każdy podzbiór jest otwarty; pod metryką euklidesową żaden jednopunktowy zbiór otwarty nie jest. Te dwie metryki nie są równoważne i żadne stałe ich nie wiążą. Metryka dyskretna jest w tym rozdziale eksperymentem kontrolnym: każda kolejna definicja zostanie na niej uruchomiona.

## Auf Deutsch: Stichwörter

Drei Metriken, dieselben offenen Mengen: Kugeln sind Scheibe, Raute und Quadrat, aber jede passt in jede.

**Stichwörter:** offene Kugel, offene Menge, innerer Punkt, euklidische Metrik, Manhattan-Metrik, Maximumsmetrik, äquivalente Metriken, diskrete Metrik, Topologie.

## See also

- [Distance is the four properties](../../08_Analytic_Geometry/other_distances/README.md) — the three circles whose insides are these balls, and the four axioms
- [Distance in n dimensions](../../08_Analytic_Geometry/distance_in_n_dimensions/README.md) — the Euclidean metric in any number of coordinates, where the same chain holds with 2 replaced by √n
- [Convergence](../convergence/README.md) — the first definition built from balls
- [Predicates and quantifiers](../../11_Logic/predicates_and_quantifiers/README.md) — "for every point there is a radius" as a ∀∃, and what its negation says
- [Open set ↗](https://en.wikipedia.org/wiki/Open_set) — Wikipedia, with the general definition and pictures of balls in several metrics
- [Equivalence of metrics ↗](https://en.wikipedia.org/wiki/Equivalence_of_metrics) — Wikipedia, with the strong and weak forms of equivalence
