# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 11 Graphs (11.1 Functions, 11.2 Plotting graphs, 11.3 Gradient and intercept,
11.4 Interpreting graphs). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(11, "Graphs", "Algebra",
         "Linear functions, tables of values and straight-line graphs, the gradient and y-intercept of y = mx + c, and real-life graphs.",
         {"O1": {"code": "8Ae.07", "sec": "11.1", "codeNote": "", "t": "Understand that a function is a relationship where each input has a single output, and find outputs and inputs."},
          "O2": {"code": "8Ae.08", "sec": "11.2", "codeNote": "", "t": "Complete tables of values and plot straight-line graphs, including lines parallel to the axes."},
          "O3": {"code": "8Ae.09", "sec": "11.3", "codeNote": "", "t": "Recognise the gradient and y-intercept in y = mx + c and find the gradient of a line."},
          "O4": {"code": "8Ae.10", "sec": "11.4", "codeNote": "", "t": "Read, interpret and draw graphs of real-life situations, including distance–time graphs."}})
eq = lambda m, c: f"y = {'' if m == 1 else '−' if m == -1 else m}x" + (f" {'+' if c > 0 else '−'} {abs(c)}" if c else "")

# ================================================================== 11.1
s = U.section("11.1", "Functions", ["O1"])
s.idea("Linear functions", ["In a function every input x has **exactly one** output y. y = 2x + 3: input 4 gives output 11.",
       "A table of values lists inputs and outputs. If the outputs go up by the same amount each time, the function is **linear** and its graph is a straight line."])
s.check(N("For y = 5x − 2, find y when x = 3.", 13, o="O1"))
s.example("Finding the input", "For y = 3x + 1, find x when y = 22.", [("3x + 1 = 22", ""), ("3x = 21, x = 7", "")], "x = 7")
s.check(MC("Before you read on: for y = 4 − x, what happens to y when x goes up by 1?", "y goes down by 1", [("y goes up by 1", "The −x makes y smaller as x grows."), ("y goes up by 4", "4 is the value when x = 0.")], o="O1"))
s.mistake("Negative inputs", ["For y = 2x + 3 and x = −4: 2 × (−4) + 3 = −5, not 11."])


def f1(r):
    m, c, x = r.randint(2, 6), r.randint(-8, 10), r.randint(-5, 8)
    return N(f"For {eq(m, c)}, find y when x = {x}.", m * x + c, o="O1", reason=f"{m} × {x if x >= 0 else f'({x})'} {'+' if c >= 0 else '−'} {abs(c)} = {m * x + c}.")
def f2(r):
    m, c, x = r.randint(2, 6), r.randint(-8, 10), r.randint(-3, 9)
    return N(f"For {eq(m, c)}, find x when y = {m * x + c}.", x, o="O1", reason=f"{m}x = {m * x + c - c} → x = {x}.")
def f3(r):
    m, c = r.randint(1, 5), r.randint(-5, 6); xs = [-1, 0, 1, 2, 3]
    return TB(f"Complete the table of values for {eq(m, c)}.", ["x", "y"], [[str(x), B(m * x + c)] for x in xs], o="O1")
def f4(r):
    m, c = r.randint(2, 5), r.randint(-4, 8); xs = r.sample(range(0, 6), 3)
    return MC("Which equation fits this table?", eq(m, c), [eq(m + 1, c - 1) if (m + 1) * xs[0] + c - 1 != m * xs[0] + c else eq(m, c + 1), eq(c if c > 0 else 2, m), eq(m, -c) if c else eq(m, 2)], o="O1", d="H", data={"head": ["x", *map(str, sorted(xs))], "rows": [["y", *[str(m * x + c) for x in sorted(xs)]]]})
def f5(r):
    rows = [("y = 3x + 1", "Linear"), ("y = x²", "Not linear"), ("y = 5 − 2x", "Linear"), ("y = 2ˣ", "Not linear"), ("y = x/2", "Linear"), ("y = 1/x", "Not linear")]
    return GD("Is each function linear?", "Linear?", r.sample(rows, 4), o="O1")
