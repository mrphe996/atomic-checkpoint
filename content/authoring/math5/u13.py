# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 13 Ratio and proportion (13.1 Ratio, 13.2 Proportion).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(13, "Ratio and Proportion", "Number",
         "Using ratio to compare parts with parts ('for every') and proportion to compare a part with the whole ('in every'), in patterns, recipes and mixtures.",
         {"O1": {"code": "5Nf.07", "sec": "13.1", "codeNote": "", "t": "Understand and use ratio to compare one part with another, using the language 'for every'."},
          "O2": {"code": "5Nf.08", "sec": "13.2", "codeNote": "", "t": "Understand and use proportion to compare a part with the whole, using the language 'in every'."}})

s = U.section("13.1", "Ratio", ["O1"])
s.idea("For every", ["A **ratio** compares one part with another part. In a pattern with **2 red beads for every 3 blue beads**, the ratio of red to blue is **2 : 3**.",
       "If the pattern repeats, both numbers grow together: 4 red for 6 blue, 6 red for 9 blue."], table={"head": ["Red", "2", "4", "6", "8"], "rows": [["Blue", "3", "6", "9", "12"]]})
s.check(N("A necklace has 3 white beads for every 1 black bead. How many white beads are there if there are 5 black beads?", 15, "beads", units=["beads"], o="O1"))
s.check(MC('Before you read on: for every 1 red bead there are 3 blue beads. With 4 red beads, how many blue?', '12', [('6', 'Multiply: 4 groups of 3.'), ('7', 'Ratio is about multiplying, not adding.')], o='O1'))
s.mistake("Not adding", ["2 red for every 3 blue: with 4 red there are 6 blue (double), not 5."])


def r1(r):
    a, b, k = r.randint(1, 5), r.randint(1, 5), r.randint(2, 6)
    if a == b: return None
    return N(f"A pattern has {a} stars for every {b} moons. How many moons are there when there are {a * k} stars?", b * k, "moons", units=["moons"], o="O1")
def r2(r):
    a, b = r.randint(1, 4), r.randint(1, 4)
    return TB(f"There are {a} cats for every {b} dogs. Complete the table.", ["Cats", "Dogs"], [[str(a * k), B(b * k)] for k in (2, 3, 5)], o="O1")
def r3(r):
    a, b = r.randint(1, 6), r.randint(1, 6)
    if a == b: return None
    return S(f"A fruit bowl has {a} apples and {b} bananas. Write the ratio of apples to bananas.", [f"{a} : {b}", f"{a}:{b}"], o="O1", data={"head": ["Fruit", "Apples", "Bananas"], "rows": [["Number", str(a), str(b)]]})
def r4(r):
    a, b, k = r.randint(1, 3), r.randint(2, 5), r.randint(2, 6)
    return N(f"Squash is made with {a} cup of juice for every {b} cups of water. How many cups of water are needed with {a * k} cups of juice?", b * k, "cups", units=["cups"], o="O1")
def r5(r):
    a, b = r.randint(2, 6), r.randint(2, 6)
    if a == b: return None
    return MC(f"In a class there are {a} girls for every {b} boys. What is the ratio of boys to girls?", f"{b} : {a}", [f"{a} : {b}", f"{b} : {a + b}"], o="O1")
def r6(r):
    a, b, k = r.randint(1, 4), r.randint(1, 4), r.randint(2, 5)
    return N(f"A tile pattern has {a} red tiles for every {b} white tiles. The pattern uses {(a + b) * k} tiles altogether. How many are red?", a * k, "tiles", units=["tiles"], o="O1", d="H")
def r7(r):
    a, k = r.randint(2, 5), r.randint(2, 6)
    return N(f"For every {a} children on a trip there is 1 adult. How many adults go with {a * k} children?", k, "adults", units=["adults"], o="O1")
def r8(r):
    a, b = r.randint(1, 4), r.randint(2, 5)
    return N(f"A recipe uses {a} egg for every {b * 50} g of flour. How many grams of flour go with {a * 4} eggs?", b * 200, "g", units=["g"], o="O1", d="H")


