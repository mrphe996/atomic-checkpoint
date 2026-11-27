# -*- coding: utf-8 -*-
"""Stage 7 · Unit 11 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u09 import BOX, ARROW

OP = lambda s: BOX(s, "#8A5A00", "#FFF6D6", 110)
MACH2 = lambda i, a, b, o, x=80, y=200, at=0: T(BOX(i, w=110) + ARROW + OP(a) + ARROW + OP(b) + ARROW + BOX(o, w=110), x=x, y=y, at=at)   # a two-step function machine
COORD = lambda xr, yr, x=640, y=110, w=620, at=0, **k: dict(a="fig", fig=dict(kind="coord", x=xr, y=yr, **k), x=x, y=y, w=w, at=at)
LG = lambda xa, ya, pts, x=600, y=120, w=660, at=0: dict(a="fig", fig=dict(kind="linegraph", x=xa, y=ya, series=[dict(pts=pts)]), x=x, y=y, w=w, at=at)
XY = lambda ys, xs=(0, 1, 2, 3, 4), rule="y", y=250, id="t": TBL(["x"] + [str(v) for v in xs], [[rule] + [str(v).replace("-", "−") for v in ys]], y=y, id=id)
EURO = lambda at=0, **k: LG(dict(min=0, max=100, step=10, label="Dollars ($)"), dict(min=0, max=90, step=10, label="Euros (€)"), [[0, 0], [100, 90]], at=at, **k)
BIKE = lambda at=0, **k: LG(dict(min=0, max=60, step=10, label="Time (minutes)"), dict(min=0, max=6, step=1, label="Distance from home (km)"), [[0, 0], [20, 4], [30, 4], [60, 0]], at=at, **k)

VIDEOS = {}

VIDEOS["11.1"] = [
    dict(kind="hook", title="Taxi fares", steps=[
        dict(say="A taxi company charges 3 dollars for every kilometre, plus a starting fee of 2 dollars.", do=[E("🚕", 90, 160, 110), T("**$3** per km + **$2** to start", x=240, y=200)]),
        PAUSE("11.1-k1", "What does a ride of 5 kilometres cost? Pause the video and work it out.", "A 5 km taxi ride at $3 per km plus $2. What does it cost?"),
    ]),
    dict(kind="hook", title="A rule for any distance", steps=[
        dict(say="5 kilometres at 3 dollars each is 15 dollars. Add the starting fee of 2 dollars. The ride costs 17 dollars.", do=[MATH("5 × 3 = 15", x=80, y=180), MATH("15 + 2 = 17", x=80, y=270, at=3.4), B("$17", x=80, y=370, color=GREEN, at=5.6)]),
        dict(say="The same rule works for any distance: multiply the distance by 3, then add 2.", do=[T("any distance: **× 3**, then **+ 2**", x=80, y=490, color=BLUE)]),
    ]),
    dict(kind="recall", title="Function machines", steps=[
        dict(say="Remember: a function machine takes an input, uses a rule, and gives an output. This machine has 2 steps.", do=[MACH2("input", "× 3", "+ 2", "output", y=180)]),
        dict(say="Put in 4. 4 times 3 is 12, and 12 plus 2 is 14. The output is 14.", do=[MACH2("4", "× 3", "+ 2", "14", y=330)]),
    ]),
    dict(kind="idea", title="A function is a rule", steps=[
        dict(say="A function links each input to exactly 1 output, using a rule. We can write the taxi rule in words: multiply by 3, then add 2.", do=[T("**Function**: each input → exactly **1 output**", x=80, y=150), MACH2("x", "× 3", "+ 2", "y", y=240)]),
        dict(say="We can also write it as an equation. y equals 3 x plus 2. Here x is the input, the distance. And y is the output, the cost.", do=[B("y = 3x + 2", x=80, y=380, color=BLUE), T("x = input (km) · y = output ($)", x=80, y=490, at=5)]),
        PAUSE("11.1-k2", "Your turn. y equals 3 x plus 2. Find y when x is 10. Pause the video and try it.", "y = 3x + 2. Find y when x = 10."),
    ]),
    dict(kind="idea", title="Check: x = 10", steps=[
        dict(say="Replace x with 10. 3 times 10 is 30, and 30 plus 2 is 32. So y is 32.", do=[MATH("y = 3 × 10 + 2", x=80, y=190), MATH("y = 30 + 2 = 32", x=80, y=280, at=2.6, color=GREEN)]),
    ]),
    dict(kind="idea", title="Tables of inputs and outputs", steps=[
        dict(say="A table shows many inputs and outputs together. When x is 0, y is 2. When x is 1, y is 5. Then 8, 11 and 14.", do=[XY([2, 5, 8, 11, 14], rule="y = 3x + 2", y=170), ROW(0, 3)]),
        dict(say="Each time x goes up by 1, y goes up by 3. That 3 is the number that multiplies x.", do=[T("x goes up 1 → y goes up **3**", x=80, y=360, color=BLUE)]),
        dict(say="And when x is 0, y is 2. That is the number added on.", do=[T("x = 0 → y = **2**", x=80, y=450, color=BLUE)]),
    ]),
    dict(kind="idea", title="Finding an input", steps=[
        dict(say="Sometimes you know the output, and you want the input. A taxi ride costs 26 dollars. How far was it?", do=[MACH2("?", "× 3", "+ 2", "26", y=160)]),
        dict(say="Work backwards, with inverse operations, in reverse order. First undo the plus 2: 26 minus 2 is 24.", do=[MATH("26 − 2 = 24", x=80, y=300)]),
        dict(say="Then undo the times 3: 24 divided by 3 is 8. The ride was 8 kilometres.", do=[MATH("24 ÷ 3 = 8", x=80, y=390), B("x = 8", x=80, y=480, color=GREEN, at=4)]),
        PAUSE("11.1-k3", "Your turn. y equals 2 x minus 7. Which value of x gives y equals 9? Pause the video and try it.", "y = 2x − 7. Which x gives y = 9?"),
    ]),
    dict(kind="idea", title="Check: y = 2x − 7", steps=[
        dict(say="First undo the minus 7: 9 plus 7 is 16. Then undo the times 2: 16 divided by 2 is 8. So x is 8.", do=[MATH("9 + 7 = 16", x=80, y=190), MATH("16 ÷ 2 = 8", x=80, y=280, at=3.4), B("x = 8", x=80, y=380, color=GREEN, at=6)]),
    ]),
    dict(kind="method", title="How do I work with a function?", steps=[
        dict(say="Here is the method. Step 1: read the rule, in words or as an equation.", do=[T("1. Read the **rule**: words, or y = …", x=80, y=170)]),
        dict(say="Step 2: to find an output, substitute the input, and follow the order of operations.", do=[T("2. **Output**: substitute the input", x=80, y=260)]),
        dict(say="Step 3: to find an input, use inverse operations, in reverse order.", do=[T("3. **Input**: inverse operations, **reverse order**", x=80, y=350)]),
        dict(say="Step 4: check by putting your answer back into the rule.", do=[T("4. **Check** with the rule", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Write the equation", steps=[
        dict(say="The rule is: divide the input by 4, then subtract 1. Write it as an equation.", do=[T("**divide by 4**, then **subtract 1**", x=80, y=160)]),
        dict(say="Divide x by 4: that is x over 4. Then subtract 1.", do=[MATH("$$x \\rightarrow \\dfrac{x}{4} \\rightarrow \\dfrac{x}{4} - 1$$", x=80, y=260)]),
        dict(say="So the equation is y equals x over 4, minus 1.", do=[MATH("$$y = \\dfrac{x}{4} - 1$$", x=80, y=410, color=GREEN)]),
    ]),
    dict(kind="example", title="A table of values", steps=[
        dict(say="Complete a table for y equals 5 x minus 4, for x from 0 to 3.", do=[B("y = 5x − 4", x=80, y=150, color=BLUE)]),
        dict(say="When x is 0: 0 minus 4 is negative 4. When x is 1: 5 minus 4 is 1.", do=[MATH("x = 0: 0 − 4 = −4", x=80, y=260), MATH("x = 1: 5 − 4 = 1", x=560, y=260, at=3.4)]),
        dict(say="When x is 2, y is 6. When x is 3, y is 11. The outputs go up by 5 each time.", do=[XY([-4, 1, 6, 11], xs=(0, 1, 2, 3), y=380), ROW(0, 0.3), T("+5 each time", x=640, y=440, color=BLUE, at=5)]),
    ]),
    dict(kind="example", title="Finding the rule", steps=[
        dict(say="Here is a table. x is 1, 2, 3, 4. And y is 1, 5, 9, 13. Find the equation.", do=[XY([1, 5, 9, 13], xs=(1, 2, 3, 4), y=160), ROW(0, 0.3)]),
        dict(say="y goes up in fours. So the rule starts with 4 x.", do=[T("y goes up in **4s** → **4x**", x=80, y=330)]),
        dict(say="Test it with x equals 1. 4 times 1 is 4, but y is 1. So we must subtract 3.", do=[MATH("4 × 1 = 4, but y = 1 → subtract 3", x=80, y=420)]),
        dict(say="The equation is y equals 4 x minus 3. Check with x equals 2: 8 minus 3 is 5. Correct.", do=[B("y = 4x − 3", x=80, y=520, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="y equals 4 x plus 6. Find x when y is 30. Here is Maya's working. Which line goes wrong first?",
             do=LINES("Maya", "y = 4x + 6, find x when y = 30", ["30 ÷ 4 = 7.5", "7.5 − 6 = 1.5", "x = 1.5"])),
        dict(say="Line 1 is wrong. You must undo the steps in reverse order. The plus 6 was done last, so undo it first.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6), dict(a="strike", id="l3", at=0.9)]),
        dict(say="30 minus 6 is 24. Then 24 divided by 4 is 6. So x is 6.", do=[B("30 − 6 = 24 → 24 ÷ 4 = 6", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Hot or cold?", steps=[
        dict(say="Here is a function for travellers. To change degrees Celsius into degrees Fahrenheit, a quick rule is: double it, and add 30.", do=[E("🌡️", 90, 160, 100), MACH2("°C", "× 2", "+ 30", "°F", x=230, y=175)]),
        dict(say="So 20 degrees Celsius is about 2 times 20 plus 30, which is 70 degrees Fahrenheit.", do=[MATH("2 × 20 + 30 = 70", x=230, y=320)]),
        dict(say="The exact function is: multiply by 1.8, and add 32. That gives 68. The quick rule is close enough for packing a suitcase.", do=[MATH("1.8 × 20 + 32 = 68", x=230, y=410, color=BLUE), E("🧳", 90, 500, 80, at=5)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("11.1-k4", "One last question. x is 1, 2, 3. And y is 7, 10, 13. What is the equation? Pause the video and work it out.", "x: 1, 2, 3; y: 7, 10, 13. y = ?"),
        dict(say="y goes up in threes, so start with 3 x. When x is 1, 3 x is 3, but y is 7. So add 4. The equation is y equals 3 x plus 4.",
             do=[XY([7, 10, 13], xs=(1, 2, 3), y=170), ROW(0, 0.3), T("up in **3s** → 3x · 3 + **4** = 7", x=80, y=340, at=3), B("y = 3x + 4", x=80, y=440, color=GREEN, at=9)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a function turns each input into exactly 1 output, using a rule.", do=[T("• **Function**: each input → 1 output", x=80, y=170)]),
        dict(say="Write the rule in words, or as an equation, like y equals 3 x plus 2.", do=[T("• Words or an equation: **y = 3x + 2**", x=80, y=250)]),
        dict(say="Find outputs by substituting. Find inputs with inverse operations, in reverse order.", do=[T("• Inputs: **inverse** operations, **reverse** order", x=80, y=330)]),
        dict(say="In a table, the step in y gives the number that multiplies x.", do=[T("• Table: the step in y → the **multiplier** of x", x=80, y=410)]),
    ]),
]

TANK = dict(lines=[dict(m=2, c=4, label="y = 2x + 4")], points=[dict(x=v, y=2 * v + 4) for v in range(5)])

VIDEOS["11.2"] = [
    dict(kind="hook", title="Filling a tank", steps=[
        dict(say="A water tank already holds 4 litres. A tap adds 2 litres every minute.", do=[E("🚰", 90, 160, 110), T("starts with **4 litres** · **+2 litres** every minute", x=240, y=200)]),
        PAUSE("11.2-k1", "How much water is in the tank after 3 minutes? Pause the video and work it out.", "The tank starts at 4 litres and gains 2 per minute. How much after 3 minutes?"),
    ]),
    dict(kind="hook", title="Minute by minute", steps=[
        dict(say="After 1 minute there are 6 litres. After 2 minutes, 8 litres. After 3 minutes, 10 litres.", do=[XY([4, 6, 8, 10], xs=(0, 1, 2, 3), rule="litres", y=170), ROW(0, 0.3), B("10 litres", x=80, y=350, color=GREEN, at=6)]),
        dict(say="As a function: y equals 2 x plus 4. y is the number of litres, after x minutes.", do=[B("y = 2x + 4", x=80, y=460, color=BLUE)]),
    ]),
    dict(kind="recall", title="Plotting coordinates", steps=[
        dict(say="Remember: the point 3, 5 means 3 across, then 5 up. The x coordinate always comes first.", do=[COORD([0, 6], [0, 6], points=[dict(x=3, y=5, l="(3, 5)")]), B("(3, 5)", x=80, y=180), T("**3 across**, then **5 up**", x=80, y=290)]),
    ]),
    dict(kind="idea", title="From a function to a graph", steps=[
        dict(say="Let's draw the tank function. First make a table of values for y equals 2 x plus 4.", do=[XY([4, 6, 8, 10, 12], rule="y", y=150), ROW(0, 2)]),
        dict(say="Each pair is a point. Plot 0, 4. Then 1, 6. Then 2, 8, and so on.", do=[COORD([-1, 5], [-1, 13], y=130, w=600, points=TANK["points"]), T("plot each pair **(x, y)**", x=80, y=330)]),
        dict(say="The points lie on a straight line. Join them with a ruler. A function with a straight line graph is called a linear function.", do=[COORD([-1, 5], [-1, 13], y=130, w=600, **TANK), B("a straight line", x=80, y=420, color=GREEN), T("a **linear** function", x=80, y=520, at=6)]),
        PAUSE("11.2-k2", "Look at the graph. Where does the line cross the y axis? Pause the video and decide.", "y = 2x + 4 crosses the y-axis at y = ?"),
    ]),
    dict(kind="idea", title="Check: crossing the y-axis", steps=[
        dict(say="The line crosses the y axis at 4. That is where x is 0. It is the starting amount: the 4 litres already in the tank.", do=[COORD([-1, 5], [-1, 13], y=130, w=600, **TANK), B("crosses at y = 4", x=80, y=190, color=GREEN), T("x = 0 → the **starting amount**", x=80, y=300, at=3)]),
    ]),
    dict(kind="idea", title="How steep?", steps=[
        dict(say="The number that multiplies x tells you how steep the line is. A bigger multiplier makes a steeper line.", do=[COORD([-1, 5], [-1, 13], y=130, w=600, lines=[dict(m=1, c=4, label="y = x + 4"), dict(m=2, c=4, label="y = 2x + 4")]), T("bigger multiplier → **steeper**", x=80, y=180)]),
        dict(say="y equals 2 x plus 4 goes up 2 for every 1 across. It is steeper than y equals x plus 4.", do=[T("y = 2x + 4: **up 2** for every 1 across", x=80, y=280)]),
        dict(say="A negative multiplier makes the line slope down, from left to right.", do=[T("negative multiplier → slopes **down**", x=80, y=380, color=RED)]),
        PAUSE("11.2-k3", "Your turn. Which line is the steepest: y equals 5 x plus 1, y equals 2 x plus 5, or y equals x plus 9? Pause the video and decide.", "Which line is steepest: y = 5x + 1, y = 2x + 5 or y = x + 9?"),
    ]),
    dict(kind="idea", title="Check: the steepest line", steps=[
        dict(say="Look at the number that multiplies x: 5, 2 and 1. The biggest is 5. So y equals 5 x plus 1 is the steepest.", do=[T("multipliers: **5**, 2, 1", x=80, y=180), B("y = 5x + 1", x=80, y=280, color=GREEN, at=4)]),
    ]),
    dict(kind="method", title="How do I draw the graph of a linear function?", steps=[
        dict(say="Here is the method. Step 1: make a table of values, with at least 3 values of x.", do=[T("1. A **table** with at least 3 values of x", x=80, y=170)]),
        dict(say="Step 2: work out y for each x.", do=[T("2. Work out **y** for each x", x=80, y=260)]),
        dict(say="Step 3: plot the points carefully.", do=[T("3. **Plot** the points (x, y)", x=80, y=350)]),
        dict(say="Step 4: join them with a ruler. If one point is not on the line, check your working.", do=[T("4. Join with a **ruler** · a point off the line? Check it", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Plotting y = x − 3", steps=[
        dict(say="Draw the graph of y equals x minus 3, for x from negative 1 to 4.", do=[B("y = x − 3", x=80, y=150, color=BLUE)]),
        dict(say="Subtract 3 from each value of x. That gives negative 4, negative 3, negative 2, negative 1, 0 and 1.", do=[XY([-4, -3, -2, -1, 0, 1], xs=("−1", 0, 1, 2, 3, 4), y=260), ROW(0, 0.3)]),
        dict(say="Plot the points and join them. The line crosses the y axis at negative 3.", do=[COORD([-2, 5], [-5, 3], x=720, y=330, w=460, lines=[dict(m=1, c=-3, label="y = x − 3")]), T("crosses the y-axis at **−3**", x=80, y=460)]),
    ]),
    dict(kind="example", title="A line that slopes down", steps=[
        dict(say="Make a table for y equals 6 minus 2 x, for x from 0 to 3.", do=[B("y = 6 − 2x", x=80, y=150, color=BLUE)]),
        dict(say="When x is 0, y is 6. When x is 1, y is 4. Then 2, and then 0.", do=[XY([6, 4, 2, 0], xs=(0, 1, 2, 3), y=260), ROW(0, 0.3)]),
        dict(say="y goes down by 2 each time. So the line slopes down.", do=[COORD([-1, 4], [-1, 7], x=720, y=150, w=480, lines=[dict(m=-2, c=6, label="y = 6 − 2x")]), T("down **2** each time → slopes **down**", x=80, y=440, color=RED)]),
    ]),
    dict(kind="example", title="Is the point on the line?", steps=[
        dict(say="Is the point 7, 19 on the line y equals 2 x plus 4?", do=[B("(7, 19)", x=80, y=160), T("on y = 2x + 4?", x=320, y=180)]),
        dict(say="Substitute x equals 7. 2 times 7 plus 4 is 18.", do=[MATH("2 × 7 + 4 = 18", x=80, y=290)]),
        dict(say="18 is not 19. So the point is not on the line.", do=[MATH("18 ≠ 19", x=80, y=380), B("No", x=80, y=470, color=RED, at=2)]),
    ]),
    dict(kind="example", title="Using the graph", steps=[
        dict(say="Use the tank graph to find when the tank holds 12 litres.", do=[COORD([-1, 5], [-1, 13], y=130, w=600, segs=[[0, 12, 4, 12], [4, 12, 4, 0]], **TANK), T("when is y = **12**?", x=80, y=180)]),
        dict(say="Go across from 12 on the y axis to the line. Then go down to the x axis. You reach 4.", do=[T("across to the line, then **down**", x=80, y=280)]),
        dict(say="So the tank holds 12 litres after 4 minutes. Check: 2 times 4 plus 4 is 12.", do=[B("after 4 minutes", x=80, y=380, color=GREEN), MATH("2 × 4 + 4 = 12 ✓", x=80, y=480)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Here is Finn's table for y equals 3 x plus 1, with x from 0 to 3. Which line goes wrong first?",
             do=LINES("Finn", "y = 3x + 1 for x = 0, 1, 2, 3", ["y = 1, 4, 7, 9", "Plot the points and join them with a curve"])),
        dict(say="Line 1 is wrong. When x is 3, y is 3 times 3 plus 1, which is 10, not 9. A linear function goes up by the same amount every time.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="The values are 1, 4, 7, 10. And the points make a straight line, not a curve.", do=[B("1, 4, 7, 10 → a straight line", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Lines that tell a story", steps=[
        dict(say="Straight line graphs describe steady change. If you save the same amount every week, the graph of your savings is a line going up.", do=[E("💰", 90, 160, 100), T("saving every week: a line going **up**", x=230, y=190)]),
        dict(say="A candle burns down steadily, so the graph of its height is a line sloping down.", do=[E("🕯️", 90, 300, 100), T("a burning candle: a line going **down**", x=230, y=330)]),
        dict(say="And the steeper the line, the faster the change.", do=[B("steeper = faster change", x=230, y=460, color=RED)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("11.2-k4", "One last question. Does the line y equals 7 minus x slope up, or slope down? Pause the video and answer.", "y = 7 − x slopes up or down?"),
        dict(say="It slopes down. As x gets bigger, we subtract more, so y gets smaller.", do=[COORD([-1, 8], [-1, 8], lines=[dict(m=-1, c=7, label="y = 7 − x")]), B("down", x=80, y=190, color=GREEN), T("bigger x → smaller y", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: make a table of values, plot the points, and join them with a ruler.", do=[T("• **Table** → **plot** → join with a **ruler**", x=80, y=170)]),
        dict(say="A linear function gives a straight line.", do=[T("• **Linear** function = straight line", x=80, y=250)]),
        dict(say="A bigger multiplier of x is steeper. A negative multiplier slopes down.", do=[T("• Bigger multiplier: **steeper** · negative: **down**", x=80, y=330)]),
        dict(say="A point is on the line if its coordinates fit the equation.", do=[T("• On the line? The coordinates **fit the equation**", x=80, y=410)]),
    ]),
]

VIDEOS["11.3"] = [
    dict(kind="hook", title="Streets on a grid", steps=[
        dict(say="Some cities are built on a grid. Every house on Avenue 3 has an x coordinate of 3, whatever its y coordinate is.", do=[E("🏙️", 90, 160, 110), T("Avenue 3: every house has **x = 3**", x=240, y=200)]),
        dict(say="Here are 3 houses: 3, 1. And 3, 4. And 3, negative 2.", do=[B("(3, 1) (3, 4) (3, −2)", x=80, y=360)]),
        PAUSE("11.3-k1", "What kind of line do these 3 points make: vertical, horizontal, or sloping? Pause the video and decide.", "(3, 1), (3, 4), (3, −2) make a vertical, horizontal or sloping line?"),
    ]),
    dict(kind="hook", title="Straight up and down", steps=[
        dict(say="Plot the points. They are all 3 across, so they sit one above another. They make a vertical line.",
             do=[COORD([-5, 5], [-5, 5], lines=[dict(x=3, label="x = 3")], points=[dict(x=3, y=1), dict(x=3, y=4), dict(x=3, y=-2)]), B("vertical", x=80, y=190, color=GREEN), T("all **3 across**", x=80, y=300)]),
    ]),
    dict(kind="recall", title="Four quadrants", steps=[
        dict(say="Remember: x is across. Negative x is to the left. And y is up. Negative y is down.", do=[COORD([-5, 5], [-5, 5], points=[dict(x=-2, y=3, l="(−2, 3)")]), T("**x**: across (negative = left)", x=80, y=180), T("**y**: up (negative = down)", x=80, y=270, at=3)]),
        dict(say="The point negative 2, 3 is 2 to the left, and 3 up.", do=[B("(−2, 3)", x=80, y=390, color=BLUE)]),
    ]),
    dict(kind="idea", title="Vertical lines: x = a", steps=[
        dict(say="Every point on a vertical line has the same x coordinate. So we name the line by that number. This is the line x equals 3.",
             do=[COORD([-5, 5], [-5, 5], lines=[dict(x=3, label="x = 3")], points=[dict(x=3, y=1), dict(x=3, y=4), dict(x=3, y=-2)]), T("vertical: the **same x** everywhere", x=80, y=180), B("x = 3", x=80, y=290, color=BLUE, at=5)]),
        PAUSE("11.3-k2", "Now think about the y axis. It is a vertical line too. Is the y axis the line x equals 0, or the line y equals 0? Pause the video and decide.", "The y-axis is the line x = 0 or y = 0?"),
    ]),
    dict(kind="idea", title="Check: the y-axis", steps=[
        dict(say="Every point on the y axis is 0 across. So the y axis is the line x equals 0.", do=[COORD([-5, 5], [-5, 5], points=[dict(x=0, y=2), dict(x=0, y=4), dict(x=0, y=-3)]), B("the y-axis is x = 0", x=80, y=190, color=GREEN), T("(0, 2) (0, 4) (0, −3)", x=80, y=300)]),
    ]),
    dict(kind="idea", title="Horizontal lines: y = b", steps=[
        dict(say="Every point on a horizontal line has the same y coordinate. These points all have y equals negative 2.",
             do=[COORD([-5, 5], [-5, 5], lines=[dict(y=-2, label="y = −2")], points=[dict(x=-4, y=-2), dict(x=0, y=-2), dict(x=5, y=-2)]), T("horizontal: the **same y** everywhere", x=80, y=180)]),
        dict(say="So this is the line y equals negative 2. And the x axis is the line y equals 0.", do=[B("y = −2", x=80, y=290, color=BLUE), T("the x-axis is **y = 0**", x=80, y=400, at=3.6)]),
        dict(say="Be careful. The line x equals a number is vertical. It crosses the x axis at that number.", do=[T("x = a is **vertical**", x=80, y=500, color=RED)]),
    ]),
    dict(kind="method", title="How do I name or draw these lines?", steps=[
        dict(say="Here is the method. Step 1: look at the points. Which coordinate stays the same?", do=[T("1. Which coordinate **stays the same**?", x=80, y=170)]),
        dict(say="Step 2: the same x means a vertical line, x equals that value. The same y means a horizontal line, y equals that value.", do=[T("2. Same x → **vertical**, x = … · same y → **horizontal**, y = …", x=80, y=260)]),
        dict(say="Step 3: to draw x equals a, find a on the x axis, and draw straight up and down through it.", do=[T("3. To draw x = a: find a on the **x-axis**", x=80, y=350)]),
        dict(say="Step 4: the lines x equals a and y equals b cross at the point a, b.", do=[T("4. x = a and y = b cross at **(a, b)**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Naming a line", steps=[
        dict(say="A line passes through negative 4, 6, and negative 4, negative 2. What is its equation?", do=[B("(−4, 6) and (−4, −2)", x=80, y=160)]),
        dict(say="The x coordinate is negative 4 both times. So it is a vertical line.", do=[T("x is **−4** both times → vertical", x=80, y=280)]),
        dict(say="Its equation is x equals negative 4.", do=[B("x = −4", x=80, y=380, color=GREEN), COORD([-5, 5], [-3, 7], x=720, y=150, w=480, lines=[dict(x=-4, label="x = −4")], points=[dict(x=-4, y=6), dict(x=-4, y=-2)])]),
    ]),
    dict(kind="example", title="Where lines cross", steps=[
        dict(say="Where do the lines x equals 4 and y equals negative 1 cross?", do=[COORD([-5, 5], [-5, 5], lines=[dict(x=4, label="x = 4"), dict(y=-1, label="y = −1")]), T("x = 4 and y = −1", x=80, y=180)]),
        dict(say="On the first line, every point has x equals 4. On the second, every point has y equals negative 1. The crossing point has both.", do=[T("it needs **x = 4** and **y = −1**", x=80, y=280)]),
        dict(say="So they cross at 4, negative 1.", do=[B("(4, −1)", x=80, y=380, color=GREEN)]),
        PAUSE("11.3-k3", "Your turn. Where do the lines x equals negative 1 and y equals 6 cross? Pause the video and try it.", "Where do x = −1 and y = 6 cross?"),
    ]),
    dict(kind="example", title="Check: x = −1 and y = 6", steps=[
        dict(say="The point must have x equals negative 1, and y equals 6. x comes first. They cross at negative 1, 6.", do=[B("(−1, 6)", x=80, y=190, color=GREEN), T("**x first**, then y", x=80, y=300)]),
    ]),
    dict(kind="example", title="A rectangle from four lines", steps=[
        dict(say="The lines x equals 2, x equals 7, y equals 1 and y equals 4 make a rectangle. Find its area.", do=[COORD([0, 8], [0, 5], lines=[dict(x=2), dict(x=7), dict(y=1), dict(y=4)], polys=[dict(pts=[[2, 1], [7, 1], [7, 4], [2, 4]])]), T("x = 2, x = 7, y = 1, y = 4", x=80, y=170)]),
        dict(say="The width is 7 minus 2, which is 5. The height is 4 minus 1, which is 3.", do=[MATH("width = 7 − 2 = 5", x=80, y=280), MATH("height = 4 − 1 = 3", x=80, y=370, at=3.4)]),
        dict(say="The area is 5 times 3, which is 15 square units.", do=[MATH("5 × 3 = 15", x=80, y=470), B("15 square units", x=80, y=560, color=GREEN, at=2.6)]),
    ]),
    dict(kind="example", title="Which points are on the line?", steps=[
        dict(say="Which of these points are on the line y equals negative 3? Negative 3, 2. Then 5, negative 3. Then 0, negative 3.", do=[B("y = −3", x=80, y=150, color=BLUE), T("(−3, 2) · (5, −3) · (0, −3)", x=80, y=270)]),
        dict(say="The y coordinate must be negative 3. In the first point, y is 2, so it is not on the line. The other 2 points are on the line.", do=[T("(−3, 2) ✗", x=80, y=380, color=RED), T("(5, −3) ✓ · (0, −3) ✓", x=320, y=380, color=GREEN, at=6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Draw the line x equals 2. Here is Ivy's working. Which line goes wrong first?", do=LINES("Ivy", "draw the line x = 2", ["Find 2 on the y-axis", "Draw a horizontal line through it"])),
        dict(say="Line 1 is wrong. x equals 2 means every point is 2 across. So find 2 on the x axis.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="Then draw a vertical line through it. Ivy drew the line y equals 2 by mistake.", do=[B("x = 2 is vertical", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Grids around the world", steps=[
        dict(say="Much of Manhattan, in New York, is a grid. Avenues run one way, and numbered streets cross them. An address is like a pair of coordinates.", do=[E("🗽", 90, 160, 100), T("Manhattan: **avenues** cross **streets**", x=230, y=190)]),
        dict(say="On a globe, the equator is the line of latitude 0 degrees. It is like the line y equals 0.", do=[E("🌍", 90, 300, 100), T("the equator: latitude **0°**, like y = 0", x=230, y=330)]),
        dict(say="And on a chessboard, each column has a letter. All the squares in column e make a vertical line.", do=[E("♟️", 90, 440, 100), T("chess: column **e** is a vertical line", x=230, y=470)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("11.3-k4", "One last question. Is the line y equals 5 horizontal, or vertical? Pause the video and answer.", "y = 5 is horizontal or vertical?"),
        dict(say="It is horizontal. Every point is 5 up, so the line runs straight across.", do=[COORD([-5, 5], [-1, 7], lines=[dict(y=5, label="y = 5")]), B("horizontal", x=80, y=190, color=GREEN), T("every point is **5 up**", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: x equals a is a vertical line. Every point has x coordinate a.", do=[T("• **x = a**: vertical", x=80, y=170)]),
        dict(say="y equals b is a horizontal line. Every point has y coordinate b.", do=[T("• **y = b**: horizontal", x=80, y=250)]),
        dict(say="The y axis is x equals 0, and the x axis is y equals 0.", do=[T("• y-axis: **x = 0** · x-axis: **y = 0**", x=80, y=330)]),
        dict(say="The lines x equals a and y equals b cross at the point a, b.", do=[T("• x = a and y = b cross at **(a, b)**", x=80, y=410)]),
    ]),
]

VIDEOS["11.4"] = [
    dict(kind="hook", title="Changing money", steps=[
        dict(say="Before a holiday, Ravi changes dollars into euros. The bank gives 0.9 euros for every dollar.", do=[E("💶", 90, 160, 110), T("**$1 = €0.90**", x=240, y=200)]),
        PAUSE("11.4-k1", "How many euros does Ravi get for 40 dollars? Pause the video and work it out.", "$40 at €0.9 per $1 = ? euros"),
    ]),
    dict(kind="hook", title="One calculation, or one graph", steps=[
        dict(say="40 times 0.9 is 36. Ravi gets 36 euros.", do=[MATH("40 × 0.9 = 36", x=80, y=180), B("€36", x=80, y=280, color=GREEN, at=2.4)]),
        dict(say="But a graph can change any amount quickly, in either direction, with no calculation at all.", do=[T("a **graph** converts any amount, both ways", x=80, y=420, color=BLUE)]),
    ]),
    dict(kind="recall", title="Reading scales", steps=[
        dict(say="Remember: before you read a graph, work out what 1 small square is worth.", do=[T("what is **1 small square** worth?", x=80, y=180)]),
        dict(say="If 5 squares take you from 0 to 10, each square is worth 2.", do=[MATH("10 ÷ 5 = 2 per square", x=80, y=290)]),
    ]),
    dict(kind="idea", title="Conversion graphs", steps=[
        dict(say="A conversion graph changes one unit into another. It is a straight line through 0, 0, because 0 dollars is 0 euros.", do=[EURO(), T("a straight line through **(0, 0)**", x=80, y=180)]),
        dict(say="To change 40 dollars: find 40 on the dollars axis. Go up to the line. Then go across to the euros axis. You read 36 euros.", do=[T("$40: **up** to the line, then **across**", x=80, y=290), B("€36", x=80, y=380, color=GREEN, at=8)]),
        dict(say="To go the other way, start on the euros axis. Go across to the line, then down. 54 euros is 60 dollars.", do=[T("€54: **across**, then **down** → $60", x=80, y=500, color=BLUE)]),
        PAUSE("11.4-k2", "Your turn. How many dollars is 18 euros? Pause the video and try it.", "Using €0.9 per $1, how many dollars is €18?"),
    ]),
    dict(kind="idea", title="Check: €18 in dollars", steps=[
        dict(say="Find 18 on the euros axis, go across to the line, then down. You reach 20 dollars. Check: 20 times 0.9 is 18.", do=[EURO(), B("$20", x=80, y=190, color=GREEN, at=5), MATH("20 × 0.9 = 18 ✓", x=80, y=310, at=7)]),
    ]),
    dict(kind="idea", title="Graphs that tell a story", steps=[
        dict(say="A distance time graph tells the story of a journey. This one shows a cyclist's distance from home.", do=[BIKE(), T("a **distance–time** graph", x=80, y=170)]),
        dict(say="A line going up means moving away from home. A flat line means stopped. A line going down means coming back.", do=[T("up = moving **away**", x=80, y=260), T("flat = **stopped**", x=80, y=340, at=3), T("down = coming **back**", x=80, y=420, at=5.4)]),
        dict(say="And a steeper line means a faster speed.", do=[T("steeper = **faster**", x=80, y=520, color=RED)]),
        PAUSE("11.4-k3", "Look at the graph. For how many minutes was the cyclist stopped? Pause the video and work it out.", "The cyclist was stopped for how many minutes?"),
    ]),
    dict(kind="idea", title="Check: the flat part", steps=[
        dict(say="The flat part of the line goes from 20 minutes to 30 minutes. So the cyclist was stopped for 10 minutes.", do=[BIKE(), MATH("30 − 20 = 10", x=80, y=190), B("10 minutes", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="method", title="How do I read a real-life graph?", steps=[
        dict(say="Here is the method. Step 1: read the title, the axes and the units.", do=[T("1. Read the **title**, **axes** and **units**", x=80, y=170)]),
        dict(say="Step 2: work out the value of 1 small square on each axis.", do=[T("2. What is **1 square** worth?", x=80, y=260)]),
        dict(say="Step 3: go from the value you know to the line, then across or down to the other axis.", do=[T("3. To the **line**, then to the **other axis**", x=80, y=350)]),
        dict(say="Step 4: describe each section. Is it going up, flat, or going down? Is it steep?", do=[T("4. Describe each section: up, flat, down, steep?", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Beyond the graph", steps=[
        dict(say="Change 300 dollars into euros. The graph only goes up to 100 dollars.", do=[EURO(), T("**$300** → euros?", x=80, y=170)]),
        dict(say="Read 100 dollars from the graph. That is 90 euros.", do=[MATH("$100 → €90", x=80, y=280)]),
        dict(say="300 dollars is 3 lots of 100 dollars. 3 times 90 is 270 euros.", do=[MATH("3 × 90 = 270", x=80, y=370), B("€270", x=80, y=460, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="How fast?", steps=[
        dict(say="How fast did the cyclist ride home, in kilometres per hour?", do=[BIKE(), T("the ride **home**", x=80, y=170)]),
        dict(say="The line goes down from 30 minutes to 60 minutes. That is 4 kilometres in 30 minutes.", do=[T("**4 km** in **30 minutes**", x=80, y=270)]),
        dict(say="30 minutes is half an hour. In a full hour, the cyclist would ride 2 times as far: 8 kilometres. The speed is 8 kilometres per hour.", do=[MATH("4 × 2 = 8", x=80, y=370), B("8 km/h", x=80, y=460, color=GREEN, at=6)]),
    ]),
    dict(kind="example", title="Which part was faster?", steps=[
        dict(say="Compare the ride out with the ride back. Both are 4 kilometres.", do=[BIKE(), T("out: **20 min** · back: **30 min**", x=80, y=170)]),
        dict(say="The ride out took 20 minutes. The ride back took 30 minutes. The ride out took less time, so it was faster.", do=[B("out was faster", x=80, y=300, color=GREEN, at=5)]),
        dict(say="You can see it on the graph too. The first part of the line is steeper.", do=[T("the first part is **steeper**", x=80, y=420)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="On a distance axis, each small square is worth 5 kilometres. A point is 3 squares above 20. Here is Theo's working. Which line goes wrong first?",
             do=LINES("Theo", "3 squares above 20, each square is 5 km", ["3 squares = 3 km", "Value = 20 + 3 = 23 km"])),
        dict(say="Line 1 is wrong. Each square is worth 5 kilometres. So 3 squares are worth 15 kilometres.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="20 plus 15 is 35. The value is 35 kilometres.", do=[B("20 + 15 = 35 km", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Graphs on your wrist", steps=[
        dict(say="A fitness watch draws graphs of your day. On a heart rate graph, a flat low line means you are resting.", do=[E("⌚", 90, 160, 100), T("flat and low: **resting**", x=230, y=190)]),
        dict(say="A steep climb means you have started to run. And a slow slope down shows your heart recovering.", do=[E("🏃", 90, 300, 100), T("steep climb: **running** · slow slope down: **recovering**", x=230, y=330)]),
        dict(say="Weather apps do the same with temperature. One look at the line tells you the story of the whole day.", do=[E("🌤️", 90, 440, 100), T("temperature through the day", x=230, y=470)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("11.4-k4", "One last question. On a distance time graph, does a steeper line mean faster, or slower? Pause the video and answer.", "A steeper line on a distance–time graph means faster or slower?"),
        dict(say="Faster. A steeper line covers more distance in the same time.", do=[BIKE(), B("faster", x=80, y=190, color=GREEN), T("more distance in the same time", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a conversion graph is a straight line through 0, 0.", do=[T("• Conversion graph: a line through **(0, 0)**", x=80, y=170)]),
        dict(say="Read up and across, or across and down, using the scale carefully.", do=[T("• Up and across, or across and down", x=80, y=250)]),
        dict(say="For values beyond the graph, use multiples.", do=[T("• Beyond the graph? Use **multiples**", x=80, y=330)]),
        dict(say="On a distance time graph: up is away, flat is stopped, down is coming back, and steeper is faster.", do=[T("• up = away · flat = stopped · down = back · **steeper = faster**", x=80, y=410)]),
    ]),
]
