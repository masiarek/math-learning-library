#!/usr/bin/env python3
"""Four founding papers of set theory, each checked on small sets.

Run:  python3 classic_set_theory.py

Set theory began in a handful of short papers, and the idea of each one
fits in a few lines of code. Cantor (1874) lists the algebraic numbers by
height; Dedekind (1888) defines "infinite" as matching a proper part of
oneself; Cantor (1891) shows that no set matches its own power set; von
Neumann (1923) makes each natural number the set of the smaller ones. The
program checks each claim exhaustively where a finite check is a proof, and
prints the first lines of the infinite case where it is not.
"""

from fractions import Fraction
from itertools import product
from math import gcd, sqrt


def show(s) -> str:
    """A set of numbers, or of sets, in braces, sorted where that makes sense."""
    if not s:
        return "{}"
    items = sorted(s) if all(isinstance(x, (int, Fraction)) for x in s) else sorted(s, key=len)
    return "{" + ", ".join(show(x) if isinstance(x, frozenset) else str(x) for x in items) + "}"


# ---------------------------------------------------------------------------
# 1. Cantor 1874
# ---------------------------------------------------------------------------

def coefficient_lists(k, total):
    """All k-tuples of integers whose absolute values add up to total."""
    if k == 0:
        if total == 0:
            yield ()
        return
    for a in range(-total, total + 1):
        for rest in coefficient_lists(k - 1, total - abs(a)):
            yield (a,) + rest


def equations(height):
    """Integer equations a0·x^n + ... + an = 0 of Cantor's height
    n - 1 + |a0| + ... + |an|, with n >= 1, a0 > 0 and no common factor."""
    out = []
    for n in range(1, height + 1):
        for coeffs in coefficient_lists(n + 1, height - n + 1):
            if coeffs[0] > 0 and gcd(*coeffs) == 1:
                out.append(coeffs)
    return out


def evaluate(coeffs, x):
    value = Fraction(0)
    for a in coeffs:
        value = value * x + a
    return value


def divisors(m):
    m = abs(m)
    return [d for d in range(1, m + 1) if m % d == 0]


def rational_roots(coeffs):
    """The roots in Q, by the rational root theorem: p/q with p | an, q | a0."""
    if coeffs[-1] == 0:
        rest = rational_roots(coeffs[:-1]) if len(coeffs) > 2 else set()
        return {Fraction(0)} | rest
    candidates = {Fraction(sign * p, q)
                  for p in divisors(coeffs[-1]) for q in divisors(coeffs[0]) for sign in (1, -1)}
    return {r for r in candidates if evaluate(coeffs, r) == 0}


def real_roots_if_irreducible(coeffs):
    """The real roots of an irreducible equation of degree at most 2, or None
    if the equation factors over Q. Enough for every equation of height <= 4:
    there, every equation of degree 3 or more has a rational root."""
    n = len(coeffs) - 1
    if n == 1:
        return [Fraction(-coeffs[1], coeffs[0])]
    if rational_roots(coeffs):
        return None                      # reducible: dropped, as Cantor did
    if n > 2:
        raise NotImplementedError("an irreducible cubic: height above 4")
    a, b, c = coeffs
    disc = b * b - 4 * a * c
    if disc < 0:
        return []                        # irreducible, but no real root
    return [(-b - sqrt(disc)) / (2 * a), (-b + sqrt(disc)) / (2 * a)]


def number(x) -> str:
    return str(x) if isinstance(x, Fraction) else f"{x:.5f}"


# ---------------------------------------------------------------------------
# 4. von Neumann 1923
# ---------------------------------------------------------------------------

def von_neumann(n):
    """0 = {}, and k + 1 = k ∪ {k}: each number is the set of the smaller ones."""
    numbers = [frozenset()]
    for k in range(n):
        numbers.append(numbers[k] | {numbers[k]})
    return numbers


