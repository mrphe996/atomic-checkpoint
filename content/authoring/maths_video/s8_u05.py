# -*- coding: utf-8 -*-
"""Stage 8 · Unit 5 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u05 import PAR
from .s7_u08 import SVG, POLY, DASH, LINE, DOT, TXT, INK

# parallel-lines figure: a, c, e, g are the acute angles; b, d, f, h the obtuse ones.
# corresponding a–e, b–f, c–g, d–h · alternate c–e, d–f · co-interior c–f, d–e
ACUTE, OBT = "#1F9D61", "#D64545"
ARC = lambda cx, cy, r, x1, y1, x2, y2, c=BLUE, sweep=0: f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 {sweep} {x2:.1f} {y2:.1f}" fill="none" stroke="{c}" stroke-width="3.5"/>'

# a triangle with its base extended at B: A(30,240) B(200,240) C(120,70)
EXT = lambda a, c, i, e, ec=BLUE: (POLY([(30, 240), (200, 240), (120, 70)]) + DASH(200, 240, 305, 240, INK) +
    ARC(200, 240, 42, 242, 240, 182.1, 202.0, ec) + TXT(70, 228, a) + TXT(122, 122, c) + TXT(178, 228, i) + TXT(250, 214, e, ec))

VIDEOS = {}

VIDEOS["5.1"] = [
    dict(kind="hook", title="A railway crossing", steps=[
        dict(say="Two straight rails are parallel. A road crosses them at an angle. It makes an angle of 58 degrees with the first rail.",
             do=[E("🛤️", 90, 170, 100), T("road meets rail 1 at **58°**", x=230, y=200), PAR({"a": "58°", "e": "?"}, at=1)]),
        PAUSE("5.1-k1", "What is the matching angle at the second rail? Pause the video and work it out.", "The road makes 58° with the first rail. The corresponding angle at the second rail?"),
    ]),
    dict(kind="hook", title="The same at both rails", steps=[
        dict(say="The road crosses both rails in the same direction. So the angle in the matching position at the second rail is also 58 degrees.",
             do=[PAR({"a": "58°", "e": "58°"}), B("58°", x=80, y=200, color=GREEN)]),
        dict(say="These are called corresponding angles. Let's see all the angle facts for parallel lines.", do=[T("**corresponding** angles", x=80, y=300)]),
    ]),
    dict(kind="recall", title="Two facts you know", steps=[
        dict(say="Remember: when two lines cross, vertically opposite angles are equal. And angles on a straight line add up to 180 degrees.",
             do=[T("vertically opposite angles are **equal**", x=80, y=170), T("angles on a straight line add up to **180°**", x=80, y=250)]),
        dict(say="So if one angle is 58 degrees, the angle next to it is 180 minus 58, which is 122 degrees.", do=[MATH("180 − 58 = 122°", x=80, y=350, color=GREEN)]),
    ]),
    dict(kind="idea", title="Corresponding, alternate, co-interior", steps=[
        dict(say="A transversal crosses two parallel lines and makes 8 angles. Angles in matching positions are corresponding angles. They are equal. Look for an F shape.",
             do=[PAR({"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h"}, x=800, w=460),
                 TBL(["Pair", "Shape", "Fact"], [["corresponding (a, e)", "F", "equal"], ["alternate (c, e)", "Z", "equal"], ["co-interior (c, f)", "C", "add to 180°"]], y=180), ROW(0, 0.5)]),
        dict(say="Alternate angles are between the parallel lines, on opposite sides of the transversal. They are equal too. Look for a Z shape.", do=[ROW(1, 0.4)]),
        dict(say="Co-interior angles are between the lines, on the same side. They are not equal. They add up to 180 degrees. Look for a C shape.", do=[ROW(2, 0.4)]),
        PAUSE("5.1-k2", "Your turn. What does a Z shape show? Pause the video and choose.", "A Z shape shows …"),
    ]),
    dict(kind="idea", title="Check: a Z shape", steps=[
        dict(say="A Z shape shows alternate angles. They are equal.", do=[B("Z → alternate angles", x=80, y=190, color=GREEN), PAR({"c": "64°", "e": "64°"}, at=0.4)]),
        dict(say="The facts also work backwards. If corresponding or alternate angles are equal, then the lines are parallel. Always give a reason for each angle.",
             do=[T("equal corresponding or alternate angles → lines **are** parallel", x=80, y=300), T("always give a **reason**", x=80, y=380, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I find angles with parallel lines?", steps=[
        dict(say="Here is the method. Step 1: mark the parallel lines and the transversal.", do=[T("1. Mark the **parallel lines** and the **transversal**", x=80, y=170)]),
        dict(say="Step 2: start from a known angle. Look for an F, Z or C shape that links it to the angle you want.", do=[T("2. Look for an **F**, **Z** or **C** shape", x=80, y=260)]),
        dict(say="Step 3: corresponding and alternate angles are equal. Co-interior angles add up to 180.", do=[T("3. F, Z → **equal** · C → **180°**", x=80, y=350)]),
        dict(say="Step 4: write a reason next to every angle.", do=[T("4. Write a **reason** for every angle", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A co-interior angle", steps=[
        dict(say="Parallel lines are cut by a transversal. One angle is 58 degrees. Find its co-interior angle.", do=[PAR({"c": "58°", "f": "?"}), B("co-interior to 58°", x=80, y=170)]),
        dict(say="Co-interior angles add up to 180 degrees. 180 minus 58 is 122 degrees.", do=[MATH("180 − 58 = 122°", x=80, y=280, color=GREEN), T("reason: co-interior angles add to 180°", x=80, y=370)]),
    ]),
    dict(kind="example", title="Using algebra", steps=[
        dict(say="Two alternate angles are 3 x plus 15, and 5 x minus 25. Find x.", do=[MATH("3x + 15  and  5x − 25", x=80, y=170)]),
        dict(say="Alternate angles are equal. So 3 x plus 15 equals 5 x minus 25. Subtract 3 x, and add 25: 40 equals 2 x. So x equals 20.",
             do=[MATH("3x + 15 = 5x − 25", x=80, y=260), MATH("40 = 2x", x=80, y=340, at=5), B("x = 20", x=80, y=430, color=GREEN, at=7)]),
        dict(say="Check: 3 times 20 plus 15 is 75, and 5 times 20 minus 25 is 75. Both angles are 75 degrees.", do=[T("both angles **75°** ✓", x=420, y=440)]),
        PAUSE("5.1-k3", "Your turn. Alternate angles are 2 x plus 10, and 70 degrees. Find x. Pause and work it out.", "Alternate angles 2x + 10 and 70. x = ?"),
    ]),
    dict(kind="example", title="Check: 2x + 10 = 70", steps=[
        dict(say="Alternate angles are equal. 2 x plus 10 equals 70. Subtract 10: 2 x equals 60. So x equals 30.", do=[MATH("2x + 10 = 70", x=80, y=190), MATH("2x = 60", x=80, y=280, at=3), B("x = 30", x=80, y=380, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Is it parallel?", steps=[
        dict(say="Two lines are cut by a transversal. The corresponding angles are 72 degrees and 74 degrees. Are the lines parallel?", do=[MATH("72° and 74°", x=80, y=170)]),
        dict(say="For parallel lines, corresponding angles must be equal. 72 is not equal to 74, so the lines are not parallel. They will meet somewhere.", do=[MATH("72 ≠ 74", x=80, y=260), B("not parallel", x=80, y=360, color=RED, at=3)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Parallel lines have an angle of 110 degrees, and its co-interior partner, y. Here is Eli's working. Which line goes wrong first?",
             do=LINES("Eli", "110° and its co-interior partner y", ["co-interior angles are equal", "y = 110°"])),
        dict(say="Line 1 is wrong. Co-interior angles add up to 180 degrees. Only corresponding and alternate angles are equal.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="y equals 180 minus 110, which is 70 degrees.", do=[B("y = 180 − 110 = 70°", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Parking bays", steps=[
        dict(say="Car parks often paint bays at an angle, not straight across. The lines of the bays are all parallel.", do=[E("🅿️", 90, 170, 100), T("angled bays: all the lines are **parallel**", x=230, y=200)]),
        dict(say="If every bay meets the kerb at 60 degrees, the painters only need to set the angle once. Corresponding angles do the rest.", do=[T("every bay meets the kerb at **60°**", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("5.1-k4", "One last question. What is the co-interior angle to 95 degrees? Pause the video and answer.", "Quick check: co-interior to 95°?"),
        dict(say="Co-interior angles add up to 180. 180 minus 95 is 85 degrees.", do=[B("180 − 95 = 85°", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: corresponding angles, in an F shape, are equal.", do=[T("• Corresponding angles (**F**) are equal", x=80, y=170)]),
        dict(say="Alternate angles, in a Z shape, are equal.", do=[T("• Alternate angles (**Z**) are equal", x=80, y=250)]),
        dict(say="Co-interior angles, in a C shape, add up to 180 degrees.", do=[T("• Co-interior angles (**C**) add to 180°", x=80, y=330)]),
        dict(say="Equal corresponding or alternate angles prove that lines are parallel. Always give reasons.", do=[T("• Equal F or Z angles prove lines are parallel; give reasons", x=80, y=410)]),
    ]),
]

VIDEOS["5.2"] = [
    dict(kind="hook", title="A roof truss", steps=[
        dict(say="A carpenter builds a triangular roof frame, and extends the bottom beam past one corner. The inside angles at the other two corners are 35 degrees and 75 degrees.",
             do=[E("🏠", 90, 170, 100), T("inside angles **35°** and **75°**", x=230, y=200), SVG(EXT("35°", "75°", "", "?"), 800, 120, w=420, at=1)]),
        PAUSE("5.2-k1", "What is the angle outside, between the roof and the extended beam? Pause the video and work it out.", "Outside angle for interior 35° and 75°?"),
    ]),
    dict(kind="hook", title="The outside angle", steps=[
        dict(say="The third inside angle is 180 minus 35 minus 75, which is 70 degrees. The outside angle is on a straight line with it, so it is 180 minus 70, which is 110 degrees.",
             do=[SVG(EXT("35°", "75°", "70°", "110°"), 800, 120, w=420), MATH("180 − 35 − 75 = 70", x=80, y=190), MATH("180 − 70 = 110°", x=80, y=280, at=6, color=GREEN)]),
        dict(say="But look: 35 plus 75 is also 110. Is that a shortcut?", do=[MATH("35 + 75 = 110 !", x=80, y=380, color=BLUE)]),
    ]),
    dict(kind="recall", title="Angles in a triangle", steps=[
        dict(say="Remember: the angles inside a triangle add up to 180 degrees. If two angles are 35 and 75, the third is 70 degrees.", do=[B("triangle: 180°", x=80, y=180), MATH("180 − (35 + 75) = 70°", x=80, y=290)]),
    ]),
    dict(kind="idea", title="Exterior angles", steps=[
        dict(say="If you extend one side of a triangle, the angle between the extension and the next side is called an exterior angle.",
             do=[SVG(EXT("a", "b", "c", "e"), 800, 120, w=420), T("**exterior angle** e: between a side and an extended side", x=80, y=170)]),
        dict(say="The interior angles a, b and c add up to 180. And c plus the exterior angle e also make 180, because they are on a straight line.",
             do=[MATH("a + b + c = 180", x=80, y=260), MATH("c + e = 180", x=80, y=340, at=5)]),
        dict(say="So the exterior angle equals a plus b. The exterior angle is the sum of the two interior angles opposite it.", do=[B("e = a + b", x=80, y=440, color=GREEN)]),
        PAUSE("5.2-k2", "Your turn. The two opposite interior angles are 20 degrees and 90 degrees. What is the exterior angle? Pause the video and try it.", "Opposite interior angles 20° and 90°. Exterior?"),
    ]),
    dict(kind="idea", title="Check: 20° and 90°", steps=[
        dict(say="The exterior angle is the sum of the two opposite interior angles. 20 plus 90 is 110 degrees.", do=[B("20 + 90 = 110°", x=80, y=200, color=GREEN)]),
        dict(say="Remember: the exterior angle and the interior angle next to it add up to 180, not the same value.", do=[T("exterior + the interior angle **next to it** = 180°", x=80, y=310)]),
    ]),
    dict(kind="method", title="How do I use the exterior angle fact?", steps=[
        dict(say="Here is the method. Step 1: find the exterior angle. It is between a side and an extended side.", do=[T("1. Find the **exterior** angle", x=80, y=170)]),
        dict(say="Step 2: find the two interior angles that are not next to it.", do=[T("2. Find the two interior angles **not next to it**", x=80, y=260)]),
        dict(say="Step 3: the exterior angle equals their sum. Or subtract to find a missing interior angle.", do=[T("3. Exterior = their **sum** (or subtract)", x=80, y=350)]),
        dict(say="Step 4: check that the three interior angles add up to 180.", do=[T("4. **Check**: interior angles add to 180°", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A missing interior angle", steps=[
        dict(say="An exterior angle is 140 degrees. One opposite interior angle is 85 degrees. Find the other one.", do=[SVG(EXT("85°", "?", "", "140°"), 800, 120, w=420), MATH("140 = 85 + x", x=80, y=190)]),
        dict(say="140 minus 85 is 55. The other angle is 55 degrees.", do=[B("x = 55°", x=80, y=290, color=GREEN)]),
        PAUSE("5.2-k3", "Your turn. An exterior angle is 150 degrees, and one opposite interior angle is 72 degrees. Find the other. Pause and work it out.", "Exterior 150°, opposite interior 72°. Other?"),
    ]),
    dict(kind="example", title="Check: 150° and 72°", steps=[
        dict(say="150 equals 72 plus the other angle. 150 minus 72 is 78 degrees.", do=[MATH("150 − 72 = 78°", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Using algebra", steps=[
        dict(say="The opposite interior angles are 2 x and 3 x. The exterior angle is 125 degrees. Find x.", do=[SVG(EXT("2x", "3x", "", "125°"), 800, 120, w=420), MATH("2x + 3x = 125", x=80, y=190)]),
        dict(say="5 x equals 125, so x equals 25. The angles are 50 degrees and 75 degrees.", do=[MATH("5x = 125", x=80, y=280), B("x = 25", x=80, y=370, color=GREEN, at=2)]),
    ]),
    dict(kind="example", title="An isosceles triangle", steps=[
        dict(say="An isosceles triangle has a top angle of 40 degrees. Find the exterior angle at a base corner.", do=[MATH("top angle 40°", x=80, y=170)]),
        dict(say="The two base angles are equal: 180 minus 40 is 140, and half of 140 is 70. The exterior angle at a base corner is 40 plus 70, which is 110 degrees.",
             do=[MATH("(180 − 40) ÷ 2 = 70°", x=80, y=260), B("40 + 70 = 110°", x=80, y=360, color=GREEN, at=6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="In triangle A B C, angle A is 50 degrees and angle B is 60 degrees. Ruby finds the exterior angle at C. Which line goes wrong first?",
             do=LINES("Ruby", "the exterior angle at C (A = 50°, B = 60°)", ["angle C = 70°", "exterior angle = angle C = 70°"])),
        dict(say="Line 2 is wrong. The exterior angle and angle C are on a straight line, so they add up to 180. They are not equal.", do=[dict(a="cross", id="l2")]),
        dict(say="The exterior angle is 50 plus 60, which is 110 degrees.", do=[B("exterior = 50 + 60 = 110°", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Turning at a corner", steps=[
        dict(say="A cyclist rides round a triangular route. At each corner she turns through an exterior angle.", do=[E("🚴", 90, 170, 100), T("at each corner she turns through an **exterior** angle", x=230, y=200)]),
        dict(say="By the time she is back at the start, she has turned all the way round once. So the three exterior angles of any triangle add up to 360 degrees.", do=[B("3 exterior angles = 360°", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("5.2-k4", "One last question. What is the exterior angle of an equilateral triangle? Pause the video and answer.", "Quick check: equilateral triangle exterior angle?"),
        dict(say="Each interior angle is 60 degrees. The exterior angle is 60 plus 60, which is 120 degrees. And 3 times 120 is 360.", do=[MATH("60 + 60 = 120°", x=80, y=200, color=GREEN), T("3 × 120 = 360 ✓", x=80, y=300, at=5)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: an exterior angle is made by extending one side of a triangle.", do=[T("• Extend a side → an **exterior** angle", x=80, y=170)]),
        dict(say="The exterior angle equals the sum of the two interior angles opposite it.", do=[T("• Exterior = sum of the two **opposite** interior angles", x=80, y=250)]),
        dict(say="The exterior angle and the interior angle next to it add up to 180 degrees.", do=[T("• Exterior + the interior next to it = 180°", x=80, y=330)]),
        dict(say="You can prove it with the angle sum of a triangle, and a straight line.", do=[T("• Prove it: triangle 180° + straight line 180°", x=80, y=410)]),
    ]),
]

# constructions in the 320 × 320 box: A(60,200) B(260,200); arcs of radius 130 meet at (160, 200 ± 83.1)
AB = LINE(60, 200, 260, 200) + DOT(60, 200, INK, 6) + DOT(260, 200, INK, 6) + TXT(46, 230, "A") + TXT(274, 230, "B")
ARCS_A = ARC(60, 200, 130, 143.6, 100.4, 143.6, 299.6, RED, 1)
ARCS_B = ARC(260, 200, 130, 176.4, 100.4, 176.4, 299.6, RED, 0)
PBIS = DASH(160, 60, 160, 315, GREEN) + DOT(160, 116.9, GREEN, 6) + DOT(160, 283.1, GREEN, 6)
# angle at O(50,260): arms to (300,260) and along 50° ; bisector at 25°
ANG = LINE(50, 260, 300, 260) + LINE(50, 260, 210.7, 68.5) + DOT(50, 260, INK, 6) + TXT(36, 290, "O")
ANG1 = ARC(50, 260, 120, 170, 260, 127.1, 168.1, RED, 0)
ANG2 = DOT(170, 260, RED, 6) + DOT(127.1, 168.1, RED, 6) + ARC(0, 0, 90, 189.8, 172.2, 237.6, 200.6, RED, 1) + ARC(0, 0, 90, 216.1, 154.5, 207.1, 209.3, RED, 1)
ABIS = DASH(50, 260, 295, 145.8, GREEN)

VIDEOS["5.3"] = [
    dict(kind="hook", title="A fair place for a well", steps=[
        dict(say="Two villages want to dig a new well. It must be exactly the same distance from both villages.", do=[E("🏘️", 90, 170, 100), T("a well **equally far** from both villages", x=230, y=200)]),
        dict(say="One point that works is halfway between them. But there are many more. Where are all the points that are the same distance from two places?", do=[T("where are **all** such points?", x=230, y=300)]),
        PAUSE("5.3-k1", "What shape do the points that are equally far from two villages make? Pause the video and choose.", "Points equally far from two villages form …"),
    ]),
    dict(kind="hook", title="A straight line", steps=[
        dict(say="They make a straight line. It goes through the halfway point, at right angles to the line joining the villages. It is called the perpendicular bisector.",
             do=[SVG(AB + PBIS, 760, 110, w=460), B("perpendicular bisector", x=80, y=200, color=GREEN)]),
        dict(say="Bisector means it cuts the line in half. Perpendicular means it meets it at 90 degrees.", do=[T("**bisect** = cut in half · **perpendicular** = at 90°", x=80, y=310)]),
    ]),
    dict(kind="recall", title="Drawing with compasses", steps=[
        dict(say="Remember: compasses draw arcs. Every point on an arc is the same distance from its centre. That distance is the radius.",
             do=[E("📏", 90, 170, 100), T("every point on an arc is the **same distance** from the centre", x=230, y=200)]),
    ]),
    dict(kind="idea", title="Constructing triangles", steps=[
        dict(say="You can construct a triangle accurately from different starting facts. With three sides, called S S S, draw one side. Then draw arcs from each end with the other two lengths.",
             do=[TBL(["Given", "Method"], [["SSS: 3 sides", "draw one side; arcs from each end; join to where they cross"], ["SAS: 2 sides, angle between", "draw a side, measure the angle, measure the second side"], ["ASA: 2 angles, side between", "draw the side, measure both angles, extend the arms"], ["RHS: right angle, hypotenuse, side", "draw the right angle, then an arc for the hypotenuse"]], y=170), ROW(0, 0.4)]),
        dict(say="With two sides and the angle between them, S A S, use a ruler and a protractor. With two angles and the side between them, A S A, measure both angles.", do=[ROW(1, 0.3), ROW(2, 4.6)]),
        dict(say="And for a right-angled triangle, R H S, draw the right angle, then use an arc for the longest side, the hypotenuse.", do=[ROW(3, 0.3)]),
        PAUSE("5.3-k2", "Your turn. You are given three sides. Which kind of construction is that? Pause the video and choose.", "Three sides given: …"),
    ]),
    dict(kind="idea", title="Check: three sides", steps=[
        dict(say="Three sides is S S S: side, side, side.", do=[B("SSS", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="The perpendicular bisector", steps=[
        dict(say="To construct the perpendicular bisector of A B, open the compasses to more than half of A B. Draw arcs from A, above and below the line.",
             do=[SVG(AB, 760, 110, w=460), SVG(ARCS_A, 760, 110, w=460, at=3)]),
        dict(say="Keep the same width. Draw arcs from B, so they cross the first arcs.", do=[SVG(ARCS_B, 760, 110, w=460)]),
        dict(say="Join the two crossing points. Every point on this line is the same distance from A and from B.", do=[SVG(PBIS, 760, 110, w=460), T("same distance from **A** and **B**", x=80, y=200, color=GREEN, at=2)]),
    ]),
    dict(kind="idea", title="The angle bisector", steps=[
        dict(say="To bisect an angle, draw an arc from the vertex, O, that crosses both arms.", do=[SVG(ANG, 760, 110, w=460), SVG(ANG1, 760, 110, w=460, at=2.4)]),
        dict(say="From the two crossing points, draw two equal arcs that cross each other.", do=[SVG(ANG2, 760, 110, w=460)]),
        dict(say="Join the vertex to that crossing point. The angle is cut exactly in half. Every point on this line is the same distance from both arms.", do=[SVG(ABIS, 760, 110, w=460), T("same distance from **both arms**", x=80, y=200, color=GREEN, at=3)]),
    ]),
    dict(kind="method", title="How do I construct with ruler and compasses?", steps=[
        dict(say="Here is the method. Step 1: make a quick sketch with the measurements.", do=[T("1. **Sketch** with the measurements", x=80, y=170)]),
        dict(say="Step 2: draw the first line accurately with a ruler.", do=[T("2. Draw the first line with a **ruler**", x=80, y=260)]),
        dict(say="Step 3: keep the compass width fixed when you draw matching arcs.", do=[T("3. Keep the **compass width** fixed", x=80, y=350)]),
        dict(say="Step 4: leave all your arcs showing, and check by measuring.", do=[T("4. **Leave the arcs**; check by measuring", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="An SSS triangle", steps=[
        dict(say="Construct triangle A B C with A B equal to 7 centimetres, B C equal to 5 centimetres, and A C equal to 6 centimetres.", do=[T("AB = **7 cm** · BC = **5 cm** · AC = **6 cm**", x=80, y=170)]),
        dict(say="Draw A B, 7 centimetres long. Set the compasses to 6 centimetres and draw an arc from A. Then set them to 5 centimetres and draw an arc from B.",
             do=[T("1. AB = 7 cm", x=80, y=260), T("2. arc of **6 cm** from A", x=80, y=330), T("3. arc of **5 cm** from B", x=80, y=400)]),
        dict(say="C is where the arcs cross. Join A C and B C.", do=[T("4. C is where they cross; join AC and BC", x=80, y=470, color=GREEN)]),
    ]),
    dict(kind="example", title="A lamp in a corner", steps=[
        dict(say="A lamp must be the same distance from the two walls of a corner. Where should it go?", do=[E("💡", 90, 160, 90), T("equally far from **two walls**", x=230, y=190)]),
        dict(say="Points that are equally far from two lines that meet are on the angle bisector. So the lamp goes on the bisector of the corner angle.", do=[SVG(ANG + ABIS, 760, 110, w=460), B("on the angle bisector", x=230, y=300, color=GREEN, at=4)]),
        PAUSE("5.3-k3", "Your turn. Points equally far from two lines that meet lie on which construction? Pause and choose.", "Equally far from two lines that meet: …"),
    ]),
    dict(kind="example", title="Check: two lines that meet", steps=[
        dict(say="Equally far from two lines that meet means the angle bisector. Equally far from two points means the perpendicular bisector.",
             do=[T("two **lines** → angle bisector", x=80, y=190, color=GREEN), T("two **points** → perpendicular bisector", x=80, y=270)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Max constructs the perpendicular bisector of A B. Which line goes wrong first?", do=LINES("Max", "the perpendicular bisector of AB", ["Arc from A with radius 5 cm", "Arc from B with radius 4 cm", "Join the crossing points"])),
        dict(say="Line 2 is wrong. Both arcs must have the same radius. Otherwise the line does not cut A B in half.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="Keep the compasses at 5 centimetres for both arcs.", do=[B("same radius from A and from B", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Mobile phone masts", steps=[
        dict(say="Phone networks use the same idea. A phone usually connects to the nearest mast. The boundary between two masts' areas is the perpendicular bisector of the line joining them.",
             do=[E("📡", 90, 170, 100), T("the boundary between two masts = **perpendicular bisector**", x=230, y=200)]),
        dict(say="Maps made of these boundaries are called Voronoi diagrams. They are also used to plan school catchment areas and delivery zones.", do=[T("**Voronoi diagrams**: catchment areas, delivery zones", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("5.3-k4", "One last question. The perpendicular bisector of a 10 centimetre line crosses it how far from each end? Pause the video and answer.", "The perpendicular bisector of a 10 cm line crosses it how far from each end (cm)?"),
        dict(say="It cuts the line in half. Half of 10 is 5. It crosses 5 centimetres from each end.", do=[B("5 cm", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: you can construct triangles from S S S, S A S, A S A or R H S.", do=[T("• Triangles: SSS, SAS, ASA, RHS", x=80, y=170)]),
        dict(say="Perpendicular bisector: equal arcs from both ends of the line.", do=[T("• Perpendicular bisector: equal arcs from **both ends**", x=80, y=250)]),
        dict(say="Angle bisector: an arc from the vertex, then two equal arcs.", do=[T("• Angle bisector: arc from the vertex, then equal arcs", x=80, y=330)]),
        dict(say="Keep your arcs, and check by measuring.", do=[T("• Keep the arcs; check by measuring", x=80, y=410)]),
    ]),
]
