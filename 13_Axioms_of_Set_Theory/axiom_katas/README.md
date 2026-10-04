# Axiom katas: the first exercises of Jech and Cunningham, checked before you prove them

**Level:** 201 · for anyone who has read the axioms and wants exercises, with a way to know the claim is true before spending an evening on its proof

**One line:** A kata is a short exercise repeated until the move is automatic, and the moves of axiomatic set theory are few: double inclusion, "exists by an axiom, unique by extensionality", the least element, induction, and the diagonal; the twenty-two exercises here, from Jech's chapter 1 and Cunningham's chapter 1, are each checked on a small universe, so a False means you misread the formula, and a True means the proof exists and is yours to find.

## How to use the page

Pick a kata, read it aloud as [reading a formula](../reading_a_formula/README.md) does, write the claim in your own words, and try the proof for ten minutes before reading anything. Then run the program: it evaluates the claim on every set of a small universe, V₃ or V₄ or the von Neumann numbers up to 6, and prints True or False. A True is not a proof, because V₄ is one universe and the proof must work in all of them, but it tells you the sentence you wrote is the sentence the book meant. A False means a wrong reading: in the list below one kata is a sentence that is false in ZF too, and the program says so.

Every proof here uses one of five moves. Name the move before you start, and the exercise is half done.

