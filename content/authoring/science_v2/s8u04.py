from science_v2.k import Unit
U = Unit("s8u04")

U.q("R", "4.1", "O1", "Which particle has a positive charge?", ("The proton", "Protons are positive."), [("The electron", "Electrons are negative."), ("The neutron", "Neutrons have no charge.")])
U.q("P", "4.1", "O3", "An atom has 6 protons. How many electrons does it have when it is neutral?", ("6", "A neutral atom has equal numbers of protons and electrons."), [("12", "That adds protons and electrons."), ("0", "Electrons balance the protons.")])
U.q("E", "4.2", "O4", "In Rutherford's experiment, most alpha particles went straight through gold foil. What did this show?", ("Most of an atom is empty space", "Only a few bounced back from the tiny nucleus."), [("Atoms are solid balls", "Then most particles would bounce back."), ("Gold is not made of atoms", "Gold is made of atoms.")])
U.q("R", "4.2", "O4", "Why was the plum pudding model replaced?", ("New experimental evidence did not fit it", "Scientific models change with evidence."), [("Scientists stopped liking puddings", "It changed because of evidence."), ("It was never used", "It was the accepted model for a while.")])
V2 = U.V2
