#!/usr/bin/env python3
"""Two of Lean's definitions, run: a proof is a program, and a set is a predicate.

Run:  python3 propositions_as_types.py

Lean checks a proof the way a compiler checks a program: a proposition is a
type, a proof is a value of that type, and "is this proof correct?" is the
question "does this term have that type?". Its core file Init/Prelude.lean
defines And as a structure with two fields (a pair), Or as an inductive type
with two constructors (inl, inr), Not a as the function type a -> False, and
False as a type with no constructors at all. Mathlib defines Set α as the
function type α -> Prop: a set is its membership test.

This program builds a small type checker for exactly those definitions.
Section 1 writes three theorems as programs and type-checks them. Section 2
runs the proof of A ∧ B -> B ∧ A as the program it is: it swaps a pair.
Section 3 rejects two wrong "proofs" at the step that is wrong. Section 4
asks why False has no proof. Section 5 treats sets as predicates on a
four-element type and checks the laws of set algebra by extensionality,
the way Lean's Set.ext does. The checker is a model of Lean's, not Lean:
no dependent types, no universes, no tactics, and no claim to completeness.
"""

# ---- propositions (types) -------------------------------------------------
# A proposition is a letter ("A"), FALSE, or a tuple built by these three.
FALSE = ("False",)


def And(a, b):
    return ("And", a, b)


def Or(a, b):
    return ("Or", a, b)


def Imp(a, b):
    return ("->", a, b)


def Not(a):
    return Imp(a, FALSE)  # Lean: def Not (a : Prop) : Prop := a → False


def show(p) -> str:
    if isinstance(p, str):
        return p
    if p == FALSE:
        return "False"
    op, a, b = p
    if op == "->" and b == FALSE:
        return "¬" + show(a)
    sym = {"And": " ∧ ", "Or": " ∨ ", "->": " → "}[op]
    return "(" + show(a) + sym + show(b) + ")"


# ---- proof terms (programs) ----------------------------------------------
# ("var", name)                    a hypothesis in scope
# ("fun", name, type, body)        fun (h : type) => body        proves type -> B
# ("app", f, x)                    f x                            modus ponens
# ("And.intro", l, r)              ⟨l, r⟩                        proves A ∧ B
# ("And.left", h) / ("And.right", h)
# ("Or.inl", x, B) / ("Or.inr", A, y)                          proves A ∨ B
# ("Or.elim", h, f, g)             cases on h with f : A → C, g : B → C
# ("False.elim", h, C)             anything follows from a proof of False


class TypeError_(Exception):
    pass


def infer(term, ctx):
    """The type of `term` under hypotheses `ctx`, or raise with the reason."""
    kind = term[0]
    if kind == "var":
        if term[1] not in ctx:
            raise TypeError_(f"unknown hypothesis {term[1]}")
        return ctx[term[1]]
    if kind == "fun":
        _, name, ty, body = term
        return Imp(ty, infer(body, {**ctx, name: ty}))
    if kind == "app":
        f, x = infer(term[1], ctx), infer(term[2], ctx)
        if not (isinstance(f, tuple) and f[0] == "->"):
            raise TypeError_(f"{show(f)} is not a function type, cannot apply it")
        if f[1] != x:
            raise TypeError_(f"function wants {show(f[1])}, argument has type {show(x)}")
        return f[2]
    if kind == "And.intro":
        return And(infer(term[1], ctx), infer(term[2], ctx))
    if kind in ("And.left", "And.right"):
        h = infer(term[1], ctx)
        if not (isinstance(h, tuple) and h[0] == "And"):
            raise TypeError_(f"{kind} needs a conjunction, got {show(h)}")
        return h[1] if kind == "And.left" else h[2]
    if kind == "Or.inl":
        return Or(infer(term[1], ctx), term[2])
    if kind == "Or.inr":
        return Or(term[1], infer(term[2], ctx))
    if kind == "Or.elim":
        h, f, g = (infer(t, ctx) for t in term[1:])
        if not (isinstance(h, tuple) and h[0] == "Or"):
            raise TypeError_(f"Or.elim needs a disjunction, got {show(h)}")
        if f[:2] != ("->", h[1]) or g[:2] != ("->", h[2]) or f[2] != g[2]:
            raise TypeError_("the two branches must take the two sides and agree on the result")
        return f[2]
    if kind == "False.elim":
        h = infer(term[1], ctx)
        if h != FALSE:
            raise TypeError_(f"False.elim needs a proof of False, got {show(h)}")
        return term[2]
    raise TypeError_(f"unknown term {kind}")


