# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 16 Interpreting and discussing results (16.1 Frequency diagrams, 16.2 Time series graphs,
16.3 Stem-and-leaf diagrams, 16.4 Pie charts, 16.5 Representing data, 16.6 Using statistics). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *

U = Unit(16, "Interpreting and Discussing Results", "Statistics and probability",
         "Frequency diagrams, time series graphs, stem-and-leaf diagrams and pie charts, choosing a representation, and comparing data with averages and the range.",
         {"O1": {"code": "8Ss.03", "sec": "16.1", "codeNote": "", "t": "Draw and interpret frequency diagrams for grouped discrete and continuous data."},
          "O2": {"code": "8Ss.04", "sec": "16.2", "codeNote": "", "t": "Draw and interpret time series graphs and describe trends."},
          "O3": {"code": "8Ss.05", "sec": "16.3", "codeNote": "", "t": "Draw and interpret stem-and-leaf diagrams, and find the median, mode and range from them."},
          "O4": {"code": "8Ss.06", "sec": "16.4", "codeNote": "", "t": "Draw and interpret pie charts, calculating angles and frequencies."},
          "O5": {"code": "8Ss.07", "sec": "16.5", "codeNote": "", "t": "Choose a suitable graph or chart for a set of data and explain the choice."},
          "O6": {"code": "8Ss.08", "sec": "16.6", "codeNote": "", "t": "Use the mean, median, mode and range to compare sets of data and draw conclusions."}})


def med(v):
    v = sorted(v); n = len(v); return v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2


