# -*- coding: utf-8 -*-
"""Cambridge Lower Secondary Mathematics Stage 8 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s8_u01", "s8_u01_book", "s8_u02", "s8_u02_book", "s8_u03", "s8_u03_book", "s8_u04", "s8_u04_book", "s8_u05", "s8_u05_book", "s8_u06", "s8_u06_book", "s8_u07", "s8_u07_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
