# Lean: a reading guide

**Level:** reference · for anyone who has heard "we need Lean", wants to know what Lean is, which of its free books to open first, and what its two founding definitions, a proof is a program and a set is a predicate, mean in practice

**One line:** Lean is one system wearing two coats, a proof assistant and a programming language, because in its dependent type theory a proposition is a type and a proof is a program of that type; *Functional Programming in Lean* teaches the language coat and says so, *Mathematics in Lean* teaches the proof coat, and the program on this page runs the two definitions that join them.

This page is a reading guide, not a lesson. What it says about Lean's definitions is read from Lean's own source files; what it says about the books is read from the source of *Functional Programming in Lean* and, for the others, from memory, marked as such. The program is a working model of Lean's type checker for the propositional connectives and of Mathlib's sets, backed like every program here by recorded output.

**What was read and what was not.** Lean's own site, lean-lang.org, is blocked from this session, as are its books' web pages. Their sources are not: the book's repository [leanprover/fp-lean ↗](https://github.com/leanprover/fp-lean) (the link the owner sent; yes, it is the right one, the whole book is in it under `book/FPLean/`), Lean's core `Init/Prelude.lean` and Mathlib's `Mathlib/Data/Set/Defs.lean` were read in full where quoted. The Lean FRO roadmap page the owner sent, `lean-lang.org/fro/roadmap/y4-1/`, could not be read; the paragraph on the FRO below says what is known without it.

## Contents

