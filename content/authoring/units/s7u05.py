# -*- coding: utf-8 -*-
"""Stage 7 Unit 5 – Food Chains and Food Webs. Written by the Camday teaching team."""
from c_kit import *

STRAND = "Biology"
BLURB = "Microorganisms and decomposition, and how energy passes along food chains and food webs – including what happens when one species changes."

OBJECTIVES = {
    "O1": {"sec": "5.1", "code": "7Bs.01", "codeNote": "microorganisms are usually single cells", "t": "Describe microorganisms (bacteria, fungi, protists), where they live, and helpful and harmful examples."},
    "O2": {"sec": "5.1", "code": "7Be.01", "codeNote": "", "t": "Describe the role of microorganisms as decomposers that recycle nutrients."},
    "O3": {"sec": "5.2", "code": "7Be.02", "codeNote": "", "t": "Construct and interpret food chains and food webs, including producers, consumers and decomposers."},
    "O4": {"sec": "5.2", "code": "7SIC.05", "codeNote": "human impacts on food webs", "t": "Predict how a change to one population (or human impacts such as microplastics) affects a food web."},
}

SECTIONS = [
    {"id": "5.1", "title": "Microorganisms as decomposers", "objs": ["O1", "O2"]},
    {"id": "5.2", "title": "Food chains and food webs", "objs": ["O3", "O4"]},
]

WEB = "Food web: grass → grasshopper; grass → rabbit; grasshopper → frog; grasshopper → spider; spider → frog; frog → snake; rabbit → snake; rabbit → hawk; snake → hawk."

