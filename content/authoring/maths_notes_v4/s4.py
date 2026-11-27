# -*- coding: utf-8 -*-
"""Cambridge Primary Mathematics Stage 4 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s4_u01", "s4_u01_book", "s4_u02", "s4_u02_book", "s4_u03", "s4_u03_book", "s4_u04", "s4_u04_book", "s4_u05", "s4_u05_book", "s4_u06", "s4_u06_book", "s4_u07", "s4_u07_book", "s4_u08", "s4_u08_book", "s4_u09", "s4_u09_book", "s4_u10", "s4_u10_book", "s4_u11", "s4_u11_book", "s4_u12", "s4_u12_book", "s4_u13", "s4_u13_book", "s4_u14", "s4_u14_book", "s4_u15", "s4_u15_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
