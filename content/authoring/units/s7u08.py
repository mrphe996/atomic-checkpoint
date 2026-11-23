# -*- coding: utf-8 -*-
"""Stage 7 Unit 8 – Acids and Alkalis. Written by the Atomic teaching team."""
from c_kit import *

STRAND = "Chemistry"
BLURB = "Acids and alkalis around us, working safely, testing with indicators and the pH scale, gas tests, and neutralisation."

OBJECTIVES = {
    "O1": {"sec": "8.1", "code": "7Cp.04, 7TWSp.05", "codeNote": "", "t": "Describe acids, their properties and safe handling, and test for carbon dioxide and hydrogen."},
    "O2": {"sec": "8.2", "code": "7Cp.01", "codeNote": "alkalis", "t": "Describe alkalis, their uses and properties."},
    "O3": {"sec": "8.3", "code": "7Cp.02, 7Cp.03", "codeNote": "", "t": "Use indicators and the pH scale to classify solutions as acidic, neutral or alkaline."},
    "O4": {"sec": "8.4", "code": "7Cc.04", "codeNote": "", "t": "Describe neutralisation and its uses, using pH to follow the change."},
}

SECTIONS = [
    {"id": "8.1", "title": "What are acids?", "objs": ["O1"]},
    {"id": "8.2", "title": "What are alkalis?", "objs": ["O2"]},
    {"id": "8.3", "title": "Indicators and pH", "objs": ["O3"]},
    {"id": "8.4", "title": "Neutralisation", "objs": ["O4"]},
]

