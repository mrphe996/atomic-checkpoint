# -*- coding: utf-8 -*-
"""Stage 9 Unit 9 – Density. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Physics"
BLURB = "Measuring mass and volume, calculating density, why solids, liquids and gases differ in density, and why objects float or sink."
OBJECTIVES = {
    "O1": {"sec": "9.1", "code": "9Cp.03, 9TWSm.02", "codeNote": "measuring", "t": "Measure the volume of regular and irregular objects and the mass of solids and liquids."},
    "O2": {"sec": "9.1", "code": "9Cp.03", "codeNote": "", "t": "Calculate density using density = mass ÷ volume."},
    "O3": {"sec": "9.2", "code": "9Cp.02", "codeNote": "", "t": "Explain differences in the density of solids, liquids and gases using the particle model, and how temperature changes density."},
    "O4": {"sec": "9.3", "code": "9Pf.01", "codeNote": "", "t": "Use density to explain why objects float or sink."},
}
SECTIONS = [
    {"id": "9.1", "title": "What is density?", "objs": ["O1", "O2"]},
    {"id": "9.2", "title": "Densities of solids, liquids and gases", "objs": ["O3"]},
    {"id": "9.3", "title": "Why objects float or sink", "objs": ["O4"]},
]
u = Unit(9, 9)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 9.1
u.sec("9.1", "O2")
u.tb("r", "Complete the density table.", ["Object", "Mass (g)", "Volume (cm³)", "Density (g/cm³)"], [["Metal cube", "11.3", "1", B(11.3)], ["Wooden block", "60", "100", B(0.6)], ["Stone", "75", "30", B(2.5)]])
u.tb("r", "Displacement method. Complete the table.", ["Water before (cm³)", "Water after (cm³)", "Volume of key (cm³)"], [["50", "60", B(10)]], o="O1")
u.gd("r", "Which method finds the volume?", "Method", [("A cuboid", "Length × width × height"), ("An irregular stone", "Displacement"), ("A liquid", "Measuring cylinder")], o="O1")
u.ex("r", "Describe how to find the mass of a liquid using a balance.", [("weigh empty container", ["empty"]), ("weigh container with liquid", ["with liquid|full"]), ("subtract", ["subtract|difference|minus"])],
     "Weigh the empty container, then weigh it again with the liquid in it, and subtract the first mass from the second.", o="O1")
u.mc("r", "Density =", "mass ÷ volume", ["volume ÷ mass", "mass × volume", "mass + volume"])
u.mc("r", "A box of stones is heavier than the same box of feathers because stone…", "has a higher density", ["has a bigger volume", "is softer", "has a lower density"])
u.nm("r", "A cuboid is 5 cm × 4 cm × 2 cm. What is its volume?", 40, "cm³", o="O1", d="H")
u.mc("r", "Measurements that are close to the true value are…", "accurate", ["precise", "anomalous", "repeated"], o="O1", d="VH")
mcs("p", [
    ("Density is measured in…", "g/cm³ or kg/m³", ["cm³ only", "kg only", "newtons"]),
    ("Archimedes' method uses…", "displacement of water", ["a ruler only", "a thermometer", "a magnet"], "O1"),
    ("Mass is measured with a…", "balance", ["ruler", "measuring cylinder", "thermometer"], "O1"),
    ("Volume of a cuboid =", "length × width × height", ["length + width + height", "mass ÷ density", "length × width"], "O1"),
    ("Measurements that are consistent when repeated are…", "precise", ["accurate", "anomalous", "biased"], "O1"),
    ("Industries use density to…", "identify substances and check purity", ["measure temperature", "find speed", "count atoms"]),
    ("A high density means a lot of mass in…", "a small volume", ["a large volume", "no volume", "a gas"]),
    ("Icebergs are made of…", "fresh water ice", ["salt", "rock", "glass"]),
    ("Most of an iceberg is…", "below the surface", ["above the surface", "in the air", "on land"]),
    ("1 cm³ of water has a mass of about…", "1 g", ["10 g", "0.1 g", "100 g"]),
    ("If the water rises from 30 cm³ to 45 cm³, the object's volume is…", "15 cm³", ["75 cm³", "45 cm³", "30 cm³"], "O1"),
    ("To read a measuring cylinder, your eye should be…", "level with the bottom of the meniscus", ["above the scale", "below the cylinder", "at the top of the meniscus"], "O1"),
    ("Mass = density ×", "volume", ["mass", "area", "time"]),
    ("Volume = mass ÷", "density", ["volume", "area", "speed"]),
    ("Two blocks have the same volume. The denser one has…", "more mass", ["less mass", "the same mass", "no mass"]),
])
u.mt("p", "Match the quantity to its unit.", [("Mass", "g"), ("Volume", "cm³"), ("Density", "g/cm³")])
u.od("p", "Order the steps to find the density of a stone.", ["Measure its mass on a balance", "Read the water level in a measuring cylinder", "Lower the stone in and read again", "Divide mass by volume"])
u.nm("p", "A liquid has a mass of 50 g and a volume of 40 cm³. What is its density?", 1.25, "g/cm³")
u.nm("a", "Gold has a density of 19.3 g/cm³. What is the mass of a 2 cm³ gold bar?", 38.6, "g")
u.nm("a", "Aluminium has a density of 2.7 g/cm³. What volume does 54 g of aluminium have?", 20, "cm³")
u.ex("a", "A 'gold' ring has a mass of 24 g and a volume of 2 cm³. Gold's density is 19.3 g/cm³. Is it pure gold? Explain.", [("density = 24 ÷ 2 = 12 g/cm³", ["12"]), ("lower than 19.3 – not pure gold", ["not|lower|less"])],
     "Its density is 24 ÷ 2 = 12 g/cm³, which is much lower than 19.3 g/cm³, so it is not pure gold.")
u.mc("a", "Why does the displacement method work for irregular objects?", "The object pushes aside a volume of water equal to its own volume", ["The object absorbs the water", "Water has no volume", "It measures mass"], o="O1", skill="Reasoning")
u.stop("Why do they float?", "Icebergs are made of…", "fresh water ice", ["salt", "rock", "glass"])
u.stop("the key's volume is 10 cubic centimetres", "The displacement method finds the … of an irregular object.", "volume", ["mass", "density", "temperature"], o="O1")
u.stop("more mass is packed into the same volume", "Stone is heavier than feathers in the same box because it has a higher…", "density", ["volume", "temperature", "speed"])
u.stop("has a density of 11.3 grams per cubic centimetre", "Density equals…", "mass ÷ volume", ["volume ÷ mass", "mass × volume", "mass + volume"])

# ---------------------------------------------------------------- 9.2
u.sec("9.2", "O3")
u.gd("r", "Which state is usually the densest and the least dense?", "Density", [("Solid", "Highest"), ("Liquid", "Medium"), ("Gas", "Lowest")])
u.tb("r", "Pumice and granite blocks of the same size. Complete the table.", ["Rock", "Mass (g)", "Volume (cm³)", "Density (g/cm³)"], [["Granite", "270", "100", B(2.7)], ["Pumice", "27", "100", B(0.27)]])
u.gd("r", "Does the air rise or sink?", "Movement", [("Air heated by a burner", "Rises"), ("Cold air", "Sinks")], extra=["Stays still"])
u.ex("r", "Use the particle model to explain why gases have a much lower density than solids.", [("gas particles far apart", ["far apart|spread"]), ("solid particles tightly packed", ["tight|close|packed"]), ("so much less mass in the same volume", ["less mass|same volume"])],
     "In a gas the particles are far apart, but in a solid they are tightly packed. So a gas has much less mass in the same volume, giving it a lower density.")
u.mc("r", "Why is pumice much less dense than granite?", "It is full of air holes", ["It is made of metal", "It is hotter", "It has heavier atoms"])
u.mc("r", "When air is heated, it…", "expands and becomes less dense", ["contracts and becomes denser", "gets heavier", "stops moving"])
u.mc("r", "How does a hot-air balloon rise?", "The hot air inside is less dense than the cooler air outside", ["Hot air is heavier", "The basket pushes it up", "The burner adds helium"], d="H")
u.mc("r", "Metals are generally … than non-metals.", "denser", ["less dense", "lighter for the same volume", "more gaseous"], d="VH")
mcs("p", [
    ("Liquid particles can…", "move past each other", ["only vibrate in place", "move far apart freely", "not move"]),
    ("Gas particles are…", "far apart", ["tightly packed", "touching", "in fixed rows"]),
    ("Solid particles are…", "tightly packed", ["far apart", "moving freely", "absent"]),
    ("Hot air…", "rises", ["sinks", "stays still", "freezes"]),
    ("Cold air…", "sinks", ["rises", "boils", "expands"]),
    ("Sea breezes form because…", "air over warm land rises and cooler air moves in", ["the sea is hotter than land at noon", "the Moon pulls the air", "cold air rises"]),
    ("Pumice is about … less dense than granite.", "ten times", ["twice", "a hundred times", "the same"]),
    ("Heating a substance usually makes its density…", "decrease", ["increase", "stay the same", "double"]),
    ("Which is usually the least dense?", "A gas", ["A solid", "A liquid", "A metal"]),
    ("Which has the highest density?", "Lead", ["Air", "Water", "Cork"]),
    ("Expanding means taking up…", "more space", ["less space", "no space", "less mass"]),
    ("Pumice forms from…", "lava with gas bubbles", ["sand", "seashells", "ice"]),
    ("A balloon of hot air has … mass than the same volume of cold air.", "less", ["more", "the same", "double the"]),
    ("Particles in a hot gas move…", "faster and spread out", ["slower", "closer together", "not at all"]),
    ("In a room, warm air collects…", "near the ceiling", ["near the floor", "in the middle only", "outside"]),
])
u.ms("p", "Select ALL the reasons a substance might have a low density.", ["Particles far apart", "Air holes in its structure", "It has been heated and expanded"], ["Particles tightly packed", "Made of a dense metal"])
u.mt("p", "Match the example to the explanation.", [("Hot-air balloon", "hot air less dense"), ("Pumice floats", "full of air holes"), ("Sea breeze", "warm air over land rises")])
u.od("p", "Order from most to least dense.", ["Iron", "Water", "Cooking oil", "Air"])
u.ex("a", "Explain how a convection-driven sea breeze forms on a sunny afternoon.", [("land heats faster than sea", ["land.*(heat|warm)|faster"]), ("warm air over land rises – less dense", ["rise|less dense"]), ("cooler denser air from sea moves in", ["cool|sea|moves in|replace"])],
     "The land heats up faster than the sea. Air above the land warms, expands, becomes less dense and rises. Cooler, denser air from over the sea moves in to replace it.")
u.nm("a", "1 m³ of air at 20 °C has a mass of 1.2 kg. What is its density in kg/m³?", 1.2, "kg/m³")
u.mc("a", "Why are aircraft parts often made of aluminium rather than steel?", "Aluminium is less dense, so parts are lighter for the same size", ["Aluminium is denser", "Steel floats", "Aluminium is a gas"], skill="Application")
u.mc("a", "A metal rod is heated and expands. Its mass stays the same. Its density…", "decreases", ["increases", "stays the same", "becomes zero"], skill="Reasoning")
u.stop("so gases have the lowest density", "Which is usually the densest?", "A solid", ["A gas", "A liquid", "Air"])
u.stop("Metals are generally denser than non-metals", "Pumice is less dense than granite because it has…", "air holes", ["more metal", "heavier atoms", "no particles"])
u.stop("how sea breezes form", "Heated air…", "becomes less dense and rises", ["becomes denser and sinks", "stops moving", "gets heavier"])

# ---------------------------------------------------------------- 9.3
u.sec("9.3", "O4")
u.gd("r", "Float or sink in water (density 1 g/cm³)?", "Result", [("Cork, 0.24 g/cm³", "Floats"), ("Glass marble, 2.5 g/cm³", "Sinks"), ("Ice, 0.92 g/cm³", "Floats"), ("Iron nail, 7.9 g/cm³", "Sinks")])
u.tb("r", "Will each object float in water? Complete the table.", ["Object", "Mass (g)", "Volume (cm³)", "Density (g/cm³)"], [["A", "180", "240", B(0.75)], ["B", "300", "150", B(2)]])
u.od("r", "Liquids in a jar layer by density. Order from top to bottom.", ["Oil", "Water", "Honey"])
u.ex("r", "Explain why ice floats on water.", [("water forms open crystal structure when freezing", ["open|crystal|structure"]), ("takes up more space / expands", ["more space|expand"]), ("ice less dense than water", ["less dense"])],
     "When water freezes, its molecules form an open crystal structure that takes up more space. So ice is less dense than liquid water and floats.")
u.mc("r", "An object floats if it is…", "less dense than the fluid", ["denser than the fluid", "heavier than 1 kg", "made of metal"])
u.mc("r", "The density of water is…", "1 g/cm³", ["10 g/cm³", "0.1 g/cm³", "100 g/cm³"])
u.mc("r", "Why is it easier to float in the sea than in a swimming pool?", "Salty water is denser", ["Sea water is warmer", "Pools have waves", "Salt makes you lighter"], d="H")
u.mc("r", "Why do helium balloons rise?", "Helium is less dense than air", ["Helium is denser than air", "Balloons are magnetic", "Air pushes balloons down"], d="VH")
mcs("p", [
    ("A stone sinks in a pond because it is…", "denser than water", ["less dense than water", "too small", "dry"]),
    ("Wood floats because it is…", "less dense than water", ["denser than water", "heavier", "hollow always"]),
    ("The upward force from a fluid is called…", "upthrust", ["weight", "friction", "gravity"]),
    ("In a jar of honey, water and oil, the densest liquid is at the…", "bottom", ["top", "middle", "outside"]),
    ("Cork floats on top of…", "all three liquids", ["oil only", "nothing", "honey only"]),
    ("A glass marble in a jar of liquids sinks to the…", "bottom", ["top", "middle", "surface"]),
    ("Icebergs float because ice is…", "less dense than sea water", ["denser than water", "hollow", "made of salt"]),
    ("A substance denser than the fluid…", "sinks", ["floats", "rises", "evaporates"]),
    ("An object of density 0.5 g/cm³ in water will…", "float", ["sink", "dissolve", "boil"]),
    ("An object of density 3 g/cm³ in water will…", "sink", ["float", "rise", "freeze"]),
    ("Salty water is … than fresh water.", "denser", ["less dense", "lighter", "hotter"]),
    ("A ship made of steel floats because its overall density, including the air inside, is…", "less than water", ["more than water", "zero", "the same as steel"]),
    ("Weight acts…", "downwards", ["upwards", "sideways", "nowhere"]),
    ("If upthrust equals weight, the object…", "floats", ["sinks", "spins", "melts"]),
    ("Oil floats on water because oil is…", "less dense", ["denser", "hotter", "thicker"]),
])
u.ms("p", "Select ALL the objects that float in water (1 g/cm³).", ["Cork (0.24 g/cm³)", "Oak (0.75 g/cm³)", "Ice (0.92 g/cm³)"], ["Steel (7.8 g/cm³)", "Glass (2.5 g/cm³)"])
u.mt("p", "Match the object to what it does in water.", [("Ice cube", "floats"), ("Iron nail", "sinks"), ("Cork", "floats high")])
u.gd("p", "In which liquid does a plastic bead (1.1 g/cm³) float?", "Result", [("Fresh water (1.0 g/cm³)", "Sinks"), ("Salty water (1.2 g/cm³)", "Floats")])
u.ex("a", "Explain why a steel ship floats but a steel block of the same mass sinks.", [("ship is hollow / contains air", ["hollow|air"]), ("larger volume – average density less than water", ["volume|average|overall|less dense"]), ("block denser than water – sinks", ["block|denser"])],
     "The ship is hollow and full of air, so it has a much larger volume and its average density is less than water. The solid block has the density of steel, which is greater than water, so it sinks.")
u.nm("a", "A block has mass 450 g and volume 500 cm³. What is its density?", 0.9, "g/cm³")
u.mc("a", "The block (0.9 g/cm³) is placed in oil of density 0.8 g/cm³. What happens?", "It sinks", ["It floats", "It floats halfway out", "It dissolves"], skill="Application")
u.mc("a", "Why do fish in frozen lakes survive the winter?", "Ice floats and insulates the water below, which stays liquid", ["Ice sinks and warms the water", "Fish freeze safely", "Water freezes from the bottom up"], skill="Reasoning")
u.stop("Water has a density of 1 gram per cubic centimetre", "An object less dense than water will…", "float", ["sink", "dissolve", "melt"])
u.stop("Helium balloons rise in air for the same reason", "In a jar of honey, water and oil, which is at the bottom?", "Honey", ["Oil", "Water", "They mix"])
u.stop("because salty water is denser", "Ice floats because it is … than water.", "less dense", ["denser", "heavier", "colder only"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Density", "sec": None, "kids": [
    {"id": "me", "t": "Measuring", "d": "Volume: l × w × h, displacement • Mass: balance, subtract container", "obj": "O1", "sec": "9.1"},
    {"id": "de", "t": "Density", "d": "Density = mass ÷ volume • g/cm³ • Identifies substances", "obj": "O2", "sec": "9.1"},
    {"id": "st", "t": "States", "d": "Solids densest • Gases least dense • Air holes lower density", "obj": "O3", "sec": "9.2"},
    {"id": "tm", "t": "Temperature", "d": "Heated air expands, rises • Hot-air balloons • Sea breezes", "obj": "O3", "sec": "9.2"},
    {"id": "fl", "t": "Float or sink", "d": "Less dense than fluid floats • Water 1 g/cm³ • Ice floats • Salty water denser", "obj": "O4", "sec": "9.3"},
]}
