# -*- coding: utf-8 -*-
"""Stage 8 · Unit 10 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

# a percentage bar: 100% of the original, then the new amount as a share of it
PBAR = lambda pct, label, x=80, y=200, at=0, c=BLUE, w=6: T(f'<span style="display:inline-flex;align-items:center;gap:16px"><span style="display:inline-block;width:{pct * w}px;height:46px;background:{c};border-radius:6px"></span><b>{label}</b></span>', x=x, y=y, at=at)

VIDEOS = {}

VIDEOS["10.1"] = [
    dict(kind="hook", title="A price rise", steps=[
        dict(say="A concert ticket went up from 60 dollars to 75 dollars. The organiser says it is only a small rise.", do=[E("🎫", 90, 170, 100), T("**$60 → $75** · “only a small rise”", x=230, y=200)]),
        PAUSE("10.1-k1", "By what percentage did the price rise? Pause the video and work it out.", "$60 → $75. Percentage rise?"),
    ]),
    dict(kind="hook", title="25 percent", steps=[
        dict(say="The rise is 15 dollars. Compare it with the original price, 60 dollars. 15 divided by 60 is 0.25, which is 25 percent. That is a quarter more, not so small!",
             do=[PBAR(100, "$60 = 100%", y=170), PBAR(125, "$75 = 125%", y=250, c=RED, at=2), MATH("15 ÷ 60 × 100 = 25%", x=80, y=360, color=GREEN, at=6)]),
    ]),
    dict(kind="recall", title="A percentage of an amount", steps=[
        dict(say="Remember: to find 15 percent of 80, multiply 0.15 by 80. That is 12.", do=[MATH("15% of 80 = 0.15 × 80 = 12", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Increasing and decreasing", steps=[
        dict(say="To increase an amount by a percentage, find the percentage, then add it. To decrease, find it, then subtract it.",
             do=[TBL(["Task", "Working", "Answer"], [["increase $80 by 15%", "15% = $12; 80 + 12", "$92"], ["decrease $80 by 15%", "15% = $12; 80 − 12", "$68"]], y=170), ROW(0, 3), ROW(1, 5)]),
        PAUSE("10.1-k2", "Your turn. Increase 200 by 35 percent. Pause the video and try it.", "Increase 200 by 35%."),
    ]),
    dict(kind="idea", title="Check: 200 + 35%", steps=[
        dict(say="35 percent of 200 is 70. 200 plus 70 is 270.", do=[MATH("0.35 × 200 = 70", x=80, y=190), B("200 + 70 = 270", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="idea", title="Change as a percentage", steps=[
        dict(say="The percentage change is the change, divided by the original amount, times 100. Always divide by the original amount.",
             do=[B("% change = change ÷ original × 100", x=80, y=170, color=BLUE)]),
        dict(say="The actual change, 15 dollars, is the absolute change. 25 percent is the relative change. Percentages make it fair to compare changes of different sizes.",
             do=[T("**$15**: absolute change · **25%**: percentage change", x=80, y=280)]),
    ]),
    dict(kind="method", title="How do I work with percentage change?", steps=[
        dict(say="Here is the method. Step 1: to increase or decrease, find the percentage of the original, then add or subtract it.", do=[T("1. Find the %, then **add** or **subtract**", x=80, y=170)]),
        dict(say="Step 2: for a percentage change, find the change: the new amount minus the original.", do=[T("2. Change = **new − original**", x=80, y=260)]),
        dict(say="Step 3: divide by the original, and multiply by 100.", do=[T("3. **÷ original** × 100", x=80, y=350)]),
        dict(say="Step 4: say whether it is an increase or a decrease.", do=[T("4. Increase or decrease?", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A decrease", steps=[
        dict(say="A laptop costs 850 dollars. It is reduced by 12 percent. 12 percent of 850 is 102. 850 minus 102 is 748 dollars.",
             do=[E("💻", 90, 160, 90), MATH("0.12 × 850 = 102", x=230, y=180), B("850 − 102 = $748", x=230, y=290, color=GREEN, at=6)]),
        PAUSE("10.1-k3", "Your turn. A price falls from 80 dollars to 68 dollars. What is the percentage decrease? Pause and work it out.", "$80 → $68. Percentage decrease?"),
    ]),
    dict(kind="example", title="Check: $80 → $68", steps=[
        dict(say="The change is 12 dollars. 12 divided by 80, times 100, is 15. It is a 15 percent decrease.", do=[MATH("12 ÷ 80 × 100 = 15", x=80, y=190), B("15% decrease", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="Comparing two shops", steps=[
        dict(say="In shop A, a price went from 40 to 46 dollars. In shop B, from 120 to 132 dollars. Which had the bigger percentage rise?", do=[T("A: **$40 → $46** · B: **$120 → $132**", x=80, y=170)]),
        dict(say="Shop A: 6 divided by 40 is 15 percent. Shop B: 12 divided by 120 is 10 percent. Shop A had the bigger percentage rise, even though shop B rose more in dollars.",
             do=[MATH("A: 6 ÷ 40 = 15%", x=80, y=270), MATH("B: 12 ÷ 120 = 10%", x=80, y=350, at=4), B("shop A", x=80, y=440, color=GREEN, at=7)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A price falls from 50 dollars to 40 dollars. Jay finds the percentage decrease. Which line goes wrong first?", do=LINES("Jay", "$50 → $40: % decrease", ["change = $10", "10 ÷ 40 × 100 = 25%"])),
        dict(say="Line 2 is wrong. He divided by the new price. You must divide by the original price, 50.", do=[dict(a="cross", id="l2")]),
        dict(say="10 divided by 50, times 100, is 20 percent.", do=[B("10 ÷ 50 × 100 = 20%", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Population change", steps=[
        dict(say="Governments track population changes as percentages. A town fell from 25,000 people to 23,500.", do=[E("🏘️", 90, 170, 100), T("**25 000 → 23 500**", x=230, y=200)]),
        dict(say="The change is 1,500. 1,500 divided by 25,000, times 100, is 6. That is a 6 percent decrease, which helps compare it with towns of other sizes.",
             do=[MATH("1500 ÷ 25 000 × 100 = 6%", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("10.1-k4", "One last question. Decrease 90 by 10 percent. Pause the video and answer.", "Decrease 90 by 10%."),
        dict(say="10 percent of 90 is 9. 90 minus 9 is 81.", do=[MATH("10% of 90 = 9", x=80, y=190), B("90 − 9 = 81", x=80, y=290, color=GREEN, at=2.4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: to increase, add the percentage. To decrease, subtract it.", do=[T("• Increase: **add** · decrease: **subtract**", x=80, y=170)]),
        dict(say="Percentage change equals the change, divided by the original, times 100.", do=[T("• % change = change ÷ **original** × 100", x=80, y=250)]),
        dict(say="Know the difference between absolute change and percentage change.", do=[T("• Absolute change vs percentage change", x=80, y=330)]),
        dict(say="Use percentages to compare changes fairly.", do=[T("• Percentages compare changes fairly", x=80, y=410)]),
    ]),
]

VIDEOS["10.2"] = [
    dict(kind="hook", title="Sale!", steps=[
        dict(say="A shop takes 35 percent off everything. A jacket costs 120 dollars.", do=[E("🏷️", 90, 170, 100), T("**35% off** · jacket **$120**", x=230, y=200)]),
        dict(say="Can you find the sale price in one calculation?", do=[T("in **one** calculation?", x=230, y=300)]),
        PAUSE("10.2-k1", "What is 120 dollars with 35 percent off? Pause the video and work it out.", "$120 with 35% off = ?"),
    ]),
    dict(kind="hook", title="What you pay", steps=[
        dict(say="If 35 percent is taken off, you pay 100 minus 35, which is 65 percent. 65 percent as a decimal is 0.65.",
             do=[PBAR(100, "100%", y=170), PBAR(65, "65% you pay", y=250, c=GREEN, at=2)]),
        dict(say="So multiply by 0.65. 120 times 0.65 is 78 dollars. That is one calculation.", do=[B("120 × 0.65 = $78", x=80, y=360, color=GREEN)]),
    ]),
    dict(kind="recall", title="Percentages as decimals", steps=[
        dict(say="Remember: 35 percent is 0.35, and 100 percent is 1. 108 percent is 1.08.", do=[MATH("35% = 0.35 · 100% = 1 · 108% = 1.08", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Multipliers", steps=[
        dict(say="A multiplier changes an amount in one step. After a 15 percent increase you have 115 percent, so multiply by 1.15. After a 35 percent decrease you have 65 percent, so multiply by 0.65.",
             do=[TBL(["Change", "You have", "Multiplier"], [["15% increase", "115%", "× 1.15"], ["35% decrease", "65%", "× 0.65"], ["4% increase", "104%", "× 1.04"]], y=170), ROW(0, 2.5), ROW(1, 7), ROW(2, 10)]),
        PAUSE("10.2-k2", "Your turn. What is the multiplier for a 22 percent decrease? Pause the video and try it.", "Multiplier for a 22% decrease?"),
    ]),
    dict(kind="idea", title="Check: 22% decrease", steps=[
        dict(say="100 minus 22 is 78 percent. So the multiplier is 0.78.", do=[B("× 0.78", x=80, y=190, color=GREEN)]),
        dict(say="Multipliers also work for repeated changes. Two 10 percent rises is times 1.1, times 1.1, which is times 1.21. That is a 21 percent rise, not 20 percent.",
             do=[MATH("× 1.1 × 1.1 = × 1.21 → 21%", x=80, y=320)]),
    ]),
    dict(kind="method", title="How do I use a multiplier?", steps=[
        dict(say="Here is the method. Step 1: for an increase of r percent, the multiplier is 1 plus r over 100. For a decrease, it is 1 minus r over 100.", do=[T("1. Increase: **1 + r/100** · decrease: **1 − r/100**", x=80, y=170)]),
        dict(say="Step 2: multiply the original amount by the multiplier.", do=[T("2. Original **×** multiplier", x=80, y=260)]),
        dict(say="Step 3: for several changes, multiply the multipliers together.", do=[T("3. Several changes: **multiply** the multipliers", x=80, y=350)]),
        dict(say="Step 4: check. An increase has a multiplier above 1. A decrease has one below 1.", do=[T("4. **Check**: increase > 1, decrease < 1", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A car loses value", steps=[
        dict(say="A car worth 14,000 dollars loses 18 percent of its value. The multiplier is 0.82. 14,000 times 0.82 is 11,480 dollars.",
             do=[E("🚗", 90, 160, 90), MATH("14 000 × 0.82", x=230, y=180), B("= $11 480", x=230, y=290, color=GREEN, at=6)]),
        PAUSE("10.2-k3", "Your turn. Increase 500 by 12 percent, using times 1.12. Pause and work it out.", "Increase 500 by 12% (× 1.12)."),
    ]),
    dict(kind="example", title="Check: 500 × 1.12", steps=[
        dict(say="500 times 1.12 is 560.", do=[B("500 × 1.12 = 560", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Up 20%, then down 20%", steps=[
        dict(say="A price rises 20 percent, then falls 20 percent. Is it back where it started? Times 1.2, times 0.8, is times 0.96.",
             do=[MATH("× 1.2 × 0.8 = × 0.96", x=80, y=190)]),
        dict(say="0.96 is 96 percent. So overall it is a 4 percent decrease. It is not back to the start.", do=[B("4% decrease overall", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="example", title="Reading a multiplier", steps=[
        dict(say="A value is multiplied by 1.035. What percentage change is that? 1.035 is 103.5 percent, so it is a 3.5 percent increase.", do=[MATH("1.035 = 103.5%", x=80, y=190), B("3.5% increase", x=80, y=290, color=GREEN, at=5)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Lee decreases 90 dollars by 30 percent. Which line goes wrong first?", do=LINES("Lee", "decrease $90 by 30%", ["multiplier = 0.3", "90 × 0.3 = $27"])),
        dict(say="Line 1 is wrong. 0.3 finds the 30 percent taken off. After the decrease you keep 70 percent, so the multiplier is 0.7.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="90 times 0.7 is 63 dollars.", do=[B("90 × 0.7 = $63", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Savings interest", steps=[
        dict(say="Banks pay interest as a percentage each year. With 5 percent interest, savings are multiplied by 1.05 every year.", do=[E("🏦", 90, 170, 100), T("5% interest → **× 1.05** each year", x=230, y=200)]),
        dict(say="1,000 dollars becomes 1,000 times 1.05 times 1.05, which is 1,102 dollars 50, after 2 years. The interest earns interest too.", do=[MATH("1000 × 1.05 × 1.05 = 1102.50", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("10.2-k4", "One last question. Multiplying by 1.1 twice is what percentage increase? Pause the video and answer.", "× 1.1 twice is a ?% increase"),
        dict(say="1.1 times 1.1 is 1.21, which is 121 percent. So it is a 21 percent increase.", do=[MATH("1.1 × 1.1 = 1.21", x=80, y=190), B("21% increase", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: for an increase of r percent, multiply by 1 plus r over 100. For a decrease, multiply by 1 minus r over 100.", do=[T("• Increase: × (1 + r/100) · decrease: × (1 − r/100)", x=80, y=170)]),
        dict(say="One calculation gives the new amount.", do=[T("• One calculation gives the new amount", x=80, y=250)]),
        dict(say="For repeated changes, multiply the multipliers.", do=[T("• Repeated changes: multiply the multipliers", x=80, y=330)]),
        dict(say="You can turn a multiplier back into a percentage change.", do=[T("• Multiplier → percentage change", x=80, y=410)]),
    ]),
]
