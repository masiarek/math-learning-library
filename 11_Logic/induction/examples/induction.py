#!/usr/bin/env python3
"""Induction: a base case, a step that runs forever, and the least counterexample.

Run:  python3 induction.py

A proof by induction shows P(0) and shows that P(n) forces P(n + 1), and
concludes P(n) for every n. The program runs the two checks on a range
(evidence, never proof), then shows why the method is sound: if P failed
anywhere it would fail first somewhere, by the well-ordering principle,
and the step forbids a first failure. It finds the least counterexample
to a famous false claim, finds the exact n where the "all cars are the
same colour" proof breaks, and runs five classic inductions, including
Fibonacci facts with Binet's formula computed exactly in Q(√5).
"""

from fractions import Fraction
from itertools import combinations


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


class Q5:
    """a + b√5 with rational a, b: exact arithmetic for Binet's formula."""

    def __init__(self, a, b=0):
        self.a, self.b = Fraction(a), Fraction(b)

    def __mul__(self, o):
        return Q5(self.a * o.a + 5 * self.b * o.b, self.a * o.b + self.b * o.a)

    def __sub__(self, o):
        return Q5(self.a - o.a, self.b - o.b)

    def __pow__(self, n):
        r = Q5(1)
        for _ in range(n):
            r = r * self
        return r

    def __str__(self):
        return f"{self.a} + {self.b}√5"


