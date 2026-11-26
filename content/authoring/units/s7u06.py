# -*- coding: utf-8 -*-
"""Stage 7 Unit 6 – Materials and Their Structure. Written by the Camday teaching team."""
from c_kit import *

STRAND = "Chemistry"
BLURB = "Solids, liquids and gases and the particle model, changes of state, elements and atoms, the Periodic Table, compounds and mixtures."

OBJECTIVES = {
    "O1": {"sec": "6.1", "code": "7Cm.06", "codeNote": "", "t": "Describe the properties of solids, liquids and gases using the particle model."},
    "O2": {"sec": "6.1", "code": "7TWSm.01, 7SIC.01", "codeNote": "", "t": "Describe how the particle model developed and its strengths and limitations."},
    "O3": {"sec": "6.2", "code": "7Cm.06, 7TWSa.05", "codeNote": "", "t": "Explain changes of state with the particle model and interpret heating curves."},
    "O4": {"sec": "6.3", "code": "7Cm.01, 7TWSm.02", "codeNote": "", "t": "Describe elements, atoms and molecules and use chemical symbols and formulae."},
    "O5": {"sec": "6.4", "code": "7Cm.02, 7Cm.03", "codeNote": "", "t": "Use the Periodic Table and classify elements as metals and non-metals."},
    "O6": {"sec": "6.5", "code": "7Cm.04, 7Cm.07", "codeNote": "", "t": "Describe compounds, interpret their formulae and apply conservation of mass."},
    "O7": {"sec": "6.6", "code": "7Cm.04", "codeNote": "", "t": "Describe mixtures and alloys and compare elements, compounds and mixtures."},
}

SECTIONS = [
    {"id": "6.1", "title": "Solids, liquids and gases", "objs": ["O1", "O2"]},
    {"id": "6.2", "title": "Changes of state", "objs": ["O3"]},
    {"id": "6.3", "title": "Elements, atoms and molecules", "objs": ["O4"]},
    {"id": "6.4", "title": "The Periodic Table", "objs": ["O5"]},
    {"id": "6.5", "title": "Compounds", "objs": ["O6"]},
    {"id": "6.6", "title": "Mixtures", "objs": ["O7"]},
]

# ---------------------------------------------------------------- 6.1
S1_REQ = [
    gd("u6s1r1", "M", "O1", "Tick (✓) or cross (✗) each property.", ["Solid", "Liquid", "Gas"],
       [("Definite shape", ["✓", "✗", "✗"]), ("Definite volume", ["✓", "✓", "✗"]), ("Can flow", ["✗", "✓", "✓"]), ("Can be compressed", ["✗", "✗", "✓"])], skill="Data"),
    mt("u6s1r2", "M", "O1", "Match each state to its particle arrangement.", [("Solid", "packed closely in a regular pattern, vibrating in place"), ("Liquid", "close together, touching, moving around each other"), ("Gas", "far apart, moving fast in all directions")]),
    ex("u6s1r3", "H", "O1", "Use the particle model to explain why a gas can be compressed but a liquid cannot.",
       [("gas particles far apart / empty space", ["far apart|space|gap"]), ("liquid particles touching / close together", ["touch|close"])],
       "In a gas the particles are far apart with empty space between them, so they can be pushed closer. In a liquid the particles are already touching, so there is no space to squash them into.", need=2),
    mc("u6s1r4", "H", "O1", "Why do car brakes use a liquid in the tube?", ("Liquids cannot be compressed, so the push reaches the brakes straight away.", "Correct."),
       [("Liquids are lighter than gases.", "Not the reason."), ("Liquids have a fixed shape.", "They do not."), ("Liquids can be squashed easily.", "They cannot.")], skill="Reasoning"),
    od("u6s1r5", "H", "O2", "Order the development of the particle idea.", ["Democritus: everything is made of tiny atoms (no evidence)", "Dalton: atoms are building blocks (about 1800)", "Brown: pollen grains jiggle in water", "Einstein explains Brownian motion; Perrin's experiments confirm it"]),
    mc("u6s1r6", "H", "O2", "Which is a LIMITATION of the particle model?", ("It shows all particles as identical balls, but real particles differ in size and shape.", "Correct."),
       [("It explains why ice is hard.", "That is a strength."), ("It explains why gases fill a space.", "A strength."), ("It uses particles.", "Not a limitation.")]),
    tb("u6s1r7", "H", "O1", "Data: volume of 1 g of water in each state (approx.). Complete how many times bigger than the liquid.", ["State", "Volume (cm³)", "Times liquid volume"],
       [["Liquid water", "1.0", "1"], ["Ice", "1.1", B(1.1)], ["Steam (at 100 °C)", "1700", B(1700)]], skill="Data",
       reason="Steam takes about 1700 times the volume: gas particles are very far apart."),
    mc("u6s1r8", "VH", "O1", "Brownian motion: pollen grains in water jiggle randomly. What causes this?", ("Invisible water particles keep hitting the grains from all sides.", "Correct – evidence for moving particles."),
       [("The pollen is alive and swimming.", "Even dead dust particles jiggle."), ("Light pushes the grains.", "No."), ("The microscope shakes.", "No.")], skill="Reasoning"),
]
S1_PRAC = [
    mc("u6s1p01", "M", "O1", "Which state takes the shape of its container but keeps its volume?", "Liquid", [("Solid", "Fixed shape."), ("Gas", "Fills the whole container."), ("None", "Liquid.")]),
    mc("u6s1p02", "M", "O1", "In a solid, particles…", "vibrate about fixed positions", [("move freely in all directions", "Gas."), ("slide past each other", "Liquid."), ("do not move at all", "They vibrate.")]),
    mc("u6s1p03", "M", "O1", "Which can flow?", "Liquids and gases", [("Only solids", "No."), ("Only gases", "Liquids flow too."), ("Nothing", "No.")]),
    mc("u6s1p04", "M", "O1", "Why does a gas fill any container?", "Its particles move fast in all directions and spread out.", [("Its particles are bigger.", "No."), ("It is heavier.", "No."), ("It has a fixed volume.", "No.")]),
    mc("u6s1p05", "H", "O1", "Why can't you squash a block of wood?", "Its particles are packed closely with strong forces between them.", [("It is too heavy.", "No."), ("It is alive.", "No."), ("Its particles are far apart.", "No.")]),
    mc("u6s1p06", "M", "O1", "Water vapour is water in which state?", "Gas", [("Solid", "Ice."), ("Liquid", "Water."), ("Plasma", "No.")]),
    mc("u6s1p07", "H", "O1", "What is between gas particles?", "Empty space", [("Air", "Air is made of gas particles itself."), ("Water", "No."), ("More particles packed tightly", "No.")]),
    mc("u6s1p08", "M", "O2", "Who first suggested atoms over 2000 years ago?", "Democritus", [("Dalton", "Around 1800."), ("Einstein", "1900s."), ("Brown", "Pollen observation.")]),
    mc("u6s1p09", "M", "O2", "Who explained Brownian motion?", "Albert Einstein", [("Robert Brown", "He observed it."), ("Democritus", "No."), ("Mendeleev", "Periodic Table.")]),
    mc("u6s1p10", "H", "O2", "Why did Perrin's experiments matter?", "They matched Einstein's predictions, giving evidence for particles.", [("They disproved particles.", "No."), ("They made particles visible to the eye.", "No."), ("They discovered pollen.", "No.")]),
    mc("u6s1p11", "H", "O2", "The particle model ignores the forces between particles. Why is that a limitation?", "Attractive forces change how particles behave, e.g. when liquids flow.", [("Forces do not exist.", "They do."), ("It makes the model too hard.", "No."), ("It is not a limitation.", "It is.")]),
    mc("u6s1p12", "M", "O2", "Models in science…", "are simplified pictures that explain observations", [("are always perfect", "No."), ("are never useful", "Very useful."), ("cannot change", "They change with evidence.")]),
    ms("u6s1p13", "H", "O1", "Select ALL properties of liquids.", ["Fixed volume", "Can flow", "Cannot be compressed"], [("Fixed shape", "Takes container's shape."), ("Particles far apart", "Gas.")]),
    mc("u6s1p14", "H", "O1", "A balloon of air can be squeezed smaller. This shows gases…", "can be compressed", [("have a fixed volume", "No."), ("cannot flow", "No."), ("are solids", "No.")]),
    mc("u6s1p15", "M", "O1", "Which state has the strongest forces between particles?", "Solid", [("Liquid", "Weaker."), ("Gas", "Almost none."), ("All equal", "No.")]),
    mc("u6s1p16", "H", "O1", "Why is water runny but ice is hard?", "Water particles move around each other; ice particles vibrate in fixed places.", [("Ice has more particles.", "Same particles."), ("Water is lighter.", "No."), ("Ice is a different substance.", "Same substance.")]),
    mc("u6s1p17", "H", "O2", "Dalton described atoms as…", "tiny building blocks", [("waves", "No."), ("living cells", "No."), ("pollen grains", "No.")]),
    od("u6s1p18", "M", "O1", "Order from particles closest together to furthest apart.", ["Solid", "Liquid", "Gas"]),
]
S1_ADV = [
    adv(ex("u6s1a1", "VH", "O1", "You can smell perfume across a room a few seconds after the bottle is opened. Explain using the particle model.",
           [("perfume evaporates to gas", ["gas|evapor"]), ("particles move fast / randomly", ["move|random|fast"]), ("spread out / mix with air particles", ["spread|diffus|mix|across"])],
           "Perfume evaporates into a gas. Its particles move fast and randomly, colliding with air particles, so they spread out across the room until they reach your nose (diffusion).", need=2)),
    adv(mc("u6s1a2", "VH", "O1", "Steam occupies about 1700 times the volume of the same mass of water. What does this tell you?", ("Gas particles are very far apart compared with liquid particles.", "Correct."),
           [("Steam particles are 1700 times bigger.", "Particles stay the same size."), ("Steam has more particles.", "Same mass, same particles."), ("Steam is a solid.", "No.")], skill="Reasoning")),
    adv(mc("u6s1a3", "VH", "O2", "Why is the particle model still used even though it has limitations?", ("It explains and predicts many observations simply.", "Correct."),
           [("Nobody has found a better one.", "Better ones exist for some uses; this one is useful."), ("It is perfect.", "No."), ("Teachers like it.", "No.")], skill="Reasoning")),
    adv(mc("u6s1a4", "VH", "O1", "A gas syringe is sealed and the plunger pushed in. What happens to the particles?", ("They move closer together; the same number fill a smaller volume.", "Correct."),
           [("They get smaller.", "No."), ("Some disappear.", "No."), ("They turn into a liquid immediately.", "Not at normal pressures.")], skill="Reasoning")),
]

