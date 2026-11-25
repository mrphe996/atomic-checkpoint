# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 4 Decimals (4.1 Ordering decimals, 4.2 Multiplying decimals, 4.3 Dividing by decimals,
4.4 Making decimal calculations easier). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *

U = Unit(4, "Decimals", "Number",
         "Ordering decimals with inequality signs, multiplying and dividing by decimals, and mental strategies for decimal calculations.",
         {"O1": {"code": "8Nf.01", "sec": "4.1", "codeNote": "", "t": "Order and compare decimals, including negative decimals, using =, ≠, < and >."},
          "O2": {"code": "8Nf.02", "sec": "4.2", "codeNote": "", "t": "Multiply decimals by whole numbers and by other decimals."},
          "O3": {"code": "8Nf.03", "sec": "4.3", "codeNote": "", "t": "Divide whole numbers and decimals by a decimal."},
          "O4": {"code": "8Nf.04", "sec": "4.4", "codeNote": "", "t": "Use place value, factors and the laws of arithmetic to simplify decimal calculations."}})
d1 = lambda r: r.randint(11, 99) / 10
d2 = lambda r: r.randint(101, 999) / 100

# ================================================================== 4.1
s = U.section("4.1", "Ordering decimals", ["O1"])
s.idea("Comparing decimals", ["Line the decimal points up and compare digits from the left. It can help to write zeros so every number has the same number of decimal places: 0.7 = 0.70 > 0.65.",
       "For **negative** decimals, the one further from zero is smaller: −2.3 < −2.03."], fig={"kind": "numline", "min": -3, "max": 3})
s.check(MC("Which is the largest?", "0.7", [("0.65", "0.70 > 0.65"), ("0.699", "0.700 > 0.699"), ("0.07", "")], o="O1"))
s.idea("Signs", ["**<** is less than, **>** is greater than, **≠** means 'is not equal to'. 4.50 = 4.5 but 4.05 ≠ 4.5."])
s.check(MC("Before you read on: which is bigger, −0.3 or −0.25?", "−0.25", [("−0.3", "On a number line −0.3 is further left."), ("They are equal", "−0.30 and −0.25 differ by 0.05.")], o="O1", hint="Think of temperatures."))
s.mistake("Longer is not bigger", ["0.125 is NOT bigger than 0.2 just because it has more digits: 0.125 < 0.200."])
s.check(CMP("3.08", "3.8", "<", o="O1", reason="3.08 < 3.80."))


def o1(r):
    a = d2(r); b = round(a + pick(r, [0.01, 0.1, -0.01, -0.1, 0.09]), 2)
    sgn = "<" if a < b else ">"
    return CMP(fmt(a), fmt(b), sgn, o="O1", reason=f"{fmt(a)} {sgn} {fmt(b)}.")
def o2(r):
    base = r.randint(1, 9); vs = sorted({round(base + x, 3) for x in (r.randint(1, 9) / 10, r.randint(1, 99) / 100, r.randint(1, 999) / 1000, r.randint(1, 9) / 100)})
    if len(vs) < 4: return None
    sh = vs[:]; r.shuffle(sh)
    return OD("Put these decimals in order, smallest first.", [fmt(v) for v in vs], o="O1", reason="Compare digits place by place.")
def o3(r):
    a, b = -d2(r), -d2(r)
    if a == b: return None
    return CMP(fmt(a), fmt(b), "<" if a < b else ">", o="O1", d="H", reason="For negative numbers, the one further from zero is smaller.")
def o4(r):
    rows = [("4.5 and 4.50", "="), ("0.3 and 0.30", "="), ("2.05 and 2.5", "≠"), ("7.1 and 7.01", "≠"), ("0.60 and 0.6", "="), ("5.40 and 5.04", "≠")]
    return GD("Write = or ≠ for each pair.", "Sign", r.sample(rows, 4), o="O1")
def o5(r):
    a = d2(r); vals = [a, round(a + 0.1, 2), round(a - 0.05, 2), round(a + 0.01, 2)]
    nm = r.sample(["Ana", "Ben", "Chen", "Dev", "Eli", "Fay"], 4)
    w = nm[vals.index(max(vals))]
    return MC("Four friends jump these distances in metres. Who jumps furthest?", w, [n for n in nm if n != w], o="O1", data={"head": ["Name", *nm], "rows": [["Jump (m)", *[fmt(v) for v in vals]]]})
