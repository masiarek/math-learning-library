#!/usr/bin/env python3
"""Reading a set expression: precedence, and the two ways to write nonsense.

Run:  python3 reading_set_expressions.py

A ∪ B ∩ C means nothing until a convention says which operation goes
first. The usual one borrows from logic, where not binds tighter than and,
and and tighter than or: complement first, then difference, then
intersection, then union, left to right among equals. Python's operators
have that same order (- before & before ^ before |), so a set expression
typed as Python means what the convention says. The program checks the
order by asking Python's own parser, evaluates a worked example both
ways, runs the two notation mistakes textbooks warn about as the Python
bugs they become, and computes (1, 2) ∪ (2, 1) under both of its meanings.
"""

import ast
from itertools import product

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
    print("   one level. The textbook order for sets is complement, difference,")
    print("   intersection, union: the same ladder, with the complement written")
    print("   U - A in Python and so taken before everything else by its brackets.")
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

    print("3. PRACTICE SETS, EVALUATED BY THE RULE")
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


if __name__ == "__main__":
    main()
