# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 15 Interpreting and discussing results. Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(15, "Interpreting and discussing results", "Statistics and probability",
         "Frequency polygons, scatter graphs and correlation, back-to-back stem-and-leaf diagrams, statistics for grouped data and choosing good representations.",
         {"O1": {"sec": "15.1", "code": "9Ss.03", "codeNote": "", "t": "Draw and interpret frequency polygons, including comparing two distributions."},
          "O2": {"sec": "15.2", "code": "9Ss.04", "codeNote": "", "t": "Draw and interpret scatter graphs, describe correlation and use a line of best fit."},
          "O3": {"sec": "15.3", "code": "9Ss.05", "codeNote": "", "t": "Use back-to-back stem-and-leaf diagrams to compare two sets of data (median and range)."},
          "O4": {"sec": "15.4", "code": "9Ss.06", "codeNote": "", "t": "Estimate the mean, and find the modal class and the class containing the median, for grouped data."},
          "O5": {"sec": "15.5", "code": "9Ss.07", "codeNote": "", "t": "Choose and criticise representations of data, and draw conclusions from them."}})

def classes(r, lo, w, k):
    return [(lo + i * w, lo + (i + 1) * w) for i in range(k)]
def gtab(cl, f, unit=""):
    return {"head": [f"Class{(' (' + unit + ')') if unit else ''}", "Frequency"], "rows": [[f"{a} ≤ x < {b}", str(n)] for (a, b), n in zip(cl, f)]}
def est_mean(cl, f): return sum((a + b) / 2 * n for (a, b), n in zip(cl, f)) / sum(f)
def med_class(cl, f):
    n = sum(f); pos = (n + 1) / 2; c = 0
    for (a, b), k in zip(cl, f):
        c += k
        if c >= pos: return f"{a} ≤ x < {b}"

# ================================================================== 15.1
s = U.section("15.1", "Frequency polygons", ["O1"])
s.idea("Frequency polygons", ["For grouped data, plot each frequency at the **midpoint** of its class, then join the points with **straight lines**.",
       "Two polygons on the same axes make it easy to **compare** distributions."],
       fig={"kind": "linegraph", "x": {"min": 0, "max": 50, "step": 10, "label": "Time (minutes)"}, "y": {"min": 0, "max": 16, "step": 4, "label": "Frequency"}, "series": [{"pts": [[5, 3], [15, 9], [25, 14], [35, 8], [45, 2]]}]})
s.example("Midpoints", "Which x-value is used for the class 20 ≤ t < 30?", [("(20 + 30) ÷ 2 = 25", "")], "25")
s.check(N("In the lesson graph, how many people took 10 to 20 minutes?", 9, "people", units=["people"], reason="Read the point plotted at the midpoint 15: frequency 9.", o="O1"))
s.mistake("Not at the class boundary", ["Plot at the MIDPOINT of each class, not at the start or the end."])
s.check(N("In the lesson graph, how many people were surveyed altogether?", 36, "people", units=["people"], reason="Add the frequencies: 3 + 9 + 14 + 8 + 2 = 36.", o="O1"))
def f1(r):
    lo, w = pick(r, [(0, 10), (10, 5), (20, 10), (100, 20), (0, 4)]); cl = classes(r, lo, w, 5); i = r.randrange(5)
    return N(f"A frequency polygon is drawn for classes of width {w} starting at {lo}. At what x-value is the frequency for the class {cl[i][0]} ≤ x < {cl[i][1]} plotted?", (cl[i][0] + cl[i][1]) / 2, reason=f"Plot at the midpoint: ({cl[i][0]} + {cl[i][1]}) ÷ 2 = {fmt((cl[i][0] + cl[i][1]) / 2)}.", o="O1")
def f2(r):
    cl = classes(r, 0, 10, 5); f = [r.randint(1, 15) for _ in cl]
    return GR("Plot the frequency polygon for this data (plot at the midpoints).", {"label": "Mass (kg)", "min": 0, "max": 50, "step": 5}, {"label": "Frequency", "min": 0, "max": 16, "step": 2}, [[(a + b) / 2, n] for (a, b), n in zip(cl, f)], o="O1", data=gtab(cl, f, "kg"))
