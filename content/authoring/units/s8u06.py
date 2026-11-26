# -*- coding: utf-8 -*-
"""Stage 8 Unit 6 – Chemical Reactivity. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Chemistry"
BLURB = "How metals react with oxygen, water and dilute acids, extracting iron, inert metals and impurities, and the reactivity series."
OBJECTIVES = {
    "O1": {"sec": "6.1", "code": "8Cc.03, 8Cc.01, 8SIC.05", "codeNote": "", "t": "Describe how metals react with oxygen, write word equations and compare ways of extracting iron."},
    "O2": {"sec": "6.2", "code": "8Cc.03, 8TWSa.02", "codeNote": "", "t": "Describe how metals react with water to form hydroxides and hydrogen, and spot anomalous results."},
    "O3": {"sec": "6.3", "code": "8Cc.03, 8Cc.04, 8Cc.06", "codeNote": "", "t": "Describe how metals react with dilute acids to form salts and hydrogen, and explain inert substances and impurities."},
    "O4": {"sec": "6.4", "code": "8Cc.03, 8SIC.02", "codeNote": "", "t": "Use the reactivity series to predict reactions, and describe uses such as galvanising and catalytic converters."},
}
SECTIONS = [
    {"id": "6.1", "title": "Metals and oxygen", "objs": ["O1"]},
    {"id": "6.2", "title": "Metals and water", "objs": ["O2"]},
    {"id": "6.3", "title": "Metals and dilute acids", "objs": ["O3"]},
    {"id": "6.4", "title": "The reactivity series", "objs": ["O4"]},
]
u = Unit(8, 6)

# ---------------------------------------------------------------- 6.1
u.sec("6.1", "O1")
u.gd("r", "How does each metal react with oxygen?", "Reaction", [("Potassium", "Violently"), ("Magnesium", "Burns with a white flame"), ("Copper", "Only slowly when heated"), ("Gold", "Does not react")])
u.mc("r", "Which word equation is correct?", "magnesium + oxygen → magnesium oxide", [("magnesium → oxygen + magnesium oxide", "No."), ("magnesium oxide + oxygen → magnesium", "No."), ("magnesium + water → magnesium oxide", "Not with oxygen.")])
u.mc("r", "Why are sodium and potassium stored in oil?", "They react quickly with oxygen in the air, so oil keeps air away", [("Oil makes them shiny", "No."), ("They are liquids", "No."), ("Oil makes them more reactive", "No.")])
u.tb("r", "Write the number of the metal in order of reactivity with oxygen (1 = most reactive).", ["Metal", "Rank"], [["Potassium", "1"], ["Magnesium", B(2)], ["Iron", B(3)], ["Gold", B(4)]])
u.ex("r", "Compare extracting iron in a blast furnace with extracting it by electrolysis.", [("blast furnace releases lots of carbon dioxide", ["carbon dioxide|greenhouse"]), ("electrolysis uses lots of electricity / expensive", ["electric|expensive|cost"]), ("electrolysis more sustainable only with renewable electricity", ["renewable|sustainab"])],
     "A blast furnace uses carbon monoxide and releases a lot of carbon dioxide. Electrolysis splits molten iron oxide using electricity; it is more expensive and only more sustainable if the electricity comes from renewable sources.")
u.mc("r", "Why are gold and silver used for jewellery and coins?", "They do not react with oxygen, so they stay shiny", [("They react quickly", "No."), ("They are magnetic", "No."), ("They burn brightly", "No.")], d="H")
u.mc("r", "Iron ore such as haematite contains…", "iron oxide", ["pure iron", "iron chloride", "gold"], d="H")
u.mc("r", "Why can sodium only be extracted by electrolysis?", "It is so reactive that carbon cannot take the oxygen away from it.", [("It is not found in rocks.", "No."), ("It melts too easily.", "Not the reason."), ("Electrolysis is cheaper.", "It is more expensive.")], d="VH")
for p, r, w in [
    ("Metal + oxygen →", "metal oxide", ["metal salt", "metal hydroxide", "hydrogen"]),
    ("Magnesium burns with a…", "dazzling white flame", ["blue flame", "green flame", "no flame"]),
    ("Iron reacts with oxygen…", "slowly, forming rust over time", ["violently", "never", "only in oil"]),
    ("Copper heated in air slowly forms…", "black copper oxide", ["white magnesium oxide", "rust", "gold"]),
    ("Which metal does NOT react with oxygen even when heated?", "Gold", ["Iron", "Magnesium", "Calcium"]),
    ("Which metal reacts most violently with oxygen?", "Potassium", ["Copper", "Zinc", "Silver"]),
    ("Rocks containing metal compounds are called…", "ores", ["alloys", "salts", "oxides only"]),
    ("In a blast furnace iron ore reacts with…", "carbon monoxide", ["oxygen", "water", "gold"]),
    ("Carbon dioxide from blast furnaces is a…", "greenhouse gas", ["metal", "catalyst", "salt"]),
    ("Electrolysis uses…", "an electric current", ["a magnet", "sunlight only", "water only"]),
    ("Electrolysis of molten iron oxide makes iron and…", "oxygen", ["hydrogen", "carbon", "salt"]),
    ("Catalytic converters change harmful exhaust gases into…", "less harmful gases", ["more harmful gases", "metals", "water only"]),
    ("Car exhausts release harmful…", "carbon monoxide", ["oxygen", "nitrogen only", "water"]),
    ("Calcium and magnesium are…", "less reactive than sodium but still react well", ["inert", "more reactive than potassium", "not metals"]),
    ("Zinc reacts with oxygen…", "slowly", ["violently", "never", "explosively"]),
]:
    u.mc("p", p, r, w)
u.od("p", "Order by reactivity with oxygen, most reactive first.", ["Sodium", "Magnesium", "Zinc", "Copper", "Gold"])
u.mt("p", "Match the metal to its oxide.", [("Magnesium", "magnesium oxide"), ("Copper", "copper oxide"), ("Iron", "iron oxide (rust)")])
u.ms("p", "Select ALL the metals that do not react with oxygen even when heated.", ["Gold", "Silver"], ["Iron", "Magnesium", "Zinc"])
u.ex("a", "* Advanced. A company wants to make 'green steel'. Explain why using electrolysis powered by solar energy would reduce its climate impact.", [("blast furnace releases carbon dioxide", ["carbon dioxide|greenhouse"]), ("electrolysis does not need carbon / no CO2 from the reaction", ["no carbon|without carbon|split|electricity"]), ("solar is renewable – no CO2 from electricity", ["solar|renewable"])],
     "A blast furnace releases lots of carbon dioxide. Electrolysis splits iron oxide using electricity instead of carbon, and if the electricity comes from solar power, little carbon dioxide is released.")
u.mc("a", "Why does rust form on an iron gate but not on a gold ring?", "Iron reacts slowly with oxygen and water; gold is unreactive.", ["Gold is magnetic.", "Iron is unreactive.", "Gold reacts faster."], skill="Reasoning")
u.mc("a", "A metal burns brightly in air but does not react as violently as sodium. Where is it in the reactivity series?", "Below sodium but above zinc, like magnesium", ["Above potassium", "Below gold", "Below copper"], skill="Reasoning")
u.mc("a", "Why does electrolysis cost more than a blast furnace?", "It needs a lot of electricity to keep the iron oxide molten and split it.", ["It uses gold.", "It needs no energy.", "It is very fast."])
u.stop("they're stored in oil, to keep air away from them", "Metal + oxygen gives…", "a metal oxide", ["a metal salt", "hydrogen", "water"])
u.stop("perfect for jewellery and coins", "Which metal does not react with oxygen even when heated?", "Gold", ["Iron", "Copper", "Magnesium"])
u.stop("Very reactive metals like sodium and potassium can only be extracted by electrolysis", "A blast furnace releases lots of…", "carbon dioxide", ["oxygen", "hydrogen", "gold"])

# ---------------------------------------------------------------- 6.2
u.sec("6.2", "O2")
u.gd("r", "How does each metal react with water?", "Reaction", [("Potassium", "Very violently"), ("Calcium", "Steadily"), ("Iron", "Only with hot water"), ("Copper", "No reaction")])
u.mc("r", "Metal + water →", "metal hydroxide + hydrogen", [("metal oxide + oxygen", "No."), ("metal salt + water", "That is with acid… no."), ("metal + oxygen", "No.")])
u.tb("r", "Results: bubbles of hydrogen per minute. Complete the difference from calcium.", ["Metal", "Bubbles per minute", "Fewer than calcium by"], [["Calcium", "40", "0"], ["Magnesium (cold water)", "3", B(37)], ["Copper", "0", B(40)]])
u.ex("r", "Magnesium heated in steam formed magnesium oxide, not magnesium hydroxide. Explain why this result is called an anomaly.", [("unexpected / does not fit the pattern", ["unexpected|pattern|different"]), ("other metals form hydroxides", ["hydroxide|other metals"])],
     "Most metals react with water to form a hydroxide, so magnesium forming an oxide with steam is unexpected and does not fit the pattern – an anomaly.")
u.mc("r", "Calcium in water forms a milky white precipitate of…", "calcium hydroxide", ["calcium chloride", "calcium oxide", "calcium carbonate"])
u.mc("r", "Universal Indicator shows that metal hydroxide solutions are…", "alkaline", ["acidic", "neutral", "pure"], d="H")
u.mc("r", "Why can the hydrogen burn when potassium reacts with water?", "The reaction gives out so much heat that the hydrogen ignites", [("Potassium is cold", "No."), ("Water burns", "No."), ("Oxygen is made", "Hydrogen is made.")], d="H")
u.mc("r", "Which metal is the least reactive with water?", "Gold", ["Calcium", "Sodium", "Magnesium"], d="VH")
for p, r, w in [
    ("Potassium on water…", "whizzes around the surface", ["sinks quietly", "does nothing", "turns blue"]),
    ("Potassium reacts with water more violently than…", "sodium", ["nothing", "caesium", "rubidium"]),
    ("Magnesium reacts with cold water…", "only slowly", ["violently", "explosively", "not at all ever"]),
    ("Magnesium with steam forms…", "magnesium oxide", ["magnesium hydroxide", "magnesium chloride", "gold"]),
    ("An unexpected result is called…", "an anomaly", ["a hypothesis", "a variable", "a constant"]),
    ("Zinc and iron react with…", "hot water", ["cold water violently", "nothing ever", "only oil"]),
    ("Copper with water…", "does not react", ["fizzes", "explodes", "forms hydrogen quickly"]),
    ("Silver with water…", "does not react", ["burns", "fizzes", "dissolves"]),
    ("The gas given off when metals react with water is…", "hydrogen", ["oxygen", "carbon dioxide", "chlorine"]),
    ("Sodium + water →", "sodium hydroxide + hydrogen", ["sodium oxide + oxygen", "sodium chloride", "sodium + water"]),
    ("A metal hydroxide solution turns Universal Indicator…", "blue or purple", ["red", "orange", "yellow"]),
    ("Calcium reacts with water…", "steadily with bubbles", ["violently with flames", "not at all", "only when frozen"]),
    ("Which reacts fastest with water?", "Potassium", ["Calcium", "Iron", "Copper"]),
    ("The more reactive a metal, the…", "faster it reacts with water", ["slower it reacts", "heavier it is", "shinier it is"]),
    ("The milky precipitate formed with calcium is a…", "solid", ["gas", "metal", "flame"]),
]:
    u.mc("p", p, r, w)
u.od("p", "Order by reactivity with water, most reactive first.", ["Potassium", "Sodium", "Calcium", "Magnesium", "Copper"])
u.ms("p", "Select ALL the metals that do not react with water at all.", ["Copper", "Silver", "Gold"], ["Calcium", "Sodium"])
u.gd("p", "Cold water, hot water/steam only, or no reaction?", "Reacts with", [("Calcium", "Cold water"), ("Zinc", "Hot water or steam only"), ("Gold", "No reaction")])
u.ex("a", "* Advanced. Explain how you could show safely that the gas produced when calcium reacts with water is hydrogen.", [("collect gas in a test tube", ["collect|test tube"]), ("lighted splint – squeaky pop", ["squeaky|pop|splint"])],
     "Collect the gas in an upside-down test tube and hold a lighted splint at the mouth. A squeaky pop shows the gas is hydrogen.")
u.mc("a", "Lithium reacts with water steadily but less violently than sodium. Where does it fit?", "Below sodium and above calcium", ["Above potassium", "Below copper", "Below gold"], skill="Reasoning")
u.mc("a", "Why are reactions of potassium with water only shown by teachers behind a safety screen?", "The reaction is violent, hot and the hydrogen can ignite.", ["Potassium is poisonous only.", "Water is dangerous.", "It produces gold."], skill="Reasoning")
u.mc("a", "A student records copper fizzing in water. What is the most likely explanation?", "The copper was not pure or the result was recorded wrongly – it is anomalous.", ["Copper is very reactive.", "Copper always fizzes.", "Water was acidic copper."], skill="Reasoning")
u.stop("the heat can make the hydrogen burn", "Metals react with water to form a metal hydroxide and…", "hydrogen", ["oxygen", "carbon dioxide", "salt"])
u.stop("called an anomaly", "An unexpected result is called…", "an anomaly", ["a prediction", "a hypothesis", "a constant"])

# ---------------------------------------------------------------- 6.3
u.sec("6.3", "O3")
u.gd("r", "Which salt does each acid make?", "Salt", [("Hydrochloric acid", "Chloride"), ("Sulfuric acid", "Sulfate"), ("Nitric acid", "Nitrate")])
u.mc("r", "Metal + dilute acid →", "metal salt + hydrogen", [("metal oxide + water", "No."), ("metal hydroxide + oxygen", "No."), ("no reaction ever", "No.")])
u.tb("r", "Fizzing rate with dilute hydrochloric acid. Complete the difference from magnesium.", ["Metal", "Bubbles per minute", "Fewer than magnesium by"], [["Magnesium", "60", "0"], ["Zinc", "15", B(45)], ["Copper", "0", B(60)]])
u.ex("r", "Explain why aluminium drinks cans have a plastic lining inside.", [("fizzy drinks are acidic", ["acid"]), ("acid would react with the metal", ["react|dissolve|corrode"]), ("lining keeps drink and metal apart", ["lining|separate|apart|barrier"])],
     "Fizzy drinks are acidic, and the acid would react with the aluminium. The plastic lining keeps the drink away from the metal.")
u.mc("r", "Zinc + hydrochloric acid →", "zinc chloride + hydrogen", ["zinc sulfate + hydrogen", "zinc oxide + water", "zinc + chlorine"])
u.mc("r", "A substance that does not react with other substances is…", "inert", ["reactive", "an acid", "a catalyst"], d="H")
u.mc("r", "Why must impurities be removed from medicines?", "They are unwanted products that could be harmful", ["They add flavour", "They make medicines stronger", "They are always water"], d="H")
u.mc("r", "Why are sodium and potassium never added to acid in a school lab?", "They react far too violently.", [("They don't react with acids.", "They react violently."), ("They are too expensive.", "Not the reason."), ("They make no gas.", "No.")], d="VH")
for p, r, w in [
    ("Magnesium in dilute hydrochloric acid…", "fizzes vigorously", ["does nothing", "turns gold", "freezes"]),
    ("Magnesium + hydrochloric acid →", "magnesium chloride + hydrogen", ["magnesium sulfate + hydrogen", "magnesium oxide", "magnesium hydroxide"]),
    ("Copper with dilute acid…", "does not react", ["fizzes fast", "explodes", "burns"]),
    ("Gold and silver are…", "inert with water, oxygen and dilute acids", ["very reactive", "acids", "gases"]),
    ("Sulfuric acid makes…", "sulfates", ["chlorides", "nitrates", "oxides"]),
    ("Nitric acid makes…", "nitrates", ["sulfates", "chlorides", "hydroxides"]),
    ("Hydrochloric acid makes…", "chlorides", ["nitrates", "sulfates", "carbonates"]),
    ("The gas made when metals react with acids is…", "hydrogen", ["oxygen", "chlorine", "nitrogen"]),
    ("Zinc reacts with acid…", "more slowly than magnesium", ["faster than magnesium", "not at all", "explosively"]),
    ("Unwanted substances in a product are called…", "impurities", ["catalysts", "solvents", "salts only"]),
    ("Iron + sulfuric acid →", "iron sulfate + hydrogen", ["iron chloride + hydrogen", "iron oxide + water", "iron nitrate"]),
    ("Fizzy drinks are…", "acidic", ["alkaline", "neutral metals", "inert"]),
    ("Reactions sometimes make…", "a mixture of products", ["only pure products", "no products", "only metals"]),
    ("Which metal reacts fastest with acid?", "Magnesium", ["Zinc", "Copper", "Gold"]),
    ("A metal that is inert is useful for…", "jewellery", ["fireworks", "batteries that react", "fertiliser"]),
]:
    u.mc("p", p, r, w)
u.mt("p", "Match the reactants to the salt formed.", [("Zinc + sulfuric acid", "zinc sulfate"), ("Magnesium + nitric acid", "magnesium nitrate"), ("Iron + hydrochloric acid", "iron chloride")])
u.ms("p", "Select ALL the metals that react with dilute hydrochloric acid in a school lab.", ["Magnesium", "Zinc", "Iron"], ["Copper", "Gold"])
u.od("p", "Order by speed of reaction with acid, fastest first.", ["Magnesium", "Zinc", "Iron", "Copper"])
u.ex("a", "* Advanced. Plan a fair test to compare how reactive magnesium, zinc and iron are with dilute acid.", [("same acid concentration and volume", ["same (acid|volume|concentration)"]), ("same mass / size of metal", ["same (mass|size|amount)"]), ("measure gas / bubbles / time", ["bubbles|gas|time|volume of hydrogen"])],
     "Use the same volume and concentration of acid and the same mass and size of each metal. Measure the volume of hydrogen made in one minute (or count bubbles) for each metal.")
u.mc("a", "A reaction makes the salt you want plus an unwanted product. What is the unwanted product?", "An impurity that must be removed", ["A catalyst", "An inert metal", "The solvent"])
u.mc("a", "Why does the mass of a beaker of acid and magnesium fall during the reaction?", "Hydrogen gas escapes into the air.", ["Magnesium disappears.", "Acid evaporates instantly.", "Mass is destroyed."], skill="Reasoning")
u.mc("a", "Why is platinum used for electrical contacts in medical implants?", "It is very unreactive, so it does not corrode in the body.", ["It is very reactive.", "It is cheap.", "It dissolves in acid."], skill="Reasoning")
u.stop("nitric acid makes nitrates", "Metal + dilute acid gives a metal salt and…", "hydrogen", ["oxygen", "water only", "carbon dioxide"])
u.stop("so aluminium cans need a plastic lining inside", "Which metal does not react with dilute hydrochloric acid?", "Copper", ["Magnesium", "Zinc", "Iron"])
u.stop("must be removed, for example from medicines and food", "A substance that does not react with other substances is…", "inert", ["reactive", "acidic", "a salt"])

# ---------------------------------------------------------------- 6.4
u.sec("6.4", "O4")
u.od("r", "Put these metals in reactivity series order, most reactive first.", ["Potassium", "Sodium", "Calcium", "Magnesium", "Zinc", "Iron", "Copper", "Silver", "Gold"])
u.gd("r", "Use the reactivity series. Will each metal react with dilute acid?", "Prediction", [("Calcium", "Yes, quickly"), ("Iron", "Yes, slowly"), ("Silver", "No")])
u.tb("r", "Position in the reactivity series (1 = most reactive). Complete the table.", ["Metal", "Position"], [["Potassium", "1"], ["Calcium", B(3)], ["Zinc", B(5)], ["Gold", B(9)]])
u.ex("r", "Explain how galvanising protects steel from rusting.", [("coating of zinc", ["zinc"]), ("zinc forms protective oxide layer", ["oxide|layer|coat"]), ("keeps air and water away from iron", ["air|water|oxygen"])],
     "Steel is coated with zinc, which forms a protective oxide layer that keeps air and water away from the iron, so it does not rust.")
u.mc("r", "A catalyst is a substance that…", "speeds up a reaction without being changed itself", [("is used up in a reaction", "No."), ("slows reactions", "No."), ("is always a gas", "No.")])
u.mc("r", "Which metals are used in catalytic converters?", "Platinum, palladium and rhodium", ["Iron, copper and zinc", "Sodium and potassium", "Gold and silver only"], d="H")
u.mc("r", "A metal that reacts strongly with oxygen will also react…", "strongly with water and dilute acids", [("weakly with water", "No."), ("not at all with acids", "No."), ("only with gold", "No.")], d="H")
u.mc("r", "Why might using rare metals in catalytic converters raise concerns?", "They are rare, costly and mined in only a few places.", [("They are too common.", "No."), ("They are not metals.", "No."), ("They react with petrol.", "No.")], d="VH")
for p, r, w in [
    ("The reactivity series lists metals from…", "most reactive to least reactive", ["heaviest to lightest", "oldest to newest", "cheapest to dearest"]),
    ("The most reactive metal in this series is…", "potassium", ["gold", "iron", "zinc"]),
    ("The least reactive metal in this series is…", "gold", ["potassium", "magnesium", "calcium"]),
    ("Which is more reactive, magnesium or copper?", "Magnesium", ["Copper", "They are the same", "Neither reacts"]),
    ("Which is more reactive, zinc or iron?", "Zinc", ["Iron", "They are equal", "Neither"]),
    ("The reactivity series helps us…", "predict how a metal will react", ["measure mass", "find boiling points", "draw food chains"]),
    ("Galvanised steel is coated with…", "zinc", ["gold", "copper", "sodium"]),
    ("Catalytic converters reduce…", "harmful exhaust gases", ["engine size", "fuel price", "tyre wear"]),
    ("Platinum is a…", "catalyst in catalytic converters", ["fuel", "plastic", "acid"]),
    ("Calcium is placed…", "between sodium and magnesium", ["above potassium", "below gold", "between copper and silver"]),
    ("Silver is placed…", "between copper and gold", ["above sodium", "between zinc and iron", "at the top"]),
    ("Which metal could be stored safely in air?", "Copper", ["Potassium", "Sodium", "Calcium"]),
    ("Metals high in the series are extracted by…", "electrolysis", ["handpicking", "sieving", "filtering"]),
    ("A catalyst is not used up, so it…", "can be used again and again", ["must be replaced every reaction", "disappears", "becomes a product"]),
    ("Iron is placed…", "below zinc and above copper", ["above sodium", "below gold", "at the top"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the metals more reactive than iron.", ["Zinc", "Magnesium", "Sodium"], ["Copper", "Gold"])
u.gd("p", "More or less reactive than zinc?", "Compared with zinc", [("Magnesium", "More reactive"), ("Copper", "Less reactive"), ("Potassium", "More reactive"), ("Silver", "Less reactive")])
u.mt("p", "Match the use to the property.", [("Gold jewellery", "very unreactive"), ("Zinc coating on steel", "reacts to form a protective layer"), ("Platinum in converters", "acts as a catalyst")])
u.ex("a", "* Advanced. A new metal X reacts slowly with cold water and fizzes steadily with dilute acid. Use the reactivity series to place X and justify your answer.", [("reacts with water – fairly reactive", ["water"]), ("not violent – below calcium / sodium", ["below (calcium|sodium)|not violent"]), ("above zinc / iron – similar to magnesium", ["magnesium|above (zinc|iron)"])],
     "X reacts with water and acid but not violently, so it is below calcium and sodium. It reacts with cold water, so it is above zinc and iron – similar to magnesium.")
u.mc("a", "Why does zinc protect steel even when the zinc coating is scratched?", "Zinc is more reactive than iron, so it reacts first and protects the iron.", ["Zinc is less reactive.", "Scratches heal.", "Iron becomes gold."], skill="Reasoning")
u.mc("a", "Which pair would react most violently?", "Potassium and water", ["Copper and water", "Gold and acid", "Silver and oxygen"])
u.mc("a", "Why do we not use potassium to make coins?", "It reacts violently with air and water.", ["It is too heavy.", "It is inert.", "It is too shiny."], skill="Reasoning")
u.stop("helps us predict how a metal will react", "Which metal is at the top of the reactivity series?", "Potassium", ["Gold", "Iron", "Zinc"])
u.stop("keeps air and water away from the iron", "Galvanised steel is coated with…", "zinc", ["gold", "copper", "silver"])
u.stop("mined in only a few places", "A catalyst…", "speeds up a reaction without being changed", ["is used up", "slows a reaction", "is always a gas"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Chemical reactivity", "sec": None, "kids": [
    {"id": "ox", "t": "Metals + oxygen", "d": "metal + oxygen → metal oxide • K, Na stored in oil • Au, Ag don't react", "obj": "O1", "sec": "6.1"},
    {"id": "ex", "t": "Extracting iron", "d": "Ores • Blast furnace – CO2 • Electrolysis – electricity", "obj": "O1", "sec": "6.1"},
    {"id": "wa", "t": "Metals + water", "d": "metal + water → hydroxide + hydrogen • Alkaline • Mg + steam anomaly", "obj": "O2", "sec": "6.2"},
    {"id": "ac", "t": "Metals + acids", "d": "metal + acid → salt + hydrogen • Chlorides, sulfates, nitrates", "obj": "O3", "sec": "6.3"},
    {"id": "in", "t": "Inert and impure", "d": "Inert – gold, silver • Impurities must be removed", "obj": "O3", "sec": "6.3"},
    {"id": "rs", "t": "Reactivity series", "d": "K, Na, Ca, Mg, Zn, Fe, Cu, Ag, Au • Predict reactions", "obj": "O4", "sec": "6.4"},
    {"id": "us", "t": "Uses", "d": "Galvanising with zinc • Catalysts – Pt, Pd, Rh", "obj": "O4", "sec": "6.4"},
]}
