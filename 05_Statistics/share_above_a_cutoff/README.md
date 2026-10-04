# A share above a cutoff

**Level:** 101 · for anyone who has read a headline like "20% of people have Lp(a) 50+"

**One line:** "p% of people are at or above c" says only that c is the (100 − p)-th percentile. It does not tell you the typical value or the average, and when the quantity is skewed the mean can sit right at the cutoff while four people in five are below it.

## The sentence

A health video puts it in large letters: **20% of people have Lp(a) 50+.** Lp(a), lipoprotein(a), is a cholesterol-carrying particle in the blood, close kin to LDL, and a high level is linked to heart attack and stroke. Two facts about it make the headline worth reading carefully. The level is set mostly by one gene, so it barely changes over a lifetime and one test is usually enough. And it is lopsided: most people have little, and a minority have a great deal. The 50 is in mg/dL, and 50 mg/dL is a threshold that guidelines commonly use for raised risk. The European Atherosclerosis Society's 2022 consensus statement is one example.

The medicine is for a doctor. The mathematics in that sentence is for this page. It has three parts: a quantity, a cutoff and a share. What can you conclude from it, and what can't you?

## It is a percentile, read from the other end

Section 1 of the program sorts twenty made-up results and counts: 4 of the 20 are at or above 50, and 16 are below it. Saying "20% are at or above 50" and saying "50 is the 80th percentile" is saying the same thing twice. A percentile answers *what value has this share of people below it?* A cutoff with a share answers the same question backwards: *what share of people is above this value?*

That is all the sentence says. It fixes one point on the distribution and leaves everything else free.

## What the one fact leaves free

Section 2 builds two populations that both satisfy the headline exactly:

- **A:** sixteen people at 0 and four at 50. The median is 0 and the mean is 10.
- **B:** sixteen people at 49 and four at 500. The median is 49 and the mean is 139.2.

Both have 20% at or above 50. They share nothing else. So the sentence tells you neither what a typical person has nor what the average is.

It does rule one thing out. A level cannot be negative, so the one person in five at 50 or more contributes at least 50 × ⅕ = 10 to the mean on their own:

> mean ≥ share × cutoff = ⅕ × 50 = 10

This is **Markov's inequality**. It is the whole of what the headline guarantees about the mean, and population A shows that the bound can be met exactly. There is no upper bound, because the people above the cutoff can be as high as you like.

## A skewed model

To see what a realistic shape does, section 3 assumes one: log(Lp(a)) is normally distributed, a **log-normal** model, with a median of 12 mg/dL and with 20% at or above 50. Both numbers are the assumption. A median of that order has been reported for populations of European descent, but the program is an illustration and not a data set. The real distribution has a lighter far tail than a log-normal: values above a few hundred mg/dL are very rare, and the model's 95th percentile of 195 is too high. The shape near the middle is roughly right, and the middle is where the argument lives.

Two numbers fix the model. The median fixes μ = ln 12. The 80th percentile of a standard normal is z = 0.842, so 50 = e^(μ + 0.842 σ), which gives σ = 1.70. The program prints the percentiles, and then something that surprises most readers:

- the **median** is 12, a quarter of the cutoff;
- the **mean** is e^(μ + σ²/2) = 50.5, right at the cutoff;
- **80%** of people are below the mean.

In a right-skewed quantity the mean sits far above most of the people it describes. The few very high values pull it up and the many low values cannot pull it back, the same effect as the owner's salary in [mean, average, arithmetic mean](../mean_vs_average/README.md). The sentences "the average person has about 50" and "80% of people are below 50" are both true of this model.

## Where the line is drawn decides the percentage

Section 4 keeps the model and moves the cutoff. At 30 mg/dL the share above is 29%; at 50 it is 20%; at 100 it is 11%; at 180 it is 6%. "20%" belongs to the pair (population, cutoff) and not to either one alone. The same people give a different headline when a guideline moves its line, and the same line gives a different headline in a population with a different mix of genes. Lp(a) levels do differ a great deal between ancestries.

## The unit is part of the cutoff

Lp(a) is reported in two units. mg/dL measures the mass of the particles, and nmol/L counts them. The particles do not all weigh the same, because the part that gives Lp(a) its "(a)" comes in many sizes that are set by the gene. So there is no single factor between the units. 50 mg/dL is usually quoted as about 105 to 125 nmol/L. A cutoff copied from one unit to the other with a fixed factor is an approximation dressed as an exact number, which is the problem [exact vs approximate](../../01_Precision/exact_vs_approximate/README.md) is about.

## How to read such a sentence

1. **Turn it into a percentile.** "p% at or above c" means c is the (100 − p)-th percentile, and nothing more.
2. **Don't read an average into it.** The median can be far below c, and the mean can be anywhere from share × c upward.
3. **Ask whose population and whose cutoff.** Moving either one changes the percentage.
4. **Check the unit.** A threshold in the wrong unit is a different threshold.

