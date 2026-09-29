#!/usr/bin/env python3
"""Rectangular coordinates: a point is two signed distances, a quadrant is two signs.

Run:  python3 rectangular_coordinates.py

Descartes' idea is that a point of the plane is an ordered pair of numbers and
an ordered pair of numbers is a point of the plane. The program checks what the
textbook says about that on real points: where the four points of the standard
figure land, which axis each coordinate measures from, why (-3, 1) is not
(1, -3), that a quadrant depends on nothing but the signs of x and y, why the
axes have to belong to no quadrant, and what the word "quadrant" buys you when
a point is reflected, multiplied, or only known by sign.

Everything is an integer, so every claim is exact.
"""

from itertools import product

# The four points plotted in the textbook's figure, labelled for the grid.
FIGURE = [("A", (-3, 1)), ("B", (3, 2)), ("C", (3, -2)), ("D", (-2, -3))]


def quadrant(point: tuple[int, int]) -> str:
    """The quadrant of a point, from the two signs alone; '-' on an axis."""
    x, y = point
    if x == 0 or y == 0:
        return "-"
    if x > 0 and y > 0:
        return "I"
    if x < 0 and y > 0:
        return "II"
    if x < 0 and y < 0:
        return "III"
    return "IV"


def sign(n: int) -> str:
    return "+" if n > 0 else "-" if n < 0 else "0"


def fmt(point: tuple[int, int]) -> str:
    return f"({point[0]}, {point[1]})"


def plot(points: list[tuple[str, tuple[int, int]]], lo: int = -4, hi: int = 4, y_up: bool = True) -> None:
    """Draw the xy-plane as a grid of cells, the axes as | and -, the origin as O.

    y_up=False draws y positive downward, the way a computer screen does.
    """
    marks = {p: label for label, p in points}
    rows = range(hi, lo - 1, -1) if y_up else range(lo, hi + 1)
    for y in rows:
        row = []
        for x in range(lo, hi + 1):
            if (x, y) in marks:
                cell = marks[(x, y)]
            elif x == 0 and y == 0:
                cell = "O"
            elif x == 0:
                cell = "|"
            elif y == 0:
                cell = "-"
            else:
                cell = "."
            row.append(f"{cell:>3}")
        print(f"   {y:>3} " + "".join(row))
    print("       " + "".join(f"{x:>3}" for x in range(lo, hi + 1)) + "   x")


