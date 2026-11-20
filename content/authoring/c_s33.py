# -*- coding: utf-8 -*-
from c_base import *

S33_REQ = [
 label("s33r1", "Label the neurone (nerve cell).", "neurone", {"endings": "Branched endings", "body": "Cell body with nucleus", "fibre": "Long fibre"}, "M", "O8",
   confuse={"Branched endings|Long fibre": "Branched endings RECEIVE messages; the long fibre CARRIES impulses a long distance."},
   hint="The many small branches receive messages; the long part carries impulses a long way.",
   twin=label("s33r1t", "Label the root hair cell extension and nucleus.", "roothair", {"extension": "Extension (root hair)", "nucleus": "Nucleus"}, "M", "O8")),
 graph("s33r2", "Data: A student measured how much water root hairs of different average lengths absorbed in 10 minutes. Plot all the points on the graph (tap the grid; tap a point again to remove it).",
   {"label": "Average root hair length (mm)", "min": 0, "max": 5, "step": 1}, {"label": "Water absorbed (mL)", "min": 0, "max": 10, "step": 1},
   [[1, 2], [2, 4], [3, 6], [4, 8]], "H", "O8",
   follow=mcq("s33r2f", "What does your graph show?", [
     O("Longer root hairs → more water absorbed, because surface area is larger", True, "Correct – a positive trend linked to surface area."),
     O("Longer root hairs absorb less water", False, "Look at the slope – it goes UP."),
     O("Length has no effect", False, "The points rise steadily."),
     O("Water makes root hairs longer", False, "Correlation direction: length was the variable changed.")], "H", "O8", "Data"),
   table_rows=[["1", "2"], ["2", "4"], ["3", "6"], ["4", "8"]],
   hint="Each pair (length, volume) is one point. The horizontal axis is length.",
   reason="Plot (1,2), (2,4), (3,6), (4,8). Straight line upward → positive relationship.",
   twin=graph("s33r2t", "Plot these two points: (1, 3) and (3, 9).", {"label": "Length (mm)", "min": 0, "max": 5, "step": 1}, {"label": "Water (mL)", "min": 0, "max": 10, "step": 1}, [[1, 3], [3, 9]], "M", "O8")),
 mcq("s33r3", "Which TWO features make a red blood cell good at carrying oxygen?", [
   O("Contains haemoglobin and has no nucleus", True, "Correct – more room for haemoglobin, which carries oxygen."),
   O("Has cilia and mucus", False, "Those are features of ciliated cells."),
   O("Has chloroplasts and a cell wall", False, "Those are plant features."),
   O("Has a long fibre and branched endings", False, "Those are neurone features."),
 ], "M", "O8", hint="Which pigment carries oxygen? Which part is missing to make more room?",
   twin=mcq("s33r3t", "What shape is a red blood cell?", [O("A disc with a dimple", True, "Yes – gives a large surface area."), O("A long column", False, "Palisade cells."), O("A cube", False, "No."), O("A branched star", False, "Neurones.")], "M", "O8")),
 match("s33r4", "Match each specialised cell to the feature that suits its function.", [
   ("Root hair cell", "long extension → large surface area for absorbing water"),
   ("Palisade cell", "many chloroplasts near the top of the leaf"),
   ("Red blood cell", "no nucleus → more room for haemoglobin"),
   ("Ciliated cell", "cilia that beat to move mucus"),
   ("Neurone", "long fibre to carry impulses quickly")], "H", "O8",
   twin=match("s33r4t", "Match two cells.", [("Palisade cell", "absorbs light for photosynthesis"), ("Ciliated cell", "moves mucus away from the lungs")], "M", "O8")),
 mcq("s33r5", "Palisade cells are found near the UPPER surface of a leaf. Why is this position useful?", [
   O("It is where the most light reaches, so their chloroplasts can absorb more light energy", True, "Correct."),
   O("It is closest to the soil water", False, "Roots are closest to soil water."),
   O("It protects the leaf from insects", False, "That's the epidermis' role."),
   O("It is where oxygen is stored", False, "Leaves do not store oxygen there."),
 ], "H", "O8", "Reasoning", hint="Which surface of a leaf does light reach first?",
   twin=mcq("s33r5t", "What do palisade cells have many of?", [O("Chloroplasts", True, "Yes."), O("Cilia", False, "No."), O("Haemoglobin", False, "No."), O("Branched endings", False, "No.")], "M", "O8")),
 explain("s33r6", "Explain how ciliated cells and mucus work together to protect the lungs.", [
   ("Mucus is sticky and traps dust/particles (and microorganisms).", [r"trap", r"sticky", r"catch"]),
   ("Cilia beat together / wave.", [r"beat", r"wave", r"sweep", r"move"]),
   ("This moves the mucus (with dust) AWAY from the lungs.", [r"away", r"out of|up (the|from)", r"throat", r"from the lungs"]),
 ], "Sticky mucus traps dust and other particles in the air we breathe in. The cilia on the ciliated cells beat together, sweeping the mucus with the trapped dust away from the lungs (up towards the throat).",
   "H", "O8", need=2, hint="Two steps: what TRAPS the dust? What MOVES it away?", reason="Trap (mucus) + move (cilia) + direction (away from lungs).",
   twin=mcq("s33r6t", "What traps dust in the air passages?", [O("Mucus", True, "Yes."), O("Cilia", False, "Cilia move it."), O("Haemoglobin", False, "No."), O("Chloroplasts", False, "No.")], "M", "O8")),
 multi("s33r7", "Select ALL the features of a neurone that help it carry messages.", [
   O("Branched endings to receive messages", True, ""), O("A long fibre to carry impulses quickly over long distances", True, ""),
   O("Many chloroplasts", False, "Neurones are animal cells – no chloroplasts."), O("Haemoglobin", False, "That's in red blood cells."),
 ], "M", "O8", twin=mcq("s33r7t", "Messages carried by neurones are called…", [O("impulses", True, "Electrical signals called impulses."), O("mucus", False, "No."), O("sap", False, "No."), O("oxygen", False, "No.")], "M", "O8")),
 mcq("s33r8", "'When different cells in an organism carry out different jobs.' What is this called?", [
   O("Division of labour", True, "Correct."), O("Cell theory", False, "Cell theory is about all living things being made of cells."),
   O("Photosynthesis", False, "That's how plants make food."), O("Respiration", False, "That releases energy.")], "M", "O8",
   twin=mcq("s33r8t", "A cell that has a special shape for a job is…", [O("specialised", True, "Yes."), O("unicellular", False, "No."), O("dead", False, "No."), O("a tissue", False, "No.")], "M", "O8")),
]

