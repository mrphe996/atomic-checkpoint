# -*- coding: utf-8 -*-
"""Stage 7 Unit 9 – Chemical Reactions. Written by the Atomic teaching team."""
from c_kit import *

STRAND = "Chemistry"
BLURB = "Physical and chemical changes, word equations and particle models, useful and harmful reactions, and the evidence that a reaction has happened."

OBJECTIVES = {
    "O1": {"sec": "9.1", "code": "7Cc.01", "codeNote": "new substances form", "t": "Distinguish physical changes from chemical changes."},
    "O2": {"sec": "9.2", "code": "7Cc.03", "codeNote": "", "t": "Write word equations, identify reactants and products, and use particle models to explain conservation of mass."},
    "O3": {"sec": "9.3", "code": "7SIC.05", "codeNote": "useful and harmful reactions", "t": "Describe useful and harmful chemical reactions, including combustion, acid rain and rusting, and how rusting is prevented."},
    "O4": {"sec": "9.4", "code": "7Cc.01, 7Cc.02, 7Cp.04", "codeNote": "", "t": "Use evidence (colour change, precipitate, gas, reactants used up) and gas tests to decide whether a reaction has happened."},
}

SECTIONS = [
    {"id": "9.1", "title": "Physical and chemical changes", "objs": ["O1"]},
    {"id": "9.2", "title": "Simple chemical reactions", "objs": ["O2"]},
    {"id": "9.3", "title": "Useful and harmful reactions", "objs": ["O3"]},
    {"id": "9.4", "title": "Has a reaction taken place?", "objs": ["O4"]},
]