def check(name, claim, term):
    try:
        got = infer(term, {})
    except TypeError_ as e:
        print(f"   {name}: REJECTED  ({e})")
        return False
    ok = got == claim
    print(f"   {name}: {'accepted' if ok else 'REJECTED'}  the term has type {show(got)}")
    return ok


# ---- running a proof as a program ---------------------------------------
def run(term, env):
    """Evaluate a proof term on data: And is a pair, Or a tagged value, fun a closure."""
    kind = term[0]
    if kind == "var":
        return env[term[1]]
    if kind == "fun":
        return lambda v: run(term[3], {**env, term[1]: v})
    if kind == "app":
        return run(term[1], env)(run(term[2], env))
    if kind == "And.intro":
        return (run(term[1], env), run(term[2], env))
    if kind == "And.left":
        return run(term[1], env)[0]
    if kind == "And.right":
        return run(term[1], env)[1]
    if kind == "Or.inl":
        return ("inl", run(term[1], env))
    if kind == "Or.inr":
        return ("inr", run(term[2], env))
    if kind == "Or.elim":
        tag, v = run(term[1], env)
        return run(term[2] if tag == "inl" else term[3], env)(v)
    raise ValueError(kind)


# ---- sets as predicates ----------------------------------------------------
# Mathlib: def Set (α : Type u) := α → Prop ; a ∈ s is s a.
U = ("a", "b", "c", "d")  # the type α, four inhabitants


def mem(s, x):
    return s(x)


def union(s, t):
    return lambda x: s(x) or t(x)  # x ∈ s ∪ t ↔ x ∈ s ∨ x ∈ t


def inter(s, t):
    return lambda x: s(x) and t(x)


def compl(s):
    return lambda x: not s(x)  # ¬(x ∈ s), i.e. s x → False


def ext_equal(s, t):
    """Set.ext: s = t when ∀ x, x ∈ s ↔ x ∈ t. On a finite type, a loop."""
    return all(mem(s, x) == mem(t, x) for x in U)


def as_braces(s):
    return "{" + ", ".join(x for x in U if s(x)) + "}"


