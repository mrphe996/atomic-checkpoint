# -*- coding: utf-8 -*-
"""Concept maps for Stage 7 (Atomic's own wording and layout). Written by the Atomic teaching team.
Each map: nodes on a 5-column grid (col 0-4, row 0..), links with a short linking phrase.
k: root (the unit idea) | key (main branch) | node (concept) | info (short explanation, bullet lines in d)
s: the section the node is taught in – tapping a node opens that section's video clip and questions."""
import json, os

def N(id, t, s, col, row, k='node', d=None):
    return {"id": id, "t": t, "s": s, "c": col, "r": row, "k": k, **({"d": d} if d else {})}

MAPS = {}

MAPS[1] = {"nodes": [
    N("sci", "Science", "1.1", 2, 0, "root"),
    N("know", "Explaining the world", "1.1", 0, 1, "key", ["Builds knowledge that explains what we observe"]),
    N("tech", "Technology", "1.4", 4, 1, "key"),
    N("tech_i", "Benefits and problems", "1.4", 4, 2, "info", ["Improves lives", "Can harm the environment", "Has limits"]),
    N("att", "Attitudes", "1.1", 0, 3, "key"),
    N("att_i", "Scientific attitudes", "1.1", 0, 4, "info", ["Curious and open-minded", "Patient and fair", "Honest, with healthy doubt"]),
    N("skills", "Enquiry skills", "1.2", 2, 3, "key"),
    N("skills_i", "Testing ideas", "1.2", 2, 4, "info", ["Ask a question", "Make a hypothesis and prediction", "Plan a fair test", "Measure, analyse, conclude", "Evaluate"]),
    N("lab", "Working in the lab", "1.3", 4, 3, "key"),
    N("lab_i", "Staying safe", "1.3", 4, 4, "info", ["Follow the safety rules", "Read hazard symbols", "Choose suitable apparatus"]),
    N("collab", "Working together", "1.1", 2, 5, "node"),
    N("collab_i", "Sharing science", "1.1", 2, 6, "info", ["Peer review", "Publishing results"]),
  ], "links": [["sci", "know", "builds"], ["sci", "tech", "is used in"], ["tech", "tech_i", "brings"], ["sci", "att", "needs"], ["sci", "skills", "is done through"],
               ["skills", "lab", "used when"], ["att", "att_i", ""], ["skills", "skills_i", ""], ["lab", "lab_i", "means"], ["skills", "collab", "improved by"], ["collab", "collab_i", ""]]}

MAPS[2] = {"nodes": [
    N("pq", "Physical quantities", "2.1", 1, 0, "root"),
    N("meas", "Measurements", "2.2", 3, 0, "key"),
    N("acc", "Accurate", "2.2", 2, 1, "node", ["Close to the true value"]),
    N("pre", "Precise", "2.2", 4, 1, "node", ["Repeats are close together"]),
    N("len", "Length", "2.2", 0, 2, "key"), N("len_i", "Units and tools", "2.2", 0, 3, "info", ["mm, cm, m, km", "Ruler, tape measure"]),
    N("area", "Area", "2.3", 1, 2, "key"), N("area_i", "Units and method", "2.3", 1, 3, "info", ["cm², m²", "Calculate: base × height"]),
    N("vol", "Volume", "2.4", 2, 2, "key"), N("vol_i", "Units and tools", "2.4", 2, 3, "info", ["ml, l, cm³, m³", "Measuring cylinder", "Displacement for odd shapes"]),
    N("mass", "Mass", "2.5", 3, 2, "key"), N("mass_i", "Units and tools", "2.5", 3, 3, "info", ["g, kg", "Balance (use tare)"]),
    N("time", "Time", "2.6", 4, 2, "key"), N("time_i", "Units and tools", "2.6", 4, 3, "info", ["s, min, h", "Stopwatch, clock, timer"]),
  ], "links": [["pq", "meas", "described by"], ["meas", "acc", "can be"], ["meas", "pre", "can be"], ["pq", "len", "e.g."], ["pq", "area", "e.g."], ["pq", "vol", "e.g."], ["pq", "mass", "e.g."], ["pq", "time", "e.g."],
               ["len", "len_i", ""], ["area", "area_i", ""], ["vol", "vol_i", ""], ["mass", "mass_i", ""], ["time", "time_i", ""]]}

