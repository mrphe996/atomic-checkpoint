# -*- coding: utf-8 -*-
"""Cambridge Primary Mathematics Stage 5 – lesson notes v3 (all units)."""
NOTES = {}
for _m in ("s5a", "s5b"):
    NOTES.update(__import__(f"maths_notes_v3.{_m}", fromlist=["NOTES"]).NOTES)
