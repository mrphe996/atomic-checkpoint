# -*- coding: utf-8 -*-
"""Stage 9 · Unit 5 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u05 import PAR, SHAPE
from .s7_u08 import SVG, POLY, REG, DOT, LINE

VIDEOS = {}

VIDEOS["5.1"] = [
    dict(kind="hook", title="A roof truss", steps=[
        dict(say="A carpenter builds a roof truss. Two parallel beams are joined by a sloping strut, and one angle is marked 64 degrees. The truss also contains an isosceles triangle.",
             do=[E("🏠", 90, 170, 100), T("parallel beams · a strut at **64°** · an isosceles triangle", x=230, y=200), PAR({"a": "64°", "e": "?"}, at=2, x=760, w=460)]),
        PAUSE("5.1-k1", "Which facts will help to find the other angles: parallel-line and triangle facts, or only Pythagoras? Pause the video and choose.", "Useful facts include … parallel-line and triangle facts, or only Pythagoras?"),
    ]),
    dict(kind="hook", title="Angle facts", steps=[
        dict(say="Parallel-line facts and triangle facts. Pythagoras finds lengths, not angles.", do=[B("parallel-line and triangle facts", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Angle facts you know", steps=[
        dict(say="Remember: angles on a straight line add up to 180 degrees, and around a point to 360. Vertically opposite angles are equal. A triangle's angles add to 180, and a quadrilateral's to 360.",
             do=[T("line **180°** · point **360°** · vertically opposite **equal**", x=80, y=180), T("triangle **180°** · quadrilateral **360°**", x=80, y=270, at=8)]),
    ]),
    dict(kind="idea", title="Parallel lines", steps=[
        dict(say="Where a line crosses two parallel lines, corresponding angles are equal. They make an F shape.",
             do=[PAR({"a": "a", "c": "c", "e": "e", "f": "f"}, x=800, w=460), TBL(["Pair", "Shape", "Fact"], [["corresponding (a, e)", "F", "equal"], ["alternate (c, e)", "Z", "?"], ["co-interior (c, f)", "C", "add to 180°"]], y=180), ROW(0, 0.5)]),
        dict(say="Co-interior angles are between the lines, on the same side. They make a C shape, and they add up to 180 degrees.", do=[ROW(2, 0.4)]),
        PAUSE("5.1-k2", "Your turn. Alternate angles make a Z shape. Are they equal, or do they add up to 180 degrees? Pause and choose.", "Z-shaped pair: alternate – equal, or co-interior – sum 180°?"),
    ]),
    dict(kind="idea", title="Check: alternate", steps=[
        dict(say="Alternate angles are equal. Only co-interior angles add up to 180 degrees.", do=[B("alternate (Z) → equal", x=80, y=190, color=GREEN)]),
        dict(say="Real problems need a chain of facts. Write the reason for each step, like alternate angles, or angles in a triangle.", do=[T("a **chain** of facts, with a **reason** for each step", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I find an angle?", steps=[
        dict(say="Here is the method. Step 1: mark all the angles you know on the diagram.", do=[T("1. **Mark** what you know", x=80, y=170)]),
        dict(say="Step 2: look for parallel lines, triangles, straight lines and points.", do=[T("2. Look for **parallels**, triangles, lines", x=80, y=260)]),
        dict(say="Step 3: find one angle at a time, and give a reason each time.", do=[T("3. One angle at a time, with a **reason**", x=80, y=350)]),
        dict(say="Step 4: check that the angles add up where they should.", do=[T("4. **Check** the totals", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Two facts", steps=[
        dict(say="A transversal makes an angle of 72 degrees with a parallel line. The alternate angle, inside a triangle, is also 72 degrees. The triangle has another angle of 50 degrees.",
             do=[MATH("alternate angle = 72°", x=80, y=180)]),
        dict(say="So the third angle is 180 minus 72 minus 50, which is 58 degrees. Reason: angles in a triangle.", do=[B("180 − 72 − 50 = 58°", x=80, y=290, color=GREEN)]),
        PAUSE("5.1-k3", "Your turn. An isosceles triangle has a top angle of 40 degrees. What is each base angle? Pause and work it out.", "Isosceles apex 40°. Base angle?"),
    ]),
    dict(kind="example", title="Check: base angles", steps=[
        dict(say="The two base angles are equal. 180 minus 40 is 140, and half of 140 is 70 degrees.", do=[B("(180 − 40) ÷ 2 = 70°", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="example", title="A parallelogram", steps=[
        dict(say="A parallelogram has neighbouring angles of 3 X and 2 X plus 20. Neighbouring angles add up to 180. So 5 X plus 20 is 180, and X is 32. The angles are 96 and 84 degrees.",
             do=[MATH("3x + 2x + 20 = 180", x=80, y=180), MATH("5x = 160 → x = 32", x=80, y=270, at=7), B("96° and 84°", x=80, y=370, color=GREEN, at=10)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Two co-interior angles lie between parallel lines. One is 110 degrees. Sara finds the other. Which line is wrong?", do=LINES("Sara", "co-interior pair, one is 110°", ["they are equal, so the other is 110°"])),
        dict(say="Line 1 is wrong. Co-interior angles add up to 180 degrees.", do=[dict(a="cross", id="l1")]),
        dict(say="180 minus 110 is 70 degrees.", do=[B("180 − 110 = 70°", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Joinery", steps=[
        dict(say="Carpenters and surveyors use parallel-line angle facts every day, to cut joints that fit, and to lay out roads that cross railways.",
             do=[E("🪚", 90, 170, 100), T("cutting joints · laying out roads", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("5.1-k4", "One last question. Angles on a straight line are 2 Y plus 10, and 3 Y minus 5. Find Y. Pause the video and answer.", "Angles on a line 2y + 10 and 3y − 5. y?"),
        dict(say="They add up to 180. 5 Y plus 5 is 180, so 5 Y is 175, and Y is 35.", do=[B("5y + 5 = 180 → y = 35", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: corresponding angles, F, and alternate angles, Z, are equal.", do=[T("• Corresponding (F), alternate (Z): equal", x=80, y=170)]),
        dict(say="Co-interior angles, C, add up to 180 degrees.", do=[T("• Co-interior (C): add to 180°", x=80, y=250)]),
        dict(say="Chain the facts, one step at a time, with reasons.", do=[T("• Chain facts, with reasons", x=80, y=330)]),
        dict(say="The base angles of an isosceles triangle are equal.", do=[T("• Isosceles base angles are equal", x=80, y=410)]),
    ]),
]

VIDEOS["5.2"] = [
    dict(kind="hook", title="Octagon tiles", steps=[
        dict(say="A floor designer wants to use regular octagons for tiles. To see how they fit together, she needs the size of each angle inside an octagon.",
             do=[E("🔷", 90, 170, 100), SVG(POLY(REG(8)), 820, 140, w=340, at=1)]),
        PAUSE("5.2-k1", "To find the angle sum of an octagon, would you split it into triangles, or circles? Pause the video and choose.", "To find the angle sum, split into … triangles or circles?"),
    ]),
    dict(kind="hook", title="Triangles", steps=[
        dict(say="Triangles. We know that the angles in a triangle add up to 180 degrees.", do=[B("split into triangles", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Triangles and quadrilaterals", steps=[
        dict(say="Remember: a triangle's angles add up to 180 degrees. A quadrilateral splits into 2 triangles, so its angles add up to 360.", do=[MATH("triangle 180°   ·   quadrilateral 2 × 180 = 360°", x=80, y=190)]),
    ]),
    dict(kind="idea", title="The angle sum", steps=[
        dict(say="From one corner, draw all the diagonals. A polygon with N sides splits into N minus 2 triangles. So the angle sum is N minus 2, times 180 degrees.",
             do=[B("sum = (n − 2) × 180°", x=80, y=170, color=BLUE), TBL(["Polygon", "n", "Triangles", "Angle sum"], [["pentagon", "5", "3", "540°"], ["hexagon", "6", "4", "720°"]], y=280), ROW(0, 7), ROW(1, 8)]),
        PAUSE("5.2-k2", "Your turn. What is the angle sum of an octagon? Pause the video and try it.", "Octagon angle sum?"),
    ]),
    dict(kind="idea", title="Check: octagon", steps=[
        dict(say="An octagon has 8 sides, so it splits into 6 triangles. 6 times 180 is 1,080 degrees.", do=[B("6 × 180 = 1080°", x=80, y=190, color=GREEN)]),
        dict(say="In a regular polygon, every angle is the same. So each angle is the angle sum, divided by N.", do=[T("regular: each angle = **sum ÷ n**", x=80, y=300, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I find interior angles?", steps=[
        dict(say="Here is the method. Step 1: count the sides, N.", do=[T("1. Count the sides, **n**", x=80, y=170)]),
        dict(say="Step 2: the angle sum is N minus 2, times 180.", do=[T("2. Sum = **(n − 2) × 180°**", x=80, y=260)]),
        dict(say="Step 3: for a regular polygon, divide by N. For a missing angle, subtract the known angles.", do=[T("3. Regular: ÷ n · missing: **subtract**", x=80, y=350)]),
        dict(say="Step 4: check that your answer is sensible.", do=[T("4. **Check** it is sensible", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A missing angle", steps=[
        dict(say="A pentagon has angles of 100, 120, 95, 110 and X degrees. The sum is 540. The known angles add to 425, so X is 115 degrees.",
             do=[MATH("sum = 540°", x=80, y=180), MATH("100 + 120 + 95 + 110 = 425", x=80, y=270, at=5), B("x = 540 − 425 = 115°", x=80, y=370, color=GREEN, at=8)]),
        PAUSE("5.2-k3", "Your turn. What is each interior angle of a regular octagon? Pause and work it out.", "Regular octagon interior angle?"),
    ]),
    dict(kind="example", title="Check: 135°", steps=[
        dict(say="The angle sum is 1,080, and there are 8 equal angles. 1,080 divided by 8 is 135 degrees.", do=[B("1080 ÷ 8 = 135°", x=80, y=190, color=GREEN)]),
        dict(say="Two octagons meet with 270 degrees at a point. That leaves 90 degrees, so a small square fills each gap.", do=[MATH("135 + 135 = 270 → 90° gap: a square", x=80, y=300)]),
    ]),
    dict(kind="example", title="How many sides?", steps=[
        dict(say="The angles of a polygon add up to 2,520 degrees. How many sides? N minus 2, times 180, equals 2,520. So N minus 2 is 14, and N is 16.",
             do=[MATH("(n − 2) × 180 = 2520", x=80, y=180), B("n − 2 = 14 → n = 16", x=80, y=290, color=GREEN, at=8)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Omar finds the angle sum of a hexagon. Which line is wrong?", do=LINES("Omar", "angle sum of a hexagon", ["6 triangles × 180 = 1080°"])),
        dict(say="Line 1 is wrong. From one corner, a hexagon splits into 6 minus 2, which is 4 triangles.", do=[dict(a="cross", id="l1")]),
        dict(say="4 times 180 is 720 degrees.", do=[B("4 × 180 = 720°", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Honeycomb", steps=[
        dict(say="Bees build honeycomb from regular hexagons. Each angle is 120 degrees, so three hexagons meet exactly at a point, with no gaps.",
             do=[E("🐝", 90, 170, 100), MATH("3 × 120° = 360°", x=230, y=200), SVG(POLY(REG(6)), 860, 150, w=300)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("5.2-k4", "One last question. What is the angle sum of a decagon, with 10 sides? Pause the video and answer.", "Decagon angle sum?"),
        dict(say="10 minus 2 is 8 triangles. 8 times 180 is 1,440 degrees.", do=[B("8 × 180 = 1440°", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the angle sum is N minus 2, times 180 degrees.", do=[T("• Sum = (n − 2) × 180°", x=80, y=170)]),
        dict(say="Regular polygon: each angle is the sum divided by N.", do=[T("• Regular: each = sum ÷ n", x=80, y=250)]),
        dict(say="A missing angle is the sum minus the known angles.", do=[T("• Missing = sum − known", x=80, y=330)]),
        dict(say="Rearrange to find N.", do=[T("• Rearrange to find n", x=80, y=410)]),
    ]),
]

VIDEOS["5.3"] = [
    dict(kind="hook", title="A robot walk", steps=[
        dict(say="A robot vacuum cleaner walks around the edge of a room shaped like a regular hexagon. It turns at each corner, until it faces the way it started.",
             do=[E("🤖", 90, 170, 100), SVG(POLY(REG(6)), 820, 140, w=340, at=1)]),
        PAUSE("5.3-k1", "How far has it turned altogether, in degrees? Pause the video and work it out.", "Total turn?"),
    ]),
    dict(kind="hook", title="One full turn", steps=[
        dict(say="It ends up facing the same way, so it has turned through one full turn. That is 360 degrees.", do=[B("360°", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Angles on a line", steps=[
        dict(say="Remember: angles on a straight line add up to 180 degrees.", do=[MATH("angles on a line = 180°", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Exterior angles", steps=[
        dict(say="Extend one side at each corner. The exterior angle is between the extension and the next side. The interior and exterior angles add up to 180 degrees.",
             do=[T("interior + exterior = **180°**", x=80, y=170)]),
        dict(say="Walking all the way round any polygon, you turn through one full turn. So the exterior angles of any polygon add up to 360 degrees.", do=[B("exterior angles add to 360°", x=80, y=270, color=BLUE)]),
        PAUSE("5.3-k2", "Your turn. How much does the robot turn at each corner of the regular hexagon? Pause the video and try it.", "Each corner of a regular hexagon?"),
    ]),
    dict(kind="idea", title="Check: 60°", steps=[
        dict(say="360 shared between 6 equal corners is 60 degrees each. In a regular polygon, each exterior angle is 360 divided by N.", do=[B("360 ÷ 6 = 60°", x=80, y=190, color=GREEN), T("regular: exterior = **360 ÷ n**", x=80, y=300)]),
        dict(say="So the number of sides is 360 divided by the exterior angle.", do=[T("n = **360 ÷ exterior**", x=80, y=390, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I use exterior angles?", steps=[
        dict(say="Here is the method. Step 1: remember the exterior angles add up to 360 degrees.", do=[T("1. Exterior angles total **360°**", x=80, y=170)]),
        dict(say="Step 2: in a regular polygon, each one is 360 divided by N.", do=[T("2. Regular: each = **360 ÷ n**", x=80, y=260)]),
        dict(say="Step 3: the interior angle is 180 minus the exterior angle.", do=[T("3. Interior = **180 − exterior**", x=80, y=350)]),
        dict(say="Step 4: to find N, divide 360 by the exterior angle.", do=[T("4. n = 360 ÷ exterior", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Number of sides", steps=[
        dict(say="A regular polygon has exterior angles of 24 degrees. 360 divided by 24 is 15. It has 15 sides.", do=[MATH("360 ÷ 24 = 15", x=80, y=180), B("15 sides", x=80, y=290, color=GREEN)]),
        PAUSE("5.3-k3", "Your turn. What is the exterior angle of a regular 9-sided polygon? Pause and work it out.", "Regular 9-gon exterior?"),
    ]),
    dict(kind="example", title="Check: 40°", steps=[
        dict(say="360 divided by 9 is 40 degrees.", do=[B("360 ÷ 9 = 40°", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="example", title="Interior from exterior", steps=[
        dict(say="Find the interior angle of a regular 20-sided polygon. The exterior angle is 360 divided by 20, which is 18. The interior angle is 180 minus 18, which is 162 degrees.",
             do=[MATH("exterior = 360 ÷ 20 = 18°", x=80, y=180), B("interior = 180 − 18 = 162°", x=80, y=290, color=GREEN, at=7)]),
        dict(say="Can a regular polygon have exterior angles of 50 degrees? 360 divided by 50 is 7.2. That is not a whole number, so no.", do=[MATH("360 ÷ 50 = 7.2 → no", x=80, y=400, color=RED)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Nina finds the exterior angle sum of an octagon. Which line is wrong?", do=LINES("Nina", "exterior angle sum of an octagon", ["(8 − 2) × 180 = 1080°"])),
        dict(say="Line 1 is wrong. That is the interior angle sum.", do=[dict(a="cross", id="l1")]),
        dict(say="The exterior angles of every polygon add up to 360 degrees.", do=[B("360°", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Drawing with code", steps=[
        dict(say="Programmers draw regular polygons with turtle graphics. Move forward, then turn 360 divided by N degrees, and repeat N times.",
             do=[E("🐢", 90, 170, 100), MATH("repeat n: forward, turn 360 ÷ n", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("5.3-k4", "One last question. A regular polygon has exterior angles of 45 degrees. What is each interior angle? Pause the video and answer.", "Exterior 45°. Interior?"),
        dict(say="180 minus 45 is 135 degrees. It is a regular octagon.", do=[B("180 − 45 = 135°", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the exterior angles of any polygon add up to 360 degrees.", do=[T("• Exterior angles total 360°", x=80, y=170)]),
        dict(say="Regular: each is 360 divided by N.", do=[T("• Regular: 360 ÷ n each", x=80, y=250)]),
        dict(say="Interior plus exterior is 180 degrees.", do=[T("• Interior + exterior = 180°", x=80, y=330)]),
        dict(say="N is 360 divided by the exterior angle.", do=[T("• n = 360 ÷ exterior", x=80, y=410)]),
    ]),
]

VIDEOS["5.4"] = [
    dict(kind="hook", title="A logo", steps=[
        dict(say="A design student must draw a regular hexagon logo, with guide lines at 60, 30 and 45 degrees. She may only use a ruler and compasses.",
             do=[E("✏️", 90, 170, 100), T("hexagon · 60°, 30°, 45° · **ruler and compasses only**", x=230, y=200)]),
        PAUSE("5.4-k1", "Is a protractor needed, or not allowed? Pause the video and choose.", "A protractor is … needed, or not allowed?"),
    ]),
    dict(kind="hook", title="No protractor", steps=[
        dict(say="A protractor is not allowed. In a construction, you use compasses. Circles make exact equal lengths, and equal lengths make exact angles.", do=[B("no protractor – use compasses", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Bisectors", steps=[
        dict(say="Remember: an angle bisector cuts an angle in half. A perpendicular bisector meets a line at 90 degrees, through its midpoint.", do=[T("angle bisector: **half** · perpendicular bisector: **90°**, through the middle", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Constructing 60°", steps=[
        dict(say="Draw a line A B. Put the compasses on A, and draw an arc that crosses the line at C. Keep the same radius. Put the compasses on C, and draw an arc that crosses the first arc at D.",
             do=[T("arc from **A** → C · same radius, arc from **C** → D", x=80, y=170)]),
        dict(say="A C, A D and C D are all the same length. Triangle A C D is equilateral, so angle D A C is exactly 60 degrees.", do=[B("equilateral → 60°", x=80, y=270, color=BLUE)]),
        PAUSE("5.4-k2", "Your turn. If you bisect the 60 degree angle, what angle do you get? Pause the video and try it.", "Bisect 60° gives?"),
    ]),
    dict(kind="idea", title="Check: 30°", steps=[
        dict(say="Half of 60 is 30 degrees. For 45 degrees, construct a right angle with a perpendicular, then bisect it.", do=[B("60 ÷ 2 = 30°", x=80, y=190, color=GREEN), MATH("90° → bisect → 45°", x=80, y=300)]),
        dict(say="Always leave your construction arcs. They show your method.", do=[T("leave the **arcs** visible", x=80, y=400)]),
    ]),
    dict(kind="idea", title="Polygons in a circle", steps=[
        dict(say="For a regular hexagon, draw a circle. Keep the same radius, and step it round the circle, marking points. Join the points.",
             do=[SVG(POLY(REG(6), "#E8F1FF") + "".join(DOT(x, y) for x, y in REG(6)), 820, 140, w=340), T("step the **radius** round the circle", x=80, y=200)]),
        dict(say="For a square, draw two diameters at right angles. For an octagon, bisect the right angles between them.", do=[T("square: perpendicular diameters · octagon: bisect them", x=80, y=300)]),
        PAUSE("5.4-k3", "Your turn. Stepping the radius round a circle, how many points do you mark? Pause and work it out.", "Points stepped round a circle with the radius?"),
    ]),
    dict(kind="idea", title="Check: 6 points", steps=[
        dict(say="6 points. Each side of the hexagon is the same as the radius, because it makes 6 equilateral triangles at the centre.", do=[B("6 points", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I construct an angle?", steps=[
        dict(say="Here is the method. Step 1: 60 degrees comes from an equilateral triangle.", do=[T("1. **60°**: equilateral triangle", x=80, y=170)]),
        dict(say="Step 2: 90 degrees comes from a perpendicular bisector.", do=[T("2. **90°**: perpendicular", x=80, y=260)]),
        dict(say="Step 3: bisect to halve an angle: 30, 45, 15 degrees.", do=[T("3. **Bisect** to halve", x=80, y=350)]),
        dict(say="Step 4: keep the radius fixed, and leave the arcs.", do=[T("4. Same radius; **leave the arcs**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="120° and 15°", steps=[
        dict(say="To construct 120 degrees, construct 60 degrees on a straight line. The angle on the other side is 180 minus 60, which is 120.", do=[MATH("180 − 60 = 120°", x=80, y=180)]),
        dict(say="To construct 15 degrees, bisect 60 to get 30, then bisect again.", do=[MATH("60° → 30° → 15°", x=80, y=280)]),
        dict(say="A hexagon drawn in a circle of radius 5 centimetres has sides of 5 centimetres, so its perimeter is 30 centimetres.", do=[B("6 × 5 = 30 cm", x=80, y=380, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Dan constructs 60 degrees. Which line is wrong?", do=LINES("Dan", "construct 60°", ["arc from A with radius 4 cm", "arc from C with radius 6 cm"])),
        dict(say="Line 2 is wrong. The radius must stay the same, so that the triangle is equilateral.", do=[dict(a="cross", id="l2")]),
        dict(say="The arc from C must also have radius 4 centimetres.", do=[B("arc from C: radius 4 cm", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Before computers", steps=[
        dict(say="Architects and engineers used compass constructions for centuries. Today, design software uses exactly the same geometry.", do=[E("📐", 90, 170, 100), T("the same geometry in **design software**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("5.4-k4", "One last question. What angle do you get if you bisect 45 degrees? Pause the video and answer.", "Bisect 45°?"),
        dict(say="Half of 45 is 22.5 degrees.", do=[B("45 ÷ 2 = 22.5°", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: 60 degrees comes from an equilateral triangle.", do=[T("• 60° from an equilateral triangle", x=80, y=170)]),
        dict(say="30 and 45 degrees come from bisecting 60 and 90.", do=[T("• 30°, 45°: bisect 60°, 90°", x=80, y=250)]),
        dict(say="For a hexagon, step the radius round a circle.", do=[T("• Hexagon: step the radius round", x=80, y=330)]),
        dict(say="Squares and octagons come from perpendicular diameters.", do=[T("• Square, octagon: perpendicular diameters", x=80, y=410)]),
    ]),
]

VIDEOS["5.5"] = [
    dict(kind="hook", title="A ladder", steps=[
        dict(say="A 5 metre ladder leans against a wall. Its foot is 1.4 metres from the wall. The wall and the ground make a right angle.",
             do=[E("🪜", 90, 170, 100), T("ladder **5 m** · foot **1.4 m** from the wall", x=230, y=200)]),
        PAUSE("5.5-k1", "How high up the wall does the ladder reach? Pause the video and work it out.", "Height (m)?"),
    ]),
    dict(kind="hook", title="4.8 m", steps=[
        dict(say="Height squared is 5 squared minus 1.4 squared. That is 25 minus 1.96, which is 23.04. The square root of 23.04 is 4.8 metres.",
             do=[MATH("h² = 5² − 1.4² = 25 − 1.96 = 23.04", x=80, y=190), B("h = √23.04 = 4.8 m", x=80, y=300, color=GREEN, at=8)]),
        dict(say="This uses Pythagoras' theorem.", do=[T("→ **Pythagoras' theorem**", x=80, y=400, color=BLUE)]),
    ]),
    dict(kind="recall", title="Squares and roots", steps=[
        dict(say="Remember: 6 squared is 36, and the square root of 49 is 7.", do=[MATH("6² = 36   ·   √49 = 7", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Pythagoras' theorem", steps=[
        dict(say="In a right-angled triangle, the longest side is the hypotenuse, C. Call the other sides A and B.",
             do=[SHAPE([[0, 0], [4, 0], [0, 3]], x=760, y=120, w=440, s=["a = 4", "c = 5", "b = 3"], right=[0]), T("the longest side: the **hypotenuse**, c", x=80, y=180)]),
        dict(say="Pythagoras' theorem says: A squared plus B squared equals C squared. Check with 3, 4 and 5: 9 plus 16 is 25.", do=[B("a² + b² = c²", x=80, y=280, color=BLUE), MATH("9 + 16 = 25 ✓", x=80, y=380, at=6)]),
        PAUSE("5.5-k2", "Your turn. Where is the hypotenuse: opposite the right angle, or is it the shortest side? Pause the video and choose.", "The hypotenuse is …"),
    ]),
    dict(kind="idea", title="Check: hypotenuse", steps=[
        dict(say="The hypotenuse is opposite the right angle. It is always the longest side.", do=[B("opposite the right angle – the longest side", x=80, y=190, color=GREEN)]),
        dict(say="To find a shorter side, rearrange: A squared equals C squared minus B squared.", do=[MATH("a² = c² − b²", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I use Pythagoras?", steps=[
        dict(say="Here is the method. Step 1: find the hypotenuse: the side opposite the right angle.", do=[T("1. Find the **hypotenuse**", x=80, y=170)]),
        dict(say="Step 2: square the sides you know.", do=[T("2. **Square** the known sides", x=80, y=260)]),
        dict(say="Step 3: for the hypotenuse, add. For a shorter side, subtract.", do=[T("3. Hypotenuse: **add** · shorter side: **subtract**", x=80, y=350)]),
        dict(say="Step 4: take the square root, and check the hypotenuse is the longest.", do=[T("4. **Square root**; check", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="The hypotenuse", steps=[
        dict(say="A right-angled triangle has sides of 5 and 12 centimetres. 25 plus 144 is 169. The square root of 169 is 13 centimetres.",
             do=[MATH("5² + 12² = 25 + 144 = 169", x=80, y=180), B("√169 = 13 cm", x=80, y=290, color=GREEN, at=7)]),
        PAUSE("5.5-k3", "Your turn. The two shorter sides are 9 and 12. Find the hypotenuse. Pause and work it out.", "Sides 9 and 12. Hypotenuse?"),
    ]),
    dict(kind="example", title="Check: 9 and 12", steps=[
        dict(say="81 plus 144 is 225. The square root of 225 is 15.", do=[B("√(81 + 144) = √225 = 15", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="example", title="A shorter side", steps=[
        dict(say="The hypotenuse is 17 metres, and one side is 8 metres. Subtract: 289 minus 64 is 225. The square root is 15 metres.",
             do=[MATH("17² − 8² = 289 − 64 = 225", x=80, y=180), B("√225 = 15 m", x=80, y=290, color=GREEN, at=7)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="The hypotenuse is 13 centimetres, and one side is 5 centimetres. Lily finds the other side. Which line is wrong?", do=LINES("Lily", "hypotenuse 13, side 5", ["13² + 5² = 194", "√194 ≈ 13.9 cm"])),
        dict(say="Line 1 is wrong. For a shorter side, subtract. Her answer is longer than the hypotenuse, which is impossible.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="169 minus 25 is 144. The square root is 12 centimetres.", do=[B("169 − 25 = 144 → 12 cm", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="The 3-4-5 rule", steps=[
        dict(say="Builders use the 3 4 5 rule. If a corner has sides of 3 metres and 4 metres, and the diagonal is exactly 5 metres, the corner is a perfect right angle.",
             do=[E("👷", 90, 170, 100), T("3, 4, 5 → a perfect **right angle**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("5.5-k4", "One last question. Is a triangle with sides 5, 6 and 8 right-angled? Pause the video and choose.", "5, 6, 8 is right-angled?"),
        dict(say="25 plus 36 is 61. But 8 squared is 64. They are not equal, so it is not right-angled.", do=[B("25 + 36 = 61 ≠ 64 → No", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: A squared plus B squared equals C squared, where C is the hypotenuse.", do=[T("• a² + b² = c²", x=80, y=170)]),
        dict(say="For the hypotenuse, add. For a shorter side, subtract.", do=[T("• Hypotenuse add · shorter side subtract", x=80, y=250)]),
        dict(say="The hypotenuse is the longest side.", do=[T("• The hypotenuse is the longest", x=80, y=330)]),
        dict(say="If A squared plus B squared equals C squared, the angle is 90 degrees.", do=[T("• a² + b² = c² → right angle", x=80, y=410)]),
    ]),
]
