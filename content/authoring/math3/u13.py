# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 13 Time (2) (13.1 Time intervals, 13.2 Timetables).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(13, "Time (2)", "Geometry and measure",
         "Finding how long things take in minutes and hours, finding start and end times, and reading simple timetables and calendars.",
         {"O1": {"code": "3Gt.03", "sec": "13.1", "codeNote": "", "t": "Find time intervals in minutes and hours and work out start and end times."},
          "O2": {"code": "3Gt.04", "sec": "13.2", "codeNote": "", "t": "Read and use simple timetables."}})
def t12(m): h, mm = divmod(m, 60); return f"{(h - 1) % 12 + 1}:{mm:02d}"

s = U.section("13.1", "Time intervals", ["O1"])
s.idea("How long?", ["To find how long something takes, **count on** from the start time to the end time: from 2:40 to 3:15 is 20 minutes to 3:00 and 15 more: **35 minutes**.",
       "Remember: **60 minutes = 1 hour**."], fig={"kind": "clock", "h": 2, "m": 40})
s.check(N("A lesson starts at 10:15 and ends at 11:00. How many minutes long is it?", 45, "minutes", units=["minutes", "min"], o="O1"))
s.check(MC('Before you read on: from 2:30 to 3:15, how long is it?', '45 minutes', [('85 minutes', 'There are 60 minutes in an hour.'), ('1 hour 15 minutes', '2:30 → 3:00 is 30 min, then 15 more.')], o='O1'))
s.mistake("Not 100 minutes", ["From 9:50 to 10:10 is 20 minutes, not 60."])


def i1(r):
    a = r.randint(8 * 60, 15 * 60) // 5 * 5; d = r.randint(2, 11) * 5
    return N(f"A game starts at {t12(a)} and ends at {t12(a + d)}. How many minutes does it last?", d, "minutes", units=["minutes", "min"], o="O1")
def i2(r):
    a = r.randint(8 * 60, 15 * 60) // 5 * 5; d = r.randint(2, 11) * 5
    return S(f"A walk starts at {t12(a)} and takes {d} minutes. When does it end? Write it like 4:35.", [t12(a + d)], o="O1")
def i3(r):
    a = r.randint(8 * 60, 15 * 60) // 5 * 5; d = r.randint(2, 11) * 5
    return S(f"A cake must bake for {d} minutes. It comes out at {t12(a + d)}. When did it go in? Write it like 4:35.", [t12(a)], o="O1", d="H")
def i4(r):
    h, m = r.randint(1, 10), pick(r, [0, 15, 30, 45])
    return S("The clock shows when a film starts. It lasts 1 hour. When does it end? Write it like 4:35.", [f"{h + 1}:{m:02d}"], o="O1", fig={"kind": "clock", "h": h, "m": m})
def i5(r):
    a, b = r.randint(10, 40), r.randint(10, 40)
    return N(f"Homework takes {a} minutes and reading takes {b} minutes. How long altogether?", a + b, "minutes", units=["minutes", "min"], o="O1")
def i6(r):
    m = r.randint(61, 119)
    return TB(f"Write {m} minutes in hours and minutes.", ["Hours", "Minutes"], [[B(1), B(m - 60)]], o="O1")
def i7(r):
    h, m = r.randint(1, 10), pick(r, [0, 30])
    d = pick(r, [15, 30, 45])
    return MC(f"It is {h}:{m:02d}. What time will it be in {d} minutes?", t12(h * 60 + m + d), [t12(h * 60 + m + d + 10), t12(h * 60 + m + d - 10), f"{h}:{d:02d}" if m else t12(h * 60 + d + 60)], o="O1")
def i8(r):
    a, b = r.randint(20, 50), r.randint(20, 50)
    return N(f"Ali ran for {a} minutes and Bea ran for {b} minutes. How many more minutes did the longer runner run?", abs(a - b), "minutes", units=["minutes", "min"], o="O1") if a != b else None


s.std([i4, i6, i1, i2, i5, i7, i3, i8], EX("Explain how to find the time from 3:45 to 4:20.", [("15 minutes to 4:00", "15|4:00|4 o"), ("20 more minutes: 35 minutes", "35")], "Count on from 3:45 to 4:00: 15 minutes. Then from 4:00 to 4:20: 20 minutes. 15 + 20 = 35 minutes.", o="O1"))

