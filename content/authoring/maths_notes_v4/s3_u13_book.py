# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u13 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(13, "13.1")]["book"] = BK(
    keys=[("time interval", "how long between two times")],
    intro=[], examples=[],
    exercise=[
        Ex("How long?", ("2:10 to 2:45", "35 minutes"), ("6:40 to 7:20", "40 minutes"), ("9:00 to 11:30", "2 hours 30 minutes")),
        Ex("Find the end time.", ("start 3:25, 30 minutes", "3:55"), ("start 10:45, 25 minutes", "11:10")),
    ],
    check=["Can I find time intervals and start and end times?"], look=[], note=NOTE)

N[(13, "13.2")]["book"] = BK(
    keys=[("timetable", "a list of what happens and when")],
    intro=[], examples=[],
    exercise=[
        Ex("Make a timetable for your Saturday with start and end times. How long is each activity?", ans="Answers vary.", think=True),
        Ex("A film starts at 4:20 and ends at 5:55. How long is it?", ans="1 hour 35 minutes"),
    ],
    check=["Can I read and use simple timetables?"], look=[], note=NOTE)
