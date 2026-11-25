# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 2 Time and timetables (2.1 Time, 2.2 Timetables and time intervals).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(2, "Time and Timetables", "Geometry and measure",
         "Reading 12-hour and 24-hour clocks, converting between units of time, and using timetables to find time intervals.",
         {"O1": {"code": "4Gt.01", "sec": "2.1", "codeNote": "", "t": "Read and record time on 12-hour and 24-hour clocks, and convert between units of time."},
          "O2": {"code": "4Gt.02", "sec": "2.2", "codeNote": "", "t": "Use timetables and calendars, and find time intervals."}})
ST = ["Bridge", "Market", "Library", "Station"]

s = U.section("2.1", "Time", ["O1"])
s.idea("12-hour and 24-hour clocks", ["The 24-hour clock counts from **00:00** (midnight) to **23:59**. For afternoon times, add 12 to the hour: 4:20 p.m. = **16:20**.",
       "1 minute = 60 seconds, 1 hour = 60 minutes, 1 day = 24 hours."], fig={"kind": "clock", "h": 4, "m": 20})
s.check(S("Write 3:45 p.m. in 24-hour time.", ["15:45", "1545"], o="O1"))
s.check(MC('Before you read on: what is 15:30 in 12-hour time?', '3:30 p.m.', [('5:30 p.m.', '15 − 12 = 3.'), ('3:30 a.m.', '15:30 is in the afternoon.')], o='O1'))
s.mistake("Morning times", ["9:30 a.m. is 09:30, not 21:30."])


def t1(r):
    t = r.randint(13 * 60, 23 * 60 + 55) // 5 * 5
    return S(f"Write {am(t)} in 24-hour time.", [hm(t), hm(t).replace(":", "")], o="O1")
def t2(r):
    t = r.randint(13 * 60, 23 * 60 + 55) // 5 * 5
    return S(f"Write {hm(t)} as a 12-hour time with a.m. or p.m.", [am(t), am(t).replace(".", ""), am(t).replace(" ", "")], o="O1")
def t3(r):
    h, m = r.randint(1, 12), pick(r, range(0, 60, 5))
    return S("What time does the clock show? Write it like 4:35.", [f"{h}:{m:02d}"], o="O1", fig={"kind": "clock", "h": h, "m": m})
def t4(r):
    h = r.randint(2, 9)
    return TB("Complete the table.", ["Time", "Minutes"], [[f"{h} hours", B(60 * h)], [f"{h} and a half hours", B(60 * h + 30)]], o="O1")
def t5(r):
    m = r.randint(2, 9)
    return N(f"How many seconds are in {m} minutes?", 60 * m, "seconds", units=["seconds", "s"], o="O1")
def t6(r):
    d = r.randint(2, 7)
    return N(f"How many hours are in {d} days?", 24 * d, "hours", units=["hours"], o="O1")
def t7(r):
    m = r.randint(70, 200)
    return S(f"Write {m} minutes in hours and minutes, like 2 h 15 min.", [f"{m // 60} h {m % 60} min", f"{m // 60}h {m % 60}min", f"{m // 60} hours {m % 60} minutes", f"{m // 60} hour {m % 60} minutes"], o="O1", d="H")
def t8(r):
    ev = [("eating breakfast", "07:30"), ("eating dinner", "18:30"), ("school starts", "08:15"), ("watching the sunset", "19:00")]
    a, b = r.sample(ev, 2)
    return MC(f"Which 24-hour time is most likely for {a[0]}?", a[1], [b[1], "03:00"], o="O1")


s.std([t3, t4, t1, t2, t5, t6, t8, t7], EX("Explain how to change 7:10 p.m. into 24-hour time.", [("p.m. times add 12 to the hour", "add 12|\\+ ?12"), ("7 + 12 = 19, so 19:10", "19:10|1910")], "p.m. times are after midday, so add 12 to the hour: 7 + 12 = 19. The time is 19:10.", o="O1"))

