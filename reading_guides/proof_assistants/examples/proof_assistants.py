#!/usr/bin/env python3
"""A proof is data a program can check: natural deduction with Isabelle's rule names.

Run:  python3 proof_assistants.py

Every other program in this library checks a claim on a model: it builds
the sets and looks. A proof assistant does something else. It is handed a
proof, a list of lines each saying which rule produced it from which earlier
lines, and it checks that every line has the shape its rule demands. It never
asks whether the claim is true; a proof that passes is the evidence. This
program is such a checker for the propositional part of Isabelle's
first-order logic, with Isabelle's own rule names (conjI, conjunct1, impI,
mp, notI, classical, ...). It accepts a proof, rejects two doctored ones at
the line that is wrong, proves the excluded middle with the one classical
step marked, and then puts the two methods side by side on a theorem from
Paulson's manual, Pow(A ∩ B) = Pow(A) ∩ Pow(B): checked on 64 pairs of sets
here, proved for all sets there.
"""

from itertools import product

# A formula is a letter ("A"), the constant "False", or a tuple built by:
FALSE = "False"


def And(p, q):
    return ("and", p, q)


def Or(p, q):
    return ("or", p, q)


def Imp(p, q):
    return ("imp", p, q)


def Not(p):
    return ("not", p)


PREC = {"not": 4, "and": 3, "or": 2, "imp": 1}
SIGN = {"and": "∧", "or": "∨", "imp": "⟶"}


def fmt(f) -> str:
    """A formula as Isabelle prints it: ∧ above ∨ above ⟶, all grouping to the right."""
    if isinstance(f, str):
        return f
    if f[0] == "not":
        inner = fmt(f[1])
        return "¬" + (inner if isinstance(f[1], str) or f[1][0] == "not" else f"({inner})")
    op, p, q = f

    def side(g, right):
        s = fmt(g)
        if isinstance(g, str) or g[0] == "not" or PREC[g[0]] > PREC[op] or (right and g[0] == op):
            return s
        return f"({s})"

    return f"{side(p, False)} {SIGN[op]} {side(q, True)}"


def sequent(hyps, phi) -> str:
    """Γ ⊢ φ: what is assumed, then what is claimed from it."""
    left = ", ".join(sorted(fmt(h) for h in hyps))
    return f"{left} ⊢ {fmt(phi)}" if left else f"⊢ {fmt(phi)}"


# ---------------------------------------------------------------------------
# The rules. Each one takes the assumptions G and formula phi of the line
# being checked, plus the (assumptions, formula) pairs of the lines it cites,
# and returns None when the shape is right or a sentence saying what is wrong.
# A premise may rest on fewer assumptions than the conclusion, never more,
# except for the one assumption a rule discharges (impI, disjE, notI,
# classical): that one is allowed in the premise and gone from the conclusion.
# ---------------------------------------------------------------------------

LEANS = "a premise rests on an assumption the conclusion does not carry"


def under(premise, G, discharged=None) -> bool:
    hyps, _ = premise
    allowed = G | ({discharged} if discharged is not None else set())
    return hyps <= allowed


def is_(f, op) -> bool:
    return isinstance(f, tuple) and f[0] == op


def r_assume(G, phi, prem):
    return None if phi in G else f"{fmt(phi)} is not among the assumptions"


def r_conjI(G, phi, prem):
    (_, p), (_, q) = prem
    if not (under(prem[0], G) and under(prem[1], G)):
        return LEANS
    return None if phi == And(p, q) else f"conjI would give {fmt(And(p, q))}"


def r_conjunct(which):
    def rule(G, phi, prem):
        [(_, pq)] = prem
        if not under(prem[0], G):
            return LEANS
        if not is_(pq, "and"):
            return "the premise is not a conjunction"
        return None if phi == pq[which] else f"conjunct{which} of {fmt(pq)} is {fmt(pq[which])}"
    return rule


def r_disjI(which):
    def rule(G, phi, prem):
        [(_, p)] = prem
        if not under(prem[0], G):
            return LEANS
        if not (is_(phi, "or") and phi[which] == p):
            return f"the conclusion must be a disjunction with {fmt(p)} on the {'left' if which == 1 else 'right'}"
        return None
    return rule


def r_disjE(G, phi, prem):
    (_, pq), left, right = prem
    if not is_(pq, "or"):
        return "the first premise is not a disjunction"
    if not (under(prem[0], G) and under(left, G, pq[1]) and under(right, G, pq[2])):
        return LEANS
    if not (left[1] == phi and right[1] == phi):
        return "both cases must conclude the same formula as this line"
    return None


def r_impI(G, phi, prem):
    [(hyps, q)] = prem
    if not is_(phi, "imp"):
        return "the conclusion is not an implication"
    p = phi[1]
    if not under(prem[0], G, p):
        return LEANS
    return None if q == phi[2] else f"impI would give {fmt(Imp(p, q))}"


