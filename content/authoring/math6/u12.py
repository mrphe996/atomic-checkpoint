# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 12 Ratio and proportion (12.1 Ratio, 12.2 Direct proportion).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from math import gcd
from kit import *

U = Unit(12, "Ratio and Proportion", "Number",
         "Using ratio to compare parts with parts, proportion to compare parts with the whole, and solving direct proportion problems.",
         {"O1": {"code": "6Nf.07", "sec": "12.1", "codeNote": "", "t": "Understand ratio as a part-to-part comparison and write and simplify ratios."},
          "O2": {"code": "6Nf.08", "sec": "12.2", "codeNote": "", "t": "Understand direct proportion and use it to solve problems, including recipes and prices."}})
ROW = lambda a, b, ca="R", cb="B": {"head": ["Beads", *([ca] * a + [cb] * b)], "rows": []}

s = U.section("12.1", "Ratio", ["O1"])
s.idea("Ratio compares parts", ["A **ratio** compares one part with another. If there are 3 red beads for every 2 blue beads, the ratio of red to blue is **3 : 2**.",
       "The **proportion** of red beads is 3 out of 5, or 3/5."], table={"head": ["Red", "Blue", "Total"], "rows": [["3", "2", "5"], ["6", "4", "10"]]})
s.check(S("A pattern has 4 squares for every 1 circle. Write the ratio of squares to circles.", ["4 : 1", "4:1"], o="O1"))
s.idea("Simplifying", ["Divide both numbers by a common factor: 6 : 4 = **3 : 2**."])
s.check(MC("Before you read on: for every 2 red beads there are 3 blue beads. If there are 10 red beads, how many are blue?", "15", [("11", "The ratio is about multiplying, not adding."), ("6", "10 red is 5 groups of 2.")], o="O1"))
s.mistake("Order matters", ["'Red to blue' 3 : 2 is not the same as 'blue to red' 2 : 3."])


def r1(r):
    a, b = r.randint(1, 9), r.randint(1, 9)
    if a == b: return None
    return S(f"A bag has {a} red and {b} blue marbles. Write the ratio of red to blue.", [f"{a} : {b}", f"{a}:{b}"], o="O1", data={"head": ["Colour", "Red", "Blue"], "rows": [["Marbles", str(a), str(b)]]})
def r2(r):
    a, b = r.randint(1, 6), r.randint(1, 6); k = r.randint(2, 6); g = gcd(a, b); a, b = a // g, b // g
    if a == b: return None
    return S(f"Write {a * k} : {b * k} in its simplest form.", [f"{a} : {b}", f"{a}:{b}"], o="O1")
def r3(r):
    a, b, k = r.randint(1, 5), r.randint(1, 5), r.randint(2, 8)
    return N(f"Squash is made with {a} cup of juice to {b} cups of water. How much water is needed for {a * k} cups of juice?", b * k, "cups", units=["cups"], o="O1")
def r4(r):
    a, b, k = r.randint(1, 5), r.randint(1, 5), r.randint(2, 8)
    return TB(f"Boys and girls are in the ratio {a} : {b}. Complete the table.", ["Boys", "Girls", "Total"], [[str(a * k), B(b * k), B((a + b) * k)]], o="O1")
def r5(r):
    a, b, k = r.randint(1, 5), r.randint(1, 5), r.randint(2, 6)
    if a == b: return None
    return N(f"Red and green counters are in the ratio {a} : {b}. There are {(a + b) * k} counters. How many are green?", b * k, "counters", units=["counters"], o="O1", d="H")
def r6(r):
    a, b = r.randint(1, 6), r.randint(1, 6)
    return N(f"In a pattern the ratio of stars to moons is {a} : {b}. What fraction of the shapes are stars? Give the numerator when the denominator is {a + b}.", a, o="O1")
