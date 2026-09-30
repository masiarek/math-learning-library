# The Pythagorean theorem and its converse

**Level:** 101 · for anyone reviewing geometry before precalculus, or meeting a² + b² = c² again after many years

**One line:** The theorem turns a right angle into an equation, c² = a² + b², and the converse turns the equation back into a right angle; together they make a test that three lengths pass or fail, and the test only works when c is the longest side.

## The idea

A right triangle is a triangle with one angle of 90°, a square corner. The side opposite that corner is the **hypotenuse**, always the longest side, and the two sides that meet at the corner are the **legs**. Call the legs a and b and the hypotenuse c. The Pythagorean theorem says:

> In a right triangle, the square of the hypotenuse equals the sum of the squares of the legs: **c² = a² + b²**.

That sentence goes one way: *right angle ⇒ equation*. The **converse** goes the other way: *equation ⇒ right angle*. If the square of one side of a triangle equals the sum of the squares of the other two, the triangle is a right triangle, and the right angle is opposite that side. A theorem and its converse are two different claims ([if A then B](../../11_Logic/converse_and_contrapositive/README.md) has the whole story), and a true theorem can have a false converse ("if it is a dog, it has four legs" is true; "if it has four legs, it is a dog" is not). Here both happen to be true, and that is what makes c² = a² + b² useful in both directions: find a missing side when you know the angle is right, or prove the angle is right when you know the sides.

This page follows Section A.2, *Geometry Essentials*, of the review appendix in Michael Sullivan's *Precalculus*, its Examples 1–3 and its problems 7–8 and 13–26. The next page of the book, the distance formula in section 1.1, is where the theorem is first put to work; it has [its own lesson](../../08_Analytic_Geometry/distance_formula/README.md).

## Symbol by symbol

| Piece | Say it | What it means |
|---|---|---|
| right angle, 90°, ⌐ | "right angle" | a square corner, a quarter of a full turn. The little square drawn in the corner of a figure is the symbol for it. |
| right triangle | "right triangle" | a triangle with one right angle. It cannot have two: the three angles of any triangle add up to 180°, so two right angles would leave 0° for the third. |
| hypotenuse, c | "hypotenuse" | the side *opposite* the right angle, the one that does not touch the square corner. Always the longest side. |
| legs, a and b | "legs" | the two sides that form the right angle. Which one is a and which is b does not matter, because a² + b² = b² + a². |
| c² | "c squared" | c · c, the area of a square whose side is c. The theorem is a statement about three squares drawn on the three sides. |
| √ | "square root of" | the non-negative number whose square is the one under the sign: √25 = 5. From c² = 25, c = 5, not −5, because a length is not negative. |
| converse | "converse" | the statement with the "if" and the "then" swapped. Its truth has to be proved separately. |

## Why it is true: one square, cut two ways

Draw a big square with side a + b. Inside it, put four copies of the right triangle, one in each corner, with their hypotenuses facing in. What is left in the middle is a tilted square whose side is c. So the big square's area can be counted two ways:

(a + b)² = 4 · (ab/2) + c²

Multiply out the left side: a² + 2ab + b². The four triangles are 2ab. Take 2ab away from both sides and what remains is a² + b² = c². Section 2 of the program does this with numbers, and the left-over area always equals a² + b². There are hundreds of proofs of this theorem; this one needs nothing but the area of a square and a triangle, which are on the [next page](../area_and_volume_formulas/README.md).

## The converse as a test

Given three lengths, is it a right triangle? The recipe has two steps, and the first is the one people forget:

1. **Find the longest side.** It is the only candidate for the hypotenuse, because the hypotenuse is always the longest side.
2. **Compare its square with the sum of the other two squares.** Equal: right triangle, and the right angle is opposite the longest side. Not equal: not a right triangle.

Problem 25 lists its sides as 6, 4, 3, with the longest first. Testing 3² against 6² + 4² asks the wrong question. The right question is whether 6² = 36 equals 4² + 3² = 25. It does not.

### Alone and together: the letters are jobs, not names

