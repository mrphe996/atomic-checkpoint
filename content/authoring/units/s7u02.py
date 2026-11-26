# -*- coding: utf-8 -*-
"""Stage 7 Unit 2 – Measurements. Written by the Camday teaching team."""
from c_kit import *

STRAND = "Thinking and Working Scientifically"
BLURB = "Why scientists measure, SI units, and how to measure length, area, volume, mass and time accurately – avoiding parallax errors and outliers."

OBJECTIVES = {
    "O1": {"sec": "2.1", "code": "7TWSc.04", "codeNote": "", "t": "Distinguish qualitative and quantitative observations and name SI units for physical quantities."},
    "O2": {"sec": "2.2", "code": "7TWSc.02, 7TWSc.04", "codeNote": "", "t": "Measure length with suitable instruments, convert units and avoid parallax error."},
    "O3": {"sec": "2.2", "code": "7TWSc.03, 7TWSa.02", "codeNote": "", "t": "Repeat measurements, spot outliers, calculate averages and explain accuracy and precision."},
    "O4": {"sec": "2.3", "code": "7TWSm.02", "codeNote": "using formulae", "t": "Calculate area (base × height) and convert units of area."},
    "O5": {"sec": "2.4", "code": "7TWSc.02, 7TWSc.04", "codeNote": "", "t": "Measure volume with a measuring cylinder (meniscus) and by displacement; convert units of volume."},
    "O6": {"sec": "2.5", "code": "7TWSc.02", "codeNote": "", "t": "Measure mass with a balance, using tare, and convert units of mass."},
    "O7": {"sec": "2.6", "code": "7TWSc.04", "codeNote": "", "t": "Measure time intervals and convert units of time."},
}

SECTIONS = [
    {"id": "2.1", "title": "Physical quantities", "objs": ["O1"]},
    {"id": "2.2", "title": "Measuring length", "objs": ["O2", "O3"]},
    {"id": "2.3", "title": "Area", "objs": ["O4"]},
    {"id": "2.4", "title": "Volume", "objs": ["O5"]},
    {"id": "2.5", "title": "Mass", "objs": ["O6"]},
    {"id": "2.6", "title": "Time", "objs": ["O7"]},
]

