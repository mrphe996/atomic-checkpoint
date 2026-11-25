# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 3 Addition and subtraction of whole numbers (3.1 Using a symbol to represent a missing number
or operation, 3.2 Addition and subtraction of whole numbers, 3.3 Generalising with odd and even numbers). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(3, "Addition and Subtraction of Whole Numbers", "Number",
         "Using a symbol for a missing number or operation, adding and subtracting numbers with up to 3 digits, and rules about odd and even numbers.",
         {"O1": {"code": "4Ae.01", "sec": "3.1", "codeNote": "", "t": "Use a symbol to represent a missing number or operation in a number sentence."},
          "O2": {"code": "4Nc.01", "sec": "3.2", "codeNote": "", "t": "Estimate, add and subtract whole numbers with up to three digits."},
          "O3": {"code": "4Nc.02", "sec": "3.3", "codeNote": "", "t": "Use the properties of odd and even numbers to generalise about sums and differences."}})

s = U.section("3.1", "Using a symbol to represent a missing number or operation", ["O1"])
s.idea("Missing numbers and signs", ["A shape can stand for a missing number: in **▲ + 25 = 60**, ▲ = 35.",
       "A missing **operation** can be +, −, × or ÷: 12 ○ 4 = 3 means 12 **÷** 4 = 3."], table={"head": ["Number sentence", "Missing"], "rows": [["▲ + 25 = 60", "35"], ["12 ○ 4 = 3", "÷"]]})
s.check(N("Find ▲: ▲ − 18 = 30", 48, o="O1"))
s.check(MC('Before you read on: ☐ + 7 = 15. What is ☐?', '8', [('22', '15 − 7 = 8.'), ('7', 'Check: 7 + 7 = 14.')], o='O1'))
s.mistake("Use the inverse", ["To find ▲ in ▲ − 18 = 30, add: 30 + 18 = 48."])


def m1(r):
    a, t = r.randint(10, 80), r.randint(90, 200)
    return N(f"Find ▲: ▲ + {a} = {t}. The bar model shows the whole and one part.", t - a, o="O1", data={"head": ["Whole", str(t)], "rows": [["Parts", f"▲ + {a}"]]})
def m2(r):
    a, b = r.randint(10, 90), r.randint(10, 90)
    return N(f"Find ▲: ▲ − {a} = {b}", a + b, o="O1")
