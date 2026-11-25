from science_v2.k import Unit
U = Unit("s8u14")

U.q("R", "14.1", "O1", "Which is largest?", ("A galaxy", "A galaxy contains billions of stars."), [("The Solar System", "It is one star system inside a galaxy."), ("The Sun", "The Sun is one star.")])
U.q("P", "14.2", "O2", "Which planets are rocky?", ("Mercury, Venus, Earth and Mars", "The inner planets are rocky."), [("Jupiter and Saturn", "They are gas giants."), ("Uranus and Neptune", "They are ice giants.")])
U.q("E", "14.2", "O3", "Ty says a planet must orbit our Sun. What is wrong?", ("Many planets (exoplanets) orbit other stars", "Planetary systems exist around other stars."), [("Nothing", "Exoplanets orbit other stars."), ("Planets orbit the Moon", "Planets orbit stars.")])
U.q("R", "14.3", "O4", "How does the Earth's magnetic field protect life?", ("It deflects harmful charged particles from the Sun", "That is why auroras form near the poles."), [("It keeps the air warm", "It does not heat the air."), ("It holds the Moon in orbit", "Gravity does that.")])
V2 = U.V2
