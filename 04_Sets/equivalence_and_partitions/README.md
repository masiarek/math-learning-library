# Equivalence relations, partitions and the kernel of a function

**Level:** 101 · for anyone who has met "reflexive, symmetric, transitive" as three words to memorise and wants to know what they buy

**One line:** Cutting a set into blocks, saying when two things count as the same, and asking which inputs a function cannot tell apart are one idea three ways: a partition, an equivalence relation and the kernel of a function determine each other exactly, which is why there are the same number of each on a finite set and why every function is a surjection followed by a bijection followed by an inclusion; the rest of the textbook chapter, comparing equivalences, generating them, well-definedness and orbits, is four more program sections.

## Three definitions

**A partition** of S is a collection of nonempty blocks, pairwise disjoint, whose union is S: Simovici and Djeraba's Definition 1.107. The five partitions of {1, 2, 3} are listed in section 1 of the program; a set of n members has B(n) partitions, the Bell numbers 1, 2, 5, 15, 52, …

**An equivalence relation** on S is a [relation](../relations_and_functions/README.md), a set of pairs, that is reflexive (every x ~ x), symmetric (x ~ y gives y ~ x) and transitive (x ~ y and y ~ z give x ~ z). The **class** of u is [u] = {y : u ~ y}, and the **quotient** S/~ is the set of classes.

**The kernel** of a function f on S is the relation ker(f) = {(u, v) : f(u) = f(v)}, "f cannot tell u from v". It is always an equivalence, since = is one.

## Why they are one idea

Given a partition, relate x and y when they share a block; given an equivalence, take its classes as blocks. Section 2 checks on {1, 2, 3} that each construction undoes the other, and counts: of the 512 relations on {1, 2, 3}, exactly 5 are equivalences, the number of partitions. This is Simovici and Djeraba's Corollary 1.114, a bijection between EQ(S) and PART(S), and the reason "reflexive, symmetric, transitive" is the right list: those are precisely the three properties a "shares a block with" relation has, and section 2 shows what goes wrong without transitivity, a tolerance whose would-be classes [1] = {1, 2} and [3] = {2, 3} overlap.

The kernel closes the triangle. Every function has one, and every equivalence is one: ~ is the kernel of the function "which class am I in", u ↦ [u]. Section 3 takes f = length on seven words and shows its kernel's classes; section 4 is the **decomposition theorem**, Simovici's 1.116 and the same statement as the first isomorphism theorem of algebra: every function f : U → V is a surjection U → U/ker(f) onto the classes, then a bijection U/ker(f) → f(U), then an inclusion f(U) → V. Three maps, each of one kind, and f is their composite.

## The one everyone uses

Congruence mod m, section 5: p ≡ q (mod m) when m divides p − q. It is the kernel of "remainder on division by m", its classes are the m remainders, and the quotient ℤ/mℤ is the set the whole of modular arithmetic, from clock faces to RSA, is done in. [The laws of an operation](../../06_Algebraic_Structures/laws_of_an_operation/README.md) is where that set gets its + and ×.

## Where it is used

| Branch | What is an equivalence or partition there |
|---|---|
| Number theory | Congruence mod m; ℤ/mℤ; "same remainder" as the only fact that matters |
| Algebra | Cosets of a subgroup, which partition the group; the quotient group G/H; "isomorphic" as an equivalence on structures |
| Geometry and topology | Gluing: a torus is a square with opposite edges identified, which is a quotient by an equivalence |
| Analysis | The real numbers themselves: Cauchy sequences of rationals, two equivalent when their difference tends to 0 |
| Data mining | Clustering is a partition of the data; the rows that agree on some columns form the classes of a functional dependency, Simovici and Djeraba's chapter 12 |
| Computing | `GROUP BY` in SQL partitions rows by the kernel of the grouping expression; a hash table partitions keys by the kernel of the hash |

## Where the textbook sections live here

The owner asked whether this library has sub-pages for the sections of Wikipedia's article on equivalence relations (blocked from this session, so the list is from memory). Not sub-pages: a page per section would be a stub, which the [roadmap](../../ROADMAP.md) rules out. Each section has a place, and the four that had none are now sections 6 to 9 of the program, below.

