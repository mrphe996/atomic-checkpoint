# -*- coding: utf-8 -*-
"""Question kinds for Stages 1-2, built from simple data. All tap-only. Written by the Atomic teaching team."""
from ykit import *


def lab(it): return f"{it[1]} {it[0]}"      # "🐶 dog"


def k_sort(items, cats, o, prompt=None, n=4, d="M", reason=""):
    """grid: put each picture in the right group. items: (name, emoji, cat)"""
    def t(r):
        ch = r.sample(items, min(n, len(items)))
        if len({c for _, _, c in ch}) < 2: return None
        return GD(prompt or f"Is each one {' or '.join(c.lower() for c in cats)}?", "Group", [(lab(x), x[2]) for x in ch], o=o, d=d, extra=cats, reason=reason)
    return t


def k_pick(items, cat, o, prompt, d="M", reason="", hint=""):
    """tap the one picture that is in group `cat`"""
    def t(r):
        yes = [x for x in items if x[2] == cat]; no = [x for x in items if x[2] != cat]
        if not yes or len(no) < 2: return None
        a = pick(r, yes); w = r.sample(no, min(3, len(no)))
        return PIC(prompt, a[0], [(x[0], f"{x[0].capitalize()} is {x[2].lower()}.") for x in w], pics={x[0]: x[1] for x in [a] + w}, o=o, d=d,
                   reason=reason or f"{a[0].capitalize()} is {cat.lower()}.", hint=hint)
    return t


def k_all(items, cat, o, prompt, d="H", reason=""):
    """multi: tap ALL the pictures in a group (more than one right answer – look at every one)"""
    def t(r):
        yes = [x for x in items if x[2] == cat]; no = [x for x in items if x[2] != cat]
        if len(yes) < 2 or len(no) < 2: return None
        a = r.sample(yes, min(len(yes), r.choice([2, 3]))); w = r.sample(no, 2)
        return MS(prompt, [lab(x) for x in a], [lab(x) for x in w], o=o, d=d, reason=reason or "Check every picture: " + ", ".join(f"{x[0]} is {x[2].lower()}" for x in a + w) + ".")
    return t


def k_odd(items, o, d="H", why="the group"):
    """odd one out: three from one group, one from another – the learner has to find what the three share"""
    def t(r):
        cats = sorted({x[2] for x in items})
        c1 = pick(r, cats); same = [x for x in items if x[2] == c1]; diff = [x for x in items if x[2] != c1]
        if len(same) < 3 or not diff: return None
        s3 = r.sample(same, 3); odd = pick(r, diff)
        return PIC("Which one is the odd one out?", odd[0], [(x[0], f"{x[0].capitalize()} belongs with the others: all three are {c1.lower()}.") for x in s3], pics={x[0]: x[1] for x in s3 + [odd]}, o=o, d=d,
                   hint=f"What is the same about three of them?", reason=f"{', '.join(x[0] for x in s3)} are all {c1.lower()}. {odd[0].capitalize()} is {odd[2].lower()}, so it is the odd one out.")
    return t


def k_claim(claims, o, d="H"):
    """a child says something – is it right? claims: (who-says text, True/False, why)"""
    def t(r):
        c, ok, why = pick(r, claims); name = pick(r, ["Ali", "Mia", "Sam", "Zara", "Leo", "Ana", "Kim", "Ben"])
        right = "Yes, that is right" if ok else "No, that is not right"
        return PIC(f"{name} says: “{c}” Is {name} right?", right, [("No, that is not right" if ok else "Yes, that is right", why)], pics={"Yes, that is right": "👍", "No, that is not right": "👎"}, o=o, d=d, reason=why)
    return t


def k_order(seqs, o, prompt, d="M"):
    def t(r):
        items, why = pick(r, seqs)
        return OD(prompt, list(items), o=o, d=d, reason=why)
    return t


def k_match(pairs, o, prompt, n=3, d="M"):
    def t(r):
        ch = r.sample(pairs, min(n, len(pairs)))
        return MT(prompt, ch, o=o, d=d, reason="; ".join(f"{a} – {b}" for a, b in ch) + ".")
    return t


def k_word(words, o, d="M"):
    """which word means …? (from the lesson word bank)"""
    def t(r):
        w = pick(r, words); ws = r.sample([x for x in words if x[0] != w[0]], min(2, len(words) - 1))
        return PIC(f"Which word means: {w[1]}?", w[0], [(x[0], f"{x[0].capitalize()} means {x[1]}.") for x in ws], pics={x[0]: x[2] for x in [w] + ws}, o=o, d=d, reason=f"{w[0].capitalize()} means {w[1]}.")
    return t


def k_count(items, o, prompt, d="M"):
    """count pictures in a group and choose the number"""
    def t(r):
        e = pick(r, items); n = r.randint(2, 9)
        return NUMS(prompt.format(name=e[0]), n, [x for x in {n - 1, n + 1, n + 2} if x > 0][:2], o=o, d=d, fig={"kind": "emojis", "groups": [[e[1], n]]}, reason=f"Count them one by one, touching each picture once: there are {n}.")
    return t
