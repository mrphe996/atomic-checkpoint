"""Adds a 6-mark paragraph question (data or a chart, marked by AI then a teacher if unsure) to Unit Tests A and B, keeping 30 marks.
The questions and their mark schemes live in the git-ignored content/private/tests_stage<N>_para.py (never commit answer keys).
Usage: python3 unit_test_para.py 8      Then: node tools/build-content.mjs && node tools/build-edge.mjs && node tools/seal-keys.mjs"""
import json, os, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'private'))
stage = int(sys.argv[1])
P = importlib.import_module('tests_stage%d_para' % stage).PAPERS
for u, spec in sorted(P.items()):
    p = os.path.join(HERE, '..', '..', 'src', 'stage%d-unit%02d.json' % (stage, u)); d = json.load(open(p))
    for f in 'AB':
        new = spec[f]; assert new['obj'] in d['objectives'], new['id']
        t = [q for q in d['tests'][f] if q['id'] not in spec['DROP'][f] and q['id'] != new['id']] + [new]
        assert sum(q['pts'] for q in t) == 30, (u, f, sum(q['pts'] for q in t)); d['tests'][f] = t
    json.dump(d, open(p, 'w'), ensure_ascii=False)
    print('stage%d unit %d: Tests A and B now have a 6-mark paragraph question (30 marks)' % (stage, u))
