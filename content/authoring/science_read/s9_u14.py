# -*- coding: utf-8 -*-
"""Science Stage 9 · Unit 14 Astronomy – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 9 (9ESs.01–9ESs.03)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}

# =====================================================================================================
# 14.1 Asteroid collision with Earth · 9ESs.01
# =====================================================================================================
READ["14.1"] = L(
    H("A rock from space",
      "The Moon's surface is covered in craters. Earth has been hit just as often – but most of its craters have worn away.",
      "What happens when a big rock from space hits a planet?"),
    I("Asteroids",
      "**Asteroids** are rocky objects orbiting the Sun, from a few metres to nearly 1000 km across. Most are in the **asteroid belt** between Mars and Jupiter.",
      fig={"kind": "orbits"},
      then=["Gravity can pull some asteroids out of their orbits and onto planets and moons."]),
    I("Asteroids and the end of the dinosaurs",
      "About 66 million years ago a huge asteroid hit what is now the Gulf of Mexico, leaving a crater around 200 km wide.",
      fig={"kind": "sciFlow", "title": "From impact to extinction", "steps": [{"t": "asteroid impact"}, {"t": "dust blocks sunlight"}, {"t": "plants cannot photosynthesise; temperatures drop"}, {"t": "food chains collapse"}, {"t": "mass extinction"}]},
      then=["Most dinosaurs died out in this **mass extinction**, but small feathered dinosaurs survived and evolved into today's birds. Drilling into the crater has found asteroid material, supporting the idea."]),
    I("Predict, watch, explain: making craters",
      "A marble is dropped into flour dusted with cocoa, first from 20 cm and then from 80 cm.",
      then=["From higher up, the marble hits faster with more **kinetic energy**, so it makes a wider crater and throws flour out in long rays – just like real impact craters."]),
    Y("Mass extinction",
      mcq("s9u14r11", "Why did the asteroid impact cause most dinosaurs to die out?",
          [("Dust blocked sunlight, so plants died and food chains collapsed.", True, "Yes."), ("The asteroid landed on every dinosaur.", False, "The impact was in one place."),
           ("It made Earth's gravity stronger.", False, "Gravity did not change."), ("It moved Earth closer to the Sun.", False, "Earth's orbit did not change.")],
          "Think about producers in food chains.", "Without sunlight, producers die, so the animals that depend on them die too.")),
    K("Key points",
      "Asteroids are rocky objects orbiting the Sun; most are in the asteroid belt.",
      "An impact 66 million years ago blocked sunlight and caused a **mass extinction**.",
      "Faster, heavier impacts make bigger craters."),
    book=BK(
        [("asteroid", "a rocky object orbiting the Sun"), ("asteroid belt", "the region between Mars and Jupiter where most asteroids orbit"), ("mass extinction", "when many species die out in a short time")],
        [], [],
        [Ex("Where are most asteroids found?", ans="in the asteroid belt between Mars and Jupiter"),
         Ex("Describe the chain of events that led from the asteroid impact to the extinction of the dinosaurs.", ans="impact → dust blocks sunlight → plants die, temperatures fall → food chains collapse → extinction"),
         Ex("Why did dropping the marble from higher make a bigger crater?", ans="It was moving faster, so it had more kinetic energy to transfer."),
         Ex("Why are there many more visible craters on the Moon than on Earth?", ans="Earth's weather, water and plate movements wear craters away; the Moon has none.", think=True)],
        ["describe asteroids", "explain how an impact caused a mass extinction"],
        look=["the chain of events", "the crater experiment"],
        note="Read it after the video: asteroids and the end of the dinosaurs (answers at the back)."),
)

# =====================================================================================================
# 14.2 The formation of the Moon · 9ESs.02
# =====================================================================================================
READ["14.2"] = L(
    H("Where did the Moon come from?",
      "The Moon is unusually large compared with its planet. Mars's moons are tiny captured rocks.",
      "How might Earth have got such a big Moon?"),
    I("The collision theory",
      "About 4.5 billion years ago, soon after Earth formed, a planet-sized body (often called **Theia**) crashed into it.",
      fig={"kind": "sciFlow", "title": "The collision theory", "steps": [{"t": "Theia hits young Earth"}, {"t": "rock is melted and thrown into space"}, {"t": "debris orbits Earth"}, {"t": "debris clumps together and cools: the Moon"}]}),
    I("Evidence",
      "Why scientists support this theory:",
      table=[["Evidence", "How it fits"], ["Moon rocks brought back by astronauts are very like Earth's outer rocks", "the Moon formed from material blasted from Earth"],
             ["the Moon has only a small iron core", "mostly lighter outer rock was thrown off"], ["the Moon's surface was once molten", "the collision released huge amounts of energy"]]),
    I("Real data: how dense are Earth and the Moon?",
      "Mean densities:",
      fig={"kind": "barchart", "labels": ["Earth", "Moon"], "values": [5.5, 3.3], "ymax": 6, "step": 1, "ylabel": "density (g/cm³)", "xlabel": "body"},
      then=["The Moon is only about 60% as dense as Earth. Iron is very dense, so the Moon must have much less iron – a small core – which fits the collision theory."]),
    Y("Density",
      num("s9u14r21", "Earth's mean density is 5.5 g/cm³ and the Moon's is 3.3 g/cm³. What fraction of Earth's density is the Moon's? Give a decimal.", 0.6, "Divide the Moon's by Earth's.", "3.3 ÷ 5.5 = 0.6.", tol=0.01)),
    K("Key points",
      "The Moon probably formed when a planet-sized body hit the young Earth.",
      "Evidence: similar rocks, a small iron core, lower density, a once-molten surface."),
    book=BK(
        [("collision theory", "the idea that the Moon formed from debris after a giant impact"), ("debris", "broken pieces thrown out by a collision")],
        [], [],
        [Ex("Describe the collision theory of how the Moon formed.", ans="A planet-sized body hit Earth; molten debris was thrown into orbit and clumped together to form the Moon."),
         Ex("Give two pieces of evidence for the theory.", ans="any two: similar rocks, small iron core, lower density, once-molten surface"),
         Ex("Explain how the Moon's lower density supports the theory.", ans="It has less dense iron, because mostly outer rock was thrown off.", think=True)],
        ["describe the collision theory", "use evidence to support it"],
        look=["the collision steps", "the density chart"],
        note="Read it after the video: how the Moon formed (answers at the back)."),
)

# =====================================================================================================
# 14.3 Nebulae: where stars are born · 9ESs.03
# =====================================================================================================
READ["14.3"] = L(
    H("A fuzzy patch",
      "On a very dark night, below the three stars of Orion's belt, there is a faint fuzzy patch that is not a star.",
      "What could it be?"),
    I("Nebulae",
      "A **nebula** is a huge cloud of **dust and gas** (mostly hydrogen and helium) in space.",
      then=["Some nebulae are **stellar nurseries** where new stars form. Others are the remains of stars that have died."]),
    I("How stars form",
      "Gravity turns a cloud into a star:",
      fig={"kind": "sciFlow", "title": "How a star forms", "steps": [{"t": "cloud of dust and gas"}, {"t": "gravity pulls a clump together"}, {"t": "it collapses and heats up"}, {"t": "core reactions start: a star shines"}]},
      then=["Stars can shine for billions of years. Our Sun formed this way about 4.6 billion years ago."]),
    I("Real life: nebulae in our sky",
      "Examples astronomers study:",
      table=[["Nebula", "What it is"], ["Orion Nebula", "a stellar nursery visible without a telescope"], ["Pillars of Creation (Eagle Nebula)", "columns of dust and gas with young stars forming"],
             ["Crab Nebula", "the remains of a star that exploded, seen in the year 1054"]]),
    Y("Star birth",
      mcq("s9u14r31", "What force makes a clump of gas in a nebula collapse to form a star?",
          [("gravity", True, "Yes – gravity pulls the matter together."), ("magnetism", False, "Not the main force."), ("friction", False, "Friction does not pull matter together."),
           ("upthrust", False, "Upthrust acts in fluids on Earth.")],
          "What pulls all matter together?", "Gravity pulls dust and gas together until it is dense and hot enough to shine.")),
    K("Key points",
      "A **nebula** is a cloud of dust and gas.",
      "In **stellar nurseries**, gravity pulls clumps together; they heat up and become stars.",
      "Some nebulae are the remains of dead stars."),
    book=BK(
        [("nebula", "a huge cloud of dust and gas in space"), ("stellar nursery", "a nebula where new stars form")],
        [], [],
        [Ex("What is a nebula made of?", ans="dust and gas, mostly hydrogen and helium"),
         Ex("Describe how a star forms in a nebula.", ans="Gravity pulls a clump together; it collapses and heats up until core reactions start."),
         Ex("Quick quiz.", ("Where are most asteroids?", "the asteroid belt between Mars and Jupiter"), ("Why did an asteroid impact cause mass extinction?", "dust blocked sunlight; plants and food chains failed"),
            ("One piece of evidence for the Moon's collision theory?", "Moon rocks are like Earth's"), ("What force forms stars?", "gravity")),
         Ex("How is the Crab Nebula different from the Orion Nebula?", ans="The Crab is the remains of an exploded star; Orion is where new stars are forming.", think=True)],
        ["describe nebulae", "describe how stars form"],
        look=["how stars form"],
        note="Read it after the video: nebulae and how stars are born, plus a quick quiz (answers at the back)."),
)