In a² + b² = c² the letter c does not mean "the third number written down". It is a job: *the side opposite the right angle*. The equation is shorthand for one sentence, (leg)² + (other leg)² = (hypotenuse)², and it only says something true when every side has been given its right job.

Take the 3-4-5 triangle, whose right angle sits between the sides 3 and 4. There are three ways to choose which side stands alone:

| Standing alone, as c | The other two, added | Alone, squared | Equal? |
|---|---|---|---|
| **5**, the hypotenuse | 3² + 4² = 9 + 16 = 25 | 5² = 25 | yes |
| 4, a leg | 3² + 5² = 9 + 25 = 34 | 4² = 16 | no |
| 3, a leg | 4² + 5² = 16 + 25 = 41 | 3² = 9 | no |

It is the same triangle each time. The last two rows fail because they make a claim the theorem never made, "leg² + hypotenuse² = other leg²", and that sentence is false. They could not have worked: two squares added are bigger than either one alone, so whatever stands alone must be the *biggest* side. Put a short side there and the lone square is too small, 16 < 34 and 9 < 41.

Which side of the equals sign doesn't matter. a² + b² = c² and c² = a² + b² are the same equation read in opposite directions. What matters is **alone** and **together**:

1. Find the longest side. That is c.
2. Put c² **alone** on one side of the equals sign, and the other two squares **added** on the other side.
3. Compare.

## Why the converse is true

The converse needs its own proof, and it is short. Take a triangle with sides a, b, c where a² + b² = c². Now build a second triangle on purpose: two legs a and b meeting at a right angle. By the theorem, its third side is √(a² + b²), which is √(c²) = c. So the two triangles have the same three sides, a, b and c, and by the Side-Side-Side rule of [congruent and similar triangles](../congruent_and_similar_triangles/README.md) they are the same triangle. The second one has a right angle between a and b, so the first one does too. The theorem proves its own converse, with one step of congruence in between.

## More than yes or no

When the test fails, *how* it fails still tells you something. Books usually leave this out:

- c² **=** a² + b²: the angle opposite c is **right** (exactly 90°).
- c² **<** a² + b²: that angle is **acute** (less than 90°): c is too short to reach a square corner.
- c² **>** a² + b²: that angle is **obtuse** (more than 90°): c is so long it has pushed the corner open.

Hold two sides at 3 and 4 and let the third grow: at 4 the triangle is acute, at 5 exactly right, at 6 obtuse, and at 7 it has collapsed to a flat line, since 3 + 4 = 7. That last one is the **triangle inequality**: any side must be shorter than the other two added together, or there is no triangle at all. In trigonometry this three-way comparison becomes the law of cosines, c² = a² + b² − 2ab cos C, and the Pythagorean theorem is the case C = 90°, where cos C = 0.

## What follows from the right angle

