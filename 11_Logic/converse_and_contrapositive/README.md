# If A then B: converse, contrapositive and inverse

**Level:** 101 · for anyone who has met "the converse of the Pythagorean theorem" and wondered why it needed its own proof

**One line:** "If A then B" breaks in exactly one case, A true and B false; its contrapositive "if not B then not A" breaks in the same case and so is the same claim, while its converse "if B then A" breaks in a different case and must be proved on its own.

## The idea

Most theorems have the shape **if A then B**. A is the **hypothesis** (what is assumed), B is the **conclusion** (what follows). The Pythagorean theorem: *if* a triangle is right, *then* a² + b² = c². The statement makes one promise: whenever A holds, B holds too. It says nothing at all about what happens when A does not hold.

Swapping and negating the two parts gives three more statements:

| Name | Form | Pythagorean example | Same claim as the original? |
|---|---|---|---|
| statement | if A then B | if a triangle is right, then a² + b² = c² | — |
| **converse** | if B then A | if a² + b² = c², then the triangle is right | **no**: must be proved separately |
| inverse | if not A then not B | if a triangle is not right, then a² + b² ≠ c² | no, but the same claim as the converse |
| **contrapositive** | if not B then not A | if a² + b² ≠ c², then the triangle is not right | **yes**, always |

That table is the whole lesson. The rest explains why it holds.

## When does "if A then B" fail?

Only in one situation: **A is true and B is false**. That is the only way to break a promise that says "whenever A, then B". If A is false, the promise was never triggered, so it cannot be broken, and the statement counts as true there. That can feel odd at first. It is why "if n is divisible by 4, then n is even" is not refuted by n = 3 or n = 6: they are not divisible by 4, so the statement made no promise about them.

The truth table in section 1 of the program lists the four cases. Now look at the **contrapositive**, "if not B then not A". It fails only when "not B" is true and "not A" is false, which means B false and A true: *the same single case*. So a statement and its contrapositive fail in exactly the same situations. They are the same claim in different words, and proving one proves the other.

The **converse**, "if B then A", fails when B is true and A is false: a *different* case. So the converse can be true or false whatever the original is, and it needs its own argument:

- "If n is divisible by 4, then n is even": true. The converse "if n is even, then n is divisible by 4" is false: 2, 6 and 10 are counterexamples.
- "If a triangle has sides 3k, 4k, 5k, then it is right": true. The converse "if it is right, its sides are 3k, 4k, 5k" is false: 5, 12, 13.
- The Pythagorean theorem: true, and its converse also true, proved separately (by building a right triangle and using SSS; see [the Pythagorean theorem lesson](../../10_Geometry/pythagorean_theorem/README.md)).

The **inverse**, "if not A then not B", is the contrapositive of the converse, so it always agrees with the converse and tells you nothing new.

## If and only if

When a statement and its converse are both true, the two conditions always come together, and mathematicians say **A if and only if B**, written A ⇔ B, sometimes shortened to "iff". The Pythagorean theorem with its converse is exactly this: a triangle is right **if and only if** a² + b² = c², with c its longest side. Every definition is an "if and only if": a triangle *is* a right triangle if and only if it has a 90° angle. Proving an "if and only if" means two proofs, one for each direction.

## Two mistakes everyone makes

Knowing "if A then B", three conclusions look tempting. Only one of them is valid:

| You know | You see | You conclude | Valid? | Name |
|---|---|---|---|---|
| if A then B | B | A | **no** | affirming the consequent, which confuses the statement with its converse |
| if A then B | not A | not B | **no** | denying the antecedent, which confuses it with its inverse |
| if A then B | not B | not A | **yes** | the contrapositive |

"If it rained, the street is wet. The street is wet." It does not follow that it rained: someone may have washed the street. But "the street is dry" really does mean it did not rain.

## Examples prove nothing, one counterexample disproves

An "if A then B" about infinitely many things, such as every number or every triangle, cannot be proved by checking cases, however many. It can be *disproved* by one case where A is true and B is false. Section 6 of the program shows the classic warning. "If p is prime, then 2ᵖ − 1 is prime" holds for p = 2, 3, 5, 7, and fails at p = 11, where 2¹¹ − 1 = 2047 = 23 × 89. Its converse, "if 2ⁿ − 1 is prime, then n is prime", is a different claim, and it happens to be true.

