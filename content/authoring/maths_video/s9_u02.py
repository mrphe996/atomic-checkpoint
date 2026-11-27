# -*- coding: utf-8 -*-
"""Stage 9 · Unit 2 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u07 import F

K = lambda s: f"$${s}$$"

VIDEOS = {}

VIDEOS["2.1"] = [
    dict(kind="hook", title="Braking distance", steps=[
        dict(say="A driving app estimates braking distance in metres with the expression v squared over 20, plus v over 3. Here v is the speed in kilometres per hour.",
             do=[E("🚗", 90, 170, 100), MATH(K("\\dfrac{v^2}{20} + \\dfrac{v}{3}"), x=230, y=170)]),
        dict(say="Engineers test it with different values of v.", do=[T("test it with values of **v**", x=230, y=320)]),
        PAUSE("2.1-k1", "What is its value when v is 30? Pause the video and work it out.", "Value of v²/20 + v/3 at v = 30?"),
    ]),
    dict(kind="hook", title="v = 30", steps=[
        dict(say="30 squared is 900, and 900 over 20 is 45. 30 over 3 is 10. So the braking distance is 45 plus 10, which is 55 metres.",
             do=[MATH("900 ÷ 20 + 30 ÷ 3 = 45 + 10", x=80, y=190), B("55 m", x=80, y=300, color=GREEN, at=6)]),
        dict(say="If someone types negative 30 by mistake, v squared is still 900, but v over 3 is negative 10. The app gives 35, which makes no sense.", do=[MATH("v = −30 → 45 − 10 = 35 ✗", x=80, y=400, color=RED)]),
    ]),
    dict(kind="recall", title="Order of operations", steps=[
        dict(say="Remember the order of operations: brackets, then indices, then multiply and divide, then add and subtract.", do=[B("brackets → indices → × ÷ → + −", x=80, y=190, color=BLUE)]),
    ]),
    dict(kind="idea", title="Negatives and powers", steps=[
        dict(say="Replace each letter by its value in brackets. Then follow the order of operations.", do=[T("put each value **in brackets**", x=80, y=170)]),
        dict(say="Take care when a value is negative. When A is negative 3, negative A squared is negative 9, because only the 3 is squared. And A cubed is negative 27.",
             do=[TBL(["Expression", "a = −3"], [["−a²", "−(3²) = −9"], ["a³", "(−3)³ = −27"]], y=250), ROW(0, 3), ROW(1, 7)]),
        PAUSE("2.1-k2", "Your turn. What is negative 3, all squared? Pause the video and try it.", "(−3)² = ?"),
    ]),
    dict(kind="idea", title="Check: (−3)²", steps=[
        dict(say="Negative 3 times negative 3 is positive 9. A negative number squared is always positive.", do=[B("(−3)² = 9", x=80, y=190, color=GREEN)]),
        dict(say="A counter-example is one case that shows a statement is false. N squared is always bigger than N? No: when N is 0.5, N squared is only 0.25.",
             do=[T("**counter-example**: one case that proves it false", x=80, y=300), MATH("0.5² = 0.25 < 0.5", x=80, y=380, at=6)]),
    ]),
    dict(kind="method", title="How do I substitute safely?", steps=[
        dict(say="Here is the method. Step 1: write the expression, with each letter replaced by its value in brackets.", do=[T("1. Values **in brackets**", x=80, y=170)]),
        dict(say="Step 2: work out the powers first. Take care with negative signs.", do=[T("2. **Powers** first – watch the signs", x=80, y=260)]),
        dict(say="Step 3: then multiply and divide, then add and subtract.", do=[T("3. Then × ÷, then + −", x=80, y=350)]),
        dict(say="Step 4: ask yourself: is the answer sensible?", do=[T("4. Is it **sensible**?", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Powers", steps=[
        dict(say="Find 3 X squared, minus 2 Y cubed, when X is negative 4 and Y is 2.", do=[MATH("3x² − 2y³,  x = −4, y = 2", x=80, y=170)]),
        dict(say="3 times negative 4, all squared, is 3 times 16, which is 48. 2 times 2 cubed is 2 times 8, which is 16. 48 minus 16 is 32.",
             do=[MATH("3(−4)² = 3 × 16 = 48", x=80, y=260), MATH("2(2)³ = 16", x=80, y=340, at=5), B("48 − 16 = 32", x=80, y=430, color=GREEN, at=8)]),
        PAUSE("2.1-k3", "Your turn. What is X cubed when X is negative 2? Pause and work it out.", "x³ at x = −2?"),
    ]),
    dict(kind="example", title="Check: (−2)³", steps=[
        dict(say="Negative 2 times negative 2 is 4. 4 times negative 2 is negative 8. A negative number cubed stays negative.", do=[B("(−2)³ = −8", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="example", title="A fraction", steps=[
        dict(say="Find P plus Q, over P minus Q, when P is 7 and Q is negative 3. The top is 7 plus negative 3, which is 4. The bottom is 7 minus negative 3, which is 10.",
             do=[MATH(K("\\dfrac{p + q}{p - q}") + "  p = 7, q = −3", x=80, y=170), MATH("top 4, bottom 10", x=80, y=300, at=7)]),
        dict(say="4 over 10 is 0.4.", do=[B("0.4", x=80, y=400, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ella finds 2 X squared when X is negative 5. Which line is wrong?", do=LINES("Ella", "2x² when x = −5", ["2 × −5 = −10", "(−10)² = 100"])),
        dict(say="Line 1 is wrong. Indices come before multiplying. Square the negative 5 first.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="Negative 5 squared is 25, and 2 times 25 is 50.", do=[B("2 × (−5)² = 2 × 25 = 50", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Testing apps", steps=[
        dict(say="Spreadsheets and apps substitute values into formulae millions of times a day.", do=[E("💻", 90, 170, 100), T("formulae run **millions** of times", x=230, y=200)]),
        dict(say="Engineers test them with negative, zero and huge inputs, to make sure the answers are always sensible.", do=[T("test negative, zero and huge values", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.1-k4", "One last question. What is negative X squared, when X is 4? Pause the video and answer.", "−x² at x = 4?"),
        dict(say="Only X is squared. 4 squared is 16, and the negative sign makes it negative 16.", do=[B("−(4²) = −16", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: substitute values in brackets.", do=[T("• Substitute **in brackets**", x=80, y=170)]),
        dict(say="A negative number squared is positive. Cubed, it is negative.", do=[T("• (−a)² positive · (−a)³ negative", x=80, y=250)]),
        dict(say="Indices come before multiplying and dividing, then adding and subtracting.", do=[T("• Indices, then × ÷, then + −", x=80, y=330)]),
        dict(say="One counter-example proves a statement is false.", do=[T("• One counter-example disproves", x=80, y=410)]),
    ]),
]

VIDEOS["2.2"] = [
    dict(kind="hook", title="Concert tickets", steps=[
        dict(say="Adult tickets cost A dollars, and child tickets cost C dollars. A family buys 2 adult tickets and 3 child tickets, and pays with a 100 dollar note.",
             do=[E("🎫", 90, 170, 100), T("adult **$a** · child **$c** · pays with **$100**", x=230, y=200)]),
        PAUSE("2.2-k1", "Is the change 100 minus, bracket, 2A plus 3C? Or 100 minus 2A plus 3C? Pause the video and choose.", "The change is … 100 − (2a + 3c) or 100 − 2a + 3c?"),
    ]),
    dict(kind="hook", title="Use a bracket", steps=[
        dict(say="The whole cost is 2A plus 3C. The change takes all of it away from 100, so it needs a bracket: 100 minus, bracket, 2A plus 3C.",
             do=[MATH("cost = 2a + 3c", x=80, y=180), B("change = 100 − (2a + 3c)", x=80, y=290, color=GREEN, at=5)]),
    ]),
    dict(kind="recall", title="Collecting like terms", steps=[
        dict(say="Remember: collect like terms to simplify. 3 X plus 2 Y minus X is 2 X plus 2 Y.", do=[MATH("3x + 2y − x = 2x + 2y", x=80, y=190)]),
    ]),
    dict(kind="idea", title="From words to algebra", steps=[
        dict(say="Turn each phrase into an operation. Use a bracket when a whole quantity is multiplied, divided, or squared.",
             do=[TBL(["Words", "Expression"], [["cost of 2 adults and 3 children", "2a + 3c"], ["10% off that cost", "0.9(2a + 3c)"], ["the square of n more than m", "(m + n)²"], ["mean of x, y and z", "(x + y + z) ÷ 3"]], y=170), ROW(0, 1), ROW(1, 3), ROW(2, 5), ROW(3, 7)]),
        PAUSE("2.2-k2", "Your turn. Write an expression for the mean of A and B. Pause the video and try it.", "Mean of a and b?"),
    ]),
    dict(kind="idea", title="Check: the mean", steps=[
        dict(say="Add them, then divide by how many there are. The mean of two numbers is their total, in a bracket, divided by 2.", do=[B(K("\\dfrac{a + b}{2}"), x=80, y=180, color=GREEN)]),
        dict(say="Always say what the letters stand for, and check with a number.", do=[T("say what the letters **mean**, and test a number", x=80, y=340)]),
    ]),
    dict(kind="method", title="How do I construct an expression?", steps=[
        dict(say="Here is the method. Step 1: choose letters for the unknowns, and say what they mean.", do=[T("1. **Define** the letters", x=80, y=170)]),
        dict(say="Step 2: turn each phrase into an operation.", do=[T("2. Phrase → **operation**", x=80, y=260)]),
        dict(say="Step 3: use brackets for a total, or a sum, that is operated on.", do=[T("3. **Brackets** for whole quantities", x=80, y=350)]),
        dict(say="Step 4: simplify, then test with a simple number.", do=[T("4. Simplify, then **test**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Ages", steps=[
        dict(say="Ali is X years old. His sister is 3 years younger, and his father is 4 times Ali's age. Write the total of their ages.", do=[T("Ali **x** · sister **x − 3** · father **4x**", x=80, y=170)]),
        dict(say="X, plus X minus 3, plus 4 X. Collect like terms: 6 X minus 3.", do=[MATH("x + (x − 3) + 4x", x=80, y=270), B("6x − 3", x=80, y=370, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="A rectangle", steps=[
        dict(say="A rectangle has sides of X plus 4, and 2 X. Its perimeter is two of each side.", do=[T("sides **x + 4** and **2x**", x=80, y=170)]),
        PAUSE("2.2-k3", "Your turn. Write the perimeter, and simplify it. Pause and work it out.", "Perimeter of a rectangle with sides x + 4 and 2x?"),
    ]),
    dict(kind="example", title="Check: perimeter", steps=[
        dict(say="2 lots of X plus 4 is 2 X plus 8. 2 lots of 2 X is 4 X. Altogether, 6 X plus 8.", do=[MATH("2(x + 4) + 2(2x) = 2x + 8 + 4x", x=80, y=190), B("6x + 8", x=80, y=300, color=GREEN, at=6)]),
        dict(say="Test with X equals 1. The sides are 5 and 2, so the perimeter is 14. And 6 plus 8 is 14. It works.", do=[MATH("x = 1: 5 + 2 + 5 + 2 = 14 ✓", x=80, y=400)]),
    ]),
    dict(kind="example", title="A percentage", steps=[
        dict(say="A price of P dollars goes up by 15 percent. The multiplier is 1.15, so the new price is 1.15 P.", do=[MATH("+15% → × 1.15", x=80, y=180), B("1.15P", x=80, y=290, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ben writes: the total of A and B, divided by 4. Which line is wrong?", do=LINES("Ben", "the total of a and b, divided by 4", ["a + b ÷ 4"])),
        dict(say="Line 1 is wrong. Only B would be divided by 4. The total needs a bracket.", do=[dict(a="cross", id="l1")]),
        dict(say="It should be the bracket A plus B, all divided by 4.", do=[B("(a + b) ÷ 4", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Online shopping", steps=[
        dict(say="Online shops build expressions to price your basket. 10 percent off 2 adult and 3 child tickets, plus 5 dollars delivery, is 0.9, bracket, 2A plus 3C, plus 5.",
             do=[E("🛒", 90, 170, 100), MATH("0.9(2a + 3c) + 5", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.2-k4", "One last question. Write an expression for 20 percent off a price P. Pause the video and answer.", "20% off price P?"),
        dict(say="20 percent off leaves 80 percent. So the new price is 0.8 P.", do=[B("0.8P", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: say what your letters stand for.", do=[T("• Define your letters", x=80, y=170)]),
        dict(say="Use brackets for whole quantities.", do=[T("• Brackets for whole quantities", x=80, y=250)]),
        dict(say="Simplify by collecting like terms.", do=[T("• Collect like terms", x=80, y=330)]),
        dict(say="Test your expression with a number.", do=[T("• Test with a number", x=80, y=410)]),
    ]),
]

VIDEOS["2.3"] = [
    dict(kind="hook", title="A growing cube", steps=[
        dict(say="A cube has edges of length X squared centimetres. Its volume is X squared, all cubed.", do=[E("🧊", 90, 170, 100), MATH("volume = (x²)³", x=230, y=190)]),
        PAUSE("2.3-k1", "Is X squared, all cubed, equal to X to the 5, or X to the 6? Pause the video and choose.", "(x²)³ = x⁵ or x⁶?"),
    ]),
    dict(kind="hook", title="(x²)³ = x⁶", steps=[
        dict(say="X squared, all cubed, is X squared, times X squared, times X squared. That is 2 plus 2 plus 2, which is 6. So it is X to the 6.",
             do=[MATH("x² × x² × x² = x⁶", x=80, y=190, color=GREEN)]),
        dict(say="Check with X equals 2. 2 squared is 4, and 4 cubed is 64. 2 to the 6 is also 64.", do=[MATH("x = 2: 4³ = 64 = 2⁶ ✓", x=80, y=300)]),
    ]),
    dict(kind="recall", title="Index laws for numbers", steps=[
        dict(say="Remember: 3 to the 4, times 3 squared, is 3 to the 6. And 5 to the 7, divided by 5 cubed, is 5 to the 4.", do=[MATH("3⁴ × 3² = 3⁶   ·   5⁷ ÷ 5³ = 5⁴", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Index laws in algebra", steps=[
        dict(say="The same laws work with letters. Multiply: add the indices. Divide: subtract them. A power of a power: multiply the indices.",
             do=[TBL(["Law", "Example"], [["× → add", "x² × x⁵ = x⁷"], ["÷ → subtract", "y⁹ ÷ y⁴ = ?"], ["power of a power → multiply", "(z³)⁴ = z¹²"]], y=170), ROW(0, 3), ROW(1, 5), ROW(2, 7)]),
        PAUSE("2.3-k2", "Your turn. Simplify Y to the 9, divided by Y to the 4. Pause the video and try it.", "y⁹ ÷ y⁴?"),
    ]),
    dict(kind="idea", title="Check: y⁹ ÷ y⁴", steps=[
        dict(say="Dividing, so subtract the indices. 9 minus 4 is 5. The answer is Y to the 5.", do=[B("y⁹ ÷ y⁴ = y⁵", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="With numbers in front", steps=[
        dict(say="Deal with the numbers and the letters separately. 3 A to the 4, times 5 A squared, is 15 A to the 6.", do=[MATH("3a⁴ × 5a² = 15a⁶", x=80, y=170)]),
        dict(say="12 B to the 7, divided by 4 B cubed, is 3 B to the 4.", do=[MATH("12b⁷ ÷ 4b³ = 3b⁴", x=80, y=260)]),
        dict(say="Only add terms with exactly the same letter and power. 6 W cubed plus 2 W cubed is 8 W cubed.", do=[MATH("6w³ + 2w³ = 8w³", x=80, y=350)]),
    ]),
    dict(kind="method", title="How do I simplify with indices?", steps=[
        dict(say="Here is the method. Step 1: multiply or divide the numbers first.", do=[T("1. The **numbers** first", x=80, y=170)]),
        dict(say="Step 2: for each letter, multiplying adds the indices, dividing subtracts, and a power of a power multiplies.", do=[T("2. × add · ÷ subtract · power of power multiply", x=80, y=260)]),
        dict(say="Step 3: a bracket raised to a power: apply the power to everything inside.", do=[T("3. Bracket power → **every factor** inside", x=80, y=350)]),
        dict(say="Step 4: check by substituting a small number.", do=[T("4. **Check** with a number", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Multiplying", steps=[
        dict(say="Simplify 4 P cubed Q, times 2 P Q to the 5. The numbers: 4 times 2 is 8. P cubed times P is P to the 4. Q times Q to the 5 is Q to the 6.",
             do=[MATH("4p³q × 2pq⁵", x=80, y=170), B("8p⁴q⁶", x=80, y=290, color=GREEN, at=8)]),
    ]),
    dict(kind="example", title="A bracket to a power", steps=[
        dict(say="Simplify 3 K squared, all cubed. Cube the 3: 27. Cube K squared: K to the 6. The answer is 27 K to the 6.",
             do=[MATH("(3k²)³ = 3³ × (k²)³", x=80, y=170), B("27k⁶", x=80, y=290, color=GREEN, at=6)]),
        PAUSE("2.3-k3", "Your turn. Simplify 2 C cubed, all squared. Pause and work it out.", "(2c³)²?"),
    ]),
    dict(kind="example", title="Check: (2c³)²", steps=[
        dict(say="Square the 2 too: 2 squared is 4. C cubed, squared, is C to the 6. The answer is 4 C to the 6.", do=[B("(2c³)² = 4c⁶", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Tom simplifies 2 Y to the 4, all cubed. Which line is wrong?", do=LINES("Tom", "(2y⁴)³", ["(2y⁴)³ = 2y¹²"])),
        dict(say="Line 1 is wrong. He forgot to cube the 2. Everything inside the bracket is cubed.", do=[dict(a="cross", id="l1")]),
        dict(say="2 cubed is 8, so the answer is 8 Y to the 12.", do=[B("(2y⁴)³ = 8y¹²", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Bigger balloons", steps=[
        dict(say="Index laws help in science. If a balloon's radius doubles, its volume, which depends on R cubed, becomes 2 cubed, which is 8 times bigger.",
             do=[E("🎈", 90, 170, 100), MATH("(2r)³ = 8r³", x=230, y=200), T("8 times the volume", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.3-k4", "One last question. Can 6 W cubed plus 2 W squared be simplified? Pause the video and choose.", "6w³ + 2w² …"),
        dict(say="No. W cubed and W squared are not like terms. So it cannot be simplified.", do=[B("cannot be simplified", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: multiply, add the indices. Divide, subtract. Power of a power, multiply.", do=[T("• × add · ÷ subtract · power of power multiply", x=80, y=170)]),
        dict(say="Deal with numbers and letters separately.", do=[T("• Numbers and letters separately", x=80, y=250)]),
        dict(say="A power on a bracket applies to everything inside.", do=[T("• (ab)ⁿ = aⁿbⁿ", x=80, y=330)]),
        dict(say="Only like terms can be added.", do=[T("• Only like terms can be added", x=80, y=410)]),
    ]),
]

VIDEOS["2.4"] = [
    dict(kind="hook", title="A bigger garden", steps=[
        dict(say="A square garden has sides of X metres. The owner makes it 3 metres longer and 2 metres wider.", do=[E("🌳", 90, 170, 100), T("x by x → **(x + 3)** by **(x + 2)**", x=230, y=200)]),
        PAUSE("2.4-k1", "When X is 10, what is the new area? Pause the video and work it out.", "New area when x = 10?"),
    ]),
    dict(kind="hook", title="156 square metres", steps=[
        dict(say="The new sides are 13 and 12. 13 times 12 is 156 square metres. It is not X squared plus 6, which would only be 106.",
             do=[MATH("13 × 12 = 156 m²", x=80, y=190, color=GREEN), T("not x² + 6 = 106 ✗", x=80, y=300, color=RED)]),
    ]),
    dict(kind="recall", title="Single brackets", steps=[
        dict(say="Remember: 4, bracket, X plus 3, is 4 X plus 12. And X, bracket, X minus 5, is X squared minus 5 X.", do=[MATH("4(x + 3) = 4x + 12   ·   x(x − 5) = x² − 5x", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Two brackets", steps=[
        dict(say="Multiply every term in the first bracket by every term in the second. A grid helps.",
             do=[TBL(["×", "x", "+3"], [["x", "x²", "3x"], ["+2", "2x", "+6"]], y=170), ROW(0, 1), ROW(1, 2)]),
        PAUSE("2.4-k2", "Your turn. Use the grid to expand X plus 3, times X plus 2. Pause the video and try it.", "(x + 3)(x + 2)?"),
    ]),
    dict(kind="idea", title="Check: (x + 3)(x + 2)", steps=[
        dict(say="Add the four parts: X squared, plus 3 X, plus 2 X, plus 6. Collect the middle terms: X squared plus 5 X plus 6.",
             do=[MATH("x² + 3x + 2x + 6", x=80, y=190), B("x² + 5x + 6", x=80, y=300, color=GREEN, at=5)]),
        dict(say="With X equals 10: 100 plus 50 plus 6 is 156. That matches the garden.", do=[MATH("100 + 50 + 6 = 156 ✓", x=80, y=400)]),
    ]),
    dict(kind="idea", title="Special products", steps=[
        dict(say="A perfect square: X plus 4, all squared, is X plus 4 times X plus 4. That gives X squared plus 8 X plus 16.", do=[MATH("(x + 4)² = x² + 8x + 16", x=80, y=170)]),
        dict(say="The difference of two squares: X plus A, times X minus A. The middle terms cancel out, leaving X squared minus A squared.", do=[MATH("(x + a)(x − a) = x² − a²", x=80, y=270, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I expand two brackets?", steps=[
        dict(say="Here is the method. Step 1: draw a grid.", do=[T("1. Draw a **grid**", x=80, y=170)]),
        dict(say="Step 2: multiply each pair of terms, keeping the signs.", do=[T("2. Multiply each pair, **keep the signs**", x=80, y=260)]),
        dict(say="Step 3: collect the like terms. Usually these are the two middle terms.", do=[T("3. **Collect** the middle terms", x=80, y=350)]),
        dict(say="Step 4: check by substituting a number.", do=[T("4. **Check** with a number", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Negative signs", steps=[
        dict(say="Expand X minus 6, times X minus 2. Negative 6 times negative 2 is positive 12.", do=[MATH("(x − 6)(x − 2) = x² − 2x − 6x + 12", x=80, y=170)]),
        dict(say="Collect the middle terms: X squared minus 8 X plus 12.", do=[B("x² − 8x + 12", x=80, y=290, color=GREEN)]),
        PAUSE("2.4-k3", "Your turn. Expand Y plus 5, times Y minus 5. Pause and work it out.", "(y + 5)(y − 5)?"),
    ]),
    dict(kind="example", title="Check: (y + 5)(y − 5)", steps=[
        dict(say="Y squared, minus 5 Y, plus 5 Y, minus 25. The middle terms cancel. The answer is Y squared minus 25.", do=[MATH("y² − 5y + 5y − 25", x=80, y=190), B("y² − 25", x=80, y=300, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Mental maths", steps=[
        dict(say="Use the difference of two squares to work out 41 times 39. That is 40 plus 1, times 40 minus 1. So it is 40 squared minus 1 squared: 1,600 minus 1, which is 1,599.",
             do=[MATH("41 × 39 = (40 + 1)(40 − 1)", x=80, y=170), MATH("= 40² − 1² = 1600 − 1", x=80, y=270, at=6), B("1599", x=80, y=380, color=GREEN, at=10)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Zara expands X plus 3, all squared. Which line is wrong?", do=LINES("Zara", "(x + 3)²", ["(x + 3)² = x² + 9"])),
        dict(say="Line 1 is wrong. She squared each term, and missed the middle terms.", do=[dict(a="cross", id="l1")]),
        dict(say="X plus 3, times X plus 3, is X squared plus 6 X plus 9.", do=[B("x² + 6x + 9", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Quick multiplying", steps=[
        dict(say="Mental maths champions use this trick. 51 times 49 is 50 squared minus 1, which is 2,499.", do=[E("🧠", 90, 170, 100), MATH("51 × 49 = 2500 − 1 = 2499", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.4-k4", "One last question. Use the difference of two squares to work out 31 times 29. Pause the video and answer.", "31 × 29 using the difference of two squares?"),
        dict(say="31 times 29 is 30 plus 1, times 30 minus 1. 900 minus 1 is 899.", do=[B("30² − 1² = 899", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: multiply every term by every term.", do=[T("• Every term × every term", x=80, y=170)]),
        dict(say="X plus A, all squared, is X squared plus 2 A X plus A squared.", do=[T("• (x + a)² = x² + 2ax + a²", x=80, y=250)]),
        dict(say="X plus A, times X minus A, is X squared minus A squared.", do=[T("• (x + a)(x − a) = x² − a²", x=80, y=330)]),
        dict(say="Collect like terms, and check with a number.", do=[T("• Collect like terms; check", x=80, y=410)]),
    ]),
]

VIDEOS["2.5"] = [
    dict(kind="hook", title="Sharing the bill", steps=[
        dict(say="Two friends share a pizza bill of X dollars. Ana pays X over 3, and Ben pays X over 4.", do=[E("🍕", 90, 170, 100), MATH("Ana " + F("x", 3) + "   Ben " + F("x", 4), x=230, y=170)]),
        PAUSE("2.5-k1", "What fraction of X have they paid together? Pause the video and try it.", "x/3 + x/4 = ?"),
    ]),
    dict(kind="hook", title="7x/12", steps=[
        dict(say="Use a common denominator of 12. X over 3 is 4 X over 12. X over 4 is 3 X over 12. Together, 7 X over 12.",
             do=[MATH(F("4x", 12) + " + " + F("3x", 12) + " = " + F("7x", 12), x=80, y=180, color=GREEN)]),
        dict(say="Check with X equals 12: Ana pays 4 and Ben pays 3. That is 7, and 7 twelfths of 12 is 7.", do=[MATH("x = 12: 4 + 3 = 7 ✓", x=80, y=340)]),
    ]),
    dict(kind="recall", title="Number fractions", steps=[
        dict(say="Remember: 1 third plus 1 quarter is 4 twelfths plus 3 twelfths, which is 7 twelfths.", do=[MATH(F(1, 3) + " + " + F(1, 4) + " = " + F(4, 12) + " + " + F(3, 12) + " = " + F(7, 12), x=80, y=180)]),
    ]),
    dict(kind="idea", title="Adding and subtracting", steps=[
        dict(say="Algebraic fractions have letters in them. Add and subtract them just like number fractions, with a common denominator.", do=[T("same rules: a **common denominator**", x=80, y=170)]),
        dict(say="With different letters on the bottom, multiply them to get the common denominator.", do=[T("different letters → multiply the denominators", x=80, y=260)]),
        PAUSE("2.5-k2", "Your turn. Is 2 over A, plus 3 over B, equal to 2 B plus 3 A, over A B? Or 5 over A plus B? Pause and choose.", "2/a + 3/b = ?"),
    ]),
    dict(kind="idea", title="Check", steps=[
        dict(say="The common denominator is A B. 2 over A becomes 2 B over A B. 3 over B becomes 3 A over A B. So the answer is 2 B plus 3 A, over A B.",
             do=[B(K("\\dfrac{2}{a} + \\dfrac{3}{b} = \\dfrac{2b + 3a}{ab}"), x=80, y=180, color=GREEN)]),
        dict(say="You never add the denominators.", do=[T("never add the denominators ✗", x=80, y=360, color=RED)]),
    ]),
    dict(kind="idea", title="Multiplying and cancelling", steps=[
        dict(say="To multiply, multiply the tops and multiply the bottoms. To divide, flip the second fraction and multiply.", do=[T("× tops and bottoms · ÷ flip and multiply", x=80, y=170)]),
        dict(say="Cancel common factors at the end.", do=[T("cancel **common factors**", x=80, y=260)]),
    ]),
    dict(kind="method", title="How do I simplify algebraic fractions?", steps=[
        dict(say="Here is the method. Step 1: to add or subtract, use a common denominator, then combine the numerators.", do=[T("1. + − : **common denominator**", x=80, y=170)]),
        dict(say="Step 2: to multiply, multiply the numerators and the denominators.", do=[T("2. × : top × top, bottom × bottom", x=80, y=260)]),
        dict(say="Step 3: to divide, flip the second fraction and multiply.", do=[T("3. ÷ : **flip** and multiply", x=80, y=350)]),
        dict(say="Step 4: cancel any common factors.", do=[T("4. **Cancel** common factors", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Cancelling", steps=[
        dict(say="Simplify 6 X squared over 9 X. Both the top and the bottom divide by 3 X. That leaves 2 X over 3.", do=[MATH(F("6x^2", "9x") + " = " + F("2x", 3), x=80, y=190, color=GREEN)]),
        dict(say="Simplify 4 Q over 9, times 3 over 2 Q. Multiply: 12 Q over 18 Q. The Q cancels, leaving 2 thirds.", do=[MATH(F("4q", 9) + " × " + F(3, "2q") + " = " + F("12q", "18q") + " = " + F(2, 3), x=80, y=330)]),
        PAUSE("2.5-k3", "Your turn. Simplify 5 X squared over 10 X. Pause and work it out.", "Simplify 5x²/(10x)."),
    ]),
    dict(kind="example", title="Check: 5x²/10x", steps=[
        dict(say="Divide the top and bottom by 5 X. That leaves X over 2.", do=[B(F("5x^2", "10x") + " = " + F("x", 2), x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="example", title="Brackets on top", steps=[
        dict(say="Simplify X plus 1 over 3, plus X minus 2 over 2. The common denominator is 6.", do=[MATH(F("x+1", 3) + " + " + F("x-2", 2), x=80, y=170)]),
        dict(say="That gives 2, bracket, X plus 1, plus 3, bracket, X minus 2, all over 6. Expand and collect: 5 X minus 4, over 6.",
             do=[MATH(F("2(x+1) + 3(x-2)", 6), x=80, y=290, at=1), B(F("5x-4", 6), x=80, y=420, color=GREEN, at=8)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Kim simplifies X over 3, plus X over 5. Which line is wrong?", do=LINES("Kim", "x/3 + x/5", ["= 2x/8 = x/4"])),
        dict(say="Line 1 is wrong. She added the denominators. Use a common denominator of 15.", do=[dict(a="cross", id="l1")]),
        dict(say="5 X over 15, plus 3 X over 15, is 8 X over 15.", do=[B(F("5x", 15) + " + " + F("3x", 15) + " = " + F("8x", 15), x=110, y=360, color=GREEN)]),
    ]),
    dict(kind="life", title="Lenses", steps=[
        dict(say="Camera lenses use a formula with algebraic fractions: 1 over F equals 1 over U, plus 1 over V. Designers combine fractions like these to focus the image.",
             do=[E("📷", 90, 170, 100), MATH(K("\\dfrac{1}{f} = \\dfrac{1}{u} + \\dfrac{1}{v}"), x=230, y=170)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.5-k4", "One last question. Simplify Y over 2, minus Y over 6. Pause the video and answer.", "y/2 − y/6?"),
        dict(say="Y over 2 is 3 Y over 6. 3 Y over 6, minus Y over 6, is 2 Y over 6, which simplifies to Y over 3.",
             do=[B(F("3y", 6) + " − " + F("y", 6) + " = " + F("2y", 6) + " = " + F("y", 3), x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: algebraic fractions follow the same rules as number fractions.", do=[T("• Same rules as number fractions", x=80, y=170)]),
        dict(say="Use a common denominator to add or subtract.", do=[T("• Common denominator to + −", x=80, y=250)]),
        dict(say="Flip and multiply to divide.", do=[T("• Flip and multiply to ÷", x=80, y=330)]),
        dict(say="Cancel common factors.", do=[T("• Cancel common factors", x=80, y=410)]),
    ]),
]

VIDEOS["2.6"] = [
    dict(kind="hook", title="Speeding up", steps=[
        dict(say="A cyclist starts at a speed of U metres per second. She speeds up by A metres per second every second. After T seconds, her speed is V equals U plus A T.",
             do=[E("🚴", 90, 170, 100), B("v = u + at", x=230, y=190, color=BLUE)]),
        dict(say="Her final speed is 14, her starting speed is 2, and T is 4 seconds.", do=[MATH("v = 14,  u = 2,  t = 4", x=230, y=300)]),
        PAUSE("2.6-k1", "Find A, her acceleration. Pause the video and work it out.", "v = u + at, v = 14, u = 2, t = 4. Find a."),
    ]),
    dict(kind="hook", title="a = 3", steps=[
        dict(say="14 equals 2 plus 4 A. Take away 2: 12 equals 4 A. Divide by 4: A equals 3 metres per second, every second.",
             do=[MATH("14 = 2 + 4a → 12 = 4a", x=80, y=190), B("a = 3", x=80, y=300, color=GREEN, at=6)]),
    ]),
    dict(kind="recall", title="Solving equations", steps=[
        dict(say="Remember: to solve an equation, do the same to both sides, to undo each operation.", do=[T("do the **same to both sides**", x=80, y=190)]),
    ]),
    dict(kind="idea", title="The subject of a formula", steps=[
        dict(say="A formula is a rule that links variables. The variable on its own is the subject. In V equals U plus A T, the subject is V.", do=[T("the **subject** is on its own: **v** = u + at", x=80, y=170)]),
        dict(say="Changing the subject means rearranging, so that a different variable is on its own. Subtract U from both sides, then divide by T.",
             do=[TBL(["Step", "v = u + at"], [["subtract u", "v − u = at"], ["divide by t", "a = (v − u) ÷ t"]], y=260), ROW(0, 5), ROW(1, 7)]),
        PAUSE("2.6-k2", "Your turn. Make T the subject of V equals U plus A T. Pause the video and try it.", "Make t the subject of v = u + at."),
    ]),
    dict(kind="idea", title="Check: t", steps=[
        dict(say="Subtract U: V minus U equals A T. This time divide by A. So T equals V minus U, all over A.", do=[MATH("v − u = at", x=80, y=190), B(K("t = \\dfrac{v - u}{a}"), x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="idea", title="Deriving a formula", steps=[
        dict(say="You can write your own formula. A plumber charges a 40 dollar call-out fee, plus 25 dollars per hour. The cost C for H hours is C equals 40 plus 25 H.",
             do=[E("🔧", 90, 170, 90), B("C = 40 + 25h", x=230, y=190, color=BLUE)]),
        dict(say="Rearrange it to find the hours: H equals C minus 40, over 25.", do=[MATH(K("h = \\dfrac{C - 40}{25}"), x=230, y=300)]),
    ]),
    dict(kind="method", title="How do I change the subject?", steps=[
        dict(say="Here is the method. Step 1: circle the new subject.", do=[T("1. **Circle** the new subject", x=80, y=170)]),
        dict(say="Step 2: undo the operations around it, in reverse order. Do the same to both sides.", do=[T("2. Undo in **reverse order**, both sides", x=80, y=260)]),
        dict(say="Step 3: keep fractions and brackets clear.", do=[T("3. Keep fractions and brackets **clear**", x=80, y=350)]),
        dict(say="Step 4: check by substituting numbers.", do=[T("4. **Check** with numbers", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Area of a triangle", steps=[
        dict(say="Make H the subject of A equals a half B H. Multiply both sides by 2: 2 A equals B H. Then divide by B: H equals 2 A over B.",
             do=[MATH(K("A = \\tfrac{1}{2}bh"), x=80, y=170), MATH("2A = bh", x=80, y=270, at=5), B(K("h = \\dfrac{2A}{b}"), x=80, y=360, color=GREEN, at=8)]),
        PAUSE("2.6-k3", "Your turn. Make B the subject of the same formula. Pause and work it out.", "Make b the subject of A = ½bh."),
    ]),
    dict(kind="example", title="Check: b", steps=[
        dict(say="2 A equals B H. This time divide by H. So B equals 2 A over H.", do=[B(K("b = \\dfrac{2A}{h}"), x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="example", title="A square", steps=[
        dict(say="Make R the subject of A equals pi R squared. Divide by pi: R squared equals A over pi. Then take the square root.",
             do=[MATH(K("A = \\pi r^2 \\Rightarrow r^2 = \\dfrac{A}{\\pi}"), x=80, y=170), B(K("r = \\sqrt{\\dfrac{A}{\\pi}}"), x=80, y=310, color=GREEN, at=6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Max makes A the subject of V equals U plus A T. Which line is wrong?", do=LINES("Max", "make a the subject of v = u + at", ["v ÷ t = u + a", "a = v ÷ t − u"])),
        dict(say="Line 1 is wrong. Adding U was done last, so undo it first. Subtract U, then divide by T.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="V minus U equals A T. So A equals V minus U, over T.", do=[B(K("a = \\dfrac{v - u}{t}"), x=110, y=400, color=GREEN)]),
    ]),
    dict(kind="life", title="Medicine", steps=[
        dict(say="Doctors rearrange formulae to work out medicine doses. Engineers rearrange V equals U plus A T to design brakes that stop a train in time.",
             do=[E("💊", 90, 170, 100), T("rearranged every day by doctors and engineers", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.6-k4", "One last question. Make X the subject of Y equals X over 4. Pause the video and answer.", "Make x the subject of y = x/4."),
        dict(say="X was divided by 4, so multiply both sides by 4. X equals 4 Y.", do=[B("x = 4y", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the subject is the variable on its own.", do=[T("• The subject is on its own", x=80, y=170)]),
        dict(say="Use inverse operations, in reverse order.", do=[T("• Inverse operations, reverse order", x=80, y=250)]),
        dict(say="A square is undone by a square root.", do=[T("• Square ↔ square root", x=80, y=330)]),
        dict(say="Check with numbers.", do=[T("• Check with numbers", x=80, y=410)]),
    ]),
]
