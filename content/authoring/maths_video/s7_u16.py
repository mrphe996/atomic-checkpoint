# -*- coding: utf-8 -*-
"""Stage 7 · Unit 16 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG
from .s7_u04 import TBL, ROW
from .s7_u07 import F
from .s7_u11 import LG

BL, OR, INK = "#3B7DD8", "#E07A3F", "#1F2A37"
BARS = lambda labels, values, ymax, step, ylabel, x=660, y=130, w=580, at=0, colours=(BL, OR, BL, OR): FIG(x, y, w, at, kind="barchart", labels=labels, values=values, ymax=ymax, step=step, ylabel=ylabel, colours=list(colours))
PIE = lambda labels, values, x=680, y=130, w=540, at=0: FIG(x, y, w, at, kind="pie", labels=labels, values=values)
def STACK(bars, unit=24, x=700, y=140, w=500, at=0, names=("boys", "girls")):
    """A compound (stacked) bar chart of our own: bars = [(label, bottom, top)], drawn in a 480 × 340 box."""
    s = f'<line x1="70" y1="20" x2="70" y2="290" stroke="{INK}" stroke-width="3"/><line x1="70" y1="290" x2="460" y2="290" stroke="{INK}" stroke-width="3"/>'
    for i, (lab, a, b) in enumerate(bars):
        bx = 130 + i * 160; ha, hb = a * unit, b * unit
        s += f'<rect x="{bx}" y="{290 - ha}" width="90" height="{ha}" fill="{BL}"/><rect x="{bx}" y="{290 - ha - hb}" width="90" height="{hb}" fill="{OR}"/>'
        s += f'<text x="{bx + 45}" y="{290 - ha / 2 + 8}" font-size="22" font-weight="700" text-anchor="middle" fill="#fff">{a}</text><text x="{bx + 45}" y="{290 - ha - hb / 2 + 8}" font-size="22" font-weight="700" text-anchor="middle" fill="#fff">{b}</text>'
        s += f'<text x="{bx + 45}" y="320" font-size="20" font-weight="700" text-anchor="middle" fill="{INK}">{lab}</text><text x="{bx + 45}" y="{290 - ha - hb - 10}" font-size="20" font-weight="700" text-anchor="middle" fill="{INK}">{a + b}</text>'
    s += f'<rect x="330" y="24" width="18" height="18" fill="{OR}"/><text x="356" y="40" font-size="18" fill="{INK}">{names[1]}</text><rect x="330" y="50" width="18" height="18" fill="{BL}"/><text x="356" y="66" font-size="18" fill="{INK}">{names[0]}</text>'
    return T(f'<svg viewBox="0 0 480 340" width="{w}" height="{w * 340 // 480}">{s}</svg>', x=x, y=y, at=at)
LUNCH_HEAD = ["", "Pasta", "Rice", "Salad", "Total"]
LUNCH = [["Year 7", "14", "10", "6", "30"], ["Year 8", "12", "13", "9", "34"], ["Total", "26", "23", "15", "64"]]
SCREEN = lambda at=0, **k: BARS(["Sat boys", "Sat girls", "Sun boys", "Sun girls"], [4, 3, 5, 4], 6, 1, "Hours", at=at, **k)
TRAVEL = lambda at=0, **k: PIE(["Walk", "Bus", "Car", "Bike"], [60, 30, 18, 12], at=at, **k)
DROPS = lambda n, x, y, at=0: T(f'<span style="font-size:40px;letter-spacing:2px">{"💧" * n}</span>', x=x, y=y, at=at)

VIDEOS = {}

VIDEOS["16.1"] = [
    dict(kind="hook", title="School lunches", steps=[
        dict(say="A canteen records the lunches for 1 day. Students from Year 7 and Year 8 choose pasta, rice or salad. 64 students eat lunch.", do=[E("🍝", 90, 150, 100), T("**Year 7** and **Year 8** · pasta, rice or salad", x=230, y=180)]),
        dict(say="The cook wants to answer questions like: how many Year 8 students chose rice?", do=[T("“How many Year 8s chose rice?”", x=230, y=290, color=BLUE)]),
        PAUSE("16.1-k1", "Which layout records both the year and the choice: a table with rows for the years and columns for the choices, or a single list of choices? Pause the video and decide.",
              "Which layout records year AND choice: rows for years and columns for choices, or a single list of choices?"),
    ]),
    dict(kind="hook", title="Rows and columns", steps=[
        dict(say="Use rows for the years, and columns for the choices. Each number in the table then tells you 2 things at once.", do=[TBL(LUNCH_HEAD, LUNCH[:2], y=170), ROW(0, 0.5), ROW(1, 2.5), T("each number tells you **2 things**", x=80, y=390)]),
        dict(say="Find the row for Year 8, and the column for rice. They meet at 13. So 13 students in Year 8 chose rice.", do=[B("Year 8 and rice: 13", x=80, y=480, color=GREEN)]),
    ]),
    dict(kind="recall", title="Adding a row", steps=[
        dict(say="Remember: the total of a row is the sum of the numbers in it. 12 plus 9 plus 7 is 28.", do=[MATH("12 + 9 + 7 = 28", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Two-way tables", steps=[
        dict(say="A two-way table shows data sorted in 2 ways at once. Here it is sorted by year, in the rows, and by lunch, in the columns.", do=[T("**Two-way table**: sorted in **2 ways** at once", x=80, y=150), TBL(LUNCH_HEAD, LUNCH[:2], y=230), ROW(0, 0.3), ROW(1, 0.6)]),
        dict(say="Each row has a total. Year 7 has 30 students, and Year 8 has 34.", do=[T("row totals: **30** and **34**", x=640, y=280, color=BLUE)]),
        PAUSE("16.1-k2", "Look at the salad column. 6 students in Year 7 chose salad, and 9 in Year 8. How many students chose salad altogether? Pause the video and work it out.", "From the lunch table: how many students chose salad?"),
    ]),
    dict(kind="idea", title="Check: the salad column", steps=[
        dict(say="6 plus 9 is 15. Add a totals row to the table: 26 chose pasta, 23 chose rice, and 15 chose salad.", do=[TBL(LUNCH_HEAD, LUNCH, y=170), ROW(0, 0.2), ROW(1, 0.4), ROW(2, 3)]),
        dict(say="The number in the bottom right corner is the grand total: 64 students. You get 64 if you add the row totals, and also if you add the column totals.", do=[MATH("30 + 34 = 64", x=80, y=450), MATH("26 + 23 + 15 = 64", x=480, y=450, at=5)]),
    ]),
    dict(kind="idea", title="Filling in missing values", steps=[
        dict(say="Sometimes a table has gaps. Use the totals to fill them. A missing number is the total, minus the other numbers in that row or column.", do=[B("missing = total − the others", x=80, y=170, color=BLUE)]),
        dict(say="Fill a row or column that has only 1 gap. Then look for the next one.", do=[T("start where there is only **1 gap**", x=80, y=290)]),
        PAUSE("16.1-k3", "Your turn. A column reads 7, then a gap, then 11. Its total is 30. What is the missing value? Pause the video and try it.", "Column: 7, ?, 11, total 30. What is the missing value?"),
    ]),
    dict(kind="idea", title="Check: the missing value", steps=[
        dict(say="7 plus 11 is 18. 30 minus 18 is 12. The missing value is 12.", do=[MATH("7 + 11 = 18", x=80, y=190), MATH("30 − 18 = 12", x=80, y=280, at=3, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I use a two-way table?", steps=[
        dict(say="Here is the method. Step 1: read the labels. What do the rows show? What do the columns show?", do=[T("1. Read the **labels**", x=80, y=170)]),
        dict(say="Step 2: fill a gap where only 1 value is missing in a row or a column.", do=[T("2. Fill a row or column with **1 gap**", x=80, y=260)]),
        dict(say="Step 3: keep going until the table is complete.", do=[T("3. Keep going until it is **complete**", x=80, y=350)]),
        dict(say="Step 4: check the grand total both ways.", do=[T("4. **Check** the grand total both ways", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Completing a table", steps=[
        dict(say="This table shows how 56 students travel to school. Some numbers are missing. Start with the boys row: 28 minus 16 is 12 boys take the bus.",
             do=[TBL(["", "Walk", "Bus", "Total"], [["Boys", "16", "?", "28"], ["Girls", "?", "9", "?"], ["Total", "35", "?", "56"]], y=160), ROW(0, 0.3), ROW(1, 0.6), ROW(2, 0.9), MATH("boys, bus: 28 − 16 = 12", x=620, y=180, at=6)]),
        dict(say="In the walk column: 35 minus 16 is 19 girls walk. So the girls total is 19 plus 9, which is 28.", do=[MATH("girls, walk: 35 − 16 = 19", x=620, y=270), MATH("girls: 19 + 9 = 28", x=620, y=360, at=5)]),
        dict(say="The bus total is 12 plus 9, which is 21. Check: 35 plus 21 is 56. Correct.", do=[MATH("bus: 12 + 9 = 21", x=620, y=450), MATH("35 + 21 = 56 ✓", x=80, y=500, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="A fraction from the table", steps=[
        dict(say="Go back to the lunch table. What fraction of the Year 8 students chose rice?", do=[TBL(LUNCH_HEAD, LUNCH, y=160), ROW(0, 0.2), ROW(1, 0.4), ROW(2, 0.6)]),
        dict(say="The question is about Year 8, so use the Year 8 total: 34. 13 of them chose rice. The fraction is 13 over 34.", do=[MATH(F(13, 34), x=640, y=200, color=GREEN), T("use the **Year 8** total", x=760, y=240)]),
    ]),
    dict(kind="example", title="Comparing groups", steps=[
        dict(say="Did a greater proportion of Year 7, or of Year 8, choose pasta?", do=[TBL(LUNCH_HEAD, LUNCH, y=160), ROW(0, 0.2), ROW(1, 0.4), ROW(2, 0.6)]),
        dict(say="In Year 7, it is 14 out of 30. That is about 47 per cent. In Year 8, it is 12 out of 34. That is about 35 per cent.", do=[MATH(f"Year 7: {F(14, 30)} ≈ 47%", x=80, y=400), MATH(f"Year 8: {F(12, 34)} ≈ 35%", x=560, y=400, at=5)]),
        dict(say="So a greater proportion of Year 7 chose pasta.", do=[B("Year 7", x=80, y=540, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="From the lunch table: what fraction of the students who ate pasta were in Year 7? Here is Gus's working. Which line goes wrong first?",
             do=LINES("Gus", "the fraction of pasta-eaters who were in Year 7", ["Year 7 pasta = 14", "Year 7 total = 30", "Answer: 14/30"])),
        dict(say="Line 2 is wrong. The question is about the students who ate pasta. So divide by the pasta total, 26, not by the Year 7 total.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="The fraction is 14 over 26, which simplifies to 7 over 13.", do=[MATH(f"{F(14, 26)} = {F(7, 13)}", x=110, y=470, color=GREEN)]),
    ]),
    dict(kind="life", title="Two-way tables you already use", steps=[
        dict(say="A bus or train timetable is a two-way table. The rows are the stops, and the columns are the different journeys.", do=[E("🚌", 90, 160, 100), T("timetable: **stops** × **journeys**", x=230, y=190)]),
        dict(say="A multiplication square is one too. Find a row and a column, and read where they meet.", do=[E("✖️", 90, 300, 100), T("multiplication square: **row** × **column**", x=230, y=330)]),
        dict(say="And a country's census sorts millions of people in 2 ways: for example, by age group and by region.", do=[E("🌍", 90, 440, 100), T("census: **age group** × **region**", x=230, y=470)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.1-k4", "One last question. Add the row totals. Then add the column totals. Should the 2 answers be the same, or different? Pause the video and decide.", "The grand total should be the same or different whether you add the row totals or the column totals?"),
        dict(say="The same. Both ways count every person exactly once. If the answers are different, there is a mistake in the table.", do=[B("the same", x=80, y=190, color=GREEN), T("different answers → a **mistake**", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a two-way table sorts data by 2 categories at once.", do=[T("• **Two-way table**: 2 categories at once", x=80, y=170)]),
        dict(say="Use the row totals and column totals to fill the gaps.", do=[T("• Use the **totals** to fill gaps", x=80, y=250)]),
        dict(say="Check the grand total both ways.", do=[T("• Check the **grand total** both ways", x=80, y=330)]),
        dict(say="For a fraction, divide by the total of the group in the question.", do=[T("• Fractions: divide by the **right total**", x=80, y=410)]),
    ]),
]

VIDEOS["16.2"] = [
    dict(kind="hook", title="Screen time", steps=[
        dict(say="A class records its screen time at the weekend, in hours. On Saturday, the boys' average is 4 hours, and the girls' is 3. On Sunday, the boys' is 5, and the girls' is 4.",
             do=[E("📱", 90, 150, 100), TBL(["", "Boys", "Girls"], [["Saturday", "4", "3"], ["Sunday", "5", "4"]], x=230, y=170), ROW(0, 2), ROW(1, 7)]),
        PAUSE("16.2-k1", "Which chart compares the boys and the girls, day by day: a dual bar chart, with 2 bars side by side, or a single bar chart of totals? Pause the video and decide.",
              "Which chart compares boys and girls day by day: a dual bar chart or a single bar chart of totals?"),
    ]),
    dict(kind="hook", title="Two bars for each day", steps=[
        dict(say="A dual bar chart. For each day, there are 2 bars side by side: blue for the boys, and orange for the girls.", do=[SCREEN(), B("a dual bar chart", x=80, y=180, color=GREEN), T("**blue**: boys · **orange**: girls", x=80, y=290)]),
        dict(say="You can see at a glance that the boys had more screen time on both days.", do=[T("boys had more on **both days**", x=80, y=390)]),
    ]),
    dict(kind="recall", title="Reading a bar chart", steps=[
        dict(say="Remember: the height of a bar shows the frequency. Read the scale carefully. A bar that reaches halfway between 10 and 20 shows 15.", do=[T("bar height = **frequency**", x=80, y=180), MATH("halfway between 10 and 20 = 15", x=80, y=280, at=4)]),
    ]),
    dict(kind="idea", title="Dual bar charts", steps=[
        dict(say="A dual bar chart puts 2 bars side by side for each category. It uses 2 colours, and a key to explain them.", do=[SCREEN(), T("**Dual**: 2 bars side by side", x=80, y=170), T("2 colours and a **key**", x=80, y=260, at=4)]),
        dict(say="It is good for comparing 2 groups, category by category.", do=[T("good for **comparing 2 groups**", x=80, y=360)]),
        PAUSE("16.2-k2", "Your turn. On Saturday, the boys had 4 hours and the girls had 3 hours. What is the total for Saturday? Pause the video and try it.", "From the screen time data: total hours (boys + girls) on Saturday?"),
    ]),
    dict(kind="idea", title="Check: Saturday's total", steps=[
        dict(say="4 plus 3 is 7 hours. But the dual bar chart does not show that total directly. For totals, there is a better chart.", do=[MATH("4 + 3 = 7 hours", x=80, y=190, color=GREEN), T("the dual chart does not **show** the total", x=80, y=300, at=3)]),
    ]),
    dict(kind="idea", title="Compound bar charts", steps=[
        dict(say="A compound bar chart stacks the groups on top of each other, in 1 bar. It is also called a stacked bar chart.", do=[STACK([("Saturday", 4, 3), ("Sunday", 5, 4)]), T("**Compound**: the groups are **stacked**", x=80, y=170)]),
        dict(say="The total height shows the whole: 7 hours for Saturday, and 9 for Sunday. Each section shows a part.", do=[T("total height = the **whole**", x=80, y=270), T("each section = a **part**", x=80, y=350, at=5)]),
        dict(say="To read a top section, subtract. Take the top of the section, minus the bottom of the section.", do=[B("top − bottom", x=80, y=460, color=BLUE)]),
        PAUSE("16.2-k3", "Your turn. A compound bar reaches 40. Its bottom section reaches 22. How big is the top section? Pause the video and try it.", "A compound bar reaches 40; the bottom section reaches 22. How big is the top section?"),
    ]),
    dict(kind="idea", title="Check: the top section", steps=[
        dict(say="40 minus 22 is 18. The top section shows 18.", do=[MATH("40 − 22 = 18", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="Which chart, and how?", steps=[
        dict(say="Here is the method. Step 1: choose. Use a dual bar chart to compare groups. Use a compound bar chart to show totals and parts.", do=[T("1. **Dual**: compare groups · **compound**: totals and parts", x=80, y=170)]),
        dict(say="Step 2: draw the axes with a clear, even scale. Add labels and a key.", do=[T("2. Even **scale**, **labels**, a **key**", x=80, y=260)]),
        dict(say="Step 3: for a dual chart, draw 2 bars side by side for each category. For a compound chart, stack them.", do=[T("3. Side by side, or **stacked**", x=80, y=350)]),
        dict(say="Step 4: to read a stacked section, take the top minus the bottom.", do=[T("4. Stacked section: **top − bottom**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Reading a compound bar", steps=[
        dict(say="A compound bar shows the vehicles that pass a school on Monday. The whole bar reaches 32. The lower section, for bikes, reaches 19. How many scooters does the upper section show?", do=[T("bar reaches **32** · bikes reach **19** · scooters?", x=80, y=160)]),
        dict(say="Top minus bottom: 32 minus 19 is 13. There were 13 scooters.", do=[MATH("32 − 19 = 13", x=80, y=280), B("13 scooters", x=80, y=380, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Choosing a chart", steps=[
        dict(say="A shop wants to show its total sales for each month, split into online sales and sales in the store. Which chart should it use?", do=[E("🛒", 90, 140, 80), T("**total** sales, split into online and in-store", x=200, y=160)]),
        dict(say="Both the totals and the parts matter. So the shop should use a compound bar chart.", do=[B("a compound bar chart", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="example", title="Comparing two towns", steps=[
        dict(say="This dual bar chart shows rainfall, in millimetres. Town A had 70 in January and 50 in February. Town B had 90 in January and 40 in February.",
             do=[BARS(["Jan A", "Jan B", "Feb A", "Feb B"], [70, 90, 50, 40], 100, 10, "Rain (mm)"), T("**blue**: Town A · **orange**: Town B", x=80, y=170)]),
        dict(say="Which town had more rain in total? Town A: 70 plus 50 is 120. Town B: 90 plus 40 is 130.", do=[MATH("A: 70 + 50 = 120", x=80, y=280), MATH("B: 90 + 40 = 130", x=80, y=370, at=5)]),
        dict(say="Town B had more rain in total, even though it had less in February.", do=[B("Town B", x=80, y=470, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A compound bar shows fruit sold. The lower section, for apples, reaches 24. The whole bar reaches 45. How many pears does the upper section show? Here is Wren's working. Which line goes wrong first?",
             do=LINES("Wren", "apples reach 24, the bar reaches 45: how many pears?", ["The pears section ends at 45", "So there are 45 pears"])),
        dict(say="Line 2 is wrong. 45 is the total for apples and pears together. The pears section starts at 24, not at 0.", do=[dict(a="cross", id="l2")]),
        dict(say="45 minus 24 is 21. There are 21 pears.", do=[B("45 − 24 = 21 pears", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Charts in the news", steps=[
        dict(say="An Olympic medal table is often drawn as a compound bar chart. Each country's bar is split into gold, silver and bronze.", do=[E("🏅", 90, 160, 100), T("medals: **gold**, **silver**, **bronze** stacked", x=230, y=190)]),
        dict(say="Weather websites use dual bar charts to compare 2 cities, month by month.", do=[E("🌦️", 90, 300, 100), T("2 cities, month by month: **dual** bars", x=230, y=330)]),
        dict(say="Before you read any chart, look for the key. It tells you what each colour means.", do=[B("always read the key", x=230, y=460, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.2-k4", "One last question. To show totals and parts, do you use a compound bar chart, or a dual bar chart? Pause the video and answer.", "To show totals AND parts, use a compound bar chart or a dual bar chart?"),
        dict(say="A compound bar chart. The height of the whole bar is the total, and the sections are the parts.", do=[STACK([("Saturday", 4, 3), ("Sunday", 5, 4)]), B("compound", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a dual bar chart has bars side by side. It compares 2 groups.", do=[T("• **Dual**: side by side – compares 2 groups", x=80, y=170)]),
        dict(say="A compound bar chart has stacked parts. It shows totals and parts.", do=[T("• **Compound**: stacked – totals and parts", x=80, y=250)]),
        dict(say="Use a clear scale, labels and a key.", do=[T("• A clear **scale**, **labels** and a **key**", x=80, y=330)]),
        dict(say="For a stacked section, take the top minus the bottom.", do=[T("• Stacked section: **top − bottom**", x=80, y=410)]),
    ]),
]

VIDEOS["16.3"] = [
    dict(kind="hook", title="Getting to school", steps=[
        dict(say="A survey asks 120 students how they travel to school. Half of them walk. A quarter take the bus. The rest come by car or by bike.", do=[E("🚶", 90, 150, 100), T("**120** students · half walk · a quarter take the bus", x=230, y=180)]),
        dict(say="A pie chart shows these parts of the whole as slices of a circle.", do=[TRAVEL(at=0.4, x=780, y=250, w=420), T("a **pie chart**: slices of a circle", x=230, y=290)]),
        PAUSE("16.3-k1", "A full circle is 360 degrees. What angle shows the half who walk? Pause the video and work it out.", "What angle shows 'half walk'?"),
    ]),
    dict(kind="hook", title="Half of 360", steps=[
        dict(say="Half of 360 is 180. The sector for walking has an angle of 180 degrees. It is half of the circle.", do=[TRAVEL(), MATH("360 ÷ 2 = 180°", x=80, y=190, color=GREEN)]),
        dict(say="A quarter of 360 is 90. So the bus sector has an angle of 90 degrees.", do=[MATH("360 ÷ 4 = 90°", x=80, y=290)]),
    ]),
    dict(kind="recall", title="Fractions of 360", steps=[
        dict(say="Remember: a full turn is 360 degrees. Half is 180. A quarter is 90. And 1 tenth is 36.", do=[MATH(f"{F(1, 2)} → 180°", x=80, y=170), MATH(f"{F(1, 4)} → 90°", x=80, y=300, at=3), MATH(f"{F(1, 10)} → 36°", x=80, y=430, at=5)]),
    ]),
    dict(kind="idea", title="Pie charts", steps=[
        dict(say="A pie chart is a circle, split into sectors. The angle of each sector is in proportion to its frequency.", do=[T("**Pie chart**: a circle split into **sectors**", x=80, y=150)]),
        dict(say="To find an angle: divide the frequency by the total, then multiply by 360.", do=[MATH("angle = frequency ÷ total × 360°", x=80, y=230, color=BLUE)]),
        dict(say="18 students come by car. 18 divided by 120, times 360, is 54 degrees. 12 come by bike. That is 36 degrees.",
             do=[TBL(["Travel", "Students", "Angle"], [["Walk", "60", "180°"], ["Bus", "30", "90°"], ["Car", "18", "54°"], ["Bike", "12", "36°"]], y=320), ROW(0, 0.2), ROW(1, 0.4), ROW(2, 4), ROW(3, 8)]),
        PAUSE("16.3-k2", "Your turn. The total is 72. 1 group has 18. What angle does that group need? Pause the video and try it.", "Total 72; one group 18. What is the angle?"),
    ]),
    dict(kind="idea", title="Check: 18 out of 72", steps=[
        dict(say="18 out of 72 is 1 quarter. A quarter of 360 is 90 degrees.", do=[MATH(f"{F(18, 72)} = {F(1, 4)}", x=80, y=180), B("90°", x=80, y=330, color=GREEN, at=3)]),
    ]),
    dict(kind="idea", title="Reading a pie chart", steps=[
        dict(say="You can also go from an angle back to a frequency. Divide the angle by 360, then multiply by the total.", do=[MATH("frequency = angle ÷ 360 × total", x=80, y=160, color=BLUE)]),
        dict(say="A pie chart shows 240 students. The sector for drama is 45 degrees. 45 over 360 is 1 eighth. 1 eighth of 240 is 30 students.", do=[MATH(f"{F(45, 360)} = {F(1, 8)}", x=80, y=270), MATH("240 ÷ 8 = 30 students", x=80, y=410, at=7)]),
        PAUSE("16.3-k3", "Your turn. The total is 180. A sector has an angle of 60 degrees. What is the frequency? Pause the video and try it.", "Total 180; sector 60°. What is the frequency?"),
    ]),
    dict(kind="idea", title="Check: a 60° sector", steps=[
        dict(say="60 over 360 is 1 sixth. 1 sixth of 180 is 30. The frequency is 30.", do=[MATH(f"{F(60, 360)} = {F(1, 6)}", x=80, y=180), MATH("180 ÷ 6 = 30", x=80, y=320, at=3, color=GREEN)]),
    ]),
    dict(kind="idea", title="Waffle diagrams", steps=[
        dict(say="A waffle diagram is a grid of 100 squares: 10 rows of 10. Each square is 1 per cent.", do=[FIG(700, 130, 520, 0, kind="waffle", n=45, title="45% walk on a rainy day"), T("**Waffle**: 100 squares · each is **1%**", x=80, y=170)]),
        dict(say="This waffle has 45 squares shaded. It shows 45 per cent. Waffles make percentages easy to count.", do=[B("45 squares = 45%", x=80, y=290, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I draw a pie chart?", steps=[
        dict(say="Here is the method. Step 1: find the total frequency.", do=[T("1. Find the **total**", x=80, y=170)]),
        dict(say="Step 2: work out the degrees for 1 item: 360 divided by the total. Then multiply by each frequency.", do=[T("2. **360 ÷ total** = degrees for 1 item", x=80, y=260)]),
        dict(say="Step 3: draw each angle with a protractor.", do=[T("3. Draw with a **protractor**", x=80, y=350)]),
        dict(say="Step 4: check that the angles add up to 360 degrees. Add labels or a key.", do=[T("4. Check: the angles add up to **360°**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Degrees for each person", steps=[
        dict(say="40 people choose their favourite sport. 16 choose football, 14 choose tennis, and 10 choose swimming. Find the angles for a pie chart.", do=[T("**40** people: football **16**, tennis **14**, swimming **10**", x=80, y=160)]),
        dict(say="360 divided by 40 is 9. So each person gets 9 degrees.", do=[MATH("360 ÷ 40 = 9° per person", x=80, y=260)]),
        dict(say="Football: 16 times 9 is 144 degrees. Tennis: 14 times 9 is 126 degrees. Swimming: 10 times 9 is 90 degrees.", do=[MATH("144°, 126°, 90°", x=80, y=350, color=GREEN), PIE(["Football", "Tennis", "Swimming"], [16, 14, 10], x=760, y=230, w=440, at=4)]),
        dict(say="Check: 144 plus 126 plus 90 is 360.", do=[MATH("144 + 126 + 90 = 360 ✓", x=80, y=450)]),
    ]),
    dict(kind="example", title="From a waffle to a number", steps=[
        dict(say="A waffle diagram has 28 squares shaded, for people who own a pet. 350 people were asked. How many own a pet?", do=[FIG(760, 150, 440, 0, kind="waffle", n=28, title="own a pet"), T("**28** squares · **350** people", x=80, y=170)]),
        dict(say="28 squares means 28 per cent. 0.28 times 350 is 98. So 98 people own a pet.", do=[MATH("0.28 × 350 = 98", x=80, y=280), B("98 people", x=80, y=380, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="Two pie charts", steps=[
        dict(say="School A has 600 students. On its pie chart, the sport sector is 60 degrees. School B has 240 students. Its sport sector is 120 degrees. Which school has more students who chose sport?",
             do=[TBL(["School", "Students", "Sport sector"], [["A", "600", "60°"], ["B", "240", "120°"]], y=160), ROW(0, 0.3), ROW(1, 6)]),
        dict(say="School A: 60 over 360 is 1 sixth. 1 sixth of 600 is 100 students.", do=[MATH("A: 600 ÷ 6 = 100", x=80, y=360)]),
        dict(say="School B: 120 over 360 is 1 third. 1 third of 240 is 80 students. School A has more, even though its sector is smaller.", do=[MATH("B: 240 ÷ 3 = 80", x=80, y=450), B("School A", x=560, y=400, color=GREEN, at=6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="2 pie charts show favourite sports. Class A has 20 students, and its football sector is 180 degrees. Class B has 40 students, and its football sector is 90 degrees. Here is Dev's working. Which line goes wrong first?",
             do=LINES("Dev", "Class A (20 students) 180° · Class B (40 students) 90°", ["Class A's sector is bigger", "So more students in Class A like football"])),
        dict(say="Line 2 is wrong. A pie chart shows proportions, not numbers. You must use the totals.", do=[dict(a="cross", id="l2")]),
        dict(say="Half of 20 is 10. A quarter of 40 is 10. The 2 classes have the same number.", do=[B("10 and 10: the same", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="The air around you", steps=[
        dict(say="A pie chart of the air you breathe has 1 huge sector. About 78 per cent of air is nitrogen.", do=[PIE(["Nitrogen", "Oxygen", "Other"], [78, 21, 1]), T("nitrogen: about **78%**", x=80, y=180)]),
        dict(say="About 21 per cent is oxygen. All the other gases together make up only about 1 per cent.", do=[T("oxygen: about **21%**", x=80, y=270), T("other gases: about **1%**", x=80, y=360, at=3)]),
        dict(say="On a waffle diagram, that is 78 squares, 21 squares, and just 1 square.", do=[B("78 + 21 + 1 = 100", x=80, y=470, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.3-k4", "One last question. A waffle diagram has 27 squares shaded. What percentage does it show? Pause the video and answer.", "A waffle with 27 squares shaded shows ?%"),
        dict(say="27 per cent. On a waffle diagram, each square is 1 per cent.", do=[FIG(760, 150, 440, 0, kind="waffle", n=27, title=""), B("27%", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the angle on a pie chart is the frequency, divided by the total, times 360.", do=[T("• Angle = frequency ÷ total **× 360°**", x=80, y=170)]),
        dict(say="The frequency is the angle, divided by 360, times the total.", do=[T("• Frequency = angle ÷ 360 **× total**", x=80, y=250)]),
        dict(say="A waffle diagram has 100 squares. Each one is 1 per cent.", do=[T("• **Waffle**: 100 squares, each **1%**", x=80, y=330)]),
        dict(say="Pie charts show proportions. Check the totals before you compare 2 charts.", do=[T("• Pie charts show **proportions** – check the totals", x=80, y=410)]),
    ]),
]

VIDEOS["16.4"] = [
    dict(kind="hook", title="Facts at a glance", steps=[
        dict(say="A poster from a water company says: a shower uses 60 litres of water, and a bath uses 150 litres. It uses pictures of water droplets. 1 droplet stands for 10 litres.", do=[E("🚿", 90, 150, 100), T("shower **60 litres** · bath **150 litres**", x=230, y=180), T("💧 = **10 litres**", x=230, y=280, at=7)]),
        PAUSE("16.4-k1", "How many droplets does the poster need for the shower? Pause the video and work it out.", "1 droplet = 10 litres. How many droplets for a 60 litre shower?"),
    ]),
    dict(kind="hook", title="Count the droplets", steps=[
        dict(say="60 divided by 10 is 6. The shower needs 6 droplets.", do=[T("shower", x=80, y=180), DROPS(6, 230, 165), MATH("60 ÷ 10 = 6", x=760, y=170, color=GREEN)]),
        dict(say="The bath needs 15 droplets. You can see at once that a bath uses much more water.", do=[T("bath", x=80, y=300), DROPS(15, 230, 285), MATH("150 ÷ 10 = 15", x=80, y=420)]),
    ]),
    dict(kind="recall", title="Reading a key", steps=[
        dict(say="Remember: the key tells you what 1 symbol stands for. If 1 symbol is 10 items, then half a symbol is 5 items.", do=[T("1 symbol = 10 → half a symbol = **5**", x=80, y=180)]),
        dict(say="If 1 icon is 20 people, then 3 and a half icons show 70 people.", do=[MATH("3.5 × 20 = 70", x=80, y=290)]),
    ]),
    dict(kind="idea", title="What is an infographic?", steps=[
        dict(say="An infographic mixes pictures, icons, a few words and simple charts. It is designed to give information quickly.", do=[T("**Infographic**: pictures + icons + words + charts", x=80, y=150)]),
        dict(say="It often has a pictogram, with a key. It may have 1 big number as a headline. And it may have a small bar chart or pie chart.",
             do=[TBL(["Part", "Example"], [["pictogram", "💧 = 10 litres"], ["big number", "“150 litres for one bath”"], ["small chart", "a pie chart of how water is used"]], y=240), ROW(0, 0.3), ROW(1, 4), ROW(2, 7)]),
        PAUSE("16.4-k2", "Your turn. 1 icon stands for 50 people. How many people do 7 icons show? Pause the video and try it.", "1 icon = 50 people. 7 icons = ?"),
    ]),
    dict(kind="idea", title="Check: 7 icons", steps=[
        dict(say="7 times 50 is 350 people.", do=[MATH("7 × 50 = 350 people", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Read with care", steps=[
        dict(say="Infographics are made to grab your attention. So read them with care. First, check the scale. All the icons should be the same size.", do=[T("check the **scale**: icons the same size?", x=80, y=160)]),
        dict(say="Second, check the source. Who collected the data? How many people were asked?", do=[T("check the **source** and the **sample size**", x=80, y=250)]),
        dict(say="Third, watch out for pictures that grow in 2 directions. A picture drawn 2 times as tall, and 2 times as wide, covers 4 times the area.",
             do=[T('<svg viewBox="0 0 400 220" width="400" height="220"><rect x="20" y="130" width="70" height="70" fill="#3B7DD8"/><rect x="160" y="60" width="140" height="140" fill="#E07A3F"/></svg>', x=760, y=320), MATH("2 × 2 = 4 times the area", x=80, y=380, color=RED)]),
        PAUSE("16.4-k3", "Your turn. A picture is drawn 3 times as tall, and 3 times as wide. How many times as big does it look: 9, or 3? Pause the video and decide.", "A picture is drawn 3 times as tall and 3 times as wide. It looks … times as big."),
    ]),
    dict(kind="idea", title="Check: three times each way", steps=[
        dict(say="3 times 3 is 9. The picture covers 9 times the area, so it looks 9 times as big.", do=[MATH("3 × 3 = 9", x=80, y=190), B("9 times as big", x=80, y=290, color=GREEN, at=2.6)]),
    ]),
    dict(kind="method", title="How do I read an infographic?", steps=[
        dict(say="Here is the method. Step 1: find the headline message.", do=[T("1. Find the **headline**", x=80, y=170)]),
        dict(say="Step 2: read the key and the units. Turn the icons into numbers.", do=[T("2. Read the **key** · icons → numbers", x=80, y=260)]),
        dict(say="Step 3: check the scale, the source and the sample size.", do=[T("3. Check the **scale**, **source** and **sample**", x=80, y=350)]),
        dict(say="Step 4: decide. Does the picture match the numbers fairly?", do=[T("4. Does the picture match the numbers **fairly**?", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Icons into numbers", steps=[
        dict(say="On a forest poster, 1 tree icon stands for 200 trees. A hillside has 6 and a half icons. How many trees is that?", do=[T('<span style="font-size:44px">🌲🌲🌲🌲🌲🌲</span>', x=80, y=150), T("+ half an icon · 🌲 = **200 trees**", x=520, y=170)]),
        dict(say="6.5 times 200 is 1,300 trees.", do=[MATH("6.5 × 200 = 1300", x=80, y=290), B("1300 trees", x=80, y=390, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="A headline number", steps=[
        dict(say="A school poster says: 2 in every 5 students play a sport each week. The school has 900 students. How many play a sport each week?", do=[E("⚽", 90, 140, 80), T("“**2 in 5** students play a sport each week” · **900** students", x=200, y=160)]),
        dict(say="1 fifth of 900 is 180. So 2 fifths is 2 times 180, which is 360 students.", do=[MATH("900 ÷ 5 = 180", x=80, y=290), MATH("2 × 180 = 360", x=80, y=380, at=3), B("360 students", x=80, y=480, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Check the source", steps=[
        dict(say="An advert says: 8 out of 10 cat owners prefer our cat food. In small print, it says that 10 owners were asked, in the company's own shop. Comment on the claim.", do=[E("🐱", 90, 140, 80), T("“**8 out of 10** cat owners prefer our food”", x=200, y=160), T("small print: 10 owners, in the company's own shop", x=200, y=250, color=GREY, at=5)]),
        dict(say="10 people is a tiny sample. And they were already shopping in that company's shop, so the sample is not fair.", do=[T("a **tiny** sample · **not fair**", x=80, y=370, color=RED)]),
        dict(say="So the claim is not reliable.", do=[B("not reliable", x=80, y=470, color=RED)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A poster shows 2 house icons. 1 is drawn 2 times as tall and 2 times as wide as the other, to show 2 times as many houses. Here is Lars's comment. Which line goes wrong first?",
             do=LINES("Lars", "an icon drawn 2 times as tall and 2 times as wide", ["The bigger icon is twice the size", "So it fairly shows twice as many"])),
        dict(say="Line 1 is wrong. 2 times as tall and 2 times as wide gives 4 times the area. The icon looks 4 times as big.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="The picture exaggerates. A fair poster would draw 2 icons of the same size.", do=[B("draw 2 icons of the same size", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Pictures instead of words", steps=[
        dict(say="Infographics are everywhere. Exit signs, and signs in airports, use simple pictures. People can understand them in any language.", do=[E("🚪", 90, 160, 100), T("signs that work in **any language**", x=230, y=190)]),
        dict(say="Weather apps use icons and a few numbers, to show a whole week on 1 small screen.", do=[E("🌤️", 90, 300, 100), T("a whole week on **one screen**", x=230, y=330)]),
        dict(say="And many food packets use red, amber and green labels, to show sugar, salt and fat at a glance.", do=[E("🚦", 90, 440, 100), T("red, amber, green: sugar, salt and fat", x=230, y=470)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.4-k4", "One last question. Which makes a claim more reliable: a large, fair sample, or bright colours? Pause the video and answer.", "Which makes a claim more reliable: a large, fair sample or bright colours?"),
        dict(say="A large, fair sample. Bright colours make a poster look good, but they do not make it true.", do=[B("a large, fair sample", x=80, y=190, color=GREEN), T("colours do not make it **true**", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: infographics combine pictures, numbers and simple charts.", do=[T("• **Infographic**: pictures, numbers, simple charts", x=80, y=170)]),
        dict(say="Use the key to turn icons into numbers.", do=[T("• Use the **key**: icons → numbers", x=80, y=250)]),
        dict(say="Check the scale, the source and the sample size.", do=[T("• Check the **scale**, **source** and **sample**", x=80, y=330)]),
        dict(say="Pictures that grow in 2 directions exaggerate the difference.", do=[T("• Growing in 2 directions **exaggerates**", x=80, y=410)]),
    ]),
]

HEIGHT = lambda at=0, **k: LG(dict(min=5, max=12, step=1, label="Age (years)"), dict(min=100, max=160, step=10, label="Height (cm)"), [[5, 110], [6, 116], [7, 122], [8, 127], [9, 133], [10, 138], [11, 144], [12, 150]], at=at, **k)

VIDEOS["16.5"] = [
    dict(kind="hook", title="Choosing the right chart", steps=[
        dict(say="You have 3 sets of data. First: your height on every birthday, from age 5 to age 12.", do=[T("1. your **height** on every birthday", x=80, y=170)]),
        dict(say="Second: how 30 classmates travel to school. Third: test scores for boys and girls, in 4 subjects.", do=[T("2. how 30 classmates **travel** to school", x=80, y=260), T("3. test scores: **boys and girls**, 4 subjects", x=80, y=350, at=4)]),
        PAUSE("16.5-k1", "Start with your height on every birthday. Is that best shown on a line graph, or on a pie chart? Pause the video and decide.", "Height every birthday is best shown on a line graph or a pie chart?"),
    ]),
    dict(kind="hook", title="Change over time", steps=[
        dict(say="A line graph. Your height changes over time, and a line graph shows that change clearly.", do=[HEIGHT(), B("a line graph", x=80, y=180, color=GREEN), T("it shows **change over time**", x=80, y=290)]),
    ]),
    dict(kind="recall", title="Types of data", steps=[
        dict(say="Remember the 3 types of data. Categorical data is words, like colours. Discrete data is counted, like the number of pets. Continuous data is measured, like height.",
             do=[T("**categorical**: words", x=80, y=170), T("**discrete**: counted", x=80, y=260, at=4), T("**continuous**: measured", x=80, y=350, at=8)]),
    ]),
    dict(kind="idea", title="Which chart for which data?", steps=[
        dict(say="Different charts do different jobs. A bar chart compares categories, or counts.",
             do=[TBL(["Chart", "Best for", "Example"], [["bar chart", "comparing categories", "favourite sports"], ["dual bar chart", "comparing 2 groups", "boys and girls"], ["line graph", "change over time", "height each year"], ["pie chart or waffle", "parts of a whole", "how a class travels"]], y=170), ROW(0, 0.3)]),
        dict(say="A dual bar chart compares 2 groups. A line graph shows change over time.", do=[ROW(1, 0.3), ROW(2, 3)]),
        PAUSE("16.5-k2", "Your turn. Which chart shows the parts of a whole: a pie chart, or a line graph? Pause the video and decide.", "To show parts of a whole, use a pie chart or a line graph?"),
    ]),
    dict(kind="idea", title="Check: parts of a whole", steps=[
        dict(say="A pie chart. Each sector is 1 part, and the whole circle is the whole group. A waffle diagram does the same job.",
             do=[FIG(700, 130, 520, 0, kind="pie", labels=["Walk", "Bus", "Car"], values=[15, 10, 5]), B("a pie chart", x=80, y=190, color=GREEN), T("or a **waffle** diagram", x=80, y=300, at=5)]),
    ]),
    dict(kind="idea", title="What makes a good chart?", steps=[
        dict(say="A good chart has a title. Its axes have labels, with units.", do=[T("a **title** · axis **labels** with **units**", x=80, y=170)]),
        dict(say="The scale goes up in equal steps. For a bar chart, it should start at 0.", do=[T("an **even scale** · bars start at **0**", x=80, y=260)]),
        dict(say="If there are colours, there is a key. And a good chart says where the data came from.", do=[T("a **key** · the **source** of the data", x=80, y=350)]),
    ]),
    dict(kind="method", title="How do I choose a chart?", steps=[
        dict(say="Here is the method. Step 1: what type of data is it? Is it measured over time?", do=[T("1. What **type** of data? Over **time**?", x=80, y=170)]),
        dict(say="Step 2: what do you want to show? A comparison, the parts of a whole, or a trend?", do=[T("2. **Compare**, **parts of a whole**, or a **trend**?", x=80, y=260)]),
        dict(say="Step 3: pick the chart, and draw it carefully.", do=[T("3. **Pick** the chart · draw it carefully", x=80, y=350)]),
        dict(say="Step 4: add the title, the labels, the units and a key.", do=[T("4. Title, labels, units, key", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Shares of a whole", steps=[
        dict(say="A café records the drinks it sells in 1 day: 90 coffees, 45 teas, 30 juices and 15 bottles of water. Which chart shows the share of each drink?", do=[E("☕", 90, 140, 80), T("coffee **90** · tea **45** · juice **30** · water **15**", x=200, y=160)]),
        dict(say="The shares are parts of a whole, so use a pie chart. The total is 180 drinks, so each drink gets 2 degrees.", do=[B("a pie chart", x=80, y=270, color=GREEN), MATH("360 ÷ 180 = 2° per drink", x=80, y=370, at=4)]),
        dict(say="The angles are 180 degrees, 90 degrees, 60 degrees and 30 degrees.", do=[MATH("180°, 90°, 60°, 30°", x=80, y=460), PIE(["Coffee", "Tea", "Juice", "Water"], [90, 45, 30, 15], x=760, y=230, w=440)]),
    ]),
    dict(kind="example", title="A trend", steps=[
        dict(say="A town records its population every year, from 2015 to 2024. Which chart should it use?", do=[E("🏘️", 90, 140, 80), T("population **every year**, 2015 to 2024", x=200, y=160)]),
        dict(say="The data changes over time, so a line graph is best. It shows the trend: is the population rising, or falling?", do=[B("a line graph", x=80, y=290, color=GREEN), T("it shows the **trend**", x=80, y=400)]),
        PAUSE("16.5-k3", "Your turn. You want to compare the scores of 2 classes, in 3 tests. Do you use a dual bar chart, or a pie chart? Pause the video and decide.", "Comparing two classes' scores in 3 tests: dual bar chart or pie chart?"),
    ]),
    dict(kind="example", title="Check: two classes, three tests", steps=[
        dict(say="A dual bar chart. For each test, draw 2 bars side by side: 1 for each class.", do=[B("a dual bar chart", x=80, y=190, color=GREEN), T("2 bars side by side for **each test**", x=80, y=300)]),
    ]),
    dict(kind="example", title="Improving a chart", steps=[
        dict(say="A bar chart has no title. Its axis starts at 20. And there are no units. How can you improve it?", do=[T("no title · axis starts at **20** · no units", x=80, y=160, color=RED)]),
        dict(say="Add a title. Start the axis at 0, so that the heights of the bars can be compared fairly. And label the axis, with its units.", do=[T("add a **title**", x=80, y=280), T("start the axis at **0**", x=80, y=360, at=2), T("label the axis with **units**", x=80, y=440, at=6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A survey of favourite fruit finds: apple 8, banana 5, mango 11. Here is Ines's plan for a chart. Which line goes wrong first?",
             do=LINES("Ines", "apple 8, banana 5, mango 11", ["Plot a point for apple, banana and mango", "Join the points with lines, to make a line graph"])),
        dict(say="Line 2 is wrong. Fruit names are categories. There is nothing in between apple and banana, so joining the points has no meaning.", do=[dict(a="cross", id="l2")]),
        dict(say="Use a bar chart for categories.", do=[B("use a bar chart", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="When a chart misleads", steps=[
        dict(say="Be careful with bar charts in adverts. 2 phones score 52 and 55 in a test. If the axis starts at 50, the bars are 2 units and 5 units tall.", do=[E("📊", 90, 160, 100), T("scores **52** and **55** · axis starts at **50**", x=230, y=190)]),
        dict(say="The second bar looks more than 2 times as tall. But 55 is only about 6 per cent more than 52.", do=[MATH("bars: 2 and 5 units", x=230, y=300), MATH("really: about 6% more", x=230, y=390, color=RED, at=4)]),
        dict(say="So always look at where the axis starts.", do=[B("where does the axis start?", x=230, y=500, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.5-k4", "One last question. The axis of a bar chart should usually start at which number: 0, or the smallest value in the data? Pause the video and answer.", "Bar chart axes should usually start at 0 or the smallest value?"),
        dict(say="At 0. Then the height of each bar matches its value, and the comparison is fair.", do=[B("start at 0", x=80, y=190, color=GREEN), T("then the bar heights are **fair**", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: bar charts compare categories. Dual bar charts compare 2 groups.", do=[T("• **Bar**: categories · **dual bar**: 2 groups", x=80, y=170)]),
        dict(say="Pie charts and waffle diagrams show the parts of a whole.", do=[T("• **Pie** and **waffle**: parts of a whole", x=80, y=250)]),
        dict(say="Line graphs show change over time.", do=[T("• **Line graph**: change over time", x=80, y=330)]),
        dict(say="A good chart has a title, labels, units, a key and a fair scale.", do=[T("• Title, labels, units, key, **fair scale**", x=80, y=410)]),
    ]),
]

VIDEOS["16.6"] = [
    dict(kind="hook", title="Who is the better player?", steps=[
        dict(say="2 basketball players record their points in their last 5 games. Ana scores 12, 15, 11, 14 and 13. Bo scores 4, 25, 9, 22 and 5.",
             do=[E("🏀", 90, 150, 100), TBL(["Player", "Points in 5 games"], [["Ana", "12, 15, 11, 14, 13"], ["Bo", "4, 25, 9, 22, 5"]], x=230, y=170), ROW(0, 3), ROW(1, 8)]),
        PAUSE("16.6-k1", "What is the mean of Ana's points? Pause the video and work it out.", "What is Ana's mean number of points (12, 15, 11, 14, 13)?"),
    ]),
    dict(kind="hook", title="The same mean", steps=[
        dict(say="Add Ana's points: the total is 65. Divide by 5 games. Her mean is 13 points.", do=[MATH("12 + 15 + 11 + 14 + 13 = 65", x=80, y=170), MATH("65 ÷ 5 = 13", x=80, y=260, at=3, color=GREEN)]),
        dict(say="Now Bo. His total is also 65, so his mean is 13 too. But the 2 players are very different. We need more than the mean to compare them.", do=[MATH("Bo: 65 ÷ 5 = 13", x=80, y=380), T("the same mean, but **very different** players", x=80, y=480, at=5)]),
    ]),
    dict(kind="recall", title="Putting data in order", steps=[
        dict(say="Remember: it helps to write data in order, smallest first. Ana's points in order are 11, 12, 13, 14, 15. Bo's are 4, 5, 9, 22, 25.", do=[MATH("Ana: 11, 12, 13, 14, 15", x=80, y=180), MATH("Bo: 4, 5, 9, 22, 25", x=80, y=280, at=5)]),
    ]),
    dict(kind="idea", title="Three averages", steps=[
        dict(say="There are 3 kinds of average. The mode is the most common value. Ana and Bo have no mode, because no score is repeated.",
             do=[TBL(["Average", "How to find it", "Ana", "Bo"], [["mode", "the most common value", "none", "none"], ["median", "the middle value, in order", "13", "9"], ["mean", "total ÷ number of values", "13", "13"]], y=170), ROW(0, 3)]),
        dict(say="The median is the middle value, when the data is in order. Ana's median is 13. Bo's median is 9.", do=[ROW(1, 0.3)]),
        dict(say="The mean is the total, divided by the number of values. Both means are 13.", do=[ROW(2, 0.3)]),
        PAUSE("16.6-k2", "Your turn. Find the mean of 4, 8, 6 and 2. Pause the video and try it.", "What is the mean of 4, 8, 6, 2?"),
    ]),
    dict(kind="idea", title="Check: the mean of 4, 8, 6, 2", steps=[
        dict(say="The total is 20. There are 4 values. 20 divided by 4 is 5. The mean is 5.", do=[MATH("4 + 8 + 6 + 2 = 20", x=80, y=190), MATH("20 ÷ 4 = 5", x=80, y=280, at=3, color=GREEN)]),
    ]),
    dict(kind="idea", title="The range", steps=[
        dict(say="The range tells you how spread out the data is. It is the largest value, minus the smallest value.", do=[B("range = largest − smallest", x=80, y=160, color=BLUE)]),
        dict(say="Ana's range is 15 minus 11, which is 4. Bo's range is 25 minus 4, which is 21.", do=[MATH("Ana: 15 − 11 = 4", x=80, y=280), MATH("Bo: 25 − 4 = 21", x=80, y=370, at=4)]),
        dict(say="Ana's scores are close together, so she is consistent. Bo has some great games, and some poor ones.", do=[T("Ana: **consistent** · Bo: up and down", x=80, y=480)]),
    ]),
    dict(kind="idea", title="A median between two values", steps=[
        dict(say="With an even number of values, there are 2 middle values. The median is halfway between them.", do=[T("an **even** number of values → **2** middle values", x=80, y=150)]),
        dict(say="Find the median of 9, 2, 14, 7, 11 and 4. In order: 2, 4, 7, 9, 11, 14. The middle values are 7 and 9.", do=[MATH("2, 4, 7, 9, 11, 14", x=80, y=250), T("middle values: **7** and **9**", x=80, y=340, at=7)]),
        dict(say="Halfway between 7 and 9 is 8. The median is 8.", do=[MATH("(7 + 9) ÷ 2 = 8", x=80, y=430, color=GREEN)]),
        PAUSE("16.6-k3", "Your turn. Find the median of 3, 9, 4 and 7. Pause the video and try it.", "What is the median of 3, 9, 4, 7?"),
    ]),
    dict(kind="idea", title="Check: the median of 3, 9, 4, 7", steps=[
        dict(say="In order: 3, 4, 7, 9. The middle values are 4 and 7. Halfway between them is 5.5.", do=[MATH("3, 4, 7, 9", x=80, y=190), MATH("(4 + 7) ÷ 2 = 5.5", x=80, y=280, at=3, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I compare two sets of data?", steps=[
        dict(say="Here is the method. Step 1: find an average for each set.", do=[T("1. Find an **average** for each", x=80, y=170)]),
        dict(say="Step 2: find the range for each set.", do=[T("2. Find the **range** for each", x=80, y=260)]),
        dict(say="Step 3: compare. Which average is higher? Which range is smaller?", do=[T("3. Higher **average**? Smaller **range**?", x=80, y=350)]),
        dict(say="Step 4: write 2 sentences, about the real situation.", do=[T("4. Write **2 sentences** about the situation", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="The mode", steps=[
        dict(say="7 students give their shoe sizes: 3, 5, 5, 6, 5, 8 and 3. Find the mode.", do=[E("👟", 90, 140, 80), MATH("3, 5, 5, 6, 5, 8, 3", x=200, y=150)]),
        dict(say="Size 5 appears 3 times. That is more than any other size. So the mode is 5.", do=[T("5 appears **3 times**", x=80, y=280), B("mode = 5", x=80, y=380, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Comparing two classes", steps=[
        dict(say="2 classes take the same test. Class A has a mean of 68 and a range of 12. Class B has a mean of 61 and a range of 30. Compare them.",
             do=[TBL(["Class", "Mean", "Range"], [["A", "68", "12"], ["B", "61", "30"]], y=160), ROW(0, 0.3), ROW(1, 5)]),
        dict(say="Class A has the higher mean. So on average, Class A scored higher.", do=[T("68 > 61 → Class A scored **higher** on average", x=80, y=360)]),
        dict(say="Class A also has the smaller range. So its scores were more consistent.", do=[T("12 < 30 → Class A was **more consistent**", x=80, y=450)]),
    ]),
    dict(kind="example", title="Which average?", steps=[
        dict(say="5 people work at a small company. Their salaries, in thousands of dollars, are 18, 20, 21, 23 and 168. Which average shows a typical salary?", do=[MATH("18, 20, 21, 23, 168", x=80, y=160), T("(thousands of dollars)", x=520, y=180, color=GREY)]),
        dict(say="The total is 250, so the mean is 50. But that is more than 4 of the 5 people earn. 1 huge salary pulls the mean up.", do=[MATH("mean: 250 ÷ 5 = 50", x=80, y=280, color=RED)]),
        dict(say="The median is the middle value: 21. That is a much better picture of a typical salary.", do=[MATH("median: 21", x=80, y=380, color=GREEN), T("use the **median** when 1 value is extreme", x=80, y=480, at=4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Find the median of 8, 3, 6, 1 and 5. Here is Tom's working. Which line goes wrong first?", do=LINES("Tom", "the median of 8, 3, 6, 1, 5", ["The middle value of the list is 6", "Median = 6"])),
        dict(say="Line 1 is wrong. You must put the data in order first.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="In order: 1, 3, 5, 6, 8. The middle value is 5. The median is 5.", do=[B("1, 3, 5, 6, 8 → median 5", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Averages at work", steps=[
        dict(say="A shoe shop uses the mode. It needs to know which size sells the most, so that it can order more of that size.", do=[E("👟", 90, 160, 100), T("a shoe shop needs the **mode**", x=230, y=190)]),
        dict(say="News reports often give the median house price, not the mean. A few very expensive houses would pull the mean up.", do=[E("🏠", 90, 300, 100), T("house prices: the **median**", x=230, y=330)]),
        dict(say="And a mean does not have to be a real value. A country can have a mean of 2.4 people in each home, but no home has 2.4 people.", do=[E("👨‍👩‍👧", 90, 440, 100), T("a mean of **2.4** people in each home", x=230, y=470)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.6-k4", "One last question. Does a smaller range mean more consistent, or higher scores? Pause the video and answer.", "A smaller range means more consistent or higher scores?"),
        dict(say="More consistent. A small range means the values are close together. It does not tell you how high they are.", do=[B("more consistent", x=80, y=190, color=GREEN), T("values **close together**", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the mode is the most common value. The median is the middle value, in order. The mean is the total, divided by the number of values.", do=[T("• **Mode**: most common · **median**: middle · **mean**: total ÷ number", x=80, y=170)]),
        dict(say="The range is the largest minus the smallest. It shows the spread.", do=[T("• **Range** = largest − smallest", x=80, y=250)]),
        dict(say="Compare 2 sets of data with an average, and with the range.", do=[T("• Compare with an **average** and the **range**", x=80, y=330)]),
        dict(say="Choose the median when there are extreme values.", do=[T("• Extreme values? Use the **median**", x=80, y=410)]),
    ]),
]
