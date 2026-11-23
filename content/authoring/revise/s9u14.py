# -*- coding: utf-8 -*-
"""Stage 9 Unit 14 Astronomy — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NASAMOON", "name": "NASA NSSDCA – Moon Fact Sheet (Moon/Earth comparison)", "url": "https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html", "use": "Mean densities (Moon 3344 kg/m³, Earth 5514 kg/m³) and the Moon's recession rate (3.8 cm per year) for the video graph and Challenge (14.2)."},
    {"id": "SRC-CHICX", "name": "University of Texas Institute for Geophysics – Asteroid dust found in crater closes case of dinosaur extinction (2021)", "url": "https://ig.utexas.edu/news/2021/asteroid-dust-found-in-crater-closes-case-of-dinosaur-extinction/", "use": "Iridium-rich asteroid dust found in the Chicxulub drill core (reported 2021); corrects the earlier '2016' date (14.1)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}
_wrong = "Not quite – look again at the key idea."

DENS = {"kind": "barchart", "labels": ["Earth", "Moon"], "values": [5.51, 3.34], "ymax": 6, "step": 1, "ylabel": "Mean density (g/cm³)"}
CRATER = {"kind": "linegraph", "x": {"min": 0, "max": 100, "step": 20, "label": "Drop height (cm)"}, "y": {"min": 0, "max": 7, "step": 1, "label": "Crater diameter (cm)"},
          "series": [{"pts": [[20, 3.0], [40, 4.1], [60, 4.9], [80, 5.6]], "label": "one marble"}]}

NEW_STOPS = {
 "s9u14n11p": dict(note="Paused before a marble is dropped into flour from 20 cm and from 80 cm.",
   q=mc("s9u14n11p_q", "M", "O1", "PREDICT: which drop will make the bigger crater?", ("The drop from 80 cm", "Good prediction – now watch."),
        [("The drop from 20 cm", "Watch carefully."), ("Both craters will be the same size", "Watch carefully."), ("Neither will make a crater", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u14n11p_t", "M", "O1", "In this test, the variable that is changed on purpose is…", "the drop height", [("the size of the marble", ""), ("the type of flour", ""), ("the depth of the tray", "")])),
 "s9u14n11e": dict(note="Paused after the 80 cm drop made a wider crater with rays of flour.",
   q=ex("s9u14n11e_q", "H", "O1", "EXPLAIN why the higher drop made a bigger crater, and link this to the Chicxulub asteroid.",
        [("dropped from higher it hits faster, so it has more kinetic energy", ["faster|kinetic|more energy"]), ("a real asteroid hits very fast, so it makes a huge crater and throws dust into the air", ["asteroid|chicxulub|dust|huge|200"])],
        "Dropped from higher, the marble hits faster, so it has more kinetic energy and pushes more flour aside, making a wider crater. A real asteroid hits at many kilometres per second, so it made the huge Chicxulub crater and threw dust high into the atmosphere."),
   twin=mc("s9u14n11e_t", "M", "O1", "The rays of white flour over the cocoa are like…", "material thrown out around a real crater", [("lava from a volcano", ""), ("rivers on Mars", ""), ("cracks caused by earthquakes", "")])),
 "s9u14n21": dict(note="Paused on NASA's data: Earth 5.51 g/cm³, Moon 3.34 g/cm³.",
   q=ex("s9u14n21_q", "H", "O2", "What does the Moon's lower density suggest about its core, and how does this fit the collision theory?",
        [("the Moon has only a small iron core / is mostly rock", ["small.{0,20}core|mostly rock|less iron|little iron|rock"]), ("the Moon formed from rock blasted from Earth's outer layers (crust and mantle), not its iron core", ["outer|mantle|crust|debris|theia|collision|blasted"])],
        "The Moon's lower density suggests it has only a small iron core and is made mostly of rock. This fits the collision theory: the Moon formed from rock blasted out of the outer layers of Earth and Theia, while most of the dense iron stayed in Earth's core.", skill="Data"),
   twin=nm("s9u14n21_t", "M", "O2", "Use the chart. How much denser is Earth than the Moon, in g/cm³?", 2.17, "g/cm³", tol=0.01, units=["g/cm³"], fig=DENS)),
 "s9u14n31": dict(note="Paused after four real nebulae: Orion, the Pillars of Creation, the Crab Nebula and the cloud that formed our Sun.",
   q=mc("s9u14n31_q", "M", "O3", "What force makes a clump of gas in a nebula collapse to form a star?", ("Gravity", "Correct – gravity pulls the gas and dust together."),
        [("Magnetism", "Not this one."), ("Friction", "Not this one."), ("Air resistance", "There is no air in space.")]),
   twin=mc("s9u14n31_t", "M", "O3", "The Crab Nebula is…", "the remains of a star that exploded", [("a stellar nursery", ""), ("a planet", ""), ("a cloud of water vapour", "")])),
}

DROP = {"14.1": ["s9u14s1p06", "s9u14s1p07"], "14.2": ["s9u14s2p05", "s9u14s2p08"], "14.3": ["s9u14s3p01", "s9u14s3p07"]}

REPLACE = {
 "s9u14s1r07": {"id": "s9u14s1r07", "type": "mcq", "prompt": "In 2021, scientists reported evidence from rock drilled out of the Chicxulub crater. What did they find?", "diff": "H", "obj": "O1", "skill": "Knowledge",
                "options": [{"t": "A living dinosaur", "ok": False, "fb": _wrong}, {"t": "The asteroid itself, still whole", "ok": False, "fb": _wrong},
                            {"t": "Asteroid dust, rich in the metal iridium, inside the crater", "ok": True, "fb": "Correct – the iridium-rich dust matches the layer found all over the world."}, {"t": "Fossils of modern birds", "ok": False, "fb": _wrong}], "hint": "", "reason": ""},
}

NEW_PRAC = {
 "14.1": [
  nm("s9u14s1p21", "M", "O1", "A class drops a marble into flour from different heights. Use the graph: what is the crater diameter for a 60 cm drop?", 4.9, "cm", tol=0.1, units=["cm"], fig=CRATER, skill="Data"),
  ex("s9u14s1p22", "H", "O1", "Use the graph. Describe the pattern and explain it.",
     [("the higher the drop, the wider the crater", ["higher.{0,40}(wider|bigger|larger)|(wider|bigger|larger).{0,40}higher|increases"]), ("a higher drop means a faster impact with more kinetic energy", ["faster|kinetic|energy"])],
     "The higher the drop, the wider the crater. A marble dropped from higher is moving faster when it hits, so it has more kinetic energy to push the flour aside.", fig=CRATER, skill="Data"),
  mc("s9u14s1p23", "H", "O1", "Why is the marble-and-flour test only a model of an asteroid impact?", "A real asteroid is far bigger and faster, and its impact releases heat and dust into the air",
     [("Marbles are not round", "They are round – think about speed and size."), ("Flour is heavier than rock", "Not true."), ("Asteroids never hit Earth", "They do.")], skill="Evaluation"),
 ],
 "14.2": [
  nm("s9u14s2p21", "H", "O2", "Use the NASA chart. How many times denser is Earth than the Moon? Give your answer to one decimal place.", 1.6, "", tol=0.05, fig=DENS, skill="Data"),
  ex("s9u14s2p22", "H", "O2", "Iron has a density of about 7.9 g/cm³ and rock about 3 g/cm³. Use these values and the chart to explain why scientists think the Moon has only a small iron core.",
     [("the Moon's density (3.34) is close to that of rock", ["close to.{0,20}rock|rock|3\\.34|similar"]), ("so it cannot contain much dense iron; Earth (5.51) has a large iron core", ["iron|5\\.51|not much|little|small"])],
     "The Moon's density of 3.34 g/cm³ is close to the density of rock, so it cannot contain much iron, which is far denser. Earth's density of 5.51 g/cm³ is much higher because it has a large iron core.", fig=DENS, skill="Data"),
 ],
 "14.3": [
  gd("s9u14s3p21", "M", "O3", "Stellar nursery or the remains of an exploded star?", ["Type"],
     [("Orion Nebula", ["Stellar nursery"]), ("Crab Nebula", ["Remains of an exploded star"]), ("Pillars of Creation (Eagle Nebula)", ["Stellar nursery"])]),
  nm("s9u14s3p22", "M", "O3", "The star explosion that made the Crab Nebula was seen from Earth in the year 1054. How many years before 2024 was that?", 970, "years", tol=0, units=["years"]),
  ex("s9u14s3p23", "H", "O3", "Explain why a collapsing clump of gas in a nebula gets hotter until a star begins to shine.",
     [("gravity pulls the gas and dust inwards, so the clump becomes denser", ["gravity|pull|denser|squash"]), ("the particles move faster / the temperature rises, until reactions start in the core and it gives out light", ["hotter|faster|temperature|react|fusion|shine|light"])],
     "Gravity pulls the gas and dust inwards, squeezing the clump so it becomes denser. The particles move faster and the temperature rises until reactions start in the core, and the new star begins to shine."),
 ],
}

NEW_ADV = {
 "14.1": [adv(ex("s9u14s1a05", "VH", "O1", "Iridium is a metal that is very rare in Earth's crust but more common in some asteroids. A thin layer rich in iridium is found in rocks 66 million years old all over the world, and in 2021 scientists reported the same iridium-rich dust inside the Chicxulub crater. Explain how these two findings together support the idea that an asteroid impact caused the mass extinction.",
     [("iridium is rare on Earth, so the layer must come from an asteroid", ["rare|asteroid|space|extraterrestrial"]), ("the worldwide layer shows dust spread across the whole planet at that time", ["world|global|everywhere|spread"]), ("the same dust in the crater links that layer to this impact at the time of the extinction", ["crater|chicxulub|same|link|match"])],
     "Iridium is rare in Earth's crust, so a layer rich in it must have come from an asteroid. Finding the layer in 66-million-year-old rocks all over the world shows that asteroid dust spread across the whole planet at that time. Finding the same iridium-rich dust inside the Chicxulub crater links that worldwide layer to this particular impact, at exactly the time of the extinction.", need=2, src=src("SRC-CHICX")))],
 "14.2": [adv(nm("s9u14s2a05", "VH", "O2", "NASA's Moon Fact Sheet gives the Moon's recession rate as 3.8 cm per year: it is slowly moving away from Earth. How many kilometres further away will it be after 1 million years?", 38, "km", tol=0, units=["km"], src=src("SRC-NASAMOON")))],
}

from tests_stage9_unit14_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
