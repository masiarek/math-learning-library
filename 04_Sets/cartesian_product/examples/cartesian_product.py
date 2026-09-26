#!/usr/bin/env python3
"""The Cartesian product: every ordered pair, first entry from A, second from B.

Run:  python3 cartesian_product.py

A x B is the set of all pairs (a, b) with a in A and b in B. Three things
about it are easy to say and easy to get wrong, so the program checks each
one on real sets: the pair is ordered, so (2, 5) and (5, 2) are different
members; the product is not commutative, so A x B and B x A can share no
member at all; and a pair may repeat its entry, so (1, 1) is in A x A.

Python's tuple is an ordered pair, and its set is a set, so the checks are
one-liners over the real objects rather than claims about them.
"""

from itertools import product


def cartesian(A: frozenset, B: frozenset) -> frozenset:
    """A x B, built from the definition: every (a, b) with a in A and b in B."""
    return frozenset((a, b) for a in A for b in B)


def show(name: str, pairs: frozenset, per_row: int) -> None:
    """Print a set of pairs as a grid, sorted so the output is stable."""
    cells = [f"({a}, {b})" for a, b in sorted(pairs, key=lambda p: (str(p[0]), str(p[1])))]
    for i in range(0, len(cells), per_row):
        row = "  ".join(f"{c:<7}" for c in cells[i : i + per_row])
        print(f"     {name if i == 0 else ' ' * len(name)}  {row}".rstrip())


def main() -> None:
    P = frozenset({"a", "b"})
    Q = frozenset({1, 2, 3})

    print("1. A PAIR IS ORDERED; A SET IS NOT")
    print(f"   (2, 5) == (5, 2)   is {(2, 5) == (5, 2)}")
    print(f"   {{2, 5}} == {{5, 2}}   is {({2, 5} == {5, 2})}")
    print(f"   (3, 3) has {len((3, 3))} entries;  {{3, 3}} has {len({3, 3})} member")
    print("   Two pairs are equal exactly when both entries match in order.")
    print()

    print("2. THE PRODUCT, FROM THE DEFINITION")
    print("   P = {a, b}   Q = {1, 2, 3}")
    print("   P x Q is every (p, q) with p in P and q in Q, laid out as a grid:")
    print("   rows are members of P, columns are members of Q.")
    PQ = cartesian(P, Q)
    show("P x Q =", PQ, per_row=3)
    print(f"   |P| x |Q| = {len(P)} x {len(Q)} = {len(P) * len(Q)};  the grid has {len(PQ)} cells.")
    print()

    print("3. SWAP THE FACTORS AND YOU GET A DIFFERENT SET")
    QP = cartesian(Q, P)
    show("Q x P =", QP, per_row=2)
    print(f"   P x Q == Q x P            is {PQ == QP}")
    print(f"   members they share:       {sorted(PQ & QP)}")
    print(f"   ('a', 1) in P x Q         is {('a', 1) in PQ}")
    print(f"   ('a', 1) in Q x P         is {('a', 1) in QP}")
    print("   'a' is not in Q, so it cannot be a first entry of a Q x P pair.")
    print("   Same size, and not one member in common. The product is not")
    print("   commutative: which set feeds which slot is part of the definition.")
    print()

    print("4. A SET TIMES ITSELF, AND THE PAIRS WITH A REPEATED ENTRY")
    S = frozenset({0, 1})
    SS = cartesian(S, S)
    print("   S = {0, 1}")
    show("S x S =", SS, per_row=2)
    print(f"   (0, 0) in S x S           is {(0, 0) in SS}")
    print(f"   (1, 1) in S x S           is {(1, 1) in SS}")
    print(f"   |S x S| = {len(SS)}, not {len(SS) - len(S)}. Dropping the repeats is the usual")
    print("   mistake: nothing in the definition says the two entries differ.")
    print()

    print("5. THE COUNT IS ALWAYS THE PRODUCT OF THE SIZES")
    print(f"     {'|A|':>3}  {'|B|':>3}  {'|A x B|':>7}  |A| x |B|")
    for m in range(0, 4):
        for n in (0, 1, 3, 5):
            A = frozenset(range(m))
            B = frozenset(range(100, 100 + n))
            AB = cartesian(A, B)
            assert len(AB) == m * n
            print(f"     {m:>3}  {n:>3}  {len(AB):>7}  {m * n:>9}")
    print("   Including the empty set: a product with an empty factor is empty,")
    print("   because there is nothing to put in that slot.")
    print()

    print("6. THE SAME THING PYTHON CALLS itertools.product")
    print(f"   set(product(P, Q)) == P x Q   is {frozenset(product(P, Q)) == PQ}")
    print("   The library and the definition agree, pair for pair.")


if __name__ == "__main__":
    main()
