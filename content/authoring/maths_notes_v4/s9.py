# -*- coding: utf-8 -*-
"""Cambridge Lower Secondary Mathematics Stage 9 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s9_u01", "s9_u01_book", "s9_u02", "s9_u02_book", "s9_u03", "s9_u03_book", "s9_u04", "s9_u04_book", "s9_u05", "s9_u05_book", "s9_u06", "s9_u06_book", "s9_u07", "s9_u07_book", "s9_u08", "s9_u08_book", "s9_u09", "s9_u09_book", "s9_u10", "s9_u10_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
