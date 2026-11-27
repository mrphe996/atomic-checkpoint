# -*- coding: utf-8 -*-
"""Stage 7 · Unit 5 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG

BIG = lambda f: dict(f, big=True)   # bigger labels than the app's figures
PT = lambda angles, labels, x=640, y=120, w=600, at=0, start=90: BIG(FIG(x, y, w, at, kind="anglept", angles=angles, start=start, labels=labels))
SHAPE = lambda pts, x=640, y=120, w=600, at=0, **k: BIG(FIG(x, y, w, at, kind="shape", pts=pts, **k))

VIDEOS = {}

VIDEOS["5.1"] = [
    dict(kind="hook", title="Pizza slices", steps=[
        dict(say="A round pizza is cut from the centre into 4 slices. Three of the slices have angles of 95 degrees, 120 degrees and 80 degrees at the centre.",
             do=[E("🍕", 90, 170, 100), T("slices: **95°**, **120°**, **80°** and **?**", x=230, y=200), PT([95, 120, 80, 65], ["95°", "120°", "80°", "?"], at=2)]),
        PAUSE("5.1-k1", "What angle does the last slice make? Pause the video and work it out.", "Pizza slices of 95°, 120° and 80°. What angle is the last slice?"),
    ]),
    dict(kind="hook", title="A full turn", steps=[
        dict(say="All the way round the centre is one full turn. A full turn is 360 degrees.", do=[PT([95, 120, 80, 65], ["95°", "120°", "80°", "65°"]), B("full turn = 360°", x=80, y=170, color=BLUE)]),
        dict(say="The three slices we know add up to 295 degrees.", do=[MATH("95 + 120 + 80 = 295", x=80, y=290)]),
        dict(say="360 minus 295 is 65. The last slice has an angle of 65 degrees.", do=[MATH("360 − 295 = 65", x=80, y=380), B("65°", x=80, y=470, color=GREEN, at=3)]),
    ]),
    dict(kind="recall", title="Angles on a straight line", steps=[
        dict(say="Remember: angles on a straight line add up to 180 degrees. That is half a turn.", do=[B("straight line = 180°", x=80, y=170), PT([128, 52, 180], ["128°", "?", ""], start=0, at=0.4)]),
        dict(say="If one angle is 128 degrees, the other is 180 minus 128, which is 52 degrees.", do=[MATH("180 − 128 = 52°", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="idea", title="Angles around a point", steps=[
        dict(say="The angles around a point always add up to 360 degrees.", do=[B("Angles around a point = 360°", x=80, y=160, color=BLUE), PT([140, 85, 135], ["140°", "85°", "b"], start=20, at=0.4)]),
        dict(say="Here, two of the angles are 140 degrees and 85 degrees. Find angle b.", do=[MATH("140 + 85 = 225", x=80, y=290, at=3)]),
        dict(say="140 plus 85 is 225. 360 minus 225 is 135. So b is 135 degrees.", do=[MATH("360 − 225 = 135", x=80, y=380, at=2.6), B("b = 135°", x=80, y=470, color=GREEN, at=5.6)]),
        PAUSE("5.1-k2", "Your turn. Three angles around a point are 200 degrees, 95 degrees, and y. Find y. Pause the video and try it.", "Angles around a point: 200°, 95° and y. Find y."),
    ]),
    dict(kind="idea", title="Check: 200°, 95° and y", steps=[
        dict(say="200 plus 95 is 295. 360 minus 295 is 65. So y is 65 degrees.", do=[MATH("200 + 95 = 295", x=80, y=190), MATH("360 − 295 = 65", x=80, y=280, at=2.4), B("y = 65°", x=80, y=380, color=GREEN, at=4.6)]),
    ]),
    dict(kind="idea", title="Angles in a quadrilateral", steps=[
        dict(say="A quadrilateral is a shape with 4 straight sides. Draw a diagonal, and it splits into 2 triangles.",
             do=[SHAPE([[0, 0], [7, 0], [8, 4], [1, 5]], ang=["74°", "106°", "82°", "d"]), T("a diagonal makes **2 triangles**", x=80, y=170)]),
        dict(say="The angles in each triangle add up to 180 degrees. So the angles in a quadrilateral add up to 2 times 180, which is 360 degrees.",
             do=[MATH("2 × 180° = 360°", x=80, y=270, color=BLUE), B("quadrilateral = 360°", x=80, y=360, at=5)]),
        dict(say="In this one, 74 plus 106 plus 82 is 262. 360 minus 262 is 98. So angle d is 98 degrees.", do=[MATH("360 − 262 = 98", x=80, y=470), B("d = 98°", x=420, y=462, color=GREEN, at=6)]),
    ]),
    dict(kind="method", title="How do I find a missing angle?", steps=[
        dict(say="Here is the method. Step 1: decide which fact to use. A straight line is 180. Around a point is 360. A triangle is 180. A quadrilateral is 360.",
             do=[T("1. Which fact? line **180°** · point **360°** · triangle **180°** · quadrilateral **360°**", x=80, y=170)]),
        dict(say="Step 2: add the angles you know.", do=[T("2. **Add** the angles you know", x=80, y=260)]),
        dict(say="Step 3: subtract from the total.", do=[T("3. **Subtract** from the total", x=80, y=350)]),
        dict(say="Step 4: check that your answer looks sensible on the diagram.", do=[T("4. Does it look right on the diagram?", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Equal angles around a point", steps=[
        dict(say="Five equal angles meet at a point. How big is each one?", do=[PT([72, 72, 72, 72, 72], ["?", "?", "?", "?", "?"]), B("5 equal angles", x=80, y=170)]),
        dict(say="The total is 360 degrees. Share it equally: 360 divided by 5 is 72. Each angle is 72 degrees.", do=[MATH("360 ÷ 5 = 72", x=80, y=290, at=2.4), B("72° each", x=80, y=390, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Using algebra", steps=[
        dict(say="Around a point, the angles are 2 x, 3 x, 100 degrees and 80 degrees. Find x.", do=[PT([72, 108, 100, 80], ["2x", "3x", "100°", "80°"], start=0), B("2x, 3x, 100°, 80°", x=80, y=160)]),
        dict(say="They add up to 360. 2 x plus 3 x plus 100 plus 80 equals 360.", do=[MATH("2x + 3x + 100 + 80 = 360", x=80, y=270)]),
        dict(say="Collect like terms: 5 x plus 180 equals 360. Subtract 180: 5 x equals 180.", do=[MATH("5x + 180 = 360", x=80, y=350), MATH("5x = 180", x=80, y=430, at=3.6)]),
        dict(say="Divide by 5. x equals 36.", do=[B("x = 36", x=80, y=520, color=GREEN)]),
        PAUSE("5.1-k3", "Your turn. A quadrilateral has three right angles. What is the fourth angle? Pause and work it out.", "A quadrilateral has three right angles. What is the fourth angle?"),
    ]),
    dict(kind="example", title="Check: three right angles", steps=[
        dict(say="Three right angles make 3 times 90, which is 270. 360 minus 270 is 90. The fourth angle is a right angle too. The shape is a rectangle.",
             do=[MATH("3 × 90 = 270", x=80, y=190), MATH("360 − 270 = 90°", x=80, y=280, at=3, color=GREEN), SHAPE([[0, 0], [6, 0], [6, 3.5], [0, 3.5]], ang=["90°", "90°", "90°", "?"], at=0.4)]),
    ]),
    dict(kind="example", title="A clock", steps=[
        dict(say="What is the smaller angle between the hands of a clock at 4 o'clock?", do=[FIG(660, 130, 560, 0, kind="clock", h=4, m=0), B("4 o'clock", x=80, y=170)]),
        dict(say="The 12 hour marks share 360 degrees. 360 divided by 12 is 30 degrees between each pair of marks.", do=[MATH("360 ÷ 12 = 30°", x=80, y=290)]),
        dict(say="From 12 to 4 is 4 marks. 4 times 30 is 120. The angle is 120 degrees.", do=[MATH("4 × 30 = 120", x=80, y=380), B("120°", x=80, y=470, color=GREEN, at=3.4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Three angles around a point are 150 degrees, 90 degrees, and a. Here is Leo's working. Which line goes wrong first?",
             do=LINES("Leo", "150°, 90° and a around a point", ["150 + 90 = 240", "a = 180 − 240", "a = −60"])),
        dict(say="Line 2 is wrong. Angles around a point add up to 360 degrees, not 180. And an angle cannot be negative.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="360 minus 240 is 120. So a is 120 degrees.", do=[B("a = 360 − 240 = 120°", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Why 360?", steps=[
        dict(say="Why are there 360 degrees in a full turn? The idea is thought to come from ancient Babylon, about 4,000 years ago. The Babylonians counted in sixties.",
             do=[E("🏛️", 90, 170, 100), T("Ancient Babylon counted in **sixties**", x=230, y=200)]),
        dict(say="360 is a very handy number. It can be divided exactly by 2, 3, 4, 5, 6, 8, 9, 10 and 12.", do=[T("360 ÷ 2, 3, 4, 5, 6, 8, 9, 10, 12 – all exact", x=230, y=310, color=BLUE)]),
        dict(say="Skateboarders use the same number. A full spin in the air is called a 360.", do=[E("🛹", 90, 420, 100), B("a full spin = a “360”", x=230, y=440, color=RED)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("5.1-k4", "One last question. 6 equal angles meet at a point. How big is each one? Pause the video and answer.", "6 equal angles meet at a point. How big is each?"),
        dict(say="360 divided by 6 is 60. Each angle is 60 degrees.", do=[MATH("360 ÷ 6 = 60", x=80, y=190), B("60°", x=80, y=300, color=GREEN, at=2.4), PT([60, 60, 60, 60, 60, 60], ["60°", "60°", "60°", "60°", "60°", "60°"], at=0.4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: angles around a point add up to 360 degrees.", do=[T("• Around a point: **360°**", x=80, y=170)]),
        dict(say="Angles in a quadrilateral add up to 360 degrees, because it is made of 2 triangles.", do=[T("• Quadrilateral: **360°** (2 triangles)", x=80, y=250)]),
        dict(say="Angles on a straight line, and in a triangle, add up to 180 degrees.", do=[T("• Straight line and triangle: **180°**", x=80, y=330)]),
        dict(say="Add the angles you know, subtract from the total, then check.", do=[T("• Add, subtract from the total, check", x=80, y=410)]),
    ]),
]

X4 = lambda labels, at=0, x=640, y=120, w=600: PT([40, 140, 40, 140], labels, x, y, w, at, start=20)
PAR = lambda labels, at=0, x=640, y=120, w=600: BIG(FIG(x, y, w, at, kind="parallel", labels=labels))

VIDEOS["5.2"] = [
    dict(kind="hook", title="Scissors", steps=[
        dict(say="Open a pair of scissors. The two blades cross, and they make 4 angles.", do=[E("✂️", 90, 170, 110), T("two blades cross → **4 angles**", x=240, y=205), X4(["40°", "?", "?", "?"], at=1.6)]),
        dict(say="Suppose you open the scissors so that one angle is 40 degrees.", do=[T("one angle is **40°**", x=240, y=300)]),
        PAUSE("5.2-k1", "What is the angle next to it? Pause the video and work it out.", "Scissors make an angle of 40°. What is the angle next to it?"),
    ]),
    dict(kind="hook", title="Next to 40°", steps=[
        dict(say="The 40 degree angle and the angle next to it sit on a straight line. So together they make 180 degrees.", do=[X4(["40°", "140°", "?", "?"]), T("on a straight line: **180°**", x=80, y=180)]),
        dict(say="180 minus 40 is 140. The angle next to it is 140 degrees.", do=[MATH("180 − 40 = 140°", x=80, y=290, color=GREEN)]),
        dict(say="And here is the surprise. The other two angles are 40 and 140 again. Let's see why.", do=[X4(["40°", "140°", "40°", "140°"], at=0.3), T("the others: **40°** and **140°** again", x=80, y=400, at=1)]),
    ]),
    dict(kind="recall", title="Straight line and triangle", steps=[
        dict(say="Remember two facts. Angles on a straight line add up to 180 degrees.", do=[B("straight line: 180°", x=80, y=170)]),
        dict(say="And the angles of a triangle add up to 180 degrees. If two angles are 55 and 75, the third is 180 minus 130, which is 50 degrees.",
             do=[B("triangle: 180°", x=80, y=280), MATH("180 − (55 + 75) = 50°", x=80, y=390, at=3.6, color=GREEN)]),
    ]),
    dict(kind="idea", title="Vertically opposite angles", steps=[
        dict(say="When two straight lines cross, we say they intersect. They make 4 angles. Call them a, b, c and d.", do=[X4(["a", "b", "c", "d"]), T("two lines **intersect**", x=80, y=170)]),
        dict(say="The angles opposite each other are equal. They are called vertically opposite angles. So a equals c, and b equals d.",
             do=[B("a = c  and  b = d", x=80, y=260, color=GREEN), T("**vertically opposite** angles are **equal**", x=80, y=350, at=2.6)]),
        dict(say="Why? a and b make a straight line, so a plus b is 180. b and c also make a straight line, so b plus c is 180. That means a and c must be equal.",
             do=[MATH("a + b = 180", x=80, y=440), MATH("b + c = 180", x=360, y=440, at=4), T("so a = c", x=640, y=448, color=BLUE, at=8)]),
        PAUSE("5.2-k2", "Your turn. Two lines cross, and one angle is 101 degrees. What is the angle next to it? Pause the video and try it.", "Two lines cross. One angle is 101°. What is the angle next to it?"),
    ]),
    dict(kind="idea", title="Check: next to 101°", steps=[
        dict(say="Angles next to each other on a straight line add up to 180. 180 minus 101 is 79 degrees.", do=[MATH("180 − 101 = 79°", x=80, y=200, color=GREEN), PT([101, 79, 101, 79], ["101°", "79°", "101°", "79°"], start=10, at=0.4)]),
    ]),
    dict(kind="idea", title="Perpendicular and parallel lines", steps=[
        dict(say="Lines that meet at 90 degrees are called perpendicular. All 4 angles are right angles.", do=[T("**Perpendicular**: lines that meet at 90°", x=80, y=160), PT([90, 90, 90, 90], ["90°", "90°", "90°", "90°"], x=880, y=80, w=360, start=0)]),
        dict(say="Parallel lines never meet. On a diagram, they are marked with arrows.", do=[T("**Parallel**: lines that never meet (marked with arrows)", x=80, y=240)]),
        dict(say="A line that crosses parallel lines is called a transversal. It makes 8 angles, but there are only 2 different sizes.",
             do=[PAR({"a": "65°", "b": "115°", "c": "65°", "d": "115°", "e": "65°", "f": "115°", "g": "65°", "h": "115°"}, x=30, y=290, w=540), T("a **transversal** makes 8 angles, only **2 sizes**", x=600, y=440)]),
        dict(say="Corresponding angles are in matching positions, and they are equal. Alternate angles are on opposite sides of the transversal, between the parallel lines, and they are equal too.",
             do=[T("**corresponding** angles are equal (F shape)", x=600, y=510, color=BLUE), T("**alternate** angles are equal (Z shape)", x=600, y=570, color=RED, at=5)]),
    ]),
    dict(kind="method", title="Angles where lines cross", steps=[
        dict(say="Here is the method. Step 1: mark the angles you know on the diagram.", do=[T("1. **Mark** the angles you know", x=80, y=170)]),
        dict(say="Step 2: use these facts. Vertically opposite angles are equal. A straight line is 180. Around a point is 360.", do=[T("2. opposite → **equal** · line → **180°** · point → **360°**", x=80, y=260)]),
        dict(say="Step 3: with parallel lines, corresponding angles and alternate angles are equal.", do=[T("3. Parallel lines: corresponding and alternate angles are **equal**", x=80, y=350)]),
        dict(say="Step 4: write the reason next to each answer.", do=[T("4. Give a **reason** for each answer", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="All four angles", steps=[
        dict(say="Two lines intersect. One angle is 118 degrees. Find the other three.", do=[PT([118, 62, 118, 62], ["118°", "?", "?", "?"], start=10), B("one angle: 118°", x=80, y=170)]),
        dict(say="The angle vertically opposite is equal, so it is 118 degrees.", do=[T("vertically opposite: **118°**", x=80, y=280)]),
        dict(say="The angle next to it is on a straight line. 180 minus 118 is 62 degrees.", do=[T("straight line: 180 − 118 = **62°**", x=80, y=360)]),
        dict(say="And the last angle is vertically opposite that one, so it is 62 degrees as well.", do=[T("vertically opposite: **62°**", x=80, y=440), PT([118, 62, 118, 62], ["118°", "62°", "118°", "62°"], start=10, at=0.6)]),
    ]),
    dict(kind="example", title="Using algebra", steps=[
        dict(say="Two vertically opposite angles are 3 x plus 10, and 70 degrees. Find x.", do=[B("3x + 10  and  70°", x=80, y=160)]),
        dict(say="Vertically opposite angles are equal. So 3 x plus 10 equals 70.", do=[MATH("3x + 10 = 70", x=80, y=270)]),
        dict(say="Subtract 10. 3 x equals 60. Divide by 3. x equals 20.", do=[MATH("3x = 60", x=80, y=360), B("x = 20", x=80, y=450, color=GREEN, at=2.8)]),
        PAUSE("5.2-k3", "Your turn. Two vertically opposite angles are 2 y, and 80 degrees. What is y? Pause and work it out.", "Two vertically opposite angles are 2y and 80°. What is y?"),
    ]),
    dict(kind="example", title="Check: 2y and 80°", steps=[
        dict(say="They are equal, so 2 y equals 80. Divide by 2. y equals 40.", do=[MATH("2y = 80", x=80, y=190), B("y = 40", x=80, y=300, color=GREEN, at=2.6)]),
    ]),
    dict(kind="example", title="Parallel lines", steps=[
        dict(say="A transversal crosses two parallel lines. One angle is 48 degrees.", do=[PAR({"a": "", "b": "", "c": "48°", "d": "", "e": "?", "f": "", "g": "", "h": ""}), B("one angle: 48°", x=80, y=170)]),
        dict(say="The alternate angle is equal. So it is also 48 degrees.", do=[T("alternate angle: **48°**", x=80, y=290)]),
        dict(say="The angle on a straight line with it is 180 minus 48, which is 132 degrees.", do=[T("on a straight line: 180 − 48 = **132°**", x=80, y=380)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Two lines cross. One angle is 35 degrees. Mia wants the angle vertically opposite it. Which line is wrong?",
             do=LINES("Mia", "the angle opposite 35°", ["Vertically opposite angles add up to 180°", "180 − 35 = 145°"])),
        dict(say="Line 1 is wrong. Vertically opposite angles are equal. It is the angles next to each other that add up to 180.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="So the vertically opposite angle is 35 degrees.", do=[B("vertically opposite = 35°", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Railway tracks", steps=[
        dict(say="Railway tracks are a famous example of parallel lines. On most of the world's railways, the two rails are exactly 1,435 millimetres apart.",
             do=[E("🛤️", 90, 170, 110), T("rails: **1 435 mm** apart, all the way", x=240, y=205)]),
        dict(say="If the rails were not parallel, the gap would change, and the train would come off the track.", do=[E("🚆", 90, 320, 100), T("not parallel → the train comes off!", x=240, y=350)]),
        dict(say="The wooden sleepers under the rails cross them at right angles. They are perpendicular to the rails.", do=[T("sleepers are **perpendicular** to the rails", x=240, y=470, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("5.2-k4", "One last question. Between two parallel lines, an angle is 57 degrees. What is its alternate angle? Pause the video and answer.", "What is the alternate angle to 57° between parallel lines?"),
        dict(say="Alternate angles are equal. So the alternate angle is 57 degrees.", do=[B("alternate angle = 57°", x=80, y=190, color=GREEN), PAR({"a": "", "b": "", "c": "57°", "d": "", "e": "57°", "f": "", "g": "", "h": ""}, at=0.4, y=260)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: vertically opposite angles are equal.", do=[T("• Vertically opposite angles are **equal**", x=80, y=170)]),
        dict(say="Angles on a straight line add up to 180 degrees. Around a point, 360.", do=[T("• Straight line 180°; around a point 360°", x=80, y=250)]),
        dict(say="Perpendicular lines meet at 90 degrees.", do=[T("• Perpendicular lines meet at 90°", x=80, y=330)]),
        dict(say="With parallel lines, corresponding angles and alternate angles are equal.", do=[T("• Parallel lines: corresponding and alternate angles are equal", x=80, y=410)]),
    ]),
]

RECT = [[0, 0], [7, 0], [7, 4], [0, 4]]
PARA = [[0, 0], [6, 0], [7.5, 3], [1.5, 3]]

VIDEOS["5.3"] = [
    dict(kind="hook", title="Marking out a garden bed", steps=[
        dict(say="A gardener wants a rectangular flower bed, 6 metres by 3 and a half metres. She has string, pegs and a tape measure.",
             do=[E("🌷", 90, 170, 100), T("a rectangle **6 m by 3.5 m**", x=230, y=200), SHAPE([[0, 0], [6, 0], [6, 3.5], [0, 3.5]], s=["6 m", "3.5 m", "", ""], at=2)]),
        dict(say="She measures the 4 sides correctly. But are the corners really right angles?", do=[T("are the corners really **90°**?", x=230, y=300)]),
        PAUSE("5.3-k1", "Which property guarantees that the corners are right angles? Pause the video and choose.", "Which property guarantees that the gardener's rectangle has right-angled corners?"),
    ]),
    dict(kind="hook", title="Measure the diagonals", steps=[
        dict(say="The answer is: the two diagonals are equal. A shape with the correct sides can still lean over, like a parallelogram.", do=[SHAPE(PARA, x=60, y=160, w=500), T("right sides, but leaning ✗", x=110, y=510, color=RED)]),
        dict(say="But when the two diagonals are the same length, the shape must be a rectangle, with 4 right angles.", do=[SHAPE(RECT, x=640, y=160, w=500, at=0.4), T("equal diagonals → a rectangle ✓", x=680, y=510, color=GREEN, at=1)]),
    ]),
    dict(kind="recall", title="Using a protractor", steps=[
        dict(say="Remember how to use a protractor. Put its centre on the vertex of the angle.", do=[E("📐", 90, 160, 100), T("1. Centre on the **vertex**", x=230, y=190)]),
        dict(say="Line up zero with one arm of the angle.", do=[T("2. Line **0°** up with one arm", x=230, y=280)]),
        dict(say="Then read from the scale that starts at zero. An acute angle must be less than 90 degrees, so if you read 130 and 50, choose 50.", do=[T("3. Read the scale that **starts at 0**", x=230, y=370), T("acute angle: 50°, not 130°", x=230, y=460, color=GREEN, at=4.4)]),
    ]),
    dict(kind="idea", title="Perpendicular and parallel lines", steps=[
        dict(say="To draw a line perpendicular to another line, use a set square. Put one edge along the line, and draw along the other edge.", do=[T("**Perpendicular**: one edge of a set square on the line, draw along the other", x=80, y=160, w=1000), PT([90, 90, 180], ["90°", "", ""], x=720, y=230, w=460, start=0, at=0.6)]),
        dict(say="You can also use a protractor. Put the centre on the point, and mark 90 degrees.", do=[T("or use a protractor: mark **90°**", x=80, y=280)]),
        dict(say="To draw parallel lines, slide the set square along a ruler, and draw a line at each position. The lines stay the same distance apart.",
             do=[T("**Parallel**: slide a set square along a ruler", x=80, y=380), T("parallel lines are marked with matching **arrows**", x=80, y=460, color=BLUE, at=4)]),
        PAUSE("5.3-k2", "Your turn. On a diagram, what do lines marked with matching arrows tell you? Pause the video and choose.", "Lines marked with matching arrows are …"),
    ]),
    dict(kind="idea", title="Check: matching arrows", steps=[
        dict(say="Matching arrows mean the lines are parallel. Small squares in a corner mean a right angle, and matching dashes mean equal lengths.",
             do=[T("arrows → **parallel**", x=80, y=190, color=GREEN), T("small square → **right angle**", x=80, y=280, at=2.6), T("dashes → **equal lengths**", x=80, y=370, at=4.6)]),
    ]),
    dict(kind="idea", title="Drawing quadrilaterals accurately", steps=[
        dict(say="To draw a quadrilateral accurately, draw one side first. Then use a protractor for each angle, and a ruler for each length.", do=[T("One side first, then **protractor** for angles, **ruler** for lengths", x=80, y=160)]),
        dict(say="Take this parallelogram. Draw the base, 6 centimetres long.", do=[SHAPE(PARA, x=620, y=210, w=580, s=["6 cm", "", "6 cm", ""], ang=["63°", "117°", "63°", "117°"]), T("1. base **6 cm**", x=80, y=260)]),
        dict(say="At the left end, measure an angle of 63 degrees. At the right end, measure 117 degrees.", do=[T("2. angles **63°** and **117°**", x=80, y=340)]),
        dict(say="Mark the sloping sides to the same length, and join the top. Notice that the two neighbouring angles add up to 180 degrees.", do=[T("3. mark the sides, join the top", x=80, y=420), MATH("63 + 117 = 180", x=80, y=500, at=4, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I draw a quadrilateral?", steps=[
        dict(say="Here is the method. Step 1: make a quick sketch, and label every length and angle you know.", do=[T("1. **Sketch** and label", x=80, y=170)]),
        dict(say="Step 2: draw the longest side you know with a ruler.", do=[T("2. Draw the longest known **side**", x=80, y=260)]),
        dict(say="Step 3: measure each angle at its ends with a protractor, and draw the next sides.", do=[T("3. Measure the **angles**; draw the next sides", x=80, y=350)]),
        dict(say="Step 4: mark the lengths, join up, and check your drawing by measuring.", do=[T("4. Mark lengths, join up, **check**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A rectangle", steps=[
        dict(say="Draw a rectangle 7 centimetres by 4 centimetres. First draw the side A B, 7 centimetres long.", do=[SHAPE(RECT, s=["7 cm", "4 cm", "7 cm", "4 cm"], ang=["90°", "90°", "90°", "90°"]), T("1. AB = **7 cm**", x=80, y=180)]),
        dict(say="At A and at B, draw lines perpendicular to A B.", do=[T("2. perpendicular lines at A and B", x=80, y=270)]),
        dict(say="Mark a point 4 centimetres up each line. Call the points D and C.", do=[T("3. mark D and C, **4 cm** up", x=80, y=360)]),
        dict(say="Join D to C. Check: D C should be 7 centimetres long, and the diagonals should be equal.", do=[T("4. join DC; check DC = 7 cm, diagonals equal", x=80, y=450, color=GREEN)]),
    ]),
    dict(kind="example", title="Checking a drawing", steps=[
        dict(say="Amir draws a parallelogram with an angle of 50 degrees. What should the other angles be?", do=[SHAPE([[0, 0], [5, 0], [7, 2.4], [2, 2.4]], ang=["50°", "?", "?", "?"]), B("one angle: 50°", x=80, y=170)]),
        dict(say="In a parallelogram, opposite angles are equal. So the opposite angle is 50 degrees.", do=[T("opposite angle: **50°**", x=80, y=290)]),
        dict(say="Neighbouring angles add up to 180 degrees. 180 minus 50 is 130. The other two angles are 130 degrees each.", do=[T("neighbours: 180 − 50 = **130°**", x=80, y=380), MATH("50 + 130 + 50 + 130 = 360", x=80, y=480, at=4.6, color=BLUE)]),
        PAUSE("5.3-k3", "Your turn. A parallelogram has an angle of 64 degrees. What is the angle next to it? Pause and work it out.", "A parallelogram has an angle of 64°. What is the angle next to it?"),
    ]),
    dict(kind="example", title="Check: next to 64°", steps=[
        dict(say="Neighbouring angles in a parallelogram add up to 180 degrees. 180 minus 64 is 116 degrees.", do=[MATH("180 − 64 = 116°", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Kim draws an angle of 40 degrees at point A. Which line goes wrong first?",
             do=LINES("Kim", "an angle of 40° at A", ["Centre on A, base line on 0°", "Read 40 on the scale that starts at 180", "Draw the line"])),
        dict(say="Line 2 is wrong. Kim read the wrong scale, so the angle she drew is really 140 degrees.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="Always use the scale that starts at zero on the arm of the angle. And check: 40 degrees is acute, so it must look smaller than a right angle.", do=[T("Use the scale that **starts at 0**. 40° must look **acute**.", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="The builder's 3-4-5 trick", steps=[
        dict(say="Builders need perfect right angles for walls and floors. Here is a trick they still use today.", do=[E("👷", 90, 170, 100), T("How do builders get a perfect **right angle**?", x=230, y=200)]),
        dict(say="They make a triangle with sides of 3, 4 and 5 units. For example, 3 metres, 4 metres and 5 metres.", do=[SHAPE([[0, 0], [4, 0], [0, 3]], x=660, y=220, w=520, s=["4 m", "5 m", "3 m"], ang=["90°", "", ""]), T("a triangle with sides **3, 4, 5**", x=230, y=310)]),
        dict(say="The corner between the 3 side and the 4 side is always exactly 90 degrees. No protractor needed.", do=[B("always 90°", x=230, y=420, color=GREEN)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("5.3-k4", "One last question. What is true about the angles of a kite? Pause the video and choose.", "A kite has …"),
        dict(say="A kite has one pair of equal opposite angles. It also has two pairs of equal sides next to each other.",
             do=[SHAPE([[0, 3], [2, 0], [4, 3], [2, 4.2]], x=660, y=130, w=520), T("one pair of **equal opposite angles**", x=80, y=200, color=GREEN), T("two pairs of equal neighbouring sides", x=80, y=300, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: perpendicular lines meet at 90 degrees, and parallel lines never meet.", do=[T("• Perpendicular: 90°. Parallel: never meet", x=80, y=170)]),
        dict(say="Use a set square or a protractor for perpendicular lines, and a sliding set square for parallel lines.", do=[T("• Set square or protractor; slide for parallels", x=80, y=250)]),
        dict(say="To draw a quadrilateral: sketch, draw one side, measure the angles, mark the lengths.", do=[T("• Sketch, one side, angles, lengths", x=80, y=330)]),
        dict(say="Check with what you know: equal diagonals, equal opposite angles, and neighbours that add up to 180.", do=[T("• Check with the shape's properties", x=80, y=410)]),
    ]),
]
