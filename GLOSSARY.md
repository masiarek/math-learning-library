# Glossary

Terms used across the library, with the page that explains each in full. For set theory beyond what is here, [the terms map](reading_guides/set_theory_terms/README.md) takes the owner's list of some 700 terms and says which have a page or an entry, and which book treats the rest.

**Abelian group** — a group whose operation is commutative, named after Niels Henrik Abel. The integers under +, the vectors under +, and the nonzero fractions under × are abelian; the invertible 2 × 2 matrices under × are not. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).
{ #abelian-group }

**Abscissa** — the x-coordinate of a point: its signed distance from the y-axis, positive to the right of it and negative to the left. The y-coordinate is the *ordinate*. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).
{ #abscissa }

**Absolute error** — |x − x̂|, the difference between a value and the truth, in the value's own units (`±0.05 cm`). What `+` and `−` propagate. Defined in [relative error and correct digits](01_Precision/relative_error/README.md); propagated in [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).
{ #absolute-error }

**Aleph, beth and the continuum (ℵ, ℶ, 𝔠)** — ℵ₀ is the size of ℕ, ℵ₁ the next infinite size, ℵ_α the α-th; ℶ₀ = ℵ₀, ℶ₁ = |𝒫(ℕ)| = |ℝ| = 𝔠, the continuum, and ℶ_{n+1} = 2^ℶₙ; the continuum hypothesis is ℵ₁ = ℶ₁, which Gödel and Cohen showed the axioms cannot decide. κ⁺ is the next cardinal after κ, and the gimel function ℷ(κ) = κ^cf(κ) is always larger than κ (König). See [cardinality](04_Sets/cardinality/README.md) and the [reading guide](reading_guides/set_theory/README.md#the-founding-papers).
{ #aleph-beth-and-the-continuum-c }

**Almost everywhere** — everywhere except on a set of measure zero. The Cantor function's slope is 0 almost everywhere, and the function still climbs from 0 to 1, so an almost-everywhere fact can miss the thing that matters. Probability's name for the same idea is *almost surely*. See [the Cantor function](02_Measure_Zero/cantor_function/README.md).
{ #almost-everywhere }

**Almost surely** — with probability 1, which is not the same as certainly: the exceptions exist, and together they have measure zero. A number drawn at random from [0, 1] is almost surely irrational. See [probability zero](02_Measure_Zero/probability_zero/README.md).
{ #almost-surely }

**Altitude** — of a triangle, the height measured at a right angle to the base, from the base to the opposite corner. Not a side unless the triangle is right; for a slanted triangle it is shorter than the slanted sides. Area = ½ · base · altitude. See [area and volume formulas](10_Geometry/area_and_volume_formulas/README.md).
{ #altitude }

**Antisymmetric relation** — x R y and y R x together force x = y: no reversed pair unless the two elements coincide. ≤ and ⊆ are antisymmetric, which is why a ⊆ b and b ⊆ a prove a = b. See [orderings](04_Sets/orderings/README.md).
{ #antisymmetric-relation }

**Arithmetic mean** — the sum of the numbers divided by how many there are; what school calls "the mean" or "the average", and a spreadsheet `AVERAGE`. The one number that can replace every value without changing their sum, so the distances above and below it cancel. The adjective tells it apart from the geometric and harmonic means. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).
{ #arithmetic-mean }

**Associative** — (a · b) · c = a · (b · c): the grouping does not change the answer, so a chain of the operation needs no brackets. True for integer addition, string concatenation and composition of functions; false for subtraction and for float addition. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).
{ #associative }

**Asymmetric relation** — x R y forbids y R x: no reversed pair at all, which makes the relation irreflexive too. < and "is a descendant of" are asymmetric. See [orderings](04_Sets/orderings/README.md).
{ #asymmetric-relation }

**Average** — any single value that stands for a whole set. In everyday speech it almost always means the arithmetic mean, but in statistics the median and the mode are averages too, so "the average salary" can honestly be three different numbers. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).
{ #average }

**Axiom (of set theory)** — one of the sentences of Zermelo and Fraenkel that say which sets exist: extensionality, pairs, unions, power set, comprehension, replacement, infinity, foundation, and choice (ZFC). Except for extensionality each says "there is a set whose members are …", so each is a demand on the universe, not a description of it, and a small universe can fail it. See [the axioms chapter](13_Axioms_of_Set_Theory/README.md).
{ #axiom-of-set-theory }

**Axiom of choice** — for every family of nonempty sets there is a choice function, one that picks a member of each; equivalently a product of nonempty sets is nonempty. A theorem for finite families, unnecessary when a rule exists, and independent of the other axioms (Gödel 1938, Cohen 1963). See [choice](13_Axioms_of_Set_Theory/choice/README.md).
{ #axiom-of-choice }

**Banach–Tarski theorem** — a solid ball can be cut into finitely many pieces (five suffice, Robinson 1947) that rotations and translations reassemble into two balls the size of the original. Not a paradox: the pieces are sets chosen with the axiom of choice and have no volume. See [two balls from one](13_Axioms_of_Set_Theory/two_balls_from_one/README.md).
{ #banachtarski-theorem }

**Bell number** — B(n), the number of partitions of an n-set, equally the number of equivalence relations on it: 1, 1, 2, 5, 15, 52, 203, …; the sum of the Stirling numbers of a row, and the left edge of the Bell triangle. See [equivalence relations and partitions](04_Sets/equivalence_and_partitions/README.md).
{ #bell-number }

**Bijection** — a function that is both one-to-one (injective: different inputs, different outputs) and onto (surjective: every member of the target is hit), so every target is hit exactly once and the function can be undone; also called a one-to-one correspondence, which is not the same as "one-to-one". Two sets have the same cardinality exactly when a bijection runs between them; on a finite set the three properties agree. See [relations and functions](04_Sets/relations_and_functions/README.md) and [cardinality](04_Sets/cardinality/README.md).
{ #bijection }

**Bloom's taxonomy** — six levels of working with an idea, in the 2001 revision: remembering, understanding, applying, analyzing, evaluating, creating (in 1956: knowledge, comprehension, application, analysis, synthesis, evaluation). See [studying vs learning ↗](https://masiarek.github.io/learning-to-learn-library/01_Knowing_What_You_Know/studying_vs_learning/).
{ #bloom-s-taxonomy }

**Boolean algebra** — a set with two operations + and ·, a complement −, and constants 0 and 1, satisfying commutativity, associativity, distributivity, absorption and complementation; the subsets of any set under ∪, ∩ and complement are one, and so is the two-valued logic of true and false. The structure that [the algebra of sets](04_Sets/algebra_of_sets/README.md) and [truth tables](11_Logic/truth_tables_and_laws/README.md) share. See [choice](13_Axioms_of_Set_Theory/choice/README.md#the-equivalent-forms-and-the-weaker-ones).
{ #boolean-algebra }

**Brier score** — the mean of (confidence − outcome)², with outcome 1 for right and 0 for wrong: 0 is perfect, and saying 50% every time scores 0.25. It is a proper scoring rule, so its expected value is smallest when you report what you really believe. See [metacognition ↗](https://masiarek.github.io/learning-to-learn-library/01_Knowing_What_You_Know/metacognition/).
{ #brier-score }

**Calibration** — how well confidence matches results: a calibrated learner's 90% answers are right about 9 times in 10. See [metacognition ↗](https://masiarek.github.io/learning-to-learn-library/01_Knowing_What_You_Know/metacognition/).
{ #calibration }

**Cantor function** — also the *devil's staircase*. Read x in base 3, cut after the first 1, turn 2s into 1s, and read the result in base 2. Continuous, climbing from 0 to 1, and flat on every gap of the Cantor set, so its whole rise happens on a set of length 0. See [the Cantor function](02_Measure_Zero/cantor_function/README.md).
{ #cantor-function }

**Cantor–Schröder–Bernstein theorem** — if there are one-to-one maps A → B and B → A, there is a bijection between A and B; so |A| ≤ |B| and |B| ≤ |A| give |A| = |B|, and ≤ on sizes is antisymmetric without the axiom of choice. The proof traces each element's ancestors through the two maps. See [Cantor–Schröder–Bernstein](04_Sets/schroeder_bernstein/README.md).
{ #cantor-schr-der-bernstein-theorem }

**Cardinality** — |A|, the size of a set. For a finite set, the number of members; in general, defined by matching: |A| = |B| when the members can be paired one to one with none left over. The same bars around a number mean absolute value. |A × B| = |A| · |B|; |ℕ| = |even numbers| = ℵ₀; |ℝ| is strictly larger. See [cardinality](04_Sets/cardinality/README.md).
{ #cardinality }

**Cantor set** — what survives when the open middle third of [0, 1] is deleted, then the middle third of every piece left, forever. Uncountably many points and total length 0; exactly the numbers that can be written in base 3 with only 0s and 2s. See [the Cantor set](02_Measure_Zero/cantor_set/README.md).
{ #cantor-set }

**Cartesian plane** — the plane with a pair of perpendicular number lines chosen in it, so that every point is an ordered pair (x, y). Also the *coordinate plane* and the *xy-plane*; the coordinates themselves are *rectangular* or *Cartesian*. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).
{ #cartesian-plane }

**Cartesian product** — A × B, the set of every ordered pair (a, b) with a ∈ A and b ∈ B. It has |A| · |B| members, includes pairs with a repeated entry, and is not commutative: A × B and B × A share no member unless A = B. ℝ × ℝ = ℝ² is the coordinate plane. See [the Cartesian product](04_Sets/cartesian_product/README.md).
{ #cartesian-product }

**Catastrophic cancellation** — the loss of most significant figures when two nearly equal numbers are subtracted. It does not create error; it removes the leading digits that were hiding error already present. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).
{ #catastrophic-cancellation }

**Category** — a collection of objects and arrows between them, with a composition of arrows that is associative and has identities. Sets with functions, groups with homomorphisms, and vector spaces with linear maps are categories. See [maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md).
{ #category }

**Cayley graph** — of a group with chosen generators: a vertex for each element and an edge labelled g from ρ to gρ for each generator g. Halbeisen labels the vertices of the Cayley graph of Hausdorff's rotation group with ❶, ❷, ❸ so that the three label classes satisfy B = ψ[A], C = ψ⁻¹[A] and B ∪ C = φ[A]. See [two balls from one](13_Axioms_of_Set_Theory/two_balls_from_one/README.md#the-labelled-cayley-graph).
{ #cayley-graph }

**Chain and antichain** — in a poset, a chain is a subset on which every two elements are comparable, an antichain one in which no two are: under divisibility, 1, 2, 4, 8 is a chain and the primes an antichain. See [orderings](04_Sets/orderings/README.md).
{ #chain-and-antichain }

**Chain rule** — the rule for the velocity of a function of a function. The case the talk uses: e^(kt) is the motion e^t on a clock running k times as fast, and speeding up the clock by k multiplies every velocity by k, so d/dt e^(kt) = k · e^(kt). See [velocity equals position](09_Calculus/velocity_equals_position/README.md).
{ #chain-rule }

**Circle** — the set of points at a fixed distance r, the radius, from a fixed point (h, k), the center. Its equation is the distance formula held fixed: (x − h)² + (y − k)² = r². See [circles](08_Analytic_Geometry/circles/README.md).
{ #circle }

**Class** — a collection given by a formula, {x : F[x]}, which may or may not be a set. The class of all sets and the class of ordinals are **proper classes**, not sets; comprehension says a class cut down to a set is a set. See [comprehension](13_Axioms_of_Set_Theory/comprehension/README.md).
{ #class }

**Closed form** — a formula for a sum or sequence with no Σ and no "…": 1 + 2 + ⋯ + n = n(n + 1)/2. Found by guessing and proved by induction. See [induction](11_Logic/induction/README.md).
{ #closed-form }

**Closed under an operation** — a subset is closed under an operation when applying it to members of the subset always gives a member of the subset. The line y = 2x is closed under + and scaling; the half-plane x ≥ 0 is not closed under scaling by −1. See [subsets inherit the laws](06_Algebraic_Structures/subsets_inherit_the_laws/README.md).
{ #closed-under-an-operation }

**Codomain, image, range** — for f : S → T, the codomain is T, the image is the set of values actually taken, and "range" means the image in this library and in Jech but the codomain in many calculus and computer-science books. Surjective means image = codomain. See [relations and functions](04_Sets/relations_and_functions/README.md#the-three-words).
{ #codomain-image-range }

**Coefficient** — a fixed number standing in front of a variable in a linear combination: in 40h + 15c the coefficients are 40 and 15. In a system, aᵢ,ⱼ is the coefficient in equation i in front of variable j. Zero is allowed. See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md).
{ #coefficient }

**Commutative** — a · b = b · a: the order of the two inputs does not matter. True for adding and multiplying numbers; false for subtraction, string concatenation, matrix multiplication and composing maps. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).
{ #commutative }

**Comparable** — two elements a, b of a poset with a ≤ b or b ≤ a. In a linear order every pair is; under ⊆, {1} and {2} are not. See [orderings](04_Sets/orderings/README.md).
{ #comparable }

**Complement** — A′, the members of a fixed universal set U that are not in A: A′ = U ∖ A; also written Ā or Aᶜ. It has no meaning without U, since there is no set of everything; in Python it is `U - a`. See [the algebra of sets](04_Sets/algebra_of_sets/README.md).
{ #complement }

**Completing the square** — rewriting x² + ax as (x + a/2)² − (a/2)², by adding half the coefficient squared to both sides. It turns the general form of a circle back into the standard form. See [circles](08_Analytic_Geometry/circles/README.md).
{ #completing-the-square }

**Complex multiplication** — the rule (x₁, y₁) · (x₂, y₂) = (x₁x₂ − y₁y₂, x₁y₂ + x₂y₁) on pairs of reals. It is the whole definition of the complex numbers: i is the pair (0, 1), and i² = −1 is what the rule gives for (0, 1) · (0, 1). See [multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md).
{ #complex-multiplication }

**Complex multiplication, geometrically** — multiplying by a point z scales the plane by the distance of z from the origin and turns it by the angle of z. Lengths multiply, angles add. So (0, 1) is a quarter turn and i² = −1 says two quarter turns are a half turn. See [multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md).
{ #complex-multiplication-geometrically }

**Componentwise relative error** — for vectors, the largest of the individual relative errors, max |xᵢ − x̂ᵢ| / |xᵢ|. A normwise relative error ‖x − x̂‖ / ‖x‖ can report four correct digits while a small component is 10% wrong; this measure cannot. See [relative error and correct digits](01_Precision/relative_error/README.md).
{ #componentwise-relative-error }

**Comprehension (separation, subset axiom)** — for every set a and formula F there is a set {x ∈ a : F[x]}; Python's `{x for x in a if F(x)}`. A scheme, one axiom per formula. Without the "x ∈ a" it is Cantor's comprehension principle and contradicts itself (Russell). See [comprehension](13_Axioms_of_Set_Theory/comprehension/README.md).
{ #comprehension-separation-subset-axiom }

**Conditioning** — how much a problem's output changes for a small change in its input. A property of the *problem*, not of any algorithm; an ill-conditioned problem defeats every method. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).
{ #conditioning }

**Congruent triangles** — triangles with every pair of corresponding sides and angles equal: the same triangle in two places. Three measurements prove it: SSS, SAS or ASA, never AAA or SSA. See [congruent and similar triangles](10_Geometry/congruent_and_similar_triangles/README.md).
{ #congruent-triangles }

**Connectives (¬, ∧, ∨, ⇒, ⇔)** — the symbols that build statements from statements: ¬ not, ∧ and, ∨ or (inclusive), ⇒ implies (also →), ⇔ if and only if (also ↔), and ⇏ for "does not imply". Each is defined by its truth table, and the laws of the algebra of sets are their laws read through membership: ∪ is ∨, ∩ is ∧, complement is ¬. See [truth tables and laws](11_Logic/truth_tables_and_laws/README.md).
{ #connectives }

**Contrapositive** — of "if A then B", the statement "if not B then not A". It is false in exactly the same case as the original, A true and B false, so it is the same claim. See [if A then B](11_Logic/converse_and_contrapositive/README.md).
{ #contrapositive }

**Converse** — the statement with its *if* and *then* swapped. It must be proved on its own: "a dog has four legs" is true and its converse is not. The converse of the Pythagorean theorem happens to be true, which turns c² = a² + b² into a test for a right angle. See [if A then B](11_Logic/converse_and_contrapositive/README.md) and [the Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md).
{ #converse }

**Correct rounding** — returning exactly what the chosen rounding function gives for the exact result, as if the operation had been carried out with unlimited precision. IEEE 754 requires it for +, −, ×, ÷ and √, which is why those give the same bits on every conforming machine. See [machine numbers](01_Precision/machine_numbers/README.md).
{ #correct-rounding }

**Correct significant digits** — a count with only p + 1 possible values and two competing definitions: x and x̂ round to the same p-digit number, or |x − x̂| is under half a unit in the p-th digit of x. The first is not monotone (0.9949 and 0.9951 agree to one and three digits but not two); the second calls 0.123 and 0.127 two-digit agreement. The relative error is the precise measure. See [relative error and correct digits](01_Precision/relative_error/README.md).
{ #correct-significant-digits }

**Countable** — able to be written as a list — a first, a second, a third — with every member somewhere in it; equivalently, of cardinality ℵ₀ or finite. The whole numbers and the rationals are countable; [0, 1] is not. Every countable set has measure zero. See [countable sets](02_Measure_Zero/countable_sets/README.md) and [cardinality](04_Sets/cardinality/README.md).
{ #countable }

**Counterexample** — a case where the hypothesis of an "if A then B" holds and the conclusion fails. One is enough to disprove the statement; no number of examples proves it. See [if A then B](11_Logic/converse_and_contrapositive/README.md).
{ #counterexample }

**De Moivre's formula** — (cos A, sin A)ⁿ = (cos nA, sin nA): the n-th power of a unit point is the unit point at n times the angle. It is "angles add" applied n − 1 times, and its n = 2 and n = 3 cases are the double- and triple-angle formulas. See [roots of unity](03_Complex_Numbers/roots_of_unity/README.md).
{ #de-moivre-s-formula }

**De Morgan's laws** — (A ∪ B)′ = A′ ∩ B′ and (A ∩ B)′ = A′ ∪ B′; in logic, not (p or q) is (not p) and (not q). Not either is neither; not both is at least one missing. See [the algebra of sets](04_Sets/algebra_of_sets/README.md).
{ #de-morgan-s-laws }

**Derivative** — the velocity at an instant: the number that the average velocities (x(t + h) − x(t)) / h settle on as h shrinks, written d/dt x, x′(t) or dx/dt. For x = t² at t = 3 the averages are exactly 6 + h, so the derivative is 6. See [the derivative is a velocity](09_Calculus/derivative_as_velocity/README.md).
{ #derivative }

**Diagonal argument** — Cantor's proof that the infinite 0/1 sequences cannot be listed: flip the r-th bit of the r-th row and the result is on no row. It makes ℝ uncountable, and makes the functions from ℕ to {0, 1} outnumber the programs. See [cardinality](04_Sets/cardinality/README.md).
{ #diagonal-argument }

**Dense** — found inside every interval, however short. The rationals are dense in the line and still have measure zero. See [countable sets](02_Measure_Zero/countable_sets/README.md).
{ #dense }

**Dimension of a formula** — how many lengths each term multiplies together: one for a perimeter, two for an area, three for a volume. Scaling every length by k scales the result by k to that power, which catches a misremembered formula. See [area and volume formulas](10_Geometry/area_and_volume_formulas/README.md).
{ #dimension-of-a-formula }

**Disjoint** — two sets with no member in common: A ∩ B = ∅. In a Venn diagram, two circles drawn apart; in Python, `a.isdisjoint(b)`. See [the algebra of sets](04_Sets/algebra_of_sets/README.md).
{ #disjoint }

**Distance formula** — d(P₁, P₂) = √((x₂ − x₁)² + (y₂ − y₁)²), the Pythagorean theorem with the legs read off the coordinates. The squares erase the signs, so the order of the points does not matter. See [the distance formula](08_Analytic_Geometry/distance_formula/README.md).
{ #distance-formula }

**Distributive** — a × (b + c) = a × b + a × c, and (a + b) × c = a × c + b × c: the law that links two operations. It is what turns two groups on one set into a ring. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).
{ #distributive }

**Domain and range** — of a relation ρ, the set dom(ρ) of first entries of its pairs and the set ran(ρ) of second entries; Cori and Lascar write Im(f) for the range. See [relations and functions](04_Sets/relations_and_functions/README.md).
{ #domain-and-range }

**Empty set** — ∅, the set with no members. There is only one, because two sets with the same members are equal and any two empty sets have the same members: none. In Python it is `set()`, since `{}` is an empty dict. Some books call it the *null set*, but in measure theory a null set is any set of measure zero, which can be infinite. See [what is a set?](04_Sets/what_is_a_set/README.md).
{ #empty-set }

**End of proof (∎, □, QED)** — a filled or hollow square at the end of a proof, Halmos's tombstone, standing for the older *quod erat demonstrandum*, "which was to be shown". Halbeisen uses ⊣ for it. See [induction](11_Logic/induction/README.md) for proofs that end this way.
{ #end-of-proof-qed }

**Equidecomposable** — two sets of points are equidecomposable when each is cut into the same finite number of pieces, congruent in pairs (Halbeisen writes A ≃ A′, and A ≃ₙ A′ with at most n pieces). A ball is equidecomposable with two balls, in five pieces. See [two balls from one](13_Axioms_of_Set_Theory/two_balls_from_one/README.md).
{ #equidecomposable }

**Equivalence relation** — a relation that is reflexive, symmetric and transitive; its classes [u] partition the set, and every partition arises this way. Congruence mod m is the one everyone uses. See [equivalence relations and partitions](04_Sets/equivalence_and_partitions/README.md).
{ #equivalence-relation }

**Euler's formula** — e^{it} = (cos t, sin t): the exponential of an imaginary number is the unit point at angle t, in radians. It is what compounding gives, since (1 + it/n)ⁿ is n small turns whose angles add up to t while their stretches fade to nothing, and it is forced by the law e^{a+b} = e^a e^b, because multiplying unit points can only add angles. See [Euler's identity](03_Complex_Numbers/eulers_identity/README.md).
{ #euler-s-formula }

**Euler's identity** — e^{iπ} = −1, the t = π row of Euler's formula: the unit point half a turn from (1, 0) is (−1, 0). It is i² = −1 with the quarter turn cut finer, and the program reaches it exactly as (0, 1)², as (1, 1)⁴ / 4 and as the sixth power of the clock's first mark. `cmath.exp(1j * math.pi)` is not −1 but −1 + 1.2 × 10⁻¹⁶ i, because `math.pi` is not π. See [Euler's identity](03_Complex_Numbers/eulers_identity/README.md).
{ #euler-s-identity }

**Euler's number e** — 2.71828…, the number compound interest settles on, (1 + 1/n)ⁿ as n grows, and the position at time 1 of a point that starts at 1 and always moves with velocity equal to its position. Its power series is 1 + 1 + 1/2 + 1/6 + 1/24 + ⋯. See [velocity equals position](09_Calculus/velocity_equals_position/README.md).
{ #euler-s-number-e }

**Exact number** — one that was counted or defined rather than measured (ballots cast, inches per foot, π). Has infinitely many significant figures and never limits a calculation. See [exact vs approximate](01_Precision/exact_vs_approximate/README.md).
{ #exact-number }

**Extensionality** — the axiom that two sets with the same members are the same set. It is what "distinct objects" in the textbook definition is reaching for: {2, 5} = {5, 2} and {1, 1, 2} = {1, 2}, because order and repeats are not membership. See [what is a set?](04_Sets/what_is_a_set/README.md).
{ #extensionality }

**Fat Cantor set** — also the *Smith–Volterra–Cantor set*. Built like the Cantor set, but the gaps deleted at step n are 1/4ⁿ long. It contains no interval and still has length 1/2 — the proof that full of gaps does not mean measure zero. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).
{ #fat-cantor-set }

**Field** — a set with + and × in which both are commutative and associative, both have identities (0 and 1), every member has an inverse under + and every member except 0 has one under ×, and × distributes over +. The rationals, the reals and the complex numbers are fields; the integers are not, because 2 has no inverse. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).
{ #field }

**Filter and ultrafilter** — a filter on a set is a family of "large" subsets, closed under supersets and finite intersections and not containing ∅; an ultrafilter also decides every subset, A or its complement. On a finite set every ultrafilter is principal, the sets containing one fixed point; non-principal ones on ℕ exist by the axiom of choice and are the tool of ultrapowers and of several forcing arguments. No lesson here yet; the [reading guide](reading_guides/set_theory/README.md) names the books.
{ #filter-and-ultrafilter }

**Finer and coarser** — of two equivalence relations or partitions on one set, R is finer than T (and T coarser) when R ⊆ T, that is, every block of R lies inside a block of T. The identity is the finest, the one-block partition the coarsest, and all of them form a lattice: meet is intersection, join is the equivalence generated by the union. See [equivalence relations and partitions](04_Sets/equivalence_and_partitions/README.md#where-the-textbook-sections-live-here).
{ #finer-and-coarser }

**Finite character** — a family of sets has finite character when a set belongs to it exactly if every finite subset does; the linearly independent sets of vectors are the example. Teichmüller's principle, also Tukey's lemma: a nonempty family of finite character has a maximal member. Equivalent to the axiom of choice. See [choice](13_Axioms_of_Set_Theory/choice/README.md#the-equivalent-forms-and-the-weaker-ones).
{ #finite-character }

**Floating point** — the machine's stand-in for the real numbers: a finite set of exact values, fixed by a radix, a precision and an exponent range, with every result rounded into it. Its errors look like measurement errors and are unrelated to them: the value was known perfectly and the *hardware* could not hold it. What the set is, and which laws of arithmetic survive rounding into it, is [machine numbers](01_Precision/machine_numbers/README.md); how its bits are laid out is covered by the sibling Rust library ([What a float actually stores ↗](https://masiarek.github.io/rust-learning-library/19_Numbers/what_a_float_stores/index.html)); what happens when you subtract two of them is [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).
{ #floating-point }

**Foundation (regularity)** — every nonempty set has a member that shares no member with it. Hence no set is its own member, no membership chain descends forever, and every set has a rank. See [foundation](13_Axioms_of_Set_Theory/foundation/README.md).
{ #foundation-regularity }

**Free group** — all words in some letters and their inverses, with a letter cancelled against its inverse and nothing else; the group with no relations. The free group on two letters splits into four pieces which, two of them shifted by one letter, make two copies of the whole, and that is where the Banach–Tarski theorem lives. See [two balls from one](13_Axioms_of_Set_Theory/two_balls_from_one/README.md).
{ #free-group }

**Frozenset** — Python's immutable set. It cannot change after it is made, so it is hashable and can be a member of a set or a key of a dict; it has no `add`, and "adding" builds a new one with `union` or `|`. See [a set is a hash table ↗](https://masiarek.github.io/python-learning-library/04_Names_and_Objects/a_set_is_a_hash_table/index.html) in the Python library.
{ #frozenset }

**Function** — a relation in which each x has at most one partner y; f(x) names that y. A function is its set of pairs, the table of its values, not the formula that produced it, so x² and |x|² are one function. A Python dict is the same object. See [relations and functions](04_Sets/relations_and_functions/README.md).
{ #function }

**Geometric mean** — the n-th root of the product of n numbers: the one number that can replace every value without changing their product. The right mean for growth rates, which multiply: +100% then −50% is a geometric mean of 0% a year, not the arithmetic +25%. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).
{ #geometric-mean }

**Graph (directed, undirected)** — a relation drawn: a point for each member of the base set and an arrow from x to y for each pair (x, y). An undirected graph is a symmetric relation, or a set of two-element sets. A membership table x ∈ y is a directed graph too. See [relations and functions](04_Sets/relations_and_functions/README.md).
{ #graph-directed-undirected }

**Graph of an equation** — the set of all points (x, y) whose coordinates satisfy the equation. A point is on it exactly when substituting it makes the equation true. See [graphs of equations: intercepts and symmetry](08_Analytic_Geometry/graphs_intercepts_symmetry/README.md).
{ #graph-of-an-equation }

**Group** — a set with an operation that is associative, has an identity, and gives every member an inverse. The integers under +, the nonzero fractions under ×, the invertible matrices under ×, and the n-th roots of unity under × are groups. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).
{ #group }

**Harmonic mean** — n divided by the sum of the reciprocals of n numbers: the one number that keeps the sum of reciprocals. The right mean for speeds over equal distances; 30 km/h out and 60 km/h back averages 40 km/h, not 45. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).
{ #harmonic-mean }

**Hartogs' theorem** — for every set there is a well-ordered set that does not inject into it (Hartogs 1915), proved without the axiom of choice. It gives the least aleph not below a cardinal, and from it the comparability of any two cardinals is equivalent to choice. See [choice](13_Axioms_of_Set_Theory/choice/README.md#the-equivalent-forms-and-the-weaker-ones).
{ #hartogs-theorem }

**Hashable** — in Python, an object whose `hash` works and never changes while it is stored, which is what a set member or dict key must be. Lists, dicts and sets are not; ints, strings, frozensets, and tuples of hashables are. A tuple that holds a list is not, so the rule is hashable, not immutable. See [a set is a hash table ↗](https://masiarek.github.io/python-learning-library/04_Names_and_Objects/a_set_is_a_hash_table/index.html) in the Python library.
{ #hashable }

**Homomorphism** — a map f between two sets with operations that keeps the operation: f(a · b) = f(a) ∗ f(b). A linear map is one; so are n ↦ 2ⁿ, the logarithm, the determinant, and the length of a string. A homomorphism of groups sends the identity to the identity and inverses to inverses, which is why 2⁰ = 1, log 1 = 0, T(0) = 0 and det I = 1 are one theorem. See [maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md).
{ #homomorphism }

**Hypotenuse** — the side of a right triangle opposite the right angle; always the longest side, and the c in c² = a² + b². See [the Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md).
{ #hypotenuse }

**Hypothesis and conclusion** — the two parts of "if A then B": A is assumed, B follows. See [if A then B](11_Logic/converse_and_contrapositive/README.md).
{ #hypothesis-and-conclusion }

**Identity element** — a member e with a · e = e · a = a for every a: 0 for +, 1 for ×, the empty string for concatenation, the identity matrix for matrix multiplication. There is at most one, since two identities e and e′ give e = e · e′ = e′. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).
{ #identity-element }

**If and only if** — A ⇔ B: "if A then B" and its converse both hold, so A and B are always true together. Every definition is one; the Pythagorean theorem with its converse is one. See [if A then B](11_Logic/converse_and_contrapositive/README.md).
{ #if-and-only-if }

**Inclusion–exclusion** — |S ∪ T| = |S| + |T| − |S ∩ T|: the overlap was counted twice, so subtract it once. See [set katas](04_Sets/set_katas/README.md#from-ashlocks-problem-set).
{ #inclusion-exclusion }

**Induction (mathematical)** — a proof of P(n) for every natural number n from a base case P(0) and a step, P(n) implies P(n + 1). Valid because of the well-ordering principle: a failure would have a least case m, and the step from m − 1 forbids it. See [induction](11_Logic/induction/README.md).
{ #induction-mathematical }

**Inductive set** — a set containing ∅ and, with each member x, its successor x ∪ {x}. The axiom of infinity says one exists; ω, the natural numbers, is the smallest. See [infinity](13_Axioms_of_Set_Theory/infinity/README.md).
{ #inductive-set }

**Injective (one-to-one)** — a function in which different inputs always give different outputs: f(a) = f(b) forces a = b, so no two arrows land on the same target. Latin *in-icere*, to throw in. "One-to-one" means this, not bijective. See [relations and functions](04_Sets/relations_and_functions/README.md#the-three-words).
{ #injective-one-to-one }

**Intercept** — a coordinate of a point where a graph meets an axis. For x-intercepts set y = 0 and solve; for y-intercepts set x = 0. Sullivan means the number, 3, not the point (3, 0). See [graphs of equations: intercepts and symmetry](08_Analytic_Geometry/graphs_intercepts_symmetry/README.md).
{ #intercept }

**Inverse** — for a member a, a member b with a · b = b · a = e, the identity. −3 is the inverse of 3 under +, and 1/2 is the inverse of 2 under ×. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).
{ #inverse }

**Inverse of a statement** — of "if A then B", the statement "if not A then not B". Not to be confused with the inverse of a member under an operation. It is the contrapositive of the converse, so it is true exactly when the converse is. See [if A then B](11_Logic/converse_and_contrapositive/README.md).
{ #inverse-of-a-statement }

**Irreflexive relation** — no element is related to itself: (x, x) ∉ R for all x. < and ∈ (under foundation) are irreflexive; a relation can be neither reflexive nor irreflexive. See [orderings](04_Sets/orderings/README.md).
{ #irreflexive-relation }

**Isomorphism** — a homomorphism that can be undone, showing two structures are the same one with the members renamed. The logarithm is an isomorphism from the positive numbers under × to the numbers under +, which is how a slide rule multiplies by adding lengths. See [maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md).
{ #isomorphism }

**Kernel of a function** — ker(f) = {(u, v) : f(u) = f(v)}, the pairs f cannot tell apart; always an equivalence relation, and every equivalence is one. See [equivalence relations and partitions](04_Sets/equivalence_and_partitions/README.md).
{ #kernel-of-a-function }

**König's lemma** — an infinite tree in which every node has finitely many children has an infinite branch. It turns the infinite Ramsey theorem into the finite one, and more generally a property of ℕ into a bound on finite sets, without saying what the bound is: the pattern called compactness. See [Ramsey's theorem](04_Sets/ramsey/README.md#finite-from-infinite-konigs-lemma).
{ #konig-s-lemma }

**Kurepa's principle** — every poset has a maximal antichain. Equivalent to the axiom of choice given foundation, and not without it (Halbeisen, Theorem 6.2). See [choice](13_Axioms_of_Set_Theory/choice/README.md#the-equivalent-forms-and-the-weaker-ones).
{ #kurepa-s-principle }

**Lebesgue's criterion** — a bounded function on a closed interval has a Riemann integral exactly when the points where it is discontinuous form a set of measure zero. Also called the *Lebesgue–Vitali theorem*. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).
{ #lebesgue-s-criterion }

**Legs** — of a right triangle, the two sides that form the right angle; the a and b in c² = a² + b². See [the Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md).
{ #legs }

**Lexicographic order** — the dictionary order on pairs: (a, b) ≤ (c, d) when a < c, or a = c and b ≤ d. A partial order, linear when both coordinates are; a two-column sort uses it. See [orderings](04_Sets/orderings/README.md).
{ #lexicographic-order }

**Linear combination** — a₁x₁ + a₂x₂ + ⋯ + aₙxₙ: each variable multiplied by a fixed number, then added. No powers, no products of variables, no variable inside a function. It keeps sums and multiples, which is what makes it a linear map. See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md).
{ #linear-combination }

**Linear equation** — a linear combination set equal to a number, the constant: a₁x₁ + ⋯ + aₙxₙ = d. It does not say what the variables are; it is a test that any n-tuple of numbers passes or fails. See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md).
{ #linear-equation }

**Linear map** — a map T between vector spaces with T(u + v) = Tu + Tv and T(av) = aTv. Multiplying by i and projecting onto an axis are linear; x ↦ x + 1 is not, since a linear map always sends 0 to 0. See [maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md).
{ #linear-map }

**Linear order (total order)** — a partial order in which every two elements are comparable: a ≤ b or b ≤ a. ≤ on numbers is one; ⊆ is not. A set of n members has n! linear orders. See [orderings](04_Sets/orderings/README.md).
{ #linear-order-total-order }

**Log-normal distribution** — the distribution of a quantity whose logarithm is normally distributed. It is skewed to the right, so its mean e^(μ + σ²/2) lies above its median e^μ, and the gap grows fast with σ. See [a share above a cutoff](05_Statistics/share_above_a_cutoff/README.md).
{ #log-normal-distribution }

**Logical matrix** — a relation on n elements drawn as an n × n grid of 0s and 1s, a 1 in row x and column y when x R y; also called a Boolean or adjacency matrix. Reflexive is a full diagonal, symmetric a grid equal to its transpose, an equivalence blocks of 1s along the diagonal, and transitive means the Boolean product M·M stays inside M. See [orderings](04_Sets/orderings/README.md#a-relation-as-a-logical-matrix).
{ #logical-matrix }

**Machine number** — a member of the finite set a floating-point format can represent, fixed by its radix, precision and exponent range. Each one is an exact number; the approximation happens when a real result is rounded into the set. See [machine numbers](01_Precision/machine_numbers/README.md).
{ #machine-number }

**Maximal and maximum** — in a poset, an element is maximal when nothing is strictly above it and the maximum when it is above everything else; a maximum is maximal, but a poset can have several maximal elements and no maximum, as Mortimer's family tree has two spontaneously generated ancestors. Minimal and minimum likewise. See [orderings](04_Sets/orderings/README.md).
{ #maximal-and-maximum }

**Mean** — a family of averages, each the one number that can replace every value while keeping some total unchanged. The arithmetic mean keeps the sum, the geometric mean the product, the harmonic mean the sum of reciprocals, the quadratic mean the sum of squares. With no adjective it means the arithmetic mean. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).
{ #mean }

**Measure zero** — a set has measure zero if, for every ε > 0, it fits inside a list of intervals whose lengths add up to at most ε. With squares or cubes in place of intervals, the same definition gives zero area or zero volume. Also called a *null set*. See [what measure zero means](02_Measure_Zero/what_measure_zero_means/README.md).
{ #measure-zero }

**Markov's inequality** — for a quantity that cannot be negative, the share of values at or above c is at most mean / c. Read the other way round: if a share p is at or above c, the mean is at least p × c. See [a share above a cutoff](05_Statistics/share_above_a_cutoff/README.md).
{ #markov-s-inequality }

**Median** — the middle value once the numbers are sorted, or halfway between the two middle ones: at least half the values are at or below it, and at least half are at or above it. An average but not a mean, and the one a single huge value cannot drag. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).
{ #median }

**Membership (∈, ∉, ∋)** — a ∈ A says a is a member of A, a ∉ A that it is not, and A ∋ a is the same fact written from the set's side, read "A contains a"; ∌ negates it. The symbol ∋ is a mirrored ∈ and nothing to do with ∃, "there exists", which one circulating chart put in its place. Membership is the one primitive relation of set theory; everything else is defined from it. See [what is a set?](04_Sets/what_is_a_set/README.md).
{ #membership }

**Metacognition** — John Flavell's word (1976) for thinking about your own thinking, including the ability to judge accurately how much you have learned, the one part a program can measure. See [metacognition ↗](https://masiarek.github.io/learning-to-learn-library/01_Knowing_What_You_Know/metacognition/).
{ #metacognition }

**Midpoint** — the point halfway along a segment, ((x₁ + x₂)/2, (y₁ + y₂)/2): an average per coordinate. Equidistant from both ends and on the segment; equidistance alone describes the perpendicular bisector. See [the midpoint formula](08_Analytic_Geometry/midpoint_formula/README.md).
{ #midpoint }

**Mode** — the value that occurs most often. When several values tie for most often, a set has more than one mode. An average, but not a mean. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).
{ #mode }

**Model finder** — a program that looks for a universe in which given sentences are true, or one of them fails: by trying small universes exhaustively, as every program in the [axioms chapter](13_Axioms_of_Set_Theory/README.md) does, or by SAT search, as Alloy does. A counterexample is a finite object, so this is the tool that finds one; a proof assistant can only fail to prove. See [proof assistants: a reading guide](reading_guides/proof_assistants/README.md).
{ #model-finder }

**Monoid** — a set with an operation that is associative and has an identity, but where members need not have inverses. Strings under concatenation, and the integers under ×. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).
{ #monoid }

**Multiplicity** — the count a multiset gives a member; the multiset is the function from members to counts. See [multisets](04_Sets/multisets/README.md).
{ #multiplicity }

**Multiset** — a collection in which a member may occur more than once: formally a function M from a set S to ℕ giving each member's multiplicity, written [2, 2, 2, 5, 7, 7]. The prime factorisation of a number is a multiset of primes; Python's `collections.Counter` is one. Union takes the larger multiplicity, intersection the smaller, sum adds them, which is gcd, lcm and product on factorisations. See [multisets](04_Sets/multisets/README.md).
{ #multiset }

**Natural deduction** — Gentzen's way of writing proofs: for each connective, rules that introduce it (conjI: from P and Q, P ∧ Q) and rules that eliminate it (conjunct1: from P ∧ Q, P), with assumptions made and later discharged (impI turns Q-under-the-assumption-P into P ⟶ Q). Isabelle's FOL is one, and the program of [proof assistants: a reading guide](reading_guides/proof_assistants/README.md) checks proofs written in it.
{ #natural-deduction }

**Negative reciprocal** — −1/m: the slope of a line perpendicular to one of slope m, so the two slopes multiply to −1. Flip the fraction and change its sign. See [lines: slope, equations, parallel and perpendicular](08_Analytic_Geometry/lines_and_slope/README.md).
{ #negative-reciprocal }

**Non-crossing partition** — a partition of points on a circle in which no two blocks cross: no a < b < c < d with a, c in one block and b, d in another. Counted by the Catalan numbers, 42 of the 52 partitions of five points. See [equivalence relations and partitions](04_Sets/equivalence_and_partitions/README.md).
{ #non-crossing-partition }

**Nowhere dense** — for a closed set on the line, containing no interval at all: there are gaps everywhere. Both Cantor sets are nowhere dense, but only the standard one has measure zero. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).
{ #nowhere-dense }

**Number sets (ℕ, ℤ, ℚ, ℝ, ℂ)** — the blackboard-bold letters for the natural numbers ℕ (with or without 0, by book), the integers ℤ (German *Zahlen*), the rationals ℚ (quotients), the reals ℝ and the complex numbers ℂ, each a subset of the next; 𝔸 is sometimes the algebraic numbers and 𝕋 the circle. In set theory ℕ is ω, the first infinite ordinal, and |ℕ| is ℵ₀. See [infinity](13_Axioms_of_Set_Theory/infinity/README.md) and [countable sets](02_Measure_Zero/countable_sets/README.md).
{ #number-sets-n-z-q-r-c }

**Orbit** — of a point under a group acting on a set, the set of points it can be moved to; the orbits are the classes of the equivalence “can be moved to”, and Burnside's lemma counts them as the average number of points each group element fixes. Congruent triangles are the orbits of the rigid motions. See [equivalence relations and partitions](04_Sets/equivalence_and_partitions/README.md#where-the-textbook-sections-live-here).
{ #orbit }

**Ordered pair** — (a, b), an object that remembers which entry is first: (a, b) = (c, d) exactly when a = c and b = d. Unlike the set {a, b}, it distinguishes (2, 5) from (5, 2) and does not collapse (3, 3). See [the Cartesian product](04_Sets/cartesian_product/README.md).
{ #ordered-pair }

**Ordinal** — a set that is transitive (every member is a subset) and well-ordered by ∈: 0 = ∅, 1 = {0}, 2 = {0, 1}, …, ω, ω + 1, …. The measuring sticks for well-orderings; a strictly decreasing sequence of ordinals is finite, which is what makes Goodstein sequences stop. See [ordinals](13_Axioms_of_Set_Theory/ordinals/README.md).
{ #ordinal }

**Ordinate** — the y-coordinate of a point: its signed distance from the x-axis, positive above it and negative below. The x-coordinate is the *abscissa*. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).
{ #ordinate }

**Partial order** — a relation that is reflexive, antisymmetric and transitive but need not compare every pair; a set with one is a poset, and [orderings](04_Sets/orderings/README.md) counts the 19 on three points. ⊆ on sets is the standard example: {1} and {2} are incomparable, which is why `sorted()` on a list of Python sets gives no meaningful order. A set with one is a *poset*. See [the algebra of sets](04_Sets/algebra_of_sets/README.md).
{ #partial-order }

**Partition** — a collection of nonempty, pairwise disjoint blocks whose union is the whole set; the same thing as an equivalence relation, seen as blocks instead of pairs. Real analysis uses the word for a finite list of cut points of an interval, a different object, whose refinement order is a poset; see [orderings](04_Sets/orderings/README.md#the-other-partition). A set of n members has a Bell number of them: 1, 2, 5, 15, 52, …. See [equivalence relations and partitions](04_Sets/equivalence_and_partitions/README.md).
{ #partition }

**Partition relation (arrow notation)** — κ → (λ)ⁿ_r means: however the n-element subsets of a set of size κ are split into r pieces, some subset of size λ has all its n-element subsets in one piece. Ramsey's theorem is ω → (ω)ⁿ_r; Sierpiński's ω₁ ↛ (ω₁)²₂ says the first uncountable set fails; κ → (κ)²₂ defines a weakly compact cardinal. See [Ramsey's theorem](04_Sets/ramsey/README.md#why-this-is-set-theory).
{ #partition-relation-arrow-notation }

**Percentile** — the p-th percentile is the value with p% of the data below it. "p% of people are at or above c" says exactly that c is the (100 − p)-th percentile, and nothing else. See [a share above a cutoff](05_Statistics/share_above_a_cutoff/README.md).
{ #percentile }

**Permutation** — a bijection of a finite set with itself, a rearrangement; a set of n members has n! of them, and they form a group under composition, not commutative from n = 3. See [group](06_Algebraic_Structures/laws_of_an_operation/structures/group/README.md).
{ #permutation }

**Pigeonhole principle** — more pigeons than holes, so some hole holds two; infinitely many pigeons in finitely many holes, so some hole holds infinitely many. The first fact of combinatorics, and the step repeated in every proof of Ramsey's theorem. See [Ramsey's theorem](04_Sets/ramsey/README.md).
{ #pigeonhole-principle }

**Point-slope form** — y − y₁ = m(x − x₁), the line through (x₁, y₁) with slope m; the form to write first. See [lines: slope, equations, parallel and perpendicular](08_Analytic_Geometry/lines_and_slope/README.md).
{ #point-slope-form }

**Polar form** — a nonzero complex number written as r e^{iθ}: its length r times the unit point at its angle θ. Multiplying two of them multiplies the lengths and adds the angles, which is the law of exponents, and de Moivre's formula is (e^{iθ})ⁿ = e^{inθ}. `cmath.polar` reads r and θ off a number and `cmath.rect` puts them back. See [Euler's identity](03_Complex_Numbers/eulers_identity/README.md).
{ #polar-form }

**Poset** — a partially ordered set: a set with a relation that is reflexive, antisymmetric and transitive, in which some pairs may be incomparable. ⊆ on subsets and divisibility on positive integers are the standard examples; a linearly ordered set, in which every pair is comparable, is sometimes called a *toset* or a chain. See [orderings](04_Sets/orderings/README.md).
{ #poset }

**Power series** — a polynomial that never ends, a₀ + a₁x + a₂x² + ⋯. For e^x the rule "velocity = position" forces aₖ = 1/k!, and putting x = it splits the terms into the series for cos t and sin t. See [power series](09_Calculus/power_series/README.md).
{ #power-series }

**Power set** — 𝒫(a), the set of all subsets of a, with 2ⁿ members for |a| = n and always strictly more members than a (Cantor). Jech writes P(X), Cori and Lascar ℘(a). See [power set](13_Axioms_of_Set_Theory/power_set/README.md).
{ #power-set }

**Predicate** — a statement with a hole, P(x), that becomes true or false when x is filled from the universe of discourse. See [predicates and quantifiers](11_Logic/predicates_and_quantifiers/README.md).
{ #predicate }

**Preorder** — a relation that is reflexive and transitive but not necessarily antisymmetric, such as "is no taller than" or divisibility on all the integers (2 and −2 each divide the other). Quotienting by "both ways" turns a preorder into a partial order. No lesson here yet; see [orderings](04_Sets/orderings/README.md).
{ #preorder }

**Prime ideal theorem** — every Boolean algebra has a prime ideal, equivalently every filter extends to an ultrafilter. It follows from the axiom of choice and is strictly weaker (Halpern and Lévy 1971); enough for Tychonoff's theorem on Hausdorff spaces and the completeness theorem of logic. See [choice](13_Axioms_of_Set_Theory/choice/README.md#the-equivalent-forms-and-the-weaker-ones).
{ #prime-ideal-theorem }

**Proof assistant** — a program that checks a proof line by line, verifying that each line has the shape its rule demands from the lines it cites, without evaluating a single formula; Isabelle, Lean, Rocq and Metamath are ones. It proves a theorem about every model, where a [model finder](#model-finder) checks one. See [proof assistants: a reading guide](reading_guides/proof_assistants/README.md).
{ #proof-assistant }

**Proper factor** — a factor of n other than n itself; on the stricter convention, which the Math is Fun quizzes use, other than 1 as well, so the proper factors of 6 are 2 and 3. "Proper" as in proper subset: the whole thing excluded. Divisibility read as sets: a divides b exactly when the factors of a are a subset of the factors of b. See [set katas](04_Sets/set_katas/README.md#quiz-katas).
{ #proper-factor }

**Pythagorean theorem** — in a right triangle, the square of the hypotenuse equals the sum of the squares of the legs, c² = a² + b². Its converse is also true. See [the Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md).
{ #pythagorean-theorem }

**Pythagorean triple** — three whole numbers with a² + b² = c², such as 3, 4, 5 or 5, 12, 13; any multiple of one is another. See [the Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md).
{ #pythagorean-triple }

**Quadrant** — one of the four regions the coordinate axes cut the plane into, numbered I to IV counterclockwise from the upper right. Membership depends only on the signs of x and y, so (1, 1) and (1000, 5) share a quadrant, and a point on an axis, where one coordinate is 0, is in none. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).
{ #quadrant }

**Quadratic mean** — also the *root mean square*: the square root of the mean of the squares, the one number that keeps the sum of squares. The rated value of an AC voltage is one. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).
{ #quadratic-mean }

**Quadrature** — combining independent uncertainties as √(a² + b²) rather than a + b. Linear addition is the worst case and is correct only for perfectly correlated errors. See [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).
{ #quadrature }

**Quantifier** — ∀x ("for every x", an upside-down A for All) and ∃x ("for some x", a backwards E for Exists); in code, `all(...)` and `any(...)` over the universe. A ¬ pushed through one flips it; ∀x∃y and ∃y∀x are different claims. ∃!x means "there is exactly one x" and ∄x, or ¬∃x, "there is no x". See [predicates and quantifiers](11_Logic/predicates_and_quantifiers/README.md).
{ #quantifier }

**Radian** — the unit of angle in which a point of the unit circle turned through angle t travels a distance t along the circle, so a full turn is 2π and a half turn is π. It is the unit Euler's formula needs, because compounding (1 + it/n)ⁿ turns through the number t itself, and it is the reason the identity has a π in it and not 180. Only in radians is d/dt sin t = cos t. See [radians](09_Calculus/radians/README.md) and [Euler's identity](03_Complex_Numbers/eulers_identity/README.md).
{ #radian }

**Ramsey's theorem** — colour every pair from a large enough set with finitely many colours and some large subset has all its pairs one colour. Finite form: R(3, 3) = 6, six points force a one-colour triangle and five do not; infinite form (Ramsey 1930): colouring the pairs of ℕ leaves an infinite one-colour set, and the same for n-element subsets. Written κ → (λ)ⁿ_r in the arrow notation of Erdős and Rado. See [Ramsey's theorem](04_Sets/ramsey/README.md).
{ #ramsey-s-theorem }

**Rank** — the stage V_α at which a set first appears when the universe is built from ∅ by power sets: rank(∅) = 0 and rank(s) = 1 + the largest rank of a member. Pairs and power sets raise rank, unions lower it, which is why a finite stage fails some axioms and not others. See [foundation](13_Axioms_of_Set_Theory/foundation/README.md) and [reading a formula](13_Axioms_of_Set_Theory/reading_a_formula/README.md).
{ #rank }

**Rectangular coordinates** — also *Cartesian coordinates*, after Descartes: the ordered pair (x, y) that locates a point of the plane by its signed distances from two perpendicular number lines, x from the y-axis and y from the x-axis. The origin O = (0, 0) is where the axes cross. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).
{ #rectangular-coordinates }

**Reflexive relation** — every element is related to itself: (x, x) ∈ R for all x in S. ≤, ⊆, divides and = are reflexive; < is not. See [orderings](04_Sets/orderings/README.md).
{ #reflexive-relation }

**Related rates** — problems where two quantities are tied by an equation at every instant, so their rates of change are tied by its derivative in time: V = (4/3)πr³ gives dV/dt = 4πr² · dr/dt. Differentiate first, then put in the numbers of the instant. See [related rates](09_Calculus/related_rates/README.md).
{ #related-rates }

**Relation** — a set of ordered pairs; x ρ y means (x, y) ∈ ρ and nothing more. Divides, less than, likes, ∈ and every database table are relations. See [relations and functions](04_Sets/relations_and_functions/README.md).
{ #relation }

**Relative error** — |x − x̂| / |x|, the error as a fraction of the true value (`0.81%`); equivalently |ρ| where x̂ = x(1 + ρ). Undefined at x = 0, unchanged by a change of units, and the measure numerical analysis reports in place of a count of correct digits. What `×` and `÷` propagate, and the reason their rule counts significant figures. Defined in [relative error and correct digits](01_Precision/relative_error/README.md); propagated in [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).
{ #relative-error }

**Replacement** — if a formula F is functional (each x has at most one y) then for every set a the values {φ_F(x) : x ∈ a} form a set; Python's `{f(x) for x in a}`. The F of ZF, added by Fraenkel in 1922; needed for ω + ω and recursion along the ordinals. See [replacement](13_Axioms_of_Set_Theory/replacement/README.md).
{ #replacement }

**Right triangle** — a triangle with one angle of 90°. It cannot have two, since the angles add up to 180°. See [the Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md).
{ #right-triangle }

**Ring** — a set with + and × where + makes a commutative group, × is associative with an identity, and × distributes over +. The integers are a commutative ring, and the 2 × 2 matrices are a ring that is not commutative. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).
{ #ring }

**Root of unity** — a solution of zⁿ = 1; equivalently, a unit point that is back at (1, 0) after n multiplications by itself. There are exactly n of them, spaced evenly around the unit circle, and the twelfth roots are the marks of a clock face. A *primitive* n-th root needs all n steps to return, and its powers visit all n. See [roots of unity](03_Complex_Numbers/roots_of_unity/README.md).
{ #root-of-unity }

**Rounding** — the mechanical operation of cutting a number at some place. The *action*; significant figures are the argument for where the action must stop. See [significant figures](01_Precision/significant_figures/README.md).
{ #rounding }

**Rounding function** — a rule sending every real number to a machine number, or to an infinity. IEEE 754 defines five: toward −∞, toward +∞, toward zero, and to nearest with ties going either to the even significand or away from zero. See [machine numbers](01_Precision/machine_numbers/README.md).
{ #rounding-function }

**Russell's paradox** — the rule "x is not a member of itself" is sharp, yet no set R can obey it, since R ∈ R holds exactly when it does not. It shows that a well-defined rule does not always give a set. With the axiom of separation, which only cuts a rule out of an existing set, the same argument proves that no set contains every set. See [the textbook definition on trial](04_Sets/definition_on_trial/README.md).
{ #russell-s-paradox }

**Scale factor** — the one ratio k shared by every pair of corresponding sides of similar figures. Lengths scale by k, areas by k², volumes by k³. See [congruent and similar triangles](10_Geometry/congruent_and_similar_triangles/README.md) and [area and volume formulas](10_Geometry/area_and_volume_formulas/README.md).
{ #scale-factor }

**Scientific notation** — writing a value as mantissa × 10ⁿ, so the mantissa carries the precision claim and the exponent carries the magnitude. The only unambiguous way to write trailing zeros. See [significant figures](01_Precision/significant_figures/README.md).
{ #scientific-notation }

**Semigroup** — a set with an associative operation and nothing more: no identity or inverses required. The integers under max. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).
{ #semigroup }

**Set-builder notation** — {(x, y) | x, y ∈ ℝ}, read "the set of all (x, y) such that x and y are in ℝ": the shape of a member left of the bar, the condition it must meet right of it. Python's set comprehension `{(x, y) for x in S for y in S}` is the same notation, runnable. See [the Cartesian product](04_Sets/cartesian_product/README.md).
{ #set-builder-notation }

**Signed distance** — also *directed distance*: a distance with a sign that says which side. The x-coordinate of a point is its signed distance from the y-axis, positive to the right and negative to the left. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).
{ #signed-distance }

**Significant figures** — the digits of a measurement that carry information about the instrument rather than about place value. A claim about knowledge, not a formatting choice. See [significant figures](01_Precision/significant_figures/README.md).
{ #significant-figures }

**Similar triangles** — triangles with the same shape: corresponding angles equal and corresponding sides proportional, with one scale factor. Proved by AA, SSS (proportional) or SAS (proportional). See [congruent and similar triangles](10_Geometry/congruent_and_similar_triangles/README.md).
{ #similar-triangles }

**Slope** — rise over run, m = (y₂ − y₁)/(x₂ − x₁): one number for a whole line, because every pair of its points makes a similar right triangle. Undefined for a vertical line, 0 for a horizontal one. See [lines: slope, equations, parallel and perpendicular](08_Analytic_Geometry/lines_and_slope/README.md).
{ #slope }

**Slope-intercept form** — y = mx + b, a line with slope m and y-intercept b. It cannot describe a vertical line. See [lines: slope, equations, parallel and perpendicular](08_Analytic_Geometry/lines_and_slope/README.md).
{ #slope-intercept-form }

**Solution** — of a linear equation, an n-tuple (s₁, …, sₙ) that makes it true when sᵢ is put in for xᵢ; of a system, a tuple that is a solution of every equation at once. One equation in two unknowns has a whole line of solutions. See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md).
{ #solution }

**Solution set** — of an equation or inequality, the set of every value, or pair of values, that makes it true: {x : x² + x + 1 > 0} is all of ℝ, written (−∞, ∞); {x : x² = 4} is {−2, 2}; {(x, y) : x² + y² = 1} is the unit circle, so the graph of an equation is its solution set drawn. It is set-builder notation with the equation as the test, which is what the comprehension axiom licenses; the solution set of a system is the intersection of the solution sets, and "no solution" means the solution set is ∅. See [graphs of equations](08_Analytic_Geometry/graphs_intercepts_symmetry/README.md) and [what is a set?](04_Sets/what_is_a_set/README.md).
{ #solution-set }

**Spacing effect** — the same number of reviews works better spread out than crammed together, because a review strengthens memory most when some has been forgotten. See [spaced retrieval ↗](https://masiarek.github.io/learning-to-learn-library/02_Making_It_Stay/spaced_retrieval/).
{ #spacing-effect }

**Stability** — whether a particular *algorithm* preserves the accuracy a well-conditioned problem allows. The textbook quadratic formula is unstable for one of its two roots; a conjugate rearrangement fixes it for free. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).
{ #stability }

**Standard model** — the assumption behind rounding error analysis: every basic floating-point operation returns the exact result times (1 + δ) with |δ| ≤ u, the unit roundoff. Checked exactly on thousands of operations in [relative error and correct digits](01_Precision/relative_error/README.md).
{ #standard-model }

**Sterbenz's lemma** — if two floats a and b satisfy b/2 ≤ a ≤ 2b, then a − b is computed exactly. So the subtraction in a catastrophic cancellation adds no error of its own. See [machine numbers](01_Precision/machine_numbers/README.md).
{ #sterbenz-s-lemma }

**Stirling numbers of the second kind** — S(n, k), the number of partitions of an n-set into exactly k blocks; S(n, k) = k·S(n − 1, k) + S(n − 1, k − 1), and the row sums are the Bell numbers: S(5, k) = 1, 15, 25, 10, 1, total 52. See [equivalence relations and partitions](04_Sets/equivalence_and_partitions/README.md).
{ #stirling-numbers-of-the-second-kind }

**Strict order** — a relation that is irreflexive, asymmetric and transitive, written a < b; the non-strict partial order a ≤ b with the pairs (x, x) removed, and the two match one to one. See [orderings](04_Sets/orderings/README.md).
{ #strict-order }

**Subnormal** — a float below the smallest normal one, written with a leading zero digit at the lowest exponent. Subnormals fill the gap between zero and the smallest normal number; without them, a − b could round to 0 while a ≠ b. See [machine numbers](01_Precision/machine_numbers/README.md).
{ #subnormal }

**Subspace** — a subset of a vector space that is a vector space with the same operations. It needs only three checks — it contains 0, and it is closed under + and under scalar multiplication — because the other laws are inherited. The subspaces of the plane are the origin, the lines through it, and the plane. See [subsets inherit the laws](06_Algebraic_Structures/subsets_inherit_the_laws/README.md).
{ #subspace }

**Such that (:, |)** — the colon or bar inside set-builder notation, {x ∈ A : P(x)} or {x ∈ A | P(x)}, read "the set of x in A such that P(x)"; both spellings mean the same, and the bar is avoided when the condition itself contains a bar, as in |x| < 1. See [set-builder notation](#set-builder-notation).
{ #such-that }

**Surjective (onto)** — a function that reaches every member of its target: for each y in T some x has f(x) = y, so no target is missed. Latin *sur-jacere*, to throw onto. See [relations and functions](04_Sets/relations_and_functions/README.md#the-three-words).
{ #surjective-onto }

**Symmetric difference** — A △ B, the members of exactly one of two sets, (A ∖ B) ∪ (B ∖ A); `a ^ b` in Python. Chained over several sets it keeps what is in an odd number of them, not what is in exactly one, because the subsets form a group under △ in which every set cancels itself; also written A ⊖ B or A + B. See [the algebra of sets](04_Sets/algebra_of_sets/README.md).
{ #symmetric-difference }

**Symmetric relation** — x R y always gives y R x: the reversed pair of every pair is present. "Is a sibling of" and = are symmetric; ≤ is not. Symmetric plus transitive does not give reflexive. See [orderings](04_Sets/orderings/README.md).
{ #symmetric-relation }

**Symmetry of a graph** — about the y-axis if (−x, y) is on it whenever (x, y) is; about the x-axis for (x, −y); about the origin for (−x, −y). Tested by substituting and comparing equations; two symmetries force the third. See [graphs of equations: intercepts and symmetry](08_Analytic_Geometry/graphs_intercepts_symmetry/README.md).
{ #symmetry-of-a-graph }

**System of linear equations** — m linear equations in the same n variables, written with double subscripts: aᵢ,ⱼ is the coefficient in equation i of variable j, and dᵢ is the constant of equation i. Its solutions are the tuples that pass every equation. See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md).
{ #system-of-linear-equations }

**Tablemaker's dilemma** — an entry computed as 0.124|5000000, correct to a few digits past the bar, cannot be rounded at the bar until some further digit breaks the run of zeros, and nothing says in advance how far out that digit is. An exact tie is possible only for an algebraic value. See [relative error and correct digits](01_Precision/relative_error/README.md).
{ #tablemaker-s-dilemma }

**Tautology** — a sentence true on every row of its truth table, like P ∨ ¬P; a **contradiction** is false on every row. Two sentences are logically equivalent, ψ ⇔ φ, when ψ ↔ φ is a tautology. See [truth tables and the laws of logic](11_Logic/truth_tables_and_laws/README.md).
{ #tautology }

**Testing effect** — retrieving something from memory makes it last longer than reading it again for the same time. See [spaced retrieval ↗](https://masiarek.github.io/learning-to-learn-library/02_Making_It_Stay/spaced_retrieval/).
{ #testing-effect }

**Therefore and because (∴, ∵)** — three dots pointing up, ∴, read "therefore", and pointing down, ∵, read "because"; shorthand of school proofs and older books, not of the logic that ⇒ and ⊢ formalise. See [connectives](#connectives).
{ #therefore-and-because }

**Transitive closure** — the smallest transitive relation containing R: add a shortcut (x, z) for every chain (x, y), (y, z) until none is missing. With the diagonal and the reversed pairs added first it is the equivalence generated by R, whose classes are the connected components. See [equivalence relations and partitions](04_Sets/equivalence_and_partitions/README.md#where-the-textbook-sections-live-here).
{ #transitive-closure }

**Transitive relation** — x R y and y R z give x R z: every chained pair has its shortcut. ≤, ⊆, divides and = are transitive; "is a parent of" and "are distinct siblings" are not. See [orderings](04_Sets/orderings/README.md).
{ #transitive-relation }

**Transitive set** — a set every member of which is also a subset, so that y ∈ x ∈ a gives y ∈ a. Every ordinal is one; V₃ = {∅, {∅}, {{∅}}, {∅, {∅}}} is one and is not an ordinal. See [ordinals](13_Axioms_of_Set_Theory/ordinals/README.md).
{ #transitive-set }

**Triangle inequality** — each side of a triangle is shorter than the other two added together; in coordinates, d(P, R) ≤ d(P, Q) + d(Q, R), with equality only when Q is on the segment. See [the Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md) and [the distance formula](08_Analytic_Geometry/distance_formula/README.md).
{ #triangle-inequality }

**Truth table** — a sentence of propositional logic listed on every combination of truth values of its letters, 2ⁿ rows for n letters. A law of logic is two sentences whose columns agree on every row, and the table is the proof. See [truth tables and the laws of logic](11_Logic/truth_tables_and_laws/README.md).
{ #truth-table }

**Tuple** — an ordered list of numbers, (s₁, …, sₙ), called an n-tuple when it has n entries; a pair is a 2-tuple and a triple a 3-tuple. ℝⁿ is the set of all n-tuples of reals. Order matters: (1, 4) is not (4, 1). See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md) and [the Cartesian product](04_Sets/cartesian_product/README.md).
{ #tuple }

**Turnstile (⊢, ⊨)** — A ⊢ B, "B is provable from A", is about proofs; A ⊨ B, "every model of A is a model of B", is about truth; Gödel's completeness theorem says they agree for first-order logic. The negations are ⊬ and ⊭. The reversed sign ⊣ is not "does not yield", as one chart says; it is ⊢ read right to left, or in category theory "is left adjoint to". Halbeisen is the one book in the [symbol table](#symbols) that uses both signs on its first pages. See [reading a formula](13_Axioms_of_Set_Theory/reading_a_formula/README.md).
{ #turnstile }

**Uncountable** — too big to be written as a list. [0, 1] is uncountable, and so is the Cantor set, which still has measure zero. See [the Cantor set](02_Measure_Zero/cantor_set/README.md).
{ #uncountable }

**Unit circle** — x² + y² = 1, center (0, 0), radius 1. Every Pythagorean triple a, b, c gives a point (a/c, b/c) on it. See [circles](08_Analytic_Geometry/circles/README.md).
{ #unit-circle }

**Unit roundoff** — u = 2⁻⁵³ ≈ 1.1 × 10⁻¹⁶ for binary64: the largest relative error that rounding a real number to the nearest float can make, and the bound on δ in the standard model. See [relative error and correct digits](01_Precision/relative_error/README.md) and [machine numbers](01_Precision/machine_numbers/README.md).
{ #unit-roundoff }

**Universal class** — in a class theory such as Robert André's, 𝒰 = {x : x = x}, the class of all elements; a proper class, not a set, and not the universal set U of a Venn diagram, which is a set chosen for one problem. See [orderings](04_Sets/orderings/README.md) and [the reading guide](reading_guides/set_theory/README.md).
{ #universal-class }

**Universal set** — the set U, fixed in advance, that every set under discussion is a subset of; complements are taken relative to it, and in a Venn diagram it is the rectangle the circles are drawn in. There is no universal set of everything, so U is a choice, and the same A has a different complement under a different U. See [the algebra of sets](04_Sets/algebra_of_sets/README.md).
{ #universal-set }

**Universe (of set theory)** — a collection of points with a membership relation, in which the axioms are true or false; Cori and Lascar's 𝒰 with its set of points U. The chapter's small universes V₁ to V₄ have 1, 2, 4 and 16 sets. Not the universal set of a Venn diagram, though the word has the same root. See [reading a formula](13_Axioms_of_Set_Theory/reading_a_formula/README.md).
{ #universe-of-set-theory }

**Vector space** — a set with an addition and a scalar multiplication satisfying eight conditions: commutativity, two associativities, an additive identity, additive inverses, 1v = v, and two distributive laws. ℝ² is one; so are the functions from any set to ℝ, and the positive numbers with multiplication as their addition. See [a definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md).
{ #vector-space }

**Venn diagram** — sets drawn as circles inside a rectangle that stands for the universal set U. n circles make 2ⁿ regions, one per pattern of membership, and every set operation is a choice of regions; a circle inside another draws A ⊆ B, two circles apart draw disjoint sets, and the rectangle outside a circle is its complement. See [the algebra of sets](04_Sets/algebra_of_sets/README.md).
{ #venn-diagram }

**Weakly compact cardinal** — an uncountable cardinal κ with κ → (κ)²₂, so that Ramsey's theorem holds at κ as it does at ω. ZFC cannot prove one exists: it is a large cardinal. See [Ramsey's theorem](04_Sets/ramsey/README.md#why-this-is-set-theory).
{ #weakly-compact-cardinal }

**Well-defined (on classes)** — a function on a quotient set S/R is well defined when its value does not depend on which representative of a class is used: [a] + [b] = [a + b] on ℤ/mℤ passes, since a ≡ a′ and b ≡ b′ give a + b ≡ a′ + b′, and n ↦ n mod 3 on ℤ/5ℤ fails. Every quotient construction has to pass this check. See [equivalence relations and partitions](04_Sets/equivalence_and_partitions/README.md#where-the-textbook-sections-live-here).
{ #well-defined-on-classes }

**Well-ordering** — a total order in which every nonempty subset has a least member, so every descent is finite; ℕ is one, ℤ and ℚ are not. The **well-ordering principle** for ℕ is what makes [induction](11_Logic/induction/README.md) valid. Every set can be well-ordered exactly when the axiom of choice holds. See [ordinals](13_Axioms_of_Set_Theory/ordinals/README.md).
{ #well-ordering }

**Well-ordering principle (theorem)** — every set can be well-ordered (Zermelo 1904); equivalent to the axiom of choice, and often the easier form to apply, through transfinite induction along the well-ordering. For ℕ alone the principle is a theorem, see [well-ordering](#well-ordering). See [choice](13_Axioms_of_Set_Theory/choice/README.md#the-equivalent-forms-and-the-weaker-ones).
{ #well-ordering-principle-theorem }

**Zero divisor** — a nonzero number that multiplies some other nonzero number to give zero. Multiplying pairs entry by entry creates them, since (1, 0)(0, 1) = (0, 0), and a zero divisor can never be divided by. Complex multiplication has none: the product's x² + y² is the product of the two factors' x² + y², which is zero only when a factor is (0, 0). See [multiplication can be undone](03_Complex_Numbers/multiplication_can_be_undone/README.md).
{ #zero-divisor }

**Zorn's lemma** — if every chain in a nonempty poset has an upper bound, the poset has a maximal element; also the Kuratowski–Zorn lemma. Equivalent to the axiom of choice over ZF, and the form algebra uses: a basis for every vector space, a maximal ideal in every ring. See [choice](13_Axioms_of_Set_Theory/choice/README.md#the-equivalent-forms-and-the-weaker-ones).
{ #zorn-s-lemma }


## Symbols

The same ideas in the spellings of the books this library reads. The definitions never vary; only the ink does. The last column is not a book but a machine, Isabelle/ZF, read in its theory files for the [proof assistants guide](reading_guides/proof_assistants/README.md); its composition, `g O f`, is from memory.

| Idea | This library | Cori and Lascar | Cunningham | Jech | Kunen | Simovici and Djeraba | Stoll | André | Halbeisen | Isabelle/ZF |
|---|---|---|---|---|---|---|---|---|---|---|
| subset, equal allowed | a ⊆ b | a ⊆ b | A ⊆ B | X ⊂ Y | x ⊆ y | S ⊆ T | A ⊆ B | A ⊆ B | C ⊆ P | A ⊆ B |
| proper subset | a ⊊ b | a ⊊ b | A ⊂ B | X ⊂ Y, X ≠ Y | x ⊊ y | — | A ⊂ B | A ⊂ B | — | — |
| difference | a ∖ b | a ∖ b | A ∖ B | X − Y | x ∖ y | S − T | A − B | A − B | P ∖ A | A − B |
| complement | A′ | — | — | — | — | T̄ | Ā | A′ = {x : x ∉ A}, absolute, a class | S ∖ X, and −X in a Boolean algebra | — |
| symmetric difference | A △ B | — | — | — | — | U ⊕ V | A + B | A △ B | — | — |
| union of a family | ∪a | ∪a, ∪ₓ∈ₐ x | ∪𝓕 | ∪X | ∪𝓕 | ∪𝒞 | ∪𝒜 | ∪_{C∈𝒜} C | ∪𝒞 | ⋃(C) |
| power set | 𝒫(a) | ℘(a) | 𝒫(A) | P(X) | 𝒫(x) | 𝒫(S) | 𝒫(A) | 𝒫(A) | 𝒫(S) | Pow(A) |
| set builder | {x ∈ a : F[x]} | {x ∈ a : F[x]} | {x ∈ A : φ(x)} | {u ∈ X : φ(u)} | {x ∈ z : φ(x)} | {x ∈ S \| P(x)} | {x ∈ A \| P(x)} | {x : P(x)}, a class | {x ∈ S : …} | {x ∈ A . P(x)} |
| ordered pair | (a, b) | (a, b) | (a, b) | (a, b) | ⟨x, y⟩ | (x, y) | ⟨x, y⟩ | (a, b) | ⟨a, b⟩ | ⟨a, b⟩ |
| relation | ρ, R | R | R | R | R | ρ, σ, δ | ρ | R | a binary relation ≤ on P | r |
| x related to y | x ρ y, (x, y) ∈ ρ | — | x R y | x R y | x R y | x ρ y | x ρ y | x R y | p ≤ q | ⟨x, y⟩ ∈ r |
| domain, range | dom, ran | dom(f), Im(f) | dom, ran | dom, ran | dom, ran | Dom, Ran | 𝒟, ℛ | dom, ran | dom(f) | domain(r), range(r) |
| image of a set | f[a] | f̄(c) | f[A] | f"X, f(X) | F"A, F(A) | f(L) | f[A] | f[A] | f[A] | `r``A` |
| composition of f then g | g ∘ f | g ∘ f | g ∘ f | g ∘ f | g ∘ f | gf (functions), ρσ (relations) | g ∘ f | g ∘ f | gf, written right to left, as in σρσ⁻¹ | g O f |
| partial function | — | — | — | — | — | f : S ⇝ T | — | — | — | — |
| natural numbers | ω, ℕ | ω, ℕ | ω | ω, **N** | ω = ℕ | ℕ (from 0) | ℕ | ℕ, ω | ω | nat |
| cardinality words | injection, bijection, \|A\| | subpotent, equipotent, card | — | \|X\| ≤ \|Y\| | A ≼ B, A ≈ B | equinumerous, \|S\| | ~, cardinal number | equipotent, \|A\|, 𝒞 | 𝔪, 𝔫; \|x\|; ≤*; ℵ(𝔪) | A ≈ B, A ≲ B, \|A\| |
| the ordinals | Ord | On[v₀] | — | Ord | ON | — | — | 𝒪 | Ω | Ord(i), a predicate |
| if … then, iff | ⇒, ⇔ | ⇒, ⇔ | →, ↔ (in a formula); ⇒, ⇔ (between sentences) | →, ↔ | →, ↔ | — | →, ↔ | ⇒, ⇔ | →, ↔; :⟺ in definitions | ⟶, ⟷ in formulas; ⟹ between rules |
| equality in the formal language | = | ≃ | = | = | = | = | = | = | = | = |
| regularity / foundation | foundation | foundation | regularity | regularity | foundation | — | restriction | regularity | Axiom of Foundation | foundation |

Three conventions deserve a warning. Jech's ⊂ allows equality and Cunningham's does not, so the same symbol means ⊆ in one book and ⊊ in the other. André's objects are *classes*, and his {x : P(x)} is always a class, which is a set only when some axiom says so; the other books have no classes as objects at all. His complement is therefore absolute, taken in the universal class, where this library's A′ is U ∖ A for a chosen U. Simovici and Djeraba write gf for "f, then g", the order most books write as g ∘ f; both mean (g ∘ f)(x) = g(f(x)).

## Symbol index

Every symbol of the charts and tables the owner has sent, in one place, with where it is explained. Read a row as "symbol, how to say it, where". The cross-book table above is for the symbols whose spelling changes from book to book; this one is for finding a symbol at all. It is also an Anki deck, [`symbol_index.txt`](04_Sets/reading_set_expressions/anki/symbol_index.txt), generated from this table.

| Symbol | Read as | Where |
|---|---|---|
| ∈  ∉  ∋  ∌ | is a member of, is not, contains | [glossary: membership](#membership) |
| {a, b, c} | the set whose members are a, b, c | [what is a set](04_Sets/what_is_a_set/README.md) |
| {x ∈ A : P(x)}, {x \| P(x)} | the set of x such that P(x) | [glossary: set builder notation](#set-builder-notation) |
| ∅, { } | the empty set | [glossary: empty set](#empty-set) |
| U, 𝒰, E, Ω | the universal set (Ω also the class of ordinals, or ω₁) | [glossary: universal set](#universal-set) |
| ⊆  ⊂  ⊊  ⊇  ⊃  ⊄  ⊉ | subset, proper subset (two conventions), superset, and their negations | [glossary: symbols](#symbols) |
| A = B | the same members, by extensionality | [glossary: extensionality](#extensionality) |
| ∪  ∩ | union, intersection; ∪𝓕 and ∩𝓕 over a family | [algebra of sets](04_Sets/algebra_of_sets/README.md) |
| ∖  − | difference, A ∖ B = {x ∈ A : x ∉ B} | [algebra of sets](04_Sets/algebra_of_sets/laws/difference/README.md) |
| A′  Aᶜ  Ā  U − A | complement within the universal set | [glossary: complement](#complement) |
| △  ⊕ | symmetric difference | [glossary: symmetric difference](#symmetric-difference) |
| A × B | Cartesian product, the set of ordered pairs | [glossary: cartesian product](#cartesian-product) |
| (a, b), ⟨a, b⟩ | ordered pair | [glossary: ordered pair](#ordered-pair) |
| 𝒫(A), 2ᴬ | power set | [glossary: power set](#power-set) |
| \|A\|, n(A), #A, card(A) | cardinality | [glossary: cardinality](#cardinality) |
| ℵ₀, ℵ₁, ℶ₁, 𝔠, κ⁺, ℷ | infinite cardinals, the continuum, successor, gimel | [glossary: aleph beth and the continuum c](#aleph-beth-and-the-continuum-c) |
| ω, ω₁, ε₀, α + 1, S(α) | ordinals and successors | [glossary: ordinal](#ordinal) |
| ℕ  ℤ  ℚ  ℝ  ℂ | the number sets | [glossary: number sets n z q r c](#number-sets-n-z-q-r-c) |
| x R y, (x, y) ∈ R, dom R, ran R | a relation and its domain and range | [glossary: relation](#relation) |
| f: A → B, x ↦ f(x), f[A], f⁻¹, g ∘ f | function, image of a set, inverse, composition | [relations and functions](04_Sets/relations_and_functions/README.md) |
| [x], A/~ | equivalence class, quotient set | [glossary: equivalence relation](#equivalence-relation) |
| ≤, <, ≺ on a poset | partial order, strict order | [glossary: partial order](#partial-order) |
| ≈, ~, ≼, \|A\| ≤ \|B\| | equinumerous, injects into | [glossary: symbols](#symbols) |
| κ → (λ)ⁿ_r | partition relation | [glossary: partition relation arrow notation](#partition-relation-arrow-notation) |
| ∀  ∃  ∃!  ∄ | for all, there exists, exactly one, none | [glossary: quantifier](#quantifier) |
| ¬  ∧  ∨  ⇒  →  ⇔  ↔  ⇏ | not, and, or, implies, iff, does not imply | [glossary: connectives](#connectives) |
| ⊢  ⊬  ⊨  ⊣ | proves, does not prove, models; the reversed turnstile | [glossary: turnstile](#turnstile) |
| ∴  ∵ | therefore, because | [glossary: therefore and because](#therefore-and-because) |
| ∎  ■  □ | end of proof | [glossary: end of proof qed](#end-of-proof-qed) |
| :=  :⟺  ≝ | is defined as (a term, a statement) | [README.md#three-books-three-notations](13_Axioms_of_Set_Theory/README.md#three-books-three-notations) |
| ≃ | equality inside Cori and Lascar's formal language | [reading a formula](13_Axioms_of_Set_Theory/reading_a_formula/README.md) |
