# -*- coding: utf-8 -*-
from c_base import *

# Video stops. t = seconds inside the section clip. review = [from, to] inside the clip.
STOPS = {
"3.1": [
 {"id": "v31a", "t": 85.2, "review": [52.2, 85.2], "note": "Paused while the screen shows multicellular vs unicellular organisms.",
  "q": mcq("v31a_q", "Look at the screen. A student says: 'An Amoeba is only one cell, so it is part of an organism, not a whole organism.' Which reply is correct?", [
     O("He is right – one cell cannot carry out all life processes.", False, "A unicellular organism does carry out all life processes (moving, feeding, growing…) inside its single cell."),
     O("An Amoeba is a complete unicellular organism – its single cell carries out every life process.", True, "Correct. Unicellular = one cell = the whole organism."),
     O("An Amoeba is multicellular because it is big enough to see.", False, "Amoeba needs a microscope to be seen – it is a microorganism with one cell."),
     O("An Amoeba is not living because it has no organs.", False, "Living things do not need organs. Bacteria, yeast and Amoeba are living but have no organs."),
  ], "M", "O2", hint="Re-read the definition of 'unicellular organism' on screen: an organism made of only ONE cell.",
  reason="Step 1: Count the cells: Amoeba = 1 cell. Step 2: Ask 'Is it alive and does it do all life processes?' Yes. Step 3: So that one cell IS the whole organism."),
  "twin": mcq("v31a_t", "Yeast is made of one cell. Which word describes yeast?", [
     O("multicellular organism", False, "Multi- means many cells."), O("unicellular organism", True, "Uni- means one: yeast is a one-celled organism."),
     O("tissue", False, "A tissue is a group of similar cells inside a multicellular organism."), O("organ", False, "An organ is made of several tissues.")], "M", "O2")},
 {"id": "v31b", "t": 171.2, "review": [85.3, 171.3], "note": "Paused on the cell theory summary, before the microscope scene.",
  "q": multi("v31b_q", "Select ALL the statements that are part of cell theory (including Virchow's addition).", [
     O("All living things are made up of one or more cells.", True, ""),
     O("Cells are the basic units of life.", True, ""),
     O("All cells come from pre-existing cells.", True, ""),
     O("All cells contain a cell wall.", False, "Animal cells have no cell wall – this cannot be part of cell theory."),
     O("All cells are living.", False, "Hooke's cork cells were dead – cell theory does not say every cell is alive."),
  ], "H", "O3", hint="There are exactly 3: two from Schleiden & Schwann (1839) and one that Virchow added about 15 years later.",
  reason="Schleiden + Schwann → (1) all living things are made of cells, (2) cells are the basic units of life. Virchow → (3) cells come from pre-existing cells."),
  "twin": mcq("v31b_t", "Which scientist added the idea 'all cells come from pre-existing cells'?", [
     O("Robert Hooke", False, "Hooke named cells after looking at cork."), O("Rudolf Virchow", True, "Yes – about 15 years after 1839."),
     O("Theodor Schwann", False, "Schwann studied animal cells and helped write the first two statements."), O("Antonie van Leeuwenhoek", False, "He made powerful lenses and saw unicellular organisms.")], "M", "O3")},
 {"id": "v31c", "t": 223.6, "review": [171.3, 223.7], "note": "Paused on the labelled light microscope diagram – students read the labels.",
  "q": mcq("v31c_q", "Look at the microscope on screen. A student sees a very DARK, blurry image at ×100. Which part should she adjust FIRST to let more light reach the specimen?", [
     O("Eyepiece", False, "The eyepiece only magnifies; it does not control light."),
     O("Diaphragm", True, "The diaphragm controls the amount of light reaching the specimen."),
     O("Stage clips", False, "Stage clips hold the slide – they do not change brightness."),
     O("Coarse adjustment wheel", False, "This changes focus (sharpness), not the amount of light. Use the fine wheel at high power."),
  ], "H", "O4", hint="Find the part on the diagram labelled 'controls the amount of light'.",
  reason="Dark image = too little light. Which label says 'controls the amount of light that reaches the specimen'? → diaphragm. (Also check the light source is on.)"),
  "twin": mcq("v31c_t", "Which part of the microscope do you look through?", [
     O("Objective lens", False, "The objective lens is close to the specimen."), O("Eyepiece", True, "Yes – the eyepiece lens is at the top."),
     O("Diaphragm", False, "The diaphragm controls light."), O("Stage", False, "The slide sits on the stage.")], "M", "O4")},
 {"id": "v31d", "t": 320.6, "review": [279.0, 320.8], "note": "Paused on 'Try it!' – the answer is shown only after the student predicts.",
  "q": num("v31d_q", "Predict before the video shows it: van Leeuwenhoek's lens magnified ×200. How long would a 0.1 mm object appear?", 20, "mm", "H", "O4",
     units=["mm", "cm", "µm"], errs=[{"v": 200.1, "fb": "You added 0.1 + 200. Magnification means MULTIPLY: image size = real size × magnification."},
                                    {"v": 0.0005, "fb": "You divided. The image is BIGGER than the object, so multiply: 0.1 × 200."},
                                    {"v": 2, "fb": "Check the decimal: 0.1 × 200 = 20, not 2."}],
     unitFb="Units: the real object is measured in mm and magnification has no unit, so the answer is still in mm.",
     hint="Image size = real size × magnification.", reason="image size = real size × magnification = 0.1 mm × 200 = 20 mm."),
  "twin": num("v31d_t", "A lens magnifies ×50. A 0.2 mm hair is viewed. How long does the image appear?", 10, "mm", "M", "O4",
     units=["mm", "cm", "µm"], errs=[{"v": 50.2, "fb": "Multiply, don't add: 0.2 × 50."}], unitFb="Give the answer in mm.")},
],
"3.2": [
 {"id": "v32a", "t": 67.1, "review": [0.0, 67.2], "note": "Paused on the fully labelled plant cell diagram.",
  "q": mcq("v32a_q", "Use the plant cell on screen. Which part is made of cellulose and gives the cell its regular shape?", [
     O("Cell membrane", False, "The membrane is thin and controls what goes in and out – it is not made of cellulose."),
     O("Cell wall", True, "The strong, stiff cellulose wall supports the cell."),
     O("Sap vacuole", False, "The vacuole keeps the cell firm by taking in water, but it is not made of cellulose."),
     O("Cytoplasm", False, "Cytoplasm is jelly-like – it cannot give a fixed shape."),
  ], "M", "O5", hint="Find the label that mentions 'cellulose'.", reason="Cellulose → cell wall. Wall = strong + stiff → support + regular shape."),
  "twin": mcq("v32a_t", "Which part controls what goes into and out of a cell?", [
     O("Cell wall", False, "The wall lets most substances through; it supports the cell."), O("Cell membrane", True, "Yes – only certain substances can pass."),
     O("Nucleus", False, "The nucleus controls cell activities, not entry of substances."), O("Chloroplast", False, "Chloroplasts trap light energy.")], "M", "O5")},
 {"id": "v32b", "t": 104.9, "review": [67.2, 105.0], "note": "Paused on the cheek cell diagram.",
  "q": multi("v32b_q", "A cheek cell is an animal cell. Select ALL the parts a cheek cell does NOT have.", [
     O("Cell wall", True, ""), O("Chloroplasts", True, ""), O("Large sap vacuole", True, ""),
     O("Mitochondria", False, "Animal cells DO have mitochondria – they need energy from aerobic respiration."),
     O("Cell membrane", False, "Every cell has a cell membrane."),
  ], "M", "O6", hint="Three parts are found only in plant cells.", reason="Plant-only parts: cell wall, chloroplasts, large sap vacuole. Both types: nucleus, cytoplasm, membrane, mitochondria."),
  "twin": mcq("v32b_t", "Which part is found in BOTH plant and animal cells?", [
     O("Chloroplast", False, "Plant only."), O("Cell wall", False, "Plant only."), O("Mitochondrion", True, "Yes – both release energy by aerobic respiration."), O("Large sap vacuole", False, "Plant only.")], "M", "O6")},
 {"id": "v32c", "t": 148.3, "review": [104.6, 148.6], "note": "Paused right after the 'Think about it' question, before Unit 3.3.",
  "q": explain("v32c_q", "Answer the video's question: Why do plant cells need cell walls but animal cells do not? (Hint: think of tall trees.)", [
     ("Cell walls are strong/stiff and SUPPORT the plant (keep shape).", [r"support", r"strong", r"stiff", r"rigid", r"shape"]),
     ("Plants (e.g. tall trees) have no skeleton, so they need walls to stand upright.", [r"skeleton", r"bone", r"upright", r"stand", r"tall", r"tree"]),
     ("Animals are supported by a skeleton / need to move and change shape.", [r"skeleton", r"bone", r"move", r"flexib"]),
  ], "Plant cells need a strong, stiff cell wall to support the plant and keep its shape – a tall tree has no skeleton, so its cells must hold it upright. Animals are supported by a skeleton and need flexible cells so they can move.",
  "H", "O6", need=2, hint="Think: what keeps a plant upright? What keeps your body upright?",
  reason="1) What does a wall do? → supports, keeps shape. 2) What holds up a tree? → only its cells (no bones). 3) What holds up an animal? → a skeleton; animals also move, so cells must bend."),
  "twin": mcq("v32c_t", "A celery stalk goes floppy when it loses water. Which TWO parts normally keep plant cells firm?", [
     O("Sap vacuole and cell wall", True, "The full vacuole presses against the stiff wall, keeping the cell firm."),
     O("Nucleus and mitochondria", False, "These control activities and release energy – not firmness."),
     O("Chloroplasts and cytoplasm", False, "These do not make the cell firm."),
     O("Cell membrane and nucleus", False, "The membrane alone is too thin to give support.")], "H", "O5")},
],
"3.3": [
 {"id": "v33a", "t": 17.0, "review": [0.0, 17.1], "note": "Paused when the root hair cell first appears – before the narrator explains the extension.",
  "q": mcq("v33a_q", "PREDICT: The root hair cell on screen has a long extension pushed into the soil. What is the main advantage of this shape?", [
     O("It increases the surface area so water and mineral salts are absorbed quickly.", True, "Correct – more surface in contact with soil water."),
     O("It lets the cell photosynthesise underground.", False, "Root hair cells are in the dark soil and have no chloroplasts."),
     O("It anchors the whole plant like a hook.", False, "Anchoring is done by the root system as a whole, not by the hair's surface."),
     O("It stores food for the plant.", False, "Storage is not linked to having a thin extension."),
  ], "H", "O8", hint="A long, thin shape: how does that change the surface area touching the soil?",
  reason="Long, thin extension → much more membrane touching soil water → more surface area → faster absorption of water and mineral salts."),
  "twin": mcq("v33a_t", "Which cell has a long extension to absorb water?", [
     O("Palisade cell", False, "Palisade cells are in leaves and absorb light."), O("Root hair cell", True, "Yes."),
     O("Red blood cell", False, "Red blood cells carry oxygen."), O("Ciliated cell", False, "Ciliated cells move mucus.")], "M", "O8")},
 {"id": "v33b", "t": 53.9, "review": [43.5, 54.0], "note": "Paused on the ciliated cell diagram.",
  "q": mcq("v33b_q", "Smoking damages cilia so they stop beating. Using the ciliated cell on screen, predict what happens.", [
     O("Mucus and trapped dust build up and move towards the lungs.", True, "Correct – without beating cilia, the mucus is not swept away from the lungs."),
     O("The cells make more oxygen.", False, "Ciliated cells do not make oxygen."),
     O("Dust is absorbed by the cilia and destroyed.", False, "Cilia do not absorb dust; they move the mucus that traps it."),
     O("Nothing changes because mucus traps the dust anyway.", False, "Mucus traps dust, but cilia are needed to MOVE it away."),
  ], "VH", "O8", hint="Mucus traps dust. What job do the cilia do with the mucus?",
  reason="Mucus TRAPS dust. Cilia MOVE the mucus away. No movement → dirty mucus stays → can reach the lungs."),
  "twin": mcq("v33b_t", "What is the job of cilia on ciliated cells?", [
     O("Trap dust", False, "Mucus traps dust."), O("Beat to move mucus away from the lungs", True, "Yes."),
     O("Carry oxygen", False, "Red blood cells carry oxygen."), O("Send impulses", False, "Neurones do that.")], "M", "O8")},
 {"id": "v33c", "t": 66.2, "review": [54.0, 66.3], "note": "Paused on the red blood cell diagram.",
  "q": mcq("v33c_q", "A red blood cell has NO nucleus. How does this help it do its job?", [
     O("There is more space for haemoglobin, so it can carry more oxygen.", True, "Correct."),
     O("It makes the cell heavier so it sinks to the tissues.", False, "Weight is not the reason."),
     O("It lets the cell divide faster.", False, "Without a nucleus a red blood cell cannot divide at all."),
     O("It gives the cell a larger surface area.", False, "The large surface area comes from the dimpled disc SHAPE, not from losing the nucleus."),
  ], "H", "O8", hint="With no nucleus, what can the space inside be used for?",
  reason="Two different adaptations: no nucleus → more room for haemoglobin; dimpled disc shape → large surface area."),
  "twin": mcq("v33c_t", "Which pigment in red blood cells carries oxygen?", [
     O("Chlorophyll", False, "Chlorophyll is in chloroplasts of plant cells."), O("Haemoglobin", True, "Yes."), O("Cellulose", False, "Cellulose makes cell walls."), O("Mucus", False, "Mucus is made by cells in air passages.")], "M", "O8")},
],
"3.4": [
 {"id": "v34a", "t": 29.8, "review": [0.0, 29.9], "note": "Paused on the tissues screen.",
  "q": mcq("v34a_q", "Which of these is a TISSUE (not a cell, organ or organ system)?", [
     O("Xylem", True, "Xylem is a group of similar cells that carry water – a tissue."),
     O("Leaf", False, "A leaf contains several different tissues – it is an organ."),
     O("Neurone", False, "A neurone is one cell. Many neurones together form nerve tissue."),
     O("Circulatory system", False, "That is an organ system (heart + blood vessels)."),
  ], "H", "O9", hint="Tissue = a group of SIMILAR cells working together to carry out one function.",
  reason="Ask: one cell? (neurone) → cell. Many similar cells? (xylem) → tissue. Several tissues? (leaf) → organ. Several organs? → system."),
  "twin": mcq("v34a_t", "A tissue is…", [
     O("a group of similar cells that perform a function", True, "Yes."), O("a group of different organs", False, "That is an organ system."),
     O("a single specialised cell", False, "One cell is a cell."), O("any part of a plant", False, "Too vague – a flower is an organ.")], "M", "O9")},
 {"id": "v34b", "t": 62.0, "review": [29.9, 62.1], "note": "Paused on the plant and human organs diagram.",
  "q": mcq("v34b_q", "Look at the plant on screen. Which organ both SUPPORTS the plant and MOVES water upwards?", [
     O("Root", False, "Roots absorb water and anchor the plant; they do not hold the leaves up."),
     O("Stem", True, "Correct – the stem supports leaves and flowers and transports water up."),
     O("Leaf", False, "Leaves make food by photosynthesis."),
     O("Flower", False, "Flowers are for reproduction."),
  ], "M", "O9", hint="Read the label on each plant organ in the picture.", reason="Support + transport upward = stem."),
  "twin": mcq("v34b_t", "Which human organ pumps blood around the body?", [
     O("Lungs", False, "Lungs take in oxygen."), O("Heart", True, "Yes."), O("Stomach", False, "The stomach digests food."), O("Brain", False, "The brain controls body functions.")], "M", "O9")},
 {"id": "v34c", "t": 95.4, "review": [62.1, 95.5], "note": "Paused on the six human organ systems.",
  "q": mcq("v34c_q", "A person's kidneys stop working. Which organ system is affected FIRST, and what builds up in the body?", [
     O("Excretory system – waste products, excess water and salts", True, "Correct – the excretory system removes waste."),
     O("Digestive system – undigested food", False, "Kidneys are not part of the digestive system."),
     O("Respiratory system – oxygen", False, "The respiratory system includes lungs and air tubes."),
     O("Skeletal system – bones", False, "Kidneys are not part of the skeleton."),
  ], "H", "O9", hint="Kidneys + bladder: which system on screen do they belong to?", reason="Kidneys + bladder = excretory system → removes waste, excess water and salts."),
  "twin": mcq("v34c_t", "Which organ system contains the lungs and air tubes?", [
     O("Circulatory", False, "Heart and blood vessels."), O("Respiratory", True, "Yes."), O("Digestive", False, "Stomach and intestines."), O("Muscular", False, "Muscles attached to bones.")], "M", "O9")},
 {"id": "v34d", "t": 98.8, "review": [95.5, 140.5], "note": "Paused at 'Let's put it all together' – before the levels are revealed.",
  "q": order("v34d_q", "PREDICT the order before the video shows it. Arrange from smallest to largest level of organisation.",
     ["muscle cell", "muscle tissue", "heart (organ)", "circulatory system", "human being (organism)"], "M", "O9",
     hint="Start from the smallest unit of life.", reason="cell → tissue (similar cells) → organ (several tissues) → organ system (several organs) → organism."),
  "twin": order("v34d_t", "Put these in order from smallest to largest.", ["cell", "tissue", "organ", "organ system", "organism"], "M", "O9")},
],
}
