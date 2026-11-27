# -*- coding: utf-8 -*-
"""Stage 9 · Unit 1 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u07 import F
from .s8_u01 import SQR

K = lambda s: f"$${s}$$"

VIDEOS = {}

VIDEOS["1.1"] = [
    dict(kind="hook", title="A square patio", steps=[
        dict(say="A square patio must have an area of exactly 20 square metres. So each side is the square root of 20 metres.",
             do=[E("🧱", 90, 170, 100), T("area **20 m²** → side = **√20 m**", x=230, y=200), SQR("20 m²", 220, 860, 140, at=1)]),
        dict(say="A calculator shows 4.472135955, and the digits keep going.", do=[MATH("√20 = 4.472135955…", x=230, y=300)]),
        PAUSE("1.1-k1", "Can the square root of 20 be written exactly as a fraction? Pause the video and decide.", "Is √20 a fraction?"),
    ]),
    dict(kind="hook", title="Not a fraction", steps=[
        dict(say="No. 20 is not a square number, so its square root can never be written as a fraction. Its digits go on forever, with no repeating pattern.",
             do=[B("√20 is not a fraction", x=80, y=190, color=GREEN), T("digits go on forever, **no pattern**", x=80, y=300)]),
        dict(say="Numbers like this are called irrational numbers.", do=[T("→ an **irrational** number", x=80, y=380, color=BLUE)]),
    ]),
    dict(kind="recall", title="Squares and cubes", steps=[
        dict(say="Remember the square numbers: 1, 4, 9, 16, 25, 36, 49, 64, 81 and 100.", do=[MATH("1, 4, 9, 16, 25, 36, 49, 64, 81, 100", x=80, y=180)]),
        dict(say="And the cube numbers: 1, 8, 27, 64, 125 and 216. So the cube root of 125 is 5.", do=[MATH("1, 8, 27, 64, 125, 216", x=80, y=280), MATH("∛125 = 5", x=80, y=380, color=GREEN, at=4)]),
    ]),
    dict(kind="idea", title="Rational and irrational", steps=[
        dict(say="A rational number can be written as a fraction of two integers. Integers, fractions, terminating decimals and recurring decimals are all rational.",
             do=[T("**rational**: a fraction of two integers", x=80, y=170), MATH(f"0.45 = {F(9, 20)}   ·   0.4545… = {F(5, 11)}", x=80, y=250, at=5)]),
        dict(say="An irrational number cannot be written as a fraction. Its decimal goes on forever, without repeating. The square root of 3, the cube root of 10, and pi are irrational.",
             do=[T("**irrational**: never ends, **never repeats**", x=80, y=360, color=RED), MATH("√3,  ∛10,  π", x=80, y=440, at=6)]),
        PAUSE("1.1-k2", "Your turn. Is pi rational or irrational? Pause the video and choose.", "π is …"),
    ]),
    dict(kind="idea", title="Check: π", steps=[
        dict(say="Pi is irrational. It is 3.14159, and its digits never end and never repeat. 22 sevenths is only an estimate of pi.",
             do=[B("π is irrational", x=80, y=190, color=GREEN), MATH(f"π = 3.14159…   {F(22, 7)} is only an estimate", x=80, y=300)]),
        dict(say="The square root of a whole number is either a whole number, like the square root of 36, or it is irrational, like the square root of 20. An irrational root is called a surd.",
             do=[MATH("√36 = 6   ·   √20 is irrational", x=80, y=400), T("an irrational root = a **surd**", x=80, y=480, color=BLUE, at=6)]),
    ]),
    dict(kind="idea", title="Estimating roots", steps=[
        dict(say="To estimate a root, find the square numbers on either side. 20 is between 16 and 25, so the square root of 20 is between 4 and 5, nearer 4.",
             do=[TBL(["Root", "Between", "Estimate"], [["√20", "√16 = 4 and √25 = 5", "about 4.5"], ["∛40", "∛27 = 3 and ∛64 = 4", "about 3.4"]], y=180), ROW(0, 1)]),
        dict(say="For a cube root, use cube numbers. 40 is between 27 and 64, so the cube root of 40 is between 3 and 4.", do=[ROW(1, 0.4)]),
    ]),
    dict(kind="method", title="How do I decide and estimate?", steps=[
        dict(say="Here is the method. Step 1: can the number be written as a fraction of integers? Terminating and recurring decimals are rational.", do=[T("1. A **fraction** of integers? → rational", x=80, y=170)]),
        dict(say="Step 2: for a square root or cube root, is the number a square or cube number? If not, the root is irrational.", do=[T("2. Not a square / cube number → root is **irrational**", x=80, y=260)]),
        dict(say="Step 3: find the square or cube numbers just below and just above.", do=[T("3. Squares / cubes **either side**", x=80, y=350)]),
        dict(say="Step 4: estimate between the two roots, nearer the closer one.", do=[T("4. Estimate, **nearer** the closer one", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Sorting numbers", steps=[
        dict(say="Sort these: 0.7, the square root of 81, the square root of 12, 2 ninths, and negative 5.", do=[MATH("0.7,  √81,  √12,  2/9,  −5", x=80, y=170)]),
        dict(say="0.7 is 7 tenths. The square root of 81 is 9. 2 ninths and negative 5 are rational too.", do=[T("rational: 0.7, √81 = 9, 2/9, −5", x=80, y=270, color=GREEN)]),
        dict(say="12 is not a square number, so the square root of 12 is the only irrational one.", do=[T("irrational: **√12**", x=80, y=360, color=RED)]),
    ]),
    dict(kind="example", title="Between two whole numbers", steps=[
        dict(say="Between which two whole numbers is the square root of 70? 64 is 8 squared, and 81 is 9 squared.", do=[MATH("8² = 64,  9² = 81", x=80, y=180)]),
        dict(say="70 is between 64 and 81, nearer 64. So the square root of 70 is between 8 and 9, a bit less than halfway.", do=[MATH("64 < 70 < 81", x=80, y=280), T("between **8 and 9**, nearer 8", x=80, y=370, at=4)]),
        PAUSE("1.1-k3", "Your turn. Is the square root of 70 closer to 8.4, or 8.9? Pause and choose.", "√70 is closest to … 8.4 or 8.9?"),
    ]),
    dict(kind="example", title="Check: √70", steps=[
        dict(say="Check by squaring. 8.4 squared is 70.56. 8.9 squared is 79.21. So the square root of 70 is about 8.4.",
             do=[MATH("8.4² = 70.56   ·   8.9² = 79.21", x=80, y=190), B("√70 ≈ 8.4", x=80, y=300, color=GREEN, at=6)]),
        dict(say="Surds can multiply to give rational numbers. The square root of 2, times the square root of 8, is the square root of 16, which is 4.", do=[MATH("√2 × √8 = √16 = 4", x=80, y=410)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Raj asks: is 0.272727, and so on, rational? Which line is wrong?", do=LINES("Raj", "is 0.2727… rational?", ["the decimal never ends", "so it is irrational"])),
        dict(say="Line 2 is wrong. The decimal never ends, but it repeats. Repeating decimals are rational.", do=[dict(a="cross", id="l2")]),
        dict(say="0.2727, and so on, is 27 ninety-ninths, which is 3 elevenths.", do=[B(f"0.2727… = {F(27, 99)} = {F(3, 11)}", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Square tiles", steps=[
        dict(say="The diagonal of a square tile with sides of 1 metre is the square root of 2 metres. That is irrational.",
             do=[E("🔲", 90, 170, 100), T("diagonal of a 1 m tile = **√2 m**", x=230, y=200)]),
        dict(say="A builder cannot measure it exactly, so they round it: about 1.414 metres.", do=[MATH("√2 ≈ 1.414 m", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("1.1-k4", "One last question. Is 0.333, and so on, rational or irrational? Pause the video and choose.", "0.333… is …"),
        dict(say="It is rational. It repeats, and it is equal to 1 third.", do=[B(f"0.333… = {F(1, 3)} → rational", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a rational number can be written as a fraction of integers. An irrational number cannot.", do=[T("• Rational = a fraction; irrational = not", x=80, y=170)]),
        dict(say="Roots of whole numbers that are not square or cube numbers are irrational surds.", do=[T("• Non-square roots are **surds**", x=80, y=250)]),
        dict(say="Estimate roots between known squares or cubes.", do=[T("• Estimate between squares / cubes", x=80, y=330)]),
        dict(say="Recurring decimals are rational.", do=[T("• Recurring decimals are rational", x=80, y=410)]),
    ]),
]

VIDEOS["1.2"] = [
    dict(kind="hook", title="Too many zeros", steps=[
        dict(say="Light travels about 300,000,000 metres every second. A red blood cell is about 0.000008 metres across.",
             do=[E("💡", 90, 170, 100), MATH("300 000 000 m every second", x=230, y=190), MATH("0.000 008 m across", x=230, y=280, at=4)]),
        dict(say="Writing all those zeros is slow, and easy to get wrong. There is a shorter way.", do=[T("a **shorter** way?", x=230, y=370)]),
        PAUSE("1.2-k1", "Is 300,000,000 equal to 3 times 10 to the power 8, or 3 times 10 to the power 9? Pause the video and choose.", "300 000 000 = 3 × 10⁸ or 3 × 10⁹?"),
    ]),
    dict(kind="hook", title="Count the places", steps=[
        dict(say="Start at 3, and move the decimal point 8 places to the right to get 300,000,000. So it is 3 times 10 to the power 8.",
             do=[MATH("3 → 300 000 000: 8 places", x=80, y=190), B("3 × 10⁸", x=80, y=300, color=GREEN, at=5)]),
    ]),
    dict(kind="recall", title="Powers of 10", steps=[
        dict(say="Remember: 10 cubed is 1,000. And 10 to the power negative 2 is 1 hundredth, which is 0.01.", do=[MATH("10³ = 1000", x=80, y=180), MATH(f"10⁻² = {F(1, 100)} = 0.01", x=80, y=280)]),
    ]),
    dict(kind="idea", title="Standard form", steps=[
        dict(say="A number in standard form is written as A times 10 to the power N. A is at least 1, and less than 10. N is an integer.",
             do=[B("A × 10ⁿ,  1 ≤ A < 10", x=80, y=170, color=BLUE)]),
        dict(say="Large numbers have a positive power. Small numbers, less than 1, have a negative power.",
             do=[TBL(["Ordinary", "Standard form"], [["52 000", "5.2 × 10⁴"], ["7 600 000", "7.6 × 10⁶"], ["0.034", "3.4 × 10⁻²"], ["0.000 905", "9.05 × 10⁻⁴"]], y=260), ROW(0, 1), ROW(1, 2), ROW(2, 4), ROW(3, 5)]),
        PAUSE("1.2-k2", "Your turn. Write 8 times 10 to the power negative 6 as an ordinary number. Pause the video and try it.", "8 × 10⁻⁶ as an ordinary number?"),
    ]),
    dict(kind="idea", title="Check: 8 × 10⁻⁶", steps=[
        dict(say="A negative power makes a small number. Move the point 6 places to the left: 0.000008. That is the red blood cell.",
             do=[B("8 × 10⁻⁶ = 0.000 008", x=80, y=190, color=GREEN)]),
        dict(say="To compare numbers in standard form, compare the powers first. Then compare the values of A.", do=[T("compare the **powers** first, then A", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I write a number in standard form?", steps=[
        dict(say="Here is the method. Step 1: put the point after the first non-zero digit. That gives A.", do=[T("1. Point after the **first non-zero digit** → A", x=80, y=170)]),
        dict(say="Step 2: count how many places the point has moved.", do=[T("2. **Count** the places moved", x=80, y=260)]),
        dict(say="Step 3: a big number gets a positive power. A number less than 1 gets a negative power.", do=[T("3. Big → **positive** power · less than 1 → **negative**", x=80, y=350)]),
        dict(say="Step 4: check, by changing it back to an ordinary number.", do=[T("4. **Check** by converting back", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A small number", steps=[
        dict(say="Write 0.00052 in standard form. Put the point after the 5: A is 5.2.", do=[MATH("0.000 52 → A = 5.2", x=80, y=170)]),
        dict(say="The point moved 4 places to the right, and the number is less than 1. So the power is negative 4.", do=[MATH("4 places, less than 1 → 10⁻⁴", x=80, y=270), B("5.2 × 10⁻⁴", x=80, y=370, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Not standard form", steps=[
        dict(say="Is 45 times 10 cubed in standard form? No, because 45 is not less than 10.", do=[MATH("45 × 10³", x=80, y=170), T("45 is **not** less than 10 ✗", x=80, y=260, color=RED)]),
        dict(say="45 is 4.5 times 10. So the number is 4.5 times 10 to the power 4.", do=[MATH("4.5 × 10¹ × 10³ = 4.5 × 10⁴", x=80, y=350, color=GREEN)]),
        PAUSE("1.2-k3", "Your turn. Which is in standard form: 1.2 times 10 to the power 5, or 12 times 10 to the power 4? Pause and choose.", "Which is in standard form? 1.2 × 10⁵ or 12 × 10⁴"),
    ]),
    dict(kind="example", title="Check: standard form", steps=[
        dict(say="1.2 times 10 to the power 5 is in standard form, because 1.2 is between 1 and 10. 12 is too big.",
             do=[B("1.2 × 10⁵ ✓", x=80, y=190, color=GREEN), T("12 × 10⁴ ✗  (12 is not less than 10)", x=80, y=300, color=RED)]),
    ]),
    dict(kind="example", title="Ordering", steps=[
        dict(say="Order these from smallest: 6 times 10 to the negative 3, 2.1 times 10 to the negative 2, and 9.9 times 10 to the negative 4.",
             do=[MATH("6 × 10⁻³,  2.1 × 10⁻²,  9.9 × 10⁻⁴", x=80, y=170)]),
        dict(say="Compare the powers first. Negative 4 is the smallest power, then negative 3, then negative 2.",
             do=[MATH("9.9 × 10⁻⁴ < 6 × 10⁻³ < 2.1 × 10⁻²", x=80, y=280, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Lin writes 0.006 in standard form. Which line is wrong?", do=LINES("Lin", "0.006 in standard form", ["A = 6", "the point moved 3 places", "6 × 10³"])),
        dict(say="Line 3 is wrong. 0.006 is less than 1, so the power must be negative.", do=[dict(a="cross", id="l3")]),
        dict(say="The answer is 6 times 10 to the power negative 3.", do=[B("6 × 10⁻³", x=110, y=470, color=GREEN)]),
    ]),
    dict(kind="life", title="Science and calculators", steps=[
        dict(say="Scientists use standard form for very big and very small things. A galaxy can be 10 to the power 21 metres across. An atom is about 10 to the power negative 10 metres.",
             do=[E("🔭", 90, 170, 100), MATH("galaxy ≈ 10²¹ m   ·   atom ≈ 10⁻¹⁰ m", x=230, y=200)]),
        dict(say="Calculators show standard form too. 3E8 on the screen means 3 times 10 to the power 8.", do=[MATH("3E8 = 3 × 10⁸", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("1.2-k4", "One last question. Which is bigger: 2 times 10 to the power 5, or 9 times 10 to the power 4? Pause the video and choose.", "Bigger: 2 × 10⁵ or 9 × 10⁴?"),
        dict(say="Compare the powers first. 10 to the power 5 is bigger. 2 times 10 to the power 5 is 200,000, but 9 times 10 to the power 4 is only 90,000.",
             do=[B("2 × 10⁵ = 200 000", x=80, y=190, color=GREEN), MATH("9 × 10⁴ = 90 000", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: standard form is A times 10 to the power N, with A at least 1 and less than 10.", do=[T("• A × 10ⁿ with 1 ≤ A < 10", x=80, y=170)]),
        dict(say="Large numbers have a positive power. Small numbers have a negative power.", do=[T("• Large → positive n · small → negative n", x=80, y=250)]),
        dict(say="Compare the powers first, then A.", do=[T("• Compare powers first, then A", x=80, y=330)]),
        dict(say="Check by converting back.", do=[T("• Check by converting back", x=80, y=410)]),
    ]),
]

VIDEOS["1.3"] = [
    dict(kind="hook", title="Folding paper", steps=[
        dict(say="Fold a sheet of paper in half, again and again. After 5 folds there are 2 to the power 5 layers, which is 32.",
             do=[E("📄", 90, 170, 100), MATH("2⁵ = 32 layers", x=230, y=190)]),
        dict(say="Now go backwards. Each unfold halves the number of layers: 32, 16, 8, 4, 2. What comes next?",
             do=[TBL(["2⁵", "2⁴", "2³", "2²", "2¹", "2⁰"], [["32", "16", "8", "4", "2", "?"]], y=280), ROW(0, 2)]),
        PAUSE("1.3-k1", "Halve 2 once more. What is 2 to the power 0? Pause the video and work it out.", "2⁰ = ?"),
    ]),
    dict(kind="hook", title="2⁰ = 1", steps=[
        dict(say="Half of 2 is 1. So 2 to the power 0 is 1. That is one sheet, with no folds.", do=[B("2⁰ = 1", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="recall", title="Powers", steps=[
        dict(say="Remember: 2 to the power 5 means five 2s multiplied together. 2 times 2 times 2 times 2 times 2 is 32.", do=[MATH("2⁵ = 2 × 2 × 2 × 2 × 2 = 32", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Zero and negative indices", steps=[
        dict(say="Keep going down. Each step divides by 2. So 2 to the power negative 2 is a quarter, and 2 to the power negative 3 is an eighth.",
             do=[TBL(["2⁻³", "2⁻²", "2⁻¹", "2⁰", "2¹", "2²", "2³"], [[F(1, 8), F(1, 4), "?", "1", "2", "4", "8"]], y=170), ROW(0, 1)]),
        dict(say="So A to the power 0 is 1, for any number A that is not zero. And A to the power negative N is 1 over A to the power N.",
             do=[B("a⁰ = 1   ·   " + K("a^{-n} = \\dfrac{1}{a^{n}}"), x=80, y=380, color=BLUE)]),
        PAUSE("1.3-k2", "Your turn. Write 2 to the power negative 1 as a decimal. Pause the video and try it.", "2⁻¹ as a decimal?"),
    ]),
    dict(kind="idea", title="Check: 2⁻¹", steps=[
        dict(say="2 to the power negative 1 is 1 over 2, which is a half. As a decimal, that is 0.5.", do=[B(f"2⁻¹ = {F(1, 2)} = 0.5", x=80, y=190, color=GREEN)]),
        dict(say="Another example: 5 to the power negative 2 is 1 over 25.", do=[MATH(f"5⁻² = {F(1, 25)}", x=80, y=310)]),
    ]),
    dict(kind="idea", title="Index laws", steps=[
        dict(say="With the same base, when you multiply, add the indices. 3 to the 4, times 3 squared, is 3 to the 6.", do=[MATH("3⁴ × 3² = 3⁶", x=80, y=170)]),
        dict(say="When you divide, subtract the indices. 7 to the 5, divided by 7 squared, is 7 cubed.", do=[MATH("7⁵ ÷ 7² = 7³", x=80, y=260)]),
        dict(say="These laws work with negative and zero indices too. But only when the bases are the same.", do=[T("only when the **bases are the same**", x=80, y=360, color=RED)]),
    ]),
    dict(kind="method", title="How do I use the index laws?", steps=[
        dict(say="Here is the method. Step 1: check that the bases are the same.", do=[T("1. **Same base**?", x=80, y=170)]),
        dict(say="Step 2: multiplying, add the indices. Dividing, subtract them.", do=[T("2. × → **add** · ÷ → **subtract**", x=80, y=260)]),
        dict(say="Step 3: take care with the signs of negative indices.", do=[T("3. Watch the **signs**", x=80, y=350)]),
        dict(say="Step 4: use A to the power 0 is 1, and A to the negative N is 1 over A to the N, to find a value.", do=[T("4. a⁰ = 1, a⁻ⁿ = 1/aⁿ", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Multiplying", steps=[
        dict(say="Simplify 5 cubed times 5 to the power negative 7. Add the indices: 3 plus negative 7 is negative 4.", do=[MATH("5³ × 5⁻⁷", x=80, y=170), MATH("3 + (−7) = −4", x=80, y=260)]),
        dict(say="The answer is 5 to the power negative 4.", do=[B("5⁻⁴", x=80, y=360, color=GREEN)]),
        PAUSE("1.3-k3", "Your turn. 3 to the 4, times 3 to the power negative 2, is 3 to what power? Pause and work it out.", "3⁴ × 3⁻² = 3ⁿ. n?"),
    ]),
    dict(kind="example", title="Check: 3⁴ × 3⁻²", steps=[
        dict(say="Add the indices. 4 plus negative 2 is 2. So it is 3 squared, which is 9.", do=[MATH("4 + (−2) = 2", x=80, y=190), B("3² = 9", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="example", title="Dividing", steps=[
        dict(say="Simplify 6 to the negative 2, divided by 6 to the negative 5. Subtract the indices: negative 2 minus negative 5 is 3.",
             do=[MATH("6⁻² ÷ 6⁻⁵", x=80, y=170), MATH("−2 − (−5) = 3", x=80, y=260)]),
        dict(say="The answer is 6 cubed.", do=[B("6³", x=80, y=360, color=GREEN)]),
    ]),
    dict(kind="example", title="A missing index", steps=[
        dict(say="8 to the 4, times 8 to the power something, is 8 to the negative 1. Find the missing index.", do=[MATH("8⁴ × 8ⁿ = 8⁻¹", x=80, y=170)]),
        dict(say="4 plus the missing index is negative 1. So the missing index is negative 5.", do=[MATH("4 + ? = −1", x=80, y=260), B("? = −5", x=80, y=360, color=GREEN, at=4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Sam works out 4 to the power negative 2. Which line is wrong?", do=LINES("Sam", "4⁻²", ["4⁻² = −16"])),
        dict(say="Line 1 is wrong. A negative index does not make a negative number. It means 1 over.", do=[dict(a="cross", id="l1")]),
        dict(say="4 to the power negative 2 is 1 over 4 squared, which is 1 sixteenth.", do=[B(f"4⁻² = {F(1, 16)}", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Computer memory", steps=[
        dict(say="Computer memory comes in powers of 2. 2 to the power 10 bytes is 1,024 bytes, called a kibibyte.",
             do=[E("💾", 90, 170, 100), MATH("2¹⁰ = 1024 bytes", x=230, y=200)]),
        dict(say="And when a medicine halves in the body every few hours, the amount left uses powers of a half.", do=[MATH(f"amount × ({F(1, 2)})ⁿ", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("1.3-k4", "One last question. What is 7 to the power 0? Pause the video and answer.", "7⁰ = ?"),
        dict(say="Any number, except zero, to the power 0 is 1. So 7 to the power 0 is 1.", do=[B("7⁰ = 1", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: A to the power 0 is 1. A to the power negative N is 1 over A to the N.", do=[T("• a⁰ = 1 · a⁻ⁿ = 1/aⁿ", x=80, y=170)]),
        dict(say="Multiply: add the indices. Divide: subtract them.", do=[T("• × add · ÷ subtract", x=80, y=250)]),
        dict(say="The laws need the same base.", do=[T("• Same base only", x=80, y=330)]),
        dict(say="A negative index does not make a negative number.", do=[T("• Negative index ≠ negative number", x=80, y=410)]),
    ]),
]
