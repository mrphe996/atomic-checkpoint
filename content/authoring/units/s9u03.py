# -*- coding: utf-8 -*-
"""Stage 9 Unit 3 – Variation and Inheritance. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Biology"
BLURB = "Chromosomes, genes and DNA, how sex is inherited, how a fetus develops, inherited and environmental variation, natural selection and what changes population size."
OBJECTIVES = {
    "O1": {"sec": "3.1", "code": "9Bs.03, 9SIC.01", "codeNote": "", "t": "Describe chromosomes, genes and DNA and how scientists worked out DNA's structure."},
    "O2": {"sec": "3.2", "code": "9Bp.01, 9Bp.02", "codeNote": "", "t": "Describe fertilisation and explain how sex is determined by X and Y chromosomes."},
    "O3": {"sec": "3.2", "code": "9Bp.08", "codeNote": "", "t": "Describe how a fetus develops and how the mother's health affects it."},
    "O4": {"sec": "3.3", "code": "9Bp.03", "codeNote": "", "t": "Distinguish inherited from environmental variation."},
    "O5": {"sec": "3.4", "code": "9Bp.04", "codeNote": "", "t": "Explain natural selection, including antibiotic and insecticide resistance."},
    "O6": {"sec": "3.5", "code": "9Be.01", "codeNote": "", "t": "Describe how environmental changes, including human activity, affect populations and can cause extinction."},
}
SECTIONS = [
    {"id": "3.1", "title": "Chromosomes, genes and DNA", "objs": ["O1"]},
    {"id": "3.2", "title": "Inheritance and fetal development", "objs": ["O2", "O3"]},
    {"id": "3.3", "title": "What is variation?", "objs": ["O4"]},
    {"id": "3.4", "title": "Natural selection", "objs": ["O5"]},
    {"id": "3.5", "title": "Populations and environment", "objs": ["O6"]},
]
u = Unit(9, 3)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 3.1
u.sec("3.1", "O1")
u.od("r", "Order from largest to smallest.", ["Cell", "Nucleus", "Chromosome", "Gene"])
u.tb("r", "Chromosome numbers. Complete the table.", ["Organism", "Pairs", "Total chromosomes"], [["Human", "23", B(46)], ["Fruit fly", "4", B(8)]])
u.gd("r", "Who made each discovery?", "Scientist(s)", [("Found 'nuclein' in 1869", "Miescher"), ("Discovered the double helix in 1953", "Watson and Crick"), ("Took X-ray images of DNA", "Franklin")], extra=["Darwin"])
u.ex("r", "Explain how Watson and Crick's discovery shows that science builds on the work of others.", [("used Franklin's X-ray images", ["franklin|x-ray"]), ("used earlier findings about DNA", ["earlier|miescher|avery|levene|before"])],
     "Watson and Crick's double helix model relied on Rosalind Franklin's X-ray images and on earlier work showing DNA carries hereditary information.")
u.mc("r", "Chromosomes are found in the…", "nucleus", ["cell membrane", "cytoplasm only", "cell wall"])
u.mc("r", "A gene is…", "a section of DNA that controls a characteristic", ["a whole chromosome", "a type of cell", "a protein in the blood"])
u.mc("r", "The shape of a DNA molecule is a…", "double helix", ["single straight strand", "circle", "cube"], d="H")
u.mc("r", "What did Avery, MacLeod and McCarty show in 1944?", "DNA, not protein, carries hereditary information", ["DNA is a double helix", "Humans have 46 chromosomes", "Genes cause cystic fibrosis"], d="VH")
mcs("p", [
    ("Humans have … pairs of chromosomes.", "23", ["46", "74", "8"]),
    ("Camels have … chromosomes.", "74", ["46", "8", "23"]),
    ("One pair of human chromosomes are the…", "sex chromosomes", ["DNA chromosomes", "blood chromosomes", "gene chromosomes"]),
    ("A characteristic such as eye colour is also called a…", "trait", ["gene", "nucleus", "helix"]),
    ("Genes can have different…", "forms", ["nuclei", "cells", "colours of DNA"]),
    ("Chromosomes are made of DNA and…", "proteins", ["fats", "starch", "water only"]),
    ("When cells divide, chromosomes are…", "copied", ["destroyed", "halved and lost", "turned into protein"]),
    ("Each chromosome carries…", "hundreds or thousands of genes", ["one gene only", "no genes", "one cell"]),
    ("Albrecht Kossel named…", "DNA and RNA", ["the double helix", "genes", "chromosomes"]),
    ("Phoebus Levene discovered…", "DNA's building blocks", ["the nucleus", "evolution", "X-rays"]),
    ("The Human Genome Project was completed in…", "2003", ["1869", "1953", "1944"]),
    ("The Human Genome Project mapped…", "all human genes", ["all animal cells", "the brain", "the Moon"]),
    ("Knowing genes helps scientists find the causes of disorders such as…", "cystic fibrosis", ["a broken leg", "a cold", "sunburn"]),
    ("Genetic information controls…", "the cell", ["the weather", "the Sun", "the soil"]),
    ("DNA's two strands are twisted like a…", "ladder", ["ball", "flat sheet", "single thread"]),
])
u.mt("p", "Match the term to its meaning.", [("Chromosome", "long thread of DNA and protein"), ("Gene", "section of DNA for one trait"), ("DNA", "molecule carrying genetic information")])
u.od("p", "Order the discoveries in time.", ["Miescher finds nuclein", "Avery shows DNA carries hereditary information", "Watson and Crick find the double helix", "Human Genome Project completed"])
u.ms("p", "Select ALL the true statements.", ["Chromosomes are in the nucleus", "Genes are sections of DNA", "Humans have 46 chromosomes"], ["Every species has 46 chromosomes", "DNA is a single strand"])
u.ex("a", "Explain why every new cell made by cell division needs a copy of every chromosome.", [("chromosomes carry genes / instructions", ["gene|instruction|information"]), ("cell needs full set to work / be controlled", ["control|work|function|complete"])],
     "Chromosomes carry the genes that control the cell. Each new cell needs a complete set of instructions to work properly, so the chromosomes are copied before division.")
u.mc("a", "Why did it take almost 100 years from finding DNA to understanding its structure?", "New techniques, such as X-ray imaging, and evidence from many scientists were needed", ["Nobody studied DNA", "DNA only appeared in 1953", "Chromosomes were not in cells before"], skill="Reasoning")
u.mc("a", "Why is it useful to know which gene is linked to a disorder?", "It helps diagnose, predict and develop treatments", ["It changes the person's blood group", "It stops cell division", "It removes chromosomes"], skill="Reasoning")
u.mc("a", "A species has 39 pairs of chromosomes. How many chromosomes are in each body cell?", "78", ["39", "19.5", "156"], skill="Application")
u.stop("Camels have 74, and fruit flies just 8!", "Humans have … chromosomes in each body cell.", "46", ["23", "74", "8"])
u.stop("another short fur", "A gene is a section of…", "DNA", ["protein", "a cell wall", "a nucleus membrane"])
u.stop("discovered the double helix structure", "Which scientists discovered the double helix?", "Watson and Crick", ["Miescher", "Darwin", "Levene"])

# ---------------------------------------------------------------- 3.2
u.sec("3.2", "O2")
u.gd("r", "XX or XY?", "Chromosomes", [("Female", "XX"), ("Male", "XY")], extra=["YY"])
u.tb("r", "Number of chromosomes. Complete the table.", ["Cell", "Chromosomes"], [["Sperm", "23"], ["Egg", B(23)], ["Zygote", B(46)]])
u.od("r", "Order the stages of development.", ["Fertilisation", "Zygote", "Ball of cells implants", "Embryo", "Fetus"], o="O3")
u.ex("r", "Explain why the father's sperm decides the sex of a baby.", [("every egg carries an X", ["egg.*x|x.*egg"]), ("sperm carries X or Y", ["sperm.*(x or y|y)|x or y"]), ("X → girl XX, Y → boy XY", ["girl|boy|xx|xy"])],
     "Every egg carries an X chromosome, but a sperm can carry an X or a Y. An X sperm gives XX, a girl; a Y sperm gives XY, a boy.")
u.mc("r", "At fertilisation…", "the nuclei of a sperm and an egg fuse", ["two eggs join", "a sperm divides", "an embryo becomes a fetus"])
u.mc("r", "The placenta…", "passes oxygen and nutrients to the fetus and removes wastes", ["makes eggs", "stores urine", "fights all infections alone"], o="O3")
u.mc("r", "Identical twins form when…", "one zygote splits into two", ["two eggs are fertilised", "two sperm fertilise one egg", "the placenta divides"], o="O3", d="H")
u.mc("r", "Why is the first few weeks of pregnancy especially important for avoiding alcohol and smoking?", "The fetus's organs are forming then", ["The fetus is largest then", "The placenta stops working", "The fetus cannot move"], o="O3", d="VH")
mcs("p", [
    ("Inheritance is…", "passing traits from parents to offspring", ["growth of a fetus", "variation caused by soil", "a type of excretion"]),
    ("Sex cells are also called…", "gametes", ["zygotes", "embryos", "fetuses"]),
    ("A fertilised egg is a…", "zygote", ["gamete", "placenta", "chromosome"]),
    ("Every egg cell carries a … chromosome.", "X", ["Y", "Z", "XY"]),
    ("The chance of a baby being a girl is about…", "50%", ["25%", "75%", "100%"]),
    ("Each zygote has … combination of DNA.", "a unique", ["the same", "no", "the mother's only"]),
    ("A developing baby is called an embryo until about…", "nine weeks", ["nine months", "two days", "40 weeks"], "O3"),
    ("Pregnancy lasts about…", "40 weeks", ["9 weeks", "20 weeks", "60 weeks"], "O3"),
    ("The fetus grows in the…", "uterus", ["bladder", "stomach", "ovary"], "O3"),
    ("The umbilical cord connects the fetus to the…", "placenta", ["bladder", "ovary", "amnion only"], "O3"),
    ("Amniotic fluid…", "cushions the fetus", ["feeds the mother", "makes sperm", "carries urine to the bladder"], "O3"),
    ("Antibodies passed across the placenta help the baby…", "fight infections", ["grow hair", "breathe air", "digest milk"], "O3"),
    ("Folic acid, iron and calcium are important in the mother's…", "diet", ["breath", "urine", "sweat"], "O3"),
    ("Non-identical twins come from…", "two separate eggs", ["one zygote splitting", "one sperm", "one egg and no sperm"], "O3"),
    ("Smoking in pregnancy can cause…", "low birth weight", ["taller babies", "more chromosomes", "identical twins"], "O3"),
])
u.ms("p", "Select ALL the things that cross the placenta to the fetus.", ["Oxygen", "Nutrients", "Antibodies"], ["Urine", "Whole red blood cells of the father"], o="O3")
u.mt("p", "Match the structure to its job.", [("Placenta", "exchanges substances with the mother's blood"), ("Umbilical cord", "connects fetus to placenta"), ("Amnion", "bag of fluid cushioning the fetus")], o="O3")
u.gd("p", "Which twins?", "Type", [("From one zygote that splits", "Identical"), ("From two eggs", "Non-identical")])
u.ex("a", "Explain why sperm and egg cells contain only 23 chromosomes.", [("fuse at fertilisation", ["fuse|fertilis|join"]), ("zygote gets 46 / full set", ["46|full|complete"]), ("half from each parent", ["half|each parent"])],
     "When a sperm and egg fuse at fertilisation, the zygote gets 23 from each parent, making the full set of 46. If gametes had 46, the number would double every generation.")
u.ex("a", "Explain how alcohol drunk by a pregnant mother can harm the fetus.", [("alcohol crosses the placenta", ["placenta|cross"]), ("enters fetus's blood", ["blood|fetus"]), ("damages developing organs / birth defects", ["organ|defect|damage|harm"])],
     "Alcohol crosses the placenta into the fetus's blood and can damage developing organs, causing birth defects or low birth weight.", o="O3")
u.mc("a", "A couple already have three boys. What is the chance their next baby is a girl?", "About 50%", ["0%", "100%", "25%"], skill="Reasoning")
u.mc("a", "Why do identical twins have exactly the same DNA?", "They come from the same zygote", ["They have the same birthday", "They share a placenta only", "They eat the same food"], o="O3", skill="Reasoning")
u.stop("a unique combination of DNA", "How many chromosomes are in a human egg cell?", "23", ["46", "92", "12"])
u.stop("about fifty-fifty", "The sex chromosomes of a male are…", "XY", ["XX", "YY", "XZ"])
u.stop("the amnion and its fluid cushion the fetus", "The placenta passes … to the fetus.", "oxygen and nutrients", ["urine", "carbon dioxide only", "chromosomes"], o="O3")

# ---------------------------------------------------------------- 3.3
u.sec("3.3", "O4")
u.gd("r", "Inherited or environmental variation?", "Type", [("Blood group", "Inherited"), ("Eye colour", "Inherited"), ("Large muscles from exercise", "Environmental"), ("Darker skin from sunshine", "Environmental")])
u.gd("r", "Hydrangea flower colour in different soils.", "Colour", [("Acidic soil", "Blue"), ("Alkaline soil", "Pink")], extra=["White"])
u.tb("r", "Heights of three pupils. Complete the table.", ["Pupil", "Height (cm)", "Difference from tallest (cm)"], [["A", "162", "0"], ["B", "155", B(7)], ["C", "149", B(13)]])
u.ex("r", "Explain why siblings with the same parents look different.", [("each gamete carries a different half of DNA", ["different|half|each gamete|each sperm|each egg"]), ("new combination at fertilisation", ["combination|mix"])],
     "Each sperm and egg carries a different half set of the parents' DNA, so each fertilised egg gets a new combination of genes.")
u.mc("r", "Variation is…", "the differences between members of the same species", ["the differences between species", "a change in the weather", "a type of chromosome"])
u.mc("r", "Inherited variation is caused by…", "differences in DNA", ["diet", "climate", "exercise"])
u.mc("r", "Which variation cannot be seen?", "Blood group", ["Height", "Eye colour", "Earlobe shape"], d="H")
u.mc("r", "Two identical twins grow up in different countries. One is much taller. The best explanation is…", "environmental variation, such as diet", ["different DNA", "different sex chromosomes", "inherited variation only"], d="VH")
mcs("p", [
    ("Individuals of a species share…", "almost the same DNA", ["completely different DNA", "no DNA", "the same height"]),
    ("Variation caused by climate, nutrition or soil is…", "environmental", ["inherited", "genetic", "chromosomal"]),
    ("Natural eye colour is…", "inherited", ["environmental", "caused by diet", "caused by exercise"]),
    ("Exercise building muscles is…", "environmental variation", ["inherited variation", "a gene", "fertilisation"]),
    ("Earlobe shape is…", "inherited", ["caused by sunshine", "caused by soil", "caused by exercise"]),
    ("Hydrangeas in acidic soil are…", "blue", ["pink", "white", "yellow"]),
    ("Crops grown with more fertiliser grow taller. This is…", "environmental variation", ["inherited variation", "natural selection", "extinction"]),
    ("A scar is an example of…", "environmental variation", ["inherited variation", "a gene", "a chromosome"]),
    ("Natural hair colour is mainly…", "inherited", ["environmental", "from exercise", "from soil"]),
    ("A suntan is…", "environmental", ["inherited", "a chromosome", "a gamete"]),
    ("Without identical twins, everyone in a class…", "looks different", ["looks the same", "has the same DNA", "has the same blood group"]),
    ("Each gamete carries…", "half a set of DNA", ["a full set of DNA", "no DNA", "two sets of DNA"]),
    ("Height is affected by…", "both genes and the environment", ["only genes", "only soil", "only blood group"]),
    ("Language spoken is…", "environmental", ["inherited", "in the DNA", "a sex chromosome"]),
    ("Blood group is controlled by…", "genes", ["diet", "exercise", "climate"]),
])
u.ms("p", "Select ALL the examples of inherited variation.", ["Blood group", "Natural eye colour", "Earlobe shape"], ["Tattoo", "Muscle from training"])
u.mt("p", "Match the cause to the variation.", [("Sunshine", "darker skin"), ("Exercise", "bigger muscles"), ("Soil pH", "hydrangea colour")])
u.od("p", "Order to show how inherited variation arises.", ["Parents make gametes with different half sets of DNA", "Fertilisation combines two gametes", "Zygote has a new combination of DNA", "Offspring differs from siblings"])
u.ex("a", "Plan an investigation to show that soil pH affects hydrangea flower colour.", [("same type of plant / cuttings from one plant", ["same|cutting|identical"]), ("grow in soils of different pH", ["acid|alkal|ph|different soil"]), ("keep other conditions same, record colour", ["same light|water|control|record|colour"])],
     "Take cuttings from one hydrangea so they have the same genes. Grow them in acidic and alkaline soil, keep light and water the same, and record the flower colour.")
u.mc("a", "Why are identical twins useful for studying environmental variation?", "They have the same DNA, so differences must be environmental", ["They always live apart", "They have no DNA", "They never vary"], skill="Enquiry")
u.mc("a", "A plant's leaf size varies a lot within one field. What would show that the cause is environmental?", "Cuttings of the same plant grown in different conditions develop different leaf sizes", ["All leaves are green", "The plants have chromosomes", "Leaves fall in autumn"], skill="Enquiry")
u.mc("a", "Why does sexual reproduction produce more variation than cell division?", "It combines DNA from two parents in new ways", ["It copies DNA exactly", "It uses no DNA", "It only uses the mother's DNA"], skill="Reasoning")
u.stop("can't even be seen", "Differences between members of the same species are called…", "variation", ["fertilisation", "excretion", "extinction"])
u.stop("That's inherited variation", "Inherited variation is caused by differences in…", "DNA", ["diet", "soil", "climate"])
u.stop("That's environmental variation", "Hydrangea colour depending on soil is…", "environmental variation", ["inherited variation", "a sex chromosome", "fertilisation"])

# ---------------------------------------------------------------- 3.4
u.sec("3.4", "O5")
u.od("r", "Order the steps of natural selection.", ["Individuals vary", "Some variations help survival", "Survivors breed", "They pass on the useful variation", "Over generations it becomes common"])
u.gd("r", "Mice in a dark forest hunted by owls. Which colour is favoured?", "Result", [("Light grey mice", "Eaten more"), ("Dark grey mice", "Survive more")], extra=["No change"])
u.tb("r", "Percentage of dark mice over generations. Complete the change.", ["Generation", "Dark mice (%)"], [["1", "50"], ["10", "80"], ["Change from 1 to 10", B(30)]])
u.ex("r", "Explain how bacteria can become resistant to an antibiotic.", [("some bacteria have a resistant variation", ["variation|resist|mutation|gene"]), ("antibiotic kills the rest", ["kill|die"]), ("resistant ones multiply / pass it on", ["multipl|breed|reproduc|pass"])],
     "One bacterium may carry a variation that resists the antibiotic. The antibiotic kills the others, and the resistant one multiplies, passing on the resistance.")
u.mc("r", "Natural selection means…", "individuals best suited to the environment survive and breed", ["all individuals survive", "humans choose which animals breed", "animals choose to change"])
u.mc("r", "Darwin based his theory partly on…", "Galápagos finches", ["fruit flies", "camels", "hydrangeas"])
u.mc("r", "Why can natural selection be fast in bacteria?", "They reproduce very quickly", ["They are very large", "They have no DNA", "They live for many years"], d="H")
u.mc("r", "Why have insecticide-treated bed nets become less effective?", "Resistant mosquitoes survived and bred", ["Mosquitoes learned to avoid nets", "The nets wore out only", "Malaria disappeared"], d="VH")
mcs("p", [
    ("More offspring are born than…", "can survive", ["are needed for variation", "have DNA", "can grow"]),
    ("A variation that helps survival is called…", "favourable", ["harmful", "neutral always", "environmental only"]),
    ("Over a long time, natural selection can produce…", "new species", ["the same species forever", "no change", "extinct DNA"]),
    ("Finches' beaks were suited to…", "different foods", ["different weather only", "flying faster", "laying eggs"]),
    ("In the mouse example, owls spot … mice more easily.", "light grey", ["dark grey", "all", "no"]),
    ("'Super bugs' are…", "bacteria resistant to antibiotics", ["very large insects", "mosquitoes with nets", "viruses only"]),
    ("Antibiotics kill…", "bacteria", ["viruses", "mosquitoes", "plants"]),
    ("Mosquitoes spread…", "malaria", ["cystic fibrosis", "rinderpest", "scurvy"]),
    ("Survivors pass on their useful variations through their…", "genes", ["diet", "habitat", "skills"]),
    ("Insecticide resistance arises because a few insects…", "have genes to resist it", ["learn to resist it", "eat the insecticide", "avoid all nets"]),
    ("Because of resistance, scientists must develop…", "new insecticides and antibiotics", ["fewer nets", "more mosquitoes", "new chromosomes"]),
    ("The theory of natural selection was put forward by…", "Charles Darwin", ["Rosalind Franklin", "Friedrich Miescher", "James Watson"]),
    ("Natural selection acts on…", "variation", ["identical individuals", "rocks", "weather"]),
    ("Taking the full course of antibiotics helps…", "reduce the chance of resistant bacteria surviving", ["make bacteria grow", "cause malaria", "make mosquitoes resistant"]),
    ("If the environment changes, the favourable variation may…", "change too", ["always stay the same", "disappear from DNA", "never matter"]),
])
u.ms("p", "Select ALL the ideas in natural selection.", ["Individuals vary", "More are born than survive", "The best-suited survive and breed"], ["Animals choose to change their genes", "All offspring survive"])
u.mt("p", "Match the example to the selecting factor.", [("Dark mice survive", "owls hunting"), ("Resistant bacteria survive", "antibiotics"), ("Resistant mosquitoes survive", "insecticides")])
u.gd("p", "True or false?", "Answer", [("Natural selection needs variation", "True"), ("Individuals change their own genes to survive", "False"), ("Resistance can spread over generations", "True")])
u.ex("a", "Peppered moths were mostly pale. After factories blackened tree trunks with soot, dark moths became common. Explain this using natural selection.", [("dark moths camouflaged on dark trunks", ["camoufl|hidden|harder to see"]), ("pale moths eaten by birds more", ["eaten|bird|predator"]), ("dark moths survived and bred, passing on genes", ["surviv|breed|pass|gene"])],
     "On sooty trunks, dark moths were camouflaged while pale moths were easily seen and eaten by birds. More dark moths survived and bred, passing on the dark colour.")
u.gr("a", "Percentage of bacteria resistant to an antibiotic. Plot the points.", {"label": "Year", "min": 0, "max": 20, "step": 5}, {"label": "Resistant (%)", "min": 0, "max": 60, "step": 10}, [[0, 2], [5, 8], [10, 20], [15, 35], [20, 52]])
u.mc("a", "What does the resistance graph suggest about using this antibiotic?", "It is becoming less effective, so new antibiotics are needed", ["It is getting more effective", "Resistance is falling", "Bacteria are dying out"], skill="Data")
u.mc("a", "Why is it wrong to say 'the mice turned dark to hide from owls'?", "Individuals don't choose; the dark ones already varied and survived to breed", ["Mice can change colour at will", "Owls made the mice dark", "Mice are not affected by owls"], skill="Reasoning")
u.stop("This is natural selection", "In the mouse example, which mice survive more?", "Dark grey mice", ["Light grey mice", "All mice", "No mice"])
u.stop("new species can form", "Darwin's theory was based partly on…", "Galápagos finches", ["fruit flies", "camels", "bed nets"])
u.stop("into 'super bugs'", "Bacteria resistant to antibiotics are called…", "super bugs", ["viruses", "gametes", "zygotes"])

# ---------------------------------------------------------------- 3.5
u.sec("3.5", "O6")
u.gd("r", "Natural or human cause of population change?", "Cause", [("Drought", "Natural"), ("Overfishing", "Human"), ("Deforestation", "Human"), ("Asteroid impact", "Natural")])
u.gr("r", "A deer population on an island. Plot the points.", {"label": "Year", "min": 0, "max": 8, "step": 2}, {"label": "Number of deer", "min": 0, "max": 500, "step": 100}, [[0, 50], [2, 200], [4, 400], [6, 420], [8, 410]])
u.mc("r", "The deer population levels off at about 410. This number is the habitat's…", "carrying capacity", ["extinction point", "birth rate", "variation"], skill="Data")
u.ex("r", "Explain why a population cannot keep growing for ever in a habitat.", [("limited food / water / shelter", ["food|water|shelter|resource"]), ("reaches carrying capacity", ["carrying capacity|maximum|largest"])],
     "A habitat has limited food, water and shelter, so the population grows until it reaches the carrying capacity, the largest number the habitat can support.")
u.mc("r", "A population is…", "a group of one species living in the same habitat", ["all the species in a habitat", "one animal", "a habitat with no animals"])
u.mc("r", "A species that has died out completely is…", "extinct", ["endangered", "resistant", "invasive"])
u.mc("r", "Which human activity removes animals faster than they can reproduce?", "Overfishing", ["Planting trees", "Recycling", "Building nature reserves"], d="H")
u.mc("r", "Why does coral bleaching reduce fish populations?", "It destroys the habitat that provides fish with food and shelter", ["It adds more food", "It makes fish resistant", "It increases carrying capacity"], d="VH")
mcs("p", [
    ("A population needs food, water and…", "shelter", ["insecticide", "antibiotics", "fertilisation"]),
    ("Rinderpest was a disease that killed many…", "African buffalo", ["mosquitoes", "finches", "hydrangeas"]),
    ("The dinosaurs were wiped out by…", "an asteroid impact", ["overfishing", "deforestation", "pollution from cars"]),
    ("Which is a weather hazard?", "Flood", ["Overhunting", "Deforestation", "Recycling"]),
    ("Deforestation destroys…", "habitats", ["asteroids", "chromosomes", "antibiotics"]),
    ("Pollution can poison…", "land, water and air", ["only rocks", "only the Sun", "nothing"]),
    ("The largest population a habitat can support is the…", "carrying capacity", ["birth rate", "food chain", "habitat size"]),
    ("Overhunting can lead to…", "extinction", ["more variation", "carrying capacity rising", "natural selection stopping"]),
    ("Which activity does the most damage to populations?", "Human activities", ["Asteroids", "Volcanoes only", "Rainbows"]),
    ("A disease spreading through a herd usually makes the population…", "fall", ["rise", "stay the same", "become extinct at once always"]),
    ("Fires and droughts are examples of…", "natural events that reduce populations", ["human farming", "variation", "inheritance"]),
    ("Overfishing affects…", "fish populations", ["bird beaks", "chromosomes", "the Sun"]),
    ("Protecting habitats helps…", "prevent extinction", ["cause disease", "reduce variation", "increase pollution"]),
    ("If food supply increases, the population usually…", "rises", ["falls", "becomes extinct", "stops breeding"]),
    ("Coral bleaching is caused mainly by…", "warming seas and pollution", ["more fish", "extra coral", "asteroids"]),
])
u.ms("p", "Select ALL the human activities that harm populations.", ["Deforestation", "Overhunting", "Pollution"], ["Creating nature reserves", "Breeding endangered animals"])
u.mt("p", "Match the term to its meaning.", [("Population", "one species in a habitat"), ("Carrying capacity", "largest population a habitat supports"), ("Extinct", "died out completely")])
u.od("p", "Order the effects of deforestation.", ["Trees are cut down", "Habitat is destroyed", "Animals lose food and shelter", "Population falls"])
u.ex("a", "Suggest two ways people can help prevent a species becoming extinct, and explain how each helps.", [("protect habitats / reserves", ["protect|reserve|habitat"]), ("limit hunting / fishing", ["hunt|fish|ban|limit"]), ("breeding programmes / reduce pollution", ["breed|captiv|pollution"])],
     "Protecting habitats in nature reserves keeps food and shelter available; limiting hunting and fishing lets numbers recover; breeding programmes increase numbers.")
u.nm("a", "A fish population of 12 000 falls by 25% because of overfishing. How many fish remain?", 9000, "fish")
u.mc("a", "Why are species with small populations more at risk of extinction from a disease?", "There is less variation, so fewer may resist it", ["Small populations have more DNA", "Diseases only affect large populations", "They breed faster"], skill="Reasoning")
u.mc("a", "Why might a population fall below its carrying capacity after a drought?", "Less water and food are available, so fewer survive", ["Droughts add more food", "Carrying capacity increases in drought", "Animals breed more in drought"], skill="Reasoning")
u.stop("it becomes extinct", "A group of one species living in the same habitat is a…", "population", ["community", "ecosystem", "gene"])
u.stop("can all cause huge drops", "Which caused the dinosaurs' extinction?", "An asteroid", ["Overfishing", "Deforestation", "Rinderpest"])
u.stop("pollution poisons land, water and air", "Overfishing removes fish faster than they can…", "reproduce", ["swim", "grow scales", "breathe"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Variation and inheritance", "sec": None, "kids": [
    {"id": "dna", "t": "DNA", "d": "Nucleus → chromosomes → genes • 46 in humans • Double helix", "obj": "O1", "sec": "3.1"},
    {"id": "inh", "t": "Inheritance", "d": "Gametes 23 • Zygote 46 • XX girl, XY boy", "obj": "O2", "sec": "3.2"},
    {"id": "fet", "t": "Fetus", "d": "Embryo → fetus • Placenta, cord, amnion • Mother's health", "obj": "O3", "sec": "3.2"},
    {"id": "var", "t": "Variation", "d": "Inherited: blood group, eye colour • Environmental: diet, soil, sun", "obj": "O4", "sec": "3.3"},
    {"id": "ns", "t": "Natural selection", "d": "Vary • Survive • Breed • Pass on • Resistance", "obj": "O5", "sec": "3.4"},
    {"id": "pop", "t": "Populations", "d": "Carrying capacity • Disease, disasters • Human activity • Extinction", "obj": "O6", "sec": "3.5"},
]}