def f3(r):
    f = [r.randint(1, 15) for _ in range(5)]; pts = [[5 + 10 * i, f[i]] for i in range(5)]; q = r.randrange(2)
    fig = {"kind": "linegraph", "x": {"min": 0, "max": 50, "step": 10, "label": "Score"}, "y": {"min": 0, "max": 16, "step": 2, "label": "Frequency"}, "series": [{"pts": pts}]}
    if q: return N("How many results are shown in the frequency polygon altogether?", sum(f), reason=f"Add the frequencies: {' + '.join(map(str, f))} = {sum(f)}.", o="O1", fig=fig)
    m = max(f)
    if f.count(m) > 1: return None
    i = f.index(m)
    return MC("Which is the modal class?", f"{10*i} ≤ x < {10*i+10}", [(f"{10*j} ≤ x < {10*j+10}", "") for j in range(5) if j != i][:3], o="O1", fig=fig)
def f4(r):
    base = [2, 6, 12, 6, 2, 1, 1]
    sa = r.randint(0, 1); sb = sa + r.randint(1, 2)
    fa = [max(1, base[(i - sa) % 7] + r.randint(-1, 1)) if 0 <= i - sa < 5 else 1 for i in range(5)]
    fb = [max(1, base[(i - sb) % 7] + r.randint(-1, 1)) if 0 <= i - sb < 5 else 1 for i in range(5)]
    hiB = r.random() < 0.5
    A_, B_ = (fa, fb) if hiB else (fb, fa)
    ans = "Class B generally scored higher" if hiB else "Class A generally scored higher"
    other = "Class A generally scored higher" if hiB else "Class B generally scored higher"
    return MC("The two frequency polygons show test scores for classes A and B. Which statement is best supported?", ans, [(other, "Look at which polygon is further to the right (higher scores)."), ("The classes did equally well", ""), ("The two classes had very different numbers of students", "")], o="O1", d="H",
              fig={"kind": "linegraph", "x": {"min": 0, "max": 50, "step": 10, "label": "Score"}, "y": {"min": 0, "max": 14, "step": 2, "label": "Frequency"}, "series": [{"pts": [[5 + 10 * i, A_[i]] for i in range(5)], "label": "A"}, {"pts": [[5 + 10 * i, B_[i]] for i in range(5)], "label": "B", "dash": True}]})
s.core(f1(s.rng), f2(s.rng), f3(s.rng) or f3(s.rng) or f3(s.rng), f4(s.rng), f1(s.rng), f2(s.rng),
       MC("Why are the points on a frequency polygon joined with straight lines?", "to show the overall shape of the distribution", [("because the data is exact", ""), ("to show the mean", ""), ("because every value lies on the line", "Values between midpoints are not known.")], o="O1"),
       EX("Explain why frequency polygons are useful for comparing two sets of grouped data.", [("both can be drawn on the same axes", ["same axes|same graph|same grid|together|overlap"]), ("easy to compare shape / which is higher", ["compare|shape|higher|spread|shift"])], "Two polygons can be drawn on the same axes without hiding each other, so you can easily compare their shapes and see which has higher values.", o="O1"))
s.gen("p", 44, f1, f2, f3, f4)
s.gen("a", 8, f4, lambda r: (lambda f: N("Estimate the mean from the frequency polygon (1 d.p.).", round(sum((5 + 10 * i) * f[i] for i in range(5)) / sum(f), 1), tol=0.06, reason=f"Σ(midpoint × frequency) ÷ Σfrequency = {sum((5 + 10 * i) * f[i] for i in range(5))} ÷ {sum(f)} = {round(sum((5 + 10 * i) * f[i] for i in range(5)) / sum(f), 1)}.", o="O1", d="VH",
       fig={"kind": "linegraph", "x": {"min": 0, "max": 50, "step": 10, "label": "Score"}, "y": {"min": 0, "max": 16, "step": 2, "label": "Frequency"}, "series": [{"pts": [[5 + 10 * i, f[i]] for i in range(5)]}]}))([r.randint(1, 15) for _ in range(5)]))

