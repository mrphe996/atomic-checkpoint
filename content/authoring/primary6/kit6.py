# -*- coding: utf-8 -*-
"""Atomic Primary Science (Stage 6) authoring kit. Reuses the question builders of the Mathematics kit,
without its number tidy-up. Each section has an animated video with pause questions, 8 Core questions
(4 listening + 4 say-the-word: these unlock the next lesson), Practice, * Advanced, a word bank and an experiment room.
Written by the Atomic teaching team."""
import os, sys, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.append(os.path.join(HERE, '..', 'math9'))
import kit as K
K.pretty = lambda t: t            # science text is left exactly as written
from kit import MC, MS, S, CZ, TB, B, GD, TK, EX, OD, MT, GR, Q, finish, Paper

MEDIA = 'media/s6'
slug = lambda w: w.lower().replace(' ', '-')
wa = lambda w, kind='': f"{MEDIA}/w/{kind}{slug(w)}.mp3"

def SAY(word, meaning, emoji, o, d='M'):
    return Q.base('say', f'Listen to the word, then say it out loud.', d, o, 'Speaking', word=word, audio=wa(word), meaning=meaning, emoji=emoji, tag='🎤 Say the word')

def LISTEN_WORD(word, others, o, d='M'):
    return MC('Listen. Which word do you hear?', word, [(w, f'Listen again – the word you hear is not “{w}”.') for w in others], d=d, o=o, audio=wa(word), tag='🎧 Listening', skill='Listening',
              reason=f'The word was “{word}”. Press 🐢 Slowly to hear each sound.')

def LISTEN_MEANING(word, meaning, others, o, d='M'):
    return MC('Listen to the meaning. Which word is it?', word, [(w, f'“{w}” means something else. Listen again.') for w in others], d=d, o=o, audio=wa(word, 'd-'), tag='🎧 Listening', skill='Listening',
              reason=f'“{meaning[0].upper() + meaning[1:]}” – that is the meaning of “{word}”.')

def LISTEN_GAP(word, sentence, others, o, d='M'):
    gap = sentence.replace(word, '______', 1) if word in sentence else sentence.replace(word.capitalize(), '______', 1)
    return MC(f'Listen to the sentence. Which word is missing?  “{gap}”', word, [(w, f'Listen again – the missing word is not “{w}”.') for w in others], d=d, o=o, audio=wa(word, 'e-'), tag='🎧 Listening', skill='Listening',
              reason=f'You hear: “{sentence}”')

def LISTEN_TYPE(word, o, d='H'):
    return S('Listen and type the word you hear. Check your spelling.', [word], d=d, o=o, audio=wa(word), tag='🎧 Listen and spell', skill='Listening',
             hint=f'It starts with “{word[0]}” and has {len(word.replace(" ", ""))} letters.', reason=f'The word is “{word}”.')


def core_for(V, SAYW):
    """The 8 Core questions of a lesson: 4 listening (word, meaning, gap, spell) + the 4 words to say aloud."""
    def core(sec, o_words, o_say):
        rows = V[sec.sid]; W = [r[0] for r in rows]; byw = {r[0]: r for r in rows}
        lw = [w for w in W if w not in SAYW[sec.sid]] + SAYW[sec.sid]
        def near(w):   # distractors: the other words of this lesson, rotated so each question differs
            i = W.index(w); return [W[(i + k) % len(W)] for k in (1, 2, 3)]
        sec.core(LISTEN_WORD(lw[0], near(lw[0]), o_words), LISTEN_MEANING(lw[1], byw[lw[1]][1], near(lw[1]), o_words),
                 LISTEN_GAP(lw[2], byw[lw[2]][2], near(lw[2]), o_words), LISTEN_TYPE(lw[3], o_words))
        for w in SAYW[sec.sid]: sec.core(SAY(w, byw[w][1], byw[w][3], o_say))
    return core