def o6(r):
    lo = r.randint(2, 8) + r.randint(1, 9) / 10
    return N(f"Write a number with 2 decimal places that is between {fmt(lo)} and {fmt(round(lo + 0.1, 1))}, and ends in 5.", round(lo + 0.05, 2), o="O1", reason=f"{fmt(round(lo + 0.05, 2))}.")
def o7(r):
    vs = sorted(r.sample([-3.2, -3.02, -2.9, -0.5, -0.45, 0.4, 1.05, -1.5], 4))
    return OD("Put these numbers in order, smallest first.", [fmt(v) for v in vs], o="O1", d="H")
def o8(r):
    a = r.randint(1, 9) + r.randint(1, 99) / 100
    return MS(f"Select ALL the numbers greater than {fmt(a)}.", [fmt(round(a + 0.01, 2)), fmt(round(a + 0.1, 2))], [fmt(round(a - 0.01, 2)), fmt(round(a - 0.1, 2))], o="O1")
def o9(r):
    t = sorted(round(r.uniform(9.5, 12.5), 2) for _ in range(4)); nm = ["Lane 1", "Lane 2", "Lane 3", "Lane 4"]; sh = t[:]; r.shuffle(sh)
    w = nm[sh.index(min(sh))]
    return MC("These are times (seconds) in a 100 m race. Which lane wins?", w, [n for n in nm if n != w], o="O1", data={"head": ["Lane", *nm], "rows": [["Time (s)", *[f"{v:.2f}" for v in sh]]]}, d="H", reason="The smallest time wins.")


def z11(r):   # find all between negatives
    good = r.sample(["−0.35", "−0.32", "−0.38", "−0.31"], 2); bad = r.sample(["−0.29", "−0.41", "−0.3", "−0.4"], 2)
    return MS("Select ALL the numbers between −0.4 and −0.3.", good, bad, o="O1", d="H", reason="On the number line they lie between −0.40 and −0.30 (not including the ends).")


s.std([o4, o5, o1, o2, o3, o6, o8, o7, o9], EX("Explain why 0.4 is greater than 0.35.", [("write 0.4 as 0.40", ["0\\.40|same number of decimal|add a zero"]), ("40 hundredths > 35 hundredths / 4 tenths > 3 tenths", ["40.*35|tenths|4 ?> ?3|hundredths"])], "0.4 = 0.40. Comparing the tenths, 4 tenths is more than 3 tenths, so 0.40 > 0.35.", o="O1"),
      deep=[z11])

# ================================================================== 4.2
s = U.section("4.2", "Multiplying decimals", ["O2"])
s.idea("Method", ["Ignore the decimal points and multiply the whole numbers. Then count the **total number of decimal places** in the question and put that many in the answer.",
       "0.3 × 0.04: 3 × 4 = 12; 1 + 2 = 3 decimal places → 0.012."])
s.example("Two decimals", "Work out 2.6 × 1.4.", [("26 × 14 = 364", "whole numbers"), ("1 + 1 = 2 decimal places", ""), ("3.64", "estimate: 3 × 1 = 3 ✓")], "3.64")
s.check(N("Work out 0.6 × 0.07.", 0.042, o="O2", reason="6 × 7 = 42; 3 decimal places → 0.042."))
s.idea("Estimate first, then place the point", ["2.3 × 0.4: estimate 2 × 0.4 = 0.8. Work out 23 × 4 = 92, then use the estimate (or count 2 decimal places) to place the point: 0.92.",
       "Multiplying by a number between 0 and 1 gives a smaller answer."])
s.check(MC("Before you read on: is 0.6 × 0.7 more or less than 0.6?", "Less: 0.42", [("More: 4.2", "Multiplying by 0.7 (less than 1) makes it smaller."), ("More: 0.42", "0.42 is less than 0.6.")], o="O2"))
s.mistake("Estimate first", ["Always estimate: 4.8 × 3.1 ≈ 5 × 3 = 15, so an answer of 148.8 or 1.488 is clearly wrong."])


def x1(r):
    a, b = d1(r), r.randint(2, 9)
    return N(f"Work out {fmt(a)} × {b}.", round(a * b, 4), o="O2", reason=f"{round(a * 10)} × {b} = {round(a * 10) * b}; 1 d.p. → {fmt(round(a * b, 4))}.")
