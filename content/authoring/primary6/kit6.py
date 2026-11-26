# -*- coding: utf-8 -*-
"""Camday Primary Science (Stage 6) authoring kit. Reuses the question builders of the Mathematics kit,
without its number tidy-up. Each section has an animated video with pause questions, 8 Core questions
(4 listening + 4 say-the-word: these unlock the next lesson), Practice, * Advanced, a word bank and an experiment room.
Written by the Camday teaching team."""
import os, sys, json, random, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.append(os.path.join(HERE, '..', 'math9'))
import kit as K
K.pretty = lambda t: t            # science text is left exactly as written
from kit import MC, MS, S, CZ, TB, B, GD, TK, EX, OD, MT, GR, Q, finish, Paper

STAGE = 6
MEDIA = 'media/s6'
def set_stage(n):
    """Use this kit for another Primary stage (e.g. 5): media folder, ids and course labels follow."""
    global STAGE, MEDIA
    STAGE = n; MEDIA = f'media/s{n}'
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
        sec.speak(SAYW[sec.sid])
    return core


class Section:
    def __init__(self, unit, sid, title, objs):
        self.u, self.sid, self.title, self.objs = unit, sid, title, objs
        self.n = int(sid.split('.')[1]); self.pools = {'r': [], 'p': [], 'a': []}; self.stops = []; self.vocab = []; self.lab = None; self.rows = []; self.sayw = []; self.extra_done = False
    def add(self, pool, q):
        lst = self.pools[pool]; qid = f"{self.u.pre}s{self.n}{pool}{len(lst) + 1:02d}"; q = finish(q, qid)
        if pool == 'a' and not q['prompt'].startswith('* Advanced.'): q['prompt'] = '* Advanced. ' + q['prompt']
        lst.append(q); return q
    def core(self, *qs): [self.add('r', q) for q in qs]; return self
    def prac(self, *qs): [self.add('p', q) for q in qs]; return self
    def adv(self, *qs): [self.add('a', q) for q in qs]; return self
    def words(self, rows):
        self.rows = rows; self.vocab = [{'w': w, 'def': d, 'audio': wa(w), 'emoji': e} for w, d, _, e in rows]; return self
    def speak(self, words):
        self.sayw = list(words); return self
    def stop(self, q, twin):
        i = len(self.stops) + 1; self.stops.append({'q': finish(q, f"{self.u.pre}s{self.n}v{i}"), 'twin': finish(twin, f"{self.u.pre}s{self.n}v{i}t")}); return self
    def labs(self, title, v, h):
        # questions inside the lab get their own ids
        for part, key in ((v, 'lv'), (h, 'lh')):
            part['qs'] = [finish(q, f"{self.u.pre}s{self.n}{key}{k + 1}") for k, q in enumerate(part.get('qs', []))]
        self.lab = {'title': title, 'v': v, 'h': h}; return self
    def extras(self, o):
        """More, and more varied, practice built from the lesson's words and its experiment:
        say every word aloud, listen and spell, listen for the meaning, match words to meanings, fill the gaps,
        and questions from the virtual lab (put results in order / sort into groups)."""
        if self.extra_done or not self.rows: return self
        self.extra_done = True; rows = self.rows; W = [r[0] for r in rows]; byw = {r[0]: r for r in rows}
        near = lambda w: [W[(W.index(w) + k) % len(W)] for k in (1, 2, 3)][:max(1, len(W) - 1)]
        # matching words and meanings, in groups of up to 5
        for i in range(0, len(rows), 5):
            grp = rows[i:i + 5]
            if len(grp) >= 3: self.prac(MT('Match each word to its meaning.', [(r[0], r[1]) for r in grp], o=o, skill='Vocabulary'))
        # fill the gaps with this lesson's words
        sents = [(r[0], r[2]) for r in rows if r[0].lower() in r[2].lower()]
        for i in range(0, len(sents), 3):
            grp = sents[i:i + 3]
            if len(grp) < 2: break
            text, acc = [], []
            for k, (w, sen) in enumerate(grp):
                j = sen.lower().index(w.lower()); text.append(sen[:j] + '{%d}' % k + sen[j + len(w):]); acc.append([w, w.lower()])
            bank = ', '.join(sorted({w for w, _ in grp} | set(near(grp[0][0])[:1])))
            self.prac(CZ(f'Fill each gap with a word from the lesson. Words to use: {bank}.', ' '.join(text), acc, o=o, skill='Vocabulary'))
        # the lab results, as data questions
        L = (self.lab or {}).get('v') or {}
        if L.get('kind') == 'test' and len(L.get('conds', [])) >= 3:
            cs = sorted(L['conds'], key=lambda c: c['val'])
            self.prac(OD(f"Results from the virtual lab “{L['title']}”. Put them in order, from the smallest {L['measure'].lower()} to the largest.", [f"{c['t']}: {c['val']} {L['unit']}" for c in cs], o=o, skill='Data'))
            big = cs[-1]; self.prac(MC(f"In the virtual lab “{L['title']}”, which gave the largest {L['measure'].lower()}?", big['t'], [(c['t'], f"{c['t']} gave {c['val']} {L['unit']}.") for c in cs[:-1]][:3], o=o, skill='Data', reason=f"{big['t']} gave {big['val']} {L['unit']}, the largest result."))
        if L.get('kind') == 'sort' and L.get('items'):
            self.prac(GD(L['intro'].split('.')[0].rstrip('?') + '.' if len(L['intro']) < 90 else 'Sort each card into the right group.', 'Group', [(it['t'], L['groups'][it['g']]) for it in L['items']], o=o))
        # listening: meaning of every word not met in Core, then spelling of the say-words
        for w in W:
            if w not in self.sayw: self.prac(LISTEN_MEANING(w, byw[w][1], near(w), o, d='M'))
        for w in self.sayw: self.prac(LISTEN_TYPE(w, o, d='M'))
        # speaking: every word of the lesson that is not already a Core say-the-word question
        for w in W:
            if w not in self.sayw: self.prac(SAY(w, byw[w][1], byw[w][3], o))
        return self
    def export(self, meta):
        stops = []
        for (t, rev), s in zip(meta['stops'], self.stops):
            stops.append({'id': f"v{self.sid.replace('.', '')}{chr(97 + len(stops))}", 't': t, 'review': [rev, t], 'note': 'Paused on the “Pause and think” card.', 'q': s['q'], 'twin': s['twin']})
        assert len(stops) == len(self.stops), (self.sid, len(meta['stops']), len(self.stops))
        caps = meta['captions']; used = [x['t'] for x in stops]; byw = {r[0]: r for r in self.rows}
        # in-video speaking stops were removed at the owner's request (speaking stays in Core and practice)
        for k, w in enumerate(self.sayw if VIDEO_SAY else []):
            for i, (t0, txt) in enumerate(caps):
                pat = r'\b' + re.escape(w.lower()) + r's?\b'
                if w.endswith('ing') and ' ' not in w: pat = r'\b' + re.escape(w.lower()[:-3]) + r'(?:s|es|ing)?\b'
                if t0 < 6 or not re.search(pat, txt.lower()): continue
                t = round((caps[i + 1][0] if i + 1 < len(caps) else meta['dur'] - 2.5) - 0.15, 2)
                if any(abs(t - u) < 4 for u in used): continue
                used.append(t); r = byw[w]
                q = finish(SAY(w, r[1], r[3], self.objs[0]), f"{self.u.pre}s{self.n}w{k + 1}"); q['prompt'] = f'New word! Listen to “{w}”, then say it out loud.'
                twin = finish(LISTEN_WORD(w, [x for x in self.sayw if x != w][:3], self.objs[0]), f"{self.u.pre}s{self.n}w{k + 1}t")
                stops.append({'id': f"v{self.sid.replace('.', '')}w{k + 1}", 't': t, 'review': [t0, t], 'note': 'Say the new word you just heard.', 'kind': 'say', 'q': q, 'twin': twin}); break
        stops.sort(key=lambda x: x['t'])
        assert len(self.pools['r']) == 8, (self.sid, 'core', len(self.pools['r']))
        return {'id': self.sid, 'title': self.title, 'objs': self.objs,
                'video': {'src': f"{MEDIA}/u{self.u.n}_s{self.n}.mp4", 'poster': f"{MEDIA}/u{self.u.n}_s{self.n}_poster.jpg", 'offset': 0, 'dur': meta['dur'], 'range': ''},
                'stops': stops, 'captions': meta['captions'], 'chapters': meta['chapters'],
                'req': self.pools['r'], 'prac': self.pools['p'], 'adv': self.pools['a'], 'vocab': self.vocab, 'lab': self.lab}


