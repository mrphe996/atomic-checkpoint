from science_v2.k import Unit
U = Unit("s9u06")

U.q("R", "6.1", "O1", "In the word equation magnesium + oxygen → magnesium oxide, what are the reactants?", ("Magnesium and oxygen", "Reactants are on the left."), [("Magnesium oxide", "That is the product."), ("Oxygen only", "Both substances on the left react.")])
U.q("P", "6.2", "O2", "An iron nail is put in copper sulfate solution. What happens?", ("Copper forms on the nail and the blue colour fades", "Iron is more reactive and displaces copper."), [("Nothing", "Iron is more reactive than copper."), ("Iron forms in the solution", "Iron goes into solution as iron sulfate.")])
U.q("P", "6.2", "O3", "Copper is put in zinc sulfate solution. What happens?", ("No reaction", "Copper is less reactive than zinc, so it cannot displace it."), [("Zinc forms on the copper", "Copper cannot displace zinc."), ("The copper dissolves", "No displacement happens.")])
V2 = U.V2
