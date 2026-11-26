# -*- coding: utf-8 -*-
"""Stage 9 Unit 9 Density — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-USCGIIP", "name": "US Coast Guard International Ice Patrol – Iceberg Formation (fact sheet)", "url": "https://www.navcen.uscg.gov/sites/default/files/pdf/iip/Iceberg_Formation.pdf", "use": "About 7/8 of an iceberg is below the waterline: Challenge question (9.3)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

ALU = {"kind": "linegraph", "x": {"min": 0, "max": 50, "step": 10, "label": "Volume (cm³)"}, "y": {"min": 0, "max": 140, "step": 20, "label": "Mass (g)"},
       "series": [{"pts": [[0, 0], [10, 27], [20, 54], [30, 81], [40, 108]], "label": "aluminium"}]}
DEN = {"kind": "barchart", "labels": ["cork", "ice", "water", "aluminium", "iron", "lead"], "values": [0.24, 0.92, 1.0, 2.7, 7.9, 11.3], "ymax": 12, "step": 2, "ylabel": "Density (g/cm³)"}

NEW_STOPS = {
 "s9u09n11": dict(note="Paused on the graph: aluminium blocks 10, 20, 30, 40 cm³ with masses 27, 54, 81, 108 g.",
   q=nm("s9u09n11_q", "H", "O2", "Use the graph. What is the density of aluminium?", 2.7, "g/cm³", tol=0, units=["g/cm³", "g/cm3"], fig=ALU, skill="Data"),
   twin=mc("s9u09n11_t", "M", "O2", "A 50 cm³ block of the same aluminium has a density of…", "2.7 g/cm³, the same as the others", [("5.4 g/cm³", ""), ("135 g/cm³", ""), ("0.37 g/cm³", "")])),
 "s9u09n21": dict(note="Paused on the chart: cork 0.24, ice 0.92, water 1.0, aluminium 2.7, iron 7.9, lead 11.3 g/cm³.",
   q=gd("s9u09n21_q", "M", "O3", "Float or sink in water?", ["In water"],
        [("Cork", ["Float"]), ("Ice", ["Float"]), ("Aluminium", ["Sink"]), ("Lead", ["Sink"])], extra=[], skill="Data"),
   twin=nm("s9u09n21_t", "M", "O3", "Use the chart. How many times denser is lead than water (to 1 decimal place)?", 11.3, "", tol=0, units=[""], fig=DEN)),
 "s9u09n31p": dict(note="Paused before eggs are lowered into tap water and very salty water.",
   q=mc("s9u09n31p_q", "M", "O4", "PREDICT: what will the eggs do?", ("Sink in tap water, float in salty water", "Good prediction – now watch."),
        [("Float in both", "Watch carefully."), ("Sink in both", "Watch carefully."), ("Float in tap water, sink in salty water", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u09n31p_t", "M", "O4", "An object floats in a liquid if it is…", "less dense than the liquid", [("heavier than the liquid", ""), ("denser than the liquid", ""), ("made of metal", "")])),
 "s9u09n31e": dict(note="Paused after the egg sank in tap water and floated in very salty water.",
   q=ex("s9u09n31e_q", "H", "O4", "EXPLAIN the result.",
        [("the egg is denser than tap water, so it sinks", ["denser than (tap )?water|more dense than (tap )?water"]), ("dissolving salt makes the water denser than the egg, so it floats", ["salt.{0,40}(denser|more dense|higher density)|less dense than (the )?salt"])],
        "The egg is denser than tap water, so it sinks. Dissolving lots of salt makes the water denser than the egg, so the egg is now less dense than the liquid and floats."),
   twin=mc("s9u09n31e_t", "H", "O4", "Ships float a little higher in sea water than in a freshwater river because…", "sea water is denser than fresh water", [("sea water is warmer", ""), ("rivers have no upthrust", ""), ("ships are lighter at sea", "")])),
}

DROP = {"9.1": ["s9u09s1p01", "s9u09s1p13", "s9u09s1p14"], "9.2": ["s9u09s2p04", "s9u09s2p05"], "9.3": ["s9u09s3p01", "s9u09s3p02", "s9u09s3p08"]}

CYL = {"kind": "barchart", "labels": ["water only", "water + stone"], "values": [40, 58], "ymax": 70, "step": 10, "ylabel": "Reading on measuring cylinder (cm³)"}
NEW_PRAC = {
 "9.1": [
  nm("s9u09s1p21", "M", "O1", "Use the chart. What is the volume of the stone?", 18, "cm³", tol=0, units=["cm³", "cm3"], fig=CYL, skill="Data"),
  nm("s9u09s1p22", "H", "O2", "The stone has a mass of 45 g. Use the chart to calculate its density.", 2.5, "g/cm³", tol=0, units=["g/cm³", "g/cm3"], fig=CYL, skill="Data"),
  nm("s9u09s1p23", "M", "O1", "A cuboid measures 5 cm × 4 cm × 2 cm. What is its volume?", 40, "cm³", tol=0, units=["cm³", "cm3"]),
 ],
 "9.2": [
  ex("s9u09s2p21", "H", "O3", "Use the particle model to explain why a gas is much less dense than the same substance as a solid.",
     [("gas particles are far apart / large spaces", ["far apart|spaces|spread out"]), ("so the same mass takes up a much larger volume", ["larger volume|more space|same mass|takes up"])],
     "In a gas the particles are far apart with large spaces between them, so the same mass of particles takes up a much larger volume. Density = mass ÷ volume, so the gas has a much lower density."),
  mc("s9u09s2p22", "H", "O3", "A hot-air balloon rises because…", "the hot air inside is less dense than the cooler air outside", [("hot air has no mass", "It still has mass."), ("the balloon is pulled by the Sun", "No."), ("hot air is denser", "It is less dense.")]),
 ],
 "9.3": [
  od("s9u09s3p21", "M", "O4", "Use the chart of densities. Order from the material that floats highest in water to the one that sinks fastest.", ["cork", "ice", "aluminium", "lead"], fig=DEN, skill="Data"),
  ex("s9u09s3p22", "H", "O4", "A steel ship floats although steel (7.9 g/cm³) is denser than water. Explain why.",
     [("the ship's hull contains a lot of air", ["air|hollow"]), ("so its overall (average) density is less than water's", ["overall|average|less than (1|water)|whole ship"])],
     "The ship's hull is hollow and contains a lot of air, so the overall (average) density of the whole ship, steel plus air, is less than the density of water, and it floats."),
 ],
}
NEW_ADV = {
 "9.3": [adv(ex("s9u09s3a05", "VH", "O4", "The US Coast Guard's International Ice Patrol says that about 7/8 of an iceberg's mass is below the waterline. Ice has a density of about 0.92 g/cm³ and sea water about 1.03 g/cm³. Show that these densities explain the 7/8 figure, and explain why icebergs are a hidden danger to ships.",
     [("0.92 ÷ 1.03 ≈ 0.89, close to 7/8 = 0.875", ["0\\.89|0\\.9|89 ?%|0\\.875|7/8"]), ("the fraction below water equals the ratio of the densities (ice slightly less dense than sea water)", ["ratio|fraction|less dense|density of ice"]), ("most of the ice is hidden underwater, so it is bigger than it looks / ships can hit the hidden part", ["hidden|underwater|below|cannot see|bigger than|hit"])],
     "The fraction of a floating object below the surface equals its density divided by the liquid's density: 0.92 ÷ 1.03 ≈ 0.89, close to 7/8 (0.875). Because ice is only slightly less dense than sea water, almost nine-tenths of an iceberg is hidden underwater, so it is far bigger than it looks and ships can strike the submerged part.", need=2, src=src("SRC-USCGIIP")))],
}

from tests_stage9_unit09_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
