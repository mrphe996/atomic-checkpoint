# -*- coding: utf-8 -*-
"""Stage 7 Unit 13 – The Earth. Written by the Camday teaching team."""
from c_kit import *

STRAND = "Earth and Space"
BLURB = "The Earth's layers and tectonic plates, earthquakes, volcanoes and fold mountains, the composition of air, and the water cycle."

OBJECTIVES = {
    "O1": {"sec": "13.1", "code": "7ESp.01", "codeNote": "", "t": "Describe the structure of the Earth and the model of plate tectonics."},
    "O2": {"sec": "13.2", "code": "7ESp.02", "codeNote": "", "t": "Explain how earthquakes, volcanoes and fold mountains form at plate boundaries."},
    "O3": {"sec": "13.3", "code": "7ESp.03", "codeNote": "", "t": "Describe the composition of air and how natural events and pollution change it."},
    "O4": {"sec": "13.4", "code": "7ESc.01", "codeNote": "", "t": "Describe the stages of the water cycle."},
}

SECTIONS = [
    {"id": "13.1", "title": "Structure of the Earth", "objs": ["O1"]},
    {"id": "13.2", "title": "Movement of tectonic plates", "objs": ["O2"]},
    {"id": "13.3", "title": "The Earth's atmosphere", "objs": ["O3"]},
    {"id": "13.4", "title": "The water cycle", "objs": ["O4"]},
]

