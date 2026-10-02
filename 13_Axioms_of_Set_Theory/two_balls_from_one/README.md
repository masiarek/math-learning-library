# Two balls from one: where the paradox lives, and where choice enters

**Level:** 301 · for anyone who has read that a ball can be cut into five pieces that reassemble into two balls and said "this is absolutely crazy"

**One line:** The Banach–Tarski theorem is three facts stacked: a group that can be split into pieces which, moved by one element each, make two copies of the group; a pair of rotations of space whose group is that free; and the axiom of choice, which picks one point from every orbit of that group on the sphere and so copies the group's pieces onto the sphere's points. The first two facts a program checks exactly, word by word and matrix by matrix, including the labelled Cayley graph Halbeisen draws; the third is the one step no program can take, and it is also the reason the pieces have no volume, so that nothing about volume was ever contradicted.

## What is claimed

Two figures in space are congruent when a rotation or translation carries one onto the other; two figures are equidecomposable when each can be cut into the same finite number of pieces, with the pieces congruent in pairs. Hausdorff showed in 1914 that the surface of a ball, minus a countable set, splits into three pieces A, B, C with A congruent to B, to C, and to B ∪ C: one piece is a third of the sphere and also two thirds of it. Banach and Tarski in 1924 turned this into the solid ball being equidecomposable with two solid balls, and Raphael Robinson in 1947 brought the number of pieces down to five, which is the least possible. Halbeisen's chapter 7 presents Hausdorff's partition and Robinson's decomposition in full; this page follows the first and says where the second differs.

The theorem is called a paradox, and it is not one. It contradicts the belief that every set of points has a volume, and that belief is false: the pieces are not shapes but scatterings of points, selected by the [axiom of choice](../choice/README.md), and the volume of such a set is undefined, not zero. Section 4 of the program prints the four-line argument. If a volume μ were defined on all subsets of the sphere, additive on disjoint sets and equal on congruent ones, then μ(A) = μ(B) = μ(C) and μ(A) = μ(B) + μ(C) force μ(A) = 0, so the whole sphere minus a countable set has volume 0, which no volume allows.

## The paradox lives in a group

