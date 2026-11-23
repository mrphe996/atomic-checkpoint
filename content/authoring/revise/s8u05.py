# -*- coding: utf-8 -*-
"""Stage 8 Unit 5 Mixtures and Solubility — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-BAOGOLD", "name": "The Birmingham Assay Office – Gold assay and hallmarking", "url": "https://www.theassayoffice.co.uk/our-services/hallmarking/gold-assay-and-hallmarking/", "use": "Fineness marks: 375 = 9 ct (37.5% gold), 750 = 18 ct (75%), 916 = 22 ct (91.6%) (video chart and Challenge question, 5.1)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s8u05n11": dict(note="Paused on the chart: 24 ct 99.9%, 22 ct 91.6%, 18 ct 75%, 9 ct 37.5% gold.",
   q=nm("s8u05n11_q", "H", "O2", "An 18 carat gold ring (75% gold) has a mass of 8 g. What mass of gold does it contain?", 6, "g", tol=0, units=["g"], skill="Data"),
   twin=mc("s8u05n11_t", "M", "O2", "Which gold is the purest?", "24 carat", [("9 carat", ""), ("18 carat", ""), ("22 carat", "")])),
 "s8u05n12p": dict(note="Paused before water soaks up the paper past a spot of black ink.",
   q=mc("s8u05n12p_q", "M", "O3", "PREDICT: what will happen to the black ink spot?", ("It will separate into different colours", "Good prediction – now watch."),
        [("It will stay as one black spot", "Watch carefully."), ("It will disappear completely", "Watch carefully."), ("It will turn white", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u05n12p_t", "M", "O3", "Why is the starting line drawn in pencil, not pen?", "Pencil does not dissolve and run up the paper", [("Pencil is darker", ""), ("Pen is too slow", ""), ("Pencil is a solvent", "")])),
 "s8u05n12e": dict(note="Paused after the ink separated into yellow, red and blue spots.",
   q=ex("s8u05n12e_q", "H", "O3", "EXPLAIN why the black ink separated into three spots.",
        [("black ink is a mixture of dyes", ["mixture|several dyes|different dyes|three dyes"]), ("dyes travel / move up the paper at different speeds", ["different speed|different rate|further|faster|slower"])],
        "Black ink is a mixture of three dyes. They dissolve in the water but travel up the paper at different speeds, so they separate into different spots."),
   twin=mc("s8u05n12e_t", "M", "O3", "A pure substance on a chromatogram gives…", "one spot", [("three spots", ""), ("no spots", ""), ("a black line", "")])),
 "s8u05n13": dict(note="Paused on the solubility curve: 32 g at 20 °C, 110 g at 60 °C (per 100 g water).",
   q=nm("s8u05n13_q", "VH", "O4", "A saturated solution in 100 g of water at 60 °C is cooled to 20 °C. What mass of potassium nitrate crystals forms?", 78, "g", tol=1, units=["g"], skill="Data"),
   twin=nm("s8u05n13_t", "M", "O4", "Use the graph. What is the solubility of potassium nitrate at 40 °C (g per 100 g of water)?", 64, "g", tol=2, units=["g", "g per 100 g"])),
}

DROP = {"5.1": ["s8u05s1p03", "s8u05s1p04", "s8u05s1p10"], "5.2": ["s8u05s2p03", "s8u05s2p07", "s8u05s2p15"], "5.3": ["s8u05s3p03", "s8u05s3p05", "s8u05s3p07"]}

SALT = {"kind": "linegraph", "x": {"min": 0, "max": 100, "step": 20, "label": "Temperature (°C)"}, "y": {"min": 0, "max": 50, "step": 10, "label": "Solubility (g per 100 g of water)"},
        "series": [{"pts": [[0, 35.7], [20, 36.0], [40, 36.6], [60, 37.3], [80, 38.4], [100, 39.8]], "label": "sodium chloride"}]}
CHR = {"kind": "barchart", "labels": ["ink A", "ink B", "ink C", "ink X (unknown)"], "values": [1, 2, 3, 2], "ymax": 3, "step": 1, "ylabel": "Number of spots", "xlabel": "Ink"}
PURE = {"kind": "barchart", "labels": ["sample 1", "sample 2", "sample 3"], "values": [96, 88, 99], "ymax": 100, "step": 20, "ylabel": "Purity of aspirin (%)", "xlabel": "Sample"}
NEW_PRAC = {
 "5.1": [
  mc("s8u05s1p21", "M", "O2", "Use the bar chart. Which aspirin sample is purest?", "Sample 3", [("Sample 1", "96% is less than 99%."), ("Sample 2", "This is the least pure."), ("They are all the same", "The bars differ.")], fig=PURE, skill="Data"),
  nm("s8u05s1p22", "H", "O2", "Use the bar chart. A 500 mg tablet is made from sample 2. What mass is pure aspirin?", 440, "mg", tol=0, units=["mg"], fig=PURE, skill="Data"),
  gd("s8u05s1p23", "H", "O1", "Element, compound or mixture?", ["Type"],
     [("Oxygen gas", ["Element"]), ("Water", ["Compound"]), ("Sea water", ["Mixture"]), ("Air", ["Mixture"])], extra=[]),
 ],
 "5.2": [
  mc("s8u05s2p21", "M", "O3", "Use the bar chart of chromatography results. Which ink is a pure dye?", "Ink A", [("Ink B", "It gave two spots."), ("Ink C", "It gave three spots."), ("Ink X", "It gave two spots.")], fig=CHR, skill="Data"),
  mc("s8u05s2p22", "H", "O3", "Ink X gives two spots at the same heights as ink B. What can you conclude?", "Ink X is probably the same ink as ink B", [("Ink X is pure", "It gives two spots."), ("Ink X is ink C", "C gives three spots."), ("Nothing at all", "Matching spots are evidence.")], fig=CHR, skill="Data"),
  od("s8u05s2p23", "H", "O3", "Order the steps to get pure, dry salt from rock salt (salt mixed with sand).", ["Crush the rock salt", "Stir it in warm water to dissolve the salt", "Filter to remove the sand", "Evaporate the water from the filtrate"]),
 ],
 "5.3": [
  mc("s8u05s3p21", "M", "O4", "Use the graph. How does the solubility of sodium chloride change with temperature?", "It increases only slightly", [("It increases a lot", "The line is almost flat."), ("It decreases", "The line rises."), ("It stays exactly the same", "It rises a little.")], fig=SALT, skill="Data"),
  ex("s8u05s3p22", "H", "O4", "Use this graph and the potassium nitrate graph in the video. Explain why cooling a hot saturated solution gives many crystals of potassium nitrate but very few of salt.",
     [("potassium nitrate solubility falls a lot on cooling", ["potassium nitrate.{0,60}(falls|drops|decreases|much|lot)|steep"]), ("salt solubility hardly changes with temperature", ["salt|sodium chloride|hardly|little|flat|slight"])],
     "The solubility of potassium nitrate falls a lot as the solution cools, so much of it comes out as crystals. The solubility of salt hardly changes with temperature, so very little crystallises.", fig=SALT),
  nm("s8u05s3p23", "H", "O4", "25 g of sugar is dissolved to make 250 cm³ of solution. What is the concentration in g/dm³? (1 dm³ = 1000 cm³)", 100, "g/dm³", tol=0, units=["g/dm³", "g/dm3", "g/l", "g/L"]),
 ],
}
NEW_ADV = {
 "5.1": [adv(ex("s8u05s1a05", "VH", "O2", "Hallmarks show gold purity in parts per thousand: 375 for 9 carat, 750 for 18 carat and 916 for 22 carat. A 12 g bracelet is stamped 375. Calculate the mass of gold in it, and suggest why jewellers do not use pure gold.",
     [("12 × 0.375 = 4.5 g of gold", ["4\\.5"]), ("pure gold is too soft / alloys are harder / cheaper", ["soft|hard|scratch|bend|cheap|cost"])],
     "12 g × 375 ÷ 1000 = 4.5 g of gold. Pure gold is very soft and easily scratched or bent, so it is mixed with other metals to make a harder alloy (which is also cheaper).", src=src("SRC-BAOGOLD")))],
}

from tests_stage8_unit05_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
