from science_v2.k import Unit
U = Unit("s7u13")

U.q("R", "13.1", "O1", "Which layer of the Earth is the thinnest?", ("The crust", "It is only a few kilometres to tens of kilometres thick."), [("The mantle", "The mantle is about 2900 km thick."), ("The core", "The core is thousands of kilometres across.")])
U.q("E", "13.2", "O2", "Earthquakes happen far more often in Japan than in the middle of Australia. Why?", ("Japan is near the boundary of tectonic plates", "Most earthquakes happen where plates meet."), [("Japan is an island", "Being an island is not the cause."), ("Australia has no rocks", "Australia is in the middle of a plate.")])
U.q("R", "13.3", "O3", "Which gas makes up most of the air?", ("Nitrogen (about 78%)", "Oxygen is about 21%."), [("Oxygen", "Oxygen is only about 21%."), ("Carbon dioxide", "It is about 0.04%.")])
U.q("P", "13.4", "O4", "A puddle disappears on a sunny day. Where does the water go?", ("It evaporates into water vapour in the air", "That is part of the water cycle."), [("It is destroyed by the Sun", "Matter is not destroyed."), ("It all soaks into the ground", "Most evaporates on a hot day.")])
V2 = U.V2
