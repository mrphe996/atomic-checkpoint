#!/usr/bin/env python3
"""Copy each lesson video from web/media/mv/index.json into its lesson's `lv` in web/content (run after apply_notes_v3.py).
Usage: python3 tools/maths_video/apply.py 7"""
import glob, json, os, sys
WEB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "web")
stage = sys.argv[1]; idx_p = os.path.join(WEB, "media", "mv", "index.json")
vids = (json.load(open(idx_p)) if os.path.exists(idx_p) else {}).get(stage, {})
n = 0
for f in sorted(glob.glob(os.path.join(WEB, "content", f"stage1{stage}-unit[0-9][0-9].json"))):
    d = json.load(open(f, encoding="utf-8")); hit = False
    for s in d["sections"]:
        if vids.get(s["id"], {}).get("up"):   # only videos already in the video storage ("up": true in index.json) are shown to learners
            v = vids[s["id"]]; assert set(v["times"]) == {x["id"] for x in s["stops"]}, f"{s['id']}: video pauses do not match the check questions"
            s["lv"] = {k: x for k, x in v.items() if k != "up"}; hit = True; n += 1
    if hit: json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False)
print(f"Stage {stage}: {n} lesson videos")
