# Glossary

Terms used across the library, with the page that explains each in full.

**Abelian group** — a group whose operation is commutative, named after Niels Henrik Abel. The integers under +, the vectors under +, and the nonzero fractions under × are abelian; the invertible 2 × 2 matrices under × are not. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).

**Abscissa** — the x-coordinate of a point: its signed distance from the y-axis, positive to the right of it and negative to the left. The y-coordinate is the *ordinate*. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).

**Absolute error** — |x − x̂|, the difference between a value and the truth, in the value's own units (`±0.05 cm`). What `+` and `−` propagate. Defined in [relative error and correct digits](01_Precision/relative_error/README.md); propagated in [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Almost everywhere** — everywhere except on a set of measure zero. The Cantor function's slope is 0 almost everywhere, and the function still climbs from 0 to 1, so an almost-everywhere fact can miss the thing that matters. Probability's name for the same idea is *almost surely*. See [the Cantor function](02_Measure_Zero/cantor_function/README.md).

**Almost surely** — with probability 1, which is not the same as certainly: the exceptions exist, and together they have measure zero. A number drawn at random from [0, 1] is almost surely irrational. See [probability zero](02_Measure_Zero/probability_zero/README.md).

**Arithmetic mean** — the sum of the numbers divided by how many there are; what school calls "the mean" or "the average", and a spreadsheet `AVERAGE`. The one number that can replace every value without changing their sum, so the distances above and below it cancel. The adjective tells it apart from the geometric and harmonic means. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).

**Associative** — (a · b) · c = a · (b · c): the grouping does not change the answer, so a chain of the operation needs no brackets. True for integer addition, string concatenation and composition of functions; false for subtraction and for float addition. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).

**Average** — any single value that stands for a whole set. In everyday speech it almost always means the arithmetic mean, but in statistics the median and the mode are averages too, so "the average salary" can honestly be three different numbers. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).

**Cantor function** — also the *devil's staircase*. Read x in base 3, cut after the first 1, turn 2s into 1s, and read the result in base 2. Continuous, climbing from 0 to 1, and flat on every gap of the Cantor set, so its whole rise happens on a set of length 0. See [the Cantor function](02_Measure_Zero/cantor_function/README.md).

**Cardinality** — |A|, the size of a set. For a finite set, the number of members; in general, defined by matching: |A| = |B| when the members can be paired one to one with none left over. The same bars around a number mean absolute value. |A × B| = |A| · |B|; |ℕ| = |even numbers| = ℵ₀; |ℝ| is strictly larger. See [cardinality](04_Sets/cardinality/README.md).

**Cantor set** — what survives when the open middle third of [0, 1] is deleted, then the middle third of every piece left, forever. Uncountably many points and total length 0; exactly the numbers that can be written in base 3 with only 0s and 2s. See [the Cantor set](02_Measure_Zero/cantor_set/README.md).

**Cartesian plane** — the plane with a pair of perpendicular number lines chosen in it, so that every point is an ordered pair (x, y). Also the *coordinate plane* and the *xy-plane*; the coordinates themselves are *rectangular* or *Cartesian*. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).

**Cartesian product** — A × B, the set of every ordered pair (a, b) with a ∈ A and b ∈ B. It has |A| · |B| members, includes pairs with a repeated entry, and is not commutative: A × B and B × A share no member unless A = B. ℝ × ℝ = ℝ² is the coordinate plane. See [the Cartesian product](04_Sets/cartesian_product/README.md).

**Catastrophic cancellation** — the loss of most significant figures when two nearly equal numbers are subtracted. It does not create error; it removes the leading digits that were hiding error already present. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Category** — a collection of objects and arrows between them, with a composition of arrows that is associative and has identities. Sets with functions, groups with homomorphisms, and vector spaces with linear maps are categories. See [maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md).

**Closed under an operation** — a subset is closed under an operation when applying it to members of the subset always gives a member of the subset. The line y = 2x is closed under + and scaling; the half-plane x ≥ 0 is not closed under scaling by −1. See [subsets inherit the laws](06_Algebraic_Structures/subsets_inherit_the_laws/README.md).

**Coefficient** — a fixed number standing in front of a variable in a linear combination: in 40h + 15c the coefficients are 40 and 15. In a system, aᵢ,ⱼ is the coefficient in equation i in front of variable j. Zero is allowed. See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md).

**Commutative** — a · b = b · a: the order of the two inputs does not matter. True for adding and multiplying numbers; false for subtraction, string concatenation, matrix multiplication and composing maps. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).