# ================================================================== 15.2
s = U.section("15.2", "Scatter graphs", ["O2"])
s.idea("Correlation", ["A **scatter graph** plots pairs of values. **Positive correlation**: as one increases, so does the other. **Negative**: as one increases, the other decreases. **No correlation**: no pattern.",
       "A **line of best fit** follows the trend with about as many points above as below. Use it to **estimate** values – but only inside the data range (not far outside)."],
       fig={"kind": "linegraph", "x": {"min": 0, "max": 10, "step": 2, "label": "Hours of revision"}, "y": {"min": 0, "max": 100, "step": 20, "label": "Test mark"}, "series": [{"pts": [[1, 30], [2, 38], [3, 45], [4, 52], [5, 50], [6, 63], [7, 70], [8, 72], [9, 85]], "line": False}, {"pts": [[0, 24], [10, 89]], "dots": False, "dash": True}]})
s.check(MC("What type of correlation does the lesson graph show?", "positive", [("negative", ""), ("none", "")], o="O2"))
s.idea("Correlation is not causation", ["A scatter graph may show that ice-cream sales and sunburn cases rise together (positive correlation). That does not mean ice cream causes sunburn: hot weather causes both.",
       "Describe the pattern, then think about whether a third factor could explain it."])
s.mistake("Correlation is not cause", ["Ice-cream sales and sunburn are positively correlated, but ice cream does not cause sunburn – hot weather causes both."])
s.check(N("Use the line of best fit in the lesson graph to estimate the mark for 5 hours of revision (to the nearest 5).", 55, "marks", units=["marks"], tol=4, reason="Go up from 5 hours to the line, then across: about 55 marks.", o="O2"))
def sc1(r):
    t = r.randrange(3); pts = []
    for x in range(1, 10):
        y = 50 + (6 * x - 30) * (1 if t == 0 else -1 if t == 1 else 0) + (r.randint(-8, 8) if t < 2 else r.randint(-35, 35))
        pts.append([x, max(2, min(98, y))])
    ans = ["positive", "negative", "no correlation"][t]
    return MC("Describe the correlation shown.", ans, [(a, "") for a in ["positive", "negative", "no correlation"] if a != ans], o="O2",
              fig={"kind": "linegraph", "x": {"min": 0, "max": 10, "step": 2, "label": "x"}, "y": {"min": 0, "max": 100, "step": 20, "label": "y"}, "series": [{"pts": pts, "line": False}]})
def sc2(r):
    rows = [("Age of a car and its value", "Negative"), ("Height and arm span", "Positive"), ("Shoe size and test score", "No correlation"), ("Temperature and hot drinks sold", "Negative"),
            ("Hours of sunshine and ice creams sold", "Positive"), ("House number and age of owner", "No correlation"), ("Distance travelled and fuel left", "Negative")]
    return GD("What correlation would you expect?", "Correlation", r.sample(rows, 4), o="O2", extra=["Positive", "Negative", "No correlation"])
def sc3(r):
    m, c = r.choice([4, 5, 6, 7, 8]), r.randint(5, 30); x = r.randint(2, 8)
    return N(f"The line of best fit through a scatter graph has equation y = {m}x + {c}. Estimate y when x = {x}.", m * x + c, reason=f"y = {m} × {x} + {c} = {m * x + c}.", o="O2", d="H")
def sc4(r):
    x = r.randint(25, 60)
    return MC(f"A line of best fit was drawn for children aged 2 to 12, plotting age against height. Why is it not sensible to use it to estimate the height of someone aged {x}?", "it is far outside the range of the data", [("the line is not straight", ""), ("there is negative correlation", ""), ("adults have no height", "")], o="O2", d="H")
def sc5(r):
    pts = [[x, 20 + 7 * x + r.randint(-6, 6)] for x in range(1, 10)]; out = r.randint(2, 8); pts[out - 1][1] = 20 + 7 * out + pick(r, [-40, 40])
    return TB("One point does not fit the trend (an outlier). Give its coordinates.", ["x", "y"], [[B(pts[out - 1][0]), B(pts[out - 1][1])]], reason=f"The y-values rise by about 7 each time; at x = {pts[out - 1][0]} the value {pts[out - 1][1]} is far from the trend.", o="O2", d="H",
              data={"head": ["x"] + [str(p[0]) for p in pts], "rows": [["y"] + [str(p[1]) for p in pts]]})
