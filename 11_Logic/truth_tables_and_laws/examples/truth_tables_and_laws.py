#!/usr/bin/env python3
"""Truth tables: a logic law is two columns that agree on every row.

Run:  python3 truth_tables_and_laws.py

A propositional sentence is a function from truth values of its letters
to a truth value, and a truth table lists it on every input. Two
sentences are logically equivalent when their columns agree, so every
law of propositional logic is checked, and proved, by a table with 2^n
rows. The program builds Cunningham's tables (Problems 1 to 4), checks
his whole list of logic laws, settles the exercises of section 1.2, and
shows the difference between ↔, a column, and ⇔, a claim about columns.
"""

from itertools import product

T, F = True, False


def imp(p, q):
    return (not p) or q


def iff(p, q):
    return p == q


def rows(n):
    return list(product((T, F), repeat=n))


def tv(b):
    return "T" if b else "F"


def table(letters, columns):
    """Print a truth table: letters, then each named column."""
    names = list(letters) + [name for name, _ in columns]
    width = max(len(n) for n in names)
    print("   " + "  ".join(f"{n:^{width}}" for n in names))
    for values in rows(len(letters)):
        env = dict(zip(letters, values))
        cells = [tv(v) for v in values] + [tv(f(env)) for _, f in columns]
        print("   " + "  ".join(f"{c:^{width}}" for c in cells))


def equivalent(letters, f, g):
    return all(f(dict(zip(letters, v))) == g(dict(zip(letters, v))) for v in rows(len(letters)))


def tautology(letters, f):
    return all(f(dict(zip(letters, v))) for v in rows(len(letters)))


