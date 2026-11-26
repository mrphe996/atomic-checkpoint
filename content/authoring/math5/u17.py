# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 17 Number and the laws of arithmetic (17.1 Order of operations, 17.2 Using the laws of arithmetic).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(17, "Number and the Laws of Arithmetic", "Number",
         "The order of operations, including brackets, and using the commutative, associative and distributive laws to calculate mentally.",
         {"O1": {"code": "5Ni.04", "sec": "17.1", "codeNote": "", "t": "Use the order of operations, including brackets, to work out calculations."},
          "O2": {"code": "5Ni.05", "sec": "17.2", "codeNote": "", "t": "Use the commutative, associative and distributive laws to calculate mentally."}})

s = U.section("17.1", "Order of operations", ["O1"])
s.idea("What comes first", ["Work out **brackets first**, then **× and ÷**, then **+ and −**.",
       "4 + 5 × 2 = 4 + 10 = **14**, but (4 + 5) × 2 = 9 × 2 = **18**."], table={"head": ["Order", "1st", "2nd", "3rd"], "rows": [["", "Brackets", "× and ÷", "+ and −"]]})
s.check(N("Work out 10 − 2 × 3.", 4, o="O1"))
s.check(MC('Before you read on: what is 3 + 4 × 2?', '11', [('14', 'Multiply before adding.'), ('9', '4 × 2 = 8, then + 3.')], o='O1'))
s.mistake("Not always left to right", ["3 + 4 × 5 is 23, not 35. Multiply first."])


def o1(r):
    a, b, c = r.randint(2, 20), r.randint(2, 9), r.randint(2, 9)
    return N(f"Work out {a} + {b} × {c}.", a + b * c, o="O1")
def o2(r):
    a, b, c = r.randint(2, 12), r.randint(2, 9), r.randint(2, 6)
    return N(f"Work out ({a} + {b}) × {c}.", (a + b) * c, o="O1")
def o3(r):
    b, c = r.randint(2, 9), r.randint(2, 9); a = b * c + r.randint(1, 20)
    return N(f"Work out {a} − {b} × {c}.", a - b * c, o="O1")
def o4(r):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(2, 6)
    return TB("Complete the table.", ["Calculation", "Answer"], [[f"{a} + {b} × {c}", B(a + b * c)], [f"({a} + {b}) × {c}", B((a + b) * c)]], o="O1")
def o5(r):
    c, q, a = r.randint(2, 9), r.randint(2, 9), r.randint(1, 20)
    return N(f"Work out {a} + {c * q} ÷ {c}.", a + q, o="O1")
def o6(r):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(2, 6)
    return MC(f"Where do the brackets go to make {a} + {b} × {c} = {(a + b) * c}?", f"({a} + {b}) × {c}", [f"{a} + ({b} × {c})", f"no brackets needed"], o="O1", d="H")
def o7(r):
    a, b = r.randint(10, 40), r.randint(2, 9)
    return N(f"Pens cost {b} cents each. Mia has {a + 5 * b} cents and buys 5 pens. Work out {a + 5 * b} − 5 × {b} to find how much she has left.", a, "cents", units=["cents"], o="O1", data={"head": ["Money (cents)", "Pens", "Cost of a pen (cents)"], "rows": [[str(a + 5 * b), "5", str(b)]]})
def o8(r):
    a, b, c, d = r.randint(2, 6), r.randint(2, 6), r.randint(2, 6), r.randint(2, 6)
    return N(f"Work out {a} × {b} + {c} × {d}.", a * b + c * d, o="O1", d="H")


def g171(r):
    return MC('Lia says 20 − 6 ÷ 2 = 7. What is right?', '17', [('7', 'Divide first: 6 ÷ 2 = 3.'), ('13', '20 − 3 = 17.')], o='O1', d="H", reason='Divide before subtracting: 20 − 3 = 17.')


