# -*- coding: utf-8 -*-
"""Stage 8 · Unit 12 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW, STEPT
from .s7_u12 import SQ, PARTS, Y, BL, GAP

PARTS3 = lambda a, b, c, label="", x=80, y=200, at=0: T(SQ("#1F9D61", a, label) + GAP + SQ(BL, b, label) + GAP + SQ("#E0483E", c, label), x=x, y=y, at=at)

VIDEOS = {}

VIDEOS["12.1"] = [
    dict(kind="hook", title="Pastry", steps=[
        dict(say="A pastry recipe uses 0.5 kilograms of flour and 250 grams of butter. Another recipe uses flour and butter in the ratio 3 to 2.",
             do=[E("🥐", 90, 170, 100), T("recipe 1: **0.5 kg** flour, **250 g** butter", x=230, y=190), T("recipe 2: flour : butter = **3 : 2**", x=230, y=270)]),
        PAUSE("12.1-k1", "Which recipe is more buttery? Pause the video and choose.", "Which recipe is more buttery?"),
    ]),
    dict(kind="hook", title="Same units first", steps=[
        dict(say="Change to the same units. 0.5 kilograms is 500 grams. So recipe 1 is 500 to 250, which simplifies to 2 to 1.", do=[MATH("500 g : 250 g = 2 : 1", x=80, y=190)]),
        dict(say="Recipe 1 has 2 parts of flour for each part of butter. Recipe 2 has 3 to 2, which is 1.5 to 1. Less flour for each part of butter, so recipe 2 is more buttery.",
             do=[MATH("3 : 2 = 1.5 : 1", x=80, y=290), B("recipe 2 (3 : 2) is more buttery", x=80, y=390, color=GREEN, at=7)]),
    ]),
    dict(kind="recall", title="Simplest form", steps=[
        dict(say="Remember: to simplify a ratio, divide all the parts by their highest common factor. 12 to 18 simplifies to 2 to 3. 45 to 60 simplifies to 3 to 4.",
             do=[MATH("12 : 18 = 2 : 3", x=80, y=180), MATH("45 : 60 = 3 : 4", x=80, y=270, at=6)]),
    ]),
    dict(kind="idea", title="Different units", steps=[
        dict(say="If the units are different, change them to the same units first.", do=[B("same units first", x=80, y=170, color=BLUE)]),
        dict(say="To compare ratios, write them in the form n to 1, or 1 to n. Then they are easy to compare.", do=[T("compare with **n : 1** or **1 : n**", x=80, y=270)]),
        PAUSE("12.1-k2", "Your turn. Simplify 400 metres to 1.2 kilometres. Pause the video and try it.", "Simplify 400 m : 1.2 km."),
    ]),
    dict(kind="idea", title="Check: 400 m : 1.2 km", steps=[
        dict(say="1.2 kilometres is 1,200 metres. 400 to 1,200. Divide both by 400: 1 to 3.", do=[MATH("400 : 1200 = 1 : 3", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Decimals, fractions, three parts", steps=[
        dict(say="Clear decimals by multiplying. 1.2 to 0.8 is 12 to 8, which is 3 to 2.", do=[MATH("1.2 : 0.8 = 12 : 8 = 3 : 2", x=80, y=170)]),
        dict(say="Clear fractions by multiplying by a common denominator. A half to a third, times 6, is 3 to 2.", do=[MATH("½ : ⅓ = 3 : 2  (× 6)", x=80, y=260)]),
        dict(say="Three-part ratios simplify in the same way. 24 to 36 to 60, divided by 12, is 2 to 3 to 5.", do=[MATH("24 : 36 : 60 = 2 : 3 : 5", x=80, y=350)]),
    ]),
    dict(kind="method", title="How do I simplify and compare ratios?", steps=[
        dict(say="Here is the method. Step 1: change to the same units, and clear any decimals or fractions.", do=[T("1. Same **units**; clear decimals and fractions", x=80, y=170)]),
        dict(say="Step 2: divide all the parts by the H C F.", do=[T("2. Divide by the **HCF**", x=80, y=260)]),
        dict(say="Step 3: to compare, write each ratio in the form 1 to n, or n to 1.", do=[T("3. Compare with **1 : n** or **n : 1**", x=80, y=350)]),
        dict(say="Step 4: keep the parts in the same order as the question.", do=[T("4. Keep the **order**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A decimal ratio", steps=[
        dict(say="Simplify 3 quarters to 2 thirds. Multiply both by 12: 9 to 8.", do=[MATH("¾ : ⅔ = 9 : 8", x=80, y=170)]),
        PAUSE("12.1-k3", "Your turn. Simplify 0.6 to 1.5. Pause and work it out.", "Simplify 0.6 : 1.5."),
    ]),
    dict(kind="example", title="Check: 0.6 : 1.5", steps=[
        dict(say="Multiply by 10: 6 to 15. Divide by 3: 2 to 5.", do=[MATH("6 : 15 = 2 : 5", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="A map scale", steps=[
        dict(say="A map's scale is 4 centimetres to 1 kilometre. Write it as 1 to n. 1 kilometre is 100,000 centimetres. So it is 4 to 100,000. Divide by 4: 1 to 25,000.",
             do=[E("🗺️", 90, 160, 90), MATH("4 : 100 000", x=230, y=180), B("1 : 25 000", x=230, y=290, color=GREEN, at=9)]),
    ]),
    dict(kind="example", title="Comparing classes", steps=[
        dict(say="Class A has 12 boys and 18 girls. Class B has 10 boys and 14 girls. Which has more girls per boy? A: 18 divided by 12 is 1.5. B: 14 divided by 10 is 1.4. Class A.",
             do=[MATH("A: 18 ÷ 12 = 1.5", x=80, y=180), MATH("B: 14 ÷ 10 = 1.4", x=80, y=270, at=6), B("class A", x=80, y=370, color=GREEN, at=9)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Jo simplifies 300 grams to 2 kilograms. Which line is wrong?", do=LINES("Jo", "300 g : 2 kg", ["÷ 2 → 150 : 1"])),
        dict(say="Line 1 is wrong. She ignored the units. Change to the same units first: 300 grams to 2,000 grams.", do=[dict(a="cross", id="l1")]),
        dict(say="Divide by 100: 3 to 20.", do=[B("300 : 2000 = 3 : 20", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Screen shapes", steps=[
        dict(say="Screens are described by ratios. A widescreen TV is 16 to 9. An older TV was 4 to 3.", do=[E("📺", 90, 170, 100), T("widescreen **16 : 9** · older **4 : 3**", x=230, y=200)]),
        dict(say="In the form n to 1, 16 to 9 is about 1.78 to 1, and 4 to 3 is about 1.33 to 1. So widescreen is much wider for its height.", do=[MATH("1.78 : 1 vs 1.33 : 1", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("12.1-k4", "One last question. Write 5 to 8 in the form 1 to n. What is n? Pause the video and answer.", "5 : 8 as 1 : n. n = ?"),
        dict(say="Divide both parts by 5. 8 divided by 5 is 1.6. So it is 1 to 1.6.", do=[MATH("5 : 8 = 1 : 1.6", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: use the same units, clear decimals and fractions, then divide by the H C F.", do=[T("• Same units; no decimals or fractions; ÷ HCF", x=80, y=170)]),
        dict(say="The forms 1 to n, and n to 1, help you compare.", do=[T("• 1 : n or n : 1 to compare", x=80, y=250)]),
        dict(say="Three-part ratios work the same way.", do=[T("• Three-part ratios work the same way", x=80, y=330)]),
        dict(say="Keep the order of the parts.", do=[T("• Keep the order", x=80, y=410)]),
    ]),
]

VIDEOS["12.2"] = [
    dict(kind="hook", title="Sharing the money", steps=[
        dict(say="Three friends buy a painting together. Ana pays 200 dollars, Ben 300 dollars, and Cara 100 dollars. Later they sell it for 840 dollars.",
             do=[E("🖼️", 90, 170, 100), T("Ana **$200** · Ben **$300** · Cara **$100** · sold for **$840**", x=230, y=200)]),
        dict(say="To be fair, they share the money in the same ratio as they paid: 200 to 300 to 100, which is 2 to 3 to 1.", do=[MATH("200 : 300 : 100 = 2 : 3 : 1", x=230, y=300)]),
        PAUSE("12.2-k1", "What is Ana's fair share of 840 dollars? Pause the video and work it out.", "Ana's fair share of $840 (ratio 2 : 3 : 1)?"),
    ]),
    dict(kind="hook", title="Find one part", steps=[
        dict(say="2 plus 3 plus 1 is 6 parts. One part is 840 divided by 6, which is 140 dollars.",
             do=[PARTS3(2, 3, 1, "140", y=170), STEPT("Working", [["one part", "840 ÷ 6 = 140"], ["Ana", "2 × 140 = $280"], ["Ben", "3 × 140 = $420"], ["Cara", "1 × 140 = $140"]], y=270), ROW(0, 3)]),
        dict(say="Ana gets 2 parts, 280 dollars. Ben gets 420, and Cara gets 140. Check: they add up to 840.", do=[ROW(1, 0.3), ROW(2, 2), ROW(3, 3.4)]),
    ]),
    dict(kind="recall", title="Sharing in a ratio", steps=[
        dict(say="Remember: to share 60 in the ratio 2 to 3, there are 5 parts. One part is 12. So the shares are 24 and 36.", do=[PARTS(2, 3, "12", y=180), MATH("24 and 36", x=80, y=300)]),
    ]),
    dict(kind="idea", title="Total, one share, or a difference", steps=[
        dict(say="Always find the value of one part first. From a total: divide the total by the number of parts.", do=[B("find **one part** first", x=80, y=170, color=BLUE), T("from the **total**: total ÷ number of parts", x=80, y=260)]),
        dict(say="From one share: if Ben got 420 dollars for 3 parts, one part is 140.", do=[T("from **one share**: 420 ÷ 3 = 140", x=80, y=340)]),
        dict(say="From a difference: if Ben got 280 dollars more than Cara, that is 2 parts. So one part is 140.", do=[T("from a **difference**: 280 ÷ 2 = 140", x=80, y=420)]),
        PAUSE("12.2-k2", "Your turn. Share 56 in the ratio 3 to 4 to 7. What is the smallest share? Pause the video and try it.", "Share 56 in 3 : 4 : 7. Smallest?"),
    ]),
    dict(kind="idea", title="Check: 56 in 3 : 4 : 7", steps=[
        dict(say="3 plus 4 plus 7 is 14 parts. One part is 56 divided by 14, which is 4. The smallest share is 3 times 4, which is 12.", do=[MATH("56 ÷ 14 = 4", x=80, y=190), B("3 × 4 = 12", x=80, y=290, color=GREEN, at=5)]),
    ]),
    dict(kind="method", title="How do I solve a ratio problem?", steps=[
        dict(say="Here is the method. Step 1: simplify the ratio if you can.", do=[T("1. **Simplify** the ratio", x=80, y=170)]),
        dict(say="Step 2: decide what you know: the total, one share, or a difference.", do=[T("2. Total, one share, or a **difference**?", x=80, y=260)]),
        dict(say="Step 3: find the value of one part.", do=[T("3. Find **one part**", x=80, y=350)]),
        dict(say="Step 4: multiply to get each share. Check that they add up to the total.", do=[T("4. Multiply; **check** the total", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="From a difference", steps=[
        dict(say="Red sweets and blue sweets are in the ratio 5 to 3. There are 12 more red than blue. How many sweets altogether?", do=[PARTS(5, 3, y=170, ca="#E0483E")]),
        dict(say="The difference is 2 parts, which is 12. So one part is 6. The total is 8 parts, which is 48 sweets.", do=[MATH("2 parts = 12 → 1 part = 6", x=80, y=290), B("8 × 6 = 48", x=80, y=390, color=GREEN, at=5)]),
        PAUSE("12.2-k3", "Your turn. Cats and dogs are in the ratio 2 to 5. There are 15 dogs. How many cats? Pause and work it out.", "Cats : dogs = 2 : 5; 15 dogs. Cats?"),
    ]),
    dict(kind="example", title="Check: cats and dogs", steps=[
        dict(say="5 parts is 15 dogs, so one part is 3. Cats are 2 parts, which is 6.", do=[MATH("5 parts = 15 → 1 part = 3", x=80, y=190), B("cats = 2 × 3 = 6", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="Angles in a ratio", steps=[
        dict(say="A triangle's angles are in the ratio 2 to 3 to 4. Find them. The angles add up to 180 degrees, and there are 9 parts. One part is 20 degrees. The angles are 40, 60 and 80 degrees.",
             do=[MATH("9 parts = 180° → 1 part = 20°", x=80, y=180), B("40°, 60°, 80°", x=80, y=290, color=GREEN, at=9)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Max shares 720 dollars in the ratio 2 to 3 to 4. Which line goes wrong first?", do=LINES("Max", "$720 in 2 : 3 : 4", ["720 ÷ 3 = 240 (three people)", "shares 480, 720, 960"])),
        dict(say="Line 1 is wrong. Divide by the total number of parts, which is 9, not by the number of people. And his shares add up to much more than 720!", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="One part is 80. The shares are 160, 240 and 320 dollars.", do=[B("160, 240, 320", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Business partners", steps=[
        dict(say="Business partners often share profits in the ratio of the money they put in. The painting cost 600 dollars and sold for 840, so the profit was 240 dollars.",
             do=[E("🤝", 90, 170, 100), MATH("profit = 840 − 600 = $240", x=230, y=190)]),
        dict(say="Shared 2 to 3 to 1, that is 6 parts of 40 dollars: Ana's profit is 80, Ben's 120, and Cara's 40.", do=[MATH("80, 120, 40", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("12.2-k4", "One last question. A triangle's angles are in the ratio 1 to 1 to 2. What is the largest angle? Pause the video and answer.", "Angles 1 : 1 : 2 in a triangle. Largest?"),
        dict(say="4 parts make 180 degrees, so one part is 45. The largest angle is 2 parts, which is 90 degrees.", do=[MATH("180 ÷ 4 = 45", x=80, y=190), B("2 × 45 = 90°", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the total divided by the number of parts gives one part.", do=[T("• Total ÷ number of parts = **one part**", x=80, y=170)]),
        dict(say="From one share, or a difference, find one part first.", do=[T("• From a share or a difference: find one part", x=80, y=250)]),
        dict(say="The shares must add up to the total.", do=[T("• Shares add up to the total", x=80, y=330)]),
        dict(say="Profits and angles can be shared in ratios too.", do=[T("• Profits and angles can be shared too", x=80, y=410)]),
    ]),
]

VIDEOS["12.3"] = [
    dict(kind="hook", title="Shades of green", steps=[
        dict(say="To make a shade of green, Ali mixes 2 litres of blue with 3 litres of yellow. Bea mixes 3 litres of blue with 5 litres of yellow.",
             do=[E("🎨", 90, 170, 100), PARTS(2, 3, y=180, ca=BL, cb=Y), PARTS(3, 5, y=280, ca=BL, cb=Y, at=3)]),
        PAUSE("12.3-k1", "Will the two shades be the same? Pause the video and choose.", "Same shade?"),
    ]),
    dict(kind="hook", title="Different shades", steps=[
        dict(say="No. Write each as blue to 1 litre of yellow. Ali: 2 to 3 is about 0.67 to 1. Bea: 3 to 5 is 0.6 to 1. The ratios are different, so the shades are different. Ali's is bluer.",
             do=[MATH("Ali: 2 : 3 ≈ 0.67 : 1", x=80, y=180), MATH("Bea: 3 : 5 = 0.6 : 1", x=80, y=270, at=5), B("different — Ali's is bluer", x=80, y=370, color=GREEN, at=9)]),
    ]),
    dict(kind="recall", title="The unitary method", steps=[
        dict(say="Remember the unitary method. If 4 pens cost 6 dollars, 1 pen costs 1 dollar 50, and 7 pens cost 10 dollars 50.", do=[MATH("4 → $6 · 1 → $1.50 · 7 → $10.50", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Direct proportion", steps=[
        dict(say="Two quantities are in direct proportion if their ratio stays the same. To get the same shade, the ratio of blue to yellow must not change.", do=[B("direct proportion: the ratio **stays the same**", x=80, y=170, color=BLUE)]),
        dict(say="So to make more of Ali's green, multiply both parts by the same number. 2 to 3 becomes 4 to 6, or 10 to 15.", do=[MATH("2 : 3 = 4 : 6 = 10 : 15", x=80, y=280)]),
        PAUSE("12.3-k2", "Your turn. Sand and cement are mixed in the ratio 4 to 1. How much cement goes with 26 kilograms of sand? Pause the video and try it.", "Sand : cement = 4 : 1. Cement for 26 kg sand?"),
    ]),
    dict(kind="idea", title="Check: 26 kg of sand", steps=[
        dict(say="4 parts is 26 kilograms, so 1 part is 26 divided by 4, which is 6.5 kilograms of cement.", do=[B("26 ÷ 4 = 6.5 kg", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Best buys", steps=[
        dict(say="To compare prices, find a unit rate, like the price per 100 grams.", do=[TBL(["Pack", "Price", "Per 100 g"], [["400 g", "$3.60", "$0.90"], ["650 g", "$5.53", "$0.85"]], y=170), ROW(0, 2), ROW(1, 4)]),
        dict(say="The 650 gram pack is better value, because it costs less per 100 grams.", do=[T("650 g is the **better buy**", x=80, y=380, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I solve proportion problems?", steps=[
        dict(say="Here is the method. Step 1: write the ratio, with the units in the same order.", do=[T("1. Write the ratio, units **in order**", x=80, y=170)]),
        dict(say="Step 2: find the multiplier from the quantity you know, or use the unitary method.", do=[T("2. Find the **multiplier** (or one unit)", x=80, y=260)]),
        dict(say="Step 3: multiply the other part by the same number.", do=[T("3. Multiply the other part by the **same** number", x=80, y=350)]),
        dict(say="Step 4: to compare, find unit rates. The best buy has the lowest price per unit.", do=[T("4. Compare with **unit rates**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A recipe", steps=[
        dict(say="Flour and sugar are in the ratio 5 to 2. How much flour goes with 350 grams of sugar? 2 parts is 350, so 1 part is 175. 5 parts is 875 grams.",
             do=[E("🍪", 90, 160, 90), MATH("2 parts = 350 → 1 part = 175", x=230, y=180), B("5 × 175 = 875 g", x=230, y=290, color=GREEN, at=8)]),
        PAUSE("12.3-k3", "Your turn. Which is better value: 300 grams for 2 dollars 40, or 500 grams for 3 dollars 90? Pause and choose.", "Better: 300 g $2.40 or 500 g $3.90?"),
    ]),
    dict(kind="example", title="Check: best buy", steps=[
        dict(say="300 grams for 2 dollars 40 is 80 cents per 100 grams. 500 grams for 3 dollars 90 is 78 cents per 100 grams. The 500 gram pack is better value.",
             do=[MATH("300 g: $0.80 per 100 g", x=80, y=180), MATH("500 g: $0.78 per 100 g", x=80, y=270, at=4), B("500 g", x=80, y=370, color=GREEN, at=7)]),
    ]),
    dict(kind="example", title="Is it proportional?", steps=[
        dict(say="Here x is 2, 5, 8, and y is 7, 17.5, 28. Are they in direct proportion? Divide y by x: 3.5, 3.5, 3.5. The same every time, so yes. y equals 3.5 x.",
             do=[TBL(["x", "2", "5", "8"], [["y", "7", "17.5", "28"], ["y ÷ x", "3.5", "3.5", "3.5"]], y=170), ROW(0, 0.5), ROW(1, 6), B("yes: y = 3.5x", x=80, y=400, color=GREEN, at=10)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ali's mix is 2 blue to 3 yellow. He uses 6 litres of yellow. How much blue? Which line goes wrong first?", do=LINES("Ali", "2 blue : 3 yellow, with 6 yellow", ["yellow went up by 3", "so blue = 2 + 3 = 5"])),
        dict(say="Line 1 is wrong. Ratios scale by multiplying, not adding. Yellow was multiplied by 2.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="So blue is 2 times 2, which is 4 litres.", do=[B("blue = 2 × 2 = 4 litres", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Concrete", steps=[
        dict(say="Builders mix concrete in ratios of cement, sand and gravel, such as 1 to 2 to 3. If the ratio changes, the concrete can be weak.", do=[E("🏗️", 90, 170, 100), T("cement : sand : gravel = **1 : 2 : 3**", x=230, y=200)]),
        dict(say="For a big job they scale up every part by the same multiplier: 50 kilograms of cement needs 100 of sand and 150 of gravel.", do=[MATH("50 : 100 : 150 kg", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("12.3-k4", "One last question. y is in direct proportion to x. y is 12 when x is 3. What is y when x is 10? Pause the video and answer.", "y ∝ x; y = 12 when x = 3. y when x = 10?"),
        dict(say="12 divided by 3 is 4, so y equals 4 x. When x is 10, y is 40.", do=[MATH("y = 4x", x=80, y=190), B("4 × 10 = 40", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: in direct proportion, the ratio stays the same.", do=[T("• Direct proportion: the ratio **stays the same**", x=80, y=170)]),
        dict(say="Scale both parts by the same multiplier.", do=[T("• Scale both parts by the same multiplier", x=80, y=250)]),
        dict(say="Compare using 1 to n, or unit rates.", do=[T("• Compare with 1 : n or unit rates", x=80, y=330)]),
        dict(say="The best buy has the lowest price per unit.", do=[T("• Best buy = lowest price per unit", x=80, y=410)]),
    ]),
]
