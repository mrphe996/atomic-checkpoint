from science_v2.k import Unit
U = Unit("s8u03")

U.q("P", "3.1", "O1", "A pond's frogs all die out. What is likely to happen to the number of insects the frogs ate?", ("It increases", "Fewer predators means more prey survive."), [("It decreases", "The insects lost a predator."), ("It stays the same", "Changes spread through the ecosystem.")])
U.q("R", "3.1", "O2", "Which is a non-living (abiotic) part of an ecosystem?", ("Temperature", "Temperature is a physical factor."), [("Grass", "Grass is living."), ("Bacteria", "Bacteria are living.")])
U.q("E", "3.2", "O3", "A farmer says cutting down a forest only affects the trees. What is wrong?", ("Animals lose their habitat and food, so many populations fall", "Organisms in an ecosystem depend on each other."), [("Nothing", "Whole food webs are affected."), ("It only affects the soil", "Many living things are affected.")])
U.q("R", "3.2", "O4", "Which action helps protect an ecosystem?", ("Creating a nature reserve", "Reserves protect habitats."), [("Dumping waste in rivers", "Pollution harms ecosystems."), ("Bringing in a new predator", "Invasive species can harm native ones.")])
V2 = U.V2