S1_REQ = [
    od("u13s1r1", "M", "O1", "Order the Earth's layers from the outside in.", ["Crust", "Mantle", "Outer core", "Inner core"]),
    gd("u13s1r2", "M", "O1", "Solid or liquid?", ["State"], [("Crust", ["Solid"]), ("Upper mantle (magma)", ["Semi-molten"]), ("Outer core", ["Liquid"]), ("Inner core", ["Solid"])], skill="Figure"),
    mc("u13s1r3", "M", "O1", "The core is made mainly of…", ("iron and nickel", "Correct."), [("rock and sand", "No."), ("water", "No."), ("gold and silver", "No.")]),
    ex("u13s1r4", "H", "O1", "The inner core is the hottest layer. Explain why it is solid.",
       [("enormous pressure", ["pressure"])],
       "The enormous pressure at the centre of the Earth keeps the inner core solid, even though it is the hottest layer.", need=1),
    mc("u13s1r5", "H", "O1", "Oceanic crust compared with continental crust is…", ("denser", "Correct."), [("less dense", "No."), ("lighter in colour always", "No."), ("liquid", "No.")]),
    tb("u13s1r6", "H", "O1", "A plate moves 5 cm a year. Complete.", ["Time (years)", "Distance moved (cm)"],
       [["1", "5"], ["10", B(50)], ["1000", B(5000)]], skill="Data"),
    mc("u13s1r7", "M", "O1", "Tectonic plates are…", ("huge slabs of crust that fit together like a jigsaw", "Correct."), [("layers of the core", "No."), ("clouds", "No."), ("small rocks", "No.")]),
    mc("u13s1r8", "VH", "O1", "Why do scientists think plates move?", ("The hot core heats magma in the mantle, which rises, spreads and sinks, dragging plates.", "Correct."), [("The Moon pulls them", "No."), ("Wind pushes them", "No."), ("Oceans push them", "No.")], skill="Reasoning"),
]
S1_PRAC = [
    mc("u13s1p01", "M", "O1", "The thin outer layer of solid rock is the…", "crust", [("mantle", "No."), ("core", "No."), ("magma", "No.")]),
    mc("u13s1p02", "M", "O1", "The crust is up to about ___ km thick.", "60", [("6000", "No."), ("600", "No."), ("6", "Too thin.")]),
    mc("u13s1p03", "M", "O1", "Semi-molten rock is called…", "magma", [("lava", "Magma at the surface."), ("crust", "No."), ("core", "No.")]),
    mc("u13s1p04", "M", "O1", "The lower mantle is solid because of…", "huge pressure", [("low temperature", "It's extremely hot."), ("water", "No."), ("iron", "No.")]),
    mc("u13s1p05", "M", "O1", "The outer core is…", "liquid metal", [("solid rock", "No."), ("gas", "No."), ("water", "No.")]),
    mc("u13s1p06", "M", "O1", "Plates move about…", "1 to 10 cm a year", [("1 to 10 km a year", "No."), ("1 m a day", "No."), ("not at all", "No.")]),
    mc("u13s1p07", "H", "O1", "Plates are about ___ thick.", "100 km", [("1 km", "No."), ("10 m", "No."), ("10 000 km", "No.")]),
    mc("u13s1p08", "M", "O1", "Continental crust forms…", "the continents", [("the ocean floor", "Oceanic."), ("the core", "No."), ("clouds", "No.")]),
    mc("u13s1p09", "M", "O1", "Geothermal energy is…", "heat from inside the Earth", [("energy from wind", "No."), ("energy from tides", "No."), ("energy from food", "No.")]),
    gd("u13s1p10", "M", "O1", "Which layer?", ["Layer"], [("Iron and nickel", ["Core"]), ("Thin solid rock", ["Crust"]), ("Magma", ["Mantle"])], skill="Figure"),
    mc("u13s1p11", "H", "O1", "Why do diagrams that show the crust as one piece mislead us?", "The crust is really broken into tectonic plates", [("The crust is liquid", "No."), ("There is no crust", "No."), ("The crust is the core", "No.")], skill="Reasoning"),
    mc("u13s1p12", "H", "O1", "The plates rest on the…", "mantle", [("inner core", "No."), ("ocean", "No."), ("atmosphere", "No.")]),
    mc("u13s1p13", "H", "O1", "Which layer is the hottest?", "Inner core", [("Crust", "No."), ("Upper mantle", "No."), ("Outer core", "Close, but no.")]),
    nm("u13s1p14", "H", "O1", "A plate moves 2 cm a year. How far in 1 million years, in km? (100 000 cm = 1 km)", 20, "km"),
    mc("u13s1p15", "M", "O1", "Volcanoes are openings where…", "heat escapes from inside the Earth", [("water enters the core", "No."), ("wind is made", "No."), ("plates are glued", "No.")]),
    mc("u13s1p16", "H", "O1", "Oceanic crust forms…", "the ocean floor", [("mountains only", "No."), ("the continents", "No."), ("the core", "No.")]),
    mc("u13s1p17", "H", "O1", "The idea that the crust is made of moving plates is called…", "plate tectonics", [("the water cycle", "No."), ("the particle model", "No."), ("the Big Bang", "No.")]),
    od("u13s1p18", "M", "O1", "Order the convection that moves plates.", ["Core heats magma", "Hot magma rises", "Magma spreads under the plates", "Magma cools and sinks"]),
]
S1_ADV = [
    adv(ex("u13s1a1", "VH", "O1", "Use the jigsaw idea to explain one piece of evidence that continents were once joined.",
           [("coastlines fit together", ["coast|fit|shape|jigsaw"]), ("plates/continents moved apart", ["moved|drift|apart|plates"])],
           "The coastlines of South America and Africa fit together like jigsaw pieces, suggesting they were once joined and have since moved apart on separate plates.", need=2)),
    adv(mc("u13s1a2", "VH", "O1", "Why can't scientists drill to the core to check its structure?", ("It is thousands of km deep, extremely hot and under huge pressure.", "Correct."), [("It is made of water", "No."), ("It's illegal", "No."), ("The core is at the surface", "No.")], skill="Reasoning")),
    adv(nm("u13s1a3", "VH", "O1", "The Atlantic widens about 2.5 cm a year. How many years to widen by 1 m?", 40, "years")),
    adv(mc("u13s1a4", "VH", "O1", "A model of the Earth as a peach (skin, flesh, stone) is limited because…", ("it doesn't show the core's two parts or the plates", "Correct."), [("peaches are round", "So is Earth."), ("it is too small", "Scale is fine."), ("it shows plates perfectly", "No.")], skill="Reasoning")),
]