def sc6(r):
    pts = [[x, 90 - 8 * x + r.randint(-5, 5)] for x in range(1, 9)]
    return GR("Plot these points on the scatter graph.", {"label": "x", "min": 0, "max": 9, "step": 1}, {"label": "y", "min": 0, "max": 100, "step": 10}, [list(p) for p in pts[:5]], o="O2", d="M",
              data={"head": ["x"] + [str(p[0]) for p in pts[:5]], "rows": [["y"] + [str(p[1]) for p in pts[:5]]]})
s.core(sc1(s.rng), sc2(s.rng), sc3(s.rng), sc4(s.rng), sc5(s.rng), sc1(s.rng), sc6(s.rng),
       EX("A scatter graph shows strong positive correlation between ice-cream sales and drownings. Explain why this does not mean ice cream causes drowning.", [("correlation does not show cause", ["correlation|does not mean|not cause|doesn't cause"]), ("another factor, e.g. hot weather, causes both", ["weather|hot|summer|sun|third|other factor|both"])], "Correlation does not prove cause. Hot weather makes more people buy ice cream and more people swim, so both increase together.", o="O2"))
def o2_1(r):
    rows = r.sample([("height and shoe size", "Positive"), ("age of a car and its value", "Negative"), ("shoe size and maths score", "None"), ("hours of revision and test score", "Positive")], 4)
    return GD("What type of correlation would you expect?", "Correlation", rows, o="O2", d="H", extra=["Positive", "Negative", "None"], reason="Ask: as one goes up, does the other tend to go up, go down, or show no pattern?")


s.gen("p", 44, sc1, sc2, sc3, sc4, sc5, sc6)
s.capped("p", [1] * 1, [o2_1]).capped("m", [2] * 1, [o2_1])   # v2 reasoning kinds
s.gen("a", 8, sc5, sc3, lambda r: (lambda a, b: N(f"A line of best fit passes through ({a}, {10*a+5}) and ({b}, {10*b+5}). Use it to estimate x when y = {10*(a+b)//2*1 + 5}.", (a + b) / 2, reason=f"The line is y = 10x + 5, so x = ({5 * (a + b) + 5} − 5) ÷ 10 = {fmt((a + b) / 2)}.", o="O2", d="VH", tol=0.01))(r.randint(1, 4), r.randint(6, 10)))

# ================================================================== 15.3
s = U.section("15.3", "Back-to-back stem-and-leaf diagrams", ["O3"])
s.idea("Back-to-back", ["Two sets of data share the **same stems**. Leaves for one set go to the **left** (read right to left), the other set to the **right**.",
       "Compare using an **average** (median) and a **measure of spread** (range)."],
       fig={"kind": "stemleaf", "stems": [1, 2, 3, 4], "left": [[5, 8], [2, 4, 7], [1, 6, 9], [3]], "right": [[9], [5, 6], [0, 2, 4, 8], [1, 5]], "titles": ["Boys", "Girls"], "key": "Key: 5 | 2 | 6 means 25 for boys and 26 for girls"})
s.example("Reading the left side", "In the lesson diagram, what are the boys' values in the 20s?", [("leaves 2, 4, 7, reading outwards from the stem", "")], "22, 24, 27")
s.check(N("What is the range of the girls' values in the lesson diagram?", 26, reason="Largest 45 − smallest 19 = 26.", o="O3"))
s.mistake("Read the key", ["On the left side, 5 | 2 means 25, not 52."])
s.check(N("What is the median of the girls' values in the lesson diagram?", 32, reason="9 values: 19, 25, 26, 30, 32, 34, 38, 41, 45. The 5th is 32.", o="O3", d="H"))
def sl_data(r, n):
    vals = sorted(r.sample(range(10, 60), n)); return vals
