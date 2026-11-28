# -*- coding: utf-8 -*-
"""Science Stage 9 · Unit 9 Density – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 9 (9Cp.02, 9Cp.03, 9Pf.01, 9TWSm.02)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}
CARD = lambda title, cards, cols=None: dict({"kind": "sciCards", "title": title, "cards": cards}, **({"cols": cols} if cols else {}))

# =====================================================================================================
# 9.1 What is density? · 9Cp.03, 9TWSm.02
# =====================================================================================================
READ["9.1"] = L(
    H("Heavier than it looks",
      "Two identical shoeboxes: one full of feathers, one full of sand. Same size – but you can lift only one with a finger.",
      "What word describes the difference between feathers and sand?"),
    I("Measuring volume and mass",
      "To find density we need **mass** and **volume**.",
      table=[["Object", "How to find the volume"], ["regular solid (cuboid)", "length × width × height"], ["irregular solid", "**displacement**: the rise in water level in a measuring cylinder"],
             ["liquid", "read a measuring cylinder at the bottom of the meniscus"]],
      fig={"kind": "displacement", "before": 45, "after": 57, "max": 60},
      then=["Mass is measured on a balance. For a liquid: weigh the empty container, then the container with liquid, and subtract."]),
    I("What is density?",
      "**Density** is the mass in each unit of volume – how tightly matter is packed.",
      table=[["", ""], ["**density = mass ÷ volume**", "ρ = m ÷ V"], ["mass = density × volume", "volume = mass ÷ density"]],
      then=["Units: **g/cm³** (or kg/m³). A stone has a higher density than feathers: more mass is packed into the same volume."]),
    W("Calculating density",
      "A key displaces 12 cm³ of water and has a mass of 102 g. What is its density?",
      [("density = mass ÷ volume", "write the equation"), ("= 102 ÷ 12", "mass in g, volume in cm³"), ("= 8.5", "calculate")], "8.5 g/cm³ (likely brass)"),
    Y("Density",
      num("s9u09r11", "A block has a mass of 540 g and a volume of 200 cm³. What is its density in g/cm³?", 2.7, "density = mass ÷ volume.", "540 ÷ 200 = 2.7 g/cm³ (aluminium).",
          errs=[(108000, "Divide mass by volume.")])),
    I("Class data: aluminium blocks",
      "Mass and volume of four aluminium blocks of different sizes:",
      fig={"kind": "linegraph", "x": {"min": 0, "max": 40, "step": 10, "label": "volume (cm³)"}, "y": {"min": 0, "max": 120, "step": 20, "label": "mass (g)"},
           "series": [{"pts": [[0, 0], [10, 27], [20, 54], [30, 81], [40, 108]]}]},
      then=["A straight line through the origin: doubling the volume doubles the mass. The **gradient** (mass ÷ volume) is the density – 2.7 g/cm³ for every block. Density does not depend on the size of the piece.",
            "Good measurements are **accurate** (close to the true value) and **precise** (consistent when repeated). Industries use density to identify substances and check purity."]),
    K("Key points",
      "Volume: formula for regular solids, **displacement** for irregular solids, measuring cylinder for liquids.",
      "**Density = mass ÷ volume** (g/cm³).",
      "Density is the same for any sample of a pure substance, whatever its size."),
    book=BK(
        [("density", "mass per unit volume"), ("displacement method", "finding volume from the water an object pushes aside"), ("g/cm³", "grams per cubic centimetre, a unit of density")],
        [], [],
        [Ex("Calculate the density: (a) 79 g, 10 cm³ (b) 30 g, 40 cm³.", ans="(a) 7.9 g/cm³ (b) 0.75 g/cm³"),
         Ex("Gold has a density of 19.3 g/cm³. What is the mass of 5 cm³ of gold?", ans="19.3 × 5 = 96.5 g"),
         Ex("A stone raises the water in a cylinder from 40 cm³ to 55 cm³. Its mass is 39 g. Find its density.", ans="volume 15 cm³; 39 ÷ 15 = 2.6 g/cm³"),
         Ex("Two cubes of the same metal, one twice as big as the other, are compared. Explain why they have the same density.", ans="The big one has twice the mass and twice the volume, so mass ÷ volume is the same.", think=True)],
        ["measure volume and mass", "calculate density", "explain why density does not depend on size"],
        look=["density = mass ÷ volume", "the aluminium graph"],
        note="Read it after the video: measuring volume and mass and calculating density (answers at the back)."),
)

# =====================================================================================================
# 9.2 Densities of solids, liquids and gases · 9Cp.02
# =====================================================================================================
READ["9.2"] = L(
    H("Floating rock",
      "Pumice is a rock that floats on water. Granite is a rock that sinks like a stone.",
      "How can two rocks be so different?"),
    I("Solids, liquids and gases",
      "The particle model explains why density depends on the state.",
      fig={"kind": "particles"},
      then=["**Solids** usually have the highest density – particles are tightly packed. **Liquids** are a little less dense. **Gases** have very low density – particles are far apart.",
            "Water vapour is about 1600 times less dense than liquid water.",
            "Pumice is full of air bubbles trapped when lava cooled, so overall it is much less dense than granite. Metals are generally denser than non-metals."]),
    I("Temperature changes density",
      "When a substance is heated, its particles move faster and spread out: it **expands**, so its **density decreases**.",
      then=["Hot air is less dense than cold air, so it **rises** – that is how hot-air balloons fly and how sea breezes form. Cold, dense air sinks."]),
    I("Data: densities of common materials",
      "Typical densities at room temperature:",
      fig={"kind": "barchart", "labels": ["cork", "ice", "water", "aluminium", "iron", "lead"], "values": [0.24, 0.92, 1.0, 2.7, 7.9, 11.3], "ymax": 12, "step": 2,
           "ylabel": "density (g/cm³)", "xlabel": "material"},
      then=["Anything less dense than water (1 g/cm³) floats; anything denser sinks: cork and ice float; aluminium, iron and lead sink."]),
    Y("Float or sink?",
      grid("s9u09r21", "Will each material float or sink in water?", ["Floats", "Sinks"],
           [("cork (0.24 g/cm³)", "Floats"), ("iron (7.9 g/cm³)", "Sinks"), ("ice (0.92 g/cm³)", "Floats"), ("glass (2.5 g/cm³)", "Sinks"), ("oak (0.75 g/cm³)", "Floats")],
           "Compare with water: 1 g/cm³.", "Less than 1 g/cm³ floats; more sinks.")),
    K("Key points",
      "Solids are usually densest, gases least dense – because of how closely particles are packed.",
      "Heating makes a substance expand, so its density falls; hot air rises.",
      "Materials less dense than water (1 g/cm³) float; denser ones sink."),
    book=BK(
        [("expand", "get bigger as particles spread out"), ("pumice", "a rock full of air bubbles, less dense than water")],
        [], [],
        [Ex("Use the particle model to explain why gases have a much lower density than solids.", ans="Gas particles are far apart, so there is much less mass in each cm³."),
         Ex("Explain how a hot-air balloon rises.", ans="Heating the air inside makes it expand and become less dense than the surrounding air, so the balloon rises."),
         Ex("Use the chart: which materials would float in water?", ans="cork and ice"),
         Ex("Why might a metal cube sink but a metal ship float?", ans="The ship contains a lot of air, so its overall density is less than water's.", think=True)],
        ["explain density differences between solids, liquids and gases", "explain how temperature changes density"],
        look=["the particle diagrams", "the density chart"],
        note="Read it after the video: density of solids, liquids and gases and temperature (answers at the back)."),
)

# =====================================================================================================
# 9.3 Why objects float or sink · 9Pf.01
# =====================================================================================================
READ["9.3"] = L(
    H("The floating egg",
      "A fresh egg sinks in a glass of tap water. Stir in lots of salt and the same egg floats.",
      "The egg has not changed. What has?"),
    I("Predict, watch, explain: an egg in fresh and salty water",
      "A fresh egg has a density a little more than 1 g/cm³, so it sinks in tap water (1 g/cm³). Dissolving salt makes the water **denser** than the egg, so it floats.",
      then=["An object **floats** if it is **less dense** than the fluid around it, and **sinks** if it is **denser**."]),
    I("Forces on floating objects",
      "Water pushes up on anything in it with an **upthrust**. An object floats when the upthrust balances its weight before it is completely under water – which happens when it is less dense than the water.",
      fig={"kind": "sciForce", "obj": "floating log", "shape": "box", "forces": [{"dir": "up", "t": "upthrust", "n": 3}, {"dir": "down", "t": "weight", "n": 3}]}),
    I("Layers of liquids",
      "Pour honey, water and oil into a jar: they settle in layers by density, the densest at the bottom.",
      table=[["Layer (top to bottom)", "Density (g/cm³)"], ["cooking oil", "0.92"], ["water", "1.00"], ["honey", "1.4"]],
      then=["A cork floats on the oil, ice floats in the water layer, a glass marble sinks to the bottom. Helium balloons rise in air for the same reason – helium is less dense than air."]),
    I("Why ice floats",
      "Most substances are denser as solids, but water is unusual. When it freezes, its molecules form an **open crystal structure** that takes up more space, so **ice is less dense than liquid water**.",
      then=["That is why icebergs float (with about 90% below the surface) and why ponds freeze from the top, letting fish survive underneath. It is also easier to float in the sea: salty water is denser."]),
    Y("Float or sink?",
      num("s9u09r31", "An object has a mass of 180 g and a volume of 240 cm³. What is its density in g/cm³?", 0.75, "density = mass ÷ volume.",
          "180 ÷ 240 = 0.75 g/cm³ – less than water, so it floats.")),
    Y("Layers",
      mcq("s9u09r32", "Liquid A (1.3 g/cm³), liquid B (0.8 g/cm³) and water are poured into a jar. Which order do they settle in, from top to bottom?",
          [("B, water, A", True, "Yes – least dense on top."), ("A, water, B", False, "That is densest on top."), ("water, A, B", False, "Water is in the middle."), ("they mix completely", False, "Liquids that do not mix form layers by density.")],
          "Least dense floats on top.", "0.8 (B) on top, 1.0 (water), 1.3 (A) at the bottom.")),
    K("Key points",
      "An object **floats** if it is less dense than the fluid; **sinks** if it is denser.",
      "Upthrust from the fluid balances the weight of a floating object.",
      "Liquids form layers by density.",
      "Ice is less dense than water because of its open crystal structure; salty water is denser than fresh water."),
    book=BK(
        [("upthrust", "the upward force of a fluid on an object in it"), ("fluid", "a liquid or a gas")],
        [], [],
        [Ex("Will a 50 cm³ block of mass 65 g float in water? Explain.", ans="density 1.3 g/cm³ – denser than water, so it sinks"),
         Ex("Explain why an egg that sinks in tap water floats in very salty water.", ans="Salt makes the water denser than the egg."),
         Ex("Why does ice float on water?", ans="Its open crystal structure makes it less dense than liquid water."),
         Ex("Quick quiz.", ("Formula for density?", "density = mass ÷ volume"), ("180 g, 240 cm³: float or sink in water?", "float (0.75 g/cm³)"),
            ("Why does hot air rise?", "it is less dense"), ("Which state usually has the lowest density?", "gas")),
         Ex("Why is it easier to float in the Dead Sea than in a swimming pool?", ans="The Dead Sea is very salty, so the water is much denser and gives more upthrust.", think=True)],
        ["use density to explain floating and sinking", "explain why liquids form layers", "explain why ice floats"],
        look=["the egg experiment", "layers of liquids"],
        note="Read it after the video: floating, sinking and density, plus a quick quiz (answers at the back)."),
)
