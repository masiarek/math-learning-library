# Set theory: a reading guide

**Level:** reference · for anyone choosing a book on sets, from a first proofs course to forcing and large cardinals, and for anyone who wants the short papers the subject grew from

**One line:** Set theory is two subjects with one name, the language of sets that every proof-based course speaks and the study of the axioms themselves; Velleman and Halmos teach the first in a hundred pages, Hrbacek and Jech are the course for the second and Jech and Kunen its reference, and the founding papers are shorter than the books about them, so four of them run here as a program.

Every other page in this library is a lesson: one idea, backed by a program. This page is a reading guide, and what it says about books is opinion, not a test result. The years and journals of the papers at the end are given from memory; where a link is given, follow the link rather than trusting the citation. The one worked example, four founding results of the subject checked on small sets, is backed by a program like everything else.

## Two subjects with one name

Ask a mathematician what set theory is and you get one of two answers, depending on what they do all day.

**The first is a language.** [Sets](../../04_Sets/what_is_a_set/README.md), [subsets](../../04_Sets/algebra_of_sets/README.md#is-a-partial-order), [unions](../../04_Sets/algebra_of_sets/README.md), [the empty set](../../04_Sets/what_is_a_set/README.md), [ordered pairs](../../04_Sets/cartesian_product/README.md), [relations, functions](../../04_Sets/relations_and_functions/README.md), [one-to-one and onto](../../04_Sets/relations_and_functions/README.md), [equivalence relations](../../04_Sets/equivalence_and_partitions/README.md), [countable](../../02_Measure_Zero/countable_sets/README.md) and [uncountable](../../04_Sets/cardinality/README.md), [Zorn's lemma](../../13_Axioms_of_Set_Theory/choice/README.md). Every proof-based course uses these words from the first lecture, and a book on analysis or algebra spends its first chapter on them. This set theory is finished and small: a good book covers it in fifty to a hundred pages, and nobody researches it.

**The second is a subject.** What are the rules for building sets, written down exactly, and what follows from the rules? This is the [axiomatic set theory of Zermelo and Fraenkel](../../13_Axioms_of_Set_Theory/README.md) (ZF, and ZFC with the [axiom of choice](../../13_Axioms_of_Set_Theory/choice/README.md)), and it is where the famous results live: that the axiom of choice and the continuum hypothesis can neither be proved nor refuted from the other axioms ([Gödel 1938, Cohen 1963](#the-founding-papers)), the hierarchy of larger and larger infinities ([ordinals](../../13_Axioms_of_Set_Theory/ordinals/README.md), [power sets](../../13_Axioms_of_Set_Theory/power_set/README.md)), and the study of which sets of real numbers are tame. This set theory is alive, and its books are long.

Most people who ask "which book on sets?" want the first and are handed one on the second, which is where the reputation for difficulty comes from. The table below separates them.

| You want | Read | Pages on sets |
|---|---|---|
| The language, for a proofs course or this library | Velleman, Hammack | 100 |
| The language, told by a master, with the axioms named but not fussed over | Halmos | 100 |
| The axioms as a one-semester course | Hrbacek and Jech; Enderton; Goldrei | 300 |
| Independence proofs: why the continuum hypothesis cannot be settled | Kunen | 400 |
| The whole subject on one shelf | Jech | 750 |

## Set theory among the branches of mathematics

The owner asked which branches of mathematics are related to set theory and how. Two answers, because the subject is two things, as the section above says.

**As a branch**, set theory is one of the four parts of mathematical logic, beside model theory, proof theory and computability theory, and its own sub-areas are the eight the [beyond-ZFC section](#beyond-zfc-the-map-in-wikipedias-article) lists. **As a language**, it runs under everything else, and each branch takes something specific from it and, often, gave something back.

| Branch | What it takes from set theory | What it gave, or what set theory does inside it |
|---|---|---|
| **Logic and foundations** | The axioms, the universe V, models of theories | Gödel's incompleteness, Löwenheim–Skolem, independence proofs by forcing; the question of what a proof assistant's foundation is ([tools](#tools-languages-proof-assistants-model-finders)) |
| **Analysis** | ℝ built as Dedekind cuts or Cauchy classes, both quotient constructions; σ-algebras and measure; countable and uncountable | Set theory was born here: Cantor invented ordinals in 1872 for a question about Fourier series, and the pathologies of analysis (Vitali's non-measurable set, Banach–Tarski) are the [axiom of choice](../../13_Axioms_of_Set_Theory/choice/README.md) at work; descriptive set theory, which sets of reals are tame, is the shared border |
| **Topology** | Open sets closed under arbitrary unions and finite intersections, which is the [unions axiom](../../13_Axioms_of_Set_Theory/unions/README.md) in use; Zorn's lemma for Tychonoff's theorem | Topology was born in Hausdorff's 1914 set theory textbook; set-theoretic topology asks which spaces exist under which axioms |
| **Algebra** | Quotients by [equivalence relations](../../04_Sets/equivalence_and_partitions/README.md) (ℤ/mℤ, G/H), cardinality of bases, Zorn's lemma for a basis of every vector space and a maximal ideal in every ring | Boolean algebras, the structure that sets and logic share ([the algebra of sets](../../04_Sets/algebra_of_sets/README.md)); lattices and orders ([orderings](../../04_Sets/orderings/README.md)) |
| **Number theory** | ℕ built from the [axiom of infinity](../../13_Axioms_of_Set_Theory/infinity/README.md), then forgotten; [induction](../../11_Logic/induction/README.md); factorisations as [multisets](../../04_Sets/multisets/README.md) | Goodstein's theorem, a statement about integers whose only known proof uses [ordinals](../../13_Axioms_of_Set_Theory/ordinals/README.md); the Paris–Harrington theorem likewise |
| **Graph theory** | A graph is a set of vertices with a set of 2-element subsets, or [a relation drawn](../../04_Sets/relations_and_functions/README.md); a colouring is a partition of the edge set | [Ramsey's theorem](../../04_Sets/ramsey/README.md) and König's lemma on trees are theorems about graphs that are also theorems of set theory; Erdős made infinite graphs a set-theoretic subject |
| **Combinatorics** | Finite sets, [partitions](../../04_Sets/equivalence_and_partitions/README.md), Bell and Stirling numbers, [inclusion–exclusion](../../04_Sets/set_katas/README.md) | Infinite combinatorics (Ramsey theory, trees, almost-disjoint families) is a research area of set theory in its own right |
| **Probability** | Kolmogorov's 1933 axioms: a sample space, events as subsets forming a σ-algebra, a measure on them; [probability zero](../../02_Measure_Zero/probability_zero/README.md) | Measurable cardinals began with Ulam's 1930 question about measures |
| **Geometry** | Points as ordered pairs ([the Cartesian product](../../04_Sets/cartesian_product/README.md)); congruence and similarity as [orbits](../../04_Sets/equivalence_and_partitions/README.md) of groups of motions | Banach–Tarski, a ball reassembled as two from five pieces, from the axiom of choice |
| **Category theory** | Sets as the first example of a category | A rival foundation: Lawvere's ETCS describes sets by their functions alone, and type theory, used by Lean, by their types |
| **Computer science** | Relations as database tables, comprehension as `WHERE`, [functions as dictionaries](../../04_Sets/relations_and_functions/README.md), induction on data types, well-founded orders for termination | Computability theory, Cantor's diagonal argument as the halting problem, and the model finders and proof assistants of the [tools table](#tools-languages-proof-assistants-model-finders) |
| **Philosophy** | What a number is, whether the continuum hypothesis has an answer, whether a proof needs choice | Maddy's essay on the philosophy shelf below is the current state of that conversation |

Functions are not in the table because they are not a branch: a function is a set of pairs with one property, as [relations and functions](../../04_Sets/relations_and_functions/README.md) shows, and so every branch that uses functions is using sets twice, once for the domain and once for the pairs. The owner's question "how is it possible that set theory is in functions, combinatorics, graphs" has that one answer: each of these objects is defined as a set with a property, so every theorem about it is a theorem about a set.

The pattern repeats: a branch meets a question it cannot settle with its own tools, the question turns out to be about sets, and set theory keeps it. Fourier series gave ordinals, measure gave large cardinals, topology gave set-theoretic topology, and the halting problem is Cantor's diagonal in a new suit.

### Two pasted summaries, checked

The owner pasted two AI-written summaries of the branches and asked whether they are right and whether their structure is good. Claim by claim, with how sure this page is of each.

The first summary listed "branches that focus on sets" and, a second time, "core branches of set theory" and "branches deeply reliant on sets".

| Claim | How sure | Note |
|---|---|---|
| Axiomatic set theory: ZFC, the infinite, ordinals and cardinals, limits of what can be proved | sure | the [axioms chapter](../../13_Axioms_of_Set_Theory/README.md) |
| Order theory: posets, lattices, well-ordered sets | sure | [orderings](../../04_Sets/orderings/README.md) |
| Topology: open and closed sets instead of distance | sure | |
| Measure theory: σ-algebras closed under complement and countable union | sure | |
| Abstract algebra: sets with operations | sure | |
| Combinatorics "deals with finite sets"; extremal set theory | half | the finite part is right; infinite combinatorics is a research area of set theory, see [Ramsey's theorem](../../04_Sets/ramsey/README.md) |
| Descriptive set theory: definable sets of reals, Polish spaces, Borel and analytic sets | sure | |
| Category theory: the category Set as a universal translator | sure | and a rival foundation, which the summary does not say |
| Combinatorial set theory: infinite graphs, Ramsey theory, cardinal arithmetic | sure | Halbeisen's book, above |
| Fuzzy set theory as a "core branch of set theory", "heavily used in AI" | no | Zadeh's fuzzy sets (1965) are an applied subject, mostly control engineering; no set theorist counts them as a branch, and modern AI does not use them. The second summary says this correctly |
| What is missing | | analysis, number theory, probability, geometry, computer science and logic itself, all in the table above; and the two lists are one answer given twice with different wording |

The second summary split the subject into a "mainstream foundation" to learn and "esoteric branches" that are optional.

| Claim | How sure | Note |
|---|---|---|
| Mainstream: relations, functions, partitions; cardinality and Cantor's theorem; ordinal and cardinal arithmetic; choice and Zorn's lemma | sure, and the order is right | it is this library's chapter 4 followed by chapter 13 |
| "You must understand transfinite induction" | half | true for a logician; most working mathematicians use Zorn's lemma and never touch an ordinal |
| Missing from the mainstream list | | the elementary layer: [the algebra of sets](../../04_Sets/algebra_of_sets/README.md), the [Cartesian product](../../04_Sets/cartesian_product/README.md), [injective and surjective](../../04_Sets/relations_and_functions/README.md#the-three-words), and the axioms themselves |
| Forcing, Cohen, the continuum hypothesis independent of ZFC | sure | |
| Large cardinals measure consistency strength; inaccessible, Mahlo, Woodin | sure | |
| Determinacy: every set of reals measurable, contradicts choice | sure on the facts | but not "a parallel universe": under large cardinals, determinacy holds inside L(ℝ), the inner model where descriptive set theorists work, within an ordinary ZFC universe |
| Anti-foundation, x = {x}, used in computer science | sure | Aczel 1988; see [foundation](../../13_Axioms_of_Set_Theory/foundation/README.md) |
| Quine's New Foundations: a universal set, restricted comprehension | sure | from memory: its consistency, open since 1937, was proved by Holmes and checked by machine in 2024 |
| Fuzzy sets "kept separate from pure set theory" | sure | the honest sentence the first summary lacked |
| The structure itself: forcing, large cardinals and determinacy as "esoteric and optional" | misleading | for a set theorist those three are the subject; they are optional only for a user of sets. New Foundations, anti-foundation and fuzzy sets are alternatives to the axioms, a different kind of thing, and belong in a separate group. The [suggested paths](#suggested-paths) below are this library's version of the same structure |

## What a founding result looks like

The subject began with a few short papers, and the idea of each one fits in a few lines of code. The program takes four: Cantor's first paper (1874), which lists the algebraic numbers by a "height" and so shows they are countable; Dedekind's definition of an infinite set (1888) as one that can be matched with a proper part of itself; Cantor's diagonal argument (1891), that no set can be matched with the set of its subsets; and von Neumann's definition of the natural numbers (1923), where each number is the set of the smaller ones. Where a finite check is a proof, the program checks every case; where the claim is about an infinite set, it prints the first lines of the infinite pattern and leaves the proof to the paper.

<!-- output:classic_set_theory -->
*Verified output of [`classic_set_theory.py`](examples/classic_set_theory.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. CANTOR 1874: THE ALGEBRAIC NUMBERS CAN BE LISTED BY HEIGHT
   An algebraic number is a real root of a0·x^n + ... + an = 0 with
   integer coefficients, a0 > 0 and no common factor. Cantor gives the
   equation a height, n - 1 + |a0| + ... + |an|, and only finitely
   many equations share a height:
     height         1    2    3    4    5    6    7
     equations      1    3    9   23   61  151  377
   An equation of degree n has at most n real roots, so each height
   adds finitely many numbers. Listed height by height, with the
   reducible equations dropped as Cantor dropped them, the real
   algebraic numbers begin:
     height 1:  0
     height 2:  -1, 1
     height 3:  -2, -1/2, 1/2, 2
     height 4:  -3, -1.61803, -1.41421, -0.70711, -0.61803, -1/3, 1/3, 0.61803, 0.70711, 1.41421, 1.61803, 3
   Every algebraic number has a height, so every one gets a place in
   the list: the algebraic numbers are countable. The second half of
   the paper shows that the real numbers cannot be listed at all, so
   some real numbers are not algebraic: transcendental numbers exist,
   proved without exhibiting a single one.

2. DEDEKIND 1888: INFINITE MEANS MATCHING A PROPER PART OF ITSELF
   Dedekind's definition: a set is infinite when some one-to-one map
   sends it into a proper subset of itself, and finite otherwise.
   Finite sets fail it. A set of n members has n^n maps into itself;
   the one-to-one ones are the n! permutations, and each one is onto:
     n = 1:     1 maps,    1 one-to-one, all onto: True
     n = 2:     4 maps,    2 one-to-one, all onto: True
     n = 3:    27 maps,    6 one-to-one, all onto: True
     n = 4:   256 maps,   24 one-to-one, all onto: True
     n = 5:  3125 maps,  120 one-to-one, all onto: True
   N passes it. n -> 2n is one-to-one and lands in the even numbers:
     n:    0  1  2  3  4  5  6  7  8  9 ...
     2n:   0  2  4  6  8 10 12 14 16 18 ...
   1, 3, 5, 7, ... are never hit, so the image is a proper part of N.
   That is why a set can have as many members as one of its proper
   subsets, and why only an infinite set can.

3. CANTOR 1891: NO SET MATCHES ITS OWN POWER SET
   A = {a, b, c}; P(A), the set of its subsets, has 2^3 = 8 members.
   A map f: A -> P(A) picks a subset for each member. The diagonal set
   D = {x in A : x not in f(x)} differs from f(x) at x, for every x:
     f(a) = {a, b}     a in f(a): True   so a not in D
     f(b) = {}         b in f(b): False  so b in D
     f(c) = {a, b, c}  c in f(c): True   so c not in D
     D = {b}, and D is not f(a), f(b) or f(c): True
   All 8^3 = 512 maps A -> P(A) checked: D is never in the image,
   so no map is onto: True. Here counting would do (3 < 8), but the
   sentence 'D differs from f(x) at x' never counted anything, so it
   works for infinite sets too: |P(A)| > |A| always, and no set is
   the largest.

4. VON NEUMANN 1923: EACH NUMBER IS THE SET OF THE SMALLER ONES
   0 = {}, and n + 1 = n ∪ {n}:
     0 = {} = {}
     1 = {0} = {{}}
     2 = {0, 1} = {{}, {{}}}
     3 = {0, 1, 2}
     4 = {0, 1, 2, 3}
     5 = {0, 1, 2, 3, 4}
   n has exactly n members: True
   m < n  iff  m ∈ n: True      m < n  iff  m is a proper subset of n: True
   Order, membership and inclusion agree, and nothing but sets was
   used, so the natural numbers need no axiom of their own. Carrying
   on past them, ω = {0, 1, 2, ...} and ω + 1 = ω ∪ {ω}, gives the
   ordinals, and n ∪ {n} is still the successor.
```
<!-- /output -->

Section 1 is the first page of set theory, and it is worth seeing why Cantor needed the height. An algebraic number is a root of a polynomial equation with integer coefficients, and there are infinitely many equations of every degree, so "list them by degree" never finishes degree 1. The height bundles the degree and the sizes of the coefficients into one number, and only finitely many equations share a height, so listing height by height reaches every equation at a finite position. The same trick, listing by a size that only finitely many objects share, is how every proof that a set is countable works; [countable sets](../../02_Measure_Zero/countable_sets/README.md) does it for the rationals.

Section 2 answers a question the owner of this library met in Cori and Lascar's set theory chapter: how can a set have as many members as one of its proper subsets? Dedekind's reply is that this is not a paradox to be explained away but the *definition* of infinite, and the program shows the two halves: no finite set does it, because a one-to-one map of a finite set into itself is always onto, and ℕ does it with n ↦ 2n. Section 3 is the argument that there is no largest set, and the point to notice is the one the output makes: for a three-member set, counting would settle it, but the diagonal sentence never counts, so it works for infinite sets too, where counting is impossible. [Cardinality of sets](../../04_Sets/cardinality/README.md) runs the same argument on sequences of bits. Section 4 is the construction every axiomatic book makes in its first chapter, and the [axioms chapter](../../13_Axioms_of_Set_Theory/README.md) builds on it.

## What you need first

**For the language of sets: nothing beyond school algebra and the will to read a proof.** This library's [sets chapter](../../04_Sets/README.md) and [logic chapter](../../11_Logic/README.md) are the warm-up, and a proofs book (Velleman, Hammack) is the course.

**For an axiomatic course:** one proofs course, with induction and the words [*injective*](../../GLOSSARY.md#injective-one-to-one), [*surjective*](../../GLOSSARY.md#surjective-onto), [*bijective*](../../GLOSSARY.md#bijection), explained in plain words on [the relations page](../../04_Sets/relations_and_functions/README.md#the-three-words); nothing else. Halmos assumes exactly that, and Hrbacek and Jech assume slightly less.

**For the graduate books:** a first course in mathematical logic, since forcing and the constructible universe are statements about models of a first-order theory. Enderton's *A Mathematical Introduction to Logic*, the first part of Cori and Lascar, or Kunen's own *Foundations of Mathematics* all serve; the last is written as the prerequisite for Kunen's *Set Theory*. Descriptive set theory needs real analysis and point-set topology on top.

### A quick self-check

1. Show that n ↦ n + 1 is one-to-one on ℕ and not onto.
2. Prove that no set can be matched one-to-one with the set of its subsets.
3. Write the number 3 as a set, using only ∅ and braces.

If the third is new, start with the language: Velleman, then Halmos. If the second is easy, start with Hrbacek and Jech. If you can also state the axiom of replacement and say what it is for, start with Kunen.

## Which book

### The language of sets: a first course

**Before any book.** The [Math is Fun introduction to sets ↗](https://www.mathsisfun.com/sets/sets-introduction.html) is a sound first hour: sets as collections, braces and ∈, the standard number sets, equality, subsets and proper subsets, the empty set, cardinality including a first look at infinite sets, the universal set, and short "your turn" questions, with follow-on pages on set-builder notation, power sets and Venn diagrams. (Described from the owner's screenshots and from memory; the site could not be fetched from this session.) Its universal set is right, and in the right words: "a set that contains everything. Well, not exactly everything. Everything that is relevant to our question", with the integers for number theory, the reals for calculus and the complex numbers for complex analysis as the examples, which is what [the algebra of sets](../../04_Sets/algebra_of_sets/README.md#the-complement-needs-a-universe) says too. One caution for a reader going on to the books: it treats "a collection of things" as a definition, which [what is a set?](../../04_Sets/what_is_a_set/README.md) shows leaves out the rule everything else relies on. Its quizzes are on the [set katas](../../04_Sets/set_katas/README.md#quiz-katas) page, answered and computed.

A school textbook is the other good first hour, and the owner sent chapter 1 of an Indian one at Class 11 level (the title is not on the pages; its examples are blood groups, Kho-Kho and mock tests). It is friendly and correct: roster and set-builder form, finite and infinite, ∈ and ⊆, power sets with 2ⁿ, the universal set as "a specific all-encompassing set", Venn diagrams, the four operations, De Morgan verified on numbers, and then the one topic the university books skip, counting by Venn regions: n(A ∪ B) = n(A) + n(B) − n(A ∩ B), its three-set version, and word problems about students and surveys. Its summary page is a flashcard deck already, and it now is one: the [set katas](../../04_Sets/set_katas/README.md#flashcards) deck, with its exercises worked and checked on [that page](../../04_Sets/set_katas/README.md#from-a-school-textbook-versus-nested-sets-and-counting-by-venn-regions). Read it, or Math is Fun, then this library's sets chapter, then Velleman. Read it, then this library's [sets chapter](../../04_Sets/README.md), which covers the same ground with a program behind each claim, and then Velleman.

| Book | What it is | Verdict |
|---|---|---|
| **Daniel Velleman, *How to Prove It*** (3rd ed., Cambridge, 2019) | A proofs course whose vehicle is sets: logic, then sets, relations, functions, induction, and a closing chapter on infinite sets. | The one book for a reader at this library's level. Its angle, that every set statement is a logic statement in disguise, is the angle of [the algebra of sets](../../04_Sets/algebra_of_sets/README.md). |
| **Richard Hammack, [*Book of Proof* ↗](https://richardhammack.github.io/BookOfProof/)** (3rd ed., 2018, free) | The same course, shorter, with sets in part I. | Free and good. Read it if Velleman's price or length puts you off. |
| **Paul Halmos, *Naive Set Theory*** (1960; Dover, 2017) | A hundred pages that walk through the axioms of ZFC without ever making a fuss about them, up to ordinals, cardinals and the axiom of choice. | The classic, and still the best bridge between the language and the subject. Its one fault is terseness: a page a day is the right speed, and the few exercises are in the prose. |
| **A. Shen and N. K. Vereshchagin, *Basic Set Theory*** (AMS, 2002) | A short Russian course: cardinality, orders, ordinals, Zorn's lemma, with many problems. | The best problem collection at this level, and cheap. |
| **Derek Goldrei, *Classic Set Theory: For Guided Independent Study*** (Chapman and Hall, 1996) | An Open University text: Dedekind's reals, Cantor's theorems, the ZF axioms, ordinals and cardinals, written for a reader alone with the book. | The right first axiomatic book for self-study, because it was designed for it: the exercises come with full solutions and the prose says what to try before the proof. |

### The axioms: an undergraduate course

| Book | What it is | Verdict |
|---|---|---|
| **Karel Hrbacek and Thomas Jech, *Introduction to Set Theory*** (3rd ed., Marcel Dekker, 1999) | The standard one-semester course: axioms, relations and functions, the natural numbers, finite and countable sets, cardinals, ordinals, the axiom of choice, cardinal arithmetic, then a tour of the real numbers, filters, combinatorics and large cardinals. | The book most courses use, and the one to read after Halmos. For a reader put off by formulas it is the gentlest axiomatic text of all: chapter 1 states every axiom in English ("if every element of X is an element of Y and every element of Y is an element of X, then X = Y"), writes a property as **P**(x) and explains, before any axiom, why "the great American novels" and "the numbers that could be written down" do not define sets. It starts from an Axiom of Existence (some set exists) and derives ∅, where Cunningham assumes ∅ and Cori and Lascar derive it from logic. The last chapters are a window into the graduate subject. |
| **Herbert Enderton, *Elements of Set Theory*** (Academic Press, 1977) | The same course with more care: the natural numbers, integers, rationals and reals are built from ∅ one step at a time. | Slower and clearer than Hrbacek and Jech; the better book for a reader who wants every step. |
| **Charles Pinter, *A Book of Set Theory*** (Dover, 2014) | A clear 1971 text, revised: classes and sets, functions, orders, the natural numbers, ordinals and cardinals, the axiom of choice, and a chapter on consistency and independence. | Cheap and readable, with a chapter on classes that the others skip. |
| **Robert André, *Set Theory: An Introduction to Axiomatic Reasoning*** (University of Waterloo; free PDF on the author's page, revised editions since about 2014; from memory, the owner sent the contents and preface) | Thirty-five short chapters in ten parts: axioms and classes, class operations, relations, functions, the numbers built from sets through Dedekind cuts, infinite sets and Schröder–Bernstein, cardinals, ordinals, choice with regularity and Martin's axiom, ordinal arithmetic, and an appendix on Boolean algebras. Every chapter ends with *concept review* questions answered in the text and exercises graded A, B and C. Written, its preface says, from lecture notes based on Hrbacek and Jech, for a one-semester course that does not assume the student has written proofs before. | A good book, and free, which puts it beside Cunningham as the first axiomatic text for a reader who wants help with proof-writing; it is longer and gentler, with far more worked examples, and goes further at the end (Martin's axiom is rare in an introduction). Two cautions. First, its axioms are not quite ZF: the primitive concepts are *class*, *set* and *belongs to*, every object is a class, a set is a class that belongs to some class, and axiom A2 (class construction) says that every formula defines a *class*, with A4 (subsets) then saying a subclass of a set is a set. That is the Gödel–Bernays way, and it is honest and clean, since Russell's collection simply exists as a proper class, but no other book in this list states the axioms that way, and a reader who learned "there is no set of all sets" has to relearn it as "the class of all sets is not a set". Second, it is self-published, so expect typos and an uneven finish (its own pages promise that at first the axioms "will look like gibberish", and chapter 1 reads as a conversation rather than a text). Its own fast path, from the preface, is the right reading order for a reader who knows the language of sets: chapter 1 (ZFC), 13 and 14 (natural numbers), 18 to 22 (infinite sets and cardinals), 26 to 29 (ordinals), 32 and 33, then 30 and 31 (choice and regularity). |
| **Daniel Cunningham, *Set Theory: A First Course*** (Cambridge, 2016) | A recent undergraduate text: a chapter of logic first (truth tables, predicates, quantifiers, the formal language), then each axiom stated in English before its formula, then relations, functions, the natural numbers, cardinality, ordinals and cardinals, with exercises that carry hints. | The right first axiomatic book for a reader who found Cori and Lascar's chapter 7 opaque: it explains what the books that assume a logic course assume. Slow on purpose; stops before forcing. |
| **Keith Devlin, *The Joy of Sets*** (2nd ed., Springer, 1993) | Naive set theory, then ZFC, ordinals and cardinals, then sketches of the constructible universe, forcing and non-well-founded sets, in two hundred pages. | The widest view at this length. Dense; better as a second book than a first. |
| **Irving Kaplansky, *Set Theory and Metric Spaces*** (1972; AMS Chelsea) | Sets, cardinals, ordinals and Zorn's lemma in seventy pages, then metric spaces. | The shortest honest treatment of Zorn's lemma, by a famous expositor. |
| **Daniel Ashlock, *Basic Set Theory*** (chapter 2 of a course text for computer-science students; a [free PDF ↗](https://www.math.uh.edu/~dlabate/settheory_Ashlock.pdf) circulates, and the book's title could not be confirmed from this session) | Sets with an operator-precedence convention, De Morgan proved, induction from the well-ordering principle with Fibonacci and chocolate-bar problems, functions with injective/surjective/bijective and the two meanings of "range", permutations, a Collatz interlude, and a closing section that builds 0, 1, 2, … and ω from braces. | A brisk first course with the best problem sets at this level, and the source of this library's [induction lesson](../../11_Logic/induction/README.md). Two cautions: its precedence rules for ∩ and ∪ are its own and most books bracket instead, and its "∞ + 1" section is the von Neumann ordinals under another name, which [infinity](../../13_Axioms_of_Set_Theory/infinity/README.md) and [ordinals](../../13_Axioms_of_Set_Theory/ordinals/README.md) treat with the standard words. |
| **Erich Kamke, *Theory of Sets*** (1928; Dover, 1950) | Cantor's theory in a hundred pages: cardinals, order types, ordinals, well-ordering, in the style of its decade. (From memory.) | The oldest title still on the Dover shelf and still readable; Halmos is the better first choice, Kamke the better second for cardinal and ordinal arithmetic. |
| **Patrick Suppes, *Axiomatic Set Theory*** (1960; Dover, 1972) | ZF developed with full formal care, including the construction of the number systems, by a logician. (From memory.) | The classic between Halmos and Jech, dated in notation and thorough in proofs; most readers now take Enderton or Hrbacek and Jech instead. |
| **Robert R. Stoll, *Set Theory and Logic*** (1963; Dover, 1979) | Intuitive set theory, the number systems built from ℕ to ℝ, a logic course, Boolean algebras, then the ZF axioms in chapter 7 and first-order theories with Gödel's theorems in chapter 9, in one cheap volume. | The Dover classic: sound, patient and dated in typography and notation, with no solutions. Chapters 1 and 7 are the ones to read; Cunningham covers the same ground with more help, and Stoll is the better buy for the price. |

**How accurate is André? Chapters 1 to 8, checked claim by claim.** The owner sent pages 3 to 72, which is enough to judge the care of the writing. The verdict: good, and accurate where it matters, with the slips of a self-published text that nobody copy-edited. The axioms and the theorems are right; the slips are in asides, cross-references and one proof written in half. None would mislead a reader for long, and two or three would mislead a reader for an hour.

| Claim, pages 3–72 | Verdict |
|---|---|
| Zermelo and Fraenkel 1908–1922, with Skolem and von Neumann adjusting afterwards | right |
| Hilbert's 1899 axioms for geometry: 21, one shown redundant in 1902, 20 since | right, and a detail most books get wrong |
| Primitive concepts *class*, *set*, *belongs to*; a set is a class that belongs to a class; A2 makes every formula a class | right; this is the Gödel–Bernays presentation, as the row above says |
| A1 extent, A3 pair, A4 subsets (with the footnote that it is a schema), A5 power set, A6 union, A7 replacement (footnote: a schema; images of sets are sets), A9 regularity, choice as a choice function | right |
| A8 infinity as "a nonempty set closed under X ↦ X ∪ {X}", without requiring ∅ ∈ A | nonstandard but equivalent to the usual form over the other axioms; harmless |
| "Some of the ZF axioms listed follow from the others" (footnote 5) | right: pairing from replacement and power set, subsets from replacement |
| "In 1963 it was proven that neither the axiom of choice nor its negation can be proven from ZF" | half right: Cohen 1963 showed choice cannot be proved; that it cannot be refuted is Gödel, 1938 |
| The formal axiom of pair written as ∀x∀y∃z(x ∈ z ∨ y ∈ z) | wrong: with ∨ the sentence only asks for a set containing x *or* y, which {x} already does; the axiom needs ∧ |
| Regularity "states that non-empty classes which don't have a *least* element are not sets" | loose: it is an ∈-*minimal* member, not a least one; ∈ is not a total order |
| Points (a, b) and rationals a/b "are two-element sets {a, b} stated in a particular order" | loose: {a, b} forgets order and collapses when a = b; a pair is {{a}, {a, b}}, which chapter 4 presumably gives |
| Example (b), page 5: the collection U of all infinite sets "is an element of U" | deliberately naive, and never flagged: in the theory the book builds, U is a proper class, so U ∉ U |
| "We don't know for sure whether the ZF axioms are consistent", and ZF cannot settle it from inside | right, and a point the generic abstracts in the caution below get wrong |
| Fraenkel, Bar-Hillel and Levy on choice as "second only to Euclid's axiom of parallels" | a real quotation from *Foundations of Set Theory* (1973), from memory |
| Theorem 2.4, the class {x : x ∉ x} is not an element, and its proof | the theorem is right; the printed proof writes only one of the two cases (it assumes C ∈ C and derives C ∉ C, and never handles C ∉ C) |
| Page 18: "By Theorem 2.3 part (a), every element is equal to itself" | wrong cross-reference: reflexivity is Theorem 2.1; 2.3(a) is symmetry |
| Page 18: "Axiom A1: if x = y and x ∈ A then y ∈ A" | misquoted: A1 as stated on page 10 is extensionality; substitution of equals is a rule of logic, not A1 |
| Theorem 2.7, ∅ is a set and every set is an element; the universal class and the class of all sets are proper classes | right, and cleanly proved |
| Page 21: "No one has been able to prove that 𝒫(A) is a set", so it is postulated | misleading: it is *known* to be unprovable from the other axioms, not an open problem |
| The formal power set axiom ∀A∃P[B ∈ P ⟺ B ⊆ A] | a quantifier over B is missing; harmless |
| Example 2(e), page 22: z ∉ 𝒫(C) "since z does not appear as an element of C" | wrong reason: z ∈ 𝒫(C) means z ⊆ C, not z ∈ C; the verdict "cannot write it" is right |
| Page 30: for an empty class 𝒜, the union and the intersection of its members "are ∅ by definition" | the union is; the intersection, by the book's own formula {x : x ∈ C for all C ∈ 𝒜}, is the universal class 𝒰, which the book's theory can name; the ∅ is a convention stated as a fact ([unions](../../13_Axioms_of_Set_Theory/unions/README.md) has the same point for ZF) |
| Page 31: 𝒜 = {x : x is a set and x ∉ x}, and ∪𝒜 is not a set, via 𝒜 ⊆ 𝒫(∪𝒜) | right, and the best example in these pages: a union over a proper class fails to be a set |
| Theorems 3.5 to 3.12: absorption, double complement, De Morgan, commutative, idempotent, associative, distributive, the laws with 𝒰 and ∅, and the generalised distributive and De Morgan laws | all right; the proofs are two-inclusion arguments written line by line, which is the book's teaching method, and [the algebra of sets](../../04_Sets/algebra_of_sets/README.md) checks the same list by program |
| Chapter 4: Kuratowski's pair and Theorem 4.2; Hausdorff's pair {{c, ∅}, {d, {∅}}} and Theorem 4.10; Lemma 4.5, C × D ⊆ 𝒫(𝒫(C ∪ D)); Theorem 4.7's six product laws | all right; the two pair constructions and the lemma are checked by program on [pairs](../../13_Axioms_of_Set_Theory/pairs/README.md) and [orderings](../../04_Sets/orderings/README.md) |
| Theorem 4.9, a one-to-one correspondence between S × (U × V) and (S × U) × V | the proof shows only that φ is one-to-one; onto is obvious and unstated |
| Definition 5.1: a binary relation is "any *subset* of ordered pairs in 𝒰 × 𝒰" | 𝒰 × 𝒰 is a proper class, so "subclass"; the book's own distinction, forgotten for a line |
| Definition 5.5: T ∘ R = {(x, y) : (z, y) ∈ T for some z ∈ im R} | wrong as printed: x does not appear in the condition; the intended definition is (x, z) ∈ R and (z, y) ∈ T for some z |
| Page 53: R ∘ T = {({a}, {a}), ({∅}, {∅})} for the membership relation R and T = {(x, y) : x = {y}} | incomplete: ({a}, {a, b}) is missing, since T sends {a} to a and R sends a to {a, b}; the program on [relations and functions](../../04_Sets/relations_and_functions/README.md) computes it |
| Page 56: "distinct siblings" is symmetric and transitive | not transitive: x T y and y T x would need x T x; the book's own repair, "siblings or the same person" on page 58, is an equivalence |
| Page 57: R₃ = {(a,a), (b,b), (c,c), (d,d), (a,b), (b,a), (b,c), (c,b)} "is transitive" | not transitive: (a, b) and (b, c) are in R₃ and (a, c) is not; so R₃ is not an equivalence either, though the page treats it as the model of one |
| Page 57: symmetric + transitive does not imply reflexive, with R₂ as witness | right, and a good catch to teach |
| Chapter 6: Mortimer's ancestors (strict partial order, minimum, two maximal, no maximum); divisibility on ℤ with 0 at the bottom; Definition 6.4 on chains, maximal, maximum | right, and checked on [orderings](../../04_Sets/orderings/README.md); the molecules example calls a molecule "a set whose elements are atoms" and then counts atoms with multiplicity, which makes it a multiset |
| Chapter 7: S_x nonempty, x R y iff S_x = S_y, distinct classes disjoint; 𝒮_R a set by power set and subsets; finest and coarsest partitions; Definition 8.1 | all right |

The slips cluster where the book is being informal, cross-referencing itself, or working an example by hand; the axioms and the numbered theorems are stated and proved correctly, and three of the four errors in chapters 5 and 6 are in examples that a program settles in a line. A reader who keeps this table beside chapters 1 to 8 loses nothing, and a reader who runs the examples finds the slips themselves, which is the better lesson. The Wikipedia footnote for Russell's dates is the other sign of self-publication, and no reason to distrust the mathematics.

**On André's symbols, since the owner noticed them again.** Of every book in this guide, André's spelling is the closest to this library's own: A′ for the complement, C − D for difference, C △ D for symmetric difference, ⊆ for subset and ⊂ for proper subset, 𝒫(A) for the power set, {x : P(x)} for set-builder. Two things are new, and only one is notation. The script letters 𝒜, 𝒰 and 𝒮 mark a *class* of classes, the universal class and the class of all sets; that is spelling. The other is an idea: his complement C′ = {x : x ∉ C} is *absolute*, with no universal set chosen first, because in a class theory the class 𝒰 of everything exists and C′ is simply a class. [The algebra of sets](../../04_Sets/algebra_of_sets/README.md#the-complement-needs-a-universe) says a complement needs a universe fixed in advance, and both are right: in ZF there is no set of everything, so U must be chosen; in André's theory the complement of a set is always a proper class, so to get a *set* you intersect with a chosen U after all. Same practice, different bookkeeping.

### The subject: graduate and research

| Book | What it is | Verdict |
|---|---|---|
| **Kenneth Kunen, *Set Theory*** (College Publications, 2011; the 1980 original is *Set Theory: An Introduction to Independence Proofs*) | Axioms and combinatorics, then the constructible universe and forcing, the two tools that show what ZFC cannot decide. | The book to learn forcing from, with the best exercises in the field, and the standard text of a graduate set theory course: Ohio State's Math 6003, for one, lists it as the textbook and its syllabus (axioms, ordinals and cardinals, transitive models, L and HOD, forcing, large cardinals, descriptive set theory) is Kunen's table of contents, with a mathematical logic course as the prerequisite. Read Kunen's *Foundations of Mathematics* (2009) first for the logic it assumes. |
| **Kenneth Kunen, *The Foundations of Mathematics*** (College Publications, 2009) | Set theory, then logic, then computability, in one short cheap book: chapter I states the axioms, says in English what each one is for, and builds numbers, functions, ordinals and cardinals from them, with the formal and the informal discussion kept apart on purpose. | The best-written explanation of what the axioms mean, by the author of the standard forcing text; its exercise I.2.1, which axioms hold in seven small membership graphs, is the method of this library's [axioms chapter](../../13_Axioms_of_Set_Theory/README.md). Read it alongside Cunningham or instead of him if you prefer a terse author. |
| **Thomas Jech, *Set Theory*** (3rd millennium ed., Springer, 2003) | Three parts, basic to advanced: everything from the axioms to large cardinals, descriptive set theory, forcing and its iterations, and PCF theory. | The reference, not a textbook. Every set theorist owns it, and few read it in order. Chapter 1 is thirteen pages, with the axioms in one line each and a "Why axiomatic set theory?" worth reading now; the rest of Part I after an undergraduate course, Part II after Kunen. |
| **Azriel Levy, *Basic Set Theory*** (1979; Dover, 2002) | A thorough development of ZF with every detail, up to trees and the beginnings of descriptive set theory, without forcing. | The careful book: when another text says "it is easy to see", Levy sees it for you. |
| **Ralf Schindler, *Set Theory: Exploring Independence and Truth*** (Springer, 2014) | A fast path from the axioms to forcing and large cardinals. | For a reader who already knows the undergraduate course and wants the frontier quickly. |
| **Lorenz Halbeisen, *Combinatorial Set Theory: With a Gentle Introduction to Forcing*** (3rd ed., Springer, 2025; 2nd ed. 2017) | Four parts. I, the preliminaries: the setting (what combinatorics is, p. 3), first-order logic in a nutshell, the axioms of ZF and ZFC. II, "topics in combinatorial set theory": Ramsey's theorem as the overture, cardinal relations in ZF, forms of choice (chapter 6), two balls from one (chapter 7), models with atoms, thirteen cardinals, the shattering number, happy families, the dual Ramsey theorem. III, from Martin's axiom to Cohen forcing. IV, the combinatorics of forcing extensions: Sacks, Silver, Miller, Mathias and Laver forcing, Ramsey ultrafilters. | The friendliest road into forcing after Kunen, and the book that answers "how can combinatorics be relevant to sets": its first page defines combinatorics as the study of how large or small a collection satisfying some criteria can be, and never says "finite". Chapters 6 and 7 are now lessons here, [the forms of choice](../../13_Axioms_of_Set_Theory/choice/README.md#the-equivalent-forms-and-the-weaker-ones) and [two balls from one](../../13_Axioms_of_Set_Theory/two_balls_from_one/README.md), and the overture is [Ramsey's theorem](../../04_Sets/ramsey/README.md). His notation has a column in the [chapter 13 table](../../13_Axioms_of_Set_Theory/README.md#three-books-three-notations). |
| **Akihiro Kanamori, *The Higher Infinite*** (2nd ed., Springer, 2003) | Large cardinals, from inaccessibles to the top, with the history. | The reference for large cardinals, and the best-written history in the field. |
| **Alexander Kechris, *Classical Descriptive Set Theory*** (Springer, 1995); **Yiannis Moschovakis, *Descriptive Set Theory*** (2nd ed., AMS, 2009, free on his page) | Which sets of real numbers are tame: Borel, analytic, projective. | Kechris for the classical theory, Moschovakis for the effective one and the large-cardinal connections. |
| **Péter Komjáth and Vilmos Totik, *Problems and Theorems in Classical Set Theory*** (Springer, 2006) | A thousand problems with solutions, from cardinal arithmetic to infinite graphs. | The problem book, Hungarian style. |
| **Nik Weaver, *Forcing for Mathematicians*** (World Scientific, 2014); **Timothy Chow, "A beginner's guide to forcing"** (2008, [arXiv:0712.1320 ↗](https://arxiv.org/abs/0712.1320)) | Forcing explained to outsiders, in a hundred pages and in twenty. | Read Chow's article before any forcing chapter; it says what the construction is for. |
| **Raymond Smullyan and Melvin Fitting, *Set Theory and the Continuum Problem*** (1996; Dover, 2010) | Gödel's and Cohen's results, with an elementary approach to the constructible universe. | The gentlest route to the two independence results. |
| **Thomas Jech, *The Axiom of Choice*** (1973; Dover, 2008) | Everything about one axiom: its equivalents, its consequences, and models where it fails. | For anyone who wants to know exactly what choice buys. |

### Set theory inside a logic course: Cori and Lascar

**René Cori and Daniel Lascar, *Mathematical Logic: A Course with Exercises*** (Oxford, 2000 and 2001, two parts; the Paris logic course, translated from the French) is where the pages that prompted this guide come from: chapter 7 of Part II is set theory. It is a good book, and a hard place to start. Chapter 7 is a compressed version of the undergraduate course above, from the axioms through ordinals, cardinals and the axiom of choice to the cumulative hierarchy and relative consistency, with every axiom written as a formula in variables v₀, v₁, v₂ and every proof done in prose. That is a deliberate feature: the book's subject is logic, and the chapter's aim is to show set theory as a first-order theory, something a model can satisfy or not, which is why it opens with the distinction between the formal language and the language we speak about it. Two consequences for a reader:

- **The formulas are the content, not decoration.** The axiom of unions reads ∀v₀∃v₁∀v₂(v₂ ∈ v₁ ⇔ ∃v₃(v₃ ∈ v₀ ∧ v₂ ∈ v₃)) and nothing else; the book expects you to read it aloud as "for every set, there is a set whose members are the members of its members". The [axioms chapter](../../13_Axioms_of_Set_Theory/README.md) of this library does that reading for each axiom, symbol by symbol, and checks each one on a small universe by program.
- **"Universe" has a second meaning here.** In [the algebra of sets](../../04_Sets/algebra_of_sets/README.md), U is the universal set of one problem. In Cori and Lascar, 𝒰 is a model of the axioms and U is its set of all points; "set" means a point of U, and the book forbids itself from speaking of "the set U" inside the theory, because from inside there is no set of all sets. The two uses have one root, the collection everything under discussion is drawn from, and the second is the first taken seriously.

Read chapter 7 after Halmos or alongside Hrbacek and Jech, and read Part I's chapters on first-order logic first, which the chapter assumes. Kunen's *Foundations of Mathematics* is the same mixture of logic and set theory at twice the length and half the speed. One slip to know about: the chapter's first sentence dates the creation of set theory by Cantor to "the beginning of the twentieth century"; Cantor's papers run from 1874 to 1897, and it was the axioms, Zermelo's in 1908, that belong to the new century.

### Beyond ZFC: the map in Wikipedia's article

The owner asked whether [Wikipedia's *Set theory* ↗](https://en.wikipedia.org/wiki/Set_theory) adds anything. (Wikipedia is blocked from this session, so this is from memory of the article, and the table says how sure each claim is.) As a survey it is sound and short, and most of it is covered above or in the chapters. What it has that this library did not, until now, is the map of the subject *beside* ZFC: the other axiom systems, and the list of research areas. Three of those items change a sentence that this library repeats.

| Claim, from memory of the article | How sure | What it changes here |
|---|---|---|
| **NBG** (von Neumann–Bernays–Gödel) adds proper classes as objects, proves the same theorems about sets as ZFC, and has finitely many axioms where ZFC needs schemes | sure | The [class](../../13_Axioms_of_Set_Theory/comprehension/README.md) of all sets, which ZF can only talk around, is an object in NBG; Morse–Kelley goes one step further. |
| **New Foundations** (Quine, 1937) restricts comprehension to *stratified* formulas instead of to subsets of a given set, and in it a universal set V with V ∈ V exists | sure of the claim; the consistency of NF was open until Holmes's proof in the 2010s, and I am not sure of the date | "There is no set of everything" is a theorem of ZF, not a law of nature; the [comprehension](../../13_Axioms_of_Set_Theory/comprehension/README.md) page now says so. |
| **Kripke–Platek** is a weak set theory without power set, used in computability; **constructive** set theories (IZF, CZF) drop the excluded middle; **type theory** is the rival foundation that proof assistants such as Lean use | sure | Explains the owner's "we need Lean": Lean's foundation is type theory, with ZFC's universe buildable inside it. |
| Research areas: combinatorial set theory, descriptive set theory, inner model theory, large cardinals, determinacy, forcing, cardinal invariants of the continuum, set-theoretic topology, fuzzy set theory | sure, except that fuzzy sets are usually listed as an application rather than a branch | The graduate table above covers all but fuzzy sets and cardinal invariants; [day or night](../../12_Learning_to_Learn/day_or_night/README.md) has fuzzy membership. |
| **Objections**: Poincaré ("a disease"), Brouwer and the intuitionists, Wittgenstein; and category theory, Lawvere's ETCS, as an alternative foundation | fairly sure of the names; the Poincaré quotation is disputed and may be apocryphal | Lawvere and Rosebrugh's book, above, is the category view. |
| **Education**: the 1960s "New Math" put sets into primary school and was abandoned; Venn diagrams survived | sure | Nothing to change. |

So: read the article once for the map, especially the paragraph on NF, and come back to the books for everything else.

**A caution about infographics.** Two pictures of the kind that circulate on social media reached the owner, and both are worth a warning. An "Areas of set theory" map listed the eight areas above correctly and drew two of them wrong: its large-cardinal pyramid put Woodin cardinals above supercompact ones, when a supercompact cardinal is the stronger notion, and its inner-model diagram nested HOD inside L, when L is the smallest inner model and L ⊆ HOD ⊆ V. A "Set theory symbols" chart was an AI-generated image whose columns had slipped: ∉ missing, two meanings on ⊂ and on ⊆, "empty set" and "universal set" listed twice, "symmetric d-" cut off, and |A| paired with "implies" and "therefore". Such a chart looks authoritative and will be learned from, which is the harm; a symbol table has to say that ⊂ means "proper subset" in some books and "subset" in others, and the [glossary's table](../../GLOSSARY.md#symbols) does. The rule the owner uses for pasted summaries applies to pictures too: a table of what is sure and what is not, never a copy.

A third chart, a hand-lettered "Set Theory Symbols" with eight entries, is the one to keep, with three notes. Its ∈, ∉, ⊆, ∪, ∩, ∅ and 𝒫 are right, and 𝒫({1, 2}) = {∅, {1}, {2}, {1, 2}} is the right example. Entry 3, ⊂ as "proper subset" with {1, 2} ⊂ {1, 2, 3}, is right in Cunningham's and this library's convention and wrong in Jech's and Halmos's, where ⊂ allows equality; the chart does not say so, and that is the one trap. Entry 7's example "A = ∅" names the empty set rather than showing one; {x ∈ ℕ : x < 0} = ∅ would show it, and the chart should add that {∅} is not empty. And "total set theory symbols = 8" is the kind of sentence a chart should not make: the [glossary's table](../../GLOSSARY.md#symbols) has twenty-two rows, and ∖, the complement, ×, |A|, the set-builder braces and the quantifiers are the ones a reader meets next.

A fourth, a 24-symbol "ultimate cheat sheet" from an exam-tutoring account, is correct throughout, with the same unspoken ⊂ convention as the third, and it has what the third lacked: the complement written as U − A with the universal set named, ∉, ⊄ and ⊉, the ordered pair, A × B, |A| and ∅ = { }. Two phrases to read with care: "a collection of well-defined objects" is the textbook sentence that [what is a set?](../../04_Sets/what_is_a_set/README.md) takes apart, and "|A| is the number of elements" is right for finite sets only, since [cardinality](../../04_Sets/cardinality/README.md) is defined by matching. Everything on it is in the [glossary](../../GLOSSARY.md), with the page that explains each symbol; the sheet is useful as a reminder before an exam and useless as a place to learn from, because a symbol's meaning is its definition and a card has no room for one.

A fifth, "Set Theory & Logic Symbols" in 36 tiles, has three mistakes of the kind that teach a wrong symbol for good: the tile labelled "contains" shows A ∃ a, the quantifier, where the mirrored membership sign A ∋ a belongs; the tile for the universal set shows ξ, a Greek letter no book uses for it (U, 𝒰, E or Ω are the spellings); and A ⊣ B is labelled "does not yield", when ⊬ is "does not prove" and ⊣ is the turnstile read backwards. Its "improper subset" for ⊆ is a phrase to drop, since ⊆ is simply the subset sign with equality allowed. The rest, including ⊢, ∴, ∵, ∃! and the tombstone, is right, and all 36 are now in the [glossary's symbol index](../../GLOSSARY.md#symbol-index).

The owner then found the one web table worth bookmarking, [Math Vault's set theory symbols ↗](https://mathvault.ca/hub/higher-math/math-symbols/set-theory-symbols/) (blocked from this session; two of its tables arrived as screenshots). Its relational table states the ⊂ convention it uses, A ⊂ B ⟺ A ⊆ B and A ≠ B, explains ⊄ by the witness, an x ∈ A with x ∉ B, and has ∋ and ∌ right; its cardinality table has |ℕ| = |ℤ|, the alephs with the continuum hypothesis as ℵ₁ = 2^ℵ₀, the beths, the gimel function, 𝔠 = |ℝ| = |𝒫(ℕ)|, ω + 1 = ω ∪ {ω}, ε₀ and κ⁺, every one correct. Its only convention to know is Ω = ω₁, Cantor's use, where Halbeisen writes Ω for the class of all ordinals.

**An online course with its own vocabulary.** The owner also asked about [settheory.net ↗](https://settheory.net/sets/all2), Sylvain Poirier's *Set Theory and Foundations of Mathematics* (blocked from this session; from memory). It is a serious, original, self-published course that presents set theory and model theory together as one theory, with functions and operators as primitives beside sets, with the universe of sets thought of as growing in time, and with terms of its own for all of it ("meta-objects", "one-model theory"). That is its interest and its cost: a reader who knows the standard story will find a genuinely different angle, and a reader learning the subject will find words no textbook uses and no exercise sheet tests. Read it after Hrbacek and Jech or Cunningham, as a second view, and not instead of them.

Its companion, [Wikipedia's *Glossary of set theory* ↗](https://en.wikipedia.org/wiki/Glossary_of_set_theory), is a different kind of page: several hundred one-line entries, alphabetical, from *absolute* and *aleph* to *Zorn's lemma*, with a symbols section at the top. (Also from memory.) It is written for someone who already knows the subject and has forgotten a word, so it is the wrong place to learn a term and the right place to check one: an entry such as *club set* or *Δ-system* is a sentence, not an explanation. Use it the way this library's own [glossary](../../GLOSSARY.md) is meant to be used, as the index that points back to a page, and when an entry there has no page here, that is a gap to note in the [roadmap](../../ROADMAP.md).

### Philosophy, history and the popular shelf

| Book | What it is |
|---|---|
| **Michael Potter, *Set Theory and Its Philosophy*** (Oxford, 2004) | The axioms developed with the philosophical questions kept in view: why these axioms, and what the hierarchy of sets is. |
| **Penelope Maddy, ["Set-theoretic foundations" ↗](https://sites.socsci.uci.edu/~pjmaddy/bio/STF%20printed%20version.pdf)** (free on her page; from memory, in *Foundations of Mathematics*, Contemporary Mathematics 690, AMS, 2017) | What it means to say set theory is "the foundation" of mathematics, taken apart into the separate jobs the phrase covers (a shared arena, a risk assessment, a final court of appeal, a meta-mathematical corral) and which of them category theory could do instead. The clearest short answer to "why is set theory important, or is it not?" by the leading philosopher of the subject. |
| **[Internet Encyclopedia of Philosophy, "Set Theory" ↗](https://iep.utm.edu/set-theo/)** (free) | A survey like the Stanford entry, shorter and more elementary; a good second map. (From memory.) |
| **José Ferreirós, *Labyrinth of Thought: A History of Set Theory*** (2nd ed., Birkhäuser, 2007) | The history from Riemann and Dedekind to Zermelo, and the best account of how the subject came out of nineteenth-century analysis and algebra. |
| **Joseph Dauben, *Georg Cantor: His Mathematics and Philosophy of the Infinite*** (Harvard, 1979) | The biography, with the mathematics. |
| **John Stillwell, *Roads to Infinity*** (A K Peters, 2010) | Cantor, ordinals, Gödel and large cardinals for a reader with first-year mathematics; the readable bridge between the popular books and the textbooks. |
| **N. Ya. Vilenkin, *Stories about Sets*** (Academic Press, 1968); **Raymond Smullyan, *Satan, Cantor and Infinity*** (Knopf, 1992) | Two popular books that are also correct. Vilenkin's is the Soviet classic for schoolchildren; Smullyan's is puzzles. |
| **F. William Lawvere and Robert Rosebrugh, *Sets for Mathematics*** (Cambridge, 2003) | Sets done through their functions rather than their members, the category-theoretic view; a different subject with the same name again. |
| **Joan Bagaria, "Set Theory", [*Stanford Encyclopedia of Philosophy* ↗](https://plato.stanford.edu/entries/set-theory/)** (free, revised periodically) | A survey by a working set theorist: origins, the ZFC axioms, ordinals and cardinals, the continuum hypothesis, Gödel's L and Cohen's forcing, large cardinals, determinacy and descriptive set theory, with a bibliography. (This description is from memory; the page could not be fetched from this session.) The right free map of the whole subject, and nothing in it is new relative to the books above, since a survey is what it sets out to be; read it once before choosing a graduate book, and its sibling entries on the axiom of choice, the continuum hypothesis and large cardinals as each topic comes up. |
| **Jean van Heijenoort (ed.), *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*** (Harvard, 1967); **William Ewald (ed.), *From Kant to Hilbert*** (2 vols., Oxford, 1996) | English translations of the founding papers, with introductions. Most of the table below is in one or the other. |

**Amazon's best-seller list for set theory** (which the owner asked about; the page is blocked from this session) ranks by sales, not by fitness for a reader, and from memory it is the Dover shelf plus the standard texts: Halmos, Jech, Enderton, Stoll, Suppes, Kamke, Hrbacek and Jech, Cunningham, Goldrei, Pinter, Smullyan and Fitting, Devlin, with the odd Venn-diagram puzzle book. Every one of those has a verdict in the tables above; the list adds no title worth reading that they lack.

**A caution about search results.** A search for "set theory and its role in modern mathematics" turns up several papers with that title or abstract in journals such as JETIR, Longdom and uploads on ResearchGate (one from 2025, apparently from El Shorouk Academy, whose abstract the owner pasted). Their abstracts are generic, they are not peer-reviewed in any meaningful sense, and the one definite claim in the pasted abstract, that axiomatic set theory "establishes consistency", is false by Gödel's second incompleteness theorem. ResearchGate is blocked from this session, so the paper itself could not be read; nothing in its abstract suggests it would add to the books and essays above. Maddy's essay is the serious version of the same question.

### Tools: languages, proof assistants, model finders

The owner asked whether any programming language is related to set theory, and what other tools there are. Yes, on three levels, and the division of labour between them is the one this library's chapter on the axioms draws: a language *uses* sets, a model finder *checks* a theory on a small universe, a proof assistant *proves* theorems about all of them. (Versions and dates from memory; none of these sites could be fetched from this session.)

| Tool | What it is | Where it sits |
|---|---|---|
| **SETL** (Jack Schwartz, NYU, 1969) | The language whose values *are* sets, tuples and maps, with set-builder expressions as syntax: `{x in S | p(x)}` is a statement. Python's comprehensions and `set` type descend from it through ABC, and the first working Python compiler for Ada was written in it. | The direct ancestor of what every program in this library does. |
| **Python's `set`, `frozenset`, comprehensions**; **SQL** | Python's `set` is a finite set with ∪ ∩ ∖ △ ⊆ as operators and comprehensions as separation, which [sets in Python](../../04_Sets/python_sets/README.md) walks through. SQL is Codd's relational model: a table is a relation, `WHERE` is separation, `JOIN` is a relation product, `GROUP BY` is a partition. | The language of sets as it is used by millions who never say "set theory". |
| **Haskell, ML, Lean's type theory** | Functional languages whose type systems are the rival foundation, type theory: a value has a type, and there is no ∈ between arbitrary objects. | Why "we need Lean" is right and also a change of foundation. |
| **Alloy** (Daniel Jackson, MIT) | A relational language with a SAT-based *model finder*: write a specification in terms of sets and relations, bound the universe, and it searches for a model or a counterexample. | Exactly what the programs in [the axioms chapter](../../13_Axioms_of_Set_Theory/README.md) do by brute force, done well: Kunen's exercise I.2.1 is an Alloy exercise. |
| **TLA⁺** (Leslie Lamport) and the **B method** (Jean-Raymond Abrial; **Atelier B**, **Rodin**) | Specification languages whose mathematics is ZF set theory with first-order logic, used for distributed algorithms at Amazon Web Services and for the driverless Paris Métro Line 14. The TLA⁺ model checker TLC enumerates states; Rodin discharges proof obligations. | Set theory as an engineering notation, with a model checker beside it. |
| **Metamath**, with its database **set.mm** | A proof verifier with no built-in logic at all: set.mm starts from the ZFC axioms written as formulas like the ones in the chapter and derives tens of thousands of theorems, each checkable in milliseconds. The proof of 2 + 2 = 4 from the axioms is famous for its length. | The closest thing to "ZFC, verified": every step is substitution. |
| **Isabelle/ZF** and **Isabelle/HOL**; **Mizar** | Isabelle/ZF formalises ZF directly (Paulson's constructible universe is in it); Isabelle/HOL and Mizar use typed set theory, and Mizar's library, the MML, is the largest body of checked classical mathematics after Lean's. | Proof assistants in which set theory is the object language. |
| **Lean 4** with **Mathlib** | The proof assistant most mathematicians now learn. Its foundation is dependent type theory, with ZFC's universe built inside it as a type (`Mathlib.SetTheory.ZFC`), and its cardinals and ordinals as types of their own. | Where to go after the chapter, if "a proof, not a check" is the goal; its *Natural Number Game* and *Mathematics in Lean* are the on-ramps. |
| **Coq / Rocq**, **Agda** | The other dependent-type-theory assistants; Coq's `Ensembles` library is set theory as predicates. | Same family as Lean, older. |
| **Sage**, **Mathematica**, **Maple** | Computer algebra systems with finite set types and combinatorics: Sage's `Set`, `Subsets`, `Posets`, `SetPartitions` draw Hasse diagrams and count Bell numbers. | For the finite combinatorics of this chapter at larger sizes than Python prints comfortably. |
| **Z notation**, **VDM** | The older specification notations built on sets and schemas, ISO-standardised, taught in formal-methods courses. | History, and still read. |
| **OEIS** | The On-Line Encyclopedia of Integer Sequences: Bell numbers (A000110), partial orders on n points (A001035), equivalence relations, posets up to isomorphism. | Where [orderings](../../04_Sets/orderings/README.md) checked its count of 19. |

The path from here: Python for finite models (this library), Alloy or TLC when the models get large, Metamath to see ZFC run with no interpretation at all, Lean when the goal is a proof. The reading guide for logic that would place the proof assistants properly is on the [roadmap](../../ROADMAP.md).

### Po polsku: the Polish school

Poland is where much of the subject was built. *Fundamenta Mathematicae*, founded in Warsaw in 1920 by Sierpiński, Mazurkiewicz and Janiszewski, was the first journal devoted to one field, set theory and its applications, and Sierpiński, Kuratowski, Tarski, Banach, Ulam, Lindenbaum and Mostowski wrote their papers in it. Its early volumes are free to read at the [Polish digital mathematics library ↗](https://matwbn.icm.edu.pl/). The textbooks of that school are still the standard Polish first-year course:

| Book | What it is |
|---|---|
| **Helena Rasiowa, *Wstęp do matematyki współczesnej*** (PWN, 1968, many editions; English *Introduction to Modern Mathematics*, 1973) | The classic first-year text: logic, sets, relations, functions, cardinals, orders. The Polish counterpart of Velleman, written by a logician. |
| **Wiktor Marek and Janusz Onyszkiewicz, *Elementy logiki i teorii mnogości w zadaniach*** (PWN, 1972, many editions) | The problem book every Polish mathematics student has done. |
| **Wojciech Guzicki and Paweł Zakrzewski, *Wykłady ze wstępu do matematyki: wprowadzenie do teorii mnogości*** and ***Wstęp do matematyki: zbiór zadań*** (PWN, 2005) | The current Warsaw course and its problems, up to ordinals, cardinals and the axiom of choice. |
| **Kazimierz Kuratowski, *Wstęp do teorii mnogości i topologii*** (PWN, 1955, many editions; English *Introduction to Set Theory and Topology*) | Sets as the first half of a topology course, by the man who defined the ordered pair. |
| **Kazimierz Kuratowski and Andrzej Mostowski, *Teoria mnogości*** (PWN, 1952, 2nd ed. 1966; English *Set Theory, with an Introduction to Descriptive Set Theory*, North-Holland, 1976) | The Polish graduate text of its era: everything up to descriptive set theory, by two of the people who made it. |
| **Wacław Sierpiński, *Cardinal and Ordinal Numbers*** (PWN, 1958; 2nd ed. 1965) | The classic monograph on cardinal and ordinal arithmetic, in English from a Polish press. |

### Suggested paths

- **From this library:** Velleman, then Halmos or Goldrei, then Hrbacek and Jech. Shen and Vereshchagin for problems along the way.
- **Allergic to formal notation:** Hrbacek and Jech first, whose axioms are English sentences, then Cunningham or André, whose early chapters teach the notation and the proof-writing the others assume, and only then Cori and Lascar or Jech.
- **Want a free book with many worked examples and graded exercises:** André, on his preface's fast path, with this library's [axioms chapter](../../13_Axioms_of_Set_Theory/README.md) beside its chapter 1.
- **Reading Cori and Lascar:** Cunningham or Kunen's *Foundations* first, their Part I alongside, Hrbacek and Jech when chapter 7 goes too fast.
- **Toward the frontier:** Hrbacek and Jech, then Kunen with his *Foundations* beside it, then Jech as the reference, then Kanamori or Kechris by taste.
- **For the story:** Stillwell, then Ferreirós, then the papers themselves in van Heijenoort and Ewald.

## The founding papers

The subject began in papers that are mostly a few pages long, and reading them is easier than their reputation suggests, because the authors were explaining ideas that were new. Years and journals here are from memory; the free archives linked at the end hold the originals.

| Year | Paper | What it did | In the program |
|---|---|---|---|
| 1874 | Cantor, "Über eine Eigenschaft des Inbegriffes aller reellen algebraischen Zahlen", Crelle's journal 77 | The algebraic numbers are countable, the reals are not: the first proof that there are different sizes of infinity, and the birth of the subject. | Section 1 |
| 1878 | Cantor, "Ein Beitrag zur Mannigfaltigkeitslehre", Crelle 84 | The line and the plane have the same cardinality ("I see it, but I don't believe it"), and the continuum hypothesis is first stated. | |
| 1883 | Cantor, *Grundlagen einer allgemeinen Mannigfaltigkeitslehre* | The ordinal numbers, and the claim that every set can be well-ordered. English in Ewald. | |
| 1888 | Dedekind, *Was sind und was sollen die Zahlen?* | The natural numbers from sets and chains, the recursion theorem, and "infinite" defined as matching a proper part of oneself. English in Dover's *Essays on the Theory of Numbers* and in Ewald. | Section 2 |
| 1891 | Cantor, "Über eine elementare Frage der Mannigfaltigkeitslehre", Jahresbericht der DMV 1 | The diagonal argument, and the theorem that the subsets of a set outnumber its members. English in Ewald. | Section 3 |
| 1895, 1897 | Cantor, "Beiträge zur Begründung der transfiniten Mengenlehre", Mathematische Annalen 46 and 49 | Cardinals and ordinals laid out as a theory, ℵ₀ and its arithmetic. English as *Contributions to the Founding of the Theory of Transfinite Numbers* (Jourdain, 1915; Dover). | |
| 1902 | Russell, letter to Frege of 16 June | The paradox of the set of all sets that are not members of themselves, in a page. In van Heijenoort, with Frege's reply. | |
| 1904 | Zermelo, "Beweis, daß jede Menge wohlgeordnet werden kann", Mathematische Annalen 59 | The axiom of choice stated and used, to prove that every set can be well-ordered, in three pages. In van Heijenoort. | |
| 1908 | Zermelo, "Untersuchungen über die Grundlagen der Mengenlehre I", Mathematische Annalen 65 | The axioms: Zermelo set theory, the Z of ZF. In van Heijenoort. | |
| 1914 | Hausdorff, *Grundzüge der Mengenlehre* | The first textbook of the subject, and the book in which topology was born; the paradoxical decomposition of the sphere is in its appendix. English of the 1937 edition as *Set Theory* (AMS Chelsea). | |
| 1921 | Kuratowski, "Sur la notion de l'ordre dans la théorie des ensembles", Fundamenta Mathematicae 2 | The ordered pair as the set {{a}, {a, b}}, which [the Cartesian product](../../04_Sets/cartesian_product/README.md) uses. | |
| 1922 | Fraenkel, and independently Skolem, on the axiom of replacement | The F of ZF, and Skolem's remark that the axioms, being first-order, have countable models. Both in van Heijenoort. | |
| 1923 | von Neumann, "Zur Einführung der transfiniten Zahlen", Acta Szeged 1 | Each ordinal is the set of the smaller ordinals, so the natural numbers are 0 = ∅, 1 = {0}, 2 = {0, 1}. In van Heijenoort. | Section 4 |
| 1924 | Banach and Tarski, "Sur la décomposition des ensembles de points en parties respectivement congruentes", Fundamenta Mathematicae 6 | A ball cut into finitely many pieces that reassemble into two balls, from the axiom of choice. | |
| 1930 | Ulam, "Zur Masstheorie in der allgemeinen Mengenlehre", Fundamenta Mathematicae 16 | Measurable cardinals, the beginning of large cardinals, from a question about measures. | |
| 1935 | Zorn, "A remark on method in transfinite algebra", Bulletin of the AMS 41 | Zorn's lemma, the form of the axiom of choice that algebra uses. | |
| 1938 | Gödel, "The consistency of the axiom of choice and of the generalized continuum-hypothesis", PNAS 24 | Two pages: the constructible universe, in which choice and the continuum hypothesis hold, so neither can be refuted from ZF. The 1940 monograph has the proofs. | |
| 1961 | Scott, "Measurable cardinals and constructible sets", Bulletin of the Polish Academy of Sciences 9 | A measurable cardinal contradicts Gödel's V = L: large cardinals and constructibility pull apart. | |
| 1963, 1964 | Cohen, "The independence of the continuum hypothesis" I and II, PNAS 50 and 51 | Forcing: models of ZF in which the continuum hypothesis fails, so it cannot be proved either. The Fields Medal of 1966. | |
| 1970 | Solovay, "A model of set theory in which every set of reals is Lebesgue measurable", Annals of Mathematics 92 | Without the axiom of choice, every set of reals can be measurable: the pathologies of analysis come from choice. | |

Where to read them for free: the German originals of Cantor, Zermelo and Hausdorff are scanned at the [Göttingen digitisation centre ↗](https://gdz.sub.uni-goettingen.de/), which holds Crelle's journal and the *Mathematische Annalen*; the Polish papers are at the [Polish digital mathematics library ↗](https://matwbn.icm.edu.pl/); the two-page notes of Gödel and Cohen are open at [PNAS ↗](https://www.pnas.org/); Jourdain's translation of Cantor and Beman's of Dedekind are on the [Internet Archive ↗](https://archive.org/). For English translations with context, van Heijenoort and Ewald, above.

### A textbook's history box, checked

Sullivan's *Precalculus* has a "Historical Feature" on counting and probability, and the owner asked whether it is good history. Mostly, with one large error and two about notation.

| Claim | How sure | Note |
|---|---|---|
| Counting and probability took form in the 1654 letters of Fermat and Pascal on dividing the stakes of an interrupted game | sure | the standard account |
| "Set theory" took form there too | wrong | set theory began with Boole's algebra of classes (1847) and Cantor's paper of 1874, two centuries later; the box conflates the subject with its use in counting |
| Fermat listed the cases, Pascal used the arithmetical triangle | sure | |
| Huygens's book of 1657 was the first on probability and introduced expectation | sure | |
| Cardano's treatise, published only in 1663, came too late to matter | sure | written about 1564 |
| Jakob Bernoulli's *Ars Conjectandi* (1713, posthumous) "gave the theory the form it would have until 1900" | half | the date is right; Laplace reshaped the subject in 1812 and Kolmogorov's axioms of 1933 gave it its present form |
| C(n, r) and P(n, r) are English notation from after 1830 | from memory, cannot confirm | plausible |
| The notation (n over r) "goes back to Euler" and "is now losing ground" | wrong twice | Euler used brackets, [n/r]; the vertical form is Ettingshausen's (1826). And it is not losing ground: it is the standard notation of mathematics, and C(n, r) survives mainly in school books and on calculators |
| ∪ and ∩ were introduced by Peano in 1888 | sure | |
| ⊂ was introduced by Schröder about 1890 | mostly | Schröder's 1890 sign was for subsumption; Gergonne had a C for containment in 1817 |
| Boole wrote A + B for union and AB for intersection; statisticians still write AB | half | AB, yes; Boole's + was only for disjoint classes, and Jevons (1864) made it the union of any two. Statisticians' P(AB) for P(A ∩ B) is right |

The problem of points in the box, A needing two points and B three, is the one program the box invites: list the 16 outcomes of four more plays, and A wins in 11 of them, so the stakes split 11 to 5. The founding papers section above is this page's own history of set theory, for comparison.

## Questions a learner asks, with short answers

The questions below came up, in this order, while the owner of this library read the books above. Each answer is short, and names the page where the long one is.

**What is a universal set?** The set of everything under discussion in one problem, fixed before the problem starts; the rectangle of a Venn diagram, out of which complements are taken. Not a set of everything, which does not exist, and a choice, so the same A has different complements under different U. [The algebra of sets](../../04_Sets/algebra_of_sets/README.md).

**These axioms seem silly and obvious at the same time.** Because they are demands, not descriptions: every axiom but extensionality says "there is a set whose members are …", and on a universe of sixteen small sets, pairs, power set, replacement and infinity each come out false, each failure being a set the axiom asks for that the universe lacks. The one rule that seems most obvious, "every property has a set", contradicts itself in two lines, which is why there is a list at all. [The axioms chapter](../../13_Axioms_of_Set_Theory/README.md), [reading a formula](../../13_Axioms_of_Set_Theory/reading_a_formula/README.md), [comprehension](../../13_Axioms_of_Set_Theory/comprehension/README.md).

**I miss the formal characters: inverted A and E, the strange biconditional, predicates, quantifiers.** ∀ is an upside-down A for *All* and runs as a loop that must succeed every time; ∃ is a backwards E for *Exists* and must succeed once; a predicate is a statement with a hole; ⇔ between sentences says their truth-table columns agree, while ↔ is a connective inside a sentence; ≃ is Cori and Lascar's equals sign in the formal language. [Truth tables](../../11_Logic/truth_tables_and_laws/README.md), [predicates and quantifiers](../../11_Logic/predicates_and_quantifiers/README.md), [reading a formula](../../13_Axioms_of_Set_Theory/reading_a_formula/README.md).

**Every book uses different notation. Why can't authors agree?** Each inherits a tradition (Peano, Bourbaki, the Polish school, computer science) and optimises the symbols for its own chapter. The definitions never vary, only the ink; the [glossary's symbol table](../../GLOSSARY.md#symbols) lists seven books side by side, and the [chapter table](../../13_Axioms_of_Set_Theory/README.md) four. Two real traps: Jech's ⊂ allows equality and Cunningham's does not; Simovici writes gf for what the others write g ∘ f.

**We already have a cardinality lesson. Is it the same cardinality?** Yes. [Cardinality of sets](../../04_Sets/cardinality/README.md) defines size by bijection; the axioms chapter supplies the bijections and the sets they compare, and Cantor's theorem returns as a consequence of the [power set axiom](../../13_Axioms_of_Set_Theory/power_set/README.md). The topic map's thread "From a set to its axioms" links the two.

**Why learn these theorems? Which branches of mathematics use set theory? Is it practical?** Every proof that two sets are equal is extensionality; relations, functions, graphs and database tables are sets of pairs; topologies and probability spaces live in power sets; induction is the axiom of infinity; a basis for every vector space is the axiom of choice; termination proofs and Goodstein's theorem are the ordinals. Databases, formal methods (B, TLA⁺, Alloy) and proof assistants use the whole package. Number theory builds ℕ from the axioms once and then forgets them, except for theorems like Goodstein's, which Peano arithmetic cannot prove. The table by axiom is on the [chapter page](../../13_Axioms_of_Set_Theory/README.md); the applications of relations and equivalences are on [their pages](../../04_Sets/relations_and_functions/README.md).

**How to learn this: theorems? proofs and propositions? What mathematics first?** Learn the moves, not the theorems: the proofs of a first course use five patterns, listed on the [axiom katas](../../13_Axioms_of_Set_Theory/axiom_katas/README.md) page, and recognising the pattern turns a proposition from a fact to memorise into an example. Before an axiomatic book you need one proofs course: nested quantifiers, induction, and [injective and surjective](../../04_Sets/relations_and_functions/README.md#the-three-words), the two words that drive everyone mad and that the relations page explains with their Latin. The [chapter page](../../13_Axioms_of_Set_Theory/README.md) has the study routine and the chapter order in each book.

**At this level Python is useless; we need Lean.** Half right. Python checks a finite model, which is what every program in the chapter does and what Kunen's first exercise asks for; a proof assistant proves theorems about all models. The division of labour is the right one, and a Metamath or Lean page is in the inbox.

**Graphs and functions have a connection to sets? Cartesian product in the context of sets?** A relation is a set of ordered pairs, a function is a relation in which each input has one output, a graph is a relation drawn as arrows, a database table is a relation stored; the Cartesian product A × B is the set all such pairs are drawn from, and Kuratowski's (a, b) = {{a}, {a, b}} makes a pair out of nothing but sets. [Relations and functions](../../04_Sets/relations_and_functions/README.md), [the Cartesian product](../../04_Sets/cartesian_product/README.md), [pairs](../../13_Axioms_of_Set_Theory/pairs/README.md).

**What the heck is a multiset? What are algebras? What is a monoid?** A multiset is a function from a set to ℕ giving each member a count, written [2, 2, 2, 5, 7, 7]; a prime factorisation is one, Python's `Counter` is one, and gcd and lcm are its intersection and union. An algebra, in Simovici and Djeraba's sense, is a set with some operations on it, each of a fixed arity. A monoid is one associative operation with a unit: ℕ with × and 1, or ℕ with gcd and 0. The [glossary](../../GLOSSARY.md) has multiset; [the laws of an operation](../../06_Algebraic_Structures/laws_of_an_operation/README.md) has monoid, semigroup and group.

**How good is this book, and what chapters first?** Verdicts for each book are in the tables above. The short reading order, for a reader put off by formulas: Hrbacek and Jech chapters 1 and 2, whose axioms are English sentences; then Cunningham chapter 1, which teaches the notation the others assume; then Cori and Lascar chapter 7 with Jech chapter 1 beside it; Kunen's *Set Theory* when forcing is the goal. The Ohio State graduate course chose Kunen because its syllabus is Kunen's table of contents and its prerequisite is a logic course. The Stanford Encyclopedia entry is a free survey and a good map, with nothing new relative to the books.

**Add some katas.** [Set katas](../../04_Sets/set_katas/README.md) (Cunningham 1.1), [function katas](../../04_Sets/function_katas/README.md) (Hrbacek and Jech 3.1–3.13 and 4.1–4.3, with solutions) and [axiom katas](../../13_Axioms_of_Set_Theory/axiom_katas/README.md) (Jech, Cunningham, Kunen): in each, a program checks the claim on a small universe before you look for the proof.

## What this library already covers

The [terms map](../set_theory_terms/README.md) is the long version of this section: the owner's list of some 700 terms of set theory, each linked to the lesson or glossary entry that covers it, the rest named with the book that does.

- [04_Sets](../../04_Sets/README.md) — the language: [what a set is](../../04_Sets/what_is_a_set/README.md), with extensionality, separation and Russell's paradox; [the algebra of sets](../../04_Sets/algebra_of_sets/README.md); [the Cartesian product](../../04_Sets/cartesian_product/README.md) with Kuratowski's pair; [cardinality](../../04_Sets/cardinality/README.md) with the diagonal argument.
- [13_Axioms_of_Set_Theory](../../13_Axioms_of_Set_Theory/README.md) — the axioms of Zermelo and Fraenkel one page each, read aloud and checked on a small universe, from Cori and Lascar's chapter 7.
- [02_Measure_Zero](../../02_Measure_Zero/README.md) — [countable sets](../../02_Measure_Zero/countable_sets/README.md) and [the Cantor set](../../02_Measure_Zero/cantor_set/README.md), Cantor's other legacy.
- [11_Logic](../../11_Logic/README.md) — the if–then that every axiom is written in.

What it does not cover: ordinals beyond the finite ones, cardinal arithmetic, the axiom of choice at work, and anything about models. Those are the books'.

## Po polsku, w skrócie

„Teoria mnogości" to dwie rzeczy pod jedną nazwą. Pierwsza to język: zbiory, podzbiory, suma, para uporządkowana, relacja, funkcja, równoliczność, lemat Zorna. Tego języka używa każdy kurs z dowodami od pierwszego wykładu i dobra książka wykłada go w sto stron; w Polsce robi to *Wstęp do matematyki współczesnej* Rasiowej, a zadania są u Marka i Onyszkiewicza oraz u Guzickiego i Zakrzewskiego. Druga to przedmiot badań: jakie dokładnie są reguły budowania zbiorów (aksjomaty Zermelo–Fraenkla) i co z nich wynika. Tam żyją słynne twierdzenia Gödla i Cohena, że pewnika wyboru ani hipotezy continuum nie da się z pozostałych aksjomatów ani udowodnić, ani obalić. Kto pyta o „książkę o zbiorach", zwykle chce pierwszej, a dostaje drugą, i stąd opinia, że to trudne.

Po angielsku droga wygląda tak: Velleman albo darmowy Hammack (język), potem Halmos albo Goldrei (aksjomaty bez zadęcia), potem Hrbacek i Jech (kurs), a dalej Kunen (forsing) i Jech (encyklopedia). Rozdział 7 książki Coriego i Lascara, z którego pochodzą przysłane strony, to ten sam kurs ściśnięty i zapisany formułami logiki pierwszego rzędu; to dobra książka, ale do czytania po Halmosie, nie zamiast niego. Słowo „uniwersum" znaczy tam co innego niż na diagramie Venna: nie zbiór wszystkiego, o czym mowa w zadaniu, lecz model aksjomatów widziany z zewnątrz.

Polska szkoła tę dziedzinę współtworzyła: *Fundamenta Mathematicae*, założone w Warszawie w 1920 roku, było pierwszym czasopismem poświęconym jednej dziedzinie, a pisali w nim Sierpiński, Kuratowski, Tarski, Banach, Ulam i Mostowski. Dawne tomy są darmowe w Bibliotece Wirtualnej Matematyki. Program na tej stronie uruchamia cztery wyniki założycielskie na małych zbiorach: wyliczenie liczb algebraicznych według „wysokości" (Cantor 1874), definicję zbioru nieskończonego jako równolicznego ze swoją właściwą częścią (Dedekind 1888), argument przekątniowy (Cantor 1891) i liczby naturalne von Neumanna, gdzie każda liczba jest zbiorem mniejszych (1923).

## Run it yourself

From the root of your clone of this repository:

```bash
python3 reading_guides/set_theory/examples/classic_set_theory.py
```

## See also

- [13_Axioms_of_Set_Theory](../../13_Axioms_of_Set_Theory/README.md) — each axiom read aloud and checked by a program
- [What is a set?](../../04_Sets/what_is_a_set/README.md) — extensionality, separation and Russell's paradox, the first three ideas of any of these books
- [Cardinality of sets](../../04_Sets/cardinality/README.md) — the diagonal argument on sequences of bits
- [Countable sets](../../02_Measure_Zero/countable_sets/README.md) — listing the rationals, the same trick as Cantor's height
- [Linear algebra: a reading guide](../linear_algebra/README.md) and [Precalculus: a reading guide](../precalculus/README.md) — the other guides, same format
- [Set theory ↗](https://en.wikipedia.org/wiki/Set_theory) and [Zermelo–Fraenkel set theory ↗](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory) — Wikipedia
