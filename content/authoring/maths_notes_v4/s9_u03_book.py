# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u03 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(3, "3.1")]["book"] = BK(
    keys=[("power of 10", "10ⁿ; negative powers are 1/10, 1/100, …")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("2.9 × 10⁻²", "0.029"), ("0.41 ÷ 10⁻³", "410"), ("750 × 10⁻⁴", "0.075"), ("0.006 ÷ 10²", "0.000 06")),
        Ex("Find n: 3.6 × 10ⁿ = 0.0036.", ans="n = −3"),
    ],
    check=["Can I multiply and divide by any power of 10?"], look=[], note=NOTE)

N[(3, "3.2")]["book"] = BK(
    keys=[("equivalent calculation", "a calculation with the same answer, e.g. 3.6 ÷ 0.4 = 36 ÷ 4")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out without a calculator.", ("0.7 × 0.08", "0.056"), ("3.4 × 1.5", "5.1"), ("2.7 ÷ 0.09", "30"), ("−0.48 ÷ 0.6", "−0.8")),
        Ex("Given 23 × 17 = 391, write down 2.3 × 0.17 and 39.1 ÷ 0.17.", ans="0.391; 230"),
    ],
    check=["Can I multiply and divide decimals?", "Do I estimate first?"], look=[], note=NOTE)

N[(3, "3.3")]["book"] = BK(
    keys=[("compound percentage", "a percentage change applied repeatedly to the new amount"), ("multiplier", "the number you multiply by for a percentage change")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the final amount.", ("$3000 at 4% a year for 3 years", "$3374.59"), ("a $12 000 car losing 12% a year for 2 years", "$9292.80")),
        Ex("A price rises 30% and then falls 30%. What is the overall percentage change?", ans="9% decrease"),
    ],
    check=["Can I use multipliers for compound changes?"], look=[], note=NOTE)

N[(3, "3.4")]["book"] = BK(
    keys=[("lower bound", "smallest value that rounds to the given value"), ("upper bound", "the boundary above; values must be less than it")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the bounds as an inequality.", ("x = 30 (nearest 10)", "25 ≤ x < 35"), ("m = 4.6 kg (1 d.p.)", "4.55 ≤ m < 4.65"), ("t = 0.83 s (2 d.p.)", "0.825 ≤ t < 0.835")),
        Ex("A square has side 9 cm to the nearest cm. Find the upper bound of its perimeter.", ans="38 cm"),
    ],
    check=["Can I find upper and lower bounds?"], look=[], note=NOTE)
