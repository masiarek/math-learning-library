#!/usr/bin/env python3
"""A share above a cutoff: "20% of people have Lp(a) 50+", read as mathematics.

Run:  python3 share_above_a_cutoff.py

A sentence of the form "p% of people have X at or above c" says exactly one
thing: c is the (100 - p)-th percentile of X. It does not say what the typical
value is, or the average. In a right-skewed quantity like lipoprotein(a), the
average can sit near the cutoff while four people in five are below it.

Sections 1 and 2 use small made-up lists and exact fractions. Sections 3 and 4
use a log-normal model, an assumption chosen for illustration, not measured
data: median 12 mg/dL, and 20% at or above 50 mg/dL.
"""

import math
import statistics
from fractions import Fraction
from statistics import NormalDist

CUTOFF = 50
SHARE = Fraction(1, 5)  # "20% of people"


def share_at_or_above(xs: list[int], c: int) -> Fraction:
    return Fraction(sum(1 for x in xs if x >= c), len(xs))


def pct(f: float | Fraction) -> str:
    return f"{float(f) * 100:.0f}%"


print("1. The sentence is a percentile, read from the other end")
print()
results = [3, 5, 6, 8, 9, 10, 11, 12, 14, 15, 17, 20, 24, 29, 33, 41, 55, 72, 98, 140]
print(f"   twenty made-up results, sorted (mg/dL): {results[:10]}")
print(f"                                           {results[10:]}")
print(f"   share at or above {CUTOFF}: {share_at_or_above(results, CUTOFF)} = {pct(share_at_or_above(results, CUTOFF))}")
below = sum(1 for x in results if x < CUTOFF)
print(f"   {below} of {len(results)} are below {CUTOFF}, so {CUTOFF} sits at the {pct(Fraction(below, len(results)))} mark:")
print(f"   '20% at or above {CUTOFF}' and '{CUTOFF} is the 80th percentile' are one fact.")
print()

print("2. What the one fact pins down, and what it leaves free")
print()
low = [0] * 16 + [50] * 4
high = [49] * 16 + [500] * 4
for name, xs in (("A", low), ("B", high)):
    print(f"   population {name}: share >= {CUTOFF} = {pct(share_at_or_above(xs, CUTOFF))}"
          f"   median = {statistics.median(xs):>4g}   mean = {float(statistics.mean(xs)):>5g}")
bound = SHARE * CUTOFF
print(f"   Both satisfy the sentence. The only thing it forces on the mean")
print(f"   (Markov's inequality, for values that cannot be negative):")
print(f"      mean >= share x cutoff = {SHARE} x {CUTOFF} = {bound}")
print(f"   population A meets that bound exactly: mean = {statistics.mean(low)}")
print()

print("3. A skewed model: median 12, and 20% at or above 50")
print()
median = 12.0
z80 = NormalDist().inv_cdf(1 - float(SHARE))
mu = math.log(median)
sigma = (math.log(CUTOFF) - mu) / z80
model = NormalDist(mu, sigma)  # the distribution of log(Lp(a))
print(f"   log(Lp(a)) is normal with mu = ln {median:g} = {mu:.3f}, sigma = {sigma:.3f}")
print()
print("   percentile   Lp(a), mg/dL")
for p in (10, 25, 50, 75, 80, 90, 95):
    value = math.exp(model.inv_cdf(p / 100))
    mark = "   <- the cutoff" if p == 80 else ("   <- the median" if p == 50 else "")
    print(f"   {p:>7}th   {value:>10.1f}{mark}")
mean = math.exp(mu + sigma**2 / 2)
share_below_mean = model.cdf(math.log(mean))
print()
print(f"   mean = exp(mu + sigma^2/2) = {mean:.1f} mg/dL")
print(f"   share of people below the mean: {pct(share_below_mean)}")
print("   In this model the mean, the average person, is at the cutoff,")
print("   and the median, the typical person, is at a quarter of it.")
print()

print("4. Where the line is drawn decides the percentage")
print()
print("   cutoff, mg/dL   share at or above it (same model)")
for c in (30, 50, 70, 100, 180):
    share = 1 - model.cdf(math.log(c))
    print(f"   {c:>13}   {pct(share):>5}")
print("   '20%' is a property of the pair (population, cutoff), not of either alone.")