def f6(r):
    c, k = r.randint(5, 30), r.randint(2, 9); n = r.randint(3, 15)
    return N(f"A taxi charges C = {c} + {k}d dollars for d km. How much does a {n} km journey cost?", c + k * n, "$", units=["$"], o="O1", reason=f"{c} + {k} × {n} = {c + k * n}.")
def f7(r):
    m, c = r.randint(2, 6), r.randint(1, 9); x = r.randint(2, 8)
    return MS(f"Select ALL the points that lie on {eq(m, c)}.", [f"({x}, {m * x + c})", f"(0, {c})"], [f"({x}, {m * x + c + 1})", f"({c}, 0)"], o="O1", d="H")
def f8(r):
    m, c = r.randint(2, 4), r.randint(-3, 5)
    return N(f"The output of {eq(m, c)} is 4 times the input. What is the input?", -c / (m - 4) if m != 4 else None, o="O1", d="VH", reason=f"{m}x + {c} = 4x → x = {fmt(-c / (m - 4))}.") if m != 4 and c % (4 - m) == 0 and c != 0 else None


def g111(r):
    m, c = r.randint(2, 5), r.randint(-5, 5)
    return MC(f"Which point is NOT on y = {m}x {'+' if c >= 0 else '−'} {abs(c)}?", f"(2, {2 * m + c + 1})", [(f"(0, {c})", "Substitute x = 0."), (f"(1, {m + c})", "Substitute x = 1."), (f"(3, {3 * m + c})", "Substitute x = 3.")], o="O1", d="H", reason=f"When x = 2, y = {2 * m + c}, not {2 * m + c + 1}.")


s.std([f3, f4, f1, f2, f5, f6, f7, f8], EX("Explain how a table of values shows that y = 4x − 1 is linear.", [("the y values go up by the same amount each time", ["same amount|constant|equal steps|by 4 each"]), ("by 4 for each increase of 1 in x", ["4"])], "When x goes up by 1, y goes up by 4 every time. A constant change in y means the function is linear.", o="O1"),
      deep=[g111])

# ================================================================== 11.2
s = U.section("11.2", "Plotting graphs", ["O2"])
s.idea("Plotting a straight line", ["Make a table of values, plot each (x, y) point and join them with a **straight line** using a ruler. Three points are enough – the third is a check.",
       "Lines **parallel to the axes**: x = 3 is a vertical line; y = −2 is a horizontal line."], fig={"kind": "coord", "x": [-2, 5], "y": [-3, 8], "lines": [{"m": 2, "c": 1, "label": "y = 2x + 1"}, {"x": 3, "label": "x = 3"}]})
s.check(N("The line y = 2x + 1 passes through (2, k). Find k.", 5, o="O2"))
s.check(MC("Before you read on: how many points do you need to draw a straight-line graph?", "2, plus a third to check", [("1", "One point does not fix the direction."), ("10", "Two points fix a straight line; a third checks it.")], o="O2"))
s.mistake("x = or y =?", ["x = 4 is a VERTICAL line (every point has x-coordinate 4). y = 4 is horizontal."])


def p1(r):
    m, c = r.randint(1, 4), r.randint(-3, 4); xs = [0, 1, 2, 3]
    return GR(f"Plot the graph of {eq(m, c)} for x = 0 to 3.", {"min": 0, "max": 4, "step": 1, "label": "x"}, {"min": min(-3, c), "max": max(m * 3 + c, 5) + 1, "step": 1, "label": "y"}, [[x, m * x + c] for x in xs], o="O2", reason="Plot (x, y) from the table and join with a ruler.") if False else TB(f"Complete the table for {eq(m, c)} and use it to plot the line.", ["x", "y"], [[str(x), B(m * x + c)] for x in xs], o="O2")
def p2(r):
    k = nz(r, -5, 6); ax = pick(r, ["x", "y"])
    return MC(f"Which describes the line {ax} = {k}?", "a vertical line" if ax == "x" else "a horizontal line", ["a horizontal line" if ax == "x" else "a vertical line", "a line through the origin", f"a line with gradient {k}"], o="O2", fig={"kind": "coord", "x": [-6, 6], "y": [-6, 6], "lines": [{"x": k} if ax == "x" else {"y": k}]})