| Move | What it looks like | Katas that use it |
|---|---|---|
| **[Double inclusion](../extensionality/README.md#what-it-is-for)** | to show a = b, show a ⊆ b and b ⊆ a | Jech 1.3, 1.14, 1.15; Cunningham 1.5.6, 1.5.7 |
| **[Exists by an axiom, unique by extensionality](../extensionality/README.md#what-it-is-for)** | name the axiom, write the formula, say "unique" | Cunningham 1.5.1, 1.5.2, 1.5.6, 1.5.7 |
| **[Least element](../../11_Logic/induction/README.md#why-it-works-the-least-counterexample)** | take the least counterexample, or the ∈-minimal member foundation gives, and contradict it | Jech 1.7; Cunningham 1.5.3, 1.5.4, 1.5.5 |
| **[Induction](../../11_Logic/induction/README.md)** | show a set is inductive, so it contains ℕ | Jech 1.3, 1.5, 1.8, 1.10 |
| **[Diagonal and counting](../../04_Sets/cardinality/README.md)** | a set that differs from every candidate, or 2ⁿ > n | Jech 1.2; Cunningham 1.5.8 |
| **[Check the model](../reading_a_formula/README.md)** | evaluate the formula on a small universe, as the programs do | Kunen I.2.1, I.6.3, I.6.11, I.6.13 |

## The katas

From Jech, *Set Theory*, chapter 1, exercises 1.1 to 1.15, Cunningham, *Set Theory: A First Course*, exercises 1.4 and 1.5, and Kunen, *The Foundations of Mathematics*, Exercise I.2.1. The numbering is the books'.

- **Kunen I.2.1.** Seven small universes drawn as directed graphs, an arrow from x to y meaning x ∈ y: which of extensionality, foundation, pairing and union hold in each? Kunen's hint is to picture the children of each node, and his answer for pairing is "true in #2 and false in the rest". The program evaluates all four axioms on all seven, and the table it prints is the method of this whole chapter in one exercise: an axiom is checked on a universe, not believed. Then try his I.6.3, I.6.11 and I.6.13, which ask for the graph among the seven that satisfies some axioms and not others.

- **Jech 1.1.** (a, b) = (c, d) if and only if a = c and b = d, for Kuratowski's pair {{a}, {a, b}}. Two cases, a = b and a ≠ b; Cori and Lascar's Proposition 7.4 is a model answer.
- **Jech 1.2.** There is no set X with 𝒫(X) ⊆ X. Hint: Cantor. (Jech writes ⊂ for subset-or-equal; see the chapter page for his notation.)
- **Jech 1.3, 1.5, 1.8.** Facts about ℕ as the least inductive set: each n is transitive and equals {m : m < n}; n ∉ n and n ≠ n + 1; every n ≠ 0 is a successor. Each is "show the set of n with the property is inductive".
- **Jech 1.7.** Every nonempty X ⊆ ℕ has an ∈-minimal element. The book's hint, pick n ∈ X and look at X ∩ n, is the whole proof once 1.3 is known.
- **Jech 1.10.** Each n is T-finite: every nonempty family of subsets of n has a ⊆-maximal member. Tarski's definition of finite without numbers, and an induction.
- **Jech 1.14.** Separation follows from replacement: F = {(x, x) : φ(x)} is a function and F(X) = {x ∈ X : φ(x)}. [Replacement](../replacement/README.md) does it with H.
- **Jech 1.15.** The weak union axiom, "some Y contains ∪X", plus separation, gives the union axiom; likewise for power set and replacement. Separation inside the big Y is the move.
- **Cunningham 1.4.1 to 1.4.5.** Say in English: ∃x ∀y (y ∉ x); ∀y ∃x (y ∉ x); ∀y ∃x (x ∉ y); ∀y ¬∃x (x ∉ y); ∀z ∃x ∃y (x ∈ y ∧ y ∈ z). The program's English is one reading; check yours against it, and note which two sentences are false, and why ∅ is the reason both times.
- **Cunningham 1.5.1, 1.5.2.** {u, v, w} and {A} exist. Pairs and unions, then "unique by extensionality".
- **Cunningham 1.5.3, 1.5.4, 1.5.5.** From regularity: A ∉ A; A ∈ B implies B ∉ A; A ∈ B ∈ C implies C ∉ A. Look at {A}, {A, B}, {A, B, C}; [foundation](../foundation/README.md) shows why the pair is the set to look at.
- **Cunningham 1.5.6, 1.5.7.** 𝒫(A) ∩ B and A ∖ B exist. Separation inside 𝒫(A), and inside A.
- **Cunningham 1.5.8.** ∅, {∅} and {∅, {∅}} are three different sets. Extensionality: count members.

## What the program prints

<!-- output:axiom_katas -->
*Verified output of [`axiom_katas.py`](examples/axiom_katas.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
KUNEN, EXERCISE I.2.1: WHICH AXIOMS HOLD IN SEVEN SMALL MEMBERSHIP GRAPHS?
   (x, y) in E means x ∈ y; Pairing and Union in Kunen's weak forms.
   #   universe                                       Ext  Found  Pair  Union
   1   a = {}                                        True   True False   True
   2   a = {a}                                       True  False  True   True
   3   a = {b}, b = {a}                              True   True False   True
   4   a = {b}, b = {a}, c = {a, b}                  True  False False   True
   5   a = {}, b = {a}, c = {a}                     False   True False   True
   6   0 = {}, 1 = {0}, 2 = {0, 1}, 3 = {0, 1, 2}    True   True False   True
   7   a = {}, b = {a}, c = {b}                      True   True False   True
   Pairing holds only in #2, as Kunen says: a ∈ a is the one point that
   contains a pair. Extensionality fails only in #5, where b and c have
   the same member. Foundation fails in #2 (a ∈ a) and #4 (c = {a, b} with
   a and b members of each other); #3 has the same two-cycle and passes,
   because the pair {a, b} is not in it. This exercise is the method of
   the whole chapter: an axiom is checked on a universe, not believed.

KATAS, CHECKED BEFORE YOU PROVE THEM
  Jech 1.1          (a, b) = (c, d) iff a = c and b = d, with (a, b) = {{a}, {a, b}}
                    -> True   (all 256 choices from V_3)
  Jech 1.2          there is no set X with P(X) ⊆ X
                    -> True   (every X in V_4; |P(X)| = 2^|X| > |X| is the proof)
  Jech 1.3          each n in N is transitive, and n = {m ∈ N : m < n}
                    -> True   (0 to 6, with m < n meaning m ∈ n)
  Jech 1.5          n ∉ n and n ≠ n + 1 for each n in N
                    -> True
  Jech 1.7          every nonempty X ⊆ N has an ∈-minimal element
                    -> True   (all 31 nonempty subsets of {0, ..., 4}; the hint says: pick n ∈ X, look at X ∩ n)
  Jech 1.8          each n ≠ 0 in N is m + 1 for some m
                    -> True
  Jech 1.10         each n in N is T-finite (Tarski): every nonempty X ⊆ P(n) has a ⊆-maximal member
                    -> True   (n = 0 to 3; for n = 3, P(n) has 8 members and 255 nonempty X)
  Jech 1.14         separation follows from replacement: {x ∈ X : φ(x)} = F(X) for F = {(x, x) : φ(x)}
                    -> True   (φ = 'x has one member', every X in V_4)
  Jech 1.15         the weak union axiom (∃Y ⊇ ∪X) plus separation gives ∪X
                    -> True   (Y = V_3 works for every X in V_4; the same move does power set and replacement)
  Cunningham 1.4.1  ∃x ∀y (y ∉ x):  'there is a set with no members'
                    -> True   (true in V_4, as in ZF)
  Cunningham 1.4.2  ∀y ∃x (y ∉ x):  'for every set there is a set it does not belong to'
                    -> True   (true in V_4, as in ZF)
  Cunningham 1.4.3  ∀y ∃x (x ∉ y):  'no set contains every set'
                    -> True   (true in V_4, as in ZF)
  Cunningham 1.4.4  ∀y ¬∃x (x ∉ y):  'every set contains every set'
                    -> False   (false in V_4, as in ZF: ∅ is the counterexample)
  Cunningham 1.4.5  ∀z ∃x ∃y (x ∈ y ∧ y ∈ z):  'every set has a member that has a member'
                    -> False   (false in V_4, as in ZF: ∅ is the counterexample)
  Cunningham 1.5.1  {u, v, w} exists: it is ∪{{u, v}, {w}} (pairs twice, union once)
                    -> True
  Cunningham 1.5.2  {A} exists: it is the pair {A, A}
                    -> True
  Cunningham 1.5.3  A ∩ {A} = ∅, hence A ∉ A  (regularity)
                    -> True
  Cunningham 1.5.4  if A ∈ B then B ∉ A  (look at {A, B})
                    -> True
  Cunningham 1.5.5  if A ∈ B and B ∈ C then C ∉ A  (look at {A, B, C})
                    -> True   (4096 triples)
  Cunningham 1.5.6  P(A) ∩ B exists: separation inside P(A) with 'x ∈ B'
                    -> True
  Cunningham 1.5.7  A ∖ B exists: separation inside A with 'x ∉ B'
                    -> True
  Cunningham 1.5.8  ∅, {∅}, {∅, {∅}} are pairwise distinct
                    -> True   (extensionality: ∅ has no member, {∅} has one, {∅, {∅}} has two)

20 of 22 checks come out True; the one False is
Cunningham 1.4.4, a sentence that is false in ZF too. A check is not a
proof: V_4 is one universe, and the proof has to work in every one.
```
<!-- /output -->

## Po polsku, w skrócie

Kata to krótkie ćwiczenie powtarzane, aż ruch stanie się automatyczny, a ruchów w aksjomatycznej teorii mnogości jest pięć: podwójne zawieranie (a ⊆ b i b ⊆ a), „istnieje na mocy aksjomatu, jedyny na mocy ekstensjonalności", element najmniejszy (albo ∈-minimalny z aksjomatu regularności), indukcja (zbiór jest induktywny, więc zawiera ℕ) i przekątna lub liczenie (2ⁿ > n). Strona zbiera dwadzieścia dwa zadania z rozdziału 1 Jecha (1.1–1.15) i rozdziału 1 Cunninghama (1.4, 1.5); do każdego program sprawdza tezę na małym uniwersum, V₃, V₄ albo liczbach von Neumanna do 6. True nie jest dowodem, bo dowód musi działać w każdym uniwersum, ale mówi, że zdanie zostało dobrze odczytane; False oznacza błędne odczytanie, a jedno zadanie Cunninghama (1.4.4) jest zdaniem fałszywym także w ZF. Przed dowodem nazwij ruch; wtedy zadanie jest w połowie zrobione.

## Auf Deutsch: Stichwörter

Die ersten Übungen von Jech und Cunningham, jede im Modell geprüft, bevor man sie beweist.

**Stichwörter:** Übungsaufgabe (kata), Axiom, Modellprüfung, Stufen V₁ bis V₄, Gegenbeispiel, Beweis.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 13_Axioms_of_Set_Theory/axiom_katas/examples/axiom_katas.py
```

## See also

- [Reading a formula](../reading_a_formula/README.md) — how to read each kata aloud before proving it
- [Set katas](../../04_Sets/set_katas/README.md) — the same idea for the language of sets, from Cunningham's exercises 1.1
- [Studying vs learning ↗](https://masiarek.github.io/learning-to-learn-library/01_Knowing_What_You_Know/studying_vs_learning/) and [spaced retrieval ↗](https://masiarek.github.io/learning-to-learn-library/02_Making_It_Stay/spaced_retrieval/) — why the proof should be attempted before it is read, and repeated a week later
