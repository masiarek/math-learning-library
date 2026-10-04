# What is a set?

**Level:** 101 · for anyone who wants the definition first, and the argument about the textbook's version afterwards

**One line:** A set is one object determined by its members and by nothing else: *set* and *member of* are the undefined words, two sets with the same members are one set, and a rule picks members out of a set you already have.

## The definition

> A **set** is a single object that has **members**, also called **elements**. The sentence a ∈ A says that a is a member of A, and a ∉ A that it is not. *Set* and *is a member of* are not defined through other words: they are the first words of mathematics, and everything else said about sets, equality, subset, union, is defined through them. For every object a and every set A, exactly one of a ∈ A and a ∉ A holds, whether or not anyone knows which. Four rules say how these words behave.
>
> 1. **Extensionality.** Two sets with the same members are the same set. A set records which objects are its members and nothing else: not the order they were named in, not how many times, not the rule that picked them out.
> 2. **A set is one object.** It can be a member of another set, so there are sets of sets. ∅ has no members and {∅} has one, so they are different sets.
> 3. **Separation.** A rule does not make a set out of nothing. For a set A already in hand and a property P, there is a set {x ∈ A : P(x)}, the members of A that satisfy P. There is no set {x : P(x)} of everything that satisfies P.
> 4. **There is a set with no members**, written ∅, and by rule 1 there is only one.

That is the whole definition, and it is what textbooks are reaching for when they open with "a set is a well-defined collection of distinct objects". What that sentence gets right, what it leaves out, and how a rule as sharp as "x is not a member of itself" can fail to give any set at all, Russell's paradox, is the subject of [The textbook definition on trial](../definition_on_trial/README.md). This page stays with the definition and lets a program check each rule.

## What each rule buys

**The undefined words.** "A set is a collection" explains the word by a synonym, which is why it cannot be the definition: something has to be the first undefined word, and in mathematics it is *set* together with *member of*. Modern treatments say what sets do instead of what they are, which is what the axioms of [Zermelo–Fraenkel set theory](../../13_Axioms_of_Set_Theory/README.md) are for, and the four rules above are the first of them in plain words. Python makes the same choice: `x in A` is the primitive operation of a set, and section 1 of the program writes equality and subset in it alone, then checks on all 64 pairs of subsets of {0, 1, 2} that its versions agree with Python's `==` and `<=`. Nothing is lost, because there was nothing more to a set than its [membership](../../GLOSSARY.md#membership).

