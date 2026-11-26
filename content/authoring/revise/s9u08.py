# -*- coding: utf-8 -*-
"""Stage 9 Unit 8 Rate of Reaction — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-RSCTHIO", "name": "Royal Society of Chemistry – The effect of temperature on reaction rate (sodium thiosulfate and hydrochloric acid)", "url": "https://edu.rsc.org/experiments/the-effect-of-temperature-on-reaction-rate/448.article", "use": "The 'disappearing cross' method: Challenge question (8.3)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

SYR = {"kind": "linegraph", "x": {"min": 0, "max": 180, "step": 30, "label": "Time (s)"}, "y": {"min": 0, "max": 65, "step": 10, "label": "Volume of gas (cm³)"},
       "series": [{"pts": [[0, 0], [30, 24], [60, 40], [90, 50], [120, 56], [150, 58], [180, 58]], "label": "marble + acid"}]}
TAB = {"kind": "barchart", "labels": ["10 °C", "20 °C", "40 °C", "60 °C"], "values": [95, 62, 32, 18], "ymax": 100, "step": 20, "ylabel": "Time for fizzing to stop (s)"}

NEW_STOPS = {
 "s9u08n21": dict(note="Paused on the graph: 24 cm³ after 30 s, levelling off at 58 cm³ after 150 s.",
   q=nm("s9u08n21_q", "H", "O2", "Use the graph. What was the average rate of reaction in the first 30 s, in cm³/s?", 0.8, "cm³/s", tol=0, units=["cm³/s", "cm3/s"], fig=SYR, skill="Data"),
   twin=mc("s9u08n21_t", "M", "O3", "Why does the curve level off at 58 cm³?", "One reactant has been used up, so the reaction has stopped", [("The syringe is full", ""), ("The gas has turned into liquid", ""), ("The reaction is speeding up", "")])),
 "s9u08n31p": dict(note="Paused before a whole tablet and a crushed tablet are put in water.",
   q=mc("s9u08n31p_q", "M", "O4", "PREDICT: which tablet will stop fizzing first?", ("The crushed tablet", "Good prediction – now watch."),
        [("The whole tablet", "Watch carefully."), ("Both at the same time", "Watch carefully."), ("Neither will fizz", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u08n31p_t", "M", "O4", "Crushing a solid into powder increases its…", "surface area", [("mass", ""), ("temperature", ""), ("concentration", "")])),
 "s9u08n31e": dict(note="Paused after the crushed tablet stopped after 24 s and the whole tablet after 62 s.",
   q=ex("s9u08n31e_q", "H", "O4", "EXPLAIN the result using collision theory.",
        [("crushed: larger surface area / more particles exposed", ["surface area|exposed|more particles"]), ("more collisions per second, so faster reaction", ["more (frequent )?collisions|collide more|faster"])],
        "The crushed tablet has a larger surface area, so more particles are exposed to the water. There are more collisions every second, so the reaction is faster and finishes sooner."),
   twin=mc("s9u08n31e_t", "H", "O4", "Both tablets made the same total volume of gas because…", "they had the same mass of reactants", [("they were in the same glass", ""), ("they fizzed for the same time", ""), ("powder makes more gas", "")])),
 "s9u08n32": dict(note="Paused on the chart: 95 s at 10 °C, 62 s at 20 °C, 32 s at 40 °C, 18 s at 60 °C.",
   q=ex("s9u08n32_q", "H", "O4", "Describe the pattern and explain it using collision theory.",
        [("higher temperature → shorter time / faster reaction", ["higher temperature.{0,40}(shorter|faster|less time)|hotter.{0,40}(faster|shorter)|time (falls|decreases)"]), ("particles have more energy, move faster and collide more often / harder (more effective collisions)", ["more energy|faster|more often|harder|more collisions|effective"])],
        "The higher the temperature, the shorter the time, so the faster the reaction. At higher temperatures the particles have more energy, move faster and collide more often and with more energy, so there are more effective collisions each second.", skill="Data"),
   twin=nm("s9u08n32_t", "M", "O4", "Use the chart. How many times faster is the reaction at 60 °C than at 10 °C (to 1 decimal place)?", 5.3, "", tol=0.1, units=[""], fig=TAB)),
}

DROP = {"8.1": ["s9u08s1p03", "s9u08s1p11"], "8.2": ["s9u08s2p05", "s9u08s2p06", "s9u08s2p07"], "8.3": ["s9u08s3p03", "s9u08s3p07", "s9u08s3p05"]}

CONC = {"kind": "linegraph", "x": {"min": 0, "max": 120, "step": 20, "label": "Time (s)"}, "y": {"min": 0, "max": 50, "step": 10, "label": "Volume of hydrogen (cm³)"},
        "series": [{"pts": [[0, 0], [20, 22], [40, 36], [60, 44], [80, 47], [100, 48], [120, 48]], "label": "concentrated acid"},
                   {"pts": [[0, 0], [20, 10], [40, 19], [60, 27], [80, 34], [100, 40], [120, 44]], "label": "dilute acid"}]}
NEW_PRAC = {
 "8.1": [
  ex("s9u08s1p21", "H", "O1", "Vinegar and baking soda react in an open beaker on a balance. The mass goes down. Explain why mass is still conserved.",
     [("carbon dioxide gas is made and escapes into the air", ["gas|carbon dioxide|escape"]), ("atoms are not destroyed; total mass including the gas stays the same", ["not destroyed|conserv|same|including the gas|sealed"])],
     "The reaction makes carbon dioxide gas, which escapes from the open beaker into the air. No atoms are destroyed: if the gas were collected in a sealed container, the total mass would stay the same."),
  gd("s9u08s1p22", "M", "O1", "Physical or chemical change?", ["Type"],
     [("Ice melting", ["Physical"]), ("Wood burning", ["Chemical"]), ("Iron rusting", ["Chemical"]), ("Sugar dissolving", ["Physical"])], extra=[]),
 ],
 "8.2": [
  nm("s9u08s2p21", "M", "O2", "Use the graph. What was the final volume of gas?", 58, "cm³", tol=0, units=["cm³", "cm3"], fig=SYR, skill="Data"),
  mc("s9u08s2p22", "H", "O2", "Use the graph. When was the reaction fastest?", "In the first 30 seconds, where the curve is steepest", [("Between 150 and 180 s", "The curve is flat there."), ("At 90 s", "It is already slowing."), ("The rate is the same throughout", "The curve gets less steep.")], fig=SYR, skill="Data"),
 ],
 "8.3": [
  ex("s9u08s3p21", "H", "O4", "Use the graph. Compare the two reactions and explain the difference.",
     [("concentrated acid reacts faster (steeper at the start)", ["concentrated.{0,40}(faster|steeper|quicker)|steeper"]), ("more acid particles in the same volume → more collisions per second", ["more (acid )?particles|more collisions|crowded"])],
     "The concentrated acid reacts faster: its line is steeper at the start and levels off sooner. It has more acid particles in the same volume, so there are more collisions every second.", fig=CONC, skill="Data"),
  nm("s9u08s3p22", "M", "O4", "Use the graph. How much more hydrogen had the concentrated acid made than the dilute acid after 40 s?", 17, "cm³", tol=0, units=["cm³", "cm3"], fig=CONC, skill="Data"),
 ],
}
NEW_ADV = {
 "8.3": [adv(ex("s9u08s3a05", "VH", "O4", "In the RSC 'disappearing cross' practical, sodium thiosulfate solution reacts with hydrochloric acid and a cloudy precipitate of sulfur forms. The time for a cross under the flask to disappear is measured at different temperatures. Explain how this measures the rate, and suggest TWO ways to make the results more reliable.",
     [("the cross disappears when a fixed amount of sulfur has formed; a shorter time means a faster rate", ["fixed amount|same amount|shorter time.{0,30}faster|faster.{0,30}shorter|rate.{0,20}(1|one) ?÷|1/time"]), ("repeat each temperature and take a mean", ["repeat|mean|average"]), ("same person / same cross / same volumes and concentrations; measure temperature accurately", ["same person|same cross|same volume|same concentration|thermometer|water bath"])],
     "The cross disappears when a fixed amount of sulfur has formed, so the time taken shows how fast the reaction is: a shorter time means a faster rate (rate ∝ 1 ÷ time). To make the results more reliable, repeat each temperature and calculate a mean, and keep the volumes, concentrations, flask and cross the same, with the same person judging when the cross disappears.", need=2, src=src("SRC-RSCTHIO")))],
}

from tests_stage9_unit08_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