**Complex multiplication** — the rule (x₁, y₁) · (x₂, y₂) = (x₁x₂ − y₁y₂, x₁y₂ + x₂y₁) on pairs of reals. It is the whole definition of the complex numbers: i is the pair (0, 1), and i² = −1 is what the rule gives for (0, 1) · (0, 1). See [multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md).

**Complex multiplication, geometrically** — multiplying by a point z scales the plane by the distance of z from the origin and turns it by the angle of z. Lengths multiply, angles add. So (0, 1) is a quarter turn and i² = −1 says two quarter turns are a half turn. See [multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md).

**Componentwise relative error** — for vectors, the largest of the individual relative errors, max |xᵢ − x̂ᵢ| / |xᵢ|. A normwise relative error ‖x − x̂‖ / ‖x‖ can report four correct digits while a small component is 10% wrong; this measure cannot. See [relative error and correct digits](01_Precision/relative_error/README.md).

**Conditioning** — how much a problem's output changes for a small change in its input. A property of the *problem*, not of any algorithm; an ill-conditioned problem defeats every method. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Correct rounding** — returning exactly what the chosen rounding function gives for the exact result, as if the operation had been carried out with unlimited precision. IEEE 754 requires it for +, −, ×, ÷ and √, which is why those give the same bits on every conforming machine. See [machine numbers](01_Precision/machine_numbers/README.md).

**Correct significant digits** — a count with only p + 1 possible values and two competing definitions: x and x̂ round to the same p-digit number, or |x − x̂| is under half a unit in the p-th digit of x. The first is not monotone (0.9949 and 0.9951 agree to one and three digits but not two); the second calls 0.123 and 0.127 two-digit agreement. The relative error is the precise measure. See [relative error and correct digits](01_Precision/relative_error/README.md).

**Countable** — able to be written as a list — a first, a second, a third — with every member somewhere in it; equivalently, of cardinality ℵ₀ or finite. The whole numbers and the rationals are countable; [0, 1] is not. Every countable set has measure zero. See [countable sets](02_Measure_Zero/countable_sets/README.md) and [cardinality](04_Sets/cardinality/README.md).

**De Moivre's formula** — (cos A, sin A)ⁿ = (cos nA, sin nA): the n-th power of a unit point is the unit point at n times the angle. It is "angles add" applied n − 1 times, and its n = 2 and n = 3 cases are the double- and triple-angle formulas. See [roots of unity](03_Complex_Numbers/roots_of_unity/README.md).

**Diagonal argument** — Cantor's proof that the infinite 0/1 sequences cannot be listed: flip the r-th bit of the r-th row and the result is on no row. It makes ℝ uncountable, and makes the functions from ℕ to {0, 1} outnumber the programs. See [cardinality](04_Sets/cardinality/README.md).

**Dense** — found inside every interval, however short. The rationals are dense in the line and still have measure zero. See [countable sets](02_Measure_Zero/countable_sets/README.md).

**Distributive** — a × (b + c) = a × b + a × c, and (a + b) × c = a × c + b × c: the law that links two operations. It is what turns two groups on one set into a ring. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).

**Euler's formula** — e^{it} = (cos t, sin t): the exponential of an imaginary number is the unit point at angle t, in radians. It is what compounding gives, since (1 + it/n)ⁿ is n small turns whose angles add up to t while their stretches fade to nothing, and it is forced by the law e^{a+b} = e^a e^b, because multiplying unit points can only add angles. See [Euler's identity](03_Complex_Numbers/eulers_identity/README.md).

**Euler's identity** — e^{iπ} = −1, the t = π row of Euler's formula: the unit point half a turn from (1, 0) is (−1, 0). It is i² = −1 with the quarter turn cut finer, and the program reaches it exactly as (0, 1)², as (1, 1)⁴ / 4 and as the sixth power of the clock's first mark. `cmath.exp(1j * math.pi)` is not −1 but −1 + 1.2 × 10⁻¹⁶ i, because `math.pi` is not π. See [Euler's identity](03_Complex_Numbers/eulers_identity/README.md).

**Exact number** — one that was counted or defined rather than measured (ballots cast, inches per foot, π). Has infinitely many significant figures and never limits a calculation. See [exact vs approximate](01_Precision/exact_vs_approximate/README.md).

**Fat Cantor set** — also the *Smith–Volterra–Cantor set*. Built like the Cantor set, but the gaps deleted at step n are 1/4ⁿ long. It contains no interval and still has length 1/2 — the proof that full of gaps does not mean measure zero. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).

