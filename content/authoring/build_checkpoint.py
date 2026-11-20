"""Builds content/src/stage7-cp.json (Atomic Checkpoint-format Science papers) from content/private/checkpoint_stage7.py (both git-ignored)."""
import json, os, sys, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
g = int(sys.argv[1]) if len(sys.argv) > 1 else 7
spec = importlib.util.spec_from_file_location("cp", os.path.join(H, "..", "private", f"checkpoint_stage{g}.py"))
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
out = {"final": True, "kind": "checkpoint",
       "unit": {"title": "Checkpoint practice papers", "stage": g, "covers": "Stage 7" if g == 7 else f"Stages 7–{g}", "subject": "Science", "syllabus": "0893",
                "note": "Written by the Atomic teaching team in the format of Cambridge Lower Secondary Checkpoint Science (0893). Not Cambridge papers."},
       "objectives": cp.OBJECTIVES, "minutes": 45, "max": 50, "pass": 0.5, "level": 0, "meta": cp.META, "papers": cp.PAPERS}
os.makedirs(os.path.join(H, "..", "src"), exist_ok=True)
json.dump(out, open(os.path.join(H, "..", "src", f"stage{g}-cp.json"), "w"), ensure_ascii=False)
print("checkpoint papers", len(cp.PAPERS), "questions", sum(len(p) for p in cp.PAPERS.values()))
