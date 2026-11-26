# -*- coding: utf-8 -*-
"""Authoring kit for the Camday ESL courses, Stages 2–9 (course keys 22–29).
A lesson is written in a compact text format (see parse) and becomes: a lesson video script, two pause questions,
Core / Practice / Advanced / More practice pools, a word bank (word games, Stages 2–5) and Unit Test templates.
Every text, word list and question is an Camday original. Written by the Camday teaching team."""
import os, sys, re, json, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "young"))
import ykit
from ykit import *          # noqa: F401,F403  (kit, PIC, MC, MS, OD, MT, S, finish, ykey, YSection, YUnit, EXQ, pick, others)
ykit.TAP.add("short")       # from Stage 6 learners also type single missing words

NAMES = ["Ali", "Mia", "Sam", "Zara", "Leo", "Ana", "Kim", "Ben", "Noor", "Tom", "Lina", "Omar"]
TF = {"True": "👍", "False": "👎"}


# ------------------------------------------------------------------ lesson format
def parse(src):
    """One lesson per block.  Lines:
    L id | title | objective
    W word | meaning | emoji          (six or more)
    G rule name | rule | example 1 / example 2
    g sentence with ___ | right | wrong, wrong | why
    T text title | kind
    > text line (as many as needed; a blank '>' starts a new paragraph)
    q question | right | wrong, wrong | why
    t statement | T or F | why
    o a sentence whose words are put in order
    s right spelling | wrong, wrong"""
    out, cur = [], None
    for raw in src.strip().splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"): continue
        tag, _, rest = line.strip().partition(" ")
        f = [x.strip() for x in rest.split("|")]
        if tag == "L":
            cur = {"id": f[0], "title": f[1], "obj": f[2], "W": [], "g": [], "q": [], "t": [], "o": [], "s": [], "text": [], "G": None, "T": None}; out.append(cur)
        elif tag == "W": cur["W"].append((f[0], f[1], f[2] if len(f) > 2 else "📘"))
        elif tag == "G": cur["G"] = {"name": f[0], "rule": f[1], "ex": [e.strip() for e in f[2].split(" / ")]}
        elif tag == "g": cur["g"].append((f[0], f[1], [w.strip() for w in f[2].split(",")], f[3] if len(f) > 3 else ""))
        elif tag == "T": cur["T"] = {"title": f[0], "kind": f[1] if len(f) > 1 else "story"}
        elif tag == ">": cur["text"].append(rest.strip())
        elif tag == "q": cur["q"].append((f[0], f[1], [w.strip() for w in f[2].split(",")], f[3] if len(f) > 3 else ""))
        elif tag == "t": cur["t"].append((f[0], f[1].upper().startswith("T"), f[2] if len(f) > 2 else ""))
        elif tag == "o": cur["o"].append(rest.strip())
        elif tag == "s": cur["s"].append((f[0], [w.strip() for w in f[1].split(",")]))
        else: raise ValueError(f"unknown line: {line}")
    for L in out:
        L["paras"] = [t for t in L["text"] if t]     # every '>' line is one paragraph (or one line of a poem / dialogue)
        need = {"W": 6, "g": 7, "q": 5, "t": 3, "o": 3, "s": 4}
        for k, n in need.items(): assert len(L[k]) >= n, f"{L['id']}: needs {n} '{k}' lines (has {len(L[k])})"
        assert L["G"] and L["T"] and L["paras"], f"{L['id']}: grammar rule, text title and text are required"
        for s_, r, w, _ in L["g"]: assert "___" in s_ and r not in w, f"{L['id']}: bad grammar item {s_}"
    return out


def ctx_of(L):
    return f"{L['T']['title']}\n" + "\n".join(L["paras"])


# ------------------------------------------------------------------ question templates (from one lesson)
def tpl_mean(L, o, pics):
    W = L["W"]
    def t(r):
        w = pick(r, W); ws = r.sample([x for x in W if x[0] != w[0]], 2)
        return PIC(f"Which word means “{w[1]}”?", w[0], [(x[0], f"“{x[0]}” means {x[1]}.") for x in ws], pics={x[0]: x[2] for x in [w] + ws} if pics else None, o=o, reason=f"“{w[0]}” means {w[1]}.")
    return t


