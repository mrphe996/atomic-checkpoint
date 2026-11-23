# -*- coding: utf-8 -*-
"""Stage 7 Unit 2 Measurements — 2026 revision (written by the Atomic teaching team).
Practice: repeated unit-conversion and recall questions out; scale readings, data tables, graphs and
practical-method questions in. Challenge: ideas adapted from outside sources (named under the question)."""
from c_kit import *
from c_base import scale

SOURCES = [
    {"id": "SRC-BIPM", "name": "BIPM – The International System of Units (SI): the seven base units", "url": "https://www.bipm.org/en/measurement-units/si-base-units", "use": "SI base units question (2.1)."},
    {"id": "SRC-PAPER", "name": "Yale-New Haven Teachers Institute – Measuring paper thickness with a ruler (all measurements are estimates)", "url": "https://teachersinstitute.yale.edu/curriculum/units/1985/8/85.08.05/4", "use": "Idea for the 'measure many, divide' question (2.2)."},
    {"id": "SRC-NUFFREACT", "name": "Scientific American – Speedy Science: How Fast Can You React? (ruler-drop chart)", "url": "https://scientificamerican.com/article/bring-science-home-reaction-time", "use": "Ruler-drop distances and reaction times (2.6 graph and Challenge)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "u2n21": dict(note="Paused after four everyday measurements: 5 ml, 250 g, 38.5 °C, 10.52 s.",
   q=mc("u2n21_q", "M", "O1", "Which of these measurements is already given in an SI unit?", ("10.52 s", "Yes – the second is the SI unit of time."),
        [("250 g", "The SI unit of mass is the kilogram, not the gram."), ("38.5 °C", "The SI unit of temperature is the kelvin."), ("5 ml", "The SI unit of volume is the cubic metre.")]),
   twin=mc("u2n21_t", "M", "O1", "The SI unit of mass is the…", "kilogram", [("gram", ""), ("newton", ""), ("litre", "")])),
 "u2n22p": dict(note="Paused before the stack of 100 sheets is measured.",
   q=mc("u2n22p_q", "H", "O3", "PREDICT: how can you find the thickness of ONE sheet of paper with a 30 cm ruler?", ("Measure a stack of many identical sheets, then divide by the number of sheets", "Good thinking – now watch."),
        [("Measure one sheet very carefully", "One sheet is far thinner than the smallest mark (1 mm)."), ("Fold the sheet once and measure it", "Two layers are still too thin to read."), ("It cannot be done with a ruler", "It can – watch the method.")], skill="Prediction"),
   twin=nm("u2n22p_t", "M", "O3", "A stack of 200 sheets is 18 mm thick. How thick is one sheet?", 0.09, "mm")),
 "u2n22e": dict(note="Paused after 8 mm ÷ 100 = 0.08 mm.",
   q=ex("u2n22e_q", "H", "O3", "EXPLAIN why measuring 100 sheets and dividing gives a more accurate answer than trying to measure one sheet.",
        [("one sheet is smaller than the smallest scale division / too thin to read", ["too thin|smaller than|1 mm|smallest|can.?t read|cannot read"]), ("the stack is big enough to measure", ["stack|many|big enough|thick enough|100 sheets"]), ("the reading error is shared / divided by 100", ["error.{0,30}(divid|shar|small)|divid.{0,30}error|share"])],
        "One sheet is much thinner than 1 mm, the smallest mark on the ruler. A stack of 100 sheets is thick enough to measure, and any error in reading the ruler is divided by 100 too.", need=2),
   twin=nm("u2n22e_t", "H", "O3", "50 identical coins in a stack are 85 mm tall. How thick is one coin?", 1.7, "mm")),
 "u2n23p": dict(note="Paused before the squares under the leaf are counted.",
   q=mc("u2n23p_q", "M", "O4", "PREDICT: how can you find the area of a leaf with squared paper (1 cm squares)?", ("Draw round it and count the squares it covers, counting a square if more than half is covered", "Good – now watch."),
        [("Measure its length and multiply by 2", "A leaf is not a rectangle, so this would not work."), ("Weigh the leaf", "Weighing gives mass, not area."), ("Use a measuring cylinder", "That measures volume.")], skill="Prediction"),
   twin=nm("u2n23p_t", "M", "O4", "A shape covers 15 whole squares and 8 squares more than half covered. Each square is 1 cm². Estimate its area.", 23, "cm²", units=["cm²", "cm2"])),
 "u2n23e": dict(note="Paused after counting: about 32 cm².",
   q=mc("u2n23e_q", "H", "O4", "EXPLAIN: why would 0.5 cm squares give a more accurate area than 1 cm squares?", "There are fewer part-covered squares at the edge, so less is guessed",
        [("Smaller squares are easier to colour", "Colouring is not the reason."), ("The leaf gets smaller", "The leaf stays the same size."), ("Each square is worth more", "Each small square is worth less, not more.")]),
   twin=mc("u2n23e_t", "M", "O4", "When counting squares under a shape, a square that is less than half covered is…", "not counted", [("counted as one", ""), ("counted as two", ""), ("counted as half", "")])),
 "u2n24": dict(note="Paused after four everyday volumes: 5 ml, 330 ml, 1.5 l, 2 500 000 l.",
   q=nm("u2n24_q", "M", "O5", "How many 5 ml medicine spoons would fill a 1.5 l bottle?", 300, "spoons", units=["spoons", ""], errs=[(3, "Change 1.5 l into ml first (1.5 × 1000 = 1500 ml).")],
        hint="1.5 l = 1500 ml.", reason="1500 ÷ 5 = 300 spoons."),
   twin=nm("u2n24_t", "M", "O5", "How many millilitres are in 2.5 l?", 2500, "ml", units=["ml", "mL", "cm³"])),
 "u2n25p": dict(note="Paused with the dish of ice on the balance reading 150.0 g.",
   q=mc("u2n25p_q", "M", "O6", "PREDICT: when all the ice has melted, the balance reading will…", ("stay at 150.0 g", "Good prediction – now watch."),
        [("go up, because water is heavier than ice", "Watch carefully – nothing is added."), ("go down, because ice is solid", "Watch carefully – nothing is taken away."), ("show 0 g", "The water is still in the dish.")], skill="Prediction"),
   twin=mc("u2n25p_t", "M", "O6", "Mass is…", "the amount of matter in an object", [("the space an object takes up", ""), ("how hot an object is", ""), ("how long an object is", "")])),
 "u2n25e": dict(note="Paused after the result: still 150.0 g.",
   q=ex("u2n25e_q", "H", "O6", "EXPLAIN why the mass did not change when the ice melted.",
        [("no matter added or removed / same amount of matter", ["no matter|nothing (added|removed|taken)|same (amount|matter)|amount of matter"]), ("only the state / shape / volume changed", ["state|shape|volume|liquid|solid"])],
        "Melting only changes ice (solid) into water (liquid). No matter is added or taken away, so the amount of matter – the mass – stays the same."),
   twin=mc("u2n25e_t", "H", "O6", "Water freezes into ice in a sealed bottle. Its mass…", "stays the same", [("increases", ""), ("decreases", ""), ("becomes zero", "")])),
 "u2n26": dict(note="Paused on the reaction-time bar chart: 18, 16, 31, 17, 18 cm.",
   q=nm("u2n26_q", "H", "O7", "Ignore the outlier (31 cm). What is the mean distance the ruler fell?", 17.25, "cm", tol=0.05, hint="Add 18, 16, 17 and 18, then divide by 4.", reason="(18 + 16 + 17 + 18) ÷ 4 = 69 ÷ 4 = 17.25 cm.", skill="Data"),
   twin=mc("u2n26_t", "M", "O7", "Why do important races use electronic timing instead of a person with a stopwatch?", "A person's reaction time (about 0.2 s) adds error", [("Stopwatches cannot show seconds", ""), ("Electronic timers are cheaper", ""), ("Runners prefer it", "")])),
}

