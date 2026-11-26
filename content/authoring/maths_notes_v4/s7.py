# -*- coding: utf-8 -*-
"""Cambridge Lower Secondary Mathematics Stage 7 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s7_u09", "s7_u09_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
