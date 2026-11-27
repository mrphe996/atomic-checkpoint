# -*- coding: utf-8 -*-
"""Stage 8 · Unit 8 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG
from .s7_u04 import TBL, ROW
from .s7_u05 import BIG
from .s7_u08 import SVG, POLY, DASH, LINE, DOT, TXT, INK, RECT, PARA, KITE, SOLID, CELLS

SQUARE = [(70, 70), (250, 70), (250, 250), (70, 250)]
RHOMB = [(160, 30), (270, 160), (160, 290), (50, 160)]
TRAP = [(40, 240), (280, 240), (220, 90), (100, 90)]
DIAG = lambda pts, c=RED: DASH(*pts[0], *pts[2], c) + DASH(*pts[1], *pts[3], c)
CIRC = lambda x=760, y=130, w=460, at=0, **k: BIG(FIG(x, y, w, at, kind="circle", **k))
PI = "π"

VIDEOS = {}

VIDEOS["8.1"] = [
    dict(kind="hook", title="A family of shapes", steps=[
        dict(say="Someone says: a square is a rectangle, and a rectangle is a parallelogram. Is that true?",
             do=[E("🟦", 90, 170, 100), T("“A square **is** a rectangle, and a rectangle **is** a parallelogram.”", x=230, y=200)]),
        PAUSE("8.1-k1", "Is a square a rectangle? Pause the video and decide.", "Is a square a rectangle?"),
    ]),
    dict(kind="hook", title="Yes!", steps=[
        dict(say="A rectangle is any quadrilateral with 4 right angles. A square has 4 right angles, so yes, a square is a special rectangle. It also has 4 equal sides.",
             do=[SVG(POLY(SQUARE), 800, 120, w=360), B("a square **is** a rectangle", x=80, y=200, color=GREEN), T("4 right angles ✓ (and 4 equal sides)", x=80, y=300)]),
    ]),
    dict(kind="recall", title="Symmetry of regular polygons", steps=[
        dict(say="Remember: a regular polygon with n sides has n lines of symmetry, and rotational symmetry of order n. A regular octagon has 8 lines of symmetry.",
             do=[T("regular n-gon: **n** lines, order **n**", x=80, y=170), MATH("octagon: 8 lines, order 8", x=80, y=270)]),
    ]),
    dict(kind="idea", title="Properties", steps=[
        dict(say="Each quadrilateral has its own properties: sides, angles, diagonals and symmetry.",
             do=[TBL(["Shape", "Sides", "Angles", "Diagonals", "Lines / order"],
                     [["square", "4 equal, 2 pairs parallel", "all 90°", "equal, bisect at 90°", "4 / 4"],
                      ["rectangle", "opposites equal, 2 pairs parallel", "all 90°", "equal, bisect", "2 / 2"],
                      ["rhombus", "4 equal, 2 pairs parallel", "opposites equal", "bisect at 90°", "2 / 2"],
                      ["parallelogram", "opposites equal, 2 pairs parallel", "opposites equal", "bisect", "0 / 2"],
                      ["kite", "2 pairs of adjacent equal", "one pair equal", "cross at 90°, one bisects", "1 / 1"],
                      ["trapezium", "1 pair parallel", "–", "–", "0 / 1"]], x=40, y=150), ROW(0, 0.3), ROW(1, 1.3), ROW(2, 2.3)]),
        dict(say="Look carefully at the diagonals. In a kite, the diagonals cross at 90 degrees, but only one of them cuts the other in half.", do=[ROW(3, 0.3), ROW(4, 1.2), ROW(5, 3.5)]),
        PAUSE("8.1-k2", "Your turn. The diagonals cross at 90 degrees, and only one bisects the other. Which shape is it? Pause the video and choose.", "Diagonals cross at 90° and only one bisects the other: …"),
    ]),
    dict(kind="idea", title="Check: a kite", steps=[
        dict(say="It is a kite. The long diagonal cuts the short one in half, at 90 degrees. But the short one does not cut the long one in half.",
             do=[SVG(POLY(KITE) + DIAG(KITE), 800, 120, w=380), B("kite", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="The family tree", steps=[
        dict(say="A shape belongs to a family if it has all the properties of that family. So a square is a rectangle, a rectangle is a parallelogram, and a parallelogram is a trapezium.",
             do=[MATH("square ⊂ rectangle ⊂ parallelogram ⊂ trapezium", x=80, y=180)]),
        dict(say="A square is also a rhombus, and a rhombus is a parallelogram. A rhombus is also a kite.", do=[MATH("square ⊂ rhombus ⊂ parallelogram", x=80, y=280), T("a rhombus is also a **kite**", x=80, y=370)]),
        dict(say="But not every rhombus is a square. A rhombus does not need right angles.", do=[SVG(POLY(RHOMB), 840, 150, w=320), T("not every rhombus is a square ✗", x=80, y=450, color=RED)]),
    ]),
    dict(kind="method", title="How do I identify a quadrilateral?", steps=[
        dict(say="Here is the method. Step 1: check the sides. Are they equal? Are they parallel?", do=[T("1. **Sides**: equal? parallel?", x=80, y=170)]),
        dict(say="Step 2: check the angles. Right angles? Opposite angles equal?", do=[T("2. **Angles**: right angles? opposites equal?", x=80, y=260)]),
        dict(say="Step 3: check the diagonals. Equal? Perpendicular? Do they bisect each other?", do=[T("3. **Diagonals**: equal? perpendicular? bisecting?", x=80, y=350)]),
        dict(say="Step 4: name the most specific shape. But remember it belongs to the bigger families too.", do=[T("4. Name the **most specific** shape", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="From the diagonals", steps=[
        dict(say="A quadrilateral's diagonals are equal and bisect each other, but they are not perpendicular. Name it.", do=[T("diagonals: **equal**, **bisect**, not at 90°", x=80, y=170)]),
        dict(say="Bisecting diagonals means a parallelogram. Equal diagonals means a rectangle. Not perpendicular means it is not a square. So it is a rectangle.",
             do=[SVG(POLY(RECT) + DIAG(RECT), 800, 120, w=380), B("rectangle", x=80, y=280, color=GREEN, at=7)]),
    ]),
    dict(kind="example", title="Symmetry of a rhombus", steps=[
        dict(say="A rhombus has 2 lines of symmetry: its two diagonals. It looks the same after a half turn, so its rotational symmetry has order 2.",
             do=[SVG(POLY(RHOMB) + DIAG(RHOMB, GREEN), 800, 120, w=380), MATH("2 lines, order 2", x=80, y=200, color=GREEN)]),
        PAUSE("8.1-k3", "Your turn. What is the order of rotational symmetry of a parallelogram? Pause and work it out.", "Order of rotational symmetry of a parallelogram?"),
    ]),
    dict(kind="example", title="Check: a parallelogram", steps=[
        dict(say="A parallelogram fits onto itself after a half turn, and after a full turn. So the order is 2. But it has no lines of symmetry.",
             do=[SVG(POLY(PARA), 800, 120, w=380), B("order 2", x=80, y=200, color=GREEN), T("0 lines of symmetry", x=80, y=300)]),
    ]),
    dict(kind="example", title="Can a trapezium be symmetric?", steps=[
        dict(say="True or false: a trapezium can have a line of symmetry. True. An isosceles trapezium has one line, through the middles of the parallel sides.",
             do=[SVG(POLY(TRAP) + DASH(160, 60, 160, 270, GREEN), 800, 120, w=380), B("true", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A shape has exactly one pair of parallel sides. Ben names it. Which line is wrong?", do=LINES("Ben", "exactly one pair of parallel sides", ["It has parallel sides", "so it is a parallelogram"])),
        dict(say="Line 2 is wrong. A parallelogram needs two pairs of parallel sides. One pair makes a trapezium.", do=[dict(a="cross", id="l2")]),
        dict(say="The shape is a trapezium.", do=[B("trapezium", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Folding tables", steps=[
        dict(say="Many folding tables and lamps use parallelograms. When the sides are joined at hinges, a parallelogram can lean over, but its opposite sides stay parallel.",
             do=[E("🛋️", 90, 170, 100), T("a hinged **parallelogram** keeps its sides parallel", x=230, y=200)]),
        dict(say="So the table top stays level, even as the legs fold. A rectangle that leans over becomes a parallelogram.", do=[T("the top stays **level** as the legs fold", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.1-k4", "One last question. A rhombus with a right angle is what shape? Pause the video and choose.", "A rhombus with a right angle is a …"),
        dict(say="A rhombus has 4 equal sides. If one angle is 90 degrees, all four are, so it is a square.", do=[SVG(POLY(SQUARE), 800, 120, w=360), B("square", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: know the sides, angles, diagonals and symmetry of each quadrilateral.", do=[T("• Sides, angles, diagonals, symmetry", x=80, y=170)]),
        dict(say="A square is a rectangle, and a rectangle is a parallelogram. A square is also a rhombus.", do=[T("• square ⊂ rectangle ⊂ parallelogram; square ⊂ rhombus", x=80, y=250)]),
        dict(say="A regular polygon with n sides has n lines of symmetry, and order n.", do=[T("• Regular n-gon: n lines, order n", x=80, y=330)]),
        dict(say="Name the most specific shape that fits.", do=[T("• Name the most specific shape", x=80, y=410)]),
    ]),
]

VIDEOS["8.2"] = [
    dict(kind="hook", title="How far does a wheel go?", steps=[
        dict(say="A bicycle wheel has a diameter of 70 centimetres. Each full turn, the bike moves forward one circumference: the distance round the wheel.",
             do=[E("🚲", 90, 170, 100), T("diameter **70 cm** · one turn = one **circumference**", x=230, y=200), CIRC(d="70 cm", at=1)]),
        PAUSE("8.2-k1", "Roughly how far does the bike go in one turn: 2 times 70, or 3 times 70? Pause the video and choose.", "One turn of a 70 cm wheel is about …"),
    ]),
    dict(kind="hook", title="About 3 times", steps=[
        dict(say="The distance round a circle is a bit more than 3 times its diameter. So one turn is about 3 times 70, which is 210 centimetres.", do=[MATH("≈ 3 × 70 = 210 cm", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="recall", title="Radius and diameter", steps=[
        dict(say="Remember: the diameter goes right across the circle, through the centre. It is twice the radius. A radius of 4.5 centimetres gives a diameter of 9 centimetres.",
             do=[MATH("d = 2r", x=80, y=180), MATH("r = 4.5 → d = 9 cm", x=80, y=280), CIRC(r="r", at=1)]),
    ]),
    dict(kind="idea", title="Discovering pi", steps=[
        dict(say="Measure the circumference and the diameter of some round objects, and divide. Something amazing happens.",
             do=[TBL(["Object", "C (cm)", "d (cm)", "C ÷ d"], [["can", "22.0", "7.0", "3.14"], ["plate", "78.5", "25.0", "3.14"], ["coin", "7.5", "2.4", "3.13"]], y=170), ROW(0, 1), ROW(1, 2.4), ROW(2, 3.8)]),
        dict(say="The answer is always about 3.14. This number is called pi. Its digits go on forever: 3.14159, and so on.", do=[B(f"C ÷ d = {PI} ≈ 3.14159…", x=80, y=420, color=BLUE)]),
        PAUSE("8.2-k2", "Your turn. Circumference divided by diameter, for any circle, is about what, to 2 decimal places? Pause the video and answer.", "C ÷ d for any circle ≈ ? (2 d.p.)"),
    ]),
    dict(kind="idea", title="The formula", steps=[
        dict(say="It is 3.14. So the circumference is pi times the diameter. Or, because the diameter is 2 r, it is 2 pi r.", do=[B(f"C = {PI}d = 2{PI}r", x=80, y=190, color=GREEN)]),
        dict(say="For the wheel: pi times 70 is 219.9, which is about 220 centimetres. That is close to our estimate.", do=[MATH(f"{PI} × 70 = 219.9… ≈ 220 cm", x=80, y=300)]),
        dict(say="Use the pi button on a calculator, and round sensibly. Without a calculator, use 3.14.", do=[T(f"use the **{PI}** button · or {PI} ≈ 3.14", x=80, y=400)]),
    ]),
    dict(kind="method", title="How do I find a circumference?", steps=[
        dict(say="Here is the method. Step 1: decide whether you have the radius or the diameter.", do=[T("1. **Radius** or **diameter**?", x=80, y=170)]),
        dict(say="Step 2: use C equals pi d, or C equals 2 pi r.", do=[T(f"2. C = {PI}d  or  C = 2{PI}r", x=80, y=260)]),
        dict(say="Step 3: use the pi button, and round sensibly, with units.", do=[T(f"3. **{PI}** button; round; units", x=80, y=350)]),
        dict(say="Step 4: check with an estimate. The circumference is just over 3 times the diameter.", do=[T("4. **Check**: just over 3 × d", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="From the radius", steps=[
        dict(say="Find the circumference when the radius is 8 centimetres. C equals 2 times pi times 8, which is 50.26, or 50.3 centimetres to 1 decimal place.",
             do=[CIRC(r="8 cm"), MATH(f"C = 2 × {PI} × 8", x=80, y=190), B("≈ 50.3 cm", x=80, y=300, color=GREEN, at=5)]),
        PAUSE("8.2-k3", "Your turn. Find the circumference when the diameter is 20 centimetres, to 1 decimal place. Pause and work it out.", "C for d = 20 cm (1 d.p.)?"),
    ]),
    dict(kind="example", title="Check: d = 20 cm", steps=[
        dict(say="Pi times 20 is 62.83. To 1 decimal place, that is 62.8 centimetres.", do=[MATH(f"{PI} × 20 = 62.83…", x=80, y=190), B("62.8 cm", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Finding the diameter", steps=[
        dict(say="A round pond has a circumference of 31.4 metres. Find its diameter. C equals pi d, so d equals C divided by pi.", do=[MATH(f"d = C ÷ {PI}", x=80, y=170)]),
        dict(say="31.4 divided by pi is 9.99, which is about 10 metres.", do=[MATH(f"31.4 ÷ {PI} = 9.99…", x=80, y=270), B("≈ 10 m", x=80, y=370, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="A semicircle", steps=[
        dict(say="Find the perimeter of a semicircle with diameter 10 centimetres. The curved part is half of pi times 10, which is 15.7.",
             do=[CIRC(part="semi", d="10 cm"), MATH(f"½ × {PI} × 10 = 15.7", x=80, y=190)]),
        dict(say="Don't forget the straight edge, which is the diameter, 10. The perimeter is 25.7 centimetres.", do=[MATH("15.7 + 10", x=80, y=290), B("25.7 cm", x=80, y=390, color=GREEN, at=4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Maya finds the circumference when the radius is 6 centimetres. Which line goes wrong first?", do=LINES("Maya", "C when r = 6 cm", [f"C = {PI}d = {PI} × 6", "C = 18.8 cm"])),
        dict(say="Line 1 is wrong. 6 is the radius, not the diameter. The diameter is 12.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="Pi times 12 is 37.7 centimetres.", do=[B(f"C = {PI} × 12 = 37.7 cm", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Measuring a road", steps=[
        dict(say="Surveyors measure roads with a measuring wheel. It has a circumference of exactly 1 metre, so it counts 1 metre for every turn.",
             do=[E("🛞", 90, 170, 100), T("a measuring wheel: circumference **1 m**", x=230, y=200)]),
        dict(say="Its diameter must be 1 divided by pi, which is about 31.8 centimetres.", do=[MATH(f"d = 1 ÷ {PI} ≈ 0.318 m", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.2-k4", "One last question. A circle has a circumference of 25.1 centimetres. Find its diameter, to the nearest centimetre. Pause the video and answer.", "C = 25.1 cm. Diameter (nearest cm)?"),
        dict(say="d equals C divided by pi. 25.1 divided by pi is 7.99, which is 8 centimetres.", do=[MATH(f"25.1 ÷ {PI} = 7.99…", x=80, y=190), B("8 cm", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: pi is the circumference divided by the diameter. It is about 3.14159.", do=[T(f"• {PI} = C ÷ d ≈ 3.14159…", x=80, y=170)]),
        dict(say="C equals pi d, or 2 pi r.", do=[T(f"• C = {PI}d = 2{PI}r", x=80, y=250)]),
        dict(say="To find the diameter, divide the circumference by pi.", do=[T(f"• d = C ÷ {PI}", x=80, y=330)]),
        dict(say="Round sensibly, and estimate with 3 times the diameter.", do=[T("• Round sensibly; estimate with 3 × d", x=80, y=410)]),
    ]),
]

VIDEOS["8.3"] = [
    dict(kind="hook", title="Three views", steps=[
        dict(say="An architect builds a model and draws it from three directions: from the front, from the side, and from above. The view from above is called the plan.",
             do=[E("🏗️", 90, 170, 100), T("**front** · **side** · **above** (the plan)", x=230, y=200), SOLID("cuboid", a="4", b="2", c="3", at=1)]),
        dict(say="Why does she need all three? Could two different buildings look the same from the front?", do=[T("same front view, different buildings?", x=230, y=300)]),
        PAUSE("8.3-k1", "Could two different solids have the same front view? Pause the video and decide.", "Could two different solids have the same front view?"),
    ]),
    dict(kind="hook", title="Yes", steps=[
        dict(say="Yes. A cylinder and a cuboid can both look like a rectangle from the front. You need other views to tell them apart.",
             do=[SOLID("cylinder", x=640, w=300), SOLID("cuboid", x=960, w=300, at=0.6), B("both: a rectangle from the front", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="recall", title="Faces, edges, vertices", steps=[
        dict(say="Remember: a triangular prism has 5 faces, 9 edges and 6 vertices. A square-based pyramid has 5 faces, 8 edges and 5 vertices.",
             do=[SOLID("triprism", x=700, w=420), MATH("prism: F 5, E 9, V 6", x=80, y=190), MATH("square pyramid: F 5, E 8, V 5", x=80, y=280, at=5)]),
    ]),
    dict(kind="idea", title="Euler's rule", steps=[
        dict(say="For any solid with flat faces and no holes, faces plus vertices minus edges equals 2. This is Euler's rule.",
             do=[B("F + V − E = 2", x=80, y=160, color=BLUE), TBL(["Solid", "F", "V", "E", "F + V − E"], [["cube", "6", "8", "12", "2"], ["triangular prism", "5", "6", "9", "2"], ["square-based pyramid", "5", "5", "8", "2"]], y=260), ROW(0, 3), ROW(1, 4), ROW(2, 5)]),
        PAUSE("8.3-k2", "Your turn. What is F plus V minus E for a cube? Pause the video and work it out.", "F + V − E for a cube?"),
    ]),
    dict(kind="idea", title="Check: a cube", steps=[
        dict(say="A cube has 6 faces, 8 vertices and 12 edges. 6 plus 8 minus 12 is 2.", do=[MATH("6 + 8 − 12 = 2", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Plans and elevations", steps=[
        dict(say="The plan is the view from directly above. The front elevation is the view from the front, and the side elevation is the view from the side.",
             do=[T("**plan**: from above · **front elevation** · **side elevation**", x=80, y=170)]),
        dict(say="Here is a solid made of 4 cubes: 3 in a row, with 1 on top of the left cube. From the front it looks like an L of 4 squares.",
             do=[CELLS([[0, 1], [1, 1], [2, 1], [0, 0]], x=80, y=260, w=300), T("front", x=150, y=500)]),
        dict(say="From the side, you see 2 squares, one on top of the other. From above, you see 3 squares in a row.",
             do=[CELLS([[0, 1], [0, 0]], x=460, y=260, w=200), T("side", x=500, y=500), CELLS([[0, 0], [1, 0], [2, 0]], x=760, y=260, w=300, at=3), T("plan", x=830, y=500, at=3)]),
    ]),
    dict(kind="method", title="How do I describe a 3D shape?", steps=[
        dict(say="Here is the method. Step 1: name the shape from its cross-section, for a prism, or its base, for a pyramid.", do=[T("1. Name it: **cross-section** or **base**", x=80, y=170)]),
        dict(say="Step 2: count the faces, vertices and edges carefully. Check with Euler's rule.", do=[T("2. Count F, V, E; check **F + V − E = 2**", x=80, y=260)]),
        dict(say="Step 3: draw the plan, front and side elevations to scale.", do=[T("3. Draw plan and elevations **to scale**", x=80, y=350)]),
        dict(say="Step 4: use the views together to identify a solid.", do=[T("4. Use the views **together**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Using Euler's rule", steps=[
        dict(say="A pyramid has 7 vertices. One is the top, so the base has 6 corners. It is a hexagonal pyramid.", do=[MATH("V = 7 → base has 6 corners", x=80, y=170)]),
        dict(say="It has 7 faces: the base and 6 triangles. It has 12 edges: 6 round the base and 6 up to the top. Check: 7 plus 7 minus 12 is 2.",
             do=[MATH("F = 7, E = 12", x=80, y=270), B("7 + 7 − 12 = 2 ✓", x=80, y=370, color=GREEN, at=7)]),
    ]),
    dict(kind="example", title="From views to solid", steps=[
        dict(say="The plan is a circle. The front and side views are both triangles. What solid is it? It is round from above, and pointed from the sides. It is a cone.",
             do=[T("plan: **circle** · front and side: **triangle**", x=80, y=170), SOLID("cone", x=760, w=380), B("cone", x=80, y=280, color=GREEN, at=6)]),
        PAUSE("8.3-k3", "Your turn. What is the plan of a cylinder standing up? Pause and choose.", "The plan of a cylinder standing up is …"),
    ]),
    dict(kind="example", title="Check: a cylinder", steps=[
        dict(say="From directly above, a standing cylinder looks like a circle. From the front and the side, it looks like a rectangle.",
             do=[SOLID("cylinder", x=760, w=380), B("plan: a circle", x=80, y=200, color=GREEN), T("front and side: rectangles", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A shape has 6 faces and 12 edges. Kim finds the number of vertices. Which line goes wrong first?", do=LINES("Kim", "6 faces and 12 edges: vertices?", ["F + V + E = 2", "V = 2 − 6 − 12 = −16"])),
        dict(say="Line 1 is wrong. Euler's rule is F plus V minus E equals 2. You cannot have negative vertices!", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="6 plus V minus 12 equals 2, so V equals 8. It could be a cube.", do=[B("6 + V − 12 = 2 → V = 8", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Football", steps=[
        dict(say="A classic football is made of 12 pentagons and 20 hexagons, so it has 32 faces. It has 60 vertices and 90 edges.",
             do=[E("⚽", 90, 170, 100), T("12 pentagons + 20 hexagons: **F 32, V 60, E 90**", x=230, y=200)]),
        dict(say="Check Euler's rule: 32 plus 60 minus 90 is 2. It works even for a football.", do=[MATH("32 + 60 − 90 = 2 ✓", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.3-k4", "One last question. A prism has 15 edges. How many vertices does it have? Pause the video and answer.", "A prism has 15 edges. How many vertices?"),
        dict(say="A prism with an n-sided end has 3 n edges and 2 n vertices. 15 edges means n is 5, a pentagonal prism. So it has 10 vertices.",
             do=[MATH("3n = 15 → n = 5", x=80, y=190), B("2n = 10 vertices", x=80, y=300, color=GREEN, at=5)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: for solids with flat faces, F plus V minus E equals 2.", do=[T("• F + V − E = 2", x=80, y=170)]),
        dict(say="The plan is the view from above. The elevations are the views from the front and the side.", do=[T("• Plan = from above; elevations = front and side", x=80, y=250)]),
        dict(say="Draw the views to scale.", do=[T("• Draw the views to scale", x=80, y=330)]),
        dict(say="Use several views together to identify a solid.", do=[T("• Use several views to identify a solid", x=80, y=410)]),
    ]),
]
