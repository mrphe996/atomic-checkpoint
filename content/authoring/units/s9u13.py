# -*- coding: utf-8 -*-
"""Stage 9 Unit 13 – Earth and Climate Change. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Earth and Space"
BLURB = "How convection currents move tectonic plates, the evidence that plates move, the carbon cycle, and the causes and effects of climate change."
OBJECTIVES = {
    "O1": {"sec": "13.1", "code": "9ESp.01", "codeNote": "", "t": "Explain how convection currents in the mantle move tectonic plates, and what happens at plate boundaries."},
    "O2": {"sec": "13.2", "code": "9ESp.02, 9SIC.02", "codeNote": "", "t": "Describe the evidence for tectonic plate movement."},
    "O3": {"sec": "13.3", "code": "9ESc.01", "codeNote": "", "t": "Describe the carbon cycle, including photosynthesis, respiration, decomposition and combustion."},
    "O4": {"sec": "13.4", "code": "9ESc.02, 9SIC.05", "codeNote": "", "t": "Describe the causes and impacts of climate change, past and present."},
}
SECTIONS = [
    {"id": "13.1", "title": "Movement of tectonic plates", "objs": ["O1"]},
    {"id": "13.2", "title": "Evidence for tectonic plates", "objs": ["O2"]},
    {"id": "13.3", "title": "The carbon cycle", "objs": ["O3"]},
    {"id": "13.4", "title": "What is climate change?", "objs": ["O4"]},
]
u = Unit(9, 13)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 13.1
u.sec("13.1", "O1")
u.gd("r", "What forms where plates move like this?", "Feature", [("Plates push together, rocks fold upwards", "Fold mountains"), ("Plates suddenly slip past each other", "Earthquakes"), ("Plates pull apart, magma rises", "Volcanoes")])
u.od("r", "Order the stages of a mantle convection current.", ["Hot magma rises", "It cools near the crust", "It moves sideways, dragging plates", "It sinks again"])
u.tb("r", "A plate moves 5 cm per year. Complete the table.", ["Years", "Distance (cm)"], [["10", B(50)], ["1000", B(5000)]])
u.ex("r", "Explain how convection currents move tectonic plates.", [("magma heated deep in mantle rises", ["rise|heat"]), ("cools near crust and sinks", ["cool|sink"]), ("circular currents drag plates along", ["drag|carry|move the plates|pull"])],
     "Magma heated deep in the mantle becomes less dense and rises. Near the crust it cools, spreads sideways and sinks again. These convection currents drag the plates slowly along.")
u.mc("r", "Earth's crust is made of huge rigid…", "tectonic plates", ["magma chambers", "ice sheets", "continents only"])
u.mc("r", "Convection currents happen in the…", "mantle", ["crust", "atmosphere", "inner core"])
u.mc("r", "The Himalayas formed where two plates…", "pushed together", ["pulled apart", "slid past", "stopped moving"], d="H")
u.mc("r", "Why do plates move only a few centimetres a year?", "Mantle convection currents are very slow", ["Plates are very light", "The crust is liquid", "Gravity stops them"], d="VH")
mcs("p", [
    ("Below the crust is the…", "mantle", ["inner core", "atmosphere", "ocean floor"]),
    ("Magma is…", "hot molten rock", ["cold ice", "seawater", "solid granite"]),
    ("Hot magma rises because it is…", "less dense", ["denser", "colder", "heavier"]),
    ("Cooler magma…", "sinks", ["rises", "evaporates", "explodes"]),
    ("Fold mountains form where plates…", "push together", ["pull apart", "stop", "melt"]),
    ("Earthquakes happen when plates…", "suddenly slip", ["stay still", "slowly cool", "fold upwards"]),
    ("Volcanoes form where plates…", "pull apart or one slides under another", ["never move", "are in the middle", "freeze"]),
    ("Earth's surface has changed over…", "millions of years", ["a few days", "one century", "one year"]),
    ("Tectonic plates move about…", "a few centimetres a year", ["a few metres a day", "a kilometre a year", "not at all"]),
    ("A convection current is a … flow.", "circular", ["straight", "random", "upward only"]),
    ("The heat that drives mantle convection comes from…", "Earth's core", ["the Sun", "the Moon", "the oceans"]),
    ("The boundary where plates meet is a…", "plate boundary", ["core", "mantle plume", "trench only"]),
    ("Most earthquakes happen…", "near plate boundaries", ["in the centre of plates", "in space", "in the core"]),
    ("Rising seas are eating away…", "coastlines", ["mountains", "volcanoes", "the core"]),
    ("Which feature is caused by plates pushing together?", "Fold mountains", ["Mid-ocean ridge", "Rift valley", "Hot spring"]),
])
u.mt("p", "Match the plate movement to the feature.", [("Push together", "fold mountains"), ("Slip past", "earthquakes"), ("Pull apart", "volcanoes and ridges")])
u.ms("p", "Select ALL the events caused by moving plates.", ["Earthquakes", "Volcanoes", "Fold mountains"], ["Tides", "Seasons"])
u.gd("p", "Rises or sinks in the mantle?", "Movement", [("Hot, less dense magma", "Rises"), ("Cooler, denser magma", "Sinks")])
u.ex("a", "Explain why the Atlantic Ocean is slowly getting wider.", [("plates pulling apart at mid-Atlantic", ["pull apart|apart|ridge"]), ("magma rises and forms new crust", ["magma|new crust|new rock"]), ("driven by convection currents", ["convect"])],
     "At the Mid-Atlantic Ridge the plates are pulling apart, driven by convection currents. Magma rises and cools to form new crust, so the ocean slowly widens.")
u.nm("a", "The Atlantic widens 2.5 cm a year. How many kilometres wider will it be in 1 million years? (100 000 cm = 1 km)", 25, "km")
u.mc("a", "Why does convection need a fluid, such as the hot, slowly flowing mantle rock?", "The material must be able to move and carry heat", ["Solids carry heat by convection best", "Fluids cannot be heated", "Convection only happens in space"], skill="Reasoning")
u.mc("a", "Mount Everest still grows a few millimetres a year. What is the best explanation?", "The Indian and Eurasian plates are still pushing together", ["Snow is piling up", "The mantle is cooling", "The plates are pulling apart"], skill="Reasoning")
u.stop("rising seas are eating away coastlines", "Over millions of years, Earth's surface changed because…", "tectonic plates moved", ["the Sun moved", "the Moon shrank", "oceans froze"])
u.stop("These currents drag the plates slowly along", "Tectonic plates are moved by convection currents in the…", "mantle", ["crust", "atmosphere", "oceans"])
u.stop("we get earthquakes", "Where plates push together, … form.", "fold mountains", ["rift valleys", "ocean ridges", "hot springs"])

# ---------------------------------------------------------------- 13.2
u.sec("13.2", "O2")
u.gd("r", "Which evidence for plate movement is this?", "Evidence", [("South America and Africa coasts fit together", "Fitting coastlines"), ("Same freshwater reptile on two continents", "Matching fossils"), ("Volcanoes along the Ring of Fire", "Location of volcanoes"), ("Magnetic stripes either side of the ridge", "Magnetic stripes")])
u.tb("r", "The Atlantic widens about 2.5 cm a year. Complete the table.", ["Years", "Widening (cm)"], [["100", B(250)], ["1000", B(2500)]])
u.mc("r", "Matching magnetic stripes on both sides of the Mid-Atlantic Ridge show that…", "the sea floor is spreading apart", ["the ocean is shrinking", "the magnetic field never changes", "the ridge is a mountain range"], skill="Figure")
u.ex("r", "Explain why Mesosaurus fossils are evidence that South America and Africa were once joined.", [("same fossils on both continents", ["same|identical|both"]), ("freshwater reptile couldn't swim an ocean", ["freshwater|swim|ocean"]), ("so the lands were once joined", ["joined|together|one continent"])],
     "Identical Mesosaurus fossils are found in South America and Africa. It was a freshwater reptile that could not have swum across an ocean, so the two continents must once have been joined.")
u.mc("r", "The idea of one giant continent that broke apart is supported by…", "coastlines that fit like jigsaw pieces", ["the shape of the Moon", "the weather", "the number of rivers"])
u.mc("r", "Volcanoes and earthquakes occur mainly…", "along plate boundaries", ["in the middle of plates", "at the poles only", "randomly everywhere"])
u.mc("r", "Why did people not believe plates moved at first?", "The movement is too slow to see and the cause was unknown", ["Nobody had seen a map", "Plates move very fast", "There was no evidence at all"], d="H")
u.mc("r", "How do rocks at the Mid-Atlantic Ridge record Earth's past magnetic field?", "Magma cools into rock that locks in the field's direction", ["The rocks are magnets from space", "Seawater magnetises them", "Fossils point north"], d="VH")
mcs("p", [
    ("The coasts of South America and Africa…", "fit together like a jigsaw", ["are identical in shape to Asia", "are straight lines", "never touch"]),
    ("Mesosaurus was a…", "freshwater reptile", ["sea fish", "bird", "mammal"]),
    ("The Pacific Ring of Fire is a belt of…", "volcanoes and earthquakes", ["coral reefs", "deserts", "rivers"]),
    ("At the Mid-Atlantic Ridge, magma…", "rises and cools into new rock", ["sinks into the core", "turns to ice", "becomes seawater"]),
    ("Earth's magnetic field has…", "flipped many times", ["never changed", "only pointed south", "disappeared"]),
    ("The Atlantic widens by about…", "2.5 cm a year", ["2.5 m a year", "25 km a year", "0 cm a year"]),
    ("Matching rock types on different continents suggest they were…", "once joined", ["never joined", "made in space", "always apart"]),
    ("Scientific ideas are accepted when there is…", "enough evidence", ["one opinion", "no testing", "a vote"]),
    ("Fossils of the same plant on separate continents suggest…", "the continents were joined", ["the plant could fly", "seeds swam", "nothing"]),
    ("Magnetic stripes are … on each side of the ridge.", "symmetrical", ["random", "missing", "only on one side"]),
    ("The single giant continent is often called…", "Pangaea", ["Atlantis", "Gondwana only", "Eurasia"]),
    ("New sea floor forms at…", "mid-ocean ridges", ["the poles", "deserts", "fold mountains"]),
    ("Earthquakes are recorded using a…", "seismometer", ["thermometer", "barometer", "voltmeter"]),
    ("Evidence from many sources makes a theory…", "stronger", ["weaker", "wrong", "untestable"]),
    ("Which is NOT evidence for plate movement?", "The phases of the Moon", ["Fitting coastlines", "Matching fossils", "Magnetic stripes"]),
])
u.mt("p", "Match the evidence to what it shows.", [("Fitting coastlines", "continents were once joined"), ("Volcano locations", "plates meet along boundaries"), ("Magnetic stripes", "sea floor is spreading")])
u.ms("p", "Select ALL the evidence for moving plates.", ["Matching fossils", "Fitting coastlines", "Magnetic stripes"], ["Ocean tides", "Seasons"])
u.od("p", "Order how magnetic stripes form.", ["Magma rises at the ridge", "It cools into rock", "The rock locks in the field's direction", "The plates move apart, carrying the stripe away"])
u.ex("a", "Explain how several different types of evidence together made scientists accept that plates move.", [("one piece alone could be coincidence", ["coincidence|alone|one piece"]), ("fossils, coastlines, volcanoes, stripes all agree", ["fossil|coast|volcano|stripe"]), ("convection gave a mechanism / explanation", ["convect|mechanism|cause|explain"])],
     "A single clue, like fitting coastlines, might be coincidence. But fossils, coastlines, volcano patterns and magnetic stripes all point the same way, and mantle convection explained how plates could move, so scientists accepted the theory.")
u.nm("a", "Two magnetic stripes are 50 km apart, and the plates move apart at 2.5 cm a year. How many years did that take? (1 km = 100 000 cm)", 2000000, "years")
u.mc("a", "Why are earthquakes rare in the middle of a large plate?", "Plates are rigid, so stress builds up mostly at their edges", ["Plates melt in the middle", "There is no rock there", "Earthquakes need oceans"], skill="Reasoning")
u.mc("a", "If identical fossils were found on two continents separated by a narrow land bridge, would it be strong evidence of plate movement?", "No, animals could have walked across", ["Yes, always", "No, fossils prove nothing", "Yes, bridges move plates"], skill="Evidence")
u.stop("a single giant continent that broke apart", "Which clue suggests South America and Africa were joined?", "Their coastlines fit together", ["They have the same weather", "They have the same rivers", "They are the same size"])
u.stop("where plates are moving", "Volcanoes and earthquakes occur mainly…", "along plate boundaries", ["in plate centres", "at the poles", "nowhere"])
u.stop("so the lands must once have been joined", "Mesosaurus fossils show the continents were…", "once joined", ["never joined", "underwater", "always apart"])

# ---------------------------------------------------------------- 13.3
u.sec("13.3", "O3")
u.gd("r", "Does each process take in or release carbon dioxide?", "Effect", [("Photosynthesis", "Takes in"), ("Respiration", "Releases"), ("Combustion", "Releases"), ("Decomposition", "Releases")])
u.od("r", "Order the path of carbon from the air to fossil fuel to the air.", ["Carbon dioxide in the air", "Plants photosynthesise", "Dead plants are buried, not decomposed", "Fossil fuel forms", "Fuel is burned", "Carbon dioxide returns to the air"])
u.tb("r", "A simple carbon budget (units per year). Complete the table.", ["Carbon added to air", "Carbon removed", "Net change"], [["10", "7", B(3)]])
u.ex("r", "Explain why burning fossil fuels upsets the carbon cycle.", [("fossil fuels store carbon from long ago", ["store|long ago|million"]), ("burning releases it as carbon dioxide quickly", ["burn|combust|release"]), ("added faster than removed – builds up", ["faster|build|increase|than removed"])],
     "Fossil fuels lock away carbon from millions of years ago. Burning them releases it as carbon dioxide much faster than photosynthesis can remove it, so carbon dioxide builds up in the air.")
u.mc("r", "Plants take in carbon dioxide for…", "photosynthesis", ["respiration only", "combustion", "decomposition"])
u.mc("r", "Animals get carbon by…", "feeding", ["photosynthesis", "breathing in carbon dioxide", "drinking water"])
u.mc("r", "Burning fuel is called…", "combustion", ["respiration", "photosynthesis", "decomposition"], d="H")
u.mc("r", "Why did some dead organisms become fossil fuels instead of decomposing?", "They were buried where decomposers could not break them down", ["They were too hot", "Decomposers ate them twice", "They were still alive"], d="VH")
mcs("p", [
    ("All living things release carbon dioxide by…", "respiration", ["photosynthesis", "combustion only", "drinking"]),
    ("Decomposers release carbon from…", "dead organisms", ["the Sun", "rocks", "the Moon"]),
    ("Fossil fuels include…", "coal, oil and natural gas", ["wood and paper", "water and salt", "iron and copper"]),
    ("Carbon moves around the Earth in the…", "carbon cycle", ["water cycle", "rock cycle only", "food web only"]),
    ("Which process removes carbon dioxide from the air?", "Photosynthesis", ["Respiration", "Combustion", "Decomposition"]),
    ("Humans now add carbon … than the cycle can remove it.", "faster", ["slower", "at the same speed", "never"]),
    ("Cutting down forests means … carbon dioxide is removed.", "less", ["more", "the same", "all"]),
    ("Carbon is stored in oceans, rocks, fossil fuels and…", "living things", ["the Sun", "the Moon", "the magnetic field"]),
    ("Decomposers include…", "bacteria and fungi", ["lions and eagles", "plants only", "rocks"]),
    ("When a cow eats grass, carbon moves from…", "plant to animal", ["animal to plant", "air to rock", "rock to air"]),
    ("Combustion needs…", "oxygen", ["nitrogen", "carbon dioxide", "water"]),
    ("Carbon in fossil fuels was originally taken in by…", "ancient plants", ["volcanoes", "the oceans only", "the Sun"]),
    ("Burning wood releases carbon dioxide and…", "water vapour", ["oxygen", "nitrogen", "helium"]),
    ("Respiration happens in…", "all living things", ["only animals", "only plants", "only bacteria"]),
    ("Planting trees helps the carbon cycle because trees…", "absorb carbon dioxide", ["release carbon dioxide only", "burn fuel", "decompose instantly"]),
])
u.mt("p", "Match the process to what happens to carbon.", [("Photosynthesis", "taken from the air"), ("Respiration", "returned to the air"), ("Feeding", "passed along a food chain")])
u.ms("p", "Select ALL the processes that release carbon dioxide.", ["Respiration", "Combustion", "Decomposition"], ["Photosynthesis", "Burial of dead plants"])
u.gd("p", "Carbon store or process?", "Type", [("Coal", "Store"), ("Burning", "Process"), ("Oceans", "Store")])
u.ex("a", "Suggest two ways to reduce the amount of carbon dioxide humans add to the air, and explain each.", [("use renewable energy instead of fossil fuels", ["renewable|solar|wind|less fossil"]), ("plant trees / stop deforestation", ["plant|tree|forest"]), ("explanation: less combustion / more photosynthesis", ["combust|burn|photosynth|absorb"])],
     "Generate electricity from renewable sources, so less fossil fuel is burned. Plant trees and protect forests, so more carbon dioxide is taken in by photosynthesis.")
u.nm("a", "A car releases 120 g of carbon dioxide per km. How many kilograms does it release in 500 km?", 60, "kg")
u.mc("a", "Why is burning wood from a sustainably replanted forest considered nearly carbon neutral?", "New trees take in about the same carbon dioxide as burning released", ["Wood releases no carbon dioxide", "Trees do not respire", "Fire destroys carbon"], skill="Reasoning")
u.mc("a", "Why does warming oceans make the carbon problem worse?", "Warmer water holds less dissolved carbon dioxide", ["Warm water absorbs more carbon dioxide", "Oceans burn carbon", "Fish make carbon dioxide disappear"], skill="Reasoning")
u.stop("decomposers release carbon from dead organisms", "Plants take in carbon dioxide for…", "photosynthesis", ["respiration", "combustion", "decomposition"])
u.stop("Humans now add carbon faster than the cycle can remove it", "Burning fossil fuels is called…", "combustion", ["respiration", "photosynthesis", "decomposition"])

# ---------------------------------------------------------------- 13.4
u.sec("13.4", "O4")
u.gd("r", "Natural or human cause of climate change?", "Cause", [("Asteroid impact dust", "Natural"), ("Burning fossil fuels", "Human"), ("Ice ages", "Natural"), ("Deforestation", "Human")])
u.gr("r", "Global temperature change since 1880. Plot the points.", {"label": "Year", "min": 1880, "max": 2020, "step": 20}, {"label": "Change (°C)", "min": -0.4, "max": 1.2, "step": 0.4}, [[1880, -0.2], [1920, -0.3], [1960, 0.0], [1980, 0.2], [2000, 0.4], [2020, 1.0]])
u.tb("r", "Sea level rises about 3.5 mm a year. Complete the table.", ["Years", "Rise (mm)"], [["10", B(35)], ["100", B(350)]])
u.ex("r", "Explain two reasons why sea levels are rising.", [("warmer water expands", ["expand"]), ("ice sheets / glaciers melt", ["melt|ice"]), ("linked to global warming", ["warm|temperature"])],
     "As the oceans warm, the water expands, and ice sheets and glaciers on land melt, adding more water. Both are caused by global warming.")
u.mc("r", "Climate change is a change in Earth's…", "long-term pattern of temperature, wind and rainfall", ["weather today", "tides", "day length"])
u.mc("r", "In the past, an asteroid impact changed the climate by…", "throwing up dust that blocked sunlight", ["adding water", "creating oceans", "making the Sun hotter"])
u.mc("r", "What does the temperature graph show about the last 30 years?", "Warming has been much faster than before", ["Temperatures have fallen", "No change", "Warming has slowed"], d="H")
u.mc("r", "Why are cities like Jakarta especially threatened by climate change?", "They are low-lying coastal cities facing rising seas", ["They are high in mountains", "They have no rainfall", "They are near the poles"], d="VH")
mcs("p", [
    ("Temperature records go back to about…", "1880", ["1580", "1980", "2010"]),
    ("A time when Earth was almost completely frozen is called…", "snowball Earth", ["the greenhouse age", "the asteroid era", "the Ring of Fire"]),
    ("Scientists predict more severe…", "storms, droughts and floods", ["earthquakes only", "eclipses", "tides only"]),
    ("Sea levels are rising about…", "3.5 mm a year", ["3.5 m a year", "35 cm a year", "0 mm a year"]),
    ("Human activity is upsetting the…", "carbon cycle", ["rock cycle only", "Moon's orbit", "magnetic field"]),
    ("Warmer oceans…", "expand", ["shrink", "freeze", "disappear"]),
    ("Ice sheets melting causes sea levels to…", "rise", ["fall", "stay the same", "freeze"]),
    ("Climate change in the past was caused by…", "natural events such as asteroids and ice ages", ["cars", "factories", "power stations"]),
    ("Climate is different from weather because it describes…", "long-term patterns", ["today only", "one storm", "one hour"]),
    ("A greenhouse gas released by burning fuel is…", "carbon dioxide", ["oxygen", "nitrogen", "argon"]),
    ("Droughts reduce…", "crop yields", ["sea level", "rainfall forecasting", "air pressure"]),
    ("Coral reefs are harmed by…", "warmer, more acidic oceans", ["cooler oceans", "less carbon dioxide", "fewer storms"]),
    ("Floods are more likely because warmer air holds…", "more water vapour", ["less water vapour", "no water", "more oxygen"]),
    ("Reducing fossil fuel use helps…", "slow climate change", ["speed up warming", "cause ice ages", "stop all weather"]),
    ("Scientists predict future climate using…", "computer models and data", ["guesses", "one thermometer", "fortune telling"]),
])
u.mt("p", "Match the cause to the effect.", [("Warmer oceans", "sea water expands"), ("Melting ice sheets", "more water in the sea"), ("More heat in the atmosphere", "more severe storms")])
u.ms("p", "Select ALL the predicted effects of climate change.", ["Rising sea levels", "More droughts", "More severe storms"], ["More ice ages", "Fewer floods everywhere"])
u.od("p", "Order the chain of events.", ["More carbon dioxide released", "More heat trapped", "Global temperatures rise", "Ice melts and seas rise"])
u.ex("a", "Using the temperature graph, describe the trend since 1880 and explain how scientists link it to human activity.", [("small changes until ~1960, then rapid rise", ["rise|increase|warm"]), ("about 1 °C warmer", ["1 ?°c|1\\.0|one degree"]), ("matches rise in CO2 from burning fuels", ["carbon|co2|fossil|burn"])],
     "Temperatures changed little until about 1960, then rose quickly, reaching about 1 °C above 1880 levels. This rise matches the increase in carbon dioxide from burning fossil fuels, which traps more heat.")
u.nm("a", "If sea level rises 3.5 mm a year, how many centimetres will it rise in 80 years?", 28, "cm")
u.mc("a", "Why do scientists say current climate change is different from past natural changes?", "It is happening much faster and is driven by human activity", ["It is slower", "It is caused only by asteroids", "It has stopped"], skill="Reasoning")
u.mc("a", "A low-lying island nation is most concerned about which effect?", "Rising sea levels", ["Fewer storms", "More ice", "Colder winters"], skill="Application")
u.stop("and even a 'snowball Earth'", "In the past, asteroid dust changed the climate by…", "blocking sunlight", ["adding heat", "making water", "moving plates"])
u.stop("Human activity is upsetting the carbon cycle", "Records since 1880 show the planet is…", "warming", ["cooling", "unchanged", "freezing"])
u.stop("threatening coastal cities like Jakarta", "Sea levels rise because warmer water expands and…", "ice sheets melt", ["it rains less", "plates sink", "the Moon pulls less"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Earth and climate change", "sec": None, "kids": [
    {"id": "pl", "t": "Plates", "d": "Mantle convection drags plates • Fold mountains, volcanoes, earthquakes", "obj": "O1", "sec": "13.1"},
    {"id": "ev", "t": "Evidence", "d": "Fitting coastlines • Mesosaurus fossils • Ring of Fire • Magnetic stripes", "obj": "O2", "sec": "13.2"},
    {"id": "cc", "t": "Carbon cycle", "d": "Photosynthesis takes in • Respiration, decomposition, combustion release", "obj": "O3", "sec": "13.3"},
    {"id": "cl", "t": "Climate change", "d": "Past: asteroids, ice ages • Now: fast warming since 1880", "obj": "O4", "sec": "13.4"},
    {"id": "im", "t": "Impacts", "d": "Storms, droughts, floods • Sea level +3.5 mm/year • Coastal cities", "obj": "O4", "sec": "13.4"},
]}