def main() -> None:
    print("1. THE TWO CHECKS, RUN ON A RANGE:  1 + 2 + ... + n = n(n + 1)/2")
    P = lambda n: sum(range(1, n + 1)) == Fraction(n * (n + 1), 2)
    step = all(Fraction(n * (n + 1), 2) + (n + 1) == Fraction((n + 1) * (n + 2), 2) for n in range(0, 200))
    print(f"   base case P(1): {P(1)}")
    print(f"   step: n(n+1)/2 + (n+1) == (n+1)(n+2)/2 for n = 0..199: {step}")
    print(f"   and P(n) itself for n = 1..200: {all(P(n) for n in range(1, 201))}")
    print("   The range is evidence. The proof is the algebra of the step, which")
    print("   holds for the letter n, not for 200 values of it.")
    print()

    print("2. WHY IT WORKS: A FALSE CLAIM HAS A LEAST COUNTEREXAMPLE, A STEP FORBIDS ONE")
    claim = lambda n: is_prime(n * n + n + 41)
    least = next(n for n in range(0, 1000) if not claim(n))
    print(f"   claim: n² + n + 41 is prime for every n.  true for n = 0..{least - 1}, and")
    print(f"   the least counterexample is n = {least}: {least}² + {least} + 41 = {least * least + least + 41} = 41 · 41.")
    print(f"   so the step P({least - 1}) → P({least}) is false: there is no proof of it to find.")
    print("   Well-ordering: every nonempty set of natural numbers has a least member.")
    print("   If the set of failures were nonempty it would have a least member m;")
    print("   m ≠ 0 by the base case, so P(m − 1) holds and the step gives P(m):")
    print("   contradiction. So the set of failures is empty. That is the whole proof")
    print("   that induction is a valid method.")
    print()

    print("3. WHERE THE 'ALL CARS ARE THE SAME COLOUR' PROOF BREAKS")
    print("   the step: in a set of n + 1 cars, {1..n} and {2..n+1} each have n cars,")
    print("   so each is one colour by hypothesis, and they overlap, so the colours agree.")
    for n in range(1, 5):
        first, second = set(range(1, n + 1)), set(range(2, n + 2))
        print(f"   n = {n}: {sorted(first)} and {sorted(second)} overlap in {sorted(first & second) or '∅'}"
              + ("   <- no overlap: the step from 1 car to 2 fails" if not first & second else ""))
    print("   The base case is fine and the step is fine for n ≥ 2; it is false for")
    print("   n = 1, and one missing rung is enough. Every car after that stands on it.")
    print()

    print("4. FIBONACCI: f(3n) EVEN, f(4n) DIVISIBLE BY 3, f(5n) BY 5; BINET EXACTLY")
    print(f"   f(3n) % 2 == 0 for n ≤ 30: {all(fib(3 * n) % 2 == 0 for n in range(31))}"
          f"   f(4n) % 3 == 0: {all(fib(4 * n) % 3 == 0 for n in range(31))}"
          f"   f(5n) % 5 == 0: {all(fib(5 * n) % 5 == 0 for n in range(31))}")
    print("   the step for f(3n) even: f(3n+3) = f(3n+2) + f(3n+1) = 2 f(3n+1) + f(3n), even + even.")
    phi, psi, r5 = Q5(Fraction(1, 2), Fraction(1, 2)), Q5(Fraction(1, 2), Fraction(-1, 2)), Q5(0, Fraction(1, 5))
    binet = lambda n: r5 * (phi ** n - psi ** n)
    b30 = binet(30)
    print(f"   Binet, computed in a + b√5 with exact fractions: f(30) = {b30}  (the √5 part cancels)")
    print(f"   f(30) by addition: {fib(30)}   equal: {b30.a == fib(30) and b30.b == 0}")
    nearest = all(round(((1 + 5 ** 0.5) / 2) ** n / 5 ** 0.5) == fib(n) for n in range(2, 60))
    print(f"   f(n) is the integer nearest φⁿ/√5 for n = 2..59: {nearest}   (|ψ|ⁿ/√5 < 1/2 from n = 2)")
    print()

    print("5. A SET OF n MEMBERS HAS 2ⁿ SUBSETS: THE PAIRING STEP, COUNTED")
    for n in range(1, 6):
        items = list(range(1, n + 1))
        subs = [frozenset(c) for r in range(n + 1) for c in combinations(items, r)]
        with_x = sum(1 for s in subs if n in s)
        print(f"   n = {n}: {len(subs):>2} subsets = {with_x} containing {n} + {len(subs) - with_x} not = 2 · 2^{n - 1}")
    print("   each subset without x pairs with one subset with x (add x), so the two")
    print("   halves are equal, and 2^n = 2 · 2^(n-1) is the step.")
    print()

    print("6. THE CHOCOLATE BAR: n × m SQUARES NEED nm − 1 BREAKS, IN ANY ORDER")

    def breaks(pieces, choose):
        count = 0
        while any(w * h > 1 for w, h in pieces):
            i = choose(pieces)
            w, h = pieces.pop(i)
            if w > 1:
                pieces += [(w // 2, h), (w - w // 2, h)]
            else:
                pieces += [(w, h // 2), (w, h - h // 2)]
            count += 1
        return count

    largest = lambda ps: max(range(len(ps)), key=lambda i: ps[i][0] * ps[i][1])
    first = lambda ps: next(i for i, (w, h) in enumerate(ps) if w * h > 1)
    for name, pick in [("split the largest piece", largest), ("split the first piece", first)]:
        print(f"   6 × 4, {name:<24} breaks: {breaks([(6, 4)], pick)}")
    print("   invariant: every break turns one piece into two, so pieces = breaks + 1,")
    print("   and 24 pieces need 23 breaks whatever the order. That invariant is the")
    print("   induction: P(k) = 'k squares need k − 1 breaks', and a break splits k into")
    print("   a + b with (a − 1) + (b − 1) + 1 = k − 1.")
    print()

    print("7. CLOSED FORMS, CHECKED, AND ONE DERIVED FROM THREE")
    N = range(0, 60)
    s1 = all(sum(range(1, n + 1)) == n * (n + 1) // 2 for n in N)
    s2 = all(sum(i * i for i in range(1, n + 1)) == n * (n + 1) * (2 * n + 1) // 6 for n in N)
    s3 = all(sum(i ** 3 for i in range(1, n + 1)) == (n * (n + 1) // 2) ** 2 for n in N)
    print(f"   Σi = n(n+1)/2: {s1}   Σi² = n(n+1)(2n+1)/6: {s2}   Σi³ = (n(n+1)/2)²: {s3}")
    mixed = all(sum(i * i + 3 * i + 5 for i in range(1, n + 1)) == Fraction(n * (n + 1) * (2 * n + 1), 6) + Fraction(3 * n * (n + 1), 2) + 5 * n for n in N)
    print(f"   Σ(i² + 3i + 5) = n(n+1)(2n+1)/6 + 3n(n+1)/2 + 5n: {mixed}   (sigma is linear: Σ(f + g) = Σf + Σg)")


if __name__ == "__main__":
    main()
