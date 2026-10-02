#!/usr/bin/env python3
"""Cantor–Schröder–Bernstein: two injections make a bijection, by tracing ancestors.

Run:  python3 schroeder_bernstein.py

If f: A -> B and g: B -> A are both one-to-one, then A and B have the same
size: there is a bijection h: A -> B. The proof is an algorithm. Trace each
a backwards through g and f (a = g(b), b = f(a'), ...) until the chain
stops in A, stops in B, or never stops; send a to f(a) unless its chain
stops in B, where g⁻¹(a) is used instead. The program runs the construction
on every pair of injections between two four-element sets and on an
infinite example, N with f(n) = 2n and g(n) = 3n, checking that h is
one-to-one and onto in each case.
"""

from itertools import permutations


def csb(A, B, f, g):
    """The bijection h: A -> B built from injections f: A -> B and g: B -> A."""
    ginv = {g(b): b for b in B}
    finv = {f(a): a for a in A}

    def stops_in_B(a):
        x, side, seen = a, "A", set()
        while True:
            if (x, side) in seen:
                return False                   # a cycle: counts as never stopping
            seen.add((x, side))
            if side == "A":
                if x in ginv:
                    x, side = ginv[x], "B"
                else:
                    return False               # stops in A
            else:
                if x in finv:
                    x, side = finv[x], "A"
                else:
                    return True                # stops in B

    return {a: (ginv[a] if stops_in_B(a) else f(a)) for a in A}, stops_in_B


def is_bijection(h, A, B):
    return len(set(h.values())) == len(A) and set(h.values()) == set(B)


def main() -> None:
    print("1. THE CONSTRUCTION ON EVERY PAIR OF INJECTIONS BETWEEN TWO 4-SETS")
    A, B = (0, 1, 2, 3), ("w", "x", "y", "z")
    cases = 0
    ok = True
    differs = 0
    for pf in permutations(B):
        for pg in permutations(A):
            f = dict(zip(A, pf)).__getitem__
            g = dict(zip(B, pg)).__getitem__
            h, _ = csb(A, B, f, g)
            cases += 1
            ok &= is_bijection(h, A, B)
            differs += any(h[a] != f(a) for a in A)
    print(f"   {cases} pairs (f, g); h is a bijection every time: {ok}; h differs from f in {differs} of them.")
    print("   On finite sets of equal size every injection is already a bijection, so the")
    print("   finite check only shows the recipe never breaks; the infinite case is the point.")
    print()

    print("2. N WITH f(n) = 2n AND g(n) = 3n: NEITHER IS ONTO, h IS")
    N = range(0, 400)
    f = lambda n: 2 * n
    g = lambda n: 3 * n
    h, stops_in_B = csb(list(N), list(N), f, g)
    print("   trace a back: a = g(b)? only if 3 | a;  b = f(a')? only if b is even; and so on.")
    print(f"   {'a':>4} {'chain':<34} {'stops in':<9} h(a)")
    for a in [0, 1, 2, 3, 6, 9, 12, 18, 36, 54]:
        chain, x, side = [f"{a}"], a, "A"
        for _ in range(8):
            if side == "A" and x % 3 == 0 and x // 3 != x:
                x, side = x // 3, "B"; chain.append(f"g({x})")
            elif side == "B" and x % 2 == 0 and x // 2 != x:
                x, side = x // 2, "A"; chain.append(f"f({x})")
            else:
                break
        stop = "cycle" if a == 0 else ("B" if stops_in_B(a) else "A")
        print(f"   {a:>4} {' = '.join(chain):<34} {stop:<9} {h[a]}")
    inj = len(set(h.values())) == len(h)
    onto = all(any(h[a] == b for a in range(0, 3 * b + 1)) for b in range(0, 80))
    print(f"   h one-to-one on 0..399: {inj};  every b in 0..79 is h(a) for some a: {onto}.")
    print("   Where the chain stops in A or never stops, h = f; where it stops in B, h = g⁻¹,")
    print("   the division by 3. Every b is reached: by f if b's own chain stops in A or")
    print("   never, by g⁻¹ from g(b) if it stops in B, and never twice.")
    print()

    print("3. WHAT IT BUYS: ≤ ON SIZES IS ANTISYMMETRIC, WITHOUT THE AXIOM OF CHOICE")
    print("   |A| ≤ |B| means an injection A -> B exists. The theorem says |A| ≤ |B| and")
    print("   |B| ≤ |A| give |A| = |B|, so ≤ on cardinals is reflexive, antisymmetric and")
    print("   transitive: a partial order. That any two cardinals are comparable, making it")
    print("   linear, is equivalent to the axiom of choice; this theorem needs none of it.")
    print("   Classic use: [0, 1] and (0, 1). x -> x injects (0, 1) into [0, 1] and")
    print("   x -> x/2 + 1/4 injects [0, 1] into (0, 1); so the two intervals are equinumerous,")
    print("   and the recipe above says which countably many points have to shift to show it.")


if __name__ == "__main__":
    main()
