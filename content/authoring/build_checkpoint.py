"""Builds content/src/stage7-cp.json (Atomic Checkpoint-format Science papers) from content/private/checkpoint_stage7.py (both git-ignored)."""
import json, os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cp", os.path.join(H, "..", "private", "checkpoint_stage7.py"))
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
out = {"final": True, "kind": "checkpoint",
       "unit": {"title": "Checkpoint practice papers", "stage": 7, "subject": "Science", "syllabus": "0893",
                "note": "Written by the Atomic teaching team in the format of Cambridge Lower Secondary Checkpoint Science (0893). Not Cambridge papers."},
       "objectives": cp.OBJECTIVES, "minutes": 45, "max": 50, "pass": 0.5, "level": 0, "meta": cp.META, "papers": cp.PAPERS}
os.makedirs(os.path.join(H, "..", "src"), exist_ok=True)
json.dump(out, open(os.path.join(H, "..", "src", "stage7-cp.json"), "w"), ensure_ascii=False)
print("checkpoint papers", len(cp.PAPERS), "questions", sum(len(p) for p in cp.PAPERS.values()))
