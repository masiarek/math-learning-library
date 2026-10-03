# What a proof is: from what you assume to what you claim, one checked step at a time

**Level:** 101 · for anyone about to prove a first theorem, such as the distance formula, and unsure what "prove it" is asking for

**One line:** To prove a claim is to write a chain of statements from what is already accepted to the claim, each with its reason beside it, so that a reader can check every step without trusting the author and no case is left out; checking cases, however many, is not that, because one unchecked case can be the one that fails.

## What "prove it" asks for

A theorem is a claim about every case in some range: every pair of points in the plane, every right triangle, every natural number n. [The distance formula](../../08_Analytic_Geometry/distance_formula/README.md) says that for *any* two points P₁ = (x₁, y₁) and P₂ = (x₂, y₂), the distance between them is √((x₂ − x₁)² + (y₂ − y₁)²). Sullivan's book finds the distance from (1, 3) to (5, 6) and then states the theorem; the question this page answers is what more the theorem needs than that example.

"Prove it" asks for three things, written down:

1. **What you take as given.** Definitions, axioms, and theorems already proved. For the distance formula: [the Pythagorean theorem](../../10_Geometry/pythagorean_theorem/README.md); that two points on one horizontal line are |x₂ − x₁| apart, and on a vertical one |y₂ − y₁|; and that the axes are perpendicular, so a horizontal line and a vertical line meet at a right angle. Also two definitions: a horizontal line is a line of points with one fixed y, and √ means the non-negative root.
2. **What you claim.** The formula, for every pair of points.
3. **A chain of statements from the first to the second**, each with its reason: a given, a definition, an earlier line in the chain, or a rule of arithmetic or logic that holds for every value of the letters. A reader who asks "why?" at any line must find the answer beside it.

The chain is written with letters, x₁, y₁, x₂, y₂, not with 1, 3, 5, 6. That is the whole trick, and the reason ten lines can cover infinitely many pairs of points at once: if no line depends on which numbers the letters stand for, the chain holds for all of them. Sullivan's example is the chain run on one pair; the proof is the same chain with the numbers replaced by letters, plus a check that no line used that 5 − 1 is 4 rather than some other value. The book's figure draws P₂ to the upper right of P₁, and a proof must survive every position the figure cannot show: P₂ to the left, P₂ below, P₂ level with P₁. That last one is where the figure's triangle disappears, and a proof has to say what happens then.

## Why checking cases is not proving

