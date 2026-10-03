#!/usr/bin/env python3
"""Reading a set expression: precedence, and the two ways to write nonsense.

Run:  python3 reading_set_expressions.py

A ∪ B ∩ C means nothing until a convention says which operation goes
first. The part every source shares borrows from logic, where not binds
tighter than and, and and tighter than or: complement first, then
intersection, then union, left to right among equals. Difference has no
agreed place: Python reads it above ∩, Lean 4 level with ∩, Isabelle/HOL,
Pascal, the SQL standard and Z level with ∪, and most textbooks give it no
level and always bracket it. The program checks Python's order by asking
its own parser, evaluates a worked example both ways, runs the two
notation mistakes textbooks warn about as the Python bugs they become,
computes (1, 2) ∪ (2, 1) under both of its meanings, and reads the same
expressions under each system's precedence to show where they part.
"""

import ast
import re
from itertools import combinations, product

SYMBOL = {ast.BitOr: "|", ast.BitAnd: "&", ast.BitXor: "^", ast.Sub: "-"}


def bracketed(node) -> str:
    """Rewrite a parsed expression with every operation in brackets."""
    if isinstance(node, ast.BinOp):
        return f"({bracketed(node.left)} {SYMBOL[type(node.op)]} {bracketed(node.right)})"
    if isinstance(node, ast.Name):
        return node.id
    return ast.unparse(node)


def show(s) -> str:
    """A set, nested or not, in braces and in a stable order."""
    if not isinstance(s, (set, frozenset)):
        return str(s)
    if not s:
        return "{}"
    items = sorted(s, key=lambda v: (len(v), sorted(v)) if isinstance(v, frozenset) else (0, [v]))
    return "{" + ", ".join(show(x) for x in items) + "}"


