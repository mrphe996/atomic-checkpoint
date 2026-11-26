# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 11 Ratio and proportion. Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from fractions import Fraction as Fr
from math import gcd
from kit import *

U = Unit(11, "Ratio and proportion", "Number",
         "Simplifying and sharing in ratios, comparing ratios, and solving direct and inverse proportion problems.",
         {"O1": {"sec": "11.1", "code": "9Nf.07", "codeNote": "", "t": "Use ratios: simplify, share an amount in a ratio, and solve problems where one share or the difference is known."},
          "O2": {"sec": "11.2", "code": "9Nf.08", "codeNote": "", "t": "Recognise and solve problems involving direct and inverse proportion, including best-value comparisons."}})

# ================================================================== 11.1
s = U.section("11.1", "Using ratios", ["O1"])
s.idea("Ratios", ["A **ratio** compares quantities: 12 : 18 simplifies to **2 : 3** (divide by the HCF 6).",
       "To **share** an amount in the ratio a : b, find the total number of parts a + b, then the value of **one part**."])
s.example("Sharing", "Share $84 in the ratio 3 : 4.", [("3 + 4 = 7 parts", ""), ("one part = 84 ÷ 7 = $12", ""), ("3 × 12 = $36 and 4 × 12 = $48", "")], "$36 and $48")
s.check(N("Share 90 kg in the ratio 2 : 7. How much is the larger share?", 70, "kg", units=["kg"], reason="2 + 7 = 9 parts; one part = 90 ÷ 9 = 10 kg; larger share = 7 × 10 = 70 kg.", o="O1"))
s.example("Using the difference", "Ana and Ben share sweets in the ratio 5 : 2. Ana gets 21 more than Ben. How many sweets are there?", [("difference = 5 − 2 = 3 parts = 21", ""), ("one part = 7", ""), ("total = 7 parts = 49", "")], "49")
s.check(MC("Before you read on: the ratio of boys to girls is 3 : 5. What fraction of the class are boys?", "3/8", [("3/5", "There are 3 + 5 = 8 parts in total."), ("5/8", "That is the girls.")], o="O1"))
s.mistake("Parts, not people", ["In 3 : 5, there are 8 parts, not 2. Dividing by the number of people is a common error."])
s.check(N("Write the ratio 4 : 10 in the form 1 : n. Find n.", 2.5, reason="Divide both parts by 4: 1 : 2.5.", o="O1"))
def a1(r):
    a, b, k = r.randint(1, 9), r.randint(1, 9), r.randint(2, 12)
    if gcd(a, b) != 1 or a == b: return None
    return TB(f"Simplify the ratio {a*k} : {b*k}.", ["First", "Second"], [[B(a), B(b)]], reason=f"Divide both parts by the highest common factor {k}: {a} : {b}.", o="O1")
def a2(r):
    a, b = r.randint(1, 9), r.randint(1, 9); u = r.randint(3, 40); tot = (a + b) * u
    if a == b: return None
    item = pick(r, [("$", ""), ("", " kg"), ("", " litres"), ("", " m")])
    return TB(f"Share {item[0]}{tot}{item[1]} in the ratio {a} : {b}.", ["First share", "Second share"], [[B(a * u), B(b * u)]], reason=f"{a} + {b} = {a + b} parts; one part = {tot} ÷ {a + b} = {u}; shares {a} × {u} = {a * u} and {b} × {u} = {b * u}.", o="O1")
def a3(r):
    a, b = r.randint(2, 9), r.randint(1, 8)
    if a <= b: return None
    u = r.randint(3, 25)
    return N(f"Paint is mixed red : white in the ratio {a} : {b}. There is {(a-b)*u} ml more red than white. How much paint is there altogether?", (a + b) * u, "ml", units=["ml"], reason=f"The difference is {a} − {b} = {a - b} parts = {(a - b) * u} ml, so one part = {u} ml. Total = {a + b} parts = {(a + b) * u} ml.", o="O1", d="H")
def a4(r):
    a, b, c = r.randint(1, 6), r.randint(1, 6), r.randint(1, 6); u = r.randint(4, 30)
    return N(f"Share ${(a+b+c)*u} in the ratio {a} : {b} : {c}. What is the largest share?", max(a, b, c) * u, "$", units=["$", "dollars"], reason=f"{a} + {b} + {c} = {a + b + c} parts; one part = {(a + b + c) * u} ÷ {a + b + c} = {u}; largest = {max(a, b, c)} × {u} = {max(a, b, c) * u}.", o="O1", d="H")