# ---------------------------------------------------------------- 6.2
S2_REQ = [
    gd("u6s2r1", "M", "O3", "Name each change of state.", ["Change"],
       [("Solid → liquid", ["Melting"]), ("Liquid → solid", ["Freezing"]), ("Liquid → gas", ["Evaporation or boiling"]), ("Gas → liquid", ["Condensation"])], skill="Data"),
    mc("u6s2r2", "M", "O3", "In a change of state, what changes?", ("Only the arrangement, closeness and movement of the particles – no new substance is made.", "Correct."),
       [("The particles become a new substance.", "No new substance."), ("The particles change size.", "No."), ("The number of particles changes.", "No.")]),
    gr("u6s2r3", "H", "O3", "Data: heating crushed ice. Plot the temperature.", {"label": "Time (min)", "min": 0, "max": 20, "step": 2}, {"label": "Temperature (°C)", "min": -20, "max": 120, "step": 20},
       [[0, -20], [2, 0], [4, 0], [6, 40], [8, 80], [10, 100], [12, 100]],
       follow=mc("u6s2r3f", "H", "O3", "Why is the line flat at 0 °C and 100 °C?", ("Energy is used to overcome forces between particles during melting and boiling, so the temperature does not rise.", "Correct."),
                 [("The Bunsen burner was switched off.", "No."), ("The thermometer broke.", "No."), ("Water cannot get hotter than 0 °C.", "No.")])),
    ex("u6s2r4", "H", "O3", "Use the particle model to explain what happens when ice melts.",
       [("particles gain energy / vibrate faster", ["energy|vibrat"]), ("overcome forces holding them", ["overcome|break|force"]), ("start moving around each other", ["move around|slide|move past"])],
       "When ice is heated, its particles gain energy and vibrate faster. At the melting point they have enough energy to overcome the forces holding them in place and begin to move around each other – the solid becomes a liquid.", need=2),
    mc("u6s2r5", "H", "O3", "What is the difference between evaporation and boiling?", ("Evaporation happens only at the surface at any temperature; boiling happens throughout the liquid at the boiling point.", "Correct."),
       [("They are the same.", "No."), ("Boiling happens at any temperature.", "Only at the boiling point."), ("Evaporation makes bubbles inside.", "That is boiling.")]),
    tb("u6s2r6", "H", "O3", "Data: melting and boiling points. Complete the state at 25 °C.", ["Substance", "Melting point (°C)", "Boiling point (°C)", "State at 25 °C"],
       [["Water", "0", "100", B("liquid")], ["Aluminium", "660", "2470", B("solid")], ["Oxygen", "-218", "-183", B("gas")]], skill="Data",
       hint="Below the melting point → solid; between melting and boiling → liquid; above boiling → gas."),
    mc("u6s2r7", "M", "O3", "Water droplets on the outside of a cold glass come from…", ("water vapour in the air condensing", "Correct."), [("water leaking through the glass", "No."), ("melting ice", "No."), ("the glass sweating", "No.")]),
    mc("u6s2r8", "VH", "O3", "If you heat MORE ice, how does the heating graph change?", ("It takes longer, but the melting point (0 °C) and boiling point (100 °C) stay the same.", "Correct."),
       [("The melting point rises.", "No."), ("The flat parts disappear.", "No."), ("Water boils at 50 °C.", "No.")], skill="Reasoning"),
]
S2_PRAC = [
    mc("u6s2p01", "M", "O3", "Chocolate in your hand is…", "melting", [("freezing", "No."), ("boiling", "No."), ("condensing", "No.")]),
    mc("u6s2p02", "M", "O3", "Rain turning into ice is…", "freezing", [("melting", "No."), ("evaporation", "No."), ("condensation", "No.")]),
    mc("u6s2p03", "M", "O3", "Pure water boils at…", "100 °C", [("0 °C", "Melting point."), ("50 °C", "No."), ("212 °C", "That is °F.")]),
    mc("u6s2p04", "M", "O3", "Pure aluminium melts at…", "660 °C", [("100 °C", "No."), ("0 °C", "No."), ("2000 °C", "No.")]),
    mc("u6s2p05", "M", "O3", "A substance's freezing point is…", "the same as its melting point", [("higher than its melting point", "No."), ("its boiling point", "No."), ("always 0 °C", "Only water.")]),
    mc("u6s2p06", "H", "O3", "Why do puddles dry up on a cool day?", "Evaporation happens at any temperature.", [("Puddles boil.", "No."), ("Water soaks into clouds.", "No."), ("Puddles freeze.", "No.")]),
    mc("u6s2p07", "H", "O3", "When a liquid cools and freezes, its particles…", "lose energy, slow down and lock into a regular arrangement", [("gain energy", "Lose."), ("move further apart", "Closer."), ("disappear", "No.")]),
    mc("u6s2p08", "M", "O3", "Condensation is the opposite of…", "evaporation/boiling", [("melting", "Opposite of freezing."), ("freezing", "No."), ("dissolving", "No.")]),
    mc("u6s2p09", "H", "O3", "Is melting a chemical change?", "No – no new substance is made; it is a physical change.", [("Yes – a new substance forms.", "No."), ("Only for metals.", "No."), ("Only above 100 °C.", "No.")]),
    mc("u6s2p10", "H", "O3", "Bubbles forming inside water show it is…", "boiling", [("evaporating at the surface", "No bubbles inside."), ("freezing", "No."), ("melting", "No.")]),
    mc("u6s2p11", "H", "O3", "A substance melts at −39 °C and boils at 357 °C. At 20 °C it is a…", "liquid", [("solid", "Above its melting point."), ("gas", "Below boiling point."), ("plasma", "No.")], skill="Data"),
    mc("u6s2p12", "H", "O3", "A substance melts at 801 °C. At room temperature it is…", "solid", [("liquid", "No."), ("gas", "No."), ("cannot tell", "Below melting point → solid.")], skill="Data"),
    mc("u6s2p13", "M", "O3", "What safety equipment is needed when heating ice in a beaker?", "Safety goggles", [("Sunglasses", "No."), ("Nothing", "No."), ("Gloves only", "Goggles.")]),
    mc("u6s2p14", "H", "O3", "Why does the temperature stay at 100 °C while water boils?", "The energy is used to separate particles into a gas.", [("The thermometer stops.", "No."), ("Water cannot hold energy.", "No."), ("The flame gets weaker.", "No.")]),
    od("u6s2p15", "M", "O3", "Order the changes as ice is heated to steam.", ["Solid ice warms up", "Ice melts at 0 °C", "Water warms up", "Water boils at 100 °C"]),
    mc("u6s2p16", "H", "O3", "Butter melting in a hot pan is…", "a change of state", [("a new substance forming", "No."), ("condensation", "No."), ("evaporation", "No.")]),
    gd("u6s2p17", "M", "O3", "Heat taken in or given out?", ["Energy"], [("Melting", ["Taken in"]), ("Boiling", ["Taken in"]), ("Freezing", ["Given out"]), ("Condensation", ["Given out"])], skill="Data"),
    mc("u6s2p18", "H", "O3", "Gas particles cooling and coming together to form a liquid is…", "condensation", [("evaporation", "No."), ("melting", "No."), ("boiling", "No.")]),
]
S2_ADV = [
    adv(ex("u6s2a1", "VH", "O3", "Salt water boils at a little above 100 °C and has no sharp freezing point. What does this tell you about salt water?",
           [("not pure / mixture", ["mixture|not pure|impure"]), ("pure substances have fixed points", ["pure|fixed"])],
           "Salt water is a mixture, not a pure substance. Pure substances have fixed melting and boiling points; mixtures do not.", need=2)),
    adv(mc("u6s2a2", "VH", "O3", "Why do sweat and wet clothes feel cold as they dry?", ("Evaporation takes energy from your skin.", "Correct."),
           [("Water is always cold.", "No."), ("Condensation releases cold.", "No."), ("Wind turns water to ice.", "No.")], skill="Reasoning")),
    adv(mc("u6s2a3", "VH", "O3", "Oxygen boils at −183 °C. At −200 °C oxygen is…", ("a liquid (it freezes at −218 °C)", "Correct."), [("a gas", "Below boiling point."), ("a solid", "Above −218 °C."), ("cannot exist", "No.")], skill="Data")),
    adv(nm("u6s2a4", "VH", "O3", "Ice warms from −20 °C to 0 °C in 2 minutes. At the same rate, how many °C per minute?", 10, "°C/min")),
]

