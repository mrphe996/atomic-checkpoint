# -*- coding: utf-8 -*-
import json, os, sys
from c_base import OBJECTIVES, SECTIONS, SEGMENTS, SOURCES
from c_video import STOPS
from c_s31 import S31_REQ, S31_PRAC, S31_ADV
from c_s32 import S32_REQ, S32_PRAC, S32_ADV
from c_s33 import S33_REQ, S33_PRAC, S33_ADV
from c_s34 import S34_REQ, S34_PRAC, S34_ADV
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'private'))
from tests_stage7_unit03 import TEST_A, TEST_B  # answer keys: content/private (git-ignored)

POOLS = {"3.1": (S31_REQ, S31_PRAC, S31_ADV), "3.2": (S32_REQ, S32_PRAC, S32_ADV),
         "3.3": (S33_REQ, S33_PRAC, S33_ADV), "3.4": (S34_REQ, S34_PRAC, S34_ADV)}

# Atomic concept map (independent design). links → sections / objectives
MINDMAP = {
 "id": "root", "t": "Cells", "sec": None,
 "kids": [
  {"id": "uni", "t": "Unicellular organisms", "d": "Are only a single cell. Examples: bacterium, yeast, amoeba.", "obj": "O2", "sec": "3.1"},
  {"id": "multi", "t": "Multicellular organisms", "d": "Examples: plants, animals. Made up of many cells.", "obj": "O1", "sec": "3.1"},
  {"id": "theory", "t": "Cell theory", "d": "All living things are made up of cells • Cells are the basic units of life • Cells come from pre-existing cells.", "obj": "O3", "sec": "3.1"},
  {"id": "micro", "t": "Light microscope", "d": "Total magnification = eyepiece × objective.", "obj": "O4", "sec": "3.1"},
  {"id": "plant", "t": "Plant cells", "d": "Cell wall • Chloroplasts • Large sap vacuole (plus nucleus, cytoplasm, membrane, mitochondria).", "obj": "O5", "sec": "3.2"},
  {"id": "animal", "t": "Animal cells", "d": "Nucleus • Cytoplasm • Cell membrane • Mitochondria.", "obj": "O6", "sec": "3.2"},
  {"id": "spec", "t": "Specialised cells", "d": "Plant: root hair, palisade. Animal: red blood cell, neurone, ciliated cell.", "obj": "O8", "sec": "3.3"},
  {"id": "levels", "t": "Tissues → Organs → Organ systems", "d": "Cells are grouped into tissues, tissues into organs, organs work together in organ systems, forming an organism.", "obj": "O9", "sec": "3.4"},
 ]}

import re
def srt(path):
    txt = open(path, encoding="utf-8").read().strip().split("\n\n"); out = []
    for b in txt:
        L = b.strip().split("\n")
        m = re.match(r"(\d+):(\d+):(\d+),(\d+)", L[1])
        t = int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3]) + int(m[4]) / 1000
        out.append([t, " ".join(L[2:])])
    return out
CHAPTERS = {
 "3.1": [[0.0, "Introduction"], [30.5, "Cells & organisms"], [52.2, "Unicellular / multicellular"], [85.3, "How cell theory developed"], [171.3, "The light microscope"], [279.0, "Magnification"]],
 "3.2": [[0.0, "Plant cell parts"], [60.3, "Onion cells"], [67.2, "Animal cell parts"], [105.1, "Plant vs animal cells"], [140.3, "Think about it"]],
 "3.3": [[0.0, "Specialised cells"], [11.0, "Root hair cells"], [25.8, "Palisade cells"], [40.6, "Ciliated & red blood cells"], [66.3, "Nerve cells"]],
 "3.4": [[0.0, "Tissues"], [29.9, "Organs"], [62.1, "Organ systems"], [95.5, "Putting it together"]],
}
CAPS = srt("/home/claude/vid/deliver/S7_Unit03_Cells_lesson_Alice.srt")

def main(out):
    import os
    secs = []
    allq = []
    for s in SECTIONS:
        req, prac, adv = POOLS[s["id"]]
        srcmap = {x["id"]: x for x in SOURCES}
        for x in adv:
            x["adv"] = True
            if isinstance(x.get("src"), str):
                sx = srcmap[x["src"]]; x["src"] = {"id": sx["id"], "name": sx["name"], "url": sx["url"]}
        n = len(req) + len(prac) + len(adv)
        assert n >= 30, (s["id"], n)
        fig = sum(1 for x in req if x["type"] in ("label", "scale", "grid", "table", "graph", "sim") or x.get("skill") in ("Data", "Figure"))
        exp = sum(1 for x in req if x["type"] == "explain")
        assert fig >= 2 and exp >= 1, (s["id"], fig, exp)
        ss = dict(s)
        ss["stops"] = STOPS[s["id"]]
        o, d = s["video"]["offset"], s["video"]["dur"]
        ss["captions"] = [[round(max(0, t - o), 2), x] for t, x in CAPS if o - 0.01 <= t < o + d - 0.05]
        ch = [[0.0, "Introduction to section" + s["id"]]]
        for ob in s["objs"]:
            sg = SEGMENTS[ob]
            if sg[1] > 1 and all(abs(sg[1] - c[0]) > 2 for c in ch): ch.append([sg[1], sg[3]])
            elif sg[1] <= 1: ch[0] = [0.0, sg[3]]
        ss["chapters"] = CHAPTERS.get(s["id"], sorted(ch))
        ss["req"], ss["prac"], ss["adv"] = req, prac, adv
        secs.append(ss)
        allq += req + prac + adv
    for t in (TEST_A, TEST_B):
        assert sum(x["pts"] for x in t) == 30, sum(x["pts"] for x in t)
    ids = [x["id"] for x in allq + TEST_A + TEST_B]
    assert len(ids) == len(set(ids)), "dup ids"
    data = {
        "course": {"id": "s7", "title": "Atomic Checkpoint Secondary Cambridge Science — Stage 7",
                   "units": [{"n": i + 1, "t": t} for i, t in enumerate([
                       "Introducing Science", "Measurements", "Cells", "Classifying Living Things",
                       "Food Chains and Food Webs", "Materials and Their Structure", "Properties of Materials",
                       "Acids and Alkalis", "Chemical Reactions", "Forces", "Energy", "Electricity",
                       "Earth Processes", "Earth and Beyond"])]},
        "unit": {"n": 3, "title": "Cells", "strandShort": "Biology", "blurb": "The basic units of life — from using a microscope to how cells build tissues, organs and organ systems.", "strand": "Biology: structure and function", "framework": "Cambridge Lower Secondary Science (0893), Stage 7", "fullVideo": "S7_Unit03_Cells_lesson_Alice.mp4 (12:56)"},
        "objectives": OBJECTIVES, "sections": secs, "segments": SEGMENTS, "sources": SOURCES,
        "tests": {"A": TEST_A, "B": TEST_B, "pass": 0.7}, "mindmap": MINDMAP,
    }
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=0)
    print("sections", [(s["id"], len(s["req"]), len(s["prac"]), len(s["adv"]), len(s["stops"])) for s in secs])
    print("total questions", len(allq), "+ test", len(TEST_A), len(TEST_B))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "stage7-unit03.json"))
