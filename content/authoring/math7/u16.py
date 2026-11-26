# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 16 Interpreting and discussing results (16.1 Two-way tables, 16.2 Dual and compound bar charts,
16.3 Pie charts and waffle diagrams, 16.4 Infographics, 16.5 Representing data, 16.6 Using statistics).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from collections import Counter
from kit import *

U = Unit(16, "Interpreting and Discussing Results", "Statistics and probability",
         "Two-way tables, dual and compound bar charts, pie charts and waffle diagrams, infographics, choosing a chart, and the mode, median, mean and range.",
         {"O1": {"code": "7Ss.03", "sec": "16.1", "codeNote": "", "t": "Complete and interpret two-way tables."},
          "O2": {"code": "7Ss.04", "sec": "16.2", "codeNote": "", "t": "Draw and interpret dual and compound bar charts."},
          "O3": {"code": "7Ss.05", "sec": "16.3", "codeNote": "", "t": "Interpret pie charts and waffle diagrams as parts of a whole."},
          "O4": {"code": "7Ss.06", "sec": "16.4", "codeNote": "", "t": "Read information from infographics and comment on how they present data."},
          "O5": {"code": "7Ss.07", "sec": "16.5", "codeNote": "", "t": "Choose a suitable way to represent a set of data."},
          "O6": {"code": "7Ss.08", "sec": "16.6", "codeNote": "", "t": "Find the mode, median, mean and range and use them to compare data."}})


def med(v):
    v = sorted(v); n = len(v); return v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2


# ================================================================== 16.1
s = U.section("16.1", "Two-way tables", ["O1"])
s.idea("Two-way tables", ["A **two-way table** shows two kinds of information at once, for example gender and favourite sport. Rows and columns have **totals**.",
       "Missing values can be found by adding or subtracting along a row or down a column."], table={"head": ["", "Football", "Tennis", "Total"], "rows": [["Boys", "12", "5", "17"], ["Girls", "8", "10", "18"], ["Total", "20", "15", "35"]]})
s.check(N("In the table above, how many girls chose tennis?", 10, o="O1"))
s.idea("Why the totals check everything", ["In a two-way table every row adds across to its total and every column adds down to its total. The grand total in the corner is the same both ways.",
       "Missing values can always be found from a total: total − the known parts."])
s.check(MC("Before you read on: a two-way table has row totals 12 and 18. What must the grand total be?", "30", [("6", "Add the row totals."), ("It cannot be found", "The grand total is the sum of the row totals.")], o="O1"))
s.mistake("Check the totals", ["The row totals and the column totals must both add up to the same grand total."])


def tw(r):
    a, b, c, d = [r.randint(3, 20) for _ in range(4)]
    return a, b, c, d


def w1(r):
    a, b, c, d = tw(r)
    return TB("Complete the two-way table.", ["", "Walk", "Bus", "Total"], [["Boys", str(a), str(b), B(a + b)], ["Girls", str(c), B(d), str(c + d)], ["Total", B(a + c), str(b + d), B(a + b + c + d)]], o="O1", d="H")
def w2(r):
    a, b, c, d = tw(r)
    return N("How many students were asked altogether?", a + b + c + d, "students", units=["students"], o="O1", data={"head": ["", "Walk", "Bus"], "rows": [["Boys", str(a), str(b)], ["Girls", str(c), str(d)]]})
def w3(r):
    a, b, c, d = tw(r)
    return N("How many students travel by bus?", b + d, "students", units=["students"], o="O1", data={"head": ["", "Walk", "Bus"], "rows": [["Boys", str(a), str(b)], ["Girls", str(c), str(d)]]})
def w4(r):
    a, b, c, d = tw(r)
    return N("How many more boys than girls walk? (Negative if fewer.)", a - c, o="O1", data={"head": ["", "Walk", "Bus"], "rows": [["Boys", str(a), str(b)], ["Girls", str(c), str(d)]]})
def w5(r):
    a, b, c, d = tw(r)
    return N("What fraction of the girls walk? Give a decimal to 2 d.p.", round(c / (c + d), 2), o="O1", d="H", tol=0.006, data={"head": ["", "Walk", "Bus"], "rows": [["Boys", str(a), str(b)], ["Girls", str(c), str(d)]]})