S1_REQ = [
    mt("u8s1r1", "M", "O1", "Match the acid to where it is found.", [("Citric acid", "lemons"), ("Ethanoic acid", "vinegar"), ("Hydrochloric acid", "the stomach"), ("Carbonic acid", "fizzy drinks"), ("Sulfuric acid", "car batteries")]),
    gd("u8s1r2", "M", "O1", "Safe or unsafe practice with acids?", ["Practice"],
       [("Wearing safety goggles", ["Safe"]), ("Pouring water into acid", ["Unsafe"]), ("Tasting to check if acidic", ["Unsafe"]), ("Using a dropper", ["Safe"]), ("Rinsing a spill with plenty of water", ["Safe"])], skill="Data"),
    tb("u8s1r3", "H", "O1", "Complete the gas tests.", ["Gas", "Test", "Positive result"],
       [["Carbon dioxide", "bubble through limewater", "turns milky"], ["Hydrogen", "lighted splint", "squeaky pop"], ["Number of gases tested here", "", B(2)]], skill="Data"),
    mc("u8s1r4", "M", "O1", "Acid + carbonate produces which gas?", ("Carbon dioxide", "Correct."), [("Hydrogen", "From acid + metal."), ("Oxygen", "No."), ("Nitrogen", "No.")]),
    mc("u8s1r5", "M", "O1", "Acid + magnesium produces which gas?", ("Hydrogen", "Correct – squeaky pop."), [("Carbon dioxide", "From carbonates."), ("Oxygen", "No."), ("Chlorine", "No.")]),
    ex("u8s1r6", "H", "O1", "Explain why you must always add acid to water and not water to acid.",
       [("water into acid can spit / splash", ["spit|splash|spray"]), ("adding acid slowly to water is safer", ["slow|safer|dilute|acid to water"])],
       "Pouring water into acid can make it spit and splash onto skin. Adding acid slowly to water is safer because the mixture stays dilute.", need=2),
    mc("u8s1r7", "H", "O1", "Why is acid rain a problem?", ("It harms trees and corrodes statues and buildings.", "Correct."), [("It makes plants grow faster.", "No."), ("It is alkaline.", "It is acidic."), ("It is pure water.", "No.")]),
    mc("u8s1r8", "VH", "O1", "A gas turns limewater milky. Which reaction most likely made it?", ("Acid + a carbonate", "Correct – CO₂."), [("Acid + magnesium", "Hydrogen."), ("Water + salt", "No gas."), ("Burning hydrogen", "Water.")], skill="Reasoning"),
]
S1_PRAC = [
    mc("u8s1p01", "M", "O1", "Acids usually taste…", "sour", [("bitter", "Alkalis."), ("sweet", "No."), ("salty", "No.")], hint="Never taste chemicals in the lab."),
    mc("u8s1p02", "M", "O1", "Blue litmus in an acid turns…", "red", [("blue", "No change only for alkalis."), ("green", "No."), ("purple", "No.")]),
    mc("u8s1p03", "M", "O1", "Dilute acids have been…", "mixed with water to make them weaker", [("heated", "No."), ("made stronger", "No."), ("frozen", "No.")]),
    mc("u8s1p04", "M", "O1", "Vitamin C is…", "ascorbic acid", [("citric acid", "No."), ("sulfuric acid", "No."), ("an alkali", "No.")]),
    mc("u8s1p05", "M", "O1", "Which acid builds up in muscles during exercise?", "Lactic acid", [("Nitric acid", "No."), ("Sulfuric acid", "No."), ("Citric acid", "No.")]),
    mc("u8s1p06", "M", "O1", "Nitric acid is used to make…", "fertilisers", [("toothpaste", "No."), ("soap", "No."), ("glass", "No.")]),
    mc("u8s1p07", "H", "O1", "Why is rainwater naturally slightly acidic?", "Carbon dioxide dissolves in it", [("Salt dissolves in it", "No."), ("It is boiled", "No."), ("Oxygen makes it acidic", "No.")]),
    mc("u8s1p08", "M", "O1", "The 'corrosive' hazard symbol warns that a substance…", "can burn skin and damage materials", [("is flammable", "Different symbol."), ("is safe", "No."), ("is radioactive", "No.")]),
    mc("u8s1p09", "H", "O1", "Why is sulfuric acid used in car batteries?", "Acids conduct electricity", [("Acids are sweet", "No."), ("It is neutral", "No."), ("It is solid", "No.")]),
    mc("u8s1p10", "M", "O1", "If acid spills on your skin you should…", "rinse with plenty of water and tell your teacher", [("wipe it on clothes", "No."), ("ignore it", "No."), ("add more acid", "No.")]),
    mc("u8s1p11", "H", "O1", "Red litmus in an acid…", "stays red", [("turns blue", "Alkali."), ("turns green", "No."), ("disappears", "No.")]),
    mc("u8s1p12", "M", "O1", "Your stomach makes hydrochloric acid to…", "kill bacteria and digest food", [("cool the body", "No."), ("make bones", "No."), ("store energy", "No.")]),
    ms("u8s1p13", "H", "O1", "Select ALL properties of acids.", ["Sour taste", "Corrosive", "Conduct electricity", "Turn blue litmus red"], [("Feel soapy", "Alkalis."), ("Turn red litmus blue", "Alkalis.")]),
    mc("u8s1p14", "H", "O1", "Acid + alkali gives…", "a salt and water", [("hydrogen", "No."), ("carbon dioxide", "No."), ("oxygen", "No.")]),
    mc("u8s1p15", "H", "O1", "Burning fossil fuels causes acid rain because it releases…", "acidic pollutant gases", [("pure water", "No."), ("oxygen", "No."), ("alkalis", "No.")]),
    gd("u8s1p16", "M", "O1", "Which gas test?", ["Gas"], [("Limewater turns milky", ["Carbon dioxide"]), ("Squeaky pop", ["Hydrogen"]), ("Glowing splint relights", ["Oxygen"])], skill="Data"),
    mc("u8s1p17", "H", "O1", "Why use a dropper rather than pouring acid?", "To control small amounts and avoid spills", [("To make it stronger", "No."), ("To heat it", "No."), ("For colour", "No.")], skill="Reasoning"),
    od("u8s1p18", "M", "O1", "Order the steps to test a gas for hydrogen.", ["Collect the gas in a test tube", "Light a wooden splint", "Hold the lit splint at the mouth of the tube", "Listen for a squeaky pop"]),
]
S1_ADV = [
    adv(ex("u8s1a1", "VH", "O1", "A student adds marble chips (calcium carbonate) to acid and sees fizzing. Describe how to identify the gas.",
           [("bubble gas through limewater", ["limewater"]), ("turns milky / cloudy = carbon dioxide", ["milky|cloudy"])],
           "Bubble the gas through limewater. If the limewater turns milky, the gas is carbon dioxide.", need=2)),
    adv(mc("u8s1a2", "VH", "O1", "Why do old marble statues wear away faster in cities with heavy traffic?", ("Acid rain reacts with the carbonate in marble.", "Correct."), [("Wind is stronger in cities.", "Not the main reason."), ("Marble is alkaline rain-proof.", "No."), ("Cars heat them.", "No.")], skill="Reasoning")),
    adv(mc("u8s1a3", "VH", "O1", "A metal added to dilute acid gives no bubbles. The best conclusion is…", ("The metal is unreactive with that acid (e.g. copper or gold).", "Correct."), [("The acid is an alkali.", "No."), ("Hydrogen is invisible.", "Bubbles would still show."), ("All metals react.", "No.")], skill="Reasoning")),
    adv(nm("u8s1a4", "VH", "O1", "A stomach makes about 1.5 litres of gastric juice a day. How many litres in a week?", 10.5, "L")),
]

