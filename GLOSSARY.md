# Glossary

Terms used across the library, with the page that explains each in full.

**Absolute error** — |x − x̂|, the difference between a value and the truth, in the value's own units (`±0.05 cm`). What `+` and `−` propagate. Defined in [relative error and correct digits](01_Precision/relative_error/README.md); propagated in [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Almost everywhere** — everywhere except on a set of measure zero. The Cantor function's slope is 0 almost everywhere, and the function still climbs from 0 to 1, so an almost-everywhere fact can miss the thing that matters. Probability's name for the same idea is *almost surely*. See [the Cantor function](02_Measure_Zero/cantor_function/README.md).

**Almost surely** — with probability 1, which is not the same as certainly: the exceptions exist, and together they have measure zero. A number drawn at random from [0, 1] is almost surely irrational. See [probability zero](02_Measure_Zero/probability_zero/README.md).

**Cantor function** — also the *devil's staircase*. Read x in base 3, cut after the first 1, turn 2s into 1s, and read the result in base 2. Continuous, climbing from 0 to 1, and flat on every gap of the Cantor set, so its whole rise happens on a set of length 0. See [the Cantor function](02_Measure_Zero/cantor_function/README.md).

**Cardinality** — |A|, the size of a set. For a finite set, the number of members; in general, defined by matching: |A| = |B| when the members can be paired one to one with none left over. The same bars around a number mean absolute value. |A × B| = |A| · |B|; |ℕ| = |even numbers| = ℵ₀; |ℝ| is strictly larger. See [cardinality](04_Sets/cardinality/README.md).

**Cantor set** — what survives when the open middle third of [0, 1] is deleted, then the middle third of every piece left, forever. Uncountably many points and total length 0; exactly the numbers that can be written in base 3 with only 0s and 2s. See [the Cantor set](02_Measure_Zero/cantor_set/README.md).

**Cartesian product** — A × B, the set of every ordered pair (a, b) with a ∈ A and b ∈ B. It has |A| · |B| members, includes pairs with a repeated entry, and is not commutative: A × B and B × A share no member unless A = B. ℝ × ℝ = ℝ² is the coordinate plane. See [the Cartesian product](04_Sets/cartesian_product/README.md).

**Catastrophic cancellation** — the loss of most significant figures when two nearly equal numbers are subtracted. It does not create error; it removes the leading digits that were hiding error already present. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Complex multiplication** — the rule (x₁, y₁) · (x₂, y₂) = (x₁x₂ − y₁y₂, x₁y₂ + x₂y₁) on pairs of reals. It is the whole definition of the complex numbers: i is the pair (0, 1), and i² = −1 is what the rule gives for (0, 1) · (0, 1). See [multiplication as pairs](03_Complex_Numbers/multiplication_as_pairs/README.md).

**Complex multiplication, geometrically** — multiplying by a point z scales the plane by the distance of z from the origin and turns it by the angle of z. Lengths multiply, angles add. So (0, 1) is a quarter turn and i² = −1 says two quarter turns are a half turn. See [multiplication rotates](03_Complex_Numbers/multiplication_rotates/README.md).

**Componentwise relative error** — for vectors, the largest of the individual relative errors, max |xᵢ − x̂ᵢ| / |xᵢ|. A normwise relative error ‖x − x̂‖ / ‖x‖ can report four correct digits while a small component is 10% wrong; this measure cannot. See [relative error and correct digits](01_Precision/relative_error/README.md).

**Conditioning** — how much a problem's output changes for a small change in its input. A property of the *problem*, not of any algorithm; an ill-conditioned problem defeats every method. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Correct rounding** — returning exactly what the chosen rounding function gives for the exact result, as if the operation had been carried out with unlimited precision. IEEE 754 requires it for +, −, ×, ÷ and √, which is why those give the same bits on every conforming machine. See [machine numbers](01_Precision/machine_numbers/README.md).

**Correct significant digits** — a count with only p + 1 possible values and two competing definitions: x and x̂ round to the same p-digit number, or |x − x̂| is under half a unit in the p-th digit of x. The first is not monotone (0.9949 and 0.9951 agree to one and three digits but not two); the second calls 0.123 and 0.127 two-digit agreement. The relative error is the precise measure. See [relative error and correct digits](01_Precision/relative_error/README.md).

**Countable** — able to be written as a list — a first, a second, a third — with every member somewhere in it; equivalently, of cardinality ℵ₀ or finite. The whole numbers and the rationals are countable; [0, 1] is not. Every countable set has measure zero. See [countable sets](02_Measure_Zero/countable_sets/README.md) and [cardinality](04_Sets/cardinality/README.md).

**Diagonal argument** — Cantor's proof that the infinite 0/1 sequences cannot be listed: flip the r-th bit of the r-th row and the result is on no row. It makes ℝ uncountable, and makes the functions from ℕ to {0, 1} outnumber the programs. See [cardinality](04_Sets/cardinality/README.md).

**Dense** — found inside every interval, however short. The rationals are dense in the line and still have measure zero. See [countable sets](02_Measure_Zero/countable_sets/README.md).

**Exact number** — one that was counted or defined rather than measured (ballots cast, inches per foot, π). Has infinitely many significant figures and never limits a calculation. See [exact vs approximate](01_Precision/exact_vs_approximate/README.md).

**Fat Cantor set** — also the *Smith–Volterra–Cantor set*. Built like the Cantor set, but the gaps deleted at step n are 1/4ⁿ long. It contains no interval and still has length 1/2 — the proof that full of gaps does not mean measure zero. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).

