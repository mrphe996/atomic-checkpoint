# -*- coding: utf-8 -*-
"""Stage 9 Unit 2 Excretion — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NIDDKKID", "name": "NIDDK (US National Institutes of Health) – Your Kidneys & How They Work", "url": "https://www.niddk.nih.gov/health-information/kidney-disease/kidneys-how-they-work", "use": "Nephrons filter the blood and tubules return needed substances: Challenge question (2.1)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

LOSS = {"kind": "barchart", "labels": ["urine", "sweat", "breathing out", "faeces"], "values": [1.5, 0.5, 0.4, 0.1], "ymax": 1.8, "step": 0.3, "ylabel": "Water lost per day (litres)"}

NEW_STOPS = {
 "s9u02n11p": dict(note="Paused before a student breathes onto a cold mirror.",
   q=mc("s9u02n11p_q", "M", "O1", "PREDICT: what will appear on the cold mirror?", ("A mist of tiny water droplets", "Good prediction – now watch."),
        [("Nothing at all", "Watch carefully."), ("A white powder", "Watch carefully."), ("A layer of ice", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u02n11p_t", "M", "O1", "Which organ excretes carbon dioxide?", "The lungs", [("The kidneys", ""), ("The bladder", ""), ("The stomach", "")])),
 "s9u02n11e": dict(note="Paused after a misty patch of water droplets appeared.",
   q=ex("s9u02n11e_q", "H", "O1", "EXPLAIN what appeared and why this shows the lungs are excretory organs.",
        [("breathed-out air contains water vapour, which condenses on the cold mirror", ["water vapour|condens"]), ("the water is a waste product of respiration, removed by the lungs", ["respiration|waste|excret|metabolism"])],
        "Breathed-out air contains water vapour, which condenses into droplets on the cold mirror. This water is a waste product of respiration in our cells, and the lungs remove it, so they are excretory organs."),
   twin=mc("s9u02n11e_t", "M", "O1", "Water vapour in breathed-out air is made by…", "respiration in our cells", [("photosynthesis", ""), ("the kidneys", ""), ("digesting protein", "")])),
 "s9u02n12": dict(note="Paused on the chart: urine 1.5 L, sweat 0.5 L, breathing out 0.4 L, faeces 0.1 L per day.",
   q=ex("s9u02n12_q", "H", "O3", "On a hot day, which amount would rise, and how would the kidneys respond?",
        [("sweat increases", ["sweat"]), ("the kidneys save water: less urine, more concentrated / darker", ["less urine|less water|concentrated|darker|save|conserve"])],
        "On a hot day you sweat more. To balance this, the kidneys save water, so they make less urine and it is more concentrated and darker.", skill="Data"),
   twin=nm("s9u02n12_t", "M", "O3", "Use the chart. What is the total water lost in one day?", 2.5, "litres", tol=0, units=["litres", "L"], fig=LOSS)),
 "s9u02n13": dict(note="Paused after four real-life examples: sport, drinking water, dialysis and organ donation.",
   q=mc("s9u02n13_q", "H", "O4", "Why can a living person donate one kidney?", ("One healthy kidney can filter enough blood to keep the body healthy", "Yes."),
        [("Kidneys grow back", "They do not."), ("The bladder takes over", "The bladder only stores urine."), ("The lungs filter urea instead", "Urea is removed by the kidneys.")]),
   twin=mc("s9u02n13_t", "M", "O4", "Dialysis is used when…", "the kidneys fail and cannot filter the blood", [("the lungs are damaged", ""), ("a person is thirsty", ""), ("the bladder is full", "")])),
}

DROP = {"2.1": ["s9u02s1p08", "s9u02s1p11", "s9u02s1p01", "s9u02s1p06"]}

UREA = {"kind": "barchart", "labels": ["low protein", "normal", "high protein"], "values": [15, 25, 40], "ymax": 45, "step": 5, "ylabel": "Urea in urine (g per day)"}
DRINK = {"kind": "linegraph", "x": {"min": 0, "max": 3, "step": 0.5, "label": "Water drunk in a morning (litres)"}, "y": {"min": 0, "max": 2.5, "step": 0.5, "label": "Urine made (litres)"},
         "series": [{"pts": [[0, 0.3], [0.5, 0.6], [1, 1.0], [1.5, 1.3], [2, 1.7], [3, 2.4]], "label": "one student"}]}
NEW_PRAC = {
 "2.1": [
  ex("s9u02s1p21", "H", "O2", "Use the chart. Explain why people on a high-protein diet excrete more urea.",
     [("urea is made when the body breaks down (extra) protein / amino acids", ["break.{0,10}down.{0,20}protein|protein.{0,30}broken|amino"]), ("more protein eaten → more urea made (40 g v 25 g)", ["more protein|40|extra protein"])],
     "Urea is made in the liver when the body breaks down protein it does not need. On a high-protein diet more extra protein is broken down, so more urea is made and excreted: 40 g a day compared with 25 g.", fig=UREA, skill="Data"),
  nm("s9u02s1p22", "M", "O3", "Use the graph. How much urine was made after drinking 2 litres of water?", 1.7, "litres", tol=0.05, units=["litres", "L"], fig=DRINK, skill="Data"),
  mc("s9u02s1p23", "H", "O3", "Use the graph. What is the pattern?", "The more water drunk, the more urine is made", [("The more water drunk, the less urine", "The line rises."), ("Urine does not change", "It changes."), ("No urine is made without drinking", "0.3 L is still made.")], fig=DRINK, skill="Data"),
  od("s9u02s1p24", "M", "O4", "Put the parts in the order urine passes through them.", ["kidney", "ureter", "bladder", "urethra"]),
 ],
}
NEW_ADV = {
 "2.1": [adv(ex("s9u02s1a05", "VH", "O4", "NIDDK explains that each kidney has about a million nephrons: a filter (glomerulus) removes water and small substances from the blood, and a tubule returns the substances the body needs. The kidneys filter about 180 litres of fluid a day but make only about 1.5 litres of urine. Calculate the percentage of the filtered fluid that is returned to the blood, and explain why this return is essential.",
     [("(180 − 1.5) ÷ 180 × 100 ≈ 99 %", ["99"]), ("needed substances such as glucose, water and useful salts are returned", ["glucose|water|salt|useful|needed"]), ("otherwise we would lose huge amounts of water / dehydrate quickly", ["dehydrat|lose.{0,20}water|180|would die|run out"])],
     "(180 − 1.5) ÷ 180 × 100 ≈ 99 %, so about 99 % of the filtered fluid is returned to the blood. The tubules return water, glucose and useful salts; without this we would lose about 180 litres of water a day and would quickly become dehydrated and die.", need=2, src=src("SRC-NIDDKKID")))],
}

from tests_stage9_unit02_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
