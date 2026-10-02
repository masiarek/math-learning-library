# Reading a formula: ∀ is a loop, ∃ is a search

**Level:** 201 · for anyone opening an axiomatic set theory book, Cori and Lascar's chapter 7 or any other, and stopping at the first ∀v₀∀v₁

**One line:** A formula of set theory is a program that runs over the universe: ∀ is a loop that must succeed every time, ∃ a loop that must succeed once, ⇒ is "not p or q" and ∈ is a lookup; read that way each axiom is a sentence of plain English, and a small universe shows which sentences it makes true.

## The symbols

Cori and Lascar write every axiom in a formal language with two relation symbols, ≃ for equality and ∈ for membership, variables v₀, v₁, v₂, …, and the connectives and quantifiers of first-order logic. Here is the whole alphabet, with how to say each symbol and what it becomes in Python when a formula is checked by brute force.

| Symbol | Name | Read aloud | Python |
|---|---|---|---|
| ∀v F | universal quantifier | for every v, F | `all(F(v) for v in U)` |
| ∃v F | existential quantifier | there is a v such that F | `any(F(v) for v in U)` |
| F ∧ G | conjunction | F and G | `F and G` |
| F ∨ G | disjunction | F or G, or both | `F or G` |
| ¬F | negation | not F | `not F` |
| F ⇒ G | implication | if F then G | `(not F) or G` |
| F ⇔ G | equivalence | F exactly when G | `F == G` |
| x ≃ y | equality | x and y are the same set | `x == y` |
| x ∈ y | membership | x is a member of y | `x in U[y]` |
| x ∉ y | abbreviation for ¬ x ∈ y | x is not a member of y | `x not in U[y]` |
| ∀x ∈ y F | abbreviation for ∀x (x ∈ y ⇒ F) | for every member x of y, F | `all(F(x) for x in U[y])` |
| ∃x ∈ y F | abbreviation for ∃x (x ∈ y ∧ F) | some member x of y has F | `any(F(x) for x in U[y])` |

Three things about this table trip up most readers.

**The inverted A and the mirrored E.** ∀ is an upside-down A for *All* and ∃ a backwards E for *Exists*. Giuseppe Peano introduced ∃ in 1897 and Gerhard Gentzen ∀ in 1935; before that Russell and Whitehead wrote (x) for "for all x" and (∃x) for "there is an x". (Those dates are from memory.) They are not two kinds of variable but two kinds of loop: ∀x says "the inner sentence must hold for every x the loop visits", ∃x says "it must hold for at least one".

**The order of the loops matters.** ∀x ∃y (y is x's mother) says everyone has a mother. ∃y ∀x (y is x's mother) says one person is everyone's mother. The second quantifier runs inside the first, as in nested `for` loops, and swapping them changes the claim. The axiom of pairs, ∀v₀ ∀v₁ ∃v₂ …, says: whichever two sets the outer loops pick, the search for v₂ succeeds. If it were ∃v₂ ∀v₀ ∀v₁ … it would claim one set that is the pair of everything, which is false.

**v₀, v₁, v₂ are just names.** The book numbers its variables because the formal language needs infinitely many and letters run out. Read v₀ as a, v₁ as b, v₂ as c, and every formula gets shorter. The book's ≃ is its equals sign in the formal language; it reserves = for the language it writes the book in.

## The universe, and the word "set"

Everything in the chapter happens inside a **universe**: Cori and Lascar's 𝒰 is a model of the axioms, and U its set of points. In the formal language the word *set* means a point of U and nothing else, and x ∈ y means "the universe's membership relation holds between the points x and y". A formula is true or false in 𝒰, written 𝒰 ⊨ F, and that is the only kind of truth the chapter talks about.

This is the same word as the **universal set** of [the algebra of sets](../../04_Sets/algebra_of_sets/README.md), and nearly the same idea: the collection everything under discussion is drawn from. The difference is who is looking. In a Venn diagram, U is a set like any other and you may take its complement. Here, U is seen from outside, by whoever is reading the book, and from inside the theory it is not a set at all: the book forbids itself from saying "the set U", because the theory proves there is no set of all sets. The two levels of language, the formal one and the one the proofs are written in, are the reason for the chapter's slow first page.

What makes this concrete is that a universe can be small. The program keeps one as a Python dictionary: each point maps to the set of its members. V₃ has four points, ∅, {∅}, {{∅}}, {∅, {∅}}, and V₄ has sixteen, every set whose members are those four. On such a universe a formula is checked by running the loops.

