# -*- coding: utf-8 -*-
"""Stage 7 Unit 13 Earth Processes — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NOAAML", "name": "NOAA Global Monitoring Laboratory – Trends in atmospheric carbon dioxide (Mauna Loa)", "url": "https://gml.noaa.gov/ccgg/trends/", "use": "Annual mean CO₂ values used for the video graph and Challenge question (13.3)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "u13n11": dict(note="Paused on the chart: crust ≈35 km, mantle ≈2900 km, outer core ≈2200 km, inner core radius ≈1220 km.",
   q=mc("u13n11_q", "M", "O1", "Which layer is the thickest?", ("The mantle", "Yes – about 2900 km."),
        [("The crust", "The crust is the thinnest."), ("The outer core", "About 2200 km, less than the mantle."), ("The inner core", "Its radius is about 1220 km.")], skill="Data"),
   twin=mc("u13n11_t", "H", "O1", "Why is the crust compared to the skin of an apple?", "It is very thin compared with the whole Earth", [("It is red", ""), ("It is the hottest layer", ""), ("It is liquid", "")])),
 "u13n12p": dict(note="Paused before layers of modelling clay are pushed together from both ends.",
   q=mc("u13n12p_q", "M", "O2", "PREDICT: what will happen to the layers?", ("They will fold upwards", "Good prediction – now watch."),
        [("They will stay flat", "Watch carefully."), ("They will separate into a gap", "That happens when plates move apart."), ("They will melt", "Nothing is heated.")], skill="Prediction"),
   twin=mc("u13n12p_t", "M", "O2", "Plates moving towards each other meet at a…", "convergent boundary", [("divergent boundary", ""), ("transform boundary", ""), ("crust boundary", "")])),
 "u13n12e": dict(note="Paused after the layers folded into hills and valleys.",
   q=ex("u13n12e_q", "H", "O2", "EXPLAIN what the model shows about how fold mountains form.",
        [("two (continental) plates move towards each other / collide", ["collid|towards|push|converg"]), ("rock layers are forced to fold / bend upwards", ["fold|bend|buckle|up"])],
        "When two continental plates collide at a convergent boundary, the rock layers have nowhere to go, so they are forced to fold upwards into mountains."),
   twin=mc("u13n12e_t", "M", "O2", "Which mountain range formed when the Indian Plate pushed into the Eurasian Plate?", "The Himalayas", [("The Andes", ""), ("The Alps", ""), ("The Rockies", "")])),
 "u13n13": dict(note="Paused on the Mauna Loa graph: 317 ppm in 1960 rising to 425 ppm in 2024.",
   q=mc("u13n13_q", "M", "O3", "What human activity is the main cause of this rise?", ("Burning fossil fuels", "Yes – plus cutting down forests."),
        [("Breathing", "That has not changed much."), ("Volcanoes erupting", "Volcanoes add much less than human activity."), ("Planting trees", "Trees remove carbon dioxide.")], skill="Data"),
   twin=nm("u13n13_t", "H", "O3", "By how many ppm did carbon dioxide rise from 1960 (317 ppm) to 2024 (425 ppm)?", 108, "ppm", tol=0, units=["ppm"])),
 "u13n14p": dict(note="Paused before the bowl of warm salty water is left in the sun.",
   q=mc("u13n14p_q", "M", "O4", "PREDICT: what will collect in the cup?", ("Fresh water that is not salty", "Good prediction – now watch."),
        [("Salty water", "Watch carefully – does the salt evaporate?"), ("Nothing", "Watch carefully."), ("Salt crystals only", "Watch carefully.")], skill="Prediction"),
   twin=mc("u13n14p_t", "M", "O4", "Liquid water turning into water vapour is…", "evaporation", [("condensation", ""), ("precipitation", ""), ("freezing", "")])),
 "u13n14e": dict(note="Paused after the cup collected fresh water.",
   q=gd("u13n14e_q", "H", "O4", "Match each part of the model to the water cycle process.", ["Process"],
        [("Warm water turning to vapour", ["Evaporation"]), ("Drops forming under the cold cling film", ["Condensation"]), ("Drops falling into the cup", ["Precipitation"])], extra=["Run-off"]),
   twin=mc("u13n14e_t", "H", "O4", "Why was the water in the cup not salty?", "Salt does not evaporate; only the water did", [("The ice removed the salt", ""), ("The cling film filtered the salt", ""), ("Salt turns into gas", "")])),
}

DROP = {"13.1": ["u13s1p01", "u13s1p03", "u13s1p15"], "13.2": ["u13s2p01", "u13s2p03", "u13s2p05"], "13.3": ["u13s3p01", "u13s3p04", "u13s3p16"], "13.4": ["u13s4p01", "u13s4p10", "u13s4p18"]}

TEMP = {"kind": "linegraph", "x": {"min": 0, "max": 6000, "step": 1000, "label": "Depth (km)"}, "y": {"min": 0, "max": 6000, "step": 1000, "label": "Temperature (°C, approximate)"},
        "series": [{"pts": [[0, 15], [100, 1300], [670, 1900], [2900, 3700], [5150, 5000], [6370, 5400]], "label": "Earth's interior"}]}
QUAKE = {"kind": "barchart", "labels": ["Pacific Ring of Fire", "Mid-Atlantic Ridge", "Himalayas", "middle of Australia"], "values": [81, 6, 9, 0.5], "ymax": 90, "step": 10, "ylabel": "Share of large earthquakes (%, approximate)", "xlabel": "Region"}
RAIN = {"kind": "barchart", "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "values": [0, 12, 25, 8, 0, 3, 15], "ymax": 30, "step": 5, "ylabel": "Rainfall (mm)", "xlabel": "Day"}
NEW_PRAC = {
 "13.1": [
  mc("u13s1p21", "M", "O1", "Use the graph. How does temperature change as you go deeper into the Earth?", "It increases", [("It decreases", "The line rises."), ("It stays the same", "The line is not flat."), ("It rises then falls to 0", "It keeps rising.")], fig=TEMP, skill="Data"),
  nm("u13s1p22", "H", "O1", "Use the graph. About what is the temperature at the boundary between the mantle and the outer core (2900 km)?", 3700, "°C", tol=150, units=["°C"], fig=TEMP, skill="Data"),
  od("u13s1p23", "M", "O1", "Order the layers from the surface to the centre.", ["crust", "mantle", "outer core", "inner core"]),
 ],
 "13.2": [
  mc("u13s2p21", "M", "O2", "Use the bar chart. Where do most large earthquakes happen?", "Around the Pacific Ring of Fire", [("In the middle of Australia", "That has the fewest."), ("Along the Mid-Atlantic Ridge", "Only about 6%."), ("In the Himalayas", "About 9%.")], fig=QUAKE, skill="Data"),
  ex("u13s2p22", "H", "O2", "Use the bar chart. Explain why almost no large earthquakes happen in the middle of Australia.",
     [("it is far from a plate boundary / in the middle of a plate", ["boundar|middle of (a|the) plate|edge"]), ("earthquakes happen where plates meet and stress builds up", ["meet|stress|rub|stick|plates move"])],
     "The middle of Australia is far from any plate boundary. Large earthquakes happen where plates meet and stress builds up between them.", fig=QUAKE),
  gd("u13s2p23", "H", "O2", "Which kind of boundary?", ["Boundary"],
     [("Plates move apart and magma fills the gap", ["Divergent"]), ("Two continental plates collide", ["Convergent"]), ("Plates slide past each other", ["Transform"])], extra=[]),
 ],
 "13.3": [
  nm("u13s3p21", "M", "O3", "Air is 21% oxygen. How much oxygen is in 300 litres of air?", 63, "litres", tol=0.5, units=["litres", "L", "l"]),
  mc("u13s3p22", "H", "O3", "Use the Mauna Loa data in the video: 1960 = 317 ppm, 1990 = 354 ppm, 2020 = 414 ppm. Which statement is correct?", "It rose more from 1990 to 2020 than from 1960 to 1990", [("It rose by the same amount in both periods", "37 ppm vs 60 ppm."), ("It fell after 1990", "It kept rising."), ("It rose more from 1960 to 1990", "37 ppm is less than 60 ppm.")], skill="Data"),
  ms("u13s3p23", "H", "O3", "Select TWO natural sources of gases in the air.", ["volcanic eruptions", "respiration by living things"], [("car exhausts", "That is human."), ("power stations", "That is human."), ("factories", "That is human.")]),
 ],
 "13.4": [
  nm("u13s4p21", "M", "O4", "Use the bar chart. What was the total rainfall for the week?", 63, "mm", tol=0, units=["mm"], fig=RAIN, skill="Data"),
  mc("u13s4p22", "H", "O4", "Use the bar chart. On which day were puddles most likely to dry up, and why?", "Friday – no rain fell and evaporation continued", [("Wednesday – it rained most", "More rain makes bigger puddles."), ("Sunday – it rained 15 mm", "Rain adds water."), ("Tuesday – it rained 12 mm", "Rain adds water.")], fig=RAIN, skill="Data"),
  od("u13s4p23", "H", "O4", "Order the journey of water from the sea back to the sea.", ["evaporation from the sea", "condensation into clouds", "precipitation as rain", "run-off into rivers"]),
 ],
}
NEW_ADV = {
 "13.3": [adv(ex("u13s3a5", "VH", "O3", "NOAA's measurements at Mauna Loa show carbon dioxide rising from about 317 ppm in 1960 to about 425 ppm in 2024, and the rise is getting faster. Suggest TWO reasons for the rise and ONE way people could slow it.",
     [("burning fossil fuels", ["fossil|coal|oil|gas|petrol|burn"]), ("deforestation / cutting down forests", ["forest|trees|deforest"]), ("renewable energy / plant trees / use less energy", ["renewable|solar|wind|plant|less energy|electric car|public transport"])],
     "The rise is mainly caused by burning fossil fuels and by cutting down and burning forests. People could slow it by switching to renewable energy such as solar and wind, and by planting trees.", need=2, src=src("SRC-NOAAML")))],
}

from tests_stage7_unit13_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
