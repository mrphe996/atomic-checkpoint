# -*- coding: utf-8 -*-
"""Stage 7 Unit 7 – Properties of Materials. Written by the Atomic teaching team."""
from c_kit import *

STRAND = "Chemistry"
BLURB = "Physical and chemical properties of materials, how metals and non-metals differ, and why alloys are harder than pure metals."

OBJECTIVES = {
    "O1": {"sec": "7.1", "code": "7Cp.01", "codeNote": "physical properties", "t": "Describe physical properties: strength, hardness, ductility, malleability, melting point, conductivity and density."},
    "O2": {"sec": "7.2", "code": "7Cp.01", "codeNote": "chemical properties", "t": "Describe chemical properties: reactivity, flammability, acidity, corrosiveness and toxicity."},
    "O3": {"sec": "7.3", "code": "7Cp.05, 7Cm.03", "codeNote": "", "t": "Compare the physical properties of metals and non-metals, including exceptions such as carbon."},
    "O4": {"sec": "7.4", "code": "7Cp.06, 7Cp.07", "codeNote": "", "t": "Explain why alloys have different properties from pure metals and give uses of alloys."},
}

SECTIONS = [
    {"id": "7.1", "title": "Physical properties", "objs": ["O1"]},
    {"id": "7.2", "title": "Chemical properties", "objs": ["O2"]},
    {"id": "7.3", "title": "Metals and non-metals", "objs": ["O3"]},
    {"id": "7.4", "title": "Alloys", "objs": ["O4"]},
]

