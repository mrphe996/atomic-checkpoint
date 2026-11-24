# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 3 Place value and rounding (3.1 Multiplying and dividing by powers of 10, 3.2 Rounding).
Written by the Atomic teaching team."""
from kit import *

U = Unit(3, "Place Value and Rounding", "Number",
         "Multiplying and dividing whole numbers and decimals by 10, 100 and 1000, and rounding to the nearest power of 10 and to decimal places.",
         {"O1": {"code": "7Np.01", "sec": "3.1", "codeNote": "", "t": "Multiply and divide integers and decimals by 10, 100 and 1000, using place value."},
          "O2": {"code": "7Np.02", "sec": "3.2", "codeNote": "", "t": "Round numbers to the nearest 10, 100 or 1000 and to a given number of decimal places."}})
P = [10, 100, 1000]


def val(r): return pick(r, [r.randint(2, 999), r.randint(11, 999) / 10, r.randint(101, 9999) / 100])


# ================================================================== 3.1
s = U.section("3.1", "Multiplying and dividing by powers of 10", ["O1"])
s.idea("Moving digits", ["When you **multiply by 10**, every digit moves **one place to the left** (it becomes 10 times bigger). × 100 moves two places, × 1000 three places.",
       "When you **divide by 10**, every digit moves one place to the **right**. The decimal point stays still; the digits move."],
       table={"head": ["Thousands", "Hundreds", "Tens", "Ones", ".", "Tenths", "Hundredths"], "rows": [["", "", "3", "4", ".", "5", ""], ["", "3", "4", "5", ".", "", ""]]})
s.example("Using place value", "Work out 4.7 × 100 and 52 ÷ 1000.", [("4.7 × 100 = 470", "digits move 2 places left"), ("52 ÷ 1000 = 0.052", "digits move 3 places right")], "470 and 0.052")
s.check(N("Work out 3.8 × 1000.", 3800, o="O1"))
s.mistake("Not just adding zeros", ["2.5 × 10 is 25, not 2.50. Think of the digits moving."])


def p1(r):
    v, k = val(r), pick(r, P)
    return N(f"Work out {fmt(v)} × {k}.", round(v * k, 6), o="O1")
def p2(r):
    v, k = val(r), pick(r, P)
    return N(f"Work out {fmt(v)} ÷ {k}.", round(v / k, 6), o="O1")
def p3(r):
    v, k = val(r), pick(r, P); op = pick(r, ["×", "÷"]); a = round(v * k if op == "×" else v / k, 6)
    return N(f"Find the missing number: {fmt(v)} {op} ☐ = {fmt(a)}", k, o="O1", d="H")
def p4(r):
    v = val(r)
    return TB(f"Complete the table for {fmt(v)}.", ["Calculation", "Answer"], [[f"{fmt(v)} × 10", B(round(v * 10, 6))], [f"{fmt(v)} × 100", B(round(v * 100, 6))], [f"{fmt(v)} ÷ 10", B(round(v / 10, 6))]], o="O1")
def p5(r):
    rows = [("4.5 × 10", "45"), ("450 ÷ 100", "4.5"), ("0.45 × 1000", "450"), ("45 ÷ 1000", "0.045"), ("4.5 ÷ 10", "0.45")]
    return GD("Find each answer.", "Answer", r.sample(rows, 4), o="O1", extra=["4500"])
def p6(r):
    m = r.randint(12, 950) / 100
    return N(f"A rope is {fmt(m)} m long. How long is it in centimetres? (1 m = 100 cm)", round(m * 100, 4), "cm", units=["cm"], o="O1")
def p7(r):
    g = r.randint(150, 9500)
    return N(f"A parcel has a mass of {g} g. What is its mass in kilograms? (1 kg = 1000 g)", g / 1000, "kg", units=["kg"], o="O1")
def p8(r):
    p = r.randint(15, 99) / 100; n = pick(r, [10, 100, 1000])
    return N(f"One pen costs ${fmt(p)}. How much do {n} pens cost?", round(p * n, 4), "$", units=["$"], o="O1")
def p9(r):
    v = r.randint(2, 99)
    return MC(f"Which calculation gives the biggest answer?", f"{v} × 1000", [f"{v} × 100", f"{v} ÷ 10", f"{v} × 10"], o="O1")
def p10(r):
    v = r.randint(10, 99) / 10
    return N(f"Work out {fmt(v)} × 10 ÷ 100.", round(v / 10, 6), o="O1", d="H", reason="× 10 then ÷ 100 is the same as ÷ 10.")


def p11(r):
    l = r.randint(12, 95) / 10; n = pick(r, [10, 100])
    return N(f"A stack of {n} identical books is {fmt(round(l * n, 4))} cm tall. How thick is one book?", l, "cm", units=["cm"], o="O1", d="H")
def p12(r):
    k = r.randint(2, 9) * 100 + r.randint(1, 99)
    return N(f"Write {k} g in kilograms.", k / 1000, "kg", units=["kg"], o="O1")


s.std([p4, p5, p1, p2, p3, p6, p7, p8, p9, p10, p11, p12], EX("Explain why 6.2 × 100 = 620.", [("multiplying by 100 makes the number 100 times bigger", ["100 times|bigger"]), ("each digit moves two places to the left", ["two places|2 places|left"])], "Multiplying by 100 makes the number 100 times bigger, so every digit moves two places to the left: 6.2 → 620.", o="O1"))

# ================================================================== 3.2
s = U.section("3.2", "Rounding", ["O2"])
s.idea("Rounding rule", ["To round, look at the digit **after** the place you are rounding to. **5 or more: round up.** 4 or less: keep the digit.",
       "4837 to the nearest 100: look at the tens digit 3 → 4800. 6.374 to 1 decimal place: look at 7 → 6.4."])
s.check(N("Round 2659 to the nearest 100.", 2700, o="O2"))
s.check(N("Round 8.462 to 2 decimal places.", 8.46, o="O2"))
s.mistake("Keep the place values", ["4837 to the nearest 100 is 4800, not 48."])


def r1(r):
    n = r.randint(100, 99999); k = pick(r, [10, 100, 1000])
    return N(f"Round {fmt(n)} to the nearest {k}.", int(n / k + 0.5) * k, o="O2")
def r2(r):
    v = round(r.uniform(1, 99), 3); d = r.randint(1, 2)
    return N(f"Round {fmt(v)} to {d} decimal place{'s' if d > 1 else ''}.", float(f"{v + 1e-9:.{d}f}"), o="O2")
def r3(r):
    v = round(r.uniform(1, 50), 2)
    return N(f"Round {fmt(v)} to the nearest whole number.", int(v + 0.5), o="O2")
def r4(r):
    n = r.randint(1000, 9999)
    return TB(f"Round {fmt(n)} to the nearest:", ["Accuracy", "Answer"], [["10", B(int(n / 10 + 0.5) * 10)], ["100", B(int(n / 100 + 0.5) * 100)], ["1000", B(int(n / 1000 + 0.5) * 1000)]], o="O2")
def r5(r):
    v = round(r.uniform(2, 20), 3)
    return MC(f"Which is {fmt(v)} rounded to 1 decimal place?", f"{v + 1e-9:.1f}", [f"{v + 0.1:.1f}", f"{v:.2f}" if f"{v:.2f}" != f"{v + 1e-9:.1f}" else f"{v - 0.1:.1f}", str(int(v + 0.5))], o="O2")
def r6(r):
    p = r.randint(12000, 98000)
    return N(f"{fmt(p)} people watched a match. Round this to the nearest thousand.", int(p / 1000 + 0.5) * 1000, "people", units=["people"], o="O2")
def r7(r):
    a, b = r.randint(21, 89), r.randint(21, 89)
    return N(f"Estimate {a} × {b} by rounding each number to the nearest 10.", int(a / 10 + 0.5) * 10 * int(b / 10 + 0.5) * 10, o="O2", d="H")
def r8(r):
    lo = r.randint(2, 9) * 100
    return N(f"A number rounds to {lo} to the nearest 100. What is the smallest whole number it could be?", lo - 50, o="O2", d="H")
def r9(r):
    rows = [("3.46 → 1 d.p.", "3.5"), ("3.44 → 1 d.p.", "3.4"), ("3.449 → 2 d.p.", "3.45"), ("3.995 → 2 d.p.", "4.00"), ("3.05 → 1 d.p.", "3.1")]
    return GD("Round each number.", "Rounded", r.sample(rows, 4), o="O2", extra=["3.0"])
def r10(r):
    c = round(r.uniform(1, 9), 2); n = r.randint(3, 9)
    return N(f"{n} friends share ${fmt(round(c * n + 0.01, 2))}. How much does each get, to the nearest cent?", round((c * n + 0.01) / n, 2), "$", units=["$"], o="O2", d="H", tol=0.005)


def r11(r):
    hi = r.randint(2, 9) * 1000
    return N(f"A number rounds to {fmt(hi)} to the nearest 1000. What is the largest whole number it could be?", hi + 499, o="O2", d="H")
def r12(r):
    a, b = r.randint(110, 890), r.randint(21, 89)
    ea, eb = int(a / 100 + 0.5) * 100, int(b / 10 + 0.5) * 10
    return N(f"Estimate {a} × {b} by rounding {a} to the nearest 100 and {b} to the nearest 10.", ea * eb, o="O2", d="H")
def r13(r):
    v = round(r.uniform(10, 99), 2); c = round(r.uniform(10, 99), 2)
    return N(f"Two lengths are {fmt(v)} m and {fmt(c)} m. Find their total, rounded to 1 decimal place.", round(v + c + 1e-9, 1), "m", units=["m"], o="O2", d="H", tol=0.0001)


s.std([r4, r9, r1, r2, r3, r5, r6, r7, r8, r10, r11, r12, r13], EX("Explain how to round 7.85 to 1 decimal place.", [("look at the hundredths digit, 5", ["hundredth|second decimal|next digit|the 5"]), ("5 rounds up, so 7.9", ["7\\.9|round up"])], "Look at the digit after the first decimal place: it is 5. 5 or more rounds up, so 7.85 becomes 7.9.", o="O2"))

U.mindmap(("Powers of 10", "× moves digits left • ÷ moves digits right", "O1", "3.1"), ("Rounding", "Look at the next digit • 5 or more rounds up", "O2", "3.2"))
