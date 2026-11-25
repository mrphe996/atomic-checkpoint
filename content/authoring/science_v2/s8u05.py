from science_v2.k import Unit
U = Unit("s8u05")

U.q("R", "5.1", "O1", "How can you tell pure water from salty water using melting or boiling points?", ("Pure water boils at exactly 100 °C; salty water boils at a higher temperature", "Impurities change boiling points."), [("They boil at the same temperature", "Salt raises the boiling point."), ("Salty water boils at a lower temperature", "It boils at a higher temperature.")])
U.q("E", "5.1", "O2", "Ava says air is a pure substance because it looks the same everywhere. Is she right?", ("No – air is a mixture of gases", "Air contains nitrogen, oxygen, argon and more."), [("Yes", "Looking the same does not make it pure."), ("No – air is a compound", "The gases are not chemically joined.")])
U.q("F", "5.2", "O3", "Which method shows how many dyes are in a black ink?", ("Chromatography", "The dyes travel different distances up the paper."), [("Filtration", "The dyes are dissolved and pass through a filter."), ("Distillation", "That separates a liquid from a solution.")])
U.q("P", "5.3", "O4", "More and more sugar is stirred into a cup of water at the same temperature. What happens eventually?", ("No more dissolves: the solution is saturated", "There is a limit to how much dissolves."), [("It keeps dissolving for ever", "Solubility has a limit."), ("The sugar turns into water", "Sugar does not become water.")])
U.asn("5.3", "O4", "Is each statement always, sometimes or never true?", [("A solid dissolves faster in hot water than in cold water", "Sometimes true"), ("When a solid dissolves, its mass is lost", "Never true"), ("A solution is a mixture", "Always true")], "Most solids dissolve faster when hot, but not all; dissolving conserves mass; a solution is a mixture of solute and solvent.")
V2 = U.V2
