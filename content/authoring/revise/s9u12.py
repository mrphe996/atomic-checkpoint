# -*- coding: utf-8 -*-
"""Stage 9 Unit 12 Electrical Circuits — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-BRITOHM", "name": "Encyclopaedia Britannica – Ohm's law", "url": "https://www.britannica.com/science/Ohms-law", "use": "For materials obeying Ohm's law V/I stays constant: Challenge question (12.5)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

IV = {"kind": "linegraph", "x": {"min": 0, "max": 6, "step": 1, "label": "Voltage (V)"}, "y": {"min": 0, "max": 0.5, "step": 0.1, "label": "Current (A)"},
      "series": [{"pts": [[0, 0], [1.5, 0.1], [3.0, 0.2], [4.5, 0.3], [6.0, 0.4]], "label": "resistor"}]}

NEW_STOPS = {
 "s9u12n31p": dict(note="Paused before one lamp is unscrewed in a series circuit and in a parallel circuit.",
   q=mc("s9u12n31p_q", "M", "O3", "PREDICT: what happens to the other lamp in each circuit?", ("Series: goes out. Parallel: stays lit.", "Good prediction – now watch."),
        [("Both go out", "Watch carefully."), ("Both stay lit", "Watch carefully."), ("Series: stays lit. Parallel: goes out.", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u12n31p_t", "M", "O2", "A series circuit has…", "only one path for the current", [("two or more branches", ""), ("no cell", ""), ("no switch", "")])),
 "s9u12n31e": dict(note="Paused after the series lamp went out and the parallel lamp stayed lit.",
   q=ex("s9u12n31e_q", "H", "O3", "EXPLAIN the result.",
        [("series: one path, so the gap stops the current everywhere", ["one path|single (path|loop)|gap|break|stops"]), ("parallel: the other branch is still a complete circuit with full voltage", ["branch|complete circuit|own path|separate|full voltage"])],
        "In the series circuit there is only one path, so removing a lamp makes a gap and the current stops everywhere. In the parallel circuit each lamp is on its own branch, which is still a complete circuit with the full voltage, so the other lamp stays lit."),
   twin=mc("s9u12n31e_t", "H", "O3", "Why are the lights in a house wired in parallel?", "Each can be switched on and off on its own, and one failing does not affect the others", [("It uses less wire", ""), ("It makes all lamps dimmer", ""), ("Series circuits cannot have switches", "")])),
 "s9u12n51": dict(note="Paused on the graph: 0.1 A at 1.5 V, 0.2 A at 3 V, 0.3 A at 4.5 V, 0.4 A at 6 V.",
   q=nm("s9u12n51_q", "H", "O5", "Use the graph. What is the resistance of the resistor?", 15, "Ω", tol=0, units=["Ω", "ohms", "ohm"], fig=IV, skill="Data"),
   twin=mc("s9u12n51_t", "M", "O5", "The straight line through the origin shows that the resistance…", "stays the same", [("increases with voltage", ""), ("decreases with voltage", ""), ("is zero", "")])),
}

DROP = {"12.1": ["s9u12s1p01", "s9u12s1p02"], "12.2": ["s9u12s2p04", "s9u12s2p05", "s9u12s2p07"], "12.3": ["s9u12s3p03", "s9u12s3p04"],
        "12.4": ["s9u12s4p03", "s9u12s4p06"], "12.5": ["s9u12s5p05", "s9u12s5p06", "s9u12s5p01"]}

AMM = {"kind": "barchart", "labels": ["A1 (main)", "A2 (branch 1)", "A3 (branch 2)"], "values": [0.9, 0.5, 0.4], "ymax": 1.0, "step": 0.2, "ylabel": "Current (A)"}
NEW_PRAC = {
 "12.1": [
  gd("s9u12s1p21", "M", "O1", "Which meter and unit?", ["Meter and unit"],
     [("Current", ["Ammeter, amps (A)"]), ("Voltage", ["Voltmeter, volts (V)"])], extra=["Ammeter, volts (V)", "Thermometer, °C"]),
  mc("s9u12s1p22", "H", "O1", "In the water-pipe model of a circuit, the current is like…", "the rate at which water flows", [("the pump", "That is the cell (voltage)."), ("a narrow section of pipe", "That is resistance."), ("the colour of the water", "No.")]),
 ],
 "12.2": [
  nm("s9u12s2p21", "M", "O2", "Three identical lamps are in series with a 6 V battery. What is the voltage across each lamp?", 2, "V", tol=0, units=["V"]),
  ex("s9u12s2p22", "H", "O2", "Explain why adding a third lamp in series makes all the lamps dimmer.",
     [("the voltage is shared between more lamps", ["shared|split|divided"]), ("more resistance, so the current falls", ["resistance|current (falls|decreases|is less|is smaller)|less current"])],
     "With more lamps in series, the battery's voltage is shared between more lamps and the total resistance is greater, so the current through every lamp falls and they are all dimmer."),
 ],
 "12.3": [
  nm("s9u12s3p21", "M", "O3", "Use the chart. Check: what is A2 + A3?", 0.9, "A", tol=0, units=["A"], fig=AMM, skill="Data"),
  mc("s9u12s3p22", "H", "O3", "Use the chart. Why does A1 read 0.9 A?", "The main current splits between the branches, so it equals their sum", [("Current is used up in the lamps", "Current is not used up."), ("A1 is faulty", "The readings agree."), ("Parallel circuits double the current", "It is the sum of the branches.")], fig=AMM, skill="Data"),
 ],
 "12.4": [
  mc("s9u12s4p22", "H", "O4", "A torch needs 6 V but you only have 1.5 V cells. How many cells are needed, and how are they connected?", "Four cells in series", [("Four cells in parallel", "Parallel keeps 1.5 V."), ("Two cells in series", "That gives 3 V."), ("Six cells in parallel", "That still gives 1.5 V.")]),
  gd("s9u12s4p21", "H", "O4", "Three 1.5 V cells. What is the total voltage?", ["Voltage"],
     [("All in series", ["4.5 V"]), ("All in parallel", ["1.5 V"]), ("Two in series, one reversed", ["1.5 V"])], extra=["3 V", "0 V"]),
 ],
 "12.5": [
  nm("s9u12s5p21", "M", "O5", "Use the graph. What current flows at 4.5 V?", 0.3, "A", tol=0, units=["A"], fig=IV, skill="Data"),
  nm("s9u12s5p22", "H", "O5", "Use the resistance you found from the graph (15 Ω). What current would flow at 9 V?", 0.6, "A", tol=0, units=["A"]),
 ],
}
NEW_ADV = {
 "12.5": [adv(ex("s9u12s5a05", "VH", "O5", "Britannica explains that for materials obeying Ohm's law, V ÷ I stays constant. A student measures a filament lamp: 0.20 A at 2 V, 0.30 A at 4 V and 0.35 A at 6 V. Calculate the resistance at 2 V and at 6 V, and explain whether the lamp obeys Ohm's law.",
     [("2 V: 10 Ω; 6 V: about 17 Ω (6 ÷ 0.35 = 17.1)", ["10 ?(Ω|ohm)|17"]), ("resistance increases as voltage increases, so V/I is not constant", ["increas|not constant|changes|rises"]), ("so it does not obey Ohm's law (the filament gets hotter)", ["does not obey|doesn't obey|not ohmic|non-ohmic|hotter|temperature"])],
     "At 2 V: R = 2 ÷ 0.20 = 10 Ω. At 6 V: R = 6 ÷ 0.35 ≈ 17 Ω. The resistance increases as the voltage increases, so V ÷ I is not constant and the lamp does not obey Ohm's law: its filament gets hotter at higher currents, which increases its resistance.", need=2, src=src("SRC-BRITOHM")))],
}

from tests_stage9_unit12_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