S2_REQ = [
    mc("u8s2r1", "M", "O2", "Alkalis are the chemical opposites of…", ("acids", "Correct."), [("salts", "No."), ("metals", "No."), ("water", "No.")]),
    gd("u8s2r2", "M", "O2", "Acid or alkali?", ["Type"], [("Toothpaste", ["Alkali"]), ("Vinegar", ["Acid"]), ("Oven cleaner", ["Alkali"]), ("Lemon juice", ["Acid"]), ("Soap", ["Alkali"])], skill="Data"),
    mc("u8s2r3", "M", "O2", "Red litmus in an alkali turns…", ("blue", "Correct."), [("red", "No change for acids."), ("yellow", "No."), ("green", "No.")]),
    mc("u8s2r4", "M", "O2", "Sodium hydroxide is also called…", ("caustic soda", "Correct."), [("baking soda", "No."), ("table salt", "No."), ("limewater", "No.")]),
    ex("u8s2r5", "H", "O2", "Explain why oven cleaner must be handled with goggles and gloves.",
       [("contains a strong alkali", ["alkali|sodium hydroxide|caustic"]), ("corrosive / burns skin or eyes", ["corros|burn|damage"])],
       "Oven cleaner contains a strong alkali (sodium hydroxide), which is corrosive and can burn skin and eyes.", need=2),
    tb("u8s2r6", "H", "O2", "Litmus results. Write the number of alkalis in the last row.", ["Solution", "Red litmus", "Blue litmus"],
       [["Soap", "blue", "blue"], ["Vinegar", "red", "red"], ["Ammonia", "blue", "blue"], ["Number of alkalis", "", B(2)]], skill="Data"),
    mc("u8s2r7", "H", "O2", "Which is true of alkalis?", ("They conduct electricity and feel soapy.", "Correct."), [("They taste sour.", "Acids."), ("They turn blue litmus red.", "Acids."), ("They are never corrosive.", "Strong ones are.")]),
    mc("u8s2r8", "VH", "O2", "An antacid tablet helps indigestion because it…", ("contains an alkali that reacts with extra stomach acid", "Correct."), [("adds more acid", "No."), ("is sweet", "No."), ("kills all bacteria", "No.")], skill="Reasoning"),
]
S2_PRAC = [
    mc("u8s2p01", "M", "O2", "Alkalis taste…", "bitter", [("sour", "Acids."), ("sweet", "No."), ("salty", "No.")]),
    mc("u8s2p02", "M", "O2", "Ammonia solution is used in…", "floor cleaners", [("fizzy drinks", "No."), ("car batteries", "No."), ("vinegar", "No.")]),
    mc("u8s2p03", "M", "O2", "Alkalis feel…", "soapy", [("gritty", "No."), ("sticky", "No."), ("hot", "No.")]),
    mc("u8s2p04", "M", "O2", "Blue litmus in an alkali…", "stays blue", [("turns red", "Acids."), ("turns green", "No."), ("turns white", "No.")]),
    mc("u8s2p05", "M", "O2", "Strong alkalis are used to…", "clean tough dirt", [("make food sour", "No."), ("make batteries", "No."), ("make fizzy drinks", "No.")]),
    mc("u8s2p06", "H", "O2", "Alkalis react with acids to make…", "a salt and water", [("hydrogen", "No."), ("carbon dioxide only", "No."), ("more acid", "No.")]),
    mc("u8s2p07", "M", "O2", "Which contains an alkali?", "Toothpaste", [("Orange juice", "Acid."), ("Cola", "Acid."), ("Vinegar", "Acid.")]),
    mc("u8s2p08", "H", "O2", "Why should you handle alkalis as carefully as acids?", "Strong alkalis are corrosive too", [("They are flammable", "No."), ("They are always weak", "No."), ("They are radioactive", "No.")]),
    ms("u8s2p09", "H", "O2", "Select ALL properties of alkalis.", ["Bitter taste", "Feel soapy", "Turn red litmus blue", "Conduct electricity"], [("Sour taste", "Acids."), ("Turn blue litmus red", "Acids.")]),
    mc("u8s2p10", "M", "O2", "Oven cleaner contains…", "sodium hydroxide", [("citric acid", "No."), ("ethanoic acid", "No."), ("carbonic acid", "No.")]),
    mc("u8s2p11", "H", "O2", "A solution turns red litmus blue. It is…", "an alkali", [("an acid", "No."), ("neutral", "No change."), ("pure water", "No change.")]),
    mc("u8s2p12", "H", "O2", "A solution does not change red OR blue litmus. It is…", "neutral", [("an acid", "Blue would turn red."), ("an alkali", "Red would turn blue."), ("corrosive", "Not shown.")]),
    gd("u8s2p13", "M", "O2", "Property of an acid or an alkali?", ["Type"], [("Sour", ["Acid"]), ("Soapy", ["Alkali"]), ("Turns blue litmus red", ["Acid"]), ("Turns red litmus blue", ["Alkali"])], skill="Data"),
    mc("u8s2p14", "H", "O2", "Why is soap slightly alkaline useful?", "Alkalis help break down grease and dirt", [("It makes skin sour", "No."), ("It conducts heat", "No."), ("It adds acid", "No.")]),
    mc("u8s2p15", "M", "O2", "Some antacid tablets contain…", "alkalis", [("acids", "No."), ("sugar only", "No."), ("salt only", "No.")]),
    mc("u8s2p16", "H", "O2", "Which pair are both alkalis?", "Soap and ammonia", [("Vinegar and soap", "Vinegar is acid."), ("Lemon and ammonia", "Lemon is acid."), ("Cola and vinegar", "Both acids.")]),
    mc("u8s2p17", "H", "O2", "A bee sting is acidic. Which might ease it?", "A weak alkali such as baking soda", [("Vinegar", "Acid."), ("Lemon juice", "Acid."), ("More acid", "No.")], skill="Reasoning"),
    od("u8s2p18", "M", "O2", "Order the safety steps before using oven cleaner.", ["Read the hazard label", "Put on goggles and gloves", "Use the cleaner carefully", "Wash hands afterwards"]),
]
S2_ADV = [
    adv(ex("u8s2a1", "VH", "O2", "You have three unlabelled colourless liquids: an acid, an alkali and water. Describe how to identify them with red and blue litmus.",
           [("acid turns blue litmus red", ["blue.*red|acid.*red"]), ("alkali turns red litmus blue", ["red.*blue|alkali.*blue"]), ("water changes neither", ["neither|no change|water"])],
           "Dip red and blue litmus into each. The acid turns blue litmus red; the alkali turns red litmus blue; water changes neither.", need=2)),
    adv(mc("u8s2a2", "VH", "O2", "Why can't litmus tell you whether drain cleaner is a stronger alkali than soap?", ("Litmus only shows acid or alkali, not how strong.", "Correct."), [("Litmus doesn't work on alkalis.", "It does."), ("Both are acids.", "No."), ("Litmus is a metal.", "No.")], skill="Reasoning")),
    adv(mc("u8s2a3", "VH", "O2", "Why might a hairdresser rinse hair after an alkaline shampoo with a slightly acidic conditioner?", ("To neutralise leftover alkali, leaving hair smoother.", "Correct."), [("To make it more alkaline.", "No."), ("Acid adds colour.", "No."), ("No reason.", "No.")], skill="Reasoning")),
    adv(nm("u8s2a4", "VH", "O2", "In a class test, 18 of 24 household liquids turned red litmus blue. What percentage were alkaline?", 75, "%")),
]

