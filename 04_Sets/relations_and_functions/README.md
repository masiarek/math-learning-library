# Relations and functions are sets of pairs

**Level:** 101 · for anyone surprised that a book on sets has chapters on functions and graphs, or that a table in a database is a "relation"

**One line:** A relation is a set of ordered pairs and nothing else, a function is a relation with one extra property, a graph is a relation drawn as arrows, and a database table is a relation stored; so every fact about sets applies to all of them, "x ρ y" is just a way of writing (x, y) ∈ ρ, and a function is the table of its values, not the formula that produced it.

## Three definitions, one object

**A relation is a set of ordered pairs.** "m divides n" on the numbers 1 to 6 is not a verb but a set: the fourteen pairs (m, n) for which the division works, printed in section 1 of the program. To ask whether 2 divides 6 is to ask whether (2, 6) is a member. The notation x ρ y, or x < y, or x ∈ y, means (x, y) ∈ ρ and nothing more; Jech writes it in one line, "an n-ary relation R is a set of n-tuples", and Simovici and Djeraba's Definition 1.24 says the same. The **domain** dom(ρ) is the set of first entries, the **range** ran(ρ) the set of second entries, and the **inverse** ρ⁻¹ is the same pairs turned round. All three are sets built from ρ by the [axioms](../../13_Axioms_of_Set_Theory/README.md) of the next chapter: a pair (x, y) is Kuratowski's {{x}, {x, y}}, so x and y are members of members of ρ, and dom and ran are comprehensions inside ∪∪ρ, which is Jech's page 10.

**A function is a relation with one property.** For each x there is at most one y with (x, y) in it: Jech's "(x, y) ∈ f and (x, z) ∈ f implies y = z", Simovici's Definition 1.34, Cunningham's and Kunen's too. Then f(x) means "the unique y", and that is all f(x) ever means. Section 2 shows the squaring relation, which is a function, and its inverse, which is not, since 4 has the partners 2 and −2. A Python dictionary is this object with no change: `dict(square)` is the set of pairs with lookup, and a dictionary with a key repeated is impossible for the same reason a function cannot have two values at one input.

**A graph is a relation drawn.** Put the members of the base set on the page and an arrow from x to y for each pair (x, y) in ρ, and the result is a **directed graph**; an **undirected graph** is a symmetric relation, one equal to its inverse, or equivalently a set of two-element sets {x, y}. Section 5 draws the "likes" relation from [predicates and quantifiers](../../11_Logic/predicates_and_quantifiers/README.md). Kunen's Exercise I.2.1 draws seven small universes of set theory this way, an arrow for each x ∈ y, and the [axiom katas](../../13_Axioms_of_Set_Theory/axiom_katas/README.md) evaluate the axioms on each of them: a membership relation is a directed graph, so the universe of set theory is one too.

A **database table** is the same object a fourth time: a relation whose pairs are rows, which is why Codd called his model relational and why SQL's `JOIN` is the relation product of the next section. Simovici and Djeraba's chapter 12 is this observation at book length.

## The three words

Injective, surjective and bijective drive most readers mad, because they are Latin for pictures. Draw the function as arrows from the inputs on the left to the targets on the right.