S1_REQ = [
    mc("u5s1r1", "M", "O1", "Why do we usually need a microscope to see a microorganism?", ("Most are just one cell, which is far too small to see.", "Correct: micro = very small, organism = living thing."),
       [("They are invisible because they are not living.", "Microorganisms are living."), ("They only come out at night.", "No."), ("They are made of glass.", "No.")]),
    mt("u5s1r2", "M", "O1", "Match each microorganism to its group.", [("Bacteria", "single cells found almost everywhere"), ("Mould", "tiny fungus"), ("Alga", "protist that can photosynthesise"), ("Amoeba", "protist that cannot photosynthesise")]),
    gd("u5s1r3", "H", "O1", "Helpful or harmful?", ["Effect"], [("Gut bacteria that help break down food", ["Helpful"]), ("Mouth bacteria that cause tooth decay", ["Harmful"]), ("Fungus that causes athlete's foot", ["Harmful"]), ("Skin bacteria that help fight infection", ["Helpful"]), ("Decomposers in soil", ["Helpful"])], skill="Data"),
    od("u5s1r4", "H", "O2", "Put the steps of decomposition in order.",
       ["Plants grow using mineral salts from the soil", "Leaves and plants die and fall to the ground", "Microorganisms feed on and respire the dead matter", "Dead matter is broken down into simpler substances", "Mineral salts are released into the soil and absorbed by roots"]),
    tb("u5s1r5", "H", "O2", "Data: dead leaves in net bags lost mass over time. The starting mass was 100 g. Complete the table.",
       ["Time (months)", "Mass lost (%)", "Mass left (g)"], [["1", "20", B(80)], ["3", "45", B(55)], ["9", "70", B(30)]],
       hint="Mass left = 100 − percentage lost (because the start was 100 g).", reason="100 − 20 = 80; 100 − 45 = 55; 100 − 70 = 30."),
    mc("u5s1r6", "H", "O2", "In the leaf-bag investigation, what is the dependent variable?", ("The mass of the leaves", "Correct – it is what was measured."),
       [("Time", "Time is the independent variable (what was changed)."), ("The type of leaves", "A control variable."), ("The place the bags were left", "A control variable.")], skill="Experiment"),
    ex("u5s1r7", "H", "O2", "Explain why decomposers are important in an ecosystem.",
       [("break down dead matter / wastes", ["break(s)? down", "dead", "waste", "decompos"]), ("release / recycle mineral salts or nutrients", ["mineral|nutrient|recycl"]), ("plants can use them / waste does not build up", ["plant|root|build up|pile"])],
       "Decomposers break down dead organisms and wastes, which stops waste building up. This releases mineral salts into the soil, so they are recycled and can be absorbed by plants again.", need=2),
    gr("u5s1r8", "VH", "O2", "Data: plot the percentage of leaf mass LOST over time.", {"label": "Time (months)", "min": 0, "max": 9, "step": 1}, {"label": "Mass lost (%)", "min": 0, "max": 80, "step": 10},
       [[0, 0], [1, 20], [3, 45], [9, 70]],
       follow=mc("u5s1r8f", "VH", "O2", "What is the best prediction for 12 months?", ("A little more than 70% lost – the loss keeps going but more slowly.", "Correct: the curve is levelling off."),
                 [("Exactly 100% lost.", "The rate is slowing; not all may be gone."), ("Less than 70% lost.", "Mass cannot come back."), ("Back to 0%.", "No.")])),
]
S1_PRAC = [
    mc("u5s1p01", "M", "O1", "What does 'micro' mean?", "Very small", [("Living", "That is 'organism'."), ("Green", "No."), ("Old", "No.")]),
    mc("u5s1p02", "M", "O1", "A microorganism that causes disease is called a…", "pathogen", [("producer", "Makes food."), ("decomposer", "Breaks down dead matter."), ("colony", "A group growing together.")]),
    mc("u5s1p03", "M", "O1", "Why can you see mould on old bread without a microscope?", "Millions of cells grow together as a colony.", [("Each mould cell is huge.", "Each is tiny."), ("Bread is a magnifying glass.", "No."), ("Mould is not a microorganism.", "It is a fungus.")]),
    ms("u5s1p04", "M", "O1", "Select ALL the places microorganisms live.", ["Soil", "Fresh, salty and brackish water", "On and inside animals' bodies", "In waste"], [("Nowhere – they are rare", "They live almost everywhere.")]),
    mc("u5s1p05", "M", "O1", "Which protist can photosynthesise?", "Alga", [("Amoeba", "Cannot photosynthesise."), ("Mould", "A fungus."), ("Bacterium", "Not a protist.")]),
    mc("u5s1p06", "H", "O1", "How do bacteria in your nose help you?", "They help stop harmful microbes getting in.", [("They make you sneeze all day.", "No."), ("They digest food.", "That is gut bacteria."), ("They make your hair grow.", "No.")]),
    mc("u5s1p07", "M", "O2", "Microorganisms that break down dead matter are called…", "decomposers", [("producers", "Make food."), ("predators", "Hunt prey."), ("herbivores", "Eat plants.")]),
    mc("u5s1p08", "M", "O2", "Decomposition releases ___ into the soil.", "mineral salts", [("sunlight", "No."), ("plastic", "No."), ("oxygen only", "Not the main point.")]),
    mc("u5s1p09", "H", "O2", "What would happen to dead leaves in a forest with NO decomposers?", "They would pile up and nutrients would not be recycled.", [("They would disappear faster.", "Decomposers make them disappear."), ("Plants would grow better.", "Fewer nutrients for plants."), ("Nothing would change.", "Waste would build up.")], skill="Reasoning"),
    mc("u5s1p10", "M", "O2", "Earthworms break dead matter into smaller pieces. They are called…", "detritivores", [("producers", "No."), ("pathogens", "No."), ("carnivores", "No.")]),
    mc("u5s1p11", "H", "O2", "An ecosystem is…", "all the living and non-living parts of an area", [("only the animals in an area", "Plants and non-living parts too."), ("a single food chain", "Much more."), ("a type of microorganism", "No.")]),
    ms("u5s1p12", "M", "O2", "Select ALL the non-living parts of an ecosystem.", ["Sunlight", "Rain", "Temperature", "Soil"], [("Fungi", "Living."), ("Trees", "Living.")]),
    mc("u5s1p13", "H", "O2", "In the leaf-bag investigation, which is a control variable?", "The type of leaves", [("The time", "Independent variable."), ("The mass of leaves", "Dependent variable."), ("The result", "Not a variable to control.")], skill="Experiment"),
    nm("u5s1p14", "H", "O2", "A 200 g pile of leaves loses 45% of its mass. How many grams are lost?", 90, "g", errs=[(110, "That is the mass LEFT. Mass lost = 45% of 200 = 90 g.")], reason="45 ÷ 100 × 200 = 90 g."),
    mc("u5s1p15", "H", "O2", "Which is the only thing that must come into an ecosystem from outside?", "Energy, as light from the Sun", [("Water", "Water cycles round."), ("Mineral salts", "These are recycled."), ("Carbon dioxide", "Recycled by living things.")]),
    mc("u5s1p16", "M", "O1", "Mouth bacteria can cause…", "tooth decay and bad breath", [("athlete's foot", "Fungus on feet."), ("dandruff", "Fungus on the scalp."), ("photosynthesis", "No.")]),
    mc("u5s1p17", "H", "O2", "Why does food go mouldy faster when it is warm and moist?", "Microorganisms grow and respire faster in warm, moist conditions.", [("Warmth kills microorganisms.", "Usually warmth helps them grow."), ("Mould is made by the fridge.", "No."), ("Dry food rots fastest.", "Moisture helps decay.")], skill="Reasoning"),
    od("u5s1p18", "M", "O2", "Order the nutrient cycle starting from a living plant.", ["Living plant", "Dead leaves fall", "Decomposers break them down", "Mineral salts in soil", "New plant absorbs them"]),
]
S1_ADV = [
    adv(ex("u5s1a1", "VH", "O2", "A student wants to test whether leaves decompose faster in warm or cold conditions using net bags. Describe a fair test.",
           [("change only temperature", ["temperature|warm|cold"]), ("keep leaf type / mass / bag the same", ["same|control|type of leaves|mass"]), ("measure mass after the same time", ["mass|weigh", "time|weeks|months"])],
           "Put the same mass of the same type of leaves into identical bags. Leave some in a warm place and some in a cold place for the same time, keeping moisture the same. Measure the mass left to compare.", need=2)),
    adv(mc("u5s1a2", "VH", "O2", "Mass loss was 20% after 1 month but only 25% more over the next 6 months (45% → 70%). Why does decomposition slow down?", ("The easy-to-digest parts go first; tougher parts take longer.", "Correct – a reasonable explanation."),
           [("Decomposers stop respiring.", "They still respire."), ("The leaves become heavier.", "Mass keeps falling."), ("Time stops.", "No.")], skill="Reasoning")),
    adv(mc("u5s1a3", "VH", "O1", "Why are some microorganisms grown on purpose by people?", ("For useful products such as bread, yoghurt and medicines.", "Correct."),
           [("To cause disease.", "No."), ("To make soil infertile.", "No."), ("Because they are plants.", "Most are not.")])),
    adv(nm("u5s1a4", "VH", "O1", "A bacterium divides into two every 20 minutes. Starting with 1, how many are there after 2 hours (if none die)?", 64, "bacteria", hint="2 hours = 6 divisions.", reason="2⁶ = 64.")),
]

