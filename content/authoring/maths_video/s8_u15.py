# -*- coding: utf-8 -*-
"""Stage 8 · Unit 15 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG
from .s7_u04 import TBL, ROW
from .s7_u05 import BIG
from .s7_u08 import SVG, POLY, DASH, LINE, TXT, INK

PRISM = lambda a, b, c, x=720, y=130, w=500, at=0: BIG(FIG(x, y, w, at, kind="solid", solid="triprism", a=a, b=b, c=c))
PYR = lambda x=720, y=130, w=480, at=0, **k: BIG(FIG(x, y, w, at, kind="solid", solid="pyramid", **k))
# a parallelogram with its perpendicular height, and the cut-off triangle moved across to make a rectangle
PARA = lambda b, h, slant="": POLY([(30, 230), (220, 230), (290, 90), (100, 90)]) + DASH(100, 90, 100, 230) + TXT(125, 262, b) + TXT(120, 170, h, RED) + (TXT(282, 170, slant, "#667") if slant else "")
RECT = lambda b, h: POLY([(100, 230), (290, 230), (290, 90), (100, 90)]) + POLY([(220, 230), (290, 230), (290, 90)], "#BFE8CF") + TXT(195, 262, b) + TXT(78, 170, h, RED)
TRAP = lambda a, b, h: POLY([(30, 240), (290, 240), (220, 90), (110, 90)]) + DASH(110, 90, 110, 240) + TXT(165, 78, a) + TXT(160, 272, b) + TXT(130, 175, h, RED)

VIDEOS = {}

VIDEOS["15.1"] = [
    dict(kind="hook", title="A road trip", steps=[
        dict(say="A road sign in the UK says: Edinburgh, 45 miles. But the car's trip computer is set to kilometres.", do=[E("🚗", 90, 170, 100), T("road sign: **Edinburgh 45 miles**", x=230, y=200)]),
        dict(say="Is a mile longer or shorter than a kilometre? A useful fact is that 5 miles is about 8 kilometres.", do=[B("5 miles ≈ 8 km", x=230, y=300, color=BLUE)]),
        PAUSE("15.1-k1", "How many kilometres is 45 miles? Pause the video and work it out.", "45 miles in km?"),
    ]),
    dict(kind="hook", title="72 km", steps=[
        dict(say="45 miles is 9 lots of 5 miles. So it is 9 lots of 8 kilometres, which is 72 kilometres.", do=[MATH("45 ÷ 5 = 9", x=80, y=180), B("9 × 8 = 72 km", x=80, y=280, color=GREEN, at=3)]),
    ]),
    dict(kind="recall", title="A fraction of an amount", steps=[
        dict(say="Remember: 8 fifths of 30 is 30 divided by 5, times 8, which is 48. And 5 eighths of 40 is 40 divided by 8, times 5, which is 25.",
             do=[MATH("8/5 of 30 = 30 ÷ 5 × 8 = 48", x=80, y=180), MATH("5/8 of 40 = 40 ÷ 8 × 5 = 25", x=80, y=280, at=6)]),
    ]),
    dict(kind="idea", title="Miles and kilometres", steps=[
        dict(say="A mile is longer than a kilometre. 5 miles is about 8 kilometres.",
             do=[TBL(["miles", "5", "10", "25", "50"], [["km", "8", "16", "40", "80"]], y=170), ROW(0, 2)]),
        dict(say="To change miles to kilometres, divide by 5 and multiply by 8. To change kilometres to miles, divide by 8 and multiply by 5.",
             do=[T("miles → km: **÷ 5 × 8**", x=80, y=330), T("km → miles: **÷ 8 × 5**", x=80, y=410, at=5)]),
        PAUSE("15.1-k2", "Your turn. How many kilometres is 15 miles? Pause the video and try it.", "15 miles in km?"),
    ]),
    dict(kind="idea", title="Check: 15 miles", steps=[
        dict(say="15 divided by 5 is 3, and 3 times 8 is 24 kilometres.", do=[MATH("15 ÷ 5 × 8 = 24 km", x=80, y=190, color=GREEN)]),
        dict(say="For the same distance, the number of kilometres is always bigger, about 1.6 times the miles. Speeds convert the same way: 50 miles per hour is about 80 kilometres per hour.",
             do=[T("km ≈ **1.6 ×** miles", x=80, y=290), MATH("50 mph ≈ 80 km/h", x=80, y=380, at=7)]),
    ]),
    dict(kind="method", title="How do I convert?", steps=[
        dict(say="Here is the method. Step 1: remember that 5 miles is about 8 kilometres.", do=[T("1. **5 miles ≈ 8 km**", x=80, y=170)]),
        dict(say="Step 2: miles to kilometres, divide by 5, then multiply by 8.", do=[T("2. miles → km: ÷ 5 × 8", x=80, y=260)]),
        dict(say="Step 3: kilometres to miles, divide by 8, then multiply by 5.", do=[T("3. km → miles: ÷ 8 × 5", x=80, y=350)]),
        dict(say="Step 4: check. The kilometres should be the bigger number.", do=[T("4. **Check**: km is bigger", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Kilometres to miles", steps=[
        dict(say="Convert 120 kilometres to miles. 120 divided by 8 is 15. 15 times 5 is 75 miles.", do=[MATH("120 ÷ 8 × 5 = 75 miles", x=80, y=200, color=GREEN)]),
        PAUSE("15.1-k3", "Your turn. How many miles is 200 kilometres? Pause and work it out.", "200 km in miles?"),
    ]),
    dict(kind="example", title="Check: 200 km", steps=[
        dict(say="200 divided by 8 is 25. 25 times 5 is 125 miles.", do=[MATH("200 ÷ 8 × 5 = 125 miles", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Which is further?", steps=[
        dict(say="Which is further: 30 miles, or 45 kilometres? 30 miles is 30 divided by 5, times 8, which is 48 kilometres. 48 is more than 45, so 30 miles is further.",
             do=[MATH("30 miles = 48 km", x=80, y=180), B("30 miles is further", x=80, y=290, color=GREEN, at=8)]),
    ]),
    dict(kind="example", title="A speed limit", steps=[
        dict(say="A speed limit is 70 miles per hour. 70 divided by 5 is 14, and 14 times 8 is 112 kilometres per hour.", do=[MATH("70 ÷ 5 × 8 = 112 km/h", x=80, y=200, color=GREEN)]),
        dict(say="For numbers that are not multiples of 5, multiply by 1.6. 13 miles is 13 times 1.6, which is 20.8 kilometres.", do=[MATH("13 × 1.6 = 20.8 km", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ola converts 40 miles to kilometres. Which line is wrong?", do=LINES("Ola", "40 miles in km", ["40 × 5/8 = 25 km"])),
        dict(say="Line 1 is wrong. The kilometres must be the bigger number. She used the wrong fraction.", do=[dict(a="cross", id="l1")]),
        dict(say="40 times 8 fifths is 64 kilometres.", do=[B("40 × 8/5 = 64 km", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Marathons", steps=[
        dict(say="A marathon is about 26.2 miles long. Using 1.6 kilometres per mile, that is about 42 kilometres. The official distance is 42.195 kilometres.",
             do=[E("🏃", 90, 170, 100), MATH("26.2 × 1.6 ≈ 42 km", x=230, y=190, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.1-k4", "One last question. Which is longer: 1 mile or 1 kilometre? Pause the video and choose.", "Longer?"),
        dict(say="1 mile is longer. It is about 1.6 kilometres.", do=[B("1 mile (≈ 1.6 km)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: 5 miles is about 8 kilometres.", do=[T("• 5 miles ≈ 8 km", x=80, y=170)]),
        dict(say="Miles to kilometres, times 8 fifths. Kilometres to miles, times 5 eighths.", do=[T("• miles → km × 8/5 · km → miles × 5/8", x=80, y=250)]),
        dict(say="Kilometres are about 1.6 times the miles.", do=[T("• km ≈ 1.6 × miles", x=80, y=330)]),
        dict(say="Speeds convert in the same way.", do=[T("• Speeds convert the same way", x=80, y=410)]),
    ]),
]

VIDEOS["15.2"] = [
    dict(kind="hook", title="Garden beds", steps=[
        dict(say="A garden has a flower bed shaped like a parallelogram, and a lawn shaped like a trapezium. A trapezium has two parallel sides of different lengths.",
             do=[E("🌷", 90, 170, 100), SVG(PARA("", ""), 560, 120, w=320, at=1), SVG(TRAP("", "", ""), 900, 120, w=320, at=3)]),
        dict(say="Can we find their areas using only rectangles and triangles?", do=[T("use **rectangles** and **triangles**?", x=230, y=200)]),
        PAUSE("15.2-k1", "A parallelogram can be rearranged into which shape? Pause the video and choose.", "A parallelogram can be rearranged into …"),
    ]),
    dict(kind="hook", title="Into a rectangle", steps=[
        dict(say="Cut a right-angled triangle off one end of the parallelogram, and slide it to the other end. You get a rectangle, with the same base and height.",
             do=[SVG(PARA("b", "h"), 500, 120, w=360), SVG(RECT("b", "h"), 880, 120, w=360, at=3), B("a rectangle", x=80, y=200, color=GREEN, at=5)]),
    ]),
    dict(kind="recall", title="Rectangles and triangles", steps=[
        dict(say="Remember: the area of a rectangle is length times width. The area of a triangle is a half, times base, times height. A triangle with base 8 and height 5 has area 20.",
             do=[MATH("rectangle: l × w", x=80, y=170), MATH("triangle: ½ × b × h", x=80, y=260), MATH("½ × 8 × 5 = 20", x=80, y=350, at=8)]),
    ]),
    dict(kind="idea", title="Parallelogram: A = bh", steps=[
        dict(say="So the area of a parallelogram is base times height, just like the rectangle. The height must be the perpendicular height, at right angles to the base. Not the slanting side.",
             do=[B("A = b × h", x=80, y=170, color=BLUE), SVG(PARA("b", "h", "slant"), 760, 120, w=400), T("**perpendicular** height, not the slant", x=80, y=270, color=RED)]),
        PAUSE("15.2-k2", "Your turn. A parallelogram has base 7 and height 3. What is its area? Pause the video and try it.", "Parallelogram b = 7, h = 3. Area?"),
    ]),
    dict(kind="idea", title="Trapezium: A = ½(a + b)h", steps=[
        dict(say="7 times 3 is 21. Now the trapezium. Two identical trapezia, one turned upside down, fit together to make a parallelogram. Its base is a plus b, and its height is h.",
             do=[MATH("7 × 3 = 21", x=80, y=170, color=GREEN), SVG(TRAP("a", "b", "h"), 760, 120, w=400, at=4)]),
        dict(say="So one trapezium is half of that. Add the parallel sides, halve, and multiply by the height.", do=[B("A = ½(a + b)h", x=80, y=280, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I find these areas?", steps=[
        dict(say="Here is the method. Step 1: find the base, or the parallel sides, and the perpendicular height.", do=[T("1. Base (or parallel sides) and **perpendicular height**", x=80, y=170)]),
        dict(say="Step 2: ignore any slanting sides.", do=[T("2. **Ignore** slanting sides", x=80, y=260)]),
        dict(say="Step 3: use A equals b h, or A equals a half, a plus b, times h.", do=[T("3. A = bh  or  A = ½(a + b)h", x=80, y=350)]),
        dict(say="Step 4: give the units squared.", do=[T("4. Units **squared**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A trapezium", steps=[
        dict(say="A trapezium has parallel sides 6 and 10 centimetres, and height 5 centimetres. 6 plus 10 is 16, half of 16 is 8, and 8 times 5 is 40 square centimetres.",
             do=[SVG(TRAP("6 cm", "10 cm", "5 cm"), 760, 120, w=400), MATH("½(6 + 10) × 5 = 8 × 5", x=80, y=190), B("40 cm²", x=80, y=290, color=GREEN, at=9)]),
        PAUSE("15.2-k3", "Your turn. A trapezium has parallel sides 5 and 7, and height 2. What is its area? Pause and work it out.", "Trapezium a = 5, b = 7, h = 2. Area?"),
    ]),
    dict(kind="example", title="Check: the trapezium", steps=[
        dict(say="5 plus 7 is 12. Half of 12 is 6. 6 times 2 is 12.", do=[MATH("½(5 + 7) × 2 = 12", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="A missing side", steps=[
        dict(say="A trapezium has area 63 square centimetres, height 7, and one parallel side of 4. Find the other. 63 equals a half, 4 plus b, times 7. Half of 7 is 3.5, and 63 divided by 3.5 is 18.",
             do=[MATH("63 = ½(4 + b) × 7", x=80, y=180), MATH("4 + b = 18", x=80, y=270, at=8)]),
        dict(say="So b is 14 centimetres.", do=[B("b = 14 cm", x=80, y=370, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A parallelogram has base 10, a slanting side of 6, and height 5. Max finds the area. Which line is wrong?", do=LINES("Max", "base 10, slant 6, height 5", ["A = 10 × 6 = 60 cm²"])),
        dict(say="Line 1 is wrong. He used the slanting side. Use the perpendicular height.", do=[dict(a="cross", id="l1")]),
        dict(say="10 times 5 is 50 square centimetres.", do=[B("A = 10 × 5 = 50 cm²", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Roofs", steps=[
        dict(say="Many roofs have trapezium-shaped sides. To order roof tiles, a builder works out the area of each trapezium.", do=[E("🏠", 90, 170, 100), T("trapezium roof faces → order **tiles**", x=230, y=200)]),
        dict(say="A roof face with parallel edges of 8 and 12 metres, and a slope height of 4 metres, has an area of a half times 20 times 4, which is 40 square metres.", do=[MATH("½ × (8 + 12) × 4 = 40 m²", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.2-k4", "One last question. A parallelogram has area 40 and base 8. What is its height? Pause the video and answer.", "Parallelogram area 40, base 8. Height?"),
        dict(say="40 equals 8 times h. So h is 40 divided by 8, which is 5.", do=[MATH("40 = 8h", x=80, y=190), B("h = 5", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the area of a parallelogram is base times height.", do=[T("• Parallelogram: **A = bh**", x=80, y=170)]),
        dict(say="The area of a trapezium is a half, a plus b, times h.", do=[T("• Trapezium: **A = ½(a + b)h**", x=80, y=250)]),
        dict(say="Always use the perpendicular height.", do=[T("• Always the **perpendicular** height", x=80, y=330)]),
        dict(say="Rearrange to find a missing length.", do=[T("• Rearrange to find a missing length", x=80, y=410)]),
    ]),
]

VIDEOS["15.3"] = [
    dict(kind="hook", title="A tent", steps=[
        dict(say="A ridge tent is a triangular prism. Its end is a triangle 2 metres wide and 1.5 metres high. The tent is 3 metres long.", do=[E("⛺", 90, 170, 100), PRISM("3 m", "2 m", "1.5 m", at=1)]),
        PAUSE("15.3-k1", "How much air is inside the tent, in cubic metres? Pause the video and work it out.", "Tent volume (m³)?"),
    ]),
    dict(kind="hook", title="4.5 cubic metres", steps=[
        dict(say="The triangle's area is a half times 2 times 1.5, which is 1.5 square metres. That triangle runs the whole 3 metres, so the volume is 1.5 times 3, which is 4.5 cubic metres.",
             do=[PRISM("3 m", "2 m", "1.5 m"), MATH("½ × 2 × 1.5 = 1.5 m²", x=80, y=190), B("1.5 × 3 = 4.5 m³", x=80, y=300, color=GREEN, at=8)]),
    ]),
    dict(kind="recall", title="Cuboids", steps=[
        dict(say="Remember: the volume of a cuboid is length times width times height. A 5 by 3 by 2 centimetre cuboid has a volume of 30 cubic centimetres.", do=[MATH("5 × 3 × 2 = 30 cm³", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Prisms", steps=[
        dict(say="A prism has the same cross-section all along its length. Its volume is the area of the cross-section, times the length.", do=[B("V = cross-section area × length", x=80, y=170, color=BLUE)]),
        dict(say="A cuboid is a prism too. For a triangular prism, the volume is a half, times b, times h, times the length.", do=[MATH("triangular prism: V = ½ × b × h × l", x=80, y=280)]),
        PAUSE("15.3-k2", "Your turn. A prism has a cross-section of 5 square metres and a length of 4 metres. What is its volume? Pause the video and try it.", "Cross-section 5 m², length 4 m. V?"),
    ]),
    dict(kind="idea", title="Check: 5 × 4", steps=[
        dict(say="5 times 4 is 20 cubic metres. Volume is measured in cubic units, like cubic centimetres and cubic metres. And 1 litre is 1,000 cubic centimetres.",
             do=[B("20 m³", x=80, y=180, color=GREEN), T("units: cm³, m³ · **1 litre = 1000 cm³**", x=80, y=290)]),
    ]),
    dict(kind="method", title="How do I find the volume?", steps=[
        dict(say="Here is the method. Step 1: find the triangle's base and perpendicular height.", do=[T("1. Triangle's **base** and **height**", x=80, y=170)]),
        dict(say="Step 2: the cross-section area is a half, times b, times h.", do=[T("2. Cross-section = **½bh**", x=80, y=260)]),
        dict(say="Step 3: multiply by the length of the prism.", do=[T("3. × **length**", x=80, y=350)]),
        dict(say="Step 4: write the answer in cubic units.", do=[T("4. **Cubic** units", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A wedge", steps=[
        dict(say="A wedge has a triangular end with base 6 centimetres and height 4. It is 15 centimetres long. The cross-section is a half times 6 times 4, which is 12. The volume is 12 times 15, which is 180 cubic centimetres.",
             do=[PRISM("15 cm", "6 cm", "4 cm"), MATH("½ × 6 × 4 = 12", x=80, y=190), B("12 × 15 = 180 cm³", x=80, y=300, color=GREEN, at=10)]),
        PAUSE("15.3-k3", "Your turn. A triangle with base 4 and height 3 makes a prism 10 long. What is its volume? Pause and work it out.", "Triangle 4 × 3 (b × h), length 10. V?"),
    ]),
    dict(kind="example", title="Check: 4, 3 and 10", steps=[
        dict(say="A half times 4 times 3 is 6. 6 times 10 is 60.", do=[MATH("½ × 4 × 3 × 10 = 60", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="A missing length", steps=[
        dict(say="A prism has a volume of 210 cubic centimetres. Its cross-section is a triangle with base 5 and height 6, so the area is 15. The length is 210 divided by 15, which is 14 centimetres.",
             do=[MATH("½ × 5 × 6 = 15", x=80, y=180), B("210 ÷ 15 = 14 cm", x=80, y=290, color=GREEN, at=9)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A triangular prism has a triangle with base 8 and height 5, and a length of 10. Zoe finds the volume. Which line is wrong?", do=LINES("Zoe", "triangle b 8, h 5; length 10", ["V = 8 × 5 × 10 = 400"])),
        dict(say="Line 1 is wrong. She forgot the half. The cross-section is a triangle, so its area is a half times 8 times 5, which is 20.", do=[dict(a="cross", id="l1")]),
        dict(say="20 times 10 is 200.", do=[B("V = 20 × 10 = 200", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="A water trough", steps=[
        dict(say="A water trough for animals is a triangular prism. Its end has base 40 centimetres and height 30, and it is 150 centimetres long.",
             do=[E("🐴", 90, 170, 100), MATH("½ × 40 × 30 = 600 cm²", x=230, y=190)]),
        dict(say="The volume is 600 times 150, which is 90,000 cubic centimetres. Divide by 1,000: it holds 90 litres of water.", do=[MATH("600 × 150 = 90 000 cm³", x=230, y=290), B("90 litres", x=230, y=390, color=GREEN, at=6)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.3-k4", "One last question. How many litres is 5,000 cubic centimetres? Pause the video and answer.", "5000 cm³ in litres?"),
        dict(say="1 litre is 1,000 cubic centimetres. 5,000 divided by 1,000 is 5 litres.", do=[B("5 litres", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the volume of a prism is the cross-section area times the length.", do=[T("• Prism: V = cross-section × length", x=80, y=170)]),
        dict(say="A triangle cross-section has area a half b h.", do=[T("• Triangle: ½bh", x=80, y=250)]),
        dict(say="Rearrange to find a missing length.", do=[T("• Rearrange for a missing length", x=80, y=330)]),
        dict(say="1 litre is 1,000 cubic centimetres.", do=[T("• 1 litre = 1000 cm³", x=80, y=410)]),
    ]),
]

VIDEOS["15.4"] = [
    dict(kind="hook", title="Making a gift box", steps=[
        dict(say="A gift box is a triangular prism. You want to know how much card is needed to make it.", do=[E("🎁", 90, 170, 100), PRISM("", "", "", at=1)]),
        dict(say="How many faces does it have, and what shapes are they?", do=[T("how many **faces**? what **shapes**?", x=230, y=200)]),
        PAUSE("15.4-k1", "What are the faces of a triangular prism? Pause the video and choose.", "Faces of a triangular prism?"),
    ]),
    dict(kind="hook", title="Five faces", steps=[
        dict(say="It has 2 triangles, one at each end, and 3 rectangles round the sides. That is 5 faces.", do=[PRISM("", "", ""), B("2 triangles + 3 rectangles", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="recall", title="Nets", steps=[
        dict(say="Remember: a net is a flat shape that folds up to make a solid. It shows every face.", do=[T("a **net** folds up into the solid", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Surface area of a prism", steps=[
        dict(say="The surface area is the total area of all the faces. Here is a prism whose ends are right-angled triangles with sides 3, 4 and 5 centimetres. It is 10 centimetres long.",
             do=[TBL(["Face", "Area (cm²)"], [["2 triangles", "2 × ½ × 3 × 4 = 12"], ["rectangle 3 × 10", "30"], ["rectangle 4 × 10", "40"], ["rectangle 5 × 10", "50"], ["total", "132"]], y=170), ROW(0, 7)]),
        dict(say="The three rectangles are 30, 40 and 50. Add everything: 12 plus 120 is 132 square centimetres.", do=[ROW(1, 0.3), ROW(2, 1.2), ROW(3, 2.1), ROW(4, 5)]),
    ]),
    dict(kind="idea", title="Pyramids", steps=[
        dict(say="A pyramid has a base, and triangular faces that meet at a point. A square-based pyramid has 1 square and 4 identical triangles. A tetrahedron has 4 triangles.",
             do=[PYR(), T("square-based: **1 square + 4 triangles**", x=80, y=180), T("tetrahedron: **4 triangles**", x=80, y=260, at=7)]),
        dict(say="For each triangle, use its slant height: the height of the triangle face, not the height of the pyramid.", do=[T("use the **slant height** of each face", x=80, y=350, color=RED)]),
        PAUSE("15.4-k2", "Your turn. How many faces does a square-based pyramid have? Pause the video and try it.", "Faces of a square-based pyramid?"),
    ]),
    dict(kind="idea", title="Check: 5 faces", steps=[
        dict(say="1 square base, plus 4 triangles, makes 5 faces.", do=[B("5 faces", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I find a surface area?", steps=[
        dict(say="Here is the method. Step 1: sketch the net, or list the faces.", do=[T("1. Sketch the **net** or list the faces", x=80, y=170)]),
        dict(say="Step 2: find the area of each face. Triangles need a half b h.", do=[T("2. Area of each face (triangles: **½bh**)", x=80, y=260)]),
        dict(say="Step 3: group the identical faces.", do=[T("3. Group **identical** faces", x=80, y=350)]),
        dict(say="Step 4: add them all, and give the units squared.", do=[T("4. **Add** them; units squared", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A pyramid", steps=[
        dict(say="A square-based pyramid has a base of side 4 centimetres. Each triangle has a slant height of 6. The base is 4 times 4, which is 16. Each triangle is a half times 4 times 6, which is 12. 4 triangles make 48.",
             do=[PYR(), MATH("base: 4 × 4 = 16", x=80, y=180), MATH("triangles: 4 × ½ × 4 × 6 = 48", x=80, y=270, at=6)]),
        dict(say="The total is 16 plus 48, which is 64 square centimetres.", do=[B("16 + 48 = 64 cm²", x=80, y=370, color=GREEN)]),
        PAUSE("15.4-k3", "Your turn. A square base of side 6 has triangles with slant height 5. What is the surface area? Pause and work it out.", "Square base 6, slant 5. Surface area?"),
    ]),
    dict(kind="example", title="Check: base 6, slant 5", steps=[
        dict(say="The base is 36. Each triangle is a half times 6 times 5, which is 15. 4 triangles make 60. 36 plus 60 is 96.", do=[MATH("36 + 4 × 15 = 96", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="A tent with no floor", steps=[
        dict(say="A tent has triangular ends with base 2 metres and height 1.5. Its two sloping sides are 1.8 by 3 metres. It has no floor. The two ends make 3 square metres. The two sides make 10.8. In total, 13.8 square metres of fabric.",
             do=[MATH("ends: 2 × ½ × 2 × 1.5 = 3", x=80, y=180), MATH("sides: 2 × 1.8 × 3 = 10.8", x=80, y=270, at=6), B("13.8 m²", x=80, y=370, color=GREEN, at=11)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A prism has triangles of a half times 4 times 3, and rectangles of 40, 30 and 50. Raj adds up the surface area. Which line is wrong?", do=LINES("Raj", "triangles ½ × 4 × 3; rectangles 40, 30, 50", ["6 + 40 + 30 + 50 = 126"])),
        dict(say="Line 1 is wrong. There are two triangular ends, not one.", do=[dict(a="cross", id="l1")]),
        dict(say="2 times 6 is 12, plus 120 is 132.", do=[B("12 + 120 = 132", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Packaging", steps=[
        dict(say="Some chocolate bars are sold in triangular prism boxes. Designers work out the surface area to know how much card each box needs.", do=[E("🍫", 90, 170, 100), T("surface area → how much **card** per box", x=230, y=200)]),
        dict(say="Saving even a few square centimetres per box adds up to a lot of card over millions of boxes.", do=[T("small savings × millions of boxes", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.4-k4", "One last question. How many faces does a tetrahedron have? Pause the video and answer.", "Faces of a tetrahedron?"),
        dict(say="A tetrahedron has 4 faces. They are all triangles.", do=[B("4", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: surface area is the total area of all the faces.", do=[T("• Surface area = the sum of all face areas", x=80, y=170)]),
        dict(say="A triangular prism has 2 triangles and 3 rectangles.", do=[T("• Triangular prism: 2 triangles + 3 rectangles", x=80, y=250)]),
        dict(say="A pyramid has a base plus triangles. Use the slant heights.", do=[T("• Pyramid: base + triangles (slant heights)", x=80, y=330)]),
        dict(say="A net helps you not to miss a face.", do=[T("• A net helps you not miss a face", x=80, y=410)]),
    ]),
]
