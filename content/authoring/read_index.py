# -*- coding: utf-8 -*-
"""Page map of the Camday reading packs (web/media/read/*.pdf): which PDF pages hold each lesson section.
Section headings are found on the page text ("2.3 Collecting like terms"). → web/media/read/index.json
Usage: python3 read_index.py"""
import json, os, re, subprocess
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
RD = os.path.join(ROOT, "web/media/read")
out = {}
for f in sorted(os.listdir(RD)):
    if not f.endswith(".pdf"): continue
    key = f[:-4]; p = os.path.join(RD, f)
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", p], capture_output=True, text=True).stdout).group(1))
    starts = {}
    for pg in range(1, n + 1):
        txt = subprocess.run(["pdftotext", "-f", str(pg), "-l", str(pg), "-layout", p, "-"], capture_output=True, text=True).stdout
        for line in txt.splitlines():
            m = re.match(r"^\s*(\d{1,2}\.\d{1,2})\s+[A-Z][a-z]", line)
            if m and m.group(1) not in starts: starts[m.group(1)] = pg
    ids = sorted(starts, key=lambda s: (starts[s], [int(x) for x in s.split(".")]))
    secs = {}
    for i, sid in enumerate(ids):
        end = (starts[ids[i + 1]] if i + 1 < len(ids) else n)
        secs[sid] = [starts[sid], max(starts[sid], end if i + 1 == len(ids) else (end - 1 if end > starts[sid] else end))]
    out[key] = {"pages": n, "secs": secs}
json.dump(out, open(os.path.join(RD, "index.json"), "w"), separators=(",", ":"))
print(len(out), "packs ·", out.get("m7u02"))
