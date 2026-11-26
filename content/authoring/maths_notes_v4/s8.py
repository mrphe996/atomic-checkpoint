# -*- coding: utf-8 -*-
"""Cambridge Lower Secondary Mathematics Stage 8 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s8_u01", "s8_u01_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
