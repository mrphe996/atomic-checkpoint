# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 3 Decimals, percentages and rounding. Written by the Atomic teaching team."""
import math
from kit import *

U = Unit(3, "Decimals, Percentages and Rounding", "Number",
         "Multiplying and dividing by powers of 10, calculating with decimals, compound percentages, and upper and lower bounds.",
         {"O1": {"sec": "3.1", "code": "9Np.01", "codeNote": "", "t": "Multiply and divide numbers by 10 to any positive or negative power, e.g. 10³, 10⁻², and by 0.1 and 0.01."},
          "O2": {"sec": "3.2", "code": "9Nf.07", "codeNote": "", "t": "Multiply and divide by decimals, using estimation to check answers."},
          "O3": {"sec": "3.3", "code": "9Nf.05", "codeNote": "", "t": "Understand compound percentages, e.g. a 10% increase followed by a 10% decrease, and calculate repeated percentage change."},
          "O4": {"sec": "3.4", "code": "9Np.02", "codeNote": "", "t": "Find the upper and lower bounds of a number rounded to a given degree of accuracy."}})

# ================================================================== 3.1
s = U.section("3.1", "Multiplying and dividing by powers of 10", ["O1"])
s.idea("Powers of 10", ["Multiplying by 10ⁿ moves the digits **n places to the left** (the number gets bigger); dividing by 10ⁿ moves them n places to the **right**.",
       "10⁻¹ = 0.1 and 10⁻² = 0.01. So **multiplying by 0.1 is the same as dividing by 10**, and dividing by 0.01 is the same as multiplying by 100."])
s.example("Negative powers", "Work out 3.7 × 10⁻³.", [("10⁻³ = 0.001", ""), ("3.7 ÷ 1000", "× 10⁻³ is the same as ÷ 10³"), ("0.0037", "")], "0.0037")
s.check(N("Work out 45 ÷ 0.01.", 4500, o="O1", reason="÷ 0.01 is × 100."))
s.example("Mixed", "Work out 0.62 × 10⁴ ÷ 10².", [("0.62 × 10⁴ = 6200", ""), ("6200 ÷ 100 = 62", "")], "62")
s.mistake("Adding zeros", ["0.5 × 100 is not 0.500. The digits move: 0.5 × 100 = 50."])
s.check(MC("Which calculation gives the same answer as 72 × 0.1?", "72 ÷ 10", [("72 × 10", "0.1 is smaller than 1, so the answer is smaller."), ("72 ÷ 0.1", "That is 720."), ("72 ÷ 100", "")], o="O1"))
def t1(r):
    m = round(r.uniform(0.1, 99), r.randint(1, 3)); e = r.randint(-4, 5); v = m * 10 ** e
    op = f"× 10{sup(e)}" if r.random() < 0.6 else f"÷ 10{sup(-e)}"
    return N(f"Work out {fmt(m)} {op}.", round(v, 10), o="O1", reason=f"{op} moves the digits {abs(e)} place(s) {'left' if e>0 else 'right'}: {fmt(round(v,10))}.")
def t2(r):
    m = round(r.uniform(1, 999), r.randint(0, 2)); k = pick(r, [("× 0.1", 0.1), ("× 0.01", 0.01), ("÷ 0.1", 10), ("÷ 0.01", 100), ("× 0.001", 0.001)])
    return N(f"Work out {fmt(m)} {k[0]}.", round(m * k[1], 10), o="O1")
def t3(r):
    m = round(r.uniform(0.01, 50), 2); e = r.randint(-3, 4); v = round(m * 10 ** e, 10)
    return N(f"{fmt(m)} × 10ⁿ = {fmt(v)}. Find n.", e, o="O1", d="H")
def t4(r):
    rows = [("× 10⁻²", "÷ 100"), ("÷ 10⁻¹", "× 10"), ("× 0.001", "÷ 1000"), ("÷ 0.01", "× 100")]
    return MT("Match each operation with an equivalent one.", r.sample(rows, 4), o="O1")
def t5(r):
    a, b = round(r.uniform(1, 9), 1), r.randint(-3, 3); c = r.randint(-3, 3)
    return N(f"Work out {fmt(a)} × 10{sup(b)} × 10{sup(c)}.", round(a * 10 ** (b + c), 10), o="O1", d="H", reason=f"× 10{sup(b+c)} overall.")