def p3(r):
    m, c = r.randint(1, 3), r.randint(-2, 3); x = r.randint(-2, 4)
    return N(f"The graph shows the line {eq(m, c)}. Use it or the equation to find y when x = {x}.", m * x + c, o="O2", fig={"kind": "coord", "x": [-3, 5], "y": [min(-6, m * -3 + c), max(m * 5 + c, 6)], "lines": [{"m": m, "c": c, "label": eq(m, c)}]})
def p4(r):
    a, b = nz(r, -5, 5), nz(r, -5, 5)
    return S(f"Write the coordinates of the point where the lines x = {a} and y = {b} cross.", [f"({a}, {b})", f"({a},{b})", f"{a}, {b}", f"{a},{b}"], o="O2", fig={"kind": "coord", "x": [-6, 6], "y": [-6, 6], "lines": [{"x": a, "label": f"x = {a}"}, {"y": b, "label": f"y = {b}"}]}, reason=f"({a}, {b}).")
def p5(r):
    m, c = r.randint(1, 4), r.randint(-4, 5)
    pts = [(0, c), (1, m + c), (2, 2 * m + c + pick(r, [1, -1]))]
    return MC(f"A student plotted three points for {eq(m, c)}. Which point is wrong?", f"(2, {pts[2][1]})", [f"(0, {c})", f"(1, {m + c})", "none of them"], o="O2", d="H", reason=f"When x = 2, y = {2 * m + c}.")
def p6(r):
    k = nz(r, -5, 6)
    if k in (1, 2, -3): k = 4
    return MS(f"Select ALL the points on the line y = {k}.", [f"(2, {k})", f"(−3, {k})"], [f"({k}, 2)", f"({k}, {k + 1})"], o="O2")
def p7(r):
    m, c = r.randint(2, 5), r.randint(-6, 6)
    return N(f"Where does the line {eq(m, c)} cross the y-axis? Give the y-coordinate.", c, o="O2", reason="At the y-axis x = 0, so y = c.")
def p8(r):
    m, c = r.randint(1, 4), r.randint(1, 8); x = -c / m
    return N(f"Where does the line {eq(m, c)} cross the x-axis? Give the x-coordinate (1 d.p. if needed).", round(x, 1), o="O2", d="H", tol=0.05, reason=f"y = 0: {m}x + {c} = 0 → x = {fmt(round(x, 2))}.")


def g112(r):
    m, c = r.randint(1, 4), r.randint(-3, 4); x = r.randint(-2, 4)
    return MC(f"Ali plots y = {m}x + {c} and his points are (0, {c}), (1, {m + c}), ({x}, {m * x + c + 2}). Which point is wrong?", f"({x}, {m * x + c + 2})", [(f"(0, {c})", f"0 × {m} + {c} = {c} ✓"), (f"(1, {m + c})", f"1 × {m} + {c} = {m + c} ✓")], o="O2", d="H",
              reason=f"When x = {x}, y = {m * x + c}. A point off the line means a working mistake.") if x not in (0, 1) else None


s.std([p2, p3, p1, p4, p5, p6, p7, p8], EX("Explain why you only need two points to draw a straight line, but should plot a third.", [("two points fix a straight line", ["two points|2 points|join"]), ("the third point checks for mistakes", ["check|mistake|error"])], "A straight line is fixed by two points, but a third point acts as a check: if it is not on the line, one of the calculations is wrong.", o="O2"),
      deep=[g112])

# ================================================================== 11.3
s = U.section("11.3", "Gradient and intercept", ["O3"])
s.idea("y = mx + c", ["In **y = mx + c**, m is the **gradient** (steepness) and c is the **y-intercept** (where the line crosses the y-axis).",
       "Gradient = change in y ÷ change in x. A positive gradient slopes up to the right; a negative gradient slopes down."], fig={"kind": "coord", "x": [-1, 5], "y": [-2, 10], "lines": [{"m": 2, "c": 1, "label": "y = 2x + 1"}, {"m": -1, "c": 6, "label": "y = −x + 6"}]})