S1_REQ = [
    gd("u7s1r1", "M", "O1", "Physical or chemical property?", ["Type"],
       [("Hardness", ["Physical"]), ("Melting point", ["Physical"]), ("Flammability", ["Chemical"]), ("Density", ["Physical"]), ("Reactivity", ["Chemical"])], skill="Data"),
    mt("u7s1r2", "M", "O1", "Match the property to its meaning.", [("Ductile", "can be stretched into wires"), ("Malleable", "can be hammered or rolled into shape"), ("Flexible", "bends without breaking"), ("Hard", "not easily scratched"), ("Strong", "withstands forces without breaking")]),
    tb("u7s1r3", "H", "O1", "Mohs scale: a material scratches anything with a LOWER number. Complete the table.", ["Pair", "Fingernail 2.5 vs glass 5.5 – which scratches?"],
       [["Answer (write the hardness number of the winner)", B(5.5)]], skill="Data"),
    mc("u7s1r4", "H", "O1", "A steel nail (6.5) and glass (5.5): which statement is correct?", ("The nail scratches the glass.", "Correct – higher number scratches lower."),
       [("The glass scratches the nail.", "Lower cannot scratch higher."), ("Neither can scratch the other.", "No."), ("Both scratch each other equally.", "No.")], skill="Data"),
    ex("u7s1r5", "H", "O1", "Explain why cooking utensils often have wooden or plastic handles.",
       [("metals are good thermal conductors / get hot", ["metal|conduct|hot"]), ("wood/plastic are thermal insulators", ["insulat"])],
       "Metals are good thermal conductors, so a metal handle gets hot. Wood and plastic are thermal insulators, so the handle stays cool enough to hold.", need=2),
    tb("u7s1r6", "H", "O1", "Data: mass of 1 cm³ blocks. Density = mass ÷ volume. Complete.", ["Material", "Mass (g)", "Volume (cm³)", "Density (g/cm³)"],
       [["Silver", "10.5", "1", B(10.5)], ["Wood", "0.9", "1", B(0.9)], ["Aluminium", "5.4", "2", B(2.7)]], skill="Data"),
    mc("u7s1r7", "VH", "O1", "Why does a steel ship float even though steel is denser than water?", ("The air inside the hull makes the ship as a whole less dense than water.", "Correct."),
       [("Steel becomes lighter in water.", "No."), ("Ships are made of wood.", "No."), ("Water pushes steel up whatever its shape.", "Shape (air inside) matters.")], skill="Reasoning"),
    mc("u7s1r8", "M", "O1", "Nitrogen boils at −196 °C. At room temperature it is…", ("a gas", "Correct."), [("a solid", "No."), ("a liquid", "Room temperature is far above −196 °C."), ("a metal", "No.")], skill="Data"),
]
S1_PRAC = [
    mc("u7s1p01", "M", "O1", "Physical properties can be observed…", "without changing the substance", [("only when it reacts", "Chemical properties."), ("never", "No."), ("only by tasting", "Never taste.")]),
    mc("u7s1p02", "M", "O1", "The hardest material on the Mohs scale is…", "diamond (10)", [("talc", "Softest (1)."), ("glass", "About 5.5."), ("steel", "About 6.5.")]),
    mc("u7s1p03", "M", "O1", "The softest mineral on the Mohs scale is…", "talc (1)", [("diamond", "Hardest."), ("quartz", "No."), ("glass", "No.")]),
    mc("u7s1p04", "M", "O1", "Aluminium foil is made by rolling aluminium. This shows aluminium is…", "malleable", [("brittle", "No."), ("an insulator", "No."), ("flammable", "No.")]),
    mc("u7s1p05", "M", "O1", "Copper is used in wires because it is…", "a good electrical conductor and ductile", [("an insulator", "No."), ("brittle", "No."), ("transparent", "No.")]),
    mc("u7s1p06", "M", "O1", "Why are electric wires covered in plastic?", "Plastic is an electrical insulator, protecting us from shocks.", [("To make them heavier", "No."), ("Plastic conducts better", "No."), ("For colour only", "No.")]),
    mc("u7s1p07", "H", "O1", "A glass jug cracks when knocked; a metal jug does not. The metal is…", "stronger", [("harder", "Hardness = scratching."), ("more brittle", "Glass is brittle."), ("less dense", "No.")]),
    mc("u7s1p08", "H", "O1", "A nail scratches a plastic bowl but not a metal bowl. So…", "the metal is harder than the plastic", [("the plastic is harder", "No."), ("they are equally hard", "No."), ("the nail is soft", "No.")]),
    mc("u7s1p09", "M", "O1", "Gold melts at about…", "1064 °C", [("100 °C", "No."), ("0 °C", "No."), ("−196 °C", "No.")]),
    mc("u7s1p10", "H", "O1", "Why are most metals solid at room temperature?", "They have high melting points.", [("They are cold.", "No."), ("They have low melting points.", "No."), ("They are non-metals.", "No.")]),
    mc("u7s1p11", "M", "O1", "Which is flexible?", "Metal wire", [("A pencil", "Snaps."), ("Glass rod", "Brittle."), ("Chalk", "Brittle.")]),
    mc("u7s1p12", "H", "O1", "Density measures…", "how much matter is packed into a space", [("how hot something is", "No."), ("how hard it is", "No."), ("how big it is only", "No.")]),
    mc("u7s1p13", "H", "O1", "Wood floats on water because…", "it is less dense than water", [("it is heavier", "No."), ("it is a metal", "No."), ("it absorbs water", "Not the reason.")]),
    nm("u7s1p14", "H", "O1", "A block has mass 27 g and volume 10 cm³. Density?", 2.7, "g/cm³"),
    mc("u7s1p15", "M", "O1", "Which is a thermal insulator?", "Silicone", [("Copper", "Conductor."), ("Aluminium", "Conductor."), ("Iron", "Conductor.")]),
    mc("u7s1p16", "H", "O1", "Liquid nitrogen boils as soon as it is poured because…", "room temperature is far above its boiling point (−196 °C)", [("it is very hot", "Very cold."), ("it is a metal", "No."), ("it reacts with air", "Not boiling.")]),
    mc("u7s1p17", "H", "O1", "A drill bit (8.5) can scratch…", "glass (5.5) and steel (6.5)", [("diamond (10)", "No."), ("nothing", "No."), ("only talc", "More than talc.")], skill="Data"),
    od("u7s1p18", "M", "O1", "Order from softest to hardest.", ["Talc (1)", "Fingernail (2.5)", "Glass (5.5)", "Steel nail (6.5)", "Diamond (10)"]),
]
S1_ADV = [
    adv(ex("u7s1a1", "VH", "O1", "Choose a material for a frying-pan base and explain your choice using TWO properties.",
           [("metal e.g. iron/aluminium/steel", ["iron|alumin|steel|copper|metal"]), ("good thermal conductor", ["conduct"]), ("high melting point / strong", ["melting|strong|hard"])],
           "Use a metal such as iron or aluminium: it is a good thermal conductor so food cooks evenly, and it has a high melting point and is strong, so it does not melt or break.", need=2)),
    adv(nm("u7s1a2", "VH", "O1", "Gold's density is 19.3 g/cm³. Mass of a 5 cm³ gold bar?", 96.5, "g", tol=0.01)),
    adv(mc("u7s1a3", "VH", "O1", "Why were early aeroplanes made of wood and fabric, and modern jets of aluminium and titanium alloys?", ("The alloys are light, strong and long-lasting.", "Correct."), [("Wood is denser.", "No."), ("Alloys are cheaper than wood.", "Not the reason."), ("Wood conducts electricity.", "No.")], skill="Reasoning")),
    adv(mc("u7s1a4", "VH", "O1", "An object floats in water but sinks in oil. What can you say about its density?", ("It is between the density of oil and water.", "Correct."), [("It is greater than water's.", "It floats in water."), ("It is less than oil's.", "It sinks in oil."), ("It has no density.", "No.")], skill="Reasoning")),
]