[If A then B](../converse_and_contrapositive/README.md#examples-prove-nothing-one-counterexample-disproves) says it once: examples prove nothing, one counterexample disproves. The reason is that a loop checks the cases it reaches, and a claim about all n has cases no loop reaches. Section 1 of the program runs the most famous instance. Fermat claimed that 2^(2ⁿ) + 1 is prime for every n, and it is, for n = 0 to 4: 3, 5, 17, 257, 65537. Euler found in 1732 that the next one, 4 294 967 297, is 641 × 6 700 417. Five cases, each true, and a claim about every n that is false.

Closer to the distance formula: √(t²) = t holds for every positive t, a thousand of them in section 2, and fails at the first negative one, because √9 is 3 and not −3. The true statement is √(t²) = |t|, and its proof does what the loop cannot: it splits every real t into two cases, t ≥ 0 and t < 0, and argues each with the letter t. Two cases, both covered, where the loop covered a thousand of the infinitely many. **Proof by cases** is legal exactly when the cases together cover everything, and that coverage is itself a claim to be checked. For the distance formula the cases are "both coordinates differ", "the y's agree" and "the x's agree", and the program checks that they cover every pair with a four-row [truth table](../truth_tables_and_laws/README.md#why-a-table-proves-a-law) over the two tests x₁ = x₂ and y₁ = y₂: every row lands in a case. That finite table is a proof, for the reason lesson 2 gives: there are only four rows, and the table runs all of them.

## What a step is

A line is a step when its reason is one of four things: a given, a definition, an earlier line, or a rule that holds for every value of the letters, such as (−t)² = t² or "a ≥ 0 and a² = s give a = √s". "It is obvious", "look at the figure" and "it worked for (1, 3) and (5, 6)" are not reasons. The figure is a guide to the chain, not part of it.

A chain can fail to be a proof even when every line in it is true, in two ways that a reader catches by following the arrows: a line that cites a later line, which is a circle, and a given that is the claim itself, which assumes what was to be proved. A third failure is a line that is simply wrong with a perfectly good shape, and the arrows cannot see it. Numbers can: a line that disagrees with the line it cites, on one example, is wrong, and one example is enough. The reverse does not hold. A line that agrees with its sources on a thousand examples has been tested, not proved; what proves it is its reason. Section 4 of the program breaks the distance-formula chain each of the three ways and shows which check catches which.

A program that reads the arrows is a toy version of a [proof assistant](../../reading_guides/proof_assistants/README.md), which also checks that each cited rule has the shape the line claims, and knows nothing else. That is the sense in which a proof is something a machine can check and an example is not.

## Where the chain stops

Every "why?" leads one level down, and a proof says where it stops: at the givens. Two lines of the chain below draw that question most often.

*Why is P₁P₃ horizontal?* This is not a theorem but a word's meaning written out. A horizontal line is a line of points with one fixed y, the line y = c; P₁ = (x₁, y₁) and P₃ = (x₂, y₁) both have y = y₁, so both lie on the line y = y₁. Line 2 cites that definition, D1, and nothing else. Before trying to prove a line, ask whether it is a definition unpacked; a good share of the lines in any proof are.

*Why is the distance along a horizontal line |x₂ − x₁|?* In Sullivan's book this is a given, A2 here: Appendix A.1 defines the distance between a and b on the number line as |b − a|, and the line y = y₁ is treated as a number line with the x-axis's unit. To go one level lower you would prove two things. That the line y = y₁ is a copy of the x-axis: the four points (x₁, y₁), (x₂, y₁), (x₂, 0) and (x₁, 0) make a rectangle, two sides vertical and two horizontal, and opposite sides of a rectangle are equal, which is Euclid's geometry. And that on a number line the distance from a to b is |b − a|: a coordinate is a signed distance from 0, lengths along a line add, and the cases 0 ≤ a ≤ b, a ≤ 0 ≤ b and a ≤ b ≤ 0, with the three where a and b trade places, each give b − a or a − b, which is |b − a|. Proof by cases once more, and below that Euclid's axioms, where this library's geometry stops. There is no bottom that every book shares. What a proof owes the reader is to name its givens, so the reader knows what to go and check, and the chain below names five.

## The distance formula, line by line

The chain, as section 3 of the program prints it. A1 is Pythagoras, A2 the distance along a horizontal or vertical line, A3 the perpendicular axes, D1 the definition of a horizontal line (one fixed y) and a vertical one (one fixed x), D2 the definition of √ together with "a distance is never negative".

| # | Line | Because |
|---|---|---|
| 1 | Let P₁ = (x₁, y₁) and P₂ = (x₂, y₂) be any two points, d their distance, and P₃ = (x₂, y₁). | names |
| 2 | P₁ and P₃ share y₁, so P₁P₃ is horizontal; P₃ and P₂ share x₂, so P₃P₂ is vertical. | 1, D1 |
| 3 | \|P₁P₃\| = \|x₂ − x₁\| and \|P₃P₂\| = \|y₂ − y₁\|. | 2, A2 |
| 4 | Case 1, x₁ ≠ x₂ and y₁ ≠ y₂: P₁, P₂, P₃ are three points, and the angle at P₃ is right. | 2, A3 |
| 5 | In case 1, d² = \|x₂ − x₁\|² + \|y₂ − y₁\|². | 3, 4, A1 |
| 6 | For every real t, \|t\|² = t²: if t ≥ 0, \|t\| = t; if t < 0, \|t\| = −t and (−t)² = t². | cases |
| 7 | In case 1, d² = (x₂ − x₁)² + (y₂ − y₁)². | 5, 6 |
| 8 | Case 2, y₁ = y₂: P₃ = P₂, so d = \|x₂ − x₁\|, and (x₂ − x₁)² + (y₂ − y₁)² = (x₂ − x₁)² = d². | 1, A2, 6 |
| 9 | Case 3, x₁ = x₂: P₃ = P₁, so d = \|y₂ − y₁\|, and (x₂ − x₁)² + (y₂ − y₁)² = (y₂ − y₁)² = d². | 1, A2, 6 |
| 10 | The cases cover every pair, so d² = (x₂ − x₁)² + (y₂ − y₁)²; d ≥ 0, so d = √((x₂ − x₁)² + (y₂ − y₁)²). | 7, 8, 9, D2 |

Three things to notice. Line 6 is a small theorem of its own, a **lemma**, proved by cases inside the chain and used three times. Lines 8 and 9 are what the book means when it says the formula "also holds for horizontal and vertical segments": there is no triangle in those cases, A1 is never used, and A2 alone gives the distance. And every given is cited somewhere; a given that no line cites was not needed, and a proof tells you exactly what each line costs. Line 4 is the one that costs A3. On a grid whose axes meet at 60°, A3 is false, line 4 fails, and so does the formula, which is why the answer to "where is the right angle?" matters more than it looks.

## What the program prints

<!-- output:what_a_proof_is -->
*Verified output of [`what_a_proof_is.py`](examples/what_a_proof_is.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. CHECKING CASES IS NOT PROVING: FERMAT'S CLAIM
   Fermat claimed that 2^(2^n) + 1 is prime for every n. The first cases:
   n = 0:          3  prime
   n = 1:          5  prime
   n = 2:         17  prime
   n = 3:        257  prime
   n = 4:      65537  prime
   n = 5: 4294967297  = 641 x 6700417   (Euler found this in 1732)
   Five cases, each true; the claim about every n is false.
   No number of cases proves a claim about all n. One case disproves it.

2. A LOOP OVER t = 1..1000, AND THE TWO CASES THAT COVER EVERY t
   Claim: sqrt(t^2) = t.   Holds for t = 1, 2, ..., 1000: True
   t = -3: sqrt(9) = 3, not -3. The loop never reached a negative t.
   Theorem: sqrt(t^2) = |t| for every real t. Proof, by cases:
     t >= 0: t^2 has the non-negative root t, and |t| = t.
     t <  0: t^2 = (-t)^2 and -t > 0, so the root is -t, and |t| = -t.
   Two cases, and every real t is in one of them: that is what covers all t.
   Tried on t = -1000..1000, as a check that the cases were copied right: True

3. THE DISTANCE FORMULA AS A CHAIN: EVERY LINE WITH ITS REASON
   The proof, as a list of lines.
   Given:
     A1  Pythagoras: a right triangle with legs a, b and hypotenuse c has c^2 = a^2 + b^2.
     A2  Two points on one horizontal line, (x1, y) and (x2, y), are |x2 - x1| apart; on a vertical line, |y2 - y1|.
     A3  The axes are perpendicular, so a horizontal line and a vertical line meet at a right angle.
     D1  A horizontal line is the set of points with one fixed y, the line y = c; a vertical line has one fixed x.
     D2  sqrt(s) is the non-negative number whose square is s, and a distance is never negative.
   Claim: d = sqrt((x2 - x1)^2 + (y2 - y1)^2), for every P1 = (x1, y1) and P2 = (x2, y2).
    1. Let P1 = (x1, y1), P2 = (x2, y2) be any two points, d their distance, and P3 = (x2, y1).
       because: names
    2. P1 and P3 share y1, so P1P3 is horizontal; P3 and P2 share x2, so P3P2 is vertical.
       because: line 1, D1
    3. |P1P3| = |x2 - x1| and |P3P2| = |y2 - y1|.
       because: line 2, A2
    4. Case 1, x1 != x2 and y1 != y2: P1, P2, P3 are three points, and the angle at P3 is right.
       because: line 2, A3
    5. In case 1, d^2 = |x2 - x1|^2 + |y2 - y1|^2.
       because: line 3, line 4, A1
    6. For every real t, |t|^2 = t^2: if t >= 0, |t| = t; if t < 0, |t| = -t and (-t)^2 = t^2.
       because: cases
    7. In case 1, d^2 = (x2 - x1)^2 + (y2 - y1)^2.
       because: line 5, line 6
    8. Case 2, y1 = y2: P3 = P2, so d = |x2 - x1|, and (x2 - x1)^2 + (y2 - y1)^2 = (x2 - x1)^2 = d^2.
       because: line 1, A2, line 6
    9. Case 3, x1 = x2: P3 = P1, so d = |y2 - y1|, and (x2 - x1)^2 + (y2 - y1)^2 = (y2 - y1)^2 = d^2.
       because: line 1, A2, line 6
   10. The cases cover every pair, so d^2 = (x2 - x1)^2 + (y2 - y1)^2; d >= 0, so d = sqrt((x2 - x1)^2 + (y2 - y1)^2).
       because: line 7, line 8, line 9, D2
   Shape check: every citation is a given or an earlier line, no given is
   the claim, and the last line states the claim: OK
   Do the three cases cover every pair? A truth table over the two tests:
     x1 = x2   y1 = y2   lands in
     False     False     case 1
     False     True      case 2
     True      False     case 3
     True      True      case 2 and case 3
   Four rows, each in a case: the split is exhaustive, and the table is the proof of that.

4. THREE BROKEN CHAINS, AND WHICH CHECK CATCHES EACH
   (a) Line 5 cites line 7 instead of A1, and line 7 cites line 5: a circle.
       Shape check: NOT A PROOF
     - line 5 cites line 7, which is not established yet
   (b) Two lines, the second citing a new given A4, which is the distance formula.
       Shape check: NOT A PROOF
     - given A4 is the claim itself
   (c) Line 7 reads 'd^2 = (|x2 - x1| + |y2 - y1|)^2', citing lines 5 and 6 as before.
       Shape check: OK
       On P1 = (1, 3), P2 = (5, 6): line 5 says d^2 = 25, the new line 7 says d^2 = 49.
       A line that disagrees with the line it cites, on one example, is wrong: caught by numbers.
   The shape check reads arrows and knows nothing about numbers. The number check
   can refute a line and never confirm one. What confirms a line is its reason.

5. EACH LINE WITH SOMETHING TO COMPUTE, ON SIX PAIRS OF POINTS
   P1            P2            line 2  line 4  line 6  line 7  line 8  line 9
   (1, 3)        (5, 6)        True    True    True    True    -       -
   (5, 6)        (1, 3)        True    True    True    True    -       -
   (-2, 4)       (5, 4)        True    -       True    True    True    -
   (3, -1)       (3, -7)       True    -       True    True    -       True
   (2, 2)        (2, 2)        True    -       True    True    True    True
   (1/2, 0)      (0, 1/2)      True    True    True    True    -       -
   A dash: the line's case does not apply to that pair. Lines 1, 3, 5 and 10
   apply a given or a definition and compute nothing: their reason is the check.
   Six passes are evidence that the lines were written down right. The proof is the reasons.
```
<!-- /output -->

Section 5 tries every line that has something to compute on six pairs of points, with exact fractions, including the pairs the figure cannot show: the points swapped, a horizontal pair, a vertical pair, a point paired with itself. Lines 1, 3, 5 and 10 apply a given or a definition and compute nothing, and the table says so with a dash: their reason is their check.

## Questions

**1. Sullivan finds the distance from (1, 3) to (5, 6), draws the corner (5, 3), and then states the theorem. Which step turns the computation into a proof?**

<details><summary>Answer</summary>

Replacing 1, 3, 5, 6 by the letters x₁, y₁, x₂, y₂ and checking that no line of the argument used the particular values, only the facts that hold for every value: the corner shares a coordinate with each point, the legs are differences, the axes are perpendicular. Then the chain holds for every pair at once. The example is the chain run once; the proof is the chain itself.

</details>

**2. A friend checks the distance formula on ten thousand random pairs of points with a program and says it is now proved. What has the program shown?**

<details><summary>Answer</summary>

Evidence: ten thousand cases in which the claim holds, out of infinitely many. A single failing pair would have disproved the formula, so the run was worth doing, but no number of passing pairs proves it. The proof is the ten-line chain, whose letters stand for every pair.

</details>

**3. Which line of the chain uses the perpendicular axes, and what happens to the formula on a grid whose axes meet at 60°?**

<details><summary>Answer</summary>

Line 4, which says the angle at P₃ is right. On skewed axes a horizontal and a vertical line meet at 60°, line 4 is false, Pythagoras does not apply, and the formula is wrong: the law of cosines would be needed instead. The proof names the exact assumption the formula rests on.

</details>

**4. Why does the chain need cases 2 and 3 at all? What is P₃ when y₁ = y₂?**

<details><summary>Answer</summary>

When y₁ = y₂, P₃ = (x₂, y₁) = (x₂, y₂) = P₂: the corner is the second point, there is no triangle, and Pythagoras has nothing to apply to. The distance is |x₂ − x₁| by A2 directly, and line 8 checks that the formula gives the same. Case 3 is the same with the roles of x and y swapped. Without those lines the chain would prove the formula only for pairs that make a triangle.

</details>

**5. Is "|t|² = t²" a given, a definition, or a step?**

<details><summary>Answer</summary>

A step, and a small theorem in its own right: a lemma. It is proved by cases from the definition of |t|, as t when t ≥ 0 and −t when t < 0, together with (−t)² = t². The chain uses it in lines 7, 8 and 9.

</details>

**6. Line 10 cites D2. What is D2, and what goes wrong without it?**

<details><summary>Answer</summary>

D2 says that √s means the non-negative number whose square is s, and that a distance is never negative. Without it, d² = s only says d is √s or −√s, and the chain could not pick one. Both halves are needed: the definition of √ to name the root, and d ≥ 0 to say d is that one.

</details>

**7. A chain ends with the line "d = √((x₂ − x₁)² + (y₂ − y₁)²), by the distance formula". Why is it not a proof?**

<details><summary>Answer</summary>

Its last line cites the claim as a given: it assumes what it set out to prove. Every line in it may be true, and it still establishes nothing. The shape check in section 4 catches it without looking at a single number.

</details>

**8. Someone replaces line 7 with "d² = (|x₂ − x₁| + |y₂ − y₁|)²", citing lines 5 and 6 as before. How do you show it is wrong, and how much work does it take?**

<details><summary>Answer</summary>

One example. On (1, 3) and (5, 6), line 5 says d² = 16 + 9 = 25 and the new line says d² = (4 + 3)² = 49. A line that disagrees with the line it cites, on one pair of points, is wrong. The shape of the chain is fine, which is why numbers are the check for this kind of mistake.

</details>

**9. Why can a split into two cases prove something about every real number, when a loop over a thousand of them cannot?**

<details><summary>Answer</summary>

Because the two cases, t ≥ 0 and t < 0, together contain every real number, and each case is argued with the letter t rather than with a value. The loop reaches a thousand numbers; the cases reach all of them. A split is a proof only when the cases are exhaustive, which is a claim to check in its own right, and the program checks the distance formula's split with a four-row truth table.

</details>

**10. "P₁ and P₃ share y₁, so P₁P₃ is horizontal." How do you prove that?**

<details><summary>Answer</summary>

By saying what horizontal means. A horizontal line is a line y = c, all its points at one height; P₁ and P₃ both have y = y₁, so both are on the line y = y₁. There is nothing to prove beyond unpacking the word, and the line's reason is the definition D1. The same question about the length of that segment, |x₂ − x₁|, leads to a given, A2, and below it to a rectangle's opposite sides and to distance on a number line; a proof stops where its givens are, and says so.

</details>

**11. What does the program's shape check look at, and what does it not look at?**

<details><summary>Answer</summary>

It looks at where each line's reasons point: at a given or an earlier line, never a later one; at whether any given is the claim itself; and at whether the last line states the claim. It does not look at whether the cited rule really produces the line, which a [proof assistant](../../reading_guides/proof_assistants/README.md) does, and it never looks at numbers. The number check of section 5 is the other half, and it can only refute.

</details>

**12. Isn't the distance formula just the Pythagorean theorem, so that no proof is needed?**

<details><summary>Answer</summary>

It is Pythagoras, and that sentence is the proof once four things are said: that there is a right triangle at all, which costs the perpendicular axes; that its legs are |x₂ − x₁| and |y₂ − y₁|, which costs A2; that the bars drop inside the squares, which is the lemma |t|² = t²; and that the formula still holds when the points are level or one above the other, where there is no triangle and Pythagoras says nothing. Those are lines 3 to 9, and line 5 is the one that says "Pythagoras". "Just Pythagoras" would hold on any axes, and the formula does not: on axes meeting at 60° it is false. A short proof is still a proof, and this one tells you which assumption the formula rests on.

</details>

## How to practise

1. **Before proving, write the three lists**: what is given, what is claimed, and the letters that stand for every case.
2. **Number the lines and give each a reason.** A line without a reason is a wish. "Obvious" is not a reason; "line 3 and A2" is.
3. **Hunt for the cases the figure hides.** Swap the points, put them level, put one directly above the other, make a coordinate negative. Each is a case the chain must cover, and a split into cases needs its coverage checked.
4. **Test a line you doubt on one example** before believing it, and remember which way the test cuts: a failure settles it, a pass does not.

## Flashcards

The page as a deck of Anki cards: [`what_a_proof_is.txt`](anki/what_a_proof_is.txt). Import with File → Import. Tags: `what`, `why`, `method`, `trap`.

## Where this goes next

[Induction](../induction/README.md) is the first proof method: a chain with one step that runs forever, valid because a false claim about ℕ would fail first somewhere. [Proof assistants](../../reading_guides/proof_assistants/README.md) do this page's shape check properly, with the rules of logic named one by one. And [the Pythagorean theorem](../../10_Geometry/pythagorean_theorem/README.md), given A1 here, has its own chain on its own page, one square cut two ways.

## Po polsku, w skrócie

Twierdzenie mówi coś o każdym przypadku: o każdej parze punktów, o każdej liczbie naturalnej. Udowodnić je to spisać łańcuch zdań od tego, co już przyjęte, do tego, co się twierdzi, przy każdym zdaniu podając powód: założenie, definicję, wcześniejszą linię albo regułę, która zachodzi dla każdej wartości liter. Czytelnik, który przy dowolnej linii zapyta „dlaczego?", musi znaleźć odpowiedź obok. Łańcuch pisze się literami, x₁, y₁, x₂, y₂, a nie liczbami 1, 3, 5, 6; dlatego dziesięć linii obejmuje nieskończenie wiele par punktów naraz.

Sprawdzanie przypadków to nie dowód. Fermat twierdził, że 2^(2ⁿ) + 1 jest zawsze pierwsze; pięć pierwszych przypadków się zgadza, szósty nie (Euler, 641). Pętla sprawdza przypadki, do których dociera, a twierdzenie o wszystkich n ma przypadki, do których żadna pętla nie dotrze. Dowód przez przypadki robi to, czego pętla nie może: dzieli wszystkie liczby na kilka przypadków, które razem obejmują wszystko, i w każdym argumentuje literą. Wzór na odległość ma trzy przypadki: obie współrzędne różne, równe y, równe x; program sprawdza czterowierszową tabelą prawdy, że nic nie zostało pominięte.

Program zapisuje dowód wzoru na odległość jako dziesięć linii z powodami i sprawdza kształt łańcucha: każdy powód wskazuje założenie albo wcześniejszą linię, żadne założenie nie jest samym twierdzeniem, ostatnia linia jest twierdzeniem. Potem psuje łańcuch na trzy sposoby. Koło i założenie tezy łapie sprawdzenie kształtu; błędną linię o dobrym kształcie łapie jeden przykład liczbowy. Liczby mogą linię obalić, ale nigdy potwierdzić; potwierdza ją jej powód.

## See also

- [The distance formula](../../08_Analytic_Geometry/distance_formula/README.md) — the theorem this page proves line by line, with its program and exercises
- [The Pythagorean theorem and its converse](../../10_Geometry/pythagorean_theorem/README.md) — the given A1, proved on its own page by one square cut two ways
- [If A then B: converse, contrapositive and inverse](../converse_and_contrapositive/README.md) — examples prove nothing, one counterexample disproves
- [Truth tables and the laws of logic](../truth_tables_and_laws/README.md) — why a finite table is a proof, which the case check here relies on
- [Induction](../induction/README.md) — the first proof method, with the least counterexample behind it
- [Proof assistants: a reading guide](../../reading_guides/proof_assistants/README.md) — the shape check done properly, rule by rule
- [Mathematical proof ↗](https://en.wikipedia.org/wiki/Mathematical_proof) — Wikipedia, with the kinds of proof and their history
- Michael Sullivan, *Precalculus* (Pearson), section 1.1 *The Distance and Midpoint Formulas*; the example and the theorem this page turns into a chain
