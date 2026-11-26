# -*- coding: utf-8 -*-
"""Stage 8 Unit 8 Forces and Motion — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NASAMCO", "name": "NASA Science – Mars Climate Orbiter (mission page)", "url": "https://science.nasa.gov/mission/mars-climate-orbiter", "use": "Units-mix-up Challenge question (8.1)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s8u08n11": dict(note="Paused after four real-life examples of speed (walking, school zones, sports day, flights).",
   q=nm("s8u08n11_q", "H", "O1", "A pupil walks 840 m to school at 1.4 m/s. How long does the walk take, in seconds?", 600, "s", tol=0, units=["s"], skill="Application"),
   twin=nm("s8u08n11_t", "M", "O1", "A runner finishes 100 m in 12.5 s. What is the average speed?", 8, "m/s", tol=0, units=["m/s"])),
 "s8u08n21": dict(note="Paused on the cyclist's distance–time graph: 200 m in 40 s, stopped 40–60 s, then 120 m in 40 s.",
   q=gd("s8u08n21_q", "H", "O2", "Use the graph. Complete for each part of the journey.", ["Speed"],
        [("0–40 s", ["5 m/s"]), ("40–60 s", ["0 m/s"]), ("60–100 s", ["3 m/s"])], extra=["8 m/s", "2 m/s"], skill="Data"),
   twin=mc("s8u08n21_t", "M", "O2", "On the cyclist's graph, the flat part from 40 s to 60 s shows that she…", "was not moving", [("was at top speed", ""), ("was speeding up", ""), ("was riding home", "")])),
 "s8u08n31p": dict(note="Paused before a small and a large paper cone of equal mass are dropped.",
   q=mc("s8u08n31p_q", "M", "O3", "PREDICT: which cone will land first?", ("The small cone", "Good prediction – now watch."),
        [("The large cone", "Watch carefully."), ("They land together", "Watch carefully."), ("Neither, they float", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u08n31p_t", "M", "O3", "The force from the air that acts against a falling object is…", "air resistance", [("weight", ""), ("upthrust from water", ""), ("magnetism", "")])),
 "s8u08n31e": dict(note="Paused after the small cone landed first and the large cone fell slowly.",
   q=ex("s8u08n31e_q", "H", "O3", "EXPLAIN why the large cone fell more slowly.",
        [("it has a larger surface area, so more air resistance", ["surface area|wider|bigger.{0,20}(area|surface)|more air resistance"]), ("its weight is balanced by air resistance at a lower speed", ["balanc|lower speed|slower|terminal"])],
        "The large cone has a larger surface area, so more air resistance acts on it. The air resistance balances its weight at a lower speed, so it falls more slowly."),
   twin=mc("s8u08n31e_t", "M", "O3", "A parachute slows a skydiver because it…", "increases the air resistance", [("reduces her weight", ""), ("removes gravity", ""), ("makes her heavier", "")])),
 "s8u08n41p": dict(note="Paused before one coin is placed to balance two coins 10 cm from the pivot.",
   q=mc("s8u08n41p_q", "M", "O4", "PREDICT: where must ONE coin go to balance TWO coins 10 cm from the pivot?", ("20 cm from the pivot", "Good prediction – now watch."),
        [("10 cm from the pivot", "Watch carefully."), ("5 cm from the pivot", "Watch carefully."), ("It can never balance", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u08n41p_t", "M", "O4", "A moment depends on…", "the force and its distance from the pivot", [("the force only", ""), ("the distance only", ""), ("the colour of the object", "")])),
 "s8u08n41e": dict(note="Paused after one coin at 20 cm balanced two coins at 10 cm.",
   q=ex("s8u08n41e_q", "H", "O4", "EXPLAIN why the ruler balanced, using the word moment.",
        [("2 × 10 = 1 × 20 / the moments are equal", ["2 ?(×|x) ?10|1 ?(×|x) ?20|equal|same|20"]), ("clockwise moment = anticlockwise moment", ["clockwise|anticlockwise|moment"])],
        "The anticlockwise moment of two coins at 10 cm (2 × 10) equals the clockwise moment of one coin at 20 cm (1 × 20), so the moments are balanced and the ruler balances."),
   twin=nm("s8u08n41e_t", "H", "O4", "Three coins sit 10 cm left of the pivot. How far to the right must ONE coin go to balance them?", 30, "cm", tol=0, units=["cm"])),
}

DROP = {"8.1": ["s8u08s1p03", "s8u08s1p13", "s8u08s1p14"], "8.2": ["s8u08s2p03", "s8u08s2p07", "s8u08s2p11"],
        "8.3": ["s8u08s3p01", "s8u08s3p04", "s8u08s3p11"], "8.4": ["s8u08s4p02", "s8u08s4p09", "s8u08s4p12"]}

BUS = {"kind": "linegraph", "x": {"min": 0, "max": 60, "step": 10, "label": "Time (min)"}, "y": {"min": 0, "max": 30, "step": 5, "label": "Distance from depot (km)"},
       "series": [{"pts": [[0, 0], [20, 10], [30, 10], [50, 25], [60, 25]], "label": "bus"}]}
TWO = {"kind": "linegraph", "x": {"min": 0, "max": 20, "step": 5, "label": "Time (s)"}, "y": {"min": 0, "max": 100, "step": 20, "label": "Distance (m)"},
       "series": [{"pts": [[0, 0], [20, 100]], "label": "runner A"}, {"pts": [[0, 0], [20, 60]], "label": "runner B"}]}
SPEEDS = {"kind": "barchart", "labels": ["walking", "cycling", "car in town", "cheetah"], "values": [1.5, 5, 13, 30], "ymax": 35, "step": 5, "ylabel": "Typical speed (m/s)"}
NEW_PRAC = {
 "8.1": [
  nm("s8u08s1p21", "M", "O1", "Use the bar chart. How many times faster than walking is the car in town (to the nearest whole number)?", 9, "", tol=0.5, units=[""], fig=SPEEDS, skill="Data"),
  nm("s8u08s1p22", "H", "O1", "Use the bar chart. How far does the cyclist travel in 2 minutes?", 600, "m", tol=0, units=["m"], fig=SPEEDS, skill="Data"),
  mc("s8u08s1p23", "H", "O1", "A student times a toy car over 1 m with a stopwatch three times: 2.1 s, 2.4 s, 2.0 s. What is the best value to use?", "The mean, about 2.2 s", [("The fastest, 2.0 s", "Use all repeats."), ("The first, 2.1 s", "Use all repeats."), ("The slowest, 2.4 s", "Use all repeats.")], skill="Data"),
 ],
 "8.2": [
  nm("s8u08s2p21", "M", "O2", "Use the graph. What is the speed of the bus in the first 20 minutes, in km/h?", 30, "km/h", tol=0, units=["km/h"], fig=BUS, skill="Data"),
  gd("s8u08s2p22", "H", "O2", "Use the graph. Describe each part of the bus journey.", ["Motion"],
     [("0–20 min", ["Moving at a steady speed"]), ("20–30 min", ["Stopped"]), ("30–50 min", ["Moving at a steady speed"]), ("50–60 min", ["Stopped"])], extra=["Moving back to the depot"], fig=BUS),
  mc("s8u08s2p23", "H", "O2", "Use the graph. Which statement is correct?", "Runner A is faster: 5 m/s compared with 3 m/s", [("Runner B is faster because his line is lower", "Lower slope = slower."), ("They run at the same speed", "Their slopes differ."), ("Runner A is faster: 3 m/s compared with 5 m/s", "Check the numbers.")], fig=TWO, skill="Data"),
 ],
 "8.3": [
  gd("s8u08s3p21", "H", "O3", "Find the resultant force on each trolley.", ["Resultant"],
     [("8 N right, 8 N left", ["0 N"]), ("15 N right, 6 N left", ["9 N right"]), ("4 N right, 10 N left", ["6 N left"])], extra=["14 N left", "21 N right"]),
  ex("s8u08s3p22", "H", "O3", "A cyclist pedals with a constant force. Explain why her speed stops increasing after a while.",
     [("air resistance increases as she speeds up", ["air resistance|drag|friction"]), ("until it balances the forward force; resultant force is zero, so constant speed", ["balanc|equal|zero|constant|steady"])],
     "As she speeds up, the air resistance on her increases. When it is equal to her forward force, the forces are balanced, the resultant force is zero, and she moves at a steady speed."),
 ],
 "8.4": [
  nm("s8u08s4p21", "M", "O4", "A 3 N weight hangs 40 cm left of a pivot. What weight 30 cm to the right balances it?", 4, "N", tol=0, units=["N"]),
  ex("s8u08s4p22", "H", "O4", "Explain why it is easier to cut card near the pivot of a pair of scissors than at the tips.",
     [("the card is closer to the pivot", ["close|near|short"]), ("the same hand moment gives a larger force on the card (moment = force × distance)", ["larger|bigger|more force|moment|force ?(×|x) ?distance"])],
     "Moment = force × distance. Near the pivot the distance to the card is small, so the moment from your hand produces a larger force on the card, which makes it easier to cut."),
 ],
}
NEW_ADV = {
 "8.1": [adv(ex("s8u08s1a05", "VH", "O1", "In 1999 NASA lost the Mars Climate Orbiter because ground software worked in one system of units and the spacecraft's software in another. Explain why stating and checking units matters in any speed or force calculation.",
     [("a number means nothing without its unit / different units give different values", ["unit|meaning|mean"]), ("mixing units gives a wrong answer (e.g. pound-force vs newtons, km/h vs m/s)", ["mix|wrong|different|convert|newton|pound|m/s|km/h"]), ("checking/converting to one system (SI) avoids errors", ["check|convert|same|SI|metric"])],
     "A value is meaningless without its unit: 100 could be 100 m/s or 100 km/h. When one team used English units and the other metric units, the numbers were used as if they were in the same units, so the calculation was wrong. Converting everything into one system (SI) and checking units avoids such errors.", need=2, src=src("SRC-NASAMCO")))],
}

from tests_stage8_unit08_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
