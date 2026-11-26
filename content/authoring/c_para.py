"""Paragraph-question builder shared by the private Unit Test files (same shape as extreme/s8u07.py's para(), without its side effects)."""
S8 = [4, 6]
F8 = 'The data show … For example, at … the value was … This is because … The results are / are not reliable because …'
def para(id, obj, prompt, rubric, need, model, partial, data=None, adv=False, ext=False, words=40, sentences=S8, frame=F8, teacher=False, pts=None):
    q = {'id': id, 'type': 'para', 'prompt': ('* Advanced. ' if adv else '') + prompt, 'diff': 'VH', 'obj': obj, 'skill': 'Reasoning',
         'sentences': sentences, 'minWords': words, 'frame': frame, 'rubric': [{'pt': p, 'kw': [k]} for p, k in rubric], 'need': need,
         'model': model, 'partial': [{'text': t, 'score': s, 'why': w} for t, s, w in partial], 'hint': '', 'reason': ''}
    if data: q['data'] = {'head': data[0], 'rows': data[1:]}
    if adv: q['adv'] = True
    if ext: q['source'] = 'Camday original'
    if teacher: q['teacher'] = True; q['pts'] = pts
    return q