# ---------------------------------------------------------------- 2.1
S1_REQ = [
    gd("u2s1r1", "M", "O1", "Qualitative or quantitative?", ["Type"],
       [("She runs fast", ["Qualitative"]), ("She runs 100 m in 14.2 s", ["Quantitative"]), ("The water feels warm", ["Qualitative"]), ("The water is 32 °C", ["Quantitative"]), ("The leaf is bright green", ["Qualitative"])], skill="Data"),
    mt("u2s1r2", "M", "O1", "Match each physical quantity to its SI unit.", [("Length", "metre (m)"), ("Mass", "kilogram (kg)"), ("Time", "second (s)"), ("Temperature", "kelvin (K)"), ("Electric current", "ampere (A)")]),
    mc("u2s1r3", "M", "O1", "Why do scientists use standard units?", ("So measurements can be compared anywhere in the world.", "Correct."), [("Because they are shorter words.", "No."), ("To make maths harder.", "No."), ("Because body parts are the same for everyone.", "They are not – that is the problem.")]),
    mc("u2s1r4", "H", "O1", "Why was the cubit not a good unit?", ("People's arms are different lengths, so a cubit varied.", "Correct."), [("Elbows did not exist.", "No."), ("It was too accurate.", "No."), ("It was made of metal.", "No.")]),
    mc("u2s1r5", "H", "O1", "In 1875 the metre bar was made of platinum and iridium. Why?", ("The alloy is hard and does not rust or scratch easily, so its length stays the same.", "Correct."),
       [("It was cheap.", "Platinum is expensive."), ("It was soft and bendy.", "It was hard."), ("It glowed in the dark.", "No.")], skill="Reasoning"),
    ex("u2s1r6", "H", "O1", "Explain why quantitative observations are more useful in science than qualitative ones.",
       [("use numbers / measured with instruments", ["number|measur|instrument"]), ("objective / not opinion / can be compared", ["objective|opinion|compar|fact"])],
       "Quantitative observations use numbers measured with instruments, so they are objective – based on facts, not opinions – and can be compared and repeated by others.", need=2),
    tb("u2s1r7", "H", "O1", "Data: a runner's times for 100 m. Complete the differences from her best time (13.8 s).", ["Race", "Time (s)", "Slower than best by (s)"],
       [["1", "14.2", B(0.4)], ["2", "13.8", B(0)], ["3", "14.5", B(0.7)]], skill="Data"),
    ms("u2s1r8", "M", "O1", "Select ALL the physical quantities.", ["Length", "Mass", "Time", "Temperature"], [("Beauty", "Cannot be measured with an instrument."), ("Kindness", "Not a physical quantity.")]),
]
S1_PRAC = [
    mc("u2s1p01", "M", "O1", "A qualitative observation is described…", "in words", [("with numbers", "Quantitative."), ("with a graph only", "No."), ("in SI units", "No.")]),
    mc("u2s1p02", "M", "O1", "A quantitative observation uses…", "numbers", [("only words", "Qualitative."), ("colours", "No."), ("opinions", "No.")]),
    mc("u2s1p03", "M", "O1", "The SI unit of mass is the…", "kilogram", [("gram", "Common, but not the SI base unit."), ("newton", "Force."), ("litre", "Volume.")]),
    mc("u2s1p04", "M", "O1", "The SI unit of temperature is the…", "kelvin", [("degree Celsius", "Common, but SI is kelvin."), ("metre", "Length."), ("second", "Time.")]),
    mc("u2s1p05", "M", "O1", "The SI unit of electric current is the…", "ampere", [("volt", "Voltage."), ("watt", "Power."), ("kelvin", "Temperature.")]),
    mc("u2s1p06", "M", "O1", "A physical quantity is…", "something in the physical world that can be measured", [("a feeling", "No."), ("a colour you like", "No."), ("a type of instrument", "No.")]),
    mc("u2s1p07", "H", "O1", "Why are world records only possible with standard units?", "Times and distances from different countries can be compared fairly.", [("Athletes like units.", "No."), ("Units make people run faster.", "No."), ("Records are not measured.", "They are.")]),
    mc("u2s1p08", "M", "O1", "Which instrument measures temperature?", "Thermometer", [("Stopwatch", "Time."), ("Balance", "Mass."), ("Tape measure", "Length.")]),
    mc("u2s1p09", "M", "O1", "Which instrument measures mass?", "Electronic balance", [("Thermometer", "Temperature."), ("Ruler", "Length."), ("Stopwatch", "Time.")]),
    mc("u2s1p10", "H", "O1", "Observations made with instruments are…", "objective – based on facts", [("subjective – based on opinion", "No."), ("always wrong", "No."), ("qualitative", "Usually quantitative.")]),
    mc("u2s1p11", "H", "O1", "Which is quantitative?", "The plant grew 4.5 cm in a week", [("The plant grew a lot", "Words only."), ("The plant looks healthy", "Words only."), ("The plant smells nice", "Words only.")]),
    mc("u2s1p12", "M", "O1", "Where was the 1875 metre bar kept?", "Locked away in Paris", [("In London", "No."), ("On the Moon", "No."), ("In every school", "No.")]),
    mc("u2s1p13", "H", "O1", "How does measuring help protect the environment?", "Scientists measure air quality, pollution and populations to see changes.", [("It stops all pollution.", "It helps us see it."), ("It makes animals grow.", "No."), ("It does not help.", "It does.")]),
    gd("u2s1p14", "M", "O1", "Which instrument would you use?", ["Instrument"], [("Temperature of soup", ["Thermometer"]), ("Time for a race", ["Stopwatch"]), ("Mass of an apple", ["Balance"]), ("Length of a desk", ["Tape measure"])], skill="Data"),
    mc("u2s1p15", "H", "O1", "Which unit symbol is written correctly?", "kg", [("KG", "Lower case k and g."), ("Kg", "Lower case k."), ("kG", "Lower case g.")]),
    mc("u2s1p16", "M", "O1", "Before standard units, people measured with…", "parts of their bodies", [("lasers", "Much later."), ("computers", "Much later."), ("satellites", "No.")]),
    mc("u2s1p17", "H", "O1", "A pupil writes 'the pencil is long'. How could she make this quantitative?", "Measure it with a ruler and give the length in cm", [("Say it is very long", "Still words."), ("Draw it", "Not a measurement."), ("Ask a friend", "Still opinion.")]),
    od("u2s1p18", "M", "O1", "Order how length measurement developed.", ["Body parts such as the cubit", "Sticks and string with standard lengths", "Platinum–iridium metre bar (1875)", "Modern instruments such as tape measures"]),
]
S1_ADV = [
    adv(ex("u2s1a1", "VH", "O1", "Two schools time the same race. One uses hand-held stopwatches, the other electronic sensors. Explain which times are more trustworthy and why.",
           [("electronic sensors more accurate", ["electronic|sensor"]), ("human reaction time causes error", ["reaction|human|press|delay"])],
           "Electronic sensors start and stop automatically, so they avoid human reaction-time errors. Hand-held stopwatches depend on how quickly a person presses the button, which adds error.", need=2)),
    adv(mc("u2s1a2", "VH", "O1", "Why is the kelvin, not the degree Celsius, the SI unit of temperature?", ("The kelvin scale starts at absolute zero, the lowest possible temperature.", "Correct."),
           [("Celsius does not exist.", "It does."), ("Kelvin is easier to read on thermometers.", "Not the reason."), ("Kelvin is only used in Paris.", "No.")], skill="Reasoning")),
    adv(nm("u2s1a3", "VH", "O1", "A cubit is about 45 cm. A boat is 20 cubits long. About how long is it in metres?", 9, "m", units=["m", "cm"], reason="20 × 45 cm = 900 cm = 9 m.")),
    adv(mc("u2s1a4", "VH", "O1", "Why might a measurement be 'quantitative' but still not useful?", ("If the instrument was used wrongly or is not accurate, the number may be wrong.", "Correct."),
           [("Numbers are never useful.", "No."), ("Quantitative always means correct.", "No."), ("Units are optional.", "No.")], skill="Reasoning")),
]

