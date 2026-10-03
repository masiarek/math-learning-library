# Math — Learning Library

<!-- --8<-- [start:hero] -->

A learning library for mathematics, built the same way as its siblings [rust-learning-library ↗](https://github.com/masiarek/rust-learning-library) and [star-voting-library ↗](https://github.com/masiarek/star-voting-library): **one idea per page, and every claim backed by a program that actually runs.**

No page here hand-types what a program prints. Each lesson links a real `.py` file; a tool runs it, checks the output against a recorded answer key, and pastes that verified output into the page. CI fails if any of the three drift apart. So when a page says *"this prints `3.2E+6`"*, that is not a promise — it is a test result.

The examples are **stdlib-only, on purpose**. A library about how much of a number is real should not open with a dependency-resolution failure. If you have `python3`, you can run every page in this repo.

📖 **Read it as a site:** <https://masiarek.github.io/math-learning-library/>

<!-- --8<-- [end:hero] -->

<!-- --8<-- [start:below-hero] -->

## Start here

[**01_Precision/**](01_Precision/README.md) — *How much of this number is real?*

The first chapter is a single argument in six steps, and it starts from a question that sounds like it has an obvious answer and does not: **are significant figures just rounding?**

| Lesson | What it teaches |
|---|---|
| [Exact vs approximate](01_Precision/exact_vs_approximate/README.md) | Which numbers have significant figures at all — and why a counted thing has infinitely many |
| [Significant figures](01_Precision/significant_figures/README.md) | What the notation claims, and why the rule for `+` is a *different rule* from the rule for `×` |
| [Relative error and correct digits](01_Precision/relative_error/README.md) | Why "correct to three digits" has no definition that behaves, and the one number to report instead |
| [Uncertainty propagation](01_Precision/uncertainty_propagation/README.md) | The rigorous version those rules approximate, and the two places they lie |
| [Machine numbers](01_Precision/machine_numbers/README.md) | What a float really is — an exact member of a finite set — the five ways to round into it, and which laws of arithmetic survive |
| [Catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md) | The one operation that destroys ten significant figures at once, silently |

Read them in that order; each one answers a question the previous one raises.

[**02_Measure_Zero/**](02_Measure_Zero/README.md) — *How can infinitely many points take up no room?*

The second chapter is about sets so thin that they have zero length, area or volume, even when they hold infinitely many points — even uncountably many. It does not need chapter 1. On the way it meets a set that is full of gaps and still fills half the room, and a staircase that climbs from 0 to 1 while standing still almost everywhere.

| Lesson | What it teaches |
|---|---|
| [What measure zero means](02_Measure_Zero/what_measure_zero_means/README.md) | The definition, which never measures the set itself — and why a segment has no area but does have length |
| [Countable sets](02_Measure_Zero/countable_sets/README.md) | Why the rationals, found inside every interval, still have measure zero |
| [The Cantor set](02_Measure_Zero/cantor_set/README.md) | Uncountably many points, and total length zero |
| [The fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md) | No interval inside it, yet length 1/2 — and why that breaks the Riemann integral |
| [The Cantor function](02_Measure_Zero/cantor_function/README.md) | The devil's staircase: continuous, flat almost everywhere, and still climbing from 0 to 1 |
| [Probability zero](02_Measure_Zero/probability_zero/README.md) | Why probability zero is not impossible, and why on a computer it is |

[**03_Complex_Numbers/**](03_Complex_Numbers/README.md) — *What is a complex number, before anyone says √−1?*

The third chapter builds the complex numbers the way Hamilton did: a complex number is a pair (x, y) of reals, and multiplication is the rule (x₁, y₁) · (x₂, y₂) = (x₁x₂ − y₁y₂, x₁y₂ + x₂y₁). The number whose square is −1 is a consequence of that rule, not an assumption behind it.

| Lesson | What it teaches |
|---|---|
| [Multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md) | The rule, why (0, 1) squares to (−1, 0), why x + yi is the same thing, and where the same rule appears with no complex numbers in sight |
| [Multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md) | Multiplying scales by a length and turns by an angle, so i² = −1 is two quarter turns making a half turn |
| [Multiplication can be undone](03_Complex_Numbers/multiplication_can_be_undone/README.md) | Why pairs are not multiplied entry by entry: zero divisors, and ℂ* as the pairs you can divide by |
| [Roots of unity](03_Complex_Numbers/roots_of_unity/README.md) | Multiplying a unit point by itself walks around the circle in equal steps, so zⁿ = 1 has exactly n solutions: the twelve marks of a clock face, with √3 carried exactly |
| [Euler's identity](03_Complex_Numbers/eulers_identity/README.md) | What e^{iπ} = −1 means, why the exponential can do nothing with an imaginary input but turn, and what the formula is for: the half turn reached exactly, the polar form, and why Python's answer is −1 + 1.2 × 10⁻¹⁶ i |

[**04_Sets/**](04_Sets/README.md) — *What is this collection, exactly?*

The fourth chapter is groundwork: the constructions every other page takes for granted, checked on real sets. It needs nothing from chapters 1 or 2.

| Lesson | What it teaches |
|---|---|
| [The Cartesian product](04_Sets/cartesian_product/README.md) | What ℝ² is, why (2, 5) is not (5, 2), why A × B is not B × A, and why (1, 1) counts |
| [Cardinality of sets](04_Sets/cardinality/README.md) | What \|A\| means, why size is defined by matching, and where it shows up in types, databases and computability |
| [Relations and functions are sets of pairs](04_Sets/relations_and_functions/README.md) | A relation is a set of pairs, a function a relation with one property, a graph a relation drawn, a table a relation stored; every relation on {1, 2, 3} sorted, composition as a relation product, and a function as its table of values |
| [Equivalence relations, partitions and the kernel of a function](04_Sets/equivalence_and_partitions/README.md) | Partitions, equivalences and kernels determine each other exactly: 5 of 512 relations on {1, 2, 3}, the Bell numbers, the decomposition of every function into surjection, bijection and inclusion, and congruence mod m |
| [Orderings](04_Sets/orderings/README.md) | Six properties as loops on all 512 relations on three points: 5 equivalences, 19 partial orders, 6 linear; the identity wears two names; two of a textbook's examples fail the loop; chains, antichains, maximal versus maximum on Mortimer's ancestors and divisibility; the Riemann partition as the other meaning of the word |
| [Cantor–Schröder–Bernstein](04_Sets/schroeder_bernstein/README.md) | Two injections make a bijection: the ancestor-tracing construction run on all 576 pairs of maps between two 4-sets and on ℕ with 2n and 3n; ≤ on sizes is antisymmetric without choice |
| [Multisets](04_Sets/multisets/README.md) | A set that counts, as a function to ℕ and as `Counter`: min and max as ∩ and ∪, gcd and lcm as ∩ and ∪ of factorisations checked to 60, stars and bars, the law that is lost |
| [Ramsey's theorem](04_Sets/ramsey/README.md) | The pigeonhole principle for pairs: R(3, 3) = 6 checked on all 32 768 colourings of six points, the infinite theorem run as an algorithm, König's lemma on the tree of bad colourings, and the arrow notation that turns a counting question into one about the axioms |
| [Set katas](04_Sets/set_katas/README.md) | Cunningham's first exercises checked on every choice of subsets of {1, 2, 3} before you prove them, with the four proof moves |
| [Function katas](04_Sets/function_katas/README.md) | Hrbacek and Jech's exercises on functions with solutions: compositions and inverses of 2x − 1, √x, 1/x computed exactly; left versus right inverses; why preimages respect ∩ and images do not; all 64 partial functions on {1, 2, 3} |

[**05_Statistics/**](05_Statistics/README.md) — *What does one number say about many?*

The fifth chapter is about the single number that stands in for a list: the average score, the average salary, the average speed. It starts with the names. *Average*, *mean* and *arithmetic mean* are one calculation in a classroom and three different sizes of word outside it. It needs nothing from the other chapters.

| Lesson | What it teaches |
|---|---|
| [Mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md) | Why one calculation has so many names, what the adjective *arithmetic* is for, and why "the average salary" can honestly be three different numbers |
| [A share above a cutoff](05_Statistics/share_above_a_cutoff/README.md) | What "20% of people have Lp(a) 50+" pins down (one percentile) and what it leaves free, and why a skewed quantity's mean can sit at the cutoff |

[**06_Algebraic_Structures/**](06_Algebraic_Structures/README.md) — *Why does every book list the same laws?*

The sixth chapter starts from a complaint: a school book lists a + b = b + a for the integers, a linear-algebra book lists u + v = v + u for vectors, and then lists the same laws again for linear maps. The answer is that there are only four laws to list, and the chapter follows the tools that stop the repetition: a definition that any set can pass, subsets that inherit the laws, and maps that carry them across. It needs school algebra; lessons 2 to 4 are easier after a first look at vectors.

| Lesson | What it teaches |
|---|---|
| [The laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md) | The four laws every book reprints, the names for their combinations, and a witness for every law that fails, from subtraction to floats |
| [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) | The vector-space axioms run against five candidates, and why 0v = 0, proved once, says x⁰ = 1 in a space where adding means multiplying |
| [Subsets inherit the laws](06_Algebraic_Structures/subsets_inherit_the_laws/README.md) | Why a subspace needs three checks instead of eight, and why a subgroup needs a fourth |
| [Maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md) | Linear maps, logarithms, determinants and string length as one shape; 2⁰ = 1, log 1 = 0, T(0) = 0 and det I = 1 as one proof; and the slide rule as an isomorphism |

[**07_Linear_Systems/**](07_Linear_Systems/README.md) — *What does it mean to solve a system of equations?*

The seventh chapter follows the first section of Jim Hefferon's *Linear Algebra*. Before any method, it says what is being looked for: a linear equation is a test that a list of numbers passes or fails, and a solution of a system passes every test at once. It needs nothing but school algebra.

| Lesson | What it teaches |
|---|---|
| [Linear equations and their solutions](07_Linear_Systems/linear_equations/README.md) | Hefferon's Definition 1.1 symbol by symbol: coefficients, constants, tuples and the double subscripts aᵢ,ⱼ, checked on two balances and a system in three unknowns, and why *linear* means keeping sums and multiples |

[**08_Analytic_Geometry/**](08_Analytic_Geometry/README.md) — *What does it mean to draw a number?*

The eighth chapter is the first chapter of every precalculus book: two number lines at right angles turn each point of the plane into a pair of numbers, and each pair into a point; then distance, midpoint, the graph of an equation, lines and circles. Every lesson ends with the book's questions, answers folded away, and a deck of Anki flashcards. It needs nothing but a number line.

| Lesson | What it teaches |
|---|---|
| [Rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md) | A point is two signed distances, and from the other axis than you expect; a quadrant is the pair of signs and nothing more, so the axes belong to none; and why that one word runs through trigonometry, complex numbers and the symmetry of graphs |
| [The distance formula](08_Analytic_Geometry/distance_formula/README.md) | Pythagoras with the legs read off the coordinates; why the squares make the order of the points and the signs irrelevant, and why distances are compared by their squares |
| [The midpoint formula](08_Analytic_Geometry/midpoint_formula/README.md) | One average per coordinate; halfway means equidistant *and* on the segment; half the difference is a trip, not a place |
| [Graphs of equations: intercepts and symmetry](08_Analytic_Geometry/graphs_intercepts_symmetry/README.md) | A graph is the set of points that pass an equation, so intercepts are points with a 0 coordinate and symmetry is a mirror image that passes too; drawn on a text grid |
| [Lines: slope, equations, parallel and perpendicular](08_Analytic_Geometry/lines_and_slope/README.md) | One slope per line because of similar triangles; point-slope, slope-intercept and general forms; negative reciprocals from a quarter turn |
| [Circles: standard form and general form](08_Analytic_Geometry/circles/README.md) | The distance formula held fixed; completing the square; when the "circle" is a point or nothing at all |
| [Distance in n dimensions, and the length of a vector](08_Analytic_Geometry/distance_in_n_dimensions/README.md) | Pythagoras twice gives the box diagonal 3-4-12-13, once per axis gives the formula in n dimensions by induction, √(v·v) is the distance from the origin, and the four metric properties are checked exactly on a grid |
| [Distance is the four properties](08_Analytic_Geometry/other_distances/README.md) | A metric is four properties, not a formula: taxicab and Chebyshev circles drawn on a grid, the p = ½ formula and the squared distance both broken by one triple, only the Euclidean distance unchanged by an exact 3-4-5 rotation, and the Hamming distance checked on all 512 triples of bit strings |

[**09_Calculus/**](09_Calculus/README.md) — *What is a velocity, and which motion is its own velocity?*

The ninth chapter is calculus as motion, the four pieces the talk behind [Euler's identity](03_Complex_Numbers/eulers_identity/README.md) leans on. Lost in that talk? [Euler's formula: a lesson plan](reading_guides/eulers_formula/README.md) says what to learn first, step by step, and which lesson here teaches each step.

| Lesson | What it teaches |
|---|---|
| [The derivative is a velocity](09_Calculus/derivative_as_velocity/README.md) | The velocity at an instant is what average velocities settle on, exactly 6 + h for t² at t = 3; and why a float derivative cannot shrink its step for ever |
| [Velocity equals position](09_Calculus/velocity_equals_position/README.md) | Start at 1 and always move as fast as your position: that is e^t, e is where you are at time 1, and the law of exponents, "double" and "flip and squish" follow |
| [Radians](09_Calculus/radians/README.md) | Archimedes' polygons measure the circle, a radian is one radius of arc, and in radians the angle is the distance walked, so d/dt sin t = cos t |
| [Power series](09_Calculus/power_series/README.md) | "Velocity = position" forces every coefficient of e^x to be 1/k!, and with an imaginary input the terms split into cos and sin |
| [Related rates](09_Calculus/related_rates/README.md) | Two quantities tied by an equation have velocities tied by its derivative; differentiate first, substitute last; balloons, ladders and kites from a Calculus I worksheet, each answer checked by measuring the motion |

[**10_Geometry/**](10_Geometry/README.md) — *How few numbers fix a shape?*

The tenth chapter is the geometry review every precalculus book assumes, Sullivan's Appendix A.2, to be read just in time: the distance formula sends the reader here first. Every lesson ends with the book's questions, answers folded away, and a deck of Anki flashcards with trap cards.

| Lesson | What it teaches |
|---|---|
| [The Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md) | c² = a² + b² one way and the converse the other, which makes a test; sort first, because only the longest side can be the hypotenuse; and what c² < a² + b² and c² > a² + b² say |
| [Area and volume formulas](10_Geometry/area_and_volume_formulas/README.md) | The eleven formulas of the book's box, told apart by one check: the power of length is the dimension, so scaling by k gives k, k², k³ |
| [Congruent and similar triangles](10_Geometry/congruent_and_similar_triangles/README.md) | SSS, SAS and ASA fix a triangle, AAA fixes only its shape, and SSA can fit two triangles, built and counted by a program |

[**11_Logic/**](11_Logic/README.md) — *What does "if A then B" actually claim?*

The eleventh chapter is the logic the theorems in every other chapter are written in. It needs nothing but school arithmetic.

| Lesson | What it teaches |
|---|---|
| [If A then B: converse, contrapositive and inverse](11_Logic/converse_and_contrapositive/README.md) | "If A then B" breaks only when A is true and B false, so the contrapositive is the same claim and the converse is not; if and only if; two classic mistakes; and why examples never prove but one counterexample disproves |
| [Truth tables and the laws of logic](11_Logic/truth_tables_and_laws/README.md) | A law of logic is two columns that agree on every row, so a 2ⁿ-row table proves it; tautology, contradiction, ↔ versus ⇔; a misprinted exercise caught by one row |
| [Predicates and quantifiers](11_Logic/predicates_and_quantifiers/README.md) | ∀ and ∃ as loops; "everyone likes someone" versus "someone is liked by everyone" on 65 536 relations; negation flips a quantifier; which distribution laws fail |
| [What a proof is](11_Logic/what_a_proof_is/README.md) | A chain from the givens to the claim, a reason beside every line, argued with letters so it covers every case; Fermat's five primes and √(t²) = t show why a loop cannot; the distance formula as ten checked lines, broken three ways to see which check catches which |
| [Induction](11_Logic/induction/README.md) | Base case, step, and why it works: the least counterexample; n² + n + 41 fails first at 40; the all-cars proof breaks at n = 1; Fibonacci facts with Binet computed exactly, 2ⁿ subsets, the chocolate bar, closed forms |

[**13_Axioms_of_Set_Theory/**](13_Axioms_of_Set_Theory/README.md) — *What are the rules for building sets, and why these?*

The thirteenth chapter decodes the formal language of set theory and gives each axiom of Zermelo and Fraenkel a page: read aloud in English, what it builds, what goes wrong without it, and a program that checks it on a small universe of sets. An axiom turns out to be a demand on the universe, not a description of it, and every False the programs print is a set the axiom asks for and the universe lacks.

| Lesson | What it teaches |
|---|---|
| [Reading a formula](13_Axioms_of_Set_Theory/reading_a_formula/README.md) | ∀ is a loop that must always succeed, ∃ one that must succeed once, ⇒ is "not p or q", ∈ is a lookup; every axiom evaluated on four small universes |
| [Extensionality](13_Axioms_of_Set_Theory/extensionality/README.md) | Same members, same set; the proof method a ⊆ b and b ⊆ a; why "the" pair; a universe with two empty sets |
| [Pairs](13_Axioms_of_Set_Theory/pairs/README.md) | {a, b} needs an axiom because every finite universe runs out; three pairs make Kuratowski's ordered pair |
| [Unions](13_Axioms_of_Set_Theory/unions/README.md) | The axiom gives ∪a, not a ∪ b; why it never fails in a finite universe; why ∩∅ cannot exist |
| [Power set](13_Axioms_of_Set_Theory/power_set/README.md) | ⊆ hidden in a ∀…⇒; V_{n+1} = 𝒫(V_n); Cantor's theorem |
| [Comprehension](13_Axioms_of_Set_Theory/comprehension/README.md) | One axiom per formula; drop the "x ∈ a" and Russell's paradox is a truth table with no true row |
| [Replacement](13_Axioms_of_Set_Theory/replacement/README.md) | "Functional" formulas, images, and the set Zermelo's axioms cannot collect |
| [Infinity](13_Axioms_of_Set_Theory/infinity/README.md) | An inductive set; no finite universe has one; ω as what all inductive sets share |
| [Choice](13_Axioms_of_Set_Theory/choice/README.md) | A theorem for finite families, unnecessary when a rule exists, an axiom only for infinitely many socks |
| [Two balls from one](13_Axioms_of_Set_Theory/two_balls_from_one/README.md) | Banach–Tarski taken apart: the free group doubles itself on 4 373 words, Hausdorff's two rotations are checked free in exact √3 arithmetic, the labelled Cayley graph satisfies B = ψ[A], C = ψ⁻¹[A], B ∪ C = φ[A], and the axiom of choice is the one step onto the sphere |
| [Foundation](13_Axioms_of_Set_Theory/foundation/README.md) | No set is its own member; every set has a rank; a two-cycle breaks the axiom only once {a, b} exists |
| [Ordinals](13_Axioms_of_Set_Theory/ordinals/README.md) | Transitive sets well-ordered by ∈; Goodstein sequences, a theorem about integers whose only proof uses ordinals |
| [Axiom katas](13_Axioms_of_Set_Theory/axiom_katas/README.md) | Exercises from Jech, Cunningham and Kunen, each checked on a small universe before you prove it, with the five proof moves |

[**14_Metric_Spaces/**](14_Metric_Spaces/README.md) — *What does analysis need from a distance?*

The fourteenth chapter takes the four properties of a distance and nothing else, and defines a limit, a continuous function and a complete space from them, so that each definition holds at once for the line, the plane under three metrics, n dimensions and strings of bits. Every definition is run: the N for an ε, the δ for an ε, the one ε that breaks the step function, the Cauchy sequence of rationals with no rational limit. The triangle inequality for the Euclidean distance, checked but not proved in the analytic geometry chapter, is proved at the end.

| Lesson | What it teaches |
|---|---|
| [Open balls: three metrics, the same open sets](14_Metric_Spaces/open_balls/README.md) | An open ball is the points closer than r; a set is open when every point keeps a ball inside; cheb ≤ eucl ≤ taxi ≤ 2 cheb proved in three lines and checked on 2 401 pairs, so the three balls nest and the three metrics share every open set; the discrete metric, whose balls are a point or everything, does not |
| [Convergence: a limit is a statement about every ball](14_Metric_Spaces/convergence/README.md) | x_n → L when every ball around L holds a tail; N found for 1/n and three radii with the algebra that makes it work for all n; (−1)ⁿ has no limit by one ball; limits are unique by two disjoint balls; three equivalent metrics give three N and one limit; under the discrete metric 1/n stops converging |
| [Continuity by ε and δ](14_Metric_Spaces/continuity/README.md) | f sends a δ-ball around p into the ε-ball around f(p); δ = min(1, ε/7) for x² at 3 with the two-line reason; the step function has one ε that defeats every δ, witness x = −δ/2; the distance to a point is continuous with δ = ε by the triangle inequality; the identity between equivalent metrics is a homeomorphism; out of a discrete space every function is continuous |
| [Cauchy sequences and completeness](14_Metric_Spaces/completeness/README.md) | Terms within ε of each other, no limit named; Newton's iteration for √2 in exact fractions is Cauchy in ℚ and no rational squares to 2, so ℚ has holes; ℝ is complete by construction, √2 to 12 decimals by isqrt; (0, 1) and ℝ share their open sets and differ in completeness, so completeness is not topological; the discrete metric and ℤ are complete cheaply |
| [The triangle inequality proved: Cauchy–Schwarz](14_Metric_Spaces/cauchy_schwarz/README.md) | |u + tw|² is a quadratic in t that is never negative, so its discriminant is ≤ 0, which is (u·w)² ≤ |u|²|w|²; equality exactly for parallel vectors; checked on 15 625 pairs; the triangle inequality for the Euclidean distance in three lines without a square root, paying the debt the chapter ran up |

[**12_Learning_to_Learn/**](12_Learning_to_Learn/README.md) — *How do you know that you know?* **Now its own library:** the [Learning to Learn library ↗](https://masiarek.github.io/learning-to-learn-library/), built the same way, where the ten lessons that began here live with pages on planning, sleep, exercise and the brain. The chapter page here points across, and the lessons still use this library's mathematics.

| Lesson | What it teaches |
|---|---|
| [Metacognition: judging what you know ↗](https://masiarek.github.io/learning-to-learn-library/01_Knowing_What_You_Know/metacognition/) | Flavell's four abilities, and the one a program can measure: confidence against results, the Brier score, and why honest confidence minimises it |
| [Count the vowels ↗](https://masiarek.github.io/learning-to-learn-library/01_Knowing_What_You_Know/count_the_vowels/) | McGuire's exercise: 3 of 15 phrases remembered after counting vowels, 12 after knowing the goal and the principle |
| [Studying vs learning ↗](https://masiarek.github.io/learning-to-learn-library/01_Knowing_What_You_Know/studying_vs_learning/) | Bloom's six levels climbed on the Pythagorean theorem, up to a formula that re-creates the facts a student would memorise |
| [Spaced retrieval ↗](https://masiarek.github.io/learning-to-learn-library/02_Making_It_Stay/spaced_retrieval/) | The forgetting curve, why testing beats rereading, the study cycle, and why a geometric review schedule makes remembering cost a logarithm |
| [Day or night: perspective taking ↗](https://masiarek.github.io/learning-to-learn-library/03_Believing_You_Can/day_or_night/) | "When does night begin?" has four exact answers in Starbuck, WA, 20:49 to 23:39, one per cutoff; the sorites, and fuzzy logic's third way out |
| [Learned helplessness ↗](https://masiarek.github.io/learning-to-learn-library/03_Believing_You_Can/learned_helplessness/) | Honest counting, (s + 1)/(n + 2), leaves a learner who failed ten times never trying the lever that works; four small successes, or four watched ones, get them started |
| [The buffer hour ↗](https://masiarek.github.io/learning-to-learn-library/04_Planning_the_Work/the_buffer_hour/) | Task times are skewed, so five honestly estimated one-hour tasks fit in five hours one day in thirteen; a reserved hour gives 47%, and a recorded overrun ratio corrects the estimates |
| [Cognitive load ↗](https://masiarek.github.io/learning-to-learn-library/02_Making_It_Stay/cognitive_load/) | Working memory holds about four chunks, and a chunk is whatever practice made automatic: (a+b)² = a² + 2ab + b² is 19 items to a beginner and 1 to an expert; practice, modelled as byte-pair merging, chunks what repeats |
| [Interleaving ↗](https://masiarek.github.io/learning-to-learn-library/02_Making_It_Stay/interleaving/) | A blocked sheet of volume problems asks you to choose a formula 4 times in 12, a mixed exam 7 in 8; a student who reuses the last formula scores 75% on the sheet and 25% on the exam |
| [Focused and diffuse thinking ↗](https://masiarek.github.io/learning-to-learn-library/02_Making_It_Stay/focused_and_diffuse/) | Small uphill steps stop on the nearest hill: a thousand focused steps end where three did, a wide survey finds the right hill but not its top, and focus, step back, focus again reaches the answer in fifteen looks. |

The books behind it, and behind the other chapters, are on the [resources](RESOURCES.md) page.

**Looking for a subject rather than a chapter?** The [topic map](TOPICS.md) sorts every lesson into branches and follows the threads that run between chapters.

## Why a math library and not a Python one

The code here is the *illustration*, never the subject. Mathematics is exact — `1/3` is exactly one third, forever — and that is precisely why a chapter on significant figures has to explain that they are **not** a mathematical idea but a measurement one, living in the gap between the world and the arithmetic.

Python earns its place because it happens to encode several of these distinctions in syntax you can run: `:.2f` versus `:.2g` is decimal places versus significant figures, and `decimal.getcontext().prec` is the only knob in the standard library that counts significant digits. Those are good teaching instruments. They are not the lesson.

## How the library works

```
01_Precision/
  significant_figures/
    README.md                          the lesson  (prose + a generated output block)
    examples/
      significant_figures.py           the program a reader can run
      significant_figures.out          its recorded output — the answer key
```

A lesson page never pastes output by hand. It marks the spot:

```markdown
<!-- output:significant_figures -->
<!-- /output -->
```

and `tools/run_examples.py` fills it from a real run. Inside the markers is generated; outside is yours.

```bash
python3 tools/run_examples.py            # verify, and refill the pages
python3 tools/run_examples.py --update   # accept current output as the answer key
python3 tools/run_examples.py --check    # write nothing, fail on drift (what CI runs)
```

There is a second block kind, `source:`, which pastes the program itself for pages where the code *is* the lesson.

Conventions for anyone writing a page: [CONTRIBUTING.md](CONTRIBUTING.md). What is planned and deliberately not written yet: [ROADMAP.md](ROADMAP.md).

<!-- --8<-- [end:below-hero] -->