Take all words in two letters a and b and their inverses A and B, cancelled wherever a letter meets its inverse: this is the [free group](../../GLOSSARY.md#free-group) on two generators. Sort the non-empty words by first letter into S(a), S(A), S(b), S(B). Multiply every word of S(A) on the left by a: the first letter cancels, and what remains is every word that does not begin with a. So the group is S(a) ⊔ a·S(A), and by the same token S(b) ⊔ b·S(B). Four pieces, two of them shifted by one letter, make two copies of the whole. Section 1 checks this on the 4 373 reduced words of length up to 7: every shorter word lies in exactly one of S(a) and a·S(A), and likewise for b.

That is already the theorem, for the group. A measure on the group that is finitely additive and unchanged by left multiplication would give the four pieces sizes p, q, r, s with p + q = 1 = r + s and p + q + r + s ≤ 1, which is impossible. What remains is to find this group inside the rotations of space and to carry its pieces onto points.

## Two rotations that are free enough

Hausdorff's rotations are φ, a half turn about the axis (1, 0, 1), and ψ, a third of a turn about the vertical axis. Their matrices have entries in the numbers p + q√3 with p and q rational, so the program computes with them exactly, as pairs of fractions, and no floating point enters. The relations φ² = ι and ψ³ = ι are checked, and the claim is that these are the only relations: no reduced word in φ, ψ, ψ⁻¹ other than the empty one is the identity, so the group they generate is the free product ℤ₂ * ℤ₃. Section 2 computes all 442 reduced words of length up to 12 and finds 442 distinct matrices and no identity.

Halbeisen leaves one exercise to the reader, on page 175: the product of n factors of the form ψ^±φ, multiplied by 2ⁿ, has a fixed shape, with even integers in five positions and odd integers in four, some multiplied by √3. The identity does not have that shape, so no such product is the identity, which proves the claim for all lengths at once. The program checks the shape on all 510 products with n ≤ 8 and finds no entry out of pattern. A free product ℤ₂ * ℤ₃ contains a free group on two letters, so the doubling of section 1 happens among rotations.

## The labelled Cayley graph

Halbeisen's figure on page 176 is a graph with one vertex per element of the group, an edge labelled φ from ρ to φρ and an edge labelled ψ from ρ to ψρ, and a label ❶, ❷ or ❸ on each vertex: ι gets ❶; φ sends ❷ or ❸ to ❶ and ❶ to ❷ or ❸; ψ sends ❶ to ❷, ❷ to ❸ and ❸ to ❶. Because every element is one reduced word, the label is a recursion on the word, and section 3 computes it. The rules then have to hold on every edge of the graph, including the edges along which a word gets shorter, and the program checks all 308 edges in the ball of radius 10 and finds none broken.

Let A, B, C be the elements labelled ❶, ❷, ❸. The three set identities that make the paradox, B = ψ[A], C = ψ⁻¹[A] and B ∪ C = φ[A], are then checked on the ball. So A is carried onto B by ψ, onto C by ψ⁻¹, and onto B ∪ C by φ: the piece A is a third of the group and also two thirds of it. Nothing so far used the axiom of choice; all of it is finite computation on words.

## Where the axiom of choice enters

The group acts on the sphere: each rotation moves points. Call two points equivalent when some rotation in the group moves one to the other; this is an [equivalence relation](../../04_Sets/equivalence_and_partitions/README.md), and its classes are the orbits. Leave out the countable set F of points that some rotation fixes, the points on the axes. Each remaining orbit is a copy of the group: pick one point m in it, and every other point of the orbit is ρ(m) for exactly one ρ, because no rotation other than ι fixes m.

Now choose one point from every orbit. There are uncountably many orbits and no rule that picks a point from each, so this is the [axiom of choice](../choice/README.md), used once and essentially. With the chosen points fixed, give each point x the label of the unique ρ with x = ρ(chosen point of x's orbit), and the sphere minus F splits into three pieces with the group's three identities carried over: B = ψ[A], C = ψ⁻¹[A], B ∪ C = φ[A]. That is Hausdorff's paradox, and the pieces are the sets a volume cannot measure. Robinson's decomposition of the solid ball does the same with four rotations and a more careful labelling, shown in Halbeisen's figures on pages 178 and 179, with the five pieces chosen so that two of them make one ball and the other three another.

Halbeisen records, as Related Result 48, that without the axiom of choice neither decomposition can be proved. In Solovay's model of set theory, built with an inaccessible cardinal and without full choice, every set of reals has a Lebesgue measure, and there the sphere cannot be doubled. So the crazy thing is not a fact about space; it is a fact about which sets of points the axioms let you name.

## What the program prints

<!-- output:two_balls_from_one -->
*Verified output of [`two_balls_from_one.py`](examples/two_balls_from_one.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. A GROUP THAT DOUBLES ITSELF: THE FREE GROUP ON a AND b
   reduced words in a, b and their inverses A, B, of length ≤ 7: 4373
   split them by first letter: S(a), S(A), S(b), S(B), and the empty word
   |S(a)| = 1093, |S(A)| = 1093, |S(b)| = 1093, |S(B)| = 1093
   every word (length ≤ 6) is in S(a) or in a·S(A), never both: True
   every word (length ≤ 6) is in S(b) or in b·S(B), never both: True
   So the group is S(a) ⊔ a·S(A) and also S(b) ⊔ b·S(B): four pieces,
   two of them moved by one letter, make two copies of the whole group.
   (The empty word is the one leftover; a trick absorbs it.) A measure that
   is finitely additive and invariant under left multiplication cannot exist.

2. HAUSDORFF'S TWO ROTATIONS GENERATE A GROUP THAT IS JUST AS FREE
   φ: half turn about the axis (1, 0, 1);  ψ: third turn about the z-axis
   φ² = ι: True;   ψ³ = ι: True;   ψ·ψ⁻¹ = ι: True
   reduced words in φ, ψ, ψ⁻¹ of length ≤ 12 (φ² = ψ³ = ι used to reduce): 442
   distinct rotation matrices among them: 442;  non-empty words equal to ι: 0
   Exact arithmetic in p + q√3, so 'distinct' is exact, not a float comparison.
   Halbeisen (p. 175) states the shape of 2ⁿ·(ψ^±φ ⋯ ψ^±φ): the entries marked
   a are even integers, those marked b are odd integers times √3 or not:
        ⎛ a₁    b₁√3  b₂  ⎞
        ⎜ a₂√3  b₃    b₄√3 ⎟
        ⎝ a₃    a₄√3  a₅  ⎠
   products of n ≤ 8 factors ψ^±φ checked: 510;  entries breaking the pattern: 0
   The pattern shows no such product is ι (ι has odd entries where a's sit),
   so the only relations are φ² = ψ³ = ι, and the group is the free product
   ℤ₂ * ℤ₃. It contains a free group on two letters, so section 1 applies.

3. THE LABELLED CAYLEY GRAPH: THREE PIECES, ONE A THIRD AND ALSO A HALF
   Halbeisen's rules: ι gets ❶; φ sends ❷ or ❸ to ❶ and ❶ to ❷ (or ❸);
   ψ sends ❶ → ❷ → ❸ → ❶. Labels by recursion on the reduced word:
      ι     label 1
      f     label 2
      p     label 2
      q     label 3
      fp    label 1
      pf    label 3
      qf    label 1
      fpf   label 1
      pfp   label 2
      fqf   label 2
   Cayley-graph edges checked in the ball of radius 10: 308;  rules broken: 0
   |A| = 94, |B| = 62, |C| = 62 in the ball
   B = ψ[A]:      True
   C = ψ⁻¹[A]:    True
   B ∪ C = φ[A]:  True
   (each identity checked on the words that stay inside the ball)
   So A ≅ B, A ≅ C and A ≅ B ∪ C: the piece A is a third of the group and,
   rotated by φ, also two thirds of it. Nothing here used the axiom of choice.

4. WHERE THE AXIOM OF CHOICE ENTERS, AND WHAT IT COSTS
   The group acts on the sphere. Two points are equivalent when some rotation
   in the group moves one to the other; the classes are the orbits. Choose
   one point in every orbit (the axiom of choice: uncountably many orbits,
   no rule). Every other point x is ρ(chosen point) for exactly one ρ in the
   group, and x gets ρ's label. The sphere, minus the countable set F of
   points on some rotation axis, becomes A ⊔ B ⊔ C with B = ψ[A],
   C = ψ⁻¹[A], B ∪ C = φ[A]: Hausdorff's paradox (1914).
   A volume μ that is additive on disjoint sets and equal on congruent sets:
     μ(A) = μ(B) = μ(C)            congruent pieces
     μ(A) = μ(B ∪ C) = μ(B) + μ(C)  congruent, then additive
     so μ(A) = 2·μ(A), μ(A) = 0, and μ(sphere ∖ F) = 3·μ(A) = 0,
     against μ(sphere) > 0 with F countable. No such μ exists on all subsets.
   Robinson (1947): the solid ball is five pieces that make two balls, and four
   do not suffice; Banach and Tarski (1924) had it with more pieces. Without
   the axiom of choice neither decomposition can be proved (Halbeisen's Related
   Result 48): in Solovay's model every set of reals has a volume.
```
<!-- /output -->

## Po polsku, w skrócie

Twierdzenie Banacha–Tarskiego: kulę można pociąć na pięć części (Robinson 1947; Banach i Tarski w 1924 potrzebowali ich więcej) i złożyć z nich, samymi obrotami i przesunięciami, dwie kule tej samej wielkości. To nie paradoks, tylko fakt o zbiorach punktów, które nie mają objętości. Konstrukcja ma trzy piętra. Pierwsze: grupa wolna o dwóch generatorach dzieli się na cztery kawałki, z których dwa przesunięte o jedną literę dają razem z pozostałymi dwie kopie całej grupy; program sprawdza to na 4373 słowach. Drugie: dwa obroty Hausdorffa, φ (pół obrotu) i ψ (jedna trzecia obrotu), spełniają tylko relacje φ² = ψ³ = ι, więc ich grupa jest równie wolna; program liczy dokładnie, w liczbach p + q√3, 442 słowa i 442 różne macierze, i sprawdza kształt iloczynów z ćwiczenia Halbeisena ze strony 175. Trzecie, na którym stoi etykietowany graf Cayleya ze strony 176: wierzchołki grupy dostają etykiety ❶❷❸ tak, że B = ψ[A], C = ψ⁻¹[A], B ∪ C = φ[A]; kawałek A jest jedną trzecią grupy i zarazem dwiema trzecimi. Dopiero przeniesienie tego z grupy na punkty sfery wymaga pewnika wyboru: z każdej orbity trzeba wybrać jeden punkt, a orbit jest nieprzeliczalnie wiele i nie ma reguły. Bez pewnika wyboru twierdzenia nie da się udowodnić: w modelu Solovaya każdy zbiór liczb rzeczywistych ma miarę.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 13_Axioms_of_Set_Theory/two_balls_from_one/examples/two_balls_from_one.py
```

## See also

- [Choice](../choice/README.md) — the axiom, what it buys and what it costs; Banach–Tarski sits in the cost column
- [Equivalence relations and partitions](../../04_Sets/equivalence_and_partitions/README.md) — orbits of a group acting on a set, the equivalence the construction uses
- [Measure zero](../../02_Measure_Zero/README.md) — what it means for a set to have a volume at all
- [Laws of an operation](../../06_Algebraic_Structures/laws_of_an_operation/README.md) — groups, the structure the paradox lives in
- Lorenz Halbeisen, *Combinatorial Set Theory*, 3rd ed. (Springer, 2025), chapter 7, "How to make two balls from one"; Stan Wagon, *The Banach–Tarski Paradox* (Cambridge, 1985), the book-length account
- [Banach–Tarski paradox ↗](https://en.wikipedia.org/wiki/Banach%E2%80%93Tarski_paradox) — Wikipedia
