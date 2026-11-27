# -*- coding: utf-8 -*-
"""Stage 8 · Unit 4 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG
from .s7_u04 import TBL, ROW

NL = lambda mn, mx, ticks, marks=(), x=560, y=150, w=660, at=0: FIG(x, y, w, at, kind="numline", min=mn, max=mx, minor=0, ticks=[[v, l] for v, l in ticks], marks=list(marks))

VIDEOS = {}

VIDEOS["4.1"] = [
    dict(kind="hook", title="Winter temperatures", steps=[
        dict(say="Here are the overnight temperatures in four cities: negative 2.45, negative 2.5, negative 2.405 and negative 2.054 degrees Celsius.",
             do=[E("🥶", 90, 170, 100), T("**−2.45 °C · −2.5 °C · −2.405 °C · −2.054 °C**", x=230, y=200)]),
        dict(say="Which city was the coldest?", do=[T("which was **coldest**?", x=230, y=300)]),
        PAUSE("4.1-k1", "Type the coldest temperature. Pause the video and work it out.", "Type the coldest temperature."),
    ]),
    dict(kind="hook", title="The coldest", steps=[
        dict(say="The coldest is the smallest number. That is the one furthest below zero. Negative 2.5 is the furthest from zero, so it is the coldest.",
             do=[NL(-2.6, -2.0, [(-2.5, "−2.5"), (-2.45, "−2.45"), (-2.405, ""), (-2.054, "−2.054"), (-2.0, "−2")], marks=[-2.5, -2.45, -2.405, -2.054], x=80, y=200, w=900), B("coldest: −2.5 °C", x=80, y=170, color=GREEN, at=4)]),
        dict(say="The warmest is negative 2.054, because it is closest to zero.", do=[T("warmest: **−2.054 °C** (closest to zero)", x=80, y=260)]),
    ]),
    dict(kind="recall", title="Comparing positive decimals", steps=[
        dict(say="Remember: to compare decimals, look at the whole numbers first, then the tenths, then the hundredths.", do=[T("whole numbers → tenths → hundredths …", x=80, y=170)]),
        dict(say="8.518 and 8.56: the whole numbers and the tenths are the same. In the hundredths, 1 is less than 6. So 8.518 is less than 8.56.", do=[MATH("8.518 < 8.56", x=80, y=270, color=GREEN)]),
    ]),
    dict(kind="idea", title="Negative decimals", steps=[
        dict(say="On a number line, numbers further to the left are smaller. For negative numbers, the one with the bigger size is further from zero, so it is smaller.",
             do=[B("negatives: bigger size → **smaller** number", x=80, y=160, color=BLUE)]),
        dict(say="3.4 is bigger than 3.04. So negative 3.4 is further left, and negative 3.4 is less than negative 3.04.",
             do=[NL(-3.6, -2.9, [(-3.4, "−3.4"), (-3.04, "−3.04")], marks=[-3.4, -3.04], x=80, y=250, w=900), MATH("−3.4 < −3.04", x=80, y=260, color=GREEN, at=4)]),
        PAUSE("4.1-k2", "Your turn. Which is smaller: negative 3.9, or negative 3.85? Pause the video and choose.", "Which is smaller: −3.9 or −3.85?"),
    ]),
    dict(kind="idea", title="Check: −3.9 or −3.85", steps=[
        dict(say="3.9 is the same as 3.90, which is bigger than 3.85. So negative 3.9 is further from zero. Negative 3.9 is smaller.",
             do=[MATH("3.90 > 3.85", x=80, y=190), MATH("−3.9 < −3.85", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="idea", title="Equal or not equal", steps=[
        dict(say="Zeros at the end of a decimal do not change its value. 0.50 equals 0.5.", do=[MATH("0.50 = 0.5", x=80, y=170)]),
        dict(say="But a sign does. Negative 0.5 is not equal to 0.5. This sign means not equal to.", do=[MATH("−0.5 ≠ 0.5", x=80, y=260), T("≠ means **not equal to**", x=420, y=268)]),
        dict(say="In a mixed list, all the negatives come before zero, and all the positives come after.", do=[T("negatives < 0 < positives", x=80, y=360)]),
    ]),
    dict(kind="method", title="How do I order decimals with negatives?", steps=[
        dict(say="Here is the method. Step 1: split the numbers into negatives, zero and positives.", do=[T("1. Split: **negatives**, zero, **positives**", x=80, y=170)]),
        dict(say="Step 2: for positives, compare place by place. Fill with zeros so they have the same length.", do=[T("2. Positives: place by place (fill with zeros)", x=80, y=260)]),
        dict(say="Step 3: for negatives, compare the sizes. The biggest size is the smallest number.", do=[T("3. Negatives: biggest size = **smallest**", x=80, y=350)]),
        dict(say="Step 4: if you are not sure, sketch a number line.", do=[T("4. Not sure? Sketch a **number line**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A mixed list", steps=[
        dict(say="Put these in order, smallest first: 0.3, negative 0.32, negative 0.302, and 0.03.", do=[MATH("0.3, −0.32, −0.302, 0.03", x=80, y=170)]),
        dict(say="The negatives first. 0.320 is bigger than 0.302, so negative 0.32 is smaller than negative 0.302.", do=[MATH("−0.320 < −0.302", x=80, y=260)]),
        dict(say="Then the positives: 0.03 is less than 0.3. The order is negative 0.32, negative 0.302, 0.03, 0.3.", do=[MATH("0.03 < 0.3", x=80, y=340), B("−0.32, −0.302, 0.03, 0.3", x=80, y=430, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="Using symbols", steps=[
        dict(say="Is negative 2.30 equal to negative 2.3? The zero at the end makes no difference.", do=[MATH("−2.30 ☐ −2.3", x=80, y=170)]),
        PAUSE("4.1-k3", "Your turn. Equal, or not equal? Pause and choose.", "= or ≠? −2.30 ☐ −2.3"),
    ]),
    dict(kind="example", title="Check: −2.30 and −2.3", steps=[
        dict(say="They are the same number, so they are equal. Negative 2.30 equals negative 2.3.", do=[B("−2.30 = −2.3", x=80, y=200, color=GREEN)]),
        dict(say="Now compare negative 4.12 and negative 4.2. 4.12 is less than 4.20, so negative 4.12 is closer to zero. Negative 4.12 is greater than negative 4.2.",
             do=[MATH("4.12 < 4.20", x=80, y=300), MATH("−4.12 > −4.2", x=80, y=390, color=GREEN, at=6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Finn wants to know which is smaller: negative 0.8 or negative 0.75. Which line is wrong?", do=LINES("Finn", "−0.8 or −0.75?", ["0.8 > 0.75", "so −0.8 > −0.75"])),
        dict(say="Line 2 is wrong. For negatives, the bigger size is further from zero. So the inequality turns round.", do=[dict(a="cross", id="l2")]),
        dict(say="Negative 0.8 is less than negative 0.75.", do=[B("−0.8 < −0.75", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Golf scores", steps=[
        dict(say="In golf, scores are often given compared with par, and the lowest score wins. Three players have average scores of negative 3.5, negative 2.75 and negative 3.25.",
             do=[E("⛳", 90, 170, 100), T("averages: **−3.5**, **−2.75**, **−3.25**", x=230, y=200)]),
        dict(say="The smallest number is negative 3.5, so that player is winning.", do=[MATH("−3.5 < −3.25 < −2.75", x=230, y=310, color=BLUE), B("winner: −3.5", x=230, y=400, color=GREEN, at=3)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.1-k4", "One last question. Write a number halfway between negative 0.4 and negative 0.5. Pause the video and answer.", "Write a number halfway between −0.4 and −0.5."),
        dict(say="Halfway between 0.4 and 0.5 is 0.45. So halfway between negative 0.4 and negative 0.5 is negative 0.45.",
             do=[NL(-0.5, -0.4, [(-0.5, "−0.5"), (-0.45, "−0.45"), (-0.4, "−0.4")], marks=[-0.45], x=80, y=200, w=900), B("−0.45", x=80, y=170, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: compare decimals place by place.", do=[T("• Compare **place by place**", x=80, y=170)]),
        dict(say="For negatives, the bigger size is the smaller number.", do=[T("• Negatives: bigger size = smaller number", x=80, y=250)]),
        dict(say="Use the signs for equal, not equal, less than and greater than carefully.", do=[T("• Use =, ≠, <, > carefully", x=80, y=330)]),
        dict(say="Sketch a number line if you are not sure.", do=[T("• Sketch a number line if unsure", x=80, y=410)]),
    ]),
]

VIDEOS["4.2"] = [
    dict(kind="hook", title="A new rug", steps=[
        dict(say="A rug costs 18 dollars 75 per square metre. A room is 3.6 metres by 2.5 metres.", do=[E("🧶", 90, 170, 100), T("**$18.75** per m² · room **3.6 m × 2.5 m**", x=230, y=200)]),
        dict(say="Before working it out exactly, estimate. The price is about 20 dollars, and the area is about 9 square metres.", do=[T("price ≈ **$20** · area ≈ **9 m²**", x=230, y=300)]),
        PAUSE("4.2-k1", "Estimate the cost: 20 times 9. Pause the video and work it out.", "Estimate the carpet cost (20 × 9)."),
    ]),
    dict(kind="hook", title="About $180", steps=[
        dict(say="20 times 9 is 180. The rug will cost about 180 dollars.", do=[MATH("20 × 9 = 180", x=80, y=190), B("about $180", x=80, y=290, color=GREEN, at=2.4)]),
        dict(say="To be exact, we need 3.6 times 2.5. How do we multiply two decimals?", do=[MATH("3.6 × 2.5 = ?", x=80, y=400)]),
    ]),
    dict(kind="recall", title="A decimal times a whole number", steps=[
        dict(say="Remember: for 2.4 times 3, work out 24 times 3, which is 72. There is one decimal place in the question, so the answer is 7.2.",
             do=[MATH("24 × 3 = 72", x=80, y=180), MATH("2.4 × 3 = 7.2", x=80, y=280, color=GREEN, at=5)]),
    ]),
    dict(kind="idea", title="A decimal times a decimal", steps=[
        dict(say="Multiply without the decimal points. Then count the total number of decimal places in the question. The answer has that many.",
             do=[TBL(["Calculation", "Without points", "Decimal places", "Answer"], [["3.6 × 2.5", "36 × 25 = 900", "1 + 1 = 2", "9.00 = 9"], ["0.4 × 0.03", "4 × 3 = 12", "1 + 2 = 3", "0.012"]], y=170), ROW(0, 0.4)]),
        dict(say="36 times 25 is 900. There are 2 decimal places, so the answer is 9.00, which is 9. The room is exactly 9 square metres.", do=[]),
        dict(say="Why does it work? 3.6 is 36 divided by 10, and 2.5 is 25 divided by 10. So the answer is 36 times 25, divided by 100. Two divisions by 10 give two decimal places.",
             do=[MATH("3.6 × 2.5 = 36 × 25 ÷ 100", x=80, y=400)]),
        dict(say="For 0.4 times 0.03: 4 times 3 is 12. There are 3 decimal places, so the answer is 0.012.", do=[ROW(1, 0.3)]),
        PAUSE("4.2-k2", "Your turn. Work out 0.9 times 0.7. Pause the video and try it.", "Work out 0.9 × 0.7."),
    ]),
    dict(kind="idea", title="Check: 0.9 × 0.7", steps=[
        dict(say="9 times 7 is 63. There are 2 decimal places, so the answer is 0.63. It is smaller than both numbers, because both are less than 1.",
             do=[MATH("9 × 7 = 63", x=80, y=190), MATH("0.9 × 0.7 = 0.63", x=80, y=280, color=GREEN, at=3)]),
    ]),
    dict(kind="method", title="How do I multiply decimals?", steps=[
        dict(say="Here is the method. Step 1: estimate, by rounding to 1 significant figure.", do=[T("1. **Estimate** (round to 1 s.f.)", x=80, y=170)]),
        dict(say="Step 2: multiply the numbers as whole numbers.", do=[T("2. Multiply as **whole numbers**", x=80, y=260)]),
        dict(say="Step 3: count the total decimal places in both numbers, and place the point.", do=[T("3. Count the **total** decimal places", x=80, y=350)]),
        dict(say="Step 4: compare the answer with your estimate.", do=[T("4. Compare with the **estimate**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A written method", steps=[
        dict(say="Work out 4.73 times 2.6. Estimate first: 5 times 3 is 15.", do=[MATH("4.73 × 2.6", x=80, y=170), T("estimate: 5 × 3 = **15**", x=420, y=178)]),
        dict(say="Now 473 times 26. 473 times 20 is 9,460. 473 times 6 is 2,838. Together they make 12,298.",
             do=[MATH("473 × 20 = 9460", x=80, y=260), MATH("473 × 6 = 2838", x=80, y=340, at=3), MATH("9460 + 2838 = 12 298", x=80, y=420, at=5.5)]),
        dict(say="There are 2 plus 1, which is 3 decimal places. The answer is 12.298. That is close to the estimate of 15.", do=[B("4.73 × 2.6 = 12.298", x=640, y=340, color=GREEN)]),
    ]),
    dict(kind="example", title="Small numbers", steps=[
        dict(say="Work out 0.05 times 0.008. 5 times 8 is 40. There are 2 plus 3, which is 5 decimal places.", do=[MATH("0.05 × 0.008", x=80, y=170), MATH("5 × 8 = 40", x=80, y=260)]),
        dict(say="Count back 5 places from 40. The answer is 0.00040, which is 0.0004.", do=[B("0.000 40 = 0.0004", x=80, y=360, color=GREEN)]),
        PAUSE("4.2-k3", "Your turn. Work out 2.5 times 1.2. Pause and work it out.", "Work out 2.5 × 1.2."),
    ]),
    dict(kind="example", title="Check: 2.5 × 1.2", steps=[
        dict(say="25 times 12 is 300. There are 2 decimal places, so the answer is 3.00, which is 3.", do=[MATH("25 × 12 = 300", x=80, y=190), B("2.5 × 1.2 = 3", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Using a known fact", steps=[
        dict(say="You are told that 37 times 54 is 1,998. Use this to find 3.7 times 0.054.", do=[MATH("37 × 54 = 1998", x=80, y=170), MATH("3.7 × 0.054 = ?", x=80, y=260)]),
        dict(say="There are 1 plus 3, which is 4 decimal places. So the answer is 0.1998.", do=[B("0.1998", x=80, y=360, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Jo works out 0.3 times 0.2. Which line goes wrong first?", do=LINES("Jo", "0.3 × 0.2", ["Line up the decimal points like addition", "0.3 × 0.2 = 0.6"])),
        dict(say="Line 1 is wrong. You do not line up the points when you multiply. 3 times 2 is 6, and there are 2 decimal places.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="0.3 times 0.2 is 0.06.", do=[B("0.3 × 0.2 = 0.06", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Filling up", steps=[
        dict(say="Petrol costs 1 dollar 42 per litre. A car's tank takes 38.5 litres. Estimate: 1.4 times 40 is 56 dollars.", do=[E("⛽", 90, 170, 100), T("**$1.42** per litre × **38.5** litres", x=230, y=200), T("estimate: 1.4 × 40 = **56**", x=230, y=290)]),
        dict(say="142 times 385 is 54,670. There are 3 decimal places, so the cost is 54.670. That is 54 dollars 67.", do=[MATH("142 × 385 = 54 670", x=230, y=380), B("$54.67", x=230, y=470, color=GREEN, at=5)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.2-k4", "One last question. What is 0.2 times 0.02? Pause the video and answer.", "0.2 × 0.02 = ?"),
        dict(say="2 times 2 is 4. There are 1 plus 2, which is 3 decimal places. The answer is 0.004.", do=[MATH("2 × 2 = 4", x=80, y=190), B("0.2 × 0.02 = 0.004", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: multiply as whole numbers, then count the total decimal places.", do=[T("• Whole numbers first, then count the **total** decimal places", x=80, y=170)]),
        dict(say="Estimate to check your answer.", do=[T("• Estimate to check", x=80, y=250)]),
        dict(say="Multiplying by a number between 0 and 1 makes the answer smaller.", do=[T("• × a number between 0 and 1 → smaller", x=80, y=330)]),
        dict(say="Use known facts, and move the decimal point.", do=[T("• Use known facts and move the point", x=80, y=410)]),
    ]),
]

VIDEOS["4.3"] = [
    dict(kind="hook", title="Ribbon bows", steps=[
        dict(say="A craft shop has 5.67 metres of ribbon. Each bow needs 0.7 metres. How many bows can be made?", do=[E("🎀", 90, 170, 100), T("**5.67 m** of ribbon · **0.7 m** per bow", x=230, y=200)]),
        dict(say="Dividing by a decimal looks hard. Can you make it easier?", do=[MATH("5.67 ÷ 0.7", x=230, y=300, color=BLUE)]),
        PAUSE("4.3-k1", "What is 5.67 divided by 0.7? Pause the video and work it out.", "5.67 ÷ 0.7 = ?"),
    ]),
    dict(kind="hook", title="Make it whole", steps=[
        dict(say="Multiply both numbers by 10. 5.67 divided by 0.7 is the same as 56.7 divided by 7.", do=[MATH("5.67 ÷ 0.7 = 56.7 ÷ 7", x=80, y=190)]),
        dict(say="56 divided by 7 is 8, and 0.7 divided by 7 is 0.1. So the answer is 8.1. The shop can make 8 whole bows.", do=[B("= 8.1", x=80, y=290, color=GREEN), T("→ **8** whole bows", x=320, y=300, at=5)]),
    ]),
    dict(kind="recall", title="Short division", steps=[
        dict(say="Remember: for 36.8 divided by 4, divide each part. 36 divided by 4 is 9, and 0.8 divided by 4 is 0.2. So the answer is 9.2. Keep the point in line.",
             do=[MATH("36.8 ÷ 4 = 9.2", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Make the divisor whole", steps=[
        dict(say="Multiply both numbers by the same power of 10, so that the number you divide by becomes a whole number. The answer does not change.",
             do=[TBL(["Calculation", "× both by", "Easier", "Answer"], [["5.67 ÷ 0.7", "10", "56.7 ÷ 7", "8.1"], ["1.56 ÷ 0.12", "100", "156 ÷ 12", "13"]], y=170), ROW(0, 0.4)]),
        dict(say="If the divisor has 2 decimal places, multiply both by 100. 1.56 divided by 0.12 becomes 156 divided by 12, which is 13.", do=[ROW(1, 0.3)]),
        dict(say="Dividing by a number between 0 and 1 gives a bigger answer. 3 divided by 0.5 is 6, because there are 6 halves in 3.", do=[MATH("3 ÷ 0.5 = 6", x=80, y=420), T("÷ a number less than 1 → **bigger**", x=420, y=428, color=RED)]),
        PAUSE("4.3-k2", "Your turn. Work out 2.5 divided by 0.5. Pause the video and try it.", "Work out 2.5 ÷ 0.5."),
    ]),
    dict(kind="idea", title="Check: 2.5 ÷ 0.5", steps=[
        dict(say="Multiply both by 10. 25 divided by 5 is 5. There are 5 halves in 2 and a half.", do=[MATH("2.5 ÷ 0.5 = 25 ÷ 5 = 5", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I divide by a decimal?", steps=[
        dict(say="Here is the method. Step 1: multiply the divisor by 10 or 100, to make it a whole number.", do=[T("1. Make the divisor **whole** (× 10 or × 100)", x=80, y=170)]),
        dict(say="Step 2: multiply the other number by the same amount.", do=[T("2. Multiply the other number by the **same**", x=80, y=260)]),
        dict(say="Step 3: divide, using short division. Keep the point in line.", do=[T("3. **Short division**; keep the point in line", x=80, y=350)]),
        dict(say="Step 4: check by multiplying back.", do=[T("4. **Check** by multiplying back", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A decimal answer", steps=[
        dict(say="Work out 7.35 divided by 0.5. Multiply both by 10: 73.5 divided by 5.", do=[MATH("7.35 ÷ 0.5 = 73.5 ÷ 5", x=80, y=170)]),
        dict(say="73.5 divided by 5 is 14.7. Check: 14.7 times 0.5 is 7.35.", do=[B("= 14.7", x=80, y=270, color=GREEN)]),
        PAUSE("4.3-k3", "Your turn. Work out 0.36 divided by 0.04. Pause and work it out.", "Work out 0.36 ÷ 0.04."),
    ]),
    dict(kind="example", title="Check: 0.36 ÷ 0.04", steps=[
        dict(say="The divisor has 2 decimal places, so multiply both by 100. 36 divided by 4 is 9.", do=[MATH("0.36 ÷ 0.04 = 36 ÷ 4 = 9", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Filling cups", steps=[
        dict(say="How many 0.25 litre cups can be filled from a 3.8 litre jug? Multiply both by 100: 380 divided by 25, which is 15.2.",
             do=[E("🥤", 90, 160, 90), MATH("3.8 ÷ 0.25 = 380 ÷ 25 = 15.2", x=230, y=180)]),
        dict(say="We can only count full cups, so the answer is 15 cups.", do=[B("15 full cups", x=230, y=290, color=GREEN)]),
    ]),
    dict(kind="example", title="Price per kilogram", steps=[
        dict(say="0.6 kilograms of cherries cost 4 dollars 32. What is the price per kilogram? Multiply both by 10: 43.2 divided by 6, which is 7.2.",
             do=[E("🍒", 90, 160, 90), MATH("4.32 ÷ 0.6 = 43.2 ÷ 6 = 7.2", x=230, y=180)]),
        dict(say="The price is 7 dollars 20 per kilogram.", do=[B("$7.20 per kg", x=230, y=290, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Tia works out 6.3 divided by 0.9. Which line goes wrong first?", do=LINES("Tia", "6.3 ÷ 0.9", ["Make 0.9 into 9", "6.3 ÷ 9 = 0.7"])),
        dict(say="Line 1 is wrong. She only multiplied 0.9 by 10. Both numbers must be multiplied by 10. Also, dividing by 0.9 should give an answer bigger than 6.3.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="63 divided by 9 is 7.", do=[B("6.3 ÷ 0.9 = 63 ÷ 9 = 7", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Fuel economy", steps=[
        dict(say="A car uses 0.06 litres of fuel for every kilometre. How far can it go on 45 litres? 45 divided by 0.06 is 4,500 divided by 6, which is 750 kilometres.",
             do=[E("🚙", 90, 170, 100), MATH("45 ÷ 0.06 = 4500 ÷ 6 = 750", x=230, y=190), B("750 km", x=230, y=290, color=GREEN, at=7)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.3-k4", "One last question. Is 9 divided by 0.3 equal to 30, 3, or 2.7? Pause the video and choose.", "9 ÷ 0.3 is …"),
        dict(say="Multiply both by 10: 90 divided by 3 is 30. It is bigger than 9, because we divided by a number less than 1.", do=[MATH("9 ÷ 0.3 = 90 ÷ 3", x=80, y=190), B("= 30", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: multiply both numbers by 10 or 100, to make the divisor a whole number.", do=[T("• Multiply **both** by 10 or 100", x=80, y=170)]),
        dict(say="Then use short division.", do=[T("• Then use short division", x=80, y=250)]),
        dict(say="Dividing by a number between 0 and 1 makes the answer bigger.", do=[T("• ÷ a number between 0 and 1 → bigger", x=80, y=330)]),
        dict(say="Check by multiplying back.", do=[T("• Check by multiplying back", x=80, y=410)]),
    ]),
]

VIDEOS["4.4"] = [
    dict(kind="hook", title="A quick bill", steps=[
        dict(say="A school buys 25 calculators at 7 dollars 96 each. The office has no calculator to hand!", do=[E("🧮", 90, 170, 100), T("**25** calculators at **$7.96**", x=230, y=200)]),
        dict(say="How could you work out the total quickly, in your head?", do=[MATH("25 × 7.96", x=230, y=300, color=BLUE)]),
        PAUSE("4.4-k1", "What is 25 times 7 dollars 96? Pause the video and work it out.", "25 × $7.96 = ?"),
    ]),
    dict(kind="hook", title="Round and adjust", steps=[
        dict(say="7.96 is 4 cents less than 8. 25 times 8 is 200.", do=[MATH("25 × 8 = 200", x=80, y=190)]),
        dict(say="But each calculator is 0.04 less, and there are 25 of them. 25 times 0.04 is 1. So the total is 200 minus 1, which is 199 dollars.",
             do=[MATH("25 × 0.04 = 1", x=80, y=280), B("200 − 1 = $199", x=80, y=380, color=GREEN, at=5)]),
    ]),
    dict(kind="recall", title="Compensation and pairs", steps=[
        dict(say="Remember: 9 times 4.2 is 10 times 4.2, minus one 4.2. That is 42 minus 4.2, which is 37.8.", do=[MATH("9 × 4.2 = 42 − 4.2 = 37.8", x=80, y=180)]),
        dict(say="And look for pairs that make 1. 0.25 times 4 is 1.", do=[MATH("0.25 × 4 = 1", x=80, y=280)]),
    ]),
    dict(kind="idea", title="Strategies", steps=[
        dict(say="Here are some ways to make decimal calculations easier. Round and adjust, like the calculators.",
             do=[TBL(["Strategy", "Example"], [["round and adjust", "25 × 7.96 = 200 − 1 = 199"], ["use factors", "3.6 × 15 = 3.6 × 3 × 5 = 10.8 × 5 = 54"], ["decimals as fractions", "0.25 × 7.2 = 7.2 ÷ 4 = 1.8"], ["pairs that make 1 or 10", "0.2 × 4.6 × 5 = 4.6 × 1"]], y=160), ROW(0, 0.3)]),
        dict(say="Use factors. 15 is 3 times 5, so 3.6 times 15 is 3.6 times 3, which is 10.8, then times 5, which is 54.", do=[ROW(1, 0.3)]),
        dict(say="Use fractions. 0.25 is a quarter, so 0.25 times 7.2 is 7.2 divided by 4, which is 1.8.", do=[ROW(2, 0.3)]),
        dict(say="And look for pairs. 0.2 times 5 is 1.", do=[ROW(3, 0.3)]),
        PAUSE("4.4-k2", "Your turn. Work out 0.2 times 4.6 times 5. Pause the video and try it.", "Work out 0.2 × 4.6 × 5."),
    ]),
    dict(kind="idea", title="Check: 0.2 × 4.6 × 5", steps=[
        dict(say="Pair 0.2 with 5. 0.2 times 5 is 1. And 1 times 4.6 is 4.6.", do=[MATH("0.2 × 5 = 1", x=80, y=190), B("1 × 4.6 = 4.6", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="method", title="How do I choose an easier method?", steps=[
        dict(say="Here is the method. Step 1: look for numbers close to a whole number or a round number.", do=[T("1. Close to a **round number**? Round and adjust", x=80, y=170)]),
        dict(say="Step 2: look for pairs that multiply to make 1, 10 or 100.", do=[T("2. Pairs that make **1, 10, 100**", x=80, y=260)]),
        dict(say="Step 3: split a number into factors, or use fractions. 0.25 is a quarter, 0.5 is a half, 0.2 is a fifth.", do=[T("3. **Factors**, or 0.25 = ¼, 0.5 = ½, 0.2 = ⅕", x=80, y=350)]),
        dict(say="Step 4: follow the order of operations, and check with an estimate.", do=[T("4. Order of operations; **estimate** to check", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Taking out a common factor", steps=[
        dict(say="Work out 3.6 times 8.5, plus 3.6 times 1.5. Both parts have 3.6, so take it out: 3.6 times, bracket, 8.5 plus 1.5.",
             do=[MATH("3.6 × 8.5 + 3.6 × 1.5", x=80, y=170), MATH("= 3.6 × (8.5 + 1.5)", x=80, y=260, at=5)]),
        dict(say="8.5 plus 1.5 is 10. 3.6 times 10 is 36.", do=[B("= 3.6 × 10 = 36", x=80, y=360, color=GREEN)]),
    ]),
    dict(kind="example", title="Dividing by a half", steps=[
        dict(say="Work out 5.2 divided by 0.5. 0.5 is a half, and there are 2 halves in every whole. So dividing by 0.5 is the same as multiplying by 2.",
             do=[MATH("5.2 ÷ 0.5", x=80, y=170), T("÷ 0.5 = **× 2**", x=420, y=178, at=4)]),
        PAUSE("4.4-k3", "Your turn. Finish it: what is 5.2 divided by 0.5? Pause and work it out.", "Work out 5.2 ÷ 0.5."),
    ]),
    dict(kind="example", title="Check: 5.2 ÷ 0.5", steps=[
        dict(say="5.2 times 2 is 10.4.", do=[B("5.2 × 2 = 10.4", x=80, y=200, color=GREEN)]),
        dict(say="In the same way, dividing by 0.25 is multiplying by 4. So 6.3 divided by 0.25 is 6.3 times 4, which is 25.2.", do=[MATH("6.3 ÷ 0.25 = 6.3 × 4 = 25.2", x=80, y=310)]),
    ]),
    dict(kind="example", title="Pairs", steps=[
        dict(say="Work out 0.125 times 7.3 times 8. 0.125 is an eighth, so 0.125 times 8 is 1. And 1 times 7.3 is 7.3.",
             do=[MATH("0.125 × 7.3 × 8", x=80, y=170), MATH("0.125 × 8 = 1", x=80, y=260, at=4), B("= 7.3", x=80, y=360, color=GREEN, at=7)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Dan works out 15 times 5.98. Which line goes wrong first?", do=LINES("Dan", "15 × 5.98", ["15 × 6 = 90", "5.98 is 0.02 less than 6, so subtract 0.02", "90 − 0.02 = 89.98"])),
        dict(say="Line 2 is wrong. There are 15 lots of 0.02 to subtract, not just one. 15 times 0.02 is 0.3.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="90 minus 0.3 is 89.7.", do=[B("90 − 0.3 = 89.7", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Prices ending in 99", steps=[
        dict(say="Shops often set prices like 4 dollars 99, because they look smaller than 5 dollars. Round and adjust beats that trick.",
             do=[E("🏷️", 90, 170, 100), T("**$4.99** looks smaller than $5", x=230, y=200)]),
        dict(say="6 items at 4 dollars 99 cost 6 times 5, which is 30, minus 6 cents. That is 29 dollars 94.", do=[MATH("6 × 4.99 = 30 − 0.06 = 29.94", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.4-k4", "One last question. Work out 7.3 times 99. Pause the video and answer.", "7.3 × 99 = ?"),
        dict(say="99 is 1 less than 100. 7.3 times 100 is 730. Subtract one 7.3: 730 minus 7.3 is 722.7.", do=[MATH("7.3 × 100 = 730", x=80, y=190), B("730 − 7.3 = 722.7", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: round and adjust. Adjust by the difference times the multiplier.", do=[T("• Round and adjust (difference × multiplier)", x=80, y=170)]),
        dict(say="Use factors, and pairs that make 1, 10 or 100.", do=[T("• Factors and pairs that make 1, 10, 100", x=80, y=250)]),
        dict(say="Remember: 0.25 is a quarter, 0.5 is a half, 0.2 is a fifth, and 0.125 is an eighth.", do=[T("• 0.25 = ¼ · 0.5 = ½ · 0.2 = ⅕ · 0.125 = ⅛", x=80, y=330)]),
        dict(say="Use the distributive law, and the order of operations.", do=[T("• Distributive law and the order of operations", x=80, y=410)]),
    ]),
]
