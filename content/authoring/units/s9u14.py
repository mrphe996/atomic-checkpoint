# -*- coding: utf-8 -*-
"""Stage 9 Unit 14 – Astronomy. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Earth and Space"
BLURB = "What asteroids are and how an asteroid impact caused a mass extinction, the collision theory of the Moon's formation, and how stars are born in nebulae."
OBJECTIVES = {
    "O1": {"sec": "14.1", "code": "9ESs.01", "codeNote": "", "t": "Describe asteroids and explain how an asteroid collision caused a mass extinction."},
    "O2": {"sec": "14.2", "code": "9ESs.02", "codeNote": "", "t": "Describe the collision theory of the Moon's formation and the evidence for it."},
    "O3": {"sec": "14.3", "code": "9ESs.03", "codeNote": "", "t": "Describe nebulae and how stars form in stellar nurseries."},
}
SECTIONS = [
    {"id": "14.1", "title": "Asteroid collision with Earth", "objs": ["O1"]},
    {"id": "14.2", "title": "The formation of the Moon", "objs": ["O2"]},
    {"id": "14.3", "title": "Nebulae: where stars are born", "objs": ["O3"]},
]
u = Unit(9, 14)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 14.1
u.sec("14.1", "O1")
u.od("r", "Order the events after the asteroid impact 66 million years ago.", ["Asteroid strikes the Gulf of Mexico", "Dust fills the atmosphere", "Sunlight is blocked", "Plants cannot photosynthesise", "Food chains collapse", "Most dinosaurs die out"])
u.tb("r", "Asteroid sizes. Complete the table.", ["Asteroid", "Diameter (km)", "Diameter (m)"], [["Small", "0.002", B(2)], ["Largest", "940", B(940000)]])
u.gd("r", "True or false about asteroids?", "Answer", [("Most orbit between Mars and Jupiter", "True"), ("They are made of gas", "False"), ("Gravity can pull them onto planets", "True"), ("All are larger than 1000 km", "False")])
u.ex("r", "Explain how an asteroid impact could cause a mass extinction.", [("dust blocked sunlight", ["dust|block"]), ("plants could not photosynthesise / died", ["photosynth|plant"]), ("temperatures dropped, food chains collapsed", ["temperature|cold|food chain|food"])],
     "The impact threw dust into the atmosphere that blocked sunlight. Plants could not photosynthesise and died, temperatures dropped, and food chains collapsed, so many species died out.")
u.mc("r", "Asteroids are…", "rocky objects orbiting the Sun", ["balls of gas", "stars", "moons of Jupiter only"])
u.mc("r", "Where are most asteroids found?", "In the asteroid belt between Mars and Jupiter", ["Beyond Neptune", "Inside the Sun", "Between Earth and the Moon"])
u.mc("r", "What evidence in 2016 confirmed the impact theory?", "Asteroid dust was found inside the crater", ["A living dinosaur was found", "The asteroid was seen in a telescope", "Fossils of birds were found"], d="H")
u.mc("r", "Why do scientists say dinosaurs are not completely extinct?", "Small dinosaurs survived and evolved into birds", ["Large dinosaurs still live in jungles", "Dinosaurs live on the Moon", "Crocodiles are dinosaurs"], d="VH")
mcs("p", [
    ("The asteroid struck Earth about…", "66 million years ago", ["66 thousand years ago", "6.6 billion years ago", "660 years ago"]),
    ("The impact crater is in the…", "Gulf of Mexico", ["Sahara Desert", "Arctic Ocean", "Himalayas"]),
    ("The crater is about … wide.", "200 km", ["2 km", "20 m", "2000 km"]),
    ("Asteroids range in size from about 2 m to nearly…", "1000 km", ["10 km", "1 m", "100 000 km"]),
    ("A mass extinction is when…", "many species die out in a short time", ["one animal dies", "a population grows", "a new species forms"]),
    ("Dust in the atmosphere made temperatures…", "drop", ["rise sharply", "stay the same", "reach boiling point"]),
    ("Plants could not photosynthesise because…", "sunlight was blocked", ["there was too much water", "oxygen ran out", "the soil froze instantly"]),
    ("Today's birds evolved from…", "small dinosaurs", ["fish", "mammals", "insects"]),
    ("Gravity can pull asteroids onto…", "planets and moons", ["the Sun only", "nothing", "stars only"]),
    ("Scientists dream of mining asteroids for…", "materials", ["water vapour only", "oxygen gas", "sunlight"]),
    ("When herbivores lost their food, carnivores…", "also starved", ["thrived", "became plants", "were unaffected"]),
    ("Craters on the Moon are mostly caused by…", "impacts from asteroids and meteoroids", ["volcanoes only", "water", "wind"]),
    ("Asteroids are … than planets.", "smaller", ["bigger", "hotter", "brighter"]),
    ("Space agencies track asteroids to…", "spot any that may hit Earth", ["find aliens", "measure tides", "count stars"]),
    ("An idea becomes accepted when it is supported by…", "evidence", ["opinion", "a single guess", "a vote"]),
])
u.mt("p", "Match the term to its meaning.", [("Asteroid", "rocky object orbiting the Sun"), ("Asteroid belt", "region between Mars and Jupiter"), ("Mass extinction", "many species die out together")])
u.ms("p", "Select ALL the effects of the asteroid impact.", ["Dust blocked sunlight", "Temperatures dropped", "Plants died"], ["Oceans boiled away completely", "The Sun went out"])
u.gd("p", "Survived or died out after the impact?", "Fate", [("Large dinosaurs like T. rex", "Died out"), ("Small feathered dinosaurs", "Survived")])
u.ex("a", "Suggest why some small animals survived the impact while large dinosaurs did not.", [("small animals need less food", ["less food|small"]), ("could shelter / burrow", ["shelter|burrow|hide|underground"]), ("could eat seeds, insects or dead matter", ["seed|insect|dead|scaveng"])],
     "Small animals needed less food, could shelter in burrows or water, and could survive on seeds, insects or dead matter, while large dinosaurs needed huge amounts of plants or prey.")
u.nm("a", "The impact was 66 million years ago. The first humans appeared about 300 000 years ago. How many times longer ago was the impact?", 220, "times")
u.mc("a", "Why do scientists study craters on the Moon to learn about asteroid impacts on Earth?", "The Moon has no weather or plates to erase its craters", ["The Moon has more asteroids", "Earth has no craters", "The Moon is made of asteroids"], skill="Reasoning")
u.mc("a", "Which observation would best support the idea that an impact caused an extinction?", "A layer of asteroid material at the same rock layer where fossils disappear", ["A new species of bird today", "A volcano erupting now", "Rain in the Gulf of Mexico"], skill="Evidence")
u.stop("mining asteroids for materials one day", "When did a huge asteroid strike Earth?", "66 million years ago", ["66 years ago", "6 billion years ago", "6000 years ago"])
u.stop("gravity can pull some onto planets and moons", "Most asteroids are found…", "between Mars and Jupiter", ["beyond Neptune", "inside the Sun", "on Earth"])
u.stop("so plants couldn't photosynthesise and temperatures dropped", "Dust from the impact…", "blocked sunlight", ["added heat", "made rain", "made oxygen"])

# ---------------------------------------------------------------- 14.2
u.sec("14.2", "O2")
u.od("r", "Order the collision theory of the Moon's formation.", ["Solar System forms", "Theia smashes into the young Earth", "Rock and dust are blasted into space", "Debris clumps together", "The Moon cools"])
u.gd("r", "Evidence for the collision theory?", "Supports theory?", [("Moon rocks are very similar to Earth rocks", "Yes"), ("The Moon has an iron core", "Yes"), ("The Moon's surface was once molten", "Yes"), ("The Moon has seasons", "No")])
u.tb("r", "Densities. Complete the comparison.", ["Body", "Density (g/cm³)", "Difference from Earth"], [["Earth", "5.5", "0"], ["Moon", "3.3", B(2.2)]])
u.ex("r", "Explain why Moon rocks brought back by Apollo missions support the collision theory.", [("Moon rocks very similar to Earth rocks", ["similar|same"]), ("suggests Moon made from Earth material", ["earth material|from earth|blasted"]), ("debris from collision formed Moon", ["debris|collision|theia"])],
     "Apollo Moon rocks are very similar to Earth rocks, which suggests the Moon formed from material blasted out of the young Earth when Theia collided with it.")
u.mc("r", "The planet that hit the young Earth is called…", "Theia", ["Mars", "Venus", "Gaia"])
u.mc("r", "Theia was about the size of…", "Mars", ["Jupiter", "the Sun", "a small asteroid"])
u.mc("r", "The collision happened about…", "4.5 billion years ago", ["66 million years ago", "4.5 million years ago", "450 years ago"], d="H")
u.mc("r", "Why is the Moon less dense than Earth?", "It formed mostly from Earth's outer, rocky layers, with only a small iron core", ["It is hollow", "It is made of gas", "It has more iron than Earth"], d="VH")
mcs("p", [
    ("The Moon is Earth's natural…", "satellite", ["star", "planet", "asteroid belt"]),
    ("The collision theory says the Moon formed from…", "debris from a giant impact", ["a captured comet", "a piece of the Sun", "gas from Jupiter"]),
    ("The debris … together to form the Moon.", "clumped", ["evaporated", "melted into the Sun", "dissolved"]),
    ("The Moon's surface was once…", "molten", ["frozen solid", "covered in oceans", "made of gas"]),
    ("Apollo missions brought back…", "Moon rocks", ["Mars rocks", "comet ice", "asteroid dust only"]),
    ("The Moon has a small…", "iron core", ["water core", "gas core", "gold core"]),
    ("The young Earth was struck soon after the … formed.", "Solar System", ["Milky Way", "Universe", "dinosaurs"]),
    ("The Moon is … dense than Earth.", "less", ["more", "equally", "infinitely more"]),
    ("A scientific theory is a well-tested…", "explanation supported by evidence", ["guess", "opinion", "story"]),
    ("Theia's impact blasted rock and dust into…", "space", ["the Sun", "the oceans", "Earth's core"]),
    ("The Moon cooled from a…", "hot, molten state", ["frozen state", "gas cloud only", "liquid water"]),
    ("Which is NOT evidence for the collision theory?", "The Moon reflects sunlight", ["Similar rocks", "Iron core", "Once-molten surface"]),
    ("Scientists use … to test how a giant impact could form a moon.", "computer simulations", ["cooking", "weather balloons", "microscopes only"]),
    ("Gravity pulled the debris into a…", "ball", ["flat sheet", "ring forever", "cube"]),
    ("Earth's Moon is unusually large compared with…", "its planet", ["the Sun", "Jupiter", "galaxies"]),
])
u.mt("p", "Match the evidence to what it suggests.", [("Similar rocks", "Moon made of Earth material"), ("Small iron core", "mostly outer layers were blasted off"), ("Once-molten surface", "huge energy from impact")])
u.ms("p", "Select ALL the evidence for the collision theory.", ["Moon rocks match Earth rocks", "Moon's iron core", "Moon less dense than Earth"], ["Moon has phases", "Moon causes tides"])
u.gd("p", "True or false?", "Answer", [("Theia was a Mars-sized planet", "True"), ("The Moon formed 66 million years ago", "False"), ("The Moon is denser than Earth", "False")])
u.ex("a", "Explain how the Moon's small iron core and lower density support the collision theory.", [("impact blasted mainly Earth's outer rocky layers", ["outer|rocky|mantle|crust"]), ("Earth's iron was mostly in its core – stayed", ["iron.*(core|stayed)|core"]), ("so the Moon has little iron, lower density", ["little iron|small core|less dense"])],
     "Earth's heavy iron had already sunk into its core, so the impact blasted out mostly outer rocky material. The Moon therefore has only a small iron core and a lower density than Earth.")
u.nm("a", "The Moon's diameter is about 3500 km and Earth's about 12 700 km. To one decimal place, how many times wider is Earth?", 3.6, "times", tol=0.1)
u.mc("a", "Why do scientists still call it the collision 'theory'?", "It is the best explanation of the evidence but could be revised with new evidence", ["It has no evidence", "It has been proven wrong", "It is a guess"], skill="Reasoning")
u.mc("a", "If the Moon had been a captured asteroid, what would we expect?", "Its rocks would be very different from Earth's", ["Its rocks would match Earth's", "It would have a huge iron core", "It would be molten now"], skill="Reasoning")
u.stop("blasting rock and dust into space", "The collision theory says the Moon formed when … hit the young Earth.", "Theia", ["Mars", "an asteroid 66 million years ago", "a comet"])
u.stop("and its surface was once molten", "Which evidence supports the collision theory?", "Moon rocks are similar to Earth rocks", ["The Moon has phases", "The Moon causes tides", "The Moon reflects light"])

# ---------------------------------------------------------------- 14.3
u.sec("14.3", "O3")
u.od("r", "Order the stages of star formation.", ["Nebula of dust and gas", "A clump forms", "Gravity pulls in more matter", "It collapses and heats up", "Core particles react", "A new star shines"])
u.gd("r", "Stellar nursery or remains of an exploded star?", "Type", [("Orion Nebula", "Stellar nursery"), ("Crab Nebula", "Remains of exploded star")])
u.tb("r", "Composition of a typical nebula (simplified). Complete the table.", ["Substance", "Percentage (%)"], [["Hydrogen", "74"], ["Helium", "24"], ["Other elements and dust", B(2)]])
u.ex("r", "Describe how a star forms in a stellar nursery.", [("dust and gas clump together", ["clump|dust|gas"]), ("gravity pulls in more matter, collapses", ["gravity|collapse"]), ("heats up until core particles react – star shines", ["heat|react|fusion|shine"])],
     "In a nebula, dust and gas form a clump whose gravity pulls in more matter. It collapses and heats up until particles in the core react, and a new star begins to shine.")
u.mc("r", "A nebula is…", "a giant cloud of dust and gas", ["a type of planet", "a black hole", "a comet"])
u.mc("r", "Nebulae are mostly made of…", "hydrogen", ["oxygen", "iron", "carbon dioxide"])
u.mc("r", "What force causes a clump in a nebula to collapse?", "Gravity", ["Magnetism", "Friction", "Wind"], d="H")
u.mc("r", "The Crab Nebula formed from…", "an exploded star", ["a newborn star", "the Moon", "an asteroid impact"], d="VH")
mcs("p", [
    ("Places where stars are born are called…", "stellar nurseries", ["black holes", "asteroid belts", "galaxies only"]),
    ("Stars can live for…", "billions of years", ["a few days", "a hundred years", "one year"]),
    ("A collapsing clump of gas…", "heats up", ["cools down", "freezes", "disappears"]),
    ("A new star begins to shine when particles in its core…", "react", ["freeze", "stop moving", "escape"]),
    ("The Orion Nebula is a…", "stellar nursery", ["dead planet", "comet", "moon"]),
    ("Some nebulae are the remains of…", "exploded stars", ["moons", "asteroids", "planets"]),
    ("Gravity pulls … into a clump.", "more matter", ["light", "sound", "heat only"]),
    ("Our Sun formed from a…", "nebula", ["comet", "black hole", "planet"]),
    ("The main gas in stars is…", "hydrogen", ["oxygen", "nitrogen", "carbon dioxide"]),
    ("Nebulae can be seen with…", "telescopes", ["microscopes", "thermometers", "magnets"]),
    ("Stars are … objects.", "luminous", ["non-luminous", "solid", "cold"]),
    ("Material from exploded stars can form…", "new stars and planets", ["nothing", "only black holes", "only comets"]),
    ("As a clump collapses, its temperature…", "rises", ["falls", "stays the same", "becomes zero"]),
    ("The young star at the centre of a collapsing cloud is a…", "protostar", ["planet", "moon", "comet"]),
    ("Heavier elements in our bodies were made in…", "stars", ["oceans", "plants", "volcanoes"]),
])
u.mt("p", "Match the term to its meaning.", [("Nebula", "cloud of dust and gas"), ("Stellar nursery", "region where stars form"), ("Protostar", "young star still forming")])
u.ms("p", "Select ALL the things needed for a star to form.", ["Gas and dust", "Gravity", "High temperature in the core"], ["Water", "Sunlight from another star"])
u.gd("p", "True or false?", "Answer", [("Nebulae are mostly hydrogen", "True"), ("Stars form quickly in a few days", "False"), ("Some nebulae come from exploded stars", "True")])
u.ex("a", "Explain why we say we are 'made of star stuff'.", [("heavier elements made inside stars", ["made in stars|inside stars|stars make"]), ("exploding stars scatter them into nebulae", ["explod|scatter|nebula"]), ("Solar System and Earth formed from that material", ["solar system|earth|formed|us"])],
     "Heavier elements such as carbon and iron are made inside stars. When stars explode, these are scattered into nebulae, and our Solar System, Earth and our bodies formed from that material.")
u.nm("a", "A star will live 10 billion years. It is 4.6 billion years old. How many billion years does it have left?", 5.4, "billion years")
u.mc("a", "Why do astronomers often use infrared telescopes to study stellar nurseries?", "Infrared passes through the dust that hides young stars", ["Infrared is visible light", "Dust blocks infrared", "Stars give out no visible light"], skill="Reasoning")
u.mc("a", "A nebula is mostly hydrogen. Why does this matter for star formation?", "Hydrogen is the fuel that reacts in a star's core", ["Hydrogen blocks gravity", "Hydrogen is heavy", "Hydrogen cools the star"], skill="Reasoning")
u.stop("the remains of exploded stars", "A nebula is a giant cloud of…", "dust and gas", ["water", "rock", "ice only"])
u.stop("Stars can live for billions of years!", "A clump in a nebula collapses because of…", "gravity", ["magnetism", "wind", "friction"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Astronomy", "sec": None, "kids": [
    {"id": "as", "t": "Asteroids", "d": "Rocky, orbit the Sun • Belt between Mars and Jupiter", "obj": "O1", "sec": "14.1"},
    {"id": "ex", "t": "Mass extinction", "d": "Impact 66 million years ago • Dust blocked sunlight • Dinosaurs died out, birds survived", "obj": "O1", "sec": "14.1"},
    {"id": "mo", "t": "Moon's formation", "d": "Theia hit young Earth • Debris clumped • Evidence: similar rocks, iron core, density", "obj": "O2", "sec": "14.2"},
    {"id": "ne", "t": "Nebulae", "d": "Dust and gas, mostly hydrogen • Nurseries and remains of stars", "obj": "O3", "sec": "14.3"},
    {"id": "st", "t": "Star birth", "d": "Clump • Gravity • Collapse and heat • Core reacts • Star shines", "obj": "O3", "sec": "14.3"},
]}