VIDEO_SAY = False


class Unit:
    def __init__(self, n, title, strand, blurb, objectives):
        self.n, self.title, self.strand, self.blurb, self.objectives = n, title, strand, blurb, objectives
        self.pre = f"p{STAGE}u{n:02d}"; self.sections = []; self.mind = []
    def section(self, sid, title, objs):
        s = Section(self, sid, title, objs); self.sections.append(s); return s
    def mindmap(self, *kids):
        self.mind = [{'id': f'k{i}', 't': t, 'd': d, 'obj': o, 'sec': s} for i, (t, d, o, s) in enumerate(kids)]
    def export(self, metas, tests, titles):
        for s in self.sections: s.extras(s.objs[0])
        secs = [s.export(metas[s.sid]) for s in self.sections]
        segs = {}
        for s in secs:
            for o in s['objs']: segs.setdefault(o, [s['id'], 0.0, s['video']['dur'], s['title']])
        return {'course': {'id': f's{STAGE}', 'title': f'Camday – Cambridge Primary Science — Stage {STAGE}', 'units': [{'n': i + 1, 't': t} for i, t in enumerate(titles)]},
                'unit': {'n': self.n, 'stage': STAGE, 'title': self.title, 'strandShort': self.strand.split(':')[0], 'blurb': self.blurb, 'strand': self.strand,
                         'framework': f'Cambridge Primary Science (0097), Stage {STAGE}', 'primary': True},
                'objectives': self.objectives, 'sections': secs, 'segments': segs, 'sources': [],
                'tests': {'A': tests[0], 'B': tests[1], 'pass': 0.7},
                'mindmap': {'id': 'root', 't': self.title, 'sec': None, 'kids': self.mind}}

TITLES = ['The human body', 'Materials: properties and changes', 'Rocks, the rock cycle and soil', 'Food chains and food webs', 'Forces and electricity', 'Light and the Solar System']
