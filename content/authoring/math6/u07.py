# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 7 Exploring measures (7.1 Rectangles and triangles, 7.2 Time).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(7, "Exploring Measures", "Geometry and measure",
         "Area and perimeter of rectangles, compound shapes and right-angled triangles, and working with time, including the 24-hour clock and timetables.",
         {"O1": {"code": "6Gg.04", "sec": "7.1", "codeNote": "", "t": "Find the area and perimeter of rectangles and compound shapes, and the area of right-angled triangles."},
          "O2": {"code": "6Gt.01", "sec": "7.2", "codeNote": "", "t": "Use 12- and 24-hour clocks, convert between units of time and find time intervals, including with timetables."}})
RECT = lambda l, w: {"kind": "shape", "pts": [[0, 0], [l, 0], [l, w], [0, w]], "s": [f"{l} cm", f"{w} cm", "", ""], "right": [0, 1, 2, 3]}
def hm(t): return f"{t // 60:02d}:{t % 60:02d}"
def am(t):
    h, m = divmod(t, 60); return f"{(h - 1) % 12 + 1}:{m:02d} {'a.m.' if h < 12 else 'p.m.'}"


s = U.section("7.1", "Rectangles and triangles", ["O1"])
s.idea("Area and perimeter", ["The **perimeter** is the distance all the way round. The **area** is the space inside, measured in square units such as **cm²**.",
       "For a rectangle: **area = length × width** and perimeter = 2 × (length + width)."], fig=RECT(7, 4))
s.check(N("A rectangle is 9 cm by 5 cm. Find its area.", 45, "cm²", units=["cm²"], o="O1"))
s.idea("Right-angled triangles", ["A right-angled triangle is **half a rectangle**. Area = (base × height) ÷ 2."], fig={"kind": "shape", "pts": [[0, 0], [8, 0], [0, 5]], "s": ["8 cm", "", "5 cm"], "right": [0]})
s.idea("Compound shapes", ["Split an L-shape into two rectangles, find each area, then add."])
s.idea("Why a triangle is half a rectangle", ["Draw a rectangle around a right-angled triangle: the triangle is exactly half of it. So the area of a triangle is half of base × height.",
       "Area is measured in square units (cm²) because it counts squares."])
s.check(MC("Before you read on: a rectangle is 6 cm by 4 cm. What is the area of the triangle made by cutting it along a diagonal?", "12 cm²", [("24 cm²", "That is the whole rectangle."), ("10 cm²", "That adds the sides.")], o="O1"))
s.mistake("cm or cm²", ["Perimeter is a length (cm); area is measured in square units (cm²)."])


def a1(r):
    l, w = r.randint(3, 15), r.randint(2, 12)
    return N("Find the area of the rectangle.", l * w, "cm²", units=["cm²"], o="O1", fig=RECT(l, w))
def a2(r):
    l, w = r.randint(3, 15), r.randint(2, 12)
    return N("Find the perimeter of the rectangle.", 2 * (l + w), "cm", units=["cm"], o="O1", fig=RECT(l, w))