MAPS[3] = {"nodes": [
    N("uni", "Unicellular organisms", "3.1", 0, 0, "key", ["One cell only", "e.g. bacteria, yeast, amoeba"]),
    N("multi", "Multicellular organisms", "3.1", 4, 0, "key", ["Many cells", "e.g. plants, animals"]),
    N("cells", "Cells", "3.1", 2, 1, "root"),
    N("theory", "Cell theory", "3.1", 0, 2, "node", ["All living things are made of cells", "Cells are the basic unit of life", "New cells come from existing cells"]),
    N("tis", "Tissues", "3.4", 4, 2, "node"), N("org", "Organs", "3.4", 4, 3, "node"), N("sys", "Organ systems", "3.4", 4, 4, "node"), N("orgm", "Organism", "3.4", 4, 5, "node"),
    N("plant", "Plant cells", "3.2", 1, 4, "key", ["Nucleus, membrane, cytoplasm, mitochondria", "Cell wall, chloroplasts, large vacuole"]),
    N("animal", "Animal cells", "3.2", 2, 5, "key", ["Nucleus, membrane, cytoplasm, mitochondria"]),
    N("pspec", "Specialised plant cells", "3.3", 0, 6, "info", ["Palisade cell", "Root hair cell"]),
    N("aspec", "Specialised animal cells", "3.3", 2, 6, "info", ["Red blood cell", "Nerve cell (neurone)", "Ciliated cell"]),
  ], "links": [["uni", "cells", "made of"], ["multi", "cells", "made of"], ["cells", "theory", "explained by"], ["cells", "tis", "group into"], ["tis", "org", "make"], ["org", "sys", "work together in"], ["sys", "orgm", "make an"],
               ["cells", "plant", "include"], ["cells", "animal", "include"], ["plant", "pspec", "specialise as"], ["animal", "aspec", "specialise as"]]}

MAPS[4] = {"nodes": [
    N("living", "Living things", "4.1", 2, 0, "root"),
    N("chars", "Seven characteristics", "4.1", 0, 1, "key", ["Movement, Respiration, Sensitivity", "Growth, Reproduction", "Excretion, Nutrition"]),
    N("virus", "Viruses", "4.2", 0, 3, "node", ["Show only some of the seven", "Copy themselves inside living cells"]),
    N("class", "Classification", "4.3", 4, 1, "key"),
    N("species", "Species", "4.3", 4, 2, "node", ["Can breed to give fertile offspring", "Two-part scientific name, e.g. Homo sapiens"]),
    N("groups", "Plant and animal groups", "4.4", 3, 3, "node", ["Vertebrates and invertebrates", "Flowering and non-flowering plants"]),
    N("keys", "Dichotomous keys", "4.5", 2, 2, "key"),
    N("branch", "Branching key", "4.5", 1, 4, "info", ["A diagram that splits in two at each step"]),
    N("paired", "Paired statements", "4.5", 3, 4, "info", ["Numbered pairs: choose a or b", "Go to the next step"]),
  ], "links": [["living", "chars", "show"], ["virus", "chars", "lack some"], ["living", "class", "sorted by"], ["class", "species", "down to"], ["class", "groups", "into"], ["living", "keys", "identified with"],
               ["keys", "branch", "drawn as"], ["keys", "paired", "or written as"]]}

MAPS[5] = {"nodes": [
    N("micro", "Microorganisms", "5.1", 1, 0, "root", ["Bacteria, fungi, protists"]),
    N("chains", "Food chains", "5.2", 4, 0, "key", ["One path of energy transfer"]),
    N("webs", "Food webs", "5.2", 4, 2, "key", ["Many linked food chains"]),
    N("decomp", "Decomposers", "5.1", 1, 2, "key", ["Break down dead matter and waste", "Return nutrients to the soil"]),
    N("prod", "Producers", "5.2", 0, 4, "node", ["Make their own food (plants)"]),
    N("prim", "Primary consumers", "5.2", 1, 4, "node", ["Herbivores eat producers"]),
    N("sec", "Secondary consumers", "5.2", 2, 4, "node", ["Eat other animals"]),
    N("ter", "Tertiary consumers", "5.2", 3, 4, "node"),
    N("arrow", "Arrows", "5.2", 4, 4, "info", ["Point the way energy flows", "From the food to the eater"]),
  ], "links": [["micro", "decomp", "include"], ["micro", "chains", "are vital in"], ["chains", "webs", "combine into"], ["prod", "prim", "eaten by"], ["prim", "sec", "eaten by"], ["sec", "ter", "eaten by"],
               ["decomp", "prod", "feed nutrients to"], ["webs", "arrow", "use"]]}

