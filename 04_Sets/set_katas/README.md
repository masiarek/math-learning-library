# Set katas: Cunningham's first exercises, checked before you prove them

**Level:** 101 · for anyone who has read the definitions of ⊆, ∪, ∩ and ∖ and wants exercises with a way to know the claim is true before starting

**One line:** The exercises at the end of a first section on sets all have one proof, take an arbitrary element and unpack the definitions, and one failure mode, misreading a formula; the program checks each claim on every choice of subsets of {1, 2, 3} and computes every truth set and interval, so the only thing left to do is the proof.

## How to use the page

A kata is a short exercise repeated until the move is automatic. The exercises here are Cunningham's section 1.1 (*Set Theory: A First Course*, Cambridge, 2016), the first page of exercises in a first course, and the same page in any other book would do. Pick one, write the claim in your own words, try the proof for ten minutes, then run the program. For a statement about arbitrary sets it checks all 512 choices of A, B, C among the subsets of {1, 2, 3}, and all three choices of an element a, 1 536 cases in all: a True means your reading of the formula is the book's; a False means the formula was misread, which is the mistake this page exists to catch. For a truth set it prints the set; for an interval it computes the result exactly, with rational endpoints, or checks a claimed interval on a grid of sample points where the exercise asks you to solve an inequality.

The moves, which the [axiom katas](../../13_Axioms_of_Set_Theory/axiom_katas/README.md) page extends to the axioms:

| Move | What it looks like | Katas |
|---|---|---|
| **Element chase** | "let x ∈ A ∖ (B ∖ C); then x ∈ A and x ∉ B ∖ C; so x ∉ B or x ∈ C; …" | 1 to 7, problem 5 |
| **Unpack a negation** | x ∉ A ∖ B means x ∉ A or x ∈ B, by De Morgan | 1, 3, 7, problem 5 |
| **Two inclusions** | an equality of sets is two ⊆ | 9, 11 |
| **Solve, then describe** | a truth set is the solutions of a condition; name them | 8, 10, 12 |

## The katas

Exercises 1.1, with the move for each:

- **1.** If a ∉ A ∖ B and a ∈ A, then a ∈ B. Unpack a ∉ A ∖ B.
- **2.** If A ⊆ B, then C ∖ B ⊆ C ∖ A. Element chase; the contrapositive of A ⊆ B does the work.
- **3.** If A ∖ B ⊆ C, then A ∖ C ⊆ B. Take x ∈ A with x ∉ C; it cannot be in A ∖ B.
- **4.** If A ⊆ B and A ⊆ C, then A ⊆ B ∩ C. The shortest one.
- **5.** If A ⊆ B and B ∩ C = ∅, then A ⊆ B ∖ C. An element of A is in B and therefore not in C.
- **6.** A ∖ (B ∖ C) ⊆ (A ∖ B) ∪ C. Unpack x ∉ B ∖ C into two cases.
- **7.** If A ∖ B ⊆ C and A ⊄ C, then A ∩ B ≠ ∅. The element of A outside C is the witness.
- **8.** P(x) is x > 1/x: which of P(2), P(−2), P(½), P(−½) hold? Two do, and the sign of x is the whole story.
- **9.** Write (−3, 2) ∩ (1, 3), (−3, 4) ∪ (0, ∞) and (−3, 2) ∖ [1, 3) as intervals. Draw the number line.
- **10.** {1, 4, 9, 16, 25, …} and {…, −10, −5, 0, 5, 10, …} as truth sets. Name the condition.
- **11.** {x ∈ ℝ : x² − 1 ≤ 3} and {x ∈ ℝ : x > 0 and (x − 1)² < 1} as intervals. Solve the inequality; the program only samples.
- **12.** Evaluate {x ∈ ℕ : 0 < x² < 24}, {y ∈ ℤ : y divides 12}, {z ∈ ℕ : 4 divides z} and {y ∈ ℝ⁻ : 1 ≤ y² ≤ 4}. Cunningham's ℕ begins at 0, so 0 divides nothing but is divisible by 4.
- **Problem 5 of section 1.2.** x ∉ A ∖ B is equivalent to x ∉ A or x ∈ B. This is the lemma that katas 1, 3 and 7 use, and its proof is De Morgan's law applied to the definition of ∖, which [the algebra of sets](../algebra_of_sets/README.md) covers.

