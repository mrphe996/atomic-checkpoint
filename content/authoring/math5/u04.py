# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 4 Averages (4.1 The mode, 4.2 The median). Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(4, "Averages", "Statistics and probability",
         "Finding the mode and the median of a set of data, and using them to describe and compare data.",
         {"O1": {"code": "5Ss.03", "sec": "4.1", "codeNote": "", "t": "Find and interpret the mode of a set of data, including data with no mode or more than one mode."},
          "O2": {"code": "5Ss.04", "sec": "4.2", "codeNote": "", "t": "Find and interpret the median of a set of data."}})
FRUIT = ["apple", "banana", "mango", "orange", "pear"]
NAMES = ["Ana", "Bo", "Cai", "Dev", "Ema", "Finn", "Gia"]

s = U.section("4.1", "The mode", ["O1"])
s.idea("Most common", ["The **mode** is the value that appears **most often**. In 3, 5, 5, 7, 8 the mode is 5.",
       "A set can have **two modes**, or **no mode** if every value appears the same number of times."], fig={"kind": "barchart", "labels": FRUIT[:4], "values": [4, 9, 6, 3], "ymax": 10, "step": 2, "ylabel": "Children"})
s.check(S("Favourite fruits: apple, mango, apple, pear, mango, apple. What is the mode?", ["apple", "Apple"], o="O1"))
s.mistake("The mode is a value", ["In the bar chart the mode is 'banana', not 9. Give the value, not how many."])


def m1(r):
    xs = r.sample(range(1, 20), 4); m = pick(r, xs); xs = xs + [m, m]; r.shuffle(xs)
    return N(f"Find the mode of {', '.join(map(str, xs))}.", m, o="O1")
def m2(r):
    v = r.sample([2, 3, 4, 5, 6, 7, 8, 9], 4); k = v.index(max(v)); lab = FRUIT[:4]
    return S("The bar chart shows favourite fruits. What is the mode?", [lab[k], lab[k].capitalize()], o="O1", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 10, "step": 2, "ylabel": "Children"})
def m3(r):
    sh = ["2", "4", "6", "8", "10"]; v = r.sample([1, 2, 3, 4, 5, 6], 5); k = v.index(max(v))
    return N("The table shows shoe sizes in a group. What is the modal shoe size?", int(sh[k]) + 20, o="O1", data={"head": ["Size", *[str(int(x) + 20) for x in sh]], "rows": [["Children", *map(str, v)]]})
def m4(r):
    xs = r.sample(range(1, 30), 5)
    return MC(f"What is the mode of {', '.join(map(str, xs))}?", "there is no mode", [str(xs[0]), str(max(xs)), str(min(xs))], o="O1")
def m5(r):
    a, b = r.sample(range(1, 15), 2); c = r.randint(15, 25)
    xs = [a, a, b, b, c]; r.shuffle(xs)
    return MC(f"What are the modes of {', '.join(map(str, xs))}?", f"{min(a, b)} and {max(a, b)}", [str(c), f"{min(a, b)} only", "there is no mode"], o="O1", d="H")
def m6(r):
    xs = [r.randint(1, 6) for _ in range(10)]
    cs = sorted((xs.count(x) for x in set(xs)), reverse=True)
    if len(cs) > 1 and cs[0] == cs[1]: return None
    m = max(set(xs), key=xs.count)
    return TB(f"Dice scores: {', '.join(map(str, xs))}. Complete the tally table.", ["Score", "1", "2", "3", "4", "5", "6"], [["Frequency", *[B(xs.count(i)) for i in range(1, 7)]]], o="O1")
def m7(r):
    xs = r.sample(range(2, 12), 4); m = xs[0]; xs = xs + [m]; r.shuffle(xs)
    return N(f"The numbers {', '.join(map(str, xs))} have mode {m}. Which number could you add so that {m} is still the only mode?", m, o="O1", d="H")
