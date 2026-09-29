#!/usr/bin/env python3
"""Plot points on a text grid and say which quadrant, or which axis, each is on.

Run:  python3 plot_points.py                          the book's problems 15 and 16
      python3 plot_points.py -3,2 6,0 "(0, -3)"       your own points, labelled A, B, C ...
      python3 plot_points.py P=2,5 Q=5,2              your own labels
      python3 plot_points.py --drill 3                eight points to plot, answers below a line

Without arguments it plots the two "Skill Building" exercises that follow the
textbook section on rectangular coordinates, so the recorded output is an
answer key. With points on the command line it plots those instead, which is
how to check a plot of your own: type the coordinates, and compare the grid
and the last column with what you drew. --drill takes a seed, so the same
number always gives the same eight points and the answers can be checked
against a friend's.

Coordinates are integers, because the grid has one cell per unit.
"""

import random
import string
import sys

Point = tuple[int, int]

# Sullivan, Precalculus, section 1.1, problems 15 and 16: "plot each point in
# the xy-plane. State which quadrant or on what coordinate axis each point lies."
EXERCISES: list[tuple[str, list[tuple[str, Point]]]] = [
    ("Problem 15", [("A", (-3, 2)), ("B", (6, 0)), ("C", (-2, -2)), ("D", (6, 5)), ("E", (0, -3)), ("F", (6, -3))]),
    ("Problem 16", [("A", (1, 4)), ("B", (-3, -4)), ("C", (-3, 4)), ("D", (4, 1)), ("E", (0, 1)), ("F", (-3, 0))]),
]


def where(point: Point) -> str:
    """Quadrant or axis, from the signs alone."""
    x, y = point
    if x == 0 and y == 0:
        return "the origin, on both axes"
    if y == 0:
        return "on the x-axis"
    if x == 0:
        return "on the y-axis"
    if x > 0 and y > 0:
        return "quadrant I"
    if x < 0 and y > 0:
        return "quadrant II"
    if x < 0 and y < 0:
        return "quadrant III"
    return "quadrant IV"


def fmt(point: Point) -> str:
    return f"({point[0]}, {point[1]})"


def plot(points: list[tuple[str, Point]]) -> None:
    """The grid: axes as | and -, origin O, one letter per point, * where two share a cell."""
    reach = max([6] + [abs(c) for _, p in points for c in p])
    cells: dict[Point, list[str]] = {}
    for label, p in points:
        cells.setdefault(p, []).append(label)
    print("     y")
    for y in range(reach, -reach - 1, -1):
        row = []
        for x in range(-reach, reach + 1):
            if (x, y) in cells:
                labels = cells[(x, y)]
                cell = labels[0] if len(labels) == 1 else "*"
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
    print("       " + "".join(f"{x:>3}" for x in range(-reach, reach + 1)) + "   x")


def report(points: list[tuple[str, Point]]) -> None:
    plot(points)
    width = max(len(fmt(p)) for _, p in points)
    for label, p in points:
        print(f"   {label} = {fmt(p):<{width}}   {where(p)}")
    shared = [p for p in {p for _, p in points} if sum(1 for _, q in points if q == p) > 1]
    for p in sorted(shared):
        names = ", ".join(label for label, q in points if q == p)
        print(f"   * at {fmt(p)}: {names} are the same point")


def parse(args: list[str]) -> list[tuple[str, Point]]:
    """'-3,2', '(−3, 2)' or 'P=-3,2' -> a labelled point; unlabelled ones get A, B, C ..."""
    points = []
    letters = iter(string.ascii_uppercase)
    for arg in args:
        label, _, coords = arg.rpartition("=")
        text = coords.replace("−", "-").replace("(", "").replace(")", "").replace(" ", "")
        try:
            x, y = (int(part) for part in text.split(","))
        except ValueError:
            sys.exit(f"cannot read {arg!r}: write a point as x,y with integer coordinates, e.g. -3,2")
        points.append((label or next(letters), (x, y)))
    return points


def drill(seed: int) -> None:
    """Eight points to plot, then the answers below a line to cover."""
    rng = random.Random(seed)
    nonzero = [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]
    points: list[tuple[str, Point]] = []
    for label in string.ascii_uppercase[:8]:
        while True:
            kind = rng.choice(["quadrant", "quadrant", "quadrant", "axis"])
            if kind == "axis":
                p = rng.choice([(rng.choice(nonzero), 0), (0, rng.choice(nonzero))])
            else:
                p = (rng.choice(nonzero), rng.choice(nonzero))
            if p not in {q for _, q in points}:
                break
        points.append((label, p))
    print(f"DRILL {seed}: plot each point, and say which quadrant or axis it is on.")
    for label, p in points:
        print(f"   {label} = {fmt(p)}")
    print()
    print("   " + "-" * 60 + "  answers below")
    print()
    report(points)


def main(argv: list[str]) -> None:
    if argv[:1] == ["--drill"]:
        drill(int(argv[1]) if len(argv) > 1 else 1)
        return
    if argv:
        report(parse(argv))
        return
    for name, points in EXERCISES:
        print(f"{name.upper()}: plot each point; state which quadrant or coordinate axis it lies on")
        report(points)
        print()
    print("To check a plot of your own:  python3 plot_points.py -3,2 6,0 0,-3")
    print("For eight points to practise on:  python3 plot_points.py --drill 3")


if __name__ == "__main__":
    main(sys.argv[1:])