S1_REQ = [
    gd("u9s1r1", "M", "O1", "Physical or chemical change?", ["Change"],
       [("Ice melting", ["Physical"]), ("Candle burning", ["Chemical"]), ("Paper tearing", ["Physical"]), ("Padlock rusting", ["Chemical"]), ("Bread toasting", ["Chemical"])], skill="Data"),
    mc("u9s1r2", "M", "O1", "The key question to decide if a change is chemical is…", ("Has a new substance been made?", "Correct."), [("Did it get hot?", "Physical changes can too."), ("Did it change shape?", "Physical."), ("Is it a liquid?", "No.")]),
    mc("u9s1r3", "M", "O1", "Sugar dissolving in tea is…", ("a physical change – still sugar and water", "Correct."), [("a chemical change", "No new substance."), ("combustion", "No."), ("rusting", "No.")]),
    ex("u9s1r4", "H", "O1", "Explain why burning wood is a chemical change.",
       [("new substances formed (smoke/ash/CO₂)", ["new substance|ash|smoke|carbon dioxide"]), ("cannot be reversed", ["revers|can't|cannot|back"])],
       "Burning makes new substances (ash, smoke, carbon dioxide) and it cannot be reversed – the ash cannot become wood again.", need=2),
    tb("u9s1r5", "H", "O1", "Count the chemical changes in the list: freezing water, mould on bread, melting chocolate, frying an egg, dissolving salt.", ["List", "Number of chemical changes"], [["5 changes", B(2)]], skill="Data"),
    mc("u9s1r6", "H", "O1", "Which chemical reaction can be reversed?", ("Recharging a rechargeable battery", "Correct."), [("Burning paper", "No."), ("Cooking an egg", "No."), ("Rust forming", "Not easily.")]),
    mc("u9s1r7", "M", "O1", "In a physical change, energy changes…", ("the shape or state of matter", "Correct."), [("the atoms into new elements", "Never."), ("the substance into a new one", "Chemical."), ("nothing", "No.")]),
    mc("u9s1r8", "VH", "O1", "Mould grows on bread. Why is this a chemical change?", ("The mould feeds on the bread and makes new products.", "Correct."), [("The bread changes shape.", "Not enough."), ("It can be reversed.", "No."), ("It is a change of state.", "No.")], skill="Reasoning"),
]
S1_PRAC = [
    mc("u9s1p01", "M", "O1", "A chemical change is also called…", "a chemical reaction", [("a state change", "No."), ("dissolving", "No."), ("melting", "No.")]),
    mc("u9s1p02", "M", "O1", "Melting ice is…", "a physical change", [("a chemical change", "No."), ("combustion", "No."), ("neutralisation", "No.")]),
    mc("u9s1p03", "M", "O1", "Physical changes are usually…", "easy to reverse", [("impossible to reverse", "Chemical."), ("dangerous", "No."), ("new substances", "No.")]),
    mc("u9s1p04", "M", "O1", "Cooking an egg is…", "chemical – it cannot be reversed", [("physical", "No."), ("a state change", "No."), ("dissolving", "No.")]),
    mc("u9s1p05", "M", "O1", "Which is a physical change?", "An iceberg melting", [("Toast browning", "Chemical."), ("Wood burning", "Chemical."), ("Iron rusting", "Chemical.")]),
    mc("u9s1p06", "H", "O1", "Which is a chemical change?", "Baking a cake", [("Chopping carrots", "Physical."), ("Boiling water", "Physical."), ("Freezing juice", "Physical.")]),
    mc("u9s1p07", "H", "O1", "Fertilisers are made by…", "chemical reactions in factories", [("melting rocks", "No."), ("freezing air", "No."), ("dissolving sand", "No.")]),
    mc("u9s1p08", "M", "O1", "Tearing paper is physical because…", "no new substance forms", [("it burns", "No."), ("it gets hot", "No."), ("it changes colour", "No.")]),
    gd("u9s1p09", "M", "O1", "Physical or chemical?", ["Change"], [("Butter melting", ["Physical"]), ("Fireworks exploding", ["Chemical"]), ("Salt dissolving", ["Physical"]), ("Milk going sour", ["Chemical"])], skill="Data"),
    mc("u9s1p10", "H", "O1", "Water boiling to steam is physical because…", "steam is still water", [("steam is a new substance", "No."), ("it can't be reversed", "It can."), ("it burns", "No.")]),
    mc("u9s1p11", "H", "O1", "Which is the best evidence of a chemical change?", "A new substance with different properties forms", [("Shape changes", "Physical."), ("It melts", "Physical."), ("It is cut", "Physical.")]),
    mc("u9s1p12", "M", "O1", "Toasted bread's brown crust is…", "a new substance", [("melted bread", "No."), ("water", "No."), ("dust", "No.")]),
    mc("u9s1p13", "H", "O1", "Chemical reactions happen in our bodies during…", "digestion and respiration", [("blinking only", "No."), ("growing hair only", "No."), ("sleeping only", "No.")]),
    mc("u9s1p14", "H", "O1", "Why is dissolving salt in water physical?", "Evaporating the water gets the salt back", [("Salt is destroyed", "No."), ("A gas forms", "No."), ("It burns", "No.")], skill="Reasoning"),
    ms("u9s1p15", "H", "O1", "Select ALL chemical changes.", ["Rusting", "Burning", "Cooking"], [("Melting", "Physical."), ("Dissolving", "Physical.")]),
    mc("u9s1p16", "M", "O1", "Freezing is…", "a physical change", [("a chemical change", "No."), ("combustion", "No."), ("rusting", "No.")]),
    mc("u9s1p17", "H", "O1", "Energy for physical changes can be transferred by…", "heat, light or electricity", [("only sound", "No."), ("only magnets", "No."), ("nothing", "No.")]),
    od("u9s1p18", "M", "O1", "Order the thinking steps to classify a change.", ["Observe the change", "Ask: has a new substance formed?", "If yes → chemical", "If no → physical"]),
]
S1_ADV = [
    adv(ex("u9s1a1", "VH", "O1", "Is dissolving sugar or burning sugar a chemical change? Give evidence.",
           [("burning is chemical", ["burn"]), ("new substances / black carbon / gases", ["new|carbon|black|gas|smoke"]), ("dissolving reversible / still sugar", ["dissolv|evaporat|still sugar"])],
           "Burning sugar is chemical: it turns black (carbon) and gives off gases – new substances that cannot change back. Dissolving is physical: evaporating the water gets the sugar back.", need=2)),
    adv(mc("u9s1a2", "VH", "O1", "Hard-boiled egg cannot be unboiled, but melted chocolate can set again. This shows…", ("cooking egg is chemical; melting chocolate is physical", "Correct."), [("both are chemical", "No."), ("both are physical", "No."), ("egg is physical", "No.")], skill="Reasoning")),
    adv(mc("u9s1a3", "VH", "O1", "Why is 'it got hot' not good evidence of a chemical change on its own?", ("Physical changes can also involve energy changes.", "Correct."), [("Chemical changes never get hot.", "No."), ("Heat is a substance.", "No."), ("It always is good evidence.", "No.")], skill="Reasoning")),
    adv(nm("u9s1a4", "VH", "O1", "Of 40 changes in a survey, 15% were chemical. How many were physical?", 34, "")),
]

