# -*- coding: utf-8 -*-
"""Science Stage 8 · Unit 11 Magnetism – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 8 (8Pe.01–8Pe.03, 8ESp.01, 8SIC.02, 8TWSp.04)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}
CARD = lambda title, cards, cols=None: dict({"kind": "sciCards", "title": title, "cards": cards}, **({"cols": cols} if cols else {}))

# =====================================================================================================
# 11.1 Magnetic fields · 8Pe.01, 8ESp.01
# =====================================================================================================
READ["11.1"] = L(
    H("A train that floats",
      "Some high-speed trains do not touch their rails at all: magnets lift them and push them along at over 400 km/h.",
      "What do you already know about how magnets push and pull?"),
    I("Magnets and magnetic materials",
      "Every magnet has a **North pole** and a **South pole**. **Unlike poles attract; like poles repel.**",
      table=[["Kind of magnet", "Description"], ["**permanent**", "keeps its magnetism (heating, hammering or dropping it can weaken it)"],
             ["**temporary**", "soft iron becomes magnetic only while near a magnet"], ["**electromagnet**", "magnetic only when a current flows – can be switched on and off"]],
      then=["**Magnetic materials** are attracted to magnets: **iron, nickel, cobalt** and **steel** (mostly iron)."]),
    I("Predict, watch, explain: what does a magnet attract?",
      "A strong magnet is lowered over an iron nail, a steel paper clip, a copper coin, an aluminium can and a plastic spoon. Only the nail and the paper clip jump up.",
      then=["Copper and aluminium are metals but are **not magnetic**. 'All metals are magnetic' is a common mistake – recycling centres use this to separate steel cans from aluminium cans."]),
    Y("Magnetic or not?",
      grid("s8u11r11", "Is each material attracted to a magnet?", ["Magnetic", "Not magnetic"],
           [("iron", "Magnetic"), ("copper", "Not magnetic"), ("nickel", "Magnetic"), ("aluminium", "Not magnetic"), ("steel", "Magnetic"), ("gold", "Not magnetic")],
           "Only four common magnetic materials.", "Iron, nickel and steel (and cobalt) are magnetic; copper, aluminium and gold are not.")),
    I("Magnetic fields",
      "Around a magnet is a region where its force acts: the **magnetic field**. Iron filings sprinkled round a magnet line up along the **field lines**.",
      fig={"kind": "sciField"},
      then=["Field lines go from **N to S**. They are closest together at the poles, where the field is **strongest**; the field gets weaker further away. A small **plotting compass** points along the field lines."]),
    I("Fields interact",
      "When two magnets come close, their fields interact.",
      fig={"kind": "sciField", "pair": "attract"},
      then=["Unlike poles: the field lines join up and the magnets attract. Like poles: the lines push apart, with a **neutral point** between them, and the magnets repel."]),
    I("The Earth is a magnet",
      "Molten iron moving in the Earth's outer core makes the Earth behave like a giant bar magnet. A compass needle lines up with Earth's magnetic field and points north.",
      then=["The Earth's magnetic field also shields us from harmful charged particles from the Sun. You will learn more about it in Unit 14."]),
    Y("Like poles",
      mcq("s8u11r12", "What happens when the North pole of one magnet is brought near the North pole of another?",
          [("They repel.", True, "Yes – like poles repel."), ("They attract.", False, "Unlike poles attract."), ("Nothing happens.", False, "Magnets always affect each other nearby."),
           ("They swap poles.", False, "Poles do not swap.")],
          "Like or unlike?", "North–North are like poles, so they repel.")),
    K("Key points",
      "Unlike poles attract; like poles repel. Magnetic materials: iron, nickel, cobalt, steel.",
      "Permanent, temporary and electromagnets.",
      "A **magnetic field** surrounds a magnet; field lines go N → S and are strongest at the poles.",
      "Fields interact; the Earth has a magnetic field that a compass follows."),
    book=BK(
        [("magnetic material", "a material attracted to a magnet: iron, nickel, cobalt, steel"), ("magnetic field", "the region round a magnet where its force acts"),
         ("field lines", "lines showing the shape and direction of a magnetic field"), ("permanent magnet", "keeps its magnetism"), ("temporary magnet", "magnetic only near another magnet")],
        [], [],
        [Ex("Name three magnetic materials and two non-magnetic metals.", ans="iron, nickel, cobalt (steel); copper, aluminium (gold, silver)"),
         Ex("Draw the field lines round a bar magnet, with arrows.", ans="loops from N round to S, closest at the poles, arrows from N to S"),
         Ex("How could you find where a magnet's field is strongest?", ans="Use iron filings (lines closest together) or see where it picks up the most paper clips."),
         Ex("A student says 'a magnet will pick up a 10p coin because coins are metal.' Is she right? Explain.", ans="Not necessarily – only magnetic metals (iron, nickel, cobalt, steel) are attracted; many coins are copper alloys.", think=True)],
        ["describe magnets and magnetic materials", "draw and describe magnetic fields", "explain how fields interact and that the Earth has a magnetic field"],
        look=["the field round a bar magnet", "attracting magnets"],
        note="Read it after the video: magnets, magnetic materials and magnetic fields (answers at the back)."),
)

# =====================================================================================================
# 11.2 Electromagnets · 8Pe.02, 8Pe.03, 8TWSp.04
# =====================================================================================================
READ["11.2"] = L(
    H("A magnet with a switch",
      "A scrapyard crane lifts a crushed car, swings it over a lorry – and lets it drop. A permanent magnet could never let go.",
      "How could you make a magnet you can switch off?"),
    I("Electromagnets",
      "A current flowing in a wire makes a magnetic field around it. Coil the wire and the fields add together; put an **iron core** inside and the field becomes much stronger.",
      fig={"kind": "electromagnet", "turns": 10, "cells": 1, "clips": 4},
      then=["Close the switch: current flows, the coil and core become magnetic and pick up paper clips. Open the switch: the magnetism disappears and the clips drop.",
            "Do not leave the current on for long – the wire gets hot."]),
    I("Making an electromagnet stronger",
      "Three ways to increase the strength:",
      fig=CARD("Stronger electromagnet", [{"t": "More turns", "d": "each turn adds to the field"}, {"t": "More current", "d": "e.g. more cells"}, {"t": "An iron core", "d": "concentrates the field lines"}], 3),
      then=["To test one factor fairly, change only that one and keep the others the same."]),
    I("Real data: turns and paper clips",
      "A class used the same cell each time and counted the paper clips picked up.",
      fig={"kind": "linegraph", "x": {"min": 0, "max": 50, "step": 10, "label": "number of turns"}, "y": {"min": 0, "max": 16, "step": 4, "label": "paper clips picked up"},
           "series": [{"pts": [[10, 3], [20, 6], [30, 9], [40, 12], [50, 15]]}]},
      then=["The points lie on a straight line: every 10 extra turns picks up 3 more clips. **Independent variable**: number of turns; **dependent**: clips picked up; **control**: current, core, size of clips."]),
    Y("Predict",
      num("s8u11r21", "Using the pattern, how many paper clips would you expect with 70 turns?", 21, "3 clips for every 10 turns.", "70 ÷ 10 × 3 = 21 clips.")),
    Y("Stronger?",
      mcq("s8u11r22", "Which change would NOT make an electromagnet stronger?",
          [("Using a plastic core instead of iron.", True, "Right – a plastic core does not concentrate the field."), ("Adding more turns.", False, "More turns make it stronger."),
           ("Increasing the current.", False, "More current makes it stronger."), ("Using an iron core.", False, "An iron core makes it stronger.")],
          "Three things make it stronger.", "More turns, more current and an iron core increase the strength; plastic does not.")),
    K("Key points",
      "An **electromagnet** is a coil of wire, often round an iron core, that is magnetic only when current flows.",
      "Stronger with **more turns**, **more current** and an **iron core**.",
      "In tests, change one variable at a time."),
    book=BK(
        [("electromagnet", "a coil of wire that becomes a magnet when current flows"), ("core", "the iron rod inside a coil"), ("coil", "wire wound into loops")],
        [], [],
        [Ex("Describe how to make an electromagnet.", ans="Wind insulated wire many times round an iron nail and connect the ends to a cell and switch."),
         Ex("Give three ways to make an electromagnet stronger.", ans="more turns, more current, iron core"),
         Ex("Plan a fair test of how current affects strength.", ans="Change the number of cells (current); keep turns and core the same; count paper clips picked up; repeat."),
         Ex("Why do scrapyards use electromagnets rather than permanent magnets?", ans="They can be switched off to drop the metal.", think=True)],
        ["describe how to make an electromagnet", "investigate factors that change its strength"],
        look=["the electromagnet diagram", "the turns and clips graph"],
        note="Read it after the video: making electromagnets and changing their strength (answers at the back)."),
)

# =====================================================================================================
# 11.3 Uses of electromagnets · 8Pe.02, 8SIC.02
# =====================================================================================================
READ["11.3"] = L(
    H("Hidden magnets",
      "There may be more than twenty electromagnets in your home right now – most of them hidden inside machines.",
      "Guess three devices that might contain one."),
    I("Electromagnets at work",
      "Electromagnets are useful because they can be **switched on and off** and their **strength can be controlled**.",
      table=[["Place", "Use"], ["scrapyards", "cranes lift scrap iron and steel, then drop it"], ["recycling plants", "pull steel cans out of mixed waste, leaving aluminium behind"],
             ["power stations", "generators use spinning electromagnets to produce electricity"], ["hospitals", "MRI scanners use very strong electromagnets to make pictures inside the body"],
             ["maglev trains", "electromagnets lift and drive the train with no friction from rails"]]),
    I("Real life: electromagnets around us",
      "Four everyday examples:",
      fig=CARD("Electromagnets at home", [{"icon": "megaphone", "t": "Doorbell", "d": "pulls a striker onto the bell"}, {"icon": "nolabel", "t": "Security doors", "d": "held shut until the current is switched off"},
                                          {"icon": "ear", "t": "Speakers", "d": "a changing current moves a cone to make sound"}, {"icon": "factory", "t": "Recycling", "d": "lifts steel out of rubbish"}], 4)),
    I("How an MRI scanner works",
      "A huge electromagnet lines up hydrogen atoms in the water in your body. Radio waves knock them out of line; as they flip back they give out signals.",
      then=["A computer turns the signals into detailed pictures of soft tissues such as the brain – without X-rays. Patients must remove metal objects because the magnet is so strong."]),
    Y("Why an electromagnet?",
      mcq("s8u11r31", "Why are electromagnets used in security doors?",
          [("The door can be unlocked by switching the current off.", True, "Yes – the lock releases when the current stops."), ("They are lighter than keys.", False, "That is not the main reason."),
           ("They attract aluminium doors.", False, "Aluminium is not magnetic."), ("They never need electricity.", False, "They need a current to work.")],
          "What can an electromagnet do that a permanent magnet cannot?", "It can be switched on and off.")),
    K("Key points",
      "Electromagnets can be switched on and off and their strength controlled.",
      "Uses: scrapyard cranes, recycling, generators, MRI scanners, maglev trains, doorbells, security doors, speakers."),
    book=BK(
        [("MRI scanner", "a hospital machine that uses a strong magnet and radio waves to image the body"), ("generator", "a machine that produces electricity using magnets and coils")],
        [], [],
        [Ex("Give three uses of electromagnets and the reason an electromagnet is chosen for each.", ans="e.g. scrapyard crane – can drop the load; doorbell – works only when pressed; recycling – separates steel from aluminium"),
         Ex("Explain how an electromagnet separates steel and aluminium cans.", ans="Steel is magnetic and is lifted out; aluminium is not magnetic and is left behind."),
         Ex("Quick quiz.", ("What happens when two North poles meet?", "they repel"), ("Name three magnetic materials.", "iron, nickel, cobalt (steel)"),
            ("Give two ways to make an electromagnet stronger.", "more turns, more current, iron core"), ("Why use electromagnets in scrapyards?", "they can be switched off to drop the metal")),
         Ex("Why must patients remove watches and keys before an MRI scan?", ans="The very strong magnet would pull on magnetic metal objects, which could be dangerous.", think=True)],
        ["describe uses of electromagnets in homes, industry and medicine", "explain why electromagnets are chosen for each use"],
        look=["the uses table", "electromagnets at home"],
        note="Read it after the video: uses of electromagnets, plus a quick quiz (answers at the back)."),
)
