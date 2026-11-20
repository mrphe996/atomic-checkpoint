# -*- coding: utf-8 -*-
"""Stage 8 Unit 11 – Magnetism. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Physics"
BLURB = "Magnets and magnetic materials, magnetic fields and Earth's field, making and strengthening electromagnets, and how electromagnets are used."
OBJECTIVES = {
    "O1": {"sec": "11.1", "code": "8Pe.01, 8ESp.01", "codeNote": "", "t": "Describe magnetic materials, magnetic fields and how fields interact, and explain Earth's magnetic field."},
    "O2": {"sec": "11.2", "code": "8Pe.02, 8Pe.03, 8TWSp.04", "codeNote": "", "t": "Describe how to make an electromagnet and investigate the factors that change its strength."},
    "O3": {"sec": "11.3", "code": "8Pe.02, 8SIC.02", "codeNote": "", "t": "Describe uses of electromagnets in homes, industry and medicine."},
}
SECTIONS = [
    {"id": "11.1", "title": "Magnetic fields", "objs": ["O1"]},
    {"id": "11.2", "title": "Electromagnets", "objs": ["O2"]},
    {"id": "11.3", "title": "Uses of electromagnets", "objs": ["O3"]},
]
u = Unit(8, 11)

# ---------------------------------------------------------------- 11.1
u.sec("11.1", "O1")
u.gd("r", "Magnetic or non-magnetic?", "Material", [("Iron", "Magnetic"), ("Copper", "Non-magnetic"), ("Nickel", "Magnetic"), ("Aluminium", "Non-magnetic")])
u.gd("r", "Attract or repel?", "Result", [("North and South", "Attract"), ("North and North", "Repel"), ("South and South", "Repel")])
u.mc("r", "A magnetic field is…", "the region around a magnet where its force acts", [("the North pole only", "No."), ("a type of metal", "No."), ("the iron filings", "They only show the field.")])
u.ex("r", "Explain what causes Earth's magnetic field.", [("moving molten metal in outer core", ["molten|liquid|outer core|moving metal"]), ("creates electric currents", ["current"]), ("currents produce the magnetic field", ["produce|make|field"])],
     "Molten metal moving in Earth's outer core creates electric currents, and these currents produce the magnetic field.")
u.mc("r", "Where is the magnetic field of a bar magnet strongest?", "At the poles, where the field lines are closest", [("In the middle", "No."), ("Far away from the magnet", "Weaker there."), ("Everywhere equally", "No.")], d="H")
u.mc("r", "A temporary magnet made of soft iron is magnetic…", "only while it is in a magnetic field", [("forever", "That is permanent."), ("only when hot", "No."), ("never", "No.")])
u.mc("r", "Field lines on a bar magnet go from…", "the North pole to the South pole", ["the South pole to the North pole", "the middle outwards", "nowhere"], d="H")
u.mc("r", "Why do maps show a difference between magnetic north and true north?", "Earth's magnetic poles are not quite at the geographic poles", [("Compasses are faulty", "No."), ("The Earth is flat", "No."), ("Magnetic north is in the south", "No.")], d="VH")
for p, r, w in [
    ("Every magnet has…", "a North pole and a South pole", ["only a North pole", "three poles", "no poles"]),
    ("Unlike poles…", "attract", ["repel", "do nothing", "melt"]),
    ("Like poles…", "repel", ["attract", "join", "vanish"]),
    ("Which is a magnetic material?", "Cobalt", ["Wood", "Plastic", "Glass"]),
    ("Steel is…", "magnetic", ["non-magnetic", "a gas", "an insulator only"]),
    ("Heating or hammering a permanent magnet can…", "destroy its magnetism", ["make it stronger", "turn it into copper", "nothing"]),
    ("Electromagnets can be…", "switched on and off", ["never switched off", "only permanent", "made of plastic"]),
    ("Iron filings around a magnet show…", "the field lines", ["the mass", "the temperature", "the colour"]),
    ("The field gets weaker…", "further from the magnet", ["nearer the poles", "inside the poles", "never"]),
    ("Magnetic force…", "acts at a distance", ["needs contact", "only works on wood", "is a type of friction"]),
    ("Between two like poles there is a…", "neutral point", ["strong attraction", "spark", "battery"]),
    ("A compass needle points…", "north", ["south", "east", "down"]),
    ("Earth's field protects us from…", "fast charged particles from the Sun", ["rain", "meteors only", "sound"]),
    ("Birds use Earth's magnetic field to…", "navigate", ["feed", "sleep", "build nests"]),
    ("Maglev trains use magnets to…", "lift and push the train", ["slow it with friction", "make it heavier", "cool it"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the magnetic materials.", ["Iron", "Nickel", "Steel"], ["Copper", "Aluminium"])
u.mt("p", "Match the type of magnet to its description.", [("Permanent magnet", "keeps its magnetism"), ("Temporary magnet", "magnetic only in a field"), ("Electromagnet", "can be switched on and off")])
u.od("p", "Order the field strength around a bar magnet, strongest first.", ["At the poles", "Near the magnet's sides", "Far from the magnet"])
u.ex("a", "* Advanced. Describe how you could use a compass to plot the field lines around a bar magnet.", [("place compass near the magnet", ["place|put|near"]), ("mark where the needle points, move compass on", ["mark|dot|move"]), ("join the dots into lines from N to S", ["join|line|N.*S|north.*south"])],
     "Place a small compass near the North pole and mark where the needle points. Move the compass to that mark and repeat, then join the dots to draw a field line from N to S. Repeat from other starting points.")
u.mc("a", "Why do two maglev magnets with like poles facing each other lift the train?", "Like poles repel, pushing the train up off the track.", ["Like poles attract.", "Gravity pushes up.", "The track is non-magnetic."], skill="Reasoning")
u.mc("a", "A steel paper clip sticks to a magnet and then picks up another clip. Why?", "The first clip becomes a temporary magnet.", ["Paper clips are permanent magnets.", "The second clip is copper.", "Gravity is reversed."], skill="Reasoning")
u.gd("a", "What happens to the field lines?", "Field lines", [("Opposite poles near each other", "Join up"), ("Like poles near each other", "Push apart")])
u.stop("unlike poles attract, and like poles repel", "Two North poles brought together…", "repel", ["attract", "join", "do nothing"])
u.stop("are non-magnetic", "Which is a magnetic material?", "Iron", ["Copper", "Aluminium", "Wood"])
u.stop("where the field is strongest", "The magnetic field of a bar magnet is strongest…", "at the poles", ["in the middle", "far away", "nowhere"])
u.stop("so maps show the difference", "Earth's magnetic field is produced by…", "moving molten metal in the outer core", ["a giant bar magnet", "the Moon", "the Sun"])

# ---------------------------------------------------------------- 11.2
u.sec("11.2", "O2")
u.tb("r", "Results: paper clips picked up by an electromagnet. Complete the table.", ["Turns of wire", "Paper clips picked up", "More than with 10 turns"], [["10", "4", "0"], ["20", "9", B(5)], ["30", "13", B(9)]])
u.gd("r", "Does each change make an electromagnet stronger or weaker?", "Effect", [("More turns on the coil", "Stronger"), ("Bigger current", "Stronger"), ("Removing the iron core", "Weaker"), ("Fewer cells", "Weaker")])
u.mc("r", "Who discovered that an electric current affects a compass needle?", "Hans Christian Ørsted", ["Isaac Newton", "Marie Curie", "Charles Darwin"])
u.ex("r", "Describe how to make a simple electromagnet.", [("coil insulated wire around an iron nail", ["coil|wind|wrap|nail"]), ("connect to a cell and switch", ["cell|battery|switch"]), ("current flows – nail becomes magnetic", ["current|magnet"])],
     "Wind insulated wire into a coil around an iron nail and connect the ends to a cell and a switch. When the switch is closed, current flows and the nail becomes a magnet.")
u.mc("r", "When the switch of an electromagnet is opened…", "the magnetism disappears and the clips drop", [("it stays magnetic forever", "No."), ("it gets stronger", "No."), ("the clips stick harder", "No.")])
u.mc("r", "Why should the current not be left on too long?", "The wire can get hot", [("It runs out of magnetism", "No."), ("The nail melts at once", "No."), ("The clips get heavier", "No.")], d="H")
u.mc("r", "To test how the number of turns affects strength fairly, you should…", "change only the turns and keep the current and core the same", [("change the current too", "No."), ("use different nails", "No."), ("change everything", "No.")], d="H")
u.mc("r", "Why does an iron core make an electromagnet stronger?", "It concentrates the magnetic field lines", [("It adds current", "No."), ("It is non-magnetic", "No."), ("It cools the wire", "No.")], d="VH")
for p, r, w in [
    ("A wire carrying a current has…", "a magnetic field around it", ["no field", "an electric field only", "a gravitational pull only"]),
    ("Ørsted showed that electricity and magnetism…", "interact", ["are unrelated", "cancel out", "are the same as heat"]),
    ("An electromagnet uses a coil of…", "insulated wire", ["string", "plastic only", "glass"]),
    ("The core of an electromagnet is usually…", "iron", ["copper", "wood", "plastic"]),
    ("Adding more turns to the coil makes the electromagnet…", "stronger", ["weaker", "switch off", "non-magnetic"]),
    ("Increasing the current makes it…", "stronger", ["weaker", "colder", "heavier"]),
    ("You can increase the current by…", "adding more cells", ["removing cells", "using plastic wire", "removing the switch"]),
    ("An electromagnet with no current is…", "not magnetic", ["very strong", "a permanent magnet", "hot"]),
    ("The main advantage of electromagnets is that they…", "can be switched on and off", ["never work", "are always on", "are made of wood"]),
    ("Each extra turn of wire…", "adds to the magnetic field", ["takes away from it", "makes no difference", "cools the core"]),
    ("Steel paper clips are used in tests because they are…", "magnetic", ["non-magnetic", "electrical insulators", "very heavy"]),
    ("The dependent variable when testing turns is…", "the number of paper clips picked up", ["the number of turns", "the type of core", "the cell"]),
    ("The independent variable when testing turns is…", "the number of turns", ["the paper clips", "the switch", "the nail size"]),
    ("A control variable when testing turns is…", "the current", ["the number of turns", "the paper clips picked up", "the result"]),
    ("Electromagnets turn electrical energy into…", "a magnetic effect", ["light only", "sound only", "chemical energy"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the ways to make an electromagnet stronger.", ["More turns", "More current", "An iron core"], ["A plastic core", "Fewer cells"])
u.od("p", "Order the steps when the switch is closed.", ["Current flows in the coil", "Coil becomes a magnet", "Iron core is magnetised", "Paper clips are picked up"])
u.gr("p", "Plot the paper clips picked up against the number of turns.", {"label": "Turns", "min": 0, "max": 40, "step": 10}, {"label": "Paper clips", "min": 0, "max": 20, "step": 5}, [[10, 4], [20, 9], [30, 13], [40, 18]])
u.ex("a", "* Advanced. A student's results: 10 turns – 4 clips, 20 turns – 9 clips, 30 turns – 3 clips. Identify the anomaly and suggest what to do.", [("30 turns result is anomalous", ["30|3 clips|anomal"]), ("does not fit the pattern / should be higher", ["pattern|higher|more"]), ("repeat the test", ["repeat|again"])],
     "The 30-turn result (3 clips) is anomalous – it does not fit the pattern of more clips with more turns. The student should repeat that test and check the wires and current.")
u.mc("a", "Why does a steel core keep some magnetism after the current stops, but soft iron does not?", "Steel is a permanent magnetic material; soft iron is temporary.", ["Steel is non-magnetic.", "Soft iron is a permanent magnet.", "Steel conducts no current."], skill="Reasoning")
u.mc("a", "From the graph, about how many clips would 25 turns pick up?", "About 11", ["About 4", "About 20", "About 30"], skill="Data")
u.mc("a", "Why does the wire of an electromagnet need insulation?", "So the current flows around the coil instead of short-circuiting through the core.", ["To make it magnetic.", "To keep it cold.", "To make it lighter."], skill="Reasoning")
u.stop("Any wire carrying a current has a magnetic field around it", "Who noticed a compass needle moving near a current?", "Ørsted", ["Newton", "Rutherford", "Galileo"])
u.stop("as the wire can get hot", "When the current stops, the electromagnet…", "loses its magnetism", ["keeps its magnetism", "gets stronger", "gets heavier"])
u.stop("keeping the current and core the same", "Which change makes an electromagnet stronger?", "More turns on the coil", ["Fewer cells", "Removing the core", "A plastic core"])

# ---------------------------------------------------------------- 11.3
u.sec("11.3", "O3")
u.gd("r", "Where is each electromagnet used?", "Setting", [("Crane lifting scrap steel", "Industry"), ("MRI scanner", "Hospital"), ("Electric bell", "Home"), ("Loudspeaker", "Home")])
u.mc("r", "Why do scrapyards use electromagnets instead of permanent magnets?", "They can be switched off to drop the metal", [("They are cheaper", "Not the reason."), ("They attract copper", "No."), ("They never get hot", "No.")])
u.ex("r", "Explain how a loudspeaker uses an electromagnet to make sound.", [("changing current in a coil", ["changing current|current"]), ("changing magnetic field", ["field|magnet"]), ("moves the cone, which vibrates the air", ["cone|vibrat|move"])],
     "A changing current in the coil makes a changing magnetic field, which pushes and pulls against a magnet, moving the cone back and forth so it vibrates the air and makes sound.")
u.tb("r", "Recycling plant: mass of each metal in 100 kg of mixed cans. Complete the table.", ["Metal", "Mass (kg)", "Pulled out by magnet?"], [["Steel", "60", "Yes"], ["Aluminium", B(40), "No"]])
u.mc("r", "MRI scanners use a huge magnet to line up…", "hydrogen atoms in the body", [("bones", "No."), ("blood cells only", "No."), ("iron filings", "No.")], d="H")
u.mc("r", "Power station generators use…", "spinning electromagnets", ["light bulbs", "permanent magnets only", "batteries"], d="H")
u.mc("r", "Which is NOT a use of an electromagnet?", "A wooden spoon", ["An electric motor", "A hard drive", "An electric bell"])
u.mc("r", "Why can recycling plants separate steel cans from aluminium cans with a magnet?", "Steel is magnetic but aluminium is not", [("Aluminium is magnetic", "No."), ("Steel is lighter", "No."), ("Both are magnetic", "No.")], d="VH")
for p, r, w in [
    ("Electromagnets are used in the motors of…", "blenders and fans", ["candles", "pencils", "rulers"]),
    ("A loudspeaker coil moves the…", "cone", ["battery", "plug", "case"]),
    ("Computer hard drives use…", "electromagnets", ["prisms", "lenses", "thermometers"]),
    ("Giant crane electromagnets lift…", "scrap iron and steel", ["scrap copper", "plastic", "glass"]),
    ("Recycling plants use electromagnets to remove…", "magnetic metals from waste", ["paper", "glass", "food"]),
    ("In an MRI scanner, radio waves knock atoms…", "out of line", ["into the magnet", "out of the body", "into the blood"]),
    ("As atoms flip back in an MRI scanner they…", "release energy used to build pictures", ["absorb X-rays", "make sound only", "stop moving"]),
    ("MRI scanners make…", "detailed pictures inside the body", ["electricity", "magnets", "sound"]),
    ("Electric bells use an electromagnet to…", "pull a striker repeatedly", ["make light", "heat water", "cool the bell"]),
    ("Maglev trains emit far less carbon than…", "diesel trains", ["bicycles", "walking", "sailing boats"]),
    ("An electromagnet in a door lock can…", "hold the door shut until switched off", ["make the door lighter", "cool the room", "make sound"]),
    ("Spinning electromagnets in generators produce…", "electricity", ["sound", "fuel", "water"]),
    ("Which device turns electrical energy into movement?", "An electric motor", ["A thermometer", "A prism", "A ruler"]),
    ("Electromagnets are useful in industry because they can be…", "very strong and switched off", ["weak and permanent", "made of plastic", "never controlled"]),
    ("Which metal can a scrapyard magnet NOT pick up?", "Copper", ["Iron", "Steel", "Nickel"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the devices that use electromagnets.", ["Electric bell", "Loudspeaker", "MRI scanner"], ["Candle", "Mirror"])
u.mt("p", "Match the device to what the electromagnet does.", [("Crane", "lifts and drops scrap steel"), ("Loudspeaker", "moves a cone"), ("Generator", "produces electricity")])
u.gd("p", "Can a magnet pull it out of mixed waste?", "Magnet?", [("Steel can", "Yes"), ("Aluminium can", "No"), ("Plastic bottle", "No")])
u.ex("a", "* Advanced. Suggest why people with metal implants may not be allowed in an MRI scanner.", [("very strong magnet", ["strong magnet|huge magnet|powerful"]), ("magnetic metal is pulled / moves / heats", ["pull|move|attract|heat"]), ("could injure the patient or damage the scan", ["injur|harm|danger|damage"])],
     "The MRI scanner has a very powerful magnet. A magnetic metal implant could be pulled or moved, or heat up, which could injure the patient.")
u.mc("a", "Why are maglev trains more energy-efficient than wheeled trains?", "There is no friction between wheels and track.", ["They are heavier.", "They use coal.", "They have more wheels."], skill="Reasoning")
u.mc("a", "How could an electromagnet sort a mixture of iron and copper scraps?", "Switch it on to lift the iron, move it, then switch it off.", ["It would lift the copper.", "It would lift both.", "It cannot be switched on."], skill="Reasoning")
u.mc("a", "Why does a loudspeaker need a CHANGING current?", "A changing current makes the cone move back and forth to create vibrations.", ["A steady current makes louder sound.", "Current does not matter.", "To keep it cool."], skill="Reasoning")
u.stop("all use electromagnets", "A loudspeaker makes sound by moving its…", "cone", ["battery", "wire colour", "plug"])
u.stop("then switch off to drop it", "Why do scrapyards use electromagnets?", "They can be switched off to drop the metal", ["They attract all metals", "They are made of copper", "They never work"])
u.stop("build detailed pictures inside you", "MRI scanners line up…", "hydrogen atoms", ["bones", "iron filings", "copper atoms"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Magnetism", "sec": None, "kids": [
    {"id": "mg", "t": "Magnets", "d": "N and S poles • Unlike attract, like repel • Fe, Ni, Co, steel", "obj": "O1", "sec": "11.1"},
    {"id": "fd", "t": "Magnetic fields", "d": "Field lines N → S • Strongest at poles • Fields interact", "obj": "O1", "sec": "11.1"},
    {"id": "ea", "t": "Earth's field", "d": "Molten metal in outer core • Compasses • Birds navigate • Protects us", "obj": "O1", "sec": "11.1"},
    {"id": "em", "t": "Electromagnets", "d": "Coil + iron core + current • Switch on and off • Ørsted", "obj": "O2", "sec": "11.2"},
    {"id": "st", "t": "Stronger electromagnets", "d": "More turns • More current • Iron core • Fair test", "obj": "O2", "sec": "11.2"},
    {"id": "us", "t": "Uses", "d": "Speakers, bells, motors • Cranes, recycling, generators • MRI scanners", "obj": "O3", "sec": "11.3"},
]}
