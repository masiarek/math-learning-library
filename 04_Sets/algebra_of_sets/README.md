# The algebra of sets

**Level:** 101 → 201 · for anyone who has drawn a Venn diagram, or written `if a and not b`

**One line:** Union, intersection and complement are *or*, *and* and *not* applied to one question, "is x a member?", so every law of set algebra, De Morgan's included, is a law of logic in disguise; that is also why a finite check of membership proves it, why the complement needs a universe, and why ⊆ orders sets only partially.

## One question per member

[What is a set?](../what_is_a_set/README.md) opens with the rule that a set is nothing but its members. So to know a set built from A and B, it is enough to know, for each object x, whether x is in it, and that answer depends only on whether x is in A and whether x is in B:

| Set | x is a member when | Logic | Python |
|---|---|---|---|
| A ∪ B | x ∈ A **or** x ∈ B | ∨ | `a \| b` |
| A ∩ B | x ∈ A **and** x ∈ B | ∧ | `a & b` |
| A ∖ B | x ∈ A **and not** x ∈ B | ∧ ¬ | `a - b` |
| A △ B | x ∈ A **or** x ∈ B, **not both** | exclusive or | `a ^ b` |
| A′ (complement) | **not** x ∈ A | ¬ | `U - a` |
| A ⊆ B | **if** x ∈ A **then** x ∈ B, for every x | ⇒ | `a <= b` |

Section 2 of the program prints this table for two small sets and then checks the translation for every member of every pair of subsets of U = {1, 2, 3, 4}. The ⊆ row is the [if–then of the logic chapter](../../11_Logic/converse_and_contrapositive/README.md) applied to every member at once.

## The complement needs a universe

A′, "everything not in A", has no meaning on its own: not in A, out of what? Not a number, the numbers 1 to 4, every object that exists? The last choice is exactly the one [Russell's paradox](../definition_on_trial/README.md#the-repair-and-the-paradox-as-a-theorem) rules out, since there is no set of everything. So a complement is always relative to a **universal set** U fixed in advance, and A′ = U ∖ A. Python's `set` has no complement operator for the same reason; the code has to name U and write `U - a`. (Books that admit *classes* as objects, such as Robert André's in [the reading guide](../../reading_guides/set_theory/README.md), write an absolute complement {x : x ∉ A} with no U, which is a class and never a set; to get a set they intersect with a chosen U, which is the same rule in different bookkeeping.)

The universal set is not a set of everything, then, but the set of everything *under discussion*, chosen before the problem starts: the whole numbers 1 to 9 in a textbook exercise, the 52 cards in a probability question, every student in a survey. Each set in the problem is a subset of it. Sullivan's *Precalculus* takes U = {1, 2, 3, 4, 5, 6, 7, 8, 9} and A = {1, 3, 5, 7, 9}, the odd ones, and gets Ā = {2, 4, 6, 8}, the even ones; and since every member of U is odd or not, and none is both, A ∪ Ā = U and A ∩ Ā = ∅ follow at once, which is the book's "do you see why". The bar is Sullivan's spelling of the complement; A′ and Aᶜ mean the same, and this library writes A′. Because U is a choice, the same A has a different complement under a different U, which section 1 of the program shows: A = {1, 2} has complement {3, 4} in {1, 2, 3, 4}, {3, 4, 5, 6} in {1, …, 6}, and ∅ in {1, 2}. A complement quoted without its universe is an unfinished sentence.

## The laws, and why they are true

Section 3 checks the standard list on every case: each law in one set on all 16 subsets of U, in two sets on all 256 pairs, in three sets on all 4,096 triples. Each law also has [a page of its own](laws/README.md), with why it is true, where it is used, the trap beside it, and a program.

| Law | Sets | Logic |
|---|---|---|
| [identity](laws/identity/README.md) | A ∪ ∅ = A, A ∩ U = A | p ∨ false = p, p ∧ true = p |
| [domination](laws/domination/README.md) | A ∪ U = U, A ∩ ∅ = ∅ | p ∨ true = true, p ∧ false = false |
| [idempotent](laws/idempotent/README.md) | A ∪ A = A, A ∩ A = A | p ∨ p = p |
| [complement](laws/complement/README.md) | A ∪ A′ = U, A ∩ A′ = ∅ | p ∨ ¬p = true, p ∧ ¬p = false |
| [double complement](laws/double_complement/README.md) | (A′)′ = A | ¬¬p = p |
| [commutative, associative](laws/commutative_associative/README.md) | A ∪ B = B ∪ A, … | p ∨ q = q ∨ p, … |
| [distributive](laws/distributive/README.md) | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C), and with ∪ and ∩ swapped | p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) |
| [absorption](laws/absorption/README.md) | A ∪ (A ∩ B) = A | p ∨ (p ∧ q) = p |
| [**De Morgan**](laws/de_morgan/README.md) | (A ∪ B)′ = A′ ∩ B′, (A ∩ B)′ = A′ ∪ B′ | ¬(p ∨ q) = ¬p ∧ ¬q |
| [difference](laws/difference/README.md) | A ∖ B = A ∩ B′ | p ∧ ¬q |