def w6(r):
    t = r.randint(30, 60); b = r.randint(10, t - 10)
    return N(f"A class of {t} has {b} boys. How many girls are there?", t - b, "girls", units=["girls"], o="O1")
def w7(r):
    a, b, c, d = tw(r)
    big = max([("boys who walk", a), ("boys who take the bus", b), ("girls who walk", c), ("girls who take the bus", d)], key=lambda x: x[1])
    if [a, b, c, d].count(big[1]) > 1: return None
    return MC("Which group is the largest?", big[0], [x for x in ["boys who walk", "boys who take the bus", "girls who walk", "girls who take the bus"] if x != big[0]], o="O1", data={"head": ["", "Walk", "Bus"], "rows": [["Boys", str(a), str(b)], ["Girls", str(c), str(d)]]})


def tw1(r):   # missing cell chain
    a, b, c = r.randint(3, 15), r.randint(3, 15), r.randint(3, 15); tot = a + b + c + r.randint(3, 15)
    return TB("Complete the two-way table.", ["", "Walk", "Bus", "Total"], [["Boys", str(a), str(b), str(a + b)], ["Girls", str(c), B(tot - a - b - c), B(tot - a - b)], ["Total", B(a + c), B(tot - a - c), str(tot)]], o="O1", d="H",
              reason="Use the totals: the column totals and the grand total fix every missing cell.")


s.std([w1, w2, w3, w4, w5, w6, w7], EX("Explain how to find a missing number in a two-way table.", [("use the row or column total", ["total"]), ("subtract the known values from the total", ["subtract|take away|minus|difference"])], "Find a row or column where only one value is missing. Subtract the known values from that row's or column's total.", o="O1"),
      deep=[tw1])

# ================================================================== 16.2
s = U.section("16.2", "Dual and compound bar charts", ["O2"])
s.idea("Comparing groups", ["A **dual bar chart** puts two bars side by side for each category, so two groups can be compared.",
       "A **compound bar chart** stacks the groups in one bar, so you can see the total and the parts."], fig={"kind": "barchart", "labels": ["Mon B", "Mon G", "Tue B", "Tue G"], "values": [8, 11, 6, 9], "ymax": 12, "step": 2, "ylabel": "Students"})
s.check(N("In the chart above, how many girls (G) came on Monday?", 11, o="O2"))
s.idea("Dual or compound?", ["A dual bar chart puts bars side by side to compare groups directly. A compound (stacked) bar chart stacks the parts so you can see each total as well as its parts.",
       "Choose dual to compare the parts; choose compound to compare the totals."])
s.check(MC("Before you read on: which chart makes it easiest to compare the TOTAL number of students in each class?", "Compound bar chart", [("Dual bar chart", "The parts are separate, so you must add them yourself."), ("Neither", "A stacked bar shows the total as its height.")], o="O2"))
s.mistake("Read the key", ["Check which colour or label shows which group."])
DAYS = ["Mon", "Tue", "Wed", "Thu"]


def b1(r):
    v = [r.randint(2, 14) for _ in range(4)]; k = r.randrange(4)
    lab = [f"{d} {g}" for d in DAYS[:2] for g in ("B", "G")]
    return N(f"The dual bar chart shows boys (B) and girls (G) in a club. How many came for '{lab[k]}'?", v[k], o="O2", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 16, "step": 2, "ylabel": "Students"})
def b2(r):
    v = [r.randint(2, 14) for _ in range(4)]
    lab = [f"{d} {g}" for d in DAYS[:2] for g in ("B", "G")]
    return N("How many students came on Monday altogether (boys and girls)?", v[0] + v[1], o="O2", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 16, "step": 2, "ylabel": "Students"})
def b3(r):
    v = [r.randint(2, 14) for _ in range(4)]
    lab = [f"{d} {g}" for d in DAYS[:2] for g in ("B", "G")]
    return N("How many more girls than boys came on Tuesday? (Negative if fewer.)", v[3] - v[2], o="O2", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 16, "step": 2, "ylabel": "Students"})
