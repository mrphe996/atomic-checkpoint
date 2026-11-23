# -*- coding: utf-8 -*-
"""Build content/src/stage3-unitNN.json (Primary Science Stage 3) from primary3/uNN.py, the video timings in build/p3/out
and the private Unit Tests.  Usage: python3 build_p3.py [--dry] [1 …]   (--dry: made-up video timings, to check the questions)"""
import json, os, sys, importlib.util, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kit3
BUILD = os.path.join(HERE, '..', '..', '..', '..', 'build', 'p3'); VID = os.path.join(BUILD, 'out'); MEDIA = os.path.join(HERE, '..', '..', '..', 'web', 'media', 's3')
PRIV = os.path.join(HERE, '..', '..', 'private'); STAGE = 3

def load(path, name):   # load by file path: other stages have modules with the same names
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def dry_meta(n, k):
    sc = load(os.path.join(BUILD, f'script_u{n}.py'), f'p{STAGE}sc{n}'); sec = next(s for s in sc.SECTIONS if s['id'] == f'{n}.{k}')
    t, caps, stops, chap = 0.0, [], [], []
    for x in sec['scenes']:
        chap.append([round(t, 2), x.get('head') or x['k']])
        for line in x['say']: caps.append([round(t, 2), line]); t += max(2.5, len(line) / 12)
        if x.get('stop'): stops.append([round(t - 0.2, 2), round(chap[-2][0] if len(chap) > 1 else 0, 2)])
        t += 1.3
    return {'dur': round(t + 2, 2), 'captions': caps, 'chapters': chap, 'stops': stops}

def build(n, dry=False):
    U = load(os.path.join(HERE, f'u{n:02d}.py'), f'p{STAGE}u{n:02d}').U
    tp = os.path.join(PRIV, f'tests_stage{STAGE}_unit{n:02d}_v3.py')   # 2026 Unit Test format wins
    if not os.path.exists(tp): tp = os.path.join(PRIV, f'tests_stage{STAGE}_unit{n:02d}.py')
    T = load(tp, f'p{STAGE}t{n:02d}') if os.path.exists(tp) else None
    metas = {}; os.makedirs(MEDIA, exist_ok=True)
    for s in U.sections:
        k = int(s.sid.split('.')[1])
        if dry: metas[s.sid] = dry_meta(n, k); continue
        metas[s.sid] = json.load(open(os.path.join(VID, f'u{n}_s{k}.json')))
        for ext in ('.mp4', '_poster.jpg'):
            src = os.path.join(VID, f'u{n}_s{k}{ext}'); dst = os.path.join(MEDIA, f'u{n}_s{k}{ext}')
            if os.path.exists(src) and (not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst)): shutil.copy2(src, dst)
    data = U.export(metas, (T.TEST_A, T.TEST_B) if T else ([], []), kit3.TITLES)
    if not dry or SAVE:
        out = os.path.join(HERE, '..', '..', 'src', f'stage{STAGE}-unit{n:02d}.json'); json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
    print(n, [(s['id'], len(s['req']), len(s['prac']), len(s['adv']), len(s['stops']), len(s['vocab'])) for s in data['sections']], 'tests' if T else 'NO TESTS')
    return data

SAVE = '--save' in sys.argv   # with --dry: write the file anyway, to run the content checks before the videos exist
if __name__ == '__main__':
    dry = '--dry' in sys.argv; args = [a for a in sys.argv[1:] if not a.startswith('--')]
    for n in [int(a) for a in args] or [1]: build(n, dry)
