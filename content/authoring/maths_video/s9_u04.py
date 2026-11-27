# -*- coding: utf-8 -*-
"""Stage 9 · Unit 4 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, INEQ
from .s7_u04 import TBL, ROW
from .s7_u07 import F

VIDEOS = {}

VIDEOS["4.1"] = [
    dict(kind="hook", title="Two phone plans", steps=[
        dict(say="Plan A costs 20 dollars a month, plus 10 cents per minute. Plan B costs 8 dollars a month, plus 25 cents per minute.",
             do=[E("📱", 90, 170, 100), T("A: **$20 + $0.10** a minute", x=230, y=180), T("B: **$8 + $0.25** a minute", x=230, y=260, at=4)]),
        PAUSE("4.1-k1", "For how many minutes do the two plans cost the same? Pause the video and work it out.", "Minutes for equal cost?"),
    ]),
    dict(kind="hook", title="80 minutes", steps=[
        dict(say="Let M be the minutes. Plan A costs 20 plus 0.1 M. Plan B costs 8 plus 0.25 M. Set them equal.", do=[MATH("20 + 0.1m = 8 + 0.25m", x=80, y=170)]),
        dict(say="Take away 8 and 0.1 M from both sides: 12 equals 0.15 M. So M is 80 minutes.", do=[MATH("12 = 0.15m", x=80, y=270), B("m = 80", x=80, y=370, color=GREEN, at=5)]),
        dict(say="Check: plan A is 20 plus 8, which is 28. Plan B is 8 plus 20, which is 28.", do=[MATH("A: 28   B: 28 ✓", x=80, y=460)]),
    ]),
    dict(kind="recall", title="Solving", steps=[
        dict(say="Remember: do the same to both sides. 3 X plus 4 equals 19, so 3 X equals 15, and X equals 5.", do=[MATH("3x + 4 = 19 → 3x = 15 → x = 5", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Brackets", steps=[
        dict(say="To construct an equation, choose a letter for the unknown, and write both sides in algebra.", do=[T("choose a **letter**, write **both sides**", x=80, y=170)]),
        dict(say="If there are brackets, expand them first. Then collect the unknowns on the side with more of them.", do=[T("expand brackets, then **collect** the unknowns", x=80, y=260)]),
        PAUSE("4.1-k2", "Your turn. Solve 3, bracket, 2 X minus 1, equals 2, bracket, X plus 7. Pause the video and try it.", "Solve 3(2x − 1) = 2(x + 7)."),
    ]),
    dict(kind="idea", title="Check", steps=[
        dict(say="Expand: 6 X minus 3 equals 2 X plus 14. Take 2 X from both sides, and add 3: 4 X equals 17. So X is 4.25.",
             do=[MATH("6x − 3 = 2x + 14", x=80, y=170), MATH("4x = 17", x=80, y=260, at=5), B("x = 4.25", x=80, y=360, color=GREEN, at=8)]),
    ]),
    dict(kind="idea", title="Fractions", steps=[
        dict(say="Clear fractions by multiplying every term by the denominator. X plus 5, over 3, equals X minus 1. Times 3: X plus 5 equals 3 X minus 3. So X is 4.",
             do=[MATH(F("x+5", 3) + " = x − 1", x=80, y=170), MATH("x + 5 = 3x − 3 → x = 4", x=80, y=300, at=5)]),
        dict(say="With two fractions, multiply by a common multiple of the denominators.", do=[T("two fractions → × a **common multiple**", x=80, y=410, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I solve it?", steps=[
        dict(say="Here is the method. Step 1: say what the letter stands for, and write the equation.", do=[T("1. Define the letter; **write** the equation", x=80, y=170)]),
        dict(say="Step 2: expand any brackets, and clear any fractions.", do=[T("2. **Expand**; clear fractions", x=80, y=260)]),
        dict(say="Step 3: collect the unknowns on one side, and the numbers on the other.", do=[T("3. **Collect** terms; do the same to both sides", x=80, y=350)]),
        dict(say="Step 4: check your answer in the original problem.", do=[T("4. **Check** in the problem", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Think of a number", steps=[
        dict(say="I think of a number, double it, add 3, then double the result. I get 58. Write 2, bracket, 2 N plus 3, equals 58.", do=[MATH("2(2n + 3) = 58", x=80, y=180)]),
        dict(say="Divide by 2: 2 N plus 3 equals 29. Take 3: 2 N equals 26. So N is 13.", do=[MATH("2n + 3 = 29 → 2n = 26", x=80, y=280), B("n = 13", x=80, y=380, color=GREEN, at=6)]),
        PAUSE("4.1-k3", "Your turn. Solve X over 2, plus X over 5, equals 14. Pause and work it out.", "Solve x/2 + x/5 = 14."),
    ]),
    dict(kind="example", title="Check: x/2 + x/5 = 14", steps=[
        dict(say="Multiply every term by 10: 5 X plus 2 X equals 140. So 7 X equals 140, and X is 20.",
             do=[MATH("× 10: 5x + 2x = 140", x=80, y=180), B("7x = 140 → x = 20", x=80, y=290, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Angles in a triangle", steps=[
        dict(say="The angles of a triangle are X, 2 X plus 15, and 3 X minus 15. They add up to 180 degrees. So 6 X equals 180, and X is 30. The angles are 30, 75 and 75 degrees.",
             do=[MATH("x + (2x + 15) + (3x − 15) = 180", x=80, y=180), MATH("6x = 180 → x = 30", x=80, y=280, at=7), B("30°, 75°, 75°", x=80, y=380, color=GREEN, at=11)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Eva solves X over 3, plus 2, equals 6. Which line is wrong?", do=LINES("Eva", "x/3 + 2 = 6", ["× 3: x + 2 = 18", "x = 16"])),
        dict(say="Line 1 is wrong. Every term must be multiplied by 3, including the 2.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="X plus 6 equals 18, so X is 12.", do=[B("x + 6 = 18 → x = 12", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Choosing a tariff", steps=[
        dict(say="Choosing between phone plans, taxis, or energy tariffs comes down to one equation: cost A equals cost B. Below the answer one is cheaper, and above it, the other is.",
             do=[E("💡", 90, 170, 100), B("cost A = cost B", x=230, y=190, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.1-k4", "One last question. Solve 2 X plus 9 equals 5 X. Pause the video and answer.", "Solve 2x + 9 = 5x."),
        dict(say="Take 2 X from both sides: 9 equals 3 X. So X is 3.", do=[B("9 = 3x → x = 3", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: say what your letter means, and write the equation.", do=[T("• Define the letter; write the equation", x=80, y=170)]),
        dict(say="Expand brackets, clear fractions, and collect terms.", do=[T("• Expand, clear fractions, collect", x=80, y=250)]),
        dict(say="Do the same to both sides.", do=[T("• Same to both sides", x=80, y=330)]),
        dict(say="Check in the original problem.", do=[T("• Check in the problem", x=80, y=410)]),
    ]),
]

VIDEOS["4.2"] = [
    dict(kind="hook", title="Café order", steps=[
        dict(say="At a café, 2 juices and 3 muffins cost 13 dollars. 2 juices and 1 muffin cost 7 dollars.",
             do=[E("🧁", 90, 170, 100), T("2 juices + 3 muffins = **$13**", x=230, y=180), T("2 juices + 1 muffin = **$7**", x=230, y=260, at=3)]),
        PAUSE("4.2-k1", "How much is one muffin? Pause the video and work it out.", "Muffin price?"),
    ]),
    dict(kind="hook", title="Compare the orders", steps=[
        dict(say="The two orders have the same juices. The difference is 2 muffins, and 13 minus 7 is 6 dollars. So one muffin costs 3 dollars.",
             do=[MATH("2 muffins = 13 − 7 = $6", x=80, y=190), B("muffin = $3", x=80, y=300, color=GREEN, at=6)]),
        dict(say="Then 2 juices plus 3 is 7, so a juice costs 2 dollars.", do=[MATH("2j + 3 = 7 → j = $2", x=80, y=400)]),
    ]),
    dict(kind="recall", title="Substitution", steps=[
        dict(say="Remember: if Y is 4, then 3 X plus Y equals 19 gives 3 X equals 15, so X is 5.", do=[MATH("y = 4: 3x + 4 = 19 → x = 5", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Elimination", steps=[
        dict(say="Simultaneous equations are two equations with the same two unknowns, both true at once.", do=[T("two equations, two unknowns, **both true**", x=80, y=170)]),
        dict(say="To eliminate a letter, match its coefficients. If they are the same, subtract. If they have opposite signs, add.",
             do=[TBL(["Equations", "Action"], [["3x + 2y = 16,  x + 2y = 8", "subtract → 2x = 8"], ["2x + 3y = 13,  x + y = 5", "× 2 second, then subtract"]], y=260), ROW(0, 3), ROW(1, 6)]),
        PAUSE("4.2-k2", "Your turn. X plus Y equals 10, and X minus Y equals 4. Find X. Pause the video and try it.", "x + y = 10, x − y = 4. x?"),
    ]),
    dict(kind="idea", title="Check: add them", steps=[
        dict(say="The Y terms have opposite signs, so add the equations. 2 X equals 14, so X is 7. Then Y is 3.", do=[MATH("(x + y) + (x − y) = 10 + 4", x=80, y=180), B("2x = 14 → x = 7", x=80, y=290, color=GREEN, at=5)]),
    ]),
    dict(kind="idea", title="Substitution", steps=[
        dict(say="If one equation gives a letter directly, like Y equals 2 X minus 1, substitute it into the other equation.", do=[T("a letter given directly → **substitute** it", x=80, y=170)]),
        dict(say="Always check the pair of answers in both of the original equations.", do=[T("check in **both** equations", x=80, y=260, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I solve simultaneous equations?", steps=[
        dict(say="Here is the method. Step 1: label the equations 1 and 2.", do=[T("1. **Label** the equations", x=80, y=170)]),
        dict(say="Step 2: make the coefficients of one letter match, multiplying if you need to.", do=[T("2. **Match** a coefficient", x=80, y=260)]),
        dict(say="Step 3: add or subtract to eliminate it. Solve, then substitute back.", do=[T("3. Add or subtract; **substitute** back", x=80, y=350)]),
        dict(say="Step 4: check in both equations.", do=[T("4. **Check** in both", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Multiply first", steps=[
        dict(say="Solve 3 X plus 2 Y equals 12, and X plus Y equals 5. Double the second equation: 2 X plus 2 Y equals 10.", do=[MATH("3x + 2y = 12   ·   x + y = 5", x=80, y=170), MATH("× 2: 2x + 2y = 10", x=80, y=260, at=6)]),
        dict(say="Subtract: X equals 2. Then Y is 3.", do=[B("x = 2,  y = 3", x=80, y=360, color=GREEN)]),
        PAUSE("4.2-k3", "Your turn. Y equals 2 X minus 1, and 3 X plus Y equals 14. Find X. Pause and work it out.", "y = 2x − 1, 3x + y = 14. x?"),
    ]),
    dict(kind="example", title="Check: substitute", steps=[
        dict(say="Replace Y with 2 X minus 1: 3 X plus 2 X minus 1 equals 14. So 5 X equals 15, and X is 3. Then Y is 5.",
             do=[MATH("3x + (2x − 1) = 14", x=80, y=180), B("5x = 15 → x = 3", x=80, y=290, color=GREEN, at=6)]),
    ]),
    dict(kind="example", title="Two numbers", steps=[
        dict(say="Two numbers add to 37, and their difference is 13. X plus Y equals 37, and X minus Y equals 13. Add: 2 X equals 50. So the numbers are 25 and 12.",
             do=[MATH("x + y = 37   ·   x − y = 13", x=80, y=180), B("25 and 12", x=80, y=290, color=GREEN, at=9)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Lucy solves 3 X plus 2 Y equals 8, and 3 X minus 2 Y equals 4, by subtracting. Which line is wrong?", do=LINES("Lucy", "3x + 2y = 8, 3x − 2y = 4", ["(1) − (2): 0x + 0y = 4"])),
        dict(say="Line 1 is wrong. 2 Y minus negative 2 Y is 4 Y, not zero.", do=[dict(a="cross", id="l1")]),
        dict(say="So 4 Y equals 4, and Y is 1. Then 3 X equals 6, so X is 2.", do=[B("4y = 4 → y = 1,  x = 2", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Mixing", steps=[
        dict(say="Businesses use simultaneous equations to mix ingredients to a target, and to find the price where income equals costs.", do=[E("🏭", 90, 170, 100), T("mixes, prices and break-even points", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.2-k4", "One last question. X plus Y equals 5, and X equals 1. What is Y? Pause the video and answer.", "x + y = 5, x = 1. y?"),
        dict(say="1 plus Y equals 5, so Y is 4.", do=[B("y = 4", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: two equations, with two unknowns.", do=[T("• Two equations, two unknowns", x=80, y=170)]),
        dict(say="Elimination: match a coefficient, then add or subtract.", do=[T("• Match, then add or subtract", x=80, y=250)]),
        dict(say="Use substitution when a letter is given directly.", do=[T("• Substitution when a letter is given", x=80, y=330)]),
        dict(say="Check in both equations.", do=[T("• Check in both equations", x=80, y=410)]),
    ]),
]

VIDEOS["4.3"] = [
    dict(kind="hook", title="Lift limit", steps=[
        dict(say="A lift can carry at most 630 kilograms. A delivery worker weighs 80 kilograms. She wants to take boxes of 25 kilograms each.",
             do=[E("🛗", 90, 170, 100), T("at most **630 kg** · worker **80 kg** · boxes **25 kg**", x=230, y=200)]),
        PAUSE("4.3-k1", "What is the largest number of boxes she can take? Pause the video and work it out.", "Maximum boxes?"),
    ]),
    dict(kind="hook", title="22 boxes", steps=[
        dict(say="80 plus 25 B must be less than or equal to 630. So 25 B is at most 550, and B is at most 22. She can take up to 22 boxes. Any number up to 22 works, so the answer is a range.",
             do=[MATH("80 + 25b ≤ 630 → 25b ≤ 550", x=80, y=190), B("b ≤ 22", x=80, y=300, color=GREEN, at=7)]),
    ]),
    dict(kind="recall", title="Inequality symbols", steps=[
        dict(say="Remember: less than, less than or equal to, greater than, and greater than or equal to.", do=[B("<   ≤   >   ≥", x=80, y=190, color=BLUE)]),
    ]),
    dict(kind="idea", title="Number lines", steps=[
        dict(say="Solve an inequality just like an equation. The solution set is every value that works. Show it on a number line.", do=[T("solve like an equation; the answer is a **set**", x=80, y=170)]),
        dict(say="Use an open circle for less than, or greater than: that value is not included.", do=[INEQ(80, 250, 700, min=-2, max=6, a=2, dir="right"), T("x > 2: **open** circle", x=820, y=280)]),
        PAUSE("4.3-k2", "Your turn. X is less than or equal to 3. Does the circle at 3 look open, or closed? Pause and choose.", "x ≤ 3 on a number line uses …"),
    ]),
    dict(kind="idea", title="Check: closed circle", steps=[
        dict(say="A closed, filled-in circle. 3 is included, so it is less than or equal to.", do=[INEQ(80, 180, 700, min=-2, max=6, a=3, dir="left", ca=True), B("x ≤ 3: closed", x=820, y=210, color=GREEN)]),
        dict(say="When you multiply or divide both sides by a negative number, reverse the sign.", do=[T("× or ÷ by a **negative** → **reverse** the sign", x=80, y=400, color=RED)]),
    ]),
    dict(kind="method", title="How do I solve an inequality?", steps=[
        dict(say="Here is the method. Step 1: solve it like an equation.", do=[T("1. Solve like an **equation**", x=80, y=170)]),
        dict(say="Step 2: if you multiply or divide by a negative, reverse the sign.", do=[T("2. Negative × or ÷ → **reverse**", x=80, y=260)]),
        dict(say="Step 3: show it with open or closed circles, or list the integers.", do=[T("3. Open < > · closed ≤ ≥", x=80, y=350)]),
        dict(say="Step 4: check with a value.", do=[T("4. **Check** with a value", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Negative coefficient", steps=[
        dict(say="Solve 7 minus 2 X is greater than or equal to 13. Take 7: negative 2 X is at least 6. Divide by negative 2, and reverse: X is less than or equal to negative 3.",
             do=[MATH("7 − 2x ≥ 13 → −2x ≥ 6", x=80, y=180), B("x ≤ −3", x=80, y=290, color=GREEN, at=9)]),
        PAUSE("4.3-k3", "Your turn. Solve negative 3 X less than 12. Pause and work it out.", "−3x < 12 gives …"),
    ]),
    dict(kind="example", title="Check: −3x < 12", steps=[
        dict(say="Divide by negative 3, and reverse the sign. X is greater than negative 4. Check with X equals 0: 0 is less than 12. True.",
             do=[B("x > −4", x=80, y=190, color=GREEN), MATH("x = 0: −3(0) = 0 < 12 ✓", x=80, y=300, at=5)]),
    ]),
    dict(kind="example", title="A double inequality", steps=[
        dict(say="List the integers where negative 5 is less than or equal to 3 N plus 1, which is less than 10. Take 1 from each part, then divide by 3. N is from negative 2, up to but not including 3.",
             do=[MATH("−6 ≤ 3n < 9 → −2 ≤ n < 3", x=80, y=180), B("−2, −1, 0, 1, 2", x=80, y=290, color=GREEN, at=11)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Jo solves 10 minus 3 X is greater than 4. Which line is wrong?", do=LINES("Jo", "10 − 3x > 4", ["−3x > −6", "x > 2"])),
        dict(say="Line 2 is wrong. Dividing by negative 3 reverses the sign.", do=[dict(a="cross", id="l2")]),
        dict(say="X is less than 2. Check with X equals 0: 10 is greater than 4.", do=[B("x < 2", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Limits", steps=[
        dict(say="Weight limits, speed limits and budgets are inequalities, not equations. Anything up to the limit is allowed.", do=[E("🚸", 90, 170, 100), T("limits are **inequalities**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.3-k4", "One last question. What is the largest integer with 2 X less than 9? Pause the video and answer.", "Largest integer with 2x < 9?"),
        dict(say="X is less than 4.5. The largest integer below 4.5 is 4.", do=[B("x < 4.5 → 4", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: solve inequalities like equations.", do=[T("• Solve like equations", x=80, y=170)]),
        dict(say="Multiplying or dividing by a negative reverses the sign.", do=[T("• × ÷ negative → reverse", x=80, y=250)]),
        dict(say="Open circles for less than or greater than. Closed circles when the value is included.", do=[T("• Open < >, closed ≤ ≥", x=80, y=330)]),
        dict(say="Check with a value.", do=[T("• Check with a value", x=80, y=410)]),
    ]),
]
