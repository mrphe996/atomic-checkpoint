# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 3 Place value and rounding (3.1 Multiplying and dividing by powers of 10, 3.2 Rounding).
Upgraded lesson (v2): why digits move, paired examples, prediction checks, and Practice built from decisions
(work backwards, find all, spot the error, bounds) rather than repeated routines. Written by the Atomic teaching team."""
from kit import *

U = Unit(3, "Place Value and Rounding", "Number",
         "Multiplying and dividing whole numbers and decimals by 10, 100 and 1000, and rounding to the nearest power of 10 and to decimal places.",
         {"O1": {"code": "7Np.01", "sec": "3.1", "codeNote": "", "t": "Multiply and divide integers and decimals by 10, 100 and 1000, using place value."},
          "O2": {"code": "7Np.02", "sec": "3.2", "codeNote": "", "t": "Round numbers to the nearest 10, 100 or 1000 and to a given number of decimal places."}})
P = [10, 100, 1000]
NLD = lambda lo, hi, m: {"kind": "numline", "min": lo, "max": hi, "mark": m}


def val(r): return pick(r, [r.randint(2, 999), r.randint(11, 999) / 10, r.randint(101, 9999) / 100])


# ================================================================== 3.1
s = U.section("3.1", "Multiplying and dividing by powers of 10", ["O1"])
s.idea("Moving digits", ["When you **multiply by 10**, every digit moves **one place to the left** (it becomes 10 times bigger). × 100 moves two places, × 1000 three places.",
       "When you **divide by 10**, every digit moves one place to the **right**. The decimal point stays still; the digits move."],
       table={"head": ["Thousands", "Hundreds", "Tens", "Ones", ".", "Tenths", "Hundredths"], "rows": [["", "", "3", "4", ".", "5", ""], ["", "3", "4", "5", ".", "", ""]]})
s.idea("Why the digits move", ["In 34.5 the 3 means 3 tens. Multiply by 10 and every part is ten times bigger: 3 tens become 3 hundreds, 4 ones become 4 tens, 5 tenths become 5 ones. So 34.5 × 10 = 345.",
       "Each column is worth 10 times the column on its right. Making a number 10 times bigger is exactly 'move one column left'."])
s.check(MC("Before you read on: what is 0.6 × 10?", "6", [("0.60", "Adding a zero after the decimal point does not change the value: 0.60 = 0.6."), ("60", "0.6 × 10 moves the 6 one place left, from tenths to ones."), ("0.06", "That divides by 10.")], o="O1", hint="6 tenths, made 10 times bigger."))
s.example("Using place value", "Work out 4.7 × 100 and 52 ÷ 1000.", [("4.7 × 100 = 470", "digits move 2 places left"), ("52 ÷ 1000 = 0.052", "digits move 3 places right")], "470 and 0.052",
          p=["Compare 4.7 × 100 = 470 with 4.7 ÷ 100 = 0.047: same digits, same number of places, opposite directions."])
s.check(N("Work out 3.8 × 1000.", 3800, o="O1"))
s.method("Multiplying or dividing by 10, 100 or 1000", ["Count the zeros: that is how many places the digits move.", "× moves the digits left (bigger); ÷ moves them right (smaller).", "Fill empty places before the decimal point with zeros, and check the size makes sense."])
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


def k1(r):   # which calculations give this answer (find all)
    a = pick(r, [3.6, 0.42, 7.5, 0.08, 2.15]); t = round(a * 100, 6)
    good = [f"{fmt(round(a, 6))} × 100", f"{fmt(round(a * 10, 6))} × 10", f"{fmt(round(a * 100000, 6))} ÷ 1000"]
    bad = [f"{fmt(round(a, 6))} × 10", f"{fmt(round(a * 1000, 6))} ÷ 1000"]
    return MS(f"Select ALL the calculations that equal {fmt(t)}.", good[:2] + [good[2]] if r.random() < .5 else good[:2], bad, o="O1", d="H", reason=f"Each must make the digits of {fmt(t)}: check how many places they move.")
def k2(r):   # spot the error
    a = pick(r, [2.5, 3.4, 6.08, 0.7]); k = pick(r, [10, 100])
    wrong = fmt(a) + "0" * (len(str(k)) - 1)
    return MC(f"Ben says {fmt(a)} × {k} = {wrong} because 'you add a zero for each zero'. What is the correct answer?", fmt(round(a * k, 6)),
              [(wrong, f"{wrong} has the same value as {fmt(a)} – zeros after the decimal point change nothing."), (fmt(round(a / k, 6)), "That divides."), (fmt(round(a * k * 10, 6)), "That moves one place too many.")],
              o="O1", d="H", reason=f"Multiplying by {k} moves every digit {len(str(k)) - 1} place{'s' if k > 10 else ''} left: {fmt(a)} → {fmt(round(a * k, 6))}.")
def k3(r):   # chain: undo
    a = r.randint(12, 98) / 10; k1_, k2_ = r.sample(P, 2)
    out = round(a * k1_ / k2_, 6)
    return N(f"Lin thinks of a number, multiplies it by {k1_}, then divides by {k2_}. The answer is {fmt(out)}. What was her number?", a, o="O1", d="H",
             hint="Undo the steps in reverse order.", reason=f"{fmt(out)} × {k2_} = {fmt(round(out * k2_, 6))}, then ÷ {k1_} = {fmt(a)}.")
def k4(r):   # how many times bigger
    a = pick(r, [0.035, 0.42, 7.2, 0.6]); k = pick(r, P)
    return N(f"How many times bigger is {fmt(round(a * k, 6))} than {fmt(a)}?", k, o="O1", d="H", reason=f"The digits have moved {len(str(k)) - 1} places left, so it is {k} times bigger.")
def k5(r):   # units decision
    rows = r.sample([("350 cm in metres", "3.5"), ("2.4 kg in grams", "2400"), ("75 mm in cm", "7.5"), ("0.6 km in m", "600"), ("4500 g in kg", "4.5"), ("0.25 m in cm", "25")], 4)
    return GD("Convert each measurement.", "Answer", rows, o="O1", d="H", extra=["0.35", "240"],
              reason="Decide first: a bigger unit gives a smaller number (divide); a smaller unit gives a bigger number (multiply). 1 m = 100 cm, 1 kg = 1000 g, 1 cm = 10 mm, 1 km = 1000 m.")


s.std([p4, p5, p1, p2, p3, p6, p7, p8, p9, p10, p11, p12], EX("Explain why 6.2 × 100 = 620.", [("multiplying by 100 makes the number 100 times bigger", ["100 times|bigger"]), ("each digit moves two places to the left", ["two places|2 places|left"])], "Multiplying by 100 makes the number 100 times bigger, so every digit moves two places to the left: 6.2 → 620.", o="O1"),
      deep=[k1, k2, k3, k4, k5])

# ================================================================== 3.2
s = U.section("3.2", "Rounding", ["O2"])
s.idea("Rounding rule", ["To round, look at the digit **after** the place you are rounding to. **5 or more: round up.** 4 or less: keep the digit.",
       "4837 to the nearest 100: look at the tens digit 3 → 4800. 6.374 to 1 decimal place: look at 7 → 6.4."])
s.idea("Rounding means 'which is nearer?'", ["4837 lies between 4800 and 4900. The halfway point is 4850. 4837 is below halfway, so it is nearer to 4800.",
       "The digit after the place you round to tells you which side of halfway you are on. A 5 is exactly halfway (or past it), and by agreement we round up."],
       table={"head": ["Number", "Between", "Halfway", "Nearer to"], "rows": [["4837", "4800 and 4900", "4850", "4800"], ["4862", "4800 and 4900", "4850", "4900"]]})
s.check(MC("Before you read on: 6.35 rounded to 1 decimal place is…", "6.4", [("6.3", "The next digit is 5, so round up."), ("6.0", "That rounds to the nearest whole number with the wrong digit."), ("6.35", "That has 2 decimal places.")], o="O2"))
s.example("One digit apart", "Round 3.849 and 3.851 to 1 decimal place.", [("3.849: next digit 4 → 3.8", "below halfway between 3.8 and 3.9"), ("3.851: next digit 5 → 3.9", "above halfway")], "3.8 and 3.9",
          p=["The numbers differ by only 0.002, but they lie either side of 3.85, the halfway point."])
s.check(N("Round 2659 to the nearest 100.", 2700, o="O2"))
s.check(N("Round 8.462 to 2 decimal places.", 8.46, o="O2"))
s.method("Rounding", ["Find the two possible answers either side of your number.", "Look at the next digit to decide which is nearer (5 or more: round up).", "Keep the place value: fill with zeros before the decimal point."])
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


def w1(r):   # find all that round to
    t = pick(r, [3.5, 7.2, 12.8]); lo = round(t - 0.05, 2)
    good = [fmt(round(lo + 0.01 * k, 2)) for k in r.sample(range(0, 10), 2)]
    bad = [fmt(round(lo - 0.01 * k, 2)) for k in r.sample(range(1, 5), 1)] + [fmt(round(t + 0.05 + 0.01 * k, 2)) for k in r.sample(range(0, 4), 1)]
    return MS(f"Select ALL the numbers that round to {fmt(t)} (1 decimal place).", good, bad, o="O2", d="H", reason=f"They must be at least {fmt(lo)} and less than {fmt(round(t + 0.05, 2))}.")
def w2(r):   # spot the error: rounding 9 up
    a = pick(r, [3.96, 7.97, 12.98, 0.95]); right = f"{a + 1e-9:.1f}"
    return MC(f"Amy rounds {fmt(a)} to 1 decimal place and writes {str(a)[:-2]}10. What should she write?", right,
              [(str(a)[:-2] + "10", "A digit cannot be 10: the extra ten tenths make one more whole."), (f"{a - 0.06:.1f}", "The next digit is 5 or more, so round up."), (str(int(a)), "That has no decimal place.")],
              o="O2", d="H", reason=f"{fmt(a)} is between {int(a * 10) / 10:.1f} and {right}; it is nearer to {right}.")
def w3(r):   # estimate sensibly: which estimate is closest
    a, b = r.randint(21, 89), r.randint(21, 89)
    e = round(a, -1) * round(b, -1)
    return MC(f"Without a calculator, which is the best estimate of {a} × {b}?", fmt(e), [(fmt(e * 10), "Too big by a factor of 10."), (fmt(round(a, -1) + round(b, -1)), "That adds instead of multiplying."), (fmt(e // 10), "Too small by a factor of 10.")],
              o="O2", d="H", reason=f"Round to {round(a, -1)} × {round(b, -1)} = {e}.")
def w4(r):   # bounds, decision
    t = r.randint(3, 9) * 1000
    return TB(f"A crowd is {fmt(t)} to the nearest 1000. Complete the table.", ["", "Number of people"], [["Smallest possible", B(t - 500)], ["Largest possible", B(t + 499)]], o="O2", d="H",
              reason=f"Halfway points are {fmt(t - 500)} and {fmt(t + 500)}. {fmt(t - 500)} rounds up to {fmt(t)}; {fmt(t + 500)} would round to {fmt(t + 1000)}, so the largest whole number is {fmt(t + 499)}.")
def w5(r):   # round then calculate vs calculate then round
    a, b = pick(r, [(2.46, 3.47), (1.44, 2.45), (4.35, 1.36), (0.46, 0.47)])
    return MC(f"Kim rounds {a} and {b} to 1 decimal place and then adds them. Lee adds them first and then rounds to 1 decimal place. Do they get the same answer?",
              "No" if round(round(a + 1e-9, 1) + round(b + 1e-9, 1), 1) != round(a + b + 1e-9, 1) else "Yes",
              [("Yes" if round(round(a + 1e-9, 1) + round(b + 1e-9, 1), 1) != round(a + b + 1e-9, 1) else "No", "Work out both ways and compare."), ("It is impossible to say", "You can work both out.")],
              o="O2", d="VH", reason=f"Kim: {round(a + 1e-9, 1)} + {round(b + 1e-9, 1)} = {round(round(a + 1e-9, 1) + round(b + 1e-9, 1), 1)}. Lee: {fmt(round(a + b, 2))} → {round(a + b + 1e-9, 1)}. Rounding early can change the answer.")


s.std([r4, r9, r1, r2, r3, r5, r6, r7, r8, r10, r11, r12, r13], EX("Explain how to round 7.85 to 1 decimal place.", [("look at the hundredths digit, 5", ["hundredth|second decimal|next digit|the 5"]), ("5 rounds up, so 7.9", ["7\\.9|round up"])], "Look at the digit after the first decimal place: it is 5. 5 or more rounds up, so 7.85 becomes 7.9.", o="O2"),
      deep=[w1, w2, w3, w4, w5])

U.mindmap(("Powers of 10", "× moves digits left • ÷ moves digits right", "O1", "3.1"), ("Rounding", "Look at the next digit • 5 or more rounds up", "O2", "3.2"))
