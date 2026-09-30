# Euler's formula: a lesson plan

**Level:** reference · for anyone who watched Grant Sanderson's talk on e^{πi} = −1 and got lost, and wants to know what to learn first, and in what order

**One line:** The talk leans on ten ideas from four subjects, exponents, the plane, the circle and calculus; learned in this order, each needs only the ones before it, the first six need no calculus, and every one has a lesson in this library.

Every other page in this library is a lesson, one idea backed by a program. This one is a plan. It is for the talk [*Designing Math* ↗](https://youtu.be/bLSLN96Gn-w), which Grant Sanderson of 3Blue1Brown gave at Config 2026, and for the lesson here that follows it, [Euler's identity](../../03_Complex_Numbers/eulers_identity/README.md). The talk moves fast because it assumes a lot, and "I am completely lost" usually means one or two missing steps rather than all of them. The plan below lists the steps in order, and says for each one what to learn, which moment of the talk needs it, and which page here teaches it.

## How to use it

Do the [self-check](#a-quick-self-check) first. The first question you cannot answer names the step to start from; everything before it you already have. Then take one step at a time: read the lesson it points to, run that lesson's program, and move on when the step's one-sentence summary makes sense to you. When you reach step 10, watch the talk again with [the slide-by-slide table](#the-talk-slide-by-slide) open beside it.

## The plan

### Part A: exponents, no calculus

**Step 1. Exponents and their one law.** 2³ means 2 · 2 · 2, and 2³ · 2⁴ = 2⁷ because the multiplications just line up. The law that matters is *adding exponents multiplies*: a^(m+n) = aᵐ · aⁿ. It forces 2⁰ = 1 and 2⁻¹ = 1/2, and it is the only law of exponents the talk uses. **Take away:** adding inputs multiplies outputs.
- *In the talk:* e^x = e · e ⋯ e, "x times", crossed out as "nonsense if x is complex". Counting multiplications only works for whole x, and the talk is warning that something else has to take over.
- *Here:* [a definition is a test](../../06_Algebraic_Structures/a_definition_is_a_test/README.md), which proves x⁰ = 1 from the laws instead of declaring it; [maps that keep the laws](../../06_Algebraic_Structures/maps_that_keep_the_laws/README.md#a-map-that-can-be-undone), the logarithm as the map that turns multiplying into adding, and the exponential as the same map run backwards.
- *Elsewhere:* [Algebra 1, Khan Academy ↗](https://www.khanacademy.org/math/algebra), the unit on exponents.

**Step 2. The number e.** e = 2.71828… is not defined by multiplying. It is what compound interest settles on: 1 at 100% a year, paid in n instalments of 1/n, grows to (1 + 1/n)ⁿ, and as n grows that heads for e. **Take away:** e is the number growth settles on when it is compounded ever more often.
- *In the talk:* the e in every equation.
- *Here:* [e is where the motion is at time 1](../../09_Calculus/velocity_equals_position/README.md#e-is-where-the-motion-is-at-time-1); the doubling-time example in the [precalculus reading guide](../precalculus/README.md#what-a-precalculus-problem-looks-like); section 1 of [Euler's identity](../../03_Complex_Numbers/eulers_identity/README.md#what-does-it-mean).
- *Elsewhere:* [An intuitive guide to exponential functions and e, BetterExplained ↗](https://betterexplained.com/articles/an-intuitive-guide-to-exponential-functions-e/).

### Part B: the plane and complex numbers, no calculus

**Step 3. The plane as pairs of numbers.** A point of the plane is a pair (x, y): x is its signed distance from the vertical axis, y its signed distance from the horizontal one. **Take away:** a point is two numbers, and an arrow from the origin is the same thing drawn differently.
- *In the talk:* every grid on every slide.
- *Here:* [rectangular coordinates](../../08_Analytic_Geometry/rectangular_coordinates/README.md#the-idea), and [the Cartesian product](../../04_Sets/cartesian_product/README.md) for ℝ² as a set of pairs.

**Step 4. A complex number is a point.** a + bi is the point (a, b), and i is the point (0, 1), one step up. Adding complex numbers is adding arrows tip to tail. **Take away:** i is not mysterious; it is a place.
- *In the talk:* the arrow to a + bi, and the vertical axis marked i, 2i, 3i.
- *Here:* [multiplication as pairs](../../03_Complex_Numbers/multiplication_as_pairs/README.md), especially [why x + yi is the same thing](../../03_Complex_Numbers/multiplication_as_pairs/README.md#why-x-yi-is-the-same-thing).
- *Elsewhere:* [Complex number fundamentals, 3Blue1Brown ↗](https://www.3blue1brown.com/lessons/ldm-complex-numbers/), a lecture by the same speaker.

**Step 5. Multiplying by i turns 90°.** i · (a + bi) = −b + ai: the a becomes ai, and the bi becomes bi · i = −b. Every arrow turns a quarter turn counterclockwise, and i² = −1 says that two quarter turns make a half turn. **Take away:** "times i" means "turn a quarter turn".
- *In the talk:* "× i" beside a + bi, the picture of bi · i = −b, and later the label "Rotate 90°".
- *Here:* [multiplying by (0, 1) is a quarter turn](../../03_Complex_Numbers/multiplication_rotates/README.md#multiplying-by-0-1-is-a-quarter-turn), and [angles add](../../03_Complex_Numbers/multiplication_rotates/README.md#angles-add) for multiplying by any point of the circle.

### Part C: the circle, no calculus

**Step 6. The unit circle, cos, sin and radians.** On the circle of radius 1, the point at angle t is (cos t, sin t). Measured in radians, t is also the distance walked round the circle from 1, so half a turn is π and a whole turn 2π. **Take away:** in radians, angle is distance walked.
- *In the talk:* the first picture, a circle of radius 1 with its upper half labelled π.
- *Here:* [radians](../../09_Calculus/radians/README.md), especially [the angle is the distance walked](../../09_Calculus/radians/README.md#the-angle-is-the-distance-walked); [the clock face](../../03_Complex_Numbers/roots_of_unity/README.md#the-clock-face) of the roots of unity, twelve points of the unit circle computed exactly.
- *Elsewhere:* [Trigonometry, Khan Academy ↗](https://www.khanacademy.org/math/trigonometry), the units on the unit circle and radians.

### Part D: calculus, as motion

**Step 7. A derivative is a velocity.** If a point is at x(t) at time t, its average velocity over a short time h is (x(t + h) − x(t)) / h, and its velocity at the instant is what those averages settle on as h shrinks. That is the derivative, d/dt x. Over a short time dt, the point moves by about velocity · dt. **Take away:** the velocity arrow says where the position arrow goes next.
- *In the talk:* the two arrows, Position and Velocity, the second drawn from the tip of the first, and the box around d/dt.
- *Here:* [the derivative is a velocity](../../09_Calculus/derivative_as_velocity/README.md), especially [a motion that speeds up](../../09_Calculus/derivative_as_velocity/README.md#a-motion-that-speeds-up) and [stepping with a velocity](../../09_Calculus/derivative_as_velocity/README.md#stepping-with-a-velocity).
- *Elsewhere:* [Essence of calculus, 3Blue1Brown ↗](https://www.3blue1brown.com/topics/calculus), chapters 1 and 2.

**Step 8. e^t is its own velocity.** Start at 1 and always move with velocity equal to your position: you are at e^t at time t. Make the velocity k times the position and you are at e^(kt), because it is the same motion on a clock k times as fast, so d/dt e^(kt) = k · e^(kt). That factor k is the chain rule. **Take away:** k says what to do to the position arrow to get the velocity arrow.
- *In the talk:* d/dt e^t = e^t with e⁰ = 1; "Double", d/dt e^(2t) = 2 · e^(2t); "Flip and squish", d/dt e^(−0.5t) = −0.5 · e^(−0.5t); and the readouts e^(2·0.29) = 1.78… and e^(−0.5·0.60) = 0.74….
- *Here:* [velocity equals position](../../09_Calculus/velocity_equals_position/README.md), especially [double, or flip and squish](../../09_Calculus/velocity_equals_position/README.md#double-or-flip-and-squish).
- *Elsewhere:* [Essence of calculus ↗](https://www.3blue1brown.com/topics/calculus), chapter 4 for the chain rule and chapter 5 for e.

**Step 9. Velocity i · position goes round the circle.** Put k = i. The velocity is the position turned 90° (step 5), so it is always at right angles to the position: the point moves round the origin and never toward it or away. The velocity is as long as the position, 1, so the point moves at speed 1 and has walked a distance t after a time t, which is angle t in radians (step 6). After a time π it has walked half the circle, to −1. **Take away:** e^{iπ} = −1 says that walking π round the unit circle from 1 lands on −1.
- *In the talk:* "Rotate 90°", d/dt e^{it} = i · e^{it}; the complex plane with the velocity pointing straight up from 1; the ring of blue position arrows with green velocity arrows at their tips; the field of arrows, and e^{i·3.14} = −1.00 + 0.00i.
- *Here:* [the talk's version](../../03_Complex_Numbers/eulers_identity/README.md#the-talks-version-velocity-is-position-turned-a-quarter-turn) in Euler's identity, whose section 3 steps the motion and reproduces those readouts; [the velocity of a turning point](../../09_Calculus/radians/README.md#the-velocity-of-a-turning-point) in radians.
- *Elsewhere:* [e^{iπ} in 3.14 minutes, 3Blue1Brown ↗](https://www.youtube.com/watch?v=v0YEaeIClKY), this step as a short animation.

**Step 10. The other road: power series.** e^x = 1 + x + x²/2 + x³/6 + ⋯, because "velocity = position" forces every coefficient. Put x = πi in and each term is the one before it turned a quarter turn and scaled by π/k; laid end to end, the arrows spiral in onto −1. The even terms make cos and the odd terms sin. **Take away:** the same identity, reached by adding instead of by moving.
- *In the talk:* the series e^{πi} = 1 + πi + ½(πi)² + ⋯ with green arrows labelled (π²/2)·i², (π³/6)·i³, (π⁴/24)·i⁴, and later the same at t = 3.23.
- *Here:* [power series](../../09_Calculus/power_series/README.md), especially [the coefficients are forced](../../09_Calculus/power_series/README.md#the-coefficients-are-forced) and [cos and sin fall out](../../09_Calculus/power_series/README.md#put-in-it-cos-and-sin-fall-out); [the series](../../03_Complex_Numbers/eulers_identity/README.md#the-series-the-way-a-course-proves-it) in Euler's identity, which prints the spiral term by term.
- *Elsewhere:* [Essence of calculus ↗](https://www.3blue1brown.com/topics/calculus), chapter 11.

Then read [Euler's identity](../../03_Complex_Numbers/eulers_identity/README.md) from the top. Its three questions are the talk's, and [how is it used?](../../03_Complex_Numbers/eulers_identity/README.md#how-is-it-used) is the part the talk leaves for later.

## The talk, slide by slide

The screens are listed in the order they were shared from the talk, not necessarily the order it shows them.

| On the screen | What it says | Step | Read |
|---|---|---|---|
| e^{πi} = −1 next to a circle of radius 1, its upper half labelled π | Walk π round the circle from 1 and you are at −1 | 6 | [Radians](../../09_Calculus/radians/README.md) |
| An arrow to a + bi, then "× i", and bi · i = −b | Multiplying by i turns every arrow a quarter turn | 4, 5 | [Multiplication rotates](../../03_Complex_Numbers/multiplication_rotates/README.md) |
| e^x = e · e ⋯ e, x times, and "Nonsense if x is complex" | Counting multiplications works only for whole x | 1, 2 | [Euler's identity](../../03_Complex_Numbers/eulers_identity/README.md#what-does-it-mean) |
| e^x = 1 + x + ½x² + ⋯, then e^{πi} = 1 + πi + ⋯ with green arrows | The series; each term is the last turned 90° | 10 | [Power series](../../09_Calculus/power_series/README.md) |
| "What does it mean? Why does it want to be true?" | The talk's questions | all | [Euler's identity](../../03_Complex_Numbers/eulers_identity/README.md#three-questions) |
| d/dt e^t = e^t, Velocity and Position, e⁰ = 1 | The point's velocity is its position | 7, 8 | [Velocity equals position](../../09_Calculus/velocity_equals_position/README.md) |
| "Double": d/dt e^(2t) = 2 · e^(2t), and e^(2·0.29) = 1.78… | Velocity twice the position; the 2 is the chain rule | 8 | [Double, or flip and squish](../../09_Calculus/velocity_equals_position/README.md#double-or-flip-and-squish) |
| "Flip and squish": d/dt e^(−0.5t) = −0.5 · e^(−0.5t), and 0.74… | Velocity points back, half as long; the point decays toward 0 | 8 | [Double, or flip and squish](../../09_Calculus/velocity_equals_position/README.md#double-or-flip-and-squish) |
| "Rotate 90°": d/dt e^{it} = i · e^{it} | Velocity is the position turned a quarter turn | 5, 9 | [The talk's version](../../03_Complex_Numbers/eulers_identity/README.md#the-talks-version-velocity-is-position-turned-a-quarter-turn) |
| "Complex plane": Position to 1, Velocity straight up | At the start the point moves straight up | 9 | [The velocity of a turning point](../../09_Calculus/radians/README.md#the-velocity-of-a-turning-point) |
| A ring of blue arrows with green arrows at their tips | Everywhere on the circle, the velocity is at right angles and of length 1 | 9 | [The velocity of a turning point](../../09_Calculus/radians/README.md#the-velocity-of-a-turning-point) |
| A field of arrows, and e^{i·3.14} = −1.00 + 0.00i | Carried along for a time π, the point is at −1 | 6, 9 | [The talk's version](../../03_Complex_Numbers/eulers_identity/README.md#the-talks-version-velocity-is-position-turned-a-quarter-turn) |
| e^{it} = 1 + it + ⋯ at t = 3.23, a spiral ending on a circle | The series lands on the unit circle at angle t, for every t | 10 | [Cos and sin fall out](../../09_Calculus/power_series/README.md#put-in-it-cos-and-sin-fall-out) |

## A quick self-check

Try each question before reading its answer below. The first you cannot do is the step to start from.

1. Write 2³ · 2⁴ as one power of 2. Why must 2⁰ be 1? *(step 1)*
2. Put 1 in a bank at 100% a year, paid monthly. How much is there after a year? *(step 2)*
3. Where is the point 3 + 2i, and where is it after multiplying by i? *(steps 3 to 5)*
4. What are i², i³ and i⁴, and what turn is each? *(step 5)*
5. How many radians is a quarter turn? Walking round the unit circle from 1, how far have you gone when you reach −1? *(step 6)*
6. A point is at x = t² at time t. What is its velocity at t = 3? *(step 7)*
7. A point starts at 1, and its velocity is always twice its position. Where is it at time 1/2? *(step 8)*
8. A point starts at 1, and its velocity is always its position turned a quarter turn counterclockwise. How fast does it move, and where is it at time π/2 and at time π? *(step 9)*
9. What are the first four terms of e^x, and what do they add up to at x = 1? *(step 10)*

The answers, computed by the program in this folder:

<!-- output:euler_self_check -->
*Verified output of [`euler_self_check.py`](examples/euler_self_check.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. EXPONENTS (step 1)
   2^3 . 2^4 = 8 . 16 = 128 = 2^7: adding exponents multiplies.
   2^0 . 2^3 must be 2^(0+3) = 2^3, so 2^0 is the number that changes
   nothing when it multiplies: 2^0 = 1.

2. THE NUMBER e (step 2)
   1 in a bank at 100% a year, paid in n instalments of 1/n:
     paid monthly        n = 12         (1 + 1/n)^n = 2.613035
     paid daily          n = 365        (1 + 1/n)^n = 2.714567
     paid every second   n = 31536000   (1 + 1/n)^n = 2.718282
     paid ever more often, the limit              e = 2.718282

3. A COMPLEX NUMBER IS A POINT (steps 3 to 5)
   3 + 2i is the point (3, 2). Times i, the point (0, 1): (-2, 3),
   which is -2 + 3i: the same arrow turned a quarter turn counterclockwise.

4. POWERS OF i (step 5)
   i^1 = (0, 1)
   i^2 = (-1, 0)
   i^3 = (0, -1)
   i^4 = (1, 0)
   Four quarter turns make a whole turn, back to 1. Two make a half turn: i^2 = -1.

5. RADIANS (step 6)
   a quarter turn = pi/2 = 1.570796 radians, a half turn = pi = 3.141593
   From 1 to -1 round the unit circle is half of its length 2 pi: 3.141593.

6. A VELOCITY AT AN INSTANT (step 7)
   x = t^2, average velocity over [3, 3 + 1/10] = 61/10
   x = t^2, average velocity over [3, 3 + 1/1000] = 6001/1000
   x = t^2, average velocity over [3, 3 + 1/1000000] = 6000001/1000000
   The averages are exactly 6 + h, and they settle on 6: the velocity at t = 3.

7. VELOCITY = 2 . POSITION (step 8)
   Start at 1, step to t = 1/2 in 100000 steps: position 2.718268; e = 2.718282.
   Exactly e in the limit: twice the velocity is the motion e^t on a clock
   running twice as fast, so time 1/2 here is time 1 there. d/dt e^(2t) = 2 e^(2t):
   measured at t = 1/2, velocity / position = 2.000002

8. VELOCITY = POSITION TURNED A QUARTER TURN (step 9)
   At the start the position is (1, 0) and the velocity is i . (1, 0) =
   (0, 1): straight up, length 1. Stepping the motion, 10^6 steps:
   t = pi/2  position (0.000000, 1.000001)
   t = pi    position (-1.000005, 0.000000)
   Speed 1 round the circle: a quarter of it, pi/2, reaches i, and half,
   pi, reaches -1. (The straight steps drift outward by a few millionths.)

9. THE SERIES (step 10)
   e^x = 1 + x + x^2/2 + x^3/6 + ...; at x = 1 the first four terms add to
   1 + 1 + 1/2 + 1/6 = 8/3 = 2.666667, already near e = 2.718282.
```
<!-- /output -->

## What you don't need

- **Proofs.** Why the averages in step 7 settle, and why the series in step 10 adds up, are theorems of a calculus course. The talk does not prove them and neither do the lessons; they show why each should be true and measure it.
- **Integrals**, the other half of calculus. Nothing in the talk integrates.
- **Complex analysis.** The talk and the lessons use complex numbers as points of the plane and nothing more.
- **Python beyond running a file.** Every lesson's program runs with `python3` and nothing installed, and its output is printed on the page anyway.

## Suggested paths

- **Completely lost:** steps 1 to 10 in order, one lesson at a sitting, then the talk again with the table above.
- **Fine with algebra, never met complex numbers:** steps 4, 5 and 6, then 7 to 10.
- **Fine with complex numbers, never did calculus:** steps 6 to 9; step 10 when you want the second road.
- **Did calculus once and forgot it:** questions 6 to 9 of the self-check, then [Euler's identity](../../03_Complex_Numbers/eulers_identity/README.md) directly.

## Po polsku, w skrócie

Wykład *Designing Math* Granta Sandersona zakłada dziesięć rzeczy z czterech działów i przechodzi przez nie szybko, więc zagubienie zwykle oznacza brak jednego czy dwóch kroków, a nie wszystkich. Najpierw potęgi: dodawanie wykładników to mnożenie wyników, a e = 2,71828 to granica procentu składanego. Potem płaszczyzna: punkt to para liczb, liczba zespolona a + bi to punkt (a, b), a mnożenie przez i obraca każdą strzałkę o 90°. Potem okrąg: punkt pod kątem t to (cos t, sin t), a w radianach kąt to droga przebyta po okręgu, więc pół okręgu to π. Dopiero na końcu analiza, jako ruch: pochodna to prędkość; e^t to ruch, którego prędkość równa się położeniu; dla e^{it} prędkość to położenie obrócone o 90°, więc punkt krąży po okręgu z prędkością 1 i po czasie π jest w −1. Szereg potęgowy to druga droga do tego samego.

Najpierw zrób test z pytaniami powyżej: pierwsze pytanie, na które nie znasz odpowiedzi, wskazuje krok, od którego zacząć. Każdy krok odsyła do lekcji w tej bibliotece, a tabela „slajd po slajdzie" mówi, który krok jest potrzebny do którego ekranu wykładu.

## See also

- [Euler's identity](../../03_Complex_Numbers/eulers_identity/README.md) — the lesson this plan leads to
- [09_Calculus](../../09_Calculus/README.md) — steps 6 to 10, one lesson each
- [03_Complex_Numbers](../../03_Complex_Numbers/README.md) — steps 4 and 5, and where the identity lives
- [Precalculus: a reading guide](../precalculus/README.md) — the course that teaches steps 1, 2, 3 and 6, and which book to learn it from
- [The topic map](../../TOPICS.md#from-exponents-to-eulers-identity) — the same path as a thread through the library
- [*Designing Math*, Grant Sanderson at Config 2026 ↗](https://youtu.be/bLSLN96Gn-w) — the talk
- [Intuitive understanding of Euler's formula, BetterExplained ↗](https://betterexplained.com/articles/intuitive-understanding-of-eulers-formula/) — the same idea in plain words, with no calculus
