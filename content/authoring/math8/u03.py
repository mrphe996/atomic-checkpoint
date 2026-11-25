# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 3 Place value and rounding (3.1 Multiplying and dividing by 0.1 and 0.01, 3.2 Rounding).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *

U = Unit(3, "Place Value and Rounding", "Number",
         "Multiplying and dividing by 0.1 and 0.01, and rounding to decimal places and significant figures.",
         {"O1": {"code": "8Np.01", "sec": "3.1", "codeNote": "", "t": "Multiply and divide integers and decimals by 0.1 and 0.01, and explain the effect."},
          "O2": {"code": "8Np.02", "sec": "3.2", "codeNote": "", "t": "Round numbers to a given number of decimal places or significant figures."}})


def dp(v, n): return float(f"{v:.{n}f}")


# ================================================================== 3.1
s = U.section("3.1", "Multiplying and dividing by 0.1 and 0.01", ["O1"])
s.idea("Equivalent operations", ["Multiplying by **0.1** is the same as **dividing by 10**. Multiplying by **0.01** is the same as **dividing by 100**.",
       "Dividing by **0.1** is the same as **multiplying by 10**. Dividing by **0.01** is the same as **multiplying by 100**."],
       table={"head": ["Operation", "Same as"], "rows": [["× 0.1", "÷ 10"], ["× 0.01", "÷ 100"], ["÷ 0.1", "× 10"], ["÷ 0.01", "× 100"]]})
s.example("Using place value", "Work out 36 × 0.01 and 4.2 ÷ 0.1.", [("36 × 0.01 = 36 ÷ 100 = 0.36", "digits move 2 places right"), ("4.2 ÷ 0.1 = 4.2 × 10 = 42", "digits move 1 place left")], "0.36 and 42")
s.check(N("Work out 7.5 ÷ 0.01.", 750, o="O1", reason="÷ 0.01 is the same as × 100: 750."))
s.idea("Why × 0.1 is the same as ÷ 10", ["0.1 is one tenth, so multiplying by 0.1 means finding one tenth of the number: 45 × 0.1 = 4.5 = 45 ÷ 10.",
       "In the same way × 0.01 = ÷ 100, and ÷ 0.1 = × 10 (how many tenths are in 4.5? 45)."],
       table={"head": ["Calculation", "Same as", "Answer"], "rows": [["45 × 0.1", "45 ÷ 10", "4.5"], ["45 × 0.01", "45 ÷ 100", "0.45"], ["4.5 ÷ 0.1", "4.5 × 10", "45"], ["4.5 ÷ 0.01", "4.5 × 100", "450"]]})
s.check(MC("Before you read on: is 6 ÷ 0.1 bigger or smaller than 6?", "Bigger: 60", [("Smaller: 0.6", "That is 6 × 0.1. How many tenths make 6?"), ("The same", "Dividing by a number less than 1 makes it bigger.")], o="O1"))
s.mistake("Bigger or smaller?", ["Multiplying by a number less than 1 makes a positive number **smaller**. Dividing by a number less than 1 makes it **bigger**. Use this to check."])
s.check(MC("Which gives the biggest answer?", "8 ÷ 0.01", [("8 × 0.01", "This divides by 100."), ("8 ÷ 0.1", "This is × 10, but ÷ 0.01 is × 100."), ("8 × 0.1", "This divides by 10.")], o="O1"))
OPS = [("× 0.1", lambda v: v / 10), ("× 0.01", lambda v: v / 100), ("÷ 0.1", lambda v: v * 10), ("÷ 0.01", lambda v: v * 100)]


def val(r):
    return pick(r, [r.randint(2, 999), r.randint(11, 999) / 10, r.randint(101, 9999) / 100])


def p1(r):
    v = val(r); op, f = pick(r, OPS)
    return N(f"Work out {fmt(v)} {op}.", round(f(v), 6), o="O1", reason=f"{op} is the same as {'÷' if op[0] == '×' else '×'} {'10' if '0.1' in op and '0.01' not in op else '100'}: {fmt(round(f(v), 6))}.")
def p2(r):
    v = val(r); op, f = pick(r, OPS); a = round(f(v), 6)
    return N(f"Find the missing number: {fmt(v)} {op[0]} ☐ = {fmt(a)}", float(op[2:]), o="O1", d="H", reason=f"{fmt(v)} {op} = {fmt(a)}.")
def p3(r):
    rows = [("× 0.1", "÷ 10"), ("× 0.01", "÷ 100"), ("÷ 0.1", "× 10"), ("÷ 0.01", "× 100")]
    return GD("Which operation has the same effect?", "Same as", r.sample(rows, 4), o="O1", extra=["× 1000", "÷ 1000"])
