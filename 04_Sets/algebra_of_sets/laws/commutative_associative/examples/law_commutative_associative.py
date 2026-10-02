#!/usr/bin/env python3
"""The commutative and associative laws: order and grouping do not matter: checked on every subset of a four-element universe.

Run:  python3 law_commutative_associative.py

A law of set algebra is decided member by member, so checking it on all
subsets of U = {1, 2, 3, 4} (every pattern of membership there is) proves
it. The program checks the law, prints one worked instance, and shows the
law of logic it is in disguise, as a truth table.
"""

from itertools import combinations, product

U = frozenset({1, 2, 3, 4})
E = frozenset()
S = [frozenset(c) for r in range(5) for c in combinations(sorted(U), r)]


def comp(a):
    return U - a


def show(s):
    return "{" + ", ".join(str(x) for x in sorted(s)) + "}" if s else "∅"


def law(a, b=E, c=E):
    return (a | b) == (b | a) and (a & b) == (b & a) and ((a | b) | c) == (a | (b | c)) and ((a & b) & c) == (a & (b & c))


def main() -> None:
    print("1. THE LAW: A ∪ B = B ∪ A, A ∩ B = B ∩ A; (A ∪ B) ∪ C = A ∪ (B ∪ C), (A ∩ B) ∩ C = A ∩ (B ∩ C)")
    arity = 3
    cases = list(product(S, repeat=arity))
    print(f"   checked on all {len(cases)} choices of {arity} subset(s) of U = {show(U)}: {all(law(*t) for t in cases)}")
    print()
    print("2. ONE INSTANCE, WORKED")
    a, b, c = frozenset({1, 2}), frozenset({2, 3}), frozenset({3, 4})
    print(f"   A = {show(a)}, B = {show(b)}, C = {show(c)}, A' = {show(comp(a))}, B' = {show(comp(b))}")
    for line in [f'A ∪ B = {show(a | b)} = B ∪ A = {show(b | a)}', f'(A ∪ B) ∪ C = {show((a | b) | c)} = A ∪ (B ∪ C) = {show(a | (b | c))}']:
        print(f"   {line}")
    print()
    print("3. THE SAME LAW IN LOGIC: p ∨ q = q ∨ p, (p ∨ q) ∨ r = p ∨ (q ∨ r), and the same for ∧")
    print("   every row of the truth table agrees, which is why the member-by-member check is a proof:")
    letters = "pqr"[:3]
    rows = list(product((True, False), repeat=len(letters)))
    print("   " + "  ".join(letters) + "   left  right")
    for vals in rows:
        env = dict(zip(letters, vals))
        left, right = ((env['p'] or env['q']) or env['r']), (env['p'] or (env['q'] or env['r']))
        print("   " + "  ".join("T" if v else "F" for v in vals) + f"   {str(left)[0]:<5} {str(right)[0]}")


if __name__ == "__main__":
    main()
