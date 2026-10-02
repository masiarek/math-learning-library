# Induction: a base case, a step that runs forever, and the least counterexample

**Level:** 101 → 201 · for anyone who has seen "assume P(n), prove P(n + 1)" and wondered why that is allowed, or has met the proof that all cars are the same colour and not found the hole

**One line:** A proof by induction shows one case and shows that each case forces the next, and is valid because of the well-ordering principle: if the claim failed anywhere it would fail *first* somewhere, and a step that always works forbids a first failure; so a false claim has a least counterexample, which a program can find, and a true one has none, which only the algebra of the step can show.

## What induction claims

Let P(n) be a statement about the natural number n: "1 + 2 + ⋯ + n = n(n + 1)/2", "n² ≥ 2n", "the Fibonacci number f(3n) is even". **Mathematical induction** says: if P(0) is true, and whenever P(n) is true so is P(n + 1), then P(n) is true for every n. Ashlock, whose chapter 2 this page follows, states it as Theorem 2.1 and gives the three-part recipe: a **base case**, directly checked; the **induction hypothesis**, that P(n) holds for some n; and the **inductive step**, that P(n + 1) then follows. The base case can start at any k instead of 0, and the conclusion is then P(n) for n ≥ k.

Section 1 of the program runs the two checks for the sum formula on n up to 200 and finds nothing wrong. That is evidence, and the page on [truth tables](../truth_tables_and_laws/README.md) says why evidence of this kind is never a proof: a finite range cannot speak for all n. The proof is the algebra of the step, n(n + 1)/2 + (n + 1) = (n + 1)(n + 2)/2, which holds for the letter n and so for every value at once. The program checks the algebra too, on a range, which is a check that the algebra was copied right.

## Why it works: the least counterexample

Induction is not an axiom here; it is a theorem, and its proof is the one idea worth keeping. The **well-ordering principle** says every nonempty set of natural numbers has a least member. Suppose the base case and the step both hold, and let S be the set of n for which P(n) fails. If S is nonempty it has a least member m. Then m ≠ 0, because P(0) holds. So m − 1 is a natural number not in S, so P(m − 1) holds, so by the step P(m) holds, so m ∉ S. That contradicts m ∈ S, so S is empty: P(n) holds for all n. This is Ashlock's proof of Theorem 2.1, and it is a **proof by contradiction**: assume the opposite, derive something impossible.

Section 2 shows the idea on a claim that is false: n² + n + 41 is prime for every n. It is true for n from 0 to 39, and the program finds the least counterexample, n = 40, where the value is 41 · 41. For that claim the step from P(39) to P(40) is false, which is why no proof of the step exists. For a true claim the search for a least counterexample finds nothing, and the step is where the proof has to be. Well-ordering and induction are two forms of one principle; the [ordinals](../../13_Axioms_of_Set_Theory/ordinals/README.md) page takes well-ordering past the finite numbers, and the [axiom of infinity](../../13_Axioms_of_Set_Theory/infinity/README.md) is what makes "the set of n for which P(n) holds is inductive, so it is all of ℕ" a sentence about a set.

## The famous wrong proof

Ashlock's Problem 2.41: all cars are the same colour. Base case, one car has one colour. Step: in any set of n + 1 cars, number them, and the sets {1, …, n} and {2, …, n + 1} each have n cars, so each is one colour by hypothesis, and car n is in both, so the two colours are the same. Where is the hole? Section 3 computes the overlap for n = 1, 2, 3, 4. For n = 1 the two sets are {1} and {2}, and they do not overlap, so nothing forces the two colours to agree. The step is valid for every n ≥ 2 and false for n = 1, and one missing rung is enough: the conclusion for 2 cars was never established, and every larger case stands on it. The lesson is the one that catches most wrong inductions: check that the step really works at the smallest n it is used for, not only "in general".

## Induction at work

Sections 4 to 7 run the chapter's examples, each a step worth reading aloud.

