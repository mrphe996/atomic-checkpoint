# -*- coding: utf-8 -*-
"""Stage 7 · Unit 4 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, J, TEST, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG

TBL = lambda head, rows, x=80, y=250, id="t": dict(a="table", id=id, head=head, rows=rows, x=x, y=y)
ROW = lambda i, at=0.3, id="t": dict(a="row", id=id, i=i, at=at)
COL = lambda rows, x=80, y=250, id="t": TBL([""] + list(rows[0]), [[lab] + list(r) for lab, r in rows[1:]], x, y, id)   # column working: first row is the top number

VIDEOS = {}

VIDEOS["4.1"] = [
    dict(kind="hook", title="Photo finish", steps=[
        dict(say="Four swimmers finish a race. Their times are 58.4 seconds, 58.39 seconds, 58.04 seconds, and 58.415 seconds.",
             do=[E("🏊", 90, 160, 90), T("**58.4 s**", x=230, y=185), T("**58.39 s**", x=430, y=185, at=2.4), T("**58.04 s**", x=650, y=185, at=4.6), T("**58.415 s**", x=870, y=185, at=6.8)]),
        PAUSE("4.1-k1", "The smallest time wins. Which time won? Pause the video and decide.", "Four times: 58.4 s, 58.39 s, 58.04 s and 58.415 s. Which time won (the smallest)?"),
    ]),
    dict(kind="hook", title="Who won?", steps=[
        dict(say="Every time starts with 58, so look at the tenths. 58.04 has 0 tenths. The others have 3 or 4 tenths.",
             do=[TBL(["Time", "Ones", ".", "tenths", "hundredths", "thousandths"], [["58.4", "58", ".", "4", "", ""], ["58.39", "58", ".", "3", "9", ""], ["58.04", "58", ".", "**0**", "4", ""], ["58.415", "58", ".", "4", "1", "5"]], y=160),
                 ROW(0, 0.2), ROW(1, 0.5), ROW(2, 0.8), ROW(3, 1.1)]),
        dict(say="So 58.04 seconds is the smallest time. That swimmer won.", do=[B("58.04 s wins", x=80, y=480, color=GREEN), E("🥇", 420, 466, 60, at=1)]),
    ]),
    dict(kind="recall", title="Comparison signs", steps=[
        dict(say="Remember these signs. Less than, and greater than.", do=[B("<", x=80, y=160, color=BLUE), T("is less than", x=160, y=178), B(">", x=480, y=160, color=RED, at=1.4), T("is greater than", x=560, y=178, at=1.4)]),
        dict(say="Equal to, and not equal to.", do=[B("=", x=80, y=280, color=GREEN), T("is equal to", x=160, y=298), B("≠", x=480, y=280, at=1.2), T("is not equal to", x=560, y=298, at=1.2)]),
        dict(say="0.5 is equal to 0.50. A zero at the end of a decimal does not change its value.", do=[MATH("0.5 = 0.50", x=80, y=420, color=GREEN)]),
    ]),
    dict(kind="idea", title="Compare place by place", steps=[
        dict(say="To compare decimals, start with the whole-number parts. If they are the same, compare the tenths.", do=[T("whole numbers → **tenths** → **hundredths** → **thousandths**", x=80, y=160)]),
        dict(say="Compare 58.4 and 58.39. The whole numbers match. The tenths are 4 and 3. 4 is bigger, so 58.4 is greater than 58.39.",
             do=[MATH("58.4", x=110, y=270), MATH("58.39", x=110, y=350), T("tenths: **4** and **3**", x=420, y=310, at=4.4), B("58.4 > 58.39", x=80, y=460, color=GREEN, at=7.6)]),
        dict(say="You only move on to the hundredths when the tenths are the same.", do=[T("Same tenths? Then compare hundredths.", x=640, y=478, color=GREY)]),
    ]),
    dict(kind="idea", title="Fill the gaps with zeros", steps=[
        dict(say="Here is a useful trick. Write zeros at the end, so that every number has the same number of decimal places.",
             do=[MATH("58.400", x=110, y=170), MATH("58.390", x=110, y=250, at=0.4), MATH("58.040", x=110, y=330, at=0.8), MATH("58.415", x=110, y=410, at=1.2)]),
        dict(say="Now compare them like whole numbers: 400, 390, 40 and 415.", do=[T("400,  390,  040,  415", x=480, y=290, color=BLUE)]),
        dict(say="In order, smallest first: 58.04, 58.39, 58.4, 58.415.", do=[B("58.04 < 58.39 < 58.4 < 58.415", x=80, y=510, color=GREEN)]),
        dict(say="Be careful. A longer number is not always bigger. 0.7 is greater than 0.6999.", do=[MATH("0.7 > 0.6999", x=760, y=180, color=RED)]),
        PAUSE("4.1-k2", "Your turn. Which of these numbers is the largest? Pause the video and choose.", "Which is the largest? Compare the tenths first."),
    ]),
    dict(kind="idea", title="Check: the largest", steps=[
        dict(say="The answer is 0.6. It has 6 tenths. The other numbers have fewer tenths, even though they have more digits.",
             do=[B("0.6", x=80, y=180, color=GREEN), T("= 0.600: **6 tenths**", x=260, y=198, at=1.6), T("More digits does **not** mean bigger", x=80, y=320, color=RED, at=4.4)]),
    ]),
    dict(kind="method", title="How do I order decimals?", steps=[
        dict(say="Here is the method. Step 1: line the numbers up by the decimal point.", do=[T("1. **Line up** the decimal points", x=80, y=170)]),
        dict(say="Step 2: fill empty places with zeros, so they all have the same number of decimal places.", do=[T("2. Fill the gaps with **zeros**", x=80, y=260)]),
        dict(say="Step 3: compare the whole numbers, then the tenths, then the hundredths, and so on.", do=[T("3. Compare whole numbers, tenths, hundredths…", x=80, y=350)]),
        dict(say="Step 4: write the original numbers in order.", do=[T("4. Write the **original** numbers in order", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Ordering four decimals", steps=[
        dict(say="Write these in order, smallest first: 6.2, 6.05, 6.199 and 6.21.", do=[B("6.2,  6.05,  6.199,  6.21", x=80, y=150)]),
        dict(say="Give them all 3 decimal places.", do=[MATH("6.200", x=110, y=260), MATH("6.050", x=330, y=260, at=0.5), MATH("6.199", x=550, y=260, at=1), MATH("6.210", x=770, y=260, at=1.5)]),
        dict(say="Compare 200, 50, 199 and 210. The smallest is 50, then 199, then 200, then 210.", do=[T("050 < 199 < 200 < 210", x=110, y=360, color=BLUE)]),
        dict(say="So the order is 6.05, 6.199, 6.2, 6.21.", do=[B("6.05,  6.199,  6.2,  6.21", x=80, y=460, color=GREEN)]),
    ]),
    dict(kind="example", title="Negative decimals", steps=[
        dict(say="Which is smaller: negative 1.4, or negative 1.35?", do=[B("−1.4  or  −1.35 ?", x=80, y=150)]),
        dict(say="Without the signs, 1.40 is bigger than 1.35.", do=[MATH("1.40 > 1.35", x=80, y=260)]),
        dict(say="So negative 1.4 is further from zero. It is further left on the number line, which makes it smaller.",
             do=[FIG(520, 250, 640, 0, kind="numline", min=-1.5, max=-1.2, minor=0, ticks=[[-1.4, "−1.4"], [-1.35, "−1.35"], [-1.2, "−1.2"]], mark=-1.4)]),
        dict(say="Negative 1.4 is less than negative 1.35.", do=[B("−1.4 < −1.35", x=80, y=380, color=GREEN)]),
        PAUSE("4.1-k3", "Your turn. Which is smaller: negative 0.3, or negative 0.25? Pause and decide.", "Which is smaller: −0.3 or −0.25?"),
    ]),
    dict(kind="example", title="Check: −0.3 or −0.25", steps=[
        dict(say="0.30 is bigger than 0.25. So negative 0.3 is further from zero, and it is the smaller number.",
             do=[MATH("0.30 > 0.25", x=80, y=190), B("−0.3 < −0.25", x=80, y=300, color=GREEN, at=3.6)]),
    ]),
    dict(kind="example", title="Equal or not equal?", steps=[
        dict(say="Is 4.30 equal to 4.3? Yes. 4.30 has 3 tenths and 0 hundredths. That is the same as 4.3.", do=[B("4.30 = 4.3", x=80, y=170, color=GREEN)]),
        dict(say="Is 0.09 equal to 0.9? No. 0.09 is 9 hundredths, but 0.9 is 9 tenths.", do=[B("0.09 ≠ 0.9", x=80, y=320, color=RED), T("9 hundredths  ≠  9 tenths", x=420, y=338, color=GREY, at=3)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ivy puts 0.8, 0.75 and 0.125 in order, smallest first. Which line goes wrong first?",
             do=LINES("Ivy", "0.8, 0.75, 0.125 in order", ["0.125 has the most digits, so it is biggest", "Order: 0.8, 0.75, 0.125"])),
        dict(say="Line 1 is wrong. The number of digits does not tell you the size. Compare the tenths: 8, 7 and 1.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6), T("tenths: 8, 7, 1", x=110, y=400, color=BLUE, at=4.4)]),
        dict(say="The correct order, smallest first, is 0.125, 0.75, 0.8.", do=[B("0.125,  0.75,  0.8", x=110, y=490, color=GREEN)]),
    ]),
    dict(kind="life", title="One hundredth of a second", steps=[
        dict(say="Ordering decimals decides who gets the gold medal. At the 2008 Olympic Games, Michael Phelps won the 100 metres butterfly in 50.58 seconds.",
             do=[E("🏊", 90, 170, 100), T("Beijing 2008, 100 m butterfly: **50.58 s**", x=230, y=200)]),
        dict(say="The swimmer in second place took 50.59 seconds.", do=[T("second place: **50.59 s**", x=230, y=300)]),
        dict(say="The tenths are the same. Only the hundredths are different. He won by just one hundredth of a second!",
             do=[B("50.58 < 50.59", x=230, y=400, color=GREEN), T("a gap of **0.01 s**", x=640, y=418, at=3), E("🥇", 1000, 380, 100, at=3.6)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.1-k4", "One last question. How many of these numbers are greater than 1.1? 1.5, 1.05, 1.505 and 1.055. Pause the video and count.", "How many of 1.5, 1.05, 1.505, 1.055 are greater than 1.1?"),
        dict(say="Compare the tenths with 1.1. 1.5 and 1.505 have 5 tenths, so they are greater. 1.05 and 1.055 have 0 tenths, so they are smaller. The answer is 2.",
             do=[MATH("1.5 ✓", x=110, y=190, color=GREEN), MATH("1.505 ✓", x=330, y=190, color=GREEN, at=0.4), MATH("1.05 ✗", x=110, y=290, color=RED, at=5), MATH("1.055 ✗", x=330, y=290, color=RED, at=5.4), B("2 numbers", x=80, y=410, color=GREEN, at=9)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: compare the whole numbers, then the tenths, then the hundredths, in turn.", do=[T("• Compare whole numbers, tenths, hundredths… in turn", x=80, y=170)]),
        dict(say="Add zeros at the end, so the numbers have the same number of decimal places.", do=[T("• Add zeros so the lengths match", x=80, y=250)]),
        dict(say="More digits does not mean bigger.", do=[T("• More digits does **not** mean bigger", x=80, y=330)]),
        dict(say="With negative numbers, the one further from zero is smaller.", do=[T("• Negatives: further from zero = smaller", x=80, y=410)]),
    ]),
]

VIDEOS["4.2"] = [
    dict(kind="hook", title="Shopping receipt", steps=[
        dict(say="Lena buys a book for 7 dollars 85, and a pen for 2 dollars 40. She pays with a 20 dollar note.",
             do=[E("📕", 90, 160, 90), T("**$7.85**", x=200, y=190), E("🖊️", 420, 160, 90, at=2.4), T("**$2.40**", x=530, y=190, at=2.4), E("💵", 760, 160, 90, at=4.6), T("pays **$20**", x=870, y=190, at=4.6)]),
        PAUSE("4.2-k1", "How much change should she get? Pause the video and work it out.", "How much change from $20 for $7.85 + $2.40?"),
    ]),
    dict(kind="hook", title="Add, then subtract", steps=[
        dict(say="First add the prices. 7.85 plus 2.40 is 10.25.", do=[MATH("7.85 + 2.40 = 10.25", x=80, y=180)]),
        dict(say="Then take that away from 20. 20 minus 10.25 is 9.75. Lena gets 9 dollars 75 change.", do=[MATH("20.00 − 10.25 = 9.75", x=80, y=290, color=BLUE), B("$9.75 change", x=80, y=410, color=GREEN, at=4.6)]),
    ]),
    dict(kind="recall", title="Column addition", steps=[
        dict(say="Remember column addition. Line up ones under ones, and tens under tens. 476 plus 58.",
             do=[COL([("H", "T", "O"), ("", ("4", "7", "6")), ("+", ("", "5", "8")), ("=", ("5", "3", "4"))], y=170), ROW(0, 3), ROW(1, 4)]),
        dict(say="Carry when a column adds up to 10 or more. The answer is 534.", do=[ROW(2, 2)]),
    ]),
    dict(kind="idea", title="Line up the decimal points", steps=[
        dict(say="With decimals, the rule is: line up the decimal points. Then every digit sits under a digit with the same place value.",
             do=[T("**Line up the decimal points**", x=80, y=150, color=RED)]),
        dict(say="7.85 plus 2.4. Write 2.4 as 2.40, so there are no gaps.",
             do=[COL([("T", "O", ".", "t", "h"), ("", ("", "7", ".", "8", "5")), ("+", ("", "2", ".", "4", "**0**")), ("=", ("1", "0", ".", "2", "5"))], y=240), ROW(0, 0.3), ROW(1, 1.4)]),
        dict(say="Add from the right. 5 plus 0 is 5. 8 plus 4 is 12: write 2, carry 1. 7 plus 2 plus 1 is 10.", do=[ROW(2, 5)]),
        dict(say="The decimal point in the answer goes straight under the other points. The total is 10.25.", do=[B("10.25", x=640, y=330, color=GREEN)]),
        PAUSE("4.2-k2", "Your turn. Work out 0.9 plus 0.35. Pause the video and try it.", "Work out 0.9 + 0.35."),
    ]),
    dict(kind="idea", title="Check: 0.9 + 0.35", steps=[
        dict(say="Write 0.9 as 0.90. 90 hundredths plus 35 hundredths is 125 hundredths. The answer is 1.25.",
             do=[COL([("O", ".", "t", "h"), ("", ("0", ".", "9", "**0**")), ("+", ("0", ".", "3", "5")), ("=", ("1", ".", "2", "5"))], y=170), ROW(0, 0.2), ROW(1, 1), ROW(2, 4), B("1.25", x=560, y=260, color=GREEN, at=6.4)]),
    ]),
    dict(kind="idea", title="Subtracting", steps=[
        dict(say="Subtracting works the same way. 20 minus 10.25. Write 20 as 20.00.",
             do=[COL([("T", "O", ".", "t", "h"), ("", ("2", "0", ".", "**0**", "**0**")), ("−", ("1", "0", ".", "2", "5")), ("=", ("", "9", ".", "7", "5"))], y=160), ROW(0, 0.3), ROW(1, 1.4)]),
        dict(say="Subtract column by column from the right, exchanging when you need to. The answer is 9.75.", do=[ROW(2, 3)]),
        dict(say="Check by adding back. 9.75 plus 10.25 is 20.", do=[T("check: 9.75 + 10.25 = 20 ✓", x=640, y=260, color=GREY)]),
        dict(say="With negative numbers, use the integer rules. 4.2 minus negative 1.3 is 4.2 plus 1.3, which is 5.5.", do=[MATH("4.2 − (−1.3) = 4.2 + 1.3 = 5.5", x=80, y=500, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I add or subtract decimals?", steps=[
        dict(say="Here is the method. Step 1: estimate first, by rounding.", do=[T("1. **Estimate** first", x=80, y=170)]),
        dict(say="Step 2: write the numbers with the decimal points lined up, and fill the gaps with zeros.", do=[T("2. Line up the **points**; fill gaps with zeros", x=80, y=260)]),
        dict(say="Step 3: add or subtract column by column, from the right.", do=[T("3. Work column by column from the **right**", x=80, y=350)]),
        dict(say="Step 4: put the decimal point in the answer, under the others. Then compare with your estimate.", do=[T("4. Point under the points; compare with the estimate", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Adding three decimals", steps=[
        dict(say="Work out 4.7 plus 0.36 plus 12.05. First estimate: 5 plus 0 plus 12 is about 17.", do=[B("4.7 + 0.36 + 12.05", x=80, y=150), T("estimate: 5 + 0 + 12 = **17**", x=640, y=168, color=GREY, at=3.6)]),
        dict(say="Line up the points.",
             do=[COL([("T", "O", ".", "t", "h"), ("", ("", "4", ".", "7", "0")), ("", ("", "0", ".", "3", "6")), ("+", ("1", "2", ".", "0", "5")), ("=", ("1", "7", ".", "1", "1"))], y=250), ROW(0, 0.2), ROW(1, 0.5), ROW(2, 0.8)]),
        dict(say="Hundredths: 0 plus 6 plus 5 is 11. Write 1, carry 1. Tenths: 7 plus 3 plus 0 plus 1 is 11. Write 1, carry 1. The answer is 17.11.", do=[ROW(3, 6), B("17.11", x=640, y=380, color=GREEN, at=9)]),
    ]),
    dict(kind="example", title="Subtracting with zeros", steps=[
        dict(say="Work out 8 minus 2.374. Write 8 with 3 decimal places.",
             do=[COL([("O", ".", "t", "h", "th"), ("", ("8", ".", "**0**", "**0**", "**0**")), ("−", ("2", ".", "3", "7", "4")), ("=", ("5", ".", "6", "2", "6"))], y=170), ROW(0, 1.6), ROW(1, 2.6)]),
        dict(say="Exchange: 8 ones become 7 ones, 9 tenths, 9 hundredths and 10 thousandths.", do=[T("8.000 = 7 ones, 9 tenths, 9 hundredths, 10 thousandths", x=560, y=200, color=GREY, w=560)]),
        dict(say="Now subtract. The answer is 5.626.", do=[ROW(2, 0.6), B("5.626", x=560, y=330, color=GREEN, at=2)]),
        PAUSE("4.2-k3", "Your turn. Work out 2.5 minus negative 0.7. Pause and work it out.", "Work out 2.5 − (−0.7)."),
    ]),
    dict(kind="example", title="Check: 2.5 − (−0.7)", steps=[
        dict(say="Subtracting a negative is the same as adding. 2.5 plus 0.7 is 3.2.", do=[MATH("2.5 − (−0.7) = 2.5 + 0.7", x=80, y=190), B("= 3.2", x=80, y=300, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Flour for a recipe", steps=[
        dict(say="A recipe needs 0.75 kilograms of flour. Ama has 2.1 kilograms. She makes the recipe twice. How much flour is left?",
             do=[E("🌾", 90, 160, 90), T("recipe: **0.75 kg**.  Ama has **2.1 kg**.  Made **twice**", x=210, y=190)]),
        dict(say="She uses 0.75 plus 0.75, which is 1.5 kilograms.", do=[MATH("0.75 + 0.75 = 1.5 kg", x=80, y=310)]),
        dict(say="2.10 minus 1.50 is 0.6. She has 0.6 kilograms left.", do=[MATH("2.10 − 1.50 = 0.60", x=80, y=410, color=BLUE), B("0.6 kg left", x=560, y=402, color=GREEN, at=3.4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Raj works out 3.6 plus 1.25 like this. He lined up the digits on the right. What went wrong?",
             do=[T("Raj's working for **3.6 + 1.25**:", x=80, y=160), COL([("", "", "", ""), ("", ("", "3", ".", "6")), ("+", ("1", ".", "2", "5")), ("=", ("1", ".", "6", "1"))], y=230), ROW(0, 0.2), ROW(1, 0.5), ROW(2, 0.8)]),
        dict(say="The 6 tenths were added to 5 hundredths. The decimal points are not in a line.", do=[E("❌", 420, 300, 70), T("the points are **not** lined up", x=520, y=320, color=RED)]),
        dict(say="Line up the points and fill in a zero. 3.60 plus 1.25 is 4.85.", do=[B("3.60 + 1.25 = 4.85", x=420, y=440, color=GREEN)]),
    ]),
    dict(kind="life", title="Body temperature", steps=[
        dict(say="Doctors add and subtract decimals every day. Normal body temperature is about 37 degrees Celsius.",
             do=[E("🌡️", 90, 170, 100), T("normal body temperature: about **37.0 °C**", x=230, y=200)]),
        dict(say="Suppose a thermometer reads 38.6 degrees. How far above normal is that?", do=[T("reading: **38.6 °C**", x=230, y=300)]),
        dict(say="38.6 minus 37.0 is 1.6. The temperature is 1.6 degrees above normal. That is a fever.", do=[MATH("38.6 − 37.0 = 1.6", x=230, y=400, color=BLUE), E("🤒", 760, 380, 90, at=3.4)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.2-k4", "One last question. What is 10 minus 0.01? Pause the video and answer.", "10 − 0.01 = ?"),
        dict(say="Write 10 as 10.00. Take away 1 hundredth. The answer is 9.99.", do=[MATH("10.00 − 0.01", x=80, y=190), B("= 9.99", x=80, y=300, color=GREEN, at=3.4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: line up the decimal points, and fill gaps with zeros.", do=[T("• Line up the **points**; fill gaps with zeros", x=80, y=170)]),
        dict(say="Add or subtract as you do with whole numbers.", do=[T("• Then add or subtract like whole numbers", x=80, y=250)]),
        dict(say="Use the integer rules for negative decimals.", do=[T("• Negative decimals: use the integer rules", x=80, y=330)]),
        dict(say="Estimate first, and check with the inverse operation.", do=[T("• Estimate first; check with the inverse", x=80, y=410)]),
    ]),
]

VIDEOS["4.3"] = [
    dict(kind="hook", title="Filling the tank", steps=[
        dict(say="Petrol costs 1 dollar 36 for each litre. A car's tank takes 42 litres.",
             do=[E("⛽", 90, 160, 100), T("**$1.36** per litre", x=230, y=190), E("🚗", 560, 160, 100, at=2.6), T("tank: **42 litres**", x=700, y=190, at=2.6)]),
        PAUSE("4.3-k1", "Estimate the cost of a full tank, by working out 40 times 1.4. Pause the video and try it.", "Estimate the cost of 42 litres at $1.36: work out 40 × 1.4."),
    ]),
    dict(kind="hook", title="About $56", steps=[
        dict(say="4 times 14 is 56, so 40 times 1.4 is also 56. A full tank costs about 56 dollars.", do=[MATH("40 × 1.4 = 56", x=80, y=180), B("about $56", x=80, y=290, color=GREEN, at=3.6)]),
        dict(say="Now let's find the exact cost: 1.36 times 42.", do=[B("1.36 × 42 = ?", x=80, y=420, color=BLUE)]),
    ]),
    dict(kind="recall", title="Whole-number multiplying", steps=[
        dict(say="First, remember how to multiply whole numbers. 136 times 42.", do=[B("136 × 42", x=80, y=160)]),
        dict(say="136 times 40 is 5,440. 136 times 2 is 272. Add them: 5,712.", do=[MATH("136 × 40 = 5440", x=80, y=270), MATH("136 × 2 = 272", x=80, y=350, at=2.6), MATH("5440 + 272 = 5712", x=80, y=450, at=4.6, color=GREEN)]),
    ]),
    dict(kind="idea", title="Ignore the point, then put it back", steps=[
        dict(say="To multiply a decimal, first multiply as if there were no decimal point. 136 times 42 is 5,712.",
             do=[TBL(["Step", "1.36 × 42"], [["1. Multiply without the point", "136 × 42 = **5712**"], ["2. Count the decimal places in the question", "1.36 has **2**"], ["3. Give the answer the same number", "**57.12**"]], y=170), ROW(0, 2)]),
        dict(say="Then count the decimal places in the question. 1.36 has 2 decimal places.", do=[ROW(1, 0.3)]),
        dict(say="The answer must have 2 decimal places as well. So it is 57.12.", do=[ROW(2, 0.3)]),
        dict(say="A full tank costs 57 dollars 12. That is close to our estimate of 56, so the point is in the right place.", do=[B("$57.12", x=80, y=460, color=GREEN), T("estimate: 56 ✓", x=360, y=478, color=GREY, at=2.6)]),
        PAUSE("4.3-k2", "Your turn. Work out 2.7 times 3. Pause the video and try it.", "Work out 2.7 × 3."),
    ]),
    dict(kind="idea", title="Check: 2.7 × 3", steps=[
        dict(say="27 times 3 is 81. The question has 1 decimal place, so the answer is 8.1.", do=[MATH("27 × 3 = 81", x=80, y=190), T("1 decimal place", x=420, y=198, color=GREY, at=2), B("2.7 × 3 = 8.1", x=80, y=300, color=GREEN, at=3.6)]),
    ]),
    dict(kind="idea", title="Decimal × decimal", steps=[
        dict(say="The same idea works with two decimals. Count the decimal places in both numbers.", do=[T("Count the decimal places in **both** numbers", x=80, y=160)]),
        dict(say="0.3 times 0.2. 3 times 2 is 6. There is 1 decimal place in each number, so 2 altogether. The answer is 0.06.",
             do=[MATH("0.3 × 0.2", x=80, y=260), MATH("3 × 2 = 6", x=420, y=260, at=2, color=GREY), T("1 + 1 = **2** decimal places", x=420, y=340, at=4), B("= 0.06", x=80, y=420, color=GREEN, at=7.4)]),
        dict(say="Notice something. Multiplying by a number less than 1 makes the answer smaller.", do=[T("× a number less than 1 → **smaller**", x=80, y=530, color=RED)]),
    ]),
    dict(kind="method", title="How do I multiply decimals?", steps=[
        dict(say="Here is the method. Step 1: estimate, by rounding.", do=[T("1. **Estimate**", x=80, y=170)]),
        dict(say="Step 2: multiply the numbers as if there were no decimal points.", do=[T("2. Multiply **without** the points", x=80, y=260)]),
        dict(say="Step 3: count the total number of decimal places in the question.", do=[T("3. **Count** the decimal places in the question", x=80, y=350)]),
        dict(say="Step 4: put the point in, so the answer has that many decimal places. Check with your estimate.", do=[T("4. Give the answer that many places; check", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Written method", steps=[
        dict(say="Work out 23.8 times 6. Estimate first: 24 times 6 is 144.", do=[B("23.8 × 6", x=80, y=150), T("estimate: 24 × 6 = **144**", x=420, y=168, color=GREY, at=2.4)]),
        dict(say="Without the point: 238 times 6. 200 times 6 is 1,200. 30 times 6 is 180. 8 times 6 is 48. Altogether, 1,428.",
             do=[MATH("1200 + 180 + 48 = 1428", x=80, y=280)]),
        dict(say="The question has 1 decimal place. So the answer is 142.8.", do=[B("142.8", x=80, y=390, color=GREEN), T("close to 144 ✓", x=320, y=408, color=GREY, at=2.4)]),
    ]),
    dict(kind="example", title="Two decimals", steps=[
        dict(say="Work out 1.5 times 0.4.", do=[B("1.5 × 0.4", x=80, y=160)]),
        dict(say="15 times 4 is 60.", do=[MATH("15 × 4 = 60", x=80, y=270)]),
        dict(say="There are 2 decimal places in the question. So the answer is 0.60, which is 0.6.", do=[T("1 + 1 = 2 decimal places", x=420, y=278, color=GREY), B("0.60 = 0.6", x=80, y=380, color=GREEN, at=2.6)]),
        PAUSE("4.3-k3", "Your turn. Work out 0.9 times 0.9. Pause and work it out.", "Work out 0.9 × 0.9."),
    ]),
    dict(kind="example", title="Check: 0.9 × 0.9", steps=[
        dict(say="9 times 9 is 81. There are 2 decimal places in the question. The answer is 0.81.", do=[MATH("9 × 9 = 81", x=80, y=190), B("0.9 × 0.9 = 0.81", x=80, y=300, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Buying fabric", steps=[
        dict(say="Fabric costs 4 dollars 65 for each metre. How much do 3.2 metres cost? Estimate: 5 times 3 is 15.",
             do=[E("🧵", 90, 160, 90), T("**$4.65** per metre × **3.2 m**", x=210, y=190), T("estimate: 5 × 3 = **15**", x=760, y=190, color=GREY, at=5)]),
        dict(say="Without the points: 465 times 32 is 14,880.", do=[MATH("465 × 32 = 14 880", x=80, y=310)]),
        dict(say="There are 2 plus 1, so 3 decimal places. That gives 14.880. The fabric costs 14 dollars 88.", do=[T("2 + 1 = 3 decimal places → 14.880", x=80, y=400), B("$14.88", x=80, y=480, color=GREEN, at=3.4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Zoe works out 0.2 times 0.3. Which line is wrong?", do=LINES("Zoe", "0.2 × 0.3", ["2 × 3 = 6", "0.2 × 0.3 = 0.6"])),
        dict(say="Line 2 is wrong. The question has 2 decimal places altogether, so the answer needs 2 as well.", do=[dict(a="cross", id="l2")]),
        dict(say="The answer is 0.06. That makes sense: a part of 0.3 must be less than 0.3.", do=[B("0.2 × 0.3 = 0.06", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="How far away is the storm?", steps=[
        dict(say="Here is a trick for a stormy day. Sound travels about 0.34 kilometres every second.", do=[E("⛈️", 90, 170, 100), T("sound travels about **0.34 km** each second", x=230, y=200)]),
        dict(say="You see lightning, and count 6 seconds until the thunder.", do=[E("⚡", 90, 310, 90), T("lightning … **6 seconds** … thunder", x=230, y=335)]),
        dict(say="0.34 times 6. 34 times 6 is 204, and there are 2 decimal places. The storm is about 2.04 kilometres away.",
             do=[MATH("0.34 × 6 = 2.04", x=230, y=440, color=BLUE), T("about **2 km** away", x=640, y=450, at=5)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.3-k4", "One last question. Which of these answers is smaller than 12? Pause the video and choose.", "Which answer is smaller than 12?"),
        dict(say="12 times 0.8. Multiplying by a number less than 1 makes the answer smaller. 12 times 0.8 is 9.6.", do=[MATH("12 × 0.8 = 9.6", x=80, y=190, color=GREEN), T("× less than 1 → smaller", x=480, y=198, color=GREY, at=2)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: multiply without the points, then count the decimal places in the question.", do=[T("• Multiply without the points; count decimal places", x=80, y=170)]),
        dict(say="The answer has the same total number of decimal places.", do=[T("• The answer has the **same total**", x=80, y=250)]),
        dict(say="Multiplying by a number between 0 and 1 makes the answer smaller.", do=[T("• × a number between 0 and 1 → smaller", x=80, y=330)]),
        dict(say="Always estimate, to check where the point goes.", do=[T("• Estimate to check the point", x=80, y=410)]),
    ]),
]

STEPT = lambda title, rows, x=80, y=240: TBL(["Step", title], [list(r) for r in rows], x, y)

VIDEOS["4.4"] = [
    dict(kind="hook", title="Sharing the bill", steps=[
        dict(say="Six friends share a pizza bill. The bill is 38 dollars 70, and they split it equally.",
             do=[E("🍕", 90, 160, 100), T("bill: **$38.70**", x=230, y=190), T("shared by **6** friends", x=520, y=190, at=2.4)]),
        PAUSE("4.4-k1", "How much does each friend pay? Pause the video and work it out.", "$38.70 shared equally by 6. How much does each pay, in dollars?"),
    ]),
    dict(kind="hook", title="38.70 ÷ 6", steps=[
        dict(say="We need 38.70 divided by 6. Estimate first: 36 divided by 6 is 6, so the answer is a bit more than 6.", do=[MATH("38.70 ÷ 6", x=80, y=170), T("estimate: 36 ÷ 6 = **6**", x=480, y=178, color=GREY, at=3)]),
        dict(say="The exact answer is 6.45. Each friend pays 6 dollars 45. Let's see how to work that out.", do=[B("$6.45 each", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="recall", title="Short division", steps=[
        dict(say="Remember short division. 774 divided by 6.", do=[B("774 ÷ 6", x=80, y=150)]),
        dict(say="7 divided by 6 is 1, remainder 1. Carry the 1 to make 17.", do=[STEPT("774 ÷ 6", [("7 ÷ 6", "1 remainder 1"), ("17 ÷ 6", "2 remainder 5"), ("54 ÷ 6", "9")]), ROW(0, 0.4)]),
        dict(say="17 divided by 6 is 2, remainder 5. Carry the 5 to make 54. 54 divided by 6 is 9. The answer is 129.", do=[ROW(1, 0.3), ROW(2, 4), B("129", x=560, y=290, color=GREEN, at=7)]),
    ]),
    dict(kind="idea", title="Keep the point in line", steps=[
        dict(say="To divide a decimal by a whole number, use short division. Write the decimal point in the answer directly above the point in the question.",
             do=[T("The point in the answer goes **directly above** the point in the question", x=80, y=150, color=RED)]),
        dict(say="38.70 divided by 6. 3 divided by 6 is 0, so look at 38. 38 divided by 6 is 6, remainder 2.",
             do=[STEPT("38.70 ÷ 6", [("38 ÷ 6", "**6** remainder 2"), ("the point", "write **.** in the answer"), ("27 ÷ 6", "**4** remainder 3"), ("30 ÷ 6", "**5**")], y=230), ROW(0, 3.6)]),
        dict(say="Now we reach the decimal point, so put a point in the answer.", do=[ROW(1, 0.3)]),
        dict(say="Carry the 2 to make 27. 27 divided by 6 is 4, remainder 3. Then 30 divided by 6 is 5.", do=[ROW(2, 0.6), ROW(3, 4.4)]),
        dict(say="The answer is 6.45.", do=[B("38.70 ÷ 6 = 6.45", x=640, y=300, color=GREEN)]),
        PAUSE("4.4-k2", "Your turn. Work out 8.4 divided by 2. Pause the video and try it.", "Work out 8.4 ÷ 2."),
    ]),
    dict(kind="idea", title="Check: 8.4 ÷ 2", steps=[
        dict(say="8 divided by 2 is 4. Write the point. 4 divided by 2 is 2. The answer is 4.2.", do=[MATH("8 ÷ 2 = 4", x=80, y=190), MATH("4 ÷ 2 = 2", x=420, y=190, at=2.4), B("8.4 ÷ 2 = 4.2", x=80, y=300, color=GREEN, at=4.4)]),
    ]),
    dict(kind="idea", title="When it doesn't divide exactly", steps=[
        dict(say="Sometimes there is a remainder at the end. Then write extra zeros after the decimal point, and keep dividing.", do=[T("Remainder at the end? **Add zeros** and keep going", x=80, y=150)]),
        dict(say="7.3 divided by 4. Write 7.3 as 7.300.", do=[MATH("7.3 ÷ 4  →  7.300 ÷ 4", x=80, y=240)]),
        dict(say="7 divided by 4 is 1, remainder 3. 33 divided by 4 is 8, remainder 1. 10 divided by 4 is 2, remainder 2. 20 divided by 4 is 5.",
             do=[STEPT("7.300 ÷ 4", [("7 ÷ 4", "**1** remainder 3"), ("33 ÷ 4", "**8** remainder 1"), ("10 ÷ 4", "**2** remainder 2"), ("20 ÷ 4", "**5**")], y=320), ROW(0, 0.3), ROW(1, 3), ROW(2, 6), ROW(3, 9)]),
        dict(say="The answer is 1.825.", do=[B("1.825", x=640, y=390, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I divide a decimal?", steps=[
        dict(say="Here is the method. Step 1: estimate first.", do=[T("1. **Estimate**", x=80, y=170)]),
        dict(say="Step 2: set out short division. Write the point in the answer above the point in the question.", do=[T("2. Short division; **point above point**", x=80, y=260)]),
        dict(say="Step 3: divide digit by digit, carrying the remainders.", do=[T("3. Divide digit by digit; carry remainders", x=80, y=350)]),
        dict(say="Step 4: if there is a remainder at the end, add zeros and carry on. Then check by multiplying.", do=[T("4. Remainder? Add zeros. Check by multiplying", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Simple division", steps=[
        dict(say="Work out 14.56 divided by 4. Estimate: 16 divided by 4 is 4.", do=[B("14.56 ÷ 4", x=80, y=150), T("estimate: 16 ÷ 4 = **4**", x=480, y=168, color=GREY, at=2.6)]),
        dict(say="14 divided by 4 is 3, remainder 2. Write 3, then the point.", do=[STEPT("14.56 ÷ 4", [("14 ÷ 4", "**3** remainder 2, then the point"), ("25 ÷ 4", "**6** remainder 1"), ("16 ÷ 4", "**4**")], y=250), ROW(0, 0.3)]),
        dict(say="25 divided by 4 is 6, remainder 1. 16 divided by 4 is 4.", do=[ROW(1, 0.3), ROW(2, 3)]),
        dict(say="The answer is 3.64. That is close to the estimate of 4.", do=[B("3.64", x=700, y=310, color=GREEN)]),
        PAUSE("4.4-k3", "Your turn. Work out 3 divided by 8. You will need to add zeros. Pause and work it out.", "Work out 3 ÷ 8."),
    ]),
    dict(kind="example", title="Check: 3 ÷ 8", steps=[
        dict(say="Write 3 as 3.000. 30 divided by 8 is 3, remainder 6. 60 divided by 8 is 7, remainder 4. 40 divided by 8 is 5. The answer is 0.375.",
             do=[STEPT("3.000 ÷ 8", [("30 ÷ 8", "**3** remainder 6"), ("60 ÷ 8", "**7** remainder 4"), ("40 ÷ 8", "**5**")], y=170), ROW(0, 2.4), ROW(1, 5.6), ROW(2, 8.6), B("3 ÷ 8 = 0.375", x=560, y=230, color=GREEN, at=11)]),
    ]),
    dict(kind="example", title="A two-digit divisor", steps=[
        dict(say="Work out 52.8 divided by 16. Estimate: 48 divided by 16 is 3.", do=[B("52.8 ÷ 16", x=80, y=150), T("estimate: 48 ÷ 16 = **3**", x=480, y=168, color=GREY, at=2.6)]),
        dict(say="It helps to list the multiples of 16: 16, 32, 48, 64.", do=[T("16, 32, 48, 64", x=80, y=260, color=BLUE)]),
        dict(say="52 divided by 16 is 3, remainder 4. Write the point. Then 48 divided by 16 is 3. The answer is 3.3.", do=[MATH("52 ÷ 16 = 3 r 4", x=80, y=350), MATH("48 ÷ 16 = 3", x=480, y=350, at=3.6), B("3.3", x=80, y=450, color=GREEN, at=6)]),
    ]),
    dict(kind="example", title="Cutting a plank", steps=[
        dict(say="A plank is 2.85 metres long. It is cut into 5 equal pieces. How long is each piece, in centimetres?",
             do=[E("🪵", 90, 160, 90), T("**2.85 m** cut into **5** equal pieces", x=210, y=190)]),
        dict(say="2.85 divided by 5 is 0.57 metres.", do=[MATH("2.85 ÷ 5 = 0.57 m", x=80, y=310)]),
        dict(say="Multiply by 100 to change metres to centimetres. Each piece is 57 centimetres long.", do=[MATH("0.57 × 100 = 57 cm", x=80, y=410, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Max works out 7.2 divided by 3. Which line is wrong?", do=LINES("Max", "7.2 ÷ 3", ["7 ÷ 3 = 2 r 1", "12 ÷ 3 = 4", "Answer: 24"])),
        dict(say="Line 3 is wrong. Max forgot the decimal point. It goes in the answer, straight above the point in 7.2.", do=[dict(a="cross", id="l3")]),
        dict(say="The answer is 2.4. An estimate helps: 7 divided by 3 is about 2, so 24 is far too big.", do=[B("7.2 ÷ 3 = 2.4", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Half a marathon", steps=[
        dict(say="A marathon is a very exact distance: 42.195 kilometres.", do=[E("🏃", 90, 170, 100), T("marathon: **42.195 km**", x=230, y=200)]),
        dict(say="A half marathon is that distance divided by 2.", do=[MATH("42.195 ÷ 2", x=230, y=300)]),
        dict(say="42 divided by 2 is 21, and 0.195 divided by 2 is 0.0975. A half marathon is 21.0975 kilometres. That is about 21.1 kilometres.",
             do=[B("= 21.0975 km", x=230, y=400, color=GREEN), T("about **21.1 km**", x=640, y=418, at=6.4)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.4-k4", "One last question. What is 0.9 divided by 3? Pause the video and answer.", "0.9 ÷ 3 = ?"),
        dict(say="9 tenths divided by 3 is 3 tenths. The answer is 0.3.", do=[MATH("9 tenths ÷ 3 = 3 tenths", x=80, y=190), B("0.9 ÷ 3 = 0.3", x=80, y=300, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: put the point in the answer, above the point in the question.", do=[T("• **Point above point**", x=80, y=170)]),
        dict(say="Divide digit by digit, carrying remainders.", do=[T("• Divide digit by digit; carry remainders", x=80, y=250)]),
        dict(say="Add zeros after the point to keep dividing.", do=[T("• Add zeros to keep dividing", x=80, y=330)]),
        dict(say="Estimate first, and check by multiplying.", do=[T("• Estimate first; check by multiplying", x=80, y=410)]),
    ]),
]

VIDEOS["4.5"] = [
    dict(kind="hook", title="Mental shortcut", steps=[
        dict(say="A market seller sells 9 boxes of mangoes. Each box costs 6 dollars 80.",
             do=[E("🥭", 90, 160, 100), T("**9** boxes at **$6.80** each", x=230, y=190)]),
        PAUSE("4.5-k1", "Can you work out the total in your head? Pause the video and try.", "9 boxes at $6.80 each. What is the total, in dollars?"),
    ]),
    dict(kind="hook", title="Ten boxes, then take one away", steps=[
        dict(say="9 is nearly 10. And 10 boxes are easy: 10 times 6.80 is 68 dollars.", do=[MATH("10 × 6.80 = 68.00", x=80, y=180)]),
        dict(say="That is one box too many. So take one box off. 68 minus 6.80 is 61.20.", do=[MATH("68.00 − 6.80 = 61.20", x=80, y=290, color=BLUE)]),
        dict(say="9 boxes cost 61 dollars 20. This trick is called compensation.", do=[B("$61.20", x=80, y=410, color=GREEN), T("**compensation**", x=360, y=428, at=3)]),
    ]),
    dict(kind="recall", title="Laws of arithmetic", steps=[
        dict(say="Remember three useful laws. You can multiply in any order. 3 times 7 is the same as 7 times 3.", do=[MATH("3 × 7 = 7 × 3", x=80, y=170)]),
        dict(say="You can group in any way. 2 times 5, times 9, is the same as 2, times 5 times 9.", do=[MATH("(2 × 5) × 9 = 2 × (5 × 9)", x=80, y=270)]),
        dict(say="And you can split a number. 6 times 14 is 6 times 10, plus 6 times 4.", do=[MATH("6 × 14 = 6 × 10 + 6 × 4", x=80, y=370, color=BLUE)]),
    ]),
    dict(kind="idea", title="Compensation", steps=[
        dict(say="Compensation means: use a nearby round number, then adjust.", do=[T("**Compensation**: use a round number, then **adjust**", x=80, y=160)]),
        dict(say="9 times a number is 10 times the number, minus the number.", do=[B("9 × a = 10 × a − a", x=80, y=260, color=BLUE)]),
        dict(say="So 9 times 6.8 is 68 minus 6.8, which is 61.2.", do=[MATH("9 × 6.8 = 68 − 6.8 = 61.2", x=80, y=380)]),
        dict(say="It works for 99 as well. 99 times a number is 100 times the number, minus the number.", do=[MATH("99 × a = 100 × a − a", x=80, y=490, color=GREY)]),
    ]),
    dict(kind="idea", title="Place value and factors", steps=[
        dict(say="Here are three more strategies. First: a decimal is a division. 0.06 is 6 divided by 100.",
             do=[T("**A decimal is a division**", x=80, y=150, color=BLUE), MATH("0.06 × 3500 = 6 × 3500 ÷ 100 = 6 × 35 = 210", x=80, y=210, at=3)]),
        dict(say="So 0.06 times 3,500 is 6 times 35, which is 210.", do=[E("✅", 1040, 196, 50)]),
        dict(say="Second: split the divisor. Dividing by 40 is the same as dividing by 4, then by 10. 13.6 divided by 4 is 3.4, and 3.4 divided by 10 is 0.34.",
             do=[T("**Split the divisor**", x=80, y=310, color=RED), MATH("13.6 ÷ 40 = 3.4 ÷ 10 = 0.34", x=80, y=370, at=4.6)]),
        dict(say="Third: re-order, to use an easy pair. 0.25 times 4 is exactly 1.", do=[T("**Re-order** to use easy pairs", x=80, y=470, color=GREEN), MATH("0.25 × 4 = 1", x=80, y=530, at=2.4)]),
        PAUSE("4.5-k2", "Your turn. Work out 0.5 times 4.6 times 2 in your head. Pause the video and try it.", "Work out 0.5 × 4.6 × 2."),
    ]),
    dict(kind="idea", title="Check: 0.5 × 4.6 × 2", steps=[
        dict(say="Do the easy pair first. 0.5 times 2 is 1. Then 1 times 4.6 is 4.6.", do=[MATH("0.5 × 2 = 1", x=80, y=190, color=BLUE), B("1 × 4.6 = 4.6", x=80, y=300, color=GREEN, at=3)]),
    ]),
    dict(kind="method", title="How do I make it easier?", steps=[
        dict(say="Here is the method. Step 1: look at the numbers. Is one close to a round number? Is there a pair that makes 1, 10 or 100?", do=[T("1. **Look**: a round number nearby? A pair making 1, 10 or 100?", x=80, y=170)]),
        dict(say="Step 2: choose a strategy. Compensate, split, re-order, or write the decimal as a division.", do=[T("2. **Choose**: compensate, split, re-order, or decimal as a division", x=80, y=260)]),
        dict(say="Step 3: write down the steps, so you do not lose track.", do=[T("3. **Write** the steps", x=80, y=350)]),
        dict(say="Step 4: check with an estimate.", do=[T("4. **Check** with an estimate", x=80, y=440), E("✅", 1000, 410, 90, at=0.6)]),
    ]),
    dict(kind="example", title="Re-ordering", steps=[
        dict(say="Work out 0.25 times 9.7 times 4.", do=[B("0.25 × 9.7 × 4", x=80, y=160)]),
        dict(say="Re-order it. Do 0.25 times 4 first. That is 1.", do=[MATH("0.25 × 4 = 1", x=80, y=270, color=BLUE)]),
        dict(say="1 times 9.7 is 9.7. Done, with no written multiplication.", do=[B("1 × 9.7 = 9.7", x=80, y=380, color=GREEN)]),
    ]),
    dict(kind="example", title="A decimal as a division", steps=[
        dict(say="Work out 0.08 times 450.", do=[B("0.08 × 450", x=80, y=160)]),
        dict(say="0.08 is 8 divided by 100.", do=[MATH("0.08 = 8 ÷ 100", x=80, y=270, color=BLUE)]),
        dict(say="8 times 450 is 3,600. Divide by 100. The answer is 36.", do=[MATH("8 × 450 = 3600", x=80, y=360), B("3600 ÷ 100 = 36", x=80, y=460, color=GREEN, at=2.6)]),
    ]),
    dict(kind="example", title="Splitting the divisor", steps=[
        dict(say="Work out 7.2 divided by 30.", do=[B("7.2 ÷ 30", x=80, y=160)]),
        dict(say="Dividing by 30 is dividing by 3, then by 10.", do=[T("÷ 30  =  ÷ 3, then ÷ 10", x=80, y=270, color=BLUE)]),
        dict(say="7.2 divided by 3 is 2.4. Then 2.4 divided by 10 is 0.24.", do=[MATH("7.2 ÷ 3 = 2.4", x=80, y=360), B("2.4 ÷ 10 = 0.24", x=80, y=460, color=GREEN, at=2.6)]),
        PAUSE("4.5-k3", "Your turn. Work out 8.4 divided by 20. Pause and work it out.", "Work out 8.4 ÷ 20."),
    ]),
    dict(kind="example", title="Check: 8.4 ÷ 20", steps=[
        dict(say="Divide by 2, then by 10. 8.4 divided by 2 is 4.2. Then 4.2 divided by 10 is 0.42.", do=[MATH("8.4 ÷ 2 = 4.2", x=80, y=190, color=BLUE), B("4.2 ÷ 10 = 0.42", x=80, y=300, color=GREEN, at=3.6)]),
    ]),
    dict(kind="example", title="Compensation with money", steps=[
        dict(say="A ticket costs 11 dollars 95. How much do 6 tickets cost?", do=[E("🎟️", 90, 160, 90), T("**$11.95** each × **6**", x=210, y=190)]),
        dict(say="Round up to 12 dollars. 6 times 12 is 72.", do=[MATH("6 × 12 = 72", x=80, y=300)]),
        dict(say="Each ticket was 5 cents too much. 6 times 5 cents is 30 cents.", do=[MATH("6 × 0.05 = 0.30", x=80, y=390, color=BLUE)]),
        dict(say="Take that off. 72 minus 0.30 is 71.70. The tickets cost 71 dollars 70.", do=[B("72 − 0.30 = $71.70", x=80, y=490, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Sam works out 9 times 3.4, using 10 times 3.4. Which line goes wrong first?",
             do=LINES("Sam", "9 × 3.4", ["10 × 3.4 = 34", "9 is one less than 10, so subtract 1", "34 − 1 = 33"])),
        dict(say="Line 2 is wrong. 9 lots is one lot of 3.4 less than 10 lots. So subtract 3.4, not 1.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="34 minus 3.4 is 30.6.", do=[B("34 − 3.4 = 30.6", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Prices that end in 99", steps=[
        dict(say="Shops love prices that end in 99. Compensation makes them easy. Suppose you buy 5 drinks at 3 dollars 99 each.",
             do=[E("🥤", 90, 170, 100), T("**5** drinks at **$3.99**", x=230, y=200)]),
        dict(say="Pretend each one costs 4 dollars. 5 times 4 is 20.", do=[MATH("5 × 4 = 20", x=230, y=300)]),
        dict(say="Each price was 1 cent too much, so take off 5 cents. The total is 19 dollars 95.", do=[MATH("20 − 0.05 = 19.95", x=230, y=400, color=BLUE), B("$19.95", x=640, y=392, color=GREEN, at=3), E("🧠", 1000, 380, 100, at=3.6)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("4.5-k4", "One last question. What is 99 times 0.3? Pause the video and answer.", "99 × 0.3 = ?"),
        dict(say="100 times 0.3 is 30. That is one lot of 0.3 too many. 30 minus 0.3 is 29.7.", do=[MATH("100 × 0.3 = 30", x=80, y=190), B("30 − 0.3 = 29.7", x=80, y=300, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: compensation means round, calculate, then adjust.", do=[T("• Compensation: round, calculate, adjust", x=80, y=170)]),
        dict(say="Split numbers or divisors. Dividing by 40 is dividing by 4, then by 10.", do=[T("• Split: ÷ 40 = ÷ 4, then ÷ 10", x=80, y=250)]),
        dict(say="Re-order to use easy pairs, like 0.25 times 4.", do=[T("• Re-order for easy pairs: 0.25 × 4 = 1", x=80, y=330)]),
        dict(say="And a decimal is a division. 0.06 is 6 divided by 100.", do=[T("• A decimal is a division: 0.06 = 6 ÷ 100", x=80, y=410)]),
    ]),
]
