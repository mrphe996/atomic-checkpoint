# -*- coding: utf-8 -*-
"""Cambridge Lower Secondary Mathematics Stage 9 – lesson notes v3 (all units)."""
NOTES = {}
for _m in ("s9a", "s9b", "s9c"):
    NOTES.update(__import__(f"maths_notes_v3.{_m}", fromlist=["NOTES"]).NOTES)