def b4(r):
    return MC("Which chart shows both the total and the parts in one bar?", "a compound bar chart", ["a dual bar chart", "a pictogram", "a line graph"], o="O2")
def b5(r):
    v = [r.randint(2, 14) for _ in range(4)]; lab = [f"{d} {g}" for d in DAYS[:2] for g in ("B", "G")]
    return TB("Read the dual bar chart to complete the table.", ["", "Boys", "Girls"], [["Mon", B(v[0]), B(v[1])], ["Tue", B(v[2]), B(v[3])]], o="O2", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 16, "step": 2, "ylabel": "Students"})
def b6(r):
    a, b = r.randint(10, 40), r.randint(10, 40)
    return N(f"In a compound bar for Year 7, the bottom part (boys) reaches {a} and the whole bar reaches {a + b}. How many girls are in Year 7?", b, "girls", units=["girls"], o="O2", d="H")


def b7(r):
    v = [r.randint(2, 14) for _ in range(4)]; lab = [f"{d} {g}" for d in DAYS[:2] for g in ("B", "G")]
    return N("How many girls came on the two days altogether?", v[1] + v[3], o="O2", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 16, "step": 2, "ylabel": "Students"})


def bc1(r):   # choose chart
    rows = r.sample([("Compare boys and girls in each sport", "Dual bar chart"), ("Show the total visitors each month, split into adults and children", "Compound bar chart"), ("Compare two shops' sales each day", "Dual bar chart")], 3)
    return GD("Which chart suits each purpose best?", "Chart", rows, o="O2", d="H", extra=["Dual bar chart", "Compound bar chart", "Pie chart"], reason="Side-by-side bars compare parts; stacked bars show totals made of parts.")


s.std([b1, b5, b2, b3, b4, b6, b7], EX("Explain when a dual bar chart is useful.", [("to compare two groups", ["compare|two groups|side by side"]), ("for each category, the two bars are next to each other", ["next to|side by side|each category"])], "A dual bar chart is useful for comparing two groups, because the two bars for each category stand side by side.", o="O2"),
      deep=[bc1])

# ================================================================== 16.3
s = U.section("16.3", "Pie charts and waffle diagrams", ["O3"])
s.idea("Parts of a whole", ["A **pie chart** shows how a whole is split up: the bigger the sector, the bigger the share. A half circle is 50%, a quarter is 25%.",
       "A **waffle diagram** is a 10 by 10 grid of 100 squares: each square is **1%**."], fig={"kind": "pie", "labels": ["Walk", "Bus", "Car", "Bike"], "values": [50, 25, 15, 10]})
s.check(N("In a waffle diagram, 37 squares are shaded. What percentage is that?", 37, "%", units=["%"], o="O3"))
s.idea("Why a pie chart uses 360°", ["A pie chart shares the whole circle (360°) between the categories in proportion. If 1/4 of the people chose red, red gets 1/4 of 360° = 90°.",
       "Angle for a category = (frequency ÷ total) × 360°."])
s.check(MC("Before you read on: 30 people were asked. How many degrees does each person get in the pie chart?", "12°", [("30°", "360 ÷ 30 = 12."), ("3°", "Share 360° between 30 people.")], o="O3"))
s.mistake("Compare like with like", ["A bigger slice in a pie chart of 20 people may be fewer people than a smaller slice in a pie chart of 200."])
LAB = ["Football", "Tennis", "Swimming", "Running", "Hockey"]


def p1(r):
    v = pick(r, [[50, 25, 25], [50, 30, 20], [40, 30, 20, 10], [25, 25, 50], [60, 20, 20]]); lab = r.sample(LAB, len(v)); k = r.randrange(len(v))
    return N(f"The pie chart shows favourite sports. What percentage chose {lab[k].lower()}?", v[k], "%", units=["%"], o="O3", fig={"kind": "pie", "labels": [f"{l} ({x}%)" if i != k else l for i, (l, x) in enumerate(zip(lab, v))], "values": v}) if False else N(f"The pie chart shows favourite sports. The {lab[k].lower()} sector is shown as a fraction of the circle. What percentage chose {lab[k].lower()}?", v[k], "%", units=["%"], o="O3", fig={"kind": "pie", "labels": lab, "values": v, "angles": True})