def tpl_match(L, o):
    def t(r):
        ch = r.sample(L["W"], 3)
        return MT("Match each word to its meaning.", [(w, d) for w, d, _ in ch], o=o, reason="; ".join(f"{w} – {d}" for w, d, _ in ch) + ".")
    return t


def tpl_gram(items, o, d="M"):
    def t(r):
        s_, right, wr, why = pick(r, items)
        return MC(f"Choose the word that fits.  {s_}", right, [(w, why or "Check the rule again.") for w in wr], o=o, d=d, reason=why or f"The answer is “{right}”.")
    return t


def tpl_type(items, o):
    """typed gap fill (Stages 6–9): only single-word answers"""
    ok = [x for x in items if re.fullmatch(r"[A-Za-z'’-]+", x[1])]
    if not ok: return None
    def t(r):
        s_, right, wr, why = pick(r, ok)
        return S(f"Type the missing word.  {s_}", [right, right.lower()], o=o, d="H", reason=why or f"The answer is “{right}”.")
    return t


def tpl_read(L, items, o, d="M"):
    ctx = ctx_of(L)
    def t(r):
        q, right, wr, why = pick(r, items)
        return MC(f"Read “{L['T']['title']}”. {q}", right, [(w, why or "Look back at the text.") for w in wr], o=o, d=d, ctx=ctx, reason=why or f"The text tells us: {right}.")
    return t


def tpl_tf(L, items, o, d="H"):
    ctx = ctx_of(L)
    def t(r):
        st, ok, why = pick(r, items)
        return PIC(f"Read “{L['T']['title']}”. True or false?  “{st}”", "True" if ok else "False", [("False" if ok else "True", why or "Look back at the text.")], pics=TF, o=o, d=d, ctx=ctx, reason=why)
    return t


def tpl_order(items, o, d="H"):
    items = [x for x in items if 3 <= len(x.split()) <= 12]
    def t(r):
        s_ = pick(r, items); words = s_.split()
        return OD("Put the words in order to make a sentence.", words, o=o, d=d, reason=f"“{s_}”")
    return t


def tpl_spell(items, o):
    def t(r):
        right, wr = pick(r, items)
        return MC("Which word is spelt correctly?", right, [(w, f"The correct spelling is “{right}”.") for w in wr], o=o, reason=f"The correct spelling is “{right}”.")
    return t


def tpl_who(L, o):
    """a learner uses a word in a sentence – is it used correctly? (meaning in context)"""
    W = L["W"]
    def t(r):
        w = pick(r, W); other = pick(r, [x for x in W if x[0] != w[0]]); nm = pick(r, NAMES); ok = r.random() < 0.5
        meaning = w[1] if ok else other[1]
        return PIC(f"{nm} says: “‘{w[0].capitalize()}’ means {meaning}.” Is {nm} right?", "True" if ok else "False", [("False" if ok else "True", f"“{w[0]}” means {w[1]}.")], pics=TF, o=o, d="H", reason=f"“{w[0]}” means {w[1]}.")
    return t


# ------------------------------------------------------------------ sections and units
class ESection(YSection):
    def export(self, dur):
        x = super().export(dur)
        return x


