# -*- coding: utf-8 -*-
"""Stage 9 Unit 10 Transfer of Thermal Energy — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-DOELED", "name": "US Department of Energy (Energy Saver) – LED Lighting", "url": "https://www.energy.gov/energysaver/articles/led-lighting", "use": "Incandescent bulbs release about 90% of their energy as heat; LEDs use at least 75% less energy: Challenge question (10.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

TEA = {"kind": "linegraph", "x": {"min": 0, "max": 40, "step": 10, "label": "Time (min)"}, "y": {"min": 0, "max": 90, "step": 10, "label": "Temperature (°C)"},
       "series": [{"pts": [[0, 80], [5, 64], [10, 53], [15, 45], [20, 39], [30, 32], [40, 27]], "label": "tea"}]}

NEW_STOPS = {
 "s9u10n31": dict(note="Paused on the cooling curve: 80 °C falling to 27 °C over 40 minutes in a 22 °C room.",
   q=ex("s9u10n31_q", "H", "O3", "Why does the tea cool more slowly as time goes on, and what temperature will it finally reach?",
        [("the temperature difference between tea and room gets smaller, so heat flows more slowly", ["difference.{0,30}(smaller|less)|closer to room|less difference"]), ("it reaches room temperature, 22 °C, then stops cooling", ["22|room temperature"])],
        "As the tea cools, the difference between its temperature and the room's gets smaller, so heat flows out more slowly. It will finally reach room temperature, 22 °C, and then stop cooling.", skill="Data"),
   twin=nm("s9u10n31_t", "M", "O3", "Use the graph. By how much did the tea cool in the first 10 minutes?", 27, "°C", tol=0, units=["°C"], fig=TEA)),
 "s9u10n41p": dict(note="Paused before copper, steel and glass rods with waxed pins are heated at one end.",
   q=mc("s9u10n41p_q", "M", "O4", "PREDICT: on which rod will the pin fall off first?", ("Copper", "Good prediction – now watch."),
        [("Steel", "Watch carefully."), ("Glass", "Watch carefully."), ("All at the same time", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u10n41p_t", "M", "O4", "Heat travelling through a solid by vibrating particles is called…", "conduction", [("convection", ""), ("radiation", ""), ("evaporation", "")])),
 "s9u10n41e": dict(note="Paused after the copper pin fell at 40 s, the steel pin at 3 min and the glass pin stayed.",
   q=ex("s9u10n41e_q", "H", "O4", "EXPLAIN the order in which the pins fell.",
        [("heat travels by conduction: vibrations passed from particle to particle", ["conduct|vibrat"]), ("metals (copper best) have free electrons that carry energy quickly; glass is an insulator", ["free electrons|electrons|insulator|poor conductor"])],
        "Heat travels along each rod by conduction, as particles pass on their vibrations. Metals also have free electrons that carry energy quickly, so copper, the best conductor, lost its pin first, then steel. Glass has no free electrons; it is an insulator, so its pin did not fall."),
   twin=mc("s9u10n41e_t", "H", "O4", "Saucepans are made of metal with plastic handles because…", "metal conducts heat to the food, and plastic insulates your hand", [("plastic conducts heat well", ""), ("metal is an insulator", ""), ("plastic is shiny", "")])),
}

DROP = {"10.1": ["s9u10s1p02", "s9u10s1p09"], "10.2": ["s9u10s2p01", "s9u10s2p05"], "10.3": ["s9u10s3p01", "s9u10s3p03"], "10.4": ["s9u10s4p01", "s9u10s4p03"], "10.5": ["s9u10s5p01", "s9u10s5p02"]}

LAMP = {"kind": "barchart", "labels": ["incandescent: light", "incandescent: heat", "LED: light", "LED: heat"], "values": [10, 90, 75, 25], "ymax": 100, "step": 20, "ylabel": "Energy per 100 J supplied (J)"}
NEW_PRAC = {
 "10.1": [
  mc("s9u10s1p21", "H", "O1", "A swimming pool at 25 °C and a cup of tea at 80 °C. Which statement is correct?", "The pool has more thermal energy, but the tea has a higher temperature", [("The tea has more thermal energy", "The pool has far more particles."), ("They have the same thermal energy", "No."), ("The pool has a higher temperature", "25 °C is lower.")]),
  nm("s9u10s1p22", "M", "O1", "Hot water at 70 °C and cold water at 10 °C are mixed in equal amounts. Assuming no heat is lost, what is the final temperature?", 40, "°C", tol=0, units=["°C"]),
 ],
 "10.2": [
  nm("s9u10s2p21", "M", "O2", "Use the chart. What is the efficiency of the LED lamp?", 75, "%", tol=0, units=["%"], fig=LAMP, skill="Data"),
  ex("s9u10s2p22", "H", "O2", "Use the chart. Explain why switching to LED lamps saves money.",
     [("LED transfers more of the energy as light (75 % v 10 %)", ["75|more light|efficien"]), ("so less electrical energy is needed for the same light / less wasted as heat", ["less (energy|electricity|power)|wasted|heat|lower bill"])],
     "LED lamps transfer 75 % of the energy as light compared with only 10 % for incandescent lamps. So they need much less electrical energy for the same amount of light, wasting less as heat, and the electricity bill is lower.", fig=LAMP, skill="Data"),
 ],
 "10.3": [
  ex("s9u10s3p21", "H", "O3", "Explain why a heat sink on a computer chip has many thin metal fins.",
     [("fins give a large surface area", ["surface area"]), ("so heat dissipates into the air quickly, stopping the chip overheating", ["dissipat|transfer|air|overheat|cool"])],
     "The thin fins give the heat sink a large surface area, so heat dissipates from the metal into the surrounding air quickly and the chip does not overheat."),
  nm("s9u10s3p22", "M", "O3", "Use the cooling graph. What was the temperature of the tea after 20 minutes?", 39, "°C", tol=0, units=["°C"], fig=TEA, skill="Data"),
 ],
 "10.4": [
  gd("s9u10s4p21", "M", "O4", "Which way is heat mainly transferred?", ["Transfer"],
     [("Along a metal spoon in hot soup", ["Conduction"]), ("Warm air rising from a heater", ["Convection"]), ("From the Sun to Earth", ["Radiation"]), ("Through the water in a heated pan", ["Convection"])], extra=["Evaporation"]),
 ],
 "10.5": [
  ex("s9u10s5p21", "H", "O5", "Explain why a clay pot keeps drinking water cool on a hot, dry day.",
     [("water seeps through the clay and evaporates from the outside", ["evaporat"]), ("the fastest particles escape, taking energy, so the water left cools", ["fastest|energy|heat|cool"])],
     "Water seeps through the porous clay and evaporates from the outer surface. The fastest particles escape, taking energy with them, so the water left inside the pot cools down. Dry air makes evaporation faster."),
  mc("s9u10s5p22", "M", "O5", "On which day will washing dry fastest?", "Warm, dry and windy", [("Cold, humid and still", "Slowest."), ("Warm, humid and still", "Humid air slows it."), ("Cold, dry and still", "Wind and warmth help.")]),
 ],
}
NEW_ADV = {
 "10.2": [adv(ex("s9u10s2a05", "VH", "O2", "The US Department of Energy says incandescent bulbs release about 90 % of their energy as heat, and LEDs use at least 75 % less energy for the same light. A 60 W incandescent bulb is replaced by an LED giving the same light. Calculate the maximum power of the LED, and explain where the 'wasted' energy of the old bulb went.",
     [("75 % less than 60 W: at most 15 W (60 × 0.25)", ["15"]), ("the wasted energy is transferred as heat to the surroundings", ["heat|thermal|surroundings"]), ("energy is conserved: not destroyed, just not useful / dissipated", ["conserv|not destroyed|dissipat|spread"])],
     "75 % less than 60 W leaves 25 %: 60 × 0.25 = 15 W, so the LED uses at most 15 W. The old bulb's 'wasted' energy was not destroyed: about 90 % of it was transferred as heat to the surroundings, where it spread out and was no longer useful. Energy is conserved.", need=2, src=src("SRC-DOELED")))],
}

from tests_stage9_unit10_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