def p2(r):
    t = r.randint(2, 10) * 20; pc = pick(r, [25, 50, 10, 20, 75])
    return N(f"A pie chart shows {t} people. One sector is {pc}% of the pie. How many people is that?", t * pc // 100, "people", units=["people"], o="O3")
def p3(r):
    k = r.randint(5, 95)
    return N(f"A waffle diagram has 100 squares and {k} are shaded. What fraction of the whole is shaded? Give a decimal.", k / 100, o="O3")
def p4(r):
    v = [r.randint(1, 6) * 10 for _ in range(3)]; v.append(100 - sum(v)); lab = r.sample(LAB, 4)
    if v[3] <= 0: return None
    k = max(range(4), key=lambda i: v[i])
    if v.count(v[k]) > 1: return None
    return MC("Which sport is the most popular?", lab[k], [x for x in lab if x != lab[k]], o="O3", fig={"kind": "pie", "labels": lab, "values": v})
def p5(r):
    a, b, c = r.randint(10, 40), r.randint(10, 30), r.randint(5, 20); d = 100 - a - b - c
    return TB("A waffle diagram shows how 100 students travel. Complete the table.", ["Travel", "Squares", "Percentage"], [["Walk", str(a), B(a)], ["Bus", str(b), B(b)], ["Other", B(d), B(d)]], o="O3", data={"head": ["Walk", "Bus", "Car"], "rows": [[str(a), str(b), str(c)]]})
def p6(r):
    t1, t2 = r.randint(20, 40), r.randint(150, 300)
    return MC(f"In School A's pie chart ({t1} students) 'Bus' is half the pie. In School B's pie chart ({t2} students) 'Bus' is a quarter. Which school has more bus users?", "School B", ["School A", "They have the same", "You cannot compare pie charts"], o="O3", d="H")
def p7(r):
    return MC("A sector is exactly a quarter of a pie chart. What percentage is that?", "25%", ["4%", "40%", "75%"], o="O3")


def pc1(r):   # spot the error
    return MC("Two pie charts show that 50% of class A and 50% of class B walk to school. Jo says the same number of students walk in each class. Is she right?", "Not necessarily – the classes may have different sizes", [("Yes", "50% of 20 is 10 but 50% of 30 is 15."), ("No – class A always has more", "Without the totals you cannot tell.")], o="O3", d="H",
              reason="A pie chart shows proportions, not the actual numbers.")


s.std([p1, p5, p2, p3, p4, p6, p7], EX("Explain how a waffle diagram shows percentages.", [("it has 100 squares", ["100"]), ("each square is 1%, so count the shaded squares", ["1%|one per cent|count"])], "A waffle diagram is a grid of 100 squares, so each square is 1% of the whole. Count the shaded squares to read the percentage.", o="O3"),
      deep=[pc1])

# ================================================================== 16.4
s = U.section("16.4", "Infographics", ["O4"])
s.idea("Reading infographics", ["An **infographic** mixes pictures, numbers and short text to show information quickly.",
       "Read the numbers carefully and check that the pictures are not misleading (for example, a picture twice as tall may look four times as big)."])
s.check(MC("Why should you check the numbers on an infographic, not just the pictures?", "pictures can make differences look bigger or smaller than they are", ["the pictures are always wrong", "numbers are not important", "infographics never have numbers"], o="O4"))
s.idea("Reading an infographic critically", ["Infographics mix pictures, numbers and charts. Check what each symbol is worth, whether the axes start at zero, and where the data came from.",
       "A picture can make a difference look bigger than it is, for example by making an icon twice as tall AND twice as wide."])
s.mistake("Size of pictures", ["Doubling the height AND width of a picture makes it look four times as big."])


def i1(r):
    a, b = r.randint(20, 90), r.randint(20, 90)
    return N(f"An infographic says {a}% of students like music and {b}% like sport. What is the difference in percentage points?", abs(a - b), "%", units=["%"], o="O4", data={"head": ["Likes", "Music", "Sport"], "rows": [["Students", f"{a}%", f"{b}%"]]})
def i2(r):
    n = r.randint(200, 900); pc = pick(r, [10, 20, 25, 50])
    return N(f"An infographic says '{pc}% of our {n} students cycle to school'. How many students is that?", n * pc / 100, "students", units=["students"], o="O4")
def i3(r):
    k = r.randint(2, 6); v = k * r.randint(10, 50)
    return N(f"In an infographic, each 🍎 symbol stands for {k} apples. There are {v // k} symbols. How many apples is that?", v, "apples", units=["apples"], o="O4")
def i4(r):
    v = [r.randint(5, 20) for _ in range(3)]
    return N("The infographic table shows hours of screen time per week. What is the total?", sum(v), "hours", units=["hours"], o="O4", data={"head": ["Device", "Phone", "TV", "Computer"], "rows": [["Hours", *map(str, v)]]})
def i5(r):
    return MC("A picture of a bag of rice is drawn twice as tall and twice as wide to show 'twice as much rice'. Why is this misleading?", "it looks four times as big", ["it is the wrong colour", "rice cannot be counted", "it is too small"], o="O4", d="H")
def i6(r):
    a = r.randint(1, 9) * 10
    return N(f"An infographic shows {a} out of every 100 people recycle. How many out of 20 people is that?", a * 20 // 100, "people", units=["people"], o="O4", d="H")
def i7(r):
    rows = [("Uses pictures to show numbers", "Infographic"), ("A grid of 100 squares", "Waffle diagram"), ("Sectors of a circle", "Pie chart"), ("Rows and columns with totals", "Two-way table")]
    return GD("Match each description to the display.", "Display", rows, o="O4")


def ig1(r):   # misleading
    return MC("An infographic shows 2 cars and 1 car, but the first car is drawn twice as tall and twice as wide. Why is this misleading?", "The bigger car looks 4 times bigger, not 2 times", [("It is not misleading", "Doubling both height and width makes the area 4 times bigger."), ("Cars cannot show numbers", "Icons are fine if their sizes are fair.")], o="O4", d="H",
              reason="The eye compares areas; 2 × 2 = 4 times the area exaggerates a ratio of 2.")


s.std([i1, i4, i2, i3, i5, i6, i7], EX("Explain one way an infographic can be misleading.", [("pictures can be the wrong size / scale, or axes can start above zero", ["size|scale|picture|axis|zero"]), ("so differences look bigger or smaller than they really are", ["bigger|smaller|exaggerat|look"])], "Pictures can be drawn at the wrong size: making a picture twice as tall and twice as wide makes it look four times as big, so the difference looks bigger than it really is.", o="O4"),
      deep=[ig1])

# ================================================================== 16.5
s = U.section("16.5", "Representing data", ["O5"])
s.idea("Choosing a display", ["**Bar chart**: compare categories. **Pie chart / waffle diagram**: parts of a whole. **Line graph**: change over time. **Two-way table**: two kinds of information.",
       "Choose the display that answers your question most clearly."])
s.check(MC("Which display best shows how a puppy's mass changes over 6 months?", "a line graph", ["a pie chart", "a two-way table", "a waffle diagram"], o="O5"))
s.idea("Choosing a diagram", ["Bar charts compare categories. Pie charts show parts of one whole. Line graphs show change over time. Frequency diagrams show grouped continuous data.",
       "Ask: what question do I want the reader to answer at a glance?"])
s.mistake("Pie charts need a whole", ["Only use a pie chart if the parts make one whole."])
CH = [("Favourite fruit of a class", "Bar chart"), ("How a family spends its money", "Pie chart"), ("Temperature each day for a week", "Line graph"), ("Boys and girls who walk or take the bus", "Two-way table"),
      ("Percentage of a garden used for each crop", "Waffle diagram"), ("Number of books read by each student", "Bar chart")]


def c1(r):
    q, a = pick(r, CH)
    return MC(f"Which display is best for this data? {q}", a, [x for x in ["Bar chart", "Pie chart", "Line graph", "Two-way table", "Waffle diagram"] if x != a][:3], o="O5")
def c2(r):
    return GD("Choose the best display for each set of data.", "Display", r.sample(CH, 4), o="O5", extra=["Bar chart", "Pie chart", "Line graph"])
def c3(r):
    v = [r.randint(2, 15) for _ in range(4)]; lab = r.sample(["Cats", "Dogs", "Fish", "Birds", "Rabbits"], 4); k = r.randrange(4)
    return N(f"The bar chart shows pets owned by a class. How many {lab[k].lower()} are there?", v[k], o="O5", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 16, "step": 2, "ylabel": "Number"})
def c4(r):
    v = [r.randint(2, 15) for _ in range(4)]; lab = r.sample(["Cats", "Dogs", "Fish", "Birds", "Rabbits"], 4)
    return N("How many pets are shown altogether?", sum(v), o="O5", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 16, "step": 2, "ylabel": "Number"})
