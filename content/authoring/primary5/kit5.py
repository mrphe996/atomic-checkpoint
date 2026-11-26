# -*- coding: utf-8 -*-
"""Stage 5 uses the Primary kit with stage 5 settings (media/s5, ids p5uNN). Written by the Camday teaching team."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(HERE, '..', 'primary6')); sys.path.append(os.path.join(HERE, '..', '..', '..', '..', 'build', 'p5'))
import kit6
kit6.set_stage(5)
from kit6 import *
TITLES = ['Life cycles of flowering plants', 'Sound', 'States and properties of matter', 'The digestive system', 'Forces and magnetism', 'Seasons and adaptations']
from vocab_all import V, SAY as SAYW
core = core_for(V, SAYW)
def test_lab(title, intro, change, measure, unit, mx, step, instr, conds, qs):
    return {'kind': 'test', 'title': title, 'intro': intro, 'change': change, 'measure': measure, 'unit': unit, 'max': mx, 'step': step, 'instr': instr,
            'conds': [{'k': f'c{i}', 't': t, 'emoji': e, 'val': v} for i, (t, e, v) in enumerate(conds)], 'qs': qs}
def sort_lab(title, intro, groups, items, qs):
    return {'kind': 'sort', 'title': title, 'intro': intro, 'groups': groups, 'items': [{'t': t, 'emoji': e, 'g': g, 'why': w} for t, e, g, w in items], 'qs': qs}
def home(title, intro, need, safety, steps, head, rows, hint, qs):
    return {'title': title, 'intro': intro, 'need': need, 'safety': safety, 'steps': steps, 'record': {'head': head, 'rows': rows, 'hint': hint}, 'qs': qs}
