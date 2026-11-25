from science_v2.k import Unit
U = Unit("s7u14")

U.q("E", "14.1", "O1", "Ella says the Sun goes round the Earth because it rises in the east and sets in the west. What is the better explanation?", ("The Earth spins on its axis once a day", "The Sun only seems to move."), [("She is right", "The Earth orbits the Sun, and its spin makes day and night."), ("The Sun moves round the Earth once a year", "The Earth orbits the Sun once a year.")])
U.q("R", "14.2", "O2", "What mainly causes tides on Earth?", ("The Moon's gravity pulling on the oceans", "The Moon's pull raises bulges of water."), [("The wind", "Wind makes waves, not tides."), ("The Earth's magnetic field", "Magnetism does not move the sea.")])
U.q("P", "14.3", "O3", "During a solar eclipse, where is the Moon?", ("Between the Sun and the Earth", "The Moon blocks the Sun's light."), [("Behind the Earth", "That gives a lunar eclipse."), ("Beside the Sun", "It must be in line between them.")])
U.q("E", "14.4", "O4", "Why did scientists replace the model with the Earth at the centre of the Solar System?", ("New observations, such as Jupiter's moons, fitted the Sun-centred model better", "Models change with new evidence."), [("People simply changed their minds", "The change was driven by evidence."), ("The Earth moved", "The Earth was always orbiting the Sun.")])
V2 = U.V2
