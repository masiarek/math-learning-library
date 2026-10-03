# 11_Logic — what does "if A then B" actually claim?

**Level:** 101 · for anyone reading theorems, from the first page of a precalculus book on

Every theorem in the other chapters has the shape "if A then B", and the book uses words like *converse* and *if and only if* as if everyone already knew what they mean. This chapter says what they mean, and checks each claim on numbers and triangles by brute force. It needs nothing but school arithmetic.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [If A then B: converse, contrapositive and inverse](converse_and_contrapositive/README.md) | Which rewordings of a theorem say the same thing, which need their own proof, and what is "if and only if"? |
| 2 | [Truth tables and the laws of logic](truth_tables_and_laws/README.md) | What makes a "law of logic" true, and what is the difference between ↔ and ⇔? |
| 3 | [Predicates and quantifiers](predicates_and_quantifiers/README.md) | What do ∀ and ∃ mean, which pairs of them can be swapped, and what does "not everyone" say? |
| 4 | [What a proof is](what_a_proof_is/README.md) | What does "prove it" ask for, why is a loop over cases not it, and where does a chain of "why?" stop? |
| 5 | [Induction](induction/README.md) | Why is "assume P(n), prove P(n + 1)" allowed, and where does the proof that all cars are the same colour break? |

## The through-line

An "if A then B" breaks in one case only, A true and B false. Everything in lesson 1 follows from that: the contrapositive breaks in the same case and so is the same claim; the converse breaks in a different case and so needs its own proof; and a theorem whose converse is also true is an "if and only if", like [Pythagoras](../10_Geometry/pythagorean_theorem/README.md).

Lesson 2 widens the view from one connective to all five. A sentence built from letters and connectives is a function of the letters' truth values, a truth table lists it on every row, and a law of logic is two sentences whose columns agree on every row; that is why a finite table proves a law, and why ↔ inside a sentence and ⇔ between sentences are different things. Lesson 3 adds the two symbols a table cannot handle, ∀ and ∃, as loops over a universe of discourse: ¬ flips one into the other, same-type pairs swap and mixed pairs do not, and "everyone likes someone" is not "someone is liked by everyone". The three lessons together are the language the [axioms of set theory](../13_Axioms_of_Set_Theory/README.md) are written in. Lesson 4 says what a proof is at all: a chain from the givens to the claim, a reason beside every line, argued with letters so that it covers every case at once where a loop covers only the cases it reaches; the distance formula is written out as ten such lines, and a program checks the chain's shape and breaks it three ways. Lesson 5 is the first proof *method*: induction, valid because a false claim about the natural numbers has a least counterexample and a step that always works forbids one; the famous wrong proof that all cars are the same colour breaks at exactly one rung, which the program finds. Proof by contradiction appears inside it; construction is still on the [roadmap](../ROADMAP.md).

## Po polsku, w skrócie

Prawie każde twierdzenie ma postać „jeśli A, to B". Ten rozdział wyjaśnia, co to zdanie naprawdę twierdzi: jest fałszywe tylko wtedy, gdy A jest prawdziwe, a B fałszywe. Z tego wynika, że transpozycja („jeśli nie B, to nie A") mówi to samo, a twierdzenie odwrotne („jeśli B, to A") trzeba udowodnić osobno. Gdy oba kierunki są prawdziwe, mówimy „wtedy i tylko wtedy", jak w twierdzeniu Pitagorasa z jego odwrotnym. Druga lekcja pokazuje, że prawo logiki to dwie kolumny tabeli prawdy, które zgadzają się w każdym wierszu, więc skończona tabela jest dowodem, a ↔ wewnątrz zdania i ⇔ między zdaniami to dwie różne rzeczy. Trzecia dodaje kwantyfikatory ∀ i ∃ jako pętle po uniwersum: negacja odwraca kwantyfikator, kwantyfikatory tego samego rodzaju można zamieniać, mieszanych nie. W tym języku zapisane są aksjomaty teorii mnogości z rozdziału 13. Czwarta lekcja mówi, czym w ogóle jest dowód: łańcuchem zdań od założeń do tezy, z powodem przy każdej linii, zapisanym literami, więc obejmującym wszystkie przypadki naraz, czego pętla po przypadkach nie potrafi; wzór na odległość jest w niej rozpisany na dziesięć takich linii. Piąta lekcja to indukcja: pierwsza metoda dowodu, poprawna dzięki zasadzie dobrego uporządkowania, z błędnym dowodem o samochodach, który zawodzi na jednym szczeblu.

## A note on the code

Each "if A then B" is a pair of Python functions, and the program lists every case in a finite range where A holds and B fails. An empty list is evidence, not proof; the lesson says so, and shows a claim that survives four tests and fails the fifth. Lesson 4 turns that into a checker: a proof is data, a list of lines with their reasons, and the program verifies the shape of the chain, then tries each line on numbers, which can refute a line and never confirm one. Lessons 2 and 3 are different: a truth table over n letters, or a quantifier over a universe of four points, has finitely many cases and the programs run all of them, so there the check is the proof, and the pages say why.
