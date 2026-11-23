# -*- coding: utf-8 -*-
"""Stage 8 Unit 4 The Structure of an Atom — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-HYPERRUTH", "name": "HyperPhysics (Georgia State University) – Evidence for nuclear interaction (Rutherford scattering)", "url": "https://hyperphysics.gsu.edu/hbase/Nuclear/rutsca3.html", "use": "Geiger and Marsden: about 1 in 8000 alpha particles scattered by more than 90° (Challenge question, 4.2)."},
    {"id": "SRC-APSRUTH", "name": "APS News – This Month in Physics History: Rutherford and the discovery of the atomic nucleus", "url": "https://www.aps.org/apsnews/2006/05/rutherford-discovery-atomic-nucleus", "use": "Background to the gold foil experiment and the plum pudding model (Challenge question, 4.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s8u04n11p": dict(note="Paused before a balloon rubbed on hair is held near a stream of water.",
   q=mc("s8u04n11p_q", "M", "O2", "PREDICT: what will the stream of water do?", ("Bend towards the balloon", "Good prediction – now watch."),
        [("Bend away from the balloon", "Watch carefully."), ("Stop flowing", "Watch carefully."), ("Nothing", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u04n11p_t", "M", "O2", "Rubbing a balloon on hair moves…", "electrons onto the balloon", [("protons onto the balloon", ""), ("neutrons off the balloon", ""), ("atoms of hair into the balloon", "")])),
 "s8u04n11e": dict(note="Paused after the water bent towards the balloon.",
   q=ex("s8u04n11e_q", "H", "O2", "EXPLAIN why the water bent, and link it to how an atom holds its electrons.",
        [("balloon has a negative charge (extra electrons)", ["negative|extra electron"]), ("opposite charges attract", ["opposite|attract"]), ("same force holds electrons near the positive nucleus", ["nucleus|proton"])],
        "The balloon gained electrons, so it is negatively charged, and opposite charges attract, so the water was pulled towards it. In an atom, the same attraction holds the negative electrons around the positive nucleus.", need=2),
   twin=mc("s8u04n11e_t", "M", "O2", "Like charges…", "repel", [("attract", ""), ("cancel out", ""), ("have no effect", "")])),
 "s8u04n12": dict(note="Paused on the chart of atomic numbers: H 1, He 2, C 6, N 7, O 8, Na 11.",
   q=mc("s8u04n12_q", "H", "O3", "A neutral sodium atom has 11 protons. How many electrons, and how are they arranged?", ("11 electrons: 2, 8, 1", "Yes."),
        [("11 electrons: 8, 2, 1", "The first shell holds only 2."), ("12 electrons: 2, 8, 2", "Electrons equal protons."), ("1 electron in one shell", "That is hydrogen.")], skill="Data"),
   twin=nm("s8u04n12_t", "M", "O3", "Oxygen has atomic number 8. How many electrons does a neutral oxygen atom have?", 8, "", tol=0, units=["", "electrons"])),
 "s8u04n13p": dict(note="Paused before alpha particles are fired at the gold foil.",
   q=mc("s8u04n13p_q", "M", "O4", "PREDICT: if the plum pudding model is right, what will happen to the alpha particles?", ("They will all pass straight through with tiny deflections", "That is what Rutherford expected – now watch."),
        [("They will all bounce back", "The positive charge is spread thinly in this model."), ("They will stick to the foil", "Watch carefully."), ("They will turn into gold", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u04n13p_t", "M", "O4", "Alpha particles have a…", "positive charge", [("negative charge", ""), ("no charge", ""), ("magnetic charge", "")])),
 "s8u04n13e": dict(note="Paused after: most straight through, a few deflected, very few bounced back.",
   q=gd("s8u04n13e_q", "H", "O4", "What does each observation show?", ["Conclusion"],
        [("Most passed straight through", ["The atom is mostly empty space"]), ("A very few bounced straight back", ["There is a tiny, dense nucleus"]), ("Positive particles were pushed away", ["The nucleus is positively charged"])], extra=[]),
   twin=mc("s8u04n13e_t", "H", "O4", "Which model replaced the plum pudding model after this experiment?", "The nuclear model with a tiny central nucleus", [("Dalton's solid-sphere model", ""), ("The electron-cloud model only", ""), ("No model", "")])),
}

DROP = {"4.1": ["s8u04s1p01", "s8u04s1p06", "s8u04s1p14"], "4.2": ["s8u04s2p08", "s8u04s2p10", "s8u04s2p11"]}

SHELL = {"kind": "barchart", "labels": ["Li", "Be", "B", "C", "N", "O", "F", "Ne"], "values": [1, 2, 3, 4, 5, 6, 7, 8], "ymax": 8, "step": 1, "ylabel": "Electrons in the outer shell", "xlabel": "Element (atomic numbers 3 to 10)"}
SCAT = {"kind": "barchart", "labels": ["0–10°", "10–30°", "30–90°", "over 90°"], "values": [9900, 85, 14, 1], "ymax": 10000, "step": 2000, "ylabel": "Number of alpha particles (out of 10 000)", "xlabel": "Angle of deflection"}
NEW_PRAC = {
 "4.1": [
  mc("s8u04s1p21", "M", "O3", "Use the bar chart. Which element has a full outer shell?", "Neon (Ne)", [("Lithium (Li)", "It has 1 outer electron."), ("Oxygen (O)", "It needs 2 more."), ("Carbon (C)", "It has 4 of 8.")], fig=SHELL, skill="Data"),
  mc("s8u04s1p22", "H", "O3", "Use the bar chart. Fluorine needs one more electron to fill its outer shell. Which element would most easily give it one?", "Lithium, which has 1 outer electron", [("Neon, which has a full shell", "Neon does not lose electrons easily."), ("Carbon, which has 4", "Carbon shares rather than gives."), ("Oxygen, which needs 2", "Oxygen also gains electrons.")], fig=SHELL, skill="Data"),
  gd("s8u04s1p23", "H", "O1", "Complete the table for a carbon atom (atomic number 6, 6 neutrons).", ["Number"],
     [("Protons", ["6"]), ("Neutrons", ["6"]), ("Electrons", ["6"]), ("Electrons in the first shell", ["2"])], extra=["4", "12"]),
 ],
 "4.2": [
  mc("s8u04s2p21", "M", "O4", "Use the bar chart of results. What happened to most alpha particles?", "They were deflected by less than 10°", [("They bounced back", "Only about 1 did."), ("They were deflected by 30–90°", "Only about 14."), ("They were absorbed", "They were detected after passing through.")], fig=SCAT, skill="Data"),
  ex("s8u04s2p22", "H", "O4", "Use the bar chart. Explain why the result 'over 90°' was so surprising to Rutherford.",
     [("plum pudding model predicted only small deflections", ["plum pudding|small deflect|spread|thin"]), ("a large deflection needs a tiny, dense, concentrated positive charge (nucleus)", ["nucleus|dense|concentrat|tiny"])],
     "In the plum pudding model the positive charge was spread out thinly, so alpha particles should only be deflected a tiny amount. Bouncing back over 90° showed that the positive charge and mass were concentrated in a tiny, dense nucleus.", fig=SCAT),
  od("s8u04s2p23", "H", "O4", "Order the atomic models by date, earliest first.", ["Dalton's solid spheres", "Thomson's plum pudding", "Rutherford's nuclear model", "Chadwick finds the neutron"]),
 ],
}
NEW_ADV = {
 "4.2": [adv(nm("s8u04s2a05", "VH", "O4", "Geiger and Marsden found that about 1 in every 8000 alpha particles was scattered by more than 90°. If 40 000 alpha particles were fired at the foil, about how many would bounce back by more than 90°?", 5, "", tol=0, units=["", "particles"], src=src("SRC-HYPERRUTH"))),
         adv(ex("s8u04s2a06", "VH", "O4", "Rutherford's team expected the plum pudding model to be confirmed, but it was not. Explain what this shows about how scientific models develop.",
     [("evidence did not fit the model", ["evidence|result|observ|did not fit|contradict"]), ("so the model was changed / replaced by a better one", ["chang|replac|new model|improv|updat"])],
     "The results did not fit the plum pudding model, so scientists replaced it with a new nuclear model that explained the evidence. Models change when new evidence is found.", src=src("SRC-APSRUTH")))],
}

from tests_stage8_unit04_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
