"""Builds content/src/stage7-final.json from content/private/finals_stage7.py (both git-ignored)."""
import json, os, sys, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("fin", os.path.join(H, "..", "private", "finals_stage7.py"))
fin = importlib.util.module_from_spec(spec); spec.loader.exec_module(fin)
out = {"final": True, "unit": {"title": "End-of-year exam", "stage": 7}, "objectives": fin.OBJECTIVES,
       "minutes": 60, "max": 50, "pass": 0.6, "level": 10, "papers": fin.PAPERS}
os.makedirs(os.path.join(H, "..", "src"), exist_ok=True)
json.dump(out, open(os.path.join(H, "..", "src", "stage7-final.json"), "w"), ensure_ascii=False)
print("papers", len(fin.PAPERS), "questions", sum(len(p) for p in fin.PAPERS.values()))
