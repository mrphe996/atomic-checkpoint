# -*- coding: utf-8 -*-
"""Stage 8 · Unit 16 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG
from .s7_u04 import TBL, ROW
from .s7_u07 import F
from .s7_u11 import LG
from .s7_u16 import BARS, PIE, BL, OR

SLEEP = lambda gap=False, x=640, y=130, w=600, at=0: FIG(x, y, w, at, kind="barchart", labels=["5–6", "6–7", "7–8", "8–9", "9–10", "10–11"], values=[2, 5, 9, 8, 4, 2], ymax=10, step=2, ylabel="Frequency", xlabel="Time asleep, t (hours)", gap=gap, colours=[BL] * 6)
BATTERY = lambda at=0, **k: LG(dict(min=8, max=14, step=1, label="Time (hour)"), dict(min=0, max=100, step=20, label="Battery (%)"), [[8, 100], [9, 88], [10, 75], [11, 66], [12, 52], [13, 40], [14, 31]], at=at, **k)
STEM = lambda stems, right, key, x=700, y=140, w=480, at=0: FIG(x, y, w, at, kind="stemleaf", stems=stems, right=right, key=key)
REACT = lambda at=0, **k: STEM([1, 2, 3, 4], [[8, 9], [2, 4, 5, 6, 7, 8, 9], [0, 1, 3, 5, 7], [1]], "Key: 2 | 4 means 24", at=at, **k)

VIDEOS = {}

VIDEOS["16.1"] = [
    dict(kind="hook", title="A sleep survey", steps=[
        dict(say="A class records how long each student slept last night, to the nearest minute. The times go from 5 hours 40 minutes, up to 10 hours 10 minutes.",
             do=[E("😴", 90, 170, 100), T("times from **5 h 40 min** to **10 h 10 min**", x=230, y=200)]),
        dict(say="A bar for every possible time would be useless. Almost every bar would have a height of 1.", do=[T("a bar for every minute? **useless**", x=230, y=300)]),
        PAUSE("16.1-k1", "What is the best way to show the pattern? Pause the video and choose.", "Best idea?"),
    ]),
    dict(kind="hook", title="Group the data", steps=[
        dict(say="Group the times into classes, like 6 to 7 hours, and count how many are in each class.", do=[B("group the times into classes", x=80, y=200, color=GREEN), SLEEP(at=2)]),
    ]),
    dict(kind="recall", title="Discrete and continuous", steps=[
        dict(say="Remember: discrete data is counted, like the number of pets. Continuous data is measured, like a time or a mass.", do=[T("**discrete**: counted · **continuous**: measured", x=80, y=190)]),
        PAUSE("16.1-k2", "Your turn. Is mass discrete or continuous? Pause the video and choose.", "Mass is …"),
    ]),
    dict(kind="idea", title="Grouping data", steps=[
        dict(say="Mass is continuous, because it is measured. Put data into classes with equal class intervals.", do=[B("mass: continuous", x=80, y=170, color=GREEN), T("equal **class intervals**", x=80, y=270, at=4)]),
        dict(say="For discrete data, groups like 0 to 4, 5 to 9, and 10 to 14 work. For continuous data, use inequalities, so that every value fits exactly one class. 6 is less than or equal to t, which is less than 7.",
             do=[T("discrete: 0–4, 5–9, 10–14", x=80, y=350), MATH("continuous: 6 ≤ t < 7,  7 ≤ t < 8 …", x=80, y=430, at=6)]),
    ]),
    dict(kind="idea", title="Frequency diagrams", steps=[
        dict(say="For continuous data, draw a frequency diagram. The bars have no gaps, because the scale is continuous. Label both axes.",
             do=[SLEEP(), T("continuous → **no gaps**", x=80, y=180)]),
        dict(say="For grouped discrete data, draw a bar chart with gaps.", do=[T("discrete → bars **with gaps**", x=80, y=270)]),
        PAUSE("16.1-k3", "Your turn. What do the bars for continuous data have? Pause the video and choose.", "Bars for continuous data have …"),
    ]),
    dict(kind="method", title="How do I draw a frequency diagram?", steps=[
        dict(say="No gaps. Here is the method. Step 1: choose equal class intervals that cover all the data.", do=[T("1. **Equal** class intervals covering all the data", x=80, y=170)]),
        dict(say="Step 2: tally the data into a frequency table.", do=[T("2. **Tally** into a frequency table", x=80, y=260)]),
        dict(say="Step 3: draw the bars. Gaps for discrete data, no gaps for continuous data.", do=[T("3. Gaps for discrete; **no gaps** for continuous", x=80, y=350)]),
        dict(say="Step 4: label the axes, and give a title.", do=[T("4. **Label** the axes; title", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Modal class and total", steps=[
        dict(say="Look at the sleep diagram. The modal class is the one with the highest frequency, 9. That is 7 is less than or equal to t, which is less than 8.",
             do=[SLEEP(), MATH("modal class: 7 ≤ t < 8", x=80, y=190, color=GREEN)]),
        dict(say="The number of students is the total of the frequencies: 2 plus 5 plus 9 plus 8 plus 4 plus 2, which is 30.", do=[MATH("2 + 5 + 9 + 8 + 4 + 2 = 30", x=80, y=290)]),
        dict(say="The fraction who slept at least 9 hours is 4 plus 2, which is 6 out of 30. That is 1 fifth.", do=[MATH(f"{F(6, 30)} = {F(1, 5)}", x=80, y=390)]),
    ]),
    dict(kind="example", title="Choosing classes", steps=[
        dict(say="Masses go from 41 to 78 kilograms. Classes of width 10 could be: 40 to 50, 50 to 60, 60 to 70, and 70 to 80. They cover all the data, with equal widths.",
             do=[MATH("40 ≤ m < 50, 50 ≤ m < 60, 60 ≤ m < 70, 70 ≤ m < 80", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Lee uses classes 140 to 150, 150 to 160, and 160 to 170 centimetres for heights. Which line shows the problem?", do=LINES("Lee", "classes 140–150, 150–160, 160–170", ["a height of 150 cm goes in both 140–150 and 150–160"])),
        dict(say="The classes overlap. A height of exactly 150 fits two classes. Use inequalities instead.", do=[dict(a="cross", id="l1")]),
        dict(say="140 is less than or equal to h, which is less than 150. Then 150 to 160, and so on.", do=[B("140 ≤ h < 150, 150 ≤ h < 160 …", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="How much sleep?", steps=[
        dict(say="Health experts recommend that teenagers sleep about 8 to 10 hours a night. In our class, only 14 of the 30 students slept 8 hours or more.",
             do=[E("🛌", 90, 170, 100), T("teenagers: about **8–10 hours**", x=230, y=200), MATH("8 + 4 + 2 = 14 of 30", x=230, y=300, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.1-k4", "One last question. The frequencies are 4, 9 and 2. What is the frequency of the modal class? Pause the video and answer.", "Frequencies 4, 9, 2. Modal class frequency?"),
        dict(say="The modal class has the highest frequency, which is 9.", do=[B("9", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: use equal class intervals, with no overlaps.", do=[T("• Equal class intervals, no overlaps", x=80, y=170)]),
        dict(say="For continuous data, use inequalities, like 6 is less than or equal to t, which is less than 7.", do=[T("• Continuous: 6 ≤ t < 7", x=80, y=250)]),
        dict(say="Continuous data has no gaps between bars. Discrete data has gaps.", do=[T("• Continuous: no gaps · discrete: gaps", x=80, y=330)]),
        dict(say="The modal class has the highest frequency.", do=[T("• Modal class = highest frequency", x=80, y=410)]),
    ]),
]

VIDEOS["16.2"] = [
    dict(kind="hook", title="Phone battery", steps=[
        dict(say="Mia's phone records the battery level every hour from 8 am to 2 pm: 100, 88, 75, 66, 52, 40 and 31 percent.",
             do=[E("🔋", 90, 170, 100), T("**100, 88, 75, 66, 52, 40, 31 %**", x=230, y=200), BATTERY(x=640, y=270, w=560, at=4)]),
        PAUSE("16.2-k1", "Is the battery running down roughly steadily? Pause the video and choose.", "Is the fall roughly steady?"),
    ]),
    dict(kind="hook", title="Roughly steady", steps=[
        dict(say="Yes. It falls by about 11 to 13 percent every hour, so the points lie close to a straight line.", do=[BATTERY(x=640, y=150, w=560), B("about 11–13 % an hour", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="recall", title="Line graphs", steps=[
        dict(say="Remember: for a line graph, plot the points, then join them with straight lines. Time goes on the horizontal axis.", do=[T("plot, join with **straight lines** · time **across**", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Time series graphs", steps=[
        dict(say="A time series graph shows a quantity measured at regular time intervals, with the points joined by straight lines.",
             do=[BATTERY(x=640, y=150, w=560), T("measured at **regular** time intervals", x=80, y=180)]),
        dict(say="It shows the trend: the general direction of change. Up, down, or steady.", do=[T("the **trend**: up, down or steady", x=80, y=270)]),
        PAUSE("16.2-k2", "Your turn. What is the battery's trend? Pause the video and choose.", "The battery's trend is …"),
    ]),
    dict(kind="idea", title="Reading and predicting", steps=[
        dict(say="It is a downward trend. Points between the plotted times are only estimates. At 10:30, the battery was probably about 70 percent, halfway between 75 and 66.",
             do=[B("downward trend", x=80, y=170, color=GREEN), MATH("10:30 ≈ (75 + 66) ÷ 2 ≈ 70%", x=80, y=270, at=6)]),
        dict(say="Continuing the trend, the battery would reach 0 at about 4 or 5 pm. But predictions far into the future are less reliable.", do=[T("predict: about **0% around 4–5 pm**", x=80, y=360)]),
    ]),
    dict(kind="method", title="How do I draw and read one?", steps=[
        dict(say="Here is the method. Step 1: put time on the horizontal axis, with equal steps.", do=[T("1. **Time** across, equal steps", x=80, y=170)]),
        dict(say="Step 2: choose a vertical scale that fits the data.", do=[T("2. A vertical scale that fits", x=80, y=260)]),
        dict(say="Step 3: plot each point accurately, and join them with straight lines.", do=[T("3. Plot; join with **straight lines**", x=80, y=350)]),
        dict(say="Step 4: describe the trend, and any big changes.", do=[T("4. Describe the **trend**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="The biggest drop", steps=[
        dict(say="In which hour did the battery drop most? The drops are 12, 13, 9, 14, 12 and 9. The biggest is 14, from 11 am to 12 noon.",
             do=[TBL(["Hour", "8–9", "9–10", "10–11", "11–12", "12–1", "1–2"], [["Drop (%)", "12", "13", "9", "14", "12", "9"]], y=170), ROW(0, 2), B("11 am to 12 noon", x=80, y=330, color=GREEN, at=9)]),
        PAUSE("16.2-k3", "Your turn. How much did it drop from 1 pm to 2 pm? Pause and check the table.", "Drop from 1 pm to 2 pm (%)?"),
    ]),
    dict(kind="example", title="Check: 1 pm to 2 pm", steps=[
        dict(say="From 40 percent to 31 percent is a drop of 9 percent.", do=[MATH("40 − 31 = 9", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="A misleading scale", steps=[
        dict(say="Be careful with scales. If the vertical axis starts at 60 percent instead of 0, small changes look huge. Always check where the axis starts.",
             do=[T("an axis starting at **60%** exaggerates changes", x=80, y=200, color=RED)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Sam draws the battery graph. Which line is wrong?", do=LINES("Sam", "the battery graph", ["battery % on the horizontal axis, time on the vertical"])),
        dict(say="Line 1 is wrong. In a time series graph, time always goes on the horizontal axis.", do=[dict(a="cross", id="l1")]),
        dict(say="Time across, battery percentage up.", do=[B("time → horizontal axis", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Climate records", steps=[
        dict(say="Scientists use time series graphs to show how the world's average temperature has changed since the 1800s. The graph goes up and down from year to year, but the overall trend is upward.",
             do=[E("🌍", 90, 170, 100), T("ups and downs, but an **upward trend**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.2-k4", "One last question. Is a prediction 3 days ahead more reliable, or less reliable? Pause the video and choose.", "A prediction 3 days ahead is …"),
        dict(say="Less reliable. The further ahead you predict, the more things can change.", do=[B("less reliable", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: regular time intervals go on the horizontal axis.", do=[T("• Regular time intervals across", x=80, y=170)]),
        dict(say="Join the points with straight lines.", do=[T("• Join with straight lines", x=80, y=250)]),
        dict(say="Describe the trend.", do=[T("• Describe the trend", x=80, y=330)]),
        dict(say="Values in between, and in the future, are only estimates.", do=[T("• In-between and future values are estimates", x=80, y=410)]),
    ]),
]

VIDEOS["16.3"] = [
    dict(kind="hook", title="Reaction times", steps=[
        dict(say="Fifteen students test their reaction times, in hundredths of a second. The results are 24, 31, 19, 27, 35, 22, 28, 41, 26, 33, 29, 18, 37, 25 and 30.",
             do=[E("⚡", 90, 170, 100), T("24, 31, 19, 27, 35, 22, 28, 41, 26, 33, 29, 18, 37, 25, 30", x=230, y=200)]),
        dict(say="How could you show every value in order, and still see the shape of the data?", do=[T("every value, **in order**, and the **shape**?", x=230, y=300)]),
        PAUSE("16.3-k1", "Which diagram keeps all the values in order? Pause the video and choose.", "A diagram that keeps all values in order?"),
    ]),
    dict(kind="hook", title="A stem-and-leaf diagram", steps=[
        dict(say="A stem-and-leaf diagram. The tens digit is the stem, and the units digit is the leaf.", do=[REACT(), B("stem-and-leaf diagram", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="recall", title="Median and range", steps=[
        dict(say="Remember: the median is the middle value, when the values are in order. The range is the largest minus the smallest. 41 minus 18 is 23.", do=[T("median: the **middle** value · range: largest − smallest", x=80, y=180), MATH("41 − 18 = 23", x=80, y=280, at=6)]),
    ]),
    dict(kind="idea", title="Stem-and-leaf diagrams", steps=[
        dict(say="Write the stems in a column. Write each leaf next to its stem, in order, lined up. Always give a key, like: 2, leaf 4, means 24.",
             do=[REACT(), T("leaves **in order**, lined up, with a **key**", x=80, y=180)]),
        dict(say="It keeps every value, and it shows the shape like a bar chart on its side.", do=[T("every value + the **shape**", x=80, y=270)]),
        PAUSE("16.3-k2", "Your turn. There are 15 values. What is the median? Pause the video and try it.", "Median of the reaction times?"),
    ]),
    dict(kind="idea", title="Check: the median", steps=[
        dict(say="With 15 values, the median is the 8th. Count along: 18, 19, then 22, 24, 25, 26, 27, 28. The median is 28.", do=[REACT(), B("median = 28", x=80, y=200, color=GREEN, at=8)]),
        dict(say="The mean is the sum, 425, divided by 15, which is about 28.3.", do=[MATH("425 ÷ 15 ≈ 28.3", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I draw and use one?", steps=[
        dict(say="Here is the method. Step 1: choose the stems, often the tens, and write them in a column.", do=[T("1. **Stems** in a column", x=80, y=170)]),
        dict(say="Step 2: write each leaf next to its stem. Then redraw it with the leaves in order.", do=[T("2. Leaves, then put them **in order**", x=80, y=260)]),
        dict(say="Step 3: line up the leaves, and add a key.", do=[T("3. Line up; add a **key**", x=80, y=350)]),
        dict(say="Step 4: read off the median, mode and range.", do=[T("4. Read the median, mode, range", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Drawing one", steps=[
        dict(say="Draw a diagram for 52, 47, 61, 55, 49, 58, 63 and 50. The stems are 4, 5 and 6.", do=[STEM([4, 5, 6], [[7, 9], [0, 2, 5, 8], [1, 3]], "Key: 5 | 2 means 52")]),
        dict(say="There are 8 values, so the median is halfway between the 4th and the 5th: 52 and 55.", do=[MATH("4th 52, 5th 55", x=80, y=200)]),
        PAUSE("16.3-k3", "Your turn. What is the median of these 8 values? Pause and work it out.", "Median of 47, 49, 50, 52, 55, 58, 61, 63?"),
    ]),
    dict(kind="example", title="Check: 53.5", steps=[
        dict(say="52 plus 55 is 107. Halve it: 53.5.", do=[MATH("(52 + 55) ÷ 2 = 53.5", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Decimals", steps=[
        dict(say="A key can show decimals. If 3, leaf 4, means 3.4 kilograms, then 3 with leaves 1, 4, 4, 8 means 3.1, 3.4, 3.4 and 3.8. The mode is 3.4, because it appears twice.",
             do=[STEM([3], [[1, 4, 4, 8]], "Key: 3 | 4 means 3.4 kg"), MATH("3.1, 3.4, 3.4, 3.8", x=80, y=200), B("mode = 3.4 kg", x=80, y=300, color=GREEN, at=10)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Kai draws a stem-and-leaf diagram for 34, 31 and 38. Which line is wrong?", do=LINES("Kai", "34, 31, 38", ["3 | 4 1 8"])),
        dict(say="Line 1 is wrong. The leaves are not in order, and there is no key.", do=[dict(a="cross", id="l1")]),
        dict(say="It should be 3, leaves 1, 4, 8, with a key: 3, leaf 1, means 31.", do=[B("3 | 1 4 8 · key: 3 | 1 = 31", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Timetables", steps=[
        dict(say="Some railway timetables are stem-and-leaf diagrams! The hour is the stem, and the minutes of each departure are the leaves.",
             do=[E("🚉", 90, 170, 100), T("hour = **stem** · minutes = **leaves**", x=230, y=200), STEM([8, 9], [[5, 20, 35, 50], [5, 35]], "Key: 8 | 20 means 8:20", at=3)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.3-k4", "One last question. What does a stem-and-leaf diagram always need? Pause the video and choose.", "A stem-and-leaf diagram needs …"),
        dict(say="It always needs a key, so that readers know what the numbers mean.", do=[B("a key", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the stem is the leading digit, and the leaf is the last digit.", do=[T("• Stem = leading digit(s) · leaf = last digit", x=80, y=170)]),
        dict(say="Leaves go in order, and lined up.", do=[T("• Leaves in order, lined up", x=80, y=250)]),
        dict(say="Always give a key.", do=[T("• Always give a **key**", x=80, y=330)]),
        dict(say="Find the median, mode and range straight from the diagram.", do=[T("• Read the median, mode and range", x=80, y=410)]),
    ]),
]

VIDEOS["16.4"] = [
    dict(kind="hook", title="Two clubs", steps=[
        dict(say="Two clubs show how their members travel there, in pie charts. In both charts, the cycle sector is 90 degrees. Club A has 40 members, and club B has 200.",
             do=[E("🚲", 90, 170, 100), T("cycle sector **90°** in both · A: **40** members · B: **200**", x=230, y=200), PIE(["Cycle", "Walk", "Bus", "Car"], [90, 120, 80, 70], at=3, y=270, w=420)]),
        PAUSE("16.4-k1", "Do the same number of people cycle to each club? Pause the video and choose.", "Same number cycle?"),
    ]),
    dict(kind="hook", title="Proportions, not amounts", steps=[
        dict(say="No. 90 degrees is a quarter of the circle, so a quarter of each club cycles. A quarter of 40 is 10. A quarter of 200 is 50.",
             do=[MATH(f"90° = {F(1, 4)}", x=80, y=180), MATH(f"A: {F(1, 4)} × 40 = 10", x=80, y=270, at=5), MATH(f"B: {F(1, 4)} × 200 = 50", x=80, y=350, at=8), B("10 vs 50", x=80, y=440, color=GREEN, at=10)]),
    ]),
    dict(kind="recall", title="Sector angles", steps=[
        dict(say="Remember: a sector's angle is its fraction of 360 degrees. 90 degrees is a quarter. 180 degrees is a half.", do=[MATH("angle = fraction × 360°", x=80, y=190), MATH(f"90° = {F(1, 4)} · 180° = {F(1, 2)}", x=80, y=290)]),
    ]),
    dict(kind="idea", title="Proportions", steps=[
        dict(say="A pie chart shows proportions, which are fractions of the whole. It does not show actual numbers. Equal sectors can mean very different numbers of people.",
             do=[B("pie charts show **proportions**", x=80, y=170, color=BLUE)]),
        dict(say="To find a number, use: the angle, divided by 360, times the total.", do=[B("number = angle ÷ 360 × total", x=80, y=280, color=BLUE)]),
        PAUSE("16.4-k2", "Your turn. How many members of club B cycle? Pause the video and check.", "Club B: number who cycle?"),
    ]),
    dict(kind="idea", title="Comparing pie charts", steps=[
        dict(say="90 divided by 360, times 200, is 50. To compare proportions, compare the angles. To compare numbers, work out each amount.",
             do=[MATH("90 ÷ 360 × 200 = 50", x=80, y=180, color=GREEN), T("proportions → compare **angles** · numbers → **calculate**", x=80, y=290, at=5)]),
    ]),
    dict(kind="method", title="How do I compare pie charts?", steps=[
        dict(say="Here is the method. Step 1: decide. Is the question about a proportion, or an actual number?", do=[T("1. **Proportion** or **number**?", x=80, y=170)]),
        dict(say="Step 2: for proportions, compare the angles, or the fractions.", do=[T("2. Proportions: compare the **angles**", x=80, y=260)]),
        dict(say="Step 3: for numbers, work out the angle divided by 360, times the total, for each chart.", do=[T("3. Numbers: angle ÷ 360 × **total**", x=80, y=350)]),
        dict(say="Step 4: explain your conclusion, using both charts.", do=[T("4. **Explain**, using both charts", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Proportion or number?", steps=[
        dict(say="In school P, the Science sector is 108 degrees, out of 30 students. In school Q, it is 96 degrees, out of 60 students. Which has a greater proportion choosing Science? 108 is more than 96, so school P.",
             do=[T("P: **108°** of 30 · Q: **96°** of 60", x=80, y=170), MATH("proportion: 108° > 96° → P", x=80, y=270, at=9)]),
        dict(say="But which has more students choosing Science? P: 108 over 360, times 30, is 9. Q: 96 over 360, times 60, is 16. School Q.",
             do=[MATH("P: 9 · Q: 16 → Q", x=80, y=370, color=GREEN)]),
        PAUSE("16.4-k3", "Your turn. How many is a 120 degree sector of 45? Pause and work it out.", "120° of 45?"),
    ]),
    dict(kind="example", title="Check: 120° of 45", steps=[
        dict(say="120 degrees is a third of 360. A third of 45 is 15.", do=[MATH(f"120° = {F(1, 3)} → {F(1, 3)} × 45 = 15", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Find the total", steps=[
        dict(say="A sector of 60 degrees represents 15 people. What is the total? 60 degrees is a sixth of the circle. So the total is 15 times 6, which is 90 people.",
             do=[MATH(f"60° = {F(1, 6)}", x=80, y=180), B("15 × 6 = 90", x=80, y=290, color=GREEN, at=7)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="In pie A, pasta is 180 degrees, out of 20 people. In pie B, pasta is 120 degrees, out of 90 people. Which line is wrong?", do=LINES("Ed", "A: 180° of 20 · B: 120° of 90", ["A has the bigger angle, so more people like pasta in A"])),
        dict(say="Line 1 is wrong. A bigger angle means a bigger proportion, not more people. A: half of 20 is 10. B: a third of 90 is 30.", do=[dict(a="cross", id="l1")]),
        dict(say="More people like pasta in B.", do=[B("A: 10 people · B: 30 people", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="News charts", steps=[
        dict(say="News reports often show pie charts of how a country spends its money. Before comparing two countries, check the totals. A small slice of a big budget can be more money than a big slice of a small one.",
             do=[E("📰", 90, 170, 100), T("check the **totals** before comparing", x=230, y=200, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.4-k4", "One last question. What is a 72 degree sector as a percentage? Pause the video and answer.", "72° as a percentage?"),
        dict(say="72 divided by 360 is 0.2, which is 20 percent.", do=[MATH("72 ÷ 360 = 0.2", x=80, y=190), B("20%", x=80, y=290, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: pie charts show proportions.", do=[T("• Pie charts show **proportions**", x=80, y=170)]),
        dict(say="The number is the angle, divided by 360, times the total.", do=[T("• Number = angle ÷ 360 × total", x=80, y=250)]),
        dict(say="Compare proportions by angle. Compare amounts by calculating.", do=[T("• Proportions: angles · amounts: calculate", x=80, y=330)]),
        dict(say="Check the totals before you decide.", do=[T("• Check the totals", x=80, y=410)]),
    ]),
]

VIDEOS["16.5"] = [
    dict(kind="hook", title="Choosing a chart", steps=[
        dict(say="A sports club has four sets of data: members' favourite sports, monthly attendance for a year, the times of a 400 metre race, and boys and girls in each age group.",
             do=[E("🏅", 90, 170, 100), T("favourite sports · **monthly attendance** · race times · boys vs girls", x=230, y=200)]),
        dict(say="Which kind of chart suits each one? Start with the monthly attendance.", do=[T("which chart for each?", x=230, y=300)]),
        PAUSE("16.5-k1", "Which chart is best for attendance each month? Pause the video and choose.", "Attendance per month?"),
    ]),
    dict(kind="hook", title="A time series graph", steps=[
        dict(say="A time series graph, because the attendance is measured every month, and we want to see how it changes over time.", do=[B("time series graph", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="recall", title="Charts you know", steps=[
        dict(say="Remember the charts you know: bar charts, pie charts, line graphs, frequency diagrams, stem-and-leaf diagrams, and scatter graphs.", do=[T("bar · pie · line · frequency diagram · stem-and-leaf · scatter", x=80, y=200)]),
    ]),
    dict(kind="idea", title="Matching charts to data", steps=[
        dict(say="Choose the chart for the question you want to answer.",
             do=[TBL(["Chart", "Use it when …"], [["Venn / Carroll diagram", "sorting into groups by features"], ["bar or dual bar chart", "comparing categories or groups"], ["pie chart", "showing proportions of a whole"], ["time series graph", "showing change over time"], ["frequency diagram", "grouped continuous data"], ["scatter graph", "a relationship between two variables"]], y=150), ROW(0, 0.5), ROW(1, 1.5), ROW(2, 2.5), ROW(3, 3.5), ROW(4, 4.5), ROW(5, 5.5)]),
        PAUSE("16.5-k2", "Your turn. Which diagram sorts shapes by has a right angle, and is a quadrilateral? Pause the video and choose.", "Sorting shapes by 'has right angle' and 'is quadrilateral'?"),
    ]),
    dict(kind="idea", title="Check: sorting", steps=[
        dict(say="A Carroll diagram. It sorts items into a grid by two features: yes or no for each.", do=[B("Carroll diagram", x=80, y=190, color=GREEN)]),
        dict(say="To justify a choice means to give a reason. For example: a time series graph, because the data is attendance measured each month, and I want to see the trend.",
             do=[T("**justify** = give a **reason**", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I choose a chart?", steps=[
        dict(say="Here is the method. Step 1: identify the type of data: categorical, discrete, continuous, over time, or in pairs.", do=[T("1. What **type** of data?", x=80, y=170)]),
        dict(say="Step 2: decide what you want to show: a comparison, a proportion, a trend, or a relationship.", do=[T("2. What do you want to **show**?", x=80, y=260)]),
        dict(say="Step 3: pick the chart that shows that most clearly.", do=[T("3. Pick the **clearest** chart", x=80, y=350)]),
        dict(say="Step 4: justify your choice with a reason.", do=[T("4. **Justify** your choice", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Three choices", steps=[
        dict(say="Favourite sports, as fractions of all the members: a pie chart, because it shows proportions of a whole.", do=[T("favourite sports → **pie chart**", x=80, y=180)]),
        dict(say="40 race times, measured to a tenth of a second: a frequency diagram, because the data is continuous, with many values.", do=[T("race times → **frequency diagram**", x=80, y=270)]),
        dict(say="Boys and girls in each age group: a dual bar chart, to compare the two groups side by side.", do=[T("boys vs girls → **dual bar chart**", x=80, y=360)]),
        PAUSE("16.5-k3", "Your turn. Which chart shows the relationship between revision time and test score? Pause and choose.", "Relationship between revision time and score?"),
    ]),
    dict(kind="example", title="Check: a relationship", steps=[
        dict(say="A scatter graph, because there are two variables for each student, and we want to see if they are related.", do=[B("scatter graph", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Amy wants to show monthly attendance through the year. Which line is wrong?", do=LINES("Amy", "monthly attendance through the year", ["… use a pie chart with 12 sectors"])),
        dict(say="Line 1 is wrong. A pie chart hides the order of the months. A time series graph shows the trend.", do=[dict(a="cross", id="l1")]),
        dict(say="Use a time series graph.", do=[B("time series graph", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Data journalists", steps=[
        dict(say="Data journalists choose charts every day. The same numbers can tell a clear story in one chart, and be confusing in another. Choosing the right chart is part of telling the truth with data.",
             do=[E("📊", 90, 170, 100), T("the right chart tells the story **clearly**", x=230, y=200, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.5-k4", "One last question. What does justify mean? Pause the video and choose.", "'Justify' means …"),
        dict(say="Justify means give a reason.", do=[B("give a reason", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: match the chart to the type of data, and to its purpose.", do=[T("• Match the chart to the data and the purpose", x=80, y=170)]),
        dict(say="Proportion: pie chart. Trend: time series. Relationship: scatter graph.", do=[T("• Proportion → pie · trend → time series · relationship → scatter", x=80, y=250)]),
        dict(say="Comparison: a bar or dual bar chart. Grouped continuous data: a frequency diagram.", do=[T("• Comparison → bar · grouped continuous → frequency diagram", x=80, y=330)]),
        dict(say="Always justify your choice.", do=[T("• Always **justify** your choice", x=80, y=410)]),
    ]),
]

VIDEOS["16.6"] = [
    dict(kind="hook", title="Choosing a bowler", steps=[
        dict(say="A cricket coach must pick one bowler. These are the runs each bowler gave away per over in recent games. Asha: 4, 5, 4, 6, 5. Ben: 1, 9, 2, 8, 5.",
             do=[E("🏏", 90, 170, 100), T("Asha: **4, 5, 4, 6, 5**", x=230, y=190), T("Ben: **1, 9, 2, 8, 5**", x=230, y=270)]),
        PAUSE("16.6-k1", "Which bowler is the more reliable choice? Pause the video and choose.", "A reliable choice?"),
    ]),
    dict(kind="hook", title="Consistent Asha", steps=[
        dict(say="Their averages are almost the same. But Asha's runs are always between 4 and 6, while Ben's go from 1 to 9. Asha is more consistent, so she is the more reliable choice.",
             do=[TBL(["", "Mean", "Median", "Lowest", "Highest"], [["Asha", "4.8", "5", "4", "6"], ["Ben", "5", "5", "1", "9"]], y=170), ROW(0, 3), ROW(1, 4), B("Asha (more consistent)", x=80, y=360, color=GREEN, at=9)]),
    ]),
    dict(kind="recall", title="Averages and range", steps=[
        dict(say="Remember: the mean is the sum divided by the count. The median is the middle value. The mode is the most common. The range is the largest minus the smallest.",
             do=[T("mean · median · mode · **range**", x=80, y=190)]),
        PAUSE("16.6-k2", "Your turn. What is the range of Asha's runs? Pause the video and try it.", "Range of Asha's runs?"),
    ]),
    dict(kind="idea", title="Comparing two sets", steps=[
        dict(say="6 minus 4 is 2. To compare two sets of data, compare an average, which shows how big the values are. And compare the range, which shows how spread out they are.",
             do=[MATH("6 − 4 = 2", x=80, y=170, color=GREEN), T("**average**: how big · **range**: how spread out", x=80, y=270, at=4)]),
        dict(say="A smaller range means more consistent.", do=[B("smaller range = more consistent", x=80, y=370, color=BLUE)]),
    ]),
    dict(kind="idea", title="Which average?", steps=[
        dict(say="The mean uses every value, but it is pulled by extreme values, called outliers. The median is not affected by extremes. The mode suits categories, or the most popular size.",
             do=[T("**mean**: uses every value, pulled by outliers", x=80, y=170), T("**median**: not affected by extremes", x=80, y=250, at=5), T("**mode**: categories, most popular", x=80, y=330, at=8)]),
        PAUSE("16.6-k3", "Your turn. With an outlier, which average should you use? Pause the video and choose.", "With an outlier, use …"),
    ]),
    dict(kind="method", title="How do I compare data sets?", steps=[
        dict(say="The median. Here is the method. Step 1: work out a suitable average for each set.", do=[T("1. A suitable **average** for each", x=80, y=170)]),
        dict(say="Step 2: work out the range for each set.", do=[T("2. The **range** for each", x=80, y=260)]),
        dict(say="Step 3: compare. Which average is higher? Which set is more consistent?", do=[T("3. Higher average? More **consistent**?", x=80, y=350)]),
        dict(say="Step 4: write a conclusion in context, using the numbers.", do=[T("4. Conclude **in context**, with numbers", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="An outlier", steps=[
        dict(say="Five salaries, in thousands of dollars, are 28, 30, 31, 33 and 150. The mean is 54.4, pulled up by the 150. The median is 31, which is more typical. Use the median.",
             do=[T("28, 30, 31, 33, **150**", x=80, y=170), MATH("mean = 54.4 · median = 31", x=80, y=270, at=6), B("use the median", x=80, y=370, color=GREEN, at=10)]),
    ]),
    dict(kind="example", title="Comparing classes", steps=[
        dict(say="Class X has a mean of 62 and a range of 30. Class Y has a mean of 58 and a range of 12. Class X did better on average. Class Y's marks were more consistent.",
             do=[T("X: mean **62**, range **30** · Y: mean **58**, range **12**", x=80, y=180), T("X higher on average · Y more **consistent**", x=80, y=290, color=GREEN, at=8)]),
    ]),
    dict(kind="example", title="The mode", steps=[
        dict(say="A shop sells shoes in sizes 5, 6, 6, 7, 6, 8 and 9. Which average helps the shop order stock? The mode, 6, because it is the most popular size.", do=[B("mode = size 6", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Team A has a range of 3. Team B has a range of 10. Which line is wrong?", do=LINES("Lia", "Team A range 3, Team B range 10", ["so Team B scores more"])),
        dict(say="Line 1 is wrong. The range measures spread, not size. Team B is less consistent. Use an average to say who scores more.", do=[dict(a="cross", id="l1")]),
        dict(say="Team B's scores are more spread out.", do=[B("range = spread, not size", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="House prices", steps=[
        dict(say="News reports usually give the median house price, not the mean. A few very expensive houses would pull the mean up, and make prices look higher than most people pay.",
             do=[E("🏡", 90, 170, 100), T("reports use the **median** price", x=230, y=200, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("16.6-k4", "One last question. What does the range tell you about? Pause the video and choose.", "Range tells you about …"),
        dict(say="The range tells you about the spread of the data.", do=[B("spread", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: compare an average, and the range.", do=[T("• Compare an **average** and the **range**", x=80, y=170)]),
        dict(say="A smaller range means more consistent.", do=[T("• Smaller range = more consistent", x=80, y=250)]),
        dict(say="The median resists outliers. The mode suits categories.", do=[T("• Median resists outliers · mode for categories", x=80, y=330)]),
        dict(say="Write your conclusion in context, with numbers.", do=[T("• Conclude in context, with numbers", x=80, y=410)]),
    ]),
]
