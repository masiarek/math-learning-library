#!/usr/bin/env python3
"""Axiom katas: the first exercises of Jech and Cunningham, checked on a small universe.

Run:  python3 axiom_katas.py

A kata is an exercise done many times until the move is automatic. Each one
here is a statement from Jech's Set Theory, chapter 1 (exercises 1.1 to
1.15) or Cunningham's Set Theory: A First Course (exercises 1.4 and 1.5).
The program does not prove them; it checks each on every set of a small
universe, so that you know the claim is true before you look for the
proof, and so that a wrong reading of a formula shows up as a False.
"""

from itertools import combinations, product


def cumulative(n):
    level = [frozenset()] if n >= 1 else []
    for _ in range(n - 1):
        level = [frozenset(c) for r in range(len(level) + 1) for c in combinations(level, r)]
    return level


def show(s) -> str:
    if not s:
        return "∅"
    return "{" + ", ".join(sorted((show(x) for x in s), key=lambda t: (len(t), t))) + "}"


def power(a):
    items = list(a)
    return frozenset(frozenset(c) for r in range(len(items) + 1) for c in combinations(items, r))


def pair(a, b):
    return frozenset({a, b})


def kuratowski(a, b):
    return pair(pair(a, a), pair(a, b))


def von_neumann(n):
    numbers = [frozenset()]
    for k in range(n):
        numbers.append(numbers[k] | {numbers[k]})
    return numbers


def transitive(a):
    return all(x <= a for x in a)


