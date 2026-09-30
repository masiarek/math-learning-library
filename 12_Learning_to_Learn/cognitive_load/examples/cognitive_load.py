#!/usr/bin/env python3
"""Cognitive load: the same page weighs less once practice has made chunks.

Run:  python3 cognitive_load.py

Working memory holds about four chunks at once (Cowan, 2001). What counts as
one chunk is not fixed: it is whatever you have practised until it is
automatic. So the load of a page, its intrinsic load in Sweller's terms,
depends on the reader, and anything else in the room takes its share of the
same four places.

The program reads strings the way a learner with a given set of known chunks
would: at each point it takes the longest piece it knows, one symbol if it
knows nothing longer. Section 3 then builds chunks by practice, merging the
pair of neighbours found in the most lines, which is the byte-pair encoding
algorithm (Gage, 1994) that language models use to build their vocabularies.
"""

CAPACITY = 4


def read(text, known):
    """Split text into chunks: at each point the longest known piece, else one symbol."""
    chunks, i = [], 0
    longest = max((len(k) for k in known), default=1)
    while i < len(text):
        for size in range(min(longest, len(text) - i), 0, -1):
            piece = text[i:i + size]
            if size == 1 or piece in known:
                chunks.append(piece)
                i += size
                break
    return chunks


def show(chunks):
    return " | ".join(chunks)


print("1. The same string, three readers")
print()
for digits in ["2851012", "1234567"]:
    c = read(digits, {"1234567"})
    print(f"   {digits}, to someone who knows counting: {len(c)} chunk{'s' if len(c) > 1 else ''}")
    print(f"     {show(c)}")
print()
digits = "149217761945"
for who, known in [("knows digits only", set()),
                   ("knows the years 1492, 1776, 1945", {"1492", "1776", "1945"})]:
    c = read(digits, known)
    print(f"   {who}: {len(c)} chunks")
    print(f"     {show(c)}")
print()
formula = "(a+b)^2=a^2+2ab+b^2"
readers = [
    ("a beginner, who knows the symbols", set()),
    ("a student, who knows the two sides", {"(a+b)^2", "a^2+2ab+b^2"}),
    ("an expert, who knows the identity", {formula}),
]
for who, known in readers:
    c = read(formula, known)
    print(f"   {who}: {len(c)} chunks")
    print(f"     {show(c)}")
print()
print("   Nothing on the page changed. The load is in the reader.")
print()

print(f"2. A budget of {CAPACITY}: intrinsic load plus whatever else is in the room")
print()
print("   Suppose a conversation nearby takes 2 places and a phone on the desk")
print("   takes 1: numbers for the example, not measurements.")
print()
rooms = [("quiet room", 0), ("phone on the desk", 1), ("conversation nearby", 2)]
print(f"   {'reader':<12}" + "".join(f"{r:>22}" for r, _ in rooms))
for (who, known), short in zip(readers, ["beginner", "student", "expert"]):
    intrinsic = len(read(formula, known))
    cells = []
    for _, extra in rooms:
        total = intrinsic + extra
        cells.append(f"{total} {'fits' if total <= CAPACITY else 'overloaded'}")
    print(f"   {short:<12}" + "".join(f"{c:>22}" for c in cells))
print()
print("   The expert reads this formula anywhere. The student reads it in a")
print("   quiet room or beside a phone, but not beside a conversation: that is")
print("   the load that tips it over, and moving to another room is the fix, as")
print("   the book says. For the beginner no room is quiet enough; only")
print("   practice helps.")
print()
print("3. Practice makes chunks: merge the pair found in the most lines")
print()
practice = ["(a+b)^2=a^2+2ab+b^2", "(x+y)^2=x^2+2xy+y^2", "(p+q)^2=p^2+2pq+q^2",
            "(u+v)^2=u^2+2uv+v^2", "(s+t)^2=s^2+2st+t^2"]
test = "(m+n)^2=m^2+2mn+n^2"
print("   Practice sheet, five expansions of a square:")
for line in practice:
    print(f"     {line}")
print(f"   Test line, never practised: {test}")
print()
seqs = [list(line) for line in practice]
known = set()
print("   merge   new chunk     chunks in the test line")
print(f"   {0:>5}   {'':<12}  {len(read(test, known)):>3}")
for step in range(1, 20):
    # count each pair once per line: a pattern is what recurs across lines
    counts = {}
    for s in seqs:
        for pair in set(zip(s, s[1:])):
            counts[pair] = counts.get(pair, 0) + 1
    # most frequent pair; ties broken by first appearance, so the run is reproducible
    order = []
    for s in seqs:
        for a, b in zip(s, s[1:]):
            if (a, b) not in order:
                order.append((a, b))
    best = max(order, key=lambda p: counts[p])
    if counts[best] < 2:
        break
    new = best[0] + best[1]
    known.add(new)
    merged = []
    for s in seqs:
        out, i = [], 0
        while i < len(s):
            if i + 1 < len(s) and (s[i], s[i + 1]) == best:
                out.append(new)
                i += 2
            else:
                out.append(s[i])
                i += 1
        merged.append(out)
    seqs = merged
    print(f"   {step:>5}   {new!r:<12}  {len(read(test, known)):>3}")
print()
print(f"   The test line now reads as: {show(read(test, known))}")
print()
print("   Practice took the line from 19 chunks to 12, and every chunk it built")
print("   is a part that repeats across lines: '^2', ')^2=', '^2+2'. The letters")
print("   change from line to line, so they never became chunks, and what")
print("   practice built carries over to m and n, never practised.")
print()
print("   What is left is the two letters, three times each. Merging can go no")
print("   further; the last step is to see the line as one chunk with two slots,")
print("   (first + second)^2 = first^2 + 2 first second + second^2. That is a")
print("   schema, in the book's word, and it is how the expert in section 1")
print("   holds the identity as one chunk. Every merge cost effort on the")
print("   practice sheet: that effort is germane load.")
