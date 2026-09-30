#!/usr/bin/env python3
"""Day or night: a yes/no word on a continuous quantity is a cutoff someone chose.

Run:  python3 day_or_night.py

"Is it day?" sounds like a question with two answers. Underneath it is a
number that changes smoothly, the height of the sun above the horizon, and a
yes/no answer needs a cutoff on that number. The program computes the sun's
height at Starbuck, Washington and at Times Square on the summer solstice,
21 June 2026, and asks when night begins under the four cutoffs astronomers
actually use. Each cutoff gives a sharp, reproducible answer. They do not
give the same answer.

The sun's position comes from NOAA's short Fourier-series formulas, good to
about a minute, which is all a question about dusk needs. Times are local
daylight time: PDT (UTC-7) in Starbuck, EDT (UTC-4) in New York.
"""

import math

DAY_OF_YEAR = 172          # 21 June 2026
PLACES = {
    # name: (latitude N, longitude E, hours from UTC)
    "Starbuck, WA": (46.5184, -118.1236, -7),
    "Times Square": (40.7580, -73.9855, -4),
}

# The sun's centre this many degrees above (+) or below (-) the horizon.
CUTOFFS = [
    ("sunset", -0.833, "top edge of the sun leaves the horizon"),
    ("civil dusk", -6.0, "too dark to read outdoors"),
    ("nautical dusk", -12.0, "sea horizon no longer visible"),
    ("astronomical dusk", -18.0, "sky as dark as it gets"),
]


def declination_and_eqtime(day, utc_hours):
    """Sun's declination (degrees) and the equation of time (minutes)."""
    g = 2 * math.pi / 365 * (day - 1 + (utc_hours - 12) / 24)
    eqtime = 229.18 * (0.000075 + 0.001868 * math.cos(g) - 0.032077 * math.sin(g)
                       - 0.014615 * math.cos(2 * g) - 0.040849 * math.sin(2 * g))
    decl = (0.006918 - 0.399912 * math.cos(g) + 0.070257 * math.sin(g)
            - 0.006758 * math.cos(2 * g) + 0.000907 * math.sin(2 * g)
            - 0.002697 * math.cos(3 * g) + 0.00148 * math.sin(3 * g))
    return math.degrees(decl), eqtime


def elevation(place, local_hours):
    """Height of the sun's centre above the horizon, in degrees."""
    lat, lon, tz = PLACES[place]
    utc = local_hours - tz
    decl, eqtime = declination_and_eqtime(DAY_OF_YEAR, utc)
    solar_minutes = utc * 60 + eqtime + 4 * lon
    hour_angle = math.radians(solar_minutes / 4 - 180)
    la, de = math.radians(lat), math.radians(decl)
    s = math.sin(la) * math.sin(de) + math.cos(la) * math.cos(de) * math.cos(hour_angle)
    return math.degrees(math.asin(s))


def crossing(place, cutoff, start=12.0, end=27.0):
    """First local time after noon when the sun sinks below cutoff, or None."""
    step = 1 / 60
    t = start
    while t < end:
        if elevation(place, t) >= cutoff > elevation(place, t + step):
            lo, hi = t, t + step
            for _ in range(40):
                mid = (lo + hi) / 2
                if elevation(place, mid) >= cutoff:
                    lo = mid
                else:
                    hi = mid
            return lo
        t += step
    return None


def clock(hours):
    minutes = round(hours * 60) % (24 * 60)
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def verdict(e, cutoff):
    return "not yet" if e >= cutoff else "night"


print("1. The quantity underneath: the sun's height, Starbuck, 21 June 2026")
print()
print("   local time   sun's height")
for h in [12, 18, 20, 20.5, 21, 21.5, 22, 22.5, 23, 24, 25]:
    print(f"     {clock(h)}      {elevation('Starbuck, WA', h):+7.2f} deg")
print()
print("   It falls smoothly through zero. Nothing in the column says where")
print("   day stops; a yes/no answer needs a cutoff, and someone has to pick it.")
print()