# ---------------------------------------------------------------- 2.2
S2_REQ = [
    nm("u2s2r1", "M", "O2", "Convert 2.5 km to metres.", 2500, "m", errs=[(250, "1 km = 1000 m, so multiply by 1000.")], hint="Big unit → small unit: multiply."),
    nm("u2s2r2", "M", "O2", "Convert 45 mm to centimetres.", 4.5, "cm", errs=[(450, "Small unit → big unit: divide by 10.")], hint="1 cm = 10 mm."),
    gd("u2s2r3", "H", "O2", "Choose the best instrument.", ["Instrument"],
       [("Your waist", ["Soft tape measure"]), ("Width of a pin", ["Vernier calipers"]), ("A sports field", ["Measuring wheel"]), ("A pen", ["30 cm rule"]), ("Distance a car travels", ["Odometer"])], skill="Data"),
    mc("u2s2r4", "H", "O2", "Reading a rule from an angle gives 19.8 cm or 20.2 cm instead of 20.0 cm. This is called…", ("a parallax error", "Correct – look vertically down at the mark."), [("a zero error", "Different error."), ("an outlier", "An outlier is a result that does not fit."), ("precision", "No.")]),
    tb("u2s2r5", "H", "O3", "Paper clip lengths (cm). Leave out the outlier and complete the average.", ["Trial 1", "Trial 2", "Trial 3", "Average (cm)"], [["3.2", "3.0", "26.8", B(3.1)]], skill="Data",
       hint="26.8 cm is not reasonable for a paper clip.", reason="(3.2 + 3.0) ÷ 2 = 3.1 cm."),
    gd("u2s2r6", "VH", "O3", "Darts on a target (centre = true value). Describe each pattern.", ["Description"],
       [("All close together at the centre", ["Accurate and precise"]), ("Close together but far from centre", ["Precise, not accurate"]), ("Spread out, far from centre", ["Neither"])], skill="Data"),
    ex("u2s2r7", "H", "O3", "Explain why you should repeat a measurement at least three times.",
       [("spot outliers / mistakes", ["outlier|mistake|wrong|error"]), ("check results are close / precise", ["close|precise|agree"]), ("calculate an average", ["average|mean"])],
       "Repeating lets you spot an outlier or mistake, check that results are close together (precise), and calculate an average that is closer to the true value.", need=2),
    mc("u2s2r8", "M", "O2", "Before measuring with a rule, you should…", ("line up one end of the object with the zero mark", "Correct."), [("start from the 1 cm mark without adjusting", "That adds 1 cm error."), ("hold the rule at an angle", "Parallax error."), ("guess the length", "No.")]),
]
S2_PRAC = [
    mc("u2s2p01", "M", "O2", "'Kilo' means…", "a thousand", [("a hundred", "Centi is a hundredth."), ("a thousandth", "Milli."), ("a million", "Mega.")]),
    mc("u2s2p02", "M", "O2", "'Milli' means…", "one thousandth", [("one hundredth", "Centi."), ("a thousand", "Kilo."), ("ten", "No.")]),
    nm("u2s2p03", "M", "O2", "How many centimetres are in 3 m?", 300, "cm"),
    nm("u2s2p04", "M", "O2", "Convert 1200 m to km.", 1.2, "km", errs=[(1200000, "Small → big: divide by 1000.")]),
    nm("u2s2p05", "M", "O2", "Convert 7 cm to mm.", 70, "mm"),
    nm("u2s2p06", "H", "O2", "Convert 0.35 m to cm.", 35, "cm"),
    nm("u2s2p07", "H", "O2", "Convert 2 km to cm.", 200000, "cm", reason="2 km = 2000 m = 200 000 cm."),
    mc("u2s2p08", "M", "O2", "To avoid parallax error, put your eye…", "directly above the mark", [("to the left", "Error."), ("to the right", "Error."), ("far away", "Not the point.")]),
    mc("u2s2p09", "M", "O2", "A theodolite is used by surveyors to measure…", "distances and angles", [("mass", "No."), ("temperature", "No."), ("time", "No.")]),
    mc("u2s2p10", "H", "O2", "A hard tape measure is best for…", "rooms and furniture", [("your waist", "Soft tape."), ("a pin", "Vernier calipers."), ("a car journey", "Odometer.")]),
    mc("u2s2p11", "M", "O3", "A result that does not fit the pattern is an…", "outlier", [("average", "No."), ("accurate result", "No."), ("instrument", "No.")]),
    mc("u2s2p12", "H", "O3", "Three measurements are enough if…", "at least two of them are close together", [("they are all different", "Then repeat more."), ("one is very big", "Check it."), ("you are tired", "No.")]),
    nm("u2s2p13", "H", "O3", "Find the average of 12.4, 12.6 and 12.5 cm.", 12.5, "cm", tol=0.01),
    mc("u2s2p14", "M", "O3", "Precise means…", "close to one another", [("close to the true value", "Accurate."), ("very big", "No."), ("written in words", "No.")]),
    mc("u2s2p15", "M", "O3", "Accurate means…", "close to the true value", [("close to one another", "Precise."), ("measured once", "No."), ("in kilometres", "No.")]),
    mc("u2s2p16", "H", "O3", "If other people repeat your measurement and get the same results, your results are…", "reliable", [("biased", "No."), ("qualitative", "No."), ("outliers", "No.")]),
    mc("u2s2p17", "H", "O3", "A paper clip measured as 26.8 cm is probably…", "a mistake – measure again", [("correct", "Not reasonable."), ("the average", "No."), ("very precise", "No.")]),
    od("u2s2p18", "M", "O2", "Order from smallest to largest.", ["1 mm", "1 cm", "1 m", "1 km"]),
]
S2_ADV = [
    adv(nm("u2s2a1", "VH", "O2", "Vernier calipers read 0.25 cm for a pin. What is that in mm?", 2.5, "mm")),
    adv(ex("u2s2a2", "VH", "O3", "Results: 15.1, 15.2, 18.7, 15.0 cm. Explain how to report the length.",
           [("18.7 is an outlier", ["18\\.7|outlier"]), ("average the others", ["average|mean"]), ("≈ 15.1 cm", ["15\\.1"])],
           "18.7 cm does not fit, so it is an outlier and is left out. The average of 15.1, 15.2 and 15.0 is 45.3 ÷ 3 = 15.1 cm.", need=2)),
    adv(mc("u2s2a3", "VH", "O3", "A ruler's end is worn so every reading is 2 mm too long. The results are…", ("precise but not accurate", "Correct – a systematic error."), [("accurate but not precise", "No."), ("accurate and precise", "No."), ("outliers", "No.")], skill="Reasoning")),
    adv(nm("u2s2a4", "VH", "O2", "A running track lap is 400 m. How many laps make 10 km?", 25, "laps")),
]

