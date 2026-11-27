# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u02 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(2, "2.1")]["book"] = BK(
    keys=[("a.m. / p.m.", "before midday / after midday"), ("24-hour clock", "hours from 00 to 23")],
    intro=[], examples=[],
    exercise=[
        Ex("Write in 24-hour time.", ("5:20 a.m.", "05:20"), ("5:20 p.m.", "17:20"), ("11:55 p.m.", "23:55")),
        Ex("Write in 12-hour time.", ("15:45", "3:45 p.m."), ("09:10", "9:10 a.m."), ("21:30", "9:30 p.m.")),
        Ex("Convert.", ("4 hours to minutes", "240"), ("3 minutes to seconds", "180"), ("5 weeks to days", "35")),
    ],
    check=["Can I change between 12-hour and 24-hour times and units of time?"], look=[], note=NOTE)

N[(2, "2.2")]["book"] = BK(
    keys=[("timetable", "a table of times"), ("time interval", "how long between two times")],
    intro=[], examples=[],
    exercise=[
        Ex("How long?", ("08:25 to 09:10", "45 min"), ("13:40 to 15:05", "1 h 25 min"), ("10:15 to 12:50", "2 h 35 min")),
        Ex("Make a timetable for your school day and find how long each lesson lasts.", ans="Answers vary.", think=True),
    ],
    check=["Can I read timetables and find time intervals?"], look=[], note=NOTE)