S2_REQ = [
    mc("u5s2r1", "M", "O3", "What do the arrows in a food chain show?", ("The direction energy flows – 'is eaten by'.", "Correct."),
       [("Who is bigger.", "Size is not shown."), ("Which way animals walk.", "No."), ("Who eats whom backwards.", "The arrow points to the eater.")]),
    od("u5s2r2", "M", "O3", "Build the food chain: chameleons eat termites, pythons eat chameleons, termites eat banana leaves.", ["Banana leaves", "Termites", "Chameleons", "Pythons"]),
    gd("u5s2r3", "H", "O3", "Ocean chain: phytoplankton → zooplankton → fish → shark. Name each position.", ["Position"],
       [("Phytoplankton", ["Producer"]), ("Zooplankton", ["Primary consumer"]), ("Fish", ["Secondary consumer"]), ("Shark", ["Tertiary consumer"])], skill="Data"),
    mc("u5s2r4", "M", "O3", "Why does every food chain start with a producer?", ("Producers make their own food by photosynthesis, bringing energy into the chain.", "Correct."),
       [("Producers are the biggest organisms.", "Size does not matter."), ("Producers eat everything else.", "They make food; they don't eat."), ("It is a rule with no reason.", "Energy enters through producers.")]),
    nm("u5s2r5", "H", "O3", WEB + " How many different food chains in this web start with grass and end with the hawk?", 4, "food chains", skill="Data",
       hint="Trace every route: through the rabbit, and through the grasshopper.", reason="grass→rabbit→hawk; grass→rabbit→snake→hawk; grass→grasshopper→frog→snake→hawk; grass→grasshopper→spider→frog→snake→hawk = 4."),
    mc("u5s2r6", "H", "O3", WEB + " The frog eats grasshoppers and spiders. Which consumer is it?", ("Both a secondary consumer (eating grasshoppers) and a tertiary consumer (eating spiders).", "Correct – in a web an animal can be at more than one level."),
       [("Only a primary consumer.", "It does not eat plants."), ("A producer.", "It does not photosynthesise."), ("Only a quaternary consumer.", "No.")], skill="Data"),
    ex("u5s2r7", "H", "O4", WEB + " Snakes are removed. Predict and explain ONE effect on the food web.",
       [("frogs (or rabbits) increase", ["frogs?|rabbits?", "increase|more|go up"]), ("because they are no longer eaten", ["eaten|predator|no snake|hunted"]), ("hawks have less food / eat more rabbits", ["hawk"])],
       "Frogs and rabbits would probably increase because snakes no longer eat them. Hawks lose one food source so they may eat more rabbits.", need=2),
    mc("u5s2r8", "VH", "O4", "Microplastics have been found in animals at the top of food chains, even penguins in Antarctica. How do they get there?", ("Small animals eat them by mistake; predators eat those animals, so the plastic passes up the chain.", "Correct."),
       [("Penguins collect plastic to build nests.", "Not the main route described."), ("Plastic is a producer.", "No."), ("The Sun makes plastic in the sea.", "No.")], skill="Reasoning"),
]
S2_PRAC = [
    mc("u5s2p01", "M", "O3", "An organism that makes its own food is a…", "producer", [("consumer", "Eats others."), ("decomposer", "Breaks down dead matter."), ("predator", "Hunts.")]),
    mc("u5s2p02", "M", "O3", "Herbivores eat…", "plants", [("animals", "Carnivores."), ("both plants and animals", "Omnivores."), ("dead matter only", "Detritivores/decomposers.")]),
    mc("u5s2p03", "M", "O3", "Humans eat plants and animals, so we are…", "omnivores", [("herbivores", "Only plants."), ("carnivores", "Only animals."), ("producers", "We cannot photosynthesise.")]),
    mc("u5s2p04", "M", "O3", "A lion hunts a zebra. The zebra is the…", "prey", [("predator", "The lion."), ("producer", "No."), ("decomposer", "No.")]),
    mc("u5s2p05", "H", "O3", "What does a plant need for photosynthesis?", "Light, carbon dioxide and water", [("Oxygen and sugar", "These are products."), ("Soil and darkness", "Light is needed."), ("Meat and water", "No.")]),
    mc("u5s2p06", "H", "O3", "What does photosynthesis produce?", "Glucose (food) and oxygen", [("Carbon dioxide and water", "These are used up."), ("Mineral salts", "No."), ("Light", "Light is used.")]),
    mc("u5s2p07", "H", "O3", "The copper beech has red leaves. Is it a producer?", "Yes – red pigments hide its chlorophyll but it still photosynthesises.", [("No – only green plants photosynthesise.", "It still has chlorophyll."), ("No – it is a consumer.", "No."), ("Only in winter.", "No.")]),
    od("u5s2p08", "M", "O3", "Order this mangrove food chain.", ["Mangrove plants", "Crab", "Kingfisher", "Python"]),
    mc("u5s2p09", "H", "O3", "In 'mangrove → crab → kingfisher → python', the kingfisher is the…", "secondary consumer", [("primary consumer", "The crab."), ("producer", "Mangrove."), ("tertiary consumer", "The python.")]),
    mc("u5s2p10", "H", "O3", "An animal that eats a tertiary consumer is a…", "quaternary consumer", [("primary consumer", "No."), ("producer", "No."), ("secondary consumer", "No.")]),
    mc("u5s2p11", "M", "O3", "A food web is…", "many food chains joined together", [("one food chain", "A web has many."), ("a spider's web", "No."), ("a list of plants", "No.")]),
    mc("u5s2p12", "H", "O3", WEB + " Which organisms are primary consumers?", "Grasshopper and rabbit", [("Frog and spider", "They eat animals."), ("Snake and hawk", "They eat animals."), ("Grass", "Producer.")], skill="Data"),
    mc("u5s2p13", "H", "O4", WEB + " Grasshoppers die out. What happens to spiders?", "They decrease – they lose their only food.", [("They increase.", "Less food."), ("Nothing changes.", "Their food is gone."), ("They start eating grass.", "Spiders are carnivores.")], skill="Data"),
    mc("u5s2p14", "M", "O3", "Where do decomposers fit in a food web?", "They break down dead organisms and wastes from every level.", [("Only at the top.", "Every level."), ("They are producers.", "No."), ("They are not part of webs.", "They are.")]),
    mc("u5s2p15", "H", "O4", "Why did huge jellyfish swarms appear on Mediterranean coasts?", "A warmer sea from climate change lets jellyfish breed and grow faster.", [("The sea got colder.", "Warmer."), ("More sharks ate jellyfish.", "No."), ("Plastic turned into jellyfish.", "No.")]),
    mc("u5s2p16", "H", "O4", "More jellyfish eat more phytoplankton. Which animals get LESS food?", "Small fish (and then whales, seals and seabirds)", [("Turtles", "They eat jellyfish – more food."), ("Sunfish", "More food."), ("Jellyfish", "More food.")], skill="Reasoning"),
    mc("u5s2p17", "M", "O4", "PLA is a plastic made from plants. Why is it useful?", "Decomposers can break it down into water and carbon dioxide.", [("It never breaks down.", "It is biodegradable."), ("It is a food for sharks.", "No."), ("It makes the sea warmer.", "No.")]),
    mc("u5s2p18", "H", "O3", "A pit viper eats a squirrel and is eaten by an eagle. The pit viper is…", "both predator and prey", [("only a predator", "It is also eaten."), ("only prey", "It also hunts."), ("a producer", "No.")]),
]
S2_ADV = [
    adv(ex("u5s2a1", "VH", "O4", "Farmers spray a field to kill all the grasshoppers. Use the food web to explain why this could affect hawks, even though hawks do not eat grasshoppers. " + WEB,
           [("frogs / spiders lose food and decrease", ["frogs?|spiders?", "decrease|fewer|less food"]), ("snakes then have fewer frogs", ["snakes?"]), ("hawks get less food / eat more rabbits", ["hawks?"])],
           "With no grasshoppers, frogs and spiders lose food and decrease. Snakes then have fewer frogs to eat, so there are fewer snakes. Hawks eat snakes, so they get less food and may eat more rabbits.", need=2)),
    adv(mc("u5s2a2", "VH", "O3", "Why are there usually fewer top predators than herbivores in an ecosystem?", ("Energy is lost at each step of a food chain, so less is available at the top.", "Correct."),
           [("Predators are lazy.", "No."), ("Herbivores are bigger.", "Not the reason."), ("Predators do not need energy.", "They do.")], skill="Reasoning")),
    adv(mc("u5s2a3", "VH", "O4", "Turtles eat jellyfish. If sea turtles are overfished, what may happen to jellyfish and small fish?", ("Jellyfish increase, eat more phytoplankton, and small fish have less food.", "Correct."),
           [("Jellyfish decrease.", "Their predator is gone."), ("Small fish increase.", "Less food for them."), ("Nothing changes.", "Webs are linked.")], skill="Reasoning")),
    adv(gd("u5s2a4", "VH", "O3", "Name the role of each organism in: algae → shrimp → jellyfish → turtle → shark.", ["Role"],
           [("Algae", ["Producer"]), ("Shrimp", ["Primary consumer"]), ("Jellyfish", ["Secondary consumer"]), ("Turtle", ["Tertiary consumer"]), ("Shark", ["Quaternary consumer"])], skill="Data")),
]

