# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u16 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(16, "16.1")]["book"] = BK(
    keys=[("24-hour clock", "hours numbered 00 to 23"), ("time interval", "how long between two times")],
    intro=[], examples=[],
    exercise=[
        Ex("Write in 24-hour time.", ("6:20 a.m.", "06:20"), ("8:45 p.m.", "20:45"), ("12:10 p.m.", "12:10")),
        Ex("How long?", ("07:50 to 09:15", "1 h 25 min"), ("11:40 to 14:05", "2 h 25 min"), ("10:30 a.m. to 4:10 p.m.", "5 h 40 min")),
        Ex("Find a real bus or train timetable and work out three journey times.", ans="Answers vary.", think=True),
    ],
    check=["Can I find time intervals using 12- and 24-hour clocks?"], look=[], note=NOTE)

N[(16, "16.2")]["book"] = BK(
    keys=[("time zone", "a region that uses the same clock time"), ("ahead / behind", "later / earlier clock time")],
    intro=[], examples=[],
    exercise=[
        Ex("London is 11:00. What time is it in…", ("Hanoi (+7 h)", "18:00"), ("Dubai (+4 h)", "15:00"), ("New York (−5 h)", "06:00")),
        Ex("Hanoi is 03:00 on Saturday. What time and day is it in London?", ans="20:00 on Friday"),
    ],
    check=["Can I work out the time in another time zone?"], look=[], note=NOTE)