- [What Lean is](#what-lean-is)
- [The two definitions, run](#the-two-definitions-run)
- [The books](#the-books)
- [Lean beside this library](#lean-beside-this-library)
- [The Lean FRO, and Lean Beam](#the-lean-fro-and-lean-beam)
- [Where to start](#where-to-start)
- [How sure](#how-sure)

## What Lean is

The book's own first paragraph says it exactly: "Lean is an interactive theorem prover based on dependent type theory. Originally developed at Microsoft Research, development now takes place at the Lean FRO. Dependent type theory unites the worlds of programs and proofs; thus, Lean is also a programming language." As a language it is, in the book's four words, *strict*, *pure*, *functional* and *dependently typed*: arguments are evaluated before a call, a function cannot have a side effect its type does not declare, functions are values, and types can contain programs and programs can compute types. Lean is written in Lean.

The foundation matters for this library because it is not the one the [axioms of set theory](../../13_Axioms_of_Set_Theory/README.md) chapter uses. ZFC has one kind of thing, sets, and one relation, ∈; Lean has types, and every term has exactly one. A "set" in Lean is a predicate on a type, below, and ZFC's universe is something Mathlib builds inside Lean as one type among others (`ZFSet`). The [set theory guide](../set_theory/README.md) calls type theory "the rival foundation" for that reason; the [proof assistants guide](../proof_assistants/README.md) compares Lean with Isabelle, whose ZF object logic keeps the books' untyped sets.

## The two definitions, run

Everything a Lean user does rests on two lines, and both are short enough to quote. From `Init/Prelude.lean`, the core library that every Lean file imports:

```lean
structure And (a b : Prop) : Prop where
  intro ::
  left : a
  right : b

inductive Or (a b : Prop) : Prop where
  | inl (h : a) : Or a b
  | inr (h : b) : Or a b

inductive False : Prop

def Not (a : Prop) : Prop := a → False
```

A conjunction is a *structure with two fields*: a pair. A disjunction is an *inductive type with two constructors*: a tagged value. `False` is a type with *no constructors*, so nothing can have it as its type. And ¬a is not a primitive at all; it is the function type from a to False. These are the same words a programmer uses for pairs, enums, the empty type and functions, because they are the same things: *Functional Programming in Lean* puts it as "In Lean, propositions are in fact types. They specify what counts as evidence that the statement is true." A proof of A ∧ B → B ∧ A is a function that takes a pair and returns the swapped pair, and Lean accepts it because that function has that type.

The second line is Mathlib's, from `Mathlib/Data/Set/Defs.lean`:

```lean
def Set (α : Type u) := α → Prop

protected def Mem (s : Set α) (a : α) : Prop := s a
```

A set of elements of type α is a function from α to propositions, and a ∈ s *is* the application s a. Union is ∨ on the two predicates, intersection ∧, complement →False, and two sets are equal when their predicates agree on every element (`Set.ext`), which is [extensionality](../../13_Axioms_of_Set_Theory/extensionality/README.md) in its typed form. The docstring adds that this is "an implementation detail which should not be relied on", meaning Mathlib wants its users to go through `∈` and the lemmas, but the definition is what makes those lemmas true.

The program is a small type checker for the first definition and a four-element model of the second.

<!-- output:propositions_as_types -->
*Verified output of [`propositions_as_types.py`](examples/propositions_as_types.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. THREE THEOREMS WRITTEN AS PROGRAMS, THEN TYPE-CHECKED
   Lean: a proposition is a type, a proof is a term of that type.
   theorem and_swap : ((A ∧ B) → (B ∧ A))
     fun h => ⟨h.right, h.left⟩
   and_swap: accepted  the term has type ((A ∧ B) → (B ∧ A))
   theorem const : (A → (B → A))
     fun a => fun b => a
   const: accepted  the term has type (A → (B → A))
   theorem de_morgan : (¬(A ∨ B) → (¬A ∧ ¬B))
     fun h => ⟨fun a => h (Or.inl a), fun b => h (Or.inr b)⟩
   de_morgan: accepted  the term has type (¬(A ∨ B) → (¬A ∧ ¬B))
   ¬A is the function type A → False, so a proof of ¬A is a function
   that would turn any proof of A into a proof of False.

2. THE PROOF OF A ∧ B → B ∧ A, RUN AS THE PROGRAM IT IS
   and_swap applied to (1, 'one') gives ('one', 1)
   and_swap applied to ('x', 'y') gives ('y', 'x')
   And.intro builds a pair, And.left and And.right take it apart:
   the proof is the swap function. Lean erases such programs at
   run time (Prop is proof-irrelevant), but the type checker ran them.

3. TWO WRONG PROOFS, REJECTED AT THE STEP THAT IS WRONG
   fun h => ⟨h.left, h.left⟩  offered for A ∧ B → B ∧ A
   wrong1: REJECTED  the term has type ((A ∧ B) → (A ∧ A))
   fun h => h.left  offered for A ∨ B → A
   wrong2: REJECTED  (And.left needs a conjunction, got (A ∨ B))
   The first is a well-typed program that proves the wrong theorem;
   the second is not a program at all. Lean reports both as type errors.

4. WHY False HAS NO PROOF
   False is an inductive type with no constructors, so no closed term
   has type False; the checker above can only reach False by applying
   a hypothesis of type ¬A to a proof of A. The one rule about False,
   False.elim, says a proof of it would prove anything:
   ex_falso: accepted  the term has type (False → C)

5. A SET IS A PREDICATE: Mathlib's  def Set (α : Type u) := α → Prop
   α = {a, b, c, d}   s = {a, b}   t = {b, c}
   b ∈ s is the application s b = True;  d ∈ s is s d = False
   s ∪ t = {a, b, c}  (x ∈ s ∨ x ∈ t)
   s ∩ t = {b}      (x ∈ s ∧ x ∈ t)
   sᶜ    = {c, d}  (x ∈ s → False)
   Laws checked by Set.ext, that is by ∀ x, x ∈ lhs ↔ x ∈ rhs:
     (s ∪ t)ᶜ = sᶜ ∩ tᶜ           True
     (s ∩ t)ᶜ = sᶜ ∪ tᶜ           True
     s ∩ (s ∪ t) = s              True
     (sᶜ)ᶜ = s                    True
     s ∪ t = s ∩ t  (false)       False
   Each law is a law of logic read through the arrow: De Morgan for sets
   is De Morgan for ∨ and ∧, which section 1 proved as a program.
```
<!-- /output -->

Three things to take from the output. Section 2 is the one that makes the slogan concrete: the accepted proof of A ∧ B → B ∧ A, handed a Python pair, swaps it. Section 3 shows the two ways a proof fails in Lean, and that both are type errors: a correct program for the wrong theorem, and a term that is not a program. Section 5 is what the [algebra of sets](../../04_Sets/algebra_of_sets/README.md) lesson checks by brute force over subsets, done the way Mathlib would prove it, by extensionality over the elements of the type, and it shows why: De Morgan for sets is De Morgan for ∨ and ∧, read through the arrow. The checker is a model of Lean's kernel, not Lean: it has no dependent types, no universes, no equality, no quantifiers and no tactics, which is most of Lean.

## The books

All free, all online, and all by people inside the project.

| Book | What it teaches | Who it is for | Read from |
|---|---|---|---|
| ***Functional Programming in Lean*** (David Thrane Christiansen; Microsoft 2023, now Lean FRO; CC BY 4.0) | Lean as a programming language: twelve chapters, *Getting to Know Lean*, *Hello, World!*, an interlude *Propositions, Proofs, and Indexing*, *Overloading and Type Classes*, *Monads*, *Functors, Applicative Functors, and Monads*, *Monad Transformers*, *Programming with Dependent Types*, an interlude *Tactics, Induction, and Proofs*, *Programming, Proving, and Performance*, *Next Steps* | "programmers who want to learn Lean, but who have not necessarily used a functional programming language before"; loops, functions and data structures assumed; explicitly "not a good first book on programming in general"; also for mathematicians who will write proof automation | the source: the book is written in Lean's own documentation tool, Verso, every example type-checked against the Lean version the book pins (4.33 at the time of reading); release history runs from June 2022 to October 2025, the last update for Lean 4.23 adding functional induction and `grind` |
| ***Theorem Proving in Lean 4*** (Avigad, de Moura, Kong, Ullrich and others) | Lean as a proof assistant from the type theory up: dependent types, propositions as types, quantifiers, tactics, inductive types, structures, type classes, axioms | someone who wants to understand *why* a proof checks, with a logic or CS background | memory; it is the reference the FP book sends readers to for the proof side |
| ***Mathematics in Lean*** (Avigad and Massot) | Mathlib: sets, functions, relations, number theory, algebra, topology and analysis done in Lean, with exercises in a downloadable project | a mathematician or student who knows the mathematics and wants it formal; the fastest route to proving things about [sets](../../04_Sets/README.md) | memory; chapter 4, *Sets and Functions*, covers what [04_Sets](../../04_Sets/README.md) covers, in Lean |
| ***The Natural Number Game*** (Buzzard and others, in the browser) | induction and rewriting on ℕ as a game with Lean's real tactics, no installation | the first hour of anyone, before any book | memory; already the first step in the [proof assistants guide](../proof_assistants/README.md#where-to-start) |
| ***The Little Typer*** (Friedman and Christiansen, MIT Press, not free) | the ideas of dependent type theory in a tiny language, in dialogue form | someone who wants the theory before the tool; the FP book's author wrote it | memory |

**Which first.** It depends on which coat you want. To *compute* with Lean, *Functional Programming in Lean* from chapter 1, in order, as its introduction asks ("intended to be read linearly"), doing the exercises; its two interludes are the smallest honest account of propositions as types in print. To *prove* with Lean, the Natural Number Game for an hour, then *Mathematics in Lean* with *Theorem Proving in Lean 4* open beside it for the why. The FP book's own advice to mathematicians is the surprising one: they will end up writing proof automation, which is programming, and "most working mathematicians are trained in languages like Python and Mathematica", so the programming book is for them too.

## Lean beside this library

The pattern of this library is to build a finite model and look; Lean's is to write the proof and have it checked. The two are not rivals. Every page here that ends in a table of `True` is a claim Lean could prove for all cases, and the [proof assistants guide](../proof_assistants/README.md) does one such pair, 𝒫(A ∩ B) = 𝒫(A) ∩ 𝒫(B) checked on 64 pairs of sets here and proved in Isabelle there. What Lean adds is the conviction that there is no 65th pair; what Python adds is that you can see the pair.

Where the two meet on this library's own pages:

| Here | In Lean |
|---|---|
| [What a proof is](../../11_Logic/what_a_proof_is/README.md): a chain of lines, each with its reason | a term whose type is the theorem; the reasons are the constructors and the function applications |
| [Truth tables and the laws of logic](../../11_Logic/truth_tables_and_laws/README.md): a law is two columns that agree | a law is a term of type (P ↔ Q); Lean's `decide` tactic builds the truth table for you on decidable propositions |
| [Predicates and quantifiers](../../11_Logic/predicates_and_quantifiers/README.md): ∀ is a loop, ∃ a search | ∀ x, P x is a dependent function type, a proof is a function from x to a proof of P x; ∃ is a pair of a witness and a proof |
| [Induction](../../11_Logic/induction/README.md): a base case and a step | `Nat.rec`, the recursor of the inductive type ℕ; `induction n with` in a tactic proof |
| [The algebra of sets](../../04_Sets/algebra_of_sets/README.md): laws checked over all subsets of a small U | `Set.ext fun x => by simp [...]`, or `Finset` with `decide` for a finite type, as section 5 above |
| [Reading a set expression](../../04_Sets/reading_set_expressions/README.md): where ∖ sits | Lean puts `\` level with `∩`, left-associative, as that page records from Lean's source |
| [Extensionality](../../13_Axioms_of_Set_Theory/extensionality/README.md) | `Set.ext` for typed sets; for ZFC inside Lean, Mathlib's `ZFSet.ext` |
| [Orderings](../../04_Sets/orderings/README.md): six properties, four names | type classes `Preorder`, `PartialOrder`, `LinearOrder`, with the properties as fields |

## The Lean FRO, and Lean Beam

Lean's development moved in 2023 from Microsoft Research to the **Lean Focused Research Organization**, a non-profit led by Leonardo de Moura, Lean's creator, and funded by philanthropic grants (the Simons Foundation, the Alfred P. Sloan Foundation and Richard Merkin are the names in its announcement; from memory). It publishes a yearly roadmap; the owner's link names year 4, which would be 2026 to 2027, and the page could not be read from here, so nothing on it is reported. The first three roadmaps, from memory, were about scalability (compiling Mathlib faster), usability (the language server and error messages), documentation (the Verso tool the FP book is now written in, and a reference manual) and proof automation.

**Lean Beam** ([leanprover/lean-beam ↗](https://github.com/leanprover/lean-beam), read from its README) is the piece of that work the owner's third link points at: a preview project, released as a separate install, for "efficient interaction with Lean from AI agents and other tools". It adds extensions to Lean's language server and a small broker that exposes them as a command line, `lean-beam`, and as an MCP server, so that an agent can ask "would this tactic work at this position?" in a saved file without editing it or rebuilding the project. The README names the use it has found: proof repair, proof search, translating and porting proofs, autoformalization and ordinary AI-assisted Lean editing, and says the interface may still change. It ships agent instruction files (`AGENTS.md`, `CLAUDE.md`, a `skills/` folder for Lean and for Rocq) and pins Lean 4.33. For this library the relevance is direct: it is the tooling that would let a session like this one check a Lean proof of a page's claim instead of a Python model of it, once the owner has Lean installed, which the [proof assistants guide](../proof_assistants/README.md) has not assumed so far.

## Where to start

1. The program on this page: write a fourth theorem as a term, A → ¬¬A is a good one (`fun a => fun na => na a`), and run `check` on it; then hand `wrong1` a different wrong pair and read the type it gets.
2. The *Natural Number Game*, in the browser.
3. *Functional Programming in Lean*, chapters 1 and 2, then the interlude on propositions, proofs and indexing, which is where sections 1 to 4 of the program come from.
4. *Mathematics in Lean*, chapter 4, with [04_Sets](../../04_Sets/README.md) beside it, to see the pages of this library proved rather than checked.
5. Then the rest of the FP book if you program, *Theorem Proving in Lean 4* if you want the foundations.

## How sure

| Claim | How sure | Why |
|---|---|---|
| What Lean is, who the FP book is for, its chapters, release history and licence | high | read from `book/FPLean/Intro.lean` and `book/FPLean.lean` in the book's repository |
| The definitions of And, Or, False, Not and Set, and the Set docstring | high | read from `Init/Prelude.lean` and `Mathlib/Data/Set/Defs.lean`; the quotations are the source lines, comments dropped |
| What Lean Beam is and does | high | read from its README |
| The other books: authors, content, which chapter covers sets | medium | from memory; titles and authors are stable, chapter numbers may have moved |
| The Lean FRO's founding, funders and roadmap themes | medium to low | from memory of its 2023 announcement and earlier roadmaps; the year-4 roadmap was not read |
| The model checker's behaviour matching Lean's on the connectives | high for what it covers | the terms it accepts are Lean terms with the same constructor names; it covers no quantifiers, equality or universes |

## Po polsku, w skrócie

Lean to jeden system w dwóch płaszczach: asystent dowodzenia i język programowania, bo w jego teorii typów zależnych zdanie jest typem, a dowód jest programem tego typu. Dwie krótkie definicje mówią wszystko: koniunkcja `And` to struktura z dwoma polami (para), alternatywa `Or` to typ z dwoma konstruktorami, `False` nie ma konstruktorów wcale, a negacja to funkcja w `False`. Mathlib definiuje zbiór jako predykat, `Set α := α → Prop`, więc „a ∈ s” to po prostu zastosowanie s a. Program na tej stronie jest małym sprawdzaczem typów dla tych definicji: dowód A ∧ B → B ∧ A okazuje się funkcją zamieniającą miejscami elementy pary, a dwa błędne dowody odpadają jako błędy typów. Książka *Functional Programming in Lean* uczy płaszcza programisty i jest przeznaczona dla programistów bez doświadczenia z językami funkcyjnymi; *Mathematics in Lean* uczy płaszcza matematyka. Strona FRO i jej plan na rok czwarty są z tej sesji niedostępne; Lean Beam, trzeci link, to narzędzie pozwalające agentom AI pytać Leana „czy ta taktyka zadziała tutaj?” bez edytowania pliku.

## Auf Deutsch: Stichwörter

Lean ist Beweisassistent und Programmiersprache zugleich, weil in seiner abhängigen Typentheorie ein Satz ein Typ und ein Beweis ein Programm dieses Typs ist; das Programm der Seite prüft drei Beweise als Terme und modelliert Mathlibs Mengen als Prädikate.

**Stichwörter:** Lean 4, abhängige Typen (dependent types), Sätze als Typen (propositions as types), Beweisterm, Konstruktor, induktiver Typ, Strukturtyp, Typklasse, Taktik, Mathlib, Menge als Prädikat, Extensionalität, Lean FRO, Verso, Lean Beam, MCP-Server.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 reading_guides/lean/examples/propositions_as_types.py
```

## See also

- [Proof assistants: a reading guide](../proof_assistants/README.md), a natural deduction checker with Isabelle's rule names, the ZF axioms as Isabelle/ZF states them, and Python, Rust, Lean and Isabelle compared for sets.
- [Set theory: a reading guide](../set_theory/README.md#tools-languages-proof-assistants-model-finders), the tools table, where Lean sits among Alloy, TLA⁺, Metamath and Mizar.
- [Truth tables and the laws of logic](../../11_Logic/truth_tables_and_laws/README.md) and [what a proof is](../../11_Logic/what_a_proof_is/README.md), the two pages the program's sections 1 to 4 rest on.
- [The algebra of sets](../../04_Sets/algebra_of_sets/README.md), the laws section 5 proves by extensionality.
- [Functional Programming in Lean, source ↗](https://github.com/leanprover/fp-lean) and [Lean Beam ↗](https://github.com/leanprover/lean-beam), the two repositories read for this page.
