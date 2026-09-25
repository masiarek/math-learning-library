# 03_Complex_Numbers — what is a complex number, before anyone says √−1?

**Level:** 101 → 201 · for anyone who has multiplied out (a + b)(c + d)

The usual introduction to complex numbers asks you to accept a number whose square is −1, and then to trust that arithmetic with it still works. This chapter takes the other road, the one Hamilton took in 1835: a complex number **is** a pair of real numbers, and multiplication is a rule on pairs. The rule is written down, nothing is assumed, and the number whose square is −1 comes out at the end as a consequence rather than going in at the start as an axiom. The second lesson says what the rule *does*: it scales and turns the plane, so that i² = −1 is nothing more than a quarter turn done twice.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [Multiplication as pairs](multiplication_as_pairs/README.md) | What is complex multiplication, if not "multiply out and replace i² by −1"? |
| 2 | [Multiplication rotates](multiplication_rotates/README.md) | Why should two positive things multiply to something negative? |

## A note on the code

The examples compute with exact fractions (`fractions.Fraction`), never with Python's built-in `complex` type, except in one section that compares the two. The point is that the rule is nothing but real arithmetic, and a program that quietly used `complex` would hide exactly the thing the page is trying to show.
