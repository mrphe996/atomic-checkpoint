"""Primary Maths v2 overlay (Stages 3-6): adds a "Why it works" idea, a worked example and a method box to each section
that lacks them. Blocks carry "v2p": True so re-applying is idempotent. Data: p3.py … p6.py, dict W[unit][section] =
(why_title, why_text, (ex_title, question, [(step, note), …], answer), (method_title, [step, …])).  Written by the Atomic teaching team."""
import importlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..'))
SRC = os.path.join(HERE, '..', '..', 'src')

def apply(stage, unit, d):
    try: W = importlib.import_module(f"maths_primary_v2.p{stage}").W
    except ModuleNotFoundError: return d
    secs = W.get(unit, {})
    for s in d['sections']:
        L = [b for b in s['lesson'] if not b.get('v2p')]
        w = secs.get(s['id'])
        if w:
            why_t, why_p, ex, meth = w
            have_why = any(b['k'] == 'idea' and b.get('t', '').startswith('Why') for b in L)
            add = []
            if not have_why and why_t: add.append({'k': 'idea', 't': why_t, 'p': [x.strip() for x in why_p.split('\n') if x.strip()], 'v2p': True})
            if ex and not any(b['k'] == 'example' for b in L):
                add.append({'k': 'example', 't': ex[0], 'p': [], 'q': ex[1], 'steps': [list(x) for x in ex[2]], 'a': ex[3], 'v2p': True})
            if meth and not any(b['k'] == 'method' for b in L):
                add.append({'k': 'method', 't': meth[0], 'p': list(meth[1]), 'v2p': True})
            cut = next((i for i, b in enumerate(L) if b['k'] == 'mistake'), len(L))
            L = L[:cut] + add + L[cut:]
        s['lesson'] = L
    return d

if __name__ == '__main__':
    n = 0
    for st in (3, 4, 5, 6):
        for u in range(1, 20):
            p = os.path.join(SRC, f'stage{st + 10}-unit{u:02d}.json')
            if not os.path.exists(p): continue
            d = json.load(open(p, encoding='utf-8')); apply(st, u, d)
            n += sum(1 for s in d['sections'] for b in s['lesson'] if b.get('v2p'))
            json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
    print('primary maths v2 blocks in place:', n)