S3_REQ = [
    gd("u8s3r1", "M", "O3", "Acidic, neutral or alkaline?", ["Type"], [("pH 1", ["Acidic"]), ("pH 7", ["Neutral"]), ("pH 10", ["Alkaline"]), ("pH 4", ["Acidic"]), ("pH 14", ["Alkaline"])], skill="Data"),
    mc("u8s3r2", "M", "O3", "Red cabbage juice in an alkali turns…", ("green or yellow", "Correct."), [("red", "Acids."), ("purple", "Neutral."), ("black", "No.")]),
    tb("u8s3r3", "H", "O3", "Universal Indicator results. Write how many are acidic.", ["Liquid", "pH"],
       [["Lemon juice", "2"], ["Pure water", "7"], ["Milk", "6"], ["Bleach", "12"], ["Number acidic", B(2)]], skill="Data"),
    od("u8s3r4", "H", "O3", "Order from most acidic to most alkaline.", ["Battery acid", "Lemon juice", "Pure water", "Baking soda", "Drain cleaner"], skill="Data"),
    ex("u8s3r5", "H", "O3", "Explain why Universal Indicator is more useful than litmus.",
       [("gives pH / how acidic or alkaline", ["ph|how acidic|how alkaline|strength|strong"]), ("litmus only acid or alkali", ["litmus|only"])],
       "Litmus only shows whether a solution is acidic or alkaline. Universal Indicator gives a pH number, so it shows how acidic or alkaline it is.", need=2),
    mc("u8s3r6", "H", "O3", "Hydrangeas with blue flowers are growing in soil that is…", ("acidic", "Correct."), [("alkaline", "Pink/red."), ("neutral", "Pink/red."), ("salty", "No.")]),
    mc("u8s3r7", "M", "O3", "Lower pH below 7 means…", ("a stronger acid", "Correct."), [("a weaker acid", "No."), ("more alkaline", "No."), ("neutral", "No.")]),
    mc("u8s3r8", "VH", "O3", "Why might an indicator that works inside the body help doctors treat cancer?", ("Tumour areas are more acidic, so changes in pH can show whether treatment works.", "Correct."), [("It cures cancer.", "No."), ("Tumours are alkaline.", "More acidic."), ("It makes MRI unnecessary.", "It is seen by MRI.")], skill="Reasoning"),
]
S3_PRAC = [
    mc("u8s3p01", "M", "O3", "An indicator…", "changes colour depending on pH", [("neutralises acids", "No."), ("makes gas", "No."), ("is always red", "No.")]),
    mc("u8s3p02", "M", "O3", "The pH scale runs from…", "0 to 14", [("1 to 10", "No."), ("0 to 7", "No."), ("7 to 14", "No.")]),
    mc("u8s3p03", "M", "O3", "Pure water has pH…", "7", [("0", "No."), ("14", "No."), ("1", "No.")]),
    mc("u8s3p04", "M", "O3", "Red cabbage juice in a neutral solution is…", "purple", [("red", "Acid."), ("green", "Alkali."), ("yellow", "Alkali.")]),
    mc("u8s3p05", "M", "O3", "Red cabbage juice in vinegar turns…", "red", [("green", "No."), ("purple", "No."), ("blue", "No.")]),
    mc("u8s3p06", "H", "O3", "Turmeric turns red-orange in…", "alkalis", [("acids", "No."), ("water", "No."), ("oil", "No.")]),
    mc("u8s3p07", "M", "O3", "Which device gives a digital pH reading?", "A pH meter", [("A thermometer", "No."), ("A burette", "No."), ("Litmus paper", "No.")]),
    mc("u8s3p08", "H", "O3", "Which has the lowest pH?", "Stomach acid", [("Milk", "Weakly acidic."), ("Pure water", "7."), ("Soap", "Alkaline.")]),
    mc("u8s3p09", "H", "O3", "Which has the highest pH?", "Drain cleaner", [("Bleach", "High but lower."), ("Ammonia", "Lower."), ("Baking soda", "Lower.")]),
    mc("u8s3p10", "M", "O3", "Coffee is…", "acidic", [("alkaline", "No."), ("neutral", "No."), ("pH 14", "No.")]),
    gd("u8s3p11", "M", "O3", "Red cabbage colour → type", ["Type"], [("Red", ["Acidic"]), ("Purple", ["Neutral"]), ("Green", ["Alkaline"])], skill="Data"),
    mc("u8s3p12", "H", "O3", "How do you make red cabbage indicator?", "Chop leaves, soak in hot water, strain and cool", [("Freeze the cabbage", "No."), ("Burn it", "No."), ("Add salt", "No.")]),
    mc("u8s3p13", "H", "O3", "Universal Indicator is used by…", "comparing its colour with a chart", [("smelling it", "No."), ("tasting it", "Never."), ("weighing it", "No.")]),
    nm("u8s3p14", "H", "O3", "A solution changes from pH 3 to pH 7. By how many pH units did it rise?", 4, ""),
    mc("u8s3p15", "H", "O3", "Hydrangeas with pink flowers grow in soil that is…", "neutral to alkaline", [("strongly acidic", "Blue."), ("frozen", "No."), ("pure water", "No.")]),
    mc("u8s3p16", "M", "O3", "In 2013, Dr Franz Schilling's team found an acid detectable by MRI called…", "zymonic acid", [("citric acid", "No."), ("lactic acid", "No."), ("nitric acid", "No.")]),
    mc("u8s3p17", "H", "O3", "Above pH 7, the higher the number…", "the more alkaline", [("the more acidic", "No."), ("the more neutral", "No."), ("the colder", "No.")]),
    od("u8s3p18", "M", "O3", "Order by pH, lowest first.", ["Battery acid (0)", "Vinegar (3)", "Milk (6)", "Soap (10)", "Drain cleaner (14)"], skill="Data"),
]
S3_ADV = [
    adv(ex("u8s3a1", "VH", "O3", "A gardener has a pink hydrangea and wants blue flowers. What should she change and why?",
           [("make the soil more acidic", ["acid"]), ("blue flowers in acidic soil", ["blue"])],
           "Make the soil more acidic (lower its pH), because hydrangeas produce blue flowers in acidic soil.", need=2)),
    adv(mc("u8s3a2", "VH", "O3", "Two acids: pH 2 and pH 5. Which is stronger and why?", ("pH 2 – lower pH means stronger acid.", "Correct."), [("pH 5 – higher is stronger.", "No."), ("Same – both acids.", "No."), ("Cannot tell.", "pH shows it.")], skill="Reasoning")),
    adv(mc("u8s3a3", "VH", "O3", "Why is a digital pH meter better than Universal Indicator paper for a coloured juice?", ("The juice's own colour can hide the indicator colour.", "Correct."), [("Paper is too acidic.", "No."), ("Meters taste it.", "No."), ("Paper only works on water.", "No.")], skill="Reasoning")),
    adv(nm("u8s3a4", "VH", "O3", "Each pH step is a ten-times change in acidity. How many times more acidic is pH 3 than pH 6?", 1000, "times")),
]

