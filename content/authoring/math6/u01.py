# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 1 The number system (1.1 Place value, 1.2 Rounding decimal numbers).
Written by the Atomic teaching team."""
from kit import *

U = Unit(1, "The Number System", "Number",
         "Place value in whole numbers and decimals up to thousandths, multiplying and dividing by 10, 100 and 1000, and rounding decimals.",
         {"O1": {"code": "6Np.01", "sec": "1.1", "codeNote": "", "t": "Understand the value of each digit in whole numbers and decimals with up to three decimal places."},
          "O2": {"code": "6Np.02", "sec": "1.2", "codeNote": "", "t": "Round numbers with up to two decimal places to the nearest tenth or whole number."}})
PV = ["ten thousands", "thousands", "hundreds", "tens", "ones", "tenths", "hundredths", "thousandths"]
PVV = [10000, 1000, 100, 10, 1, 0.1, 0.01, 0.001]


def num(r):
    w = r.randint(1, 9999); d = r.randint(1, 999)
    return w + d / 1000


def digits(v):
    s = f"{v:.3f}"; w, d = s.split(".")
    return w, d


# ================================================================== 1.1
s = U.section("1.1", "Place value", ["O1"])
s.idea("Digits and places", ["Every digit has a **value** that depends on its **place**. In 4072.358 the 4 is worth 4000, the 7 is worth 70, the 3 is worth 3 tenths (0.3), the 5 is worth 5 hundredths (0.05) and the 8 is worth 8 thousandths (0.008).",
       "A zero holds a place: in 4072 there are no hundreds."],
       table={"head": ["Thousands", "Hundreds", "Tens", "Ones", ".", "Tenths", "Hundredths", "Thousandths"], "rows": [["4", "0", "7", "2", ".", "3", "5", "8"]]})
s.check(N("What is the value of the digit 6 in 3.462? Give your answer as a decimal.", 0.06, o="O1"))
s.idea("× and ÷ by 10, 100 and 1000", ["Multiplying by 10 moves every digit **one place to the left**; dividing by 10 moves every digit one place to the right. × 100 and ÷ 100 move two places; × 1000 and ÷ 1000 move three places."])
s.example("Moving digits", "Work out 3.75 × 100 and 52 ÷ 1000.", [("3.75 × 100 = 375", "digits move 2 places left"), ("52 ÷ 1000 = 0.052", "digits move 3 places right")], "375 and 0.052")
s.mistake("Zeros keep places", ["0.5 and 0.05 are not the same: the 5 is in a different place."])


def p1(r):
    ds = [r.randint(1, 9) for _ in range(7)]          # thousands … thousandths, no zeros
    v = round(sum(d * w for d, w in zip(ds, PVV[1:])), 3); k = r.randrange(7)
    return N(f"What is the value of the digit {ds[k]} in {fmt(v)}?", round(ds[k] * PVV[1 + k], 3), o="O1", reason=f"It is in the {PV[1 + k]} place.") if ds.count(ds[k]) == 1 else None
def p2(r):
    v = round(r.randint(100, 99999) / 100, 2); k = pick(r, [10, 100, 1000])
    return N(f"Work out {fmt(v)} × {k}.", round(v * k, 4), o="O1")
def p3(r):
    v = r.randint(2, 9999); k = pick(r, [10, 100, 1000])
    return N(f"Work out {v} ÷ {k}.", v / k, o="O1")
def p4(r):
    a, b, c, d = r.randint(1, 9), r.randint(0, 9), r.randint(1, 9), r.randint(1, 9)
    v = a * 10 + b + c / 10 + d / 100
    return TB(f"Write {fmt(v)} in the place value table.", ["Tens", "Ones", "Tenths", "Hundredths"], [[B(a), B(b), B(c), B(d)]], o="O1")
def p5(r):
    a, b, c = r.randint(1, 9), r.randint(1, 9), r.randint(1, 9); w = r.randint(1, 99)
    return N(f"Write as a decimal: {w} + {fmt(a / 10)} + {fmt(b / 100)} + {fmt(c / 1000)}", round(w + a / 10 + b / 100 + c / 1000, 3), o="O1")
def p6(r):
    rows = [("0.4", "4 tenths"), ("0.04", "4 hundredths"), ("0.004", "4 thousandths"), ("40", "4 tens"), ("400", "4 hundreds")]
    return GD("What is each number worth?", "Value", r.sample(rows, 4), o="O1")
def p7(r):
    v = round(r.randint(100, 9999) / 1000, 3); k = pick(r, [10, 100, 1000])
    return N(f"Find the missing number: {fmt(v)} × ☐ = {fmt(round(v * k, 3))}", k, o="O1", d="H")
def p8(r):
    m = r.randint(105, 990) / 100
    return N(f"A ribbon is {fmt(m)} m long. How long is it in centimetres? (1 m = 100 cm)", round(m * 100), "cm", units=["cm"], o="O1")
def p9(r):
    v = r.randint(1000, 9999) / 1000
    return MS(f"Select ALL the numbers that are 10 times bigger than {fmt(v)}.", [fmt(round(v * 10, 3))], [fmt(round(v * 100, 3)), fmt(round(v / 10, 4)), fmt(round(v + 10, 3))], o="O1")


s.std([p4, p6, p1, p2, p3, p5, p7, p8, p9], EX("Explain why 0.3 is ten times bigger than 0.03.", [("the 3 is in the tenths place in 0.3", ["tenth"]), ("and in the hundredths place in 0.03; a tenth is 10 hundredths", ["hundredth|10 times|one place"])], "In 0.3 the 3 is worth 3 tenths, but in 0.03 it is worth 3 hundredths. One tenth is 10 hundredths, so 0.3 is ten times bigger.", o="O1"))

# ================================================================== 1.2
s = U.section("1.2", "Rounding decimal numbers", ["O2"])
s.idea("Rounding", ["To round to the **nearest whole number**, look at the tenths digit. To round to **one decimal place** (the nearest tenth), look at the hundredths digit.",
       "**5 or more**: round up. **4 or less**: round down."], fig={"kind": "numline", "min": 3, "max": 5})
s.example("Nearest tenth", "Round 6.47 to one decimal place.", [("6.47 is between 6.4 and 6.5", ""), ("the hundredths digit is 7, so round up", "")], "6.5")
s.check(N("Round 8.36 to the nearest whole number.", 8, o="O2"))
s.mistake("Rounding up 9", ["4.96 to one decimal place is 5.0, because 4.9 + 0.1 = 5.0."])


def r1(r):
    v = round(r.uniform(1, 99), 1)
    return N(f"Round {fmt(v)} to the nearest whole number.", int(v + 0.5), o="O2")
def r2(r):
    v = round(r.uniform(1, 50), 2)
    if abs(v * 10 - round(v * 10)) < 1e-9: return None
    return N(f"Round {fmt(v)} to one decimal place.", round(v + 1e-9, 1), o="O2")
def r3(r):
    v = round(r.uniform(1, 20), 2)
    return TB(f"Round {fmt(v)}.", ["To the nearest", "Answer"], [["whole number", B(int(v + 0.5))], ["tenth", B(round(v + 1e-9, 1))]], o="O2")
def r4(r):
    a = r.randint(2, 9)
    v = round(a + r.randint(1, 9) / 10, 1)
    return N(f"The arrow points to {fmt(v)} on the number line. Round it to the nearest whole number.", int(v + 0.5), o="O2", fig={"kind": "numline", "min": a - 1, "max": a + 2, "from": {"v": v, "closed": True}, "to": {"v": v, "closed": True}})
def r5(r):
    m = round(r.uniform(1, 3), 2)
    return N(f"A girl is {fmt(m)} m tall. Round her height to one decimal place.", round(m + 1e-9, 1), "m", units=["m"], o="O2")
def r6(r):
    lo = r.randint(2, 9)
    vals = [round(lo + x / 100, 2) for x in r.sample(range(1, 99), 4)]
    return GD(f"Does each number round to {lo} or {lo + 1} (nearest whole number)?", "Rounds to", [(fmt(v), str(int(v + 0.5))) for v in vals], o="O2")
def r7(r):
    p = round(r.uniform(1, 9), 2)
    return MC(f"Which is {fmt(p)} rounded to one decimal place?", f"{p + 1e-9:.1f}", [f"{p:.2f}", str(int(p + 0.5)), f"{p - 0.1:.1f}" if f"{p - 0.1:.1f}" != f"{p + 1e-9:.1f}" else f"{p + 0.2:.1f}"], o="O2")
def r8(r):
    a = r.randint(2, 9)
    return N(f"A number has one decimal place and rounds to {a} (nearest whole number). What is the smallest it could be?", a - 0.5, o="O2", d="H")


s.std([r3, r4, r1, r2, r5, r6, r7, r8], EX("Explain how to round 7.85 to one decimal place.", [("look at the hundredths digit, 5", ["hundredth|the 5|next digit"]), ("5 or more rounds up: 7.9", ["7\\.9|round up"])], "Look at the hundredths digit, which is 5. Five or more rounds up, so 7.85 becomes 7.9.", o="O2"))

U.mindmap(("Place value", "Thousands to thousandths • × and ÷ by 10, 100, 1000", "O1", "1.1"), ("Rounding", "Look at the next digit • 5 or more rounds up", "O2", "1.2"))
