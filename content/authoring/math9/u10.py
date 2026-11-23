# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 10 Graphs. Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(10, "Graphs", "Algebra",
         "Linear functions and their tables, plotting straight-line graphs, gradient and y-intercept, and interpreting real-life graphs.",
         {"O1": {"sec": "10.1", "code": "9As.04", "codeNote": "", "t": "Understand that a linear function y = mx + c gives a straight line, and complete tables of values."},
          "O2": {"sec": "10.2", "code": "9As.05", "codeNote": "", "t": "Plot graphs of linear functions, including those written implicitly (e.g. 2x + 3y = 12)."},
          "O3": {"sec": "10.3", "code": "9As.06", "codeNote": "", "t": "Find the gradient and y-intercept of a straight line from its equation or two points, and recognise parallel lines."},
          "O4": {"sec": "10.4", "code": "9As.07", "codeNote": "", "t": "Interpret real-life graphs, including distance–time and conversion graphs, and find rates of change."}})
def eqn(m, c):
    mm = frac(Fr(m)) if not isinstance(m, int) else (str(m) if abs(m) != 1 else ("" if m == 1 else "−"))
    if isinstance(m, int) and m not in (1, -1): mm = fmt(m)
    return "y = " + (poly((m, "x"), (c, "")) if isinstance(m, int) else f"{mm}x" + ("" if c == 0 else (f" + {c}" if c > 0 else f" − {-c}")))

# ================================================================== 10.1
s = U.section("10.1", "Functions", ["O1"])
s.idea("Linear functions", ["An equation like **y = 3x − 2** is a **linear function**: every x gives one y, and the points lie on a **straight line**.",
       "Make a **table of values**: choose x values, substitute, and find y."], table={"caption": "y = 3x − 2", "head": ["x", "−1", "0", "1", "2", "3"], "rows": [["y", "−5", "−2", "1", "4", "7"]]})
s.example("Is the point on the line?", "Is (4, 9) on the line y = 2x + 1?", [("x = 4: 2 × 4 + 1 = 9", ""), ("y = 9 ✓", "")], "Yes")
s.check(N("y = 5 − 2x. Find y when x = −3.", 11, o="O1"))
s.idea("Linear or not?", ["Linear functions have **x to the power 1 only**: y = 4x + 1, y = 7 − x, y = x/2. Functions such as y = x² or y = 1/x are **not** linear – their graphs are curves."])
s.check(MC("Which function is NOT linear?", "y = x² + 1", [("y = 3x − 4", ""), ("y = 10 − x", ""), ("y = x/5", "")], o="O1"))
def l1(r):
    m, c = nz(r, -5, 5), r.randint(-8, 8); xs = r.sample(range(-3, 5), 4); xs.sort()
    return TB(f"Complete the table of values for {eqn(m, c)}.", ["x"] + [str(x) for x in xs], [["y"] + [B(m * x + c) for x in xs]], reason=f"Substitute each x: y = {m} × x + ({c}). For example x = {xs[0]} gives {m} × {xs[0]} + ({c}) = {m*xs[0]+c}.", o="O1")
def l2(r):
    m, c = nz(r, -5, 5), r.randint(-8, 8); x = r.randint(-6, 8); on = r.random() < 0.5; y = m * x + c + (0 if on else nz(r, -2, 2))
    return MC(f"Is the point ({x}, {y}) on the line {eqn(m, c)}?", "Yes" if on else "No", [("No" if on else "Yes", f"Substitute x = {x}: y = {m*x+c}.")], o="O1")
def l3(r):
    m, c = nz(r, -5, 5), r.randint(-8, 8); y = m * r.randint(-6, 8) + c
    return N(f"The point (a, {y}) lies on {eqn(m, c)}. Find a.", (y - c) / m, reason=f"{y} = {m}a + ({c}), so {m}a = {y - c} and a = {y - c} ÷ {m} = {fmt((y - c) / m)}.", o="O1", d="H")
def l4(r):
    rows = [("y = 4x − 1", "Linear"), ("y = x²", "Not linear"), ("y = 6 − 2x", "Linear"), ("y = 1/x", "Not linear"), ("x + y = 8", "Linear"), ("y = x³ − 1", "Not linear")]
    return GD("Is each function linear?", "Linear?", r.sample(rows, 4), o="O1")
