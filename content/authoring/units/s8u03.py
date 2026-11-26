# -*- coding: utf-8 -*-
"""Stage 8 Unit 3 – Ecosystems. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Biology"
BLURB = "Populations, communities and ecosystems, habitats and adaptations, seed banks, and how habitat loss, invasive species, pollution and bioaccumulation affect living things."
OBJECTIVES = {
    "O1": {"sec": "3.1", "code": "8Be.01", "codeNote": "", "t": "Describe populations, communities and ecosystems, and identify the range of habitats in an ecosystem."},
    "O2": {"sec": "3.1", "code": "8Be.01, 8SIC.02", "codeNote": "", "t": "Describe physical and behavioural adaptations, and explain why seed banks protect biodiversity."},
    "O3": {"sec": "3.2", "code": "8Be.03, 8SIC.05", "codeNote": "", "t": "Explain how habitat destruction, overexploitation and invasive species affect organisms and ecosystems."},
    "O4": {"sec": "3.2", "code": "8Be.02", "codeNote": "", "t": "Describe how pollution harms ecosystems and how toxic substances bioaccumulate along food chains."},
}
SECTIONS = [
    {"id": "3.1", "title": "Ecosystems and habitats", "objs": ["O1", "O2"]},
    {"id": "3.2", "title": "Human impact on ecosystems", "objs": ["O3", "O4"]},
]
u = Unit(8, 3)

# ---------------------------------------------------------------- 3.1
u.sec("3.1", "O1")
u.gd("r", "Population, community or ecosystem?", "Level", [("A herd of elephants", "Population"), ("All the animals and plants in a savanna", "Community"), ("The savanna's living things plus light, water and temperature", "Ecosystem")])
u.mc("r", "A habitat is…", "the place where a particular organism lives", [("all the populations in an area", "That is a community."), ("one species in an area", "That is a population."), ("a type of food chain", "No.")])
u.gd("r", "Physical or behavioural adaptation?", "Type", [("Dolphin's blubber", "Physical"), ("Dolphins living in pods", "Behavioural"), ("Monkey's gripping tail", "Physical"), ("Monkeys living high in the treetops", "Behavioural")], o="O2")
u.ex("r", "Explain how two features of a dolphin help it survive in the ocean.", [("streamlined body – moves fast through water", ["streamline|fast|swim"]), ("blowhole – breathes air at the surface", ["blowhole|breath"]), ("blubber – keeps warm", ["blubber|warm|insulat"])],
     "Its streamlined body lets it move quickly through water, and its blubber keeps it warm in cold water. Its blowhole lets it breathe at the surface.", o="O2")
u.mc("r", "Which ecosystem gets little rain, lots of sun and has only a few producers?", "Desert", ["Rainforest", "Coral reef", "Pond"])
u.mc("r", "Why are seeds in a seed bank kept dark, dry and at about −20 °C?", "So they do not start to grow and stay alive for many years", [("To kill pests only", "No."), ("To make them grow faster", "No."), ("To change their DNA", "No.")], o="O2", d="H")
u.mc("r", "Non-living factors in an ecosystem include…", "light, water and temperature", [("plants and animals", "Those are living."), ("predators and prey", "Living."), ("bacteria", "Living.")], d="H")
u.mc("r", "Losing a plant species can threaten other organisms because…", "organisms depend on each other for food and shelter", [("plants eat animals", "No."), ("plants make water", "No."), ("it changes the weather at once", "No.")], o="O2", d="VH")
for p, r, w, o in [
    ("A population is…", "one species living in an area", ["all the species in an area", "the non-living factors", "one organism"], "O1"),
    ("An ecosystem can be as small as…", "a sealed glass jar", ["one cell", "an atom", "a single leaf cell"], "O1"),
    ("Forests usually have…", "lots of rain and very varied life", ["little rain and few plants", "no animals", "salt water"], "O1"),
    ("Grasslands are…", "open, sunny and windy", ["dark and wet", "under the sea", "covered in ice always"], "O1"),
    ("Which is a freshwater ecosystem?", "A river", ["The ocean", "A coral reef", "A desert"], "O1"),
    ("Oceans cover…", "most of Earth's surface", ["a tiny part of Earth", "only the poles", "no part of Earth"], "O1"),
    ("A beetle's habitat might be…", "the bark of a single tree", ["the whole planet", "the ocean floor only", "the Sun"], "O1"),
    ("Adaptations are features that…", "help an organism survive in its habitat", ["harm the organism", "are learned from books", "only plants have"], "O2"),
    ("A forest monkey's teeth are adapted to…", "grind leaves, seeds and fruit", ["tear meat only", "filter water", "drill wood"], "O2"),
    ("A dolphin breathes through its…", "blowhole", ["gills", "fins", "tail"], "O2"),
    ("Blubber helps a dolphin to…", "keep warm", ["see in the dark", "breathe underwater", "climb trees"], "O2"),
    ("The resurrection plant survives drought by…", "curling up into a ball", ["growing very tall", "swimming", "eating insects"], "O2"),
    ("About what fraction of plant species may be endangered?", "Two out of five", ["One in a million", "All of them", "None"], "O2"),
    ("Scientists store seeds in…", "seed banks", ["food webs", "landfills", "greenhouses only"], "O2"),
    ("Why are seed vaults protected from floods and earthquakes?", "To keep the seeds safe for the future", ["To make seeds grow", "To warm the seeds", "To sell the seeds"], "O2"),
]:
    u.mc("p", p, r, w, o=o)
u.od("p", "Order from smallest to largest.", ["Organism", "Population", "Community", "Ecosystem"])
u.gd("p", "Match the ecosystem to its description.", "Ecosystem", [("Very little rain", "Desert"), ("Salt water and coral", "Ocean"), ("Ponds, rivers and lakes", "Freshwater")], extra=["Grassland"])
u.ms("p", "Select ALL the adaptations of a forest monkey.", ["Long, strong limbs", "A gripping tail", "Feet that grip like hands"], ["Blubber", "A blowhole"], o="O2")
u.ex("a", "* Advanced. A seed bank stores seeds of a rare wheat variety. Explain why this could protect our food supply in the future.", [("variety may resist new disease / drought", ["disease|drought|pest|climate"]), ("can be grown again if crops fail / lost", ["grow again|replant|fail|lost|extinct"])],
     "If a disease or drought wipes out crops, the stored variety may have useful features, such as resistance, and can be grown again to replace lost crops.", o="O2")
u.mc("a", "A polar bear has small ears and thick fur. Which explanation is best?", "Both reduce heat loss in a very cold habitat.", ["Both help it swim faster.", "Both help it hide in trees.", "They are behavioural adaptations."], o="O2", skill="Reasoning")
u.mc("a", "Why is a sealed glass jar with plants, soil and water called an ecosystem?", "It has living things interacting with each other and with non-living factors.", ["It has only one species.", "It has no light.", "It contains no living things."], skill="Reasoning")
u.gd("a", "Living or non-living factor?", "Factor", [("Temperature", "Non-living"), ("Bacteria in soil", "Living"), ("Amount of light", "Non-living"), ("Predators", "Living")])
u.stop("like a herd of elephants", "One species living in an area is a…", "population", ["community", "ecosystem", "habitat"])
u.stop("as small as a sealed glass jar", "An ecosystem includes the community and…", "its non-living factors", ["only the plants", "only the predators", "nothing else"])
u.stop("and communicate with each other", "Dolphins living in pods is a…", "behavioural adaptation", ["physical adaptation", "habitat", "population"], o="O2")
u.stop("where it was collected", "Seeds in a seed bank are kept…", "dark, dry and very cold", ["warm and wet", "in sunlight", "in salt water"], o="O2")

# ---------------------------------------------------------------- 3.2
u.sec("3.2", "O3")
u.gd("r", "What type of human impact is each?", "Impact", [("Cutting down forests for farms", "Habitat destruction"), ("Catching fish faster than they can reproduce", "Overexploitation"), ("Nile perch put into Lake Victoria", "Invasive species"), ("Oil spills", "Pollution")])
u.mc("r", "An invasive species is…", "a non-native species that causes harm in its new ecosystem", [("any native species", "No."), ("a species that is extinct", "No."), ("a plant that grows slowly", "No.")])
u.tb("r", "Mercury builds up along a food chain. Each step has 10 times more than the step before. Complete the table.", ["Organism", "Mercury (units)"], [["Plankton", "1"], ["Small fish", B(10)], ["Large fish", B(100)]], o="O4")
u.ex("r", "Explain why fertilisers washed into a lake can make water plants die.", [("algae grow out of control / algal bloom", ["algae|algal|bloom"]), ("block sunlight", ["sunlight|light|block"]), ("plants cannot photosynthesise / die", ["photosynth|die|cannot"])],
     "Fertilisers make algae grow out of control (an algal bloom). The algae block sunlight, so water plants cannot photosynthesise and die.", o="O4")
u.mc("r", "Why does deforestation add to climate change?", "Forests absorb carbon dioxide, so cutting them down leaves more in the air.", [("Trees make the air colder.", "No."), ("Forests release methane only.", "No."), ("It makes more rain.", "No.")], d="H")
u.mc("r", "Bioaccumulation is…", "the slow build-up of a toxic substance in an organism's body", [("a type of fishing", "No."), ("cleaning a river", "No."), ("growth of algae", "No.")], o="O4")
u.mc("r", "Habitat fragmentation is when…", "habitats are broken into small pieces by roads, cities or farms", [("habitats grow bigger", "No."), ("new species arrive", "No."), ("rivers are cleaned", "No.")], d="H")
u.mc("r", "Why do top predators have the most mercury in their bodies?", "They eat many animals that each contain mercury, so it builds up along the food chain.", [("They live longest underwater.", "Not the main reason."), ("They drink more water.", "No."), ("Mercury is made in their bodies.", "No.")], o="O4", d="VH")
for p, r, w, o in [
    ("Deforestation means…", "cutting down forests", ["planting trees", "cleaning rivers", "farming fish"], "O3"),
    ("Bats spread the seeds of banyan trees by…", "eating the fruit", ["burying them", "carrying them on fur only", "planting them"], "O3"),
    ("If banyan trees disappeared, bat numbers would…", "fall", ["rise", "stay the same", "double"], "O3"),
    ("Overfishing is an example of…", "overexploitation", ["pollution", "fragmentation", "adaptation"], "O3"),
    ("The Nile perch harmed Lake Victoria because it…", "ate many native fish", ["made the water warmer", "was a plant", "cleaned the lake"], "O3"),
    ("Asian hornets harm ecosystems by preying on…", "native bees", ["sharks", "trees", "whales"], "O3"),
    ("Rats arriving on ships have…", "driven many native birds to extinction", ["helped birds", "pollinated flowers", "cleaned islands"], "O3"),
    ("Re-introducing wolves to Yellowstone helped…", "the ecosystem recover", ["destroy the park", "pollute rivers", "remove all deer from Earth"], "O3"),
    ("Rotting rubbish in landfills releases…", "methane", ["oxygen", "pure water", "vitamins"], "O4"),
    ("Acid rain forms when these gases dissolve in clouds:", "sulfur dioxide and nitrogen oxides", ["oxygen and nitrogen", "helium and neon", "water vapour only"], "O4"),
    ("Oil spills harm birds because oil…", "sticks to feathers", ["feeds them", "warms them", "cleans them"], "O4"),
    ("Turtles can be harmed by swallowing…", "plastic bags", ["seaweed", "plankton", "sand"], "O4"),
    ("Tiny pieces of plastic in food chains are called…", "microplastics", ["plankton", "nutrients", "minerals"], "O4"),
    ("Mercury pollution comes mainly from…", "mining and manufacturing", ["trees", "rain", "volcanoes only"], "O4"),
    ("The increase of a toxin at each step of a food chain is…", "biomagnification", ["photosynthesis", "fragmentation", "respiration"], "O4"),
]:
    u.mc("p", p, r, w, o=o)
u.gd("p", "Land, air or water pollution?", "Type", [("Litter seeping chemicals into soil", "Land"), ("Car exhaust fumes", "Air"), ("Fertiliser runoff", "Water")], o="O4")
u.od("p", "Order the food chain from least to most mercury.", ["Plankton", "Small fish", "Large fish", "Fish-eating bird"], o="O4")
u.ms("p", "Select ALL the ways humans destroy or break up habitats.", ["Building roads", "Clearing forests for farms", "Building cities"], ["Planting native trees", "Creating nature reserves"])
u.ex("a", "* Advanced. Explain how removing banyan trees from a forest could reduce the number of hawks.", [("bats lose food / bat numbers fall", ["bat"]), ("hawks eat bats", ["hawk.*bat|eat bat|prey"]), ("less food for hawks so they decrease", ["less food|fewer|decrease|fall"])],
     "Bats feed on banyan fruit, so without the trees bat numbers fall. Hawks eat bats, so they have less food and their numbers fall too.")
u.nm("a", "Plankton contain 0.02 units of mercury. Small fish have 50 times more. How much mercury do small fish contain?", 1, "units", o="O4")
u.mc("a", "Why can a pesticide that is harmless in small amounts kill top predators?", "It bioaccumulates and biomagnifies, so predators receive a very large dose.", ["Predators are smaller.", "It changes into a different chemical.", "Predators drink it directly."], o="O4", skill="Reasoning")
u.mc("a", "Which action would best help fish populations recover?", "Fishing limits and protected areas where fishing is banned", ["Scooping up the ocean floor", "Adding invasive predators", "Building more dams"], skill="Reasoning")
u.stop("thousands of species", "Cutting down forests is called…", "deforestation", ["fragmentation", "pollution", "biomagnification"])
u.stop("A non-native species that causes this much harm is called invasive", "The Nile perch in Lake Victoria is an example of…", "an invasive species", ["a native species", "a producer", "a pollutant gas"])
u.stop("make acid rain, which harms plants and animals", "Acid rain forms from…", "sulfur dioxide and nitrogen oxides", ["oxygen and nitrogen", "methane and water", "plastic and oil"], o="O4")
u.stop("can get mercury poisoning", "Mercury gets more concentrated along a food chain. This is…", "biomagnification", ["photosynthesis", "an algal bloom", "deforestation"], o="O4")

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Ecosystems", "sec": None, "kids": [
    {"id": "lv", "t": "Levels", "d": "Population – one species • Community – all species • Ecosystem – plus non-living factors", "obj": "O1", "sec": "3.1"},
    {"id": "ty", "t": "Types of ecosystem", "d": "Forest • Grassland • Desert • Freshwater • Ocean", "obj": "O1", "sec": "3.1"},
    {"id": "ad", "t": "Adaptations", "d": "Physical – blubber, tail • Behavioural – pods, treetops", "obj": "O2", "sec": "3.1"},
    {"id": "sb", "t": "Seed banks", "d": "Dark, dry, −20 °C • Protect biodiversity • Svalbard vault", "obj": "O2", "sec": "3.1"},
    {"id": "hd", "t": "Habitat loss", "d": "Deforestation • Fragmentation • Carbon sinks lost", "obj": "O3", "sec": "3.2"},
    {"id": "inv", "t": "Overexploitation and invasive species", "d": "Overfishing • Nile perch • Asian hornets • Wolves re-introduced", "obj": "O3", "sec": "3.2"},
    {"id": "pol", "t": "Pollution", "d": "Land – litter • Air – acid rain • Water – algal blooms, oil, plastics", "obj": "O4", "sec": "3.2"},
    {"id": "bio", "t": "Bioaccumulation", "d": "Mercury builds up • Increases along food chain (biomagnification)", "obj": "O4", "sec": "3.2"},
]}