def r_mp(G, phi, prem):
    (_, pq), (_, p) = prem
    if not (under(prem[0], G) and under(prem[1], G)):
        return LEANS
    if not (is_(pq, "imp") and pq[1] == p):
        return "the first premise must be an implication whose antecedent is the second"
    return None if phi == pq[2] else f"mp would give {fmt(pq[2])}"


def r_FalseE(G, phi, prem):
    [(_, f)] = prem
    if not under(prem[0], G):
        return LEANS
    return None if f == FALSE else "the premise must be False"


def r_notI(G, phi, prem):
    [(_, f)] = prem
    if not is_(phi, "not"):
        return "the conclusion is not a negation"
    if not under(prem[0], G, phi[1]):
        return LEANS
    return None if f == FALSE else "the premise must be False"


def r_notE(G, phi, prem):
    (_, np), (_, p) = prem
    if not (under(prem[0], G) and under(prem[1], G)):
        return LEANS
    return None if np == Not(p) else "the first premise must be the negation of the second"


def r_classical(G, phi, prem):
    [(_, p)] = prem
    if not under(prem[0], G, Not(phi)):
        return LEANS
    return None if p == phi else "the premise must conclude this line's formula from its negation"


RULES = {
    # name: (premises, checker, the rule as Isabelle's IFOL.thy and FOL.thy state it)
    "assume":    (0, r_assume,       "P ⟹ P                           an assumption may be claimed"),
    "conjI":     (2, r_conjI,        "⟦P; Q⟧ ⟹ P ∧ Q"),
    "conjunct1": (1, r_conjunct(1),  "P ∧ Q ⟹ P"),
    "conjunct2": (1, r_conjunct(2),  "P ∧ Q ⟹ Q"),
    "disjI1":    (1, r_disjI(1),     "P ⟹ P ∨ Q"),
    "disjI2":    (1, r_disjI(2),     "Q ⟹ P ∨ Q"),
    "disjE":     (3, r_disjE,        "⟦P ∨ Q; P ⟹ R; Q ⟹ R⟧ ⟹ R"),
    "impI":      (1, r_impI,         "(P ⟹ Q) ⟹ P ⟶ Q"),
    "mp":        (2, r_mp,           "⟦P ⟶ Q; P⟧ ⟹ Q"),
    "FalseE":    (1, r_FalseE,       "False ⟹ P"),
    "notI":      (1, r_notI,         "(P ⟹ False) ⟹ ¬P              derived: ¬P abbreviates P ⟶ False"),
    "notE":      (2, r_notE,         "⟦¬P; P⟧ ⟹ R                    derived"),
    "classical": (1, r_classical,    "(¬P ⟹ P) ⟹ P                  the one axiom FOL adds to IFOL"),
}


def check(proof) -> bool:
    """Check a proof line by line; print each line, and the first wrong one."""
    done = []
    for n, (hyps, phi, rule, cited) in enumerate(proof, 1):
        G = frozenset(hyps)
        arity, checker, _ = RULES[rule]
        tag = f"by {rule}" + (f" {cited}" if cited else "")
        line = f"   {n:>2}. {sequent(G, phi):<34} {tag}"
        if any(not 1 <= c < n for c in cited):
            print(f"{line}\n       REJECTED: a line may cite only earlier lines")
            return False
        premises = [done[c - 1] for c in cited]
        if len(premises) != arity:
            print(f"{line}\n       REJECTED: {rule} takes {arity} premise(s), {len(premises)} cited")
            return False
        problem = checker(G, phi, premises)
        if problem:
            print(f"{line}\n       REJECTED: {problem}")
            return False
        print(line)
        done.append((G, phi))
    print("   accepted: every line has the shape its rule demands")
    return True


def power(s):
    """The power set of a finite set, as a frozenset of frozensets."""
    items = sorted(s)
    return frozenset(frozenset(x for x, keep in zip(items, bits) if keep)
                     for bits in product([False, True], repeat=len(items)))


def show(s) -> str:
    if not s:
        return "{}"
    return "{" + ", ".join(show(x) if isinstance(x, frozenset) else str(x) for x in sorted(s, key=lambda v: (len(v), sorted(v)) if isinstance(v, frozenset) else (0, [v]))) + "}"