S33_PRAC = [
 mcq("s33p01", "A root hair cell has NO chloroplasts. Why?", [O("It is underground in the dark, so it cannot photosynthesise", True, "Correct."), O("Chloroplasts would block water", False, "Not the reason."), O("It is an animal cell", False, "It is a plant cell."), O("It is dead", False, "It is alive.")], "H", "O8", "Reasoning"),
 mcq("s33p02", "Which feature gives a red blood cell a LARGE surface area?", [O("Its dimpled disc shape", True, "Correct."), O("Having no nucleus", False, "That gives room for haemoglobin."), O("Haemoglobin", False, "That carries oxygen."), O("Its red colour", False, "Colour doesn't change area.")], "M", "O8"),
 mcq("s33p03", "Why do some neurones need to be up to 1 metre long?", [O("To carry impulses quickly over long distances, e.g. from the spine to the foot", True, "Correct."), O("To store more food", False, "No."), O("To absorb water", False, "That's root hairs."), O("To carry oxygen", False, "That's red blood cells.")], "H", "O8"),
 match("s33p04", "Match the cell to where it is found.", [("Palisade cell", "upper part of a leaf"), ("Root hair cell", "root, in the soil"), ("Ciliated cell", "lining of air passages"), ("Red blood cell", "in the blood")], "M", "O8"),
 mcq("s33p05", "'Multicellular organisms are made of just one type of cell.' Is this true?", [O("No – they have many types of specialised cells", True, "Correct."), O("Yes – all cells are the same", False, "Cells differ in shape and job."), O("Yes, but only in plants", False, "Plants also have many cell types."), O("Only animals have specialised cells", False, "Plants do too.")], "M", "O8"),
 mcq("s33p06", "Muscle cells change shape to lift your bag. What would muscle cells need lots of?", [O("Mitochondria, to release energy", True, "Correct – movement needs energy."), O("Chloroplasts", False, "Animal cells don't have them."), O("Cell walls", False, "Muscle cells must change shape – no wall."), O("Cilia", False, "No.")], "VH", "O8", "Reasoning"),
 multi("s33p07", "Select ALL specialised PLANT cells.", [O("Root hair cell", True, ""), O("Palisade cell", True, ""), O("Neurone", False, "Animal."), O("Ciliated cell", False, "Animal.")], "M", "O8"),
 mcq("s33p08", "A person has fewer red blood cells than normal. Which symptom is most likely?", [O("Feeling tired because less oxygen reaches body cells", True, "Correct – less oxygen for respiration."), O("Coughing up more mucus", False, "Linked to ciliated cells."), O("Losing the sense of touch", False, "Linked to neurones."), O("Growing taller", False, "No.")], "VH", "O8", "Reasoning"),
 mcq("s33p09", "Which change would make a root hair cell absorb water MORE slowly?", [O("A shorter extension (smaller surface area)", True, "Correct."), O("A longer extension", False, "That speeds absorption."), O("More root hairs", False, "That speeds absorption."), O("Wetter soil", False, "More water available.")], "H", "O8", "Reasoning"),
 mcq("s33p10", "Palisade cells are tall and column-shaped. How does this help?", [O("Many can pack closely side by side to absorb lots of light", True, "Correct."), O("It helps them swim", False, "No."), O("It makes them carry oxygen", False, "No."), O("It traps dust", False, "No.")], "H", "O8"),
 order("s33p11", "Put the steps of the lung's cleaning system in order.", ["Air with dust is breathed in", "Sticky mucus traps the dust", "Cilia beat together", "Mucus moves away from the lungs"], "M", "O8"),
 mcq("s33p12", "What is haemoglobin?", [O("A red pigment that carries oxygen", True, "Correct."), O("A green pigment for photosynthesis", False, "Chlorophyll."), O("A sticky substance", False, "Mucus."), O("A type of cell", False, "It's a substance in red blood cells.")], "M", "O8"),
 mcq("s33p13", "Which cell would be MOST affected by a chemical that stops cilia beating?", [O("Ciliated cell in the air passages", True, "Correct."), O("Root hair cell", False, "No cilia."), O("Red blood cell", False, "No cilia."), O("Palisade cell", False, "No cilia.")], "M", "O8"),
 grid("s33p14", "Plant or animal specialised cell?", ["Plant", "Animal"], [("Root hair cell", ["Plant"]), ("Neurone", ["Animal"]), ("Palisade cell", ["Plant"]), ("Red blood cell", ["Animal"]), ("Ciliated cell", ["Animal"])], "M", "O8"),
 mcq("s33p15", "A new cell is found with a huge folded membrane and many tiny finger-like projections. What is its most likely job?", [O("Absorbing substances quickly", True, "Correct – large surface area = fast absorption."), O("Carrying impulses", False, "That needs long fibres."), O("Supporting a tree", False, "That needs walls."), O("Making food from light", False, "That needs chloroplasts.")], "VH", "O8", "Reasoning"),
 mcq("s33p16", "Why does division of labour make an organism efficient?", [O("Each cell type is specialised and does its own job very well", True, "Correct."), O("All cells do every job at once", False, "That's the opposite."), O("Cells stop working", False, "No."), O("It reduces the number of cells", False, "No.")], "H", "O8"),
 mcq("s33p17", "Where are the branched endings of a neurone and what do they do?", [O("At the ends of the cell; they receive messages from other cells", True, "Correct."), O("Inside the nucleus; they store DNA", False, "No."), O("On the surface; they trap dust", False, "That's cilia + mucus."), O("In the blood; they carry oxygen", False, "No.")], "M", "O8"),
 explain("s33p18", "Describe how the structure of a palisade cell is related to its function.", [
   ("Many chloroplasts to absorb light energy.", [r"chloroplast"]), ("Tall / column-shaped, packed closely.", [r"tall", r"column", r"pack|close"]), ("Near the upper surface where most light falls → photosynthesis.", [r"upper|top", r"light", r"photosynth"])],
   "Palisade cells have many chloroplasts to absorb light energy for photosynthesis. They are tall, column-shaped and packed closely near the upper surface of the leaf, where most light falls.", "H", "O8", need=2),
]

