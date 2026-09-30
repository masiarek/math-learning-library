#!/usr/bin/env python3
"""The algebra of sets is the algebra of logic, checked on every subset.

Run:  python3 algebra_of_sets.py

A member x of a universe U is in A or not, so every set operation is a
logical operation on that one yes/no: union is 'or', intersection is 'and',
complement is 'not', and A <= B is 'if x in A then x in B'. The program
takes U = {1, 2, 3, 4}, builds all 16 of its subsets, and checks each law
of set algebra on every pair or triple of them, 4,096 cases for a law in
three sets. It then searches for counterexamples to laws that look true
and are not, and shows that <= orders sets only partially, which is why
sorted() on a list of sets returns nonsense.
"""

from itertools import combinations, product

U = frozenset({1, 2, 3, 4})


def show(s) -> str:
    return "{" + ", ".join(str(x) for x in sorted(s)) + "}" if s else "{}"


def subsets(universe):
    items = sorted(universe)
    return [frozenset(c) for r in range(len(items) + 1) for c in combinations(items, r)]


def comp(a):
    """The complement, which only exists relative to a universe."""
    return U - a


def main() -> None:
    S = subsets(U)
    print("1. THE UNIVERSE AND ITS SUBSETS")
    print(f"   U = {show(U)}, and it has 2^{len(U)} = {len(S)} subsets:")
    for i in range(0, len(S), 8):
        print("     " + "  ".join(f"{show(s):<12}" for s in S[i:i + 8]).rstrip())
    A = frozenset({1, 2})
    print(f"   the complement of A = {show(A)} is U - A = {show(comp(A))}.")
    print("   Python's set has no complement operator: 'everything not in A'")
    print("   means nothing until U is fixed, so the code has to write U - A.")
    print()

    print("2. EACH OPERATION IS A LOGICAL OPERATION ON MEMBERSHIP")
    B = frozenset({2, 3})
    print(f"   A = {show(A)}, B = {show(B)}; for each x in U, is x in the result?")
    heads = ["in A", "in B", "A | B", "A & B", "A - B", "A ^ B", "U - A"]
    print("       x  " + "".join(f"{h:<7}" for h in heads).rstrip())
    for x in sorted(U):
        row = [x in A, x in B, x in A | B, x in A & B, x in A - B, x in A ^ B, x in comp(A)]
        print(f"     {x:>3}  " + "".join(f"{str(v):<7}" for v in row).rstrip())
    checks = all(
        ((x in a | b) == (x in a or x in b))
        and ((x in a & b) == (x in a and x in b))
        and ((x in a - b) == (x in a and x not in b))
        and ((x in a ^ b) == ((x in a) != (x in b)))
        and ((x in comp(a)) == (x not in a))
        for a, b in product(S, S) for x in U
    )
    print("   |  is or,  &  is and,  -  is 'and not',  ^  is 'exclusive or',")
    print(f"   U - A is not. Checked for every x in every pair of subsets: {checks}")
    sub = all((a <= b) == all((x not in a) or (x in b) for x in U) for a, b in product(S, S))
    print(f"   and A <= B is 'if x in A then x in B', for every pair: {sub}")
    print()

    print("3. THE LAWS, CHECKED ON EVERY CASE")
    E = frozenset()
    laws = [
        ("identity", "A | {} = A,   A & U = A", 1, lambda a, b, c: (a | E) == a and (a & U) == a),
        ("domination", "A | U = U,   A & {} = {}", 1, lambda a, b, c: (a | U) == U and (a & E) == E),
        ("idempotent", "A | A = A,   A & A = A", 1, lambda a, b, c: (a | a) == a and (a & a) == a),
        ("complement", "A | A' = U,  A & A' = {}", 1, lambda a, b, c: (a | comp(a)) == U and (a & comp(a)) == E),
        ("double complement", "(A')' = A", 1, lambda a, b, c: comp(comp(a)) == a),
        ("commutative", "A | B = B | A,  A & B = B & A", 2, lambda a, b, c: (a | b) == (b | a) and (a & b) == (b & a)),
        ("De Morgan", "(A | B)' = A' & B'", 2, lambda a, b, c: comp(a | b) == comp(a) & comp(b)),
        ("De Morgan", "(A & B)' = A' | B'", 2, lambda a, b, c: comp(a & b) == comp(a) | comp(b)),
        ("absorption", "A | (A & B) = A", 2, lambda a, b, c: (a | (a & b)) == a),
        ("difference", "A - B = A & B'", 2, lambda a, b, c: (a - b) == (a & comp(b))),
        ("associative", "(A | B) | C = A | (B | C)", 3, lambda a, b, c: ((a | b) | c) == (a | (b | c))),
        ("distributive", "A & (B | C) = (A & B) | (A & C)", 3, lambda a, b, c: (a & (b | c)) == ((a & b) | (a & c))),
        ("distributive", "A | (B & C) = (A | B) & (A | C)", 3, lambda a, b, c: (a | (b & c)) == ((a | b) & (a | c))),
    ]
    print(f"   {'law':<18} {'statement':<34} {'cases':>6}  holds")
    for name, text, arity, law in laws:
        cases = list(product(S, repeat=arity))
        ok = all(law(*(case + (E,) * (3 - arity))) for case in cases)
        print(f"   {name:<18} {text:<34} {len(cases):>6}  {ok}")
    print("   Every law holds in every case. Replace | & ' by or, and, not and each")
    print("   line is a law of logic; that is why they are true, and why checking")
    print("   the membership of one x settles them for all sets at once.")
    print()

    print("4. LAWS THAT LOOK TRUE AND ARE NOT: THE SEARCH FINDS A COUNTEREXAMPLE")
    tempting = [
        ("(A | B) - B = A", 2, lambda a, b, c: ((a | b) - b) == a),
        ("(A - B) | B = A", 2, lambda a, b, c: ((a - b) | b) == a),
        ("A - (B - C) = (A - B) - C", 3, lambda a, b, c: (a - (b - c)) == ((a - b) - c)),
        ("A - B = B - A", 2, lambda a, b, c: (a - b) == (b - a)),
        ("A | B = A | C  implies  B = C", 3, lambda a, b, c: (a | b) != (a | c) or b == c),
    ]
    for text, arity, law in tempting:
        bad = [case for case in product(S, repeat=arity) if not law(*(case + (E,) * (3 - arity)))]
        first = min(bad, key=lambda t: (sum(len(x) for x in t), [sorted(x) for x in t]))
        names = "ABC"[:arity]
        where = ", ".join(f"{n} = {show(s)}" for n, s in zip(names, first))
        print(f"   {text:<32} fails in {len(bad):>4} cases, e.g. {where}")
    print("   One counterexample is enough to kill a law; for the true laws of")
    print("   section 3, the search over every case is the proof that none exists.")
    print()

    print("5. VENN DIAGRAMS: n SETS MAKE 2^n REGIONS, ONE PER PATTERN OF MEMBERSHIP")
    for title, sets in [
        ("red and yellow overlap, green apart", {"red": {1, 2, 5}, "yellow": {1, 6}, "green": {4, 7}}),
        ("all three overlap at 1", {"red": {1, 2, 5}, "yellow": {1, 6}, "green": {1, 4, 7}}),
    ]:
        print(f"   {title}:  " + "  ".join(f"{k} = {show(v)}" for k, v in sets.items()))
        everything = set().union(*sets.values())
        for pattern in product((True, False), repeat=3):
            if not any(pattern):
                continue
            region = {x for x in everything
                      if all((x in s) == p for s, p in zip(sets.values(), pattern))}
            label = " & ".join(k if p else f"not {k}" for k, p in zip(sets, pattern))
            print(f"     {label:<34} {show(region)}")
        r, y, g = sets.values()
        print(f"     green.isdisjoint(red | yellow): {g.isdisjoint(r | y)}")
    print("   The 8th pattern, in none of the three, is everything outside the")
    print("   circles: the complement of the union, U - (R | Y | G).")
    print()

    print("6. <= IS A PARTIAL ORDER, SO SORTING SETS DOES NOT WORK")
    refl = all(a <= a for a in S)
    anti = all(not (a <= b and b <= a) or a == b for a, b in product(S, S))
    trans = all(not (a <= b and b <= c) or a <= c for a, b, c in product(S, S, S))
    comparable = sum(1 for a, b in combinations(S, 2) if a <= b or b <= a)
    pairs = len(S) * (len(S) - 1) // 2
    print(f"   reflexive {refl},  antisymmetric {anti},  transitive {trans}")
    print(f"   but of the {pairs} pairs of distinct subsets only {comparable} are comparable;")
    print(f"   {pairs - comparable} pairs, like {{1}} and {{2}}, have neither {{1}} <= {{2}} nor {{2}} <= {{1}}.")
    for data in ([{3}, {1, 2}, {1}], [{1, 2}, {1}, {3}], [{1}, {3}, {1, 2}]):
        print(f"   sorted({[show(d) for d in data]}) = {[show(d) for d in sorted(data)]}")
    print("   Same three sets, three different 'sorted' orders: sorted() uses <,")
    print("   which for sets is 'proper subset', and {3} is neither above nor below")
    print("   the others. Sort by a key that is a total order instead:")
    data = [{3}, {1, 2}, {1}]
    print(f"   sorted(..., key=lambda s: (len(s), sorted(s))) = "
          f"{[show(d) for d in sorted(data, key=lambda s: (len(s), sorted(s)))]}")

    print()

    print("7. SYMMETRIC DIFFERENCE: EXCLUSIVE OR, AND A GROUP")
    A, B = frozenset({1, 2, 3, 4}), frozenset({1, 4, 5})
    print(f"   A = {show(A)}, B = {show(B)}:  A ^ B = {show(A ^ B)}"
          "   2, 3 and 5 are each in one, not both")
    print(f"   (A - B) | (B - A) = {show((A - B) | (B - A))}   (A | B) - (A & B) = {show((A | B) - (A & B))}")
    assoc = all(((a ^ b) ^ c) == (a ^ (b ^ c)) for a, b, c in product(S, S, S))
    ident = all((a ^ E) == a for a in S)
    inverse = all((a ^ a) == E for a in S)
    comm = all((a ^ b) == (b ^ a) for a, b in product(S, S))
    print(f"   associative {assoc}   identity {{}} {ident}   A ^ A = {{}} {inverse}   commutative {comm}")
    print("   So the 16 subsets form a group under ^, every set its own inverse,")
    print("   which is why it is also written A + B. Adding the same set twice")
    print("   cancels, so a chain keeps exactly what occurs an odd number of times:")
    sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}, {7, 8, 1}]
    chain = frozenset()
    for t in sets:
        chain = chain ^ t
    print(f"   {' ^ '.join(show(t) for t in sets)} = {show(chain)}")
    eq = all(((a ^ b) == E) == (a == b) for a, b in product(S, S))
    print(f"   and A ^ B is empty exactly when A = B, for every pair: {eq}")

    print()

    print("8. QUANTIFIERS OVER A UNION OR AN INTERSECTION")
    V = frozenset({1, 2, 3})
    VS = subsets(V)
    preds = VS  # a predicate p on V is the set of x where p(x) is true

    def every(X, p):
        return all(x in p for x in X)

    def some(X, p):
        return any(x in p for x in X)

    claims = [
        ("∀x∈A∪B p  ⇒  ∀x∈A∩B p", lambda a, b, p: not every(a | b, p) or every(a & b, p)),
        ("∀x∈A∪B p  ⇔  ∀x∈A p ∧ ∀x∈B p", lambda a, b, p: every(a | b, p) == (every(a, p) and every(b, p))),
        ("∃x∈A∩B p  ⇒  ∃x∈A p ∧ ∃x∈B p", lambda a, b, p: not some(a & b, p) or (some(a, p) and some(b, p))),
        ("∃x∈A∪B p  ⇔  ∃x∈A p ∨ ∃x∈B p", lambda a, b, p: some(a | b, p) == (some(a, p) or some(b, p))),
        ("∀x∈A p ∨ ∀x∈B p  ⇒  ∀x∈A∪B p", lambda a, b, p: not (every(a, p) or every(b, p)) or every(a | b, p)),
        ("∃x∈A p ∧ ∃x∈B p  ⇒  ∃x∈A∩B p", lambda a, b, p: not (some(a, p) and some(b, p)) or some(a & b, p)),
    ]
    cases = list(product(VS, VS, preds))
    print(f"   every A, B ⊆ {show(V)} and every predicate p on it: {len(cases)} cases")
    for text, claim in claims:
        bad = [c for c in cases if not claim(*c)]
        if not bad:
            print(f"     {text:<34} holds")
        else:
            a, b, p = min(bad, key=lambda c: (sum(len(x) for x in c), [sorted(x) for x in c]))
            print(f"     {text:<34} fails, e.g. A = {show(a)}, B = {show(b)}, p true on {show(p)}")
    print("   ∀ splits over ∪ as ∧ and ∃ splits over ∪ as ∨; over ∩ only one")
    print("   direction survives. And over ∅:")
    print(f"     ∀x∈∅ p is {all(every(E, p) for p in preds)} for every p, "
          f"∃x∈∅ p is {any(some(E, p) for p in preds)} for every p")
    print("   which is why ∅ ⊆ A: 'every x in ∅ is in A' has no x to fail on.")
    dbl = all((a == b) == (a <= b and b <= a) for a, b in product(S, S))
    print(f"   and A = B exactly when A ⊆ B and B ⊆ A, for every pair of subsets of U: {dbl}")


if __name__ == "__main__":
    main()
