# -*- coding: utf-8 -*-
"""Cambridge Primary Mathematics Stage 5 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s5_u01", "s5_u01_book", "s5_u02", "s5_u02_book", "s5_u03", "s5_u03_book", "s5_u04", "s5_u04_book", "s5_u05", "s5_u05_book", "s5_u06", "s5_u06_book", "s5_u07", "s5_u07_book", "s5_u08", "s5_u08_book", "s5_u09", "s5_u09_book", "s5_u10", "s5_u10_book", "s5_u11", "s5_u11_book", "s5_u12", "s5_u12_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