def main() -> None:
    print("1. A TRUTH TABLE, BUILT INSIDE OUT (CUNNINGHAM, PROBLEM 1)")
    print("   ¬P → (Q ∧ P): the outside connective is →, its parts ¬P and Q ∧ P.")
    table("PQ", [("¬P", lambda e: not e["P"]),
                 ("Q∧P", lambda e: e["Q"] and e["P"]),
                 ("¬P→(Q∧P)", lambda e: imp(not e["P"], e["Q"] and e["P"]))])
    print("   → is false in one case only, T → F; the two F rows are the rows with P false.")
    print()

    print("2. TAUTOLOGY, CONTRADICTION, AND WHAT ⇔ MEANS")
    table("P", [("¬P", lambda e: not e["P"]),
                ("P∨¬P", lambda e: e["P"] or not e["P"]),
                ("P∧¬P", lambda e: e["P"] and not e["P"])])
    print("   P ∨ ¬P is true on every row: a tautology. P ∧ ¬P never: a contradiction.")
    print("   ψ ⇔ φ ('logically equivalent') means the columns of ψ and φ agree on")
    print("   every row, which is the same as saying ψ ↔ φ is a tautology. ↔ is a")
    print("   connective inside a sentence; ⇔ is a claim about two sentences.")
    dm = lambda e: not (e["P"] or e["Q"])
    dm2 = lambda e: (not e["P"]) and (not e["Q"])
    print(f"   ¬(P∨Q) ⇔ ¬P∧¬Q: columns agree: {equivalent('PQ', dm, dm2)};"
          f"   ¬(P∨Q) ↔ (¬P∧¬Q) is a tautology: {tautology('PQ', lambda e: iff(dm(e), dm2(e)))}")
    print()

    print("3. TWO SENTENCES THAT ARE NOT EQUIVALENT (PROBLEM 3): ONE ROW DECIDES")
    f = lambda e: e["P"] or (e["Q"] and not e["P"])
    g = lambda e: (e["P"] or e["Q"]) and not e["P"]
    table("PQ", [("P∨(Q∧¬P)", f), ("(P∨Q)∧¬P", g)])
    print(f"   equivalent: {equivalent('PQ', f, g)}. The brackets moved and the meaning changed.")
    print()

    print("4. CUNNINGHAM'S LOGIC LAWS, EVERY ONE CHECKED ON EVERY ROW")
    P, Q, R = (lambda e: e["P"]), (lambda e: e["Q"]), (lambda e: e["R"])
    laws = [
        ("De Morgan 1", "¬(P∨Q) ⇔ ¬P∧¬Q", lambda e: not (P(e) or Q(e)), lambda e: not P(e) and not Q(e)),
        ("De Morgan 2", "¬(P∧Q) ⇔ ¬P∨¬Q", lambda e: not (P(e) and Q(e)), lambda e: not P(e) or not Q(e)),
        ("commutative", "P∧Q ⇔ Q∧P", lambda e: P(e) and Q(e), lambda e: Q(e) and P(e)),
        ("associative", "P∨(Q∨R) ⇔ (P∨Q)∨R", lambda e: P(e) or (Q(e) or R(e)), lambda e: (P(e) or Q(e)) or R(e)),
        ("idempotent", "P∧P ⇔ P", lambda e: P(e) and P(e), P),
        ("distributive 1", "P∧(Q∨R) ⇔ (P∧Q)∨(P∧R)", lambda e: P(e) and (Q(e) or R(e)), lambda e: (P(e) and Q(e)) or (P(e) and R(e))),
        ("distributive 2", "P∨(Q∧R) ⇔ (P∨Q)∧(P∨R)", lambda e: P(e) or (Q(e) and R(e)), lambda e: (P(e) or Q(e)) and (P(e) or R(e))),
        ("double negation", "¬¬P ⇔ P", lambda e: not not P(e), P),
        ("tautology law", "P∧(Q∨¬Q) ⇔ P", lambda e: P(e) and (Q(e) or not Q(e)), P),
        ("contradiction law", "P∨(Q∧¬Q) ⇔ P", lambda e: P(e) or (Q(e) and not Q(e)), P),
        ("conditional 1", "P→Q ⇔ ¬P∨Q", lambda e: imp(P(e), Q(e)), lambda e: not P(e) or Q(e)),
        ("conditional 2", "P→Q ⇔ ¬(P∧¬Q)", lambda e: imp(P(e), Q(e)), lambda e: not (P(e) and not Q(e))),
        ("contrapositive", "P→Q ⇔ ¬Q→¬P", lambda e: imp(P(e), Q(e)), lambda e: imp(not Q(e), not P(e))),
        ("biconditional", "P↔Q ⇔ (P→Q)∧(Q→P)", lambda e: iff(P(e), Q(e)), lambda e: imp(P(e), Q(e)) and imp(Q(e), P(e))),
        ("Problem 4", "(P→R)∧(Q→R) ⇔ (P∨Q)→R", lambda e: imp(P(e), R(e)) and imp(Q(e), R(e)), lambda e: imp(P(e) or Q(e), R(e))),
    ]
    for name, text, lhs, rhs in laws:
        print(f"   {name:<18} {text:<28} rows: 8   holds: {equivalent('PQR', lhs, rhs)}")
    print("   Three letters, eight rows: a finite check that is a complete proof,")
    print("   because a law says nothing about the letters except their truth values.")
    print()

    print("5. EXERCISES 1.2")
    ex = [
        ("1", "¬(P→Q) ⇔ P∧¬Q", lambda e: not imp(P(e), Q(e)), lambda e: P(e) and not Q(e)),
        ("2", "P↔Q ⇔ (P→Q)∧(Q→P)", lambda e: iff(P(e), Q(e)), lambda e: imp(P(e), Q(e)) and imp(Q(e), P(e))),
        ("3", "P ⇔ ¬P→(Q∧¬Q)", P, lambda e: imp(not P(e), Q(e) and not Q(e))),
        ("4", "(P∨Q)∧R ⇔ (P∧R)∨(P∧Q)", lambda e: (P(e) or Q(e)) and R(e), lambda e: (P(e) and R(e)) or (P(e) and Q(e))),
        ("5", "(P→Q)∧(P→R) ⇔ P→(Q∧R)", lambda e: imp(P(e), Q(e)) and imp(P(e), R(e)), lambda e: imp(P(e), Q(e) and R(e))),
        ("6", "(P→R)∨(Q→R) ⇔ (P∧Q)→R", lambda e: imp(P(e), R(e)) or imp(Q(e), R(e)), lambda e: imp(P(e) and Q(e), R(e))),
        ("7", "P→(Q→R) ⇔ (P∧Q)→R", lambda e: imp(P(e), imp(Q(e), R(e))), lambda e: imp(P(e) and Q(e), R(e))),
        ("8", "(P→Q)→R ⇔ P→(Q→R)", lambda e: imp(imp(P(e), Q(e)), R(e)), lambda e: imp(P(e), imp(Q(e), R(e)))),
    ]
    for num, text, lhs, rhs in ex:
        ok = equivalent("PQR", lhs, rhs)
        line = f"   {num}  {text:<26} {ok}"
        if not ok:
            bad = next(v for v in rows(3) if lhs(dict(zip("PQR", v))) != rhs(dict(zip("PQR", v))))
            line += f"   differ at P, Q, R = {', '.join(tv(b) for b in bad)}"
        print(line)
    print("   Exercise 4 as printed is not a law: with P false, Q and R true, the")
    print("   left side is true and the right false; the intended right side is")
    print("   (P∧R)∨(Q∧R). Exercise 8 is the book's own example of a non-equivalence:")
    print("   → does not associate, so the brackets in P→Q→R must be written.")


if __name__ == "__main__":
    main()
