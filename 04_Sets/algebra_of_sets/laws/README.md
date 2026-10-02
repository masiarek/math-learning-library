# The laws of set algebra, one page each

**Level:** 101 · reference · the ten rows of the table on [the algebra of sets](../README.md), each with its own page

Each page states one law for sets, for logic and in Python, says in a sentence why it is true, names where it is used and the trap next to it, and runs a program that checks the law on every subset of a four-element universe and prints the matching truth table.

| Law | Sets |
|---|---|
| [identity](identity/README.md) | A ∪ ∅ = A, A ∩ U = A |
| [domination](domination/README.md) | A ∪ U = U, A ∩ ∅ = ∅ |
| [idempotent](idempotent/README.md) | A ∪ A = A, A ∩ A = A |
| [complement](complement/README.md) | A ∪ A′ = U, A ∩ A′ = ∅ |
| [double complement](double_complement/README.md) | (A′)′ = A |
| [commutative, associative](commutative_associative/README.md) | A ∪ B = B ∪ A, (A ∪ B) ∪ C = A ∪ (B ∪ C), and the same for ∩ |
| [distributive](distributive/README.md) | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C), and with ∪ and ∩ swapped |
| [absorption](absorption/README.md) | A ∪ (A ∩ B) = A, A ∩ (A ∪ B) = A |
| [De Morgan](de_morgan/README.md) | (A ∪ B)′ = A′ ∩ B′, (A ∩ B)′ = A′ ∪ B′ |
| [difference](difference/README.md) | A ∖ B = A ∩ B′ |

## Po polsku, w skrócie

Dziesięć praw algebry zbiorów z tabeli na stronie nadrzędnej, każde na osobnej stronie: dla zbiorów, dla logiki i w Pythonie, z jednym zdaniem dlaczego zachodzi, z zastosowaniem i pułapką obok, i z programem, który sprawdza prawo na wszystkich podzbiorach czteroelementowego uniwersum.