def p4(r):
    v = val(r); ops = r.sample(OPS, 3)
    return TB(f"Complete the table for the number {fmt(v)}.", ["Calculation", "Answer"], [[f"{fmt(v)} {o}", B(round(f(v), 6))] for o, f in ops], o="O1")
def p5(r):
    c = r.randint(15, 95)
    return N(f"A sweet costs {c} cents. 1 cent = $0.01. How much is that in dollars?", c / 100, "$", units=["$"], o="O1", reason=f"{c} × 0.01 = {fmt(c / 100)}.")
def p6(r):
    m = r.randint(12, 950) / 10
    return N(f"A plank is {fmt(m)} m long. How many pieces 0.1 m long can be cut from it?", round(m * 10), "pieces", units=["pieces"], o="O1", reason=f"{fmt(m)} ÷ 0.1 = {fmt(m)} × 10 = {round(m * 10)}.")
def p7(r):
    v = val(r); op, f = pick(r, OPS)
    big = f(v) > v
    return MC(f"Without calculating, is {fmt(v)} {op} bigger or smaller than {fmt(v)}?", "bigger" if big else "smaller", [("smaller" if big else "bigger", "Dividing by a number less than 1 makes it bigger; multiplying makes it smaller."), ("the same", "")], o="O1")
def p8(r):
    v = r.randint(21, 990)
    return N(f"Work out {v} × 0.1 × 0.1.", v / 100, o="O1", d="H", reason=f"× 0.1 twice = ÷ 100: {fmt(v / 100)}.")
def p9(r):
    a = r.randint(2, 99) / 100; k = pick(r, [0.1, 0.01])
    return N(f"Work out {fmt(a)} ÷ {fmt(k)} × {fmt(k)}.", a, o="O1", d="H", reason="Dividing then multiplying by the same number leaves it unchanged.")
def p10(r):
    g = r.randint(150, 990)
    return N(f"A bag of rice has a mass of {g} g. 1 g = 0.001 kg. Write the mass of 10 bags in kg.", g * 10 / 1000, "kg", units=["kg"], o="O1", d="H", reason=f"{g} × 10 = {g * 10} g = {fmt(g * 10 / 1000)} kg.")
def p11(r):
    v = val(r); op, f = pick(r, OPS)
    a = round(f(v), 6)
    return MS(f"Select ALL the calculations equal to {fmt(v)} {op}.", [f"{fmt(v)} {'÷' if op[0] == '×' else '×'} {'10' if op[2:] == '0.1' else '100'}"], [f"{fmt(v)} {op[0]} {'10' if op[2:] == '0.1' else '100'}", f"{fmt(v)} {'÷' if op[0] == '×' else '×'} {'100' if op[2:] == '0.1' else '10'}"], o="O1", reason=f"{op} has the same effect as {'÷' if op[0] == '×' else '×'} {'10' if op[2:] == '0.1' else '100'}.")
def pa(r):
    v = r.randint(2, 9) * 10 + r.randint(1, 9)
    return N(f"Work out {v} ÷ 0.01 ÷ 0.1.", v * 1000, o="O1", d="VH", reason=f"× 100 then × 10: {v * 1000}.")


def y11(r):   # match equivalent
    rows = r.sample([("× 0.1", "÷ 10"), ("× 0.01", "÷ 100"), ("÷ 0.1", "× 10"), ("÷ 0.01", "× 100")], 4)
    return GD("Match each operation to the one that gives the same answer.", "Same as", rows, o="O1", d="H", extra=["× 1000"], reason="0.1 = 1/10 and 0.01 = 1/100.")
def y12(r):   # spot error
    a = r.randint(12, 98)
    return MC(f"Ben says {a} ÷ 0.1 = {a / 10:g}. What is right?", str(a * 10), [(f"{a / 10:g}", "That is × 0.1. Dividing by a tenth asks how many tenths fit in."), (f"{a / 100:g}", "That is ÷ 100.")], o="O1", d="H", reason=f"There are 10 tenths in each 1, so {a} ÷ 0.1 = {a * 10}.")


s.std([p3, p4, p1, p2, p5, p6, p7, p11, p8, p9, p10], EX("Explain why 5 ÷ 0.1 = 50.", [("0.1 goes into 1 ten times", ["ten|10 times|goes into|how many tenths"]), ("so ÷ 0.1 is the same as × 10", ["× ?10|multiply.*10|same as"])], "Dividing by 0.1 asks how many tenths are in 5. There are 10 tenths in each 1, so 5 ÷ 0.1 = 5 × 10 = 50.", o="O1"), adv=[pa, p2, p8],
      deep=[y11, y12])