s.std([r2, r3, r1, r4, r5, r7, r6, r8], EX("Explain what '3 red for every 2 blue' means for 9 red counters.", [("9 red is 3 groups of 3", "3 groups|3 lots|9 ?÷ ?3|three times"), ("so there are 3 × 2 = 6 blue", "\\b6\\b")], "For every 3 red there are 2 blue. 9 red is 3 groups of 3, so there are 3 groups of 2 blue: 6 blue counters.", o="O1"))

s = U.section("13.2", "Proportion", ["O2"])
s.idea("In every", ["**Proportion** compares a part with the **whole**. If **2 in every 5** beads are red, the proportion of red beads is 2/5.",
       "In 20 beads, 2 in every 5 are red: 20 ÷ 5 = 4 groups, 4 × 2 = **8** red beads."], fig=PIE(5, [0, 1]))
s.check(N("1 in every 4 children in a class has a bike. There are 24 children. How many have a bike?", 6, "children", units=["children"], o="O2"))
s.check(MC('Before you read on: 2 apples cost 60c. How much do 5 apples cost?', '$1.50', [('$1.20', 'One apple costs 30c.'), ('$3.00', '5 × 30c = 150c.')], o='O2'))
s.mistake("Part or whole?", ["2 red for every 3 blue (ratio) means 2 in every 5 are red (proportion)."])


def p1(r):
    a, b, k = r.randint(1, 4), r.randint(3, 8), r.randint(2, 8)
    if a >= b: return None
    return N(f"{a} in every {b} sweets in a jar are orange. There are {b * k} sweets. How many are orange?", a * k, "sweets", units=["sweets"], o="O2")
def p2(r):
    d = pick(r, [4, 5, 6, 8]); n = r.randint(1, d - 1)
    return S("The circle shows a pattern. What proportion is shaded? Give it as a fraction.", [f"{n}/{d}"], o="O2", fig=PIE(d, range(n)))
def p3(r):
    a, b = r.randint(1, 5), r.randint(1, 5)
    return S(f"A pattern has {a} squares for every {b} circles. What fraction of the shapes are squares?", [f"{a}/{a + b}"], o="O2", d="H")
def p4(r):
    a, b = r.randint(1, 3), r.randint(3, 6)
    if a >= b: return None
    return TB(f"{a} in every {b} cars is red. Complete the table.", ["Cars", "Red cars"], [[str(b * k), B(a * k)] for k in (2, 4, 10)], o="O2")
def p5(r):
    n, p = r.randint(2, 6), r.randint(10, 50)
    return N(f"{n} pens cost {n * p} cents. How much do {n * 3} pens cost, in cents?", 3 * n * p, "cents", units=["cents"], o="O2")
def p6(r):
    a, b, k = r.randint(1, 3), r.randint(4, 7), r.randint(3, 9)
    return N(f"{a} in every {b} days this month were rainy. There were {a * k} rainy days. How many days were there altogether?", b * k, "days", units=["days"], o="O2", d="H")
def p7(r):
    a, b = r.randint(1, 4), r.randint(5, 10)
    return MC(f"{a} in every {b} children wear glasses. Which is true?", f"{b - a} in every {b} do not wear glasses", [f"{a} in every {b - a} do not wear glasses", f"{b} in every {a} wear glasses"], o="O2")
def p8(r):
    s1, s2 = pick(r, [(2, 4), (2, 6), (4, 8), (3, 6)]); q = r.randint(1, 6) * 50
    return N(f"A recipe for {s1} people uses {q} g of rice. How much rice is needed for {s2} people?", q * s2 // s1, "g", units=["g"], o="O2", data={"head": ["People", str(s1), str(s2)], "rows": [["Rice (g)", str(q), "?"]]})


s.std([p2, p8, p1, p4, p5, p7, p3, p6], EX("Explain how to find how many of 30 beads are blue if 1 in every 3 is blue.", [("30 ÷ 3 = 10 groups", "10|30 ?÷ ?3"), ("1 blue in each group, so 10 blue", "10 blue|1 in each|\\b10\\b")], "Split the 30 beads into groups of 3: 30 ÷ 3 = 10 groups. Each group has 1 blue bead, so there are 10 blue beads.", o="O2"))

U.mindmap(("Ratio", "Part to part • 'for every' • 2 : 3", "O1", "13.1"), ("Proportion", "Part to whole • 'in every' • 2/5", "O2", "13.2"))