def sl(vals):
    st = sorted({v // 10 for v in vals}); st = list(range(st[0], st[-1] + 1))
    return {"kind": "stemleaf", "stems": st, "right": [sorted(v % 10 for v in vals if v // 10 == s_) for s_ in st], "key": f"Key: {st[0]} | 3 means {st[0] * 10 + 3}"}


# ================================================================== 16.1
s = U.section("16.1", "Interpreting and drawing frequency diagrams", ["O1"])
s.idea("Grouped data", ["When there are lots of different values, group them into **classes** of equal width, such as 0 ≤ t < 10, 10 ≤ t < 20.",
       "A **frequency diagram** for continuous data has bars that touch, with the classes on a continuous scale."], fig={"kind": "barchart", "labels": ["0–10", "10–20", "20–30", "30–40"], "values": [4, 9, 12, 5], "ymax": 14, "step": 2, "ylabel": "Frequency", "xlabel": "Time (minutes)"})
s.check(N("From the diagram above, how many people took 20 to 30 minutes?", 12, "people", units=["people"], o="O1"))
s.idea("Modal class", ["The **modal class** is the class with the highest frequency. Add all the frequencies to find the total."])
s.mistake("Class boundaries", ["A time of exactly 10 minutes goes in 10 ≤ t < 20, not 0 ≤ t < 10."])
CL = ["0–10", "10–20", "20–30", "30–40", "40–50"]


def fq(r, k=5): return [r.randint(1, 15) for _ in range(k)]
def fd(f, lab="Time (minutes)"): return {"kind": "barchart", "labels": CL[:len(f)], "values": f, "ymax": max(f) + 2 - max(f) % 2, "step": 2, "ylabel": "Frequency", "xlabel": lab}


def g1(r):
    f = fq(r); k = r.randrange(5)
    return N(f"The frequency diagram shows how long students spent on homework. How many students spent {CL[k].replace('–', ' to ')} minutes?", f[k], "students", units=["students"], o="O1", fig=fd(f))
def g2(r):
    f = fq(r)
    return N("How many students are shown altogether in the frequency diagram?", sum(f), "students", units=["students"], o="O1", fig=fd(f), reason=f"{' + '.join(map(str, f))} = {sum(f)}.")
def g3(r):
    f = fq(r); k = max(range(5), key=lambda i: f[i])
    if f.count(f[k]) > 1: f[k] += 1
    return MC("What is the modal class?", CL[k], [c for c in CL if c != CL[k]][:3], o="O1", fig=fd(f))
def g4(r):
    f = fq(r); k = r.randint(1, 4)
    return N(f"How many students spent at least {k * 10} minutes?", sum(f[k:]), "students", units=["students"], o="O1", d="H", fig=fd(f), reason=f"Add the classes from {k * 10} up: {sum(f[k:])}.")
def g5(r):
    vals = [r.randint(0, 49) for _ in range(16)]
    f = [sum(1 for v in vals if 10 * i <= v < 10 * i + 10) for i in range(5)]
    return TB(f"Put these times (minutes) into the frequency table: {', '.join(map(str, vals))}.", ["Time t (min)", "Frequency"], [[f"{10 * i} ≤ t < {10 * i + 10}", B(f[i])] for i in range(5)], o="O1", d="H")
def g6(r):
    v = r.choice([10, 20, 30, 40])
    return MC(f"A time of exactly {v} minutes is recorded. Which class does it go in?", f"{v} ≤ t < {v + 10}", [f"{v - 10} ≤ t < {v}", f"{v + 10} ≤ t < {v + 20}", "either class"], o="O1")
def g7(r):
    f = fq(r); k = r.randrange(5)
    return N(f"What percentage of the students spent {CL[k].replace('–', ' to ')} minutes? Give your answer to 1 d.p.", round(f[k] / sum(f) * 100, 1), "%", units=["%"], o="O1", d="H", tol=0.05, fig=fd(f))


s.std([g1, g2, g3, g4, g5, g6, g7], EX("Explain why the bars of a frequency diagram for continuous data touch.", [("the data is continuous: there are no gaps between classes", ["continuous|no gaps|measured|any value"]), ("one class ends where the next begins", ["ends|begins|next class|boundary"])], "The data is continuous, so every value fits somewhere on the scale. One class ends exactly where the next begins, so there are no gaps between the bars.", o="O1"))

# ================================================================== 16.2
s = U.section("16.2", "Time series graphs", ["O2"])
s.idea("Change over time", ["A **time series graph** shows how something changes over time. Time goes on the horizontal axis. Plot the points and join them with straight lines.",
       "Describe the **trend**: increasing, decreasing or staying about the same, and any pattern that repeats (such as seasons)."], fig={"kind": "linegraph", "x": {"min": 1, "max": 6, "step": 1, "label": "Month"}, "y": {"min": 0, "max": 30, "step": 5, "label": "Temperature (°C)"}, "series": [{"pts": [[1, 12], [2, 15], [3, 19], [4, 24], [5, 27], [6, 26]]}]})
s.check(N("From the graph above, what was the temperature in month 4 (°C)?", 24, "°C", units=["°C"], o="O2"))
s.mistake("In-between points", ["The lines between points only show the trend; values between months may not be exact."])


def ts(r, k=6, lo=10, hi=40):
    v = [r.randint(lo, hi)]
    for _ in range(k - 1): v.append(max(lo, min(hi, v[-1] + r.randint(-6, 8))))
    return v


def tf(v, lab="Visitors (hundreds)"): return {"kind": "linegraph", "x": {"min": 1, "max": len(v), "step": 1, "label": "Week"}, "y": {"min": 0, "max": max(v) + 5 - max(v) % 5, "step": 5, "label": lab}, "series": [{"pts": [[i + 1, x] for i, x in enumerate(v)]}]}


def h1(r):
    v = ts(r); k = r.randrange(6)
    return N(f"The time series graph shows visitors (in hundreds) to a museum. How many hundreds of visitors were there in week {k + 1}?", v[k], o="O2", fig=tf(v))
def h2(r):
    v = ts(r); k = max(range(6), key=lambda i: v[i])
    if v.count(v[k]) > 1: return None
    return N("In which week were there the most visitors?", k + 1, o="O2", fig=tf(v))
def h3(r):
    v = ts(r); i = r.randrange(5)
    return N(f"By how much (in hundreds) did the number of visitors change from week {i + 1} to week {i + 2}? (Negative for a fall.)", v[i + 1] - v[i], o="O2", d="H", fig=tf(v))
def h4(r):
    v = sorted(ts(r)); up = r.random() < 0.5
    if not up: v = v[::-1]
    return MC("Describe the trend shown by the graph.", "increasing" if up else "decreasing", ["decreasing" if up else "increasing", "no change", "it goes up and down equally"], o="O2", fig=tf(v))
def h5(r):
    v = ts(r)
    return TB("Read the graph to complete the table.", ["Week", "Visitors (hundreds)"], [[str(i + 1), B(v[i])] for i in r.sample(range(6), 3)], o="O2", fig=tf(v))
def h6(r):
    v = ts(r)
    return N("Find the range of the weekly visitor numbers shown (in hundreds).", max(v) - min(v), o="O2", fig=tf(v), reason=f"{max(v)} − {min(v)} = {max(v) - min(v)}.")
def h7(r):
    v = ts(r)
    return N("Find the mean number of visitors per week (in hundreds), to 1 d.p.", round(sum(v) / 6, 1), o="O2", d="H", tol=0.05, fig=tf(v), reason=f"{sum(v)} ÷ 6 ≈ {round(sum(v) / 6, 1)}.")


s.std([h1, h5, h2, h3, h4, h6, h7], EX("Explain why time is always put on the horizontal axis of a time series graph.", [("time is the independent variable / goes in order left to right", ["independent|order|left to right|along"]), ("so you can read how the other value changes as time passes", ["changes|trend|over time"])], "Time is the variable that goes steadily in order, so it goes along the horizontal axis. Then you can read how the other value changes as time passes, from left to right.", o="O2"))

# ================================================================== 16.3
s = U.section("16.3", "Stem-and-leaf diagrams", ["O3"])
s.idea("Ordered data", ["A **stem-and-leaf diagram** keeps every value. The **stem** is the tens digit and the **leaf** is the units digit. Leaves are written in order, and a **key** explains how to read it.",
       "Because the data is in order, it is easy to find the median, mode and range."], fig={"kind": "stemleaf", "stems": [1, 2, 3, 4], "right": [[2, 5, 8], [0, 3, 3, 7], [1, 4, 9], [2]], "key": "Key: 2 | 3 means 23"})
s.check(N("From the diagram above, what is the largest value?", 42, o="O3"))
s.idea("Why a stem-and-leaf diagram is useful", ["It sorts the data AND keeps every value, so you can read off the median and range straight away, and see the shape like a bar chart turned on its side.",
       "Always include a key, such as 3 | 4 means 34."])
s.mistake("Use the key", ["2 | 3 might mean 23, 2.3 or 230. Always read the key."])


def vals(r, n=11, lo=12, hi=58): return sorted(r.randint(lo, hi) for _ in range(n))


def l1(r):
    v = vals(r)
    return N("Find the median of the data in the stem-and-leaf diagram.", med(v), o="O3", fig=sl(v), reason=f"The middle (6th) value is {med(v)}.")
def l2(r):
    v = vals(r)
    return N("Find the range of the data in the stem-and-leaf diagram.", v[-1] - v[0], o="O3", fig=sl(v))
def l3(r):
    v = vals(r, 10)
    return N("How many values in the stem-and-leaf diagram are more than 30?", sum(1 for x in v if x > 30), o="O3", fig=sl(v))
def l4(r):
    v = vals(r, 12); v[3] = v[4]
    from collections import Counter
    c = Counter(v); m = max(c.values()); mode = [k for k, x in c.items() if x == m]
    if len(mode) > 1: return None
    return N("Find the mode of the data in the stem-and-leaf diagram.", mode[0], o="O3", fig=sl(sorted(v)))
def l5(r):
    v = vals(r, 10)
    return N("Find the median of the data in the stem-and-leaf diagram (10 values).", med(v), o="O3", d="H", fig=sl(v), reason=f"Mean of the 5th and 6th values: {fmt(med(v))}.")
def l6(r):
    v = vals(r, 9)
    return TB("Use the stem-and-leaf diagram to complete the table.", ["Statistic", "Value"], [["Smallest", B(v[0])], ["Largest", B(v[-1])], ["Median", B(med(v))]], o="O3", fig=sl(v))
def l7(r):
    v = vals(r, 9)
    return S(f"Write the stem and leaf for {v[4]}. Type it like 3 | 5.", [f"{v[4] // 10} | {v[4] % 10}", f"{v[4] // 10}|{v[4] % 10}", f"{v[4] // 10} {v[4] % 10}"], o="O3")


def n163(r):
    vals = sorted(r.sample(range(20, 60), 9))
    return N("Here are 9 values in order: " + ", ".join(map(str, vals)) + ". In a stem-and-leaf diagram, what would the median be?", vals[4], o="O3", d="H", reason=f"The 5th value of 9 is the middle one: {vals[4]}.")


s.std([l1, l6, l2, l3, l4, l5, l7], EX("Explain one advantage of a stem-and-leaf diagram over a bar chart of grouped data.", [("it shows every individual value", ["every value|all the values|each value|raw data|individual"]), ("so you can find the median, mode and range exactly", ["median|mode|range|exact"])], "A stem-and-leaf diagram keeps every individual value in order, so you can still find the median, mode and range exactly; grouping loses the exact values.", o="O3"),
      deep=[n163])

# ================================================================== 16.4
s = U.section("16.4", "Pie charts", ["O4"])
s.idea("Angles", ["A **pie chart** shows how a whole is shared. The whole circle is **360°**.",
       "Angle for a group = frequency ÷ total × 360°. With 40 people, each person is 360 ÷ 40 = 9°."], fig={"kind": "pie", "labels": ["Walk", "Bus", "Car", "Bike"], "values": [10, 15, 9, 6], "angles": True})
s.example("Drawing", "Of 40 students, 10 walk. Find the angle for 'Walk'.", [("each student = 360 ÷ 40 = 9°", ""), ("10 × 9° = 90°", "")], "90°")
s.check(N("In a pie chart of 60 people, one sector is 120°. How many people does it represent?", 20, "people", units=["people"], o="O4"))
s.mistake("Compare totals", ["A bigger sector in one pie chart does not mean more people than a smaller sector in another pie chart with a bigger total."])
LAB = ["Football", "Tennis", "Swimming", "Hockey", "Running"]


def c1(r):
    t = pick(r, [20, 24, 30, 36, 40, 45, 60, 72, 90]); f = r.randint(1, t // 2)
    return N(f"A survey asked {t} people. {f} chose football. What angle is the football sector in a pie chart?", f * 360 / t, "°", units=["°"], o="O4", reason=f"{f} ÷ {t} × 360 = {fmt(f * 360 / t)}°.")
def c2(r):
    t = pick(r, [30, 36, 40, 45, 60, 72, 90, 120]); a = pick(r, [x for x in range(10, 300, 10) if (x * t) % 360 == 0])
    return N(f"A pie chart shows {t} people. One sector has an angle of {a}°. How many people does it represent?", a * t // 360, "people", units=["people"], o="O4", reason=f"{a} ÷ 360 × {t} = {a * t // 360}.")
def c3(r):
    t = pick(r, [36, 40, 45, 60, 72]); f = [r.randint(2, 12) for _ in range(3)]; f.append(t - sum(f))
    if f[3] <= 0: return None
    lab = r.sample(LAB, 4)
    return TB(f"Complete the angles for a pie chart of {t} people.", ["Sport", "Frequency", "Angle (°)"], [[lab[i], str(f[i]), B(f[i] * 360 / t)] for i in range(4)], o="O4", d="H")
def c4(r):
    a = [r.randint(4, 12) * 10 for _ in range(3)]; d = 360 - sum(a)
    if d <= 0: return None
    lab = r.sample(LAB, 4)
    return N(f"Three sectors of a pie chart are {a[0]}°, {a[1]}° and {a[2]}°. Find the angle of the fourth sector.", d, "°", units=["°"], o="O4", fig={"kind": "pie", "labels": lab, "values": a + [d], "angles": True, "hide": [3]}, reason=f"360 − {sum(a)} = {d}°.")
def c5(r):
    v = [r.randint(2, 10) * 10 for _ in range(3)]; v.append(360 - sum(v)); lab = r.sample(LAB, 4)
    if v[3] <= 0: return None
    k = max(range(4), key=lambda i: v[i])
    if v.count(v[k]) > 1: return None
    return MC("Which sport is the most popular?", lab[k], [x for x in lab if x != lab[k]], o="O4", fig={"kind": "pie", "labels": lab, "values": v})
def c6(r):
    t = pick(r, [40, 60, 80, 120]); a = pick(r, [90, 180, 45, 270])
    return N(f"A pie chart shows {t} people. The 'Yes' sector is {a}°. What fraction of the people said yes? Give a decimal.", a / 360, o="O4", reason=f"{a} ÷ 360 = {fmt(a / 360)}.")
def c7(r):
    t1, t2 = r.randint(20, 50), r.randint(100, 200); a = r.randint(6, 12) * 10
    return MC(f"In two pie charts the 'Bus' sector is {a}°. Chart A shows {t1} students and chart B shows {t2} students. Which shows more students who take the bus?", "chart B", [("chart A", "The angles are the same but B has more students."), ("they show the same number", "Same angle only means the same FRACTION."), ("you cannot tell", "")], o="O4", d="H")


s.std([c4, c3, c1, c2, c5, c6, c7], EX("Explain how to work out the angle for 15 people in a pie chart of 45 people.", [("each person is 360 ÷ 45 = 8°", ["8°|360 ?÷ ?45|= ?8"]), ("15 × 8 = 120°", ["120"])], "Each person is 360° ÷ 45 = 8°. So 15 people are 15 × 8° = 120°.", o="O4"))

# ================================================================== 16.5
s = U.section("16.5", "Representing data", ["O5"])
s.idea("Choosing a chart", ["**Bar chart**: compare categories. **Frequency diagram**: grouped continuous data. **Pie chart**: parts of a whole. **Line graph / time series**: change over time. **Stem-and-leaf**: show all values in order. **Scatter graph**: compare two variables."])
s.check(MC("Which chart best shows how the temperature changes during a day?", "a time series (line) graph", [("a pie chart", ""), ("a stem-and-leaf diagram", ""), ("a pictogram", "")], o="O5"))
s.mistake("Pie charts need a whole", ["Only use a pie chart when the categories make up one whole."])
CH = [("Favourite colours of 30 students", "Bar chart"), ("How a family spends its monthly income", "Pie chart"), ("Daily rainfall over a month", "Time series graph"), ("Heights of 40 plants, grouped", "Frequency diagram"),
      ("Exact test scores of a class, in order", "Stem-and-leaf diagram"), ("Hours of revision and test score for each student", "Scatter graph"), ("Monthly ice-cream sales over a year", "Time series graph"), ("Share of each sport chosen at a club", "Pie chart")]


def d1(r):
    q, a = pick(r, CH)
    return MC(f"Which is the best way to show this data? {q}", a, [x for x in ["Bar chart", "Pie chart", "Time series graph", "Frequency diagram", "Stem-and-leaf diagram", "Scatter graph"] if x != a][:3], o="O5")
def d2(r):
    return GD("Choose the best chart for each set of data.", "Chart", r.sample(CH, 4), o="O5", extra=["Bar chart", "Pie chart", "Time series graph", "Scatter graph"])
def d3(r):
    f = [r.randint(2, 12) for _ in range(4)]; lab = r.sample(["Cats", "Dogs", "Fish", "Birds", "Rabbits"], 4); k = r.randrange(4)
    return N(f"The bar chart shows the pets owned by a class. How many more {lab[k].lower()} than the smallest group?", f[k] - min(f), o="O5", fig={"kind": "barchart", "labels": lab, "values": f, "ymax": 14, "step": 2, "ylabel": "Number"})
def d4(r):
    return MC("A bar chart's vertical axis starts at 50 instead of 0. Why can this be misleading?", "differences between the bars look bigger than they are", [("the bars are the wrong colour", ""), ("there are too many bars", ""), ("the labels are missing", "")], o="O5", d="H")
def d5(r):
    a, b = r.randint(10, 40), r.randint(10, 40)
    return N(f"A dual bar chart shows {a} boys and {b} girls chose swimming. How many students chose swimming altogether?", a + b, o="O5", fig={"kind": "barchart", "labels": ["Boys", "Girls"], "values": [a, b], "ymax": 45, "step": 5, "ylabel": "Swimming"})
def d6(r):
    v = [r.randint(3, 20) for _ in range(5)]
    return N("Using the bar chart, what is the total of all five bars?", sum(v), o="O5", fig={"kind": "barchart", "labels": ["A", "B", "C", "D", "E"], "values": v, "ymax": 22, "step": 2, "ylabel": "Frequency"})
def d7(r):
    return MS("Select ALL the charts that are suitable for categorical data (such as favourite fruit).", ["Bar chart", "Pie chart"], ["Time series graph", "Scatter graph"], o="O5", d="H")


s.std([d2, d3, d1, d4, d5, d6, d7], EX("Explain why a pie chart is not suitable for showing a town's temperature each month.", [("temperatures are not parts of a whole", ["parts of a whole|not a whole|don't add|do not add|share"]), ("a time series graph shows change over time better", ["time series|line graph|change over time"])], "A pie chart shows how a whole is shared, but monthly temperatures are not parts of one whole. A time series graph shows how the temperature changes over time.", o="O5"))

# ================================================================== 16.6
s = U.section("16.6", "Using statistics", ["O6"])
s.idea("Averages and range", ["**Mean** = total ÷ number of values. **Median** = middle value in order. **Mode** = most common. **Range** = largest − smallest.",
       "To compare two sets of data, compare an **average** (which is bigger?) and the **range** (which is more consistent?)."])
s.example("Comparing", "Team A: mean 24 points, range 6. Team B: mean 27 points, range 15. Compare them.", [("B scored more on average", "higher mean"), ("A was more consistent", "smaller range")], "B higher on average; A more consistent")
s.check(N("Find the mean of 4, 7, 8, 9 and 12.", 8, o="O6"))
s.check(MC("Before you read on: house prices in a street are $200k, $210k, $220k, $230k and $2m. Which average best describes a typical house?", "The median", [("The mean", "The $2m house pulls the mean far above most houses."), ("The range", "The range is a spread, not an average.")], o="O6"))
s.mistake("Outliers", ["One very large or small value changes the mean a lot but hardly changes the median."])


def u1(r):
    v = [r.randint(2, 30) for _ in range(r.randint(5, 8))]
    return N(f"Find the mean of {', '.join(map(str, v))}. Give your answer to 1 d.p. if needed.", round(sum(v) / len(v), 1), o="O6", tol=0.05, reason=f"{sum(v)} ÷ {len(v)} ≈ {round(sum(v) / len(v), 1)}.")
def u2(r):
    v = [r.randint(2, 50) for _ in range(r.choice([7, 9]))]
    return N(f"Find the median of {', '.join(map(str, v))}.", med(v), o="O6", reason=f"In order: {', '.join(map(str, sorted(v)))}.")
def u3(r):
    m = r.randint(10, 40); n = r.randint(4, 8); v = [r.randint(5, 50) for _ in range(n - 1)]; v.append(m * n - sum(v))
    if v[-1] <= 0: return None
    return N(f"The mean of {n} numbers is {m}. The first {n - 1} numbers are {', '.join(map(str, v[:-1]))}. Find the last number.", v[-1], o="O6", d="H", reason=f"Total = {m * n}; {m * n} − {sum(v[:-1])} = {v[-1]}.")
def u4(r):
    a, b = r.randint(20, 40), r.randint(20, 40); ra, rb = r.randint(3, 10), r.randint(12, 25)
    if a == b: return None
    return MC(f"Class A: mean {a}, range {ra}. Class B: mean {b}, range {rb}. Which statement is correct?", f"Class {'A' if a > b else 'B'} did better on average, and class A was more consistent", [f"Class {'B' if a > b else 'A'} did better on average", "Class B was more consistent", "Both classes did equally well"], o="O6", d="H")
def u5(r):
    v = [r.randint(2, 20) for _ in range(6)]
    return TB(f"Find the statistics for {', '.join(map(str, v))}.", ["Statistic", "Value"], [["Range", B(max(v) - min(v))], ["Median", B(med(v))], ["Mean (1 d.p.)", B(round(sum(v) / 6, 1), 0.05)]], o="O6", d="H")
def u6(r):
    v = [r.randint(10, 20) for _ in range(6)]; out = r.randint(80, 120)
    return MC(f"The data {', '.join(map(str, v))}, {out} includes one very large value. Which average best represents the data?", "the median", [("the mean", f"The value {out} pulls the mean up."), ("the range", "The range is not an average."), ("the total", "")], o="O6", d="H")
def u7(r):
    v = [r.randint(1, 9) for _ in range(9)]
    from collections import Counter
    c = Counter(v); m = max(c.values()); md = [k for k, x in c.items() if x == m]
    if len(md) > 1: return None
    return N(f"Find the mode of {', '.join(map(str, v))}.", md[0], o="O6")
def u8(r):
    f = [r.randint(1, 8) for _ in range(4)]; x = [0, 1, 2, 3]
    return N("The table shows the number of goals scored in matches. Find the mean number of goals per match, to 1 d.p.", round(sum(a * b for a, b in zip(x, f)) / sum(f), 1), "goals", units=["goals"], o="O6", d="H", tol=0.05, data={"head": ["Goals", *map(str, x)], "rows": [["Matches", *map(str, f)]]})


def n166(r):
    v = r.sample(range(2, 20), 5); m = sum(v) / 5
    return MC("Each value in a set is increased by 3. What happens to the mean and the range?", "The mean increases by 3; the range stays the same", [("Both increase by 3", "The gap between biggest and smallest does not change."), ("Neither changes", "Every value is bigger, so the mean is bigger.")], o="O6", d="H",
              reason="Adding the same amount shifts every value: the centre moves, the spread does not.")


s.std([u5, u8, u1, u2, u3, u4, u6, u7], EX("Explain why the median can be a better average than the mean.", [("the mean is affected by extreme values / outliers", ["extreme|outlier|very large|very small|affected"]), ("the median is the middle value so it is not pulled", ["middle|not affected|not pulled|isn't affected"])], "The mean uses every value, so one extreme value can pull it a long way. The median is the middle value, so it is hardly affected by an outlier.", o="O6"),
      deep=[n166])

U.mindmap(("Frequency diagrams", "Equal classes • bars touch • modal class", "O1", "16.1"), ("Time series", "Time across • describe the trend", "O2", "16.2"),
          ("Stem-and-leaf", "Ordered • key • median, mode, range", "O3", "16.3"), ("Pie charts", "Angle = f ÷ total × 360", "O4", "16.4"),
          ("Choosing a chart", "Match the chart to the data", "O5", "16.5"), ("Using statistics", "Mean, median, mode • range for consistency", "O6", "16.6"))
