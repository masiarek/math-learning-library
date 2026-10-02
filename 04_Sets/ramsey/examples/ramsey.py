"""Ramsey's theorem: the pigeonhole principle for pairs, and why it is set theory.

Combinatorics asks how large a collection must be before some pattern is
forced. Ramsey's theorem is the first such result about sets of pairs:
colour every pair from a large enough set with two colours, and a set of
three whose pairs are all one colour appears. The program checks the finite
theorem by exhaustion, runs the proof of the infinite theorem as an
algorithm, and shows the tree argument (König's lemma) that connects the two.
Everything uses the standard library only.
"""

from itertools import combinations, permutations, product


def pairs(points):
    return list(combinations(sorted(points), 2))


def monochromatic_triangle(colour, points):
    """A triangle whose three edges share a colour, or None."""
    for a, b, c in combinations(sorted(points), 3):
        if colour[(a, b)] == colour[(a, c)] == colour[(b, c)]:
            return (a, b, c)
    return None


def triangle_by_pigeonhole(colour, points):
    """The proof of R(3, 3) <= 6 as a procedure: pick a point, apply the
    pigeonhole principle to the five edges at it, and close a triangle."""
    points = sorted(points)
    v = points[0]
    by_colour = {}
    for w in points[1:]:
        by_colour.setdefault(colour[(v, w)], []).append(w)
    col, three = max(by_colour.items(), key=lambda kv: len(kv[1]))
    three = three[:3]
    for a, b in combinations(three, 2):
        if colour[(a, b)] == col:
            return (v, a, b), col, "closes with the first point"
    return tuple(three), ("red" if col == "blue" else "blue"), "the other colour, among the three"


def longest_monotone(seq):
    best_up = best_down = 1
    n = len(seq)
    up = [1] * n
    down = [1] * n
    for j in range(n):
        for i in range(j):
            if seq[i] < seq[j]:
                up[j] = max(up[j], up[i] + 1)
            if seq[i] > seq[j]:
                down[j] = max(down[j], down[i] + 1)
        best_up, best_down = max(best_up, up[j]), max(best_down, down[j])
    return best_up, best_down


def bad_colourings(n):
    """Every 2-colouring of the pairs of {0..n-1} without a monochromatic triangle."""
    es = pairs(range(n))
    found = []
    for bits in product(("red", "blue"), repeat=len(es)):
        colour = dict(zip(es, bits))
        if monochromatic_triangle(colour, range(n)) is None:
            found.append(colour)
    return found


