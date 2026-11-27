# -*- coding: utf-8 -*-
"""Stage 9 · Unit 8 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u07 import F, M

VIDEOS = {}

VIDEOS["8.1"] = [
    dict(kind="hook", title="Sharing the cost", steps=[
        dict(say="10 dollars shared between 8 friends is exactly 1.25 dollars each. But 10 dollars shared between 6 is 1.666 and so on. The calculator never finishes.",
             do=[E("🧾", 90, 170, 100), MATH("10 ÷ 8 = 1.25", x=230, y=180), MATH("10 ÷ 6 = 1.666…", x=230, y=260, at=6)]),
        PAUSE("8.1-k1", "Why does 10 divided by 6 recur: because 6 has a factor 3, or because 6 is even? Pause the video and choose.", "10 ÷ 6 recurs because …"),
    ]),
    dict(kind="hook", title="A factor of 3", steps=[
        dict(say="Because 6 has a factor of 3. 8 is 2 times 2 times 2, so it fits into 1,000. But no power of 10 divides by 3.", do=[B("6 = 2 × 3 → recurs", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Fraction to decimal", steps=[
        dict(say="Remember: a fraction is a division. 3 eighths is 3 divided by 8, which is 0.375.", do=[MATH(f"{F(3, 8)} = 3 ÷ 8 = 0.375", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Terminating or recurring?", steps=[
        dict(say="Write the fraction in its simplest form. If the denominator's prime factors are only 2s and 5s, the decimal terminates. Otherwise, it recurs.",
             do=[B("only 2s and 5s → terminates", x=80, y=170, color=BLUE), TBL(["Fraction", "Primes", "Decimal"], [["7/40", "2³ × 5", "0.175 – terminates"], ["1/6", "2 × 3", "0.1666… – recurs"], ["5/11", "11", "0.4545… – recurs"]], y=270), ROW(0, 3), ROW(1, 6), ROW(2, 9)]),
        PAUSE("8.1-k2", "Your turn. Does 1 fortieth terminate, or recur? Pause the video and choose.", "1/40 …"),
    ]),
    dict(kind="idea", title="Check: 1/40", steps=[
        dict(say="40 is 2 times 2 times 2 times 5. Only 2s and 5s, so it terminates. 1 fortieth is 0.025.", do=[B(f"{F(1, 40)} = 0.025 – terminates", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Recurring to fraction", steps=[
        dict(say="To turn a recurring decimal into a fraction, call it X. If one digit repeats, multiply by 10. If two digits repeat, multiply by 100.", do=[T("call it **x** · 1 digit repeats: **× 10** · 2 digits: **× 100**", x=80, y=170)]),
        dict(say="Then subtract, so the repeating part cancels, and solve.", do=[T("subtract → the repeat **cancels** → solve", x=80, y=260)]),
    ]),
    dict(kind="method", title="How do I convert?", steps=[
        dict(say="Here is the method. Step 1: call the decimal X.", do=[T("1. Let **x** = the decimal", x=80, y=170)]),
        dict(say="Step 2: multiply by 10, 100 or 1,000, to line up the repeats.", do=[T("2. Multiply to **line up** the repeats", x=80, y=260)]),
        dict(say="Step 3: subtract, then solve for X.", do=[T("3. **Subtract**, then solve", x=80, y=350)]),
        dict(say="Step 4: simplify, and check on a calculator.", do=[T("4. **Simplify**; check", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="One repeating digit", steps=[
        dict(say="Write 0.7 recurring as a fraction. X is 0.777 and so on. 10 X is 7.777 and so on. Subtract: 9 X is 7, so X is 7 ninths.",
             do=[MATH("10x = 7.777… · x = 0.777…", x=80, y=180), MATH(f"9x = 7 → x = {F(7, 9)}", x=80, y=290, color=GREEN, at=8)]),
        dict(say="Write 0.3 6, recurring, as a fraction. 100 X is 36.3636. Subtract X: 99 X is 36. So X is 36 over 99, which is 4 elevenths.",
             do=[MATH(f"99x = 36 → x = {F(36, 99)} = {F(4, 11)}", x=80, y=400)]),
        PAUSE("8.1-k3", "Your turn. Write 0.4 5 recurring, 0.4545 and so on, as a fraction in its simplest form. Pause and work it out.", "0.4545… as a fraction?"),
    ]),
    dict(kind="example", title="Check: 5/11", steps=[
        dict(say="100 X minus X: 99 X is 45. X is 45 over 99, which simplifies to 5 elevenths.", do=[B(f"{F(45, 99)} = {F(5, 11)}", x=80, y=190, color=GREEN)]),
        dict(say="Does 21 over 56 terminate? Simplify first: it is 3 eighths. 8 is only 2s, so yes. It is 0.375.", do=[MATH(f"{F(21, 56)} = {F(3, 8)} = 0.375 ✓", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Does 6 fifteenths give a terminating decimal? Lucy answers. Which line is wrong?", do=LINES("Lucy", "does 6/15 terminate?", ["15 = 3 × 5 has a 3", "so it recurs"])),
        dict(say="Line 1 is wrong. She did not simplify first.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="6 fifteenths is 2 fifths, which is 0.4. It terminates.", do=[B(f"{F(6, 15)} = {F(2, 5)} = 0.4", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Computers and rounding", steps=[
        dict(say="Computers store numbers in base 2. Even 0.1 recurs in base 2, so tiny rounding errors appear. Banks use special methods to avoid them.", do=[E("💻", 90, 170, 100), T("0.1 **recurs** in base 2", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.1-k4", "One last question. Does 1 twelfth recur, or terminate? Pause the video and choose.", "1/12 …"),
        dict(say="12 is 2 times 2 times 3. It has a factor of 3, so it recurs: 0.08333 and so on.", do=[B("12 = 2² × 3 → recurs", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: simplify first.", do=[T("• Simplify first", x=80, y=170)]),
        dict(say="Only 2s and 5s in the denominator: it terminates. Otherwise it recurs.", do=[T("• Only 2s and 5s → terminates", x=80, y=250)]),
        dict(say="For recurring decimals: multiply, subtract, solve.", do=[T("• Recurring: multiply, subtract, solve", x=80, y=330)]),
        dict(say="Check with a calculator.", do=[T("• Check", x=80, y=410)]),
    ]),
]

VIDEOS["8.2"] = [
    dict(kind="hook", title="Baking", steps=[
        dict(say="A cake recipe needs 1 and 3 quarter cups of flour. You make it 2 and a half times, and then use another 2 thirds of a cup to dust the table.",
             do=[E("🧁", 90, 170, 100), MATH(f"{M(1, 3, 4)} × {M(2, 1, 2)} + {F(2, 3)}", x=230, y=190)]),
        PAUSE("8.2-k1", "How much flour do you use altogether, in cups? Give your answer as a fraction in its simplest form. Pause the video and work it out.", "Total flour (cups)?"),
    ]),
    dict(kind="hook", title="Multiply first", steps=[
        dict(say="Multiply first, then add the 2 thirds. The total is 121 over 24, which is 5 and 1 twenty-fourth cups. Let's see how.",
             do=[T("**multiply** first, then add", x=80, y=180), B(f"{F(121, 24)} = {M(5, 1, 24)} cups", x=80, y=300, color=GREEN, at=4)]),
    ]),
    dict(kind="recall", title="Order of operations", steps=[
        dict(say="Remember the order: brackets, then indices, then multiply and divide, then add and subtract.", do=[B("Brackets → Indices → × ÷ → + −", x=80, y=190, color=BLUE)]),
    ]),
    dict(kind="idea", title="Fractions follow the order", steps=[
        dict(say="Fractions follow exactly the same order. Change mixed numbers into improper fractions first. 1 and 3 quarters is 7 quarters. 2 and a half is 5 halves.",
             do=[MATH(f"{M(1, 3, 4)} = {F(7, 4)}   ·   {M(2, 1, 2)} = {F(5, 2)}", x=80, y=180)]),
        PAUSE("8.2-k2", "Your turn. Work out 7 quarters times 5 halves. Give your answer as a fraction in its simplest form. Pause the video and try it.", "7/4 × 5/2?"),
    ]),
    dict(kind="idea", title="Check: 35/8", steps=[
        dict(say="Multiply the tops and the bottoms: 35 eighths. Then add 2 thirds: 105 over 24, plus 16 over 24, is 121 over 24.", do=[B(f"{F(7, 4)} × {F(5, 2)} = {F(35, 8)}", x=80, y=190, color=GREEN), MATH(f"{F(105, 24)} + {F(16, 24)} = {F(121, 24)}", x=80, y=300, at=5)]),
        dict(say="Indices work with fractions too. 2 thirds, squared, is 4 ninths. Square the top and the bottom.", do=[MATH(f"({F(2, 3)})² = {F(4, 9)}", x=80, y=310)]),
    ]),
    dict(kind="method", title="How do I calculate in order?", steps=[
        dict(say="Here is the method. Step 1: change mixed numbers to improper fractions.", do=[T("1. Mixed → **improper**", x=80, y=170)]),
        dict(say="Step 2: work out brackets, then indices.", do=[T("2. **Brackets**, then **indices**", x=80, y=260)]),
        dict(say="Step 3: multiply and divide, then add and subtract.", do=[T("3. **× ÷**, then **+ −**", x=80, y=350)]),
        dict(say="Step 4: simplify, and check with an estimate.", do=[T("4. **Simplify**; estimate", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Brackets", steps=[
        dict(say="Work out 2 and a half, minus 1 and a third, all times 6. The bracket first: 15 sixths minus 8 sixths is 7 sixths. Times 6 is 7.",
             do=[MATH(f"({F(15, 6)} − {F(8, 6)}) × 6 = {F(7, 6)} × 6", x=80, y=180), B("= 7", x=80, y=300, color=GREEN, at=9)]),
        PAUSE("8.2-k3", "Your turn. Work out 2 thirds plus 1 sixth, all divided by a half. Give your answer as a fraction in its simplest form. Pause and work it out.", "(2/3 + 1/6) ÷ 1/2?"),
    ]),
    dict(kind="example", title="Check", steps=[
        dict(say="The bracket: 4 sixths plus 1 sixth is 5 sixths. Dividing by a half is multiplying by 2: 10 sixths, which is 5 thirds.", do=[B(f"{F(5, 6)} × 2 = {F(5, 3)}", x=80, y=190, color=GREEN)]),
        dict(say="To estimate 4 and 7 eighths, times 2 and 1 tenth, minus 3 and a third: round to 5 times 2 minus 3, which is about 7.", do=[MATH("≈ 5 × 2 − 3 = 7", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ali works out a half, plus a half times a half. Which line is wrong?", do=LINES("Ali", "1/2 + 1/2 × 1/2", ["1/2 + 1/2 = 1", "1 × 1/2 = 1/2"])),
        dict(say="Line 1 is wrong. He worked left to right. Multiply first.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="A half times a half is a quarter. A half plus a quarter is 3 quarters.", do=[B(f"{F(1, 2)} + {F(1, 4)} = {F(3, 4)}", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Spreadsheets", steps=[
        dict(say="Spreadsheets and calculators follow the same order of operations. If you type a formula without brackets, the computer still multiplies first.", do=[E("📊", 90, 170, 100), T("computers use the **same order**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.2-k4", "One last question. Work out 1 minus a half times a half. Give your answer as a fraction. Pause the video and answer.", "1 − 1/2 × 1/2?"),
        dict(say="Multiply first: a half times a half is a quarter. 1 minus a quarter is 3 quarters.", do=[B(f"1 − {F(1, 4)} = {F(3, 4)}", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: fractions follow the same order of operations.", do=[T("• Same order: B, I, × ÷, + −", x=80, y=170)]),
        dict(say="Change mixed numbers to improper fractions.", do=[T("• Mixed → improper", x=80, y=250)]),
        dict(say="Do not just work left to right.", do=[T("• Not just left to right", x=80, y=330)]),
        dict(say="Estimate to check.", do=[T("• Estimate to check", x=80, y=410)]),
    ]),
]

VIDEOS["8.3"] = [
    dict(kind="hook", title="A garden", steps=[
        dict(say="A garden is 15 sixteenths of an acre. 8 ninths of it is lawn, and 3 tenths of the lawn is reseeded.",
             do=[E("🌱", 90, 170, 100), MATH(f"{F(3, 10)} × {F(8, 9)} × {F(15, 16)}", x=230, y=190)]),
        PAUSE("8.3-k1", "What fraction of an acre is reseeded? Give your answer as a fraction in its simplest form. Pause the video and work it out.", "Reseeded fraction of an acre?"),
    ]),
    dict(kind="hook", title="A quarter", steps=[
        dict(say="Cancel before you multiply. 3 and 9, 8 and 16, 15 and 10. Everything cancels to 1 over 4. A quarter of an acre.", do=[B(f"= {F(1, 4)} acre", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Multiplying fractions", steps=[
        dict(say="Remember: to multiply fractions, multiply the tops, and multiply the bottoms. 2 thirds times 4 fifths is 8 fifteenths.", do=[MATH(f"{F(2, 3)} × {F(4, 5)} = {F(8, 15)}", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Cancel first", steps=[
        dict(say="Before multiplying, cancel any top number with any bottom number that share a factor. The numbers stay small, and the answer is already simplified.",
             do=[T("cancel **any top** with **any bottom**", x=80, y=170), MATH(f"{F(4, 9)} × {F(3, 8)} = {F(1, 3)} × {F(1, 2)} = {F(1, 6)}", x=80, y=270, at=6)]),
        dict(say="A whole number N is N over 1.", do=[T("integer n = **n/1**", x=80, y=390)]),
        PAUSE("8.3-k2", "Your turn. Work out 18 times 5 twelfths. Give your answer as a fraction in its simplest form. Pause the video and try it.", "18 × 5/12?"),
    ]),
    dict(kind="idea", title="Check: 15/2", steps=[
        dict(say="Cancel 18 and 12 by 6: 3 times 5 halves is 15 halves, or 7 and a half.", do=[B(f"{F(15, 2)} = {M(7, 1, 2)}", x=80, y=190, color=GREEN)]),
        dict(say="For mixed numbers, change them to improper fractions first.", do=[T("mixed → **improper** first", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I multiply efficiently?", steps=[
        dict(say="Here is the method. Step 1: change mixed numbers and integers into fractions.", do=[T("1. Everything as a **fraction**", x=80, y=170)]),
        dict(say="Step 2: cancel common factors, top with bottom.", do=[T("2. **Cancel** top with bottom", x=80, y=260)]),
        dict(say="Step 3: multiply the tops and the bottoms.", do=[T("3. Multiply", x=80, y=350)]),
        dict(say="Step 4: change back to a mixed number if you need to, and estimate.", do=[T("4. Mixed number; **estimate**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Mixed numbers", steps=[
        dict(say="Work out 3 and 3 quarters, times 2 and 2 fifths. That is 15 quarters times 12 fifths. Cancel 15 and 5, and 12 and 4: 3 times 3 is 9.",
             do=[MATH(f"{F(15, 4)} × {F(12, 5)} = 3 × 3", x=80, y=180), B("= 9", x=80, y=290, color=GREEN, at=9)]),
        PAUSE("8.3-k3", "Your turn. Work out 2 and 2 thirds, times 1 and 1 eighth. Pause and work it out.", "2⅔ × 1⅛?"),
    ]),
    dict(kind="example", title="Check: 3", steps=[
        dict(say="8 thirds times 9 eighths. Cancel the 8s, and 9 with 3. The answer is 3. Estimate: about 3 times 1.", do=[B(f"{F(8, 3)} × {F(9, 8)} = 3", x=80, y=190, color=GREEN)]),
        dict(say="5 eighths of 2 and 2 fifths kilograms: 5 eighths times 12 fifths is 3 halves. That is 1 and a half kilograms.", do=[MATH(f"{F(5, 8)} × {F(12, 5)} = {F(3, 2)} = {M(1, 1, 2)} kg", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Leo works out 2 thirds plus 3 quarters. Which line is wrong?", do=LINES("Leo", "2/3 + 3/4", ["cancel the 3s: 2/1 + 1/4 = 2¼"])),
        dict(say="Line 1 is wrong. You can only cancel when you multiply, not when you add.", do=[dict(a="cross", id="l1")]),
        dict(say="Use a common denominator: 8 twelfths plus 9 twelfths is 17 twelfths.", do=[B(f"{F(8, 12)} + {F(9, 12)} = {F(17, 12)}", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Scaling recipes", steps=[
        dict(say="Chefs scale recipes by multiplying every amount by the same fraction. To make 3 quarters of a recipe, multiply each amount by 3 quarters.", do=[E("👩‍🍳", 90, 170, 100), T("every amount **× ¾**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.3-k4", "One last question. Work out 6 sevenths times 7 twelfths. Give your answer as a fraction in its simplest form. Pause the video and answer.", "6/7 × 7/12?"),
        dict(say="Cancel the 7s, and 6 with 12. The answer is a half.", do=[B(f"= {F(1, 2)}", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: cancel top with bottom before multiplying.", do=[T("• Cancel first", x=80, y=170)]),
        dict(say="Integers are over 1. Mixed numbers become improper fractions.", do=[T("• n = n/1 · mixed → improper", x=80, y=250)]),
        dict(say="Only cancel when multiplying.", do=[T("• Only cancel when multiplying", x=80, y=330)]),
        dict(say="Estimate to check.", do=[T("• Estimate to check", x=80, y=410)]),
    ]),
]

VIDEOS["8.4"] = [
    dict(kind="hook", title="Ribbon bows", steps=[
        dict(say="A craft shop has 7 and a half metres of ribbon. Each bow needs 5 eighths of a metre.",
             do=[E("🎀", 90, 170, 100), MATH(f"{M(7, 1, 2)} ÷ {F(5, 8)}", x=230, y=190)]),
        PAUSE("8.4-k1", "How many bows can be made? Pause the video and work it out.", "Number of bows?"),
    ]),
    dict(kind="hook", title="12 bows", steps=[
        dict(say="12 bows, because 12 lots of 5 eighths make 60 eighths, which is 7 and a half. Let's see how to divide by a fraction.", do=[MATH(f"12 × {F(5, 8)} = {F(60, 8)} = {M(7, 1, 2)}", x=80, y=190), B("12 bows", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="recall", title="Reciprocals", steps=[
        dict(say="Remember: the reciprocal of a fraction is the fraction flipped over. The reciprocal of 3 quarters is 4 thirds. The reciprocal of 5 is a fifth.", do=[MATH(f"{F(3, 4)} → {F(4, 3)}   ·   5 → {F(1, 5)}", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Dividing by a fraction", steps=[
        dict(say="To divide by a fraction, multiply by its reciprocal. Keep the first fraction, change divide to multiply, and flip the second.",
             do=[B("÷ a fraction = × its reciprocal", x=80, y=170, color=BLUE), MATH(f"{F(2, 3)} ÷ {F(4, 5)} = {F(2, 3)} × {F(5, 4)} = {F(5, 6)}", x=80, y=290, at=6)]),
        PAUSE("8.4-k2", "Your turn. To divide by 5 eighths, do you multiply by 8 fifths, or by 5 eighths? Pause the video and choose.", "To divide by 5/8, multiply by …"),
    ]),
    dict(kind="idea", title="Check: 8/5", steps=[
        dict(say="Multiply by 8 fifths, the reciprocal. 15 halves times 8 fifths is 12.", do=[B(f"× {F(8, 5)}", x=80, y=190, color=GREEN), MATH(f"{F(15, 2)} × {F(8, 5)} = 12", x=360, y=190, at=4)]),
        dict(say="Why does it work? Dividing by a half asks: how many halves fit? 2 in every 1. So dividing by a half is the same as multiplying by 2.", do=[MATH(f"÷ {F(1, 2)} = × 2", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I divide fractions?", steps=[
        dict(say="Here is the method. Step 1: change mixed numbers and integers to fractions.", do=[T("1. Everything as a **fraction**", x=80, y=170)]),
        dict(say="Step 2: flip the second fraction, the divisor.", do=[T("2. Flip the **divisor**", x=80, y=260)]),
        dict(say="Step 3: multiply, cancelling first.", do=[T("3. **Multiply**, cancel first", x=80, y=350)]),
        dict(say="Step 4: simplify, and check that the size makes sense.", do=[T("4. Simplify; **check**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Mixed numbers", steps=[
        dict(say="Work out 3 and a third, divided by 1 and a quarter. That is 10 thirds times 4 fifths, which is 8 thirds, or 2 and 2 thirds.",
             do=[MATH(f"{F(10, 3)} × {F(4, 5)} = {F(8, 3)}", x=80, y=180), B(f"= {M(2, 2, 3)}", x=80, y=290, color=GREEN, at=8)]),
        PAUSE("8.4-k3", "Your turn. Work out 4 fifths divided by 6. Give your answer as a fraction in its simplest form. Pause and work it out.", "4/5 ÷ 6?"),
    ]),
    dict(kind="example", title="Check: 2/15", steps=[
        dict(say="Dividing by 6 is multiplying by 1 sixth. 4 fifths times 1 sixth is 4 thirtieths, which is 2 fifteenths.", do=[B(f"{F(4, 30)} = {F(2, 15)}", x=80, y=190, color=GREEN)]),
        dict(say="A 2 and a quarter litre jug fills glasses of 3 eighths of a litre. 9 quarters times 8 thirds is 6. So 6 glasses.", do=[MATH(f"{F(9, 4)} × {F(8, 3)} = 6 glasses", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ivy works out 2 thirds divided by 4 fifths. Which line is wrong?", do=LINES("Ivy", "2/3 ÷ 4/5", ["3/2 × 4/5 = 12/10 = 6/5"])),
        dict(say="Line 1 is wrong. She flipped the first fraction. Flip the second one, the divisor.", do=[dict(a="cross", id="l1")]),
        dict(say="2 thirds times 5 quarters is 10 twelfths, which is 5 sixths.", do=[B(f"{F(2, 3)} × {F(5, 4)} = {F(5, 6)}", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Cutting wood", steps=[
        dict(say="Carpenters divide lengths by fractions to see how many pieces they can cut from one plank.", do=[E("🪵", 90, 170, 100), T("length **÷** piece = number of pieces", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.4-k4", "One last question. Work out 9 divided by 3 quarters. Pause the video and answer.", "9 ÷ 3/4?"),
        dict(say="9 times 4 thirds is 12.", do=[B(f"9 × {F(4, 3)} = 12", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: to divide by a fraction, multiply by its reciprocal.", do=[T("• ÷ fraction = × reciprocal", x=80, y=170)]),
        dict(say="Flip the second fraction, not the first.", do=[T("• Flip the divisor only", x=80, y=250)]),
        dict(say="Change mixed numbers first.", do=[T("• Mixed → improper first", x=80, y=330)]),
        dict(say="Dividing by a fraction less than 1 makes the answer bigger.", do=[T("• ÷ by less than 1 → bigger", x=80, y=410)]),
    ]),
]

VIDEOS["8.5"] = [
    dict(kind="hook", title="A mental maths race", steps=[
        dict(say="Two friends race. One uses a calculator. The other looks for shortcuts. The first question is 4.7 times 9, plus 4.7.",
             do=[E("🏁", 90, 170, 100), MATH("4.7 × 9 + 4.7", x=230, y=190)]),
        PAUSE("8.5-k1", "Can you find a shortcut? Work out 4.7 times 9, plus 4.7. Pause the video and try it.", "4.7 × 9 + 4.7?"),
    ]),
    dict(kind="hook", title="47", steps=[
        dict(say="4.7 times 9, plus 4.7 times 1, is 4.7 times 10. That is 47. No calculator needed.", do=[B("4.7 × 10 = 47", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Laws of arithmetic", steps=[
        dict(say="Remember: you can multiply in any order. And A times B plus C is A B plus A C.", do=[MATH("ab = ba   ·   a(b + c) = ab + ac", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Strategies", steps=[
        dict(say="Reorder: 0.25 times 36 times 4 is 0.25 times 4, which is 1, times 36. So 36.",
             do=[TBL(["Strategy", "Example"], [["reorder", "0.25 × 36 × 4 = 1 × 36 = 36"], ["common factor", "4.7 × 9 + 4.7 = 4.7 × 10"], ["decimal → fraction", "0.25 × 48 = ¼ × 48"], ["compensate", "19.8 × 5 = 20 × 5 − 0.2 × 5"]], y=170), ROW(0, 0.5)]),
        dict(say="Take out a common factor, like 4.7. Change a decimal into a fraction. Or round, then adjust. This is called compensating.", do=[ROW(1, 0.2), ROW(2, 3), ROW(3, 5)]),
        PAUSE("8.5-k2", "Your turn. 0.125 is 1 eighth. Use this to work out 0.125 times 64. Pause the video and try it.", "0.125 × 64?"),
    ]),
    dict(kind="idea", title="Check: 8", steps=[
        dict(say="1 eighth of 64 is 8.", do=[B(f"{F(1, 8)} × 64 = 8", x=80, y=190, color=GREEN)]),
        dict(say="Choose the method that fits the numbers. If there is no shortcut, use a written method or a calculator.", do=[T("choose what **fits** the numbers", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I make it easier?", steps=[
        dict(say="Here is the method. Step 1: look for pairs that make 1, 10 or 100.", do=[T("1. Pairs that make **1, 10, 100**", x=80, y=170)]),
        dict(say="Step 2: look for a common factor.", do=[T("2. A **common factor**", x=80, y=260)]),
        dict(say="Step 3: change decimals to fractions, or round and adjust.", do=[T("3. **Fractions**, or round and adjust", x=80, y=350)]),
        dict(say="Step 4: check with an estimate.", do=[T("4. **Estimate**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Round and adjust", steps=[
        dict(say="Work out 19.8 times 5. 20 times 5 is 100. Then take away 0.2 times 5, which is 1. The answer is 99.",
             do=[MATH("20 × 5 − 0.2 × 5 = 100 − 1", x=80, y=180), B("= 99", x=80, y=290, color=GREEN, at=8)]),
        PAUSE("8.5-k3", "Your turn. Work out 3.99 times 6. Pause and work it out.", "3.99 × 6?"),
    ]),
    dict(kind="example", title="Check: 23.94", steps=[
        dict(say="4 times 6 is 24. Take away 0.01 times 6, which is 0.06. The answer is 23.94.", do=[B("24 − 0.06 = 23.94", x=80, y=190, color=GREEN)]),
        dict(say="0.75 times 2.8 is 3 quarters of 2.8, which is 2.1. And 3 fifths times 17, plus 3 fifths times 3, is 3 fifths of 20, which is 12.", do=[MATH(f"{F(3, 4)} × 2.8 = 2.1 · {F(3, 5)} × 20 = 12", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Owen works out 6 times 2.5, plus 4 times 2.5. Which line is wrong?", do=LINES("Owen", "6 × 2.5 + 4 × 2.5", ["= (6 × 4) × 2.5 = 60"])),
        dict(say="Line 1 is wrong. Take out the common factor 2.5, and add the others.", do=[dict(a="cross", id="l1")]),
        dict(say="6 plus 4 is 10. 10 times 2.5 is 25.", do=[B("(6 + 4) × 2.5 = 25", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Shopping", steps=[
        dict(say="Shoppers use compensation all the time. 3 items at 4.99 dollars is 3 times 5, minus 3 cents: 14.97 dollars.", do=[E("🛒", 90, 170, 100), MATH("3 × 5 − 0.03 = 14.97", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.5-k4", "One last question. Work out 0.5 times 88. Pause the video and answer.", "0.5 × 88?"),
        dict(say="0.5 is a half. Half of 88 is 44.", do=[B("½ × 88 = 44", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: reorder to make easy pairs.", do=[T("• Reorder for easy pairs", x=80, y=170)]),
        dict(say="Take out a common factor.", do=[T("• Common factor", x=80, y=250)]),
        dict(say="Use fractions for decimals like 0.25, 0.5 and 0.125.", do=[T("• Decimals as fractions", x=80, y=330)]),
        dict(say="Round, then adjust.", do=[T("• Round, then adjust", x=80, y=410)]),
    ]),
]