def x2(r):
    a, b = d1(r), d1(r)
    return N(f"Work out {fmt(a)} × {fmt(b)}.", round(a * b, 4), o="O2", reason=f"{round(a * 10)} × {round(b * 10)} = {round(a * 10) * round(b * 10)}; 2 d.p. → {fmt(round(a * b, 4))}.")
def x3(r):
    a, b = r.randint(2, 9) / 10, r.randint(1, 9) / 100
    return N(f"Work out {fmt(a)} × {fmt(b)}.", round(a * b, 5), o="O2", reason=f"3 decimal places in total → {fmt(round(a * b, 5))}.")
def x4(r):
    p, k = r.randint(105, 899) / 100, round(r.uniform(1.5, 4.5), 1)
    return N(f"Cheese costs ${fmt(p)} per kg. How much does {fmt(k)} kg cost? Give your answer to the nearest cent.", round(p * k, 2), "$", units=["$"], o="O2", d="H", tol=0.005, reason=f"{fmt(p)} × {fmt(k)} = {fmt(round(p * k, 4))} ≈ ${round(p * k, 2)}.")
def x5(r):
    a, b = d1(r), d1(r)
    return N(f"A rectangle measures {fmt(a)} m by {fmt(b)} m. Find its area.", round(a * b, 4), "m²", units=["m²"], o="O2", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [8, 4], [0, 4]], "s": [f"{fmt(a)} m", f"{fmt(b)} m", "", ""]}, reason=f"{fmt(a)} × {fmt(b)} = {fmt(round(a * b, 4))}.")
def x6(r):
    a, b = r.randint(12, 89), r.randint(12, 89)
    p = a * b
    return TB(f"{a} × {b} = {p}. Use this to complete the table.", ["Calculation", "Answer"], [[f"{a / 10:g} × {b}", B(round(p / 10, 4))], [f"{a / 10:g} × {b / 10:g}", B(round(p / 100, 4))], [f"{a / 100:g} × {b / 10:g}", B(round(p / 1000, 5))]], o="O2", d="H")
def x7(r):
    a, b = round(r.uniform(2, 9), 1), round(r.uniform(2, 9), 1)
    est = round(a) * round(b)
    return MC(f"Which is the best estimate of {fmt(a)} × {fmt(b)}?", str(est), [str(est * 10), str(round(est / 10, 1)), str(est + 20)], o="O2", reason=f"{round(a)} × {round(b)} = {est}.")
def x8(r):
    a, b = r.randint(2, 9) / 10, r.randint(2, 9) / 10
    return N(f"Work out ({fmt(a)})² + {fmt(b)} × 0.1.", round(a * a + b * 0.1, 4), o="O2", d="H", reason=f"{fmt(round(a * a, 4))} + {fmt(round(b * 0.1, 4))}.")
def x9(r):
    w, n = round(r.uniform(0.2, 0.9), 2), r.randint(12, 40)
    return N(f"One tile is {fmt(w)} m long. How long is a row of {n} tiles?", round(w * n, 4), "m", units=["m"], o="O2", reason=f"{fmt(w)} × {n} = {fmt(round(w * n, 4))} m.")


def z21(r):   # spot error by estimate
    a, b = pick(r, [(2.4, 0.3), (3.6, 0.2), (1.5, 0.4), (4.8, 0.5)])
    return MC(f"Max says {a} × {b} = {round(a * b * 10, 2):g}. Use an estimate to decide what is right.", f"{round(a * b, 3):g}", [(f"{round(a * b * 10, 2):g}", f"{a} × {b} should be less than {a}."), (f"{round(a * b / 10, 4):g}", "Too small: estimate it.")], o="O2", d="H",
              reason=f"Estimate {round(a)} × {b} ≈ {round(a) * b:g}; the answer is {round(a * b, 3):g}.")


s.std([x5, x6, x1, x2, x3, x7, x9, x4, x8], EX("Explain why 0.2 × 0.3 = 0.06 and not 0.6.", [("2 × 3 = 6", ["2 ?× ?3|\\b6\\b"]), ("tenths × tenths = hundredths: two decimal places", ["hundredth|two decimal|2 decimal|tenths"])], "2 × 3 = 6. Tenths multiplied by tenths give hundredths, so the answer has two decimal places: 0.06.", o="O2"),
      deep=[z21])