def a3(r):
    b, h = r.randint(2, 12) * 2, r.randint(3, 12)
    return N("Find the area of the right-angled triangle.", b * h // 2, "cm²", units=["cm²"], o="O1", fig={"kind": "shape", "pts": [[0, 0], [b, 0], [0, h]], "s": [f"{b} cm", "", f"{h} cm"], "right": [0]})
def a4(r):
    A, B_, c, d = r.randint(8, 14), r.randint(6, 10), r.randint(3, 6), r.randint(2, 4)
    if c >= A or d >= B_: return None
    area = A * B_ - c * d
    return N("Find the area of the L-shape. All corners are right angles.", area, "cm²", units=["cm²"], o="O1", d="H", fig={"kind": "shape", "pts": [[0, 0], [A, 0], [A, B_ - d], [A - c, B_ - d], [A - c, B_], [0, B_]], "s": [f"{A} cm", f"{B_ - d} cm", f"{c} cm", f"{d} cm", f"{A - c} cm", f"{B_} cm"]})
def a5(r):
    w, ar = r.randint(2, 9), r.randint(3, 12)
    return N(f"A rectangle has area {w * ar} cm² and width {w} cm. Find its length.", ar, "cm", units=["cm"], o="O1")
def a6(r):
    s_ = r.randint(3, 12)
    return N(f"A square has perimeter {4 * s_} cm. Find its area.", s_ * s_, "cm²", units=["cm²"], o="O1", d="H")
def a7(r):
    l, w = r.randint(3, 12), r.randint(2, 10)
    return TB("Complete the table for rectangles.", ["Length", "Width", "Area", "Perimeter"], [[f"{l} cm", f"{w} cm", B(l * w), B(2 * (l + w))]], o="O1")
def a8(r):
    l, w, t = r.randint(4, 10), r.randint(3, 8), pick(r, [2, 4, 5])
    return N(f"A floor is {l} m by {w} m. Tiles cost ${t} for each square metre. How much do the tiles cost?", l * w * t, "$", units=["$", "dollars"], o="O1", d="H")
def a9(r):
    s_ = r.randint(4, 12)
    return N(f"A square of side {s_} cm is cut in half along a diagonal. What is the area of one triangle?", s_ * s_ / 2, "cm²", units=["cm²"], o="O1")


def g1_1(r):
    a = r.randint(2, 9); b = r.randint(2, 9)
    pairs = [(x, a * b // x) for x in range(1, a * b + 1) if (a * b) % x == 0 and x <= a * b // x]
    return MC(f"A rectangle has area {a * b} cm². Which could be its length and width?", f"{pairs[-1][1]} cm and {pairs[-1][0]} cm", [(f"{a * b // 2} cm and 2 cm" if (a * b) % 2 else f"{a * b // 2 + 1} cm and 2 cm", "Multiply the length and width to check."), (f"{a + b} cm and 1 cm" if a + b != a * b else f"{a * b + 1} cm and 1 cm", "Length × width must equal the area.")], o="O1", d="H",
              reason=f"{pairs[-1][1]} × {pairs[-1][0]} = {a * b}.")


s.std([a1, a3, a2, a5, a7, a9, a6, a4, a8], EX("Explain why the area of a right-angled triangle is half of base × height.", [("two copies make a rectangle", "rectangle|two|double"), ("the rectangle's area is base × height, so the triangle is half", "half|÷ ?2")], "Two identical right-angled triangles fit together to make a rectangle with area base × height. So one triangle has half that area.", o="O1"), adv=[a4, a6, a8, a5],
      deep=[g1_1])

s = U.section("7.2", "Time", ["O2"])
s.idea("12- and 24-hour clocks", ["The 24-hour clock counts hours from 00:00 (midnight) to 23:59. Afternoon times add 12: 3:45 p.m. = **15:45**.",
       "1 hour = 60 minutes, 1 minute = 60 seconds, 1 day = 24 hours."], fig={"kind": "clock", "h": 3, "m": 45})
s.check(S("Write 7:20 p.m. in 24-hour time.", ["19:20", "1920"], o="O2"))
s.idea("Time intervals", ["Count on in steps: from 09:45 to 11:20 → 15 minutes to 10:00, 1 hour to 11:00, 20 minutes to 11:20: **1 hour 35 minutes**."])
s.check(MC("Before you read on: a film starts at 18:45 and lasts 1 hour 30 minutes. When does it end?", "20:15", [("19:75", "There are only 60 minutes in an hour."), ("20:45", "That adds 2 hours.")], o="O2"))
s.mistake("Not 100 minutes", ["Time does not work in hundreds: 1:50 + 20 minutes is 2:10, not 1:70."])


def t1(r):
    t = r.randint(13 * 60, 23 * 60 + 59)
    return S(f"Write {am(t)} in 24-hour time.", [hm(t), hm(t).replace(":", "")], o="O2")
def t2(r):
    t = r.randint(13 * 60, 23 * 60 + 59)
    return S(f"Write {hm(t)} in 12-hour time using a.m. or p.m.", [am(t), am(t).replace(".", ""), am(t).replace("p.m.", "pm")], o="O2")
def t3(r):
    a = r.randint(6 * 60, 15 * 60) // 5 * 5; d = r.randint(25, 200) // 5 * 5
    return N(f"A film starts at {hm(a)} and ends at {hm(a + d)}. How many minutes long is it?", d, "minutes", units=["minutes", "min"], o="O2")
def t4(r):
    h, m = r.randint(1, 12), pick(r, [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
    return S("What time does the clock show? Write it like 4:35.", [f"{h}:{m:02d}"], o="O2", fig={"kind": "clock", "h": h, "m": m})
def t5(r):
    st = [r.randint(7 * 60, 9 * 60) // 5 * 5]; gaps = [r.randint(3, 9) * 5 for _ in range(3)]
    for g in gaps: st.append(st[-1] + g)
    names = ["Park", "Market", "School", "Station"]; i, j = sorted(r.sample(range(4), 2))
    return N(f"The bus timetable is shown. How many minutes does the bus take from {names[i]} to {names[j]}?", st[j] - st[i], "minutes", units=["minutes", "min"], o="O2", data={"head": ["Stop", *names], "rows": [["Time", *map(hm, st)]]})
def t6(r):
    h = r.randint(2, 9)
    return TB("Complete the table.", ["Hours", "Minutes"], [[str(h), B(60 * h)], [f"{h} and a half", B(60 * h + 30)]], o="O2")
def t7(r):
    m = r.randint(70, 250)
    return S(f"Write {m} minutes in hours and minutes, like 2 h 15 min.", [f"{m // 60} h {m % 60} min", f"{m // 60}h {m % 60}min", f"{m // 60} hours {m % 60} minutes", f"{m // 60} hour {m % 60} minutes"], o="O2")
def t8(r):
    a = r.randint(8 * 60, 18 * 60) // 5 * 5; d = r.randint(40, 190) // 5 * 5
    return S(f"A train leaves at {hm(a)}. The journey takes {d // 60} h {d % 60} min. When does it arrive? Use the 24-hour clock.", [hm(a + d), hm(a + d).replace(":", "")], o="O2", d="H")
def t9(r):
    d = r.randint(2, 6)
    return N(f"How many hours are there in {d} days?", 24 * d, "hours", units=["hours"], o="O2")


def g2_1(r):
    h, m = r.randint(9, 16), r.choice([10, 25, 40, 50]); dur = r.choice([35, 50, 75, 95])
    e = h * 60 + m + dur
    return MC(f"A lesson starts at {h:02d}:{m:02d} and lasts {dur} minutes. When does it end?", f"{e // 60:02d}:{e % 60:02d}", [(f"{h:02d}:{m + dur}" if m + dur >= 60 else f"{h + 1:02d}:{m + dur:02d}", "There are 60 minutes in an hour, not 100."), (f"{(e + 10) // 60:02d}:{(e + 10) % 60:02d}", "Count on carefully to the next hour.")], o="O2", d="H",
              reason=f"{h:02d}:{m:02d} + {dur} minutes = {e // 60:02d}:{e % 60:02d}.") if f"{h:02d}:{m + dur}" != f"{e // 60:02d}:{e % 60:02d}" else None


s.std([t4, t5, t1, t2, t3, t6, t7, t9, t8], EX("Explain how to find the time from 10:40 to 12:15.", [("20 minutes to 11:00", "20 min|11:00"), ("1 hour to 12:00 and 15 minutes more: 1 h 35 min", "1 h(our)? ?35|95 min|35")], "Count on: 20 minutes from 10:40 to 11:00, 1 hour to 12:00, then 15 minutes to 12:15. Total 1 hour 35 minutes.", o="O2"), adv=[t8, t3, t5, t7],
      deep=[g2_1])

U.mindmap(("Area", "Rectangle l × w • triangle (b × h) ÷ 2 • compound shapes", "O1", "7.1"), ("Perimeter", "Distance all the way round", "O1", "7.1"), ("Time", "24-hour clock • intervals • timetables", "O2", "7.2"))