- **Fibonacci.** f(3n) is even: the step is f(3n + 3) = f(3n + 2) + f(3n + 1) = 2f(3n + 1) + f(3n), even plus even. The same shape gives f(4n) divisible by 3 and f(5n) by 5 (Problems 2.35 and 2.37). **Binet's formula** (Problem 2.38) writes f(n) as (φⁿ − ψⁿ)/√5 with φ = (1 + √5)/2 and ψ = (1 − √5)/2; the program computes it exactly in numbers of the form a + b√5 with rational a, b, and the √5 part cancels to give f(30) = 832 040 with no rounding. Since |ψ|ⁿ/√5 < ½ from n = 2 on, f(n) is the integer nearest φⁿ/√5 (Problem 2.39).
- **2ⁿ subsets** (Proposition 2.3). Pick a member x of an (n + 1)-set; the subsets without x are the subsets of an n-set, 2ⁿ by hypothesis, and each pairs with exactly one subset with x, so there are 2ⁿ + 2ⁿ = 2ⁿ⁺¹. Section 5 counts both halves for n up to 5. [Cardinality of sets](../../04_Sets/cardinality/README.md) and [the power set axiom](../../13_Axioms_of_Set_Theory/power_set/README.md) use the same count.
- **The chocolate bar** (Problem 2.28). A bar of n × m squares needs exactly nm − 1 breaks, in any order, because every break turns one piece into two: pieces = breaks + 1 is an invariant, and 24 pieces need 23 breaks. Section 6 breaks a 6 × 4 bar by two different strategies and gets 23 both times. As an induction on the number of squares k: a break splits k into a + b, and (a − 1) + (b − 1) + 1 = k − 1.
- **Closed forms** (Definition 2.14, Problems 2.26 and 2.31). Σi = n(n + 1)/2, Σi² = n(n + 1)(2n + 1)/6, Σi³ = (n(n + 1)/2)², each a one-step induction, and because Σ is linear, Σ(i² + 3i + 5) is the sum of three known closed forms. Section 7 checks all four.

## What it is for

Induction is the proof method of anything defined by recursion: the natural numbers themselves (the successor x ∪ {x} of [the axiom of infinity](../../13_Axioms_of_Set_Theory/infinity/README.md)), sequences, sums, trees, formulas, programs. A loop with an invariant is an induction on the number of iterations, which is why the chocolate bar argument is also how a programmer proves a loop correct. Structural induction on formulas is how every theorem about all formulas in [the axioms chapter](../../13_Axioms_of_Set_Theory/README.md) is proved; transfinite induction along the [ordinals](../../13_Axioms_of_Set_Theory/ordinals/README.md) is the same method with "least counterexample" read in a well-ordering beyond ℕ; and Goodstein's theorem on that page is the example of a statement about ordinary integers for which induction up to ω is not enough.

## What the program prints