def t6(r):
    m = round(r.uniform(0.5, 50), 2)
    return TB(f"Complete the table for the number {fmt(m)}.", ["× 10²", "× 10⁻¹", "÷ 10⁻²", "÷ 10³"], [[B(round(m * 100, 10)), B(round(m / 10, 10)), B(round(m * 100, 10)), B(round(m / 1000, 10))]], o="O1", d="H")
def t7(r):
    a = round(r.uniform(1, 9), 1); n = r.randint(2, 5)
    return MC(f"Which is the largest?", f"{fmt(a)} ÷ 10{sup(-n)}", [(f"{fmt(a)} × 10{sup(-n)}", ""), (f"{fmt(a)} ÷ 10{sup(n)}", ""), (f"{fmt(a)} × 0.1", "")], o="O1", d="H", reason=f"÷ 10{sup(-n)} = × 10{sup(n)}.")
def t8(r):
    km = round(r.uniform(0.2, 9), 2)
    return N(f"1 mm = 10⁻³ m. Convert {fmt(km)} m to millimetres.", round(km * 1000, 8), "mm", units=["mm", "m", "cm"], o="O1")
s.core(t1(s.rng), t2(s.rng), t3(s.rng), t4(s.rng), t6(s.rng), t7(s.rng),
       EX("Explain why multiplying by 10⁻² gives the same answer as dividing by 100.", [("10⁻² = 1/100 = 0.01", ["1/100|0\\.01|one hundredth"]), ("multiplying by 1/100 is dividing by 100", ["divid|same as"])], "10⁻² = 1/10² = 1/100. Multiplying by 1/100 is the same as dividing by 100.", o="O1", d="H"),
       TB("Complete the place value table.", ["Number", "× 0.1", "÷ 0.1"], [["36", B(3.6), B(360)], ["0.8", B(0.08), B(8)]], o="O1"))
s.gen("p", 44, t1, t2, t3, t4, t5, t6, t7, t8)
s.gen("a", 8, lambda r: (lambda a, b: N(f"Work out ({fmt(a)} × 10{sup(b)}) ÷ (0.01 × 10{sup(b-1)}).", round(a * 1000, 8), o="O1", d="VH", reason=f"Denominator = 10{sup(b-3)}; {fmt(a)} × 10{sup(b)} ÷ 10{sup(b-3)} = {fmt(a)} × 10³."))(round(r.uniform(1, 9), 2), r.randint(2, 6)),
      lambda r: (lambda n: N(f"How many times bigger is 10⁻² than 10{sup(-n)}?", 10 ** (n - 2), o="O1", d="VH"))(r.randint(4, 7)))

# ================================================================== 3.2
s = U.section("3.2", "Multiplying and dividing decimals", ["O2"])
s.idea("Multiplying decimals", ["Multiply the numbers **without the decimal points**, then put the point back: the answer has as many decimal places as the two numbers together.",
       "**Always estimate first.** 0.48 × 3.2 ≈ 0.5 × 3 = 1.5, so the answer must be about 1.5."])
s.example("Multiply", "Work out 0.48 × 3.2.", [("48 × 32 = 1536", "ignore the points"), ("2 + 1 = 3 decimal places", ""), ("1.536", "check: estimate was 1.5 ✓")], "1.536")
s.check(N("Work out 0.7 × 0.06.", 0.042, o="O2", reason="7 × 6 = 42; 3 decimal places → 0.042."))
s.example("Divide by a decimal", "Work out 9.36 ÷ 0.4.", [("× both by 10: 93.6 ÷ 4", "make the divisor a whole number"), ("93.6 ÷ 4 = 23.4", "")], "23.4")
s.mistake("Multiplying can make numbers smaller", ["Multiplying by a number between 0 and 1 makes the answer SMALLER: 20 × 0.3 = 6. Dividing by a number between 0 and 1 makes it BIGGER: 20 ÷ 0.5 = 40."])
s.check(MC("Without calculating, which answer is greater than 50?", "50 ÷ 0.8", [("50 × 0.8", "× 0.8 makes it smaller."), ("50 ÷ 1.2", ""), ("50 × 0.99", "")], o="O2", d="H"))
def d(r, lo, hi, dp): return round(r.uniform(lo, hi), dp)
def m1(r):
    a, b = d(r, 0.1, 20, r.randint(1, 2)), d(r, 0.1, 9, r.randint(1, 2))
    return N(f"Work out {fmt(a)} × {fmt(b)} without a calculator.", round(a * b, 6), o="O2", reason=f"Estimate {round(a)} × {round(b,0) or 0.5} first; exact answer {fmt(round(a*b,6))}.")