def main() -> None:
    print("1. CANTOR 1874: THE ALGEBRAIC NUMBERS CAN BE LISTED BY HEIGHT")
    print("   An algebraic number is a real root of a0·x^n + ... + an = 0 with")
    print("   integer coefficients, a0 > 0 and no common factor. Cantor gives the")
    print("   equation a height, n - 1 + |a0| + ... + |an|, and only finitely")
    print("   many equations share a height:")
    heights = range(1, 8)
    print("     height     " + "".join(f"{h:>5}" for h in heights))
    print("     equations  " + "".join(f"{len(equations(h)):>5}" for h in heights))
    print("   An equation of degree n has at most n real roots, so each height")
    print("   adds finitely many numbers. Listed height by height, with the")
    print("   reducible equations dropped as Cantor dropped them, the real")
    print("   algebraic numbers begin:")
    for h in range(1, 5):
        roots = []
        for coeffs in equations(h):
            found = real_roots_if_irreducible(coeffs)
            if found:
                roots.extend(found)
        print(f"     height {h}:  " + ", ".join(number(r) for r in sorted(roots)))
    print("   Every algebraic number has a height, so every one gets a place in")
    print("   the list: the algebraic numbers are countable. The second half of")
    print("   the paper shows that the real numbers cannot be listed at all, so")
    print("   some real numbers are not algebraic: transcendental numbers exist,")
    print("   proved without exhibiting a single one.")
    print()

    print("2. DEDEKIND 1888: INFINITE MEANS MATCHING A PROPER PART OF ITSELF")
    print("   Dedekind's definition: a set is infinite when some one-to-one map")
    print("   sends it into a proper subset of itself, and finite otherwise.")
    print("   Finite sets fail it. A set of n members has n^n maps into itself;")
    print("   the one-to-one ones are the n! permutations, and each one is onto:")
    for n in range(1, 6):
        members = range(n)
        maps = list(product(members, repeat=n))        # f(0), ..., f(n-1)
        injective = [f for f in maps if len(set(f)) == n]
        onto = all(set(f) == set(members) for f in injective)
        print(f"     n = {n}: {len(maps):>5} maps, {len(injective):>4} one-to-one, all onto: {onto}")
    print("   N passes it. n -> 2n is one-to-one and lands in the even numbers:")
    print("     n:  " + "".join(f"{n:>3}" for n in range(10)) + " ...")
    print("     2n: " + "".join(f"{2 * n:>3}" for n in range(10)) + " ...")
    print("   1, 3, 5, 7, ... are never hit, so the image is a proper part of N.")
    print("   That is why a set can have as many members as one of its proper")
    print("   subsets, and why only an infinite set can.")
    print()

    print("3. CANTOR 1891: NO SET MATCHES ITS OWN POWER SET")
    A = ("a", "b", "c")
    P = [frozenset(c) for r in range(len(A) + 1) for c in __import__("itertools").combinations(A, r)]
    print(f"   A = {{a, b, c}}; P(A), the set of its subsets, has 2^{len(A)} = {len(P)} members.")
    print("   A map f: A -> P(A) picks a subset for each member. The diagonal set")
    print("   D = {x in A : x not in f(x)} differs from f(x) at x, for every x:")

    def diagonal(f):
        return frozenset(x for x, fx in zip(A, f) if x not in fx)

    def braces(s):
        return "{" + ", ".join(sorted(s)) + "}"

    f = (frozenset("ab"), frozenset(), frozenset("abc"))
    for x, fx in zip(A, f):
        inside = x in fx
        print(f"     f({x}) = {braces(fx):<10} {x} in f({x}): {str(inside):<6} so {x} {'not in' if inside else 'in'} D")
    D = diagonal(f)
    print(f"     D = {braces(D)}, and D is not f(a), f(b) or f(c): {D not in f}")
    every = list(product(P, repeat=len(A)))
    never = all(diagonal(g) not in g for g in every)
    print(f"   All {len(P)}^{len(A)} = {len(every)} maps A -> P(A) checked: D is never in the image,")
    print(f"   so no map is onto: {never}. Here counting would do (3 < 8), but the")
    print("   sentence 'D differs from f(x) at x' never counted anything, so it")
    print("   works for infinite sets too: |P(A)| > |A| always, and no set is")
    print("   the largest.")
    print()

    print("4. VON NEUMANN 1923: EACH NUMBER IS THE SET OF THE SMALLER ONES")
    print("   0 = {}, and n + 1 = n ∪ {n}:")
    N = von_neumann(5)
    name = {s: k for k, s in enumerate(N)}

    def by_name(s):
        return "{" + ", ".join(str(name[x]) for x in sorted(s, key=len)) + "}"

    for k, s in enumerate(N):
        nested = f" = {show(s)}" if k <= 2 else ""
        print(f"     {k} = {by_name(s)}{nested}")
    sizes = all(len(s) == k for k, s in enumerate(N))
    member = all((m < n) == (N[m] in N[n]) for m in range(6) for n in range(6))
    subset = all((m < n) == (N[m] < N[n]) for m in range(6) for n in range(6))
    print(f"   n has exactly n members: {sizes}")
    print(f"   m < n  iff  m ∈ n: {member}      m < n  iff  m is a proper subset of n: {subset}")
    print("   Order, membership and inclusion agree, and nothing but sets was")
    print("   used, so the natural numbers need no axiom of their own. Carrying")
    print("   on past them, ω = {0, 1, 2, ...} and ω + 1 = ω ∪ {ω}, gives the")
    print("   ordinals, and n ∪ {n} is still the successor.")


if __name__ == "__main__":
    main()