# ---------------------------------------------------------------- 2.3
S3_REQ = [
    nm("u2s3r1", "M", "O4", "A tile is 12 cm long and 7 cm high. What is its area?", 84, "cm²", units=["cm²", "cm"], unitFb="Area is measured in square units.", errs=[(19, "You added. Area = base × height.")]),
    mc("u2s3r2", "M", "O4", "Area is…", ("the space taken up by a flat surface", "Correct."), [("the distance around a shape", "That is perimeter."), ("the space inside a 3D object", "Volume."), ("the mass of an object", "No.")]),
    nm("u2s3r3", "H", "O4", "How many cm² are in 1 m²?", 10000, "cm²", errs=[(100, "Square the factor: 100 × 100 = 10 000.")]),
    tb("u2s3r4", "H", "O4", "Complete the areas of the rectangles.", ["Base (cm)", "Height (cm)", "Area (cm²)"], [["5", "4", B(20)], ["8", "6", B(48)], ["10", "10", B(100)], ["2.5", "4", B(10)]], skill="Data"),
    mc("u2s3r5", "M", "O4", "The SI unit of area is the…", "square metre (m²)", [("metre (m)", "Length."), ("cubic metre (m³)", "Volume."), ("litre", "Volume.")]),
    ex("u2s3r6", "H", "O4", "Explain why 1 m² is 10 000 cm², not 100 cm².",
       [("1 m = 100 cm", ["100 ?cm|1 ?m"]), ("square both sides: 100 × 100", ["100 ?(×|x|\\*) ?100|squar|both"])],
       "A 1 m × 1 m square is 100 cm × 100 cm. Area = 100 × 100 = 10 000 cm², because you multiply both sides by 100.", need=2),
    nm("u2s3r7", "H", "O4", "A mosaic has 10 rows of 10 tiles, each 1 cm². What is its area?", 100, "cm²", skill="Data"),
    nm("u2s3r8", "VH", "O4", "A classroom floor is 8 m by 6 m. Carpet costs $5 per m². How much does carpet cost?", 240, "$", reason="8 × 6 = 48 m²; 48 × 5 = $240.", skill="Application"),
]
S3_PRAC = [
    nm("u2s3p01", "M", "O4", "Area of a 3 cm × 3 cm square?", 9, "cm²"),
    nm("u2s3p02", "M", "O4", "Area of a 6 m × 2 m rectangle?", 12, "m²"),
    nm("u2s3p03", "M", "O4", "A rectangle has area 24 cm² and base 6 cm. Height?", 4, "cm"),
    nm("u2s3p04", "H", "O4", "Convert 3 m² to cm².", 30000, "cm²"),
    nm("u2s3p05", "H", "O4", "Convert 50 000 cm² to m².", 5, "m²"),
    nm("u2s3p06", "M", "O4", "Area of a 15 cm × 10 cm book cover?", 150, "cm²"),
    mc("u2s3p07", "M", "O4", "Which unit is an area unit?", "cm²", [("cm", "Length."), ("cm³", "Volume."), ("kg", "Mass.")]),
    nm("u2s3p08", "H", "O4", "How many 1 cm² tiles cover a 20 cm × 5 cm strip?", 100, "tiles"),
    nm("u2s3p09", "H", "O4", "A garden is 12 m × 4 m. What is its area?", 48, "m²"),
    mc("u2s3p10", "H", "O4", "Two shapes: A is 4 cm × 9 cm, B is 6 cm × 6 cm. Which has the bigger area?", "They are equal (36 cm²)", [("A", "Both 36 cm²."), ("B", "Both 36 cm²."), ("Cannot tell", "Calculate.")]),
    nm("u2s3p11", "H", "O4", "A square has area 49 cm². How long is each side?", 7, "cm"),
    nm("u2s3p12", "M", "O4", "Area of a 2 cm × 2 cm stamp?", 4, "cm²"),
    mc("u2s3p13", "H", "O4", "Doubling both the base and the height of a rectangle makes its area…", "four times bigger", [("twice as big", "2 × 2 = 4."), ("the same", "No."), ("half", "No.")], skill="Reasoning"),
    nm("u2s3p14", "H", "O4", "Convert 2.5 m² to cm².", 25000, "cm²"),
    nm("u2s3p15", "M", "O4", "A phone screen is 15 cm by 7 cm. Area?", 105, "cm²"),
    mc("u2s3p16", "M", "O4", "Area = base × …", "height", [("base", "No."), ("volume", "No."), ("mass", "No.")]),
    nm("u2s3p17", "H", "O4", "A wall 5 m × 3 m has a window 2 m × 1 m. Area of wall to paint?", 13, "m²", reason="15 − 2 = 13 m²."),
    mc("u2s3p18", "M", "O4", "Which instrument would you use to find the area of a sheet of paper?", "A ruler (measure base and height, then multiply)", [("A balance", "Mass."), ("A thermometer", "No."), ("A stopwatch", "No.")]),
]
S3_ADV = [
    adv(nm("u2s3a1", "VH", "O4", "A football pitch is 100 m by 64 m. What is its area in m²?", 6400, "m²")),
    adv(nm("u2s3a2", "VH", "O4", "Tiles are 20 cm × 20 cm. How many cover a 2 m × 1 m floor?", 50, "tiles", reason="Floor = 20 000 cm²; tile = 400 cm²; 20 000 ÷ 400 = 50.")),
    adv(ex("u2s3a3", "VH", "O4", "Describe how to estimate the area of a leaf using squared paper.",
           [("draw round the leaf on cm squares", ["draw|trace|outline", "square"]), ("count whole squares", ["count"]), ("count half or more as one / ignore less than half", ["half|part"])],
           "Draw round the leaf on 1 cm squared paper. Count the whole squares, then count squares that are half or more covered as one and ignore smaller parts. The total is the area in cm².", need=2)),
    adv(mc("u2s3a4", "VH", "O4", "A 1 km² park is how many m²?", ("1 000 000 m²", "Correct: 1000 × 1000."), [("1000 m²", "Square the factor."), ("100 000 m²", "No."), ("10 000 m²", "No.")])),
]

