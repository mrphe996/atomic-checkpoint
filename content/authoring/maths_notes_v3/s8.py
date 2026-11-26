# -*- coding: utf-8 -*-
"""Cambridge Lower Secondary Mathematics Stage 8 – lesson notes v3 (all units)."""
NOTES = {}
for _m in ("s8a", "s8b", "s8c", "s8d"):
    NOTES.update(__import__(f"maths_notes_v3.{_m}", fromlist=["NOTES"]).NOTES)
