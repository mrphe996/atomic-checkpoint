# -*- coding: utf-8 -*-
"""Apply a unit revision (revise/KEY.py, KEY = s7u01 … s9u14) to content/src/stageG-unitNN.json.

A revision module defines (all optional except where used):
  DROP      {sec: [question ids]}   Practice questions removed as same-reasoning duplicates. They are kept as
                                    s['retired'] (never shown) so review lists made before the revision still open.
  NEW_PRAC  {sec: [questions]}      new Practice questions (figures, graphs, experiment set-ups …)
  NEW_ADV   {sec: [questions]}      new Challenge questions; external ideas carry src={id,name,url}
  NEW_STOPS {stop_id: {note, q, twin?}}  pause questions written for the new video scenes
  SOURCES   [{id,name,url,use}]     sources for the externally adapted questions
  TESTS     from content/private: TEST_A, TEST_B (30 marks each)
  REPLACE   {question id: question}  corrected versions of existing Core/Practice/Challenge questions (same id)
The video data (src, captions, chapters, stops with times) comes from revise/KEY_video.json (finalize_v2.py).
Applying twice gives the same result."""
import importlib, json, os, importlib, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..')); sys.path.insert(0, os.path.join(HERE, '..', '..', 'private'))


def src_path(key):
    g, u = int(key[1]), int(key[3:])
    return os.path.join(HERE, '..', '..', 'src', f'stage{g}-unit{u:02d}.json')


def apply_key(key, quiet=False):
    R = importlib.import_module(f'revise.{key}')
    path = src_path(key); d = json.load(open(path, encoding='utf-8'))
    orig_p = os.path.join(HERE, f'{key}_orig.json')
    if not os.path.exists(orig_p):   # the unit before its first revision: Practice and pause questions only (no test keys)
        json.dump({'sections': [{'id': s['id'], 'prac': s['prac'], 'stops': [{k: x[k] for k in ('id', 'note', 'q', 'twin') if k in x} for x in s['stops']]} for s in d['sections']]},
                  open(orig_p, 'w', encoding='utf-8'), ensure_ascii=False)
    orig = {s['id']: s for s in json.load(open(orig_p, encoding='utf-8'))['sections']}
    vj = os.path.join(HERE, f'{key}_video.json'); vid = json.load(open(vj)) if os.path.exists(vj) else None
    DROP, NP, NA, NS = getattr(R, 'DROP', {}), getattr(R, 'NEW_PRAC', {}), getattr(R, 'NEW_ADV', {}), getattr(R, 'NEW_STOPS', {})

    def stop_q(sid):
        if sid in NS: x = NS[sid]; return {k: v for k, v in {"id": sid, "note": x.get("note", ""), "q": x["q"], "twin": x.get("twin")}.items() if v is not None}
        for s in orig.values():
            for x in s['stops']:
                if x['id'] == sid: return dict(x)
        raise KeyError(f'{key}: no question for stop {sid}')

    for s in d['sections']:
        k = s['id']; o = orig[k]
        pool = {q['id']: q for q in o['prac'] + s['prac'] + s.get('retired', [])}
        drop = DROP.get(k, [])
        missing = [i for i in drop if i not in pool]
        if missing: raise KeyError(f'{key} {k}: DROP ids not found {missing}')
        s['retired'] = [pool[i] for i in drop]
        new = NP.get(k, []); ids = {q['id'] for q in new} | set(drop)
        base = [q for q in o['prac'] if q['id'] not in ids]
        s['prac'] = base + new
        na = NA.get(k, []); ids = {q['id'] for q in na}
        for q in na: q['adv'] = True
        s['adv'] = [q for q in s['adv'] if q['id'] not in ids] + na
        RP = getattr(R, 'REPLACE', {})
        for L in ('req', 'prac', 'adv'):
            s[L] = [dict(RP[q['id']], adv=True) if (q['id'] in RP and L == 'adv') else RP.get(q['id'], q) for q in s[L]]
        if vid and k in vid:
            v = vid[k]
            s['video'] = {"src": v['src'], "poster": v['poster'], "offset": 0, "dur": round(v['dur'], 3), "range": ""}
            s['captions'] = v['captions']; s['chapters'] = v['chapters']
            s['stops'] = [dict(stop_q(x['id']), t=x['t'], review=x['review']) for x in v['stops']]
    have = {x['id'] for x in d.get('sources', [])}
    d['sources'] = d.get('sources', []) + [x for x in getattr(R, 'SOURCES', []) if x['id'] not in have]
    T = getattr(R, 'TESTS', None)
    try:   # 2026 Unit Test format (25+ questions in sections A-D) replaces the earlier papers when written
        st_, u_ = int(key[1]), int(key[3:5])
        V3 = importlib.import_module(f"tests_stage{st_}_unit{u_:02d}_v3"); T = (V3.TEST_A, V3.TEST_B)
    except ModuleNotFoundError:
        pass
    if T:
        A, B_ = T
        for t in (A, B_): assert sum(x['pts'] for x in t) == 30, (key, sum(x['pts'] for x in t))
        d['tests'] = {"A": A, "B": B_, "pass": d.get('tests', {}).get('pass', 0.7)}
    from science_v2.apply import apply as _v2; d = _v2(int(key[1]), int(key[3:5]), d)   # v2 reasoning questions
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False)
    if not quiet:
        print(key, [(s['id'], len(s['req']), len(s['prac']), len(s['adv']), len(s['stops']), len(s.get('retired', []))) for s in d['sections']], 'video' if vid else 'no video yet')
    return d


if __name__ == '__main__':
    for key in sys.argv[1:]: apply_key(key)