## Quiz katas

Ten multiple-choice questions from the Math is Fun quizzes on sets, which the owner sent as screenshots; section 4 of the program computes each answer, with the sets listed. They are good katas for the first hour: each tests one definition (subset, proper subset, empty set, 2ⁿ) or one convention, and each can be settled by listing the sets. They are weak where the exercises above are strong: they ask for recall, never for a proof, and one of them turns on a convention rather than on mathematics.

| Question | Answer | Why |
|---|---|---|
| X = multiples of 3, Y of 6, Z of 9; which is true? | **D**, Z ⊂ X | every multiple of 9 is a multiple of 3, because 3 divides 9; Y ⊂ X is true too, but not offered |
| A = factors of 6, B = prime factors, C = proper factors, D = factors of 3; which is true? | **C**, B = C | with proper factors {2, 3}; see the note below |
| Which is the null set? | **D**, rational expressions for π | {∅} has a member; 2 is an even prime; 7 has factors 1 and 7; π is irrational |
| Subsets of {a, b, c, d}? | **C**, 16 | 2⁴: each member in or out |
| Proper subsets of {a, b, c, d, e}? | **B**, 31 | 2⁵ − 1: all subsets but the set itself |
| A ⊆ B and B ⊆ C; what must hold? | **D**, A ⊆ C | ⊆ is transitive; the other three fail for A = ∅, B = C = {1} |
| P, Q, R = factors of 5, 25, 125; which is false? | **C**, R ⊂ P | the factor sets are nested upward: {1, 5} ⊂ {1, 5, 25} ⊂ {1, 5, 25, 125} |
| A = primes < 10, B = odd < 10, C = even < 10; how many of the six proper-subset claims hold? | **D**, none | 2 is prime and not odd, so A ⊄ B; the rest fail at once |
| Which set is infinite? | **C**, integers less than 10 | 9, 8, …, 0, −1, −2, … has no end; the other three have 10, 4 and 4 members |
| A = factors of 12; which is not a member? | **C**, 5 | the factors are 1, 2, 3, 4, 6, 12 |

**Proper factors.** A factor of n is a positive integer that divides n. A *proper* factor excludes n itself, and on the stricter convention, which Math is Fun uses and the quiz needs, excludes 1 as well: the proper factors of 6 are 2 and 3. On the looser convention they are 1, 2 and 3, and then no option of that question is true. "Proper" works as it does for subsets: a proper subset of S is a subset other than S itself. (The Math is Fun definitions page could not be fetched from this session; the convention is inferred from the quiz having an answer.)

