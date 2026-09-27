# 06_Algebraic_Structures — why does every book list the same laws?

**Level:** 101 → 201 · for anyone who has read the same rules in two different books

Open a school algebra book and it lists rules for adding integers: a + b = b + a, and (a + b) + c = a + (b + c). Open a linear-algebra book and the definition of a vector space lists u + v = v + u, and (u + v) + w = u + (v + w). Two chapters later the same book lists associativity, identity and distributivity again, for products of linear maps. It looks as if every mathematics book repeats itself.

It does, and this chapter is about why, and about the tools mathematics built so that the repetition stops. There are only four laws an operation usually has, so every new set with an operation reprints the same short list. Once the list becomes a *definition*, a theorem proved from it holds in every set that passes. A subset needs to check only that its answers stay inside. And a map that keeps the operations carries theorems from one set to another. Every program in the chapter writes the laws once, as functions, and runs them on many sets. So the code does what the chapter says mathematics does.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [The laws of an operation](laws_of_an_operation/README.md) | Why is it always the same list, and what do *group*, *monoid* and *ring* add to it? |
| 2 | [A definition is a test](a_definition_is_a_test/README.md) | What changes when u + v = v + u is a condition instead of a fact, and why is x⁰ = 1 a theorem about vector spaces? |
| 3 | [Subsets inherit the laws](subsets_inherit_the_laws/README.md) | Why does a subspace need three checks when a vector space needs eight? |
| 4 | [Maps that keep the laws](maps_that_keep_the_laws/README.md) | What do T(u + v) = Tu + Tv, log(xy) = log x + log y and det(AB) = det A det B have in common? |

## The through-line

Lesson 1 finds that the rules in every book come from one menu of four laws: commutative, associative, identity and inverses, with distributivity to join two operations. The names *semigroup*, *monoid*, *group*, *ring* and *field* only say which laws hold. The integers under + and the vectors under + fill exactly the same row, and the news in any new list is the law that is missing.

Lesson 2 separates two uses of the same sentence. As a fact, a + b = b + a describes one set. As a definition, u + v = v + u is a test that any set can take, and then a theorem proved from the test is proved for every set that passes. The positive numbers pass the vector-space test with multiplication as their "addition". There the theorem 0v = 0 becomes x⁰ = 1, which nobody had to prove a second time.

Lesson 3 shows why a subset needs fewer checks: a law that says "for all" is already true of every member, so only closure can fail. The same argument is the subgroup test and the subring test, and universal algebra proves it once for all of them.

Lesson 4 turns to maps between sets. A linear map, the logarithm, the determinant, the length of a string and the powers of 2 all have the same shape. One line of proof about that shape gives 2⁰ = 1, log 1 = 0, T(0) = 0 and det I = 1 at once. When such a map can be undone, it shows that two sets are one structure in two notations. Composition of maps, associative and with identities, is where the subject called category theory starts.

## Where this is taught

The rules come first in a school or precalculus book, for the integers and the reals. Serge Lang's *Basic Mathematics* is a careful example: its first chapter states rules for addition and for multiplication, then derives further rules from them instead of checking numbers.

The definition-as-a-test view is the first chapter of any **linear algebra** course that is taught from axioms. [Sheldon Axler, *Linear Algebra Done Right* ↗](https://linear.axler.net/), 4th edition, is free to read online, and its sections 1B, 1C and 3A are lessons 2, 3 and 4 of this chapter in its own words.

Groups, rings and fields in general are the subject of **abstract algebra**. Charles Pinter's *A Book of Abstract Algebra* (Dover) is the gentle start, and Joseph Gallian's *Contemporary Abstract Algebra* is the standard undergraduate text.

The single proof behind every subgroup, subring and subspace test is **universal algebra**: Stanley Burris and H. P. Sankappanavar, *A Course in Universal Algebra*, which the authors distribute free.

The theory of structures and the maps between them is **category theory**. F. William Lawvere and Stephen Schanuel's *Conceptual Mathematics* starts from nothing, and [Tom Leinster, *Basic Category Theory* ↗](https://arxiv.org/abs/1612.09375) is a free first course with examples from algebra throughout.

The place where "write it once" is enforced by a machine is the **Lean** proof assistant and its library Mathlib. There, *module*, *vector space*, *group* and *ring* are one hierarchy of definitions, and a theorem proved for modules applies to every vector space automatically, with the laws checked by the computer instead of assumed.

## A note on the code

Everything is exact, with `fractions.Fraction`, except where a program uses floats on purpose to show which laws they lose. A program can only try finitely many members, so a failure always comes with a **witness**, the actual values that break the law, which you can check by hand. A pass is only as strong as the theorem behind it, and each page says what that theorem is. [Lesson 1](laws_of_an_operation/README.md#a-sample-can-refute-a-law-not-prove-one) shows a sample getting it wrong.
