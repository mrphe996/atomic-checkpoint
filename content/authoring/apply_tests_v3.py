"""Put the 2026 Unit Test papers (private/tests_stageN_unitUU_v3.py) into content/src. Usage: python3 apply_tests_v3.py s7u03 ..."""
import importlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'private'))
for key in sys.argv[1:]:
    st, u = int(key[1]), int(key[3:5])
    M = importlib.import_module(f"tests_stage{st}_unit{u:02d}_v3")
    path = os.path.join(HERE, '..', 'src', f'stage{st}-unit{u:02d}.json'); d = json.load(open(path, encoding='utf-8'))
    for t in (M.TEST_A, M.TEST_B): assert sum(x['pts'] for x in t) == 30 and len(t) >= 25
    d['tests'] = {"A": M.TEST_A, "B": M.TEST_B, "pass": d.get('tests', {}).get('pass', 0.7)}
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False); print(key, 'tests', len(M.TEST_A), len(M.TEST_B))
