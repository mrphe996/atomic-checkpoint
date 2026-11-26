# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 8 Time (8.1 Telling the time, 8.2 Days, weeks, months and years).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(8, "Time", "Geometry and measure",
         "Reading analogue and digital clocks to five minutes, a.m. and p.m., and units of time: seconds, minutes, hours, days, weeks, months and years.",
         {"O1": {"code": "3Gt.01", "sec": "8.1", "codeNote": "", "t": "Read and record time to five minutes on analogue and digital 12-hour clocks, using a.m. and p.m."},
          "O2": {"code": "3Gt.02", "sec": "8.2", "codeNote": "", "t": "Know the units of time and use a calendar."}})
MON = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MIN = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

s = U.section("8.1", "Telling the time", ["O1"])
s.idea("Analogue and digital", ["On an **analogue clock** the short hand shows the **hour** and the long hand shows the **minutes**. Each number on the clock is **5 minutes** for the long hand.",
       "A **digital clock** shows 3:45, which means 45 minutes past 3. **a.m.** is morning; **p.m.** is afternoon and evening."], fig={"kind": "clock", "h": 3, "m": 45})
s.check(S("What time is half past 7 on a digital clock?", ["7:30"], o="O1"))
s.check(MC('Before you read on: the minute hand points at 6. How many minutes past the hour is it?', '30 minutes', [('6 minutes', 'Each number on the clock is 5 minutes.'), ('60 minutes', '6 × 5 = 30.')], o='O1'))
s.mistake("Long hand, short hand", ["The long hand shows minutes, not hours."])


def c1(r):
    h, m = r.randint(1, 12), pick(r, MIN)
    return S("What time does the clock show? Write it like 4:35.", [f"{h}:{m:02d}"], o="O1", fig={"kind": "clock", "h": h, "m": m})
def c2(r):
    h = r.randint(1, 12); m, w = pick(r, [(0, "o'clock"), (30, "half past"), (15, "quarter past"), (45, "quarter to")])
    txt = f"{h} o'clock" if m == 0 else f"{w} {h if m != 45 else h % 12 + 1}"
    hh = h
    return S(f"Write {txt} as a digital time, like 4:35.", [f"{hh}:{m:02d}"], o="O1")
def c3(r):
    h, m = r.randint(1, 12), pick(r, MIN[1:])
    return N(f"The long hand points to the {m // 5}. How many minutes past the hour is that?", m, "minutes", units=["minutes", "min"], o="O1")
def c4(r):
    ev = [("eating breakfast", "a.m."), ("eating dinner", "p.m."), ("going to school", "a.m."), ("going to bed", "p.m."), ("watching the sunset", "p.m."), ("waking up", "a.m.")]
    return GD("Is each event usually a.m. or p.m.?", "a.m. or p.m.", r.sample(ev, 4), o="O1", extra=["a.m.", "p.m."])
def c5(r):
    h, m = r.randint(1, 11), pick(r, MIN)
    return S(f"What time is 1 hour after {h}:{m:02d}?", [f"{h + 1}:{m:02d}"], o="O1")
def c6(r):
    h, m = r.randint(1, 12), pick(r, [0, 15, 30])
    return S(f"What time is 15 minutes after {h}:{m:02d}?", [f"{h}:{m + 15:02d}"], o="O1", fig={"kind": "clock", "h": h, "m": m})
