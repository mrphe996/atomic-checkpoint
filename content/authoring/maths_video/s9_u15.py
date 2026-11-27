# -*- coding: utf-8 -*-
"""Stage 9 · Unit 15 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG
from .s7_u04 import TBL, ROW

VIDEOS = {}

GRAPH = lambda xa, ya, series, x=620, y=120, w=640, at=0: dict(a="fig", fig=dict(kind="linegraph", x=xa, y=ya, series=series), x=x, y=y, w=w, at=at)
POLYS = lambda at=0, both=True, **k: GRAPH(dict(min=0, max=40, step=5, label="Time t (minutes)"), dict(min=0, max=14, step=2, label="Frequency"),
                                           [dict(pts=[[5, 4], [15, 12], [25, 9], [35, 3]])] + ([dict(pts=[[5, 9], [15, 11], [25, 6], [35, 2]], dash=True)] if both else []), at=at, **k)
SCAT = [[14, 10], [16, 18], [18, 22], [20, 30], [22, 41], [24, 50], [27, 68], [29, 80], [31, 86], [34, 104]]
ICE = lambda fit=False, at=0, **k: GRAPH(dict(min=10, max=36, step=2, label="Temperature (°C)"), dict(min=0, max=120, step=20, label="Ice creams sold"),
                                         [dict(pts=SCAT, line=False)] + ([dict(pts=[[16, 12], [34, 106]], c="#E2483D")] if fit else []), at=at, **k)
TEAMS = lambda at=0, **k: FIG(k.get("x", 620), k.get("y", 120), k.get("w", 640), at, kind="stemleaf", stems=[3, 4, 5, 6],
                              left=[[2, 6, 9], [0, 1, 2, 4, 7], [3, 5, 8], [0]], right=[[4, 8], [1, 3, 5, 6, 9], [0, 2, 7], [1, 4]],
                              titles=["Owls", "Hawks"], key="Key: 4 | 1 = 41 for the Hawks · 2 | 3 = 32 for the Owls")

VIDEOS["15.1"] = [
    dict(kind="hook", title="Journeys to school", steps=[
        dict(say="Two classes record how many minutes their journey to school takes. Two bar charts side by side are hard to compare.",
             do=[E("🚌", 90, 170, 100), T("two classes · journey times · hard to **compare**", x=230, y=200)]),
        PAUSE("15.1-k1", "What is a clearer way: two frequency polygons on one graph, or two pie charts far apart? Pause the video and choose.", "A clearer way?"),
    ]),
    dict(kind="hook", title="Frequency polygons", steps=[
        dict(say="Two frequency polygons on one graph. You can compare them at a glance.", do=[B("two frequency polygons, one graph", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Grouped data", steps=[
        dict(say="Remember: the midpoint of the class from 10 up to 20 is 15.", do=[MATH("10 ≤ t < 20 → midpoint 15", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Frequency polygons", steps=[
        dict(say="A frequency polygon plots each class's frequency, then joins the points with straight lines.",
             do=[TBL(["Time t (min)", "0–10", "10–20", "20–30", "30–40"], [["9A", "4", "12", "9", "3"], ["9B", "9", "11", "6", "2"]], y=170), ROW(0, 1), ROW(1, 2)]),
        PAUSE("15.1-k2", "Your turn. Are the points plotted at the midpoints, or at the lower boundaries? Pause the video and choose.", "Points are plotted at …"),
    ]),
    dict(kind="idea", title="Check: midpoints", steps=[
        dict(say="At the midpoints: 5, 15, 25 and 35. Class 9A is the solid line. Class 9B is dashed.", do=[B("midpoints", x=80, y=190, color=GREEN), POLYS()]),
        dict(say="9B's polygon is higher on the left. So 9B's journeys are generally shorter. Do not join the ends down to the axis.", do=[T("9B higher on the **left** → shorter", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I draw one?", steps=[
        dict(say="Here is the method. Step 1: find each class midpoint.", do=[T("1. Class **midpoints**", x=80, y=170)]),
        dict(say="Step 2: plot each frequency at its midpoint.", do=[T("2. Plot (midpoint, **frequency**)", x=80, y=260)]),
        dict(say="Step 3: join the points with straight lines.", do=[T("3. Join with **straight lines**", x=80, y=350)]),
        dict(say="Step 4: for two groups, use the same axes, and a key.", do=[T("4. Same axes; a **key**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Reading back", steps=[
        dict(say="How many pupils are in 9A? Add the frequencies: 4 plus 12 plus 9 plus 3 is 28.", do=[POLYS(), MATH("4 + 12 + 9 + 3 = 28", x=80, y=180)]),
        dict(say="Who has more pupils taking 30 minutes or more? 9A has 3, and 9B has 2. So 9A.", do=[MATH("30+ min: 9A 3, 9B 2", x=80, y=280)]),
        PAUSE("15.1-k3", "Your turn. How many pupils are in 9B? Pause and work it out.", "Pupils in 9B?"),
    ]),
    dict(kind="example", title="Check: 28", steps=[
        dict(say="9 plus 11 plus 6 plus 2 is also 28.", do=[B("9 + 11 + 6 + 2 = 28", x=80, y=190, color=GREEN)]),
        dict(say="For discrete data, like goals in a match grouped 0 to 2, 3 to 5 and 6 to 8, plot at 1, 4 and 7.", do=[MATH("0–2 → 1 · 3–5 → 4 · 6–8 → 7", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Rob plots the class 10 up to 20, frequency 12. Which line is wrong?", do=LINES("Rob", "class 10 ≤ t < 20, frequency 12", ["plot (10, 12)"])),
        dict(say="Line 1 is wrong. He used the class boundary.", do=[dict(a="cross", id="l1")]),
        dict(say="Plot at the midpoint: 15, 12.", do=[B("(15, 12)", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Health services", steps=[
        dict(say="Health services compare the ages of patients in two years, or two towns, with frequency polygons on one graph.", do=[E("🏥", 90, 170, 100), T("compare two **distributions**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.1-k4", "One last question. Which class has shorter journeys overall: 9B, or 9A? Pause the video and choose.", "Shorter journeys overall?"),
        dict(say="9B. Its polygon is higher on the left, where the times are short.", do=[B("9B", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: plot the frequency at the class midpoint.", do=[T("• Plot at midpoints", x=80, y=170)]),
        dict(say="Join with straight lines.", do=[T("• Straight lines", x=80, y=250)]),
        dict(say="Great for comparing two groups.", do=[T("• Compare two groups", x=80, y=330)]),
        dict(say="Use the same axes, and a key.", do=[T("• Same axes, a key", x=80, y=410)]),
    ]),
]

VIDEOS["15.2"] = [
    dict(kind="hook", title="Ice creams", steps=[
        dict(say="A beach kiosk records the temperature at noon, and the number of ice creams sold, on 10 days. Do hotter days mean more sales?",
             do=[E("🍦", 90, 170, 100), T("temperature · ice creams sold · **10 days**", x=230, y=200)]),
        PAUSE("15.2-k1", "Which graph is best: a scatter graph, or a pie chart? Pause the video and choose.", "Best graph?"),
    ]),
    dict(kind="hook", title="Scatter graph", steps=[
        dict(say="A scatter graph. It plots one point for each day: the temperature across, and the sales up.", do=[B("a scatter graph", x=80, y=190, color=GREEN), ICE()]),
    ]),
    dict(kind="recall", title="Plotting points", steps=[
        dict(say="Remember: plot each pair, X across and Y up, on axes with sensible scales.", do=[T("(x, y): x **across**, y **up**", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Correlation", steps=[
        dict(say="The pattern of the points shows correlation. Positive: as one goes up, so does the other. Negative: as one goes up, the other goes down. None: no clear pattern.",
             do=[TBL(["Correlation", "Pattern"], [["positive", "both go up together"], ["negative", "one up, the other down"], ["none", "no clear pattern"]], y=170), ROW(0, 3), ROW(1, 6), ROW(2, 10)]),
        PAUSE("15.2-k2", "Your turn. Do temperature and sales show positive correlation, or negative correlation? Pause the video and choose.", "Temperature and sales show …"),
    ]),
    dict(kind="idea", title="Check: positive", steps=[
        dict(say="Positive correlation. Hotter days have higher sales.", do=[B("positive", x=80, y=190, color=GREEN), ICE()]),
        dict(say="Draw a line of best fit: a straight line through the middle of the points, with about the same number on each side. It does not have to go through the origin. This one goes through 16, 12 and 34, 106.",
             do=[ICE(fit=True), T("line of best fit: through the **middle**", x=80, y=300)]),
        PAUSE("15.2-k3", "Your turn. Use the line to estimate the sales at 26 degrees. Pause and work it out.", "Estimate at 26 °C?"),
    ]),
    dict(kind="idea", title="Check: about 64", steps=[
        dict(say="Go up from 26 to the line, then across. About 64 ice creams.", do=[B("about 64", x=80, y=190, color=GREEN), ICE(fit=True)]),
        dict(say="Only estimate inside the range of the data. At 45 degrees, the estimate would not be reliable.", do=[T("estimate **inside** the data range", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I use a scatter graph?", steps=[
        dict(say="Here is the method. Step 1: plot the points.", do=[T("1. **Plot** the points", x=80, y=170)]),
        dict(say="Step 2: describe the correlation: positive, negative or none, strong or weak.", do=[T("2. Describe the **correlation**", x=80, y=260)]),
        dict(say="Step 3: draw a line of best fit through the middle.", do=[T("3. **Line of best fit**", x=80, y=350)]),
        dict(say="Step 4: estimate inside the data range only.", do=[T("4. Estimate **inside** the range", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="Points rise steeply from left to right, close to a line: strong positive correlation.", do=[MATH("close to a line, rising → strong positive", x=80, y=180)]),
        dict(say="One hot day, only 20 ice creams were sold, because the kiosk shut early. That point is an outlier. Ignore it when you draw the line.", do=[T("an **outlier** – ignore it for the line", x=80, y=280)]),
        dict(say="Ice cream sales and sunburn are positively correlated. But ice cream does not cause sunburn. Hot sunny weather causes both.", do=[T("correlation is **not** cause", x=80, y=380, color=RED)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Lena draws a line of best fit for the ice cream data. Which line is wrong?", do=LINES("Lena", "line of best fit", ["start the line at (0, 0)"])),
        dict(say="Line 1 is wrong. A line of best fit follows the points. It does not have to go through the origin.", do=[dict(a="cross", id="l1")]),
        dict(say="Draw it through the middle of the points.", do=[B("through the middle of the points", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Business", steps=[
        dict(say="Businesses plot advertising spending against sales, to see whether their adverts seem to work.", do=[E("📈", 90, 170, 100), T("adverts vs sales", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.2-k4", "One last question. Does correlation prove that one thing causes the other? Pause the video and choose: no, or yes.", "Correlation proves cause?"),
        dict(say="No. Correlation shows a link, not a cause.", do=[B("No", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: correlation can be positive, negative, or none.", do=[T("• Positive, negative, none", x=80, y=170)]),
        dict(say="Draw the line of best fit through the middle of the points.", do=[T("• Line of best fit through the middle", x=80, y=250)]),
        dict(say="Estimate inside the data range only.", do=[T("• Estimate inside the range", x=80, y=330)]),
        dict(say="Correlation is not causation.", do=[T("• Correlation ≠ causation", x=80, y=410)]),
    ]),
]

VIDEOS["15.3"] = [
    dict(kind="hook", title="Two teams", steps=[
        dict(say="A basketball coach records the points scored by two teams in 12 matches each: the Hawks and the Owls. She wants one diagram that shows both, in order.",
             do=[E("🏀", 90, 170, 100), T("Hawks and Owls · **12** matches each", x=230, y=200)]),
        PAUSE("15.3-k1", "Which diagram can show two sets of data: a back-to-back stem-and-leaf diagram, or a pie chart? Pause the video and choose.", "One diagram for two sets?"),
    ]),
    dict(kind="hook", title="Back-to-back", steps=[
        dict(say="A back-to-back stem-and-leaf diagram.", do=[B("back-to-back stem-and-leaf", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Stem-and-leaf", steps=[
        dict(say="Remember: in a stem-and-leaf diagram, the stems are the tens and the leaves are the units, in order, with a key.", do=[T("stems: **tens** · leaves: **units** · a **key**", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Back-to-back", steps=[
        dict(say="Both teams share one column of stems. The Hawks' leaves go to the right. The Owls' leaves go to the left. Each side is in order, going outwards from the stem.",
             do=[TEAMS(), T("leaves in order, **outwards** from the stem", x=80, y=200)]),
        PAUSE("15.3-k2", "Your turn. What was the Hawks' lowest score? Pause the video and try it.", "Hawks' lowest score?"),
    ]),
    dict(kind="idea", title="Check: 34", steps=[
        dict(say="Stem 3, leaf 4: 34.", do=[TEAMS(), B("34", x=80, y=190, color=GREEN)]),
        dict(say="The Hawks' median is the mean of the 6th and 7th values, 46 and 49. That is 47.5. Their range is 64 minus 34, which is 30.", do=[MATH("median 47.5 · range 30", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I use a back-to-back diagram?", steps=[
        dict(say="Here is the method. Step 1: write one column of stems.", do=[T("1. One column of **stems**", x=80, y=170)]),
        dict(say="Step 2: put one set on the right, and one on the left, in order outwards.", do=[T("2. Right and left, **outwards**", x=80, y=260)]),
        dict(say="Step 3: add a key for each side.", do=[T("3. A **key** for each side", x=80, y=350)]),
        dict(say="Step 4: compare the medians and ranges.", do=[T("4. Compare **medians** and **ranges**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="The Owls", steps=[
        dict(say="On the left, read stem then leaf. The Owls' scores are 32, 36, 39, then 40, 41, 42, 44, 47, then 53, 55, 58 and 60.", do=[TEAMS(), MATH("32, 36, 39, 40, 41, 42, 44, …", x=80, y=200)]),
        dict(say="5 Owls scores were in the forties. Their range is 60 minus 32, which is 28.", do=[MATH("range 60 − 32 = 28", x=80, y=300)]),
        PAUSE("15.3-k3", "Your turn. What is the Owls' median? Pause and work it out.", "Owls' median?"),
    ]),
    dict(kind="example", title="Check: 43", steps=[
        dict(say="The 6th and 7th values are 42 and 44. The median is 43.", do=[B("(42 + 44) ÷ 2 = 43", x=80, y=190, color=GREEN)]),
        dict(say="Now compare the medians and the ranges. The Owls were a little more consistent, with a smaller range: 28, against 30.", do=[T("compare **medians** and **ranges** · Owls: smaller range", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="On the Owls' side, stem 3 shows the leaves 9, 6, 2, with 2 next to the stem. Dev reads it. Which line is wrong?", do=LINES("Dev", "Owls, stem 3: 9 6 2 (2 next to the stem)", ["the smallest value is 39"])),
        dict(say="Line 1 is wrong. Left leaves get bigger going outwards from the stem.", do=[dict(a="cross", id="l1")]),
        dict(say="The values are 32, 36 and 39. The smallest is 32.", do=[B("smallest = 32", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Before and after", steps=[
        dict(say="Doctors and sports scientists use back-to-back diagrams to compare two groups, like results before and after training.", do=[E("🏃", 90, 170, 100), T("**before** vs **after**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.3-k4", "One last question. Which team has the higher median: the Hawks, or the Owls? Pause the video and choose.", "Higher median?"),
        dict(say="The Hawks, with 47.5, compared with 43.", do=[B("Hawks: 47.5 > 43", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: one column of stems, with leaves on both sides.", do=[T("• One stem column, two sides", x=80, y=170)]),
        dict(say="Order the leaves outwards from the stem.", do=[T("• Leaves outwards from the stem", x=80, y=250)]),
        dict(say="Give a key for each side.", do=[T("• A key for each side", x=80, y=330)]),
        dict(say="Compare medians and ranges.", do=[T("• Compare medians and ranges", x=80, y=410)]),
    ]),
]

VIDEOS["15.4"] = [
    dict(kind="hook", title="Battery life", steps=[
        dict(say="A reviewer tests 40 phones, and groups their battery life in hours into classes. She has lost the individual results.",
             do=[E("🔋", 90, 170, 100), T("**40** phones · grouped results only", x=230, y=200)]),
        PAUSE("15.4-k1", "Can she still find an average? Pause the video and choose: yes, an estimate, or no.", "Can she find an average?"),
    ]),
    dict(kind="hook", title="An estimate", steps=[
        dict(say="Yes, but only an estimate, because the exact values are lost.", do=[B("Yes – an estimate", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Mean from a table", steps=[
        dict(say="Remember: the mean from a frequency table is the total of value times frequency, divided by the total frequency.", do=[MATH("mean = Σ(f × x) ÷ Σf", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Estimating the mean", steps=[
        dict(say="Use each class midpoint as an estimate of the values in that class. Multiply each midpoint by its frequency.",
             do=[TBL(["Battery t (h)", "f", "Midpoint x", "f × x"], [["10–15", "6", "12.5", "75"], ["15–20", "14", "17.5", "245"], ["20–25", "12", "22.5", "270"], ["25–30", "8", "27.5", "220"], ["Total", "40", "", "810"]], y=150), ROW(0, 2), ROW(1, 3), ROW(2, 4), ROW(3, 5), ROW(4, 6)]),
        PAUSE("15.4-k2", "Your turn. Find the estimated mean, in hours. Pause the video and try it.", "Estimated mean (h)?"),
    ]),
    dict(kind="idea", title="Check: 20.25 h", steps=[
        dict(say="810 divided by 40 is 20.25 hours. It is only an estimate, because we do not know the exact values in each class.", do=[B("810 ÷ 40 = 20.25 h", x=80, y=190, color=GREEN)]),
        dict(say="The modal class is the class with the highest frequency.", do=[T("**modal class**: highest frequency", x=80, y=300)]),
        PAUSE("15.4-k3", "Your turn. Which is the modal class: 15 to 20, or 20 to 25? Pause and choose.", "Modal class?"),
    ]),
    dict(kind="idea", title="Check: 15–20", steps=[
        dict(say="15 to 20 hours, with 14 phones.", do=[B("15 ≤ t < 20", x=80, y=190, color=GREEN)]),
        dict(say="For the median, use running totals: 6, 20, 32, 40. The 20th value is in 15 to 20, and the 21st is in 20 to 25. So the median is about 20.", do=[MATH("running totals 6, 20, 32, 40 → median ≈ 20", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I find grouped statistics?", steps=[
        dict(say="Here is the method. Step 1: find each class midpoint.", do=[T("1. **Midpoints**", x=80, y=170)]),
        dict(say="Step 2: multiply each midpoint by its frequency, and add.", do=[T("2. **f × x**, then add", x=80, y=260)]),
        dict(say="Step 3: divide by the total frequency.", do=[T("3. **÷ Σf**", x=80, y=350)]),
        dict(say="Step 4: find the modal class, and the median class from running totals.", do=[T("4. **Modal** and **median** classes", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Masses", steps=[
        dict(say="Masses in kilograms: 0 to 10, 4 items. 10 to 20, 10 items. 20 to 30, 6 items. 4 times 5, plus 10 times 15, plus 6 times 25 is 320. Divide by 20: an estimated mean of 16 kilograms.",
             do=[MATH("(20 + 150 + 150) ÷ 20 = 16 kg", x=80, y=180)]),
        dict(say="Brand A has an estimated mean of 20.25 hours, and a range of 20. Brand B has 18.9 hours, and a range of 15. A lasts longer on average. B is more consistent.", do=[T("A: longer · B: more consistent", x=80, y=290)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Max finds the estimated mean of the battery data. Which line is wrong?", do=LINES("Max", "estimated mean, battery data", ["810 ÷ 4 classes = 202.5 h"])),
        dict(say="Line 1 is wrong. He divided by the number of classes. Divide by the number of phones.", do=[dict(a="cross", id="l1")]),
        dict(say="810 divided by 40 is 20.25 hours.", do=[B("810 ÷ 40 = 20.25 h", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Census data", steps=[
        dict(say="Census data, like ages and incomes, is often published in groups. Statisticians estimate the mean using midpoints.", do=[E("📊", 90, 170, 100), T("grouped data → **midpoints**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.4-k4", "One last question. Estimate the range of the battery data: the largest possible value minus the smallest possible value. Pause the video and answer.", "Estimated range?"),
        dict(say="30 minus 10 is 20 hours.", do=[B("30 − 10 = 20 h", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: use midpoints to estimate.", do=[T("• Use midpoints", x=80, y=170)]),
        dict(say="The estimated mean is the total of f times X, divided by the total frequency.", do=[T("• Mean ≈ Σfx ÷ Σf", x=80, y=250)]),
        dict(say="The modal class has the highest frequency.", do=[T("• Modal class: highest frequency", x=80, y=330)]),
        dict(say="Find the median class from running totals.", do=[T("• Median class: running totals", x=80, y=410)]),
    ]),
]

VIDEOS["15.5"] = [
    dict(kind="hook", title="A health report", steps=[
        dict(say="A school nurse has five sets of data: favourite sports, students' heights, height against arm span, reaction times for two year groups, and sick days each month. She must choose a chart for each.",
             do=[E("🩺", 90, 170, 100), T("5 data sets · a chart for **each**", x=230, y=200)]),
        PAUSE("15.5-k1", "Height against arm span: a scatter graph, or a Venn diagram? Pause the video and choose.", "Height vs arm span?"),
    ]),
    dict(kind="hook", title="Scatter graph", steps=[
        dict(say="A scatter graph, because each student gives two measurements, and we want to see if they are related.", do=[B("scatter graph", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Charts you know", steps=[
        dict(say="Remember the charts you know: bar, pie, line, frequency diagrams and polygons, scatter graphs, stem-and-leaf, Venn and Carroll diagrams.", do=[T("bar · pie · line · frequency · scatter · stem-and-leaf · Venn", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Choosing", steps=[
        dict(say="Match the chart to the data and the question. Continuous data for one group: a frequency diagram. Comparing two groups: frequency polygons, or back-to-back stem-and-leaf. Change over time: a time series graph.",
             do=[TBL(["Data / purpose", "Good choice"], [["continuous, one group", "frequency diagram"], ["compare two groups", "polygons or back-to-back"], ["change over time", "time series graph"]], y=170), ROW(0, 3), ROW(1, 6), ROW(2, 11)]),
        PAUSE("15.5-k2", "Your turn. Favourite sports: a bar or pie chart, or a scatter graph? Pause the video and choose.", "Favourite sports?"),
    ]),
    dict(kind="idea", title="Check: bar or pie", steps=[
        dict(say="A bar chart or a pie chart. Sports are categories.", do=[B("bar or pie chart", x=80, y=190, color=GREEN)]),
        dict(say="Justify your choice. For example: a time series graph, because I want to show how sick days change from month to month.", do=[T("**justify**: link the chart to the data and the question", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I choose a chart?", steps=[
        dict(say="Here is the method. Step 1: what type of data is it: categories, numbers, or pairs?", do=[T("1. What **type** of data?", x=80, y=170)]),
        dict(say="Step 2: what is the question: proportion, trend, relationship, or comparison?", do=[T("2. What is the **question**?", x=80, y=260)]),
        dict(say="Step 3: choose the chart, and justify it.", do=[T("3. Choose and **justify**", x=80, y=350)]),
        dict(say="Step 4: check it is clear and honest: labels, scales, a key.", do=[T("4. Clear and **honest**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Criticise", steps=[
        dict(say="A pie chart of hours of sleep uses the groups 6 or more, 7 or more, 8 or more and 9 or more. The groups overlap, so one person is counted in several slices.", do=[T("6+, 7+, 8+, 9+ → they **overlap**", x=80, y=180)]),
        PAUSE("15.5-k3", "Your turn. Overlapping categories in a pie chart are: misleading, or fine? Pause and choose.", "Overlapping categories in a pie chart are …"),
    ]),
    dict(kind="example", title="Check: misleading", steps=[
        dict(say="Misleading. The slices must not overlap. Use separate groups, and a bar chart or frequency diagram.", do=[B("misleading", x=80, y=190, color=GREEN)]),
        dict(say="A bar chart of attendance whose axis starts at 90 makes 92 and 95 percent look very different. Start at 0, or show a break.", do=[T("axis from **90** → misleading", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="The nurse wants to show how sick days changed each month. Ana chooses a chart. Which line is wrong?", do=LINES("Ana", "show the change in sick days each month", ["use a pie chart of the 12 months"])),
        dict(say="Line 1 is wrong. A pie chart hides the order of the months.", do=[dict(a="cross", id="l1")]),
        dict(say="Use a time series graph to show the trend.", do=[B("a time series graph", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Infographics", steps=[
        dict(say="Public health posters, news graphics and company reports all depend on clear, honest charts.", do=[E("📰", 90, 170, 100), T("clear, **honest** charts", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("15.5-k4", "One last question. To compare two classes' marks and keep the exact values: back-to-back stem-and-leaf, or pie charts? Pause the video and choose.", "Compare two classes' marks with exact values?"),
        dict(say="A back-to-back stem-and-leaf diagram. It keeps every value, and puts the two classes side by side.", do=[B("back-to-back stem-and-leaf", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: match the chart to the data and the question.", do=[T("• Match chart to data and question", x=80, y=170)]),
        dict(say="Scatter for relationships, time series for trends, polygons or back-to-back for comparing.", do=[T("• Scatter · time series · polygons", x=80, y=250)]),
        dict(say="Justify your choice.", do=[T("• Justify your choice", x=80, y=330)]),
        dict(say="Spot misleading features.", do=[T("• Spot misleading features", x=80, y=410)]),
    ]),
]
