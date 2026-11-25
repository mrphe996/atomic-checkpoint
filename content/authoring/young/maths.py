# -*- coding: utf-8 -*-
"""Cambridge Primary Mathematics Stages 1 and 2 (ages 5-7) – Atomic picture lessons and tap-only practice.
Topics follow the Cambridge Primary Mathematics curriculum framework (0096) for Stages 1 and 2; every lesson, picture,
question and explanation is an Atomic original. Written by the Atomic teaching team."""
from qbank import *
from science import build_sec, EM

THINGS = [("apple", "🍎"), ("star", "⭐"), ("ball", "⚽"), ("fish", "🐟"), ("duck", "🦆"), ("car", "🚗"), ("flower", "🌸"), ("cookie", "🍪"), ("balloon", "🎈"), ("strawberry", "🍓")]
NAMES = ["Ali", "Mia", "Sam", "Zara", "Leo", "Ana", "Kim", "Ben", "Noor", "Tom"]
WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]


def near(r, n, lo=0, hi=100, k=2, far=False):
    c = [n - 1, n + 1, n - 2, n + 2] + ([n + 10, n - 10] if far else [])
    c = [x for x in dict.fromkeys(c) if lo <= x <= hi and x != n]; r.shuffle(c)
    return c[:k]


def thing(r): return pick(r, THINGS)


def unit(n, title, strand, blurb, o1, o2, stage):
    O = {"O1": {"code": f"Stage {stage} · {strand}", "sec": f"{n}.1", "codeNote": "", "t": o1}, "O2": {"code": f"Stage {stage} · {strand}", "sec": f"{n}.2", "codeNote": "", "t": o2}}
    return YUnit(n, title, strand, blurb, O, stage, "maths")


YN = {"Yes": "👍", "No": "👎"}


def claim_n(o, maker, d="H"):
    """a child counts or works something out – is it right? maker(r) -> (statement, true?, why, fig)"""
    def t(r):
        c, ok, why, fig = maker(r); nm = pick(r, NAMES)
        return PIC(f"{nm} says: “{c}” Is {nm} right?", "Yes" if ok else "No", [("No" if ok else "Yes", why)], pics=YN, o=o, d=d, reason=why, fig=fig)
    return t


# -------------------------------------------------------------- number templates
def t_count(o, lo=1, hi=10, per=5):
    def t(r):
        n = r.randint(lo, hi); nm, e = thing(r)
        return NUMS(f"How many {nm}s are there?", n, near(r, n, 0, hi + 2), o=o, fig={"kind": "emojis", "groups": [[e, n]], "per": per},
                    reason=f"Touch each {nm} once as you count: there are {n}.", hint="Count each one once. Say the numbers in order.")
    return t


def t_frame(o, lo=1, hi=10):
    def t(r):
        n = r.randint(lo, hi)
        return NUMS("How many dots are in the ten frame?" if hi <= 10 else "How many dots are in the ten frames?", n, near(r, n, 0, max(hi, 10) + 2), o=o, fig={"kind": "tenframe", "n": n, "of": 20 if hi > 10 else 10},
                    reason=(f"A full row is 5. {n} = 5 + {n - 5}." if 5 < n <= 10 else f"A full ten frame is 10. {n} = 10 + {n - 10}." if n > 10 else f"Count the dots: {n}."))
    return t


def t_word(o, lo=0, hi=10):
    def t(r):
        ns = r.sample(range(lo, hi + 1), 3)
        return MT("Match each number to its word.", [(str(n), WORDS[n]) for n in ns], o=o, reason="; ".join(f"{n} is {WORDS[n]}" for n in ns) + ".")
    return t


def t_more_less(o, lo=0, hi=10, k=1):
    def t(r):
        n = r.randint(lo + k, hi - k); up = r.random() < 0.5; a = n + k if up else n - k
        word = "more" if up else "less"
        return NUMS(f"What is {k} {word} than {n}?", a, near(r, a, 0, hi + 2), o=o, fig={"kind": "numline", "min": lo, "max": hi, "mark": n} if hi <= 20 else None,
                    reason=f"{k} {word} than {n} is {a}: {'count on' if up else 'count back'} {k}.")
    return t


def t_order(o, lo=0, hi=10, n=4):
    def t(r):
        ns = sorted(r.sample(range(lo, hi + 1), n)); desc = r.random() < 0.3
        return OD(f"Put the numbers in order, {'largest' if desc else 'smallest'} first.", [str(x) for x in (ns[::-1] if desc else ns)], o=o, reason=", ".join(str(x) for x in (ns[::-1] if desc else ns)) + ".")
    return t


def t_missing(o, lo=0, hi=10, step=1):
    def t(r):
        a = r.randint(lo, hi - 4 * step) // step * step if step > 1 else r.randint(lo, hi - 4); seq = [a + i * step for i in range(5)]; i = r.randint(1, 3); ans = seq[i]
        shown = ", ".join("?" if j == i else str(x) for j, x in enumerate(seq))
        return NUMS(f"Which number is missing? {shown}", ans, [x for x in near(r, ans, 0, hi + 10) if x not in seq][:2] or [ans + 3, ans + 5], o=o,
                    reason=f"The numbers go up in {step}s: {', '.join(map(str, seq))}.")
    return t


def t_bigger(o, lo=0, hi=10, word=None):
    def t(r):
        a, b, c = r.sample(range(lo, hi + 1), 3); big = r.random() < 0.6
        right = max(a, b, c) if big else min(a, b, c)
        return PIC(f"Which number is the {'largest' if big else 'smallest'}?", str(right), [(str(x), "") for x in (a, b, c) if x != right], o=o,
                   reason=f"{right} is the {'largest' if big else 'smallest'}: it comes {'last' if big else 'first'} when you count.")
    return t


def t_compare_groups(o, hi=10):
    def t(r):
        a, b = r.sample(range(1, hi + 1), 2); (n1, e1), (n2, e2) = r.sample(THINGS, 2); more = r.random() < 0.5
        right = n1 if (a > b) == more else n2
        return PIC(f"Are there more {n1}s or more {n2}s?" if more else f"Are there fewer {n1}s or fewer {n2}s?", f"{right}s", [(f"{n2 if right == n1 else n1}s", "")],
                   pics={f"{n1}s": e1, f"{n2}s": e2}, o=o, fig={"kind": "emojis", "groups": [[e1, a], [e2, b]], "per": 10},
                   reason=f"There are {a} {n1}s and {b} {n2}s, so there are {'more' if more else 'fewer'} {right}s.", hint="Line them up and match them one to one.")
    return t


def t_numline(o, lo=0, hi=10):
    def t(r):
        n = r.randint(lo + 1, hi - 1)
        return NUMS("Which number is the arrow pointing to?", n, near(r, n, lo, hi), o=o, fig={"kind": "numline", "min": lo, "max": hi, "mark": n}, reason=f"Count along from {lo}: the arrow points to {n}.")
    return t


# -------------------------------------------------------------- calculation templates
def t_add_pics(o, hi=10):
    def t(r):
        a = r.randint(1, hi - 1); b = r.randint(1, hi - a); nm, e = thing(r)
        return NUMS(f"{a} {nm}s and {b} more {nm}s. How many {nm}s altogether?", a + b, near(r, a + b, 0, hi + 2), o=o, fig={"kind": "emojis", "groups": [[e, a], [e, b]], "plus": True, "per": 10},
                    reason=f"{a} + {b} = {a + b}. Start at {a} and count on {b}.", hint=f"Start at {max(a, b)} and count on.")
    return t


def t_add(o, hi=10, lo_sum=2):
    def t(r):
        s = r.randint(lo_sum, hi); a = r.randint(0, s); b = s - a
        return NUMS(f"{a} + {b} = ?", s, near(r, s, 0, hi + 2), o=o, reason=f"{a} + {b} = {s}.")
    return t


def t_bond(o, total=10):
    def t(r):
        a = r.randint(1, total - 1)
        return NUMS(f"{a} + ? = {total}", total - a, near(r, total - a, 0, total), o=o, fig={"kind": "tenframe", "n": a, "of": 10} if total == 10 else None,
                    reason=f"{a} and {total - a} make {total}." + (" Count the empty boxes." if total == 10 else ""))
    return t


def t_sub_pics(o, hi=10):
    def t(r):
        a = r.randint(3, hi); b = r.randint(1, a - 1); nm, e = pick(r, [("bird", "🐦"), ("balloon", "🎈"), ("frog", "🐸"), ("butterfly", "🦋")])
        verb = {"bird": "fly away", "balloon": "pop", "frog": "jump away", "butterfly": "fly away"}[nm]
        return NUMS(f"There are {a} {nm}s. {b} {verb}. How many are left?", a - b, near(r, a - b, 0, hi), o=o, fig={"kind": "emojis", "groups": [[e, a]], "per": 10},
                    reason=f"{a} − {b} = {a - b}. Count back {b} from {a}.", hint=f"Cover {b} of them and count the rest.")
    return t


def t_sub(o, hi=10):
    def t(r):
        a = r.randint(2, hi); b = r.randint(0, a)
        return NUMS(f"{a} − {b} = ?", a - b, near(r, a - b, 0, hi), o=o, reason=f"{a} − {b} = {a - b}.")
    return t


def t_difference(o, hi=10):
    def t(r):
        a, b = sorted(r.sample(range(1, hi + 1), 2)); n1, n2 = r.sample(NAMES, 2); nm, e = thing(r)
        return NUMS(f"{n1} has {a} {nm}s. {n2} has {b} {nm}s. How many more does {n2} have?", b - a, near(r, b - a, 0, hi), o=o, d="H", fig={"kind": "emojis", "groups": [[e, a], [e, b]], "per": 10},
                    reason=f"Match them up: {b} − {a} = {b - a} more.", hint="Line them up. How many have no partner?")
    return t


def t_missing_add(o, hi=10):
    def t(r):
        s = r.randint(4, hi); a = r.randint(1, s - 1)
        return NUMS(f"? + {a} = {s}", s - a, near(r, s - a, 0, hi), o=o, d="H", reason=f"{s} − {a} = {s - a}, so {s - a} + {a} = {s}.")
    return t


