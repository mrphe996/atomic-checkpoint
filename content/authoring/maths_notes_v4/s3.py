# -*- coding: utf-8 -*-
"""Cambridge Primary Mathematics Stage 3 – v4 lessons (complete self-study lessons)."""
NOTES = {}
for _m in ("s3_u01", "s3_u01_book", "s3_u02", "s3_u02_book", "s3_u03", "s3_u03_book", "s3_u04", "s3_u04_book", "s3_u05", "s3_u05_book", "s3_u06", "s3_u06_book", "s3_u07", "s3_u07_book", "s3_u08", "s3_u08_book", "s3_u09", "s3_u09_book", "s3_u10", "s3_u10_book", "s3_u11", "s3_u11_book"):
    NOTES.update(__import__(f"maths_notes_v4.{_m}", fromlist=["NOTES"]).NOTES)
