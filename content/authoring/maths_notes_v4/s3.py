# -*- coding: utf-8 -*-
"""Cambridge Primary Mathematics Stage 3 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s3_u01", "s3_u01_book", "s3_u02", "s3_u02_book", "s3_u03", "s3_u03_book", "s3_u04", "s3_u04_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
