# -*- coding: utf-8 -*-
"""Cambridge Primary Mathematics Stage 4 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s4_u01", "s4_u01_book", "s4_u02", "s4_u02_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
