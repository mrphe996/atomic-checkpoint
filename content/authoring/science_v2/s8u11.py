from science_v2.k import Unit
U = Unit("s8u11")

U.q("P", "11.1", "O1", "Two magnets are placed with their north poles facing. What happens?", ("They repel", "Like poles repel."), [("They attract", "Opposite poles attract."), ("Nothing", "Magnets exert forces on each other.")])
U.q("F", "11.2", "O2", "To test whether more coils make an electromagnet stronger, what should stay the same?", ("The current and the type of core", "Only the number of coils changes."), [("The number of coils", "That is what you change."), ("The number of paper clips picked up", "That is what you measure.")])
U.q("R", "11.3", "O3", "Why is an electromagnet used in a scrapyard crane instead of a permanent magnet?", ("It can be switched off to drop the metal", "The magnetism stops when the current stops."), [("It is weaker", "It can be very strong."), ("It attracts all metals", "It attracts only magnetic metals such as iron.")])
U.asn("11.3", "O3", "Is each statement always, sometimes or never true?", [("A metal is magnetic", "Sometimes true"), ("An electromagnet works with no current", "Never true"), ("A magnet has two poles", "Always true")], "Only some metals (iron, nickel, cobalt) are magnetic; an electromagnet needs current; every magnet has a north and a south pole.")
V2 = U.V2
