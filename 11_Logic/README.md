# 11_Logic — what does "if A then B" actually claim?

**Level:** 101 · for anyone reading theorems, from the first page of a precalculus book on

Every theorem in the other chapters has the shape "if A then B", and the book uses words like *converse* and *if and only if* as if everyone already knew what they mean. This chapter says what they mean, and checks each claim on numbers and triangles by brute force. It needs nothing but school arithmetic.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [If A then B: converse, contrapositive and inverse](converse_and_contrapositive/README.md) | Which rewordings of a theorem say the same thing, which need their own proof, and what is "if and only if"? |

## The through-line

An "if A then B" breaks in one case only, A true and B false. Everything in lesson 1 follows from that: the contrapositive breaks in the same case and so is the same claim; the converse breaks in a different case and so needs its own proof; and a theorem whose converse is also true is an "if and only if", like [Pythagoras](../10_Geometry/pythagorean_theorem/README.md). Proof by contradiction, induction and construction are on the [roadmap](../ROADMAP.md).

## Po polsku, w skrócie

Prawie każde twierdzenie ma postać „jeśli A, to B". Ten rozdział wyjaśnia, co to zdanie naprawdę twierdzi: jest fałszywe tylko wtedy, gdy A jest prawdziwe, a B fałszywe. Z tego wynika, że transpozycja („jeśli nie B, to nie A") mówi to samo, a twierdzenie odwrotne („jeśli B, to A") trzeba udowodnić osobno. Gdy oba kierunki są prawdziwe, mówimy „wtedy i tylko wtedy", jak w twierdzeniu Pitagorasa z jego odwrotnym.

## A note on the code

Each "if A then B" is a pair of Python functions, and the program lists every case in a finite range where A holds and B fails. An empty list is evidence, not proof; the lesson says so, and shows a claim that survives four tests and fails the fifth.
