# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 4 Decimals (4.1 Ordering decimals, 4.2 Adding and subtracting decimals, 4.3 Multiplying
decimals, 4.4 Dividing decimals, 4.5 Making decimal calculations easier). Written by the Atomic teaching team."""
from kit import *

U = Unit(4, "Decimals", "Number",
         "Ordering decimals, adding and subtracting decimals, multiplying and dividing decimals by whole numbers, and mental strategies.",
         {"O1": {"code": "7Nf.01", "sec": "4.1", "codeNote": "", "t": "Compare and order decimals using =, ≠, < and >."},
          "O2": {"code": "7Nf.02", "sec": "4.2", "codeNote": "", "t": "Add and subtract decimals, lining up the decimal points."},
          "O3": {"code": "7Nf.03", "sec": "4.3", "codeNote": "", "t": "Multiply decimals by whole numbers and by decimals."},
          "O4": {"code": "7Nf.04", "sec": "4.4", "codeNote": "", "t": "Divide decimals by whole numbers."},
          "O5": {"code": "7Nf.05", "sec": "4.5", "codeNote": "", "t": "Use place value and the laws of arithmetic to make decimal calculations easier."}})
d1 = lambda r: r.randint(11, 99) / 10
d2 = lambda r: r.randint(101, 999) / 100
R4 = lambda v: round(v, 6)

# ================================================================== 4.1
s = U.section("4.1", "Ordering decimals", ["O1"])
s.idea("Compare place by place", ["Line up the decimal points and compare the digits from the left. Fill gaps with zeros: 0.4 = 0.40 > 0.38.",
       "A decimal with more digits is not always bigger: 0.125 < 0.2."], table={"head": ["Ones", ".", "Tenths", "Hundredths", "Thousandths"], "rows": [["0", ".", "4", "0", "0"], ["0", ".", "3", "8", "0"], ["0", ".", "1", "2", "5"]]})
s.check(CMP("0.7", "0.69", ">", o="O1"))
s.mistake("More digits ≠ bigger", ["2.15 is less than 2.5 because 1 tenth < 5 tenths."])


def o1(r):
    a = d2(r); b = round(a + pick(r, [0.01, 0.1, -0.01, -0.1, 0.05]), 2)
    return CMP(fmt(a), fmt(b), "<" if a < b else ">", o="O1")
def o2(r):
    b = r.randint(1, 9); vs = sorted({round(b + x, 3) for x in (r.randint(1, 9) / 10, r.randint(1, 99) / 100, r.randint(1, 999) / 1000, r.randint(1, 9) / 100)})
    if len(vs) < 4: return None
    return OD("Put these decimals in order, smallest first.", [fmt(v) for v in vs], o="O1")
def o3(r):
    rows = [("3.5 and 3.50", "="), ("0.6 and 0.06", "≠"), ("2.30 and 2.3", "="), ("4.07 and 4.7", "≠"), ("1.10 and 1.1", "=")]
    return GD("Write = or ≠ for each pair.", "Sign", r.sample(rows, 4), o="O1")
def o4(r):
    nm = r.sample(["Asha", "Ben", "Cleo", "Dan", "Eve"], 4); t = [round(r.uniform(11, 14), 2) for _ in range(4)]
    w = nm[t.index(min(t))]
    return MC("These are times in seconds for a race. Who won?", w, [n for n in nm if n != w], o="O1", data={"head": ["Runner", *nm], "rows": [["Time (s)", *[f"{x:.2f}" for x in t]]]})
def o5(r):
    a = d2(r)
    return MS(f"Select ALL the numbers bigger than {fmt(a)}.", [fmt(round(a + 0.01, 2)), fmt(round(a + 0.1, 2))], [fmt(round(a - 0.01, 2)), fmt(round(a - 0.1, 2))], o="O1")
def o6(r):
    a = r.randint(1, 9) + r.randint(1, 8) / 10
    return N(f"Write a number with 2 decimal places that is halfway between {fmt(a)} and {fmt(round(a + 0.1, 1))}.", round(a + 0.05, 2), o="O1", d="H")
def o7(r):
    a, b = d2(r), d2(r)
    if a == b: return None
    return N(f"What is the difference between {fmt(a)} and {fmt(b)}?", R4(abs(a - b)), o="O1")


s.std([o3, o4, o1, o2, o5, o6, o7], EX("Explain why 0.3 is bigger than 0.25.", [("write 0.3 as 0.30", ["0\\.30|zero|same number"]), ("30 hundredths > 25 hundredths (3 tenths > 2 tenths)", ["30|tenths|3 ?> ?2"])], "0.3 = 0.30. Comparing the tenths, 3 tenths is more than 2 tenths, so 0.30 > 0.25.", o="O1"))

# ================================================================== 4.2
s = U.section("4.2", "Adding and subtracting decimals", ["O2"])
s.idea("Line up the points", ["Write the numbers in columns with the **decimal points lined up**. Fill empty places with zeros, then add or subtract as with whole numbers.",
       "12.5 − 3.68: write 12.50 − 3.68 = 8.82."])
s.check(N("Work out 4.75 + 2.6.", 7.35, o="O2"))
s.mistake("Line up the points, not the digits", ["4.75 + 2.6 is not 5.01: the 6 is in the tenths column."])


def a1(r):
    a, b = d2(r), d1(r)
    return N(f"Work out {fmt(a)} + {fmt(b)}.", R4(a + b), o="O2")
def a2(r):
    a, b = d1(r) + 10, d2(r)
    return N(f"Work out {fmt(a)} − {fmt(b)}.", R4(a - b), o="O2")
def a3(r):
    p = [d2(r) for _ in range(3)]
    return N(f"Mia buys items costing ${p[0]:.2f}, ${p[1]:.2f} and ${p[2]:.2f}. What is the total?", R4(sum(p)), "$", units=["$"], o="O2")
def a4(r):
    p = d2(r)
    return N(f"A book costs ${p:.2f}. How much change from $20?", R4(20 - p), "$", units=["$"], o="O2")
def a5(r):
    a, b = d1(r), d1(r)
    return N(f"A plank is {fmt(a + b)} m long. A piece of {fmt(a)} m is cut off. How long is the rest?", R4(b), "m", units=["m"], o="O2")
def a6(r):
    a, b, c = d2(r), d1(r), d2(r)
    return TB("Complete the table.", ["Calculation", "Answer"], [[f"{fmt(a)} + {fmt(b)}", B(R4(a + b))], [f"{fmt(a + 10)} − {fmt(c)}", B(R4(a + 10 - c))]], o="O2")
def a7(r):
    l, w = d1(r), d1(r)
    return N("Find the perimeter of the rectangle.", R4(2 * (l + w)), "m", units=["m"], o="O2", fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 4], [0, 4]], "s": [f"{fmt(l)} m", f"{fmt(w)} m", "", ""]})
def a8(r):
    a, b = d2(r), d2(r)
    return N(f"Find the missing number: {fmt(a)} + ☐ = {fmt(R4(a + b))}", b, o="O2", d="H")


s.std([a6, a7, a1, a2, a3, a4, a5, a8], EX("Explain the mistake in 5.4 + 2.35 = 2.89.", [("the decimal points were not lined up", ["line up|lined up|points|columns"]), ("correct answer 7.75", ["7\\.75"])], "The 4 tenths was added to 5 hundredths instead of 3 tenths: the decimal points were not lined up. 5.40 + 2.35 = 7.75.", o="O2"))

# ================================================================== 4.3
s = U.section("4.3", "Multiplying decimals", ["O3"])
s.idea("Method", ["Multiply without the decimal point, then put back as many decimal places as there are in the question altogether.",
       "2.4 × 3: 24 × 3 = 72 → 7.2.   0.6 × 0.4: 6 × 4 = 24 → 0.24."])
s.check(N("Work out 3.6 × 4.", 14.4, o="O3"))
s.mistake("Estimate", ["2.4 × 3 ≈ 2 × 3 = 6, so 72 or 0.72 cannot be right."])


def m1(r):
    a, n = d1(r), r.randint(2, 9)
    return N(f"Work out {fmt(a)} × {n}.", R4(a * n), o="O3")
def m2(r):
    a, n = d2(r), r.randint(2, 9)
    return N(f"Work out {fmt(a)} × {n}.", R4(a * n), o="O3")
def m3(r):
    a, b = r.randint(2, 9) / 10, r.randint(2, 9) / 10
    return N(f"Work out {fmt(a)} × {fmt(b)}.", R4(a * b), o="O3", d="H")
def m4(r):
    p, n = d2(r), r.randint(3, 9)
    return N(f"A drink costs ${p:.2f}. How much do {n} drinks cost?", R4(p * n), "$", units=["$"], o="O3")
def m5(r):
    a, b = d1(r), r.randint(2, 9)
    return N("Find the area of the rectangle.", R4(a * b), "m²", units=["m²"], o="O3", fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 4], [0, 4]], "s": [f"{fmt(a)} m", f"{b} m", "", ""]})
def m6(r):
    a, b = r.randint(12, 89), r.randint(2, 9)
    return TB(f"{a} × {b} = {a * b}. Use this to complete the table.", ["Calculation", "Answer"], [[f"{fmt(a / 10)} × {b}", B(R4(a * b / 10))], [f"{fmt(a / 100)} × {b}", B(R4(a * b / 100))]], o="O3")
def m7(r):
    a, b = round(r.uniform(2, 9), 1), r.randint(3, 9)
    e = round(a) * b
    return MC(f"Which is the best estimate of {fmt(a)} × {b}?", str(e), [str(e * 10), str(round(e / 10, 1)), str(e + 15)], o="O3")


s.std([m5, m6, m1, m2, m3, m4, m7], EX("Explain why 0.5 × 0.3 = 0.15.", [("5 × 3 = 15", ["15"]), ("tenths × tenths = hundredths: two decimal places", ["hundredth|two decimal|2 decimal|tenths"])], "5 × 3 = 15. There are two decimal places in the question altogether (tenths × tenths = hundredths), so the answer is 0.15.", o="O3"))

# ================================================================== 4.4
s = U.section("4.4", "Dividing decimals", ["O4"])
s.idea("Short division", ["Divide a decimal by a whole number with short division. Keep the decimal point in line: 7.2 ÷ 3 = 2.4.",
       "Add zeros if you need more places: 3.4 ÷ 4 = 3.40 ÷ 4 = 0.85."])
s.check(N("Work out 9.6 ÷ 4.", 2.4, o="O4"))
s.mistake("Points in line", ["Put the decimal point of the answer straight above the point in the number you are dividing."])


def v1(r):
    n, q = r.randint(2, 9), d1(r)
    return N(f"Work out {fmt(R4(n * q))} ÷ {n}.", q, o="O4")
def v2(r):
    n, q = r.randint(2, 9), d2(r)
    return N(f"Work out {fmt(R4(n * q))} ÷ {n}.", q, o="O4")
def v3(r):
    n, q = r.randint(3, 8), d2(r)
    return N(f"{n} friends share a bill of ${R4(n * q):.2f} equally. How much does each pay?", q, "$", units=["$"], o="O4")
def v4(r):
    n, q = r.randint(2, 9), d1(r)
    return N(f"A ribbon {fmt(R4(n * q))} m long is cut into {n} equal pieces. How long is each piece?", q, "m", units=["m"], o="O4")
def v5(r):
    n = pick(r, [4, 8, 5]); a = r.randint(1, 9) + r.randint(1, 9) / 10
    return N(f"Work out {fmt(a)} ÷ {n}. (Add zeros if you need to.)", R4(a / n), o="O4", d="H")
def v6(r):
    n, qs = r.randint(2, 9), [d1(r) for _ in range(2)]
    return TB(f"Complete the divisions by {n}.", ["Calculation", "Answer"], [[f"{fmt(R4(n * q))} ÷ {n}", B(q)] for q in qs], o="O4")
def v7(r):
    w, n = d2(r) * 10, r.randint(3, 8)
    return N(f"{n} identical bags have a total mass of {fmt(R4(w * n))} kg. What is the mass of one bag?", R4(w), "kg", units=["kg"], o="O4", data={"head": ["Bags", "Total mass (kg)"], "rows": [[str(n), fmt(R4(w * n))]]})


s.std([v6, v7, v1, v2, v3, v4, v5], EX("Explain how to work out 6.3 ÷ 3.", [("divide each part: 6 ÷ 3 = 2 and 0.3 ÷ 3 = 0.1", ["6 ?÷ ?3|0\\.3 ?÷ ?3|short division"]), ("answer 2.1", ["2\\.1"])], "Use short division, keeping the point in line: 6 ÷ 3 = 2 and 3 tenths ÷ 3 = 1 tenth, so 6.3 ÷ 3 = 2.1.", o="O4"))

# ================================================================== 4.5
s = U.section("4.5", "Making decimal calculations easier", ["O5"])
s.idea("Strategies", ["**Make whole numbers first**: 2.7 + 4.6 + 0.3 = (2.7 + 0.3) + 4.6 = 7.6.",
       "**Split**: 3.2 × 5 = 3 × 5 + 0.2 × 5 = 15 + 1 = 16.  **Compensate**: 4.9 × 3 = 5 × 3 − 0.1 × 3 = 14.7."])
s.check(N("Work out 1.6 + 3.9 + 0.4 mentally.", 5.9, o="O5"))
s.mistake("Use each part", ["When you split 3.2 into 3 + 0.2, multiply both parts."])


def k1(r):
    a = d1(r); b = round(10 - a, 1) if a < 10 else 1; c = d1(r)
    return N(f"Work out {fmt(a)} + {fmt(c)} + {fmt(b)} mentally.", R4(a + b + c), o="O5")
def k2(r):
    a, n = r.randint(2, 9), r.randint(2, 9)
    return N(f"Work out {a}.2 × {n} by splitting it into {a} × {n} + 0.2 × {n}.", R4((a + 0.2) * n), o="O5")
def k3(r):
    a, n = r.randint(2, 9), r.randint(2, 9)
    return N(f"Work out {a - 1}.9 × {n} mentally.", R4((a - 0.1) * n), o="O5", d="H")
def k4(r):
    v = d1(r)
    return N(f"Work out 0.5 × {fmt(v)} × 2.", v, o="O5")
def k5(r):
    rows = [("0.5 × 2", "1"), ("0.25 × 4", "1"), ("0.2 × 5", "1"), ("2.5 × 4", "10"), ("0.1 × 10", "1")]
    return GD("Find each answer.", "Answer", r.sample(rows, 4), o="O5", extra=["0.5", "100"])
def k6(r):
    p, n = r.randint(1, 9) + 0.99, r.randint(2, 6)
    return N(f"A pen costs ${fmt(p)}. How much do {n} pens cost?", R4(p * n), "$", units=["$"], o="O5", d="H")
def k7(r):
    a = d1(r); b = d1(r)
    return TB(f"Use {fmt(a)} + {fmt(b)} = {fmt(R4(a + b))} to complete the table.", ["Calculation", "Answer"], [[f"{fmt(b)} + {fmt(a)}", B(R4(a + b))], [f"{fmt(R4(a + b))} − {fmt(a)}", B(b)]], o="O5")


s.std([k5, k7, k1, k2, k3, k4, k6], EX("Explain an easy way to work out 3.8 + 2.5 + 1.2.", [("add 3.8 and 1.2 first to make 5", ["3\\.8 ?\\+ ?1\\.2|make 5|= ?5|whole number"]), ("5 + 2.5 = 7.5", ["7\\.5"])], "Re-order to make a whole number: 3.8 + 1.2 = 5. Then 5 + 2.5 = 7.5.", o="O5"))

U.mindmap(("Ordering", "Line up points • compare tenths, then hundredths", "O1", "4.1"), ("Adding and subtracting", "Line up the decimal points", "O2", "4.2"),
          ("Multiplying", "Multiply, then count decimal places", "O3", "4.3"), ("Dividing", "Short division • point in line", "O4", "4.4"),
          ("Easier calculations", "Make wholes • split • compensate", "O5", "4.5"))
