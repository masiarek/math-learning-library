# 03_Complex_Numbers — what is a complex number, before anyone says √−1?

**Level:** 101 → 201 · for anyone who has multiplied out (a + b)(c + d)

The usual introduction to complex numbers asks you to accept a number whose square is −1, and then to trust that arithmetic with it still works. This chapter takes the other road, the one Hamilton took in 1835: a complex number **is** a pair of real numbers, and multiplication is a rule on pairs. The rule is written down, nothing is assumed, and the number whose square is −1 comes out at the end as a consequence rather than going in at the start as an axiom. The second lesson says what the rule *does*: it scales and turns the plane, so that i² = −1 is nothing more than a quarter turn done twice. The third says why the rule is this one: the obvious entry-by-entry product lets two nonzero pairs multiply to zero, and only the complex rule can always be undone.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [Multiplication as pairs](multiplication_as_pairs/README.md) | What is complex multiplication, if not "multiply out and replace i² by −1"? |
| 2 | [Multiplication rotates](multiplication_rotates/README.md) | Why should two positive things multiply to something negative? |
| 3 | [Multiplication can be undone](multiplication_can_be_undone/README.md) | Why this rule, and not the obvious entry-by-entry one? |

## Where this is taught

The subject is **complex analysis**, and the pair construction is the standard opening of its first chapter, usually titled "The complex numbers" or "The complex plane". The construction is Hamilton's, from 1835. The same material also closes an abstract-algebra course, as building ℂ from ℝ, and appears in linear algebra as the 2 × 2 matrices [[x, −y], [y, x]].

Free notes that match lesson 1, the pair construction:

- [Introduction to Complex Numbers, UC Davis ↗](https://www.math.ucdavis.edu/~anne/WQ2007/mat67-Lbc-Complex_Numbers.pdf) — pairs with the product rule, then why x + iy is the same thing; short
- [Complex numbers, MIT 18.03 notes by Bjorn Poonen ↗](https://math.mit.edu/~hrm/18.031/complexnumbers.pdf) — concise, from a differential-equations course
- [Complex Variables lecture notes, Kenneth Shum, CUHK ↗](https://mypage.cuhk.edu.cn/academics/wkshum/files/complex_variables_lecture_notes.pdf) — two constructions side by side, pairs of reals and 2 × 2 matrices; the closest match to both lessons together
- [On complex numbers, part 1, UCL ↗](https://www.homepages.ucl.ac.uk/~uczlcfe/my%20website%20notes/_maths%20-%20complex%20numbers%2001%20-%20part%201.pdf) — gentler, the ordered-pair definition explained in words
- [Complex number: construction as ordered pairs ↗](https://en.wikipedia.org/wiki/Complex_number#Construction_as_ordered_pairs) — Wikipedia

For lesson 2, multiplication as rotation:

- [Complex number fundamentals, 3Blue1Brown ↗](https://www.3blue1brown.com/lessons/ldm-complex-numbers/) — a ninety-minute live lesson built on "multiply lengths, add angles", with i as a quarter turn; also on [YouTube ↗](https://www.youtube.com/watch?v=5PcpBw5Hbwo)
- [Visual Complex Analysis, Tristan Needham ↗](https://books.google.com/books/about/Visual_Complex_Analysis.html?id=ogz5FjmiqlQC) — the book for the rotation-first approach; chapter 1 is often in the preview, and there is a [short review ↗](https://scholarcommons.scu.edu/cgi/viewcontent.cgi?article=1000&context=math_compsci)
- [Transforms, Berkeley CS184 ↗](https://cs184.eecs.berkeley.edu/sp24/lecture/4-38/transforms) — the rotation matrix from the linear-algebra side, as computer graphics uses it

For lesson 3, division and ℂ*: Titu Andreescu and Dorin Andrica, *Complex Numbers from A to … Z* (Birkhäuser, 2014), §1.1.1, which names ℂ* alongside the pair definition; its two worked examples are the lesson's first kata.

Textbooks, roughly in order of difficulty: Churchill and Brown, *Complex Variables and Applications*, chapter 1, which defines complex numbers as ordered pairs and is the most common undergraduate choice; Saff and Snider, *Fundamentals of Complex Analysis*; Ahlfors, *Complex Analysis*; Stein and Shakarchi, *Complex Analysis*; and Needham above, which is not a first course but is the one for the geometry.

## A note on the code

The examples compute with exact fractions (`fractions.Fraction`), never with Python's built-in `complex` type, except in one section that compares the two. The point is that the rule is nothing but real arithmetic, and a program that quietly used `complex` would hide exactly the thing the page is trying to show.