MAPS[6] = {"nodes": [
    N("matter", "Matter", "6.1", 2, 0, "root"),
    N("pmodel", "Particle model", "6.1", 0, 0, "key"),
    N("solid", "Solid", "6.1", 0, 1, "node", ["Fixed shape and volume", "Particles packed, vibrate in place"]),
    N("liquid", "Liquid", "6.1", 2, 1, "node", ["Fixed volume, takes container shape", "Particles touch, slide past"]),
    N("gas", "Gas", "6.1", 4, 1, "node", ["Fills its container, compressible", "Particles far apart, fast"]),
    N("change", "Changes of state", "6.2", 2, 2, "info", ["Melting, freezing", "Evaporating, condensing"]),
    N("atoms", "Atoms", "6.3", 2, 3, "key"), N("mol", "Molecules", "6.3", 4, 3, "node", ["Atoms joined together"]),
    N("elem", "Elements", "6.4", 0, 4, "key", ["One type of atom", "Cannot be split chemically"]),
    N("pt", "Periodic Table", "6.4", 0, 5, "info", ["Metals on the left", "Non-metals on the right"]),
    N("comp", "Compounds", "6.5", 2, 5, "key", ["Elements joined in a fixed ratio", "New properties"]),
    N("mix", "Mixtures", "6.6", 4, 5, "key", ["Not chemically joined", "Separated physically", "e.g. alloys, air"]),
  ], "links": [["matter", "pmodel", "explained by"], ["matter", "solid", "can be"], ["matter", "liquid", "can be"], ["matter", "gas", "can be"], ["liquid", "change", ""], ["matter", "atoms", "is made of"],
               ["atoms", "mol", "join to form"], ["atoms", "elem", "one type in"], ["elem", "pt", "listed in"], ["elem", "comp", "react to form"], ["comp", "mix", "or are mixed in"]]}

MAPS[7] = {"nodes": [
    N("props", "Properties of materials", "7.1", 2, 0, "root"),
    N("phys", "Physical properties", "7.1", 1, 1, "key", ["Strength, hardness, flexibility", "Ductile, malleable", "Melting and boiling points", "Conductivity, density"]),
    N("chem", "Chemical properties", "7.2", 3, 1, "key", ["Reactivity, flammability", "pH, corrosiveness, toxicity"]),
    N("metals", "Metals", "7.3", 1, 3, "node", ["Shiny, malleable, conduct"]),
    N("nonm", "Non-metals", "7.3", 0, 3, "node", ["Dull, brittle insulators", "Exceptions: graphite, diamond"]),
    N("alloys", "Alloys", "7.4", 3, 3, "key", ["Mixed atom sizes stop layers sliding", "Harder and stronger", "Can be designed for a job"]),
  ], "links": [["props", "phys", "include"], ["props", "chem", "include"], ["phys", "metals", "differ for"], ["phys", "nonm", "differ for"], ["metals", "alloys", "mixed to make"]]}

MAPS[8] = {"nodes": [
    N("acids", "Acids", "8.1", 1, 0, "key", ["Sour, corrosive, conduct", "Blue litmus → red", "+ carbonate → CO₂", "+ metal → hydrogen"]),
    N("alk", "Alkalis", "8.2", 3, 0, "key", ["Bitter, soapy, conduct", "Red litmus → blue"]),
    N("neut", "Neutralisation", "8.4", 2, 1, "root", ["Acid + alkali → salt + water"]),
    N("ph", "pH scale", "8.3", 2, 2, "key", ["0–6 acidic, 7 neutral, 8–14 alkaline"]),
    N("ind", "Indicators", "8.3", 2, 3, "node", ["Litmus", "Universal Indicator", "Red cabbage"]),
    N("uses", "Uses of neutralisation", "8.4", 4, 2, "info", ["Antacids", "Liming soil and lakes", "Cleaning power-station gases"]),
  ], "links": [["acids", "neut", "react in"], ["alk", "neut", "react in"], ["neut", "ph", "measured on"], ["ph", "ind", "shown by"], ["neut", "uses", "used in"]]}

