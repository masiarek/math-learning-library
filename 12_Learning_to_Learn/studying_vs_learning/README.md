# Studying vs learning: Bloom's levels on one theorem

**Level:** 101 · for anyone who has "gone over" a chapter the night before a test

**One line:** Studying is collecting the "whats"; learning is working out the "hows", "whys" and "what ifs", and Bloom's six levels say how far up that climb you have come. At the top you can re-create the facts you forgot, because what you hold is the thing that produces them.

## Studying mode and learning mode

Saundra McGuire opens chapter 4 of *Teach Yourself How to Learn* with a four-step process (Figure 4.1):

1. What's the difference between studying and learning?
2. Would you study harder to make an A on a test or to teach the material to the class?
3. Bloom's taxonomy: read about each level, then apply it to an example.
4. At what level of Bloom's have you *been* operating? At what level do you *need* to be operating now?

Answer the first two for yourself before reading on.

Among the answers she has collected: "studying is memorizing information for the exam; learning is when I understand it and can apply it", "studying is short term; learning is long term". Her colleague Pam Ball's version: cramming "is like renting the information for the test and falling behind on your payments. Right after the test, the information is repossessed!" The one McGuire likes best is from a first-year dental student:

> "Studying is focusing on the 'whats,' but learning is focusing on the 'hows,' 'whys,' and 'what ifs.' … when I focus on the 'whats,' if I forget them I can't re-create the information. But when I focus on the 'hows,' 'whys,' and 'what ifs,' even if I forget the 'whats,' I can re-create them."

Asked whether they have been in study mode or learn mode, students answer "study mode" almost unanimously, and most had not known there was another mode.

## Make-an-A mode and teach-the-material mode

The second question: would you work harder to make an A on a test, or to teach the material to the class? Most students choose teaching, and their reasons are the whole argument: "I have to really know it if I have to teach it!"; "I have to think of questions I might be asked and make sure I can answer them"; "I need to figure out how to explain the information in more than one way."

Then comes the uncomfortable follow-up: until now, have you been in make-an-A mode or teach-the-material mode? Virtually everyone admits to the first. McGuire asks when, if you had not been explaining the material to someone, you would have found out that you did not fully understand it. Groups answer in unison: **"On the test!"**

Teaching works because a teacher anticipates the *questions*. Someone preparing to teach looks at a topic from several sides, searching for any confusion their "students" might have, instead of reacting only to the biggest gaps in their own understanding. That is the fourth ability of [metacognition](../metacognition/README.md), turned into a habit. You do not need a class: McGuire suggests empty chairs, stuffed animals, a coat rack, friends, family, or pets.

## Bloom's six levels

Benjamin Bloom and his colleagues published the original hierarchy in 1956: Knowledge, Comprehension, Application, Analysis, Synthesis, Evaluation. In 2001 one of the original authors, David Krathwohl, and one of Bloom's students, Lorin Anderson, revised it. They renamed the levels as verbs, to make them sound like things you do, and swapped the top two, so that creating now sits above evaluating. This is the pyramid on the cover of McGuire's book. She says it makes no difference which version you use, as long as you see that memorising something, understanding it well enough to put in your own words, and applying it to questions you have never seen are different things.

| Level (2001) | 1956 name | Anderson and colleagues' definition, shortened | On [the Pythagorean theorem](../../10_Geometry/pythagorean_theorem/README.md) |
|---|---|---|---|
| 1. Remembering | Knowledge | retrieving, recognizing and recalling relevant knowledge from long-term memory | state a² + b² = c², list 3-4-5 |
| 2. Understanding | Comprehension | constructing meaning: interpreting, exemplifying, classifying, summarizing, inferring, comparing, explaining | say why it holds |
| 3. Applying | Application | carrying out or using a procedure | find how high a ladder reaches |
| 4. Analyzing | Analysis | breaking material into parts and seeing how they relate to one another and to the whole | sort triangles into right, acute, obtuse |
| 5. Evaluating | Evaluation (the top level in 1956) | making judgments based on criteria and standards, by checking and critiquing | refute "every whole-number right triangle is a 3-4-5" |
| 6. Creating | Synthesis | putting elements together into a coherent whole; generating, planning, producing | a formula that produces every whole-number right triangle |

