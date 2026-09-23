# 01_Precision — how much of this number is real?

**Level:** 101 → 301 · for anyone who took a science class

Every number you meet outside pure mathematics arrived by some process, and that process set a limit on how much of it you may believe. This chapter is about finding that limit and respecting it.

It is one argument in six steps. Each lesson answers a question the previous one raises, so they are worth reading in order.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [Exact vs approximate](exact_vs_approximate/README.md) | Which numbers have significant figures at all? |
| 2 | [Significant figures](significant_figures/README.md) | What does the notation claim, and is it just rounding? |
| 3 | [Relative error and correct digits](relative_error/README.md) | How good is an approximation, when a digit count is too crude to say? |
| 4 | [Uncertainty propagation](uncertainty_propagation/README.md) | What are those rules an approximation *of*? |
| 5 | [Machine numbers](machine_numbers/README.md) | What does a computer do with a number it cannot hold? |
| 6 | [Catastrophic cancellation](catastrophic_cancellation/README.md) | Where do the digits go when they go all at once? |

## The through-line

**Mathematics is exact.** `1/3` is exactly one third, `3,200,000 + 2` is exactly `3,200,002`, and no theorem in this chapter says otherwise. The first two lessons live in the gap between mathematics and the world — the gap opened by *measuring* something rather than counting or defining it.

That gap has a well-developed theory, and significant figures are its introductory dialect: a rule you can apply with no calculus and no error bars, taught in one class period. Lesson 3 asks what the dialect was trying to say — how good an approximation is, measured or computed — and finds that "correct to three digits" has no definition that behaves, while a bound on the relative error does. Lesson 4 is the real thing the dialect was translating. Lesson 5 opens a second gap, between mathematics and the machine: a number known perfectly still has to be rounded into a finite set, and lesson 3's relative error is exactly what that rounding costs. Lesson 6 is where the two gaps meet, and where every version of the rule, dialect and original alike, has to concede that the digits are simply gone.

The chapter ends in **numerical analysis**, which is where this stops being a science-class topic and becomes mathematics again: conditioning is a property of a problem, stability a property of an algorithm, and telling them apart is a genuine skill with real consequences for code.

## A note on the code

The examples are Python, stdlib-only, and they are illustrations rather than the subject. Python is used here because it happens to encode two of this chapter's distinctions in runnable syntax — `:.2f` versus `:.2g`, and `decimal.getcontext().prec` — which makes them things you can try instead of things you have to take on faith.
