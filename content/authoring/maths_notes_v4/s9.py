# -*- coding: utf-8 -*-
"""Cambridge Lower Secondary Mathematics Stage 9 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s9_u01", "s9_u01_book", "s9_u02", "s9_u02_book", "s9_u03", "s9_u03_book", "s9_u04", "s9_u04_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
