# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 16 Time (16.1 Time intervals, 16.2 Time zones).
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(16, "Time", "Geometry and measure",
         "Finding time intervals in hours and minutes using 12-hour and 24-hour clocks and timetables, and comparing times in different time zones.",
         {"O1": {"code": "5Gt.01", "sec": "16.1", "codeNote": "", "t": "Find time intervals in seconds, minutes and hours, using 12- and 24-hour clocks and timetables."},
          "O2": {"code": "5Gt.02", "sec": "16.2", "codeNote": "", "t": "Understand time zones and work out the time in another place."}})
CITY = [("London", 0), ("Dubai", 4), ("Bangkok", 7), ("Hanoi", 7), ("Tokyo", 9), ("Sydney", 11), ("New York", -5), ("Cairo", 2), ("Nairobi", 3)]

s = U.section("16.1", "Time intervals", ["O1"])
s.idea("Counting on", ["To find how long something takes, **count on** in steps to the next hour, then whole hours, then the minutes left.",
       "From 10:35 to 13:10: 25 min to 11:00, 2 hours to 13:00, 10 min to 13:10 → **2 hours 35 minutes**."], fig={"kind": "clock", "h": 10, "m": 35})
s.check(N("A lesson starts at 09:15 and ends at 10:00. How many minutes long is it?", 45, "minutes", units=["minutes", "min"], o="O1"))
s.mistake("60, not 100", ["There are 60 minutes in an hour, so 1:45 + 30 minutes is 2:15, not 1:75."])


def t1(r):
    a = r.randint(7 * 60, 16 * 60) // 5 * 5; d = r.randint(15, 180) // 5 * 5
    return N(f"A film starts at {hm(a)} and ends at {hm(a + d)}. How many minutes long is it?", d, "minutes", units=["minutes", "min"], o="O1")
def t2(r):
    h, m = r.randint(1, 12), pick(r, [0, 10, 15, 20, 30, 40, 45, 50])
    return S("What time does the clock show? Write it like 4:35.", [f"{h}:{m:02d}"], o="O1", fig={"kind": "clock", "h": h, "m": m})
