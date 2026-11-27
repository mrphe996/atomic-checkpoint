# -*- coding: utf-8 -*-
"""Stage 9 · Unit 13 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

VIDEOS = {}

VIDEOS["13.1"] = [
    dict(kind="hook", title="A rescue", steps=[
        dict(say="A lifeboat station gets a call. A yacht is 12 kilometres away, on a bearing of 140 degrees. A helicopter base is 8 kilometres due east of the station.",
             do=[E("🚁", 90, 170, 100), T("yacht: **12 km** on **140°** · base: **8 km** due east", x=230, y=200)]),
        PAUSE("13.1-k1", "What does a scale drawing let you do: measure distances and bearings you cannot measure directly, or avoid using a protractor? Pause the video and choose.", "A scale drawing lets you …"),
    ]),
    dict(kind="hook", title="Measure it", steps=[
        dict(say="It lets you measure distances and bearings you cannot measure directly, like from the base to the yacht.", do=[B("measure what you can't measure directly", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Scales and bearings", steps=[
        dict(say="Remember: bearings are measured clockwise from north, with three figures. A scale of 1 to 200,000 means 1 centimetre represents 200,000 centimetres, which is 2 kilometres.", do=[T("bearings: **clockwise** from north, 3 figures", x=80, y=170), MATH("1 : 200 000 → 1 cm = 2 km", x=80, y=260)]),
    ]),
    dict(kind="idea", title="Scales three ways", steps=[
        dict(say="A scale can be written as 1 centimetre represents 2 kilometres, or as a ratio, 1 to 200,000, with no units, because both parts are in the same unit.",
             do=[T("'1 cm represents 2 km' = **1 : 200 000**", x=80, y=170)]),
        dict(say="On the map, the station to the base is 8 kilometres, which is 4 centimetres.", do=[MATH("8 km → 4 cm", x=80, y=260)]),
        PAUSE("13.1-k2", "Your turn. At 1 to 200,000, how many centimetres on the map is 12 kilometres? Pause the video and try it.", "1 : 200 000. 12 km = ? cm on the map"),
    ]),
    dict(kind="idea", title="Check: 6 cm", steps=[
        dict(say="12 divided by 2 is 6 centimetres. Draw the station, then the yacht 6 centimetres away on 140 degrees, and the base 4 centimetres due east.", do=[B("12 ÷ 2 = 6 cm", x=80, y=190, color=GREEN)]),
        dict(say="Then measure from the base to the yacht with a ruler. Draw a north line at the base, and measure the bearing clockwise.", do=[T("ruler for the **distance** · north line + protractor for the **bearing**", x=80, y=300)]),
        PAUSE("13.1-k3", "Your turn. Base to yacht measures 4 centimetres on the map. How many kilometres is that? Pause and work it out.", "BY = 4 cm at 1 : 200 000. Real km?"),
    ]),
    dict(kind="idea", title="Check: 8 km", steps=[
        dict(say="4 times 2 is 8 kilometres. The bearing measures about 197 degrees. Measure carefully: 1 millimetre on this map is 200 metres.", do=[B("4 × 2 = 8 km, about 197°", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I use scale drawings?", steps=[
        dict(say="Here is the method. Step 1: choose a scale, and convert the real distances.", do=[T("1. **Scale**: convert distances", x=80, y=170)]),
        dict(say="Step 2: draw a north line at each point.", do=[T("2. A **north line** at each point", x=80, y=260)]),
        dict(say="Step 3: draw the bearings clockwise, and the lengths accurately.", do=[T("3. Bearings **clockwise**; accurate lengths", x=80, y=350)]),
        dict(say="Step 4: measure what you need, and convert back.", do=[T("4. **Measure** and convert back", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="4.5 kilometres on a 1 to 25,000 map. 4.5 kilometres is 450,000 centimetres. Divide by 25,000: 18 centimetres.", do=[MATH("450 000 ÷ 25 000 = 18 cm", x=80, y=180)]),
        dict(say="5 centimetres represents 1 kilometre. 1 kilometre is 100,000 centimetres, so 1 centimetre is 20,000. The scale is 1 to 20,000.", do=[MATH("1 : 20 000", x=80, y=280)]),
        dict(say="The bearing of the yacht from the station is 140. The back bearing is 140 plus 180, which is 320 degrees.", do=[MATH("140 + 180 = 320°", x=80, y=380)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="1 centimetre represents 5 kilometres. Ella writes this as a ratio. Which line is wrong?", do=LINES("Ella", "1 cm represents 5 km, as a ratio", ["1 : 5"])),
        dict(say="Line 1 is wrong. Both parts of a ratio scale must be in the same units.", do=[dict(a="cross", id="l1")]),
        dict(say="5 kilometres is 500,000 centimetres. So 1 to 500,000.", do=[B("1 : 500 000", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Orienteering", steps=[
        dict(say="Orienteers and rescue teams use a map, a scale and a compass bearing to find places they cannot see.", do=[E("🧭", 90, 170, 100), T("map + scale + **bearing**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("13.1-k4", "One last question. A plan has a scale of 1 to 50. How many metres is 3 centimetres? Pause the video and answer.", "1 : 50. 3 cm = ? m"),
        dict(say="3 times 50 is 150 centimetres, which is 1.5 metres.", do=[B("150 cm = 1.5 m", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a scale can be written in words, or as 1 to N, in the same units.", do=[T("• Scale: words, or 1 : n (same units)", x=80, y=170)]),
        dict(say="Map length is real divided by N. Real is map times N.", do=[T("• Map = real ÷ n · real = map × n", x=80, y=250)]),
        dict(say="Bearings: north line, clockwise, three figures.", do=[T("• Bearings: north, clockwise, 3 figures", x=80, y=330)]),
        dict(say="Measure carefully.", do=[T("• Measure carefully", x=80, y=410)]),
    ]),
]

VIDEOS["13.2"] = [
    dict(kind="hook", title="Charging stations", steps=[
        dict(say="A straight road runs from town A at 1, 2 to town B at 13, 8, on a grid in kilometres. Planners want charging stations one third and two thirds of the way along.",
             do=[E("🔌", 90, 170, 100), T("A **(1, 2)** → B **(13, 8)** · stations at **⅓** and **⅔**", x=230, y=200)]),
        PAUSE("13.2-k1", "Where is the point one third of the way along? Pause the video and work it out.", "One third of the way?"),
    ]),
    dict(kind="hook", title="(5, 4)", steps=[
        dict(say="The road goes 12 across and 6 up. A third of that is 4 across and 2 up. From 1, 2, that is 5, 4.", do=[B("(1 + 4, 2 + 2) = (5, 4)", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Midpoints", steps=[
        dict(say="Remember: the midpoint of 2, 4 and 8, 10 is 5, 7. It is halfway along.", do=[MATH("midpoint of (2, 4) and (8, 10) = (5, 7)", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Fractions of the way", steps=[
        dict(say="Find the step from A to B: across, 13 minus 1 is 12. Up, 8 minus 2 is 6. For a fraction of the way, start at A, and add that fraction of the step.",
             do=[MATH("step = (12, 6)", x=80, y=170), T("point = A + **fraction × step**", x=80, y=260, color=BLUE)]),
        PAUSE("13.2-k2", "Your turn. Where is the point two thirds of the way along? Pause the video and try it.", "Two thirds of the way?"),
    ]),
    dict(kind="idea", title="Check: (9, 6)", steps=[
        dict(say="Two thirds of 12 is 8. Two thirds of 6 is 4. From 1, 2, that is 9, 6.", do=[B("(1 + 8, 2 + 4) = (9, 6)", x=80, y=190, color=GREEN)]),
        dict(say="A point that divides A B in the ratio 1 to 3 splits it into 4 parts.", do=[T("ratio 1 : 3 → **4** parts", x=80, y=300)]),
        PAUSE("13.2-k3", "Your turn. Ratio 1 to 3, from A. Is that a quarter of the way, or a third of the way? Pause the video and choose.", "Ratio 1 : 3 from A means …"),
    ]),
    dict(kind="idea", title="Check: a quarter", steps=[
        dict(say="A quarter of the way. 1 part out of 1 plus 3, which is 4 parts.", do=[B("¼ of the way", x=80, y=190, color=GREEN)]),
        dict(say="Be careful with negative numbers. From negative 4, 6 to 8, negative 2, the step is 12 across, and negative 8 up.", do=[MATH("(−4, 6) → (8, −2): step (12, −8)", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I find the point?", steps=[
        dict(say="Here is the method. Step 1: find the step, B minus A.", do=[T("1. Step = **B − A**", x=80, y=170)]),
        dict(say="Step 2: for a ratio M to N, the fraction is M over M plus N.", do=[T("2. Ratio m : n → **m/(m + n)**", x=80, y=260)]),
        dict(say="Step 3: multiply the step by the fraction, and add it to A.", do=[T("3. A + **fraction × step**", x=80, y=350)]),
        dict(say="Step 4: check the point is between A and B.", do=[T("4. **Between** A and B?", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="P divides A B in the ratio 2 to 3. A is 0, 5 and B is 10, 0. The fraction is 2 fifths. The step is 10, negative 5. 2 fifths of it is 4, negative 2. So P is 4, 3.", do=[MATH("(0, 5) + (4, −2) = (4, 3)", x=80, y=180)]),
        dict(say="M at 5, 4 is one third of the way from A at 2, 1 to B. One third of the step is 3, 3. So the whole step is 9, 9, and B is 11, 10.", do=[MATH("step = 3 × (3, 3) = (9, 9) → B (11, 10)", x=80, y=280)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Find the point one third of the way from 3, 3 to 9, 12. Mia answers. Which line is wrong?", do=LINES("Mia", "⅓ of the way from (3, 3) to (9, 12)", ["⅓ of (9, 12) = (3, 4)"])),
        dict(say="Line 1 is wrong. Take a third of the step, not of the end point.", do=[dict(a="cross", id="l1")]),
        dict(say="The step is 6, 9. A third is 2, 3. Add to A: 5, 6.", do=[B("(3, 3) + (2, 3) = (5, 6)", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Animation", steps=[
        dict(say="Animation software places the in-between frames at fractions of the way along a path, so movement looks smooth.", do=[E("🎞️", 90, 170, 100), T("frames at **fractions** along a path", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("13.2-k4", "One last question. Where is the point 3 quarters of the way from 0, 0 to 4, 8? Pause the video and answer.", "¾ of the way from (0, 0) to (4, 8)?"),
        dict(say="3 quarters of 4 is 3. 3 quarters of 8 is 6. So 3, 6.", do=[B("(3, 6)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the step is B minus A.", do=[T("• Step = B − A", x=80, y=170)]),
        dict(say="The point is A plus the fraction times the step.", do=[T("• Point = A + fraction × step", x=80, y=250)]),
        dict(say="Ratio M to N means M over M plus N.", do=[T("• m : n → m/(m + n)", x=80, y=330)]),
        dict(say="The midpoint is the half-way case.", do=[T("• Midpoint: the ½ case", x=80, y=410)]),
    ]),
]

VIDEOS["13.3"] = [
    dict(kind="hook", title="A puzzle app", steps=[
        dict(say="In a puzzle app, you must move a tile into a slot. You may only reflect, rotate or translate it, maybe more than once.",
             do=[E("🧩", 90, 170, 100), T("**reflect** · **rotate** · **translate**", x=230, y=200)]),
        PAUSE("13.3-k1", "Does the tile ever change size? Pause the video and choose: no, it stays congruent, or yes.", "Does the tile change size?"),
    ]),
    dict(kind="hook", title="Congruent", steps=[
        dict(say="No. Reflections, rotations and translations never change the size or shape. The image is congruent.", do=[B("No – congruent", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Describing transformations", steps=[
        dict(say="Remember: a reflection needs a mirror line. A rotation needs an angle, a direction and a centre. A translation needs a vector.", do=[T("reflection: **line** · rotation: **angle, direction, centre** · translation: **vector**", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Combining", steps=[
        dict(say="To combine transformations, do the first one, then apply the second one to the image.", do=[T("do the first → apply the second to the **image**", x=80, y=170)]),
        dict(say="Triangle A has corners 1, 1, then 3, 1, and 1, 4. Reflect it in the Y axis to get B: negative 1, 1, then negative 3, 1, and negative 1, 4. Then rotate B 180 degrees about the origin to get C.",
             do=[MATH("A: (1, 1), (3, 1), (1, 4)", x=80, y=260), MATH("B: (−1, 1), (−3, 1), (−1, 4)", x=80, y=330, at=8)]),
        PAUSE("13.3-k2", "Your turn. Where does A's corner 3, 1 end up in C? Pause the video and try it.", "A's vertex (3, 1) after both moves (C)?"),
    ]),
    dict(kind="idea", title="Check: (3, −1)", steps=[
        dict(say="B's corner is negative 3, 1. A 180 degree rotation changes both signs: 3, negative 1.", do=[B("(−3, 1) → (3, −1)", x=80, y=190, color=GREEN)]),
        dict(say="C is 1, negative 1, then 3, negative 1, and 1, negative 4. That is just A reflected in the X axis. One transformation does the job of two.", do=[T("C = A reflected in the **x-axis**", x=80, y=300, color=BLUE)]),
        dict(say="Two reflections in perpendicular lines make a 180 degree rotation.", do=[T("perpendicular mirrors → **180° rotation**", x=80, y=390)]),
        PAUSE("13.3-k3", "Your turn. Two reflections in parallel lines make: a translation, or a 90 degree rotation? Pause and choose.", "Two reflections in parallel lines = …"),
    ]),
    dict(kind="idea", title="Check: translation", steps=[
        dict(say="A translation. Reflect in X equals 1, then in X equals 4: everything moves 6 to the right. That is twice the gap between the lines.", do=[B("a translation, (6 over 0)", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I combine transformations?", steps=[
        dict(say="Here is the method. Step 1: do the first transformation.", do=[T("1. Do the **first**", x=80, y=170)]),
        dict(say="Step 2: apply the second to the image.", do=[T("2. The second on the **image**", x=80, y=260)]),
        dict(say="Step 3: compare the final image with the start.", do=[T("3. **Compare** with the start", x=80, y=350)]),
        dict(say="Step 4: describe a single transformation fully.", do=[T("4. Describe it **fully**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="Translate by 2, negative 1, then by negative 5, 4. Add the vectors: negative 3, 3. One translation.", do=[MATH("(2, −1) + (−5, 4) = (−3, 3)", x=80, y=180)]),
        dict(say="1, 2 goes to negative 2, 1, and 3, 0 goes to 0, 3. That is a rotation of 90 degrees anticlockwise about the origin.", do=[MATH("rotation 90° anticlockwise, centre (0, 0)", x=80, y=280)]),
        dict(say="Order can matter. Doing the same two moves the other way round may give a different image.", do=[T("order **can** matter", x=80, y=380)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Describe the single transformation that moves X, Y to X plus 4, Y minus 2. Ben answers. Which line is wrong?", do=LINES("Ben", "(x, y) → (x + 4, y − 2)", ["a translation"])),
        dict(say="Line 1 is not complete. A translation needs its vector.", do=[dict(a="cross", id="l1")]),
        dict(say="A translation by the vector 4, negative 2.", do=[B("translation (4 over −2)", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Game engines", steps=[
        dict(say="Game engines and robot arms combine rotations and translations many times every second, to move objects into place.", do=[E("🤖", 90, 170, 100), T("rotate + translate, many times a second", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("13.3-k4", "One last question. Images after reflections, rotations and translations are always: congruent, or bigger? Pause the video and choose.", "Images are always …"),
        dict(say="Congruent. Same size, same shape.", do=[B("congruent", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: apply the second transformation to the image.", do=[T("• Second one on the image", x=80, y=170)]),
        dict(say="Two transformations can equal one.", do=[T("• Two can equal one", x=80, y=250)]),
        dict(say="Order can matter.", do=[T("• Order can matter", x=80, y=330)]),
        dict(say="The images stay congruent.", do=[T("• Images stay congruent", x=80, y=410)]),
    ]),
]

VIDEOS["13.4"] = [
    dict(kind="hook", title="A poster", steps=[
        dict(say="A photo is 10 centimetres by 15 centimetres. It is enlarged by scale factor 3 to make a poster.",
             do=[E("🖼️", 90, 170, 100), T("**10 cm × 15 cm** · scale factor **3**", x=230, y=200)]),
        PAUSE("13.4-k1", "How does the area change: 9 times bigger, or 3 times bigger? Pause the video and choose.", "Area becomes …"),
    ]),
    dict(kind="hook", title="9 times", steps=[
        dict(say="9 times bigger. Both the length and the width are multiplied by 3, and 3 times 3 is 9.", do=[B("3 × 3 = 9 times", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Enlargement", steps=[
        dict(say="Remember: in an enlargement, every length is multiplied by the scale factor. The angles stay the same.", do=[T("lengths **× k** · angles **unchanged**", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Perimeter and area", steps=[
        dict(say="When lengths are multiplied by K, the perimeter is multiplied by K, but the area is multiplied by K squared.",
             do=[B("perimeter × k · area × k²", x=80, y=170, color=BLUE), TBL(["", "Photo", "Poster", "Change"], [["Sides", "10 × 15", "30 × 45", "× 3"], ["Perimeter", "50 cm", "150 cm", "× 3"], ["Area", "150 cm²", "?", "× 9"]], y=270), ROW(0, 3), ROW(1, 5), ROW(2, 7)]),
        PAUSE("13.4-k2", "Your turn. What is the area of the poster, in square centimetres? Pause the video and try it.", "Poster area (cm²)?"),
    ]),
    dict(kind="idea", title="Check: 1350", steps=[
        dict(say="30 times 45 is 1,350. Or 150 times 9 is 1,350.", do=[B("30 × 45 = 150 × 9 = 1350 cm²", x=80, y=190, color=GREEN)]),
        dict(say="The scale factor is the image length divided by the object length. To find the centre, draw lines through matching corners, and extend them. They meet at the centre.", do=[T("k = image ÷ object · **ray lines** meet at the centre", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I work with enlargements?", steps=[
        dict(say="Here is the method. Step 1: find the scale factor.", do=[T("1. Scale factor **k**", x=80, y=170)]),
        dict(say="Step 2: from the centre, multiply each distance by K.", do=[T("2. From the **centre**, distances × k", x=80, y=260)]),
        dict(say="Step 3: lengths and perimeter times K; area times K squared.", do=[T("3. Perimeter × k · area × **k²**", x=80, y=350)]),
        dict(say="Step 4: check the angles are the same.", do=[T("4. **Check** the angles", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="From a centre", steps=[
        dict(say="Enlarge the point 5, 3 by scale factor 2, with centre 1, 1. From the centre, the point is 4 across and 2 up. Double it: 8 across and 4 up. The image is 9, 5.",
             do=[MATH("(1, 1) + 2 × (4, 2) = (9, 5)", x=80, y=180)]),
        PAUSE("13.4-k3", "Your turn. Enlarge the point 4, 2 by scale factor 3, with centre 1, 1. Pause and work it out.", "Enlarge (4, 2) by 3, centre (1, 1)."),
    ]),
    dict(kind="example", title="Check: (10, 4)", steps=[
        dict(say="From the centre: 3 across and 1 up. Times 3: 9 across and 3 up. The image is 10, 4.", do=[B("(1, 1) + 3 × (3, 1) = (10, 4)", x=80, y=190, color=GREEN)]),
        dict(say="A 4 by 6 rectangle is enlarged by scale factor 2.5. The area 24 is multiplied by 6.25: 150 square centimetres.", do=[MATH("24 × 2.5² = 150 cm²", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A 3 by 5 rectangle is enlarged by scale factor 2. Zoe finds the new area. Which line is wrong?", do=LINES("Zoe", "3 × 5 rectangle, scale factor 2: area?", ["15 × 2 = 30 cm²"])),
        dict(say="Line 1 is wrong. Both lengths double, so the area is multiplied by 4.", do=[dict(a="cross", id="l1")]),
        dict(say="6 times 10 is 60 square centimetres.", do=[B("6 × 10 = 60 cm²", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Printing", steps=[
        dict(say="Doubling the width and height of a printed photo uses about four times as much ink.", do=[E("🖨️", 90, 170, 100), T("double the size → **4 ×** the ink", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("13.4-k4", "One last question. Two similar shapes have areas of 12 and 108. What is the scale factor? Pause the video and answer.", "Areas 12 and 108. k?"),
        dict(say="108 divided by 12 is 9. That is K squared, so K is 3.", do=[B("k² = 9 → k = 3", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: lengths and perimeter are multiplied by K.", do=[T("• Lengths, perimeter × k", x=80, y=170)]),
        dict(say="Area is multiplied by K squared.", do=[T("• Area × k²", x=80, y=250)]),
        dict(say="K is the image length divided by the object length.", do=[T("• k = image ÷ object", x=80, y=330)]),
        dict(say="Ray lines meet at the centre.", do=[T("• Ray lines meet at the centre", x=80, y=410)]),
    ]),
]
