# -*- coding: utf-8 -*-
from c_base import *

S34_REQ = [
 order("s34r1", "Arrange the levels of organisation in the human body from smallest to largest.",
   ["muscle cell", "muscle tissue", "heart", "circulatory system", "human being"], "M", "O9",
   hint="Start with one cell. Finish with the whole body.", reason="cell → tissue → organ → organ system → organism.",
   twin=order("s34r1t", "Order: organ, cell, tissue.", ["cell", "tissue", "organ"], "M", "O9")),
 label("s34r2", "Label the organs of the flowering plant.", "plant", {"flower": "Flower", "leaf": "Leaf", "stem": "Stem", "root": "Root"}, "M", "O9",
   confuse={"Stem|Root": "The stem is ABOVE the soil and holds the leaves; roots are BELOW the soil."},
   twin=label("s34r2t", "Label the leaf and the root.", "plant", {"leaf": "Leaf", "root": "Root"}, "M", "O9")),
 label("s34r3", "Label the human organs.", "body", {"brain": "Brain", "lungs": "Lungs", "heart": "Heart", "stomach": "Stomach"}, "M", "O9",
   confuse={"Lungs|Heart": "There are two lungs on either side; the heart sits between them, slightly to the left.",
            "Stomach|Heart": "The stomach is lower, in the abdomen; the heart is in the chest."},
   twin=label("s34r3t", "Label the brain and the heart.", "body", {"brain": "Brain", "heart": "Heart"}, "M", "O9")),
 match("s34r4", "Match each organ system to its main function.", [
   ("Skeletal system", "supports the body, protects organs, allows movement"),
   ("Respiratory system", "takes in oxygen, removes carbon dioxide"),
   ("Muscular system", "moves bones (walking, moving fingers)"),
   ("Circulatory system", "transports nutrients and oxygen in blood"),
   ("Digestive system", "breaks down food and absorbs nutrients"),
   ("Excretory system", "removes waste, excess water and salts")], "H", "O9",
   twin=match("s34r4t", "Match two systems.", [("Digestive system", "breaks down food"), ("Respiratory system", "takes in oxygen")], "M", "O9")),
 mcq("s34r5", "Xylem is made of many similar cells that carry water. Is xylem a cell, tissue, organ or organ system?", [
   O("Tissue", True, "Similar cells working together = tissue."),
   O("Organ", False, "An organ (like a leaf or stem) contains several DIFFERENT tissues."),
   O("Cell", False, "Xylem contains many cells."),
   O("Organ system", False, "A system contains several organs."),
 ], "H", "O9", hint="Many similar cells → ?", twin=mcq("s34r5t", "The heart is…", [O("an organ", True, "Made of muscle, nerve and other tissues."), O("a tissue", False, "It has several tissues."), O("a cell", False, "No."), O("an organism", False, "No.")], "M", "O9")),
 grid("s34r6", "Classify each example at the correct level of organisation.", ["Cell", "Tissue", "Organ", "Organ system"], [
   ("Neurone", ["Cell"]), ("Phloem", ["Tissue"]), ("Stomach", ["Organ"]), ("Lungs + air tubes", ["Organ system"]),
   ("Epithelial tissue", ["Tissue"]), ("Leaf", ["Organ"]), ("Root hair cell", ["Cell"])], "H", "O9", "Data",
   twin=grid("s34r6t", "Classify.", ["Cell", "Tissue", "Organ"], [("Red blood cell", ["Cell"]), ("Brain", ["Organ"])], "M", "O9")),
 explain("s34r7", "A student says: 'A leaf is a tissue because it is green.' Explain why a leaf is an ORGAN.", [
   ("An organ is made of different tissues working together.", [r"different tissues", r"several tissues", r"many tissues", r"more than one tissue", r"tissues"]),
   ("Name tissues in a leaf (e.g. epidermal, xylem, phloem, palisade/photosynthetic).", [r"epiderm", r"xylem", r"phloem", r"palisade"]),
   ("They work together for a function (photosynthesis).", [r"together", r"photosynth", r"function|make food"]),
 ], "A leaf is an organ because it is made of several different tissues – for example epidermal tissue, palisade (photosynthetic) tissue, xylem and phloem – which work together to carry out photosynthesis. Colour does not decide the level.",
   "H", "O9", need=2, hint="What is the definition of an organ? Which tissues are found in a leaf?",
   twin=mcq("s34r7t", "Which is made of different tissues working together?", [O("An organ", True, "Yes."), O("A tissue", False, "A tissue = similar cells."), O("A cell", False, "No."), O("A molecule", False, "No.")], "M", "O9")),
 mcq("s34r8", "Jellyfish and sponges do NOT have a circulatory system. Which organs are they missing?", [
   O("A heart and blood vessels", True, "Correct – these make up the circulatory system."),
   O("Lungs and air tubes", False, "That's the respiratory system."),
   O("Kidneys and bladder", False, "Excretory system."),
   O("Stomach and intestines", False, "Digestive system."),
 ], "VH", "O9", "Reasoning", twin=mcq("s34r8t", "Which organs form the circulatory system?", [O("Heart and blood vessels", True, "Yes."), O("Brain and nerves", False, "No."), O("Bones", False, "No."), O("Stomach", False, "No.")], "M", "O9")),
]

