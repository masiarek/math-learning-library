"""Focused and diffuse thinking, as a search on a bumpy landscape.

Barbara Oakley's pinball picture: in focused mode the bumpers are close
together and the ball moves in small steps; in diffuse mode they are far
apart and the ball crosses the table. Here a problem is a row of 60
positions, each with a score, and a solution is the highest score. The
focused player climbs one step at a time; the diffuse player looks at
every seventh position. The scores are a fixed formula, so the output is
the same on every run.
"""

import math

N = 60          # positions on the table
START = 10      # where the first idea lands
CLOSE = 1       # focused mode: bumpers next to each other
FAR = 7         # diffuse mode: bumpers seven apart


def score(x):
    """How good position x is. Several hills, one of them the highest."""
    return round(50 + 18 * math.sin(x / 1.6) + 14 * math.sin(x / 5.3 + 2) + 0.5 * x)


def focused(x, max_steps):
    """Step to the better neighbour until neither neighbour is better."""
    trail = [x]
    for _ in range(max_steps):
        better = [y for y in (x - CLOSE, x + CLOSE) if 0 <= y < N and score(y) > score(x)]
        if not better:
            break
        x = max(better, key=score)
        trail.append(x)
    return trail


def diffuse():
    """Look at every FAR-th position across the whole table."""
    return list(range(0, N, FAR))


def picture(marks):
    """The landscape as columns of #, with letters under chosen positions."""
    lines = []
    for level in range(90, 20, -10):
        row = "".join("#" if score(x) >= level else " " for x in range(N))
        lines.append(f"   {level:3d} |{row}".rstrip())
    lines.append("       +" + "-" * N)
    under = [" "] * N
    for x, ch in marks:
        under[x] = ch
    lines.append("        " + "".join(under).rstrip())
    return lines


def main():
    top = max(range(N), key=score)

    print("1. The problem: 60 positions, and the score of each")
    print()
    for line in picture([(START, "S"), (top, "*")]):
        print(line)
    print()
    print(f"   S is where the first idea lands (position {START}, score {score(START)}).")
    print(f"   * is the best answer (position {top}, score {score(top)}).")
    print("   There are several hills; only one is the highest.")
    print()

    print("2. Focused mode only: small steps uphill from S")
    print()
    trail = focused(START, 3)
    print("   step  position  score")
    for i, x in enumerate(trail):
        print(f"   {i:4d}  {x:8d}  {score(x):5d}")
    stuck = trail[-1]
    print()
    print(f"   After {len(trail) - 1} steps both neighbours are lower, so the climb stops")
    print(f"   at score {score(stuck)}: the top of the nearest hill, not of the highest.")
    print()
    print("   Trying harder, with the same small steps:")
    print()
    print("   steps allowed   final position   final score")
    for effort in (3, 10, 100, 1000):
        end = focused(START, effort)[-1]
        print(f"   {effort:13d}   {end:14d}   {score(end):11d}")
    print()
    print("   A thousand steps end where three did. Effort is not the problem;")
    print("   the step size is. Every step away from the peak goes downhill, so")
    print("   a focused climber never takes it.")
    print()

    print(f"3. Diffuse mode only: one look at every {FAR}th position")
    print()
    looks = diffuse()
    print("   position  " + "".join(f"{x:4d}" for x in looks))
    print("   score     " + "".join(f"{score(x):4d}" for x in looks))
    rough = max(looks, key=score)
    print()
    print(f"   The best look is position {rough}, score {score(rough)}. It has found the")
    print(f"   right hill, far from S, but not its top: {score(rough)}, not {score(top)}.")
    print("   Wide bounces cross the table and miss the details.")
    print()

    print("4. Both, one at a time: focus, step back, focus again")
    print()
    first = focused(START, 1000)
    second = focused(rough, 1000)
    print("   phase                          positions visited   best score")
    print(f"   focused from S                 {len(first):17d}   {score(first[-1]):10d}")
    print(f"   diffuse survey                 {len(looks):17d}   {score(rough):10d}")
    print(f"   focused from the best look     {len(second):17d}   {score(second[-1]):10d}")
    total = len(first) + len(looks) + len(second)
    print(f"   total                          {total:17d}")
    print()
    for line in picture([(START, "S"), (stuck, "F")] + [(x, "d") for x in looks if x not in (START, stuck)] + [(second[-1], "*")]):
        print(line)
    print()
    print(f"   S start, F where focus got stuck, d the diffuse looks, * the answer.")
    print(f"   {total} looks in all reach score {score(second[-1])}, which a thousand focused steps")
    print("   did not. The survey picks the hill; focus climbs it.")
    print()

    print("5. Every starting point, focused mode only")
    print()
    ends = {}
    for s in range(N):
        end = focused(s, 1000)[-1]
        ends.setdefault(end, []).append(s)
    print("   stuck at position   score   starting positions   how many")
    for end in sorted(ends, key=lambda e: (-score(e), e)):
        starts = ends[end]
        span = f"{starts[0]}-{starts[-1]}" if len(starts) > 1 else f"{starts[0]}"
        print(f"   {end:17d}   {score(end):5d}   {span:>18}   {len(starts):8d}")
    good = len(ends[top])
    print()
    print(f"   Focus alone finds the answer from {good} of {N} starts ({100 * good // N}%): only when")
    print("   the first idea already landed on the right hill. Where you start")
    print("   decides where focus ends.")


if __name__ == "__main__":
    main()