S33_ADV = [
 mcq("s33a1", "* Advanced. An open anatomy textbook explains that red blood cells LOSE their nucleus as they mature. A student argues this breaks cell theory ('cells come from pre-existing cells'). Which reply is best?", [
   O("No – mature red blood cells cannot divide, but they still came from pre-existing cells in the bone marrow", True, "Correct – they were made by dividing cells; they just can't divide themselves."),
   O("Yes – cell theory is wrong", False, "One special case doesn't break the rule here."),
   O("Red blood cells are not cells", False, "They are cells (specialised)."),
   O("Red blood cells make new red blood cells", False, "They cannot divide without a nucleus."),
 ], "VH", "O8", "Evidence", src="SRC6"),
 table("s33a2", "* Advanced. Surface area: a cube cell 2 µm × 2 µm × 2 µm is flattened into a thin slab 4 µm × 4 µm × 0.5 µm (same volume). Fill in the surface areas (µm²). Surface area = 2(lw + lh + wh).",
   ["Shape", "Volume (µm³)", "Surface area (µm²)"], [["Cube 2×2×2", "8", B(24)], ["Slab 4×4×0.5", "8", B(40)]], "VH", "O8", "Data", src="SRC6",
   hint="Cube: 6 faces × (2×2). Slab: 2(16 + 2 + 2).", reason="Cube = 6 × 4 = 24 µm². Slab = 2(4×4 + 4×0.5 + 4×0.5) = 2(16 + 2 + 2) = 40 µm². Same volume, much more surface – like a red blood cell disc."),
 mcq("s33a3", "* Advanced. A sickle-shaped red blood cell carries less oxygen and gets stuck in tiny blood vessels. Which conclusion best uses structure–function thinking?", [
   O("A change in shape changes how well the cell does its job", True, "Correct – structure is linked to function."),
   O("Shape never matters for cells", False, "This evidence shows it does."),
   O("Sickle cells have more haemoglobin, so they carry more oxygen", False, "The evidence says they carry less."),
   O("Sickle cells are plant cells", False, "They are animal cells."),
 ], "VH", "O8", "Evidence"),
 explain("s33a4", "* Advanced. Design an experiment to test whether root hair length affects water absorption. State the variable you change, the variable you measure and TWO variables you keep the same.", [
   ("Change: root hair length / number of root hairs.", [r"change.*(length|root hair)", r"independent", r"length"]),
   ("Measure: volume of water absorbed (in a fixed time).", [r"measure.*water|volume|absorb"]),
   ("Control variables: same plant type/age, temperature, light, time, amount of water.", [r"same|control|constant|fixed", r"temperature|light|time|type|species|age|amount"]),
 ], "Change the average root hair length (use seedlings of the same type with different root hair lengths). Measure the volume of water absorbed in 10 minutes. Keep the same: plant type and age, temperature, light, time and volume of water at the start.",
   "VH", "O8", need=2, skill="Enquiry"),
]
