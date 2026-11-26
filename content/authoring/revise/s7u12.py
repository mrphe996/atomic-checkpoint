# -*- coding: utf-8 -*-
"""Stage 7 Unit 12 Electricity — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NASAISSSA", "name": "NASA – Solar Arrays on the International Space Station", "url": "https://www.nasa.gov/image-article/solar-arrays-international-space-station/", "use": "Facts about the ISS solar arrays and batteries used in the Challenge question (12.4)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "u12n11p": dict(note="Paused before a coin, a plastic ruler, pencil graphite and a rubber eraser are tested in the circuit gap.",
   q=ms("u12n11p_q", "M", "O1", "PREDICT: which TWO materials will make the lamp light?", ["steel coin", "pencil graphite"], [("plastic ruler", "Watch carefully."), ("rubber eraser", "Watch carefully.")], skill="Prediction"),
   twin=mc("u12n11p_t", "M", "O1", "Electricity is a flow of…", "electrons", [("protons", ""), ("neutrons", ""), ("atoms", "")])),
 "u12n11e": dict(note="Paused after the results: coin lit, graphite dim, plastic and rubber off.",
   q=ex("u12n11e_q", "H", "O1", "EXPLAIN why the coin lit the lamp but the plastic ruler did not.",
        [("coin is a metal / conductor with free electrons", ["metal|conduct|free electron"]), ("plastic is an insulator, electrons not free to move", ["insulat|not free|can't move|cannot move"])],
        "The steel coin is a metal, a conductor with free electrons that can flow, so current passed and the lamp lit. Plastic is an insulator: its electrons are not free to move, so no current flowed."),
   twin=mc("u12n11e_t", "H", "O1", "Graphite is unusual because it is a non-metal that…", "conducts electricity", [("is magnetic", ""), ("is a gas", ""), ("rusts", "")])),
 "u12n12": dict(note="Paused after four switches: torch, doorbell, fridge light, traffic lights.",
   q=mc("u12n12_q", "M", "O2", "When the fridge door is shut, is the light's circuit open or closed?", ("Open – the light is off", "Yes – shutting the door opens the switch."),
        [("Closed – the light is on", "Then the light would be on all the time."), ("Both at once", "A circuit is either open or closed."), ("It has no circuit", "The light is part of a circuit.")]),
   twin=mc("u12n12_t", "M", "O2", "Pressing a doorbell button…", "closes the circuit", [("opens the circuit", ""), ("removes the cell", ""), ("breaks the wire", "")])),
 "u12n13": dict(note="Paused on the chart: all three ammeters read 0.30 A.",
   q=mc("u12n13_q", "H", "O3", "What do the three readings show?", ("The current is the same everywhere in a series circuit", "Yes – it is not used up."),
        [("The lamps use up some current", "A3 would be smaller if they did."), ("The current is biggest near the cell", "All the readings are equal."), ("The ammeters are broken", "Equal readings are expected.")], skill="Data"),
   twin=nm("u12n13_t", "M", "O3", "Another series circuit has 0.25 A at one ammeter. What does an ammeter at the other side of the lamp read?", 0.25, "A", tol=0, units=["A"])),
 "u12n14": dict(note="Paused on the chart: 1 lamp 0.40 A, 2 lamps 0.21 A, 3 lamps 0.14 A.",
   q=ex("u12n14_q", "H", "O4", "Why does adding lamps in series make the current smaller?",
        [("each lamp adds resistance", ["resist"]), ("more resistance → less current for the same cell / push", ["less current|smaller current|current (falls|decreases|drops)|same (cell|push)"])],
        "Each lamp adds resistance, making it harder for charge to flow. With the same cell (the same push), more resistance means a smaller current."),
   twin=mc("u12n14_t", "M", "O4", "How could you make the lamps brighter again?", "Add another cell in series", [("Add another lamp", ""), ("Use a longer wire only", ""), ("Open the switch", "")])),
}

DROP = {"12.1": ["u12s1p01", "u12s1p11", "u12s1p18"], "12.2": ["u12s2p01", "u12s2p06", "u12s2p16"], "12.3": ["u12s3p01", "u12s3p03", "u12s3p16"], "12.4": ["u12s4p01", "u12s4p02", "u12s4p04"]}

CELLS = {"kind": "linegraph", "x": {"min": 0, "max": 4, "step": 1, "label": "Number of cells"}, "y": {"min": 0, "max": 1.0, "step": 0.2, "label": "Current (A)"},
         "series": [{"pts": [[0, 0], [1, 0.22], [2, 0.44], [3, 0.66], [4, 0.88]], "label": "one lamp"}]}
WIRE = {"kind": "barchart", "labels": ["copper", "aluminium", "steel", "graphite", "plastic"], "values": [0.48, 0.46, 0.40, 0.12, 0], "ymax": 0.6, "step": 0.1, "ylabel": "Current (A)", "xlabel": "Material in the gap"}
NEW_PRAC = {
 "12.1": [
  mc("u12s1p21", "M", "O1", "Use the bar chart. Which material is the worst conductor that still lets current flow?", "Graphite", [("Plastic", "Plastic lets no current flow."), ("Steel", "Steel gives 0.40 A."), ("Copper", "Copper is the best conductor here.")], fig=WIRE, skill="Data"),
  mc("u12s1p22", "H", "O1", "Use the bar chart. Why is copper used for wires in houses?", "It gives the biggest current, so it is the best conductor", [("It gives zero current", "That is plastic."), ("It is the cheapest metal", "The chart does not show cost."), ("It is a non-metal", "Copper is a metal.")], fig=WIRE, skill="Data"),
  ex("u12s1p23", "H", "O1", "Explain why electricians wear rubber gloves and rubber-soled shoes.",
     [("rubber is an insulator", ["insulat"]), ("stops current flowing through the body to the ground / prevents shock", ["shock|body|ground|flow"])],
     "Rubber is an electrical insulator, so it stops current flowing through the electrician's body to the ground, which prevents an electric shock."),
 ],
 "12.2": [
  gd("u12s2p21", "M", "O2", "Will the lamp light?", ["Lights?"],
     [("Cell, lamp and closed switch in a complete loop", ["Yes"]), ("Cell, lamp and open switch", ["No"]), ("Cell and lamp, one wire disconnected", ["No"]), ("Cell, lamp and a steel paper clip in the gap", ["Yes"])], extra=[]),
  od("u12s2p22", "H", "O2", "Order the energy path in a torch.", ["chemical store of the cell", "electrical transfer through the wires", "lamp", "light and heat to the surroundings"]),
  mt("u12s2p23", "H", "O2", "Match each circuit symbol description to the component.", [("Long and short parallel lines", "cell"), ("Circle with a cross", "lamp"), ("Circle with an A", "ammeter"), ("A gap with a hinged line", "open switch")]),
 ],
 "12.3": [
  nm("u12s3p21", "M", "O3", "Use the graph. What current flows with 3 cells?", 0.66, "A", tol=0.02, units=["A"], fig=CELLS, skill="Data"),
  mc("u12s3p22", "H", "O3", "Use the graph. Which statement describes the pattern?", "Doubling the number of cells doubles the current", [("More cells give less current", "The line rises."), ("The current stays the same", "The line is not flat."), ("Current only changes after 3 cells", "It rises from the start.")], fig=CELLS, skill="Data"),
  gd("u12s3p23", "H", "O3", "Ammeter A1 before a lamp reads 0.35 A. What do the others read in this series circuit?", ["Reading (A)"],
     [("A2 between the two lamps", ["0.35"]), ("A3 after the second lamp", ["0.35"]), ("A4 next to the cell's negative terminal", ["0.35"])], extra=["0.70", "0.17"]),
 ],
 "12.4": [
  nm("u12s4p21", "M", "O4", "Use the graph. Predict the current with 5 cells.", 1.1, "A", tol=0.03, units=["A"], fig=CELLS, skill="Data"),
  mc("u12s4p22", "H", "O4", "A circuit with 2 cells and 1 lamp gives 0.44 A. A second lamp is added in series. What happens?", "The current falls and both lamps are dimmer", [("The current doubles", "More lamps add resistance."), ("Nothing changes", "Resistance has increased."), ("Only the new lamp lights", "In series, both carry the same current.")]),
  gd("u12s4p23", "H", "O4", "Does the current go up or down?", ["Change"],
     [("Add a cell in series", ["Up"]), ("Add a lamp in series", ["Down"]), ("Remove a lamp from a two-lamp series circuit", ["Up"]), ("Remove a cell from a three-cell battery", ["Down"])], extra=[]),
 ],
}
NEW_ADV = {
 "12.4": [adv(ex("u12s4a5", "VH", "O4", "NASA says the International Space Station's solar arrays can generate 84 to 120 kilowatts. When the station is in sunlight, much of this electricity charges the station's batteries. Explain why the station needs batteries as well as solar arrays.",
     [("the station passes into Earth's shadow / night side", ["shadow|dark|night|no sun|not in sun"]), ("solar arrays give no electricity without sunlight", ["no (electricity|power|current)|stop|can't|cannot"]), ("batteries store energy (chemical store) to keep circuits working", ["store|chemical|keep|power the station"])],
     "Every orbit the station passes into Earth's shadow, where the solar arrays receive no sunlight and make no electricity. Batteries store energy in their chemical store while in sunlight, so they can keep life support and other circuits running in the dark.", need=2, src=src("SRC-NASAISSSA")))],
}

from tests_stage7_unit12_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
