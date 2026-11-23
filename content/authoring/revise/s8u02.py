# -*- coding: utf-8 -*-
"""Stage 8 Unit 2 Human Body Systems — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NHSBTO", "name": "NHS Blood and Transplant – O negative blood type", "url": "https://www.blood.co.uk/why-give-blood/the-need-for-blood/group-o/", "use": "About 8% of people are O negative, but it makes up about 13% of hospital requests for red cells (Challenge question, 2.3)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s8u02n11p": dict(note="Paused before the elastic 'biceps' of the model arm is pushed and then pulled.",
   q=mc("s8u02n11p_q", "M", "O1", "PREDICT: what will make the model arm bend?", ("Pulling the elastic", "Good prediction – now watch."),
        [("Pushing the elastic", "Watch carefully."), ("Both pushing and pulling", "Watch carefully."), ("Neither", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u02n11p_t", "M", "O1", "The elbow is a…", "hinge joint", [("ball-and-socket joint", ""), ("fixed joint", ""), ("muscle", "")])),
 "s8u02n11e": dict(note="Paused after pushing did nothing and pulling bent the arm.",
   q=ex("s8u02n11e_q", "H", "O1", "EXPLAIN why muscles work in antagonistic pairs.",
        [("muscles can only pull / contract, not push", ["only pull|cannot push|can't push|contract"]), ("one muscle bends the joint, the other straightens it", ["bend|straighten|opposite|biceps|triceps"])],
        "Muscles can only pull by contracting; they cannot push. So a second muscle is needed to pull the bone back: the biceps bends the arm and the triceps straightens it."),
   twin=mc("s8u02n11e_t", "M", "O1", "To straighten the arm, which muscle contracts?", "Triceps", [("Biceps", ""), ("Diaphragm", ""), ("Heart", "")])),
 "s8u02n12p": dict(note="Paused before room air and breathed-out air bubble through limewater.",
   q=mc("s8u02n12p_q", "M", "O3", "PREDICT: which limewater will turn milky first?", ("The one with breathed-out air", "Good prediction – now watch."),
        [("The one with room air", "Watch carefully."), ("Both at the same time", "Watch carefully."), ("Neither will change", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u02n12p_t", "M", "O3", "Limewater turns milky with…", "carbon dioxide", [("oxygen", ""), ("nitrogen", ""), ("water vapour", "")])),
 "s8u02n12e": dict(note="Paused after the breathed-out air turned limewater milky quickly.",
   q=ex("s8u02n12e_q", "H", "O3", "EXPLAIN why breathed-out air turned the limewater milky faster.",
        [("breathed-out air has more carbon dioxide", ["more carbon dioxide|more co2|4 ?%|carbon dioxide"]), ("made by respiration in cells", ["respir|cells"])],
        "Breathed-out air contains much more carbon dioxide (about 4%) than room air, because our cells make carbon dioxide in respiration."),
   twin=mc("s8u02n12e_t", "M", "O3", "Aerobic respiration produces…", "carbon dioxide and water", [("oxygen and glucose", ""), ("starch", ""), ("nitrogen", "")])),
 "s8u02n13": dict(note="Paused on the chart: oxygen 21% in, 16% out; carbon dioxide 0.04% in, 4% out.",
   q=ex("s8u02n13_q", "H", "O2", "Where did the missing oxygen go, and where did the extra carbon dioxide come from?",
        [("oxygen diffused into the blood (in the alveoli) to be used by cells", ["blood|alveol|diffus|cells|respir"]), ("carbon dioxide made by respiration, diffused from blood into alveoli", ["respir|made|produced|from the blood|cells"])],
        "Oxygen diffused from the alveoli into the blood and was used by cells in respiration. The cells made carbon dioxide, which diffused from the blood into the alveoli and was breathed out."),
   twin=nm("s8u02n13_t", "M", "O2", "By how many percentage points does oxygen fall between air in (21%) and air out (16%)?", 5, "%", tol=0, units=["%", ""])),
 "s8u02n14": dict(note="Paused on the chart: plasma 55%, red cells 44%, white cells + platelets 1%.",
   q=mc("s8u02n14_q", "M", "O4", "Which part transports glucose and carbon dioxide, and which carries oxygen?", ("Plasma transports glucose and CO₂; red blood cells carry oxygen", "Yes."),
        [("Platelets carry oxygen; plasma fights germs", "Platelets help clotting."), ("White cells carry glucose; plasma carries oxygen", "That is the wrong way round."), ("Red cells carry glucose; platelets carry oxygen", "Red cells carry oxygen.")], skill="Data"),
   twin=nm("s8u02n14_t", "H", "O4", "An adult has 5 litres of blood. About how much is plasma (55%)?", 2.75, "litres", tol=0.05, units=["litres", "L", "l"])),
}

DROP = {"2.1": ["s8u02s1p01", "s8u02s1p04", "s8u02s1p11"], "2.2": ["s8u02s2p01", "s8u02s2p06", "s8u02s2p12"], "2.3": ["s8u02s3p05", "s8u02s3p09", "s8u02s3p14"]}

LUNG = {"kind": "barchart", "labels": ["sitting", "walking", "jogging", "sprinting"], "values": [12, 20, 35, 50], "ymax": 60, "step": 10, "ylabel": "Breaths per minute", "xlabel": "Activity"}
PULSE = {"kind": "linegraph", "x": {"min": 0, "max": 12, "step": 2, "label": "Time (min)"}, "y": {"min": 60, "max": 160, "step": 20, "label": "Pulse (beats per minute)"},
         "series": [{"pts": [[0, 70], [2, 70], [4, 135], [6, 150], [8, 105], [10, 80], [12, 72]], "label": "pulse"}]}
GRIP = {"kind": "barchart", "labels": ["8 years", "10 years", "12 years", "14 years"], "values": [12, 16, 22, 30], "ymax": 35, "step": 5, "ylabel": "Mean grip strength (kg)", "xlabel": "Age"}
NEW_PRAC = {
 "2.1": [
  mc("s8u02s1p21", "M", "O1", "Use the bar chart of a class survey. How does grip strength change with age?", "It increases as children get older", [("It decreases", "The bars get taller."), ("It stays the same", "The bars are different."), ("It only changes after 14", "It rises from 8 years.")], fig=GRIP, skill="Data"),
  ex("s8u02s1p22", "H", "O1", "Use the bar chart. Suggest a reason for the pattern.",
     [("muscles grow bigger / stronger with age", ["muscle.{0,40}(bigger|stronger|grow)|grow"]), ("bones get harder / stronger as children grow", ["bone"])],
     "As children grow, their muscles get bigger and stronger and their bones become harder, so they can grip with more force.", fig=GRIP),
  gd("s8u02s1p23", "H", "O1", "Which kind of joint?", ["Joint"],
     [("Shoulder", ["Ball and socket"]), ("Knee", ["Hinge"]), ("Skull", ["Fixed"]), ("Hip", ["Ball and socket"])], extra=[]),
 ],
 "2.2": [
  mc("s8u02s2p21", "M", "O2", "Use the bar chart. How does breathing rate change with activity?", "It increases as activity gets harder", [("It decreases", "The bars get taller."), ("It stays at 12", "Only sitting is 12."), ("It is highest when sitting", "Sitting is lowest.")], fig=LUNG, skill="Data"),
  ex("s8u02s2p22", "H", "O3", "Use the bar chart. Explain why breathing rate is highest when sprinting.",
     [("muscles respire faster / need more energy", ["respir|energy"]), ("so more oxygen is needed and more carbon dioxide removed", ["oxygen|carbon dioxide|co2"])],
     "When sprinting, the muscles respire much faster to release more energy, so they need more oxygen and produce more carbon dioxide, which must be breathed out.", fig=LUNG),
  od("s8u02s2p23", "H", "O2", "Order the path of oxygen from the air to a muscle cell.", ["nose or mouth", "trachea", "bronchus", "alveolus", "blood in a capillary", "muscle cell"]),
 ],
 "2.3": [
  nm("s8u02s3p21", "M", "O4", "Use the graph. What is the resting pulse rate?", 70, "beats per minute", tol=1, units=["beats per minute", "bpm", ""], fig=PULSE, skill="Data"),
  mc("s8u02s3p22", "H", "O4", "Use the graph. When did the exercise most likely stop?", "At about 6 minutes", [("At 2 minutes", "That is when it started."), ("At 10 minutes", "The pulse was already falling."), ("At 12 minutes", "It was back to resting by then.")], fig=PULSE, skill="Data"),
  ex("s8u02s3p23", "H", "O4", "Explain why the heart beats faster during exercise.",
     [("muscles need more oxygen and glucose", ["oxygen|glucose"]), ("blood must be pumped faster to deliver them / remove carbon dioxide", ["pump|deliver|faster|carbon dioxide|remove"])],
     "Working muscles need more oxygen and glucose for respiration, so the heart pumps blood faster to deliver them and to carry away carbon dioxide."),
 ],
}
NEW_ADV = {
 "2.3": [adv(ex("s8u02s3a05", "VH", "O4", "NHS Blood and Transplant says only about 8% of people have O negative blood, but it makes up about 13% of hospital requests for red cells. Explain why O negative blood is in such high demand.",
     [("O negative can be given to anyone / universal donor", ["anyone|everyone|universal|all blood"]), ("used in emergencies when the patient's blood type is not known", ["emergenc|not known|unknown|ambulance|quick"]), ("few people have it, so supply is limited", ["few|only 8|rare|limited|supply"])],
     "O negative red cells can be given safely to anyone, so hospitals and ambulances use them in emergencies when there is no time to find the patient's blood type. Only about 8% of people have it, so supply is limited compared with demand.", need=2, src=src("SRC-NHSBTO")))],
}

from tests_stage8_unit02_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
