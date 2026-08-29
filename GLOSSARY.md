# Glossary

Terms used across the library, with the page that explains each in full.

**Absolute error** — the difference between a value and the truth, in the value's own units (`±0.05 cm`). What `+` and `−` propagate. See [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Catastrophic cancellation** — the loss of most significant figures when two nearly equal numbers are subtracted. It does not create error; it removes the leading digits that were hiding error already present. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Conditioning** — how much a problem's output changes for a small change in its input. A property of the *problem*, not of any algorithm; an ill-conditioned problem defeats every method. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Exact number** — one that was counted or defined rather than measured (ballots cast, inches per foot, π). Has infinitely many significant figures and never limits a calculation. See [exact vs approximate](01_Precision/exact_vs_approximate/README.md).

**Floating point** — the machine's binary approximation of a real number. Its errors look like measurement errors and are unrelated to them: the value was known perfectly and the *hardware* could not hold it. What a float *stores* is covered in full by the sibling Rust library ([What a float actually stores ↗](https://masiarek.github.io/rust-learning-library/19_Numbers/what_a_float_stores/index.html)); what happens when you subtract two of them is [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).

**Quadrature** — combining independent uncertainties as √(a² + b²) rather than a + b. Linear addition is the worst case and is correct only for perfectly correlated errors. See [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Relative error** — error as a fraction of the value (`0.81%`). What `×` and `÷` propagate, and the reason their rule counts significant figures. See [uncertainty propagation](01_Precision/uncertainty_propagation/README.md).

**Rounding** — the mechanical operation of cutting a number at some place. The *action*; significant figures are the argument for where the action must stop. See [significant figures](01_Precision/significant_figures/README.md).

**Scientific notation** — writing a value as mantissa × 10ⁿ, so the mantissa carries the precision claim and the exponent carries the magnitude. The only unambiguous way to write trailing zeros. See [significant figures](01_Precision/significant_figures/README.md).

**Significant figures** — the digits of a measurement that carry information about the instrument rather than about place value. A claim about knowledge, not a formatting choice. See [significant figures](01_Precision/significant_figures/README.md).

**Stability** — whether a particular *algorithm* preserves the accuracy a well-conditioned problem allows. The textbook quadratic formula is unstable for one of its two roots; a conjugate rearrangement fixes it for free. See [catastrophic cancellation](01_Precision/catastrophic_cancellation/README.md).
