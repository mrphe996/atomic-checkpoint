from science_v2.k import Unit
U = Unit("s8u01")

U.q("P", "1.1", "O1", "Iodine solution is added to a piece of bread. What colour change is expected?", ("Orange-brown to blue-black", "Bread contains starch."), [("Blue to purple", "That is the biuret test for protein."), ("No change", "Bread contains plenty of starch.")])
U.q("R", "1.1", "O2", "Which nutrient is mainly needed for growth and repair of cells?", ("Protein", "Proteins build new cells."), [("Carbohydrate", "Carbohydrates mainly give energy."), ("Fibre", "Fibre helps food move through the gut.")])
U.q("E", "1.2", "O3", "Raj eats only rice and bread because they give energy. What is the problem?", ("He will lack protein, vitamins and minerals", "A balanced diet needs all the nutrient groups."), [("Nothing – energy is all you need", "The body also needs materials for growth and repair."), ("He will get too much protein", "Rice and bread are low in protein.")])
U.q("R", "1.2", "O3", "A cyclist training hard and an office worker are the same age. Who needs more energy from food each day?", ("The cyclist", "More activity uses more energy."), [("The office worker", "Sitting uses less energy."), ("They need exactly the same", "Energy needs depend on activity.")])
U.q("E", "1.3", "O4", "Lu says 'Fat is always bad for you.' Which is the best reply?", ("Some fat is needed for energy and warmth; too much is unhealthy", "Balance matters."), [("She is right", "The body needs some fat."), ("Fat is always good", "Too much fat can lead to heart disease.")])
U.q("P", "1.3", "O4", "What is a likely long-term effect of smoking on the lungs?", ("Damage to the alveoli, so less oxygen gets into the blood", "Smoking harms gas exchange."), [("Larger, healthier lungs", "Smoking damages the lungs."), ("No effect if you are young", "Damage builds up over time.")])
V2 = U.V2
