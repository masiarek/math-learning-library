#!/usr/bin/env python3
"""The buffer hour: why a day planned from honest estimates still overruns.

Run:  python3 the_buffer_hour.py

"Reserve an hour every day in case something takes longer than expected,"
says Set Up for Success, and "put an estimated completion time for each item;
as you estimate, your estimates will improve." This program shows why both
tips are arithmetic, not caution.

The model: every task has an estimate, and the estimate is the most likely
time. But a task can barely finish early and can run far over, so the actual
time is the estimate times a multiplier with a long right tail:

    x 1      with chance 6/10   (the estimate was right)
    x 3/2    with chance 3/10   (it took half as long again)
    x 3      with chance 1/10   (something went wrong)

The numbers are chosen for the example, not measured; the shape, rarely
early and sometimes very late, is the point. Every probability below is
computed exactly, by adding up all the ways a day can go; nothing is random.
"""

from fractions import Fraction as F

SKEWED = {F(1): F(6, 10), F(3, 2): F(3, 10), F(3): F(1, 10)}
SYMMETRIC = {F(1, 2): F(2, 10), F(1): F(6, 10), F(3, 2): F(2, 10)}


def day(multipliers, n):
    """Distribution of the total time of n one-hour tasks: {hours: chance}."""
    dist = {F(0): F(1)}
    for _ in range(n):
        new = {}
        for total, p in dist.items():
            for m, q in multipliers.items():
                new[total + m] = new.get(total + m, 0) + p * q
        dist = new
    return dist


def chance_within(dist, hours):
    return sum(p for t, p in dist.items() if t <= hours)


def mean(dist):
    return sum(t * p for t, p in dist.items())


def pct(x):
    return f"{float(x) * 100:5.1f}%"


print("1. One task, estimated at one hour")
print()
for m, p in SKEWED.items():
    print(f"   takes {float(m):>4.2f} h   chance {pct(p)}")
one = day(SKEWED, 1)
print()
print(f"   Most likely time: 1 hour, the estimate. Average time: {float(mean(one)):.2f} hours.")
print("   The estimate is the most common outcome and still 35% short of the")
print("   average, because the misses are all on one side.")
print()

print("2. A day planned to capacity: n one-hour tasks in n hours")
print()
print("   tasks   planned   average needed   chance the day fits")
for n in range(1, 7):
    d = day(SKEWED, n)
    print(f"   {n:>5}   {n:>5} h   {float(mean(d)):>10.2f} h      {pct(chance_within(d, n))}")
print()
print("   Every task is estimated honestly, and a five-task day fits one time")
print("   in thirteen. The day fits only if every task hits its estimate.")
print()

print("3. The buffer hour: five tasks, with b spare hours in the plan")
print()
five = day(SKEWED, 5)
print("   buffer   chance the day fits")
for b in [0, 1, 2, 3]:
    print(f"   {b:>4} h   {pct(chance_within(five, 5 + b))}")
print()
print("   One reserved hour turns a day that fits one time in thirteen into one")
print("   that fits nearly half the time. A plan that holds most days needs more")
print("   slack than feels reasonable, or fewer tasks. When nothing goes wrong,")
print("   the book says, enjoy the unplanned 'you time'.")
print()

print("4. Why the errors do not cancel: skewed against symmetric")
print()
sym = day(SYMMETRIC, 5)
print("   The same five tasks, if a task were as likely to finish half an hour")
print("   early as half an hour late (x 1/2, 1, 3/2 with chances 2/10, 6/10, 2/10):")
print()
print("                      average day   fits in 5 h   fits in 6 h")
print(f"   symmetric errors   {float(mean(sym)):>8.2f} h    {pct(chance_within(sym, 5))}        {pct(chance_within(sym, 6))}")
print(f"   skewed errors      {float(mean(five)):>8.2f} h    {pct(chance_within(five, 5))}        {pct(chance_within(five, 6))}")
print()
print("   With symmetric errors an early task pays for a late one, and a plan")
print("   of five hours is right on average. Real tasks cannot run much under")
print("   their estimate, so nothing pays for the late ones.")
print()

print("5. Estimates that improve: keep the ratio actual / estimated")
print()
print("   Suppose you write down, for twenty past tasks, estimated and actual time.")
record = [F(1)] * 12 + [F(3, 2)] * 6 + [F(3)] * 2   # a record in the model's proportions
ratio = sum(record) / len(record)
print(f"   Twelve took the estimate, six took 1.5 times it, two took 3 times it.")
print(f"   Average ratio: {float(ratio):.2f}. Multiply every new estimate by it:")
print()
plan = 5 * ratio
print(f"   five one-hour tasks are planned as {float(plan):.2f} hours")
print(f"   chance that fits: {pct(chance_within(five, plan))}  (unscaled: {pct(chance_within(five, 5))})")
print()
print("   The ratio is metacognition applied to time: compare what you")
print("   predicted with what happened, and correct the prediction, not the")
print("   feeling. The plan now matches the average day; the buffer hour is")
print("   for the days worse than average.")
