# Related rates

**Level:** 201 · for anyone who has met the derivative as a velocity and wants to use it on balloons, ladders and kites

**One line:** When two quantities are tied by an equation at every instant, their velocities are tied by the derivative of that equation; the one move in every related-rates problem is to differentiate the equation that holds *all the time*, and only then put in the numbers of the one instant you were asked about.

## The idea

Air goes into a spherical balloon at 2 cm³ every second. The volume grows at a steady rate. Does the radius?

It cannot. When the balloon is small, 2 cm³ spread over a small skin makes the radius jump; when it is large, the same 2 cm³ spread over a large skin barely moves it. The volume and the radius are tied at every instant by V = (4/3)πr³, and so their *velocities*, in the sense of [the derivative is a velocity](../derivative_as_velocity/README.md), are tied too. The tie between the velocities is found by asking how much V gains when r moves a little.

If r grows by a small Δr, the balloon gains a thin skin: about its surface times the thickness, 4πr² · Δr. (That is the [area and volume formulas](../../10_Geometry/area_and_volume_formulas/README.md) lesson's "the surface is what the volume gains per unit of radius".) Divide by the time Δt it took, and let Δt shrink:

> **dV/dt = 4πr² · dr/dt**

This holds at every instant. Now, and only now, put in the instant: dV/dt = 2 and r = 3 give 2 = 36π · dr/dt, so dr/dt = 1/(18π) ≈ 0.0177 cm per second. At r = 10 the same 2 cm³/s would move the radius only 0.0016 cm per second.

That is the whole method. Everything else is deciding which equation ties the quantities, which is the part no formula can do for you.

## Why the numbers go in last

Suppose you put r = 3 in first. Then V = (4/3)π · 27 = 36π, a constant, whose derivative is 0, and the problem says 2 = 0. That is not a small slip; the equation has lost its meaning. "r = 3" is true at one instant only, and an equation that holds at one instant has no velocity in it, because velocity is about how things change *between* nearby instants. Only an equation that holds at every instant can be differentiated. So: **differentiate first, then freeze the instant.**

The same goes for the ladder below. Its bottom is 15 ft from the wall at one moment; x = 15 is a snapshot. The equation that holds at every moment is x² + y² = 25², and that is the one to differentiate.

## The questions to answer on every problem

The problems on this page come from a Calculus I worksheet by Shalmali Bandyopadhyay (MATH 251, University of Tennessee at Martin). Her talk *Teaching and Mentoring in the Age of AI* explains why the worksheet gives no step-by-step procedure, does not name the technique above each problem, and asks students to draw every picture themselves: "drawing the picture is step one", and handing over the procedure "is handing over the course". What it gives instead is a set of questions to answer on every example, and this page does the same.

For every problem, **draw it first**, label every quantity, then answer:

1. What quantities appear?
2. Which are changing?
3. Which are fixed?
4. What rate is given?
5. What rate is requested?
6. Should the requested rate be positive or negative?
7. What equation relates the quantities?

and, for some of them, *will the requested rate stay the same as time passes?*

Question 6 is the one that catches mistakes: decide the sign from the picture *before* computing, and if the algebra disagrees, the algebra is wrong. Question 7 is the whole difficulty.

**The formulas you may use.** Everything else you differentiate yourself:

A = πr²  ·  V = (4/3)πr³  ·  S = 4πr²  ·  V = a³

## Examples

Try each one on paper, with a picture, before opening the answer. Radians throughout: only in [radians](../radians/README.md) is the derivative of sin equal to cos.

**Example 1.** The radius of a circle increases at 2 m/sec. How fast is the area increasing when the radius is 5 m?

<details><summary>Answers to the seven questions</summary>

1. The radius r and the area A. 2. Both. 3. Nothing. 4. dr/dt = 2 m/s. 5. dA/dt. 6. Positive: a growing circle gains area. 7. A = πr².

Differentiate: dA/dt = 2πr · dr/dt. Then r = 5: dA/dt = 2π · 5 · 2 = **20π ≈ 62.83 m²/s**.

</details>

**Example 2.** A spherical balloon is filled with air at 2 cm³/sec. How fast is the radius increasing when the radius is 3 cm?

<details><summary>Answers to the seven questions</summary>

1. The volume V and the radius r. 2. Both. 3. Nothing, though the rate dV/dt is constant. 4. dV/dt = 2 cm³/s. 5. dr/dt. 6. Positive. 7. V = (4/3)πr³.

Differentiate: dV/dt = 4πr² · dr/dt. Then 2 = 4π · 9 · dr/dt: **dr/dt = 1/(18π) ≈ 0.0177 cm/s**.

</details>

**Example 3.** The side of a cube increases at ½ m/sec. How fast is the volume increasing when the side is 4 m?

<details><summary>Answers to the seven questions</summary>

1. The side a and the volume V. 2. Both. 3. Nothing. 4. da/dt = ½ m/s. 5. dV/dt. 6. Positive. 7. V = a³.

dV/dt = 3a² · da/dt = 3 · 16 · ½ = **24 m³/s**.

</details>

**Example 4.** A kite is 80 ft above the ground and moves horizontally away from the person holding it at 5 ft/sec. How fast is the angle of elevation θ changing when the kite is 60 ft horizontally from the person?

<details><summary>Answers to the seven questions</summary>

1. The height (80), the horizontal distance x, the angle θ, and the string. 2. x, θ and the string. 3. The height, 80 ft. 4. dx/dt = 5 ft/s. 5. dθ/dt. 6. **Negative**: as the kite moves away, it sits lower in the sky. 7. The angle and the two legs are tied by tan θ = 80/x. The string is not needed.

Differentiate: sec²θ · dθ/dt = −(80/x²) · dx/dt. At x = 60 the string is 100 (a 3-4-5 triangle times 20), so sec²θ = (100/60)² = 25/9. Then dθ/dt = −(80 · 5/3600) · (9/25) = **−1/25 = −0.04 rad/s**.

</details>

**Example 5.** A balloon rises straight up at 4 ft/sec from a point 30 ft from an observer. How fast is the angle of elevation changing when the balloon is 40 ft high?

<details><summary>Answers to the seven questions</summary>

1. The distance to the lift-off point (30), the height y, the angle θ. 2. y and θ. 3. The 30 ft. 4. dy/dt = 4 ft/s. 5. dθ/dt. 6. Positive: the observer looks higher and higher. 7. tan θ = y/30.

sec²θ · dθ/dt = (1/30) · dy/dt. At y = 40 the line of sight is 50, so sec²θ = 25/9, and dθ/dt = (4/30) · (9/25) = **6/125 = 0.048 rad/s**.

Compare with Example 4: the same kind of triangle, but there the changing leg was *adjacent* to θ and here it is *opposite*, which is why one angle falls and the other rises.

</details>

**Example 6.** A 25-ft ladder leans against a wall. We push the bottom towards the wall at 1 ft/sec, starting 20 ft from the wall. How fast does the top move up the wall 5 seconds after we start pushing?

<details><summary>Answers to the seven questions</summary>

1. The ladder (25), the distance x of the bottom from the wall, the height y of the top. 2. x and y. 3. The ladder's length. 4. dx/dt = **−1** ft/s: x is *shrinking*, so its rate is negative. 5. dy/dt. 6. Positive: pushing the bottom in raises the top. 7. x² + y² = 25², by [Pythagoras](../../10_Geometry/pythagorean_theorem/README.md), because the wall meets the floor at a right angle.

Which instant? After 5 seconds the bottom has moved 5 ft, so x = 20 − 5 = 15, and then y = √(625 − 225) = 20. Working out *that* x is the hardest reasoning step in the problem.

Differentiate: 2x · dx/dt + 2y · dy/dt = 0, so dy/dt = −x · (dx/dt)/y = −15 · (−1)/20 = **3/4 ft/s**, upward.

Will it stay the same? No: see the Compare question.

</details>

**Example 7.** Two cyclists leave the same point at the same time, one riding east at 16 mph and the other north at 12 mph. How fast is the distance between them increasing after one hour?

<details><summary>Answers to the seven questions</summary>

1. The east distance x, the north distance y, the distance z between them. 2. All three. 3. Nothing is fixed, only the two speeds. 4. dx/dt = 16, dy/dt = 12. 5. dz/dt. 6. Positive. 7. x² + y² = z².

Differentiate: 2x · dx/dt + 2y · dy/dt = 2z · dz/dt. After one hour x = 16, y = 12, z = 20, so dz/dt = (16 · 16 + 12 · 12)/20 = **20 mph**.

Will it stay the same? Yes: see the Compare question.

</details>

**Compare.** Examples 6 and 7 both use x² + y² = z². What is different about them? Use that difference to explain why one requested rate stays the same as time passes and the other does not.

<details><summary>Answer</summary>

In Example 6 the hypotenuse is **fixed** (the ladder is 25 ft). As x shrinks, y must grow by less and less, so the top's speed x/y falls: 4/3 at the start, 3/4 after 5 s, about 0.25 after 14 s. In Example 7 **nothing** is fixed: every side grows in proportion (16t, 12t, 20t), so the triangle keeps its shape, it is always [similar](../../10_Geometry/congruent_and_similar_triangles/README.md) to 4-3-5, and z = 20t, whose rate is 20 at every moment. Section 5 of the program prints both, second by second.

</details>

## Practice

**P1.** The radius of a circle decreases at 1 ft/sec. How fast is the area decreasing when the radius is 6 ft?

**P2.** Air is pumped into a spherical balloon at 100 cm³/sec. How fast is the radius increasing when the radius is 10 cm?

**P3.** The volume of a cube decreases at 10 m³/sec. How fast is the side changing when the side is 2 m?

**P4.** A spherical snowball melts so that its volume decreases at 5 cm³/min. How fast is the radius decreasing when the radius is 4 cm?

<details><summary>Answers</summary>

P1: dA/dt = 2π · 6 · (−1) = −12π: decreasing at **12π ≈ 37.70 ft²/s**. P2: dr/dt = 100/(4π · 100) = **1/(4π) ≈ 0.0796 cm/s**. P3: da/dt = −10/(3 · 4) = **−5/6 ≈ −0.833 m/s**. P4: dr/dt = −5/(4π · 16) = −5/(64π): decreasing at **≈ 0.0249 cm/min**.

</details>

## Try at home

Set each one up the way the examples were set up, picture and seven questions, before solving it.

1. The radius of a sphere decreases at 3 m/sec. Find the rate at which the surface area decreases when the radius is 10 m.
2. The side of a cube decreases at 2 cm/sec. How fast is the volume decreasing when the side is 5 cm?
3. A 10-ft ladder leans against a wall. The bottom slides away from the wall at 1 ft/sec. How fast is the top sliding down when the bottom is 6 ft from the wall?
4. Two cars leave the same intersection at the same time, one driving south at 30 mph and the other west at 40 mph. How fast is the distance between them increasing after two hours?
5. Two airplanes fly at the same height, one east at 250 mi/h and the other north at 300 mi/h, both leaving the same point at the same time. How fast is the distance between them increasing after one hour?
6. A kite is 50 ft above the ground and moves horizontally away from the person holding it at 3 ft/sec. How fast is the angle of elevation changing when the kite is 120 ft horizontally from the person?
7. A 20-ft ladder leans against a wall. The bottom slides away from the wall at 2 ft/sec. How fast is the angle between the ladder and the ground changing when the bottom is 12 ft from the wall?
8. A balloon rises straight up at 6 ft/sec from a point 40 ft from an observer. How fast is the angle of elevation changing when the balloon is 30 ft high?
9. The radius of a circle increases at 4 cm/sec. How fast is the circumference increasing when the radius is 7 cm? Use C = 2πr.

<details><summary>Answers</summary>

1. dS/dt = 8πr · dr/dt = 8π · 10 · (−3): decreasing at **240π ≈ 753.98 m²/s**.
2. dV/dt = 3 · 25 · (−2): decreasing at **150 cm³/s**.
3. y = 8; dy/dt = −6 · 1/8 = **−3/4 ft/s**, sliding down at 0.75 ft/s.
4. After 2 h: 60 and 80, distance 100; dz/dt = (60 · 30 + 80 · 40)/100 = **50 mph**, and it stays 50.
5. After 1 h: 250 and 300, distance 50√61 ≈ 390.51; dz/dt = (250² + 300²)/(50√61) = **50√61 ≈ 390.51 mi/h**. The same number as the distance, because the distance is (50√61) · t.
6. tan θ = 50/x; at x = 120 the string is 130; dθ/dt = −(50 · 3/120²) · (120/130)² = **−3/338 ≈ −0.00888 rad/s**.
7. cos θ = x/20; at x = 12, y = 16 and sin θ = 4/5; −sin θ · dθ/dt = (1/20) · 2, so **dθ/dt = −1/8 rad/s**.
8. tan θ = y/40; at y = 30 the line of sight is 50; dθ/dt = (6/40) · (40/50)² = **12/125 = 0.096 rad/s**.
9. dC/dt = 2π · 4 = **8π ≈ 25.13 cm/s**, whatever the radius: the 7 cm is not needed, and noticing that is the point of the problem.

</details>

## What the program prints

The program is the answer key, and it does not trust its own algebra. Each answer is computed twice: once from the differentiated formula, and once with no calculus at all, by letting the motion run, measuring the asked-for quantity a millionth of a second before and after the instant, and dividing, which is what [a velocity is](../derivative_as_velocity/README.md). The two columns agreeing to six figures is the check that the differentiation was right.

<!-- output:related_rates -->
*Verified output of [`related_rates.py`](examples/related_rates.py) — regenerated by `tools/run_examples.py`, never hand-typed.*

```text
1. ONE EQUATION AT EVERY INSTANT, SO ONE EQUATION BETWEEN VELOCITIES
   Each formula, differentiated in t, checked at r = 3 (or a = 3, x = 3, y = 4)
   with every length growing at 1 unit per second:
                                                     formula     measured  unit     
   A = pi r^2        ->  2 pi r r'                 18.849556    18.849556  per sec  agree
   V = (4/3) pi r^3  ->  4 pi r^2 r'              113.097336   113.097336  per sec  agree
   S = 4 pi r^2      ->  8 pi r r'                 75.398224    75.398224  per sec  agree
   V = a^3           ->  3 a^2 a'                  27.000000    27.000000  per sec  agree
   C = 2 pi r        ->  2 pi r'                    6.283185     6.283185  per sec  agree
   z = sqrt(x^2+y^2) ->  (x x' + y y')/z            1.400000     1.400000  per sec  agree
   theta = atan(y/x) ->  (x y' - y x')/(x^2+y^2)    -0.040000    -0.040000  rad/sec  agree
   Each factor in front of r' is what the quantity gains per unit of r:
   4 pi r^2 is the sphere's surface, 2 pi r the circle's circumference.

2. CIRCLES, SPHERES AND CUBES
                                                     formula     measured  unit     
   circle r=5, r'=2: A' = 2 pi r r'                62.831853    62.831853  m^2/s    agree
   circle r=6, r'=-1: A' = 2 pi r r'              -37.699112   -37.699112  ft^2/s   agree
   balloon V'=2, r=3: r' = V'/(4 pi r^2)            0.017684     0.017684  cm/s     agree
   balloon V'=100, r=10: r' = V'/(4 pi r^2)         0.079577     0.079577  cm/s     agree
   snowball V'=-5, r=4: r' = V'/(4 pi r^2)         -0.024868    -0.024868  cm/min   agree
   cube a=4, a'=1/2: V' = 3 a^2 a'                 24.000000    24.000000  m^3/s    agree
   cube V'=-10, a=2: a' = V'/(3 a^2)               -0.833333    -0.833333  m/s      agree
   cube a=5, a'=-2: V' = 3 a^2 a'                -150.000000  -150.000000  cm^3/s   agree
   sphere r=10, r'=-3: S' = 8 pi r r'            -753.982237  -753.982237  m^2/s    agree
   circle r=7, r'=4: C' = 2 pi r'                  25.132741    25.132741  cm/s     agree
   Sphere with r' = 9: when do V and r grow at the same numerical rate?
   4 pi r^2 * 9 = 9 gives r^2 = 1/(4 pi), r = 0.282095 cm; there V' = 9.000000 = r'.
   Negative answers mean decreasing: the snowball's radius shrinks.

3. WHY THE NUMBERS GO IN LAST
   Balloon, r = 3. Put r = 3 in first: V = (4/3) pi 3^3 = 36 pi, a constant,
   and the derivative of a constant is 0. So 2 = 0: nonsense, not a small error.
   r = 3 is true at one instant only. An equation that holds for one instant
   has no velocity in it; only an equation that holds at every instant can be
   differentiated. Differentiate first, then freeze the instant.

4. LADDERS AND TWO TRAVELLERS
   x^2 + y^2 = L^2 at every instant, so 2x x' + 2y y' = 0, and y' = -x x'/y.
                                                     formula     measured  unit     
   ladder 25, pushed in at 1, x=15 (y=20)           0.750000     0.750000  ft/s     agree
   ladder 13, slides out at 2, x=5 (y=12)          -0.833333    -0.833333  ft/s     agree
   ladder 10, slides out at 1, x=6 (y=8)           -0.750000    -0.750000  ft/s     agree
   For two travellers leaving one point at right angles, z^2 = x^2 + y^2:
   cyclists E 16, N 12 mph, after 1 h              20.000000    20.000000  per hour agree
   cars S 30, W 40 mph, after 2 h                  50.000000    50.000000  per hour agree
   planes E 250, N 300 mi/h, after 1 h            390.512484   390.512484  per hour agree

5. WHICH RATE STAYS THE SAME? THE WORKSHEET'S 'COMPARE' QUESTION
   Ladder 25 pushed in at 1 ft/s from x = 20 (t in seconds), and the cyclists
   (t in hours, distance in miles):
        t  ladder x  top speed    cyclists apart   rate
        0        20     1.3333                 0     20
        2        18     1.0375                40     20
        5        15     0.7500               100     20
       10        10     0.4364               200     20
       14         6     0.2472               280     20
   The ladder's length is fixed, so as x shrinks the top slows: x/y falls from
   4/3 to 0.23. The cyclists' triangle keeps its shape (16t, 12t, 20t, always
   similar to 4-3-5), so the distance is 20t and its rate is 20 at every moment.

6. ANGLES
   theta' = (x y' - y x')/(x^2 + y^2), the angle's velocity seen from the corner.
                                                     formula     measured  unit     
   ladder 20, x=12, x'=2 (y=16)                    -0.125000    -0.125000  rad/s    agree
   ladder 15, x=9, x'=1 (y=12)                     -0.083333    -0.083333  rad/s    agree
   kite 80 up, x=60, x'=5                          -0.040000    -0.040000  rad/s    agree
   kite 50 up, x=120, x'=3                         -0.008876    -0.008876  rad/s    agree
   balloon 30 away, y=40, y'=4                      0.048000     0.048000  rad/s    agree
   balloon 40 away, y=30, y'=6                      0.096000     0.096000  rad/s    agree
   Exactly: the ladders -1/8 and -1/12, the kites -1/25 and -3/338,
   the balloons 6/125 and 12/125 radians per second. Radians, because
   lesson 3 showed that only in radians is the derivative of sin cos.

7. WHERE THE MODEL BREAKS: THE TOP OF A SLIDING LADDER
   Ladder 13 sliding out at 2 ft/s. The top's speed 2x/y, as y goes to 0:
     x = 5       y =  12.0000   top falls at       0.83 ft/s
     x = 12      y =   5.0000   top falls at       4.80 ft/s
     x = 12.9    y =   1.6093   top falls at      16.03 ft/s
     x = 12.99   y =   0.5098   top falls at      50.96 ft/s
     x = 12.999  y =   0.1612   top falls at     161.24 ft/s
   The formula promises unbounded speed at the floor. A real ladder leaves the
   wall before then; the equation x^2 + y^2 = 169 stops describing it.
```
<!-- /output -->

Section 7 is a warning about models. The formula says the top of a sliding ladder falls faster and faster as it nears the floor, without limit. A real ladder leaves the wall long before that; the equation x² + y² = 13² describes the ladder only while its top touches the wall.

## Questions

**1. Why must you differentiate before substituting the numbers of the instant?**

<details><summary>Answer</summary>

The numbers hold at one instant only. Put them in first and the equation becomes a relation between constants, whose derivative is 0 = 0, or 2 = 0. Only an equation true at every instant says how the quantities change together.

</details>

**2. The balloon's volume grows at a constant rate. Why doesn't the radius?**

<details><summary>Answer</summary>

dr/dt = (dV/dt)/(4πr²): the same added volume is spread over a skin that grows with r², so the radius slows down as the balloon grows.

</details>

**3. In Example 6, why is dx/dt equal to −1 and not 1?**

<details><summary>Answer</summary>

x is the distance from the wall, and pushing the ladder towards the wall makes x smaller. A quantity that is decreasing has a negative rate. Getting this sign wrong gives the top moving *down*, which the picture says is impossible: that is what question 6 is for.

</details>

**4. In Try at home 9, the radius 7 cm is given but not needed. Why?**

<details><summary>Answer</summary>

C = 2πr is linear in r, so dC/dt = 2π · dr/dt with no r left in it. The circumference grows at 8π cm/s at every radius. A problem that gives more than you need is testing whether you know what you need.

</details>

**5. In Example 4, why is the length of the kite string not in the equation?**

<details><summary>Answer</summary>

Only θ and x are changing and asked about, and tan θ = 80/x ties them directly. The string is useful afterwards, to find sec θ at the instant, but it does not have to be a variable.

</details>

**6. Two quantities are tied by x² + y² = 169, and x is increasing. Must y be decreasing?**

<details><summary>Answer</summary>

While both are positive, yes: x · dx/dt + y · dy/dt = 0, so dy/dt = −x · (dx/dt)/y has the opposite sign to dx/dt. That is the ladder sliding: bottom out, top down.

</details>

**7. The factor in dV/dt = 4πr² · dr/dt is the sphere's surface. Coincidence?**

<details><summary>Answer</summary>

No. Growing the radius by Δr adds a skin of volume about (surface) × Δr, so the surface is exactly what the volume gains per unit of radius. The same holds for the circle: dA/dt = (circumference) × dr/dt.

</details>

**8. Why are the angle rates in radians per second and not degrees per second?**

<details><summary>Answer</summary>

The derivative of tan θ is sec²θ, and of sin θ is cos θ, only when θ is in radians. In degrees every one of them picks up a factor π/180. To report degrees, compute in radians and convert at the end: −0.04 rad/s ≈ −2.29°/s.

</details>

## How to practise

1. **Picture first, every time, and label every quantity with a letter**, the fixed ones with their numbers and the changing ones with a letter only.
2. **Answer the seven questions in writing**, including the sign, before any calculus.
3. **Differentiate, then substitute.** Circle the line where the numbers go in; it must come after the derivative.
4. **Check the sign against your answer to question 6**, and the units: a rate of an area is in square units per second.
5. **The cards**, `trap` first.

## Flashcards

The page as a deck of Anki cards: [`related_rates.txt`](anki/related_rates.txt). Import with File → Import. Tags: `idea`, `questions`, `formulas`, `problems`, `trap`.

## Where this goes next

The chain rule in general, which this page uses in the form "d/dt of r³ is 3r² · dr/dt", is on the [roadmap](../../ROADMAP.md). The next topic of a Calculus I course is usually linear approximation, which is the same "small step Δr changes V by about 4πr² Δr" read the other way round.

## Po polsku, w skrócie

Gdy dwie wielkości są związane równaniem w każdej chwili, ich prędkości zmian też są związane: pochodną tego równania po czasie. Balon: V = (4/3)πr³, więc dV/dt = 4πr² · dr/dt. Czynnik 4πr² to pole powierzchni kuli, bo o tyle rośnie objętość na jednostkę promienia. Cała metoda to: znaleźć równanie prawdziwe w każdej chwili, zróżniczkować je po t, i dopiero wtedy wstawić liczby z tej jednej chwili, o którą pytają. Wstawienie liczb wcześniej zamienia równanie w związek między stałymi i daje bzdurę w rodzaju 2 = 0.

Zadania pochodzą z karty pracy Shalmali Bandyopadhyay, która celowo nie podaje gotowej procedury: rysunek i odpowiedź na siedem pytań (jakie wielkości, które się zmieniają, które są stałe, jaka prędkość jest dana, jakiej szukamy, jaki powinna mieć znak, jakie równanie je wiąże) to właśnie ta część myślenia, której trzeba się nauczyć. Znak warto przewidzieć z rysunku przed rachunkiem. Program liczy każdą odpowiedź dwa razy: ze wzoru i bez rachunku różniczkowego, mierząc ruch w odstępie milionowej części sekundy.

## Auf Deutsch: Stichwörter

Verkettete Änderungsraten: erst ableiten, dann einsetzen; Ballon, Leiter, Drachen und Höhenwinkel.

**Stichwörter:** verkettete Änderungsraten (related rates), Kettenregel, implizites Differenzieren, Änderungsrate, Leiteraufgabe, Volumen und Oberfläche.

## See also

- [The derivative is a velocity](../derivative_as_velocity/README.md) — what dV/dt means, and how the program measures it
- [Area and volume formulas](../../10_Geometry/area_and_volume_formulas/README.md) — the formulas, and the skin that makes 4πr² the rate of (4/3)πr³
- [The Pythagorean theorem and its converse](../../10_Geometry/pythagorean_theorem/README.md) — the equation of every ladder and every pair of travellers
- [Congruent and similar triangles](../../10_Geometry/congruent_and_similar_triangles/README.md) — why the cyclists' rate never changes
- [Radians](../radians/README.md) — why the angles are in radians
- [Related rates, Paul's Online Notes ↗](https://tutorial.math.lamar.edu/Classes/CalcI/RelatedRates.aspx) — more worked problems
- [Pochodna funkcji ↗](https://pl.wikipedia.org/wiki/Pochodna_funkcji) — Wikipedia po polsku
- Shalmali Bandyopadhyay, *MATH 251 Calculus I, Day 23: Word Problems on Related Rates* (University of Tennessee at Martin, Fall 2026), the source of every problem here, and her MAA webinar *Teaching and Mentoring in the Age of AI* (2026), the source of the page's design