s.example("Gradient from two points", "Find the gradient of the line through (1, 3) and (4, 12).", [("change in y = 12 − 3 = 9", ""), ("change in x = 4 − 1 = 3", ""), ("gradient = 9 ÷ 3 = 3", "")], "3")
s.check(N("What is the gradient of y = 7x − 4?", 7, o="O3"))
s.idea("What the gradient and intercept mean", ["In y = mx + c, m is the gradient: how much y goes up when x goes up by 1. c is the y-intercept: where the line crosses the y-axis (x = 0).",
       "Lines with the same gradient are parallel."])
s.check(MC("Before you read on: which line is parallel to y = 3x − 2?", "y = 3x + 5", [("y = 2x − 2", "Same intercept, different gradient."), ("y = −3x − 2", "The gradient −3 slopes the other way.")], o="O3"))
s.mistake("c is not always the second number", ["In y = 5 − 2x the gradient is −2 and the intercept is 5."])


def g1(r):
    m, c = nz(r, -6, 8), r.randint(-9, 9); k = r.randint(0, 1)
    return N(f"What is the {'gradient' if k == 0 else 'y-intercept'} of {eq(m, c)}?", m if k == 0 else c, o="O3")
def g2(r):
    x1, y1 = r.randint(-3, 3), r.randint(-3, 5); m = nz(r, -4, 5); dx = r.randint(1, 4)
    return N(f"Find the gradient of the line through ({x1}, {y1}) and ({x1 + dx}, {y1 + m * dx}).", m, o="O3", reason=f"({y1 + m * dx} − {y1}) ÷ ({x1 + dx} − {x1}) = {m * dx} ÷ {dx} = {m}.")
def g3(r):
    m, c = nz(r, -3, 3), r.randint(-3, 4)
    return S("Write the equation of the line shown in the form y = mx + c.", [eq(m, c).replace(" ", ""), eq(m, c), eq(m, c).replace("−", "-"), eq(m, c).replace("−", "-").replace(" ", "")], o="O3", d="H", fig={"kind": "coord", "x": [-4, 4], "y": [-8, 8], "lines": [{"m": m, "c": c}]}, reason=f"Intercept {c}; gradient {m}.")
def g4(r):
    m = nz(r, -5, 5); cs = r.sample(range(-6, 7), 2)
    return MC(f"Which line is parallel to {eq(m, cs[0])}?", eq(m, cs[1]), [eq(-m, cs[0]), eq(cs[0] if cs[0] else 3, m), eq(m + 1, cs[0])], o="O3", reason="Parallel lines have the same gradient.")
def g5(r):
    rows = [("y = 3x + 2", "3"), ("y = −2x + 5", "−2"), ("y = x − 4", "1"), ("y = 6 − x", "−1"), ("y = 4x", "4"), ("y = 7", "0")]
    return GD("Write the gradient of each line.", "Gradient", r.sample(rows, 4), o="O3", extra=["2", "5"])
def g6(r):
    m, c = nz(r, -5, 6), r.randint(-8, 8)
    return X(f"A line has gradient {m} and crosses the y-axis at (0, {c}). Write its equation.", f"{m}x+({c})", vars="xy", lhs="y", o="O3", show=eq(m, c).split("= ")[1])
def g7(r):
    m, c = r.randint(1, 3), r.randint(-2, 4)
    return TB("Read the gradient and y-intercept of the line.", ["Feature", "Value"], [["Gradient", B(m)], ["y-intercept", B(c)]], o="O3", fig={"kind": "coord", "x": [-3, 4], "y": [-6, 10], "lines": [{"m": m, "c": c}]})
def g8(r):
    m1, m2 = r.sample([1, 2, 3, 5, -1, -2, -4], 2)
    st = m1 if abs(m1) > abs(m2) else m2
    return MC(f"Which line is steeper: y = {m1}x + 1 or y = {m2}x − 3?", f"y = {st}x {'+ 1' if st == m1 else '− 3'}", [f"y = {m2 if st == m1 else m1}x {'− 3' if st == m1 else '+ 1'}", "they are equally steep"], o="O3", d="H", reason="The bigger the size of the gradient, the steeper the line.") if abs(m1) != abs(m2) else None


