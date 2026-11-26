# -*- coding: utf-8 -*-
"""Science v2 overlay: reasoning Practice questions (predict, spot the wrong conclusion, fair test,
always/sometimes/never, read the data) added to every Science section of Stages 3-9.
science_v2/sGuNN.py defines V2 = {section id: [questions]} written with the c_kit helpers.
apply(stage, unit, d) is called by the unit builders just before they write content/src; running
this file applies the overlay to every existing content/src unit. Applying twice gives the same result.
Written by the Camday teaching team."""
import importlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
SRC = os.path.join(HERE, '..', '..', 'src')
AT = 3   # new questions go in after the first few routine questions, so learners meet them early


def apply(stage, unit, d):
    try:
        M = importlib.import_module(f"science_v2.s{stage}u{unit:02d}")
    except ModuleNotFoundError:
        return d
    V2 = M.V2
    for s in d['sections']:
        s['prac'] = [q for q in s['prac'] if not q['id'].startswith('v2_')]
        new = V2.get(s['id'], [])
        if new:
            s['prac'] = s['prac'][:AT] + new + s['prac'][AT:]
    d['v2'] = True
    return d


if __name__ == '__main__':
    n = 0
    for st in range(3, 10):
        for u in range(1, 17):
            p = os.path.join(SRC, f'stage{st}-unit{u:02d}.json')
            if not os.path.exists(p): continue
            d = json.load(open(p, encoding='utf-8')); apply(st, u, d)
            json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
            n += sum(1 for s in d['sections'] for q in s['prac'] if q['id'].startswith('v2_'))
    print('science v2 questions in place:', n)