def main():
    print("1. THE PIGEONHOLE PRINCIPLE: MORE PIGEONS THAN HOLES")
    pigeons, holes = range(4), range(3)
    maps = list(product(holes, repeat=len(pigeons)))
    crowded = sum(1 for m in maps if any(m.count(h) >= 2 for h in holes))
    print(f"   maps from {len(pigeons)} pigeons to {len(holes)} holes: {len(maps)};"
          f" with some hole holding two or more: {crowded}")
    print("   The same for infinitely many pigeons in finitely many holes: some hole")
    print("   holds infinitely many. That is the one-colour case of what follows.")
    print()

    print("2. ERDŐS AND SZEKERES: EVERY FIVE NUMBERS HOLD A MONOTONE THREE")
    perms5 = list(permutations(range(1, 6)))
    ok5 = sum(1 for p in perms5 if max(longest_monotone(p)) >= 3)
    print(f"   orderings of 1..5: {len(perms5)}; with an increasing or decreasing run of 3: {ok5}")
    bad4 = [p for p in permutations(range(1, 5)) if max(longest_monotone(p)) < 3]
    print(f"   orderings of 1..4 with no monotone run of 3: {len(bad4)}, e.g. {bad4[0]} and {bad4[1]}")
    print("   In general n² + 1 numbers force a monotone run of n + 1 (1935). It is a")
    print("   pigeonhole statement about the set of pairs: colour each pair {i < j}")
    print("   'up' if the later number is larger, and ask for a one-colour set.")
    print()

    print("3. R(3, 3) = 6: SIX POINTS FORCE A ONE-COLOUR TRIANGLE, FIVE DO NOT")
    six = range(6)
    es6 = pairs(six)
    total = found = by_proof = 0
    for bits in product(("red", "blue"), repeat=len(es6)):
        colour = dict(zip(es6, bits))
        total += 1
        if monochromatic_triangle(colour, six) is not None:
            found += 1
        tri, col, _ = triangle_by_pigeonhole(colour, six)
        a, b, c = sorted(tri)
        if colour[(a, b)] == colour[(a, c)] == colour[(b, c)] == col:
            by_proof += 1
    print(f"   2-colourings of the {len(es6)} edges of K6: {total}; with a one-colour triangle: {found}")
    print(f"   triangles found by the pigeonhole procedure (pick a point, 5 edges, 2 colours,")
    print(f"   so 3 edges agree; among their far ends any edge of that colour closes a")
    print(f"   triangle, else the three form one of the other colour): {by_proof}")
    five = range(5)
    pent = {(i, j): ("red" if (j - i) % 5 in (1, 4) else "blue") for i, j in pairs(five)}
    print(f"   K5 coloured by distance round a pentagon (1 or 4 red, 2 or 3 blue):")
    print(f"   one-colour triangle: {monochromatic_triangle(pent, five)}")
    print("   So the Ramsey number R(3, 3) is exactly 6. In Halbeisen's arrow notation,")
    print("   6 → (3)²₂ and 5 ↛ (3)²₂: 'colour the 2-subsets of a 6-set with 2 colours")
    print("   and a 3-subset has all its 2-subsets one colour'.")
    print()

    print("4. THE TREE OF BAD COLOURINGS DIES, WHICH IS KÖNIG'S LEMMA IN REVERSE")
    for n in range(1, 7):
        print(f"   n = {n}: colourings of K{n} with no one-colour triangle: {len(bad_colourings(n))}")
    print("   Each bad colouring of K_n restricts to a bad colouring of K_{n-1}, so the")
    print("   bad colourings form a tree, finitely branching, one level per n. König's")
    print("   lemma: an infinite finitely branching tree has an infinite branch. An")
    print("   infinite branch here would colour all pairs of ℕ with no one-colour")
    print("   triangle, which the infinite theorem (section 5) forbids. So the tree is")
    print("   finite, and the level where it dies is the Ramsey number.")
    print()

    print("5. THE INFINITE THEOREM AS AN ALGORITHM (RAMSEY 1930)")
    N = 64
    points = list(range(1, N + 1))

    def c(i, j):
        return "red" if j % i == 0 else "blue"

    print(f"   points 1..{N}; the pair {{i < j}} is red when i divides j, blue otherwise")
    rest = points[:]
    chosen = []
    while len(rest) > 1:
        a, rest = rest[0], rest[1:]
        reds = [x for x in rest if c(a, x) == "red"]
        blues = [x for x in rest if c(a, x) == "blue"]
        col, rest = ("red", reds) if len(reds) >= len(blues) else ("blue", blues)
        chosen.append((a, col))
    print("   step: take the least point left, split the rest by its colour with that")
    print("   point, keep the larger part (on ℕ: the infinite part, by pigeonhole)")
    print("   chosen points and the colour each sees ahead:")
    print("   " + ", ".join(f"{a}:{col[0]}" for a, col in chosen))
    from collections import Counter
    tally = Counter(col for _, col in chosen)
    col = tally.most_common(1)[0][0]
    homog = [a for a, k in chosen if k == col] + rest
    es = pairs(homog)
    print(f"   the points that saw {col}, plus what is left: {homog}")
    print(f"   all {len(es)} pairs among them {col}: {all(c(i, j) == col for i, j in es)}")
    print("   On ℕ the chosen sequence is infinite; infinitely many of its points see the")
    print("   same colour (pigeonhole again), and they are an infinite one-colour set.")
    print("   Ramsey proved this for n-element subsets and any finite number of colours.")
    print()

    print("6. WHY THIS IS SET THEORY: THE ANSWER DEPENDS ON THE SET")
    rows = [
        ("6 → (3)²₂", "finite, checked above", "yes, by exhaustion"),
        ("ω → (ω)ⁿ_k", "Ramsey 1930, proof in section 5", "the algorithm, not the limit"),
        ("ω₁ ↛ (ω₁)²₂", "Sierpiński 1933: the first uncountable set fails", "no: it needs the reals well-ordered"),
        ("κ → (κ)²₂", "defines a weakly compact cardinal (a large cardinal)", "no: ZFC cannot prove one exists"),
        ("R(5, 5) = ?", "between 43 and 46 (from memory, 2024)", "no: 2^(C(43,2)) colourings"),
    ]
    print(f"   {'statement':<14} {'what it says':<52} can a program check it?")
    for s, what, prog in rows:
        print(f"   {s:<14} {what:<52} {prog}")
    print("   A colouring of pairs is a partition of the set of 2-subsets, and the theorem")
    print("   asks which sets are big enough that some partition piece contains all the")
    print("   pairs of a big subset. For finite sets the answer is a number; for infinite")
    print("   sets it depends on the axioms. That is Halbeisen's reason for calling the")
    print("   subject combinatorial set theory.")


if __name__ == "__main__":
    main()
