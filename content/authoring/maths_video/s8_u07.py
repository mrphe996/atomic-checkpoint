# -*- coding: utf-8 -*-
"""Stage 8 · Unit 7 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW, STEPT
from .s7_u07 import F, M, BAR

K = lambda s: f"$${s}$$"                       # any KaTeX
DOT = lambda s: K(s.replace("[", "\\dot{").replace("]", "}"))   # "0.[3]" → 0.3̇

VIDEOS = {}

VIDEOS["7.1"] = [
    dict(kind="hook", title="A never-ending answer", steps=[
        dict(say="Three friends share a 10 dollar bill. A calculator shows 10 divided by 3 equals 3.333333333.", do=[E("🧾", 90, 170, 100), MATH("10 ÷ 3 = 3.333333333", x=230, y=190)]),
        dict(say="The screen runs out of space. But does the 3 ever stop?", do=[T("does the **3** ever stop?", x=230, y=290)]),
        PAUSE("7.1-k1", "Do the 3s stop, or go on forever? Pause the video and decide.", "10 ÷ 3 = 3.333… – the 3s …"),
    ]),
    dict(kind="hook", title="Forever", steps=[
        dict(say="Divide 10 by 3 by hand. Every step leaves a remainder of 1, so the next digit is always 3. The 3s go on forever.",
             do=[MATH("1.0 ÷ 3 → 3 remainder 1 → 3 remainder 1 → …", x=80, y=190), B("the 3s go on forever", x=80, y=300, color=GREEN, at=5)]),
    ]),
    dict(kind="recall", title="Fraction to decimal", steps=[
        dict(say="Remember: to change a fraction to a decimal, divide the numerator by the denominator. 3 eighths is 3 divided by 8, which is 0.375.",
             do=[MATH(f"{F(3, 8)} = 3 ÷ 8 = 0.375", x=80, y=180)]),
    ]),
    dict(kind="idea", title="Terminating and recurring", steps=[
        dict(say="A terminating decimal ends, like 0.375. A recurring decimal repeats forever. 1 third is 0.333, and so on. 2 elevenths is 0.181818, and so on.",
             do=[T("**terminating**: ends · 3/8 = 0.375", x=80, y=170), T("**recurring**: repeats forever · 1/3 = 0.333… · 2/11 = 0.1818…", x=80, y=250, at=4)]),
        dict(say="We show the repeating digits with dots. One dot means one digit repeats. Dots on the first and last digit mean the whole block repeats.",
             do=[MATH(f"{F(1, 3)} = " + DOT("0.[3]"), x=80, y=340), MATH(f"{F(2, 11)} = " + DOT("0.[1][8]"), x=480, y=340, at=3)]),
        PAUSE("7.1-k2", "Your turn. How is 0.272727 and so on written with dots? Pause the video and choose.", "0.272727… is written …"),
    ]),
    dict(kind="idea", title="Check: 0.2727…", steps=[
        dict(say="The pair 2 7 repeats. So put a dot over the 2 and over the 7.", do=[MATH("0.272727… = " + DOT("0.[2][7]"), x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Which fractions terminate?", steps=[
        dict(say="Write the fraction in its simplest form. If the only prime factors of the denominator are 2 and 5, the decimal terminates. That is because it can be made into tenths, hundredths, or thousandths.",
             do=[B("denominator = only 2s and 5s → terminates", x=80, y=170, color=BLUE), MATH(f"{F(3, 8)}: 8 = 2³ ✓", x=80, y=270, at=6)]),
        dict(say="Any other prime factor, like 3, 7 or 11, makes it recur.", do=[MATH(f"{F(5, 6)}: 6 = 2 × 3 → recurs", x=80, y=370)]),
    ]),
    dict(kind="method", title="How do I convert and classify?", steps=[
        dict(say="Here is the method. Step 1: simplify the fraction first.", do=[T("1. **Simplify** first", x=80, y=170)]),
        dict(say="Step 2: find the prime factors of the denominator. Only 2s and 5s means it terminates.", do=[T("2. Denominator only **2s and 5s** → terminating", x=80, y=260)]),
        dict(say="Step 3: divide the numerator by the denominator, using short division and adding zeros.", do=[T("3. **Short division**, adding zeros", x=80, y=350)]),
        dict(say="Step 4: if a remainder comes back, the digits will repeat. Mark them with dots.", do=[T("4. A **remainder repeats** → the digits repeat", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="4 sevenths", steps=[
        dict(say="Write 4 sevenths as a decimal. Divide 4.000000 by 7. The digits are 5, 7, 1, 4, 2, 8.", do=[MATH("4.000000 ÷ 7 = 0.571428…", x=80, y=170)]),
        dict(say="The remainders are 5, 1, 3, 2, 6, then 4 again. We are back to the start, so the six digits repeat.", do=[T("remainders 5, 1, 3, 2, 6, then **4 again**", x=80, y=270)]),
        dict(say="4 sevenths is 0.571428 recurring, with dots on the 5 and the 8.", do=[MATH(f"{F(4, 7)} = " + DOT("0.[5]7142[8]"), x=80, y=370, color=GREEN)]),
    ]),
    dict(kind="example", title="Predicting", steps=[
        dict(say="Will 9 seventy-fifths terminate? Simplify first. 9 seventy-fifths is 3 twenty-fifths.", do=[MATH(f"{F(9, 75)} = {F(3, 25)}", x=80, y=170)]),
        dict(say="25 is 5 squared. Only 5s, so it terminates. 3 twenty-fifths is 0.12.", do=[MATH("25 = 5²", x=80, y=290), B("yes: 0.12", x=80, y=380, color=GREEN, at=3)]),
        PAUSE("7.1-k3", "Your turn. Does 11 eightieths terminate? Pause and choose.", "Does 11/80 terminate?"),
    ]),
    dict(kind="example", title="Check: 11/80", steps=[
        dict(say="11 eightieths is already in its simplest form. 80 is 2 to the power 4, times 5. Only 2s and 5s, so yes, it terminates. It is 0.1375.",
             do=[MATH("80 = 2⁴ × 5", x=80, y=190), B("yes – terminates (0.1375)", x=80, y=290, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Comparing", steps=[
        dict(say="Which is larger: 5 ninths, or 0.55? 5 ninths is 0.5555, and so on. Compare 0.5555 with 0.5500. 5 ninths is larger.",
             do=[MATH(f"{F(5, 9)} = 0.5555…", x=80, y=170), MATH("0.5555… > 0.5500", x=80, y=270, at=5), B(f"{F(5, 9)} is larger", x=80, y=380, color=GREEN, at=8)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Nia asks: does 3 twelfths give a recurring decimal? Which line goes wrong first?", do=LINES("Nia", "does 3/12 recur?", ["12 = 2² × 3 has a factor 3", "so it recurs"])),
        dict(say="Line 1 is wrong. She did not simplify first. 3 twelfths is 1 quarter, and 4 is 2 squared.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="So it terminates. 1 quarter is 0.25.", do=[B(f"{F(3, 12)} = {F(1, 4)} = 0.25", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Why a third is awkward", steps=[
        dict(say="Money uses hundredths, so it cannot split 10 dollars exactly into three. Each friend pays 3 dollars 33, and 1 cent is left over.",
             do=[E("💵", 90, 170, 100), MATH("3 × $3.33 = $9.99", x=230, y=190), T("1 cent left over!", x=230, y=290, color=RED)]),
        dict(say="Because 3 is not a factor of 10, a third can never be written exactly as a decimal.", do=[T("3 is not a factor of 10 → recurring", x=230, y=380, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.1-k4", "One last question. Write 2 ninths as a decimal, to 3 decimal places. Pause the video and answer.", "2/9 as a decimal (3 d.p.)?"),
        dict(say="2 divided by 9 is 0.2222, and so on. To 3 decimal places, that is 0.222.", do=[MATH(f"{F(2, 9)} = " + DOT("0.[2]") + " ≈ 0.222", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: terminating decimals end. Recurring decimals repeat.", do=[T("• Terminating decimals **end**; recurring decimals **repeat**", x=80, y=170)]),
        dict(say="Dots mark the repeating digits.", do=[T("• Dots mark the repeating digits", x=80, y=250)]),
        dict(say="In simplest form, a denominator with only 2s and 5s gives a terminating decimal.", do=[T("• Simplest form, only 2s and 5s → terminating", x=80, y=330)]),
        dict(say="Use short division, and watch for a remainder that comes back.", do=[T("• Short division: watch for a repeated remainder", x=80, y=410)]),
    ]),
]

VIDEOS["7.2"] = [
    dict(kind="hook", title="Divers", steps=[
        dict(say="Three divers are below the surface. Their depths are negative 2 and 3 quarters metres, negative 2 and 5 sevenths metres, and negative 2.7 metres.",
             do=[E("🤿", 90, 170, 100), MATH(f"{M('-2', 3, 4)},  {M('-2', 5, 7)},  −2.7 m", x=230, y=180)]),
        PAUSE("7.2-k1", "Who is deepest? Type the depth as a decimal. Pause the video and work it out.", "Deepest diver? Type the decimal."),
    ]),
    dict(kind="hook", title="The deepest diver", steps=[
        dict(say="Change them to decimals. 3 quarters is 0.75. 5 sevenths is about 0.714. So the depths are negative 2.75, about negative 2.714, and negative 2.7.",
             do=[MATH("−2.75,  −2.714…,  −2.7", x=80, y=190)]),
        dict(say="The deepest is the furthest below zero: negative 2.75 metres.", do=[B("deepest: −2.75 m", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="recall", title="Common denominators", steps=[
        dict(say="Remember: to compare 3 quarters and 5 sevenths, use a common denominator of 28. 3 quarters is 21 twenty-eighths, and 5 sevenths is 20 twenty-eighths. So 3 quarters is larger.",
             do=[MATH(f"{F(3, 4)} = {F(21, 28)}", x=80, y=170), MATH(f"{F(5, 7)} = {F(20, 28)}", x=400, y=170, at=4), B(f"{F(3, 4)} > {F(5, 7)}", x=80, y=300, color=GREEN, at=8)]),
    ]),
    dict(kind="idea", title="Negative fractions", steps=[
        dict(say="Order positive fractions using a common denominator, or decimals. For negative fractions, the one with the bigger size is further left, so it is smaller.",
             do=[B("negatives: bigger size → **smaller**", x=80, y=170, color=BLUE)]),
        dict(say="For example, 3 fifths is bigger than 1 half. So negative 3 fifths is smaller than negative 1 half.",
             do=[MATH(f"{F(3, 5)} > {F(1, 2)}", x=80, y=270), MATH(f"−{F(3, 5)} < −{F(1, 2)}", x=80, y=370, at=4)]),
        PAUSE("7.2-k2", "Your turn. Which is larger: negative 2 ninths, or negative 1 quarter? Pause the video and choose.", "Larger: −2/9 or −1/4?"),
    ]),
    dict(kind="idea", title="Check: −2/9 or −1/4", steps=[
        dict(say="Negative 2 ninths is closer to zero, so it is larger. 2 ninths is about 0.222, and 1 quarter is 0.25.", do=[MATH("−0.222… > −0.25", x=80, y=190), B(f"−{F(2, 9)} is larger", x=80, y=300, color=GREEN, at=4)]),
        dict(say="Choose your method. A common denominator is exact. Decimals are quick. And comparing with a half gives a fast first sort.", do=[T("common denominator · decimals · compare with ½", x=80, y=420)]),
    ]),
    dict(kind="method", title="How do I order fractions?", steps=[
        dict(say="Here is the method. Step 1: split into negatives and positives. Change improper fractions to mixed numbers.", do=[T("1. Negatives / positives; improper → **mixed**", x=80, y=170)]),
        dict(say="Step 2: compare the whole number parts first.", do=[T("2. Compare the **whole numbers** first", x=80, y=260)]),
        dict(say="Step 3: compare the fraction parts, with a common denominator or decimals.", do=[T("3. Then the fractions: common denominator or decimals", x=80, y=350)]),
        dict(say="Step 4: for negatives, remember that the order turns round.", do=[T("4. Negatives: the order **turns round**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Positive fractions", steps=[
        dict(say="Order 5 sixths, 7 ninths and 3 quarters, smallest first. The lowest common multiple of 6, 9 and 4 is 36.", do=[MATH(f"{F(5, 6)},  {F(7, 9)},  {F(3, 4)}", x=80, y=170)]),
        dict(say="That gives 30, 28 and 27 thirty-sixths. So the order is 3 quarters, 7 ninths, 5 sixths.", do=[MATH(f"{F(30, 36)},  {F(28, 36)},  {F(27, 36)}", x=80, y=280), B(f"{F(3, 4)},  {F(7, 9)},  {F(5, 6)}", x=80, y=400, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="Improper fractions", steps=[
        dict(say="Which is larger: 19 sevenths, or 2 and 3 quarters? 19 sevenths is 2 and 5 sevenths.", do=[MATH(f"{F(19, 7)} = {M(2, 5, 7)}", x=80, y=170)]),
        PAUSE("7.2-k3", "Your turn. So which is larger? Pause and choose.", "Larger: 19/7 or 2 3/4?"),
    ]),
    dict(kind="example", title="Check: 19/7 or 2 3/4", steps=[
        dict(say="The whole numbers are both 2. Then 3 quarters is larger than 5 sevenths, as we found before. So 2 and 3 quarters is larger.", do=[B(f"{M(2, 3, 4)} is larger", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="A fraction in between", steps=[
        dict(say="Find a fraction between negative 2 thirds and negative 3 fifths. As decimals, they are negative 0.666 and negative 0.6.", do=[MATH("−0.666…  and  −0.6", x=80, y=170)]),
        dict(say="Negative 0.63 is between them. That is negative 63 hundredths.", do=[B(f"−0.63 = −{F(63, 100)}", x=80, y=280, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Zoe asks: which is smaller, negative 1 quarter or negative 1 third? Which line is wrong?", do=LINES("Zoe", "−1/4 or −1/3?", ["1/4 < 1/3", "so −1/4 < −1/3"])),
        dict(say="Line 2 is wrong. For negatives, the inequality turns round. Negative 1 third is further from zero.", do=[dict(a="cross", id="l2")]),
        dict(say="So negative 1 third is smaller than negative 1 quarter.", do=[B(f"−{F(1, 3)} < −{F(1, 4)}", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Spanner sizes", steps=[
        dict(say="Some tools are sized in fractions of an inch. A mechanic must choose between spanners of 5 eighths, 9 sixteenths and 11 sixteenths of an inch.",
             do=[E("🔧", 90, 170, 100), MATH(f"{F(5, 8)},  {F(9, 16)},  {F(11, 16)} inch", x=230, y=180)]),
        dict(say="Using sixteenths: 5 eighths is 10 sixteenths. So the order is 9, 10, 11 sixteenths. The 5 eighths spanner is in the middle.", do=[MATH(f"{F(9, 16)} < {F(10, 16)} < {F(11, 16)}", x=230, y=320, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.2-k4", "One last question. Which sign goes between negative 0.6 and negative 2 thirds? Pause the video and choose.", "−0.6 ☐ −2/3"),
        dict(say="2 thirds is 0.666, which is bigger than 0.6. So negative 2 thirds is further left. Negative 0.6 is greater than negative 2 thirds.", do=[B(f"−0.6 > −{F(2, 3)}", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: use common denominators or decimals.", do=[T("• Common denominators or decimals", x=80, y=170)]),
        dict(say="Change improper fractions to mixed numbers.", do=[T("• Improper → mixed numbers", x=80, y=250)]),
        dict(say="For negatives, the bigger size is the smaller number.", do=[T("• Negatives: bigger size = smaller number", x=80, y=330)]),
        dict(say="Choose the method that suits the numbers.", do=[T("• Choose the method that suits the numbers", x=80, y=410)]),
    ]),
]

VIDEOS["7.3"] = [
    dict(kind="hook", title="Cutting a plank", steps=[
        dict(say="A builder has a plank 5 and 1 quarter metres long. She cuts off 2 and 2 thirds metres.", do=[E("🪵", 90, 170, 100), MATH(f"{M(5, 1, 4)} − {M(2, 2, 3)}", x=230, y=180)]),
        dict(say="The fraction 1 quarter is smaller than 2 thirds. How do you deal with that?", do=[T(f"1/4 is **smaller** than 2/3", x=230, y=290)]),
        PAUSE("7.3-k1", "How much plank is left? Pause the video and work it out.", "5 1/4 − 2 2/3 = ?"),
    ]),
    dict(kind="hook", title="Improper fractions", steps=[
        dict(say="One way is to use improper fractions. 5 and 1 quarter is 21 quarters. 2 and 2 thirds is 8 thirds.",
             do=[STEPT("5 1/4 − 2 2/3", [["improper fractions", "21/4 − 8/3"], ["common denominator", "63/12 − 32/12"], ["subtract", "31/12"], ["mixed number", "2 7/12"]], y=160), ROW(0, 0.4)]),
        dict(say="With a common denominator of 12: 63 twelfths minus 32 twelfths is 31 twelfths. That is 2 and 7 twelfths metres.", do=[ROW(1, 0.4), ROW(2, 3), ROW(3, 5)]),
    ]),
    dict(kind="recall", title="Common denominators", steps=[
        dict(say="Remember: to subtract fractions, use a common denominator. 5 sixths minus 1 quarter is 10 twelfths minus 3 twelfths, which is 7 twelfths.",
             do=[MATH(f"{F(5, 6)} − {F(1, 4)} = {F(10, 12)} − {F(3, 12)} = {F(7, 12)}", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Regrouping", steps=[
        dict(say="Another way: subtract the wholes and the fractions separately. If the first fraction is too small, exchange 1 whole for fractions.",
             do=[T("subtract wholes and fractions; if needed **exchange 1 whole**", x=80, y=170)]),
        dict(say="5 and 3 twelfths minus 2 and 8 twelfths. 3 twelfths is too small, so change 5 and 3 twelfths into 4 and 15 twelfths.",
             do=[MATH(f"{M(5, 3, 12)} − {M(2, 8, 12)}", x=80, y=260), MATH(f"= {M(4, 15, 12)} − {M(2, 8, 12)}", x=80, y=360, at=5)]),
        dict(say="Now 4 minus 2 is 2, and 15 twelfths minus 8 twelfths is 7 twelfths. The answer is 2 and 7 twelfths again.", do=[B(f"= {M(2, 7, 12)}", x=80, y=460, color=GREEN)]),
        PAUSE("7.3-k2", "Your turn. Work out 3 and 3 quarters, minus 1 and 1 quarter. Pause the video and try it.", "Work out 3 3/4 − 1 1/4."),
    ]),
    dict(kind="idea", title="Check: 3 3/4 − 1 1/4", steps=[
        dict(say="3 minus 1 is 2. 3 quarters minus 1 quarter is 2 quarters, which is a half. The answer is 2 and a half.", do=[MATH(f"2 + {F(2, 4)} = {M(2, 1, 2)}", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I subtract mixed numbers?", steps=[
        dict(say="Here is the method. Step 1: estimate with whole numbers.", do=[T("1. **Estimate** with whole numbers", x=80, y=170)]),
        dict(say="Step 2: either change both to improper fractions, or keep the wholes and fractions separate.", do=[T("2. Improper fractions, **or** wholes and fractions separately", x=80, y=260)]),
        dict(say="Step 3: use a common denominator. If the first fraction is smaller, exchange 1 whole.", do=[T("3. Common denominator; **exchange 1 whole** if needed", x=80, y=350)]),
        dict(say="Step 4: simplify, then check by adding back.", do=[T("4. Simplify; **check** by adding back", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Regrouping", steps=[
        dict(say="Work out 7 and 1 fifth, minus 3 and 1 half. With tenths, that is 7 and 2 tenths, minus 3 and 5 tenths.", do=[MATH(f"{M(7, 2, 10)} − {M(3, 5, 10)}", x=80, y=170)]),
        dict(say="2 tenths is too small, so exchange 1 whole: 6 and 12 tenths, minus 3 and 5 tenths. That is 3 and 7 tenths.",
             do=[MATH(f"= {M(6, 12, 10)} − {M(3, 5, 10)}", x=80, y=270), B(f"= {M(3, 7, 10)}", x=80, y=380, color=GREEN, at=5)]),
        PAUSE("7.3-k3", "Your turn. Work out 6 and 1 sixth, minus 2 and 1 half. Pause and work it out.", "Work out 6 1/6 − 2 1/2."),
    ]),
    dict(kind="example", title="Check: 6 1/6 − 2 1/2", steps=[
        dict(say="In sixths: 6 and 1 sixth minus 2 and 3 sixths. Exchange 1 whole: 5 and 7 sixths minus 2 and 3 sixths. That is 3 and 4 sixths, which simplifies to 3 and 2 thirds.",
             do=[MATH(f"{M(5, 7, 6)} − {M(2, 3, 6)} = {M(3, 4, 6)}", x=80, y=190), B(f"= {M(3, 2, 3)}", x=80, y=300, color=GREEN, at=8)]),
    ]),
    dict(kind="example", title="From a whole number", steps=[
        dict(say="Work out 5 minus 1 and 5 eighths. Write 5 as 4 and 8 eighths. Then 4 minus 1 is 3, and 8 eighths minus 5 eighths is 3 eighths.",
             do=[MATH(f"5 − {M(1, 5, 8)} = {M(4, 8, 8)} − {M(1, 5, 8)}", x=80, y=170), B(f"= {M(3, 3, 8)}", x=80, y=290, color=GREEN, at=7)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Leo works out 3 and 1 fifth, minus 1 and 3 fifths. Which line goes wrong first?", do=LINES("Leo", "3 1/5 − 1 3/5", ["3 − 1 = 2", "3/5 − 1/5 = 2/5", "Answer: 2 2/5"])),
        dict(say="Line 2 is wrong. He subtracted the fractions the wrong way round. It must be 1 fifth minus 3 fifths, which is too small. So exchange 1 whole.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="2 and 6 fifths minus 1 and 3 fifths is 1 and 3 fifths.", do=[B(f"{M(2, 6, 5)} − {M(1, 3, 5)} = {M(1, 3, 5)}", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Rainfall", steps=[
        dict(say="Rain gauges in some countries measure in inches. One week there was 3 and 1 eighth inches of rain. The next week there was 1 and 3 quarters inches.",
             do=[E("🌧️", 90, 170, 100), MATH(f"{M(3, 1, 8)} − {M(1, 3, 4)}", x=230, y=180)]),
        dict(say="The difference is 3 and 1 eighth minus 1 and 6 eighths. Exchange 1 whole: 2 and 9 eighths minus 1 and 6 eighths, which is 1 and 3 eighths inches.",
             do=[MATH(f"{M(2, 9, 8)} − {M(1, 6, 8)} = {M(1, 3, 8)}", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.3-k4", "One last question. What is 2 minus 3 sevenths? Pause the video and answer.", "2 − 3/7 = ?"),
        dict(say="Write 2 as 1 and 7 sevenths. 7 sevenths minus 3 sevenths is 4 sevenths. The answer is 1 and 4 sevenths.", do=[MATH(f"{M(1, 7, 7)} − {F(3, 7)}", x=80, y=190), B(f"= {M(1, 4, 7)}", x=80, y=300, color=GREEN, at=4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: use improper fractions, or regrouping.", do=[T("• Improper fractions or **regrouping**", x=80, y=170)]),
        dict(say="Find a common denominator first.", do=[T("• Common denominator first", x=80, y=250)]),
        dict(say="Exchange 1 whole when the first fraction is smaller.", do=[T("• Exchange 1 whole when the first fraction is smaller", x=80, y=330)]),
        dict(say="Estimate, and check by adding back.", do=[T("• Estimate; check by adding back", x=80, y=410)]),
    ]),
]

VIDEOS["7.4"] = [
    dict(kind="hook", title="Baking for a crowd", steps=[
        dict(say="A recipe needs 2 and 3 quarters cups of flour. You are making it 6 times for a school fair.", do=[E("🧁", 90, 170, 100), MATH(f"6 × {M(2, 3, 4)} cups", x=230, y=180)]),
        PAUSE("7.4-k1", "How many cups do you need? Pause the video and work it out.", "6 × 2 3/4 = ?"),
    ]),
    dict(kind="hook", title="Split it up", steps=[
        dict(say="Split 2 and 3 quarters into its parts: 2, and 3 quarters. 6 times 2 is 12. 6 times 3 quarters is 18 quarters, which is 4 and a half.",
             do=[TBL(["Part", "Working"], [["6 × 2", "12"], ["6 × 3/4", "18/4 = 4 1/2"], ["total", "12 + 4 1/2 = 16 1/2"]], y=170), ROW(0, 1.5), ROW(1, 4)]),
        dict(say="Add them: 16 and a half cups.", do=[ROW(2, 0.3)]),
    ]),
    dict(kind="recall", title="Integer times a fraction", steps=[
        dict(say="Remember: 6 times 3 quarters is 18 quarters. 18 quarters is 4 and 2 quarters, which is 4 and a half.", do=[MATH(f"6 × {F(3, 4)} = {F(18, 4)} = {M(4, 1, 2)}", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Partitioning", steps=[
        dict(say="Method 1 is partitioning. Multiply the whole number part, then the fraction part, and add.", do=[B("n × a b/c = n × a + n × b/c", x=80, y=170, color=BLUE)]),
        dict(say="Estimate first. 6 times 3 is 18. The answer should be a bit less than 18, because 2 and 3 quarters is less than 3.", do=[T("estimate: 6 × 3 = **18** (a bit more than the answer)", x=80, y=270)]),
        PAUSE("7.4-k2", "Your turn. Work out 2 times 1 and 1 third. Pause the video and try it.", "Work out 2 × 1 1/3."),
    ]),
    dict(kind="idea", title="Check: 2 × 1 1/3", steps=[
        dict(say="2 times 1 is 2. 2 times 1 third is 2 thirds. The answer is 2 and 2 thirds.", do=[MATH(f"2 + {F(2, 3)} = {M(2, 2, 3)}", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Improper fractions", steps=[
        dict(say="Method 2: change the mixed number to an improper fraction. 6 times 2 and 3 quarters is 6 times 11 quarters.", do=[MATH(f"6 × {F(11, 4)}", x=80, y=170)]),
        dict(say="Cancel before you multiply. 6 and 4 share a factor of 2. That gives 3 times 11 halves, which is 33 halves, or 16 and a half.",
             do=[MATH(f"= 3 × {F(11, 2)} = {F(33, 2)} = {M(16, 1, 2)}", x=80, y=280, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I multiply by a mixed number?", steps=[
        dict(say="Here is the method. Step 1: estimate, by rounding the mixed number.", do=[T("1. **Estimate** by rounding", x=80, y=170)]),
        dict(say="Step 2: partition. Multiply the whole part, then the fraction part.", do=[T("2. **Partition**: whole part + fraction part", x=80, y=260)]),
        dict(say="Step 3: or change to an improper fraction, cancel, and multiply.", do=[T("3. Or **improper fraction**, cancel, multiply", x=80, y=350)]),
        dict(say="Step 4: give the answer as a mixed number in its simplest form, and compare it with your estimate.", do=[T("4. Mixed number, simplest form; compare with the estimate", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Partitioning", steps=[
        dict(say="Work out 8 times 4 and 3 tenths. 8 times 4 is 32. 8 times 3 tenths is 24 tenths, which is 2 and 2 fifths.", do=[MATH("8 × 4 = 32", x=80, y=170), MATH(f"8 × {F(3, 10)} = {F(24, 10)} = {M(2, 2, 5)}", x=80, y=260, at=3)]),
        dict(say="Add them: 34 and 2 fifths.", do=[B(f"{M(34, 2, 5)}", x=80, y=380, color=GREEN)]),
        PAUSE("7.4-k3", "Your turn. Work out 4 times 2 and 5 eighths. Pause and work it out.", "Work out 4 × 2 5/8."),
    ]),
    dict(kind="example", title="Check: 4 × 2 5/8", steps=[
        dict(say="4 times 2 is 8. 4 times 5 eighths is 20 eighths, which is 2 and a half. 8 plus 2 and a half is 10 and a half.", do=[MATH(f"8 + {F(20, 8)} = 8 + {M(2, 1, 2)}", x=80, y=190), B(f"= {M(10, 1, 2)}", x=80, y=300, color=GREEN, at=6)]),
    ]),
    dict(kind="example", title="A train journey", steps=[
        dict(say="A train journey takes 1 and 2 thirds hours. How long do 5 journeys take? 5 times 1 is 5. 5 times 2 thirds is 10 thirds, which is 3 and 1 third.",
             do=[E("🚆", 90, 160, 90), MATH(f"5 × {M(1, 2, 3)} = 5 + {M(3, 1, 3)}", x=230, y=180)]),
        dict(say="That is 8 and 1 third hours. 1 third of an hour is 20 minutes, so it is 8 hours 20 minutes.", do=[B(f"{M(8, 1, 3)} hours = 8 h 20 min", x=230, y=300, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ivy works out 3 times 2 and 1 quarter. Which line is wrong?", do=LINES("Ivy", "3 × 2 1/4", ["3 × 2 = 6", "Answer: 6 1/4"])),
        dict(say="Line 2 is wrong. She forgot to multiply the fraction too. 3 times 1 quarter is 3 quarters.", do=[dict(a="cross", id="l2")]),
        dict(say="The answer is 6 and 3 quarters.", do=[B(f"6 + {F(3, 4)} = {M(6, 3, 4)}", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Paint", steps=[
        dict(say="One coat of paint for a fence needs 1 and 3 quarters litres. The fence needs 3 coats.", do=[E("🎨", 90, 170, 100), MATH(f"3 × {M(1, 3, 4)}", x=230, y=180)]),
        dict(say="3 times 1 is 3, and 3 times 3 quarters is 9 quarters, which is 2 and 1 quarter. Altogether, 5 and 1 quarter litres. So two 3 litre tins are needed.",
             do=[MATH(f"3 + {M(2, 1, 4)} = {M(5, 1, 4)} litres", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.4-k4", "One last question. Work out 7 times 3 and 9 tenths, to the nearest whole number. Pause the video and answer.", "7 × 3 9/10, to the nearest whole?"),
        dict(say="7 times 3 is 21. 7 times 9 tenths is 6.3. 21 plus 6.3 is 27.3, which is 27 to the nearest whole.", do=[MATH("21 + 6.3 = 27.3", x=80, y=190), B("≈ 27", x=80, y=300, color=GREEN, at=4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: partition. Multiply the whole part and the fraction part, then add.", do=[T("• **Partition**: whole part + fraction part", x=80, y=170)]),
        dict(say="Or use an improper fraction, and cancel first.", do=[T("• Or improper fraction; cancel first", x=80, y=250)]),
        dict(say="Always estimate first.", do=[T("• Estimate first", x=80, y=330)]),
        dict(say="Give answers as mixed numbers in their simplest form.", do=[T("• Answer as a mixed number, simplest form", x=80, y=410)]),
    ]),
]

VIDEOS["7.5"] = [
    dict(kind="hook", title="Pizza party", steps=[
        dict(say="A party has 6 pizzas. Each guest gets 3 eighths of a pizza.", do=[E("🍕", 90, 170, 100), MATH(f"6 ÷ {F(3, 8)}", x=230, y=180)]),
        PAUSE("7.5-k1", "How many guests can be served? Pause the video and work it out.", "6 ÷ 3/8 = ?"),
    ]),
    dict(kind="hook", title="Count the eighths", steps=[
        dict(say="Cut every pizza into 8 slices. 6 pizzas make 48 eighths.", do=[T(BAR(8, 8, "#F4B740"), x=80, y=170), MATH("6 × 8 = 48 eighths", x=80, y=250)]),
        dict(say="Each guest takes 3 slices. 48 divided by 3 is 16. So 16 guests can be served.", do=[MATH("48 ÷ 3 = 16", x=80, y=340), B("16 guests", x=80, y=430, color=GREEN, at=3)]),
    ]),
    dict(kind="recall", title="How many halves?", steps=[
        dict(say="Remember: 3 divided by a half asks how many halves are in 3. There are 2 in each whole, so 6.", do=[MATH(f"3 ÷ {F(1, 2)} = 6", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Dividing by a unit fraction", steps=[
        dict(say="Dividing by a unit fraction, 1 over d, is the same as multiplying by d. There are d pieces in each whole. 6 divided by 1 eighth is 48.",
             do=[B(f"n ÷ {F(1, 'd')} = n × d", x=80, y=170, color=BLUE), MATH(f"6 ÷ {F(1, 8)} = 48", x=80, y=290)]),
        PAUSE("7.5-k2", "Your turn. Work out 4 divided by 1 third. Pause the video and try it.", "Work out 4 ÷ 1/3."),
    ]),
    dict(kind="idea", title="Check: 4 ÷ 1/3", steps=[
        dict(say="There are 3 thirds in each whole, so 4 times 3 is 12.", do=[MATH(f"4 ÷ {F(1, 3)} = 4 × 3 = 12", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Any fraction: the reciprocal", steps=[
        dict(say="For 6 divided by 3 eighths, we found 48 eighths, then divided by 3. That is the same as multiplying by 8 thirds. 8 thirds is the reciprocal of 3 eighths. You turn the fraction upside down.",
             do=[MATH(f"6 ÷ {F(3, 8)} = 6 × {F(8, 3)} = {F(48, 3)} = 16", x=80, y=170), T("**reciprocal**: turn the fraction upside down", x=80, y=300, at=6)]),
        dict(say="Dividing by a fraction less than 1 always gives a bigger answer.", do=[T("÷ a fraction less than 1 → **bigger** answer", x=80, y=380, color=RED)]),
    ]),
    dict(kind="method", title="How do I divide by a fraction?", steps=[
        dict(say="Here is the method. Step 1: write the reciprocal of the fraction. Turn it upside down.", do=[T("1. Write the **reciprocal** (upside down)", x=80, y=170)]),
        dict(say="Step 2: multiply the whole number by the reciprocal.", do=[T("2. **Multiply** by the reciprocal", x=80, y=260)]),
        dict(say="Step 3: simplify, and write it as a mixed number if needed.", do=[T("3. Simplify; mixed number if needed", x=80, y=350)]),
        dict(say="Step 4: check. Dividing by a proper fraction gives a bigger answer.", do=[T("4. **Check**: the answer is **bigger**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A non-unit fraction", steps=[
        dict(say="Work out 10 divided by 4 sevenths. Multiply by the reciprocal, 7 quarters. 10 times 7 quarters is 70 quarters, which is 17 and a half.",
             do=[MATH(f"10 ÷ {F(4, 7)} = 10 × {F(7, 4)}", x=80, y=170), B(f"= {F(70, 4)} = {M(17, 1, 2)}", x=80, y=290, color=GREEN, at=6)]),
        PAUSE("7.5-k3", "Your turn. Work out 6 divided by 2 thirds. Pause and work it out.", "Work out 6 ÷ 2/3."),
    ]),
    dict(kind="example", title="Check: 6 ÷ 2/3", steps=[
        dict(say="The reciprocal of 2 thirds is 3 halves. 6 times 3 halves is 18 halves, which is 9.", do=[MATH(f"6 × {F(3, 2)} = {F(18, 2)} = 9", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Full bottles", steps=[
        dict(say="A 5 litre tub fills bottles that hold 2 thirds of a litre. How many full bottles? 5 times 3 halves is 15 halves, which is 7 and a half.",
             do=[E("🍶", 90, 160, 90), MATH(f"5 ÷ {F(2, 3)} = 5 × {F(3, 2)} = {M(7, 1, 2)}", x=230, y=180)]),
        dict(say="The half bottle is not full. So the answer is 7 full bottles.", do=[B("7 full bottles", x=230, y=300, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Sam works out 8 divided by 2 fifths. Which line goes wrong first?", do=LINES("Sam", "8 ÷ 2/5", ["Reciprocal of 8 is 1/8", "1/8 × 2/5 = 1/20"])),
        dict(say="Line 1 is wrong. You turn over the fraction you are dividing by, which is 2 fifths. Not the 8.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="8 times 5 halves is 40 halves, which is 20.", do=[B(f"8 × {F(5, 2)} = 20", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Cutting pipes", steps=[
        dict(say="A plumber has a 9 metre pipe and needs pieces 3 quarters of a metre long.", do=[E("🔧", 90, 170, 100), MATH(f"9 ÷ {F(3, 4)}", x=230, y=180)]),
        dict(say="9 times 4 thirds is 36 thirds, which is 12. She can cut 12 pieces with nothing wasted.", do=[MATH(f"9 × {F(4, 3)} = 12", x=230, y=290, color=BLUE), B("12 pieces", x=230, y=390, color=GREEN, at=4)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.5-k4", "One last question. What is the reciprocal of 7 ninths? Pause the video and choose.", "The reciprocal of 7/9 is …"),
        dict(say="Turn it upside down. The reciprocal of 7 ninths is 9 sevenths.", do=[B(f"{F(9, 7)}", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: dividing by 1 over d is the same as multiplying by d.", do=[T(f"• n ÷ 1/d = n × d", x=80, y=170)]),
        dict(say="Dividing by a fraction is the same as multiplying by its reciprocal.", do=[T("• ÷ a fraction = × its **reciprocal**", x=80, y=250)]),
        dict(say="The answer is bigger than the number you started with.", do=[T("• The answer is **bigger**", x=80, y=330)]),
        dict(say="Think about remainders in real problems.", do=[T("• Think about remainders in context", x=80, y=410)]),
    ]),
]

VIDEOS["7.6"] = [
    dict(kind="hook", title="Mental maths race", steps=[
        dict(say="A quiz question: 3 quarters times 17, plus 3 quarters times 3. You have 10 seconds, and no paper.", do=[E("⏱️", 90, 170, 100), MATH(f"{F(3, 4)} × 17 + {F(3, 4)} × 3", x=230, y=180)]),
        PAUSE("7.6-k1", "What is the answer? Pause the video and work it out.", "3/4 × 17 + 3/4 × 3 = ?"),
    ]),
    dict(kind="hook", title="Take out 3 quarters", steps=[
        dict(say="Both parts have 3 quarters. So take it out: 3 quarters times, bracket, 17 plus 3. That is 3 quarters of 20, which is 15.",
             do=[MATH(f"= {F(3, 4)} × (17 + 3) = {F(3, 4)} × 20", x=80, y=190), B("= 15", x=80, y=300, color=GREEN, at=6)]),
    ]),
    dict(kind="recall", title="The distributive law", steps=[
        dict(say="Remember: A times B, plus A times C, equals A times, bracket, B plus C. For example, 7 times 23, plus 7 times 77, is 7 times 100, which is 700.",
             do=[MATH("a × b + a × c = a × (b + c)", x=80, y=170), MATH("7 × 23 + 7 × 77 = 7 × 100 = 700", x=80, y=270, at=6)]),
    ]),
    dict(kind="idea", title="Strategies", steps=[
        dict(say="Here are some ways to make fraction calculations easier. Take out a common factor, like the quiz question.",
             do=[TBL(["Strategy", "Example"], [["take out a common factor", "3/4 × 17 + 3/4 × 3 = 3/4 × 20 = 15"], ["cancel before multiplying", "14/15 × 25/28 = 1/3 × 5/2 = 5/6"], ["whole minus a part", "7/8 of 48 = 48 − 6 = 42"]], y=170), ROW(0, 0.3)]),
        dict(say="Cancel before multiplying. 14 and 28 share 14. 25 and 15 share 5. That leaves 1 third times 5 halves, which is 5 sixths.", do=[ROW(1, 0.3)]),
        dict(say="And use whole minus a part. 7 eighths of 48 is the whole 48, minus 1 eighth of 48. That is 48 minus 6, which is 42.", do=[ROW(2, 0.3)]),
        PAUSE("7.6-k2", "Your turn. Find 9 tenths of 250. Pause the video and try it.", "Find 9/10 of 250."),
    ]),
    dict(kind="idea", title="Check: 9/10 of 250", steps=[
        dict(say="1 tenth of 250 is 25. So 9 tenths is 250 minus 25, which is 225.", do=[MATH("250 − 25 = 225", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Order of operations", steps=[
        dict(say="The order of operations still applies. Multiply before you add. 1 half plus 1 third times 3 quarters is 1 half plus 1 quarter, which is 3 quarters.",
             do=[MATH(f"{F(1, 2)} + {F(1, 3)} × {F(3, 4)} = {F(1, 2)} + {F(1, 4)} = {F(3, 4)}", x=80, y=180)]),
        dict(say="But brackets come first. 1 half plus 1 third, in a bracket, times 6, is 5 sixths times 6, which is 5.", do=[MATH(f"({F(1, 2)} + {F(1, 3)}) × 6 = {F(5, 6)} × 6 = 5", x=80, y=320)]),
    ]),
    dict(kind="method", title="How do I make it easier?", steps=[
        dict(say="Here is the method. Step 1: look for a common factor to take out.", do=[T("1. A **common factor** to take out?", x=80, y=170)]),
        dict(say="Step 2: cancel before you multiply.", do=[T("2. **Cancel** before multiplying", x=80, y=260)]),
        dict(say="Step 3: re-order the numbers, or use whole minus a part.", do=[T("3. Re-order, or **whole minus a part**", x=80, y=350)]),
        dict(say="Step 4: follow the order of operations, and check with an estimate.", do=[T("4. Order of operations; check with an estimate", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Cancelling", steps=[
        dict(say="Work out 18 thirty-fifths times 21 twenty-fourths. 18 and 24 share 6, leaving 3 and 4. 21 and 35 share 7, leaving 3 and 5.",
             do=[MATH(f"{F(18, 35)} × {F(21, 24)}", x=80, y=170), MATH(f"= {F(3, 5)} × {F(3, 4)}", x=80, y=290, at=5)]),
        dict(say="3 fifths times 3 quarters is 9 twentieths.", do=[B(f"= {F(9, 20)}", x=80, y=410, color=GREEN)]),
        PAUSE("7.6-k3", "Your turn. Work out 10 twenty-firsts times 14 fifteenths. Pause and work it out.", "Work out 10/21 × 14/15."),
    ]),
    dict(kind="example", title="Check: 10/21 × 14/15", steps=[
        dict(say="10 and 15 share 5, leaving 2 and 3. 14 and 21 share 7, leaving 2 and 3. So it is 2 thirds times 2 thirds, which is 4 ninths.",
             do=[MATH(f"{F(2, 3)} × {F(2, 3)} = {F(4, 9)}", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Mixed numbers", steps=[
        dict(say="Work out 4 times 2 and 3 eighths, plus 4 times 1 and 5 eighths. Take out the 4: 4 times, bracket, 2 and 3 eighths plus 1 and 5 eighths.",
             do=[MATH(f"4 × {M(2, 3, 8)} + 4 × {M(1, 5, 8)}", x=80, y=170), MATH(f"= 4 × ({M(2, 3, 8)} + {M(1, 5, 8)})", x=80, y=290, at=6)]),
        dict(say="The bracket is exactly 4. And 4 times 4 is 16.", do=[B("= 4 × 4 = 16", x=80, y=410, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Max works out 1 third plus 2 thirds times 1 half. Which line goes wrong first?", do=LINES("Max", "1/3 + 2/3 × 1/2", ["1/3 + 2/3 = 1", "1 × 1/2 = 1/2"])),
        dict(say="Line 1 is wrong. Multiplication comes before addition. 2 thirds times 1 half is 1 third.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="Then 1 third plus 1 third is 2 thirds.", do=[B(f"{F(1, 3)} + {F(1, 3)} = {F(2, 3)}", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Sale prices", steps=[
        dict(say="A shop has a sale: everything is 1 quarter off. So you pay 3 quarters of the price.", do=[E("🛍️", 90, 170, 100), T("**¼ off** → pay **¾** of the price", x=230, y=200)]),
        dict(say="You buy a 36 dollar shirt and a 44 dollar pair of jeans. Instead of two calculations, add first: 3 quarters of 80 is 60 dollars.",
             do=[MATH(f"{F(3, 4)} × 36 + {F(3, 4)} × 44 = {F(3, 4)} × 80 = $60", x=230, y=320, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.6-k4", "One last question. What is 1 half minus 1 quarter times 2? Pause the video and answer.", "1/2 − 1/4 × 2 = ?"),
        dict(say="Multiply first. 1 quarter times 2 is 1 half. Then 1 half minus 1 half is 0.", do=[MATH(f"{F(1, 4)} × 2 = {F(1, 2)}", x=80, y=190), B(f"{F(1, 2)} − {F(1, 2)} = 0", x=80, y=310, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: take out common factors, using the distributive law.", do=[T("• Take out **common factors**", x=80, y=170)]),
        dict(say="Cancel before multiplying.", do=[T("• **Cancel** before multiplying", x=80, y=250)]),
        dict(say="Use whole minus a part, and re-ordering.", do=[T("• Whole minus a part; re-order", x=80, y=330)]),
        dict(say="The order of operations still applies.", do=[T("• The order of operations still applies", x=80, y=410)]),
    ]),
]
