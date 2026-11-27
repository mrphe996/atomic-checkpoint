# -*- coding: utf-8 -*-
"""Stage 9 · Unit 9 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

VIDEOS = {}

VIDEOS["9.1"] = [
    dict(kind="hook", title="Bowling pins", steps=[
        dict(say="Bowling pins are set out in a triangle. The front row has 1 pin, the next row 2, then 3, and so on. The running totals are 1, 3, 6, 10, 15.",
             do=[E("🎳", 90, 170, 100), MATH("1, 3, 6, 10, 15, …", x=230, y=190)]),
        PAUSE("9.1-k1", "What are the next two totals? Pause the video and work them out.", "Next two totals?"),
    ]),
    dict(kind="hook", title="21 and 28", steps=[
        dict(say="The totals grow by 2, then 3, then 4, then 5. So next we add 6, then 7: 21 and 28.", do=[B("15 + 6 = 21, 21 + 7 = 28", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Term-to-term rules", steps=[
        dict(say="Remember: a term-to-term rule tells you how to get from one term to the next. 5, 9, 13, 17: add 4 each time.", do=[MATH("5, 9, 13, 17 … : + 4", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Linear and non-linear", steps=[
        dict(say="In a linear sequence, the terms change by the same amount each time. In a non-linear sequence, the change is different each time.",
             do=[T("**linear**: same change · **non-linear**: changing", x=80, y=170)]),
        dict(say="Look at the differences. For 1, 3, 6, 10, 15, the first differences are 2, 3, 4, 5. The second differences are all 1. Constant second differences mean the sequence is quadratic.",
             do=[TBL(["Sequence", "1", "3", "6", "10", "15"], [["1st differences", "", "2", "3", "4", "5"], ["2nd differences", "", "", "1", "1", "1"]], y=260), ROW(0, 5), ROW(1, 9)]),
        PAUSE("9.1-k2", "Your turn. 1 and a half, 4, 6 and a half, 9. Is this sequence linear, or non-linear? Pause the video and choose.", "1½, 4, 6½, 9 is …"),
    ]),
    dict(kind="idea", title="Check: linear", steps=[
        dict(say="It is linear. It goes up by 2 and a half every time.", do=[B("linear: + 2½", x=80, y=190, color=GREEN)]),
        dict(say="Rules can multiply too. Multiply by 3 from 2 gives 2, 6, 18, 54. Always use the previous term each time.", do=[MATH("× 3: 2, 6, 18, 54, …", x=80, y=300), T("use the **previous** term", x=80, y=390)]),
    ]),
    dict(kind="method", title="How do I describe a sequence?", steps=[
        dict(say="Here is the method. Step 1: find the differences between terms.", do=[T("1. Find the **differences**", x=80, y=170)]),
        dict(say="Step 2: the same difference means linear. Changing differences mean non-linear.", do=[T("2. Same → **linear** · changing → **non-linear**", x=80, y=260)]),
        dict(say="Step 3: for non-linear, look at second differences, or a multiplying rule.", do=[T("3. **2nd differences**, or × rule", x=80, y=350)]),
        dict(say="Step 4: use the pattern, and check one more step.", do=[T("4. Continue; **check**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A fractional step", steps=[
        dict(say="The first term is 3, and the rule is add 3 quarters. The terms are 3, 3 and 3 quarters, 4 and a half, 5 and a quarter.", do=[MATH("3, 3¾, 4½, 5¼", x=80, y=180)]),
        dict(say="Next term of 50, 41, 33, 26, 20? The differences are minus 9, minus 8, minus 7, minus 6. They go down by 1 each time.", do=[MATH("−9, −8, −7, −6, …", x=80, y=280)]),
        PAUSE("9.1-k3", "Your turn. What is the next term of 50, 41, 33, 26, 20? Pause and work it out.", "Next term of 50, 41, 33, 26, 20?"),
    ]),
    dict(kind="example", title="Check: 15", steps=[
        dict(say="The next difference is minus 5. 20 minus 5 is 15.", do=[B("20 − 5 = 15", x=80, y=190, color=GREEN)]),
        dict(say="A two-step rule: start at 1, double, then add 3. 1, 5, 13, 29.", do=[MATH("× 2 then + 3: 1, 5, 13, 29", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="The first term is 2, and the rule is square the term. Rosa writes the sequence. Which line is wrong?", do=LINES("Rosa", "first term 2, rule: square the term", ["2, 4, 4, 4"])),
        dict(say="Line 1 is wrong. She squared the first term every time. Each term comes from the previous term.", do=[dict(a="cross", id="l1")]),
        dict(say="2, 4, 16, 256.", do=[B("2, 4, 16, 256", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Cells", steps=[
        dict(say="Bacteria can split in two every 20 minutes. 1, 2, 4, 8, 16: a non-linear sequence that grows very fast.", do=[E("🦠", 90, 170, 100), MATH("1, 2, 4, 8, 16, … (× 2)", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("9.1-k4", "One last question. 3, 6, 12, 24. Is it non-linear, times 2, or linear? Pause the video and choose.", "3, 6, 12, 24 is …"),
        dict(say="The differences are 3, 6, 12. They change, so it is non-linear. The rule is times 2.", do=[B("non-linear (× 2)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: linear sequences have a constant difference.", do=[T("• Linear: constant difference", x=80, y=170)]),
        dict(say="Non-linear sequences have changing differences, or a multiplying rule.", do=[T("• Non-linear: changing, or ×", x=80, y=250)]),
        dict(say="Constant second differences mean quadratic.", do=[T("• Constant 2nd differences → quadratic", x=80, y=330)]),
        dict(say="Rules act on the previous term.", do=[T("• Use the previous term", x=80, y=410)]),
    ]),
]

VIDEOS["9.2"] = [
    dict(kind="hook", title="Cinema seats", steps=[
        dict(say="In a cinema, row 1 has 18 seats, row 2 has 22, row 3 has 26, and so on. Listing 40 rows would take a long time.",
             do=[E("🎬", 90, 170, 100), MATH("18, 22, 26, …", x=230, y=190)]),
        PAUSE("9.2-k1", "How many seats are in row 40? Pause the video and work it out.", "Seats in row 40?"),
    ]),
    dict(kind="hook", title="174 seats", steps=[
        dict(say="From row 1 to row 40 there are 39 steps of 4. 18 plus 39 times 4 is 18 plus 156, which is 174 seats. A formula makes this quicker.", do=[MATH("18 + 39 × 4 = 174", x=80, y=190), B("174 seats", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="recall", title="Position-to-term", steps=[
        dict(say="Remember: the Nth term gives any term from its position. 3 N minus 1 gives 2, 5, 8, and so on.", do=[MATH("3n − 1 → 2, 5, 8, …", x=80, y=190)]),
    ]),
    dict(kind="idea", title="The nth term", steps=[
        dict(say="The difference tells you the multiple of N. Then compare with the sequence, and adjust.", do=[T("difference **d** → **dn**, then adjust", x=80, y=170)]),
        dict(say="For example: 7, 10, 13. The difference is 3, so start with 3 N: 3, 6, 9. Each term is 4 more. So the Nth term is 3 N plus 4.",
             do=[MATH("3n: 3, 6, 9 → + 4 → 3n + 4", x=80, y=270)]),
        PAUSE("9.2-k2", "Your turn. Find the Nth term of 18, 22, 26. Pause the video and try it.", "nth term of 18, 22, 26?"),
    ]),
    dict(kind="idea", title="Check: 4n + 14", steps=[
        dict(say="The difference is 4, so 4 N: 4, 8, 12. Each term is 14 more. The Nth term is 4 N plus 14. Row 40: 160 plus 14 is 174.", do=[B("4n + 14", x=80, y=190, color=GREEN), MATH("4 × 40 + 14 = 174 ✓", x=80, y=300)]),
        dict(say="Some sequences are based on N squared: 1, 4, 9, 16, 25. For example, 2 N squared gives 2, 8, 18, 32.", do=[MATH("n²: 1, 4, 9, 16 · 2n²: 2, 8, 18, 32", x=80, y=400)]),
    ]),
    dict(kind="method", title="How do I find the nth term?", steps=[
        dict(say="Here is the method. Step 1: find the difference, D. Start with D N.", do=[T("1. Difference **d** → **dn**", x=80, y=170)]),
        dict(say="Step 2: compare D N with the sequence, and add or subtract.", do=[T("2. Compare and **adjust**", x=80, y=260)]),
        dict(say="Step 3: if it looks quadratic, compare with N squared.", do=[T("3. Quadratic? Compare with **n²**", x=80, y=350)]),
        dict(say="Step 4: check with a term.", do=[T("4. **Check** with a term", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Decreasing", steps=[
        dict(say="Find the Nth term of 40, 37, 34, 31. The difference is minus 3, so minus 3 N: minus 3, minus 6, minus 9. Each term is 43 more. So 43 minus 3 N.",
             do=[MATH("−3n: −3, −6, −9 → + 43", x=80, y=180), B("43 − 3n", x=80, y=290, color=GREEN, at=9)]),
        PAUSE("9.2-k3", "Your turn. Write the first four terms of N squared plus 3. Pause and work it out.", "First four terms of n² + 3?"),
    ]),
    dict(kind="example", title="Check: n² + 3", steps=[
        dict(say="1 plus 3, 4 plus 3, 9 plus 3, 16 plus 3: 4, 7, 12, 19.", do=[B("4, 7, 12, 19", x=80, y=190, color=GREEN)]),
        dict(say="Is 100 in the sequence 4 N plus 14? 4 N plus 14 equals 100 gives N equals 21.5. That is not a whole number, so no.", do=[MATH("4n + 14 = 100 → n = 21.5 → no", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Finn finds the Nth term of 5, 8, 11, 14. Which line is wrong?", do=LINES("Finn", "nth term of 5, 8, 11, 14", ["difference 3", "nth term n + 3"])),
        dict(say="Line 2 is wrong. The difference is the multiple of N, so start with 3 N.", do=[dict(a="cross", id="l2")]),
        dict(say="3 N gives 3, 6, 9. Add 2. The Nth term is 3 N plus 2.", do=[B("3n + 2", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Saving up", steps=[
        dict(say="If you have 50 dollars and save 12 dollars a week, after N weeks you have 12 N plus 50. Planners use Nth terms like this all the time.", do=[E("🐷", 90, 170, 100), MATH("12n + 50", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("9.2-k4", "One last question. Which term of 2 N plus 1 is 41? Pause the video and answer.", "Which term of 2n + 1 is 41?"),
        dict(say="2 N plus 1 equals 41. 2 N is 40, so N is 20. It is the 20th term.", do=[B("2n + 1 = 41 → n = 20", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: linear Nth term: D N, then adjust.", do=[T("• Linear: dn + adjustment", x=80, y=170)]),
        dict(say="Check with the first term.", do=[T("• Check with the first term", x=80, y=250)]),
        dict(say="Quadratic: compare with N squared.", do=[T("• Quadratic: compare with n²", x=80, y=330)]),
        dict(say="Solve an equation to test if a number is in the sequence.", do=[T("• Solve to test a number", x=80, y=410)]),
    ]),
]

VIDEOS["9.3"] = [
    dict(kind="hook", title="A tile app", steps=[
        dict(say="A tiling app takes the side of a square tile, X centimetres. It squares it, then adds 4 square centimetres for the grout. The output is 85.",
             do=[E("🧮", 90, 170, 100), MATH("x → square → + 4 → 85", x=230, y=190)]),
        PAUSE("9.3-k1", "What was the input? Give the positive answer. Pause the video and work it out.", "Input for output 85 (positive)?"),
    ]),
    dict(kind="hook", title="Work backwards", steps=[
        dict(say="Work backwards. 85 minus 4 is 81. The square root of 81 is 9. So the input was 9.", do=[MATH("85 − 4 = 81 → √81 = 9", x=80, y=190), B("x = 9", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="recall", title="Function machines", steps=[
        dict(say="Remember: X, times 3, add 1, gives Y. So Y equals 3 X plus 1.", do=[MATH("x → × 3 → + 1 → y   ·   y = 3x + 1", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Machines with powers", steps=[
        dict(say="A function machine can include powers. X, square, add 4, gives Y equals X squared plus 4.",
             do=[MATH("x → square → + 4 → y = x² + 4", x=80, y=170), TBL(["x", "0", "1", "2", "3"], [["y", "4", "5", "8", "13"]], y=280), ROW(0, 4)]),
        PAUSE("9.3-k2", "Your turn. Find Y when X is negative 3. Pause the video and try it.", "y = x² + 4 at x = −3?"),
    ]),
    dict(kind="idea", title="Check: 13", steps=[
        dict(say="Negative 3 squared is 9. 9 plus 4 is 13. So X equals 3 and X equals negative 3 both give 13.", do=[B("(−3)² + 4 = 13", x=80, y=190, color=GREEN)]),
        dict(say="Order matters. Square, then times 2, gives Y equals 2 X squared.", do=[MATH("square → × 2 → y = 2x²", x=80, y=300)]),
        PAUSE("9.3-k3", "Your turn. What about times 2, then square: is it Y equals 4 X squared, or Y equals 2 X squared? Pause the video and choose.", "'× 2 then square' is …"),
    ]),
    dict(kind="idea", title="Check: 4x²", steps=[
        dict(say="Times 2 then square is 2 X, all squared. That is 4 X squared. Brackets keep the order.", do=[B("(2x)² = 4x²", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I represent functions?", steps=[
        dict(say="Here is the method. Step 1: follow the steps in order to make a table of values.", do=[T("1. Steps **in order** → table", x=80, y=170)]),
        dict(say="Step 2: write the equation, using brackets to keep the order.", do=[T("2. Equation with **brackets**", x=80, y=260)]),
        dict(say="Step 3: draw a mapping diagram if you need one.", do=[T("3. **Mapping** diagram", x=80, y=350)]),
        dict(say="Step 4: to find an input, use inverse operations in reverse order.", do=[T("4. **Inverse** operations, reversed", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Machines and equations", steps=[
        dict(say="X, add 1, then square, gives Y equals X plus 1, all squared.", do=[MATH("x → + 1 → square → y = (x + 1)²", x=80, y=180)]),
        dict(say="Y equals X cubed minus 5. The output is 59. Add 5: 64. The cube root of 64 is 4.", do=[MATH("59 + 5 = 64 → ∛64 = 4", x=80, y=280)]),
        dict(say="Halve X, then square, gives Y equals X squared over 4.", do=[MATH("(x/2)² = x²/4", x=80, y=380)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Jay writes X, add 3, then square, as an equation. Which line is wrong?", do=LINES("Jay", "x → + 3 → square", ["y = x + 3²"])),
        dict(say="Line 1 is wrong. The square must apply to the whole of X plus 3.", do=[dict(a="cross", id="l1")]),
        dict(say="Y equals X plus 3, all squared.", do=[B("y = (x + 3)²", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Spreadsheets", steps=[
        dict(say="A spreadsheet formula is a function machine. Type a value in one cell, and the formula turns it into an output in another.", do=[E("📊", 90, 170, 100), T("input cell → **formula** → output cell", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("9.3-k4", "One last question. Y equals X cubed. Find Y when X is negative 2. Pause the video and answer.", "y = x³ at x = −2?"),
        dict(say="Negative 2 times negative 2 times negative 2 is negative 8.", do=[B("(−2)³ = −8", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: follow the steps in order.", do=[T("• Steps in order", x=80, y=170)]),
        dict(say="Use brackets to show the order in an equation.", do=[T("• Brackets show the order", x=80, y=250)]),
        dict(say="Work backwards with inverse operations, in reverse order.", do=[T("• Inverse operations, reversed", x=80, y=330)]),
        dict(say="With squares, two inputs can give the same output.", do=[T("• Squares: two inputs, one output", x=80, y=410)]),
    ]),
]
