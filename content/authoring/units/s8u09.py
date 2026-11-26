# -*- coding: utf-8 -*-
"""Stage 8 Unit 9 – Pressure and Diffusion. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Physics"
BLURB = "Pressure as force over area, pressure in liquids and gases, atmospheric pressure, the particle model, and diffusion."
OBJECTIVES = {
    "O1": {"sec": "9.1", "code": "8Pf.05", "codeNote": "", "t": "Calculate pressure = force ÷ area and explain how changing the area changes the pressure."},
    "O2": {"sec": "9.2", "code": "8Pf.06", "codeNote": "liquids", "t": "Explain why pressure in a liquid increases with depth, using particles."},
    "O3": {"sec": "9.3", "code": "8Pf.06", "codeNote": "gases", "t": "Explain gas pressure and atmospheric pressure using particle collisions, and how heating or squeezing a gas changes it."},
    "O4": {"sec": "9.4", "code": "8Pf.06, 8SIC.02", "codeNote": "", "t": "Use the particle model of solids, liquids and gases to explain compression, expansion and how pressure makes diamonds."},
    "O5": {"sec": "9.5", "code": "8Pf.07", "codeNote": "", "t": "Describe diffusion in liquids and gases and the factors that make it faster."},
}
SECTIONS = [
    {"id": "9.1", "title": "Pressure", "objs": ["O1"]},
    {"id": "9.2", "title": "Pressure in liquids", "objs": ["O2"]},
    {"id": "9.3", "title": "Gas pressure", "objs": ["O3"]},
    {"id": "9.4", "title": "The particle model and pressure", "objs": ["O4"]},
    {"id": "9.5", "title": "Diffusion", "objs": ["O5"]},
]
u = Unit(8, 9)

# ---------------------------------------------------------------- 9.1
u.sec("9.1", "O1")
u.nm("r", "A rock weighing 5000 N rests on 0.5 m². What pressure does it exert?", 10000, "N/m²")
u.nm("r", "A truck exerts 10 000 N/m² over 0.4 m². What force does it exert?", 4000, "N")
u.tb("r", "Pressure = force ÷ area. Complete the table.", ["Force (N)", "Area (m²)", "Pressure (N/m²)"], [["600", "2", B(300)], ["700", "1.4", B(500)], ["900", "0.3", B(3000)]])
u.gd("r", "High or low pressure?", "Pressure", [("Point of a pushpin", "High"), ("Skis on snow", "Low"), ("Sharp knife edge", "High"), ("Wide snowboard", "Low")])
u.ex("r", "Explain why a sharp knife cuts more easily than a blunt one.", [("sharp edge has a small area", ["small area|thin"]), ("same force over smaller area – higher pressure", ["higher pressure|more pressure|greater pressure"]), ("blunt edge wider – lower pressure", ["blunt|wider|bigger area"])],
     "A sharp knife has a very thin edge with a small area, so the same force gives a higher pressure. A blunt edge is wider, so the pressure is lower and it cuts less easily.")
u.mc("r", "The unit of pressure is…", "N/m²", [("N", "That is force."), ("m²", "That is area."), ("kg", "No.")])
u.mc("r", "Why do skis stop a skier sinking into snow?", "The large area spreads the weight, reducing the pressure", [("They make the skier lighter", "No."), ("They increase the pressure", "No."), ("They melt the snow", "No.")], d="H")
u.mc("r", "The same force acts on two areas, 0.1 m² and 1 m². The pressure on 0.1 m² is…", "10 times greater", ["10 times smaller", "the same", "100 times smaller"], d="VH")
for p, r, w in [
    ("Pressure is the force acting on a…", "given area", ["given mass", "given time", "given speed"]),
    ("Pressure =", "force ÷ area", ["area ÷ force", "force × area", "mass × area"]),
    ("Which formula gives force from pressure?", "pressure × area", ["pressure ÷ area", "area ÷ pressure", "pressure + area"]),
    ("Air inside a bicycle tyre makes it firm by…", "pressing on the inner surface", ["cooling it", "making it heavier", "pulling it in"]),
    ("A pushpin goes in easily because the point has…", "a tiny area", ["a large area", "a big head", "no force"]),
    ("The smaller the area, the…", "greater the pressure", ["smaller the pressure", "smaller the force", "greater the mass"]),
    ("Knives are sharpened to keep the cutting area…", "small", ["large", "round", "soft"]),
    ("Snowboards and surfboards have large areas to…", "reduce pressure", ["increase pressure", "go faster in air", "add weight"]),
    ("A 700 N skier on 1.4 m² of skis exerts…", "500 N/m²", ["980 N/m²", "1400 N/m²", "70 N/m²"]),
    ("Geothermal energy uses pressure that pushes hot water and…", "steam to the surface", ["ice to the surface", "oil into the air", "sand upwards"]),
    ("A box weighing 600 N on 2 m² exerts…", "300 N/m²", ["1200 N/m²", "602 N/m²", "3 N/m²"]),
    ("Camels' wide feet help them on sand because they…", "reduce pressure", ["increase pressure", "make them lighter", "dig holes"]),
    ("A drawing pin's broad head…", "spreads the force on your thumb", ["concentrates the force", "makes the pin sharp", "removes the force"]),
    ("Which exerts the most pressure on the floor?", "A high-heeled shoe", ["A flat trainer", "A snowshoe", "A wide boot"]),
    ("Tractors have wide tyres so that they…", "don't sink into soft ground", ["go faster", "use more fuel", "are heavier"]),
]:
    u.mc("p", p, r, w)
u.nm("p", "A 50 N force acts on 0.01 m². What is the pressure?", 5000, "N/m²")
u.od("p", "Order from lowest to highest pressure on snow (same person).", ["Wearing skis", "Wearing snowshoes", "Wearing boots", "Standing on one heel"])
u.ms("p", "Select ALL the objects designed to INCREASE pressure.", ["Knife blade", "Nail point", "Axe edge"], ["Snowshoe", "Ski"])
u.nm("a", "An elephant weighs 40 000 N and stands on 4 feet, each 0.1 m². What pressure does it exert on the ground?", 100000, "N/m²")
u.nm("a", "What area is needed to support 1200 N at a pressure of 400 N/m²?", 3, "m²")
u.ex("a", "* Advanced. A person stands on a frozen lake and the ice starts to crack. Explain why lying flat could help.", [("lying flat spreads weight over a bigger area", ["bigger area|larger area|spread"]), ("same weight / force", ["same (weight|force)"]), ("lower pressure on the ice", ["lower pressure|less pressure|reduce"])],
     "Lying flat spreads the same weight over a much bigger area, so the pressure on the ice is lower and it is less likely to break.")
u.mc("a", "Why does a blunt knife need a bigger force to cut?", "Its edge is wider, so a bigger force is needed to reach the same pressure.", ["Blunt knives are heavier.", "Pressure does not depend on area.", "Blunt knives have less mass."], skill="Reasoning")
u.stop("making the tyre firm", "Pressure is…", "force acting on an area", ["mass of an object", "speed of particles only", "area of a surface"])
u.stop("10 thousand newtons per square metre", "Pressure =", "force ÷ area", ["area ÷ force", "force × area", "mass × area"])
u.stop("so they don't sink", "Skis reduce pressure because they have…", "a large area", ["a small area", "a sharp edge", "a heavy mass"])

# ---------------------------------------------------------------- 9.2
u.sec("9.2", "O2")
u.gd("r", "A bottle has three holes filled with water. Which spurts furthest?", "Spurt", [("Top hole", "Shortest"), ("Middle hole", "Medium"), ("Bottom hole", "Furthest")])
u.mc("r", "Pressure in a liquid…", "increases with depth", [("decreases with depth", "No."), ("is the same everywhere", "No."), ("is zero at the bottom", "No.")])
u.tb("r", "Water pressure rises by about 10 000 N/m² for every metre of depth. Complete the table.", ["Depth (m)", "Extra pressure (N/m²)"], [["1", "10 000"], ["5", B(50000)], ["40", B(400000)]])
u.ex("r", "Explain, using particles, why water pressure is greater at the bottom of a pool.", [("more water above pressing down", ["more (water|liquid) above|weight above"]), ("particles collide with walls / each other", ["collid|hit"]), ("so pressure increases with depth", ["deeper|depth"])],
     "At the bottom there is more water above pressing down. The particles are pushed together and collide with the walls more, so pressure increases with depth.")
u.mc("r", "In a liquid, particles are…", "close together but can slide past each other", [("far apart", "That is a gas."), ("fixed in place", "That is a solid."), ("not moving", "No.")])
u.mc("r", "Why do divers' ears pop as they go deeper?", "The water pressure on them increases", [("The water gets colder", "Not the cause."), ("They lose mass", "No."), ("Light is dimmer", "No.")], d="H")
u.mc("r", "Why must submarines be built from very strong materials?", "To withstand the huge water pressure at depth", [("To float better", "No."), ("To be heavier", "No."), ("To keep warm", "No.")], d="H")
u.mc("r", "Why are dams built much thicker at the bottom than at the top?", "Water pressure is greatest at the bottom", [("Water is lighter at the bottom", "No."), ("To look stronger", "No."), ("Pressure is greatest at the top", "No.")], d="VH")
for p, r, w in [
    ("Pressure in liquids is caused by…", "particles colliding with each other and the walls", ["light", "air only", "heat only"]),
    ("The deeper you go, the more liquid is…", "above you, pressing down", ["below you", "evaporating", "freezing"]),
    ("For every metre you dive, pressure rises by about…", "10 000 N/m²", ["10 N/m²", "1 N/m²", "1 000 000 N/m²"]),
    ("Divers deeper than about 40 m must rise…", "slowly, stopping on the way up", ["as fast as possible", "without stopping", "upside down"]),
    ("Rising too fast from deep dives can cause…", "decompression sickness", ["sunburn", "hunger", "frostbite only"]),
    ("Water spurts furthest from the lowest hole because…", "the pressure there is greatest", ["the hole is biggest", "the water is warmer", "air pushes it"]),
    ("Liquids can flow because their particles…", "slide past each other", ["are fixed", "are far apart", "do not move"]),
    ("Can liquids be squashed easily?", "No – their particles are close together", ["Yes, very easily", "Only when cold", "Only in bottles"]),
    ("Pressure at 2 m depth compared with 1 m is…", "greater", ["smaller", "the same", "zero"]),
    ("The pressure on a fish at 100 m is…", "much greater than at the surface", ["less than at the surface", "the same as the surface", "zero"]),
    ("Water pressure acts…", "in all directions", ["only downwards", "only upwards", "only sideways"]),
    ("A water tower is built high so that…", "water pressure in the pipes is high", ["water is cooler", "birds can drink", "it uses less water"]),
    ("Deep-sea creatures are adapted to…", "very high pressure", ["very low pressure", "no water", "bright light"]),
    ("Extra pressure at 3 m depth is about…", "30 000 N/m²", ["3 N/m²", "300 N/m²", "3 000 000 N/m²"]),
    ("Liquid pressure depends on…", "depth", ["the shape of the container only", "colour", "the time of day"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the designs that cope with high liquid pressure.", ["Thick dam walls at the bottom", "Strong submarine hulls", "Divers rising slowly"], ["Thin bottles for deep water", "Glass windows at the bottom of a dam"])
u.od("p", "Order from lowest to highest water pressure.", ["Surface of a pool", "1 m deep", "10 m deep", "100 m deep"])
u.mt("p", "Match the depth to the extra water pressure.", [("1 m", "10 000 N/m²"), ("2 m", "20 000 N/m²"), ("10 m", "100 000 N/m²")])
u.nm("a", "A diver is at 25 m. About how much extra pressure does the water exert compared with the surface?", 250000, "N/m²")
u.ex("a", "* Advanced. Explain why water pressure acts on a diver from all directions, not just from above.", [("particles move randomly in all directions", ["all directions|random|every direction"]), ("collide with every surface", ["collid|hit"]), ("so push on sides and below too", ["side|below|every"])],
     "Water particles move randomly in all directions and collide with every surface they touch, so they push on the diver from the sides and below as well as from above.")
u.mc("a", "Why do deep-sea fish often die when brought quickly to the surface?", "Their bodies are adapted to high pressure, and the sudden drop harms them.", ["The water is too cold.", "They get sunburnt.", "Pressure increases at the surface."], skill="Reasoning")
u.mc("a", "A tall and a wide container are filled to the same depth. How do the pressures at the bottom compare?", "They are the same, because pressure depends on depth.", ["The wide one is higher.", "The tall one is lower.", "It depends on colour."], skill="Reasoning")
u.stop("because the pressure there is greatest", "Water spurts furthest from the bottom hole because…", "pressure increases with depth", ["the hole is bigger", "water is warmer there", "air pushes it"])
u.stop("That's why your ears pop", "For every metre of depth, water pressure rises by about…", "10 000 N/m²", ["10 N/m²", "100 N/m²", "1 N/m²"])

# ---------------------------------------------------------------- 9.3
u.sec("9.3", "O3")
u.gd("r", "Does the gas pressure increase or decrease?", "Pressure", [("Heating a sealed gas", "Increases"), ("Squeezing gas into a smaller volume", "Increases"), ("Cooling a sealed gas", "Decreases"), ("Climbing a high mountain (air)", "Decreases")])
u.mc("r", "Gas pressure is caused by…", "particles colliding with surfaces", [("particles being still", "No."), ("light", "No."), ("gravity alone", "No.")])
u.tb("r", "Pressure in a sealed tyre at different temperatures. Complete the rise from 10 °C.", ["Temperature (°C)", "Pressure (kPa)", "Rise (kPa)"], [["10", "200", "0"], ["30", "214", B(14)], ["50", "228", B(28)]])
u.ex("r", "Explain why a beach ball from the fridge feels soft but gets harder when it warms up.", [("warming gives particles more energy", ["energy|faster"]), ("collide with walls more often and harder", ["collid|hit|often|harder"]), ("pressure increases", ["pressure"])],
     "When the air warms, its particles gain energy and move faster, so they hit the inside of the ball more often and harder. The pressure increases and the ball feels harder.")
u.mc("r", "Why does atmospheric pressure fall as you climb a mountain?", "There is less air above, and the air is less dense", [("The air gets warmer", "No."), ("Gravity gets stronger", "No."), ("There is more air above", "Reversed.")], d="H")
u.mc("r", "Gas always moves from…", "high pressure to low pressure", [("low pressure to high pressure", "Reversed."), ("cold to hot only", "No."), ("up to down only", "No.")])
u.mc("r", "Why does air flow into your lungs when your chest expands?", "The pressure in the lungs drops below the air pressure outside", [("Lungs suck air with muscles", "Not exactly."), ("Air pressure inside rises", "No."), ("Air is pulled by gravity", "No.")], d="H")
u.mc("r", "Squeezing a gas into a smaller volume raises its pressure because…", "particles hit the walls more often", [("particles get bigger", "No."), ("particles slow down", "No."), ("there are fewer particles", "No.")], d="VH")
for p, r, w in [
    ("Gas particles are always…", "moving fast and colliding", ["still", "in fixed positions", "touching in rows"]),
    ("An inflated balloon holds its shape because…", "more particles push on the inside than outside", ["the rubber is stiff", "air is solid", "gravity pulls it"]),
    ("More gas particles in the same space means…", "more collisions and more pressure", ["less pressure", "no change", "lower temperature"]),
    ("Heating a gas makes its particles…", "move faster", ["move slower", "stop", "get smaller"]),
    ("Sitting on an exercise ball…", "squeezes the gas and raises the pressure", ["lowers the pressure", "heats the gas a lot", "removes particles"]),
    ("Air pressing on us all the time is…", "atmospheric pressure", ["liquid pressure", "water pressure", "solid pressure"]),
    ("Near Earth's surface the air is denser because…", "gravity pulls particles closer together", ["it is colder", "there is less air", "the Sun heats it"]),
    ("At sea level there is…", "more air above, pressing down", ["less air above", "no air", "only water vapour"]),
    ("Wind is caused by air moving from…", "high pressure to low pressure", ["low to high pressure", "cold to hot only", "night to day"]),
    ("Atmospheric pressure at the top of a mountain is…", "lower", ["higher", "the same", "zero"]),
    ("A sealed can heated in a fire may explode because…", "the gas pressure inside rises", ["the gas cools", "particles stop", "metal melts first"]),
    ("Gas pressure is measured in…", "N/m² (or kPa)", ["kg", "metres", "seconds"]),
    ("Fewer gas particles in a balloon means…", "lower pressure", ["higher pressure", "same pressure", "a bigger balloon"]),
    ("Pumping more air into a tyre…", "increases the pressure", ["decreases the pressure", "cools the tyre", "removes air"]),
    ("When you breathe in, lung pressure is…", "lower than outside", ["higher than outside", "the same as outside", "zero"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the ways to increase the pressure of a gas in a sealed container.", ["Heat it", "Squeeze it into a smaller volume", "Add more gas"], ["Cool it", "Let some gas out"])
u.od("p", "Order the steps when a sealed gas is heated.", ["Particles gain energy", "Particles move faster", "They hit the walls more often and harder", "Pressure increases"])
u.mt("p", "Match the cause to the effect on gas pressure.", [("Heating", "pressure rises"), ("Cooling", "pressure falls"), ("More particles", "pressure rises")])
u.ex("a", "* Advanced. Explain why aerosol cans carry the warning 'Do not heat'.", [("gas inside at high pressure", ["high pressure|pressurised"]), ("heating makes particles faster, pressure rises more", ["heat.*(faster|pressure)|pressure rises|increase"]), ("can could burst / explode", ["burst|explode"])],
     "The gas in an aerosol is already at high pressure. Heating makes the particles move faster and hit the can harder and more often, so the pressure rises further and the can could burst.")
u.mc("a", "Why do packets of crisps puff up when taken up a mountain?", "Outside air pressure is lower, so the gas inside pushes the packet out.", ["The crisps expand.", "Air gets heavier.", "Inside pressure falls."], skill="Reasoning")
u.nm("a", "A tyre is at 200 kPa. Heating raises the pressure by 7 kPa for every 10 °C. What is the pressure after a 30 °C rise?", 221, "kPa")
u.mc("a", "On a weather map, wind blows from area A (1030 units) to area B (990 units). Why?", "Air moves from high pressure to low pressure.", ["Air moves from low to high pressure.", "Wind always blows north.", "Pressure has no effect."], skill="Reasoning")
u.stop("more collisions and more pressure", "Gas pressure is caused by…", "particles colliding with surfaces", ["particles sitting still", "the colour of the gas", "light"])
u.stop("warm it up and it gets harder", "Heating a gas in a sealed container makes the pressure…", "increase", ["decrease", "stay the same", "become zero"])
u.stop("That's what causes wind, too", "Gas always moves from…", "high pressure to low pressure", ["low to high pressure", "cold to hot", "down to up"])

# ---------------------------------------------------------------- 9.4
u.sec("9.4", "O4")
u.gd("r", "Solid, liquid or gas?", "State", [("Particles vibrate in fixed places", "Solid"), ("Particles slide past each other", "Liquid"), ("Particles far apart and fast", "Gas"), ("Easy to compress", "Gas")])
u.mc("r", "Why can gases be compressed easily but liquids cannot?", "Gas particles are far apart; liquid particles are close together", [("Gas particles are bigger", "No."), ("Liquids have no particles", "No."), ("Gases are heavier", "No.")])
u.tb("r", "Heating a metal rod. Complete the expansion.", ["Temperature (°C)", "Length (mm)", "Longer than at 20 °C by (mm)"], [["20", "1000.0", "0"], ["220", "1002.4", B(2.4)]])
u.ex("r", "Explain why a substance expands when it is heated.", [("particles gain energy", ["energy"]), ("move / vibrate faster", ["faster"]), ("spread further apart", ["further apart|spread|more space"])],
     "Heating gives the particles more energy, so they move or vibrate faster and spread further apart, so the substance takes up more space – it expands.")
u.mc("r", "Natural diamonds form deep in the mantle because of…", "enormous pressure and high temperature", [("low pressure and cold", "No."), ("water and light", "No."), ("fast cooling in air", "No.")])
u.mc("r", "When enough heat is added, particles break away from each other and the substance…", "changes state", ["shrinks", "becomes a new element", "loses mass"], d="H")
u.mc("r", "About what percentage of synthetic diamonds are made using high pressure and high temperature?", "About 99%", ["About 1%", "About 50%", "None"], d="H")
u.mc("r", "Why can expanding or changing state be dangerous in a sealed container?", "It can greatly increase the pressure inside", [("It lowers the pressure", "No."), ("It removes particles", "No."), ("It cools the container", "No.")], d="VH")
for p, r, w in [
    ("In a solid, particles are held by…", "strong forces", ["no forces", "weak forces only", "magnetism"]),
    ("In a solid, particles…", "vibrate in place", ["move freely", "are far apart", "flow"]),
    ("Liquids flow because forces between particles are…", "weaker", ["stronger", "zero", "magnetic"]),
    ("In a gas, particles move…", "fast in all directions", ["slowly in rows", "only upwards", "not at all"]),
    ("Melting happens when particles…", "gain enough energy to break from fixed positions", ["lose energy", "stop moving", "join tightly"]),
    ("Boiling happens when particles…", "gain enough energy to escape as a gas", ["lose energy", "vibrate in place", "become solid"]),
    ("Diamonds are made of…", "carbon atoms", ["oxygen atoms", "water", "iron"]),
    ("Diamonds form in the Earth's…", "mantle", ["atmosphere", "oceans", "crust surface"]),
    ("Lab diamonds have been grown at normal pressure using…", "a liquid metal alloy at high temperature", ["ice", "sea water", "sunlight only"]),
    ("Lab-grown diamonds have many…", "industrial uses", ["food uses", "medical vitamins", "fuel uses"]),
    ("Expansion means taking up…", "more space", ["less space", "less mass", "no space"]),
    ("Which state is hardest to compress?", "Solid", ["Gas", "Air", "Steam"]),
    ("The particle model describes…", "how particles are arranged and move", ["the colour of substances", "the price of materials", "the shape of atoms only"]),
    ("Gaps are left in railway tracks because…", "metal expands when heated", ["metal shrinks in summer", "to save metal", "for drainage"]),
    ("Heating a liquid in a thermometer makes it…", "expand up the tube", ["shrink", "freeze", "become solid"]),
]:
    u.mc("p", p, r, w)
u.mt("p", "Match the change of state to what happens to particles.", [("Melting", "break free from fixed positions"), ("Boiling", "escape as a gas"), ("Freezing", "lock into fixed positions")])
u.ms("p", "Select ALL the properties of gases.", ["Easy to compress", "Particles far apart", "Fill their container"], ["Fixed shape", "Particles in fixed rows"])
u.od("p", "Order the states by how far apart particles are, closest first.", ["Solid", "Liquid", "Gas"])
u.ex("a", "* Advanced. Explain why a sealed bottle of water left in a freezer might crack.", [("water expands when it freezes", ["expand"]), ("ice takes up more space", ["more space|bigger volume|larger"]), ("pressure on the bottle walls", ["pressure|push|force"])],
     "Water expands as it freezes, so the ice takes up more space than the liquid. It pushes hard on the walls, and the high pressure can crack the bottle.")
u.mc("a", "Why do bridges have expansion joints?", "The metal expands in hot weather and needs room to move.", ["To let water through", "To make the bridge lighter", "Metal shrinks when hot"], skill="Reasoning")
u.mc("a", "Why is graphite soft but diamond very hard, though both are carbon?", "The carbon atoms are arranged differently.", ["Diamond has more protons.", "Graphite is a gas.", "Diamond contains iron."], skill="Reasoning")
u.nm("a", "A 1000 mm metal rod expands by 0.012 mm for every 1 °C. How much longer is it after a 50 °C rise?", 0.6, "mm", tol=0.01)
u.stop("vibrating in place", "In a solid, particles…", "vibrate in fixed positions", ["move freely", "are far apart", "flow"])
u.stop("so gases are easy to compress", "Gases are easy to compress because particles are…", "far apart", ["close together", "fixed", "very heavy"])
u.stop("into diamond's special crystal structure", "Natural diamonds form under…", "high pressure and high temperature", ["low pressure and cold", "water", "light"])

# ---------------------------------------------------------------- 9.5
u.sec("9.5", "O5")
u.gd("r", "Does each change make diffusion faster or slower?", "Diffusion", [("Higher temperature", "Faster"), ("Heavier particles", "Slower"), ("Bigger spaces between particles", "Faster"), ("Liquid instead of gas", "Slower")])
u.mc("r", "Diffusion is the spreading of particles from…", "high concentration to low concentration", [("low to high concentration", "Reversed."), ("cold to hot", "No."), ("solid to gas", "No.")])
u.tb("r", "Time for a smell to cross a room. Complete the difference from 10 °C.", ["Temperature (°C)", "Time (s)", "Faster than at 10 °C by (s)"], [["10", "60", "0"], ["20", "45", B(15)], ["30", "32", B(28)]])
u.ex("r", "Explain why diffusion is much faster in gases than in liquids.", [("gas particles move faster", ["faster"]), ("bigger spaces between particles", ["space|far apart|gaps"]), ("fewer collisions slowing them", ["collid|bump|in the way"])],
     "Gas particles move faster and have much bigger spaces between them, so they spread out with fewer collisions getting in the way.")
u.mc("r", "Why does diffusion happen on its own?", "Particles are always moving", [("Someone stirs it", "Not needed."), ("Gravity pulls particles", "No."), ("Particles are still", "No.")])
u.mc("r", "Diffusion is not the same as…", "dissolving", ["spreading out", "mixing by particle movement", "particles moving randomly"], d="H")
u.mc("r", "A tea bag in water. Why do the tea particles eventually spread evenly?", "They move randomly from high to low concentration until evenly mixed", [("Water pushes them up", "No."), ("They are heavier than water", "No."), ("Tea particles repel each other only", "No.")], d="H")
u.mc("r", "Why does a stink bomb smell reach you faster on a hot day?", "Particles have more energy and move faster", [("Hot air is heavier", "No."), ("The smell particles get bigger", "No."), ("Diffusion stops when cold", "Slower, not stopped.")], d="VH")
for p, r, w in [
    ("You smell perfume across a room because of…", "diffusion", ["condensation", "freezing", "filtration"]),
    ("Diffusion happens in…", "liquids and gases", ["only solids", "only metals", "nowhere"]),
    ("Lighter particles diffuse…", "faster", ["slower", "not at all", "only in solids"]),
    ("Higher temperature makes diffusion…", "faster", ["slower", "stop", "unchanged"]),
    ("Particles in liquids and gases move…", "freely and collide randomly", ["in straight rows", "not at all", "only upwards"]),
    ("Diffusion continues until particles are…", "evenly mixed", ["all in one place", "solid", "gone"]),
    ("Diffusion is slow in liquids because particles are…", "close together", ["far apart", "very light", "very hot"]),
    ("A drop of ink in still water…", "slowly spreads out", ["stays as a drop", "sinks and stops", "turns into gas"]),
    ("Oxygen moves from the lungs into the blood by…", "diffusion", ["filtration", "evaporation", "freezing"]),
    ("Diffusion in solids is…", "extremely slow or does not happen", ["very fast", "the fastest", "the same as gases"]),
    ("The smell of cooking spreads through a house by…", "diffusion", ["condensation", "melting", "freezing"]),
    ("Which diffuses fastest?", "A light gas at high temperature", ["A heavy gas at low temperature", "A solid", "A cold liquid"]),
    ("Bigger spaces between particles mean…", "faster diffusion", ["slower diffusion", "no diffusion", "freezing"]),
    ("Concentration means…", "how many particles are in a given space", ["the colour of particles", "the speed of light", "the mass of a container"]),
    ("Diffusion needs…", "particles that can move", ["fixed particles", "a magnet", "electricity"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the examples of diffusion.", ["Perfume spreading through a room", "Tea spreading in water", "Oxygen entering the blood"], ["Water freezing", "Sand being sieved"])
u.od("p", "Order from fastest to slowest diffusion.", ["Hot gas", "Cold gas", "Liquid", "Solid"])
u.mt("p", "Match the factor to its effect on diffusion.", [("Higher temperature", "faster"), ("Heavier particles", "slower"), ("Bigger spaces", "faster")])
u.ex("a", "* Advanced. Plan an investigation to see how temperature affects how fast food colouring spreads in water.", [("change temperature of water", ["temperature"]), ("same volume / same drop / still water", ["same (volume|amount|drop|size)"]), ("time until evenly coloured", ["time|until"])],
     "Use beakers of water at different temperatures with the same volume. Add one drop of the same food colouring without stirring and time how long until the colour is evenly spread.")
u.mc("a", "Why do we smell a gas leak before we can see any change?", "Gas particles diffuse quickly through the air and reach our nose.", ["Gas is solid.", "Light carries smells.", "Diffusion only happens in liquids."], skill="Reasoning")
u.gr("a", "* Advanced. Time for colour to spread at different temperatures. Plot the points.", {"label": "Temperature (°C)", "min": 0, "max": 80, "step": 20}, {"label": "Time (min)", "min": 0, "max": 20, "step": 5}, [[20, 16], [40, 10], [60, 6], [80, 4]])
u.mc("a", "What pattern does the colour-spreading graph show?", "The higher the temperature, the shorter the time.", ["Temperature has no effect.", "Higher temperature takes longer.", "The time doubles every 20 °C."], skill="Data")
u.stop("because particles are always moving", "Diffusion is particles spreading from…", "high to low concentration", ["low to high concentration", "cold to hot", "liquid to solid"])
u.stop("evenly mixed with the water particles", "Diffusion happens in…", "liquids and gases", ["solids only", "metals only", "a vacuum only"])
u.stop("diffusion isn't the same as dissolving", "Diffusion is faster when the temperature is…", "higher", ["lower", "zero", "the same always"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Pressure and diffusion", "sec": None, "kids": [
    {"id": "pr", "t": "Pressure", "d": "Pressure = force ÷ area • N/m² • Small area → high pressure", "obj": "O1", "sec": "9.1"},
    {"id": "li", "t": "Liquid pressure", "d": "Increases with depth • Dams, submarines, divers", "obj": "O2", "sec": "9.2"},
    {"id": "ga", "t": "Gas pressure", "d": "Particle collisions • Heating or squeezing raises it", "obj": "O3", "sec": "9.3"},
    {"id": "at", "t": "Atmospheric pressure", "d": "Falls with height • High → low pressure • Breathing and wind", "obj": "O3", "sec": "9.3"},
    {"id": "pm", "t": "Particle model", "d": "Solid, liquid, gas • Expansion • Changes of state • Diamonds", "obj": "O4", "sec": "9.4"},
    {"id": "di", "t": "Diffusion", "d": "High → low concentration • Faster: hot, light, big spaces • Gases > liquids", "obj": "O5", "sec": "9.5"},
]}
