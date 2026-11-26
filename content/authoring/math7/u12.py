# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 12 Ratio and proportion (12.1 Simplifying ratios, 12.2 Sharing in a ratio, 12.3 Using direct
proportion). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from math import gcd
from kit import *

U = Unit(12, "Ratio and Proportion", "Number",
         "Writing and simplifying ratios, sharing amounts in a ratio, and solving direct proportion problems such as recipes and best buys.",
         {"O1": {"code": "7Nf.13", "sec": "12.1", "codeNote": "", "t": "Write and simplify ratios, including ratios of three quantities."},
          "O2": {"code": "7Nf.14", "sec": "12.2", "codeNote": "", "t": "Share an amount in a given ratio."},
          "O3": {"code": "7Nf.15", "sec": "12.3", "codeNote": "", "t": "Use direct proportion to solve problems, such as scaling recipes and comparing prices."}})
R = lambda v: " : ".join(map(str, v))
ACC = lambda v: [R(v), ":".join(map(str, v)), " :".join(map(str, v)), ": ".join(map(str, v))]


def simp(*v):
    g = 0
    for x in v: g = gcd(g, x)
    return [x // g for x in v]


# ================================================================== 12.1
s = U.section("12.1", "Simplifying ratios", ["O1"])
s.idea("Ratio", ["A **ratio** compares amounts. If there are 6 red and 9 blue beads, red : blue = 6 : 9.",
       "**Simplify** by dividing every part by the same number: 6 : 9 = 2 : 3. A ratio is in its simplest form when the parts have no common factor."])
s.check(S("Simplify 12 : 16.", ACC([3, 4]), o="O1"))
s.idea("Why we can divide both parts", ["A ratio compares amounts. 6 : 4 means for every 6 red there are 4 blue. Grouping them in 2s gives 3 groups of red for every 2 groups of blue: 3 : 2.",
       "Dividing both parts by the same number keeps the comparison the same, just like an equivalent fraction."])
s.check(MC("Before you read on: is 4 : 6 the same as 6 : 4?", "No", [("Yes", "The order matters: 4 red to 6 blue is not 6 red to 4 blue."), ("Only if simplified", "2 : 3 and 3 : 2 are still different.")], o="O1"))
s.mistake("Order matters", ["red : blue = 2 : 3 is not the same as blue : red = 2 : 3."])


def r1(r):
    a, b, k = r.randint(1, 9), r.randint(1, 9), r.randint(2, 10)
    if a == b: return None
    return S(f"Simplify {a * k} : {b * k}.", ACC(simp(a, b)), o="O1")
def r2(r):
    a, b, c, k = r.randint(1, 6), r.randint(1, 6), r.randint(1, 6), r.randint(2, 6)
    return S(f"Simplify {a * k} : {b * k} : {c * k}.", ACC(simp(a, b, c)), o="O1", d="H")
def r3(r):
    c, d = r.randint(2, 15), r.randint(2, 15)
    return S("Write the ratio cats : dogs in its simplest form.", ACC(simp(c, d)), o="O1", data={"head": ["Pet", "Cats", "Dogs"], "rows": [["Number", str(c), str(d)]]})
def r4(r):
    rows = [("4 : 6", "2 : 3"), ("10 : 15", "2 : 3"), ("8 : 12", "2 : 3"), ("5 : 20", "1 : 4"), ("6 : 24", "1 : 4"), ("9 : 12", "3 : 4")]
    return GD("Simplify each ratio.", "Simplest form", r.sample(rows, 4), o="O1", extra=["1 : 2"])
def r5(r):
    a, b = r.randint(2, 6), r.randint(2, 6); k = r.randint(2, 5)
    if a == b: return None
    return MC(f"Which ratio is equivalent to {a} : {b}?", R([a * k, b * k]), [R([a + k, b + k]), R([b, a]), R([a * k, b])], o="O1")
def r6(r):
    b, g = r.randint(5, 20), r.randint(5, 20)
    return S(f"A class has {b} boys and {g} girls. Write the ratio girls : boys in its simplest form.", ACC(simp(g, b)), o="O1")
def r7(r):
    a, b = r.randint(2, 6), r.randint(2, 6); x = r.randint(2, 10)
    return N(f"Juice and water are mixed in the ratio {a} : {b}. How much water is needed for {a * x} ml of juice?", b * x, "ml", units=["ml"], o="O1", d="H")


def q9(r):   # find all equivalent
    a, b = pick(r, [(2, 3), (3, 4), (1, 4), (5, 2)])
    ks = r.sample(range(2, 7), 2)
    good = [f"{a * k} : {b * k}" for k in ks]; bad = [f"{a + k} : {b + k}" for k in r.sample(range(1, 4), 1)] + [f"{b * ks[0]} : {a * ks[0]}"]
    return MS(f"Select ALL the ratios equivalent to {a} : {b}.", good, bad, o="O1", d="H", reason="Multiply BOTH parts by the same number; keep the order.")
def q10(r):   # units decision
    m = r.randint(2, 9) * 10; cm = r.randint(1, 4)
    from math import gcd
    g = gcd(cm * 100, m)
    return X(f"Write the ratio {cm} m : {m} cm in its simplest form.", f"{cm * 100 // g}:{m // g}", o="O1", d="H", vars="", show=f"{cm * 100 // g} : {m // g}",
             reason=f"Use the same units: {cm * 100} cm : {m} cm = {cm * 100 // g} : {m // g}.") if False else MC(f"Write the ratio {cm} m : {m} cm in its simplest form.", f"{cm * 100 // g} : {m // g}",
             [(f"{cm // gcd(cm, m)} : {m // gcd(cm, m)}", "Change to the same units first."), (f"{m // g} : {cm * 100 // g}", "Keep the order.")], o="O1", d="H", reason=f"Use the same units: {cm * 100} cm : {m} cm = {cm * 100 // g} : {m // g}.")


s.std([r3, r4, r1, r2, r5, r6, r7], EX("Explain how to simplify 15 : 25.", [("find the highest common factor, 5", ["5|common factor|HCF"]), ("divide both parts by 5: 3 : 5", ["3 ?: ?5"])], "The highest common factor of 15 and 25 is 5. Divide both parts by 5 to get 3 : 5.", o="O1"),
      deep=[q9, q10])

# ================================================================== 12.2
s = U.section("12.2", "Sharing in a ratio", ["O2"])
s.idea("Parts", ["To share $40 in the ratio 3 : 5: add the parts (3 + 5 = 8), find one part (40 ÷ 8 = 5), then multiply: $15 and $25.",
       "Check: the shares add up to the total."])
s.check(N("Share 30 sweets in the ratio 1 : 2. How many are in the bigger share?", 20, "sweets", units=["sweets"], o="O2"))
s.idea("Why we add the parts", ["Share 30 in the ratio 2 : 3. Think of 2 + 3 = 5 equal parts. Each part is 30 ÷ 5 = 6, so the shares are 2 × 6 = 12 and 3 × 6 = 18.",
       "Check: 12 + 18 = 30, and 12 : 18 = 2 : 3."])
s.check(MC("Before you read on: £20 is shared 1 : 3. How many equal parts are there?", "4", [("3", "Add the parts: 1 + 3."), ("2", "There are two people, but 4 parts.")], o="O2"))
s.mistake("Divide by the total parts", ["For 3 : 5 divide by 8, not by 3 or 5."])
NM = ["Amy", "Ben", "Chi", "Dev", "Ela"]


def h1(r):
    a, b, k = r.randint(1, 7), r.randint(1, 7), r.randint(2, 15); n = r.sample(NM, 2)
    return N(f"{n[0]} and {n[1]} share ${(a + b) * k} in the ratio {a} : {b}. How much does {n[0]} get?", a * k, "$", units=["$"], o="O2")
def h2(r):
    a, b, c, k = r.randint(1, 5), r.randint(1, 5), r.randint(1, 5), r.randint(2, 10)
    return TB(f"Share {(a + b + c) * k} stickers in the ratio {a} : {b} : {c}.", ["Person", "Stickers"], [["First", B(a * k)], ["Second", B(b * k)], ["Third", B(c * k)]], o="O2", d="H")
def h3(r):
    a, b, k = r.randint(1, 5), r.randint(1, 5), r.randint(3, 12)
    return N(f"A class has boys and girls in the ratio {a} : {b}. There are {(a + b) * k} students. How many girls are there?", b * k, "girls", units=["girls"], o="O2")
def h4(r):
    a, b, k = r.randint(1, 5), r.randint(2, 6), r.randint(2, 10)
    return N(f"Paint is mixed red : white in the ratio {a} : {b}. A tin holds {(a + b) * k} litres. How much is white?", b * k, "litres", units=["litres", "l"], o="O2", data={"head": ["Colour", "Red", "White"], "rows": [["Parts", str(a), str(b)]]})
def h5(r):
    a, b = r.randint(1, 5), r.randint(1, 5); t = (a + b) * r.randint(2, 10)
    return MC(f"${t} is shared in the ratio {a} : {b}. What is the value of one part?", f"${t // (a + b)}", [f"${t // a if t % a == 0 else t - a}", f"${t - (a + b)}", f"${t * (a + b)}"], o="O2")
def h6(r):
    a, b, k = r.randint(1, 4), r.randint(5, 8), r.randint(2, 9)
    return N(f"Two numbers are in the ratio {a} : {b}. The bigger number is {b * k}. What is the smaller number?", a * k, o="O2", d="H")
def h7(r):
    a, b, k = r.randint(1, 4), r.randint(2, 6), r.randint(3, 10)
    if a >= b: return None
    return N(f"Prizes are shared in the ratio {a} : {b}. The second person gets ${(b - a) * k} more than the first. How much was shared altogether?", (a + b) * k, "$", units=["$"], o="O2", d="VH")


def h9(r):   # work backwards from one share
    a, b = r.sample(range(1, 6), 2); p = r.randint(2, 9)
    return N(f"Money is shared in the ratio {a} : {b}. The first person gets ${a * p}. How much was shared altogether?", (a + b) * p, "$", units=["$"], o="O2", d="H",
             reason=f"{a} parts = {a * p}, so 1 part = {p}; total {a + b} parts = {(a + b) * p}.")
def h10(r):   # difference given
    a, b = sorted(r.sample(range(1, 8), 2)); p = r.randint(3, 9)
    return N(f"Two numbers are in the ratio {a} : {b}. Their difference is {(b - a) * p}. What is the smaller number?", a * p, o="O2", d="VH", reason=f"The difference is {b - a} parts = {(b - a) * p}, so 1 part = {p}; the smaller number is {a} × {p} = {a * p}.")
def h11(r):   # spot the error
    t = pick(r, [30, 40, 60]); 
    return MC(f"Leo shares {t} in the ratio 1 : 2 and says the shares are {t // 2} and {t}. What is wrong?", f"He divided by 2 instead of by 3: the shares are {t // 3} and {2 * t // 3}", [("Nothing", f"{t // 2} + {t} is more than {t}."), (f"The shares are {t // 2} and {t // 2}", "That is the ratio 1 : 1.")], o="O2", d="H",
              reason=f"1 + 2 = 3 parts; 1 part = {t // 3}.") if t % 3 == 0 else None


s.std([h2, h4, h1, h3, h5, h6, h7], EX("Explain how to share 35 marbles in the ratio 2 : 5.", [("2 + 5 = 7 parts; one part = 35 ÷ 7 = 5", ["7 parts|÷ ?7|one part|= ?5"]), ("2 × 5 = 10 and 5 × 5 = 25", ["10|25"])], "Add the parts: 2 + 5 = 7. One part is 35 ÷ 7 = 5. The shares are 2 × 5 = 10 and 5 × 5 = 25.", o="O2"),
      deep=[h9, h10, h11])

# ================================================================== 12.3
s = U.section("12.3", "Using direct proportion", ["O3"])
s.idea("Unitary method", ["Two amounts are in **direct proportion** if, when one doubles, the other doubles.",
       "Find the value of **one** first: 4 bananas cost $2, so 1 costs $0.50, so 7 cost $3.50."])
s.check(N("3 pens cost $6. How much do 5 pens cost?", 10, "$", units=["$"], o="O3"))
s.idea("Why the unitary method works", ["In direct proportion, doubling one amount doubles the other. So first find the value for ONE, then multiply.",
       "5 pens cost $4. One pen costs 4 ÷ 5 = $0.80, so 8 pens cost 8 × 0.80 = $6.40."])
s.check(MC("Before you read on: 3 bags weigh 12 kg. Is this direct proportion with 6 bags weighing 24 kg?", "Yes", [("No", "Doubling the bags doubles the mass."), ("Only if the bags are full", "We assume every bag is the same.")], o="O3"))
s.mistake("Scale both", ["A recipe for 4 people uses 200 g of flour. For 8 people use 400 g (double), not 204 g."])


def d1(r):
    n, p, m = r.randint(2, 6), r.randint(2, 9), r.randint(2, 12)
    if n == m: return None
    it = pick(r, ["apples", "pencils", "stickers", "rulers"])
    return N(f"{n} {it} cost ${n * p}. How much do {m} {it} cost?", m * p, "$", units=["$"], o="O3")
def d2(r):
    s_, g = pick(r, [2, 4, 5]), r.randint(5, 30) * 10; n = s_ * r.randint(2, 4)
    return N(f"A recipe for {s_} people uses {g} g of rice. How much rice is needed for {n} people?", g * n // s_, "g", units=["g"], o="O3")
def d3(r):
    a, b = r.randint(2, 6), r.randint(7, 12); pa = a * r.randint(20, 60) / 100; pb = round(pa / a * b * pick(r, [0.9, 1.1]), 2)
    best = "A" if pa / a < pb / b else "B"
    return MC(f"Pack A has {a} cans for ${pa:.2f}. Pack B has {b} cans for ${pb:.2f}. Which is better value?", f"Pack {best}", [f"Pack {'B' if best == 'A' else 'A'}", "They are the same"], o="O3", d="H", data={"head": ["Pack", "A", "B"], "rows": [["Cans", str(a), str(b)], ["Price", f"${pa:.2f}", f"${pb:.2f}"]]})
def d4(r):
    rate = r.randint(5, 15)
    return TB(f"A worker earns ${rate} per hour. Complete the table.", ["Hours", "Pay ($)"], [["1", str(rate)], ["4", B(4 * rate)], ["10", B(10 * rate)]], o="O3")
def d5(r):
    rows = [("Number of tickets and total cost", "Yes"), ("Age and height", "No"), ("Litres of petrol and cost", "Yes"), ("Shoe size and test score", "No")]
    return GD("Are the two amounts in direct proportion?", "Direct proportion?", rows, o="O3")
def d6(r):
    km, l = r.randint(2, 6) * 50, r.randint(2, 8) * 5; x = km * r.randint(2, 4)
    return N(f"A car uses {l} litres of fuel to travel {km} km. How much fuel does it use for {x} km?", l * x // km, "litres", units=["litres", "l"], o="O3")
def d7(r):
    n, w = r.randint(2, 8), r.randint(2, 9) * 100
    return N(f"{n} identical boxes have a mass of {n * w} g. What is the mass of 1 box?", w, "g", units=["g"], o="O3")


def d9(r):   # proportional or not
    rows = r.sample([("cost of apples at a fixed price per kg", "Proportional"), ("a person's height and their age", "Not proportional"), ("distance travelled at a steady speed and time", "Proportional"),
                     ("a taxi fare with a fixed starting charge and the distance", "Not proportional"), ("number of tickets and total cost at a fixed price", "Proportional")], 4)
    return GD("Is each pair of quantities in direct proportion?", "Proportional?", rows, o="O3", d="H", extra=["Proportional", "Not proportional"],
              reason="Direct proportion: zero of one gives zero of the other, and doubling one doubles the other. A fixed charge breaks this.")
def d10(r):   # best buy
    a, pa = pick(r, [(4, 3.2), (6, 4.5), (5, 3.5)]); b, pb = pick(r, [(10, 7.0), (12, 8.4), (8, 6.0)])
    ua, ub = pa / a, pb / b
    if abs(ua - ub) < 1e-9: return None
    return MC(f"Pack A: {a} cans for ${pa:.2f}. Pack B: {b} cans for ${pb:.2f}. Which is better value?", "Pack A" if ua < ub else "Pack B", [("Pack B" if ua < ub else "Pack A", f"Find the price of one can in each pack: ${ua:.3f} and ${ub:.3f}.")], o="O3", d="H",
              reason=f"A: ${ua:.3f} per can; B: ${ub:.3f} per can.")


s.std([d3, d4, d1, d2, d5, d6, d7], EX("Explain how to find the cost of 9 notebooks if 3 notebooks cost $4.50.", [("find the cost of one: 4.50 ÷ 3 = $1.50 (or 9 is 3 times 3)", ["one|÷ ?3|1\\.5|three times|× ?3"]), ("9 notebooks cost $13.50", ["13\\.5"])], "Find the cost of one notebook: $4.50 ÷ 3 = $1.50. Then 9 notebooks cost 9 × $1.50 = $13.50.", o="O3"),
      deep=[d9, d10])

U.mindmap(("Simplifying", "Divide by a common factor • order matters", "O1", "12.1"), ("Sharing", "Add the parts • one part • multiply", "O2", "12.2"),
          ("Direct proportion", "Find one first • recipes • best buys", "O3", "12.3"))