DROP = {
 "2.1": ["u2s1p04", "u2s1p05", "u2s1p09", "u2s1p16"],
 "2.2": ["u2s2p05", "u2s2p07", "u2s2p02", "u2s2p16"],
 "2.3": ["u2s3p02", "u2s3p06", "u2s3p12", "u2s3p15", "u2s3p09"],
 "2.4": ["u2s4p05", "u2s4p07", "u2s4p18"],
 "2.5": ["u2s5p02", "u2s5p03", "u2s5p17"],
 "2.6": ["u2s6p01", "u2s6p03", "u2s6p08", "u2s6p14"],
}
CLIPS = {"kind": "barchart", "labels": ["Ana", "Ben", "Chi", "Dan"], "values": [3.1, 3.0, 3.1, 4.6], "ymax": 5, "step": 1, "ylabel": "Length of clip (cm)", "xlabel": "Student"}
REACT = {"kind": "linegraph", "x": {"min": 0, "max": 40, "step": 10, "label": "Distance ruler falls (cm)"}, "y": {"min": 0, "max": 0.3, "step": 0.05, "label": "Reaction time (s)"},
         "series": [{"pts": [[5, 0.10], [10, 0.14], [15, 0.17], [20, 0.20], [25, 0.23], [30, 0.25], [35, 0.27]]}]}
