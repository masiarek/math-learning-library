# Glossary

Terms used across the library, with the page that explains each in full.

**Absolute error** — the difference between a value and the truth, in the value's own units (`±0.05 cm`). What `+` and `−` propagate. See [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Almost surely** — with probability 1, which is not the same as certainly: the exceptions exist, and together they have measure zero. A number drawn at random from [0, 1] is almost surely irrational. See [probability zero](02_Measure_Zero/probability_zero/README.md).

**Cantor set** — what survives when the open middle third of [0, 1] is deleted, then the middle third of every piece left, forever. Uncountably many points and total length 0; exactly the numbers that can be written in base 3 with only 0s and 2s. See [the Cantor set](02_Measure_Zero/cantor_set/README.md).

**Catastrophic cancellation** — the loss of most significant figures when two nearly equal numbers are subtracted. It does not create error; it removes the leading digits that were hiding error already present. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Conditioning** — how much a problem's output changes for a small change in its input. A property of the *problem*, not of any algorithm; an ill-conditioned problem defeats every method. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Countable** — able to be written as a list — a first, a second, a third — with every member somewhere in it. The whole numbers and the rationals are countable; [0, 1] is not. Every countable set has measure zero. See [countable sets](02_Measure_Zero/countable_sets/README.md).

**Dense** — found inside every interval, however short. The rationals are dense in the line and still have measure zero. See [countable sets](02_Measure_Zero/countable_sets/README.md).

**Exact number** — one that was counted or defined rather than measured (ballots cast, inches per foot, π). Has infinitely many significant figures and never limits a calculation. See [exact vs approximate](01_Precision/exact_vs_approximate/README.md).

**Fat Cantor set** — also the *Smith–Volterra–Cantor set*. Built like the Cantor set, but the gaps deleted at step n are 1/4ⁿ long. It contains no interval and still has length 1/2 — the proof that full of gaps does not mean measure zero. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).

**Floating point** — the machine's binary approximation of a real number. Its errors look like measurement errors and are unrelated to them: the value was known perfectly and the *hardware* could not hold it. What a float *stores* is covered in full by the sibling Rust library ([What a float actually stores ↗](https://masiarek.github.io/rust-learning-library/19_Numbers/what_a_float_stores/index.html)); what happens when you subtract two of them is [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Lebesgue's criterion** — a bounded function on a closed interval has a Riemann integral exactly when the points where it is discontinuous form a set of measure zero. Also called the *Lebesgue–Vitali theorem*. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).

**Measure zero** — a set has measure zero if, for every ε > 0, it fits inside a list of intervals whose lengths add up to at most ε. With squares or cubes in place of intervals, the same definition gives zero area or zero volume. Also called a *null set*. See [what measure zero means](02_Measure_Zero/what_measure_zero_means/README.md).

**Nowhere dense** — for a closed set on the line, containing no interval at all: there are gaps everywhere. Both Cantor sets are nowhere dense, but only the standard one has measure zero. See [the fat Cantor set](02_Measure_Zero/fat_cantor_set/README.md).

**Quadrature** — combining independent uncertainties as √(a² + b²) rather than a + b. Linear addition is the worst case and is correct only for perfectly correlated errors. See [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Relative error** — error as a fraction of the value (`0.81%`). What `×` and `÷` propagate, and the reason their rule counts significant figures. See [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Rounding** — the mechanical operation of cutting a number at some place. The *action*; significant figures are the argument for where the action must stop. See [significant figures](01_Precision/significant_figures/README.md).

**Scientific notation** — writing a value as mantissa × 10ⁿ, so the mantissa carries the precision claim and the exponent carries the magnitude. The only unambiguous way to write trailing zeros. See [significant figures](01_Precision/significant_figures/README.md).

**Significant figures** — the digits of a measurement that carry information about the instrument rather than about place value. A claim about knowledge, not a formatting choice. See [significant figures](01_Precision/significant_figures/README.md).

**Stability** — whether a particular *algorithm* preserves the accuracy a well-conditioned problem allows. The textbook quadratic formula is unstable for one of its two roots; a conjugate rearrangement fixes it for free. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Uncountable** — too big to be written as a list. [0, 1] is uncountable, and so is the Cantor set, which still has measure zero. See [the Cantor set](02_Measure_Zero/cantor_set/README.md).