class EUnit(YUnit):
    def __init__(self, n, title, strand, blurb, objectives, stage):
        super().__init__(n, title, strand, blurb, objectives, stage, "esl")
        self.pre = f"e{stage}u{n:02d}"; self.lessons = []
    def section(self, sid, title, objs):
        s = ESection(self, sid, title, objs); s.rng = random.Random(f"esl{self.stage}-{sid}"); self.sections.append(s); return s

    def add(self, L):
        st = self.stage; o = "O" + L["id"].split(".")[1]
        s = self.section(L["id"], L["title"], [o]); s.L = L
        s.words(*L["W"])
        g_pool, g_res = L["g"][:-2], L["g"][-2:]
        q_pool, q_res = L["q"][:-1], L["q"][-1:]
        t_pool, t_res = L["t"][:-1], L["t"][-1:]
        s_pool, s_res = L["s"][:-1], L["s"][-1:]
        pics = st <= 5
        # two pause questions for the video (never reused anywhere else)
        w0 = L["W"][0]; ws = L["W"][1:3]
        s.check(PIC(f"Which word means “{w0[1]}”?", w0[0], [(x[0], f"“{x[0]}” means {x[1]}.") for x in ws], pics={x[0]: x[2] for x in [w0] + ws} if pics else None, o=o, reason=f"“{w0[0]}” means {w0[1]}."))
        q, right, wr, why = q_pool[0]
        s.check(MC(f"{q}", right, [(w, why or "Listen to the text again.") for w in wr], o=o, reason=why))
        q_pool = q_pool[1:]
        T = [tpl_mean(L, o, pics), tpl_match(L, o), tpl_gram(g_pool, o), tpl_read(L, q_pool, o), tpl_spell(s_pool, o)]
        deep = [tpl_tf(L, t_pool, o), tpl_order(L["o"], o), tpl_who(L, o), tpl_gram(g_pool, o, d="H")]
        if st >= 6:
            tt = tpl_type(g_pool, o)
            if tt: deep.append(tt)
        s.young(T, EXQ(tpl_gram(g_pool[:1], o)), deep)
        # test-only items
        self.ttpl(L["id"], tpl_gram(g_res, o), tpl_read(L, q_res, o), tpl_tf(L, t_res, o), tpl_spell(s_res, o))
        if st >= 6:
            tt = tpl_type(g_res, o)
            if tt: self.ttpl(L["id"], tt)
        self.lessons.append(L)
        return s

    def eexport(self, titles, timing):
        """timing: {sid: {dur, src, poster, stops:[t, t], review:[[a,b],[a,b]], captions, chapters}} from the video render (or None)"""
        tests = self.tests()
        st = self.stage; prim = st <= 6
        secs = []
        for s in self.sections:
            x = s.export(180); tm = (timing or {}).get(s.sid)
            if tm:
                x["video"] = {"src": tm["src"], "poster": tm["poster"], "offset": 0, "dur": tm["dur"], "range": ""}
                x["captions"] = tm["captions"]; x["chapters"] = tm["chapters"]
                for i, stp in enumerate(x["stops"]):
                    stp["t"] = tm["stops"][i]; stp["review"] = tm["review"][i]; stp["note"] = "Pause question"; stp.pop("after", None)
            else:
                x["video"] = {"src": None, "offset": 0, "dur": 180, "range": ""}
                for i, stp in enumerate(x["stops"]): stp["t"] = 60 + 60 * i; stp["review"] = [0, 0]; stp.pop("after", None)
            x.pop("lesson", None)
            secs.append(x)
        segs = {}
        for s in secs:
            for o in s["objs"]: segs.setdefault(o, [s["id"], 0.0, s["video"]["dur"], s["title"]])
        lvl = "Primary" if prim else "Lower Secondary"
        fw = f"Cambridge {lvl} English as a Second Language ({'0057' if prim else '0876'}), Stage {st}"
        return {"course": {"id": f"s{20 + st}", "title": f"Camday – Cambridge {lvl} English as a Second Language — Stage {st}", "units": [{"n": i + 1, "t": t} for i, t in enumerate(titles)]},
                "unit": {"n": self.n, "stage": 20 + st, "title": self.title, "strandShort": self.strand, "blurb": self.blurb, "strand": self.strand,
                         "framework": fw, "subject": "esl", "esl": True, "young": st <= 4},
                "objectives": self.objectives, "sections": secs, "segments": segs, "sources": [],
                "tests": {"A": tests[0], "B": tests[1], "pass": 0.7},
                "mindmap": {"id": "root", "t": self.title, "sec": None, "kids": [{"id": f"k{i}", "t": L["title"], "d": L["obj"], "obj": "O" + L["id"].split(".")[1], "sec": L["id"]} for i, L in enumerate(self.lessons)]}}


