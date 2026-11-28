# -*- coding: utf-8 -*-
"""Science Stage 8 · Unit 7 Exothermic and Endothermic Changes – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 8 (8Cc.01, 8Cc.02, 8Cc.04, 8TWSc.04)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}
CARD = lambda title, cards, cols=None: dict({"kind": "sciCards", "title": title, "cards": cards}, **({"cols": cols} if cols else {}))

# =====================================================================================================
# 7.1 Exothermic changes · 8Cc.01, 8Cc.02, 8Cc.04
# =====================================================================================================
READ["7.1"] = L(
    H("Heat in a packet",
      "Click the metal disc in a reusable hand warmer and the clear liquid turns solid – and the packet becomes warm in seconds.",
      "Where does the heat come from? Write your idea."),
    I("Exothermic reactions",
      "'Exo' means **out** and 'thermic' means **heat**. An **exothermic** change **releases energy** (usually heat) to the surroundings, so the **temperature rises**.",
      then=["In an exothermic reaction the products have **less** stored energy than the reactants; the difference is given out. Sometimes the energy also comes out as light, as in a sparkler.",
            "A plaster cast feels warm as it sets because plaster of Paris reacts with water exothermically."]),
    I("Predict, watch, explain: dissolving calcium chloride",
      "Water in a beaker is at **19 °C**. A spoonful of calcium chloride is stirred in. The thermometer rises to **36 °C** and the beaker feels warm.",
      fig={"kind": "thermometer", "min": 0, "max": 50, "value": 36, "major": 10, "minor": 2},
      then=["Dissolving calcium chloride **releases heat** to the water, so the temperature goes up: it is **exothermic**. Some self-heating food cans and hand warmers work this way."]),
    Y("Temperature change",
      num("s8u07r11", "The temperature went from 19 °C to 36 °C. By how many degrees did it rise?", 17, "final − starting temperature.", "36 − 19 = 17 °C.")),
    I("Types of exothermic reaction",
      "Many reactions you have met are exothermic.",
      table=[["Reaction", "Example"], ["**combustion**", "burning fuels: methane + oxygen → carbon dioxide + water"], ["**neutralisation**", "acid + alkali → salt + water"],
             ["**respiration**", "glucose + oxygen → carbon dioxide + water, in your cells"], ["reactive metals with water or acid", "sodium in water; magnesium in acid"],
             ["**hydration**", "cement or plaster setting when water is added"], ["rusting", "iron + oxygen + water – releases heat very slowly"]],
      then=["Biogas plants let microorganisms turn crop waste and manure into **methane**, which is burned as a cleaner fuel for cooking."]),
    I("Exothermic processes",
      "Physical changes can be exothermic too – no new substance forms, but heat is released.",
      table=[["Process", "Why heat is released"], ["**freezing** (liquid → solid)", "particles lose energy and lock into fixed positions"], ["**condensing** (gas → liquid)", "particles slow down and come closer together"],
             ["dissolving some substances", "calcium chloride, sodium hydroxide"], ["**crystallisation**", "the hand warmer: a supersaturated solution crystallises"]]),
    Y("Exothermic?",
      grid("s8u07r12", "Does each change release heat (exothermic)?", ["Exothermic", "Not exothermic"],
           [("burning wood", "Exothermic"), ("water freezing", "Exothermic"), ("ice melting", "Not exothermic"), ("neutralising an acid", "Exothermic"), ("water evaporating", "Not exothermic")],
           "Does it give out heat?", "Burning, freezing and neutralisation release heat; melting and evaporating take heat in.")),
    K("Key points",
      "**Exothermic** changes release heat to the surroundings: the temperature **rises**.",
      "Exothermic reactions: combustion, neutralisation, respiration, metals with water or acid, hydration, rusting.",
      "Exothermic processes: freezing, condensing, crystallisation, dissolving some substances."),
    book=BK(
        [("exothermic", "releases heat to the surroundings"), ("combustion", "burning a fuel in oxygen"), ("hydration", "a reaction with water"), ("crystallisation", "a solid forming crystals from a solution")],
        [], [],
        [Ex("How can you tell from a thermometer that a change is exothermic?", ans="The temperature of the surroundings rises."),
         Ex("Name three exothermic reactions.", ans="e.g. combustion, neutralisation, respiration"),
         Ex("Is freezing exothermic? Explain using particles.", ans="Yes – the particles lose energy as they slow down and lock into place, releasing heat."),
         Ex("Suggest why a self-heating can of soup has two compartments.", ans="The chemicals are kept apart until needed; mixing them starts an exothermic change that heats the soup.", think=True)],
        ["identify exothermic changes from a temperature rise", "give examples of exothermic reactions and processes"],
        look=["the calcium chloride results", "types of exothermic reaction"],
        note="Read it after the video: exothermic reactions and processes (answers at the back)."),
)

# =====================================================================================================
# 7.2 Endothermic changes · 8Cc.02, 8TWSc.04
# =====================================================================================================
READ["7.2"] = L(
    H("Ice without a freezer",
      "A sports first-aid kit has an 'instant cold pack'. Squeeze it, shake it, and it becomes icy cold – no freezer needed.",
      "Where does the heat go?"),
    I("Predict, watch, explain: the sherbet reaction",
      "Citric acid and baking soda are dissolved in water at 20 °C. The mixture fizzes and the thermometer **falls** to 12 °C.",
      then=["The reaction **takes in heat** from the water (and from your hand or tongue), so the temperature falls. That is why sherbet feels cool and tingly."]),
    I("Endothermic reactions",
      "'Endo' means **in**. An **endothermic** change **takes in energy** (usually heat) from the surroundings, so the **temperature falls**. The products have **more** stored energy than the reactants.",
      table=[["Reaction", "Example"], ["citric acid + baking soda", "sherbet, some cold packs"], ["**thermal decomposition**", "heating copper carbonate: copper carbonate → copper oxide + carbon dioxide"],
             ["**photosynthesis**", "plants take in light energy and store it as chemical energy in glucose"], ["cooking", "baking bread absorbs heat; reactions change its sugars and proteins"]]),
    I("Endothermic processes",
      "Some physical changes take in heat.",
      table=[["Process", "Example"], ["**melting**", "ice in a drink takes in heat – the drink cools"], ["**evaporating**", "sweat or hand sanitiser cools your skin as it evaporates"],
             ["dissolving some salts", "ammonium chloride or ammonium nitrate in cold packs"], ["boiling", "water takes in heat to turn into steam"]]),
    I("Data: final temperatures",
      "Four changes each started at 20 °C.",
      fig={"kind": "barchart", "labels": ["dissolve CaCl₂", "neutralise", "melt ice in drink", "dissolve NH₄Cl"], "values": [36, 27, 7, 11], "ymax": 40, "step": 10,
           "ylabel": "final temperature (°C)", "xlabel": "change"},
      then=["Above 20 °C → **exothermic** (dissolving calcium chloride, neutralisation). Below 20 °C → **endothermic** (melting ice, dissolving ammonium chloride)."]),
    Y("Which is endothermic?",
      mcq("s8u07r21", "Which change is endothermic?",
          [("ice melting", True, "Yes – it takes in heat."), ("water freezing", False, "Freezing releases heat."), ("wood burning", False, "Combustion releases heat."),
           ("acid neutralising an alkali", False, "Neutralisation releases heat.")],
          "Which one takes heat in?", "Melting takes in heat from the surroundings.")),
    Y("Exo or endo?",
      grid("s8u07r22", "Exothermic or endothermic?", ["Exothermic", "Endothermic"],
           [("temperature rises from 20 °C to 31 °C", "Exothermic"), ("photosynthesis", "Endothermic"), ("a cold pack feels icy", "Endothermic"), ("respiration", "Exothermic"),
            ("thermal decomposition", "Endothermic")],
           "Heat out or heat in?", "Temperature rise and respiration release heat; photosynthesis, cold packs and decomposition take heat in.")),
    K("Key points",
      "**Endothermic** changes take in heat: the temperature **falls**.",
      "Endothermic reactions: thermal decomposition, photosynthesis, citric acid + baking soda, cooking.",
      "Endothermic processes: melting, evaporating, boiling, dissolving some salts (cold packs).",
      "Compare the final and starting temperatures to decide exo or endo."),
    book=BK(
        [("endothermic", "takes in heat from the surroundings"), ("thermal decomposition", "breaking down a substance by heating it")],
        [], [],
        [Ex("How can you tell from a thermometer that a change is endothermic?", ans="The temperature falls."),
         Ex("Classify as exothermic or endothermic: (a) evaporation (b) combustion (c) photosynthesis (d) freezing.", ans="(a) endothermic (b) exothermic (c) endothermic (d) exothermic"),
         Ex("Explain why sweating cools you down.", ans="Sweat evaporates, which is endothermic – it takes heat from your skin."),
         Ex("Quick quiz.", ("A reaction makes a test tube warm. Exo or endo?", "exothermic"), ("Is freezing exothermic or endothermic?", "exothermic"),
            ("Give an endothermic reaction in plants.", "photosynthesis"), ("Which salt is used in cold packs?", "ammonium chloride (or ammonium nitrate)")),
         Ex("Plan a fair test to compare the temperature change when four different salts dissolve.", ans="Same volume and starting temperature of water, same mass of each salt, stir the same, measure the lowest or highest temperature.", think=True)],
        ["identify endothermic changes from a temperature fall", "give examples of endothermic reactions and processes", "measure and compare temperature changes"],
        look=["the sherbet reaction", "the final temperature chart"],
        note="Read it after the video: endothermic reactions and processes, plus a quick quiz (answers at the back)."),
)
