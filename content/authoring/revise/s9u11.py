# -*- coding: utf-8 -*-
"""Stage 9 Unit 11 Sound — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NIOSHNOISE", "name": "CDC / NIOSH – Noise-Induced Hearing Loss (recommended exposure limit)", "url": "https://www.cdc.gov/niosh/noise/about/noise.html", "use": "85 dBA over 8 hours and the 3 dB exchange rate: Challenge question (11.2)."},
    {"id": "SRC-NIDCDNIHL", "name": "NIDCD (US National Institutes of Health) – Noise-Induced Hearing Loss", "url": "https://www.nidcd.nih.gov/health/noise-induced-hearing-loss-0", "use": "Typical decibel levels of everyday sounds for the video chart (11.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

SPD = {"kind": "barchart", "labels": ["air", "water", "steel"], "values": [343, 1480, 5960], "ymax": 6500, "step": 1000, "ylabel": "Speed of sound (m/s)"}
DB = {"kind": "barchart", "labels": ["whisper", "conversation", "lawnmower", "concert", "siren", "jet"], "values": [30, 60, 90, 105, 120, 140], "ymax": 150, "step": 30, "ylabel": "Sound level (dB)"}

NEW_STOPS = {
 "s9u11n11p": dict(note="Paused before the air is pumped out of a jar with a ringing bell.",
   q=mc("s9u11n11p_q", "M", "O1", "PREDICT: what will happen to the sound as the air is removed?", ("It will get quieter", "Good prediction – now watch."),
        [("It will get louder", "Watch carefully."), ("It will stay the same", "Watch carefully."), ("Its pitch will get higher", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u11n11p_t", "M", "O1", "A material that sound travels through is called a…", "medium", [("vacuum", ""), ("wave", ""), ("vibration", "")])),
 "s9u11n11e": dict(note="Paused after the ringing faded although the hammer kept moving.",
   q=ex("s9u11n11e_q", "H", "O1", "EXPLAIN why the sound faded although the bell kept vibrating.",
        [("sound needs particles / a medium to travel", ["particles|medium"]), ("fewer air particles to pass on vibrations; none in a vacuum", ["fewer|vacuum|no air|less air|removed"])],
        "Sound needs a medium of particles to pass on the vibrations. As the air was pumped out there were fewer particles to carry the vibrations to the glass and our ears, so the sound faded. In a vacuum sound cannot travel."),
   twin=mc("s9u11n11e_t", "M", "O1", "Why could we still SEE the hammer moving?", "Light can travel through a vacuum, but sound cannot", [("Light needs air to travel", ""), ("The jar was still full of air", ""), ("Sound is faster than light", "")])),
 "s9u11n12": dict(note="Paused on the chart: air 343, water 1480, steel 5960 m/s.",
   q=ex("s9u11n12_q", "H", "O1", "Why is sound fastest in steel and slowest in air?",
        [("particles in solids are closest together (air particles far apart)", ["close|tightly|far apart"]), ("so vibrations are passed on more quickly", ["pass(ed)? on|quick|faster"])],
        "In steel the particles are very close together and strongly linked, so vibrations are passed on quickly. In air the particles are far apart, so it takes longer for vibrations to pass from one to the next.", skill="Data"),
   twin=nm("s9u11n12_t", "M", "O1", "Use the chart. How many times faster is sound in water than in air (to 1 decimal place)?", 4.3, "", tol=0.1, units=[""], fig=SPD)),
 "s9u11n21": dict(note="Paused on the chart: whisper 30, conversation 60, lawnmower 90, concert 105, siren 120, jet 140 dB.",
   q=ms("s9u11n21_q", "H", "O2", "Select ALL the sounds that could damage hearing with long or repeated exposure (85 dB or more).", ["lawnmower", "concert", "siren", "jet take-off"], [("whisper", "30 dB is safe."), ("conversation", "60 dB is safe.")], skill="Data"),
   twin=nm("s9u11n21_t", "M", "O2", "Use the chart. How many decibels louder is a concert than normal conversation?", 45, "dB", tol=0, units=["dB"], fig=DB)),
}

DROP = {"11.1": ["s9u11s1p03", "s9u11s1p05", "s9u11s1p04"], "11.2": ["s9u11s2p03", "s9u11s2p04", "s9u11s2p01"], "11.4": ["s9u11s4p01", "s9u11s4p02"]}

WAVES = {"kind": "barchart", "labels": ["sound A", "sound B", "sound C"], "values": [2, 5, 3], "ymax": 6, "step": 1, "ylabel": "Amplitude on oscilloscope (squares)"}
NEW_PRAC = {
 "11.1": [
  nm("s9u11s1p21", "H", "O1", "Use the chart. Sound travels 1715 m through air. How long does it take?", 5, "s", tol=0, units=["s"], fig=SPD, skill="Data"),
  ex("s9u11s1p22", "H", "O1", "Describe how a loudspeaker produces a sound wave in the air.",
     [("the cone vibrates back and forth", ["vibrat|back and forth|oscillat"]), ("moving forward squashes air particles (compression); moving back spreads them (rarefaction)", ["compression|rarefaction|squash|spread"]), ("these pass on from particle to particle to the ear", ["pass|particle to particle|ear|travel"])],
     "The speaker cone vibrates back and forth. Moving forward, it squashes air particles together (a compression); moving back, it spreads them apart (a rarefaction). These compressions and rarefactions pass from particle to particle until they reach the ear.", need=3),
 ],
 "11.2": [
  mc("s9u11s2p21", "M", "O2", "Use the chart. Which sound is loudest?", "Sound B", [("Sound A", "Smallest amplitude."), ("Sound C", "3 squares."), ("All the same", "The amplitudes differ.")], fig=WAVES, skill="Data"),
  nm("s9u11s2p22", "M", "O3", "A tuning fork vibrates 440 times every second. What is its frequency?", 440, "Hz", tol=0, units=["Hz"]),
  gd("s9u11s2p23", "H", "O3", "Can a human hear it? (Human range about 20–20 000 Hz)", ["Audible?"],
     [("A dog whistle at 30 000 Hz", ["No"]), ("A piano note at 262 Hz", ["Yes"]), ("An elephant rumble at 10 Hz", ["No"])], extra=[]),
 ],
 "11.4": [
  nm("s9u11s4p21", "M", "O4", "Two waves in phase, with amplitudes of 2 cm and 3 cm, meet. What is the amplitude of the combined wave?", 5, "cm", tol=0, units=["cm"]),
  ex("s9u11s4p22", "H", "O4", "Explain how noise-cancelling headphones reduce engine noise on a plane.",
     [("a microphone records the outside noise", ["microphone|record|detect"]), ("the headphones play an inverted / out-of-phase copy", ["out of phase|invert|reverse|opposite"]), ("crests meet troughs and cancel: destructive interference", ["destructive|cancel"])],
     "A microphone picks up the engine noise. The headphones play back an inverted copy that is out of phase with it, so crests meet troughs and cancel out by destructive interference, making the noise much quieter.", need=3),
 ],
}
NEW_ADV = {
 "11.2": [adv(ex("s9u11s2a05", "VH", "O2", "NIOSH recommends a limit of 85 dBA averaged over an 8-hour working day, and halving the time for every 3 dBA increase. How long can a worker safely spend at 91 dBA? Explain why the limit matters for people who use headphones.",
     [("85 → 88 halves to 4 hours; 88 → 91 halves to 2 hours", ["2 hours|two hours|2 h"]), ("louder sounds damage hearing more quickly / permanently", ["damage|permanent|hearing loss"]), ("headphones at high volume can exceed 85 dB, so keep volume down / take breaks", ["volume|lower|breaks|limit|85"])],
     "From 85 dBA to 88 dBA the safe time halves to 4 hours, and from 88 to 91 dBA it halves again to 2 hours. Louder sounds damage the inner ear more quickly and the damage is permanent. Headphones at high volume can easily exceed 85 dB, so users should keep the volume down and take breaks.", need=2, src=src("SRC-NIOSHNOISE")))],
}

from tests_stage9_unit11_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
