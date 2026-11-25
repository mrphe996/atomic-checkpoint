from science_v2.k import Unit
U = Unit("s9u14")

U.q("R", "14.1", "O1", "Which evidence supports the idea that a large asteroid hit Earth 66 million years ago?", ("A huge crater and a worldwide layer of rare metal (iridium) in rocks", "These are the key clues."), [("Dinosaurs are mentioned in old books", "No humans saw it."), ("The Moon has craters", "That is not evidence for this event.")])
U.q("E", "14.2", "O2", "Moon rocks are very similar to Earth's mantle. Which idea does this support?", ("The Moon formed from material thrown out when a large object hit Earth", "That is the collision theory."), [("The Moon was captured from far away", "Then its rocks would be very different."), ("The Moon is made of a different material altogether", "The rocks are similar.")])
U.q("R", "14.3", "O3", "What pulls the gas and dust in a nebula together to form a star?", ("Gravity", "Gravity makes the cloud collapse."), [("Magnetism", "Gravity is the main force."), ("Wind", "There is no wind in space.")])
V2 = U.V2