## What the program prints

Each "if A then B" is tested by brute force: the program lists every case in its range where A holds and B fails. None means true within that range; the first few are printed otherwise.

<!-- output:converse_and_contrapositive -->
*Verified output of [`converse_and_contrapositive.py`](examples/converse_and_contrapositive.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. THE TRUTH TABLE: WHEN DOES 'IF A THEN B' FAIL?
      A  B | if A then B | converse | inverse | contrapositive
      T  T |      T      |    T     |    T    |       T
      T  F |      F      |    T     |    T    |       F
      F  T |      T      |    F     |    F    |       T
      F  F |      T      |    T     |    T    |       T
   The statement fails in one row only: A true, B false.
   Its column matches the contrapositive's in every row: they are one claim.
   The converse's column matches the inverse's, and differs from the statement's.

2. ON THE NUMBERS 1 TO 30: A = 'n is divisible by 4', B = 'n is even'
     statement:      if div by 4, then even                     true
     converse:       if even, then div by 4                     FALSE, e.g. 2, 6, 10
     inverse:        if not div by 4, then odd                  FALSE, e.g. 2, 6, 10
     contrapositive: if odd, then not div by 4                  true
   The counterexamples to the converse and to the inverse are the same numbers:
   even but not divisible by 4. Each claim is true exactly when its partner is.

3. ON 2135 TRIANGLES WITH WHOLE SIDES UP TO 30 (sorted, longest last)
     if sides are 3k, 4k, 5k, then right                        true
     converse: if right, then sides are 3k, 4k, 5k              FALSE, e.g. (5, 12, 13), (8, 15, 17), (7, 24, 25)
   The first is true and its converse false: 5, 12, 13 is right and not 3-4-5.
   ('Right' is tested here with a^2 + b^2 = c^2, which the converse of the
   Pythagorean theorem entitles us to do.)

4. BOTH DIRECTIONS AT ONCE: 'IF AND ONLY IF'
     if n is a perfect square, it has an odd number of divisors true
     if n has an odd number of divisors, it is a perfect square true
   Both true, so: n is a perfect square IF AND ONLY IF it has an odd number of
   divisors. The Pythagorean theorem with its converse is the same kind of pair:
   a triangle is right if and only if a^2 + b^2 = c^2, with c the longest side.

5. A FALSE 'IF' MAKES THE STATEMENT TRUE: THE ROWS WHERE A FAILS
   'If n is divisible by 4 then n is even', checked at n = 3, 6, 8:
     n = 3:  A F, B F  ->  T
     n = 6:  A F, B T  ->  T
     n = 8:  A T, B T  ->  T
   At n = 3 and n = 6 the statement makes no promise, so it cannot be broken.
   Only a number that is divisible by 4 and odd could refute it, and there is none.

6. MANY EXAMPLES PROVE NOTHING; ONE COUNTEREXAMPLE DISPROVES
     p =  2 (prime):  2^p - 1 =    3   prime: True
     p =  3 (prime):  2^p - 1 =    7   prime: True
     p =  5 (prime):  2^p - 1 =   31   prime: True
     p =  7 (prime):  2^p - 1 =  127   prime: True
     p = 11 (prime):  2^p - 1 = 2047   prime: False
     p = 13 (prime):  2^p - 1 = 8191   prime: True
   'If p is prime then 2^p - 1 is prime' survives four tests and dies at 11:
   2047 = 23 x 89. The converse is a different claim, so it gets its own test:
     if 2^n - 1 is prime, then n is prime (n = 1 to 30)         true
   True here, and true for every n: if n = ab, then 2^a - 1 divides 2^n - 1.

7. THE TWO CLASSIC MISTAKES, AS TRUTH-TABLE ROWS
   Known: if A then B.  Observed: B.  Conclude A?   'Affirming the consequent'.
     The row A = F, B = T keeps 'if A then B' true, so A may be false. Invalid.
   Known: if A then B.  Observed: not A.  Conclude not B?   'Denying the antecedent'.
     The same row: A false, B true. Invalid.
   Known: if A then B.  Observed: not B.  Conclude not A?   The contrapositive. Valid.
```
<!-- /output -->

## Questions

**1. Write the converse, the inverse and the contrapositive of "if a number is divisible by 6, then it is divisible by 3". Which are true?**

<details><summary>Answer</summary>

Converse: if divisible by 3, then divisible by 6. False (3, 9). Inverse: if not divisible by 6, then not divisible by 3. False (3 again). Contrapositive: if not divisible by 3, then not divisible by 6. True, like the original.

</details>

**2. Is "if a quadrilateral is a square, then it has four right angles" true? Its converse?**

<details><summary>Answer</summary>

The statement is true. The converse, "if it has four right angles, it is a square", is false: a 2 × 5 rectangle has four right angles and is not a square.

</details>

**3. The statement is true. Must its contrapositive be true? Its converse?**

<details><summary>Answer</summary>

The contrapositive, yes, always: it fails in exactly the same case (A true, B false). The converse, not necessarily; it has to be checked separately.

</details>

**4. "If n = 7, then n² = 49." True? Converse?**

<details><summary>Answer</summary>

True. The converse, "if n² = 49 then n = 7", is false: n = −7. This is the same trap as √(t²) = |t|: squaring loses the sign, so it cannot be run backwards.

</details>

**5. Why is "if 2 + 2 = 5, then the Moon is made of cheese" counted as true?**

<details><summary>Answer</summary>

The hypothesis is false, so the promise is never triggered and cannot be broken. An "if … then" is false only when the hypothesis is true and the conclusion false. Mathematicians call this *vacuously true*. It matters because theorems are applied to cases where the hypothesis does not hold, and there they must not count as broken.

</details>

**6. The distance lesson says: "if d(A, B)² < d(A, C)², then d(A, B) < d(A, C)". Is the converse true? Why does that matter?**

<details><summary>Answer</summary>

Yes: for non-negative numbers, x < y if and only if x² < y². Because it is an "if and only if", comparing squared distances is a complete test in both directions, and no square root is needed.

</details>

**7. A student knows "if a triangle is right, then a² + b² = c²" and measures a triangle with a² + b² ≠ c². What can they conclude, and by which rule?**

<details><summary>Answer</summary>

It is not a right triangle, by the contrapositive. This needs only the theorem, not its converse.

</details>

**8. A student knows only the theorem (not the converse), and measures a triangle with a² + b² = c². Can they conclude it is right?**

<details><summary>Answer</summary>

Not from the theorem alone: that would be affirming the consequent. It is the converse that licenses the conclusion, which is exactly why the book states the converse as a separate theorem.

</details>

**9. "If x > 2, then x² > 4." True? Converse? Inverse?**

<details><summary>Answer</summary>

True. Converse, "if x² > 4 then x > 2": false, x = −3. Inverse, "if x ≤ 2 then x² ≤ 4": false, x = −3 again, as it must be, since the inverse and the converse always stand or fall together.

</details>

**10. Rewrite "every right triangle has an angle bigger than both others" as an "if … then", and give its converse. Is the converse true?**

<details><summary>Answer</summary>

If a triangle is right, then one angle is bigger than both others. Converse: if one angle is bigger than both others, the triangle is right. False: a triangle with angles 100°, 40°, 40° has a largest angle and is obtuse.

</details>

**11. Which is the definition and which is the theorem: "a right triangle has a 90° angle" and "a right triangle has a² + b² = c²"? Why can the definition be read in both directions without proof?**

<details><summary>Answer</summary>

The first is the definition, the second the theorem. A definition is an "if and only if" by agreement: it gives a name to exactly the things that have the property. A theorem connects two things that were defined separately, so each direction needs its own proof.

</details>

**12. The program checked "if 2ⁿ − 1 is prime then n is prime" for n up to 30 and found no counterexample. Is that a proof?**

<details><summary>Answer</summary>

No: 30 cases prove nothing about the 31st. The proof is algebra: if n = ab with a, b > 1, then 2ᵃ − 1 divides 2ⁿ − 1, so 2ⁿ − 1 is not prime. That is the contrapositive: if n is not prime, then 2ⁿ − 1 is not prime.

</details>

## How to practise

1. **Name A and B out loud.** For every theorem in the book, say "the hypothesis is …, the conclusion is …" before using it.
2. **Write all four versions** for one statement a day, and mark each true or false with a counterexample where false.
3. **Ask of every theorem you meet: is the converse true?** The book states the converse when it is (Pythagoras), and often not when it is not.
4. **The cards**, especially the `trap` tag.

## Flashcards

The page as a deck of Anki cards: [`converse_and_contrapositive.txt`](anki/converse_and_contrapositive.txt). Import with File → Import. Tags: `definition`, `truth-table`, `iff`, `mistakes`, `problems`, `trap`.

## Where this goes next

Proof by contradiction and proof by contrapositive both grow out of this table, and so does the "if and only if" in every definition of the book. The [roadmap](../../ROADMAP.md) lists proof as a chapter to come.

## Po polsku, w skrócie

Twierdzenie ma zwykle postać „jeśli A, to B". A to założenie, B to teza. Takie zdanie jest fałszywe tylko w jednym przypadku: A prawdziwe, B fałszywe. Gdy A jest fałszywe, obietnica w ogóle nie obowiązuje, więc zdanie jest prawdziwe.

Z tego zdania powstają trzy inne. **Twierdzenie odwrotne**: „jeśli B, to A". **Przeciwne**: „jeśli nie A, to nie B". **Transpozycja** (kontrapozycja): „jeśli nie B, to nie A". Transpozycja zawodzi dokładnie w tym samym przypadku co zdanie wyjściowe, więc jest tym samym twierdzeniem. Twierdzenie odwrotne zawodzi w innym przypadku, więc trzeba je udowodnić osobno. Przykład: „jeśli n dzieli się przez 4, to jest parzyste" jest prawdziwe, a odwrotne jest fałszywe (n = 2). Twierdzenie Pitagorasa i twierdzenie do niego odwrotne są oba prawdziwe, więc razem dają „wtedy i tylko wtedy".

Dwa klasyczne błędy: z „jeśli A, to B" i z B wnioskować A, albo z „nie A" wnioskować „nie B". Poprawny jest tylko wniosek z „nie B" na „nie A". I jeszcze jedno: żadna liczba przykładów nie dowodzi twierdzenia o nieskończenie wielu przypadkach, a jeden kontrprzykład je obala (2¹¹ − 1 = 2047 = 23 · 89).

## Auf Deutsch: Stichwörter

Aus „wenn A, dann B“ folgt die Kontraposition „wenn nicht B, dann nicht A“ umsonst; Umkehrung und Inversion brauchen eigene Beweise.

**Stichwörter:** Implikation, Umkehrung (converse), Kontraposition, Inversion (inverse), Äquivalenz (genau dann, wenn), notwendig und hinreichend, Gegenbeispiel.

## See also

- [The Pythagorean theorem and its converse](../../10_Geometry/pythagorean_theorem/README.md) — the converse this page is about, with its proof
- [A definition is a test](../../06_Algebraic_Structures/a_definition_is_a_test/README.md) — a definition as a test that objects pass or fail
- [Linear equations and their solutions](../../07_Linear_Systems/linear_equations/README.md) — an equation as a test, the same idea one level down
- [Converse (logic) ↗](https://en.wikipedia.org/wiki/Converse_(logic)) and [Contraposition ↗](https://en.wikipedia.org/wiki/Contraposition) — Wikipedia
- [Affirming the consequent ↗](https://en.wikipedia.org/wiki/Affirming_the_consequent) — Wikipedia, with more street-is-wet examples
- [Implikacja ↗](https://pl.wikipedia.org/wiki/Implikacja) — Wikipedia po polsku, the truth table of "jeśli A, to B"
- Michael Sullivan, *Precalculus* (Pearson), Appendix A.2, where "the converse of the Pythagorean theorem is also true" is the book's first use of the word