**[Extensionality](../../GLOSSARY.md#extensionality)** is the rule a first course uses on every page without stating it. It is why {2, 5} = {5, 2}, why {1, 1, 2} is a legal and slightly silly way to write {1, 2}, and why a set built by one rule can be the same set as one built by another. Section 2 checks all three. It is also rule 4's "only one": two rules that select nothing have the same members, none, so by extensionality they select the same set, and *the* [empty set](../../GLOSSARY.md#empty-set) is a correct phrase. The axiom itself, in the formal language, is on [its own page](../../13_Axioms_of_Set_Theory/extensionality/README.md).

**A set is one object.** This is the rule that makes set theory a foundation rather than a notation. Because a set is a single thing, it can be a member of another set, so a function can be a set of pairs, a number can be a set, and Russell's question "is this set a member of itself?" can be asked at all. Section 3 checks the two consequences that trip readers up. ∅ and {∅} are different sets: an empty box is still a box, and a box holding an empty box holds one thing. And ∈ looks exactly one level down: 1 ∈ {1} and {1} ∈ {{1}}, while 1 ∉ {{1}}, so a member of a member is not a member. The last line of the section is the reason the box picture misleads: 1 is a member of four of the eight subsets of {0, 1, 2} at once, and a marble sits in one box.

**[Separation](../../GLOSSARY.md#comprehension-separation-subset-axiom)** says what a rule may do. It may cut: from a set A you already have, it picks the members that satisfy it. It may not create: there is no set of everything that satisfies a rule, and the trial page shows what goes wrong when a definition promises otherwise. Section 4 runs Russell's rule the permitted way. From A = {∅, {∅}, {{∅}}}, the rule "x is not a member of itself" picks a set R, and R is not a member of A. That is not an accident of this A: if R were a member y of A, then asking whether y ∈ y would get opposite answers from A's membership and from R's rule. So the rule that used to give a paradox now gives a theorem, no set has every set as a member, and [the trial page](../definition_on_trial/README.md#the-repair-and-the-paradox-as-a-theorem) checks it on every one of the 512 universes of three objects. The axiom scheme is on [its own page](../../13_Axioms_of_Set_Theory/comprehension/README.md) too.

## What the program prints

<!-- output:what_is_a_set -->
*Verified output of [`what_is_a_set.py`](examples/what_is_a_set.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. MEMBERSHIP IS THE ONLY PRIMITIVE
   Define A = B as: every member of A is in B, and every member of B is in A.
   Define A ⊆ B as: every member of A is in B.
   subsets of {0, 1, 2}: 8; pairs of them: 64
   same_members(A, B) == (A == B) on every pair:  True
   is_subset(A, B) == (A <= B) on every pair:     True
   Python's == and <= on sets add nothing to 'in'. 'Set' and 'member of'
   are the undefined words; equality and subset are written in them.

2. EXTENSIONALITY: A SET IS ITS MEMBERS AND NOTHING ELSE
   {2, 5} == {5, 2}                                     is True   order is not recorded
   {1, 1, 2} == {1, 2}                                  is True   repeats are not recorded
   {n in -5..5 : n*n < 10} == {-3..3}                   is True   the rule is not recorded
   {n in 0..9 : n*n < 0} == {w in [set] : len(w) > 5}   is True
   distinct empty sets among the two:  1
   Two rules that select nothing select the same set: THE empty set.

3. A SET IS ONE OBJECT, SO A SET CAN BE A MEMBER
   len(∅) = 0,  len({∅}) = 1,  ∅ == {∅} is False
   1 ∈ {1}: True,  {1} ∈ {{1}}: True,  1 ∈ {{1}}: False
   ∈ looks exactly one level down: a member of a member is not a member.
   subsets of {0, 1, 2} that have 1 as a member:  4 of 8
   One object is a member of many sets at once: a set is not a box it sits in.

4. SEPARATION: A RULE PICKS FROM A SET YOU ALREADY HAVE
   A = {∅, {∅}, {{∅}}}, 3 members
   R = {x ∈ A : x ∉ x} has 3 members;  R == A is True
   R ∈ A is False
   Russell's rule, cut from A, is a harmless set, and it is never a member of
   the set it was cut from. So no set has every set as a member.
```
<!-- /output -->

## Flashcards

The page as a deck of Anki cards: [`what_is_a_set.txt`](anki/what_is_a_set.txt). Import with File → Import. Tags: `definition`, `axiom`, `theorem`, `trap`, `connection`. The case against the textbook's sentence has a deck of its own, on [the trial page](../definition_on_trial/README.md#flashcards).

## Po polsku, w skrócie

Zbiór to pojedynczy obiekt, który ma elementy. Słów *zbiór* i *należy do* (a ∈ A) nie definiuje się przez inne słowa: są pierwotne, a wszystko inne o zbiorach, równość, zawieranie, sumę, definiuje się przez nie. O każdym obiekcie jest rozstrzygnięte, czy należy do danego zbioru, choć nie zawsze wiadomo, jak. Cztery reguły mówią, jak te słowa się zachowują. Po pierwsze, ekstensjonalność: dwa zbiory o tych samych elementach to jeden zbiór; zbiór pamięta tylko, co do niego należy, a nie kolejność, powtórzenia ani regułę, która go wyznaczyła. Po drugie, zbiór jest jednym obiektem, więc może być elementem innego zbioru: {∅} ma jeden element, a ∅ żadnego. Po trzecie, wyróżnianie (separacja): reguła nie tworzy zbioru z niczego, lecz wybiera elementy zbioru A, który już mamy, {x ∈ A : P(x)}; zbioru {x : P(x)} „wszystkiego, co spełnia P" nie ma. Po czwarte, istnieje zbiór pusty, a dzięki pierwszej regule tylko jeden.

Program sprawdza każdą regułę: że równość i zawieranie dają się zdefiniować przez samo należenie (zgodność z `==` i `<=` Pythona na wszystkich 64 parach podzbiorów {0, 1, 2}), że {2, 5} = {5, 2} i {1, 1, 2} = {1, 2}, że 1 ∈ {1} ∈ {{1}}, ale 1 ∉ {{1}}, oraz że zbiór wycięty regułą Russella ze zbioru A jest zwykłym zbiorem, który nigdy nie należy do A. Dlaczego podręcznikowa „dobrze określona kolekcja różnych obiektów" nie jest definicją, pokazuje osobna strona, na której ta definicja staje przed sądem.

## Auf Deutsch: Stichwörter

Eine Menge ist durch ihre Elemente bestimmt: keine Reihenfolge, keine Wiederholung, Zugehörigkeit entscheidbar, Gleichheit durch Extensionalität.

**Stichwörter:** Menge, Element, Zugehörigkeit (∈), Extensionalität, keine Reihenfolge, keine Wiederholung, leere Menge, Teilmenge, aufzählende und beschreibende Schreibweise.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 04_Sets/what_is_a_set/examples/what_is_a_set.py
```

## See also

- [The textbook definition on trial](../definition_on_trial/README.md) — the case against "a well-defined collection of distinct objects": what it leaves out, Russell's paradox, and the repair
- [Sets in Python](../python_sets/README.md) — each rule as one line of Python: extensionality is `==`, separation is a comprehension
- [The algebra of sets](../algebra_of_sets/README.md) — union, intersection and complement, built on membership once the definition is in place
- [Extensionality](../../13_Axioms_of_Set_Theory/extensionality/README.md) — rule 1 as an axiom, in the formal language
- [Comprehension](../../13_Axioms_of_Set_Theory/comprehension/README.md) — rule 3 as an axiom scheme, and why the unrestricted version contradicts itself
- [The axioms of set theory](../../13_Axioms_of_Set_Theory/README.md) — the chapter that says what sets do, one axiom per page
- [A definition is a test](../../06_Algebraic_Structures/a_definition_is_a_test/README.md) — the same style of definition for groups and rings: say what the objects must do