# ---------------------------------------------------------------- 6.3
S3_REQ = [
    mc("u6s3r1", "M", "O4", "What is an element?", ("A substance that cannot be broken down into simpler substances by chemical reactions.", "Correct."),
       [("Any substance with water.", "No."), ("A mixture of two substances.", "No."), ("Something made of many compounds.", "No.")]),
    gd("u6s3r2", "H", "O4", "Element or not?", ["Element?"], [("Oxygen", ["Yes"]), ("Water", ["No"]), ("Copper", ["Yes"]), ("Salt", ["No"]), ("Neon", ["Yes"])], skill="Data"),
    mt("u6s3r3", "M", "O4", "Match each element to its symbol.", [("Sodium", "Na"), ("Iron", "Fe"), ("Copper", "Cu"), ("Silver", "Ag"), ("Magnesium", "Mg")]),
    mc("u6s3r4", "M", "O4", "Which symbol is written correctly?", "Cl", [("CL", "Second letter lower case."), ("cl", "First letter capital."), ("cL", "No.")]),
    tb("u6s3r5", "H", "O4", "Complete the number of atoms in each molecule.", ["Formula", "Element", "Atoms per molecule"],
       [["O₂", "oxygen", B(2)], ["P₄", "phosphorus", B(4)], ["S₈", "sulfur", B(8)], ["N₂", "nitrogen", B(2)]], skill="Data"),
    ex("u6s3r6", "H", "O4", "Explain the difference between an atom and a molecule of an element.",
       [("atom = smallest part of an element", ["smallest|single"]), ("molecule = atoms joined chemically", ["joined|bonded|combined|together"]), ("same element", ["one (type of )?element|same element|only one"])],
       "An atom is the smallest part of an element that cannot be broken down chemically. A molecule of an element is two or more atoms of the same element joined chemically, e.g. O₂.", need=2),
    od("u6s3r7", "H", "O4", "Order from smallest to largest.", ["Hydrogen atom", "Virus", "Bacterium", "Animal cell"]),
    mc("u6s3r8", "VH", "O4", "Water can be split into hydrogen and oxygen using electricity, but these cannot be split further. What does this show?", ("Water is not an element; hydrogen and oxygen are elements.", "Correct."),
       [("Water is an element.", "It can be broken down."), ("Electricity is an element.", "No."), ("Hydrogen is a compound.", "No.")], skill="Reasoning"),
]
S3_PRAC = [
    mc("u6s3p01", "M", "O4", "Symbol for helium?", "He", [("H", "Hydrogen."), ("HE", "Lower case e."), ("Hl", "No.")]),
    mc("u6s3p02", "M", "O4", "Symbol for carbon?", "C", [("Ca", "Calcium."), ("Co", "Cobalt."), ("Cb", "No.")]),
    mc("u6s3p03", "M", "O4", "Fe comes from the Latin name…", "ferrum (iron)", [("fluorine", "F."), ("feather", "No."), ("argentum", "Ag.")]),
    mc("u6s3p04", "M", "O4", "The most common element in the universe is…", "hydrogen", [("oxygen", "Most common in Earth's crust."), ("carbon", "No."), ("iron", "No.")]),
    mc("u6s3p05", "M", "O4", "Which element is found in all living things?", "Carbon", [("Neon", "No."), ("Gold", "No."), ("Helium", "No.")]),
    mc("u6s3p06", "M", "O4", "Which element glows in some signs?", "Neon", [("Iron", "No."), ("Sulfur", "No."), ("Copper", "No.")]),
    mc("u6s3p07", "H", "O4", "Which element exists as single atoms?", "Argon", [("Oxygen", "O₂ molecules."), ("Nitrogen", "N₂."), ("Sulfur", "S₈.")]),
    mc("u6s3p08", "H", "O4", "In N₂, the small 2 is called a…", "subscript", [("superscript", "No."), ("symbol", "N is the symbol."), ("charge", "No.")]),
    mc("u6s3p09", "M", "O4", "A bar of pure copper contains…", "only copper atoms", [("copper and oxygen atoms", "Pure copper."), ("molecules of water", "No."), ("cells", "No.")]),
    mc("u6s3p10", "H", "O4", "To see an image of atoms we need a…", "scanning tunnelling microscope", [("hand lens", "Far too weak."), ("light microscope", "Too weak."), ("telescope", "No.")]),
    mc("u6s3p11", "M", "O4", "The smallest atom is…", "hydrogen", [("oxygen", "No."), ("gold", "No."), ("carbon", "No.")]),
    mc("u6s3p12", "H", "O4", "Why are chemical symbols useful?", "They are the same in every language.", [("They are shorter than numbers.", "Not the main reason."), ("They show the colour.", "No."), ("They change in each country.", "They do not.")]),
    mc("u6s3p13", "M", "O4", "Symbol for chlorine?", "Cl", [("C", "Carbon."), ("Ch", "No."), ("CL", "Lower case l.")]),
    mc("u6s3p14", "H", "O4", "Na comes from…", "natrium (sodium)", [("nitrogen", "N."), ("neon", "Ne."), ("nickel", "Ni.")]),
    mc("u6s3p15", "H", "O4", "How many atoms in one S₈ molecule?", "8", [("1", "No."), ("2", "No."), ("16", "No.")]),
    mc("u6s3p16", "M", "O4", "The most common element in Earth's crust is…", "oxygen", [("hydrogen", "Universe."), ("iron", "No."), ("carbon", "No.")]),
    mc("u6s3p17", "H", "O4", "Ag is the symbol for…", "silver", [("gold", "Au."), ("aluminium", "Al."), ("argon", "Ar.")]),
    mt("u6s3p18", "M", "O4", "Match symbol to element.", [("H", "hydrogen"), ("O", "oxygen"), ("Mg", "magnesium"), ("Cu", "copper")]),
]
S3_ADV = [
    adv(mc("u6s3a1", "VH", "O4", "Ozone has formula O₃. Is ozone an element or a compound?", ("A form of the element oxygen – all its atoms are oxygen.", "Correct."), [("A compound.", "Only one element."), ("A mixture.", "Atoms are joined."), ("Not a substance.", "No.")], skill="Reasoning")),
    adv(ex("u6s3a2", "VH", "O4", "Explain why 'water' is not an element even though it is one pure substance.",
           [("can be broken down / split", ["broken|split|decompos"]), ("into hydrogen and oxygen / two elements", ["hydrogen|oxygen|two element"])],
           "Water can be broken down by a chemical reaction (using electricity) into hydrogen and oxygen, so it is made of two elements chemically joined – it is a compound, not an element.", need=2)),
    adv(nm("u6s3a3", "VH", "O4", "How many atoms are in 5 molecules of P₄?", 20, "atoms")),
    adv(mc("u6s3a4", "VH", "O4", "Trillions of atoms make one cell. What does this tell you about atoms?", ("They are extremely small.", "Correct."), [("They are alive.", "No."), ("They are bigger than cells.", "No."), ("Each is a cell.", "No.")])),
]