S4_REQ = [
    mc("u8s4r1", "M", "O4", "Neutralisation: acid + alkali →", ("salt + water", "Correct."), [("hydrogen + salt", "No."), ("carbon dioxide only", "No."), ("more acid", "No.")]),
    gr("u8s4r2", "H", "O4", "Alkali is added to acid. Plot pH against volume of alkali.", {"label": "Volume of alkali added (cm³)", "min": 0, "max": 25, "step": 5}, {"label": "pH", "min": 0, "max": 14, "step": 1},
       [[0, 1], [5, 2], [10, 3], [15, 7], [20, 11], [25, 12]], skill="Data"),
    tb("u8s4r3", "H", "O4", "Use the data: alkali added (cm³) and pH. At what volume is the solution neutral?", ["Volume (cm³)", "pH"],
       [["10", "3"], ["15", "7"], ["20", "11"], ["Neutral at (cm³)", B(15)]], skill="Data"),
    mc("u8s4r4", "M", "O4", "Hydrochloric acid + sodium hydroxide makes…", ("sodium chloride and water", "Correct."), [("sodium and chlorine", "No."), ("hydrogen and oxygen", "No."), ("carbon dioxide", "No.")]),
    ex("u8s4r5", "H", "O4", "Explain how power stations reduce acid rain.",
       [("sulfur dioxide (acidic gas)", ["sulfur|acid"]), ("neutralised by alkali / calcium hydroxide (scrubbing)", ["neutral|alkali|calcium|scrub"])],
       "Burning fossil fuels releases acidic sulfur dioxide. Power stations neutralise it with an alkali, calcium hydroxide, in a process called scrubbing.", need=2),
    mc("u8s4r6", "M", "O4", "A burette is used in titration to…", ("add alkali drop by drop to reach pH 7 exactly", "Correct."), [("heat the acid", "No."), ("measure temperature", "No."), ("test for hydrogen", "No.")]),
    mt("u8s4r7", "M", "O4", "Match the use of neutralisation.", [("Antacid tablets", "treat indigestion"), ("Lime", "treat acidic lakes and soil"), ("Calcium hydroxide", "scrub power-station gases"), ("Conditioner", "balance alkaline shampoo")]),
    mc("u8s4r8", "VH", "O4", "Too much alkali is added past neutralisation. Universal Indicator turns…", ("blue-purple, as the solution is now alkaline", "Correct."), [("green, it stays neutral", "No."), ("red", "No."), ("colourless", "No.")], skill="Reasoning"),
]
S4_PRAC = [
    mc("u8s4p01", "M", "O4", "At neutralisation the pH is…", "7", [("1", "No."), ("14", "No."), ("0", "No.")]),
    mc("u8s4p02", "M", "O4", "Adding alkali to acid makes the pH…", "rise", [("fall", "No."), ("stay the same", "No."), ("become negative", "No.")]),
    mc("u8s4p03", "M", "O4", "Indigestion can be treated with…", "antacid tablets", [("vinegar", "Acid."), ("lemon juice", "Acid."), ("cola", "Acid.")]),
    mc("u8s4p04", "M", "O4", "Universal Indicator in a neutral solution is…", "green", [("red", "No."), ("purple", "No."), ("orange", "No.")]),
    mc("u8s4p05", "H", "O4", "Farmers add lime to fields to…", "neutralise acidic soil", [("make soil more acidic", "No."), ("kill crops", "No."), ("add water", "No.")]),
    mc("u8s4p06", "M", "O4", "The method of adding alkali drop by drop with a burette is…", "titration", [("filtration", "No."), ("distillation", "No."), ("evaporation", "No.")]),
    mc("u8s4p07", "H", "O4", "Sodium chloride is…", "table salt", [("caustic soda", "Sodium hydroxide."), ("vinegar", "No."), ("chalk", "No.")]),
    mc("u8s4p08", "H", "O4", "Acid at pH 1 with Universal Indicator is…", "red", [("green", "No."), ("purple", "No."), ("blue", "No.")]),
    mc("u8s4p09", "M", "O4", "Many shampoos are…", "alkaline", [("acidic", "Conditioners are."), ("neutral always", "No."), ("pH 0", "No.")]),
    mc("u8s4p10", "H", "O4", "A salt is made when…", "an acid reacts with an alkali", [("water boils", "No."), ("a metal melts", "No."), ("gas cools", "No.")]),
    mc("u8s4p11", "H", "O4", "Why do farmers test soil pH?", "Crops grow best in soil of the right pH", [("To find gold", "No."), ("To measure rain", "No."), ("For colour", "No.")]),
    mc("u8s4p12", "H", "O4", "Antacids can contain carbonates. Neutralising acid with a carbonate also makes…", "carbon dioxide", [("hydrogen", "No."), ("oxygen", "No."), ("chlorine", "No.")]),
    gd("u8s4p13", "M", "O4", "Does pH go up or down?", ["Change"], [("Alkali added to acid", ["Up"]), ("Acid added to alkali", ["Down"]), ("Lime added to acidic lake", ["Up"])], skill="Data"),
    mc("u8s4p14", "H", "O4", "Why do lakes need treating after acid rain?", "Too acidic water harms plants and animals", [("They get too salty", "No."), ("They freeze", "No."), ("They become alkaline", "No.")]),
    mc("u8s4p15", "M", "O4", "Which is neutralisation?", "Adding sodium hydroxide to hydrochloric acid", [("Melting ice", "No."), ("Dissolving sugar", "No."), ("Boiling water", "No.")]),
    nm("u8s4p16", "H", "O4", "10 cm³ of alkali neutralises 10 cm³ of acid. How much of the same alkali neutralises 25 cm³ of the acid?", 25, "cm³"),
    mc("u8s4p17", "H", "O4", "A student adds alkali quickly from a beaker and overshoots pH 7. What should she use?", "A burette, adding drop by drop", [("A bigger beaker", "No."), ("A thermometer", "No."), ("Litmus only", "No.")], skill="Reasoning"),
    od("u8s4p18", "M", "O4", "Order Universal Indicator colours as alkali is added to strong acid.", ["Red", "Orange", "Green", "Blue", "Purple"]),
]
S4_ADV = [
    adv(ex("u8s4a1", "VH", "O4", "Describe how to make a neutral solution of a salt from an acid and an alkali using Universal Indicator.",
           [("add indicator to acid", ["indicator"]), ("add alkali a little at a time / burette", ["drop|little|burette|slowly"]), ("stop at green / pH 7", ["green|ph 7|neutral"])],
           "Add Universal Indicator to the acid. Add alkali a little at a time (from a burette), mixing, until the indicator turns green (pH 7). The solution is now neutral salt solution.", need=2)),
    adv(mc("u8s4a2", "VH", "O4", "Why isn't a strong alkali like sodium hydroxide used as an antacid?", ("It is corrosive and would damage the body.", "Correct."), [("It is acidic.", "No."), ("It does not react with acid.", "It does."), ("It is too sweet.", "No.")], skill="Reasoning")),
    adv(nm("u8s4a3", "VH", "O4", "A lake needs 2 tonnes of lime per hectare. How much lime for a 7.5 hectare lake?", 15, "tonnes")),
    adv(mc("u8s4a4", "VH", "O4", "In the pH graph, the pH jumps sharply from 3 to 11 between 10 and 20 cm³. What does that show?", ("Neutralisation happens around 15 cm³, so near pH 7 each drop matters.", "Correct."), [("The acid boiled.", "No."), ("Nothing happened.", "No."), ("More acid was added.", "No.")], skill="Data")),
]