**Field** — a set with + and × in which both are commutative and associative, both have identities (0 and 1), every member has an inverse under + and every member except 0 has one under ×, and × distributes over +. The rationals, the reals and the complex numbers are fields; the integers are not, because 2 has no inverse. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).

**Floating point** — the machine's stand-in for the real numbers: a finite set of exact values, fixed by a radix, a precision and an exponent range, with every result rounded into it. Its errors look like measurement errors and are unrelated to them: the value was known perfectly and the *hardware* could not hold it. What the set is, and which laws of arithmetic survive rounding into it, is [machine numbers](01_Precision/machine_numbers/README.md); how its bits are laid out is covered by the sibling Rust library ([What a float actually stores ↗](https://masiarek.github.io/rust-learning-library/19_Numbers/what_a_float_stores/index.html)); what happens when you subtract two of them is [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Geometric mean** — the n-th root of the product of n numbers: the one number that can replace every value without changing their product. The right mean for growth rates, which multiply: +100% then −50% is a geometric mean of 0% a year, not the arithmetic +25%. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).

**Group** — a set with an operation that is associative, has an identity, and gives every member an inverse. The integers under +, the nonzero fractions under ×, the invertible matrices under ×, and the n-th roots of unity under × are groups. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).

**Harmonic mean** — n divided by the sum of the reciprocals of n numbers: the one number that keeps the sum of reciprocals. The right mean for speeds over equal distances; 30 km/h out and 60 km/h back averages 40 km/h, not 45. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).

**Homomorphism** — a map f between two sets with operations that keeps the operation: f(a · b) = f(a) ∗ f(b). A linear map is one; so are n ↦ 2ⁿ, the logarithm, the determinant, and the length of a string. A homomorphism of groups sends the identity to the identity and inverses to inverses, which is why 2⁰ = 1, log 1 = 0, T(0) = 0 and det I = 1 are one theorem. See [maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md).

**Identity element** — a member e with a · e = e · a = a for every a: 0 for +, 1 for ×, the empty string for concatenation, the identity matrix for matrix multiplication. There is at most one, since two identities e and e′ give e = e · e′ = e′. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).

**Inverse** — for a member a, a member b with a · b = b · a = e, the identity. −3 is the inverse of 3 under +, and 1/2 is the inverse of 2 under ×. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).

**Isomorphism** — a homomorphism that can be undone, showing two structures are the same one with the members renamed. The logarithm is an isomorphism from the positive numbers under × to the numbers under +, which is how a slide rule multiplies by adding lengths. See [maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md).

**Lebesgue's criterion** — a bounded function on a closed interval has a Riemann integral exactly when the points where it is discontinuous form a set of measure zero. Also called the *Lebesgue–Vitali theorem*. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).

**Linear combination** — a₁x₁ + a₂x₂ + ⋯ + aₙxₙ: each variable multiplied by a fixed number, then added. No powers, no products of variables, no variable inside a function. It keeps sums and multiples, which is what makes it a linear map. See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md).

**Linear equation** — a linear combination set equal to a number, the constant: a₁x₁ + ⋯ + aₙxₙ = d. It does not say what the variables are; it is a test that any n-tuple of numbers passes or fails. See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md).

**Linear map** — a map T between vector spaces with T(u + v) = Tu + Tv and T(av) = aTv. Multiplying by i and projecting onto an axis are linear; x ↦ x + 1 is not, since a linear map always sends 0 to 0. See [maps that keep the laws](06_Algebraic_Structures/maps_that_keep_the_laws/README.md).

**Machine number** — a member of the finite set a floating-point format can represent, fixed by its radix, precision and exponent range. Each one is an exact number; the approximation happens when a real result is rounded into the set. See [machine numbers](01_Precision/machine_numbers/README.md).

**Mean** — a family of averages, each the one number that can replace every value while keeping some total unchanged. The arithmetic mean keeps the sum, the geometric mean the product, the harmonic mean the sum of reciprocals, the quadratic mean the sum of squares. With no adjective it means the arithmetic mean. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).

**Measure zero** — a set has measure zero if, for every ε > 0, it fits inside a list of intervals whose lengths add up to at most ε. With squares or cubes in place of intervals, the same definition gives zero area or zero volume. Also called a *null set*. See [what measure zero means](02_Measure_Zero/what_measure_zero_means/README.md).

**Median** — the middle value once the numbers are sorted, or halfway between the two middle ones: at least half the values are at or below it, and at least half are at or above it. An average but not a mean, and the one a single huge value cannot drag. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).

