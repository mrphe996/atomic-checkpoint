from science_v2.k import Unit
U = Unit("s9u01")

U.q("P", "1.1", "O1", "A plant is kept in the dark for two days and then a leaf is tested with iodine. What is expected?", ("No starch: the iodine stays orange-brown", "Without light there is no photosynthesis, and stored starch is used up."), [("Blue-black: lots of starch", "Starch is not made in the dark."), ("The leaf turns red", "Iodine does not turn red.")])
U.q("F", "1.1", "O2", "To show that light is needed for photosynthesis, which leaves should be compared?", ("Leaves from the same plant, one covered and one in light", "Only light should differ."), [("A leaf from a plant in the dark and a leaf from a different kind of plant", "Two things would differ."), ("Two leaves both in the light", "There is no comparison of light.")])
U.q("R", "1.2", "O3", "Why do root hair cells absorb water quickly?", ("They have a large surface area in contact with soil", "More surface allows faster absorption."), [("They contain chloroplasts", "Root cells have no chloroplasts."), ("They are dead cells", "They are living cells.")])
U.q("P", "1.2", "O4", "A celery stalk is put in red-dyed water. After some hours, where is the dye seen?", ("In the xylem tubes running up the stalk", "Xylem carries water up the plant."), [("Only in the leaves' edges", "The dye travels through the stalk first."), ("Nowhere", "Water and dye are taken up.")])
V2 = U.V2
