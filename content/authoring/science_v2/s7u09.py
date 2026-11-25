from science_v2.k import Unit
U = Unit("s7u09")

U.asn("9.1", "O1", "Is each change always, sometimes or never a chemical change?", [("Burning", "Always true"), ("Melting", "Never true"), ("A colour change", "Sometimes true")], "A chemical change makes a new substance. Burning always does; melting never does; a colour change can be a sign of a reaction, but not always (paint mixing is physical).")
U.q("P", "9.2", "O2", "A lit splint is held at the mouth of a test tube where hydrogen is made. What happens?", ("A squeaky pop", "Hydrogen burns with a squeaky pop."), [("The splint relights", "That is the test for oxygen."), ("Limewater goes cloudy", "That is the test for carbon dioxide.")])
U.q("R", "9.3", "O3", "Which reaction is harmful rather than useful?", ("Iron rusting on a bridge", "Rust weakens the structure."), [("Burning fuel to cook", "That is useful."), ("Baking a cake", "That is useful.")])
U.q("E", "9.4", "O4", "Bubbles form when two liquids are mixed. Ali says a chemical reaction must have happened. What should he check?", ("Whether a new substance (a gas) is made, or whether air was just trapped when stirring", "Bubbles can come from stirring air in."), [("Nothing – bubbles always mean a reaction", "Stirring can trap air bubbles."), ("Whether the liquids are the same colour", "Colour does not answer the question.")])
V2 = U.V2