def m3(r):
    a, b = r.randint(2, 10), r.randint(2, 10); op = pick(r, ["+", "−", "×", "÷"])
    x, y = (a * b, a) if op == "÷" else (a + b, a) if op == "−" else (a, b)
    res = {"+": x + y, "−": x - y, "×": x * y, "÷": x // y}[op]
    return MC(f"Which sign goes in the circle? {x} ○ {y} = {res}", op, [o for o in ["+", "−", "×", "÷"] if o != op and {"+": x + y, "−": x - y, "×": x * y, "÷": x / y}[o] != res][:3], o="O1")
def m4(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return N(f"Find ■: {a} × ■ = {a * b}", b, o="O1")
def m5(r):
    a, b = r.randint(20, 60), r.randint(5, 30)
    return TB("Find each missing number.", ["Number sentence", "Missing number"], [[f"☐ + {b} = {a + b}", B(a)], [f"{a + b} − ☐ = {a}", B(b)]], o="O1")
def m6(r):
    a, b = r.randint(10, 50), r.randint(10, 50)
    return N(f"Kim had some stickers. She was given {a} more and now has {a + b}. Write it as ▲ + {a} = {a + b}. Find ▲.", b, "stickers", units=["stickers"], o="O1")
def m7(r):
    a, b, c = r.randint(10, 40), r.randint(10, 40), r.randint(5, 20)
    return N(f"Find ▲: {a} + ▲ = {b} + {c + a}", b + c, o="O1", d="H")
def m8(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return N(f"The same shape stands for the same number. ● + ● = {2 * a} and ● + ▲ = {a + b}. What is ▲?", b, o="O1", d="H")


s.std([m5, m3, m1, m2, m4, m6, m7, m8], EX("Explain how to find ▲ in ▲ + 45 = 120.", [("use the inverse: subtract 45", "subtract|take away|− ?45|inverse"), ("120 − 45 = 75", "75")], "Use the inverse of adding 45, which is subtracting 45: 120 − 45 = 75. So ▲ = 75.", o="O1"))

s = U.section("3.2", "Addition and subtraction of whole numbers", ["O2"])
s.idea("Columns and estimates", ["Line up hundreds, tens and ones. **Exchange** when a column makes 10 or more (adding) or is too small (subtracting).",
       "Estimate first by rounding: 487 + 236 ≈ 490 + 240 = 730. Check by using the inverse."], table={"head": ["", "H", "T", "O"], "rows": [["", "4", "8", "7"], ["+", "2", "3", "6"], ["=", "7", "2", "3"]]})
s.check(N("Work out 487 + 236.", 723, o="O2"))
s.check(MC('Before you read on: what is 300 − 1?', '299', [('209', 'Count back 1 from 300.'), ('290', '300 − 10 = 290; 300 − 1 = 299.')], o='O2'))
s.mistake("Exchange across zeros", ["In 402 − 167, exchange from the hundreds through the tens."])


def a1(r):
    a, b = r.randint(150, 650), r.randint(150, 349)
    return N(f"Work out {a} + {b}.", a + b, o="O2")
def a2(r):
    a, b = r.randint(400, 999), r.randint(100, 399)
    return N(f"Work out {a} − {b}.", a - b, o="O2")
def a3(r):
    a, b = r.randint(110, 490), r.randint(110, 490); e = round(a, -1) + round(b, -1)
    return MC(f"Which is the best estimate for {a} + {b}?", str(e), [str(e + 100), str(e - 100), str(e * 2)], o="O2")
def a4(r):
    lab = ["Mon", "Tue", "Wed"]; v = [r.randint(100, 400) for _ in lab]
    return N("The table shows visitors to a park. How many visitors in total?", sum(v), "visitors", units=["visitors"], o="O2", data={"head": ["Day", *lab], "rows": [["Visitors", *map(str, v)]]})
def a5(r):
    a, b = r.randint(300, 900), r.randint(100, 290)
    return TB(f"Work out {a} − {b} in columns.", ["H", "T", "O"], [[B((a - b) // 100), B((a - b) // 10 % 10), B((a - b) % 10)]], o="O2")
def a6(r):
    a, b = r.randint(200, 900), r.randint(100, 199)
    return N(f"A shop had {a} pencils. It sold {b}. How many are left?", a - b, "pencils", units=["pencils"], o="O2")
def a7(r):
    a, b = r.randint(400, 900), r.randint(100, 399)
    return MC(f"Which calculation checks {a} − {b} = {a - b}?", f"{a - b} + {b}", [f"{a} + {b}", f"{a - b} − {b}"], o="O2")
def a8(r):
    a, b, c = r.randint(100, 300), r.randint(100, 300), r.randint(10, 99)
    return N(f"Work out {a} + {b} − {c}.", a + b - c, o="O2", d="H")


s.std([a5, a4, a1, a2, a3, a6, a7, a8], EX("Explain how to estimate 512 − 289.", [("round to 500 − 300 or 510 − 290", "500|300|510|290|round"), ("about 200 or 220", "200|220")], "Round each number: 512 ≈ 510 and 289 ≈ 290. 510 − 290 = 220, so the answer is about 220.", o="O2"))

s = U.section("3.3", "Generalising with odd and even numbers", ["O3"])
s.idea("Odd and even rules", ["**even + even = even**, **odd + odd = even**, **odd + even = odd**. The same rules work for subtraction.",
       "Test a rule with examples, and look for a counter-example that breaks it."], table={"head": ["+", "even", "odd"], "rows": [["even", "even", "odd"], ["odd", "odd", "even"]]})
s.check(MC("Is 37 + 45 odd or even?", "even", [("odd", "")], o="O3"))
s.check(MC('Before you read on: is odd + odd always even?', 'Yes', [('No, always odd', '3 + 5 = 8, 7 + 1 = 8.'), ('Sometimes', 'Pair up the dots: the two odd ones pair together.')], o='O3'))
s.mistake("Look at the ones digit", ["Only the ones digit tells you if a number is odd or even."])


def e1(r):
    a, b = r.randint(10, 500), r.randint(10, 500)
    return MC(f"Without adding, is {a} + {b} odd or even?", "even" if (a + b) % 2 == 0 else "odd", ["odd" if (a + b) % 2 == 0 else "even"], o="O3")
def e2(r):
    a, b = sorted(r.sample(range(10, 500), 2), reverse=True)
    return MC(f"Without subtracting, is {a} − {b} odd or even?", "even" if (a - b) % 2 == 0 else "odd", ["odd" if (a - b) % 2 == 0 else "even"], o="O3")
def e3(r):
    ns = r.sample(range(100, 9999), 4)
    return GD("Is each number odd or even?", "Odd or even", [(str(n), "even" if n % 2 == 0 else "odd") for n in ns], o="O3", extra=["odd", "even"])
def e4(r):
    rows = r.sample([("odd + odd", "even"), ("odd + even", "odd"), ("even + even", "even"), ("even − odd", "odd"), ("odd − odd", "even")], 4)
    return GD("Is each answer always odd or always even?", "Answer", rows, o="O3", extra=["odd", "even"])
def e5(r):
    return MC("Ben says: 'odd + odd + odd is always even.' Is he right?", "No, it is always odd", ["Yes, always", "Only sometimes"], o="O3", d="H")
def e6(r):
    a = r.randint(10, 99) * 2 + 1
    return MC(f"Which number added to {a} gives an even answer?", str(a + 2 * r.randint(1, 5)), [str(a + 1), str(a + 3 + 1), str(2 * r.randint(10, 40))], o="O3")
def e7(r):
    lo = r.randint(20, 80)
    return N(f"How many odd numbers are there from {lo} to {lo + 9}?", 5, o="O3")
def e8(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return MS("Select ALL the sums that are even.", [f"{2 * a + 1} + {2 * b + 1}", f"{2 * a} + {2 * b}"], [f"{2 * a + 1} + {2 * b}", f"{2 * a} + {2 * b + 1}"], o="O3")


def c43(r):
    rows = r.sample([('odd + odd = even', 'Always true'), ('even + odd = even', 'Never true'), ('odd × odd = odd', 'Always true'), ('a number that ends in 6 is even', 'Always true'), ('an odd number divides by 3', 'Sometimes true')], 4)
    return GD('Is each statement always, sometimes or never true?', "Always / sometimes / never", rows, o='O3', d="H", extra=["Always true", "Sometimes true", "Never true"], reason='Test a few examples, then explain with pairs: an odd number has one left over.')


s.std([e3, e4, e1, e2, e6, e7, e8, e5], EX("Explain why odd + odd is always even.", [("each odd number has one left over when paired", "left over|one extra|spare"), ("the two left-overs make a pair", "pair|together|even")], "When you make pairs, each odd number has one left over. The two left-overs make one more pair, so the total has no left-over: it is even.", o="O3"),
      deep=[c43])

U.mindmap(("Symbols", "▲ for a missing number • ○ for a missing sign", "O1", "3.1"), ("Columns", "Exchange • estimate • inverse", "O2", "3.2"), ("Odd and even", "odd + odd = even", "O3", "3.3"))
