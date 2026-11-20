# -*- coding: utf-8 -*-
"""Stage 8 Unit 2 – Human Body Systems. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Biology"
BLURB = "Bones, joints and antagonistic muscles; how we breathe and exchange gases; aerobic respiration; and the heart, blood vessels and blood."
OBJECTIVES = {
    "O1": {"sec": "2.1", "code": "8Bs.01, 8TWSm.01", "codeNote": "", "t": "Describe the jobs of the skeleton, identify ball-and-socket and hinge joints and explain how antagonistic muscles move a joint."},
    "O2": {"sec": "2.2", "code": "8Bs.03", "codeNote": "", "t": "Describe the structure of the respiratory system and how breathing in and out works."},
    "O3": {"sec": "2.2", "code": "8Bs.04, 8Bp.04, 8Bp.05", "codeNote": "", "t": "Explain gas exchange in the alveoli by diffusion, tell breathing from respiration and use the word equation for aerobic respiration."},
    "O4": {"sec": "2.3", "code": "8Bs.02", "codeNote": "", "t": "Describe the heart, blood vessels and the parts of blood and their jobs."},
}
SECTIONS = [
    {"id": "2.1", "title": "The musculoskeletal system", "objs": ["O1"]},
    {"id": "2.2", "title": "The respiratory system", "objs": ["O2", "O3"]},
    {"id": "2.3", "title": "The circulatory system", "objs": ["O4"]},
]
u = Unit(8, 2)

# ---------------------------------------------------------------- 2.1
u.sec("2.1", "O1")
u.gd("r", "Which type of joint is each?", "Joint", [("Shoulder", "Ball and socket"), ("Elbow", "Hinge"), ("Knee", "Hinge"), ("Skull", "Fixed")])
u.mc("r", "Why do skeletal muscles work in pairs?", "Muscles can only pull, not push", [("Muscles can only push", "They pull."), ("One muscle is always resting", "No."), ("Bones push the muscles", "Bones are pulled.")])
u.mt("r", "Match each part of the skeleton to the organ it protects.", [("Skull", "brain"), ("Ribs", "heart and lungs"), ("Spine (backbone)", "spinal cord")])
u.gd("r", "When you bend your arm, what does each muscle do?", "Action", [("Biceps", "Contracts"), ("Triceps", "Relaxes")])
u.ex("r", "Explain how the biceps and triceps straighten your arm.", [("triceps contracts / shortens", ["triceps.*contract|triceps.*short"]), ("pulls the lower arm down", ["pull|down"]), ("biceps relaxes", ["biceps.*relax"])],
     "The triceps contracts and gets shorter, pulling the lower arm down, while the biceps relaxes.")
u.mc("r", "Muscles are attached to bones by…", "tendons", [("ligaments only", "Ligaments join bone to bone."), ("cartilage", "No."), ("nerves", "No.")])
u.mc("r", "Comparing a hinge joint to a door hinge is an example of…", "an analogy", [("a hypothesis", "No."), ("a result", "No."), ("a variable", "No.")], d="H")
u.mc("r", "A ball-and-socket joint allows more movement than a hinge joint because…", "the ball can turn in many directions inside the socket", [("it has more muscles", "No."), ("its bones bend", "Bones can't bend."), ("it has no tendons", "No.")], d="VH")
for p, r, w in [
    ("The skeleton gives the body…", "support, shape, movement and protection", ["energy", "oxygen", "food"]),
    ("A joint is where…", "two or more bones meet", ["a muscle meets skin", "blood is made", "food is digested"]),
    ("Which joint allows movement in a full circle?", "Hip", ["Elbow", "Knee", "Finger"]),
    ("Which joints do not move?", "The joints of the skull", ["Shoulder joints", "Knee joints", "Elbow joints"]),
    ("When a muscle contracts it becomes…", "shorter and fatter", ["longer and thinner", "harder to see", "a bone"]),
    ("When a muscle relaxes it…", "returns to its original shape", ["pushes the bone", "becomes a tendon", "breaks"]),
    ("Muscles that work in pairs pulling opposite ways are called…", "antagonistic muscles", ["hinge muscles", "fixed muscles", "heart muscles"]),
    ("To bend your arm, which muscle contracts?", "Biceps", ["Triceps", "Both", "Neither"]),
    ("A newborn baby's bones are…", "soft and weak", ["harder than an adult's", "made of steel", "fully grown"]),
    ("Human bone is about how strong compared with steel of the same mass?", "About five times stronger", ["Much weaker", "The same", "A hundred times weaker"]),
    ("We have more than how many muscles?", "600", ["60", "6", "6000 bones"]),
    ("Your fingers have…", "hinge joints", ["ball-and-socket joints", "fixed joints", "no joints"]),
    ("The pelvis joints are…", "fixed", ["ball and socket", "hinge", "elastic"]),
    ("Thigh muscles bend and straighten the leg by working…", "in antagonistic pairs", ["alone", "only by pushing", "without bones"]),
    ("In old age bones may…", "weaken", ["turn into muscle", "grow longer", "become steel"]),
]:
    u.mc("p", p, r, w)
u.od("p", "Order the steps when you bend your arm.", ["Brain sends a signal", "Biceps contracts", "Biceps pulls the lower arm up", "Arm bends at the elbow"], d="H")
u.ms("p", "Select ALL the hinge joints.", ["Elbow", "Knee", "Finger"], ["Shoulder", "Hip"])
u.mt("p", "Match the term to its meaning.", [("Contract", "get shorter"), ("Relax", "go back to normal length"), ("Tendon", "joins muscle to bone")])
u.ex("a", "* Advanced. A door hinge is used as an analogy for the knee. Give one way the analogy works and one way it does not.", [("works: moves back and forth in one direction", ["back and forth|one direction|open and close"]), ("doesn't: knee moved by muscles / living / slight twist / not metal", ["muscle|living|twist|grow|not metal|cartilage"])],
     "It works because both move back and forth in one direction. It is not perfect: the knee is moved by muscles pulling on bones, is living tissue and can twist slightly.")
u.mc("a", "Why can't a single muscle both bend and straighten the arm?", "It can only pull when it contracts, so another muscle must pull the other way.", ["It is too short.", "Muscles push to straighten.", "Bones straighten the arm by themselves."], skill="Reasoning")
u.mc("a", "Which feature makes bone strong but light?", "It is made of living tissue with a strong structure, not solid metal.", ["It is hollow and empty.", "It is made of muscle.", "It contains steel."])
u.gd("a", "When you straighten your leg, what does each thigh muscle do?", "Action", [("Front thigh muscle", "Contracts"), ("Back thigh muscle", "Relaxes")])
u.stop("They are fixed joints", "Which joints do not move?", "Fixed joints", ["Hinge joints", "Ball-and-socket joints", "All joints"])
u.stop("called an analogy", "Which joint moves back and forth in one direction only?", "Hinge joint", ["Ball-and-socket joint", "Fixed joint", "None"])
u.stop("while the triceps relaxes", "To bend the arm, the biceps…", "contracts", ["relaxes", "pushes", "stays still"])

# ---------------------------------------------------------------- 2.2
u.sec("2.2", "O2")
u.od("r", "Put the parts in the order air passes through them.", ["Nose or mouth", "Trachea", "Bronchus", "Bronchiole", "Alveoli"])
u.gd("r", "What happens when you breathe in?", "Breathing in", [("Intercostal muscles", "Contract"), ("Diaphragm", "Moves down"), ("Volume of chest", "Increases"), ("Pressure in lungs", "Decreases")], extra=["Relax", "Moves up", "Decreases", "Increases"])
u.tb("r", "Compare air breathed in and out. Complete the table.", ["Gas", "In (%)", "Out (%)", "Out − In"], [["Oxygen", "21", "16", B(-5)], ["Carbon dioxide", "0.04", "4", B(3.96)]], o="O3")
u.ex("r", "Explain why gas exchange in the alveoli is fast.", [("walls one cell thick / thin", ["one cell|thin"]), ("diffusion from high to low concentration", ["diffus|high.*low|concentration"]), ("many capillaries / large surface area", ["capillar|surface|many"])],
     "The walls of the alveoli and capillaries are only one cell thick and there are many capillaries, so oxygen and carbon dioxide diffuse quickly from high to low concentration.", o="O3")
u.mc("r", "What is the difference between breathing and respiration?", "Breathing moves air in and out; respiration releases energy from food in cells.", [("They are the same.", "No."), ("Respiration only happens in the lungs.", "It happens in every cell."), ("Breathing releases energy.", "No.")], o="O3")
u.mc("r", "Which is the word equation for aerobic respiration?", "glucose + oxygen → carbon dioxide + water", [("carbon dioxide + water → glucose + oxygen", "That is photosynthesis."), ("glucose → oxygen + water", "No."), ("oxygen + water → glucose", "No.")], o="O3")
u.mc("r", "Where in a cell does aerobic respiration happen?", "In the mitochondria", [("In the nucleus", "No."), ("In the cell wall", "No."), ("In the vacuole", "No.")], o="O3", d="H")
u.mc("r", "When you breathe out, the pressure in the lungs…", "rises, pushing air out", [("falls, pulling air in", "That is breathing in."), ("stays the same", "No."), ("becomes zero", "No.")], d="VH")
for p, r, w, o in [
    ("The trachea divides into two…", "bronchi", ["alveoli", "capillaries", "ribs"], "O2"),
    ("Tiny air sacs in the lungs are called…", "alveoli", ["bronchi", "tendons", "platelets"], "O2"),
    ("The dome-shaped muscle below the lungs is the…", "diaphragm", ["biceps", "trachea", "heart"], "O2"),
    ("Muscles between the ribs are the…", "intercostal muscles", ["triceps", "tendons", "diaphragm"], "O2"),
    ("When you breathe out, the diaphragm…", "relaxes and domes upwards", ["contracts and moves down", "disappears", "pushes the ribs out"], "O2"),
    ("Breathing in is also called…", "inhaling", ["exhaling", "respiring", "digesting"], "O2"),
    ("Air breathed out contains about what percentage of oxygen?", "16%", ["21%", "0%", "78%"], "O2"),
    ("Why does a mirror mist up when you breathe on it?", "Breathed-out air has more water vapour", ["It has more oxygen", "The mirror is wet", "Air has no water"], "O2"),
    ("Alveoli are surrounded by tiny blood vessels called…", "capillaries", ["arteries", "bronchi", "tendons"], "O3"),
    ("Oxygen moves from the alveoli into the…", "blood", ["trachea", "stomach", "bone"], "O3"),
    ("Gases move into and out of the blood by…", "diffusion", ["pumping", "filtering", "freezing"], "O3"),
    ("Diffusion is movement from…", "high concentration to low concentration", ["low to high concentration", "up to down only", "cold to hot"], "O3"),
    ("Starch is digested into…", "glucose", ["oxygen", "protein", "water"], "O3"),
    ("Respiration happens…", "all the time, even while we sleep", ["only during exercise", "only in daytime", "only in the lungs"], "O3"),
    ("Germinating seeds give off carbon dioxide, which turns limewater…", "milky", ["blue", "red", "clear"], "O3"),
]:
    u.mc("p", p, r, w, o=o)
u.gd("p", "Breathing or respiration?", "Process", [("Moving air into the lungs", "Breathing"), ("Releasing energy from glucose", "Respiration"), ("Happens in mitochondria", "Respiration")], o="O3")
u.ms("p", "Select ALL the products of aerobic respiration.", ["Carbon dioxide", "Water", "Energy released"], ["Glucose", "Oxygen"], o="O3")
u.mt("p", "Match the part to its job.", [("Trachea", "carries air to the lungs"), ("Alveoli", "gas exchange"), ("Diaphragm", "helps change chest volume")])
u.ex("a", "* Advanced. Explain why the air pressure inside the lungs falls when you breathe in, and why this makes air rush in.", [("chest volume increases", ["volume|bigger|expand"]), ("same air spread out / lower pressure", ["lower pressure|pressure (drops|falls|decreases)"]), ("air moves from high pressure outside to low inside", ["higher pressure|high to low|outside"])],
     "The ribs move up and out and the diaphragm moves down, so the chest volume increases. The same air fills a bigger space, so the pressure falls, and air from outside at higher pressure rushes in.", o="O2")
u.nm("a", "A person breathes 6 litres of air a minute. 5% of it is oxygen that is absorbed. How many litres of oxygen is absorbed in one minute?", 0.3, "l", o="O3", tol=0.01)
u.mc("a", "Why do cells need a steady, controlled release of energy?", "Sudden release would waste energy as heat and could damage cells.", ["Cells only need energy at night.", "Energy cannot be stored.", "Respiration only happens once a day."], o="O3", skill="Reasoning")
u.mc("a", "During hard exercise breathing gets faster. Why?", "Muscles respire more, so more oxygen is needed and more carbon dioxide must be removed.", ["Muscles need less oxygen.", "Lungs get smaller.", "Blood stops flowing."], o="O3", skill="Reasoning")
u.stop("one for each lung", "The trachea divides into two…", "bronchi", ["alveoli", "capillaries", "veins"])
u.stop("Air from outside, at higher pressure, rushes in", "When you breathe in, the diaphragm…", "contracts and moves down", ["relaxes and moves up", "stays still", "pushes air out"])
u.stop("so gases pass through quickly", "Gases cross the alveolus wall by…", "diffusion", ["respiration", "digestion", "evaporation"], o="O3")
u.stop("turns limewater milky", "Aerobic respiration produces…", "carbon dioxide and water", ["glucose and oxygen", "oxygen only", "starch"], o="O3")

# ---------------------------------------------------------------- 2.3
u.sec("2.3", "O4")
u.gd("r", "Which part of the blood does each job?", "Part", [("Carries oxygen", "Red blood cells"), ("Fights pathogens", "White blood cells"), ("Helps blood clot", "Platelets"), ("Carries dissolved glucose", "Plasma")])
u.mc("r", "Arteries carry blood…", "away from the heart", [("towards the heart", "That is veins."), ("only to the lungs", "No."), ("only to the brain", "No.")])
u.tb("r", "Blood separated in a centrifuge. Complete the table.", ["Layer", "Percentage"], [["Plasma", "55"], ["Red blood cells", B(41)], ["White cells and platelets", "4"]])
u.ex("r", "Explain how the shape and structure of a red blood cell help it carry oxygen.", [("no nucleus – more room for haemoglobin", ["no nucleus|haemoglobin"]), ("biconcave disc – large surface area", ["biconcave|surface area|disc"]), ("take in / release oxygen quickly", ["quick|fast|oxygen"])],
     "It has no nucleus, so there is more room for haemoglobin, and its biconcave disc shape gives a large surface area, so it takes in and releases oxygen quickly.")
u.mc("r", "Why is the heart called a double pump?", "One side pumps blood to the lungs and the other pumps blood to the rest of the body.", [("It beats twice as fast as other muscles.", "No."), ("It has two hearts inside.", "No."), ("It pumps air and blood.", "No.")], d="H")
u.mc("r", "White blood cells that wrap around pathogens and destroy them carry out…", "phagocytosis", ["photosynthesis", "respiration", "diffusion"], d="H")
u.mc("r", "Why is O negative blood in high demand for emergencies?", "It can be given safely to anyone.", [("It is the rarest blood.", "Not the reason."), ("It has no red cells.", "No."), ("It clots faster.", "No.")], d="H")
u.mc("r", "Capillaries are where…", "oxygen and nutrients pass to cells and waste is collected", [("blood is made", "No."), ("air enters", "No."), ("the heart beats", "No.")], d="VH")
for p, r, w in [
    ("The three parts of the circulatory system are…", "heart, blood vessels and blood", ["lungs, ribs and diaphragm", "bones, muscles and joints", "stomach, liver and gut"]),
    ("The right side of the heart pumps blood to the…", "lungs", ["brain", "legs", "stomach"]),
    ("Veins carry blood…", "back to the heart", ["away from the heart", "to the lungs only", "nowhere"]),
    ("Deoxygenated blood has…", "little oxygen", ["lots of oxygen", "no water", "no cells"]),
    ("An adult has about how much blood?", "5 litres", ["50 litres", "0.5 litres", "500 litres"]),
    ("The red pigment in red blood cells is…", "haemoglobin", ["chlorophyll", "plasma", "glucose"]),
    ("Some white blood cells make…", "antibodies", ["haemoglobin", "glucose", "bone"]),
    ("Platelets help form…", "scabs over cuts", ["new bones", "antibodies", "oxygen"]),
    ("Plasma is…", "a pale yellow liquid", ["a red solid", "a gas", "a type of bone"]),
    ("The main blood groups are…", "A, B, AB and O", ["1, 2, 3 and 4", "X and Y", "red and white"]),
    ("A universal recipient has blood group…", "AB positive", ["O negative", "A negative", "B positive"]),
    ("Blood carries carbon dioxide away from cells to the…", "lungs", ["brain", "bones", "skin only"]),
    ("Comparing blood vessels to roads is…", "an analogy", ["a fair test", "a result", "a variable"]),
    ("Pathogens are…", "microorganisms that cause disease", ["blood cells", "nutrients", "platelets"]),
]:
    u.mc("p", p, r, w)
u.gd("p", "Artery, vein or capillary?", "Vessel", [("Carries blood away from the heart", "Artery"), ("Carries blood back to the heart", "Vein"), ("Wall one cell thick", "Capillary")])
u.od("p", "Order the path of blood leaving the left side of the heart.", ["Left side of heart", "Artery", "Capillaries in body organs", "Vein", "Right side of heart"], d="H")
u.ms("p", "Select ALL the things plasma carries.", ["Blood cells", "Dissolved glucose", "Carbon dioxide"], ["Bones", "Air bubbles"])
u.mt("p", "Match the blood group to its special role.", [("O negative", "universal donor"), ("AB positive", "universal recipient")])
u.ex("a", "* Advanced. A person loses a lot of blood in an accident. Explain why they may feel tired and why a transfusion helps.", [("fewer red blood cells / less haemoglobin", ["red blood|haemoglobin|fewer"]), ("less oxygen to cells / less respiration", ["oxygen|respiration|energy"]), ("transfusion replaces blood / red cells", ["replace|transfusion|donat"])],
     "With less blood there are fewer red blood cells and less haemoglobin, so less oxygen reaches the cells for respiration and less energy is released. A transfusion replaces the lost blood.")
u.nm("a", "An adult has 5 litres of blood and 41% is red blood cells. What volume is red blood cells?", 2.05, "l", tol=0.01)
u.mc("a", "Why must donated blood be matched to the patient's blood group?", "Antibodies in the patient's blood could attack the wrong type of blood cells.", ["Different groups have different colours.", "Matching makes blood warmer.", "It does not matter."], skill="Reasoning")
u.mc("a", "Why do people living high in the mountains often have more red blood cells?", "There is less oxygen in the air, so more red cells help carry enough oxygen.", ["There is more oxygen up there.", "Cold air makes blood red.", "They eat more iron only."], skill="Reasoning")
u.stop("delivering oxygen and nutrients to cells", "Which vessels carry blood away from the heart?", "Arteries", ["Veins", "Capillaries", "Alveoli"])
u.stop("to take in and release oxygen quickly", "Red blood cells have no nucleus so that…", "there is more room for haemoglobin", ["they can divide faster", "they can fight pathogens", "they can clot"])
u.stop("they can receive any blood type", "Which blood group is the universal donor?", "O negative", ["AB positive", "A positive", "B negative"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Human body systems", "sec": None, "kids": [
    {"id": "sk", "t": "Skeleton", "d": "Support • Shape • Movement • Protection (skull, ribs)", "obj": "O1", "sec": "2.1"},
    {"id": "jt", "t": "Joints", "d": "Fixed • Hinge – elbow, knee • Ball and socket – shoulder, hip", "obj": "O1", "sec": "2.1"},
    {"id": "mu", "t": "Antagonistic muscles", "d": "Muscles only pull • Biceps and triceps • Tendons join muscle to bone", "obj": "O1", "sec": "2.1"},
    {"id": "rs", "t": "Breathing", "d": "Trachea → bronchi → bronchioles → alveoli • Ribs and diaphragm change pressure", "obj": "O2", "sec": "2.2"},
    {"id": "ge", "t": "Gas exchange", "d": "Alveoli and capillaries • Diffusion high → low • Walls one cell thick", "obj": "O3", "sec": "2.2"},
    {"id": "resp", "t": "Aerobic respiration", "d": "glucose + oxygen → carbon dioxide + water • In mitochondria • Releases energy", "obj": "O3", "sec": "2.2"},
    {"id": "ht", "t": "Heart and vessels", "d": "Double pump • Arteries away • Veins back • Capillaries exchange", "obj": "O4", "sec": "2.3"},
    {"id": "bl", "t": "Blood", "d": "Plasma • Red cells – oxygen • White cells – defence • Platelets – clotting", "obj": "O4", "sec": "2.3"},
]}