def m8(r):
    v = r.sample([2, 3, 4, 5, 6, 7, 8], 5); k = v.index(max(v))
    return S("The table shows how many goals were scored in some matches. What is the modal number of goals?", [str(k)], o="O1", data={"head": ["Goals", "0", "1", "2", "3", "4"], "rows": [["Matches", *map(str, v)]]})


s.std([m2, m3, m1, m4, m6, m8, m5, m7], EX("Explain why 2, 3, 4, 5 has no mode.", [("each value appears only once", "once|same number|each"), ("no value appears more often than the others", "no value|none|more often")], "Every value appears exactly once, so no value appears more often than the others. There is no mode.", o="O1"))

s = U.section("4.2", "The median", ["O2"])
s.idea("The middle value", ["The **median** is the **middle value** when the data are in order. For 8, 3, 6, 2, 9 → 2, 3, **6**, 8, 9 → the median is 6.",
       "If there are two middle values, the median is halfway between them: 2, 4, 6, 8 → (4 + 6) ÷ 2 = **5**."], table={"head": ["In order", "2", "3", "6", "8", "9"], "rows": [["", "", "", "↑ middle", "", ""]]})
s.check(N("Find the median of 7, 1, 4, 9, 5.", 5, o="O2"))
s.mistake("Order first", ["The median of 9, 1, 5 is 5 (order: 1, 5, 9), not 1."])


def d1(r):
    xs = r.sample(range(1, 30), 5)
    return N(f"Find the median of {', '.join(map(str, xs))}.", sorted(xs)[2], o="O2")
def d2(r):
    xs = r.sample(range(1, 40), 7)
    return N(f"Find the median of {', '.join(map(str, xs))}.", sorted(xs)[3], o="O2")
def d3(r):
    nm = r.sample(NAMES, 5); xs = r.sample(range(120, 150), 5)
    return N("The table shows children's heights in cm. Find the median height.", sorted(xs)[2], "cm", units=["cm"], o="O2", data={"head": ["Name", *nm], "rows": [["Height (cm)", *map(str, xs)]]})
def d4(r):
    xs = r.sample(range(1, 20), 4); s_ = sorted(xs)
    if (s_[1] + s_[2]) % 2: return None
    return N(f"Find the median of {', '.join(map(str, xs))}.", (s_[1] + s_[2]) // 2, o="O2", d="H")
def d5(r):
    xs = r.sample(range(1, 50), 5)
    return OD(f"Put the data in order to find the median: {', '.join(map(str, xs))}", [str(x) for x in sorted(xs)], o="O2")
def d6(r):
    lab = ["Mon", "Tue", "Wed", "Thu", "Fri"]; v = r.sample(range(2, 20), 5)
    return N("The bar chart shows how many books were borrowed each day. Find the median.", sorted(v)[2], "books", units=["books"], o="O2", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 20, "step": 2, "ylabel": "Books"})
def d7(r):
    xs = r.sample(range(1, 30), 5); s_ = sorted(xs)
    return MC(f"Lin says the median of {', '.join(map(str, xs))} is {xs[2]}. Is she right?", "Yes" if xs[2] == s_[2] else f"No, it is {s_[2]}", ["Yes" if xs[2] != s_[2] else f"No, it is {xs[0]}", f"No, it is {s_[-1]}"], o="O2", d="H") if xs[0] != s_[2] else None
def d8(r):
    a, b = r.sample(range(1, 25), 2)
    xs = r.sample(range(1, 30), 5); m = sorted(xs)[2]
    return TB(f"Data: {', '.join(map(str, xs))}. Complete the table.", ["Smallest", "Median", "Largest"], [[B(min(xs)), B(m), B(max(xs))]], o="O2")


s.std([d3, d6, d1, d2, d5, d8, d4, d7], EX("Explain how to find the median of 10, 4, 7.", [("put them in order: 4, 7, 10", "order|4, ?7, ?10"), ("the middle value is 7", "middle|\\b7\\b")], "Put the numbers in order: 4, 7, 10. The middle value is 7, so the median is 7.", o="O2"))

U.mindmap(("Mode", "Most common value • can have none or two", "O1", "4.1"), ("Median", "Middle value in order", "O2", "4.2"))