S2_REQ = [
    mc("u7s2r1", "M", "O2", "Chemical properties can only be observed when…", ("the material reacts with another substance", "Correct."), [("you look at it", "Physical."), ("you weigh it", "Physical."), ("you measure its length", "Physical.")]),
    mt("u7s2r2", "M", "O2", "Match the chemical property to its meaning.", [("Reactivity", "how easily it reacts"), ("Flammability", "ability to burn"), ("Toxicity", "how poisonous it is"), ("Corrosiveness", "destroys materials and living tissue")]),
    mc("u7s2r3", "M", "O2", "Rust forms when iron reacts with…", ("oxygen and water", "Correct – iron oxide forms."), [("nitrogen only", "No."), ("sunlight only", "No."), ("gold", "No.")]),
    gd("u7s2r4", "H", "O2", "Acidic, neutral or alkaline?", ["Type"], [("pH 2", ["Acidic"]), ("pH 7", ["Neutral"]), ("pH 12", ["Alkaline"]), ("Lemon juice", ["Acidic"]), ("Oven cleaner", ["Alkaline"])], skill="Data"),
    ex("u7s2r5", "H", "O2", "Explain why gold is used for jewellery, using a chemical property.",
       [("gold is unreactive / inert", ["unreactive|inert|does not react"]), ("stays shiny / does not tarnish or rust", ["shiny|tarnish|rust|corrod"])],
       "Gold is very unreactive (inert): it does not react with air or water, so it stays shiny and does not rust or tarnish.", need=2),
    tb("u7s2r6", "H", "O2", "Data: mass of an iron nail left in damp air (rusting adds oxygen). Complete the gain.", ["Week", "Mass (g)", "Gain since start (g)"],
       [["0", "5.00", "0"], ["2", "5.08", B(0.08)], ["4", "5.15", B(0.15)]], skill="Data"),
    mc("u7s2r7", "H", "O2", "Sodium reacts violently with water, producing hydrogen. This shows sodium is…", ("very reactive", "Correct."), [("inert", "Opposite."), ("toxic only", "Not shown here."), ("an alloy", "No.")]),
    mc("u7s2r8", "VH", "O2", "Why is pure iron a poor choice for an outdoor gate?", ("It rusts in wet conditions and weakens.", "Correct."), [("It is too soft to shape.", "Not the main reason."), ("It is flammable.", "No."), ("It does not conduct.", "Irrelevant.")], skill="Reasoning"),
]
S2_PRAC = [
    mc("u7s2p01", "M", "O2", "The opposite of reactive is…", "inert", [("toxic", "No."), ("flammable", "No."), ("dense", "No.")]),
    mc("u7s2p02", "M", "O2", "Which is flammable?", "Petrol", [("Water", "No."), ("Gold", "No."), ("Sand", "No.")]),
    mc("u7s2p03", "M", "O2", "When wood burns it turns into…", "ash, carbon dioxide, water vapour and other gases", [("more wood", "No."), ("pure oxygen", "No."), ("iron", "No.")]),
    mc("u7s2p04", "M", "O2", "The pH scale runs from…", "0 to 14", [("1 to 10", "No."), ("0 to 100", "No."), ("−7 to 7", "No.")]),
    mc("u7s2p05", "M", "O2", "pH 7 is…", "neutral", [("acidic", "Below 7."), ("alkaline", "Above 7."), ("toxic", "No.")]),
    mc("u7s2p06", "H", "O2", "Which elements are toxic and harmed people in the past?", "Lead, arsenic and mercury", [("Oxygen and nitrogen", "No."), ("Gold and silver", "No."), ("Helium and neon", "No.")]),
    mc("u7s2p07", "H", "O2", "Batteries left too long can leak…", "corrosive substances", [("water", "No."), ("gold", "No."), ("oxygen", "No.")]),
    mc("u7s2p08", "H", "O2", "Pesticides kill insects but can…", "harm people and the environment", [("make crops toxic-free", "No."), ("cure diseases", "No."), ("make soil inert", "No.")]),
    mc("u7s2p09", "M", "O2", "Rust is…", "iron oxide", [("iron chloride", "No."), ("pure iron", "No."), ("oxygen gas", "No.")]),
    mc("u7s2p10", "H", "O2", "Inert gases are used inside some lamps because…", "they do not react with the hot filament", [("they burn brightly", "No."), ("they are toxic", "No."), ("they are cheap metals", "No.")]),
    mc("u7s2p11", "H", "O2", "Is burning a physical or chemical property?", "Chemical – new substances form", [("Physical", "New substances form."), ("Neither", "No."), ("Both always", "No.")]),
    mc("u7s2p12", "M", "O2", "Many household cleaners are…", "alkaline", [("acidic", "Some are, but many are alkaline."), ("neutral always", "No."), ("toxic metals", "No.")]),
    ms("u7s2p13", "M", "O2", "Select ALL chemical properties.", ["Flammability", "Toxicity", "Reactivity"], [("Density", "Physical."), ("Hardness", "Physical.")]),
    mc("u7s2p14", "H", "O2", "A substance with pH 1 is…", "strongly acidic", [("weakly acidic", "Lower = stronger."), ("neutral", "No."), ("alkaline", "No.")]),
    mc("u7s2p15", "H", "O2", "How can rusting of iron be prevented?", "Painting or coating it to keep out water and oxygen", [("Heating it", "No."), ("Wetting it", "Speeds rusting."), ("Breaking it", "No.")], skill="Reasoning"),
    mc("u7s2p16", "M", "O2", "Corrosive substances destroy…", "materials, including living tissue", [("only metals", "No."), ("only plastic", "No."), ("nothing", "No.")]),
    mc("u7s2p17", "H", "O2", "Which is a chemical property of oxygen?", "It supports burning", [("It is colourless", "Physical."), ("It is a gas at 20 °C", "Physical."), ("It has low density", "Physical.")]),
    mc("u7s2p18", "H", "O2", "Why must sodium be stored under oil?", "It reacts violently with water (and air).", [("It is flammable only in oil", "No."), ("Oil makes it shiny", "No."), ("It is inert", "No.")]),
]
S2_ADV = [
    adv(ex("u7s2a1", "VH", "O2", "Plan an investigation to test whether salt water makes iron nails rust faster than tap water.",
           [("same nails / same conditions", ["same|identical"]), ("change only salt in water", ["salt"]), ("observe/measure rust over time", ["measure|observe|mass|days|week"])],
           "Put identical iron nails in tubes of tap water and salt water (same volume, same temperature, same time). Observe the amount of rust or measure the gain in mass every few days.", need=2)),
    adv(mc("u7s2a2", "VH", "O2", "The nail data show mass gained over 4 weeks. Why does rusting INCREASE the mass?", ("Oxygen from the air combines with the iron.", "Correct."), [("Iron grows.", "No."), ("Water evaporates.", "No."), ("The nail absorbs light.", "No.")], skill="Reasoning")),
    adv(mc("u7s2a3", "VH", "O2", "A new material does not burn, does not react with acids and is non-toxic. Which use fits best?", ("Lining for a chemical storage tank", "Correct."), [("Fuel", "It does not burn."), ("Fireworks", "No."), ("A battery acid", "No.")], skill="Reasoning")),
    adv(nm("u7s2a4", "VH", "O2", "pH 3 is ten times more acidic than pH 4. How many times more acidic is pH 2 than pH 4?", 100, "times")),
]

