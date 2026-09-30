# 09_Calculus — what is a velocity, and which motion is its own velocity?

**Level:** 101 → 201 · for anyone who can multiply out (3 + h)², and who wants to follow the talk behind [Euler's identity](../03_Complex_Numbers/eulers_identity/README.md)

Calculus usually starts with the slopes of graphs and a careful definition of a limit. This chapter starts where Grant Sanderson's talk *Designing Math* starts: with motion. A point moves along a line, or round a circle, and the only question is how fast and which way. The first lesson says what a velocity at an instant is: the number that average velocities settle on as the time interval shrinks, called the derivative, and the thing that lets a program take the next small step. The second follows the one motion that matters most: start at 1 and always move with velocity equal to your position. That is e^t, the number e is where it is at time 1, and the law of exponents, the talk's "double" and its "flip and squish" all come out of the rule. The third says why angles are measured in radians: in radians the angle is the distance walked round the circle, so a point turning at speed 1 is at angle t at time t, and the derivative of sin is cos. The fourth writes e^x as a polynomial that never ends, finds that "velocity = position" leaves no choice for any coefficient, and gets cos and sin by putting an imaginary number in.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [The derivative is a velocity](derivative_as_velocity/README.md) | What is a velocity at an instant, when an instant has no length? |
| 2 | [Velocity equals position](velocity_equals_position/README.md) | Which motion is its own velocity, and why does it obey e^(a+b) = eᵃ · eᵇ? |
| 3 | [Radians](radians/README.md) | Why do calculus and Euler's formula measure angles in radians and not degrees? |
| 4 | [Power series](power_series/README.md) | Why is e^x = 1 + x + x²/2 + x³/6 + ⋯, and where are cos and sin in it? |

The chapter is not a calculus course. It is the part of one that [Euler's identity](../03_Complex_Numbers/eulers_identity/README.md) and the talk lean on, and [Euler's formula: a lesson plan](../reading_guides/eulers_formula/README.md) says where each lesson fits in learning them. Integrals, the product rule, and limits done with ε and δ are not here.

## Where this is taught

The first two lessons are the opening chapters of a first calculus course, usually called *Calculus I*: the derivative, then the derivatives of exponential and trigonometric functions and the chain rule. Radians are defined in precalculus, in the trigonometry chapter, and cashed in by Calculus I when it differentiates sin. Power series close *Calculus II*, in a chapter called "Taylor series" or "Power series".

Free, to watch or read:

- [Essence of calculus, 3Blue1Brown ↗](https://www.3blue1brown.com/topics/calculus) — the same author as the talk, and the same pictures. Chapters 1 and 2 are lesson 1, chapter 4 is the chain rule, chapter 5 is lesson 2, and chapter 11 is lesson 4
- [Calculus Volume 1, OpenStax ↗](https://openstax.org/details/books/calculus-volume-1) — a free textbook; chapter 3 is derivatives, including those of eˣ, sin and cos, and chapter 1 reviews radians
- [Calculus Volume 2, OpenStax ↗](https://openstax.org/details/books/calculus-volume-2) — chapter 6 is power series and Taylor series
- [Calculus I, Paul's Online Notes ↗](https://tutorial.math.lamar.edu/classes/calci/calci.aspx) — short notes with worked examples, the ones students use the night before an exam
- [Calculus 1, Khan Academy ↗](https://www.khanacademy.org/math/calculus-1) — videos and exercises that grade themselves

Books, roughly easiest first: Silvanus P. Thompson, *Calculus Made Easy* (1910, revised by Martin Gardner in 1998), which is exactly as friendly as its title and still in print; James Stewart, *Calculus: Early Transcendentals*, the usual course book; Gilbert Strang, *Calculus*, free from MIT and written with the same motion-first instinct as this chapter; and Michael Spivak, *Calculus*, which proves everything and is the book for the theorems this chapter only measures.

## Po polsku, w skrócie

Rachunek różniczkowy zaczyna się zwykle od nachylenia wykresu i starannej definicji granicy. Ten rozdział zaczyna tak jak wykład Granta Sandersona: od ruchu. Pierwsza lekcja mówi, czym jest prędkość w jednej chwili: liczbą, do której dążą prędkości średnie, gdy odcinek czasu maleje; to jest pochodna, i to ona pozwala zrobić następny mały krok. Druga śledzi ruch, w którym prędkość zawsze równa się położeniu, startujący z 1: to e^t, a e to położenie w chwili 1, i z tej jednej reguły wychodzi prawo potęg, „podwojenie" i „odwrócenie ze ściśnięciem" z wykładu. Trzecia wyjaśnia radiany: kąt w radianach to droga przebyta po okręgu, więc pochodna sinusa to cosinus. Czwarta zapisuje eˣ jako wielomian bez końca i pokazuje, że reguła „prędkość = położenie" wymusza każdy współczynnik, a po wstawieniu liczby urojonej wypadają z niego cos i sin. To nie jest cały kurs analizy, tylko ta jego część, na której opiera się tożsamość Eulera.

## A note on the code

Where the argument is exact, the programs are exact: the average velocities of t² are fractions, so "6 + h" is an equality, and the coefficients of the series are built as fractions from the rule k·aₖ = aₖ₋₁. Where the function is e^t, sin or cos, whose values are not fractions, they use `math.exp`, `math.sin` and `math.cos` and print six decimals, and velocities are measured over a time of 10⁻⁶, near the best a double allows, for the reason [the derivative is a velocity](derivative_as_velocity/README.md#in-floats-the-step-cannot-shrink-forever) shows in its last section.