McGuire's plain-language test for each level: at Remembering you have memorised the formula but could not put it in your own words; at Understanding you could explain it to a 7-year-old or a 70-year-old with examples from their lives; at Applying you can solve problems you have never seen; at Analyzing you can break a concept into its parts and give a mini-lecture on it; at Evaluating you can look at two methods someone else proposes and judge which is likelier to be correct or efficient; at Creating you can design your own.

Most students say they did very well in school at the first or second level, and recognise that harder courses need level 4 or above; section 7 of the program measures how far that recognition moved one group. Night-before studying lives on level 1: it collects the whats. Most test questions in mathematics start at level 3, and a question you have never seen can be answered only from the levels above it.

### Is it really a pyramid?

Some educators object to drawing Bloom's as a pyramid: the levels do not proceed in order, they say, and a student can create something without knowing the foundations. McGuire grants the point but keeps the pyramid, because it shows that you are unlikely to *apply* what you do not *understand*, or understand what you have not *memorised*. Her story: a medical resident, asked whether pseudoephedrine drugs are advisable for pregnant women, looked it up on his phone and answered correctly, "No", but could not say why. The why, that drugs which constrict blood vessels are a bad idea in pregnancy, is what would have answered the next question. "We can solve problems and do critical thinking only with information already stored in our brains." Level 1 is not the goal, but it is the floor: the program's section 6 needs to know what a right triangle is before it can generate one.

## What the program prints

The program climbs all six levels on one theorem. Each level is a different kind of code: level 1 is a list, level 2 an area computation, level 4 a comparison that turns out to sort all triangles, level 5 a search for a counterexample, and level 6 **Euclid's formula**, which generates right triangles from two numbers m and n. The last check is the dental student's point, made by a program: the three triples a student would memorise at level 1 come back out of the formula, with eleven more, and a brute-force search confirms that no triangle is missing. Section 7 puts McGuire's Figure 4.5 into numbers: 250 chemistry students asked at what level they had worked in high school, and at what level they would need to work in college.