NEW_PRAC = {
 "2.1": [
  gd("u2s1p21", "M", "O1", "Is each observation qualitative or quantitative?", ["Type"],
     [("The soup is very hot", ["Qualitative"]), ("The soup is at 72 °C", ["Quantitative"]), ("The plant has 14 leaves", ["Quantitative"]), ("The flower smells sweet", ["Qualitative"])], extra=[]),
  tb("u2s1p22", "H", "O1", "Complete the table: write the SI unit for each quantity.", ["Quantity", "SI unit"],
     [["length", {"ans": "metre"}], ["mass", {"ans": "kilogram"}], ["time", {"ans": "second"}]], hint="Use the full name: metre, kilogram, second, kelvin, ampere."),
  mt("u2s1p23", "M", "O1", "Match each measurement to the instrument used to make it.", [("38.5 °C", "thermometer"), ("250 g", "electronic balance"), ("10.52 s", "stopwatch"), ("5 ml", "measuring cylinder or syringe")]),
 ],
 "2.2": [
  nm("u2s2p21", "H", "O3", "A pupil measures 50 identical coins stacked on top of each other: 85 mm. How thick is one coin?", 1.7, "mm", errs=[(4250, "Divide the stack height by the number of coins.")], hint="Thickness of one = height of stack ÷ number of coins."),
  mc("u2s2p22", "H", "O3", "Four students measure the same paper clip. Look at the bar chart. Which result is the outlier?", "Dan's (4.6 cm)",
     [("Ana's (3.1 cm)", "Ana's result is close to the others."), ("Ben's (3.0 cm)", "Ben's is close to the others."), ("None – all are correct", "One bar is much taller than the rest.")], fig=CLIPS, skill="Data"),
  nm("u2s2p23", "H", "O3", "Use the bar chart. Leave out the outlier and calculate the mean length of the clip (2 d.p.).", 3.07, "cm", tol=0.01, fig=CLIPS, skill="Data", hint="(3.1 + 3.0 + 3.1) ÷ 3"),
  gd("u2s2p24", "H", "O3", "Choose the best instrument for each length.", ["Instrument"],
     [("Width of a pin", ["Vernier calipers"]), ("Distance around a tree trunk", ["Soft tape measure"]), ("Length of a football pitch", ["Measuring wheel"]), ("Length of a pencil", ["30 cm rule"])], extra=["Odometer"]),
 ],
 "2.3": [
  nm("u2s3p21", "M", "O4", "A leaf drawn on 1 cm squared paper covers 26 whole squares and 9 squares that are more than half covered. Estimate the area of the leaf.", 35, "cm²", units=["cm²", "cm2"],
     errs=[(26, "Also count the squares that are more than half covered."), (39.5, "Count each more-than-half square as 1, not as a half plus a whole.")]),
  nm("u2s3p22", "H", "O4", "An L-shaped room is made of two rectangles: 6 m × 4 m and 3 m × 2 m. What is the total floor area?", 30, "m²", units=["m²", "m2"], hint="Find each rectangle's area and add them."),
  mc("u2s3p23", "H", "O4", "Why do smaller squares give a more accurate estimate of the area of a leaf?", "Fewer squares are only partly covered at the edge, so less guessing is needed",
     [("Small squares are easier to count", "Counting is not what makes it more accurate."), ("The leaf is smaller on small squares", "The leaf stays the same."), ("Each square is worth more", "Each small square is worth less.")]),
  nm("u2s3p24", "H", "O4", "A pupil draws round her hand on 1 cm squared paper. She counts 64 whole squares and 22 squares more than half covered. Estimate the area of her hand.", 86, "cm²", units=["cm²", "cm2"]),
  tb("u2s3p25", "H", "O4", "Complete the table for these rectangles.", ["Base", "Height", "Area"], [["8 cm", "5 cm", {"ans": 40}], ["2.5 m", "4 m", {"ans": 10}], ["12 cm", {"ans": 6}, "72 cm²"]], hint="Area = base × height; height = area ÷ base."),
 ],
 "2.4": [
  scale("u2s4p21", "Read the volume of liquid in the measuring cylinder.", {"kind": "cylinder", "min": 0, "max": 100, "major": 20, "minor": 2, "value": 68, "unit": "cm³"},
        68, "cm³", "M", "O5", tol=0.5, units=["cm³", "cm3", "ml", "mL"], hint="Each small mark is 2 cm³. Read the bottom of the meniscus."),
  nm("u2s4p22", "H", "O5", "Use the diagram. What is the volume of the stone?", 26, "cm³", units=["cm³", "cm3", "ml", "mL"], fig={"kind": "displacement", "before": 46, "after": 72, "max": 100},
     errs=[(72, "That is the reading WITH the stone. Subtract the starting volume."), (118, "Subtract, do not add.")], skill="Data"),
  od("u2s4p23", "H", "O5", "Put the steps for finding the volume of a stone in order.", ["Pour water into a measuring cylinder", "Read the starting volume at eye level", "Lower the stone in gently on a string", "Read the new volume", "Subtract the starting volume from the new volume"]),
 ],
 "2.5": [
  nm("u2s5p21", "M", "O6", "An empty beaker on a balance reads 64.5 g. The pupil presses TARE, then adds salt. The balance now reads 12.8 g. What is the mass of the salt?", 12.8, "g",
     errs=[(77.3, "After pressing tare, the balance shows only what you add."), (51.7, "The tare button already removed the beaker's mass.")]),
  mc("u2s5p22", "H", "O6", "A sealed bottle of water has a mass of 520 g. It is frozen solid. What is its mass now?", "520 g",
     [("More than 520 g, because ice is heavier", "Freezing changes the state, not the amount of matter."), ("Less than 520 g, because ice floats", "Floating is about density, not mass."), ("0 g", "The ice is still there.")]),
  tb("u2s5p23", "H", "O6", "Complete the table.", ["Mass in kg", "Mass in g"], [["2", {"ans": 2000}], [{"ans": 0.45, "tol": 0.001}, "450"], ["1.2", {"ans": 1200}]]),
 ],
 "2.6": [
  num("u2s6p21", "Use the graph. A ruler falls 20 cm before a student catches it. What is the student's reaction time?", 0.20, "s", "M", "O7", skill="Data", tol=0.01, units=["s"], fig=REACT,
      hint="Go up from 20 cm to the line, then across."),
  mc("u2s6p22", "H", "O7", "Use the graph. What happens to the reaction time as the distance the ruler falls increases?", "The reaction time increases",
     [("The reaction time decreases", "Read the line – it goes up."), ("The reaction time stays the same", "The line is not flat."), ("There is no pattern", "There is a clear trend.")], fig=REACT, skill="Data"),
  nm("u2s6p23", "H", "O7", "20 swings of a pendulum take 31 s. How long does ONE swing take?", 1.55, "s", hint="Time many swings, then divide – like the paper stack."),
 ],
}