S2_REQ = [
    mc("u9s2r1", "M", "O2", "In a word equation, the reactants are written…", ("on the left of the arrow", "Correct."), [("on the right", "Products."), ("under the arrow", "No."), ("nowhere", "No.")]),
    mc("u9s2r2", "M", "O2", "Carbon + oxygen →", ("carbon dioxide", "Correct."), [("water", "No."), ("carbon", "No."), ("oxygen", "No.")]),
    gd("u9s2r3", "H", "O2", "Hydrochloric acid + zinc → zinc chloride + hydrogen. Reactant or product?", ["Role"],
       [("Hydrochloric acid", ["Reactant"]), ("Zinc", ["Reactant"]), ("Zinc chloride", ["Product"]), ("Hydrogen", ["Product"])], skill="Data"),
    tb("u9s2r4", "H", "O2", "2 hydrogen molecules + 1 oxygen molecule → 2 water molecules. Count the atoms.", ["Atoms", "Before", "After"],
       [["Hydrogen", B(4), B(4)], ["Oxygen", B(2), B(2)]], skill="Data"),
    ex("u9s2r5", "H", "O2", "Explain why mass is conserved in a chemical reaction.",
       [("atoms rearranged", ["rearrang"]), ("not created or destroyed", ["created|destroyed|same number|lost"])],
       "In a reaction atoms are only rearranged into new substances; they are not created or destroyed, so the total mass stays the same.", need=2),
    mc("u9s2r6", "H", "O2", "What starts the carbon + oxygen reaction in the particle model?", ("Energy (heat) breaks the oxygen molecule apart", "Correct."), [("Carbon splits", "No."), ("Cooling", "No."), ("Nothing is needed", "No.")]),
    nm("u9s2r7", "H", "O2", "12 g of carbon reacts with 32 g of oxygen. Mass of carbon dioxide?", 44, "g", skill="Data"),
    mc("u9s2r8", "VH", "O2", "Can a reaction turn iron atoms into gold atoms?", ("No – reactions only rearrange atoms, not change elements.", "Correct."), [("Yes, with enough heat.", "No."), ("Yes, with acid.", "No."), ("Sometimes.", "No.")], skill="Reasoning"),
]
S2_PRAC = [
    mc("u9s2p01", "M", "O2", "The new substances in a reaction are the…", "products", [("reactants", "Starting substances."), ("indicators", "No."), ("catalysts", "No.")]),
    mc("u9s2p02", "M", "O2", "The arrow in a word equation shows…", "the direction of the reaction", [("equals", "No."), ("heat", "No."), ("a gas", "No.")]),
    mc("u9s2p03", "M", "O2", "Acid + alkali →", "salt + water", [("hydrogen", "No."), ("carbon dioxide", "No."), ("oxygen", "No.")]),
    mc("u9s2p04", "M", "O2", "An oxygen molecule is made of…", "two oxygen atoms joined", [("one oxygen atom", "No."), ("oxygen and hydrogen", "No."), ("three atoms", "No.")]),
    mc("u9s2p05", "H", "O2", "Iron + sulfur → iron sulfide. The product is…", "iron sulfide", [("iron", "Reactant."), ("sulfur", "Reactant."), ("iron and sulfur", "Reactants.")]),
    mc("u9s2p06", "H", "O2", "One carbon dioxide molecule contains…", "1 carbon and 2 oxygen atoms", [("2 carbon and 1 oxygen", "No."), ("1 carbon, 1 oxygen", "No."), ("3 carbon", "No.")]),
    mc("u9s2p07", "M", "O2", "Conservation of mass means…", "total mass before = total mass after", [("mass increases", "No."), ("mass is lost", "No."), ("mass doesn't matter", "No.")]),
    nm("u9s2p08", "H", "O2", "4 g hydrogen + 32 g oxygen → ? g water", 36, "g"),
    mc("u9s2p09", "H", "O2", "Sometimes the warmth of the surroundings is enough to…", "start a reaction", [("stop all reactions", "No."), ("create atoms", "No."), ("destroy mass", "No.")]),
    mc("u9s2p10", "H", "O2", "Chalk fizzes in vinegar and the beaker gets lighter because…", "carbon dioxide gas escapes", [("atoms are destroyed", "No."), ("chalk evaporates", "No."), ("vinegar disappears", "No.")], skill="Reasoning"),
    mc("u9s2p11", "M", "O2", "Hydrogen + oxygen →", "water", [("hydrogen peroxide", "No."), ("carbon dioxide", "No."), ("ammonia", "No.")]),
    gd("u9s2p12", "M", "O2", "Carbon + oxygen → carbon dioxide. Reactant or product?", ["Role"], [("Carbon", ["Reactant"]), ("Oxygen", ["Reactant"]), ("Carbon dioxide", ["Product"])], skill="Data"),
    mc("u9s2p13", "H", "O2", "Magnesium + oxygen → magnesium oxide. Why is the product heavier than the magnesium?", "Oxygen atoms from the air have joined it", [("Magnesium grows", "No."), ("Mass is created", "No."), ("It absorbs heat", "No.")], skill="Reasoning"),
    nm("u9s2p14", "H", "O2", "24 g magnesium reacts to make 40 g magnesium oxide. Mass of oxygen used?", 16, "g"),
    mc("u9s2p15", "M", "O2", "A word equation uses…", "names of substances", [("pictures only", "No."), ("numbers only", "No."), ("colours", "No.")]),
    mc("u9s2p16", "H", "O2", "In the particle model, the circles represent…", "atoms", [("cells", "No."), ("bubbles", "No."), ("planets", "No.")]),
    mc("u9s2p17", "H", "O2", "Zinc + hydrochloric acid → zinc chloride + ?", "hydrogen", [("oxygen", "No."), ("water", "No."), ("carbon dioxide", "No.")]),
    od("u9s2p18", "M", "O2", "Order what happens in a reaction.", ["Energy is supplied", "Reactant molecules break apart", "Atoms rearrange", "New product molecules form"]),
]
S2_ADV = [
    adv(ex("u9s2a1", "VH", "O2", "A student burns magnesium in an open dish and finds the mass goes UP. Another burns a candle and the mass goes DOWN. Explain both.",
           [("magnesium gains oxygen from air", ["oxygen|air"]), ("candle products are gases that escape", ["gas|escape|carbon dioxide|water vapour"]), ("mass still conserved overall", ["conserv|atoms"])],
           "Magnesium combines with oxygen from the air, so the solid product is heavier. A candle's products (carbon dioxide, water vapour) are gases that escape, so the dish gets lighter. Overall, atoms – and mass – are conserved.", need=2)),
    adv(mc("u9s2a2", "VH", "O2", "How could you show mass is conserved when chalk reacts with acid?", ("Do it in a sealed flask so the gas cannot escape, and weigh before and after.", "Correct."), [("Use an open beaker", "Gas escapes."), ("Heat it", "No."), ("Use more chalk", "No.")], skill="Reasoning")),
    adv(nm("u9s2a3", "VH", "O2", "56 g iron + 32 g sulfur → iron sulfide. If 8 g of sulfur was left over, mass of iron sulfide?", 80, "g")),
    adv(mc("u9s2a4", "VH", "O2", "A particle model is useful but limited because…", ("atoms are not really coloured balls, and it doesn't show the energy involved", "Correct."), [("it shows exact atom sizes", "No."), ("it is a real photo", "No."), ("it shows atoms being destroyed", "No.")], skill="Reasoning")),
]

