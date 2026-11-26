# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 10 Percentages (10.1 Percentage increases and decreases, 10.2 Using a multiplier).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(10, "Percentages", "Number",
         "Increasing and decreasing amounts by a percentage, finding a change as a percentage, and using decimal multipliers.",
         {"O1": {"code": "8Nf.11", "sec": "10.1", "codeNote": "", "t": "Increase and decrease an amount by a percentage, and express a change as a percentage."},
          "O2": {"code": "8Nf.12", "sec": "10.2", "codeNote": "", "t": "Use a decimal multiplier to calculate percentage increases and decreases."}})
ITEMS = [("a bike", 120, 400), ("a phone", 150, 900), ("a jacket", 40, 160), ("a game", 20, 80), ("a tent", 60, 300), ("a watch", 50, 250)]
PCS = [5, 10, 12, 15, 20, 25, 30, 35, 40, 60, 75]
m2 = lambda v: round(v, 2)

# ================================================================== 10.1
s = U.section("10.1", "Percentage increases and decreases", ["O1"])
s.idea("Increase and decrease", ["To **increase** an amount by a percentage, find the percentage and **add** it. To **decrease**, find it and **subtract** it.",
       "Increase $80 by 15%: 15% of 80 = 12, so 80 + 12 = $92."])
s.example("A sale", "A coat costs $64. It is reduced by 25% in a sale. Find the sale price.", [("25% of 64 = 16", "¼ of 64"), ("64 − 16 = 48", "")], "$48")
s.check(N("Increase 250 by 12%.", 280, o="O1", reason="12% of 250 = 30; 250 + 30 = 280."))
s.idea("Percentage change", ["**Percentage change = change ÷ original amount × 100**.",
       "A price goes from $50 to $62: change = 12, 12 ÷ 50 × 100 = 24% increase."])
s.check(N("A plant grows from 40 cm to 46 cm. Find the percentage increase.", 15, "%", units=["%"], o="O1"))
s.idea("Why the order of increases matters", ["A 10% increase followed by a 10% decrease does NOT bring you back. $100 → $110 → $99, because the second 10% is of $110, not $100.",
       "Always ask: a percentage OF WHAT?"])
s.check(MC("Before you read on: a price rises by 20% and then falls by 20%. Is it back to the start?", "No – it is 4% lower", [("Yes", "The fall is 20% of a bigger amount."), ("No – it is higher", "100 → 120 → 96.")], o="O1"))
s.mistake("Divide by the original", ["The percentage change is worked out from the ORIGINAL amount, not the new one."])


