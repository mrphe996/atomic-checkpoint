# -*- coding: utf-8 -*-
"""Cambridge Primary Mathematics Stage 6 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s6_u01", "s6_u01_book", "s6_u02", "s6_u02_book", "s6_u03", "s6_u03_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
