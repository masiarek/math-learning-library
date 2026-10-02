#!/usr/bin/env python3
"""A multiset is a set that counts: a function from a set to N, and Python's Counter.

Run:  python3 multisets.py

A set forgets how many times a thing was listed; a multiset remembers. The
program shows the letters of BANANA as a set and as a multiset, writes a
multiset as a function to N, checks that Counter's &, | and + are
intersection, union and sum, shows that gcd and lcm are the intersection
and union of prime factorisations, checks which set laws survive (union is
still idempotent, sum is not), and counts multisets with stars and bars.
"""

from collections import Counter
from itertools import combinations_with_replacement
from math import comb, gcd, lcm


def factors(n):
    """The prime factorisation of n as a multiset of primes."""
    out, p = Counter(), 2
    while n > 1:
        while n % p == 0:
            out[p] += 1
            n //= p
        p += 1
    return out


def show(c):
    return "[" + ", ".join(str(k) for k in sorted(c.elements())) + "]"


def main() -> None:
    print("1. BANANA AS A SET AND AS A MULTISET")
    word = "BANANA"
    print(f"   set(\"{word}\")     = {sorted(set(word))}: 3 members, repetition forgotten")
    print(f"   Counter(\"{word}\") = {dict(sorted(Counter(word).items()))}: each letter with its multiplicity")
    print("   A multiset M on a set S is a function M: S -> N giving each member a count;")
    print("   its members are the x with M(x) > 0, and |M| is the sum of the counts.")
    print(f"   |Counter(\"{word}\")| = {sum(Counter(word).values())} = len(\"{word}\")")
    print()

    print("2. THE OPERATIONS: & IS MIN, | IS MAX, + ADDS, - SUBTRACTS AND DROPS ZEROS")
    a, b = Counter("aabbbc"), Counter("abbdd")
    print(f"   a = {show(a)}   b = {show(b)}")
    for name, c in [("a & b (min)", a & b), ("a | b (max)", a | b), ("a + b (sum)", a + b), ("a - b (difference)", a - b)]:
        print(f"   {name:<20} = {show(c)}")
    print("   a ⊆ b for multisets means every count in a is at most the count in b:")
    sub = lambda x, y: all(x[k] <= y[k] for k in x)
    print(f"   a ⊆ a | b: {sub(a, a | b)}   a & b ⊆ a: {sub(a & b, a)}   a ⊆ b: {sub(a, b)}")
    print()

    print("3. GCD AND LCM ARE ∩ AND ∪ OF PRIME FACTORISATIONS, THE PRODUCT IS +")
    for n in (360, 84):
        print(f"   {n} = {show(factors(n))}")
    print(f"   360 & 84 = {show(factors(360) & factors(84))} = {gcd(360, 84)} = gcd;   360 | 84 = {show(factors(360) | factors(84))} = {lcm(360, 84)} = lcm")
    value = lambda c: eval("*".join(str(k) for k in c.elements()) or "1")
    ok = all(value(factors(x) & factors(y)) == gcd(x, y) and value(factors(x) | factors(y)) == lcm(x, y)
             and value(factors(x) + factors(y)) == x * y for x in range(1, 61) for y in range(1, 61))
    print(f"   checked for all x, y in 1..60: {ok}.  'm divides n' is 'factors(m) ⊆ factors(n)', as a multiset.")
    print()

    print("4. WHICH SET LAWS SURVIVE")
    c = Counter("aab")
    print(f"   c = {show(c)}:  c | c = {show(c | c)} (idempotent, like ∪)   c + c = {show(c + c)} (not: like + on numbers)")
    print(f"   c & c = {show(c & c)} (idempotent)   c - c = {show(c - c)} (empty)")
    print("   |, & and + are commutative and associative; | and & distribute over each other;")
    print("   there is no complement, since a count has no 'everything above it' to subtract from.")
    print()

    print("5. COUNTING MULTISETS: k THINGS FROM n KINDS, REPETITION ALLOWED")
    kinds = "abc"
    ms = list(combinations_with_replacement(kinds, 2))
    print(f"   multisets of size 2 from {{a, b, c}}: {len(ms)}: " + ", ".join("".join(m) for m in ms))
    print(f"   formula C(n + k − 1, k) = C(4, 2) = {comb(4, 2)}; against C(n, k) = {comb(3, 2)} sets of size 2.")
    print("   Stars and bars: write k stars and n − 1 bars, aa|b| is a a b; choose where the bars go.")
    print()

    print("6. WHERE THE SET WAS THE WRONG TYPE")
    weights = [70, 82, 70, 65, 82, 82]
    print(f"   'the weights of all people in Canada', Ashlock's problem 2.1: list {weights}")
    print(f"   as a set {sorted(set(weights))} loses the count; as a multiset {dict(sorted(Counter(weights).items()))} keeps it,")
    print("   and 'all weights at least one person had' is exactly the set. A histogram is a")
    print("   multiset; so is a prime factorisation, a shopping basket, a bag of words.")


if __name__ == "__main__":
    main()