Why is checking one small universe enough? Because each law is decided member by member. Whether x is on the left side of De Morgan's law depends only on whether x ∈ A and whether x ∈ B, which is one of four cases, and the law is true in all four: that is its truth table. A universe of four members with all their subsets meets every combination of memberships there is, so the exhaustive check is a proof, not a sample. The same argument makes set algebra and the logic of *and*, *or* and *not* one structure, a **Boolean algebra**; the [laws of an operation](../../06_Algebraic_Structures/laws_of_an_operation/README.md) page lists what such lists of laws have in common.

De Morgan's law is the one worth memorising in words: *not (either)* is *neither*, and *not (both)* is *at least one missing*. In code it is the reason `not (a or b)` can be written `not a and not b`, and in SQL the reason `NOT (x = 1 OR y = 2)` is `x <> 1 AND y <> 2`.

## Laws that look true and are not

Algebra with numbers invites some moves that set algebra does not allow. Section 4 searches all cases and prints the smallest counterexample for each:

- **(A ∪ B) ∖ B = A** fails when A and B overlap: A = {1}, B = {1} gives ∅. Taking B back out also takes out the part of A that was in B. Union is not addition, and difference does not undo it.
- **(A ∖ B) ∪ B = A** fails when B has members outside A.
- **A ∖ (B ∖ C) = (A ∖ B) ∖ C** fails: difference is not associative, which is the "left to right" of Python's `s1 - s2 - s3` (see [a set is a hash table ↗](https://masiarek.github.io/python-learning-library/04_Names_and_Objects/a_set_is_a_hash_table/index.html)).
- **A ∖ B = B ∖ A** fails; difference is not commutative.
- **A ∪ B = A ∪ C implies B = C** fails: A = {1}, B = ∅, C = {1}. There is no cancellation for union, because A can absorb the difference.

One counterexample kills a law. For the true laws of section 3 the same search finds none, and since the search covers every case, that is the proof.

## Venn diagrams

A **Venn diagram** draws sets as circles inside a rectangle, and the rectangle is U: that is why a textbook's figure carries "universal set" in its corner. The part of the rectangle outside a circle is that set's complement, so the complement can only be drawn once the rectangle is. Two positions of the circles say something on their own: a circle drawn inside another says A ⊆ B, and two circles drawn apart say A ∩ B = ∅, sets with no member in common, called **disjoint**. The usual picture of overlapping circles claims nothing yet; it only makes room for every region, and a region may turn out empty.

