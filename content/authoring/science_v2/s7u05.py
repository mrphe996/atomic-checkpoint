from science_v2.k import Unit
U = Unit("s7u05")

U.q("P", "5.1", "O1", "A leaf is buried in dry sand and another in damp soil. Which decays faster?", ("The leaf in damp soil", "Decomposers need moisture and are common in soil."), [("The leaf in dry sand", "Decomposers grow slowly without water."), ("They decay at the same rate", "The conditions are different.")])
U.q("E", "5.1", "O2", "Ben says decomposers are harmful because they make things rot. Which is the best reply?", ("They recycle nutrients from dead material back into the soil for plants", "Without decomposers, nutrients would stay locked in dead matter."), [("He is right – they should be removed", "Removing them would stop the nutrient cycle."), ("Decomposers do not exist in soil", "Soil is full of bacteria and fungi.")])
U.q("P", "5.2", "O4", "In a food web, owls eat mice and mice eat seeds. A disease kills most of the owls. What happens to the seeds at first?", ("Fewer seeds, because there are more mice to eat them", "With fewer owls, mice increase and eat more seeds."), [("More seeds, because there are fewer owls", "Owls do not eat seeds."), ("No change", "A change in one population spreads through the web.")])
U.q("R", "5.2", "O3", "Why do food chains rarely have more than four or five links?", ("Energy is lost at each link, so little is left for top consumers", "Each level passes on only a small part of its energy."), [("Animals get bored of eating", "It is about energy, not behaviour."), ("There are not enough animal names", "The limit comes from energy loss.")])
V2 = U.V2
