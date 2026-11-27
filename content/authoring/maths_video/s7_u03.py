# -*- coding: utf-8 -*-
"""Stage 7 · Unit 3 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, J, TEST, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG

PV = ["", "Th", "H", "T", "O", ".", "t", "h", "th"]   # place-value grid: thousands … thousandths
PVT = lambda rows, x=80, y=250, **k: dict(a="table", id="pv", head=PV, rows=rows, x=x, y=y, **k)
ROW = lambda i, at=0.3: dict(a="row", id="pv", i=i, at=at)

VIDEOS = {}

VIDEOS["3.1"] = [
    dict(kind="hook", title="A box of screws", steps=[
        dict(say="A factory packs 1000 screws in every box. Each screw has a mass of 2.35 grams.",
             do=[E("🔩", 90, 170, 90), T("one screw: **2.35 g**", x=210, y=195), E("📦", 90, 310, 90, at=0.3), T("one box: **1000** screws", x=210, y=335, at=0.3)]),
        PAUSE("3.1-k1", "What is the mass of all the screws in one box? Pause the video and work it out.", "What is the mass of 1000 screws of 2.35 g each, in grams?"),
    ]),
    dict(kind="hook", title="1000 times as heavy", steps=[
        dict(say="We need 2.35 times 1000. Watch what happens to the digits.", do=[MATH("2.35 × 1000", x=80, y=160)]),
        dict(say="Multiplying by 1000 moves every digit 3 places to the left. The 2 moves from the ones to the thousands.",
             do=[PVT([["2.35", "", "", "", "2", ".", "3", "5", ""], ["× 1000", "2", "3", "5", "0", ".", "", "", ""]]), ROW(0, 0.2), ROW(1, 2.6)]),
        dict(say="The answer is 2,350 grams. That is more than 2 kilograms of screws.", do=[B("2.35 × 1000 = 2350 g", x=80, y=470, color=GREEN)]),
    ]),
    dict(kind="recall", title="Place value", steps=[
        dict(say="Remember place value. In 4.07, the 4 is worth 4 ones.", do=[B("4.07", x=80, y=160), T("4 → 4 **ones**", x=80, y=280)]),
        dict(say="The 0 is worth 0 tenths, and the 7 is worth 7 hundredths.", do=[T("0 → 0 **tenths**", x=80, y=360), T("7 → 7 **hundredths**", x=80, y=440, at=1.6)]),
    ]),
    dict(kind="idea", title="Powers of 10", steps=[
        dict(say="10, 100, 1000 and 10,000 are called powers of 10.", do=[T("10, 100, 1000, 10 000 … are **powers of 10**", x=80, y=150)]),
        dict(say="We can write them with an index. 100 is 10 times 10, so it is 10 to the power 2.",
             do=[dict(a="table", id="t", head=["Number", "Product of 10s", "Power of 10"], x=80, y=240,
                      rows=[["10", "10", "10¹"], ["100", "10 × 10", "10²"], ["1000", "10 × 10 × 10", "10³"], ["10 000", "10 × 10 × 10 × 10", "10⁴"]]),
                 dict(a="row", id="t", i=0, at=0.4), dict(a="row", id="t", i=1, at=2.4)]),
        dict(say="1000 is 10 to the power 3, and 10,000 is 10 to the power 4.", do=[dict(a="row", id="t", i=2, at=0.2), dict(a="row", id="t", i=3, at=2.2)]),
        dict(say="Notice the pattern. The index is the same as the number of zeros.", do=[T("The **index** = the number of **zeros**", x=640, y=300, color=BLUE)]),
    ]),
    dict(kind="idea", title="Digits move, the point stays", steps=[
        dict(say="When you multiply by 10, every digit moves one place to the left. It becomes worth 10 times as much.",
             do=[T("× 10 → digits move **one place left**", x=80, y=150, color=GREEN), PVT([["2.35", "", "", "", "2", ".", "3", "5", ""], ["× 10", "", "", "2", "3", ".", "5", "", ""], ["× 100", "", "2", "3", "5", ".", "", "", ""], ["÷ 10", "", "", "", "0", ".", "2", "3", "5"]], y=300),
                 ROW(0, 0.2), ROW(1, 2.6)]),
        dict(say="Multiply by 100, and the digits move 2 places to the left. 2.35 becomes 235.", do=[ROW(2, 0.3)]),
        dict(say="Dividing by 10 moves every digit one place to the right. 2.35 becomes 0.235.", do=[T("÷ 10 → digits move **one place right**", x=640, y=150, color=RED), ROW(3, 1.6)]),
        dict(say="The decimal point never moves. Only the digits move.", do=[T("The decimal point **stays still**", x=80, y=220)]),
        PAUSE("3.1-k2", "Your turn. Work out 7.1 times 10 to the power 3. Pause the video and try it.", "Work out 7.1 × 10³."),
    ]),
    dict(kind="idea", title="Check: 7.1 × 10³", steps=[
        dict(say="10 to the power 3 is 1000, so the digits move 3 places to the left. We fill the gaps with zeros. The answer is 7,100.",
             do=[PVT([["7.1", "", "", "", "7", ".", "1", "", ""], ["× 10³", "7", "1", "0", "0", ".", "", "", ""]], y=180), ROW(0, 0.2), ROW(1, 3.2), B("7.1 × 10³ = 7100", x=80, y=420, color=GREEN, at=6.4)]),
    ]),
    dict(kind="method", title="Multiplying and dividing by a power of 10", steps=[
        dict(say="Here is the method. Step 1: count the zeros, or read the index. 10 to the power 3 means 3 places.", do=[T("1. Count the zeros (or read the index): 10³ → **3 places**", x=80, y=170)]),
        dict(say="Step 2: to multiply, move the digits left. To divide, move the digits right.", do=[T("2. × → digits move **left**   ÷ → digits move **right**", x=80, y=260)]),
        dict(say="Step 3: fill any gaps with zeros.", do=[T("3. Fill the gaps with **zeros**", x=80, y=350)]),
        dict(say="Step 4: check. Multiplying makes the number bigger. Dividing makes it smaller.", do=[T("4. Check: × bigger, ÷ smaller", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Dividing a whole number", steps=[
        dict(say="Work out 56 divided by 1000.", do=[B("56 ÷ 1000", x=80, y=150)]),
        dict(say="1000 has 3 zeros, so the digits move 3 places to the right.", do=[T("3 zeros → **3 places right**", x=480, y=168)]),
        dict(say="56 becomes 5.6, then 0.56, then 0.056.",
             do=[MATH("56", x=110, y=280), MATH("→ 5.6", x=230, y=280, at=1.2), MATH("→ 0.56", x=420, y=280, at=2.4), MATH("→ 0.056", x=640, y=280, at=3.6, color=GREEN)]),
        dict(say="A zero fills the empty tenths place. The answer is 0.056.", do=[B("56 ÷ 1000 = 0.056", x=80, y=400, color=GREEN)]),
        PAUSE("3.1-k3", "Your turn. Work out 85 divided by 10 to the power 4. Pause and work it out.", "Work out 85 ÷ 10⁴."),
    ]),
    dict(kind="example", title="Check: 85 ÷ 10⁴", steps=[
        dict(say="10 to the power 4 is 10,000. Move the digits 4 places to the right. 85 becomes 0.0085.",
             do=[MATH("85 → 8.5 → 0.85 → 0.085 → 0.0085", x=80, y=190), B("85 ÷ 10⁴ = 0.0085", x=80, y=310, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="The missing power", steps=[
        dict(say="Fill the gap. 9.2 times something equals 920.", do=[B("9.2 × ☐ = 920", x=80, y=160)]),
        dict(say="The 9 has moved from the ones to the hundreds. That is 2 places to the left.", do=[T("9 moves from ones to hundreds: **2 places left**", x=80, y=280)]),
        dict(say="2 places means 10 to the power 2, which is 100.", do=[B("☐ = 10² = 100", x=80, y=380, color=GREEN)]),
    ]),
    dict(kind="example", title="A pile of paper", steps=[
        dict(say="A sheet of paper is 0.09 millimetres thick. How thick is a pile of 1000 sheets, in centimetres?",
             do=[E("📄", 90, 160, 90), T("one sheet: **0.09 mm**.  1000 sheets = ? cm", x=210, y=190)]),
        dict(say="0.09 times 1000: move the digits 3 places left. That is 90 millimetres.", do=[MATH("0.09 × 1000 = 90 mm", x=80, y=310)]),
        dict(say="There are 10 millimetres in a centimetre. 90 divided by 10 is 9. The pile is 9 centimetres thick.", do=[MATH("90 ÷ 10 = 9 cm", x=80, y=410, color=GREEN), E("📚", 520, 390, 90, at=3.6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Noor works out 6.8 times 10. Which line goes wrong first?", do=LINES("Noor", "6.8 × 10", ["× 10 means add a zero", "6.8 × 10 = 6.80", "So the answer is 6.80"])),
        dict(say="Line 1 is wrong. Adding a zero only works for whole numbers. 6.80 is the same as 6.8, so nothing has changed.",
             do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6), dict(a="strike", id="l3", at=0.9)]),
        dict(say="The digits must move one place to the left. 6.8 times 10 is 68.", do=[B("6.8 × 10 = 68", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Kilo and milli", steps=[
        dict(say="Powers of 10 are built into the metric system. Kilo means 1000. So 1 kilometre is 1000 metres, and 1 kilogram is 1000 grams.",
             do=[E("📏", 90, 170, 90), T("**kilo** = × 1000:  1 km = 1000 m,  1 kg = 1000 g", x=210, y=195)]),
        dict(say="A 5 kilometre run is 5 times 1000, which is 5000 metres.", do=[E("🏃", 90, 300, 90), MATH("5 × 1000 = 5000 m", x=210, y=315, color=BLUE)]),
        dict(say="Milli means divide by 1000. A 250 millilitre glass of juice is 250 divided by 1000, which is 0.25 litres.",
             do=[E("🧃", 90, 430, 90), MATH("250 ÷ 1000 = 0.25 litres", x=210, y=445, color=RED, at=3.6)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("3.1-k4", "One last question. Which calculation is equal to 0.6? Pause the video and choose.", "Which calculation is equal to 0.6?"),
        dict(say="60 divided by 100. The digits move 2 places to the right. 60 becomes 0.60, which is 0.6.",
             do=[MATH("60 ÷ 100", x=80, y=190), MATH("60 → 6 → 0.6", x=80, y=290, at=2.4), E("✅", 420, 276, 56, at=5)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the index of a power of 10 tells you the number of zeros.", do=[T("• 10² = 100, 10³ = 1000: index = number of zeros", x=80, y=170)]),
        dict(say="To multiply, digits move left. To divide, digits move right.", do=[T("• × → digits move left;  ÷ → digits move right", x=80, y=250)]),
        dict(say="Fill gaps with zeros. The decimal point does not move.", do=[T("• Fill gaps with zeros; the point stays still", x=80, y=330)]),
        dict(say="And check: multiplying makes it bigger, dividing makes it smaller.", do=[T("• Check: × bigger, ÷ smaller", x=80, y=410)]),
    ]),
]

CUT = lambda kept, rest, x, y, **k: MATH(f'{kept}<span style="color:#E0483E"> | </span><span style="color:#667">{rest}</span>', x=x, y=y, **k)   # 27.6 | 49

VIDEOS["3.2"] = [
    dict(kind="hook", title="How fast?", steps=[
        dict(say="A sprinter crosses the line. The timing system measures 10.386 seconds.", do=[E("🏃", 90, 170, 100), T("measured: **10.386 s**", x=230, y=200)]),
        dict(say="But the big screen only shows 10.4 seconds. It has been rounded.", do=[E("📺", 90, 320, 100), T("on screen: **10.4 s**", x=230, y=350)]),
        PAUSE("3.2-k1", "What would the screen show with 2 digits after the point? Pause the video and work it out.", "What is 10.386 rounded to 2 decimal places?"),
    ]),
    dict(kind="hook", title="Two digits after the point", steps=[
        dict(say="Keep 2 digits after the point: 10.38. The next digit is 6.", do=[CUT("10.38", "6", 80, 180)]),
        dict(say="6 is 5 or more, so we round up. The 8 becomes 9. The screen would show 10.39 seconds.", do=[B("10.39 s", x=80, y=300, color=GREEN, at=3)]),
        dict(say="On a number line, 10.386 is past the halfway point, so it is closer to 10.39.",
             do=[FIG(560, 150, 620, 0, kind="numline", min=10.38, max=10.39, minor=0, ticks=[[10.385, "10.385 (halfway)"], [10.39, "10.39"]], mark=10.386)]),
    ]),
    dict(kind="recall", title="Rounding whole numbers", steps=[
        dict(say="You already know how to round whole numbers. Round 3,748 to the nearest hundred.", do=[B("3748", x=80, y=160), T("to the nearest hundred", x=300, y=178, color=GREY)]),
        dict(say="It lies between 3,700 and 3,800. The tens digit is 4, which is less than 5. So it rounds down, to 3,700.",
             do=[dict(a="nl", id="n", min=3700, max=3800, y=440, every=10), dict(a="dot", nl="n", v=3748, label="3748", color=RED, at=1.6), B("3700", x=80, y=280, color=GREEN, at=6.4)]),
    ]),
    dict(kind="idea", title="Degree of accuracy", steps=[
        dict(say="You are always told how accurate the answer must be. This is the degree of accuracy.", do=[T("**Degree of accuracy**: how many digits to keep", x=80, y=150)]),
        dict(say="It might be the nearest whole number, 1 decimal place, or 2 decimal places. We write d p for decimal places.",
             do=[T("nearest whole number   ·   **1 d.p.**   ·   **2 d.p.**", x=80, y=230)]),
        dict(say="The rule is always the same. First, find the last digit you are keeping.",
             do=[dict(a="table", id="t", head=["Step", "What to do"], x=80, y=320, rows=[["1", "Find the **last digit to keep**"], ["2", "Look at the **next digit** (the decider)"], ["3", "5 or more → round **up**.  Less than 5 → **keep**"]]),
                 dict(a="row", id="t", i=0, at=2.4)]),
        dict(say="Then look at the next digit. We call it the decider.", do=[dict(a="row", id="t", i=1, at=0.3)]),
        dict(say="If the decider is 5 or more, round up. If it is less than 5, leave the digit as it is.", do=[dict(a="row", id="t", i=2, at=0.3)]),
    ]),
    dict(kind="idea", title="Rounding to decimal places", steps=[
        dict(say="Round 10.386 to 1 decimal place. Keep the 3. The decider is 8, so round up. The answer is 10.4.",
             do=[T("1 d.p.", x=80, y=178, color=GREY), CUT("10.3", "86", 240, 170), MATH("→ 10.4", x=560, y=170, at=5.4, color=GREEN)]),
        dict(say="Now to 2 decimal places. Keep the 8. The decider is 6, so round up. The answer is 10.39.",
             do=[T("2 d.p.", x=80, y=298, color=GREY), CUT("10.38", "6", 240, 290), MATH("→ 10.39", x=560, y=290, at=5.4, color=GREEN)]),
        PAUSE("3.2-k2", "Your turn. Round 12.75 to 1 decimal place. Pause the video and try it.", "Round 12.75 to 1 decimal place."),
    ]),
    dict(kind="idea", title="Check: 12.75 to 1 d.p.", steps=[
        dict(say="Keep 1 digit after the point: 12.7. The decider is 5. 5 or more means round up. The answer is 12.8.",
             do=[CUT("12.7", "5", 80, 190), T("decider 5 → round **up**", x=420, y=198, at=3), B("12.8", x=80, y=310, color=GREEN, at=5.6)]),
    ]),
    dict(kind="method", title="How do I round to decimal places?", steps=[
        dict(say="Here is the method. Step 1: count that many digits after the decimal point, and draw a line after the last one.", do=[T("1. Count the digits to keep; **draw a line**", x=80, y=170)]),
        dict(say="Step 2: look at the digit just after the line.", do=[T("2. Look at the digit **just after** the line", x=80, y=260)]),
        dict(say="Step 3: if it is 5 or more, add 1 to the last digit you kept. If it is under 5, leave it.", do=[T("3. 5 or more → **add 1**;  under 5 → leave it", x=80, y=350)]),
        dict(say="Step 4: write exactly the number of decimal places asked for.", do=[T("4. Write **exactly** that many decimal places", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Round to 1 d.p.", steps=[
        dict(say="Round 27.649 to 1 decimal place.", do=[B("27.649", x=80, y=160), T("to 1 d.p.", x=360, y=178, color=GREY)]),
        dict(say="Keep 1 digit after the point, and draw the line.", do=[CUT("27.6", "49", 80, 270)]),
        dict(say="The decider is 4. That is less than 5, so the 6 stays. The answer is 27.6.", do=[T("decider 4 → keep", x=420, y=278), B("27.6", x=80, y=380, color=GREEN, at=3.6)]),
        dict(say="Do not look at the 9. Only the digit straight after the line matters.", do=[T("Only the digit **straight after** the line matters", x=80, y=490, color=RED)]),
    ]),
    dict(kind="example", title="A 9 that rolls over", steps=[
        dict(say="Round 3.596 to 2 decimal places.", do=[B("3.596", x=80, y=160), T("to 2 d.p.", x=360, y=178, color=GREY)]),
        dict(say="Keep 2 digits: 3.59. The decider is 6, so we add 1 to the 9.", do=[CUT("3.59", "6", 80, 270)]),
        dict(say="3.59 plus 0.01 is 3.60. The 9 becomes 0, and 1 is carried to the tenths.", do=[MATH("3.59 + 0.01 = 3.60", x=80, y=370, color=BLUE)]),
        dict(say="Write 3.60. Keep the final zero. It shows that the number is given to 2 decimal places.", do=[B("3.60", x=80, y=470, color=GREEN), T("keep the 0", x=300, y=488, color=GREY, at=2)]),
        PAUSE("3.2-k3", "Your turn. Round 0.0458 to 2 decimal places. Pause and work it out.", "Round 0.0458 to 2 decimal places."),
    ]),
    dict(kind="example", title="Check: 0.0458 to 2 d.p.", steps=[
        dict(say="Keep 2 digits after the point: 0.04. The decider is 5, so round up. The answer is 0.05.",
             do=[CUT("0.04", "58", 80, 190), T("decider 5 → round **up**", x=420, y=198, at=3), B("0.05", x=80, y=310, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Sharing a bill", steps=[
        dict(say="Three friends share a 25 dollar bill equally. How much does each pay, to the nearest cent?",
             do=[E("🧾", 90, 160, 90), T("**$25** shared by 3 friends", x=210, y=190)]),
        dict(say="25 divided by 3 is 8.3333, and the threes go on for ever.", do=[MATH("25 ÷ 3 = 8.3333…", x=80, y=310)]),
        dict(say="Cents need 2 decimal places. Keep 8.33. The decider is 3, so round down. Each friend pays 8 dollars 33.",
             do=[CUT("8.33", "33…", 80, 410), B("$8.33", x=520, y=402, color=GREEN, at=5)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Eli rounds 8.2471 to 1 decimal place. Which line goes wrong first?",
             do=LINES("Eli", "8.2471 to 1 d.p.", ["The last digit is 1, so round down", "8.2471 → 8.247 → 8.25 → 8.3", "Answer: 8.3"])),
        dict(say="Line 1 is wrong. Eli started from the last digit and rounded again and again. Only the digit straight after the kept place matters.",
             do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6), dict(a="strike", id="l3", at=0.9)]),
        dict(say="Keep 8.2. The decider is 4, so the 2 stays. The answer is 8.2. Always round in one step.",
             do=[CUT("8.2", "471", 110, 480), B("8.2", x=520, y=472, color=GREEN, at=3.4)]),
    ]),
    dict(kind="life", title="The world record", steps=[
        dict(say="Sprint times are recorded to 2 decimal places. The men's 100 metres world record is 9.58 seconds, set by Usain Bolt in 2009.",
             do=[E("🥇", 90, 170, 100), T("100 m world record: **9.58 s** (Usain Bolt, 2009)", x=230, y=200)]),
        dict(say="To the nearest whole number, that is 10 seconds. To 1 decimal place, it is 9.6 seconds.",
             do=[T("nearest whole number: **10 s**", x=230, y=310), T("1 d.p.: **9.6 s**", x=230, y=390, at=3.6)]),
        dict(say="The more decimal places you keep, the more accurate the number is. That is why races use hundredths of a second.",
             do=[T("More decimal places = **more accurate**", x=230, y=490, color=BLUE), E("⏱️", 1000, 440, 100, at=1.5)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("3.2-k4", "One last question. Round 6.997 to 2 decimal places, and write all the digits. Pause the video and answer.", "Round 6.997 to 2 decimal places (write all the digits)."),
        dict(say="Keep 6.99. The decider is 7, so add 1 hundredth. 6.99 plus 0.01 is 7.00. Write 7.00, with both zeros.",
             do=[CUT("6.99", "7", 80, 190), MATH("6.99 + 0.01 = 7.00", x=80, y=290, at=3, color=BLUE), B("7.00", x=80, y=400, color=GREEN, at=7)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: find the last digit to keep, then look at the next digit, the decider.", do=[T("• Last digit to keep, then the **decider**", x=80, y=170)]),
        dict(say="5 or more, round up. Under 5, keep.", do=[T("• 5 or more → up;  under 5 → keep", x=80, y=250)]),
        dict(say="Round in one step, from the original number.", do=[T("• Round in **one step**", x=80, y=330)]),
        dict(say="Give exactly the number of decimal places asked for, and keep any final zero.", do=[T("• Exactly that many decimal places; keep a final 0", x=80, y=410)]),
    ]),
]