S2_REQ = [
    gd("u13s2r1", "M", "O2", "Which plate boundary?", ["Boundary"],
       [("Plates slide past each other", ["Transform"]), ("Plates move apart", ["Divergent"]), ("Plates collide", ["Convergent"])], skill="Figure"),
    mc("u13s2r2", "M", "O2", "The point underground where an earthquake starts is the…", ("focus", "Correct."), [("epicentre", "On the surface."), ("vent", "Volcano."), ("crater", "No.")]),
    ex("u13s2r3", "H", "O2", "Explain how an earthquake happens at a transform boundary.",
       [("friction makes plates stick / stress builds", ["friction|stick|stress"]), ("sudden movement releases energy / seismic waves", ["sudden|release|seismic|shock|wave"])],
       "Friction makes the plates stick, so stress builds up. When it becomes too great, the plates move suddenly, releasing energy as seismic waves that shake the ground.", need=2),
    od("u13s2r4", "H", "O2", "Order the steps of a volcanic eruption.", ["Magma rises because it is less dense", "Magma collects in a magma chamber", "Pressure builds up", "Magma bursts out through the vent as lava"]),
    mc("u13s2r5", "M", "O2", "Magma that reaches the surface is called…", ("lava", "Correct."), [("ash", "No."), ("crust", "No."), ("core", "No.")]),
    tb("u13s2r6", "H", "O2", "Everest may grow up to 0.5 cm a year. Complete.", ["Years", "Growth (cm)"],
       [["10", B(5)], ["100", B(50)]], skill="Data"),
    mc("u13s2r7", "H", "O2", "The Himalayas formed when…", ("the Indian Plate pushed into the Eurasian Plate", "Correct."), [("a volcano erupted", "No."), ("plates moved apart", "No."), ("ice melted", "No.")]),
    mc("u13s2r8", "VH", "O2", "Why does Indonesia have many earthquakes?", ("Three plates meet there.", "Correct."), [("It is near the equator", "No."), ("It is an island", "Not why."), ("It has many people", "No.")], skill="Reasoning"),
]
S2_PRAC = [
    mc("u13s2p01", "M", "O2", "Where two or more plates meet is a…", "plate boundary", [("plate centre", "No."), ("core", "No."), ("magma chamber", "No.")]),
    mc("u13s2p02", "M", "O2", "The point on the surface directly above the focus is the…", "epicentre", [("vent", "No."), ("core", "No."), ("crater", "No.")]),
    mc("u13s2p03", "M", "O2", "Fold mountains form at…", "convergent boundaries", [("transform boundaries", "No."), ("divergent boundaries", "No."), ("the core", "No.")]),
    mc("u13s2p04", "M", "O2", "Energy from an earthquake travels as…", "seismic waves", [("light", "No."), ("magma", "No."), ("wind", "No.")]),
    mc("u13s2p05", "M", "O2", "A volcano is…", "a vent in the crust where magma and gases escape", [("a mountain made of ice", "No."), ("a hole in the core", "No."), ("a type of earthquake", "No.")]),
    mc("u13s2p06", "M", "O2", "Magma rises because it is…", "less dense than the solid rock around it", [("heavier", "No."), ("cold", "No."), ("magnetic", "No.")]),
    mc("u13s2p07", "H", "O2", "Mount Vesuvius destroyed which Roman city?", "Pompeii", [("Rome", "No."), ("Athens", "No."), ("London", "No.")]),
    mc("u13s2p08", "M", "O2", "There are about ___ active volcanoes today.", "600", [("6", "No."), ("60 000", "No."), ("6 million", "No.")]),
    mc("u13s2p09", "H", "O2", "A volcano's cone is made from…", "layers of lava and ash", [("ice", "No."), ("sand from the sea", "No."), ("iron from the core", "No.")]),
    mc("u13s2p10", "H", "O2", "At a divergent boundary, magma rising into the gap forms…", "volcanoes and valleys", [("fold mountains", "Convergent."), ("nothing", "No."), ("deserts", "No.")]),
    gd("u13s2p11", "M", "O2", "Feature and boundary", ["Boundary"], [("Fold mountains", ["Convergent"]), ("Earthquakes from sliding plates", ["Transform"]), ("New crust from rising magma", ["Divergent"])], skill="Data"),
    mc("u13s2p12", "H", "O2", "Geothermal power plants use…", "underground water heated by magma", [("wind", "No."), ("sunlight", "No."), ("coal", "No.")]),
    mc("u13s2p13", "H", "O2", "You can model fold mountains by…", "gently pushing two sheets of paper together", [("pouring water", "No."), ("heating ice", "No."), ("drawing circles", "No.")]),
    mc("u13s2p14", "M", "O2", "The Himalayas formed about…", "50 million years ago", [("50 years ago", "No."), ("5000 years ago", "No."), ("5 billion years ago", "No.")]),
    nm("u13s2p15", "H", "O2", "Vesuvius erupted in 79 CE. About how many years before 2026 was that?", 1947, "years"),
    mc("u13s2p16", "H", "O2", "Why are earthquakes and volcanoes found in long belts on a world map?", "They mostly occur along plate boundaries", [("They follow rivers", "No."), ("They follow the equator", "No."), ("They are random", "No.")], skill="Reasoning"),
    od("u13s2p17", "M", "O2", "Order the earthquake process.", ["Plates push against each other", "Friction makes them stick", "Stress builds up", "Plates move suddenly – seismic waves"]),
    mc("u13s2p18", "H", "O2", "Why might Everest still be growing?", "The plates are still colliding", [("Snow keeps falling", "Not the reason."), ("Volcanoes underneath", "No."), ("Erosion", "Makes it smaller.")]),
]
S2_ADV = [
    adv(ex("u13s2a1", "VH", "O2", "Compare how a volcano and a fold mountain form.",
           [("volcano: magma/lava erupts at weak point", ["magma|lava|erupt|vent"]), ("fold mountain: plates collide, rock folds up", ["collide|fold|push|converg"])],
           "A volcano forms when magma rises through a weak point and erupts, building layers of lava and ash. A fold mountain forms when two continental plates collide and the rock layers are folded upwards.", need=2)),
    adv(nm("u13s2a2", "VH", "O2", "Seismic waves travel at about 6 km/s. How long to reach a town 300 km from the focus?", 50, "s")),
    adv(mc("u13s2a3", "VH", "O2", "Why do people still live near active volcanoes?", ("Volcanic soil is fertile and geothermal energy is available.", "Correct."), [("Volcanoes are never dangerous", "No."), ("It's colder", "No."), ("There is no rain", "No.")], skill="Reasoning")),
    adv(mc("u13s2a4", "VH", "O2", "Why can't scientists predict the exact time of an earthquake?", ("Stress builds slowly underground and the moment of release is hard to measure.", "Correct."), [("Earthquakes are random everywhere", "They cluster at boundaries."), ("They always give warning", "No."), ("Plates don't move", "No.")], skill="Reasoning")),
]