# ---------------------------------------------------------------- 2.4
S4_REQ = [
    mc("u2s4r1", "M", "O5", "Where should you read a measuring cylinder?", ("At the bottom of the meniscus, with your eye level with the liquid", "Correct."),
       [("At the top of the curve, looking down", "Parallax error."), ("Anywhere on the glass", "No."), ("From below the table", "No.")]),
    tb("u2s4r2", "M", "O5", "Displacement: complete the volume of each stone.", ["Start (cm³)", "With stone (cm³)", "Volume of stone (cm³)"], [["38", "49", B(11)], ["50", "62", B(12)], ["25", "40", B(15)]], skill="Data"),
    nm("u2s4r3", "M", "O5", "How many millilitres are in 2 litres?", 2000, "mL"),
    mc("u2s4r4", "M", "O5", "1 mL is the same as…", "1 cm³", [("1 m³", "Far bigger."), ("1 L", "1000 mL."), ("10 cm³", "No.")]),
    od("u2s4r5", "H", "O5", "Order the steps of the displacement method.", ["Pour water into a measuring cylinder", "Record the starting volume", "Lower the object in on a string", "Record the new volume", "Subtract to find the object's volume"]),
    ex("u2s4r6", "H", "O5", "Why can't you use a formula to find the volume of a stone, and what do you do instead?",
       [("irregular shape", ["irregular|not a regular|odd shape|no formula"]), ("use displacement / water rises", ["displac|water|rise|cylinder"])],
       "A stone has an irregular shape, so there is no simple formula. Put it in water in a measuring cylinder; the rise in water level equals its volume (displacement).", need=2),
    mc("u2s4r7", "H", "O5", "Why lower the stone gently on a string?", ("So water does not splash out and the cylinder does not break.", "Correct."), [("To make it heavier.", "No."), ("To cool it.", "No."), ("So it floats.", "No.")]),
    nm("u2s4r8", "VH", "O5", "A box is 10 cm × 5 cm × 4 cm. What is its volume in mL?", 200, "mL", reason="10 × 5 × 4 = 200 cm³ = 200 mL.", skill="Data"),
]
S4_PRAC = [
    mc("u2s4p01", "M", "O5", "Volume is…", "the amount of space taken up by an object or substance", [("the mass of an object", "No."), ("the area of a surface", "No."), ("how loud it is", "Different meaning.")]),
    mc("u2s4p02", "M", "O5", "The SI unit of volume is the…", "cubic metre (m³)", [("litre", "Common, not SI."), ("square metre", "Area."), ("kilogram", "Mass.")]),
    mc("u2s4p03", "M", "O5", "The curved surface of a liquid in a cylinder is the…", "meniscus", [("parallax", "An error."), ("outlier", "No."), ("scale", "No.")]),
    nm("u2s4p04", "M", "O5", "Convert 1.5 L to mL.", 1500, "mL"),
    nm("u2s4p05", "M", "O5", "Convert 750 mL to L.", 0.75, "L"),
    nm("u2s4p06", "H", "O5", "Water rises from 20 cm³ to 27 cm³ when a key is added. Key volume?", 7, "cm³"),
    nm("u2s4p07", "H", "O5", "1 L is how many cm³?", 1000, "cm³"),
    mc("u2s4p08", "H", "O5", "A student reads the top of the meniscus. The reading will be…", "a little too high", [("exactly right", "Read the bottom."), ("much too low", "No."), ("in grams", "No.")]),
    nm("u2s4p09", "M", "O5", "A cube has sides of 3 cm. Volume?", 27, "cm³"),
    mc("u2s4p10", "M", "O5", "Which unit is a volume unit?", "mL", [("mm", "Length."), ("mg", "Mass."), ("ms", "Time.")]),
    nm("u2s4p11", "H", "O5", "How many 250 mL cups fill a 2 L jug?", 8, "cups"),
    mc("u2s4p12", "H", "O5", "When a stone sinks in water, the water level rises because…", "the stone pushes aside its own volume of water", [("the stone dissolves", "No."), ("the water gets warmer", "No."), ("air comes out", "No.")]),
    nm("u2s4p13", "H", "O5", "A rectangular tank is 50 cm × 20 cm × 30 cm. Volume in litres?", 30, "L", reason="30 000 cm³ = 30 L."),
    mc("u2s4p14", "M", "O5", "Which apparatus measures the volume of a liquid accurately?", "Measuring cylinder", [("Beaker", "Less accurate."), ("Balance", "Mass."), ("Ruler", "Length.")]),
    nm("u2s4p15", "H", "O5", "Start 42 cm³, with three identical marbles 48 cm³. Volume of ONE marble?", 2, "cm³"),
    mc("u2s4p16", "H", "O5", "Why is a cubic metre often too big for school science?", "It is 1000 litres – far more than we usually measure.", [("It is too small.", "No."), ("It is a mass unit.", "No."), ("It is not SI.", "It is SI.")]),
    od("u2s4p17", "M", "O5", "Order from smallest to largest.", ["1 mL", "100 cm³", "1 L", "1 m³"]),
    mc("u2s4p18", "M", "O5", "To avoid parallax, your eye must be…", "level with the liquid surface", [("above the cylinder", "Too high."), ("below the table", "Too low."), ("closed", "No.")]),
]
S4_ADV = [
    adv(ex("u2s4a1", "VH", "O5", "How could you find the volume of a cork, which floats?",
           [("push it under / sinker", ["push|sink|weight|sinker|pin"]), ("measure rise and subtract sinker", ["subtract|rise|differen"])],
           "Tie a heavy sinker to it. Measure the water level with the sinker alone, then with the sinker and cork fully under water. The difference is the cork's volume.", need=2)),
    adv(nm("u2s4a2", "VH", "O5", "A rock displaces water from 120 cm³ to 155 cm³ and has a mass of 87.5 g. Its density is mass ÷ volume. Density in g/cm³?", 2.5, "g/cm³", reason="Volume 35 cm³; 87.5 ÷ 35 = 2.5 g/cm³.")),
    adv(mc("u2s4a3", "VH", "O5", "A measuring cylinder has 1 cm³ divisions. Which reading is sensible?", ("36.5 cm³ (half-way between marks)", "Correct – estimate to half a division."), [("36.527 cm³", "Too many decimals."), ("about 40", "Too rough."), ("36 kg", "Wrong unit.")], skill="Measurement")),
    adv(nm("u2s4a4", "VH", "O5", "How many cm³ are in 1 m³?", 1000000, "cm³")),
]