def m2(r):
    b = pick(r, [0.2, 0.4, 0.5, 0.25, 0.03, 0.06, 1.5, 2.4]); q = d(r, 2, 90, 1); a = round(q * b, 6)
    return N(f"Work out {fmt(a)} ÷ {fmt(b)}.", q, o="O2", d="H", tol=1e-6, reason=f"Multiply both by a power of 10 so the divisor is whole: answer {fmt(q)}.")
def m3(r):
    a, b = d(r, 1, 40, 1), d(r, 1, 9, 1)
    return MC(f"Which is the best estimate for {fmt(a)} × {fmt(b)}?", fmt(round(a) * round(b)), [(fmt(round(a) * round(b) * 10), ""), (fmt(round(a) * round(b) / 10), ""), (fmt(round(a) + round(b)), "")], o="O2", d="M")
def m4(r):
    p, kg = d(r, 1.2, 9.8, 2), d(r, 0.25, 4.5, 2)
    return N(f"Apples cost ${fmt(p, 2)} per kg. Find the cost of {fmt(kg)} kg, correct to the nearest cent.", round(p * kg, 2), "$", units=["$", "kg"], o="O2", tol=0.005)
def m5(r):
    L = d(r, 2, 9, 1); piece = pick(r, [0.15, 0.25, 0.3, 0.4, 0.45]); n = int(L // piece)
    return N(f"A ribbon is {fmt(L)} m long. How many whole pieces of length {fmt(piece)} m can be cut from it?", n, "pieces", units=["pieces", "m"], o="O2", d="H", reason=f"{fmt(L)} ÷ {fmt(piece)} = {L/piece:.2f} → {n} whole pieces.")
def m6(r):
    a, b = r.randint(12, 99), r.randint(12, 99); c = a * b
    return TB(f"{a} × {b} = {c}. Use this fact to complete the table.", [f"{a/10} × {b}", f"{a/10} × {b/10}", f"{c/100} ÷ {b/10}", f"{a} × {b/1000}"], [[B(round(c / 10, 6)), B(round(c / 100, 6)), B(round(a / 10, 6)), B(round(c / 1000, 6))]], o="O2", d="H")
def m7(r):
    a = d(r, 10, 99, 1)
    return GD("Will the answer be bigger or smaller than the starting number?", "Bigger or smaller?", [(f"{fmt(a)} × 0.7", "Smaller"), (f"{fmt(a)} ÷ 0.7", "Bigger"), (f"{fmt(a)} × 1.3", "Bigger"), (f"{fmt(a)} ÷ 1.3", "Smaller")], o="O2", d="M")
def m8(r):
    w, l = d(r, 1.2, 9.5, 1), d(r, 1.5, 12, 2)
    return N(f"A rectangle measures {fmt(w)} m by {fmt(l)} m. Find its area.", round(w * l, 6), "m²", units=["m²", "m"], o="O2", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [8, 4], [0, 4]], "s": [f"{fmt(l)} m", f"{fmt(w)} m", "", ""]})
s.core(m1(s.rng), m2(s.rng), m4(s.rng), m6(s.rng), m7(s.rng), m5(s.rng), m8(s.rng),
       EX("Ravi says 3.2 × 0.5 = 16. Use estimation to explain why he must be wrong.", [("× 0.5 is half / makes it smaller", ["half|smaller|less than 3"]), ("answer is about 1.6", ["1\\.6|about 1|around 1|less than"])], "Multiplying by 0.5 halves the number, so the answer must be about 1.6, not 16. In fact 3.2 × 0.5 = 1.6.", o="O2", d="H"))
