# -*- coding: utf-8 -*-
"""Stage 7 · Unit 14 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u11 import COORD

P = lambda x, y, l="": dict(x=x, y=y, l=l)
POLY = lambda pts, l="", c=None: dict(pts=[list(p) for p in pts], l=l, **({"c": c} if c else {}))
TA = [(1, 1), (4, 1), (1, 3)]

VIDEOS = {}

VIDEOS["14.1"] = [
    dict(kind="hook", title="Planning a walk", steps=[
        dict(say="On a hiking map, the scale is 1 to 25,000. The path from the car park to a waterfall measures 12 centimetres on the map.", do=[E("🗺️", 90, 150, 110), T("scale **1 : 25 000** · path on the map: **12 cm**", x=240, y=190)]),
        PAUSE("14.1-k1", "How far is the real walk, in kilometres? Pause the video and work it out.", "12 cm on a 1 : 25 000 map. What is the real distance in km?"),
    ]),
    dict(kind="hook", title="From the map to the ground", steps=[
        dict(say="Every 1 centimetre on the map is 25,000 centimetres on the ground. 12 times 25,000 is 300,000 centimetres.", do=[MATH("12 × 25 000 = 300 000 cm", x=80, y=180)]),
        dict(say="Divide by 100 to get metres: 3,000 metres. Divide by 1,000 to get kilometres: 3 kilometres.", do=[MATH("300 000 cm = 3000 m = 3 km", x=80, y=280), B("3 km", x=80, y=380, color=GREEN, at=6)]),
    ]),
    dict(kind="recall", title="Converting lengths", steps=[
        dict(say="Remember: 100 centimetres make 1 metre, and 1,000 metres make 1 kilometre. So 100,000 centimetres make 1 kilometre.", do=[MATH("100 cm = 1 m", x=80, y=170), MATH("1000 m = 1 km", x=80, y=260, at=2.6), B("100 000 cm = 1 km", x=80, y=370, color=BLUE, at=5.6)]),
    ]),
    dict(kind="idea", title="Scales", steps=[
        dict(say="A scale tells you how distances on a map compare with real distances. You can write a scale in 2 ways.", do=[T("**Scale**: map distance compared with real distance", x=80, y=150)]),
        dict(say="In words: 1 centimetre represents 2 kilometres.",
             do=[TBL(["Type", "Example", "Meaning"], [["in words", "1 cm represents 2 km", "1 cm on the map is 2 km in real life"], ["as a ratio", "1 : 200 000", "1 unit on the map is 200 000 of the same unit"]], y=240), ROW(0, 0.3)]),
        dict(say="Or as a ratio: 1 to 200,000. A ratio has no units. It means 1 of any unit on the map is 200,000 of the same unit in real life.", do=[ROW(1, 0.3)]),
        PAUSE("14.1-k2", "Your turn. 1 centimetre represents 4 kilometres. What does 9 centimetres represent? Pause the video and try it.", "1 cm represents 4 km. 9 cm represents ? km"),
    ]),
    dict(kind="idea", title="Check: 9 cm on the map", steps=[
        dict(say="Each centimetre is 4 kilometres. 9 times 4 is 36 kilometres.", do=[MATH("9 × 4 = 36 km", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Plans", steps=[
        dict(say="Architects draw plans of rooms and buildings to scale. A common scale is 1 to 50. 1 centimetre on the plan is 50 centimetres in real life.", do=[E("📐", 90, 150, 90), T("plan scale **1 : 50** → 1 cm is 50 cm", x=220, y=180)]),
        dict(say="A room is 8 centimetres by 6 centimetres on the plan. Multiply by 50: it is 400 centimetres by 300 centimetres. That is 4 metres by 3 metres.", do=[MATH("8 cm × 50 = 400 cm = 4 m", x=80, y=300), MATH("6 cm × 50 = 300 cm = 3 m", x=80, y=390, at=5), B("4 m by 3 m", x=80, y=490, color=GREEN, at=9)]),
        PAUSE("14.1-k3", "Your turn. A plan has a scale of 1 to 100. A wall is 3.6 centimetres long on the plan. How long is the real wall, in metres? Pause the video and try it.", "1 : 100 plan. A wall is 3.6 cm on the plan. Real length in metres?"),
    ]),
    dict(kind="idea", title="Check: the wall", steps=[
        dict(say="3.6 times 100 is 360 centimetres. That is 3.6 metres.", do=[MATH("3.6 × 100 = 360 cm", x=80, y=190), B("3.6 m", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="method", title="How do I use a scale?", steps=[
        dict(say="Here is the method. Step 1: measure accurately on the map.", do=[T("1. **Measure** on the map", x=80, y=170)]),
        dict(say="Step 2: from the map to real life, multiply by the scale. From real life to the map, divide.", do=[T("2. Map → real: **multiply** · real → map: **divide**", x=80, y=260)]),
        dict(say="Step 3: with a ratio scale, the answer is in the same units as you started with. Then convert it.", do=[T("3. Ratio scale: **same units**, then convert", x=80, y=350)]),
        dict(say="Step 4: check that your answer is sensible.", do=[T("4. Is the answer **sensible**?", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A ratio scale", steps=[
        dict(say="The scale is 1 to 40,000. A road is 9 centimetres long on the map. How long is the real road?", do=[T("scale **1 : 40 000** · road: **9 cm**", x=80, y=160)]),
        dict(say="9 times 40,000 is 360,000 centimetres.", do=[MATH("9 × 40 000 = 360 000 cm", x=80, y=270)]),
        dict(say="Divide by 100,000 to change centimetres to kilometres. The road is 3.6 kilometres long.", do=[MATH("360 000 ÷ 100 000 = 3.6", x=80, y=360), B("3.6 km", x=80, y=450, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="From real life to the map", steps=[
        dict(say="A lake is 800 metres long. How long is it on a map with a scale of 1 to 20,000?", do=[T("lake: **800 m** · scale **1 : 20 000**", x=80, y=160)]),
        dict(say="First change to centimetres. 800 metres is 80,000 centimetres.", do=[MATH("800 m = 80 000 cm", x=80, y=270)]),
        dict(say="From real life to the map, divide. 80,000 divided by 20,000 is 4. The lake is 4 centimetres long on the map.", do=[MATH("80 000 ÷ 20 000 = 4", x=80, y=360), B("4 cm", x=80, y=450, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Finding the scale", steps=[
        dict(say="A road is 3 kilometres long. It measures 6 centimetres on a map. Write the scale as a ratio.", do=[T("**6 cm** on the map · **3 km** in real life", x=80, y=160)]),
        dict(say="Use the same units. 3 kilometres is 300,000 centimetres. So the ratio is 6 to 300,000.", do=[MATH("6 : 300 000", x=80, y=270)]),
        dict(say="Divide both parts by 6. The scale is 1 to 50,000.", do=[T("÷ 6", x=420, y=286, color=GREY), B("1 : 50 000", x=80, y=380, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="The scale is 1 to 30,000. A path is 4 centimetres on the map. Find the real distance. Here is Bea's working. Which line goes wrong first?",
             do=LINES("Bea", "scale 1 : 30 000, 4 cm on the map", ["4 × 30 000 = 120 000", "So the distance is 120 000 km"])),
        dict(say="Line 2 is wrong. With a ratio scale, the answer is in the units you started with: centimetres, not kilometres.", do=[dict(a="cross", id="l2")]),
        dict(say="120,000 centimetres is 1.2 kilometres. That is a sensible length for a path.", do=[B("120 000 cm = 1.2 km", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Scales all around", steps=[
        dict(say="Many model railways use a scale of 1 to 87. A real locomotive, 20 metres long, becomes a model about 23 centimetres long.", do=[E("🚂", 90, 160, 100), MATH("2000 cm ÷ 87 ≈ 23 cm", x=230, y=180)]),
        dict(say="When you zoom in on a map on your phone, the scale changes. 1 centimetre on the screen might be 5 kilometres, or only 50 metres.", do=[E("📱", 90, 320, 100), T("zooming changes the **scale**", x=230, y=350)]),
        dict(say="That is why digital maps show a small scale bar, which changes as you zoom.", do=[T("look for the **scale bar**", x=230, y=470, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.1-k4", "One last question. The scale is 1 to 50,000. A real distance is 2.5 kilometres. How many centimetres is that on the map? Pause the video and work it out.", "1 : 50 000. 2.5 km is ? cm on the map"),
        dict(say="2.5 kilometres is 250,000 centimetres. Divide by 50,000. It is 5 centimetres on the map.", do=[MATH("2.5 km = 250 000 cm", x=80, y=190), MATH("250 000 ÷ 50 000 = 5", x=80, y=280, at=3.6), B("5 cm", x=80, y=380, color=GREEN, at=6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: from the map to real life, multiply by the scale. From real life to the map, divide.", do=[T("• Map → real: **multiply** · real → map: **divide**", x=80, y=170)]),
        dict(say="A ratio scale, like 1 to 50,000, uses the same unit on both sides.", do=[T("• 1 : n uses the **same unit** on both sides", x=80, y=250)]),
        dict(say="100 centimetres is 1 metre, and 100,000 centimetres is 1 kilometre.", do=[T("• 100 cm = 1 m · **100 000 cm = 1 km**", x=80, y=330)]),
        dict(say="Always check that your answer is sensible.", do=[T("• Check that the answer is **sensible**", x=80, y=410)]),
    ]),
]

ROBOT = dict(points=[P(-3, 2, "A"), P(5, 2, "B"), P(5, -4, "C")], segs=[[-3, 2, 5, 2], [5, 2, 5, -4]])

VIDEOS["14.2"] = [
    dict(kind="hook", title="A delivery robot", steps=[
        dict(say="A delivery robot in a warehouse can only move along the grid lines. It starts at negative 3, 2. It must reach 5, 2.", do=[E("🤖", 90, 150, 100), T("from **(−3, 2)** to **(5, 2)**", x=80, y=300), COORD([-5, 6], [-5, 4], points=[P(-3, 2, "A"), P(5, 2, "B")])]),
        PAUSE("14.2-k1", "How far does the robot travel? Pause the video and work it out.", "What is the distance from (−3, 2) to (5, 2)?"),
    ]),
    dict(kind="hook", title="Count the squares", steps=[
        dict(say="Count along the grid. From negative 3 to 0 is 3 squares. From 0 to 5 is 5 more. That makes 8 units.", do=[COORD([-5, 6], [-5, 4], points=[P(-3, 2, "A"), P(5, 2, "B")], segs=[[-3, 2, 5, 2]]), MATH("3 + 5 = 8", x=80, y=190), B("8 units", x=80, y=290, color=GREEN, at=5)]),
    ]),
    dict(kind="recall", title="Four quadrants", steps=[
        dict(say="Remember: in a coordinate pair, x comes first. x is across, and left is negative. y is up, and down is negative.", do=[COORD([-5, 5], [-5, 5], points=[P(-4, -1, "(−4, −1)")]), T("**(x, y)**: across, then up", x=80, y=180), T("left and down are **negative**", x=80, y=270, at=4)]),
    ]),
    dict(kind="idea", title="Points on a horizontal line", steps=[
        dict(say="A and B have the same y coordinate. So they lie on a horizontal line.", do=[COORD([-5, 6], [-5, 4], **ROBOT), T("same **y** → a horizontal line", x=80, y=170)]),
        dict(say="The distance between them is the difference of the x coordinates. 5 minus negative 3 is 8.", do=[MATH("5 − (−3) = 8", x=80, y=270, color=BLUE)]),
        dict(say="Subtracting a negative is the same as adding. 5 plus 3 is 8.", do=[T("subtract a negative = **add**", x=80, y=370)]),
    ]),
    dict(kind="idea", title="Points on a vertical line", steps=[
        dict(say="Next, the robot goes from B to C: from 5, 2 down to 5, negative 4. These points have the same x coordinate, so the line is vertical.", do=[COORD([-5, 6], [-5, 4], **ROBOT), T("same **x** → a vertical line", x=80, y=170)]),
        dict(say="The distance is the difference of the y coordinates. 2 minus negative 4 is 6.", do=[MATH("2 − (−4) = 6", x=80, y=270, color=BLUE)]),
        dict(say="So the whole journey is 8 plus 6, which is 14 units.", do=[MATH("8 + 6 = 14 units", x=80, y=370, color=GREEN)]),
        PAUSE("14.2-k2", "Your turn. What is the distance from 1, 4 to 1, negative 5? Pause the video and try it.", "What is the distance from (1, 4) to (1, −5)?"),
    ]),
    dict(kind="idea", title="Check: (1, 4) to (1, −5)", steps=[
        dict(say="The x coordinates are the same, so subtract the y coordinates. 4 minus negative 5 is 9. The distance is 9 units.", do=[MATH("4 − (−5) = 9", x=80, y=190), B("9 units", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="method", title="How do I find the distance?", steps=[
        dict(say="Here is the method. Step 1: check which coordinate is the same. The same y means horizontal. The same x means vertical.", do=[T("1. Same y → **horizontal** · same x → **vertical**", x=80, y=170)]),
        dict(say="Step 2: subtract the other coordinates: the larger minus the smaller.", do=[T("2. **Larger − smaller**", x=80, y=260)]),
        dict(say="Step 3: remember that subtracting a negative is adding.", do=[T("3. Subtract a negative = **add**", x=80, y=350)]),
        dict(say="Step 4: check. A distance is never negative.", do=[T("4. A distance is **never negative**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A vertical distance", steps=[
        dict(say="Find the distance from P, at negative 2, negative 6, to Q, at negative 2, 5.", do=[COORD([-5, 5], [-7, 6], points=[P(-2, -6, "P"), P(-2, 5, "Q")], segs=[[-2, -6, -2, 5]]), T("P(−2, −6) and Q(−2, 5)", x=80, y=170)]),
        dict(say="The x coordinate is negative 2 both times, so the line is vertical.", do=[T("same x → **vertical**", x=80, y=270)]),
        dict(say="5 minus negative 6 is 11. The distance is 11 units.", do=[MATH("5 − (−6) = 11", x=80, y=370), B("11 units", x=80, y=460, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="A missing coordinate", steps=[
        dict(say="R is at negative 4, 3. S is 10 units to the right of R. Find S.", do=[T("R(−4, 3) · S is **10 right**", x=80, y=160)]),
        dict(say="Moving right adds to the x coordinate. Negative 4 plus 10 is 6. The y coordinate stays the same.", do=[MATH("−4 + 10 = 6", x=80, y=270)]),
        dict(say="So S is at 6, 3.", do=[B("S = (6, 3)", x=80, y=370, color=GREEN)]),
        PAUSE("14.2-k3", "Your turn. T is 6 units below the point 3, 2. What is the y coordinate of T? Pause the video and try it.", "T is 6 units below (3, 2). What is T's y-coordinate?"),
    ]),
    dict(kind="example", title="Check: 6 units below", steps=[
        dict(say="Moving down subtracts from the y coordinate. 2 minus 6 is negative 4. T is at 3, negative 4.", do=[MATH("2 − 6 = −4", x=80, y=190), B("y = −4", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="A rectangle", steps=[
        dict(say="A rectangle has corners at negative 2, negative 3. Then 4, negative 3. Then 4, 1. And negative 2, 1. Find its perimeter and its area.", do=[COORD([-4, 6], [-5, 3], polys=[POLY([(-2, -3), (4, -3), (4, 1), (-2, 1)])])]),
        dict(say="The width is 4 minus negative 2, which is 6. The height is 1 minus negative 3, which is 4.", do=[MATH("width: 4 − (−2) = 6", x=80, y=180), MATH("height: 1 − (−3) = 4", x=80, y=270, at=4)]),
        dict(say="For the perimeter, add the width and the height, then double: 2 times 10 is 20 units. The area is 6 times 4, which is 24 square units.", do=[MATH("perimeter: 2 × (6 + 4) = 20", x=80, y=390, color=GREEN), MATH("area: 6 × 4 = 24", x=80, y=480, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Halfway between", steps=[
        dict(say="Find the point halfway between negative 6, 2 and 4, 2.", do=[T("halfway between **(−6, 2)** and **(4, 2)**", x=80, y=160)]),
        dict(say="The distance is 4 minus negative 6, which is 10. Half of 10 is 5.", do=[MATH("4 − (−6) = 10", x=80, y=270), MATH("10 ÷ 2 = 5", x=520, y=270, at=3.4)]),
        dict(say="Move 5 right from negative 6. Negative 6 plus 5 is negative 1. The halfway point is negative 1, 2.", do=[MATH("−6 + 5 = −1", x=80, y=370), B("(−1, 2)", x=80, y=460, color=GREEN, at=4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Find the distance from negative 5, 1 to 3, 1. Here is Otto's working. Which line goes wrong first?", do=LINES("Otto", "the distance from (−5, 1) to (3, 1)", ["5 − 3 = 2", "Distance = 2"])),
        dict(say="Line 1 is wrong. The first x coordinate is negative 5, not 5.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="3 minus negative 5 is 8. The distance is 8 units. You can check by counting on the grid.", do=[B("3 − (−5) = 8", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Up and down, left and right", steps=[
        dict(say="A lift works like a vertical number line. From floor negative 2, in the car park, up to floor 9, is 9 minus negative 2: 11 floors.", do=[E("🛗", 90, 160, 100), MATH("9 − (−2) = 11 floors", x=230, y=180)]),
        dict(say="In chess, a rook moves only along rows and columns. Its moves are exactly the distances in this lesson.", do=[E("♜", 90, 320, 100), T("a rook moves along **rows** and **columns**", x=230, y=350)]),
        dict(say="And in a city built on a grid, you count blocks across, and blocks up, in just the same way.", do=[E("🏙️", 90, 460, 100), T("city blocks: across, then up", x=230, y=490)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.2-k4", "One last question. What is the distance from negative 7, 0 to negative 2, 0? Pause the video and answer.", "What is the distance from (−7, 0) to (−2, 0)?"),
        dict(say="Larger minus smaller: negative 2 minus negative 7. That is negative 2 plus 7, which is 5 units.", do=[MATH("−2 − (−7) = 5", x=80, y=190), B("5 units", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the same y means a horizontal line. The distance is the difference in x.", do=[T("• Same y → horizontal: difference in **x**", x=80, y=170)]),
        dict(say="The same x means a vertical line. The distance is the difference in y.", do=[T("• Same x → vertical: difference in **y**", x=80, y=250)]),
        dict(say="Take the larger minus the smaller. Subtracting a negative is adding.", do=[T("• Larger − smaller · subtract a negative = **add**", x=80, y=330)]),
        dict(say="Distances are never negative.", do=[T("• Distances are **never negative**", x=80, y=410)]),
    ]),
]

TRI_A, TRI_B = [(1, 1), (3, 1), (1, 4)], [(5, -2), (7, -2), (5, 1)]

VIDEOS["14.3"] = [
    dict(kind="hook", title="Sliding furniture", steps=[
        dict(say="In a room planning app, you drag a sofa 4 squares right, and 2 squares down. It does not turn, and it does not change size. It just slides.", do=[E("🛋️", 90, 150, 110), T("**4 right** and **2 down**", x=240, y=190)]),
        dict(say="One corner of the sofa starts at 1, 3.", do=[B("corner at (1, 3)", x=240, y=300, color=BLUE)]),
        PAUSE("14.3-k1", "Where is that corner now? Pause the video and work it out.", "(1, 3) moved 4 right and 2 down is …"),
    ]),
    dict(kind="hook", title="Change x, then y", steps=[
        dict(say="Moving 4 right adds 4 to the x coordinate: 1 plus 4 is 5. Moving 2 down subtracts 2 from the y coordinate: 3 minus 2 is 1.", do=[MATH("x: 1 + 4 = 5", x=80, y=180), MATH("y: 3 − 2 = 1", x=80, y=270, at=5)]),
        dict(say="The corner is now at 5, 1.", do=[B("(5, 1)", x=80, y=380, color=GREEN)]),
    ]),
    dict(kind="recall", title="Moving on a grid", steps=[
        dict(say="Remember: moving right or left changes x. Moving up or down changes y.", do=[T("right / left → changes **x**", x=80, y=180), T("up / down → changes **y**", x=80, y=270, at=2.6)]),
    ]),
    dict(kind="idea", title="Translation", steps=[
        dict(say="A translation slides a shape, without turning it or flipping it. Every point moves the same distance, in the same direction.", do=[COORD([-1, 8], [-3, 5], polys=[POLY(TRI_A, "A"), POLY(TRI_B, "B")]), T("**Translation**: a slide", x=80, y=170), T("every point moves the **same way**", x=80, y=260, at=4)]),
        dict(say="The starting shape is called the object. The new shape is called the image. Here, triangle A is the object, and triangle B is its image.", do=[T("A: the **object** · B: the **image**", x=80, y=360)]),
        dict(say="A translation does not change the lengths or the angles.", do=[T("lengths and angles **stay the same**", x=80, y=460)]),
        PAUSE("14.3-k2", "So, is the image of a translation congruent to the object, or bigger than the object? Pause the video and decide.", "The image of a translation is congruent to or bigger than the object?"),
    ]),
    dict(kind="idea", title="Check: congruent", steps=[
        dict(say="It is congruent to the object. It has exactly the same shape and the same size.", do=[B("congruent", x=80, y=190, color=GREEN), T("same shape, same size", x=80, y=300)]),
    ]),
    dict(kind="idea", title="Describing a translation", steps=[
        dict(say="To describe a translation, say how far left or right, then how far up or down. Pick 1 corner of the object, and the matching corner of the image.", do=[COORD([-1, 8], [-3, 5], polys=[POLY(TRI_A, "A"), POLY(TRI_B, "B")], segs=[[1, 1, 5, 1], [5, 1, 5, -2]]), T("left / right, then up / down", x=80, y=170)]),
        dict(say="The corner at 1, 1 moves to 5, negative 2. That is 4 squares right, and 3 squares down.", do=[MATH("(1, 1) → (5, −2)", x=80, y=270), B("4 right, 3 down", x=80, y=360, color=GREEN, at=4)]),
        dict(say="With coordinates: right adds to x, and left subtracts. Up adds to y, and down subtracts.", do=[T("right **+x** · left **−x** · up **+y** · down **−y**", x=80, y=480)]),
        PAUSE("14.3-k3", "Your turn. A point moves from 0, 0 to negative 3, 4. Is that 3 left and 4 up, or 3 right and 4 down? Pause the video and decide.", "(0, 0) → (−3, 4) is 3 left, 4 up or 3 right, 4 down?"),
    ]),
    dict(kind="idea", title="Check: (0, 0) to (−3, 4)", steps=[
        dict(say="x goes from 0 to negative 3: that is 3 left. y goes from 0 to 4: that is 4 up.", do=[MATH("x: 0 → −3", x=80, y=180), MATH("y: 0 → 4", x=80, y=270, at=3), B("3 left, 4 up", x=80, y=370, color=GREEN, at=5)]),
    ]),
    dict(kind="method", title="How do I translate a shape?", steps=[
        dict(say="Here is the method. Step 1: read the translation. How far left or right? How far up or down?", do=[T("1. **Read** the translation", x=80, y=170)]),
        dict(say="Step 2: move each corner of the shape that many squares.", do=[T("2. Move **each corner**", x=80, y=260)]),
        dict(say="Step 3: join the new corners in the same order.", do=[T("3. **Join** the corners in the same order", x=80, y=350)]),
        dict(say="Step 4: check that the image is the same shape and size, and the same way up.", do=[T("4. Check: same shape, size and **way up**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Translating a triangle", steps=[
        dict(say="Translate the triangle with corners 2, 1. Then 5, 1. And 2, 3. Move it 3 left and 2 up.", do=[COORD([-2, 6], [0, 6], polys=[POLY([(2, 1), (5, 1), (2, 3)], "A")]), T("**3 left** and **2 up**", x=80, y=170)]),
        dict(say="Subtract 3 from every x coordinate, and add 2 to every y coordinate. 2, 1 goes to negative 1, 3.", do=[MATH("(2, 1) → (−1, 3)", x=80, y=270)]),
        dict(say="5, 1 goes to 2, 3. And 2, 3 goes to negative 1, 5.", do=[MATH("(5, 1) → (2, 3)", x=80, y=360), MATH("(2, 3) → (−1, 5)", x=80, y=450, at=3), COORD([-2, 6], [0, 6], at=5, polys=[POLY([(2, 1), (5, 1), (2, 3)], "A"), POLY([(-1, 3), (2, 3), (-1, 5)], "B")])]),
    ]),
    dict(kind="example", title="Describe it", steps=[
        dict(say="A corner of a square moves from negative 2, 4 to 3, 1. Describe the translation.", do=[MATH("(−2, 4) → (3, 1)", x=80, y=160)]),
        dict(say="x goes from negative 2 to 3. That is a change of plus 5: 5 right.", do=[MATH("x: −2 → 3 is +5", x=80, y=280), T("**5 right**", x=520, y=296, color=BLUE)]),
        dict(say="y goes from 4 to 1. That is a change of negative 3: 3 down. The translation is 5 right and 3 down.", do=[MATH("y: 4 → 1 is −3", x=80, y=370), T("**3 down**", x=520, y=386, color=BLUE), B("5 right, 3 down", x=80, y=480, color=GREEN, at=6)]),
    ]),
    dict(kind="example", title="Going back", steps=[
        dict(say="Shape B is shape A, translated 5 right and 3 down. Describe the translation from B back to A.", do=[T("A → B: **5 right, 3 down**", x=80, y=170)]),
        dict(say="To go back, reverse each direction. Right becomes left, and down becomes up.", do=[T("reverse each direction", x=80, y=280)]),
        dict(say="So the translation from B to A is 5 left and 3 up.", do=[B("B → A: 5 left, 3 up", x=80, y=380, color=GREEN)]),
    ]),
    dict(kind="example", title="Two translations", steps=[
        dict(say="A point is translated 2 right and 6 up. Then it is translated 5 left and 2 down. Describe the single translation that does the same job.", do=[T("**2 right, 6 up**, then **5 left, 2 down**", x=80, y=160)]),
        dict(say="For x: plus 2, then minus 5, makes negative 3. That is 3 left.", do=[MATH("x: +2 − 5 = −3", x=80, y=280), T("**3 left**", x=520, y=296, color=BLUE)]),
        dict(say="For y: plus 6, then minus 2, makes plus 4. That is 4 up. The single translation is 3 left and 4 up.", do=[MATH("y: +6 − 2 = +4", x=80, y=370), T("**4 up**", x=520, y=386, color=BLUE), B("3 left, 4 up", x=80, y=480, color=GREEN, at=6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Triangle A has a corner at 2, 1. Triangle B has the matching corner at 8, 1. Describe the translation. Here is Suki's working. Which line goes wrong first?",
             do=LINES("Suki", "corner (2, 1) → matching corner (8, 1)", ["The gap between the triangles is 4 squares", "So the translation is 4 right"])),
        dict(say="Line 1 is wrong. Do not measure the gap between the shapes. Count from a corner to the matching corner.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="From 2 to 8 is 6. The translation is 6 right.", do=[B("8 − 2 = 6 → 6 right", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Slides everywhere", steps=[
        dict(say="In a video game, when a character runs across the screen, its picture is translated: a few pixels right, in every frame.", do=[E("🎮", 90, 160, 100), T("a game character: a few pixels **right** each frame", x=230, y=190)]),
        dict(say="Wallpaper and floor tiles repeat a pattern by translation. The same shape slides across, again and again.", do=[E("🧱", 90, 300, 100), T("tiles and wallpaper: the pattern **slides**", x=230, y=330)]),
        dict(say="And a lift is a translation too: straight up, or straight down, with no turning.", do=[E("🛗", 90, 440, 100), T("a lift: straight **up** or **down**", x=230, y=470)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.3-k4", "One last question. A shape moves 2 right, then 2 left. Does that give no movement, or 4 right? Pause the video and answer.", "2 right then 2 left gives no movement or 4 right?"),
        dict(say="No movement. Plus 2, then minus 2, is 0. The shape is back where it started.", do=[MATH("+2 − 2 = 0", x=80, y=190), B("no movement", x=80, y=290, color=GREEN, at=2.6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a translation slides a shape. No turning, no flipping, and the same size.", do=[T("• **Translation**: a slide – no turn, no flip", x=80, y=170)]),
        dict(say="Describe it as left or right, then up or down.", do=[T("• Describe: **left / right**, then **up / down**", x=80, y=250)]),
        dict(say="Right and left change x. Up and down change y.", do=[T("• Right / left change **x** · up / down change **y**", x=80, y=330)]),
        dict(say="Always count between matching corners.", do=[T("• Count between **matching corners**", x=80, y=410)]),
    ]),
]

MIR = dict(lines=[dict(x=0, label="mirror")], polys=[POLY(TA, "A"), POLY([(-1, 1), (-4, 1), (-1, 3)], "B")])

VIDEOS["14.4"] = [
    dict(kind="hook", title="Reflections in a lake", steps=[
        dict(say="On a still day, a tree on the bank of a lake appears upside down in the water. The top of the tree is 8 metres above the water line.", do=[E("🌳", 90, 150, 110), T("tree top: **8 m above** the water line", x=240, y=190)]),
        PAUSE("14.4-k1", "Where does the top of the tree appear in the reflection? Pause the video and decide.", "The tree top is 8 m above the water. Where does it appear in the reflection?"),
    ]),
    dict(kind="hook", title="The same distance below", steps=[
        dict(say="It appears 8 metres below the water line. The water acts as a mirror line. The reflection is the same distance from the line, on the other side.", do=[B("8 m below", x=80, y=180, color=GREEN), T("the water is the **mirror line**", x=80, y=290), T("same distance, **other side**", x=80, y=380, at=5)]),
    ]),
    dict(kind="recall", title="Lines on a grid", steps=[
        dict(say="Remember: a line such as x equals 2 is vertical. A line such as y equals 1 is horizontal.", do=[COORD([-5, 5], [-5, 5], lines=[dict(x=2, label="x = 2"), dict(y=1, label="y = 1")]), T("x = 2: **vertical**", x=80, y=180), T("y = 1: **horizontal**", x=80, y=270, at=3)]),
    ]),
    dict(kind="idea", title="Reflection", steps=[
        dict(say="A reflection flips a shape over a mirror line. Here, triangle A is reflected in the y axis, to give triangle B.", do=[COORD([-5, 5], [-1, 5], **MIR), T("**Reflection**: a flip over a **mirror line**", x=80, y=170)]),
        dict(say="Each point of the image is the same distance from the mirror line as the object point, but on the opposite side.", do=[T("same distance · **opposite side**", x=80, y=270)]),
        dict(say="We measure that distance at right angles to the mirror line. The image is congruent to the object, but it is flipped.", do=[T("measure at **right angles** to the line", x=80, y=370), T("congruent, but **flipped**", x=80, y=460, at=5)]),
    ]),
    dict(kind="idea", title="Reflecting with coordinates", steps=[
        dict(say="Reflections in the axes follow a simple rule. Reflect the point 3, 2 in the y axis. The x coordinate changes sign: negative 3, 2.",
             do=[TBL(["Mirror line", "What happens", "(3, 2) goes to"], [["the y-axis", "x changes sign", "(−3, 2)"], ["the x-axis", "y changes sign", "(3, −2)"]], y=170), ROW(0, 3)]),
        dict(say="Reflect 3, 2 in the x axis. This time the y coordinate changes sign: 3, negative 2.", do=[ROW(1, 0.3)]),
        PAUSE("14.4-k2", "Your turn. Reflect the point negative 5, 1 in the y axis. Pause the video and try it.", "Reflect (−5, 1) in the y-axis."),
    ]),
    dict(kind="idea", title="Check: (−5, 1) in the y-axis", steps=[
        dict(say="In the y axis, the x coordinate changes sign. Negative 5 becomes 5. The image is 5, 1.", do=[MATH("(−5, 1) → (5, 1)", x=80, y=190, color=GREEN), COORD([-6, 6], [-2, 4], points=[P(-5, 1, "(−5, 1)"), P(5, 1, "(5, 1)")])]),
    ]),
    dict(kind="idea", title="Other mirror lines", steps=[
        dict(say="For any other mirror line, count squares. Reflect the point 3, 2 in the line x equals 1.", do=[COORD([-3, 5], [-1, 5], lines=[dict(x=1, label="x = 1")], points=[P(3, 2, "(3, 2)")]), T("reflect (3, 2) in **x = 1**", x=80, y=170)]),
        dict(say="The point is 2 squares to the right of the line. So the image is 2 squares to the left of the line. 1 minus 2 is negative 1.", do=[T("2 right of the line → **2 left**", x=80, y=270), MATH("1 − 2 = −1", x=80, y=360, at=6)]),
        dict(say="The image is negative 1, 2. The y coordinate does not change.", do=[B("(−1, 2)", x=80, y=460, color=GREEN), COORD([-3, 5], [-1, 5], lines=[dict(x=1, label="x = 1")], points=[P(3, 2, "(3, 2)"), P(-1, 2, "(−1, 2)")])]),
    ]),
    dict(kind="method", title="How do I reflect a shape?", steps=[
        dict(say="Here is the method. Step 1: find the mirror line.", do=[T("1. Find the **mirror line**", x=80, y=170)]),
        dict(say="Step 2: for each corner, count the squares to the line, at right angles.", do=[T("2. **Count** squares to the line (at right angles)", x=80, y=260)]),
        dict(say="Step 3: count the same number on the other side, and mark the image corner.", do=[T("3. The **same number** on the other side", x=80, y=350)]),
        dict(say="Step 4: join the image corners, and check that the shape is flipped.", do=[T("4. **Join** the corners · it should be flipped", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="In the y-axis", steps=[
        dict(say="Reflect the triangle with corners 2, 1. Then 5, 1. And 2, 4. Use the y axis as the mirror line.", do=[COORD([-6, 6], [-1, 5], polys=[POLY([(2, 1), (5, 1), (2, 4)], "A")]), T("mirror line: the **y-axis**", x=80, y=170)]),
        dict(say="Change the sign of each x coordinate. The corners become negative 2, 1. Then negative 5, 1. And negative 2, 4.", do=[MATH("(−2, 1), (−5, 1), (−2, 4)", x=80, y=280, color=GREEN), COORD([-6, 6], [-1, 5], at=3, polys=[POLY([(2, 1), (5, 1), (2, 4)], "A"), POLY([(-2, 1), (-5, 1), (-2, 4)], "B")])]),
    ]),
    dict(kind="example", title="In the line x = 2", steps=[
        dict(say="Reflect the point 6, 3 in the line x equals 2.", do=[COORD([-3, 7], [-1, 5], lines=[dict(x=2, label="x = 2")], points=[P(6, 3, "(6, 3)")]), T("reflect (6, 3) in **x = 2**", x=80, y=170)]),
        dict(say="6 is 4 squares to the right of the line. So go 4 squares to the left of the line: 2 minus 4 is negative 2.", do=[MATH("6 − 2 = 4", x=80, y=270), MATH("2 − 4 = −2", x=80, y=360, at=5)]),
        dict(say="The image is negative 2, 3.", do=[B("(−2, 3)", x=80, y=460, color=GREEN)]),
    ]),
    dict(kind="example", title="In the line y = 1", steps=[
        dict(say="Reflect the point 4, negative 2 in the line y equals 1.", do=[COORD([-1, 6], [-3, 5], lines=[dict(y=1, label="y = 1")], points=[P(4, -2, "(4, −2)")]), T("reflect (4, −2) in **y = 1**", x=80, y=170)]),
        dict(say="This mirror line is horizontal, so measure up and down. The point is 3 squares below the line. The image is 3 squares above: 1 plus 3 is 4.", do=[T("3 below the line → **3 above**", x=80, y=270), MATH("1 + 3 = 4", x=80, y=360, at=7)]),
        dict(say="The image is 4, 4.", do=[B("(4, 4)", x=80, y=460, color=GREEN)]),
        PAUSE("14.4-k3", "Your turn. Reflect the point 0, 3 in the line y equals 1. Pause the video and try it.", "Reflect (0, 3) in y = 1."),
    ]),
    dict(kind="example", title="Check: (0, 3) in y = 1", steps=[
        dict(say="The point is 2 squares above the line. So the image is 2 squares below it: 1 minus 2 is negative 1. The image is 0, negative 1.", do=[COORD([-3, 3], [-2, 4], lines=[dict(y=1, label="y = 1")], points=[P(0, 3, "(0, 3)"), P(0, -1, "(0, −1)")]), MATH("1 − 2 = −1", x=80, y=190), B("(0, −1)", x=80, y=290, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Finding the mirror line", steps=[
        dict(say="A point at negative 2, 4 has its image at 6, 4. Find the mirror line.", do=[COORD([-3, 7], [-1, 6], points=[P(-2, 4, "A"), P(6, 4, "A′")]), T("(−2, 4) → (6, 4)", x=80, y=170)]),
        dict(say="The mirror line is halfway between the point and its image. Halfway between negative 2 and 6 is 2.", do=[MATH("(−2 + 6) ÷ 2 = 2", x=80, y=280)]),
        dict(say="So the mirror line is the vertical line x equals 2.", do=[B("x = 2", x=80, y=380, color=GREEN), COORD([-3, 7], [-1, 6], lines=[dict(x=2, label="x = 2")], points=[P(-2, 4, "A"), P(6, 4, "A′")])]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Reflect the point 5, 6 in the line y equals 3. Here is Kofi's working. Which line goes wrong first?", do=LINES("Kofi", "reflect (5, 6) in y = 3", ["The point is 2 squares right of the line x = 3", "Image: (1, 6)"])),
        dict(say="Line 1 is wrong. The line y equals 3 is horizontal. So measure up and down, not left and right.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="The point is 3 squares above the line. The image is 3 squares below it, at 5, 0.", do=[B("3 above → 3 below: (5, 0)", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Mirror images", steps=[
        dict(say="On the front of many ambulances, the word AMBULANCE is written back to front. A driver ahead reads it the right way round in the mirror.", do=[E("🚑", 90, 160, 100), T("written **back to front** – correct in a mirror", x=230, y=190)]),
        dict(say="The Taj Mahal, in India, was built beside a long pool. The pool reflects the whole building, upside down, like a mirror line.", do=[E("🕌", 90, 310, 100), T("the Taj Mahal and its **reflection**", x=230, y=340)]),
        dict(say="And your face in a mirror is a reflection too. Raise your right hand, and the image raises its left.", do=[E("🪞", 90, 460, 100), T("right hand → the image's **left** hand", x=230, y=490)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.4-k4", "One last question. A point lies on the mirror line. When it is reflected, does it stay where it is, or move twice as far? Pause the video and answer.", "A point on the mirror line stays where it is or moves twice as far?"),
        dict(say="It stays where it is. Its distance from the mirror line is 0, so its image is in the same place.", do=[B("it stays where it is", x=80, y=190, color=GREEN), T("distance from the line = **0**", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a reflection flips a shape over a mirror line.", do=[T("• **Reflection**: a flip over a mirror line", x=80, y=170)]),
        dict(say="Image points are the same distance from the line, on the other side, at right angles.", do=[T("• Same distance · other side · at **right angles**", x=80, y=250)]),
        dict(say="In the x axis, y changes sign. In the y axis, x changes sign.", do=[T("• x-axis: **y** changes sign · y-axis: **x** changes sign", x=80, y=330)]),
        dict(say="Points on the mirror line do not move.", do=[T("• Points on the mirror line **do not move**", x=80, y=410)]),
    ]),
]

ROT = dict(polys=[POLY([(0, 0), (3, 0), (0, 2)], "A"), POLY([(0, 0), (0, -3), (2, 0)], "B")])

VIDEOS["14.5"] = [
    dict(kind="hook", title="Turning a key", steps=[
        dict(say="You turn a key a quarter turn clockwise, to unlock a door. Before you turn it, the key points straight up.", do=[E("🔑", 90, 150, 110), T("a **quarter turn clockwise**", x=240, y=190)]),
        PAUSE("14.5-k1", "Which way does the key point after the quarter turn: right, left, or down? Pause the video and decide.", "Up, then a quarter turn clockwise, points right, left or down?"),
    ]),
    dict(kind="hook", title="A quarter turn", steps=[
        dict(say="Clockwise is the way the hands of a clock move. From pointing up, a quarter turn clockwise points to the right.", do=[E("⬆️", 120, 170, 90), E("➡️", 360, 170, 90, at=3), T("→", x=250, y=190), B("right", x=80, y=330, color=GREEN, at=3.4)]),
        dict(say="After a half turn, the key would point straight down.", do=[E("⬇️", 600, 170, 90), T("half turn: **down**", x=560, y=330)]),
    ]),
    dict(kind="recall", title="Turns and degrees", steps=[
        dict(say="Remember: a quarter turn is 90 degrees. A half turn is 180 degrees. A full turn is 360 degrees.", do=[MATH("quarter turn = 90°", x=80, y=170), MATH("half turn = 180°", x=80, y=260, at=2.6), MATH("full turn = 360°", x=80, y=350, at=5.2)]),
    ]),
    dict(kind="idea", title="Rotation", steps=[
        dict(say="A rotation turns a shape about a fixed point. That point is called the centre of rotation.", do=[COORD([-4, 4], [-4, 4], **ROT), T("**Rotation**: a turn about a **centre**", x=80, y=170)]),
        dict(say="To describe a rotation, you need 3 things: the angle, the direction, and the centre.", do=[T("**angle** · **direction** · **centre**", x=80, y=270)]),
        dict(say="Here, triangle A is rotated 90 degrees clockwise about the point 0, 0, to give triangle B.", do=[B("90° clockwise about (0, 0)", x=80, y=370, color=BLUE)]),
        PAUSE("14.5-k2", "Think about the centre of rotation. Does it not move at all, or does it move the furthest? Pause the video and decide.", "The centre of rotation does not move or moves the furthest?"),
    ]),
    dict(kind="idea", title="Check: the centre", steps=[
        dict(say="The centre does not move. Everything else turns around it, like a wheel turning around its axle.", do=[B("the centre does not move", x=80, y=190, color=GREEN), E("🎡", 90, 320, 110, at=2)]),
    ]),
    dict(kind="idea", title="A half turn", steps=[
        dict(say="In a rotation, every point stays the same distance from the centre. So the image is congruent to the object.", do=[T("every point stays the **same distance** from the centre", x=80, y=160)]),
        dict(say="A half turn about 0, 0 has a simple rule. Both coordinates change sign. The point 2, 5 goes to negative 2, negative 5.", do=[COORD([-6, 6], [-6, 6], x=700, y=230, w=480, points=[P(2, 5, "(2, 5)"), P(-2, -5, "(−2, −5)")], segs=[[2, 5, -2, -5]]), MATH("(2, 5) → (−2, −5)", x=80, y=290, color=BLUE)]),
        dict(say="For a half turn, the direction does not matter. Clockwise and anticlockwise give the same image.", do=[T("180°: clockwise or anticlockwise – **the same**", x=80, y=400)]),
        PAUSE("14.5-k3", "Your turn. Rotate the point 0, 3 through 180 degrees about 0, 0. Pause the video and try it.", "Rotate (0, 3) through 180° about (0, 0)."),
    ]),
    dict(kind="idea", title="Check: (0, 3) half turn", steps=[
        dict(say="Both coordinates change sign. 0 stays 0, and 3 becomes negative 3. The image is 0, negative 3.", do=[MATH("(0, 3) → (0, −3)", x=80, y=190, color=GREEN), COORD([-4, 4], [-4, 4], points=[P(0, 3, "(0, 3)"), P(0, -3, "(0, −3)")])]),
    ]),
    dict(kind="method", title="How do I rotate a shape?", steps=[
        dict(say="Here is the method. Step 1: find the centre, the angle, and the direction.", do=[T("1. Find the **centre**, **angle** and **direction**", x=80, y=170)]),
        dict(say="Step 2: trace the shape, and mark the centre on your tracing paper.", do=[T("2. **Trace** the shape and the centre", x=80, y=260)]),
        dict(say="Step 3: hold the centre still with your pencil point, and turn the tracing paper through the angle.", do=[T("3. Hold the centre · **turn** the paper", x=80, y=350)]),
        dict(say="Step 4: mark the image, and check that it is the same shape and size.", do=[T("4. Mark the **image** · same shape and size", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A quarter turn about a corner", steps=[
        dict(say="A rectangle has corners 0, 0. Then 3, 0. Then 3, 1. And 0, 1. Rotate it 90 degrees anticlockwise about 0, 0.", do=[COORD([-3, 4], [-1, 4], polys=[POLY([(0, 0), (3, 0), (3, 1), (0, 1)], "A")]), T("**90° anticlockwise** about (0, 0)", x=80, y=170)]),
        dict(say="The long side lies along the x axis. After a quarter turn anticlockwise, it stands up along the y axis. So 3, 0 goes to 0, 3.", do=[MATH("(3, 0) → (0, 3)", x=80, y=280)]),
        dict(say="The corner 3, 1 goes to negative 1, 3. And 0, 1 goes to negative 1, 0. The centre, 0, 0, stays where it is.", do=[MATH("(3, 1) → (−1, 3)", x=80, y=370), MATH("(0, 1) → (−1, 0)", x=80, y=460, at=4), COORD([-3, 4], [-1, 4], at=6, polys=[POLY([(0, 0), (3, 0), (3, 1), (0, 1)], "A"), POLY([(0, 0), (0, 3), (-1, 3), (-1, 0)], "B")])]),
    ]),
    dict(kind="example", title="A half turn about a corner", steps=[
        dict(say="A triangle has corners 2, 1. Then 5, 1. And 2, 3. Rotate it 180 degrees about the corner 2, 1.", do=[COORD([-2, 6], [-2, 4], polys=[POLY([(2, 1), (5, 1), (2, 3)], "A")]), T("**180°** about (2, 1)", x=80, y=170)]),
        dict(say="The corner 5, 1 is 3 squares right of the centre. After a half turn, it is 3 squares left: negative 1, 1.", do=[MATH("(5, 1) → (−1, 1)", x=80, y=280)]),
        dict(say="The corner 2, 3 is 2 squares above the centre. After a half turn, it is 2 squares below: 2, negative 1.", do=[MATH("(2, 3) → (2, −1)", x=80, y=370), COORD([-2, 6], [-2, 4], at=5, polys=[POLY([(2, 1), (5, 1), (2, 3)], "A"), POLY([(2, 1), (-1, 1), (2, -1)], "B")])]),
    ]),
    dict(kind="example", title="Describe the rotation", steps=[
        dict(say="An arrow points to the right. It is turned so that it points up. Describe the rotation.", do=[E("➡️", 120, 160, 90), T("→", x=250, y=180), E("⬆️", 360, 160, 90, at=2)]),
        dict(say="From right to up is a quarter turn. It goes the opposite way to the hands of a clock.", do=[T("a **quarter turn**, against the clock", x=80, y=320)]),
        dict(say="So it is a rotation of 90 degrees anticlockwise.", do=[B("90° anticlockwise", x=80, y=420, color=GREEN)]),
    ]),
    dict(kind="example", title="Two ways to say it", steps=[
        dict(say="Is a turn of 90 degrees clockwise the same as a turn of 270 degrees anticlockwise?", do=[T("90° clockwise = 270° anticlockwise?", x=80, y=170)]),
        dict(say="90 plus 270 is 360, a full turn. So going 90 degrees one way ends in the same place as going 270 degrees the other way. Yes, they are the same.", do=[MATH("90 + 270 = 360", x=80, y=280), B("Yes", x=80, y=380, color=GREEN, at=6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A shape points up. It is turned to point left. Describe the rotation. Here is Jade's working. Which line goes wrong first?", do=LINES("Jade", "up → left: describe the rotation", ["It is a quarter turn", "Answer: a rotation of 90°"])),
        dict(say="Line 2 is wrong. The answer is not complete. A rotation needs a direction, and a centre as well.", do=[dict(a="cross", id="l2")]),
        dict(say="From up to left is against the clock. It is a rotation of 90 degrees anticlockwise.", do=[B("90° anticlockwise", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Things that turn", steps=[
        dict(say="The minute hand of a clock makes a full turn every hour. That is 360 degrees in 60 minutes: 6 degrees every minute.", do=[E("🕐", 90, 160, 100), MATH("360° ÷ 60 = 6° per minute", x=230, y=180)]),
        dict(say="The Earth rotates too. It makes 1 full turn in 24 hours. That is 15 degrees every hour.", do=[E("🌍", 90, 320, 100), MATH("360° ÷ 24 = 15° per hour", x=230, y=340)]),
        dict(say="That is why the time changes by 1 hour for about every 15 degrees you travel east or west.", do=[T("15° east or west → about **1 hour** of time", x=230, y=470, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.5-k4", "One last question. A turn of 90 degrees anticlockwise is the same as which clockwise turn: 270 degrees, or 90 degrees? Pause the video and answer.", "90° anticlockwise is the same as 270° clockwise or 90° clockwise?"),
        dict(say="270 degrees clockwise. 90 plus 270 makes a full turn of 360.", do=[B("270° clockwise", x=80, y=190, color=GREEN), MATH("90 + 270 = 360", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a rotation turns a shape about a centre. Give the angle, the direction and the centre.", do=[T("• **Rotation**: angle, direction, centre", x=80, y=170)]),
        dict(say="Every point stays the same distance from the centre.", do=[T("• Every point stays the **same distance** from the centre", x=80, y=250)]),
        dict(say="Use tracing paper. A half turn is the same in both directions.", do=[T("• Use **tracing paper** · 180° is the same both ways", x=80, y=330)]),
        dict(say="A half turn about 0, 0 changes the sign of both coordinates.", do=[T("• 180° about (0, 0): **both signs change**", x=80, y=410)]),
    ]),
]

ENL = dict(polys=[POLY([(1, 1), (3, 1), (3, 2), (1, 2)], "A"), POLY([(4, 2), (10, 2), (10, 5), (4, 5)], "B")])

VIDEOS["14.6"] = [
    dict(kind="hook", title="Printing a photo", steps=[
        dict(say="A photo on a phone is 4 centimetres wide and 3 centimetres tall. You print it 3 times as big, for a frame.", do=[E("🖼️", 90, 150, 110), T("**4 cm** wide, **3 cm** tall · print **3 times** as big", x=240, y=190)]),
        PAUSE("14.6-k1", "How wide is the print? Pause the video and work it out.", "A 4 cm wide photo is printed 3 times as big. What is its width in cm?"),
    ]),
    dict(kind="hook", title="Three times as big", steps=[
        dict(say="Multiply the width by 3. 4 times 3 is 12 centimetres.", do=[MATH("4 × 3 = 12 cm", x=80, y=180, color=GREEN)]),
        dict(say="The height is multiplied by 3 as well: 3 times 3 is 9 centimetres. The print is bigger, but it is the same shape.", do=[MATH("3 × 3 = 9 cm", x=80, y=280), T("bigger, but the **same shape**", x=80, y=400, at=4)]),
    ]),
    dict(kind="recall", title="Times as long", steps=[
        dict(say="Remember: 4 times as long means multiply by 4. A line of 2.5 centimetres becomes 10 centimetres.", do=[MATH("2.5 × 4 = 10 cm", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Enlargement and scale factor", steps=[
        dict(say="An enlargement changes the size of a shape, but not its shape. Every length is multiplied by the same number, called the scale factor.", do=[COORD([0, 11], [0, 7], **ENL), T("every length × the **scale factor**", x=80, y=170)]),
        dict(say="Rectangle A is 2 squares by 1 square. It is enlarged by scale factor 3. Rectangle B is 6 squares by 3 squares.", do=[MATH("2 × 3 = 6", x=80, y=300), MATH("1 × 3 = 3", x=80, y=390, at=4), B("scale factor 3", x=80, y=490, color=BLUE, at=5)]),
        PAUSE("14.6-k2", "Think about the corners of the 2 rectangles. In an enlargement, do the angles stay the same, or are they multiplied too? Pause the video and decide.", "In an enlargement, angles stay the same or are multiplied?"),
    ]),
    dict(kind="idea", title="Check: the angles", steps=[
        dict(say="The angles stay the same. Both rectangles have 4 right angles. Only the lengths change.", do=[COORD([0, 11], [0, 7], **ENL), B("angles stay the same", x=80, y=190, color=GREEN), T("only the **lengths** change", x=80, y=300)]),
    ]),
    dict(kind="idea", title="Finding the scale factor", steps=[
        dict(say="To find a scale factor, divide a length on the image by the matching length on the object.", do=[B("image ÷ object", x=80, y=160, color=BLUE)]),
        dict(say="A side of 4 centimetres becomes 10 centimetres. 10 divided by 4 is 2.5. The scale factor is 2.5.", do=[MATH("10 ÷ 4 = 2.5", x=80, y=280)]),
        dict(say="An enlarged shape is similar to the original. That means the same shape. But it is not congruent, because the size is different.", do=[T("**similar** (same shape) – but not congruent", x=80, y=390)]),
        PAUSE("14.6-k3", "Your turn. A side of 2 centimetres becomes 7 centimetres. What is the scale factor? Pause the video and try it.", "Sides 2 → 7. What is the scale factor?"),
    ]),
    dict(kind="idea", title="Check: 2 becomes 7", steps=[
        dict(say="Image divided by object: 7 divided by 2 is 3.5. The scale factor is 3.5.", do=[MATH("7 ÷ 2 = 3.5", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I enlarge a shape on a grid?", steps=[
        dict(say="Here is the method. Step 1: count the length of each side in squares, and multiply by the scale factor.", do=[T("1. **Multiply** each length by the scale factor", x=80, y=170)]),
        dict(say="Step 2: start at 1 corner, and draw each side with its new length.", do=[T("2. Start at a corner · draw each **new side**", x=80, y=260)]),
        dict(say="Step 3: keep all the angles the same. For a slanted side, multiply both the across move and the up move.", do=[T("3. Same **angles** · slanted side: multiply **both moves**", x=80, y=350)]),
        dict(say="Step 4: check that every side has been multiplied by the same number.", do=[T("4. **Check** every side", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="On a grid", steps=[
        dict(say="A right-angled triangle has a base of 3 squares and a height of 2 squares. Enlarge it by scale factor 3.", do=[COORD([0, 11], [0, 8], polys=[POLY([(1, 1), (4, 1), (1, 3)], "A")]), T("base **3**, height **2** · scale factor **3**", x=80, y=170)]),
        dict(say="The new base is 3 times 3, which is 9 squares. The new height is 2 times 3, which is 6 squares.", do=[MATH("3 × 3 = 9", x=80, y=280), MATH("2 × 3 = 6", x=80, y=370, at=4)]),
        dict(say="Draw the new triangle. It is 3 times as wide, and 3 times as tall, with the same right angle.", do=[COORD([0, 11], [0, 8], polys=[POLY([(1, 1), (4, 1), (1, 3)], "A"), POLY([(1, 1), (10, 1), (1, 7)], "B", "#D64545")]), B("base 9, height 6", x=80, y=480, color=GREEN)]),
    ]),
    dict(kind="example", title="Find the scale factor", steps=[
        dict(say="A rectangle is 6 centimetres by 4 centimetres. It is enlarged to 15 centimetres by 10 centimetres. Find the scale factor.", do=[T("**6 cm × 4 cm** → **15 cm × 10 cm**", x=80, y=160)]),
        dict(say="15 divided by 6 is 2.5. Check with the other pair of sides: 10 divided by 4 is also 2.5.", do=[MATH("15 ÷ 6 = 2.5", x=80, y=280), MATH("10 ÷ 4 = 2.5", x=520, y=280, at=4)]),
        dict(say="Both pairs give the same number, so this is an enlargement, with scale factor 2.5.", do=[B("scale factor 2.5", x=80, y=400, color=GREEN)]),
    ]),
    dict(kind="example", title="A slanted side", steps=[
        dict(say="A side of a shape goes 2 squares right and 1 square up. What happens to it in an enlargement with scale factor 4?", do=[T("**2 right, 1 up** · scale factor **4**", x=80, y=160)]),
        dict(say="Multiply both moves by 4. The new side goes 8 squares right and 4 squares up.", do=[MATH("2 × 4 = 8", x=80, y=280), MATH("1 × 4 = 4", x=520, y=280, at=3), B("8 right, 4 up", x=80, y=400, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="Not an enlargement", steps=[
        dict(say="A rectangle 5 by 2 becomes a rectangle 10 by 6. Is this an enlargement?", do=[T("**5 × 2** → **10 × 6**", x=80, y=160)]),
        dict(say="10 divided by 5 is 2. But 6 divided by 2 is 3. The 2 numbers are different.", do=[MATH("10 ÷ 5 = 2", x=80, y=280), MATH("6 ÷ 2 = 3", x=520, y=280, at=3)]),
        dict(say="So no. The shape has been stretched. It is not an enlargement.", do=[B("not an enlargement", x=80, y=400, color=RED)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Enlarge a rectangle, 3 by 4, by scale factor 2. Here is Milo's working. Which line goes wrong first?", do=LINES("Milo", "enlarge a 3 × 4 rectangle by scale factor 2", ["3 + 2 = 5 and 4 + 2 = 6", "New rectangle: 5 × 6"])),
        dict(say="Line 1 is wrong. A scale factor means multiply every length. It does not mean add.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="3 times 2 is 6, and 4 times 2 is 8. The new rectangle is 6 by 8.", do=[B("6 × 8", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Making things bigger", steps=[
        dict(say="A microscope is an enlargement machine. With a magnification of 400, a cell 0.02 millimetres wide looks 8 millimetres wide.", do=[E("🔬", 90, 160, 100), MATH("0.02 mm × 400 = 8 mm", x=230, y=180)]),
        dict(say="When you pinch to zoom on a phone, the picture is enlarged. Every length grows by the same scale factor, so nothing looks stretched.", do=[E("📱", 90, 320, 100), T("pinch to zoom: one **scale factor** for every length", x=230, y=350)]),
        dict(say="A scale factor of 2 makes a photo 2 times as wide and 2 times as tall. So it covers 4 times as much of the screen.", do=[T("× 2 wide and × 2 tall → **4 times** the area", x=230, y=470, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.6-k4", "One last question. A rectangle 3 by 4 becomes a rectangle 9 by 16. Is that an enlargement, or not an enlargement? Pause the video and decide.", "3 × 4 → 9 × 16 is an enlargement or not an enlargement?"),
        dict(say="It is not an enlargement. 9 divided by 3 is 3, but 16 divided by 4 is 4. The sides are not multiplied by the same number.", do=[MATH("9 ÷ 3 = 3", x=80, y=190), MATH("16 ÷ 4 = 4", x=520, y=190, at=3), B("not an enlargement", x=80, y=320, color=GREEN, at=5)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: an enlargement multiplies every length by the scale factor.", do=[T("• **Enlargement**: every length × the scale factor", x=80, y=170)]),
        dict(say="The angles do not change, so the shape stays the same.", do=[T("• **Angles** do not change", x=80, y=250)]),
        dict(say="The scale factor is an image length, divided by the matching object length.", do=[T("• Scale factor = **image ÷ object**", x=80, y=330)]),
        dict(say="On a grid, multiply both the across move and the up move.", do=[T("• On a grid: multiply **both moves**", x=80, y=410)]),
    ]),
]
