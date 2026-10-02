#!/usr/bin/env python3
"""Predicates and quantifiers: ∀ is a loop that must always succeed, ∃ one that must succeed once.

Run:  python3 predicates_and_quantifiers.py

A predicate P(x) is a statement with a hole; it becomes true or false
when x is filled from a universe of discourse. ∀x P(x) and ∃x P(x) are
then computed by loops. The program evaluates Cunningham's "x likes y"
sentences on two small worlds, checks the quantifier negation,
interchange and distribution laws on every predicate over a four-point
universe, finds the two laws that fail, and writes "exactly one" with
∃ and ∀.
"""

from itertools import product

PEOPLE = ("a", "b", "c", "d")


def predicates(universe):
    """Every one-place predicate on the universe, as the set where it is true."""
    return [frozenset(c for c, keep in zip(universe, bits) if keep)
            for bits in product((True, False), repeat=len(universe))]


def main() -> None:
    print("1. 'x LIKES y' IN TWO SMALL WORLDS (CUNNINGHAM, FIGURES 1.3 AND 1.4)")
    worlds = {
        "world A": {("a", "a"), ("a", "c"), ("b", "a"), ("b", "c"), ("c", "c"), ("d", "c")},
        "world B": {("a", "a"), ("b", "c"), ("c", "b"), ("d", "c")},
    }
    sentences = [
        ("∃x∃y L(x,y)", "someone likes someone", lambda L: any((x, y) in L for x in PEOPLE for y in PEOPLE)),
        ("∃y∃x L(x,y)", "someone is liked by someone", lambda L: any((x, y) in L for y in PEOPLE for x in PEOPLE)),
        ("∀x∀y L(x,y)", "everyone likes everyone", lambda L: all((x, y) in L for x in PEOPLE for y in PEOPLE)),
        ("∀x∃y L(x,y)", "everyone likes someone", lambda L: all(any((x, y) in L for y in PEOPLE) for x in PEOPLE)),
        ("∃y∀x L(x,y)", "someone is liked by everyone", lambda L: any(all((x, y) in L for x in PEOPLE) for y in PEOPLE)),
    ]
    for name, L in worlds.items():
        print(f"   {name}: " + ", ".join(f"{x} likes {y}" for x, y in sorted(L)))
    print(f"   {'sentence':<14} {'in English':<30} {'world A':>8} {'world B':>8}")
    for formula, english, test in sentences:
        print(f"   {formula:<14} {english:<30} {str(test(worlds['world A'])):>8} {str(test(worlds['world B'])):>8}")
    print("   The mixed pair differs in world B: everyone likes someone, but nobody")
    print("   is liked by everyone. ∀x∃y and ∃y∀x are different sentences.")
    print()

    print("2. INTERCHANGE LAWS, CHECKED ON ALL 65,536 RELATIONS ON FOUR PEOPLE")
    pairs = [(x, y) for x in PEOPLE for y in PEOPLE]
    relations = [frozenset(p for p, keep in zip(pairs, bits) if keep) for bits in product((True, False), repeat=16)]
    ee = all(sentences[0][2](L) == sentences[1][2](L) for L in relations)
    aa = all(all((x, y) in L for x in PEOPLE for y in PEOPLE) == all((x, y) in L for y in PEOPLE for x in PEOPLE) for L in relations)
    ea_implies = all((not sentences[4][2](L)) or sentences[3][2](L) for L in relations)
    gap = sum(1 for L in relations if sentences[3][2](L) and not sentences[4][2](L))
    print(f"   ∃x∃y ⇔ ∃y∃x: {ee}     ∀x∀y ⇔ ∀y∀x: {aa}     ∃y∀x ⇒ ∀x∃y: {ea_implies}")
    print(f"   ∀x∃y ⇒ ∃y∀x fails in {gap} of {len(relations)} relations; world B is one of them.")
    print("   Same-type quantifiers swap freely; a mixed pair swaps one way only.")
    print()

    print("3. NEGATION LAWS, ON EVERY PREDICATE OVER {a, b, c, d}")
    preds = predicates(PEOPLE)
    neg_all = all((not all(x in P for x in PEOPLE)) == any(x not in P for x in PEOPLE) for P in preds)
    neg_some = all((not any(x in P for x in PEOPLE)) == all(x not in P for x in PEOPLE) for P in preds)
    print(f"   ¬∀x P(x) ⇔ ∃x ¬P(x): {neg_all}      ¬∃x P(x) ⇔ ∀x ¬P(x): {neg_some}   ({len(preds)} predicates)")
    subsets = preds
    bounded = all((not all(x in P for x in A)) == any(x not in P for x in A) for A in subsets for P in preds)
    print(f"   bounded: ¬(∀x∈A)P(x) ⇔ (∃x∈A)¬P(x), every A and P: {bounded}")
    print("   Pushing ¬ through a quantifier flips it: 'not everyone' is 'someone not'.")
    print()

    print("4. DISTRIBUTION LAWS: TWO HOLD, TWO FAIL")
    tests = [
        ("∃x(P∨Q) ⇔ ∃xP ∨ ∃xQ", lambda P, Q: any(x in P or x in Q for x in PEOPLE) == (any(x in P for x in PEOPLE) or any(x in Q for x in PEOPLE))),
        ("∀x(P∧Q) ⇔ ∀xP ∧ ∀xQ", lambda P, Q: all(x in P and x in Q for x in PEOPLE) == (all(x in P for x in PEOPLE) and all(x in Q for x in PEOPLE))),
        ("∀x(P∨Q) ⇔ ∀xP ∨ ∀xQ", lambda P, Q: all(x in P or x in Q for x in PEOPLE) == (all(x in P for x in PEOPLE) or all(x in Q for x in PEOPLE))),
        ("∃x(P∧Q) ⇔ ∃xP ∧ ∃xQ", lambda P, Q: any(x in P and x in Q for x in PEOPLE) == (any(x in P for x in PEOPLE) and any(x in Q for x in PEOPLE))),
    ]
    for text, test in tests:
        bad = [(P, Q) for P in preds for Q in preds if not test(P, Q)]
        line = f"   {text:<24} holds for all {len(preds) ** 2} pairs: {not bad}"
        if bad:
            P, Q = min(bad, key=lambda t: (len(t[0]) + len(t[1]), sorted(t[0]), sorted(t[1])))
            line += f"   e.g. P true on {{{', '.join(sorted(P))}}}, Q true on {{{', '.join(sorted(Q))}}}"
        print(line)
    print("   'Everyone is P or Q' does not make everyone P or everyone Q; 'someone is")
    print("   P and someone is Q' does not make one person both.")
    print()

    print("5. 'EXACTLY ONE' FROM ∃ AND ∀, AND EXAMPLE 4 ON THE INTEGERS")
    unique = lambda P: any(x in P for x in PEOPLE) and all((x not in P or y not in P) or x == y for x in PEOPLE for y in PEOPLE)
    print(f"   ∃!x P(x) ⇔ ∃xP(x) ∧ ∀x∀y((P(x)∧P(y)) → x = y), every P: {all(unique(P) == (len(P) == 1) for P in preds)}")
    Z = range(-5, 6)
    print(f"   over the integers −5..5:  ∀x∃y (x + y = 0): {all(any(x + y == 0 for y in Z) for x in Z)}"
          f"     ∃y∀x (x + y = 0): {any(all(x + y == 0 for x in Z) for y in Z)}")
    print("   Every x has its own y = −x; no single y works for all x.")


if __name__ == "__main__":
    main()
