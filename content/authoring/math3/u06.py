# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 6 Fractions of shapes (6.1 Fractions of shapes, 6.2 Equivalent fractions of shapes).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *
from h import *

U = Unit(6, "Fractions of Shapes", "Number",
         "Halves, quarters, thirds, fifths and tenths of shapes, unit and non-unit fractions, and simple equivalent fractions.",
         {"O1": {"code": "3Nf.01", "sec": "6.1", "codeNote": "", "t": "Understand that a fraction is equal parts of a whole and name unit and non-unit fractions of shapes."},
          "O2": {"code": "3Nf.02", "sec": "6.2", "codeNote": "", "t": "Recognise that two fractions can be equivalent, such as 1/2 = 2/4."}})
NM = {2: "halves", 3: "thirds", 4: "quarters", 5: "fifths", 6: "sixths", 8: "eighths", 10: "tenths"}

s = U.section("6.1", "Fractions of shapes", ["O1"])
s.idea("Equal parts", ["A fraction is **equal parts** of a whole. A circle cut into 4 equal parts shows **quarters**. One part is **1/4**.",
       "**3/4** means 3 of the 4 equal parts. The bottom number (denominator) is how many equal parts; the top number (numerator) is how many we have."], fig=PIE(4, range(3)))
s.check(MC("A pizza is cut into 3 equal slices. What is one slice called?", "one third", [("one half", ""), ("one quarter", "")], o="O1"))
s.check(MC('Before you read on: a shape is cut into 4 parts, but they are different sizes. Is each part a quarter?', 'No', [('Yes', 'Quarters must be 4 EQUAL parts.'), ('Only the biggest', 'All 4 parts must be the same size.')], o='O1'))
s.mistake("Equal parts only", ["If the parts are not equal, they are not quarters."])


def f1(r):
    d = pick(r, [2, 3, 4, 5, 6, 8, 10]); n = r.randint(1, d - 1)
    return S("What fraction of the circle is shaded?", [f"{n}/{d}"], o="O1", fig=PIE(d, range(n)))
def f2(r):
    d = pick(r, [2, 3, 4, 5, 10])
    return MC(f"A cake is cut into {d} equal pieces. What is one piece called?", f"one {NM[d][:-1] if d != 2 else 'half'}" if d != 4 else "one quarter", ["one half" if d != 2 else "one third", "one tenth" if d != 10 else "one fifth"], o="O1")
def f3(r):
    d = pick(r, [3, 4, 5, 6, 8]); n = r.randint(1, d - 1)
    return N(f"How many parts of the circle are NOT shaded? Write the numerator over {d}.", d - n, o="O1", fig=PIE(d, range(n)))
def f4(r):
    d = pick(r, [4, 5, 6, 8, 10]); n = r.randint(1, d - 1)
    return TB(f"A shape has {d} equal parts and {n} are shaded. Complete the table.", ["Shaded", "Not shaded"], [[B(n), B(d - n)]], o="O1")
def f5(r):
    d = pick(r, [3, 4, 5, 8, 10])
    return N(f"How many {NM[d]} make one whole?", d, o="O1")
def f6(r):
    d = pick(r, [4, 5, 6, 8]); n = r.randint(2, d - 1)
    return MC(f"Which fraction means {n} out of {d} equal parts?", f"{n}/{d}", [f"{d}/{n}", f"1/{d}", f"{n}/{d + n}"], o="O1")
def f7(r):
    a, b = r.sample([2, 3, 4, 5, 8, 10], 2)
    return CMP(f"1/{a}", f"1/{b}", "<" if a > b else ">", o="O1", d="H")
def f8(r):
    d = pick(r, [4, 8, 10]); n = r.randint(1, d - 2); k = r.randint(1, d - n - 1)
    return S(f"{n}/{d} of a shape is red and {k}/{d} is blue. What fraction is coloured?", [f"{n + k}/{d}"], o="O1", d="H")


s.std([f1, f4, f2, f3, f5, f6, f7, f8], EX("Explain why a shape cut into 4 unequal pieces does not show quarters.", [("quarters must be equal parts", "equal"), ("4 equal parts make quarters", "4 equal|four equal|same size")], "Quarters are 4 equal parts of a whole. If the pieces are different sizes, they are not quarters.", o="O1"))

s = U.section("6.2", "Equivalent fractions of shapes", ["O2"])
s.idea("Same amount, different names", ["**1/2 = 2/4**: half a circle covers the same amount as two quarters.",
       "Other equivalent fractions: 1/2 = 3/6 = 4/8 = 5/10 and 1/5 = 2/10."], fig=PIE(8, range(4)))
s.check(N("How many quarters are the same as one half?", 2, "quarters", units=["quarters"], o="O2"))
s.check(MC('Before you read on: is 2/4 of a shape the same as 1/2?', 'Yes', [('No', '2 quarters cover half the shape.'), ('Only for circles', 'It works for any shape.')], o='O2'))
s.mistake("More parts, same amount", ["2/4 has more parts than 1/2, but the parts are smaller, so the amount is the same."])


def e1(r):
    d = pick(r, [4, 6, 8, 10])
    return MC("The circle is shaded. Which fraction is the same as the shaded part?", "1/2", ["1/4", "1/3", "3/4"], o="O2", fig=PIE(d, range(d // 2)))
def e2(r):
    d = pick(r, [4, 6, 8, 10])
    return N(f"Find the missing number: 1/2 = ☐/{d}", d // 2, o="O2")
def e3(r):
    a, b = pick(r, [(1, 4), (1, 5), (3, 4), (2, 5), (1, 3)]); k = 2
    return N(f"Find the missing number: {a}/{b} = ☐/{b * k}", a * k, o="O2", fig=PIE(b * k, range(a * k)))
def e4(r):
    ps = r.sample([("1/2", "2/4"), ("1/5", "2/10"), ("1/4", "2/8"), ("3/4", "6/8"), ("1/3", "2/6")], 4)
    return MT("Match the equivalent fractions.", ps, o="O2")
def e5(r):
    return MS("Select ALL the fractions that are equal to one half.", r.sample(["2/4", "3/6", "4/8", "5/10"], 2), ["1/4", "2/3", "3/8"], o="O2")
def e6(r):
    d = pick(r, [4, 6, 8, 10])
    return TB("Complete the table of fractions equal to 1/2.", ["Parts", "Shaded for one half"], [[str(x), B(x // 2)] for x in (4, 6, 10)], o="O2")
def e7(r):
    return MC("Ali eats 1/2 of a pizza. Ben eats 2/4 of the same size pizza. Who eats more?", "they eat the same", ["Ali", "Ben"], o="O2", d="H")
def e8(r):
    return MC("How many tenths are the same as one fifth?", "2", ["5", "1", "10"], o="O2", d="H")


s.std([e1, e3, e6, e2, e4, e5, e7, e8], EX("Explain why 1/2 is the same as 2/4.", [("cut each half into two equal pieces", "cut|split|two pieces"), ("the shaded amount stays the same", "same amount|same size|equal")], "If you cut each half of a shape into two equal pieces, you get quarters. One half becomes two quarters, but the shaded amount is the same, so 1/2 = 2/4.", o="O2"))

U.mindmap(("Fractions", "Equal parts • numerator and denominator", "O1", "6.1"), ("Equivalent", "1/2 = 2/4 = 5/10", "O2", "6.2"))
