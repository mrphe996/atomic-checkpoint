from science_v2.k import Unit
U = Unit("s9u10")

U.q("E", "10.1", "O1", "A bath and a cup of tea are both at 60 °C. Which contains more thermal energy?", ("The bath, because it has much more water", "Temperature is not the same as thermal energy."), [("The tea", "Same temperature, but much less water."), ("They are the same", "Same temperature, different amounts of energy.")])
U.q("R", "10.2", "O2", "A hot drink cools in a room. Where does its energy go?", ("Into the surroundings, warming them slightly", "Energy is conserved, not destroyed."), [("It disappears", "Energy cannot be destroyed."), ("It turns into cold", "Cold is not a form of energy.")])
U.q("R", "10.3", "O3", "Why do computers have cooling fans?", ("To remove wasted thermal energy so parts do not overheat", "Wasted energy heats the computer."), [("To make the computer faster", "The fan stops overheating."), ("To produce electricity", "Fans use electricity.")])
U.q("P", "10.4", "O4", "A metal spoon and a wooden spoon stand in hot soup. Which handle gets hot first?", ("The metal one", "Metals are good thermal conductors."), [("The wooden one", "Wood is an insulator."), ("Both at the same time", "The materials conduct differently.")])
U.q("R", "10.5", "O5", "Why does sweating cool you down?", ("Evaporating sweat takes energy from the skin", "The fastest particles escape, lowering the temperature."), [("Sweat is cold", "Sweat is at body temperature."), ("Sweat reflects sunlight", "It is evaporation that cools.")])
V2 = U.V2
