# Topic map

**Level:** reference · for finding a page by subject instead of by chapter

**One line:** The sidebar lists the chapters A to Z; this page sorts every lesson by subject into branches, then follows the threads that run between chapters.

The chapter numbers are the suggested reading order, and each chapter is one argument, so inside a chapter the lessons are best read in order. This page is the other way in, for when you know what you want and not which chapter holds it. A lesson sits once in the tree, where it belongs; a ↪ marks a lesson from another branch that is worth reading alongside. The build checks that every lesson appears here.

## The tree

- **Numbers**
    - **How exact is a number?** · from [Precision](01_Precision/README.md)
        - [Exact vs approximate](01_Precision/exact_vs_approximate/README.md) — a counted or defined number has infinitely many significant figures
        - [Significant figures](01_Precision/significant_figures/README.md) — what the digits claim, and why + and × follow different rules
        - [Relative error and correct digits](01_Precision/relative_error/README.md) — the one number to report instead of "correct to p digits"
        - [Uncertainty propagation](01_Precision/uncertainty_propagation/README.md) — the rigorous version of the significant-figure rules
    - **Numbers inside a computer** · from [Precision](01_Precision/README.md)
        - [Machine numbers](01_Precision/machine_numbers/README.md) — a float is an exact member of a finite set, and which laws of arithmetic survive
        - [Catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md) — the subtraction that destroys almost every digit at once
    - **Complex numbers** · from [Complex Numbers](03_Complex_Numbers/README.md)
        - [Multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md) — a complex number is a pair of reals, and i² = −1 falls out of the rule
        - [Multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md) — multiplying scales by a length and turns by an angle
        - [Multiplication can be undone](03_Complex_Numbers/multiplication_can_be_undone/README.md) — why pairs are not multiplied entry by entry
        - [Roots of unity](03_Complex_Numbers/roots_of_unity/README.md) — zⁿ = 1 has exactly n solutions, evenly spaced around a circle
        - [Euler's identity](03_Complex_Numbers/eulers_identity/README.md) — e^{iπ} = −1: the exponential turns adding into multiplying, so an imaginary input can only turn, and half a turn from 1 is −1
        - ↪ [Precalculus: a reading guide](reading_guides/precalculus/README.md) — where complex numbers sit in the course before calculus, what to know first, which book to read
        - ↪ [Euler's formula: a lesson plan](reading_guides/eulers_formula/README.md) — what to learn, in order, to follow Euler's identity and the 3Blue1Brown talk on it
- **Sets and size**
    - **Building sets** · from [Sets](04_Sets/README.md)
        - [What is a set?](04_Sets/what_is_a_set/README.md) — well-defined, extensionality, the empty set, null set, Russell's paradox, separation, no set of all sets
        - [The algebra of sets](04_Sets/algebra_of_sets/README.md) — universal set, complement, De Morgan's laws, distributive and absorption laws, Boolean algebra, Venn regions, ⊆ as a partial order (poset)
        - [Reading a set expression](04_Sets/reading_set_expressions/README.md) — order of operations for sets, precedence from logic, Python's - & ^ | ladder, x ∈ A ∩ x ∈ B and x ∈ A ∧ B as bugs, (1, 2) as pair or interval
        - [Sets in Python](04_Sets/python_sets/README.md) — the bridge: extensionality is ==, separation is a comprehension, | & - ^ as or, and, and-not, xor, no complement without U; links to the Python, Rust and ABAP pages
        - [The Cartesian product](04_Sets/cartesian_product/README.md) — ordered pairs, ℝ², and why A × B is not B × A
        - ↪ [Rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md) — the pairs of ℝ² as points of the plane
    - **Size by matching** · from [Sets](04_Sets/README.md) and [Measure Zero](02_Measure_Zero/README.md)
        - [Cardinality of sets](04_Sets/cardinality/README.md) — size defined by matching, not counting
        - [Countable sets](02_Measure_Zero/countable_sets/README.md) — any set that can be listed, even the rationals, has measure zero
    - **Size by length** · from [Measure Zero](02_Measure_Zero/README.md)
        - [What measure zero means](02_Measure_Zero/what_measure_zero_means/README.md) — fitting a set inside intervals of total length as small as anyone asks
        - [The Cantor set](02_Measure_Zero/cantor_set/README.md) — as many points as the whole interval, and length 0
        - [The fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md) — no interval inside it, yet length 1/2
        - [The Cantor function](02_Measure_Zero/cantor_function/README.md) — a staircase that climbs from 0 to 1 while flat almost everywhere
        - ↪ [Countable sets](02_Measure_Zero/countable_sets/README.md) — the first sets shown to have measure zero
- **Algebra**
    - **Laws and structures** · from [Algebraic Structures](06_Algebraic_Structures/README.md)
        - [The laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md) — every book's list of rules is the same four laws
        - [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) — axioms as a test that any set can pass or fail
        - [Subsets inherit the laws](06_Algebraic_Structures/subsets_inherit_the_laws/README.md) — why a subspace needs three checks, not eight
        - [Maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md) — linear maps, logarithms and determinants have one shape
        - ↪ [Euler's identity](03_Complex_Numbers/eulers_identity/README.md) — the exponential as the map that turns adding into multiplying, followed into the plane
        - ↪ [Precalculus: a reading guide](reading_guides/precalculus/README.md) — exponentials and logarithms as the course before calculus teaches them, and which book to learn them from
    - **Linear algebra** · from [Linear Systems](07_Linear_Systems/README.md)
        - [Linear equations and their solutions](07_Linear_Systems/linear_equations/README.md) — an equation is a test, and a solution of a system passes every one
        - ↪ [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) — the definition of a vector space
        - ↪ [Subsets inherit the laws](06_Algebraic_Structures/subsets_inherit_the_laws/README.md) — subspaces
        - ↪ [Maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md) — linear maps
        - ↪ [Linear algebra: a reading guide](reading_guides/linear_algebra/README.md) — why it is useful, what to know first, which book to read
- **Geometry**
    - **Triangles: Pythagoras, congruence, similarity** · from [Geometry](10_Geometry/README.md)
        - [The Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md) — right triangle, hypotenuse, legs, c² = a² + b²; the converse as a test, acute and obtuse, triangle inequality
        - [Congruent and similar triangles](10_Geometry/congruent_and_similar_triangles/README.md) — SSS, SAS, ASA, why AAA and SSA fail, scale factor, proportional sides
        - ↪ [The distance formula](08_Analytic_Geometry/distance_formula/README.md) — Pythagoras in coordinates
    - **Area, perimeter and volume** · from [Geometry](10_Geometry/README.md)
        - [Area and volume formulas](10_Geometry/area_and_volume_formulas/README.md) — rectangle, triangle, circle, box, sphere, cylinder; dimension, scaling by k, k², k³
        - ↪ [Congruent and similar triangles](10_Geometry/congruent_and_similar_triangles/README.md) — similar figures, areas in the ratio k²
    - **The coordinate plane** · from [Analytic Geometry](08_Analytic_Geometry/README.md)
        - [Rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md) — a point is two signed distances, a quadrant is two signs, and the axes belong to none
        - [The distance formula](08_Analytic_Geometry/distance_formula/README.md) — distance between two points, √((x₂ − x₁)² + (y₂ − y₁)²), order and signs, comparing squared distances
        - [The midpoint formula](08_Analytic_Geometry/midpoint_formula/README.md) — midpoint, average of coordinates, perpendicular bisector, point a fraction t of the way
        - ↪ [The Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md) — the theorem the distance formula is
        - ↪ [Mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md) — each coordinate of the midpoint is one
    - **Graphs of equations: intercepts, symmetry, lines, circles** · from [Analytic Geometry](08_Analytic_Geometry/README.md)
        - [Graphs of equations: intercepts and symmetry](08_Analytic_Geometry/graphs_intercepts_symmetry/README.md) — graph as a set of points, x-intercept, y-intercept, symmetry about the axes and the origin
        - [Lines: slope, equations, parallel and perpendicular](08_Analytic_Geometry/lines_and_slope/README.md) — slope, rise over run, point-slope, slope-intercept, general form, negative reciprocal
        - [Circles: standard form and general form](08_Analytic_Geometry/circles/README.md) — center, radius, unit circle, completing the square
        - ↪ [Linear equations and their solutions](07_Linear_Systems/linear_equations/README.md) — the solution set of Ax + By = C is a line
        - ↪ [Congruent and similar triangles](10_Geometry/congruent_and_similar_triangles/README.md) — why a line has one slope
        - ↪ [The Cartesian product](04_Sets/cartesian_product/README.md) — the set ℝ² that the plane is
        - ↪ [Multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md) — a complex number is a point of this plane, and multiplying by i moves it one quadrant on
        - ↪ [Precalculus: a reading guide](reading_guides/precalculus/README.md) — the course this is the first page of, and which book to read it in
        - ↪ [Radians](09_Calculus/radians/README.md) — an angle measured by the arc it cuts from the unit circle, counterclockwise from the positive x-axis
- **Calculus**
    - **Change as motion** · from [Calculus](09_Calculus/README.md)
        - [The derivative is a velocity](09_Calculus/derivative_as_velocity/README.md) — the velocity at an instant is what average velocities settle on as the time shrinks
        - [Velocity equals position](09_Calculus/velocity_equals_position/README.md) — e^t, the number e and the law of exponents, all from one rule of motion
        - [Radians](09_Calculus/radians/README.md) — in radians the angle is the distance walked round the circle, so d/dt sin t = cos t
        - [Power series](09_Calculus/power_series/README.md) — "velocity = position" forces every coefficient of e^x, and cos and sin fall out of it
        - ↪ [Euler's identity](03_Complex_Numbers/eulers_identity/README.md) — the motion whose velocity is its position turned a quarter turn goes round to −1
        - ↪ [Euler's formula: a lesson plan](reading_guides/eulers_formula/README.md) — the chapter's lessons as steps 6 to 10 of a path to the identity
    - **Related rates: derivatives in use** · from [Calculus](09_Calculus/README.md)
        - [Related rates](09_Calculus/related_rates/README.md) — related rates, chain rule, balloon, ladder, kite, angle of elevation, differentiate first then substitute
        - ↪ [The derivative is a velocity](09_Calculus/derivative_as_velocity/README.md) — what a rate is
        - ↪ [Area and volume formulas](10_Geometry/area_and_volume_formulas/README.md) — the formulas differentiated, and the surface as the volume's rate
        - ↪ [The Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md) — the ladder's equation
- **Logic and proof**
    - **If A then B: converse, contrapositive, if and only if** · from [Logic](11_Logic/README.md)
        - [If A then B: converse, contrapositive and inverse](11_Logic/converse_and_contrapositive/README.md) — implication, hypothesis, conclusion, truth table, converse, inverse, contrapositive, if and only if, counterexample, affirming the consequent
        - ↪ [The Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md) — a theorem whose converse is also true
        - ↪ [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) — a definition as an "if and only if"
        - ↪ [What is a set?](04_Sets/what_is_a_set/README.md) — Russell's paradox: an argument by cases in which both cases fail
        - ↪ [The algebra of sets](04_Sets/algebra_of_sets/README.md) — ∪ ∩ ′ are or, and, not; ⊆ is if–then; De Morgan's laws
        - ↪ [Day or night: perspective taking](12_Learning_to_Learn/day_or_night/README.md) — a definition by cutoff, the sorites, and fuzzy logic's "day and not day"
- **Chance and data**
    - **Averages** · from [Statistics](05_Statistics/README.md)
        - [Mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md) — one calculation, three sizes of word
        - [A share above a cutoff](05_Statistics/share_above_a_cutoff/README.md) — percentile, median, skew, log-normal model, Markov's inequality, Lp(a)
    - **Probability** · from [Measure Zero](02_Measure_Zero/README.md)
        - [Probability zero](02_Measure_Zero/probability_zero/README.md) — probability zero is not impossible, except on a computer
- **Learning to learn**
    - **Knowing what you know** · from [Learning to Learn](12_Learning_to_Learn/README.md)
        - [Metacognition: judging what you know](12_Learning_to_Learn/metacognition/README.md) — Flavell's four abilities, calibration, overconfidence, Brier score, proper scoring rule, rereading vs self-testing
        - [Count the vowels](12_Learning_to_Learn/count_the_vowels/README.md) — McGuire's exercise, levels of processing, knowing the goal, organising principle, 15!
        - ↪ [If A then B: converse, contrapositive and inverse](11_Logic/converse_and_contrapositive/README.md) — why many examples prove nothing: the same distrust of feeling sure
    - **Learning that lasts** · from [Learning to Learn](12_Learning_to_Learn/README.md)
        - [Studying vs learning: Bloom's levels on one theorem](12_Learning_to_Learn/studying_vs_learning/README.md) — whats vs hows and whys, make-an-A vs teach-the-material, Bloom's taxonomy 1956 and 2001, Euclid's formula
        - [Spaced retrieval](12_Learning_to_Learn/spaced_retrieval/README.md) — forgetting curve, testing effect, spacing effect, SM-2, logarithmic cost, McGuire's study cycle, intense study sessions
        - ↪ [The Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md) — the theorem Bloom's levels are climbed on
        - ↪ [Velocity equals position](09_Calculus/velocity_equals_position/README.md) — e^t, the shape of the forgetting curve
    - **Thinking with others** · from [Learning to Learn](12_Learning_to_Learn/README.md)
        - [Day or night: perspective taking and the cutoff under a dichotomy](12_Learning_to_Learn/day_or_night/README.md) — dichotomous thinking, perspective taking, cutoff, twilight, sorites paradox, fuzzy logic, Set Up for Success
        - ↪ [A share above a cutoff](05_Statistics/share_above_a_cutoff/README.md) — another cutoff on a smooth quantity

## Threads across chapters

Each thread follows one idea through lessons in different chapters. They are the links the lessons already make to one another, gathered in one place.

### Floats and exact numbers

A computer holds a finite set of numbers, and that fact reaches well beyond chapter 1.

1. [Machine numbers](01_Precision/machine_numbers/README.md) — the finite set, and which laws of arithmetic survive rounding into it.
2. [The laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md) and [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) — floats fail associativity and distributivity, because each grouping rounds at a different step.
3. [Multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md) — Python's `complex` is two floats, so every warning applies twice.
4. [Probability zero](02_Measure_Zero/probability_zero/README.md) — a finite set has measure zero, so a real number picked at random is almost never a float.
5. [Exact vs approximate](01_Precision/exact_vs_approximate/README.md) → [Mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md) — a count is exact, so dividing by it costs no significant figures.
6. [Linear equations and their solutions](07_Linear_Systems/linear_equations/README.md) — exact fractions, so "a tuple passes" means the two sides are equal, not nearly equal.
7. [The derivative is a velocity](09_Calculus/derivative_as_velocity/README.md) — a derivative measured in floats cannot shrink its step for ever: past h = 10⁻⁸ cancellation takes over.
8. [Euler's identity](03_Complex_Numbers/eulers_identity/README.md) — `cmath.exp(1j * math.pi)` is not −1: the double nearest π falls short of it by 1.2 × 10⁻¹⁶, and the answer sits exactly that far above the axis.

### Two kinds of size

Matching and length are different questions about how big a set is, and they can give opposite answers.

1. [Cardinality of sets](04_Sets/cardinality/README.md) — size by matching: ℕ is the same size as its even numbers, and ℝ is larger.
2. [The Cartesian product](04_Sets/cartesian_product/README.md) → [Countable sets](02_Measure_Zero/countable_sets/README.md) — a product of finite sets can be listed, and ℝ × ℝ cannot.
3. [Countable sets](02_Measure_Zero/countable_sets/README.md) — the matching of ℕ with the rationals, which makes them measure zero.
4. [The Cantor set](02_Measure_Zero/cantor_set/README.md) — uncountable, as large as ℝ by matching, and still length 0.

### Matrices in disguise

Several lessons meet 2 × 2 matrices before any chapter is about them.

1. [Multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md) and [Multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md) → [Maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md) — the pair (x, y) behaves exactly like the matrix [[x, −y], [y, x]], so building ℂ from pairs and building it from matrices build the same thing.
2. [Multiplication can be undone](03_Complex_Numbers/multiplication_can_be_undone/README.md) → [The laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md) — zero divisors, and why the 2 × 2 matrices are a ring and not a field.
3. [Linear equations and their solutions](07_Linear_Systems/linear_equations/README.md) — the coefficients aᵢ,ⱼ of a system, laid out in rows and columns, are where matrices come from.

### Definitions as tests

A definition in the axiomatic style is a test that objects pass or fail, and a theorem proved from the test holds for everything that passes.

1. [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) — the vector-space axioms as a test for whole sets.
2. [Subsets inherit the laws](06_Algebraic_Structures/subsets_inherit_the_laws/README.md) — the shorter test for a subspace.
3. [Linear equations and their solutions](07_Linear_Systems/linear_equations/README.md) — the same idea one level down: an equation is a test for a tuple.
4. [If A then B: converse, contrapositive and inverse](11_Logic/converse_and_contrapositive/README.md) — a definition is an "if and only if" by agreement, while a theorem's converse needs its own proof.

### The plane as pairs

ℝ² is a set of ordered pairs, and three chapters use it as a plane.

1. [The Cartesian product](04_Sets/cartesian_product/README.md) — the set: every (x, y) with x and y real, and why the order matters.
2. [Rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md) — the plane: each pair is a point, each coordinate a signed distance from an axis, and the four quadrants are the four pairs of signs.
3. [Multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md) → [Multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md) — the same points with a multiplication, which turns them; multiplying by i moves a point one quadrant counterclockwise.
4. [Linear equations and their solutions](07_Linear_Systems/linear_equations/README.md) — one equation in x and y has a line of solutions, and each solution is a point of the plane.
5. [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) — the same pairs read as vectors, displacements rather than locations, and the axioms they pass.

### Pythagoras everywhere

One theorem about right triangles turns out to be how every distance in this library is measured.

1. [The Pythagorean theorem and its converse](10_Geometry/pythagorean_theorem/README.md) — c² = a² + b², and the converse that turns it into a test.
2. [Area and volume formulas](10_Geometry/area_and_volume_formulas/README.md) — the diagonal of a square, and the altitude of a triangle, both found by it.
3. [Congruent and similar triangles](10_Geometry/congruent_and_similar_triangles/README.md) — why two sides of a right triangle fix the third, the one case where SSA works.
4. [The distance formula](08_Analytic_Geometry/distance_formula/README.md) — the theorem with the legs read off coordinates.
5. [Circles: standard form and general form](08_Analytic_Geometry/circles/README.md) — the distance formula held fixed, with twelve whole-number points on x² + y² = 25.
6. [Lines: slope, equations, parallel and perpendicular](08_Analytic_Geometry/lines_and_slope/README.md) — perpendicular slopes, checked by the converse.
7. [Multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md) — the length of a complex number, √(x² + y²), is the same formula measured from 0.
8. [Catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md) — the Burj Khalifa example subtracts two nearly equal squares, and a calculator pays for it.
9. [Related rates](09_Calculus/related_rates/README.md) — ladders and travellers: x² + y² = z², differentiated in time.
10. [Studying vs learning](12_Learning_to_Learn/studying_vs_learning/README.md) — Bloom's six levels climbed on the theorem, up to Euclid's formula for every whole-number right triangle.

### Scale factor k

1. [Area and volume formulas](10_Geometry/area_and_volume_formulas/README.md) — lengths times k, areas times k², volumes times k³.
2. [Congruent and similar triangles](10_Geometry/congruent_and_similar_triangles/README.md) — similar triangles are one triangle scaled by k.
3. [Multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md) — multiplying by a complex number scales by its length and turns, so every triangle goes to a similar one.
4. [The midpoint formula](08_Analytic_Geometry/midpoint_formula/README.md) — k = ½: halfway across and halfway up is halfway along.
5. [Lines: slope, equations, parallel and perpendicular](08_Analytic_Geometry/lines_and_slope/README.md) — every rise-over-run triangle on a line is a scaled copy of every other.
6. [Related rates](09_Calculus/related_rates/README.md) — the cyclists' triangle grows by a scale factor 20t, so its rate of growth never changes.

### From exponents to Euler's identity

The path of [Euler's formula: a lesson plan](reading_guides/eulers_formula/README.md), through the pages this library has for it.

1. [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) → [Maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md) — the exponent laws, and the exponential as the map that turns adding into multiplying.
2. [Rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md) → [Multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md) — the plane as pairs, and a complex number as a point of it.
3. [Multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md) — multiplying by i is a quarter turn.
4. [Radians](09_Calculus/radians/README.md) → [Roots of unity](03_Complex_Numbers/roots_of_unity/README.md) — the unit circle measured by distance walked, and twelve points of it computed exactly.
5. [The derivative is a velocity](09_Calculus/derivative_as_velocity/README.md) → [Velocity equals position](09_Calculus/velocity_equals_position/README.md) — the talk's two arrows, and the rule velocity = k · position.
6. [Euler's identity](03_Complex_Numbers/eulers_identity/README.md) — k = i, and the point goes round the circle to −1.
7. [Power series](09_Calculus/power_series/README.md) — the other road, adding arrows instead of moving.

### The complex numbers as a field

1. [Multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md) — the pairs, with their rule, form a field.
2. [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) — in any field, a polynomial of degree n has at most n roots.
3. [Roots of unity](03_Complex_Numbers/roots_of_unity/README.md) — which is how the lesson knows that the n solutions of zⁿ = 1 it finds are all of them.