def a5(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    if a == b: return None
    return N(f"Write {a} : {b} in the form 1 : n. Give n to 2 d.p.", round(b / a, 2), reason=f"Divide both parts by {a}: n = {b} ÷ {a} = {round(b / a, 2)}.", o="O1", tol=0.006)
def a6(r):
    g, b = r.randint(2, 7), r.randint(2, 7); u = r.randint(3, 12)
    if g == b: return None
    return N(f"In a club the ratio of girls to boys is {g} : {b}. There are {g*u} girls. How many members are there?", (g + b) * u, "members", units=["members"], reason=f"{g} parts = {g * u} girls, so one part = {u}. Members = {g + b} parts = {(g + b) * u}.", o="O1")
def a7(r):
    cm, km = pick(r, [(2, 1), (4, 1), (5, 2), (3, 1.5)]); sc = int(km * 100000 / cm)
    d = r.randint(3, 20)
    return N(f"A map has scale 1 : {sc:,}. Two towns are {d} cm apart on the map. How far apart are they in km?", d * sc / 100000, "km", units=["km"], reason=f"{d} × {sc} = {d * sc} cm = {fmt(d * sc / 100000)} km (÷ 100 000).", o="O1", d="H")
def a8(r):
    a, b = r.randint(1, 5), r.randint(1, 5); c, d = r.randint(1, 5), r.randint(1, 5)
    if a * d == b * c: return None
    x, y = Fr(a, a + b), Fr(c, c + d)
    return MC(f"Mix A is juice : water = {a} : {b}. Mix B is juice : water = {c} : {d}. Which mix has the greater fraction of juice?", "Mix A" if x > y else "Mix B", [("Mix B" if x > y else "Mix A", f"Juice fractions: A = {frac(x)}, B = {frac(y)}."), ("They are the same", "")], o="O1", d="H")
def a9(r):
    a, b = r.randint(2, 7), r.randint(2, 7); m = r.randint(2, 6)
    if a == b: return None
    return N(f"The ratio of x : y is {a} : {b}. If y = {b*m}, find x + y.", (a + b) * m, reason=f"y = {b} parts = {b * m}, so one part = {m}; x + y = {a + b} parts = {(a + b) * m}.", o="O1")
s.core(a1(s.rng) or a1(s.rng) or TB("Simplify the ratio 24 : 36.", ["First", "Second"], [[B(2), B(3)]], o="O1"),
       a2(s.rng) or TB("Share $96 in the ratio 5 : 3.", ["First share", "Second share"], [[B(60), B(36)]], o="O1"),
       a3(s.rng) or N("Red : white = 5 : 2. There is 60 ml more red. Total?", 140, "ml", units=["ml"], o="O1", d="H"),
       a4(s.rng), a6(s.rng) or N("Girls : boys = 3 : 4, 18 girls. Total members?", 42, "members", units=["members"], o="O1"),
       a7(s.rng), a8(s.rng) or MC("Mix A is juice : water = 1 : 3. Mix B is 2 : 5. Which has the greater fraction of juice?", "Mix B", [("Mix A", ""), ("They are the same", "")], o="O1", d="H"),
       EX("Explain how to share $60 in the ratio 1 : 4.", [("5 parts in total", ["5 parts|five parts|1 ?\\+ ?4"]), ("one part is $12, so $12 and $48", ["12|48"])], "There are 1 + 4 = 5 parts, so one part is 60 ÷ 5 = $12. The shares are $12 and $48.", o="O1"))
def k1_1(r):
    a, b = r.sample(range(2, 8), 2); extra = r.randint(2, 6); k = r.randint(2, 6)
    return N(f"A bag has red and blue counters in the ratio {a} : {b}. There are {a * k} red counters. How many counters are there altogether?", (a + b) * k, o="O1", d="H", reason=f"{a} parts = {a * k}, 1 part = {k}; total {a + b} parts = {(a + b) * k}.")


s.gen("p", 44, a1, a2, a3, a4, a5, a6, a7, a8, a9)
s.capped("p", [1] * 1, [k1_1]).capped("m", [2] * 1, [k1_1])   # v2 reasoning kinds
s.gen("a", 8, a3, a8, lambda r: (lambda a, b, k: N(f"The ratio of boys to girls in a class is {a} : {b}. {k} more boys join and the ratio becomes 1 : 1. How many students were there at first?", (a + b) * (k // (b - a)) if False else (a + b) * k // (b - a), reason=f"The gap of {b - a} parts is {k} boys, so one part = {k // (b - a)}; at first there were {a + b} parts = {(a + b) * k // (b - a)}." if b > a and k % (b - a) == 0 else "", o="O1", d="VH") if b > a and k % (b - a) == 0 else None)(r.randint(2, 6), r.randint(3, 9), r.randint(2, 24)))

# ================================================================== 11.2
s = U.section("11.2", "Direct and inverse proportion", ["O2"])
s.idea("Direct proportion", ["Two quantities are in **direct proportion** if, when one doubles, the other doubles. Their **ratio is constant**: y = kx.",
       "Use the **unitary method**: find the value for ONE, then multiply."])
s.example("Unitary method", "5 pens cost $3.40. Find the cost of 8 pens.", [("1 pen = 3.40 ÷ 5 = $0.68", ""), ("8 pens = 8 × 0.68 = $5.44", "")], "$5.44")
s.check(N("6 m of rope has mass 1.5 kg. Find the mass of 10 m.", 2.5, "kg", units=["kg"], o="O2"))
s.idea("Inverse proportion", ["Two quantities are in **inverse proportion** if, when one doubles, the other **halves**. Their **product is constant**: xy = k.",
       "Example: more workers → fewer days. 4 workers take 6 days, so the job is 24 worker-days; 3 workers take 24 ÷ 3 = 8 days."])
s.idea("Direct or inverse?", ["Direct proportion: double one, double the other (cost of apples). Inverse proportion: double one, HALVE the other (more workers, less time). In inverse proportion the product stays the same.",
       "4 workers take 6 days: 4 × 6 = 24 worker-days, so 8 workers take 24 ÷ 8 = 3 days."])
s.check(MC("Before you read on: 3 pumps empty a tank in 12 hours. How long do 6 pumps take?", "6 hours", [("24 hours", "More pumps empty it faster."), ("12 hours", "Doubling the pumps halves the time.")], o="O2"))
s.mistake("Which proportion?", ["Ask: if one quantity goes up, does the other go up (direct) or down (inverse)? Then multiply or divide accordingly."])
s.check(N("4 pumps empty a tank in 9 hours. How long do 6 pumps take?", 6, "hours", units=["hours"], o="O2"))
def b1(r):
    n, p, m = r.randint(3, 9), round(r.uniform(0.5, 4), 2), r.randint(2, 15)
    item = pick(r, ["pens", "apples", "notebooks", "tickets", "bottles"])
    return N(f"{n} {item} cost ${fmt(round(n*p,2))}. Find the cost of {m} {item}.", round(m * round(n * p, 2) / n, 2), "$", units=["$"], tol=0.006, reason=f"One costs {fmt(round(n * p, 2))} ÷ {n}; {m} cost {fmt(round(n * p, 2))} ÷ {n} × {m} = ${round(m * round(n * p, 2) / n, 2):.2f}.", o="O2")
def b2(r):
    w, d = r.randint(2, 9), r.randint(2, 12); w2 = pick(r, [x for x in range(2, 13) if (w * d) % x == 0 and x != w])
    return N(f"{w} builders take {d} days to build a wall. How many days would {w2} builders take, working at the same rate?", w * d / w2, "days", units=["days"], reason=f"Inverse proportion: the job is {w} × {d} = {w * d} builder-days; {w * d} ÷ {w2} = {fmt(w * d / w2)} days.", o="O2")
def b3(r):
    rows = [("Cost of apples and number of apples", "Direct"), ("Number of workers and time to finish a job", "Inverse"), ("Speed and time for a fixed journey", "Inverse"),
            ("Distance travelled at a steady speed and time", "Direct"), ("Number of people sharing a pizza and size of each share", "Inverse"), ("Mass of flour and number of cakes made", "Direct")]
    return GD("Is each pair in direct or inverse proportion?", "Proportion", r.sample(rows, 4), o="O2")
def b4(r):
    s1, p1 = r.randint(200, 600), round(r.uniform(1, 5), 2); s2 = s1 * pick(r, [2, 3]) // 2 + pick(r, [0, 50]); p2 = round(p1 * s2 / s1 * r.uniform(0.85, 1.15), 2)
    if abs(p1 / s1 - p2 / s2) < 0.0002: return None
    best = "Small" if p1 / s1 < p2 / s2 else "Large"
    return MC(f"Which pack is better value? Small: {s1} g for ${p1:.2f}. Large: {s2} g for ${p2:.2f}.", best, [("Large" if best == "Small" else "Small", ""), ("They are the same value", "")], o="O2", d="H",
              data={"head": ["Pack", "Mass (g)", "Price ($)"], "rows": [["Small", str(s1), f"{p1:.2f}"], ["Large", str(s2), f"{p2:.2f}"]]})
def b5(r):
    k = r.randint(2, 12); x1 = r.randint(2, 8); x2 = r.randint(9, 20); inv = r.random() < 0.5
    if inv:
        K = k * x1 * x2
        return N(f"y is inversely proportional to x. When x = {x1}, y = {K//x1}. Find y when x = {x2}.", K / x2, reason=f"xy is constant: {x1} × {K // x1} = {K}; y = {K} ÷ {x2} = {fmt(round(K / x2, 3))}.", o="O2", d="H", tol=0.006)
    return N(f"y is directly proportional to x. When x = {x1}, y = {k*x1}. Find y when x = {x2}.", k * x2, reason=f"y ÷ x is constant: {k * x1} ÷ {x1} = {k}; y = {k} × {x2} = {k * x2}.", o="O2")
def b6(r):
    v, t = r.randint(30, 90), r.randint(2, 6); v2 = pick(r, [x for x in range(20, 121, 5) if (v * t * 60) % x == 0 and x != v])
    return N(f"A journey takes {t} hours at {v} km/h. How many minutes does it take at {v2} km/h?", v * t * 60 / v2, "minutes", units=["minutes"], reason=f"Distance = {v} × {t} = {v * t} km; time = {v * t} ÷ {v2} h = {fmt(v * t * 60 / v2)} minutes.", o="O2", d="H")
def b7(r):
    serves, g, n = pick(r, [4, 6, 8]), r.randint(100, 500), pick(r, [3, 5, 10, 12])
    ing = pick(r, ["flour", "rice", "butter", "sugar"])
    return N(f"A recipe for {serves} people uses {g} g of {ing}. How much {ing} is needed for {n} people? (1 d.p.)", round(g * n / serves, 1), "g", units=["g"], tol=0.06, reason=f"{g} ÷ {serves} = {fmt(round(g / serves, 3))} g per person; × {n} = {round(g * n / serves, 1)} g.", o="O2")
def b8(r):
    k = r.randint(2, 8); xs = [1, 2, 4, 8]; inv = r.random() < 0.5
    ys = [k * 8 // x for x in xs] if inv else [k * x for x in xs]
    return MC("What type of proportion does the table show?", "Inverse" if inv else "Direct", [("Direct" if inv else "Inverse", "Check: does x × y stay the same (inverse) or y ÷ x (direct)?"), ("Neither", "")], o="O2", data={"head": ["x"] + [str(x) for x in xs], "rows": [["y"] + [str(y) for y in ys]]})
def b9(r):
    k = r.randint(2, 6); c = r.randint(1, 9)
    return MC(f"Is y = {k}x + {c} an example of direct proportion?", "No, because the line does not pass through the origin", [("Yes, because it is a straight line", "Direct proportion needs y = kx (through (0, 0))."), (f"Yes, the constant is {k}", ""), ("No, because it is a curve", "")], o="O2", d="H")
s.core(b1(s.rng), b2(s.rng), b3(s.rng), b4(s.rng) or b4(s.rng) or b4(s.rng), b5(s.rng), b8(s.rng), b9(s.rng),
       EX("Explain how you can tell from a table whether x and y are in inverse proportion.", [("multiply x by y", ["multipl|product|x ?× ?y|xy"]), ("the product is always the same", ["same|constant|equal"])], "Multiply each x by its y. If the product is always the same, x and y are in inverse proportion.", o="O2"))
def k2_1(r):
    rows = r.sample([("number of workers and time to finish a job", "Inverse"), ("number of tickets and total cost", "Direct"), ("speed and time for a fixed journey", "Inverse"), ("length of fabric and its price", "Direct")], 4)
    return GD("Is each relationship direct or inverse proportion?", "Proportion", rows, o="O2", d="H", extra=["Direct", "Inverse"], reason="Ask: when one doubles, does the other double (direct) or halve (inverse)?")
def k2_2(r):
    w, d = pick(r, [(4, 6), (3, 8), (6, 10), (5, 12)]); w2 = pick(r, [2, 8, 10, 12, 15])
    if (w * d) % w2: return None
    return N(f"{w} workers take {d} days to build a wall. How long would {w2} workers take, working at the same rate?", w * d // w2, "days", units=["days"], o="O2", d="H", reason=f"{w} × {d} = {w * d} worker-days; ÷ {w2} = {w * d // w2} days.")


s.gen("p", 44, b1, b2, b3, b4, b5, b6, b7, b8, b9)
s.capped("p", [1] * 2, [k2_1, k2_2]).capped("m", [2] * 2, [k2_1, k2_2])   # v2 reasoning kinds
s.gen("a", 8, b6, b4, lambda r: (lambda w, d, e: N(f"{w} machines complete an order in {d} hours. After 2 hours, {e} machines break down. How many more hours are needed to finish? (1 d.p.)", round((w * d - 2 * w) / (w - e), 1), "hours", units=["hours"], tol=0.06, reason=f"The order needs {w} × {d} = {w * d} machine-hours; after 2 hours {w * d - 2 * w} are left for {w - e} machines: {round((w * d - 2 * w) / (w - e), 1)} hours." if d > 2 and w > e else "", o="O2", d="VH") if d > 2 and w > e else None)(r.randint(4, 10), r.randint(3, 12), r.randint(1, 3)))

U.mindmap(("Ratios", "Simplify by the HCF • total parts • value of one part", "O1", "11.1"), ("Proportion", "Direct: y ÷ x constant • inverse: x × y constant • unitary method", "O2", "11.2"))