# ================================================================== 4.3
s = U.section("4.3", "Dividing by decimals", ["O3"])
s.idea("Make the divisor whole", ["To divide by a decimal, multiply **both** numbers by 10, 100, … until the number you divide by is a whole number. The answer does not change.",
       "4.8 ÷ 0.6 = 48 ÷ 6 = 8.   7.2 ÷ 0.08 = 720 ÷ 8 = 90."])
s.example("Dividing", "Work out 15.6 ÷ 1.2.", [("× 10: 156 ÷ 12", "both numbers"), ("= 13", "")], "13")
s.check(N("Work out 3.6 ÷ 0.4.", 9, o="O3", reason="36 ÷ 4 = 9."))
s.idea("Why we multiply both numbers by 10", ["7.2 ÷ 0.3 is the same as 72 ÷ 3, because multiplying both numbers by 10 keeps the answer the same (how many 3s in 72 = how many 0.3s in 7.2).",
       "Make the divisor a whole number, then divide as normal."])
s.check(MC("Before you read on: is 8 ÷ 0.5 bigger or smaller than 8?", "Bigger: 16", [("Smaller: 4", "That is 8 × 0.5. How many halves are in 8?"), ("The same", "Dividing by less than 1 gives more.")], o="O3"))
s.mistake("Both numbers", ["If you multiply only the divisor by 10, the answer is 10 times too small."])


def v1(r):
    b, q = r.randint(2, 9) / 10, r.randint(2, 15)
    return N(f"Work out {fmt(round(b * q, 2))} ÷ {fmt(b)}.", q, o="O3", reason=f"× 10: {fmt(round(b * q * 10, 2))} ÷ {round(b * 10)} = {q}.")
def v2(r):
    b, q = r.randint(2, 9) / 100, r.randint(2, 30)
    return N(f"Work out {fmt(round(b * q, 3))} ÷ {fmt(b)}.", q, o="O3", reason=f"× 100: {fmt(round(b * q * 100, 2))} ÷ {round(b * 100)} = {q}.")
def v3(r):
    b, q = r.randint(11, 25) / 10, r.randint(3, 12)
    return N(f"Work out {fmt(round(b * q, 2))} ÷ {fmt(b)}.", q, o="O3", d="H", reason=f"× 10: {fmt(round(b * q * 10, 1))} ÷ {round(b * 10)} = {q}.")
def v4(r):
    l, p = r.randint(3, 12), r.randint(2, 8) / 10
    return N(f"A ribbon is {l} m long. How many {fmt(p)} m pieces can be cut from it?", int(l / p + 1e-9), "pieces", units=["pieces"], o="O3", d="H", reason=f"{l} ÷ {fmt(p)} = {fmt(round(l / p, 3))}, so {int(l / p + 1e-9)} whole pieces.")
