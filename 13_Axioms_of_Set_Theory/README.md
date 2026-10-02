# 13_Axioms_of_Set_Theory — the rules for building sets, one page each

**Level:** 201 · for anyone opening an axiomatic set theory book, Cori and Lascar, Cunningham or Jech, and stopping at the first ∀v₀∀v₁

The axioms of Zermelo and Fraenkel are nine sentences, and a reader meeting them for the first time has two complaints at once: they are unreadable, written in a formal language of ∀, ∃, ⇒ and v₀, v₁, v₂, and they are obvious, saying things like "any two sets can be put in a pair". This chapter takes both complaints seriously. One page decodes the symbols and shows that a formula is a program that runs over a universe. Then each axiom gets a page of its own: read aloud in English, with what it builds, what goes wrong without it, and a program that checks it on a small universe of sets. A page on ordinals follows, because the owner's books go there next, and a page of katas, exercises from Jech and Cunningham with a program that checks each claim before you prove it.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [Reading a formula](reading_a_formula/README.md) | What do ∀, ∃, ⇒, ⇔, ≃, v₀ mean, and how is a formula checked on a universe? |
| 2 | [Extensionality](extensionality/README.md) | When are two sets the same set, and why is that the only axiom about equality? |
| 3 | [Pairs](pairs/README.md) | Why does {a, b} need an axiom, and how do three pairs make an ordered pair? |
| 4 | [Unions](unions/README.md) | Why does the axiom give ∪a and not a ∪ b, and why can ∩∅ not exist? |
| 5 | [Power set](power_set/README.md) | Where is ⊆ in the formula, and why is 𝒫(a) always bigger than a? |
| 6 | [Comprehension](comprehension/README.md) | Why one axiom per formula, and what does the "x ∈ a" prevent? |
| 7 | [Replacement](replacement/README.md) | What does "functional" mean, and what could Zermelo's axioms not build? |
| 8 | [Infinity](infinity/README.md) | How does a formula say "infinite", and why can no finite universe satisfy it? |
| 9 | [Choice](choice/README.md) | Why is the axiom obvious and incomprehensible at once, and what does it buy? |
| 10 | [Foundation](foundation/README.md) | Can a set be a member of itself, and why does every set have a rank? |
| 11 | [Ordinals](ordinals/README.md) | What is an ordinal, and why does a theorem about integers need them? |
| 12 | [Axiom katas](axiom_katas/README.md) | Which five moves prove every exercise, and is the claim true before I start? |

## The through-line

**An axiom is a demand, not a description.** Except for extensionality, every axiom says "there is a set whose members are …", and the chapter's programs make that literal. A universe is a collection of points with a membership relation, kept as a dictionary; the universes V₁, V₂, V₃, V₄ have 1, 2, 4 and 16 sets, each stage the power set of the one before. On such a universe every axiom can be evaluated by brute force, with ∀ as a loop that must always succeed and ∃ as a loop that must succeed once. The result is a table: V₄ satisfies extensionality, unions, comprehension and foundation, which ask for nothing above the ranks it already has, and fails pairs, power set, replacement and infinity, which each ask for a set one rank up or infinitely far up. Every False is a set the axiom demands and the universe lacks. That is what the axioms are: a list of demands on the universe, chosen so that mathematics fits inside and Russell's paradox does not.

**The obvious list is the wrong list.** The one rule that seems most obvious, "every property has a set", is Cantor's comprehension principle, and it contradicts itself in two lines. [Comprehension](comprehension/README.md) shows the contradiction as a truth table with no true row. So the axioms could not be "whatever is obvious", and each one on the list is there because something in mathematics needed it and nothing else provided it: [infinity](infinity/README.md) for ℕ, [power set](power_set/README.md) for ℝ, [replacement](replacement/README.md) for ω + ω and recursion along the ordinals, [choice](choice/README.md) for a basis of every vector space.

**Ordinals are what "it must stop" means.** The last lessons go past the axioms to the first thing built with them that other mathematics borrows: a well-ordering is an order in which every descent is finite, ordinals are the standard well-orderings, and a process whose steps are labelled by decreasing ordinals terminates. Goodstein's sequences, run by the [ordinals](ordinals/README.md) program, are the showpiece: integers that climb for 3 · 2^402653211 − 2 steps while their ordinal labels fall, and a theorem about them that Peano arithmetic cannot prove.