# ---------------------------------------------------------------- 6.4
S4_REQ = [
    gd("u6s4r1", "M", "O5", "Metal or non-metal property?", ["Type"],
       [("Shiny", ["Metal"]), ("Conducts electricity well", ["Metal"]), ("Dull", ["Non-metal"]), ("Low melting point (usually)", ["Non-metal"]), ("Can be hammered into shape", ["Metal"])], skill="Data"),
    mc("u6s4r2", "M", "O5", "Where are metals on the Periodic Table?", ("On the left", "Correct."), [("On the right", "Non-metals."), ("Only at the top", "No."), ("In the middle row only", "No.")]),
    mc("u6s4r3", "M", "O5", "Rows of the Periodic Table are called…", "periods", [("groups", "Columns."), ("families only", "No."), ("lines", "No.")]),
    mc("u6s4r4", "H", "O5", "Why do magnesium and calcium have similar properties?", ("They are in the same group.", "Correct."), [("Same period.", "Group decides similar properties."), ("Same colour.", "No."), ("Both are gases.", "No.")]),
    mt("u6s4r5", "M", "O5", "Match the word to its meaning.", [("Ductile", "can be stretched into wires"), ("Malleable", "can be hammered into shape"), ("Conductor", "lets heat or electricity pass"), ("Insulator", "does not let electricity pass easily")]),
    ex("u6s4r6", "H", "O5", "Mendeleev left gaps in his 1869 table. Explain why this was clever.",
       [("gaps for elements not yet discovered", ["not (yet )?discovered|undiscovered|unknown"]), ("predicted their properties / later found", ["predict|later|found"])],
       "He arranged elements by properties and left gaps for elements not yet discovered. He could predict their properties, and when they were found later they fitted the gaps – evidence his table was right.", need=2),
    tb("u6s4r7", "H", "O5", "Data: count the elements.", ["Fact", "Number"], [["Elements known to Mendeleev in 1869", "63"], ["Elements added in 2016", "4"], ["Naturally occurring elements (about)", B(90)]], skill="Data"),
    mc("u6s4r8", "VH", "O5", "Calcium is in group 2, period 4. What does this tell you?", ("It is a metal, on the left, with properties like magnesium.", "Correct."), [("It is a non-metal gas.", "Group 2 is metals."), ("It is in row 2.", "Period 4 is the row."), ("It is the lightest element.", "No.")], skill="Data"),
]
S4_PRAC = [
    mc("u6s4p01", "M", "O5", "Columns of the Periodic Table are…", "groups", [("periods", "Rows."), ("metals", "No."), ("atoms", "No.")]),
    mc("u6s4p02", "M", "O5", "Who is called the father of the Periodic Table?", "Dmitri Mendeleev", [("John Dalton", "Atoms."), ("Marie Curie", "Radioactivity."), ("Einstein", "No.")]),
    mc("u6s4p03", "M", "O5", "Which is a non-metal?", "Sulfur", [("Iron", "Metal."), ("Copper", "Metal."), ("Magnesium", "Metal.")]),
    mc("u6s4p04", "M", "O5", "Which is a metal?", "Calcium", [("Carbon", "Non-metal."), ("Chlorine", "Non-metal."), ("Oxygen", "Non-metal.")]),
    mc("u6s4p05", "H", "O5", "Non-metals are usually…", "dull, with low melting points, and insulators", [("shiny and malleable", "Metals."), ("good conductors", "No."), ("ductile", "No.")]),
    mc("u6s4p06", "H", "O5", "The mass of atoms in the Periodic Table…", "increases across a period and down a group", [("decreases down a group", "Increases."), ("is the same for all", "No."), ("is random", "No.")]),
    mc("u6s4p07", "M", "O5", "Why are copper wires used in electric cables?", "Copper is a metal that conducts electricity well and is ductile.", [("It is a non-metal.", "No."), ("It is cheap plastic.", "No."), ("It is an insulator.", "No.")]),
    mc("u6s4p08", "H", "O5", "Some group 2 metals are used in fireworks because…", "they give bright colours", [("they are non-metals", "No."), ("they do not burn", "No."), ("they are gases", "No.")]),
    mc("u6s4p09", "M", "O5", "About how many elements occur naturally?", "About 90", [("About 10", "Far more."), ("Exactly 63", "Mendeleev's number in 1869."), ("Over 1000", "No.")]),
    mc("u6s4p10", "H", "O5", "Four new elements were added in…", "2016", [("1869", "Mendeleev's table."), ("1800", "No."), ("2000", "No.")]),
    mc("u6s4p11", "H", "O5", "How were the 2016 elements predicted?", "Using the Periodic Table, before they were made", [("By guessing", "No."), ("By finding them in rocks", "They were made."), ("By Mendeleev in 2016", "No.")]),
    mc("u6s4p12", "M", "O5", "A shiny element that conducts heat is probably a…", "metal", [("non-metal", "No."), ("gas", "No."), ("compound", "No.")]),
    mc("u6s4p13", "H", "O5", "Carbon (graphite) conducts electricity but is a non-metal. This shows…", "some elements do not fit the usual pattern", [("carbon is a metal", "No."), ("rules are useless", "No."), ("graphite is a compound", "No.")], skill="Reasoning"),
    od("u6s4p14", "M", "O5", "Order these by when they happened.", ["Mendeleev's table (1869)", "More natural elements discovered", "Scientists make new elements", "Four elements added (2016)"]),
    mc("u6s4p15", "H", "O5", "Elements in the same PERIOD have…", "the same number of electron shells (same row)", [("very similar properties", "That is groups."), ("the same mass", "No."), ("the same symbol", "No.")]),
    mc("u6s4p16", "M", "O5", "Chlorine is on the right of the table, so it is a…", "non-metal", [("metal", "No."), ("compound", "No."), ("mixture", "No.")]),
    mc("u6s4p17", "M", "O5", "Malleable means…", "can be hammered into shape", [("can be stretched into wires", "Ductile."), ("dull", "No."), ("poisonous", "No.")]),
    mc("u6s4p18", "H", "O5", "Mendeleev arranged elements by…", "their properties", [("their colour", "No."), ("alphabetical order", "No."), ("the date found", "No.")]),
]
S4_ADV = [
    adv(ex("u6s4a1", "VH", "O5", "An unknown element is shiny, conducts electricity and has a melting point of 1085 °C. Is it a metal or non-metal? Give two reasons.",
           [("metal", ["metal"]), ("shiny / conducts", ["shiny|conduct"]), ("high melting point", ["high|1085|melting"])],
           "It is a metal: it is shiny, conducts electricity and has a high melting point (1085 °C).", need=2)),
    adv(mc("u6s4a2", "VH", "O5", "Strontium is in the same group as calcium. Predict one property.", ("It is a reactive metal with properties similar to calcium.", "Correct."), [("It is a non-metal gas.", "No."), ("It is unreactive like neon.", "No."), ("It is a liquid like mercury.", "No.")], skill="Reasoning")),
    adv(mc("u6s4a3", "VH", "O5", "Why did Mendeleev's mother travel more than 2400 km?", ("To find a school for him.", "Correct (a fact from his life)."), [("To sell elements.", "No."), ("To see a volcano.", "No."), ("To meet Dalton.", "No.")])),
    adv(nm("u6s4a4", "VH", "O5", "In 1869, 63 elements were known. Today about 118 are known. How many more is that?", 55, "elements")),
]

