# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 1 The number system (1.1 Understanding place value, 1.2 Rounding decimal numbers).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(1, "The Number System", "Number",
         "Place value in whole numbers and decimals with up to two decimal places, multiplying and dividing by 10 and 100, and rounding decimals.",
         {"O1": {"code": "5Np.01", "sec": "1.1", "codeNote": "", "t": "Understand the value of each digit in whole numbers and decimals with one or two decimal places, and multiply and divide by 10 and 100."},
          "O2": {"code": "5Np.02", "sec": "1.2", "codeNote": "", "t": "Round numbers with one decimal place to the nearest whole number."}})
PV = ["thousands", "hundreds", "tens", "ones", "tenths", "hundredths"]
PVV = [1000, 100, 10, 1, 0.1, 0.01]

s = U.section("1.1", "Understanding place value", ["O1"])
s.idea("Ones, tenths and hundredths", ["The digits after the decimal point are **tenths** and **hundredths**. In 347.25 the 2 is worth 2 tenths (0.2) and the 5 is worth 5 hundredths (0.05).",
       "1 = 10 tenths = 100 hundredths."], table={"head": ["Hundreds", "Tens", "Ones", ".", "Tenths", "Hundredths"], "rows": [["3", "4", "7", ".", "2", "5"]]})
s.check(N("What is the value of the digit 8 in 5.81? Give your answer as a decimal.", 0.8, o="O1"))
s.idea("× and ÷ by 10 and 100", ["× 10 moves every digit **one place left**; ÷ 10 moves every digit one place right. × 100 and ÷ 100 move **two places**.",
       "4.6 × 10 = 46 and 52 ÷ 100 = 0.52."])
s.check(MC('Before you read on: what is the value of the 6 in 3.06?', '6 hundredths', [('6 tenths', 'The tenths digit is 0.'), ('6 ones', 'It is after the decimal point.')], o='O1'))
s.mistake("Do not just add a zero", ["4.6 × 10 is 46, not 4.60."])


def p1(r):
    ds = r.sample(range(1, 10), 6); v = round(sum(d * w for d, w in zip(ds, PVV)), 2); k = r.randrange(6)
    return N(f"What is the value of the digit {ds[k]} in {fmt(v)}?", round(ds[k] * PVV[k], 2), o="O1", reason=f"It is in the {PV[k]} place.")
def p2(r):
    v = dec(r, 1, 99, 1); k = pick(r, [10, 100])
    return N(f"Work out {fmt(v)} × {k}.", round(v * k, 2), o="O1")
def p3(r):
    v = r.randint(1, 999); k = pick(r, [10, 100])
    return N(f"Work out {v} ÷ {k}.", round(v / k, 2), o="O1")
def p4(r):
    v = dec(r, 10, 999, 2)
    w, d = f"{v:.2f}".split(".")
    w = w.zfill(3)
    return TB(f"Write the digits of {v:.2f} in the place value table.", ["Hundreds", "Tens", "Ones", "Tenths", "Hundredths"], [[B(int(w[0])), B(int(w[1])), B(int(w[2])), B(int(d[0])), B(int(d[1]))]], o="O1")
def p5(r):
    a, b = r.randint(10, 60), r.randint(1, 9)
    v = round(a / 10, 1)
    return N("What number is the arrow pointing to? The number line goes up in tenths.", v, o="O1", fig={"kind": "numline", "min": int(v), "max": int(v) + 1, "mark": v})
def p6(r):
    o, t, h = r.randint(1, 9), r.randint(0, 9), r.randint(1, 9)
    return N(f"Write as a decimal: {o} ones, {t} tenths and {h} hundredths.", round(o + t / 10 + h / 100, 2), o="O1")
def p7(r):
    v = dec(r, 1, 9, 2)
    return N(f"Find the missing number: {fmt(v)} × ☐ = {fmt(round(v * 100, 2))}", 100, o="O1", d="H")
def p8(r):
    xs = r.sample([round(r.randint(100, 999) / 100, 2) for _ in range(8)], 4)
    if len(set(xs)) < 4: return None
    return OD("Put these decimals in order, smallest first.", [fmt(x) for x in sorted(xs)], o="O1")
def p9(r):
    v = r.randint(2, 99); k = pick(r, [10, 100])
    return N(f"A pack of {k} stickers costs ${v}. How much does one sticker cost?", round(v / k, 2), "$", units=["$", "dollars"], o="O1", d="H")