**Mode** — the value that occurs most often. When several values tie for most often, a set has more than one mode. An average, but not a mean. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).

**Monoid** — a set with an operation that is associative and has an identity, but where members need not have inverses. Strings under concatenation, and the integers under ×. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).

**Nowhere dense** — for a closed set on the line, containing no interval at all: there are gaps everywhere. Both Cantor sets are nowhere dense, but only the standard one has measure zero. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).

**Ordered pair** — (a, b), an object that remembers which entry is first: (a, b) = (c, d) exactly when a = c and b = d. Unlike the set {a, b}, it distinguishes (2, 5) from (5, 2) and does not collapse (3, 3). See [the Cartesian product](04_Sets/cartesian_product/README.md).

**Ordinate** — the y-coordinate of a point: its signed distance from the x-axis, positive above it and negative below. The x-coordinate is the *abscissa*. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).

**Polar form** — a nonzero complex number written as r e^{iθ}: its length r times the unit point at its angle θ. Multiplying two of them multiplies the lengths and adds the angles, which is the law of exponents, and de Moivre's formula is (e^{iθ})ⁿ = e^{inθ}. `cmath.polar` reads r and θ off a number and `cmath.rect` puts them back. See [Euler's identity](03_Complex_Numbers/eulers_identity/README.md).

**Quadrant** — one of the four regions the coordinate axes cut the plane into, numbered I to IV counterclockwise from the upper right. Membership depends only on the signs of x and y, so (1, 1) and (1000, 5) share a quadrant, and a point on an axis, where one coordinate is 0, is in none. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).

**Quadratic mean** — also the *root mean square*: the square root of the mean of the squares, the one number that keeps the sum of squares. The rated value of an AC voltage is one. See [mean, average, arithmetic mean](05_Statistics/mean_vs_average/README.md).

**Quadrature** — combining independent uncertainties as √(a² + b²) rather than a + b. Linear addition is the worst case and is correct only for perfectly correlated errors. See [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Radian** — the unit of angle in which a point of the unit circle turned through angle t travels a distance t along the circle, so a full turn is 2π and a half turn is π. It is the unit Euler's formula needs, because compounding (1 + it/n)ⁿ turns through the number t itself, and it is the reason the identity has a π in it and not 180. See [Euler's identity](03_Complex_Numbers/eulers_identity/README.md).

**Rectangular coordinates** — also *Cartesian coordinates*, after Descartes: the ordered pair (x, y) that locates a point of the plane by its signed distances from two perpendicular number lines, x from the y-axis and y from the x-axis. The origin O = (0, 0) is where the axes cross. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).

**Relative error** — |x − x̂| / |x|, the error as a fraction of the true value (`0.81%`); equivalently |ρ| where x̂ = x(1 + ρ). Undefined at x = 0, unchanged by a change of units, and the measure numerical analysis reports in place of a count of correct digits. What `×` and `÷` propagate, and the reason their rule counts significant figures. Defined in [relative error and correct digits](01_Precision/relative_error/README.md); propagated in [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Ring** — a set with + and × where + makes a commutative group, × is associative with an identity, and × distributes over +. The integers are a commutative ring, and the 2 × 2 matrices are a ring that is not commutative. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).

**Root of unity** — a solution of zⁿ = 1; equivalently, a unit point that is back at (1, 0) after n multiplications by itself. There are exactly n of them, spaced evenly around the unit circle, and the twelfth roots are the marks of a clock face. A *primitive* n-th root needs all n steps to return, and its powers visit all n. See [roots of unity](03_Complex_Numbers/roots_of_unity/README.md).

**Rounding** — the mechanical operation of cutting a number at some place. The *action*; significant figures are the argument for where the action must stop. See [significant figures](01_Precision/significant_figures/README.md).

**Rounding function** — a rule sending every real number to a machine number, or to an infinity. IEEE 754 defines five: toward −∞, toward +∞, toward zero, and to nearest with ties going either to the even significand or away from zero. See [machine numbers](01_Precision/machine_numbers/README.md).

**Scientific notation** — writing a value as mantissa × 10ⁿ, so the mantissa carries the precision claim and the exponent carries the magnitude. The only unambiguous way to write trailing zeros. See [significant figures](01_Precision/significant_figures/README.md).

**Semigroup** — a set with an associative operation and nothing more: no identity or inverses required. The integers under max. See [the laws of an operation](06_Algebraic_Structures/laws_of_an_operation/README.md).