def c5(r):
    return MC("A bar chart's vertical axis starts at 40 instead of 0. Why can this be misleading?", "small differences look much bigger", ["the bars are too wide", "it uses too many colours", "the title is missing"], o="O5", d="H")
def c6(r):
    return MS("Select ALL the displays that show parts of a whole.", ["Pie chart", "Waffle diagram"], ["Line graph", "Two-way table"], o="O5")
def c7(r):
    v = [r.randint(2, 15) for _ in range(4)]; lab = ["Cats", "Dogs", "Fish", "Birds"]
    k = max(range(4), key=lambda i: v[i])
    if v.count(v[k]) > 1: return None
    return MC("Which pet is the most common?", lab[k], [x for x in lab if x != lab[k]], o="O5", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 16, "step": 2, "ylabel": "Number"})


def rp1(r):   # choose
    rows = r.sample([("how temperature changes during a day", "Line graph"), ("the proportion of a budget spent on each item", "Pie chart"), ("the number of each pet owned by a class", "Bar chart"), ("heights of plants in groups", "Frequency diagram")], 4)
    return GD("Choose the best diagram for each set of data.", "Diagram", rows, o="O5", d="H", extra=["Pictogram"], reason="Match the diagram to the question: change over time, parts of a whole, comparing categories or grouped measurements.")


