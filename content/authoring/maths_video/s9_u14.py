# -*- coding: utf-8 -*-
"""Stage 9 · Unit 14 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

VIDEOS = {}

VIDEOS["14.1"] = [
    dict(kind="hook", title="A water tank", steps=[
        dict(say="A farm has a cylinder-shaped water tank, 1.2 metres across and 1.5 metres tall. It also has a trough shaped like a trapezium prism.",
             do=[E("🚜", 90, 170, 100), T("tank: **1.2 m** across, **1.5 m** tall · a **trapezium** trough", x=230, y=200)]),
        PAUSE("14.1-k1", "What is a cylinder: like a prism with a circular cross-section, or a pyramid? Pause the video and choose.", "A cylinder is …"),
    ]),
    dict(kind="hook", title="Like a prism", steps=[
        dict(say="It is like a prism with a circular cross-section. The circle is the same all the way up.", do=[B("like a prism, circular cross-section", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Prisms", steps=[
        dict(say="Remember: the volume of a prism is the area of the cross-section, times the length.", do=[B("V = area of cross-section × length", x=80, y=190, color=BLUE)]),
    ]),
    dict(kind="idea", title="Any prism", steps=[
        dict(say="A prism has the same cross-section all along its length: a triangle, a trapezium, a hexagon. The trough's cross-section is a trapezium with parallel sides 0.5 and 0.3 metres, and height 0.4 metres. It is 2 metres long.",
             do=[T("trapezium: **0.5 m**, **0.3 m**, height **0.4 m** · length **2 m**", x=80, y=170)]),
        dict(say="The area is a half times 0.5 plus 0.3, times 0.4. That is 0.16 square metres. 1 cubic metre is 1,000 litres.", do=[MATH("A = ½(0.5 + 0.3) × 0.4 = 0.16 m²", x=80, y=270), MATH("1 m³ = 1000 L", x=80, y=360)]),
        PAUSE("14.1-k2", "Your turn. What is the volume of the trough, in litres? Pause the video and try it.", "Trough volume in litres?"),
    ]),
    dict(kind="idea", title="Check: 320 L", steps=[
        dict(say="0.16 times 2 is 0.32 cubic metres, which is 320 litres.", do=[B("0.16 × 2 = 0.32 m³ = 320 L", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Cylinders", steps=[
        dict(say="For a cylinder, the cross-section is a circle, so the volume is pi R squared, times the height.", do=[B("V = πr²h", x=80, y=170, color=BLUE)]),
        dict(say="The tank is 1.2 metres across, so its radius is 0.6 metres. The height is 1.5 metres.", do=[MATH("r = 0.6 m, h = 1.5 m", x=80, y=270)]),
        PAUSE("14.1-k3", "Your turn. Find the volume of the tank, in cubic metres, to 1 decimal place. Pause and work it out.", "Tank volume (m³)? (1 d.p.)"),
    ]),
    dict(kind="idea", title="Check: 1.7 m³", steps=[
        dict(say="Pi times 0.36 times 1.5 is about 1.696 cubic metres. That is about 1.7, or nearly 1,700 litres.", do=[B("π × 0.36 × 1.5 ≈ 1.7 m³", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I find the volume?", steps=[
        dict(say="Here is the method. Step 1: find the cross-section.", do=[T("1. Find the **cross-section**", x=80, y=170)]),
        dict(say="Step 2: work out its area. For a circle, halve the diameter first.", do=[T("2. Its **area** (halve diameters)", x=80, y=260)]),
        dict(say="Step 3: multiply by the length or height.", do=[T("3. **× length**", x=80, y=350)]),
        dict(say="Step 4: give units, and convert to litres if needed.", do=[T("4. **Units**; litres?", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="A triangular prism: the triangle has base 6 and height 4 centimetres, so its area is 12. The length is 9. The volume is 108 cubic centimetres.", do=[MATH("½ × 6 × 4 × 9 = 108 cm³", x=80, y=180)]),
        dict(say="A can has diameter 8 and height 12 centimetres. Pi times 16 times 12 is about 603 cubic centimetres, which is 603 millilitres.", do=[MATH("π × 4² × 12 ≈ 603 mL", x=80, y=280)]),
        dict(say="A cylinder has volume 500 and radius 5. The height is 500 divided by 25 pi, which is about 6.4 centimetres.", do=[MATH("h = 500 ÷ 25π ≈ 6.4 cm", x=80, y=380)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A cylinder has diameter 10 centimetres and height 4. Ravi finds the volume. Which line is wrong?", do=LINES("Ravi", "diameter 10 cm, height 4 cm", ["V = π × 10² × 4 ≈ 1256.6 cm³"])),
        dict(say="Line 1 is wrong. He used the diameter. The radius is 5.", do=[dict(a="cross", id="l1")]),
        dict(say="Pi times 25 times 4 is about 314.2 cubic centimetres.", do=[B("π × 5² × 4 ≈ 314.2 cm³", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Packaging", steps=[
        dict(say="Engineers use prism and cylinder volumes to size water tanks, pipes and drink cans.", do=[E("🥫", 90, 170, 100), T("tanks · pipes · cans", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.1-k4", "One last question. A cylinder has radius 1 and height 1. What is its volume, to 1 decimal place? Pause the video and answer.", "Cylinder r = 1, h = 1? (1 d.p.)"),
        dict(say="Pi times 1 times 1 is pi, about 3.1.", do=[B("π ≈ 3.1", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: prism volume is the cross-section area times the length.", do=[T("• Prism: V = A × l", x=80, y=170)]),
        dict(say="Cylinder: pi R squared H.", do=[T("• Cylinder: V = πr²h", x=80, y=250)]),
        dict(say="1 cubic metre is 1,000 litres. 1,000 cubic centimetres is 1 litre.", do=[T("• 1 m³ = 1000 L · 1000 cm³ = 1 L", x=80, y=330)]),
        dict(say="Halve the diameter.", do=[T("• Halve diameters", x=80, y=410)]),
    ]),
]

VIDEOS["14.2"] = [
    dict(kind="hook", title="A tin label", steps=[
        dict(say="A food company makes a tin 8 centimetres tall, with radius 3 centimetres. It needs a paper label all round the side, and metal for the top and bottom.",
             do=[E("🥫", 90, 170, 100), T("tin: **h = 8 cm**, **r = 3 cm**", x=230, y=200)]),
        PAUSE("14.2-k1", "When you unroll the label, what shape is it: a rectangle, or a circle? Pause the video and choose.", "The unrolled label is …"),
    ]),
    dict(kind="hook", title="A rectangle", steps=[
        dict(say="A rectangle.", do=[B("a rectangle", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Nets", steps=[
        dict(say="Remember: a net folds into a 3D shape. The surface area is the total area of the net.", do=[T("surface area = area of the **net**", x=80, y=190)]),
    ]),
    dict(kind="idea", title="The net of a cylinder", steps=[
        dict(say="The rectangle's height is the tin's height. Its length goes all the way round: the circumference, 2 pi R.",
             do=[T("height **h** · length = circumference **2πr**", x=80, y=170), B("curved surface = 2πrh", x=80, y=270, color=BLUE)]),
        PAUSE("14.2-k2", "Your turn. Find the area of the label, to 1 decimal place. Pause the video and try it.", "Label area (cm²)? (1 d.p.)"),
    ]),
    dict(kind="idea", title="Check: 150.8", steps=[
        dict(say="2 times pi times 3 times 8 is about 150.8 square centimetres.", do=[B("2π × 3 × 8 ≈ 150.8 cm²", x=80, y=190, color=GREEN)]),
        dict(say="The top and bottom are two circles, each pi R squared.", do=[MATH("top + bottom = 2πr²", x=80, y=300)]),
        PAUSE("14.2-k3", "Your turn. Find the total surface area of the tin, to 1 decimal place. Pause and work it out.", "Total surface of the tin (cm²)? (1 d.p.)"),
    ]),
    dict(kind="idea", title="Check: 207.3", steps=[
        dict(say="The two circles: 2 times pi times 9, about 56.5. Add the label: about 207.3 square centimetres.", do=[MATH("2π × 9 ≈ 56.5", x=80, y=180), B("150.8 + 56.5 ≈ 207.3 cm²", x=80, y=290, color=GREEN)]),
        dict(say="A triangular prism has 2 triangles and 3 rectangles. A pyramid has a base and triangles. Sketch the net and list each face.", do=[T("sketch the net · **list** every face", x=80, y=400)]),
    ]),
    dict(kind="method", title="How do I find a surface area?", steps=[
        dict(say="Here is the method. Step 1: sketch the net.", do=[T("1. Sketch the **net**", x=80, y=170)]),
        dict(say="Step 2: find the area of each face.", do=[T("2. Each face's **area**", x=80, y=260)]),
        dict(say="Step 3: check for open faces, like a cup with no lid.", do=[T("3. Any **open** faces?", x=80, y=350)]),
        dict(say="Step 4: add them up, and give the units.", do=[T("4. **Add**; units", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="A cup with no lid: radius 4, height 9. One circle, 16 pi, plus the side, 72 pi. That is 88 pi, about 276.5 square centimetres.", do=[MATH("16π + 72π = 88π ≈ 276.5 cm²", x=80, y=180)]),
        dict(say="A square-based pyramid: base 10, slant height 13. The base is 100. Each triangle is a half times 10 times 13, which is 65. 100 plus 4 times 65 is 360.", do=[MATH("100 + 4 × 65 = 360 cm²", x=80, y=280)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Amy finds the label for a tin with radius 3 and height 8. Which line is wrong?", do=LINES("Amy", "label, r = 3 cm, h = 8 cm", ["rectangle 3 cm × 8 cm = 24 cm²"])),
        dict(say="Line 1 is wrong. The label wraps all the way round. Its length is the circumference.", do=[dict(a="cross", id="l1")]),
        dict(say="2 pi times 3 is about 18.85. Times 8 is about 150.8.", do=[B("18.85 × 8 ≈ 150.8 cm²", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Less metal", steps=[
        dict(say="Can makers choose the radius and height carefully, to hold the same amount using as little metal as possible.", do=[E("🏭", 90, 170, 100), T("same volume, **less metal**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.2-k4", "One last question. A cylinder has radius 5 and height 6. Is its surface area 110 pi, or 80 pi? Pause the video and choose.", "r = 5, h = 6 in terms of π?"),
        dict(say="2 pi R squared is 50 pi. 2 pi R H is 60 pi. Together, 110 pi.", do=[B("50π + 60π = 110π", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a cylinder's surface is 2 pi R squared plus 2 pi R H.", do=[T("• Cylinder: 2πr² + 2πrh", x=80, y=170)]),
        dict(say="The curved surface is 2 pi R H.", do=[T("• Curved: 2πrh", x=80, y=250)]),
        dict(say="Prisms: two ends plus rectangles. Pyramids: a base plus triangles.", do=[T("• Prism: ends + rectangles · pyramid: base + triangles", x=80, y=330)]),
        dict(say="Check for open faces.", do=[T("• Check for open faces", x=80, y=410)]),
    ]),
]

VIDEOS["14.3"] = [
    dict(kind="hook", title="Cutting a cake", steps=[
        dict(say="A rectangular cake is a cuboid, but not a cube. Its edges are all different lengths. It must be cut by one straight slice, into two halves that are exact mirror images.",
             do=[E("🎂", 90, 170, 100), T("a cuboid cake · one slice · **mirror-image** halves", x=230, y=200)]),
        PAUSE("14.3-k1", "How many different ways can you do it? Pause the video and work it out.", "Ways to cut the cake?"),
    ]),
    dict(kind="hook", title="3 ways", steps=[
        dict(say="3 ways: across the length, across the width, or across the height, each time through the middle.", do=[B("3 ways", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Lines of symmetry", steps=[
        dict(say="Remember: a rectangle has 2 lines of symmetry, and a square has 4.", do=[T("rectangle **2** · square **4**", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Planes of symmetry", steps=[
        dict(say="A plane of symmetry is a flat cut that splits a solid into two congruent halves that are mirror images. A cuboid with three different edge lengths has 3.",
             do=[T("**plane of symmetry**: two mirror-image halves", x=80, y=170), TBL(["Solid", "Planes"], [["cuboid, all edges different", "3"], ["square-based cuboid", "?"], ["cube", "9"], ["cylinder", "infinitely many"]], y=270), ROW(0, 6)]),
        PAUSE("14.3-k2", "Your turn. How many planes of symmetry does a square-based cuboid have, if it is not a cube? Pause the video and try it.", "Planes of a square-based cuboid (not cube)?"),
    ]),
    dict(kind="idea", title="Check: 5", steps=[
        dict(say="5. The square end has 4 lines of symmetry, giving 4 planes along the length. Plus 1 plane halfway along.", do=[TBL(["Solid", "Planes"], [["cuboid, all edges different", "3"], ["square-based cuboid", "5"], ["cube", "9"], ["cylinder", "infinitely many"]], y=170), ROW(0, 0), ROW(1, 0.2), B("4 + 1 = 5", x=760, y=200, color=GREEN)]),
        dict(say="A cube has 9: 3 parallel to the faces, and 6 through opposite edges. A cylinder has infinitely many.", do=[ROW(2, 0.2), ROW(3, 5)]),
    ]),
    dict(kind="method", title="How do I find planes of symmetry?", steps=[
        dict(say="Here is the method. Step 1: look at the end shape, and count its lines of symmetry.", do=[T("1. The **end** shape's lines", x=80, y=170)]),
        dict(say="Step 2: each line gives a plane along the length.", do=[T("2. Each line → a plane **along**", x=80, y=260)]),
        dict(say="Step 3: if the ends match, add a plane halfway along.", do=[T("3. **+1** halfway along", x=80, y=350)]),
        dict(say="Step 4: imagine a mirror on each plane, to check.", do=[T("4. Imagine a **mirror**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Prisms", steps=[
        dict(say="A prism with isosceles triangle ends, not equilateral. The triangle has 1 line of symmetry. Plus 1 halfway along: 2 planes.", do=[MATH("1 + 1 = 2", x=80, y=180)]),
        dict(say="A prism with equilateral triangle ends: 3 lines, plus 1. That makes 4.", do=[MATH("3 + 1 = 4", x=80, y=280)]),
        PAUSE("14.3-k3", "Your turn. How many planes of symmetry does a regular hexagonal prism have? Pause and work it out.", "Planes of a regular hexagonal prism?"),
    ]),
    dict(kind="example", title="Check: 7", steps=[
        dict(say="A regular hexagon has 6 lines of symmetry. Plus 1 halfway along: 7.", do=[B("6 + 1 = 7", x=80, y=190, color=GREEN)]),
        dict(say="A cone has infinitely many: any plane through its point and the centre of its base.", do=[MATH("cone: infinitely many", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Find the planes of symmetry of a 2 by 2 by 5 cuboid. Kit answers. Which line is wrong?", do=LINES("Kit", "2 × 2 × 5 cuboid", ["the square end has 4 lines", "so 4 planes"])),
        dict(say="Line 2 is wrong. He forgot the plane halfway along the length.", do=[dict(a="cross", id="l2")]),
        dict(say="4 plus 1 is 5 planes.", do=[B("5 planes", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Car design", steps=[
        dict(say="Most cars have one plane of symmetry, down the middle. Designers often model one half, then reflect it.", do=[E("🚙", 90, 170, 100), T("design half → **reflect**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("14.3-k4", "One last question. Does a sphere have infinitely many planes of symmetry, or 1 plane? Pause the video and choose.", "A sphere has …"),
        dict(say="Infinitely many. Any plane through the centre cuts it into two mirror-image halves.", do=[B("infinitely many planes", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a plane of symmetry cuts a solid into mirror-image halves.", do=[T("• Mirror-image halves", x=80, y=170)]),
        dict(say="Cuboid 3, square-based cuboid 5, cube 9.", do=[T("• Cuboid 3 · square cuboid 5 · cube 9", x=80, y=250)]),
        dict(say="Prism: the end shape's lines, plus 1.", do=[T("• Prism: lines of the end + 1", x=80, y=330)]),
        dict(say="Cylinders, cones and spheres: infinitely many.", do=[T("• Cylinder, cone, sphere: infinitely many", x=80, y=410)]),
    ]),
]
