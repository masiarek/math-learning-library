#!/usr/bin/env python3
"""The triangle inequality proved: Cauchy-Schwarz from a quadratic with no roots.

Run:  python3 cauchy_schwarz.py

The Euclidean distance was called a metric three pages ago on the
strength of three properties proved and one checked. This program pays
the debt. For vectors u and w the function q(t) = |u + t w|^2 is a
quadratic in t that is never negative, so its discriminant is at most 0,
and that single fact is (u.w)^2 <= |u|^2 |w|^2, the Cauchy-Schwarz
inequality. The triangle inequality for the Euclidean distance then
falls out in three lines. The program computes the quadratic exactly for
sample vectors, shows the equality case, checks the inequality on every
pair of a grid in three dimensions, and derives the triangle inequality
with the square root never taken.
"""

from itertools import product


def dot(u, w):
    return sum(a * b for a, b in zip(u, w))


def quadratic(u, w):
    """Coefficients (A, B, C) of q(t) = |u + t w|^2 = A t^2 + B t + C."""
    return dot(w, w), 2 * dot(u, w), dot(u, u)


def main() -> None:
    print("1. q(t) = |u + t w|^2 IS A QUADRATIC IN t THAT IS NEVER NEGATIVE")
    u, w = (1, 2), (3, 4)
    A, B, C = quadratic(u, w)
    print(f"   u = {u}, w = {w}: q(t) = |w|^2 t^2 + 2 (u.w) t + |u|^2 = {A} t^2 + {B} t + {C}")
    for t in [-2, -1, 0, 1, 2]:
        v = tuple(a + t * b for a, b in zip(u, w))
        print(f"   t = {t:>2}: u + t w = {str(v):<10} q(t) = {dot(v, v)}")
    disc = B * B - 4 * A * C
    print(f"   q(t) is a sum of squares, so q(t) >= 0 for every real t. A quadratic with positive")
    print(f"   leading coefficient that is never negative has no two distinct real roots, so its")
    print(f"   discriminant is at most 0: B^2 - 4AC = {B}^2 - 4 * {A} * {C} = {disc} <= 0.")
    print(f"   Divide by 4: (u.w)^2 <= |u|^2 |w|^2, here {dot(u, w) ** 2} <= {dot(u, u) * dot(w, w)}. That is Cauchy-Schwarz.")
    print()

    print("2. EQUALITY EXACTLY WHEN ONE VECTOR IS A MULTIPLE OF THE OTHER")
    u, w = (1, 2), (2, 4)
    A, B, C = quadratic(u, w)
    disc = B * B - 4 * A * C
    print(f"   u = {u}, w = {w} = 2u: q(t) = {A} t^2 + {B} t + {C}, discriminant {disc}.")
    v = tuple(a + (-1) * b // 2 for a, b in zip(u, w))
    print(f"   q has the double root t = -1/2: u + (-1/2) w = {v}, and (u.w)^2 = {dot(u, w) ** 2} = |u|^2 |w|^2 = {dot(u, u) * dot(w, w)}.")
    print("   The discriminant is 0 exactly when some u + t w is the zero vector, i.e. u is a multiple of w")
    print("   (or w = 0). That is the equality case, and it is where the triangle inequality is an equality too.")
    print()

    print("3. CAUCHY-SCHWARZ ON EVERY PAIR OF A GRID IN THREE DIMENSIONS")
    grid = list(product(range(-2, 3), repeat=3))
    ok = all(dot(u, w) ** 2 <= dot(u, u) * dot(w, w) for u in grid for w in grid)
    eq = sum(dot(u, w) ** 2 == dot(u, u) * dot(w, w) for u in grid for w in grid)
    print(f"   (u.w)^2 <= |u|^2 |w|^2 on {len(grid) ** 2} pairs: {ok};  pairs with equality: {eq}")
    print("   The check is evidence that the inequality was copied right; section 1 is the proof, and it")
    print("   used nothing about the number of coordinates, so it holds in every dimension.")
    print()

    print("4. THE TRIANGLE INEQUALITY, IN THREE LINES AND WITHOUT A SQUARE ROOT")
    print("   |u + w|^2 = |u|^2 + 2 (u.w) + |w|^2                      expand the dot product")
    print("            <= |u|^2 + 2 |u| |w| + |w|^2                     u.w <= |u.w| <= |u| |w|, Cauchy-Schwarz")
    print("            = (|u| + |w|)^2,  so |u + w| <= |u| + |w|          both sides non-negative, take roots")
    print("   With u = Q - P and w = R - Q, u + w = R - P, and the line reads d(P, R) <= d(P, Q) + d(Q, R).")
    # Exact check: |u+w|^2 <= (|u|+|w|)^2  <=>  2 u.w <= 2|u||w|  <=>  u.w <= 0 or (u.w)^2 <= |u|^2|w|^2.
    def triangle_ok(u, w):
        s = dot(u, w)
        return s <= 0 or s * s <= dot(u, u) * dot(w, w)
    ok = all(triangle_ok(u, w) for u in grid for w in grid)
    print(f"   |u + w| <= |u| + |w| on the same {len(grid) ** 2} pairs, compared through squares: {ok}")
    print("   The Euclidean distance has all four properties of a metric, every one of them now proved,")
    print("   and the chapter's main example rests on nothing but 'a square is never negative'.")


if __name__ == "__main__":
    main()