def r7(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    if a == b: return None
    return MC(f"A class has {a} boys and {b} girls. Which is the ratio of girls to boys?", f"{b} : {a}", [f"{a} : {b}", f"{b} : {a + b}", f"{a} : {a + b}"], o="O1")
def r8(r):
    a, b, k = r.randint(1, 4), r.randint(1, 4), r.randint(3, 9)
    return N(f"Sand and cement are mixed in the ratio {a} : {b}. Bilal uses {a * k} kg of sand. How much cement does he use?", b * k, "kg", units=["kg"], o="O1", d="H")


s.std([r1, r4, r2, r3, r6, r7, r5, r8], EX("Explain how to simplify the ratio 12 : 18.", [("find a common factor, 6", "6|common factor|HCF"), ("12 ÷ 6 = 2, 18 ÷ 6 = 3, so 2 : 3", "2 ?: ?3")], "Both 12 and 18 divide by 6. 12 ÷ 6 = 2 and 18 ÷ 6 = 3, so 12 : 18 = 2 : 3.", o="O1"))

s = U.section("12.2", "Direct proportion", ["O2"])
s.idea("Direct proportion", ["Two amounts are in **direct proportion** if they go up and down together at the same rate: 1 pen costs 30c, so 4 pens cost 4 × 30 = **120c**.",
       "Use the **unitary method**: find the value of **one**, then multiply."], table={"head": ["Pens", "1", "2", "4", "10"], "rows": [["Cost (c)", "30", "60", "120", "300"]]})
s.check(N("3 apples cost 75 cents. How much do 5 apples cost, in cents?", 125, "cents", units=["cents"], o="O2"))
s.check(MC("Before you read on: 3 pens cost $1.50. How much do 5 pens cost?", "$2.50", [("$3.50", "Find one pen first: $0.50."), ("$2.00", "5 × $0.50 = $2.50.")], o="O2"))
s.mistake("Not adding", ["If 2 tickets cost $10, 4 tickets cost $20 (double), not $12."])
FOOD = [("flour", "g"), ("sugar", "g"), ("milk", "ml"), ("butter", "g")]


def d1(r):
    n, p, m = r.randint(2, 6), r.randint(10, 60), r.randint(3, 12)
    if m == n: return None
    return N(f"{n} pencils cost {n * p} cents. How much do {m} pencils cost, in cents?", m * p, "cents", units=["cents"], o="O2")
def d2(r):
    s1, s2 = pick(r, [(2, 4), (4, 6), (4, 2), (2, 6), (3, 6), (4, 10)])
    ing = r.sample(FOOD, 3); q = [r.randint(1, 6) * 50 for _ in ing]
    k = r.randrange(3)
    return N(f"The recipe is for {s1} people. How much {ing[k][0]} is needed for {s2} people?", q[k] * s2 // s1, ing[k][1], units=[ing[k][1]], o="O2", data={"head": ["Ingredient", *[i[0] for i in ing]], "rows": [[f"For {s1} ({', '.join(i[1] for i in ing)})", *map(str, q)]]})
def d3(r):
    p = r.randint(5, 30)
    return TB(f"One ticket costs ${p}. Complete the table.", ["Tickets", "Cost ($)"], [[str(n), B(n * p)] for n in (2, 5, 10)], o="O2")
def d4(r):
    sp, h = r.randint(40, 90), r.randint(2, 5)
    return N(f"A car travels {sp} km every hour. How far does it go in {h} hours?", sp * h, "km", units=["km"], o="O2")
def d5(r):
    n, p, t = r.randint(3, 8), r.randint(2, 9), r.randint(2, 6)
    return N(f"{n} notebooks cost ${n * p}. How many notebooks can you buy with ${p * n * t}?", n * t, "notebooks", units=["notebooks"], o="O2", d="H")
def d6(r):
    a, b = r.randint(2, 6), r.randint(2, 9)
    return MC(f"Which table shows direct proportion?", f"1 → {b}, 2 → {2 * b}, 3 → {3 * b}", [f"1 → {b}, 2 → {b + 2}, 3 → {b + 3}", f"1 → {b}, 2 → {2 * b + 1}, 3 → {3 * b + 3}", f"1 → {b}, 2 → {b * b}, 3 → {b * b * b}"], o="O2")
def d7(r):
    g, k = r.randint(2, 9) * 100, pick(r, [2, 3, 4, 5])
    return N(f"{k} bags of rice weigh {k * g} g. What do {k + 3} bags weigh?", (k + 3) * g, "g", units=["g"], o="O2", d="H")
def d8(r):
    m = r.randint(2, 8)
    return N(f"A tap fills {m} litres every minute. How many litres does it fill in {m + 4} minutes?", m * (m + 4), "litres", units=["litres", "l"], o="O2")


def l2_1(r):
    n, p, m = r.randint(2, 5), r.randint(2, 9), r.randint(6, 12)
    return N(f"{n} notebooks cost ${n * p}. How much do {m} notebooks cost?", m * p, "$", units=["$"], o="O2", d="H", reason=f"One costs ${p}; {m} cost ${m * p}.")


s.std([d2, d3, d1, d4, d6, d8, d5, d7], EX("Explain how to find the cost of 7 stamps if 4 stamps cost 80 cents.", [("1 stamp costs 80 ÷ 4 = 20 cents", "20|÷ ?4|one stamp"), ("7 stamps cost 7 × 20 = 140 cents", "140")], "Find the cost of one stamp: 80 ÷ 4 = 20 cents. Then 7 stamps cost 7 × 20 = 140 cents.", o="O2"),
      deep=[l2_1])

U.mindmap(("Ratio", "Part : part • simplify by a common factor", "O1", "12.1"), ("Proportion", "Part of the whole • fraction", "O1", "12.1"), ("Direct proportion", "Find one, then multiply • recipes", "O2", "12.2"))
