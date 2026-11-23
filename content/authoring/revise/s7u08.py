# -*- coding: utf-8 -*-
"""Stage 7 Unit 8 Acids and Alkalis — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-EPAACID", "name": "U.S. EPA – What is Acid Rain?", "url": "https://www.epa.gov/acidrain/what-acid-rain", "use": "Facts for the acid-rain Challenge question (8.1): causes of acid rain; normal rain about pH 5.6."},
    {"id": "SRC-ACSCAB", "name": "American Chemical Society – Red Cabbage Indicator activity", "url": "https://www.acs.org/education/activities/red-cabbage-indicator.html", "use": "Idea for the household-solutions Challenge question (8.2)."},
    {"id": "SRC-SACAB", "name": "Scientific American – Cabbage Chemistry: Finding Acids and Bases", "url": "https://www.scientificamerican.com/article/bring-science-home-cabbage-chemistry/", "use": "Colour–pH chart for red cabbage indicator used in the Challenge question (8.3)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "u8n81p": dict(note="Paused before the gas from acid + marble chips bubbles through limewater.",
   q=mc("u8n81p_q", "M", "O1", "PREDICT: what will happen to the clear limewater?", ("It will turn milky", "Good prediction – now watch."),
        [("It will turn red", "Watch carefully."), ("Nothing will happen", "Watch carefully."), ("It will catch fire", "Limewater does not burn.")], skill="Prediction"),
   twin=mc("u8n81p_t", "M", "O1", "Marble chips are made of…", "calcium carbonate", [("sodium chloride", ""), ("iron oxide", ""), ("magnesium", "")])),
 "u8n81e": dict(note="Paused after the chips fizzed and the limewater turned milky.",
   q=ex("u8n81e_q", "H", "O1", "EXPLAIN what the experiment shows. Name the gas and give the word equation.",
        [("the gas is carbon dioxide", ["carbon dioxide|co2|co₂"]), ("acid + carbonate → salt + water + carbon dioxide", ["salt.{0,30}water|water.{0,30}salt"]), ("carbon dioxide turns limewater milky (the test)", ["limewater|milky|cloudy"])],
        "Acid + carbonate → salt + water + carbon dioxide. The gas is carbon dioxide, because it turned limewater milky.", need=2),
   twin=mc("u8n81e_t", "M", "O1", "Which gas gives a squeaky pop with a lighted splint?", "Hydrogen", [("Carbon dioxide", ""), ("Oxygen", ""), ("Nitrogen", "")])),
 "u8n82": dict(note="Paused after four products: toothpaste, soap, oven cleaner, antacid.",
   q=mc("u8n82_q", "M", "O2", "Which of these four products would turn red litmus blue?", ("All four – they are all alkaline", "Yes – alkalis turn red litmus blue."),
        [("Only the oven cleaner", "The others are alkaline too, just weaker."), ("None of them", "They are alkalis."), ("Only toothpaste and soap", "Oven cleaner and antacids are alkaline too.")]),
   twin=mc("u8n82_t", "H", "O2", "Why must you wear gloves when using oven cleaner?", "It contains a strong alkali, which is corrosive", [("It is very cold", ""), ("It is an acid that tastes sour", ""), ("It conducts heat", "")])),
 "u8n83p": dict(note="Paused before cabbage juice is added to lemon juice, water and baking soda.",
   q=mc("u8n83p_q", "M", "O3", "PREDICT: what colour will red cabbage juice turn in lemon juice?", ("Red", "Good prediction – now watch."),
        [("Green", "Watch carefully."), ("It stays purple", "Watch carefully."), ("Blue", "Watch carefully.")], skill="Prediction"),
   twin=mc("u8n83p_t", "M", "O3", "An indicator is a substance that…", "changes colour in acids and alkalis", [("neutralises acids", ""), ("makes a gas", ""), ("dissolves metals", "")])),
 "u8n83e": dict(note="Paused after the colours: red, purple, green.",
   q=gd("u8n83e_q", "H", "O3", "EXPLAIN the colours: acidic, neutral or alkaline?", ["Type"],
        [("Lemon juice (red)", ["Acidic"]), ("Pure water (purple)", ["Neutral"]), ("Baking soda (green)", ["Alkaline"])], extra=[]),
   twin=mc("u8n83e_t", "M", "O3", "Red cabbage juice turns green. The liquid is…", "alkaline", [("acidic", ""), ("neutral", ""), ("pure water", "")])),
 "u8n84": dict(note="Paused on the bar chart of pH values for seven substances.",
   q=mc("u8n84_q", "M", "O3", "Use the chart. Which is the strongest alkali, and which is the strongest acid?", ("Ammonia; lemon juice", "Yes – highest and lowest pH."),
        [("Soap; vinegar", "Ammonia is higher; lemon juice is lower."), ("Pure water; milk", "These are neutral and nearly neutral."), ("Lemon juice; ammonia", "That is the wrong way round.")], skill="Data"),
   twin=mc("u8n84_t", "M", "O3", "A pH of 7 means…", "neutral", [("strongly acidic", ""), ("strongly alkaline", ""), ("weakly acidic", "")])),
 "u8n85": dict(note="Paused on the pH curve: pH jumps through 7 at about 20 cm³.",
   q=nm("u8n85_q", "H", "O4", "Use the graph. How much alkali was needed to neutralise the acid exactly?", 20, "cm³", tol=0.5, units=["cm³", "cm3", "ml", "mL"], skill="Data"),
   twin=mc("u8n85_t", "M", "O4", "Adding alkali drop by drop with a burette to reach pH 7 is called…", "titration", [("evaporation", ""), ("filtration", ""), ("distillation", "")])),
}

DROP = {"8.1": ["u8s1p01", "u8s1p03", "u8s1p11"], "8.2": ["u8s2p01", "u8s2p03", "u8s2p04"], "8.3": ["u8s3p01", "u8s3p03", "u8s3p05"], "8.4": ["u8s4p01", "u8s4p02", "u8s4p04"]}

GAS = {"kind": "linegraph", "x": {"min": 0, "max": 5, "step": 1, "label": "Time (min)"}, "y": {"min": 0, "max": 60, "step": 10, "label": "Volume of gas (cm³)"},
       "series": [{"pts": [[0, 0], [1, 22], [2, 38], [3, 48], [4, 52], [5, 52]], "label": "marble chips + acid"}]}
CLEAN = {"kind": "barchart", "labels": ["window spray", "bleach", "oven cleaner", "washing-up liquid"], "values": [10, 12.5, 13.5, 8], "ymax": 14, "step": 2, "ylabel": "pH", "xlabel": "Cleaner"}
SOIL = {"kind": "barchart", "labels": ["field A", "field B", "field C", "field D"], "values": [4.5, 6.5, 7.5, 5.5], "ymax": 8, "step": 1, "ylabel": "Soil pH", "xlabel": "Field"}
NEUT = {"kind": "linegraph", "x": {"min": 0, "max": 30, "step": 5, "label": "Volume of alkali added (cm³)"}, "y": {"min": 0, "max": 14, "step": 2, "label": "pH"},
        "series": [{"pts": [[0, 1], [5, 1.2], [10, 1.5], [15, 2.2], [20, 3.5], [24, 7], [26, 10.5], [30, 12]], "label": "pH"}]}
NEW_PRAC = {
 "8.1": [
  nm("u8s1p21", "M", "O1", "Marble chips react with acid. Use the graph. What volume of gas had been made after 2 minutes?", 38, "cm³", tol=1, units=["cm³", "cm3"], fig=GAS, skill="Data"),
  mc("u8s1p22", "H", "O1", "Use the graph. Why does the line become flat after 4 minutes?", "The reaction has stopped because the acid or the marble has been used up", [("The gas has turned into liquid", "The gas is still there."), ("The reaction is getting faster", "A flat line means no more gas is made."), ("The limewater has run out", "Limewater is not part of this reaction.")], fig=GAS, skill="Data"),
  od("u8s1p23", "H", "O1", "Put the steps in order to test the gas from acid + marble chips.", ["Add marble chips to dilute acid in a test tube", "Fit a delivery tube into the test tube", "Bubble the gas through limewater", "Observe whether the limewater turns milky"]),
 ],
 "8.2": [
  mc("u8s2p21", "M", "O2", "Use the bar chart. Which cleaner is the strongest alkali?", "Oven cleaner", [("Bleach", "Bleach has a lower pH than oven cleaner."), ("Window spray", "Window spray has pH 10."), ("Washing-up liquid", "This has the lowest pH.")], fig=CLEAN, skill="Data"),
  mc("u8s2p22", "H", "O2", "Use the bar chart. Which cleaner is the safest to touch with bare hands, and why?", "Washing-up liquid – its pH is closest to 7", [("Oven cleaner – it has the highest pH", "The higher the pH, the more corrosive."), ("Bleach – it is a cleaner", "Bleach is strongly alkaline."), ("They are all equally safe", "Their pH values are very different.")], fig=CLEAN, skill="Data"),
  gd("u8s2p23", "H", "O2", "A student tests four liquids with red and blue litmus. Acid, alkali or neutral?", ["Type"],
     [("Red stays red, blue turns red", ["Acid"]), ("Red turns blue, blue stays blue", ["Alkali"]), ("Red stays red, blue stays blue", ["Neutral"])], extra=[]),
 ],
 "8.3": [
  mc("u8s3p21", "M", "O3", "Use the bar chart. Which field has the most acidic soil?", "Field A", [("Field B", "Field B has pH 6.5."), ("Field C", "Field C is slightly alkaline."), ("Field D", "Field D has pH 5.5, higher than field A.")], fig=SOIL, skill="Data"),
  mc("u8s3p22", "H", "O3", "Use the bar chart. In which field would hydrangeas most likely have pink flowers?", "Field C", [("Field A", "Acidic soil gives blue flowers."), ("Field D", "This soil is acidic."), ("Field B", "Field C is the only one above 7.")], fig=SOIL, skill="Data"),
  ex("u8s3p23", "H", "O3", "Describe how to find the pH of a soil sample using Universal Indicator.",
     [("mix soil with (distilled) water and let it settle / filter", ["water|settle|filter|mix"]), ("add Universal Indicator (paper or solution)", ["universal indicator|indicator"]), ("compare the colour with the colour chart", ["compare|chart"])],
     "Mix the soil with distilled water, let it settle or filter it, add a few drops of Universal Indicator to the clear liquid, then compare the colour with the pH colour chart.", need=2),
 ],
 "8.4": [
  nm("u8s4p21", "H", "O4", "Use the graph. At what volume of alkali was the solution neutral?", 24, "cm³", tol=0.5, units=["cm³", "cm3"], fig=NEUT, skill="Data"),
  mc("u8s4p22", "H", "O4", "Use the graph. What is the pH after 30 cm³ of alkali has been added?", "About 12 – alkaline", [("About 7 – neutral", "Neutral was reached at 24 cm³."), ("About 1 – acidic", "That was at the start."), ("About 3.5 – acidic", "That was at 20 cm³.")], fig=NEUT, skill="Data"),
  ex("u8s4p23", "H", "O4", "A student makes salt by neutralising an acid with an alkali. Describe how she can get dry salt crystals from the neutral solution.",
     [("heat / evaporate the water", ["heat|evaporat|warm"]), ("leave to cool / crystallise", ["cool|crystal|dry"])],
     "Heat the neutral solution in an evaporating basin to evaporate some of the water, then leave it to cool so salt crystals form, and dry them."),
 ],
}
NEW_ADV = {
 "8.1": [adv(ex("u8s1a5", "VH", "O1", "Normal rain has a pH of about 5.6, but acid rain can have a pH of about 4.3. Explain why normal rain is slightly acidic, and what makes acid rain more acidic.",
     [("carbon dioxide dissolves in rain → weak (carbonic) acid", ["carbon dioxide|carbonic|co2"]), ("sulfur dioxide / nitrogen oxides from burning fuels", ["sulfur|sulphur|nitrogen|so2|no2|nox"]), ("these form sulfuric / nitric acid in the air", ["sulfuric|sulphuric|nitric|form acid|make acid"])],
     "Normal rain is slightly acidic because carbon dioxide from the air dissolves in it, making weak carbonic acid. Burning fossil fuels releases sulfur dioxide and nitrogen oxides, which react with water in the air to make sulfuric and nitric acids, so acid rain has a lower pH.", need=2, src=src("SRC-EPAACID")))],
 "8.2": [adv(mc("u8s2a5", "VH", "O2", "Red cabbage indicator turns blue-green in a window cleaner and greenish-yellow in an oven cleaner. What can you conclude?", "Both are alkaline, and the oven cleaner is the stronger alkali",
     [("Both are acidic", "Green and yellow colours show alkalis."), ("The window cleaner is the stronger alkali", "Greenish-yellow shows a higher pH."), ("Both are neutral", "Neutral stays purple.")], src=src("SRC-ACSCAB")))],
 "8.3": [adv(mc("u8s3a5", "VH", "O3", "Red cabbage indicator is red at about pH 2, purple at pH 4, violet at pH 6, blue at pH 8, blue-green at pH 10 and greenish-yellow at pH 12. A liquid turns it blue. What is its approximate pH and type?", "About 8 – weakly alkaline",
     [("About 2 – strongly acidic", "Red shows pH 2."), ("About 12 – strongly alkaline", "Greenish-yellow shows pH 12."), ("Exactly 7 – neutral", "Blue is above 7.")], skill="Data", src=src("SRC-SACAB")))],
}

from tests_stage7_unit08_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