## Reading an axiom aloud

Three steps turn any axiom into a sentence.

1. **Peel the quantifiers from the outside in** and give each variable a letter: ∀v₀ ∀v₁ ∃v₂ ∀v₃ becomes "for every a and b there is a c such that for every d".
2. **Translate the inner formula as a claim about membership.** v₃ ∈ v₂ ⇔ (v₃ ≃ v₀ ∨ v₃ ≃ v₁) is "d is in c exactly when d is a or d is b".
3. **Say what set the sentence is about.** "A set c whose members are exactly a and b": the pair {a, b}.

So the axiom of pairs reads: *for any two sets there is a set whose members are exactly those two.* Extensionality reads: *if every set is a member of a exactly when it is a member of b, then a and b are the same set.* Every axiom in this chapter is read this way on its own page, and almost every one has the same shape: a ∀ for the sets you start from, an ∃ for the set the axiom promises, and a ∀ … ⇔ … that says who its members are. Cori and Lascar say it in one line: except for extensionality, every axiom declares that a certain class is a set.

## Why the axioms feel silly and obvious at the same time

They feel obvious because they say what everyone does anyway: of course two sets can be put in a pair, of course the members of members form a set. They feel silly because it seems absurd to write down that {a, b} exists. Three facts resolve the feeling.

