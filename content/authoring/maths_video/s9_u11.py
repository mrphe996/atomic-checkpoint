# -*- coding: utf-8 -*-
"""Stage 9 · Unit 11 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

VIDEOS = {}

VIDEOS["11.1"] = [
    dict(kind="hook", title="Prize money", steps=[
        dict(say="Three friends share prize money in the ratio 3 to 4 to 8, based on the hours each one worked. The smallest share is 45 dollars.",
             do=[E("🏆", 90, 170, 100), T("ratio **3 : 4 : 8** · smallest share **$45**", x=230, y=200)]),
        PAUSE("11.1-k1", "What was the total prize, in dollars? Pause the video and work it out.", "Total prize ($)?"),
    ]),
    dict(kind="hook", title="$225", steps=[
        dict(say="The smallest share is 3 parts. So 1 part is 45 divided by 3, which is 15 dollars. There are 15 parts altogether. 15 times 15 is 225 dollars.",
             do=[MATH("1 part = 45 ÷ 3 = $15", x=80, y=180), B("15 × 15 = $225", x=80, y=290, color=GREEN, at=8)]),
    ]),
    dict(kind="recall", title="Sharing in a ratio", steps=[
        dict(say="Remember: to share 120 dollars in the ratio 4 to 5 to 6, add the parts: 15. 1 part is 8 dollars. The shares are 32, 40 and 48 dollars.", do=[MATH("15 parts → $8 each → $32, $40, $48", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Find one part first", steps=[
        dict(say="Whatever you are given, a share, the total, or a difference, first find the value of one part.",
             do=[B("find **1 part** first", x=80, y=170, color=BLUE), TBL(["Person", "Parts", "Share"], [["A", "3", "$45"], ["B", "4", "?"], ["C", "8", "$120"]], y=270), ROW(0, 3), ROW(2, 5)]),
        PAUSE("11.1-k2", "Your turn. B has 4 parts. What is B's share, in dollars? Pause the video and try it.", "B's share ($)?"),
    ]),
    dict(kind="idea", title="Check: $60", steps=[
        dict(say="4 times 15 is 60 dollars. Check: 45 plus 60 plus 120 is 225.", do=[B("4 × 15 = $60", x=80, y=190, color=GREEN), MATH("45 + 60 + 120 = 225 ✓", x=80, y=300)]),
        dict(say="Ratios link to fractions. In 3 to 4 to 8, A gets 3 fifteenths, which is a fifth of the total.", do=[MATH("A: 3/15 = 1/5 of the total", x=80, y=390)]),
    ]),
    dict(kind="method", title="How do I solve ratio problems?", steps=[
        dict(say="Here is the method. Step 1: add the parts.", do=[T("1. **Add** the parts", x=80, y=170)]),
        dict(say="Step 2: match what you know, a share, the total or a difference, to its number of parts.", do=[T("2. Match what you know to its **parts**", x=80, y=260)]),
        dict(say="Step 3: find one part, then multiply.", do=[T("3. **1 part**, then multiply", x=80, y=350)]),
        dict(say="Step 4: check that the shares add up to the total.", do=[T("4. **Check** the total", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A changing ratio", steps=[
        dict(say="In a club of 40, boys to girls is 3 to 5. That is 15 boys and 25 girls. 4 more boys join. The new ratio is 19 to 25.", do=[MATH("15 : 25 → 19 : 25", x=80, y=180)]),
        dict(say="A map has a scale of 1 to 25,000. 6.4 centimetres on the map is 160,000 centimetres, which is 1.6 kilometres.", do=[MATH("6.4 × 25 000 = 160 000 cm = 1.6 km", x=80, y=280)]),
        PAUSE("11.1-k3", "Your turn. Two shares are in the ratio 5 to 2. The difference between them is 27. What is the total? Pause and work it out.", "Ratio 5 : 2, difference 27. Total?"),
    ]),
    dict(kind="example", title="Check: 63", steps=[
        dict(say="The difference is 3 parts. 1 part is 27 divided by 3, which is 9. The total is 7 parts: 63.", do=[B("27 ÷ 3 = 9 → 7 × 9 = 63", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ratio 3 to 4 to 8. A's share, 3 parts, is 45 dollars. Nia finds the total. Which line is wrong?", do=LINES("Nia", "A's share (3 parts) is $45; total?", ["45 ÷ 15 = 3 per part", "total 3 × 15 = 45"])),
        dict(say="Line 1 is wrong. 45 dollars is 3 parts, not the total.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="1 part is 45 divided by 3, which is 15. The total is 225 dollars.", do=[B("45 ÷ 3 = 15 → $225", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Business partners", steps=[
        dict(say="Business partners often share profits in the ratio of the money each one invested.", do=[E("🤝", 90, 170, 100), T("profit shared in the ratio of **investment**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("11.1-k4", "One last question. Concrete is cement, sand and gravel in the ratio 1 to 2 to 5. What fraction is gravel: 5 eighths, or 5 sevenths? Pause the video and choose.", "In 1 : 2 : 5, gravel's fraction is …"),
        dict(say="There are 8 parts altogether. Gravel is 5 of them: 5 eighths.", do=[B("5/8", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: find the value of one part first.", do=[T("• Find 1 part first", x=80, y=170)]),
        dict(say="You can start from a share, the total, or a difference.", do=[T("• Share, total or difference", x=80, y=250)]),
        dict(say="When a ratio changes, work with the real amounts.", do=[T("• Ratio changes: use real amounts", x=80, y=330)]),
        dict(say="A ratio gives fractions of the total.", do=[T("• Ratios ↔ fractions of the total", x=80, y=410)]),
    ]),
]

VIDEOS["11.2"] = [
    dict(kind="hook", title="Painting a hall", steps=[
        dict(say="4 painters take 6 days to paint a school hall. The head teacher wants it done faster, so she hires more painters.",
             do=[E("🎨", 90, 170, 100), T("**4 painters → 6 days**", x=230, y=200)]),
        PAUSE("11.2-k1", "With 8 painters, how many days will it take? Pause the video and work it out.", "Days for 8 painters?"),
    ]),
    dict(kind="hook", title="3 days", steps=[
        dict(say="Twice as many painters take half the time. 6 divided by 2 is 3 days.", do=[B("3 days", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Direct proportion", steps=[
        dict(say="Remember direct proportion: if 3 kilograms cost 7.50 dollars, then 1 kilogram costs 2.50, and 5 kilograms cost 12.50.", do=[MATH("3 kg $7.50 → 1 kg $2.50 → 5 kg $12.50", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Inverse proportion", steps=[
        dict(say="In inverse proportion, when one quantity is doubled, the other is halved. Their product stays the same.",
             do=[B("double ↔ halve · the **product** stays the same", x=80, y=170, color=BLUE)]),
        dict(say="Here, multiply the painters by the days. This is the total amount of work.", do=[T("painters × days = total work", x=80, y=270)]),
        PAUSE("11.2-k2", "Your turn. How many painter-days does the hall need? Pause the video and try it.", "Painter-days?"),
    ]),
    dict(kind="idea", title="Check: 24", steps=[
        dict(say="4 times 6 is 24 painter-days. Divide 24 by the number of painters to find the days.",
             do=[B("4 × 6 = 24 painter-days", x=80, y=170, color=GREEN), TBL(["Painters", "2", "4", "6", "8", "12"], [["Days", "12", "6", "4", "3", "?"]], y=280), ROW(0, 3)]),
        PAUSE("11.2-k3", "Your turn. How many days for 12 painters? Pause the video and answer.", "12 painters: days?"),
    ]),
    dict(kind="idea", title="Check: 2 days", steps=[
        dict(say="24 divided by 12 is 2 days.", do=[B("24 ÷ 12 = 2 days", x=80, y=190, color=GREEN)]),
        dict(say="Ask: if one doubles, does the other double, or halve? Double means direct: divide to find the rate. Halve means inverse: multiply to find the total.", do=[T("doubles → **direct** · halves → **inverse**", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I solve proportion problems?", steps=[
        dict(say="Here is the method. Step 1: decide: direct, or inverse?", do=[T("1. **Direct** or **inverse**?", x=80, y=170)]),
        dict(say="Step 2: direct: find the value for one.", do=[T("2. Direct: find **1 unit**", x=80, y=260)]),
        dict(say="Step 3: inverse: multiply to find the total, then divide.", do=[T("3. Inverse: **multiply**, then divide", x=80, y=350)]),
        dict(say="Step 4: check the answer goes up or down as it should.", do=[T("4. Up or **down**? Check", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="At 60 kilometres per hour, a trip takes 2 hours. The distance is 120 kilometres. At 80 kilometres per hour: 120 divided by 80 is 1.5 hours.", do=[MATH("60 × 2 = 120 → 120 ÷ 80 = 1.5 h", x=80, y=180)]),
        dict(say="Food for 30 campers lasts 12 days. That is 360 camper-days. For 40 campers: 360 divided by 40 is 9 days.", do=[MATH("30 × 12 = 360 → 360 ÷ 40 = 9 days", x=80, y=280)]),
        dict(say="A printer prints 42 pages in 3 minutes. That is direct: 14 pages a minute. In 8 minutes, 112 pages.", do=[MATH("42 ÷ 3 = 14 → 14 × 8 = 112", x=80, y=380)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="4 painters take 6 days. Ollie finds the time for 8 painters. Which line is wrong?", do=LINES("Ollie", "4 painters take 6 days; 8 painters?", ["twice as many painters", "so 12 days"])),
        dict(say="Line 2 is wrong. More painters means less time.", do=[dict(a="cross", id="l2")]),
        dict(say="24 painter-days divided by 8 is 3 days.", do=[B("24 ÷ 8 = 3 days", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Planning projects", steps=[
        dict(say="Project managers use inverse proportion to plan how many workers they need to finish a job on time.", do=[E("📋", 90, 170, 100), T("workers × time = the **work**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("11.2-k4", "One last question. Speed and time for a fixed journey: inverse, or direct? Pause the video and choose.", "Speed and time for a fixed journey …"),
        dict(say="Inverse. Double the speed, and the time halves. Speed times time is the fixed distance.", do=[B("inverse", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: direct: the ratio is constant. Double means double.", do=[T("• Direct: double ↔ double", x=80, y=170)]),
        dict(say="Inverse: the product is constant. Double means halve.", do=[T("• Inverse: double ↔ halve", x=80, y=250)]),
        dict(say="Direct: find one unit. Inverse: find the total.", do=[T("• Direct: 1 unit · inverse: the total", x=80, y=330)]),
        dict(say="Check the answer makes sense.", do=[T("• Check it makes sense", x=80, y=410)]),
    ]),
]