def g113(r):
    m, c = r.randint(-4, 5), r.randint(-6, 6)
    if m == 0: m = 2
    return TB(f"For the line {eq(m, c)}, complete the table.", ["", "Value"], [["Gradient", B(m)], ["y-intercept", B(c)]], o="O3", d="H", reason="Read m and c from y = mx + c.")
def g114(r):
    x1, x2 = r.randint(-3, 1), r.randint(2, 6); m = r.randint(-3, 4) or 2; c = r.randint(-4, 4)
    return N(f"A line passes through ({x1}, {m * x1 + c}) and ({x2}, {m * x2 + c}). Find its gradient.", m, o="O3", d="H", reason=f"Change in y ÷ change in x = {m * (x2 - x1)} ÷ {x2 - x1} = {m}.")


s.std([g5, g7, g1, g2, g4, g6, g3, g8], EX("Explain what the 3 and the −2 tell you about the line y = 3x − 2.", [("3 is the gradient: up 3 for each 1 across", ["gradient|steep|up 3"]), ("−2 is the y-intercept: crosses the y-axis at (0, −2)", ["intercept|crosses|y-axis|\\(0, ?−2\\)|\\(0, ?-2\\)"])], "3 is the gradient: the line goes up 3 for every 1 to the right. −2 is the y-intercept: the line crosses the y-axis at (0, −2).", o="O3"),
      deep=[g113, g114])

# ================================================================== 11.4
s = U.section("11.4", "Interpreting graphs", ["O4"])
s.idea("Real-life graphs", ["Read the **labels and scales** on both axes first. A straight line means a steady rate; a steeper line means a faster rate.",
       "On a **distance–time graph**, a horizontal line means the object has **stopped**; speed = distance ÷ time."], fig={"kind": "linegraph", "x": {"min": 0, "max": 60, "step": 10, "label": "Time (minutes)"}, "y": {"min": 0, "max": 12, "step": 2, "label": "Distance (km)"}, "series": [{"pts": [[0, 0], [20, 6], [30, 6], [60, 12]]}]})
s.check(N("On the graph above, how far is the cyclist from home after 20 minutes (km)?", 6, "km", units=["km"], o="O4"))
s.check(MC("Before you read on: a distance–time graph goes down towards zero. What does that show?", "Coming back towards the start", [("Slowing down", "Slowing down makes the line less steep, not go down."), ("Going faster", "The distance from the start is getting smaller.")], o="O4"))
s.mistake("Read the scale", ["Check what one small square is worth before you read a value."])


def t1(r):
    a, t1_, t2 = r.randint(2, 6) * 2, r.randint(1, 3) * 10, r.randint(1, 2) * 10
    pts = [[0, 0], [t1_, a], [t1_ + t2, a], [t1_ + t2 + 20, 0]]
    return N("A walker's journey is shown. For how many minutes did she stop?", t2, "minutes", units=["minutes", "min"], o="O4", fig={"kind": "linegraph", "x": {"min": 0, "max": 80, "step": 10, "label": "Time (minutes)"}, "y": {"min": 0, "max": 14, "step": 2, "label": "Distance (km)"}, "series": [{"pts": pts}]}, reason="The flat part shows she stopped.")
def t2(r):
    d, t = r.randint(2, 6) * 10, r.randint(1, 4)
    return N(f"A car travels at a steady speed. The distance–time graph shows {d * t} km after {t} hours. Find its speed.", d, "km/h", units=["km/h"], o="O4", fig={"kind": "linegraph", "x": {"min": 0, "max": 5, "step": 1, "label": "Time (hours)"}, "y": {"min": 0, "max": 300, "step": 50, "label": "Distance (km)"}, "series": [{"pts": [[0, 0], [t, d * t]]}]}, reason=f"{d * t} ÷ {t} = {d} km/h.")
def t3(r):
    rate = r.randint(2, 6)
    return N(f"A tank is filled at {rate} litres per minute. The graph of volume against time is a straight line. How much water is in the tank after 8 minutes?", rate * 8, "litres", units=["litres", "l"], o="O4", fig={"kind": "linegraph", "x": {"min": 0, "max": 10, "step": 2, "label": "Time (minutes)"}, "y": {"min": 0, "max": 60, "step": 10, "label": "Volume (litres)"}, "series": [{"pts": [[0, 0], [10, rate * 10]]}]})
