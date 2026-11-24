# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 12 Ratio and proportion (12.1 Simplifying ratios, 12.2 Sharing in a ratio, 12.3 Using direct
proportion). Written by the Atomic teaching team."""
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


s.std([r3, r4, r1, r2, r5, r6, r7], EX("Explain how to simplify 15 : 25.", [("find the highest common factor, 5", ["5|common factor|HCF"]), ("divide both parts by 5: 3 : 5", ["3 ?: ?5"])], "The highest common factor of 15 and 25 is 5. Divide both parts by 5 to get 3 : 5.", o="O1"))

# ================================================================== 12.2
s = U.section("12.2", "Sharing in a ratio", ["O2"])
s.idea("Parts", ["To share $40 in the ratio 3 : 5: add the parts (3 + 5 = 8), find one part (40 ÷ 8 = 5), then multiply: $15 and $25.",
       "Check: the shares add up to the total."])
s.check(N("Share 30 sweets in the ratio 1 : 2. How many are in the bigger share?", 20, "sweets", units=["sweets"], o="O2"))
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


s.std([h2, h4, h1, h3, h5, h6, h7], EX("Explain how to share 35 marbles in the ratio 2 : 5.", [("2 + 5 = 7 parts; one part = 35 ÷ 7 = 5", ["7 parts|÷ ?7|one part|= ?5"]), ("2 × 5 = 10 and 5 × 5 = 25", ["10|25"])], "Add the parts: 2 + 5 = 7. One part is 35 ÷ 7 = 5. The shares are 2 × 5 = 10 and 5 × 5 = 25.", o="O2"))

# ================================================================== 12.3
s = U.section("12.3", "Using direct proportion", ["O3"])
s.idea("Unitary method", ["Two amounts are in **direct proportion** if, when one doubles, the other doubles.",
       "Find the value of **one** first: 4 bananas cost $2, so 1 costs $0.50, so 7 cost $3.50."])
s.check(N("3 pens cost $6. How much do 5 pens cost?", 10, "$", units=["$"], o="O3"))
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


s.std([d3, d4, d1, d2, d5, d6, d7], EX("Explain how to find the cost of 9 notebooks if 3 notebooks cost $4.50.", [("find the cost of one: 4.50 ÷ 3 = $1.50 (or 9 is 3 times 3)", ["one|÷ ?3|1\\.5|three times|× ?3"]), ("9 notebooks cost $13.50", ["13\\.5"])], "Find the cost of one notebook: $4.50 ÷ 3 = $1.50. Then 9 notebooks cost 9 × $1.50 = $13.50.", o="O3"))

U.mindmap(("Simplifying", "Divide by a common factor • order matters", "O1", "12.1"), ("Sharing", "Add the parts • one part • multiply", "O2", "12.2"),
          ("Direct proportion", "Find one first • recipes • best buys", "O3", "12.3"))