| Word | Latin | Picture | Plain words | Python test on a set of pairs |
|---|---|---|---|---|
| **[injective](../../GLOSSARY.md#injective-one-to-one)**, one-to-one | *in-icere*, to throw in | no two arrows land on the same target | different inputs, different outputs; nothing gets merged | `len({y for x, y in f}) == len(f)` |
| **[surjective](../../GLOSSARY.md#surjective-onto)**, onto | *sur-jacere*, to throw onto | every target is hit by at least one arrow | nothing in the target is missed | `{y for x, y in f} == T` |
| **[bijective](../../GLOSSARY.md#bijection)**, one-to-one correspondence | both | every target is hit exactly once | a perfect pairing, so it can be undone | both tests |

One more word drives people mad, and Ashlock's chapter is honest about it: **range** has two meanings. In this library and in Jech, ran(f) is the set of values actually taken, which others call the **image** and write Im(f) or f[S]. In many calculus books and in computer science, "range" means the set T in f : S → T, which others call the **codomain**, and the values actually taken are then the image. Surjective means "image equals codomain", and the word "onto" is safer than "range" when it matters.

Each word is a property of the arrows only, and each fails in one way: an injection fails when two inputs share an output, a surjection fails when some target is never reached. "One-to-one" is the trap: it means injective, not bijective, and "one-to-one correspondence" means bijective; the Latin words exist to end that confusion. A function is invertible exactly when it is bijective, since undoing it needs every target reached (surjective) and reached once (injective); on a finite set, the three properties coincide (Simovici and Djeraba, Theorem 1.69), which section 3 of the program counts.

## What the program checks

Section 3 takes every relation on {1, 2, 3}, 512 of them, and sorts them: 64 are functions (partial ones, defined on some inputs), 27 are functions defined on all three inputs, and of those 6 are injections, 6 surjections and 6 bijections, the 3! permutations. On a finite set the three counts agree, which is Simovici's Theorem 1.69 and the reason the pigeonhole principle works; on an infinite set they come apart, which is Dedekind's definition of infinite in [the reading guide](../../reading_guides/set_theory/README.md). The theorem that ρ is a function exactly when ρ⁻¹ is one-to-one (Simovici's 1.37) is checked on all 512.

Section 4 is **composition** as a product of relations: ρσ is "first ρ, then σ", the set of (x, z) for which some y has (x, y) ∈ ρ and (y, z) ∈ σ. On all 16 relations on {1, 2} it is associative, its inverse reverses the order, (ρσ)⁻¹ = σ⁻¹ρ⁻¹, and a product of functions is a function. Here the books part company in a way worth knowing: Simovici writes ρσ and, for functions, gf meaning "f then g"; Jech, Kunen and nearly everyone else write g ∘ f for the same set, so that (g ∘ f)(x) = g(f(x)) reads in the order of evaluation. Same set, letters swapped, and section 4 says so.

Section 7 runs Hrbacek and Jech's exercises 2.3 and 2.4 on images of sets under a relation, R[A] and R⁻¹[B], over all 512 relations and all subsets: the image of a union is the union of the images, but the image of an intersection is only *contained in* the intersection of the images, and the program finds the relation and sets where the two differ. A relation can send two different inputs to one output, and that is the whole reason; a one-to-one relation cannot, and for it the inclusions become equalities, which is Simovici and Djeraba's Theorem 1.62 and the shape of every "preimages behave better than images" lemma in analysis.

Section 6 is the point everything rests on. Two formulas that give the same output on every input, x² and |x|² say, define *one* function, because a function is its set of pairs and [extensionality](../../13_Axioms_of_Set_Theory/extensionality/README.md) says a set is its members. A function is not a rule or a formula; it is the table of its values, which is why a database table is one and why two programs that compute the same table compute the same function.

## Why the notation differs, and what is universal

Simovici and Djeraba write ρ, σ for relations, Dom and Ran in roman type, S − T for difference, T̄ for the complement, ⊕ for symmetric difference and ⇝ for a partial function; Jech writes R, dom and ran, X − Y, f"X; Cori and Lascar write Im(f) for the range; this library writes ρ, dom, ran, a ∖ b, f[A]. The owner's complaint is fair: the spellings differ because each author inherits a tradition, Peano's and Bourbaki's and the Polish school's and computer science's, and optimises the symbols for their own chapter. What is universal is the small core, ∈, ⊆, ∪, ∩, ∅, (x, y), ×, ∀, ∃, and the definitions behind the symbols, which do not vary at all. The [glossary of symbols](../../GLOSSARY.md#symbols) lists the spellings side by side; once the definition is known, a new spelling is a day's annoyance, not a new idea.

## Where this is used

| Branch | What is a relation or function there |
|---|---|
| Analysis | Every function from ℝ to ℝ is a set of pairs, its graph; images f[A] and preimages f⁻¹[B] of sets are what continuity (preimages of open sets are open) and measurability are defined by, and Simovici's Theorems 1.60 to 1.66 are the lemmas those definitions use. |
| Algebra | A homomorphism is a function that keeps the laws, as [maps that keep the laws](../../06_Algebraic_Structures/maps_that_keep_the_laws/README.md) says; a group's multiplication is a function from G × G to G. |
| Probability | A random variable is a function from the sample space to ℝ; an event is a subset, equivalently its indicator function, and Simovici's Theorem 1.55, that subsets of S match functions S → {0, 1}, is the 2ⁿ of [cardinality](../cardinality/README.md). |
| Combinatorics and graphs | A graph is a symmetric relation; a matching, a colouring and a path are functions and relations on it. |
| Databases and data mining | A table is a relation, a key is a function from rows to a column, a join is a relation product, and a partition of the rows is an equivalence relation. |
| Programming | A dictionary is a finite partial function, a type signature `f : S → T` is Jech's notation, and a pure function is one that is only its table of values. |

## Functions versus sets: Sullivan's four pictures

The owner sent section 2.1 of Sullivan's *Precalculus* and asked whether its definition is better than the one above, then said "functions vs sets, this is confusing". Both reactions are right, and the program's section 8 settles them.

Sullivan gives a function four times. First as a **mapping diagram**, two boxes and arrows (Figures 6 to 10). Second in words: "a function from X into Y is a relation that associates with each element of X exactly one element of Y", where a relation was a "correspondence". Third, a page later, as **a set of ordered pairs in which no ordered pairs have the same first element and different second elements**, which is this page's definition word for word. Fourth as an **equation** solved for y, and as a **machine** with an input pipe and an output pipe. The confusion is that these look like four different things. They are one set of pairs seen four ways: the arrows of the diagram are the pairs, the equation is a rule that generates the pairs, the machine is the rule run once, and the words "exactly one element of Y" are the one property the set must have.

So the answer to "is it better?" is: as a first description, yes, because it says what a function is *for*, certainty, one output per input, with the price of a stamp in 2018 as the relation that fails; as a definition, no, because "relation" and "associates" are left undefined, and the set-of-pairs sentence that Sullivan adds afterwards is the one that can be checked. The program runs that check on every example of the section: the specific-heat diagram, the stamp, the menu, the gestation table where 240 days has two life expectancies, Example 3's three sets of pairs, the line y = 2x − 5 and the unit circle x² + y² = 1, which fails because x = 0 has partners 1 and −1. One function `is_function` decides all nine, and it is the same function that decided section 2. Example 3(b), where the inputs 1 and 2 share the output 4, passes, as Sullivan notes: a function may merge inputs, it may not split one.

Two more of Sullivan's remarks are set theory in disguise. The warning that y = f(x) "does NOT mean f times x" is the warning that f is a set of pairs and f(x) the unique partner of x in it, so there is nothing to multiply. And the footnote crediting "the broad definition" to Lejeune Dirichlet, under which X and Y can be any two sets, is the history: Dirichlet's 1837 definition of a function as an arbitrary correspondence, with no formula required, is what section 6 above demonstrates with two different formulas giving one function.

## What the program prints

<!-- output:relations_and_functions -->
*Verified output of [`relations_and_functions.py`](examples/relations_and_functions.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. A RELATION IS A SET OF ORDERED PAIRS
   'm divides n' on {1, ..., 6} is the set of 14 pairs
   {(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 4), (2, 6), (3, 3), (3, 6), (4, 4), (5, 5), (6, 6)}
   2 divides 6?  (2, 6) ∈ δ: True     4 divides 6?  (4, 6) ∈ δ: False
   dom(δ) = [1, 2, 3, 4, 5, 6]   ran(δ) = [1, 2, 3, 4, 5, 6]
   'x ρ y' is just a way of writing (x, y) ∈ ρ; the relation IS the set.

2. A FUNCTION IS A RELATION WITH ONE PROPERTY
   square = {(-3, 9), (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4), (3, 9)}
   is a function: True   (each x has one square)
   root = square⁻¹ = {(0, 0), (1, -1), (1, 1), (4, -2), (4, 2), (9, -3), (9, 3)}
   is a function: False   (4 has partners 2 and -2)
   f(x) means 'the unique y with (x, y) ∈ f'; a Python dict is the same
   object:  dict(square) = {-3: 9, -2: 4, -1: 1, 0: 0, 1: 1, 2: 4, 3: 9}

3. FUNCTIONS, ONE-TO-ONE RELATIONS, INVERSES: EVERY RELATION ON {1, 2, 3}
   relations on {1, 2, 3}: 512   functions (partial): 64   with domain all of {1, 2, 3}: 27 = 3^3
   injections: 6   surjections: 6   bijections: 6 = 3!   (on a finite set, injective = surjective = bijective: True)
   ρ is a function  iff  ρ⁻¹ is one-to-one, all 512 relations: True   (Simovici–Djeraba, Theorem 1.37)
   (ρ⁻¹)⁻¹ = ρ and dom(ρ⁻¹) = ran(ρ): True

4. COMPOSITION IS A PRODUCT OF RELATIONS
   ρ = {(1, 2), (2, 3)}, σ = {(2, 10), (3, 20)}:  ρσ = {(1, 10), (2, 20)}   ('first ρ, then σ')
   on all 16 relations on {1, 2}:  (ρσ)τ = ρ(στ): True   (ρσ)⁻¹ = σ⁻¹ρ⁻¹: True   product of functions is a function: True
   Jech and Kunen write σ ∘ ρ for Simovici's ρσ: same set, letters swapped.

5. A GRAPH IS A RELATION DRAWN AS ARROWS
   'x likes y' from the quantifiers lesson: {(a, a), (b, c), (c, b), (d, c)}
     a → a
     b → c
     c → b
     d → c
   symmetric (an undirected graph): False;  an undirected graph is a relation equal to its inverse,
   or a set of two-element sets {x, y}. A membership table x ∈ y is a directed graph too:
   Kunen's Exercise I.2.1 draws seven of them, and the axiom katas page evaluates the axioms on each.

6. A FUNCTION IS ITS PAIRS, NOT ITS FORMULA
   y = x² and y = |x|² on {-2, ..., 2}: same set of pairs: True   so one function, by extensionality
   y = x² and y = x² mod 7 on {-2, ..., 2}: True   (they differ nowhere here) 
   Two formulas that agree on every input define one function; a function
   is the table of its values, which is why a table in a database is one.

7. IMAGES OF SETS UNDER A RELATION: HRBACEK AND JECH, EXERCISES 2.3 AND 2.4
   R[A] = {y : x R y for some x in A}; R⁻¹[B] = {x : x R y for some y in B}.
   2.3(a) R[A ∪ B] = R[A] ∪ R[B]: True    (b) R[A ∩ B] ⊆ R[A] ∩ R[B]: True    (c) R[A − B] ⊇ R[A] − R[B]: True
   2.3(d) ⊆ is not =: R = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}, A = {1}, B = {2}:
          R[A ∩ B] = ∅ but R[A] ∩ R[B] = {1, 2, 3}
   2.3(f) R⁻¹[R[A]] ⊇ A ∩ dom R, all 4096 cases: True
   2.4(a) R[X] = ran R and R⁻¹[Y] = dom R: True    2.4(e) R ∘ R⁻¹ ⊇ Id on dom R: True
   A relation can merge, so the image of an intersection can be smaller
   than the intersection of the images; a one-to-one relation cannot, and
   for it (b) and (c) become equalities (Simovici–Djeraba, Theorem 1.62).

8. SULLIVAN'S FOUR PICTURES OF A FUNCTION, ONE TEST FOR ALL
   Precalculus 2.1 shows a function as a mapping diagram, a set of pairs, an
   equation and a machine. Each is the same set of pairs, and is_function
   asks one thing of it: no two pairs with the same first member.
   Fig. 6, substance → specific heat      a function
   year → price of a stamp, 2018          not a function: 2018 has two partners
   Fig. 8, menu item → price              a function, and two inputs share the output 1, which is allowed
   Fig. 10, gestation → life expectancy   not a function: 240 has two partners
   Example 3(a)                           a function
   Example 3(b)                           a function, and two inputs share the output 4, which is allowed
   Example 3(c)                           not a function: -3 has two partners
   Example 4, y = 2x − 5 on x = −2..2     a function
   Example 5, x² + y² = 1 on a grid       not a function: 0.0 has two partners
   The machine picture is the same test read aloud: one output per input.
   'y = f(x)' names the unique partner of x, and the WARNING in the book,
   that f(x) is not f times x, is the warning that f is a set, not a number.
```
<!-- /output -->

## Po polsku, w skrócie

Relacja to zbiór par uporządkowanych i nic więcej: „m dzieli n" na liczbach 1–6 to czternaście par, a zapis x ρ y znaczy tylko (x, y) ∈ ρ. Funkcja to relacja z jedną dodatkową własnością: każdy x ma co najwyżej jeden y; f(x) oznacza „ten jedyny y", a słownik w Pythonie jest dokładnie tym obiektem. Graf to relacja narysowana strzałkami; graf nieskierowany to relacja symetryczna. Tabela w bazie danych to relacja zapisana wierszami, stąd nazwa „model relacyjny". Program sprawdza na wszystkich 512 relacjach na {1, 2, 3}, że ρ jest funkcją dokładnie wtedy, gdy ρ⁻¹ jest różnowartościowa, liczy iniekcje, suriekcje i bijekcje (na zbiorze skończonym po 6), i pokazuje złożenie jako iloczyn relacji; Simovici pisze ρσ i gf, Jech i Kunen g ∘ f, ten sam zbiór. Najważniejsze: funkcja to tabela swoich wartości, nie wzór; x² i |x|² to jedna funkcja, na mocy ekstensjonalności. Autorzy piszą te same rzeczy różnymi symbolami, bo dziedziczą różne tradycje; uniwersalny jest mały rdzeń ∈, ⊆, ∪, ∩, ∅, (x, y), × i same definicje.

Sullivan w *Precalculus* pokazuje funkcję na cztery sposoby: diagram ze strzałkami, zdanie „każdemu elementowi X odpowiada dokładnie jeden element Y", zbiór par bez dwóch par o tym samym pierwszym elemencie, i równanie albo maszynę. To jeden zbiór par widziany czterokrotnie; program sprawdza jednym testem wszystkie jego przykłady, w tym tabelę, gdzie 240 dni ciąży ma dwie długości życia (nie funkcja), i okrąg x² + y² = 1 (nie funkcja, bo x = 0 ma partnerów 1 i −1).

## Auf Deutsch: Stichwörter

Eine Relation ist eine Teilmenge von A × B, eine Funktion eine Relation mit genau einem Paar pro erstem Eintrag; der Graph ist die Funktion.

**Stichwörter:** Relation, Funktion als Paarmenge, Definitionsbereich, Wertebereich, Bild, Graph, injektiv, surjektiv, Komposition.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 04_Sets/relations_and_functions/examples/relations_and_functions.py
```

## See also

- [The Cartesian product](../cartesian_product/README.md) — the set A × B all these pairs are drawn from
- [Circles](../../08_Analytic_Geometry/circles/README.md) — the unit circle as a set of points, and why it is not a function of x
- Michael Sullivan, *Precalculus* (Pearson), section 2.1 *Functions*: the four pictures, Examples 2 to 5
- [Cardinality of sets](../cardinality/README.md) — size by bijection, the function this page counts
- [Pairs](../../13_Axioms_of_Set_Theory/pairs/README.md) and [replacement](../../13_Axioms_of_Set_Theory/replacement/README.md) — the axioms that make pairs, and images, sets
- [Predicates and quantifiers](../../11_Logic/predicates_and_quantifiers/README.md) — "x likes y" as a relation on four people
- Thomas Jech, *Set Theory* (Springer, 2003), chapter 1, pages 10 to 12; Karel Hrbacek and Thomas Jech, *Introduction to Set Theory* (3rd ed., 1999), chapter 2, sections 1 to 3; Dan A. Simovici and Chabane Djeraba, *Mathematical Tools for Data Mining* (2nd ed., Springer, 2014), section 1.3
- [Binary relation ↗](https://en.wikipedia.org/wiki/Binary_relation) — Wikipedia