S3_REQ = [
    tb("u13s3r1", "M", "O3", "Composition of clean, dry air (%). Complete.", ["Gas", "Percentage"],
       [["Nitrogen", "78"], ["Oxygen", "21"], ["Carbon dioxide and other gases", B(1)]], skill="Data"),
    mc("u13s3r2", "M", "O3", "The most common gas in air is…", ("nitrogen", "Correct – about 78%."), [("oxygen", "21%."), ("carbon dioxide", "Tiny."), ("hydrogen", "No.")]),
    mc("u13s3r3", "M", "O3", "Humidity is…", ("the amount of water vapour in the air", "Correct."), [("the amount of oxygen", "No."), ("air temperature", "No."), ("wind speed", "No.")]),
    gd("u13s3r4", "H", "O3", "Natural emission or pollution?", ["Source"], [("Volcanic eruption", ["Natural"]), ("Car exhaust", ["Pollution"]), ("Animals respiring", ["Natural"]), ("Power station", ["Pollution"])], skill="Data"),
    ex("u13s3r5", "H", "O3", "Explain how cutting down and burning tropical forests affects carbon dioxide in the air.",
       [("burning releases carbon dioxide", ["burn|release"]), ("fewer trees to absorb it / photosynthesis", ["fewer|absorb|photosynth"])],
       "Burning the trees releases carbon dioxide, and with fewer trees left there is less photosynthesis to absorb it, so carbon dioxide in the air rises.", need=2),
    mc("u13s3r6", "H", "O3", "More carbon dioxide causes global warming because…", ("it traps heat", "Correct."), [("it is poisonous", "No."), ("it blocks sunlight", "No."), ("it makes acid rain only", "No.")]),
    mc("u13s3r7", "M", "O3", "Particulate matter is…", ("tiny particles of pollution that cause breathing problems", "Correct."), [("a type of oxygen", "No."), ("water vapour", "No."), ("a cloud", "No.")]),
    mc("u13s3r8", "VH", "O3", "Warm days often feel more humid because…", ("warm air can hold more water vapour", "Correct."), [("warm air has more oxygen", "No."), ("nitrogen increases", "No."), ("there's no wind", "No.")], skill="Reasoning"),
]
S3_PRAC = [
    mc("u13s3p01", "M", "O3", "The layer of air around the Earth is the…", "atmosphere", [("crust", "No."), ("mantle", "No."), ("core", "No.")]),
    mc("u13s3p02", "M", "O3", "Oxygen makes up about ___ of air.", "21%", [("78%", "Nitrogen."), ("1%", "No."), ("50%", "No.")]),
    mc("u13s3p03", "M", "O3", "Nitrogen and oxygen together make up about ___ of dry air.", "99%", [("50%", "No."), ("78%", "No."), ("21%", "No.")]),
    mc("u13s3p04", "M", "O3", "About four-fifths of air is…", "nitrogen", [("oxygen", "No."), ("carbon dioxide", "No."), ("water", "No.")]),
    mc("u13s3p05", "M", "O3", "Every living thing gives off carbon dioxide when it…", "respires", [("sleeps", "No."), ("grows hair", "No."), ("drinks", "No.")]),
    mc("u13s3p06", "H", "O3", "A volcanic eruption releases ash, carbon dioxide, water vapour and…", "sulfur dioxide", [("oxygen", "No."), ("nitrogen only", "No."), ("helium", "No.")]),
    mc("u13s3p07", "H", "O3", "OCO-3 on the ISS measures…", "carbon dioxide in the atmosphere", [("ocean depth", "No."), ("earthquakes", "No."), ("star brightness", "No.")]),
    mc("u13s3p08", "M", "O3", "Burning fossil fuels releases…", "sulfur dioxide, oxides of nitrogen and particulates", [("pure oxygen", "No."), ("only water", "No."), ("nothing", "No.")]),
    gd("u13s3p09", "M", "O3", "Gas and percentage of dry air", ["Percentage"], [("Nitrogen", ["78%"]), ("Oxygen", ["21%"]), ("Others incl. CO₂", ["1%"])], skill="Data"),
    nm("u13s3p10", "H", "O3", "A room holds 50 m³ of air. About how much is oxygen (21%)?", 10.5, "m³"),
    nm("u13s3p11", "H", "O3", "A room holds 50 m³ of air. About how much is nitrogen (78%)?", 39, "m³"),
    mc("u13s3p12", "H", "O3", "Scientists' measurements show carbon dioxide in the air is…", "rising", [("falling", "No."), ("constant", "No."), ("zero", "No.")]),
    mc("u13s3p13", "H", "O3", "Tropical forests help reduce carbon dioxide because they…", "absorb it for photosynthesis", [("burn it", "No."), ("make it", "No."), ("freeze it", "No.")]),
    mc("u13s3p14", "M", "O3", "Real air also contains…", "water vapour", [("liquid water drops only", "No."), ("iron", "No."), ("salt crystals only", "No.")]),
    mc("u13s3p15", "H", "O3", "Why do small changes in carbon dioxide matter?", "They have big effects on the Earth's climate", [("They change oxygen to 0%", "No."), ("They don't matter", "No."), ("They stop rain", "No.")]),
    mc("u13s3p16", "M", "O3", "Which gas do we need to breathe?", "Oxygen", [("Nitrogen", "No."), ("Carbon dioxide", "No."), ("Sulfur dioxide", "No.")]),
    od("u13s3p17", "M", "O3", "Order gases in air from most to least.", ["Nitrogen", "Oxygen", "Carbon dioxide and other gases"], skill="Data"),
    mc("u13s3p18", "H", "O3", "How does OCO-3's data help?", "It helps us find solutions to climate change", [("It predicts earthquakes", "No."), ("It makes rain", "No."), ("It measures volcanoes only", "No.")]),
]
S3_ADV = [
    adv(ex("u13s3a1", "VH", "O3", "Suggest TWO ways to reduce air pollution in a city and explain one.",
           [("fewer fossil-fuel vehicles / electric / public transport", ["electric|public transport|bus|cycl|walk|fewer cars"]), ("renewable power / trees / filters", ["renew|solar|wind|tree|filter|scrub"]), ("explanation: less burning → fewer pollutants", ["less|fewer|reduce"])],
           "Use electric buses and more cycling, and generate power from renewables. Burning less fossil fuel releases less sulfur dioxide, nitrogen oxides and particulates.", need=2)),
    adv(mc("u13s3a2", "VH", "O3", "A graph shows CO₂ rising every year with small ups and downs each season. Why the seasonal dips?", ("Plants photosynthesise more in summer, absorbing CO₂.", "Correct."), [("Volcanoes stop in summer", "No."), ("People stop breathing", "No."), ("Measurement errors only", "No.")], skill="Data")),
    adv(nm("u13s3a3", "VH", "O3", "OCO-3 measures CO₂ 72 000 times a day. How many times in a week?", 504000, "")),
    adv(mc("u13s3a4", "VH", "O3", "Why does the percentage of oxygen in air stay roughly constant?", ("Photosynthesis replaces oxygen used by respiration and combustion.", "Correct."), [("Oxygen is never used", "No."), ("Nitrogen turns into oxygen", "No."), ("Volcanoes make oxygen", "No.")], skill="Reasoning")),
]

