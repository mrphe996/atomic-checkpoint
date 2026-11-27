# -*- coding: utf-8 -*-
"""Stage 8 · Unit 2 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG, BAL, INEQ
from .s7_u04 import TBL, ROW, STEPT

VIDEOS = {}

VIDEOS["2.1"] = [
    dict(kind="hook", title="A phone contract", steps=[
        dict(say="A phone contract costs 15 dollars a month. If you use more data than your allowance, you pay 2 dollars for every extra gigabyte.",
             do=[E("📱", 90, 170, 100), T("**$15** a month + **$2** per extra GB", x=230, y=200)]),
        dict(say="Suppose you go over by g gigabytes in one month. We do not know g yet, so we use a letter.", do=[T("over by **g** GB", x=230, y=300)]),
        PAUSE("2.1-k1", "Write an expression for one month's bill. Pause the video and try it.", "One month's bill: $15 plus $2 per GB over (g GB)."),
    ]),
    dict(kind="hook", title="One month, one year", steps=[
        dict(say="The fixed part is 15. Each extra gigabyte adds 2, so g gigabytes add 2 g. One month's bill is 15 plus 2 g dollars.",
             do=[MATH("15 + 2g", x=80, y=190, color=GREEN)]),
        dict(say="For a whole year, the whole monthly bill is multiplied by 12. A bracket shows that: 12 times, open bracket, 15 plus 2 g, close bracket.",
             do=[MATH("12(15 + 2g)", x=80, y=300, color=BLUE), T("the bracket means **the whole bill** × 12", x=80, y=390, at=4)]),
    ]),
    dict(kind="recall", title="Order of operations", steps=[
        dict(say="Remember the order: brackets, then indices, then times and divide, then add and subtract.", do=[T("brackets → indices → × ÷ → + −", x=80, y=170)]),
        dict(say="2 plus 3 times 4 squared is 2 plus 3 times 16, which is 50. But with a bracket, 2 plus 3, times 4 squared, is 5 times 16, which is 80.",
             do=[MATH("2 + 3 × 4² = 2 + 48 = 50", x=80, y=270), MATH("(2 + 3) × 4² = 5 × 16 = 80", x=80, y=360, at=5)]),
    ]),
    dict(kind="idea", title="Words into expressions", steps=[
        dict(say="Use a letter for each unknown. The order of the words gives the order of the operations.",
             do=[TBL(["Words", "Expression"], [["square n, then add 4", "n² + 4"], ["add 4 to n, then square", "(n + 4)²"], ["multiply n by 3, then subtract 1", "3n − 1"], ["subtract 1 from n, then multiply by 3", "3(n − 1)"]], y=170), ROW(0, 0.3), ROW(1, 1.5)]),
        dict(say="Square n then add 4 is n squared plus 4. But add 4 first, then square, needs a bracket: n plus 4, all squared.", do=[ROW(2, 4)]),
        dict(say="In the same way, subtract 1 from n, then multiply by 3, is 3 times, bracket, n minus 1.", do=[ROW(3, 0.5)]),
        PAUSE("2.1-k2", "Your turn. Write: add 3 to n, then multiply by 7. Pause the video and try it.", "Write: 'add 3 to n, then multiply by 7'."),
    ]),
    dict(kind="idea", title="Check: 7(n + 3)", steps=[
        dict(say="The adding happens first, so it goes in a bracket. Then the whole bracket is multiplied by 7. The answer is 7, bracket, n plus 3.",
             do=[MATH("7(n + 3)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Terms and coefficients", steps=[
        dict(say="Look at 5 x squared, minus 3 x, plus 7. It has three terms: 5 x squared, negative 3 x, and 7.", do=[MATH("5x² − 3x + 7", x=80, y=170), T("terms: **5x²**, **−3x**, **7**", x=80, y=260)]),
        dict(say="The number in front of a letter is its coefficient. The coefficient of x squared is 5. The coefficient of x is negative 3, because the minus sign belongs to the term. 7 is the constant.",
             do=[T("coefficient of x² = **5** · of x = **−3** · constant = **7**", x=80, y=340)]),
        dict(say="A linear expression has no power higher than 1, like 4 x plus 1. Two expressions are equivalent if they are equal for every value, like 2, bracket, x plus 3, and 2 x plus 6.",
             do=[T("**linear**: no power above 1, e.g. 4x + 1", x=80, y=420), T("**equivalent**: 2(x + 3) and 2x + 6", x=80, y=500, at=6)]),
    ]),
    dict(kind="method", title="How do I write an expression?", steps=[
        dict(say="Here is the method. Step 1: choose a letter for each unknown, and say what it stands for.", do=[T("1. Choose letters and say what they mean", x=80, y=170)]),
        dict(say="Step 2: find the fixed amounts, and the amounts for each unit.", do=[T("2. Find the **fixed** amounts and the amounts **per unit**", x=80, y=260)]),
        dict(say="Step 3: build the expression in the right order. Use a bracket for the result of a calculation.", do=[T("3. Build it in order; **brackets** for 'the result of'", x=80, y=350)]),
        dict(say="Step 4: test it with a simple number to check it makes sense.", do=[T("4. **Test** it with a simple number", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Pencils and pens", steps=[
        dict(say="Pencils cost p cents. Pens cost 3 cents more than pencils. Write an expression for the cost of 4 pencils and 2 pens.", do=[E("✏️", 90, 160, 90), T("pencil **p** cents · pen **3 more**", x=230, y=190)]),
        dict(say="A pen costs p plus 3. So the total is 4 p, plus 2 times, bracket, p plus 3.", do=[MATH("4p + 2(p + 3)", x=80, y=300)]),
        dict(say="Expand and simplify: 4 p plus 2 p plus 6, which is 6 p plus 6 cents.", do=[MATH("= 4p + 2p + 6 = 6p + 6", x=80, y=390, color=GREEN)]),
    ]),
    dict(kind="example", title="A perimeter", steps=[
        dict(say="A rectangle's length is 3 more than twice its width, w. Write an expression for its perimeter.", do=[MATH("length = 2w + 3", x=80, y=170)]),
        dict(say="The perimeter is two lengths and two widths: 2 times, bracket, 2 w plus 3, plus 2 w.", do=[MATH("2(2w + 3) + 2w", x=80, y=260)]),
        dict(say="That is 4 w plus 6 plus 2 w, which is 6 w plus 6.", do=[MATH("= 4w + 6 + 2w = 6w + 6", x=80, y=350, color=GREEN)]),
        PAUSE("2.1-k3", "Your turn. In 4 y squared, minus 9 y, plus 2, what is the coefficient of y? Pause and work it out.", "In 4y² − 9y + 2, what is the coefficient of y?"),
    ]),
    dict(kind="example", title="Check: the coefficient", steps=[
        dict(say="The y term is negative 9 y. The minus sign belongs to the term, so the coefficient of y is negative 9.", do=[MATH("4y² − 9y + 2", x=80, y=190), B("coefficient of y = −9", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Equivalent or not?", steps=[
        dict(say="Are 3, bracket, n plus 2, minus n, and 2 n plus 6 equivalent? Expand and simplify the first one.", do=[MATH("3(n + 2) − n", x=80, y=170)]),
        dict(say="3 n plus 6 minus n is 2 n plus 6. It is the same expression, so yes, they are equivalent.", do=[MATH("= 3n + 6 − n = 2n + 6", x=80, y=260), B("equivalent ✓", x=80, y=360, color=GREEN, at=4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Sam writes: double n, then square the result. Which line is wrong?", do=LINES("Sam", "double n, then square the result", ["double n is 2n", "square it: 2n²"])),
        dict(say="Line 2 is wrong. 2 n squared squares only the n. The whole of 2 n must be squared, so it needs a bracket.", do=[dict(a="cross", id="l2")]),
        dict(say="Double n, then square, is 2 n in a bracket, squared. That equals 4 n squared.", do=[B("(2n)² = 4n²", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Taxi fares", steps=[
        dict(say="Taxi meters use an expression. In many cities, a taxi charges a fixed starting fare, then a fixed amount for each kilometre.",
             do=[E("🚕", 90, 170, 100), T("fixed start + an amount **per km**", x=230, y=200)]),
        dict(say="If the start is 3 dollars and each kilometre is 1 dollar 50, a trip of k kilometres costs 3 plus 1.5 k dollars. For a 10 kilometre trip, that is 18 dollars.",
             do=[MATH("3 + 1.5k", x=230, y=310, color=BLUE), MATH("k = 10 → 3 + 15 = $18", x=230, y=400, at=6)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.1-k4", "One last question. Is 5 minus 2 x a linear expression? Pause the video and answer.", "Is 5 − 2x linear?"),
        dict(say="Yes. The highest power of x is 1, so 5 minus 2 x is linear.", do=[MATH("5 − 2x", x=80, y=190), B("linear ✓", x=80, y=290, color=GREEN, at=2)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: letters stand for unknown numbers. Say what each letter means.", do=[T("• Letters stand for unknowns; say what each means", x=80, y=170)]),
        dict(say="The order of the words gives the order of the operations. Brackets show the result of a calculation.", do=[T("• Word order → operation order; brackets for 'the result'", x=80, y=250)]),
        dict(say="Terms, coefficients and constants. A linear expression has no power above 1.", do=[T("• Terms, coefficients, constants; linear = no power above 1", x=80, y=330)]),
        dict(say="Equivalent expressions are equal for every value of the letter.", do=[T("• Equivalent = equal for every value", x=80, y=410)]),
    ]),
]

VIDEOS["2.2"] = [
    dict(kind="hook", title="A falling ball", steps=[
        dict(say="Scientists use a formula for a dropped ball. The distance d metres that it falls in t seconds is d equals 5 t squared. This ignores air.",
             do=[E("⚽", 90, 170, 100), T("distance fallen: **d = 5t²**", x=230, y=200)]),
        PAUSE("2.2-k1", "How far does the ball fall in 3 seconds? Pause the video and work it out.", "d = 5t². Find d when t = 3."),
    ]),
    dict(kind="hook", title="Three seconds", steps=[
        dict(say="Put t equals 3 into the formula. Square first: 3 squared is 9. Then multiply: 5 times 9 is 45. The ball falls 45 metres.",
             do=[MATH("d = 5 × 3²", x=80, y=190), MATH("= 5 × 9 = 45", x=80, y=280, at=3.4), B("45 m", x=80, y=380, color=GREEN, at=6)]),
        dict(say="And if it falls 80 metres, how long did it take? We will answer that later.", do=[T("falls 80 m → how long?", x=80, y=480)]),
    ]),
    dict(kind="recall", title="Substituting negatives", steps=[
        dict(say="Remember: if b is negative 3, then 4 b minus 7 is 4 times negative 3, minus 7. That is negative 12 minus 7, which is negative 19.",
             do=[MATH("4b − 7,  b = −3", x=80, y=180), MATH("4 × (−3) − 7 = −12 − 7 = −19", x=80, y=280, at=4)]),
        dict(say="Put a negative number in brackets when you substitute. It stops sign mistakes.", do=[T("negatives go in **brackets**", x=80, y=380, color=BLUE)]),
    ]),
    dict(kind="idea", title="Formulae", steps=[
        dict(say="A formula is a rule that links variables, with an equals sign. In d equals 5 t squared, the letter on its own, d, is called the subject.",
             do=[MATH("d = 5t²", x=80, y=170), T("**d** is the **subject**", x=420, y=178)]),
        dict(say="With negatives, use brackets. If y equals x squared, minus 2 x, and x is negative 1, then y is negative 1 squared, minus 2 times negative 1.",
             do=[MATH("y = x² − 2x,  x = −1", x=80, y=270), MATH("y = (−1)² − 2 × (−1)", x=80, y=350, at=6)]),
        PAUSE("2.2-k2", "Your turn. Finish it: find y when x is negative 1. Pause the video and try it.", "y = x² − 2x. Find y when x = −1."),
    ]),
    dict(kind="idea", title="Check: y when x = −1", steps=[
        dict(say="Negative 1 squared is 1. 2 times negative 1 is negative 2, and subtracting negative 2 means adding 2. So y equals 1 plus 2, which is 3.",
             do=[MATH("(−1)² − 2 × (−1) = 1 + 2", x=80, y=190), B("y = 3", x=80, y=290, color=GREEN, at=5)]),
    ]),
    dict(kind="idea", title="Changing the subject", steps=[
        dict(say="To find t when d is known, rearrange the formula so that t is the subject. Undo the operations in reverse order, just like solving an equation.",
             do=[T("make **t** the subject: undo in **reverse order**", x=80, y=170)]),
        dict(say="Start with d equals 5 t squared. Divide both sides by 5: d over 5 equals t squared. Then take the square root. For the 80 metre fall, 80 over 5 is 16, and the square root of 16 is 4. It took 4 seconds.",
             do=[STEPT("Working", [["start", "d = 5t²"], ["÷ 5", "d/5 = t²"], ["√", "t = √(d/5)"]], y=250), ROW(0, 0.2), ROW(1, 3.2), ROW(2, 6), MATH("d = 80: t = √16 = 4 s", x=760, y=330, color=GREEN, at=9)]),
    ]),
    dict(kind="method", title="How do I use and rearrange a formula?", steps=[
        dict(say="Here is the method. Step 1: to substitute, replace each letter with its value, in brackets. Then follow the order of operations.", do=[T("1. **Substitute** in brackets, then the order of operations", x=80, y=170)]),
        dict(say="Step 2: to rearrange, decide what has been done to the new subject, and in what order.", do=[T("2. What has been done to the new subject, in what order?", x=80, y=260)]),
        dict(say="Step 3: undo those operations in reverse order, doing the same to both sides.", do=[T("3. Undo in **reverse order**, same to both sides", x=80, y=350)]),
        dict(say="Step 4: check with numbers.", do=[T("4. **Check** with numbers", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Negative values", steps=[
        dict(say="P equals 2 A squared, minus 3 B. Find P when A is negative 3 and B is negative 4.", do=[MATH("P = 2a² − 3b,  a = −3, b = −4", x=80, y=170)]),
        dict(say="A squared is 9, and 2 times 9 is 18. 3 B is 3 times negative 4, which is negative 12.", do=[MATH("2 × (−3)² = 18", x=80, y=260), MATH("3 × (−4) = −12", x=80, y=340, at=3)]),
        dict(say="18 minus negative 12 is 18 plus 12. So P equals 30.", do=[B("P = 18 − (−12) = 30", x=80, y=440, color=GREEN)]),
    ]),
    dict(kind="example", title="Two steps", steps=[
        dict(say="Make x the subject of y equals 3 x minus 4. To get y, x was multiplied by 3, then 4 was subtracted.", do=[MATH("y = 3x − 4", x=80, y=170)]),
        dict(say="Undo in reverse order. First add 4 to both sides: y plus 4 equals 3 x. Then divide both sides by 3.",
             do=[MATH("y + 4 = 3x", x=80, y=260), MATH("x = (y + 4) ÷ 3", x=80, y=350, at=4, color=GREEN)]),
        PAUSE("2.2-k3", "Your turn. Make A the subject of B equals A minus 9. Pause and choose.", "Make a the subject of b = a − 9."),
    ]),
    dict(kind="example", title="Check: a = b + 9", steps=[
        dict(say="9 was subtracted from A. Undo it by adding 9 to both sides. A equals B plus 9.", do=[MATH("b = a − 9", x=80, y=190), MATH("a = b + 9", x=80, y=280, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Temperature", steps=[
        dict(say="To change Celsius to Fahrenheit, F equals 1.8 C plus 32. Make C the subject, then convert 77 degrees Fahrenheit.", do=[MATH("F = 1.8C + 32", x=80, y=170)]),
        dict(say="Subtract 32: F minus 32 equals 1.8 C. Divide by 1.8: C equals F minus 32, all divided by 1.8.", do=[MATH("C = (F − 32) ÷ 1.8", x=80, y=260)]),
        dict(say="77 minus 32 is 45. 45 divided by 1.8 is 25. So 77 degrees Fahrenheit is 25 degrees Celsius.", do=[MATH("(77 − 32) ÷ 1.8 = 45 ÷ 1.8", x=80, y=350), B("25 °C", x=80, y=440, color=GREEN, at=5)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ella makes x the subject of y equals 2 x plus 6. Which line goes wrong first?", do=LINES("Ella", "x as the subject of y = 2x + 6", ["y ÷ 2 = x + 6", "x = y ÷ 2 − 6"])),
        dict(say="Line 1 is wrong. She divided only y by 2, not the whole of the other side. Undo the plus 6 first.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="y minus 6 equals 2 x. So x equals y minus 6, all divided by 2.", do=[B("x = (y − 6) ÷ 2", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Stopping distance", steps=[
        dict(say="Driving instructors use a formula too. A car's braking distance grows with the square of its speed.", do=[E("🚗", 90, 170, 100), T("braking distance grows with **speed²**", x=230, y=200)]),
        dict(say="So doubling the speed makes the braking distance about 4 times as long, because 2 squared is 4. That is why speed limits near schools are low.",
             do=[MATH("2 × speed → 2² = 4 × the distance", x=230, y=310, color=BLUE), E("🏫", 90, 420, 90), T("low limits near schools", x=230, y=445)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.2-k4", "One last question. Using d equals 5 t squared, how many seconds does it take to fall 20 metres? Pause the video and answer.", "d = 5t². How long to fall 20 m (s)?"),
        dict(say="20 equals 5 t squared. Divide by 5: t squared equals 4. The time is positive, so t equals 2 seconds.",
             do=[MATH("20 = 5t²", x=80, y=190), MATH("t² = 4", x=80, y=280, at=2.4), B("t = 2 s", x=80, y=380, color=GREEN, at=4.6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a formula links variables. The subject is the letter on its own.", do=[T("• A formula links variables; the **subject** is on its own", x=80, y=170)]),
        dict(say="Substitute with brackets around negative numbers.", do=[T("• Substitute with brackets around negatives", x=80, y=250)]),
        dict(say="Change the subject by undoing the operations in reverse order.", do=[T("• Change the subject: undo in reverse order", x=80, y=330)]),
        dict(say="And check with numbers.", do=[T("• Check with numbers", x=80, y=410)]),
    ]),
]

GARDEN = lambda w, l, x, y, at=0, c=BLUE, sw=260, sh=160: T(f'<span style="display:inline-flex;align-items:center;justify-content:center;width:{sw}px;height:{sh}px;border:5px solid {c};background:#E3F6EC;border-radius:6px;font-weight:700;position:relative">area?</span><div style="margin-top:6px;font-weight:700">{w} × {l}</div>', x=x, y=y, at=at)

VIDEOS["2.3"] = [
    dict(kind="hook", title="Two gardens", steps=[
        dict(say="A garden is x metres wide. Its length is x plus 5 metres. So its area is x times, bracket, x plus 5.",
             do=[E("🌳", 90, 170, 100), T("width **x m**, length **(x + 5) m**", x=230, y=200), GARDEN("x", "(x + 5)", 860, 150, at=1)]),
        PAUSE("2.3-k1", "Write the area x times, bracket, x plus 5, without brackets. Pause the video and try it.", "Area of the first garden, x(x + 5), without brackets."),
    ]),
    dict(kind="hook", title="Without brackets", steps=[
        dict(say="Multiply x by each term inside. x times x is x squared. x times 5 is 5 x. The area is x squared plus 5 x.",
             do=[MATH("x(x + 5) = x × x + x × 5", x=80, y=190), MATH("= x² + 5x", x=80, y=280, color=GREEN, at=4)]),
        dict(say="Next door, a garden is 3 metres wide and 2 x minus 1 metres long. Its area is 3 times, bracket, 2 x minus 1, which is 6 x minus 3.",
             do=[MATH("3(2x − 1) = 6x − 3", x=80, y=380)]),
    ]),
    dict(kind="recall", title="A single bracket", steps=[
        dict(say="Remember: to expand a bracket, multiply every term inside by the term outside. 4, bracket, n plus 3, is 4 n plus 12.", do=[MATH("4(n + 3) = 4n + 12", x=80, y=180)]),
        dict(say="5, bracket, 2 y minus 3, is 10 y minus 15.", do=[MATH("5(2y − 3) = 10y − 15", x=80, y=280)]),
    ]),
    dict(kind="idea", title="Letters and negatives outside", steps=[
        dict(say="The term outside can be a letter, or a negative number. Multiply each term inside, and use the sign rules.",
             do=[TBL(["Expression", "Working", "Result"], [["x(x + 5)", "x × x + x × 5", "x² + 5x"], ["−3(2x − 1)", "−3 × 2x + (−3) × (−1)", "−6x + 3"], ["2a(a + 4)", "2a × a + 2a × 4", "2a² + 8a"]], y=170), ROW(0, 0.3)]),
        dict(say="Negative 3 times 2 x is negative 6 x. Negative 3 times negative 1 is positive 3. So negative 3, bracket, 2 x minus 1, is negative 6 x plus 3.", do=[ROW(1, 0.3)]),
        dict(say="And 2 A times A is 2 A squared, while 2 A times 4 is 8 A.", do=[ROW(2, 0.3)]),
        PAUSE("2.3-k2", "Your turn. Expand negative 2, bracket, A plus 6. Pause the video and try it.", "Expand −2(a + 6)."),
    ]),
    dict(kind="idea", title="Check: −2(a + 6)", steps=[
        dict(say="Negative 2 times A is negative 2 A. Negative 2 times 6 is negative 12. The answer is negative 2 A minus 12.",
             do=[MATH("−2(a + 6) = −2a − 12", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Expand and simplify", steps=[
        dict(say="To expand and simplify, expand each bracket, then collect like terms. The difference in the garden areas is x, bracket, x plus 5, minus 3, bracket, 2 x minus 1.",
             do=[MATH("x(x + 5) − 3(2x − 1)", x=80, y=170)]),
        dict(say="That is x squared plus 5 x, minus 6 x, plus 3. Collect the x terms: 5 x minus 6 x is negative x. The answer is x squared minus x plus 3.",
             do=[MATH("= x² + 5x − 6x + 3", x=80, y=260), MATH("= x² − x + 3", x=80, y=350, color=GREEN, at=6)]),
        dict(say="A minus sign in front of a bracket changes the sign of every term inside.", do=[T("a **minus** in front changes **every** sign inside", x=80, y=450, color=RED)]),
    ]),
    dict(kind="method", title="How do I expand and simplify?", steps=[
        dict(say="Here is the method. Step 1: multiply the term outside by every term inside, using the sign rules.", do=[T("1. Multiply **every** term inside, with the sign rules", x=80, y=170)]),
        dict(say="Step 2: watch for x times x, which is x squared, and negative times negative, which is positive.", do=[T("2. x × x = **x²** · − × − = **+**", x=80, y=260)]),
        dict(say="Step 3: collect like terms. Keep the x squared terms, the x terms and the numbers separate.", do=[T("3. Collect like terms: x², x, numbers", x=80, y=350)]),
        dict(say="Step 4: check by putting in a number, like x equals 2, in both forms.", do=[T("4. **Check** with x = 2 in both forms", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Two brackets subtracted", steps=[
        dict(say="Expand and simplify 5, bracket, x plus 2, minus 2, bracket, x minus 3.", do=[MATH("5(x + 2) − 2(x − 3)", x=80, y=170)]),
        dict(say="The first bracket gives 5 x plus 10. The second is negative 2 times each term: negative 2 x, and negative 2 times negative 3, which is plus 6.",
             do=[MATH("5x + 10", x=80, y=260), MATH("−2x + 6", x=420, y=260, at=4)]),
        dict(say="Collect: 5 x minus 2 x is 3 x, and 10 plus 6 is 16. The answer is 3 x plus 16.", do=[B("3x + 16", x=80, y=370, color=GREEN)]),
        PAUSE("2.3-k3", "Your turn. Expand and simplify 2, bracket, x plus 4, plus 3, bracket, x minus 1. Pause and work it out.", "Expand and simplify 2(x + 4) + 3(x − 1)."),
    ]),
    dict(kind="example", title="Check: 5x + 5", steps=[
        dict(say="2 x plus 8, plus 3 x minus 3. 2 x plus 3 x is 5 x, and 8 minus 3 is 5. The answer is 5 x plus 5.",
             do=[MATH("2x + 8 + 3x − 3", x=80, y=190), MATH("= 5x + 5", x=80, y=280, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="Two letters", steps=[
        dict(say="Expand 3 A, bracket, 2 B minus A. 3 A times 2 B is 6 A B. 3 A times negative A is negative 3 A squared.",
             do=[MATH("3a(2b − a)", x=80, y=170), MATH("= 6ab − 3a²", x=80, y=270, color=GREEN, at=5)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Noah expands and simplifies 7 minus 2, bracket, x minus 5. Which line goes wrong first?", do=LINES("Noah", "7 − 2(x − 5)", ["−2(x − 5) = −2x − 10", "7 − 2x − 10 = −2x − 3"])),
        dict(say="Line 1 is wrong. Negative 2 times negative 5 is positive 10, not negative 10.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="So it is 7 minus 2 x plus 10, which is 17 minus 2 x.", do=[B("7 − 2x + 10 = 17 − 2x", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Mental maths", steps=[
        dict(say="Expanding brackets is a mental maths trick. To work out 7 times 98, think of 98 as 100 minus 2.", do=[E("🧠", 90, 170, 100), T("7 × 98 = 7(100 − 2)", x=230, y=200)]),
        dict(say="7 times 100 is 700. 7 times 2 is 14. 700 minus 14 is 686. Shopkeepers often use this to add up prices like 99 cents quickly.",
             do=[MATH("700 − 14 = 686", x=230, y=310, color=BLUE), E("🛒", 90, 420, 90), T("prices like 99¢ = 100¢ − 1¢", x=230, y=445)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.3-k4", "One last question. Expand y, bracket, 3 minus y. Pause the video and answer.", "Expand y(3 − y)."),
        dict(say="y times 3 is 3 y. y times negative y is negative y squared. The answer is 3 y minus y squared.", do=[MATH("y(3 − y) = 3y − y²", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: multiply every term inside the bracket by the term outside.", do=[T("• Multiply **every** term inside", x=80, y=170)]),
        dict(say="x times x is x squared. Follow the sign rules.", do=[T("• x × x = x²; follow the sign rules", x=80, y=250)]),
        dict(say="A minus sign in front of a bracket changes every sign inside.", do=[T("• A minus in front changes every sign inside", x=80, y=330)]),
        dict(say="Collect like terms, and check with a number.", do=[T("• Collect like terms; check with a number", x=80, y=410)]),
    ]),
]

VIDEOS["2.4"] = [
    dict(kind="hook", title="Packing it back up", steps=[
        dict(say="Expanding unpacks a bracket. 4, bracket, x plus 3, becomes 4 x plus 12. Factorising does the opposite. It packs the bracket back up.",
             do=[E("📦", 90, 170, 100), MATH("4(x + 3) → 4x + 12", x=230, y=190), T("expand →", x=230, y=270, color=BLUE), MATH("4x + 12 → 4(x + 3)", x=230, y=340, at=5), T("← factorise", x=230, y=420, color=GREEN, at=5)]),
        PAUSE("2.4-k1", "Can you write 6 y plus 15 with a bracket? Pause the video and try it.", "Write 6y + 15 with a bracket."),
    ]),
    dict(kind="hook", title="6y + 15", steps=[
        dict(say="Find a number that divides both terms. 6 and 15 are both in the 3 times table. 6 y divided by 3 is 2 y. 15 divided by 3 is 5.",
             do=[MATH("6y ÷ 3 = 2y", x=80, y=190), MATH("15 ÷ 3 = 5", x=80, y=270, at=4)]),
        dict(say="So 6 y plus 15 equals 3, bracket, 2 y plus 5. Check by expanding: 3 times 2 y is 6 y, and 3 times 5 is 15.", do=[B("6y + 15 = 3(2y + 5)", x=80, y=370, color=GREEN)]),
    ]),
    dict(kind="recall", title="Highest common factor", steps=[
        dict(say="Remember: the highest common factor of two numbers is the biggest number that divides into both. The H C F of 12 and 18 is 6.", do=[MATH("HCF of 12 and 18 = 6", x=80, y=180)]),
        dict(say="The H C F of 20 and 35 is 5.", do=[MATH("HCF of 20 and 35 = 5", x=80, y=280)]),
    ]),
    dict(kind="idea", title="Taking out the HCF", steps=[
        dict(say="To factorise, find the highest common factor of all the terms. Write it outside the bracket. Inside goes each term divided by it.",
             do=[TBL(["Expression", "HCF", "Factorised"], [["6y + 15", "3", "3(2y + 5)"], ["x² + 4x", "x", "x(x + 4)"], ["10a − 15ab", "5a", "5a(2 − 3b)"]], y=170), ROW(0, 0.4)]),
        dict(say="The common factor can be a letter. x squared and 4 x both contain x. So x squared plus 4 x is x, bracket, x plus 4.", do=[ROW(1, 0.3)]),
        dict(say="Or a number and a letter together. 10 A and 15 A B share 5 A.", do=[ROW(2, 0.3)]),
        PAUSE("2.4-k2", "Your turn. Factorise x squared plus 4 x. Pause the video and try it.", "Factorise x² + 4x."),
    ]),
    dict(kind="idea", title="Check: x(x + 4)", steps=[
        dict(say="Both terms contain x. x squared divided by x is x. 4 x divided by x is 4. The answer is x, bracket, x plus 4.", do=[MATH("x² + 4x = x(x + 4)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Fully factorised", steps=[
        dict(say="Always use the highest common factor. 12 x plus 18 equals 2, bracket, 6 x plus 9. That is factorised, but not fully, because 6 x and 9 still share a 3.",
             do=[MATH("12x + 18 = 2(6x + 9)", x=80, y=170), T("6x and 9 still share **3** ✗", x=80, y=260, color=RED, at=4)]),
        dict(say="The H C F of 12 and 18 is 6. Fully factorised, it is 6, bracket, 2 x plus 3.", do=[B("12x + 18 = 6(2x + 3)", x=80, y=350, color=GREEN)]),
        dict(say="If one term is the H C F itself, a 1 is left inside. 5 x plus 5 is 5, bracket, x plus 1.", do=[MATH("5x + 5 = 5(x + 1)", x=80, y=450)]),
    ]),
    dict(kind="method", title="How do I factorise fully?", steps=[
        dict(say="Here is the method. Step 1: find the H C F of the numbers.", do=[T("1. Find the **HCF** of the numbers", x=80, y=170)]),
        dict(say="Step 2: find the letters that are in every term, with their lowest power.", do=[T("2. Letters in **every** term (lowest power)", x=80, y=260)]),
        dict(say="Step 3: write the H C F outside. Divide each term by it to fill the bracket.", do=[T("3. HCF outside; divide each term to fill the bracket", x=80, y=350)]),
        dict(say="Step 4: check by expanding, and check that nothing else is common inside the bracket.", do=[T("4. **Expand** to check; nothing else common?", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Numbers only", steps=[
        dict(say="Factorise 18 m minus 24. The H C F of 18 and 24 is 6. 18 m divided by 6 is 3 m. 24 divided by 6 is 4.",
             do=[MATH("18m − 24", x=80, y=170), MATH("HCF = 6", x=80, y=260)]),
        dict(say="The answer is 6, bracket, 3 m minus 4.", do=[B("6(3m − 4)", x=80, y=360, color=GREEN)]),
        PAUSE("2.4-k3", "Your turn. Factorise 9 A minus 9. Pause and work it out.", "Factorise 9a − 9."),
    ]),
    dict(kind="example", title="Check: 9(a − 1)", steps=[
        dict(say="The H C F is 9. 9 A divided by 9 is A, and 9 divided by 9 is 1. So it is 9, bracket, A minus 1. Don't forget the 1.", do=[MATH("9a − 9 = 9(a − 1)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Number and letter", steps=[
        dict(say="Factorise 14 A B plus 21 A squared. The H C F of 14 and 21 is 7, and both terms contain A. So the H C F is 7 A.",
             do=[MATH("14ab + 21a²", x=80, y=170), MATH("HCF = 7a", x=80, y=260, at=5)]),
        dict(say="14 A B divided by 7 A is 2 B. 21 A squared divided by 7 A is 3 A. The answer is 7 A, bracket, 2 B plus 3 A.", do=[B("7a(2b + 3a)", x=80, y=360, color=GREEN)]),
    ]),
    dict(kind="example", title="Three terms", steps=[
        dict(say="Factorise 6 x squared plus 9 x minus 3. The H C F is 3. It is not 3 x, because the last term, 3, has no x.",
             do=[MATH("6x² + 9x − 3", x=80, y=170), T("HCF = **3** (the 3 has no x)", x=80, y=260)]),
        dict(say="The answer is 3, bracket, 2 x squared plus 3 x minus 1.", do=[B("3(2x² + 3x − 1)", x=80, y=360, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ava factorises 16 x minus 24 fully. Which line goes wrong first?", do=LINES("Ava", "16x − 24, fully", ["HCF of 16 and 24 is 4", "16x − 24 = 4(4x − 6)"])),
        dict(say="Line 1 is wrong. 4 is a common factor, but not the highest. 4 x and 6 still share a 2. The H C F of 16 and 24 is 8.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="Fully factorised, 16 x minus 24 is 8, bracket, 2 x minus 3.", do=[B("16x − 24 = 8(2x − 3)", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Paving a path", steps=[
        dict(say="Factorising can save work. A path is made of two rectangles, both 3 metres wide. One is 17 metres long and the other is 13 metres long.",
             do=[E("🧱", 90, 170, 100), T("3 × 17 + 3 × 13", x=230, y=200)]),
        dict(say="Instead of two calculations, take out the 3. 3, bracket, 17 plus 13, is 3 times 30, which is 90 square metres.", do=[MATH("3(17 + 13) = 3 × 30 = 90 m²", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.4-k4", "One last question. Factorise 12 P Q plus 8 P fully. Pause the video and answer.", "Factorise 12pq + 8p fully."),
        dict(say="The H C F of 12 and 8 is 4, and both terms contain P. So the H C F is 4 P. 12 P Q divided by 4 P is 3 Q. 8 P divided by 4 P is 2. The answer is 4 P, bracket, 3 Q plus 2.",
             do=[MATH("HCF = 4p", x=80, y=190), B("4p(3q + 2)", x=80, y=290, color=GREEN, at=6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: factorising is the reverse of expanding.", do=[T("• Factorising is the **reverse** of expanding", x=80, y=170)]),
        dict(say="Take out the highest common factor, numbers and letters.", do=[T("• Take out the **highest** common factor", x=80, y=250)]),
        dict(say="Divide each term by the H C F to fill the bracket.", do=[T("• Divide each term to fill the bracket", x=80, y=330)]),
        dict(say="Check by expanding, and check that nothing else is common.", do=[T("• Check by expanding; nothing else common", x=80, y=410)]),
    ]),
]

VIDEOS["2.5"] = [
    dict(kind="hook", title="Two phone plans", steps=[
        dict(say="Plan A costs 20 dollars a month, plus 3 dollars per gigabyte. Plan B costs 8 dollars a month, plus 5 dollars per gigabyte.",
             do=[E("📶", 90, 170, 100), T("A: **$20 + $3** per GB · B: **$8 + $5** per GB", x=230, y=200)]),
        dict(say="For g gigabytes, the plans cost the same when 20 plus 3 g equals 8 plus 5 g.", do=[MATH("20 + 3g = 8 + 5g", x=230, y=300, color=BLUE)]),
        PAUSE("2.5-k1", "Find g. Pause the video and work it out.", "20 + 3g = 8 + 5g. Find g."),
    ]),
    dict(kind="hook", title="Both sides", steps=[
        dict(say="The unknown is on both sides. Take away the smaller amount, 3 g, from both sides. That leaves 20 equals 8 plus 2 g.",
             do=[MATH("20 + 3g = 8 + 5g", x=80, y=170), MATH("20 = 8 + 2g", x=80, y=260, at=5)]),
        dict(say="Subtract 8: 12 equals 2 g. Divide by 2: g equals 6. Both plans cost the same for 6 gigabytes.", do=[MATH("12 = 2g", x=80, y=350), B("g = 6", x=80, y=440, color=GREEN, at=3)]),
    ]),
    dict(kind="recall", title="Two-step equations", steps=[
        dict(say="Remember: to solve 3 x plus 5 equals 26, undo the operations. Subtract 5: 3 x equals 21. Divide by 3: x equals 7.",
             do=[MATH("3x + 5 = 26 → 3x = 21 → x = 7", x=80, y=180)]),
        dict(say="Do the same thing to both sides at every step, like keeping a balance level.", do=[T("same to **both sides**", x=80, y=280, color=BLUE)]),
    ]),
    dict(kind="idea", title="Unknowns on both sides", steps=[
        dict(say="When the unknown is on both sides, remove it from one side first. Usually take away the term with the smaller coefficient.",
             do=[STEPT("Working", [["start", "20 + 3g = 8 + 5g"], ["− 3g", "20 = 8 + 2g"], ["− 8", "12 = 2g"], ["÷ 2", "g = 6"]], y=170), ROW(0, 0.2), ROW(1, 3), ROW(2, 4.5), ROW(3, 6)]),
        PAUSE("2.5-k2", "Your turn. Solve 9 x equals 4 x plus 35. Pause the video and try it.", "Solve 9x = 4x + 35."),
    ]),
    dict(kind="idea", title="Check: 9x = 4x + 35", steps=[
        dict(say="Subtract 4 x from both sides: 5 x equals 35. Divide by 5: x equals 7.", do=[MATH("5x = 35", x=80, y=190), B("x = 7", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="idea", title="Equations with brackets", steps=[
        dict(say="If there are brackets, expand them first. 4, bracket, x minus 3, equals 2, bracket, x plus 5, becomes 4 x minus 12 equals 2 x plus 10.",
             do=[MATH("4(x − 3) = 2(x + 5)", x=80, y=170), MATH("4x − 12 = 2x + 10", x=80, y=260, at=5)]),
        dict(say="Subtract 2 x: 2 x minus 12 equals 10. Add 12: 2 x equals 22. So x equals 11.", do=[MATH("2x = 22", x=80, y=350), B("x = 11", x=80, y=440, color=GREEN, at=4)]),
    ]),
    dict(kind="method", title="How do I solve harder equations?", steps=[
        dict(say="Here is the method. Step 1: expand any brackets.", do=[T("1. **Expand** any brackets", x=80, y=170)]),
        dict(say="Step 2: collect the unknowns on one side, by subtracting the smaller x term from both sides.", do=[T("2. Subtract the **smaller** x term from both sides", x=80, y=260)]),
        dict(say="Step 3: collect the numbers on the other side.", do=[T("3. Collect the **numbers** on the other side", x=80, y=350)]),
        dict(say="Step 4: divide to find x, then check it in the original equation.", do=[T("4. Divide, then **check** in the original", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A negative answer", steps=[
        dict(say="Solve 2 x plus 11 equals 5 x plus 26. Subtract 2 x from both sides: 11 equals 3 x plus 26.", do=[MATH("2x + 11 = 5x + 26", x=80, y=170), MATH("11 = 3x + 26", x=80, y=260, at=4)]),
        dict(say="Subtract 26: negative 15 equals 3 x. Divide by 3: x equals negative 5. Negative answers are fine.", do=[MATH("−15 = 3x", x=80, y=350), B("x = −5", x=80, y=440, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Brackets first", steps=[
        dict(say="Solve 2, bracket, x plus 6, equals 30. One way is to expand: 2 x plus 12 equals 30.", do=[MATH("2(x + 6) = 30", x=80, y=170), MATH("2x + 12 = 30", x=80, y=260, at=4)]),
        PAUSE("2.5-k3", "Your turn. Finish it: what is x? Pause and work it out.", "Solve 2(x + 6) = 30."),
    ]),
    dict(kind="example", title="Check: x = 9", steps=[
        dict(say="Subtract 12: 2 x equals 18. Divide by 2: x equals 9. Check: 9 plus 6 is 15, and 2 times 15 is 30.", do=[MATH("2x = 18", x=80, y=190), B("x = 9", x=80, y=290, color=GREEN, at=2.6)]),
    ]),
    dict(kind="example", title="Angles in a triangle", steps=[
        dict(say="The angles of a triangle are x, 2 x plus 10, and 3 x minus 10 degrees. They add up to 180.", do=[MATH("x + (2x + 10) + (3x − 10) = 180", x=80, y=170)]),
        dict(say="The 10s cancel out, so 6 x equals 180, and x equals 30. The angles are 30, 70 and 80 degrees.", do=[MATH("6x = 180", x=80, y=260), B("x = 30 → 30°, 70°, 80°", x=80, y=360, color=GREEN, at=3)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Kai solves 6 x minus 5 equals 2 x plus 15. Which line goes wrong first?", do=LINES("Kai", "6x − 5 = 2x + 15", ["6x + 2x = 15 − 5", "8x = 10", "x = 1.25"])),
        dict(say="Line 1 is wrong. Subtracting 2 x from both sides gives 6 x minus 2 x. Adding 5 to both sides gives 15 plus 5.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6), dict(a="strike", id="l3", at=0.9)]),
        dict(say="So 4 x equals 20, and x equals 5.", do=[B("4x = 20 → x = 5", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Break-even", steps=[
        dict(say="Businesses solve this kind of equation all the time. A school club makes T-shirts. It pays 60 dollars for the printing screen, plus 4 dollars for each shirt, and sells each shirt for 10 dollars.",
             do=[E("👕", 90, 170, 100), T("cost **60 + 4n** · income **10n**", x=230, y=200)]),
        dict(say="It breaks even when 60 plus 4 N equals 10 N. That gives 6 N equals 60, so N equals 10 shirts. After that, every shirt makes a profit.",
             do=[MATH("60 + 4n = 10n → n = 10", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.5-k4", "One last question. Solve x plus 13 equals 4 x plus 1. Pause the video and answer.", "Solve x + 13 = 4x + 1."),
        dict(say="Subtract x from both sides: 13 equals 3 x plus 1. Subtract 1: 12 equals 3 x. So x equals 4.", do=[MATH("13 = 3x + 1", x=80, y=190), MATH("12 = 3x", x=80, y=280, at=3), B("x = 4", x=80, y=380, color=GREEN, at=4.6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: expand any brackets first.", do=[T("• **Expand** brackets first", x=80, y=170)]),
        dict(say="Get the unknown on one side by subtracting the smaller term.", do=[T("• Subtract the **smaller** unknown term", x=80, y=250)]),
        dict(say="Do the same to both sides at every step.", do=[T("• Same to both sides at every step", x=80, y=330)]),
        dict(say="And check the answer in the original equation.", do=[T("• Check in the original equation", x=80, y=410)]),
    ]),
]

VIDEOS["2.6"] = [
    dict(kind="hook", title="Lift limit", steps=[
        dict(say="A sign in a lift says: maximum 8 people.", do=[E("🛗", 90, 170, 100), T("**maximum 8 people**", x=230, y=200)]),
        dict(say="Can exactly 8 people use the lift? Think about how you would write the rule with p for the number of people.", do=[T("exactly 8 people: allowed?", x=230, y=300)]),
        PAUSE("2.6-k1", "Which inequality means maximum 8 people? Pause the video and choose.", "'Maximum 8 people' means …"),
    ]),
    dict(kind="hook", title="Maximum 8", steps=[
        dict(say="Maximum 8 means 8 is allowed, but 9 is not. So p is less than or equal to 8.", do=[B("p ≤ 8", x=80, y=190, color=GREEN), T("8 is **allowed**", x=360, y=200)]),
        dict(say="A ride at a fair says: riders must be at least 140 centimetres, and under 195 centimetres. Is exactly 140 allowed? Is exactly 195?",
             do=[E("🎡", 90, 300, 90), T("at least **140 cm** and under **195 cm**", x=230, y=330)]),
    ]),
    dict(kind="recall", title="Less than, greater than", steps=[
        dict(say="Remember: x is greater than 3 means x is more than 3, but 3 itself is not included. On a number line, it has an open circle at 3.",
             do=[MATH("x > 3", x=80, y=170), INEQ(80, 250, 760, min=-1, max=8, a=3, dir="right", at=3)]),
    ]),
    dict(kind="idea", title="Less than or equal to", steps=[
        dict(say="This sign means less than or equal to. This one means greater than or equal to. The boundary is included, so we draw a closed, filled circle.",
             do=[TBL(["Words", "Inequality", "Circle"], [["at most 8", "p ≤ 8", "closed at 8"], ["at least 140", "h ≥ 140", "closed at 140"], ["under 195", "h < 195", "open at 195"]], y=160), ROW(0, 0.3), ROW(1, 3.2), ROW(2, 6)]),
        dict(say="Here is x greater than or equal to 2. The closed circle shows 2 is included.", do=[INEQ(80, 400, 760, min=-3, max=6, a=2, ca=True, dir="right")]),
        PAUSE("2.6-k2", "Your turn. How is x greater than or equal to 3 shown on a number line? Pause the video and choose.", "x ≥ 3 is shown with …"),
    ]),
    dict(kind="idea", title="Check: x ≥ 3", steps=[
        dict(say="3 is included, so it is a closed circle at 3, with an arrow to the right.", do=[INEQ(80, 180, 760, min=-1, max=8, a=3, ca=True, dir="right"), B("closed circle at 3", x=80, y=420, color=GREEN, at=1)]),
    ]),
    dict(kind="idea", title="Intervals", steps=[
        dict(say="Two conditions together make an interval. The ride rule is: 140 is less than or equal to h, and h is less than 195. Closed circle at 140, open circle at 195.",
             do=[MATH("140 ≤ h < 195", x=80, y=170, color=BLUE)]),
        dict(say="This line shows negative 2 is less than or equal to x, which is less than 3. The integers in it are negative 2, negative 1, 0, 1 and 2. 3 is not included.",
             do=[INEQ(80, 250, 760, min=-4, max=5, a=-2, b=3, ca=True), T("integers: **−2, −1, 0, 1, 2**", x=80, y=480, at=5)]),
    ]),
    dict(kind="method", title="How do I write, show and solve inequalities?", steps=[
        dict(say="Here is the method. Step 1: decide if each boundary is included, with a closed circle, or not, with an open circle.", do=[T("1. Included? ≤ ≥ **closed** · < > **open**", x=80, y=170)]),
        dict(say="Step 2: for an interval, write it in order, with the smallest number on the left.", do=[T("2. Intervals: **smallest on the left**", x=80, y=260)]),
        dict(say="Step 3: solve an inequality like an equation, doing the same to both sides.", do=[T("3. **Solve** like an equation", x=80, y=350)]),
        dict(say="Step 4: when you list integers, check each boundary carefully.", do=[T("4. Check the **boundaries** when listing integers", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Reading a number line", steps=[
        dict(say="A number line shows an open circle at negative 1, and a closed circle at 4, joined together. Write the inequality.", do=[INEQ(80, 160, 760, min=-3, max=6, a=-1, b=4, cb=True)]),
        dict(say="Open at negative 1, so negative 1 is less than x. Closed at 4, so x is less than or equal to 4.", do=[B("−1 < x ≤ 4", x=80, y=400, color=GREEN, at=3)]),
        PAUSE("2.6-k3", "Your turn. What is the largest integer with x less than 4.5? Pause and work it out.", "Largest integer with x < 4.5?"),
    ]),
    dict(kind="example", title="Check: x < 4.5", steps=[
        dict(say="The integers less than 4.5 are 4, 3, 2 and so on. The largest is 4.", do=[INEQ(80, 160, 760, min=0, max=7, a=4.5, dir="left"), B("4", x=80, y=400, color=GREEN, at=2)]),
    ]),
    dict(kind="example", title="Solving", steps=[
        dict(say="Solve 5 x minus 3 is greater than 2 x plus 9. Subtract 2 x from both sides: 3 x minus 3 is greater than 9.", do=[MATH("5x − 3 > 2x + 9", x=80, y=170), MATH("3x − 3 > 9", x=80, y=260, at=4)]),
        dict(say="Add 3: 3 x is greater than 12. Divide by 3: x is greater than 4.", do=[MATH("3x > 12", x=80, y=350), B("x > 4", x=80, y=440, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Integer solutions", steps=[
        dict(say="Find the integers n where 7 is less than or equal to 2 n plus 1, which is less than 15. Subtract 1 from every part: 6 is less than or equal to 2 n, which is less than 14.",
             do=[MATH("7 ≤ 2n + 1 < 15", x=80, y=170), MATH("6 ≤ 2n < 14", x=80, y=260, at=6)]),
        dict(say="Divide every part by 2: 3 is less than or equal to n, which is less than 7. So n is 3, 4, 5 or 6.", do=[MATH("3 ≤ n < 7", x=80, y=350), B("n = 3, 4, 5, 6", x=80, y=440, color=GREEN, at=4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Mo shows x is at least negative 2 on a number line. Which line is wrong?", do=LINES("Mo", "x is at least −2", ["at least −2 means x > −2", "open circle at −2, arrow right"])),
        dict(say="Line 1 is wrong. At least negative 2 includes negative 2. So x is greater than or equal to negative 2.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="The circle at negative 2 must be closed.", do=[B("x ≥ −2: closed circle", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Safe temperatures", steps=[
        dict(say="Food safety rules use inequalities. A fridge should keep food at 5 degrees Celsius or colder. That is t less than or equal to 5.",
             do=[E("🧊", 90, 170, 100), MATH("fridge: t ≤ 5 °C", x=230, y=190)]),
        dict(say="A freezer should be at negative 18 degrees or colder. That is t less than or equal to negative 18.", do=[E("❄️", 90, 320, 90), MATH("freezer: t ≤ −18 °C", x=230, y=340)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.6-k4", "One last question. Solve 2 x minus 1 is greater than or equal to 9. Pause the video and choose.", "Solve 2x − 1 ≥ 9."),
        dict(say="Add 1: 2 x is greater than or equal to 10. Divide by 2: x is greater than or equal to 5.", do=[MATH("2x ≥ 10", x=80, y=190), B("x ≥ 5", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: less than or equal to, and greater than or equal to, include the boundary. Use a closed circle.", do=[T("• ≤ ≥ include the boundary: **closed** circle", x=80, y=170)]),
        dict(say="Less than and greater than do not include it. Use an open circle.", do=[T("• < > do not: **open** circle", x=80, y=250)]),
        dict(say="Write intervals with the smallest number on the left.", do=[T("• Intervals: a ≤ x < b, smallest on the left", x=80, y=330)]),
        dict(say="Solve them like equations, and list integers carefully at each boundary.", do=[T("• Solve like equations; check the boundaries", x=80, y=410)]),
    ]),
]
