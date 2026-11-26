# -*- coding: utf-8 -*-
"""Stage 7 · Unit 4 – Words to know, Practice on paper and checklists for the lesson documents (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u04 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(4, "4.1")]["book"] = BK(
    keys=[("tenths, hundredths, thousandths", "the places after the decimal point"), ("compare", "decide which is bigger or smaller"), ("≠", "is not equal to")],
    intro=[], examples=[],
    exercise=[
        Ex("Write <, > or = in each box.", ("4.6 ☐ 4.58", ">"), ("0.07 ☐ 0.7", "<"), ("2.50 ☐ 2.5", "="), ("−1.9 ☐ −1.09", "<")),
        Ex("Write = or ≠.", ("0.300 ☐ 0.3", "="), ("5.06 ☐ 5.6", "≠")),
        Ex("Order, smallest first: 3.42, 3.4, 3.204, 3.402, 3.024", ans="3.024, 3.204, 3.4, 3.402, 3.42"),
        Ex("Order, largest first: −0.6, 0.06, −0.06, 0.66", ans="0.66, 0.06, −0.06, −0.6"),
        Ex("Five runners' times (s): 12.08, 11.9, 12.1, 11.95, 12.008. List them fastest first.", ans="11.9, 11.95, 12.008, 12.08, 12.1"),
        Ex("Write three numbers between 0.6 and 0.61.", ans="For example 0.601, 0.605, 0.6099.", think=True),
    ],
    check=["Can I compare decimals place by place?", "Can I use <, >, = and ≠?", "Can I order negative decimals?"], look=[], note=NOTE)

N[(4, "4.2")]["book"] = BK(
    keys=[("line up", "write digits with the same place value in the same column"), ("estimate", "a rough answer using rounded numbers")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("6.4 + 2.75", "9.15"), ("0.38 + 1.9", "2.28"), ("12 − 4.36", "7.64"), ("8.05 − 2.9", "5.15")),
        Ex("Work out.", ("−2.4 + 5.1", "2.7"), ("1.6 − 3.25", "−1.65"), ("3.7 − (−1.45)", "5.15")),
        Ex("A shopper spends $12.49, $3.75 and $0.86. How much change from $20?", ans="$2.90"),
        Ex("A puppy's mass went from 3.85 kg to 5.2 kg. How much did it gain?", ans="1.35 kg"),
        Ex("Find the missing number: ☐ − 2.68 = 4.5", ans="7.18"),
        Ex("Make 10 by adding three decimals, each with 2 decimal places.", ans="For example 3.45 + 2.85 + 3.70.", think=True),
    ],
    check=["Can I line up decimal points and fill gaps with zeros?", "Can I add and subtract negative decimals?", "Can I check with an estimate?"], look=[], note=NOTE)

N[(4, "4.3")]["book"] = BK(
    keys=[("decimal places", "the number of digits after the point"), ("product", "the answer to a multiplication")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out mentally.", ("0.7 × 6", "4.2"), ("0.009 × 3", "0.027"), ("20 × 0.08", "1.6"), ("0.5 × 0.5", "0.25")),
        Ex("Use a written method.", ("4.36 × 7", "30.52"), ("2.8 × 15", "42"), ("1.25 × 3.2", "4")),
        Ex("Use 64 × 23 = 1472 to find", ("6.4 × 23", "147.2"), ("0.64 × 2.3", "1.472")),
        Ex("Paint costs $3.85 per litre. How much for 12 litres?", ans="$46.20"),
        Ex("A carpet is 3.6 m by 2.5 m. What is its area?", ans="9 m²"),
        Ex("Find two decimals whose product is 0.24.", ans="For example 0.4 × 0.6, 0.3 × 0.8, 1.2 × 0.2.", think=True),
    ],
    check=["Can I multiply a decimal by a whole number?", "Can I count decimal places to place the point?", "Can I explain why × 0.5 makes a number smaller?"], look=[], note=NOTE)

N[(4, "4.4")]["book"] = BK(
    keys=[("short division", "a written method of dividing digit by digit"), ("inverse", "the opposite operation: × undoes ÷")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("8.46 ÷ 2", "4.23"), ("13.5 ÷ 5", "2.7"), ("0.72 ÷ 8", "0.09"), ("6.3 ÷ 4", "1.575")),
        Ex("Work out.", ("38.4 ÷ 12", "3.2"), ("9.45 ÷ 15", "0.63")),
        Ex("A 4.5 m rope is cut into 6 equal pieces. How long is each piece in cm?", ans="75 cm"),
        Ex("Three friends share $25.35 equally. How much does each get?", ans="$8.45"),
        Ex("Find the missing number: ☐ ÷ 9 = 0.42", ans="3.78"),
        Ex("Explain how an estimate helps you put the decimal point in 27.36 ÷ 8.", ans="27 ÷ 8 ≈ 3, so the answer is about 3: 3.42.", think=True),
    ],
    check=["Can I keep the decimal point in line?", "Can I add zeros to keep dividing?", "Can I check by multiplying?"], look=[], note=NOTE)

N[(4, "4.5")]["book"] = BK(
    keys=[("compensation", "round a number, calculate, then adjust"), ("partition", "split a number into easier parts")],
    intro=[], examples=[],
    exercise=[
        Ex("Use compensation.", ("9 × 7.3", "65.7"), ("2.98 × 5", "14.9"), ("19 × 0.4", "7.6")),
        Ex("Re-order to make it easier.", ("0.25 × 5.7 × 4", "5.7"), ("2.5 × 1.9 × 4", "19")),
        Ex("Split the divisor.", ("9.6 ÷ 30", "0.32"), ("14.4 ÷ 40", "0.36")),
        Ex("Write the decimal as a division.", ("0.05 × 820", "41"), ("0.003 × 1600", "4.8")),
        Ex("Tickets cost $7.99. How much do 5 cost?", ans="$39.95"),
        Ex("Show two different easy methods for 4.8 × 25.", ans="4.8 × 100 ÷ 4 = 120; 4.8 × 20 + 4.8 × 5 = 96 + 24 = 120.", think=True),
    ],
    check=["Can I use compensation?", "Can I re-order or split to make it easier?", "Can I explain which method I chose and why?"], look=[], note=NOTE)
