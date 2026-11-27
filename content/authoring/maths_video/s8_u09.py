# -*- coding: utf-8 -*-
"""Stage 8 · Unit 9 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u09 import SEQ, MACH, CELLS, NT, MAP
from .s7_u11 import MACH2

# matchstick squares in a row: n squares use 3n + 1 sticks
STICKS = lambda n, x=640, y=170, at=0, c="#8A5A00": T(f'<svg viewBox="0 0 {60 * n + 20} 80" width="{60 * n + 20}" height="80">' + "".join(
    f'<line x1="{10 + 60 * i}" y1="10" x2="{70 + 60 * i}" y2="10" stroke="{c}" stroke-width="6" stroke-linecap="round"/><line x1="{10 + 60 * i}" y1="70" x2="{70 + 60 * i}" y2="70" stroke="{c}" stroke-width="6" stroke-linecap="round"/><line x1="{70 + 60 * i}" y1="10" x2="{70 + 60 * i}" y2="70" stroke="{c}" stroke-width="6" stroke-linecap="round"/>'
    for i in range(n)) + f'<line x1="10" y1="10" x2="10" y2="70" stroke="{c}" stroke-width="6" stroke-linecap="round"/></svg>', x=x, y=y, at=at)

VIDEOS = {}

VIDEOS["9.1"] = [
    dict(kind="hook", title="Two ways to save", steps=[
        dict(say="Ana saves 5 dollars more each week than the week before, starting with 5 dollars. Ben doubles his savings each week, starting with 1 dollar.",
             do=[E("🐷", 90, 170, 100), T("Ana: **+ $5** each week · Ben: **× 2** each week", x=230, y=200)]),
        dict(say="Ana's amounts go 5, 10, 15, 20, 25. Ben's go 1, 2, 4, and so on.", do=[SEQ(["5", "10", "15", "20", "25"], x=230, y=290), SEQ(["1", "2", "4", "?", "?"], x=230, y=390, at=3)]),
        PAUSE("9.1-k1", "How much does Ben save in week 5? Pause the video and work it out.", "Ben doubles from $1. Week 5?"),
    ]),
    dict(kind="hook", title="Doubling wins", steps=[
        dict(say="Ben's amounts are 1, 2, 4, 8 and 16. In week 5, Ana saves more. But by week 10 Ben saves 512 dollars, and Ana only 50.",
             do=[SEQ(["1", "2", "4", "8", "16"], x=80, y=180, c=GREEN), T("week 10: Ana **$50** · Ben **$512**", x=80, y=300, at=6)]),
    ]),
    dict(kind="recall", title="Term-to-term rules", steps=[
        dict(say="Remember: a term-to-term rule tells you how to get from one term to the next. Start at 50, and subtract 6: 50, 44, 38, 32.",
             do=[T("start **50**, rule **− 6**", x=80, y=170), SEQ(["50", "44", "38", "32"], x=80, y=250)]),
    ]),
    dict(kind="idea", title="Linear and non-linear", steps=[
        dict(say="A linear sequence goes up, or down, by the same amount each time. Ana's savings go up by 5 each week.", do=[T("**linear**: same difference each time", x=80, y=170), SEQ(["5", "10", "15", "20", "25"], x=80, y=240)]),
        dict(say="A non-linear sequence does not. Ben's savings double. And the square numbers, 1, 4, 9, 16, go up by 3, then 5, then 7.",
             do=[T("**non-linear**: the difference changes", x=80, y=350), SEQ(["1", "4", "9", "16"], x=80, y=420, c=RED)]),
        PAUSE("9.1-k2", "Your turn. Is 3, 6, 12, 24 linear or non-linear? Pause the video and choose.", "3, 6, 12, 24 is …"),
    ]),
    dict(kind="idea", title="Check: 3, 6, 12, 24", steps=[
        dict(say="The differences are 3, 6 and 12. They are not the same, so the sequence is non-linear. It doubles each time.", do=[B("non-linear (× 2)", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Position-to-term rules", steps=[
        dict(say="A position-to-term rule gives any term straight from its position, n. Term equals 3 n plus 2 gives 5, 8, 11, and so on.",
             do=[MATH("term = 3n + 2", x=80, y=170), NT([5, 8, 11, 14, 17], y=250)]),
        dict(say="It is very useful for far terms. The 50th term is 3 times 50, plus 2, which is 152.", do=[MATH("n = 50: 3 × 50 + 2 = 152", x=80, y=420, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I generate a sequence?", steps=[
        dict(say="Here is the method. Step 1: for a term-to-term rule, start with the first term, and apply the rule again and again.", do=[T("1. Term-to-term: apply the rule **again and again**", x=80, y=170)]),
        dict(say="Step 2: for a position-to-term rule, put n equals 1, 2, 3, and so on into the rule.", do=[T("2. Position-to-term: put in **n = 1, 2, 3 …**", x=80, y=260)]),
        dict(say="Step 3: check the differences. The same difference means linear. Otherwise it is non-linear.", do=[T("3. Same difference → **linear**", x=80, y=350)]),
        dict(say="Step 4: use the position-to-term rule for terms far along.", do=[T("4. Far terms: use the **position-to-term** rule", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A two-step rule", steps=[
        dict(say="Start at 4. The rule is: halve, then add 6. Half of 4 is 2, and 2 plus 6 is 8. Half of 8 is 4, plus 6 is 10. Half of 10 is 5, plus 6 is 11.",
             do=[T("start **4**, rule **÷ 2 then + 6**", x=80, y=170), SEQ(["4", "8", "10", "11"], x=80, y=260, c=GREEN)]),
    ]),
    dict(kind="example", title="A squared rule", steps=[
        dict(say="The rule is: term equals n squared, plus 1. Put in n equals 1, 2, 3, 4. That gives 2, 5, 10 and 17. The 10th term is 10 squared plus 1, which is 101.",
             do=[MATH("term = n² + 1", x=80, y=170), SEQ(["2", "5", "10", "17"], x=80, y=260), MATH("10th: 10² + 1 = 101", x=80, y=380, color=GREEN, at=7)]),
        PAUSE("9.1-k3", "Your turn. The rule is: term equals 2 n squared. What is the 3rd term? Pause and work it out.", "Term = 2n². 3rd term?"),
    ]),
    dict(kind="example", title="Check: 2n²", steps=[
        dict(say="Put n equals 3. 3 squared is 9, and 2 times 9 is 18. Square first, then multiply.", do=[MATH("2 × 3² = 2 × 9 = 18", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Halving", steps=[
        dict(say="Start at 200, and the rule is divide by 2. When does the sequence first go below 10? 200, 100, 50, 25, 12.5, then 6.25. The 6th term is the first below 10.",
             do=[SEQ(["200", "100", "50", "25", "12.5", "6.25"], x=80, y=200), B("6th term (6.25)", x=80, y=330, color=GREEN, at=9)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Start at 5. The term-to-term rule is times 3. Lucy finds the third term. Which line is wrong?", do=LINES("Lucy", "start 5, rule × 3: the third term", ["third term = 3 × 3 = 9"])),
        dict(say="Line 1 is wrong. A term-to-term rule is applied to the previous term, not to the position number.", do=[dict(a="cross", id="l1")]),
        dict(say="5, then 15, then 45. The third term is 45.", do=[SEQ(["5", "15", "45"], x=110, y=360, c=GREEN)]),
    ]),
    dict(kind="life", title="Paper folding", steps=[
        dict(say="Fold a sheet of paper in half, and it gets twice as thick. Each fold doubles it. That is a non-linear sequence: 1, 2, 4, 8 layers, and so on.",
             do=[E("📄", 90, 170, 100), SEQ(["1", "2", "4", "8", "16"], x=230, y=180)]),
        dict(say="After just 7 folds there are 128 layers, and the paper is too thick to fold again. Doubling grows very fast.", do=[T("7 folds → **128** layers!", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("9.1-k4", "One last question. Start at 1. The rule is times 2, plus 1. What is the 4th term? Pause the video and answer.", "Start 1, rule '× 2 + 1'. 4th term?"),
        dict(say="1, then 2 plus 1 is 3, then 6 plus 1 is 7, then 14 plus 1 is 15. The 4th term is 15.", do=[SEQ(["1", "3", "7", "15"], x=80, y=200, c=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: term-to-term rules use the previous term. Position-to-term rules use the position, n.", do=[T("• Term-to-term: previous term · position-to-term: **n**", x=80, y=170)]),
        dict(say="Linear sequences have a constant difference. Non-linear ones do not.", do=[T("• Linear: constant difference", x=80, y=250)]),
        dict(say="Two-step rules combine two operations.", do=[T("• Two-step rules combine operations", x=80, y=330)]),
        dict(say="Use position-to-term rules for terms far along the sequence.", do=[T("• Far terms: position-to-term rule", x=80, y=410)]),
    ]),
]

VIDEOS["9.2"] = [
    dict(kind="hook", title="Fence panels", steps=[
        dict(say="A fence is built from wooden pieces. 1 panel uses 4 pieces of wood. 2 panels use 7. 3 panels use 10.",
             do=[STICKS(1, x=80, y=170), STICKS(2, x=260, y=170, at=1.5), STICKS(3, x=500, y=170, at=3), SEQ(["4", "7", "10"], x=80, y=300, at=4)]),
        PAUSE("9.2-k1", "How many pieces of wood for 10 panels? Pause the video and work it out.", "Wood for 10 panels (4, 7, 10, …)?"),
    ]),
    dict(kind="hook", title="Add 3 each time", steps=[
        dict(say="Each new panel adds 3 pieces. From 3 panels to 10 panels is 7 more panels, so 7 times 3 more pieces. 10 plus 21 is 31.",
             do=[MATH("10 + 7 × 3 = 31", x=80, y=200, color=GREEN)]),
        dict(say="Can we find a rule that works for any number of panels?", do=[T("a rule for **any** number of panels?", x=80, y=310)]),
    ]),
    dict(kind="recall", title="Differences", steps=[
        dict(say="Remember: in 6, 11, 16, 21, the difference is 5 each time. So the next term is 26.", do=[SEQ(["6", "11", "16", "21", "26"], x=80, y=200), T("+5 each time", x=80, y=320, color=BLUE)]),
    ]),
    dict(kind="idea", title="From pattern to rule", steps=[
        dict(say="The difference tells you the multiplier. The pieces go up by 3, so the rule has 3 times n.",
             do=[TBL(["Position n", "1", "2", "3", "4"], [["3n", "3", "6", "9", "12"], ["Pieces", "4", "7", "10", "13"]], y=170), ROW(0, 3)]),
        dict(say="Compare: 3 times 1 is 3, but the first term is 4. So add 1. The rule is 3 n plus 1.", do=[ROW(1, 0.4), B("pieces = 3n + 1", x=80, y=400, color=GREEN, at=4)]),
        dict(say="It fits the picture: each panel adds 3 pieces, plus 1 extra piece at the start.", do=[STICKS(3, x=700, y=400)]),
        PAUSE("9.2-k2", "Your turn. Find the rule for 2, 8, 14, 20. Pause the video and try it.", "Rule for 2, 8, 14, 20."),
    ]),
    dict(kind="idea", title="Check: 2, 8, 14, 20", steps=[
        dict(say="The difference is 6, so start with 6 n. 6 times 1 is 6, but the first term is 2. So subtract 4. The rule is 6 n minus 4.",
             do=[MATH("6 × 1 = 6 → 2: subtract 4", x=80, y=190), B("6n − 4", x=80, y=290, color=GREEN, at=6)]),
    ]),
    dict(kind="method", title="How do I find the rule?", steps=[
        dict(say="Here is the method. Step 1: count the terms for patterns 1, 2, 3 and 4.", do=[T("1. Count patterns 1, 2, 3, 4", x=80, y=170)]),
        dict(say="Step 2: find the difference. If it is constant, the sequence is linear.", do=[T("2. Find the **difference** d", x=80, y=260)]),
        dict(say="Step 3: compare with d times n, and add or subtract to fit.", do=[T("3. Compare with **d × n**; add or subtract", x=80, y=350)]),
        dict(say="Step 4: check with another term, and link the rule to the pattern.", do=[T("4. **Check** with another term", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Going down", steps=[
        dict(say="Find the rule for 20, 17, 14, 11. The difference is negative 3, so start with negative 3 n.", do=[SEQ(["20", "17", "14", "11"], x=80, y=170), MATH("d = −3 → −3n", x=80, y=280)]),
        dict(say="When n is 1, negative 3 n is negative 3. To get 20, add 23. The rule is 23 minus 3 n.", do=[B("23 − 3n", x=80, y=380, color=GREEN)]),
        PAUSE("9.2-k3", "Your turn. Find the rule for 30, 26, 22, 18. Pause and work it out.", "Rule for 30, 26, 22, 18."),
    ]),
    dict(kind="example", title="Check: 30, 26, 22, 18", steps=[
        dict(say="The difference is negative 4. Negative 4 times 1 is negative 4. To get 30, add 34. The rule is 34 minus 4 n.", do=[B("34 − 4n", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Is it in the sequence?", steps=[
        dict(say="Is 100 a term of 3 n plus 1? Set 3 n plus 1 equal to 100. 3 n equals 99, so n equals 33. That is a whole number, so yes. It is the 33rd term.",
             do=[MATH("3n + 1 = 100 → n = 33", x=80, y=190), B("yes: the 33rd term", x=80, y=300, color=GREEN, at=7)]),
    ]),
    dict(kind="example", title="Square patterns", steps=[
        dict(say="Dots are arranged in squares: 1, 4, 9, 16. Each pattern is n dots by n dots, so the rule is n squared. Not every rule is linear.",
             do=[CELLS([[0, 0]], x=80, y=200, w=120), CELLS([[0, 0], [1, 0], [0, 1], [1, 1]], x=240, y=200, w=160, at=1), CELLS([[i, j] for i in range(3) for j in range(3)], x=440, y=200, w=200, at=2), B("n²", x=80, y=420, color=GREEN, at=5)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Jack finds the rule for 7, 12, 17, 22. Which line goes wrong first?", do=LINES("Jack", "the rule for 7, 12, 17, 22", ["the difference is 5", "rule: n + 5"])),
        dict(say="Line 2 is wrong. The difference is the number that multiplies n. It should start with 5 n.", do=[dict(a="cross", id="l2")]),
        dict(say="5 times 1 is 5, and the first term is 7, so add 2. The rule is 5 n plus 2.", do=[B("5n + 2", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Fencing a field", steps=[
        dict(say="A farmer builds a straight fence. Each section is 3 metres long, with a post at each end. 1 section needs 2 posts, 2 sections need 3, 3 sections need 4.",
             do=[E("🐄", 90, 170, 100), SEQ(["2", "3", "4"], x=230, y=180)]),
        dict(say="The rule is n plus 1 posts. So a 30 section fence needs 31 posts, not 30. Forgetting the extra post is a famous mistake!", do=[B("posts = n + 1", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("9.2-k4", "One last question. Is 62 a term of 6 n plus 2? Pause the video and choose.", "Is 62 in 6n + 2?"),
        dict(say="6 n plus 2 equals 62, so 6 n equals 60, and n equals 10. A whole number, so yes. It is the 10th term.", do=[MATH("6n = 60 → n = 10", x=80, y=190), B("yes – n = 10", x=80, y=300, color=GREEN, at=5)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a constant difference d means a linear sequence. The rule is d n plus c.", do=[T("• Constant difference d → **dn + c**", x=80, y=170)]),
        dict(say="Find c by comparing d times 1 with the first term.", do=[T("• Find c: compare d × 1 with the first term", x=80, y=250)]),
        dict(say="Check with another term.", do=[T("• Check with another term", x=80, y=330)]),
        dict(say="Link the rule to the pattern.", do=[T("• Link the rule to the pattern", x=80, y=410)]),
    ]),
]

VIDEOS["9.3"] = [
    dict(kind="hook", title="Cinema seats", steps=[
        dict(say="Row 1 of a cinema has 12 seats. Each row has 3 more seats than the row in front.", do=[E("🎬", 90, 170, 100), SEQ(["12", "15", "18", "21"], x=230, y=180)]),
        PAUSE("9.3-k1", "How many seats are there in row 25? Pause the video and work it out.", "Seats in row 25 (12, 15, 18, …)?"),
    ]),
    dict(kind="hook", title="Row 25", steps=[
        dict(say="The difference is 3, so start with 3 n. 3 times 1 is 3, but row 1 has 12, so add 9. The rule is 3 n plus 9.", do=[MATH("seats = 3n + 9", x=80, y=190)]),
        dict(say="For row 25: 3 times 25 is 75, plus 9 is 84 seats.", do=[B("3 × 25 + 9 = 84", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="recall", title="Position-to-term", steps=[
        dict(say="Remember: a position-to-term rule gives a term from its position. Term equals 3 times the position plus 9 gives 12, 15, 18, and so on.", do=[NT([12, 15, 18, 21, 24], y=200)]),
    ]),
    dict(kind="idea", title="The n-th term", steps=[
        dict(say="The n-th term is the position-to-term rule written in algebra. For 12, 15, 18, 21, the n-th term is 3 n plus 9.", do=[B("nth term = 3n + 9", x=80, y=170, color=BLUE)]),
        dict(say="It lets you find any term. And it lets you find the position of a term. Which row has 105 seats? 3 n plus 9 equals 105. 3 n equals 96, so n equals 32. Row 32.",
             do=[MATH("3n + 9 = 105 → 3n = 96 → n = 32", x=80, y=290, color=GREEN)]),
        PAUSE("9.3-k2", "Your turn. Find the n-th term of 2, 9, 16, 23. Pause the video and try it.", "nth term of 2, 9, 16, 23?"),
    ]),
    dict(kind="idea", title="Check: 2, 9, 16, 23", steps=[
        dict(say="The difference is 7, so 7 n. 7 times 1 is 7, and the first term is 2, so subtract 5. The n-th term is 7 n minus 5.", do=[B("7n − 5", x=80, y=200, color=GREEN)]),
        dict(say="To find the first term above a value, solve an inequality. Which is the first row with more than 100 seats? 3 n plus 9 is greater than 100, so n is greater than 30.33. That is row 31, with 102 seats.",
             do=[MATH("3n + 9 > 100 → n > 30.3…", x=80, y=310), B("row 31 (102 seats)", x=80, y=410, color=GREEN, at=9)]),
    ]),
    dict(kind="method", title="How do I find and use the n-th term?", steps=[
        dict(say="Here is the method. Step 1: find the common difference, d.", do=[T("1. Find the common difference **d**", x=80, y=170)]),
        dict(say="Step 2: write d n, then add or subtract to match the first term.", do=[T("2. Write **dn**, then add or subtract", x=80, y=260)]),
        dict(say="Step 3: substitute n to find terms. Solve an equation to find a position.", do=[T("3. Substitute to find terms; **solve** to find a position", x=80, y=350)]),
        dict(say="Step 4: check with a term you know.", do=[T("4. **Check** with a known term", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Negative terms", steps=[
        dict(say="Find the n-th term of negative 8, negative 3, 2, 7. The difference is 5, so 5 n. 5 times 1 is 5. To get negative 8, subtract 13. The n-th term is 5 n minus 13.",
             do=[SEQ(["−8", "−3", "2", "7"], x=80, y=170), B("5n − 13", x=80, y=300, color=GREEN, at=8)]),
        dict(say="Which term is 132? 5 n minus 13 equals 132. 5 n equals 145, so n equals 29. It is the 29th term.", do=[MATH("5n − 13 = 132 → n = 29", x=80, y=410)]),
        PAUSE("9.3-k3", "Your turn. Which term of 3 n plus 9 is 90? Pause and work it out.", "Which term of 3n + 9 is 90?"),
    ]),
    dict(kind="example", title="Check: 3n + 9 = 90", steps=[
        dict(say="3 n plus 9 equals 90. Subtract 9: 3 n equals 81. Divide by 3: n equals 27. It is the 27th term, just like the cinema row.", do=[MATH("3n = 81", x=80, y=190), B("n = 27", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Going down", steps=[
        dict(say="Find the n-th term of 50, 46, 42, 38, and its 15th term. The difference is negative 4. 50 minus negative 4 is 54, so the n-th term is 54 minus 4 n.",
             do=[SEQ(["50", "46", "42", "38"], x=80, y=170), MATH("54 − 4n", x=80, y=290, at=7)]),
        dict(say="The 15th term is 54 minus 60, which is negative 6.", do=[B("15th: 54 − 60 = −6", x=80, y=390, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Eva finds the n-th term of 9, 14, 19, 24. Which line goes wrong first?", do=LINES("Eva", "the nth term of 9, 14, 19, 24", ["d = 5", "nth term = 5n + 9"])),
        dict(say="Line 2 is wrong. 5 n plus 9 gives 14 when n is 1, not 9. She added the first term instead of comparing.", do=[dict(a="cross", id="l2")]),
        dict(say="5 times 1 is 5. To get 9, add 4. The n-th term is 5 n plus 4.", do=[B("5n + 4", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Taxi fares", steps=[
        dict(say="Some taxi fares are a sequence. A ride starts at 4 dollars, and each kilometre adds 2 dollars. After n kilometres, the fare is 2 n plus 4 dollars.",
             do=[E("🚖", 90, 170, 100), MATH("fare = 2n + 4", x=230, y=190)]),
        dict(say="How far can you go for 30 dollars? 2 n plus 4 equals 30 gives n equals 13 kilometres.", do=[MATH("2n + 4 = 30 → n = 13 km", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("9.3-k4", "One last question. What is the 20th term of 100 minus 3 n? Pause the video and answer.", "20th term of 100 − 3n?"),
        dict(say="Put n equals 20. 3 times 20 is 60, and 100 minus 60 is 40.", do=[MATH("100 − 3 × 20", x=80, y=190), B("= 40", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the n-th term of a linear sequence is d n plus c, where c is the first term minus d.", do=[T("• nth term = dn + c (c = first term − d)", x=80, y=170)]),
        dict(say="Substitute to find terms.", do=[T("• Substitute to find terms", x=80, y=250)]),
        dict(say="Solve the n-th term equal to a value to find its position. A whole number n means it is in the sequence.", do=[T("• Solve to find a position (whole n → in it)", x=80, y=330)]),
        dict(say="Use inequalities to find the first term over a value.", do=[T("• Inequalities for 'the first term over …'", x=80, y=410)]),
    ]),
]

VIDEOS["9.4"] = [
    dict(kind="hook", title="Exchange rates", steps=[
        dict(say="A travel app changes dollars into euros with a rule: euros equals dollars times 0.9. Going back, it must undo that rule.",
             do=[E("💱", 90, 170, 100), MACH("$", "× 0.9", "€", x=230, y=190)]),
        PAUSE("9.4-k1", "What rule changes euros back into dollars? Pause the video and choose.", "Euros back to dollars is …"),
    ]),
    dict(kind="hook", title="Undo it", steps=[
        dict(say="The opposite of times 0.9 is divide by 0.9. So 90 euros is 90 divided by 0.9, which is 100 dollars.", do=[MACH("€", "÷ 0.9", "$", x=80, y=190), MATH("90 ÷ 0.9 = 100", x=80, y=320, color=GREEN)]),
    ]),
    dict(kind="recall", title="Function machines", steps=[
        dict(say="Remember: a function machine does each step in order. Input 4, times 3, then plus 5, gives 17.", do=[MACH2("4", "× 3", "+ 5", "17", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Different forms", steps=[
        dict(say="A function can be shown as a machine, as a table, as a mapping diagram, or as an equation. This machine is times 2, then plus 3.",
             do=[MACH2("x", "× 2", "+ 3", "y", x=80, y=160), TBL(["x", "1", "2", "3", "4"], [["y = 2x + 3", "5", "7", "9", "11"]], y=280), ROW(0, 5)]),
        dict(say="As an equation, it is y equals 2 x plus 3. On a mapping diagram, arrows join each input to its output.", do=[MAP([[1, 5], [2, 7], [3, 9]], x=700, y=260, w=500, mx=12)]),
        PAUSE("9.4-k2", "Your turn. Using y equals 2 x plus 3, find y when x is 10. Pause the video and try it.", "y = 2x + 3. y when x = 10?"),
    ]),
    dict(kind="idea", title="Check: x = 10", steps=[
        dict(say="2 times 10 is 20, and 20 plus 3 is 23.", do=[MACH2("10", "× 2", "+ 3", "23", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Inverse functions", steps=[
        dict(say="The inverse undoes the function. Reverse the order, and use the opposite operations. Times 2, then plus 3, becomes minus 3, then divide by 2.",
             do=[MACH2("y", "− 3", "÷ 2", "x", x=80, y=180)]),
        dict(say="Check: an output of 11. 11 minus 3 is 8, and 8 divided by 2 is 4. That was the input.", do=[MACH2("11", "− 3", "÷ 2", "4", x=80, y=320), T("✓ back to the input", x=80, y=440, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I work with functions?", steps=[
        dict(say="Here is the method. Step 1: apply the steps of the machine in order.", do=[T("1. Apply the steps **in order**", x=80, y=170)]),
        dict(say="Step 2: write the function as an equation, y equals something.", do=[T("2. Write it as **y = …**", x=80, y=260)]),
        dict(say="Step 3: for the inverse, reverse the order and use the inverse operations.", do=[T("3. Inverse: **reverse** the order, **opposite** operations", x=80, y=350)]),
        dict(say="Step 4: check by going there and back.", do=[T("4. **Check**: there and back", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="An equation from a machine", steps=[
        dict(say="The machine is plus 4, then times 3. Write y in terms of x. Adding 4 gives x plus 4. Then the whole of that is multiplied by 3.",
             do=[MACH2("x", "+ 4", "× 3", "y", x=80, y=170)]),
        dict(say="So y equals 3, bracket, x plus 4. The bracket shows that adding came first.", do=[B("y = 3(x + 4)", x=80, y=310, color=GREEN)]),
    ]),
    dict(kind="example", title="From a table", steps=[
        dict(say="A table shows x equals 1, 2, 3, and y equals 1, 4, 7. y goes up by 3, so start with 3 x. 3 times 1 is 3, but y is 1, so subtract 2. y equals 3 x minus 2.",
             do=[TBL(["x", "1", "2", "3"], [["y", "1", "4", "7"]], y=170), ROW(0, 0.5), B("y = 3x − 2", x=80, y=330, color=GREEN, at=8)]),
        PAUSE("9.4-k3", "Your turn. Using the inverse of y equals 2 x plus 3, find x when y is 23. Pause and work it out.", "Inverse of y = 2x + 3: x when y = 23?"),
    ]),
    dict(kind="example", title="Check: y = 23", steps=[
        dict(say="Use the inverse: minus 3, then divide by 2. 23 minus 3 is 20, and 20 divided by 2 is 10.", do=[MACH2("23", "− 3", "÷ 2", "10", x=80, y=200)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Rosa finds the inverse of: times 2, then plus 6. Which line is wrong?", do=LINES("Rosa", "the inverse of × 2 then + 6", ["÷ 2 then − 6"])),
        dict(say="Line 1 is wrong. She used the opposite operations, but not in the reverse order. Undo the last step first.", do=[dict(a="cross", id="l1")]),
        dict(say="The inverse is minus 6, then divide by 2. Check with 1: 1 times 2 plus 6 is 8. 8 minus 6 is 2, divided by 2 is 1.", do=[B("− 6 then ÷ 2", x=110, y=360, color=GREEN)]),
    ]),
    dict(kind="life", title="Oven temperatures", steps=[
        dict(say="Recipes from different countries use different units. To change Celsius to Fahrenheit: times 1.8, then plus 32.", do=[E("🍰", 90, 170, 100), MACH2("°C", "× 1.8", "+ 32", "°F", x=230, y=190)]),
        dict(say="The inverse is minus 32, then divide by 1.8. So an oven at 356 degrees Fahrenheit is 180 degrees Celsius.", do=[MACH2("356", "− 32", "÷ 1.8", "180", x=230, y=320)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("9.4-k4", "One last question. What is the inverse of add 7? Pause the video and choose.", "Inverse of 'add 7' is …"),
        dict(say="The inverse of add 7 is subtract 7.", do=[B("subtract 7", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a function can be a machine, a table, a mapping diagram or an equation.", do=[T("• Machine, table, mapping diagram, equation", x=80, y=170)]),
        dict(say="Brackets show which step came first.", do=[T("• Brackets show which step came first", x=80, y=250)]),
        dict(say="The inverse reverses the order, and uses the inverse operations.", do=[T("• Inverse: reverse order, inverse operations", x=80, y=330)]),
        dict(say="Check by going there and back.", do=[T("• Check: there and back", x=80, y=410)]),
    ]),
]
