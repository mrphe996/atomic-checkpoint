from science_v2.k import Unit
U = Unit("s7u07")

U.q("F", "7.1", "O1", "To compare how strong three threads are, which test is fair?", ("Hang weights on threads of the same length and thickness until each breaks", "Only the material should change."), [("Use a different length for each thread", "Length would change the result too."), ("Pull each thread by hand and decide", "That is not a measurement.")])
U.q("R", "7.2", "O2", "Which of these is a CHEMICAL property?", ("Iron rusts in damp air", "Rusting forms a new substance."), [("Iron is shiny", "Appearance is a physical property."), ("Iron melts at 1538 °C", "Melting point is a physical property.")])
U.asn("7.3", "O3", "Is each statement about metals and non-metals always, sometimes or never true?", [("A metal conducts electricity", "Always true"), ("A metal is a solid at room temperature", "Sometimes true"), ("A non-metal is a good conductor of heat", "Sometimes true")], "All metals conduct electricity; mercury is a liquid metal; graphite (carbon) is a non-metal that conducts.")
U.q("R", "7.4", "O4", "Why is steel (an alloy of iron) used for bridges instead of pure iron?", ("The alloy is stronger and harder", "Different-sized atoms stop the layers sliding easily."), [("Steel is softer", "Alloys are usually harder."), ("Pure iron does not exist", "Pure iron exists but is too soft.")])
V2 = U.V2
