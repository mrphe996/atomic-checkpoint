# -*- coding: utf-8 -*-
"""Cambridge Lower Secondary Mathematics Stage 7 – lesson notes v3 (all units)."""
NOTES = {}
for _m in ("s7a", "s7b", "s7c", "s7d"):
    NOTES.update(__import__(f"maths_notes_v3.{_m}", fromlist=["NOTES"]).NOTES)
