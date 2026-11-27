# -*- coding: utf-8 -*-
"""Stage 9 · Unit 3 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u07 import F

VIDEOS = {}

VIDEOS["3.1"] = [
    dict(kind="hook", title="Tiny chips", steps=[
        dict(say="A computer chip has parts that are 5 times 10 to the power negative 9 metres wide. An engineer works with numbers like this every day.",
             do=[E("💻", 90, 170, 100), MATH("5 × 10⁻⁹ m", x=230, y=190)]),
        PAUSE("3.1-k1", "Does multiplying by 10 to the power negative 9 make a positive number smaller, or bigger? Pause the video and choose.", "× 10⁻⁹ makes a number … smaller or bigger?"),
    ]),
    dict(kind="hook", title="Smaller", steps=[
        dict(say="10 to the power negative 9 is 1 over 1,000,000,000. Multiplying by it is the same as dividing by a billion. So the number gets much smaller.",
             do=[MATH(f"10⁻⁹ = {F(1, '1\\,000\\,000\\,000')}", x=80, y=170), B("much smaller", x=80, y=320, color=GREEN, at=6)]),
    ]),
    dict(kind="recall", title="Powers of 10", steps=[
        dict(say="Remember: 10 cubed is 1,000. 10 to the power 0 is 1. And 10 to the power negative 2 is 0.01.", do=[MATH("10³ = 1000   ·   10⁰ = 1   ·   10⁻² = 0.01", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Positive and negative powers", steps=[
        dict(say="Multiplying by 10 to a positive power moves the digits to the left, so the number gets bigger. Dividing moves them to the right.",
             do=[T("× 10ⁿ → **bigger** · ÷ 10ⁿ → **smaller**", x=80, y=170)]),
        dict(say="Multiplying by 10 to a negative power is the same as dividing. And dividing by 10 to a negative power is the same as multiplying.",
             do=[TBL(["Calculation", "Same as", "Answer"], [["3.9 × 10⁻²", "3.9 ÷ 100", "0.039"], ["0.52 ÷ 10⁻³", "0.52 × 1000", "520"], ["5 ÷ 10²", "5 ÷ 100", "0.05"]], y=260), ROW(0, 4), ROW(1, 7), ROW(2, 9)]),
        PAUSE("3.1-k2", "Your turn. Work out 4.7 times 10 to the power negative 2. Pause the video and try it.", "4.7 × 10⁻²?"),
    ]),
    dict(kind="idea", title="Check: 4.7 × 10⁻²", steps=[
        dict(say="Times 10 to the negative 2 means divide by 100. Move the digits 2 places to the right: 0.047.", do=[B("4.7 ÷ 100 = 0.047", x=80, y=190, color=GREEN)]),
        dict(say="Why does it work? 10 to the negative 2 is 1 hundredth. Multiplying by 1 hundredth is dividing by 100.", do=[MATH(f"10⁻² = {F(1, 100)}", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I use a power of 10?", steps=[
        dict(say="Here is the method. Step 1: rewrite it. Times 10 to the negative N means divide by 10 to the N. Divide by 10 to the negative N means multiply by 10 to the N.", do=[T("1. **Rewrite**: × 10⁻ⁿ = ÷ 10ⁿ · ÷ 10⁻ⁿ = × 10ⁿ", x=80, y=170)]),
        dict(say="Step 2: N tells you how many places.", do=[T("2. **n** = number of places", x=80, y=260)]),
        dict(say="Step 3: move the digits. Left to make it bigger, right to make it smaller.", do=[T("3. **Move** the digits", x=80, y=350)]),
        dict(say="Step 4: check the size. Should the answer be bigger or smaller?", do=[T("4. **Check** the size", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Divide by a negative power", steps=[
        dict(say="Work out 0.072 divided by 10 to the negative 2. Dividing by 10 to the negative 2 is the same as multiplying by 100. So the answer is 7.2.",
             do=[MATH("0.072 ÷ 10⁻² = 0.072 × 100", x=80, y=180), B("7.2", x=80, y=290, color=GREEN, at=7)]),
        PAUSE("3.1-k3", "Your turn. Work out 0.36 divided by 10 to the negative 3. Pause and work it out.", "0.36 ÷ 10⁻³?"),
    ]),
    dict(kind="example", title="Check: 0.36 ÷ 10⁻³", steps=[
        dict(say="Dividing by 10 to the negative 3 means multiplying by 1,000. 0.36 times 1,000 is 360.", do=[B("0.36 × 1000 = 360", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="example", title="A missing power", steps=[
        dict(say="250 times 10 to the N is 0.025. Find N. To get from 250 to 0.025, the digits move 4 places to the right. That is dividing by 10,000, so N is negative 4.",
             do=[MATH("250 × 10ⁿ = 0.025", x=80, y=170), MATH("250 → 0.025: ÷ 10 000", x=80, y=270, at=4), B("n = −4", x=80, y=370, color=GREEN, at=10)]),
    ]),
    dict(kind="example", title="Back to the chip", steps=[
        dict(say="How many 5 nanometre parts fit across a 0.003 metre strip? 0.003 divided by 5 times 10 to the negative 9 is 0.0006 times 10 to the 9, which is 600,000.",
             do=[MATH("0.003 ÷ (5 × 10⁻⁹) = 0.0006 × 10⁹", x=80, y=180), B("600 000", x=80, y=290, color=GREEN, at=9)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Leo works out 5.4 times 10 to the negative 1. Which line is wrong?", do=LINES("Leo", "5.4 × 10⁻¹", ["× 10⁻¹ makes it bigger", "54"])),
        dict(say="Line 1 is wrong. Times 10 to the negative 1 means divide by 10. It makes the number smaller.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="5.4 divided by 10 is 0.54.", do=[B("5.4 ÷ 10 = 0.54", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Nanometres", steps=[
        dict(say="Scientists switch between metres, micrometres and nanometres using powers of 10. A nanometre is 10 to the negative 9 metres. A human hair is about 80,000 nanometres wide.",
             do=[E("🔬", 90, 170, 100), MATH("1 nm = 10⁻⁹ m", x=230, y=190), T("a hair ≈ 80 000 nm", x=230, y=290, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("3.1-k4", "One last question. Work out 82 times 10 to the negative 1. Pause the video and answer.", "82 × 10⁻¹?"),
        dict(say="Times 10 to the negative 1 means divide by 10. 82 divided by 10 is 8.2.", do=[B("82 ÷ 10 = 8.2", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: times 10 to the negative N is the same as divide by 10 to the N.", do=[T("• × 10⁻ⁿ = ÷ 10ⁿ", x=80, y=170)]),
        dict(say="Divide by 10 to the negative N is the same as multiply by 10 to the N.", do=[T("• ÷ 10⁻ⁿ = × 10ⁿ", x=80, y=250)]),
        dict(say="Move the digits N places.", do=[T("• Move the digits n places", x=80, y=330)]),
        dict(say="Check the size of the answer.", do=[T("• Check the size", x=80, y=410)]),
    ]),
]

VIDEOS["3.2"] = [
    dict(kind="hook", title="A fuel stop", steps=[
        dict(say="A car has a 52 litre fuel tank. The driver fills 0.4 of the tank.", do=[E("⛽", 90, 170, 100), T("**0.4** of a **52-litre** tank", x=230, y=200)]),
        PAUSE("3.2-k1", "Without a calculator, how many litres is 0.4 times 52? Pause the video and work it out.", "0.4 × 52?"),
    ]),
    dict(kind="hook", title="20.8 litres", steps=[
        dict(say="Work out 4 times 52, which is 208. 0.4 is 4 divided by 10, so divide 208 by 10. The answer is 20.8 litres.",
             do=[MATH("4 × 52 = 208", x=80, y=180), B("208 ÷ 10 = 20.8", x=80, y=290, color=GREEN, at=6)]),
        dict(say="Estimate to check: 0.4 times 50 is 20. Close.", do=[MATH("estimate 0.4 × 50 = 20 ✓", x=80, y=400)]),
    ]),
    dict(kind="recall", title="Place value", steps=[
        dict(say="Remember: 0.4 is 4 divided by 10. And 0.15 is 15 divided by 100.", do=[MATH("0.4 = 4 ÷ 10   ·   0.15 = 15 ÷ 100", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Multiplying decimals", steps=[
        dict(say="Multiply the whole numbers. Then count the decimal places in both numbers. The answer has that many decimal places.",
             do=[TBL(["Calculation", "Whole numbers", "Decimal places", "Answer"], [["0.6 × 0.7", "6 × 7 = 42", "2", "0.42"], ["1.2 × 2.5", "12 × 25 = 300", "2", "3.00 = 3"]], y=170), ROW(0, 5), ROW(1, 7)]),
        PAUSE("3.2-k2", "Your turn. Work out 0.3 times 0.15. Pause the video and try it.", "0.3 × 0.15?"),
    ]),
    dict(kind="idea", title="Check: 0.3 × 0.15", steps=[
        dict(say="3 times 15 is 45. There are 3 decimal places altogether: one in 0.3, and two in 0.15. So the answer is 0.045.",
             do=[MATH("3 × 15 = 45", x=80, y=180), B("3 decimal places → 0.045", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="idea", title="Dividing by a decimal", steps=[
        dict(say="To divide by a decimal, multiply both numbers by the same power of 10, until the divisor is a whole number. The answer does not change.",
             do=[T("make the divisor **whole** – multiply **both** numbers", x=80, y=170)]),
        dict(say="7.56 divided by 0.09 is the same as 756 divided by 9, which is 84.", do=[MATH("7.56 ÷ 0.09 = 756 ÷ 9 = 84", x=80, y=260)]),
        dict(say="Dividing a positive number by a number between 0 and 1 makes it bigger.", do=[T("÷ a number less than 1 → **bigger**", x=80, y=350, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I multiply and divide decimals?", steps=[
        dict(say="Here is the method. Step 1: estimate the answer.", do=[T("1. **Estimate**", x=80, y=170)]),
        dict(say="Step 2: to multiply, multiply as whole numbers, then put back the total number of decimal places.", do=[T("2. × : whole numbers, then the **total** decimal places", x=80, y=260)]),
        dict(say="Step 3: to divide, multiply both numbers by 10, or 100, until the divisor is whole. Then divide.", do=[T("3. ÷ : scale **both** until the divisor is whole", x=80, y=350)]),
        dict(say="Step 4: compare with your estimate.", do=[T("4. **Compare** with the estimate", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Divide", steps=[
        dict(say="Work out 1.44 divided by 0.012. Multiply both by 1,000: 1,440 divided by 12, which is 120.", do=[MATH("1.44 ÷ 0.012 = 1440 ÷ 12", x=80, y=180), B("120", x=80, y=290, color=GREEN, at=6)]),
        PAUSE("3.2-k3", "Your turn. Work out negative 16 divided by 0.4. Pause and work it out.", "−16 ÷ 0.4?"),
    ]),
    dict(kind="example", title="Check: −16 ÷ 0.4", steps=[
        dict(say="Multiply both by 10: negative 160 divided by 4, which is negative 40.", do=[B("−160 ÷ 4 = −40", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="example", title="Two decimals", steps=[
        dict(say="Work out 2.4 times 0.35. 24 times 35 is 840. There are 3 decimal places, so the answer is 0.840, which is 0.84. Estimate: 2 times 0.4 is 0.8. Close.",
             do=[MATH("24 × 35 = 840", x=80, y=170), B("0.84", x=80, y=280, color=GREEN, at=7), MATH("estimate 2 × 0.4 = 0.8 ✓", x=80, y=380, at=10)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Mia works out 0.2 times 0.3. Which line is wrong?", do=LINES("Mia", "0.2 × 0.3", ["2 × 3 = 6", "so 0.6"])),
        dict(say="Line 2 is wrong. There are 2 decimal places altogether, not 1.", do=[dict(a="cross", id="l2")]),
        dict(say="So the answer is 0.06.", do=[B("0.2 × 0.3 = 0.06", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="At the shop", steps=[
        dict(say="Cheese costs 12 dollars 40 per kilogram. 0.75 of a kilogram costs 12.40 times 0.75, which is 9 dollars 30.",
             do=[E("🧀", 90, 170, 100), MATH("12.40 × 0.75 = 9.30", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("3.2-k4", "One last question. Work out 3 divided by 0.5. Pause the video and answer.", "3 ÷ 0.5?"),
        dict(say="Multiply both by 10: 30 divided by 5 is 6. There are 6 halves in 3.", do=[B("30 ÷ 5 = 6", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: estimate first.", do=[T("• Estimate first", x=80, y=170)]),
        dict(say="When multiplying, count the decimal places in both numbers.", do=[T("• × : total decimal places", x=80, y=250)]),
        dict(say="When dividing, scale both numbers to make the divisor whole.", do=[T("• ÷ : make the divisor whole", x=80, y=330)]),
        dict(say="Dividing by a number less than 1 makes a positive number bigger.", do=[T("• ÷ less than 1 → bigger", x=80, y=410)]),
    ]),
]

VIDEOS["3.3"] = [
    dict(kind="hook", title="A savings account", steps=[
        dict(say="Ravi puts 2,000 dollars in a savings account. It pays 4 percent interest each year, added to the account. Next year, interest is paid on the interest too.",
             do=[E("🏦", 90, 170, 100), T("**$2000** at **4%** a year, added each year", x=230, y=200)]),
        PAUSE("3.3-k1", "After 3 years, has his money grown by exactly 12 percent? Pause the video and choose.", "After 3 years, is it exactly 12% more?"),
    ]),
    dict(kind="hook", title="A bit more than 12%", steps=[
        dict(say="No. Each year's 4 percent is of a bigger amount. So the total growth is a bit more than 12 percent.",
             do=[B("slightly more than 12%", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Multipliers", steps=[
        dict(say="Remember: to increase by 20 percent, multiply by 1.2. To decrease by 20 percent, multiply by 0.8.", do=[MATH("+20% → × 1.2   ·   −20% → × 0.8", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Compound percentages", steps=[
        dict(say="A compound percentage change applies the percentage again and again, each time to the new amount.",
             do=[TBL(["Year", "Start ($)", "End = start × 1.04 ($)"], [["1", "2000.00", "2080.00"], ["2", "2080.00", "2163.20"], ["3", "2163.20", "2249.73"]], y=170), ROW(0, 2), ROW(1, 3), ROW(2, 4)]),
        dict(say="After 3 years Ravi has 2,249 dollars 73. That is more than 2,240, which is what 12 percent would give.", do=[B("$2249.73 > $2240", x=80, y=420, color=GREEN)]),
        PAUSE("3.3-k2", "Your turn. Times 1.04, three times, is one multiplier. What is it, to 3 decimal places? Pause the video and try it.", "Multiplier for 4% each year for 3 years (3 d.p.)?"),
    ]),
    dict(kind="idea", title="Check: 1.04³", steps=[
        dict(say="1.04 cubed is 1.124864. To 3 decimal places, that is 1.125. So the money grows by about 12.5 percent.", do=[B("1.04³ = 1.124864 ≈ 1.125", x=80, y=190, color=GREEN)]),
        dict(say="Values that fall each year use a multiplier less than 1. A car that loses 15 percent a year keeps 85 percent: value equals start, times 0.85 to the N.",
             do=[MATH("−15% a year → × 0.85ⁿ", x=80, y=310)]),
    ]),
    dict(kind="method", title="How do I calculate a compound change?", steps=[
        dict(say="Here is the method. Step 1: find the multiplier. 1 plus R over 100 for an increase, 1 minus R over 100 for a decrease.", do=[T("1. Multiplier = 1 ± r/100", x=80, y=170)]),
        dict(say="Step 2: raise it to the power of the number of years.", do=[T("2. Power = number of **periods**", x=80, y=260)]),
        dict(say="Step 3: multiply by the starting amount.", do=[T("3. × the **start**", x=80, y=350)]),
        dict(say="Step 4: round only at the end.", do=[T("4. Round at the **end**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A car", steps=[
        dict(say="A car is worth 18,000 dollars. It loses 15 percent of its value each year. What is it worth after 2 years?", do=[E("🚙", 90, 170, 90), T("**$18 000**, −15% a year", x=230, y=200)]),
        PAUSE("3.3-k3", "Your turn. What is the multiplier for a 15 percent decrease? Pause and work it out.", "Multiplier for a 15% decrease?"),
    ]),
    dict(kind="example", title="Check: 0.85", steps=[
        dict(say="100 minus 15 is 85 percent, so the multiplier is 0.85. After 2 years: 18,000 times 0.85 squared, which is 13,005 dollars.",
             do=[B("× 0.85", x=80, y=180, color=GREEN), MATH("18 000 × 0.85² = 13 005", x=80, y=290, at=5)]),
    ]),
    dict(kind="example", title="How many years?", steps=[
        dict(say="1,000 dollars earns 5 percent a year. When does it first go over 1,200 dollars? 1.05 cubed is about 1.158. 1.05 to the 4 is about 1.216. So it takes 4 years.",
             do=[MATH("1.05³ ≈ 1.158   ·   1.05⁴ ≈ 1.216", x=80, y=180), B("4 years", x=80, y=290, color=GREEN, at=10)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A price rises 10 percent one year, and 10 percent the next. Kai works out the total change. Which line is wrong?", do=LINES("Kai", "+10% then +10%", ["total increase = 20%", "multiplier 1.2"])),
        dict(say="Line 1 is wrong. The second 10 percent is of the new, bigger price.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="1.1 times 1.1 is 1.21. That is a 21 percent increase.", do=[B("1.1² = 1.21 → 21%", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Everyday growth", steps=[
        dict(say="Banks, loans, inflation and population growth all use compound percentages. A town of 25,000 that grows 2 percent a year has about 27,600 people after 5 years.",
             do=[E("🏙️", 90, 170, 100), MATH("25 000 × 1.02⁵ ≈ 27 600", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("3.3-k4", "One last question. A price rises 10 percent, then falls 10 percent. What is the overall multiplier? Pause the video and answer.", "+10% then −10%: multiplier?"),
        dict(say="1.1 times 0.9 is 0.99. That is a 1 percent decrease overall, not zero.", do=[B("1.1 × 0.9 = 0.99", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the multiplier is 1 plus or minus R over 100.", do=[T("• Multiplier = 1 ± r/100", x=80, y=170)]),
        dict(say="For N years, raise the multiplier to the power N.", do=[T("• n periods → multiplierⁿ", x=80, y=250)]),
        dict(say="Changes one after another multiply.", do=[T("• Successive changes multiply", x=80, y=330)]),
        dict(say="Round at the end.", do=[T("• Round at the end", x=80, y=410)]),
    ]),
]

VIDEOS["3.4"] = [
    dict(kind="hook", title="Crowd size", steps=[
        dict(say="A news report says 65,000 fans watched a match. The number is rounded to the nearest thousand.", do=[E("🏟️", 90, 170, 100), T("**65 000** fans (nearest 1000)", x=230, y=200)]),
        PAUSE("3.4-k1", "What is the smallest the real crowd could have been? Pause the video and work it out.", "Smallest possible crowd?"),
    ]),
    dict(kind="hook", title="64,500", steps=[
        dict(say="64,500 is the smallest number that rounds up to 65,000. Anything less would round down to 64,000.", do=[B("64 500", x=80, y=190, color=GREEN)]),
        dict(say="The largest crowd is 65,499, because 65,500 would round up to 66,000.", do=[MATH("largest: 65 499", x=80, y=300)]),
    ]),
    dict(kind="recall", title="Rounding", steps=[
        dict(say="Remember: 4.36 to 1 decimal place is 4.4. 2,450 to the nearest 100 is 2,500.", do=[MATH("4.36 → 4.4   ·   2450 → 2500", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Upper and lower bounds", steps=[
        dict(say="A rounded value stands for a range. Go half a unit down for the lower bound, and half a unit up for the upper bound.",
             do=[TBL(["Rounded value", "Accuracy", "Lower bound", "Upper bound"], [["65 000", "nearest 1000", "64 500", "65 500"], ["2.3 m", "1 d.p.", "2.25 m", "2.35 m"]], y=170), ROW(0, 3), ROW(1, 6)]),
        PAUSE("3.4-k2", "Your turn. A length is 4.7 metres, to 1 decimal place. What is its upper bound? Pause the video and try it.", "4.7 m to 1 d.p. Upper bound?"),
    ]),
    dict(kind="idea", title="Check: 4.7 m", steps=[
        dict(say="The unit is 0.1. Half of 0.1 is 0.05. So the bounds are 4.65 and 4.75. The upper bound is 4.75 metres.", do=[B("4.65 ≤ L < 4.75", x=80, y=190, color=GREEN)]),
        dict(say="Write the range as an inequality. The lower bound is included. The upper bound is not, because 4.75 would round up to 4.8.", do=[T("lower **≤** L **<** upper", x=80, y=300, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I find the bounds?", steps=[
        dict(say="Here is the method. Step 1: find the accuracy: the unit it was rounded to.", do=[T("1. The **unit** of rounding", x=80, y=170)]),
        dict(say="Step 2: halve that unit.", do=[T("2. **Halve** it", x=80, y=260)]),
        dict(say="Step 3: lower bound is the value minus a half unit. Upper bound is the value plus a half unit.", do=[T("3. Value **±** half a unit", x=80, y=350)]),
        dict(say="Step 4: write: lower, less than or equal to X, less than upper.", do=[T("4. lower ≤ x < upper", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Nearest 5", steps=[
        dict(say="A time is 40 seconds, to the nearest 5 seconds. Half of 5 is 2.5. So the bounds are 37.5 and 42.5 seconds.",
             do=[MATH("½ × 5 = 2.5", x=80, y=180), B("37.5 ≤ t < 42.5", x=80, y=290, color=GREEN, at=5)]),
        PAUSE("3.4-k3", "Your turn. A mass is 320 grams, to the nearest 10 grams. What are its bounds? Pause and work it out.", "Bounds of 320 g to the nearest 10 g?"),
    ]),
    dict(kind="example", title="Check: 320 g", steps=[
        dict(say="Half of 10 is 5. So the mass is at least 315 grams, and less than 325 grams.", do=[B("315 ≤ m < 325", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="example", title="Is it possible?", steps=[
        dict(say="A rope is 12 metres long, to the nearest metre. Could it really be 12.6 metres? The bounds are 11.5 and 12.5. 12.6 is too long, so no.",
             do=[MATH("11.5 ≤ L < 12.5", x=80, y=180), B("12.6 m? No", x=80, y=290, color=RED, at=9)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A mass is 6.2 kilograms to 1 decimal place. Ana writes the bounds. Which line is wrong?", do=LINES("Ana", "6.2 kg to 1 d.p.", ["bounds 5.7 kg and 6.7 kg"])),
        dict(say="Line 1 is wrong. She used half of 1. The unit is 0.1, and half of 0.1 is 0.05.", do=[dict(a="cross", id="l1")]),
        dict(say="The bounds are 6.15 and 6.25 kilograms.", do=[B("6.15 ≤ m < 6.25", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Engineering tolerances", steps=[
        dict(say="Engineers give tolerances, like 10 millimetres, plus or minus 0.05 millimetres, so that parts always fit together.", do=[E("⚙️", 90, 170, 100), MATH("10 mm ± 0.05 mm", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("3.4-k4", "One last question. A number is 90, to the nearest 10. What is its lower bound? Pause the video and answer.", "90 to the nearest 10. Lower bound?"),
        dict(say="Half of 10 is 5. 90 minus 5 is 85.", do=[B("85", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the bounds are half a unit either side.", do=[T("• Half a unit either side", x=80, y=170)]),
        dict(say="Write lower, less than or equal to X, less than upper.", do=[T("• lower ≤ x < upper", x=80, y=250)]),
        dict(say="The upper bound itself rounds up.", do=[T("• The upper bound rounds up", x=80, y=330)]),
        dict(say="Check the accuracy carefully.", do=[T("• Check the accuracy", x=80, y=410)]),
    ]),
]