MAPS[9] = {"nodes": [
    N("useful", "Useful reactions", "9.3", 0, 0, "info", ["Burning fuels, respiration", "Photosynthesis, digestion"]),
    N("harm", "Harmful reactions", "9.3", 4, 0, "info", ["Acid rain damage", "Rusting"]),
    N("cr", "Chemical reactions", "9.1", 2, 1, "root"),
    N("feat", "Key features", "9.1", 0, 2, "info", ["New substances form", "Hard to reverse", "Mass is conserved"]),
    N("weq", "Word equations", "9.2", 3, 2, "key", ["Reactants → products"]),
    N("pm", "Particle models", "9.2", 4, 2, "node", ["Atoms rearrange"]),
    N("col", "Colour change", "9.4", 0, 4, "node"),
    N("ppt", "Precipitate", "9.4", 1, 4, "node", ["Solid forms in a solution"]),
    N("gas", "Gas given off", "9.4", 2, 4, "node"),
    N("loss", "Reactants used up", "9.4", 3, 4, "node"),
    N("tests", "Gas tests", "9.4", 2, 5, "info", ["Hydrogen: squeaky pop", "CO₂: limewater turns milky", "Oxygen: relights a glowing splint"]),
  ], "links": [["cr", "useful", "can be"], ["cr", "harm", "can be"], ["cr", "feat", "have"], ["cr", "weq", "written as"], ["cr", "pm", "drawn as"], ["cr", "col", "spotted by"], ["cr", "ppt", ""], ["cr", "gas", ""], ["cr", "loss", ""], ["gas", "tests", "identified by"]]}

MAPS[10] = {"nodes": [
    N("fd", "Force diagrams", "10.1", 2, 0, "key", ["Arrow direction = direction of force", "Arrow length = size"]),
    N("size", "Measuring force", "10.1", 4, 0, "info", ["Force meter", "Unit: newton (N)"]),
    N("forces", "Forces", "10.1", 2, 1, "root", ["Pushes and pulls"]),
    N("air", "Air resistance", "10.4", 0, 2, "key", ["Opposes motion through air"]),
    N("vac", "Vacuum", "10.4", 0, 3, "node", ["No particles, so no air resistance"]),
    N("grav", "Gravity", "10.2", 3, 2, "key", ["Attraction between masses"]),
    N("dep", "Depends on", "10.2", 2, 3, "info", ["Bigger masses → stronger", "Further apart → weaker"]),
    N("weight", "Weight", "10.3", 4, 3, "node", ["Pull of gravity, in N", "Mass stays the same (kg)"]),
  ], "links": [["forces", "fd", "shown in"], ["fd", "size", "size from"], ["forces", "air", "include"], ["forces", "grav", "include"], ["air", "vac", "absent in a"], ["grav", "dep", "strength"], ["grav", "weight", "gives objects"]]}

MAPS[11] = {"nodes": [
    N("energy", "Energy", "11.1", 2, 0, "root", ["Cannot be made or destroyed"]),
    N("stores", "Energy stores", "11.1", 0, 1, "key"),
    N("trans", "Energy transfers", "11.2", 3, 1, "key", ["Mechanically, electrically", "By heating, by waves"]),
    N("k", "Kinetic", "11.1", 0, 2, "node", ["Moving objects"]), N("gpe", "Gravitational potential", "11.1", 1, 2, "node", ["Raised objects"]),
    N("ch", "Chemical", "11.1", 0, 3, "node", ["Food, fuels, cells"]), N("el", "Elastic potential", "11.1", 1, 3, "node", ["Stretched or squashed objects"]),
    N("nuc", "Nuclear", "11.1", 0, 4, "node", ["Nucleus of an atom"]), N("th", "Thermal", "11.1", 1, 4, "node", ["Vibrating particles"]),
    N("diss", "Dissipation", "11.3", 3, 2, "info", ["Some energy spreads out and is wasted", "Efficiency = useful share"]),
    N("sound", "Sound", "11.4", 4, 3, "key", ["Vibrations passed between particles", "Cannot cross a vacuum", "Reflected sound = echo"]),
  ], "links": [["energy", "stores", "kept in"], ["energy", "trans", "moves by"], ["stores", "trans", "shifted between"], ["stores", "k", "e.g."], ["stores", "gpe", "e.g."], ["k", "ch", ""], ["gpe", "el", ""], ["ch", "nuc", ""], ["el", "th", ""],
               ["trans", "diss", "always some"], ["trans", "sound", "waves include"]]}

