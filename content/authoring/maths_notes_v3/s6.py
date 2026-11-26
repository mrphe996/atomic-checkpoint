# -*- coding: utf-8 -*-
"""Cambridge Primary Mathematics Stage 6 – lesson notes v3 (all units)."""
NOTES = {}
for _m in ("s6a", "s6b", "s6c"):
    try: NOTES.update(__import__(f"maths_notes_v3.{_m}", fromlist=["NOTES"]).NOTES)
    except ModuleNotFoundError: pass
