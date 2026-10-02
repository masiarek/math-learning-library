# Function katas: Hrbacek and Jech's exercises on functions, with solutions

**Level:** 101 · for anyone working through chapter 2 of Hrbacek and Jech's *Introduction to Set Theory* who wants the exercises checked and the solutions written out

**One line:** The exercises after a first section on functions are all the same three moves, chase an element through the definitions, show two sets each contain the other, and find the one example where an inclusion is strict; the program checks every claim on all 64 partial functions on {1, 2, 3} and computes the concrete compositions and inverses exactly, and the solutions below are written move by move.

## How to use the page

The exercises are 3.1 to 3.13 and 4.1 of chapter 2 of Hrbacek and Jech (3rd ed., 1999), pages 28 and 32, and, at the end, the exercises of section 2.1 of Sullivan's *Precalculus*, the same definition of a function met one level down. Try each for ten minutes, run the program to see whether your reading of the claim is the book's, then compare with the solution. The program's True is a check, not a proof: {1, 2, 3} is one set, and the proof must work for all. Where an exercise asks for an example, the program finds the smallest one by search, which is also how to find one by hand: try the smallest sets first.

The three moves, named in each solution:

| Move | What it looks like |
|---|---|
| **[Element chase](../../04_Sets/algebra_of_sets/README.md#one-question-per-member)** | "let x ∈ dom(g ∘ f); then there is z with x (g ∘ f) z; so there is y with x f y and y g z; …" |
| **[Two inclusions](../../13_Axioms_of_Set_Theory/extensionality/README.md#what-it-is-for)** | to prove two sets equal, prove ⊆ and ⊇ by two element chases |
| **[Smallest counterexample](../../11_Logic/induction/README.md#why-it-works-the-least-counterexample)** | for "show that ⊆ cannot be replaced by =", a function that merges two inputs and a set that separates them |

## Solutions

**3.1** If ran f ⊆ dom g then dom(g ∘ f) = dom f. *Two inclusions.* Theorem 3.5 gives dom(g ∘ f) = dom f ∩ f⁻¹[dom g], so ⊆ is immediate. For ⊇, take x ∈ dom f; then f(x) ∈ ran f ⊆ dom g, so x ∈ f⁻¹[dom g], so x is in the intersection. Section 3.1 of the program confirms it on all 2 530 pairs with the hypothesis and shows a failure without it.

**3.2** With f₁ = 2x − 1 on ℝ, f₂ = √x on x > 0, f₃ = 1/x on x ≠ 0, and dom(g ∘ f) = {x ∈ dom f : f(x) ∈ dom g}:

| composite | formula | domain | range |
|---|---|---|---|
| f₂ ∘ f₁ | √(2x − 1) | 2x − 1 > 0, so x > ½ | (0, ∞) |
| f₁ ∘ f₂ | 2√x − 1 | x > 0 | (−1, ∞) |
| f₃ ∘ f₁ | 1/(2x − 1) | x ≠ ½ | ℝ ∖ {0} |
| f₁ ∘ f₃ | 2/x − 1 | x ≠ 0 | ℝ ∖ {−1} |

(The book's f₂ has domain x > 0, so f₂ ∘ f₁ excludes x = ½, where 2x − 1 = 0; with domain x ≥ 0 it would include it. The program's table marks every point outside a domain.)

**3.3** Each fᵢ is one-to-one, by solving: 2x − 1 = 2x′ − 1 gives x = x′; √x = √x′ gives x = x′ by squaring; 1/x = 1/x′ gives x = x′ by inverting. The inverses, found by solving y = f(x) for x: f₁⁻¹(y) = (y + 1)/2 with domain ℝ = ran f₁; f₂⁻¹(y) = y² with domain (0, ∞) = ran f₂; f₃⁻¹(y) = 1/y with domain ℝ ∖ {0} = ran f₃, so f₃ is its own inverse. In each case dom fᵢ = ran fᵢ⁻¹ and ran fᵢ = dom fᵢ⁻¹, which is exercise 2.4(c) applied to a function.

**3.4 (a)** Let f be invertible, so f⁻¹ is a function. *Element chase.* If (x, z) ∈ f⁻¹ ∘ f then for some y, (x, y) ∈ f and (y, z) ∈ f⁻¹, that is (z, y) ∈ f; f is one-to-one (Theorem 3.8), so x = z, and x ∈ dom f. Conversely (x, x) ∈ f⁻¹ ∘ f for every x ∈ dom f, via y = f(x). So f⁻¹ ∘ f = Id_dom f, and f ∘ f⁻¹ = Id_ran f is the same argument with f and f⁻¹ swapped. **(b)** Suppose g ∘ f = Id_dom f. If f(a₁) = f(a₂) then a₁ = g(f(a₁)) = g(f(a₂)) = a₂, so f is one-to-one, hence invertible; and for y ∈ ran f, y = f(a) gives g(y) = g(f(a)) = a = f⁻¹(y), so g↾ran f = f⁻¹. A right inverse proves nothing: the program's example is f constant, f = {(1, 1), (2, 1), (3, 1)}, and h = {(1, 1)}, with f ∘ h = Id_{1} = Id_ran f and f far from one-to-one. A right inverse only picks one preimage per value; a left inverse must undo f on its whole domain.

**3.5** If f and g are one-to-one, so is g ∘ f: if g(f(a₁)) = g(f(a₂)) then f(a₁) = f(a₂) since g is one-to-one, then a₁ = a₂ since f is. For the inverse, *two inclusions*: (z, x) ∈ (g ∘ f)⁻¹ iff (x, z) ∈ g ∘ f iff for some y, (x, y) ∈ f and (y, z) ∈ g iff (y, x) ∈ f⁻¹ and (z, y) ∈ g⁻¹ iff (z, x) ∈ f⁻¹ ∘ g⁻¹. The order reverses: g was applied last and is undone first.

**3.6** *Two inclusions*, and the reason the inclusions of exercise 2.3 become equalities for inverse images under a function. (a) x ∈ f⁻¹[A ∩ B] iff f(x) ∈ A ∩ B iff f(x) ∈ A and f(x) ∈ B iff x ∈ f⁻¹[A] and x ∈ f⁻¹[B]. (b) The same with "and not". Each "iff" uses that f(x) is *one* value; for a relation, "x is related to something in A and to something in B" need not mean the same something, and the program shows the law failing for relations.

**3.7** f ∩ A² ≠ f↾A. *Smallest counterexample.* The restriction f↾A keeps every pair whose first entry is in A, whatever its value; f ∩ A² also demands the value in A. Take f = {(1, 2)} and A = {1}: f↾A = f, f ∩ A² = ∅. The program finds one of the same shape.

**3.8** Every system of sets A is indexed by a function: take I = A and S = Id_A, so that Sᵢ = i and {Sᵢ : i ∈ I} = A.

**3.9 (a)** B^A exists: every function on A into B is a subset of A × B, so B^A = {f ∈ 𝒫(A × B) : f is a function on A into B}, a comprehension inside a set that exists by the power set axiom. **(b)** ∏ᵢ∈I Sᵢ exists: each member is a function on I into ∪ᵢ Sᵢ, so a subset of I × ∪ᵢ Sᵢ, and the product is a comprehension inside 𝒫(I × ∪ᵢ Sᵢ). The pattern is the one [the comprehension axiom](../../13_Axioms_of_Set_Theory/comprehension/README.md) describes: name a big enough set that exists, then cut.

**3.10** x ∈ ∪_{a ∈ ∪S} F_a iff there is a ∈ ∪S with x ∈ F_a iff there is C ∈ S and a ∈ C with x ∈ F_a iff there is C ∈ S with x ∈ ∪_{a ∈ C} F_a iff x ∈ ∪_{C ∈ S}(∪_{a ∈ C} F_a). For ∩, replace "there is" by "for every" throughout; the hypothesis that S and its members are nonempty is what keeps every ∩ defined.

**3.11** De Morgan: x ∈ B − ∪ F_a iff x ∈ B and for no a is x ∈ F_a iff for every a, x ∈ B − F_a iff x ∈ ∩(B − F_a); the other law swaps ∪ and ∩ and "for no" with "for some a, x ∉". Distributive: x ∈ (∪F_a) ∩ (∪G_b) iff some a has x ∈ F_a and some b has x ∈ G_b iff some pair (a, b) has x ∈ F_a ∩ G_b; dually for ∩ and ∪. These are [the laws of the algebra of sets](../algebra_of_sets/README.md) with "for some" in place of ∨ and "for every" in place of ∧, which is the [quantifier distribution](../../11_Logic/predicates_and_quantifiers/README.md) that holds.

**3.12** f[∪F_a] = ∪f[F_a]: y is the image of some x in some F_a, either way round. f⁻¹[∪F_a] = ∪f⁻¹[F_a] and f⁻¹[∩F_a] = ∩f⁻¹[F_a]: as in 3.6, f(x) is one value, so "f(x) ∈ every F_a" and "x ∈ every f⁻¹[F_a]" are the same sentence. f[∩F_a] ⊆ ∩f[F_a]: if x is in every F_a then f(x) is in every f[F_a]. Equality fails when f merges: f = {(1, 1), (2, 1)}, A = {1}, B = {2} gives f[A ∩ B] = ∅ and f[A] ∩ f[B] = {1}, the program's example; it holds when f is one-to-one, because then y ∈ every f[F_a] has one preimage, which must lie in every F_a.

**3.13** Follow the hint. ⊇: for f ∈ B^A, F_{a, f(a)} ⊆ ∪_b F_{a, b}, so ∩_a F_{a, f(a)} ⊆ ∩_a ∪_b F_{a, b} = L. ⊆: take x ∈ L; for each a some b has x ∈ F_{a, b}, and by the disjointness hypothesis exactly one, so a ↦ that b is a function f on A into B, and x ∈ ∩_a F_{a, f(a)} ⊆ R. This is the law of [predicates and quantifiers](../../11_Logic/predicates_and_quantifiers/README.md) that ∀a ∃b becomes ∃f ∀a: a choice for each a is a function, and here no axiom of choice is needed because the b is unique.

**4.1** The program's table gives the verdicts; the arguments are one line each. (a) x > y: not reflexive (x > x fails), not symmetric (3 > 2 but not 2 > 3), transitive. (b) n | m on ℤ: reflexive (n = n · 1), not symmetric (2 | 4, not 4 | 2), transitive (m = nk, p = ml give p = n(kl)). (c) x ≠ y: not reflexive, symmetric, not transitive (1 ≠ 2, 2 ≠ 1, but 1 = 1). (d) ⊆: reflexive, not symmetric, transitive, and antisymmetric, so an ordering; ⊂: not reflexive, not symmetric, transitive. (e) ∅ in ∅: reflexive, symmetric and transitive, all vacuously, since there is no element to fail them. (f) ∅ in a nonempty A: not reflexive (a ∅ a fails for a ∈ A), symmetric and transitive vacuously.

**4.2** This is the kernel of f, done in full on [equivalence relations and partitions](../equivalence_and_partitions/README.md): E = ker(f) is an equivalence; φ([a]) = f(a) is well defined because [a] = [a′] means f(a) = f(a′); and φ ∘ j = f is the decomposition theorem.

**4.3** (r, γ) ~ (r′, γ′) when r = r′ and γ − γ′ ∈ 2πℤ is reflexive (0 is a multiple), symmetric (negate the multiple) and transitive (add two multiples). In each class there is exactly one pair with 0 ≤ γ < 2π: subtract the right multiple of 2π to land in [0, 2π), and two such angles that differ by a multiple of 2π are equal. The set of these pairs is a set of representatives, and it is the reason a polar angle is reported in [0, 2π).

### Sullivan, *Precalculus* section 2.1: functions from a precalculus book

The owner sent the exercises of Sullivan's section 2.1 and asked for them here with solutions. They are the same definition as Hrbacek and Jech's, met in a precalculus book: a function is a set of pairs with no first member twice, and three kinds of exercise follow from it. The program's sections S1 to S3 check every answer before the solution is read.

**Problems 19 to 22, mapping diagrams.** The arrows are the pairs. *One test.* 19, person → birthday, is a function: two people share March 15, which is allowed. 20, father → daughter, is not: Bob has two arrows. 21, education → income, is a function, and one-to-one. 22, hours → salary, is not: 20 hours has two salaries. Domain and range are the left and right columns, with repeats dropped.

**Problems 23 to 30, sets of ordered pairs.** *One test, read off the first coordinates.* 23: 2 appears with 6 and with 10, not a function. 24: domain {−2, −1, 3, 4}, range {3, 5, 7, 12}, a function. 25: domain {0, 1, 2, 3}, range {−2, 3, 7}, a function. 26: every pair ends in 3; domain {1, 2, 3, 4}, range {3}, a function, the constant one. 27: −4 appears with 4 and with 0, not a function. 28: 3 appears with 3 and with 5, not a function. 29: domain {−2, −1, 0, 1}, range {3, 4, 16}, a function. 30: domain {−1, 0, 2, 4}, range {−1, 3, 8}, a function.

**Problems 31 to 42, equations.** *Solve for y; if the solving gives two values for one x, it is not a function of x.* The program refutes by finding such an x on a grid and confirms the others on the grid; the reasons for every real x are: 31 y = x³, 32 y = 2x² − 3x + 4, 33 y = |x| and 40 y = ∛x compute one y from each x, functions. 34 y = 1/x is a function with domain x ≠ 0. 35 y = ±√(1 − 2x) is not: x = 0 gives y = 1 and y = −1. 36 x² = 8 − y² gives y = ±√(8 − x²), not a function (x = 2 gives ±2). 37 x = y² gives y = ±√x, not (x = 4 gives ±2). 38 x + y² = 1 gives y = ±√(1 − x), not (x = 0 gives ±1). 39 y = (3x − 1)/(x + 2) is a function with domain x ≠ −2. 41 x² − 4y² = 1 gives y = ±½√(x² − 1), not (x = 2 gives ±√3/2, and on the grid x = 5/4 gives ±3/8). 42 |y| = 2x + 3 gives y = ±(2x + 3), not (x = 0 gives ±3). The vertical-line test of the book's summary is this move drawn: a vertical line is one x, and two crossings are two y's.

**Example 9 and problems 51 to 58, the domain of a function defined by an equation.** Sullivan's definition: the largest set of real numbers for which f(x) is a real number. *Start from all reals, exclude a zero denominator and a negative radicand, nothing else.* 9(a) x² + 5x: all reals. 9(b) 3x/(x² − 4): x² − 4 = (x − 2)(x + 2), so x ≠ −2, x ≠ 2. 9(c) √(4 − 3t): 4 − 3t ≥ 0, so t ≤ 4/3, the interval (−∞, 4/3]. 9(d) √(3x + 12)/(x − 5): 3x + 12 ≥ 0 and x − 5 ≠ 0, so x ≥ −4 and x ≠ 5. 51 and 52, polynomials: all reals. 53 x²/(x² + 1) and 54 (x + 1)/(2x² + 8): the denominators are never zero, since a square plus a positive number is positive, so all reals; this is the trap, a fraction whose domain is everything. 55 x/(x² − 16): x ≠ ±4. 56 2x/(x² − 4): x ≠ ±2. 57 (x + 4)/(x³ − 4x): x³ − 4x = x(x − 2)(x + 2), so x ≠ 0, ±2. 58 (x − 2)/(x³ + x): x³ + x = x(x² + 1), so x ≠ 0 only. The program evaluates each formula exactly on 40 rational points and checks that f(x) exists precisely where the claimed domain says.

**Concepts 10 to 14.** 10, the domain of f/g is the numbers in both domains with g(x) ≠ 0: true. 11, every relation is a function: false, problem 20 is a relation that is not. 12, four ways to express a relation: words, a mapping, a set of ordered pairs, an equation (and, on this library's page, a dictionary). 13, if no domain is given it is the set of reals: false as stated, it is the largest set of reals for which f(x) is real, which problem 55 shows is not all of them. 14, x not in the domain means f is not defined at x: true.

**8 and 9, multiple choice.** The set of all images is the range (a); the independent variable is the argument (c).

## What the program prints

<!-- output:function_katas -->
*Verified output of [`function_katas.py`](examples/function_katas.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
3.1  IF ran f ⊆ dom g THEN dom(g ∘ f) = dom f
     pairs of partial functions on {1, 2, 3} with ran f ⊆ dom g: 2530; dom(g ∘ f) == dom f in all: True
     without the hypothesis it fails, e.g. f = {(1, 1), (2, 1), (3, 1)}, g = {(2, 1), (3, 1)}: dom(g ∘ f) = ∅

3.2  THE FOUR COMPOSITIONS OF f1 = 2x − 1, f2 = √x (x > 0), f3 = 1/x (x ≠ 0)
               formula      domain    range      values at x = 1/2, 5/2, 1, 4, 9/4, 0, -1, 1/4
     f2 ∘ f1   √(2x − 1)    x ≥ 1/2   [0, ∞)     —, 2, 1, —, —, —, —, —
     f1 ∘ f2   2√x − 1      x > 0     (−1, ∞)    —, —, 1, 3, 2, —, —, 0
     f3 ∘ f1   1/(2x − 1)   x ≠ 1/2   ℝ ∖ {0}    —, 1/4, 1, 1/7, 2/7, -1, -1/3, -2
     f1 ∘ f3   2/x − 1      x ≠ 0     ℝ ∖ {−1}   3, -1/5, 1, -1/2, -1/9, —, -3, 7
     — marks a point outside the domain: dom(g ∘ f) = {x ∈ dom f : f(x) ∈ dom g} (Theorem 3.5).

3.3  f1, f2, f3 ARE ONE-TO-ONE; THEIR INVERSES
     f1⁻¹(y) = (y + 1)/2 on ℝ:        f1⁻¹∘f1 = id and f1∘f1⁻¹ = id on samples: True
     f2⁻¹(y) = y² on (0, ∞):          same, on perfect squares: True
     f3⁻¹(y) = 1/y on ℝ ∖ {0}:       same (f3 is its own inverse): True
     dom f_i = ran f_i⁻¹ and ran f_i = dom f_i⁻¹: ℝ and ℝ; (0, ∞) and (0, ∞); ℝ∖{0} twice.

3.4  INVERTIBLE MEANS A TWO-SIDED INVERSE; A ONE-SIDED ONE IS NOT ENOUGH
     (a) for every one-to-one f (34 of them): f⁻¹∘f = Id_dom f and f∘f⁻¹ = Id_ran f: True
     (b) g∘f = Id_dom f forces f one-to-one and g↾ran f = f⁻¹, all pairs: True
         but f∘h = Id_ran f does not: f = {(1, 1), (2, 1), (3, 1)}, h = {(1, 1)}, f∘h = {(1, 1)}, f not one-to-one

3.5  COMPOSITION OF ONE-TO-ONE FUNCTIONS, AND (g∘f)⁻¹ = f⁻¹∘g⁻¹
     all 1156 pairs of one-to-one f, g: True   (the order reverses: socks on, shoes on; shoes off, socks off)

3.6  INVERSE IMAGES UNDER A FUNCTION RESPECT ∩ AND −  (RELATIONS ONLY RESPECT ∪)
     (a) f⁻¹[A ∩ B] = f⁻¹[A] ∩ f⁻¹[B]: True   (b) f⁻¹[A − B] = f⁻¹[A] − f⁻¹[B]: True   (4096 cases each)
     the same with an arbitrary relation in place of f: False   — a function sends x to ONE value, a relation may not

3.7  f ∩ A² VERSUS f ↾ A
     f = {(1, 1), (2, 1), (3, 1)}, A = {2}: f ↾ A = {(2, 1)} but f ∩ A² = ∅
     the restriction keeps a pair whose value lies outside A; the intersection with A² does not.

3.12 IMAGES AND INVERSE IMAGES OF UNIONS AND INTERSECTIONS
     f[∪] = ∪f[]: True   f⁻¹[∪] = ∪f⁻¹[]: True   f[∩] ⊆ ∩f[]: True   f⁻¹[∩] = ∩f⁻¹[]: True
     f[∩] = ∩f[] when f is one-to-one: True; in general not, e.g. f = {(1, 1), (2, 1)}, A = {1}, B = {2}:
     f[A ∩ B] = ∅, f[A] ∩ f[B] = {1}

4.1  REFLEXIVE, SYMMETRIC, TRANSITIVE? SIX RELATIONS, CHECKED ON A FINITE PIECE
     relation               reflexive symmetric transitive   note
     (a) x > y on ℤ             False     False       True   
     (b) n divides m on ℤ        True     False       True   not antisymmetric on ℤ: 1 | −1 and −1 | 1
     (c) x ≠ y on ℕ             False      True      False   
     (d) ⊆ on 𝒫({1, 2})          True     False       True   
     (d) ⊂ on 𝒫({1, 2})         False     False       True   
     (e) ∅ in ∅                  True      True       True   all three hold vacuously: no element to fail them
     (f) ∅ in {1, 2}            False      True       True   1 is not related to 1, so not reflexive; the other two are vacuous
     A finite piece can refute a property, never confirm it; the page gives the arguments.

S1   SULLIVAN 2.1, PROBLEMS 19 TO 30: IS THE RELATION A FUNCTION?
     19 person → birthday     dom 4, ran 3   function: True 
     20 father → daughter     dom 3, ran 4   function: False   Bob is paired twice
     21 education → income    dom 5, ran 5   function: True 
     22 hours → salary        dom 3, ran 4   function: False   20 h is paired twice
     23                       dom 3, ran 3   function: False   2 is paired twice
     24                       dom 4, ran 4   function: True 
     25                       dom 4, ran 3   function: True 
     26                       dom 4, ran 1   function: True 
     27                       dom 4, ran 5   function: False   -4 is paired twice
     28                       dom 3, ran 4   function: False   3 is paired twice
     29                       dom 4, ran 3   function: True 
     30                       dom 4, ran 3   function: True 
     One test for a diagram and for a set of pairs: no first member twice.

S2   SULLIVAN 2.1, PROBLEMS 31 TO 42: DOES THE EQUATION DEFINE y AS A FUNCTION OF x?
     31 y = x³                every x on the grid has at most one y: a function of x
     32 y = 2x² − 3x + 4      every x on the grid has at most one y: a function of x
     33 y = |x|               every x on the grid has at most one y: a function of x
     34 y = 1/x               every x on the grid has at most one y: a function of x
     35 y = ±√(1 − 2x)        x = -4 has y ∈ {-3, 3}: not a function of x
     36 x² = 8 − y²           x = -2 has y ∈ {-2, 2}: not a function of x
     37 x = y²                x = 1/4 has y ∈ {-1/2, 1/2}: not a function of x
     38 x + y² = 1            x = -3 has y ∈ {-2, 2}: not a function of x
     39 y = (3x − 1)/(x + 2)  every x on the grid has at most one y: a function of x
     40 y = ∛x                every x on the grid has at most one y: a function of x
     41 x² − 4y² = 1          every x on the grid has at most one y: a function of x
     42 |y| = 2x + 3          x = -5/4 has y ∈ {-1/2, 1/2}: not a function of x
     The grid is quarter-integers from −4 to 4; a second y refutes, a single y on
     the grid is evidence, and the solutions say why it holds for every real x.

S3   SULLIVAN 2.1, EXAMPLE 9 AND PROBLEMS 51 TO 58: THE DOMAIN OF f DEFINED BY AN EQUATION
     9(a) x² + 5x               all reals                f(x) exists iff claimed, on 40 points: True   excluded: none
     9(b) 3x/(x² − 4)           x ≠ −2, x ≠ 2            f(x) exists iff claimed, on 40 points: True   excluded: -2, 2
     9(c) √(4 − 3t)             t ≤ 4/3                  f(x) exists iff claimed, on 40 points: True   excluded: 5/3, 2, 7/3, 8/3, 3, 10/3, 11/3, 4, 13/3, 14/3, 5, 16/3, 17/3, 6
     9(d) √(3x + 12)/(x − 5)    x ≥ −4, x ≠ 5            f(x) exists iff claimed, on 40 points: True   excluded: -6, -17/3, -16/3, -5, -14/3, -13/3, 5
     51 x² + 2                  all reals                f(x) exists iff claimed, on 40 points: True   excluded: none
     52 −5x + 4                 all reals                f(x) exists iff claimed, on 40 points: True   excluded: none
     53 x²/(x² + 1)             all reals: x² + 1 > 0    f(x) exists iff claimed, on 40 points: True   excluded: none
     54 (x + 1)/(2x² + 8)       all reals: 2x² + 8 > 0   f(x) exists iff claimed, on 40 points: True   excluded: none
     55 x/(x² − 16)             x ≠ −4, x ≠ 4            f(x) exists iff claimed, on 40 points: True   excluded: -4, 4
     56 2x/(x² − 4)             x ≠ −2, x ≠ 2            f(x) exists iff claimed, on 40 points: True   excluded: -2, 2
     57 (x + 4)/(x³ − 4x)       x ≠ −2, 0, 2             f(x) exists iff claimed, on 40 points: True   excluded: -2, 0, 2
     58 (x − 2)/(x³ + x)        x ≠ 0: x² + 1 > 0        f(x) exists iff claimed, on 40 points: True   excluded: 0
     Two reasons only, as the book's box says: a zero denominator and a negative radicand.
```
<!-- /output -->

## Po polsku, w skrócie

Zadania po pierwszym rozdziale o funkcjach robi się trzema ruchami: pogonią za elementem przez definicje, dwoma zawieraniami dla równości zbiorów i najmniejszym kontrprzykładem tam, gdzie zawieranie nie jest równością. Strona zawiera zadania 3.1–3.13 i 4.1–4.3 z rozdziału 2 książki Hrbacka i Jecha z rozwiązaniami, a program sprawdza każdą tezę na wszystkich 64 funkcjach częściowych na {1, 2, 3} i liczy dokładnie złożenia oraz odwrotności funkcji 2x − 1, √x i 1/x. Najważniejsze wnioski: dziedzina złożenia g ∘ f to te x z dziedziny f, dla których f(x) leży w dziedzinie g; lewa odwrotność wymusza różnowartościowość, prawa nie; (g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹ w odwróconej kolejności; przeciwobrazy przy funkcji zachowują ∩ i −, obrazy tylko ∪, bo funkcja daje jedną wartość, a relacja może dawać wiele. Zadanie 4.2 to jądro funkcji ze strony o relacjach równoważności, a 4.3 tłumaczy, czemu kąt biegunowy podaje się z przedziału [0, 2π).

Na końcu są zadania z rozdziału 2.1 *Precalculus* Sullivana, ta sama definicja funkcji poziom niżej: diagramy ze strzałkami i zbiory par (jeden test: żaden pierwszy element dwa razy), równania (rozwiąż względem y; dwie wartości dla jednego x to nie funkcja) i dziedzina funkcji zadanej wzorem (wszystkie liczby rzeczywiste poza zerem w mianowniku i ujemną liczbą pod pierwiastkiem). Program sprawdza każdą odpowiedź, zanim przeczyta się rozwiązanie.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 04_Sets/function_katas/examples/function_katas.py
```

## See also

- [Relations and functions are sets of pairs](../relations_and_functions/README.md) — the definitions the exercises use, and Hrbacek and Jech's exercises 2.3 and 2.4 on images
- [Equivalence relations, partitions and the kernel of a function](../equivalence_and_partitions/README.md) — exercise 4.2 in full
- [Set katas](../set_katas/README.md) and [axiom katas](../../13_Axioms_of_Set_Theory/axiom_katas/README.md) — the other exercise pages
- Karel Hrbacek and Thomas Jech, *Introduction to Set Theory* (3rd ed., Marcel Dekker, 1999), chapter 2, sections 3 and 4
- Michael Sullivan, *Precalculus* (Pearson), section 2.1 *Functions*, Example 9 and problems 8 to 14, 19 to 42 and 51 to 58; the four pictures of a function are compared on [relations and functions](../relations_and_functions/README.md#functions-versus-sets-sullivans-four-pictures)