def c7(r):
    h = r.randint(1, 12); m = pick(r, MIN[1:])
    return MC("Which time does the clock show?", f"{h}:{m:02d}", [f"{m // 5}:{h * 5 % 60:02d}" if m // 5 != h else f"{h % 12 + 1}:{m:02d}", f"{h % 12 + 1}:{m:02d}"], o="O1", fig={"kind": "clock", "h": h, "m": m}, d="H")
def c8(r):
    a, d = r.randint(1, 10), pick(r, [15, 20, 30, 45])
    return N(f"A TV show starts at {a}:00 and ends at {a}:{d:02d}. How many minutes long is it?", d, "minutes", units=["minutes", "min"], o="O1")


s.std([c1, c6, c2, c3, c4, c5, c8, c7], EX("Explain how to read the minutes on an analogue clock.", [("look at the long hand", "long hand|minute hand"), ("count in fives from the 12", "fives|5|count")], "Look at the long hand. Each number it passes is 5 minutes, so count in fives from the 12 to where it points.", o="O1"))

s = U.section("8.2", "Days, weeks, months and years", ["O2"])
s.idea("Units of time", ["60 seconds = 1 minute, 60 minutes = 1 hour, 24 hours = 1 day, **7 days = 1 week**, 12 months = 1 year.",
       "A **calendar** shows the days of a month. Months have 28, 29, 30 or 31 days."], table={"head": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "rows": [["1", "2", "3", "4", "5", "6", "7"], ["8", "9", "10", "11", "12", "13", "14"]]})
s.check(N("How many days are in 2 weeks?", 14, "days", units=["days"], o="O2"))
s.check(MC('Before you read on: how many days are in 2 weeks?', '14', [('10', 'A week has 7 days.'), ('12', '7 + 7 = 14.')], o='O2'))
s.mistake("Months are not all the same", ["February is shorter than other months."])


def d1(r):
    k = r.randrange(7); n = r.randint(1, 6)
    return S(f"Today is {DAY[k]}. What day will it be in {n} day{'s' if n > 1 else ''}?", [DAY[(k + n) % 7]], o="O2")
def d2(r):
    k = r.randrange(12); n = r.randint(1, 5)
    return S(f"It is {MON[k]}. What month will it be in {n} month{'s' if n > 1 else ''}?", [MON[(k + n) % 12]], o="O2")
def d3(r):
    w = r.randint(2, 6)
    return N(f"How many days are in {w} weeks?", 7 * w, "days", units=["days"], o="O2")
def d4(r):
    us = r.sample([("minutes in an hour", 60), ("seconds in a minute", 60), ("hours in a day", 24), ("days in a week", 7), ("months in a year", 12)], 3)
    return TB("Complete the table.", ["Fact", "Number"], [[t, B(v)] for t, v in us], o="O2")
def d5(r):
    st = r.randrange(7); d = r.randint(1, 28)
    rows = [[str(i + 1 + 7 * w) if 1 <= i + 1 + 7 * w <= 28 else "" for i in range(7)] for w in range(4)]
    return S(f"Use the calendar. Which day of the week is the {d}th?", [DAY[(d - 1) % 7]], o="O2", data={"head": [x[:3] for x in DAY], "rows": rows})
def d6(r):
    return OD("Put these in order, shortest first.", ["1 second", "1 minute", "1 hour", "1 day", "1 week"], o="O2")
def d7(r):
    m = pick(r, MON)
    dd = {"February": "28 or 29"}.get(m, "30" if m in ("April", "June", "September", "November") else "31")
    return MC(f"How many days are in {m}?", dd, [x for x in ["28 or 29", "30", "31"] if x != dd], o="O2", d="H")
def d8(r):
    h = r.randint(2, 4)
    return N(f"How many minutes are in {h} hours?", 60 * h, "minutes", units=["minutes", "min"], o="O2", d="H")


s.std([d4, d5, d1, d2, d3, d6, d7, d8], EX("Explain how to find what day it is 8 days after Monday.", [("7 days later is Monday again", "7 days|a week|Monday again"), ("one more day is Tuesday", "Tuesday")], "7 days is one week, so 7 days after Monday is Monday again. One more day makes it Tuesday.", o="O2"))

U.mindmap(("Clocks", "Hour hand • minute hand • a.m. and p.m.", "O1", "8.1"), ("Units of time", "7 days = 1 week • 12 months = 1 year", "O2", "8.2"))
