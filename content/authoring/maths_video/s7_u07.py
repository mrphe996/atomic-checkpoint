# -*- coding: utf-8 -*-
"""Stage 7 · Unit 7 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

F = lambda a, b: f"$$\\dfrac{{{a}}}{{{b}}}$$"                      # a fraction
M = lambda w, a, b: f"$${w}\\tfrac{{{a}}}{{{b}}}$$"               # a mixed number
def BAR(n, k, color=BLUE, w=420, label=""):
    """a fraction bar: n equal cells, the first k shaded"""
    cells = "".join(f'<span style="flex:1;height:44px;border:2px solid #1C2A3A;margin-left:-2px;background:{color if i < k else "#fff"}"></span>' for i in range(n))
    return f'<span style="display:inline-flex;align-items:center;gap:14px"><span style="display:inline-flex;width:{w}px;padding-left:2px">{cells}</span><span>{label}</span></span>'

VIDEOS = {}

VIDEOS["7.1"] = [
    dict(kind="hook", title="Which class did better?", steps=[
        dict(say="Three classes took a swimming test. In class A, 7 tenths of the students passed. In class B, 5 eighths passed. In class C, 2 thirds passed.",
             do=[E("🏊", 90, 160, 90), MATH(f"A: {F(7, 10)}", x=230, y=170), MATH(f"B: {F(5, 8)}", x=480, y=170, at=3.6), MATH(f"C: {F(2, 3)}", x=730, y=170, at=6)]),
        PAUSE("7.1-k1", "Which class had the greatest fraction passing? Pause the video and decide.", "Which class did best: A (7/10), B (5/8) or C (2/3)?"),
    ]),
    dict(kind="hook", title="Compare the bars", steps=[
        dict(say="Fraction bars make it easy to see. Here are 7 tenths, 5 eighths and 2 thirds.",
             do=[T(BAR(10, 7, BLUE, label="A"), x=80, y=170), T(BAR(8, 5, RED, label="B"), x=80, y=260, at=1.6), T(BAR(3, 2, GREEN, label="C"), x=80, y=350, at=3)]),
        dict(say="The bar for class A is shaded the furthest. So class A did best. But drawing bars is slow. Let's learn a quicker way.", do=[B("Class A did best", x=80, y=470, color=BLUE)]),
    ]),
    dict(kind="recall", title="Equivalent fractions", steps=[
        dict(say="Remember equivalent fractions. Multiply the numerator and the denominator by the same number, and the fraction keeps its value.",
             do=[MATH(f"{F(2, 3)} = {F(4, 6)} = {F(8, 12)}", x=80, y=170)]),
        dict(say="2 thirds, 4 sixths and 8 twelfths are all the same amount.", do=[T(BAR(3, 2, GREEN), x=80, y=330), T(BAR(6, 4, GREEN), x=80, y=400, at=0.8), T(BAR(12, 8, GREEN), x=80, y=470, at=1.6)]),
    ]),
    dict(kind="idea", title="Use a common denominator", steps=[
        dict(say="To compare fractions, write them with the same denominator. Then the larger numerator is the larger fraction.", do=[T("Same **denominator** → compare the **numerators**", x=80, y=150)]),
        dict(say="For tenths, eighths and thirds, a common denominator is 120. 7 tenths is 84 over 120.",
             do=[TBL(["Fraction", "With denominator 120", "Decimal"], [[F(7, 10), F(84, 120), "0.7"], [F(5, 8), F(75, 120), "0.625"], [F(2, 3), F(80, 120), "0.666…"]], y=220), ROW(0, 3)]),
        dict(say="5 eighths is 75 over 120, and 2 thirds is 80 over 120.", do=[ROW(1, 0.3), ROW(2, 2.4)]),
        dict(say="84 is the largest numerator, so 7 tenths is the largest fraction. You can also change each fraction to a decimal, and compare those.",
             do=[MATH(f"{F(5, 8)} < {F(2, 3)} < {F(7, 10)}", x=840, y=300, color=GREEN)]),
        PAUSE("7.1-k2", "Your turn. Which is larger: 5 sixths, or 7 ninths? Pause the video and try it.", "Which is larger: 5/6 or 7/9?"),
    ]),
    dict(kind="idea", title="Check: 5/6 or 7/9", steps=[
        dict(say="A common denominator for 6 and 9 is 18. 5 sixths is 15 eighteenths. 7 ninths is 14 eighteenths. 15 is more than 14, so 5 sixths is larger.",
             do=[MATH(f"{F(5, 6)} = {F(15, 18)}", x=80, y=180), MATH(f"{F(7, 9)} = {F(14, 18)}", x=480, y=180, at=4), MATH(f"{F(5, 6)} > {F(7, 9)}", x=80, y=360, color=GREEN, at=8)]),
    ]),
    dict(kind="idea", title="Improper fractions and mixed numbers", steps=[
        dict(say="An improper fraction has a numerator bigger than its denominator, like 11 quarters.", do=[MATH(F(11, 4), x=80, y=160), T("an **improper** fraction", x=220, y=190)]),
        dict(say="11 divided by 4 is 2, remainder 3. So 11 quarters is the mixed number 2 and 3 quarters.", do=[MATH(f"{F(11, 4)} = {M(2, 3, 4)}", x=80, y=300, color=BLUE), T("11 ÷ 4 = 2 remainder 3", x=420, y=330, color=GREY)]),
        dict(say="To compare mixed numbers, compare the whole number parts first. Only if they are the same do you compare the fractions.", do=[T("Compare the **whole numbers** first, then the fractions", x=80, y=470)]),
    ]),
    dict(kind="method", title="How do I order fractions?", steps=[
        dict(say="Here is the method. Step 1: change improper fractions to mixed numbers, and compare the whole number parts first.", do=[T("1. Mixed numbers; compare the **wholes** first", x=80, y=170)]),
        dict(say="Step 2: find a common denominator. The lowest common multiple of the denominators is best.", do=[T("2. Find a **common denominator** (the LCM)", x=80, y=260)]),
        dict(say="Step 3: write equivalent fractions, and compare the numerators.", do=[T("3. Equivalent fractions; compare **numerators**", x=80, y=350)]),
        dict(say="Step 4: write your answer using the original fractions.", do=[T("4. Answer with the **original** fractions", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Three fractions", steps=[
        dict(say="Put these in order, smallest first: 5 sixths, 3 quarters, and 7 twelfths.", do=[MATH(f"{F(5, 6)}, {F(3, 4)}, {F(7, 12)}", x=80, y=150)]),
        dict(say="The lowest common multiple of 6, 4 and 12 is 12. So use twelfths.", do=[T("LCM of 6, 4, 12 = **12**", x=520, y=180)]),
        dict(say="5 sixths is 10 twelfths. 3 quarters is 9 twelfths. 7 twelfths stays the same.", do=[MATH(f"{F(10, 12)}, {F(9, 12)}, {F(7, 12)}", x=80, y=300, color=BLUE)]),
        dict(say="7 is less than 9, which is less than 10. So the order is 7 twelfths, 3 quarters, 5 sixths.", do=[MATH(f"{F(7, 12)} < {F(3, 4)} < {F(5, 6)}", x=80, y=450, color=GREEN)]),
    ]),
    dict(kind="example", title="Mixed and improper", steps=[
        dict(say="Now compare an improper fraction with a mixed number. Which is larger: 13 fifths, or 2 and 3 quarters?",
             do=[MATH(f"{F(13, 5)} and {M(2, 3, 4)}", x=80, y=160)]),
        dict(say="13 fifths is 2 and 3 fifths. Both have 2 wholes, so compare 3 fifths and 3 quarters.", do=[MATH(f"{F(13, 5)} = {M(2, 3, 5)}", x=80, y=290, color=BLUE)]),
        dict(say="In twentieths, 3 fifths is 12 twentieths, and 3 quarters is 15 twentieths. So 2 and 3 quarters is larger.",
             do=[MATH(f"{F(3, 5)} = {F(12, 20)}", x=80, y=420), MATH(f"{F(3, 4)} = {F(15, 20)}", x=420, y=420, at=2.6), MATH(f"{M(2, 3, 4)} is larger", x=760, y=420, color=GREEN, at=5.4)]),
        PAUSE("7.1-k3", "Your turn. Which is larger: 17 fifths, or 3 and a quarter? Pause and work it out.", "Which is larger: 17/5 or 3 1/4?"),
    ]),
    dict(kind="example", title="Check: 17/5 or 3 1/4", steps=[
        dict(say="17 fifths is 3 and 2 fifths. Both have 3 wholes. 2 fifths is 8 twentieths, and 1 quarter is 5 twentieths. So 17 fifths is larger.",
             do=[MATH(f"{F(17, 5)} = {M(3, 2, 5)}", x=80, y=180, color=BLUE), MATH(f"{F(2, 5)} = {F(8, 20)} > {F(5, 20)} = {F(1, 4)}", x=80, y=330, at=4), MATH(f"{F(17, 5)} is larger", x=80, y=480, color=GREEN, at=8.6)]),
    ]),
    dict(kind="example", title="Between two fractions", steps=[
        dict(say="Find a fraction between 1 third and 1 half.", do=[MATH(f"{F(1, 3)} < ? < {F(1, 2)}", x=80, y=160)]),
        dict(say="Sixths are not enough: 2 sixths and 3 sixths have no gap between them. Try twelfths. 1 third is 4 twelfths, and 1 half is 6 twelfths.",
             do=[MATH(f"{F(1, 3)} = {F(4, 12)}", x=80, y=300), MATH(f"{F(1, 2)} = {F(6, 12)}", x=420, y=300, at=5)]),
        dict(say="5 twelfths is between them.", do=[MATH(f"{F(4, 12)} < {F(5, 12)} < {F(6, 12)}", x=80, y=450, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Which is larger: 3 eighths, or 2 fifths? Here is Pia's reasoning. Which line is wrong?", do=LINES("Pia", "3/8 or 2/5?", ["8 is bigger than 5", "so 3/8 is bigger"])),
        dict(say="Line 2 is wrong. A bigger denominator means smaller pieces. You must use a common denominator.", do=[dict(a="cross", id="l2")]),
        dict(say="In fortieths, 3 eighths is 15 fortieths, and 2 fifths is 16 fortieths. So 2 fifths is larger.", do=[MATH(f"{F(3, 8)} = {F(15, 40)}", x=110, y=420), MATH(f"{F(2, 5)} = {F(16, 40)}", x=420, y=420, at=2.6, color=GREEN)]),
    ]),
    dict(kind="life", title="Spanners and drill bits", steps=[
        dict(say="In some countries, tools are measured in fractions of an inch. A mechanic might have spanners marked 3 eighths, 7 sixteenths and 1 half.",
             do=[E("🔧", 90, 170, 100), MATH(f"{F(3, 8)}, {F(7, 16)}, {F(1, 2)} inch", x=230, y=180)]),
        dict(say="Which one is the middle size? Change them all to sixteenths: 6 sixteenths, 7 sixteenths and 8 sixteenths.", do=[MATH(f"{F(6, 16)}, {F(7, 16)}, {F(8, 16)}", x=230, y=330, color=BLUE)]),
        dict(say="So the 7 sixteenths spanner is in the middle. Mechanics order fractions like this every day.", do=[MATH(f"{F(3, 8)} < {F(7, 16)} < {F(1, 2)}", x=230, y=480, color=GREEN)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.1-k4", "One last question. Which fraction is between 1 quarter and 1 half? Pause the video and choose.", "Which fraction is between 1/4 and 1/2?"),
        dict(say="In eighths, 1 quarter is 2 eighths, and 1 half is 4 eighths. So 3 eighths is between them.", do=[MATH(f"{F(2, 8)} < {F(3, 8)} < {F(4, 8)}", x=80, y=190, color=GREEN), T(BAR(8, 3, GREEN), x=80, y=360, at=1)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: write fractions with a common denominator, then compare the numerators.", do=[T("• Common denominator, then compare numerators", x=80, y=170)]),
        dict(say="Or change them to decimals.", do=[T("• Or change to decimals", x=80, y=250)]),
        dict(say="Change improper fractions to mixed numbers, and compare the whole parts first.", do=[T("• Mixed numbers: compare the wholes first", x=80, y=330)]),
        dict(say="A bigger denominator does not mean a bigger fraction.", do=[T("• Bigger denominator ≠ bigger fraction", x=80, y=410)]),
    ]),
]

VIDEOS["7.2"] = [
    dict(kind="hook", title="Baking", steps=[
        dict(say="A cake recipe needs 2 and a quarter cups of flour. The icing needs 1 and 2 thirds cups.",
             do=[E("🎂", 90, 160, 100), MATH(f"cake: {M(2, 1, 4)} cups", x=230, y=175), MATH(f"icing: {M(1, 2, 3)} cups", x=640, y=175, at=3)]),
        PAUSE("7.2-k1", "Altogether, is that more or less than 4 cups? Pause the video and decide.", "2 1/4 + 1 2/3 cups. Is that more or less than 4 cups?"),
    ]),
    dict(kind="hook", title="Just under 4", steps=[
        dict(say="The whole numbers make 3. Then we have a quarter and 2 thirds left to add.", do=[MATH("2 + 1 = 3", x=80, y=180), MATH(f"{F(1, 4)} + {F(2, 3)}", x=420, y=170, at=2)]),
        dict(say="A quarter plus 2 thirds is 11 twelfths. That is less than 1 whole. So the total is 3 and 11 twelfths cups: just less than 4.",
             do=[MATH(f"{F(3, 12)} + {F(8, 12)} = {F(11, 12)}", x=80, y=320, color=BLUE), MATH(f"{M(3, 11, 12)} cups", x=80, y=470, color=GREEN, at=5)]),
    ]),
    dict(kind="recall", title="A common denominator", steps=[
        dict(say="Remember: to add fractions, they need a common denominator. Thirds and quarters can both be written as twelfths.",
             do=[T(BAR(4, 1, BLUE, label="one quarter"), x=80, y=170), T(BAR(12, 3, BLUE, label="3 twelfths"), x=80, y=240, at=1), T(BAR(3, 2, RED, label="2 thirds"), x=80, y=340, at=2.4), T(BAR(12, 8, RED, label="8 twelfths"), x=80, y=410, at=3.4)]),
        dict(say="Add the numerators only. The denominator tells you the size of the pieces, and that does not change.", do=[T("Add the **numerators** only", x=80, y=520, color=GREEN)]),
    ]),
    dict(kind="idea", title="Adding mixed numbers", steps=[
        dict(say="To add mixed numbers, add the whole numbers first. This also gives you a good estimate.", do=[T("1. Add the **whole numbers**", x=80, y=160), MATH(f"{M(2, 1, 4)} + {M(1, 2, 3)}", x=640, y=150)]),
        dict(say="Then add the fractions, using a common denominator.", do=[T("2. Add the **fractions**", x=80, y=260)]),
        dict(say="If the fraction part is improper, change it to a mixed number, and add it on.", do=[T("3. Improper? Change it and **carry** the whole", x=80, y=360)]),
        dict(say="For example, 1 and 3 quarters plus 2 and a half. The wholes make 3. 3 quarters plus 2 quarters is 5 quarters, which is 1 and a quarter. So the total is 4 and a quarter.",
             do=[MATH(f"{M(1, 3, 4)} + {M(2, 1, 2)} = 3 + {F(5, 4)} = 3 + {M(1, 1, 4)} = {M(4, 1, 4)}", x=80, y=470, color=BLUE, at=1.5)]),
        PAUSE("7.2-k2", "Your turn. Work out 1 and 1 fifth, plus 2 and 2 fifths. Pause the video and try it.", "Work out 1 1/5 + 2 2/5."),
    ]),
    dict(kind="idea", title="Check: 1 1/5 + 2 2/5", steps=[
        dict(say="1 plus 2 is 3. 1 fifth plus 2 fifths is 3 fifths. The answer is 3 and 3 fifths.", do=[MATH("1 + 2 = 3", x=80, y=180), MATH(f"{F(1, 5)} + {F(2, 5)} = {F(3, 5)}", x=420, y=170, at=1.8), MATH(M(3, 3, 5), x=80, y=340, color=GREEN, at=4)]),
    ]),
    dict(kind="idea", title="Subtracting mixed numbers", steps=[
        dict(say="Subtracting can be tricky. Take 5 and 1 third, minus 2 and 3 quarters. 1 third is smaller than 3 quarters, so we cannot just subtract the fractions.",
             do=[MATH(f"{M(5, 1, 3)} − {M(2, 3, 4)}", x=80, y=150)]),
        dict(say="The safest method is to change both numbers to improper fractions. 5 and 1 third is 16 thirds. 2 and 3 quarters is 11 quarters.",
             do=[MATH(f"{F(16, 3)} − {F(11, 4)}", x=80, y=290, color=BLUE)]),
        dict(say="In twelfths, that is 64 twelfths minus 33 twelfths, which is 31 twelfths. As a mixed number, 2 and 7 twelfths.",
             do=[MATH(f"{F(64, 12)} − {F(33, 12)} = {F(31, 12)} = {M(2, 7, 12)}", x=80, y=440, color=GREEN)]),
    ]),
    dict(kind="method", title="Adding and subtracting mixed numbers", steps=[
        dict(say="Here is the method. Step 1: estimate with the whole numbers.", do=[T("1. **Estimate** with the whole numbers", x=80, y=170)]),
        dict(say="Step 2: add or subtract the whole numbers.", do=[T("2. Add or subtract the **wholes**", x=80, y=260)]),
        dict(say="Step 3: add or subtract the fractions with a common denominator, and simplify.", do=[T("3. Fractions: **common denominator**, simplify", x=80, y=350)]),
        dict(say="Step 4: if a fraction is improper, carry. For a hard subtraction, use improper fractions.", do=[T("4. Carry; for hard subtractions use **improper fractions**", x=80, y=440), E("✅", 1040, 410, 80, at=0.8)]),
    ]),
    dict(kind="example", title="Carrying a whole", steps=[
        dict(say="Work out 1 and 5 eighths, plus 3 and 3 quarters.", do=[MATH(f"{M(1, 5, 8)} + {M(3, 3, 4)}", x=80, y=150)]),
        dict(say="The wholes: 1 plus 3 is 4.", do=[MATH("1 + 3 = 4", x=80, y=280)]),
        dict(say="The fractions: 5 eighths plus 6 eighths is 11 eighths. That is 1 and 3 eighths.", do=[MATH(f"{F(5, 8)} + {F(6, 8)} = {F(11, 8)} = {M(1, 3, 8)}", x=420, y=270, color=BLUE)]),
        dict(say="4 plus 1 and 3 eighths is 5 and 3 eighths.", do=[MATH(f"4 + {M(1, 3, 8)} = {M(5, 3, 8)}", x=80, y=440, color=GREEN)]),
        PAUSE("7.2-k3", "Your turn. Work out 2 and 3 quarters, plus 1 and a half. Pause and work it out.", "Work out 2 3/4 + 1 1/2."),
    ]),
    dict(kind="example", title="Check: 2 3/4 + 1 1/2", steps=[
        dict(say="The wholes make 3. 3 quarters plus 2 quarters is 5 quarters, which is 1 and a quarter. 3 plus 1 and a quarter is 4 and a quarter.",
             do=[MATH("2 + 1 = 3", x=80, y=180), MATH(f"{F(3, 4)} + {F(2, 4)} = {F(5, 4)} = {M(1, 1, 4)}", x=420, y=170, at=1.6, color=BLUE), MATH(M(4, 1, 4), x=80, y=350, color=GREEN, at=6)]),
    ]),
    dict(kind="example", title="Subtracting", steps=[
        dict(say="Work out 6 and 2 fifths, minus 3 and a half.", do=[MATH(f"{M(6, 2, 5)} − {M(3, 1, 2)}", x=80, y=150)]),
        dict(say="Change to improper fractions. 6 and 2 fifths is 32 fifths. 3 and a half is 7 halves.", do=[MATH(f"{F(32, 5)} − {F(7, 2)}", x=80, y=290, color=BLUE)]),
        dict(say="In tenths: 64 tenths minus 35 tenths is 29 tenths. That is 2 and 9 tenths.", do=[MATH(f"{F(64, 10)} − {F(35, 10)} = {F(29, 10)} = {M(2, 9, 10)}", x=80, y=440, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Lin works out 1 and 1 third, plus 2 and a quarter. Which line goes wrong first?", do=LINES("Lin", "1 1/3 + 2 1/4", ["1 + 2 = 3", "1/3 + 1/4 = 2/7", "Answer: 3 2/7"])),
        dict(say="Line 2 is wrong. You cannot add the tops and add the bottoms. Thirds and quarters are different sizes.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="Use twelfths. 4 twelfths plus 3 twelfths is 7 twelfths. The answer is 3 and 7 twelfths.", do=[MATH(f"{F(4, 12)} + {F(3, 12)} = {F(7, 12)}", x=110, y=460, color=BLUE), MATH(M(3, 7, 12), x=640, y=460, color=GREEN, at=3.4)]),
    ]),
    dict(kind="life", title="In the kitchen", steps=[
        dict(say="Cooks add mixed numbers all the time. Suppose a recipe needs 1 and a half cups of milk, and you want to make it three times.",
             do=[E("🥛", 90, 170, 100), MATH(f"{M(1, 1, 2)} cups, three times", x=230, y=180)]),
        dict(say="1 and a half plus 1 and a half is 3. Add another 1 and a half, and you get 4 and a half cups.", do=[MATH(f"{M(1, 1, 2)} + {M(1, 1, 2)} + {M(1, 1, 2)} = {M(4, 1, 2)}", x=230, y=330, color=BLUE)]),
        dict(say="A measuring jug marked in halves, thirds and quarters is really a fraction number line.", do=[E("🫙", 90, 460, 90), T("a measuring jug is a **fraction number line**", x=230, y=490)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.2-k4", "One last question. What is 3 minus 1 and 1 third? Pause the video and answer.", "3 − 1 1/3 = ?"),
        dict(say="3 is 9 thirds. 1 and 1 third is 4 thirds. 9 thirds minus 4 thirds is 5 thirds, which is 1 and 2 thirds.",
             do=[MATH(f"{F(9, 3)} − {F(4, 3)} = {F(5, 3)}", x=80, y=180, color=BLUE), MATH(M(1, 2, 3), x=80, y=340, color=GREEN, at=5)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: add the wholes, then add the fractions with a common denominator.", do=[T("• Wholes first, then fractions (common denominator)", x=80, y=170)]),
        dict(say="Change an improper fraction part to a mixed number, and carry.", do=[T("• Improper part → mixed number → carry", x=80, y=250)]),
        dict(say="For subtraction, improper fractions avoid problems.", do=[T("• Subtracting: improper fractions are safest", x=80, y=330)]),
        dict(say="Estimate with the whole numbers, and simplify your answer.", do=[T("• Estimate; simplify", x=80, y=410)]),
    ]),
]

def GRID(cols, rows, shade_cols, take_rows):
    """a rectangle cut into cols × rows: the first shade_cols columns light, and the first take_rows rows of them dark"""
    cells = "".join(f'<span style="width:74px;height:54px;border:2px solid #1C2A3A;margin:-1px;background:{"#2F6FEB" if c < shade_cols and r < take_rows else "#BFD4FB" if c < shade_cols else "#fff"}"></span>' for r in range(rows) for c in range(cols))
    return f'<span style="display:inline-grid;grid-template-columns:repeat({cols},74px);padding:2px">{cells}</span>'

VIDEOS["7.3"] = [
    dict(kind="hook", title="Mowing the lawn", steps=[
        dict(say="3 quarters of a garden is lawn. A gardener mows 2 thirds of the lawn before it starts to rain.",
             do=[E("🌱", 90, 160, 100), MATH(f"lawn: {F(3, 4)} of the garden", x=230, y=170), MATH(f"mown: {F(2, 3)} of the lawn", x=230, y=320, at=2.6)]),
        PAUSE("7.3-k1", "What fraction of the whole garden has been mown? Pause the video and work it out.", "2/3 of the 3/4 lawn is mown. What fraction of the whole garden is that?"),
    ]),
    dict(kind="hook", title="A fraction of a fraction", steps=[
        dict(say="Draw the garden as a rectangle with 4 columns. 3 of the columns are lawn. That is 3 quarters.", do=[T(GRID(4, 3, 3, 0), x=80, y=170), T("3 columns of 4 are lawn", x=440, y=190)]),
        dict(say="Now cut it into 3 rows, and take 2 of them. The dark part has been mown.", do=[T(GRID(4, 3, 3, 2), x=80, y=170, at=0.3), T("2 rows of 3 are mown", x=440, y=260)]),
        dict(say="There are 12 small pieces, and 6 are dark. 6 twelfths is one half. Half of the garden has been mown.", do=[MATH(f"{F(6, 12)} = {F(1, 2)}", x=440, y=350, color=GREEN)]),
    ]),
    dict(kind="recall", title="A fraction of an amount", steps=[
        dict(say="Remember how to find a fraction of an amount. For 3 fifths of 40, divide by the denominator, then multiply by the numerator.", do=[MATH(f"{F(3, 5)} of 40", x=80, y=160)]),
        dict(say="40 divided by 5 is 8. 8 times 3 is 24.", do=[MATH("40 ÷ 5 = 8", x=80, y=310), MATH("8 × 3 = 24", x=420, y=310, at=2, color=GREEN)]),
    ]),
    dict(kind="idea", title="“Of” means multiply", steps=[
        dict(say="2 thirds of 3 quarters is the same as 2 thirds times 3 quarters.", do=[MATH(f"{F(2, 3)} of {F(3, 4)} = {F(2, 3)} × {F(3, 4)}", x=80, y=150)]),
        dict(say="To multiply fractions, multiply the numerators, and multiply the denominators.", do=[T("**top × top**, **bottom × bottom**", x=80, y=300, color=BLUE)]),
        dict(say="2 times 3 is 6. 3 times 4 is 12. That gives 6 twelfths, which simplifies to one half. It matches the diagram.",
             do=[MATH(f"{F('2 × 3', '3 × 4')} = {F(6, 12)} = {F(1, 2)}", x=80, y=400, color=GREEN), T(GRID(4, 3, 3, 2), x=760, y=300, at=0.6)]),
        PAUSE("7.3-k2", "Your turn. Work out 1 third times 1 quarter. Pause the video and try it.", "Work out 1/3 × 1/4."),
    ]),
    dict(kind="idea", title="Check: 1/3 × 1/4", steps=[
        dict(say="1 times 1 is 1. 3 times 4 is 12. The answer is 1 twelfth.", do=[MATH(f"{F(1, 3)} × {F(1, 4)} = {F('1 × 1', '3 × 4')} = {F(1, 12)}", x=80, y=180, color=GREEN), T(GRID(4, 3, 1, 1), x=760, y=170, at=0.6)]),
    ]),
    dict(kind="idea", title="Cancelling, and whole numbers", steps=[
        dict(say="You can make the numbers smaller before you multiply. This is called cancelling. Divide a numerator and a denominator by the same number.", do=[T("**Cancel**: divide a top and a bottom by the same number", x=80, y=150)]),
        dict(say="In 2 thirds times 3 quarters, the threes cancel. And 2 and 4 both divide by 2. That leaves 1 over 1, times 1 over 2, which is one half.",
             do=[MATH(f"{F(2, 3)} × {F(3, 4)}", x=80, y=260), MATH(f"= {F(1, 1)} × {F(1, 2)} = {F(1, 2)}", x=360, y=260, at=5, color=GREEN)]),
        dict(say="A whole number can be written as a fraction over 1. So 5 times 2 thirds is 5 over 1, times 2 over 3. That is 10 thirds, or 3 and 1 third.",
             do=[MATH(f"5 × {F(2, 3)} = {F(5, 1)} × {F(2, 3)} = {F(10, 3)} = $$3\\tfrac{{1}}{{3}}$$", x=80, y=440, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I multiply fractions?", steps=[
        dict(say="Here is the method. Step 1: write any whole number as a fraction over 1.", do=[T("1. Whole number → a fraction **over 1**", x=80, y=170)]),
        dict(say="Step 2: cancel common factors between any numerator and any denominator.", do=[T("2. **Cancel** common factors", x=80, y=260)]),
        dict(say="Step 3: multiply the numerators, and multiply the denominators.", do=[T("3. **Top × top**, **bottom × bottom**", x=80, y=350)]),
        dict(say="Step 4: simplify, and change an improper fraction to a mixed number.", do=[T("4. Simplify; improper → mixed number", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Two proper fractions", steps=[
        dict(say="Work out 4 ninths times 3 eighths.", do=[MATH(f"{F(4, 9)} × {F(3, 8)}", x=80, y=150)]),
        dict(say="Cancel 4 with 8. They become 1 and 2.", do=[MATH(f"{F(1, 9)} × {F(3, 2)}", x=80, y=300, color=BLUE), T("4 and 8: ÷ 4", x=380, y=330, color=GREY)]),
        dict(say="Cancel 3 with 9. They become 1 and 3.", do=[MATH(f"{F(1, 3)} × {F(1, 2)}", x=620, y=300, color=BLUE), T("3 and 9: ÷ 3", x=900, y=330, color=GREY)]),
        dict(say="1 third times 1 half is 1 sixth.", do=[MATH(f"= {F(1, 6)}", x=80, y=450, color=GREEN)]),
    ]),
    dict(kind="example", title="A whole number", steps=[
        dict(say="Work out 6 times 5 eighths.", do=[MATH(f"6 × {F(5, 8)}", x=80, y=150)]),
        dict(say="Write 6 as 6 over 1. Cancel 6 and 8 by 2. They become 3 and 4.", do=[MATH(f"{F(6, 1)} × {F(5, 8)} = {F(3, 1)} × {F(5, 4)}", x=80, y=290, color=BLUE)]),
        dict(say="3 times 5 is 15. 1 times 4 is 4. 15 quarters is 3 and 3 quarters.", do=[MATH(f"= {F(15, 4)} = {M(3, 3, 4)}", x=80, y=440, color=GREEN)]),
        PAUSE("7.3-k3", "Your turn. Work out 4 times 3 tenths. Pause and work it out.", "Work out 4 × 3/10."),
    ]),
    dict(kind="example", title="Check: 4 × 3/10", steps=[
        dict(say="4 times 3 is 12, so we get 12 tenths. That simplifies to 6 fifths, which is 1 and 1 fifth.", do=[MATH(f"4 × {F(3, 10)} = {F(12, 10)} = {F(6, 5)} = {M(1, 1, 5)}", x=80, y=180, color=GREEN)]),
    ]),
    dict(kind="example", title="Tennis club", steps=[
        dict(say="In a club, 3 fifths of the members are adults. 5 sixths of the adults play tennis. What fraction of the club are adults who play tennis?",
             do=[E("🎾", 90, 160, 90), MATH(f"adults: {F(3, 5)}", x=210, y=170), MATH(f"of them, tennis: {F(5, 6)}", x=520, y=170, at=3)]),
        dict(say="We need 5 sixths of 3 fifths. Of means multiply.", do=[MATH(f"{F(5, 6)} × {F(3, 5)}", x=80, y=320)]),
        dict(say="The fives cancel. 3 and 6 cancel to 1 and 2. The answer is one half. Half of the club are adults who play tennis.", do=[MATH(f"= {F(1, 2)} × {F(1, 1)} = {F(1, 2)}", x=380, y=320, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Omar works out 2 fifths times 3 quarters. Which line is wrong?", do=LINES("Omar", "2/5 × 3/4", ["2 × 4 = 8 and 5 × 3 = 15", "Answer: 8/15"])),
        dict(say="Line 1 is wrong. Omar multiplied across the wrong way. Multiply top by top, and bottom by bottom.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="2 times 3 is 6, and 5 times 4 is 20. 6 twentieths simplifies to 3 tenths.", do=[MATH(f"{F('2 × 3', '5 × 4')} = {F(6, 20)} = {F(3, 10)}", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Water on Earth", steps=[
        dict(say="Here is a real fraction of a fraction. About 7 tenths of the Earth's surface is covered by water.", do=[E("🌍", 90, 170, 100), MATH(f"about {F(7, 10)} of Earth's surface is water", x=230, y=175)]),
        dict(say="And the Pacific Ocean holds roughly half of all that water surface.", do=[MATH(f"the Pacific is about {F(1, 2)} of that", x=230, y=320)]),
        dict(say="One half times 7 tenths is 7 twentieths. So the Pacific Ocean alone covers about a third of the whole planet.",
             do=[MATH(f"{F(1, 2)} × {F(7, 10)} = {F(7, 20)}", x=230, y=460, color=BLUE), T("about **one third** of the planet", x=640, y=490, at=4)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.3-k4", "One last question. Is 3 quarters times 4 fifths more than 3 quarters, or less? Pause the video and choose.", "3/4 × 4/5 is … more than 3/4, or less than 3/4?"),
        dict(say="It is less than 3 quarters. Multiplying by a fraction smaller than 1 makes the answer smaller. In fact, the fours cancel, and the answer is 3 fifths.",
             do=[MATH(f"{F(3, 4)} × {F(4, 5)} = {F(3, 5)}", x=80, y=180, color=GREEN), T("× a fraction less than 1 → **smaller**", x=80, y=350, at=2)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: of means multiply.", do=[T("• “Of” means **multiply**", x=80, y=170)]),
        dict(say="Multiply the numerators, multiply the denominators, and simplify.", do=[T("• Top × top, bottom × bottom; simplify", x=80, y=250)]),
        dict(say="Cancel common factors first, to make it easier.", do=[T("• Cancel first", x=80, y=330)]),
        dict(say="A whole number is a fraction over 1. And multiplying by a proper fraction makes the answer smaller.", do=[T("• n = n/1; × a proper fraction → smaller", x=80, y=410)]),
    ]),
]

VIDEOS["7.4"] = [
    dict(kind="hook", title="Sharing leftover pizza", steps=[
        dict(say="There is 3 quarters of a pizza left. Three friends share it equally.", do=[E("🍕", 90, 160, 100), MATH(f"{F(3, 4)} of a pizza, shared by 3", x=230, y=170)]),
        PAUSE("7.4-k1", "What fraction of a whole pizza does each friend get? Pause the video and work it out.", "3/4 of a pizza is shared equally by 3 friends. What fraction does each get?"),
    ]),
    dict(kind="hook", title="One quarter each", steps=[
        dict(say="3 quarters means 3 pieces, each a quarter of the pizza. Three friends, three pieces. They get one quarter each.",
             do=[T(BAR(4, 3, RED, label="3 quarters"), x=80, y=180), MATH(f"{F(3, 4)} ÷ 3 = {F(1, 4)}", x=80, y=320, color=GREEN, at=4)]),
    ]),
    dict(kind="recall", title="Two meanings of division", steps=[
        dict(say="Remember: 12 divided by 3 can mean share 12 into 3 equal groups.", do=[MATH("12 ÷ 3 = 4", x=80, y=170), T("share 12 into **3 groups**", x=420, y=178)]),
        dict(say="It can also mean: how many threes are in 12? Both give 4.", do=[T("or: **how many 3s** are in 12?", x=420, y=268)]),
        dict(say="The second meaning helps with fractions. How many halves are in 5? There are 10.", do=[MATH(f"5 ÷ {F(1, 2)} = 10", x=80, y=400, color=BLUE)]),
    ]),
    dict(kind="idea", title="A fraction ÷ a whole number", steps=[
        dict(say="Dividing by 3 is the same as finding one third. So dividing by 3 is the same as multiplying by 1 third.", do=[T("÷ 3 is the same as **× 1/3**", x=80, y=150, color=BLUE)]),
        dict(say="3 quarters divided by 3 is 3 quarters times 1 third. That is 3 twelfths, which simplifies to 1 quarter.",
             do=[MATH(f"{F(3, 4)} ÷ 3 = {F(3, 4)} × {F(1, 3)} = {F(3, 12)} = {F(1, 4)}", x=80, y=260)]),
        dict(say="Another example. 2 fifths divided by 4 is 2 fifths times 1 quarter. That is 2 twentieths, or 1 tenth.",
             do=[MATH(f"{F(2, 5)} ÷ 4 = {F(2, 5)} × {F(1, 4)} = {F(2, 20)} = {F(1, 10)}", x=80, y=430, color=GREEN)]),
        PAUSE("7.4-k2", "Your turn. Work out 8 ninths divided by 4. Pause the video and try it.", "Work out 8/9 ÷ 4."),
    ]),
    dict(kind="idea", title="Check: 8/9 ÷ 4", steps=[
        dict(say="8 ninths shared into 4 equal parts is 2 ninths each. Or: 8 ninths times 1 quarter is 8 over 36, which simplifies to 2 ninths.",
             do=[MATH(f"{F(8, 9)} ÷ 4 = {F(8, 9)} × {F(1, 4)} = {F(8, 36)} = {F(2, 9)}", x=80, y=180, color=GREEN)]),
    ]),
    dict(kind="idea", title="A fraction ÷ a fraction", steps=[
        dict(say="3 quarters divided by 1 eighth asks: how many eighths are in 3 quarters?", do=[MATH(f"{F(3, 4)} ÷ {F(1, 8)}", x=80, y=140), T("how many **eighths** are in 3 quarters?", x=360, y=170)]),
        dict(say="3 quarters is the same as 6 eighths. So there are 6.", do=[T(BAR(4, 3, RED), x=80, y=290), T(BAR(8, 6, RED), x=80, y=350, at=1.4), B("6", x=560, y=310, color=GREEN, at=3)]),
        dict(say="Here is the method. Turn the second fraction upside down, and multiply. The upside-down fraction is called the reciprocal.",
             do=[T("Flip the **second** fraction (its **reciprocal**) and **multiply**", x=80, y=440, color=BLUE)]),
        dict(say="3 quarters times 8 over 1 is 24 quarters, which is 6. The same answer.", do=[MATH(f"{F(3, 4)} × {F(8, 1)} = {F(24, 4)} = 6", x=80, y=520, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I divide fractions?", steps=[
        dict(say="Here is the method. Step 1: write a whole number as a fraction over 1.", do=[T("1. Whole number → a fraction **over 1**", x=80, y=170)]),
        dict(say="Step 2: keep the first fraction. Change divide to multiply. Flip the second fraction.", do=[T("2. **Keep** the first · **change** ÷ to × · **flip** the second", x=80, y=260)]),
        dict(say="Step 3: cancel, and multiply.", do=[T("3. Cancel and multiply", x=80, y=350)]),
        dict(say="Step 4: check that the size of your answer makes sense.", do=[T("4. Does the size make sense?", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Fraction ÷ fraction", steps=[
        dict(say="Work out 2 thirds divided by 4 ninths.", do=[MATH(f"{F(2, 3)} ÷ {F(4, 9)}", x=80, y=150)]),
        dict(say="Keep the first, change to times, flip the second. 2 thirds times 9 quarters.", do=[MATH(f"{F(2, 3)} × {F(9, 4)}", x=80, y=300, color=BLUE)]),
        dict(say="Cancel 2 with 4, to get 1 and 2. Cancel 3 with 9, to get 1 and 3.", do=[MATH(f"= {F(1, 1)} × {F(3, 2)}", x=380, y=300, color=BLUE)]),
        dict(say="That gives 3 halves, which is 1 and a half.", do=[MATH(f"= {F(3, 2)} = {M(1, 1, 2)}", x=80, y=450, color=GREEN)]),
        PAUSE("7.4-k3", "Your turn. How many sixths are in 2 thirds? Pause and work it out.", "How many 1/6s are in 2/3?"),
    ]),
    dict(kind="example", title="Check: how many sixths in 2/3", steps=[
        dict(say="2 thirds divided by 1 sixth is 2 thirds times 6. That is 12 thirds, which is 4. There are 4 sixths in 2 thirds.",
             do=[MATH(f"{F(2, 3)} ÷ {F(1, 6)} = {F(2, 3)} × {F(6, 1)} = {F(12, 3)} = 4", x=80, y=170, color=GREEN), T(BAR(3, 2, BLUE), x=80, y=350, at=1), T(BAR(6, 4, BLUE), x=80, y=410, at=1.6)]),
    ]),
    dict(kind="example", title="How many doses?", steps=[
        dict(say="A bottle holds 5 sixths of a litre. How many doses of 1 twelfth of a litre can be poured from it?", do=[E("🧴", 90, 150, 100), MATH(f"{F(5, 6)} litre ÷ {F(1, 12)} litre", x=230, y=160)]),
        dict(say="5 sixths times 12 over 1 is 60 sixths.", do=[MATH(f"{F(5, 6)} × {F(12, 1)} = {F(60, 6)}", x=80, y=320, color=BLUE)]),
        dict(say="60 divided by 6 is 10. You can pour 10 doses.", do=[B("10 doses", x=80, y=470, color=GREEN)]),
    ]),
    dict(kind="example", title="Cutting a ribbon", steps=[
        dict(say="A ribbon is 3 fifths of a metre long. It is cut into 4 equal pieces. How long is each piece?", do=[E("🎀", 90, 150, 100), MATH(f"{F(3, 5)} m ÷ 4", x=230, y=160)]),
        dict(say="Dividing by 4 is multiplying by 1 quarter. 3 fifths times 1 quarter is 3 twentieths of a metre.", do=[MATH(f"{F(3, 5)} × {F(1, 4)} = {F(3, 20)} m", x=80, y=320, color=GREEN)]),
        dict(say="3 twentieths of a metre is 15 centimetres.", do=[T("= **15 cm**", x=520, y=350)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Jay works out 2 fifths divided by 3 quarters. Which line is wrong?", do=LINES("Jay", "2/5 ÷ 3/4", ["5/2 × 3/4", "= 15/8"])),
        dict(say="Line 1 is wrong. Jay flipped the first fraction. Keep the first fraction, and flip only the second.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="2 fifths times 4 thirds is 8 fifteenths.", do=[MATH(f"{F(2, 5)} × {F(4, 3)} = {F(8, 15)}", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Fractions in music", steps=[
        dict(say="Musicians divide fractions without even noticing. A waltz is written in 3 4 time. Each bar lasts 3 quarter notes.", do=[E("🎼", 90, 160, 100), MATH(f"one bar = {F(3, 4)}", x=230, y=165)]),
        dict(say="How many eighth notes fit in one bar? That is 3 quarters divided by 1 eighth.", do=[E("🎵", 90, 310, 90), MATH(f"{F(3, 4)} ÷ {F(1, 8)}", x=230, y=310)]),
        dict(say="3 quarters times 8 is 6. So 6 eighth notes fit in every bar of a waltz.", do=[MATH(f"= {F(3, 4)} × 8 = 6", x=480, y=310, color=GREEN), B("6 eighth notes", x=230, y=470, color=BLUE, at=2.6)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.4-k4", "One last question. What is 1 half divided by 1 quarter? Pause the video and answer.", "1/2 ÷ 1/4 = ?"),
        dict(say="How many quarters are in a half? 2. Or: 1 half times 4 is 4 halves, which is 2.", do=[MATH(f"{F(1, 2)} ÷ {F(1, 4)} = {F(1, 2)} × {F(4, 1)} = 2", x=80, y=180, color=GREEN), T(BAR(4, 2, BLUE), x=80, y=360, at=1)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: dividing by a whole number n is multiplying by 1 over n.", do=[T("• ÷ n is the same as × 1/n", x=80, y=170)]),
        dict(say="To divide by a fraction, multiply by its reciprocal.", do=[T("• ÷ a fraction: multiply by its **reciprocal**", x=80, y=250)]),
        dict(say="Keep the first fraction, and flip only the second.", do=[T("• Keep the first; flip only the second", x=80, y=330)]),
        dict(say="Dividing by a proper fraction gives a bigger answer.", do=[T("• ÷ a proper fraction → a **bigger** answer", x=80, y=410)]),
    ]),
]

VIDEOS["7.5"] = [
    dict(kind="hook", title="Sale price", steps=[
        dict(say="A games console costs 480 dollars. In a sale, it is 5 sixths of the usual price.", do=[E("🎮", 90, 160, 100), T("usual price **$480**", x=230, y=185), MATH(f"sale: {F(5, 6)} of the price", x=560, y=165, at=2.6)]),
        PAUSE("7.5-k1", "What is the sale price? Try to find a quick way. Pause the video and work it out.", "What is 5/6 of $480?"),
    ]),
    dict(kind="hook", title="Take off one sixth", steps=[
        dict(say="5 sixths is the whole price, minus 1 sixth. And 1 sixth of 480 is easy: it is 80.", do=[T(BAR(6, 5, GREEN, label="5 sixths = whole − 1 sixth"), x=80, y=170), MATH(f"{F(1, 6)} of 480 = 80", x=80, y=300)]),
        dict(say="480 minus 80 is 400. The sale price is 400 dollars.", do=[MATH("480 − 80 = 400", x=80, y=440, color=BLUE), B("$400", x=480, y=432, color=GREEN, at=2.4)]),
    ]),
    dict(kind="recall", title="Factors", steps=[
        dict(say="Remember factors. The factors of 12 are 1, 2, 3, 4, 6 and 12.", do=[T("factors of 12: **1, 2, 3, 4, 6, 12**", x=80, y=170)]),
        dict(say="A number can be split into factors in different ways. 24 is 4 times 6, and also 3 times 8.", do=[MATH("24 = 4 × 6 = 3 × 8", x=80, y=290, color=BLUE)]),
    ]),
    dict(kind="idea", title="Subtract the small part", steps=[
        dict(say="When a fraction is close to 1, find the small missing part, and subtract it from the whole.", do=[T("Fraction close to 1 → **whole − small part**", x=80, y=150, color=BLUE)]),
        dict(say="9 tenths of 350. 1 tenth is 35. So 9 tenths is 350 minus 35, which is 315.", do=[MATH(f"{F(9, 10)} of 350 = 350 − 35 = 315", x=80, y=260)]),
        dict(say="3 quarters of 96. 1 quarter is 24. So 3 quarters is 96 minus 24, which is 72.", do=[MATH(f"{F(3, 4)} of 96 = 96 − 24 = 72", x=80, y=420, color=GREEN)]),
        PAUSE("7.5-k2", "Your turn. Work out 4 fifths of 650. Pause the video and try it.", "Work out 4/5 of 650."),
    ]),
    dict(kind="idea", title="Check: 4/5 of 650", steps=[
        dict(say="1 fifth of 650 is 130. Take that away from 650. The answer is 520.", do=[MATH(f"{F(1, 5)} of 650 = 130", x=80, y=170), MATH("650 − 130 = 520", x=80, y=330, at=2.6, color=GREEN)]),
    ]),
    dict(kind="idea", title="Factors, cancelling, re-ordering", steps=[
        dict(say="Here are three more ideas. First: use factors. 1 twelfth is 1 third of 1 quarter. So 1 twelfth of 600 is 1 third of 150, which is 50.",
             do=[T("**Use factors**", x=80, y=140, color=BLUE), MATH(f"{F(1, 12)} of 600 = {F(1, 3)} of 150 = 50", x=80, y=190, at=2.6)]),
        dict(say="Second: cancel before you multiply. In 15 over 28, times 14 over 45: 14 and 28 share a factor of 14, and 15 and 45 share a factor of 15. That leaves 1 half times 1 third, which is 1 sixth.",
             do=[T("**Cancel first**", x=80, y=310, color=RED), MATH(f"{F(15, 28)} × {F(14, 45)} = {F(1, 2)} × {F(1, 3)} = {F(1, 6)}", x=80, y=360, at=3)]),
        dict(say="Third: re-order. In 3 sevenths times 5 times 14, do 3 sevenths of 14 first. That is 6. Then 6 times 5 is 30.",
             do=[T("**Re-order**", x=80, y=480, color=GREEN), MATH(f"{F(3, 7)} × 14 × 5 = 6 × 5 = 30", x=80, y=530, at=3)]),
    ]),
    dict(kind="method", title="Making a fraction calculation easier", steps=[
        dict(say="Here is the method. Step 1: look at the fraction. Is it close to 1? Then use whole minus the small part.", do=[T("1. Close to 1? **Whole − small part**", x=80, y=170)]),
        dict(say="Step 2: look for common factors, and cancel before you multiply.", do=[T("2. **Cancel** before multiplying", x=80, y=260)]),
        dict(say="Step 3: split a denominator into factors, or re-order the multiplication.", do=[T("3. **Split** a denominator, or **re-order**", x=80, y=350)]),
        dict(say="Step 4: follow the order of operations. Multiply and divide before you add and subtract.", do=[T("4. × and ÷ before + and −", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Whole minus a part", steps=[
        dict(say="Work out 11 twelfths of 840.", do=[MATH(f"{F(11, 12)} of 840", x=80, y=150)]),
        dict(say="1 twelfth of 840 is 70.", do=[MATH(f"{F(1, 12)} of 840 = 70", x=80, y=300, color=BLUE)]),
        dict(say="840 minus 70 is 770.", do=[MATH("840 − 70 = 770", x=80, y=450, color=GREEN)]),
    ]),
    dict(kind="example", title="Splitting a denominator", steps=[
        dict(say="Work out 1 fifteenth of 2,400.", do=[MATH(f"{F(1, 15)} of 2400", x=80, y=150)]),
        dict(say="15 is 3 times 5. So find 1 fifth first, then 1 third of that.", do=[T("15 = 3 × 5", x=480, y=180, color=GREY)]),
        dict(say="1 fifth of 2,400 is 480. 1 third of 480 is 160.", do=[MATH(f"{F(1, 5)} of 2400 = 480", x=80, y=300, color=BLUE), MATH(f"{F(1, 3)} of 480 = 160", x=80, y=450, color=GREEN, at=2.6)]),
        PAUSE("7.5-k3", "Your turn. Work out 1 twentieth of 1,800. Pause and work it out.", "Work out 1/20 of 1800."),
    ]),
    dict(kind="example", title="Check: 1/20 of 1800", steps=[
        dict(say="20 is 10 times 2. 1 tenth of 1,800 is 180. Half of 180 is 90.", do=[MATH(f"{F(1, 10)} of 1800 = 180", x=80, y=170, color=BLUE), MATH(f"{F(1, 2)} of 180 = 90", x=80, y=330, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Cancelling", steps=[
        dict(say="Work out 18 over 25, times 35 over 36.", do=[MATH(f"{F(18, 25)} × {F(35, 36)}", x=80, y=150)]),
        dict(say="Cancel 18 and 36. They become 1 and 2.", do=[MATH(f"{F(1, 25)} × {F(35, 2)}", x=80, y=300, color=BLUE)]),
        dict(say="Cancel 35 and 25. They become 7 and 5.", do=[MATH(f"{F(1, 5)} × {F(7, 2)}", x=420, y=300, color=BLUE)]),
        dict(say="1 fifth times 7 halves is 7 tenths.", do=[MATH(f"= {F(7, 10)}", x=80, y=450, color=GREEN)]),
    ]),
    dict(kind="example", title="Order of operations", steps=[
        dict(say="Work out 2 thirds, plus 1 third times 3 quarters.", do=[MATH(f"{F(2, 3)} + {F(1, 3)} × {F(3, 4)}", x=80, y=150)]),
        dict(say="Multiply first. 1 third times 3 quarters is 1 quarter.", do=[MATH(f"{F(1, 3)} × {F(3, 4)} = {F(1, 4)}", x=80, y=300, color=BLUE)]),
        dict(say="Then add. 2 thirds plus 1 quarter is 8 twelfths plus 3 twelfths, which is 11 twelfths.", do=[MATH(f"{F(2, 3)} + {F(1, 4)} = {F(8, 12)} + {F(3, 12)} = {F(11, 12)}", x=80, y=450, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ana works out 1 half, plus 1 half times 1 half. Which line is wrong?", do=LINES("Ana", "1/2 + 1/2 × 1/2", ["1/2 + 1/2 = 1", "1 × 1/2 = 1/2"])),
        dict(say="Line 1 is wrong. Ana added first. You must multiply before you add.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="1 half times 1 half is 1 quarter. Then 1 half plus 1 quarter is 3 quarters.", do=[MATH(f"{F(1, 2)} + {F(1, 4)} = {F(3, 4)}", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Ten per cent off", steps=[
        dict(say="You can use these tricks in any shop. A sign says 10 percent off. That means you pay 9 tenths of the price.", do=[E("🏷️", 90, 160, 100), MATH(f"10% off → pay {F(9, 10)}", x=230, y=165)]),
        dict(say="A pair of trainers costs 70 dollars. 1 tenth is 7 dollars.", do=[E("👟", 90, 310, 90), MATH(f"{F(1, 10)} of 70 = 7", x=230, y=310)]),
        dict(say="70 minus 7 is 63. You pay 63 dollars. No written calculation needed.", do=[MATH("70 − 7 = 63", x=230, y=460, color=BLUE), B("$63", x=560, y=452, color=GREEN, at=2)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("7.5-k4", "One last question. Work out 1 third, plus 2 thirds times 1 half. Pause the video and answer.", "1/3 + 2/3 × 1/2 = ?"),
        dict(say="Multiply first. 2 thirds times 1 half is 1 third. Then 1 third plus 1 third is 2 thirds.", do=[MATH(f"{F(2, 3)} × {F(1, 2)} = {F(1, 3)}", x=80, y=170, color=BLUE), MATH(f"{F(1, 3)} + {F(1, 3)} = {F(2, 3)}", x=80, y=330, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: for a fraction close to 1, use the whole minus the small part.", do=[T("• Close to 1: whole − small part", x=80, y=170)]),
        dict(say="Split denominators into factors. 1 twelfth is 1 third of 1 quarter.", do=[T("• Split denominators: 1/12 = 1/3 of 1/4", x=80, y=250)]),
        dict(say="Cancel before multiplying, and re-order when it helps.", do=[T("• Cancel first; re-order", x=80, y=330)]),
        dict(say="And always follow the order of operations.", do=[T("• Follow the order of operations", x=80, y=410)]),
    ]),
]