s = U.section("13.2", "Timetables", ["O2"])
s.idea("Reading a timetable", ["A **timetable** shows when things happen. Read across a row to find a time.",
       "To find how long a journey takes, subtract the start time from the end time."], table={"head": ["Stop", "Park", "School", "Shops"], "rows": [["Bus 1", "8:00", "8:15", "8:30"], ["Bus 2", "9:00", "9:15", "9:30"]]})
s.check(N("In the timetable, how many minutes does bus 1 take from Park to Shops?", 30, "minutes", units=["minutes", "min"], o="O2"))
s.check(MC('Before you read on: a bus leaves at 9:10 and the journey takes 20 minutes. When does it arrive?', '9:30', [('9:20', 'Add 20 minutes.'), ('11:10', '20 minutes, not 2 hours.')], o='O2'))
s.mistake("Same row", ["Keep your finger on one row so you read the times for the same bus."])
ST = ["Park", "School", "Shops", "Pool"]


def tt(r):
    st = [r.randint(16, 20) * 30]
    for _ in range(3): st.append(st[-1] + r.randint(1, 4) * 5)
    return st


def b1(r):
    t = tt(r); i, j = sorted(r.sample(range(4), 2))
    return N(f"Use the bus timetable. How many minutes from {ST[i]} to {ST[j]}?", t[j] - t[i], "minutes", units=["minutes", "min"], o="O2", data={"head": ["Stop", *ST], "rows": [["Time", *map(t12, t)]]})
def b2(r):
    t = tt(r); k = r.randrange(4)
    return S(f"Use the timetable. When does the bus reach {ST[k]}? Write it like 4:35.", [t12(t[k])], o="O2", data={"head": ["Stop", *ST], "rows": [["Time", *map(t12, t)]]})
def b3(r):
    t = tt(r)
    return N("How long is the whole journey from Park to Pool, in minutes?", t[3] - t[0], "minutes", units=["minutes", "min"], o="O2", data={"head": ["Stop", *ST], "rows": [["Time", *map(t12, t)]]})
def b4(r):
    acts = ["Maths", "Reading", "Break", "Art"]; st = 9 * 60; ts = [st]
    for _ in range(3): ts.append(ts[-1] + pick(r, [15, 30, 45]))
    k = r.randrange(3)
    return N(f"The school timetable shows start times. How long is {acts[k]}, in minutes?", ts[k + 1] - ts[k], "minutes", units=["minutes", "min"], o="O2", data={"head": ["Lesson", *acts], "rows": [["Starts", *map(t12, ts)]]})
def b5(r):
    t = tt(r); arr = t[2] - pick(r, [5, 10])
    return MC(f"Kai gets to the {ST[2]} stop at {t12(arr)}. Will he catch the bus?", "Yes", ["No", "Only if it is late"], o="O2", data={"head": ["Stop", *ST], "rows": [["Time", *map(t12, t)]]})
def b6(r):
    t = tt(r)
    return TB("Use the timetable to complete the table.", ["From", "To", "Minutes"], [[ST[0], ST[1], B(t[1] - t[0])], [ST[1], ST[2], B(t[2] - t[1])]], o="O2", data={"head": ["Stop", *ST], "rows": [["Time", *map(t12, t)]]})
def b7(r):
    t = tt(r); d = pick(r, [30, 60])
    return S(f"The next bus leaves Park {d} minutes after this one. When does it leave Park? Write it like 4:35.", [t12(t[0] + d)], o="O2", d="H", data={"head": ["Stop", *ST], "rows": [["Time", *map(t12, t)]]})
def b8(r):
    t = tt(r)
    return N("A second bus takes 5 minutes longer for the whole route. How long does it take, in minutes?", t[3] - t[0] + 5, "minutes", units=["minutes", "min"], o="O2", d="H", data={"head": ["Stop", *ST], "rows": [["Time", *map(t12, t)]]})


s.std([b1, b2, b3, b4, b5, b6, b7, b8], EX("Explain how to use a timetable to find how long a bus takes between two stops.", [("find the times at both stops on the same row", "both|same row|two times"), ("count on or subtract to find the minutes", "count on|subtract|difference")], "Find the time at the first stop and the time at the second stop in the same row. Count on from one to the other to find how many minutes it takes.", o="O2"))

U.mindmap(("Time intervals", "Count on • 60 minutes = 1 hour", "O1", "13.1"), ("Timetables", "Read across a row • journey times", "O2", "13.2"))
