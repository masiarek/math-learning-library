# Choice: a product of nonempty sets is nonempty

**Level:** 201 · for anyone who has read Cori and Lascar's "utterly incomprehensible at first glance" and "so obvious that it seems superfluous to mention" on the same page and wants both sentences explained

**One line:** The axiom of choice says that from any family of nonempty sets one member of each can be picked at once; for finite families that is a theorem, for families with a rule it is unnecessary, and only for infinite families with no rule does it say anything, which is why it looks obvious, why it had to be assumed, and why it cannot be proved or refuted from the other axioms.

## The axiom, read aloud

Three statements, each of which the books call the axiom of choice, all equivalent over ZF:

- **Cori and Lascar (page 120):** the product ∏ᵢ aᵢ of a family of nonempty sets is nonempty.
- **Jech (axiom 1.9):** every family of nonempty sets has a **choice function**, an f with f(x) ∈ x for every x in the family.
- **Zermelo (1904):** for a set of pairwise disjoint nonempty sets there is a set containing exactly one member of each.

The first two are the same sentence, since a member of the product *is* a choice function: one entry per index, drawn from that index's set. Cunningham leaves the axiom out of his chapter 1 list, as Jech's ZF does, and adds it later; ZFC is ZF with it.

## Why it seems obvious, and why it is not superfluous

**For a finite family it is a theorem.** Section 2 of the program takes every family of nonempty subsets of {1, 2, 3}, 128 families in all, and counts the choice functions of each: the product of the sizes, never zero. The proof for any finite family is by induction on its size and uses no axiom. So the axiom is never needed in a finite situation, which is where intuition is trained.

**When a rule exists, no axiom is needed either.** A family of nonempty sets of natural numbers has the choice function "take the least member", because ℕ is well-ordered; section 3 runs it. The function is defined by a formula, so [replacement](../replacement/README.md) provides it. The same holds for any well-ordered family.

**It says something only for infinite families with no rule.** Russell's picture, section 4: from infinitely many pairs of shoes pick the left one, a rule; from infinitely many pairs of socks there is no rule, and "pick one from each" is precisely what the axiom grants. Cori and Lascar's two sentences are both right: the axiom is incomprehensible because it asserts the existence of a function nobody can write down, and obvious because in every case anyone has ever met, the function could be written down.

## What it buys, and what it costs