POOLS = {"8.1": (S1_REQ, S1_PRAC, S1_ADV), "8.2": (S2_REQ, S2_PRAC, S2_ADV), "8.3": (S3_REQ, S3_PRAC, S3_ADV), "8.4": (S4_REQ, S4_PRAC, S4_ADV)}

STOPS = {
    "8.1": [stop("u8v1a", "corrodes statues and buildings", mc("u8v1a_q", "M", "O1", "Which acid does your stomach make?", "Hydrochloric acid", [("Citric acid", "Lemons."), ("Sulfuric acid", "Batteries."), ("Ethanoic acid", "Vinegar.")])),
            stop("u8v1b", "to stop it spitting", mc("u8v1b_q", "M", "O1", "The safe way to dilute an acid is…", "add the acid slowly to water", [("add water to the acid", "Can spit."), ("taste it", "Never."), ("heat it", "No.")])),
            stop("u8v1c", "you'll hear a squeaky pop", mc("u8v1c_q", "H", "O1", "Which gas turns limewater milky?", "Carbon dioxide", [("Hydrogen", "Squeaky pop."), ("Oxygen", "Relights splint."), ("Nitrogen", "No.")]))],
    "8.2": [stop("u8v2a", "to make a salt and water", mc("u8v2a_q", "M", "O2", "Alkalis turn red litmus…", "blue", [("red", "No change."), ("green", "No."), ("yellow", "No.")]))],
    "8.3": [stop("u8v3a", "turning red-orange in alkalis", mc("u8v3a_q", "M", "O3", "Red cabbage juice in lemon juice turns…", "red", [("purple", "Neutral."), ("green", "Alkali."), ("yellow", "Alkali.")])),
            stop("u8v3b", "drain cleaner", mc("u8v3b_q", "H", "O3", "pH 3 is…", "acidic", [("neutral", "No."), ("alkaline", "No."), ("pure water", "No.")])),
            stop("u8v3c", "neutral to alkaline soil", mc("u8v3c_q", "H", "O3", "Universal Indicator is better than litmus because it…", "shows how acidic or alkaline", [("is cheaper", "No."), ("is a metal", "No."), ("only shows acid", "No.")]))],
    "8.4": [stop("u8v4a", "This method is called titration", mc("u8v4a_q", "M", "O4", "Acid + alkali →", "salt + water", [("hydrogen", "No."), ("carbon dioxide", "No."), ("oxygen", "No.")])),
            stop("u8v4b", "in a process called scrubbing", mc("u8v4b_q", "H", "O4", "Antacid tablets work by…", "neutralising extra stomach acid", [("adding acid", "No."), ("cooling the stomach", "No."), ("killing bacteria", "No.")]))],
}

MINDMAP = {"id": "root", "t": "Acids and alkalis", "sec": None, "kids": [
    {"id": "acid", "t": "Acids", "d": "Citric, ethanoic, hydrochloric… • sour, corrosive, conduct • blue litmus → red • + carbonate → CO₂ (limewater milky) • + metal → H₂ (squeaky pop) • safety: goggles, add acid to water.", "obj": "O1", "sec": "8.1"},
    {"id": "alk", "t": "Alkalis", "d": "Soap, toothpaste, ammonia, sodium hydroxide • bitter, soapy • red litmus → blue.", "obj": "O2", "sec": "8.2"},
    {"id": "ph", "t": "Indicators and pH", "d": "Litmus, red cabbage, turmeric • pH 0–14, 7 neutral • Universal Indicator, pH meter • hydrangeas.", "obj": "O3", "sec": "8.3"},
    {"id": "neut", "t": "Neutralisation", "d": "Acid + alkali → salt + water at pH 7 • titration • antacids, scrubbing, liming lakes, conditioner.", "obj": "O4", "sec": "8.4"},
]}