# ---------------------------------------------------------------- 6.5
S5_REQ = [
    mc("u6s5r1", "M", "O6", "A compound is…", ("two or more elements chemically combined in a reaction", "Correct."), [("two substances just mixed", "A mixture."), ("one element only", "No."), ("any liquid", "No.")]),
    tb("u6s5r2", "H", "O6", "Count the atoms in each compound.", ["Compound", "Formula", "Total atoms"], [["Carbon dioxide", "CO₂", B(3)], ["Methane", "CH₄", B(5)], ["Ammonia", "NH₃", B(4)], ["Hydrogen peroxide", "H₂O₂", B(4)]], skill="Data"),
    mc("u6s5r3", "H", "O6", "Sodium (reactive metal) + chlorine (poisonous gas) → sodium chloride. What does this show?", ("A compound has different properties from its elements.", "Correct – salt is safe to eat."), [("Salt is poisonous.", "No."), ("Compounds keep the properties of elements.", "No."), ("Sodium chloride is a mixture.", "It is a compound.")]),
    nm("u6s5r4", "M", "O6", "3 g of carbon reacts with 8 g of oxygen. Mass of carbon dioxide made?", 11, "g", reason="Mass is conserved: 3 + 8 = 11 g."),
    ex("u6s5r5", "H", "O6", "Explain the law of conservation of mass using atoms.",
       [("atoms are not created or destroyed", ["created|destroyed|lost|made"]), ("atoms are rearranged", ["rearrang"]), ("mass of reactants = mass of products", ["reactant|product|same|equal"])],
       "In a reaction atoms are only rearranged – none are created or destroyed – so the total mass of the reactants equals the total mass of the products.", need=2),
    mc("u6s5r6", "M", "O6", "In 'hydrogen + oxygen → water', the reactants are…", "hydrogen and oxygen", [("water", "Product."), ("water and oxygen", "No."), ("the arrow", "No.")]),
    gd("u6s5r7", "H", "O6", "Name the elements in each compound.", ["Elements"], [("CO₂", ["Carbon, oxygen"]), ("NH₃", ["Nitrogen, hydrogen"]), ("CH₄", ["Carbon, hydrogen"]), ("H₂O", ["Hydrogen, oxygen"])], skill="Data"),
    mc("u6s5r8", "VH", "O6", "Water is H₂O and hydrogen peroxide is H₂O₂. Why are they different substances?", ("The atoms are in a different fixed proportion.", "Correct."), [("They have different elements.", "Same elements."), ("One is a mixture.", "Both compounds."), ("Peroxide has no oxygen.", "It has two.")], skill="Reasoning"),
]
S5_PRAC = [
    mc("u6s5p01", "M", "O6", "Which is a compound?", "Water", [("Oxygen", "Element."), ("Iron", "Element."), ("Air", "Mixture.")]),
    mc("u6s5p02", "M", "O6", "In CO₂, how many oxygen atoms?", "2", [("1", "No."), ("3", "Total atoms."), ("0", "No.")]),
    mc("u6s5p03", "M", "O6", "Solid carbon dioxide is called…", "dry ice", [("snow", "No."), ("frost", "No."), ("glass", "No.")]),
    mc("u6s5p04", "M", "O6", "Formula of methane?", "CH₄", [("CO₂", "Carbon dioxide."), ("NH₃", "Ammonia."), ("H₂O", "Water.")]),
    mc("u6s5p05", "M", "O6", "Hydrogen peroxide is used as…", "a mild antiseptic", [("a fuel for cars", "No."), ("table salt", "No."), ("a fertiliser", "No.")]),
    mc("u6s5p06", "H", "O6", "Can you separate a compound into its elements by picking them apart?", "No – they are chemically combined.", [("Yes, with tweezers.", "No."), ("Yes, with a magnet.", "Works for mixtures, not compounds."), ("Yes, by filtering.", "No.")]),
    mc("u6s5p07", "M", "O6", "In a word equation, products are written…", "on the right of the arrow", [("on the left", "Reactants."), ("above the arrow", "Conditions."), ("nowhere", "No.")]),
    nm("u6s5p08", "H", "O6", "12 g of magnesium reacts with 8 g of oxygen. Mass of magnesium oxide?", 20, "g"),
    nm("u6s5p09", "H", "O6", "Iron (56 g) + sulfur makes 88 g of iron sulfide. Mass of sulfur?", 32, "g"),
    ms("u6s5p10", "M", "O6", "Select ALL compounds.", ["Vinegar (acetic acid)", "Aspirin", "Baking soda"], [("Neon", "Element."), ("Sulfur", "Element.")]),
    mc("u6s5p11", "H", "O6", "Reactions that form compounds often need…", "heat, light or electricity", [("magnets", "No."), ("darkness", "No."), ("nothing", "Often energy is needed.")]),
    mc("u6s5p12", "H", "O6", "How many hydrogen atoms in NH₃?", "3", [("1", "No."), ("4", "Total."), ("0", "No.")]),
    mc("u6s5p13", "M", "O6", "Table salt's chemical name is…", "sodium chloride", [("sodium", "Element."), ("chlorine", "Element."), ("calcium carbonate", "No.")]),
    mc("u6s5p14", "H", "O6", "Why are millions of compounds possible?", "Over 100 elements can combine in many proportions.", [("There are millions of elements.", "About 118."), ("Compounds are mixtures.", "No."), ("Atoms change shape.", "No.")]),
    mc("u6s5p15", "H", "O6", "In a closed flask, a reaction happens. The total mass…", "stays the same", [("increases", "No."), ("decreases", "No."), ("becomes zero", "No.")]),
    mc("u6s5p16", "H", "O6", "A burning candle seems to lose mass. Why doesn't this break conservation of mass?", "Gases produced escape into the air.", [("Mass is destroyed.", "No."), ("Candles are not matter.", "No."), ("The law is wrong.", "No.")], skill="Reasoning"),
    od("u6s5p17", "M", "O6", "Order: making salt.", ["Sodium and chlorine are the reactants", "They react (often with heat)", "Atoms are rearranged", "Sodium chloride is the product"]),
    mc("u6s5p18", "H", "O6", "C with no number in CO₂ means…", "one carbon atom", [("no carbon", "No."), ("two carbon atoms", "No."), ("carbon is optional", "No.")]),
]
S5_ADV = [
    adv(nm("u6s5a1", "VH", "O6", "Glucose is C₆H₁₂O₆. How many atoms in one molecule?", 24, "atoms")),
    adv(ex("u6s5a2", "VH", "O6", "Magnesium ribbon (2.4 g) burns in air to give 4.0 g of white powder. Explain why the mass increased.",
           [("magnesium combined with oxygen", ["oxygen"]), ("oxygen from air added mass", ["air|added|gain"]), ("mass conserved overall", ["conserv|not created|total"])],
           "The magnesium reacted with oxygen from the air to form magnesium oxide. The extra 1.6 g is the mass of oxygen that combined – mass is still conserved overall.", need=2)),
    adv(mc("u6s5a3", "VH", "O6", "Carbon monoxide is CO; carbon dioxide is CO₂. Which statement is true?", ("They are different compounds with different properties.", "Correct (CO is very toxic)."), [("They are the same compound.", "Different proportions."), ("CO is an element.", "No."), ("CO₂ is a mixture.", "No.")], skill="Reasoning")),
    adv(nm("u6s5a4", "VH", "O6", "How many oxygen atoms in 3 molecules of CO₂?", 6, "atoms")),
]

