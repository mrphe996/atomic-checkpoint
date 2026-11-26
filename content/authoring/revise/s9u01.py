# -*- coding: utf-8 -*-
"""Stage 9 Unit 1 Photosynthesis and Transport in Plants — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-SAPSPOND", "name": "Science and Plants for Schools (SAPS) – Demonstrating oxygen evolution during photosynthesis using pondweed", "url": "https://www.saps.org.uk/pondweed", "use": "Pondweed practical and the Challenge question on measuring the rate (1.1)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

BUB = {"kind": "linegraph", "x": {"min": 0, "max": 60, "step": 10, "label": "Distance of lamp (cm)"}, "y": {"min": 0, "max": 45, "step": 5, "label": "Bubbles per minute"},
       "series": [{"pts": [[10, 40], [20, 26], [30, 15], [40, 9], [50, 6]], "label": "pondweed"}]}

NEW_STOPS = {
 "s9u01n11p": dict(note="Paused before pondweed is lit by a lamp 10 cm away and another 50 cm away.",
   q=mc("s9u01n11p_q", "M", "O1", "PREDICT: which pondweed will give off more bubbles?", ("The one 10 cm from the lamp", "Good prediction – now watch."),
        [("The one 50 cm from the lamp", "Watch carefully."), ("Both the same", "Watch carefully."), ("Neither will make bubbles", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u01n11p_t", "M", "O1", "Which gas is in the bubbles from pondweed in light?", "Oxygen", [("Carbon dioxide", ""), ("Nitrogen", ""), ("Hydrogen", "")])),
 "s9u01n11e": dict(note="Paused after the near pondweed gave about 40 bubbles a minute and the far one about 6.",
   q=ex("s9u01n11e_q", "H", "O1", "EXPLAIN why the pondweed near the lamp gave off more bubbles.",
        [("more light (energy) reaches it", ["more light|brighter|light intensity|more energy"]), ("so photosynthesis is faster and more oxygen is made", ["faster|rate|more oxygen|more photosynthesis"])],
        "The pondweed near the lamp receives more light energy, so it photosynthesises faster and makes more oxygen, which forms more bubbles."),
   twin=mc("s9u01n11e_t", "M", "O1", "The word equation for photosynthesis is…", "carbon dioxide + water → glucose + oxygen", [("glucose + oxygen → carbon dioxide + water", ""), ("oxygen + water → glucose + carbon dioxide", ""), ("carbon dioxide + oxygen → glucose + water", "")])),
 "s9u01n12": dict(note="Paused on the graph: 40, 26, 15, 9, 6 bubbles a minute at 10–50 cm.",
   q=ex("s9u01n12_q", "H", "O2", "Name the independent variable and explain why the water temperature must be kept the same.",
        [("independent variable: distance of the lamp / light intensity", ["distance|light intensity"]), ("temperature also affects the rate of photosynthesis, so it must be controlled for a fair test", ["temperature.{0,40}(affect|change)|fair|control"])],
        "The independent variable is the distance of the lamp (the light intensity). Temperature also affects the rate of photosynthesis, so it must be kept the same for a fair test.", skill="Data"),
   twin=nm("s9u01n12_t", "M", "O2", "Use the graph. How many bubbles per minute were given off with the lamp at 30 cm?", 15, "bubbles per minute", tol=0, units=["bubbles per minute", ""], fig=BUB)),
 "s9u01n21p": dict(note="Paused before celery stands in red-coloured water for a day.",
   q=mc("s9u01n21p_q", "M", "O4", "PREDICT: where will the red colour end up?", ("In tubes up the stalk and in the leaf veins", "Good prediction – now watch."),
        [("Only at the bottom of the stalk", "Watch carefully."), ("Evenly in every cell", "Watch carefully."), ("Nowhere: the plant will not take it up", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u01n21p_t", "M", "O4", "Water enters a plant mainly through…", "root hair cells", [("the stomata", ""), ("the flowers", ""), ("the xylem in the leaves", "")])),
 "s9u01n21e": dict(note="Paused after the leaf veins turned red and the cut stalk showed a ring of red dots.",
   q=ex("s9u01n21e_q", "H", "O4", "EXPLAIN the result.",
        [("the coloured water travels up in the xylem (vessels)", ["xylem"]), ("pulled up by transpiration / evaporation from the leaves", ["transpiration|evaporat|pulled|leaves"])],
        "The red water travelled up the stalk in the xylem vessels, which carry water and mineral salts to the leaves. Transpiration, the evaporation of water from the leaves, pulls more water up behind it."),
   twin=mc("s9u01n21e_t", "M", "O4", "Which change would make the colour climb faster?", "Putting the celery in a warm, breezy place", [("Putting it in a dark cupboard", ""), ("Covering the leaves with a plastic bag", ""), ("Removing all the leaves", "")])),
}

DROP = {"1.1": ["s9u01s1p02", "s9u01s1p05", "s9u01s1p06"], "1.2": ["s9u01s2p09", "s9u01s2p11", "s9u01s2p01"]}

TEMP = {"kind": "barchart", "labels": ["10 °C", "20 °C", "30 °C", "40 °C", "50 °C"], "values": [8, 18, 30, 22, 3], "ymax": 35, "step": 5, "ylabel": "Bubbles per minute"}
MASS = {"kind": "linegraph", "x": {"min": 0, "max": 6, "step": 1, "label": "Time (hours)"}, "y": {"min": 240, "max": 252, "step": 2, "label": "Mass of potted plant (g)"},
        "series": [{"pts": [[0, 250], [1, 249], [2, 248], [3, 247], [4, 246], [5, 245], [6, 244]], "label": "in sunlight"}]}
NEW_PRAC = {
 "1.1": [
  nm("s9u01s1p21", "M", "O2", "Use the chart. At which temperature was photosynthesis fastest?", 30, "°C", tol=0, units=["°C"], fig=TEMP, skill="Data"),
  ex("s9u01s1p22", "H", "O2", "Use the chart. Describe and explain the pattern above 30 °C.",
     [("the rate falls above 30 °C (to 3 bubbles at 50 °C)", ["falls|decreas|drops|fewer|3"]), ("enzymes for photosynthesis are damaged / denatured by high temperatures", ["enzyme|denatur|damage"])],
     "Above 30 °C the rate falls, to only 3 bubbles a minute at 50 °C, because the enzymes that control photosynthesis are damaged by the high temperature.", fig=TEMP, skill="Data"),
  od("s9u01s1p23", "H", "O1", "Put the steps of the starch test on a leaf in order.", ["Boil the leaf in water", "Put it in hot ethanol to remove the chlorophyll", "Rinse it in water to soften it", "Add iodine solution and look for blue-black"]),
 ],
 "1.2": [
  nm("s9u01s2p21", "M", "O3", "Use the graph. How much mass did the plant lose in 6 hours?", 6, "g", tol=0, units=["g"], fig=MASS, skill="Data"),
  ex("s9u01s2p22", "H", "O3", "Use the graph. Explain why the plant lost mass.",
     [("water evaporated from the leaves / transpiration", ["transpir|evaporat|water vapour"]), ("through the stomata, in sunlight", ["stomata|leaves|sun|light"])],
     "The plant lost water by transpiration: water evaporated from the leaves and escaped as water vapour through the stomata, which are open in sunlight.", fig=MASS, skill="Data"),
 ],
}
NEW_ADV = {
 "1.1": [adv(ex("s9u01s1a05", "VH", "O2", "SAPS suggests measuring the rate of photosynthesis in pondweed either by counting bubbles or by collecting the gas and measuring its volume. Evaluate which method gives more reliable results.",
     [("bubbles can be different sizes, so counting is less accurate", ["different size|size|vary|not the same"]), ("collecting gas and measuring volume is more accurate / measures the total amount", ["volume|collect|syringe|measur"]), ("repeat and take a mean / control temperature and CO₂", ["repeat|mean|average|control|temperature|carbon dioxide"])],
     "Counting bubbles is quick, but bubbles are different sizes and can be missed, so it is less accurate. Collecting the gas in a syringe or measuring cylinder and measuring its volume measures the total amount of oxygen, so it is more reliable. Either way, each reading should be repeated and a mean taken, with the temperature kept the same.", need=2, src=src("SRC-SAPSPOND")))],
}

from tests_stage9_unit01_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
