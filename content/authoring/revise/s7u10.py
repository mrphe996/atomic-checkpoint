# -*- coding: utf-8 -*-
"""Stage 7 Unit 10 Forces — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NASAPFS", "name": "NASA Goddard – Planetary Fact Sheet (metric)", "url": "https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html", "use": "Surface gravity values used for the weight-on-other-worlds video chart and Challenge question (10.3)."},
    {"id": "SRC-NASAHF", "name": "NASA Goddard – The Apollo 15 Hammer-Feather Drop", "url": "https://nssdc.gsfc.nasa.gov/planetary/lunar/apollo_15_feather_drop.html", "use": "The hammer-and-feather demonstration used in the Challenge question (10.4)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "u10n11p": dict(note="Paused before the block is pulled across glass, wood and sandpaper.",
   q=mc("u10n11p_q", "M", "O1", "PREDICT: on which surface will the force meter reading be biggest?", ("Sandpaper", "Good prediction – now watch."),
        [("Glass", "Watch carefully."), ("Wood", "Watch carefully."), ("All the same", "The surfaces are different.")], skill="Prediction"),
   twin=mc("u10n11p_t", "M", "O1", "Force is measured in…", "newtons (N)", [("kilograms (kg)", ""), ("metres (m)", ""), ("joules (J)", "")])),
 "u10n11e": dict(note="Paused after the readings: glass 1.0 N, wood 2.5 N, sandpaper 6.0 N.",
   q=ex("u10n11e_q", "H", "O1", "EXPLAIN the results.",
        [("rougher surface → more friction", ["rough.{0,40}(friction|more|grip)|friction.{0,40}rough"]), ("friction opposes motion, so a bigger pull is needed", ["oppos|against|bigger (pull|force)|more force"])],
        "Friction acts against the motion. Rougher surfaces such as sandpaper grip the block more, so friction is bigger and a bigger pull is needed to keep the block moving."),
   twin=mc("u10n11e_t", "H", "O1", "Why do ice skates glide so easily?", "Ice is very smooth, so friction is small", [("Ice is very rough", ""), ("Skates have no weight", ""), ("Gravity is weaker on ice", "")])),
 "u10n12": dict(note="Paused after four examples: rain, the atmosphere, tides, satellites.",
   q=mc("u10n12_q", "H", "O2", "Why does the Moon pull on Earth's oceans much less strongly than the Earth pulls on you?", ("The Moon has a smaller mass and is much further away", "Yes – gravity depends on mass and distance."),
        [("The Moon has no gravity", "It does – it causes tides."), ("Water is not affected by gravity", "Rain falls because of gravity."), ("The Moon is made of rock", "Material does not matter; mass does.")]),
   twin=mc("u10n12_t", "M", "O2", "The size of the gravitational force depends on…", "mass and distance", [("colour and shape", ""), ("temperature only", ""), ("speed only", "")])),
 "u10n13": dict(note="Paused on the chart: a 10 kg mass weighs 16 N on the Moon, 37 N on Mars, 98 N on Earth, 231 N on Jupiter.",
   q=mc("u10n13_q", "M", "O3", "A 70 kg astronaut goes to Mars. What happens to her mass and her weight?", ("Mass stays 70 kg; weight gets smaller", "Yes – Mars has weaker gravity."),
        [("Both get smaller", "Mass does not change."), ("Mass gets smaller; weight stays the same", "It is the other way round."), ("Both stay the same", "Weight depends on gravity.")], skill="Data"),
   twin=nm("u10n13_t", "H", "O3", "Use the chart: a 10 kg mass weighs 37 N on Mars. What would a 20 kg mass weigh on Mars?", 74, "N", tol=0.5, units=["N"])),
 "u10n14p": dict(note="Paused before a flat sheet and a crumpled ball of the same paper are dropped.",
   q=mc("u10n14p_q", "M", "O4", "PREDICT: which lands first?", ("The crumpled ball", "Good prediction – now watch."),
        [("The flat sheet", "Watch carefully."), ("They land together", "Watch carefully."), ("Neither falls", "Gravity pulls both down.")], skill="Prediction"),
   twin=mc("u10n14p_t", "M", "O4", "Air resistance acts…", "against the motion of an object through air", [("in the same direction as the motion", ""), ("only on still objects", ""), ("only in space", "")])),
 "u10n14e": dict(note="Paused after the crumpled ball landed first.",
   q=ex("u10n14e_q", "H", "O4", "EXPLAIN why the crumpled ball landed first, even though both have the same mass.",
        [("same weight / gravity pulls them equally", ["same (weight|mass|pull)|equal"]), ("flat sheet has larger surface area", ["surface area|larger area|bigger area|spread|flat"]), ("so more air resistance on the flat sheet", ["air resistance|drag"])],
        "Gravity pulls both equally because they have the same mass. The flat sheet has a much bigger surface area, so it has more air resistance and falls more slowly.", need=2),
   twin=mc("u10n14e_t", "H", "O4", "Which parachute would fall most slowly?", "The one with the largest surface area", [("The smallest one", ""), ("The heaviest one", ""), ("A crumpled one", "")])),
}

DROP = {"10.1": ["u10s1p01", "u10s1p04", "u10s1p16"], "10.2": ["u10s2p02", "u10s2p03", "u10s2p18"], "10.3": ["u10s3p01", "u10s3p03", "u10s3p17"], "10.4": ["u10s4p01", "u10s4p04", "u10s4p02"]}

SPRING = {"kind": "linegraph", "x": {"min": 0, "max": 6, "step": 1, "label": "Force (N)"}, "y": {"min": 0, "max": 12, "step": 2, "label": "Extension (cm)"},
          "series": [{"pts": [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]], "label": "spring"}]}
WGT = {"kind": "barchart", "labels": ["Moon", "Mars", "Venus", "Earth", "Jupiter"], "values": [1.6, 3.7, 8.9, 9.8, 23.1], "ymax": 25, "step": 5, "ylabel": "Weight of 1 kg (N)", "xlabel": "World"}
CONE = {"kind": "linegraph", "x": {"min": 0, "max": 500, "step": 100, "label": "Area of parachute (cm²)"}, "y": {"min": 0, "max": 4, "step": 1, "label": "Time to fall 2 m (s)"},
        "series": [{"pts": [[0, 0.7], [100, 1.3], [200, 1.9], [300, 2.4], [400, 2.8], [500, 3.2]], "label": "toy parachute"}]}
NEW_PRAC = {
 "10.1": [
  nm("u10s1p21", "M", "O1", "A force meter's spring is tested. Use the graph. What is the extension when the force is 3 N?", 6, "cm", tol=0.2, units=["cm"], fig=SPRING, skill="Data"),
  nm("u10s1p22", "H", "O1", "Use the graph. A bag stretches the spring by 9 cm. What force is the bag exerting?", 4.5, "N", tol=0.1, units=["N"], fig=SPRING, skill="Data"),
  od("u10s1p23", "H", "O1", "A block is pulled across four surfaces with a force meter. Order the surfaces from least to most friction.", ["ice", "polished wood", "carpet", "sandpaper"]),
 ],
 "10.2": [
  mc("u10s2p21", "M", "O2", "Use the bar chart. On which world is gravity strongest?", "Jupiter", [("Earth", "Earth's bar is lower than Jupiter's."), ("Venus", "Venus is just below Earth."), ("Mars", "Mars is low.")], fig=WGT, skill="Data"),
  mc("u10s2p22", "H", "O2", "Use the bar chart. Venus and Earth have similar gravity. What does this suggest about them?", "They have similar masses and sizes", [("They are the same distance from the Sun", "Gravity at the surface depends on the planet's mass and size."), ("Venus has no gravity", "Its bar shows 8.9 N."), ("They are made of gas", "Both are rocky planets.")], fig=WGT, skill="Data"),
  ex("u10s2p23", "H", "O2", "Two spacecraft drift further apart in space. Describe what happens to the gravitational force between them and why.",
     [("the force gets weaker / smaller", ["weak|small|less|decreas"]), ("because the distance between them increases", ["distance|further|apart"])],
     "The gravitational force between them gets weaker, because gravity decreases as the distance between objects increases."),
 ],
 "10.3": [
  nm("u10s3p21", "M", "O3", "Use the bar chart. What does a 5 kg rock weigh on Mars?", 18.5, "N", tol=0.3, units=["N"], fig=WGT, skill="Data"),
  gd("u10s3p22", "H", "O3", "Mass or weight?", ["Quantity"],
     [("Measured in newtons", ["Weight"]), ("Stays the same on the Moon", ["Mass"]), ("Measured with a force meter", ["Weight"]), ("The amount of matter in an object", ["Mass"])], extra=[]),
  ex("u10s3p23", "H", "O3", "An astronaut says: 'I lost weight on the Moon, so I must have lost mass too.' Explain why she is wrong.",
     [("weight is the pull of gravity, which is weaker on the Moon", ["gravity|weaker|pull"]), ("mass is the amount of matter, which does not change", ["mass.{0,50}(same|not change|doesn't change|amount of matter)|amount of matter"])],
     "Her weight fell because the Moon's gravity is weaker. Her mass is the amount of matter in her body, which stays the same wherever she is."),
 ],
 "10.4": [
  nm("u10s4p21", "M", "O4", "Toy parachutes of different areas are dropped from 2 m. Use the graph. How long does a 300 cm² parachute take to fall?", 2.4, "s", tol=0.1, units=["s"], fig=CONE, skill="Data"),
  mc("u10s4p22", "H", "O4", "Use the graph. Which conclusion is correct?", "The bigger the area, the longer it takes to fall", [("Area has no effect", "The line rises."), ("Bigger parachutes fall faster", "They take longer, so they fall more slowly."), ("Time doubles every time the area doubles", "200 cm² gives 1.9 s, 400 cm² gives 2.8 s, not double.")], fig=CONE, skill="Data"),
  ms("u10s4p23", "H", "O4", "Select the TWO control variables in this parachute investigation.", ["the height it is dropped from", "the mass hanging from the parachute"], [("the area of the parachute", ""), ("the time to fall", "")]),
 ],
}
NEW_ADV = {
 "10.3": [adv(nm("u10s3a5", "VH", "O3", "NASA's Planetary Fact Sheet gives the gravity on Jupiter as 23.1 N for each kilogram. A probe weighs 245 N on Earth (9.8 N/kg). What would it weigh on Jupiter?", 577.5, "N", tol=3, units=["N"],
     hint="First find its mass: weight ÷ 9.8. Then multiply by 23.1.", src=src("SRC-NASAPFS")))],
 "10.4": [adv(ex("u10s4a5", "VH", "O4", "In 1971, Apollo 15 astronaut David Scott dropped a hammer and a feather at the same time on the Moon. They hit the ground together. Explain why, and say what would happen on Earth.",
     [("the Moon has no air, so no air resistance", ["no air|vacuum|no atmosphere|no air resistance"]), ("gravity makes all objects fall at the same rate", ["same rate|same speed|together|equally"]), ("on Earth, air resistance slows the feather, so the hammer lands first", ["earth.{0,80}(hammer|feather|air resistance)|feather.{0,40}slow"])],
     "The Moon has no atmosphere, so there is no air resistance and gravity makes both fall at the same rate. On Earth, the feather has a lot of air resistance for its weight, so it falls slowly and the hammer lands first.", need=2, src=src("SRC-NASAHF")))],
}

from tests_stage7_unit10_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