## Why it is useful: where the axioms reach other mathematics

The honest answer first: no physicist, engineer or working number theorist writes down the axiom of replacement. What reaches other fields is of three kinds, and each axiom's page says which.

| Axiom or idea | Where it is used outside set theory |
|---|---|
| Extensionality | Every proof that two sets are equal, by double inclusion; in algebra, equality of ideals and subgroups. In code, `==` on sets, and SQL's set semantics (`UNION`, `DISTINCT`) against its bag semantics. |
| Pairs | Ordered pairs, hence relations, functions and graphs (a graph is a set of pairs), the coordinate plane, and a database row, which is a tuple. |
| Unions | Topology, where open sets are closed under arbitrary unions; measure theory and probability, whose σ-algebras are closed under countable unions; the union of a chain in every Zorn's lemma argument. |
| Power set | Topologies and σ-algebras are subsets of 𝒫(X); the events of a probability space are subsets of the sample space Ω; the real numbers are 𝒫(ω) in disguise; Cantor's theorem is why there are uncomputable functions. |
| Comprehension | Set-builder notation in every field: solution sets, kernels, level sets, truth sets; SQL's `WHERE` and Python's comprehensions are the axiom as a language feature. |
| Replacement | Indexed families and images f[X]; transfinite recursion, which builds the Borel sets of analysis in ω₁ steps and the hierarchy V_α. |
| Infinity | ℕ, induction, and everything in analysis. |
| Choice | Every vector space has a basis; every field has an algebraic closure; every ring has a maximal ideal; Tychonoff's theorem in topology; the Hahn–Banach theorem; the existence of non-measurable sets, which is why measure theory restricts itself to σ-algebras. |
| Foundation and rank | Induction on ∈; structural recursion on data types; proofs that programs terminate. Its negation, Aczel's anti-foundation axiom, models streams and processes that contain themselves. |
| Ordinals and well-ordering | Transfinite induction; the Cantor–Bendixson analysis of closed sets of reals, the problem in Fourier series Cantor invented ordinals for; Gentzen's consistency proof of arithmetic by induction up to ε₀; termination measures in term rewriting and in proof assistants; Goodstein's theorem in number theory. |

Three places use the whole package. **Databases:** Codd's relational model is sets of tuples with first-order logic as the query language, so a relational database is a finite model of exactly the language of this chapter. **Formal methods:** the Z notation, the B method used for driverless metro lines, Lamport's TLA⁺ used at Amazon Web Services, and Jackson's Alloy are all set theory and first-order logic as engineering notations, and a model checker for them does what this chapter's programs do, on bigger universes. **Proof assistants:** Metamath's set.mm derives mathematics from the ZFC axioms written as formulas like the ones on these pages; Isabelle/ZF does the same; Lean and its Mathlib library use type theory instead, with ZFC's universe available inside it as a model. Python checks a finite universe; those tools prove theorems about all of them, and the division of labour is the right one: Python for models, a proof assistant for proofs.

## Three books, three notations

The owner reads Cori and Lascar, Cunningham, Jech and Kunen's *Foundations of Mathematics*, and each spells the same things differently. This table is the dictionary; the worst trap is in the second row.