def t3(r):
    st = [r.randint(8 * 60, 10 * 60) // 5 * 5]
    for _ in range(3): st.append(st[-1] + r.randint(3, 10) * 5)
    names = ["Hill", "Park", "Shops", "School"]; i, j = sorted(r.sample(range(4), 2))
    return N(f"Use the bus timetable. How many minutes does the bus take from {names[i]} to {names[j]}?", st[j] - st[i], "minutes", units=["minutes", "min"], o="O1", data={"head": ["Stop", *names], "rows": [["Time", *map(hm, st)]]})
def t4(r):
    t = r.randint(13 * 60, 22 * 60) // 5 * 5
    return S(f"Write {am(t)} in 24-hour time.", [hm(t), hm(t).replace(":", "")], o="O1")
def t5(r):
    m = r.randint(70, 200)
    return TB(f"Change {m} minutes into hours and minutes.", ["Hours", "Minutes"], [[B(m // 60), B(m % 60)]], o="O1")
def t6(r):
    a = r.randint(8 * 60, 18 * 60) // 5 * 5; d = r.randint(35, 150) // 5 * 5
    return S(f"A journey starts at {hm(a)} and takes {d} minutes. When does it end? Use the 24-hour clock.", [hm(a + d), hm(a + d).replace(":", "")], o="O1", d="H")
def t7(r):
    m = r.randint(2, 9)
    return N(f"How many seconds are there in {m} minutes?", 60 * m, "seconds", units=["seconds", "s"], o="O1")
def t8(r):
    a, b = r.randint(20, 59), r.randint(20, 59)
    return N(f"Ali ran a race in 1 minute {a} seconds. Bea took {b} seconds longer. How many seconds did Bea take?", 60 + a + b, "seconds", units=["seconds", "s"], o="O1", d="H")


s.std([t2, t3, t1, t4, t5, t7, t6, t8], EX("Explain how to find the time from 08:50 to 10:15.", [("10 minutes to 09:00", "10 min|09:00|9:00"), ("1 hour to 10:00 and 15 more: 1 h 25 min", "1 h(our)? ?25|85 min|25")], "Count on: 10 minutes from 08:50 to 09:00, 1 hour to 10:00, then 15 minutes to 10:15. Total 1 hour 25 minutes.", o="O1"))

s = U.section("16.2", "Time zones", ["O2"])
s.idea("Different times around the world", ["The world is split into **time zones**. When it is midday in London it is **7 p.m. in Hanoi** (7 hours ahead) and **7 a.m. in New York** (5 hours behind).",
       "To find the time in another place, **add** hours if it is ahead and **subtract** hours if it is behind."], table={"head": ["City", "London", "Cairo", "Dubai", "Hanoi", "Tokyo", "New York"], "rows": [["Hours ahead of London", "0", "+2", "+4", "+7", "+9", "−5"]]})
s.check(N("Tokyo is 9 hours ahead of London. When it is 08:00 in London, what hour is it in Tokyo? Give the hour as a number from 0 to 23.", 17, o="O2"))
s.mistake("Ahead or behind?", ["Ahead means later in the day: add hours. Behind means earlier: subtract."])


def z1(r):
    c, d = pick(r, [x for x in CITY if x[1] > 0]); h = r.randint(0, 23 - d)
    return N(f"{c} is {d} hours ahead of London. When it is {h:02d}:00 in London, what hour is it in {c}? Give a number from 0 to 23.", h + d, o="O2", data={"head": ["City", "London", c], "rows": [["Time", f"{h:02d}:00", "?"]]})
def z2(r):
    h = r.randint(6, 18)
    return N(f"New York is 5 hours behind London. When it is {h:02d}:00 in London, what hour is it in New York? Give a number from 0 to 23.", h - 5, o="O2")
def z3(r):
    cs = r.sample([x for x in CITY if x[0] != "London"], 3); h = 12
    return TB("When it is 12:00 in London, what hour is it in each city? Use the table of hours ahead.", ["City", "Hour (0–23)"], [[c, B(h + d)] for c, d in cs], o="O2", data={"head": ["City", *[c for c, _ in cs]], "rows": [["Hours ahead of London", *[("+" if d >= 0 else "−") + str(abs(d)) for _, d in cs]]]})
def z4(r):
    (a, da), (b, db) = r.sample([x for x in CITY if x[0] not in ("Hanoi",)], 2)
    return N(f"How many hours is the time difference between {a} and {b}?", abs(da - db), "hours", units=["hours"], o="O2", d="H")
def z5(r):
    return MC("Bangkok is 7 hours ahead of London. Which is true?", "It is later in the day in Bangkok", ["It is earlier in Bangkok", "They have the same time", "Bangkok is 7 hours behind"], o="O2")
def z6(r):
    h = r.randint(1, 10)
    return N(f"It is {h:02d}:00 in Hanoi. Hanoi is 7 hours ahead of London. What hour is it in London? Give a number from 0 to 23.", (h - 7) % 24, o="O2", d="H")
def z7(r):
    c, d = pick(r, [x for x in CITY if x[1] > 0]); h = r.randint(8, 12)
    return N(f"A video call starts at {h:02d}:00 in London. Someone joins from {c} ({d} hours ahead). What hour is it for them?", (h + d) % 24, o="O2")
def z8(r):
    f = r.randint(2, 6); dep = r.randint(8, 14)
    return N(f"A plane leaves London at {dep:02d}:00 and flies for {f} hours to Cairo, which is 2 hours ahead. What hour is it in Cairo when it lands?", dep + f + 2, o="O2", d="H")


s.std([z3, z1, z2, z4, z5, z7, z6, z8], EX("Explain how to find the time in Dubai when it is 09:00 in London.", [("Dubai is 4 hours ahead", "4 hours|ahead"), ("add 4: 13:00", "13:00|1 ?p\\.?m|13")], "Dubai is 4 hours ahead of London, so add 4 hours: 09:00 + 4 hours = 13:00 (1 p.m.).", o="O2"))

U.mindmap(("Time intervals", "Count on • 60 minutes in an hour • timetables", "O1", "16.1"), ("Time zones", "Ahead: add • behind: subtract", "O2", "16.2"))
