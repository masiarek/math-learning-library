# 14_Metric_Spaces — what analysis needs from a distance

**Level:** 201 · for anyone who has the distance formula and has used the words *limit* and *continuous* without ever being given their definitions

A metric space is a set with a distance on it, nothing more: four properties, no formula. This chapter's claim is that those four properties are all that limits, continuity and completeness ever use. Define them once for an abstract distance and they hold at the same time for the number line, the plane under three different metrics, n dimensions, and spaces whose points are strings or functions. The price is that every definition is written with ε and δ and balls, which is what makes a first analysis course feel like a foreign language; the reward is that every definition can be run, and the programs here run them: they find the N for a given ε, the δ for a given ε, the witness that breaks a false claim, and the Cauchy sequence of rationals with no rational limit.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [Open balls: three metrics, the same open sets](open_balls/README.md) | What is a ball, what is an open set, and why do the Euclidean, taxicab and Chebyshev distances agree on which sets are open? |
| 2 | [Convergence: a limit is a statement about every ball](convergence/README.md) | What does x_n → L say exactly, why is a limit unique, and why does the discrete metric make 1/n stop converging? |
| 3 | [Continuity by ε and δ](continuity/README.md) | What does continuous mean when there is no graph to draw, and how is "not continuous" proved by one ε? |
| 4 | [Cauchy sequences and completeness](completeness/README.md) | How can a sequence be "trying to converge" with nothing to converge to, and why are the reals complete when the rationals are not? |
| 5 | [The triangle inequality proved: Cauchy–Schwarz](cauchy_schwarz/README.md) | Why is the Euclidean distance a metric at all, and what is the one fact its triangle inequality rests on? |

## The through-line

Lesson 1 gives the distance one job: around every point draw the ball of radius r, the points closer than r. A set is open when every point of it keeps some ball inside the set. The three everyday metrics of the plane draw different balls, a disc, a diamond and a square, but each ball of one kind contains a ball of each other kind, so the three agree on which sets are open; they are *equivalent*, and the discrete metric, whose balls are a single point or everything, is not. Lesson 2 defines a limit with the same balls: x_n → L when every ball around L contains a whole tail of the sequence, and the program finds the tail's starting index for each radius. Equivalent metrics give the same limits with different N; the discrete metric makes 1/n stop converging, so convergence is a fact about the metric and not the points. Lesson 3 defines continuity as balls mapped into balls, ∀ε ∃δ, finds a δ for x² and shows the step function has one ε that no δ survives, which is the negation of a ∀∃ as [predicates and quantifiers](../11_Logic/predicates_and_quantifiers/README.md) says it should be. Lesson 4 adds the one idea that is not about open sets: a Cauchy sequence, whose terms approach each other rather than a named limit. Newton's iteration for √2 is Cauchy in ℚ and has no limit there, so ℚ has holes; ℝ is built by filling them, and (0, 1) and ℝ, with the same open sets, differ in exactly this. Lesson 5 pays the debt the whole chapter ran up by calling the Euclidean distance a metric: its triangle inequality follows from a quadratic that is never negative, the Cauchy–Schwarz inequality, and from nothing else.

What this chapter does not do is prove that (0, 1) and ℝ are homeomorphic, or Minkowski's inequality for the other metrics in the p-family, or the construction of ℝ. Each is named where it is used and marked as not proved.

## Po polsku, w skrócie

Przestrzeń metryczna to zbiór z odległością: cztery własności i żaden wzór. Teza rozdziału: granica, ciągłość i zupełność używają tylko tych czterech własności, więc zdefiniowane raz dla abstrakcyjnej odległości działają naraz na prostej, na płaszczyźnie pod trzema różnymi metrykami, w n wymiarach i w przestrzeniach ciągów bitów. Pierwsza lekcja daje odległości jedno zadanie: wokół każdego punktu rysuje kulę, a zbiór jest otwarty, gdy każdy jego punkt ma w nim jakąś kulę. Metryka euklidesowa, taksówkowa i Czebyszewa rysują koło, romb i kwadrat, ale każda kula jednego rodzaju zawiera kulę każdego innego, więc zgadzają się co do zbiorów otwartych: są równoważne. Metryka dyskretna, której kule to jeden punkt albo wszystko, nie jest. Druga lekcja definiuje granicę tymi samymi kulami: x_n → L, gdy każda kula wokół L zawiera cały ogon ciągu; program znajduje indeks, od którego ogon się zaczyna. Pod metryką dyskretną 1/n przestaje zbiegać, więc zbieżność należy do metryki, nie do punktów. Trzecia lekcja to ciągłość przez ε i δ, z funkcją schodkową, której jedno ε nie przepuszcza żadnego δ. Czwarta to ciągi Cauchy'ego i zupełność: iteracja Newtona dla √2 jest ciągiem Cauchy'ego w ℚ bez granicy w ℚ, więc liczby wymierne mają dziury, a ℝ powstaje przez ich wypełnienie; (0, 1) i ℝ mają te same zbiory otwarte, a tylko jedna z nich jest zupełna. Piąta spłaca dług: nierówność trójkąta dla odległości euklidesowej wynika z nierówności Cauchy'ego–Schwarza, a ta z tego, że trójmian kwadratowy, który nigdy nie jest ujemny, ma wyróżnik co najwyżej zero.

## Auf Deutsch: Stichwörter

Was die Analysis von einem Abstand braucht: offene Kugeln, Konvergenz, Stetigkeit und Vollständigkeit allein aus den vier Eigenschaften einer Metrik.

**Stichwörter:** metrischer Raum, Metrik, offene Kugel, offene Menge, Konvergenz, Grenzwert, Stetigkeit, Cauchy-Folge, Vollständigkeit, Cauchy-Schwarz-Ungleichung.

## A note on the code

Every definition in this chapter has a ∀ε and a ∃N or ∃δ in it, and a program cannot loop over all ε. What it can do is take the ε a reader would ask about, 1/10, 1/100, 1/1000, and produce the N or the δ with the inequality that justifies it for every n or x, then check a window of values as a test that the inequality was copied right. For a negative claim, that a sequence does not converge or a function is not continuous, the program produces the one ε and the witness for each δ, which is a proof. All arithmetic is in exact fractions, with distances compared through their squares, so no output depends on floating point; √2 to twelve decimals is `isqrt(2 · 10²⁴)`.