def make_unit(stage, n, title, strand, blurb, lessons):
    objs = {f"O{L['id'].split('.')[1]}": {"code": f"Stage {stage} · {strand}", "sec": L["id"], "codeNote": "", "t": L["obj"]} for L in lessons}
    u = EUnit(n, title, strand, blurb, objs, stage)
    for L in lessons: u.add(L)
    return u


# ------------------------------------------------------------------ video script
def _sp(x):
    """a heading made speakable: no slashes, no trailing '…' or doubled stops"""
    x = x.replace(" / ", " and ").replace("…", "").strip()
    return x.rstrip(".")


def _say(x):
    """written text made speakable: slashes become pauses or 'or', arrows become 'becomes'"""
    x = x.replace(" → ", " becomes ").replace(" / ", ", ")
    x = re.sub(r"\b(\w+) ?/ ?(\w+)\b", r"\1 or \2", x)
    return x


def _lc(x):
    return x if (x[:2] in ("I ", "I'") or x[1:2].isupper()) else x[:1].lower() + x[1:]


def _end(x):
    return x if x[-1:] in ".!?" else x + "."


def script(L, stage, unit_title):
    """scenes: [{k, say:[sentences], ...display}] – the narration of one lesson video"""
    W = L["W"]; G = L["G"]; T = L["T"]
    sc = [{"k": "title", "head": L["title"], "sub": f"Stage {stage} English · {unit_title}", "obj": L["obj"], "words": [[w, e] for w, _, e in W],
           "say": [f"Hello, and welcome to Camday English, Stage {stage}.", f"In this lesson: {_end(L['title'])}", _end(L['obj'])]}]
    for i in range(0, len(W), 3):
        grp = W[i:i + 3]
        say = ["Here are some new words." if i == 0 else "And some more words."]
        for w, d, e in grp: say += [f"{w.capitalize()}.", f"{d[0].upper() + d[1:]}."]
        if stage <= 5: say.append("Listen and say them. " + ' <break time="1.2s" /> '.join(w for w, _, _ in grp) + ".")
        sc.append({"k": "words", "items": grp, "say": say})
    sc.append({"k": "pause", "n": 1, "say": ["Time for a question. The video will stop.", "Which word means: " + W[0][1] + "?"]})
    sc.append({"k": "grammar", "head": G["name"], "rule": G["rule"], "ex": G["ex"],
               "say": [f"Now some grammar: {_end(_sp(G['name']))}", _say(G["rule"])] + [_end(f"For example: {e}".replace(" → ", " becomes ")) for e in G["ex"]]})
    paras = L["paras"]
    # the text: one scene per paragraph (or two short paragraphs together)
    chunks, cur = [], []
    for p in paras:
        cur.append(p)
        if sum(len(x) for x in cur) > (260 if stage <= 4 else 420): chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    for j, ch in enumerate(chunks):
        say = ([f"Now listen, and read along. {_end(T['title'])}"] if j == 0 else []) + [_say(p) for p in ch]
        sc.append({"k": "text", "head": T["title"], "kind": T["kind"], "paras": ch, "part": j, "say": say})
    q0 = L["q"][0]
    sc.append({"k": "pause", "n": 2, "say": ["Another question. The video will stop.", q0[0]]})
    sc.append({"k": "recap", "head": "What we learned", "items": [f"New words: " + ", ".join(w for w, _, _ in W[:6]), f"{G['name']}: {G['ex'][0]}", f"We read: {T['title']}"],
               "say": ["Well done!", "Today you learned new words, like " + ", ".join(w for w, _, _ in W[:3]) + ".", f"You practised {_lc(_sp(G['name']))}.", f"And you read {_end(T['title'])}", "Now try the practice questions. See you next time!"]})
    return sc
