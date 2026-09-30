#!/usr/bin/env python3
"""Sets in Python: each idea from the Sets chapter, found in the language.

Run:  python3 python_sets.py

The chapter's ideas are language-free: a set is its members, a rule cuts
a subset out of a set you already have, a complement needs a universe,
and the operations are or, and, not. This program finds each one in
Python, where most of them are a single line. How Python's set behaves
beyond that (hashing, operators against methods, frozenset, dict views)
is the Python library's page, "A set is a hash table".
"""


def show(s) -> str:
    return "{" + ", ".join(repr(x) for x in sorted(s)) + "}" if s else "set()"


def main() -> None:
    print("1. EXTENSIONALITY IS ==")
    print(f"   {{2, 5}} == {{5, 2}}       {({2, 5} == {5, 2})}   order is not membership")
    print(f"   {{1, 1, 2}} == {{1, 2}}    {({1, 1, 2} == {1, 2})}   neither is repetition")
    empties = [set(), {n for n in range(10) if n < 0}, set("abc") - set("cba")]
    print(f"   three empty sets built three ways, all equal: {all(e == empties[0] for e in empties)}")
    print("   there is one empty set; it is written set(), because {} is a dict")
    print()

    print("2. SEPARATION IS THE COMPREHENSION")
    primes = {n for n in range(1, 21) if n > 1 and all(n % d for d in range(2, n))}
    print(f"   {{n for n in range(1, 21) if n is prime}} = {show(primes)}")
    print("   The rule always draws from an existing source. Python has no syntax")
    print("   for 'every x such that ...' with no source, so it cannot state Russell.")
    print()

    print("3. THE OPERATIONS ARE OPERATORS")
    A, B = {1, 2, 3, 4}, {1, 4, 5}
    U = set(range(1, 7))
    rows = [
        ("A ∪ B", "A | B", A | B),
        ("A ∩ B", "A & B", A & B),
        ("A ∖ B", "A - B", A - B),
        ("A △ B", "A ^ B", A ^ B),
        ("A′", "U - A", U - A),
        ("A ⊆ B", "A <= B", A <= B),
        ("3 ∈ A", "3 in A", 3 in A),
    ]
    print(f"   A = {show(A)}, B = {show(B)}, U = {show(U)}")
    for math, code, value in rows:
        shown = show(value) if isinstance(value, set) else value
        print(f"     {math:<7} {code:<8} {shown}")
    print("   The complement has no operator: 'not in A' needs a universe, so")
    print("   the code must name U and write U - A.")
    print()

    print("4. CHAINED ^ KEEPS WHAT OCCURS AN ODD NUMBER OF TIMES")
    s1, s2, s3 = {0, 1, 2, 3, 4}, {2, 3, 4}, {2, 5}
    counts = {x: sum(x in s for s in (s1, s2, s3)) for x in s1 | s2 | s3}
    odd = {x for x, c in counts.items() if c % 2}
    print(f"   {show(s1)} ^ {show(s2)} ^ {show(s3)} = {show(s1 ^ s2 ^ s3)}")
    print("   occurrences: " + "  ".join(f"{x}:{counts[x]}" for x in sorted(counts))
          + f"   odd ones: {show(odd)}")
    print("   2 is in all three sets and stays: ^ is exclusive or, and it is a group")
    print("   operation in which every set cancels itself (the algebra of sets, section 7).")


if __name__ == "__main__":
    main()