S3_REQ = [
    mc("u9s3r1", "M", "O3", "Fuel containing carbon + oxygen →", ("carbon dioxide + water", "Correct."), [("oxygen + hydrogen", "No."), ("glucose", "No."), ("rust", "No.")]),
    mc("u9s3r2", "M", "O3", "Photosynthesis: carbon dioxide + water → ? + oxygen", ("glucose", "Correct."), [("rust", "No."), ("ammonia", "No."), ("salt", "No.")]),
    gd("u9s3r3", "H", "O3", "Useful or harmful reaction?", ["Effect"],
       [("Making fertiliser", ["Useful"]), ("Rusting of a bridge", ["Harmful"]), ("Burning fuel in an engine", ["Useful"]), ("Acid rain on statues", ["Harmful"]), ("Digestion", ["Useful"])], skill="Data"),
    mt("u9s3r4", "M", "O3", "Match the rust-prevention method to how it works.", [("Painting", "protective layer keeps out air and water"), ("Stainless steel", "chromium forms a thin oxide layer"), ("Zinc coating", "zinc corrodes instead of iron")]),
    ex("u9s3r5", "H", "O3", "Explain why acid rain damages marble statues.",
       [("marble is calcium carbonate", ["calcium carbonate|carbonate"]), ("acid reacts with it / corrodes", ["react|corrod|wear|dissolv"])],
       "Marble is calcium carbonate. Acid rain reacts with it, forming calcium sulfate, carbon dioxide and water, so the stone slowly corrodes.", need=2),
    tb("u9s3r6", "H", "O3", "Data: rust on steel plates after 6 months (g). Complete the saving.", ["Plate", "Rust (g)", "Less rust than bare steel (g)"],
       [["Bare steel", "12", "0"], ["Painted steel", "2", B(10)], ["Zinc-coated steel", "1", B(11)]], skill="Data"),
    mc("u9s3r7", "H", "O3", "Ammonia for fertilisers is made from…", ("nitrogen and hydrogen", "Correct."), [("carbon and oxygen", "No."), ("iron and sulfur", "No."), ("salt and water", "No.")]),
    mc("u9s3r8", "VH", "O3", "Foresters spread crushed limestone in acid-damaged forests because…", ("it neutralises the acid in the soil", "Correct."), [("it makes soil more acidic", "No."), ("it adds iron", "No."), ("it stops rain", "No.")], skill="Reasoning"),
]
S3_PRAC = [
    mc("u9s3p01", "M", "O3", "Burning is also called…", "combustion", [("corrosion", "No."), ("respiration", "Different."), ("neutralisation", "No.")]),
    mc("u9s3p02", "M", "O3", "Which reaction restores oxygen to the air?", "Photosynthesis", [("Combustion", "Uses it."), ("Rusting", "Uses it."), ("Respiration", "Uses it.")]),
    mc("u9s3p03", "M", "O3", "Plastics are made from substances refined from…", "crude oil and plants", [("iron ore", "No."), ("salt", "No."), ("sand only", "No.")]),
    mc("u9s3p04", "M", "O3", "Rust is…", "hydrated iron oxide", [("iron sulfide", "No."), ("zinc oxide", "No."), ("pure iron", "No.")]),
    mc("u9s3p05", "H", "O3", "Why must iron bridges be checked for rust?", "Rust is flaky and weaker than iron", [("Rust is stronger", "No."), ("Rust is toxic gas", "No."), ("Rust is shiny", "No.")]),
    mc("u9s3p06", "M", "O3", "Rusting needs iron, oxygen and…", "water", [("nitrogen", "No."), ("carbon dioxide", "No."), ("salt only", "Speeds it but water is needed.")]),
    mc("u9s3p07", "H", "O3", "A watering can coated in zinc doesn't rust because…", "zinc corrodes instead of the iron", [("zinc is plastic", "No."), ("zinc adds water", "No."), ("zinc is gold", "No.")]),
    mc("u9s3p08", "M", "O3", "Burning fuels makes greenhouse gases and…", "pollutants that cause acid rain", [("oxygen", "No."), ("fertiliser", "No."), ("glucose", "No.")]),
    ms("u9s3p09", "H", "O3", "Select ALL things made of calcium carbonate.", ["Marble", "Chalk", "Eggshells", "Limestone"], [("Iron", "No."), ("Plastic", "No.")]),
    mc("u9s3p10", "H", "O3", "One drawback of plastics is…", "plastic waste can harm the environment", [("they are heavy", "Light."), ("they are expensive", "Cheap."), ("they cannot be shaped", "Easy to shape.")]),
    mc("u9s3p11", "M", "O3", "Which useful reaction happens in our cells to release energy?", "Respiration", [("Rusting", "No."), ("Acid rain", "No."), ("Corrosion", "No.")]),
    mc("u9s3p12", "H", "O3", "Stainless steel resists rusting because it contains…", "chromium", [("salt", "No."), ("water", "No."), ("sulfur", "No.")]),
    gd("u9s3p13", "M", "O3", "Reactant needed?", ["Needed"], [("Photosynthesis", ["Light"]), ("Combustion", ["Oxygen"]), ("Rusting", ["Water"])], skill="Data"),
    mc("u9s3p14", "H", "O3", "Acid rain + calcium carbonate gives calcium sulfate, water and…", "carbon dioxide", [("hydrogen", "No."), ("oxygen", "No."), ("nitrogen", "No.")]),
    mc("u9s3p15", "H", "O3", "Why are seashells and coral at risk if oceans become more acidic?", "They are calcium carbonate, which reacts with acid", [("They are iron", "No."), ("They are alkaline metals", "No."), ("They are plastic", "No.")], skill="Reasoning"),
    mc("u9s3p16", "M", "O3", "Painting steel prevents rust by…", "keeping out air and water", [("adding oxygen", "No."), ("heating it", "No."), ("making it acidic", "No.")]),
    mc("u9s3p17", "H", "O3", "Fertilisers help farmers to…", "grow enough food", [("stop rain", "No."), ("make plastics", "No."), ("prevent rust", "No.")]),
    od("u9s3p18", "M", "O3", "Order the chain of events for acid rain damage.", ["Fuels are burned", "Pollutant gases enter the air", "Gases dissolve in rain", "Acid rain corrodes stone and harms forests"]),
]
S3_ADV = [
    adv(ex("u9s3a1", "VH", "O3", "Evaluate combustion of fuels: give one benefit and one problem.",
           [("benefit: releases energy for vehicles / power", ["energy|power|vehicle|transport|heat"]), ("problem: greenhouse gases / acid rain / pollution", ["greenhouse|acid rain|pollut|carbon dioxide|climate"])],
           "Benefit: combustion releases a lot of energy to power vehicles. Problem: it produces greenhouse gases and pollutants that cause acid rain.", need=2)),
    adv(mc("u9s3a2", "VH", "O3", "A ship's steel hull has zinc blocks attached. Why?", ("The zinc corrodes instead of the steel (sacrificial protection).", "Correct."), [("Zinc makes the ship heavier", "No."), ("Zinc is decorative", "No."), ("Zinc stops waves", "No.")], skill="Reasoning")),
    adv(nm("u9s3a3", "VH", "O3", "A statue loses 0.4 mm of surface each year to acid rain. How much is lost in 25 years?", 10, "mm")),
    adv(mc("u9s3a4", "VH", "O3", "Why might painting NOT protect a bike chain well?", ("Moving parts rub the paint off, exposing iron to air and water.", "Correct."), [("Paint conducts", "No."), ("Chains never rust", "No."), ("Paint is acidic", "No.")], skill="Reasoning")),
]

