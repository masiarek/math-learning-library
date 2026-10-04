# 03_Complex_Numbers — what is a complex number, before anyone says √−1?

**Level:** 101 → 201 · for anyone who has multiplied out (a + b)(c + d)

The usual introduction to complex numbers asks you to accept a number whose square is −1, and then to trust that arithmetic with it still works. This chapter takes the other road, the one Hamilton took in 1835: a complex number **is** a pair of real numbers, and multiplication is a rule on pairs. The rule is written down, nothing is assumed, and the number whose square is −1 comes out at the end as a consequence rather than going in at the start as an axiom. The second lesson says what the rule *does*: it scales and turns the plane, so that i² = −1 is nothing more than a quarter turn done twice. The third says why the rule is this one: the obvious entry-by-entry product lets two nonzero pairs multiply to zero, and only the complex rule can always be undone. The fourth is where that picture pays off: multiply a unit point by itself and it walks around the circle in equal steps, so the equation zⁿ = 1 has exactly n solutions, the n-th roots of unity, and the program finds the twelve of them on a clock face with √3 carried exactly. The fifth answers the question the first four kept putting off, the angle as a number: e^{iπ} = −1 is not e multiplied by itself πi times but the exponential's one law, that adding inputs multiplies outputs, carried into the plane, where the only thing multiplication can do to a unit point is turn it, and the point half a turn from 1 is −1.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [Multiplication as pairs](multiplication_as_pairs/README.md) | What is complex multiplication, if not "multiply out and replace i² by −1"? |
| 2 | [Multiplication rotates](multiplication_rotates/README.md) | Why should two positive things multiply to something negative? |
| 3 | [Multiplication can be undone](multiplication_can_be_undone/README.md) | Why this rule, and not the obvious entry-by-entry one? |
| 4 | [Roots of unity](roots_of_unity/README.md) | Which points come back to (1, 0) when multiplied by themselves, and how many solutions does zⁿ = 1 have? |
| 5 | [Euler's identity](eulers_identity/README.md) | What does e^{iπ} = −1 mean, why does it want to be true, and how is it used? |

## Where this is taught

The subject is **complex analysis**, and the pair construction is the standard opening of its first chapter, usually titled "The complex numbers" or "The complex plane". The construction is Hamilton's, from 1835. The same material also closes an abstract-algebra course, as building ℂ from ℝ, and appears in linear algebra as the 2 × 2 matrices [[x, −y], [y, x]]. In school it is the complex-numbers chapter of a precalculus course, done with angles and de Moivre's formula; [Precalculus: a reading guide](../reading_guides/precalculus/README.md) says where that course sits and which book to take it from.

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

For lesson 4, de Moivre's formula and the roots of unity:

- [Complex Number Primer: powers and roots, Paul's Online Notes ↗](https://tutorial.math.lamar.edu/extras/complexprimer/roots.aspx) — de Moivre's formula and the n-th roots, computed with angles the way a course does it
- [Root of unity ↗](https://en.wikipedia.org/wiki/Root_of_unity) — Wikipedia

For lesson 5, Euler's formula and the identity:

- [*Designing Math*, Grant Sanderson at Config 2026 ↗](https://youtu.be/bLSLN96Gn-w) — the talk whose three questions the lesson follows: what does it mean, why does it want to be true, how is it used; [Euler's formula: a lesson plan](../reading_guides/eulers_formula/README.md) says what to learn first to follow it, and [09_Calculus](../09_Calculus/README.md) has the calculus it uses
- [What is Euler's formula actually saying?, 3Blue1Brown ↗](https://www.3blue1brown.com/lessons/ldm-eulers-formula) — a live lecture on the same formula, from the Lockdown Math series
- [The Feynman Lectures on Physics, vol. I, chapter 22: Algebra ↗](https://www.feynmanlectures.caltech.edu/I_22.html) — from counting to e^{iθ} in one chapter, with the imaginary powers computed by hand; the closest thing in print to the lesson's argument
- [Euler's formula ↗](https://en.wikipedia.org/wiki/Euler%27s_formula) — Wikipedia, with the proofs a course gives
- Paul Nahin, *Dr. Euler's Fabulous Formula* (Princeton, 2006) — a whole book on the formula and its uses, the sequel to *An Imaginary Tale* below

Easier books, to read before any of the textbooks below. None of them needs calculus. They need the school algebra that lesson 1 uses, and some trigonometry: the unit circle, and the angle-addition formulas for cos(A + B) and sin(A + B), which lesson 2 shows are the multiplication rule in disguise. Roughly easiest first:

- [Imagining Numbers, Barry Mazur ↗](https://books.google.com/books/about/Imagining_Numbers.html?id=nFOD5DxYJu8C) — the gentlest, written for readers with no mathematical background; about how anyone comes to imagine a number like √−15 at all, with more ideas than exercises
- [An Imaginary Tale: The Story of √−1, Paul Nahin ↗](https://press.princeton.edu/books/paperback/9780691169248/an-imaginary-tale) — the history, with the mathematics done properly; the early chapters, on cubic equations, need only algebra, and calculus arrives later
- [Complex Numbers and Geometry, Liang-shin Hahn ↗](https://bookstore.ams.org/text-52) — short and self-contained, assuming nothing about complex numbers, and proving theorems of plane geometry with complex multiplication; the one to pick if you read only one
- [Precalculus, Art of Problem Solving ↗](https://artofproblemsolving.com/store/book/precalculus) — chapters 6–8 are complex numbers, then complex numbers with trigonometry, then with geometry; the book for practice, with problems from routine to olympiad
- [Complex Numbers from A to …Z, Titu Andreescu and Dorin Andrica ↗](https://books.google.com/books/about/Complex_Numbers_from_A_to_Z.html?id=vbM5rLOu_WUC) — a step up: competition problems solved with complex numbers
- [Complex Numbers in Geometry, I. M. Yaglom ↗](https://books.google.com/books/about/Complex_Numbers_in_Geometry.html?id=LL_iBQAAQBAJ) — ordinary complex numbers alongside dual and double numbers, the siblings on the [roadmap](../ROADMAP.md); the most demanding of these

Textbooks for the course itself, which needs calculus, roughly in order of difficulty: Churchill and Brown, *Complex Variables and Applications*, chapter 1, which defines complex numbers as ordered pairs and is the most common undergraduate choice; Beck, Marchesi, Pixton and Sabalka, [A First Course in Complex Analysis ↗](https://matthbeck.github.io/complex.html), free and at about the same level; Saff and Snider, *Fundamentals of Complex Analysis*; Ahlfors, *Complex Analysis*; Stein and Shakarchi, *Complex Analysis*; and Needham above, which is not a first course but is the one for the geometry.

## Po polsku, w skrócie

Zwykły podręcznik każe uwierzyć w liczbę, której kwadrat to −1, i zaufać, że arytmetyka dalej działa. Ten rozdział idzie drogą Hamiltona: liczba zespolona **jest** parą liczb rzeczywistych, a mnożenie to spisana reguła na parach, (x₁, y₁) · (x₂, y₂) = (x₁x₂ − y₁y₂, x₁y₂ + x₂y₁). Niczego się nie zakłada; to, że (0, 1)² = (−1, 0), wychodzi z reguły na końcu, zamiast wchodzić na początku jako aksjomat. Druga lekcja mówi, co reguła robi: skaluje i obraca płaszczyznę, więc i² = −1 to tylko dwa ćwierćobroty dające półobrót. Trzecia mówi, czemu reguła jest właśnie taka: oczywiste mnożenie po współrzędnych pozwala dwóm niezerowym parom dać zero, a reguła zespolona nigdy, więc tylko ją da się zawsze odwrócić. Czwarta zbiera plon: punkt okręgu mnożony przez siebie obchodzi okrąg równymi krokami, więc zⁿ = 1 ma dokładnie n rozwiązań, a program znajduje dwanaście znaków tarczy zegara z √3 niesionym dokładnie. Piąta odpowiada na pytanie, które cztery pierwsze odkładały, o kąt jako liczbę: e^{iπ} = −1 to prawo potęg, dodawanie na wejściu to mnożenie na wyjściu, przeniesione na płaszczyznę, gdzie mnożenie może z punktem okręgu zrobić tylko jedno, obrócić go, a pół obrotu od 1 to −1.

## Auf Deutsch: Stichwörter

Eine komplexe Zahl ist ein Paar reeller Zahlen mit einer Multiplikationsregel; √−1 ist eine Folge, keine Annahme.

**Stichwörter:** komplexe Zahl, Paar (a, b), Realteil, Imaginärteil, Multiplikationsregel, Drehung, Betrag, Argument, Einheitswurzeln, eulersche Identität.

## A note on the code

The examples compute with exact fractions (`fractions.Fraction`), never with Python's built-in `complex` type, except in one section each of lessons 1 and 4 that compares the two. The point is that the rule is nothing but real arithmetic, and a program that quietly used `complex` would hide exactly the thing the page is trying to show. Lesson 4 needs √3, and carries it as a symbol with the rule √3 · √3 = 3 rather than as a float, so that h¹² = (1, 0) is an equality and not an approximation. Lesson 5 is the exception the rule was waiting for: π is not a fraction, so its compounding of (1 + iπ/n)ⁿ runs in floats, and its last sections use `cmath`, the standard library's complex exponential, because a program that asks Python for e^{iπ} and gets −1 + 1.2 × 10⁻¹⁶ i is the point. The half turn itself it still reaches exactly, as powers of the clock's marks.