# ---------------------------------------------------------------- 6.6
S6_REQ = [
    mc("u6s6r1", "M", "O7", "A mixture is…", ("two or more substances that are not chemically combined", "Correct."), [("elements joined in a reaction", "Compound."), ("one pure substance", "No."), ("always a liquid", "No.")]),
    gd("u6s6r2", "H", "O7", "Element, compound or mixture?", ["Type"],
       [("Oxygen", ["Element"]), ("Water", ["Compound"]), ("Air", ["Mixture"]), ("Sodium chloride", ["Compound"]), ("Soil", ["Mixture"]), ("Copper", ["Element"])], skill="Data"),
    tb("u6s6r3", "H", "O7", "Data: composition of air. Complete the table.", ["Gas", "Percentage"], [["Nitrogen", "78"], ["Oxygen", "21"], ["Other gases", B(1)]], skill="Data"),
    mc("u6s6r4", "M", "O7", "An alloy is…", ("a mixture of a metal with other metals or small amounts of non-metals", "Correct."), [("a pure metal", "No."), ("a compound of metals", "It is a mixture."), ("a non-metal", "No.")]),
    ex("u6s6r5", "H", "O7", "Give TWO differences between a compound and a mixture.",
       [("compound chemically combined / mixture not", ["chemically|combined|joined|react"]), ("fixed proportion vs no fixed composition", ["fixed|proportion|ratio|composition"]), ("compound different properties / mixture keeps properties", ["properties"]), ("mixture separated physically", ["separat"])],
       "A compound's elements are chemically combined in a fixed proportion and it has new properties. A mixture's parts are not joined, have no fixed composition, keep their own properties and can be separated physically.", need=2),
    mc("u6s6r6", "H", "O7", "Why is stainless steel good for cutlery?", ("It does not rust and is hard.", "Correct – about 11% chromium and 1% carbon added to iron."), [("It is soft and bendy.", "No."), ("It is pure iron.", "It is an alloy."), ("It melts easily.", "No.")]),
    mc("u6s6r7", "M", "O7", "How can you get sugar back from sugar water?", ("Evaporate the water.", "Correct – a mixture can be separated physically."), [("Filter it.", "Dissolved sugar passes through."), ("Use a magnet.", "No."), ("You cannot.", "You can.")]),
    mc("u6s6r8", "VH", "O7", "A liquid boils over a range of temperatures (78–96 °C). It is most likely…", ("a mixture", "Correct – mixtures have no fixed boiling point."), [("a pure element", "Fixed point."), ("a pure compound", "Fixed point."), ("an atom", "No.")], skill="Data"),
]
S6_PRAC = [
    mc("u6s6p01", "M", "O7", "Brass is used for…", "trumpets and trophies", [("cutlery mainly", "Stainless steel."), ("wires in buildings", "Steel/copper."), ("food", "No.")]),
    mc("u6s6p02", "M", "O7", "Steel is used for…", "wires, buildings and nails", [("trumpets", "Brass."), ("drinking", "No."), ("signs that glow", "Neon.")]),
    mc("u6s6p03", "M", "O7", "Alloys are usually…", "stronger and harder than pure metals", [("softer", "No."), ("non-metals", "No."), ("compounds", "Mixtures.")]),
    mc("u6s6p04", "M", "O7", "Soil is a mixture of…", "sand, clay, organic matter, water and air", [("only sand", "No."), ("only water", "No."), ("only one element", "No.")]),
    mc("u6s6p05", "H", "O7", "Why does soil differ from place to place?", "Mixtures have no fixed composition.", [("Soil is a compound.", "No."), ("Soil is an element.", "No."), ("It does not differ.", "It does.")]),
    mc("u6s6p06", "M", "O7", "Air is about ___% oxygen.", "21", [("78", "Nitrogen."), ("1", "Other gases."), ("50", "No.")]),
    mc("u6s6p07", "H", "O7", "Which have fixed melting and boiling points?", "Elements and compounds (pure substances)", [("Mixtures", "No fixed points."), ("Alloys", "Mixtures."), ("Soil", "Mixture.")]),
    mc("u6s6p08", "H", "O7", "A mixture of iron filings and sulfur can be separated with…", "a magnet", [("heat", "That makes iron sulfide."), ("water only", "No."), ("nothing", "A magnet works.")]),
    mc("u6s6p09", "H", "O7", "When a sodium and chlorine mixture is heated it…", "reacts to form the compound sodium chloride", [("stays a mixture", "It reacts."), ("becomes pure sodium", "No."), ("becomes air", "No.")]),
    mc("u6s6p10", "M", "O7", "Stainless steel is mostly…", "iron", [("chromium", "About 11%."), ("carbon", "About 1%."), ("copper", "No.")]),
    mc("u6s6p11", "H", "O7", "In a model of a mixture, the particles are…", "different, and not joined", [("all the same", "Element."), ("joined in a fixed ratio", "Compound."), ("invisible", "No.")]),
    mc("u6s6p12", "M", "O7", "Is sugar dissolving in water a chemical reaction?", "No – it makes a mixture (solution).", [("Yes – a new substance forms.", "No."), ("Yes – it gets hot.", "No."), ("Only in cold water.", "No.")]),
    gd("u6s6p13", "M", "O7", "Pure substance or mixture?", ["Type"], [("Distilled water", ["Pure"]), ("Sea water", ["Mixture"]), ("Gold", ["Pure"]), ("Bronze", ["Mixture"])], skill="Data"),
    mc("u6s6p14", "H", "O7", "Why are pure metals often mixed to make alloys?", "To make them stronger and harder or stop rusting", [("To make them softer", "Usually harder."), ("To make them non-metals", "No."), ("To change their symbol", "No.")]),
    mc("u6s6p15", "H", "O7", "Bronze is an alloy of…", "copper and tin", [("iron and carbon", "Steel."), ("copper and zinc", "Brass."), ("gold and silver", "No.")]),
    mc("u6s6p16", "M", "O7", "Which is NOT a mixture?", "Carbon dioxide", [("Air", "Mixture."), ("Soil", "Mixture."), ("Salt water", "Mixture.")]),
    nm("u6s6p17", "H", "O7", "In 500 cm³ of air, about how many cm³ is nitrogen (78%)?", 390, "cm³"),
    mc("u6s6p18", "H", "O7", "Mixtures keep…", "the properties of their parts", [("new properties", "Compounds."), ("no properties", "No."), ("fixed boiling points", "No.")]),
]
S6_ADV = [
    adv(ex("u6s6a1", "VH", "O7", "Use the particle model to explain why an alloy is harder than the pure metal.",
           [("different-sized atoms", ["different size|bigger|smaller"]), ("layers cannot slide easily", ["layer|slide|slip"])],
           "In a pure metal the atoms are the same size in neat layers that slide over each other. In an alloy, atoms of different sizes disrupt the layers so they cannot slide easily, making it harder.", need=2)),
    adv(mc("u6s6a2", "VH", "O7", "Gold jewellery is often an alloy with copper or silver. Why?", ("Pure gold is too soft; the alloy is harder and lasts longer.", "Correct."), [("Pure gold rusts.", "Gold does not rust."), ("To make it heavier.", "Not the reason."), ("Gold is a non-metal.", "No.")], skill="Reasoning")),
    adv(nm("u6s6a3", "VH", "O7", "A 200 g stainless steel spoon is 11% chromium. Mass of chromium?", 22, "g")),
    adv(mc("u6s6a4", "VH", "O7", "Which test best shows that a liquid is pure water?", ("It boils at exactly 100 °C and freezes at exactly 0 °C.", "Correct."), [("It is clear.", "Salt water is clear too."), ("It is wet.", "No."), ("It has no smell.", "Not enough.")], skill="Reasoning")),
]