NEW_ADV = {
 "2.1": [adv(mt("u2s1a5", "VH", "O1", "There are seven SI base units. Match each quantity to its SI base unit.",
     [("length", "metre"), ("mass", "kilogram"), ("time", "second"), ("electric current", "ampere"), ("temperature", "kelvin")], src=src("SRC-BIPM")))],
 "2.2": [adv(ex("u2s2a5", "VH", "O3", "A pupil wants the diameter of a thin copper wire. She winds it tightly 20 times around a pencil, side by side. The coil is 9 mm long. Find the diameter and explain why this method is better than measuring one turn.",
     [("diameter = 9 ÷ 20 = 0.45 mm", ["0\\.45"]), ("one wire is thinner than the smallest scale mark", ["thin|smaller than|1 mm|smallest"]), ("reading error is shared over 20 turns", ["error.{0,30}(divid|shar|small)|divid|share|20"])],
     "9 mm ÷ 20 = 0.45 mm. One wire is thinner than the 1 mm marks on a ruler, but 20 turns make a length that can be read, and any reading error is shared between 20 turns.", need=2, src=src("SRC-PAPER")))],
 "2.6": [adv(ex("u2s6a5", "VH", "O7", "In a falling-ruler test, Lan's catches are 12, 14, 13 and 25 cm. Her partner says Lan has slow reactions. Use the data to evaluate this claim and suggest how to improve the test.",
     [("25 cm is an outlier / anomaly", ["25.{0,20}(outlier|anomal|odd|wrong|ignore)|outlier|anomal"]), ("mean without it about 13 cm, which is fast / short", ["13|short|fast|quick"]), ("improvement: more trials / same hand / no warning / same person dropping", ["more trials|repeat|same hand|warning|same person|practice|more times"])],
     "25 cm is an outlier – perhaps she was distracted. Without it the mean is 13 cm, which is a short distance, so her reactions are not slow. Do more trials, use the same hand and the same person dropping the ruler.", need=2, src=src("SRC-NUFFREACT")))],
}

from tests_stage7_unit02_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