S4_REQ = [
    ms("u9s4r1", "M", "O4", "Select ALL signs that a chemical reaction may have happened.", ["Colour change", "A precipitate forms", "Bubbles of gas", "Reactants are used up"], [("The object is cut", "Physical."), ("Ice melts", "Physical.")]),
    tb("u9s4r2", "H", "O4", "Complete the gas tests.", ["Gas", "Test", "Result"],
       [["Hydrogen", "lighted splint", "squeaky pop"], ["Carbon dioxide", "limewater", "turns milky"], ["Oxygen", "glowing splint", "relights"], ["Number of gases", "", B(3)]], skill="Data"),
    mc("u9s4r3", "M", "O4", "A precipitate is…", ("a solid that appears in a solution", "Correct."), [("a gas", "No."), ("a colour", "No."), ("a liquid", "No.")]),
    mc("u9s4r4", "H", "O4", "Silver nitrate + sodium chloride gives a white solid because…", ("silver chloride is insoluble", "Correct."), [("salt freezes", "No."), ("a gas forms", "No."), ("silver melts", "No.")]),
    mc("u9s4r5", "H", "O4", "An iron nail in blue copper sulfate becomes coated with…", ("reddish copper, and the solution turns pale green", "Correct."), [("rust only", "No."), ("silver", "No."), ("sulfur", "No.")]),
    ex("u9s4r6", "H", "O4", "Magnesium ribbon seems to disappear in hydrochloric acid. Where have the magnesium atoms gone?",
       [("into a product / magnesium chloride", ["magnesium chloride|product|new substance"]), ("atoms not destroyed / rearranged", ["not destroyed|rearrang|still exist|didn't stop"])],
       "The magnesium atoms were not destroyed; they rearranged to become part of a new product, magnesium chloride, which is dissolved in the solution.", need=2),
    gd("u9s4r7", "M", "O4", "Which gas?", ["Gas"], [("Relights a glowing splint", ["Oxygen"]), ("Turns limewater milky", ["Carbon dioxide"]), ("Squeaky pop", ["Hydrogen"])], skill="Data"),
    mc("u9s4r8", "VH", "O4", "Mixing two clear solutions gives a cloudy white mixture. The best conclusion is…", ("a precipitate formed, so a reaction happened", "Correct."), [("the solutions froze", "No."), ("nothing happened", "No."), ("a gas formed", "Bubbles would show.")], skill="Reasoning"),
]
S4_PRAC = [
    mc("u9s4p01", "M", "O4", "Bubbles of gas produced in a reaction are called…", "effervescence", [("precipitation", "No."), ("condensation", "No."), ("evaporation", "No.")]),
    mc("u9s4p02", "M", "O4", "Sulfuric acid + sugar produces…", "black carbon", [("white salt", "No."), ("pure water", "No."), ("gold", "No.")]),
    mc("u9s4p03", "M", "O4", "Vinegar + baking soda gives off…", "carbon dioxide", [("hydrogen", "No."), ("oxygen", "No."), ("chlorine", "No.")]),
    mc("u9s4p04", "M", "O4", "Magnesium + hydrochloric acid gives off…", "hydrogen", [("carbon dioxide", "No."), ("oxygen", "No."), ("nitrogen", "No.")]),
    mc("u9s4p05", "H", "O4", "Limewater turns milky because…", "a white precipitate of calcium carbonate forms", [("it boils", "No."), ("it freezes", "No."), ("it evaporates", "No.")]),
    mc("u9s4p06", "M", "O4", "Hydrogen peroxide breaks down into water and…", "oxygen", [("hydrogen", "No."), ("carbon dioxide", "No."), ("salt", "No.")]),
    mc("u9s4p07", "H", "O4", "Iron + copper sulfate →", "iron sulfate + copper", [("iron + copper", "No."), ("rust", "No."), ("copper sulfate + iron", "No.")]),
    mc("u9s4p08", "M", "O4", "To test for oxygen you use…", "a glowing splint", [("a lighted splint", "Hydrogen."), ("limewater", "CO₂."), ("litmus", "No.")]),
    mc("u9s4p09", "H", "O4", "Why is a colour change alone not always proof of a reaction?", "Mixing coloured liquids or dissolving can change colour physically", [("Colour never changes", "No."), ("Reactions have no colour", "No."), ("It always is proof", "No.")], skill="Reasoning"),
    mc("u9s4p10", "M", "O4", "In magnesium + hydrochloric acid, the chlorine atoms in magnesium chloride came from…", "the acid", [("the air", "No."), ("the magnesium", "No."), ("nowhere", "No.")]),
    gd("u9s4p11", "M", "O4", "Which sign of reaction?", ["Sign"], [("Fizzing", ["Gas given off"]), ("Cloudy white solid", ["Precipitate"]), ("Blue turns green", ["Colour change"])], skill="Data"),
    mc("u9s4p12", "H", "O4", "Which shows a reaction most clearly?", "Two solutions mix and a solid forms", [("Ice melts", "Physical."), ("Sugar dissolves", "Physical."), ("Water boils", "Physical.")]),
    mc("u9s4p13", "M", "O4", "Rekindles means…", "relights", [("goes out", "No."), ("turns milky", "No."), ("pops", "No.")]),
    mc("u9s4p14", "H", "O4", "Silver chloride separates from the solution because it…", "is insoluble", [("is a gas", "No."), ("is very soluble", "No."), ("is a liquid", "No.")]),
    mc("u9s4p15", "H", "O4", "Reactants being used up is evidence of a reaction because…", "their atoms have rearranged into new substances", [("they evaporated", "No."), ("they were destroyed", "No."), ("they became invisible metal", "No.")]),
    nm("u9s4p16", "H", "O4", "A test-tube of 6 glowing-splint tests: 4 relit. How many tubes contained oxygen?", 4, "tubes"),
    od("u9s4p17", "M", "O4", "Order the oxygen test.", ["Light a wooden splint", "Blow it out so it glows", "Put it into the gas", "Watch whether it relights"]),
    mc("u9s4p18", "H", "O4", "A lit splint is held at a tube from zinc + acid. It pops. The gas is…", "hydrogen", [("oxygen", "No."), ("carbon dioxide", "Puts it out."), ("nitrogen", "No.")]),
]
S4_ADV = [
    adv(ex("u9s4a1", "VH", "O4", "You have three tubes of gas: hydrogen, oxygen, carbon dioxide. Plan how to identify each.",
           [("lighted splint → squeaky pop = hydrogen", ["pop|lighted|hydrogen"]), ("glowing splint relights = oxygen", ["glowing|relight|oxygen"]), ("limewater milky = carbon dioxide", ["limewater|milky|carbon dioxide"])],
           "Lighted splint: squeaky pop = hydrogen. Glowing splint: relights = oxygen. Bubble through limewater: milky = carbon dioxide.", need=3)),
    adv(mc("u9s4a2", "VH", "O4", "Why does an iron nail in copper sulfate gain a copper coat but the solution turns green?", ("Iron swaps places with copper, forming green iron sulfate.", "Correct."), [("The copper melts", "No."), ("The nail rusts", "No."), ("Light changes the colour", "No.")], skill="Reasoning")),
    adv(nm("u9s4a3", "VH", "O4", "A 2.4 g magnesium ribbon fully reacts in acid. How many grams of magnesium atoms are now in the products?", 2.4, "g")),
    adv(mc("u9s4a4", "VH", "O4", "Why is it good practice to look for more than one sign before concluding a reaction happened?", ("One sign could have a physical cause; several make the conclusion stronger.", "Correct."), [("Reactions always show all four", "No."), ("Teachers like it", "No."), ("Signs are random", "No.")], skill="Reasoning")),
]