# ---------------------------------------------------------------- 2.5
S5_REQ = [
    mc("u2s5r1", "M", "O6", "Mass is…", ("the amount of matter in an object", "Correct."), [("the space it takes up", "Volume."), ("how hot it is", "Temperature."), ("the pull of gravity", "Weight.")]),
    nm("u2s5r2", "M", "O6", "Convert 3.2 kg to grams.", 3200, "g"),
    nm("u2s5r3", "M", "O6", "Convert 450 mg to grams.", 0.45, "g"),
    od("u2s5r4", "H", "O6", "Order the steps to find the mass of salt in a beaker using tare.", ["Switch on and zero the balance", "Put the empty beaker on the balance", "Press tare – reading goes to zero", "Add the salt", "Read the mass of the salt"]),
    tb("u2s5r5", "H", "O6", "Complete the mass of each substance.", ["Beaker + substance (g)", "Empty beaker (g)", "Substance (g)"], [["125", "100", B(25)], ["87.5", "62.0", B(25.5)], ["210", "145", B(65)]], skill="Data"),
    ex("u2s5r6", "H", "O6", "Explain what the tare button does and why it is useful.",
       [("sets reading to zero with container on", ["zero"]), ("so you measure only the substance / not the container", ["only|container|beaker|substance"])],
       "Tare resets the balance to zero with the empty container on it, so the reading shows only the mass of the substance added, not the container.", need=2),
    gd("u2s5r7", "H", "O6", "Best unit for each mass.", ["Unit"], [("A feather", ["mg or g"]), ("A cat", ["kg"]), ("A suitcase", ["kg"]), ("A grain of salt", ["mg or g"])], skill="Data"),
    mc("u2s5r8", "VH", "O6", "A balance shows 2.0 g with nothing on it. A stone reads 15.0 g. What is the true mass?", ("13.0 g – subtract the zero error", "Correct."), [("15.0 g", "Ignores the error."), ("17.0 g", "Add? No, subtract."), ("2.0 g", "No.")], skill="Measurement"),
]
S5_PRAC = [
    mc("u2s5p01", "M", "O6", "The SI unit of mass is the…", "kilogram", [("gram", "Smaller unit."), ("newton", "Force."), ("litre", "Volume.")]),
    nm("u2s5p02", "M", "O6", "How many grams in 1 kg?", 1000, "g"),
    nm("u2s5p03", "M", "O6", "How many mg in 1 g?", 1000, "mg"),
    nm("u2s5p04", "M", "O6", "Convert 2500 g to kg.", 2.5, "kg"),
    nm("u2s5p05", "H", "O6", "Convert 0.008 g to mg.", 8, "mg"),
    mc("u2s5p06", "M", "O6", "We measure mass with a…", "balance", [("ruler", "Length."), ("measuring cylinder", "Volume."), ("thermometer", "Temperature.")]),
    mc("u2s5p07", "M", "O6", "Before measuring, a balance should read…", "zero", [("ten", "No."), ("anything", "Zero it."), ("the last result", "Zero it.")]),
    mc("u2s5p08", "M", "O6", "A cat's mass is about…", "3–5 kg", [("3–5 g", "Far too small."), ("3–5 mg", "No."), ("300 kg", "No.")]),
    nm("u2s5p09", "H", "O6", "A bag of rice is 1.25 kg. In grams?", 1250, "g"),
    mc("u2s5p10", "H", "O6", "Two types of balance are…", "beam balances and electronic balances", [("rulers and tapes", "No."), ("cylinders and beakers", "No."), ("clocks and timers", "No.")]),
    nm("u2s5p11", "H", "O6", "Empty beaker 50 g, with water 175 g. Mass of water?", 125, "g"),
    mc("u2s5p12", "M", "O6", "Which is the smallest mass?", "500 mg", [("5 g", "5000 mg."), ("0.5 kg", "500 000 mg."), ("50 g", "No.")]),
    nm("u2s5p13", "H", "O6", "How many 250 g packs make 2 kg?", 8, "packs"),
    mc("u2s5p14", "H", "O6", "Why not include the container's mass in your result?", "You only want the mass of the substance.", [("Containers have no mass.", "They do."), ("It makes the balance break.", "No."), ("It is the rule for liquids only.", "No.")]),
    od("u2s5p15", "M", "O6", "Order from lightest to heaviest.", ["Feather (about 0.008 g)", "Pencil (about 5 g)", "Apple (about 150 g)", "Cat (about 4 kg)"]),
    nm("u2s5p16", "H", "O6", "A suitcase limit is 23 kg. Yours is 25.4 kg. How much must you remove?", 2.4, "kg", tol=0.01),
    mc("u2s5p17", "M", "O6", "Mass is measured in…", "kilograms, grams or milligrams", [("metres", "Length."), ("litres", "Volume."), ("seconds", "Time.")]),
    mc("u2s5p18", "H", "O6", "An electronic balance reads to 0.1 g. Which reading is possible?", "12.3 g", [("12.34 g", "Too many decimals for this balance."), ("12.3 kg", "Wrong size."), ("twelve-ish", "Not a reading.")], skill="Measurement"),
]
S5_ADV = [
    adv(nm("u2s5a1", "VH", "O6", "50 identical paper clips have a mass of 25 g. Mass of one clip in mg?", 500, "mg", reason="25 ÷ 50 = 0.5 g = 500 mg.")),
    adv(ex("u2s5a2", "VH", "O6", "A single grain of rice is too light for your balance. Describe how to find its mass.",
           [("weigh many grains together", ["many|100|lots|several"]), ("divide by the number of grains", ["divide|÷"])],
           "Measure the mass of a large number of grains, e.g. 100, then divide the total mass by 100 to get the mass of one grain.", need=2)),
    adv(mc("u2s5a3", "VH", "O6", "An astronaut's mass on the Moon compared with on Earth is…", ("the same – mass is the amount of matter", "Correct (weight changes, mass does not)."), [("smaller", "Weight is smaller; mass is the same."), ("bigger", "No."), ("zero", "No.")], skill="Reasoning")),
    adv(nm("u2s5a4", "VH", "O6", "1 tonne = 1000 kg. A lorry carries 3.5 tonnes. Mass in kg?", 3500, "kg")),
]

