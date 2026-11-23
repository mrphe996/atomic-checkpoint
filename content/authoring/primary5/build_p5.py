# -*- coding: utf-8 -*-
"""Build content/src/stage5-unitNN.json (Primary Science Stage 5) from primary5/uNN.py, the video timings in build/p5/out
and the private Unit Tests.  Usage: python3 build_p5.py [1 …]"""
import json, os, sys, importlib.util, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kit5
VID = os.path.join(HERE, '..', '..', '..', '..', 'build', 'p5', 'out'); MEDIA = os.path.join(HERE, '..', '..', '..', 'web', 'media', 's5')
PRIV = os.path.join(HERE, '..', '..', 'private')

def load(path, name):   # load by file path: Stage 6 has modules with the same names
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def build(n):
    U = load(os.path.join(HERE, f'u{n:02d}.py'), f'p5u{n:02d}').U; T = load(os.path.join(PRIV, f'tests_stage5_unit{n:02d}.py'), f'p5t{n:02d}')
    metas = {}; os.makedirs(MEDIA, exist_ok=True)
    for s in U.sections:
        k = int(s.sid.split('.')[1]); metas[s.sid] = json.load(open(os.path.join(VID, f'u{n}_s{k}.json')))
        for ext in ('.mp4', '_poster.jpg'):
            src = os.path.join(VID, f'u{n}_s{k}{ext}'); dst = os.path.join(MEDIA, f'u{n}_s{k}{ext}')
            if os.path.exists(src) and (not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst)): shutil.copy2(src, dst)
    data = U.export(metas, (T.TEST_A, T.TEST_B), kit5.TITLES)
    out = os.path.join(HERE, '..', '..', 'src', f'stage5-unit{n:02d}.json'); json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
    print(n, [(s['id'], len(s['req']), len(s['prac']), len(s['adv']), len(s['stops']), len(s['vocab'])) for s in data['sections']])

if __name__ == '__main__':
    for n in [int(a) for a in sys.argv[1:]] or [1]: build(n)
