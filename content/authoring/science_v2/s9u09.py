from science_v2.k import Unit
U = Unit("s9u09")

U.q("R", "9.1", "O1", "A block has mass 200 g and volume 50 cm³. What is its density?", ("4 g/cm³", "Density = mass ÷ volume."), [("250 g/cm³", "That adds."), ("10 000 g/cm³", "That multiplies.")])
U.q("E", "9.1", "O2", "Tim says a big log must be denser than a small stone because it is heavier. What is wrong?", ("Density depends on mass per unit volume, not total mass", "The stone sinks; the log floats."), [("Nothing", "Heavier does not mean denser."), ("Density depends on colour", "It depends on mass and volume.")])
U.q("R", "9.2", "O3", "Why are gases much less dense than solids?", ("Their particles are far apart", "The same mass takes up much more space."), [("Gas particles are smaller", "Spacing matters, not size."), ("Gases have no mass", "Gases have mass.")])
U.q("P", "9.3", "O4", "An object has a density of 0.8 g/cm³. Will it float in water (1.0 g/cm³)?", ("Yes", "Objects less dense than water float."), [("No, it sinks", "It is less dense than water."), ("It is impossible to say", "Comparing densities answers it.")])
V2 = U.V2
