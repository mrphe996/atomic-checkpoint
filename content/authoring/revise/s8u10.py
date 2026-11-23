# -*- coding: utf-8 -*-
"""Stage 8 Unit 10 Light — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NASASKY", "name": "NASA Space Place – Why Is the Sky Blue?", "url": "https://spaceplace.nasa.gov/blue-sky/en/", "use": "Blue sky and red sunset Challenge question (10.4)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s8u10n21": dict(note="Paused on the graph: angle of reflection plotted against angle of incidence, 10° to 70°.",
   q=ex("s8u10n21_q", "H", "O2", "Do the results support the law of reflection? Explain, and suggest why some readings are 1° out.",
        [("yes: the angles are equal / straight line where i = r", ["yes|support|equal|same"]), ("differences come from measuring error, e.g. protractor or width of ray", ["protractor|width|thick|error|read|measur"])],
        "Yes. The angle of reflection equals the angle of incidence within 1°, so the points lie on the line i = r. The small differences come from measuring errors, such as reading the protractor or the width of the ray."),
   twin=nm("s8u10n21_t", "M", "O2", "A ray hits a mirror with an angle of incidence of 45°. What is the angle of reflection?", 45, "°", tol=0, units=["°", "degrees"])),
 "s8u10n31p": dict(note="Paused before water is poured into a cup with a hidden coin.",
   q=mc("s8u10n31p_q", "M", "O3", "PREDICT: what will you see when water is poured in?", ("The coin comes into view", "Good prediction – now watch."),
        [("Nothing changes", "Watch carefully."), ("The coin disappears even more", "Watch carefully."), ("The coin floats up", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u10n31p_t", "M", "O3", "Refraction is…", "the bending of light when it passes from one material into another", [("the bouncing of light off a mirror", ""), ("the splitting of light into colours only", ""), ("light being absorbed", "")])),
 "s8u10n31e": dict(note="Paused after the coin came back into view.",
   q=ex("s8u10n31e_q", "H", "O3", "EXPLAIN why the coin became visible.",
        [("light from the coin bends / refracts at the water surface", ["refract|bend|bent"]), ("it speeds up / bends away from the normal and reaches the eye over the rim", ["away from the normal|speeds up|faster|over the rim|reach.{0,15}eye|into (your|the) eye"])],
        "Light from the coin refracts at the water surface: it speeds up as it passes into air and bends away from the normal, so it travels over the rim into your eye."),
   twin=mc("s8u10n31e_t", "H", "O3", "To the observer, the coin in water seems…", "higher than it really is", [("lower than it really is", ""), ("in exactly the right place", ""), ("bigger and further away", "")])),
 "s8u10n51p": dict(note="Paused before a white card, a red apple and a green leaf are lit with red light only.",
   q=mc("s8u10n51p_q", "M", "O5", "PREDICT: what colour will the green leaf appear in red light?", ("Black (dark)", "Good prediction – now watch."),
        [("Green", "Watch carefully."), ("Red", "Watch carefully."), ("Yellow", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u10n51p_t", "M", "O5", "A green leaf in white light looks green because it…", "reflects green and absorbs the other colours", [("absorbs green", ""), ("gives out green light", ""), ("reflects all colours", "")])),
 "s8u10n51e": dict(note="Paused after the card and apple looked red and the leaf looked dark.",
   q=gd("s8u10n51e_q", "H", "O5", "What colour does each object look in red light?", ["Colour"],
        [("White card", ["Red"]), ("Red apple", ["Red"]), ("Green leaf", ["Black"])], extra=["White", "Green"], skill="Data"),
   twin=mc("s8u10n51e_t", "H", "O5", "What colour does a blue shirt look in green light?", "Black", [("Blue", ""), ("Green", ""), ("Cyan", "")])),
}

DROP = {"10.1": ["s8u10s1p04", "s8u10s1p09"], "10.2": ["s8u10s2p02", "s8u10s2p09", "s8u10s2p03"], "10.3": ["s8u10s3p01", "s8u10s3p05", "s8u10s3p06"],
        "10.4": ["s8u10s4p03", "s8u10s4p05"], "10.5": ["s8u10s5p05", "s8u10s5p03", "s8u10s5p02"]}

REFR = {"kind": "linegraph", "x": {"min": 0, "max": 80, "step": 20, "label": "Angle of incidence in air (°)"}, "y": {"min": 0, "max": 50, "step": 10, "label": "Angle of refraction in glass (°)"},
        "series": [{"pts": [[0, 0], [20, 13], [40, 25], [60, 35], [80, 41]], "label": "air into glass"}]}
TRANS = {"kind": "barchart", "labels": ["clear glass", "tracing paper", "frosted glass", "card"], "values": [90, 45, 60, 0], "ymax": 100, "step": 20, "ylabel": "Light passing through (%)"}
NEW_PRAC = {
 "10.1": [
  gd("s8u10s1p21", "M", "O1", "Use the chart. Classify each material.", ["Type"],
     [("Clear glass", ["Transparent"]), ("Tracing paper", ["Translucent"]), ("Frosted glass", ["Translucent"]), ("Card", ["Opaque"])], extra=["Luminous"], fig=TRANS, skill="Data"),
  nm("s8u10s1p22", "H", "O1", "Light travels at 300 000 km/s. The Moon is about 384 000 km away. How long does light take to reach us from the Moon? Give your answer to 2 decimal places.", 1.28, "s", tol=0.01, units=["s"]),
 ],
 "10.2": [
  nm("s8u10s2p21", "H", "O2", "A ray makes an angle of 30° with the SURFACE of a mirror. What is the angle of reflection (measured from the normal)?", 60, "°", tol=0, units=["°", "degrees"]),
  ex("s8u10s2p22", "H", "O2", "A student measures the angle of reflection for one ray only and concludes that i = r always. Suggest how she can make her conclusion more reliable.",
     [("use several different angles of incidence", ["different angles|several angles|range|more angles"]), ("repeat each measurement / use a thin ray / mark the rays carefully", ["repeat|thin|narrow|mark|careful|average"])],
     "She should test a range of different angles of incidence, repeat each measurement, and use a thin ray marked carefully, so that she can see whether i = r every time."),
 ],
 "10.3": [
  nm("s8u10s3p21", "M", "O3", "Use the graph. What is the angle of refraction when the angle of incidence is 40°?", 25, "°", tol=1, units=["°", "degrees"], fig=REFR, skill="Data"),
  ex("s8u10s3p22", "H", "O3", "Use the graph. Explain why the angle in glass is always smaller than the angle in air.",
     [("light slows down when it enters glass", ["slow|optically denser|denser"]), ("so it bends towards the normal", ["towards the normal|toward the normal"])],
     "Light slows down when it enters the glass, so it bends towards the normal. This makes the angle of refraction smaller than the angle of incidence.", fig=REFR, skill="Data"),
  mc("s8u10s3p23", "M", "O3", "Use the graph. What happens to a ray at 0° (along the normal)?", "It passes straight through without bending", [("It bends by 41°", "That is at 80°."), ("It is reflected back", "Not at this boundary."), ("It splits into colours", "Not along the normal.")], fig=REFR),
 ],
 "10.4": [
  od("s8u10s4p21", "M", "O4", "Put the colours of the spectrum in order, from least bent to most bent.", ["red", "orange", "yellow", "green", "blue", "violet"]),
 ],
 "10.5": [
  gd("s8u10s5p21", "H", "O5", "What colour does each object look under green light?", ["Colour"],
     [("White paper", ["Green"]), ("Green apple", ["Green"]), ("Red tomato", ["Black"]), ("Black bag", ["Black"])], extra=["Red", "White"]),
  mc("s8u10s5p22", "H", "O5", "A shop lights its meat counter with red-tinted lamps. Why?", "Red meat reflects red light, so it looks brighter and fresher", [("Red light keeps meat cold", "Light colour does not cool meat."), ("Red light kills bacteria", "No."), ("Meat absorbs red light", "It reflects red.")]),
 ],
}
NEW_ADV = {
 "10.4": [adv(ex("s8u10s4a05", "VH", "O4", "NASA explains that air molecules scatter blue light more than other colours. Use this idea to explain why the daytime sky is blue but the sky near the setting Sun looks red or orange.",
     [("sunlight / white light is a mixture of colours", ["mixture|all colours|white light"]), ("blue light is scattered in all directions by air, so blue reaches our eyes from all over the sky", ["blue.{0,40}scatter|scatter.{0,40}blue"]), ("at sunset light passes through more air, blue is scattered away, leaving red / orange", ["more air|further|longer path|scattered away|removed|leav.{0,20}(red|orange)"])],
     "Sunlight is a mixture of colours. Air molecules scatter blue light much more than red, so blue light reaches our eyes from every part of the sky and it looks blue. At sunset the light passes through much more air, so most of the blue is scattered away before it reaches us, leaving mainly red and orange light.", need=2, src=src("SRC-NASASKY")))],
}

from tests_stage8_unit10_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
