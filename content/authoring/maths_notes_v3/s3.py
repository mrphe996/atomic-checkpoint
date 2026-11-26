# -*- coding: utf-8 -*-
"""Cambridge Primary Mathematics Stage 3 – lesson notes v3 (all units)."""
NOTES = {}
for _m in ("s3a", "s3b"):
    NOTES.update(__import__(f"maths_notes_v3.{_m}", fromlist=["NOTES"]).NOTES)
