#!/usr/bin/env python3
"""Cardinality: the size of a set, defined by matching rather than counting.

Run:  python3 cardinality.py

|A| is the number of members of A. For a finite set that is a count. The
definition that survives infinite sets is a MATCHING: |A| = |B| when the
members of A can be paired off with the members of B, one to one, nothing
left over on either side. The program checks that the two agree on finite
sets, shows what matching says about infinite ones, and then follows the
word into the places a programmer meets it: the values of a type, the
distinct values in a column, and the count of rows on each side of a foreign key, and the reason there
are more functions than programs.
"""

import math
from itertools import combinations, permutations, product


def matched(A: frozenset, B: frozenset, pairing: dict) -> bool:
    """Is `pairing` a one-to-one matching of all of A onto all of B?"""
    return (
        set(pairing) == set(A)
        and set(pairing.values()) == set(B)
        and len(set(pairing.values())) == len(pairing)
    )


def main() -> None:
    print("1. COUNTING AND MATCHING AGREE ON FINITE SETS")
    C = frozenset({"pawn", "rook", "knight", "bishop"})
    D = frozenset({"north", "south", "east", "west"})
    pairing = dict(zip(sorted(C), sorted(D)))
    print(f"   C = {sorted(C)}")
    print(f"   D = {sorted(D)}")
    print(f"   |C| = {len(C)}, |D| = {len(D)}")
    for c, d in pairing.items():
        print(f"     {c:<7} <-> {d}")
    print(f"   one-to-one, nothing left over:  {matched(C, D, pairing)}")
    E = frozenset({"north", "south", "east"})
    print(f"   can C match {sorted(E)}?  every pairing leaves one of C over,")
    print(f"   because |C| = {len(C)} and |E| = {len(E)}.")
    print()

    print("2. THE BARS MEAN SIZE, AND SIZE DEPENDS ON THE KIND OF THING")
    print(f"   |-4|          = {abs(-4)}           absolute value of a number")
    print(f"   |{{-4}}|        = {len({-4})}           cardinality of a one-member set")
    print(f"   |{{-4, 4}}|     = {len({-4, 4})}           cardinality of a two-member set")
    print(f"   |{{1, 1, 1}}|   = {len({1, 1, 1})}           a set does not count repeats")
    print()

    print("3. THE PRODUCT RULE  |A x B| = |A| . |B|,  READ AS TYPES")
    A = frozenset(range(4))
    B = frozenset("abcdefg")
    AB = frozenset(product(A, B))
    print(f"   |A| = {len(A)}, |B| = {len(B)}, |A x B| = {len(AB)} = {len(A)} x {len(B)}")
    print("   A type is a set of values, so it has a cardinality, and the type")
    print("   constructors follow the set rules. Build each one and count it:")
    Bool = frozenset({False, True})
    U2 = frozenset(range(4))                 # a 2-bit unsigned int, small enough to enumerate
    Unit = frozenset({()})                   # one value, like Python's None or Rust's ()
    Void = frozenset()                       # no value at all
    pair = frozenset(product(Bool, U2))      # (bool, u2)
    tagged = frozenset({("L", b) for b in Bool} | {("R", u) for u in U2})   # bool | u2
    optional = frozenset(U2 | {None})        # Optional[u2]
    funcs = frozenset(product(Bool, repeat=len(U2)))   # u2 -> bool, as truth tables
    print(f"     {'type':<16} {'built as':<28} {'count':>5}   rule")
    print(f"     {'void':<16} {'no values':<28} {len(Void):>5}   0")
    print(f"     {'unit / None':<16} {'one value':<28} {len(Unit):>5}   1")
    print(f"     {'bool':<16} {'{False, True}':<28} {len(Bool):>5}   2")
    print(f"     {'u2':<16} {'{0, 1, 2, 3}':<28} {len(U2):>5}   2^2")
    print(f"     {'(bool, u2)':<16} {'every pair':<28} {len(pair):>5}   2 x 4    product type")
    print(f"     {'bool | u2':<16} {'tagged L or R':<28} {len(tagged):>5}   2 + 4    sum type")
    print(f"     {'Optional[u2]':<16} {'u2 or None':<28} {len(optional):>5}   4 + 1    sum with unit")
    print(f"     {'u2 -> bool':<16} {'every truth table':<28} {len(funcs):>5}   2^4      function type")
    print("   Sizes a programmer already knows come from the same rules:")
    u8, u16 = 2**8, 2**16
    print(f"     uint8                {u8:>12,}   2^8")
    print(f"     (uint8, uint8)       {u8 * u8:>12,}   256 x 256, the same count as uint16 = {u16:,}")
    print(f"     (bool, uint8)        {2 * u8:>12,}   2 x 256")
    print(f"     bool | uint8         {2 + u8:>12,}   2 + 256")
    print(f"     Optional[uint8]      {1 + u8:>12,}   1 + 256: one more than uint8, and a")
    print(f"                                        uint8 cannot hold it, which is why -1")
    print(f"                                        as 'no value' is a bug waiting to happen")
    print(f"     uint8 -> bool        {2 ** u8:>12.3e}   2^256")
    print("   The algebra of sets is the algebra of types. Distributivity, checked:")
    left = frozenset(product(tagged, Bool))                       # (bool | u2) x bool
    right = frozenset({("L", p) for p in product(Bool, Bool)} | {("R", p) for p in product(U2, Bool)})
    bb = len(frozenset(product(Bool, Bool)))
    ub = len(frozenset(product(U2, Bool)))
    print(f"     |(bool | u2) x bool| = {len(left)} = |bool x bool| + |u2 x bool| = {bb} + {ub} = {len(right)}")
    print("   And it is why an exhaustive match on (bool, u2) needs 8 arms, a")
    print("   match on bool | u2 needs 6, and a fuzzer that tries every")
    print("   (uint8, uint8) input has exactly 65,536 cases to run.")
    print()

    print("4. CARDINALITY OF A COLUMN")
    rows = [
        ("ann", "PL", "admin"), ("bob", "US", "user"), ("cy", "PL", "user"),
        ("dee", "DE", "user"), ("eli", "US", "user"), ("fay", "PL", "admin"),
        ("gus", "US", "user"), ("hal", "FR", "user"), ("ida", "PL", "user"),
        ("jo", "US", "user"), ("kim", "DE", "user"), ("lou", "PL", "user"),
    ]
    print(f"   a table of {len(rows)} rows:   name   country   role")
    for i, col in enumerate(("name", "country", "role")):
        values = {r[i] for r in rows}
        shown = ", ".join(sorted(values)[:6]) + (", ..." if len(values) > 6 else "")
        print(f"     COUNT(DISTINCT {col}){' ' * (8 - len(col))} = {len(values):>2}   = |{{{shown}}}|")
    print("   A query planner keeps these numbers. An index on `name` narrows")
    print("   a lookup to 1 row; an index on `role` narrows it to 10. The")
    print("   cardinality of the column is what decides whether the index is")
    print("   worth reading.")
    countries = {r[1] for r in rows}
    roles = {r[2] for r in rows}
    combos = {(r[1], r[2]) for r in rows}
    print(f"   an index on (country, role) can hold at most |country| x |role|")
    print(f"   = {len(countries)} x {len(roles)} = {len(countries) * len(roles)} distinct keys; this table uses {len(combos)} of them.")
    print("   The product rule again: the key space of a compound index is a")
    print("   Cartesian product, and its cardinality is the product of the parts.")
    print()

    print("5. CARDINALITY OF A RELATIONSHIP: HOW MANY ROWS ON EACH SIDE")
    kna1 = {"C001", "C002", "C003", "C004"}          # customers: the check table
    vbrk = {                                          # invoices: the foreign key table
        "INV1": "C001", "INV2": "C001", "INV3": "C002", "INV4": "C001", "INV5": "C004",
    }
    print("   KNA1 (customers)  = " + ", ".join(sorted(kna1)))
    print("   VBRK (invoices)   = " + ", ".join(f"{k}->{v}" for k, v in sorted(vbrk.items())))
    per_invoice = {inv: sum(1 for c in kna1 if c == cust) for inv, cust in vbrk.items()}
    per_customer = {c: sum(1 for cust in vbrk.values() if cust == c) for c in kna1}
    print(f"   customers per invoice:  {sorted(set(per_invoice.values()))}   every invoice names exactly one customer")
    print(f"   invoices per customer:  {sorted(set(per_customer.values()))}   a customer has 0, 1 or many")
    lhs = "1" if set(per_invoice.values()) == {1} else "C"
    counts = set(per_customer.values())
    rhs = "1" if counts == {1} else "C" if counts <= {0, 1} else "N" if 0 not in counts else "CN"
    print(f"   SE11 notation, check table first:        {lhs}:{rhs}")
    ddl = {"1": "1", "C": "0..1", "N": "1..*", "CN": "0..*"}
    print(f"   DDL notation, foreign key table first:   [{ddl[rhs]},{ddl[lhs]}]")
    print("   Same relationship, the two sides written in opposite orders. The")
    print("   numbers are cardinalities of sets: |{customers of INV1}| = 1 and")
    print("   |{invoices of C001}| = 3, and the notation records the range.")
    print()

    print("6. MATCHING WORKS WHERE COUNTING STOPS: N AND THE EVEN NUMBERS")
    print("   Pair n with 2n. The first few pairs, and the rule for all of them:")
    print("     " + "  ".join(f"{n}<->{2 * n}" for n in range(10)) + "  ...   n <-> 2n")
    N = 100_000
    hit = {2 * n for n in range(N)}
    print(f"   in the first {N:,} pairs, every even number below {2 * N:,} is hit")
    print(f"   exactly once:  {hit == set(range(0, 2 * N, 2))}")
    print("   The rule never runs out on either side, so by the matching")
    print("   definition |N| = |even numbers|, though one is a proper part of")
    print("   the other. Counting has no opinion here; it never finishes.")
    print()

    print("7. AND MATCHING CAN FAIL: THE DIAGONAL")
    print("   Suppose someone claims to have listed EVERY infinite 0/1 sequence,")
    print("   row 0, row 1, row 2, ... Here are 8 rows of such a list:")
    n = 8
    table = [[(r * c + r + c) % 2 for c in range(n)] for r in range(n)]
    table[3] = [1, 1, 0, 0, 1, 1, 0, 0]
    table[6] = [0, 1, 1, 0, 1, 0, 0, 1]
    for r, row in enumerate(table):
        cells = " ".join(f"[{b}]" if c == r else f" {b} " for c, b in enumerate(row))
        print(f"     row {r}:  {cells}".rstrip())
    diag = [table[r][r] for r in range(n)]
    flipped = [1 - b for b in diag]
    print(f"     diagonal:        {' '.join(f' {b} ' for b in diag)}".rstrip())
    print(f"     flipped:         {' '.join(f' {b} ' for b in flipped)}".rstrip())
    differs = [flipped[r] != table[r][r] for r in range(n)]
    print(f"   the flipped diagonal differs from row r in column r, for every r:")
    print(f"   {differs}")
    print("   So it is a 0/1 sequence that is on no row of the list. Whatever")
    print("   list is offered, this builds a sequence it missed. No matching of")
    print("   N onto the set of 0/1 sequences exists: that set is UNCOUNTABLE.")
    print()

    print("8. WHY A PROGRAMMER SHOULD CARE: MORE FUNCTIONS THAN PROGRAMS")
    print("   A program is a finite string over a finite alphabet. Those can be")
    print("   listed, shortest first, alphabetically within a length:")
    alphabet = "ab"
    listing = []
    length = 1
    while len(listing) < 14:
        for s_ in product(alphabet, repeat=length):
            listing.append("".join(s_))
        length += 1
    print("     " + "  ".join(listing[:14]) + "  ...")
    print(f"   over a {len(alphabet)}-letter alphabet there are {len(alphabet)}^L strings of length L, so")
    print("   every string has a finite position in the list, and |programs| = |N|.")
    print("   (A real alphabet has 128 or 256 letters, which changes the count")
    print("   per length and nothing else.)")
    print()
    print("   A function from N to {0, 1} is an infinite 0/1 sequence, and section")
    print("   7 showed those cannot be listed. The same diagonal works for N -> N:")
    print("   given any list of functions g_0, g_1, g_2, ..., define")
    print("     d(n) = g_n(n) + 1")
    gs = [lambda n: n, lambda n: 2 * n, lambda n: n * n, lambda n: 7, lambda n: n % 3, lambda n: 100 - n]
    d = [gs[n](n) + 1 for n in range(len(gs))]
    print(f"     g_0..g_5 at their own index:  {[gs[n](n) for n in range(len(gs))]}")
    print(f"     d at those points:            {d}")
    print(f"     d differs from every g_n at n: {all(d[n] != gs[n](n) for n in range(len(gs)))}")
    print("   d is a perfectly good function from N to N and it is on no list,")
    print("   so |N -> N| > |N| = |programs|. Some functions have no program.")
    print()
    print("   How many is 'some'? Every program computes at most one function,")
    print("   so the computable functions are at most countable. The functions")
    print("   N -> {0, 1} match the subsets of N, and Cantor's theorem says")
    print("   |P(N)| > |N|. Almost every function, in the cardinality sense, is")
    print("   uncomputable; the ones we can compute are the rare exceptions.")
    print("   This argument names no specific function. The halting problem is")
    print("   the famous named example, but counting gets there first.")
    print()

    print("9. COMBINATORICS: A SEARCH SPACE IS THE CARDINALITY OF A SET")
    items = ("w", "x", "y", "z")
    subsets = [c for k in range(len(items) + 1) for c in combinations(items, k)]
    print(f"   subsets of {{{', '.join(items)}}}: {len(subsets)} = 2^{len(items)}")
    print("     " + "  ".join("{" + ",".join(c) + "}" if c else "{}" for c in subsets))
    print("   (each item is in or out: a 4-fold product of {in, out}, so 2 x 2 x 2 x 2)")
    print()
    print(f"     {'n':>3}  {'subsets 2^n':>14}  {'edges n(n-1)/2':>15}  {'orderings n!':>22}")
    for n in (4, 10, 20, 30, 60):
        S_ = frozenset(range(n))
        edges = math.comb(n, 2)
        if n <= 10:
            assert len(list(combinations(S_, 2))) == edges
            assert sum(1 for _ in permutations(S_)) == math.factorial(n)
        subs = f"{2**n:,}" if n <= 30 else f"{2**n:.3e}"
        print(f"     {n:>3}  {subs:>14}  {edges:>15,}  {math.factorial(n):>22.3e}")
    print("   The rows n <= 10 were counted by enumeration and matched the formula;")
    print("   the rest are the formula alone, because enumerating 2^60 subsets is")
    print("   the point: a brute-force search visits every member of a set, and")
    print("   the set's cardinality is the running time. 2^n and n! are the")
    print("   cardinalities that make a problem 'exponential'. An algorithm that")
    print("   beats brute force is one that decides without visiting every member.")
    print()
    print("   Two more counts that are the same rule:")
    n_nodes = 5
    complete = frozenset(combinations(range(n_nodes), 2))
    print(f"     edges of the complete graph on {n_nodes} nodes:   {len(complete)} = C({n_nodes}, 2)")
    print(f"     possible graphs on {n_nodes} nodes:            {2 ** len(complete):,} = 2^{len(complete)}   (each edge in or out)")
    print(f"     length-4 passwords over 10 digits:        {10 ** 4:,} = 10^4   (a 4-fold product)")


if __name__ == "__main__":
    main()