| Idea | Cori and Lascar | Cunningham | Jech | Kunen, *Foundations* | This library |
|---|---|---|---|---|---|
| variables for sets | v₀, v₁, v₂ | x, y, A, B | x, y, X, Y | x, y, z, A, 𝓕 | a, b, x, y |
| subset, equal allowed | a ⊆ b | A ⊆ B | X ⊂ Y | x ⊆ y | a ⊆ b |
| proper subset | a ⊊ b | A ⊂ B | X ⊂ Y, X ≠ Y | x ⊊ y | a ⊊ b |
| equality in the formal language | ≃ | = | = | = | = |
| if … then, if and only if | ⇒, ⇔ | →, ↔ in formulas; ⇒, ⇔ between sentences | →, ↔ | →, ↔; ⟺ for definitions | ⇒, ⇔ |
| bounded quantifier | ∀x ∈ y F | (∀x ∈ A)P(x) | (∀x ∈ X)φ | ∀x ∈ A φ | ∀x ∈ y F |
| union of a family | ∪ₓ∈ₐ x, ∪a | ∪𝓕 | ∪X | ∪𝓕 | ∪a |
| power set | ℘(a) | 𝒫(A) | P(X) | 𝒫(x) | 𝒫(a) |
| separation / comprehension | {x ∈ a : F[x]}, "comprehension scheme" | {x ∈ A : φ(x)}, "subset axiom", "separation" | {u ∈ X : φ(u, p)}, "separation schema" | {x ∈ z : φ(x)}, "comprehension scheme" | {x ∈ a : F[x]}, "comprehension" |
| image of a set under f | f̄(c) | f(c), f[c] | f"X or f(X) | F"A or F(A) | f[a] |
| range, domain | Im(f), dom(f) | ran(f), dom(f) | ran(f), dom(f) | ran(f), dom(f) | ran, dom |
| the ordinals | On[v₀], the class of ordinals | — (later chapters) | Ord | ON | Ord |
| ordered pair | (a, b) | (a, b) | (a, b) | ⟨x, y⟩ when the Kuratowski definition matters | (a, b) |
| successor | α⁺, then α + 1 | α ∪ {α} | α + 1 | S(x) | α + 1 |
| the natural numbers | ω, ℕ = ⟨ω, 0, S, +, ×⟩ | ω | ω or **N** | ω = ℕ | ω |
| a sequence | (aᵢ)ᵢ∈I | (aᵢ)ᵢ∈I | ⟨aₙ : n < ω⟩, ⟨a_ξ : ξ < α⟩ | ⟨aₙ : n ∈ ω⟩ | (aᵢ)ᵢ∈I |
| cardinality words | subpotent, equipotent, card(x) | — | \|X\| ≤ \|Y\|, \|X\| = \|Y\| | A ≼ B, A ≈ B | injection, bijection, \|X\| |
| regularity / foundation | axiom of foundation | regularity axiom | regularity | foundation | foundation |

Three more differences are not notation but choice: Cunningham has an empty set axiom, Hrbacek and Jech an Axiom of Existence ("there exists a set which has no elements"), Kunen an Axiom 0 that some set exists, and Cori and Lascar derive ∅ from comprehension; Jech leaves choice out of ZF and Cori and Lascar bring it in as ZFC; Kunen states pairing and union in weak forms, "some set contains x and y", and recovers the exact sets by comprehension, which is Jech's exercise 1.15 on the katas page. Everything else is spelling.

## How to learn this, and what to learn first

**Learn the moves, not the theorems.** Cori and Lascar's chapter has some sixty numbered statements and the proofs use five patterns, listed on the [katas](axiom_katas/README.md) page. Name the pattern a proof uses and the proposition stops being a fact to memorise and becomes an example to recognise; that is the difference [studying vs learning](../12_Learning_to_Learn/studying_vs_learning/README.md) describes. For each proposition: state it in your own words, test it on a small case (the programs here, or ∅ and {∅} by hand), try the proof for ten minutes, read the book's proof and name its move, and redo it from the statement a week later, which is [spaced retrieval](../12_Learning_to_Learn/spaced_retrieval/README.md).

