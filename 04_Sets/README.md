# 04_Sets — what is this collection, exactly?

**Level:** 101 · for anyone who has written a pair of coordinates

Before a chapter can talk about how long a set is, or how many points it holds, it has to be clear what a set *is* and how new ones are built from old ones. This chapter is that groundwork: the constructions that every later page takes for granted, each one checked on real sets by a program that runs.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [What is a set?](what_is_a_set/README.md) | What is a set, in four rules, and what does each rule buy? |
| 2 | [The textbook definition on trial](definition_on_trial/README.md) | Is "a well-defined collection of distinct objects" a definition, and why does a sharp rule not always give a set? |
| 3 | [Sets in Python](python_sets/README.md) | Where is each idea of this chapter in Python, and why is the complement the one operator it lacks? |
| 4 | [The algebra of sets](algebra_of_sets/README.md) | Why are the laws of union, intersection and complement the laws of logic, and why can't Python sort a list of sets? |
| 5 | [Reading a set expression](reading_set_expressions/README.md) | What does A ∪ B ∩ C mean without brackets, and why are two classic notation mistakes also Python bugs? |
| 6 | [The Cartesian product](cartesian_product/README.md) | What is ℝ², and why is A × B not the same set as B × A? |
| 7 | [Cardinality of sets](cardinality/README.md) | What do the bars in \|A\| mean, and why is "how many" defined by matching instead of counting? |
| 8 | [Relations and functions are sets of pairs](relations_and_functions/README.md) | Why does a book on sets have chapters on functions and graphs, and why is a database table a relation? |
| 9 | [Equivalence relations, partitions and the kernel of a function](equivalence_and_partitions/README.md) | Why are "reflexive, symmetric, transitive" the right three words, and what does a function's kernel have to do with cutting a set into blocks? |
| 10 | [Orderings](orderings/README.md) | Which combinations of reflexive, symmetric, antisymmetric and transitive deserve a name, what a poset is, and why a set can have two maximal elements and no maximum? |
| 11 | [Cantor–Schröder–Bernstein](schroeder_bernstein/README.md) | Why do two one-to-one maps, one each way, give a bijection, and what does that buy without the axiom of choice? |
| 12 | [Multisets](multisets/README.md) | What is a set that counts, why are gcd and lcm its ∩ and ∪, and which set law does it lose? |
| 13 | [Ramsey's theorem](ramsey/README.md) | How can combinatorics be relevant to sets, and why does the answer stop being a number once the set is infinite? |
| 14 | [Set katas](set_katas/README.md) | Is this exercise's claim true, and which of four moves proves it? Cunningham's first exercises, checked before you prove them |
| 15 | [Function katas](function_katas/README.md) | Hrbacek and Jech's exercises on functions, 3.1 to 3.13 and 4.1 to 4.3, checked by program and solved move by move |

## The through-line

The first lesson says what a set is, in four rules: a set is its members and nothing more, so two sets with the same members are one set; a set is one object, so it can be a member of another; a rule picks members out of a set already in hand; and there is one empty set. The second puts the textbook answer, a well-defined collection of distinct objects, on trial and finds that it leaves out the first of those rules. It also finds the limit of "any clear rule makes a set": Russell's rule is clear and makes none, and the repair, cutting rules out of a set already in hand, turns the paradox into the theorem that no set holds every set. The third lesson finds each idea in Python, one line apiece; how Python's `set` behaves beyond that is the Python library's page. The fourth lesson turns the operations into algebra: union, intersection and complement are *or*, *and* and *not* on membership, so the laws of sets are the laws of logic, checked here on every case. The fifth fixes how to read an expression without brackets, a precedence that comes from logic and that Python's operators follow exactly.

A set forgets everything except membership: {2, 5} and {5, 2} are one set. Almost all of mathematics needs more than that. A point in the plane has a first coordinate and a second, a function has an input and an output, a database row has columns in a fixed order. The **ordered pair** is the smallest object that remembers order, and the **Cartesian product** is the set of all of them. Everything from the coordinate plane to the definition of a function is built on it.

The second lesson asks how big a set is. For a finite set the answer is a count, and |A × B| = |A| · |B| is the first theorem. For an infinite set counting never finishes, and the definition that replaces it, matching members one to one, is what lets ℕ be the same size as its even numbers and ℝ be strictly bigger than both. That last fact is also the reason some functions have no program, which is where the chapter touches computing.

The seventh lesson answers the surprise that functions and graphs turn up in a book on sets: a relation is a set of pairs, a function a relation with one property, a graph a relation drawn, so one definition covers them all; the eighth shows that a partition, an equivalence relation and the kernel of a function are one object three ways, and the ninth sorts all 512 relations on three points into the combinations with names, equivalences and orders, and settles the words for positions in a poset. The tenth is the theorem that makes "no bigger than" on sizes antisymmetric, two injections made into a bijection by an algorithm; the eleventh is the set that counts. The last two lessons are practice: the exercises of a first section on sets, each checked on every choice of subsets of {1, 2, 3} before you look for the proof, with the proof's move named. The [axioms chapter](../13_Axioms_of_Set_Theory/README.md) continues from here, putting the constructions of this chapter on the axioms of Zermelo and Fraenkel.

The twelfth lesson answers the owner's "how the heck can combinatorics be relevant to sets" with Ramsey's theorem: the pigeonhole principle for pairs. Six points with their pairs coloured in two colours always hold a one-colour triangle, and the program checks all 32 768 colourings; colouring the pairs of ℕ always leaves an infinite one-colour set, and the program runs the proof as an algorithm; and the same question at the first uncountable cardinal has a different answer, which is where combinatorics becomes set theory. The two kata pages close the chapter.

## A note on the code

Python has both objects natively: a `tuple` is an ordered pair and a `set` is a set. So the programs in this chapter do not simulate the definitions, they check them: `(2, 5) == (5, 2)` is asked directly and the interpreter answers `False`.

## Flashcards

Every set card in one file: [`sets_all.txt`](anki/sets_all.txt), the decks of [what is a set?](what_is_a_set/README.md#flashcards), [the definition on trial](definition_on_trial/README.md#flashcards), [sets in Python](python_sets/README.md#flashcards), [the algebra of sets](algebra_of_sets/README.md#flashcards), [reading a set expression](reading_set_expressions/README.md#flashcards), [set katas](set_katas/README.md#flashcards) and [orderings](orderings/README.md#flashcards) combined. Import it once with File → Import; a deck column files each card under its lesson's subdeck of *Math::Sets*, and when importing it again later, choose to update existing notes so changed cards are refreshed rather than duplicated. The file is generated by [`tools/combine_anki.py`](../tools/combine_anki.py) from the lesson decks, which stay the source, and CI fails if it falls out of date.

## Po polsku, w skrócie

Ten rozdział to fundament: czym jest zbiór i jak z jednych zbiorów buduje się nowe. Zbiór to wyłącznie jego elementy, bez kolejności i bez powtórzeń, więc {2, 5} i {5, 2} to ten sam zbiór; para uporządkowana (2, 5) pamięta już kolejność, a iloczyn kartezjański A × B to zbiór wszystkich takich par. Moc zbioru |A| mierzy jego wielkość przez parowanie elementów, a nie liczenie, i dzięki temu ma sens także dla zbiorów nieskończonych. Programy w Pythonie nie symulują tych definicji, tylko je sprawdzają, bo `set` i `tuple` są w języku wbudowane.