def main() -> None:
    print("1. THE PLANE, AND THE FOUR POINTS OF THE FIGURE")
    print("   y")
    plot(FIGURE)
    for label, p in FIGURE:
        print(f"   {label} = {fmt(p)}")
    print("   The y-axis is the column of |, the x-axis the row of -, O the origin.")
    print()

    print("2. EACH COORDINATE IS A SIGNED DISTANCE, AND FROM THE OTHER AXIS")
    print("     point      x: from the y-axis     y: from the x-axis     to plot it")
    for _, (x, y) in FIGURE:
        side = "right" if x > 0 else "left"
        updown = "up" if y > 0 else "down"
        print(
            f"     {fmt((x, y)):<10} {abs(x)} {side:<5} of it       "
            f"  {abs(y)} {updown:<4} from it        "
            f"{abs(x)} {side}, then {abs(y)} {updown}"
        )
    print("   x says how far right or left, which is distance from the vertical")
    print("   line, the y-axis. The sign says which side; the size says how far.")
    print()

    print("3. THE PAIR IS ORDERED: (-3, 1) IS NOT (1, -3)")
    p, q = (-3, 1), (1, -3)
    print(f"     {fmt(p)} == {fmt(q)}   is {p == q}")
    print(f"     {fmt(p)}   3 left, 1 up      quadrant {quadrant(p)}")
    print(f"     {fmt(q)}   1 right, 3 down   quadrant {quadrant(q)}")
    print("   Same two numbers, different point. The first entry is always x.")
    print()

    print("4. A QUADRANT IS NOTHING BUT THE PAIR OF SIGNS")
    print("     point        sign of x   sign of y   quadrant")
    sample = [(3, 2), (-3, 1), (-2, -3), (3, -2), (1, 1), (1000, 5), (-1, 1000), (0, 0), (4, 0), (0, -2)]
    for pt in sample:
        q = quadrant(pt)
        where = q if q != "-" else "none: on an axis"
        print(f"     {fmt(pt):<12} {sign(pt[0]):^9}   {sign(pt[1]):^9}   {where}")
    print("   (1, 1) and (1000, 5) share a quadrant: the sizes never enter into it.")
    print("   A 0 has no sign, so a point with a 0 coordinate has no quadrant.")
    print()

    print("5. WHY THE AXES MUST BELONG TO NO QUADRANT")
    grid = [(x, y) for x, y in product(range(-2, 3), repeat=2)]
    counts = {name: 0 for name in ("I", "II", "III", "IV", "-")}
    for pt in grid:
        counts[quadrant(pt)] += 1
    print("   every point with integer coordinates from -2 to 2, 5 x 5 = 25 points:")
    print(f"     quadrant I: {counts['I']}   II: {counts['II']}   III: {counts['III']}   IV: {counts['IV']}   on an axis: {counts['-']}")
    total = sum(counts.values())
    print(f"     4 + 4 + 4 + 4 + 9 = {total}: each point counted exactly once.")
    loose = {"I": 0, "II": 0, "III": 0, "IV": 0}
    for x, y in grid:
        loose["I"] += x >= 0 and y >= 0
        loose["II"] += x <= 0 and y >= 0
        loose["III"] += x <= 0 and y <= 0
        loose["IV"] += x >= 0 and y <= 0
    print("   the same 25 points if the quadrants were defined with >= and <= instead:")
    print(f"     quadrant I: {loose['I']}   II: {loose['II']}   III: {loose['III']}   IV: {loose['IV']}")
    print(f"     9 + 9 + 9 + 9 = {sum(loose.values())} memberships for 25 points: the origin would be in")
    print("     all four and every other axis point in two. Strict signs make the")
    print("     four quadrants a partition: every point off the axes is in exactly one.")
    print()

    print("6. WHAT THE WORD BUYS YOU: A SIGN CHANGE IS A CHANGE OF QUADRANT")
    print("     point        (-x, y)          (x, -y)          (-x, -y)")
    print("                  across y-axis    across x-axis    through O")
    for _, (x, y) in FIGURE:
        a, b, c = (-x, y), (x, -y), (-x, -y)
        print(
            f"     {fmt((x, y)):<9} {quadrant((x, y)):<3}"
            f"  {fmt(a):<9} {quadrant(a):<3}"
            f"    {fmt(b):<9} {quadrant(b):<3}"
            f"    {fmt(c):<9} {quadrant(c)}"
        )
    print("   Negating x swaps I with II and III with IV, whatever the numbers are.")
    print("   That is why a graph's symmetry can be checked one quadrant at a time.")
    print()

    print("7. THE SIGN OF A PRODUCT NAMES TWO QUADRANTS")
    print("     point        x * y    sign   quadrant")
    for pt in [(3, 2), (-3, 1), (-2, -3), (3, -2), (5, 5), (-5, 5)]:
        prod = pt[0] * pt[1]
        print(f"     {fmt(pt):<12} {prod:>4}     {sign(prod)}      {quadrant(pt)}")
    print("   xy > 0 exactly in I and III, xy < 0 exactly in II and IV. So 'the graph")
    print("   of y = 1/x lies in quadrants I and III' is a fact about the sign of xy.")
    print()

    print("8. A QUARTER TURN MOVES A POINT ONE QUADRANT ON")
    print("   the rule (x, y) -> (-y, x), which is multiplication by i in 03_Complex_Numbers:")
    for _, (x, y) in FIGURE:
        turned = (-y, x)
        print(f"     {fmt((x, y)):<9} quadrant {quadrant((x, y)):<4} ->  {fmt(turned):<9} quadrant {quadrant(turned)}")
    print("   I -> II -> III -> IV -> I: the quadrants are numbered in the direction")
    print("   a quarter turn goes, counterclockwise, which is why the numbering is")
    print("   the one it is and not clockwise.")
    print()

    print("9. THE SAME SYMBOLS, TWO OBJECTS: THE POINT (2, 5) AND THE INTERVAL (2, 5)")
    point = (2, 5)
    print(f"   as a point, (2, 5) is a pair, 2 right and 5 up, quadrant {quadrant(point)}:")
    print(f"     len((2, 5)) = {len(point)};   3 in (2, 5) is {3 in point}   a tuple holds 2 and 5, not 3")
    print("   as an open interval, (2, 5) is a test, 2 < t < 5:")
    for t in (3, 2, 5, 7):
        print(f"     t = {t}:  2 < {t} < 5  is {2 < t < 5}")
    print("   the endpoints fail: open means the ends are left out.")
    print(f"   (5, 2) as a point is 5 right and 2 up, quadrant {quadrant((5, 2))}. As an interval:")
    print(f"     t = 3:  5 < 3 < 2  is {5 < 3 < 2};   no t passes, the interval (5, 2) is empty,")
    print("     so when a < b fails the notation can only mean the point.")
    print()

    print("10. THE ARROW DECIDES WHICH WAY IS AROUND")
    start = (3, 2)
    trip = [start]
    for _ in range(3):
        x, y = trip[-1]
        trip.append((-y, x))
    print("   the quarter turn (x, y) -> (-y, x), applied three times from (3, 2):")
    print("     " + " -> ".join(fmt(p) for p in trip) + f",  quadrants {' '.join(quadrant(p) for p in trip)}")
    numbered = [(str(i + 1), p) for i, p in enumerate(trip)]
    print("   the four positions, numbered 1 to 4, with y positive UPWARD (the book):")
    plot(numbered, y_up=True)
    print("   the same four points, same numbers, with y positive DOWNWARD (a computer screen):")
    plot(numbered, y_up=False)
    print("   1 -> 2 -> 3 -> 4 runs counterclockwise in the first picture and clockwise in")
    print("   the second. Not one coordinate changed; only which way the y-axis points.")
    print("   The same flip turns the line through (0, 0) and (2, 2) from rising to falling.")
    print("   Which direction is positive is a choice, and the arrow records it.")


if __name__ == "__main__":
    main()