A Venn diagram of n sets draws one region for each pattern of membership: in or out of each set, 2ⁿ patterns. Three circles make 8 regions, and the eighth, outside all three, is the complement of the union. Section 5 lists the regions for the two diagrams from the notes. In the first, red {1, 2, 5} and yellow {1, 6} overlap at 1 and green {4, 7} stands apart, so every region touching green and another colour is empty and `green.isdisjoint(red | yellow)` is True. In the second, 1 is in all three and the centre region is {1}. Every set operation is a choice of regions: union takes all regions inside any circle, intersection the centre, symmetric difference of two the pair of outer lenses.

## ⊆ is a partial order

⊆ has the three properties of an order: every set is a subset of itself (reflexive), A ⊆ B and B ⊆ A together force A = B (antisymmetric, which is extensionality again), and A ⊆ B ⊆ C gives A ⊆ C (transitive). Unlike ≤ on numbers, it is not **total**: {1} and {2} are neither above nor below each other. Of the 120 pairs of distinct subsets of {1, 2, 3, 4}, only 65 are comparable. A set with an order like this is a **partially ordered set**, or poset, and the subsets of a set are the standard example.

That has a consequence in Python. `sorted()` compares with `<`, and for sets `<` means proper subset. Given sets that are not all comparable, it returns an order that depends on the input order and means nothing: section 6 sorts the same three sets three ways and gets three answers. To sort sets, give a key that is a total order, such as `key=lambda s: (len(s), sorted(s))`.

## Symmetric difference is exclusive or

A △ B is the members of exactly one of A and B, (A ∖ B) ∪ (B ∖ A), which is also (A ∪ B) ∖ (A ∩ B): in logic, *exclusive or*. For A = {1, 2, 3, 4} and B = {1, 4, 5} it is {2, 3, 5}, since each of 2, 3 and 5 is in one set but not both. Books write it A △ B, A ⊖ B, A ∇ B or A + B; Wolfram MathWorld recommends ⊖, because the other symbols already mean something else elsewhere in mathematics.

The A + B spelling is not a whim. Section 7 checks that △ is associative and commutative, that ∅ is an identity (A △ ∅ = A) and that every set is its own inverse (A △ A = ∅). So the subsets of U form a **group** under △, in the sense of [the laws of an operation](../../06_Algebraic_Structures/laws_of_an_operation/README.md), and with ∩ as multiplication they form a ring, the algebra of bits under XOR and AND. Two consequences are worth keeping. A chain A △ B △ C △ … keeps exactly the members that occur an odd number of times, because each pair of occurrences cancels: {1, 2, 3} △ {3, 4, 5} △ {5, 6, 7} △ {7, 8, 1} = {2, 4, 6, 8}. And A △ B = ∅ exactly when A = B, which makes the symmetric difference a test of equality.

## Quantifiers over a union

Statements about *every* or *some* member of a set follow the same logic. Section 8 checks six claims on every pair of subsets of {1, 2, 3} and every predicate p on it, 512 cases:

- ∀x ∈ A ∪ B: p(x) is the same as (∀x ∈ A: p(x)) ∧ (∀x ∈ B: p(x)), and ∃x ∈ A ∪ B: p(x) is the same as (∃x ∈ A: p(x)) ∨ (∃x ∈ B: p(x)). A union splits a *for all* into *and* and a *there exists* into *or*.
- Over an intersection only one direction survives. ∃x ∈ A ∩ B: p(x) gives an x in A and in B, but an x in A and a *different* x in B do not give one in A ∩ B: A = {1}, B = {2}, p true on both.
- Likewise (∀x ∈ A: p) ∨ (∀x ∈ B: p) does not give ∀x ∈ A ∪ B: p. The smallest counterexample the search finds uses A = ∅, where ∀x ∈ ∅: p(x) is true for every p because there is no x to fail. That vacuous truth is also the whole proof that ∅ ⊆ A.

The section ends with the rule that turns every set equality into two subset proofs: A = B exactly when A ⊆ B and B ⊆ A.

## What the program prints

