# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u08 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(8, "8.1")]["book"] = BK(
    keys=[("a.m.", "midnight to midday"), ("p.m.", "midday to midnight")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the time in digits.", ("quarter past 6", "6:15"), ("twenty to 3", "2:40"), ("five past 12", "12:05"), ("half past 10", "10:30")),
        Ex("Draw clock faces showing 4:25 and 8:50.", ans="Check the hands.", think=True),
    ],
    check=["Can I read and write the time to 5 minutes, using a.m. and p.m.?"], look=[], note=NOTE)

N[(8, "8.2")]["book"] = BK(
    keys=[("calendar", "a chart of days, weeks and months"), ("leap year", "a year with 366 days")],
    intro=[], examples=[],
    exercise=[
        Ex("Convert.", ("3 weeks to days", "21"), ("2 hours to minutes", "120"), ("2 years to months", "24")),
        Ex("Days in…", ("April", "30"), ("July", "31"), ("February (not a leap year)", "28")),
    ],
    check=["Can I use units of time and a calendar?"], look=[], note=NOTE)