POOLS = {"9.1": (S1_REQ, S1_PRAC, S1_ADV), "9.2": (S2_REQ, S2_PRAC, S2_ADV), "9.3": (S3_REQ, S3_PRAC, S3_ADV), "9.4": (S4_REQ, S4_PRAC, S4_ADV)}

STOPS = {
    "9.1": [stop("u9v1a", "when you recharge it", mc("u9v1a_q", "M", "O1", "Burning a candle is…", "a chemical change", [("a physical change", "New substances form."), ("melting only", "No."), ("dissolving", "No.")])),
            stop("u9v1b", "which are chemical?", mc("u9v1b_q", "H", "O1", "Which is a physical change?", "An iceberg melting", [("Bread toasting", "Chemical."), ("Mould growing", "Chemical."), ("Wood burning", "Chemical.")]))],
    "9.2": [stop("u9v2a", "go on the right", mc("u9v2a_q", "M", "O2", "In acid + zinc → zinc chloride + hydrogen, the products are…", "zinc chloride and hydrogen", [("acid and zinc", "Reactants."), ("zinc only", "No."), ("hydrogen only", "Both.")])),
            stop("u9v2b", "the conservation of mass", mc("u9v2b_q", "H", "O2", "In a reaction, atoms are…", "rearranged, not created or destroyed", [("destroyed", "No."), ("created", "No."), ("changed into other elements", "No.")]))],
    "9.3": [stop("u9v3a", "useful reactions too", mc("u9v3a_q", "M", "O3", "Photosynthesis makes glucose and…", "oxygen", [("carbon dioxide", "Reactant."), ("rust", "No."), ("ammonia", "No.")])),
            stop("u9v3b", "which neutralises the acid", mc("u9v3b_q", "H", "O3", "Marble statues are made of…", "calcium carbonate", [("iron oxide", "No."), ("plastic", "No."), ("sodium chloride", "No.")])),
            stop("u9v3c", "instead of the iron underneath", mc("u9v3c_q", "H", "O3", "Painting steel prevents rust by…", "keeping out air and water", [("adding chromium", "Stainless steel."), ("heating it", "No."), ("adding acid", "No.")]))],
    "9.4": [stop("u9v4a", "separates out as a precipitate", mc("u9v4a_q", "M", "O4", "Bubbles of gas in a reaction are called…", "effervescence", [("a precipitate", "Solid."), ("condensation", "No."), ("melting", "No.")])),
            stop("u9v4b", "That means oxygen", mc("u9v4b_q", "M", "O4", "Limewater turning milky shows…", "carbon dioxide", [("hydrogen", "Squeaky pop."), ("oxygen", "Relights splint."), ("nitrogen", "No.")])),
            stop("u9v4c", "The atoms are simply rearranged into new substances", mc("u9v4c_q", "H", "O4", "When magnesium 'disappears' in acid, its atoms…", "become part of magnesium chloride", [("are destroyed", "No."), ("turn into hydrogen", "No."), ("evaporate", "No.")]))],
}

MINDMAP = {"id": "root", "t": "Chemical reactions", "sec": None, "kids": [
    {"id": "pc", "t": "Physical vs chemical", "d": "Physical: shape/state, no new substance, usually reversible • Chemical: new substance, usually irreversible.", "obj": "O1", "sec": "9.1"},
    {"id": "eq", "t": "Word equations", "d": "Reactants → products • particle models • atoms rearranged • conservation of mass.", "obj": "O2", "sec": "9.2"},
    {"id": "uh", "t": "Useful and harmful", "d": "Combustion, photosynthesis, plastics, ammonia • acid rain on carbonates • rusting and prevention (paint, stainless steel, zinc).", "obj": "O3", "sec": "9.3"},
    {"id": "ev", "t": "Evidence of reaction", "d": "Colour change • precipitate • effervescence • reactants used up • gas tests: H₂ pop, CO₂ limewater, O₂ relights.", "obj": "O4", "sec": "9.4"},
]}
