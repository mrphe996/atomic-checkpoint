"""Helpers for the Camday Hard-question banks (s7_hard_bank.py, s9_hard_bank.py …). All questions are Camday originals."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '..', 'src')
ADV = '* Advanced. '
F8 = 'The data show … For example … This is because … The results are / are not reliable because …'
PLAN = 'I will change … I will measure … I will keep … the same. I will repeat … I expect …'

def base(id, typ, obj, prompt, skill, diff='VH'):
    return {'id': id, 'type': typ, 'prompt': ADV + prompt, 'diff': diff, 'obj': obj, 'skill': skill, 'hint': '', 'reason': '', 'adv': True, 'source': 'Camday original'}
def tbl(q, data):
    if data: q['data'] = {'head': data[0], 'rows': data[1:]}
    return q
def mcq(id, obj, prompt, right, wrong, reason='', data=None, fig=None, skill='Reasoning'):
    q = base(id, 'mcq', obj, prompt, skill); q['options'] = [{'t': right, 'ok': True, 'fb': 'Correct.'}] + [{'t': t, 'ok': False, 'fb': fb} for t, fb in wrong]
    q['reason'] = reason
    if fig: q['fig'] = fig
    return tbl(q, data)
def multi(id, obj, prompt, opts, reason='', data=None):
    q = base(id, 'multi', obj, prompt, 'Reasoning'); q['options'] = [{'t': t, 'ok': ok} for t, ok in opts]; q['reason'] = reason
    return tbl(q, data)
def num(id, obj, prompt, answer, unit, units, reason, data=None, fig=None, tol=0.0):
    q = base(id, 'num', obj, prompt, 'Application'); q.update({'answer': answer, 'unit': unit, 'tol': tol, 'units': units, 'errs': [], 'unitFb': '', 'reason': reason})
    if fig: q['fig'] = fig
    return tbl(q, data)
def order(id, obj, prompt, items, reason=''):
    q = base(id, 'order', obj, prompt, 'Knowledge', 'H'); q['items'] = items; q['reason'] = reason; return q
def graph(id, obj, prompt, x, y, pts, fprompt, fright, fwrong, reason=''):
    q = base(id, 'graph', obj, prompt, 'Data'); q.update({'x': x, 'y': y, 'pts': pts, 'reason': reason,
        'table_rows': [[str(a), str(b)] for a, b in pts],
        'follow': {'id': id + 'f', 'type': 'mcq', 'prompt': fprompt, 'diff': 'VH', 'obj': obj, 'skill': 'Data',
                   'options': [{'t': fright, 'ok': True, 'fb': 'Correct.'}] + [{'t': t, 'ok': False, 'fb': fb} for t, fb in fwrong]}})
    return q
def para(id, obj, prompt, rubric, need, model, data=None, frame=F8, words=40):
    q = base(id, 'para', obj, prompt, 'Reasoning'); q.update({'sentences': [4, 6], 'minWords': words, 'frame': frame,
        'rubric': [{'pt': p, 'kw': [k]} for p, k in rubric], 'need': need, 'model': model, 'partial': []})
    return tbl(q, data)
def line(xl, yl, x, y, series): return {'kind': 'linegraph', 'x': dict(zip(('min', 'max', 'step'), x), label=xl), 'y': dict(zip(('min', 'max', 'step'), y), label=yl), 'series': series}
def bars(labels, values, ymax, step, yl, xl=''): return {'kind': 'barchart', 'labels': labels, 'values': values, 'ymax': ymax, 'step': step, 'ylabel': yl, 'xlabel': xl}
def ax(label, lo, hi, step): return {'label': label, 'min': lo, 'max': hi, 'step': step}


def apply(stage, B):
    n = 0
    for (u, sec), qs in sorted(B.items()):
        p = os.path.join(SRC, 'stage%d-unit%02d.json' % (stage, u)); d = json.load(open(p)); s = next(x for x in d['sections'] if x['id'] == sec)
        ids = {q['id'] for q in qs}; s['adv'] = [q for q in s['adv'] if q['id'] not in ids] + qs; n += len(qs)
        for q in qs: assert q['obj'] in d['objectives'] and q['obj'] in s['objs'], (q['id'], q['obj'])
        json.dump(d, open(p, 'w'), ensure_ascii=False)
    print('Stage %d: added %d Hard questions in %d lessons' % (stage, n, len(B)))
