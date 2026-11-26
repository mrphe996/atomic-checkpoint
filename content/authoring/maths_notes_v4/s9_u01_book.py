# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u01 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(1, "1.1")]["book"] = BK(
    keys=[("rational number", "can be written as a fraction of two integers"), ("irrational number", "cannot be written as a fraction; its decimal never ends or repeats"), ("surd", "an irrational root such as √7")],
    intro=[], examples=[],
    exercise=[
        Ex("Rational or irrational?", ("√121", "rational (11)"), ("√32", "irrational"), ("0.818181…", "rational (9/11)"), ("∛64", "rational (4)")),
        Ex("Between which two whole numbers is each root?", ("√58", "7 and 8"), ("∛150", "5 and 6")),
        Ex("Estimate √85 to 1 decimal place without a calculator, then check.", ans="≈ 9.2"),
    ],
    check=["Can I tell rational from irrational numbers?", "Can I estimate square and cube roots?"], look=[], note=NOTE)

N[(1, "1.2")]["book"] = BK(
    keys=[("standard form", "a × 10ⁿ with 1 ≤ a < 10 and n an integer")],
    intro=[], examples=[],
    exercise=[
        Ex("Write in standard form.", ("56 000 000", "5.6 × 10⁷"), ("0.000 309", "3.09 × 10⁻⁴"), ("72 × 10⁻⁵", "7.2 × 10⁻⁴")),
        Ex("Write as ordinary numbers.", ("4.1 × 10⁶", "4 100 000"), ("2.75 × 10⁻³", "0.002 75")),
        Ex("Order from smallest: 3.2 × 10⁻², 8 × 10⁻³, 1.05 × 10⁻².", ans="8 × 10⁻³, 1.05 × 10⁻², 3.2 × 10⁻²"),
    ],
    check=["Can I write large and small numbers in standard form?", "Can I compare them?"], look=[], note=NOTE)

N[(1, "1.3")]["book"] = BK(
    keys=[("index", "the small raised number showing a power"), ("index laws", "aᵐ × aⁿ = aᵐ⁺ⁿ, aᵐ ÷ aⁿ = aᵐ⁻ⁿ")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("9⁰", "1"), ("2⁻⁴", "1/16"), ("10⁻¹", "1/10")),
        Ex("Simplify, leaving as a power.", ("7⁻² × 7⁶", "7⁴"), ("3⁻¹ ÷ 3⁴", "3⁻⁵"), ("(5³ × 5⁻⁸) ÷ 5⁻²", "5⁻³")),
        Ex("Find n: 4ⁿ × 4³ = 4⁻².", ans="n = −5"),
    ],
    check=["Can I use zero and negative indices?", "Can I use the index laws?"], look=[], note=NOTE)