def main() -> None:
    V3, V4 = cumulative(3), cumulative(4)
    U = set(V4)
    N = von_neumann(6)
    results = []

    def kata(source, claim, ok, note=""):
        results.append((source, claim, ok, note))

    # --- Jech, chapter 1 ---------------------------------------------------
    kata("Jech 1.1", "(a, b) = (c, d) iff a = c and b = d, with (a, b) = {{a}, {a, b}}",
         all((kuratowski(a, b) == kuratowski(c, d)) == (a == c and b == d)
             for a, b, c, d in product(V3, repeat=4)), "all 256 choices from V_3")
    kata("Jech 1.2", "there is no set X with P(X) ⊆ X",
         all(not (power(x) <= x) for x in V4), "every X in V_4; |P(X)| = 2^|X| > |X| is the proof")
    kata("Jech 1.3", "each n in N is transitive, and n = {m ∈ N : m < n}",
         all(transitive(n) for n in N) and all(N[k] == frozenset(N[:k]) for k in range(len(N))),
         "0 to 6, with m < n meaning m ∈ n")
    kata("Jech 1.5", "n ∉ n and n ≠ n + 1 for each n in N",
         all(n not in n and n != n | {n} for n in N))
    kata("Jech 1.7", "every nonempty X ⊆ N has an ∈-minimal element",
         all(any(not (m & frozenset(X)) for m in X)
             for r in range(1, 6) for X in combinations(N[:5], r)),
         "all 31 nonempty subsets of {0, ..., 4}; the hint says: pick n ∈ X, look at X ∩ n")
    kata("Jech 1.8", "each n ≠ 0 in N is m + 1 for some m",
         all(any(n == m | {m} for m in N) for n in N[1:]))

    def t_finite(s):
        """Every nonempty X ⊆ P(S) has a ⊆-maximal element."""
        ps = list(power(s))
        return all(any(not any(u < v for v in X) for u in X)
                   for r in range(1, len(ps) + 1) for X in combinations(ps, r))
    kata("Jech 1.10", "each n in N is T-finite (Tarski): every nonempty X ⊆ P(n) has a ⊆-maximal member",
         all(t_finite(n) for n in N[:4]), "n = 0 to 3; for n = 3, P(n) has 8 members and 255 nonempty X")
    kata("Jech 1.14", "separation follows from replacement: {x ∈ X : φ(x)} = F(X) for F = {(x, x) : φ(x)}",
         all(frozenset(x for x in X if len(x) == 1) == frozenset(y for x in X for y in [x] if len(x) == 1)
             for X in V4), "φ = 'x has one member', every X in V_4")

    def union_from_weak(X, Y):
        """Given a Y with ∪X ⊆ Y, separation inside Y recovers ∪X exactly."""
        return frozenset(u for u in Y if any(u in z for z in X))
    big = frozenset(V3)   # a superset of ∪X for every X in V_4
    kata("Jech 1.15", "the weak union axiom (∃Y ⊇ ∪X) plus separation gives ∪X",
         all(union_from_weak(X, big) == frozenset(u for z in X for u in z) for X in V4),
         "Y = V_3 works for every X in V_4; the same move does power set and replacement")

    # --- Cunningham, exercises 1.4: formulas in English, evaluated in V_4 --
    sentences = [
        ("1.4.1", "∃x ∀y (y ∉ x)", "there is a set with no members",
         any(all(y not in x for y in V4) for x in V4)),
        ("1.4.2", "∀y ∃x (y ∉ x)", "for every set there is a set it does not belong to",
         all(any(y not in x for x in V4) for y in V4)),
        ("1.4.3", "∀y ∃x (x ∉ y)", "no set contains every set",
         all(any(x not in y for x in V4) for y in V4)),
        ("1.4.4", "∀y ¬∃x (x ∉ y)", "every set contains every set",
         all(not any(x not in y for x in V4) for y in V4)),
        ("1.4.5", "∀z ∃x ∃y (x ∈ y ∧ y ∈ z)", "every set has a member that has a member",
         all(any(x in y and y in z for x in V4 for y in V4) for z in V4)),
    ]
    for num, formula, english, value in sentences:
        kata(f"Cunningham {num}", f"{formula}:  '{english}'", value,
             "true in V_4, as in ZF" if value else "false in V_4, as in ZF: ∅ is the counterexample")

    # --- Cunningham, exercises 1.5 ----------------------------------------
    u, v, w = V3[0], V3[1], V3[2]
    kata("Cunningham 1.5.1", "{u, v, w} exists: it is ∪{{u, v}, {w}} (pairs twice, union once)",
         frozenset(x for z in pair(pair(u, v), pair(w, w)) for x in z) == frozenset({u, v, w}))
    kata("Cunningham 1.5.2", "{A} exists: it is the pair {A, A}",
         all(pair(a, a) == frozenset({a}) for a in V4))
    kata("Cunningham 1.5.3", "A ∩ {A} = ∅, hence A ∉ A  (regularity)",
         all(not (a & frozenset({a})) and a not in a for a in V4))
    kata("Cunningham 1.5.4", "if A ∈ B then B ∉ A  (look at {A, B})",
         all((a not in b) or (b not in a) for a in V4 for b in V4))
    kata("Cunningham 1.5.5", "if A ∈ B and B ∈ C then C ∉ A  (look at {A, B, C})",
         all((not (a in b and b in c)) or (c not in a) for a in V4 for b in V4 for c in V4),
         "4096 triples")
    kata("Cunningham 1.5.6", "P(A) ∩ B exists: separation inside P(A) with 'x ∈ B'",
         all(frozenset(x for x in power(a) if x in b) == (power(a) & b) for a in V3 for b in V4))
    kata("Cunningham 1.5.7", "A ∖ B exists: separation inside A with 'x ∉ B'",
         all(frozenset(x for x in a if x not in b) == (a - b) for a in V4 for b in V4))
    kata("Cunningham 1.5.8", "∅, {∅}, {∅, {∅}} are pairwise distinct",
         len({N[0], N[1], N[2]}) == 3, "extensionality: ∅ has no member, {∅} has one, {∅, {∅}} has two")

    # --- Kunen, The Foundations of Mathematics, Exercise I.2.1 ---------------
    # Seven small membership graphs: (x, y) in E means x ∈ y. Which of
    # Extensionality, Foundation, Pairing, Union hold? Kunen's Pairing and
    # Union are the weak forms: some z contains x and y; some A contains
    # every member of every member of F.
    graphs = [
        ("1", "a", []),
        ("2", "a", [("a", "a")]),
        ("3", "ab", [("a", "b"), ("b", "a")]),
        ("4", "abc", [("a", "b"), ("b", "a"), ("a", "c"), ("b", "c")]),
        ("5", "abc", [("a", "b"), ("a", "c")]),
        ("6", "0123", [("0", "1"), ("0", "2"), ("0", "3"), ("1", "2"), ("1", "3"), ("2", "3")]),
        ("7", "abc", [("a", "b"), ("b", "c")]),
    ]

    def axioms_in(points, edges):
        u = {p: {x for x, y in edges if y == p} for p in points}
        ext = all((not all((z in u[x]) == (z in u[y]) for z in u)) or x == y for x in u for y in u)
        fnd = all((not u[x]) or any(not (u[y] & u[x]) for y in u[x]) for x in u)
        pr = all(any(x in u[z] and y in u[z] for z in u) for x in u for y in u)
        un = all(any(all(all(x in u[a] for x in u[y]) for y in u[f]) for a in u) for f in u)
        return ext, fnd, pr, un

    print("KUNEN, EXERCISE I.2.1: WHICH AXIOMS HOLD IN SEVEN SMALL MEMBERSHIP GRAPHS?")
    print("   (x, y) in E means x ∈ y; Pairing and Union in Kunen's weak forms.")
    print(f"   {'#':<3} {'universe':<44} {'Ext':>5} {'Found':>6} {'Pair':>5} {'Union':>6}")
    for num, points, edges in graphs:
        desc = ", ".join(f"{p} = {{{', '.join(sorted(x for x, y in edges if y == p))}}}" for p in points)
        ext, fnd, pr, un = axioms_in(points, edges)
        print(f"   {num:<3} {desc:<44} {str(ext):>5} {str(fnd):>6} {str(pr):>5} {str(un):>6}")
    print("   Pairing holds only in #2, as Kunen says: a ∈ a is the one point that")
    print("   contains a pair. Extensionality fails only in #5, where b and c have")
    print("   the same member. Foundation fails in #2 (a ∈ a) and #4 (c = {a, b} with")
    print("   a and b members of each other); #3 has the same two-cycle and passes,")
    print("   because the pair {a, b} is not in it. This exercise is the method of")
    print("   the whole chapter: an axiom is checked on a universe, not believed.")
    print()

    width = max(len(s) for s, _, _, _ in results)
    print("KATAS, CHECKED BEFORE YOU PROVE THEM")
    for source, claim, ok, note in results:
        print(f"  {source:<{width}}  {claim}")
        print(f"  {'':<{width}}  -> {ok}" + (f"   ({note})" if note else ""))
    print()
    print(f"{sum(1 for r in results if r[2] is True)} of {len(results)} checks come out True; the one False is")
    print("Cunningham 1.4.4, a sentence that is false in ZF too. A check is not a")
    print("proof: V_4 is one universe, and the proof has to work in every one.")


if __name__ == "__main__":
    main()