def l5(r):
    m, c = nz(r, -4, 4), r.randint(-6, 6)
    return N(f"Where does the line {eqn(m, c)} cross the y-axis? Give the y-coordinate.", c, reason=f"The line crosses the y-axis where x = 0, so y = {c}.", o="O1")
def l6(r):
    m, c = nz(r, 2, 5), r.randint(-6, 9); x = r.randint(1, 6)
    return X(f"The points (1, {m+c}), (2, {2*m+c}) and (3, {3*m+c}) lie on a straight line. Find its equation: y = ?", f"{m}x+({c})", reason=f"y goes up by {m} each time x goes up by 1, so m = {m}. At x = 1, y = {m+c}, so c = {m+c} − {m} = {c}.", o="O1", d="H", show=poly((m, 'x'), (c, '')), data={"head": ["x", "1", "2", "3"], "rows": [["y", str(m + c), str(2 * m + c), str(3 * m + c)]]})
def l7(r):
    m, c = nz(r, -4, 4), r.randint(-6, 6)
    return N(f"Where does {eqn(m, c)} cross the x-axis? Give the x-coordinate as a decimal or fraction.", -c / m, tol=1e-6, reason=f"On the x-axis y = 0: 0 = {m}x + ({c}), so x = {frac(Fr(-c, m))}.", o="O1", d="H")
s.core(l1(s.rng), l2(s.rng), l3(s.rng), l4(s.rng), l5(s.rng), l6(s.rng), l7(s.rng),
       EX("Explain how to decide whether (3, 10) lies on y = 4x − 2.", [("substitute x = 3", ["substitut|x ?= ?3|put 3"]), ("4 × 3 − 2 = 10 so yes", ["10|yes|it is on"])], "Substitute x = 3: y = 4 × 3 − 2 = 10. This matches the y-coordinate 10, so the point is on the line.", o="O1"))
s.gen("p", 44, l1, l2, l3, l4, l5, l6, l7)
s.gen("a", 8, l7, lambda r: (lambda a, b: N(f"The lines y = {a}x + 1 and y = {b} − x meet at a point. Find its x-coordinate.", (b - 1) / (a + 1), tol=1e-6, reason=f"Set {a}x + 1 = {b} − x, so {a + 1}x = {b - 1} and x = {fmt((b - 1) / (a + 1))}.", o="O1", d="VH"))(r.randint(2, 6), r.randint(5, 20)))

# ================================================================== 10.2
s = U.section("10.2", "Plotting graphs", ["O2"])
s.idea("Plotting a straight line", ["Make a table with at least **three** x values, plot the points, and join them with a ruler. Three points let you spot a mistake.",
       "For an equation like **2x + 3y = 12**, find where it crosses the axes: x = 0 gives y = 4, y = 0 gives x = 6. Plot (0, 4) and (6, 0) and join."],
       fig={"kind": "coord", "x": [-1, 7], "y": [-1, 6], "lines": [{"m": -2 / 3, "c": 4, "label": "2x + 3y = 12"}], "points": [{"x": 0, "y": 4}, {"x": 6, "y": 0}]})
s.example("Rearrange first", "Rearrange 4x + 2y = 10 into the form y = mx + c.", [("2y = 10 − 4x", ""), ("y = 5 − 2x", "")], "y = −2x + 5")
s.check(N("The line 3x + 5y = 15 crosses the x-axis at (a, 0). Find a.", 5, o="O2"))
s.mistake("Use a ruler", ["Points of a linear graph must lie on ONE straight line. If one point is off the line, re-check that calculation."])
s.check(X("Rearrange x + 2y = 8 into y = …", "4-x/2", o="O2", show="4 − x/2", lhs="y"))
def p1(r):
    m, c = nz(r, -3, 3), r.randint(-3, 4); xs = [-1, 0, 1, 2, 3]
    pts = [[x, m * x + c] for x in xs]
    ymin, ymax = min(p[1] for p in pts) - 1, max(p[1] for p in pts) + 1
    return GR(f"Plot the points of {eqn(m, c)} for x = −1, 0, 1, 2 and 3.", {"label": "x", "min": -2, "max": 4, "step": 1}, {"label": "y", "min": int(ymin), "max": int(ymax), "step": 1}, pts, o="O2", d="M")