MAPS[12] = {"nodes": [
    N("elec", "Electricity", "12.1", 1, 0, "root"),
    N("cond", "Conductors", "12.1", 3, 0, "key", ["e.g. metals", "Let electrons flow"]),
    N("ins", "Insulators", "12.1", 4, 1, "key", ["e.g. plastic, glass, rubber", "Stop electrons flowing"]),
    N("flow", "Flow of electrons", "12.1", 1, 1, "node"),
    N("cur", "Electric current", "12.3", 1, 2, "key"),
    N("amm", "Ammeter", "12.3", 0, 3, "node", ["In series", "Unit: ampere (A)"]),
    N("circ", "Circuits", "12.2", 1, 3, "node", ["Closed loop = current flows"]),
    N("diag", "Circuit diagrams", "12.2", 1, 4, "info", ["Symbols: cell, lamp, switch", "wire, buzzer, ammeter"]),
    N("cells", "More cells in series", "12.4", 3, 3, "node", ["More current, brighter lamp"]),
    N("lamps", "More lamps in series", "12.4", 4, 3, "node", ["More resistance, less current"]),
  ], "links": [["elec", "cond", "passes through"], ["elec", "ins", "blocked by"], ["elec", "flow", "is a"], ["flow", "cur", "is called"], ["cur", "amm", "measured with"], ["cur", "circ", "flows in"], ["circ", "diag", "drawn as"], ["cur", "cells", "changed by"], ["cur", "lamps", "changed by"]]}

MAPS[13] = {"nodes": [
    N("earth", "The Earth", "13.1", 2, 0, "root"),
    N("struct", "Layers", "13.1", 0, 1, "key", ["Crust, mantle", "Outer core, inner core"]),
    N("plates", "Tectonic plates", "13.1", 0, 2, "node", ["Move a few cm a year"]),
    N("bound", "Plate boundaries", "13.2", 0, 3, "node"),
    N("tb", "Transform", "13.2", 0, 4, "info", ["→ earthquakes"]), N("db", "Divergent", "13.2", 1, 4, "info", ["→ volcanoes"]), N("cb", "Convergent", "13.2", 2, 4, "info", ["→ fold mountains"]),
    N("atm", "Atmosphere", "13.3", 2, 1, "key"),
    N("air", "Air", "13.3", 2, 2, "node", ["78% nitrogen, 21% oxygen", "1% carbon dioxide and others"]),
    N("chg", "Changes in air", "13.3", 3, 3, "info", ["Volcanoes and respiration", "Pollution from fossil fuels"]),
    N("wv", "Water vapour", "13.4", 4, 1, "node"),
    N("wc", "Water cycle", "13.4", 4, 2, "key", ["Evaporation → condensation", "→ precipitation → collection"]),
  ], "links": [["earth", "struct", "has"], ["struct", "plates", "crust split into"], ["plates", "bound", "meet at"], ["bound", "tb", ""], ["bound", "db", ""], ["bound", "cb", ""], ["earth", "atm", "surrounded by"], ["atm", "air", "made of"],
               ["air", "chg", "changed by"], ["atm", "wv", "also holds"], ["wv", "wc", "part of the"]]}

MAPS[14] = {"nodes": [
    N("ss", "The Solar System", "14.1", 2, 0, "root"),
    N("neb", "Nebula", "14.1", 0, 1, "node"), N("pro", "Protostar", "14.1", 1, 1, "node"), N("star", "Star", "14.1", 2, 1, "node"), N("pl", "Planets", "14.1", 3, 1, "key", ["Mercury, Venus, Earth, Mars", "Jupiter, Saturn, Uranus, Neptune"]),
    N("sun", "The Sun", "14.1", 1, 2, "key", ["Our nearest star", "Its gravity holds the planets"]),
    N("moon", "The Moon", "14.2", 3, 3, "node", ["Orbits Earth about every 28 days"]),
    N("tides", "Tides", "14.2", 4, 4, "info", ["Two high tides a day", "Spring and neap tides"]),
    N("se", "Solar eclipse", "14.3", 0, 4, "node", ["Moon between Sun and Earth"]), N("le", "Lunar eclipse", "14.3", 2, 4, "node", ["Moon in Earth's shadow"]),
    N("models", "Models of space", "14.4", 0, 2, "info", ["Earth-centred → Sun-centred", "New evidence changes models"]),
  ], "links": [["ss", "neb", "began as a"], ["neb", "pro", "collapsed into a"], ["pro", "star", "became a"], ["star", "pl", "with"], ["star", "sun", "e.g."], ["pl", "moon", "may have a"], ["moon", "tides", "mainly controls"],
               ["sun", "se", "causes"], ["sun", "le", "causes"], ["ss", "models", "understood through"]]}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "cmaps.json")
    for n, m in MAPS.items():
        ids = {x["id"] for x in m["nodes"]}
        for a, b, _ in m["links"]: assert a in ids and b in ids, (n, a, b)
    json.dump({str(k): v for k, v in MAPS.items()}, open(out, "w"), ensure_ascii=False)
    print("wrote", out, len(MAPS))