s = U.section("2.2", "Timetables and time intervals", ["O2"])
s.idea("Reading a timetable", ["A **timetable** lists times in rows and columns, usually in 24-hour time.",
       "To find a **time interval**, count on: from 10:45 to 12:20 is 15 minutes to 11:00, 1 hour to 12:00 and 20 minutes more: **1 hour 35 minutes**."], table={"head": ["Stop", "Bridge", "Market", "Library"], "rows": [["Bus A", "09:05", "09:25", "09:40"], ["Bus B", "10:05", "10:25", "10:40"]]})
s.check(N("From 09:05 to 09:40, how many minutes?", 35, "minutes", units=["minutes", "min"], o="O2"))
s.check(MC('Before you read on: a bus leaves at 10:40 and arrives at 11:15. How long is the journey?', '35 minutes', [('75 minutes', 'There are 60 minutes in an hour, not 100.'), ('25 minutes', '10:40 → 11:00 is 20 min, then 15 more.')], o='O2'))
s.mistake("Hours are 60 minutes", ["From 10:50 to 11:10 is 20 minutes, not 60."])


def tt(r):
    st = [r.randint(14, 34) * 30]
    for _ in range(3): st.append(st[-1] + r.randint(2, 7) * 5)
    return st


def b1(r):
    t = tt(r); i, j = sorted(r.sample(range(4), 2))
    return N(f"Use the timetable. How many minutes from {ST[i]} to {ST[j]}?", t[j] - t[i], "minutes", units=["minutes", "min"], o="O2", data={"head": ["Stop", *ST], "rows": [["Time", *map(hm, t)]]})
def b2(r):
    a = r.randint(7 * 60, 16 * 60) // 5 * 5; d = r.randint(25, 170) // 5 * 5
    return N(f"A film starts at {hm(a)} and ends at {hm(a + d)}. How many minutes long is it?", d, "minutes", units=["minutes", "min"], o="O2")
def b3(r):
    a = r.randint(7 * 60, 16 * 60) // 5 * 5; d = r.randint(25, 150) // 5 * 5
    return S(f"A train leaves at {hm(a)} and the journey takes {d} minutes. When does it arrive? Use the 24-hour clock.", [hm(a + d), hm(a + d).replace(":", "")], o="O2", d="H")
def b4(r):
    t = tt(r)
    return TB("Use the timetable to complete the table.", ["From", "To", "Minutes"], [[ST[0], ST[1], B(t[1] - t[0])], [ST[1], ST[3], B(t[3] - t[1])]], o="O2", data={"head": ["Stop", *ST], "rows": [["Time", *map(hm, t)]]})
def b5(r):
    t = tt(r); arr = t[2] + pick(r, [-10, -5, 5, 10])
    ok = arr <= t[2]
    return MC(f"Sam reaches the {ST[2]} stop at {hm(arr)}. Will he catch the bus?", "Yes" if ok else "No", ["No" if ok else "Yes"], o="O2", data={"head": ["Stop", *ST], "rows": [["Time", *map(hm, t)]]})
def b6(r):
    d, st = r.randint(1, 28), r.randrange(7)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    k = r.randint(8, 20)
    return S(f"The 1st of the month is a {days[st]}. What day of the week is the {k}th?", [days[(st + k - 1) % 7]], o="O2", d="H")
def b7(r):
    a, b = r.randint(15, 50), r.randint(15, 50)
    return N(f"Swimming takes {a} minutes and tennis takes {b} minutes. How long is that in total, in minutes?", a + b, "minutes", units=["minutes", "min"], o="O2")
def b8(r):
    w = r.randint(2, 8)
    return N(f"A holiday lasts {w} weeks and 3 days. How many days is that?", 7 * w + 3, "days", units=["days"], o="O2")


s.std([b1, b4, b2, b3, b5, b7, b6, b8], EX("Explain how to find the time from 10:40 to 12:05.", [("20 minutes to 11:00", "20|11:00"), ("1 hour to 12:00 and 5 more: 1 hour 25 minutes", "1 h(our)? ?25|85")], "Count on: 20 minutes from 10:40 to 11:00, 1 hour to 12:00, then 5 minutes to 12:05. Total 1 hour 25 minutes.", o="O2"))

U.mindmap(("Clocks", "12-hour and 24-hour • units of time", "O1", "2.1"), ("Timetables", "Read rows and columns • time intervals", "O2", "2.2"))
