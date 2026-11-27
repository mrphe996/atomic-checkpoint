# -*- coding: utf-8 -*-
"""Stage 9 · Unit 7 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

VIDEOS = {}

VIDEOS["7.1"] = [
    dict(kind="hook", title="Pancake deal", steps=[
        dict(say="A café sells one large pancake with a diameter of 30 centimetres for 8 dollars, or two small pancakes with diameters of 20 centimetres for 9 dollars.",
             do=[E("🥞", 90, 170, 100), T("one **30 cm** pancake · or two **20 cm** pancakes", x=230, y=200)]),
        PAUSE("7.1-k1", "Which gives more pancake: one 30 centimetre, or two 20 centimetre? Pause the video and choose.", "More pancake?"),
    ]),
    dict(kind="hook", title="One 30 cm", steps=[
        dict(say="The one 30 centimetre pancake gives more. Let's see why, with the area of a circle.", do=[B("one 30 cm", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Radius and diameter", steps=[
        dict(say="Remember: the diameter is twice the radius. A diameter of 18 centimetres means a radius of 9.", do=[MATH("d = 2r   ·   d = 18 → r = 9", x=80, y=190)]),
    ]),
    dict(kind="idea", title="The formulae", steps=[
        dict(say="The circumference is pi times the diameter, or 2 pi R. Use the pi key on your calculator.", do=[B("C = πd = 2πr", x=80, y=170, color=BLUE)]),
        dict(say="The area of a circle is pi R squared.", do=[B("A = πr²", x=80, y=260, color=BLUE)]),
        PAUSE("7.1-k2", "Your turn. The area of a circle uses: pi R squared, or 2 pi R? Pause the video and choose.", "Area of a circle uses …"),
    ]),
    dict(kind="idea", title="Check: πr²", steps=[
        dict(say="Pi R squared. 2 pi R is the circumference.", do=[B("A = πr²", x=80, y=190, color=GREEN)]),
        dict(say="The big pancake has radius 15. Its area is about 707 square centimetres. Each small one has radius 10, so the two together have about 628.",
             do=[TBL(["Pancake", "Radius", "Area"], [["one 30 cm", "15 cm", "≈ 706.9 cm²"], ["two 20 cm", "10 cm each", "2 × 314.2 ≈ 628.3 cm²"]], y=290), ROW(0, 3), ROW(1, 7)]),
    ]),
    dict(kind="idea", title="Backwards and exact", steps=[
        dict(say="To work backwards, rearrange. From the area: R squared is A divided by pi. From the circumference: D is C divided by pi.", do=[MATH("r² = A ÷ π   ·   d = C ÷ π", x=80, y=170)]),
        dict(say="For an exact answer, leave pi in. A radius of 7 gives an area of 49 pi.", do=[MATH("r = 7 → A = 49π", x=80, y=270)]),
    ]),
    dict(kind="method", title="How do I find C or A?", steps=[
        dict(say="Here is the method. Step 1: find the radius or diameter.", do=[T("1. Find **r** or **d**", x=80, y=170)]),
        dict(say="Step 2: choose the formula: circumference or area.", do=[T("2. **C = πd** or **A = πr²**", x=80, y=260)]),
        dict(say="Step 3: work it out with the pi key, or leave pi in.", do=[T("3. Use the **π** key, or leave π in", x=80, y=350)]),
        dict(say="Step 4: round, and give the units.", do=[T("4. Round; **units**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A wheel", steps=[
        dict(say="A bike wheel has a diameter of 64 centimetres. In one turn it travels pi times 64, which is about 201.1 centimetres.", do=[MATH("π × 64 ≈ 201.1 cm", x=80, y=180)]),
        dict(say="A round rug has an area of 2.5 square metres. R squared is 2.5 divided by pi, about 0.796. So R is about 0.89 metres.", do=[MATH("r² = 2.5 ÷ π ≈ 0.796 → r ≈ 0.89 m", x=80, y=280)]),
        PAUSE("7.1-k3", "Your turn. A circle has radius 5. What is its area, in terms of pi? Pause and work it out.", "Radius 5: area in terms of π?"),
    ]),
    dict(kind="example", title="Check: 25π", steps=[
        dict(say="5 squared is 25, so the area is 25 pi.", do=[B("A = 25π", x=80, y=190, color=GREEN)]),
        dict(say="A semicircle with diameter 10: the curve is half of 10 pi, about 15.7. Add the straight edge, 10. The perimeter is about 25.7 centimetres.", do=[MATH("½ × 10π + 10 ≈ 25.7 cm", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A circle has diameter 8 centimetres. Kai finds the area. Which line is wrong?", do=LINES("Kai", "area, diameter 8 cm", ["A = π × 8² ≈ 201.1 cm²"])),
        dict(say="Line 1 is wrong. The area formula uses the radius, which is 4.", do=[dict(a="cross", id="l1")]),
        dict(say="Pi times 4 squared is 16 pi, about 50.3 square centimetres.", do=[B("π × 4² = 16π ≈ 50.3 cm²", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Bike computers", steps=[
        dict(say="A bike computer counts how many times the wheel turns. It multiplies by the circumference to work out how far you have ridden.", do=[E("🚲", 90, 170, 100), T("turns × **circumference** = distance", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.1-k4", "One last question. Find the circumference of a circle with radius 3, to 1 decimal place. Pause the video and answer.", "Circumference of radius 3? (1 d.p.)"),
        dict(say="2 times pi times 3 is 6 pi, which is about 18.8.", do=[B("2π × 3 = 6π ≈ 18.8", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the circumference is pi D, or 2 pi R.", do=[T("• C = πd = 2πr", x=80, y=170)]),
        dict(say="The area is pi R squared. Use the radius.", do=[T("• A = πr² (radius!)", x=80, y=250)]),
        dict(say="Rearrange to work backwards.", do=[T("• Rearrange to work backwards", x=80, y=330)]),
        dict(say="For exact answers, leave pi in.", do=[T("• Exact: leave π in", x=80, y=410)]),
    ]),
]

VIDEOS["7.2"] = [
    dict(kind="hook", title="A sports field", steps=[
        dict(say="A sports field is a rectangle, 80 metres by 60 metres, with a semicircle on each short end. The grass needs new seed.",
             do=[E("🏟️", 90, 170, 100), T("rectangle **80 m × 60 m** + a **semicircle** on each end", x=230, y=200)]),
        PAUSE("7.2-k1", "How would you split the field: into a rectangle and a circle, made of two semicircles, or into triangles only? Pause the video and choose.", "Split the field into …"),
    ]),
    dict(kind="hook", title="Rectangle and circle", steps=[
        dict(say="A rectangle, and two semicircles. Together, the two semicircles make one whole circle.", do=[B("rectangle + one whole circle", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Area formulae", steps=[
        dict(say="Remember the area formulae. Rectangle: length times width. Triangle: half base times height. Trapezium: half the sum of the parallel sides, times the height. Circle: pi R squared.",
             do=[MATH("lw · ½bh · ½(a + b)h · πr²", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Splitting shapes", steps=[
        dict(say="A compound shape is made of simpler shapes. Split it, find each area, then add. For holes and cut-outs, subtract.",
             do=[T("split → find each area → **add** (or **subtract** holes)", x=80, y=170)]),
        dict(say="For the field: the rectangle is 80 by 60. The circle has a diameter of 60, so its radius is 30.", do=[MATH("rectangle 80 × 60 · circle r = 30", x=80, y=270)]),
        PAUSE("7.2-k2", "Your turn. Find the area of the field, in square metres, to 1 decimal place. Pause the video and try it.", "Area of the field (m²)? (1 d.p.)"),
    ]),
    dict(kind="idea", title="Check: the field", steps=[
        dict(say="The rectangle is 4,800. The circle is pi times 30 squared, about 2,827.4. The total is about 7,627.4 square metres.",
             do=[MATH("4800 + π × 30² ≈ 4800 + 2827.4", x=80, y=180), B("≈ 7627.4 m²", x=80, y=290, color=GREEN, at=8)]),
        dict(say="Estimate first: 80 by 60 is 4,800, and the circle is about 3 times 900, which is 2,700. So about 7,500. The answer is sensible.", do=[T("estimate: 4800 + 2700 ≈ 7500 ✓", x=80, y=390)]),
    ]),
    dict(kind="method", title="How do I find a compound area?", steps=[
        dict(say="Here is the method. Step 1: split the shape into simple shapes.", do=[T("1. **Split** into simple shapes", x=80, y=170)]),
        dict(say="Step 2: find any missing lengths.", do=[T("2. Find **missing lengths**", x=80, y=260)]),
        dict(say="Step 3: find each area, then add, or subtract holes.", do=[T("3. Each area; **add** or **subtract**", x=80, y=350)]),
        dict(say="Step 4: check with an estimate, and give the units.", do=[T("4. Estimate; **units**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Triangle on a rectangle", steps=[
        dict(say="The end of a shed is a rectangle 6 metres by 4 metres, with a triangular roof of height 2 metres. 24 plus half of 6 times 2, which is 6. The total is 30 square metres.",
             do=[MATH("6 × 4 + ½ × 6 × 2 = 24 + 6", x=80, y=180), B("30 m²", x=80, y=290, color=GREEN, at=9)]),
        PAUSE("7.2-k3", "Your turn. A square tile has sides of 20 centimetres, with a round hole of radius 4 centimetres. What is the area of the tile, to 1 decimal place? Pause and work it out.", "Tile 20 cm with hole r = 4. Area? (1 d.p.)"),
    ]),
    dict(kind="example", title="Check: the tile", steps=[
        dict(say="400 minus pi times 16. That is 400 minus about 50.3, which is about 349.7 square centimetres.", do=[B("400 − 16π ≈ 349.7 cm²", x=80, y=190, color=GREEN)]),
        dict(say="A ring has outer radius 5 and inner radius 2. Its area is pi times 25 minus 4, which is 21 pi, about 66.0.", do=[MATH("π(25 − 4) = 21π ≈ 66.0", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="An L-shape is made of a 10 by 2 strip and a 2 by 8 strip. They share a 2 by 2 corner. Eva finds the area. Which line is wrong?", do=LINES("Eva", "a 10 × 2 strip and a 2 × 8 strip, sharing a corner", ["20 + 16 = 36"])),
        dict(say="Line 1 is wrong. The 2 by 2 corner is counted twice.", do=[dict(a="cross", id="l1")]),
        dict(say="36 minus 4 is 32.", do=[B("36 − 4 = 32", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Flooring", steps=[
        dict(say="Builders work out compound areas to order flooring, paint and turf. They usually add about 10 percent extra for cutting and waste.", do=[E("🧱", 90, 170, 100), T("area + about **10%** for waste", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.2-k4", "One last question. A rectangle 10 by 8 has a 4 by 3 rectangle cut from one corner. What is the area? Pause the video and answer.", "10 × 8 minus 4 × 3?"),
        dict(say="80 minus 12 is 68.", do=[B("80 − 12 = 68", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: split, find each area, then add or subtract.", do=[T("• Split → add or subtract", x=80, y=170)]),
        dict(say="Two semicircles make one whole circle.", do=[T("• Two semicircles = one circle", x=80, y=250)]),
        dict(say="Do not count an overlap twice.", do=[T("• Don't count overlaps twice", x=80, y=330)]),
        dict(say="Estimate to check.", do=[T("• Estimate to check", x=80, y=410)]),
    ]),
]

VIDEOS["7.3"] = [
    dict(kind="hook", title="Very big, very small", steps=[
        dict(say="A laptop stores 512 gigabytes. A grain of pollen is about 25 micrometres across. A cruise ship weighs 100,000 tonnes.",
             do=[E("💻", 90, 170, 100), T("**512 gigabytes** · **25 micrometres** · **100 000 tonnes**", x=230, y=200)]),
        PAUSE("7.3-k1", "What does micro mean: one millionth, or one million? Pause the video and choose.", "micro- means …"),
    ]),
    dict(kind="hook", title="One millionth", steps=[
        dict(say="Micro means one millionth. A micrometre is one millionth of a metre.", do=[B("micro = one millionth", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Metric units", steps=[
        dict(say="Remember: 1 kilometre is 1,000 metres. 1 metre is 100 centimetres, or 1,000 millimetres. 1 kilogram is 1,000 grams.", do=[MATH("1 km = 1000 m · 1 m = 1000 mm · 1 kg = 1000 g", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Prefixes", steps=[
        dict(say="A prefix multiplies the unit by a power of 10. Mega means a million, 10 to the power 6. Kilo means a thousand.",
             do=[TBL(["Prefix", "Symbol", "Multiplier"], [["mega", "M", "10⁶"], ["kilo", "k", "10³"], ["centi", "c", "10⁻²"], ["milli", "m", "10⁻³"], ["micro", "µ", "10⁻⁶"]], y=170), ROW(0, 3), ROW(1, 6)]),
        dict(say="Centi is one hundredth. Milli is one thousandth. Micro is one millionth, 10 to the power minus 6.", do=[ROW(2, 0.2), ROW(3, 2), ROW(4, 4)]),
        PAUSE("7.3-k2", "Your turn. Giga is bigger than mega. Is giga 10 to the power 9, or 10 to the power 6? Pause the video and choose.", "giga = ?"),
    ]),
    dict(kind="idea", title="Check: giga", steps=[
        dict(say="Giga is 10 to the power 9, a thousand million. 512 gigabytes is 512 times 10 to the 9 bytes.", do=[B("giga = 10⁹", x=80, y=190, color=GREEN)]),
        dict(say="Also: 1 tonne is 1,000 kilograms.", do=[MATH("1 tonne = 1000 kg", x=80, y=300)]),
        dict(say="Big unit to small unit: multiply. Small unit to big unit: divide.", do=[T("big → small: **×** · small → big: **÷**", x=80, y=400, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I convert with prefixes?", steps=[
        dict(say="Here is the method. Step 1: write the prefix as a power of 10.", do=[T("1. Prefix → **power of 10**", x=80, y=170)]),
        dict(say="Step 2: convert to the base unit, like metres or grams.", do=[T("2. Convert to the **base unit**", x=80, y=260)]),
        dict(say="Step 3: convert to the unit you want.", do=[T("3. Convert to the **new unit**", x=80, y=350)]),
        dict(say="Step 4: check: a smaller unit means a bigger number.", do=[T("4. Smaller unit → **bigger number**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Mass and length", steps=[
        dict(say="A lorry carries 12.4 tonnes. In kilograms, that is 12.4 times 1,000, which is 12,400 kilograms.", do=[MATH("12.4 × 1000 = 12 400 kg", x=80, y=180)]),
        dict(say="A bacterium is 3 micrometres long. That is 3 times 10 to the minus 6 metres, which is 0.003 millimetres.", do=[MATH("3 µm = 3 × 10⁻⁶ m = 0.003 mm", x=80, y=280)]),
        PAUSE("7.3-k3", "Your turn. A hair is 80 micrometres thick. How many millimetres is that? Pause and work it out.", "80 µm in mm?"),
    ]),
    dict(kind="example", title="Check: 0.08 mm", steps=[
        dict(say="1,000 micrometres make 1 millimetre. 80 divided by 1,000 is 0.08 millimetres.", do=[B("80 ÷ 1000 = 0.08 mm", x=80, y=190, color=GREEN)]),
        dict(say="A 6 gigabyte film is 6,000 megabytes. And 250 microlitres of medicine is 0.25 millilitres.", do=[MATH("6 GB = 6000 MB · 250 µL = 0.25 mL", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Max converts 350 milligrams to grams. Which line is wrong?", do=LINES("Max", "350 mg in grams", ["350 × 1000 = 350 000 g"])),
        dict(say="Line 1 is wrong. Grams are bigger than milligrams, so the number must get smaller. Divide.", do=[dict(a="cross", id="l1")]),
        dict(say="350 divided by 1,000 is 0.35 grams.", do=[B("350 ÷ 1000 = 0.35 g", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Chips", steps=[
        dict(say="The tiny parts inside computer chips are measured in nanometres, which are billionths of a metre. That is why so many fit on one chip.", do=[E("🔬", 90, 170, 100), T("**nanometre** = 10⁻⁹ m", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.3-k4", "One last question. How many kilograms are in 2 tonnes? Pause the video and answer.", "2 tonnes in kg?"),
        dict(say="2 times 1,000 is 2,000 kilograms.", do=[B("2000 kg", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: giga is 10 to the 9, mega 10 to the 6, kilo 10 to the 3.", do=[T("• G 10⁹ · M 10⁶ · k 10³", x=80, y=170)]),
        dict(say="Milli is 10 to the minus 3, and micro is 10 to the minus 6.", do=[T("• m 10⁻³ · µ 10⁻⁶", x=80, y=250)]),
        dict(say="1 tonne is 1,000 kilograms.", do=[T("• 1 tonne = 1000 kg", x=80, y=330)]),
        dict(say="To a bigger unit, divide. To a smaller unit, multiply.", do=[T("• Bigger unit ÷ · smaller unit ×", x=80, y=410)]),
    ]),
]