# ---------------------------------------------------------------- 2.6
S6_REQ = [
    mc("u2s6r1", "M", "O7", "The SI unit of time is the…", "second", [("minute", "Common, not SI."), ("hour", "Not SI base."), ("day", "No.")]),
    nm("u2s6r2", "M", "O7", "How many seconds in 3 minutes?", 180, "s"),
    nm("u2s6r3", "H", "O7", "How many seconds in 1 hour?", 3600, "s", errs=[(60, "1 hour = 60 minutes, each 60 s: 60 × 60.")]),
    tb("u2s6r4", "H", "O7", "Convert each time to seconds.", ["Time", "Seconds"], [["2 min", B(120)], ["1 min 30 s", B(90)], ["0.5 h", B(1800)]], skill="Data"),
    mt("u2s6r5", "M", "O7", "Match the timekeeper to how it works.", [("Sundial", "shadow from the Sun"), ("Hourglass", "sand flowing through a narrow neck"), ("Stopwatch", "measures a time interval")]),
    ex("u2s6r6", "H", "O7", "Why do scientists use a stopwatch or laboratory timer, rather than a clock on the wall, to time a falling ball?",
       [("short interval / precise", ["short|second|precise|fraction|decimal"]), ("start and stop exactly", ["start|stop|interval"])],
       "The fall takes only a short time, so we need to start and stop timing exactly and read fractions of a second – a stopwatch measures a time interval precisely; a wall clock does not.", need=2),
    gr("u2s6r7", "H", "O7", "Data: time for a toy car to travel different distances. Plot the points.", {"label": "Distance (m)", "min": 0, "max": 5, "step": 1}, {"label": "Time (s)", "min": 0, "max": 10, "step": 1},
       [[1, 2], [2, 4], [3, 6], [4, 8]], follow=mc("u2s6r7f", "H", "O7", "Predict the time for 5 m.", ("10 s", "Correct – 2 s per metre."), [("8 s", "Pattern +2 s each metre."), ("12 s", "No."), ("5 s", "No.")])),
    mc("u2s6r8", "VH", "O7", "Hand timing always has a delay because of…", ("human reaction time", "Correct – about 0.2 s."), [("the stopwatch battery", "Not usually."), ("the speed of light", "No."), ("parallax", "That is for scales.")], skill="Reasoning"),
]
S6_PRAC = [
    nm("u2s6p01", "M", "O7", "How many minutes in 2 hours?", 120, "min"),
    nm("u2s6p02", "M", "O7", "Convert 240 s to minutes.", 4, "min"),
    nm("u2s6p03", "M", "O7", "Convert 90 minutes to hours.", 1.5, "h"),
    nm("u2s6p04", "H", "O7", "How many seconds in 2.5 minutes?", 150, "s"),
    mc("u2s6p05", "M", "O7", "Which measures the time of day?", "A clock or smartphone", [("A balance", "Mass."), ("A ruler", "Length."), ("A thermometer", "Temperature.")]),
    mc("u2s6p06", "M", "O7", "A time interval is…", "how long something takes", [("the time of day", "Not quite."), ("a type of clock", "No."), ("a distance", "No.")]),
    nm("u2s6p07", "H", "O7", "A race started at 10:15 and ended at 10:52. How many minutes?", 37, "min"),
    nm("u2s6p08", "H", "O7", "Convert 1 h 20 min to minutes.", 80, "min"),
    mc("u2s6p09", "M", "O7", "A sundial needs…", "sunlight to make a shadow", [("sand", "Hourglass."), ("electricity", "No."), ("water", "No.")]),
    nm("u2s6p10", "H", "O7", "How many seconds in a day?", 86400, "s", reason="24 × 60 × 60 = 86 400."),
    mc("u2s6p11", "H", "O7", "Which is the longest?", "200 s", [("3 min", "180 s."), ("0.05 h", "180 s."), ("150 s", "Shorter.")]),
    nm("u2s6p12", "H", "O7", "A stopwatch shows 01:05.4 (min:s). Total seconds?", 65.4, "s", tol=0.01),
    mc("u2s6p13", "H", "O7", "Why repeat a timing measurement?", "To reduce the effect of reaction-time errors and spot outliers", [("To make it longer", "No."), ("Because clocks are slow", "No."), ("It is not needed", "It is.")]),
    nm("u2s6p14", "M", "O7", "How many minutes in a quarter of an hour?", 15, "min"),
    mc("u2s6p15", "M", "O7", "Which instrument would time a 100 m race?", "Stopwatch", [("Sundial", "Too rough."), ("Hourglass", "Too rough."), ("Calendar", "No.")]),
    nm("u2s6p16", "H", "O7", "Times: 4.2, 4.4 and 4.3 s. Average?", 4.3, "s", tol=0.01),
    od("u2s6p17", "M", "O7", "Order from shortest to longest.", ["1 second", "1 minute", "1 hour", "1 day"]),
    mc("u2s6p18", "H", "O7", "Hourglasses and sundials were used before…", "clocks and watches", [("people measured time", "They were early ways to measure time."), ("the Sun existed", "No."), ("sand existed", "No.")]),
]
S6_ADV = [
    adv(ex("u2s6a1", "VH", "O7", "Timing ONE swing of a pendulum is hard. Describe a better method.",
           [("time many swings (e.g. 10)", ["10|ten|many|several"]), ("divide by the number of swings", ["divide|÷"]), ("reduces reaction-time error", ["reaction|error|accura"])],
           "Time 10 swings and divide the total by 10. The reaction-time error is shared over 10 swings, so the result is more accurate.", need=2)),
    adv(nm("u2s6a2", "VH", "O7", "20 swings take 36 s. Time for one swing?", 1.8, "s")),
    adv(mc("u2s6a3", "VH", "O7", "World 100 m records are timed to 0.01 s with electronic timing. Why not hand-timed?", ("Human reaction time (~0.2 s) is far bigger than 0.01 s.", "Correct."), [("Hand timing is illegal.", "No."), ("Stopwatches only show minutes.", "No."), ("Runners prefer it.", "No.")], skill="Reasoning")),
    adv(nm("u2s6a4", "VH", "O7", "A car travels 120 m in 8 s. How many metres per second?", 15, "m/s")),
]