s.std([o4, o7, o1, o2, o3, o5, o6, o8], EX("Explain why (2 + 3) × 4 = 20 but 2 + 3 × 4 = 14.", [("brackets are worked out first: 5 × 4 = 20", "brackets first|5 ?× ?4|20"), ("without brackets multiply first: 2 + 12 = 14", "multiply first|12|14")], "With brackets, add first: (2 + 3) × 4 = 5 × 4 = 20. Without brackets, multiply first: 3 × 4 = 12, then 2 + 12 = 14.", o="O1"),
      deep=[g171])

s = U.section("17.2", "Using the laws of arithmetic", ["O2"])
s.idea("Laws that make calculating easier", ["**Commutative law**: you can swap the order when adding or multiplying: 6 × 7 = 7 × 6.",
       "**Associative law**: you can group numbers differently: (5 × 2) × 9 = 5 × (2 × 9).",
       "**Distributive law**: split a number to multiply: 7 × 23 = 7 × 20 + 7 × 3 = 140 + 21 = **161**."])
s.check(N("Work out 25 × 7 × 4 in your head.", 700, o="O2"))
s.check(MC('Before you read on: is 6 × 7 the same as 7 × 6?', 'Yes', [('No', 'Multiplying can be done in either order.'), ('Only for small numbers', 'It works for every number.')], o='O2'))
s.mistake("Not for subtraction", ["8 − 3 is not the same as 3 − 8. Swapping only works for + and ×."])


def l1(r):
    k, b = r.randint(12, 49), r.randint(3, 9)
    return N(f"Use the distributive law to work out {k} × {b}.", k * b, o="O2")
def l2(r):
    a = r.randint(3, 19)
    return N(f"Work out 5 × {a} × 2 in your head.", 10 * a, o="O2")
def l3(r):
    laws = [("9 + 6 = 6 + 9", "commutative"), ("(4 × 5) × 3 = 4 × (5 × 3)", "associative"), ("8 × 14 = 8 × 10 + 8 × 4", "distributive"),
            ("12 × 3 = 3 × 12", "commutative"), ("(7 + 2) + 8 = 7 + (2 + 8)", "associative"), ("6 × 31 = 6 × 30 + 6 × 1", "distributive")]
    return GD("Which law does each statement show?", "Law", r.sample(laws, 4), o="O2", extra=["commutative", "associative", "distributive"])
def l4(r):
    a, b = r.randint(11, 39), r.randint(3, 9)
    return TB(f"Work out {a} × {b} by splitting {a}.", ["Part", "Answer"], [[f"{a // 10 * 10} × {b}", B(a // 10 * 10 * b)], [f"{a % 10} × {b}", B(a % 10 * b)], ["Total", B(a * b)]], o="O2") if a % 10 else None
def l5(r):
    a, b = r.randint(2, 9), r.randint(11, 49)
    if b % 10 == 0: return None
    return N(f"Find the missing number: {a} × {b} = {a} × {b - b % 10} + {a} × ☐", b % 10, o="O2")
def l6(r):
    n = r.randint(3, 9)
    return MC(f"Which is the same as {n} × 13?", f"{n} × 10 + {n} × 3", [f"{n} × 10 + 3", f"{n} + 10 × 3", f"{n} × 1 × 3"], o="O2")
def l7(r):
    x = r.randint(11, 89); y = 100 - x; z = r.randint(10, 99)
    return N(f"Work out {x} + {z} + {y} by adding {x} and {y} first.", x + y + z, o="O2")
def l8(r):
    a = r.randint(12, 35)
    return N(f"Work out {a} × 9 using {a} × 10 − {a}.", a * 9, o="O2", d="H")


s.std([l3, l4, l1, l2, l5, l6, l7, l8], EX("Explain an easy way to work out 4 × 17 × 25.", [("swap the order to do 4 × 25 first", "4 ?× ?25|swap|order|commutative"), ("4 × 25 = 100, then 100 × 17 = 1700", "100|1700")], "Multiplication can be done in any order, so do 4 × 25 = 100 first. Then 100 × 17 = 1700.", o="O2"))

U.mindmap(("Order of operations", "Brackets • × ÷ • + −", "O1", "17.1"), ("Laws", "Commutative • associative • distributive", "O2", "17.2"))
