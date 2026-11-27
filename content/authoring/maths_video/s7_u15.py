# -*- coding: utf-8 -*-
"""Stage 7 · Unit 15 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG
from .s7_u04 import TBL, ROW
from .s7_u05 import BIG, SHAPE
from .s7_u08 import SVG, POLY, DASH, TXT, LINE

BOX3 = lambda a, b, c, x=680, y=130, w=540, at=0: BIG(FIG(x, y, w, at, kind="solid", solid="cuboid", a=a, b=b, c=c))
SQM = SVG(POLY([(50, 40), (270, 40), (270, 260), (50, 260)]) + TXT(160, 292, "1 m = 100 cm") + TXT(160, 160, "1 m²", "#3B7DD8", 34), 800, 150, 380)   # a 1 m square
HALF = lambda bx, by: POLY([(40, 260), (280, 260), (280, 60), (40, 60)], "#F3F4F6") + POLY([(40, 260), (280, 260), (110, 60)]) + DASH(110, 60, 110, 260) + TXT(160, 292, bx) + TXT(90, 170, by, "#D64545")

VIDEOS = {}

VIDEOS["15.1"] = [
    dict(kind="hook", title="Tiling a floor", steps=[
        dict(say="A shop sells floor tiles priced for each square metre. But your floor plan is in square centimetres. The floor is 180,000 square centimetres.", do=[E("🧱", 90, 150, 110), T("floor: **180 000 cm²** · price per **m²**", x=240, y=190)]),
        PAUSE("15.1-k1", "How many square metres is that? Be careful: it is not 1,800. Pause the video and work it out.", "180 000 cm² = ? m²"),
    ]),
    dict(kind="hook", title="Not 1800", steps=[
        dict(say="1 metre is 100 centimetres. But 1 square metre is 100 centimetres by 100 centimetres. That is 10,000 square centimetres.", do=[SQM, MATH("100 × 100 = 10 000", x=80, y=180)]),
        dict(say="So divide by 10,000, not by 100. 180,000 divided by 10,000 is 18 square metres.", do=[MATH("180 000 ÷ 10 000 = 18", x=80, y=290), B("18 m²", x=80, y=390, color=GREEN, at=5)]),
    ]),
    dict(kind="recall", title="Length conversions", steps=[
        dict(say="Remember the length facts. 1 centimetre is 10 millimetres. 1 metre is 100 centimetres. 1 kilometre is 1,000 metres.", do=[MATH("1 cm = 10 mm", x=80, y=170), MATH("1 m = 100 cm", x=80, y=260, at=3), MATH("1 km = 1000 m", x=80, y=350, at=6)]),
    ]),
    dict(kind="idea", title="Why area is different", steps=[
        dict(say="For an area, the length fact is used 2 times: once for the length, and once for the width. So you square the number.", do=[T("area uses the length fact **twice** → **square** it", x=80, y=150)]),
        dict(say="1 centimetre is 10 millimetres. So 1 square centimetre is 10 times 10, which is 100 square millimetres.",
             do=[TBL(["Length", "Area"], [["1 cm = 10 mm", "1 cm² = 10 × 10 = 100 mm²"], ["1 m = 100 cm", "1 m² = 100 × 100 = 10 000 cm²"], ["1 km = 1000 m", "1 km² = 1000 × 1000 = 1 000 000 m²"]], y=240), ROW(0, 0.3)]),
        dict(say="1 square metre is 10,000 square centimetres. And 1 square kilometre is 1 million square metres.", do=[ROW(1, 0.3), ROW(2, 4)]),
        PAUSE("15.1-k2", "Your turn. Change 2 square metres to square centimetres. Pause the video and try it.", "Change 2 m² to cm²."),
    ]),
    dict(kind="idea", title="Check: 2 m² in cm²", steps=[
        dict(say="Each square metre is 10,000 square centimetres. 2 times 10,000 is 20,000 square centimetres.", do=[MATH("2 × 10 000 = 20 000 cm²", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Multiply or divide?", steps=[
        dict(say="Going from a bigger unit to a smaller unit, you need more of them. So multiply. 4.5 square metres is 45,000 square centimetres.", do=[T("bigger unit → smaller unit: **multiply**", x=80, y=160), MATH("4.5 m² = 4.5 × 10 000 = 45 000 cm²", x=80, y=240, at=5)]),
        dict(say="Going from a smaller unit to a bigger unit, you need fewer. So divide. 730 square millimetres is 7.3 square centimetres.", do=[T("smaller unit → bigger unit: **divide**", x=80, y=370), MATH("730 mm² = 730 ÷ 100 = 7.3 cm²", x=80, y=450, at=5)]),
        PAUSE("15.1-k3", "Your turn. Change 850 square millimetres to square centimetres. Pause the video and try it.", "Change 850 mm² to cm²."),
    ]),
    dict(kind="idea", title="Check: 850 mm² in cm²", steps=[
        dict(say="100 square millimetres make 1 square centimetre. 850 divided by 100 is 8.5 square centimetres.", do=[MATH("850 ÷ 100 = 8.5 cm²", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I convert area units?", steps=[
        dict(say="Here is the method. Step 1: write the length fact. For example, 1 metre is 100 centimetres.", do=[T("1. Write the **length** fact", x=80, y=170)]),
        dict(say="Step 2: square it, to get the area fact. 1 square metre is 10,000 square centimetres.", do=[T("2. **Square** it for area", x=80, y=260)]),
        dict(say="Step 3: to a smaller unit, multiply. To a bigger unit, divide.", do=[T("3. Smaller unit: **multiply** · bigger unit: **divide**", x=80, y=350)]),
        dict(say="Step 4: check that the size of your answer makes sense.", do=[T("4. Does the **size** make sense?", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Square metres to square centimetres", steps=[
        dict(say="Change 0.6 square metres to square centimetres.", do=[B("0.6 m²", x=80, y=160)]),
        dict(say="Going to a smaller unit, so multiply by 10,000. The answer is 6,000 square centimetres.", do=[MATH("0.6 × 10 000 = 6000", x=80, y=280), B("6000 cm²", x=80, y=380, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="Mixed units", steps=[
        dict(say="A rug is 1.5 metres long and 40 centimetres wide. Find its area in square metres.", do=[T("**1.5 m** by **40 cm** · area in m²?", x=80, y=160)]),
        dict(say="Make the units the same before you multiply. 40 centimetres is 0.4 metres.", do=[MATH("40 cm = 0.4 m", x=80, y=270)]),
        dict(say="1.5 times 0.4 is 0.6. The area is 0.6 square metres.", do=[MATH("1.5 × 0.4 = 0.6", x=80, y=360), B("0.6 m²", x=80, y=450, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Painting a wall", steps=[
        dict(say="1 litre of paint covers 10 square metres. A wall measures 500 centimetres by 280 centimetres. How much paint is needed?", do=[E("🖌️", 90, 140, 80), T("wall **500 cm × 280 cm** · 1 litre covers **10 m²**", x=200, y=160)]),
        dict(say="Change the lengths to metres first: 5 metres by 2.8 metres. The area is 14 square metres.", do=[MATH("5 × 2.8 = 14 m²", x=80, y=290)]),
        dict(say="14 divided by 10 is 1.4. You need 1.4 litres of paint.", do=[MATH("14 ÷ 10 = 1.4", x=80, y=380), B("1.4 litres", x=80, y=470, color=GREEN, at=3)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Change 3 square metres to square centimetres. Here is Pita's working. Which line goes wrong first?", do=LINES("Pita", "change 3 m² to cm²", ["1 m = 100 cm", "so 3 m² = 3 × 100 = 300 cm²"])),
        dict(say="Line 2 is wrong. 100 is the fact for length. For area, you must square it: 1 square metre is 10,000 square centimetres.", do=[dict(a="cross", id="l2")]),
        dict(say="3 times 10,000 is 30,000 square centimetres.", do=[B("3 × 10 000 = 30 000 cm²", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Paper sizes", steps=[
        dict(say="Paper sizes are built on area. The largest sheet, called A0, has an area of exactly 1 square metre.", do=[E("📄", 90, 160, 100), T("A0 paper: exactly **1 m²**", x=230, y=190)]),
        dict(say="Fold it in half 4 times, and you get 16 sheets of A4, the paper in your printer.", do=[T("A0 = **16** sheets of A4", x=230, y=300)]),
        dict(say="So 1 sheet of A4 is 10,000 divided by 16. That is about 625 square centimetres.", do=[MATH("10 000 ÷ 16 = 625 cm²", x=230, y=400, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.1-k4", "One last question. A tile is 50 centimetres by 50 centimetres. What is its area in square metres? Pause the video and work it out.", "50 cm × 50 cm in m²?"),
        dict(say="Change to metres first. 50 centimetres is 0.5 metres. 0.5 times 0.5 is 0.25 square metres.", do=[MATH("0.5 × 0.5 = 0.25", x=80, y=190), B("0.25 m²", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: 1 square centimetre is 100 square millimetres. 1 square metre is 10,000 square centimetres.", do=[T("• 1 cm² = **100** mm² · 1 m² = **10 000** cm²", x=80, y=170)]),
        dict(say="Square the length fact to get the area fact.", do=[T("• **Square** the length fact", x=80, y=250)]),
        dict(say="To a smaller unit, multiply. To a bigger unit, divide.", do=[T("• Smaller unit: **multiply** · bigger unit: **divide**", x=80, y=330)]),
        dict(say="Make the units the same before you multiply lengths.", do=[T("• Use the **same units** before multiplying", x=80, y=410)]),
    ]),
]

VIDEOS["15.2"] = [
    dict(kind="hook", title="How big is a farm?", steps=[
        dict(say="An advert says that a farm has 35 hectares of land. To picture that, think of a football pitch. A pitch is about 100 metres by 70 metres.", do=[E("🚜", 90, 150, 110), T("farm: **35 hectares** · pitch: about **100 m × 70 m**", x=240, y=190)]),
        PAUSE("15.2-k1", "First, what is the area of the football pitch, in square metres? Pause the video and work it out.", "A 100 m × 70 m pitch is how many m²?"),
    ]),
    dict(kind="hook", title="Pitches on the farm", steps=[
        dict(say="100 times 70 is 7,000 square metres.", do=[MATH("100 × 70 = 7000 m²", x=80, y=180, color=GREEN)]),
        dict(say="1 hectare is 10,000 square metres. So 35 hectares is 350,000 square metres.", do=[MATH("35 ha = 350 000 m²", x=80, y=280)]),
        dict(say="350,000 divided by 7,000 is 50. The farm is as big as 50 football pitches.", do=[MATH("350 000 ÷ 7000 = 50", x=80, y=370), B("50 pitches", x=80, y=460, color=BLUE, at=4)]),
    ]),
    dict(kind="recall", title="Area of a rectangle", steps=[
        dict(say="Remember: the area of a rectangle is the length times the width. A field 250 metres by 80 metres has an area of 20,000 square metres.", do=[B("area = length × width", x=80, y=170), MATH("250 × 80 = 20 000 m²", x=80, y=290, at=3)]),
    ]),
    dict(kind="idea", title="The hectare", steps=[
        dict(say="Land is measured in hectares. 1 hectare is the area of a square, 100 metres by 100 metres. That is 10,000 square metres.", do=[SVG(POLY([(50, 40), (270, 40), (270, 260), (50, 260)], "#BFE8CF") + TXT(160, 292, "100 m") + TXT(160, 160, "1 ha", "#1F9D61", 34), 800, 150, 380), B("1 ha = 10 000 m²", x=80, y=170, color=BLUE)]),
        dict(say="The short way to write hectares is h a. A football pitch is about 0.7 hectares.", do=[T("football pitch ≈ **0.7 ha**", x=80, y=290)]),
        dict(say="To change hectares into square metres, multiply by 10,000.", do=[T("ha → m²: **× 10 000**", x=80, y=390)]),
        PAUSE("15.2-k2", "Your turn. Change 3 hectares to square metres. Pause the video and try it.", "Change 3 ha to m²."),
    ]),
    dict(kind="idea", title="Check: 3 hectares", steps=[
        dict(say="3 times 10,000 is 30,000 square metres.", do=[MATH("3 × 10 000 = 30 000 m²", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Square metres to hectares", steps=[
        dict(say="To change square metres into hectares, divide by 10,000. 85,000 square metres is 8.5 hectares.", do=[T("m² → ha: **÷ 10 000**", x=80, y=160), MATH("85 000 ÷ 10 000 = 8.5 ha", x=80, y=250, at=3)]),
        dict(say="To find the area of a field in hectares, first find its area in square metres. Then divide.", do=[T("first find the area in **m²**, then divide", x=80, y=380)]),
        PAUSE("15.2-k3", "Your turn. A field is 200 metres by 250 metres. What is its area in hectares? Pause the video and try it.", "A field 200 m × 250 m. What is its area in hectares?"),
    ]),
    dict(kind="idea", title="Check: the field", steps=[
        dict(say="200 times 250 is 50,000 square metres. Divide by 10,000. The field is 5 hectares.", do=[MATH("200 × 250 = 50 000 m²", x=80, y=190), MATH("50 000 ÷ 10 000 = 5 ha", x=80, y=280, at=3, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I work with hectares?", steps=[
        dict(say="Here is the method. Step 1: find the area in square metres. The lengths must be in metres.", do=[T("1. Area in **m²** (lengths in metres)", x=80, y=170)]),
        dict(say="Step 2: divide by 10,000 to get hectares.", do=[T("2. **÷ 10 000** → hectares", x=80, y=260)]),
        dict(say="Step 3: to go from hectares to square metres, multiply by 10,000.", do=[T("3. Hectares → m²: **× 10 000**", x=80, y=350)]),
        dict(say="Step 4: check with something you know. A football pitch is about 0.7 hectares.", do=[T("4. Check: a pitch is about **0.7 ha**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A rectangular field", steps=[
        dict(say="A field is 300 metres by 180 metres. Find its area in hectares.", do=[T("field: **300 m × 180 m**", x=80, y=160)]),
        dict(say="300 times 180 is 54,000 square metres.", do=[MATH("300 × 180 = 54 000 m²", x=80, y=270)]),
        dict(say="Divide by 10,000. The field is 5.4 hectares.", do=[MATH("54 000 ÷ 10 000 = 5.4", x=80, y=360), B("5.4 ha", x=80, y=450, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Lengths in kilometres", steps=[
        dict(say="A forest is a rectangle, 1.5 kilometres by 0.8 kilometres. Find its area in hectares.", do=[E("🌲", 90, 140, 80), T("forest: **1.5 km × 0.8 km**", x=200, y=160)]),
        dict(say="Change to metres first: 1,500 metres by 800 metres. The area is 1,200,000 square metres.", do=[MATH("1500 × 800 = 1 200 000 m²", x=80, y=280)]),
        dict(say="Divide by 10,000. The forest is 120 hectares.", do=[MATH("1 200 000 ÷ 10 000 = 120", x=80, y=370), B("120 ha", x=80, y=460, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Finding a length", steps=[
        dict(say="A rectangular field has an area of 3.6 hectares. It is 300 metres long. How wide is it?", do=[T("area **3.6 ha** · length **300 m** · width?", x=80, y=160)]),
        dict(say="3.6 hectares is 36,000 square metres.", do=[MATH("3.6 ha = 36 000 m²", x=80, y=270)]),
        dict(say="Divide the area by the length. 36,000 divided by 300 is 120. The field is 120 metres wide.", do=[MATH("36 000 ÷ 300 = 120", x=80, y=360), B("120 m", x=80, y=450, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="The price of land", steps=[
        dict(say="Land costs 6,000 dollars for each hectare. Find the price of a plot that is 500 metres by 140 metres.", do=[T("**$6000 per hectare** · plot: **500 m × 140 m**", x=80, y=160)]),
        dict(say="500 times 140 is 70,000 square metres. That is 7 hectares.", do=[MATH("500 × 140 = 70 000 m² = 7 ha", x=80, y=270)]),
        dict(say="7 times 6,000 is 42,000 dollars.", do=[MATH("7 × 6000 = 42 000", x=80, y=360), B("$42 000", x=80, y=450, color=GREEN, at=2.6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Change 62,000 square metres to hectares. Here is Yuri's working. Which line goes wrong first?", do=LINES("Yuri", "change 62 000 m² to hectares", ["1 ha = 100 m²", "62 000 ÷ 100 = 620 ha"])),
        dict(say="Line 1 is wrong. 1 hectare is 100 metres by 100 metres. That is 10,000 square metres, not 100.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="62,000 divided by 10,000 is 6.2 hectares.", do=[B("62 000 ÷ 10 000 = 6.2 ha", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Hectares on the map", steps=[
        dict(say="The smallest country in the world is Vatican City, inside Rome. Its area is only about 44 hectares.", do=[E("⛪", 90, 160, 100), T("Vatican City: about **44 hectares**", x=230, y=190)]),
        dict(say="That is less than half a square kilometre. You could walk across it in about 10 minutes.", do=[MATH("44 ha = 0.44 km²", x=230, y=300)]),
        dict(say="Central Park, in New York, is much bigger: about 340 hectares. Almost 8 Vatican Cities would fit inside it.", do=[E("🌳", 90, 420, 100), T("Central Park: about **340 hectares**", x=230, y=450)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.2-k4", "One last question. How many hectares are there in 1 square kilometre? Pause the video and work it out.", "How many hectares in 1 km²?"),
        dict(say="1 square kilometre is 1,000 metres by 1,000 metres: 1 million square metres. Divide by 10,000. That is 100 hectares.", do=[MATH("1000 × 1000 = 1 000 000 m²", x=80, y=190), MATH("1 000 000 ÷ 10 000 = 100", x=80, y=280, at=5), B("100 ha = 1 km²", x=80, y=380, color=GREEN, at=8)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: 1 hectare is 10,000 square metres. It is a square 100 metres by 100 metres.", do=[T("• **1 ha = 10 000 m²** (100 m × 100 m)", x=80, y=170)]),
        dict(say="Square metres to hectares: divide by 10,000. Hectares to square metres: multiply by 10,000.", do=[T("• m² → ha: **÷ 10 000** · ha → m²: **× 10 000**", x=80, y=250)]),
        dict(say="100 hectares make 1 square kilometre.", do=[T("• **100 ha = 1 km²**", x=80, y=330)]),
        dict(say="Always work out the area in square metres first.", do=[T("• Work out the area in **m²** first", x=80, y=410)]),
    ]),
]

VIDEOS["15.3"] = [
    dict(kind="hook", title="A sail", steps=[
        dict(say="A sailmaker is making a triangular sail. Its base is 4 metres, and its height is 6 metres.", do=[E("⛵", 90, 150, 110), T("base **4 m** · height **6 m**", x=240, y=190)]),
        PAUSE("15.3-k1", "How much fabric is needed? Here is a hint: think about the rectangle that fits around the sail. Pause the video and work it out.", "A triangular sail has base 4 m and height 6 m. What is its area in m²?"),
    ]),
    dict(kind="hook", title="Half the rectangle", steps=[
        dict(say="Draw a rectangle around the sail. It is 4 metres by 6 metres, so its area is 24 square metres.", do=[SVG(HALF("4 m", "6 m"), 800, 150, 380), MATH("4 × 6 = 24 m²", x=80, y=180)]),
        dict(say="The triangle fills exactly half of the rectangle. Half of 24 is 12. The sail needs 12 square metres of fabric.", do=[MATH("24 ÷ 2 = 12", x=80, y=280), B("12 m²", x=80, y=380, color=GREEN, at=5)]),
    ]),
    dict(kind="recall", title="Area of a rectangle", steps=[
        dict(say="Remember: the area of a rectangle is the length times the width.", do=[B("area = length × width", x=80, y=180)]),
    ]),
    dict(kind="idea", title="Half a rectangle", steps=[
        dict(say="Any triangle fits inside a rectangle with the same base and the same height. And it always takes up exactly half of it.", do=[SVG(HALF("base", "height"), 800, 150, 380), T("a triangle is **half** of its rectangle", x=80, y=170)]),
        dict(say="So the area of a triangle is a half, times the base, times the height.", do=[MATH("$$\\text{area} = \\tfrac{1}{2} \\times \\text{base} \\times \\text{height}$$", x=80, y=280, color=BLUE)]),
        dict(say="The answer is in square units, like square centimetres or square metres.", do=[T("units: **cm²**, **m²**", x=80, y=420)]),
        PAUSE("15.3-k2", "Your turn. A triangle has a base of 9 centimetres and a height of 4 centimetres. What is its area? Pause the video and try it.", "Base 9 cm, height 4 cm. What is the area?"),
    ]),
    dict(kind="idea", title="Check: base 9, height 4", steps=[
        dict(say="9 times 4 is 36. Half of 36 is 18. The area is 18 square centimetres.", do=[MATH("$$\\tfrac{1}{2} \\times 9 \\times 4 = 18$$", x=80, y=180), B("18 cm²", x=80, y=320, color=GREEN, at=3)]),
    ]),
    dict(kind="idea", title="Which height?", steps=[
        dict(say="The height must be perpendicular to the base. That means it meets the base at a right angle. It is not a slanted side.", do=[SVG(POLY([(40, 260), (280, 260), (110, 60)]) + DASH(110, 60, 110, 260) + f'<path d="M110 244 h16 v16" fill="none" stroke="#D64545" stroke-width="3"/>' + TXT(160, 292, "base") + TXT(150, 170, "height", "#D64545"), 800, 150, 380), T("the height is **perpendicular** to the base", x=80, y=170)]),
        dict(say="Any side can be the base, as long as you use the height that goes with it.", do=[T("any side can be the **base**", x=80, y=270)]),
        dict(say="In some triangles, the height falls outside the triangle. You still use a half, times base, times height.", do=[T("the height can be **outside** the triangle", x=80, y=370)]),
    ]),
    dict(kind="method", title="How do I find the area of a triangle?", steps=[
        dict(say="Here is the method. Step 1: choose a base.", do=[T("1. Choose a **base**", x=80, y=170)]),
        dict(say="Step 2: find the perpendicular height to that base.", do=[T("2. Find the **perpendicular height**", x=80, y=260)]),
        dict(say="Step 3: work out a half, times base, times height.", do=[T("3. **½ × base × height**", x=80, y=350)]),
        dict(say="Step 4: ignore any slanted side that is not the height.", do=[T("4. **Ignore** slanted sides", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A right-angled triangle", steps=[
        dict(say="A right-angled triangle has shorter sides of 9 centimetres and 6 centimetres. Find its area.", do=[SHAPE([[0, 0], [9, 0], [0, 6]], x=700, y=120, w=500, s=["9 cm", "", "6 cm"], right=[0])]),
        dict(say="The 2 shorter sides meet at a right angle. So one is the base, and the other is the height.", do=[T("the shorter sides are the **base** and **height**", x=80, y=180)]),
        dict(say="A half times 9 times 6 is 27 square centimetres.", do=[MATH("$$\\tfrac{1}{2} \\times 9 \\times 6 = 27$$", x=80, y=280), B("27 cm²", x=80, y=420, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Ignore the slanted side", steps=[
        dict(say="A triangle has a base of 14 centimetres, a slanted side of 11 centimetres, and a perpendicular height of 9 centimetres. Find its area.", do=[T("base **14 cm** · slanted side 11 cm · height **9 cm**", x=80, y=160)]),
        dict(say="Use the base, 14, and the height, 9. Do not use the slanted side.", do=[T("use **14** and **9**, not 11", x=80, y=270, color=RED)]),
        dict(say="A half times 14 times 9 is 63 square centimetres.", do=[MATH("$$\\tfrac{1}{2} \\times 14 \\times 9 = 63$$", x=80, y=350), B("63 cm²", x=80, y=490, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Finding the height", steps=[
        dict(say="A triangle has an area of 36 square centimetres, and a base of 9 centimetres. Find its height.", do=[T("area **36 cm²** · base **9 cm** · height?", x=80, y=160)]),
        dict(say="Half of the base is 4.5. So 4.5 times the height is 36.", do=[MATH("4.5 × h = 36", x=80, y=270)]),
        dict(say="36 divided by 4.5 is 8. The height is 8 centimetres.", do=[MATH("h = 36 ÷ 4.5 = 8", x=80, y=360), B("8 cm", x=80, y=450, color=GREEN, at=3)]),
        PAUSE("15.3-k3", "Your turn. A triangle has an area of 40 square centimetres, and a base of 16 centimetres. What is its height? Pause the video and try it.", "Area 40 cm², base 16 cm. What is the height?"),
    ]),
    dict(kind="example", title="Check: area 40, base 16", steps=[
        dict(say="Half of 16 is 8. So 8 times the height is 40. The height is 40 divided by 8, which is 5 centimetres.", do=[MATH("8 × h = 40", x=80, y=190), MATH("h = 40 ÷ 8 = 5", x=80, y=280, at=3), B("5 cm", x=80, y=380, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="A shape made of two parts", steps=[
        dict(say="A sign has the shape of a house. It is a rectangle, 8 metres by 5 metres, with a triangle on top. The triangle has a base of 8 metres and a height of 3 metres.",
             do=[SVG(POLY([(60, 150), (260, 150), (260, 275), (60, 275)]) + POLY([(60, 150), (260, 150), (160, 75)], "#BFE8CF") + TXT(160, 305, "8 m") + TXT(30, 220, "5 m") + DASH(160, 75, 160, 150) + TXT(192, 125, "3 m", "#D64545"), 800, 130, 400)]),
        dict(say="The rectangle is 8 times 5, which is 40 square metres. The triangle is a half times 8 times 3, which is 12 square metres.", do=[MATH("rectangle: 8 × 5 = 40", x=80, y=200), MATH("triangle: ½ × 8 × 3 = 12", x=80, y=290, at=4)]),
        dict(say="Add them. The total area is 52 square metres.", do=[MATH("40 + 12 = 52", x=80, y=400), B("52 m²", x=80, y=490, color=GREEN, at=2.4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A triangle has a base of 12 centimetres, a sloping side of 15 centimetres, and a height of 9 centimetres. Find its area. Here is Ana's working. Is it right?",
             do=LINES("Ana", "base 12 cm, sloping side 15 cm, height 9 cm", ["½ × 12 × 15 = 90"])),
        dict(say="Line 1 is wrong. 15 centimetres is the sloping side. It is not the perpendicular height.", do=[dict(a="cross", id="l1")]),
        dict(say="Use the height, 9. A half times 12 times 9 is 54 square centimetres.", do=[B("½ × 12 × 9 = 54 cm²", x=110, y=340, color=GREEN)]),
    ]),
    dict(kind="life", title="Triangles that tower", steps=[
        dict(say="Each face of the Great Pyramid in Egypt is a huge triangle. Its base is about 230 metres. Its height, measured up the slope, is about 186 metres.", do=[E("🔺", 90, 160, 100), T("base ≈ **230 m** · slope height ≈ **186 m**", x=230, y=190)]),
        dict(say="A half times 230 times 186 is about 21,400 square metres.", do=[MATH("½ × 230 × 186 ≈ 21 400 m²", x=230, y=300)]),
        dict(say="That is more than 2 hectares of stone, on just 1 face.", do=[B("more than 2 hectares", x=230, y=410, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.3-k4", "One last question. A right-angled triangle has shorter sides of 6 and 7. What is its area? Pause the video and answer.", "A right-angled triangle has shorter sides 6 and 7. What is its area?"),
        dict(say="6 times 7 is 42. Half of 42 is 21. The area is 21 square units.", do=[MATH("$$\\tfrac{1}{2} \\times 6 \\times 7 = 21$$", x=80, y=180), B("21", x=80, y=320, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the area of a triangle is a half, times the base, times the perpendicular height.", do=[T("• Area = **½ × base × height**", x=80, y=170)]),
        dict(say="The height is at right angles to the base.", do=[T("• The height is at **right angles** to the base", x=80, y=250)]),
        dict(say="Any side can be the base, with its matching height.", do=[T("• Any side can be the base", x=80, y=330)]),
        dict(say="Work backwards to find a missing base or height.", do=[T("• Work **backwards** for a missing length", x=80, y=410)]),
    ]),
]

VIDEOS["15.4"] = [
    dict(kind="hook", title="Packing a box", steps=[
        dict(say="A delivery box is 30 centimetres long, 20 centimetres wide and 10 centimetres high. You want to fill it with sugar cubes. Each cube is 1 centimetre along every edge.", do=[BOX3("30 cm", "20 cm", "10 cm"), T("fill it with **1 cm cubes**", x=80, y=180)]),
        PAUSE("15.4-k1", "How many sugar cubes fit in the box? Pause the video and work it out.", "How many 1 cm cubes fit in a 30 × 20 × 10 cm box?"),
    ]),
    dict(kind="hook", title="Layer by layer", steps=[
        dict(say="Fill the bottom layer first. It has 30 rows of 20 cubes. That is 600 cubes.", do=[BOX3("30 cm", "20 cm", "10 cm"), MATH("30 × 20 = 600", x=80, y=180)]),
        dict(say="The box is 10 centimetres high, so there are 10 layers. 600 times 10 is 6,000 cubes.", do=[MATH("600 × 10 = 6000", x=80, y=280), B("6000 cubes", x=80, y=380, color=GREEN, at=4)]),
    ]),
    dict(kind="recall", title="Area of a rectangle", steps=[
        dict(say="Remember: the area of a rectangle is the length times the width. 12 centimetres by 5 centimetres is 60 square centimetres.", do=[MATH("12 × 5 = 60 cm²", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Volume", steps=[
        dict(say="Volume is the amount of space that a 3D shape takes up. We measure it in cubic units, such as cubic centimetres.", do=[T("**Volume**: the space a 3D shape takes up", x=80, y=160), T("units: **cm³**, **m³**", x=80, y=240, at=4)]),
        dict(say="For a cuboid, multiply the length, the width and the height.", do=[B("V = length × width × height", x=80, y=350, color=BLUE)]),
        dict(say="A cube has 3 equal edges. So its volume is the side, times the side, times the side.", do=[T("cube: **side × side × side**", x=80, y=470)]),
        PAUSE("15.4-k2", "Your turn. What is the volume of a cube with sides of 5 centimetres? Pause the video and try it.", "What is the volume of a cube of side 5 cm?"),
    ]),
    dict(kind="idea", title="Check: a 5 cm cube", steps=[
        dict(say="5 times 5 is 25. And 25 times 5 is 125. The volume is 125 cubic centimetres.", do=[MATH("5 × 5 × 5 = 125", x=80, y=190), B("125 cm³", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="idea", title="Capacity", steps=[
        dict(say="Capacity is how much a container holds. 1 cubic centimetre holds 1 millilitre. So 1,000 cubic centimetres hold 1 litre.", do=[T("**Capacity**: how much a container holds", x=80, y=160), MATH("1 cm³ = 1 ml", x=80, y=250, at=3), B("1000 cm³ = 1 litre", x=80, y=340, color=BLUE, at=6)]),
        dict(say="Our delivery box has a volume of 6,000 cubic centimetres. So it could hold 6 litres of water.", do=[MATH("6000 cm³ = 6 litres", x=80, y=470)]),
        PAUSE("15.4-k3", "Your turn. How many litres is 4,500 cubic centimetres? Pause the video and try it.", "4500 cm³ = ? litres"),
    ]),
    dict(kind="idea", title="Check: 4500 cm³", steps=[
        dict(say="Divide by 1,000. 4,500 divided by 1,000 is 4.5 litres.", do=[MATH("4500 ÷ 1000 = 4.5 litres", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I find the volume of a cuboid?", steps=[
        dict(say="Here is the method. Step 1: check that all 3 lengths are in the same units.", do=[T("1. The **same units** for all 3 lengths", x=80, y=170)]),
        dict(say="Step 2: multiply the length, the width and the height, in any order.", do=[T("2. **length × width × height**", x=80, y=260)]),
        dict(say="Step 3: give the answer in cubic units.", do=[T("3. Answer in **cubic units**", x=80, y=350)]),
        dict(say="Step 4: for capacity, remember that 1,000 cubic centimetres is 1 litre.", do=[T("4. Capacity: **1000 cm³ = 1 litre**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A cuboid", steps=[
        dict(say="Find the volume of a cuboid that is 9 centimetres by 4 centimetres by 5 centimetres.", do=[BOX3("9 cm", "4 cm", "5 cm")]),
        dict(say="9 times 4 is 36. And 36 times 5 is 180. The volume is 180 cubic centimetres.", do=[MATH("9 × 4 × 5 = 180", x=80, y=190), B("180 cm³", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="Mixed units", steps=[
        dict(say="A fish tank is 1.5 metres long, 40 centimetres wide and 30 centimetres high. How many litres does it hold?", do=[E("🐟", 90, 140, 80), T("**1.5 m** × **40 cm** × **30 cm**", x=200, y=160)]),
        dict(say="Use the same units. 1.5 metres is 150 centimetres. 150 times 40 times 30 is 180,000 cubic centimetres.", do=[MATH("150 × 40 × 30 = 180 000 cm³", x=80, y=280)]),
        dict(say="Divide by 1,000. The tank holds 180 litres.", do=[MATH("180 000 ÷ 1000 = 180", x=80, y=370), B("180 litres", x=80, y=460, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Finding a length", steps=[
        dict(say="A cuboid has a volume of 420 cubic centimetres. Its base is 10 centimetres by 7 centimetres. Find its height.", do=[T("volume **420 cm³** · base **10 cm × 7 cm** · height?", x=80, y=160)]),
        dict(say="The area of the base is 10 times 7, which is 70.", do=[MATH("10 × 7 = 70", x=80, y=270)]),
        dict(say="Divide the volume by the area of the base. 420 divided by 70 is 6. The height is 6 centimetres.", do=[MATH("420 ÷ 70 = 6", x=80, y=360), B("6 cm", x=80, y=450, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="How many fit?", steps=[
        dict(say="How many cubes, each with sides of 3 centimetres, fit in a box 12 centimetres by 9 centimetres by 6 centimetres?", do=[T("**3 cm cubes** in a **12 × 9 × 6 cm** box", x=80, y=160)]),
        dict(say="Divide each length by 3. 4 cubes fit along, 3 across, and 2 up.", do=[MATH("12 ÷ 3 = 4 · 9 ÷ 3 = 3 · 6 ÷ 3 = 2", x=80, y=270)]),
        dict(say="4 times 3 times 2 is 24 cubes.", do=[MATH("4 × 3 × 2 = 24", x=80, y=360), B("24 cubes", x=80, y=450, color=GREEN, at=2.4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Find the volume of a cuboid, 6 centimetres by 5 centimetres by 2 centimetres. Here is Enzo's working. Which line goes wrong first?", do=LINES("Enzo", "the volume of a 6 × 5 × 2 cm cuboid", ["6 + 5 + 2 = 13", "Volume = 13 cm³"])),
        dict(say="Line 1 is wrong. Adding the lengths gives a length. For a volume, you must multiply.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="6 times 5 times 2 is 60 cubic centimetres.", do=[B("6 × 5 × 2 = 60 cm³", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="A very big cuboid", steps=[
        dict(say="An Olympic swimming pool is a giant cuboid. It is 50 metres long, 25 metres wide, and at least 2 metres deep.", do=[E("🏊", 90, 160, 100), T("**50 m** × **25 m** × **2 m**", x=230, y=190)]),
        dict(say="50 times 25 times 2 is 2,500 cubic metres.", do=[MATH("50 × 25 × 2 = 2500 m³", x=230, y=300)]),
        dict(say="1 cubic metre holds 1,000 litres. So the pool holds 2 and a half million litres of water.", do=[B("2 500 000 litres", x=230, y=410, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.4-k4", "One last question. What is the volume of a cuboid 2 centimetres by 3 centimetres by 10 centimetres? Pause the video and answer.", "2 cm × 3 cm × 10 cm = ? cm³"),
        dict(say="2 times 3 is 6, and 6 times 10 is 60. The volume is 60 cubic centimetres.", do=[MATH("2 × 3 × 10 = 60", x=80, y=190), B("60 cm³", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the volume of a cuboid is the length, times the width, times the height.", do=[T("• Cuboid: **length × width × height**", x=80, y=170)]),
        dict(say="The volume of a cube is the side, times the side, times the side.", do=[T("• Cube: **side × side × side**", x=80, y=250)]),
        dict(say="Use the same units, and give the answer in cubic units.", do=[T("• Same units · answer in **cm³** or **m³**", x=80, y=330)]),
        dict(say="1,000 cubic centimetres is 1 litre.", do=[T("• **1000 cm³ = 1 litre**", x=80, y=410)]),
    ]),
]

VIDEOS["15.5"] = [
    dict(kind="hook", title="Wrapping a present", steps=[
        dict(say="A gift box is 20 centimetres long, 15 centimetres wide and 10 centimetres high. You want to cover every face with wrapping paper, with no overlaps.", do=[BOX3("20 cm", "15 cm", "10 cm"), E("🎁", 90, 160, 100)]),
        PAUSE("15.5-k1", "How much paper do you need? Here is a hint: imagine opening the box out flat. Pause the video and work it out.", "How much paper covers a 20 × 15 × 10 cm box, in cm²?"),
    ]),
    dict(kind="hook", title="Three pairs of faces", steps=[
        dict(say="A box has 6 faces, in 3 matching pairs. The top and the bottom are each 20 by 15: that is 300 square centimetres each, 600 for the pair.",
             do=[TBL(["Pair of faces", "One face", "The pair"], [["top and bottom", "20 × 15 = 300", "600"], ["front and back", "20 × 10 = 200", "400"], ["the two ends", "15 × 10 = 150", "300"]], y=170), ROW(0, 4)]),
        dict(say="The front and the back are each 20 by 10: 400 for the pair. The 2 ends are each 15 by 10: 300 for the pair.", do=[ROW(1, 0.3), ROW(2, 5)]),
        dict(say="600 plus 400 plus 300 is 1,300 square centimetres of paper.", do=[MATH("600 + 400 + 300 = 1300", x=80, y=420), B("1300 cm²", x=80, y=510, color=GREEN, at=3)]),
    ]),
    dict(kind="recall", title="Nets", steps=[
        dict(say="Remember: a net is a 3D shape opened out flat. The net of a cuboid has 6 rectangles, in 3 matching pairs.", do=[FIG(700, 130, 520, 0, kind="cells", cells=[[1, 0], [0, 1], [1, 1], [2, 1], [3, 1], [1, 2]], cols=4, rows=3, grid=True), T("a **net**: the shape opened out flat", x=80, y=180), T("**6** faces, in **3 pairs**", x=80, y=270, at=4)]),
    ]),
    dict(kind="idea", title="Surface area", steps=[
        dict(say="The surface area of a 3D shape is the total area of all its faces. It is the same as the area of its net.", do=[T("**Surface area**: the total area of **all the faces**", x=80, y=160)]),
        dict(say="For a cuboid, find the area of the 3 different faces, add them, and double the total.", do=[T("cuboid: 3 different faces → add → **double**", x=80, y=260)]),
        dict(say="Surface area is an area. So it is measured in square units, not cubic units.", do=[T("units: **cm²**, **m²** – not cubic", x=80, y=360, color=RED)]),
    ]),
    dict(kind="idea", title="Cubes", steps=[
        dict(say="A cube has 6 identical square faces. So its surface area is 6 times the area of 1 face.", do=[B("cube: 6 × side × side", x=80, y=160, color=BLUE)]),
        dict(say="For a cube with sides of 3 centimetres, 1 face is 3 times 3, which is 9. 6 times 9 is 54 square centimetres.", do=[MATH("3 × 3 = 9", x=80, y=290), MATH("6 × 9 = 54 cm²", x=80, y=380, at=4)]),
        PAUSE("15.5-k2", "Your turn. What is the surface area of a cube with sides of 2 centimetres? Pause the video and try it.", "What is the surface area of a 2 cm cube?"),
    ]),
    dict(kind="idea", title="Check: a 2 cm cube", steps=[
        dict(say="1 face is 2 times 2, which is 4. There are 6 faces. 6 times 4 is 24 square centimetres.", do=[MATH("2 × 2 = 4", x=80, y=190), MATH("6 × 4 = 24", x=80, y=280, at=2.6), B("24 cm²", x=80, y=380, color=GREEN, at=4.6)]),
    ]),
    dict(kind="method", title="How do I find the surface area of a cuboid?", steps=[
        dict(say="Here is the method. Step 1: sketch the cuboid, and label its length, width and height.", do=[T("1. **Sketch** and label it", x=80, y=170)]),
        dict(say="Step 2: find the area of the 3 different faces.", do=[T("2. The area of the **3 different faces**", x=80, y=260)]),
        dict(say="Step 3: add them, and double the total, because opposite faces are equal.", do=[T("3. Add, then **double**", x=80, y=350)]),
        dict(say="Step 4: give the answer in square units.", do=[T("4. Answer in **square units**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A cuboid", steps=[
        dict(say="Find the surface area of a cuboid that is 8 centimetres by 5 centimetres by 2 centimetres.", do=[BOX3("8 cm", "5 cm", "2 cm")]),
        dict(say="The 3 different faces are 8 times 5, which is 40. Then 8 times 2, which is 16. And 5 times 2, which is 10.", do=[MATH("8 × 5 = 40", x=80, y=180), MATH("8 × 2 = 16", x=80, y=260, at=3), MATH("5 × 2 = 10", x=80, y=340, at=5.6)]),
        dict(say="Add them: 66. Double it: 132 square centimetres.", do=[MATH("2 × 66 = 132", x=80, y=440), B("132 cm²", x=80, y=530, color=GREEN, at=3)]),
        PAUSE("15.5-k3", "Your turn. A cuboid is 3 by 3 by 1. What is its surface area? Pause the video and try it.", "Cuboid 3 × 3 × 1. What is its surface area?"),
    ]),
    dict(kind="example", title="Check: 3 × 3 × 1", steps=[
        dict(say="The 3 different faces are 9, 3 and 3. They add up to 15. Double it: the surface area is 30 square units.", do=[MATH("9 + 3 + 3 = 15", x=80, y=190), MATH("2 × 15 = 30", x=80, y=280, at=4), B("30", x=80, y=380, color=GREEN, at=5.4)]),
    ]),
    dict(kind="example", title="A box with no lid", steps=[
        dict(say="A box with no lid is 40 centimetres long, 25 centimetres wide and 10 centimetres high. How much cardboard is needed?", do=[BOX3("40 cm", "25 cm", "10 cm"), T("**no lid**", x=80, y=180, color=RED)]),
        dict(say="There is only 1 face of 40 by 25, the bottom: 1,000 square centimetres.", do=[MATH("bottom: 40 × 25 = 1000", x=80, y=270)]),
        dict(say="The front and back are 2 times 40 times 10, which is 800. The ends are 2 times 25 times 10, which is 500.", do=[MATH("2 × 40 × 10 = 800", x=80, y=350), MATH("2 × 25 × 10 = 500", x=80, y=430, at=4)]),
        dict(say="The total is 2,300 square centimetres.", do=[B("2300 cm²", x=80, y=530, color=GREEN)]),
    ]),
    dict(kind="example", title="From surface area to side", steps=[
        dict(say="A cube has a surface area of 216 square centimetres. Find the length of its side.", do=[T("cube · surface area **216 cm²** · side?", x=80, y=160)]),
        dict(say="A cube has 6 equal faces. 216 divided by 6 is 36. So each face has an area of 36.", do=[MATH("216 ÷ 6 = 36", x=80, y=270)]),
        dict(say="6 times 6 is 36. So the side is 6 centimetres.", do=[MATH("6 × 6 = 36", x=80, y=360), B("6 cm", x=80, y=450, color=GREEN, at=2.6)]),
    ]),
    dict(kind="example", title="Painting a room", steps=[
        dict(say="A room is 5 metres long, 4 metres wide and 2.5 metres high. You paint the 4 walls, but not the floor or the ceiling. What area do you paint?", do=[E("🖌️", 90, 140, 80), T("**5 m** × **4 m** × **2.5 m** · the **4 walls** only", x=200, y=160)]),
        dict(say="2 walls are 5 by 2.5: 2 times 12.5 is 25. The other 2 walls are 4 by 2.5: 2 times 10 is 20.", do=[MATH("2 × 5 × 2.5 = 25", x=80, y=290), MATH("2 × 4 × 2.5 = 20", x=80, y=380, at=5)]),
        dict(say="25 plus 20 is 45 square metres.", do=[B("45 m²", x=80, y=490, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Find the surface area of a cuboid, 5 by 4 by 2. Here is Rosa's working. Which line goes wrong first?", do=LINES("Rosa", "the surface area of a 5 × 4 × 2 cuboid", ["5 × 4 = 20, 5 × 2 = 10, 4 × 2 = 8", "Surface area = 20 + 10 + 8 = 38"])),
        dict(say="Line 2 is wrong. That is only 3 faces. A cuboid has 6 faces, because each face has a matching one opposite.", do=[dict(a="cross", id="l2")]),
        dict(say="Double the total. 2 times 38 is 76 square units.", do=[B("2 × 38 = 76", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Why crushed ice melts faster", steps=[
        dict(say="Take an ice cube with sides of 2 centimetres. Its surface area is 24 square centimetres.", do=[E("🧊", 90, 160, 100), MATH("6 × 2 × 2 = 24 cm²", x=230, y=180)]),
        dict(say="Now cut it into 8 small cubes, each with sides of 1 centimetre. Each has a surface area of 6. Together, that is 48 square centimetres.", do=[MATH("8 × 6 = 48 cm²", x=230, y=290)]),
        dict(say="It is the same amount of ice, but 2 times the surface. Heat gets in faster. That is why crushed ice melts so quickly.", do=[B("same ice, double the surface", x=230, y=400, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.5-k4", "One last question. A cube has a surface area of 150 square centimetres. How long is its side? Pause the video and work it out.", "A cube has surface area 150 cm². What is its side in cm?"),
        dict(say="150 divided by 6 is 25. Each face has an area of 25. And 5 times 5 is 25. So the side is 5 centimetres.", do=[MATH("150 ÷ 6 = 25", x=80, y=190), MATH("5 × 5 = 25", x=80, y=280, at=4), B("5 cm", x=80, y=380, color=GREEN, at=6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: surface area is the total area of all the faces. It is the area of the net.", do=[T("• **Surface area**: all the faces (the net)", x=80, y=170)]),
        dict(say="For a cuboid: find the 3 different faces, add them, and double.", do=[T("• Cuboid: 3 faces → add → **double**", x=80, y=250)]),
        dict(say="For a cube: 6 times the area of 1 face.", do=[T("• Cube: **6 × one face**", x=80, y=330)]),
        dict(say="The units are square units.", do=[T("• Units: **cm²**, **m²**", x=80, y=410)]),
    ]),
]