def t4(r):
    return MC("On a distance–time graph, what does a steeper line show?", "a faster speed", [("a slower speed", ""), ("the object has stopped", "That is a horizontal line."), ("going backwards", "")], o="O4")
def t5(r):
    k = pick(r, [1.5, 2, 2.5]); x = r.randint(2, 8)
    return N(f"The graph converts kilograms to pounds (1 kg ≈ {k} lb... use the graph). How many pounds is {x} kg?".replace(" (1 kg ≈ " + str(k) + " lb... use the graph)", ""), x * k if k != 2.5 else x * 2.2, "lb", units=["lb", "pounds"], tol=0.3, o="O4", fig={"kind": "linegraph", "x": {"min": 0, "max": 10, "step": 1, "label": "Mass (kg)"}, "y": {"min": 0, "max": 25, "step": 5, "label": "Mass (lb)"}, "series": [{"pts": [[0, 0], [10, 22]]}]}, reason="Read up from the kg value to the line, then across.") if False else N(f"The conversion graph shows 10 kg = 22 lb. Use it to convert {x} kg to pounds.", round(x * 2.2, 1), "lb", units=["lb", "pounds"], tol=0.3, o="O4", fig={"kind": "linegraph", "x": {"min": 0, "max": 10, "step": 1, "label": "Mass (kg)"}, "y": {"min": 0, "max": 24, "step": 2, "label": "Mass (lb)"}, "series": [{"pts": [[0, 0], [10, 22]]}]}, reason=f"{x} × 2.2 ≈ {round(x * 2.2, 1)} lb.")
def t6(r):
    rows = [("Horizontal line", "Stopped"), ("Steep line", "Moving fast"), ("Gentle slope", "Moving slowly"), ("Line going down to 0", "Returning to the start")]
    return GD("On a distance–time graph, what does each part show?", "Meaning", rows, o="O4")
def t7(r):
    a, t = r.randint(3, 9) * 2, r.randint(2, 4)
    return N(f"Jo cycles {a} km in {t * 10} minutes at a steady speed. What is her speed in km/h?", round(a / (t * 10) * 60, 1), "km/h", units=["km/h"], o="O4", d="H", tol=0.05, reason=f"{a} km in {t * 10} min = {fmt(round(a / (t * 10) * 60, 1))} km/h.")
def t8(r):
    c, k = r.randint(10, 30), r.randint(2, 6)
    return N(f"A phone plan costs ${c} a month plus ${k} per GB of data. The graph of cost against data is a straight line. What is the cost for 5 GB?", c + 5 * k, "$", units=["$"], o="O4", fig={"kind": "linegraph", "x": {"min": 0, "max": 10, "step": 1, "label": "Data (GB)"}, "y": {"min": 0, "max": c + 10 * k + 10, "step": 10, "label": "Cost ($)"}, "series": [{"pts": [[0, c], [10, c + 10 * k]]}]})


def g115(r):
    d, t = r.randint(2, 9) * 10, r.randint(2, 5)
    return N(f"A distance–time graph is a straight line from (0, 0) to ({t} h, {d * t} km). What is the speed?", d, "km/h", units=["km/h"], o="O4", d="H", reason=f"Speed = gradient = {d * t} ÷ {t} = {d} km/h.")


s.std([t1, t2, t3, t5, t8, t4, t6, t7], EX("A distance–time graph has a horizontal section from 10:00 to 10:30. Explain what this shows.", [("the distance does not change", ["does not change|doesn't change|stays the same|same distance|constant"]), ("so the person stopped for 30 minutes", ["stop|not moving|rest|stationary"])], "The distance from the start stays the same between 10:00 and 10:30, so the person was not moving: they stopped for 30 minutes.", o="O4"),
      deep=[g115])

U.mindmap(("Functions", "One output for each input • tables of values", "O1", "11.1"), ("Plotting", "Plot 3 points • x = k vertical, y = k horizontal", "O2", "11.2"),
          ("y = mx + c", "m = gradient • c = y-intercept • parallel: same m", "O3", "11.3"), ("Real-life graphs", "Read scales • flat = stopped • speed = distance ÷ time", "O4", "11.4"))