S3_REQ = [
    gd("u7s3r1", "M", "O3", "Usually a metal or a non-metal property?", ["Type"],
       [("Shiny", ["Metal"]), ("Brittle", ["Non-metal"]), ("Good electrical conductor", ["Metal"]), ("Often a gas at room temperature", ["Non-metal"]), ("Dense", ["Metal"])], skill="Data"),
    mc("u7s3r2", "M", "O3", "Most elements are…", ("metals", "Correct."), [("non-metals", "Fewer."), ("gases", "No."), ("liquids", "No.")]),
    mc("u7s3r3", "H", "O3", "Diamond is carbon, a non-metal, but it is…", ("shiny, extremely hard and has a very high melting point", "Correct – an exception."), [("dull and soft", "No."), ("a good conductor", "Graphite conducts, not diamond."), ("a metal", "No.")]),
    mc("u7s3r4", "H", "O3", "Graphite is unusual for a non-metal because it…", ("conducts electricity", "Correct."), [("is soft", "Many non-metals are."), ("is black", "Not the point."), ("burns", "No.")]),
    ex("u7s3r5", "H", "O3", "Diamond and graphite are both pure carbon. Why are their properties so different?",
       [("atoms joined/arranged differently", ["arrang|joined|bond|structure|different way"])],
       "Their carbon atoms are joined in different ways (different structures), so their properties are very different.", need=1),
    tb("u7s3r6", "H", "O3", "Data: melting points (°C). Complete the difference.", ["Element", "Metal?", "Melting point (°C)"],
       [["Iron", "Yes", "1538"], ["Sulfur", "No", "115"], ["Difference (iron − sulfur)", "", B(1423)]], skill="Data"),
    ms("u7s3r7", "H", "O3", "Select ALL the things made from non-metal elements combined together.", ["Plastics", "Sugar", "Water", "Petrol"], [("Copper wire", "Metal."), ("Iron nail", "Metal.")]),
    mc("u7s3r8", "VH", "O3", "A dull, brittle element with a high melting point conducts electricity. It is most likely…", ("graphite (carbon)", "Correct – an exception."), [("iron", "Shiny, not brittle."), ("sulfur", "Low melting point, insulator."), ("oxygen", "Gas.")], skill="Reasoning"),
]
S3_PRAC = [
    mc("u7s3p01", "M", "O3", "Which is a metal?", "Silver", [("Sulfur", "No."), ("Oxygen", "No."), ("Carbon", "No.")]),
    mc("u7s3p02", "M", "O3", "Non-metals are usually…", "dull insulators", [("shiny conductors", "Metals."), ("malleable", "No."), ("dense", "No.")]),
    mc("u7s3p03", "M", "O3", "Brittle means…", "breaks or shatters easily", [("bends easily", "Flexible."), ("can be stretched", "Ductile."), ("shiny", "No.")]),
    mc("u7s3p04", "M", "O3", "Graphite is used in…", "pencils", [("jewellery", "Diamond."), ("wires only", "No."), ("cutlery", "No.")]),
    mc("u7s3p05", "H", "O3", "Metals are malleable and ductile, while non-metals are usually…", "brittle", [("also malleable", "No."), ("magnetic", "No."), ("liquid", "No.")]),
    mc("u7s3p06", "M", "O3", "Which element is a liquid metal at room temperature?", "Mercury", [("Iron", "Solid."), ("Oxygen", "Gas, non-metal."), ("Sulfur", "Solid non-metal.")]),
    mc("u7s3p07", "H", "O3", "Why are saucepans not made of sulfur?", "Sulfur has a low melting point, is brittle and is a poor conductor.", [("Sulfur is too shiny", "No."), ("Sulfur is magnetic", "No."), ("Sulfur is too dense", "No.")], skill="Reasoning"),
    mc("u7s3p08", "M", "O3", "Metals usually have ___ melting points.", "high", [("low", "Non-metals."), ("no", "No."), ("random", "No.")]),
    mc("u7s3p09", "H", "O3", "Which non-metal is a gas used by living things for respiration?", "Oxygen", [("Iron", "Metal."), ("Carbon", "Solid."), ("Sulfur", "Solid.")]),
    gd("u7s3p10", "M", "O3", "Metal or non-metal?", ["Type"], [("Copper", ["Metal"]), ("Chlorine", ["Non-metal"]), ("Aluminium", ["Metal"]), ("Nitrogen", ["Non-metal"])], skill="Data"),
    mc("u7s3p11", "H", "O3", "Diamond is used on drill bits because it is…", "extremely hard", [("soft", "No."), ("a conductor", "No."), ("cheap", "No.")]),
    mc("u7s3p12", "H", "O3", "Non-metals are usually less dense than metals. So a 1 cm³ cube of sulfur compared with iron is…", "lighter", [("heavier", "No."), ("the same mass", "No."), ("cannot tell", "Iron is denser.")]),
    mc("u7s3p13", "M", "O3", "Metals conduct…", "heat and electricity", [("only heat", "Both."), ("only electricity", "Both."), ("neither", "No.")]),
    mc("u7s3p14", "H", "O3", "Why do we need exceptions like graphite in our classification?", "Real elements do not always fit simple rules; evidence decides.", [("The rules are always perfect", "No."), ("Graphite is a metal", "No."), ("They are mistakes", "No.")], skill="Reasoning"),
    mc("u7s3p15", "M", "O3", "Which is NOT a typical metal property?", "Brittle", [("Shiny", "Metal."), ("Ductile", "Metal."), ("Conducts electricity", "Metal.")]),
    mc("u7s3p16", "H", "O3", "Electrical wires use copper (metal) inside and plastic (non-metals) outside because…", "copper conducts, plastic insulates", [("both conduct", "No."), ("both insulate", "No."), ("plastic conducts", "No.")]),
    mc("u7s3p17", "M", "O3", "Silicon, used in computer chips, has some metal and some non-metal properties. Such elements are called…", "metalloids", [("alloys", "Mixtures."), ("compounds", "No."), ("gases", "No.")]),
    od("u7s3p18", "M", "O3", "Order by melting point, lowest first.", ["Oxygen (−218 °C)", "Sulfur (115 °C)", "Gold (1064 °C)", "Iron (1538 °C)"]),
]
S3_ADV = [
    adv(ex("u7s3a1", "VH", "O3", "A student says 'all non-metals are soft insulators'. Use evidence to challenge this.",
           [("diamond is hard", ["diamond"]), ("graphite conducts", ["graphite"])],
           "Not all: diamond (carbon) is the hardest natural material, and graphite (also carbon) conducts electricity. So the statement has exceptions.", need=2)),
    adv(mc("u7s3a2", "VH", "O3", "An element has density 0.97 g/cm³, is soft, shiny when cut and conducts electricity. It is…", ("a metal (sodium) – conducts and shiny, though unusually light and soft", "Correct."), [("a non-metal", "It conducts and is shiny."), ("graphite", "Graphite is not shiny when cut."), ("diamond", "No.")], skill="Reasoning")),
    adv(mc("u7s3a3", "VH", "O3", "Why might a scientist test conductivity rather than appearance to classify an element?", ("Conductivity is a clearer, measurable test; appearance can mislead.", "Correct."), [("Appearance is always right", "No."), ("Conductivity is cheaper", "Not the reason."), ("Metals are invisible", "No.")], skill="Reasoning")),
    adv(nm("u7s3a4", "VH", "O3", "Of about 118 elements, about 94 are metals or metal-like. About how many are non-metals or metalloids?", 24, "elements")),
]