# ================================================================== 3.2
s = U.section("3.2", "Rounding", ["O2"])
s.idea("Decimal places", ["To round to a number of **decimal places** (d.p.), look at the next digit: **5 or more** rounds up, **4 or less** keeps the digit.",
       "3.4782 to 2 d.p. → look at the third decimal (8) → 3.48. Keep the zeros you need: 2.698 to 2 d.p. is **2.70**."])
s.check(N("Round 6.0473 to 2 decimal places.", 6.05, o="O2", reason="The third decimal is 7, so round up: 6.05."))
s.idea("Significant figures", ["The **first significant figure** is the first digit that is not zero. 0.004 52 has first significant figure 4.",
       "Round 48 361 to 2 s.f.: 48 000 (keep the place value with zeros). Round 0.006 829 to 2 s.f.: 0.0068."])
s.example("Two kinds of rounding", "Round 0.030 76 to (a) 3 d.p. (b) 3 s.f.", [("3 d.p.: 0.030|76 → 0.031", "4th decimal is 7"), ("3 s.f.: 0.0307|6 → 0.0308", "first s.f. is the 3")], "0.031 and 0.0308")
s.check(N("Round 72 449 to 2 significant figures.", 72000, o="O2", reason="72|449: the third figure is 4, so round down: 72 000."))
s.idea("Why significant figures", ["Decimal places count from the decimal point; significant figures count from the first non-zero digit. 0.004 572 to 2 s.f. is 0.0046 – the zeros at the front only show the size.",
       "Use significant figures to keep the same accuracy for very big or very small numbers."])
s.check(MC("Before you read on: round 38 472 to 2 significant figures.", "38 000", [("38", "Keep the place value: fill with zeros."), ("39 000", "The next digit is 4, so round down.")], o="O2"))
s.mistake("Keep the size", ["Rounding 3876 to 1 s.f. gives 4000, not 4. The rounded number must be about the same size."])


def sfr(v, n):
    from math import log10, floor
    k = n - 1 - floor(log10(abs(v))); return round(v, k)


def q1(r):
    v = round(r.uniform(1, 99), 4); n = r.randint(1, 3)
    return N(f"Round {fmt(v)} to {n} decimal place{'s' if n > 1 else ''}.", dp(v, n), o="O2", reason=f"Look at decimal place {n + 1}: {v:.{n}f}.")
def q2(r):
    v = r.randint(1001, 99999); n = r.randint(1, 3)
    return N(f"Round {fmt(v)} to {n} significant figure{'s' if n > 1 else ''}.", sfr(v, n), o="O2", reason=f"{fmt(sfr(v, n))}.")
def q3(r):
    v = round(r.uniform(0.001, 0.09), 5); n = r.randint(1, 2)
    return N(f"Round {fmt(v)} to {n} significant figure{'s' if n > 1 else ''}.", float(f"{sfr(v, n):.10g}"), o="O2", d="H", reason=f"The first significant figure is the first non-zero digit: {fmt(float(f'{sfr(v, n):.10g}'))}.")
def q4(r):
    v = round(r.uniform(1, 50), 3)
    return TB(f"Round {fmt(v)} to:", ["Accuracy", "Answer"], [["1 d.p.", B(dp(v, 1))], ["2 d.p.", B(dp(v, 2))], ["1 s.f.", B(sfr(v, 1))]], o="O2")
def q5(r):
    rows = [("0.0306", "3"), ("4.07", "3"), ("1200", "2"), ("0.5", "1"), ("30.04", "4"), ("0.00720", "3")]
    return GD("How many significant figures? (Zeros at the end of a whole number do not count.)", "Significant figures", r.sample(rows, 4), o="O2", d="H", extra=["1", "2", "3", "4"])
def q6(r):
    a, b = r.randint(21, 89), r.randint(21, 89)
    ea, eb = sfr(a, 1), sfr(b, 1)
    return N(f"Estimate {a} × {b} by rounding each number to 1 significant figure.", ea * eb, o="O2", reason=f"{ea} × {eb} = {ea * eb}.")
def q7(r):
    a, b = r.randint(210, 890), r.randint(21, 89)
    ea, eb = sfr(a, 1), sfr(b, 1)
    return N(f"Estimate {a} ÷ {b} by rounding each number to 1 significant figure. Give your answer to 1 d.p. if needed.", round(ea / eb, 1), o="O2", d="H", tol=0.05, reason=f"{ea} ÷ {eb} ≈ {fmt(round(ea / eb, 1))}.")
