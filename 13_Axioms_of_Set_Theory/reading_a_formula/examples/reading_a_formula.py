#!/usr/bin/env python3
"""Every symbol of a set theory formula is a line of Python; here are the lines.

Run:  python3 reading_a_formula.py

A universe is a collection of points and a membership relation between them,
nothing more. The program keeps one as a dict: each point maps to the set of
its members. On such a universe every formula of set theory can be evaluated
by brute force: ∀ is a loop that must succeed every time, ∃ a loop that must
succeed once, ⇒ is 'not p or q', ⇔ is ==, ∈ is a dictionary lookup. Section
2 prints the translation table; section 3 reads two axioms aloud in English
and in Python and evaluates them; section 4 evaluates every axiom of ZF on
four small universes, which shows what each axiom asks for.
"""

from itertools import combinations


# ---------------------------------------------------------------------------
# Universes
# ---------------------------------------------------------------------------

def cumulative(n):
    """V_n, the hereditarily finite sets of rank below n, as a universe.
    V_0 is empty; V_1 = {∅}; V_2 = {∅, {∅}}; V_3 has 4 sets; V_4 has 16."""
    level = [frozenset()] if n >= 1 else []
    for _ in range(n - 1):
        level = [frozenset(c) for r in range(len(level) + 1) for c in combinations(level, r)]
    return {s: set(s) for s in level}


def show(s) -> str:
    """A hereditarily finite set in braces, ∅ for the empty one, members sorted."""
    if not s:
        return "∅"
    return "{" + ", ".join(sorted((show(x) for x in s), key=lambda t: (len(t), t))) + "}"


def label(u, x) -> str:
    return show(x) if isinstance(x, frozenset) else str(x)


# ---------------------------------------------------------------------------
# The axioms, each as the formula and as the Python that evaluates it
# ---------------------------------------------------------------------------

def member(u, x, y):
    """x ∈ y in the universe u."""
    return x in u[y]


def extensionality(u):
    return all((not all(member(u, z, x) == member(u, z, y) for z in u)) or x == y
               for x in u for y in u)


def pairs(u):
    return all(any(all(member(u, w, z) == (w == x or w == y) for w in u) for z in u)
               for x in u for y in u)


def unions(u):
    return all(any(all(member(u, z, y) == any(member(u, w, x) and member(u, z, w) for w in u) for z in u)
                   for y in u) for x in u)


def power_set(u):
    return all(any(all(member(u, z, y) == all((not member(u, w, z)) or member(u, w, x) for w in u) for z in u)
                   for y in u) for x in u)


def comprehension(u, prop):
    """One instance of the scheme, for one property of the points."""
    return all(any(all(member(u, z, y) == (member(u, z, x) and prop(u, z)) for z in u) for y in u)
               for x in u)


def replacement(u, func):
    """One instance of the scheme, for one function on the points."""
    return all(any(all(member(u, z, y) == any(member(u, w, x) and func(u, w) == z for w in u) for z in u)
                   for y in u) for x in u)


def infinity(u):
    empty = [x for x in u if not u[x]]
    if not empty:
        return False
    e = empty[0]

    def successor_in(x, s):          # x ∪ {x} ∈ s
        return any(u[t] == u[x] | {x} for t in u if member(u, t, s))

    return any(member(u, e, s) and all((not member(u, x, s)) or successor_in(x, s) for x in u) for s in u)


def foundation(u):
    return all((not u[x]) or any(member(u, y, x) and not (u[y] & u[x]) for y in u) for x in u)


def choice(u):
    """For every set of nonempty, pairwise disjoint sets, some set meets each
    of them in exactly one point."""
    for a in u:
        family = [x for x in u if member(u, x, a)]
        if any(not u[x] for x in family):
            continue
        if any(u[x] & u[y] for x, y in combinations(family, 2)):
            continue
        if not any(all(len(u[c] & u[x]) == 1 for x in family) for c in u):
            return False
    return True


def is_empty(u, z):
    return not u[z]


def singleton_of(u, w):
    """w ↦ {w}, as a point of the universe if there is one, else None."""
    for z in u:
        if u[z] == {w}:
            return z
    return None


