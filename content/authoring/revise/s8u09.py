# -*- coding: utf-8 -*-
"""Stage 8 Unit 9 Pressure and Diffusion — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NOAAPRES", "name": "NOAA National Ocean Service – How does pressure change with ocean depth?", "url": "https://oceanservice.noaa.gov/facts/pressure.html", "use": "Deep-sea pressure Challenge question (9.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s8u09n11p": dict(note="Paused before two identical bricks are put on modelling clay, one flat and one on its end.",
   q=mc("s8u09n11p_q", "M", "O1", "PREDICT: which brick will sink deeper into the clay?", ("The brick standing on its end", "Good prediction – now watch."),
        [("The brick lying flat", "Watch carefully."), ("Both the same", "Watch carefully."), ("Neither will sink", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u09n11p_t", "M", "O1", "The unit of pressure is…", "N/m²", [("N", ""), ("m²", ""), ("N m", "")])),
 "s8u09n11e": dict(note="Paused after the brick on its end made a much deeper dent.",
   q=ex("s8u09n11e_q", "H", "O1", "EXPLAIN why the brick on its end sank deeper.",
        [("same force / weight but a smaller area", ["smaller area|small area|less area"]), ("so a larger pressure (pressure = force ÷ area)", ["larger pressure|bigger pressure|more pressure|higher pressure|force ?÷ ?area|force divided by area"])],
        "Both bricks push with the same force, but the brick on its end acts on a smaller area. Pressure = force ÷ area, so its pressure is larger and it pushes further into the clay."),
   twin=nm("s8u09n11e_t", "H", "O1", "A 40 N brick stands on an area of 0.02 m². What pressure does it exert?", 2000, "N/m²", tol=0, units=["N/m²", "N/m2", "Pa"])),
 "s8u09n21": dict(note="Paused on the graph: water pressure 0, 100, 200, 300, 400 kN/m² at 0, 10, 20, 30, 40 m.",
   q=nm("s8u09n21_q", "H", "O2", "Use the graph. What is the pressure from the water at 25 m depth?", 250, "kN/m²", tol=5, units=["kN/m²", "kN/m2"], skill="Data"),
   twin=mc("s8u09n21_t", "M", "O2", "If the diver goes from 15 m to 30 m deep, the pressure from the water…", "doubles", [("halves", ""), ("stays the same", ""), ("increases by 15 times", "")])),
 "s8u09n31": dict(note="Paused after four everyday examples of gas pressure: tyres, aerosol cans, straws and mountains.",
   q=ex("s8u09n31_q", "H", "O3", "Explain why an aerosol can must never be heated.",
        [("heating makes the gas particles move faster", ["faster|more energy|move quicker"]), ("they hit the walls more often/harder, so the pressure rises and the can could burst", ["pressure (rise|increase|goes up)|burst|explode|harder|more often"])],
        "Heating gives the gas particles more energy, so they move faster and hit the inside of the can more often and harder. The pressure rises and the can could burst."),
   twin=mc("s8u09n31_t", "M", "O3", "When you drink through a straw, the drink is pushed up by…", "air pressure on the drink outside the straw", [("the straw pulling it", ""), ("gravity", ""), ("water pressure inside your mouth", "")])),
 "s8u09n51p": dict(note="Paused before a drop of food colouring goes into cold water and hot water.",
   q=mc("s8u09n51p_q", "M", "O5", "PREDICT: in which beaker will the colour spread faster?", ("In the hot water", "Good prediction – now watch."),
        [("In the cold water", "Watch carefully."), ("The same in both", "Watch carefully."), ("It will not spread without stirring", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u09n51p_t", "M", "O5", "Diffusion is the spreading of particles from…", "a high concentration to a low concentration", [("a low concentration to a high concentration", ""), ("solids into solids only", ""), ("cold places to hot places only", "")])),
 "s8u09n51e": dict(note="Paused after the colour spread much faster in the hot water.",
   q=ex("s8u09n51e_q", "H", "O5", "EXPLAIN why the colour spread faster in the hot water.",
        [("particles have more energy / move faster when hot", ["faster|more energy|move more"]), ("so diffusion / spreading out is quicker", ["diffus|spread|mix"])],
        "In hot water the particles have more energy and move faster, so the colour particles spread out by diffusion more quickly."),
   twin=mc("s8u09n51e_t", "M", "O5", "Which change would make diffusion of a smell across a room slower?", "Cooling the room", [("Warming the room", ""), ("Using lighter particles", ""), ("Opening a window to let the air move", "")])),
}

DROP = {"9.1": ["s8u09s1p02", "s8u09s1p09", "s8u09s1p11"], "9.2": ["s8u09s2p03", "s8u09s2p06", "s8u09s2p14"],
        "9.3": ["s8u09s3p04", "s8u09s3p14", "s8u09s3p06"], "9.4": ["s8u09s4p02", "s8u09s4p08"], "9.5": ["s8u09s5p01", "s8u09s5p04", "s8u09s5p02"]}

SHOES = {"kind": "barchart", "labels": ["stiletto heel", "trainer", "snowshoe"], "values": [2000, 200, 10], "ymax": 2200, "step": 400, "ylabel": "Pressure on floor (kN/m²)"}
TYRE = {"kind": "linegraph", "x": {"min": 0, "max": 40, "step": 10, "label": "Temperature (°C)"}, "y": {"min": 200, "max": 260, "step": 10, "label": "Tyre pressure (kN/m²)"},
        "series": [{"pts": [[0, 220], [10, 228], [20, 236], [30, 244], [40, 252]], "label": "sealed tyre"}]}
SMELL = {"kind": "barchart", "labels": ["10 °C", "20 °C", "30 °C"], "values": [60, 40, 25], "ymax": 70, "step": 10, "ylabel": "Time to smell perfume 3 m away (s)"}
NEW_PRAC = {
 "9.1": [
  ex("s8u09s1p21", "H", "O1", "Use the chart. The same person wears each shoe. Explain why the pressure is so different.",
     [("same weight / force each time", ["same (weight|force)|weight is the same"]), ("different areas: stiletto smallest area so highest pressure; snowshoe largest area so lowest", ["area"])],
     "The person's weight (force) is the same, but the area in contact with the floor is different. The stiletto heel has the smallest area, so the highest pressure; the snowshoe has the largest area, so the lowest pressure.", fig=SHOES, skill="Data"),
  nm("s8u09s1p22", "H", "O1", "A 600 N student stands on one foot with an area of 0.015 m². What pressure does she exert?", 40000, "N/m²", tol=0, units=["N/m²", "N/m2", "Pa"]),
 ],
 "9.2": [
  mc("s8u09s2p21", "H", "O2", "A dam is built much thicker at the bottom than at the top. Why?", "Water pressure is greatest at the bottom", [("To save concrete", "It uses more."), ("Water is lighter at the bottom", "No."), ("Pressure is greatest at the surface", "It increases with depth.")]),
  nm("s8u09s2p22", "M", "O2", "Water pressure increases by about 10 kN/m² for every metre of depth. What is the extra pressure 7 m down?", 70, "kN/m²", tol=0, units=["kN/m²", "kN/m2"]),
 ],
 "9.3": [
  nm("s8u09s3p21", "M", "O3", "Use the graph. What is the tyre pressure at 20 °C?", 236, "kN/m²", tol=1, units=["kN/m²", "kN/m2"], fig=TYRE, skill="Data"),
  ex("s8u09s3p22", "H", "O3", "Use the graph. Describe the pattern and explain it using particles.",
     [("as temperature rises, pressure rises (about 8 kN/m² per 10 °C)", ["temperature.{0,30}(rise|increase|goes up)|higher temperature|8 ?kN"]), ("particles move faster and hit the tyre walls more often / harder", ["faster|more energy|harder|more often|collisions"])],
     "As the temperature rises, the pressure rises steadily, by about 8 kN/m² for every 10 °C. The air particles gain energy and move faster, so they hit the inside of the tyre more often and harder.", fig=TYRE, skill="Data"),
  nm("s8u09s3p23", "H", "O3", "Use the graph. Predict the tyre pressure at 50 °C if the pattern continues.", 260, "kN/m²", tol=2, units=["kN/m²", "kN/m2"], fig=TYRE, skill="Data"),
 ],
 "9.4": [
  gd("s8u09s4p21", "M", "O4", "Which state matches each description?", ["State"],
     [("Particles vibrate in fixed places", ["Solid"]), ("Particles close together but slide past each other", ["Liquid"]), ("Particles far apart and move quickly in all directions", ["Gas"])], extra=["Plasma"]),
  ex("s8u09s4p22", "H", "O4", "Use the particle model to explain why a gas can be squashed but a liquid cannot.",
     [("gas particles are far apart / big spaces", ["far apart|space|gap"]), ("liquid particles are already touching / close together", ["close|touch|no (space|gap)"])],
     "Gas particles are far apart with large spaces between them, so they can be pushed closer together. Liquid particles are already close together and touching, so there is no space to squash them into."),
 ],
 "9.5": [
  mc("s8u09s5p21", "M", "O5", "Use the chart. What is the pattern?", "The warmer the room, the faster the smell spreads", [("The warmer the room, the slower the smell spreads", "Times get shorter."), ("Temperature has no effect", "The times change."), ("The smell spreads fastest at 10 °C", "That is the slowest.")], fig=SMELL, skill="Data"),
  ex("s8u09s5p22", "H", "O5", "Use the chart. Suggest TWO variables to control in this experiment.",
     [("same perfume / same amount sprayed", ["same (perfume|amount|volume|spray)"]), ("same distance / same room / no draughts / same person", ["same distance|3 m|same room|draught|wind|window|same person"])],
     "Use the same perfume and the same amount each time, measure at the same distance (3 m) in the same room with no draughts.", fig=SMELL, need=2),
 ],
}
NEW_ADV = {
 "9.2": [adv(ex("s8u09s2a05", "VH", "O2", "NOAA states that ocean pressure increases by about one atmosphere (about 100 kN/m²) for every 10 m of depth. The deepest ocean is about 11 000 m deep. Estimate the pressure from the water there and explain why deep-sea submersibles have thick, rounded hulls.",
     [("about 1100 atmospheres / 110 000 kN/m² (11 000 ÷ 10 × 100)", ["1100|1 100|110 ?000|110000"]), ("pressure acts in all directions on the hull and is enormous", ["all directions|every direction|huge|enormous|very (high|large)"]), ("thick / rounded hull spreads the force and stops it being crushed", ["thick|strong|round|sphere|crush|spread"])],
     "11 000 m ÷ 10 m = 1100, so the water adds about 1100 atmospheres, roughly 110 000 kN/m². This enormous pressure pushes on the hull from every direction, so submersibles need thick, rounded (spherical) hulls that spread the force evenly and are not crushed.", need=2, src=src("SRC-NOAAPRES")))],
}

from tests_stage8_unit09_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