<!-- output:algebra_of_sets -->
*Verified output of [`algebra_of_sets.py`](examples/algebra_of_sets.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. THE UNIVERSE AND ITS SUBSETS
   U = {1, 2, 3, 4}, and it has 2^4 = 16 subsets:
     {}            {1}           {2}           {3}           {4}           {1, 2}        {1, 3}        {1, 4}
     {2, 3}        {2, 4}        {3, 4}        {1, 2, 3}     {1, 2, 4}     {1, 3, 4}     {2, 3, 4}     {1, 2, 3, 4}
   the complement of A = {1, 2} is U - A = {3, 4}.
   Python's set has no complement operator: 'everything not in A'
   means nothing until U is fixed, so the code has to write U - A.
   U is a choice, and a different choice gives a different complement
   of the same A = {1, 2}:
     U = {1, 2, 3, 4}           U - A = {3, 4}
     U = {1, 2, 3, 4, 5, 6}     U - A = {3, 4, 5, 6}
     U = {1, 2}                 U - A = {}
   Whatever U is, A | (U - A) = U and A & (U - A) = {}: each x in U is
   in A or not, and none is both. Checked for the three universes: True

2. EACH OPERATION IS A LOGICAL OPERATION ON MEMBERSHIP
   A = {1, 2}, B = {2, 3}; for each x in U, is x in the result?
       x  in A   in B   A | B  A & B  A - B  A ^ B  U - A
       1  True   False  True   False  True   True   False
       2  True   True   True   True   False  False  False
       3  False  True   True   False  False  True   True
       4  False  False  False  False  False  False  True
   |  is or,  &  is and,  -  is 'and not',  ^  is 'exclusive or',
   U - A is not. Checked for every x in every pair of subsets: True
   and A <= B is 'if x in A then x in B', for every pair: True

3. THE LAWS, CHECKED ON EVERY CASE
   law                statement                           cases  holds
   identity           A | {} = A,   A & U = A                16  True
   domination         A | U = U,   A & {} = {}               16  True
   idempotent         A | A = A,   A & A = A                 16  True
   complement         A | A' = U,  A & A' = {}               16  True
   double complement  (A')' = A                              16  True
   commutative        A | B = B | A,  A & B = B & A         256  True
   De Morgan          (A | B)' = A' & B'                    256  True
   De Morgan          (A & B)' = A' | B'                    256  True
   absorption         A | (A & B) = A                       256  True
   difference         A - B = A & B'                        256  True
   associative        (A | B) | C = A | (B | C)            4096  True
   distributive       A & (B | C) = (A & B) | (A & C)      4096  True
   distributive       A | (B & C) = (A | B) & (A | C)      4096  True
   Every law holds in every case. Replace | & ' by or, and, not and each
   line is a law of logic; that is why they are true, and why checking
   the membership of one x settles them for all sets at once.

4. LAWS THAT LOOK TRUE AND ARE NOT: THE SEARCH FINDS A COUNTEREXAMPLE
   (A | B) - B = A                  fails in  175 cases, e.g. A = {1}, B = {1}
   (A - B) | B = A                  fails in  175 cases, e.g. A = {}, B = {1}
   A - (B - C) = (A - B) - C        fails in 2800 cases, e.g. A = {1}, B = {}, C = {1}
   A - B = B - A                    fails in  240 cases, e.g. A = {}, B = {1}
   A | B = A | C  implies  B = C    fails in 1040 cases, e.g. A = {1}, B = {}, C = {1}
   A ^ (B | C) = (A ^ B) | C        fails in 2800 cases, e.g. A = {1}, B = {}, C = {1}
   One counterexample is enough to kill a law; for the true laws of
   section 3, the search over every case is the proof that none exists.

5. VENN DIAGRAMS: n SETS MAKE 2^n REGIONS, ONE PER PATTERN OF MEMBERSHIP
   red and yellow overlap, green apart:  red = {1, 2, 5}  yellow = {1, 6}  green = {4, 7}
     red & yellow & green               {}
     red & yellow & not green           {1}
     red & not yellow & green           {}
     red & not yellow & not green       {2, 5}
     not red & yellow & green           {}
     not red & yellow & not green       {6}
     not red & not yellow & green       {4, 7}
     green.isdisjoint(red | yellow): True
   all three overlap at 1:  red = {1, 2, 5}  yellow = {1, 6}  green = {1, 4, 7}
     red & yellow & green               {1}
     red & yellow & not green           {}
     red & not yellow & green           {}
     red & not yellow & not green       {2, 5}
     not red & yellow & green           {}
     not red & yellow & not green       {6}
     not red & not yellow & green       {4, 7}
     green.isdisjoint(red | yellow): False
   The 8th pattern, in none of the three, is everything outside the
   circles: the complement of the union, U - (R | Y | G).

6. <= IS A PARTIAL ORDER, SO SORTING SETS DOES NOT WORK
   reflexive True,  antisymmetric True,  transitive True
   but of the 120 pairs of distinct subsets only 65 are comparable;
   55 pairs, like {1} and {2}, have neither {1} <= {2} nor {2} <= {1}.
   sorted(['{3}', '{1, 2}', '{1}']) = ['{3}', '{1}', '{1, 2}']
   sorted(['{1, 2}', '{1}', '{3}']) = ['{1}', '{1, 2}', '{3}']
   sorted(['{1}', '{3}', '{1, 2}']) = ['{1}', '{3}', '{1, 2}']
   Same three sets, three different 'sorted' orders: sorted() uses <,
   which for sets is 'proper subset', and {3} is neither above nor below
   the others. Sort by a key that is a total order instead:
   sorted(..., key=lambda s: (len(s), sorted(s))) = ['{1}', '{3}', '{1, 2}']

7. SYMMETRIC DIFFERENCE: EXCLUSIVE OR, AND A GROUP
   A = {1, 2, 3, 4}, B = {1, 4, 5}:  A ^ B = {2, 3, 5}   2, 3 and 5 are each in one, not both
   (A - B) | (B - A) = {2, 3, 5}   (A | B) - (A & B) = {2, 3, 5}
   associative True   identity {} True   A ^ A = {} True   commutative True
   So the 16 subsets form a group under ^, every set its own inverse,
   which is why it is also written A + B. Adding the same set twice
   cancels, so a chain keeps exactly what occurs an odd number of times:
   {1, 2, 3} ^ {3, 4, 5} ^ {5, 6, 7} ^ {1, 7, 8} = {2, 4, 6, 8}
   and A ^ B is empty exactly when A = B, for every pair: True

8. QUANTIFIERS OVER A UNION OR AN INTERSECTION
   every A, B ⊆ {1, 2, 3} and every predicate p on it: 512 cases
     ∀x∈A∪B p  ⇒  ∀x∈A∩B p              holds
     ∀x∈A∪B p  ⇔  ∀x∈A p ∧ ∀x∈B p       holds
     ∃x∈A∩B p  ⇒  ∃x∈A p ∧ ∃x∈B p       holds
     ∃x∈A∪B p  ⇔  ∃x∈A p ∨ ∃x∈B p       holds
     ∀x∈A p ∨ ∀x∈B p  ⇒  ∀x∈A∪B p       fails, e.g. A = {}, B = {1}, p true on {}
     ∃x∈A p ∧ ∃x∈B p  ⇒  ∃x∈A∩B p       fails, e.g. A = {1}, B = {2}, p true on {1, 2}
   ∀ splits over ∪ as ∧ and ∃ splits over ∪ as ∨; over ∩ only one
   direction survives. And over ∅:
     ∀x∈∅ p is True for every p, ∃x∈∅ p is False for every p
   which is why ∅ ⊆ A: 'every x in ∅ is in A' has no x to fail on.
   and A = B exactly when A ⊆ B and B ⊆ A, for every pair of subsets of U: True
```
<!-- /output -->

## Flashcards

The page as a deck of Anki cards: [`algebra_of_sets.txt`](anki/algebra_of_sets.txt). Import with File → Import. Tags: `logic`, `definition`, `law`, `principle`, `trap`, `venn`, `order`, `example`, `python`.

## Po polsku, w skrócie

Suma, iloczyn (część wspólna) i dopełnienie zbiorów to logiczne „lub”, „i” oraz „nie” zastosowane do jednego pytania: czy x należy do zbioru? Dlatego każde prawo algebry zbiorów, na przykład prawa de Morgana (A ∪ B)′ = A′ ∩ B′ i (A ∩ B)′ = A′ ∪ B′, jest prawem logiki w przebraniu. Program sprawdza każde prawo na wszystkich podzbiorach zbioru {1, 2, 3, 4}. To jest dowód, a nie próbka, bo prawo zależy tylko od tego, do których zbiorów należy dany element, a mały uniwersum pokrywa wszystkie możliwe kombinacje.

Dopełnienie ma sens tylko względem ustalonego uniwersum U: A′ = U ∖ A. Uniwersum to nie zbiór wszystkiego, bo takiego nie ma (paradoks Russella), lecz zbiór wszystkiego, o czym mowa w zadaniu, wybrany z góry; na diagramie Venna jest nim prostokąt, w którym rysuje się koła, a dopełnienie to część prostokąta poza kołem. Ten sam zbiór A ma inne dopełnienie w innym uniwersum, więc dopełnienie bez podanego U jest niedokończonym zdaniem. Podręczniki piszą je jako A′, Ā albo Aᶜ. Koło narysowane wewnątrz drugiego koła znaczy A ⊆ B, a dwa koła osobno to zbiory rozłączne, A ∩ B = ∅. Python nie ma operatora dopełnienia i trzeba pisać `U - a`. Niektóre „prawa” kuszą, ale są fałszywe, np. (A ∪ B) ∖ B = A, bo różnica nie cofa sumy. Wreszcie zawieranie ⊆ jest porządkiem częściowym: zbiorów {1} i {2} nie da się porównać, więc `sorted()` na liście zbiorów daje przypadkową kolejność; trzeba podać klucz, np. `key=lambda s: (len(s), sorted(s))`.

## Auf Deutsch: Stichwörter

Die Gesetze von ∪, ∩ und Komplement, jedes an allen Teilmengen einer kleinen Grundmenge geprüft; die Grundmenge U entscheidet mit.

**Stichwörter:** Mengenalgebra, Vereinigung, Schnitt, Komplement, Grundmenge (universal set), De-Morgan-Gesetze, Distributivgesetz, disjunkt, Venn-Diagramm.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 04_Sets/algebra_of_sets/examples/algebra_of_sets.py
```

## See also

- [What is a set?](../what_is_a_set/README.md) — extensionality, and why there is no universal set of everything
- [Sets in Python](../python_sets/README.md) — each law as a Python operator, and why the complement has none
- [If A then B: converse, contrapositive and inverse](../../11_Logic/converse_and_contrapositive/README.md) — ⊆ is "if x ∈ A then x ∈ B"
- [The laws of an operation](../../06_Algebraic_Structures/laws_of_an_operation/README.md) — commutative, associative and distributive laws for numbers
- [Cardinality of sets](../cardinality/README.md) — why U has 2⁴ = 16 subsets
- Michael Sullivan, *Precalculus* (Pearson), Appendix A.1 *Algebra Essentials*, objective 1 *Work with Sets*: the universal set, the complement written Ā, and the Venn diagrams of subset, disjoint sets, intersection, union and complement
- [Boolean algebra ↗](https://en.wikipedia.org/wiki/Boolean_algebra_(structure)) — Wikipedia: the structure sets and logic share
- [De Morgan's laws ↗](https://en.wikipedia.org/wiki/De_Morgan%27s_laws) — Wikipedia
- [Partially ordered set ↗](https://en.wikipedia.org/wiki/Partially_ordered_set) — Wikipedia