def main() -> None:
    print("1. A UNIVERSE IS POINTS AND A MEMBERSHIP RELATION, NOTHING ELSE")
    for n in range(1, 5):
        u = cumulative(n)
        names = ", ".join(show(x) for x in sorted(u, key=lambda s: (len(show(s)), show(s))))
        print(f"   V_{n}: {len(u):>2} points: {names}" if n < 4 else f"   V_{n}: {len(u):>2} points: ∅, {{∅}}, {{{{∅}}}}, {{∅, {{∅}}}}, ... (every set of sets of sets of ∅)")
    print("   x ∈ y is looked up in a table: in V_3, ∅ ∈ {∅}? True   {∅} ∈ ∅? False")
    u3 = cumulative(3)
    e, one = frozenset(), frozenset([frozenset()])
    assert member(u3, e, one) and not member(u3, one, e)
    print()

    print("2. THE TRANSLATION TABLE")
    rows = [
        ("∀v F", "for every point v of the universe, F", "all(F(v) for v in U)"),
        ("∃v F", "for at least one point v, F", "any(F(v) for v in U)"),
        ("F ∧ G", "F and G", "F and G"),
        ("F ∨ G", "F or G, or both", "F or G"),
        ("¬F", "not F", "not F"),
        ("F ⇒ G", "if F then G: forbidden only when F true, G false", "(not F) or G"),
        ("F ⇔ G", "F and G have the same truth value", "F == G"),
        ("x ≃ y", "x and y are the same point", "x == y"),
        ("x ∈ y", "x is a member of y", "x in U[y]"),
        ("x ∉ y", "x is not a member of y", "x not in U[y]"),
        ("∀x ∈ y F", "for every member x of y, F", "all(F(x) for x in U[y])"),
        ("∃x ∈ y F", "for some member x of y, F", "any(F(x) for x in U[y])"),
    ]
    print(f"   {'formula':<11} {'read aloud':<52} Python")
    for sym, words, code in rows:
        print(f"   {sym:<11} {words:<52} {code}")
    print()

    print("3. TWO AXIOMS READ ALOUD, THEN EVALUATED")
    print("   Extensionality:  ∀v0 ∀v1 (∀v2 (v2 ∈ v0 ⇔ v2 ∈ v1) ⇒ v0 ≃ v1)")
    print("     for every v0, for every v1: if every v2 is in v0 exactly when it is")
    print("     in v1, then v0 and v1 are the same point. Two sets with the same")
    print("     members are equal.")
    print("     all((not all((z in U[x]) == (z in U[y]) for z in U)) or x == y")
    print("         for x in U for y in U)")
    print("   Pairs:  ∀v0 ∀v1 ∃v2 ∀v3 (v3 ∈ v2 ⇔ (v3 ≃ v0 ∨ v3 ≃ v1))")
    print("     for every v0 and v1 there is a v2 such that a point is in v2")
    print("     exactly when it is v0 or v1. The pair {v0, v1} exists.")
    print("     all(any(all((w in U[z]) == (w == x or w == y) for w in U) for z in U)")
    print("         for x in U for y in U)")
    for n in (2, 3, 4):
        u = cumulative(n)
        print(f"   in V_{n}:  extensionality {extensionality(u)}   pairs {pairs(u)}")
    print("   Pairs fails in every V_n: the pair of two sets from the top rank")
    print("   has a rank one higher, and that rank is not in the universe.")
    print()

    print("4. EVERY AXIOM ON FOUR UNIVERSES: TRUE MEANS 'THE UNIVERSE HAS WHAT IT ASKS FOR'")
    print("   U(atoms) is {a, b, c} with a and b memberless and c = {a}: two 'empty sets'.")
    atoms = {"a": set(), "b": set(), "c": {"a"}}
    universes = [("V_2", cumulative(2)), ("V_3", cumulative(3)), ("V_4", cumulative(4)), ("U(atoms)", atoms)]
    axioms = [
        ("extensionality", extensionality),
        ("pairs", pairs),
        ("unions", unions),
        ("power set", power_set),
        ("comprehension, F = 'v is empty'", lambda u: comprehension(u, is_empty)),
        ("replacement, F = 'w ↦ {w}'", lambda u: replacement(u, singleton_of)),
        ("infinity", infinity),
        ("foundation", foundation),
        ("choice", choice),
    ]
    print(f"   {'axiom':<34}" + "".join(f"{name:>10}" for name, _ in universes))
    for name, test in axioms:
        print(f"   {name:<34}" + "".join(f"{str(test(u)):>10}" for _, u in universes))
    print("   Each False is a set the axiom demands and the universe lacks: a pair,")
    print("   a power set, an image, an infinite set. Infinity fails in every finite")
    print("   universe, which is why it is an axiom and not a theorem.")


if __name__ == "__main__":
    main()