POOLS = {"6.1": (S1_REQ, S1_PRAC, S1_ADV), "6.2": (S2_REQ, S2_PRAC, S2_ADV), "6.3": (S3_REQ, S3_PRAC, S3_ADV),
         "6.4": (S4_REQ, S4_PRAC, S4_ADV), "6.5": (S5_REQ, S5_PRAC, S5_ADV), "6.6": (S6_REQ, S6_PRAC, S6_ADV)}

STOPS = {
    "6.1": [stop("u6v1a", "reaches the brakes straight away", mc("u6v1a_q", "M", "O1", "Which state has neither a fixed shape nor a fixed volume?", "Gas", [("Solid", "No."), ("Liquid", "Fixed volume."), ("None", "Gas.")])),
            stop("u6v1b", "which is why gases can be compressed", mc("u6v1b_q", "M", "O1", "Particles in a liquid…", "touch and move around each other", [("vibrate in fixed places", "Solid."), ("are far apart", "Gas."), ("do not move", "No.")])),
            stop("u6v1c", "Models keep changing as new evidence appears", mc("u6v1c_q", "H", "O2", "Brownian motion is evidence that…", "particles in liquids are moving", [("pollen is alive", "No."), ("atoms do not exist", "No."), ("water is solid", "No.")]))],
    "6.2": [stop("u6v2a", "so no new substance is made", mc("u6v2a_q", "M", "O3", "Gas → liquid is called…", "condensation", [("evaporation", "No."), ("melting", "No."), ("freezing", "No.")])),
            stop("u6v2b", "is the same as its melting point", mc("u6v2b_q", "H", "O3", "At its melting point, a solid's particles…", "have enough energy to overcome the forces holding them", [("stop moving", "No."), ("become smaller", "No."), ("turn into a new substance", "No.")])),
            stop("u6v2c", "the boiling point of water", mc("u6v2c_q", "H", "O3", "The flat part of a heating graph at 0 °C shows…", "ice melting", [("water boiling", "100 °C."), ("the burner off", "No."), ("condensation", "No.")]))],
    "6.3": [stop("u6v3a", "Oxygen and hydrogen are elements; water is not", mc("u6v3a_q", "M", "O4", "An element cannot be…", "broken down into simpler substances by chemical reactions", [("seen", "No."), ("named", "No."), ("used", "No.")])),
            stop("u6v3b", "Ag for silver, from argentum", mc("u6v3b_q", "M", "O4", "Symbol for iron?", "Fe", [("Ir", "Iridium."), ("I", "Iodine."), ("In", "Indium.")])),
            stop("u6v3c", "shows there are two atoms", mc("u6v3c_q", "H", "O4", "How many atoms in an oxygen molecule, O₂?", "2", [("1", "No."), ("3", "Ozone is O₃."), ("8", "Sulfur.")]))],
    "6.4": [stop("u6v4a", "Sulfur, carbon and chlorine are non-metals", mc("u6v4a_q", "M", "O5", "Metals are…", "shiny and good conductors", [("dull insulators", "Non-metals."), ("always gases", "No."), ("brittle", "Non-metals.")])),
            stop("u6v4b", "so calcium is a metal", mc("u6v4b_q", "M", "O5", "Columns in the Periodic Table are called…", "groups", [("periods", "Rows."), ("formulae", "No."), ("states", "No.")])),
            stop("u6v4c", "before they were ever made", mc("u6v4c_q", "H", "O5", "Why did Mendeleev leave gaps?", "For elements not yet discovered", [("He ran out of ink", "No."), ("To look neat", "No."), ("For compounds", "No.")]))],
    "6.5": [stop("u6v5a", "cannot be separated just by picking them apart", mc("u6v5a_q", "M", "O6", "Salt is a…", "compound", [("element", "No."), ("mixture", "No."), ("metal", "No.")])),
            stop("u6v5b", "its formula is H2O2", mc("u6v5b_q", "H", "O6", "NH₃ contains…", "one nitrogen and three hydrogen atoms", [("three nitrogen atoms", "No."), ("one hydrogen atom", "No."), ("oxygen", "No.")])),
            stop("u6v5c", "the law of conservation of mass", nm("u6v5c_q", "H", "O6", "3 g carbon + 8 g oxygen → ? g carbon dioxide", 11, "g"))],
    "6.6": [stop("u6v6a", "no fixed melting or boiling point", mc("u6v6a_q", "M", "O7", "Air is a…", "mixture", [("compound", "No."), ("element", "No."), ("solid", "No.")])),
            stop("u6v6b", "perfect for cutlery", mc("u6v6b_q", "M", "O7", "An alloy is a…", "mixture containing a metal", [("pure element", "No."), ("compound", "No."), ("gas", "No.")])),
            stop("u6v6c", "they react to form sodium chloride", mc("u6v6c_q", "H", "O7", "Which can be separated by physical means?", "A mixture", [("A compound", "Needs a reaction."), ("An element", "No."), ("An atom", "No.")]))],
}

