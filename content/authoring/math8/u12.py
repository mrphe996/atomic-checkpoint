# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 12 Ratio and proportion (12.1 Simplifying ratios, 12.2 Sharing in a ratio,
12.3 Ratio and direct proportion). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from math import gcd
from kit import *

U = Unit(12, "Ratio and Proportion", "Number",
         "Simplifying ratios (including different units), sharing an amount in a given ratio, and solving direct proportion problems.",
         {"O1": {"code": "8Nf.13", "sec": "12.1", "codeNote": "", "t": "Simplify ratios, including ratios with different units and three-part ratios."},
          "O2": {"code": "8Nf.14", "sec": "12.2", "codeNote": "", "t": "Share an amount in a given ratio and solve problems involving ratio."},
          "O3": {"code": "8Nf.15", "sec": "12.3", "codeNote": "", "t": "Use ratio and the unitary method to solve direct proportion problems, including best buys."}})


def simp(*v):
    g = 0
    for x in v: g = gcd(g, x)
    return [x // g for x in v]


R = lambda v: " : ".join(map(str, v))
ACC = lambda v: [R(v), ":".join(map(str, v)), " :".join(map(str, v)), ": ".join(map(str, v))]

# ================================================================== 12.1
s = U.section("12.1", "Simplifying ratios", ["O1"])
s.idea("Simplest form", ["A **ratio** compares quantities. Simplify it by dividing every part by their **highest common factor**: 24 : 36 = 2 : 3 (÷ 12).",
       "Write both parts in the **same units** first: 40 cm : 2 m = 40 : 200 = 1 : 5."])
s.check(S("Write 45 : 60 in its simplest form.", ACC([3, 4]), o="O1"))
s.example("Three parts", "Simplify 12 : 18 : 30.", [("HCF of 12, 18 and 30 is 6", ""), ("÷ 6", "")], "2 : 3 : 5")
s.check(MC("Before you read on: simplify 1.5 : 2.5.", "3 : 5", [("1 : 2", "Multiply both by 2 to clear the decimals: 3 : 5."), ("15 : 25", "Correct value, but not simplest form.")], o="O1"))
s.mistake("Same units", ["500 g : 2 kg is NOT 500 : 2. Change 2 kg to 2000 g: 500 : 2000 = 1 : 4."])


def r1(r):
    a, b = r.randint(1, 9), r.randint(1, 9); k = r.randint(2, 12)
    if a == b: return None
    v = simp(a, b)
    return S(f"Write {a * k} : {b * k} in its simplest form.", ACC(v), o="O1", reason=f"Divide by {gcd(a * k, b * k)}: {R(v)}.")
def r2(r):
    a, b, c = r.randint(1, 7), r.randint(1, 7), r.randint(1, 7); k = r.randint(2, 8)
    v = simp(a, b, c)
    return S(f"Write {a * k} : {b * k} : {c * k} in its simplest form.", ACC(v), o="O1", d="H")
def r3(r):
    u = pick(r, [("cm", "m", 100), ("g", "kg", 1000), ("minutes", "hours", 60), ("ml", "litres", 1000)])
    a = r.randint(1, 9) * pick(r, [5, 10, 20, 25]); b = r.randint(1, 4)
    v = simp(a, b * u[2])
    return S(f"Write {a} {u[0]} : {b} {u[1]} in its simplest form.", ACC(v), o="O1", d="H", reason=f"{b} {u[1]} = {b * u[2]} {u[0]}; {a} : {b * u[2]} = {R(v)}.")
def r4(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    if a == b: return None
    return N(f"Write {a} : {b} in the form 1 : n. Give n to 2 d.p. if needed.", round(b / a, 2), o="O1", tol=0.006, reason=f"Divide both by {a}: 1 : {fmt(round(b / a, 2))}.")
def r5(r):
    rows = [("6 : 9", "2 : 3"), ("10 : 25", "2 : 5"), ("14 : 21", "2 : 3"), ("12 : 16", "3 : 4"), ("20 : 50", "2 : 5"), ("9 : 12", "3 : 4")]
    return GD("Write each ratio in its simplest form.", "Simplest form", r.sample(rows, 4), o="O1", extra=["1 : 2"])
def r6(r):
    b, g = r.randint(5, 20), r.randint(5, 20)
    v = simp(b, g)
    return S("Write the ratio boys : girls in its simplest form.", ACC(v), o="O1", data={"head": ["", "Boys", "Girls"], "rows": [["Number", str(b), str(g)]]})
def r7(r):
    a, b = r.randint(2, 5), r.randint(2, 5); k = r.randint(2, 6)
    if a == b: return None
    return MC(f"Which ratio is equivalent to {a} : {b}?", R([a * k, b * k]), [R([a + k, b + k]), R([b * k, a * k]), R([a * k, b])], o="O1")
def r8(r):
    a, b = r.randint(2, 9), r.randint(2, 9); x = r.randint(2, 12)
    return N(f"The ratio of red to blue counters is {a} : {b}. There are {a * x} red counters. How many blue counters are there?", b * x, "counters", units=["counters"], o="O1", reason=f"{a * x} ÷ {a} = {x}; {b} × {x} = {b * x}.")


def h121(r):
    a, b = pick(r, [(0.4, 1.2), (2.5, 1.5), (0.6, 0.9)])
    from math import gcd
    A, B_ = round(a * 10), round(b * 10); g = gcd(A, B_)
    return MC(f"Write {a} : {b} in its simplest form with whole numbers.", f"{A // g} : {B_ // g}", [(f"{A} : {B_}", "Simplify further: divide by the common factor."), (f"{B_ // g} : {A // g}", "Keep the order.")], o="O1", d="H", reason=f"× 10: {A} : {B_}; ÷ {g}: {A // g} : {B_ // g}.")


s.std([r5, r6, r1, r2, r3, r4, r7, r8], EX("Explain why 2 m : 50 cm is 4 : 1, not 2 : 50.", [("change to the same units: 2 m = 200 cm", ["200|same unit"]), ("200 : 50 = 4 : 1", ["200 ?: ?50|÷ ?50|4 ?: ?1"])], "The parts must be in the same units: 2 m = 200 cm. Then 200 : 50 = 4 : 1 (divide by 50).", o="O1"),
      deep=[h121])

# ================================================================== 12.2
s = U.section("12.2", "Sharing in a ratio", ["O2"])
s.idea("Sharing", ["To share an amount in a ratio: **add the parts**, find the value of **one part**, then multiply.",
       "Share $60 in the ratio 2 : 3: 5 parts; one part = 60 ÷ 5 = 12; shares $24 and $36."])
s.example("Three people", "Share 180 g in the ratio 1 : 3 : 5.", [("1 + 3 + 5 = 9 parts", ""), ("one part = 180 ÷ 9 = 20 g", ""), ("20 g, 60 g, 100 g", "")], "20 g, 60 g, 100 g")
s.check(N("Share $45 in the ratio 4 : 5. How much is the larger share?", 25, "$", units=["$"], o="O2"))
s.check(MC("Before you read on: $60 is shared 2 : 3 : 5. What is the smallest share?", "$12", [("$20", "There are 10 parts, so one part is $6."), ("$2", "One part is $6; the smallest share is 2 parts.")], o="O2"))
s.mistake("Add the parts", ["For 2 : 3, divide by 5 (the total number of parts), not by 2 or 3."])
NM = ["Ana", "Ben", "Cai", "Dee", "Eva", "Fin"]


def h1(r):
    a, b = r.randint(1, 9), r.randint(1, 9); k = r.randint(3, 20); t = (a + b) * k; n = r.sample(NM, 2)
    return N(f"{n[0]} and {n[1]} share ${t} in the ratio {a} : {b}. How much does {n[1]} get?", b * k, "$", units=["$"], o="O2", reason=f"{a + b} parts; one part = {k}; {n[1]} gets {b} × {k} = {b * k}.")
def h2(r):
    a, b, c = r.randint(1, 6), r.randint(1, 6), r.randint(1, 6); k = r.randint(5, 30); t = (a + b + c) * k
    return TB(f"Share {t} g of sweets in the ratio {a} : {b} : {c}.", ["Person", "Share (g)"], [["First", B(a * k)], ["Second", B(b * k)], ["Third", B(c * k)]], o="O2")
def h3(r):
    a, b = r.randint(1, 7), r.randint(2, 9); k = r.randint(3, 15)
    if a == b: return None
    return N(f"A rope is cut in the ratio {a} : {b}. The longer piece is {max(a, b) * k} cm. How long was the rope?", (a + b) * k, "cm", units=["cm"], o="O2", d="H", reason=f"One part = {k} cm; total {a + b} parts = {(a + b) * k} cm.")
def h4(r):
    a, b = r.randint(1, 6), r.randint(2, 9); k = r.randint(3, 15)
    if a >= b: return None
    return N(f"Money is shared in the ratio {a} : {b}. The second person gets ${(b - a) * k} more than the first. How much was shared?", (a + b) * k, "$", units=["$"], o="O2", d="VH", reason=f"{b - a} parts = {(b - a) * k}, one part = {k}; total = {(a + b) * k}.")
def h5(r):
    a, b = r.randint(1, 5), r.randint(1, 5); k = r.randint(4, 20)
    return N(f"In a class the ratio of boys to girls is {a} : {b}. There are {(a + b) * k} students. How many girls are there?", b * k, "girls", units=["girls"], o="O2", reason=f"One part = {k}; girls = {b * k}.")
def h6(r):
    a, b = r.randint(1, 5), r.randint(1, 5); t = (a + b) * r.randint(5, 20)
    return MC(f"$({t}) is shared in the ratio {a} : {b}. What is the first step?".replace(f"$({t})", f"${t}"), f"add the parts: {a} + {b} = {a + b}", [f"divide {t} by {a}", f"divide {t} by {b}", f"multiply {t} by {a + b}"], o="O2")
def h7(r):
    a, b = r.randint(2, 5), r.randint(1, 4); k = r.randint(50, 150)
    return N(f"Concrete is mixed as sand : cement = {a} : {b}. How much cement is in {(a + b) * k} kg of concrete?", b * k, "kg", units=["kg"], o="O2", reason=f"{(a + b) * k} ÷ {a + b} × {b} = {b * k} kg.", data={"head": ["Ingredient", "Sand", "Cement"], "rows": [["Parts", str(a), str(b)]]})
def h8(r):
    a, b, c = r.randint(2, 5), r.randint(2, 5), r.randint(2, 5); k = r.randint(5, 25)
    return N(f"Angles of a triangle are in the ratio {a} : {b} : {c}. Find the largest angle (1 d.p. if needed).", round(180 / (a + b + c) * max(a, b, c), 1), "°", units=["°"], o="O2", d="H", tol=0.05, reason=f"180 ÷ {a + b + c} × {max(a, b, c)} ≈ {round(180 / (a + b + c) * max(a, b, c), 1)}°.")


def h122(r):
    a, b, c = r.sample(range(1, 6), 3); p = r.randint(2, 9)
    return N(f"Money is shared in the ratio {a} : {b} : {c}. The biggest share is ${max(a, b, c) * p}. How much was shared?", (a + b + c) * p, "$", units=["$"], o="O2", d="H",
             reason=f"{max(a, b, c)} parts = {max(a, b, c) * p}, so 1 part = {p}; total = {a + b + c} × {p} = {(a + b + c) * p}.")


s.std([h2, h7, h1, h3, h5, h6, h4, h8], EX("Explain how to share $56 in the ratio 3 : 4.", [("3 + 4 = 7 parts, one part = 56 ÷ 7 = 8", ["7 parts|÷ ?7|= ?8|one part"]), ("shares 3 × 8 = 24 and 4 × 8 = 32", ["24|32"])], "Add the parts: 3 + 4 = 7. One part is 56 ÷ 7 = $8. The shares are 3 × 8 = $24 and 4 × 8 = $32.", o="O2"),
      deep=[h122])

# ================================================================== 12.3
s = U.section("12.3", "Ratio and direct proportion", ["O3"])
s.idea("Unitary method", ["Two quantities are in **direct proportion** if they increase at the same rate: double one, and the other doubles.",
       "**Unitary method**: find the value of ONE first, then multiply. 5 pens cost $8, so 1 pen costs $1.60 and 7 pens cost $11.20."])
s.example("Best buy", "Which is better value: 300 g for $2.40 or 500 g for $3.75?", [("$2.40 ÷ 300 = 0.8 cents per g", ""), ("$3.75 ÷ 500 = 0.75 cents per g", "")], "500 g for $3.75")
s.check(N("4 tickets cost $26. How much do 6 tickets cost?", 39, "$", units=["$"], o="O3"))
s.idea("Ratio and proportion are the same idea", ["If a recipe uses flour and sugar in the ratio 3 : 1, then flour is always 3 times the sugar: the amounts are in direct proportion.",
       "Use the ratio to scale: 450 g of flour needs 150 g of sugar."])
s.mistake("Same rate", ["Add the SAME multiplier to both quantities: 3 → 9 is × 3, so 4 → 12, not 4 + 6."])


def d1(r):
    n, p, m = r.randint(2, 9), r.randint(2, 15), r.randint(2, 15)
    if n == m: return None
    it = pick(r, ["notebooks", "pens", "apples", "cinema tickets", "bus fares"])
    return N(f"{n} {it} cost ${fmt(n * p * 0.5)}. How much do {m} {it} cost?", m * p * 0.5, "$", units=["$"], o="O3", reason=f"1 costs ${fmt(p * 0.5)}; {m} cost ${fmt(m * p * 0.5)}.")
def d2(r):
    s_, g = r.randint(2, 6), r.randint(100, 300); n = r.randint(3, 10)
    return N(f"A recipe for {s_} people uses {g} g of rice. How much rice is needed for {n} people? (1 d.p. if needed)", round(g / s_ * n, 1), "g", units=["g"], o="O3", tol=0.05, reason=f"{g} ÷ {s_} × {n} ≈ {round(g / s_ * n, 1)} g.")
def d3(r):
    a, pa = r.randint(2, 6) * 100, r.randint(150, 500) / 100; b = a + r.randint(1, 4) * 100; pb = round(pa / a * b * pick(r, [0.9, 1.1]), 2)
    best = "small" if pa / a < pb / b else "large"
    return MC(f"Which is better value: a small pack of {a} g for ${pa:.2f}, or a large pack of {b} g for ${pb:.2f}?", f"the {best} pack", [(f"the {'large' if best == 'small' else 'small'} pack", "Compare the price per gram."), ("they are the same value", "")], o="O3", d="H", data={"head": ["Pack", "Small", "Large"], "rows": [["Mass", f"{a} g", f"{b} g"], ["Price", f"${pa:.2f}", f"${pb:.2f}"]]})
def d4(r):
    rate = r.randint(8, 25); h = r.randint(3, 40)
    return TB(f"A worker is paid ${rate} per hour. Complete the table.", ["Hours", "Pay ($)"], [["1", str(rate)], [str(h), B(rate * h)], ["40", B(rate * 40)]], o="O3")
def d5(r):
    rows = [("Cost of petrol and litres bought", "Yes"), ("Age and height of a person", "No"), ("Number of tickets and total cost", "Yes"), ("Speed and time for a fixed journey", "No"), ("Length of a fence and number of equal panels", "Yes")]
    return GD("Are the two quantities in direct proportion?", "Direct proportion?", r.sample(rows, 4), o="O3")
def d6(r):
    km, l = r.randint(150, 500), r.randint(10, 40); x = r.randint(50, 600)
    return N(f"A car uses {l} litres of fuel to travel {km} km. How much fuel does it use for {x} km? Give your answer to 1 d.p.", round(l / km * x, 1), "litres", units=["litres", "l"], o="O3", d="H", tol=0.05)
def d7(r):
    k = pick(r, [1.2, 1.5, 0.8, 1.25]); a = r.randint(20, 200)
    return N(f"$1 = €{fmt(k)}. Change ${a} into euros.", round(a * k, 2), "€", units=["€", "euros"], o="O3", tol=0.005, reason=f"{a} × {fmt(k)} = {fmt(round(a * k, 2))}.")
def d8(r):
    x, y = r.randint(2, 8), r.randint(3, 12); a = r.randint(2, 9) * x
    return N(f"y is directly proportional to x. When x = {x}, y = {y}. Find y when x = {a}.", y * a / x, o="O3", d="H", reason=f"y = {fmt(y / x)}x → {fmt(y * a / x)}.")


def h123(r):
    a, b = r.sample(range(2, 7), 2); k = r.randint(20, 60) * 5
    return N(f"Cement and sand are mixed in the ratio {a} : {b}. How much sand is needed with {a * k} kg of cement?", b * k, "kg", units=["kg"], o="O3", d="H", reason=f"{a} parts = {a * k} kg, so 1 part = {k} kg; sand = {b} × {k} = {b * k} kg.")


s.std([d3, d4, d1, d2, d5, d7, d6, d8], EX("Explain how to find which is better value: 6 eggs for $1.80 or 10 eggs for $2.80.", [("find the price of one egg for each", ["one egg|each egg|per egg|unit|÷ ?6|÷ ?10"]), ("30 cents vs 28 cents, so 10 eggs is better value", ["30|28|10 eggs"])], "Work out the cost of one egg: $1.80 ÷ 6 = 30 cents and $2.80 ÷ 10 = 28 cents. The 10 eggs are better value.", o="O3"),
      deep=[h123])

U.mindmap(("Simplifying", "Divide by the HCF • same units first", "O1", "12.1"), ("Sharing", "Add the parts • one part • multiply", "O2", "12.2"),
          ("Direct proportion", "Unitary method • best buys", "O3", "12.3"))