S4_REQ = [
    mc("u7s4r1", "M", "O4", "Why are pure metals soft?", ("Their same-sized atoms are in neat layers that can slide over each other.", "Correct."), [("Their atoms are far apart.", "No."), ("They are gases.", "No."), ("They contain water.", "No.")]),
    ex("u7s4r2", "H", "O4", "Explain why an alloy is harder than a pure metal.",
       [("different-sized atoms", ["different.?size|bigger|smaller|mixed"]), ("layers irregular / cannot slide", ["slide|slip|layer|irregular"])],
       "An alloy contains atoms of different sizes, so the layers are no longer regular and cannot slide over each other easily – the alloy is harder and stronger.", need=2),
    gd("u7s4r3", "H", "O4", "Match each alloy to its main metals.", ["Made from"],
       [("Bronze", ["Copper and tin"]), ("Sterling silver", ["Silver and copper"]), ("Stainless steel", ["Iron, chromium, nickel, carbon"]), ("Brass", ["Copper and zinc"])], skill="Data"),
    mt("u7s4r4", "M", "O4", "Match each alloy to a use.", [("Stainless steel", "sinks and cutlery"), ("Titanium alloy", "hip implants and aircraft"), ("Bronze", "statues and ancient tools"), ("Sterling silver", "jewellery")]),
    mc("u7s4r5", "H", "O4", "Why is titanium alloy used for hip implants?", ("It is strong, light, resists corrosion and is not toxic.", "Correct."), [("It is cheap and soft.", "No."), ("It dissolves in the body.", "No."), ("It is magnetic.", "No.")]),
    tb("u7s4r6", "H", "O4", "Data: hardness test (higher = harder). Complete the increase.", ["Material", "Hardness", "Increase over pure copper"],
       [["Pure copper", "50", "0"], ["Bronze", "120", B(70)], ["Brass", "90", B(40)]], skill="Data"),
    mc("u7s4r7", "M", "O4", "The Bronze Age is named after bronze, first used about…", "5300 years ago", [("50 years ago", "No."), ("in 1903", "No."), ("2 million years ago", "No.")]),
    mc("u7s4r8", "VH", "O4", "A model uses towers of same-sized bricks and mixed-sized bricks. What does it show?", ("Mixed sizes stop layers sliding, so alloys are harder.", "Correct."), [("Same-sized bricks are harder.", "No."), ("Alloys are compounds.", "No."), ("Metals are made of bricks.", "It's a model.")], skill="Reasoning"),
]
S4_PRAC = [
    mc("u7s4p01", "M", "O4", "An alloy is a…", "mixture of a metal with other elements", [("compound", "No."), ("pure metal", "No."), ("non-metal", "No.")]),
    mc("u7s4p02", "M", "O4", "Alloys are usually ___ than pure metals.", "harder and stronger", [("softer", "No."), ("less useful", "No."), ("more reactive always", "No.")]),
    mc("u7s4p03", "M", "O4", "Bronze is copper mixed with…", "tin", [("zinc", "Brass."), ("iron", "No."), ("carbon", "Steel.")]),
    mc("u7s4p04", "M", "O4", "Stainless steel doesn't rust, so it is used for…", "sinks and cutlery", [("fireworks", "No."), ("pencil leads", "No."), ("food", "No.")]),
    mc("u7s4p05", "H", "O4", "Sterling silver is harder than pure silver because…", "copper atoms disrupt the layers", [("it is pure silver", "No."), ("it contains gold", "No."), ("it is a compound", "No.")]),
    mc("u7s4p06", "H", "O4", "Cracks spread less easily through alloys because…", "the irregular layers stop them", [("alloys are liquids", "No."), ("alloys are softer", "No."), ("alloys have no atoms", "No.")]),
    mc("u7s4p07", "M", "O4", "Which is NOT an alloy?", "Pure copper", [("Bronze", "Alloy."), ("Steel", "Alloy."), ("Brass", "Alloy.")]),
    mc("u7s4p08", "H", "O4", "In 2023, Australian scientists developed a cheaper titanium alloy using…", "oxygen and iron", [("gold", "No."), ("plastic", "No."), ("water", "No.")]),
    mc("u7s4p09", "M", "O4", "Pure metals are malleable because…", "layers of atoms can slide", [("atoms are far apart", "No."), ("they are brittle", "No."), ("they are gases", "No.")]),
    mc("u7s4p10", "H", "O4", "Why is aircraft frame metal often an alloy?", "Alloys can be strong and light", [("Alloys are heavier", "No."), ("Alloys melt easily", "No."), ("Pure metals do not exist", "No.")]),
    mc("u7s4p11", "M", "O4", "Racing bikes often use…", "titanium alloy", [("pure lead", "No."), ("glass", "No."), ("wood only", "No.")]),
    mc("u7s4p12", "H", "O4", "Adding chromium to iron makes stainless steel…", "resist rusting", [("rust faster", "No."), ("softer", "No."), ("toxic", "No.")]),
    gd("u7s4p13", "M", "O4", "Pure metal or alloy?", ["Type"], [("Gold (24 carat)", ["Pure metal"]), ("Steel", ["Alloy"]), ("Copper wire", ["Pure metal"]), ("Brass", ["Alloy"])], skill="Data"),
    mc("u7s4p14", "H", "O4", "Alloys can be designed…", "with exactly the properties needed", [("only by accident", "No."), ("only from non-metals", "No."), ("only as compounds", "No.")]),
    mc("u7s4p15", "H", "O4", "Bronze is stronger than…", "either copper or tin alone", [("copper only", "Both."), ("nothing", "No."), ("steel always", "No.")]),
    mc("u7s4p16", "M", "O4", "Which property of pure metals is lost a little in alloys?", "Malleability (they are harder to bend)", [("Shininess always", "Not always."), ("Mass", "No."), ("Being a metal", "No.")]),
    od("u7s4p17", "M", "O4", "Order by when first used.", ["Bronze (about 5300 years ago)", "Steel (ancient, improved in the 1800s)", "Stainless steel (early 1900s)", "New cheaper titanium alloy (2023)"]),
    mc("u7s4p18", "H", "O4", "A hip implant must not poison the body. Which property matters?", "Non-toxic", [("Flammable", "No."), ("Magnetic", "No."), ("Brittle", "No.")]),
]
S4_ADV = [
    adv(ex("u7s4a1", "VH", "O4", "Design an alloy for a bicycle frame. State which properties it needs and why.",
           [("strong", ["strong"]), ("light / low density", ["light|density"]), ("resists corrosion / rust", ["rust|corros"])],
           "It must be strong (to carry the rider), light/low density (easy to ride) and resist corrosion (outdoors in rain). A titanium or aluminium alloy fits.", need=2)),
    adv(nm("u7s4a2", "VH", "O4", "Sterling silver is 92.5% silver. Mass of silver in a 40 g sterling ring?", 37, "g")),
    adv(mc("u7s4a3", "VH", "O4", "18-carat gold is 75% gold. Compared with 24-carat (pure) gold it is…", ("harder, because other metal atoms disrupt the layers", "Correct."), [("softer", "No."), ("more valuable by mass", "Less gold."), ("a compound", "No.")], skill="Reasoning")),
    adv(mc("u7s4a4", "VH", "O4", "Why is the particle (brick) model of alloys useful but limited?", ("It shows layers sliding, but real atoms are not bricks and bonds are not shown.", "Correct."), [("It is perfect", "No."), ("It shows real atom colours", "No."), ("It proves alloys are compounds", "No.")], skill="Reasoning")),
]