def main() -> None:
    print("1. WHAT PYTHON'S PARSER DOES WITH AN UNBRACKETED EXPRESSION")
    for text in ["A | B & C", "A & B | C", "A - B & C", "A & B ^ C", "A ^ B | C",
                 "A - B - C", "A | B - A & C"]:
        print(f"   {text:<16} is read as  {bracketed(ast.parse(text, mode='eval').body)}")
    print("   Tighter to looser:  -  then  &  then  ^  then  |,  left to right within")
    print("   one level. The shared textbook order for sets is complement, then")
    print("   intersection, then union: the same ladder for & and |, with the")
    print("   complement written U - A in Python and so taken first by its brackets.")
    print("   Where - sits is Python's own choice; section 6 shows the others.")
    print()

    print("2. A WORKED EXAMPLE, BOTH WAYS")
    U = {1, 2, 3, 4, 5}
    c12 = U - {1, 2}
    by_rule = {5} | c12 & {2, 3}
    other = ({5} | c12) & {2, 3}
    print(f"   U = {show(U)};  {{1, 2}}′ = {show(c12)}")
    print(f"   {{5}} ∪ {{1, 2}}′ ∩ {{2, 3}}    by the rule, ∩ first:   {{5}} | c & {{2, 3}}   = {show(by_rule)}")
    print(f"   ({{5}} ∪ {{1, 2}}′) ∩ {{2, 3}}  with the other grouping: ({{5}} | c) & {{2, 3}} = {show(other)}")
    print("   Two answers from one line of symbols: the convention is not decoration.")
    print("   Many authors never rely on it and always write the brackets; do the same")
    print("   when a reader might not know the rule.")
    print()

    print("3. PRACTICE SETS, EVALUATED AS PYTHON READS THEM")
    A, B, C = {1, 3, 5, 7}, {4, 5, 6, 7}, {1, 2, 3}
    U = set(range(10))
    env = {"A": A, "B": B, "C": C, "U": U}
    print(f"   A = {show(A)}   B = {show(B)}   C = {show(C)}   U = {{0, ..., 9}}")
    for math, code in [
        ("A ∪ B", "A | B"), ("A ∩ B", "A & B"), ("A ∖ B", "A - B"), ("B ∖ A", "B - A"),
        ("A′", "U - A"), ("A △ B", "A ^ B"),
        ("A ∪ B ∩ C", "A | B & C"), ("(A ∪ B) ∩ C", "(A | B) & C"),
        ("A ∩ B ∪ C", "A & B | C"), ("A ∩ (B ∪ C)", "A & (B | C)"),
        ("A ∖ B ∖ C", "A - B - C"), ("A ∖ (B ∖ C)", "A - (B - C)"),
        ("A ∪ B ∖ A ∩ C", "A | B - A & C"), ("A′ ∩ B", "(U - A) & B"),
    ]:
        print(f"     {math:<16} {code:<14} {show(eval(code, dict(env)))}")
    print()

    print("4. THE TWO MISTAKES, AS PYTHON BUGS")
    A, B, x = {1, 2}, {2, 3}, 2
    try:
        wrong1 = repr(eval("x in A & x in B", {"x": x, "A": A, "B": B}))
    except TypeError:
        wrong1 = "TypeError"
    print(f"   x ∈ A ∩ x ∈ B  ->  x in A & x in B    : {wrong1}")
    print("     & binds tighter than 'in', so it is read as  x in (A & x) in B,  a chained")
    print("     comparison that asks for A & 2: an operation on sets given a number.")
    print(f"   x ∈ A ∧ B      ->  x in A and B       : {x in A and B!r}")
    print("     parsed as (x in A) and B, which hands back the set B, not True or False.")
    y = 1
    print(f"     with x = {y}: x in A and B = {y in A and B!r}, truthy, though {y} is not in B;")
    print("     an 'if' takes the wrong branch and nothing complains.")
    print(f"   right:  x in A and x in B = {x in A and x in B},   x in A & B = {x in A & B}")
    print("   A set goes on each side of ∩; a statement goes on each side of ∧.")
    print()

    print("5. (1, 2) ∪ (2, 1): A PAIR OR AN INTERVAL?")
    def pair(a, b):
        return frozenset({frozenset({a}), frozenset({a, b})})
    p, q = pair(1, 2), pair(2, 1)
    print(f"   as ordered pairs, (a, b) = {{{{a}}, {{a, b}}}} (Kuratowski):")
    print(f"     (1, 2) = {show(p)}   (2, 1) = {show(q)}")
    print(f"     union {show(p | q)}   intersection {show(p & q)}   (1, 2) ∖ (2, 1) = {show(p - q)}")
    grid = [k / 4 for k in range(0, 13)]
    first = {t for t in grid if 1 < t < 2}
    second = {t for t in grid if 2 < t < 1}
    print("   as open intervals, (2, 1) has no members, since no t has 2 < t < 1:")
    print(f"     on the grid 0, 0.25, ..., 3:  (1, 2) -> {sorted(first)},  (2, 1) -> {sorted(second)}")
    print("     so (1, 2) ∪ (2, 1) = (1, 2) and (1, 2) ∩ (2, 1) = ∅.")
    print("   Same symbols, two different sets: read (a, b) by its context.")
    print()

    print("6. WHERE DOES DIFFERENCE GO? THREE SYSTEMS, TWO ANSWERS")
    A, B, C = {1, 3, 5, 7}, {4, 5, 6, 7}, {1, 2, 3}
    env = {"A": A, "B": B, "C": C, "U": set(range(10))}
    print(f"   A = {show(A)}   B = {show(B)}   C = {show(C)}   U = {{0, ..., 9}}")
    print("   Python reads ∖ above ∩ (- before &). Lean 4 declares \\ and ∩ at one level,")
    print("   70, above ∪ at 65. Isabelle/HOL declares - with ∪ at 65, below ∩ at 70, as")
    print("   Pascal, the SQL standard and Z do. Ashlock and most textbooks give ∖")
    print("   no level at all and always bracket it. Same symbols, read by each:")
    for text in ["A ∪ B ∩ C", "A ∪ B ∖ C", "A ∖ B ∩ C", "A ∩ B ∖ C", "A ∖ B ∖ C", "A ∪ B ∖ A ∩ C"]:
        print(f"   {text}")
        results = [(name, *read(text, table, env)) for name, table in CONVENTIONS]
        distinct = {show(v) for _, _, v in results if v is not None}
        if len(distinct) > 1:
            verdict = f"{len(distinct)} answers"
        elif all(v is not None for _, _, v in results):
            verdict = "all agree"
        else:
            verdict = "one set, where it parses"
        for i, (name, form, value) in enumerate(results):
            tail = f"   {verdict}" if i == len(results) - 1 else ""
            shown = show(value) if value is not None else ""
            print(f"     {name:<10} {form:<22} {shown}{tail}".rstrip())
    print("   A ∩ B ∖ C is bracketed two ways and comes out the same, because")
    laws = [("A ∩ (B ∖ C) = (A ∩ B) ∖ C", lambda a, b, c: a & (b - c) == (a & b) - c),
            ("A ∪ (B ∖ C) = (A ∪ B) ∖ C", lambda a, b, c: a | (b - c) == (a | b) - c),
            ("(A ∖ B) ∩ C = A ∖ (B ∩ C)", lambda a, b, c: (a - b) & c == a - (b & c))]
    pool = [set(s) for k in range(5) for s in combinations(range(1, 5), k)]
    for name, law in laws:
        fails = sum(not law(a, b, c) for a, b, c in product(pool, repeat=3))
        if fails == 0:
            state = f"true on all {len(pool) ** 3} triples of subsets of {{1, 2, 3, 4}}"
        else:
            state = f"false on {fails} of them"
        print(f"     {name}:  {state}")
    print("   Lean refuses A ∩ B ∖ C and A ∖ B ∖ C unbracketed: its \\ is infix, not infixl,")
    print("   so a left operand must bind tighter than 70, and A ∩ B, A ∖ B are exactly 70")
    print("   (read off the declarations; Lean was not run here).")
    print("   So in value there are two conventions, not three: ∖ with ∩ (Python, Lean)")
    print("   or ∖ with ∪ (Isabelle, Pascal, SQL, Z). This page reads ∖ as Python does.")
    print()
    print("   THE PASTED ANSWER'S EXAMPLE, READ BY EACH SYSTEM")
    env = {"A": {1, 2, 3}, "B": {3, 4}, "C": {2, 5}, "D": {1, 4, 5}, "U": {1, 2, 3, 4, 5}}
    print("   U = {1, ..., 5}   A = {1, 2, 3}   B = {3, 4}   C = {2, 5}   D = {1, 4, 5}")
    for text in ["A ∖ B ∪ C ∩ D′", "A ∪ C ∖ B"]:
        print(f"   {text}")
        for name, table in CONVENTIONS:
            form, value = read(text, table, env)
            print(f"     {name:<10} {form:<22} {show(value)}")
    print("   The first is the pasted example: its ∖ is leftmost and its ∪ is lowest in")
    print("   every system, so it cannot tell the conventions apart. The second can.")


