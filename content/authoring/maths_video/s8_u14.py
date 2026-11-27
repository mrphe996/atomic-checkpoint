# -*- coding: utf-8 -*-
"""Stage 8 · Unit 14 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG
from .s7_u04 import TBL, ROW
from .s7_u05 import BIG
from .s7_u11 import COORD
from .s7_u14 import P, POLY

BR = lambda deg, frm="A", to="B", x=760, y=130, w=460, at=0: BIG(FIG(x, y, w, at, kind="bearing", bearing=deg, **{"from": frm, "to": to}))
V = lambda a, b: f"$$\\begin{{pmatrix}}{a}\\\\{b}\\end{{pmatrix}}$$".replace("-", "−")     # a column vector
G = lambda xr, yr, at=0, x=700, y=120, w=520, **k: COORD(xr, yr, x=x, y=y, w=w, at=at, **k)

VIDEOS = {}

VIDEOS["14.1"] = [
    dict(kind="hook", title="Lost in the fog", steps=[
        dict(say="A boat leaves a harbour and sails on a bearing of 0 7 0 degrees. That means 70 degrees, turning clockwise from north.",
             do=[E("⛵", 90, 170, 100), T("sails on a bearing of **070°**", x=230, y=200), BR(70, "H", "boat", at=2)]),
        PAUSE("14.1-k1", "Roughly which way does the boat point? Pause the video and choose.", "A bearing of 070° points roughly …"),
    ]),
    dict(kind="hook", title="East-north-east", steps=[
        dict(say="70 degrees is a bit less than 90, which is east. So the boat heads east-north-east, a little north of east.",
             do=[BR(70, "H", "boat"), B("east-north-east", x=80, y=200, color=GREEN)]),
        dict(say="And what bearing would take it straight back? We will find out.", do=[T("the bearing back?", x=80, y=300)]),
    ]),
    dict(kind="recall", title="Compass directions", steps=[
        dict(say="Remember: north is 0 degrees, east is 90, south is 180, and west is 270. They are measured clockwise from north. South-east is halfway between east and south: 135 degrees.",
             do=[T("N **0°** · E **90°** · S **180°** · W **270°**", x=80, y=180), MATH("SE = 135°", x=80, y=280, at=8)]),
    ]),
    dict(kind="idea", title="What a bearing is", steps=[
        dict(say="A bearing is the direction of one point from another. It is measured from north, clockwise, and it is always written with three figures, like 0 7 0, 2 4 5, or 0 0 8.",
             do=[B("from **north**, **clockwise**, **3 figures**", x=80, y=170, color=BLUE), T("070° · 245° · 008°", x=80, y=270), BR(70)]),
        dict(say="The bearing of B from A means: stand at A, face north, then turn clockwise until you face B.", do=[T("“B **from A**”: stand at **A**", x=80, y=360)]),
        PAUSE("14.1-k2", "Your turn. What is the bearing of due west? Write three figures. Pause the video and try it.", "Bearing of due west?"),
    ]),
    dict(kind="idea", title="Back bearings", steps=[
        dict(say="Due west is 2 7 0 degrees. Now, the bearing back. The bearing of A from B differs by 180 degrees. If B is 0 4 0 from A, then A is 40 plus 180, which is 2 2 0 from B.",
             do=[MATH("west = 270°", x=80, y=170, color=GREEN), TBL(["B from A", "A from B"], [["040°", "040° + 180° = 220°"], ["300°", "300° − 180° = 120°"]], y=260), ROW(0, 5)]),
        dict(say="If the bearing is more than 180, subtract 180 instead. 3 0 0 becomes 1 2 0.", do=[ROW(1, 0.3)]),
    ]),
    dict(kind="method", title="How do I find or use a bearing?", steps=[
        dict(say="Here is the method. Step 1: find the point you are measuring from, and draw north there.", do=[T("1. Draw **north** at the point you measure **from**", x=80, y=170)]),
        dict(say="Step 2: measure clockwise from north to the line joining the points.", do=[T("2. Measure **clockwise** from north", x=80, y=260)]),
        dict(say="Step 3: write the answer with three figures.", do=[T("3. **Three figures**", x=80, y=350)]),
        dict(say="Step 4: for the back bearing, add or subtract 180.", do=[T("4. Back bearing: **± 180°**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Reading a bearing", steps=[
        dict(say="The angle clockwise from north at P to Q is 115 degrees. So the bearing of Q from P is 1 1 5. The bearing of P from Q is 115 plus 180, which is 2 9 5.",
             do=[BR(115, "P", "Q"), MATH("Q from P = 115°", x=80, y=180), B("P from Q = 295°", x=80, y=280, color=GREEN, at=8)]),
        PAUSE("14.1-k3", "Your turn. A bearing is 0 7 0 degrees. What is the back bearing? Pause and work it out.", "Bearing 070°. Back bearing?"),
    ]),
    dict(kind="example", title="Check: back from 070°", steps=[
        dict(say="70 plus 180 is 250. The back bearing is 2 5 0 degrees. That takes the boat straight back to the harbour.", do=[B("070° + 180° = 250°", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Anticlockwise angles", steps=[
        dict(say="The angle from north anticlockwise to C, at D, is 40 degrees. Bearings go clockwise, so the bearing is 360 minus 40, which is 3 2 0 degrees.",
             do=[BR(320, "D", "C"), MATH("360° − 40° = 320°", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="The angle from north, anticlockwise, to T is 65 degrees. Sam writes the bearing. Which line is wrong?", do=LINES("Sam", "65° anticlockwise from north to T", ["bearing = 065°"])),
        dict(say="Line 1 is wrong. Bearings are measured clockwise. 360 minus 65 is 295.", do=[dict(a="cross", id="l1")]),
        dict(say="The bearing is 2 9 5 degrees.", do=[B("bearing = 295°", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Ships and planes", steps=[
        dict(say="Pilots and ship captains use bearings. Airport runways are numbered by their bearing, divided by 10. A runway pointing on a bearing of about 2 7 0 is called runway 27.",
             do=[E("✈️", 90, 170, 100), T("runway **27** points about **270°**", x=230, y=200)]),
        dict(say="The other end of the same runway points the opposite way, 0 9 0, so it is called runway 9.", do=[T("the other end: **090°** → runway **9**", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.1-k4", "One last question. What is south-west as a bearing? Write three figures. Pause the video and answer.", "South-west as a bearing?"),
        dict(say="South is 180, and west is 270. South-west is halfway between: 2 2 5 degrees.", do=[B("225°", x=80, y=200, color=GREEN), BR(225, "A", "SW")]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: bearings are measured from north, clockwise, with three figures.", do=[T("• From **north**, **clockwise**, **3 figures**", x=80, y=170)]),
        dict(say="From A means stand at A.", do=[T("• “From A” means stand at A", x=80, y=250)]),
        dict(say="The back bearing is the bearing plus or minus 180 degrees.", do=[T("• Back bearing = bearing ± 180°", x=80, y=330)]),
        dict(say="Use a protractor and a scale for drawings.", do=[T("• Protractor and scale for drawings", x=80, y=410)]),
    ]),
]

VIDEOS["14.2"] = [
    dict(kind="hook", title="Meeting halfway", steps=[
        dict(say="Two friends live at 2, 7 and at 10, 3 on a town grid. They want to meet exactly halfway between their homes.",
             do=[E("🏠", 90, 170, 100), T("homes at **(2, 7)** and **(10, 3)**", x=230, y=200), G([0, 11], [0, 8], at=2, points=[P(2, 7, "A"), P(10, 3, "B")])]),
        PAUSE("14.2-k1", "Where should they meet? Pause the video and work it out.", "Meeting point?"),
    ]),
    dict(kind="hook", title="Halfway across, halfway up", steps=[
        dict(say="Halfway between 2 and 10 is 6. Halfway between 7 and 3 is 5. They meet at 6, 5.",
             do=[G([0, 11], [0, 8], points=[P(2, 7, "A"), P(10, 3, "B"), P(6, 5, "M")], segs=[[[2, 7], [10, 3]]]), MATH("x: 6 · y: 5", x=80, y=200), B("(6, 5)", x=80, y=300, color=GREEN, at=4)]),
    ]),
    dict(kind="recall", title="Coordinates", steps=[
        dict(say="Remember: in a coordinate, x comes first, across. Then y, up. And halfway between two numbers is their mean: add them and halve.", do=[T("(x, y): **across**, then **up**", x=80, y=180), MATH("halfway between 2 and 10 = (2 + 10) ÷ 2 = 6", x=80, y=280, at=5)]),
    ]),
    dict(kind="idea", title="The midpoint", steps=[
        dict(say="The midpoint of a line segment is halfway along it. Its x coordinate is halfway between the two x coordinates. Its y coordinate is halfway between the two y coordinates.",
             do=[B("midpoint = (mean of the x's, mean of the y's)", x=80, y=170, color=BLUE)]),
        dict(say="In symbols: add the x's and halve, and add the y's and halve.", do=[MATH("((x₁ + x₂) ÷ 2, (y₁ + y₂) ÷ 2)", x=80, y=280)]),
        PAUSE("14.2-k2", "Your turn. What is the midpoint of 0, 0 and 8, 6? Pause the video and try it.", "Midpoint of (0, 0) and (8, 6)?"),
    ]),
    dict(kind="idea", title="Check: (0, 0) and (8, 6)", steps=[
        dict(say="0 plus 8 is 8, halved is 4. 0 plus 6 is 6, halved is 3. The midpoint is 4, 3.", do=[B("(4, 3)", x=80, y=200, color=GREEN)]),
        dict(say="With negatives, add carefully. The midpoint of negative 4, 1 and 2, negative 5 is negative 1, negative 2.", do=[MATH("(−4, 1) and (2, −5) → (−1, −2)", x=80, y=310)]),
    ]),
    dict(kind="method", title="How do I find a midpoint?", steps=[
        dict(say="Here is the method. Step 1: add the two x coordinates, and halve.", do=[T("1. Add the **x**'s and halve", x=80, y=170)]),
        dict(say="Step 2: add the two y coordinates, and halve.", do=[T("2. Add the **y**'s and halve", x=80, y=260)]),
        dict(say="Step 3: write the point as x, y.", do=[T("3. Write **(x, y)**", x=80, y=350)]),
        dict(say="Step 4: to find a missing end, step from the known end to the midpoint, then take the same step again.", do=[T("4. Missing end: take the **same step again**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Halves", steps=[
        dict(say="Find the midpoint of 0, 3 and 5, 8. 0 plus 5 is 5, halved is 2.5. 3 plus 8 is 11, halved is 5.5. The midpoint is 2.5, 5.5.", do=[B("(2.5, 5.5)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="A missing end", steps=[
        dict(say="M at 4, 1 is the midpoint of A B, and A is at 1, negative 3. Find B. From A to M is 3 across and 4 up. Take the same step again from M: 7, 5.",
             do=[G([-1, 8], [-4, 6], points=[P(1, -3, "A"), P(4, 1, "M"), P(7, 5, "B")], segs=[[[1, -3], [7, 5]]]), MATH("A → M: +3, +4", x=80, y=200), B("B = (7, 5)", x=80, y=300, color=GREEN, at=8)]),
        PAUSE("14.2-k3", "Your turn. M is 2, 2 and A is 0, 0. Where is B? Pause and work it out.", "M(2, 2), A(0, 0). B?"),
    ]),
    dict(kind="example", title="Check: B", steps=[
        dict(say="From A to M is 2 across and 2 up. The same again from M gives 4, 4.", do=[B("B = (4, 4)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Diagonals of a square", steps=[
        dict(say="A square has opposite corners at 1, 1 and 5, 5. Where do the diagonals cross? The diagonals of a square cut each other in half, so they cross at the midpoint: 3, 3.",
             do=[G([0, 6], [0, 6], polys=[POLY([(1, 1), (5, 1), (5, 5), (1, 5)])], points=[P(3, 3, "(3, 3)")], segs=[[[1, 1], [5, 5]], [[5, 1], [1, 5]]]), B("(3, 3)", x=80, y=200, color=GREEN, at=8)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Kim finds the midpoint of 2, 3 and 8, 9. Which line goes wrong first?", do=LINES("Kim", "the midpoint of (2, 3) and (8, 9)", ["x: (8 − 2) ÷ 2 = 3", "y: (9 − 3) ÷ 2 = 3"])),
        dict(say="Line 1 is wrong. She subtracted. You must add the coordinates, then halve.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="2 plus 8 is 10, halved is 5. 3 plus 9 is 12, halved is 6. The midpoint is 5, 6.", do=[B("(5, 6)", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Game maps", steps=[
        dict(say="Video games use midpoints all the time. To place a camera halfway between two players, the game finds the midpoint of their coordinates, many times every second.",
             do=[E("🎮", 90, 170, 100), T("camera at the **midpoint** of two players", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.2-k4", "One last question. What is the midpoint of negative 4, 0 and 4, 0? Pause the video and answer.", "Midpoint of (−4, 0) and (4, 0)?"),
        dict(say="Negative 4 plus 4 is 0, and 0 plus 0 is 0. The midpoint is the origin, 0, 0.", do=[B("(0, 0)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the midpoint is the mean of the x's, and the mean of the y's.", do=[T("• Midpoint = (mean of x's, mean of y's)", x=80, y=170)]),
        dict(say="Take care with negative numbers.", do=[T("• Take care with negatives", x=80, y=250)]),
        dict(say="For a missing end, repeat the step from the end to the midpoint.", do=[T("• Missing end: repeat the step", x=80, y=330)]),
        dict(say="The diagonals of a parallelogram cross at their midpoints.", do=[T("• Parallelogram diagonals meet at their midpoints", x=80, y=410)]),
    ]),
]

TRI = [(1, 1), (4, 1), (1, 3)]
VIDEOS["14.3"] = [
    dict(kind="hook", title="Sliding furniture", steps=[
        dict(say="In a room planning app, a sofa is dragged 5 squares right and 2 squares down. The app records the move as two numbers stacked in brackets.",
             do=[E("🛋️", 90, 170, 100), T("**5 right**, **2 down**", x=230, y=200), G([-1, 9], [-3, 4], at=2, polys=[POLY(TRI, "A"), POLY([(6, -1), (9, -1), (6, 1)], "B")])]),
        PAUSE("14.3-k1", "How is that move written? Pause the video and choose.", "The sofa move?"),
    ]),
    dict(kind="hook", title="A column vector", steps=[
        dict(say="It is written as a column vector, with 5 on top and negative 2 underneath. The top number is the move across. The bottom number is the move up or down.",
             do=[MATH(V(5, -2), x=80, y=170), T("top: **across** (+ right, − left)", x=280, y=180), T("bottom: **up/down** (+ up, − down)", x=280, y=250)]),
    ]),
    dict(kind="recall", title="Translations", steps=[
        dict(say="Remember: a translation slides a shape. It does not turn or flip. Move 2, 3 by 4 right and 1 up, and you get 6, 4.", do=[T("a translation **slides**: no turning, no flipping", x=80, y=180), MATH("(2, 3) → (6, 4)", x=80, y=280, at=5)]),
    ]),
    dict(kind="idea", title="Column vectors", steps=[
        dict(say="A translation is described by a column vector. The starting shape is the object, and the moved shape is the image.",
             do=[G([-1, 9], [-3, 4], polys=[POLY(TRI, "object"), POLY([(5, -2), (8, -2), (5, 0)], "image")]), MATH(V(4, -3), x=80, y=180)]),
        dict(say="The image is congruent to the object. It has the same shape and size, and faces the same way.", do=[T("the image is **congruent**", x=80, y=330)]),
        PAUSE("14.3-k2", "Your turn. A translated image is what? Pause the video and choose.", "A translated image is …"),
    ]),
    dict(kind="idea", title="Describing and reversing", steps=[
        dict(say="It is congruent. To describe a translation, pick one vertex and count across, then up or down, to its image.", do=[B("congruent", x=80, y=170, color=GREEN), T("count from a **vertex** to its **image**", x=80, y=270)]),
        dict(say="To reverse a translation, change both signs. The reverse of 4 over negative 3 is negative 4 over 3.", do=[MATH(f"{V(4, -3)} → {V(-4, 3)}", x=80, y=360)]),
    ]),
    dict(kind="method", title="How do I translate by a vector?", steps=[
        dict(say="Here is the method. Step 1: read the top number. Move each vertex that many right, or left if it is negative.", do=[T("1. **Top**: right (+) or left (−)", x=80, y=170)]),
        dict(say="Step 2: read the bottom number. Move up, or down if it is negative.", do=[T("2. **Bottom**: up (+) or down (−)", x=80, y=260)]),
        dict(say="Step 3: plot the image vertices, and join them.", do=[T("3. Plot and join the image", x=80, y=350)]),
        dict(say="Step 4: check that the image is the same shape, the same size, and the same way round.", do=[T("4. **Check**: congruent, same way round", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Translate a triangle", steps=[
        dict(say="Translate the triangle 1, 1; 4, 1; 1, 3 by the vector negative 2 over 3. Subtract 2 from each x, and add 3 to each y.",
             do=[MATH(V(-2, 3), x=80, y=170), G([-3, 5], [0, 7], polys=[POLY(TRI, "A"), POLY([(-1, 4), (2, 4), (-1, 6)], "B")], at=5)]),
        dict(say="The image is at negative 1, 4; 2, 4; and negative 1, 6.", do=[MATH("(−1, 4), (2, 4), (−1, 6)", x=80, y=330, color=GREEN)]),
        PAUSE("14.3-k3", "Your turn. Translate 0, 0 by the vector negative 3 over negative 4. Pause and work it out.", "(0, 0) by (−3 over −4)?"),
    ]),
    dict(kind="example", title="Check: (0, 0)", steps=[
        dict(say="3 left and 4 down from 0, 0 gives negative 3, negative 4.", do=[B("(−3, −4)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Describe a translation", steps=[
        dict(say="A vertex moves from 3, negative 1 to negative 2, 4. Across: negative 2 minus 3 is negative 5. Up: 4 minus negative 1 is 5. The vector is negative 5 over 5.",
             do=[MATH("x: −2 − 3 = −5", x=80, y=180), MATH("y: 4 − (−1) = 5", x=80, y=270, at=5), MATH(V(-5, 5), x=80, y=360, color=GREEN, at=9)]),
    ]),
    dict(kind="example", title="Two translations", steps=[
        dict(say="Translate by 3 over 1, then by negative 1 over 4. Add the tops: 2. Add the bottoms: 5. It is the same as one translation by 2 over 5.",
             do=[MATH(f"{V(3, 1)} + {V(-1, 4)} = {V(2, 5)}", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ed translates 2, 2 by the vector 1 over 4. Which line is wrong?", do=LINES("Ed", "(2, 2) by (1 over 4)", ["4 right, 1 up → (6, 3)"])),
        dict(say="Line 1 is wrong. He swapped the numbers. The top number is the move across: 1 right, then 4 up.", do=[dict(a="cross", id="l1")]),
        dict(say="2 plus 1 is 3, and 2 plus 4 is 6. The image is 3, 6.", do=[B("(3, 6)", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Animation", steps=[
        dict(say="Cartoon and game animators use translations. To move a character across the screen, the computer adds the same vector to every point, many times a second.",
             do=[E("🎬", 90, 170, 100), T("move a character: add the **same vector** to every point", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.3-k4", "One last question. What is the reverse of 2 over negative 5? Pause the video and choose.", "Reverse of (2 over −5)?"),
        dict(say="Change both signs: negative 2 over 5.", do=[MATH(V(-2, 5), x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: in a column vector, the top is across and the bottom is up or down.", do=[T("• Column vector: top **across**, bottom **up/down**", x=80, y=170)]),
        dict(say="Translations keep shapes congruent, and the same way round.", do=[T("• Congruent, same way round", x=80, y=250)]),
        dict(say="Describe one by counting from a vertex to its image.", do=[T("• Count from a vertex to its image", x=80, y=330)]),
        dict(say="To reverse, change both signs.", do=[T("• Reverse: change both signs", x=80, y=410)]),
    ]),
]

VIDEOS["14.4"] = [
    dict(kind="hook", title="Lake reflections", steps=[
        dict(say="A photo shows a mountain reflected in a still lake. The water line is perfectly horizontal. The peak is 3 units above the water.",
             do=[E("🏔️", 90, 170, 100), T("peak **3 units above** the water", x=230, y=200), G([-3, 3], [-4, 4], at=2, lines=[dict(y=0, label="water")], polys=[POLY([(-2, 0), (2, 0), (0, 3)], "peak")])]),
        PAUSE("14.4-k1", "Where is the reflection of the peak? Pause the video and choose.", "The reflected peak is …"),
    ]),
    dict(kind="hook", title="3 units below", steps=[
        dict(say="A reflection is the same distance from the mirror line, on the other side. So the reflected peak is 3 units below the water.",
             do=[G([-3, 3], [-4, 4], lines=[dict(y=0, label="water")], polys=[POLY([(-2, 0), (2, 0), (0, 3)], "peak"), POLY([(-2, 0), (2, 0), (0, -3)], "image")]), B("3 units below", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="recall", title="Lines on a grid", steps=[
        dict(say="Remember: x equals 3 is a vertical line. y equals negative 1 is a horizontal line.", do=[G([-4, 4], [-4, 4], lines=[dict(x=3, label="x = 3"), dict(y=-1, label="y = −1")]), T("x = a: **vertical** · y = b: **horizontal**", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Reflecting in a line", steps=[
        dict(say="Each image point is the same distance from the mirror line as the object point, but on the other side. Measure at right angles to the line.",
             do=[T("same distance, **other side**, at right angles", x=80, y=170)]),
        dict(say="Reflect in x equals 2. The point 4, 2 is 2 to the right of the line. So its image is 2 to the left: 0, 2.",
             do=[G([-4, 6], [-1, 5], lines=[dict(x=2, label="x = 2")], points=[P(4, 2, "(4, 2)"), P(0, 2, "(0, 2)")]), MATH("(4, 2) → (0, 2)", x=80, y=280)]),
        PAUSE("14.4-k2", "Your turn. Reflect 5, 3 in x equals 2. Pause the video and try it.", "Reflect (5, 3) in x = 2."),
    ]),
    dict(kind="idea", title="Check, and diagonal lines", steps=[
        dict(say="5, 3 is 3 to the right of the line, so its image is 3 to the left: negative 1, 3. Reflecting in the line y equals x swaps the coordinates. 3, 1 becomes 1, 3.",
             do=[B("(−1, 3)", x=80, y=170, color=GREEN), G([-1, 5], [-1, 5], lines=[dict(m=1, c=0, label="y = x")], points=[P(3, 1, "(3, 1)"), P(1, 3, "(1, 3)")], at=6), MATH("y = x: (a, b) → (b, a)", x=80, y=280, at=6)]),
        dict(say="To find a mirror line, find the midpoints between object points and their images. The mirror line goes through them.", do=[T("mirror line: through the **midpoints**", x=80, y=380)]),
    ]),
    dict(kind="method", title="How do I reflect in a line?", steps=[
        dict(say="Here is the method. Step 1: draw the mirror line. x equals a is vertical, y equals b is horizontal, and y equals x is diagonal.", do=[T("1. Draw the **mirror line**", x=80, y=170)]),
        dict(say="Step 2: for each vertex, count the distance to the line, at right angles.", do=[T("2. Count the distance at **right angles**", x=80, y=260)]),
        dict(say="Step 3: count the same distance on the other side, and plot the image.", do=[T("3. Same distance on the **other side**", x=80, y=350)]),
        dict(say="Step 4: check that the image is flipped, but the same size.", do=[T("4. **Check**: flipped, same size", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A horizontal line", steps=[
        dict(say="Reflect 1, 5 and 3, negative 1 in y equals 1. 1, 5 is 4 above the line, so its image is 4 below: 1, negative 3. 3, negative 1 is 2 below, so its image is 2 above: 3, 3.",
             do=[G([-1, 5], [-4, 6], lines=[dict(y=1, label="y = 1")], points=[P(1, 5, "(1, 5)"), P(1, -3, "(1, −3)"), P(3, -1, "(3, −1)"), P(3, 3, "(3, 3)")]), MATH("(1, −3) and (3, 3)", x=80, y=200, color=GREEN, at=10)]),
        PAUSE("14.4-k3", "Your turn. Reflect 4, 1 in the line y equals x. Pause and work it out.", "Reflect (4, 1) in y = x."),
    ]),
    dict(kind="example", title="Check: in y = x", steps=[
        dict(say="Swap the coordinates. 4, 1 becomes 1, 4.", do=[B("(1, 4)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Find the mirror line", steps=[
        dict(say="2, 5 maps to 2, negative 1, and 4, 6 maps to 4, negative 2. The midpoints are 2, 2 and 4, 2. They are both on the line y equals 2. That is the mirror line.",
             do=[MATH("midpoints (2, 2) and (4, 2)", x=80, y=180), B("mirror line: y = 2", x=80, y=290, color=GREEN, at=8)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ivy reflects 5, 1 in the line x equals 3. Which line is wrong?", do=LINES("Ivy", "(5, 1) in x = 3", ["(5, 1) → (−5, 1)"])),
        dict(say="Line 1 is wrong. That is a reflection in the y axis. Count from x equals 3 instead: 5 is 2 to the right, so the image is 2 to the left.", do=[dict(a="cross", id="l1")]),
        dict(say="The image is 1, 1.", do=[B("(1, 1)", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Ambulance signs", steps=[
        dict(say="The word ambulance is often painted back to front on the front of the vehicle. Drivers ahead see it in their rear-view mirror, reflected the right way round.",
             do=[E("🚑", 90, 170, 100), T("written **back to front** → reads correctly in a mirror", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.4-k4", "One last question. Reflect 0, 4 in the line y equals 1. Pause the video and answer.", "Reflect (0, 4) in y = 1."),
        dict(say="0, 4 is 3 above the line y equals 1. So its image is 3 below: 0, negative 2.", do=[B("(0, −2)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: same distance from the mirror line, on the other side, at right angles.", do=[T("• Same distance, other side, at right angles", x=80, y=170)]),
        dict(say="x equals a is vertical. y equals b is horizontal. Reflecting in y equals x swaps the coordinates.", do=[T("• x = a vertical · y = b horizontal · y = x swaps", x=80, y=250)]),
        dict(say="Find a mirror line from the midpoints of object and image pairs.", do=[T("• Mirror line through the midpoints", x=80, y=330)]),
        dict(say="Reflections flip a shape, but keep it congruent.", do=[T("• Flipped, but congruent", x=80, y=410)]),
    ]),
]

RA = [(0, 0), (3, 0), (0, 2)]
RB = [(0, 0), (0, -3), (-2, 0)]
VIDEOS["14.5"] = [
    dict(kind="hook", title="A revolving door", steps=[
        dict(say="A revolving door turns 90 degrees clockwise about its centre post every time someone pushes it.", do=[E("🚪", 90, 170, 100), T("turns **90° clockwise** about its centre", x=230, y=200)]),
        dict(say="To describe a turn exactly, what three facts do you need?", do=[T("what **three facts** describe a turn?", x=230, y=300)]),
        PAUSE("14.5-k1", "What are the three facts? Pause the video and choose.", "Three facts are …"),
    ]),
    dict(kind="hook", title="Angle, direction, centre", steps=[
        dict(say="You need the angle, the direction, and the centre. For the door: 90 degrees, clockwise, about the centre post.", do=[B("angle · direction · centre", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="recall", title="Turns", steps=[
        dict(say="Remember: a quarter turn is 90 degrees, a half turn is 180, and a three quarter turn is 270 degrees.", do=[T("¼ turn **90°** · ½ turn **180°** · ¾ turn **270°**", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Describing a rotation", steps=[
        dict(say="A rotation needs three facts: the angle, the direction, clockwise or anticlockwise, and the centre of rotation. A half turn needs no direction.",
             do=[G([-4, 4], [-4, 4], polys=[POLY(RA, "A"), POLY(RB, "B")]), T("angle · direction · **centre**", x=80, y=180)]),
        dict(say="The image is congruent to the object. The centre is the only point that does not move.", do=[T("the **centre** stays still", x=80, y=280)]),
        PAUSE("14.5-k2", "Your turn. What is the only fixed point in a rotation? Pause the video and choose.", "The only fixed point in a rotation is …"),
    ]),
    dict(kind="idea", title="Rules for the origin", steps=[
        dict(say="The centre. You can rotate with tracing paper: trace the shape, pin the centre, and turn. About the origin there are also rules.",
             do=[B("the centre", x=80, y=170, color=GREEN), TBL(["Rotation about (0, 0)", "(x, y) →"], [["90° clockwise", "(y, −x)"], ["90° anticlockwise", "(−y, x)"], ["180°", "(−x, −y)"]], y=270), ROW(0, 5), ROW(1, 6), ROW(2, 7)]),
    ]),
    dict(kind="method", title="How do I rotate a shape?", steps=[
        dict(say="Here is the method. Step 1: find the angle, the direction and the centre.", do=[T("1. Angle, direction, **centre**", x=80, y=170)]),
        dict(say="Step 2: trace the shape, and pin the centre. Or use the rules for the origin.", do=[T("2. **Trace** and pin, or use the rules", x=80, y=260)]),
        dict(say="Step 3: turn through the angle in the right direction, and plot the image.", do=[T("3. Turn and plot", x=80, y=350)]),
        dict(say="Step 4: to describe a rotation, give all three facts.", do=[T("4. Describe with **all three** facts", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="90° clockwise", steps=[
        dict(say="Rotate 2, 5 through 90 degrees clockwise about the origin. The rule is x, y goes to y, negative x.", do=[MATH("(x, y) → (y, −x)", x=80, y=170)]),
        PAUSE("14.5-k3", "Your turn. Use the rule. Where does 2, 5 go? Pause and work it out.", "Rotate (2, 5) 90° clockwise about (0, 0)."),
    ]),
    dict(kind="example", title="Check: (2, 5)", steps=[
        dict(say="y is 5, and negative x is negative 2. So 2, 5 goes to 5, negative 2.", do=[G([-1, 6], [-3, 6], points=[P(2, 5, "(2, 5)"), P(5, -2, "(5, −2)")]), B("(5, −2)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Describe a rotation", steps=[
        dict(say="Triangle A maps to triangle B. The point 0, 0 stays fixed, so that is the centre. The point 3, 0 moves to 0, negative 3: a quarter turn clockwise. So it is a rotation of 90 degrees clockwise, about 0, 0.",
             do=[G([-4, 4], [-4, 4], polys=[POLY(RA, "A"), POLY(RB, "B")]), B("90° clockwise about (0, 0)", x=80, y=200, color=GREEN, at=12)]),
    ]),
    dict(kind="example", title="Another way to say it", steps=[
        dict(say="A turn of 270 degrees anticlockwise ends in the same place as 90 degrees clockwise, because 360 minus 270 is 90.", do=[MATH("270° anticlockwise = 90° clockwise", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ana describes a quarter turn. Which line is wrong?", do=LINES("Ana", "a quarter turn A → B", ["rotation of 90°"])),
        dict(say="Line 1 is not complete. A rotation needs the direction, and the centre, as well as the angle.", do=[dict(a="cross", id="l1")]),
        dict(say="For example: rotation 90 degrees clockwise, about 0, 0.", do=[B("90° clockwise about (0, 0)", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Clock hands", steps=[
        dict(say="A clock's minute hand is a rotation about the centre of the clock. It turns 360 degrees every hour, so 6 degrees every minute.",
             do=[E("🕐", 90, 170, 100), MATH("360° ÷ 60 = 6° per minute", x=230, y=190, color=BLUE)]),
        dict(say="In 15 minutes it rotates 90 degrees clockwise.", do=[T("15 minutes → **90° clockwise**", x=230, y=300)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.5-k4", "One last question. Rotate 4, 1 through 180 degrees about the origin. Pause the video and answer.", "(4, 1) through 180° about (0, 0)?"),
        dict(say="A half turn changes both signs. 4, 1 goes to negative 4, negative 1.", do=[B("(−4, −1)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: angle, direction and centre.", do=[T("• Angle, direction, centre", x=80, y=170)]),
        dict(say="Rotations keep shapes congruent.", do=[T("• Rotations keep shapes congruent", x=80, y=250)]),
        dict(say="About the origin: 90 clockwise gives y, negative x. 90 anticlockwise gives negative y, x. 180 gives negative x, negative y.", do=[T("• 90° cw (y, −x) · 90° acw (−y, x) · 180° (−x, −y)", x=80, y=330)]),
        dict(say="For other centres, work relative to the centre.", do=[T("• Other centres: work relative to the centre", x=80, y=410)]),
    ]),
]

EA = [(1, 1), (3, 1), (3, 2), (1, 2)]
EB = [(1, 1), (7, 1), (7, 4), (1, 4)]
VIDEOS["14.6"] = [
    dict(kind="hook", title="A projector", steps=[
        dict(say="A projector shines a small picture onto a wall. The picture on the wall is 3 times as wide as the original, and every line in it points back to the lamp.",
             do=[E("📽️", 90, 170, 100), T("**3 times** as wide · lines point back to the lamp", x=230, y=200)]),
        PAUSE("14.6-k1", "Is the picture on the wall the same shape as the original? Pause the video and choose.", "Same shape?"),
    ]),
    dict(kind="hook", title="Same shape, bigger", steps=[
        dict(say="Yes. Only the size changes. Every length is multiplied by 3, and the angles stay the same. This is called an enlargement.",
             do=[G([0, 8], [0, 5], polys=[POLY(EA, "A"), POLY(EB, "B")]), B("same shape, 3 × bigger", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="recall", title="Scale factor", steps=[
        dict(say="Remember: an enlargement with scale factor 2 doubles every length. A 4 centimetre side, enlarged by scale factor 3, becomes 12 centimetres.", do=[MATH("4 cm × 3 = 12 cm", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Enlargement from a centre", steps=[
        dict(say="An enlargement changes the size, but not the shape. All lengths are multiplied by the scale factor. All angles stay the same.",
             do=[T("lengths × **scale factor** · angles **unchanged**", x=80, y=170)]),
        dict(say="The centre of enlargement fixes the position. Each image vertex is the scale factor times as far from the centre as the object vertex.",
             do=[G([0, 8], [0, 5], polys=[POLY(EA, "A"), POLY(EB, "B")], points=[P(1, 1, "centre")]), T("distance from the centre × **scale factor**", x=80, y=270)]),
        PAUSE("14.6-k2", "Your turn. In an enlargement, what happens to the angles? Pause the video and choose.", "In an enlargement, angles …"),
    ]),
    dict(kind="idea", title="Scale factor and centre", steps=[
        dict(say="The angles stay the same. The scale factor is the image length divided by the object length. To find the centre, draw lines through pairs of matching vertices. They all meet at the centre.",
             do=[B("angles stay the same", x=80, y=170, color=GREEN), MATH("scale factor = image ÷ object", x=80, y=280, at=4), T("lines through matching vertices meet at the **centre**", x=80, y=380, at=8)]),
    ]),
    dict(kind="method", title="How do I enlarge from a centre?", steps=[
        dict(say="Here is the method. Step 1: from the centre, count the steps across and up to a vertex.", do=[T("1. Count the steps **from the centre**", x=80, y=170)]),
        dict(say="Step 2: multiply those steps by the scale factor.", do=[T("2. **Multiply** the steps by the scale factor", x=80, y=260)]),
        dict(say="Step 3: count the new steps from the centre, and plot the image vertex.", do=[T("3. Count the new steps; plot", x=80, y=350)]),
        dict(say="Step 4: repeat for every vertex, then check the lengths.", do=[T("4. Every vertex; **check** the lengths", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Centre the origin", steps=[
        dict(say="Enlarge the triangle 1, 1; 3, 1; 1, 2 by scale factor 3, centre 0, 0. With the origin as centre, just multiply every coordinate by 3: 3, 3; 9, 3; 3, 6.",
             do=[G([0, 10], [0, 7], polys=[POLY([(1, 1), (3, 1), (1, 2)], "A"), POLY([(3, 3), (9, 3), (3, 6)], "B")], at=4), MATH("(3, 3), (9, 3), (3, 6)", x=80, y=200, color=GREEN, at=7)]),
        PAUSE("14.6-k3", "Your turn. Enlarge 4, 3 by scale factor 2, centre 2, 1. Pause and work it out.", "Enlarge (4, 3) by 2, centre (2, 1)."),
    ]),
    dict(kind="example", title="Check: another centre", steps=[
        dict(say="From the centre 2, 1 to 4, 3 is 2 across and 2 up. Times 2 gives 4 across and 4 up. From 2, 1, that is 6, 5.",
             do=[MATH("2 across, 2 up → × 2 → 4 across, 4 up", x=80, y=180), B("(6, 5)", x=80, y=290, color=GREEN, at=7)]),
    ]),
    dict(kind="example", title="Perimeter", steps=[
        dict(say="A shape with a perimeter of 14 centimetres is enlarged by scale factor 4. Every length is multiplied by 4, so the perimeter is 14 times 4, which is 56 centimetres.",
             do=[MATH("14 × 4 = 56 cm", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ben enlarges 3, 2 by scale factor 2, centre 1, 1. Which line goes wrong first?", do=LINES("Ben", "(3, 2), scale factor 2, centre (1, 1)", ["steps from the centre: 2 across, 1 up", "add 2: 4 across, 3 up → (5, 4)"])),
        dict(say="Line 2 is wrong. He added 2. You must multiply the steps by 2: 4 across and 2 up.", do=[dict(a="cross", id="l2")]),
        dict(say="From 1, 1, that is 5, 3.", do=[B("(5, 3)", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Photo prints", steps=[
        dict(say="When a photo is enlarged from 10 by 15 centimetres to 20 by 30 centimetres, every length is doubled. The scale factor is 2, so the picture keeps its shape.",
             do=[E("🖼️", 90, 170, 100), MATH("10 × 15 → 20 × 30 (scale factor 2)", x=230, y=190)]),
        dict(say="But a print of 20 by 25 would not be an enlargement. The shape would change, so part of the photo must be cut off.", do=[T("20 × 25 is **not** an enlargement", x=230, y=300, color=RED)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.6-k4", "One last question. A side is 3 centimetres, and the scale factor is 5. How long is the image side? Pause the video and answer.", "Side 3 cm, scale factor 5. Image side?"),
        dict(say="3 times 5 is 15 centimetres.", do=[B("15 cm", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: lengths are multiplied by the scale factor. Angles do not change.", do=[T("• Lengths × scale factor; angles unchanged", x=80, y=170)]),
        dict(say="Distances from the centre are multiplied by the scale factor too.", do=[T("• Distances from the centre × scale factor", x=80, y=250)]),
        dict(say="The scale factor is the image length divided by the object length.", do=[T("• Scale factor = image ÷ object", x=80, y=330)]),
        dict(say="Lines through matching vertices meet at the centre.", do=[T("• Lines through matching vertices meet at the centre", x=80, y=410)]),
    ]),
]