| Section of the article | Where it is in this library |
|---|---|
| Definition; notation ~, ≡, [a] | this page, and the six properties as loops on [orderings](../orderings/README.md) |
| Examples: same birthday, congruence mod n, same image under f, similar triangles, equal cardinality | section 5 here (mod m); the kernel, section 3; [congruent and similar triangles](../../10_Geometry/congruent_and_similar_triangles/README.md); [cardinality](../cardinality/README.md), where equipotence is the equivalence whose classes are the cardinals |
| Relations that are not equivalences | the tolerance in section 2; "distinct siblings" and R₃ on [orderings](../orderings/README.md) |
| Connections to other relations: partial order, preorder, strict order, tolerance, partial equivalence | [orderings](../orderings/README.md) |
| Equivalence class, quotient set, the fundamental theorem that classes partition the set | sections 1 to 3 here |
| Comparing equivalence relations: finer, coarser, the lattice | **section 6, new**: the intersection of two equivalences is one, the union only when one contains the other, and the five equivalences on three points form a lattice under ⊆ |
| Generating an equivalence: the closure of a relation, the kernel of a function, the orbits of a group action | **section 7, new**, the smallest equivalence containing a relation, whose classes are the connected components; section 3, the kernel; **section 9, new**, orbits |
| Well-definedness under an equivalence | **section 8, new**: addition on ℤ/5ℤ is well defined because any representatives give the same class, and "n mod 3" on the same classes is not |
| Algebraic structure: group actions, groupoids, the lattice of partitions | section 9 and section 6; groupoids are not here |
| Logic: Euclid's "things equal to the same thing are equal to each other" is transitivity | [orderings](../orderings/README.md) and the matrix test M·M ⊆ M |

The owner then sent Wikipedia's picture of the 52 partitions of a five-element set, from the article on partitions. Its sections and their places: the definition and the equivalence correspondence are sections 1 to 3; refinement and the lattice of partitions are section 6 and [orderings](../orderings/README.md#the-other-partition); counting partitions, with the Bell numbers, the Stirling numbers of the second kind S(n, k) that count partitions into exactly k blocks, the Bell triangle, and the non-crossing partitions counted by the Catalan numbers, is **section 10, new**. The picture's rows are the Stirling numbers in order: 1 partition into five singletons, 10 with one pair, 25 with one triple or two pairs, 15 with a block of four or a triple and a pair, 1 with everything together, and 42 of the 52 are non-crossing when the five points sit on a circle.

**Sections 6 to 9 in a sentence each.** Two equivalences meet in their intersection, which is always an equivalence, and join in the smallest equivalence containing their union, which the union itself usually is not: {{1, 2}, {3}} and {{1}, {2, 3}} give 1 ~ 2 and 2 ~ 3 without 1 ~ 3, André's exercise 7.1. Any relation generates an equivalence by adding the diagonal, the reversed pairs, and then shortcuts until none appear; its classes are the connected components of the relation's graph, which is how a union-find structure computes them. A function on classes is well defined only if it gives the same answer for every representative, which addition mod 5 does and "n mod 3" does not; that check is the one every quotient construction, from ℤ/mℤ to the real numbers as Cauchy sequences, has to pass. And the orbits of a group acting on a set, the sixteen colourings of a four-bead necklace under rotation, say, are the classes of "can be moved to", with Burnside's lemma counting them: six.

## What the program prints

