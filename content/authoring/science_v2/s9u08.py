from science_v2.k import Unit
U = Unit("s9u08")

U.q("R", "8.1", "O1", "What must happen for particles to react?", ("They must collide with enough energy", "That is collision theory."), [("They must stay still", "Particles must move to collide."), ("They must be the same colour", "Colour is not relevant.")])
U.q("R", "8.2", "O2", "On a graph of gas volume against time, where is the reaction fastest?", ("At the start, where the line is steepest", "Steeper means faster."), [("At the end, where the line is flat", "Flat means the reaction has stopped."), ("It is the same all the way", "The rate slows as reactants are used up.")])
U.q("F", "8.2", "O3", "Which measurement can follow the rate of a reaction that gives off a gas?", ("The volume of gas collected every 10 seconds", "This tracks progress over time."), [("The colour of the flask once", "One reading cannot show a rate."), ("The starting temperature only", "That does not track progress.")])
U.q("P", "8.3", "O4", "A marble chip is crushed into powder before adding acid. What happens to the rate?", ("It increases", "Powder has a larger surface area for collisions."), [("It decreases", "Smaller pieces react faster."), ("No change", "Surface area affects the rate.")])
U.asn("8.3", "O4", "Is each statement always, sometimes or never true?", [("Raising the temperature speeds up a reaction", "Always true"), ("A catalyst is used up in a reaction", "Never true"), ("Doubling the concentration doubles the rate", "Sometimes true")], "Higher temperature always increases the rate; a catalyst is not used up; the rate rises with concentration, but not always in exact proportion.")
V2 = U.V2
