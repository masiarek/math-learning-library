# Precalculus and calculus against the Polish and German school curricula

**Level:** reference · for anyone who learned mathematics in a Polish liceum or a German Gymnasium and meets American course names, or the other way round

**One line:** "Precalculus" and "calculus" are American course names, not subjects; the same topics exist in the Polish *podstawa programowa* and the German *Bildungsstandards*, but they are cut into different years, the Polish extended matura stops at the derivative, the German Abitur reaches the integral, and only the American course teaches conics, polar coordinates, complex numbers and series at school.

This page is a map, not a lesson: three tables of contents laid side by side, with a link wherever this library has a page on the topic. Its one program treats the three curricula as [sets](../../04_Sets/README.md) and compares them with [set operations](../../04_Sets/algebra_of_sets/README.md), so every claim of the kind "X teaches this and Y does not" is a line of output and can be re-run when a row is corrected. Two short companion pages say the same in Polish, [Po polsku](po_polsku.md), and in German, [Auf Deutsch](auf_deutsch.md), for a reader who knows those names and not the American ones.

**How sure.** The Polish curriculum (the 2018 *podstawa programowa* for the four-year liceum, levels *podstawowy* and *rozszerzony*) and the German one (the KMK *Bildungsstandards im Fach Mathematik für die Allgemeine Hochschulreife*, 2012, with the sixteen Länder's own plans on top) are described from memory: both sites are blocked from this session's network. The American side follows the [precalculus reading guide](../precalculus/README.md) and the AP Calculus AB and BC course descriptions, also from memory. The year a topic first appears is the least certain part, because German Länder differ and Polish textbooks order the liceum years freely; the table at the end says how sure each kind of claim is.

## Contents

- [The three systems](#the-three-systems)
- [The map](#the-map)
- [What the program shows](#what-the-program-shows)
- [What each system has that the others lack](#what-each-system-has-that-the-others-lack)
- [How sure](#how-sure)
- [Po polsku, w skrócie](#po-polsku-w-skrocie)
- [See also](#see-also)

## The three systems

| | United States | Poland | Germany |
|---|---|---|---|
| **The last school years** | grades 11 and 12 (ages 16 to 18) | liceum ogólnokształcące, four years, classes 1 to 4 (ages 15 to 19), after eight years of szkoła podstawowa | Gymnasiale Oberstufe: Einführungsphase then Qualifikationsphase Q1 and Q2 (ages 15 to 19, class 10 or 11 to 12 or 13, depending on G8 or G9), after Sekundarstufe I |
| **The course names** | Algebra 1, Geometry, Algebra 2, **Precalculus**, **Calculus** (AP Calculus AB or BC): one subject per year | *matematyka*, every year, at one of two levels: **zakres podstawowy** (compulsory) or **zakres rozszerzony** (extended) | *Mathematik*, every year; in the Oberstufe at **grundlegendes Anforderungsniveau** (Grundkurs) or **erhöhtes Anforderungsniveau** (Leistungskurs) |
| **The leaving exam** | none national; the AP exam is optional and gives university credit | **matura**: podstawowy compulsory for everyone, rozszerzony optional and needed for most mathematics, physics and engineering degrees | **Abitur**: mathematics is compulsory to the end, written at the level of the course taken |
| **What fixes the content** | state standards (most follow the Common Core) and the College Board for AP | one national document, the *podstawa programowa* (regulation of 2018) | one national frame, the KMK *Bildungsstandards* (2012), and sixteen Länder curricula that implement it |
| **The organising idea** | one topic per year: precalculus is "the functions calculus needs" | thirteen numbered content areas, from *liczby rzeczywiste* to *optymalizacja i rachunek różniczkowy*, each at two levels | three *Sachgebiete* (Analysis, Lineare Algebra / Analytische Geometrie, Stochastik) crossed with five *Leitideen* (Algorithmus und Zahl, Messen, Raum und Form, Funktionaler Zusammenhang, Daten und Zufall) |

The first thing the table says is that *precalculus* has no counterpart. No Polish or German student takes a course by that name, because neither system has a year in which "the functions calculus needs" are gathered; they are taught as they come, mostly in the years before the final two, and calculus (Polish *rachunek różniczkowy*, German *Analysis*) starts in the Oberstufe or in the extended liceum course without a separate preparatory year. The second thing is that *calculus* is compulsory for a German school leaver and optional for a Polish and an American one.

## The map

One row per topic. The American column follows the [precalculus reading guide's table](../precalculus/README.md#what-the-course-is-for); the Polish column names the content area (I to XIII) of the podstawa programowa and the level, **P** for podstawowy and **R** for rozszerzony; the German column names the stage, **Sek I** for classes 5 to 10, **GK** for Grundkurs and **LK** for Leistungskurs in the Oberstufe. "Earlier" means the topic is taught before the stage the row is about. The last column links the page here, if any.

### The algebra under everything

| Topic | United States | Poland | Germany | Here |
|---|---|---|---|---|
| Exponent laws, roots, rational exponents | Algebra 2, reviewed in Precalculus | I *Liczby rzeczywiste*, P | Sek I (Klasse 9–10, *Potenzen und Wurzeln*) | [a definition is a test](../../06_Algebraic_Structures/a_definition_is_a_test/README.md) proves the laws |
| Quadratic equations, the quadratic formula | Algebra 1 and 2 | III *Równania i nierówności*, P | Sek I (Klasse 9, *quadratische Gleichungen*) | [catastrophic cancellation](../../01_Precision/catastrophic_cancellation/README.md), [circles](../../08_Analytic_Geometry/circles/README.md) for completing the square |
| Polynomials: zeros, factoring, division | Precalculus | II–III, R (*wielomiany*, twierdzenie Bézouta) | GK, inside Analysis (*ganzrationale Funktionen*) | not here |
| Rational functions, asymptotes | Precalculus | V *Funkcje*, R (*funkcja wymierna*, mostly homographic) | LK (*gebrochenrationale Funktionen*, not in every Land) | not here |
| Absolute value, intervals, inequalities | Algebra 2 | I and III, P | Sek I | [rectangular coordinates](../../08_Analytic_Geometry/rectangular_coordinates/README.md) on intervals; the glossary entry on [absolute value](../../GLOSSARY.md#absolute-value) |
| Systems of linear equations | Algebra 1, matrices in Precalculus | IV *Układy równań*, P (two unknowns) | Sek I; Gauß elimination in the Oberstufe (*lineare Gleichungssysteme*) | [linear equations and their solutions](../../07_Linear_Systems/linear_equations/README.md) |
| Matrices and determinants | Precalculus | not in the podstawa | LK in some Länder (*Matrizen*, *Übergangsmatrizen*) | the [linear algebra reading guide](../linear_algebra/README.md) |

### Functions

| Topic | United States | Poland | Germany | Here |
|---|---|---|---|---|
| Function: domain, range, graph, composition | Algebra 2, Precalculus | V *Funkcje*, P (composition only in R) | Sek I (*Funktionsbegriff*), composition in the Oberstufe | [relations and functions](../../04_Sets/relations_and_functions/README.md), [function katas](../../04_Sets/function_katas/README.md) |
| Shifting and stretching a graph | Precalculus | V, P (*przesunięcie wykresu*), reflections in R | Sek I (Klasse 9–10, *Parameter*) | not here |
| Inverse functions | Precalculus | V, R (*funkcja odwrotna* appears with logarithms) | GK (*Umkehrfunktion*, with ln and eˣ) | [multiplication can be undone](../../03_Complex_Numbers/multiplication_can_be_undone/README.md) is the idea for one operation |
| Exponential functions | Algebra 2, Precalculus | V, P | Sek I (Klasse 10, *exponentielles Wachstum*) | [velocity equals position](../../09_Calculus/velocity_equals_position/README.md), the [doubling-time example](../precalculus/README.md#what-a-precalculus-problem-looks-like) |
| Logarithms, logarithmic functions | Algebra 2, Precalculus | I, P (definition and laws); V, R (the function) | Sek I introduces log for solving equations; GK (*ln*, *Logarithmusfunktion*) | [maps that keep the laws](../../06_Algebraic_Structures/maps_that_keep_the_laws/README.md) |
| Sequences and series, Σ notation | Precalculus | VI *Ciągi*, P (arithmetic and geometric) | Sek I (*Folgen*, lightly; many Länder skip Σ) | [power series](../../09_Calculus/power_series/README.md) for what series become |
| Limit of a sequence, sum of a geometric series | Precalculus (informally) | VI, R (*granica ciągu*, *szereg geometryczny*) | GK (*Grenzwert*, as the entry to the derivative) | [convergence](../../14_Metric_Spaces/convergence/README.md), with ε and N |
| Mathematical induction | Precalculus (some books) | II, R (*indukcja matematyczna*) | not in the Bildungsstandards; LK in a few Länder | [induction](../../11_Logic/induction/README.md) |
| Binomial theorem | Precalculus | II, R (*dwumian Newtona*) | GK, inside Stochastik (*Binomialkoeffizient*) | not here |

### Trigonometry

| Topic | United States | Poland | Germany | Here |
|---|---|---|---|---|
| Right-triangle trigonometry | Geometry | VII *Trygonometria*, P | Sek I (Klasse 9–10) | [congruent and similar triangles](../../10_Geometry/congruent_and_similar_triangles/README.md), the ratios' reason |
| Unit circle, radians, trigonometric functions of any angle | Precalculus | VII, R (*miara łukowa*, *wzory redukcyjne*) | GK (*Sinusfunktion*, *Bogenmaß*) | [radians](../../09_Calculus/radians/README.md) |
| Identities and trigonometric equations | Precalculus | VII, R | LK, lightly | not here |
| Law of sines, law of cosines | Precalculus | VIII *Planimetria*, P (R in older editions) | Sek I (Klasse 10, *Sinus- und Kosinussatz*) | the glossary entry on the [law of cosines](../../GLOSSARY.md#law-of-cosines) |

### Geometry

| Topic | United States | Poland | Germany | Here |
|---|---|---|---|---|
| Pythagoras, similar triangles, area and volume | Geometry, reviewed in Precalculus | szkoła podstawowa, classes 7–8 | Sek I (Klasse 8–9) | all of [10_Geometry](../../10_Geometry/README.md) |
| Plane geometry with proof: triangles, circles, similarity | Geometry | VIII *Planimetria*, P and R (*twierdzenie o kątach w okręgu*, *czworokąty wpisane*) | Sek I | [the Pythagorean theorem and its converse](../../10_Geometry/pythagorean_theorem/README.md), [what a proof is](../../11_Logic/what_a_proof_is/README.md) |
| Solid geometry: prisms, pyramids, spheres, volumes | Geometry | X *Stereometria*, P (angles between lines and planes in R) | Sek I | [area and volume formulas](../../10_Geometry/area_and_volume_formulas/README.md) |
| Lines, slope, distance, midpoint in coordinates | Algebra 1, Precalculus | IX *Geometria analityczna*, P | Sek I (*lineare Funktionen*) | [08_Analytic_Geometry](../../08_Analytic_Geometry/README.md), lessons 1 to 5 |
| The circle in coordinates | Precalculus | IX, P (equation of a circle), R (circle and line) | GK, as a vector equation in some Länder | [circles](../../08_Analytic_Geometry/circles/README.md) |
| Vectors in the plane | Precalculus | IX, P (coordinates, sum, scalar multiple); R (dot product in some editions) | GK, as the start of *Analytische Geometrie* | [distance in n dimensions](../../08_Analytic_Geometry/distance_in_n_dimensions/README.md), the length of a vector |
| Vectors in space, lines and planes, dot product | not at school (multivariable calculus) | not in the podstawa | GK and LK, the whole second *Sachgebiet* (*Geraden und Ebenen im Raum*, *Skalarprodukt*, *Abstände*) | [distance in n dimensions](../../08_Analytic_Geometry/distance_in_n_dimensions/README.md) is the one piece |
| Conic sections | Precalculus | not in the podstawa (parabola only as a graph) | not in the Bildungsstandards | not here |
| Parametric equations, polar coordinates | Precalculus | not in the podstawa | LK, parametric curves in a few Länder | [multiplication rotates](../../03_Complex_Numbers/multiplication_rotates/README.md) is polar form for one kind of number |
| Complex numbers, polar form, de Moivre | Precalculus | not in the podstawa (removed from the rozszerzony in the 2008 reform) | not in the Bildungsstandards; an elective in some Länder | all of [03_Complex_Numbers](../../03_Complex_Numbers/README.md) |

### Combinatorics, probability, statistics

| Topic | United States | Poland | Germany | Here |
|---|---|---|---|---|
| Permutations and combinations | Precalculus (one chapter) | XI *Kombinatoryka*, P (*reguła mnożenia*), R (*wariacje, kombinacje*) | GK, inside Stochastik | [counting partitions](../../04_Sets/equivalence_and_partitions/README.md) is the one counting page |
| Probability: events, conditional probability | Precalculus, or a statistics course | XII, P (classical probability), R (*prawdopodobieństwo warunkowe*, *twierdzenie o prawdopodobieństwie całkowitym*) | Sek I, then GK (*bedingte Wahrscheinlichkeit*, *Baumdiagramm*) | [probability zero](../../02_Measure_Zero/probability_zero/README.md) for what the measure is |
| Binomial distribution, expected value | AP Statistics, not calculus | XII, R (*schemat Bernoulliego*) | GK (*Binomialverteilung*, *Erwartungswert*) | not here |
| Hypothesis tests, normal distribution | AP Statistics | not in the podstawa | GK (*Hypothesentest*), LK (*Normalverteilung*) | not here |
| Descriptive statistics: mean, median, deviation | middle school and Algebra 1 | szkoła podstawowa, then XII, P (*odchylenie standardowe*) | Sek I | [mean, average, arithmetic mean](../../05_Statistics/mean_vs_average/README.md), [a share above a cutoff](../../05_Statistics/share_above_a_cutoff/README.md) |

### Calculus

| Topic | United States | Poland | Germany | Here |
|---|---|---|---|---|
| Limit of a function, continuity | Calculus AB | XIII *Optymalizacja i rachunek różniczkowy*, R | GK (*Grenzwert*, mostly intuitive) | [continuity by ε and δ](../../14_Metric_Spaces/continuity/README.md) |
| The derivative and its rules | Calculus AB | XIII, R (polynomials and rational functions only) | GK (*Ableitung*, *Ableitungsregeln*: Potenz-, Summen-, Faktor-, Produkt-, Kettenregel; Quotientenregel in LK) | [the derivative is a velocity](../../09_Calculus/derivative_as_velocity/README.md) |
| Chain rule | Calculus AB | XIII, R | GK | [related rates](../../09_Calculus/related_rates/README.md) uses it |
| Curve sketching, extrema, optimisation | Calculus AB | XIII, R (*optymalizacja*: the heart of the Polish section) | GK (*Kurvendiskussion*, *Extremwertprobleme*) | not here |
| Related rates | Calculus AB | not in the podstawa | not in the Bildungsstandards | [related rates](../../09_Calculus/related_rates/README.md) |
| Derivatives of eˣ, ln x, sin x, cos x | Calculus AB | not in the podstawa | GK (*e-Funktion*), LK (*trigonometrische Funktionen*) | [velocity equals position](../../09_Calculus/velocity_equals_position/README.md), [radians](../../09_Calculus/radians/README.md) |
| Antiderivative, definite integral, fundamental theorem | Calculus AB | not in the podstawa | GK (*Stammfunktion*, *Integral*, *Hauptsatz*) | not here |
| Area between curves, volumes of revolution | Calculus AB | not in the podstawa | GK (*Flächen*), LK (*Rotationskörper*) | not here |
| Integration by substitution, by parts, partial fractions | AB (substitution), BC (the rest) | not in the podstawa | LK (*Substitution*, *partielle Integration*) | not here |
| Differential equations: separable, growth and decay | Calculus AB | not in the podstawa | LK (*Wachstumsmodelle*, *Differentialgleichungen* in some Länder) | [velocity equals position](../../09_Calculus/velocity_equals_position/README.md) is y′ = y |
| Taylor and power series | Calculus BC | not in the podstawa | not in the Bildungsstandards | [power series](../../09_Calculus/power_series/README.md) |
| Parametric, polar and vector-valued functions | Calculus BC | not in the podstawa | not in the Bildungsstandards | not here |

## What the program shows

The program holds the map above as a dictionary, topic to the courses that first teach it, closes each system upward (what the podstawowy teaches, the rozszerzony also knows), and then asks set questions.

<!-- output:curriculum_sets -->
*Verified output of [`curriculum_sets.py`](examples/curriculum_sets.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. THE COURSES AS SETS
   49 topics in the table. How many each school-leaving course has met:
      US-PRE   30   US precalculus
      US-AB    40   US precalculus + AP Calculus AB
      US-BC    43   US precalculus + AP Calculus BC
      PL-P     20   Polish matura, zakres podstawowy
      PL-R     33   Polish matura, zakres rozszerzony
      DE-G     35   German Abitur, Grundkurs
      DE-E     42   German Abitur, Leistungskurs

2. THE COMMON CORE: taught to every school leaver on the stronger track
   US-BC ∩ PL-R ∩ DE-E (28)
      - Pythagorean theorem, similar triangles, area and volume formulas
      - absolute value and intervals
      - binomial theorem
      - chain rule
      - combinatorics: permutations and combinations
      - curve sketching, extrema, optimisation
      - exponent laws, roots, rational exponents
      - exponential functions
      - functions: domain, range, graph, composition
      - inverse functions
      - law of sines and law of cosines
      - limit of a function, continuity
      - limit of a sequence, sum of a geometric series
      - lines, slope, distance and midpoint in coordinates
      - logarithms and logarithmic functions
      - polynomials: zeros, factoring, division
      - probability: events, conditional probability
      - quadratic equations and the quadratic formula
      - rational functions and asymptotes
      - right-triangle trigonometry
      - sequences and series, Σ notation
      - shifting and stretching a graph
      - systems of linear equations
      - the circle in coordinates
      - the derivative and its rules
      - trigonometric identities and equations
      - unit circle, radians, trigonometric functions of any angle
      - vectors in the plane

3. TAUGHT BY ONE SYSTEM ONLY (strongest track of each)
   US only: US-BC − (PL-R ∪ DE-E) (6)
      - Taylor and power series
      - complex numbers, polar form, de Moivre
      - conic sections: parabola, ellipse, hyperbola
      - parametric, polar and vector-valued functions in calculus
      - polar coordinates
      - related rates
   Poland only: PL-R − (US-BC ∪ DE-E) (0)
      (none)
   Germany only: DE-E − (US-BC ∪ PL-R) (2)
      - hypothesis tests and the normal distribution
      - vectors in space, lines and planes, dot product

4. WHERE THE AMERICAN PRECALCULUS YEAR LANDS
   Of the topics American precalculus teaches, how many the other systems
   teach before the final two years, in them, or not at all:
   Poland: 1 before, 24 during, 5 never, of 30
   Germany: 13 before, 13 during, 4 never, of 30
   Precalculus is not a course anywhere but America: its content is
   spread over the years before the Oberstufe or the liceum, and the
   rest is either in the final years or absent.

5. HOW FAR EACH SYSTEM GETS INTO CALCULUS
      PL-P     0 of 13 AP Calculus topics
      PL-R     4 of 13 AP Calculus topics
      DE-G     7 of 13 AP Calculus topics
      DE-E    10 of 13 AP Calculus topics
      US-AB   10 of 13 AP Calculus topics
      US-BC   13 of 13 AP Calculus topics
   in AP Calculus AB but not in the Polish rozszerzony (11)
      - antiderivative, definite integral, fundamental theorem
      - area between curves, volumes
      - complex numbers, polar form, de Moivre
      - conic sections: parabola, ellipse, hyperbola
      - derivatives of exponential and trigonometric functions
      - differential equations: separable, growth and decay
      - integration by substitution
      - matrices and determinants
      - parametric equations
      - polar coordinates
      - related rates
   in the Polish rozszerzony or German Grundkurs calculus but not in AP AB (0)
      (none)
   Poland rozszerzony has, Germany Grundkurs has not (3)
      - mathematical induction
      - rational functions and asymptotes
      - trigonometric identities and equations
   Germany Grundkurs has, Poland rozszerzony has not (5)
      - antiderivative, definite integral, fundamental theorem
      - area between curves, volumes
      - derivatives of exponential and trigonometric functions
      - hypothesis tests and the normal distribution
      - vectors in space, lines and planes, dot product

6. CHECKS
   every code in the table is a known course: True
   every topic is taught somewhere: True
   each system's tracks nest, lower inside higher: True
   |only one| + |shared by two or more| = |union|: 8 + 41 = 49: True
```
<!-- /output -->

Three lines are worth reading twice.

- **"Poland only: none."** Every topic the Polish extended matura teaches, either the American or the German strong track teaches too. The Polish course is not smaller in kind, only in reach: it stops at the derivative of a rational function and never integrates.
- **"Poland: 1 before, 24 during, 5 never"** against **"Germany: 13 before, 13 during, 4 never."** The German Sekundarstufe I has already done half of American precalculus by Klasse 10, which is why a German Oberstufe can start Analysis at once. The Polish liceum starts at fifteen with much of the same material still ahead, so its first two years are, in American terms, Algebra 2 and precalculus at once, and the extended course gets to the derivative only in the fourth year.
- **"Germany Grundkurs has, Poland rozszerzony has not: 5."** The integral, the derivatives of eˣ and the trigonometric functions, three-dimensional vector geometry and hypothesis testing. A German school leaver on the ordinary track has met more calculus than a Polish one on the extended track; the Polish one has met induction, trigonometric identities and rational functions, which the Grundkurs has not.

## What each system has that the others lack

**Only the American course** teaches conic sections, polar coordinates, complex numbers in polar form and infinite series at school. All four are old university material that moved down into precalculus and Calculus BC; the other two systems leave them for the first university year. This library has pages on three of the four: [03_Complex_Numbers](../../03_Complex_Numbers/README.md), [power series](../../09_Calculus/power_series/README.md), and polar form inside [multiplication rotates](../../03_Complex_Numbers/multiplication_rotates/README.md).

**Only the German course** treats vector geometry in space as a full *Sachgebiet*, lines and planes in ℝ³ with the dot product, distances and angles, and makes hypothesis testing part of every Abitur. An American student meets the first in multivariable calculus or linear algebra at university, and the second in AP Statistics, which is a different course from calculus; a Polish student meets neither at school.

**The Polish course** has no topic of its own in the strong-track comparison, but its emphasis is distinct: proof. The podstawa lists *dowód* as a skill from class 1, the rozszerzony has induction and a geometry section built on proving theorems about circles and quadrilaterals, and the matura rozszerzona asks for proofs every year. The American course states and practises; the German Bildungsstandards name *mathematisch argumentieren* as a competence but the Abitur asks for argument more than for proof. The nearest pages here are [11_Logic](../../11_Logic/README.md), above all [what a proof is](../../11_Logic/what_a_proof_is/README.md) and [induction](../../11_Logic/induction/README.md).

**What all three skip** is what this library spends most of its pages on: [sets](../../04_Sets/README.md) as a subject (the Polish podstawa of 2018 kept only intervals; the German Sek I uses set notation without a topic on it), [precision](../../01_Precision/README.md), [measure zero](../../02_Measure_Zero/README.md), [algebraic structures](../../06_Algebraic_Structures/README.md), the [axioms of set theory](../../13_Axioms_of_Set_Theory/README.md) and [metric spaces](../../14_Metric_Spaces/README.md). Those are the first university year in all three countries, which is where the map stops.

## How sure

| Claim | How sure | Why |
|---|---|---|
| The names of the courses, levels and exams in each country | high | stable for decades, and the owner can confirm the Polish ones |
| The thirteen content areas of the Polish podstawa and the P/R split of each row | medium to high | the 2018 document is recalled by its section titles; the P/R split of a few rows (law of cosines, composition, dot product) has moved between editions and textbooks |
| The three Sachgebiete and five Leitideen of the KMK standards | high | the 2012 document's structure |
| Which German topics are GK and which LK, and in which Klasse Sek I teaches a topic | medium to low | sixteen Länder, G8 and G9, and the GK/LK split is partly each Land's; "in some Länder" marks the rows known to vary |
| The American rows | high for precalculus and AP Calculus AB/BC, medium for the Algebra 1/2 and Geometry placement | the [precalculus reading guide](../precalculus/README.md) and the AP course descriptions; the earlier courses vary by state |
| Complex numbers removed from the Polish rozszerzony in 2008 | medium | from memory of the reform; they were in the pre-2008 extended course and are not in the 2018 podstawa |
| Everything the program prints | exact, given the table | it is set arithmetic on the rows above; correct a row and re-run |

## Po polsku, w skrócie

„Precalculus" i „calculus" to nazwy amerykańskich kursów, nie działów matematyki. W polskim liceum nie ma roku, w którym zbiera się „funkcje potrzebne do analizy": wielomiany, funkcja wymierna, logarytm, trygonometria i ciągi są rozłożone na pierwsze trzy klasy, a rachunek różniczkowy (dział XIII podstawy programowej) pojawia się dopiero w zakresie rozszerzonym i kończy się na pochodnej wielomianu i funkcji wymiernej, bez całki. Niemiecka Oberstufe dochodzi do całki i do geometrii wektorowej w przestrzeni nawet na poziomie podstawowym (Grundkurs); amerykański kurs jako jedyny uczy w szkole krzywych stożkowych, współrzędnych biegunowych, liczb zespolonych i szeregów. Polska matura rozszerzona wyróżnia się czym innym: dowodem, indukcją, tożsamościami trygonometrycznymi. Program na tej stronie traktuje trzy programy nauczania jak zbiory i liczy ich część wspólną i różnice, więc każde zdanie „X tego uczy, a Y nie" można sprawdzić i poprawić, zmieniając jeden wiersz tabeli. Krótsza wersja tej strony po polsku: [Po polsku](po_polsku.md).

## Auf Deutsch: Stichwörter

Precalculus und Calculus sind amerikanische Kursnamen; dieselben Themen stehen in der polnischen podstawa programowa und den deutschen Bildungsstandards, anders auf die Jahre verteilt; die ganze Seite auf Deutsch ist [Auf Deutsch](auf_deutsch.md).

**Stichwörter:** Lehrplan, Bildungsstandards, Sekundarstufe I, Oberstufe, Grundkurs, Leistungskurs, Abitur, matura, Analysis, Analytische Geometrie, Stochastik, Precalculus, AP Calculus.

## See also

- [Po polsku](po_polsku.md) and [Auf Deutsch](auf_deutsch.md), the two companion pages, each a short table from the Polish or German names to the American ones and to the pages here.
- [Precalculus: a reading guide](../precalculus/README.md), the American course this page maps from, with the books.
- [09_Calculus](../../09_Calculus/README.md), calculus as motion: the derivative, the exponential, radians, power series, related rates.
- [Euler's formula: a lesson plan](../eulers_formula/README.md), a path through the precalculus and calculus pages here.
- [Linear algebra: a reading guide](../linear_algebra/README.md), the course after, and the home of the German *Analytische Geometrie* at university.
- [Set theory: a reading guide](../set_theory/README.md), which has a section on the Polish school of set theory.
- [The algebra of sets](../../04_Sets/algebra_of_sets/README.md), the operations the program uses on the three curricula.