This page is about the arithmetic of the sentence and gives no medical advice. What your own Lp(a) result means is a question for a clinician.

## Run it yourself

From the root of your clone of this repository:

```bash
python3 05_Statistics/share_above_a_cutoff/examples/share_above_a_cutoff.py
```

<!-- output:share_above_a_cutoff -->
*Verified output of [`share_above_a_cutoff.py`](examples/share_above_a_cutoff.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. The sentence is a percentile, read from the other end

   twenty made-up results, sorted (mg/dL): [3, 5, 6, 8, 9, 10, 11, 12, 14, 15]
                                           [17, 20, 24, 29, 33, 41, 55, 72, 98, 140]
   share at or above 50: 1/5 = 20%
   16 of 20 are below 50, so 50 sits at the 80% mark:
   '20% at or above 50' and '50 is the 80th percentile' are one fact.

2. What the one fact pins down, and what it leaves free

   population A: share >= 50 = 20%   median =    0   mean =    10
   population B: share >= 50 = 20%   median =   49   mean = 139.2
   Both satisfy the sentence. The only thing it forces on the mean
   (Markov's inequality, for values that cannot be negative):
      mean >= share x cutoff = 1/5 x 50 = 10
   population A meets that bound exactly: mean = 10

3. A skewed model: median 12, and 20% at or above 50

   log(Lp(a)) is normal with mu = ln 12 = 2.485, sigma = 1.696

   percentile   Lp(a), mg/dL
        10th          1.4
        25th          3.8
        50th         12.0   <- the median
        75th         37.7
        80th         50.0   <- the cutoff
        90th        105.4
        95th        195.2

   mean = exp(mu + sigma^2/2) = 50.5 mg/dL
   share of people below the mean: 80%
   In this model the mean, the average person, is at the cutoff,
   and the median, the typical person, is at a quarter of it.

4. Where the line is drawn decides the percentage

   cutoff, mg/dL   share at or above it (same model)
              30     29%
              50     20%
              70     15%
             100     11%
             180      6%
   '20%' is a property of the pair (population, cutoff), not of either alone.
```
<!-- /output -->

## Po polsku, w skrócie

Zdanie „20% ludzi ma Lp(a) 50+” wygląda jak statystyka o całej populacji, ale mówi dokładnie jedną rzecz: 50 mg/dL to 80. centyl. Osiemdziesiąt procent ludzi ma mniej, dwadzieścia ma tyle albo więcej. O typowym wyniku i o średniej nie mówi nic. Program buduje dwie populacje, które spełniają to zdanie co do joty: w jednej mediana wynosi 0, w drugiej 49, a średnie to 10 i 139,2.

Jedyne, co zdanie gwarantuje, to dolna granica średniej. Wynik nie może być ujemny, więc piąta część ludzi z wynikiem co najmniej 50 sama wnosi do średniej co najmniej 10. To nierówność Markowa. Górnej granicy nie ma.

Pułapka tkwi w skośności. Lp(a) zależy głównie od genów: większość ludzi ma go mało, a nieliczni bardzo dużo. W modelu log-normalnym, dobranym tak, żeby mediana wynosiła 12, a 20% było powyżej 50, średnia wychodzi około 50, czyli równo na progu. Mimo to 80% ludzi jest poniżej średniej. „Przeciętny” w sensie średniej to nie to samo co „typowy”.

Ta sama grupa ludzi daje inny procent, gdy przesunąć próg, a ten sam próg daje inny procent w innej populacji. Trzeba też uważać na jednostkę: mg/dL i nmol/L nie przeliczają się jednym stałym współczynnikiem. To nie jest porada medyczna. Własny wynik warto omówić z lekarzem.

## Auf Deutsch: Stichwörter

Aus einer Schlagzeile einen Anteil über einer Schwelle ablesen: Perzentil, Normalverteilung und was die Zahl annimmt.

**Stichwörter:** Anteil (share), Schwelle (cutoff), Perzentil, Normalverteilung, Standardabweichung, z-Wert, Annahme.

## See also

- [Mean, average, arithmetic mean](../mean_vs_average/README.md): the same pull of a few large values, on salaries
- [Exact vs approximate](../../01_Precision/exact_vs_approximate/README.md): why a unit conversion with no fixed factor gives an approximate cutoff
- [Lipoprotein(a) ↗](https://en.wikipedia.org/wiki/Lipoprotein(a)): Wikipedia, the particle and what is known about it
- [Log-normal distribution ↗](https://en.wikipedia.org/wiki/Log-normal_distribution): Wikipedia, the model in section 3
- [Markov's inequality ↗](https://en.wikipedia.org/wiki/Markov%27s_inequality): Wikipedia, the one bound the headline gives on the mean