def t_fact_claim(o, hi=10):
    def mk(r):
        a, b = r.randint(1, hi // 2), r.randint(1, hi // 2); kind = r.randint(0, 3)
        if kind == 0: return (f"{a} + {b} is the same as {b} + {a}.", True, "You can add in any order: the total is the same.", None)
        if kind == 1: return (f"{a + b} − {a} = {b}.", True, f"{a} + {b} = {a + b}, so taking {a} away leaves {b}.", None)
        if kind == 2: return (f"{a + b} − {a} = {b + 1}.", False, f"{a + b} − {a} = {b}, because {a} + {b} = {a + b}.", None)
        return (f"{max(a, b)} − {min(a, b)} is the same as {min(a, b)} − {max(a, b)}.", a == b, "Order matters when you take away: start from the bigger number." if a != b else "Both are 0.", None)
    return claim_n(o, mk)


def t_double(o, hi=10):
    def t(r):
        a = r.randint(1, hi); h = r.random() < 0.4 and a % 2 == 0
        if h: return NUMS(f"What is half of {a}?", a // 2, near(r, a // 2, 0, hi), o=o, reason=f"{a // 2} + {a // 2} = {a}, so half of {a} is {a // 2}.", fig={"kind": "emojis", "groups": [["🍪", a]], "per": a // 2})
        return NUMS(f"Double {a} is…", 2 * a, near(r, 2 * a, 0, 2 * hi + 2), o=o, reason=f"Double {a} is {a} + {a} = {2 * a}.", fig={"kind": "emojis", "groups": [["🐞", a], ["🐞", a]], "plus": True, "per": 10})
    return t


# -------------------------------------------------------------- shapes
SH2 = {"triangle": [[0, 0], [4, 0], [2, 3.4]], "square": [[0, 0], [3, 0], [3, 3], [0, 3]], "rectangle": [[0, 0], [5, 0], [5, 2.5], [0, 2.5]], "pentagon": [[1, 0], [3, 0], [3.8, 2], [2, 3.4], [0.2, 2]],
       "hexagon": [[1, 0], [3, 0], [4, 1.7], [3, 3.4], [1, 3.4], [0, 1.7]], "octagon": [[1, 0], [2.4, 0], [3.4, 1], [3.4, 2.4], [2.4, 3.4], [1, 3.4], [0, 2.4], [0, 1]]}
SIDES = {"triangle": 3, "square": 4, "rectangle": 4, "pentagon": 5, "hexagon": 6, "octagon": 8}


def shp(name, r=None):
    pts = SH2[name]
    if r is not None:
        k = r.choice([1, 1.3, 0.8]); pts = [[x * k, y] for x, y in pts]
    return {"kind": "shape", "pts": pts}


def t_shape_name(o, names):
    def t(r):
        n = pick(r, names)
        return PIC("What is the name of this shape?", n, [(x, f"A {x} has {SIDES[x]} sides.") for x in others(r, names, n)], o=o, fig=shp(n, r), reason=f"It has {SIDES[n]} straight sides, so it is a {n}.")
    return t


def t_sides(o, names, what="sides"):
    def t(r):
        n = pick(r, names)
        return NUMS(f"How many {what} does this shape have?", SIDES[n], near(r, SIDES[n], 2, 9), o=o, fig=shp(n, r), reason=f"A {n} has {SIDES[n]} {what}. Count them, starting from one {what[:-1]} and going round.")
    return t


S3 = [("ball", "⚽", "Sphere"), ("orange", "🍊", "Sphere"), ("globe", "🌍", "Sphere"), ("dice", "🎲", "Cube"), ("ice cube", "🧊", "Cube"), ("gift box", "🎁", "Cube"), ("tin", "🥫", "Cylinder"), ("candle", "🕯️", "Cylinder"), ("drum", "🥁", "Cylinder"),
      ("ice-cream cone", "🍦", "Cone"), ("party hat", "🥳", "Cone"), ("traffic cone", "🚧", "Cone"), ("cereal box", "📦", "Cuboid"), ("book", "📕", "Cuboid"), ("brick", "🧱", "Cuboid")]


# -------------------------------------------------------------- measures and time
TALL = [("mouse", "🐭", 1), ("cat", "🐈", 2), ("dog", "🐕", 3), ("child", "🧒", 4), ("horse", "🐎", 5), ("giraffe", "🦒", 6), ("tree", "🌳", 7)]
HEAVY = [("feather", "🪶", 1), ("apple", "🍎", 2), ("book", "📕", 3), ("cat", "🐈", 4), ("child", "🧒", 5), ("cow", "🐄", 6), ("elephant", "🐘", 7)]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def t_compare_size(o, items, big_word, small_word):
    def t(r):
        ch = r.sample(items, 3); big = r.random() < 0.5; right = max(ch, key=lambda x: x[2]) if big else min(ch, key=lambda x: x[2])
        return PIC(f"Which is the {big_word if big else small_word}?", right[0], [(x[0], "") for x in ch if x is not right], pics={x[0]: x[1] for x in ch}, o=o,
                   reason=f"The {right[0]} is the {big_word if big else small_word} of the three.")
    return t


def t_cubes(o, hi=10):
    def t(r):
        n = r.randint(2, hi); nm, e = pick(r, [("pencil", "✏️"), ("worm", "🪱"), ("snake", "🐍"), ("ribbon", "🎀")])
        return NUMS(f"The {nm} is as long as this line of cubes. How many cubes long is the {nm}?", n, near(r, n, 1, hi + 2), o=o, fig={"kind": "emojis", "groups": [["🟦", n]], "per": 12, "size": 30},
                    reason=f"Count the cubes: {n}. The {nm} is {n} cubes long.")
    return t


def oclock(h, m=0):
    if m == 0: return f"{h} o'clock"
    if m == 30: return f"half past {h}"
    if m == 15: return f"quarter past {h}"
    if m == 45: return f"quarter to {h % 12 + 1}"
    return f"{h}:{m:02d}"


def t_clock(o, mins=(0, 30)):
    def t(r):
        h = r.randint(1, 12); m = pick(r, list(mins)); right = oclock(h, m)
        w = {oclock(h % 12 + 1, m), oclock(h, 30 if m == 0 else 0) if len(mins) > 1 or m else oclock((h + 1) % 12 + 1, 0), oclock(h - 1 if h > 1 else 12, m)} - {right}
        w = list(w)[:2]
        return PIC("What time does the clock show?", right, [(x, "") for x in w], o=o, fig={"kind": "clock", "h": h, "m": m},
                   reason=("The long hand points to 12 and the short hand points to " + str(h) + f", so it is {right}." if m == 0 else
                           f"The long hand points to 6 (half way round) and the short hand is just past {h}, so it is {right}." if m == 30 else
                           f"The long hand points to 3 (a quarter of the way round), so it is {right}." if m == 15 else f"The long hand points to 9: a quarter of an hour to go, so it is {right}."))
    return t


def t_day_after(o):
    def t(r):
        i = r.randint(0, 6); after = r.random() < 0.6; a = DAYS[(i + 1) % 7] if after else DAYS[(i - 1) % 7]
        return PIC(f"Which day comes {'after' if after else 'before'} {DAYS[i]}?", a, [(x, "") for x in others(r, [d for d in DAYS if d != DAYS[i]], a)], o=o, reason=f"The days go … {DAYS[(i - 1) % 7]}, {DAYS[i]}, {DAYS[(i + 1) % 7]} …", pic="📅")
    return t


def t_days_order(o, src=DAYS, k=4, what="days"):
    def t(r):
        i = r.randint(0, len(src) - 1); seq = [src[(i + j) % len(src)] for j in range(k)]
        return OD(f"Put the {what} in order, starting with {seq[0]}.", seq, o=o, reason=" → ".join(seq) + ".")
    return t


# -------------------------------------------------------------- fractions and data
def t_half_shape(o, fracs=(("a half", 2, 1),)):
    def t(r):
        name, d, k = pick(r, list(fracs)); is_it = r.random() < 0.55
        if is_it: vals = [1] * d; shade = list(range(k))
        else:
            vals = pick(r, [[2, 1], [3, 1], [1, 1, 1], [3, 2]]); shade = [0]
        fig = {"kind": "pie", "values": vals, "shade": shade, "labels": [""] * len(vals)}
        eq = len(set(vals)) == 1
        ok = is_it
        why = (f"The circle is cut into {d} equal parts and {k} {'is' if k == 1 else 'are'} shaded, so it shows {name}." if ok else
               ("The parts are not the same size, so it does not show " + name + "." if not eq else f"It is cut into {len(vals)} equal parts, not {d}."))
        return PIC(f"Does the shaded part show {name}?", "Yes" if ok else "No", [("No" if ok else "Yes", why)], pics=YN, o=o, fig=fig, reason=why)
    return t


def t_frac_amount(o, fracs=((2, 1),), hi=20):
    def t(r):
        d, k = pick(r, list(fracs)); n = d * r.randint(1, hi // d); ans = n // d * k; nm, e = thing(r)
        nmf = {(2, 1): "half", (4, 1): "a quarter", (4, 3): "three quarters", (4, 2): "two quarters"}[(d, k)]
        return NUMS(f"What is {nmf} of {n} {nm}s?", ans, near(r, ans, 0, n), o=o, fig={"kind": "emojis", "groups": [[e, n]], "per": n // d if n // d > 1 else 5},
                    reason=f"Share {n} into {d} equal groups: {n // d} in each. {nmf.capitalize()} is {k} group{'s' if k > 1 else ''}: {ans}.", hint=f"Share them into {d} equal groups.")
    return t


def t_pattern(o, hard=False):
    SETS = [["🔴", "🔵"], ["⭐", "🌙"], ["🍎", "🍌"], ["🐶", "🐱", "🐭"], ["🔺", "🟦", "🟦"], ["🟢", "🟢", "🟡"], ["🌸", "🍃", "🍃", "🌸"]]
    def t(r):
        unit_ = pick(r, SETS if hard else SETS[:5]); n = r.randint(len(unit_) * 2, len(unit_) * 2 + 2)
        seq = [unit_[i % len(unit_)] for i in range(n)]; nxt = unit_[n % len(unit_)]
        opts = list(dict.fromkeys(unit_ + [pick(r, ["🟣", "🟠", "⚫"])]))
        return PIC("What comes next in the pattern?  " + " ".join(seq) + "  ?", nxt, [(x, "") for x in opts if x != nxt][:2], pics={x: x for x in opts}, o=o, d="H" if hard else "M",
                   reason=f"The pattern repeats {' '.join(unit_)}, so next is {nxt}.", hint="Find the part that repeats.")
    return t


FRUITS = [("apples", "🍎"), ("bananas", "🍌"), ("grapes", "🍇"), ("pears", "🍐"), ("oranges", "🍊")]
PETS = [("dogs", "🐶"), ("cats", "🐱"), ("fish", "🐟"), ("rabbits", "🐰"), ("birds", "🐦")]


def chart(r, hi=8, k=4, src=None):
    cats = r.sample(src or FRUITS, k); vals = r.sample(range(1, hi + 1), k)
    return cats, vals


def t_pictogram(o, hi=8, k=3):
    def t(r):
        cats, vals = chart(r, hi, k); i = r.randrange(k); q = r.randint(0, 2)
        fig = {"kind": "emojis", "groups": [[e, v] for (_, e), v in zip(cats, vals)], "per": 10, "size": 32}
        key = "The pictogram shows the fruit children chose. " + "  ".join(f"{e} = {c}" for c, e in cats) + "."
        if q == 0: return NUMS(key + f" How many children chose {cats[i][0]}?", vals[i], near(r, vals[i], 0, hi + 2), o=o, fig=fig, reason=f"Count the {cats[i][1]} row: {vals[i]}.")
        j = max(range(k), key=lambda x: vals[x]) if q == 1 else min(range(k), key=lambda x: vals[x])
        return PIC(key + f" Which fruit did the {'most' if q == 1 else 'fewest'} children choose?", cats[j][0], [(c, "") for c, _ in cats if c != cats[j][0]], pics={c: e for c, e in cats}, o=o, fig=fig,
                   reason=f"The {cats[j][0]} row is the {'longest' if q == 1 else 'shortest'}: {vals[j]}.")
    return t


def t_barchart(o, hi=10, k=4, src=None, more=True):
    def t(r):
        cats, vals = chart(r, hi, k, src or PETS); fig = {"kind": "barchart", "labels": [c for c, _ in cats], "values": vals, "ymax": hi, "step": 1 if hi <= 10 else 2, "ylabel": "Number of children"}
        q = r.randint(0, 2 if more else 1); i, j = r.sample(range(k), 2)
        if q == 0: return NUMS(f"The block graph shows children's favourite pets. How many children chose {cats[i][0]}?", vals[i], near(r, vals[i], 0, hi), o=o, fig=fig, reason=f"Read across from the top of the {cats[i][0]} bar: {vals[i]}.")
        if q == 1:
            m = max(range(k), key=lambda x: vals[x])
            return PIC("The block graph shows children's favourite pets. Which pet is the most popular?", cats[m][0], [(c, "") for c, _ in cats if c != cats[m][0]][:3], pics={c: e for c, e in cats}, o=o, fig=fig, reason=f"{cats[m][0].capitalize()} has the tallest bar ({vals[m]}).")
        a, b = (i, j) if vals[i] > vals[j] else (j, i)
        return NUMS(f"The block graph shows children's favourite pets. How many more children chose {cats[a][0]} than {cats[b][0]}?", vals[a] - vals[b], near(r, vals[a] - vals[b], 0, hi), o=o, d="H", fig=fig,
                    reason=f"{vals[a]} − {vals[b]} = {vals[a] - vals[b]}.")
    return t


# ============================================================== STAGE 1
def stage1():
    U = []
    # ---------------------------------------------------------- 1
    u = unit(1, "Numbers to 10", "Number", "Counting objects to 10, reading and writing numbers and number words, one more and one less, and comparing numbers.",
             "Count up to 10 objects and match numbers to number words.", "Compare and order numbers to 10, and find one more or one less.", 1)
    build_sec(u, "1.1", "Counting to 10", "O1", [
        ("idea", "Count each one once", ["When we **count**, we touch each object **once** and say one number for each: one, two, three… The **last number** we say tells us **how many**."], {"kind": "emojis", "groups": [["🍎", 5]]}),
        ("check", NUMS("How many apples are there?", 5, [4, 6], o="O1", fig={"kind": "emojis", "groups": [["🍎", 5]]})),
        ("idea", "The ten frame", ["A **ten frame** has two rows of 5. A full row is **5**. A full frame is **10**. We can see how many without counting every dot."], {"kind": "tenframe", "n": 7}),
        ("tip", "Line them up", ["If objects are muddled, move each one to a line as you count it so you do not count it twice."]),
        ("check", NUMS("How many dots are in the ten frame?", 7, [6, 8], o="O1", fig={"kind": "tenframe", "n": 7}))],
        [("count", "say one number for each thing", "🔢"), ("number", "tells us how many", "7️⃣"), ("ten", "the number after nine", "🔟"), ("zero", "none at all", "0️⃣")],
        T=[t_count("O1"), t_frame("O1"), t_word("O1"), t_count("O1", 3, 10, per=10)],
        deep=[t_missing("O1"), t_order("O1"),
              claim_n("O1", lambda r: (lambda n, off: (f"There are {n + off} stars.", off == 0, f"There are {n}. Touch each star once as you count." if off else f"Yes, there are {n}.", {"kind": "emojis", "groups": [["⭐", n]], "per": 5}))(r.randint(3, 9), r.choice([0, 1, -1])))],
        ex=EXQ(t_count("O1")))
    build_sec(u, "1.2", "More, less and order", "O2", [
        ("idea", "One more, one less", ["**One more** than a number is the next number when we count. **One less** is the number just before. One more than 6 is 7. One less than 6 is 5."], {"kind": "numline", "min": 0, "max": 10, "mark": 6}),
        ("check", NUMS("What is one more than 4?", 5, [3, 6], o="O2", fig={"kind": "numline", "min": 0, "max": 10, "mark": 4})),
        ("idea", "Comparing groups", ["Match objects one to one. The group with some left over has **more**. The other group has **fewer**."], {"kind": "emojis", "groups": [["🐶", 6], ["🦴", 4]], "per": 10}),
        ("mistake", "Big pictures are not more", ["Three elephants are not 'more' than five mice. Count the objects – do not look at how big they are."]),
        ("check", PIC("Which number is larger: 3 or 8?", "8", [("3", "3 comes before 8 when we count.")], o="O2"))],
        [("more", "a bigger number of things", "➕"), ("fewer", "a smaller number of things", "➖"), ("order", "put in the right place, one after another", "📶"), ("same", "equal, not more or fewer", "🟰")],
        T=[t_more_less("O2"), t_compare_groups("O2"), t_bigger("O2"), t_numline("O2")],
        deep=[t_order("O2", n=5), t_missing("O2"),
              claim_n("O2", lambda r: (lambda a, b: (f"{a} is more than {b}.", a > b, f"{max(a, b)} is more, because it comes after {min(a, b)} when we count.", None))(*r.sample(range(0, 11), 2)))],
        ex=EXQ(t_compare_groups("O2")))
    U.append(u)
    # ---------------------------------------------------------- 2
    u = unit(2, "Numbers to 20", "Number", "Counting, reading and ordering numbers to 20; teen numbers as ten and some more; first, second and third.",
             "Read, count and show numbers from 11 to 20 as ten and some more.", "Compare and order numbers to 20 and use first, second, third.", 1)
    build_sec(u, "2.1", "Teen numbers", "O1", [
        ("idea", "Ten and some more", ["**Teen numbers** are **ten** and some more. 13 is ten and three. 17 is ten and seven. A full ten frame shows the ten."], {"kind": "tenframe", "n": 13, "of": 20}),
        ("check", NUMS("How many dots? (One frame is full.)", 13, [12, 14, 3], o="O1", fig={"kind": "tenframe", "n": 13, "of": 20})),
        ("tip", "Read the teens", ["The 1 in 14 means one ten. The 4 means four ones. Fourteen = ten and four."]),
        ("check", NUMS("Ten and six more is…", 16, [15, 61, 17], o="O1"))],
        [("teen", "a number from 13 to 19", "🔢"), ("ten", "a full ten frame", "🔟"), ("twenty", "two full tens", "2️⃣"), ("ones", "the single things left over", "1️⃣")],
        T=[t_frame("O1", 11, 20), t_count("O1", 11, 20, per=10), t_word("O1", 10, 20),
           lambda r: (lambda n: NUMS(f"Ten and {n - 10} more is…", n, near(r, n, 10, 20) or [n + 1], o="O1", reason=f"10 + {n - 10} = {n}."))(r.randint(11, 19))],
        deep=[t_missing("O1", 8, 20), lambda r: (lambda n: PIC(f"Which number is ten and {n - 10}?", str(n), [(str(int(f'{n - 10}1')), "That has the digits the wrong way round."), (str(n + 1), "")], o="O1", d="H", reason=f"Ten and {n - 10} is {n}: a 1 for the ten, then {n - 10} ones."))(r.randint(12, 19)),
              claim_n("O1", lambda r: (lambda n: (f"{n} is ten and {n - 10}.", True, f"{n} = 10 + {n - 10}.", None) if r.random() < 0.5 else (f"{n} is ten and {n - 9}.", False, f"{n} = 10 + {n - 10}.", None))(r.randint(11, 19)))],
        ex=EXQ(t_frame("O1", 11, 20)))
    POS = ["first", "second", "third", "fourth", "fifth"]
    RACERS = [("dog", "🐶"), ("cat", "🐱"), ("rabbit", "🐰"), ("frog", "🐸"), ("monkey", "🐵"), ("pig", "🐷")]
    build_sec(u, "2.2", "Order to 20 and positions", "O2", [
        ("idea", "Ordering to 20", ["On a number line the numbers get **bigger** as we go **right**. 18 is bigger than 12 because it is further along."], {"kind": "numline", "min": 0, "max": 20, "mark": 18}),
        ("check", PIC("Which is larger: 12 or 18?", "18", [("12", "12 comes before 18.")], o="O2")),
        ("idea", "First, second, third", ["In a race the winner is **first**. Next is **second**, then **third**, **fourth** and **fifth**."], EM(("🥇", 1), ("🥈", 1), ("🥉", 1))),
        ("check", PIC("🐶 🐱 🐰 🐸 are in a line, the dog first. Which animal is third?", "rabbit", [("cat", "The cat is second."), ("frog", "The frog is fourth.")], pics={"rabbit": "🐰", "cat": "🐱", "frog": "🐸"}, o="O2"))],
        [("first", "number one in a line", "🥇"), ("second", "next after first", "🥈"), ("third", "next after second", "🥉"), ("last", "at the end", "🔚")],
        T=[t_bigger("O2", 0, 20), t_order("O2", 0, 20), t_numline("O2", 0, 20), t_more_less("O2", 0, 20),
           lambda r: (lambda line, i: PIC(f"{' '.join(e for _, e in line)} are in a line, starting from the left. Which animal is {POS[i]}?", line[i][0], [(x[0], "") for x in line if x is not line[i]][:2], pics={x[0]: x[1] for x in line}, o="O2",
                                          reason=f"Count from the left: the {POS[i]} is the {line[i][0]}."))(r.sample(RACERS, 5), r.randint(0, 4))],
        deep=[t_order("O2", 0, 20, n=5), t_missing("O2", 0, 20, step=2),
              claim_n("O2", lambda r: (lambda a, b: (f"{a} is less than {b}.", a < b, f"{min(a, b)} is less: it comes first on the number line.", None))(*r.sample(range(0, 21), 2)))],
        ex=EXQ(t_bigger("O2", 0, 20)))
    U.append(u)
    # ---------------------------------------------------------- 3
    u = unit(3, "Addition", "Number", "Adding by combining groups and counting on, number bonds to 10, and doubles.",
             "Add two groups of objects by counting all or counting on.", "Know number bonds to 10 and doubles, and use them to add.", 1)
    build_sec(u, "3.1", "Adding groups", "O1", [
        ("idea", "Putting groups together", ["**Adding** puts groups together to find **how many altogether**. 3 apples and 2 apples make 5 apples. We write **3 + 2 = 5**."], {"kind": "emojis", "groups": [["🍎", 3], ["🍎", 2]], "plus": True}),
        ("check", NUMS("4 + 2 = ?", 6, [5, 7], o="O1", fig={"kind": "emojis", "groups": [["⭐", 4], ["⭐", 2]], "plus": True})),
        ("idea", "Count on", ["Start at the **bigger** number and count on. For 6 + 3: say 6, then count 7, 8, 9. So 6 + 3 = 9."], {"kind": "numline", "min": 0, "max": 10, "mark": 6}),
        ("check", NUMS("Start at 7 and count on 2. Where do you land?", 9, [8, 10], o="O1"))],
        [("add", "put together", "➕"), ("altogether", "all of them counted together", "🧺"), ("plus", "the + sign", "➕"), ("equals", "the = sign: is the same as", "🟰")],
        T=[t_add_pics("O1"), t_add("O1"), t_add_pics("O1", 8), t_add("O1", 10, 5)],
        deep=[t_missing_add("O1"), t_fact_claim("O1"),
              lambda r: (lambda a, b: NUMS(f"{pick(r, NAMES)} has {a} stickers and gets {b} more. How many stickers now?", a + b, near(r, a + b, 0, 12), o="O1", d="H", reason=f"{a} + {b} = {a + b}."))(r.randint(2, 6), r.randint(1, 4))],
        ex=EXQ(t_add_pics("O1")))
    build_sec(u, "3.2", "Number bonds and doubles", "O2", [
        ("idea", "Number bonds to 10", ["Pairs that make 10 are **number bonds to 10**: 1 + 9, 2 + 8, 3 + 7, 4 + 6, 5 + 5. On a ten frame, the empty boxes show the other part."], {"kind": "tenframe", "n": 6}),
        ("check", NUMS("6 + ? = 10", 4, [3, 5], o="O2", fig={"kind": "tenframe", "n": 6})),
        ("idea", "Doubles", ["A **double** adds a number to itself. Double 3 is 3 + 3 = 6. Doubles are easy to remember."], {"kind": "emojis", "groups": [["🐞", 3], ["🐞", 3]], "plus": True}),
        ("check", NUMS("Double 4 is…", 8, [6, 9], o="O2"))],
        [("number bond", "two numbers that make a total", "🔗"), ("double", "add a number to itself", "👯"), ("total", "the answer when you add", "🧮")],
        T=[t_bond("O2"), t_double("O2", 5), t_bond("O2", pick(random.Random(3), [6, 7, 8])),
           lambda r: (lambda a: MT("Match the pairs that make 10.", [(str(x), str(10 - x)) for x in r.sample(range(1, 10), 3)], o="O2", reason="Each pair adds to 10."))(0)],
        deep=[claim_n("O2", lambda r: (lambda a, ok: (f"{a} and {10 - a if ok else 10 - a + 1} make 10.", ok, f"{a} + {10 - a} = 10.", {"kind": "tenframe", "n": a}))(r.randint(1, 9), r.random() < 0.5)),
              lambda r: MS("Tap ALL the pairs that make 10.", [f"{a} + {10 - a}" for a in r.sample(range(1, 6), 2)], [f"{a} + {9 - a}" for a in r.sample(range(1, 5), 2)], o="O2", d="H", reason="Check each pair: only those adding to 10 are right."),
              t_missing_add("O2")],
        ex=EXQ(t_bond("O2")))
    U.append(u)
    # ---------------------------------------------------------- 4
    u = unit(4, "Subtraction", "Number", "Taking away and counting back, finding how many more, and seeing that subtraction undoes addition.",
             "Subtract by taking away and counting back.", "Find the difference between two numbers and link subtraction with addition.", 1)
    build_sec(u, "4.1", "Taking away", "O1", [
        ("idea", "Take away", ["**Subtraction** takes some away. 5 birds sit on a wall and 2 fly away. 3 are **left**. We write **5 − 2 = 3**."], {"kind": "emojis", "groups": [["🐦", 5]]}),
        ("check", NUMS("There are 6 balloons. 2 pop. How many are left?", 4, [3, 8], o="O1", fig={"kind": "emojis", "groups": [["🎈", 6]]})),
        ("idea", "Count back", ["To work out 8 − 3, start at 8 and count **back** 3: 7, 6, 5. So 8 − 3 = 5."], {"kind": "numline", "min": 0, "max": 10, "mark": 8}),
        ("mistake", "Do not count the start", ["When counting back 3 from 8, the first number you say is 7, not 8."]),
        ("check", NUMS("9 − 3 = ?", 6, [5, 7], o="O1"))],
        [("subtract", "take some away", "➖"), ("left", "what stays after taking away", "👈"), ("minus", "the − sign", "➖"), ("count back", "say numbers going down", "🔙")],
        T=[t_sub_pics("O1"), t_sub("O1"), t_sub_pics("O1", 8), t_sub("O1", 10)],
        deep=[t_fact_claim("O1"), lambda r: (lambda a, b: NUMS(f"{pick(r, NAMES)} had {a} sweets and ate {b}. How many are left?", a - b, near(r, a - b, 0, 10), o="O1", d="H", reason=f"{a} − {b} = {a - b}."))(r.randint(5, 10), r.randint(1, 4)),
              lambda r: (lambda a, b: NUMS(f"{a} − ? = {a - b}", b, near(r, b, 0, 10), o="O1", d="H", reason=f"{a} − {b} = {a - b}."))(r.randint(4, 10), r.randint(1, 3))],
        ex=EXQ(t_sub_pics("O1")))
    build_sec(u, "4.2", "How many more?", "O2", [
        ("idea", "Finding the difference", ["To find **how many more**, line up the two groups. Count the ones with no partner. That is the **difference**."], {"kind": "emojis", "groups": [["🐟", 3], ["🐟", 7]], "per": 10}),
        ("check", NUMS("3 fish and 7 fish. How many more in the second group?", 4, [3, 10], o="O2", fig={"kind": "emojis", "groups": [["🐟", 3], ["🐟", 7]], "per": 10})),
        ("idea", "Add and subtract are partners", ["If 4 + 3 = 7, then 7 − 3 = 4 and 7 − 4 = 3. Knowing one fact helps you find the others."], EM(("➕", 1), ("➖", 1))),
        ("check", PIC("4 + 3 = 7. Which subtraction is also true?", "7 − 3 = 4", [("7 − 4 = 2", "7 − 4 = 3."), ("3 − 7 = 4", "Start with the biggest number.")], o="O2"))],
        [("difference", "how many more one has than another", "↔️"), ("fewer", "a smaller number", "➖"), ("check", "make sure it is right", "✅")],
        T=[t_difference("O2"), t_difference("O2", 8), t_compare_groups("O2"),
           lambda r: (lambda a, b: PIC(f"{a} + {b} = {a + b}. Which subtraction is also true?", f"{a + b} − {b} = {a}", [(f"{a + b} − {b} = {a + 1}", ""), (f"{b} − {a + b} = {a}", "Start with the biggest number.")], o="O2"))(r.randint(1, 6), r.randint(1, 4))],
        deep=[t_missing_add("O2"), t_fact_claim("O2"),
              lambda r: (lambda a, b: MS(f"Tap ALL the facts that are true.", [f"{a} + {b} = {a + b}", f"{a + b} − {a} = {b}"], [f"{a + b} − {a} = {b + 1}", f"{a} + {b} = {a + b + 1}"], o="O2", d="H", reason=f"{a} + {b} = {a + b} and {a + b} − {a} = {b}."))(r.randint(2, 5), r.randint(2, 4))],
        ex=EXQ(t_difference("O2")))
    U.append(u)
    # ---------------------------------------------------------- 5
    u = unit(5, "Shapes", "Geometry", "Naming and describing 2D shapes by their sides and corners, and 3D shapes by how they roll and stack.",
             "Name and describe 2D shapes: circle, triangle, square and rectangle.", "Name 3D shapes: cube, cuboid, sphere, cylinder and cone.", 1)
    N1 = ["triangle", "square", "rectangle"]
    S2E = [("ball", "⚽", "Curved"), ("coin", "🪙", "Curved"), ("clock", "🕐", "Curved"), ("pizza", "🍕", "Straight sides"), ("window", "🪟", "Straight sides"), ("book", "📕", "Straight sides"), ("orange slice", "🍊", "Curved"), ("door", "🚪", "Straight sides")]
    build_sec(u, "5.1", "2D shapes", "O1", [
        ("idea", "Flat shapes", ["A **circle** is round. A **triangle** has 3 straight sides. A **square** has 4 sides all the same length. A **rectangle** has 4 sides: two long and two short."], shp("triangle")),
        ("check", PIC("What is this shape?", "triangle", [("square", "A square has 4 sides."), ("circle", "A circle is round.")], o="O1", fig=shp("triangle"))),
        ("tip", "Turned shapes keep their name", ["A triangle is still a triangle when you turn it upside down."]),
        ("check", NUMS("How many sides does a square have?", 4, [3, 5], o="O1", fig=shp("square")))],
        [("circle", "a round flat shape", "⚪"), ("triangle", "3 straight sides", "🔺"), ("square", "4 equal sides", "🟥"), ("rectangle", "4 sides, 2 long and 2 short", "▭"), ("side", "a straight edge of a shape", "📏")],
        T=[t_shape_name("O1", N1), t_sides("O1", N1), t_sides("O1", N1, "corners"), k_sort(S2E, ["Curved", "Straight sides"], "O1", "Is each one curved or does it have straight sides?")],
        deep=[k_odd([("triangle", "🔺", "3 sides"), ("slice of cake", "🍰", "3 sides"), ("warning sign", "⚠️", "3 sides"), ("ball", "⚽", "Round"), ("square tile", "🟦", "4 sides")], "O1"),
              claim_n("O1", lambda r: pick(r, [("A square is a kind of rectangle.", True, "It has 4 sides and 4 square corners, like a rectangle; its sides are all equal.", None), ("A circle has 1 corner.", False, "A circle has no corners.", None), ("An upside-down triangle is still a triangle.", True, "Turning a shape does not change its name.", None), ("A rectangle has 3 sides.", False, "A rectangle has 4 sides.", None)])),
              t_shape_name("O1", N1 + ["hexagon"])],
        ex=EXQ(t_shape_name("O1", N1)))
    build_sec(u, "5.2", "3D shapes", "O2", [
        ("idea", "Solid shapes", ["A ball is a **sphere**. A dice is a **cube**. A tin is a **cylinder**. An ice-cream cone is a **cone**. A cereal box is a **cuboid**."], EM(("⚽", 1), ("🎲", 1), ("🥫", 1), ("🍦", 1), ("📦", 1))),
        ("check", PIC("What shape is a dice?", "cube", [("sphere", "A sphere is round like a ball."), ("cone", "A cone has a point.")], o="O2", pic="🎲")),
        ("idea", "Roll or stack?", ["Shapes with **curved** surfaces can **roll** (sphere, cylinder). Shapes with **flat** faces can **stack** (cube, cuboid). A cylinder can do both."], EM(("⚽", 1), ("📦", 2))),
        ("check", PIC("Which shape rolls in every direction?", "sphere", [("cube", "A cube has flat faces."), ("cuboid", "A cuboid has flat faces.")], pics={"sphere": "⚽", "cube": "🎲", "cuboid": "📦"}, o="O2"))],
        [("sphere", "round like a ball", "⚽"), ("cube", "6 square faces, like a dice", "🎲"), ("cylinder", "like a tin", "🥫"), ("cone", "round base and a point", "🍦"), ("cuboid", "like a box", "📦")],
        T=[k_pick(S3, "Sphere", "O2", "Which one is a SPHERE?"), k_pick(S3, "Cube", "O2", "Which one is a CUBE?"), k_pick(S3, "Cylinder", "O2", "Which one is a CYLINDER?"), k_sort(S3, ["Sphere", "Cube", "Cylinder", "Cone", "Cuboid"], "O2", "What shape is each one?")],
        deep=[k_odd(S3, "O2"), k_all(S3, "Cone", "O2", "Tap ALL the cones."),
              k_claim([("A ball can be stacked in a tall tower.", False, "A sphere rolls off; it has no flat face."), ("A tin can roll and stack.", True, "A cylinder has a curved surface and two flat faces."), ("A cereal box is a cuboid.", True, "It has 6 rectangle faces.")], "O2")],
        ex=EXQ(k_pick(S3, "Cone", "O2", "Which one is a CONE?")))
    U.append(u)
    # ---------------------------------------------------------- 6
    u = unit(6, "Measures", "Geometry", "Comparing length, height, mass and capacity using words like longer, taller, heavier and full; measuring with cubes.",
             "Compare and measure lengths and heights.", "Compare mass and capacity.", 1)
    build_sec(u, "6.1", "Long, tall and short", "O1", [
        ("idea", "Comparing lengths", ["We compare things with words like **longer**, **shorter**, **taller**. Line them up at one end to compare fairly."], {"kind": "emojis", "groups": [["🟦", 7], ["🟥", 4]], "per": 10, "size": 30}),
        ("check", PIC("The blue line is 7 cubes. The red line is 4 cubes. Which is longer?", "blue", [("red", "4 cubes is shorter than 7.")], pics={"blue": "🟦", "red": "🟥"}, o="O1", fig={"kind": "emojis", "groups": [["🟦", 7], ["🟥", 4]], "per": 10, "size": 30})),
        ("idea", "Measuring with cubes", ["We can measure how long something is by counting how many **cubes** fit along it."], {"kind": "emojis", "groups": [["🟦", 6]], "per": 10, "size": 30}),
        ("check", NUMS("How many cubes long is the line?", 6, [5, 7], o="O1", fig={"kind": "emojis", "groups": [["🟦", 6]], "per": 10, "size": 30}))],
        [("long", "a big length", "📏"), ("short", "a small length", "🤏"), ("tall", "a big height", "🦒"), ("measure", "find out how long or heavy", "📐")],
        T=[t_compare_size("O1", TALL, "tallest", "shortest"), t_cubes("O1"), t_cubes("O1", 12),
           lambda r: (lambda a, b: PIC(f"A red ribbon is {a} cubes long. A green ribbon is {b} cubes long. Which is longer?", "red" if a > b else "green", [("green" if a > b else "red", "")], pics={"red": "🟥", "green": "🟩"}, o="O1",
                                       fig={"kind": "emojis", "groups": [["🟥", a], ["🟩", b]], "per": 12, "size": 28}, reason=f"{max(a, b)} cubes is longer than {min(a, b)} cubes."))(*r.sample(range(2, 12), 2))],
        deep=[lambda r: (lambda ch: OD("Put them in order, shortest first.", [x[0] for x in sorted(ch, key=lambda x: x[2])], o="O1", d="H", reason="From shortest to tallest."))(r.sample(TALL, 3)),
              claim_n("O1", lambda r: (lambda a, b: (f"The pencil is {a} cubes long and the crayon is {b}. The pencil is longer.", a > b, f"{max(a, b)} cubes is longer than {min(a, b)}.", None))(*r.sample(range(2, 11), 2))),
              k_claim([("To compare two ribbons, line them up at one end.", True, "Lining up one end makes the comparison fair."), ("A giraffe is shorter than a cat.", False, "A giraffe is much taller.")], "O1")],
        ex=EXQ(t_compare_size("O1", TALL, "tallest", "shortest")))
    CAP = [("full", "🥛", "Full"), ("empty glass", "🫙", "Empty"), ("half full", "🧃", "Half full")]
    build_sec(u, "6.2", "Heavy, light, full and empty", "O2", [
        ("idea", "Heavier and lighter", ["An object that is harder to lift is **heavier**. On a **balance**, the heavier side goes **down**."], EM(("🐘", 1), ("🪶", 1))),
        ("check", PIC("Which is heavier?", "elephant", [("feather", "A feather is very light.")], pics={"elephant": "🐘", "feather": "🪶"}, o="O2")),
        ("idea", "Full and empty", ["A cup is **full** when no more will fit. It is **empty** when there is nothing in it. **Half full** is in between."], EM(("🥛", 1), ("🫙", 1))),
        ("check", PIC("A jug has nothing in it. It is…", "empty", [("full", "Full means no more fits in."), ("half full", "Half full has some in it.")], o="O2"))],
        [("heavy", "hard to lift", "🏋️"), ("light", "easy to lift", "🪶"), ("full", "no more will fit", "🥛"), ("empty", "nothing inside", "🫙")],
        T=[t_compare_size("O2", HEAVY, "heaviest", "lightest"), t_compare_size("O2", HEAVY, "heaviest", "lightest"),
           lambda r: (lambda a, b: PIC(f"A balance has a {a[0]} on one side and a {b[0]} on the other. Which side goes down?", f"the {max(a, b, key=lambda x: x[2])[0]} side", [(f"the {min(a, b, key=lambda x: x[2])[0]} side", "The lighter side goes up.")], o="O2", pic="⚖️",
                                       reason="The heavier side of a balance goes down."))(*r.sample(HEAVY, 2)),
           k_word([("heavy", "hard to lift", "🏋️"), ("light", "easy to lift", "🪶"), ("full", "no more will fit", "🥛"), ("empty", "nothing inside", "🫙")], "O2")],
        deep=[lambda r: (lambda ch: OD("Put them in order, lightest first.", [x[0] for x in sorted(ch, key=lambda x: x[2])], o="O2", d="H", reason="Lightest to heaviest."))(r.sample(HEAVY, 3)),
              k_claim([("Big things are always heavier.", False, "A big balloon is lighter than a small stone."), ("On a balance the heavier side goes down.", True, "That is how a balance works."), ("A full cup holds more than an empty cup.", True, "An empty cup has nothing in it.")], "O2"),
              lambda r: PIC("Which is heavier: a big balloon or a small stone?", "small stone", [("big balloon", "Balloons are full of air and very light.")], pics={"small stone": "🪨", "big balloon": "🎈"}, o="O2", d="VH", reason="Size does not tell you mass: the stone is heavier.")],
        ex=EXQ(t_compare_size("O2", HEAVY, "heaviest", "lightest")))
    U.append(u)
    # ---------------------------------------------------------- 7
    u = unit(7, "Time", "Geometry", "Days of the week, ordering events, and telling the time to the hour and half hour.",
             "Know the days of the week and put events in order.", "Read o'clock and half past times on a clock.", 1)
    build_sec(u, "7.1", "Days and order", "O1", [
        ("idea", "Seven days", ["There are **7 days** in a week: **Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday**. Then Monday comes again."], EM(("📅", 1))),
        ("check", PIC("Which day comes after Tuesday?", "Wednesday", [("Monday", "Monday is before Tuesday."), ("Friday", "Friday is later.")], o="O1")),
        ("idea", "Before and after", ["We do things in order: **first** we wake up, **next** we eat breakfast, **then** we go to school, and **last** we go to bed."], EM(("⏰", 1), ("🥣", 1), ("🏫", 1), ("🛏️", 1))),
        ("check", PIC("What do you usually do first in the day?", "wake up", [("go to bed", "That is at night."), ("eat dinner", "That is in the evening.")], pics={"wake up": "⏰", "go to bed": "🛏️", "eat dinner": "🍝"}, o="O1"))],
        [("day", "Monday, Tuesday… there are 7", "📅"), ("week", "seven days", "🗓️"), ("before", "earlier", "⏮️"), ("after", "later", "⏭️"), ("morning", "the start of the day", "🌅")],
        T=[t_day_after("O1"), t_days_order("O1"), k_order([(["wake up", "eat breakfast", "go to school", "go to bed"], "This is the usual order of a day."), (["plant a seed", "water it", "it grows", "pick the flower"], "A plant has to grow before you pick it."), (["get dressed", "put on shoes", "walk outside"], "Shoes go on after clothes.")], "O1", "Put the pictures in order."),
           k_sort([("breakfast", "🥣", "Morning"), ("sunrise", "🌅", "Morning"), ("bedtime", "🛏️", "Night"), ("stars", "🌙", "Night"), ("school starts", "🏫", "Morning"), ("owl hooting", "🦉", "Night")], ["Morning", "Night"], "O1", "Morning or night?")],
        deep=[k_claim([("There are 5 days in a week.", False, "There are 7 days in a week."), ("Sunday comes before Monday.", True, "The week goes … Saturday, Sunday, Monday …"), ("Saturday and Sunday are the weekend.", True, "They are the two weekend days.")], "O1"),
              lambda r: (lambda i: PIC(f"Today is {DAYS[i]}. What day will it be in 2 days?", DAYS[(i + 2) % 7], [(DAYS[(i + 1) % 7], "That is only 1 day."), (DAYS[(i + 3) % 7], "That is 3 days.")], o="O1", d="H", reason=f"{DAYS[i]} → {DAYS[(i + 1) % 7]} → {DAYS[(i + 2) % 7]}."))(r.randint(0, 6)),
              t_days_order("O1", k=5)],
        ex=EXQ(t_day_after("O1")))
    build_sec(u, "7.2", "O'clock and half past", "O2", [
        ("idea", "The clock", ["A clock has a **short hand** for the hour and a **long hand** for the minutes. When the long hand points to **12**, it is **o'clock**."], {"kind": "clock", "h": 3, "m": 0}),
        ("check", PIC("What time is it?", "3 o'clock", [("12 o'clock", "The short hand shows the hour: 3."), ("4 o'clock", "Look at the short hand again.")], o="O2", fig={"kind": "clock", "h": 3, "m": 0})),
        ("idea", "Half past", ["When the long hand points to **6**, it has gone half way round: it is **half past**. The short hand is half way between two numbers."], {"kind": "clock", "h": 7, "m": 30}),
        ("mistake", "Which hand is which?", ["The short hand tells the hour. The long hand tells the minutes. Do not mix them up."]),
        ("check", PIC("What time is it?", "half past 7", [("7 o'clock", "The long hand points to 6, not 12."), ("half past 6", "The short hand is past 7.")], o="O2", fig={"kind": "clock", "h": 7, "m": 30}))],
        [("clock", "shows the time", "🕐"), ("hour", "the short hand shows it", "⏰"), ("o'clock", "the long hand points to 12", "🕛"), ("half past", "the long hand points to 6", "🕧")],
        T=[t_clock("O2", (0,)), t_clock("O2", (30,)), t_clock("O2", (0, 30)),
           lambda r: (lambda h: PIC(f"Where does the long hand point at {h} o'clock?", "12", [("6", "6 is for half past."), (str(h if h != 12 else 3), "That is where the short hand points.")], o="O2", reason="At o'clock the long hand points straight up to 12."))(r.randint(1, 11))],
        deep=[claim_n("O2", lambda r: (lambda h, m: (f"The clock shows {oclock(h, m)}.", True, f"It shows {oclock(h, m)}.", {"kind": "clock", "h": h, "m": m}) if r.random() < 0.5 else (f"The clock shows {oclock(h % 12 + 1, m)}.", False, f"The short hand shows {h}: it is {oclock(h, m)}.", {"kind": "clock", "h": h, "m": m}))(r.randint(1, 11), r.choice([0, 30]))),
              lambda r: (lambda h: PIC(f"It is {h} o'clock. What time will it be in one hour?", f"{h + 1} o'clock", [(f"{h - 1 if h > 1 else 12} o'clock", "That is one hour earlier."), (f"half past {h}", "That is only half an hour.")], o="O2", d="H", reason=f"One hour after {h} o'clock is {h + 1} o'clock.", fig={"kind": "clock", "h": h, "m": 0}))(r.randint(1, 10)),
              lambda r: (lambda h: PIC(f"It is {h} o'clock. What time will it be in half an hour?", f"half past {h}", [(f"{h + 1} o'clock", "That is one hour."), (f"half past {h + 1}", "That is an hour and a half.")], o="O2", d="H", reason=f"Half an hour after {h} o'clock is half past {h}."))(r.randint(1, 10))],
        ex=EXQ(t_clock("O2", (0,))))
    U.append(u)
    # ---------------------------------------------------------- 8
    u = unit(8, "Halves, Patterns and Data", "Statistics", "Finding halves of shapes and amounts, continuing repeating patterns, and reading simple pictograms.",
             "Find half of a shape or a small amount, and continue repeating patterns.", "Sort objects and read simple pictograms and block graphs.", 1)
    build_sec(u, "8.1", "Halves and patterns", "O1", [
        ("idea", "A half", ["A **half** is one of **two equal parts**. Cut a pizza into two parts the same size: each part is a half. Half of 6 apples is 3 apples."], {"kind": "pie", "values": [1, 1], "shade": [0], "labels": ["", ""]}),
        ("check", PIC("Does the shaded part show a half?", "Yes", [("No", "There are two equal parts and one is shaded.")], pics=YN, o="O1", fig={"kind": "pie", "values": [1, 1], "shade": [0], "labels": ["", ""]})),
        ("mistake", "Halves must be equal", ["If you cut a cake into a big piece and a small piece, they are not halves."]),
        ("idea", "Repeating patterns", ["A **pattern** repeats. 🔴🔵🔴🔵🔴… Find the part that repeats, then say what comes next."], EM(("🔴", 1), ("🔵", 1), ("🔴", 1), ("🔵", 1))),
        ("check", PIC("What comes next?  🔴 🔵 🔴 🔵 🔴  ?", "🔵", [("🔴", "The pattern goes red, blue, red, blue.")], pics={"🔵": "🔵", "🔴": "🔴"}, o="O1"))],
        [("half", "one of two equal parts", "🌗"), ("equal", "the same size", "🟰"), ("pattern", "something that repeats", "🔁"), ("next", "what comes after", "⏭️")],
        T=[t_half_shape("O1"), t_frac_amount("O1", hi=12), t_pattern("O1"), t_double("O1", 5)],
        deep=[t_pattern("O1", hard=True), claim_n("O1", lambda r: (lambda n, ok: (f"Half of {2 * n} is {n if ok else n + 1}.", ok, f"{n} + {n} = {2 * n}, so half of {2 * n} is {n}.", {"kind": "emojis", "groups": [["🍪", 2 * n]], "per": n}))(r.randint(1, 6), r.random() < 0.5)),
              t_half_shape("O1")],
        ex=EXQ(t_half_shape("O1")))
    build_sec(u, "8.2", "Sorting and pictograms", "O2", [
        ("idea", "Sorting", ["We can **sort** objects into groups that are the same in some way – by colour, shape or size."], EM(("🔴", 3), ("🔵", 2))),
        ("check", PIC("Which one does NOT belong with 🍎 🍓 🍒?", "🍌", [("🍅", "It is red like the others.")], pics={"🍌": "🍌", "🍅": "🍅"}, o="O2", reason="The others are all red; the banana is yellow.")),
        ("idea", "Pictograms", ["A **pictogram** uses pictures to show how many. Each picture is one thing. The longest row has the **most**."], {"kind": "emojis", "groups": [["🍎", 5], ["🍌", 3], ["🍇", 6]], "per": 10, "size": 32}),
        ("check", NUMS("🍎 = apples. How many children chose apples?", 5, [4, 6], o="O2", fig={"kind": "emojis", "groups": [["🍎", 5], ["🍌", 3], ["🍇", 6]], "per": 10, "size": 32}))],
        [("sort", "put into groups", "🗂️"), ("group", "things that go together", "🧺"), ("pictogram", "a chart made of pictures", "📊"), ("most", "the biggest number", "🏆")],
        T=[t_pictogram("O2", 8, 3), t_pictogram("O2", 6, 3), k_sort([("red ball", "🔴", "Red"), ("strawberry", "🍓", "Red"), ("apple", "🍎", "Red"), ("blue whale", "🐋", "Blue"), ("blue heart", "💙", "Blue"), ("blue book", "📘", "Blue"), ("cherry", "🍒", "Red")], ["Red", "Blue"], "O2", "Sort by colour."),
           k_odd([("cat", "🐱", "Animal"), ("dog", "🐶", "Animal"), ("cow", "🐄", "Animal"), ("pig", "🐷", "Animal"), ("car", "🚗", "Vehicle"), ("bus", "🚌", "Vehicle"), ("bike", "🚲", "Vehicle"), ("plane", "✈️", "Vehicle")], "O2")],
        deep=[lambda r: (lambda cats, vals: NUMS("The pictogram shows fruit children chose. " + "  ".join(f"{e} = {c}" for c, e in cats) + f". How many more chose {cats[max(range(3), key=lambda i: vals[i])][0]} than {cats[min(range(3), key=lambda i: vals[i])][0]}?",
                                                     max(vals) - min(vals), near(r, max(vals) - min(vals), 0, 10), o="O2", d="H", fig={"kind": "emojis", "groups": [[e, v] for (_, e), v in zip(cats, vals)], "per": 10, "size": 32}, reason=f"{max(vals)} − {min(vals)} = {max(vals) - min(vals)}."))(*chart(r, 8, 3)),
              lambda r: (lambda cats, vals: NUMS("The pictogram shows fruit children chose. " + "  ".join(f"{e} = {c}" for c, e in cats) + ". How many children are there altogether?", sum(vals), near(r, sum(vals), 0, 30), o="O2", d="H",
                                                     fig={"kind": "emojis", "groups": [[e, v] for (_, e), v in zip(cats, vals)], "per": 10, "size": 32}, reason=" + ".join(map(str, vals)) + f" = {sum(vals)}."))(*chart(r, 5, 3)),
              k_claim([("In a pictogram, the longest row shows the most.", True, "More pictures means more."), ("Sorting means putting things in a random pile.", False, "Sorting means putting things into groups that are alike.")], "O2")],
        ex=EXQ(t_pictogram("O2", 8, 3)))
    U.append(u)
    return U


# ============================================================== STAGE 2
def t_tens_ones(o):
    def t(r):
        tn, on = r.randint(1, 9), r.randint(0, 9); n = 10 * tn + on
        fig = {"kind": "emojis", "groups": [["🔟", tn], ["🟡", on]] if on else [["🔟", tn]], "per": 10, "size": 30}
        return NUMS(f"Each 🔟 is ten and each 🟡 is one. What number is shown?", n, [x for x in [10 * on + tn, n + 10, n - 1, n + 1] if x != n and 0 <= x <= 100][:2], o=o, fig=fig,
                    reason=f"{tn} tens and {on} ones make {n}.", hint="Count the tens first: 10, 20, 30…")
    return t


def t_pv(o):
    def t(r):
        n = r.randint(11, 99); tn, on = divmod(n, 10); ask = r.choice(["tens", "ones"])
        a = tn if ask == "tens" else on
        return NUMS(f"How many {ask} are in {n}?", a, [x for x in {on if ask == 'tens' else tn, a + 1, n} if x != a][:2], o=o, reason=f"{n} = {tn} tens and {on} ones.",
                    fig={"kind": "emojis", "groups": [g for g in [["🔟", tn], ["🟡", on]] if g[1]], "per": 10, "size": 28})
    return t


def t_add10(o):
    def t(r):
        n = r.randint(5, 89); up = r.random() < 0.6; a = n + 10 if up else n - 10
        return NUMS(f"What is 10 {'more' if up else 'less'} than {n}?", a, [x for x in [n + 1 if up else n - 1, a + 10 if up else a - 10, n + 100 if up else n] if x != a and x >= 0][:2], o=o,
                    fig={"kind": "numline", "min": min(n, a) // 10 * 10, "max": min(n, a) // 10 * 10 + 20, "mark": n},
                    reason=f"Only the tens digit changes: {n} → {a}.")
    return t


def t_add2(o, carry=False):
    def t(r):
        while True:
            a, b = r.randint(10, 79), r.randint(2, 20 if not carry else 29)
            if (a % 10 + b % 10 >= 10) == carry and a + b <= 99: break
        fig = {"kind": "emojis", "groups": [g for g in [["🔟", a // 10], ["🟡", a % 10], ["🔟", b // 10], ["🟡", b % 10]] if g[1]], "per": 10, "size": 24}
        return NUMS(f"{a} + {b} = ?", a + b, near(r, a + b, 0, 100, far=True), o=o, fig=fig if r.random() < 0.6 else None, reason=f"Add the tens, then the ones: {a} + {b} = {a + b}.", hint="Add the tens first, then the ones.")
    return t


def t_sub2(o, carry=False):
    def t(r):
        while True:
            a, b = r.randint(20, 99), r.randint(2, 30)
            if (a % 10 < b % 10) == carry and a - b >= 0: break
        return NUMS(f"{a} − {b} = ?", a - b, near(r, a - b, 0, 100, far=True), o=o, fig={"kind": "numline", "min": (a - b) // 10 * 10, "max": (a // 10 + 1) * 10, "mark": a} if r.random() < 0.5 and a - b >= (a // 10 - 2) * 10 else None,
                    reason=f"{a} − {b} = {a - b}.", hint="Take away the tens, then the ones.")
    return t


def t_story2(o):
    def t(r):
        k = r.randint(0, 2); nm = pick(r, NAMES)
        if k == 0:
            a, b = r.randint(15, 60), r.randint(5, 30); return NUMS(f"{nm} has {a} marbles and wins {b} more. How many marbles now?", a + b, near(r, a + b, 0, 100, far=True), o=o, d="H", reason=f"{a} + {b} = {a + b}.")
        if k == 1:
            a, b = r.randint(30, 90), r.randint(5, 25); return NUMS(f"A bus has {a} people. {b} get off. How many are still on the bus?", a - b, near(r, a - b, 0, 100, far=True), o=o, d="H", reason=f"{a} − {b} = {a - b}.")
        a, b = r.randint(10, 40), r.randint(41, 90); return NUMS(f"{nm} read {a} pages. Her friend read {b} pages. How many more pages did her friend read?", b - a, near(r, b - a, 0, 100, far=True), o=o, d="H", reason=f"{b} − {a} = {b - a}.")
    return t


def t_groups(o, tables=(2, 5, 10)):
    def t(r):
        k = pick(r, list(tables)); n = r.randint(1, 10 if k != 10 else 6); nm, e = pick(r, [("pair of socks", "🧦"), ("hand", "🖐️"), ("bag", "👜")]) if False else thing(r)
        return NUMS(f"There are {n} groups of {k} {nm}s. How many {nm}s altogether?", n * k, near(r, n * k, 0, 100) + [n + k], o=o, fig={"kind": "emojis", "groups": [[e, k] for _ in range(min(n, 6))], "per": k, "size": 26} if n <= 6 else None,
                    reason=f"{n} × {k} = {n * k}. Count in {k}s: " + ", ".join(str(k * i) for i in range(1, n + 1)) + ".")
    return t


def t_times(o, tables=(2, 5, 10)):
    def t(r):
        k = pick(r, list(tables)); n = r.randint(0, 10)
        return NUMS(f"{n} × {k} = ?", n * k, [x for x in {n * k + k, max(0, n * k - k), n + k} if x != n * k][:2], o=o, reason=f"{n} lots of {k} is {n * k}.",
                    fig={"kind": "emojis", "groups": [["🟣", k] for _ in range(n)], "per": k, "size": 22} if 1 <= n <= 5 and k <= 5 else None)
    return t


def t_share(o, tables=(2, 5, 10)):
    def t(r):
        k = pick(r, list(tables)); n = r.randint(1, 10); tot = n * k; nm, e = thing(r)
        return NUMS(f"Share {tot} {nm}s equally between {k} children. How many does each child get?", n, near(r, n, 0, 20), o=o, d="M", fig={"kind": "emojis", "groups": [[e, tot]], "per": k, "size": 26} if tot <= 30 else None,
                    reason=f"{tot} ÷ {k} = {n}, because {n} × {k} = {tot}.", hint=f"Give one to each child at a time.")
    return t


def t_oddeven(o):
    def t(r):
        ns = r.sample(range(1, 51), 5)
        return GD("Is each number odd or even?", "Odd or even", [(str(n), "Even" if n % 2 == 0 else "Odd") for n in ns], o=o, extra=["Odd", "Even"], reason="Even numbers end in 0, 2, 4, 6 or 8.")
    return t


def stage2():
    U = []
    # ---------------------------------------------------------- 1
    u = unit(1, "Numbers to 100", "Number", "Tens and ones, reading and ordering numbers to 100, 10 more and 10 less, and counting in 2s, 5s and 10s.",
             "Understand tens and ones in numbers to 100.", "Compare and order numbers to 100 and count in steps of 2, 5 and 10.", 2)
    build_sec(u, "1.1", "Tens and ones", "O1", [
        ("idea", "Tens and ones", ["In **34** the 3 means **3 tens** (30) and the 4 means **4 ones**. 34 = 30 + 4."], {"kind": "emojis", "groups": [["🔟", 3], ["🟡", 4]], "per": 10, "size": 30}),
        ("check", NUMS("Each 🔟 is ten and each 🟡 is one. What number is shown?", 34, [43, 35], o="O1", fig={"kind": "emojis", "groups": [["🔟", 3], ["🟡", 4]], "per": 10, "size": 30})),
        ("mistake", "Order of digits", ["4 tens and 3 ones is 43, not 34. The tens digit comes first."]),
        ("idea", "10 more, 10 less", ["Adding 10 changes the **tens** digit only: 10 more than 46 is 56. 10 less than 46 is 36."], {"kind": "numline", "min": 30, "max": 60, "mark": 46}),
        ("check", NUMS("What is 10 more than 52?", 62, [53, 42], o="O1"))],
        [("tens", "groups of ten", "🔟"), ("ones", "single things", "🟡"), ("digit", "one of the signs 0 to 9", "🔢"), ("hundred", "ten tens", "💯")],
        T=[t_tens_ones("O1"), t_pv("O1"), t_add10("O1"), lambda r: (lambda n: NUMS(f"{n // 10} tens and {n % 10} ones is…", n, [10 * (n % 10) + n // 10 if n % 10 else n + 1, n + 10], o="O1", reason=f"{n // 10} tens = {10 * (n // 10)}, add {n % 10}: {n}."))(r.randint(21, 98))],
        deep=[claim_n("O1", lambda r: (lambda n: pick(r, [(f"{n} has {n % 10} tens.", n % 10 == n // 10, f"{n} has {n // 10} tens and {n % 10} ones.", None), (f"{n} = {10 * (n // 10)} + {n % 10}.", True, f"{n} is {n // 10} tens and {n % 10} ones.", None)]))(r.randint(21, 98))),
              lambda r: (lambda n: PIC(f"Which number has {n // 10} tens and {n % 10} ones?", str(n), [(str(10 * (n % 10) + n // 10), "The digits are the wrong way round."), (str(n // 10 + n % 10), "That adds the digits.")], o="O1", d="H", reason=f"{n // 10} tens and {n % 10} ones is {n}."))(r.choice([x for x in range(21, 99) if x % 10 and x % 10 != x // 10])),
              lambda r: (lambda n: MS(f"Tap ALL the ways to make {n}.", [f"{10 * (n // 10)} + {n % 10}", f"{n // 10} tens and {n % 10} ones"], [f"{10 * (n % 10)} + {n // 10}", f"{n // 10} + {n % 10}"], o="O1", d="H", reason=f"{n} = {10 * (n // 10)} + {n % 10}."))(r.choice([x for x in range(21, 99) if x % 10 and x % 10 != x // 10]))],
        ex=EXQ(t_tens_ones("O1")))
    build_sec(u, "1.2", "Order and count in steps", "O2", [
        ("idea", "Comparing two-digit numbers", ["Look at the **tens** first. 52 > 48 because 5 tens is more than 4 tens. If the tens are the same, look at the ones."], {"kind": "numline", "min": 40, "max": 60, "mark": 52}),
        ("check", PIC("Which is larger: 48 or 52?", "52", [("48", "4 tens is less than 5 tens.")], o="O2")),
        ("idea", "Counting in steps", ["Count in **2s**: 2, 4, 6, 8… Count in **5s**: 5, 10, 15, 20… Count in **10s**: 10, 20, 30…"], EM(("👟", 2), ("🖐️", 2))),
        ("check", NUMS("What comes next? 5, 10, 15, 20, ?", 25, [21, 30], o="O2"))],
        [("greater", "more than (>)", "➕"), ("less", "smaller than (<)", "➖"), ("step", "the jump each time", "👣"), ("sequence", "numbers in a pattern", "🔢")],
        T=[t_bigger("O2", 10, 99), t_order("O2", 10, 99), t_missing("O2", 0, 50, step=2), t_missing("O2", 0, 100, step=5), t_missing("O2", 0, 100, step=10)],
        deep=[claim_n("O2", lambda r: (lambda a, b: (f"{a} is greater than {b}.", a > b, f"Compare the tens first: {max(a, b)} is greater.", None))(*r.sample(range(10, 100), 2))),
              lambda r: (lambda n: PIC(f"Which is greater: {n} or {10 * (n % 10) + n // 10}?", str(max(n, 10 * (n % 10) + n // 10)), [(str(min(n, 10 * (n % 10) + n // 10)), "Look at the tens digit first.")], o="O2", d="H", reason="Compare the tens first."))(r.choice([x for x in range(12, 99) if x % 10 and x % 10 != x // 10])),
              t_order("O2", 10, 99, n=5)],
        ex=EXQ(t_bigger("O2", 10, 99)))
    U.append(u)
    # ---------------------------------------------------------- 2
    u = unit(2, "Addition and Subtraction", "Number", "Adding and subtracting two-digit numbers using tens and ones, number bonds to 20 and 100, and solving word problems.",
             "Add numbers to 100 using tens and ones.", "Subtract numbers to 100 and solve word problems.", 2)
    build_sec(u, "2.1", "Adding to 100", "O1", [
        ("idea", "Add the tens, then the ones", ["To add 34 + 25: tens 30 + 20 = 50, ones 4 + 5 = 9, so **34 + 25 = 59**."], {"kind": "emojis", "groups": [["🔟", 3], ["🟡", 4], ["🔟", 2], ["🟡", 5]], "per": 10, "size": 26}),
        ("check", NUMS("23 + 14 = ?", 37, [36, 47], o="O1")),
        ("idea", "Bonds to 20 and 100", ["If 7 + 3 = 10, then 17 + 3 = 20 and 70 + 30 = 100. Use what you know."], EM(("🔗", 1))),
        ("check", NUMS("60 + ? = 100", 40, [30, 50], o="O1"))],
        [("add", "put together", "➕"), ("sum", "the answer when you add", "🧮"), ("tens", "groups of ten", "🔟"), ("bond", "two numbers that make a total", "🔗")],
        T=[t_add2("O1"), t_add2("O1", True), t_bond("O1", 20), lambda r: (lambda a: NUMS(f"{a} + ? = 100", 100 - a, [x for x in [110 - a, 90 - a] if 0 <= x <= 100], o="O1", reason=f"{a} + {100 - a} = 100."))(10 * r.randint(1, 9))],
        deep=[t_story2("O1"), t_fact_claim("O1", 20),
              lambda r: (lambda a, b: PIC(f"Which is the best estimate for {a} + {b}?", str(round((a + b) / 10) * 10), [(str(round((a + b) / 10) * 10 + 20), ""), (str(max(10, round((a + b) / 10) * 10 - 20)), "")], o="O1", d="H", reason=f"{a} + {b} = {a + b}, which is about {round((a + b) / 10) * 10}."))(r.randint(21, 48), r.randint(21, 48))],
        ex=EXQ(t_add2("O1")))
    build_sec(u, "2.2", "Subtracting to 100", "O2", [
        ("idea", "Take the tens, then the ones", ["For 57 − 23: tens 50 − 20 = 30, ones 7 − 3 = 4, so **57 − 23 = 34**."], {"kind": "numline", "min": 30, "max": 60, "mark": 57}),
        ("check", NUMS("48 − 15 = ?", 33, [32, 63], o="O2")),
        ("tip", "Check with adding", ["57 − 23 = 34. Check: 34 + 23 = 57. ✓"]),
        ("check", PIC("Which addition checks 65 − 21 = 44?", "44 + 21 = 65", [("44 + 65 = 21", "The answer plus what you took away gives the start."), ("21 − 44 = 65", "Use addition to check.")], o="O2"))],
        [("subtract", "take away", "➖"), ("difference", "how much more one is than another", "↔️"), ("check", "make sure the answer is right", "✅")],
        T=[t_sub2("O2"), t_sub2("O2", True), t_difference("O2", 20), lambda r: (lambda a: NUMS(f"100 − {a} = ?", 100 - a, [x for x in [110 - a, 90 - a] if 0 <= x <= 100], o="O2", reason=f"{a} + {100 - a} = 100."))(10 * r.randint(1, 9))],
        deep=[t_story2("O2"), lambda r: (lambda a, b: PIC(f"{a} − {b} = {a - b}. Which addition checks it?", f"{a - b} + {b} = {a}", [(f"{a} + {b} = {a - b}", ""), (f"{a - b} + {a} = {b}", "")], o="O2", d="H", reason="Answer + amount taken away = the start number."))(r.randint(40, 99), r.randint(11, 30)),
              claim_n("O2", lambda r: (lambda a, b, ok: (f"{a} − {b} = {a - b if ok else a - b + 10}.", ok, f"{a} − {b} = {a - b}.", None))(r.randint(40, 99), r.randint(11, 30), r.random() < 0.5))],
        ex=EXQ(t_sub2("O2")))
    U.append(u)
    # ---------------------------------------------------------- 3
    u = unit(3, "Multiplication and Division", "Number", "Equal groups and arrays, the 2, 5 and 10 times tables, sharing and grouping, and odd and even numbers.",
             "Multiply using equal groups for the 2, 5 and 10 times tables.", "Divide by sharing and grouping, and recognise odd and even numbers.", 2)
    build_sec(u, "3.1", "Equal groups", "O1", [
        ("idea", "Groups of the same size", ["**3 groups of 5** is 5 + 5 + 5 = 15. We write **3 × 5 = 15**. The groups must be **equal**."], {"kind": "emojis", "groups": [["🍓", 5], ["🍓", 5], ["🍓", 5]], "per": 5, "size": 28}),
        ("check", NUMS("4 groups of 2 is…", 8, [6, 10], o="O1", fig={"kind": "emojis", "groups": [["🧦", 2]] * 4, "per": 2, "size": 28})),
        ("idea", "Count in steps", ["To find 6 × 5, count in 5s six times: 5, 10, 15, 20, 25, **30**."], EM(("🖐️", 6))),
        ("check", NUMS("7 × 10 = ?", 70, [17, 60], o="O1"))],
        [("groups", "sets of the same size", "🧺"), ("times", "the × sign: lots of", "✖️"), ("equal", "the same size", "🟰"), ("array", "rows and columns of things", "🔲")],
        T=[t_groups("O1"), t_times("O1"), t_times("O1", (2,)), t_times("O1", (5, 10))],
        deep=[claim_n("O1", lambda r: (lambda a, k: (f"{a} × {k} is the same as {k} × {a}.", True, "You can multiply in any order.", None) if r.random() < 0.5 else (f"{a} × {k} = {a + k}.", a * k == a + k, f"{a} × {k} = {a * k}: {a} lots of {k}.", None))(r.randint(2, 9), r.choice([2, 5, 10]))),
              lambda r: (lambda k, n: NUMS(f"Socks come in pairs. How many socks are in {n} pairs?" if k == 2 else f"Each hand has 5 fingers. How many fingers on {n} hands?", n * k, near(r, n * k, 0, 60) + [n + k], o="O1", d="H", reason=f"{n} × {k} = {n * k}."))(r.choice([2, 5]), r.randint(3, 9)),
              lambda r: (lambda k: MS(f"Tap ALL the numbers in the {k} times table.", [str(k * x) for x in r.sample(range(1, 11), 2)], [str(k * x + 1) for x in r.sample(range(1, 9), 2)], o="O1", d="H", reason=f"The {k} times table: " + ", ".join(str(k * i) for i in range(1, 11)) + "."))(r.choice([2, 5, 10]))],
        ex=EXQ(t_groups("O1")))
    build_sec(u, "3.2", "Sharing, grouping, odd and even", "O2", [
        ("idea", "Sharing equally", ["**Division** shares things equally. 12 sweets shared between 2 children: each gets 6. We write **12 ÷ 2 = 6**."], {"kind": "emojis", "groups": [["🍬", 12]], "per": 6, "size": 28}),
        ("check", NUMS("Share 10 cookies equally between 2 plates. How many on each plate?", 5, [4, 8], o="O2", fig={"kind": "emojis", "groups": [["🍪", 10]], "per": 5})),
        ("idea", "Odd and even", ["**Even** numbers can be shared into 2 equal groups: 2, 4, 6, 8, 10… They end in 0, 2, 4, 6 or 8. **Odd** numbers have one left over: 1, 3, 5, 7, 9…"], EM(("🧦", 2), ("🧦", 1))),
        ("check", PIC("Is 7 odd or even?", "odd", [("even", "7 cannot be split into 2 equal groups; one is left over.")], o="O2"))],
        [("share", "give out equally", "🤝"), ("divide", "split into equal groups", "➗"), ("odd", "one left over in pairs", "1️⃣"), ("even", "makes pairs with none left", "2️⃣")],
        T=[t_share("O2"), t_share("O2", (2,)), t_oddeven("O2"), lambda r: (lambda k, n: NUMS(f"{n * k} ÷ {k} = ?", n, near(r, n, 0, 20), o="O2", reason=f"{n} × {k} = {n * k}, so {n * k} ÷ {k} = {n}."))(r.choice([2, 5, 10]), r.randint(1, 10))],
        deep=[claim_n("O2", lambda r: (lambda n: (f"{n} is an even number.", n % 2 == 0, f"{n} ends in {n % 10}, so it is {'even' if n % 2 == 0 else 'odd'}.", None))(r.randint(11, 99))),
              lambda r: (lambda k, n: NUMS(f"{n * k} children get into teams of {k}. How many teams?", n, near(r, n, 0, 20), o="O2", d="H", reason=f"{n * k} ÷ {k} = {n}."))(r.choice([2, 5, 10]), r.randint(2, 10)),
              lambda r: MS("Tap ALL the even numbers.", [str(2 * x) for x in r.sample(range(6, 45), 2)], [str(2 * x + 1) for x in r.sample(range(6, 45), 2)], o="O2", d="H", reason="Even numbers end in 0, 2, 4, 6 or 8.")],
        ex=EXQ(t_share("O2")))
    U.append(u)
    # ---------------------------------------------------------- 4
    u = unit(4, "Fractions", "Number", "Halves, quarters and three quarters of shapes and amounts, and seeing that two quarters make a half.",
             "Recognise ½, ¼ and ¾ of a shape.", "Find ½, ¼ and ¾ of a small amount and know that 2/4 = ½.", 2)
    FR = (("a half", 2, 1), ("a quarter", 4, 1), ("three quarters", 4, 3))
    build_sec(u, "4.1", "Fractions of shapes", "O1", [
        ("idea", "Equal parts", ["A **half** (½) is 1 of 2 equal parts. A **quarter** (¼) is 1 of 4 equal parts. **Three quarters** (¾) is 3 of 4 equal parts."], {"kind": "pie", "values": [1, 1, 1, 1], "shade": [0, 1, 2], "labels": ["", "", "", ""]}),
        ("check", PIC("What fraction is shaded?", "three quarters", [("a quarter", "Three parts are shaded, not one."), ("a half", "Count the shaded parts: 3 of 4.")], o="O1", fig={"kind": "pie", "values": [1, 1, 1, 1], "shade": [0, 1, 2], "labels": ["", "", "", ""]})),
        ("mistake", "Parts must be equal", ["A shape cut into 4 parts of different sizes is not cut into quarters."]),
        ("check", PIC("Does the shaded part show a quarter?", "No", [("Yes", "The 4 parts are not equal.")], pics=YN, o="O1", fig={"kind": "pie", "values": [3, 1, 1, 1], "shade": [1], "labels": ["", "", "", ""]}))],
        [("half", "1 of 2 equal parts", "🌗"), ("quarter", "1 of 4 equal parts", "🕒"), ("three quarters", "3 of 4 equal parts", "🥧"), ("fraction", "a part of a whole", "🍕")],
        T=[t_half_shape("O1", FR), t_half_shape("O1", FR[1:]),
           lambda r: (lambda k: PIC("What fraction is shaded?", {1: "a quarter", 2: "a half", 3: "three quarters"}[k], [(x, "") for x in ["a quarter", "a half", "three quarters"] if x != {1: "a quarter", 2: "a half", 3: "three quarters"}[k]], o="O1",
                                    fig={"kind": "pie", "values": [1, 1, 1, 1], "shade": list(range(k)), "labels": [""] * 4}, reason=f"{k} of the 4 equal parts are shaded."))(r.randint(1, 3)),
           k_word([("half", "1 of 2 equal parts", "🌗"), ("quarter", "1 of 4 equal parts", "🕒"), ("three quarters", "3 of 4 equal parts", "🥧"), ("whole", "all of it", "⚪")], "O1")],
        deep=[k_claim([("Two quarters make a half.", True, "2 of 4 equal parts is the same as 1 of 2."), ("A quarter is bigger than a half.", False, "Cutting into 4 makes smaller parts than cutting into 2."), ("Four quarters make a whole.", True, "4 of 4 equal parts is all of it.")], "O1"),
              lambda r: PIC("Which is bigger: half a pizza or a quarter of the same pizza?", "half", [("a quarter", "A quarter is half of a half.")], o="O1", d="H", pic="🍕"),
              t_half_shape("O1", FR)],
        ex=EXQ(t_half_shape("O1", FR)))
    build_sec(u, "4.2", "Fractions of amounts", "O2", [
        ("idea", "Sharing to find a fraction", ["To find **¼ of 12**, share 12 into **4 equal groups**: 3 in each. So ¼ of 12 = 3. **¾ of 12** is 3 groups: 9."], {"kind": "emojis", "groups": [["🍓", 12]], "per": 3, "size": 28}),
        ("check", NUMS("What is half of 14?", 7, [6, 12], o="O2", fig={"kind": "emojis", "groups": [["🍓", 14]], "per": 7})),
        ("tip", "Half of a half", ["A quarter is half of a half. Half of 20 is 10, and half of 10 is 5, so ¼ of 20 is 5."]),
        ("check", NUMS("What is a quarter of 8?", 2, [4, 6], o="O2", fig={"kind": "emojis", "groups": [["🍓", 8]], "per": 2}))],
        [("share", "split equally", "🤝"), ("equal", "the same size", "🟰"), ("amount", "how many things", "🔢"), ("quarter", "1 of 4 equal parts", "🕒")],
        T=[t_frac_amount("O2", ((2, 1),), 20), t_frac_amount("O2", ((4, 1),), 20), t_frac_amount("O2", ((4, 3),), 20), t_frac_amount("O2", ((2, 1), (4, 1)), 20)],
        deep=[claim_n("O2", lambda r: (lambda n: (f"¼ of {4 * n} is {n}.", True, f"{4 * n} shared into 4 groups is {n} each.", None) if r.random() < 0.5 else (f"¼ of {4 * n} is {2 * n}.", False, f"{2 * n} is half. A quarter is {n}.", None))(r.randint(1, 5))),
              lambda r: (lambda n: PIC(f"Which is more: ½ of {4 * n} or ¼ of {4 * n}?", f"½ of {4 * n}", [(f"¼ of {4 * n}", "")], o="O2", d="H", reason=f"½ of {4 * n} is {2 * n}; ¼ of {4 * n} is {n}."))(r.randint(2, 6)),
              t_frac_amount("O2", ((4, 2),), 20)],
        ex=EXQ(t_frac_amount("O2", ((2, 1),), 20)))
    U.append(u)
    # ---------------------------------------------------------- 5
    u = unit(5, "Shapes and Symmetry", "Geometry", "Sides and vertices of 2D shapes, faces of 3D shapes, and lines of symmetry.",
             "Describe 2D shapes by their sides and vertices.", "Recognise 3D shapes and find lines of symmetry.", 2)
    N2 = ["triangle", "square", "rectangle", "pentagon", "hexagon", "octagon"]
    build_sec(u, "5.1", "2D shapes", "O1", [
        ("idea", "Sides and vertices", ["A **vertex** is a corner where two sides meet. A **pentagon** has 5 sides and 5 vertices. A **hexagon** has 6. An **octagon** has 8."], shp("hexagon")),
        ("check", NUMS("How many sides does this shape have?", 6, [5, 8], o="O1", fig=shp("hexagon"))),
        ("tip", "Mark where you start", ["Put your finger on one side and count round until you are back where you started."]),
        ("check", PIC("What is this shape?", "pentagon", [("hexagon", "A hexagon has 6 sides."), ("octagon", "An octagon has 8.")], o="O1", fig=shp("pentagon")))],
        [("vertex", "a corner of a shape", "📐"), ("side", "a straight edge", "📏"), ("pentagon", "5 sides", "⬟"), ("hexagon", "6 sides", "⬡"), ("octagon", "8 sides", "🛑")],
        T=[t_shape_name("O1", N2), t_sides("O1", N2), t_sides("O1", N2, "vertices"), k_word([("vertex", "a corner of a shape", "📐"), ("pentagon", "a shape with 5 sides", "⬟"), ("hexagon", "a shape with 6 sides", "⬡"), ("octagon", "a shape with 8 sides", "🛑")], "O1")],
        deep=[claim_n("O1", lambda r: (lambda n, ok: (f"A {n} has {SIDES[n] if ok else SIDES[n] + 1} vertices.", ok, f"A {n} has {SIDES[n]} sides and {SIDES[n]} vertices.", shp(n)))(pick(r, N2), r.random() < 0.5)),
              lambda r: (lambda n: MS(f"Tap ALL the shapes with {n} sides.", [x for x in N2 if SIDES[x] == n], [x for x in N2 if SIDES[x] != n][:2], o="O1", d="H", reason=f"Shapes with {n} sides."))(4),
              t_shape_name("O1", N2)],
        ex=EXQ(t_shape_name("O1", N2)))
    SYM = [("butterfly", "🦋", "Symmetrical"), ("heart", "❤️", "Symmetrical"), ("letter A", "🅰️", "Symmetrical"), ("star", "⭐", "Symmetrical"), ("snowman", "⛄", "Symmetrical"),
           ("letter F", "🔤", "Not symmetrical"), ("letter G", "🔠", "Not symmetrical"), ("shoe", "👟", "Not symmetrical"), ("hand pointing", "👉", "Not symmetrical"), ("letter R", "®️", "Not symmetrical")]
    build_sec(u, "5.2", "3D shapes and symmetry", "O2", [
        ("idea", "Faces of 3D shapes", ["A **face** is a flat surface. A **cube** has 6 square faces. A **cuboid** has 6 faces. A **cylinder** has 2 flat circle faces and a curved surface. A **sphere** has no flat faces."], EM(("🎲", 1), ("📦", 1), ("🥫", 1), ("⚽", 1))),
        ("check", NUMS("How many faces does a cube have?", 6, [4, 8], o="O2", pic="🎲")),
        ("idea", "Line of symmetry", ["A shape is **symmetrical** if a line splits it into two halves that match like a mirror. A butterfly is symmetrical."], EM(("🦋", 1))),
        ("check", PIC("Which picture is symmetrical?", "butterfly", [("shoe", "The two halves of a shoe do not match."), ("hand pointing", "It points one way.")], pics={"butterfly": "🦋", "shoe": "👟", "hand pointing": "👉"}, o="O2"))],
        [("face", "a flat surface of a solid", "🎲"), ("symmetry", "two halves that match", "🦋"), ("mirror", "shows a matching half", "🪞"), ("solid", "a 3D shape", "📦")],
        T=[k_sort(SYM, ["Symmetrical", "Not symmetrical"], "O2", "Is each one symmetrical?"), k_pick(SYM, "Symmetrical", "O2", "Which one is SYMMETRICAL?"), k_pick(S3, "Cylinder", "O2", "Which one is a CYLINDER?"),
           lambda r: (lambda s: NUMS(f"How many flat faces does a {s} have?", {"cube": 6, "cuboid": 6, "cylinder": 2, "cone": 1, "sphere": 0}[s], [x for x in [0, 1, 2, 4, 6, 8] if x != {"cube": 6, "cuboid": 6, "cylinder": 2, "cone": 1, "sphere": 0}[s]][:2] if s != "cube" else [4, 8], o="O2",
                                     pic={"cube": "🎲", "cuboid": "📦", "cylinder": "🥫", "cone": "🍦", "sphere": "⚽"}[s], reason=f"A {s} has {({'cube': 6, 'cuboid': 6, 'cylinder': 2, 'cone': 1, 'sphere': 0})[s]} flat faces."))(pick(r, ["cube", "cuboid", "cylinder", "cone", "sphere"]))],
        deep=[k_claim([("A sphere has no flat faces.", True, "A sphere is curved all over."), ("A square has 2 lines of symmetry.", False, "A square has 4 lines of symmetry."), ("A cone has one flat face.", True, "Its base is a flat circle.")], "O2"), k_odd(SYM, "O2"), k_all(SYM, "Symmetrical", "O2", "Tap ALL the symmetrical pictures.")],
        ex=EXQ(k_pick(SYM, "Symmetrical", "O2", "Which one is SYMMETRICAL?")))
    U.append(u)
    # ---------------------------------------------------------- 6
    u = unit(6, "Measures", "Geometry", "Measuring length in centimetres and metres, mass in grams and kilograms, capacity in millilitres and litres, and reading scales.",
             "Measure and compare lengths in centimetres and metres.", "Choose units for mass and capacity and read simple scales.", 2)
    LEN = [("pencil", "✏️", "cm"), ("ladybird", "🐞", "cm"), ("crayon", "🖍️", "cm"), ("leaf", "🍃", "cm"), ("bus", "🚌", "m"), ("football pitch", "⚽", "m"), ("swimming pool", "🏊", "m"), ("classroom", "🏫", "m")]
    build_sec(u, "6.1", "Centimetres and metres", "O1", [
        ("idea", "Units of length", ["Short things are measured in **centimetres** (cm): a pencil is about 15 cm. Long things are measured in **metres** (m): a bus is about 12 m. 1 m = 100 cm."], EM(("✏️", 1), ("🚌", 1))),
        ("check", PIC("Which would you measure in METRES?", "bus", [("pencil", "A pencil is short: use cm."), ("ladybird", "A ladybird is tiny: use cm.")], pics={"bus": "🚌", "pencil": "✏️", "ladybird": "🐞"}, o="O1")),
        ("idea", "Reading a ruler", ["Line one end up with **0**. Read the number at the other end."], {"kind": "numline", "min": 0, "max": 15, "mark": 9}),
        ("check", NUMS("A crayon starts at 0 and ends at the arrow. How long is it, in cm?", 9, [8, 10], o="O1", fig={"kind": "numline", "min": 0, "max": 15, "mark": 9}))],
        [("centimetre", "a small unit of length (cm)", "📏"), ("metre", "100 cm (m)", "📐"), ("ruler", "measures length", "📏"), ("length", "how long something is", "↔️")],
        T=[k_sort(LEN, ["cm", "m"], "O1", "Would you measure each one in cm or m?"), k_pick(LEN, "m", "O1", "Which would you measure in METRES?"),
           lambda r: (lambda n: NUMS("The object starts at 0 and ends at the arrow. How long is it, in cm?", n, near(r, n, 1, 20), o="O1", fig={"kind": "numline", "min": 0, "max": 20, "mark": n}, reason=f"It ends at {n}, so it is {n} cm long."))(r.randint(3, 19)),
           t_compare_size("O1", TALL, "tallest", "shortest")],
        deep=[k_claim([("1 metre is the same as 100 centimetres.", True, "1 m = 100 cm."), ("A pencil is about 15 metres long.", False, "It is about 15 cm."), ("You start measuring from 0 on a ruler.", True, "Line the end up with 0.")], "O1"),
              lambda r: (lambda a, b: PIC(f"A red ribbon is {a} cm. A blue ribbon is {b} cm. How much longer is the longer ribbon?", f"{abs(a - b)} cm", [(f"{a + b} cm", "That adds them."), (f"{abs(a - b) + 1} cm", "")], o="O1", d="H", reason=f"{max(a, b)} − {min(a, b)} = {abs(a - b)} cm."))(*r.sample(range(5, 40), 2)),
              k_all(LEN, "cm", "O1", "Tap ALL the things you would measure in centimetres.")],
        ex=EXQ(k_pick(LEN, "m", "O1", "Which would you measure in METRES?")))
    MASS = [("apple", "🍎", "g"), ("pencil", "✏️", "g"), ("feather", "🪶", "g"), ("coin", "🪙", "g"), ("bag of potatoes", "🥔", "kg"), ("dog", "🐕", "kg"), ("child", "🧒", "kg"), ("suitcase", "🧳", "kg")]
    CAPU = [("cup of tea", "☕", "ml"), ("spoon of medicine", "🥄", "ml"), ("small bottle", "🧴", "ml"), ("bath", "🛁", "l"), ("bucket", "🪣", "l"), ("fish tank", "🐠", "l")]
    build_sec(u, "6.2", "Mass and capacity", "O2", [
        ("idea", "Grams and kilograms", ["Light things are measured in **grams** (g). Heavier things are measured in **kilograms** (kg). 1 kg = 1000 g."], EM(("🍎", 1), ("🥔", 1))),
        ("check", PIC("Which unit would you use for the mass of a dog?", "kg", [("g", "Grams are for light things."), ("cm", "cm measures length.")], o="O2", pic="🐕")),
        ("idea", "Millilitres and litres", ["Small amounts of liquid are measured in **millilitres** (ml). Large amounts are measured in **litres** (l). 1 l = 1000 ml."], EM(("🥄", 1), ("🪣", 1))),
        ("check", PIC("Which holds about 1 litre?", "a big jug", [("a teaspoon", "A teaspoon holds about 5 ml."), ("a swimming pool", "That holds thousands of litres.")], pics={"a big jug": "🫗", "a teaspoon": "🥄", "a swimming pool": "🏊"}, o="O2"))],
        [("gram", "a small unit of mass (g)", "🍎"), ("kilogram", "1000 g (kg)", "🏋️"), ("litre", "a unit of capacity (l)", "🫗"), ("millilitre", "a small unit of capacity (ml)", "💧"), ("scale", "marks for reading a measurement", "⚖️")],
        T=[k_sort(MASS, ["g", "kg"], "O2", "Would you measure each one in g or kg?"), k_sort(CAPU, ["ml", "l"], "O2", "Would you measure each one in ml or l?"), k_pick(MASS, "kg", "O2", "Which would you weigh in KILOGRAMS?"),
           lambda r: (lambda n: NUMS("The scale shows a parcel's mass in kg. What does it read?", n, near(r, n, 0, 10), o="O2", fig={"kind": "numline", "min": 0, "max": 10, "mark": n}, reason=f"The arrow points to {n}, so it is {n} kg."))(r.randint(1, 9))],
        deep=[k_claim([("1 kg is the same as 1000 g.", True, "1 kg = 1000 g."), ("A bath holds about 2 ml of water.", False, "A bath holds many litres."), ("A feather is weighed in kilograms.", False, "A feather is very light: grams.")], "O2"),
              k_all(CAPU, "l", "O2", "Tap ALL the things you would measure in litres."), k_odd(MASS, "O2")],
        ex=EXQ(k_pick(MASS, "kg", "O2", "Which would you weigh in KILOGRAMS?")))
    U.append(u)
    # ---------------------------------------------------------- 7
    u = unit(7, "Time", "Geometry", "Telling the time to the quarter hour, the months of the year, and how long things take in minutes and hours.",
             "Read o'clock, half past, quarter past and quarter to.", "Know the months, and units of time: minutes, hours, days and weeks.", 2)
    build_sec(u, "7.1", "Quarter past and quarter to", "O1", [
        ("idea", "Quarters of an hour", ["When the long hand points to **3**, it has gone a quarter of the way round: **quarter past**. When it points to **9**, there is a quarter to go: **quarter to** the next hour."], {"kind": "clock", "h": 4, "m": 15}),
        ("check", PIC("What time is it?", "quarter past 4", [("quarter to 4", "The long hand at 3 means quarter past."), ("half past 4", "Half past has the long hand at 6.")], o="O1", fig={"kind": "clock", "h": 4, "m": 15})),
        ("mistake", "Quarter to – which hour?", ["At quarter to 6 the short hand is nearly at 6, not yet past it. Say the hour that is coming next."]),
        ("check", PIC("What time is it?", "quarter to 6", [("quarter past 5", "The long hand is at 9, not 3."), ("quarter to 5", "The short hand is nearly at 6.")], o="O1", fig={"kind": "clock", "h": 5, "m": 45}))],
        [("quarter past", "the long hand points to 3", "🕒"), ("quarter to", "the long hand points to 9", "🕘"), ("minute", "a short unit of time", "⏱️"), ("hour", "60 minutes", "⏰")],
        T=[t_clock("O1", (15,)), t_clock("O1", (45,)), t_clock("O1", (0, 15, 30, 45)),
           lambda r: (lambda m: PIC(f"Where does the long hand point at {oclock(3, m).split(' ')[0]} {oclock(3, m).split(' ')[1]} 3?" if False else f"Where does the long hand point at {oclock(3, m) if m != 45 else 'quarter to 4'}?", {0: "12", 15: "3", 30: "6", 45: "9"}[m], [(x, "") for x in ["12", "3", "6", "9"] if x != {0: "12", 15: "3", 30: "6", 45: "9"}[m]][:2], o="O1",
                                    reason="o'clock → 12, quarter past → 3, half past → 6, quarter to → 9."))(r.choice([0, 15, 30, 45]))],
        deep=[claim_n("O1", lambda r: (lambda h, m: (f"The clock shows {oclock(h, m)}.", True, f"It shows {oclock(h, m)}.", {"kind": "clock", "h": h, "m": m}) if r.random() < 0.5 else (f"The clock shows {oclock(h, 60 - m if m in (15, 45) else m)}.", False, f"The long hand is at {m // 5 or 12}, so it is {oclock(h, m)}.", {"kind": "clock", "h": h, "m": m}))(r.randint(1, 11), r.choice([15, 45]))),
              lambda r: (lambda h: PIC(f"It is quarter past {h}. What time will it be in 15 minutes?", f"half past {h}", [(f"quarter to {h + 1}", "That is 30 minutes later."), (f"{h + 1} o'clock", "That is 45 minutes later.")], o="O1", d="H", reason="Quarter past + 15 minutes = half past."))(r.randint(1, 10)),
              lambda r: (lambda h: PIC(f"It is half past {h}. What time will it be in 30 minutes?", f"{h + 1} o'clock", [(f"quarter to {h + 1}", "That is 15 minutes later."), (f"half past {h + 1}", "That is an hour later.")], o="O1", d="H", reason="Half an hour after half past is the next o'clock."))(r.randint(1, 10))],
        ex=EXQ(t_clock("O1", (15,))))
    build_sec(u, "7.2", "Months and how long", "O2", [
        ("idea", "Months of the year", ["There are **12 months** in a year: January, February, March, April, May, June, July, August, September, October, November, December."], EM(("🗓️", 1))),
        ("check", PIC("Which month comes after March?", "April", [("February", "February comes before March."), ("May", "May comes after April.")], o="O2")),
        ("idea", "Units of time", ["**60 minutes** = 1 hour. **24 hours** = 1 day. **7 days** = 1 week. Brushing your teeth takes minutes. A film takes hours."], EM(("⏱️", 1), ("⏰", 1), ("📅", 1))),
        ("check", PIC("How long does it take to brush your teeth?", "2 minutes", [("2 hours", "That is far too long!"), ("2 days", "Much too long.")], o="O2", pic="🪥"))],
        [("month", "one of 12 parts of a year", "🗓️"), ("year", "12 months", "🎆"), ("minute", "60 seconds", "⏱️"), ("hour", "60 minutes", "⏰"), ("week", "7 days", "📅")],
        T=[t_days_order("O2", MONTHS, 4, "months"), lambda r: (lambda i: PIC(f"Which month comes after {MONTHS[i]}?", MONTHS[(i + 1) % 12], [(x, "") for x in others(r, [m for m in MONTHS if m not in (MONTHS[i], MONTHS[(i + 1) % 12])], None)], o="O2", reason=f"… {MONTHS[i]}, {MONTHS[(i + 1) % 12]} …", pic="🗓️"))(r.randint(0, 11)),
           k_sort([("brush teeth", "🪥", "Minutes"), ("eat a snack", "🍎", "Minutes"), ("tie your shoes", "👟", "Minutes"), ("watch a film", "🎬", "Hours"), ("a school day", "🏫", "Hours"), ("a long car journey", "🚗", "Hours")], ["Minutes", "Hours"], "O2", "Does each one take minutes or hours?"),
           k_match([("1 hour", "60 minutes"), ("1 day", "24 hours"), ("1 week", "7 days"), ("1 year", "12 months")], "O2", "Match the times that are the same.")],
        deep=[k_claim([("There are 7 days in a week.", True, "Monday to Sunday is 7 days."), ("An hour is 100 minutes.", False, "An hour is 60 minutes."), ("There are 12 months in a year.", True, "January to December is 12.")], "O2"),
              lambda r: (lambda i: PIC(f"It is {MONTHS[i]} now. Which month will it be in 2 months?", MONTHS[(i + 2) % 12], [(MONTHS[(i + 1) % 12], "That is 1 month."), (MONTHS[(i + 3) % 12], "That is 3 months.")], o="O2", d="H", reason=f"{MONTHS[i]} → {MONTHS[(i + 1) % 12]} → {MONTHS[(i + 2) % 12]}."))(r.randint(0, 11)),
              lambda r: (lambda h, k: PIC(f"A party starts at {h} o'clock and ends at {h + k} o'clock. How long is the party?", f"{k} hours", [(f"{k + 1} hours", ""), (f"{h + k} hours", "That is the end time, not how long.")], o="O2", d="H", reason=f"From {h} to {h + k} is {k} hours.", fig={"kind": "clock", "h": h, "m": 0}))(r.randint(1, 7), r.randint(2, 4))],
        ex=EXQ(t_days_order("O2", MONTHS, 4, "months")))
    U.append(u)
    # ---------------------------------------------------------- 8
    u = unit(8, "Data", "Statistics", "Collecting data with tally marks, reading pictograms where a picture can stand for 2, reading block graphs, and sorting with Carroll diagrams.",
             "Record and read data in tallies and pictograms.", "Read block graphs and sort numbers and objects in diagrams.", 2)
    def tally(n): return "卌 " * (n // 5) + "|" * (n % 5)
    build_sec(u, "8.1", "Tallies and pictograms", "O1", [
        ("idea", "Tally marks", ["We make a **tally** mark for each thing we count. Every **fifth** mark goes across the other four, so we can count in 5s: 卌 = 5."], EM(("✏️", 1))),
        ("check", NUMS("How many does this tally show?  卌 |||", 8, [7, 13], o="O1")),
        ("idea", "When one picture stands for 2", ["In some pictograms, one picture stands for **2**. Half a picture stands for 1. Always read the **key**."], {"kind": "emojis", "groups": [["⚽", 3]], "size": 32}),
        ("check", NUMS("Key: ⚽ = 2 children. ⚽⚽⚽ shows how many children?", 6, [3, 5], o="O1"))],
        [("tally", "a mark for each thing counted", "✏️"), ("pictogram", "a chart made of pictures", "📊"), ("key", "tells what each picture means", "🔑"), ("data", "information we collect", "📋")],
        T=[lambda r: (lambda n: NUMS(f"How many does this tally show?  {tally(n)}", n, near(r, n, 0, 25), o="O1", reason=f"Count the gates in 5s, then the ones: {n}."))(r.randint(3, 19)),
           lambda r: (lambda n: PIC(f"Which tally shows {n}?", tally(n), [(tally(n + 1), ""), (tally(n - 1), "")], o="O1", reason=f"{n // 5} gate(s) of 5 and {n % 5} more."))(r.randint(4, 17)),
           t_pictogram("O1", 9, 3),
           lambda r: (lambda k, e: NUMS(f"Key: {e} = 2 children. {e * k} shows how many children?", 2 * k, [k, 2 * k + 1], o="O1", reason=f"{k} pictures × 2 = {2 * k}."))(r.randint(2, 7), pick(r, ["⚽", "🍎", "⭐"]))],
        deep=[t_pictogram("O1", 9, 4), lambda r: (lambda k, e: NUMS(f"Key: {e} = 2 children. How many {e} pictures show 10 children?" if k == 5 else f"Key: {e} = 2 children. How many {e} pictures show {2 * k} children?", k, [2 * k, k + 1], o="O1", d="H", reason=f"{2 * k} ÷ 2 = {k} pictures."))(r.randint(2, 8), pick(r, ["⚽", "🍎", "⭐"])),
              k_claim([("The fifth tally mark goes across the other four.", True, "That makes a gate of 5."), ("In every pictogram one picture is always 1.", False, "Read the key: a picture can stand for 2 or more.")], "O1")],
        ex=EXQ(t_pictogram("O1", 9, 3)))
    build_sec(u, "8.2", "Block graphs and sorting", "O2", [
        ("idea", "Block graphs", ["A **block graph** shows each thing as a block. The **tallest** column is the most popular. Read across from the top of a column to the scale."], {"kind": "barchart", "labels": ["dogs", "cats", "fish"], "values": [6, 4, 2], "ymax": 8, "step": 1, "ylabel": "Number of children"}),
        ("check", NUMS("How many children chose cats?", 4, [3, 6], o="O2", fig={"kind": "barchart", "labels": ["dogs", "cats", "fish"], "values": [6, 4, 2], "ymax": 8, "step": 1, "ylabel": "Number of children"})),
        ("idea", "Carroll diagrams", ["A **Carroll diagram** sorts things by a rule, such as **even** / **not even**, or **more than 10** / **not more than 10**."], EM(("🗂️", 1))),
        ("check", PIC("Where does 14 go?", "even", [("not even", "14 ends in 4, so it is even.")], o="O2"))],
        [("block graph", "a chart with columns of blocks", "📊"), ("most popular", "chosen by the most people", "🏆"), ("Carroll diagram", "a table that sorts by a rule", "🗂️"), ("sort", "put into groups", "📥")],
        T=[t_barchart("O2"), t_barchart("O2", 10, 4, PETS, False), t_oddeven("O2"),
           lambda r: (lambda ns: GD("Sort the numbers: more than 20, or not?", "Group", [(str(n), "More than 20" if n > 20 else "Not more than 20") for n in ns], o="O2", extra=["More than 20", "Not more than 20"], reason="Compare each number with 20."))(r.sample(range(1, 50), 5))],
        deep=[t_barchart("O2", 10, 4), claim_n("O2", lambda r: (lambda cats, vals: (f"More children chose {cats[0][0]} than {cats[1][0]}.", vals[0] > vals[1], f"{cats[0][0]}: {vals[0]}, {cats[1][0]}: {vals[1]}.",
                                                                                     {"kind": "barchart", "labels": [c for c, _ in cats], "values": vals, "ymax": 10, "step": 1, "ylabel": "Number of children"}))(*chart(r, 10, 3, PETS))),
              lambda r: MS("Tap ALL the numbers that are even AND more than 10.", [str(x) for x in r.sample([12, 14, 16, 18, 20, 22, 24], 2)], [str(x) for x in r.sample([4, 6, 8, 13, 15, 17], 2)], o="O2", d="H", reason="They must be even and bigger than 10.")],
        ex=EXQ(t_barchart("O2")))
    U.append(u)
    return U


TITLES = {1: ["Numbers to 10", "Numbers to 20", "Addition", "Subtraction", "Shapes", "Measures", "Time", "Halves, Patterns and Data"],
          2: ["Numbers to 100", "Addition and Subtraction", "Multiplication and Division", "Fractions", "Shapes and Symmetry", "Measures", "Time", "Data"]}
