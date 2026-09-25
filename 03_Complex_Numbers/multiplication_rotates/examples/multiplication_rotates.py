#!/usr/bin/env python3
"""Complex multiplication rotates: multiply the lengths, add the angles.

Run:  python3 multiplication_rotates.py

The rule (x1, y1) . (x2, y2) = (x1 x2 - y1 y2, x1 y2 + x2 y1) looks like
algebra. Geometrically it does two things at once: it scales by the length
of the second point, and it turns by the angle of the second point. Below,
that is checked exactly with fractions. Lengths are compared as squares, so
no square root is ever taken, and angles are tracked with points whose angle
is known exactly: the four compass points, and unit points built from
Pythagorean triples.
"""

from fractions import Fraction as F

Pair = tuple[F, F]


def mul(z1: Pair, z2: Pair) -> Pair:
    x1, y1 = z1
    x2, y2 = z2
    return (x1 * x2 - y1 * y2, x1 * y2 + x2 * y1)


def length_squared(z: Pair) -> F:
    x, y = z
    return x * x + y * y


def show(z: Pair) -> str:
    x, y = z
    return f"({x}, {y})"


def compass(z: Pair) -> str:
    return {(1, 0): "east", (0, 1): "north", (-1, 0): "west", (0, -1): "south"}[
        (int(z[0]), int(z[1]))
    ]


EAST: Pair = (F(1), F(0))
NORTH: Pair = (F(0), F(1))


def main() -> None:
    print("1. MULTIPLYING BY (0, 1) IS A QUARTER TURN")
    print("   Take each compass point and multiply it by (0, 1):")
    for z in [EAST, NORTH, (F(-1), F(0)), (F(0), F(-1))]:
        w = mul(z, NORTH)
        print(f"     {show(z):<9} {compass(z):<6} . (0, 1) = {show(w):<9} {compass(w)}")
    print("   East to north to west to south to east: a quarter turn")
    print("   counterclockwise, every time.")
    print()

    print("2. SO (0, 1) . (0, 1) = (-1, 0) IS 'TWO QUARTER TURNS ARE A HALF TURN'")
    z = EAST
    for k in range(1, 5):
        z = mul(z, NORTH)
        turn = {1: "a quarter", 2: "a half", 3: "three quarters", 4: "a full"}[k]
        print(f"     after {k} multiplication{'s' if k > 1 else ' '} by (0, 1): {show(z):<9} {turn} turn")
    print("   A half turn sends every point to the opposite side of the origin,")
    print("   which is exactly what multiplying by -1 does. So (0, 1) squared")
    print("   behaves as -1, and that is the whole content of i^2 = -1.")
    print()

    print("3. THE TWO AXES, MULTIPLIED")
    print("   Horizontal times horizontal: angle 0 + 0, stays horizontal.")
    for a, b in [(F(2), F(3)), (F(-4), F(5))]:
        print(f"     {show((a, F(0))):<9} . {show((b, F(0))):<9} = {show(mul((a, F(0)), (b, F(0))))}")
    print("   Vertical times vertical: angle 90 + 90 = 180, lands on the")
    print("   NEGATIVE horizontal axis.")
    for a, b in [(F(3), F(2)), (F(1), F(1)), (F(-2), F(5))]:
        print(f"     {show((F(0), a)):<9} . {show((F(0), b)):<9} = {show(mul((F(0), a), (F(0), b)))}")
    print("   In the usual notation the last three read 3i . 2i = -6,")
    print("   i . i = -1, and (-2i)(5i) = 10. The minus sign is the half turn.")
    print()

    print("4. LENGTHS MULTIPLY (compared as squares, so the check is exact)")
    print(f"     {'z1':<12} {'z2':<12} {'|z1|^2':>7} {'|z2|^2':>7} {'|z1 z2|^2':>10}   product of the two")
    for z1, z2 in [((F(3), F(4)), (F(5), F(12))), ((F(1), F(1)), (F(1), F(1))),
                   ((F(0), F(3)), (F(0), F(2))), ((F(1, 2), F(1, 3)), (F(-2), F(5)))]:
        p = mul(z1, z2)
        a, b, c = length_squared(z1), length_squared(z2), length_squared(p)
        assert c == a * b
        print(f"     {show(z1):<12} {show(z2):<12} {str(a):>7} {str(b):>7} {str(c):>10}   {a} x {b} = {a * b}")
    print("   |z1 z2|^2 = |z1|^2 |z2|^2 in every row, so |z1 z2| = |z1| |z2|.")
    print()

    print("5. ANGLES ADD (checked with angles that are known exactly)")
    print("   A 3-4-5 triangle gives a unit point at angle A = atan(4/3), and a")
    print("   5-12-13 triangle one at angle B = atan(12/5). Their product should")
    print("   sit at angle A + B, and there is a way to check that without ever")
    print("   computing an angle: the point at A + B, turned back by A, is at B.")
    a = (F(3, 5), F(4, 5))
    b = (F(5, 13), F(12, 13))
    ab = mul(a, b)
    back = mul(ab, (a[0], -a[1]))  # multiplying by the mirror image turns by -A
    print(f"     a      = {show(a)}          |a|^2 = {length_squared(a)}")
    print(f"     b      = {show(b)}        |b|^2 = {length_squared(b)}")
    print(f"     a . b  = {show(ab)}      |a.b|^2 = {length_squared(ab)}")
    print(f"     (a . b) turned back by A = {show(back)}   which is b again: {back == b}")
    print("   Turning back by A means multiplying by the mirror image (3/5, -4/5),")
    print("   the point at angle -A. It works because angles add.")
    print()

    print("6. SCALE AND TURN AT ONCE")
    print("   Multiplying (1, 0) by (0, 3) should be: turn a quarter, stretch by 3.")
    for z in [EAST, (F(2), F(1)), (F(-1), F(-1))]:
        w = mul(z, (F(0), F(3)))
        print(f"     {show(z):<9} . (0, 3) = {show(w):<9} |z|^2 = {length_squared(z)}, |w|^2 = {length_squared(w)} = 9 x {length_squared(z)}")
    print("   Every point turned a quarter turn and grew by a factor of 3.")
    print("   That is what the rule always does: multiply by the length of the")
    print("   second point, turn by its angle.")


if __name__ == "__main__":
    main()
