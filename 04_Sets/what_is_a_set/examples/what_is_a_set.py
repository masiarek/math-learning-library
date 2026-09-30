#!/usr/bin/env python3
"""What is a set? Test the textbook definition against programs that run.

Run:  python3 what_is_a_set.py

The usual first definition: "a set is a well-defined collection of distinct
objects; well-defined means there is a rule that decides whether a given
object is an element." The program checks the three things that definition
leans on and does not say. Equality: a set is nothing but its membership,
which is what makes {2, 5} = {5, 2} and the empty set unique. Well-defined
is not the same as decidable: a rule can be sharp while nobody knows its
answer. And a sharp rule is not enough: Russell's rule "x is not a member of
itself" gets no answer about itself, and the repair, cutting rules out of a
set already in hand, turns the paradox into a theorem checked here on every
small universe.
"""

from itertools import product


def divisor_sum(n: int) -> int:
    """Sum of the divisors of n smaller than n."""
    total = 1 if n > 1 else 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            total += d
            if d != n // d:
                total += n // d
        d += 1
    return total


def main() -> None:
    print("1. A SET IS ITS MEMBERSHIP AND NOTHING ELSE")
    print(f"   {{2, 5}} == {{5, 2}}             is {({2, 5} == {5, 2})}     order is not recorded")
    print(f"   {{1, 1, 2}} == {{1, 2}}          is {({1, 1, 2} == {1, 2})}     repeats are not recorded")
    print(f"   len({{1, 1, 2}})                = {len({1, 1, 2})}")
    squares = {n * n for n in range(-3, 4)}
    print(f"   {{n*n for n in -3..3}}          = {sorted(squares)}   7 rules applied, 4 members")
    print("   'Distinct' is not a demand on whoever writes the list. It is")
    print("   the rule for equality: same members, same set (extensionality).")
    print()

    print("2. THEREFORE THERE IS ONE EMPTY SET, NOT MANY")
    rules = {
        "n in 0..99 with n*n < 0": {n for n in range(100) if n * n < 0},
        "n in 0..99, even and odd": {n for n in range(100) if n % 2 == 0 and n % 2 == 1},
        "n in 0..99 with n > n": {n for n in range(100) if n > n},
        "words of 'set' longer than 3": {w for w in ["set"] if len(w) > 3},
    }
    for text, s in rules.items():
        print(f"   {'{' + text + '}':<32}  = {s}")
    empties = list(rules.values())
    print(f"   all four equal:  {all(s == empties[0] for s in empties)}")
    print("   Four rules, one set. 'THE empty set' is justified only by the")
    print("   equality rule of section 1, which the textbook definition omits.")
    print()

    print("3. WELL-DEFINED IS NOT THE SAME AS KNOWN")
    print("   P = { n : n is odd and n equals the sum of its smaller divisors }")
    print("   The rule is sharp: for any n, adding up divisors settles it.")
    even_perfect = [n for n in range(2, 10_000) if divisor_sum(n) == n]
    odd_hits = [n for n in range(1, 100_000, 2) if n > 1 and divisor_sum(n) == n]
    print(f"   even n below 10,000 that pass the test:  {even_perfect}")
    print(f"   odd n below 100,000 that pass the test:  {odd_hits}")
    print("   Is P empty? Nobody knows; it is the odd perfect number problem,")
    print("   open since antiquity. Every n has an answer; the set as a whole")
    print("   does not have a known one. Well-defined means the first, not the second.")
    print()

    print("4. A SHARP RULE THAT DECIDES NOTHING: RUSSELL")
    print("   Model a set as its rule: a function that answers 'is x a member?'.")
    print("   Rules can be asked about rules, so a set may contain sets.")

    def everything(x):
        return True

    def nothing(x):
        return False

    def russell(x):
        return not x(x)

    for name, s in [("everything", everything), ("nothing", nothing)]:
        print(f"   {name + '(' + name + ')':<22} = {s(s)!s:<6}   {'russell(' + name + ')':<19} = {russell(s)}")
    try:
        answer = repr(russell(russell))
    except RecursionError:
        answer = "no answer: RecursionError, the rule asks itself forever"
    print(f"   russell(russell)       = {answer}")
    print("   And no answer could be right:")
    for guess in (True, False):
        print(f"     if russell(russell) were {guess!s:<5}, the rule says it is {not guess}")
    print("   The rule 'x is not a member of itself' is perfectly well-defined")
    print("   on every x, and still there is no set it describes.")
    print()

    print("5. THE REPAIR: CUT A RULE OUT OF A SET YOU ALREADY HAVE")
    print("   In a universe U, membership is a table: x in y is True or False.")
    print("   R = { x in U : x not in x }. Is R one of the members of U?")
    n = 3
    objects = range(n)
    cells = [(x, y) for x in objects for y in objects]
    universes = 0
    missing = 0
    for bits in product((False, True), repeat=len(cells)):
        member = dict(zip(cells, bits))
        universes += 1
        R = frozenset(x for x in objects if not member[(x, x)])
        extensions = [frozenset(x for x in objects if member[(x, y)]) for y in objects]
        if R not in extensions:
            missing += 1
    print(f"   every membership table on {n} objects: {universes} universes")
    print(f"   universes where R is none of the {n} objects:  {missing} of {universes}")
    print("   Why always: if R were object y, ask whether y is in y. The table")
    print("   and the rule for R give opposite answers at that one cell.")
    print("   So no universe contains every set. Russell's paradox, restricted")
    print("   to a set already in hand, stops being a contradiction and becomes")
    print("   a theorem; it is Cantor's diagonal from the cardinality lesson.")
    print()

    print("6. PYTHON BUILDS SETS FROM THE BOTTOM UP, SO IT NEVER MEETS RUSSELL")
    s = set()
    try:
        s.add(s)
        added = "added"
    except TypeError as e:
        added = f"TypeError: {e}"
    print(f"   s = set(); s.add(s)   ->  {added}")
    a = frozenset()
    b = frozenset({a})
    c = frozenset({a, b})
    print(f"   frozensets from nothing:  {len(a)}, {len(b)}, {len(c)} members;  c contains b: {b in c}")
    print("   A frozenset can hold only sets that existed before it, so none")
    print("   contains itself and 'x not in x' is true of every one of them.")
    print("   That is the axiomatic answer too: sets are built in stages.")

    print()

    print("7. THE BOX PICTURE: WHERE IT HELPS AND WHERE IT MISLEADS")
    empty = frozenset()
    box_of_empty = frozenset({empty})
    print(f"   an empty box is not nothing:  len(∅) = {len(empty)},  len({{∅}}) = {len(box_of_empty)},"
          f"  ∅ == {{∅}} is {empty == box_of_empty}")
    one = 1
    inner = frozenset({one})
    outer = frozenset({inner})
    print(f"   ∈ looks one level down only:  1 ∈ {{1}} is {one in inner},  {{1}} ∈ {{{{1}}}} is {inner in outer},"
          f"  1 ∈ {{{{1}}}} is {one in outer}")
    print("     a thing inside a box inside a box is 'in' the big box; a member of a")
    print("     member is not a member. ∈ is not transitive; ⊆ is.")
    A, B = frozenset({1, 2}), frozenset({1, 3})
    print(f"   one object, two sets at once:  A = {{1, 2}}, B = {{1, 3}},  1 ∈ A and 1 ∈ B is {1 in A and 1 in B}")
    print("     a real object sits in one box; an element can be in any number of sets.")
    print(f"   two copies are one element:  {{1, 1}} == {{1}} is {frozenset([1, 1]) == frozenset([1])}")
    print("     a box can hold two identical marbles; a set cannot tell them apart.")
    print("   So the box is a good picture of ∅ versus {∅}, and a bad one of")
    print("   membership: take it for the first and drop it for the other three.")

    print()

    print("8. CAN WE DENY 'C IS EITHER ORDINARY OR NOT'? TRY IT IN OTHER LOGICS")
    from fractions import Fraction as Fr
    half = Fr(1, 2)

    def kleene():
        vals = [Fr(0), half, Fr(1)]
        neg = lambda a: 1 - a
        imp = lambda a, b: max(1 - a, b)
        return "Kleene K3", vals, neg, imp

    def godel(n):
        vals = [Fr(i, n - 1) for i in range(n)]
        imp = lambda a, b: Fr(1) if a <= b else b
        neg = lambda a: imp(a, Fr(0))
        return f"Godel G{n}", vals, neg, imp

    def lukasiewicz(n):
        vals = [Fr(i, n - 1) for i in range(n)]
        imp = lambda a, b: min(Fr(1), 1 - a + b)
        neg = lambda a: 1 - a
        return f"Lukasiewicz L{n}", vals, neg, imp

    def iff(imp, a, b):
        return min(imp(a, b), imp(b, a))

    print("   P stands for 'C ∈ C'. The definition of C says P ↔ ¬P must be TRUE.")
    print("   Truth values run from 0 (false) to 1 (true); only 1 counts as true.")
    print(f"   {'logic':<16} {'P or not P always true?':<25} values of P that satisfy P ↔ ¬P")
    logics = [("classical", [Fr(0), Fr(1)], lambda a: 1 - a, lambda a, b: max(1 - a, b)),
              kleene(), godel(3), godel(5), lukasiewicz(3), lukasiewicz(5)]
    for name, vals, neg, imp in logics:
        lem = all(max(v, neg(v)) == 1 for v in vals)
        fixed = [str(v) for v in vals if iff(imp, v, neg(v)) == 1]
        print(f"   {name:<16} {('yes' if lem else 'no'):<25} {', '.join(fixed) if fixed else 'none: still a paradox'}")
    print("   Excluded middle fails in K3 and in the Godel logics, and C still has no")
    print("   truth value there: the paradox never needed statement 4. Only Lukasiewicz")
    print("   logic has a 'half true' that solves it. Then Curry's version bites:")
    print("   C_k = {x : x ∈ x → (x ∈ x → ... → false)}, with k arrows.")
    for n in (3, 4, 5, 6):
        name, vals, neg, imp = lukasiewicz(n)
        dead = []
        for k in range(1, 7):
            def curry(v, k=k):
                r = Fr(0)
                for _ in range(k):
                    r = imp(v, r)
                return r
            if not [v for v in vals if iff(imp, v, curry(v)) == 1]:
                dead.append(k)
        print(f"   {name:<16} no value for C_k ∈ C_k when k = {', '.join(map(str, dead))}")
    print("   The fixed point of C_k is k/(k+1), and a logic with finitely many values")
    print("   always misses one. Every finite-valued repair meets a paradox it cannot")
    print("   value; set theory instead keeps the logic and denies that C exists.")


if __name__ == "__main__":
    main()
