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

from itertools import product


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

    print("3. THE PRODUCT RULE  |A x B| = |A| . |B|")
    A = frozenset(range(4))
    B = frozenset("abcdefg")
    AB = frozenset(product(A, B))
    print(f"   |A| = {len(A)}, |B| = {len(B)}, |A x B| = {len(AB)} = {len(A)} x {len(B)}")
    print("   Same rule, read as types: a pair type has as many values as the")
    print("   product of its parts. Some sizes every programmer already knows:")
    bool_vals = 2
    u8 = 2**8
    u16 = 2**16
    print(f"     bool             {bool_vals:>12,}")
    print(f"     uint8            {u8:>12,}")
    print(f"     uint16           {u16:>12,}")
    print(f"     (bool, uint8)    {bool_vals * u8:>12,}   product type: 2 x 256")
    print(f"     (uint8, uint8)   {u8 * u8:>12,}   product type: 256 x 256 = uint16")
    print(f"     bool | uint8     {bool_vals + u8:>12,}   sum type (tagged union): 2 + 256")
    print(f"     Optional[uint8]  {1 + u8:>12,}   None | uint8: 1 + 256")
    print(f"     uint8 -> bool    {bool_vals ** u8:>12.3e}   function type: 2^256 tables")
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
        for s in product(alphabet, repeat=length):
            listing.append("".join(s))
        length += 1
    print("     " + "  ".join(listing[:14]) + "  ...")
    print("   So |programs| = |N|. A function from N to {0, 1} is an infinite")
    print("   0/1 sequence, and section 7 showed those cannot be listed. There")
    print("   are more such functions than there are programs, so some of them")
    print("   have no program at all. That is the cardinality argument for the")
    print("   existence of uncomputable functions, and it needs no example.")


if __name__ == "__main__":
    main()
