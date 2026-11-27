# -*- coding: utf-8 -*-
"""Stage 7 · Unit 10 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u07 import F

VIDEOS = {}

VIDEOS["10.1"] = [
    dict(kind="hook", title="Battery levels", steps=[
        dict(say="3 friends compare their phones. Mia's phone shows 0.35 of its battery left. Leo's shows 3 eighths. And Sam's shows 36 per cent.",
             do=[E("🔋", 90, 160, 100), T("Mia: **0.35**", x=240, y=180), MATH(f"Leo: {F(3, 8)}", x=520, y=160, at=4), T("Sam: **36%**", x=800, y=180, at=7)]),
        PAUSE("10.1-k1", "Whose phone has the most charge left? Pause the video and work it out.", "Who has the most charge: 0.35, 3/8 or 36%?"),
    ]),
    dict(kind="hook", title="Make them all percentages", steps=[
        dict(say="To compare them, write all 3 in the same form. 0.35 is 35 per cent.", do=[MATH("0.35 = 35%", x=80, y=170)]),
        dict(say="3 divided by 8 is 0.375, which is 37.5 per cent.", do=[MATH(f"{F(3, 8)} = 0.375 = 37.5%", x=80, y=260)]),
        dict(say="So Leo has 37.5 per cent, Sam has 36 per cent, and Mia has 35 per cent. Leo has the most charge.", do=[MATH("37.5% > 36% > 35%", x=80, y=400), B("Leo", x=80, y=490, color=GREEN, at=6)]),
    ]),
    dict(kind="recall", title="Per cent", steps=[
        dict(say="Remember: per cent means out of 100. 45 per cent is 45 out of 100.", do=[B("per cent = out of 100", x=80, y=170), MATH(f"45% = {F(45, 100)}", x=80, y=290, at=3)]),
    ]),
    dict(kind="idea", title="Three ways to write one amount", steps=[
        dict(say="A fraction, a decimal and a percentage can all show the same amount. One half is 0.5, and it is 50 per cent.",
             do=[TBL(["Fraction", "Decimal", "Percentage"], [[F(1, 2), "0.5", "50%"], [F(1, 4), "0.25", "25%"], [F(3, 4), "0.75", "75%"], [F(1, 5), "0.2", "20%"], [F(1, 10), "0.1", "10%"]], y=150), ROW(0, 4)]),
        dict(say="One quarter is 0.25, or 25 per cent. 3 quarters is 0.75, or 75 per cent.", do=[ROW(1, 0.3), ROW(2, 3.6)]),
        dict(say="One fifth is 0.2, or 20 per cent. And one tenth is 0.1, or 10 per cent. These are worth learning by heart.", do=[ROW(3, 0.3), ROW(4, 3.4), T("learn these **by heart**", x=700, y=300, color=BLUE, at=6)]),
    ]),
    dict(kind="idea", title="Converting", steps=[
        dict(say="To change a percentage to a decimal, divide by 100. 36 per cent is 0.36.", do=[T("**% → decimal**: ÷ 100", x=80, y=160), MATH("36% = 0.36", x=640, y=150)]),
        dict(say="To change a decimal to a percentage, multiply by 100. 0.07 is 7 per cent.", do=[T("**decimal → %**: × 100", x=80, y=250), MATH("0.07 = 7%", x=640, y=240)]),
        dict(say="To change a percentage to a fraction, write it over 100, then simplify. 36 per cent is 36 over 100, which is 9 over 25.", do=[T("**% → fraction**: over 100, simplify", x=80, y=350), MATH(f"36% = {F(36, 100)} = {F(9, 25)}", x=640, y=330)]),
        dict(say="To change a fraction to a decimal, divide the top by the bottom. 3 divided by 8 is 0.375.", do=[T("**fraction → decimal**: top ÷ bottom", x=80, y=480), MATH(f"{F(3, 8)} = 3 ÷ 8 = 0.375", x=640, y=460)]),
        PAUSE("10.1-k2", "Your turn. Write 3 fifths as a percentage. Pause the video and try it.", "Write 3/5 as a percentage."),
    ]),
    dict(kind="idea", title="Check: 3/5 as a percentage", steps=[
        dict(say="Make the denominator 100. Multiply the top and the bottom by 20. 3 fifths is 60 over 100, which is 60 per cent.", do=[MATH(f"{F(3, 5)} = {F(60, 100)}", x=80, y=180), T("× 20 top and bottom", x=420, y=210, color=GREY), B("60%", x=80, y=340, color=GREEN, at=6)]),
    ]),
    dict(kind="method", title="How do I compare them?", steps=[
        dict(say="Here is the method for comparing fractions, decimals and percentages. Step 1: choose one form. Percentages or decimals are usually easiest.", do=[T("1. Choose **one form** (% or decimals)", x=80, y=170)]),
        dict(say="Step 2: convert every number to that form.", do=[T("2. **Convert** every number", x=80, y=260)]),
        dict(say="Step 3: compare them.", do=[T("3. **Compare**", x=80, y=350)]),
        dict(say="Step 4: write your answer using the original numbers.", do=[T("4. Answer with the **original** numbers", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Percentage to fraction", steps=[
        dict(say="Write 65 per cent as a fraction in its simplest form.", do=[B("65%", x=80, y=160)]),
        dict(say="65 per cent is 65 over 100. Divide the top and the bottom by 5. That gives 13 over 20.", do=[MATH(f"{F(65, 100)} = {F(13, 20)}", x=80, y=280), T("÷ 5 top and bottom", x=420, y=310, color=GREY)]),
        PAUSE("10.1-k3", "Your turn. Write 15 per cent as a fraction in its simplest form. Pause the video and try it.", "Write 15% as a fraction in its simplest form."),
    ]),
    dict(kind="example", title="Check: 15% as a fraction", steps=[
        dict(say="15 per cent is 15 over 100. Divide the top and the bottom by 5. The answer is 3 over 20.", do=[MATH(f"15% = {F(15, 100)} = {F(3, 20)}", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="example", title="Fraction to percentage", steps=[
        dict(say="Write 11 over 25 as a percentage.", do=[MATH(F(11, 25), x=80, y=150)]),
        dict(say="4 times 25 is 100. So multiply the top and the bottom by 4. That gives 44 over 100, which is 44 per cent.", do=[MATH(f"{F(11, 25)} = {F(44, 100)}", x=80, y=280), B("44%", x=80, y=420, color=GREEN, at=6)]),
    ]),
    dict(kind="example", title="An awkward fraction", steps=[
        dict(say="Write 7 over 16 as a decimal, and as a percentage. 16 does not go into 100, so divide.", do=[MATH(F(7, 16), x=80, y=150)]),
        dict(say="7 divided by 16 is 0.4375.", do=[MATH("7 ÷ 16 = 0.4375", x=80, y=290)]),
        dict(say="Multiply by 100. That is 43.75 per cent.", do=[MATH("0.4375 × 100 = 43.75%", x=80, y=380, color=GREEN)]),
    ]),
    dict(kind="example", title="Ordering mixed forms", steps=[
        dict(say="Put these in order, smallest first: 3 fifths, 0.58, 61 per cent, and 5 eighths.", do=[MATH(f"{F(3, 5)}, 0.58, 61%, {F(5, 8)}", x=80, y=150)]),
        dict(say="Write them all as percentages. 3 fifths is 60 per cent. 0.58 is 58 per cent. 5 eighths is 62.5 per cent.", do=[MATH("60%, 58%, 61%, 62.5%", x=80, y=290, color=BLUE)]),
        dict(say="In order: 58, 60, 61, 62.5. So the answer is 0.58, 3 fifths, 61 per cent, 5 eighths.", do=[MATH(f"0.58 < {F(3, 5)} < 61% < {F(5, 8)}", x=80, y=420, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Write 0.4 as a percentage. Here is Zoe's working. Is it right?", do=LINES("Zoe", "0.4 as a percentage", ["0.4 = 4%"])),
        dict(say="Line 1 is wrong. To change a decimal to a percentage, multiply by 100. 0.4 times 100 is 40.", do=[dict(a="cross", id="l1"), MATH("0.4 × 100 = 40", x=110, y=330)]),
        dict(say="So 0.4 is 40 per cent. 4 per cent would be 0.04.", do=[B("0.4 = 40%", x=110, y=430, color=GREEN), T("4% = 0.04", x=520, y=446, color=GREY)]),
    ]),
    dict(kind="life", title="Same amount, three ways", steps=[
        dict(say="Shops, doctors and scientists use all 3 forms. A half price sale is 50 per cent off. It is the same as multiplying the price by 0.5.", do=[E("🏷️", 90, 160, 100), MATH(f"half price = 50% = 0.5 = {F(1, 2)}", x=230, y=170)]),
        dict(say="About 60 per cent of an adult's body is water. That is about 3 fifths.", do=[E("💧", 90, 310, 100), MATH(f"body water ≈ 60% = {F(3, 5)}", x=230, y=310)]),
        dict(say="And a basketball player who scores 17 free throws out of 20 has scored 85 per cent of them.", do=[E("🏀", 90, 460, 100), MATH(f"{F(17, 20)} = 85%", x=230, y=450)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("10.1-k4", "One last question. Write 1 eighth as a percentage. Pause the video and work it out.", "Write 1/8 as a percentage."),
        dict(say="1 divided by 8 is 0.125. Multiply by 100. 1 eighth is 12.5 per cent.", do=[MATH("1 ÷ 8 = 0.125", x=80, y=190), B("12.5%", x=80, y=300, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: percentage to decimal, divide by 100. Decimal to percentage, multiply by 100.", do=[T("• % → decimal: **÷ 100** · decimal → %: **× 100**", x=80, y=170)]),
        dict(say="Percentage to fraction: write it over 100, then simplify.", do=[T("• % → fraction: **over 100**, then simplify", x=80, y=250)]),
        dict(say="Fraction to decimal: divide the top by the bottom.", do=[T("• Fraction → decimal: **top ÷ bottom**", x=80, y=330)]),
        dict(say="To compare, put everything in the same form.", do=[T("• To compare: use the **same form**", x=80, y=410)]),
    ]),
]

VIDEOS["10.2"] = [
    dict(kind="hook", title="Bigger than 100%?", steps=[
        dict(say="A town had 8,000 people. 10 years later, its population is 150 per cent of what it was.", do=[E("🏘️", 90, 160, 110), T("was **8000** people · now **150%** of that", x=240, y=200)]),
        PAUSE("10.2-k1", "How many people live in the town now? Pause the video and work it out.", "150% of 8000 people = ?"),
    ]),
    dict(kind="hook", title="More than the whole", steps=[
        dict(say="100 per cent is the whole amount: 8,000 people. 50 per cent is half of that: 4,000.", do=[MATH("100% = 8000", x=80, y=170), MATH("50% = 4000", x=80, y=260, at=3)]),
        dict(say="150 per cent is 8,000 plus 4,000. The town now has 12,000 people.", do=[MATH("150% = 8000 + 4000", x=80, y=380), B("12 000 people", x=80, y=470, color=GREEN, at=3)]),
    ]),
    dict(kind="recall", title="10% and 1%", steps=[
        dict(say="Remember: to find 10 per cent, divide by 10. To find 1 per cent, divide by 100.", do=[T("**10%**: ÷ 10 · **1%**: ÷ 100", x=80, y=170)]),
        dict(say="You can build other percentages from these. 10 per cent of 320 is 32, so 30 per cent is 3 times 32, which is 96.", do=[MATH("10% of 320 = 32", x=80, y=280), MATH("30% = 3 × 32 = 96", x=80, y=370, at=3.6)]),
    ]),
    dict(kind="idea", title="Percentages greater than 100%", steps=[
        dict(say="100 per cent is the whole amount. More than 100 per cent means more than the whole.",
             do=[TBL(["Percentage", "Decimal", "Meaning"], [["100%", "1", "the whole amount"], ["150%", "1.5", "one and a half times"], ["200%", "2", "double"], ["250%", "2.5", "two and a half times"]], y=160), ROW(0, 2)]),
        dict(say="150 per cent is 1.5 as a decimal. It means one and a half times the amount.", do=[ROW(1, 0.3)]),
        dict(say="200 per cent is 2: double the amount. And 250 per cent is 2.5.", do=[ROW(2, 0.3), ROW(3, 3)]),
        dict(say="The rule is the same as before: to change a percentage to a decimal, divide by 100.", do=[T("still **÷ 100**", x=820, y=260, color=BLUE)]),
        PAUSE("10.2-k2", "Your turn. Write 175 per cent as a decimal. Pause the video and try it.", "Write 175% as a decimal."),
    ]),
    dict(kind="idea", title="Check: 175% as a decimal", steps=[
        dict(say="175 divided by 100 is 1.75. The digits move 2 places to the right.", do=[MATH("175 ÷ 100 = 1.75", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Percentages less than 1%", steps=[
        dict(say="A percentage can also be very small. Less than 1 per cent is less than one hundredth.", do=[T("less than 1% = less than **one hundredth**", x=80, y=150)]),
        dict(say="0.5 per cent is half of 1 per cent. As a decimal, 0.5 divided by 100 is 0.005.", do=[MATH("0.5% = 0.5 ÷ 100 = 0.005", x=80, y=240)]),
        dict(say="A bank pays 0.5 per cent interest on 600 dollars. 1 per cent of 600 is 6, so 0.5 per cent is 3 dollars.", do=[E("🏦", 90, 350, 90), MATH("1% of 600 = 6", x=230, y=350), MATH("0.5% = 3", x=230, y=440, color=GREEN, at=5)]),
        PAUSE("10.2-k3", "Your turn. Find 0.1 per cent of 3,000. Pause the video and try it.", "Find 0.1% of 3000."),
    ]),
    dict(kind="idea", title="Check: 0.1% of 3000", steps=[
        dict(say="1 per cent of 3,000 is 30. 0.1 per cent is one tenth of that, which is 3.", do=[MATH("1% = 30", x=80, y=190), MATH("0.1% = 30 ÷ 10 = 3", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="method", title="How do I find a percentage of an amount?", steps=[
        dict(say="Here is the method. Step 1: change the percentage to a decimal and multiply. Or build it from 100 per cent, 10 per cent and 1 per cent.", do=[T("1. **Decimal × amount**, or build from 100%, 10%, 1%", x=80, y=170)]),
        dict(say="Step 2: more than 100 per cent gives an answer bigger than the amount.", do=[T("2. Over 100% → **bigger** than the amount", x=80, y=260)]),
        dict(say="Step 3: less than 1 per cent gives an answer smaller than one hundredth of the amount.", do=[T("3. Under 1% → **smaller** than one hundredth", x=80, y=350)]),
        dict(say="Step 4: check that the size of your answer makes sense.", do=[T("4. Does the **size** make sense?", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Building a percentage", steps=[
        dict(say="Find 145 per cent of 80.", do=[B("145% of 80", x=80, y=150)]),
        dict(say="100 per cent is 80. 10 per cent is 8, so 40 per cent is 32. And 5 per cent is half of 10 per cent, which is 4.", do=[MATH("100% = 80", x=80, y=260), MATH("40% = 32", x=420, y=260, at=3), MATH("5% = 4", x=720, y=260, at=6.6)]),
        dict(say="Add them: 80 plus 32 plus 4 is 116.", do=[MATH("80 + 32 + 4 = 116", x=80, y=380, color=GREEN)]),
        dict(say="Check the size. 145 per cent is more than the whole, and 116 is more than 80. Good.", do=[T("116 > 80 ✓", x=80, y=480, color=GREY)]),
    ]),
    dict(kind="example", title="A small percentage", steps=[
        dict(say="Find 0.4 per cent of 2,500.", do=[B("0.4% of 2500", x=80, y=150)]),
        dict(say="1 per cent is 25. 0.1 per cent is one tenth of that: 2.5.", do=[MATH("1% = 25", x=80, y=260), MATH("0.1% = 2.5", x=420, y=260, at=2.6)]),
        dict(say="0.4 per cent is 4 times 2.5, which is 10.", do=[MATH("0.4% = 4 × 2.5 = 10", x=80, y=380, color=GREEN)]),
    ]),
    dict(kind="example", title="A decimal percentage", steps=[
        dict(say="Write 3.6 per cent as a decimal, and as a fraction.", do=[B("3.6%", x=80, y=150)]),
        dict(say="First, the decimal. 3.6 divided by 100 is 0.036.", do=[MATH("3.6 ÷ 100 = 0.036", x=80, y=260)]),
        dict(say="0.036 is 36 thousandths. Divide the top and the bottom by 4. That is 9 over 250.", do=[MATH(f"0.036 = {F(36, 1000)} = {F(9, 250)}", x=80, y=360, color=GREEN)]),
    ]),
    dict(kind="example", title="A growing kitten", steps=[
        dict(say="A kitten weighed 0.8 kilograms. Now it weighs 350 per cent of that. What does it weigh now?", do=[E("🐱", 90, 150, 100), T("was **0.8 kg** · now **350%** of that", x=230, y=180)]),
        dict(say="350 per cent is 3.5 as a decimal.", do=[MATH("350% = 3.5", x=80, y=310)]),
        dict(say="3.5 times 0.8 is 2.8. The kitten now weighs 2.8 kilograms.", do=[MATH("3.5 × 0.8 = 2.8", x=80, y=400), B("2.8 kg", x=80, y=490, color=GREEN, at=3)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Find 0.3 per cent of 700. Here is Raj's working. Which line goes wrong first?", do=LINES("Raj", "0.3% of 700", ["0.3% = 0.3", "0.3 × 700 = 210"])),
        dict(say="Line 1 is wrong. 0.3 per cent means 0.3 out of 100, which is 0.003. An answer of 210 would be 30 per cent.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="0.003 times 700 is 2.1. That is a sensible size for such a small percentage.", do=[B("0.003 × 700 = 2.1", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Very big and very small", steps=[
        dict(say="Big percentages describe growth. The population of India today is about 400 per cent of what it was in 1950. That is about 4 times as many people.", do=[E("📈", 90, 160, 100), T("India's population: about **400%** of 1950", x=230, y=190)]),
        dict(say="Small percentages matter too. Carbon dioxide is only about 0.04 per cent of the air.", do=[E("🌍", 90, 310, 100), T("carbon dioxide: about **0.04%** of the air", x=230, y=340)]),
        dict(say="That is 4 parts in every 10,000. But even that small amount helps to keep our planet warm.", do=[MATH("0.04% = " + F(4, "10\\,000"), x=230, y=450)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("10.2-k4", "One last question. What is 200 per cent of 7.5? Pause the video and answer.", "200% of 7.5?"),
        dict(say="200 per cent means double. 2 times 7.5 is 15.", do=[MATH("200% = 2", x=80, y=190), MATH("2 × 7.5 = 15", x=80, y=290, color=GREEN, at=2.4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: to change any percentage to a decimal, divide by 100. 150 per cent is 1.5, and 0.5 per cent is 0.005.", do=[T("• % → decimal: **÷ 100** (150% = 1.5 · 0.5% = 0.005)", x=80, y=170)]),
        dict(say="Over 100 per cent gives more than the amount.", do=[T("• Over 100% → **more** than the amount", x=80, y=250)]),
        dict(say="Under 1 per cent gives less than one hundredth of it.", do=[T("• Under 1% → less than **one hundredth**", x=80, y=330)]),
        dict(say="Build percentages from 100 per cent, 10 per cent and 1 per cent, and check the size of your answer.", do=[T("• Build from 100%, 10%, 1% · **check the size**", x=80, y=410)]),
    ]),
]