S4_REQ = [
    od("u13s4r1", "M", "O4", "Order the water cycle stages.", ["Evaporation", "Condensation", "Precipitation", "Run-off and collection"]),
    gd("u13s4r2", "M", "O4", "Name the stage.", ["Stage"],
       [("Sun heats sea water into vapour", ["Evaporation"]), ("Vapour cools into droplets", ["Condensation"]), ("Rain or snow falls", ["Precipitation"]), ("Water soaks into the ground", ["Groundwater"])], skill="Figure"),
    mc("u13s4r3", "M", "O4", "Clouds are made of…", ("tiny water droplets", "Correct."), [("water vapour only", "Invisible."), ("smoke", "No."), ("dust only", "No.")]),
    ex("u13s4r4", "H", "O4", "Explain why water vapour turns into clouds as it rises.",
       [("cools", ["cool"]), ("condenses into droplets", ["condens|droplet"])],
       "As water vapour rises it cools, and condenses into tiny droplets of water that collect to form clouds.", need=2),
    mc("u13s4r5", "M", "O4", "Precipitation falls because the droplets…", ("grow larger and heavier", "Correct."), [("get hotter", "No."), ("evaporate", "No."), ("become gas", "No.")]),
    tb("u13s4r6", "H", "O4", "Rain gauge data (mm). Complete the total.", ["Day", "Rain (mm)"],
       [["Mon", "4"], ["Tue", "12"], ["Wed", "0"], ["Total", B(16)]], skill="Data"),
    mc("u13s4r7", "H", "O4", "Water flowing across the land into rivers is…", ("run-off", "Correct."), [("evaporation", "No."), ("condensation", "No."), ("groundwater", "Underground.")]),
    mc("u13s4r8", "VH", "O4", "In the cling-film model, what do the ice cubes represent?", ("Cold air higher up, where vapour condenses", "Correct."), [("The Sun", "Warm water."), ("The sea", "Warm water."), ("Rivers", "No.")], skill="Reasoning"),
]
S4_PRAC = [
    mc("u13s4p01", "M", "O4", "The water cycle describes…", "how water moves continuously around the Earth", [("how plates move", "No."), ("how air is made", "No."), ("how volcanoes erupt", "No.")]),
    mc("u13s4p02", "M", "O4", "Evaporation is powered by…", "the Sun's heat", [("the Moon", "No."), ("wind only", "No."), ("the core", "No.")]),
    mc("u13s4p03", "M", "O4", "Condensation is…", "vapour turning into liquid droplets", [("liquid turning to gas", "Evaporation."), ("water falling", "Precipitation."), ("water soaking in", "No.")]),
    mc("u13s4p04", "M", "O4", "Rain and snow are…", "precipitation", [("condensation", "No."), ("evaporation", "No."), ("run-off", "No.")]),
    mc("u13s4p05", "M", "O4", "Water that soaks into the ground becomes…", "groundwater", [("vapour", "No."), ("clouds", "No."), ("ice caps", "No.")]),
    mc("u13s4p06", "H", "O4", "Groundwater can also…", "flow back to the sea", [("rise into space", "No."), ("turn into rock", "No."), ("become magma", "No.")]),
    gd("u13s4p07", "M", "O4", "Change of state in the cycle", ["Change"], [("Evaporation", ["Liquid → gas"]), ("Condensation", ["Gas → liquid"])], skill="Data"),
    mc("u13s4p08", "H", "O4", "The rain falling on you today could have been…", "in the ocean yesterday", [("made today from nothing", "No."), ("from the core", "No."), ("lost forever", "No.")]),
    mc("u13s4p09", "H", "O4", "In the glass model, the cling film represents…", "where clouds form", [("the sea", "No."), ("the Sun", "No."), ("groundwater", "No.")]),
    mc("u13s4p10", "M", "O4", "Which stage forms clouds?", "Condensation", [("Evaporation", "No."), ("Run-off", "No."), ("Precipitation", "No.")]),
    mc("u13s4p11", "H", "O4", "Why do puddles dry faster on hot days?", "Evaporation is faster when it is warmer", [("Water soaks in faster", "Not mainly."), ("Rain stops", "No."), ("Clouds absorb puddles", "No.")], skill="Reasoning"),
    nm("u13s4p12", "H", "O4", "A week's rainfall totals 35 mm. Mean rain per day?", 5, "mm"),
    mc("u13s4p13", "M", "O4", "Water collects in…", "rivers, lakes and oceans", [("the core", "No."), ("the mantle", "No."), ("the Sun", "No.")]),
    mc("u13s4p14", "H", "O4", "Which of these is NOT part of the water cycle?", "Erupting", [("Evaporating", "Yes."), ("Condensing", "Yes."), ("Precipitating", "Yes.")]),
    mc("u13s4p15", "H", "O4", "Snow falls instead of rain when…", "the air is cold enough to freeze the water", [("there is no water", "No."), ("it is hot", "No."), ("it is windy only", "No.")]),
    mc("u13s4p16", "H", "O4", "Is the water cycle a physical or chemical process?", "Physical – only the state of water changes", [("Chemical", "No new substance."), ("Both", "No."), ("Neither", "It is physical.")], skill="Reasoning"),
    od("u13s4p17", "M", "O4", "Order the journey of one water drop.", ["Ocean water evaporates", "Vapour rises and cools", "Condenses into a cloud", "Falls as rain onto a hill", "Runs off into a river"]),
    mc("u13s4p18", "M", "O4", "The cycle goes on…", "continuously", [("once a year", "No."), ("only in winter", "No."), ("only at night", "No.")]),
]
S4_ADV = [
    adv(ex("u13s4a1", "VH", "O4", "Describe how to set up the warm-water-and-ice model, and link each part to the real water cycle.",
           [("warm water = sea / evaporation", ["warm|sea|ocean|evapor"]), ("ice/cling film = cold air / condensation", ["ice|cold|condens|cling"]), ("drops fall = precipitation", ["drop|fall|rain|precip"])],
           "Put warm water in a glass, cover with cling film and put ice cubes on top. The warm water evaporates (like the sea), the vapour condenses under the cold film (clouds), and drops fall back (precipitation).", need=2)),
    adv(mc("u13s4a2", "VH", "O4", "How could cutting down forests affect the local water cycle?", ("Less water enters the air from plants, and more run-off may cause floods.", "Correct."), [("No effect", "No."), ("More clouds always", "No."), ("Rain stops forever", "No.")], skill="Reasoning")),
    adv(nm("u13s4a3", "VH", "O4", "1 mm of rain on 1 m² is 1 litre. How many litres fall on a 20 m² roof in 15 mm of rain?", 300, "L")),
    adv(mc("u13s4a4", "VH", "O4", "How is global warming likely to change the water cycle?", ("More evaporation and heavier rainfall in some places", "Correct."), [("It will stop it", "No."), ("Less evaporation everywhere", "No."), ("No change", "No.")], skill="Reasoning")),
]

