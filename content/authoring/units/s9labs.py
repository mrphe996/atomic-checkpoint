# -*- coding: utf-8 -*-
"""Stage 9 experiment practice: short investigations with a diagram or results table, added to the
practice pools of each section. Each investigation has three linked questions that share the context.
Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from c_paper import Paper, B


class Lab(Paper):
    """Like Paper, but for practice pools: no 'Question n.' or '(a)' labels, no marks."""
    def q(self, ctx=None, fig=None, data=None, sec=None):
        self.qn += 1; self.part = 0; self.sec = sec
        self.ctx = {"ctx": ctx, "fig": fig, "data": data}
        return self

    def _add(self, q, pts):
        for k in ("ctx", "fig", "data"):
            if self.ctx.get(k): q[k] = self.ctx[k]
        q.pop("pts", None); q["lab"] = True
        LABS.setdefault(self.sec, []).append(q)
        return q


LABS = {}

# ---------------------------------------------------------------- Unit 1
L = Lab("s9u01x")
L.q("Ha puts pondweed in water with different concentrations of sodium hydrogencarbonate, which adds carbon dioxide to the water. The lamp stays 10 cm away.",
    fig={"kind": "pondweed", "dist": 10},
    data={"caption": "Ha's results", "head": ["Sodium hydrogencarbonate in %", "0", "0.5", "1.0", "1.5", "2.0"], "rows": [["Bubbles per minute", "3", "12", "22", "30", "31"]]}, sec="1.1")
L.mc(1, "O1", "Which statement describes Ha's results?", "the rate rises as carbon dioxide increases, then levels off", ["the rate falls as carbon dioxide increases", "the rate stays the same", "the rate rises steadily without levelling off"])
L.ex(2, "O1", "Suggest why the rate hardly changes between 1.5% and 2.0%.",
     [("carbon dioxide is no longer the limiting factor", ["limit|no longer|enough carbon dioxide"]), ("another factor such as light or temperature now limits the rate", ["light|temperature|another|other factor"])],
     "Carbon dioxide is no longer limiting the rate; another factor, such as light intensity or temperature, now limits photosynthesis.")
L.sa(1, "O1", "Why does Ha keep the lamp at the same distance?", ["so the light intensity stays the same", "/light/i"])

L.q("Three identical potted plants were weighed, then left for 24 hours in different conditions.",
    fig={"kind": "barchart", "labels": ["Still air", "Fan blowing", "Plastic bag over plant"], "values": [4, 9, 1], "ymax": 10, "step": 2, "ylabel": "Mass lost in 24 hours in g"}, sec="1.2")
L.sa(1, "O4", "Which plant lost the most water?", ["the plant with the fan blowing", "/fan/i"])
L.ex(2, "O4", "Explain why the fan increased the water loss.",
     [("wind carries water vapour away from the leaf", ["away|carr|remov|blow"]), ("so water evaporates / diffuses out of the stomata faster", ["faster|evaporat|diffus|stoma"])],
     "The moving air carries water vapour away from the leaves, so more water evaporates and diffuses out through the stomata.")
L.mc(1, "O4", "Why did the plant in the plastic bag lose so little water?", "the air in the bag became humid, so less water evaporated", ["the bag gave the plant extra water", "the plant stopped photosynthesising", "plastic is a poor conductor"])

# ---------------------------------------------------------------- Unit 2
L = Lab("s9u02x")
L.q("Volunteers drank different volumes of water. The table shows the urine they produced in the next 3 hours.",
    data={"caption": "Urine results", "head": ["Water drunk in litres", "0.5", "1.5", "2.5"], "rows": [["Urine produced in litres", "0.4", "1.2", "2.1"], ["Colour of urine", "dark yellow", "pale yellow", "almost colourless"]]}, sec="2.1")
L.ex(2, "O2", "Describe the pattern in the results.",
     [("more water drunk, more urine", ["(more|increase).{0,40}(more|increase)"]), ("urine becomes paler / more dilute", ["pale|dilute|colourless|lighter"])],
     "The more water drunk, the more urine is produced, and the urine becomes paler and more dilute.")
L.mc(1, "O2", "Why is the urine dark yellow after drinking only 0.5 litres?", "the kidneys save water, so the same waste is dissolved in less water", ["the kidneys make more urea", "the person has drunk too much", "the bladder adds colour"])
L.sa(1, "O1", "Name the waste substance made in the liver that is removed in urine.", ["urea"])

L.q("The diagram shows the human excretory system.", fig={"kind": "excretory"}, sec="2.1")
L.sa(1, "O3", "Write the letter of the organ that stores urine.", ["C"])
L.od(2, "O3", "Put the parts in the order urine passes through them.", ["Kidney", "Ureter", "Bladder", "Urethra"])
L.ex(2, "O4", "A dialysis machine is used when the kidneys fail. Explain what it does.",
     [("filters / cleans the blood", ["filter|clean|remov"]), ("removes urea and extra water / salts", ["urea|waste|water|salt"])],
     "The dialysis machine filters the patient's blood, removing urea and extra water and salts, doing the job of the kidneys.")

# ---------------------------------------------------------------- Unit 3
L = Lab("s9u03x")
L.q("Students measured the hand span of 30 classmates and the number of left-handed and right-handed students.",
    fig={"kind": "barchart", "labels": ["16–17", "18–19", "20–21", "22–23", "24–25"], "values": [3, 7, 11, 6, 3], "ymax": 12, "step": 2, "ylabel": "Number of students", "xlabel": "Hand span in cm"}, sec="3.3")
L.sa(1, "O4", "Which hand span group has the most students?", ["20–21", "20-21", "20 to 21", "/20.{0,4}21/"])
L.mc(1, "O4", "Hand span shows continuous variation. Why?", "it can have any value within a range", ["it has only two possible values", "it is never inherited", "it is caused only by the environment"])
L.ex(2, "O4", "Being left- or right-handed is discontinuous variation. Explain the difference between continuous and discontinuous variation.",
     [("continuous: any value in a range (e.g. height, hand span)", ["any value|range|height|span|continuous"]), ("discontinuous: separate categories / groups (e.g. blood group)", ["categor|group|separate|either|distinct|blood"])],
     "Continuous variation can take any value within a range, like hand span. Discontinuous variation falls into separate categories, like being left- or right-handed.")

L.q("Doctors recorded how the percentage of bacteria resistant to an antibiotic changed after it was first used in a hospital.",
    fig={"kind": "linegraph", "x": {"min": 0, "max": 10, "step": 2, "label": "Years after the antibiotic was first used"}, "y": {"min": 0, "max": 80, "step": 10, "label": "Resistant bacteria in %"},
         "series": [{"pts": [[0, 1], [2, 5], [4, 15], [6, 35], [8, 55], [10, 70]]}]}, sec="3.4")
L.nm(1, "O5", "What percentage of the bacteria were resistant after 6 years?", 35, "%", tol=2)
L.ex(3, "O5", "Use natural selection to explain the change.",
     [("a few bacteria had a mutation / were resistant by chance", ["mutation|chance|variation|some|few"]), ("the antibiotic killed the others; resistant ones survived", ["surviv|kill"]), ("they reproduced and passed on resistance", ["reproduc|multipl|pass|offspring|gene"])],
     "By chance a few bacteria had a mutation that made them resistant. The antibiotic killed the others, so the resistant bacteria survived, reproduced and passed on the resistance gene.")
L.mc(1, "O5", "Which action slows the spread of resistant bacteria?", "only using antibiotics when they are really needed", ["stopping a course of antibiotics early", "using antibiotics for colds", "sharing antibiotics with friends"])

# ---------------------------------------------------------------- Unit 4
L = Lab("s9u04x")
L.q("The diagram shows an atom of an element.", fig={"kind": "atom", "p": 13, "n": 14, "shells": [2, 8, 3]}, sec="4.1")
L.nm(1, "O1", "What is the mass number of this atom?", 27, "×", units=["×"])
L.sa(1, "O2", "Write its electronic structure.", ["2,8,3", "2.8.3", "2 8 3", "2, 8, 3"])
L.mc(1, "O3", "Which group of the Periodic Table is this element in?", "Group 3", ["Group 1", "Group 2", "Group 8"])

L.q("Small pieces of three Group 1 metals were dropped into water.",
    data={"caption": "Observations", "head": ["Metal", "Observations", "Time to disappear in s"], "rows": [["Lithium", "fizzes steadily, floats", "60"], ["Sodium", "fizzes fast, melts into a ball", "15"], ["Potassium", "fizzes violently, lilac flame", "4"]]}, sec="4.2")
L.ex(2, "O4", "Describe the trend in reactivity down Group 1, using the data.",
     [("reactivity increases down the group", ["increase|more reactive"]), ("uses data, e.g. time falls from 60 s to 4 s", ["60|15|4 s|time"])],
     "Reactivity increases down Group 1: the time to disappear falls from 60 s for lithium to 4 s for potassium.")
L.cz(2, "O4", "Complete the word equation.", "sodium + water → sodium {0} + {1}", [["hydroxide"], ["hydrogen"]])
L.mc(1, "O4", "Why do Group 1 metals have similar reactions?", "they all have one electron in their outer shell", ["they all have the same mass", "they are all gases", "they all have eight outer electrons"])

# ---------------------------------------------------------------- Unit 5
L = Lab("s9u05x")
L.q("The diagram shows the bonding in a molecule. Only the outer electrons are shown.", fig={"kind": "dotcross", "mol": "CH4", "k1": "carbon", "k2": "hydrogen"}, sec="5.2")
L.sa(1, "O2", "Name this molecule.", ["methane", "CH4"])
L.nm(1, "O2", "How many covalent bonds are in the molecule?", 4, "bonds")
L.mc(1, "O2", "What is a covalent bond?", "a shared pair of electrons", ["a transferred electron", "a force between ions", "a sea of electrons"])

L.q("Students tested three solids.",
    data={"caption": "Results", "head": ["Solid", "Melting point in °C", "Conducts when solid?", "Conducts when dissolved or molten?"], "rows": [["X", "801", "no", "yes"], ["Y", "−182", "no", "no"], ["Z", "3550", "no", "no"]]}, sec="5.4")
L.gd(3, "O4", "Which structure does each solid have?", "Structure", [("X", "Giant ionic"), ("Y", "Simple molecular"), ("Z", "Giant covalent")])
L.ex(2, "O4", "Explain why X conducts electricity when molten but not when solid.",
     [("X is made of ions", ["ion"]), ("ions can move when molten, but are fixed in the solid", ["move|free|fixed|lattice"])],
     "X is made of ions. In the solid the ions are fixed in place, but when molten they are free to move and carry the current.")
L.mc(1, "O4", "Why does Y have such a low melting point?", "the forces between its molecules are weak", ["its covalent bonds are weak", "it is made of ions", "it is a metal"])

# ---------------------------------------------------------------- Unit 6
L = Lab("s9u06x")
L.q("Pieces of four metals were put in copper sulfate solution and the temperature rise was measured.",
    fig={"kind": "tubes", "items": [{"label": "A", "metal": "magnesium", "solution": "copper sulfate", "coat": True, "colour": "#BFE3F7"}, {"label": "B", "metal": "zinc", "solution": "copper sulfate", "coat": True, "colour": "#CFE3F7"}, {"label": "C", "metal": "iron", "solution": "copper sulfate", "coat": True, "colour": "#D8E8F2"}, {"label": "D", "metal": "silver", "solution": "copper sulfate", "colour": "#7FB8E6"}]},
    data={"caption": "Temperature rise", "head": ["Metal", "Magnesium", "Zinc", "Iron", "Silver"], "rows": [["Temperature rise in °C", "18", "9", "5", "0"]]}, sec="6.2")
L.od(2, "O2", "Use the results to put the metals in order of reactivity, most reactive first.", ["Magnesium", "Zinc", "Iron", "Silver"])
L.ex(2, "O3", "Explain why there was no change in tube D.",
     [("silver is less reactive than copper", ["less reactive|below copper|lower"]), ("so it cannot displace copper", ["cannot|can.?t|no displace|not displace"])],
     "Silver is less reactive than copper, so it cannot displace copper from copper sulfate solution.")
L.cz(2, "O3", "Complete the word equation.", "zinc + copper sulfate → {0} + {1}", [["zinc sulfate"], ["copper"]])

L.q("In the thermite reaction, aluminium powder is heated with iron oxide. Molten iron is produced.", sec="6.1")
L.cz(2, "O1", "Complete the word equation.", "aluminium + iron oxide → {0} + {1}", [["aluminium oxide"], ["iron"]])
L.mc(1, "O2", "Why does this reaction happen?", "aluminium is more reactive than iron", ["iron is more reactive than aluminium", "oxygen is a metal", "the iron is molten"])
L.ex(2, "O1", "Explain why the total mass stays the same in this reaction.",
     [("atoms are not created or destroyed", ["not (created|made|destroyed)|no atoms|same atoms|conserv"]), ("they are rearranged / oxygen moves from iron to aluminium", ["rearrang|swap|moves|transfer|join"])],
     "No atoms are created or destroyed. They are only rearranged: the oxygen moves from the iron to the aluminium, so the mass stays the same.")

# ---------------------------------------------------------------- Unit 7
L = Lab("s9u07x")
L.q("Ngoc makes copper sulfate crystals from copper oxide and sulfuric acid.", fig={"kind": "filtration", "letters": True}, sec="7.2")
L.od(2, "O4", "Put the steps in order.", ["Warm the acid and add copper oxide until no more dissolves", "Filter to remove the excess copper oxide", "Heat the filtrate to evaporate some of the water", "Leave it to cool so crystals form", "Pat the crystals dry with filter paper"])
L.mc(1, "O4", "Why is excess copper oxide added?", "to make sure all the acid is used up", ["to make the crystals bigger", "to make the solution acidic", "to cool the mixture"])
L.cz(2, "O2", "Complete the word equation.", "copper oxide + sulfuric acid → {0} + {1}", [["copper sulfate"], ["water"]])

L.q("Lam adds the same mass of four solids to dilute hydrochloric acid and records what happens.",
    data={"caption": "Lam's observations", "head": ["Solid", "Observation"], "rows": [["Magnesium", "fizzes; gas pops with a lighted splint"], ["Calcium carbonate", "fizzes; gas turns limewater milky"], ["Copper", "no change"], ["Sodium hydroxide", "gets warm; no fizzing"]]}, sec="7.2")
L.gd(3, "O3", "Which gas is made by each solid?", "Gas made", [("Magnesium", "Hydrogen"), ("Calcium carbonate", "Carbon dioxide"), ("Sodium hydroxide", "No gas")], extra=["Oxygen"])
L.sa(1, "O1", "Name the salt made when magnesium reacts with hydrochloric acid.", ["magnesium chloride"])
L.mc(1, "O3", "Why does copper not react?", "copper is less reactive than hydrogen", ["copper is a non-metal", "copper is an acid", "the acid is too cold"])

# ---------------------------------------------------------------- Unit 8
L = Lab("s9u08x")
L.q("Calcium carbonate chips react with acid in a flask on a balance. The mass is recorded every minute for large chips and for powder.",
    fig={"kind": "linegraph", "x": {"min": 0, "max": 6, "step": 1, "label": "Time in minutes"}, "y": {"min": 0, "max": 2.5, "step": 0.5, "label": "Mass lost in g"},
         "series": [{"pts": [[0, 0], [1, 1.2], [2, 1.8], [3, 2.1], [4, 2.2], [5, 2.2], [6, 2.2]], "label": "powder"}, {"pts": [[0, 0], [1, 0.5], [2, 0.9], [3, 1.3], [4, 1.6], [5, 1.9], [6, 2.1]], "label": "chips", "dash": True}]}, sec="8.3")
L.mc(1, "O4", "Which reacts faster?", "the powder, because its line is steeper", ["the chips, because their line is longer", "both react at the same rate", "the chips, because they lose less mass"])
L.ex(3, "O4", "Explain, using collision theory, why the powder reacts faster.",
     [("powder has a larger surface area", ["surface area"]), ("more particles exposed, so more collisions per second", ["more (frequent )?collisions|collide more|more often"]), ("so more successful collisions / faster rate", ["success|faster|rate"])],
     "The powder has a much larger surface area, so more particles of calcium carbonate are exposed to the acid. There are more collisions per second, so more successful collisions and a faster rate.")
L.ex(2, "O1", "Both lines end at about the same mass lost. Explain why.",
     [("same mass of calcium carbonate / same amount of reactants", ["same (mass|amount)|same reactant"]), ("so the same mass of carbon dioxide is made in the end", ["same (mass|amount|volume) of (carbon dioxide|gas)|carbon dioxide"])],
     "The same mass of calcium carbonate and acid were used, so in the end the same mass of carbon dioxide is made and lost.")

L.q("Students timed how long a cross under a flask disappeared when sodium thiosulfate reacted with acid at different temperatures. They repeated each temperature.",
    data={"caption": "Results", "head": ["Temperature in °C", "Time 1 in s", "Time 2 in s", "Time 3 in s"], "rows": [["20", "120", "118", "124"], ["30", "64", "66", "90"], ["40", "33", "31", "32"]]}, sec="8.3")
L.nm(1, "O4", "Which result is anomalous? Give the time in s.", 90, "s")
L.nm(2, "O4", "Calculate the mean time at 30 °C, ignoring the anomaly.", 65, "s")
L.ex(2, "O3", "Explain why the reaction is faster at higher temperature.",
     [("particles move faster / more energy", ["faster|more energy|kinetic"]), ("more collisions have the activation energy / more frequent collisions", ["activation|more (frequent|often|successful)|collide more"])],
     "At higher temperature the particles move faster, so they collide more often and more of the collisions have at least the activation energy.")

# ---------------------------------------------------------------- Unit 9
L = Lab("s9u09x")
L.q("Kiet measures the mass and volume of an irregular stone. Its mass is 64.8 g.", fig={"kind": "displacement", "before": 50, "after": 74, "max": 100}, sec="9.1")
L.nm(1, "O1", "What is the volume of the stone?", 24, "cm³", units=["cm³", "cm3", "mL"])
L.nm(2, "O2", "Calculate the density of the stone.", 2.7, "g/cm³", units=["g/cm³", "g/cm3"])
L.mc(1, "O4", "Will the stone float in water (density 1.0 g/cm³)?", "no, it is denser than water", ["yes, it is a solid", "yes, it is small", "only in salty water"])

L.q("The table shows the densities of some liquids. Equal volumes are poured gently into a tall cylinder.",
    data={"caption": "Densities", "head": ["Liquid", "Honey", "Water", "Vegetable oil", "Washing-up liquid"], "rows": [["Density in g/cm³", "1.42", "1.00", "0.92", "1.03"]]}, sec="9.3")
L.od(2, "O4", "Put the liquids in the order they settle, from the bottom of the cylinder to the top.", ["Honey", "Washing-up liquid", "Water", "Vegetable oil"])
L.ex(2, "O3", "Explain why a gas is much less dense than a liquid.",
     [("gas particles are far apart", ["apart|spread|gap|space"]), ("so there is less mass in each cm³", ["less mass|fewer particles|per (cm|volume)"])],
     "Gas particles are much further apart, so there is far less mass in each cubic centimetre.")
L.mc(1, "O3", "Warm water rises above cold water. Why?", "warm water is less dense than cold water", ["warm water is denser", "cold water has no particles", "heat is lighter than water"])

# ---------------------------------------------------------------- Unit 10
L = Lab("s9u10x")
L.q("Two identical cans, one painted matt black and one shiny silver, were filled with hot water and left to cool.",
    fig={"kind": "cans", "items": [{"label": "matt black", "colour": "#222"}, {"label": "shiny silver", "colour": "#D9DDE3"}]},
    data={"caption": "Temperatures in °C", "head": ["Time in minutes", "0", "5", "10", "15"], "rows": [["Matt black", "80", "68", "59", "52"], ["Shiny silver", "80", "74", "69", "65"]]}, sec="10.4")
L.sa(1, "O4", "Which can cooled faster?", ["matt black", "the matt black can", "black"])
L.ex(2, "O4", "Explain the difference.",
     [("matt black is a better emitter of infrared radiation", ["emit|radiat|infrared"]), ("so it transfers thermal energy away faster", ["faster|more (energy|heat)|loses"])],
     "Matt black surfaces are better emitters of infrared radiation, so the black can transfers thermal energy to the surroundings faster.")
L.ms(2, "O3", "Select TWO variables that had to be the same.", ["the volume of water", "the starting temperature"], ["the colour of the can", "the temperature after 15 minutes", "the time of day"])

L.q("Small dishes of water were left in different conditions for a day.",
    fig={"kind": "barchart", "labels": ["Cool, still", "Warm, still", "Warm, windy", "Warm, wide dish"], "values": [4, 9, 16, 15], "ymax": 18, "step": 3, "ylabel": "Water evaporated in g"}, sec="10.5")
L.sa(1, "O5", "Which conditions gave the most evaporation?", ["warm and windy", "/windy/i"])
L.ex(2, "O5", "Explain why the wide dish lost more water than the normal dish in warm, still air.",
     [("larger surface area", ["surface area|wider|bigger surface"]), ("more particles can escape from the surface", ["more particles|escape"])],
     "The wide dish has a larger surface area, so more water particles are at the surface and can escape.")
L.ex(2, "O5", "Explain why evaporation cools the water left behind.",
     [("the fastest / most energetic particles escape", ["fast|most energ|high(est)? energ"]), ("the average energy of those left falls, so temperature falls", ["average|left|remain|lower temperature|cool"])],
     "The fastest-moving particles with the most energy escape, so the average kinetic energy of the particles left behind falls and the water cools.")

# ---------------------------------------------------------------- Unit 11
L = Lab("s9u11x")
L.q("The diagram shows the traces of three sounds on an oscilloscope with the same settings.",
    fig={"kind": "waves", "traces": [{"amp": 1, "cycles": 2, "label": "P"}, {"amp": 2.5, "cycles": 2, "label": "Q"}, {"amp": 1, "cycles": 5, "label": "R"}]}, sec="11.2")
L.sa(1, "O3", "Which sound is the loudest?", ["Q"])
L.sa(1, "O3", "Which sound has the highest pitch?", ["R"])
L.ex(2, "O3", "Explain how you chose your answers.",
     [("loudest has the biggest amplitude (tallest wave)", ["amplitude|tall|height"]), ("highest pitch has the highest frequency (most waves)", ["frequency|most waves|closest|more waves|wavelength"])],
     "Q has the biggest amplitude, so it is loudest. R has the most waves on the screen, so the highest frequency and pitch.")

L.q("A student measures the speed of sound by standing 255 m from a wall and clapping in time with the echo. He makes 20 claps in 30 s.", sec="11.1")
L.nm(1, "O1", "How far does the sound travel between one clap and the echo returning?", 510, "m")
L.nm(2, "O1", "Each echo takes 30 ÷ 20 s to return. Calculate the speed of sound.", 340, "m/s", units=["m/s", "m per s"])
L.ex(2, "O1", "Explain how sound travels through air.",
     [("particles vibrate / compressions and rarefactions", ["vibrat|compress|rarefact"]), ("vibrations are passed on from particle to particle", ["pass|particle to particle|collide|next"])],
     "Air particles vibrate back and forth, making compressions and rarefactions. Each particle passes the vibration on to the next.")

# ---------------------------------------------------------------- Unit 12
L = Lab("s9u12x")
L.q("Linh measures the voltage across a resistor and the current through it.",
    fig={"kind": "circuit", "type": "series", "top": ["battery", {"k": "ammeter", "l": "A"}], "right": ["resistor"], "bottom": [{"k": "voltmeter", "l": "V"}], "left": ["variable"]},
    data={"caption": "Linh's results", "head": ["Voltage in V", "1.0", "2.0", "3.0", "4.0"], "rows": [["Current in A", "0.20", "0.40", "0.60", "0.80"]]}, sec="12.5")
L.nm(2, "O5", "Calculate the resistance of the resistor.", 5, "Ω", units=["Ω", "ohms"])
L.mc(1, "O2", "Linh's voltmeter is drawn in series. Where should it be connected?", "in parallel across the resistor", ["in series next to the cell", "anywhere in series", "it does not need connecting"])
L.gr(3, "O5", "Plot current against voltage.", {"label": "Voltage in V", "min": 0, "max": 5, "step": 1}, {"label": "Current in A", "min": 0, "max": 1, "step": 0.2}, [[1, 0.2], [2, 0.4], [3, 0.6], [4, 0.8]])

L.q("Two identical lamps are connected in parallel to a cell.",
    fig={"kind": "circuit", "type": "parallel", "main": ["cell", {"k": "ammeter", "l": "A1"}], "branches": [["lamp", {"k": "ammeter", "l": "A2"}], ["lamp", {"k": "ammeter", "l": "A3"}]]}, sec="12.3")
L.nm(1, "O3", "A2 reads 0.3 A and A3 reads 0.3 A. What does A1 read?", 0.6, "A", units=["A", "amps"])
L.ex(2, "O3", "One lamp breaks. Explain what happens to the other lamp.",
     [("the other lamp stays on", ["stays|still (on|lit|works)|keeps"]), ("it is on its own branch / complete loop through it", ["branch|own|separate|parallel|loop"])],
     "The other lamp stays on, because it is on its own branch, which is still a complete loop through the cell.")
L.mc(1, "O3", "Each lamp in parallel has the full voltage of the cell. Compared with two lamps in series, the lamps are…", "brighter", ["dimmer", "the same", "off"])

# ---------------------------------------------------------------- Unit 13
L = Lab("s9u13x")
L.q("The diagram shows part of the carbon cycle.", fig={"kind": "carboncycle"}, sec="13.3")
L.mc(1, "O3", "Which process removes carbon dioxide from the air?", "photosynthesis", ["respiration", "combustion", "decomposition"])
L.ex(2, "O3", "Explain how carbon in a dead tree returns to the air.",
     [("decomposers (bacteria, fungi) break down the wood", ["decompos|bacteria|fungi|microb"]), ("they respire, releasing carbon dioxide", ["respir|carbon dioxide|release"])],
     "Bacteria and fungi decompose the dead tree. As they respire they release the carbon as carbon dioxide into the air.")
L.ex(2, "O4", "Explain how cutting down and burning forests increases the carbon dioxide in the air.",
     [("burning (combustion) releases carbon dioxide", ["burn|combust|releas"]), ("fewer trees to remove carbon dioxide by photosynthesis", ["fewer trees|less photosynth|photosynth"])],
     "Burning the wood releases carbon dioxide, and with fewer trees less carbon dioxide is removed from the air by photosynthesis.")

L.q("The table shows the ages of rocks on the sea floor at different distances from a mid-ocean ridge.",
    data={"caption": "Age of sea-floor rocks", "head": ["Distance from ridge in km", "0", "100", "200", "300", "400"], "rows": [["Age in millions of years", "0", "5", "10", "15", "20"]]}, sec="13.2")
L.ex(2, "O2", "Describe the pattern and explain what it shows.",
     [("rocks are older further from the ridge", ["older|further|age increase"]), ("new crust forms at the ridge and spreads outwards / plates move apart", ["new|spread|apart|ridge"])],
     "The further from the ridge, the older the rock. New crust forms at the ridge and then moves outwards as the plates move apart.")
L.nm(2, "O2", "Calculate the speed of spreading in km per million years.", 20, "km per million years", units=["km per million years", "km/million years"])
L.mc(1, "O1", "What drives the plates apart at the ridge?", "convection currents in the mantle", ["the Moon's gravity", "earthquakes", "wind"])

# ---------------------------------------------------------------- Unit 14
L = Lab("s9u14x")
L.q("Students drop balls of the same size but different masses into sand from 1 m to model asteroid impacts.",
    fig={"kind": "crater", "h": "1 m", "d": 34},
    data={"caption": "Results", "head": ["Mass of ball in g", "20", "40", "60", "80"], "rows": [["Crater diameter in cm", "4.1", "5.2", "6.0", "6.6"]]}, sec="14.1")
L.ex(2, "O1", "Describe the pattern in the results.",
     [("heavier ball, wider crater", ["(heav|more mass|great|increase).{0,40}(wide|large|big)"]), ("the increase gets smaller", ["smaller|less|slow|not proportional"])],
     "The heavier the ball, the wider the crater, but each extra 20 g makes a smaller difference.")
L.mc(1, "O1", "Which is a limitation of this model?", "real asteroids travel far faster and explode on impact", ["the balls are round", "the sand is dry", "the crater can be measured"])
L.ex(2, "O1", "Explain how a large asteroid impact could cause a mass extinction.",
     [("dust / debris blocks sunlight, climate cools", ["dust|debris|block|sunlight|cool|dark"]), ("plants die, so food chains collapse", ["plant|photosynth|food chain|food"])],
     "The impact throws dust into the atmosphere that blocks sunlight, so the climate cools. Plants cannot photosynthesise and die, food chains collapse and many species become extinct.")

L.q("Astronomers compared rocks brought back from the Moon with rocks from Earth's mantle.",
    data={"caption": "Comparison", "head": ["Property", "Moon rock", "Earth's mantle"], "rows": [["Oxygen isotope ratio", "same", "same"], ["Iron content", "low", "low"], ["Water and gases", "almost none", "some"]]}, sec="14.2")
L.ex(2, "O2", "Explain how the data support the collision theory of the Moon's formation.",
     [("Moon rock is very similar to Earth's mantle (same isotopes)", ["same|similar|isotope|mantle"]), ("Moon formed from material knocked off Earth in a collision", ["collision|knock|impact|thrown|debris"])],
     "Moon rocks have the same oxygen isotopes as Earth's mantle, which suggests the Moon formed from mantle material thrown out when a planet-sized body collided with Earth.")
L.mc(1, "O2", "Why does Moon rock contain almost no water?", "the heat of the collision drove water off", ["the Moon is too cold", "water sank to the core", "the Sun froze it"])
L.mc(1, "O3", "Where do new stars form?", "in nebulae – clouds of dust and gas", ["inside planets", "in the asteroid belt", "on the Moon"])
