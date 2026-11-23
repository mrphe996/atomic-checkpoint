# -*- coding: utf-8 -*-
"""Stage 8 Unit 1 – Diet and Growth. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Biology"
BLURB = "The nutrients in food and their jobs, balancing energy in and out, what a balanced diet looks like, and the habits that help or harm growth and health."
OBJECTIVES = {
    "O1": {"sec": "1.1", "code": "8Bp.01", "codeNote": "", "t": "Identify the nutrients in a balanced diet and the job of each, including vitamins A, C and D, calcium and iron, water and fibre."},
    "O2": {"sec": "1.1", "code": "8Bp.02", "codeNote": "", "t": "Explain why we need food, and that carbohydrates and fats are the body's main energy stores."},
    "O3": {"sec": "1.2", "code": "8Bp.01, 8Bp.03", "codeNote": "", "t": "Balance energy in and energy out, describe a balanced diet and explain the effects of malnutrition."},
    "O4": {"sec": "1.3", "code": "8Bp.03, 8SIC.05", "codeNote": "", "t": "Discuss how sleep, exercise, alcohol, smoking and vaping affect growth and health, and how food choices affect the environment."},
}
SECTIONS = [
    {"id": "1.1", "title": "Nutrients in food", "objs": ["O1", "O2"]},
    {"id": "1.2", "title": "A balanced diet", "objs": ["O3"]},
    {"id": "1.3", "title": "Healthy and unhealthy habits", "objs": ["O4"]},
]
u = Unit(8, 1)

# ---------------------------------------------------------------- 1.1
u.sec("1.1", "O1")
u.gd("r", "Which nutrient is each food rich in?", "Nutrient", [("Rice", "Carbohydrate"), ("Eggs", "Protein"), ("Olive oil", "Fats and oils"), ("Oranges", "Vitamins")])
u.mc("r", "Which nutrient is needed for the growth and repair of cells?", "Protein", [("Carbohydrate", "Carbohydrates mainly give energy."), ("Fibre", "Fibre is not a nutrient."), ("Water", "Water is essential but not used to build cells.")])
u.mc("r", "Why are fats and oils the body's main energy store?", "They hold more than double the energy of the same mass of carbohydrate.", [("They are digested fastest.", "Sugars are absorbed fastest."), ("They contain fibre.", "No."), ("They are made of protein.", "No.")], o="O2", d="H")
u.mt("r", "Match each vitamin or mineral to its job.", [("Vitamin A", "healthy eyes and skin"), ("Vitamin C", "healthy gums and healing cuts"), ("Vitamin D", "absorbing calcium"), ("Iron", "making haemoglobin")])
u.tb("r", "Fats give about 37 kJ per gram and carbohydrates about 17 kJ per gram. Complete the table.", ["Food", "Mass (g)", "Energy (kJ)"], [["Fat", "10", B(370)], ["Carbohydrate", "10", B(170)]], o="O2")
u.ex("r", "Fibre is not a nutrient. Explain why we still need it in our diet.", [("not digested", ["not digest|can.t digest|cannot digest"]), ("keeps the digestive system healthy / moves waste", ["move|waste|constipation|bulk|digestive"]), ("helps you feel full / slows sugar absorption", ["full|slow"])],
     "Fibre cannot be digested, so it is not a nutrient, but it adds bulk, moves waste through the gut, prevents constipation and helps us feel full.")
u.mc("r", "A person feels tired and weak and has pale skin. Which mineral are they most likely short of?", "Iron", [("Calcium", "Calcium is for bones and teeth."), ("Sodium", "No."), ("Vitamin C", "Vitamin C is a vitamin, not a mineral.")], d="H")
u.mc("r", "When does the body start to break down protein from muscle for energy?", "When its carbohydrate and fat stores run out", [("After every meal", "No."), ("When it is cold", "No."), ("During sleep every night", "No.")], o="O2", d="VH")
for p, r, w in [
    ("Starch is a…", "complex carbohydrate", ["protein", "vitamin", "mineral"]),
    ("Which food is a good source of starch?", "Potatoes", ["Cheese", "Butter", "Oranges"]),
    ("Sugars give energy quickly because they…", "are absorbed into the blood quickly", ["contain fibre", "are stored in bones", "are proteins"]),
    ("Extra carbohydrate that the body does not use is…", "turned into fat and stored", ["passed out in sweat", "turned into protein", "made into vitamins"]),
    ("Proteins are also needed to make…", "enzymes and hormones", ["fibre", "starch", "calcium"]),
    ("Vegans can get protein from…", "peas and beans", ["butter", "honey", "sugar"]),
    ("Fats and oils help to…", "keep us warm and protect organs", ["make haemoglobin", "heal cuts", "absorb iron"]),
    ("A small store of carbohydrate in the liver is called…", "glycogen", ["glucose", "starch", "haemoglobin"]),
    ("A lack of vitamin A can make it hard to…", "see in dim light", ["digest food", "grow hair", "taste food"]),
    ("Which fruit is a good source of vitamin C?", "Strawberries", ["Bread", "Rice", "Milk"]),
    ("Our skin can make vitamin D when exposed to…", "sunlight", ["cold air", "water", "darkness"]),
    ("Calcium is needed for strong…", "bones and teeth", ["eyesight", "gums", "hair"]),
    ("Haemoglobin carries…", "oxygen in red blood cells", ["fat in the liver", "fibre in the gut", "calcium in bones"]),
    ("About how much water should we drink each day?", "1.5 to 2 litres", ["0.1 litres", "10 litres", "none if we eat fruit"]),
    ("We lose water when we…", "sweat, urinate and breathe out", ["sleep only", "eat bread", "sit still"]),
]:
    u.mc("p", p, r, w)
u.gd("p", "Nutrient or not a nutrient?", "Type", [("Protein", "Nutrient"), ("Fibre", "Not a nutrient"), ("Vitamin C", "Nutrient"), ("Water", "Not a nutrient")])
u.od("p", "Order the energy sources in the order the body uses them, first to last.", ["Carbohydrates", "Fats", "Proteins (from muscle)"], d="H", o="O2")
u.ms("p", "Select ALL the jobs of water in the body.", ["It is a major part of blood", "It is needed for chemical reactions"], ["It gives us most of our energy", "It builds bones"])
u.ex("a", "* Advanced. A hibernating bear survives the winter without eating. Use ideas about energy stores to explain how.", [("stores fat before winter", ["fat|store"]), ("fat has a lot of energy per gram", ["energy|double|more energy"]), ("uses the fat slowly / respires it", ["use|slow|break down|release"])],
     "Before winter the bear eats a lot and stores fat. Fat holds more than twice the energy of carbohydrate per gram, so the bear can slowly use this store for energy all winter.", o="O2")
u.nm("a", "A snack bar has 12 g of fat (37 kJ/g) and 20 g of carbohydrate (17 kJ/g). How much energy is in these two nutrients altogether?", 784, "kJ", o="O2")
u.mc("a", "Too much of some vitamins can be harmful. What does this show about a healthy diet?", "The right amount matters – both too little and too much can cause problems.", ["Vitamins should be avoided.", "Only minerals matter.", "More is always better."])
u.mc("a", "Why does vitamin C help someone with low iron?", "It helps the body absorb iron.", ["It is made of iron.", "It replaces iron.", "It makes haemoglobin without iron."], skill="Reasoning")
u.stop("fats and oils store energy", "Which nutrient mainly gives us energy?", "Carbohydrates", ["Proteins", "Vitamins", "Minerals"])
u.stop("slows down sugar absorption", "Fibre is not a nutrient because…", "we cannot digest it", ["it has no taste", "it is a protein", "it contains too much energy"])
u.stop("Too little iron makes us tired and weak", "Which mineral is needed to make haemoglobin?", "Iron", ["Calcium", "Vitamin D", "Fibre"])

# ---------------------------------------------------------------- 1.2
u.sec("1.2", "O3")
u.mc("r", "What happens if you take in more energy from food than you use?", "The extra is stored as fat.", [("You grow taller.", "No."), ("It is all lost as heat.", "No."), ("It is turned into vitamins.", "No.")])
u.gd("r", "On a healthy eating plate, how much of the plate should each food group fill?", "Share", [("Fruit and vegetables", "Half"), ("Starchy foods", "A quarter"), ("Protein foods", "A quarter")])
u.tb("r", "A boy takes in 9800 kJ a day and uses 9100 kJ. Complete the table.", ["Energy in (kJ)", "Energy used (kJ)", "Extra each day (kJ)"], [["9800", "9100", B(700)]])
u.ex("r", "Explain why a growing teenager and an older adult may need different diets.", [("energy needs depend on age / activity", ["age|active|activity|grow"]), ("teenager needs protein and calcium for growth", ["protein|calcium|bones|muscle"]), ("older adult may need more vitamin D / fibre", ["vitamin d|fibre|older"])],
     "Energy needs depend on age and how active you are. A growing teenager needs plenty of protein and calcium for muscles and bones, while an older adult may need more vitamin D and fibre.")
u.mc("r", "Malnutrition means…", "not getting the right amounts of nutrients – too little or too much", [("only eating too little", "Too much is also malnutrition."), ("eating no vegetables", "Too narrow."), ("drinking too much water", "No.")])
u.mc("r", "A severe lack of protein causes a disease called…", "kwashiorkor", ["scurvy", "rickets", "anaemia"], d="H")
u.ms("r", "Select ALL the health risks linked to obesity.", ["Heart disease", "High blood pressure", "A type of diabetes"], [("Bleeding gums", "Lack of vitamin C."), ("Night blindness", "Lack of vitamin A.")], d="H")
u.mc("r", "Two students eat the same food. One plays sport every day. Who needs more energy from food?", "The student who plays sport", ["The other student", "They need exactly the same", "Neither needs energy"], d="VH")
for p, r, w in [
    ("Food energy is measured in…", "kilojoules or kilocalories", ["newtons", "litres", "grams only"]),
    ("Where can you find the energy content of a packaged food?", "On the food label", ["On the price tag", "In the barcode only", "Nowhere"]),
    ("A balanced diet contains…", "a variety of foods giving all the nutrients we need", ["only fruit", "mostly sugar", "only protein"]),
    ("Which drink is the healthier choice?", "Water", ["Sugary cola", "Energy drink", "Milkshake with syrup"]),
    ("Wholegrain starchy foods also give us…", "fibre", ["extra salt", "alcohol", "nicotine"]),
    ("Which oil choice is healthier?", "Plant oils such as olive oil", ["Lard", "Butter in large amounts", "Reused frying fat"]),
    ("Eating too little for a long time leaves the body…", "weak and tired", ["stronger", "taller", "heavier"]),
    ("Energy needs do NOT depend on…", "the colour of your clothes", ["age", "how active you are", "sex"]),
    ("Obesity is caused by taking in…", "much more energy than you use over a long time", ["too little water", "too much fibre", "too much sleep"]),
    ("Growing children need plenty of calcium and…", "protein", ["alcohol", "salt", "sugar"]),
    ("If energy in equals energy out, body mass…", "stays about the same", ["goes up quickly", "goes down quickly", "doubles"]),
    ("Which meal is closest to the healthy plate?", "Vegetables, brown rice and fish", ["Chips and cola", "Cake and ice cream", "Only bread"]),
    ("Kwashiorkor is a type of…", "malnutrition", ["infection", "allergy", "injury"]),
    ("Starchy foods should fill about…", "a quarter of the plate", ["all of the plate", "none of the plate", "three quarters of the plate"]),
]:
    u.mc("p", p, r, w)
u.nm("p", "A girl eats 8500 kJ and uses 9300 kJ in a day. By how many kJ is she short?", 800, "kJ")
u.gd("p", "Too much, too little or balanced?", "Energy balance", [("Energy in 10 000 kJ, used 8000 kJ", "Too much"), ("Energy in 7000 kJ, used 9000 kJ", "Too little"), ("Energy in 9000 kJ, used 9000 kJ", "Balanced")])
u.ms("p", "Select ALL the parts of a healthy eating plate.", ["Fruit and vegetables", "Wholegrain starchy foods", "Protein foods"], ["Sugary drinks", "Sweets"])
u.od("p", "Order the plate shares from biggest to smallest.", ["Fruit and vegetables (half)", "Starchy foods (a quarter)", "Healthy oils (a little)"], d="H")
u.ex("a", "* Advanced. A marathon runner and an office worker are the same age and size. Explain why their energy needs differ and what could happen if the runner ate like the office worker.", [("runner uses more energy", ["more energy|uses more|active"]), ("energy in would be less than energy out", ["less|short|not enough"]), ("lose mass / tired / use stores", ["lose|tired|weak|store"])],
     "The runner uses far more energy in activity. Eating like the office worker would give less energy in than out, so the runner would use body stores, lose mass and feel tired.")
u.nm("a", "A food label says 400 kcal. 1 kcal = 4.2 kJ. How many kJ is this?", 1680, "kJ")
u.mc("a", "Why can someone be both overweight and malnourished?", "They take in too much energy but too little of some nutrients, such as vitamins.", ["It is impossible.", "Being overweight means all nutrients are present.", "Malnutrition only means too little food."], skill="Reasoning")
u.gd("a", "Which nutrient is most likely missing?", "Missing", [("Bleeding gums and slow healing", "Vitamin C"), ("Weak bones", "Vitamin D"), ("Tired and pale", "Iron")])
u.stop("the extra is stored as fat", "Taking in more energy than you use leads to…", "the extra being stored as fat", ["more muscle automatically", "losing mass", "nothing at all"])
u.stop("a quarter should be protein", "What fraction of a healthy plate should be fruit and vegetables?", "Half", ["A quarter", "None", "All of it"])

# ---------------------------------------------------------------- 1.3
u.sec("1.3", "O4")
u.gd("r", "Healthy or unhealthy habit?", "Habit", [("Sleeping about 8 hours", "Healthy"), ("Smoking", "Unhealthy"), ("Regular exercise", "Healthy"), ("Eating lots of salty snacks", "Unhealthy")])
u.mt("r", "Match each substance in tobacco smoke to its effect.", [("Nicotine", "is addictive and raises heart rate"), ("Carbon monoxide", "stops blood carrying oxygen"), ("Tar", "coats the lungs and can cause cancer")])
u.ex("r", "Explain why a pregnant woman should not drink alcohol or smoke.", [("alcohol can damage the baby's brain", ["brain|damage"]), ("slows the baby's growth", ["growth|grow|small"]), ("smoking reduces oxygen to the baby", ["oxygen|carbon monoxide"])],
     "Alcohol can damage the baby's brain and slow its growth, and smoking means carbon monoxide reduces the oxygen reaching the baby, so it may grow less well.")
u.mc("r", "Why should you warm up before exercise?", "To prepare muscles and joints and reduce injury", ["To burn more sugar", "To feel tired", "To stop sweating"])
u.tb("r", "Sleep survey: hours slept and test score. Complete the difference from the student who slept 9 hours.", ["Hours slept", "Test score (%)", "Lower than 9-hour student by"], [["9", "82", "0"], ["7", "74", B(8)], ["5", "61", B(21)]])
u.mc("r", "Why do cattle farms affect the climate?", "Cattle release methane and carbon dioxide, which are greenhouse gases", ["Cattle absorb carbon dioxide", "Cattle make oxygen", "Grass makes the air colder"], d="H")
u.mc("r", "Which is a benefit of plant-based burgers for the environment?", "They need less land and release fewer greenhouse gases", ["They contain more fat", "They need more cattle", "They are always cheaper"], d="H")
u.mc("r", "Second-hand smoke can harm…", "people nearby, including children", ["only the smoker", "nobody", "only plants"], d="VH")
for p, r, w in [
    ("Regular exercise makes which organs stronger?", "Heart and lungs", ["Stomach and liver", "Skin and hair", "Teeth only"]),
    ("Lifting weights mainly builds…", "muscle strength", ["flexibility", "eyesight", "fat"]),
    ("Stretching and yoga improve…", "flexibility", ["eyesight", "height", "sugar levels"]),
    ("After exercise you should…", "cool down", ["sleep immediately", "eat sweets", "stop suddenly and sit"]),
    ("A diet very high in sugar can cause…", "weight gain and diabetes", ["stronger bones", "better eyesight", "more energy forever"]),
    ("A lack of protein, calcium and vitamin D can…", "stunt growth and weaken bones", ["make hair grow faster", "improve sleep", "cure illness"]),
    ("Alcohol can lead to…", "addiction and brain damage", ["stronger muscles", "better memory", "healthy growth"]),
    ("Nicotine is…", "addictive", ["a vitamin", "a mineral", "a protein"]),
    ("Carbon monoxide in smoke…", "stops the blood carrying oxygen", ["cleans the lungs", "makes bones strong", "adds vitamins"]),
    ("Tar from tobacco increases the risk of…", "lung cancer", ["strong bones", "good eyesight", "faster growth"]),
    ("Vaping is…", "harmful to health", ["a healthy habit", "a type of exercise", "a source of vitamins"]),
    ("Clearing forests for grazing animals is called…", "deforestation", ["photosynthesis", "respiration", "digestion"]),
    ("Plant-based burgers can use beet juice for…", "colour", ["protein", "fat", "salt"]),
    ("Exercise helps sleep and also…", "reduces stress and lifts mood", ["causes addiction", "weakens bones", "raises blood pressure permanently"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the healthy habits.", ["Getting enough sleep", "Exercising regularly", "Drinking water"], ["Smoking", "Vaping"])
u.gd("p", "Which type of exercise mainly helps each?", "Main benefit", [("Running", "Heart and lungs"), ("Lifting weights", "Muscle strength"), ("Yoga", "Flexibility")])
u.od("p", "Order a safe exercise session.", ["Warm up", "Start slowly", "Exercise harder", "Cool down"])
u.mc("p", "Pea protein is useful in plant-based burgers because it…", "contains all the essential building blocks of proteins", ["has no nutrients", "is mostly sugar", "is made of fat"], d="H")
u.ex("a", "* Advanced. Evaluate the claim 'Everyone should stop eating meat to save the planet.' Give one argument for and one against.", [("for: less methane / land / deforestation", ["methane|land|forest|greenhouse"]), ("against: need enough nutrients / protein, iron / choice / livelihoods", ["nutrient|protein|iron|farmer|choice|culture"])],
     "For: cattle release methane and need land, which causes deforestation. Against: people must still get enough protein and iron from other foods, and some communities depend on farming.")
u.mc("a", "Why does carbon monoxide make a smoker short of breath during exercise?", "It takes the place of oxygen in red blood cells, so less oxygen reaches the muscles.", ["It makes the lungs bigger.", "It adds extra oxygen.", "It speeds up digestion."], skill="Reasoning")
u.gr("a", "* Advanced. Data: minutes of exercise per day and resting heart rate. Plot the points.", {"label": "Exercise (min/day)", "min": 0, "max": 60, "step": 15}, {"label": "Resting heart rate (beats/min)", "min": 50, "max": 90, "step": 10}, [[0, 82], [15, 76], [30, 70], [45, 65], [60, 60]])
u.mc("a", "What does the graph of exercise and resting heart rate suggest?", "More regular exercise is linked to a lower resting heart rate.", ["Exercise raises resting heart rate.", "There is no pattern.", "Heart rate does not change."], skill="Data")
u.stop("cool down afterwards", "Which activity mainly builds muscle strength?", "Lifting weights", ["Yoga", "Sleeping", "Stretching"])
u.stop("increases the risk of lung cancer", "Which substance in tobacco smoke is addictive?", "Nicotine", ["Tar", "Oxygen", "Water"])
u.stop("which can lead to deforestation", "Why does demand for meat affect forests?", "More land is cleared for grazing and animal feed.", ["Cattle eat trees.", "Meat contains wood.", "Forests need cattle."])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Diet and growth", "sec": None, "kids": [
    {"id": "nut", "t": "Nutrients", "d": "Carbohydrates – energy • Proteins – growth and repair • Fats – energy store • Vitamins and minerals", "obj": "O1", "sec": "1.1"},
    {"id": "vit", "t": "Vitamins and minerals", "d": "A – eyes • C – gums, healing • D – calcium • Calcium – bones • Iron – haemoglobin", "obj": "O1", "sec": "1.1"},
    {"id": "wf", "t": "Water and fibre", "d": "Not nutrients but essential • Water – blood, reactions • Fibre – healthy gut", "obj": "O1", "sec": "1.1"},
    {"id": "bal", "t": "Balanced diet", "d": "Energy in = energy out • Half fruit and veg • Quarter starch • Quarter protein", "obj": "O3", "sec": "1.2"},
    {"id": "mal", "t": "Malnutrition", "d": "Too little or too much • Kwashiorkor • Obesity", "obj": "O3", "sec": "1.2"},
    {"id": "hab", "t": "Healthy habits", "d": "Sleep about 8 hours • Regular exercise • Warm up and cool down", "obj": "O4", "sec": "1.3"},
    {"id": "harm", "t": "Harmful habits", "d": "Alcohol • Smoking and vaping • Nicotine, carbon monoxide, tar", "obj": "O4", "sec": "1.3"},
    {"id": "env", "t": "Food and the planet", "d": "Cattle release methane • Deforestation • Plant-based burgers", "obj": "O4", "sec": "1.3"},
]}