def main() -> None:
    A, B = "A", "B"
    AB = And(A, B)

    print("1. THE RULES, AS ISABELLE STATES THEM, AND A PROOF THEY ACCEPT")
    print("   ⟹ is Isabelle's 'from these, this'; ⟦P; Q⟧ lists what is needed.")
    for name, (_, _, statement) in RULES.items():
        print(f"     {name:<10} {statement}")
    print("   A proof is a list of lines: assumptions ⊢ claim, the rule, the lines it cites.")
    print("   Claim: A ∧ B ⟶ B ∧ A.")
    swap = [
        ({AB}, AB, "assume", []),
        ({AB}, B, "conjunct2", [1]),
        ({AB}, A, "conjunct1", [1]),
        ({AB}, And(B, A), "conjI", [2, 3]),
        (set(), Imp(AB, And(B, A)), "impI", [4]),
    ]
    check(swap)
    print()

    print("2. THE CHECKER CHECKS SHAPE, NOT TRUTH: TWO DOCTORED PROOFS")
    print("   The same proof with line 4 claiming B ∧ A straight from line 1:")
    doctored = list(swap)
    doctored[3] = ({AB}, And(B, A), "conjunct1", [1])
    check(doctored)
    print("   And with line 5 discharging an assumption line 4 never had:")
    doctored = list(swap)
    doctored[4] = (set(), Imp(A, And(B, A)), "impI", [4])
    check(doctored)
    print("   The second is the slip a human reader misses: the conclusion is false")
    print("   (A alone does not give B ∧ A), and only the bookkeeping of assumptions")
    print("   catches it. The checker never evaluated a single formula.")
    print()

    print("3. THE EXCLUDED MIDDLE, WITH THE ONE CLASSICAL STEP MARKED")
    print("   Claim: A ∨ ¬A. IFOL has no rule that reaches it; FOL adds 'classical'.")
    em = Or(A, Not(A))
    hyp = {Not(em)}
    excluded_middle = [
        (hyp | {A}, A, "assume", []),
        (hyp | {A}, em, "disjI1", [1]),
        (hyp | {A}, Not(em), "assume", []),
        (hyp | {A}, FALSE, "notE", [3, 2]),
        (hyp, Not(A), "notI", [4]),
        (hyp, em, "disjI2", [5]),
        (set(), em, "classical", [6]),
    ]
    check(excluded_middle)
    print("   Lines 1 to 6 are intuitionistic: from ¬(A ∨ ¬A) they reach A ∨ ¬A.")
    print("   Line 7 is the step (¬P ⟹ P) ⟹ P, which drops the assumption; without")
    print("   it the proof stops at line 6 with ¬(A ∨ ¬A) still on the left of ⊢.")
    print()

    print("4. A MODEL CHECK AND A PROOF OF THE SAME THEOREM")
    U = {1, 2, 3}
    pairs = [(frozenset(a), frozenset(b)) for a in power(U) for b in power(U)]
    good = sum(power(a & b) == power(a) & power(b) for a, b in pairs)
    print(f"   Pow(A ∩ B) = Pow(A) ∩ Pow(B) on every pair A, B ⊆ {{1, 2, 3}}: {len(pairs)} pairs, {good} true")
    bad = [(a, b) for a, b in pairs if power(a | b) != power(a) | power(b)]
    a, b = min(bad, key=lambda ab: (len(ab[0] | ab[1]), sorted(ab[0]), sorted(ab[1])))
    witness = next(iter(sorted(power(a | b) - (power(a) | power(b)), key=sorted)))
    print(f"   Pow(A ∪ B) = Pow(A) ∪ Pow(B): {len(pairs)} pairs, {len(bad)} false; the smallest")
    print(f"   counterexample is A = {show(a)}, B = {show(b)}: {show(witness)} ⊆ A ∪ B but ⊆ neither.")
    print("   That is what this library's programs do, and a counterexample is a finite")
    print("   object, so it is the right tool to find one. Paulson's manual proves the")
    print("   first law for all sets, in the proof of its section 'A proof about powersets':")
    for step, note in [
        ('lemma "Pow(A Int B) = Pow(A) Int Pow(B)"', ""),
        ("apply (rule equalityI)", "two inclusions, by extensionality"),
        ("apply (rule Int_greatest)", "⊆ of an intersection: ⊆ of each part"),
        ("apply (rule Int_lower1 [THEN Pow_mono])", "A ∩ B ⊆ A, and Pow is monotone"),
        ("apply (rule Int_lower2 [THEN Pow_mono])", "A ∩ B ⊆ B, likewise"),
        ("apply (rule subsetI)", "the other inclusion, member by member"),
        ("apply (erule IntE)", "x ∈ Pow(A) ∩ Pow(B) is two facts"),
        ("apply (rule PowI)", "x ∈ Pow(A ∩ B) is x ⊆ A ∩ B"),
        ("apply (drule PowD)+", "and the two facts are x ⊆ A, x ⊆ B"),
        ("apply (rule Int_greatest)", "so x ⊆ A ∩ B"),
        ("apply (assumption+)", "the two subgoals are assumptions"),
        ("done", ""),
    ]:
        print(f"     {step:<44} {note}")
    print("   Eleven steps, each a rule applied by shape, as in sections 1 to 3; the")
    print("   manual adds that 'by blast' finds this proof by itself. 64 pairs here,")
    print(f"   every set there. The checker above knows {len(RULES)} rules; Isabelle/ZF's")
    print("   difference is only size: more rules, quantifiers, and the seven axioms.")


if __name__ == "__main__":
    main()
