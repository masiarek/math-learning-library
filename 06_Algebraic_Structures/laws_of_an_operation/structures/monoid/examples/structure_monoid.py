#!/usr/bin/env python3
"""Monoid: associative, with an identity element: examples and non-examples, checked on finite samples.

Run:  python3 structure_monoid.py

A structure is a set and an operation that pass a list of laws. The program
takes each example, checks each of the four laws on a finite sample, and
prints the witness when a law fails. A sample can refute a law and never
prove one; the page says why the laws hold where they do.
"""

from fractions import Fraction
from itertools import permutations, product


def associative(items, op):
    bad = next(((a, b, c) for a in items for b in items for c in items if op(op(a, b), c) != op(a, op(b, c))), None)
    return bad is None, bad


def commutative(items, op):
    bad = next(((a, b) for a in items for b in items if op(a, b) != op(b, a)), None)
    return bad is None, bad


def identity(items, op):
    return next((e for e in items if all(op(e, x) == x == op(x, e) for x in items)), None)


def inverses(items, op, e):
    missing = [x for x in items if not any(op(x, y) == e == op(y, x) for y in items)]
    return not missing, missing


def report(name, items, op, show=str):
    assoc, bad = associative(items, op)
    comm, cbad = commutative(items, op)
    e = identity(items, op)
    inv, missing = inverses(items, op, e) if e is not None else (False, None)
    print(f"   {name}")
    print(f"     associative: {assoc}" + (f"   fails at {show(bad[0])}, {show(bad[1])}, {show(bad[2])}" if bad else ""))
    print(f"     identity:    {e is not None}" + (f"   it is {show(e)}" if e is not None else "   none in the sample"))
    print(f"     inverses:    {inv}" + (f"   none for {', '.join(show(m) for m in missing[:3])}" if missing else ""))
    print(f"     commutative: {comm}" + (f"   fails at {show(cbad[0])}, {show(cbad[1])}" if cbad else ""))
    return assoc, e is not None, inv, comm


def main() -> None:
    print("LAWS REQUIRED: associative, identity")
    from math import gcd
    nat = list(range(0, 7))
    report("ℕ under ×", nat, lambda a, b: a * b)
    report("ℕ under gcd", nat, gcd)
    report("strings under concatenation (sample)", ["", "a", "b", "ab"], lambda a, b: a + b, show=repr)
    subsets = [frozenset(c) for r in range(3) for c in [(), (1,), (2,), (1, 2)][r:r + 1]] + [frozenset({1, 2})]
    report("subsets of {1, 2} under ∪", subsets, lambda a, b: a | b, show=lambda s: "{" + ", ".join(map(str, sorted(s))) + "}" if s else "∅")
    report("positive integers 1..6 under + (the non-example)", list(range(1, 7)), lambda a, b: a + b)
    print("   each monoid has exactly one identity, and it is the value of an empty chain:")
    print(f"   sum([]) = {sum([])}, math.prod([]) = {__import__('math').prod([])}, ''.join([]) = {''.join([])!r}")


if __name__ == "__main__":
    main()
