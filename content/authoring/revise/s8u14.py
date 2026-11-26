# -*- coding: utf-8 -*-
"""Stage 8 Unit 14 Planetary Systems — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NASAPFS", "name": "NASA Goddard – Planetary Fact Sheet (metric)", "url": "https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html", "use": "Orbital periods for the video chart and the Challenge question (14.2)."},
    {"id": "SRC-NCEIPOLE", "name": "NOAA National Centers for Environmental Information – Wandering of the Geomagnetic Poles", "url": "https://www.ncei.noaa.gov/products/wandering-geomagnetic-poles", "use": "Corrected speed of the magnetic North Pole (14.3)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

ORB = {"kind": "barchart", "labels": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"], "values": [0.24, 0.62, 1.0, 1.88, 11.9, 29.5], "ymax": 32, "step": 4, "ylabel": "Time for one orbit (Earth years)"}

_wrong = "Not quite – look again at the key idea."
NEW_STOPS = {
 "s8u14n11p": dict(note="Paused before a balloon with six dots (galaxies) is blown up.",
   q=mc("s8u14n11p_q", "M", "O1", "PREDICT: what will happen to the distances between the dots?", ("They will all get bigger", "Good prediction – now watch."),
        [("They will all get smaller", "Watch carefully."), ("They will stay the same", "Watch carefully."), ("Only the dot in the middle will move", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u14n11p_t", "M", "O1", "The balloon model is used to show that the Universe is…", "expanding", [("shrinking", ""), ("flat", ""), ("not moving", "")])),
 "s8u14n11e": dict(note="Paused after every dot moved further from every other dot.",
   q=ex("s8u14n11e_q", "H", "O1", "EXPLAIN what the balloon model shows about galaxies.",
        [("space itself is stretching / expanding, like the rubber", ["stretch|expand"]), ("so galaxies are moving apart / away from each other", ["apart|away|further"])],
        "Space itself is stretching, like the rubber of the balloon, so distant galaxies are moving away from us and from each other: the Universe is expanding."),
   twin=mc("s8u14n11e_t", "H", "O1", "One limitation of the balloon model is that…", "real galaxies do not sit on a surface; space expands in three dimensions", [("balloons are red", ""), ("the dots are too big to see", ""), ("it shows galaxies getting closer", "")])),
 "s8u14n21": dict(note="Paused on the chart: Mercury 0.24, Venus 0.62, Earth 1, Mars 1.88, Jupiter 11.9, Saturn 29.5 Earth years.",
   q=ex("s8u14n21_q", "H", "O2", "What is the pattern between a planet's distance from the Sun and its orbit time?",
        [("the further from the Sun, the longer the orbit takes", ["further.{0,50}(longer|more time)|longer.{0,40}further"]), ("uses data, e.g. Mercury 0.24 years, Saturn 29.5 years", ["0\\.24|29\\.5|11\\.9|1\\.88"])],
        "The further a planet is from the Sun, the longer it takes to orbit: Mercury, the closest, takes 0.24 Earth years, while Saturn takes 29.5 Earth years.", skill="Data"),
   twin=nm("s8u14n21_t", "M", "O2", "Use the chart. How many times does Mercury orbit the Sun in one Earth year (to the nearest whole number)?", 4, "", tol=0.2, units=[""], fig=ORB)),
 "s8u14s3v02": dict(note="Paused after: “The magnetic North pole isn't at the geographic pole, and it wanders by tens of kilometres a year.”",
   q={"id": "s8u14s3v02q", "type": "mcq", "prompt": "Earth's magnetic field deflects…", "diff": "M", "obj": "O4", "skill": "Knowledge",
      "options": [{"t": "sunlight", "ok": False, "fb": _wrong}, {"t": "comets", "ok": False, "fb": _wrong}, {"t": "rain", "ok": False, "fb": _wrong}, {"t": "the solar wind", "ok": True, "fb": "Correct."}], "hint": "", "reason": ""}),
}

# Correction: the old text said the magnetic North Pole moves about 10 km a year; NOAA NCEI reports about 55 km a year (2007 survey).
REPLACE = {
 "s8u14s3r03": {"id": "s8u14s3r03", "type": "table", "prompt": "A 2007 survey found the magnetic North Pole moving about 55 km per year. Complete the table, assuming this speed.", "diff": "H", "obj": "O4", "skill": "Data",
                "head": ["Years", "Distance moved (km)"], "rows": [["1", "55"], ["4", {"ans": 220}]], "hint": "", "reason": ""},
 "s8u14s3p04": {"id": "s8u14s3p04", "type": "mcq", "prompt": "In recent decades, the magnetic North Pole has moved about…", "diff": "M", "obj": "O4", "skill": "Knowledge",
                "options": [{"t": "50 m a year", "ok": False, "fb": _wrong}, {"t": "tens of km a year", "ok": True, "fb": "Correct – about 55 km a year in a 2007 survey."}, {"t": "5000 km a year", "ok": False, "fb": _wrong}, {"t": "not at all", "ok": False, "fb": _wrong}], "hint": "", "reason": ""},
 "s8u14s3a02": {"id": "s8u14s3a02", "type": "mcq", "prompt": "* Advanced. Why must maps used for compass navigation be updated over time?", "diff": "VH", "obj": "O4", "skill": "Reasoning",
                "options": [{"t": "The magnetic North pole slowly moves.", "ok": True, "fb": "Correct."}, {"t": "The geographic North Pole moves tens of km a year.", "ok": False, "fb": "The geographic pole stays fixed; the magnetic pole moves."}, {"t": "Compasses wear out.", "ok": False, "fb": _wrong}, {"t": "Earth's core stops.", "ok": False, "fb": _wrong}], "hint": "", "reason": ""},
}

DROP = {"14.1": ["s8u14s1p02", "s8u14s1p07"], "14.2": ["s8u14s2p02", "s8u14s2p03", "s8u14s2p01"], "14.3": ["s8u14s3p02", "s8u14s3p14"]}

SIZE = {"kind": "barchart", "labels": ["Mercury", "Earth", "Jupiter", "Saturn", "Neptune"], "values": [4879, 12756, 142984, 120536, 49528], "ymax": 150000, "step": 25000, "ylabel": "Diameter (km)"}
NEW_PRAC = {
 "14.1": [
  nm("s8u14s1p21", "H", "O1", "Light from the Andromeda galaxy takes about 2.5 million years to reach us. How far away is it, in light years?", 2500000, "light years", tol=0, units=["light years"]),
  ex("s8u14s1p22", "H", "O1", "Explain why looking at a distant galaxy is like looking back in time.",
     [("light takes a long time / many years to travel from it", ["takes|years to (reach|travel)|travel"]), ("so we see it as it was when the light left it", ["as it was|in the past|when the light left|long ago"])],
     "Light from a distant galaxy takes millions of years to reach us, so we see the galaxy as it was when the light left it, long ago."),
 ],
 "14.2": [
  nm("s8u14s2p21", "M", "O2", "Use the chart. About how many times wider is Jupiter than Earth (to the nearest whole number)?", 11, "", tol=0.5, units=[""], fig=SIZE, skill="Data"),
  gd("s8u14s2p22", "H", "O3", "Use the chart. Rocky planet or gas planet?", ["Type"],
     [("Mercury", ["Rocky"]), ("Earth", ["Rocky"]), ("Jupiter", ["Gas"]), ("Neptune", ["Gas"])], extra=["Dwarf planet"], fig=SIZE),
  mc("s8u14s2p23", "H", "O2", "Planets shine with a steady light but stars twinkle because…", "planets reflect sunlight and are much closer, so they look like tiny discs, not points", [("planets are hotter than stars", "Stars are much hotter."), ("planets make their own light", "They are non-luminous."), ("stars are closer than planets", "Stars are much further away.")]),
 ],
 "14.3": [
  ex("s8u14s3p21", "H", "O4", "Explain why auroras are seen mostly near the North and South Poles.",
     [("Earth's magnetic field guides charged particles from the Sun / solar wind", ["field|magnetic|solar wind|charged particles"]), ("towards the poles, where they hit atoms in the atmosphere and give out light", ["pole|collide|hit|atoms|light"])],
     "Earth's magnetic field deflects the charged particles of the solar wind and guides some of them towards the poles. There they collide with atoms in the atmosphere, which give out light: the aurora."),
  nm("s8u14s3p22", "M", "O4", "A survey found the magnetic North Pole moving about 55 km per year. How far would it move in 3 years at this speed?", 165, "km", tol=0, units=["km"]),
 ],
}
NEW_ADV = {
 "14.2": [adv(ex("s8u14s2a05", "VH", "O2", "NASA's Planetary Fact Sheet gives Jupiter's orbit as about 11.9 Earth years and Saturn's as about 29.5 Earth years. A student is 12 years old. About how many times has Saturn orbited the Sun in her lifetime, and how many times has Jupiter? Explain why outer planets take so long to orbit.",
     [("Saturn: about 0.4 of an orbit (12 ÷ 29.5); Jupiter: about 1 orbit (12 ÷ 11.9)", ["0\\.4|less than (one|1|half)|about (1|one)|1\\.0|just over"]), ("outer planets travel a much longer path around the Sun", ["longer (path|orbit|distance|journey)|further|bigger orbit"]), ("and they move more slowly because the Sun's gravity is weaker far away", ["slower|weaker gravity|gravity.{0,20}weaker|less gravity"])],
     "Saturn has completed only about 0.4 of one orbit (12 ÷ 29.5), and Jupiter about one orbit (12 ÷ 11.9). Outer planets travel a much longer path around the Sun, and they also move more slowly because the Sun's gravity is weaker far away.", need=2, src=src("SRC-NASAPFS")))],
}

from tests_stage8_unit14_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