def a51(r):
    return MC('Mo says 0.5 is smaller than 0.45 because 5 is smaller than 45. Is he right?', 'No: 0.5 = 0.50, which is bigger than 0.45', [('Yes', 'Compare tenths first: 5 tenths is more than 4 tenths.'), ('They are equal', 'Write 0.5 as 0.50.')], o='O1', d="H", reason='Line up the decimal points and compare the tenths.')


s.std([p4, p5, p1, p2, p3, p6, p8, p7, p9], EX("Explain why 3.5 × 10 = 35.", [("multiplying by 10 makes it 10 times bigger", "10 times|bigger"), ("each digit moves one place to the left", "one place|1 place|left")], "Multiplying by 10 makes the number 10 times bigger, so every digit moves one place to the left: 3.5 becomes 35.", o="O1"),
      deep=[a51])

s = U.section("1.2", "Rounding decimal numbers", ["O2"])
s.idea("Nearest whole number", ["To round a number with one decimal place to the nearest whole number, look at the **tenths** digit.",
       "If it is **5 or more**, round up. If it is less than 5, round down. 7.6 → 8 and 7.4 → 7. 7.5 rounds up to 8."], fig={"kind": "numline", "min": 7, "max": 8})
s.check(N("Round 12.7 to the nearest whole number.", 13, o="O2"))
s.check(MC('Before you read on: round 6.5 to the nearest whole number.', '7', [('6', '5 or more rounds up.'), ('6.5', 'A whole number has no decimal part.')], o='O2'))
s.mistake("Look at one digit only", ["To round 4.49 to the nearest whole number, look at the tenths digit, 4: it rounds down to 4."])


def r1(r):
    v = dec(r, 1, 99, 1)
    if v == int(v): return None
    return N(f"Round {fmt(v)} to the nearest whole number.", int(v + 0.5), o="O2")
def r2(r):
    w = r.randint(1, 30); v = round(w + r.randint(1, 9) / 10, 1)
    return N("The arrow points to a number. Round it to the nearest whole number.", int(v + 0.5), o="O2", fig={"kind": "numline", "min": w, "max": w + 1, "mark": v})
def r3(r):
    vs = [dec(r, 1, 20, 1) for _ in range(4)]
    return TB("Round each number to the nearest whole number.", ["Number", "Rounded"], [[fmt(v), B(int(v + 0.5))] for v in vs], o="O2")
def r4(r):
    w = r.randint(2, 40)
    return MS(f"Select ALL the numbers that round to {w}.", [fmt(w - 0.4), fmt(w + 0.2), fmt(w - 0.5)], [fmt(w + 0.5), fmt(w - 0.6), fmt(w + 0.9)], o="O2")
def r5(r):
    v = dec(r, 1, 30, 1)
    if v == int(v): return None
    return N(f"A pencil is {fmt(v)} cm long. How long is it to the nearest centimetre?", int(v + 0.5), "cm", units=["cm"], o="O2")
def r6(r):
    a, b = dec(r, 1, 10, 1), dec(r, 1, 10, 1)
    return N(f"Estimate {fmt(a)} + {fmt(b)} by rounding each number to the nearest whole number first.", int(a + 0.5) + int(b + 0.5), o="O2", d="H")
def r7(r):
    w = r.randint(3, 30)
    return N(f"A number with one decimal place rounds to {w}. What is the smallest it could be?", w - 0.5, o="O2", d="H")
def r8(r):
    v = dec(r, 1, 9, 2)
    return N(f"Round {fmt(v)} to the nearest whole number.", int(v + 0.5), o="O2")
def r9(r):
    w = r.randint(1, 20); xs = [round(w + d / 10, 1) for d in (1, 3, 4, 6, 8)]
    return GD(f"Does each number round to {w} or {w + 1}?", "Rounds to", [(fmt(x), str(int(x + 0.5))) for x in r.sample(xs, 4)], o="O2", extra=[str(w), str(w + 1)])


s.std([r2, r3, r1, r4, r5, r8, r9, r6, r7], EX("Explain how to round 6.5 to the nearest whole number.", [("look at the tenths digit, 5", "tenths|the 5"), ("5 or more rounds up, so 7", "round up|\\b7\\b")], "Look at the tenths digit, 5. When it is 5 or more we round up, so 6.5 rounds to 7.", o="O2"))

U.mindmap(("Place value", "Tenths • hundredths • × and ÷ by 10, 100", "O1", "1.1"), ("Rounding", "Look at the tenths • 5 or more rounds up", "O2", "1.2"))
