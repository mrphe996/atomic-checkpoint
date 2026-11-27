# -*- coding: utf-8 -*-
"""Stage 8 · Unit 3 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u03 import PVT, ROW as PROW, CUT
from .s7_u04 import TBL, ROW

VIDEOS = {}

VIDEOS["3.1"] = [
    dict(kind="hook", title="A sale", steps=[
        dict(say="A shop takes 0.1 of the price off in a sale. A jacket costs 85 dollars. A phone app works out 85 times 0.1.",
             do=[E("🧥", 90, 170, 100), T("**0.1** of the price off · jacket **$85**", x=230, y=200), MATH("85 × 0.1", x=230, y=300, color=BLUE)]),
        dict(say="Will the answer be bigger or smaller than 85?", do=[T("bigger or smaller than 85?", x=230, y=390)]),
        PAUSE("3.1-k1", "What is 85 times 0.1? Pause the video and work it out.", "85 × 0.1 = ?"),
    ]),
    dict(kind="hook", title="One tenth", steps=[
        dict(say="0.1 is one tenth. So 85 times 0.1 means one tenth of 85. That is 85 divided by 10, which is 8.5.",
             do=[MATH("0.1 = 1/10", x=80, y=190), MATH("85 × 0.1 = 85 ÷ 10 = 8.5", x=80, y=280, color=GREEN, at=4)]),
        dict(say="The discount is 8 dollars 50. Multiplying by 0.1 made the answer smaller.", do=[B("$8.50 off", x=80, y=380, color=GREEN)]),
    ]),
    dict(kind="recall", title="Times and divide by 10 and 100", steps=[
        dict(say="Remember: when you multiply by 10, the digits move one place to the left. When you divide by 100, they move two places to the right.",
             do=[PVT([["3.6", "", "", "", "3", ".", "6", "", ""], ["÷ 100", "", "", "", "0", ".", "0", "3", "6"]], y=170), PROW(0, 0.3), PROW(1, 5)]),
        dict(say="So 3.6 divided by 100 is 0.036.", do=[MATH("3.6 ÷ 100 = 0.036", x=80, y=420, color=GREEN)]),
    ]),
    dict(kind="idea", title="Multiplying by 0.1 and 0.01", steps=[
        dict(say="0.1 is one tenth. So multiplying by 0.1 is the same as dividing by 10.", do=[B("× 0.1  =  ÷ 10", x=80, y=170, color=BLUE)]),
        dict(say="0.01 is one hundredth. So multiplying by 0.01 is the same as dividing by 100.", do=[B("× 0.01  =  ÷ 100", x=80, y=260, color=BLUE)]),
        dict(say="For example, 46 times 0.1 is 4.6. And 46 times 0.01 is 0.46.",
             do=[TBL(["Calculation", "Same as", "Answer"], [["46 × 0.1", "46 ÷ 10", "4.6"], ["46 × 0.01", "46 ÷ 100", "0.46"]], y=350), ROW(0, 0.3), ROW(1, 2.6)]),
        PAUSE("3.1-k2", "Your turn. Work out 7 times 0.01. Pause the video and try it.", "Work out 7 × 0.01."),
    ]),
    dict(kind="idea", title="Check: 7 × 0.01", steps=[
        dict(say="Times 0.01 is the same as divide by 100. 7 divided by 100 is 0.07.", do=[MATH("7 × 0.01 = 7 ÷ 100 = 0.07", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Dividing by 0.1 and 0.01", steps=[
        dict(say="Now dividing. How many tenths are there in 3? There are 10 in each whole, so 30. So dividing by 0.1 is the same as multiplying by 10.",
             do=[MATH("3 ÷ 0.1 = 30", x=80, y=170), B("÷ 0.1  =  × 10", x=80, y=260, color=BLUE, at=6)]),
        dict(say="How many hundredths are there in 3? 300. So dividing by 0.01 is the same as multiplying by 100.", do=[MATH("3 ÷ 0.01 = 300", x=80, y=360), B("÷ 0.01  =  × 100", x=80, y=450, color=BLUE, at=4)]),
        dict(say="Dividing by a number between 0 and 1 makes the answer bigger.", do=[T("÷ a number less than 1 → **bigger**", x=640, y=178, color=RED)]),
    ]),
    dict(kind="method", title="How do I times or divide by 0.1 and 0.01?", steps=[
        dict(say="Here is the method. Step 1: times 0.1 means divide by 10. Times 0.01 means divide by 100.", do=[T("1. × 0.1 → **÷ 10** · × 0.01 → **÷ 100**", x=80, y=170)]),
        dict(say="Step 2: divide by 0.1 means times 10. Divide by 0.01 means times 100.", do=[T("2. ÷ 0.1 → **× 10** · ÷ 0.01 → **× 100**", x=80, y=260)]),
        dict(say="Step 3: move the digits the right way.", do=[T("3. Move the digits the right way", x=80, y=350)]),
        dict(say="Step 4: check. Multiplying by a number less than 1 gives a smaller answer. Dividing by it gives a bigger answer.", do=[T("4. **Check**: × → smaller · ÷ → bigger", x=80, y=440), E("✅", 1100, 410, 90, at=3)]),
    ]),
    dict(kind="example", title="Dividing", steps=[
        dict(say="Work out 0.45 divided by 0.1. Divide by 0.1 is times 10. 0.45 times 10 is 4.5.", do=[MATH("0.45 ÷ 0.1", x=80, y=170), MATH("= 0.45 × 10 = 4.5", x=80, y=260, color=GREEN, at=3)]),
        PAUSE("3.1-k3", "Your turn. Work out 2.3 divided by 0.1. Pause and work it out.", "Work out 2.3 ÷ 0.1."),
    ]),
    dict(kind="example", title="Check: 2.3 ÷ 0.1", steps=[
        dict(say="Divide by 0.1 is times 10. 2.3 times 10 is 23. There are 23 tenths in 2.3.", do=[MATH("2.3 ÷ 0.1 = 2.3 × 10 = 23", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Two steps", steps=[
        dict(say="Work out 7.2 times 0.01, divided by 0.1. Times 0.01 is divide by 100: that gives 0.072.", do=[MATH("7.2 × 0.01 ÷ 0.1", x=80, y=170), MATH("7.2 × 0.01 = 0.072", x=80, y=260, at=4)]),
        dict(say="Then divide by 0.1, which is times 10. 0.072 times 10 is 0.72.", do=[MATH("0.072 ÷ 0.1 = 0.72", x=80, y=350, color=GREEN)]),
    ]),
    dict(kind="example", title="A missing number", steps=[
        dict(say="Find the missing number. 53 times what is 0.53? The digits moved two places to the right. That is divide by 100, which is the same as times 0.01.",
             do=[MATH("53 × ☐ = 0.53", x=80, y=170), MATH("☐ = 0.01", x=80, y=270, color=GREEN, at=7)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Raj works out 6 divided by 0.1. Which line goes wrong first?", do=LINES("Raj", "6 ÷ 0.1", ["÷ 0.1 is the same as ÷ 10", "6 ÷ 0.1 = 0.6"])),
        dict(say="Line 1 is wrong. There are 10 tenths in every whole, so there are 60 tenths in 6. Divide by 0.1 is the same as times 10.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="6 divided by 0.1 is 60.", do=[B("6 ÷ 0.1 = 60", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Cents and dollars", steps=[
        dict(say="1 cent is 0.01 of a dollar. So to change cents into dollars, multiply by 0.01.", do=[E("🪙", 90, 170, 100), T("1 cent = **$0.01**", x=230, y=200)]),
        dict(say="A jar holds 4,750 cents. 4,750 times 0.01 is 47.5. That is 47 dollars 50.", do=[MATH("4750 × 0.01 = 47.5", x=230, y=300), B("$47.50", x=230, y=390, color=GREEN, at=4)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("3.1-k4", "One last question. Which gives the biggest answer: 5 divided by 0.01, 5 times 0.01, or 5 divided by 0.1? Pause the video and choose.", "Which gives the biggest answer?"),
        dict(say="5 divided by 0.01 is 500. 5 times 0.01 is 0.05. 5 divided by 0.1 is 50. The biggest is 5 divided by 0.01.",
             do=TEST([("5 ÷ 0.01 = 500", True), ("5 × 0.01 = 0.05", False), ("5 ÷ 0.1 = 50", False)], 220, t0=0.4, gap=2.4, dx=330)),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: times 0.1 is the same as divide by 10. Times 0.01 is the same as divide by 100.", do=[T("• × 0.1 = ÷ 10 · × 0.01 = ÷ 100", x=80, y=170)]),
        dict(say="Divide by 0.1 is the same as times 10. Divide by 0.01 is the same as times 100.", do=[T("• ÷ 0.1 = × 10 · ÷ 0.01 = × 100", x=80, y=250)]),
        dict(say="Multiplying by a number less than 1 makes the answer smaller.", do=[T("• × a number less than 1 → smaller", x=80, y=330)]),
        dict(say="Dividing by a number less than 1 makes the answer bigger.", do=[T("• ÷ a number less than 1 → bigger", x=80, y=410)]),
    ]),
]

VIDEOS["3.2"] = [
    dict(kind="hook", title="Big and small numbers", steps=[
        dict(say="The Moon is about 384,400 kilometres from Earth.", do=[E("🌕", 90, 170, 100), T("Earth to Moon: about **384 400 km**", x=230, y=200)]),
        dict(say="A news report gives numbers with just 2 important digits, to make them easy to read. These are called significant figures.", do=[T("just **2 important digits**", x=230, y=300)]),
        PAUSE("3.2-k1", "What is 384,400 to 2 significant figures? Pause the video and try it.", "384 400 to 2 important digits (2 s.f.)?"),
    ]),
    dict(kind="hook", title="380 000", steps=[
        dict(say="The two most important digits are 3 and 8. The next digit is 4, so we do not round up. Then fill the other places with zeros to keep the size.",
             do=[CUT("38", "4 400", x=80, y=190), T("next digit **4** → don't round up", x=420, y=198, at=4)]),
        dict(say="384,400 to 2 significant figures is 380,000 kilometres.", do=[B("380 000 km", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="recall", title="Decimal places", steps=[
        dict(say="Remember how to round to decimal places. Look at the next digit. If it is 5 or more, round up.", do=[T("next digit **5 or more** → round up", x=80, y=170)]),
        dict(say="3.476 to 2 decimal places: the next digit is 6, so round up to 3.48.", do=[CUT("3.47", "6", x=80, y=260), MATH("→ 3.48", x=320, y=260, color=GREEN, at=3)]),
    ]),
    dict(kind="idea", title="Significant figures", steps=[
        dict(say="Significant figures are the digits that matter most. Start counting at the first digit that is not zero.", do=[B("start at the first **non-zero** digit", x=80, y=170)]),
        dict(say="In 384,400 the first significant figure is 3. In 0.0712, the zeros at the front do not count. The first significant figure is 7.",
             do=[TBL(["Number", "1st s.f.", "to 2 s.f."], [["384 400", "3", "380 000"], ["0.0712", "7", "0.071"], ["5.096", "5", "5.1"]], y=260), ROW(0, 0.3), ROW(1, 4)]),
        dict(say="Zeros between other digits do count. 5.096 to 2 significant figures is 5.1, because the 9 makes the 0 round up.", do=[ROW(2, 0.3)]),
        PAUSE("3.2-k2", "Your turn. How many significant figures does 0.0405 have? Pause the video and try it.", "How many s.f. does 0.0405 have?"),
    ]),
    dict(kind="idea", title="Check: 0.0405", steps=[
        dict(say="The zeros at the front do not count. Start at the 4. Then 0, then 5. The zero between the 4 and the 5 counts. So 0.0405 has 3 significant figures.",
             do=[MATH('0.0<span style="color:#1F9D61">405</span>', x=80, y=200), B("3 s.f.", x=80, y=300, color=GREEN, at=6)]),
    ]),
    dict(kind="idea", title="Keeping the size", steps=[
        dict(say="When you round a large number, fill the places after the last significant figure with zeros. 384,400 to 2 significant figures is 380,000, not 38.",
             do=[MATH("384 400 → 380 000", x=80, y=170, color=GREEN), T("not 38 ✗", x=560, y=178, color=RED)]),
        dict(say="For decimals, do not add zeros after the rounded digit. 0.0712 to 2 significant figures is just 0.071.", do=[MATH("0.0712 → 0.071", x=80, y=270, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I round to significant figures?", steps=[
        dict(say="Here is the method. Step 1: find the first digit that is not zero. That is the first significant figure.", do=[T("1. First **non-zero** digit = 1st s.f.", x=80, y=170)]),
        dict(say="Step 2: count along to the number of significant figures you need.", do=[T("2. Count along to the s.f. you need", x=80, y=260)]),
        dict(say="Step 3: look at the next digit. 5 or more means round up.", do=[T("3. Next digit **5 or more** → round up", x=80, y=350)]),
        dict(say="Step 4: for whole numbers, fill the places with zeros, up to the decimal point.", do=[T("4. Whole numbers: fill with **zeros**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A small decimal", steps=[
        dict(say="Round 0.004836 to 3 significant figures. The first significant figure is 4. Count three: 4, 8, 3. The next digit is 6, so round up.",
             do=[CUT("0.00483", "6", x=80, y=170)]),
        dict(say="So the answer is 0.00484, to 3 significant figures.", do=[B("0.004 84", x=80, y=280, color=GREEN)]),
        PAUSE("3.2-k3", "Your turn. Round 2.645 to 2 significant figures. Pause and work it out.", "Round 2.645 to 2 s.f."),
    ]),
    dict(kind="example", title="Check: 2.645", steps=[
        dict(say="The first two significant figures are 2 and 6. The next digit is 4, so do not round up. The answer is 2.6.", do=[CUT("2.6", "45", x=80, y=190), B("2.6", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="A 9 that rolls over", steps=[
        dict(say="Round 7.997 to 3 significant figures. The digits are 7, 9, 9, and the next digit is 7, so round up.", do=[CUT("7.99", "7", x=80, y=170)]),
        dict(say="7.99 plus 0.01 is 8. To show 3 significant figures, write 8.00.", do=[B("8.00", x=80, y=280, color=GREEN), T("the zeros show **3 s.f.**", x=320, y=290, at=3)]),
    ]),
    dict(kind="example", title="Estimating", steps=[
        dict(say="Rounding to 1 significant figure is good for estimating. Estimate 62.4 times 0.487.", do=[MATH("62.4 × 0.487", x=80, y=170)]),
        dict(say="62.4 is about 60. 0.487 is about 0.5. 60 times 0.5 is 30.", do=[MATH("≈ 60 × 0.5 = 30", x=80, y=270, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Lena rounds 0.003527 to 2 significant figures. Which line is wrong?", do=LINES("Lena", "0.003 527 to 2 s.f.", ["The first two significant figures are 0 and 0", "Answer: 0.0"])),
        dict(say="Line 1 is wrong. The zeros at the front are not significant. The first significant figure is 3.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="The first two are 3 and 5. The next digit is 2. So the answer is 0.0035.", do=[B("0.0035", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Crowd sizes", steps=[
        dict(say="News reports round big numbers. If 61,847 people watch a football match, a report might say about 62,000 people. That is 2 significant figures.",
             do=[E("🏟️", 90, 170, 100), MATH("61 847 → about 62 000", x=230, y=190, color=BLUE)]),
        dict(say="A human hair is about 0.07 millimetres thick. That is 1 significant figure, and it is accurate enough for most uses.", do=[E("🔬", 90, 320, 90), T("a hair: about **0.07 mm**", x=230, y=345)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("3.2-k4", "One last question. Estimate 19.7 times 41.2, by rounding each number to 1 significant figure. Pause the video and answer.", "Estimate 19.7 × 41.2 (1 s.f. each)."),
        dict(say="19.7 is about 20. 41.2 is about 40. 20 times 40 is 800.", do=[MATH("19.7 × 41.2 ≈ 20 × 40", x=80, y=190), B("≈ 800", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the first significant figure is the first digit that is not zero.", do=[T("• 1st s.f. = the first non-zero digit", x=80, y=170)]),
        dict(say="Zeros between digits count. Zeros at the front of a decimal do not.", do=[T("• Zeros between digits count; leading zeros don't", x=80, y=250)]),
        dict(say="Round as usual, then fill with zeros to keep the size of whole numbers.", do=[T("• Fill with zeros to keep the size", x=80, y=330)]),
        dict(say="Round to 1 significant figure to estimate.", do=[T("• Round to 1 s.f. to estimate", x=80, y=410)]),
    ]),
]
