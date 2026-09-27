# 05_Statistics — what does one number say about many?

**Level:** 101 · for anyone who has been told an average

A list of numbers is hard to hold in your head, so people replace it with one number: the average score, the average salary, the average speed. That number always throws something away. What decides whether it is honest is *what it keeps*, and the name in front of it is supposed to say. This chapter is about reading those names.

| # | Lesson | The question it answers |
|---|---|---|
| 1 | [Mean, average, arithmetic mean](mean_vs_average/README.md) | Why does one calculation have so many names, and when do they stop meaning the same thing? |

## The through-line

The arithmetic mean is the one number that can stand in for every value without changing their sum. Other summaries keep other things. The geometric mean keeps a product, the harmonic mean keeps a sum of reciprocals, and the median keeps the middle. Each is right for some questions and wrong for others, and no amount of care in the arithmetic rescues the wrong one. So the first lesson starts with vocabulary: *average*, *mean* and *arithmetic mean* sound like synonyms, and in a classroom they are. Outside it they are three sizes of word, and knowing which size is in use is the first step to knowing what a summary kept and what it lost.

## A note on the code

Every average in this chapter is computed with `fractions.Fraction`, so when a program says a total was kept, it has checked that the total is exactly equal, not equal to fifteen decimal places. Where Python or SQL has a built-in name for the same calculation, the program calls that too, so you can see the name and the arithmetic agree.