**Set-builder notation** — {(x, y) | x, y ∈ ℝ}, read "the set of all (x, y) such that x and y are in ℝ": the shape of a member left of the bar, the condition it must meet right of it. Python's set comprehension `{(x, y) for x in S for y in S}` is the same notation, runnable. See [the Cartesian product](04_Sets/cartesian_product/README.md).

**Signed distance** — also *directed distance*: a distance with a sign that says which side. The x-coordinate of a point is its signed distance from the y-axis, positive to the right and negative to the left. See [rectangular coordinates](08_Analytic_Geometry/rectangular_coordinates/README.md).

**Significant figures** — the digits of a measurement that carry information about the instrument rather than about place value. A claim about knowledge, not a formatting choice. See [significant figures](01_Precision/significant_figures/README.md).

**Solution** — of a linear equation, an n-tuple (s₁, …, sₙ) that makes it true when sᵢ is put in for xᵢ; of a system, a tuple that is a solution of every equation at once. One equation in two unknowns has a whole line of solutions. See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md).

**Stability** — whether a particular *algorithm* preserves the accuracy a well-conditioned problem allows. The textbook quadratic formula is unstable for one of its two roots; a conjugate rearrangement fixes it for free. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Standard model** — the assumption behind rounding error analysis: every basic floating-point operation returns the exact result times (1 + δ) with |δ| ≤ u, the unit roundoff. Checked exactly on thousands of operations in [relative error and correct digits](01_Precision/relative_error/README.md).

**Sterbenz's lemma** — if two floats a and b satisfy b/2 ≤ a ≤ 2b, then a − b is computed exactly. So the subtraction in a catastrophic cancellation adds no error of its own. See [machine numbers](01_Precision/machine_numbers/README.md).

**Subnormal** — a float below the smallest normal one, written with a leading zero digit at the lowest exponent. Subnormals fill the gap between zero and the smallest normal number; without them, a − b could round to 0 while a ≠ b. See [machine numbers](01_Precision/machine_numbers/README.md).

**Subspace** — a subset of a vector space that is a vector space with the same operations. It needs only three checks — it contains 0, and it is closed under + and under scalar multiplication — because the other laws are inherited. The subspaces of the plane are the origin, the lines through it, and the plane. See [subsets inherit the laws](06_Algebraic_Structures/subsets_inherit_the_laws/README.md).

**System of linear equations** — m linear equations in the same n variables, written with double subscripts: aᵢ,ⱼ is the coefficient in equation i of variable j, and dᵢ is the constant of equation i. Its solutions are the tuples that pass every equation. See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md).

**Tablemaker's dilemma** — an entry computed as 0.124|5000000, correct to a few digits past the bar, cannot be rounded at the bar until some further digit breaks the run of zeros, and nothing says in advance how far out that digit is. An exact tie is possible only for an algebraic value. See [relative error and correct digits](01_Precision/relative_error/README.md).

**Tuple** — an ordered list of numbers, (s₁, …, sₙ), called an n-tuple when it has n entries; a pair is a 2-tuple and a triple a 3-tuple. ℝⁿ is the set of all n-tuples of reals. Order matters: (1, 4) is not (4, 1). See [linear equations and their solutions](07_Linear_Systems/linear_equations/README.md) and [the Cartesian product](04_Sets/cartesian_product/README.md).

**Uncountable** — too big to be written as a list. [0, 1] is uncountable, and so is the Cantor set, which still has measure zero. See [the Cantor set](02_Measure_Zero/cantor_set/README.md).

**Unit roundoff** — u = 2⁻⁵³ ≈ 1.1 × 10⁻¹⁶ for binary64: the largest relative error that rounding a real number to the nearest float can make, and the bound on δ in the standard model. See [relative error and correct digits](01_Precision/relative_error/README.md) and [machine numbers](01_Precision/machine_numbers/README.md).

**Vector space** — a set with an addition and a scalar multiplication satisfying eight conditions: commutativity, two associativities, an additive identity, additive inverses, 1v = v, and two distributive laws. ℝ² is one; so are the functions from any set to ℝ, and the positive numbers with multiplication as their addition. See [a definition is a test](06_Algebraic_Structures/a_definition_is_a_test/README.md).

**Zero divisor** — a nonzero number that multiplies some other nonzero number to give zero. Multiplying pairs entry by entry creates them, since (1, 0)(0, 1) = (0, 0), and a zero divisor can never be divided by. Complex multiplication has none: the product's x² + y² is the product of the two factors' x² + y², which is zero only when a factor is (0, 0). See [multiplication can be undone](03_Complex_Numbers/multiplication_can_be_undone/README.md).