POOLS = {"7.1": (S1_REQ, S1_PRAC, S1_ADV), "7.2": (S2_REQ, S2_PRAC, S2_ADV), "7.3": (S3_REQ, S3_PRAC, S3_ADV), "7.4": (S4_REQ, S4_PRAC, S4_ADV)}

STOPS = {
    "7.1": [stop("u7v1a", "acidity and toxicity", mc("u7v1a_q", "M", "O1", "Which is a physical property?", "Hardness", [("Flammability", "Chemical."), ("Reactivity", "Chemical."), ("Toxicity", "Chemical.")])),
            stop("u7v1b", "and a drill bit 8.5", mc("u7v1b_q", "H", "O1", "Glass (5.5) vs steel nail (6.5): which scratches the other?", "The steel nail scratches the glass", [("Glass scratches steel", "No."), ("Neither", "No."), ("Both", "No.")])),
            stop("u7v1c", "which is why cooking utensils are made from them", mc("u7v1c_q", "M", "O1", "Which spoon gets hot first in boiling water?", "The metal spoon", [("The wooden spoon", "Insulator."), ("Both together", "No."), ("Neither", "No.")])),
            stop("u7v1d", "less dense than water", mc("u7v1d_q", "H", "O1", "Why does wood float?", "It is less dense than water", [("It is heavy", "No."), ("It is a metal", "No."), ("It is hard", "No.")]))],
    "7.2": [stop("u7v2a", "so pure iron is a poor choice outdoors", mc("u7v2a_q", "M", "O2", "Rusting is a…", "chemical property of iron", [("physical property", "No."), ("type of melting", "No."), ("alloy", "No.")])),
            stop("u7v2b", "used inside some lamps", mc("u7v2b_q", "M", "O2", "Gold stays shiny because it is…", "unreactive (inert)", [("very reactive", "No."), ("flammable", "No."), ("toxic", "No.")]))],
    "7.3": [stop("u7v3a", "brittle, weak and less dense", mc("u7v3a_q", "M", "O3", "Metals are usually…", "malleable, ductile and dense", [("brittle and weak", "Non-metals."), ("gases", "No."), ("insulators", "No.")])),
            stop("u7v3b", "their properties are very different", mc("u7v3b_q", "H", "O3", "Which form of carbon conducts electricity?", "Graphite", [("Diamond", "No."), ("Both", "No."), ("Neither", "No.")]))],
    "7.4": [stop("u7v4a", "mixed-sized bricks", mc("u7v4a_q", "M", "O4", "Alloys are harder because…", "different-sized atoms stop layers sliding", [("their atoms are bigger", "Not just bigger."), ("they are compounds", "No."), ("they contain water", "No.")])),
            stop("u7v4b", "using oxygen and iron", mc("u7v4b_q", "H", "O4", "Bronze is…", "copper and tin", [("iron and carbon", "Steel."), ("silver and copper", "Sterling silver."), ("pure copper", "No.")]))],
}

MINDMAP = {"id": "root", "t": "Properties of materials", "sec": None, "kids": [
    {"id": "phys", "t": "Physical properties", "d": "Strength • hardness (Mohs 1–10) • ductile, malleable, flexible • melting point • conductors/insulators • density.", "obj": "O1", "sec": "7.1"},
    {"id": "chem", "t": "Chemical properties", "d": "Reactivity (iron rusts, sodium + water, gold inert) • flammability • pH • corrosive • toxic.", "obj": "O2", "sec": "7.2"},
    {"id": "mn", "t": "Metals vs non-metals", "d": "Shiny, conductors, malleable vs dull, brittle insulators • exceptions: diamond, graphite.", "obj": "O3", "sec": "7.3"},
    {"id": "alloy", "t": "Alloys", "d": "Different-sized atoms → layers can't slide → harder • bronze, steel, sterling silver, titanium alloy.", "obj": "O4", "sec": "7.4"},
]}