def main():
    A, B, C = "A", "B", "C"
    h = lambda n: ("var", n)

    print("1. THREE THEOREMS WRITTEN AS PROGRAMS, THEN TYPE-CHECKED")
    print("   Lean: a proposition is a type, a proof is a term of that type.")
    swap = ("fun", "h", And(A, B), ("And.intro", ("And.right", h("h")), ("And.left", h("h"))))
    print(f"   theorem and_swap : {show(Imp(And(A, B), And(B, A)))}")
    print("     fun h => ⟨h.right, h.left⟩")
    check("and_swap", Imp(And(A, B), And(B, A)), swap)
    k = ("fun", "a", A, ("fun", "b", B, h("a")))
    print(f"   theorem const : {show(Imp(A, Imp(B, A)))}")
    print("     fun a => fun b => a")
    check("const", Imp(A, Imp(B, A)), k)
    # ¬(A ∨ B) → ¬A ∧ ¬B : from h : (A ∨ B) → False build two functions
    dm = ("fun", "h", Not(Or(A, B)), ("And.intro",
          ("fun", "a", A, ("app", h("h"), ("Or.inl", h("a"), B))),
          ("fun", "b", B, ("app", h("h"), ("Or.inr", A, h("b"))))))
    print(f"   theorem de_morgan : {show(Imp(Not(Or(A, B)), And(Not(A), Not(B))))}")
    print("     fun h => ⟨fun a => h (Or.inl a), fun b => h (Or.inr b)⟩")
    check("de_morgan", Imp(Not(Or(A, B)), And(Not(A), Not(B))), dm)
    print("   ¬A is the function type A → False, so a proof of ¬A is a function")
    print("   that would turn any proof of A into a proof of False.")
    print()

    print("2. THE PROOF OF A ∧ B → B ∧ A, RUN AS THE PROGRAM IT IS")
    prog = run(swap, {})
    for pair in [(1, "one"), ("x", "y")]:
        print(f"   and_swap applied to {pair!r} gives {prog(pair)!r}")
    print("   And.intro builds a pair, And.left and And.right take it apart:")
    print("   the proof is the swap function. Lean erases such programs at")
    print("   run time (Prop is proof-irrelevant), but the type checker ran them.")
    print()

    print("3. TWO WRONG PROOFS, REJECTED AT THE STEP THAT IS WRONG")
    wrong1 = ("fun", "h", And(A, B), ("And.intro", ("And.left", h("h")), ("And.left", h("h"))))
    print("   fun h => ⟨h.left, h.left⟩  offered for A ∧ B → B ∧ A")
    check("wrong1", Imp(And(A, B), And(B, A)), wrong1)
    wrong2 = ("fun", "h", Or(A, B), ("And.left", h("h")))
    print("   fun h => h.left  offered for A ∨ B → A")
    check("wrong2", Imp(Or(A, B), A), wrong2)
    print("   The first is a well-typed program that proves the wrong theorem;")
    print("   the second is not a program at all. Lean reports both as type errors.")
    print()

    print("4. WHY False HAS NO PROOF")
    print("   False is an inductive type with no constructors, so no closed term")
    print("   has type False; the checker above can only reach False by applying")
    print("   a hypothesis of type ¬A to a proof of A. The one rule about False,")
    print("   False.elim, says a proof of it would prove anything:")
    explode = ("fun", "f", FALSE, ("False.elim", h("f"), C))
    check("ex_falso", Imp(FALSE, C), explode)
    print()

    print("5. A SET IS A PREDICATE: Mathlib's  def Set (α : Type u) := α → Prop")
    s = lambda x: x in ("a", "b")
    t = lambda x: x in ("b", "c")
    print(f"   α = {{{', '.join(U)}}}   s = {as_braces(s)}   t = {as_braces(t)}")
    print(f"   b ∈ s is the application s b = {mem(s, 'b')};  d ∈ s is s d = {mem(s, 'd')}")
    print(f"   s ∪ t = {as_braces(union(s, t))}  (x ∈ s ∨ x ∈ t)")
    print(f"   s ∩ t = {as_braces(inter(s, t))}      (x ∈ s ∧ x ∈ t)")
    print(f"   sᶜ    = {as_braces(compl(s))}  (x ∈ s → False)")
    print("   Laws checked by Set.ext, that is by ∀ x, x ∈ lhs ↔ x ∈ rhs:")
    laws = [
        ("(s ∪ t)ᶜ = sᶜ ∩ tᶜ", compl(union(s, t)), inter(compl(s), compl(t))),
        ("(s ∩ t)ᶜ = sᶜ ∪ tᶜ", compl(inter(s, t)), union(compl(s), compl(t))),
        ("s ∩ (s ∪ t) = s", inter(s, union(s, t)), s),
        ("(sᶜ)ᶜ = s", compl(compl(s)), s),
        ("s ∪ t = s ∩ t  (false)", union(s, t), inter(s, t)),
    ]
    for name, lhs, rhs in laws:
        print(f"     {name:28} {ext_equal(lhs, rhs)}")
    print("   Each law is a law of logic read through the arrow: De Morgan for sets")
    print("   is De Morgan for ∨ and ∧, which section 1 proved as a program.")


if __name__ == "__main__":
    main()
