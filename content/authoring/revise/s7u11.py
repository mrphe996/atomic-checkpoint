# -*- coding: utf-8 -*-
"""Stage 7 Unit 11 Energy — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-FTCLB", "name": "U.S. Federal Trade Commission – Shopping for Light Bulbs", "url": "https://www.consumer.ftc.gov/articles/0164-shopping-light-bulbs", "use": "60 W incandescent ≈ 800 lumens; an LED gives the same light with about 9 W (video chart and Challenge question, 11.3)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "u11n11": dict(note="Paused on the graph: bounce height is about 70% of drop height.",
   q=nm("u11n11_q", "H", "O1", "Use the graph. Predict the bounce height for a drop of 250 cm.", 173, "cm", tol=6, units=["cm"], skill="Data"),
   twin=mc("u11n11_t", "M", "O1", "A ball held higher above the ground stores more…", "gravitational potential energy", [("kinetic energy", ""), ("nuclear energy", ""), ("sound energy", "")])),
 "u11n12p": dict(note="Paused before the ball is dropped from 1 m.",
   q=mc("u11n12p_q", "M", "O2", "PREDICT: how high will the ball bounce?", ("Lower than 1 m", "Good prediction – now watch."),
        [("Exactly 1 m", "Watch carefully."), ("Higher than 1 m", "That would need extra energy from somewhere."), ("It will not bounce at all", "Watch carefully.")], skill="Prediction"),
   twin=mc("u11n12p_t", "M", "O2", "As the ball falls, energy is transferred from the gravitational potential store to the…", "kinetic store", [("chemical store", ""), ("nuclear store", ""), ("elastic store only", "")])),
 "u11n12e": dict(note="Paused after the ball bounced to only about 70 cm.",
   q=ex("u11n12e_q", "H", "O2", "EXPLAIN why the ball did not bounce back to 1 m. Energy is never destroyed, so where did it go?",
        [("some energy transferred to the surroundings", ["surround|dissipat|wasted|lost"]), ("as sound and heat / thermal", ["sound|heat|thermal|warm"])],
        "Some of the energy was transferred to the surroundings as sound and heat when the ball hit the floor, so less energy was left to lift the ball back up."),
   twin=mc("u11n12e_t", "H", "O2", "Which statement is correct?", "Energy cannot be created or destroyed, only transferred", [("Energy is used up and disappears", ""), ("Energy is created when a ball bounces", ""), ("Bouncing balls make extra energy", "")])),
 "u11n13": dict(note="Paused on the chart: tungsten 60 W, halogen 43 W, fluorescent 14 W, LED 9 W for the same light.",
   q=mc("u11n13_q", "H", "O3", "Why does the tungsten bulb need so much more power for the same amount of light?", ("It wastes most of its energy as heat", "Yes – it is the least efficient."),
        [("It gives much more light", "All four give about the same light."), ("Tungsten is a poor conductor", "That is not the reason."), ("It is a bigger bulb", "Size is not the reason.")], skill="Data"),
   twin=nm("u11n13_t", "M", "O3", "How many watts less does the LED use than the tungsten bulb for the same light?", 51, "W", tol=0.5, units=["W"])),
 "u11n14p": dict(note="Paused before the air is pumped out of the jar with the ringing bell.",
   q=mc("u11n14p_q", "M", "O4", "PREDICT: what will happen to the sound as the air is pumped out?", ("It will get quieter", "Good prediction – now watch."),
        [("It will get louder", "Watch carefully."), ("It will not change", "Watch carefully."), ("The bell will stop moving", "Watch the bell closely.")], skill="Prediction"),
   twin=mc("u11n14p_t", "M", "O4", "Sound is made when objects…", "vibrate", [("melt", ""), ("glow", ""), ("stay still", "")])),
 "u11n14e": dict(note="Paused after the sound faded although the bell kept moving.",
   q=ex("u11n14e_q", "H", "O4", "EXPLAIN why the sound faded even though the bell was still moving.",
        [("sound needs particles to travel / is passed particle to particle", ["particle|medium|air"]), ("fewer particles as air was removed / no particles in a vacuum", ["fewer|less air|removed|vacuum|no air|pumped"])],
        "Sound is passed on by vibrating particles. As the air was pumped out there were fewer particles to carry the vibrations, and in a vacuum there are none, so the sound could not reach us."),
   twin=mc("u11n14e_t", "M", "O4", "Why is space silent?", "It is almost a vacuum, with no particles to carry sound", [("It is too cold", ""), ("It is too dark", ""), ("Sound is too slow", "")])),
 "u11n15": dict(note="Paused on the chart: air 343 m/s, water 1480 m/s, steel 5960 m/s.",
   q=ex("u11n15_q", "H", "O4", "Use the particle model to explain why sound travels fastest in steel.",
        [("particles in a solid are closest together", ["close|packed|tight|near"]), ("vibrations are passed on more quickly", ["pass|quick|fast|easil|next"])],
        "In a solid the particles are packed closest together, so each vibrating particle passes the vibration to the next one very quickly."),
   twin=mc("u11n15_t", "M", "O4", "In which material does sound travel slowest?", "Air", [("Water", ""), ("Steel", ""), ("Wood", "")])),
}

DROP = {"11.1": ["u11s1p01", "u11s1p02", "u11s1p05"], "11.2": ["u11s2p01", "u11s2p03", "u11s2p13"], "11.3": ["u11s3p01", "u11s3p03", "u11s3p18"], "11.4": ["u11s4p01", "u11s4p03", "u11s4p16"]}

FOOD = {"kind": "barchart", "labels": ["apple", "banana", "bread slice", "chocolate bar"], "values": [220, 400, 330, 1050], "ymax": 1200, "step": 200, "ylabel": "Energy (kJ)", "xlabel": "Food (one portion)"}
KETT = {"kind": "barchart", "labels": ["kettle A", "kettle B", "kettle C"], "values": [85, 70, 92], "ymax": 100, "step": 20, "ylabel": "Efficiency (%)", "xlabel": "Kettle"}
ECHO = {"kind": "linegraph", "x": {"min": 0, "max": 400, "step": 100, "label": "Distance to wall (m)"}, "y": {"min": 0, "max": 2.5, "step": 0.5, "label": "Time for echo (s)"},
        "series": [{"pts": [[0, 0], [100, 0.6], [200, 1.2], [300, 1.75], [400, 2.35]], "label": "echo time"}]}
NEW_PRAC = {
 "11.1": [
  mc("u11s1p21", "M", "O1", "Use the bar chart. Which food stores the most chemical energy per portion?", "Chocolate bar", [("Banana", "The banana stores 400 kJ."), ("Bread slice", "The bread stores 330 kJ."), ("Apple", "The apple stores the least.")], fig=FOOD, skill="Data"),
  nm("u11s1p22", "H", "O1", "Use the bar chart. How many joules are stored in the banana?", 400000, "J", tol=0, units=["J"], fig=FOOD, skill="Data", hint="1 kJ = 1000 J"),
  gd("u11s1p23", "H", "O1", "Which energy store is the main one in each object?", ["Store"],
     [("A drawn bow, ready to fire", ["Elastic potential"]), ("A rock at the top of a cliff", ["Gravitational potential"]), ("A cup of hot tea", ["Thermal"]), ("A rolling bowling ball", ["Kinetic"])], extra=["Nuclear"]),
 ],
 "11.2": [
  od("u11s2p21", "H", "O2", "A ball is dropped and bounces. Put the main energy stores in order, starting from when it is held.", ["gravitational potential", "kinetic (falling)", "elastic potential (squashed)", "kinetic (rising)"]),
  mc("u11s2p22", "H", "O2", "A swing goes a little less high on each swing. Which is the best explanation?", "Energy is transferred to the surroundings by air resistance and friction", [("Energy is destroyed", "Energy cannot be destroyed."), ("Gravity gets weaker", "Gravity stays the same."), ("The swing's mass increases", "Its mass does not change.")]),
  gd("u11s2p23", "M", "O2", "How is energy mainly transferred?", ["Transfer"],
     [("A phone charging", ["Electrically"]), ("Sunlight warming a leaf", ["By light (waves)"]), ("A hot pan warming a handle", ["By heating"]), ("Pushing a trolley", ["Mechanically"])], extra=[]),
 ],
 "11.3": [
  mc("u11s3p21", "M", "O3", "Use the bar chart. Which kettle is the most efficient?", "Kettle C", [("Kettle A", "85% is less than 92%."), ("Kettle B", "Kettle B is the least efficient."), ("They are all the same", "The bars are different heights.")], fig=KETT, skill="Data"),
  nm("u11s3p22", "H", "O3", "Use the bar chart. Kettle B is given 1000 J of electrical energy. How much is wasted?", 300, "J", tol=0, units=["J"], fig=KETT, skill="Data"),
  mc("u11s3p23", "H", "O3", "Kettle B has no lid and a thin metal body. Which change would most likely make it more efficient?", "Add a lid and an insulating layer", [("Paint it black", "That would make it lose heat faster."), ("Use more water than needed", "Heating extra water wastes energy."), ("Make it out of thinner metal", "That would lose more heat.")]),
 ],
 "11.4": [
  nm("u11s4p21", "M", "O4", "Use the graph. How long does the echo take to return from a wall 200 m away?", 1.2, "s", tol=0.05, units=["s"], fig=ECHO, skill="Data"),
  nm("u11s4p22", "H", "O4", "Use the graph. The echo from a cliff takes 2.35 s. How far away is the cliff?", 400, "m", tol=5, units=["m"], fig=ECHO, skill="Data"),
  ex("u11s4p23", "H", "O4", "Describe how a ship can use sonar to find the depth of the sea.",
     [("send a sound (pulse) down", ["send|pulse|emit|sound down"]), ("time how long the echo takes to return", ["time|echo|return|reflect"]), ("use speed × time ÷ 2 (there and back)", ["speed|÷ ?2|divide|half|there and back"])],
     "The ship sends a pulse of sound down to the seabed and times how long the echo takes to come back. The depth is speed of sound × time ÷ 2, because the sound travels down and back up.", need=2),
 ],
}
NEW_ADV = {
 "11.3": [adv(ex("u11s3a5", "VH", "O3", "The U.S. Federal Trade Commission says a 60 W traditional bulb gives about 800 lumens of light, and an LED gives the same light using only about 9 W. Explain what this tells you about the efficiency of the two bulbs, and why switching saves money.",
     [("LED is more efficient / wastes less energy", ["led.{0,40}(more efficient|wastes less|less wast)|more efficient"]), ("tungsten wastes most energy as heat", ["heat|thermal|wast"]), ("less power → less energy used → lower bill", ["less (power|energy|electricity)|cheaper|bill|cost|money"])],
     "Both give the same useful light, but the LED needs only 9 W while the old bulb needs 60 W, so the LED is much more efficient; the old bulb wastes most of its energy as heat. Using less power means less electrical energy is used, so electricity bills are lower.", need=2, src=src("SRC-FTCLB")))],
}

from tests_stage7_unit11_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