POOLS = {"2.1": (S1_REQ, S1_PRAC, S1_ADV), "2.2": (S2_REQ, S2_PRAC, S2_ADV), "2.3": (S3_REQ, S3_PRAC, S3_ADV),
         "2.4": (S4_REQ, S4_PRAC, S4_ADV), "2.5": (S5_REQ, S5_PRAC, S5_ADV), "2.6": (S6_REQ, S6_PRAC, S6_ADV)}

STOPS = {
    "2.1": [stop("u2v1a", "It uses numbers", mc("u2v1a_q", "M", "O1", "'She runs 100 m in 14.2 s' is…", "quantitative", [("qualitative", "It uses numbers."), ("an opinion", "No."), ("a hypothesis", "No.")])),
            stop("u2v1b", "But people's arms are not all the same size", mc("u2v1b_q", "M", "O1", "Why was the cubit a problem?", "It varied from person to person", [("It was too long", "No."), ("Nobody had elbows", "No."), ("It was in kg", "No.")])),
            stop("u2v1c", "electric current in amperes", mc("u2v1c_q", "M", "O1", "SI unit of length?", "metre", [("kilogram", "Mass."), ("second", "Time."), ("kelvin", "Temperature.")]))],
    "2.2": [stop("u2v2a", "one centimetre is 10 millimetres", nm("u2v2a_q", "M", "O2", "1 m = ? cm", 100, "cm")),
            stop("u2v2b", "Always look vertically down at the mark", mc("u2v2b_q", "M", "O2", "Reading from an angle causes…", "parallax error", [("an outlier", "No."), ("zero error", "No."), ("precision", "No.")])),
            stop("u2v2c", "our results are reliable", nm("u2v2c_q", "H", "O3", "Clip readings 3.2, 3.0 and 26.8 cm. Average without the outlier?", 3.1, "cm", tol=0.01)),
            stop("u2v2d", "but not accurate", mc("u2v2d_q", "H", "O3", "Close together but away from the target is…", "precise but not accurate", [("accurate but not precise", "No."), ("both", "No."), ("neither", "No.")]))],
    "2.3": [stop("u2v3a", "area equals base times height", nm("u2v3a_q", "M", "O4", "Area of 12 cm × 7 cm?", 84, "cm²"))],
    "2.4": [stop("u2v4a", "one millilitre equals one cubic centimetre", nm("u2v4a_q", "M", "O5", "1 L = ? mL", 1000, "mL")),
            stop("u2v4b", "read the level at the bottom of the meniscus", mc("u2v4b_q", "M", "O5", "Read a meniscus at its…", "bottom, eye level", [("top", "No."), ("side", "No."), ("anywhere", "No.")])),
            stop("u2v4c", "pushed aside its own volume of water", nm("u2v4c_q", "H", "O5", "38 cm³ → 49 cm³. Stone volume?", 11, "cm³"))],
    "2.5": [stop("u2v5a", "one gram is 1000 milligrams", nm("u2v5a_q", "M", "O6", "1 kg = ? g", 1000, "g")),
            stop("u2v5b", "only the mass of the substance", mc("u2v5b_q", "M", "O6", "The tare button…", "sets the reading to zero with the container on", [("adds the container's mass", "No."), ("turns it off", "No."), ("measures volume", "No.")]))],
    "2.6": [stop("u2v6a", "one minute is 60 seconds", nm("u2v6a_q", "M", "O7", "1 hour = ? seconds", 3600, "s")),
            stop("u2v6b", "a stopwatch or a laboratory timer", mc("u2v6b_q", "M", "O7", "Which measures a time interval?", "Stopwatch", [("Sundial", "Time of day."), ("Ruler", "No."), ("Balance", "No.")]))],
}

MINDMAP = {"id": "root", "t": "Measurements", "sec": None, "kids": [
    {"id": "q", "t": "Physical quantities", "d": "Qualitative (words) vs quantitative (numbers). SI: m, kg, s, K, A.", "obj": "O1", "sec": "2.1"},
    {"id": "len", "t": "Length", "d": "km, m, cm, mm • big→small × • choose the instrument • avoid parallax.", "obj": "O2", "sec": "2.2"},
    {"id": "rep", "t": "Good measurements", "d": "Repeat • drop outliers • average • accurate vs precise • reliable.", "obj": "O3", "sec": "2.2"},
    {"id": "area", "t": "Area", "d": "base × height • 1 m² = 10 000 cm².", "obj": "O4", "sec": "2.3"},
    {"id": "vol", "t": "Volume", "d": "1 L = 1000 mL = 1000 cm³ • read the bottom of the meniscus • displacement.", "obj": "O5", "sec": "2.4"},
    {"id": "mass", "t": "Mass", "d": "kg, g, mg • balances • tare.", "obj": "O6", "sec": "2.5"},
    {"id": "time", "t": "Time", "d": "s, min, h • stopwatch for intervals • reaction time.", "obj": "O7", "sec": "2.6"},
]}