def sl_fig(L, R, titles):
    st = sorted({v // 10 for v in L + R}); st = list(range(st[0], st[-1] + 1))
    return {"kind": "stemleaf", "stems": st, "left": [sorted([v % 10 for v in L if v // 10 == s_]) for s_ in st], "right": [sorted([v % 10 for v in R if v // 10 == s_]) for s_ in st], "titles": titles, "key": f"Key: 3 | 2 | 5 means 23 for {titles[0]} and 25 for {titles[1]}"}
def med(v): v = sorted(v); n = len(v); return v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2
def sl1(r):
    L, R = sl_data(r, pick(r, [7, 9, 11])), sl_data(r, pick(r, [7, 9, 11])); side, which = r.randrange(2), r.randrange(2)
    T = pick(r, [("Team A", "Team B"), ("Year 8", "Year 9"), ("Morning", "Afternoon")])
    v = (L, R)[side]
    return N(f"Find the {'median' if which else 'range'} for {T[side]}.", med(v) if which else max(v) - min(v), reason=f"{T[side]} in order: {', '.join(map(str, sorted(v)))}. " + (f"Median = {fmt(med(v))}." if which else f"Range = {max(v)} − {min(v)} = {max(v) - min(v)}."), o="O3", d="H" if side == 0 else "M", fig=sl_fig(L, R, T))
def sl2(r):
    L, R = sl_data(r, 9), sl_data(r, 9); T = ("Class P", "Class Q")
    mL, mR = med(L), med(R)
    if mL == mR: return None
    hi = T[0] if mL > mR else T[1]
    return MC("Which class has the higher median?", hi, [(T[1] if hi == T[0] else T[0], f"Medians: P = {fmt(mL)}, Q = {fmt(mR)}."), ("They are the same", "")], o="O3", fig=sl_fig(L, R, T))
def sl3(r):
    L, R = sl_data(r, 9), sl_data(r, 9); T = ("Shop X", "Shop Y")
    rL, rR = max(L) - min(L), max(R) - min(R)
    if rL == rR: return None
    c = T[0] if rL < rR else T[1]
    return MC("Which shop's values are more consistent?", c, [(T[1] if c == T[0] else T[0], f"Ranges: X = {rL}, Y = {rR}. Smaller range = more consistent."), ("Both the same", "")], o="O3", d="H", fig=sl_fig(L, R, T))
def sl4(r):
    L, R = sl_data(r, 9), sl_data(r, 9); T = ("Left", "Right")
    return TB("Complete the table for the two sets of data.", ["Median (left)", "Range (left)", "Median (right)", "Range (right)"], [[B(med(L)), B(max(L) - min(L)), B(med(R)), B(max(R) - min(R))]], reason=f"Left: median {fmt(med(L))}, range {max(L)} − {min(L)} = {max(L) - min(L)}. Right: median {fmt(med(R))}, range {max(R)} − {min(R)} = {max(R) - min(R)}.", o="O3", d="H", fig=sl_fig(L, R, T))
s.core(sl1(s.rng), sl2(s.rng) or sl2(s.rng) or sl2(s.rng), sl3(s.rng) or sl3(s.rng) or sl3(s.rng), sl4(s.rng), sl1(s.rng), sl1(s.rng),
       MC("Why are the left-hand leaves written in reverse order?", "so values increase moving away from the stem on both sides", [("to make the diagram look symmetrical", ""), ("because the left-hand data is smaller", ""), ("there is no reason", "")], o="O3"),
       EX("Explain how to compare two sets of data using a back-to-back stem-and-leaf diagram.", [("compare the medians (averages)", ["median|average|mean"]), ("compare the ranges (spread / consistency)", ["range|spread|consisten"])], "Find the median of each set to compare the averages, and the range of each set to compare the spread (consistency).", o="O3"))
s.gen("p", 44, sl1, sl2, sl3, sl4)
s.gen("a", 8, sl4, sl3, lambda r: (lambda L: N(f"A set of 9 values has median 34 and range 30. One new value of {max(L)+10} is added. By how much does the range increase?", 10, o="O3", d="VH"))(sl_data(r, 9)) if False else sl1(r))

# ================================================================== 15.4
s = U.section("15.4", "Statistics for grouped data", ["O4"])
s.idea("Estimating the mean", ["For grouped data you do not know exact values, so use the **midpoint** of each class.",
       "**Estimated mean = Σ(midpoint × frequency) ÷ Σ frequency.** The **modal class** has the highest frequency. The **median** is the ((n + 1)/2)th value: find which class it falls in."],
       table={"caption": "Times (minutes)", "head": ["Class", "Frequency", "Midpoint", "Midpoint × f"], "rows": [["0 ≤ t < 10", "4", "5", "20"], ["10 ≤ t < 20", "9", "15", "135"], ["20 ≤ t < 30", "7", "25", "175"], ["Total", "20", "", "330"]]})
s.example("Estimated mean", "Estimate the mean of the data in the table.", [("Σ(midpoint × f) = 330", ""), ("Σf = 20", ""), ("330 ÷ 20 = 16.5", "")], "16.5 minutes")
s.check(MC("Which class contains the median of the table data?", "10 ≤ t < 20", [("0 ≤ t < 10", ""), ("20 ≤ t < 30", "")], o="O4"))
s.idea("Why the mean from grouped data is an estimate", ["In grouped data you do not know the exact values, only the class. Using the midpoint of each class assumes the values in it average to the middle.",
       "Estimated mean = Σ(midpoint × frequency) ÷ Σ frequency."])
s.mistake("An estimate", ["It is only an ESTIMATE of the mean because the exact values in each class are unknown."])
s.check(N("Estimate the mean of: 0 ≤ x < 4 (frequency 3), 4 ≤ x < 8 (frequency 5).", 4.5, reason="(2 × 3 + 6 × 5) ÷ 8 = 36 ÷ 8 = 4.5.", o="O4", d="H"))
def gd1(r):
    lo, w = pick(r, [(0, 10), (10, 10), (0, 5), (100, 20), (20, 4)]); cl = classes(r, lo, w, pick(r, [4, 5])); f = [r.randint(1, 15) for _ in cl]
    return N("Estimate the mean (1 d.p.).", round(est_mean(cl, f), 1), tol=0.06, reason=f"Σ(midpoint × f) = {fmt(sum((a + b) / 2 * n for (a, b), n in zip(cl, f)))}; Σf = {sum(f)}; mean ≈ {round(est_mean(cl, f), 1)}.", o="O4", d="H", data=gtab(cl, f))
def gd2(r):
    cl = classes(r, 0, 10, 5); f = [r.randint(1, 15) for _ in cl]; m = max(f)
    if f.count(m) > 1: return None
    i = f.index(m); ans = f"{cl[i][0]} ≤ x < {cl[i][1]}"
    return MC("Which is the modal class?", ans, [(f"{a} ≤ x < {b}", "") for (a, b) in cl if f"{a} ≤ x < {b}" != ans][:3], o="O4", data=gtab(cl, f))
def gd3(r):
    cl = classes(r, 0, 10, 5); f = [r.randint(1, 15) for _ in cl]
    if sum(f) % 2 == 0: f[0] += 1
    ans = med_class(cl, f)
    return MC("Which class contains the median?", ans, [(f"{a} ≤ x < {b}", "") for (a, b) in cl if f"{a} ≤ x < {b}" != ans][:3], o="O4", d="H", data=gtab(cl, f))
def gd4(r):
    cl = classes(r, 0, 20, 4); f = [r.randint(2, 12) for _ in cl]
    return TB("Complete the midpoint × frequency column.", [f"{a}–{b}" for a, b in cl], [[B((a + b) / 2 * n) for (a, b), n in zip(cl, f)]], reason=f"Multiply each midpoint by its frequency, e.g. {fmt((cl[0][0] + cl[0][1]) / 2)} × {f[0]} = {fmt((cl[0][0] + cl[0][1]) / 2 * f[0])}.", o="O4", data=gtab(cl, f))
def gd5(r):
    cl = classes(r, 0, 10, 4); f = [r.randint(2, 12) for _ in cl]
    return N("What is the largest possible range of this data?", cl[-1][1] - cl[0][0], o="O4", d="H", data=gtab(cl, f), reason="Largest possible value minus smallest possible value.")
s.core(gd1(s.rng), gd2(s.rng) or gd2(s.rng) or gd2(s.rng), gd3(s.rng), gd4(s.rng), gd5(s.rng), gd1(s.rng),
       MC("Why is the mean from grouped data only an estimate?", "the exact values in each class are not known", [("the frequencies are estimates", ""), ("the midpoints are always wrong", ""), ("there are too many classes", "")], o="O4"),
       EX("Explain why the midpoint is used for each class when estimating the mean.", [("exact values unknown", ["unknown|not know|don't know|exact"]), ("midpoint is a typical / middle value of the class", ["middle|typical|average|represent|halfway"])], "We do not know the exact values in each class, so the midpoint is used as a typical value for every item in that class.", o="O4"))
def o4_1(r):
    return MC("Why is the mean from a grouped frequency table only an estimate?", "The exact values in each class are not known, so midpoints are used", [("Because the frequencies are rounded", "The frequencies are exact counts."), ("Because the classes overlap", "Classes should not overlap.")], o="O4", d="H", reason="Midpoints stand in for the unknown values.")


s.gen("p", 44, gd1, gd2, gd3, gd4, gd5)
s.capped("p", [1] * 1, [o4_1]).capped("m", [2] * 1, [o4_1])   # v2 reasoning kinds
s.gen("a", 8, gd1, gd3, lambda r: (lambda f, x: N(f"The estimated mean of this grouped data is {fmt(round(est_mean(classes(r,0,10,3), f + [x]) if False else (5*f[0]+15*f[1]+25*x)/(f[0]+f[1]+x), 3))}. Find the missing frequency x.", x, tol=0.05, o="O4", d="VH", data={"head": ["Class", "Frequency"], "rows": [["0 ≤ x < 10", str(f[0])], ["10 ≤ x < 20", str(f[1])], ["20 ≤ x < 30", "x"]]}))([r.randint(2, 9), r.randint(2, 9)], r.randint(2, 12)))

# ================================================================== 15.5
s = U.section("15.5", "Representing data", ["O5"])
s.idea("Choosing a chart", ["**Bar chart**: categories. **Pie chart**: parts of a whole. **Line graph**: change over time. **Scatter graph**: relationship between two variables. **Frequency polygon / stem-and-leaf**: distributions.",
       "Watch for **misleading** graphs: axes not starting at 0, uneven scales, 3D effects, missing labels."])
s.check(MC("Which chart best shows how a town's population changed from 2000 to 2025?", "a line graph", [("a pie chart", "Pie charts show parts of a whole."), ("a scatter graph", ""), ("a stem-and-leaf diagram", "")], o="O5"))
s.idea("Pie charts", ["Each item is **360° ÷ total**. Angle = frequency × (360 ÷ total)."])
s.mistake("Compare totals", ["A bigger sector in one pie chart does not mean a bigger number if the two pie charts have different totals."])
s.check(N("A pie chart shows 60 students. How many degrees represent one student?", 6, "°", units=["°"], reason="360 ÷ 60 = 6°.", o="O5"))
def rp1(r):
    rows = [("Favourite colours of a class", "Bar chart"), ("Temperature each hour of a day", "Line graph"), ("How a family's spending is split", "Pie chart"),
            ("Height against mass for 30 students", "Scatter graph"), ("Comparing test marks of two classes", "Back-to-back stem-and-leaf")]
    return GD("Choose the best representation for each.", "Chart", r.sample(rows, 4), o="O5", extra=["Bar chart", "Line graph", "Pie chart", "Scatter graph", "Back-to-back stem-and-leaf"])
def rp2(r):
    tot = pick(r, [24, 30, 36, 40, 45, 60, 72, 90, 120]); f = r.randint(2, tot // 3)
    return N(f"{f} out of {tot} people chose swimming. Find the angle for swimming in a pie chart.", f * 360 / tot, "°", units=["°"], reason=f"{f} ÷ {tot} × 360 = {fmt(f * 360 / tot)}°.", o="O5", tol=0.06)
def rp3(r):
    tot = pick(r, [40, 60, 80, 120, 180, 240]); ang = pick(r, [30, 45, 60, 72, 90, 120, 135])
    return N(f"A pie chart shows {tot} people. The sector for 'bus' is {ang}°. How many people chose bus?", round(tot * ang / 360, 2), "people", units=["people"], reason=f"{ang} ÷ 360 × {tot} = {fmt(round(tot * ang / 360, 2))}.", o="O5", tol=0.01)
def rp4(r):
    a, b = r.randint(41, 49), r.randint(50, 58)
    return MC(f"A bar chart has a vertical axis starting at 40. Bar A shows {a} and bar B shows {b}, and B looks {round((b-40)/(a-40))} times as tall as A. What is wrong?", "the axis does not start at 0, so differences look bigger", [("nothing is wrong", ""), ("the bars should touch", ""), ("the bars should be different colours", "")], o="O5", d="H") if round((b - 40) / (a - 40)) > 1 else None
def rp5(r):
    n1, n2 = pick(r, [(40, 120), (60, 200), (50, 150), (30, 90)]); a1, a2 = pick(r, [(90, 45), (120, 60), (72, 36), (180, 90)])
    return MC(f"School P (total {n1} students) and School Q (total {n2} students) each have a pie chart. P's 'walk' sector is {a1}° and Q's is {a2}°. Which school has MORE students who walk?", "School Q" if n2 * a2 > n1 * a1 else "School P", [("School P" if n2 * a2 > n1 * a1 else "School Q", f"P: {n1} × {a1}/360 = {fmt(n1*a1/360)}; Q: {n2} × {a2}/360 = {fmt(n2*a2/360)}."), ("You cannot tell", "")], o="O5", d="H")
def rp6(r):
    v = [r.randint(5, 40) for _ in range(4)]; d0 = r.randint(0, 1); lab = ["Mon", "Tue", "Wed", "Thu", "Fri"][d0:d0 + 4]
    i = r.randrange(4)
    return N(f"Read the bar chart. How many more were sold on {lab[i]} than on the day with the fewest sales?", v[i] - min(v), reason=f"{lab[i]}: {v[i]}; fewest: {min(v)}; difference {v[i] - min(v)}.", o="O5", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 40, "step": 5, "ylabel": "Number sold"})
s.core(rp1(s.rng), rp2(s.rng), rp3(s.rng), rp4(s.rng) or rp4(s.rng) or rp4(s.rng), rp5(s.rng), rp6(s.rng),
       MS("Which features can make a graph misleading?", ["a vertical axis that does not start at 0", "uneven scales on an axis", "3D effects that distort sizes"], ["a title", "labelled axes"], o="O5", d="H"),
       EX("Explain why a pie chart is not a good choice to show a town's population each year from 2000 to 2025.", [("pie charts show parts of a whole", ["part|whole|proportion|share|fraction"]), ("a line graph shows change over time", ["line graph|over time|change|trend"])], "A pie chart shows how a whole is split into parts. To show change over time, a line graph is better.", o="O5"))
s.gen("p", 44, rp1, rp2, rp3, rp4, rp5, rp6)
s.gen("a", 8, rp5, rp4, lambda r: (lambda t, a: N(f"In a pie chart of {t} people, the 'cycle' sector is {a}° and 'car' is 3 times as many people. Find the angle for car.", 3 * a, "°", units=["°"], reason=f"3 times as many people means 3 times the angle: 3 × {a} = {3 * a}°.", o="O5", d="VH") if 3 * a < 360 else None)(pick(r, [60, 90, 120]), pick(r, [24, 30, 36, 40, 45, 60, 72, 80, 90, 100])))

U.mindmap(("Frequency polygons", "Plot at midpoints • compare on one set of axes", "O1", "15.1"), ("Scatter graphs", "Correlation • line of best fit • not cause", "O2", "15.2"),
          ("Back-to-back stem-and-leaf", "Median and range • read the key", "O3", "15.3"), ("Grouped data", "Estimated mean • modal class • median class", "O4", "15.4"),
          ("Representing data", "Choose the right chart • spot misleading graphs", "O5", "15.5"))