def q8(r):
    p = r.randint(15000, 98000)
    return N(f"A stadium holds {fmt(p)} people. A newspaper rounds this to 2 significant figures. What number does it print?", sfr(p, 2), "people", units=["people"], o="O2", reason=f"{fmt(sfr(p, 2))}.")
def q9(r):
    v = round(r.uniform(1, 9), 4)
    return MC(f"Which is {fmt(v)} rounded to 3 significant figures?", f"{sfr(v, 3):.2f}", [(f"{sfr(v, 3) + 0.01:.2f}", ""), (f"{v:.3f}", "That is 3 decimal places (4 s.f.)."), (f"{sfr(v, 2):.1f}", "That is 2 s.f.")], o="O2")
def q10(r):
    v = round(r.uniform(2, 9), 3); n = 2; a = dp(v, n)
    if abs(a * 10 - round(a * 10)) > 1e-9: return None
    return S(f"Round {fmt(v)} to 2 decimal places. (Keep any zero you need.)", [f"{a:.2f}"], o="O2", d="H", reason=f"{a:.2f} – the zero shows it is correct to 2 d.p.")
def q11(r):
    c = round(r.uniform(5, 40), 2); n = r.randint(3, 9)
    return N(f"{n} friends share a bill of ${fmt(c * n + 0.01)} equally. How much does each pay, to the nearest cent?", round((c * n + 0.01) / n, 2), "$", units=["$"], o="O2", d="H", tol=0.005, reason=f"{fmt(c * n + 0.01)} ÷ {n} ≈ {round((c * n + 0.01) / n, 2)}.")
def q12(r):
    l = r.randint(15, 60) / 10
    return N(f"A square has side {fmt(l)} cm. Find its area correct to 1 decimal place.", dp(l * l, 1), "cm²", units=["cm²"], o="O2", fig={"kind": "shape", "pts": [[0, 0], [5, 0], [5, 5], [0, 5]], "s": [f"{fmt(l)} cm", "", "", ""]}, reason=f"{fmt(l)}² = {fmt(round(l * l, 4))} ≈ {dp(l * l, 1)}.")
def qa(r):
    a, b, c = round(r.uniform(10, 30), 1), round(r.uniform(2, 9), 1), round(r.uniform(1.1, 3.9), 1)
    return N(f"Work out ({fmt(a)} + {fmt(b)}) ÷ {fmt(c)}. Give your answer to 3 significant figures.", float(f"{sfr((a + b) / c, 3):.10g}"), o="O2", d="VH", tol=0.0001, reason=f"{fmt(round(a + b, 2))} ÷ {fmt(c)} = {(a + b) / c:.5f} → {float(f'{sfr((a + b) / c, 3):.10g}')}.")


def y21(r):   # s.f. vs d.p.
    v = pick(r, [0.04567, 0.3089, 1.2345, 0.007218])
    return MC(f"Round {v} to 2 significant figures.", f"{float(f'{v:.2g}'):g}", [(f"{v:.2f}", "That is 2 decimal places."), (f"{float(f'{v:.3g}'):g}", "That is 3 significant figures.")], o="O2", d="H",
              reason="Start counting at the first non-zero digit.") if f"{v:.2f}" != f"{float(f'{v:.2g}'):g}" else None
def y22(r):   # bounds
    t = r.randint(3, 9) * 10
    return TB(f"A length is {t} cm to the nearest 10 cm. Complete the table.", ["", "Length (cm)"], [["Lower bound", B(t - 5)], ["Upper bound", B(t + 5)]], o="O2", d="H", reason=f"Halfway points: {t - 5} and {t + 5}.")


s.std([q4, q5, q1, q2, q3, q6, q8, q9, q7, q10, q11, q12], EX("Explain why 0.0507 rounded to 2 significant figures is 0.051 and not 0.05.", [("the first significant figure is the 5 (not the zeros at the start)", ["first significant|first non.?zero|leading zeros|zeros.*don't count|zeros.*do not count"]), ("the 2nd significant figure is 0, and the next digit 7 rounds it up to 1", ["7.*round|round.*up|0 becomes 1|next digit"])], "Leading zeros are not significant, so the first significant figure is 5 and the second is 0. The next digit is 7, so the 0 rounds up to 1: 0.051.", o="O2"), adv=[qa, q3, q11],
      deep=[y21, y22])

U.mindmap(("× and ÷ by 0.1 and 0.01", "× 0.1 = ÷ 10 • ÷ 0.01 = × 100", "O1", "3.1"), ("Rounding", "d.p. counts after the point • s.f. starts at the first non-zero digit", "O2", "3.2"))
