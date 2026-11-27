# -*- coding: utf-8 -*-
"""Stage 8 · Unit 11 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u11 import MACH2, COORD, LG, XY

TRIP = lambda at=0, **k: LG(dict(min=0, max=6, step=1, label="Time (hours)"), dict(min=0, max=140, step=20, label="Distance from home (km)"), [[0, 0], [1.5, 120], [3.5, 120], [5.5, 0]], at=at, **k)
PLANS = lambda at=0, **k: COORD([-2, 5], [-2, 8], at=at, lines=[dict(m=2, c=1, label="y = 2x + 1"), dict(m=-1, c=6, label="y = 6 − x")], **k)

VIDEOS = {}

VIDEOS["11.1"] = [
    dict(kind="hook", title="Hiring a hall", steps=[
        dict(say="A community hall charges a 15 dollar booking fee, plus 40 dollars per hour.", do=[E("🎉", 90, 170, 100), T("**$15** booking fee + **$40** per hour", x=230, y=200)]),
        PAUSE("11.1-k1", "What does a 3 hour party cost? Pause the video and work it out.", "3-hour hall hire ($)?"),
    ]),
    dict(kind="hook", title="3 hours", steps=[
        dict(say="3 hours at 40 dollars is 120 dollars. Add the 15 dollar fee: 135 dollars.", do=[MACH2("3", "× 40", "+ 15", "135", x=80, y=190)]),
        dict(say="For h hours, the cost C is 40 h plus 15. And if someone paid 255 dollars, how long did they hire the hall? We will find out.", do=[B("C = 40h + 15", x=80, y=330, color=BLUE)]),
    ]),
    dict(kind="recall", title="Substituting", steps=[
        dict(say="Remember: to use a formula, substitute the value. If y equals 4 x minus 1, and x is 3, then y is 12 minus 1, which is 11.", do=[MATH("y = 4x − 1,  x = 3 → y = 11", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Functions", steps=[
        dict(say="A function is a rule where every input gives exactly one output. For the hall, the input is h hours, and the output is C dollars.",
             do=[T("a **function**: every input → **exactly one** output", x=80, y=170), MACH2("h", "× 40", "+ 15", "C", x=80, y=260)]),
        dict(say="The fixed part is 15. The rate is 40 per hour. Output equals rate times input, plus the fixed part.", do=[T("output = **rate** × input + **fixed part**", x=80, y=400)]),
        PAUSE("11.1-k2", "Your turn. Using C equals 40 h plus 15, what is the cost for 5 hours? Pause the video and try it.", "C = 40h + 15. Cost for 5 hours?"),
    ]),
    dict(kind="idea", title="Check: 5 hours", steps=[
        dict(say="40 times 5 is 200. 200 plus 15 is 215 dollars.", do=[MACH2("5", "× 40", "+ 15", "215", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Finding an input", steps=[
        dict(say="To find the input from an output, solve the equation. 40 h plus 15 equals 255. Subtract 15: 40 h equals 240. Divide by 40: h equals 6 hours.",
             do=[MATH("40h + 15 = 255", x=80, y=170), MATH("40h = 240", x=80, y=260, at=5), B("h = 6 hours", x=80, y=360, color=GREEN, at=8)]),
        dict(say="A function can be written in words, as a machine, a table, a graph or an equation. They all describe the same rule.", do=[T("words · machine · table · graph · equation", x=80, y=460)]),
    ]),
    dict(kind="method", title="How do I use a function?", steps=[
        dict(say="Here is the method. Step 1: find the fixed part, and the rate per unit.", do=[T("1. Find the **fixed part** and the **rate**", x=80, y=170)]),
        dict(say="Step 2: write the equation: output equals rate times input, plus the fixed part.", do=[T("2. output = rate × input + fixed part", x=80, y=260)]),
        dict(say="Step 3: substitute to find outputs. Solve to find inputs.", do=[T("3. **Substitute** for outputs; **solve** for inputs", x=80, y=350)]),
        dict(say="Step 4: check your answer in the real situation.", do=[T("4. **Check** in the situation", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A plumber", steps=[
        dict(say="A plumber charges a 30 dollar call-out fee, and 25 dollars per hour. The rate is 25, and the fixed part is 30. So C equals 25 h plus 30.",
             do=[E("🔧", 90, 160, 90), B("C = 25h + 30", x=230, y=180, color=GREEN)]),
        PAUSE("11.1-k3", "Your turn. A taxi charges a 10 dollar fee, plus 3 dollars per kilometre. Write y in terms of x kilometres. Pause and work it out.", "$10 fee plus $3 per km. y = … (x km)"),
    ]),
    dict(kind="example", title="Check: the taxi", steps=[
        dict(say="The rate is 3 per kilometre, and the fixed fee is 10. So y equals 3 x plus 10.", do=[B("y = 3x + 10", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="From a table", steps=[
        dict(say="A table shows x equals 0, 1, 2, 3, and y equals 5, 8, 11, 14. y goes up by 3 each time, so the rate is 3. When x is 0, y is 5. So y equals 3 x plus 5.",
             do=[XY([5, 8, 11, 14], xs=(0, 1, 2, 3), y=170), ROW(0, 0.5), B("y = 3x + 5", x=80, y=340, color=GREEN, at=9)]),
    ]),
    dict(kind="example", title="Is it a function?", steps=[
        dict(say="A rule takes x to a number whose square is x. Is it a function? If x is 9, the output could be 3, or negative 3. That is two outputs, so it is not a function.",
             do=[MATH("9 → 3 or −3", x=80, y=190), B("not a function", x=80, y=300, color=RED, at=8)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="C equals 25 h plus 30, and C is 130. Ali finds h. Which line goes wrong first?", do=LINES("Ali", "25h + 30 = 130", ["130 ÷ 25 = 5.2", "5.2 − 30 = −24.8"])),
        dict(say="Line 1 is wrong. Undo the operations in reverse order. Undo plus 30 first, then divide by 25.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="130 minus 30 is 100. 100 divided by 25 is 4 hours.", do=[B("(130 − 30) ÷ 25 = 4 hours", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Phone plans", steps=[
        dict(say="Phone companies describe plans with functions. A plan might cost 12 dollars a month, plus 5 cents per text: C equals 0.05 t plus 12.",
             do=[E("📱", 90, 170, 100), MATH("C = 0.05t + 12", x=230, y=190)]),
        dict(say="Writing the plans as functions makes it easy to compare them, and find which is cheaper for you.", do=[T("compare plans with their **functions**", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("11.1-k4", "One last question. Is x goes to x squared a function? Pause the video and choose.", "x → x² is a function?"),
        dict(say="Yes. Each input has exactly one square. Two inputs can give the same output, like 3 and negative 3 both giving 9. That is allowed.", do=[B("yes – one output each", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a function gives exactly one output for each input.", do=[T("• Exactly **one output** for each input", x=80, y=170)]),
        dict(say="Output equals rate times input, plus the fixed amount.", do=[T("• output = rate × input + fixed amount", x=80, y=250)]),
        dict(say="Substitute to find outputs. Solve to find inputs.", do=[T("• Substitute for outputs; solve for inputs", x=80, y=330)]),
        dict(say="The same rule can be words, a machine, a table, a graph or an equation.", do=[T("• Words, machine, table, graph, equation", x=80, y=410)]),
    ]),
]

VIDEOS["11.2"] = [
    dict(kind="hook", title="Two plans", steps=[
        dict(say="Two savings plans are described by y equals 2 x plus 1, and y equals 6 minus x. x is in months, and y is in tens of dollars.",
             do=[E("📈", 90, 170, 100), MATH("A: y = 2x + 1 · B: y = 6 − x", x=230, y=190)]),
        dict(say="If we plot both lines, they cross. What does the crossing point mean?", do=[PLANS(x=700, y=230, w=520, at=0.5)]),
        PAUSE("11.2-k1", "What does the crossing point of the two lines mean? Pause the video and choose.", "The crossing point of two cost lines means …"),
    ]),
    dict(kind="hook", title="The same value", steps=[
        dict(say="At the crossing point, both lines have the same x and the same y. So the plans give the same value there.",
             do=[PLANS(x=700, y=130, w=520), B("the same value there", x=80, y=200, color=GREEN)]),
        dict(say="They cross at x equals 5 thirds, which is about 1.7 months.", do=[T("crossing near **x ≈ 1.7**", x=80, y=300)]),
    ]),
    dict(kind="recall", title="Tables of values", steps=[
        dict(say="Remember: to make a table, substitute each x. For y equals 2 x plus 1: x equals 0, 1, 2 gives y equals 1, 3, 5.", do=[XY([1, 3, 5], xs=(0, 1, 2), rule="y = 2x + 1", y=180), ROW(0, 3)]),
    ]),
    dict(kind="idea", title="Plotting a line", steps=[
        dict(say="Make a table, plot the points, then join them with a ruler. Extend the line across the grid, and label it.",
             do=[TBL(["x", "−1", "0", "1", "2", "3"], [["y = 2x + 1", "−1", "1", "3", "5", "7"], ["y = 6 − x", "7", "6", "5", "4", "3"]], x=40, y=160), ROW(0, 1), ROW(1, 3), PLANS(x=700, y=150, w=520, at=4)]),
        PAUSE("11.2-k2", "Your turn. For y equals 2 x plus 1, what is y when x is negative 1? Pause the video and try it.", "y = 2x + 1. y when x = −1?"),
    ]),
    dict(kind="idea", title="Lines parallel to the axes", steps=[
        dict(say="2 times negative 1 is negative 2, plus 1 is negative 1. Now some special lines. x equals a number is a vertical line. y equals a number is a horizontal line.",
             do=[MATH("2 × (−1) + 1 = −1", x=80, y=180, color=GREEN), COORD([-4, 4], [-4, 4], x=700, y=130, w=500, at=4, lines=[dict(x=-2, label="x = −2"), dict(y=3, label="y = 3")])]),
        dict(say="y equals x goes through the origin, at 45 degrees. Every point on it has equal coordinates.", do=[COORD([-4, 4], [-4, 4], x=700, y=130, w=500, lines=[dict(x=-2, label="x = −2"), dict(y=3, label="y = 3"), dict(m=1, c=0, label="y = x")])]),
    ]),
    dict(kind="method", title="How do I plot a straight line?", steps=[
        dict(say="Here is the method. Step 1: choose at least 3 x values. Include negatives if the axes allow.", do=[T("1. At least **3** x-values", x=80, y=170)]),
        dict(say="Step 2: work out y for each one. Check the pattern is steady.", do=[T("2. Work out y; a **steady** pattern?", x=80, y=260)]),
        dict(say="Step 3: plot carefully. Join with a ruler, extend, and label the line.", do=[T("3. Plot, **ruler**, extend, **label**", x=80, y=350)]),
        dict(say="Step 4: if a point is not on the line, check that point's calculation.", do=[T("4. A point off the line? **Recheck** it", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A line sloping down", steps=[
        dict(say="Plot y equals negative 2 x plus 3, for x from negative 1 to 3. The y values are 5, 3, 1, negative 1, negative 3. The line slopes down.",
             do=[XY([5, 3, 1, -1, -3], xs=(-1, 0, 1, 2, 3), y=170), ROW(0, 3), COORD([-2, 4], [-4, 6], x=760, y=150, w=460, at=6, lines=[dict(m=-2, c=3, label="y = −2x + 3")])]),
        PAUSE("11.2-k3", "Your turn. Is the line y equals negative 3 horizontal or vertical? Pause and choose.", "y = −3 is …"),
    ]),
    dict(kind="example", title="Check: y = −3", steps=[
        dict(say="Every point has y equal to negative 3, whatever x is. So it is a horizontal line.", do=[COORD([-4, 4], [-4, 4], x=700, y=130, w=500, lines=[dict(y=-3, label="y = −3")]), B("horizontal", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Rearrange first", steps=[
        dict(say="Plot x plus y equals 5. First make y the subject: y equals 5 minus x. When x is 0, y is 5. When x is 5, y is 0. Join those two points.",
             do=[MATH("x + y = 5 → y = 5 − x", x=80, y=170), COORD([-1, 6], [-1, 6], x=700, y=130, w=500, at=5, lines=[dict(m=-1, c=5, label="x + y = 5")], points=[dict(x=0, y=5, l="(0, 5)"), dict(x=5, y=0, l="(5, 0)")])]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ruby makes a table for y equals 4 minus 2 x, for x equals negative 1, 0, 1, 2. Which line is wrong?", do=LINES("Ruby", "y = 4 − 2x, x = −1, 0, 1, 2", ["y = 2, 4, 2, 0"])),
        dict(say="Line 1 is wrong at x equals negative 1. 4 minus 2 times negative 1 is 4 plus 2, which is 6. Subtracting a negative adds.", do=[dict(a="cross", id="l1")]),
        dict(say="The values are 6, 4, 2, 0.", do=[B("y = 6, 4, 2, 0", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Break-even charts", steps=[
        dict(say="Businesses plot cost and income on the same graph. Where the two lines cross, income equals cost. That is called the break-even point.",
             do=[E("📊", 90, 170, 100), T("lines cross → **break-even point**", x=230, y=200)]),
        dict(say="To the right of it, the business makes a profit. To the left, it makes a loss.", do=[T("right of it: **profit** · left: **loss**", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("11.2-k4", "One last question. Where do y equals x and y equals 4 cross? Pause the video and choose.", "Where do y = x and y = 4 cross?"),
        dict(say="On y equals 4, y is 4. On y equals x, x equals y, so x is 4 too. They cross at 4, 4.", do=[COORD([-1, 6], [-1, 6], x=700, y=130, w=500, lines=[dict(m=1, c=0, label="y = x"), dict(y=4, label="y = 4")], points=[dict(x=4, y=4, l="(4, 4)")]), B("(4, 4)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: make a table, plot, use a ruler, extend and label.", do=[T("• Table → plot → ruler → extend → label", x=80, y=170)]),
        dict(say="Rearrange to y equals something first.", do=[T("• Rearrange to y = … first", x=80, y=250)]),
        dict(say="x equals a number is vertical. y equals a number is horizontal.", do=[T("• x = a vertical · y = b horizontal", x=80, y=330)]),
        dict(say="Where two lines cross, they have the same value.", do=[T("• Crossing point: equal values", x=80, y=410)]),
    ]),
]

VIDEOS["11.3"] = [
    dict(kind="hook", title="Steep roads", steps=[
        dict(say="Some road signs show a gradient. A gradient of 1 in 8 means the road rises 1 metre for every 8 metres across.", do=[E("⛰️", 90, 170, 100), T("road sign: gradient **1 : 8**", x=230, y=200)]),
        dict(say="Lines have gradients too. Which is steeper: y equals 2 x plus 1, or y equals 3 x minus 4?", do=[COORD([-1, 4], [-5, 9], x=700, y=150, w=480, at=2, lines=[dict(m=2, c=1, label="y = 2x + 1"), dict(m=3, c=-4, label="y = 3x − 4")])]),
        PAUSE("11.3-k1", "Which line is steeper? Pause the video and choose.", "Steeper line?"),
    ]),
    dict(kind="hook", title="The steeper line", steps=[
        dict(say="y equals 3 x minus 4 is steeper. It goes up 3 for every 1 across. y equals 2 x plus 1 only goes up 2. The number in front of x tells you the steepness.",
             do=[B("y = 3x − 4 is steeper", x=80, y=200, color=GREEN), T("up **3** for every 1 across", x=80, y=300)]),
    ]),
    dict(kind="recall", title="Plotting", steps=[
        dict(say="Remember: y equals 2 x plus 1 passes through 0, 1 and 1, 3. And y equals 3 x minus 4 crosses the y axis at negative 4.", do=[MATH("y = 2x + 1: (0, 1), (1, 3)", x=80, y=180), MATH("y = 3x − 4: (0, −4)", x=80, y=270, at=5)]),
    ]),
    dict(kind="idea", title="y = mx + c", steps=[
        dict(say="In y equals m x plus c, m is the gradient. It is how much y goes up when x goes up by 1. c is the y intercept, where the line crosses the y axis.",
             do=[B("y = mx + c", x=80, y=160, color=BLUE), TBL(["Equation", "Gradient m", "Intercept c"], [["y = 2x + 1", "2", "1"], ["y = −3x + 4", "−3", "4"], ["y = x − 5", "1", "−5"]], y=260), ROW(0, 6), ROW(1, 7.5), ROW(2, 9)]),
        PAUSE("11.3-k2", "Your turn. What is the intercept of y equals 5 x minus 2? Pause the video and try it.", "Intercept of y = 5x − 2?"),
    ]),
    dict(kind="idea", title="Gradient from a graph", steps=[
        dict(say="The intercept is negative 2. To find a gradient from a graph, choose two points on the line. The gradient is the change in y, divided by the change in x. Rise over run.",
             do=[MATH("c = −2", x=80, y=170, color=GREEN), B("gradient = rise ÷ run", x=80, y=260, color=BLUE, at=4),
                 COORD([-1, 5], [-1, 9], x=700, y=130, w=480, lines=[dict(m=2, c=1)], points=[dict(x=1, y=3, l="A"), dict(x=4, y=9, l="B")], at=4)]),
        dict(say="From A at 1, 3, to B at 4, 9: the rise is 6, and the run is 3. 6 divided by 3 is 2. The line crosses at 1, so it is y equals 2 x plus 1.",
             do=[MATH("rise 6, run 3 → 6 ÷ 3 = 2", x=80, y=360), B("y = 2x + 1", x=80, y=450, color=GREEN, at=7)]),
    ]),
    dict(kind="method", title="How do I find the equation of a line?", steps=[
        dict(say="Here is the method. Step 1: read the y intercept, c, where the line crosses the y axis.", do=[T("1. Read the **y-intercept** c", x=80, y=170)]),
        dict(say="Step 2: choose two clear points. The gradient m is rise over run. It is negative if the line slopes down.", do=[T("2. m = **rise ÷ run** (negative if it slopes down)", x=80, y=260)]),
        dict(say="Step 3: write y equals m x plus c.", do=[T("3. Write **y = mx + c**", x=80, y=350)]),
        dict(say="Step 4: check with another point on the line.", do=[T("4. **Check** with another point", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="From two points", steps=[
        dict(say="A line goes through 0, negative 3, and 2, 5. It crosses the y axis at negative 3, so c is negative 3.", do=[MATH("(0, −3) and (2, 5) → c = −3", x=80, y=170)]),
        dict(say="The rise is 5 minus negative 3, which is 8. The run is 2. 8 divided by 2 is 4. So y equals 4 x minus 3.", do=[MATH("m = 8 ÷ 2 = 4", x=80, y=270), B("y = 4x − 3", x=80, y=370, color=GREEN, at=6)]),
        PAUSE("11.3-k3", "Your turn. What is the gradient of the line through 0, 1, and 2, 7? Pause and work it out.", "Gradient through (0, 1) and (2, 7)?"),
    ]),
    dict(kind="example", title="Check: (0, 1) and (2, 7)", steps=[
        dict(say="The rise is 7 minus 1, which is 6. The run is 2. 6 divided by 2 is 3.", do=[MATH("6 ÷ 2 = 3", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Sloping down", steps=[
        dict(say="A line goes through 0, 6 and 3, 0. c is 6. The line goes down 6 as it goes across 3. Negative 6 divided by 3 is negative 2. So y equals negative 2 x plus 6.",
             do=[COORD([-1, 4], [-1, 7], x=700, y=130, w=480, lines=[dict(m=-2, c=6)], points=[dict(x=0, y=6, l="(0, 6)"), dict(x=3, y=0, l="(3, 0)")]), MATH("m = −6 ÷ 3 = −2", x=80, y=190), B("y = −2x + 6", x=80, y=300, color=GREEN, at=8)]),
    ]),
    dict(kind="example", title="Parallel lines", steps=[
        dict(say="Parallel lines have the same gradient. A line parallel to y equals 5 x minus 1, through 0, 4, has gradient 5 and intercept 4. It is y equals 5 x plus 4.",
             do=[T("parallel → **same gradient**", x=80, y=170), B("y = 5x + 4", x=80, y=270, color=GREEN, at=6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Finn finds the gradient through 2, 1 and 6, 3. Which line goes wrong first?", do=LINES("Finn", "the gradient through (2, 1) and (6, 3)", ["change in x = 4, change in y = 2", "gradient = 4 ÷ 2 = 2"])),
        dict(say="Line 2 is wrong. He divided the run by the rise. The gradient is the change in y divided by the change in x.", do=[dict(a="cross", id="l2")]),
        dict(say="2 divided by 4 is a half.", do=[B("gradient = 2 ÷ 4 = ½", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Wheelchair ramps", steps=[
        dict(say="Building rules limit how steep a wheelchair ramp can be. A common limit is a gradient of 1 in 12. That means 1 unit up for every 12 across.",
             do=[E("♿", 90, 170, 100), T("ramp limit: about **1 : 12**", x=230, y=200)]),
        dict(say="So to rise 60 centimetres, a ramp needs to be about 7.2 metres long across the ground.", do=[MATH("60 cm × 12 = 720 cm = 7.2 m", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("11.3-k4", "One last question. Which line is parallel to y equals negative 2 x plus 1? Pause the video and choose.", "Parallel to y = −2x + 1?"),
        dict(say="Parallel lines have the same gradient, negative 2. So y equals negative 2 x minus 5 is parallel.", do=[B("y = −2x − 5", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: in y equals m x plus c, m is the gradient and c is the y intercept.", do=[T("• y = mx + c: **m** gradient, **c** y-intercept", x=80, y=170)]),
        dict(say="Gradient is rise over run. A negative gradient slopes down.", do=[T("• Gradient = rise ÷ run; negative slopes down", x=80, y=250)]),
        dict(say="Parallel lines have the same gradient.", do=[T("• Parallel lines: same gradient", x=80, y=330)]),
        dict(say="Rearrange to y equals something, to read m and c.", do=[T("• Rearrange to y = … to read m and c", x=80, y=410)]),
    ]),
]

VIDEOS["11.4"] = [
    dict(kind="hook", title="A family trip", steps=[
        dict(say="A family drives 120 kilometres to a beach in 1 and a half hours. They stay 2 hours, then drive home in 2 hours because of traffic.",
             do=[E("🏖️", 90, 170, 100), T("**120 km** in **1.5 h** · stay **2 h** · home in **2 h**", x=230, y=200), TRIP(x=640, y=260, w=560, at=3)]),
        PAUSE("11.4-k1", "On which part of the trip were they fastest? Pause the video and choose.", "Fastest part of the trip?"),
    ]),
    dict(kind="hook", title="Going out", steps=[
        dict(say="Going out, they drove 120 kilometres in 1.5 hours. That is 80 kilometres per hour. Coming home took 2 hours, which is only 60 kilometres per hour. So they were fastest going out.",
             do=[TRIP(x=640, y=150, w=560), MATH("out: 120 ÷ 1.5 = 80 km/h", x=80, y=190), MATH("home: 120 ÷ 2 = 60 km/h", x=80, y=280, at=5), B("fastest: going out", x=80, y=380, color=GREEN, at=10)]),
    ]),
    dict(kind="recall", title="Speed", steps=[
        dict(say="Remember: speed equals distance divided by time.", do=[B("speed = distance ÷ time", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Distance-time graphs", steps=[
        dict(say="On a distance-time graph, the gradient is the speed. A steeper line means faster. A flat line means stopped. A line sloping down means coming back.",
             do=[TRIP(x=640, y=150, w=560), T("steeper → **faster**", x=80, y=180), T("flat → **stopped**", x=80, y=260, at=4), T("down → **coming back**", x=80, y=340, at=6)]),
        PAUSE("11.4-k2", "Your turn. What was their speed on the way home: 120 kilometres in 2 hours? Pause the video and try it.", "Speed home (120 km in 2 h)?"),
    ]),
    dict(kind="idea", title="Curves tell a story", steps=[
        dict(say="120 divided by 2 is 60 kilometres per hour. The shape of any graph tells a story. A straight line means a steady rate. A curve means the rate is changing.",
             do=[MATH("120 ÷ 2 = 60 km/h", x=80, y=180, color=GREEN), T("straight → **steady** rate · curve → **changing** rate", x=80, y=280, at=5)]),
        dict(say="Fill a tall, thin vase with water at a steady rate, and the depth rises quickly. In a wide bowl, it rises slowly.", do=[E("🏺", 80, 360, 80), T("thin vase: depth rises **fast** · wide bowl: **slowly**", x=190, y=385)]),
    ]),
    dict(kind="method", title="How do I read a real-life graph?", steps=[
        dict(say="Here is the method. Step 1: read the title, the axes and the units. Check the scale.", do=[T("1. Title, axes, **units**, scale", x=80, y=170)]),
        dict(say="Step 2: describe each section. Is it going up, flat or going down? Steep or gentle?", do=[T("2. Each section: up, flat, down? steep or gentle?", x=80, y=260)]),
        dict(say="Step 3: work out rates as gradients, like speed equals distance divided by time.", do=[T("3. Rates = **gradients**", x=80, y=350)]),
        dict(say="Step 4: explain what it means in the real situation.", do=[T("4. Explain in **context**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Average speed", steps=[
        dict(say="Find the average speed for the whole trip, including the stop. The total distance is 240 kilometres. The total time is 5 and a half hours.",
             do=[MATH("240 km ÷ 5.5 h", x=80, y=180)]),
        dict(say="240 divided by 5.5 is about 43.6 kilometres per hour. The stop brings the average down.", do=[B("≈ 43.6 km/h", x=80, y=290, color=GREEN)]),
    ]),
    dict(kind="example", title="Filling a funnel", steps=[
        dict(say="Water flows steadily into a cylinder with a narrowing funnel on top. In the cylinder, the depth rises at a steady rate, so the graph is a straight line.",
             do=[T("cylinder → straight line", x=80, y=180)]),
        dict(say="In the funnel, the space gets narrower, so the depth rises faster and faster. The graph curves upwards, getting steeper.", do=[T("narrowing top → a curve getting **steeper**", x=80, y=270)]),
        PAUSE("11.4-k3", "Your turn. A curve getting steeper means the rate is what? Pause and choose.", "A curve getting steeper means the rate is …"),
    ]),
    dict(kind="example", title="Check: getting steeper", steps=[
        dict(say="Getting steeper means the rate is increasing.", do=[B("increasing", x=80, y=200, color=GREEN)]),
        dict(say="And if two people's lines cross on a distance-time graph, they are at the same place at the same time. They meet.", do=[T("lines cross → they **meet**", x=80, y=310)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A distance-time graph reaches 60 kilometres at 2 hours. Zara finds the speed. Which line goes wrong first?", do=LINES("Zara", "60 km at 2 hours: the speed", ["The height is 60", "so the speed is 60 km/h"])),
        dict(say="Line 2 is wrong. The height shows the distance, not the speed. The speed is the gradient.", do=[dict(a="cross", id="l2")]),
        dict(say="60 divided by 2 is 30 kilometres per hour.", do=[B("60 ÷ 2 = 30 km/h", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Fitness trackers", steps=[
        dict(say="A running app draws a distance-time graph of your run. Steep parts show where you ran fast. Flat parts show where you stopped, maybe at a traffic light.",
             do=[E("⌚", 90, 170, 100), T("steep = **fast** · flat = **stopped**", x=230, y=200)]),
        dict(say="The app's pace is just the gradient of the graph, worked out for you.", do=[T("pace = the **gradient**", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("11.4-k4", "One last question. 9 kilometres in 45 minutes is how many kilometres per hour? Pause the video and answer.", "9 km in 45 min = ? km/h"),
        dict(say="45 minutes is three quarters of an hour. 9 divided by 0.75 is 12. Or: 3 kilometres every 15 minutes, which is 12 in an hour.", do=[MATH("9 ÷ 0.75 = 12", x=80, y=190), B("12 km/h", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: on a distance-time graph, the gradient is the speed. Flat means stopped. Down means coming back.", do=[T("• Gradient = speed · flat = stopped · down = returning", x=80, y=170)]),
        dict(say="A straight line means a steady rate. A curve means a changing rate.", do=[T("• Straight = steady rate · curve = changing", x=80, y=250)]),
        dict(say="Average speed is total distance divided by total time.", do=[T("• Average speed = total distance ÷ total time", x=80, y=330)]),
        dict(say="Describe each section in context.", do=[T("• Describe each section in context", x=80, y=410)]),
    ]),
]