POOLS = {"13.1": (S1_REQ, S1_PRAC, S1_ADV), "13.2": (S2_REQ, S2_PRAC, S2_ADV), "13.3": (S3_REQ, S3_PRAC, S3_ADV), "13.4": (S4_REQ, S4_PRAC, S4_ADV)}

STOPS = {
    "13.1": [stop("u13v1a", "the enormous pressure keeps it solid", mc("u13v1a_q", "M", "O1", "The thin outer layer of the Earth is the…", "crust", [("mantle", "No."), ("core", "No."), ("magma", "No.")])),
             stop("u13v1b", "dragging the plates along", mc("u13v1b_q", "H", "O1", "Which crust is denser?", "Oceanic crust", [("Continental crust", "No."), ("Both the same", "No."), ("Neither", "No.")]))],
    "13.2": [stop("u13v2a", "pushing the land up into fold mountains", mc("u13v2a_q", "M", "O2", "Plates moving apart is a…", "divergent boundary", [("convergent boundary", "Collide."), ("transform boundary", "Slide."), ("focus", "No.")])),
             stop("u13v2b", "because three plates meet there", mc("u13v2b_q", "M", "O2", "The point on the surface above an earthquake's focus is the…", "epicentre", [("vent", "No."), ("crater", "No."), ("core", "No.")])),
             stop("u13v2c", "to generate electricity", mc("u13v2c_q", "H", "O2", "Magma that reaches the surface is…", "lava", [("ash", "No."), ("crust", "No."), ("groundwater", "No.")]))],
    "13.3": [stop("u13v3a", "because warm air holds more water vapour", mc("u13v3a_q", "M", "O3", "About what percentage of air is nitrogen?", "78%", [("21%", "Oxygen."), ("1%", "No."), ("50%", "No.")])),
             stop("u13v3b", "causes global warming and climate change", mc("u13v3b_q", "H", "O3", "Which is a natural source of gases in air?", "A volcanic eruption", [("A car", "Pollution."), ("A factory", "Pollution."), ("A power plant", "Pollution.")]))],
    "13.4": [stop("u13v4a", "which can also flow back to the sea", mc("u13v4a_q", "M", "O4", "Water vapour cooling into droplets is…", "condensation", [("evaporation", "No."), ("precipitation", "No."), ("run-off", "No.")]))],
}

MINDMAP = {"id": "root", "t": "The Earth", "sec": None, "kids": [
    {"id": "st", "t": "Structure", "d": "Crust (≤60 km) • mantle (magma) • liquid outer core • solid inner core (iron, nickel) • tectonic plates on the mantle, 1–10 cm/year.", "obj": "O1", "sec": "13.1"},
    {"id": "pl", "t": "Plate boundaries", "d": "Transform → earthquakes (focus, epicentre) • divergent → volcanoes • convergent → fold mountains (Himalayas).", "obj": "O2", "sec": "13.2"},
    {"id": "at", "t": "Atmosphere", "d": "78% nitrogen, 21% oxygen, 1% CO₂ and others • humidity • volcanoes, respiration, pollution • CO₂ rising, OCO-3.", "obj": "O3", "sec": "13.3"},
    {"id": "wc", "t": "Water cycle", "d": "Evaporation → condensation → precipitation → run-off, groundwater → back to the sea.", "obj": "O4", "sec": "13.4"},
]}