- **The obvious list is inconsistent.** The most obvious rule of all, "every property has a set of the things with that property", is what Cori and Lascar call the unrestricted comprehension scheme, and page 113 shows it contradicts itself (Russell's paradox; [what is a set?](../../04_Sets/what_is_a_set/README.md) runs it). So the list cannot be "whatever is obvious". It is, in the book's words, a compromise: enough to build mathematics, not enough to build a contradiction, and every axiom on it had to earn its place.
- **Each axiom is a claim that the universe is big enough**, and a small universe refutes it. Section 4 of the program checks every axiom on V₂, V₃ and V₄. Pairs fails in each, because the pair of two sets from the top rank has one rank more; power set fails for the same reason; infinity fails in every finite universe. The axioms are not descriptions of what sets are like. They are demands for sets, and a universe passes only if it has them.
- **They are what a machine can check.** A proof assistant such as Lean, or the Metamath database of set theory, starts from exactly these formulas and nothing else, and every theorem of mathematics it verifies is derived from them. The axioms are silly in the way the rules of chess are silly: nobody plays for the rules, and nothing can be played without them.

## What the program prints

<!-- output:reading_a_formula -->
*Verified output of [`reading_a_formula.py`](examples/reading_a_formula.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. A UNIVERSE IS POINTS AND A MEMBERSHIP RELATION, NOTHING ELSE
   V_1:  1 points: ∅
   V_2:  2 points: ∅, {∅}
   V_3:  4 points: ∅, {∅}, {{∅}}, {∅, {∅}}
   V_4: 16 points: ∅, {∅}, {{∅}}, {∅, {∅}}, ... (every set of sets of sets of ∅)
   x ∈ y is looked up in a table: in V_3, ∅ ∈ {∅}? True   {∅} ∈ ∅? False

2. THE TRANSLATION TABLE
   formula     read aloud                                           Python
   ∀v F        for every point v of the universe, F                 all(F(v) for v in U)
   ∃v F        for at least one point v, F                          any(F(v) for v in U)
   F ∧ G       F and G                                              F and G
   F ∨ G       F or G, or both                                      F or G
   ¬F          not F                                                not F
   F ⇒ G       if F then G: forbidden only when F true, G false     (not F) or G
   F ⇔ G       F and G have the same truth value                    F == G
   x ≃ y       x and y are the same point                           x == y
   x ∈ y       x is a member of y                                   x in U[y]
   x ∉ y       x is not a member of y                               x not in U[y]
   ∀x ∈ y F    for every member x of y, F                           all(F(x) for x in U[y])
   ∃x ∈ y F    for some member x of y, F                            any(F(x) for x in U[y])

3. TWO AXIOMS READ ALOUD, THEN EVALUATED
   Extensionality:  ∀v0 ∀v1 (∀v2 (v2 ∈ v0 ⇔ v2 ∈ v1) ⇒ v0 ≃ v1)
     for every v0, for every v1: if every v2 is in v0 exactly when it is
     in v1, then v0 and v1 are the same point. Two sets with the same
     members are equal.
     all((not all((z in U[x]) == (z in U[y]) for z in U)) or x == y
         for x in U for y in U)
   Pairs:  ∀v0 ∀v1 ∃v2 ∀v3 (v3 ∈ v2 ⇔ (v3 ≃ v0 ∨ v3 ≃ v1))
     for every v0 and v1 there is a v2 such that a point is in v2
     exactly when it is v0 or v1. The pair {v0, v1} exists.
     all(any(all((w in U[z]) == (w == x or w == y) for w in U) for z in U)
         for x in U for y in U)
   in V_2:  extensionality True   pairs False
   in V_3:  extensionality True   pairs False
   in V_4:  extensionality True   pairs False
   Pairs fails in every V_n: the pair of two sets from the top rank
   has a rank one higher, and that rank is not in the universe.

4. EVERY AXIOM ON FOUR UNIVERSES: TRUE MEANS 'THE UNIVERSE HAS WHAT IT ASKS FOR'
   U(atoms) is {a, b, c} with a and b memberless and c = {a}: two 'empty sets'.
   axiom                                    V_2       V_3       V_4  U(atoms)
   extensionality                          True      True      True     False
   pairs                                  False     False     False     False
   unions                                  True      True      True      True
   power set                              False     False     False     False
   comprehension, F = 'v is empty'         True      True      True      True
   replacement, F = 'w ↦ {w}'             False     False     False     False
   infinity                               False     False     False     False
   foundation                              True      True      True      True
   choice                                  True      True      True      True
   Each False is a set the axiom demands and the universe lacks: a pair,
   a power set, an image, an infinite set. Infinity fails in every finite
   universe, which is why it is an axiom and not a theorem.
```
<!-- /output -->

Section 2 is the table above, section 3 reads two axioms aloud and evaluates them, and section 4 is the chapter in one table. Read its columns downward: V₂, V₃ and V₄ each satisfy extensionality, unions, comprehension and foundation, which ask for nothing above the ranks already present, and each fails pairs, power set, replacement and infinity, which ask for a set one rank up. The fourth universe has three points, two of them with no members, and it fails extensionality alone: two different sets with the same (no) members. Each later page of this chapter takes one row of this table and asks what the axiom builds, why it is needed, and which universe lacks it.

## Po polsku, w skrócie

Formuła teorii mnogości to program, który przebiega uniwersum: ∀ (odwrócone A, od *All*) to pętla, która musi się udać za każdym razem, ∃ (odwrócone E, od *Exists*) to pętla, która musi się udać choć raz, ⇒ to „nie p lub q", ⇔ to równość wartości logicznych, a x ∈ y to sprawdzenie w tablicy należenia. Zmienne v₀, v₁, v₂ to tylko nazwy; czytając v₀ jako a, v₁ jako b, każdy aksjomat staje się zdaniem po polsku. Kolejność kwantyfikatorów ma znaczenie: ∀x∃y to „każdy ma matkę", ∃y∀x to „ktoś jest matką wszystkich". Uniwersum 𝒰 w książce Coriego i Lascara to model aksjomatów oglądany z zewnątrz; w środku „zbiór" znaczy punkt tego modelu, a zbioru wszystkich punktów nie ma. Aksjomaty wydają się zarazem oczywiste i niepoważne, bo mówią to, co i tak każdy robi; ale „oczywista" lista jest sprzeczna (paradoks Russella), a każdy aksjomat to żądanie, by uniwersum było dość duże: program sprawdza wszystkie aksjomaty na małych uniwersach V₂, V₃, V₄ i pokazuje, który z nich żąda zbioru, którego tam nie ma.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 13_Axioms_of_Set_Theory/reading_a_formula/examples/reading_a_formula.py
```

## See also

- [Extensionality](../extensionality/README.md) — the next page: the first axiom, read aloud and checked
- [If A then B: converse, contrapositive and inverse](../../11_Logic/converse_and_contrapositive/README.md) — the ⇒ of every axiom, and why it is forbidden only when the hypothesis is true and the conclusion false
- [The algebra of sets](../../04_Sets/algebra_of_sets/README.md) — ∪ ∩ ′ as or, and, not, and the universal set U of one problem
- [What is a set?](../../04_Sets/what_is_a_set/README.md) — Russell's paradox, the reason the obvious list is not the list
- [Set theory: a reading guide](../../reading_guides/set_theory/README.md) — where Cori and Lascar sits among the books
- [First-order logic ↗](https://en.wikipedia.org/wiki/First-order_logic) — Wikipedia
