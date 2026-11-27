# -*- coding: utf-8 -*-
"""Stage 9 · Unit 10 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u11 import LG

VIDEOS = {}

RIDE = lambda at=0, **k: LG(dict(min=0, max=60, step=10, label="Time (minutes)"), dict(min=0, max=12, step=2, label="Distance from home (km)"), [[0, 0], [20, 10], [30, 10], [60, 0]], at=at, **k)
DROP = lambda at=0, **k: LG(dict(min=0, max=2, step=0.5, label="Time t (s)"), dict(min=0, max=20, step=5, label="Distance fallen (m)"), [[t / 4, 5 * (t / 4) ** 2] for t in range(9)], at=at, **k)

VIDEOS["10.1"] = [
    dict(kind="hook", title="Pencils and pens", steps=[
        dict(say="Pencils cost 2 dollars and pens cost 6 dollars. Kofi spends exactly 30 dollars on pencils and pens.",
             do=[E("✏️", 90, 170, 100), T("pencil **$2** · pen **$6** · total **$30**", x=230, y=200)]),
        PAUSE("10.1-k1", "How many possible answers are there: several, or exactly one? Pause the video and choose.", "How many answers?"),
    ]),
    dict(kind="hook", title="Several answers", steps=[
        dict(say="Several. For example, 15 pencils and no pens, or 12 pencils and 1 pen.", do=[B("several", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Two letters", steps=[
        dict(say="Remember: X plus Y equals 10 has many solutions, like 3 and 7, or 4.5 and 5.5.", do=[MATH("x + y = 10: (3, 7), (4.5, 5.5), …", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Functions of two variables", steps=[
        dict(say="A function can link two quantities. If Kofi buys C pencils and K pens, then 2 C plus 6 K equals 30.", do=[B("2c + 6k = 30", x=80, y=170, color=BLUE)]),
        dict(say="Each pair that works is a solution. Here, C and K must be whole numbers.", do=[TBL(["c (pencils)", "15", "12", "?", "6"], [["k (pens)", "0", "1", "2", "3"]], y=270), ROW(0, 2)]),
        PAUSE("10.1-k2", "Your turn. If K is 2, what is C? Pause the video and try it.", "2c + 6k = 30 with k = 2. c?"),
    ]),
    dict(kind="idea", title="Check: 9", steps=[
        dict(say="2 C plus 12 equals 30. 2 C is 18, so C is 9.", do=[B("2c = 18 → c = 9", x=80, y=190, color=GREEN)]),
        dict(say="This is a linear function. When one quantity goes up by 1, the other changes by a fixed amount.", do=[T("**linear**: a fixed change", x=80, y=300)]),
        dict(say="X times Y equals 24 is an inverse function. As one goes up, the other goes down, but not at a fixed rate: 1 and 24, 2 and 12, 4 and 6.", do=[MATH("xy = 24: (1, 24), (2, 12), (4, 6)", x=80, y=390)]),
    ]),
    dict(kind="method", title="How do I use a two-variable function?", steps=[
        dict(say="Here is the method. Step 1: choose letters, and write the function.", do=[T("1. Letters; **write** the function", x=80, y=170)]),
        dict(say="Step 2: substitute the value you know.", do=[T("2. **Substitute** the known value", x=80, y=260)]),
        dict(say="Step 3: solve for the other one.", do=[T("3. **Solve** for the other", x=80, y=350)]),
        dict(say="Step 4: check the answer makes sense, like a whole number of tickets.", do=[T("4. Makes **sense**?", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Tickets", steps=[
        dict(say="Adult tickets cost 8 dollars, and child tickets 5 dollars. The total is 100 dollars. So 8 A plus 5 C equals 100.", do=[MATH("8a + 5c = 100", x=80, y=180)]),
        dict(say="If A is 5: 40 plus 5 C equals 100. 5 C is 60, so C is 12.", do=[MATH("40 + 5c = 100 → c = 12", x=80, y=280)]),
        dict(say="A 120 kilometre trip: speed times time is 120. At 80 kilometres per hour, the time is 120 divided by 80, which is 1.5 hours.", do=[MATH("st = 120 → t = 120 ÷ 80 = 1.5 h", x=80, y=380)]),
        PAUSE("10.1-k3", "Your turn. X Y equals 24, and X is 3. What is Y? Pause and work it out.", "xy = 24, x = 3. y?"),
    ]),
    dict(kind="example", title="Check: 8", steps=[
        dict(say="3 Y equals 24, so Y is 8.", do=[B("y = 24 ÷ 3 = 8", x=80, y=190, color=GREEN)]),
        dict(say="Words to symbols: Y is 5 less than three times X. Y equals 3 X minus 5.", do=[MATH("y = 3x − 5", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Pia solves 2 C plus 6 K equals 30. Which line is wrong?", do=LINES("Pia", "2c + 6k = 30", ["c = 15, k = 0 is the only answer"])),
        dict(say="Line 1 is wrong. One equation with two unknowns usually has many solutions.", do=[dict(a="cross", id="l1")]),
        dict(say="12 and 1, 9 and 2, 6 and 3, 3 and 4, and 0 and 5 all work too.", do=[B("(12, 1), (9, 2), (6, 3), (3, 4), (0, 5)", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Budgets", steps=[
        dict(say="Any budget is a function of two variables: 30 dollars to spend on two kinds of snack gives many possible mixes.", do=[E("💰", 90, 170, 100), T("a fixed budget → many **mixes**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("10.1-k4", "One last question. X Y equals 24. Is it inverse, or linear? Pause the video and choose.", "xy = 24 is …"),
        dict(say="It is inverse. When X doubles, Y halves.", do=[B("inverse", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a function can link two variables, like 2 C plus 6 K equals 30.", do=[T("• Functions link two variables", x=80, y=170)]),
        dict(say="Many pairs can be solutions.", do=[T("• Many pairs can work", x=80, y=250)]),
        dict(say="Linear: a fixed rate. Inverse: X Y is a constant.", do=[T("• Linear: fixed rate · inverse: xy = constant", x=80, y=330)]),
        dict(say="Check answers make sense.", do=[T("• Check they make sense", x=80, y=410)]),
    ]),
]

VIDEOS["10.2"] = [
    dict(kind="hook", title="A falling ball", steps=[
        dict(say="A ball is dropped. A sensor records how far it falls. After T seconds, it has fallen about 5 T squared metres.",
             do=[E("⚽", 90, 170, 100), MATH("d = 5t²", x=230, y=190)]),
        PAUSE("10.2-k1", "Would the graph of distance against time be a straight line? Pause the video and choose: no, a curve, or yes.", "Straight line?"),
    ]),
    dict(kind="hook", title="A curve", steps=[
        dict(say="No, it is a curve. The ball falls faster and faster, so the distance does not go up by the same amount each second.", do=[B("No – a curve", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Tables of values", steps=[
        dict(say="Remember: for Y equals 2 X plus 3, X equals negative 1 gives 1, 0 gives 3, and 1 gives 5.", do=[MATH("y = 2x + 3: (−1, 1), (0, 3), (1, 5)", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Straight lines", steps=[
        dict(say="Linear functions give straight lines. Choose X values, find Y, plot the points and join them with a ruler.", do=[T("linear → a **straight line**", x=80, y=170)]),
        dict(say="For 2 X plus 3 Y equals 12, the quickest points are where the line crosses the axes. Put X equals 0, then Y equals 0.", do=[MATH("2x + 3y = 12: x = 0 → y = ? · y = 0 → x = ?", x=80, y=270)]),
        PAUSE("10.2-k2", "Your turn. In 2 X plus 3 Y equals 12, what is Y when X is 0? Pause the video and try it.", "2x + 3y = 12: y when x = 0?"),
    ]),
    dict(kind="idea", title="Check: 4", steps=[
        dict(say="3 Y equals 12, so Y is 4. And when Y is 0, X is 6. Plot 0, 4 and 6, 0, and join. A third point checks it: X equals 3 gives Y equals 2.", do=[B("(0, 4) and (6, 0)", x=80, y=190, color=GREEN), MATH("check: (3, 2) ✓", x=80, y=300)]),
    ]),
    dict(kind="idea", title="Curves", steps=[
        dict(say="Functions with X squared give curves. Plot more points, and join them with a smooth curve, not straight lines.",
             do=[DROP(), TBL(["t", "0", "0.5", "1", "1.5", "2"], [["d", "0", "1.25", "5", "?", "20"]], y=200, id="d"), ROW(0, 2, id="d")]),
    ]),
    dict(kind="method", title="How do I plot a graph?", steps=[
        dict(say="Here is the method. Step 1: make a table of values.", do=[T("1. **Table** of values", x=80, y=170)]),
        dict(say="Step 2: choose scales, and plot the points.", do=[T("2. Scales; **plot**", x=80, y=260)]),
        dict(say="Step 3: straight line for linear, smooth curve for X squared.", do=[T("3. Line, or **smooth curve**", x=80, y=350)]),
        dict(say="Step 4: check with an extra point.", do=[T("4. **Check** an extra point", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Tables", steps=[
        dict(say="Where does 5 X plus 2 Y equals 10 cross the axes? X equals 0 gives Y equals 5. Y equals 0 gives X equals 2.", do=[MATH("(0, 5) and (2, 0)", x=80, y=180)]),
        dict(say="Y equals X squared minus 3, for X from negative 2 to 2: 1, negative 2, negative 3, negative 2, 1.", do=[MATH("1, −2, −3, −2, 1", x=80, y=280)]),
        PAUSE("10.2-k3", "Your turn. For the ball, D equals 5 T squared. Find D when T is 1.5. Pause and work it out.", "d = 5t² at t = 1.5?"),
    ]),
    dict(kind="example", title="Check: 11.25", steps=[
        dict(say="1.5 squared is 2.25. 5 times 2.25 is 11.25 metres.", do=[B("5 × 2.25 = 11.25 m", x=80, y=190, color=GREEN)]),
        dict(say="Is 4, 1 on the line 2 X plus 3 Y equals 12? 8 plus 3 is 11, not 12. So no.", do=[MATH("2(4) + 3(1) = 11 ≠ 12 → no", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Tom plots Y equals X squared, for X from negative 2 to 2. Which line is wrong?", do=LINES("Tom", "plot y = x²", ["plot (−2, 4), (−1, 1), (0, 0), (1, 1), (2, 4)", "join them with a ruler"])),
        dict(say="Line 2 is wrong. Y equals X squared is a curve.", do=[dict(a="cross", id="l2")]),
        dict(say="Join the points with a smooth curve.", do=[B("a smooth curve", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Stopping distances", steps=[
        dict(say="Engineers plot stopping distances against speed. It is a curve: double the speed, and the braking distance is about four times as long.", do=[E("🚗", 90, 170, 100), T("2 × speed → about **4 ×** braking distance", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("10.2-k4", "One last question. Is Y equals 3 X minus 1 a straight line, or a curve? Pause the video and choose.", "y = 3x − 1 is …"),
        dict(say="A straight line. It is linear: there is no X squared.", do=[B("a straight line", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: table, plot, join.", do=[T("• Table → plot → join", x=80, y=170)]),
        dict(say="For A X plus B Y equals C, use where it crosses the axes.", do=[T("• ax + by = c: use the intercepts", x=80, y=250)]),
        dict(say="Linear gives a straight line. X squared gives a smooth curve.", do=[T("• Linear: line · x²: smooth curve", x=80, y=330)]),
        dict(say="Check with an extra point.", do=[T("• Check an extra point", x=80, y=410)]),
    ]),
]

VIDEOS["10.3"] = [
    dict(kind="hook", title="Steep roads", steps=[
        dict(say="A road sign shows a gradient of 1 in 10. You rise 1 metre for every 10 metres along. How can you see the steepness of a line like 3 X plus 2 Y equals 8?",
             do=[E("⛰️", 90, 170, 100), T("**1 in 10** · steepness of 3x + 2y = 8?", x=230, y=200)]),
        PAUSE("10.3-k1", "What should you do: rearrange to Y equals, or look at the number in front of X? Pause the video and choose.", "To read the steepness you should …"),
    ]),
    dict(kind="hook", title="Rearrange", steps=[
        dict(say="Rearrange to Y equals. Then the number in front of X is the gradient.", do=[B("rearrange to y = …", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="y = mx + c", steps=[
        dict(say="Remember: in Y equals M X plus C, M is the gradient and C is the Y intercept.", do=[B("y = mx + c", x=80, y=190, color=BLUE), T("m: gradient · c: y-intercept", x=80, y=290)]),
    ]),
    dict(kind="idea", title="Make y the subject", steps=[
        dict(say="Take 3 X plus 2 Y equals 8. Subtract 3 X: 2 Y equals 8 minus 3 X. Then divide by 2.",
             do=[MATH("2y = 8 − 3x", x=80, y=170), MATH("y = 4 − ?x", x=80, y=260, at=6)]),
        PAUSE("10.3-k2", "Your turn. What is the gradient of 3 X plus 2 Y equals 8? Pause the video and try it.", "Gradient of 3x + 2y = 8?"),
    ]),
    dict(kind="idea", title="Check: −1.5", steps=[
        dict(say="Y equals 4 minus 1.5 X. The gradient is negative 1.5, and the Y intercept is 4.", do=[B("y = 4 − 1.5x → m = −1.5", x=80, y=190, color=GREEN)]),
        dict(say="From two points: the gradient is the change in Y divided by the change in X. Through 1, 3 and 5, 11: 8 divided by 4 is 2. So the line is Y equals 2 X plus C. Substitute a point to find C.",
             do=[MATH("(11 − 3) ÷ (5 − 1) = 2 → y = 2x + c", x=80, y=300)]),
        PAUSE("10.3-k3", "Your turn. The line is Y equals 2 X plus 1. What is the Y intercept? Pause and answer.", "Intercept of y = 2x + 1?"),
    ]),
    dict(kind="idea", title="Check: 1", steps=[
        dict(say="The Y intercept is 1. Check with the point 1, 3: 2 plus 1 is 3. The line crosses the Y axis at 0, 1.", do=[B("c = 1", x=80, y=190, color=GREEN)]),
        dict(say="Parallel lines have the same gradient. Y equals 2 X plus 1 and Y equals 2 X minus 7 are parallel.", do=[T("**parallel** ↔ the same gradient", x=80, y=300, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I find m and c?", steps=[
        dict(say="Here is the method. Step 1: rearrange to Y equals.", do=[T("1. Rearrange to **y = …**", x=80, y=170)]),
        dict(say="Step 2: read off the gradient and the intercept.", do=[T("2. Read **m** and **c**", x=80, y=260)]),
        dict(say="Step 3: from two points, change in Y over change in X.", do=[T("3. Two points: **Δy ÷ Δx**", x=80, y=350)]),
        dict(say="Step 4: substitute a point to find C.", do=[T("4. Substitute to find **c**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="X minus 3 Y equals 6. 3 Y equals X minus 6, so Y equals a third X minus 2. The gradient is a third, the intercept negative 2.", do=[MATH("y = ⅓x − 2", x=80, y=180)]),
        dict(say="Through negative 2, 7 and 2, negative 1: the change in Y is negative 8, the change in X is 4. The gradient is negative 2. The line is Y equals negative 2 X plus 3.", do=[MATH("−8 ÷ 4 = −2 → y = −2x + 3", x=80, y=280)]),
        dict(say="A line parallel to Y equals 4 X minus 1, through 0, 6: Y equals 4 X plus 6.", do=[MATH("y = 4x + 6", x=80, y=380)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Sam finds the gradient of 2 X plus 5 Y equals 20. Which line is wrong?", do=LINES("Sam", "gradient of 2x + 5y = 20", ["gradient = 2"])),
        dict(say="Line 1 is wrong. He did not make Y the subject.", do=[dict(a="cross", id="l1")]),
        dict(say="Y equals 4 minus 0.4 X. The gradient is negative 0.4.", do=[B("y = 4 − 0.4x → m = −0.4", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Ramps", steps=[
        dict(say="Wheelchair ramps must not be too steep. Many building rules say a ramp should rise no more than 1 metre for every 12 metres along.", do=[E("♿", 90, 170, 100), T("about **1 in 12** or gentler", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("10.3-k4", "One last question. Which line is parallel to Y equals 5 X: Y equals 5 X minus 3, or Y equals negative 5 X? Pause the video and choose.", "Parallel to y = 5x?"),
        dict(say="Y equals 5 X minus 3. It has the same gradient, 5.", do=[B("y = 5x − 3", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: in Y equals M X plus C, M is the gradient and C the intercept.", do=[T("• y = mx + c", x=80, y=170)]),
        dict(say="Rearrange first.", do=[T("• Rearrange ax + by = c first", x=80, y=250)]),
        dict(say="Gradient is the change in Y over the change in X.", do=[T("• m = change in y ÷ change in x", x=80, y=330)]),
        dict(say="Parallel lines have equal gradients.", do=[T("• Parallel ↔ equal gradients", x=80, y=410)]),
    ]),
]

VIDEOS["10.4"] = [
    dict(kind="hook", title="A bike ride", steps=[
        dict(say="Amara's fitness watch draws a graph of her bike ride. A steep section, then a flat section, then a less steep section back home.",
             do=[E("⌚", 90, 170, 100), RIDE(at=1)]),
        PAUSE("10.4-k1", "What does the flat section mean: she stopped, or she was fastest? Pause the video and choose.", "Flat means …"),
    ]),
    dict(kind="hook", title="Stopped", steps=[
        dict(say="She stopped. Time goes on, but her distance from home does not change.", do=[RIDE(), B("flat = stopped", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Speed", steps=[
        dict(say="Remember: speed equals distance divided by time.", do=[MATH("speed = distance ÷ time", x=80, y=190)]),
    ]),
    dict(kind="idea", title="The gradient is the speed", steps=[
        dict(say="On a distance-time graph, the gradient is the speed. Steeper means faster. Sloping down means coming back.",
             do=[RIDE(), T("**gradient = speed**", x=80, y=170, color=BLUE), T("steeper → faster", x=80, y=240)]),
        dict(say="Out: 10 kilometres in 20 minutes. 20 minutes is a third of an hour, so 10 times 3 is 30 kilometres per hour.", do=[MATH("10 km in ⅓ h = 30 km/h", x=80, y=330)]),
        PAUSE("10.4-k2", "Your turn. Find her speed on the way back, in kilometres per hour. Pause the video and try it.", "Return speed (km/h)?"),
    ]),
    dict(kind="idea", title="Check: 20 km/h", steps=[
        dict(say="Back: 10 kilometres in 30 minutes, which is half an hour. 10 divided by a half is 20 kilometres per hour.", do=[RIDE(), B("10 ÷ ½ = 20 km/h", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Equations and rates", steps=[
        dict(say="A straight line through the origin gives an equation. A runner covers 240 metres in 100 seconds, so D equals 2.4 T.", do=[MATH("d = 2.4t", x=80, y=170)]),
        dict(say="On a cost graph, the gradient is the price for each item. On a tank graph, it is litres per minute.", do=[T("gradient = a **rate**: price per item, litres per minute", x=80, y=270)]),
    ]),
    dict(kind="method", title="How do I read a real-life graph?", steps=[
        dict(say="Here is the method. Step 1: read the axes and the units.", do=[T("1. **Axes** and units", x=80, y=170)]),
        dict(say="Step 2: describe each section: up, flat, or down.", do=[T("2. Each **section**", x=80, y=260)]),
        dict(say="Step 3: gradient equals change up over change across. That is the rate.", do=[T("3. **Gradient** = rate", x=80, y=350)]),
        dict(say="Step 4: check the units, like minutes or hours.", do=[T("4. Check **units**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Fastest", steps=[
        dict(say="Three sections: 4 kilometres in 10 minutes, 6 in 20 minutes, 3 in 5 minutes. Per minute: 0.4, 0.3, 0.6. The third is fastest.", do=[MATH("0.4, 0.3, 0.6 km/min → the third", x=80, y=180)]),
        dict(say="A taxi graph goes through 0, 3 and 10, 23. The gradient is 20 over 10, which is 2. So C equals 2 D plus 3.", do=[MATH("C = 2d + 3", x=80, y=280)]),
        PAUSE("10.4-k3", "Your turn. D equals 2.4 T. Find D when T is 900 seconds. Pause and work it out.", "d = 2.4t; t = 900. d?"),
    ]),
    dict(kind="example", title="Check: 2160 m", steps=[
        dict(say="2.4 times 900 is 2,160 metres, if she keeps the same speed.", do=[B("2.4 × 900 = 2160 m", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="At the flat section, Amara is 10 kilometres from home. Leo reads the graph. Which line is wrong?", do=LINES("Leo", "flat section, 10 km from home", ["so she is going at 10 km/h"])),
        dict(say="Line 1 is wrong. The height is the distance. The speed is the gradient.", do=[dict(a="cross", id="l1")]),
        dict(say="Flat means a speed of 0. She has stopped.", do=[B("speed 0 – stopped", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Delivery tracking", steps=[
        dict(say="Delivery apps and smart energy meters show graphs where the gradient is a rate: kilometres per hour, or kilowatt hours per day.", do=[E("📦", 90, 170, 100), T("gradient = **rate**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("10.4-k4", "One last question. A tank fills from 30 litres to 90 litres in 4 minutes. What is the rate, in litres per minute? Pause the video and answer.", "30 L to 90 L in 4 min. Rate?"),
        dict(say="60 litres in 4 minutes is 15 litres per minute.", do=[B("60 ÷ 4 = 15 L/min", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the gradient is the rate. On a distance-time graph, it is the speed.", do=[T("• Gradient = rate (speed)", x=80, y=170)]),
        dict(say="Flat means no change. Steeper means faster.", do=[T("• Flat = stopped · steeper = faster", x=80, y=250)]),
        dict(say="Check the units.", do=[T("• Check units", x=80, y=330)]),
        dict(say="Straight lines give equations for predictions.", do=[T("• Lines give equations", x=80, y=410)]),
    ]),
]
