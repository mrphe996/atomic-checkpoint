# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 11 Graphs (11.1 Functions, 11.2 Graphs of functions, 11.3 Lines parallel to the axes,
11.4 Interpreting graphs). Written by the Atomic teaching team."""
from kit import *

U = Unit(11, "Graphs", "Algebra",
         "Functions written as equations, tables of values, plotting straight-line graphs, lines parallel to the axes and reading real-life graphs.",
         {"O1": {"code": "7Ae.07", "sec": "11.1", "codeNote": "", "t": "Understand a function as a rule linking an input and an output, written in words or as an equation."},
          "O2": {"code": "7Ae.08", "sec": "11.2", "codeNote": "", "t": "Complete a table of values and plot the graph of a linear function."},
          "O3": {"code": "7Ae.09", "sec": "11.3", "codeNote": "", "t": "Recognise and draw lines parallel to the axes, such as x = 3 and y = −2."},
          "O4": {"code": "7Ae.10", "sec": "11.4", "codeNote": "", "t": "Read and interpret graphs of real-life situations, including conversion graphs."}})
eq = lambda m, c: f"y = {'' if m == 1 else m}x" + (f" + {c}" if c > 0 else f" − {-c}" if c < 0 else "")
PACC = lambda p: [f"({p[0]}, {p[1]})", f"({p[0]},{p[1]})", f"{p[0]}, {p[1]}", f"{p[0]},{p[1]}"]

# ================================================================== 11.1
s = U.section("11.1", "Functions", ["O1"])
s.idea("Rules", ["A **function** turns every input into one output. 'Multiply by 2 then add 1' can be written as an equation: **y = 2x + 1**, where x is the input and y is the output."])
s.check(N("For y = 3x + 2, find y when x = 4.", 14, o="O1"))
s.mistake("Order", ["In y = 2x + 1, multiply first, then add."])


def f1(r):
    m, c, x = r.randint(2, 6), r.randint(-5, 10), r.randint(0, 10)
    return N(f"For {eq(m, c)}, find y when x = {x}.", m * x + c, o="O1")
def f2(r):
    m, c, x = r.randint(2, 6), r.randint(0, 10), r.randint(1, 10)
    return N(f"For {eq(m, c)}, find x when y = {m * x + c}.", x, o="O1", d="H")
def f3(r):
    m, c = r.randint(2, 5), r.randint(1, 9)
    return X(f"Write the rule 'multiply by {m}, then add {c}' as an equation for y.", f"{m}x+{c}", vars="xy", lhs="y", o="O1")
def f4(r):
    m, c = r.randint(2, 5), r.randint(0, 6); xs = r.sample(range(0, 8), 3)
    return MC("Which equation fits the table?", eq(m, c), [eq(m + 1, c), eq(m, c + 2), eq(c if c > 1 else m + 2, m)], o="O1", data={"head": ["x", *map(str, sorted(xs))], "rows": [["y", *[str(m * x + c) for x in sorted(xs)]]]})
def f5(r):
    m, c = r.randint(2, 5), r.randint(1, 9)
    return TB(f"Complete the table for {eq(m, c)}.", ["x", "y"], [[str(x), B(m * x + c)] for x in (0, 1, 2, 3)], o="O1")
def f6(r):
    m, c = r.randint(2, 5), r.randint(0, 6)
    return MS(f"Select ALL the input–output pairs that fit {eq(m, c)}.", [f"x = 1 → y = {m + c}", f"x = 3 → y = {3 * m + c}"], [f"x = 2 → y = {2 * m + c + 1}", f"x = 0 → y = {m}"] if m != c else [f"x = 2 → y = {2 * m + c + 1}"], o="O1")
def f7(r):
    k = r.randint(2, 9)
    return N(f"A shop charges ${k} per notebook. Use y = {k}x to find the cost of 7 notebooks.", 7 * k, "$", units=["$"], o="O1")


s.std([f4, f5, f1, f2, f3, f6, f7], EX("Explain what the equation y = 4x − 3 tells you to do with an input.", [("multiply the input by 4", ["multiply by 4|× ?4|times 4"]), ("then subtract 3", ["subtract 3|− ?3|- ?3|take away 3"])], "Multiply the input x by 4, then subtract 3, to get the output y.", o="O1"))

# ================================================================== 11.2
s = U.section("11.2", "Graphs of functions", ["O2"])
s.idea("Plotting", ["Make a **table of values**, then plot each pair (x, y) as a point. For a linear function the points lie on a **straight line**: join them with a ruler."], fig={"kind": "coord", "x": [-1, 5], "y": [-1, 10], "lines": [{"m": 2, "c": 1, "label": "y = 2x + 1"}], "points": [{"x": 0, "y": 1}, {"x": 1, "y": 3}, {"x": 2, "y": 5}, {"x": 3, "y": 7}]})
s.check(MC("Does the point (2, 5) lie on y = 2x + 1?", "Yes", ["No", "Only if x is negative"], o="O2"))
s.mistake("x first", ["Coordinates are written (x, y): across first, then up."])


def g1(r):
    m, c = r.randint(1, 3), r.randint(0, 4); x = r.randint(0, 4)
    return N(f"Use the graph of {eq(m, c)} to find y when x = {x}.", m * x + c, o="O2", fig={"kind": "coord", "x": [-1, 6], "y": [-1, 3 * 6 + 4], "lines": [{"m": m, "c": c, "label": eq(m, c)}]})
def g2(r):
    m, c = r.randint(1, 4), r.randint(0, 5); x = r.randint(0, 6)
    good = r.random() < 0.5; y = m * x + c + (0 if good else pick(r, [1, -1, 2]))
    return MC(f"Does the point ({x}, {y}) lie on {eq(m, c)}?", "Yes" if good else "No", ["No" if good else "Yes", "Cannot tell"], o="O2")
def g3(r):
    m, c = r.randint(1, 3), r.randint(0, 3)
    return S(f"Write the coordinates of the point where {eq(m, c)} crosses the y-axis.", PACC((0, c)), o="O2", fig={"kind": "coord", "x": [-1, 5], "y": [-1, 15], "lines": [{"m": m, "c": c}]})
def g4(r):
    m, c = r.randint(1, 4), r.randint(-3, 5)
    return TB(f"Complete the table of values for {eq(m, c)}, ready to plot.", ["x", "y"], [[str(x), B(m * x + c)] for x in (-1, 0, 1, 2)], o="O2")
def g5(r):
    m, c = r.randint(1, 3), r.randint(0, 4); x = r.randint(0, 5)
    return S(f"Write the coordinates of the point on {eq(m, c)} where x = {x}.", PACC((x, m * x + c)), o="O2")
def g6(r):
    rows = [("(2, 7)", "On y = 3x + 1"), ("(1, 4)", "On y = 3x + 1"), ("(3, 9)", "Not on y = 3x + 1"), ("(0, 1)", "On y = 3x + 1"), ("(4, 12)", "Not on y = 3x + 1")]
    return GD("Is each point on the line y = 3x + 1?", "Line", r.sample(rows, 4), o="O2", d="H")
def g7(r):
    m = r.randint(1, 4)
    return MC(f"What shape is the graph of y = {m}x + 2?", "a straight line", ["a curve", "a circle", "a zigzag"], o="O2")


s.std([g1, g4, g2, g3, g5, g6, g7], EX("Explain why you should plot at least three points for a straight-line graph.", [("two points are enough to draw a line", ["two points|2 points"]), ("the third point checks for mistakes", ["check|mistake|error"])], "Two points fix a straight line, but plotting a third point checks your working: if it does not lie on the line, a value is wrong.", o="O2"))

# ================================================================== 11.3
s = U.section("11.3", "Lines parallel to the axes", ["O3"])
s.idea("Horizontal and vertical lines", ["Every point on the line **x = 3** has x-coordinate 3: it is a **vertical** line.",
       "Every point on **y = −2** has y-coordinate −2: it is a **horizontal** line."], fig={"kind": "coord", "x": [-5, 5], "y": [-5, 5], "lines": [{"x": 3, "label": "x = 3"}, {"y": -2, "label": "y = −2"}]})
s.check(MC("Which line is horizontal?", "y = 4", ["x = 4", "y = 4x", "x = −4"], o="O3"))
s.mistake("Not the other way round", ["x = 2 is vertical (it goes up and down through x = 2)."])


def h1(r):
    k = nz(r, -5, 5); ax = pick(r, ["x", "y"])
    return MC(f"Describe the line {ax} = {k}.", "vertical" if ax == "x" else "horizontal", ["horizontal" if ax == "x" else "vertical", "diagonal"], o="O3", fig={"kind": "coord", "x": [-6, 6], "y": [-6, 6], "lines": [{"x": k} if ax == "x" else {"y": k}]})
def h2(r):
    k = nz(r, -5, 5); ax = pick(r, ["x", "y"])
    return S("Write the equation of the line shown.", [f"{ax} = {k}", f"{ax}={k}"], o="O3", fig={"kind": "coord", "x": [-6, 6], "y": [-6, 6], "lines": [{"x": k} if ax == "x" else {"y": k}]})
def h3(r):
    a, b = nz(r, -5, 5), nz(r, -5, 5)
    return S(f"Where do the lines x = {a} and y = {b} cross? Write the coordinates.", PACC((a, b)), o="O3")
def h4(r):
    k = nz(r, -5, 5)
    return MS(f"Select ALL the points that lie on x = {k}.", [f"({k}, 3)", f"({k}, −2)"], [f"(3, {k})", f"({k + 1}, {k})"], o="O3")
def h5(r):
    rows = [("x = 4", "Vertical"), ("y = −1", "Horizontal"), ("x = −3", "Vertical"), ("y = 6", "Horizontal"), ("x = 0 (the y-axis)", "Vertical")]
    return GD("Is each line vertical or horizontal?", "Direction", r.sample(rows, 4), o="O3")
def h6(r):
    a, b = sorted(r.sample(range(-5, 6), 2)); c, d = sorted(r.sample(range(-5, 6), 2))
    return N(f"The lines x = {a}, x = {b}, y = {c} and y = {d} make a rectangle. Find its area.", (b - a) * (d - c), "square units", units=["square units", "units²"], o="O3", d="H")
def h7(r):
    k = nz(r, -5, 5)
    return S(f"What is the equation of the line through (2, {k}) and (−4, {k})?", [f"y = {k}", f"y={k}"], o="O3", d="H")


s.std([h1, h2, h3, h4, h5, h6, h7], EX("Explain why the line x = 5 is vertical.", [("every point has x-coordinate 5", ["every point|all points|x-coordinate (is )?5"]), ("so the points are directly above and below each other", ["above|below|up and down|same across"])], "Every point on x = 5 has x-coordinate 5, for example (5, 0), (5, 2) and (5, −3). These points are directly above and below each other, so the line is vertical.", o="O3"))

# ================================================================== 11.4
s = U.section("11.4", "Interpreting graphs", ["O4"])
s.idea("Reading graphs", ["Read the labels and scales on both axes. To read a value, go up from the x-axis to the line, then across to the y-axis.",
       "A **conversion graph** changes one unit into another, e.g. dollars to euros or km to miles."], fig={"kind": "linegraph", "x": {"min": 0, "max": 50, "step": 10, "label": "Miles"}, "y": {"min": 0, "max": 80, "step": 10, "label": "Kilometres"}, "series": [{"pts": [[0, 0], [50, 80]]}]})
s.check(N("Use the graph above: 25 miles is about how many kilometres?", 40, "km", units=["km"], o="O4"))
s.mistake("Check the scale", ["Work out what one small square is worth before you read a value."])


def i1(r):
    x = r.randint(1, 10) * 5
    return N(f"Use the conversion graph to change {x} miles into kilometres.", x * 8 / 5, "km", units=["km"], o="O4", tol=1, fig={"kind": "linegraph", "x": {"min": 0, "max": 50, "step": 10, "label": "Miles"}, "y": {"min": 0, "max": 80, "step": 10, "label": "Kilometres"}, "series": [{"pts": [[0, 0], [50, 80]]}]})
def i2(r):
    v = [r.randint(5, 30) for _ in range(6)]; k = r.randrange(6)
    return N(f"The graph shows the temperature (°C) over six hours. What was the temperature at hour {k + 1}?", v[k], "°C", units=["°C"], o="O4", fig={"kind": "linegraph", "x": {"min": 1, "max": 6, "step": 1, "label": "Hour"}, "y": {"min": 0, "max": 35, "step": 5, "label": "Temperature (°C)"}, "series": [{"pts": [[i + 1, x] for i, x in enumerate(v)]}]})
def i3(r):
    rate = r.randint(2, 8)
    return N(f"A taxi costs ${rate} per km. The graph shows cost against distance. How much does 6 km cost?", 6 * rate, "$", units=["$"], o="O4", fig={"kind": "linegraph", "x": {"min": 0, "max": 10, "step": 1, "label": "Distance (km)"}, "y": {"min": 0, "max": rate * 10, "step": rate * 2, "label": "Cost ($)"}, "series": [{"pts": [[0, 0], [10, rate * 10]]}]})
def i4(r):
    return MC("On a graph of distance from home against time, what does a horizontal line show?", "staying in the same place", ["walking quickly", "going home", "speeding up"], o="O4")
def i5(r):
    v = [r.randint(5, 30) for _ in range(6)]
    return N("The graph shows the temperature over six hours. What was the rise from the lowest to the highest temperature?", max(v) - min(v), "°C", units=["°C"], o="O4", d="H", fig={"kind": "linegraph", "x": {"min": 1, "max": 6, "step": 1, "label": "Hour"}, "y": {"min": 0, "max": 35, "step": 5, "label": "Temperature (°C)"}, "series": [{"pts": [[i + 1, x] for i, x in enumerate(v)]}]})
def i6(r):
    k = pick(r, [2, 3, 4])
    return TB(f"A conversion graph shows $1 = {k} units of another currency. Complete the table.", ["Dollars", "Other currency"], [["5", B(5 * k)], ["12", B(12 * k)]], o="O4", fig={"kind": "linegraph", "x": {"min": 0, "max": 20, "step": 5, "label": "Dollars"}, "y": {"min": 0, "max": 20 * k, "step": 10, "label": "Other currency"}, "series": [{"pts": [[0, 0], [20, 20 * k]]}]})
def i7(r):
    a = r.randint(2, 6) * 2; t = r.randint(1, 3) * 10
    return N(f"A walker goes {a} km in {t} minutes, stops, then walks home. How far from home is the furthest point?", a, "km", units=["km"], o="O4", fig={"kind": "linegraph", "x": {"min": 0, "max": 90, "step": 10, "label": "Time (min)"}, "y": {"min": 0, "max": 14, "step": 2, "label": "Distance from home (km)"}, "series": [{"pts": [[0, 0], [t, a], [t + 20, a], [t + 50, 0]]}]})


s.std([i1, i2, i3, i4, i5, i6, i7], EX("Explain how to use a conversion graph to change 30 miles into kilometres.", [("find 30 on the miles axis and go up to the line", ["go up|find 30|to the line"]), ("go across to the kilometres axis and read the value (48 km)", ["across|read|48"])], "Find 30 on the miles axis, go straight up to the line, then go across to the kilometres axis and read the value: about 48 km.", o="O4"))

U.mindmap(("Functions", "y = 2x + 1: input x, output y", "O1", "11.1"), ("Plotting", "Table of values • straight line", "O2", "11.2"),
          ("Parallel to the axes", "x = k vertical • y = k horizontal", "O3", "11.3"), ("Real-life graphs", "Read scales • conversion graphs", "O4", "11.4"))