s.std([c2, c3, c1, c4, c5, c6, c7], EX("Explain why a line graph is better than a pie chart for showing temperature over a week.", [("a line graph shows change over time", ["change over time|over time|trend"]), ("temperatures are not parts of a whole", ["parts of a whole|not a whole|don't add|do not add"])], "A line graph shows how the temperature changes over time. A pie chart shows parts of a whole, but daily temperatures do not make up a whole.", o="O5"),
      deep=[rp1])

# ================================================================== 16.6
s = U.section("16.6", "Using statistics", ["O6"])
s.idea("Averages and range", ["**Mode**: the most common value. **Median**: the middle value when the data is in order. **Mean**: add all the values and divide by how many there are.",
       "**Range** = largest − smallest. It shows how spread out the data is."], table={"head": ["Data", "3, 5, 5, 7, 10"], "rows": [["Mode", "5"], ["Median", "5"], ["Mean", "30 ÷ 5 = 6"], ["Range", "10 − 3 = 7"]]})
s.check(N("Find the mean of 4, 6, 8 and 10.", 7, o="O6"))
s.idea("Mean, median or mode?", ["The mode is the most common value – the only average for categorical data. The median is the middle value – not affected by one very big or very small value. The mean uses every value – a single extreme value can pull it a long way.",
       "Example: salaries 20, 22, 25, 25, 200 (thousand). Mean = 58.4, median = 25, mode = 25. The mean is misleading here."])
s.check(MC("Before you read on: which average is best for 'favourite colour'?", "Mode", [("Mean", "You cannot add colours."), ("Median", "Colours have no order.")], o="O6"))
s.mistake("Order first", ["Put the data in order before finding the median."])


def a1(r):
    v = [r.randint(1, 20) for _ in range(r.randint(4, 7))]
    return N(f"Find the mean of {', '.join(map(str, v))}. Give your answer to 1 d.p. if needed.", round(sum(v) / len(v), 1), o="O6", tol=0.05)
def a2(r):
    v = [r.randint(1, 30) for _ in range(pick(r, [5, 7, 9]))]
    return N(f"Find the median of {', '.join(map(str, v))}.", med(v), o="O6")
