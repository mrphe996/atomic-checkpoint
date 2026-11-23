# -*- coding: utf-8 -*-
"""Stage 7 Unit 14 Earth and Beyond — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NASAPFS", "name": "NASA Goddard – Planetary Fact Sheet (metric)", "url": "https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html", "use": "Orbital periods used for the video chart and Challenge question (14.1)."},
    {"id": "SRC-NOAASPR", "name": "NOAA National Ocean Service – What are spring and neap tides?", "url": "https://oceanservice.noaa.gov/facts/springtide.html", "use": "Spring tides at new and full moon; neap tides about seven days later (Challenge question, 14.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "u14n11": dict(note="Paused on the chart: Mercury 88, Venus 225, Earth 365, Mars 687, Jupiter 4331 Earth days.",
   q=mc("u14n11_q", "M", "O1", "What is the pattern between distance from the Sun and the length of a planet's year?", ("The further from the Sun, the longer the year", "Yes – the bars get taller."),
        [("The closer to the Sun, the longer the year", "Mercury has the shortest year."), ("All planets have the same year", "The bars are very different."), ("There is no pattern", "The bars increase in order.")], skill="Data"),
   twin=nm("u14n11_t", "H", "O1", "Use the chart: about how many Earth years is one Mars year? (Mars 687 days, Earth 365 days; 1 decimal place)", 1.9, "years", tol=0.05, units=["years", "Earth years", ""])),
 "u14n12": dict(note="Paused on the tide graph: high tide 5.0 m, low tide 1.2 m.",
   q=nm("u14n12_q", "H", "O2", "Use the graph. What is the tidal range (high tide 5.0 m, low tide 1.2 m)?", 3.8, "m", tol=0.05, units=["m"], skill="Data"),
   twin=mc("u14n12_t", "M", "O2", "How many high tides are there in about one day?", "Two", [("One", ""), ("Four", ""), ("None", "")])),
 "u14n13p": dict(note="Paused before the Moon ball moves between the torch and the Earth ball.",
   q=mc("u14n13p_q", "M", "O3", "PREDICT: what will you see on the Earth ball?", ("A small dark shadow on part of it", "Good prediction – now watch."),
        [("The whole Earth goes dark", "Watch carefully – how big is the Moon?"), ("Nothing changes", "Watch carefully."), ("The Earth gets brighter", "Watch carefully.")], skill="Prediction"),
   twin=mc("u14n13p_t", "M", "O3", "Light travels in…", "straight lines", [("circles", ""), ("zigzags only", ""), ("curves around objects", "")])),
 "u14n13e": dict(note="Paused after a small dark shadow fell on part of the Earth ball.",
   q=ex("u14n13e_q", "H", "O3", "EXPLAIN why a total solar eclipse can only be seen from a small part of Earth.",
        [("the Moon blocks the Sun's light / light travels in straight lines", ["block|straight"]), ("the Moon is small, so its darkest shadow (umbra) covers only a small area", ["small|umbra|darkest|area|part"])],
        "Light travels in straight lines, so the Moon blocks the Sun's light. The Moon is much smaller than Earth, so its darkest shadow, the umbra, covers only a small area; only people there see a total eclipse."),
   twin=mc("u14n13e_t", "M", "O3", "In a solar eclipse, the order is…", "Sun – Moon – Earth", [("Sun – Earth – Moon", ""), ("Moon – Sun – Earth", ""), ("Earth – Sun – Moon", "")])),
 "u14n14": dict(note="Paused after four tools: space telescopes, probes, radio telescopes, satellites.",
   q=ex("u14n14_q", "H", "O4", "Why did Galileo's view of moons orbiting Jupiter not fit the old Earth-centred model?",
        [("the moons orbited Jupiter, not Earth", ["jupiter|not (round|around) earth|orbit jupiter"]), ("so not everything orbits the Earth", ["not everything|everything|centre|center"])],
        "The Earth-centred model said everything orbits the Earth, but Galileo saw moons orbiting Jupiter, which showed that not everything orbits the Earth."),
   twin=mc("u14n14_t", "M", "O4", "How does science respond to new evidence?", "Models are changed or replaced to fit the evidence", [("Evidence is ignored", ""), ("Models never change", ""), ("Only old ideas are trusted", "")])),
}

DROP = {"14.1": ["u14s1p02", "u14s1p06", "u14s1p11"], "14.2": ["u14s2p01", "u14s2p12", "u14s2p18"], "14.3": ["u14s3p02", "u14s3p11", "u14s3p18"], "14.4": ["u14s4p02", "u14s4p05", "u14s4p08"]}

DAYS = {"kind": "barchart", "labels": ["Mercury", "Venus", "Earth", "Mars"], "values": [1408, 5832, 24, 25], "ymax": 6000, "step": 1000, "ylabel": "Length of one day (hours)", "xlabel": "Planet"}
TIDES = {"kind": "linegraph", "x": {"min": 0, "max": 28, "step": 7, "label": "Day of the lunar month"}, "y": {"min": 0, "max": 6, "step": 1, "label": "Tidal range (m)"},
         "series": [{"pts": [[0, 5.2], [3.5, 4.0], [7, 2.6], [10.5, 3.9], [14, 5.1], [17.5, 4.0], [21, 2.7], [24.5, 3.9], [28, 5.2]], "label": "harbour"}]}
NEW_PRAC = {
 "14.1": [
  mc("u14s1p21", "M", "O1", "Use the bar chart. Which planet has the longest day?", "Venus", [("Mercury", "Mercury's day is long, but Venus's is longer."), ("Earth", "Earth's day is 24 hours."), ("Mars", "Mars's day is about 25 hours.")], fig=DAYS, skill="Data"),
  mc("u14s1p22", "H", "O1", "Use the bar chart. Which planet has a day most like Earth's?", "Mars", [("Venus", "Venus's day is thousands of hours."), ("Mercury", "Mercury's day is over 1400 hours."), ("None of them", "Mars is very close.")], fig=DAYS, skill="Data"),
  gd("u14s1p23", "H", "O1", "Inner rocky planet or outer gas giant?", ["Type"],
     [("Mars", ["Rocky"]), ("Saturn", ["Gas giant"]), ("Venus", ["Rocky"]), ("Neptune", ["Gas giant"])], extra=[]),
 ],
 "14.2": [
  mc("u14s2p21", "M", "O2", "Use the graph. On which days are spring tides (the largest tidal range)?", "Days 0, 14 and 28", [("Days 7 and 21", "Those have the smallest range."), ("Days 3.5 and 10.5", "These are in between."), ("Every day", "The range changes.")], fig=TIDES, skill="Data"),
  nm("u14s2p22", "H", "O2", "Use the graph. How many days are there between a spring tide and the next neap tide?", 7, "days", tol=0, units=["days", ""], fig=TIDES, skill="Data"),
  mc("u14s2p23", "H", "O2", "Use the graph. Where are the Sun and Moon on day 7?", "At right angles to each other, so their pulls partly cancel", [("In a straight line", "That gives spring tides."), ("Both behind the Earth", "Day 7 is a neap tide."), ("The Moon has disappeared", "The Moon is always there.")], fig=TIDES, skill="Data"),
 ],
 "14.3": [
  gd("u14s3p21", "M", "O3", "Solar or lunar eclipse?", ["Eclipse"],
     [("The Moon passes between the Sun and Earth", ["Solar"]), ("The Moon passes through Earth's shadow", ["Lunar"]), ("The Moon looks red", ["Lunar"]), ("Day briefly turns dark", ["Solar"])], extra=[]),
  od("u14s3p22", "H", "O3", "Put the bodies in order for a lunar eclipse, from the light source.", ["Sun", "Earth", "Moon"]),
  ex("u14s3p23", "H", "O3", "During a lunar eclipse the Moon often looks red. Explain why.",
     [("Earth's atmosphere bends some sunlight onto the Moon", ["atmosphere|bend|refract"]), ("blue light is removed / scattered, so mostly red light reaches it", ["blue|red|scatter|removes"])],
     "Earth's atmosphere bends some sunlight into the shadow and onto the Moon, and removes most of the blue light, so mostly red light reaches the Moon."),
 ],
 "14.4": [
  od("u14s4p21", "M", "O4", "Order these ideas by date, earliest first.", ["Ptolemy's Earth-centred model", "Copernicus's Sun-centred model", "Galileo sees moons of Jupiter", "Neptune predicted and found"]),
  mc("u14s4p22", "H", "O4", "Neptune was predicted using Newton's laws before anyone saw it. What does this show about a good scientific model?", "It can make predictions that are then tested", [("It never needs evidence", "Predictions must be checked."), ("It is always right first time", "Models are improved over time."), ("It cannot be changed", "Models change with evidence.")]),
  gd("u14s4p23", "H", "O4", "Which model does each idea belong to?", ["Model"],
     [("The Sun orbits the Earth", ["Geocentric"]), ("The Earth orbits the Sun", ["Heliocentric"]), ("Earth is at the centre of everything", ["Geocentric"]), ("Earth's spin makes the Sun appear to move", ["Heliocentric"])], extra=[]),
 ],
}
NEW_ADV = {
 "14.1": [adv(nm("u14s1a5", "VH", "O1", "NASA's Planetary Fact Sheet gives Jupiter's orbital period as 4331 Earth days. How many Earth years is that? Give your answer to 1 decimal place (1 year = 365.25 days).", 11.9, "years", tol=0.05, units=["years", "Earth years", ""], src=src("SRC-NASAPFS")))],
 "14.2": [adv(ex("u14s2a5", "VH", "O2", "NOAA says spring tides happen at new moon and full moon, and neap tides about seven days later. Explain why the tidal range is biggest at new and full moon.",
     [("the Sun, Earth and Moon are in a line", ["line|align"]), ("the Sun's pull adds to the Moon's pull", ["add|together|combine|same direction"]), ("so high tides are higher and low tides lower", ["higher|bigger|larger|lower"])],
     "At new and full moon the Sun, Earth and Moon are in a straight line, so the Sun's gravitational pull adds to the Moon's. The ocean bulges more, so high tides are higher and low tides lower.", need=2, src=src("SRC-NOAASPR")))],
}

from tests_stage7_unit14_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
