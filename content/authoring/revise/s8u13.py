# -*- coding: utf-8 -*-
"""Stage 8 Unit 13 Weather and Climate — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NOAAML", "name": "NOAA Global Monitoring Laboratory – Trends in atmospheric carbon dioxide (Mauna Loa)", "url": "https://gml.noaa.gov/ccgg/trends/", "use": "Annual mean CO₂ values for the video graph and the Challenge question (13.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

ML = {"kind": "linegraph", "x": {"min": 1960, "max": 2020, "step": 10, "label": "Year"}, "y": {"min": 300, "max": 430, "step": 20, "label": "CO₂ (parts per million)"},
      "series": [{"pts": [[1960, 317], [1970, 326], [1980, 339], [1990, 354], [2000, 370], [2010, 390], [2020, 414]], "label": "Mauna Loa"}]}

NEW_STOPS = {
 "s8u13n12": dict(note="Paused on the climate graph: January 4 °C, July and August 19 °C.",
   q=mc("s8u13n12_q", "H", "O1", "One day in January reaches 15 °C. Does this change the city's climate?", ("No: it is one day of weather; climate is the average over about 30 years", "Yes."),
        [("Yes: the climate is now warmer", "One day hardly changes a 30-year average."), ("Yes: January is now summer", "No."), ("No: climate never changes", "Climate can change over long periods.")], skill="Data"),
   twin=nm("s8u13n12_t", "M", "O1", "Use the climate graph. What is the difference between the warmest and coldest monthly averages (19 °C and 4 °C)?", 15, "°C", tol=0, units=["°C"])),
 "s8u13n11p": dict(note="Paused before one torch shines straight down and one at an angle on squared paper.",
   q=mc("s8u13n11p_q", "M", "O2", "PREDICT: which patch of light will be brighter?", ("The patch from the torch pointing straight down", "Good prediction – now watch."),
        [("The patch from the tilted torch", "Watch carefully."), ("Both the same", "Watch carefully."), ("Neither, the light will not reach", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u13n11p_t", "M", "O2", "Latitude is…", "how far a place is from the equator", [("how high a place is", ""), ("how mountainous a place is", ""), ("how close to the sea it is", "")])),
 "s8u13n11e": dict(note="Paused after the straight torch made a small bright patch and the tilted torch a large dim one.",
   q=ex("s8u13n11e_q", "H", "O2", "EXPLAIN how this models why the poles are colder than the equator.",
        [("at an angle the same energy is spread over a larger area", ["larger area|bigger area|spread"]), ("near the poles the Sun's rays arrive at a low angle, so less energy per square metre / colder", ["pole|low angle|less energy|colder|cold"])],
        "When the beam arrives at an angle, the same energy is spread over a larger area, so each part gets less. Near the poles the Sun's rays arrive at a low angle, so the energy is spread out and it is colder; at the equator they arrive almost straight down."),
   twin=mc("s8u13n11e_t", "M", "O2", "Which factor affecting climate does the torch model show?", "Latitude", [("Altitude", ""), ("Relief", ""), ("Distance from the sea", "")])),
 "s8u13n21": dict(note="Paused on the Mauna Loa graph: 317 ppm in 1960, 354 ppm in 1990, 414 ppm in 2020.",
   q=nm("s8u13n21_q", "H", "O4", "Use the graph. By how much did carbon dioxide rise from 1960 to 2020?", 97, "ppm", tol=1, units=["ppm", "parts per million"], fig=ML, skill="Data"),
   twin=mc("s8u13n21_t", "M", "O4", "What is the main cause of the rise in carbon dioxide since 1960?", "Burning fossil fuels", [("Volcanoes erupting more", ""), ("Plants making more oxygen", ""), ("The Sun getting hotter", "")])),
 "s8u13n22p": dict(note="Paused before an open jar and a jar with a clear lid are put under a lamp.",
   q=mc("s8u13n22p_q", "M", "O4", "PREDICT: which jar will warm up more?", ("The jar with the lid", "Good prediction – now watch."),
        [("The open jar", "Watch carefully."), ("Both the same", "Watch carefully."), ("Neither will warm", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u13n22p_t", "M", "O4", "Which is a greenhouse gas?", "Methane", [("Oxygen", ""), ("Nitrogen", ""), ("Argon", "")])),
 "s8u13n22e": dict(note="Paused after 20 minutes: open jar 26 °C, jar with lid 33 °C.",
   q=ex("s8u13n22e_q", "H", "O4", "EXPLAIN the result and link it to greenhouse gases.",
        [("the lid traps the warm air / heat inside", ["trap|stop.{0,20}escap|keeps? (the )?heat|cannot escape"]), ("greenhouse gases trap some of Earth's heat in a similar way, warming the planet", ["greenhouse|atmosphere|earth"])],
        "Light passes through the lid and warms the inside, and the lid traps the warm air so heat builds up. Greenhouse gases in the atmosphere trap some of the heat Earth gives off in a similar way, keeping the planet warmer."),
   twin=nm("s8u13n22e_t", "M", "O4", "How much warmer was the jar with the lid than the open jar after 20 minutes (33 °C and 26 °C)?", 7, "°C", tol=0, units=["°C"])),
}

DROP = {"13.1": ["s8u13s1p01", "s8u13s1p06", "s8u13s1p11"], "13.2": ["s8u13s2p01", "s8u13s2p09", "s8u13s2p12"]}

RAIN = {"kind": "barchart", "labels": ["Jan", "Mar", "May", "Jul", "Sep", "Nov"], "values": [20, 60, 250, 320, 280, 40], "ymax": 350, "step": 50, "ylabel": "Rainfall (mm)"}
ALT = {"kind": "linegraph", "x": {"min": 0, "max": 3000, "step": 500, "label": "Height above sea level (m)"}, "y": {"min": 0, "max": 30, "step": 5, "label": "Average temperature (°C)"},
       "series": [{"pts": [[0, 27], [1000, 20.5], [2000, 14], [3000, 7.5]], "label": "mountain"}]}
ICE = {"kind": "linegraph", "x": {"min": 0, "max": 400, "step": 100, "label": "Thousands of years ago"}, "y": {"min": -10, "max": 4, "step": 2, "label": "Temperature compared with today (°C)"},
       "series": [{"pts": [[0, 0], [20, -8], [125, 2], [150, -8], [240, 1], [270, -8], [330, 2], [350, -8], [400, 1]], "label": "ice core record"}]}
NEW_PRAC = {
 "13.1": [
  ex("s8u13s1p21", "H", "O1", "Use the chart. Describe the rainfall pattern in this tropical region.",
     [("a dry season around Nov–Mar (20–60 mm)", ["dry|20|40|60|low"]), ("a wet season May–Sep, highest in July (320 mm)", ["wet|rainy|monsoon|320|july|high"])],
     "There is a dry season from about November to March with very little rain (20–60 mm a month), and a wet season from May to September, with the most rain in July (320 mm).", fig=RAIN, skill="Data"),
  nm("s8u13s1p22", "M", "O2", "Use the graph. About how much does the temperature fall for every 1000 m you climb?", 6.5, "°C", tol=0.5, units=["°C"], fig=ALT, skill="Data"),
  mc("s8u13s1p23", "H", "O2", "Use the graph. Which factor affecting climate does it show?", "Altitude", [("Latitude", "Latitude is distance from the equator."), ("Relief", "Relief is the shape of the land."), ("Distance from the sea", "Not shown here.")], fig=ALT),
 ],
 "13.2": [
  nm("s8u13s2p21", "M", "O3", "Use the graph. About how many thousand years ago was the last glacial maximum (coldest point)?", 20, "thousand years ago", tol=5, units=["thousand years ago", ""], fig=ICE, skill="Data"),
  ex("s8u13s2p22", "H", "O3", "Use the graph. Describe the pattern and say what it shows about Earth's climate.",
     [("temperature goes up and down in cycles / repeating pattern", ["cycle|up and down|repeat|pattern|rises and falls"]), ("glacials (cold) and interglacials (warm) about every 100 000 years / climate changes naturally", ["100|glacial|interglacial|natural|ice age"])],
     "The temperature rises and falls in repeating cycles, with cold glacials and warm interglacials about every 100 000 years. Earth's climate has changed naturally many times.", fig=ICE, skill="Data"),
  mc("s8u13s2p23", "H", "O4", "Use the Mauna Loa graph. Which statement is best supported by the data?", "CO₂ rose every decade, and faster after 1990", [("CO₂ stayed the same", "It rose."), ("CO₂ fell after 2000", "It kept rising."), ("CO₂ rose only before 1980", "It kept rising.")], fig=ML, skill="Data"),
 ],
}
NEW_ADV = {
 "13.2": [adv(ex("s8u13s2a05", "VH", "O4", "NOAA's Mauna Loa record shows about 317 ppm of CO₂ in 1960 and 414 ppm in 2020. Calculate the average rise per year, and explain why the ice-core record of natural cycles does not mean today's warming is natural.",
     [("(414 − 317) ÷ 60 ≈ 1.6 ppm per year", ["1\\.6|1\\.62|97 ?÷ ?60"]), ("today's rise is much faster than natural changes, which took thousands of years", ["faster|quick|thousands|decades|rapid"]), ("it matches human emissions from burning fossil fuels / deforestation", ["fossil|human|burning|deforest|industr"])],
     "Average rise = (414 − 317) ÷ 60 ≈ 1.6 ppm per year. Natural changes between glacials and interglacials took thousands of years, but today's CO₂ and temperature are rising over decades, matching the CO₂ released by humans burning fossil fuels and cutting down forests.", need=2, src=src("SRC-NOAAML")))],
}

from tests_stage8_unit13_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
