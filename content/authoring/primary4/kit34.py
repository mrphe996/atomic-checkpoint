# -*- coding: utf-8 -*-
"""Atomic Primary Science for the youngest learners (Stages 3 and 4, ages 7–9).
Uses the Primary kit, with these rules: no typing anywhere (they cannot type words yet), most questions are
multiple choice with big picture cards, everyday-life questions, and labs where results are tapped, not typed.
Core (8): listen and tap the picture (4), read the meaning and tap the picture (2), listen to a sentence and tap the
missing word's picture (2).  Written by the Atomic teaching team."""
import os, sys, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(HERE, '..', 'primary6'))
import kit6
from kit6 import MC, MS, GD, TK, OD, MT, TB, B, Q, Unit, Section, wa
import kit as K          # the shared question kit (its Paper also finishes questions)
_finish0 = K.finish

# picture options: PM(...) stores the picture of each option; they are put on the options when the question is finished
def _finish(q, qid):
    pics = q.get('_pics'); q = _finish0(q, qid)
    if pics:
        q.pop('_pics', None)
        for o in q.get('options', []): o['e'] = pics.get(o['t'], '❔')
    return q
kit6.finish = _finish; K.finish = _finish
finish = _finish
Paper = K.Paper

class YUnit(Unit):
    """A unit for young learners: tap-only extra practice, and marked 'young' so the platform checks there is no typing."""
    def export(self, metas, tests, titles):
        for s in self.sections:
            if not s.extra_done: extras(s, s.objs[0]); s.extra_done = True
        d = Unit.export(self, metas, tests, titles); d['unit']['young'] = True; return d

def PM(prompt, right, wrongs, o, d='M', pic=None, reason='', **kw):
    """Picture multiple choice. right = (emoji, text); wrongs = [(emoji, text, why), ...]."""
    q = MC(prompt, right[1], [(w[1], w[2] if len(w) > 2 else '') for w in wrongs], d=d, o=o, reason=reason, pic=pic, **kw)
    q['_pics'] = {right[1]: right[0], **{w[1]: w[0] for w in wrongs}}
    return q

def YN(prompt, yes, o, pic=None, why='', d='M'):
    """An everyday yes/no question with thumbs pictures."""
    r = ('👍', 'Yes') if yes else ('👎', 'No'); w = ('👎', 'No', why) if yes else ('👍', 'Yes', why)
    return PM(prompt, r, [w], o, d=d, pic=pic, reason=why)

def setup(stage):
    kit6.set_stage(stage)

def core_for(V):
    """8 Core picture questions from the lesson's words (no typing, no speaking)."""
    def core(sec, o):
        rows = V[sec.sid]; W = [r[0] for r in rows]; by = {r[0]: r for r in rows}
        def others(w, k=2):
            i = W.index(w); return [W[(i + j) % len(W)] for j in range(1, k + 1)]
        qs = []
        for w in W[:4]:   # listen to the word, tap its picture
            qs.append(PM('🎧 Listen. Tap the picture of the word you hear.', (by[w][3], w), [(by[x][3], x, f'Listen again – this is “{x}”.') for x in others(w)], o,
                         audio=wa(w), tag='🎧 Listen and tap', skill='Listening', reason=f'The word was “{w}”.'))
        for w in (W[4:] + W)[:2]:   # read the meaning, tap the picture
            qs.append(PM(f'Which word means “{by[w][1]}”?', (by[w][3], w), [(by[x][3], x, f'“{x}” means {by[x][1]}.') for x in others(w)], o,
                         audio=wa(w, 'd-'), tag='📖 Meaning', skill='Vocabulary', reason=f'“{w}” means {by[w][1]}.'))
        for w in (W[2:] + W)[:2]:   # listen to a sentence, tap the missing word
            sen = by[w][2]; gap = sen.replace(w, '____', 1) if w in sen else sen.replace(w.capitalize(), '____', 1)
            qs.append(PM(f'🎧 Listen to the sentence. Which word is missing? “{gap}”', (by[w][3], w), [(by[x][3], x, f'Listen again – the missing word is not “{x}”.') for x in others(w)], o,
                         audio=wa(w, 'e-'), tag='🎧 Listen and tap', skill='Listening', reason=f'You hear: “{sen}”'))
        sec.core(*qs[:8])
    return core

def extras(sec, o):
    """More practice from the lesson's words and lab, all by tapping: match words to pictures and meanings,
    find the picture, and results from the virtual lab."""
    rows = sec.rows; W = [r[0] for r in rows]; by = {r[0]: r for r in rows}
    rng = random.Random(sec.sid)
    sec.prac(MT('Match each word to its meaning.', [(r[0], r[1]) for r in rows[:5]], o=o, skill='Vocabulary'))
    for w in W:
        oth = [x for x in W if x != w]; rng.shuffle(oth)
        sec.prac(PM(f'Tap the picture for “{w}”.', (by[w][3], w), [(by[x][3], x, f'That is “{x}”.') for x in oth[:2]], o, skill='Vocabulary', audio=wa(w), tag='👀 Find the picture'))
    L = (sec.lab or {}).get('v') or {}
    if L.get('kind') == 'test' and len(L.get('conds', [])) >= 3:
        cs = sorted(L['conds'], key=lambda c: c['val']); big = cs[-1]
        sec.prac(PM(f"In the lab “{L['title']}”, which gave the biggest {L['measure'].lower()}?", (big['emoji'], big['t']), [(c['emoji'], c['t'], f"{c['t']} gave {c['val']} {L['unit']}.") for c in cs[:-1]][:3], o, skill='Data'))
        sec.prac(OD(f"Put the lab results in order, from the smallest {L['measure'].lower()} to the biggest.", [f"{c['t']} ({c['val']} {L['unit']})" for c in cs], o=o, skill='Data'))
    if L.get('kind') == 'sort' and L.get('items'):
        sec.prac(GD('Sort each one into the right group.', 'Group', [(it['emoji'] + ' ' + it['t'], L['groups'][it['g']]) for it in L['items']], o=o))

def test_lab(title, intro, change, measure, unit, mx, step, instr, conds, qs):
    """A fair test where the child taps the reading on the scale (choose=True: no typing)."""
    return {'kind': 'test', 'choose': True, 'title': title, 'intro': intro, 'change': change, 'measure': measure, 'unit': unit, 'max': mx, 'step': step, 'instr': instr,
            'conds': [{'k': f'c{i}', 't': t, 'emoji': e, 'val': v} for i, (t, e, v) in enumerate(conds)], 'qs': qs}
def sort_lab(title, intro, groups, items, qs):
    return {'kind': 'sort', 'title': title, 'intro': intro, 'groups': groups, 'items': [{'t': t, 'emoji': e, 'g': g, 'why': w} for t, e, g, w in items], 'qs': qs}
def home(title, intro, need, safety, steps, head, rows, qs, hint='Tap your answer in each row.'):
    """A home experiment; each result is tapped from a list (rows = [(label, [choice, ...]), ...])."""
    return {'title': title, 'intro': intro, 'need': need, 'safety': safety, 'steps': steps,
            'record': {'head': head, 'rows': [[lab, {'choices': ch}] for lab, ch in rows], 'hint': hint}, 'qs': qs}