**Is this number theory?** Yes, read as sets. The three questions about factors and multiples are one fact of number theory in set clothing: a divides b exactly when the factors of a are a subset of the factors of b, and exactly when the multiples of b are a subset of the multiples of a. Divisibility is a partial order, like ⊆, and the program checks the equivalence for every a and b up to 12. [The algebra of sets](../algebra_of_sets/README.md#is-a-partial-order) has ⊆ as a partial order; divisibility is the other standard example, and the one [Hrbacek and Jech](../function_katas/README.md) use for "incomparable" (2 and 3 are incomparable under divides).

## From Ashlock's problem set

Daniel Ashlock's chapter *Basic Set Theory* (free PDF; see [the reading guide](../../reading_guides/set_theory/README.md)) ends its first section with problems of a different flavour, and section 5 of the program takes five of them.

- **2.1, which of these are sets?** "The weights, to the nearest kilogram, of all people in Canada" is a list with repeats, a [multiset](../../GLOSSARY.md#multiset), not a set; "all weights at least one person had" is the set behind it. First names in a phone book, in order, are a list; the set forgets the order. {√x : x < 0} is ∅ in the reals and a set of imaginary numbers in the complex numbers, so the answer depends on the universal set, which is the warning in the problem.
- **2.7, precedence.** Ashlock's convention is complement first, then ∩, then ∪, with ∖ and △ always bracketed, the same ladder as ¬, ∧, ∨ in [reading a set expression](../reading_set_expressions/README.md). The program shows the difference brackets make on one example.
- **2.9 and 2.10, Venn diagrams of four sets.** A diagram of n sets needs 2ⁿ regions, and n circles in general position make at most n² − n + 2: enough for n up to 3 and short from n = 4, where 14 < 16. Venn drew four sets with ellipses, and any number can be drawn with other shapes; the program prints the two columns side by side.
- **2.19 and 2.20, k-element subsets.** C(n, k) = n!/(k!(n − k)!), counted and compared with the formula for n = 4, and the row sums to 2ⁿ.
- **2.21, inclusion–exclusion.** |S ∪ T| = |S| + |T| − |S ∩ T|, checked on every pair of subsets of {1, 2, 3}: the overlap was counted twice and is subtracted once.

Problem 2.18, that △ does not distribute over ∪, is now in the search for false laws on [the algebra of sets](../algebra_of_sets/README.md#laws-that-look-true-and-are-not).

## From a school textbook: ∈ versus ⊆, nested sets, and counting by Venn regions

The owner sent chapter 1, *Sets*, of an Indian school textbook at Class 11 level (title not shown on the pages; blood groups, Kho-Kho and mock tests for examples). It is friendly and correct, its summary is already a list of flashcards, and its exercises are of two kinds the pages above lack: traps about ∈, ⊆ and nested braces, and word problems counted by Venn regions. Section 6 of the program does both.

| Kata | Answer | Why |
|---|---|---|
| 1 ∈ {1}; {2} ∈ {2}; {2} ∈ {{2}}; ∅ ∈ {1, 2, 3}; ∅ ⊆ {1, 2, 3} | T, F, T, F, T | ∈ asks "is it a member", ⊆ asks "is every member of it a member"; ∅ is a subset of every set and a member only of sets that list it |
| cardinality of {a}, {a, {a}}, {∅, 1, 2, {1, 2}}, {1, {1}, {1, {1}}}, {∅, {∅}, {∅, {∅}}} | 1, 2, 4, 3, 3 | a member that is itself a set counts once; inner braces do not open |
| P(∅), P({∅}), P({∅, {∅}}) | 1, 2, 4 members | 2ⁿ for n = 0, 1, 2; P(∅) = {∅} is not empty |
| n(A) = 10, n(A) = 100 | 2¹⁰ = 1 024, 2¹⁰⁰ ≈ 1.27 × 10³⁰ | the second is why power sets outrun everything |
| the set of letters of BANANA | {A, B, N}, 3 members | repetition is not membership |
| 40 students, 22 badminton, 11 both, 16 neither: table tennis only? | 2 | n(B ∪ T) = 40 − 16 = 24, so n(T) = 24 − 22 + 11 = 13, and 13 − 11 = 2 |
| 120 students, 92 language, 46 maths, all teach: both? exactly one? | 18; 102 | 92 + 46 − 120; 92 + 46 − 2 · 18 |
| 100 students, 70 physics, 60 chemistry: least both? most neither? | 30; 30 | n(P ∪ C) ≤ 100 forces n(P ∩ C) ≥ 30; n(P ∪ C) ≥ 70 forces neither ≤ 30 |
| 56 certificates, 17 + 28 + 25 awards, 4 with all three: exactly two? | 6 | pair overlaps sum to 70 + 4 − 56 = 18, and each triple student is in three of them: 18 − 12 |
| 100 students, E 60, G 50, S 35, EG 40, GS 30, ES 25, all three 25 | at least two 45, at most one 55, none 25 | n(E ∪ G ∪ S) = 145 − 95 + 25 = 75 |

The program does not apply the formulas; it builds sets with the stated region sizes and counts, and then shows the formula giving the same number. That is the right order: n(A ∪ B) = n(A) + n(B) − n(A ∩ B) is a theorem about counting, and the Venn regions are its proof. The three-set version adds the triple overlap back because it was subtracted three times after being added three times.

## Flashcards

The textbook's summary and these katas as a deck of Anki cards: [`set_katas.txt`](anki/set_katas.txt). Import with File → Import. Tags: `definition`, `notation`, `trap`, `counting`, `formula`, `example`. The cards are also in the chapter's combined deck.

## What the program prints

<!-- output:set_katas -->
*Verified output of [`set_katas.py`](examples/set_katas.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. STATEMENTS ABOUT SETS: EXERCISES 1.1, 1 TO 7, ON EVERY A, B, C ⊆ {1, 2, 3}
   1               if a ∉ A ∖ B and a ∈ A, then a ∈ B
                   holds in all 384 cases where the hypothesis holds (of 1536): True
   2               if A ⊆ B, then C ∖ B ⊆ C ∖ A
                   holds in all 648 cases where the hypothesis holds (of 1536): True
   3               if A ∖ B ⊆ C, then A ∖ C ⊆ B
                   holds in all 1029 cases where the hypothesis holds (of 1536): True
   4               if A ⊆ B and A ⊆ C, then A ⊆ B ∩ C
                   holds in all 375 cases where the hypothesis holds (of 1536): True
   5               if A ⊆ B and B ∩ C = ∅, then A ⊆ B ∖ C
                   holds in all 192 cases where the hypothesis holds (of 1536): True
   6               A ∖ (B ∖ C) ⊆ (A ∖ B) ∪ C
                   holds in all 1536 cases where the hypothesis holds (of 1536): True
   7               if A ∖ B ⊆ C and A ⊄ C, then A ∩ B ≠ ∅
                   holds in all 381 cases where the hypothesis holds (of 1536): True
   1.2, problem 5  x ∉ A ∖ B  iff  x ∉ A or x ∈ B
                   holds in all 1536 cases where the hypothesis holds (of 1536): True
   Every one is proved by taking an arbitrary x and unpacking the
   definitions of ∖, ∩, ∪ and ⊆; the page names the move for each.

2. TRUTH SETS: PROBLEM 1 AND EXERCISES 8, 10, 12
   {x ∈ ℕ : 3 < x < 11}         = {4, 5, 6, 7, 8, 9, 10}
   {y ∈ ℤ : y² = 4}             = {-2, 2}
   {z ∈ ℕ : z is a multiple of 3} = {0, 3, 6, 9, 12, 15, ...}   (Cunningham's ℕ starts at 0)
   exercise 8, P(x): x > 1/x:  P(2) True  P(-2) False  P(1/2) False  P(-1/2) True
   exercise 10: {1, 4, 9, 16, 25, ...} = {x ∈ ℕ : x = n² for some n ≥ 1};
                {..., -10, -5, 0, 5, 10, ...} = {y ∈ ℤ : 5 divides y}
   exercise 12(a) {x ∈ ℕ : 0 < x² < 24}        = {1, 2, 3, 4}
   exercise 12(b) {y ∈ ℤ : y divides 12}       = {-12, -6, -4, -3, -2, -1, 1, 2, 3, 4, 6, 12}
   exercise 12(c) {z ∈ ℕ : 4 divides z}        = {0, 4, 8, 12, 16, ...}

3. INTERVALS: EXERCISE 9 EXACTLY, EXERCISES 11 AND 12(d) ON A GRID
   9(a) (−3, 2) ∩ (1, 3)    = (1, 2)
   9(b) (−3, 4) ∪ (0, ∞)    = (-3, ∞)
   9(c) (−3, 2) ∖ [1, 3)    = (-3, 1)
   11(a) {x ∈ ℝ : x² − 1 ≤ 3}               = [-2, 2]    agrees on 81 sample points in [−5, 5]: True
   11(b) {x ∈ ℝ : x > 0 and (x − 1)² < 1}   = (0, 2)     agrees on 81 sample points in [−5, 5]: True
   12(d) {y ∈ ℝ⁻ : 1 ≤ y² ≤ 4}              = [-2, -1]   agrees on 81 sample points in [−5, 5]: True
   The grid check is evidence, not proof: solving x² − 1 ≤ 3 is the kata.

4. QUIZ KATAS: SEVEN MULTIPLE-CHOICE QUESTIONS, COMPUTED
   Q1 X = multiples of 3, Y of 6, Z of 9 (within 1..199):
      A  X ⊂ Y: False
      B  X ⊂ Z: False
      C  Z ⊂ Y: False
      D  Z ⊂ X: True
      every multiple of 9 is a multiple of 3, because 3 | 9; and Y ⊂ X too, since 3 | 6.
   Q2 A = factors of 6 = [1, 2, 3, 6], B = prime factors = [2, 3], D = factors of 3 = [1, 3]
      C = proper factors of 6: [2, 3] if 1 is excluded (Math is Fun), [1, 2, 3] if only 6 is
      A = B False   A = C False   B = C True   C = D False   -> C, on the convention that excludes 1
   Q3 which is the null set?
      A  subsets of ∅: [frozenset()]   empty: False
      B  even primes: [2]   empty: False
      C  factors of 7: [1, 7]   empty: False
      D  rational expressions for π: ∅   empty: True
      {∅} has one member, ∅ itself; π is irrational, so D.
   Q4 subsets of {a, b, c, d}: 2^4 = 16   (each of 4 members in or out)
   Q5 proper subsets of {a, b, c, d, e}: 2^5 − 1 = 31   (all subsets but the set itself)
   Q6 A ⊆ B and B ⊆ C imply A ⊆ C, on all triples of subsets of {1, 2, 3}: True   -> D; the other three fail e.g. A = ∅, B = C = {1}
   Q7 factors of 5, 25, 125: [1, 5], [1, 5, 25], [1, 5, 25, 125]
      P ⊂ Q True   Q ⊂ R True   R ⊂ P False   P ⊂ R True   -> C is the false one
   Q8 A = primes < 10 = [2, 3, 5, 7], B = odd < 10 = [1, 3, 5, 7, 9], C = even < 10 = [0, 2, 4, 6, 8]
      A ⊂ B False   B ⊂ A False   A ⊂ C False   C ⊂ A False   B ⊂ C False   C ⊂ B False   -> 0 true: D, None; 2 is the prime that is not odd
   Q9 which is infinite? whole numbers < 10: 10 of them; primes < 10: 4; factors of 10: 4;
      integers < 10: 9, 8, 7, ..., 0, −1, −2, ... with no end -> C
   Q10 factors of 12 = [1, 2, 3, 4, 6, 12]; not a member: [5] -> C
   Behind Q1, Q2, Q7 and Q10 is one fact of number theory read as sets:
      a | b  iff  factors(a) ⊆ factors(b)  iff  multiples(b) ⊆ multiples(a)
      checked for all a, b in 1..12: True

5. FROM ASHLOCK'S PROBLEM SET: WHICH ARE SETS, PRECEDENCE, FOUR CIRCLES, COUNTING
   2.1  'the weights of all people in Canada' repeats values: a multiset, not a set;
        'all weights at least one person had' drops repeats: a set. In Python:
        list [70, 82, 70, 65, 82, 82] -> set [65, 70, 82]; 'the first names in a phone book, in order' is a list,
        the set behind it forgets the order. {√x : x < 0} is ∅ in ℝ and a set of imaginaries in ℂ: it depends on U.
   2.7  precedence (Ashlock: complement, then ∩, then ∪; ∖ and △ always bracketed):
        A ∪ B ∩ C ∪ D reads A ∪ (B ∩ C) ∪ D;  Aᶜ ∩ Bᶜ ∪ C reads (Aᶜ ∩ Bᶜ) ∪ C;  A ∪ B = A ∩ C is a truth value
        with A = [1, 2], B = [2, 3], C = [3, 4]: A ∪ (B ∩ C) = [1, 2, 3] but (A ∪ B) ∩ C = [3]
   2.9/2.10  a Venn diagram of n sets needs 2^n regions; n circles in general position
        make at most n² − n + 2 regions, so circles stop working at four sets (Venn used ellipses):
        n:            1    2    3    4    5    6
        2^n:          2    4    8   16   32   64
        n²−n+2:       2    4    8   14   22   32
   2.19/2.20  k-element subsets of an n-set: C(n, k) = n! / (k!(n−k)!)
        n = 4: counted [1, 4, 6, 4, 1], formula [1, 4, 6, 4, 1], sum 16 = 2^4
   2.21  |S ∪ T| = |S| + |T| − |S ∩ T| on all pairs of subsets of {1, 2, 3}: True   (inclusion–exclusion)

6. FROM A SCHOOL TEXTBOOK: ∈ VERSUS ⊆, NESTED SETS, AND COUNTING BY VENN REGIONS
   1.2.2 true or false:  1 ∈ {1}: True   {2} ∈ {2}: False   {2} ∈ {{2}}: True   ∅ ∈ {1, 2, 3}: False   ∅ ⊆ {1, 2, 3}: True
         ∈ asks 'is it a member'; ⊆ asks 'is every member of it a member'. ∅ is a subset of everything and a member of almost nothing.
   1.2.4 cardinality of nested sets: {a} -> 1   {a, {a}} -> 2   {∅, 1, 2, {1, 2}} -> 4   {1, {1}, {1, {1}}} -> 3   {∅, {∅}, {∅, {∅}}} -> 3
         a member that is itself a set still counts once; braces inside braces do not open.
   1.2.3 P(∅) has 1 member; P({∅}) has 2; P({∅, {∅}}) has 4;  n(A) = 10 gives 2^10 = 1024, n(A) = 100 gives 2^100 = 1267650600228229401496703205376
   BANANA: the set of its letters is ['A', 'B', 'N'], 3 members, not 6
   Ex.20 40 students, 22 badminton, 11 both, 16 neither -> table tennis only: build the sets and count: 2
         check: n(U) = 40, n(B) = 22, n(B ∩ T) = 11, n(neither) = 16; formula n(T) = n(U) − n(neither) − n(B) + n(B ∩ T) = 13
   Ex.21 120 students, 92 language, 46 maths, all teach something -> both: 18 = 92 + 46 − 120; exactly one: 102 = 92 + 46 − 2·18
   Ex.22 100 students, 70 physics, 60 chemistry: n(P ∪ C) = 130 − n(P ∩ C) and n(P ∪ C) ≤ 100,
         so n(P ∩ C) ≥ 30 (least both) and, with C ⊆ P, n(P ∪ C) = 70 so neither ≤ 30 (most neither)
   1.3.10 100 students: E 60, G 50, S 35, EG 40, GS 30, ES 25, all three 25. Build 8 regions, then count:
         sizes rebuilt: n(E) = 60, n(G) = 50, n(S) = 35, n(E ∩ G) = 40, n(G ∩ S) = 30, n(E ∩ S) = 25, all three 25
         at least two: 45   at most one: 55   none: 25
         n(E ∪ G ∪ S) by inclusion–exclusion = 60 + 50 + 35 − (40 + 30 + 25) + 25 = 75; counted: 75
   1.3.9 56 certificates, 17 + 28 + 25 = 70 awards, 4 students with all three: pairs sum to 70 + 4 − 56 = 18,
         exactly two = 18 − 3·4 = 6  (each triple student sits in three of the pair counts)
```
<!-- /output -->

## Po polsku, w skrócie

Zadania z końca pierwszego rozdziału o zbiorach mają jeden dowód: weź dowolny element i rozpakuj definicje ⊆, ∪, ∩ i ∖; i jeden sposób, by się pomylić: źle odczytać formułę. Program sprawdza każdą tezę o dowolnych zbiorach A, B, C na wszystkich 512 wyborach podzbiorów {1, 2, 3} (1 536 przypadków z elementem a), oblicza zbiory prawdziwości i przedziały dokładnie, z końcami wymiernymi, a tam, gdzie zadanie każe rozwiązać nierówność, sprawdza podany przedział na siatce punktów. True znaczy, że formuła została odczytana tak, jak chciał autor; False znaczy, że nie. Dowód pozostaje do zrobienia: ruchy to pogoń za elementem, rozpakowanie negacji (x ∉ A ∖ B to x ∉ A lub x ∈ B, prawo De Morgana), dwa zawierania dla równości i „rozwiąż, potem nazwij" dla zbiorów prawdziwości. Zadania pochodzą z podrozdziału 1.1 książki Cunninghama *Set Theory: A First Course*.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 04_Sets/set_katas/examples/set_katas.py
```

## See also

- [The algebra of sets](../algebra_of_sets/README.md) — De Morgan's laws, the lemma behind half the katas
- [Reading a set expression](../reading_set_expressions/README.md) — how to read A ∖ (B ∖ C) before chasing an element through it
- [Axiom katas](../../13_Axioms_of_Set_Theory/axiom_katas/README.md) — the same idea for the axioms
- [Set theory: a reading guide](../../reading_guides/set_theory/README.md) — Cunningham among the other books