S34_PRAC = [
 match("s34p01", "Match each plant organ with its function.", [("Root", "absorbs water and mineral salts; anchors the plant"), ("Stem", "supports the plant; moves water up and food around"), ("Leaf", "photosynthesis"), ("Flower", "reproduction")], "M", "O9"),
 match("s34p02", "Match each plant tissue with its function.", [("Epidermal tissue", "outer layer; protects from water loss and injury"), ("Xylem", "moves water and mineral salts from roots"), ("Phloem", "carries food made in leaves to other parts")], "H", "O9"),
 match("s34p03", "Match each animal tissue with its function.", [("Muscle tissue", "contracts to cause movement"), ("Nerve tissue", "carries electrical impulses"), ("Fat (adipose) tissue", "stores food for energy"), ("Epithelial tissue", "covers and protects cells beneath"), ("Bone tissue", "keeps bones firm and strong")], "H", "O9"),
 mcq("s34p04", "How many organ systems does the human body have?", [O("11", True, "Correct."), O("6", False, "The book shows six of the 11."), O("4", False, "No."), O("206", False, "That's the number of bones in an adult.")], "M", "O9"),
 mcq("s34p05", "Which TWO organ systems work together to deliver oxygen to muscle cells?", [O("Respiratory and circulatory", True, "Lungs take in oxygen; blood carries it."), O("Digestive and skeletal", False, "No."), O("Excretory and muscular", False, "No."), O("Skeletal and respiratory", False, "Blood is needed to carry oxygen.")], "H", "O9", "Reasoning"),
 mcq("s34p06", "Which of these is an ORGAN SYSTEM in plants?", [O("Water transport system (roots, stem, leaves)", True, "Correct."), O("Xylem", False, "A tissue."), O("A root hair cell", False, "A cell."), O("A leaf", False, "An organ.")], "H", "O9"),
 mcq("s34p07", "What feature of plant cells would NOT be found in root cells? Why?", [O("Chloroplasts – roots grow in the dark and do not photosynthesise", True, "Correct."), O("Cell walls – roots are soft", False, "Root cells have walls."), O("Nuclei – roots are dead", False, "No."), O("Vacuoles – roots don't need water", False, "Roots absorb water.")], "H", "O9", "Reasoning"),
 order("s34p08", "Order a plant example from smallest to largest.", ["palisade cell", "palisade tissue", "leaf", "water transport system", "sunflower plant"], "H", "O9"),
 mcq("s34p09", "Which organ controls all body functions, including what we think and feel?", [O("Brain", True, "Correct."), O("Heart", False, "Pumps blood."), O("Stomach", False, "Digests food."), O("Lungs", False, "Gas exchange.")], "M", "O9"),
 mcq("s34p10", "The skeletal system protects vital organs. Which organs does the skull protect?", [O("Brain (and eyes)", True, "Correct."), O("Heart and lungs", False, "The rib cage protects these."), O("Stomach", False, "No."), O("Kidneys", False, "No.")], "M", "O9"),
 grid("s34p11", "Which system does each organ belong to?", ["Digestive", "Circulatory", "Excretory", "Respiratory"], [("Stomach", ["Digestive"]), ("Kidney", ["Excretory"]), ("Heart", ["Circulatory"]), ("Lungs", ["Respiratory"]), ("Bladder", ["Excretory"]), ("Intestines", ["Digestive"])], "M", "O9"),
 mcq("s34p12", "Why must organ systems work together?", [O("So the whole organism functions efficiently", True, "Correct."), O("So cells can stop working", False, "No."), O("Because each system can do every job", False, "Each has its own job."), O("They do not need to", False, "They depend on each other.")], "M", "O9"),
 mcq("s34p13", "A muscle cell, muscle tissue and the heart are all involved in pumping blood. Which statement is correct?", [O("The heart is an organ made of muscle tissue and other tissues", True, "Correct."), O("The heart is a single giant muscle cell", False, "No."), O("Muscle tissue is an organ", False, "It's a tissue."), O("The heart is an organ system", False, "It's part of the circulatory system.")], "H", "O9"),
 multi("s34p14", "Select ALL the organs.", [O("Eye", True, ""), O("Stomach", True, ""), O("Leaf", True, ""), O("Xylem", False, "Tissue."), O("Neurone", False, "Cell.")], "H", "O9"),
 mcq("s34p15", "In a tall tree, water reaches the top leaves. Which tissue makes this possible?", [O("Xylem", True, "Correct."), O("Phloem", False, "Phloem carries food."), O("Epidermal", False, "Protection."), O("Palisade", False, "Photosynthesis.")], "M", "O9"),
 mcq("s34p16", "Sunflower seeds are made in the ovary of the flower. Which level is the ovary?", [O("Organ", True, "Correct – the book uses ovaries as an example of an organ."), O("Cell", False, "It has many cells."), O("Organism", False, "No."), O("Organ system", False, "It's part of the reproductive system.")], "H", "O9"),
 mcq("s34p17", "Which organ system breaks down food and absorbs nutrients into the blood?", [O("Digestive", True, "Correct."), O("Excretory", False, "Removes waste."), O("Muscular", False, "Movement."), O("Respiratory", False, "Gases.")], "M", "O9"),
 explain("s34p18", "Give an example of how TWO organ systems work together when you run.", [
   ("Name two systems (e.g. muscular + skeletal, respiratory + circulatory).", [r"muscular|skeletal|respiratory|circulatory"]),
   ("Describe what each does in the example.", [r"move|pull|contract|bones?|oxygen|blood|pump"]),
   ("Explain the link (one system helps the other).", [r"together|so that|because|helps?|supply|deliver"]),
 ], "When you run, the muscular system contracts muscles that pull on the bones of the skeletal system, so the legs move. The respiratory system takes in more oxygen and the circulatory system carries it to the muscle cells for energy.",
   "H", "O9", need=2),
]