def v5(r):
    a, b = r.randint(12, 96), r.randint(2, 9)
    a -= a % b
    return TB(f"{a} ÷ {b} = {a // b}. Use this to complete the table.", ["Calculation", "Answer"], [[f"{a} ÷ {fmt(b / 10)}", B(a // b * 10)], [f"{fmt(a / 10)} ÷ {fmt(b / 10)}", B(a // b)], [f"{fmt(a / 10)} ÷ {fmt(b / 100)}", B(a // b * 10)]], o="O3", d="H")
def v6(r):
    p, q = r.randint(2, 9) / 10, r.randint(3, 15)
    return N(f"Pencils cost ${fmt(p)} each. How many can you buy with ${fmt(round(p * q, 2))}?", q, "pencils", units=["pencils"], o="O3", reason=f"{fmt(round(p * q, 2))} ÷ {fmt(p)} = {q}.")
def v7(r):
    b = r.randint(2, 9) / 10; q = r.randint(2, 12)
    return MC(f"Which calculation has the same answer as {fmt(round(b * q, 2))} ÷ {fmt(b)}?", f"{fmt(round(b * q * 10, 2))} ÷ {round(b * 10)}", [f"{fmt(round(b * q, 2))} ÷ {round(b * 10)}", f"{fmt(round(b * q * 100, 2))} ÷ {round(b * 10)}", f"{fmt(round(b * q, 2))} × {round(b * 10)}"], o="O3")
def v8(r):
    rows = [("8 ÷ 0.5", "16"), ("6 ÷ 0.2", "30"), ("4.5 ÷ 0.9", "5"), ("0.3 ÷ 0.01", "30"), ("2.4 ÷ 0.6", "4"), ("7 ÷ 0.1", "70")]
    return GD("Find each answer.", "Answer", r.sample(rows, 4), o="O3", extra=["0.8", "3"])
def v9(r):
    d, t = r.randint(30, 150), r.randint(3, 9) / 2
    return N(f"A car travels {fmt(d * t)} km in {fmt(t)} hours. Find its average speed in km/h.", d, "km/h", units=["km/h"], o="O3", d="H", reason=f"{fmt(d * t)} ÷ {fmt(t)} = {d}.")


def z31(r):   # equivalent divisions
    a, b = pick(r, [(4.8, 0.6), (3.6, 0.4), (2.5, 0.5), (9.6, 0.8)])
    good = [f"{a * 10:g} ÷ {b * 10:g}", f"{a * 100:g} ÷ {b * 100:g}"]; bad = [f"{a * 10:g} ÷ {b:g}", f"{a:g} ÷ {b * 10:g}"]
    return MS(f"Select ALL the calculations with the same answer as {a} ÷ {b}.", good, bad, o="O3", d="H", reason="Multiply BOTH numbers by the same power of 10.")


s.std([v5, v8, v1, v2, v6, v7, v4, v3, v9], EX("Explain why 6 ÷ 0.5 = 12.", [("how many halves in 6", ["halves|0\\.5 goes|how many"]), ("2 halves in each 1, so 6 × 2 = 12 / multiply both by 10: 60 ÷ 5", ["2 halves|× ?2|60 ?÷ ?5|twice"])], "Dividing by 0.5 asks how many halves fit into 6. There are 2 halves in each whole, so 6 × 2 = 12 (or 60 ÷ 5 = 12).", o="O3"),
      deep=[z31])

# ================================================================== 4.4
s = U.section("4.4", "Making decimal calculations easier", ["O4"])
s.idea("Strategies", ["**Re-order** to make nice pairs: 0.25 × 7.3 × 4 = (0.25 × 4) × 7.3 = 7.3.",
       "**Split** a number: 4.9 × 6 = 5 × 6 − 0.1 × 6 = 30 − 0.6 = 29.4.  **Use factors**: 1.5 × 12 = 1.5 × 2 × 6 = 3 × 6 = 18."])
s.example("Compensation", "Work out 3.99 × 5 in your head.", [("3.99 = 4 − 0.01", ""), ("4 × 5 − 0.01 × 5 = 20 − 0.05", "")], "19.95")
s.check(N("Work out 0.5 × 3.7 × 2 mentally.", 3.7, o="O4", reason="0.5 × 2 = 1, so the answer is 3.7."))
s.check(MC("Before you read on: which is easiest to work out mentally, 0.25 × 36 or 36 ÷ 4?", "They are the same – 36 ÷ 4 = 9", [("0.25 × 36 is easier", "0.25 = 1/4, so it is the same as ÷ 4."), ("They give different answers", "0.25 × 36 = 36 ÷ 4.")], o="O4"))
s.mistake("Keep the value", ["When you split 4.9 into 5 − 0.1, you must multiply BOTH parts."])


def k1(r):
    v = d2(r); p = pick(r, [(0.25, 4), (0.5, 2), (0.2, 5), (2.5, 4)])
    return N(f"Work out {fmt(p[0])} × {fmt(v)} × {p[1]} mentally.", round(p[0] * p[1] * v, 4), o="O4", reason=f"{fmt(p[0])} × {p[1]} = {fmt(p[0] * p[1])}, so {fmt(round(p[0] * p[1] * v, 4))}.")
def k2(r):
    a, n = r.randint(2, 9), r.randint(3, 9)
    return N(f"Work out {a - 1}.9 × {n} by working out {a} × {n} − 0.1 × {n}.", round((a - 0.1) * n, 4), o="O4", reason=f"{a * n} − {fmt(0.1 * n)} = {fmt(round((a - 0.1) * n, 4))}.")
def k3(r):
    a, n = r.randint(2, 9), r.randint(3, 9)
    return N(f"Work out {a - 1}.99 × {n} mentally.", round((a - 0.01) * n, 4), o="O4", d="H", reason=f"{a} × {n} − 0.01 × {n} = {fmt(round((a - 0.01) * n, 4))}.")
def k4(r):
    a, b = r.randint(2, 9) / 10, pick(r, [12, 14, 16, 18, 24])
    return N(f"Work out {fmt(1 + a)} × {b} using factors (e.g. × 2, then × {b // 2}).", round((1 + a) * b, 4), o="O4", reason=f"{fmt(1 + a)} × 2 = {fmt(2 * (1 + a))}; × {b // 2} = {fmt(round((1 + a) * b, 4))}.")
def k5(r):
    a, b, c = d1(r), d1(r), d1(r)
    t = round(10 - a, 1)
    return N(f"Work out {fmt(a)} + {fmt(b)} + {fmt(t)} mentally.", round(a + b + t, 4), o="O4", reason=f"{fmt(a)} + {fmt(t)} = 10 first.")
def k6(r):
    rows = [("0.25 × 4", "1"), ("0.5 × 2", "1"), ("0.2 × 5", "1"), ("1.25 × 8", "10"), ("2.5 × 4", "10"), ("0.125 × 8", "1")]
    return GD("Find each product.", "Product", r.sample(rows, 4), o="O4", extra=["100", "0.1"])
def k7(r):
    a = d1(r); b = d1(r)
    return TB(f"Use {fmt(a)} × {fmt(b)} = {fmt(round(a * b, 4))} to complete the table.", ["Calculation", "Answer"], [[f"{fmt(b)} × {fmt(a)}", B(round(a * b, 4))], [f"{fmt(a * 10)} × {fmt(b)}", B(round(a * b * 10, 4))], [f"{fmt(round(a * b, 4))} ÷ {fmt(a)}", B(b)]], o="O4", d="H")
def k8(r):
    a = r.randint(2, 9) + 0.5; n = r.randint(4, 12) * 2
    return MC(f"Which calculation makes {fmt(a)} × {n} easiest to work out mentally?", f"{fmt(a * 2)} × {n // 2}", [f"{fmt(a)} + {n}", f"{fmt(a / 2)} × {n // 2}", f"{fmt(a)} × {n * 2}"], o="O4", reason=f"Double {fmt(a)} and halve {n}: {fmt(a * 2)} × {n // 2} = {fmt(a * n)}.")
def k9(r):
    p, n = r.randint(1, 9) + 0.99, r.randint(3, 6)
    return N(f"A T-shirt costs ${fmt(p)}. How much do {n} T-shirts cost? Work it out mentally.", round(p * n, 2), "$", units=["$"], o="O4", reason=f"{round(p + 0.01)} × {n} − 0.01 × {n} = {fmt(round(p * n, 2))}.")


def z41(r):   # pick strategy
    rows = r.sample([("0.25 × 48", "Divide by 4"), ("0.5 × 86", "Halve"), ("19.9 × 3", "Round and adjust"), ("2.5 × 4 × 1.7", "Make 10 first")], 4)
    return GD("Choose the best strategy for each.", "Strategy", rows, o="O4", d="H", extra=["Long multiplication"], reason="0.25 is a quarter, 0.5 is a half, 19.9 is close to 20, and 2.5 × 4 = 10.")


s.std([k6, k7, k1, k2, k4, k5, k8, k3, k9], EX("Explain an easy way to work out 0.25 × 9.6 × 4.", [("re-order: 0.25 × 4 first", ["0\\.25 ?× ?4|re.?order|swap|first"]), ("= 1, so the answer is 9.6", ["9\\.6|= ?1"])], "Multiply in any order: 0.25 × 4 = 1, then 1 × 9.6 = 9.6.", o="O4"),
      deep=[z41])

U.mindmap(("Ordering", "Line up points • same number of d.p. • < > = ≠", "O1", "4.1"), ("Multiplying", "Ignore points • count the d.p. • estimate", "O2", "4.2"),
          ("Dividing", "Make the divisor whole • change both numbers", "O3", "4.3"), ("Easier calculations", "Re-order • split • factors • compensate", "O4", "4.4"))