class Section:
    def __init__(self, unit, sid, title, objs):
        self.u, self.sid, self.title, self.objs = unit, sid, title, objs
        self.n = int(sid.split('.')[1]); self.pools = {'r': [], 'p': [], 'a': []}; self.stops = []; self.vocab = []; self.lab = None
    def add(self, pool, q):
        lst = self.pools[pool]; qid = f"{self.u.pre}s{self.n}{pool}{len(lst) + 1:02d}"; q = finish(q, qid)
        if pool == 'a' and not q['prompt'].startswith('* Advanced.'): q['prompt'] = '* Advanced. ' + q['prompt']
        lst.append(q); return q
    def core(self, *qs): [self.add('r', q) for q in qs]; return self
    def prac(self, *qs): [self.add('p', q) for q in qs]; return self
    def adv(self, *qs): [self.add('a', q) for q in qs]; return self
    def words(self, rows):
        self.vocab = [{'w': w, 'def': d, 'audio': wa(w), 'emoji': e} for w, d, _, e in rows]; return self
    def stop(self, q, twin):
        i = len(self.stops) + 1; self.stops.append({'q': finish(q, f"{self.u.pre}s{self.n}v{i}"), 'twin': finish(twin, f"{self.u.pre}s{self.n}v{i}t")}); return self
    def labs(self, title, v, h):
        # questions inside the lab get their own ids
        for part, key in ((v, 'lv'), (h, 'lh')):
            part['qs'] = [finish(q, f"{self.u.pre}s{self.n}{key}{k + 1}") for k, q in enumerate(part.get('qs', []))]
        self.lab = {'title': title, 'v': v, 'h': h}; return self
    def export(self, meta):
        stops = []
        for (t, rev), s in zip(meta['stops'], self.stops):
            stops.append({'id': f"v{self.sid.replace('.', '')}{chr(97 + len(stops))}", 't': t, 'review': [rev, t], 'note': 'Paused on the “Pause and think” card.', 'q': s['q'], 'twin': s['twin']})
        assert len(stops) == len(self.stops), (self.sid, len(meta['stops']), len(self.stops))
        assert len(self.pools['r']) == 8, (self.sid, 'core', len(self.pools['r']))
        return {'id': self.sid, 'title': self.title, 'objs': self.objs,
                'video': {'src': f"{MEDIA}/u{self.u.n}_s{self.n}.mp4", 'poster': f"{MEDIA}/u{self.u.n}_s{self.n}_poster.jpg", 'offset': 0, 'dur': meta['dur'], 'range': ''},
                'stops': stops, 'captions': meta['captions'], 'chapters': meta['chapters'],
                'req': self.pools['r'], 'prac': self.pools['p'], 'adv': self.pools['a'], 'vocab': self.vocab, 'lab': self.lab}


class Unit:
    def __init__(self, n, title, strand, blurb, objectives):
        self.n, self.title, self.strand, self.blurb, self.objectives = n, title, strand, blurb, objectives
        self.pre = f"p6u{n:02d}"; self.sections = []; self.mind = []
    def section(self, sid, title, objs):
        s = Section(self, sid, title, objs); self.sections.append(s); return s
    def mindmap(self, *kids):
        self.mind = [{'id': f'k{i}', 't': t, 'd': d, 'obj': o, 'sec': s} for i, (t, d, o, s) in enumerate(kids)]
    def export(self, metas, tests, titles):
        secs = [s.export(metas[s.sid]) for s in self.sections]
        segs = {}
        for s in secs:
            for o in s['objs']: segs.setdefault(o, [s['id'], 0.0, s['video']['dur'], s['title']])
        return {'course': {'id': 's6', 'title': 'Atomic – Cambridge Primary Science — Stage 6', 'units': [{'n': i + 1, 't': t} for i, t in enumerate(titles)]},
                'unit': {'n': self.n, 'stage': 6, 'title': self.title, 'strandShort': self.strand.split(':')[0], 'blurb': self.blurb, 'strand': self.strand,
                         'framework': 'Cambridge Primary Science (0097), Stage 6', 'primary': True},
                'objectives': self.objectives, 'sections': secs, 'segments': segs, 'sources': [],
                'tests': {'A': tests[0], 'B': tests[1], 'pass': 0.7},
                'mindmap': {'id': 'root', 't': self.title, 'sec': None, 'kids': self.mind}}

TITLES = ['The human body', 'Materials: properties and changes', 'Rocks, the rock cycle and soil', 'Food chains and food webs', 'Forces and electricity', 'Light and the Solar System']