# Each operator: (what its left operand must bind at least, its own level, what its right
# operand must bind at least), higher binding tighter. In Lean's terms infixl:p is
# (p, p, p + 1) and infix:p, non-associative, is (p + 1, p, p + 1).
CONVENTIONS = [
    ("Python", {"∖": (3, 3, 4), "∩": (2, 2, 3), "∪": (1, 1, 2)}),
    ("Lean 4", {"∖": (3, 2, 3), "∩": (2, 2, 3), "∪": (1, 1, 2)}),
    ("Isabelle", {"∩": (2, 2, 3), "∖": (1, 1, 2), "∪": (1, 1, 2)}),
]
TOP = 99


def read(text: str, table: dict, env: dict) -> tuple:
    """Read a set expression under one precedence table, ′ postfix and tightest, and
    return its fully bracketed form and its value, or ("no parse", None)."""
    tokens = re.findall(r"[A-Z]|′|[∖∩∪()]", text)
    pos = 0

    def primary():
        nonlocal pos
        token = tokens[pos]
        pos += 1
        if token == "(":
            form, value, _ = expression(0)
            if pos >= len(tokens) or tokens[pos] != ")":
                raise ValueError
            pos += 1
        else:
            form, value = token, env[token]
        while pos < len(tokens) and tokens[pos] == "′":
            pos += 1
            form, value = form + "′", env["U"] - value
        return form, value, TOP

    def expression(floor):
        nonlocal pos
        form, value, level = primary()
        while pos < len(tokens) and tokens[pos] in table:
            left_min, own, right_min = table[tokens[pos]]
            if own < floor or level < left_min:
                break
            op = tokens[pos]
            pos += 1
            right_form, right, _ = expression(right_min)
            value = {"∖": value - right, "∩": value & right, "∪": value | right}[op]
            form, level = f"({form} {op} {right_form})", own
        return form, value, level

    try:
        form, value, _ = expression(0)
    except ValueError:
        return "no parse", None
    if pos < len(tokens):
        return "no parse", None
    return form, value

if __name__ == "__main__":
    main()
