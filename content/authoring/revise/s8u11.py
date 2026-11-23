# -*- coding: utf-8 -*-
"""Stage 8 Unit 11 Magnetism — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NCEIPOLE", "name": "NOAA National Centers for Environmental Information – Wandering of the Geomagnetic Poles", "url": "https://www.ncei.noaa.gov/products/wandering-geomagnetic-poles", "use": "Moving magnetic north pole Challenge question (11.1)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s8u11n11p": dict(note="Paused before a magnet is lowered over a nail, a paper clip, a copper coin, an aluminium can and a plastic spoon.",
   q=ms("s8u11n11p_q", "M", "O1", "PREDICT: select ALL the objects the magnet will pick up.", ["Iron nail", "Steel paper clip"], [("Copper coin", "Watch carefully."), ("Aluminium can", "Watch carefully."), ("Plastic spoon", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u11n11p_t", "M", "O1", "Which is a magnetic material?", "Nickel", [("Copper", ""), ("Gold", ""), ("Glass", "")])),
 "s8u11n11e": dict(note="Paused after only the nail and paper clip were attracted.",
   q=ex("s8u11n11e_q", "H", "O1", "EXPLAIN the result. Why is 'all metals are magnetic' wrong?",
        [("only iron, steel, nickel and cobalt are magnetic", ["iron|steel|nickel|cobalt"]), ("copper and aluminium are metals but are not magnetic", ["copper|aluminium"])],
        "Only magnetic materials such as iron, steel, nickel and cobalt are attracted. Copper and aluminium are metals but they are not magnetic, so not all metals are magnetic."),
   twin=mc("s8u11n11e_t", "M", "O1", "How could a recycling centre separate steel cans from aluminium cans?", "Use a magnet: only the steel cans are attracted", [("Use water: steel floats", ""), ("Use a sieve", ""), ("Use heat", "")])),
 "s8u11n21": dict(note="Paused on the graph: 3, 6, 9, 11, 14 paper clips for 10, 20, 30, 40, 50 turns.",
   q=gd("s8u11n21_q", "H", "O2", "Identify the variables in the investigation.", ["Variable"],
        [("Number of turns", ["Independent"]), ("Paper clips picked up", ["Dependent"]), ("The cell used", ["Control"])], extra=[], skill="Data"),
   twin=nm("s8u11n21_t", "H", "O2", "Use the pattern. About how many paper clips would 60 turns pick up?", 17, "clips", tol=1, units=["clips", ""])),
 "s8u11n31": dict(note="Paused after four everyday electromagnets: doorbell, door lock, speaker and recycling centre.",
   q=mc("s8u11n31_q", "H", "O3", "Why is an electromagnet, not a permanent magnet, used in a security door lock?", ("It can be switched off to let the door open", "Yes."),
        [("It is always on", "A permanent magnet is always on."), ("It is lighter", "That is not the reason."), ("It attracts plastic", "No magnet attracts plastic.")]),
   twin=mc("s8u11n31_t", "M", "O3", "In an electric doorbell, the electromagnet…", "pulls a metal striker onto the bell", [("heats the bell", ""), ("plays a recording", ""), ("repels the bell", "")])),
}

DROP = {"11.1": ["s8u11s1p02", "s8u11s1p03", "s8u11s1p04"], "11.2": ["s8u11s2p05", "s8u11s2p13", "s8u11s2p12"], "11.3": ["s8u11s3p04", "s8u11s3p02"]}

CUR = {"kind": "linegraph", "x": {"min": 0, "max": 2.0, "step": 0.5, "label": "Current (A)"}, "y": {"min": 0, "max": 20, "step": 5, "label": "Paper clips picked up"},
       "series": [{"pts": [[0, 0], [0.5, 4], [1.0, 8], [1.5, 12], [2.0, 15]], "label": "50 turns, iron core"}]}
CORE = {"kind": "barchart", "labels": ["no core", "aluminium", "steel", "iron"], "values": [1, 1, 9, 12], "ymax": 14, "step": 2, "ylabel": "Paper clips picked up"}
NEW_PRAC = {
 "11.1": [
  gd("s8u11s1p21", "M", "O1", "Attract or repel?", ["Force"], [("N pole near S pole", ["Attract"]), ("N pole near N pole", ["Repel"]), ("S pole near S pole", ["Repel"]), ("S pole near an iron nail", ["Attract"])], extra=[]),
  ex("s8u11s1p22", "H", "O1", "A student says a steel paper clip is a magnet because it is attracted to a magnet. Describe a test to show whether it is a permanent magnet.",
     [("bring it near both poles of a magnet / another magnet", ["both poles|each pole|N and S|north and south"]), ("only a magnet can REPEL; if it is repelled by one pole it is a magnet", ["repel"])],
     "Hold each end of the paper clip near both poles of a bar magnet. A magnetic material is always attracted, but only a magnet can be repelled. If one end is repelled by a pole, the paper clip is a magnet."),
 ],
 "11.2": [
  nm("s8u11s2p21", "M", "O2", "Use the graph. How many paper clips are picked up with a current of 1.0 A?", 8, "clips", tol=0, units=["clips", ""], fig=CUR, skill="Data"),
  ex("s8u11s2p22", "H", "O2", "Use the chart. Explain which core is best and why aluminium is no better than no core.",
     [("iron gives the strongest electromagnet (12 clips)", ["iron"]), ("aluminium is not magnetic, so it does not concentrate the field", ["not magnetic|non-magnetic|isn't magnetic|is not a magnetic"])],
     "Iron is best: it picked up 12 clips, because it is magnetic and concentrates the magnetic field. Aluminium is not a magnetic material, so it does not strengthen the field, and it picked up the same as no core.", fig=CORE, skill="Data"),
  mc("s8u11s2p23", "H", "O2", "Use the graph. What happens to the number of clips when the current is doubled from 0.5 A to 1.0 A?", "It doubles from 4 to 8", [("It halves", "It increases."), ("It stays the same", "It changes."), ("It goes up by 1", "Check the graph.")], fig=CUR, skill="Data"),
 ],
 "11.3": [
  gd("s8u11s3p22", "M", "O3", "Which job does the electromagnet do in each device?", ["Job"],
     [("Scrapyard crane", ["Lifts and drops steel"]), ("Loudspeaker", ["Moves a cone to make sound"]), ("Security door", ["Holds the door shut"])], extra=["Heats water"]),
  od("s8u11s3p21", "H", "O3", "Put the steps of an electric doorbell in order.", ["The button is pressed and the circuit is complete", "Current flows and the electromagnet is switched on", "The electromagnet pulls the striker onto the bell", "The bell rings"]),
 ],
}
NEW_ADV = {
 "11.1": [adv(ex("s8u11s1a05", "VH", "O1", "NOAA reports that a 2007 survey found the North Magnetic Pole moving about 55 km per year. How far would it move in 10 years at this rate, and why must navigation systems on phones and planes be updated regularly?",
     [("about 550 km in 10 years", ["550"]), ("compasses point to the magnetic pole, which moves / is not the geographic pole", ["magnetic (north )?pole.{0,40}(move|chang|drift)|not.{0,20}geographic|moves"]), ("so the difference between magnetic and true north changes, and maps/models must be corrected", ["update|correct|model|map|chang|difference|direction"])],
     "55 km × 10 = 550 km. A compass points towards the magnetic pole, not the geographic North Pole. Because the magnetic pole moves, the angle between magnetic north and true north changes, so the models used by phones and planes must be updated to give correct directions.", need=2, src=src("SRC-NCEIPOLE")))],
}

from tests_stage8_unit11_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