**What to know first.** A proofs course: how to read a formula with nested quantifiers (the [first lesson](reading_a_formula/README.md) and the [logic chapter](../11_Logic/README.md)), induction, and the words [injective, surjective, bijective](../04_Sets/relations_and_functions/README.md#the-three-words). Nothing else. For Cori and Lascar specifically, their Part I chapters on propositional and first-order logic, because chapter 7 speaks of models and satisfaction from its first page.

**Which chapters first, in each book.** Cunningham: chapters 1 to 4 in order, logic, the language, the axioms, then relations, functions, the natural numbers and cardinality; it is the book written for a first pass, with the English before each formula and exercises with hints. Jech: chapter 1 now, thirteen pages whose "Why axiomatic set theory?" and one-line axioms are the best summary in print, and whose exercises are on the katas page; chapters 2 and 3 after Cunningham's 5 and 6; Part II only after Kunen. Kunen's *Foundations of Mathematics*: chapter I in order, sections I.1 to I.9; it is the book that most carefully separates the formal discussion from the informal one (his Remark I.3.1), says in English what each axiom means and what it is for ("Foundation is never needed in the development of mathematics"; "most of elementary mathematics takes place within ZC⁻"), and its Exercise I.2.1, which axioms hold in seven small membership graphs, is the method of this chapter. Hrbacek and Jech: chapters 1 and 2 first if formulas put you off, since their axioms are English sentences and their "property" **P**(x) is the predicate of [the logic chapter](../11_Logic/predicates_and_quantifiers/README.md) without the symbols; the exercise of translating each of their axioms into the formula on its page here is a good one. Cori and Lascar: chapter 7 after Cunningham or Kunen, with Part I beside it. The [reading guide](../reading_guides/set_theory/README.md) places all three among the other books.

## A note on the code

Every program here keeps a universe as a Python dictionary from points to sets of members, or as `frozenset`s nested in `frozenset`s, and evaluates a formula by nested `all` and `any` over it. That is a model checker, the simplest kind, and it is exactly what a formula means: 𝒰 ⊨ F is computed, not interpreted. Python's own sets supply `==` (extensionality), `|` and `set().union(*a)` (unions), comprehensions (comprehension), `{f(x) for x in a}` (replacement) and `<=` (the subset formula inside power set); the programs use them so that each axiom can be seen as the language feature it became.

## Po polsku, w skrócie

Aksjomaty Zermela–Fraenkla to dziewięć zdań, a czytelnik ma do nich dwa zarzuty naraz: są nieczytelne, bo zapisane w języku formalnym z ∀, ∃, ⇒ i zmiennymi v₀, v₁, i są oczywiste, bo mówią rzeczy w rodzaju „dwa zbiory można włożyć do pary". Ten rozdział traktuje oba zarzuty poważnie. Pierwsza lekcja rozszyfrowuje symbole: formuła to program, który przebiega uniwersum, ∀ to pętla, która musi się udać zawsze, ∃ pętla, która musi się udać raz. Potem każdy aksjomat ma własną stronę: odczytany po angielsku, z tym, co buduje, z tym, co się psuje bez niego, i z programem, który sprawdza go na małym uniwersum V₄ szesnastu zbiorów. Tabela wyników to teza rozdziału: aksjomat jest żądaniem, nie opisem; każde False to zbiór, którego aksjomat żąda, a uniwersum nie ma. Lista „oczywistych" reguł jest sprzeczna (paradoks Russella), więc każdy aksjomat na liście jest tam dlatego, że matematyka go potrzebowała. Lekcja o liczbach porządkowych pokazuje, po co to komu: ciągi Goodsteina to twierdzenie o liczbach naturalnych, którego jedyny znany dowód idzie przez liczby porządkowe. Strona kata zbiera zadania z Jecha i Cunninghama, a tabela notacji tłumaczy między trzema książkami (uwaga: ⊂ u Jecha to „zawiera się lub równa", u Cunninghama „zawiera się właściwie"). Jak się tego uczyć: nie twierdzeń, lecz pięciu ruchów dowodowych; najpierw Cunningham rozdziały 1–4, rozdział 1 Jecha, a Cori i Lascar potem.

## See also

- [04_Sets](../04_Sets/README.md) — the language of sets, which this chapter puts on axioms
- [11_Logic](../11_Logic/README.md) — if–then, and the propositional laws the formulas obey
- [Set theory: a reading guide](../reading_guides/set_theory/README.md) — the books, in order, and the founding papers
- René Cori and Daniel Lascar, *Mathematical Logic: A Course with Exercises*, Part II (Oxford, 2001), chapter 7; Daniel W. Cunningham, *Set Theory: A First Course* (Cambridge, 2016), chapter 1; Thomas Jech, *Set Theory*, third millennium edition (Springer, 2003), chapters 1 and 2; Kenneth Kunen, *The Foundations of Mathematics* (College Publications, 2009), chapter I: the four books these pages read