POOLS = {"5.1": (S1_REQ, S1_PRAC, S1_ADV), "5.2": (S2_REQ, S2_PRAC, S2_ADV)}

STOPS = {
    "5.1": [stop("u5v1a", "big enough to see without a microscope", mc("u5v1a_q", "M", "O1", "Mould is a kind of…", "fungus", [("bacterium", "No."), ("plant", "No."), ("animal", "No.")])),
            stop("u5v1b", "is called a pathogen", mc("u5v1b_q", "M", "O1", "A pathogen is a microorganism that…", "causes disease", [("makes food", "No."), ("lives in soil only", "No."), ("is always helpful", "No.")])),
            stop("u5v1c", "are called decomposers", mc("u5v1c_q", "H", "O2", "What do decomposers release into the soil?", "Mineral salts", [("Sunlight", "No."), ("Seeds", "No."), ("Plastic", "No.")])),
            stop("u5v1d", "Can you predict what would happen after a year", mc("u5v1d_q", "H", "O2", "What is the independent variable in the leaf-bag investigation?", "Time", [("Mass of leaves", "Dependent."), ("Type of bag", "Control."), ("Type of leaves", "Control.")]))],
    "5.2": [stop("u5v2a", "the direction that energy flows", mc("u5v2a_q", "M", "O3", "An arrow in a food chain means…", "'is eaten by'", [("'eats'", "Arrow points to the eater."), ("'is bigger than'", "No."), ("'lives with'", "No.")])),
            stop("u5v2b", "we are omnivores", mc("u5v2b_q", "M", "O3", "A carnivore eats…", "other animals", [("plants", "Herbivore."), ("both", "Omnivore."), ("sunlight", "No.")])),
            stop("u5v2c", "it is a tertiary consumer", mc("u5v2c_q", "H", "O3", "Zooplankton eat phytoplankton. Zooplankton are…", "primary consumers", [("producers", "No."), ("secondary consumers", "No."), ("decomposers", "No.")])),
            stop("u5v2d", "One change can ripple through the whole web", mc("u5v2d_q", "H", "O4", "If one species disappears from a food web, its prey might…", "increase", [("decrease", "Fewer are eaten."), ("become producers", "No."), ("always disappear too", "No.")]))],
}

MINDMAP = {"id": "root", "t": "Food chains and webs", "sec": None, "kids": [
    {"id": "micro", "t": "Microorganisms", "d": "Bacteria, fungi (moulds), protists (algae, amoebae). Helpful or harmful (pathogens).", "obj": "O1", "sec": "5.1"},
    {"id": "decomp", "t": "Decomposers", "d": "Break down dead matter and wastes → release mineral salts → recycled by plants.", "obj": "O2", "sec": "5.1"},
    {"id": "chain", "t": "Food chains", "d": "Producer → primary → secondary → tertiary consumer. Arrows = 'is eaten by' = energy flow.", "obj": "O3", "sec": "5.2"},
    {"id": "web", "t": "Food webs", "d": "Linked chains. An animal can be at several levels. Remove one species → the web changes.", "obj": "O4", "sec": "5.2"},
    {"id": "impact", "t": "Human impacts", "d": "Microplastics pass up food chains • climate change → jellyfish swarms.", "obj": "O4", "sec": "5.2"},
]}
