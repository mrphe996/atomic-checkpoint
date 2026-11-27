# -*- coding: utf-8 -*-
"""Stage 7 · Unit 9 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG
from .s7_u04 import TBL, ROW
from .s7_u05 import BIG

BOX = lambda s, c="#1F2A37", bg="#fff", w=92: f'<span style="display:inline-flex;align-items:center;justify-content:center;width:{w}px;height:66px;margin-right:14px;border:3px solid {c};border-radius:12px;background:{bg};color:{c};font-weight:700">{s}</span>'
SEQ = lambda terms, x=80, y=200, at=0, c="#1F2A37": T("".join(BOX(t, c) for t in terms), x=x, y=y, at=at)          # a row of term boxes
ARROW = '<span style="margin-right:14px;font-weight:700">→</span>'
MACH = lambda i, op, o, x=80, y=200, at=0: T(BOX(i, w=120) + ARROW + BOX(op, "#8A5A00", "#FFF6D6", 130) + ARROW + BOX(o, w=120), x=x, y=y, at=at)   # a function machine
CELLS = lambda cells, x=640, y=130, w=600, at=0, **k: FIG(x, y, w, at, kind="cells", cells=cells, **k)
L3 = [[0, 3], [1, 3], [0, 2], [3, 3], [4, 3], [5, 3], [3, 2], [3, 1], [7, 3], [8, 3], [9, 3], [10, 3], [7, 2], [7, 1], [7, 0]]   # L-shaped patterns 1 to 3

VIDEOS = {}

VIDEOS["9.1"] = [
    dict(kind="hook", title="Lena's money box", steps=[
        dict(say="Lena puts 6 dollars in a money box in week 1. Every week after that, she adds 5 dollars.", do=[E("🐷", 90, 160, 110), T("week 1: **$6** · then **$5** more each week", x=240, y=200)]),
        PAUSE("9.1-k1", "How much is in the box at the end of week 4? Pause the video and work it out.", "Week 1: $6. She adds $5 every week. How much at the end of week 4?"),
    ]),
    dict(kind="hook", title="Week by week", steps=[
        dict(say="Week 1: 6 dollars. Week 2: 6 plus 5 is 11. Week 3: 11 plus 5 is 16. Week 4: 16 plus 5 is 21.", do=[SEQ(["6"], 80), SEQ(["11"], 186, at=2.6), SEQ(["16"], 292, at=5.4), SEQ(["21"], 398, at=8.2, c=GREEN), T("+5 each week", x=80, y=300, color=BLUE, at=2.6)]),
        dict(say="At the end of week 4, there are 21 dollars in the box.", do=[B("$21", x=80, y=400, color=GREEN)]),
    ]),
    dict(kind="recall", title="Undoing an operation", steps=[
        dict(say="Remember: every operation has an inverse, which undoes it. Add and subtract undo each other.", do=[T("**add** ↔ **subtract**", x=80, y=170), MATH("12 + 7 = 19 → 19 − 7 = 12", x=80, y=250)]),
        dict(say="Multiply and divide undo each other too.", do=[T("**multiply** ↔ **divide**", x=80, y=370), MATH("8 × 3 = 24 → 24 ÷ 3 = 8", x=80, y=450)]),
    ]),
    dict(kind="idea", title="What is a sequence?", steps=[
        dict(say="Lena's amounts make a list: 6, 11, 16, 21. A list of numbers in a set order is called a sequence.", do=[SEQ(["6", "11", "16", "21"], y=160), T("a **sequence**: numbers in a set order", x=560, y=180)]),
        dict(say="Each number in the list is a term. Every term has a position: first, second, third, fourth.",
             do=[TBL(["Position", "1st", "2nd", "3rd", "4th"], [["Term", "6", "11", "16", "21"]], y=290), ROW(0, 3)]),
        dict(say="The position tells you where the term is. The value is the number itself. The 3rd term has the value 16.", do=[T("**position**: where it is · **value**: the number", x=80, y=460), B("3rd term = 16", x=80, y=540, color=BLUE, at=4)]),
        PAUSE("9.1-k2", "Now think about this. A sequence starts 2, 4. What is the next term? Pause the video and decide.", "A sequence starts 2, 4, … What is the next term?"),
    ]),
    dict(kind="idea", title="Check: two terms are not enough", steps=[
        dict(say="You cannot tell from two terms. The rule could be add 2, which gives 2, 4, 6.", do=[SEQ(["2", "4", "6"], y=170), T("add 2", x=440, y=190, color=BLUE)]),
        dict(say="Or the rule could be multiply by 2, which gives 2, 4, 8. Both rules fit.", do=[SEQ(["2", "4", "8"], y=290), T("multiply by 2", x=440, y=310, color=RED)]),
        dict(say="With 3 or more terms, you can test a rule, and be sure.", do=[B("use 3 or more terms", x=80, y=440, color=GREEN)]),
    ]),
    dict(kind="idea", title="Term-to-term rules", steps=[
        dict(say="A term-to-term rule tells you how to get from one term to the next term.", do=[T("**Term-to-term rule**: from one term to the **next**", x=80, y=160)]),
        dict(say="To build a sequence, you need 2 things: the first term, and the rule.", do=[T("you need the **first term** and the **rule**", x=80, y=240)]),
        dict(say="First term 9, rule add 6. 9 plus 6 is 15. 15 plus 6 is 21. 21 plus 6 is 27.", do=[SEQ(["9"], 80, 350), SEQ(["15"], 186, 350, at=2.4), SEQ(["21"], 292, 350, at=4.6), SEQ(["27"], 398, 350, at=6.8), T("+6", x=560, y=370, color=BLUE)]),
        PAUSE("9.1-k3", "Your turn. A sequence starts at 5, and the rule is add 4. What is the 4th term? Pause the video and try it.", "A sequence starts at 5 and the rule is 'add 4'. What is the 4th term?"),
    ]),
    dict(kind="idea", title="Check: start at 5, add 4", steps=[
        dict(say="5, then 9, then 13, then 17. The 4th term is 17.", do=[SEQ(["5"], 80), SEQ(["9"], 186, at=1), SEQ(["13"], 292, at=2), SEQ(["17"], 398, at=3, c=GREEN), B("4th term = 17", x=80, y=340, color=GREEN, at=4)]),
    ]),
    dict(kind="idea", title="Other rules", steps=[
        dict(say="A rule is not always add. Each of these sequences starts at 60. Subtract 8 gives 60, 52, 44, 36.",
             do=[TBL(["Rule", "Sequence"], [["subtract 8", "60, 52, 44, 36, …"], ["divide by 2", "60, 30, 15, 7.5, …"], ["multiply by 2", "60, 120, 240, 480, …"]], y=190), ROW(0, 4)]),
        dict(say="Divide by 2 gives 60, 30, 15, 7.5.", do=[ROW(1, 0.3)]),
        dict(say="And multiply by 2 gives 60, 120, 240, 480.", do=[ROW(2, 0.3)]),
    ]),
    dict(kind="method", title="How do I find a missing term?", steps=[
        dict(say="Here is the method. Step 1: find the rule, or read it from the question.", do=[T("1. Find the **rule**", x=80, y=170)]),
        dict(say="Step 2: find a term you know, next to the gap.", do=[T("2. Find a known term **next to the gap**", x=80, y=260)]),
        dict(say="Step 3: to move right, to a later term, use the rule. To move left, to an earlier term, use the inverse.", do=[T("3. Move right → the **rule** · move left ← the **inverse**", x=80, y=350)]),
        dict(say="Step 4: check by running the rule along the whole sequence.", do=[T("4. **Check** the whole sequence", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A multiplying rule", steps=[
        dict(say="The first term is 5. The rule is multiply by 3. Write the first 4 terms.", do=[T("first term **5** · rule **× 3**", x=80, y=160)]),
        dict(say="5 times 3 is 15. 15 times 3 is 45. 45 times 3 is 135.", do=[SEQ(["5"], 80, 270), SEQ(["15"], 186, 270, at=1), SEQ(["45"], 292, 270, at=3.2), SEQ(["135"], 398, 270, at=5.4)]),
        dict(say="The sequence is 5, 15, 45, 135. Multiplying makes a sequence grow very quickly.", do=[B("5, 15, 45, 135", x=80, y=420, color=GREEN)]),
    ]),
    dict(kind="example", title="A rule with two steps", steps=[
        dict(say="The first term is 2. The rule is: multiply by 3, then subtract 1. Write the first 4 terms.", do=[T("first term **2** · rule **× 3, then − 1**", x=80, y=160)]),
        dict(say="2 times 3 is 6, subtract 1 is 5.", do=[MATH("2 × 3 − 1 = 5", x=80, y=260)]),
        dict(say="5 times 3 is 15, subtract 1 is 14. And 14 times 3 is 42, subtract 1 is 41.", do=[MATH("5 × 3 − 1 = 14", x=80, y=340), MATH("14 × 3 − 1 = 41", x=80, y=420, at=4)]),
        dict(say="The sequence is 2, 5, 14, 41.", do=[B("2, 5, 14, 41", x=80, y=520, color=GREEN)]),
    ]),
    dict(kind="example", title="Working backwards", steps=[
        dict(say="The rule is subtract 6. The 3rd term is 10. Find the first 4 terms. First, put 10 in the 3rd position.", do=[T("rule **− 6** · 3rd term is **10**", x=80, y=160), SEQ(["?", "?", "10", "?"], y=260)]),
        dict(say="To move right, use the rule. 10 minus 6 is 4. The 4th term is 4.", do=[MATH("10 − 6 = 4", x=640, y=260)]),
        dict(say="To move left, use the inverse: add 6. 10 plus 6 is 16, and 16 plus 6 is 22.", do=[MATH("10 + 6 = 16", x=640, y=350, color=BLUE), MATH("16 + 6 = 22", x=640, y=430, color=BLUE, at=3.4)]),
        dict(say="The sequence is 22, 16, 10, 4. Check: it goes down by 6 each time.", do=[SEQ(["22", "16", "10", "4"], y=520, c=GREEN)]),
    ]),
    dict(kind="example", title="Two missing terms", steps=[
        dict(say="Find the missing terms: 14, blank, blank, 38. The rule is add a number.", do=[SEQ(["14", "?", "?", "38"], y=160)]),
        dict(say="From 14 to 38 there are 3 steps. Count the gaps, not the boxes.", do=[T("**3 steps** from 14 to 38", x=80, y=280)]),
        dict(say="38 minus 14 is 24. 24 divided by 3 is 8. So the rule is add 8.", do=[MATH("38 − 14 = 24", x=80, y=360), MATH("24 ÷ 3 = 8", x=420, y=360, at=2.6)]),
        dict(say="14 plus 8 is 22, and 22 plus 8 is 30. Check: 30 plus 8 is 38.", do=[SEQ(["14", "22", "30", "38"], y=470, c=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="The rule is subtract 5. The 3rd term is 9. Find the 2nd term. Here is Dan's working. Which line goes wrong first?",
             do=LINES("Dan", "rule − 5, 3rd term 9, find the 2nd term", ["The rule is subtract 5", "To go back one place, subtract 5", "2nd term = 9 − 5 = 4"])),
        dict(say="Line 2 is wrong. Going back means moving left, so you must use the inverse: add 5.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="9 plus 5 is 14. The 2nd term is 14. Check: 14 minus 5 is 9.", do=[B("9 + 5 = 14", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Sequences in real life", steps=[
        dict(say="Sequences are everywhere. Leap years usually come every 4 years: 2024, 2028, 2032. The rule is add 4.", do=[E("📅", 90, 160, 100), T("leap years: 2024, 2028, 2032 … **+4**", x=230, y=190)]),
        dict(say="Some bacteria can split in two about every 20 minutes. 1 becomes 2, then 4, then 8. The rule is multiply by 2.", do=[E("🦠", 90, 300, 100), T("bacteria: 1, 2, 4, 8 … **× 2**", x=230, y=330)]),
        dict(say="After only 7 hours of doubling, 1 bacterium could become more than 2 million.", do=[B("7 hours → over 2 million", x=230, y=460, color=RED)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("9.1-k4", "One last question. The rule is add 3. The 4th term is 20. What is the 1st term? Pause the video and work it out.", "The rule is 'add 3'. The 4th term is 20. What is the 1st term?"),
        dict(say="Move left, so subtract 3 each time. 20, 17, 14, 11. The 1st term is 11.", do=[SEQ(["11", "14", "17", "20"], y=190), T("moving left: **− 3**", x=80, y=310, color=BLUE), B("1st term = 11", x=80, y=400, color=GREEN, at=4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a sequence is a list of terms in order. The position says where a term is, and the value is the number.", do=[T("• **Position**: where · **value**: the number", x=80, y=170)]),
        dict(say="A term-to-term rule takes you from one term to the next.", do=[T("• **Term-to-term rule**: one term → the next", x=80, y=250)]),
        dict(say="To go back, use the inverse operation.", do=[T("• Going back? Use the **inverse**", x=80, y=330)]),
        dict(say="And use 3 or more terms to be sure of a rule.", do=[T("• Use **3 or more terms** to find a rule", x=80, y=410)]),
    ]),
]

VIDEOS["9.2"] = [
    dict(kind="hook", title="A growing pattern", steps=[
        dict(say="Here are the first 3 patterns of a tile design. Pattern 1 has 3 tiles. Pattern 2 has 5 tiles. Pattern 3 has 7 tiles.",
             do=[CELLS(L3, x=340, y=150, w=900, cols=11, rows=4), T("Pattern 1, 2, 3", x=80, y=170), T("**3**, **5**, **7** tiles", x=80, y=250, at=2)]),
        PAUSE("9.2-k1", "How many tiles will Pattern 4 have? Pause the video and work it out.", "How many tiles will Pattern 4 of the L-shaped design have?"),
    ]),
    dict(kind="hook", title="One more on each arm", steps=[
        dict(say="Each new pattern has 1 more tile on each arm of the L. That is 2 more tiles each time.", do=[SEQ(["3", "5", "7"], y=180), T("+2 each time", x=540, y=200, color=BLUE)]),
        dict(say="7 plus 2 is 9. Pattern 4 has 9 tiles.", do=[SEQ(["9"], 398, 180, c=GREEN), B("Pattern 4: 9 tiles", x=80, y=330, color=GREEN)]),
    ]),
    dict(kind="recall", title="Differences between terms", steps=[
        dict(say="Remember: a quick way to see an add or subtract rule is to write the differences between the terms.", do=[SEQ(["7", "11", "15", "19"], y=180)]),
        dict(say="7, 11, 15, 19. The differences are plus 4, plus 4, plus 4.", do=[T("+4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +4", x=140, y=270, color=BLUE)]),
        PAUSE("9.2-k2", "Look at these 2 sequences. 4, 7, 10, 13. And 1, 4, 9, 16. Which one goes up by the same amount every time? Pause the video and decide.",
              "Which goes up by the SAME amount every time: 4, 7, 10, 13 or 1, 4, 9, 16?"),
    ]),
    dict(kind="idea", title="Linear sequences", steps=[
        dict(say="4, 7, 10, 13 goes up by 3 every time. But 1, 4, 9, 16 goes up by 3, then 5, then 7.", do=[SEQ(["4", "7", "10", "13"], y=150), T("+3, +3, +3 ✓", x=540, y=170, color=GREEN), SEQ(["1", "4", "9", "16"], y=250, at=4), T("+3, +5, +7 ✗", x=540, y=270, color=RED, at=5)]),
        dict(say="A sequence is linear when the differences between terms next to each other are all the same.", do=[T("**Linear**: all the differences are **the same**", x=80, y=380)]),
        dict(say="A linear sequence can go up, or it can go down. 30, 26, 22, 18 is linear, with differences of negative 4.", do=[SEQ(["30", "26", "22", "18"], y=470), T("−4 each time ✓", x=540, y=490, color=GREEN)]),
    ]),
    dict(kind="idea", title="Why the rule works", steps=[
        dict(say="Look at the tile pattern again. Every pattern has 1 corner tile, and 2 equal arms.", do=[CELLS(L3, x=500, y=150, w=760, cols=11, rows=4), T("1 **corner** + 2 equal **arms**", x=80, y=170)]),
        dict(say="In Pattern 3, each arm has 3 tiles. 1 plus 3 plus 3 is 7.", do=[MATH("1 + 3 + 3 = 7", x=80, y=420)]),
        dict(say="So you can jump straight to any pattern. Pattern 6 has 1 plus 6 plus 6, which is 13 tiles.", do=[MATH("Pattern 6: 1 + 6 + 6 = 13", x=80, y=510, color=BLUE)]),
        PAUSE("9.2-k3", "Your turn. How many tiles are in Pattern 8? Pause the video and try it.", "How many tiles are in Pattern 8 of the L-shaped design?"),
    ]),
    dict(kind="idea", title="Check: Pattern 8", steps=[
        dict(say="Pattern 8 has 1 corner, and 2 arms of 8 tiles. 1 plus 8 plus 8 is 17 tiles.", do=[MATH("1 + 8 + 8 = 17", x=80, y=190), B("17 tiles", x=80, y=300, color=GREEN, at=3)]),
    ]),
    dict(kind="idea", title="Two special sequences", steps=[
        dict(say="Square numbers come from square patterns: 1, 4, 9, 16. The differences are 3, 5, 7. They are not equal, so the sequence is not linear.",
             do=[T("**Square numbers**", x=80, y=150), SEQ(["1", "4", "9", "16"], y=220), T("+3, +5, +7 → not linear", x=540, y=240, color=RED, at=5)]),
        dict(say="Triangular numbers come from triangle patterns: 1, 3, 6, 10. The differences are 2, 3, 4. This sequence is not linear either.",
             do=[T("**Triangular numbers**", x=80, y=370), SEQ(["1", "3", "6", "10"], y=440), T("+2, +3, +4 → not linear", x=540, y=460, color=RED, at=5)]),
    ]),
    dict(kind="method", title="How do I decide if a sequence is linear?", steps=[
        dict(say="Here is the method. Step 1: write the difference between every pair of terms that are next to each other.", do=[T("1. Write **every** difference", x=80, y=170)]),
        dict(say="Step 2: if all the differences are equal, the sequence is linear.", do=[T("2. All equal → **linear**", x=80, y=260)]),
        dict(say="Step 3: if even one difference is different, it is not linear.", do=[T("3. One different → **not linear**", x=80, y=350)]),
        dict(say="Step 4: to continue a linear sequence, keep adding the same difference.", do=[T("4. Continue: keep adding the **same difference**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Is it linear?", steps=[
        dict(say="Is this sequence linear? 3, 6, 11, 18.", do=[SEQ(["3", "6", "11", "18"], y=160)]),
        dict(say="The differences are 3, 5 and 7. They are not all equal, so it is not linear.", do=[T("+3, +5, +7", x=540, y=180, color=RED), B("not linear", x=840, y=170, color=RED, at=3.4)]),
        dict(say="What about 52, 45, 38, 31?", do=[SEQ(["52", "45", "38", "31"], y=350)]),
        dict(say="The differences are all negative 7. So this sequence is linear.", do=[T("−7, −7, −7", x=540, y=370, color=GREEN), B("linear", x=840, y=360, color=GREEN, at=2.6)]),
    ]),
    dict(kind="example", title="A matchstick pattern", steps=[
        dict(say="Pattern 1 is a square made of 4 matchsticks. Each new pattern adds 1 more square to the row, sharing a side.", do=[CELLS([[0, 0], [3, 0], [4, 0], [7, 0], [8, 0], [9, 0]], x=80, y=130, w=700, cols=10, rows=1), T("**4**, then **+3** each time", x=820, y=300)]),
        dict(say="A new square needs only 3 new matchsticks. So the sequence is 4, 7, 10, 13, 16. Pattern 5 has 16 matchsticks.", do=[SEQ(["4", "7", "10", "13", "16"], y=440), B("Pattern 5: 16", x=700, y=440, color=GREEN, at=7)]),
        dict(say="Which pattern uses 31 matchsticks? 31 minus 4 is 27, and 27 divided by 3 is 9 steps. 9 steps after Pattern 1 is Pattern 10.", do=[MATH("(31 − 4) ÷ 3 = 9 steps", x=80, y=560), B("Pattern 10", x=700, y=550, color=GREEN, at=8)]),
    ]),
    dict(kind="example", title="Exactly 50 tiles?", steps=[
        dict(say="In the L-shaped design, is there a pattern with exactly 50 tiles?", do=[SEQ(["3", "5", "7", "9"], y=160), T("exactly **50** tiles?", x=560, y=180)]),
        dict(say="Every pattern is 1 corner plus 2 equal arms. 2 equal arms make an even number, and 1 more makes an odd number.", do=[T("1 + (2 equal arms) = 1 + even = **odd**", x=80, y=300)]),
        dict(say="Every term is odd, but 50 is even. So no pattern has exactly 50 tiles.", do=[B("No: 50 is even", x=80, y=410, color=RED)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Is 1, 2, 4, 7, 11 a linear sequence? Here is Kai's working. Which line goes wrong first?",
             do=LINES("Kai", "is 1, 2, 4, 7, 11 linear?", ["Differences: +1, +2, +3, +4", "They go up by 1 each time, so it is linear"])),
        dict(say="Line 2 is wrong. For a linear sequence, the differences themselves must be equal. Here they are 1, 2, 3, 4, which are all different.", do=[dict(a="cross", id="l2")]),
        dict(say="So the sequence is not linear.", do=[B("not linear", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Number patterns you can see", steps=[
        dict(say="In ten-pin bowling, the pins stand in a triangle: 1, then 2, then 3, then 4. That makes 10, a triangular number.", do=[E("🎳", 90, 160, 100), T("bowling pins: 1 + 2 + 3 + 4 = **10**", x=230, y=190)]),
        dict(say="A chessboard has 8 rows of 8 squares. 8 times 8 is 64, a square number.", do=[E("♟️", 90, 300, 100), T("chessboard: 8 × 8 = **64**", x=230, y=330)]),
        dict(say="And the seats in a cinema row are numbered 1, 2, 3, 4: a linear sequence.", do=[E("🎬", 90, 440, 100), T("seat numbers: a **linear** sequence", x=230, y=470)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("9.2-k4", "One last question. Pattern 1 uses 5 matchsticks, and each new pattern adds 4. How many matchsticks are in Pattern 7? Pause the video and work it out.",
              "Pattern 1 uses 5 matchsticks and each new pattern adds 4. How many in Pattern 7?"),
        dict(say="From Pattern 1 to Pattern 7 is 6 steps. 6 times 4 is 24, and 5 plus 24 is 29 matchsticks.", do=[T("Pattern 1 → Pattern 7: **6 steps**", x=80, y=180), MATH("5 + 6 × 4 = 29", x=80, y=280, at=3), B("29 matchsticks", x=80, y=380, color=GREEN, at=6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: count the pieces in each pattern to make a sequence. The picture shows you why the rule works.", do=[T("• Count the pieces → a **sequence**", x=80, y=170)]),
        dict(say="A sequence is linear if all the differences are equal. It can go up or down.", do=[T("• **Linear**: all differences equal", x=80, y=250)]),
        dict(say="Square numbers and triangular numbers are not linear.", do=[T("• Square and triangular numbers: **not linear**", x=80, y=330)]),
        dict(say="To reach a later pattern, count the steps, not the patterns.", do=[T("• Count the **steps**, not the patterns", x=80, y=410)]),
    ]),
]

NT = lambda terms, y=250, id="t": TBL(["Position number n", "1", "2", "3", "4", "5"], [["Term"] + [str(t) for t in terms]], y=y, id=id)

VIDEOS["9.3"] = [
    dict(kind="hook", title="Cinema tickets", steps=[
        dict(say="Cinema tickets cost 7 dollars each. 1 ticket costs 7 dollars, 2 tickets cost 14 dollars, and 3 tickets cost 21 dollars.", do=[E("🎟️", 90, 160, 110), T("**$7** each: 7, 14, 21, …", x=240, y=200)]),
        PAUSE("9.3-k1", "How much do 20 tickets cost? Pause the video and work it out.", "Tickets cost $7 each. How much do 20 tickets cost?"),
    ]),
    dict(kind="hook", title="Use the number of tickets", steps=[
        dict(say="You could keep adding 7, twenty times. But there is a faster way: multiply the number of tickets by 7.", do=[T("adding 7 twenty times is slow", x=80, y=180, color=GREY), MATH("20 × 7 = 140", x=80, y=280, at=4)]),
        dict(say="20 times 7 is 140. 20 tickets cost 140 dollars.", do=[B("$140", x=80, y=390, color=GREEN)]),
    ]),
    dict(kind="recall", title="Letters for numbers", steps=[
        dict(say="Remember: in algebra, a letter stands for a number. 7 n means 7 times n.", do=[B("7n = 7 × n", x=80, y=180)]),
        dict(say="And n plus 3 means n, add 3. If n is 9, then 7 n is 63, and n plus 3 is 12.", do=[B("n + 3", x=80, y=290), T("n = 9 → 7n = **63** · n + 3 = **12**", x=80, y=410, at=4)]),
    ]),
    dict(kind="idea", title="Position number and term", steps=[
        dict(say="Write the ticket prices in a table. The position number, n, says where each term is: first, second, third.", do=[NT([7, 14, 21, 28, 35], y=170), ROW(0, 3)]),
        dict(say="Compare each term with its position number. 7 is 1 times 7. 14 is 2 times 7. 21 is 3 times 7.", do=[MATH("7 = 1 × 7 · 14 = 2 × 7 · 21 = 3 × 7", x=80, y=340)]),
        dict(say="Every term is 7 times its position number. So the term in position n is 7 n. We call this the nth term.", do=[B("nth term = 7n", x=80, y=450, color=BLUE)]),
        dict(say="A term-to-term rule gets the next term. The nth term rule gets any term, straight from its position.", do=[T("the **nth term** gives any term from its **position**", x=80, y=560)]),
    ]),
    dict(kind="idea", title="Rules that add or subtract", steps=[
        dict(say="Now look at this sequence: 4, 5, 6, 7, 8. It is not a times table.", do=[NT([4, 5, 6, 7, 8], y=170), ROW(0, 0.5)]),
        dict(say="Compare each term with its position number. 4 is 1 plus 3. 5 is 2 plus 3. 6 is 3 plus 3. Each term is 3 more than its position.", do=[MATH("4 = 1 + 3 · 5 = 2 + 3 · 6 = 3 + 3", x=80, y=340)]),
        dict(say="So the nth term is n plus 3.", do=[B("nth term = n + 3", x=80, y=450, color=BLUE)]),
        PAUSE("9.3-k2", "Your turn. The nth term of a sequence is n plus 8. What is the 15th term? Pause the video and try it.", "The nth term of a sequence is n + 8. What is the 15th term?"),
    ]),
    dict(kind="idea", title="Check: the 15th term", steps=[
        dict(say="For the 15th term, n is 15. 15 plus 8 is 23.", do=[T("15th term → **n = 15**", x=80, y=180), MATH("15 + 8 = 23", x=80, y=280, color=GREEN, at=2.6)]),
    ]),
    dict(kind="method", title="How do I find the nth term?", steps=[
        dict(say="Here is the method. Step 1: write the sequence in a table, under the position numbers 1, 2, 3.", do=[T("1. Table: terms under **positions** 1, 2, 3 …", x=80, y=170)]),
        dict(say="Step 2: if the terms are a times table, multiply. The 9 times table has nth term 9 n.", do=[T("2. A **times table**? → multiply (9, 18, 27 → **9n**)", x=80, y=260)]),
        dict(say="Step 3: if each term is a fixed amount more or less than its position, add or subtract that amount.", do=[T("3. A fixed amount more or less? → **n + a** or **n − a**", x=80, y=350)]),
        dict(say="Step 4: check your rule with the 1st, 2nd and 3rd terms.", do=[T("4. **Check** with n = 1, 2, 3", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A times-table sequence", steps=[
        dict(say="Find the nth term of 12, 24, 36, 48. Then find the 20th term.", do=[SEQ(["12", "24", "36", "48"], y=160)]),
        dict(say="12 is 1 times 12. 24 is 2 times 12. 36 is 3 times 12. It is the 12 times table, so the nth term is 12 n.", do=[MATH("1 × 12, 2 × 12, 3 × 12", x=80, y=280), B("nth term = 12n", x=80, y=370, color=BLUE, at=6)]),
        dict(say="For the 20th term, n is 20. 12 times 20 is 240.", do=[MATH("12 × 20 = 240", x=80, y=480, color=GREEN)]),
    ]),
    dict(kind="example", title="An add sequence", steps=[
        dict(say="Find the nth term of 21, 22, 23, 24. Then find the 50th term.", do=[SEQ(["21", "22", "23", "24"], y=160)]),
        dict(say="21 minus 1 is 20. 22 minus 2 is 20. 23 minus 3 is 20. Each term is 20 more than its position. The nth term is n plus 20.", do=[MATH("21 − 1 = 20 · 22 − 2 = 20", x=80, y=280), B("nth term = n + 20", x=80, y=370, color=BLUE, at=7)]),
        dict(say="For the 50th term, 50 plus 20 is 70.", do=[MATH("50 + 20 = 70", x=80, y=480, color=GREEN)]),
    ]),
    dict(kind="example", title="Negative terms", steps=[
        dict(say="Write the first 4 terms of the sequence with nth term n minus 6.", do=[B("nth term = n − 6", x=80, y=160, color=BLUE)]),
        dict(say="Put in n equals 1: 1 minus 6 is negative 5. For n equals 2: 2 minus 6 is negative 4.", do=[MATH("1 − 6 = −5", x=80, y=280), MATH("2 − 6 = −4", x=420, y=280, at=3.6)]),
        dict(say="Then negative 3, and negative 2. The sequence is negative 5, negative 4, negative 3, negative 2.", do=[SEQ(["−5", "−4", "−3", "−2"], y=400, c=GREEN)]),
    ]),
    dict(kind="example", title="Which position?", steps=[
        dict(say="The nth term of a sequence is 8 n. Which term is equal to 96?", do=[B("8n = 96", x=80, y=170, color=BLUE)]),
        dict(say="8 times n is 96. Use the inverse: 96 divided by 8 is 12. It is the 12th term.", do=[MATH("n = 96 ÷ 8 = 12", x=80, y=290), B("the 12th term", x=80, y=390, color=GREEN, at=4.6)]),
        dict(say="Is 50 in this sequence? 50 divided by 8 is 6.25. That is not a whole number, so 50 is not a term.", do=[MATH("50 ÷ 8 = 6.25 → not a term", x=80, y=510, color=RED)]),
        PAUSE("9.3-k3", "Your turn. The nth term is 6 n. Which term is equal to 54? Pause the video and try it.", "The nth term is 6n. Which term is equal to 54?"),
    ]),
    dict(kind="example", title="Check: 6n = 54", steps=[
        dict(say="54 divided by 6 is 9. It is the 9th term. Check: 6 times 9 is 54.", do=[MATH("n = 54 ÷ 6 = 9", x=80, y=190), B("the 9th term", x=80, y=300, color=GREEN, at=2.6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Find the nth term of 5, 10, 15, 20. Here is Ben's working. Which line goes wrong first?",
             do=LINES("Ben", "the nth term of 5, 10, 15, 20", ["The terms go up by 5 each time", "So the nth term is n + 5", "So the 10th term is 10 + 5 = 15"])),
        dict(say="Line 2 is wrong. Add 5 is the term-to-term rule. Test n plus 5 with n equals 1: it gives 6, but the first term is 5.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="This is the 5 times table. The nth term is 5 n, and the 10th term is 50.", do=[B("nth term = 5n → 10th term = 50", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Rules that jump ahead", steps=[
        dict(say="On many streets, the houses on one side have even numbers: 2, 4, 6, 8. The nth house on that side is number 2 n.", do=[E("🏠", 90, 160, 100), T("house numbers 2, 4, 6 … → **2n**", x=230, y=190)]),
        dict(say="A resting adult heart beats about 70 times every minute. After n minutes, that is about 70 n beats.", do=[E("❤️", 90, 300, 100), T("heartbeats after n minutes → **70n**", x=230, y=330)]),
        dict(say="In 1 day there are 1,440 minutes. 70 times 1,440 is about 100,000 beats, every day.", do=[B("about 100 000 beats a day", x=230, y=460, color=RED)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("9.3-k4", "One last question. The nth term is n minus 7. Find the 3rd term. Pause the video and answer.", "The nth term is n − 7. Find the 3rd term."),
        dict(say="For the 3rd term, n is 3. 3 minus 7 is negative 4.", do=[MATH("3 − 7 = −4", x=80, y=190), B("−4", x=80, y=300, color=GREEN, at=2.4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the position number n tells you where a term is. The nth term rule turns n into the term.", do=[T("• **n** = position · the **nth term** rule gives the term", x=80, y=170)]),
        dict(say="A times table sequence has an nth term like 7 n.", do=[T("• Times table: 7, 14, 21 … → **7n**", x=80, y=250)]),
        dict(say="If each term is a fixed amount more or less than its position, add or subtract.", do=[T("• Fixed amount more or less: **n + a**, **n − a**", x=80, y=330)]),
        dict(say="Always test your rule with n equals 1.", do=[T("• Always **test** with n = 1", x=80, y=410)]),
    ]),
]

MAP = lambda pairs, x=640, y=150, w=600, at=0, mx=10: BIG(FIG(x, y, w, at, kind="mapping", min=0, max=mx, pairs=pairs))

VIDEOS["9.4"] = [
    dict(kind="hook", title="A money changer", steps=[
        dict(say="A tourist changes dollars into another currency. The money changer's rule is simple: multiply by 4. So 5 dollars becomes 20.", do=[E("💱", 90, 160, 110), T("rule: **× 4**", x=240, y=200), MACH("5", "× 4", "20", y=330, at=5)]),
        PAUSE("9.4-k1", "Someone receives 36. How many dollars did they hand in? Pause the video and work it out.", "The rule is × 4. Someone receives 36. How many dollars did they hand in?"),
    ]),
    dict(kind="hook", title="Run it backwards", steps=[
        dict(say="We know what came out, so we work backwards. The opposite of multiply by 4 is divide by 4.", do=[MACH("?", "× 4", "36", y=170), T("backwards: **÷ 4**", x=80, y=290, color=BLUE)]),
        dict(say="36 divided by 4 is 9. They handed in 9 dollars.", do=[MATH("36 ÷ 4 = 9", x=80, y=380), B("$9", x=80, y=470, color=GREEN, at=2.6)]),
    ]),
    dict(kind="recall", title="Inverse operations", steps=[
        dict(say="Remember: every operation has an inverse that undoes it. Add undoes subtract. Multiply undoes divide.", do=[T("**+** ↔ **−** · **×** ↔ **÷**", x=80, y=180)]),
        dict(say="If 7 times 6 is 42, then 42 divided by 6 is 7.", do=[MATH("7 × 6 = 42 → 42 ÷ 6 = 7", x=80, y=300)]),
    ]),
    dict(kind="idea", title="Function machines", steps=[
        dict(say="A function is a rule that links 2 sets of numbers. A function machine shows the rule in a box.", do=[T("**Function**: a rule linking two sets of numbers", x=80, y=150), MACH("input", "+ 3", "output", y=240)]),
        dict(say="The numbers that go in are the inputs. The numbers that come out are the outputs.", do=[T("**inputs** go in · **outputs** come out", x=80, y=350)]),
        dict(say="Put 2 into this machine. 2 plus 3 is 5. Put in 6, and out comes 9. Each input has exactly 1 output.", do=[MACH("2", "+ 3", "5", y=440), MACH("6", "+ 3", "9", x=640, y=440, at=4)]),
        PAUSE("9.4-k2", "Your turn. The input is 8, and the machine subtracts 3. What is the output? Pause the video and try it.", "Input 8 → − 3 → output. What is the output?"),
    ]),
    dict(kind="idea", title="Check: 8 into − 3", steps=[
        dict(say="8 minus 3 is 5. The output is 5.", do=[MACH("8", "− 3", "5", y=190), B("output = 5", x=80, y=330, color=GREEN, at=1.6)]),
    ]),
    dict(kind="idea", title="Mapping diagrams", steps=[
        dict(say="A mapping diagram shows the same function with 2 number lines. An arrow goes from each input to its output.", do=[T("**Mapping diagram**: arrows from inputs to outputs", x=80, y=150), MAP([[2, 5], [4, 7], [5, 8]], x=560, y=220, w=660)]),
        dict(say="For the machine plus 3, every arrow moves 3 places to the right. The arrows are all parallel.", do=[MACH("in", "+ 3", "out", y=290), T("every arrow: **3 to the right**", x=80, y=430)]),
    ]),
    dict(kind="idea", title="Finding an input", steps=[
        dict(say="If you know the output, run the machine backwards, using the inverse operation.", do=[T("know the output? run it **backwards**", x=80, y=150), MACH("?", "× 4", "36", y=240)]),
        dict(say="The inverse machine for multiply by 4 is divide by 4. 36 goes in, and 9 comes out.", do=[MACH("36", "÷ 4", "9", y=370), T("the **inverse machine**", x=640, y=390, color=BLUE)]),
        PAUSE("9.4-k3", "Your turn. A machine adds 7. The output is 12. What was the input? Pause the video and try it.", "Input → + 7 → output. The output is 12. What was the input?"),
    ]),
    dict(kind="idea", title="Check: + 7 gives 12", steps=[
        dict(say="The inverse of add 7 is subtract 7. 12 minus 7 is 5. The input was 5. Check: 5 plus 7 is 12.", do=[MACH("?", "+ 7", "12", y=170), MATH("12 − 7 = 5", x=80, y=310, at=2.6), B("input = 5", x=80, y=410, color=GREEN, at=5)]),
    ]),
    dict(kind="method", title="How do I use a function machine?", steps=[
        dict(say="Here is the method. Step 1: to find an output, put the input through the machine.", do=[T("1. **Output**: put the input through", x=80, y=170)]),
        dict(say="Step 2: to find an input, use the inverse operation on the output.", do=[T("2. **Input**: use the **inverse** on the output", x=80, y=260)]),
        dict(say="Step 3: to find the rule, compare the inputs and outputs. Try adding, then try multiplying.", do=[T("3. **Rule**: compare; try + then ×", x=80, y=350)]),
        dict(say="Step 4: test your rule on every pair.", do=[T("4. **Test** the rule on every pair", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Outputs and inputs", steps=[
        dict(say="This machine multiplies by 5. Find the missing numbers. 1 goes to what? 3 goes to what? And what goes to 40?",
             do=[MACH("input", "× 5", "output", y=150), TBL(["Input", "1", "3", "?"], [["Output", "?", "?", "40"]], y=280, id="q"), ROW(0, 3, "q")]),
        dict(say="1 times 5 is 5. 3 times 5 is 15.", do=[MATH("1 × 5 = 5 · 3 × 5 = 15", x=640, y=290)]),
        dict(say="For the last one, work backwards. 40 divided by 5 is 8. The input was 8.", do=[MATH("40 ÷ 5 = 8", x=640, y=380, color=BLUE), B("5, 15 and 8", x=80, y=500, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="An inverse machine", steps=[
        dict(say="This machine subtracts 6. The outputs are 4, 11 and 19. Find the inputs.", do=[MACH("input", "− 6", "output", y=150), T("outputs: **4**, **11**, **19**", x=80, y=270)]),
        dict(say="The inverse machine adds 6.", do=[MACH("output", "+ 6", "input", y=350)]),
        dict(say="4 plus 6 is 10. 11 plus 6 is 17. 19 plus 6 is 25. The inputs are 10, 17 and 25.", do=[MATH("4 + 6 = 10 · 11 + 6 = 17 · 19 + 6 = 25", x=80, y=480), B("10, 17, 25", x=80, y=570, color=GREEN, at=7)]),
    ]),
    dict(kind="example", title="Finding the rule", steps=[
        dict(say="A one-step machine maps 2 to 8, 3 to 9, and 5 to 11. What is the function?", do=[TBL(["Input", "2", "3", "5"], [["Output", "8", "9", "11"]], y=160, id="r"), ROW(0, 0.5, "r")]),
        dict(say="2 goes to 8. That could be add 6, or it could be multiply by 4. One pair is not enough.", do=[T("2 → 8: **+ 6** or **× 4**?", x=80, y=320)]),
        dict(say="Test add 6. 3 plus 6 is 9, correct. 5 plus 6 is 11, correct.", do=[MATH("3 + 6 = 9 ✓ · 5 + 6 = 11 ✓", x=80, y=400, color=GREEN)]),
        dict(say="Test multiply by 4. 3 times 4 is 12, not 9. So the function is add 6.", do=[MATH("3 × 4 = 12 ✗", x=80, y=480, color=RED), B("the function is + 6", x=520, y=474, color=GREEN, at=4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A machine divides by 4. The output is 6. Find the input. Here is Tia's working. Which line goes wrong first?",
             do=LINES("Tia", "input → ÷ 4 → 6", ["The machine divides by 4", "To go backwards, divide again: 6 ÷ 4 = 1.5", "The input is 1.5"])),
        dict(say="Line 2 is wrong. To go backwards, use the inverse. The inverse of divide by 4 is multiply by 4.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="6 times 4 is 24. The input is 24. Check: 24 divided by 4 is 6.", do=[B("6 × 4 = 24", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Machines you already use", steps=[
        dict(say="You use function machines every day. To change inches into centimetres, multiply by 2.54.", do=[E("📏", 90, 160, 100), MACH("inches", "× 2.54", "cm", x=230, y=175)]),
        dict(say="In winter, the time in Hanoi is 7 hours ahead of London. London time goes in, add 7, and Hanoi time comes out.", do=[E("🕖", 90, 310, 100), MACH("London", "+ 7", "Hanoi", x=230, y=325)]),
        dict(say="And to go from Hanoi time back to London time, use the inverse machine: subtract 7.", do=[T("back again: **− 7**", x=230, y=470, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("9.4-k4", "One last question. A machine divides by 2. The output is 9. What was the input? Pause the video and answer.", "Input → ÷ 2 → output. The output is 9. What was the input?"),
        dict(say="The inverse of divide by 2 is multiply by 2. 9 times 2 is 18. The input was 18.", do=[MACH("?", "÷ 2", "9", y=170), MATH("9 × 2 = 18", x=80, y=310, at=2.6), B("input = 18", x=80, y=410, color=GREEN, at=4.6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a function machine turns inputs into outputs. Each input has 1 output.", do=[T("• **Function machine**: input → rule → output", x=80, y=170)]),
        dict(say="A mapping diagram shows a function with arrows.", do=[T("• **Mapping diagram**: arrows from inputs to outputs", x=80, y=250)]),
        dict(say="To find an input, use the inverse operation on the output.", do=[T("• Input? Use the **inverse** on the output", x=80, y=330)]),
        dict(say="To find a rule, test it on every pair.", do=[T("• Rule? **Test** it on every pair", x=80, y=410)]),
    ]),
]
