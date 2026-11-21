# -*- coding: utf-8 -*-
"""Build content/src/stage6-unitNN.json (Primary Science Stage 6) from primary6/uNN.py, the video timings in build/p6/out
and the private Unit Tests.  Usage: python3 build_p6.py [1 …]"""
import json, os, sys, importlib, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..', 'private'))
from kit6 import TITLES
VID = os.path.join(HERE, '..', '..', '..', '..', 'build', 'p6', 'out'); MEDIA = os.path.join(HERE, '..', '..', '..', 'web', 'media', 's6')

def build(n):
    U = importlib.import_module(f'u{n:02d}').U; T = importlib.import_module(f'tests_stage6_unit{n:02d}')
    metas = {}
    for s in U.sections:
        k = int(s.sid.split('.')[1]); mp = os.path.join(VID, f'u{n}_s{k}.json'); metas[s.sid] = json.load(open(mp))
        for ext in ('.mp4', '_poster.jpg'):
            src = os.path.join(VID, f'u{n}_s{k}{ext}'); dst = os.path.join(MEDIA, f'u{n}_s{k}{ext}')
            if os.path.exists(src) and (not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst)): shutil.copy2(src, dst)
    data = U.export(metas, (T.TEST_A, T.TEST_B), TITLES)
    out = os.path.join(HERE, '..', '..', 'src', f'stage6-unit{n:02d}.json'); json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
    print(n, [(s['id'], len(s['req']), len(s['prac']), len(s['adv']), len(s['stops']), len(s['vocab'])) for s in data['sections']])

if __name__ == '__main__':
    for n in [int(a) for a in sys.argv[1:]] or [1]: build(n)
