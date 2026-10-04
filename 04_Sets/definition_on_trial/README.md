# The textbook definition on trial

**Level:** 101 → 201 · for anyone who has met "a set is a well-defined collection of distinct objects"

**One line:** The textbook definition is a good description and a bad definition: "collection" is only a synonym, it leaves out the rule that makes {2, 5} = {5, 2} and the empty set unique, and "well-defined" is not enough, because Russell's rule is perfectly sharp and still describes no set.

The definition itself, in four rules, is on [What is a set?](../what_is_a_set/README.md). This page is the case against the sentences first courses open with, and it ends where that page begins.

## The definition on trial

Most first courses open with something like this:

> A **set** is a well-defined collection of distinct objects. The objects of a set are called its **elements**. By **well-defined**, we mean that there is a rule that enables us to determine whether a given object is an element of the set. If a set has no elements, it is called the **empty set**, or **null set**, and is denoted by the symbol ∅.

As a working description for a first course, it does its job. It says the right thing to focus on, membership, and it gives a usable test: a set is pinned down once you can say, of any object, whether it is in or out. Every set in the rest of this chapter meets it.

As a definition, it has four problems, and each one is the seed of something real.

1. **"Collection" is a synonym, not a definition.** It explains *set* by a word that means the same thing, so it names the idea without reducing it to anything simpler. That is not a fault that can be fixed: something has to be the first undefined word, and in mathematics it is *set* and *member of*. Modern treatments admit this openly and say what sets do instead of what they are, which is what the axioms of [Zermelo–Fraenkel set theory](../../13_Axioms_of_Set_Theory/README.md) are for.
2. **It never says when two sets are equal.** "Distinct" sounds like a demand on whoever writes the list, but {1, 1, 2} is a legal way to write the set {1, 2}. What the word is reaching for is the **axiom of extensionality**: two sets with the same members are the same set. It is the most important sentence about sets, and the definition leaves it out. Section 1 of the program checks it and section 2 shows what it buys: four different rules that happen to select nothing are one set, and that is the only reason one can say *the* empty set.
3. **"Well-defined" is ambiguous.** Does it mean the rule gives an answer, or that we can find the answer? Section 3 takes the set of odd numbers that equal the sum of their smaller divisors. For each number the test is a finite calculation, so the rule is sharp; whether the set is empty is the odd perfect number problem, open for two thousand years. Well-defined has to mean the first: every object is determinately in or out, whether or not anyone knows which.
4. **A sharp rule does not guarantee a set.** This is the serious one. Take the rule "x is not a member of itself". It is as clear as a rule can be. Suppose it defines a set R and ask whether R is a member of R. If it is, it fails the rule, so it is not. If it is not, it passes the rule, so it is. That is **Russell's paradox** (1901), and it broke the first attempt to found mathematics on sets, Frege's, which assumed exactly what this textbook definition says: any well-defined rule gives a set.

So is it a good definition? It is a good *first* definition, and it should be read the way Halmos titled his book, *Naive Set Theory*: fine for everything a first course does with sets, and not a foundation. The honest version of it is short, and it is the definition on [What is a set?](../what_is_a_set/README.md): *set* and *member* are undefined; two sets with the same members are equal; and a rule carves a set out of a set you already have, not out of everything.

## A second definition: the box

Another common opening reads:

> A **set** is a collection of objects known as **elements**. An element can be almost anything, such as numbers, functions, or lines. A set is a single object that can contain many elements. Think of it as a box with things inside. The box is the set, and the things are the elements. We use uppercase letters to label sets, and elements will usually be represented by lowercase letters. The symbol ∈ (fashioned after the Greek letter *epsilon*) is used to mean "element of", so if A is a set and a is an element of A, write ∈aA or, the more standard, a ∈ A. The notation a, b ∈ A means a ∈ A and b ∈ A. If c is not an element of A, write c ∉ A. If A contains no elements, it is the **empty set**. It is represented by the symbol ∅. Think of the empty set as a box with no things inside.

Is it better? **Better at notation, worse at the one idea the first definition was reaching for.**

What it does better:

- **It does not pretend.** "Collection" is offered as a picture, not a definition, which is honest: *set* and *element of* are undefined words, and this text treats them that way.
- **It puts ∈ at the centre.** Membership is the only primitive of set theory, and this definition is built around it: a ∈ A, c ∉ A, and the shorthand a, b ∈ A. The first definition never gives the symbol.
- **It says a set is a single object.** That is what lets a set be an element of another set, the step that makes sets of sets, functions as sets of pairs, and Russell's question possible. "Elements can be almost anything" includes other sets.
- **It is right that ∅ is something.** An empty box is still a box: ∅ has no members, but {∅}, the box holding an empty box, has one. Section 7 checks it.
- In passing it shows prefix notation, ∈aA, beside the usual infix a ∈ A, the same choice as `union(a, b)` against `a | b`.

What it loses:

- **Equality is gone entirely.** The first definition at least said "distinct"; this one never says when two sets are the same, so nothing in it rules out {1, 1} and {1} being different, or explains why there is only *one* empty set. [Extensionality](#the-definition-on-trial) is still missing.
- **"Well-defined" is gone too**, so it has no answer to Russell, not even the insufficient one.

And the box picture misleads in three places, each checked in section 7:

1. **∈ is not "inside".** A marble in a small box inside a big box is inside the big box. But 1 ∈ {1} and {1} ∈ {{1}}, while 1 ∉ {{1}}: a member of a member is not a member. ∈ looks exactly one level down; ⊆ is the relation that is transitive.
2. **One element, many sets.** A marble sits in one box at a time; 1 is in {1, 2} and in {1, 3} at once, and in infinitely many other sets.
3. **No copies.** A box can hold two identical marbles; {1, 1} is {1}. The box picture has no way to say so, which is the equality rule it left out.

Use the box for ∅ against {∅}, and drop it for membership. Taken together, the two textbook openings make one adequate definition: this one's notation, the first one's "distinct", and the equality rule neither of them states. Written out, that definition is [What is a set?](../what_is_a_set/README.md).

## One more word: "null set"

The definition offers "null set" as a second name for ∅. In most of algebra and logic books it is. In measure theory and probability, a **null set** means a set of *measure zero*, which can be infinite, even uncountable: the [Cantor set](../../02_Measure_Zero/cantor_set/README.md) is a null set in that sense and has as many points as the whole line. Read the word by the book it is in, and prefer "empty set" for ∅.

## What the program prints

<!-- output:definition_on_trial -->
*Verified output of [`definition_on_trial.py`](examples/definition_on_trial.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. A SET IS ITS MEMBERSHIP AND NOTHING ELSE
   {2, 5} == {5, 2}             is True     order is not recorded
   {1, 1, 2} == {1, 2}          is True     repeats are not recorded
   len({1, 1, 2})                = 2
   {n*n for n in -3..3}          = [0, 1, 4, 9]   7 rules applied, 4 members
   'Distinct' is not a demand on whoever writes the list. It is
   the rule for equality: same members, same set (extensionality).

2. THEREFORE THERE IS ONE EMPTY SET, NOT MANY
   {n in 0..99 with n*n < 0}         = set()
   {n in 0..99, even and odd}        = set()
   {n in 0..99 with n > n}           = set()
   {words of 'set' longer than 3}    = set()
   all four equal:  True
   Four rules, one set. 'THE empty set' is justified only by the
   equality rule of section 1, which the textbook definition omits.

3. WELL-DEFINED IS NOT THE SAME AS KNOWN
   P = { n : n is odd and n equals the sum of its smaller divisors }
   The rule is sharp: for any n, adding up divisors settles it.
   even n below 10,000 that pass the test:  [6, 28, 496, 8128]
   odd n below 100,000 that pass the test:  []
   Is P empty? Nobody knows; it is the odd perfect number problem,
   open since antiquity. Every n has an answer; the set as a whole
   does not have a known one. Well-defined means the first, not the second.

4. A SHARP RULE THAT DECIDES NOTHING: RUSSELL
   Model a set as its rule: a function that answers 'is x a member?'.
   Rules can be asked about rules, so a set may contain sets.
   everything(everything) = True     russell(everything) = False
   nothing(nothing)       = False    russell(nothing)    = True
   russell(russell)       = no answer: RecursionError, the rule asks itself forever
   And no answer could be right:
     if russell(russell) were True , the rule says it is False
     if russell(russell) were False, the rule says it is True
   The rule 'x is not a member of itself' is perfectly well-defined
   on every x, and still there is no set it describes.

5. THE REPAIR: CUT A RULE OUT OF A SET YOU ALREADY HAVE
   In a universe U, membership is a table: x in y is True or False.
   R = { x in U : x not in x }. Is R one of the members of U?
   every membership table on 3 objects: 512 universes
   universes where R is none of the 3 objects:  512 of 512
   Why always: if R were object y, ask whether y is in y. The table
   and the rule for R give opposite answers at that one cell.
   So no universe contains every set. Russell's paradox, restricted
   to a set already in hand, stops being a contradiction and becomes
   a theorem; it is Cantor's diagonal from the cardinality lesson.

6. PYTHON BUILDS SETS FROM THE BOTTOM UP, SO IT NEVER MEETS RUSSELL
   s = set(); s.add(s)   ->  TypeError: unhashable type: 'set'
   frozensets from nothing:  0, 1, 2 members;  c contains b: True
   A frozenset can hold only sets that existed before it, so none
   contains itself and 'x not in x' is true of every one of them.
   That is the axiomatic answer too: sets are built in stages.

7. THE BOX PICTURE: WHERE IT HELPS AND WHERE IT MISLEADS
   an empty box is not nothing:  len(∅) = 0,  len({∅}) = 1,  ∅ == {∅} is False
   ∈ looks one level down only:  1 ∈ {1} is True,  {1} ∈ {{1}} is True,  1 ∈ {{1}} is False
     a thing inside a box inside a box is 'in' the big box; a member of a
     member is not a member. ∈ is not transitive; ⊆ is.
   one object, two sets at once:  A = {1, 2}, B = {1, 3},  1 ∈ A and 1 ∈ B is True
     a real object sits in one box; an element can be in any number of sets.
   two copies are one element:  {1, 1} == {1} is True
     a box can hold two identical marbles; a set cannot tell them apart.
   So the box is a good picture of ∅ versus {∅}, and a bad one of
   membership: take it for the first and drop it for the other three.

8. CAN WE DENY 'C IS EITHER ORDINARY OR NOT'? TRY IT IN OTHER LOGICS
   P stands for 'C ∈ C'. The definition of C says P ↔ ¬P must be TRUE.
   Truth values run from 0 (false) to 1 (true); only 1 counts as true.
   logic            P or not P always true?   values of P that satisfy P ↔ ¬P
   classical        yes                       none: still a paradox
   Kleene K3        no                        none: still a paradox
   Godel G3         no                        none: still a paradox
   Godel G5         no                        none: still a paradox
   Lukasiewicz L3   no                        1/2
   Lukasiewicz L5   no                        1/2
   Excluded middle fails in K3 and in the Godel logics, and C still has no
   truth value there: the paradox never needed statement 4. Only Lukasiewicz
   logic has a 'half true' that solves it. Then Curry's version bites:
   C_k = {x : x ∈ x → (x ∈ x → ... → false)}, with k arrows.
   Lukasiewicz L3   no value for C_k ∈ C_k when k = 2, 3, 4, 5, 6
   Lukasiewicz L4   no value for C_k ∈ C_k when k = 1, 3, 4, 5, 6
   Lukasiewicz L5   no value for C_k ∈ C_k when k = 2, 4, 5, 6
   Lukasiewicz L6   no value for C_k ∈ C_k when k = 1, 2, 3, 5, 6
   The fixed point of C_k is k/(k+1), and a logic with finitely many values
   always misses one. Every finite-valued repair meets a paradox it cannot
   value; set theory instead keeps the logic and denies that C exists.
```
<!-- /output -->

## Russell, run as a program

Section 4 makes the paradox concrete by taking the definition literally: a set is its rule, so model a set as a Python function that answers "is x a member?". Functions can be given functions, so these sets can contain sets, and the rule `russell(x) = not x(x)` is one line.

Asked about the set of everything, it answers False, because everything contains itself. Asked about the empty set, it answers True. Asked about itself, it has to compute `not russell(russell)`, which needs `russell(russell)`, which needs it again, and Python gives up with a `RecursionError`. The program then shows that the loop is not a bug in the code: whichever answer it returned, the rule would demand the opposite. A well-defined rule, a question with no answer.

## The repair, and the paradox as a theorem

Zermelo's fix (1908) is the **axiom of separation**: a rule does not create a set out of nothing, it selects the members of a set A that you already have. The set is {x ∈ A : P(x)}, never {x : P(x)}.

Run Russell's rule under that restriction. In any universe U, form R = {x ∈ U : x ∉ x}. Now R is certainly a set, and the argument that used to be a contradiction proves something instead: R is not a member of U. If it were some object y of U, then asking whether y ∈ y gives opposite answers from the membership table and from R's rule. Section 5 checks this on every possible universe of three objects, all 2⁹ = 512 ways of filling in the table of who is a member of whom, including the strange ones where objects contain themselves. In all 512, R is missing.

So **there is no set of all sets**. That is the theorem Russell's paradox becomes once rules are forced to cut from an existing set, and it is the same diagonal that shows, in [cardinality](../cardinality/README.md), that no list of 0/1 sequences contains all of them: build the object that disagrees with entry y at position y.

Section 6 shows the other half of the modern answer, and Python agrees with it. A mutable `set` cannot be put into itself at all, and a `frozenset` can only hold sets that already existed when it was made. Sets built that way, from ∅ upward in stages, never contain themselves, so "x ∉ x" is true of all of them and Russell's question never gets a foothold. The axioms of ZF describe exactly this: a world of sets built in stages, in which "the set of all sets" is not a set, only a way of speaking.

## "Every set is one type or the other": drop that instead?

A natural objection, asked on Mathematics Stack Exchange and elsewhere: call a set *ordinary* if it is not a member of itself and *extraordinary* if it is, and let C be the set of all ordinary sets. The usual argument says "C is either ordinary or extraordinary", then shows that both cases fail. So why not reject that step? It looks obvious, but C itself seems to be a counterexample to it, and a hypothesis should be dropped once a counterexample turns up.

It is a good question. The answer has two parts.

**First, the contradiction does not use that step.** Write P for "C ∈ C". The definition of C says P ↔ ¬P. Now argue without splitting into cases. Suppose P; then ¬P, which contradicts P, so P is false: ¬P. But ¬P gives P, by the definition again. Both P and ¬P follow, and no line said "either P or not P". This argument is valid even in intuitionistic logic, which rejects the law of excluded middle outright. So throwing statement 4 away leaves the contradiction exactly where it was. Section 8 checks this in logics where "P or not P" genuinely fails, Kleene's three-valued logic and Gödel's logics: in none of them can "C ∈ C" be given any truth value that makes the definition of C true.

**Second, a contradiction refutes the premises together, and you choose which one to give up.** The argument uses the logic and one more premise: *C exists*, a set whose members are exactly the ordinary sets. Mathematics gives up that premise. With [Zermelo's separation](#the-repair-and-the-paradox-as-a-theorem) there is no set of *all* ordinary sets, only the ordinary members of some set you already have, and the same argument then proves that this set is never one of its own members. (In ZF every set is ordinary, by the axiom of foundation, so C would be the set of everything, which section 5 already showed cannot exist.) C is not a counterexample to "every set is one type or the other", because C is not a set.

Keeping C and changing the logic can work, but only up to a point, and section 8 shows where the limit is. In Łukasiewicz's three-valued logic, "C ∈ C" can be exactly half true, since "½ ↔ not ½" is fully true there. That is the objection made precise. But Curry's paradox, C_k = {x : x ∈ x → (x ∈ x → … → false)} with k arrows, has a fixed point only at the truth value k/(k + 1). Every Łukasiewicz logic with finitely many values misses one of those, so each has a set it cannot value. Only a continuum of truth values escapes this, and naive set theory in that logic has troubles of its own. Other routes exist too: paraconsistent logics accept the contradiction and stop it from proving everything, and logics without the rule of contraction block the step "P leads to ¬P, so ¬P". All of them are real research programmes. None is how ordinary mathematics is done, which is why the standard answer keeps classical logic and denies that C exists.

## Flashcards

The page as a deck of Anki cards: [`definition_on_trial.txt`](anki/definition_on_trial.txt). Import with File → Import. Tags: `definition`, `axiom`, `theorem`, `trap`, `example`, `history`, `connection`, `principle`, `logic`. The Python side is a second deck, on [sets in Python](../python_sets/README.md#flashcards).

## Po polsku, w skrócie

Podręcznikowa „definicja” zbioru, czyli „dobrze określona kolekcja różnych obiektów”, jest dobrym opisem na start, ale nie jest definicją. „Kolekcja” to tylko inne słowo na zbiór; w matematyce *zbiór* i *należy do* są pojęciami pierwotnymi, których się nie definiuje, a jedynie opisuje aksjomatami. Sama definicja, w czterech regułach, jest na stronie *What is a set?*; ta strona to proces, który do niej prowadzi.

Brakuje w niej najważniejszego zdania: dwa zbiory o tych samych elementach są równe (aksjomat ekstensjonalności). To dzięki niemu {2, 5} = {5, 2}, zapis {1, 1, 2} oznacza po prostu {1, 2}, a zbiór pusty jest tylko jeden, choć można go opisać na wiele sposobów.

„Dobrze określony” znaczy, że o każdym obiekcie wiadomo, czy należy, czy nie, co nie oznacza, że my to wiemy: zbiór nieparzystych liczb doskonałych jest dobrze określony, a nikt nie wie, czy jest pusty. Co gorsza, sama ostra reguła nie wystarcza: reguła „x nie należy do siebie” jest jasna, a zbioru nie wyznacza, bo pytanie, czy taki zbiór należy do siebie, prowadzi do sprzeczności (paradoks Russella). Program pokazuje to dosłownie: funkcja `russell(russell)` wywołuje samą siebie bez końca.

Druga popularna definicja („zbiór to pudełko z rzeczami w środku”) lepiej wprowadza zapis a ∈ A i uczciwie przyznaje, że „kolekcja” to tylko obraz, ale gubi całkiem zasadę równości zbiorów. Obraz pudełka myli w trzech miejscach: element elementu nie jest elementem (1 ∈ {1} ∈ {{1}}, ale 1 ∉ {{1}}), jeden element może należeć do wielu zbiorów naraz, a dwie kopie tego samego to jeden element. Dobrze natomiast pokazuje, że {∅} to nie ∅: puste pudełko w pudełku to już jeden element.

Częsty zarzut: może winne jest założenie „każdy zbiór jest zwykły albo niezwykły”? Nie, bo sprzeczność da się wyprowadzić bez niego: z C ∈ C wynika C ∉ C, więc C ∉ C, a stąd C ∈ C. To rozumowanie jest poprawne nawet w logice intuicjonistycznej, która odrzuca prawo wyłączonego środka. Program sprawdza to w logikach Kleenego i Gödla: tam również żadna wartość logiczna nie ratuje C. Logika Łukasiewicza daje „pół prawdy”, ale paradoks Curry’ego znowu ją łamie. Dlatego matematyka zostawia logikę klasyczną i odrzuca istnienie C.

Naprawa Zermela polega na tym, że regułą wycina się elementy z już istniejącego zbioru. Wtedy paradoks zamienia się w twierdzenie: nie istnieje zbiór wszystkich zbiorów. Program sprawdza to na wszystkich 512 możliwych „wszechświatach” złożonych z trzech obiektów. Uwaga językowa: „zbiór zerowy” (ang. *null set*) w teorii miary oznacza zbiór miary zero, niekoniecznie pusty.

## Auf Deutsch: Stichwörter

Die Schulbuchdefinition „eine Menge ist eine Sammlung von Objekten“ vor Gericht: was sie offen lässt und wo Russell sie bricht.

**Stichwörter:** Definition, Sammlung (collection), Russellsche Antinomie, uneingeschränkte Komprehension, Element, wohldefiniert.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 04_Sets/definition_on_trial/examples/definition_on_trial.py
```

## See also

- [What is a set?](../what_is_a_set/README.md) — the definition this trial ends in, stated first and checked rule by rule
- [Cardinality of sets](../cardinality/README.md) — the diagonal argument that section 5 reuses
- [The Cartesian product](../cartesian_product/README.md) — the next construction: an object that, unlike a set, remembers order
- [A definition is a test](../../06_Algebraic_Structures/a_definition_is_a_test/README.md) — the axiomatic style: say what objects must do, not what they are
- [If A then B: converse, contrapositive and inverse](../../11_Logic/converse_and_contrapositive/README.md) — the logic that the Russell argument runs on
- [Russell's paradox ↗](https://plato.stanford.edu/entries/russell-paradox/) — Stanford Encyclopedia of Philosophy
- [The axioms of set theory](../../13_Axioms_of_Set_Theory/README.md) — the chapter on the axioms, one page each, with a program that checks each one on a small universe
- [Zermelo–Fraenkel set theory ↗](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory) — Wikipedia: the axioms, extensionality and separation among them
- [Null set ↗](https://en.wikipedia.org/wiki/Null_set) — Wikipedia: the measure-theory meaning