<!-- output:equivalence_and_partitions -->
*Verified output of [`equivalence_and_partitions.py`](examples/equivalence_and_partitions.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. THE PARTITIONS OF {1, 2, 3}, AND THE RELATION EACH ONE IS
   a partition: nonempty blocks, pairwise disjoint, with union the whole set.
   π = {{1}, {2}, {3}}            ρ_π has  3 pairs; equivalence: True
   π = {{1, 2}, {3}}              ρ_π has  5 pairs; equivalence: True
   π = {{1, 3}, {2}}              ρ_π has  5 pairs; equivalence: True
   π = {{1}, {2, 3}}              ρ_π has  5 pairs; equivalence: True
   π = {{1, 2, 3}}                ρ_π has  9 pairs; equivalence: True
   Bell numbers: a set of 1, 2, 3, 4, 5 members has 1, 2, 5, 15, 52 partitions.

2. EQUIVALENCES AMONG ALL 512 RELATIONS ON {1, 2, 3}
   reflexive and symmetric and transitive: 5 of 512, the same number as partitions.
   partition -> relation -> partition is the identity: True
   equivalence -> classes -> equivalence is the identity: True
   So EQ(S) and PART(S) are in bijection (Simovici–Djeraba, Corollary 1.114).
   a tolerance that is not an equivalence: 1~2, 2~3, but 1~3? False: transitivity fails,
   and 'has a block' fails with it: the classes [1] = {1, 2} and [3] = {2, 3} overlap.

3. EVERY FUNCTION HAS A KERNEL, AND EVERY EQUIVALENCE IS ONE
   f = length, on ['set', 'map', 'pair', 'class', 'block', 'ring', 'field']
   ker(f) = {(u, v) : f(u) = f(v)} has classes:
     length 5: ['block', 'class', 'field']
     length 3: ['map', 'set']
     length 4: ['pair', 'ring']
   ker(f) is an equivalence: True
   conversely every equivalence on {1, 2, 3} is ker of 'which class am I in': True

4. THE DECOMPOSITION THEOREM: f = (inclusion) ∘ (bijection) ∘ (quotient)
   U/ker(f) has 3 classes and f(U) = [3, 4, 5] has 3 values: h is a bijection: True
   k(h(g(w))) == f(w) for every w: True   (Theorem 1.116)
   Every function is a surjection onto its classes, then a relabelling, then an inclusion.

5. THE ONE EVERYONE USES: CONGRUENCE MOD m
   p ≡ q (mod 5) when 5 divides p − q; on −7..7 it is an equivalence: True
     [3] = [-7, -2, 3]
     [4] = [-6, -1, 4]
     [0] = [-5, 0, 5]
     [1] = [-4, 1, 6]
     [2] = [-3, 2, 7]
   5 classes, which are the 5 possible remainders: ℤ/5ℤ.
   It is ker(r) for r(n) = n mod 5: True

6. COMPARING EQUIVALENCES: FINER, COARSER, MEET AND JOIN (ANDRÉ, EXERCISES 7.1 AND 7.4)
   R ∩ T is an equivalence for all 25 pairs of equivalences on {1, 2, 3}: True
   R ∪ T is one in 19 of 25 pairs, exactly the 19 pairs where one contains the other: True
   e.g. {{1, 2}, {3}} ∪ {{1}, {2, 3}} has 1 ~ 2 and 2 ~ 3 but not 1 ~ 3: transitivity fails.
   R is finer than T (R ⊆ T) when every block of R sits inside a block of T. The
   equivalences on a set form a lattice under ⊆: meet = intersection, join = the
   smallest equivalence containing the union (section 7), bottom = Id, top = all pairs.

7. THE EQUIVALENCE GENERATED BY A RELATION: CLOSE IT UP
   R = [(1, 2), (2, 3), (5, 6)] on 1..6 is not an equivalence: False
   add the diagonal, the reversed pairs, then shortcuts until none appear (1 round):
   classes {{1, 2, 3}, {4}, {5, 6}}, 14 pairs. It is the smallest equivalence containing R:
   removing any one off-diagonal pair breaks it: True. The classes are the connected components of the graph of R.

8. WELL-DEFINED ON CLASSES: + ON ℤ/5ℤ IS, 'n MOD 3' IS NOT
   [a] + [b] := [a + b]: the result is the same whichever representatives are picked, all choices in -10..10: True
   f([n]) := n mod 3 on ℤ/5ℤ is not well defined: -10 and -5 are the same class mod 5 and give 2 and 1.
   A function on classes must give one answer per class; a map from representatives
   that respects the relation is the only kind that descends to the quotient.

9. ORBITS OF A GROUP ACTION ARE AN EQUIVALENCE: A FOUR-BEAD NECKLACE
   16 colourings of 4 beads in 2 colours; 'is a rotation of' is an equivalence: True
   its classes, the orbits, number 6: ['oooo', 'ooox', 'ooxx', 'oxox', 'oxxx', 'xxxx'] as representatives
   Burnside's count: (fixed by each rotation [16, 2, 4, 2]) / 4 = 6, the same number.
   Every group acting on a set partitions it into orbits; 'congruent' and 'similar'
   triangles are the orbits of the rigid motions and of the similarities of the plane.

10. COUNTING PARTITIONS: STIRLING NUMBERS, BELL NUMBERS, THE BELL TRIANGLE, NON-CROSSING
   S(n, k), partitions of an n-set into exactly k blocks, S(n, k) = k·S(n−1, k) + S(n−1, k−1):
   n \ k     1    2    3    4    5    6   Bell
       1     1    .    .    .    .    .      1
       2     1    1    .    .    .    .      2
       3     1    3    1    .    .    .      5
       4     1    7    6    1    .    .     15
       5     1   15   25   10    1    .     52
       6     1   31   90   65   15    1    203
   the 52 partitions of a 5-set by number of blocks, enumerated: [1, 15, 25, 10, 1] = S(5, k);
   the Wikipedia picture draws them in that order: one five-block partition, then 10, 25, 15, 1.
   Bell triangle: start each row with the end of the row above, add the number above to the left:
       1
       1   2
       2   3   5
       5   7  10  15
      15  20  27  37  52
      52  67  87 114 151 203
   its left edge 1, 1, 2, 5, 15, 52 is the Bell numbers.
   non-crossing partitions of 5 points on a circle (no a < b < c < d with a, c in one block and b, d in another): 42,
   the Catalan number C(10, 5)/6 = 42; the picture's crossed pairs of lines are the 10 crossing ones.
```
<!-- /output -->

## Po polsku, w skrócie

Podział zbioru na rozłączne, niepuste bloki pokrywające całość; relacja równoważności, czyli zwrotna, symetryczna i przechodnia; jądro funkcji, czyli relacja „f nie odróżnia u od v": to jedna idea w trzech postaciach. Podział daje relację „mamy wspólny blok", relacja daje podział na klasy, i program sprawdza na {1, 2, 3}, że każda z tych konstrukcji odwraca drugą; z 512 relacji na tym zbiorze dokładnie 5 to równoważności, tyle ile podziałów (liczby Bella: 1, 2, 5, 15, 52). Bez przechodniości klasy by się nakładały. Każda funkcja ma jądro, a każda równoważność jest jądrem funkcji „w której klasie jestem"; stąd twierdzenie o rozkładzie: każda funkcja to suriekcja na klasy, potem bijekcja, potem włożenie. Przykład, którego używają wszyscy, to przystawanie modulo m: jądro funkcji „reszta z dzielenia przez m", klasy to reszty, iloraz to ℤ/mℤ. Sekcje 6–9 programu dodają resztę hasła z Wikipedii: przekrój dwóch relacji równoważności jest relacją równoważności, suma zwykle nie; każdą relację można domknąć do najmniejszej relacji równoważności, której klasy to składowe spójne grafu; działanie na klasach jest dobrze określone tylko wtedy, gdy nie zależy od wyboru reprezentanta (dodawanie modulo 5 tak, „n mod 3" na klasach modulo 5 nie); orbity działania grupy, na przykład obroty naszyjnika z czterech koralików, są klasami równoważności, a lemat Burnside'a je liczy. Sekcja 10 liczy podziały: liczby Stirlinga drugiego rodzaju S(n, k) to podziały na dokładnie k bloków, ich suma to liczba Bella, trójkąt Bella je generuje, a podziały nieprzecinające się pięciu punktów na okręgu liczy liczba Catalana 42.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 04_Sets/equivalence_and_partitions/examples/equivalence_and_partitions.py
```

## See also

- [Relations and functions are sets of pairs](../relations_and_functions/README.md) — what a relation is, before three properties are asked of it
- [The laws of an operation](../../06_Algebraic_Structures/laws_of_an_operation/README.md) — ℤ/mℤ with its arithmetic
- [Cardinality of sets](../cardinality/README.md) — the bijection in the middle of the decomposition
- Dan A. Simovici and Chabane Djeraba, *Mathematical Tools for Data Mining* (2nd ed., Springer, 2014), sections 1.3.6 and 1.3.7
- [Equivalence relation ↗](https://en.wikipedia.org/wiki/Equivalence_relation) — Wikipedia