print("2. Four cutoffs, four answers to 'when does night begin?'")
print()
print(f"   {'night begins at':<20}{'cutoff':>9}   {'Starbuck':>9}   {'Times Sq':>9}")
for name, c, _ in CUTOFFS:
    a = crossing("Starbuck, WA", c)
    b = crossing("Times Square", c)
    a = clock(a) if a is not None else "never"
    b = clock(b) if b is not None else "never"
    print(f"   {name:<20}{c:>+9.3f}   {a:>9}   {b:>9}")
first = crossing("Starbuck, WA", -0.833)
last = crossing("Starbuck, WA", -18.0)
print()
print(f"   In Starbuck the four answers span {round((last - first) * 60)} minutes.")
print("   Every one of them is exact to the minute and anyone can recompute it.")
print("   They disagree because they answer four different questions.")
print()

print("3. Same sky, different verdicts: Starbuck at 22:00")
print()
e = elevation("Starbuck, WA", 22)
print(f"   The sun is at {e:+.2f} deg. Under each cutoff:")
for name, c, meaning in CUTOFFS:
    print(f"     {name:<20} {verdict(e, c):<8} ({meaning})")
print()
print("   Two people who call 22:00 'night' and 'not night yet' agree about the sky.")
print("   They disagree about the cutoff, and the argument ends once they say it.")
print()

print("4. No minute is the one: the sorites")
print()
t0, t1 = crossing("Starbuck, WA", -0.833), crossing("Starbuck, WA", -18.0)
steps = []
t = t0
while t + 1 / 60 <= t1:
    steps.append(elevation("Starbuck, WA", t) - elevation("Starbuck, WA", t + 1 / 60))
    t += 1 / 60
print(f"   From sunset to astronomical dusk: {len(steps)} one-minute steps.")
print(f"   The largest drop in one minute:  {max(steps):.3f} deg")
print(f"   The smallest drop in one minute: {min(steps):.3f} deg")
print()
print("   No single minute changes the sky by even a quarter of a degree,")
print("   so 'if it is day now, it is day a minute later' feels safe. Applied")
print(f"   {len(steps)} times it carries you from sunset to full dark. The premise is")
print("   false for every cutoff: at exactly one minute it fails, and the")
print("   cutoff is what says which minute.")
print()

print("5. Where a cutoff is never reached: the lowest sun on the solstice")
print()
decl, _ = declination_and_eqtime(DAY_OF_YEAR, 12)
print(f"   The sun's declination today is {decl:+.2f} deg, so at local midnight")
print("   it sits at  -(90 - latitude - declination)  degrees.")
print()
print(f"   {'latitude':>9}   {'lowest sun':>10}   last cutoff the sun sinks past")
for lat in [40.76, 46.52, 48.0, 50.0, 55.0, 60.0, 66.0, 67.0]:
    low = -(90 - lat - decl)
    reached = [name for name, c, _ in CUTOFFS if low < c]
    label = reached[-1] if reached else "none: the sun never sets"
    print(f"   {lat:>8.2f}N   {low:>+9.2f}    {label}")
print()
print(f"   North of {90 - 18 - decl:.2f}N there is no astronomical night in late June.")
print("   Ask 'when does night begin?' there with the astronomers' cutoff and")
print("   the honest answer is 'it doesn't', not a time.")
print()

print("6. A third way out: a degree of day instead of a yes or no")
print()
print("   Let  day(e) = 0 below -18 deg, 1 above -0.833 deg, a straight line")
print("   between. Then 'day and not day' has the value min(day, 1 - day).")
print()
print("   local time   height      day   day and not-day")
for h in [20.5, 21, 21.25, 21.5, 22, 22.5, 23]:
    e = elevation("Starbuck, WA", h)
    d = min(1.0, max(0.0, (e + 18) / (18 - 0.833)))
    print(f"     {clock(h)}    {e:+7.2f}     {d:.2f}        {min(d, 1 - d):.2f}")
print()
print("   At noon and midnight 'day and not day' is 0, as a two-valued logic")
print("   insists. At dusk it rises to one half. Fuzzy logic keeps both halves")
print("   of the dichotomy and reports how much of each; a cutoff throws that")
print("   number away to get a yes or no.")
