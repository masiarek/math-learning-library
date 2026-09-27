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
- **Sets and size**
    - **Building sets** · from [Sets](04_Sets/README.md)
        - [The Cartesian product](04_Sets/cartesian_product/README.md) — ordered pairs, ℝ², and why A × B is not B × A
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
    - **Linear algebra** · from [Linear Systems](07_Linear_Systems/README.md)
        - [Linear equations and their solutions](07_Linear_Systems/linear_equations/README.md) — an equation is a test, and a solution of a system passes every one
        - ↪ [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) — the definition of a vector space
        - ↪ [Subsets inherit the laws](06_Algebraic_Structures/subsets_inherit_the_laws/README.md) — subspaces
        - ↪ [Maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md) — linear maps
        - ↪ [Linear algebra: a reading guide](reading_guides/linear_algebra/README.md) — why it is useful, what to know first, which book to read
- **Chance and data**
    - **Averages** · from [Statistics](05_Statistics/README.md)
        - [Mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md) — one calculation, three sizes of word
    - **Probability** · from [Measure Zero](02_Measure_Zero/README.md)
        - [Probability zero](02_Measure_Zero/probability_zero/README.md) — probability zero is not impossible, except on a computer

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

### The complex numbers as a field

1. [Multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md) — the pairs, with their rule, form a field.
2. [A definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md) — in any field, a polynomial of degree n has at most n roots.
3. [Roots of unity](03_Complex_Numbers/roots_of_unity/README.md) — which is how the lesson knows that the n solutions of zⁿ = 1 it finds are all of them.