**Perpendicular.** Two lines that meet at a right angle are *perpendicular*, written ℓ₁ ⊥ ℓ₂, and then all four angles where they cross are 90°. A right angle is a quarter turn: 90°, or π/2 radians (a quarter of the unit circle's circumference 2π), or 100 gradians in surveying.

**The other two angles are acute and complementary.** The angles of a triangle add up to 180°, and the right angle takes 90°, so the other two share the remaining 90°: each is less than 90°, and they add up to exactly 90°. If one is θ, the other is 90° − θ.

**Why the hypotenuse is the longest side.** In any triangle the largest angle is opposite the longest side. The right angle is the largest here, so the side opposite it is the longest. The theorem says the same: c² = a² + b² is bigger than a² or b² alone. But c is still shorter than a + b, because (a + b)² = a² + b² + 2ab, and the 2ab is the gap.

**The two special right triangles.** Two shapes come up so often that their side ratios are worth knowing by heart, and both come straight from the theorem:

| Triangle | How to get it | Sides |
|---|---|---|
| 45°-45°-90° | half a square, cut along its diagonal | 1 : 1 : √2 |
| 30°-60°-90° | half an equilateral triangle, cut down the middle | 1 : √3 : 2 |

In the first, the legs are equal and c² = 1 + 1 = 2. In the second, cutting an equilateral triangle of side 2 in half gives hypotenuse 2 and short leg 1, so the long leg is √(4 − 1) = √3. The short leg is opposite the 30° angle and is always half the hypotenuse.

**The theorem twice: a box's long diagonal.** In a box p × q × r, the diagonal across the bottom face has d₁² = p² + q². That diagonal and the vertical edge r meet at a right angle, so the diagonal from corner to opposite corner has d² = d₁² + r² = **p² + q² + r²**. A 3 × 4 × 12 box has face diagonal 5 and space diagonal 13. This is the [distance formula](../../08_Analytic_Geometry/distance_formula/README.md) in three dimensions.

**Which comes first, Pythagoras or the law of cosines?** For any triangle, the law of cosines says c² = a² + b² − 2ab cos C. At C = 90° the cosine is 0 and Pythagoras is what remains. Some summaries turn this around and call Pythagoras "a consequence of the law of cosines". The order is the other way: the law of cosines is usually *proved* with Pythagoras, by dropping a perpendicular and applying the theorem to the two right triangles it makes. Pythagoras is the foundation, and the law of cosines generalises it. The acute/obtuse test above is the law of cosines without the cosine: −2ab cos C is negative when C is acute and positive when C is obtuse.

## What the program prints

Every length is a whole number or a fraction, so every comparison is exact: "equal" means equal, not "equal to eight decimals".

<!-- output:pythagorean_theorem -->
*Verified output of [`pythagorean_theorem.py`](examples/pythagorean_theorem.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. THE THEOREM: TWO LEGS GIVE THE HYPOTENUSE
   Example 1 and problems 13-18: c^2 = a^2 + b^2, then c = sqrt(c^2).
              a    b     a^2 + b^2 = c^2      c
     Ex 1     4    3         16 + 9 = 25      5
     13       5   12      25 + 144 = 169     13
     14       6    8       36 + 64 = 100     10
     15      10   24     100 + 576 = 676     26
     16       4    3         16 + 9 = 25      5
     17       7   24      49 + 576 = 625     25
     18      14   48   196 + 2304 = 2500     50
   Every answer is a whole number, because the book picked the legs so.
   Legs 1 and 2 give c^2 = 5 and c = sqrt(5) = 2.2361..., which no ruler reads.

2. WHY IT IS TRUE: THE SAME SQUARE CUT TWO WAYS
   A square of side a + b holds four copies of the triangle (each ab/2)
   and a tilted square of side c in the middle. So (a + b)^2 = 4(ab/2) + c^2.
       a   b   (a+b)^2  4 * ab/2  left over  a^2 + b^2
       3   4        49        24         25         25
       5  12       289       120        169        169
       1   2         9         4          5          5
       2   7        81        28         53         53
   The left-over area is c^2 and it always equals a^2 + b^2: expand
   (a+b)^2 = a^2 + 2ab + b^2 and take away the 2ab. No measuring needed.

3. THE CONVERSE AS A TEST: PROBLEMS 19-26
   Sort the sides; the longest is the only candidate for the hypotenuse.
     19  (3, 4, 5)     right: 5^2 = 25 = 9 + 16, hypotenuse 5
     20  (6, 8, 10)    right: 10^2 = 100 = 36 + 64, hypotenuse 10
     21  (4, 5, 6)     acute: 6^2 = 36 < 16 + 25 = 41
     22  (2, 2, 3)     obtuse: 3^2 = 9 > 4 + 4 = 8
     23  (7, 24, 25)   right: 25^2 = 625 = 49 + 576, hypotenuse 25
     24  (10, 24, 26)  right: 26^2 = 676 = 100 + 576, hypotenuse 26
     25  (6, 4, 3)     obtuse: 6^2 = 36 > 9 + 16 = 25
     26  (5, 4, 7)     obtuse: 7^2 = 49 > 16 + 25 = 41
   Only 19, 20, 23, 24 are right. 25 is listed 6, 4, 3: testing 3^2 against
   6^2 + 4^2 would be the wrong question, because 3 is not the longest side.

4. THE TRAP: THE THEOREM NEEDS THE RIGHT SIDE ON THE LEFT
   For 5, 12, 13: 13^2 = 169 and 5^2 + 12^2 = 169: right.
   But 5^2 = 25 is not 12^2 + 13^2 = 313, and 12^2 = 144 is not 5^2 + 13^2 = 194.
   The equation names the side opposite the right angle. Put a leg there
   and a true right triangle fails the test.

5. MORE THAN YES OR NO: THE LONGEST SIDE AGAINST THE OTHER TWO
   Hold two sides at 3 and 4, and let the third one grow.
     3, 4, 4   acute: 4^2 = 16 < 9 + 16 = 25
     3, 4, 5   right: 5^2 = 25 = 9 + 16, hypotenuse 5
     3, 4, 6   obtuse: 6^2 = 36 > 9 + 16 = 25
     3, 4, 7   not a triangle: 3 + 4 = 7 does not exceed 7
   Bigger than 5 opens the angle past 90 degrees; smaller closes it.
   At 7 the triangle has gone flat: 3 + 4 = 7 is a line segment.

6. EXAMPLE 3: HOW FAR CAN YOU SEE FROM THE BURJ KHALIFA?
   The line of sight touches the Earth at a right angle to the radius, so
   (R + h)^2 = R^2 + d^2 with R = 3960 miles and h = 1483 feet = 1483/5280 mile.
   d^2 = (R + h)^2 - R^2 = 2Rh + h^2 = 2224.5789, so d = 47.1654 miles.
   The h^2 term is 0.0789 of that; d is about sqrt(2Rh) = 47.1646.
   A calculator keeping 6 significant figures, the two ways:
     (R + h)^2 - R^2 = 2.2E+3     2Rh + h^2 = 2224.58
   The first subtracts two numbers near 15.7 million that agree in
   their leading digits, and the difference keeps almost none of them.

7. THE TWO SPECIAL RIGHT TRIANGLES, EXACTLY
   45-45-90: half a square of side 1, cut along its diagonal.
     legs 1 and 1:  c^2 = 1 + 1 = 2, so c = sqrt(2).  Ratio 1 : 1 : sqrt(2).
   30-60-90: half an equilateral triangle of side 2, cut down the middle.
     hypotenuse 2, short leg 1:  long leg^2 = 4 - 1 = 3, so it is sqrt(3).  Ratio 1 : sqrt(3) : 2.
   The short leg is opposite the 30 degree angle and is half the hypotenuse.
     scaled by 2: 45-45-90 legs 2, 2, hypotenuse 2 sqrt(2);  30-60-90 sides 2, 2 sqrt(3), 4
     scaled by 5: 45-45-90 legs 5, 5, hypotenuse 5 sqrt(2);  30-60-90 sides 5, 5 sqrt(3), 10

8. THE THEOREM TWICE: THE LONG DIAGONAL OF A BOX
     box            face diagonal^2   space diagonal^2         d
     3 x 4 x 12      3^2 + 4^2 = 25    25 + 12^2 = 169        13
     2 x 3 x 6       2^2 + 3^2 = 13      13 + 6^2 = 49         7
     1 x 1 x 1        1^2 + 1^2 = 2        2 + 1^2 = 3   sqrt(3)
     1 x 4 x 8       1^2 + 4^2 = 17      17 + 8^2 = 81         9
   The face diagonal and the third edge meet at a right angle, so
   d^2 = p^2 + q^2 + r^2. The unit cube's diagonal is sqrt(3).

9. THE HYPOTENUSE IS THE LONGEST SIDE, AND THE OTHER ANGLES ARE ACUTE
   The angles add to 180, the right angle takes 90, so the other two add to 90:
   each is acute, and they are complementary. The largest angle is opposite
   the longest side, so the hypotenuse is the longest. And a + b > c still:
     legs 3, 4     c^2 =    25 < (a + b)^2 =    49, so c =   5.0000 < a + b = 7
     legs 1, 1     c^2 =     2 < (a + b)^2 =     4, so c =   1.4142 < a + b = 2
     legs 5, 12    c^2 =   169 < (a + b)^2 =   289, so c =  13.0000 < a + b = 17
     legs 1, 100   c^2 = 10001 < (a + b)^2 = 10201, so c = 100.0050 < a + b = 101
   (a + b)^2 = a^2 + b^2 + 2ab, and the 2ab is the gap.
```
<!-- /output -->

Section 6 is the book's Example 3, and it hides a warning that belongs to [catastrophic cancellation](../../01_Precision/catastrophic_cancellation/README.md). The book computes d² = (3960 + 1483/5280)² − 3960²: two numbers near 15.7 million, subtracted. On a calculator that keeps six significant figures, both round to the same few leading digits, and the difference keeps almost none. Written as 2Rh + h², which is the same thing expanded, there is no subtraction to lose digits in, and six figures are plenty.

To judge three lengths of your own, give them after the program name; fractions are fine:

```bash
python3 10_Geometry/pythagorean_theorem/examples/pythagorean_theorem.py 7 24 25
python3 10_Geometry/pythagorean_theorem/examples/pythagorean_theorem.py 1/2 2 3/2
```

## Questions

Try each one before opening the answer. The first ones are the book's, the later ones ask what the page implies.

**1. The legs of a right triangle are 10 and 24 (problem 15). Find the hypotenuse.**

<details><summary>Answer</summary>

c² = 10² + 24² = 100 + 576 = 676, so c = √676 = 26. Notice that 10, 24, 26 is 5, 12, 13 doubled.

</details>

**2. Is a triangle with sides 7, 24, 25 a right triangle (problem 23)? If so, which side is the hypotenuse?**

<details><summary>Answer</summary>

The longest side is 25. 25² = 625 and 7² + 24² = 49 + 576 = 625. Equal, so yes, and 25 is the hypotenuse.

</details>

**3. True or false (problem 8): the triangle with sides 6, 8 and 10 is a right triangle.**

<details><summary>Answer</summary>

True: 10² = 100 = 36 + 64. It is the 3-4-5 triangle with every side doubled, and doubling every side keeps every angle (see [congruent and similar triangles](../congruent_and_similar_triangles/README.md)).

</details>

**4. True or false (problem 7): "in a right triangle, the square of the length of the longest side equals the sum of the squares of the lengths of the other two sides."**

<details><summary>Answer</summary>

True, because in a right triangle the longest side is the hypotenuse. The statement is careful: it says *longest side*, not *any side*.

</details>

**5. Sides 6, 4, 3 (problem 25): right or not? What mistake does the order tempt you into?**

<details><summary>Answer</summary>

Not right: the longest side is 6, and 6² = 36 while 4² + 3² = 25. The trap is to put the last number listed, 3, in the place of c. Always sort first.

</details>

**6. The sides are 2, 2, 3 (problem 22). Not right, but is the largest angle acute or obtuse?**

<details><summary>Answer</summary>

3² = 9 and 2² + 2² = 8. The longest side squared is bigger, so the angle opposite it is obtuse, a little more than 90°.

</details>

**7. A right triangle has hypotenuse 13 and one leg 5. Find the other leg.**

<details><summary>Answer</summary>

Rearrange: b² = c² − a² = 169 − 25 = 144, so b = 12. The theorem works backwards too, as long as you subtract from the hypotenuse's square and not the other way round.

</details>

**8. Can a right triangle have legs 3 and 4 and hypotenuse 6? Why can a leg never be the longest side?**

<details><summary>Answer</summary>

No: 3² + 4² = 25 forces c = 5. A leg can never be longest because c² = a² + b² is bigger than a² alone (b is not 0), and for positive lengths, a bigger square means a bigger side.

</details>

**9. Why is it enough to check c² against a² + b² for the longest side only? Could the triangle be right with the right angle somewhere else?**

<details><summary>Answer</summary>

If the triangle had a right angle, the side opposite it would be the hypotenuse, which is the longest side. So a right angle anywhere else is impossible, and the other two checks can only fail. The program's section 4 shows 5-12-13 failing both of them.

</details>

**10. Legs 1 and 1. What is the hypotenuse, and can a ruler measure it exactly?**

<details><summary>Answer</summary>

c = √2 ≈ 1.41421356…, a number that is not a fraction, so its decimal never ends or repeats. Pythagoras's own school is said to have been shaken by this. The theorem is exact, but the answer is exact only as √2.

</details>

**11. Three numbers a, b, c with a² + b² = c² are called a Pythagorean triple. If 3, 4, 5 is one, why is 30, 40, 50 one too?**

<details><summary>Answer</summary>

(10a)² + (10b)² = 100a² + 100b² = 100(a² + b²) = 100c² = (10c)². Any whole-number multiple of a triple is a triple, which is why the book's answers are so often 3-4-5 or 5-12-13 in disguise.

</details>

**12. In Example 3, the book subtracts 3960² from (3960 + 0.28)². Why is that risky on a calculator, and what is the safer form?**

<details><summary>Answer</summary>

Both squares are about 15.7 million and agree in their leading digits, so the subtraction cancels them and leaves mostly rounding error. Expanding first, (R + h)² − R² = 2Rh + h², removes the subtraction. The program shows six-digit arithmetic giving 2.2 × 10³ the first way and 2224.58 the second.

</details>

**13. Sides 3, 4, 7: right, acute, obtuse, or none of these?**

<details><summary>Answer</summary>

None: 3 + 4 = 7, so the "triangle" is a flat line segment. Before the Pythagorean test, three lengths must pass the triangle inequality: each side shorter than the sum of the other two.

</details>

**14. Why is the converse true? Give the idea of the proof in two sentences.**

<details><summary>Answer</summary>

Build a right triangle with legs a and b. The theorem gives it hypotenuse √(a² + b²) = c, so it has the same three sides as the given triangle, and SSS makes them congruent, right angle included.

</details>

**15. A 45-45-90 triangle has legs 7. Find the hypotenuse. A 30-60-90 triangle has hypotenuse 10. Find both legs.**

<details><summary>Answer</summary>

7√2 ≈ 9.90. For the second, the short leg is half the hypotenuse, 5, and the long leg is 5√3 ≈ 8.66. Check: 25 + 75 = 100.

</details>

**16. A box measures 2 × 3 × 6. How long is a rod that fits exactly from one corner to the opposite corner?**

<details><summary>Answer</summary>

d² = 4 + 9 + 36 = 49, so d = 7. Or in two steps: the bottom diagonal is √13, and then √(13 + 36) = 7.

</details>

**17. One acute angle of a right triangle is 35°. What is the other? Could a right triangle have an angle of 95°?**

<details><summary>Answer</summary>

55°, since the two acute angles add up to 90°. No: 90° + 95° is already more than 180°.

</details>

**18. Someone says the Pythagorean theorem is "just a special case of the law of cosines, so it depends on it". What is right and what is wrong about that?**

<details><summary>Answer</summary>

Right: at C = 90° the law of cosines reduces to c² = a² + b². Wrong: the dependence goes the other way. The usual proof of the law of cosines drops a perpendicular and uses Pythagoras on the two right triangles. Using the law to prove the theorem would be circular.

</details>

## How to practise

1. **Problems 13–26 on paper, then the program.** Do each by hand, then check the whole set against section 1 and section 3 of the output above.
2. **Sort first, out loud.** For each triple of lengths, say "the longest is …" before you square anything. It is the one habit that prevents the problem-25 mistake.
3. **Know five triples by sight:** 3-4-5, 5-12-13, 8-15-17, 7-24-25, 20-21-29, and their multiples. Half the book's answers are these.
4. **Invent your own and let the program judge:** `python3 pythagorean_theorem.py 9 40 41`.
5. **The cards.** The Anki deck below, a few minutes a day.

## Flashcards

The page as a deck of Anki cards, one fact per card: [`pythagorean_theorem.txt`](anki/pythagorean_theorem.txt). In Anki choose File → Import and pick the file; the header lines set the separator, note type (Basic), deck and tags, so nothing needs changing in the dialog. Tags such as `vocabulary`, `theorem`, `converse`, `special-triangles`, `three-d`, `law-of-cosines` and `problems` let you study one kind at a time, and `trap` gathers the cards built around a tempting wrong answer.

## Where this goes next

The next lesson, [area and volume formulas](../area_and_volume_formulas/README.md), gives the areas this page's proof used, and the diagonal of a square needs this theorem. [Congruent and similar triangles](../congruent_and_similar_triangles/README.md) explains why 6-8-10 has the same angles as 3-4-5. And in [the distance formula](../../08_Analytic_Geometry/distance_formula/README.md), the legs of the triangle are read off two points' coordinates, which turns this theorem into the way every distance in the plane is measured.

## Po polsku, w skrócie

Twierdzenie Pitagorasa mówi: jeśli trójkąt jest prostokątny, to kwadrat przeciwprostokątnej równa się sumie kwadratów przyprostokątnych, c² = a² + b². Przeciwprostokątna to bok naprzeciw kąta prostego, zawsze najdłuższy; przyprostokątne to dwa boki tworzące kąt prosty. Twierdzenie odwrotne mówi to samo w drugą stronę: jeśli kwadrat jednego boku równa się sumie kwadratów dwóch pozostałych, to trójkąt jest prostokątny, a kąt prosty leży naprzeciw tego boku. To dwa osobne twierdzenia, oba prawdziwe, i razem dają test: trzy długości albo go przechodzą, albo nie.

Kąt prosty to ćwierć obrotu, 90° albo π/2; pozostałe dwa kąty są ostre i sumują się do 90°. Dwa trójkąty warto znać na pamięć: 45-45-90 o bokach 1 : 1 : √2 (pół kwadratu) i 30-60-90 o bokach 1 : √3 : 2 (pół trójkąta równobocznego). Przekątna prostopadłościanu to Pitagoras dwa razy: d² = p² + q² + r². A twierdzenie cosinusów uogólnia Pitagorasa, ale to ono jest dowodzone z Pitagorasa, nie odwrotnie.

Pułapka: test ma sens tylko dla najdłuższego boku. W zadaniu 25 boki podano jako 6, 4, 3, i porównanie 3² z 6² + 4² to złe pytanie. Najpierw sortujemy, potem liczymy. A gdy równości nie ma, nierówność też coś mówi: jeśli c² < a² + b², największy kąt jest ostry; jeśli c² > a² + b², rozwarty. Program sprawdza to na dokładnych liczbach i pokazuje dowód przez pola: kwadrat o boku a + b to cztery trójkąty i kwadrat o boku c w środku.

W przykładzie z Burdż Chalifa odejmuje się dwie prawie równe liczby, co na kalkulatorze niszczy cyfry; postać 2Rh + h² jest bezpieczna. I nie ma wstydu w powrocie do podstaw: każdy matematyk robi to przez całe życie.

## See also

- [Area and volume formulas](../area_and_volume_formulas/README.md) — the areas the proof uses, and the diagonal of a square
- [Congruent and similar triangles](../congruent_and_similar_triangles/README.md) — why 6-8-10 is 3-4-5 at twice the size, and why two sides of a right triangle fix the third
- [The distance formula](../../08_Analytic_Geometry/distance_formula/README.md) — this theorem with the legs read off the coordinates
- [Rectangular coordinates](../../08_Analytic_Geometry/rectangular_coordinates/README.md) — the plane the distance formula works in
- [Catastrophic cancellation](../../01_Precision/catastrophic_cancellation/README.md) — why subtracting two nearly equal squares, as Example 3 does, loses digits
- [Exact vs approximate](../../01_Precision/exact_vs_approximate/README.md) — √2 is exact as a symbol and approximate as every decimal
- [Precalculus: a reading guide](../../reading_guides/precalculus/README.md) — where Appendix A.2 sits in the course, and when to read it
- [Pythagorean theorem ↗](https://en.wikipedia.org/wiki/Pythagorean_theorem) — Wikipedia, with many proofs drawn out, including the rearrangement proof above
- [Twierdzenie Pitagorasa ↗](https://pl.wikipedia.org/wiki/Twierdzenie_Pitagorasa) — Wikipedia po polsku
- Michael Sullivan, *Precalculus* (Pearson), Appendix A, Section A.2 *Geometry Essentials*, objective 1; this page follows it