<!-- output:studying_vs_learning -->
*Verified output of [`studying_vs_learning.py`](examples/studying_vs_learning.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. REMEMBERING: recall the fact
   'In a right triangle, a^2 + b^2 = c^2.' Common triples, as flashcards:
   (3, 4, 5), (5, 12, 13), (8, 15, 17)
   Enough to answer 'state the theorem'. Nothing more.

2. UNDERSTANDING: say why it holds, in your own terms
   Put four copies of the (3, 4) triangle inside a square of side 3 + 4.
   The big square has area 49; the four triangles take 24;
   the tilted square left in the middle has area 49 - 24 = 25 = 5^2.
   In letters: (a + b)^2 - 2ab = a^2 + b^2, and the middle square is c^2.

3. APPLYING: use it on a new problem
   A 13 m ladder stands 5 m from a wall. How high does it reach?
   sqrt(13^2 - 5^2) = sqrt(144) = 12 m.

4. ANALYZING: take the claim apart; what does each piece do?
   (5, 12, 13): a^2 + b^2 = 169, c^2 = 169  ->  right
   (5, 12, 12): a^2 + b^2 = 169, c^2 = 144  ->  acute
   (5, 12, 14): a^2 + b^2 = 169, c^2 = 196  ->  obtuse
   The comparison does more than the theorem said: it sorts every triangle
   into three kinds, and it only works if c is the longest side.

5. EVALUATING: judge a claim, with evidence
   Claim: 'every right triangle with whole sides is a multiple of 3-4-5'.
   Verdict: false. First counterexample: (5, 12, 13).

6. CREATING: build something new that produces the facts
   Euclid's formula: for m > n > 0, coprime, not both odd,
   (m^2 - n^2, 2mn, m^2 + n^2) is a right triangle with no common factor.
   m = 2, n = 1:  ( 3,  4,  5)  <- was a flashcard
   m = 3, n = 2:  ( 5, 12, 13)  <- was a flashcard
   m = 4, n = 1:  ( 8, 15, 17)  <- was a flashcard
   m = 4, n = 3:  ( 7, 24, 25)
   m = 5, n = 2:  (20, 21, 29)
   m = 6, n = 1:  (12, 35, 37)
   m = 5, n = 4:  ( 9, 40, 41)
   m = 7, n = 2:  (28, 45, 53)
   m = 6, n = 5:  (11, 60, 61)
   m = 8, n = 1:  (16, 63, 65)
   m = 7, n = 4:  (33, 56, 65)
   m = 8, n = 3:  (48, 55, 73)
   m = 7, n = 6:  (13, 84, 85)
   m = 9, n = 2:  (36, 77, 85)
   14 triples with hypotenuse up to 85, every one checked, from one formula.
   A brute-force search finds 14 with no common factor; the same ones: True.

7. WHERE STUDENTS SAY THEY WORKED, AND WHERE THEY SAY THEY MUST
   McGuire's Figure 4.5: 250 general chemistry students, 2013, after hearing
   about Bloom's (1956 names). Percent choosing each level:
   level              high school   college
   1. Knowledge               21%        7%   ##########         ###
   2. Comprehension           35%        6%   #################  ###
   3. Application             25%       14%   ############       #######
   4. Analysis                13%       35%   ######             #################
   5. Synthesis                3%       23%   #                  ###########
   6. Evaluation               3%       15%   #                  #######
   high school  average level 2.51, at level 4 or above: 19%
   college      average level 4.06, at level 4 or above: 73%
   Two questions moved the answer by one and a half levels: most had done well
   by remembering and understanding, and saw that they would now need to analyze.

WHAT CHANGED ON THE WAY UP
   Level 1 stored three triples. Level 6 stores one formula and re-creates
   those three and 11 more, on demand. A student who forgets the 'whats'
   at level 6 can rebuild them; one who forgets them at level 1 has nothing.
```
<!-- /output -->

## Questions

**1. What is McGuire's distinction between studying and learning, in the dental student's words?**

<details><summary>Answer</summary>

Studying focuses on the "whats"; learning focuses on the "hows", "whys" and "what ifs". If you forget a what, you cannot re-create it; if you understand the hows and whys, you can.

</details>

**2. Name Bloom's six levels, bottom to top. What changed from the 1956 version?**

<details><summary>Answer</summary>

Remembering, understanding, applying, analyzing, evaluating, creating. In 1956 they were nouns (Knowledge, Comprehension, Application, Analysis, Synthesis, Evaluation), and evaluation was at the top; the 2001 revision put creating (the old synthesis) above it.

</details>

**3. "Find the height a 13 m ladder reaches 5 m from the wall." Which level?**

<details><summary>Answer</summary>

Applying: using the theorem on a problem you had not seen in that form.

</details>

**4. "Is every right triangle with whole sides a multiple of 3-4-5?" Which level, and what is the answer?**

<details><summary>Answer</summary>

Evaluating: judging a claim with evidence. False; 5-12-13 is a counterexample.

</details>

**5. Use Euclid's formula with m = 4, n = 1. Check that the result is a right triangle.**

<details><summary>Answer</summary>

m² − n² = 15, 2mn = 8, m² + n² = 17. And 8² + 15² = 64 + 225 = 289 = 17².

</details>

**6. Why would you work harder to teach the class than to get an A?**

<details><summary>Answer</summary>

A test asks the questions on it; a class asks any question. To be ready for questions you cannot foresee, you need the hows and whys, not just the answers.

</details>

**7. If you never explain the material to anyone, when do you find out that you did not understand it?**

<details><summary>Answer</summary>

"On the test!", as McGuire's workshop groups answer. Explaining it, even to an empty chair, moves that discovery to a time when you can still fix it.

</details>

**8. A student says "studying is when I go over what I learned in class". What does McGuire's reaction suggest is wrong with that?**

<details><summary>Answer</summary>

It assumes the learning already happened in class, so "going over it" the night before seems enough. Hearing something explained is at best level 2; the levels above have to be reached by working on it yourself.

</details>

## How to practise

1. **Ask McGuire's step 4 about every topic**: at what level have I been working, and at what level will the test ask?
2. **Write one question per level** for the lesson you are studying, then answer them. Levels 4 to 6 are the ones you will be tempted to skip.
3. **Switch to teach-the-material mode.** Explain the page to a friend, a pet or an empty chair, list the questions a class would ask, and note where you got stuck: that is where you were still at level 1.
4. **When you catch yourself memorising a list, look for what produces it**, the way Euclid's formula produces the triples.

## Flashcards

The page as a deck of Anki cards: [`studying_vs_learning.txt`](anki/studying_vs_learning.txt). Import with File → Import. Tags: `definition`, `bloom`, `pythagoras`, `trap`.

## Po polsku, w skrócie

Saundra McGuire pyta studentów, czym różni się „uczenie się do egzaminu" (studying) od „nauczenia się" (learning). Najlepsza odpowiedź, jaką usłyszała: wkuwanie to skupianie się na „co", a uczenie się to skupianie się na „jak", „dlaczego" i „co by było, gdyby". Kto zna tylko fakty, a je zapomni, nie ma z czego ich odtworzyć. Kto rozumie, skąd się biorą, odtworzy je sam.

Taksonomia Blooma (w wersji Andersona i Krathwohla z 2001 roku) ma sześć poziomów: zapamiętywanie, rozumienie, stosowanie, analizowanie, ocenianie i tworzenie. Program przechodzi przez wszystkie na jednym twierdzeniu Pitagorasa: od wyrecytowania wzoru, przez wyjaśnienie, dlaczego jest prawdziwy, zadanie z drabiną i podział trójkątów na prostokątne, ostrokątne i rozwartokątne, aż po wzór Euklidesa, który wytwarza wszystkie trójki pitagorejskie. Trzy trójki, których student uczyłby się na pamięć, wychodzą z tego wzoru same, razem z jedenastoma innymi.

Pytanie kontrolne McGuire: czy bardziej byś się starał, żeby dostać piątkę, czy żeby wytłumaczyć materiał całej klasie? Większość wybiera tłumaczenie, bo wtedy trzeba przewidzieć pytania i umieć wyjaśnić rzecz na kilka sposobów. A kiedy odkryjesz, że czegoś nie rozumiesz, jeśli nikomu tego nie tłumaczysz? „Na egzaminie!". Klasa nie jest potrzebna: wystarczą puste krzesła, pluszaki albo pies.

## See also

- [Count the vowels](../count_the_vowels/README.md) — the lesson before: the task decides what you remember
- [Spaced retrieval](../spaced_retrieval/README.md) — the lesson after: keeping what you learned, and McGuire's study cycle for climbing these levels
- [The Pythagorean theorem and its converse](../../10_Geometry/pythagorean_theorem/README.md) — the theorem this page climbs, taught in full
- [If A then B](../../11_Logic/converse_and_contrapositive/README.md) — evaluating a claim: one counterexample disproves it
- [Resources](../../RESOURCES.md) — the books behind this chapter
- Saundra Yancy McGuire with Stephanie McGuire, *Teach Yourself How to Learn* (Stylus, 2018), chapter 4 and Figure 4.1
- Lorin W. Anderson and David R. Krathwohl (eds.), *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives* (Longman, 2001)
- [Bloom's taxonomy ↗](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy) and [Pythagorean triple ↗](https://en.wikipedia.org/wiki/Pythagorean_triple) — Wikipedia
- [Taksonomia Blooma ↗](https://pl.wikipedia.org/wiki/Taksonomia_Blooma) — Wikipedia po polsku
