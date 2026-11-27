# -*- coding: utf-8 -*-
"""Stage 7 · Unit 12 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u07 import F

SQ = lambda color, n, label="": "".join(f'<span style="display:inline-flex;align-items:center;justify-content:center;width:58px;height:58px;margin-right:8px;border-radius:10px;background:{color};color:#fff;font-weight:700">{label}</span>' for _ in range(n))
Y, BL, GAP = "#F2B705", "#3B7DD8", '<span style="display:inline-block;width:26px"></span>'
PARTS = lambda a, b, label="", x=80, y=200, at=0, ca="#1F9D61", cb=BL: T(SQ(ca, a, label) + GAP + SQ(cb, b, label), x=x, y=y, at=at)   # a ratio as coloured parts

VIDEOS = {}

VIDEOS["12.1"] = [
    dict(kind="hook", title="Mixing paint", steps=[
        dict(say="To make a shade of green, a decorator mixes 6 tins of yellow paint with 4 tins of blue paint.", do=[E("🎨", 90, 150, 100), PARTS(6, 4, x=230, y=170, ca=Y), T("**6** yellow · **4** blue", x=230, y=260)]),
        dict(say="For a small job, she wants the same shade of green, but with fewer tins.", do=[T("same shade, **fewer tins**?", x=230, y=350)]),
        PAUSE("12.1-k1", "What is the simplest ratio of yellow to blue? Pause the video and work it out.", "Simplify 6 tins yellow : 4 tins blue."),
    ]),
    dict(kind="hook", title="Half of each", steps=[
        dict(say="Split the tins into 2 equal groups. Each group has 3 yellow and 2 blue.", do=[PARTS(3, 2, y=170, ca=Y), PARTS(3, 2, y=250, ca=Y, at=1)]),
        dict(say="So 3 tins of yellow with 2 tins of blue makes the same shade. The ratio 6 to 4 is the same as 3 to 2.", do=[B("6 : 4 = 3 : 2", x=80, y=380, color=GREEN)]),
    ]),
    dict(kind="recall", title="Highest common factor", steps=[
        dict(say="Remember: the highest common factor of 2 numbers is the biggest number that divides both of them.", do=[T("**HCF**: the biggest number that divides both", x=80, y=170)]),
        dict(say="The highest common factor of 18 and 24 is 6.", do=[MATH("HCF of 18 and 24 = 6", x=80, y=280, color=BLUE)]),
    ]),
    dict(kind="idea", title="What a ratio means", steps=[
        dict(say="A ratio compares quantities. Yellow to blue is 6 to 4. We write it with a colon.", do=[T("yellow : blue", x=80, y=160), B("6 : 4", x=80, y=230, color=BLUE)]),
        dict(say="The order matters. Blue to yellow is 4 to 6.", do=[T("blue : yellow", x=520, y=160), B("4 : 6", x=520, y=230, color=RED)]),
        dict(say="To simplify a ratio, divide every part by the same number. It is best to divide by the highest common factor.", do=[T("**Simplify**: divide **every part** by the HCF", x=80, y=380), MATH("6 : 4 = 3 : 2 (÷ 2)", x=80, y=470, at=4)]),
        PAUSE("12.1-k2", "Your turn. Simplify the ratio 14 to 35. Pause the video and try it.", "Simplify 14 : 35."),
    ]),
    dict(kind="idea", title="Check: 14 : 35", steps=[
        dict(say="The highest common factor of 14 and 35 is 7. 14 divided by 7 is 2. 35 divided by 7 is 5. The answer is 2 to 5.", do=[T("HCF = **7**", x=80, y=180), B("14 : 35 = 2 : 5", x=80, y=280, color=GREEN, at=4)]),
    ]),
    dict(kind="idea", title="Units, and three parts", steps=[
        dict(say="Before you simplify, both parts must be in the same units. 50 centimetres to 2 metres is 50 centimetres to 200 centimetres. That simplifies to 1 to 4.",
             do=[T("use the **same units**", x=80, y=150), MATH("50 cm : 2 m = 50 : 200 = 1 : 4", x=80, y=230, at=3)]),
        dict(say="A ratio can have 3 parts. 12 to 18 to 30. Divide every part by 6, to get 2 to 3 to 5.", do=[T("**three parts** work the same way", x=80, y=370), MATH("12 : 18 : 30 = 2 : 3 : 5 (÷ 6)", x=80, y=450, at=3)]),
        PAUSE("12.1-k3", "Your turn. Simplify 6 to 9 to 12. Pause the video and try it.", "Simplify 6 : 9 : 12."),
    ]),
    dict(kind="idea", title="Check: 6 : 9 : 12", steps=[
        dict(say="The highest common factor of 6, 9 and 12 is 3. Divide every part by 3. The answer is 2 to 3 to 4.", do=[T("HCF = **3**", x=80, y=180), B("6 : 9 : 12 = 2 : 3 : 4", x=80, y=280, color=GREEN, at=4)]),
    ]),
    dict(kind="idea", title="Ratios and fractions", steps=[
        dict(say="A ratio also tells you fractions of the total. In the paint, yellow to blue is 3 to 2. That makes 5 parts altogether.", do=[PARTS(3, 2, y=170, ca=Y), T("3 + 2 = **5 parts**", x=80, y=270)]),
        dict(say="So 3 fifths of the mixture is yellow, and 2 fifths is blue.", do=[MATH(f"yellow = {F(3, 5)}", x=80, y=370), MATH(f"blue = {F(2, 5)}", x=520, y=370, at=2.4)]),
    ]),
    dict(kind="method", title="How do I simplify a ratio?", steps=[
        dict(say="Here is the method. Step 1: put all the parts in the same units. If there are decimals, multiply to make whole numbers.", do=[T("1. **Same units**, whole numbers", x=80, y=170)]),
        dict(say="Step 2: find the highest common factor of all the parts.", do=[T("2. Find the **HCF**", x=80, y=260)]),
        dict(say="Step 3: divide every part by it.", do=[T("3. **Divide** every part", x=80, y=350)]),
        dict(say="Step 4: check. The only common factor left should be 1.", do=[T("4. Check: no common factor left", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Two parts", steps=[
        dict(say="Simplify 56 to 42.", do=[B("56 : 42", x=80, y=160)]),
        dict(say="The highest common factor of 56 and 42 is 14.", do=[T("HCF = **14**", x=80, y=280)]),
        dict(say="56 divided by 14 is 4. 42 divided by 14 is 3. The answer is 4 to 3.", do=[MATH("56 ÷ 14 = 4 · 42 ÷ 14 = 3", x=80, y=360), B("4 : 3", x=80, y=460, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Different units", steps=[
        dict(say="Simplify 600 grams to 1.5 kilograms.", do=[B("600 g : 1.5 kg", x=80, y=160)]),
        dict(say="First use the same units. 1.5 kilograms is 1,500 grams.", do=[MATH("600 : 1500", x=80, y=280)]),
        dict(say="Divide both parts by 300. The answer is 2 to 5.", do=[T("÷ 300", x=420, y=296, color=GREY), B("2 : 5", x=80, y=390, color=GREEN)]),
    ]),
    dict(kind="example", title="Decimals in a ratio", steps=[
        dict(say="Simplify 1.2 to 3.", do=[B("1.2 : 3", x=80, y=160)]),
        dict(say="Multiply both parts by 10, to get whole numbers: 12 to 30.", do=[MATH("12 : 30", x=80, y=280), T("× 10", x=320, y=296, color=GREY)]),
        dict(say="Then divide both parts by 6. The answer is 2 to 5.", do=[T("÷ 6", x=320, y=406, color=GREY), B("2 : 5", x=80, y=390, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Simplify 36 to 48. Here is Eva's working. Which line goes wrong first?", do=LINES("Eva", "simplify 36 : 48", ["÷ 2 → 18 : 24", "Answer: 18 : 24"])),
        dict(say="Line 2 is wrong. The ratio is not fully simplified. 18 and 24 can both still be divided by 6.", do=[dict(a="cross", id="l2")]),
        dict(say="Divide by the highest common factor, 12, straight away. 36 to 48 is 3 to 4.", do=[B("36 : 48 = 3 : 4 (÷ 12)", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Ratios you can see", steps=[
        dict(say="You are watching this video in a ratio. A Full HD screen is 1,920 pixels wide and 1,080 pixels high.", do=[E("🖥️", 90, 160, 100), MATH("1920 : 1080", x=230, y=180)]),
        dict(say="Divide both by 120, and you get 16 to 9. That is the shape of most screens today.", do=[B("16 : 9", x=560, y=170, color=GREEN)]),
        dict(say="On a bicycle, a front gear with 48 teeth drives a back gear with 16 teeth. That is a ratio of 3 to 1. One turn of the pedals turns the wheel 3 times.", do=[E("🚲", 90, 350, 100), MATH("48 : 16 = 3 : 1", x=230, y=370), T("1 turn of the pedals → **3 turns** of the wheel", x=230, y=470, at=7)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("12.1-k4", "One last question. Simplify 80 centimetres to 1.2 metres. Pause the video and work it out.", "Simplify 80 cm : 1.2 m."),
        dict(say="Use the same units. 1.2 metres is 120 centimetres. 80 to 120: divide both by 40. The answer is 2 to 3.", do=[MATH("80 : 120", x=80, y=190), T("÷ 40", x=360, y=206, color=GREY, at=4), B("2 : 3", x=80, y=300, color=GREEN, at=6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a ratio compares quantities, in a fixed order.", do=[T("• A ratio compares quantities – **order matters**", x=80, y=170)]),
        dict(say="Simplify by dividing every part by the highest common factor.", do=[T("• Simplify: divide every part by the **HCF**", x=80, y=250)]),
        dict(say="Use the same units in every part.", do=[T("• Use the **same units**", x=80, y=330)]),
        dict(say="Add the parts to find fractions of the total.", do=[T("• Add the parts → **fractions** of the total", x=80, y=410)]),
    ]),
]

VIDEOS["12.2"] = [
    dict(kind="hook", title="Sharing a prize", steps=[
        dict(say="2 friends enter a competition together. Amira paid 3 dollars of the entry fee, and Ben paid 2 dollars. They win 400 dollars!", do=[E("🏆", 90, 150, 110), T("Amira paid **$3** · Ben paid **$2** · prize **$400**", x=240, y=190)]),
        dict(say="They share the prize in the same ratio as they paid: 3 to 2.", do=[B("3 : 2", x=240, y=300, color=BLUE)]),
        PAUSE("12.2-k1", "How much does Amira get? Pause the video and work it out.", "$400 shared 3 : 2. How much does Amira (3 parts) get?"),
    ]),
    dict(kind="hook", title="Five equal parts", steps=[
        dict(say="3 parts for Amira and 2 parts for Ben make 5 equal parts. 400 divided by 5 is 80. Each part is worth 80 dollars.", do=[PARTS(3, 2, "80", y=170, at=4), T("3 + 2 = **5 parts**", x=80, y=270), MATH("400 ÷ 5 = 80", x=420, y=262, at=4)]),
        dict(say="Amira gets 3 parts: 3 times 80 is 240 dollars. Ben gets 2 parts: 160 dollars.", do=[B("Amira: $240", x=80, y=380, color=GREEN), B("Ben: $160", x=520, y=380, color=BLUE, at=4)]),
        dict(say="Check: 240 plus 160 is 400.", do=[MATH("240 + 160 = 400 ✓", x=80, y=500)]),
    ]),
    dict(kind="recall", title="Equal parts", steps=[
        dict(say="Remember: to share into equal parts, divide. 240 shared into 6 equal parts is 40 each.", do=[MATH("240 ÷ 6 = 40", x=80, y=190), PARTS(6, 0, "40", y=300, at=2)]),
    ]),
    dict(kind="idea", title="Sharing in a ratio", steps=[
        dict(say="Every sharing problem uses the same 3 steps. First, add the parts of the ratio.",
             do=[TBL(["Step", "Share $400 in the ratio 3 : 2"], [["1. Total parts", "3 + 2 = 5"], ["2. One part", "400 ÷ 5 = 80"], ["3. Each share", "3 × 80 = 240 and 2 × 80 = 160"]], y=170), ROW(0, 3)]),
        dict(say="Second, divide the amount by the total number of parts. That gives the value of 1 part.", do=[ROW(1, 0.3)]),
        dict(say="Third, multiply 1 part by each number in the ratio.", do=[ROW(2, 0.3)]),
        PAUSE("12.2-k2", "Your turn. Share 30 in the ratio 1 to 4. What is the smaller share? Pause the video and try it.", "Share 30 in the ratio 1 : 4. What is the smaller share?"),
    ]),
    dict(kind="idea", title="Check: 30 in the ratio 1 : 4", steps=[
        dict(say="1 plus 4 is 5 parts. 30 divided by 5 is 6. The smaller share is 1 part, which is 6. The larger share is 24.", do=[PARTS(1, 4, "6", y=170), MATH("30 ÷ 5 = 6", x=80, y=280), B("smaller share = 6", x=80, y=380, color=GREEN, at=5)]),
    ]),
    dict(kind="idea", title="When you know one share", steps=[
        dict(say="Sometimes you know 1 share, not the total. Red beads to blue beads is 4 to 7, and there are 28 red beads.", do=[T("red : blue = **4 : 7** · red = **28**", x=80, y=150), PARTS(4, 7, y=230, ca="#D64545")]),
        dict(say="The 4 red parts are worth 28. So 1 part is 28 divided by 4, which is 7.", do=[MATH("28 ÷ 4 = 7", x=80, y=340)]),
        dict(say="Blue is 7 parts: 7 times 7 is 49 blue beads.", do=[MATH("7 × 7 = 49", x=80, y=430), B("49 blue", x=420, y=424, color=BLUE, at=3)]),
        PAUSE("12.2-k3", "Your turn. Red to blue is 2 to 5. There are 14 red. How many blue? Pause the video and try it.", "Red : blue = 2 : 5. There are 14 red. How many blue?"),
    ]),
    dict(kind="idea", title="Check: 14 red", steps=[
        dict(say="2 parts are 14, so 1 part is 7. Blue is 5 parts: 5 times 7 is 35.", do=[MATH("14 ÷ 2 = 7", x=80, y=190), MATH("5 × 7 = 35", x=80, y=280, at=3), B("35 blue", x=80, y=380, color=GREEN, at=5)]),
    ]),
    dict(kind="method", title="How do I share in a ratio?", steps=[
        dict(say="Here is the method. Step 1: add the parts of the ratio.", do=[T("1. **Add** the parts", x=80, y=170)]),
        dict(say="Step 2: divide the amount by the total number of parts, to find 1 part.", do=[T("2. **Divide** to find 1 part", x=80, y=260)]),
        dict(say="Step 3: multiply 1 part by each number in the ratio.", do=[T("3. **Multiply** for each share", x=80, y=350)]),
        dict(say="Step 4: check that the shares add up to the total.", do=[T("4. **Check**: the shares add up", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Sharing stickers", steps=[
        dict(say="Share 63 stickers between Kai and Lola in the ratio 2 to 7.", do=[E("⭐", 90, 140, 80), T("**63** stickers · Kai : Lola = **2 : 7**", x=200, y=160)]),
        dict(say="2 plus 7 is 9 parts. 63 divided by 9 is 7 stickers in each part.", do=[MATH("2 + 7 = 9", x=80, y=280), MATH("63 ÷ 9 = 7", x=420, y=280, at=2.6)]),
        dict(say="Kai gets 2 times 7, which is 14. Lola gets 7 times 7, which is 49.", do=[B("Kai 14", x=80, y=400, color=GREEN), B("Lola 49", x=420, y=400, color=BLUE, at=3)]),
    ]),
    dict(kind="example", title="Three people", steps=[
        dict(say="900 dollars is shared in the ratio 2 to 3 to 4. Find each share.", do=[T("**$900** in the ratio **2 : 3 : 4**", x=80, y=160)]),
        dict(say="2 plus 3 plus 4 is 9 parts. 900 divided by 9 is 100 dollars for each part.", do=[MATH("2 + 3 + 4 = 9", x=80, y=270), MATH("900 ÷ 9 = 100", x=520, y=270, at=3)]),
        dict(say="The shares are 200 dollars, 300 dollars and 400 dollars.", do=[B("$200, $300, $400", x=80, y=400, color=GREEN)]),
    ]),
    dict(kind="example", title="Knowing one share", steps=[
        dict(say="A builder mixes cement and sand in the ratio 1 to 4. She uses 60 kilograms of sand. How much cement does she need?", do=[E("🧱", 90, 140, 80), T("cement : sand = **1 : 4** · sand = **60 kg**", x=200, y=160)]),
        dict(say="The 4 parts of sand are 60 kilograms. So 1 part is 15 kilograms. She needs 15 kilograms of cement.", do=[MATH("60 ÷ 4 = 15", x=80, y=290), B("cement: 15 kg", x=80, y=390, color=GREEN, at=5)]),
        dict(say="The whole mix is 5 parts: 75 kilograms.", do=[MATH("5 × 15 = 75 kg", x=80, y=500)]),
    ]),
    dict(kind="example", title="Using a difference", steps=[
        dict(say="In a club, boys to girls is 4 to 7. There are 15 more girls than boys. How many students are there?", do=[T("boys : girls = **4 : 7** · **15 more** girls", x=80, y=160), PARTS(4, 7, y=240)]),
        dict(say="The difference is 7 minus 4, which is 3 parts. Those 3 parts are 15 students. So 1 part is 5.", do=[MATH("7 − 4 = 3 parts = 15", x=80, y=350), MATH("1 part = 5", x=640, y=350, at=5)]),
        dict(say="Altogether there are 11 parts. 11 times 5 is 55 students.", do=[MATH("11 × 5 = 55", x=80, y=450), B("55 students", x=420, y=444, color=GREEN, at=3)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Share 90 dollars in the ratio 1 to 2. Here is Hugo's working. Which line goes wrong first?", do=LINES("Hugo", "share $90 in the ratio 1 : 2", ["90 ÷ 1 = 90 and 90 ÷ 2 = 45", "Shares: $90 and $45"])),
        dict(say="Line 1 is wrong. Those shares add up to 135 dollars, not 90. You must divide by the total number of parts.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="1 plus 2 is 3 parts. 90 divided by 3 is 30. The shares are 30 dollars and 60 dollars.", do=[B("3 parts → $30 and $60", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Ratios in materials", steps=[
        dict(say="Jewellers use ratios. 18 carat gold is 18 parts gold in every 24 parts. So gold to other metals is 18 to 6, which is 3 to 1.", do=[E("💍", 90, 160, 100), MATH("18 : 6 = 3 : 1", x=230, y=180), T("18-carat gold", x=560, y=196, color=GREY)]),
        dict(say="The air you breathe is a ratio too. Nitrogen to oxygen is about 4 to 1.", do=[E("🌬️", 90, 340, 100), T("air: nitrogen : oxygen ≈ **4 : 1**", x=230, y=370)]),
        dict(say="So in every 5 litres of air, about 1 litre is oxygen.", do=[T("5 litres of air → about **1 litre** of oxygen", x=230, y=480, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("12.2-k4", "One last question. Share 100 in the ratio 3 to 7. What is the larger share? Pause the video and answer.", "Share 100 in the ratio 3 : 7. What is the larger share?"),
        dict(say="3 plus 7 is 10 parts. 100 divided by 10 is 10. The larger share is 7 parts: 70.", do=[PARTS(3, 7, "10", y=170), MATH("100 ÷ 10 = 10", x=80, y=280), B("7 × 10 = 70", x=80, y=380, color=GREEN, at=4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: add the parts, find 1 part, then multiply.", do=[T("• **Add** the parts → **1 part** → **multiply**", x=80, y=170)]),
        dict(say="If you know 1 share, use it to find 1 part.", do=[T("• Know one share? Find **1 part** from it", x=80, y=250)]),
        dict(say="If you know the difference, use the difference in parts.", do=[T("• Know the difference? Use the **difference in parts**", x=80, y=330)]),
        dict(say="Always check that the shares add up to the total.", do=[T("• **Check**: the shares add up to the total", x=80, y=410)]),
    ]),
]

VIDEOS["12.3"] = [
    dict(kind="hook", title="Pancakes for a crowd", steps=[
        dict(say="A pancake recipe for 4 people uses 200 grams of flour, 2 eggs and 300 millilitres of milk.", do=[E("🥞", 90, 150, 110), T("for **4 people**: 200 g flour · 2 eggs · 300 ml milk", x=240, y=190)]),
        dict(say="Mo is cooking for 10 people.", do=[B("for 10 people?", x=240, y=300, color=BLUE)]),
        PAUSE("12.3-k1", "How much flour does Mo need? Pause the video and work it out.", "4 people need 200 g of flour. How much flour for 10 people?"),
    ]),
    dict(kind="hook", title="First find one", steps=[
        dict(say="First find the flour for 1 person. 200 divided by 4 is 50 grams.", do=[MATH("1 person: 200 ÷ 4 = 50 g", x=80, y=180)]),
        dict(say="Then multiply by 10. Mo needs 500 grams of flour.", do=[MATH("10 people: 10 × 50 = 500 g", x=80, y=270), B("500 g of flour", x=80, y=370, color=GREEN, at=3)]),
        dict(say="In the same way, he needs 5 eggs, and 750 millilitres of milk.", do=[T("eggs: **5** · milk: **750 ml**", x=80, y=490)]),
    ]),
    dict(kind="recall", title="One, then many", steps=[
        dict(say="Remember: if 1 pen costs 3 dollars, then 6 pens cost 18 dollars. And if 5 pens cost 4 dollars, 1 pen costs 4 divided by 5, which is 80 cents.", do=[MATH("1 pen $3 → 6 pens $18", x=80, y=190), MATH("5 pens $4 → 1 pen $0.80", x=80, y=290, at=5)]),
    ]),
    dict(kind="idea", title="Direct proportion", steps=[
        dict(say="2 quantities are in direct proportion if they grow at the same rate. Double one, and the other doubles. Halve one, and the other halves.", do=[T("**Direct proportion**: double one → the other **doubles**", x=80, y=150)]),
        dict(say="Flour and people are in direct proportion. 4 people need 200 grams. 8 people need 400 grams. 2 people need 100 grams.",
             do=[TBL(["People", "2", "4", "8", "10"], [["Flour (g)", "100", "200", "400", "500"]], y=240), ROW(0, 0.5)]),
        dict(say="The unitary method always works: find the value for 1, then multiply up.", do=[B("find 1, then multiply", x=80, y=440, color=BLUE)]),
        PAUSE("12.3-k2", "Your turn. 3 kilograms of rice cost 4 dollars 50. How much do 7 kilograms cost? Pause the video and try it.", "3 kg of rice costs $4.50. What is the cost of 7 kg?"),
    ]),
    dict(kind="idea", title="Check: 7 kg of rice", steps=[
        dict(say="1 kilogram costs 4.50 divided by 3, which is 1 dollar 50. 7 kilograms cost 7 times 1.50, which is 10 dollars 50.", do=[MATH("1 kg: 4.50 ÷ 3 = 1.50", x=80, y=190), MATH("7 kg: 7 × 1.50 = 10.50", x=80, y=280, at=5), B("$10.50", x=80, y=380, color=GREEN, at=8)]),
    ]),
    dict(kind="idea", title="Best buys", steps=[
        dict(say="Which pack is better value? To compare, find the price of the same amount of each. Here we find the price for 100 grams.",
             do=[TBL(["Pack", "Price", "Price per 100 g"], [["300 g", "$2.70", "2.70 ÷ 3 = $0.90"], ["500 g", "$4.00", "4.00 ÷ 5 = $0.80"]], y=170), ROW(0, 5)]),
        dict(say="The small pack costs 90 cents for 100 grams. The large pack costs 80 cents for 100 grams.", do=[ROW(1, 3)]),
        dict(say="So the large pack is better value.", do=[B("the 500 g pack", x=80, y=420, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I solve a proportion problem?", steps=[
        dict(say="Here is the method. Step 1: check that the quantities are in direct proportion. Does doubling one double the other?", do=[T("1. Is it **direct proportion**?", x=80, y=170)]),
        dict(say="Step 2: divide, to find the value for 1 unit.", do=[T("2. **Divide** to find 1 unit", x=80, y=260)]),
        dict(say="Step 3: multiply by the number of units you need.", do=[T("3. **Multiply** by the number you need", x=80, y=350)]),
        dict(say="Step 4: check that your answer is a sensible size.", do=[T("4. Is the answer a **sensible size**?", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Scaling a recipe", steps=[
        dict(say="A smoothie recipe for 5 people needs 750 millilitres of milk. How much milk is needed for 8 people?", do=[E("🥤", 90, 140, 80), T("**5 people**: 750 ml · **8 people**: ?", x=200, y=160)]),
        dict(say="For 1 person: 750 divided by 5 is 150 millilitres.", do=[MATH("750 ÷ 5 = 150", x=80, y=280)]),
        dict(say="For 8 people: 8 times 150 is 1,200 millilitres.", do=[MATH("8 × 150 = 1200", x=80, y=370), B("1200 ml", x=80, y=460, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="A printer", steps=[
        dict(say="A printer prints 180 pages in 6 minutes. How many pages does it print in 25 minutes?", do=[E("🖨️", 90, 140, 80), T("**180 pages** in 6 minutes · in 25 minutes?", x=200, y=160)]),
        dict(say="In 1 minute: 180 divided by 6 is 30 pages.", do=[MATH("180 ÷ 6 = 30", x=80, y=280)]),
        dict(say="In 25 minutes: 25 times 30 is 750 pages.", do=[MATH("25 × 30 = 750", x=80, y=370), B("750 pages", x=80, y=460, color=GREEN, at=3)]),
        PAUSE("12.3-k3", "Your turn. A car uses 6 litres of fuel for 80 kilometres. How many litres does it use for 200 kilometres? Pause the video and try it.", "A car uses 6 litres of fuel for 80 km. How many litres for 200 km?"),
    ]),
    dict(kind="example", title="Check: fuel for 200 km", steps=[
        dict(say="Half of 80 is 40, so 40 kilometres uses 3 litres. 200 kilometres is 5 lots of 40. 5 times 3 is 15 litres.", do=[MATH("40 km → 3 litres", x=80, y=190), MATH("200 km = 5 × 40 km", x=80, y=280, at=4), B("5 × 3 = 15 litres", x=80, y=380, color=GREEN, at=7)]),
    ]),
    dict(kind="example", title="Is it proportional?", steps=[
        dict(say="A taxi costs 6 dollars for 1 kilometre, and 10 dollars for 2 kilometres. Is the cost in direct proportion to the distance?", do=[E("🚕", 90, 140, 80), T("1 km: **$6** · 2 km: **$10**", x=200, y=160)]),
        dict(say="If it were, doubling the distance would double the cost. 2 kilometres would cost 12 dollars.", do=[MATH("2 × 6 = 12", x=80, y=290)]),
        dict(say="But it costs 10 dollars. So no. There must be a fixed fee, as well as a price per kilometre.", do=[B("No: 10 ≠ 12", x=80, y=390, color=RED), T("there is a **fixed fee**", x=80, y=500)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="5 tickets cost 40 dollars. How much do 8 tickets cost? Here is Luca's working. Which line goes wrong first?", do=LINES("Luca", "5 tickets cost $40; cost of 8 tickets", ["8 is 3 more than 5", "So the cost is $40 + $3 = $43"])),
        dict(say="Line 2 is wrong. In direct proportion, we multiply. We do not add.", do=[dict(a="cross", id="l2")]),
        dict(say="1 ticket costs 40 divided by 5, which is 8 dollars. So 8 tickets cost 8 times 8, which is 64 dollars.", do=[B("$8 each → 8 × 8 = $64", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="How far away is the storm?", steps=[
        dict(say="Here is direct proportion in a thunderstorm. Sound travels about 1 kilometre every 3 seconds.", do=[E("⛈️", 90, 160, 100), T("sound: about **1 km** every **3 seconds**", x=230, y=190)]),
        dict(say="You see the lightning, and then count the seconds until the thunder. If you count 6 seconds, the storm is about 2 kilometres away.", do=[MATH("6 seconds → 2 km", x=230, y=320)]),
        dict(say="If you count 12 seconds, it is about 4 kilometres away. Double the time means double the distance.", do=[MATH("12 seconds → 4 km", x=230, y=410), B("double the time → double the distance", x=230, y=510, color=BLUE, at=4)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("12.3-k4", "One last question. Which is better value: 500 grams for 2 dollars, or 300 grams for 1 dollar 50? Pause the video and decide.", "Better value: 500 g for $2 or 300 g for $1.50?"),
        dict(say="Find the price for 100 grams. 2 dollars divided by 5 is 40 cents. 1.50 divided by 3 is 50 cents. So 500 grams for 2 dollars is better value.",
             do=[MATH("2.00 ÷ 5 = 0.40", x=80, y=190), MATH("1.50 ÷ 3 = 0.50", x=80, y=280, at=4), B("500 g for $2", x=80, y=380, color=GREEN, at=8)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: in direct proportion, when one quantity doubles, the other doubles.", do=[T("• **Direct proportion**: double one → double the other", x=80, y=170)]),
        dict(say="The unitary method: find 1, then multiply.", do=[T("• **Unitary method**: find 1, then multiply", x=80, y=250)]),
        dict(say="To compare value, find the price for the same amount.", do=[T("• Best buy: the price for the **same amount**", x=80, y=330)]),
        dict(say="A fixed fee means the quantities are not in direct proportion.", do=[T("• A fixed fee → **not** direct proportion", x=80, y=410)]),
    ]),
]