s.gen("p", 44, m1, m2, m3, m4, m5, m6, m7, m8)
s.gen("a", 8, lambda r: (lambda a, b, c: N(f"Work out ({fmt(a)} × {fmt(b)}) ÷ {fmt(c)}.", round(a * b / c, 6), o="O2", d="VH", tol=1e-6))(d(r, 0.2, 9, 1), pick(r, [0.4, 1.2, 2.5]), pick(r, [0.2, 0.05, 0.4])),
      lambda r: (lambda v: N(f"Petrol costs $1.38 per litre. Sam has ${fmt(v)}. How many whole litres can he buy?", int(v // 1.38), "litres", units=["litres", "$"], o="O2", d="VH"))(r.randint(20, 90)))

# ================================================================== 3.3
s = U.section("3.3", "Understanding compound percentages", ["O3"])
s.idea("Multipliers", ["An increase of r% means multiplying by **1 + r/100**. A decrease of r% means multiplying by **1 − r/100**. So +15% is × 1.15 and −8% is × 0.92.",
       "For changes one after another, **multiply the multipliers**. A 10% increase then a 10% decrease is × 1.1 × 0.9 = × 0.99 – a 1% decrease overall, NOT 'no change'."])
s.example("Compound interest", "$2000 is invested at 4% compound interest per year. Find the value after 3 years.", [("multiplier 1.04", ""), ("2000 × 1.04³", ""), ("= 2249.73", "")], "$2249.73")
s.check(N("Write the multiplier for a 7% decrease.", 0.93, o="O3"))
s.example("Overall change", "A price rises by 20% then falls by 25%. What is the overall percentage change?", [("1.2 × 0.75 = 0.9", ""), ("0.9 means 90% of the original", ""), ("10% decrease", "")], "a 10% decrease")
s.mistake("Percentages do not simply add", ["+20% then −20% is not 0%: 1.2 × 0.8 = 0.96, a 4% decrease."])
s.check(MC("A price is increased by 50% and then decreased by 50%. Overall it has…", "decreased by 25%", [("stayed the same", "1.5 × 0.5 = 0.75."), ("decreased by 50%", ""), ("increased by 25%", "")], o="O3", d="H"))
def c1(r):
    p = r.randint(1, 35); up = r.random() < 0.5
    return N(f"Write the multiplier for a {p}% {'increase' if up else 'decrease'}.", round(1 + p / 100 if up else 1 - p / 100, 4), o="O3")
def c2(r):
    P, rate, n = r.randint(5, 80) * 100, pick(r, [2, 2.5, 3, 4, 5, 6]), r.randint(2, 6)
    return N(f"${fmt(P)} is invested at {fmt(rate)}% compound interest per year. Find its value after {n} years, to the nearest cent.", round(P * (1 + rate / 100) ** n, 2), "$", units=["$", "%"], o="O3", d="H", tol=0.01, reason=f"{fmt(P)} × {1+rate/100}{sup(n)} = {P*(1+rate/100)**n:.2f}.")
def c3(r):
    a, b = r.randint(5, 40), r.randint(5, 40); up1, up2 = r.random() < 0.5, r.random() < 0.5
    m = (1 + a / 100 if up1 else 1 - a / 100) * (1 + b / 100 if up2 else 1 - b / 100); ch = round((m - 1) * 100, 2)
    return N(f"A value is {'increased' if up1 else 'decreased'} by {a}% then {'increased' if up2 else 'decreased'} by {b}%. Find the overall percentage change (use a minus sign for a decrease).", ch, "%", units=["%"], o="O3", d="H", tol=0.01, reason=f"Multiplier {m:.4f} → {ch}%.")
def c4(r):
    V, rate, n = r.randint(8, 40) * 1000, r.randint(8, 25), r.randint(2, 5)
    return N(f"A car worth ${fmt(V)} loses {rate}% of its value each year. Find its value after {n} years, to the nearest dollar.", round(V * (1 - rate / 100) ** n), "$", units=["$", "%"], o="O3", d="H", tol=1)
def c5(r):
    P, rate = r.randint(2, 20) * 100, pick(r, [3, 4, 5, 6])
    rows = [[str(y), B(round(P * (1 + rate / 100) ** y, 2), 0.01)] for y in (1, 2, 3)]
    return TB(f"${fmt(P)} earns {rate}% compound interest each year. Complete the table (to the nearest cent).", ["Year", "Value ($)"], rows, o="O3", d="H")
def c6(r):
    a = r.randint(5, 30)
    return EX(f"Explain why increasing a price by {a}% and then decreasing it by {a}% does not give the original price.", [("the decrease is of a larger amount / new price", ["larger|bigger|new price|different amount|higher price"]), (f"multiplier product less than 1", ["0\\.9|less than 1|smaller|lower"])],
              f"The {a}% decrease is taken from the new, larger price, so more is taken off than was added. (1 + {a/100}) × (1 − {a/100}) is less than 1.", o="O3", d="H")
def c7(r):
    r1, n = pick(r, [5, 10, 20]), r.randint(2, 4)
    return MC(f"Which calculation finds the value of $500 after {n} years at {r1}% compound interest?", f"500 × {1+r1/100}{sup(n)}", [(f"500 × {1+r1/100} × {n}", "That multiplies by the number of years instead of using a power."), (f"500 + {n} × {r1}% of 500", "That is simple interest."), (f"500 × {r1/100}{sup(n)}", "")], o="O3")
def c8(r):
    orig, p = r.randint(20, 400), r.randint(5, 40); new = round(orig * (1 + p / 100), 2)
    return N(f"After a {p}% increase, a price is ${fmt(new)}. What was the price before the increase?", orig, "$", units=["$", "%"], o="O3", d="VH", tol=0.01, reason=f"{fmt(new)} ÷ {1+p/100} = {orig}.")
s.core(c1(s.rng), c2(s.rng), c3(s.rng), c5(s.rng), c6(s.rng), c7(s.rng), c4(s.rng),
       GD("Compare simple and compound interest on $1000 at 10% for 2 years.", "Value after 2 years", [("Simple interest", "$1200"), ("Compound interest", "$1210")], extra=["$1100", "$1020"], o="O3", d="H"))
s.gen("p", 44, c1, c2, c3, c4, c5, c7, c8)
s.gen("a", 8, c8, lambda r: (lambda rate: N(f"Money is invested at {rate}% compound interest per year. After how many whole years does it first double?", next(n for n in range(1, 200) if (1 + rate / 100) ** n >= 2), "years", units=["years", "%"], o="O3", d="VH"))(pick(r, [3, 4, 5, 6, 8, 10, 12])))

# ================================================================== 3.4
s = U.section("3.4", "Understanding upper and lower bounds", ["O4"])
s.idea("Bounds", ["A rounded number could have been any value in a range. If a length is 8 cm **to the nearest cm**, the real length is at least 7.5 cm (the **lower bound**) and less than 8.5 cm (the **upper bound**).",
       "The bounds are **half a unit** below and above. We write 7.5 ≤ l < 8.5."])
s.example("Nearest 10", "A crowd is 3400 to the nearest 100. Write the lower and upper bounds.", [("half of 100 = 50", ""), ("3400 − 50 = 3350, 3400 + 50 = 3450", "")], "3350 ≤ n < 3450")
s.check(N("A mass is 2.6 kg correct to 1 decimal place. Write the lower bound.", 2.55, "kg", units=["kg", "g"], o="O4"))
s.example("Decimal places", "x = 0.37 to 2 decimal places. Write the error interval.", [("half of 0.01 = 0.005", ""), ("0.365 ≤ x < 0.375", "")], "0.365 ≤ x < 0.375")
s.mistake("The upper bound", ["For 8 cm to the nearest cm the upper bound is 8.5 cm, not 8.4 cm or 8.49 cm – values up to (but not including) 8.5 round to 8."])
s.check(MC("A length is 120 cm to the nearest 10 cm. Which is the error interval?", "115 ≤ l < 125", [("119.5 ≤ l < 120.5", "That is for the nearest cm."), ("110 ≤ l < 130", "Half of 10 is 5."), ("115 ≤ l ≤ 124", "")], o="O4", d="H"))
UNITS = [("to the nearest whole number", 1, 0), ("to the nearest 10", 10, 0), ("to the nearest 100", 100, 0), ("to 1 decimal place", 0.1, 1), ("to 2 decimal places", 0.01, 2)]
def b1(r):
    nm, u, dp = pick(r, UNITS); v = round(r.uniform(2, 900) / u) * u; lo = round(v - u / 2, dp + 1)
    return N(f"A number is {fmt(round(v, dp))} {nm}. Write its lower bound.", lo, o="O4", reason=f"Half of {fmt(u)} is {fmt(u/2)}; {fmt(round(v,dp))} − {fmt(u/2)} = {fmt(lo)}.")
def b2(r):
    nm, u, dp = pick(r, UNITS); v = round(r.uniform(2, 900) / u) * u; hi = round(v + u / 2, dp + 1)
    return N(f"A number is {fmt(round(v, dp))} {nm}. Write its upper bound.", hi, o="O4")
def b3(r):
    nm, u, dp = pick(r, UNITS[:3]); v = round(r.uniform(20, 900) / u) * u
    return TB(f"A length is {fmt(v)} m {nm}. Complete the error interval.", ["Lower bound", "", "Upper bound"], [[B(v - u / 2), "≤ l <", B(v + u / 2)]], o="O4", d="M")
def b4(r):
    a = r.randint(4, 20)
    return N(f"The side of a square is {a} cm to the nearest cm. Find the upper bound of its perimeter.", 4 * (a + 0.5), "cm", units=["cm", "cm²"], o="O4", d="H")
def b5(r):
    a, b = r.randint(5, 30), r.randint(5, 30)
    return N(f"A rectangle is {a} cm by {b} cm, both to the nearest cm. Find the lower bound of its area.", (a - 0.5) * (b - 0.5), "cm²", units=["cm²", "cm"], o="O4", d="H", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [8, 4], [0, 4]], "s": [f"{a} cm", f"{b} cm", "", ""]})
def b6(r):
    v = round(r.uniform(3, 9), 1)
    return MS(f"x = {fmt(v)} to 1 decimal place. Select ALL the values x could be.", [fmt(round(v - 0.05, 2)), fmt(round(v + 0.04, 2))], [fmt(round(v + 0.05, 2)), fmt(round(v - 0.06, 2))], o="O4", d="H")
def b7(r):
    n = r.randint(12, 80) * 10
    return N(f"{n} people (to the nearest 10) went to a concert. What is the least possible number of people?", n - 5, "people", units=["people"], o="O4", d="H", reason="People are whole numbers: the lower bound is n − 5 (that still rounds up to n).")
s.core(b1(s.rng), b2(s.rng), b3(s.rng), b4(s.rng), b5(s.rng), b6(s.rng),
       EX("A box has a mass of 4 kg to the nearest kg. Explain why its mass could be 3.5 kg but not 4.5 kg.", [("3.5 rounds up to 4", ["3\\.5.{0,30}(round|4)"]), ("4.5 rounds up to 5", ["4\\.5.{0,30}(round|5)"])], "3.5 kg rounds up to 4 kg, so it is the lower bound. 4.5 kg would round up to 5 kg, so 4.5 is not included – the mass is less than 4.5 kg.", o="O4", d="H"),
       b7(s.rng))
s.gen("p", 44, b1, b2, b3, b4, b5, b6, b7)
s.gen("a", 8, lambda r: (lambda dd, t: N(f"A car travels {dd} km (nearest km) in {t} hours (nearest hour). Find the upper bound of its average speed, to 1 decimal place.", round((dd + 0.5) / (t - 0.5), 1), "km/h", units=["km/h", "km"], tol=0.05, o="O4", d="VH", reason="Greatest speed = greatest distance ÷ least time."))(r.randint(100, 400), r.randint(2, 6)),
      lambda r: (lambda a: N(f"The area of a square is {a} cm² to the nearest cm². Find the lower bound of its side, to 2 decimal places.", round(math.sqrt(a - 0.5), 2), "cm", units=["cm", "cm²"], tol=0.006, o="O4", d="VH"))(r.randint(20, 150)))

U.mindmap(("Powers of 10", "× 10⁻ⁿ is ÷ 10ⁿ • × 0.1 = ÷ 10", "O1", "3.1"), ("Decimal calculations", "Estimate first • count decimal places", "O2", "3.2"),
          ("Compound percentages", "Multiply multipliers • 1.1 × 0.9 = 0.99", "O3", "3.3"), ("Bounds", "Half a unit either side • lower ≤ x < upper", "O4", "3.4"))