def a3(r):
    v = [r.randint(1, 9) for _ in range(9)]; c = Counter(v); m = max(c.values()); md = [k for k, x in c.items() if x == m]
    if len(md) > 1: return None
    return N(f"Find the mode of {', '.join(map(str, v))}.", md[0], o="O6")
def a4(r):
    v = [r.randint(1, 50) for _ in range(6)]
    return N(f"Find the range of {', '.join(map(str, v))}.", max(v) - min(v), o="O6")
def a5(r):
    v = [r.randint(1, 15) for _ in range(5)]
    return TB(f"Find the statistics for {', '.join(map(str, v))}.", ["Statistic", "Value"], [["Range", B(max(v) - min(v))], ["Median", B(med(v))], ["Mean", B(sum(v) / 5)]], o="O6")
def a6(r):
    a, b = r.randint(10, 20), r.randint(10, 20); ra, rb = r.randint(2, 6), r.randint(8, 15)
    if a == b: return None
    return MC(f"Team A: mean {a} points, range {ra}. Team B: mean {b} points, range {rb}. Which statement is correct?", f"Team {'A' if a > b else 'B'} scored more on average and Team A was more consistent", [f"Team {'B' if a > b else 'A'} scored more on average", "Team B was more consistent", "The teams are the same"], o="O6", d="H")
def a7(r):
    v = [r.randint(5, 15) for _ in range(4)]; n = 5; m = r.randint(8, 14); last = m * n - sum(v)
    if last <= 0: return None
    return N(f"The mean of five numbers is {m}. Four of them are {', '.join(map(str, v))}. What is the fifth number?", last, o="O6", d="H")
def a8(r):
    f = [r.randint(1, 8) for _ in range(4)]
    k = max(range(4), key=lambda i: f[i])
    if f.count(f[k]) > 1: return None
    return N("The table shows the number of pets owned by students. What is the mode?", k, "pets", units=["pets"], o="O6", data={"head": ["Pets", "0", "1", "2", "3"], "rows": [["Students", *map(str, f)]]})


def st1(r):   # effect of outlier
    v = sorted(r.sample(range(10, 30), 5)); big = 100
    m1 = sum(v) / 5; m2 = (sum(v) + big) / 6
    return MC(f"The values {', '.join(map(str, v))} have mean {m1:g}. A sixth value, {big}, is added. What happens?", "The mean rises a lot; the median changes only a little",
              [("Both change by the same amount", "The mean uses the size of every value; the median only uses the middle position."), ("The median rises a lot", "The median moves only to the next middle position.")], o="O6", d="H",
              reason=f"New mean = {m2:.1f}. Median moves from {v[2]} to {(v[2] + v[3]) / 2:g}.")
def st2(r):   # find missing value for mean
    v = r.sample(range(2, 15), 4); m = r.randint(6, 12)
    x = 5 * m - sum(v)
    if x <= 0 or x > 40: return None
    return N(f"Five numbers have a mean of {m}. Four of them are {', '.join(map(str, v))}. What is the fifth?", x, o="O6", d="H", reason=f"Total = 5 × {m} = {5 * m}; {5 * m} − {sum(v)} = {x}.")


s.std([a5, a8, a1, a2, a3, a4, a6, a7], EX("Explain how to find the median of 7, 2, 9, 4, 5.", [("put the numbers in order: 2, 4, 5, 7, 9", ["order|2, ?4, ?5"]), ("the middle value is 5", ["\\b5\\b|middle"])], "Put the numbers in order: 2, 4, 5, 7, 9. The median is the middle value, 5.", o="O6"),
      deep=[st1, st2])

U.mindmap(("Two-way tables", "Rows, columns, totals", "O1", "16.1"), ("Dual and compound bar charts", "Compare groups • see totals", "O2", "16.2"),
          ("Pie charts and waffles", "Parts of a whole • 1 square = 1%", "O3", "16.3"), ("Infographics", "Read the numbers • watch for misleading pictures", "O4", "16.4"),
          ("Choosing a display", "Match the display to the question", "O5", "16.5"), ("Statistics", "Mode, median, mean, range", "O6", "16.6"))
