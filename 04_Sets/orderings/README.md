# Orderings: six properties, four names, and what "poset" means

**Level:** 101 → 201 · for anyone who has met "reflexive, symmetric, antisymmetric, transitive" as a list to memorise and wants to see which combinations are worth a name, and why a set can have two maximal elements and no maximum

**One line:** A relation on a finite set is a set of pairs, so each of the six properties a book asks of it is a loop that can be run; running them on all 512 relations on three points sorts out which combinations have names (equivalence, partial order, linear order, their strict versions), shows the identity relation wearing two of them, and catches two examples in the book that its author got wrong.

## The six properties, as loops

Let R be a relation on S, a set of pairs (x, y) with x and y in S, as [relations and functions](../relations_and_functions/README.md) defines it. Robert André's Definition 6.1, whose chapters 5 to 8 this page follows, lists six properties and one word:

| Property | Says | Loop |
|---|---|---|
| [reflexive](../../GLOSSARY.md#reflexive-relation) | every x is related to itself | every (x, x) is in R |
| [irreflexive](../../GLOSSARY.md#irreflexive-relation) | no x is related to itself | no (x, x) is in R |
| [symmetric](../../GLOSSARY.md#symmetric-relation) | x R y gives y R x | for every pair in R, the reversed pair is in R |
| [antisymmetric](../../GLOSSARY.md#antisymmetric-relation) | x R y and y R x force x = y | no reversed pair in R unless x = y |
| [asymmetric](../../GLOSSARY.md#asymmetric-relation) | x R y forbids y R x | no reversed pair in R at all |
| [transitive](../../GLOSSARY.md#transitive-relation) | x R y and y R z give x R z | for every chained pair, the shortcut is in R |
| [comparable](../../GLOSSARY.md#comparable) (two elements) | x R y or y R x | at least one of the two pairs is in R |

Each line is one `all(...)` over the pairs, and section 1 of the program runs them on André's four examples. Three things come out that are easy to miss by eye. The empty relation is irreflexive, symmetric, antisymmetric, asymmetric and transitive at once, all vacuously, since there is no pair to fail any of them. Symmetric plus transitive does not give reflexive, which the book warns about on page 57: R₂ = {(a, a), (b, b), (d, d), (a, b)} is the counterexample, and the loop shows (c, c) missing. And two of the book's own verdicts are wrong: "distinct siblings" is called transitive, but x T y and y T x would need x T x, and nobody is their own distinct sibling (the book's repair, "siblings or the same person", on page 58, is an equivalence); and R₃ on page 57 is called transitive, but it has (a, b) and (b, c) without (a, c). The program prints both failures. A relation is a set of pairs, and a claim about it is checked by looking at the pairs, which is what the loops do and the eye does not.

## Four names

Two families of combinations have names, and section 2 counts them on all 512 relations on {a, b, c}.

**[Equivalence](../../GLOSSARY.md#equivalence-relation)**: reflexive, symmetric, transitive. "Counts as the same." There are 5 on three points, the Bell number, because an equivalence is the same thing as a [partition](../equivalence_and_partitions/README.md).

**[Partial order](../../GLOSSARY.md#partial-order)** (non-strict): reflexive, antisymmetric, transitive, written a ≤ b. A **[linear](../../GLOSSARY.md#linear-order-total-order)** (total) order is a partial order in which every two elements are comparable. The **[strict](../../GLOSSARY.md#strict-order)** versions replace reflexive by irreflexive and antisymmetric by asymmetric, written a < b, and the two kinds match one to one: remove the diagonal pairs (x, x) from a partial order and a strict one remains; add them back and the partial order returns. On three points there are 19 partial orders, 6 of them linear (the 3! arrangements), and 19 strict ones. A **[poset](../../GLOSSARY.md#poset)** is a partially ordered set, a set together with a partial order on it; André's footnote records *loset* for a linearly ordered set, which almost nobody says, the usual word being *toset* or *chain*.

The identity relation wears two names: it is an equivalence (every class is a singleton) and a partial order (nothing is below anything else). It is the only relation that is both, since symmetric and antisymmetric together force every pair to be (x, x).

## Words for positions in a poset

André's Definition 6.4, run on two examples in sections 3 and 4:

- A **[chain](../../GLOSSARY.md#chain-and-antichain)** is a subset on which the order is linear; an **antichain** is a subset no two of whose members are comparable.
- m is **minimal** when nothing is below it, **[maximal](../../GLOSSARY.md#maximal-and-maximum)** when nothing is above it.
- m is the **minimum** when it is below everything else, the **maximum** when above everything else. A minimum is minimal, and when every two elements are comparable the words agree; in a partial order they come apart.

Mortimer's ancestors, ordered by "a is a descendant of b", are a strict partial order in which Mortimer is the minimum, two spontaneously generated ancestors A and E are each maximal, and there is no maximum, because A and E are not comparable. Divisibility on 1 to 12 is a partial order with minimum 1, six maximal elements (7 to 12, which divide nothing else in range), no maximum, the chain 1, 2, 4, 8, and the primes as an antichain. [The algebra of sets](../algebra_of_sets/README.md#is-a-partial-order) has ⊆ as the other standard poset, and divisibility read as ⊆ of factor sets is on [the set katas](../set_katas/README.md#quiz-katas). Section 5 is André's exercise 7.8, the **[lexicographic](../../GLOSSARY.md#lexicographic-order)** order on pairs: compare first entries, and only on a tie compare the second. It is the order of a dictionary and of a database sort on two columns, and the program confirms it is a partial order on 16 pairs of subsets.

## The other "partition"

The owner asked whether this connects to the partitions of real analysis. Same word, two objects. A set-theory partition, [the previous lesson](../equivalence_and_partitions/README.md), is a family of nonempty disjoint blocks covering a set. A partition of an interval [a, b] in the Riemann sense is a finite list of cut points a = x₀ < x₁ < ⋯ < xₙ = b, and the integral is squeezed between the lower and upper sums over the cells it makes. The cells overlap at their endpoints, so they are not a partition in the first sense, though the half-open cells [xᵢ, xᵢ₊₁) are. Section 6 computes both sums for x² on [0, 2] exactly, with 3 cells and then 200, and the integral 8/3 sits between them while the gap shrinks. The connection to this page is the order: one Riemann partition **refines** another when it contains all its cut points, and refinement is a partial order on partitions, under which any two have a common refinement, their union. That is the fact the Riemann integral's definition rests on, and it is a poset fact.

## What the program prints

<!-- output:orderings -->
*Verified output of [`orderings.py`](examples/orderings.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. SIX PROPERTIES, EACH A LOOP (ANDRÉ, DEFINITION 6.1)
   relation on {a, b, c, d}           reflexi irrefle symmetr antisym asymmet transit   name
   R1 = {(a,a),(b,b),(c,c),(d,d),(a,b)}       T       F       F       T       F       T   partial order
   R2 = {(a,a),(b,b),(d,d),(a,b)}           F       F       F       T       F       T   none of these
   R3 = R1 + (b,a),(b,c),(c,b)              T       F       T       F       F       F   none of these
   Id_S                                     T       F       T       T       F       T   equivalence, partial order
   ∅, the empty relation                    F       T       T       T       T       T   strict partial order
   R1 is a partial order (reflexive, antisymmetric, transitive). R2 is neither reflexive
   nor irreflexive. ∅ is irreflexive, symmetric, antisymmetric, asymmetric and transitive,
   all vacuously, so a strict partial order. And R3, which the book calls transitive,
   is not: it has (a, b) and (b, c) but (a, c) ∈ R3 is False. The loop catches what the eye missed.
   The trap on page 57: symmetric + transitive does not give reflexive; R2 is the witness.
   'distinct siblings' on three siblings: symmetric True, transitive False:
   x T y and y T x would need x T x, and nobody is their own distinct sibling. The book
   calls T transitive on page 56; its H on page 58, 'siblings or the same person', is.

2. ALL 512 RELATIONS ON {a, b, c}, SORTED BY NAME
   equivalence               5
   partial order            13
   linear order              6
   strict partial order     13
   strict linear order       6
   none of these           470
   non-strict orders 19 (13 partial, the identity among them, + 6 linear),
   strict orders 19; remove the diagonal True, add it back True: a one-to-one match.
   equivalences: 5, the Bell number B(3); linear orders: 6 = 3!; partial orders on 3 labelled
   points: 19, the third term of OEIS A001035 (1, 1, 3, 19, 219, ...).

3. MORTIMER'S ANCESTORS: A STRICT PARTIAL ORDER WITH MINIMUM, NO MAXIMUM, TWO MAXIMALS
   'a is a descendant of b', 24 pairs: irreflexive True, asymmetric True, transitive True -> strict partial order
   minimal: ['M']  minimum: ['M']  maximal: ['A', 'E']  maximum: none
   A and E are not comparable, so there are two maximal elements and no maximum;
   M is below everyone, so it is the minimum. Is (A, E) comparable? False

4. DIVISIBILITY ON 1..12: A POSET WITH CHAINS, ANTICHAINS, MAXIMALS AND A MINIMUM
   m | n: reflexive True, antisymmetric True, transitive True, comparable False -> partial order
   minimum: 1 (divides everything); maximal: [7, 8, 9, 10, 11, 12] (divide nothing else in 1..12); maximum: none
   a chain: [1, 2, 4, 8], every pair comparable: True
   an antichain: the primes [2, 3, 5, 7, 11], no two comparable: True
   The subset order ⊆ on P({1, 2, 3}) is the other standard poset; both are drawn as Hasse diagrams.

5. LEXICOGRAPHIC ORDER ON PAIRS (ANDRÉ, EXERCISE 7.8, FOR SUBSETS OF {1, 2})
   ((A, B), (C, D)) ∈ R iff A ⊂ C, or A = C and B ⊆ D, on 16 pairs:
   reflexive True, antisymmetric True, transitive True -> partial order
   Dictionary order: compare first entries, and only on a tie compare the second.

6. THE OTHER 'PARTITION': REAL ANALYSIS CUTS AN INTERVAL, NOT A SET
   a partition of [0, 2] in the Riemann sense is a finite list of points ['0', '1/2', '1', '2'],
   cutting it into subintervals [('0', '1/2'), ('1/2', '1'), ('1', '2')], which overlap at endpoints.
   lower sum of x² over it = 9/8, upper sum = 37/8; the integral 8/3 lies between: True
   with 200 cells: lower 2.6467, upper 2.6867, gap 0.0400; the gap goes to 0 as the mesh does.
   Same word, two objects: a set-theory partition is a family of disjoint blocks, and the
   half-open cells [0, 1/2), [1/2, 1), [1, 2] make it one; the Riemann partition is the
   list of cut points, and the refinement order on those lists is itself a poset.
```
<!-- /output -->

## Flashcards

Relations, orderings and partitions, with the definitions from André's chapters 5 to 8 and the traps the program found, as a deck of Anki cards: [`orderings.txt`](anki/orderings.txt). Import with File → Import. Tags: `definition`, `trap`, `example`, `notation`, `class`. The cards are also in the chapter's combined deck.

## Po polsku, w skrócie

Relacja na zbiorze skończonym to zbiór par, więc każda z sześciu własności z podręcznika (zwrotna, przeciwzwrotna, symetryczna, antysymetryczna, asymetryczna, przechodnia) to pętla po parach, którą można uruchomić. Program uruchamia je na wszystkich 512 relacjach na {a, b, c} i liczy, które kombinacje mają nazwy: relacja równoważności (zwrotna, symetryczna, przechodnia; 5 sztuk, liczba Bella), porządek częściowy (zwrotna, antysymetryczna, przechodnia; 19), porządek liniowy (każde dwa elementy porównywalne; 6 = 3!) i ich wersje ostre (przeciwzwrotne, zapisywane a < b; też 19). Poset to zbiór częściowo uporządkowany. Relacja identyczności jest zarazem równoważnością i porządkiem. Pętle wyłapują też dwa błędne przykłady w książce: „rodzeństwo" nie jest relacją przechodnią (x T y i y T x wymagałoby x T x), a R₃ ze strony 57 ma (a, b) i (b, c) bez (a, c). Słowa o pozycjach: łańcuch, antyłańcuch, element minimalny i maksymalny (nic pod nim, nic nad nim) kontra najmniejszy i największy (pod wszystkim, nad wszystkim); przodkowie Mortimera mają dwa elementy maksymalne i żadnego największego. Podział przedziału w analizie to inny obiekt niż podział zbioru: lista punktów cięcia, a drobnienie podziałów jest porządkiem częściowym.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 04_Sets/orderings/examples/orderings.py
```

## See also

- [Relations and functions are sets of pairs](../relations_and_functions/README.md) — what a relation is before properties are asked of it
- [Equivalence relations, partitions and the kernel of a function](../equivalence_and_partitions/README.md) — the first family of names, in full
- [The algebra of sets](../algebra_of_sets/README.md#is-a-partial-order) — ⊆ as a poset, and why Python cannot sort sets
- [Ordinals](../../13_Axioms_of_Set_Theory/ordinals/README.md) — well-orderings, the linear orders in which every descent is finite
- [Function katas](../function_katas/README.md) — Hrbacek and Jech's exercise 4.1, the same six properties on six relations
- Robert André, *Set Theory: An Introduction to Axiomatic Reasoning*, chapters 5 to 8 (free; see [the reading guide](../../reading_guides/set_theory/README.md)); Karel Hrbacek and Thomas Jech, *Introduction to Set Theory*, chapter 2, section 5
- [Partially ordered set ↗](https://en.wikipedia.org/wiki/Partially_ordered_set) — Wikipedia