S34_ADV = [
 mcq("s34a1", "* Advanced. Unfamiliar situation: A tapeworm lives inside the human gut and absorbs digested food through its body surface. Which organ system would you expect it to be MISSING?", [
   O("A digestive system", True, "Correct – its food is already digested by the host."),
   O("A nervous system", False, "Not supported by the evidence given."),
   O("A reproductive system", False, "Tapeworms reproduce."),
   O("It must have all systems", False, "Parasites often lose systems they don't need."),
 ], "VH", "O9", "Reasoning", src="SRC7"),
 mcq("s34a2", "* Advanced. Evidence: Taro corms (underground stems) have yellow cells packed with starch. Plants make glucose in photosynthesis. Why is the glucose NOT made in the corm cells themselves?", [
   O("The corm is underground with no light, so its cells cannot photosynthesise; glucose is made in leaves and carried by phloem", True, "Correct – links tissues and organs."),
   O("Starch cells are dead", False, "No evidence of that."),
   O("Corms make glucose from soil", False, "Plants make glucose by photosynthesis."),
   O("Xylem carries starch down", False, "Phloem carries food; xylem carries water."),
 ], "VH", "O9", "Reasoning"),
 explain("s34a3", "* Advanced. A model shows the body as a city: cells = bricks, tissues = walls, organs = buildings, organ systems = neighbourhoods. Give one strength and one limitation of this model.", [
   ("Strength: shows small parts combining into bigger levels / hierarchy.", [r"small|bigger|level|build|combine|hierarch|order"]),
   ("Limitation: bricks are not alive / identical; cells are living, specialised and work together.", [r"alive|living|not identical|same|specialis|different jobs|work together"]),
 ], "Strength: it shows clearly how small units combine into bigger levels. Limitation: bricks are identical and not alive, but cells are living, specialised for different jobs and depend on each other.",
   "VH", "O9", need=2, skill="Evaluation"),
 mcq("s34a4", "* Advanced. Design flaw: To find which organ system is most important, a student lists systems by SIZE and says 'the biggest is the most important'. What is wrong?", [
   O("Size does not measure importance – all systems depend on each other, so the question needs a different test", True, "Correct."),
   O("He should list them by colour", False, "Colour is no better."),
   O("He forgot the skeletal system is the biggest", False, "Misses the point."),
   O("Nothing is wrong", False, "Size ≠ importance."),
 ], "VH", "O9", "Enquiry"),
]
