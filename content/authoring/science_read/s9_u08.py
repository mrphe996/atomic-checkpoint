# -*- coding: utf-8 -*-
"""Science Stage 9 · Unit 8 Rate of Reaction – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 9 (9Cc.04, 9Cc.05, 9TWSm.01, 9TWSa.03)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}
CARD = lambda title, cards, cols=None: dict({"kind": "sciCards", "title": title, "cards": cards}, **({"cols": cols} if cols else {}))

# =====================================================================================================
# 8.1 Chemical reactions · 9Cc.05
# =====================================================================================================
READ["8.1"] = L(
    H("Fast and slow",
      "A firework explodes in a fraction of a second. Rust creeps over an old bicycle for years.",
      "Both are chemical reactions. Before asking why their speeds differ, recall what all reactions have in common."),
    I("Physical and chemical changes",
      "In a **physical change** (melting, dissolving) no new substance forms and the change can usually be reversed. In a **chemical change** (burning, rusting, cooking) atoms rearrange to make **new substances**."),
    I("Mass is conserved",
      "In a reaction atoms are **rearranged**, never created or destroyed: 2H₂ + O₂ → 2H₂O has 4 H and 2 O atoms on both sides. So the **total mass stays the same**.",
      then=["Burnt wood only seems lighter because gases (carbon dioxide and water vapour) escape into the air. In a sealed container the mass would not change."]),
    I("Energy is conserved",
      "Energy is not created or destroyed in a reaction – it is **transferred**.",
      table=[["Reaction", "Energy transfer"], ["burning charcoal", "chemical store → heat and light to the surroundings (exothermic)"],
             ["photosynthesis", "light from the Sun → chemical store in glucose (endothermic)"], ["respiration", "chemical store in glucose → energy for cells"]]),
    Y("Conservation",
      mcq("s9u08r11", "A candle burns on a balance in the open air. The reading falls. Why?",
          [("Gases made by burning escape into the air.", True, "Yes – mass is conserved, but the products leave."), ("Atoms are destroyed in the flame.", False, "Atoms are never destroyed."),
           ("Energy has mass that disappears.", False, "Not the reason here."), ("The balance is broken.", False, "The balance is fine.")],
          "Where do the products go?", "Carbon dioxide and water vapour escape.")),
    K("Key points",
      "Chemical changes make new substances by rearranging atoms.",
      "**Mass is conserved**: atoms are not created or destroyed.",
      "**Energy is conserved**: it is transferred (e.g. chemical → heat and light)."),
    book=BK(
        [("conservation of mass", "the total mass is the same before and after a reaction"), ("conservation of energy", "energy is transferred, never created or destroyed")],
        [], [],
        [Ex("Explain why mass is conserved in a chemical reaction.", ans="Atoms are only rearranged; none are created or destroyed."),
         Ex("Describe the energy transfers when charcoal burns on a barbecue.", ans="chemical energy in the charcoal → thermal energy (heat) and light"),
         Ex("Iron wool is heated in air and gets heavier. Explain.", ans="Oxygen from the air combines with the iron, adding mass.", think=True)],
        ["explain why mass and energy are conserved in reactions"],
        look=["counting atoms", "energy transfers"],
        note="Read it after the video: conservation of mass and energy (answers at the back)."),
)

# =====================================================================================================
# 8.2 What is rate of reaction? · 9Cc.04, 9TWSm.01
# =====================================================================================================
READ["8.2"] = L(
    H("How fast?",
      "A race result tells you how far someone ran in a certain time. How could you describe 'how fast' a chemical reaction goes?",
      "Think of something you could measure every few seconds."),
    I("Measuring the rate of reaction",
      "The **rate of reaction** is how quickly reactants are used up or products are made.",
      table=[["Method", "What you measure"], ["collect gas in a **gas syringe**", "volume of gas every 30 s"], ["measure **mass lost** on a balance", "mass every 30 s as gas escapes"],
             ["time how long until a cross disappears", "time for a cloudy precipitate to form"]],
      fig={"kind": "gassyringe"},
      then=["Average rate = amount of product ÷ time, e.g. cm³ of gas per second."]),
    I("Class data: carbon dioxide in a gas syringe",
      "Marble chips react with dilute hydrochloric acid; the gas volume is read every 30 s.",
      fig={"kind": "linegraph", "x": {"min": 0, "max": 180, "step": 30, "label": "time (s)"}, "y": {"min": 0, "max": 70, "step": 10, "label": "volume of CO₂ (cm³)"},
           "series": [{"pts": [[0, 0], [30, 27], [60, 44], [90, 54], [120, 59], [150, 61], [180, 61]]}]},
      then=["The steepest part (the start) is the fastest. The curve gets less steep and is flat after about 150 s – the reaction has stopped because a reactant has been used up.",
            "Average rate in the first 30 s: 27 ÷ 30 = **0.9 cm³/s**."]),
    Y("Average rate",
      num("s9u08r21", "Use the graph. What was the average rate from 30 s to 60 s, in cm³ per second? (Give your answer to 2 decimal places.)", 0.57,
          "Gas made in that interval ÷ 30 s.", "44 − 27 = 17 cm³; 17 ÷ 30 ≈ 0.57 cm³/s.", errs=[(1.47, "Use only the gas made between 30 s and 60 s.")], tol=0.01)),
    I("Collision theory",
      "Reactions happen when particles **collide**. Only **effective** collisions make products: the particles must hit with enough energy and the right way round.",
      then=["The minimum energy needed for a reaction is the **activation energy**.",
            "At the start there are many reactant particles, so many collisions – the reaction is fast. As reactants are used up there are fewer collisions, so it slows, and stops when one reactant runs out."]),
    K("Key points",
      "**Rate** = how fast reactants are used or products made; measure gas volume, mass lost or time.",
      "On a rate graph the steepest part is fastest; flat means the reaction has stopped.",
      "**Collision theory**: particles must collide with at least the **activation energy**.",
      "Reactions slow down as reactants are used up."),
    book=BK(
        [("rate of reaction", "how quickly a reaction happens"), ("collision theory", "particles must collide with enough energy to react"),
         ("activation energy", "the minimum energy particles need to react"), ("gas syringe", "apparatus to collect and measure a volume of gas")],
        [], [],
        [Ex("Give two ways to measure the rate of a reaction that makes a gas.", ans="collect gas in a gas syringe; measure the mass lost on a balance"),
         Ex("Use the graph: what total volume of gas was made? When did the reaction stop?", ans="61 cm³; at about 150 s"),
         Ex("What is activation energy?", ans="the minimum energy colliding particles need to react"),
         Ex("Explain why the graph gets less steep over time.", ans="Reactants are used up, so there are fewer collisions per second and the reaction slows.", think=True)],
        ["describe ways to measure rate of reaction", "interpret rate graphs", "explain reactions with collision theory and activation energy"],
        look=["the gas syringe graph", "collision theory"],
        note="Read it after the video: measuring rate, rate graphs and collision theory (answers at the back)."),
)

# =====================================================================================================
# 8.3 What factors affect the rate of reaction? · 9Cc.04, 9TWSa.03
# =====================================================================================================
READ["8.3"] = L(
    H("Powder danger",
      "A lump of coal burns slowly in a fire, but fine coal dust in a mine can explode.",
      "Both are coal. Why is the dust so much more dangerous?"),
    I("Predict, watch, explain: whole or crushed tablet?",
      "A whole effervescent tablet and a crushed one are dropped into equal volumes of water at the same temperature. The crushed tablet fizzes more strongly and stops after **24 s**; the whole tablet takes **62 s**.",
      then=["Crushing gives a much larger **surface area**, so more particles are exposed and there are more collisions each second. Both make the same amount of gas in the end – they have the same mass."]),
    I("What speeds up a reaction?",
      "Three factors increase the rate, each explained by collision theory.",
      table=[["Factor", "Change", "Why it is faster"], ["**temperature**", "higher", "particles move faster: more frequent and more energetic collisions, so more effective collisions"],
             ["**concentration**", "higher", "more reactant particles in the same volume, so more collisions"], ["**surface area**", "larger (powder instead of lumps)", "more particles exposed to collide"]],
      then=["(A **catalyst** also speeds up reactions without being used up – for example in car exhausts.)"]),
    I("Reading rate graphs",
      "Two runs of the same reaction:",
      fig={"kind": "linegraph", "x": {"min": 0, "max": 120, "step": 20, "label": "time (s)"}, "y": {"min": 0, "max": 60, "step": 10, "label": "volume of gas (cm³)"},
           "series": [{"pts": [[0, 0], [20, 36], [40, 50], [60, 55], [80, 56], [120, 56]], "label": "A: powder"}, {"pts": [[0, 0], [20, 16], [40, 29], [60, 39], [80, 46], [100, 52], [120, 55]], "label": "B: lumps"}]},
      then=["Line A is steeper at the start and levels off sooner – a faster reaction. Both end at about the same height, because the same amounts of reactants give the same amount of product."]),
    I("Class data: fizzing time and temperature",
      "Whole tablets in water at different temperatures:",
      fig={"kind": "barchart", "labels": ["10 °C", "20 °C", "40 °C", "60 °C"], "values": [95, 62, 32, 18], "ymax": 100, "step": 20, "ylabel": "time to stop fizzing (s)", "xlabel": "water temperature"},
      then=["The hotter the water, the shorter the time – the faster the reaction. If one result had not fitted the pattern (an **anomalous result**), it should be checked by repeating that measurement."]),
    Y("Which is fastest?",
      mcq("s9u08r31", "Which conditions give the fastest reaction between magnesium and acid?",
          [("magnesium powder in concentrated, hot acid", True, "Yes – large surface area, high concentration, high temperature."), ("a magnesium ribbon in dilute, cold acid", False, "All three factors are low."),
           ("magnesium powder in dilute, cold acid", False, "Only the surface area is high."), ("a ribbon in concentrated, cold acid", False, "Temperature and surface area are low.")],
          "Temperature, concentration, surface area.", "All three factors high → fastest.")),
    K("Key points",
      "Rate increases with higher **temperature**, higher **concentration** and larger **surface area** (and catalysts).",
      "Collision theory explains each: more frequent and/or more energetic collisions.",
      "Faster reactions give steeper graphs, but the same final amount of product.",
      "Check anomalous results by repeating."),
    book=BK(
        [("concentration", "how much substance is dissolved in a given volume"), ("surface area", "the area of a solid exposed to other reactants"),
         ("catalyst", "speeds up a reaction without being used up"), ("anomalous result", "a result that does not fit the pattern")],
        [], [],
        [Ex("Use collision theory to explain why raising the temperature speeds up a reaction.", ans="Particles move faster, so they collide more often and with more energy; more collisions exceed the activation energy."),
         Ex("Why does powder react faster than lumps of the same mass?", ans="Powder has a larger surface area, so more particles are exposed to collisions."),
         Ex("In the graph, why do lines A and B end at the same volume?", ans="The same amounts of reactants were used, so the same amount of gas is made."),
         Ex("Quick quiz.", ("Why is mass conserved?", "atoms are only rearranged"), ("What is activation energy?", "the minimum energy needed for a reaction"),
            ("Three factors that increase rate?", "higher temperature, higher concentration, larger surface area"), ("Why does a reaction slow over time?", "reactants are used up, so fewer collisions")),
         Ex("Back to 'Start here': explain why coal dust can explode.", ans="It has an enormous surface area, so it reacts with oxygen extremely fast, releasing a lot of energy and gas at once.", think=True)],
        ["explain how temperature, concentration and surface area affect rate", "read rate graphs", "identify anomalous results"],
        look=["the factors table", "graph lines A and B"],
        note="Read it after the video: factors affecting rate and reading rate graphs, plus a quick quiz (answers at the back)."),
)