MINDMAP = {"id": "root", "t": "Materials", "sec": None, "kids": [
    {"id": "states", "t": "States of matter", "d": "Solid • liquid • gas – explained by the particle model.", "obj": "O1", "sec": "6.1"},
    {"id": "model", "t": "Particle model", "d": "Democritus → Dalton → Brown → Einstein/Perrin. Useful but simplified.", "obj": "O2", "sec": "6.1"},
    {"id": "change", "t": "Changes of state", "d": "Melting • freezing • evaporation/boiling • condensation. Flat lines on heating graphs.", "obj": "O3", "sec": "6.2"},
    {"id": "elem", "t": "Elements & atoms", "d": "Cannot be broken down • symbols (Na, Fe, Cu…) • molecules O₂, P₄, S₈.", "obj": "O4", "sec": "6.3"},
    {"id": "pt", "t": "Periodic Table", "d": "Metals left, non-metals right • periods (rows), groups (columns) • Mendeleev.", "obj": "O5", "sec": "6.4"},
    {"id": "comp", "t": "Compounds", "d": "Elements chemically combined, fixed proportion • CO₂, CH₄, NH₃ • mass is conserved.", "obj": "O6", "sec": "6.5"},
    {"id": "mix", "t": "Mixtures & alloys", "d": "Not combined, no fixed composition • air, soil • steel, brass, bronze.", "obj": "O7", "sec": "6.6"},
]}