**Floating point** — the machine's stand-in for the real numbers: a finite set of exact values, fixed by a radix, a precision and an exponent range, with every result rounded into it. Its errors look like measurement errors and are unrelated to them: the value was known perfectly and the *hardware* could not hold it. What the set is, and which laws of arithmetic survive rounding into it, is [machine numbers](01_Precision/machine_numbers/README.md); how its bits are laid out is covered by the sibling Rust library ([What a float actually stores ↗](https://masiarek.github.io/rust-learning-library/19_Numbers/what_a_float_stores/index.html)); what happens when you subtract two of them is [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Lebesgue's criterion** — a bounded function on a closed interval has a Riemann integral exactly when the points where it is discontinuous form a set of measure zero. Also called the *Lebesgue–Vitali theorem*. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).

**Machine number** — a member of the finite set a floating-point format can represent, fixed by its radix, precision and exponent range. Each one is an exact number; the approximation happens when a real result is rounded into the set. See [machine numbers](01_Precision/machine_numbers/README.md).

**Measure zero** — a set has measure zero if, for every ε > 0, it fits inside a list of intervals whose lengths add up to at most ε. With squares or cubes in place of intervals, the same definition gives zero area or zero volume. Also called a *null set*. See [what measure zero means](02_Measure_Zero/what_measure_zero_means/README.md).

**Nowhere dense** — for a closed set on the line, containing no interval at all: there are gaps everywhere. Both Cantor sets are nowhere dense, but only the standard one has measure zero. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).

**Ordered pair** — (a, b), an object that remembers which entry is first: (a, b) = (c, d) exactly when a = c and b = d. Unlike the set {a, b}, it distinguishes (2, 5) from (5, 2) and does not collapse (3, 3). See [the Cartesian product](04_Sets/cartesian_product/README.md).

**Quadrature** — combining independent uncertainties as √(a² + b²) rather than a + b. Linear addition is the worst case and is correct only for perfectly correlated errors. See [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Relative error** — |x − x̂| / |x|, the error as a fraction of the true value (`0.81%`); equivalently |ρ| where x̂ = x(1 + ρ). Undefined at x = 0, unchanged by a change of units, and the measure numerical analysis reports in place of a count of correct digits. What `×` and `÷` propagate, and the reason their rule counts significant figures. Defined in [relative error and correct digits](01_Precision/relative_error/README.md); propagated in [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Rounding** — the mechanical operation of cutting a number at some place. The *action*; significant figures are the argument for where the action must stop. See [significant figures](01_Precision/significant_figures/README.md).

**Rounding function** — a rule sending every real number to a machine number, or to an infinity. IEEE 754 defines five: toward −∞, toward +∞, toward zero, and to nearest with ties going either to the even significand or away from zero. See [machine numbers](01_Precision/machine_numbers/README.md).

**Scientific notation** — writing a value as mantissa × 10ⁿ, so the mantissa carries the precision claim and the exponent carries the magnitude. The only unambiguous way to write trailing zeros. See [significant figures](01_Precision/significant_figures/README.md).

**Set-builder notation** — {(x, y) | x, y ∈ ℝ}, read "the set of all (x, y) such that x and y are in ℝ": the shape of a member left of the bar, the condition it must meet right of it. Python's set comprehension `{(x, y) for x in S for y in S}` is the same notation, runnable. See [the Cartesian product](04_Sets/cartesian_product/README.md).

**Significant figures** — the digits of a measurement that carry information about the instrument rather than about place value. A claim about knowledge, not a formatting choice. See [significant figures](01_Precision/significant_figures/README.md).

**Stability** — whether a particular *algorithm* preserves the accuracy a well-conditioned problem allows. The textbook quadratic formula is unstable for one of its two roots; a conjugate rearrangement fixes it for free. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Standard model** — the assumption behind rounding error analysis: every basic floating-point operation returns the exact result times (1 + δ) with |δ| ≤ u, the unit roundoff. Checked exactly on thousands of operations in [relative error and correct digits](01_Precision/relative_error/README.md).

**Sterbenz's lemma** — if two floats a and b satisfy b/2 ≤ a ≤ 2b, then a − b is computed exactly. So the subtraction in a catastrophic cancellation adds no error of its own. See [machine numbers](01_Precision/machine_numbers/README.md).

**Subnormal** — a float below the smallest normal one, written with a leading zero digit at the lowest exponent. Subnormals fill the gap between zero and the smallest normal number; without them, a − b could round to 0 while a ≠ b. See [machine numbers](01_Precision/machine_numbers/README.md).

**Tablemaker's dilemma** — an entry computed as 0.124|5000000, correct to a few digits past the bar, cannot be rounded at the bar until some further digit breaks the run of zeros, and nothing says in advance how far out that digit is. An exact tie is possible only for an algebraic value. See [relative error and correct digits](01_Precision/relative_error/README.md).

**Uncountable** — too big to be written as a list. [0, 1] is uncountable, and so is the Cantor set, which still has measure zero. See [the Cantor set](02_Measure_Zero/cantor_set/README.md).

**Unit roundoff** — u = 2⁻⁵³ ≈ 1.1 × 10⁻¹⁶ for binary64: the largest relative error that rounding a real number to the nearest float can make, and the bound on δ in the standard model. See [relative error and correct digits](01_Precision/relative_error/README.md) and [machine numbers](01_Precision/machine_numbers/README.md).

**Zero divisor** — a nonzero number that multiplies some other nonzero number to give zero. Multiplying pairs entry by entry creates them, since (1, 0)(0, 1) = (0, 0), and a zero divisor can never be divided by. Complex multiplication has none: the product's x² + y² is the product of the two factors' x² + y², which is zero only when a factor is (0, 0). See [multiplication can be undone](03_Complex_Numbers/multiplication_can_be_undone/README.md).
