# Ramsey's theorem: the pigeonhole principle for pairs

**Level:** 201 · for anyone who has asked how combinatorics, the art of counting, can be relevant to sets

**One line:** Ten pigeons in nine holes crowd a hole; colour every pair from six points with two colours and three points appear whose pairs are all one colour; colour every pair of natural numbers and an infinite such set appears. Each statement is the previous one with "pair" in place of "point", each is about which sets are big enough to force a pattern, and the program checks the finite one by exhaustion, runs the proof of the infinite one as an algorithm, and shows the tree argument that ties them together. For finite sets the answer is a number; for infinite sets it depends on the axioms, and that is why a book called *Combinatorial Set Theory* exists.

## The question

Lorenz Halbeisen opens his book with a definition: combinatorics deals with collections of objects that satisfy some criteria, and asks how large or how small such a collection can be. Nothing in that sentence says "finite". The owner's reaction, "how the heck can combinatorics be relevant to sets?", has a one-word answer, Ramsey, and this page is the long version.

The [pigeonhole principle](../../GLOSSARY.md#pigeonhole-principle) is the first fact of combinatorics: more pigeons than holes, so some hole holds two. The program's section 1 checks it on every one of the 81 maps from four pigeons to three holes. The infinite version is just as plain: infinitely many pigeons in finitely many holes, so some hole holds infinitely many.

Now replace points by pairs. Take six points and colour each of the 15 pairs red or blue, in any way. Then some three points have all three of their pairs the same colour. Five points do not suffice: colour the pairs of a pentagon red when they are sides and blue when they are diagonals, and no triangle is one colour. The smallest number that works, 6, is the [Ramsey number](../../GLOSSARY.md#ramsey-s-theorem) R(3, 3). Section 3 checks all 2¹⁵ = 32 768 colourings of the six points and exhibits the pentagon.

The proof is a pigeonhole argument, and the program runs it as a procedure rather than reading it as a sentence. Pick one point. Five pairs leave it, in two colours, so three of them share a colour, say red. Look at the three far ends. If any pair among them is red, it closes a red triangle with the first point; if none is, the three far ends are a blue triangle. Section 3 reports that this procedure finds a one-colour triangle in all 32 768 colourings.

## The infinite theorem, run as an algorithm

Frank Ramsey proved in 1930 that colouring every pair of natural numbers with finitely many colours leaves an infinite set all of whose pairs are one colour; and the same for triples, quadruples, any fixed size. He needed it for a problem in logic, a decision procedure for a fragment of first-order logic, which is the first sign that the theorem is not about counting.

The proof is the pigeonhole principle applied over and over. Take the least number, a₀. The other numbers split by the colour of their pair with a₀, and one part is infinite; keep that part and remember the colour a₀ saw. Take its least member, a₁, and repeat inside the part. The sequence a₀, a₁, a₂, … is infinite, each aᵢ saw one colour, and by pigeonhole once more infinitely many of them saw the same colour. Those form the set: any pair aᵢ < aⱼ from it has the colour aᵢ saw. Section 5 runs this on the numbers 1 to 64, colouring a pair red when the smaller divides the larger, and finds the chain 1, 2, 4, 8, 16, 32, 64, all pairs red. On ℕ "keep the larger part" becomes "keep the infinite part", which is the only step a program cannot take.

## Finite from infinite: König's lemma

The finite theorem follows from the infinite one by an argument about trees, and the program draws the tree. A colouring of the pairs of {0, …, n−1} with no one-colour triangle restricts to one of {0, …, n−2} with the same property, so the bad colourings form a tree with one level per n, and each node has finitely many children. Section 4 counts the levels: 1, 2, 6, 18, 12, 0. The tree dies at level 6, which is R(3, 3) again.

[König's lemma](../../GLOSSARY.md#konig-s-lemma) says that an infinite tree in which every node has finitely many children has an infinite branch. If the tree of bad colourings had a node at every level, the lemma would give an infinite branch, which is a colouring of all pairs of ℕ with no one-colour triangle, and the infinite theorem says there is none. So the tree is finite, and the level where it dies is the Ramsey number. This is the pattern called compactness: a property of the infinite set forces a bound on finite sets, without saying what the bound is.

The same pigeonhole, pushed one step further, gives the theorem of Erdős and Szekeres from 1935: among n² + 1 distinct numbers in any order there is a monotone run of n + 1. Section 2 checks it for n = 2 on all 120 orderings of five numbers, and finds the four orderings of four numbers that avoid it.

## Why this is set theory

A colouring of pairs is a [partition](../../GLOSSARY.md#partition) of the set of 2-element subsets, and Halbeisen writes the theorem in Erdős and Rado's arrow notation: κ → (λ)ⁿ_r means that whenever the n-element subsets of a set of size κ are split into r pieces, some subset of size λ has all its n-element subsets in one piece. Section 3 proves 6 → (3)²₂ and 5 ↛ (3)²₂; Ramsey's theorem is ω → (ω)ⁿ_r. The statement is about sets and their sizes, nothing else.

Then the sizes go up, and the ground moves. Sierpiński showed in 1933 that the first uncountable cardinal fails: ω₁ ↛ (ω₁)²₂, by colouring pairs of reals according to whether a well-ordering of the reals agrees with the usual order, a construction that needs the [axiom of choice](../../13_Axioms_of_Set_Theory/choice/README.md). A cardinal κ with κ → (κ)²₂ is called weakly compact, and ZFC cannot prove that one exists: it is a large cardinal, the first rung of the ladder the [reading guide](../../reading_guides/set_theory/README.md#beyond-zfc-the-map-in-wikipedias-article) describes. So the question "how large must a set be for this pattern to be forced", which for finite sets is settled by a number and a computer, for infinite sets runs straight into the axioms. That is what combinatorial set theory is, and section 6 lays the five statements side by side with a column saying which of them a program can check.

For contrast, the finite side has its own wall: R(5, 5) is unknown, somewhere between 43 and 46 by the results this page recalls from memory, and checking 43 points by exhaustion would mean 2⁹⁰³ colourings. Erdős's story about it, that if aliens demanded R(5, 5) we should put every computer on it and if they demanded R(6, 6) we should attack, is about the finite theorem.

## What the program prints

<!-- output:ramsey -->
*Verified output of [`ramsey.py`](examples/ramsey.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. THE PIGEONHOLE PRINCIPLE: MORE PIGEONS THAN HOLES
   maps from 4 pigeons to 3 holes: 81; with some hole holding two or more: 81
   The same for infinitely many pigeons in finitely many holes: some hole
   holds infinitely many. That is the one-colour case of what follows.

2. ERDŐS AND SZEKERES: EVERY FIVE NUMBERS HOLD A MONOTONE THREE
   orderings of 1..5: 120; with an increasing or decreasing run of 3: 120
   orderings of 1..4 with no monotone run of 3: 4, e.g. (2, 1, 4, 3) and (2, 4, 1, 3)
   In general n² + 1 numbers force a monotone run of n + 1 (1935). It is a
   pigeonhole statement about the set of pairs: colour each pair {i < j}
   'up' if the later number is larger, and ask for a one-colour set.

3. R(3, 3) = 6: SIX POINTS FORCE A ONE-COLOUR TRIANGLE, FIVE DO NOT
   2-colourings of the 15 edges of K6: 32768; with a one-colour triangle: 32768
   triangles found by the pigeonhole procedure (pick a point, 5 edges, 2 colours,
   so 3 edges agree; among their far ends any edge of that colour closes a
   triangle, else the three form one of the other colour): 32768
   K5 coloured by distance round a pentagon (1 or 4 red, 2 or 3 blue):
   one-colour triangle: None
   So the Ramsey number R(3, 3) is exactly 6. In Halbeisen's arrow notation,
   6 → (3)²₂ and 5 ↛ (3)²₂: 'colour the 2-subsets of a 6-set with 2 colours
   and a 3-subset has all its 2-subsets one colour'.

4. THE TREE OF BAD COLOURINGS DIES, WHICH IS KÖNIG'S LEMMA IN REVERSE
   n = 1: colourings of K1 with no one-colour triangle: 1
   n = 2: colourings of K2 with no one-colour triangle: 2
   n = 3: colourings of K3 with no one-colour triangle: 6
   n = 4: colourings of K4 with no one-colour triangle: 18
   n = 5: colourings of K5 with no one-colour triangle: 12
   n = 6: colourings of K6 with no one-colour triangle: 0
   Each bad colouring of K_n restricts to a bad colouring of K_{n-1}, so the
   bad colourings form a tree, finitely branching, one level per n. König's
   lemma: an infinite finitely branching tree has an infinite branch. An
   infinite branch here would colour all pairs of ℕ with no one-colour
   triangle, which the infinite theorem (section 5) forbids. So the tree is
   finite, and the level where it dies is the Ramsey number.

5. THE INFINITE THEOREM AS AN ALGORITHM (RAMSEY 1930)
   points 1..64; the pair {i < j} is red when i divides j, blue otherwise
   step: take the least point left, split the rest by its colour with that
   point, keep the larger part (on ℕ: the infinite part, by pigeonhole)
   chosen points and the colour each sees ahead:
   1:r, 2:r, 4:r, 8:r, 16:r, 32:r
   the points that saw red, plus what is left: [1, 2, 4, 8, 16, 32, 64]
   all 21 pairs among them red: True
   On ℕ the chosen sequence is infinite; infinitely many of its points see the
   same colour (pigeonhole again), and they are an infinite one-colour set.
   Ramsey proved this for n-element subsets and any finite number of colours.

6. WHY THIS IS SET THEORY: THE ANSWER DEPENDS ON THE SET
   statement      what it says                                         can a program check it?
   6 → (3)²₂      finite, checked above                                yes, by exhaustion
   ω → (ω)ⁿ_k     Ramsey 1930, proof in section 5                      the algorithm, not the limit
   ω₁ ↛ (ω₁)²₂    Sierpiński 1933: the first uncountable set fails     no: it needs the reals well-ordered
   κ → (κ)²₂      defines a weakly compact cardinal (a large cardinal) no: ZFC cannot prove one exists
   R(5, 5) = ?    between 43 and 46 (from memory, 2024)                no: 2^(C(43,2)) colourings
   A colouring of pairs is a partition of the set of 2-subsets, and the theorem
   asks which sets are big enough that some partition piece contains all the
   pairs of a big subset. For finite sets the answer is a number; for infinite
   sets it depends on the axioms. That is Halbeisen's reason for calling the
   subject combinatorial set theory.
```
<!-- /output -->

## Po polsku, w skrócie

Zasada szufladkowa: więcej gołębi niż szufladek, więc w którejś siedzą dwa. Twierdzenie Ramseya to ta sama zasada dla par: pokoloruj każdą z 15 par sześciu punktów na czerwono lub niebiesko, a znajdą się trzy punkty, których wszystkie trzy pary mają jeden kolor; dla pięciu punktów tak nie jest (boki pięciokąta czerwone, przekątne niebieskie). Liczba Ramseya R(3, 3) = 6, a program sprawdza wszystkie 32 768 kolorowań. Wersja nieskończona (Ramsey 1930): pokoloruj wszystkie pary liczb naturalnych, a istnieje nieskończony zbiór o parach jednego koloru; dowód to zasada szufladkowa stosowana w kółko, i program wykonuje go jako algorytm na liczbach od 1 do 64. Wersję skończoną wyprowadza się z nieskończonej przez lemat Königa o drzewach: drzewo „złych" kolorowań ma poziomy 1, 2, 6, 18, 12, 0 i umiera na poziomie 6. Dlaczego to teoria mnogości? Bo pytanie „jak duży musi być zbiór, żeby wzór był wymuszony" dla zbiorów skończonych ma odpowiedź liczbową, a dla nieskończonych zależy od aksjomatów: ω₁ już nie ma tej własności (Sierpiński 1933), a kardynał κ z κ → (κ)²₂ to duży kardynał, którego istnienia ZFC nie dowodzi. Stąd nazwa książki Halbeisena: kombinatoryczna teoria mnogości.

## Auf Deutsch: Stichwörter

Ramseys Satz als Schubfachprinzip für Paare: unter sechs Personen kennen sich drei oder drei kennen sich nicht; alle Färbungen durchprobiert.

**Stichwörter:** Satz von Ramsey, Schubfachprinzip (pigeonhole), Färbung, vollständiger Graph K₆, Clique, unabhängige Menge, Ramsey-Zahl R(3,3) = 6.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 04_Sets/ramsey/examples/ramsey.py
```

## See also

- [Equivalence relations and partitions](../equivalence_and_partitions/README.md) — a colouring of pairs is a partition of the set of pairs
- [Orderings](../orderings/README.md) — chains and antichains; the divisibility order whose chains the algorithm finds
- [Choice](../../13_Axioms_of_Set_Theory/choice/README.md) — the axiom behind Sierpiński's counterexample
- [Induction](../../11_Logic/induction/README.md) — the finite pigeonhole principle is proved by it
- [The reading guide](../../reading_guides/set_theory/README.md#the-subject-graduate-and-research) — Halbeisen's *Combinatorial Set Theory*, whose Part II opens with this theorem
- Lorenz Halbeisen, *Combinatorial Set Theory*, 3rd ed. (Springer, 2025), chapter 1 (the definition of combinatorics) and chapter 4 (Ramsey's theorem)
- [Ramsey's theorem ↗](https://en.wikipedia.org/wiki/Ramsey%27s_theorem) and [König's lemma ↗](https://en.wikipedia.org/wiki/K%C5%91nig%27s_lemma) — Wikipedia
