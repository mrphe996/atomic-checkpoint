# -*- coding: utf-8 -*-
"""Cambridge Lower Secondary Mathematics Stage 7 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s7_u01", "s7_u01_book", "s7_u02", "s7_u02_book", "s7_u03", "s7_u03_book", "s7_u04", "s7_u04_book", "s7_u05", "s7_u05_book", "s7_u06", "s7_u06_book", "s7_u07", "s7_u07_book", "s7_u08", "s7_u08_book", "s7_u09", "s7_u09_book", "s7_u10", "s7_u10_book", "s7_u11", "s7_u11_book", "s7_u12", "s7_u12_book", "s7_u13", "s7_u13_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
