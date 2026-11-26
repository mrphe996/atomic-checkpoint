# -*- coding: utf-8 -*-
"""Stage 8 · Unit 1 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u01 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(1, "1.1")]["book"] = BK(
    keys=[("prime factor", "a factor that is a prime number"), ("factor tree", "a diagram splitting a number into primes"), ("index form", "using powers, e.g. 2³ × 3²")],
    intro=[], examples=[],
    exercise=[
        Ex("Write as a product of prime factors in index form.", ("96", "2⁵ × 3"), ("294", "2 × 3 × 7²"), ("1000", "2³ × 5³")),
        Ex("Find the HCF and LCM.", ("48 and 180", "HCF 12, LCM 720"), ("2² × 3³ × 5 and 2³ × 3 × 7", "HCF 12, LCM 7560")),
        Ex("Two runners lap a track in 72 s and 90 s. They start together. After how many seconds are they together at the start again?", ans="360 s"),
        Ex("Explain how the prime factors of a number show whether it is a square number.", ans="All the powers are even.", think=True),
    ],
    check=["Can I write a number as a product of primes?", "Can I find the HCF and LCM using prime factors?"], look=[], note=NOTE)

N[(1, "1.2")]["book"] = BK(
    keys=[("integer", "a whole number, positive, negative or zero"), ("order of operations", "brackets, indices, × and ÷, + and −")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("(−9) × (−7)", "63"), ("(−84) ÷ 12", "−7"), ("(−2)⁴", "16"), ("−2⁴", "−16")),
        Ex("Work out.", ("6 − 4 × (−3)", "18"), ("(−5 + 2)² × (−1)", "−9"), ("(−30) ÷ (−5) − 7", "−1")),
        Ex("Find the value of 3x² − 2y when x = −2 and y = −4.", ans="20"),
        Ex("Write a calculation with three negative numbers whose answer is −60.", ans="For example (−3) × (−4) × (−5).", think=True),
    ],
    check=["Can I multiply and divide negative integers?", "Can I use the order of operations, including powers of negatives?"], look=[], note=NOTE)

N[(1, "1.3")]["book"] = BK(
    keys=[("square root", "a number that squared gives n; positive numbers have two"), ("cube root", "a number that cubed gives n"), ("rational number", "a number that can be written as a fraction of integers")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the square roots.", ("196", "±14"), ("0.25", "±0.5")),
        Ex("Find.", ("∛216", "6"), ("∛(−1000)", "−10")),
        Ex("Estimate to 1 d.p.", ("√40", "6.3"), ("√110", "10.5")),
        Ex("Solve.", ("x² = 400", "±20"), ("x³ = −27", "−3"), ("3x² = 75", "±5")),
        Ex("Give an example of a number that is rational but not an integer, and one that is an integer but not natural.", ans="For example 1/2; −3.", think=True),
    ],
    check=["Can I find positive and negative square roots?", "Can I find cube roots of negative numbers?", "Can I estimate roots?"], look=[], note=NOTE)

N[(1, "1.4")]["book"] = BK(
    keys=[("index (power)", "how many times the base is multiplied"), ("base", "the number being raised to a power")],
    intro=[], examples=[],
    exercise=[
        Ex("Simplify, giving a single power.", ("6⁴ × 6⁵", "6⁹"), ("2¹² ÷ 2⁷", "2⁵"), ("a⁴ × a⁶ ÷ a³", "a⁷")),
        Ex("Work out.", ("8⁰", "1"), ("3² × 3³ ÷ 3⁴", "3"), ("10⁷ ÷ 10⁴", "1000")),
        Ex("Find the missing index.", ("5^☐ × 5³ = 5¹⁰", "7"), ("x¹² ÷ x^☐ = x⁴", "8")),
        Ex("Explain why 2³ × 2⁴ ≠ 2¹².", ans="That is seven 2s multiplied together, so 2⁷.", think=True),
    ],
    check=["Can I multiply and divide powers with the same base?", "Do I know that a⁰ = 1?"], look=[], note=NOTE)