Section 5 lists the consequences, and the first three are more than consequences: they are equivalent to the axiom over ZF. Every set can be well-ordered (Zermelo 1904, Cori and Lascar's Theorem 7.37); Zorn's lemma, the form algebra uses; every vector space has a basis. Then come the results the book names on page 120 as needing it, the Hahn–Banach theorem and Krull's theorem on maximal ideals; then the cost, a set of reals with no length (Vitali) and the Banach–Tarski decomposition of a ball into five pieces that reassemble into two balls, which the book calls paradoxical. Finally the two theorems the book promises not to prove: Gödel (1938) showed the axiom cannot be refuted from ZF, Cohen (1963) that it cannot be proved. It is independent, and mathematicians, in the book's phrase, commonly use it.

## The equivalent forms, and the weaker ones

Halbeisen's chapter 6, "Forms of choice", is a catalogue of statements that look nothing like the axiom and are the axiom. The owner sent its first pages, and the program's section 6 runs each form on a finite set, where every one of them is a theorem, so that the words are tied to something checkable before the infinite case is believed.

| Form | What it says | Status over ZF |
|---|---|---|
| **Well-ordering principle** (Zermelo 1904) | every set can be well-ordered | equivalent (Theorem 3.23) |
| **Kuratowski–Zorn lemma** | a nonempty poset in which every chain has an upper bound has a maximal element | equivalent (Theorem 6.0) |
| **Teichmüller's principle**, also Tukey's lemma | a nonempty family of finite character has a maximal member under ⊆ | equivalent (Theorem 6.0) |
| **Downward basis principle** | every set of vectors that generates a vector space contains a basis | equivalent (Theorem 6.1) |
| **Vector-space-basis principle** | every vector space has a basis | equivalent, with foundation (Theorem 6.2); open without it |
| **Multiple choice** | a function picking a nonempty finite subset of each set of a family | equivalent, with foundation (Theorem 6.2) |
| **Kurepa's principle** | every poset has a maximal antichain | equivalent, with foundation (Theorem 6.2); not without it |
| **Trichotomy of cardinals** | any two cardinals are comparable | equivalent (Hartogs 1915) |
| **m² = m** for every infinite cardinal | | equivalent (Tarski 1924) |
| **Prime ideal theorem** | every Boolean algebra has a prime ideal; equivalently every filter extends to an ultrafilter | strictly weaker (Halpern and Lévy 1971) |
| **Countable choice**, **dependent choice** | a choice function for countable families; a sequence each term chosen from the next | strictly weaker, and all analysis needs |

A family has **finite character** when a set belongs to it exactly if all its finite subsets do: the linearly independent sets of vectors are the example, since dependence is witnessed by finitely many vectors. The program takes the seven nonzero vectors of GF(2)³, lists the 57 independent subsets, checks finite character, and finds the 28 maximal members, which are the bases, each of size 3; then checks that every generating set contains one. For the divisors of 12 under divisibility it enumerates every chain and every antichain, finds the one maximal element, 12, and the maximal antichains. On a finite poset all of this is exhaustion; on an infinite one it is the axiom, and the proofs in the book run by transfinite recursion along a well-ordering that the axiom supplies.

The two proofs most worth reading are Halbeisen's (b) ⇒ (c) on page 134, where a chain of sets of finite character has its union as an upper bound, and his (b) ⇒ (a) of Theorem 6.1 on pages 135 and 136, where the choice function for a family of sets is pulled out of a basis of a vector space of rational functions over a field: the axiom of choice hidden inside linear algebra. The weaker forms are where the subject becomes delicate: the prime ideal theorem, which the program's section 7 illustrates by listing the three prime ideals of the Boolean algebra of subsets of {1, 2, 3}, is enough for Tychonoff's theorem for Hausdorff spaces and the completeness theorem of logic, and not enough for a basis of every vector space.

## What the program prints

<!-- output:choice -->
*Verified output of [`choice.py`](examples/choice.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. THE AXIOM, THREE WAYS
   Cori and Lascar: the product ∏ a_i of a family of nonempty sets is nonempty.
   Choice function:  for every set a of nonempty sets there is f with f(x) ∈ x for x ∈ a.
   Zermelo 1904:     for pairwise disjoint nonempty sets there is a set meeting each in one point.
   A member of the product IS a choice function: a tuple with one entry per index.

2. FOR FINITE FAMILIES IT IS A THEOREM: COUNT THE CHOICE FUNCTIONS
   the 7 nonempty subsets of {1, 2, 3}, and every family drawn from them:
     family {1}, {2}                       choice functions:  1   e.g. pick (1, 2)
     family {1}, {3}                       choice functions:  1   e.g. pick (1, 3)
     family {1}, {1, 2}                    choice functions:  2   e.g. pick (1, 1)
     family {1}, {1, 3}                    choice functions:  2   e.g. pick (1, 1)
   families checked: 128; with at least one choice function: 128
   The count is the product of the sizes, never zero. For a finite family
   the proof is by induction on its size and needs no axiom.

3. WHEN A RULE EXISTS, NO AXIOM IS NEEDED
   a family of nonempty sets of natural numbers: {2, 5, 9}, {3, 7}, {8}
   rule 'take the least':  [2, 3, 8]
   ℕ is well-ordered, so 'the least member' is a formula, and the choice
   function exists by replacement. The same for any well-ordered set.

4. RUSSELL'S SHOES AND SOCKS
   infinitely many pairs of shoes:  pick the left one   (a rule: no axiom)
   infinitely many pairs of socks:  the two are alike    (no rule: the axiom)
   With finitely many pairs of socks you point at one from each; with
   infinitely many, 'point at one from each' is exactly what the axiom grants.

5. WHAT IT BUYS, AND WHAT IT COSTS
   Zermelo 1904           every set can be well-ordered
   Zorn's lemma           a chain-bounded poset has a maximal element
   linear algebra         every vector space has a basis
   analysis               Hahn–Banach; a non-measurable set of reals (Vitali)
   Banach–Tarski 1924     one ball cut into five pieces reassembles as two
   Gödel 1938             AC cannot be refuted from ZF (true in L)
   Cohen 1963             AC cannot be proved from ZF either
   The first three are equivalent to the axiom over ZF, not consequences
   of it: assume any one and you have assumed choice.

6. THE EQUIVALENT FORMS, ON A FINITE SET WHERE EACH IS A THEOREM
   the divisors of 12 under 'divides': chains: 31, every chain has an
   upper bound: True; maximal elements: [12]   (Zorn's lemma holds)
   antichains: 9; maximal antichains: 5, e.g. (1,) and (4, 6)   (Kurepa's principle holds)
   the 7 nonzero vectors of GF(2)³: linearly independent subsets: 57;
   the family has finite character: True; maximal members: 28,
   all of size {3}: the bases   (Teichmüller's principle holds)
   generating sets: 28; each contains a basis: True   (downward basis principle holds)
   well-orderings of a 4-set: 24, the orderings of its
   members in a row   (well-ordering principle holds)
   On a finite set every form is a theorem. Halbeisen's chapter 6 proves that on
   arbitrary sets each is equivalent to the axiom: AC ⇔ Zorn ⇔ Teichmüller ⇔
   downward basis ⇔ well-ordering ⇔ trichotomy of cardinals ⇔ m² = m, and, with
   foundation, ⇔ Kurepa ⇔ every vector space has a basis ⇔ multiple choice.

7. A BOOLEAN ALGEBRA, WHERE THE WEAKER FORM LIVES
   commutativity    on all 512 triples of subsets of {1, 2, 3}: True
   associativity    on all 512 triples of subsets of {1, 2, 3}: True
   distributivity   on all 512 triples of subsets of {1, 2, 3}: True
   absorption       on all 512 triples of subsets of {1, 2, 3}: True
   complementation  on all 512 triples of subsets of {1, 2, 3}: True
   De Morgan        on all 512 triples of subsets of {1, 2, 3}: True
   ideals of this algebra (down-closed, closed under ∪): 8; prime ideals: 3:
      the sets avoiding 3, 4 of them
      the sets avoiding 2, 4 of them
      the sets avoiding 1, 4 of them
   The prime ideal theorem, 'every Boolean algebra has a prime ideal', follows
   from choice and is strictly weaker than it (Halpern and Lévy 1971): the
   first of the weaker forms, with countable choice and dependent choice.
```
<!-- /output -->

## Po polsku, w skrócie

Pewnik wyboru mówi, że z każdej rodziny zbiorów niepustych można naraz wybrać po jednym elemencie: iloczyn kartezjański takiej rodziny jest niepusty, czyli istnieje funkcja wyboru f z f(x) ∈ x dla każdego x. Cori i Lascar piszą na jednej stronie, że jest „niezrozumiały na pierwszy rzut oka" i „tak oczywisty, że zbędny", i oba zdania są prawdziwe. Dla rodzin skończonych to twierdzenie: program liczy funkcje wyboru dla wszystkich 128 rodzin niepustych podzbiorów {1, 2, 3} i nigdy nie dostaje zera. Gdy istnieje reguła, na przykład „weź najmniejszy" w zbiorach liczb naturalnych, aksjomat też nie jest potrzebny. Mówi coś dopiero dla rodzin nieskończonych bez reguły: buty można wybrać regułą „lewy", skarpetek nie. Równoważne mu są twierdzenie Zermela o dobrym uporządkowaniu, lemat Zorna i istnienie bazy każdej przestrzeni liniowej; kosztem są zbiór Vitalego i paradoks Banacha–Tarskiego; Gödel (1938) i Cohen (1963) pokazali, że z ZF nie da się go ani obalić, ani udowodnić.

Rozdział 6 Halbeisena wylicza postaci równoważne pewnikowi: zasadę dobrego uporządkowania, lemat Kuratowskiego–Zorna, zasadę Teichmüllera (rodzina o charakterze skończonym ma element maksymalny), zasadę Kurepy (każdy porządek częściowy ma maksymalny antyłańcuch), istnienie bazy każdej przestrzeni liniowej, porównywalność mocy; słabsze są twierdzenie o ideale pierwszym i przeliczalny wybór. Program sprawdza każdą z nich na zbiorze skończonym, gdzie wszystkie są twierdzeniami.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 13_Axioms_of_Set_Theory/choice/examples/choice.py
```

## See also

- [Replacement](../replacement/README.md) — why a rule makes the axiom unnecessary
- [Ordinals](../ordinals/README.md) — well-orderings, which the axiom provides for every set
- [Two balls from one](../two_balls_from_one/README.md) — the Banach–Tarski theorem, the axiom's most famous cost, with the group it lives in checked by program
- [Orderings](../../04_Sets/orderings/README.md) — chains, antichains and maximal elements, the words of Zorn's lemma
- Lorenz Halbeisen, *Combinatorial Set Theory*, 3rd ed. (Springer, 2025), chapter 6, "Forms of choice": Theorems 6.0 to 6.2 and the prime ideal theorem
- [Set theory: a reading guide](../../reading_guides/set_theory/README.md) — Zermelo 1904, Gödel 1938 and Cohen 1963 among the founding papers
- [Axiom of choice ↗](https://en.wikipedia.org/wiki/Axiom_of_choice) — Wikipedia