def p2(r):
    a, b = pick(r, [(2, 3), (3, 4), (4, 5), (2, 5), (3, 2), (5, 2)]); k = a * b * r.randint(1, 2)
    w = r.random() < 0.5
    return N(f"The line {a}x + {b}y = {k} crosses the {'x' if w else 'y'}-axis at which value?", k / a if w else k / b, tol=1e-6, reason=f"Put {'y' if w else 'x'} = 0: {(str(a) + 'x') if w else (str(b) + 'y')} = {k}, so the answer is {fmt(k / a) if w else fmt(k / b)}.", o="O2")
def p3(r):
    a, b = pick(r, [(2, 1), (4, 2), (6, 3), (3, 1), (8, 4)]); k = r.randint(2, 12) * b
    return X(f"Rearrange {a}x + {b}y = {k} into the form y = mx + c.", f"({k}-{a}x)/{b}", reason=f"{b}y = {k} − {a}x, then divide every term by {b}.", o="O2", lhs="y", show=poly((-a // b if a % b == 0 else 0, 'x'), (k // b, '')) if a % b == 0 else f"({k} − {a}x)/{b}")
def p4(r):
    m, c = nz(r, -3, 3), r.randint(-4, 4)
    pts = [[x, m * x + c] for x in (0, 1, 2)]; bad = r.randrange(3); pts2 = [p[:] for p in pts]; pts2[bad][1] += nz(r, -2, 2)
    return MC(f"Sam plots {eqn(m, c)} using the points ({pts2[0][0]}, {pts2[0][1]}), ({pts2[1][0]}, {pts2[1][1]}) and ({pts2[2][0]}, {pts2[2][1]}). Which point is wrong?", f"({pts2[bad][0]}, {pts2[bad][1]})", [(f"({pts2[i][0]}, {pts2[i][1]})", "") for i in range(3) if i != bad] + [("none of them", "")], o="O2", d="H")
def p5(r):
    k = r.randint(-5, 6); v = pick(r, ["x", "y"])
    return MC(f"What does the graph of {v} = {k} look like?", "a horizontal line" if v == "y" else "a vertical line", [("a vertical line" if v == "y" else "a horizontal line", ""), ("a line through the origin", ""), ("a curve", "")], o="O2")
def p6(r):
    a, b = pick(r, [(2, 3), (3, 4), (4, 3), (5, 2), (1, 2)]); k = a * b * r.randint(1, 3)
    return TB(f"Find where {a}x + {b}y = {k} crosses each axis.", ["x-intercept", "y-intercept"], [[B(k / a, 1e-6), B(k / b, 1e-6)]], reason=f"y = 0 gives x = {k} ÷ {a} = {fmt(k / a)}; x = 0 gives y = {k} ÷ {b} = {fmt(k / b)}.", o="O2", d="H")
s.core(p1(s.rng), p2(s.rng), p3(s.rng), p4(s.rng), p5(s.rng), p6(s.rng), p1(s.rng),
       EX("Explain why you should plot at least three points when drawing a straight-line graph.", [("two points always make a line", ["two points|2 points|any two"]), ("the third point checks for a mistake", ["check|mistake|error|wrong"])], "Any two points can be joined with a straight line, so a third point checks your calculations: if it is not on the line, there is a mistake.", o="O2"))
s.gen("p", 44, p1, p2, p3, p4, p5, p6)
s.gen("a", 8, p6, lambda r: (lambda a: N(f"Find the area of the triangle made by the line {a}x + 2y = {4*a} and the two axes.", 0.5 * 4 * 2 * a, "units²", units=["units²"], reason=f"Intercepts: x = {4*a} ÷ {a} = 4 and y = {4*a} ÷ 2 = {2*a}. Area = ½ × 4 × {2*a} = {4*a}.", o="O2", d="VH"))(r.randint(1, 6)))

# ================================================================== 10.3
s = U.section("10.3", "Gradient and intercept", ["O3"])
s.idea("y = mx + c", ["In **y = mx + c**, **m is the gradient** (steepness) and **c is the y-intercept** (where the line crosses the y-axis).",
       "Gradient from two points: **m = (change in y) ÷ (change in x)** = (y₂ − y₁)/(x₂ − x₁). Lines going down to the right have a negative gradient. **Parallel lines have the same gradient.**"],
       fig={"kind": "coord", "x": [-2, 6], "y": [-2, 10], "lines": [{"m": 2, "c": 1, "label": "y = 2x + 1"}], "points": [{"x": 1, "y": 3, "l": "(1, 3)"}, {"x": 3, "y": 7, "l": "(3, 7)"}]})
s.example("Two points", "Find the gradient of the line through (1, 3) and (3, 7).", [("change in y = 7 − 3 = 4", ""), ("change in x = 3 − 1 = 2", ""), ("m = 4 ÷ 2 = 2", "")], "2")
s.check(N("What is the gradient of y = 7 − 3x?", -3, o="O3"))
s.example("Equation from gradient and a point", "A line has gradient 3 and passes through (2, 5). Find its equation.", [("y = 3x + c", ""), ("5 = 3 × 2 + c → c = −1", ""), ("y = 3x − 1", "")], "y = 3x − 1")
s.mistake("Rearrange first", ["For 2y = 6x + 4 the gradient is NOT 6. Divide by 2 first: y = 3x + 2, so the gradient is 3."])
s.check(MC("Which line is parallel to y = 4x − 2?", "y = 4x + 7", [("y = −4x − 2", "Same intercept, different gradient."), ("y = 2x + 4", ""), ("y = x/4", "")], o="O3"))
def gr1(r):
    m, c = nz(r, -6, 6), r.randint(-9, 9); w = r.random() < 0.5
    return N(f"Write the {'gradient' if w else 'y-intercept'} of {eqn(m, c)}.", m if w else c, reason=f"In y = mx + c the gradient is m = {m} and the y-intercept is c = {c}.", o="O3")
def gr2(r):
    x1, y1 = r.randint(-6, 6), r.randint(-6, 6); dx = nz(r, -5, 5); m = Fr(nz(r, -6, 6), pick(r, [1, 1, 2]))
    x2 = x1 + dx * m.denominator; y2 = y1 + int(m * dx * m.denominator)
    return N(f"Find the gradient of the line through ({x1}, {y1}) and ({x2}, {y2}).", float(m), tol=1e-6, reason=f"Gradient = ({y2} − ({y1})) ÷ ({x2} − ({x1})) = {y2 - y1} ÷ {x2 - x1} = {fmt(float(m))}.", o="O3", fig={"kind": "coord", "x": [min(x1, x2) - 2, max(x1, x2) + 2], "y": [min(y1, y2) - 2, max(y1, y2) + 2], "points": [{"x": x1, "y": y1, "l": "A"}, {"x": x2, "y": y2, "l": "B"}], "segs": [[x1, y1, x2, y2]]})
def gr3(r):
    m, x, c = nz(r, -5, 5), r.randint(-5, 5), r.randint(-8, 8); y = m * x + c
    return X(f"A line has gradient {m} and passes through ({x}, {y}). Find its equation: y = ?", f"{m}x+({c})", reason=f"y = {m}x + c. Substitute ({x}, {y}): {y} = {m} × {x} + c, so c = {y - m * x}.", o="O3", d="H", show=poly((m, 'x'), (c, '')), lhs="y")
def gr4(r):
    k = pick(r, [2, 3, 4]); m, c = nz(r, -4, 4), r.randint(-6, 6)
    return N(f"Find the gradient of the line {k}y = {k*m}x + {k*c}.".replace("+ -", "− "), m, reason=f"Divide every term by {k}: y = {m}x + ({c}), so the gradient is {m}.", o="O3", d="H")
def gr5(r):
    m = nz(r, -5, 5); c1, c2 = r.sample(range(-8, 9), 2)
    return MC(f"Which line is parallel to {eqn(m, c1)}?", eqn(m, c2), [(eqn(-m, c1), ""), (eqn(m + 1, c2), ""), (eqn(c1 or 1, m), "")], o="O3")
def gr6(r):
    x1, y1, x2, y2 = r.randint(-6, 3), r.randint(-6, 6), r.randint(4, 9), r.randint(-6, 6)
    m = Fr(y2 - y1, x2 - x1); c = y1 - m * x1
    if m.denominator != 1 or c.denominator != 1: return None
    return X(f"Find the equation of the line through ({x1}, {y1}) and ({x2}, {y2}).", f"{int(m)}x+({int(c)})", reason=f"m = ({y2} − ({y1})) ÷ ({x2} − ({x1})) = {int(m)}; c = {y1} − {int(m)} × ({x1}) = {int(c)}.", o="O3", d="VH", show=poly((int(m), 'x'), (int(c), '')), lhs="y")
def gr7(r):
    m, c = nz(r, -3, 3), r.randint(-4, 4)
    return TB(f"Read the gradient and y-intercept of the line drawn.", ["Gradient", "y-intercept"], [[B(m), B(c)]], reason=f"The line crosses the y-axis at {c}; it goes {'up' if m > 0 else 'down'} {abs(m)} for every 1 across, so the gradient is {m}.", o="O3", fig={"kind": "coord", "x": [-5, 5], "y": [-10, 10], "sy": 2, "lines": [{"m": m, "c": c}]})
def gr8(r):
    rows = [("y = 3x + 1", "y = 3x − 5"), ("y = −2x", "y = 4 − 2x"), ("y = x/2 + 3", "2y = x"), ("y = 5", "y = −1")]
    return MT("Match each line with a line parallel to it.", rows, o="O3")
s.core(gr1(s.rng), gr2(s.rng), gr3(s.rng), gr4(s.rng), gr5(s.rng), gr7(s.rng), gr8(s.rng),
       EX("Explain how you know the lines y = 2x + 3 and 4x − 2y = 6 are parallel.", [("rearrange: y = 2x − 3", ["2x ?- ?3|2x − 3|rearrang"]), ("both have gradient 2", ["gradient|same|both 2|m ?= ?2"])], "Rearranging 4x − 2y = 6 gives y = 2x − 3. Both lines have gradient 2, so they are parallel.", o="O3", d="H"))
s.gen("p", 44, gr1, gr2, gr3, gr4, gr5, gr6, gr7, gr8)
s.gen("a", 8, gr6, gr3, lambda r: (lambda m, c, x: X(f"Find the equation of the line parallel to y = {m}x + {c} that passes through ({x}, 0).", f"{m}x-{m*x}", reason=f"Parallel lines have the same gradient {m}. 0 = {m} × {x} + c gives c = {-m * x}.", o="O3", d="VH", show=poly((m, 'x'), (-m * x, '')), lhs="y"))(r.randint(2, 5), r.randint(1, 9), r.randint(1, 6)))

# ================================================================== 10.4
s = U.section("10.4", "Interpreting graphs", ["O4"])
s.idea("Real-life graphs", ["On a **distance–time graph** the gradient is the **speed**. A horizontal section means the object has **stopped**. Steeper means faster.",
       "On a **conversion graph** (e.g. dollars to euros) read across and down. The gradient is the **rate** (e.g. euros per dollar)."],
       fig={"kind": "linegraph", "x": {"min": 0, "max": 60, "step": 10, "label": "Time in minutes"}, "y": {"min": 0, "max": 20, "step": 5, "label": "Distance in km"}, "series": [{"pts": [[0, 0], [20, 10], [30, 10], [60, 20]]}]})
s.example("Speed from the graph", "In the graph, how fast does the cyclist travel in the first 20 minutes?", [("10 km in 20 minutes", ""), ("= 30 km per hour", "× 3")], "30 km/h")
s.check(N("In the graph, for how many minutes is the cyclist stopped?", 10, "minutes", units=["minutes"], o="O4"))
s.mistake("Units of speed", ["Check the time units: 10 km in 20 minutes is 0.5 km per minute, or 30 km per HOUR."])
s.check(MC("On a distance–time graph, what does a steeper line mean?", "a faster speed", [("a slower speed", ""), ("stopped", "Horizontal means stopped."), ("going uphill", "")], o="O4"))
def r1(r):
    t1, d1, stop, t3 = pick(r, [10, 15, 20, 30]), r.randint(4, 15), pick(r, [5, 10, 15]), pick(r, [20, 30])
    d3 = d1 + r.randint(3, 12); pts = [[0, 0], [t1, d1], [t1 + stop, d1], [t1 + stop + t3, d3]]
    q = r.randrange(3)
    fig = {"kind": "linegraph", "x": {"min": 0, "max": pts[-1][0] + 10, "step": 10, "label": "Time in minutes"}, "y": {"min": 0, "max": d3 + 5, "step": 5, "label": "Distance in km"}, "series": [{"pts": pts}]}
    if q == 0: return N("For how many minutes was the walker stopped?", stop, "minutes", units=["minutes"], reason=f"The horizontal part runs from {t1} to {t1 + stop} minutes: {stop} minutes.", o="O4", fig=fig)
    if q == 1: return N("Find the speed in the first part of the journey, in km/h (1 d.p.).", round(d1 / t1 * 60, 1), "km/h", units=["km/h", "km"], tol=0.05, reason=f"{d1} km in {t1} minutes = {d1} ÷ {t1} × 60 = {round(d1 / t1 * 60, 1)} km/h.", o="O4", d="H", fig=fig)
    return N("Find the speed in the last part of the journey, in km/h (1 d.p.).", round((d3 - d1) / t3 * 60, 1), "km/h", units=["km/h", "km"], tol=0.05, reason=f"{d3} − {d1} = {d3 - d1} km in {t3} minutes = {d3 - d1} ÷ {t3} × 60 = {round((d3 - d1) / t3 * 60, 1)} km/h.", o="O4", d="H", fig=fig)
def r2(r):
    rate = pick(r, [0.8, 0.9, 1.2, 1.5, 25, 23, 4]); top = 100
    v = r.randint(10, 90)
    return N(f"A conversion graph shows 1 dollar = {fmt(rate)} units of another currency. How many units do you get for ${v}?", round(v * rate, 2), "units", units=["units", "$"], reason=f"{v} × {fmt(rate)} = {fmt(round(v * rate, 2))}.", o="O4", fig={"kind": "linegraph", "x": {"min": 0, "max": 100, "step": 20, "label": "Dollars"}, "y": {"min": 0, "max": round(rate * 100), "step": max(1, round(rate * 20)), "label": "Other currency"}, "series": [{"pts": [[0, 0], [100, round(rate * 100, 2)]], "dots": False}]})
def r3(r):
    c, k = r.randint(5, 30), r.randint(2, 8)
    return TB(f"A taxi charges ${c} plus ${k} per km. Complete the table and give the gradient of the cost graph.", ["Cost for 0 km", "Cost for 10 km", "Gradient"], [[B(c), B(c + 10 * k), B(k)]], reason=f"0 km: ${c}. 10 km: {c} + 10 × {k} = ${c + 10 * k}. The cost goes up ${k} for each km, so the gradient is {k}.", o="O4", d="H")
def r4(r):
    rows = [("Horizontal line", "Not moving"), ("Steep straight line", "Moving fast at a constant speed"), ("Shallow straight line", "Moving slowly at a constant speed"), ("Line going down towards zero", "Returning to the start")]
    return MT("Match each part of a distance–time graph with its meaning.", rows, o="O4", skill="Data")
def r5(r):
    return MC("A bath is filled, someone gets in, then it is emptied. Which feature shows the person getting in?", "a sudden jump up in the water level", [("a horizontal line", "That is when nothing changes."), ("a line going down", "That is emptying."), ("a curve", "")], o="O4", d="H")
def r6(r):
    a, b = r.randint(30, 90), r.randint(30, 90)
    return N(f"A car travels {a} km in 1 hour then {b} km in the next 2 hours. Find its average speed for the whole journey, in km/h (1 d.p.).", round((a + b) / 3, 1), "km/h", units=["km/h"], tol=0.05, reason=f"Total distance {a} + {b} = {a + b} km in 3 hours: {a + b} ÷ 3 = {round((a + b) / 3, 1)} km/h.", o="O4", d="H")
s.core(r1(s.rng), r1(s.rng), r2(s.rng), r3(s.rng), r4(s.rng), r5(s.rng), r6(s.rng),
       EX("Explain why the gradient of a distance–time graph gives the speed.", [("gradient = change in distance ÷ change in time", ["distance ?(÷|/|over|divided by) ?time|change in distance"]), ("distance ÷ time is speed", ["speed"])], "The gradient is change in distance ÷ change in time, and distance ÷ time is speed.", o="O4"))
s.gen("p", 44, r1, r2, r3, r4, r5, r6)
s.gen("a", 8, r1, r6, lambda r: (lambda v1, v2, d_: N(f"Two cars set off towards each other from towns {d_} km apart at {v1} km/h and {v2} km/h. After how many hours do they meet? (2 d.p.)", round(d_ / (v1 + v2), 2), "hours", units=["hours"], tol=0.006, reason=f"They close the gap at {v1} + {v2} = {v1 + v2} km/h, so time = {d_} ÷ {v1 + v2} = {round(d_ / (v1 + v2), 2)} hours.", o="O4", d="VH"))(r.randint(40, 90), r.randint(40, 90), r.randint(100, 400)))

U.mindmap(("Linear functions", "y = mx + c • straight line • tables of values", "O1", "10.1"), ("Plotting", "At least three points • intercepts for 2x + 3y = 12", "O2", "10.2"),
          ("Gradient", "change in y ÷ change in x • parallel lines: same m", "O3", "10.3"), ("Real-life graphs", "Gradient = speed or rate • horizontal = stopped", "O4", "10.4"))