<!-- output:induction -->
*Verified output of [`induction.py`](examples/induction.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. THE TWO CHECKS, RUN ON A RANGE:  1 + 2 + ... + n = n(n + 1)/2
   base case P(1): True
   step: n(n+1)/2 + (n+1) == (n+1)(n+2)/2 for n = 0..199: True
   and P(n) itself for n = 1..200: True
   The range is evidence. The proof is the algebra of the step, which
   holds for the letter n, not for 200 values of it.

2. WHY IT WORKS: A FALSE CLAIM HAS A LEAST COUNTEREXAMPLE, A STEP FORBIDS ONE
   claim: n² + n + 41 is prime for every n.  true for n = 0..39, and
   the least counterexample is n = 40: 40² + 40 + 41 = 1681 = 41 · 41.
   so the step P(39) → P(40) is false: there is no proof of it to find.
   Well-ordering: every nonempty set of natural numbers has a least member.
   If the set of failures were nonempty it would have a least member m;
   m ≠ 0 by the base case, so P(m − 1) holds and the step gives P(m):
   contradiction. So the set of failures is empty. That is the whole proof
   that induction is a valid method.

3. WHERE THE 'ALL CARS ARE THE SAME COLOUR' PROOF BREAKS
   the step: in a set of n + 1 cars, {1..n} and {2..n+1} each have n cars,
   so each is one colour by hypothesis, and they overlap, so the colours agree.
   n = 1: [1] and [2] overlap in ∅   <- no overlap: the step from 1 car to 2 fails
   n = 2: [1, 2] and [2, 3] overlap in [2]
   n = 3: [1, 2, 3] and [2, 3, 4] overlap in [2, 3]
   n = 4: [1, 2, 3, 4] and [2, 3, 4, 5] overlap in [2, 3, 4]
   The base case is fine and the step is fine for n ≥ 2; it is false for
   n = 1, and one missing rung is enough. Every car after that stands on it.

4. FIBONACCI: f(3n) EVEN, f(4n) DIVISIBLE BY 3, f(5n) BY 5; BINET EXACTLY
   f(3n) % 2 == 0 for n ≤ 30: True   f(4n) % 3 == 0: True   f(5n) % 5 == 0: True
   the step for f(3n) even: f(3n+3) = f(3n+2) + f(3n+1) = 2 f(3n+1) + f(3n), even + even.
   Binet, computed in a + b√5 with exact fractions: f(30) = 832040 + 0√5  (the √5 part cancels)
   f(30) by addition: 832040   equal: True
   f(n) is the integer nearest φⁿ/√5 for n = 2..59: True   (|ψ|ⁿ/√5 < 1/2 from n = 2)

5. A SET OF n MEMBERS HAS 2ⁿ SUBSETS: THE PAIRING STEP, COUNTED
   n = 1:  2 subsets = 1 containing 1 + 1 not = 2 · 2^0
   n = 2:  4 subsets = 2 containing 2 + 2 not = 2 · 2^1
   n = 3:  8 subsets = 4 containing 3 + 4 not = 2 · 2^2
   n = 4: 16 subsets = 8 containing 4 + 8 not = 2 · 2^3
   n = 5: 32 subsets = 16 containing 5 + 16 not = 2 · 2^4
   each subset without x pairs with one subset with x (add x), so the two
   halves are equal, and 2^n = 2 · 2^(n-1) is the step.

6. THE CHOCOLATE BAR: n × m SQUARES NEED nm − 1 BREAKS, IN ANY ORDER
   6 × 4, split the largest piece  breaks: 23
   6 × 4, split the first piece    breaks: 23
   invariant: every break turns one piece into two, so pieces = breaks + 1,
   and 24 pieces need 23 breaks whatever the order. That invariant is the
   induction: P(k) = 'k squares need k − 1 breaks', and a break splits k into
   a + b with (a − 1) + (b − 1) + 1 = k − 1.

7. CLOSED FORMS, CHECKED, AND ONE DERIVED FROM THREE
   Σi = n(n+1)/2: True   Σi² = n(n+1)(2n+1)/6: True   Σi³ = (n(n+1)/2)²: True
   Σ(i² + 3i + 5) = n(n+1)(2n+1)/6 + 3n(n+1)/2 + 5n: True   (sigma is linear: Σ(f + g) = Σf + Σg)
```
<!-- /output -->

## Po polsku, w skrócie

Dowód przez indukcję pokazuje przypadek początkowy P(0) i krok: że z P(n) wynika P(n + 1); wniosek brzmi, że P(n) zachodzi dla każdego n. Metoda jest poprawna dzięki zasadzie dobrego uporządkowania: każdy niepusty zbiór liczb naturalnych ma element najmniejszy. Gdyby zdanie gdzieś zawodziło, zawodziłoby po raz pierwszy dla pewnego m; m ≠ 0 z przypadku początkowego, więc P(m − 1) zachodzi, a krok daje P(m), sprzeczność. Program pokazuje to na fałszywym zdaniu „n² + n + 41 jest pierwsze": najmniejszy kontrprzykład to n = 40, i właśnie tam krok jest fałszywy. Słynny błędny dowód, że wszystkie samochody mają ten sam kolor, zawodzi w kroku od jednego samochodu do dwóch, bo zbiory {1} i {2} się nie nakładają; brakujący jeden szczebel wystarczy. Dalej program przechodzi przykłady z rozdziału Ashlocka: parzystość f(3n) i wzór Bineta liczony dokładnie w liczbach a + b√5, 2ⁿ podzbiorów przez parowanie, tabliczka czekolady n × m wymagająca nm − 1 łamań w dowolnej kolejności (niezmiennik: kawałki = łamania + 1) i postacie zwarte sum Σi, Σi², Σi³.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 11_Logic/induction/examples/induction.py
```

## See also

- [If A then B: converse, contrapositive and inverse](../converse_and_contrapositive/README.md) — the step is an if–then, and a counterexample is one case
- [Predicates and quantifiers](../predicates_and_quantifiers/README.md) — P(n) is a predicate, and the conclusion is ∀n P(n)
- [Infinity](../../13_Axioms_of_Set_Theory/infinity/README.md) — induction as "the set where P holds is inductive"
- [Ordinals](../../13_Axioms_of_Set_Theory/ordinals/README.md) — well-ordering beyond ℕ, and a theorem induction on ℕ cannot reach
- [Function katas](../../04_Sets/function_katas/README.md) — the proof moves, with induction among them
- Daniel Ashlock, *Basic Set Theory*, chapter 2 of his course text, section 2.2 (free PDF, see [the reading guide](../../reading_guides/set_theory/README.md))
- [Mathematical induction ↗](https://en.wikipedia.org/wiki/Mathematical_induction) — Wikipedia
