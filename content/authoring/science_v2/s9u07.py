from science_v2.k import Unit
U = Unit("s9u07")

U.q("R", "7.1", "O1", "Which salt forms when hydrochloric acid reacts with sodium hydroxide?", ("Sodium chloride", "Hydrochloric acid makes chlorides."), [("Sodium sulfate", "That comes from sulfuric acid."), ("Sodium nitrate", "That comes from nitric acid.")])
U.q("P", "7.1", "O2", "An acid reacts with a metal carbonate. Which gas is produced?", ("Carbon dioxide", "Acid + carbonate → salt + water + carbon dioxide."), [("Hydrogen", "Hydrogen comes from acid + metal."), ("Oxygen", "Oxygen is not produced.")])
U.q("F", "7.2", "O3", "Excess copper oxide is added to acid to make copper sulfate. How is the extra copper oxide removed?", ("Filtration", "Unreacted solid stays in the filter paper."), [("Evaporation", "That removes water."), ("Chromatography", "That separates dyes.")])
U.q("E", "7.2", "O4", "Ana boils a salt solution until completely dry and gets tiny, broken crystals. How can she get larger crystals?", ("Heat only until crystals start to form, then leave it to cool slowly", "Slow crystallisation gives bigger crystals."), [("Boil it harder", "That makes small crystals."), ("Add more acid", "That does not affect crystal size.")])
V2 = U.V2