def p1(r):
    it, lo, hi = pick(r, ITEMS); p = r.randint(lo // 10, hi // 10) * 10; pc = pick(r, PCS)
    return N(f"{it.capitalize()} costs ${p}. Its price increases by {pc}%. Find the new price.", m2(p * (1 + pc / 100)), "$", units=["$"], o="O1", tol=0.005, reason=f"{pc}% of {p} = {fmt(m2(p * pc / 100))}; {p} + {fmt(m2(p * pc / 100))} = {fmt(m2(p * (1 + pc / 100)))}.")
def p2(r):
    it, lo, hi = pick(r, ITEMS); p = r.randint(lo // 10, hi // 10) * 10; pc = pick(r, PCS)
    return N(f"{it.capitalize()} costs ${p}. In a sale the price is reduced by {pc}%. Find the sale price.", m2(p * (1 - pc / 100)), "$", units=["$"], o="O1", tol=0.005, reason=f"{pc}% of {p} = {fmt(m2(p * pc / 100))}; {p} − {fmt(m2(p * pc / 100))} = {fmt(m2(p * (1 - pc / 100)))}.")
def p3(r):
    a = r.randint(4, 40) * 5; pc = pick(r, [10, 20, 25, 30, 40, 50, 15, 5]); b = a * (100 + pc) // 100 if (a * pc) % 100 == 0 else None
    if b is None: return None
    return N(f"The number of members of a club goes up from {a} to {b}. Find the percentage increase.", pc, "%", units=["%"], o="O1", reason=f"Change {b - a}; {b - a} ÷ {a} × 100 = {pc}%.")
def p4(r):
    a = r.randint(4, 40) * 10; pc = pick(r, [10, 20, 25, 30, 40, 50, 15, 5]); b = a - a * pc // 100
    if (a * pc) % 100: return None
    return N(f"A car's value falls from ${a} to ${b}. Find the percentage decrease.", pc, "%", units=["%"], o="O1", d="H", reason=f"Change {a - b}; {a - b} ÷ {a} × 100 = {pc}%.")
def p5(r):
    m = r.randint(40, 90); t = m + r.randint(5, 30)
    return N(f"Sam scored {m} in a test and {t} in the next one. Find the percentage increase, to 1 d.p.", round((t - m) / m * 100, 1), "%", units=["%"], o="O1", d="H", tol=0.05, reason=f"{t - m} ÷ {m} × 100 ≈ {round((t - m) / m * 100, 1)}%.")
def p6(r):
    p = r.randint(10, 60) * 10; pcs = r.sample(PCS, 2)
    return TB(f"A price is ${p}. Complete the table.", ["Change", "New price ($)"], [[f"Increase by {pcs[0]}%", B(m2(p * (1 + pcs[0] / 100)), 0.005)], [f"Decrease by {pcs[1]}%", B(m2(p * (1 - pcs[1] / 100)), 0.005)]], o="O1")
def p7(r):
    a, b = r.randint(20, 80), r.randint(20, 80)
    if a == b: return None
    nm = ["January", "February"]
    return N(f"A shop sold {a} bikes in January and {b} in February. Find the percentage {'increase' if b > a else 'decrease'}, to 1 d.p.", round(abs(b - a) / a * 100, 1), "%", units=["%"], o="O1", d="H", tol=0.05, data={"head": ["Month", *nm], "rows": [["Bikes sold", str(a), str(b)]]})
def p8(r):
    p = r.randint(20, 80) * 10; pc = pick(r, [10, 20, 25])
    return MC(f"A price of ${p} is increased by {pc}% and then the new price is decreased by {pc}%. What is the final price?", f"${fmt(m2(p * (1 + pc / 100) * (1 - pc / 100)))}", [(f"${p}", "The decrease is worked out on the bigger, new price."), (f"${fmt(m2(p * (1 - pc / 100)))}", ""), (f"${fmt(m2(p * (1 + pc / 100)))}", "")], o="O1", d="VH")
def p9(r):
    s_ = r.randint(15, 45) * 100; pc = pick(r, [2, 3, 4, 5, 6])
    return N(f"A worker earns ${fmt(s_)} a month. She gets a {pc}% pay rise. How much does she earn now?", s_ * (100 + pc) / 100, "$", units=["$"], o="O1", reason=f"{pc}% of {s_} = {fmt(s_ * pc / 100)}.")
def p10(r):
    rows = [("Increase 40 by 50%", "60"), ("Decrease 40 by 25%", "30"), ("Increase 80 by 10%", "88"), ("Decrease 80 by 50%", "40"), ("Increase 60 by 20%", "72"), ("Decrease 60 by 10%", "54")]
    return GD("Find each answer.", "Answer", r.sample(rows, 4), o="O1", extra=["50", "90"])


def p11(r):
    it, lo, hi = pick(r, ITEMS); p = r.randint(lo // 10, hi // 10) * 10; pc = pick(r, PCS)
    return N(f"{it.capitalize()} costs ${p}. There is {pc}% off. How much money do you save?", m2(p * pc / 100), "$", units=["$"], o="O1", tol=0.005, reason=f"{pc}% of {p} = {fmt(m2(p * pc / 100))}.")
def p12(r):
    b = r.randint(10, 80) * 5; pc = pick(r, [10, 20, 25, 40, 50]); s_ = b * (100 + pc) // 100
    if (b * pc) % 100: return None
    return N(f"A trader buys a bike for ${b} and sells it for ${s_}. Find the percentage profit.", pc, "%", units=["%"], o="O1", d="H", reason=f"Profit {s_ - b}; {s_ - b} ÷ {b} × 100 = {pc}%.")
def p13(r):
    a = r.randint(1200, 9000); b = a - r.randint(50, 800)
    return N(f"A town's population falls from {fmt(a)} to {fmt(b)}. Find the percentage decrease, to 1 d.p.", round((a - b) / a * 100, 1), "%", units=["%"], o="O1", d="H", tol=0.05, reason=f"{a - b} ÷ {fmt(a)} × 100 ≈ {round((a - b) / a * 100, 1)}%.")
def p14(r):
    p = r.randint(8, 30) * 10; pc = pick(r, [10, 15, 20, 25]); off = r.randint(2, 8) * 5
    a, b = p * (1 - pc / 100), p - off
    if a == b: return None
    return MC(f"A ${p} jacket is on sale. Shop A takes {pc}% off. Shop B takes ${off} off. Which is cheaper?", "Shop A" if a < b else "Shop B", [("Shop B" if a < b else "Shop A", f"Shop A: ${fmt(m2(a))}; Shop B: ${fmt(b)}."), ("They are the same", "")], o="O1", reason=f"Shop A: ${fmt(m2(a))}; Shop B: ${fmt(b)}.")
def p15(r):
    w = r.randint(30, 90) / 10; pc = pick(r, [5, 10, 15, 20])
    return N(f"A puppy has a mass of {fmt(w)} kg. It gains {pc}% in a month. What is its new mass in kg?", m2(w * (1 + pc / 100)), "kg", units=["kg"], o="O1", tol=0.005, reason=f"{fmt(w)} × {fmt(1 + pc / 100)} = {fmt(m2(w * (1 + pc / 100)))} kg.")


def f101(r):
    p = pick(r, [10, 20, 25, 50]); v = pick(r, [80, 120, 200, 400])
    return N(f"A price of ${v} rises by {p}% and then falls by {p}%. What is the final price?", round(v * (1 + p / 100) * (1 - p / 100), 2), "$", units=["$"], o="O1", d="H",
             reason=f"{v} × {1 + p / 100:g} = {v * (1 + p / 100):g}; × {1 - p / 100:g} = {v * (1 + p / 100) * (1 - p / 100):g}.")


s.std([p6, p7, p1, p2, p3, p9, p10, p4, p5, p8, p11, p12, p13, p14, p15], EX("Explain how to find the percentage increase when a price rises from $40 to $50.", [("the change is $10", ["\\b10\\b|change"]), ("divide by the original 40 and multiply by 100: 25%", ["25|÷ ?40|original"])], "The change is $50 − $40 = $10. Divide by the original price and multiply by 100: 10 ÷ 40 × 100 = 25%.", o="O1"),
      deep=[f101])

# ================================================================== 10.2
s = U.section("10.2", "Using a multiplier", ["O2"])
s.idea("Multipliers", ["An increase of 15% means you have 100% + 15% = 115% of the amount, so **multiply by 1.15**.",
       "A decrease of 15% means you have 85% left, so **multiply by 0.85**. One multiplication does the whole job."],
       table={"head": ["Change", "Multiplier"], "rows": [["+ 20%", "1.2"], ["+ 5%", "1.05"], ["− 30%", "0.7"], ["− 3%", "0.97"]]})
s.example("With a multiplier", "Decrease $260 by 35%.", [("100% − 35% = 65% → 0.65", ""), ("260 × 0.65 = 169", "")], "$169")
s.check(N("What decimal multiplier increases an amount by 8%?", 1.08, o="O2"))
s.idea("Why a multiplier works", ["Increasing by 15% means keeping 100% and adding 15%: 115% = 1.15. So the new amount is 1.15 × the old one, in one step.",
       "A decrease of 15% leaves 85% = 0.85."])
s.check(MC("Before you read on: what multiplier decreases an amount by 8%?", "0.92", [("0.08", "That finds the 8%, not what is left."), ("1.08", "That is an increase.")], o="O2"))
s.mistake("1.5 is not 5%", ["An increase of 5% is × 1.05, not × 1.5 (that is a 50% increase)."])


def u1(r):
    pc = r.randint(1, 60); inc = r.random() < 0.5
    return N(f"What decimal multiplier {'increases' if inc else 'decreases'} an amount by {pc}%?", round(1 + pc / 100 if inc else 1 - pc / 100, 2), o="O2", reason=f"{100 + pc if inc else 100 - pc}% = {fmt(round(1 + pc / 100 if inc else 1 - pc / 100, 2))}.")
def u2(r):
    a = r.randint(20, 900); pc = pick(r, [3, 7, 12, 17, 23, 35, 45]); inc = r.random() < 0.5
    m = 1 + pc / 100 if inc else 1 - pc / 100
    return N(f"Use a multiplier to {'increase' if inc else 'decrease'} {a} by {pc}%.", m2(a * m), o="O2", tol=0.005, reason=f"{a} × {fmt(round(m, 2))} = {fmt(m2(a * m))}.")
def u3(r):
    m = pick(r, [1.04, 1.15, 1.3, 0.9, 0.75, 0.62, 1.5, 0.97, 2.0])
    pc = round(abs(m - 1) * 100)
    return MC(f"Multiplying by {fmt(m)} is the same as…", f"{'an increase' if m > 1 else 'a decrease'} of {pc}%", [f"{'a decrease' if m > 1 else 'an increase'} of {pc}%", f"{'an increase' if m > 1 else 'a decrease'} of {fmt(m)}%", f"{'an increase' if m > 1 else 'a decrease'} of {round(m * 100)}%"], o="O2")
def u4(r):
    rows = [("Increase by 10%", "1.1"), ("Decrease by 10%", "0.9"), ("Increase by 25%", "1.25"), ("Decrease by 25%", "0.75"), ("Increase by 3%", "1.03"), ("Decrease by 40%", "0.6")]
    return GD("Choose the multiplier for each change.", "Multiplier", r.sample(rows, 4), o="O2", extra=["1.3", "0.3"])
def u5(r):
    p = r.randint(50, 500); pc = pick(r, [5, 10, 15, 20]); y = r.randint(2, 3)
    return N(f"A house plant costs ${p}. Its price rises by {pc}% each year for {y} years. Find its price after {y} years, to the nearest cent.", m2(p * (1 + pc / 100) ** y), "$", units=["$"], o="O2", d="VH", tol=0.006, reason=f"{p} × {fmt(1 + pc / 100)}^{y} = {fmt(m2(p * (1 + pc / 100) ** y))}.")
def u6(r):
    p = r.randint(20, 300); m = pick(r, [1.1, 1.2, 1.25, 0.8, 0.9, 0.75])
    return TB("Complete the table.", ["Original", "Multiplier", "New amount"], [[str(p), fmt(m), B(m2(p * m), 0.005)]], o="O2", data={"head": ["Change", "Multiplier"], "rows": [["+10%", "1.1"], ["−20%", "0.8"]]})
def u7(r):
    a = r.randint(10, 80) * 10; m = pick(r, [0.8, 0.9, 1.1, 1.2, 1.25, 0.75])
    return N(f"After a change, a value is {fmt(m2(a * m))}. The multiplier used was {fmt(m)}. What was the original value?", a, o="O2", d="VH", reason=f"{fmt(m2(a * m))} ÷ {fmt(m)} = {a}.")
def u8(r):
    p = r.randint(40, 200); pc = pick(r, [15, 20, 12])
    return N(f"A meal costs ${p} before a {pc}% service charge is added. Use a multiplier to find the total cost.", m2(p * (1 + pc / 100)), "$", units=["$"], o="O2", tol=0.005, reason=f"{p} × {fmt(1 + pc / 100)} = {fmt(m2(p * (1 + pc / 100)))}.")
def u9(r):
    a, b = r.randint(100, 500), r.randint(2, 30)
    return N(f"A population of {a} birds falls by {b}% this year. Use a multiplier to find the new population (nearest whole bird).", round(a * (1 - b / 100)), "birds", units=["birds"], o="O2", tol=0.5, reason=f"{a} × {fmt(1 - b / 100)} ≈ {round(a * (1 - b / 100))}.")


def u10(r):
    a, b = pick(r, [10, 20, 25, 30, 50]), pick(r, [10, 20, 40])
    m = round((1 + a / 100) * (1 - b / 100), 4)
    return N(f"A price is increased by {a}% and then decreased by {b}%. What single multiplier has the same effect?", m, o="O2", d="VH", tol=0.00005, reason=f"{fmt(1 + a / 100)} × {fmt(1 - b / 100)} = {fmt(m)}.")
def u11(r):
    m = pick(r, [1.08, 1.35, 0.88, 0.65, 1.125, 0.95, 1.6]); pc = round(abs(m - 1) * 100, 1)
    return N(f"A value is multiplied by {fmt(m)}. By what percentage has it {'increased' if m > 1 else 'decreased'}?", pc, "%", units=["%"], o="O2", reason=f"{fmt(m)} = {fmt(m * 100)}%, a change of {fmt(pc)}%.")
def u12(r):
    a = r.randint(2, 50) * 100; pc = pick(r, [2, 3, 4, 5])
    return N(f"${fmt(a)} is saved in a bank that adds {pc}% interest at the end of the year. Use a multiplier to find the amount after 1 year.", a * (100 + pc) / 100, "$", units=["$"], o="O2", reason=f"{a} × {fmt(1 + pc / 100)} = {fmt(a * (100 + pc) / 100)}.")
def u13(r):
    p = r.randint(10, 200); t = pick(r, [5, 7, 8, 10, 15, 20])
    return N(f"Sales tax of {t}% is added to a price of ${p}. Use a multiplier to find the price including tax.", m2(p * (1 + t / 100)), "$", units=["$"], o="O2", tol=0.005, reason=f"{p} × {fmt(1 + t / 100)} = {fmt(m2(p * (1 + t / 100)))}.")


def f102(r):
    rows = r.sample([("increase by 30%", "1.3"), ("decrease by 30%", "0.7"), ("increase by 5%", "1.05"), ("decrease by 5%", "0.95"), ("increase by 100%", "2")], 4)
    return GD("Write the multiplier for each change.", "Multiplier", rows, o="O2", d="H", extra=["0.3", "0.05"], reason="Increase: 1 + p/100. Decrease: 1 − p/100.")
def f103(r):
    p = pick(r, [10, 20, 25]); new = pick(r, [66, 90, 120, 150])
    old = new / (1 + p / 100)
    if old != int(old): return None
    return N(f"After a {p}% increase, a price is ${new}. What was it before?", int(old), "$", units=["$"], o="O2", d="VH", reason=f"{new} ÷ {1 + p / 100:g} = {int(old)}. (Not {new} − {p}% of {new}.)")


s.std([u4, u6, u1, u2, u3, u8, u9, u5, u7, u10, u11, u12, u13], EX("Explain why multiplying by 0.85 decreases an amount by 15%.", [("0.85 = 85%", ["85"]), ("100% − 15% = 85% is what is left", ["100 ?− ?15|100 ?- ?15|left|remain"])], "0.85 is 85%. Decreasing by 15% leaves 100% − 15% = 85% of the amount, so multiplying by 0.85 does the decrease in one step.", o="O2"),
      deep=[f102, f103])

U.mindmap(("Increase and decrease", "Find the % then add or subtract • % change = change ÷ original × 100", "O1", "10.1"),
          ("Multipliers", "+15% → × 1.15 • −15% → × 0.85", "O2", "10.2"))
