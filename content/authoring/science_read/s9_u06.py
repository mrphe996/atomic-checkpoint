# -*- coding: utf-8 -*-
"""Science Stage 9 · Unit 6 Displacement Reactions – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 9 (9Cc.01, 9Cc.02, 9TWSp.01)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}
CARD = lambda title, cards, cols=None: dict({"kind": "sciCards", "title": title, "cards": cards}, **({"cols": cols} if cols else {}))

# =====================================================================================================
# 6.1 Describing chemical reactions · 9Cc.01
# =====================================================================================================
READ["6.1"] = L(
    H("A universal language",
      "A Chinese chemist, a Brazilian chemist and a Kenyan chemist speak different languages – but all of them understand '2H₂ + O₂ → 2H₂O'.",
      "What does this line tell you about what happens in the reaction?"),
    I("Reactions rearrange atoms",
      "In a chemical reaction the atoms of the **reactants** separate and join up in new ways to make **products** with different properties. No atoms are created or destroyed.",
      fig={"kind": "sciMatter", "boxes": [{"t": "2H₂ + O₂", "d": "reactants", "kind": "mixel", "a": "#B0BEC5", "c": "#D64545"}, {"t": "2H₂O", "d": "product", "kind": "compound", "a": "#B0BEC5", "b": "#D64545"}]}),
    I("Word and symbol equations",
      "A **word equation** uses names; a **symbol equation** uses symbols and formulae.",
      table=[["Word equation", "Symbol equation"], ["hydrogen + oxygen → water", "2H₂ + O₂ → 2H₂O"], ["magnesium + oxygen → magnesium oxide", "2Mg + O₂ → 2MgO"],
             ["carbon + oxygen → carbon dioxide", "C + O₂ → CO₂"]],
      then=["In a **balanced** symbol equation there are the **same number of each kind of atom** on both sides. The big numbers in front (2H₂) tell you how many molecules; the small numbers (H₂) are part of the formula and are never changed."]),
    W("Checking an equation is balanced",
      "Is 2Mg + O₂ → 2MgO balanced?",
      [("left: Mg = 2, O = 2", "2Mg and O₂"), ("right: Mg = 2, O = 2", "2MgO = 2 Mg and 2 O"), ("same on both sides", "so it is balanced")], "Yes – 2 Mg and 2 O atoms on each side"),
    I("Predict, watch, explain: burning magnesium in a crucible",
      "Magnesium ribbon in a crucible with a lid weighs **31.62 g** in total. It is heated strongly, lifting the lid now and then to let air in. It glows white and leaves a white powder. The total is now **31.79 g**.",
      then=["Magnesium reacted with **oxygen from the air** to form magnesium oxide: 2Mg + O₂ → 2MgO. Oxygen atoms joined the magnesium, so the solid is heavier. No atoms were created – the extra 0.17 g is the oxygen."]),
    Y("Count the atoms",
      num("s9u06r11", "In the equation CH₄ + 2O₂ → CO₂ + 2H₂O, how many oxygen atoms are on the right-hand side?", 4, "CO₂ has 2; each H₂O has 1, and there are 2 water molecules.",
          "2 (in CO₂) + 2 (in 2H₂O) = 4 – the same as on the left (2O₂).")),
    K("Key points",
      "A reaction **rearranges atoms** into new products; no atoms are made or lost.",
      "Word equations use names; **symbol equations** use formulae and must be **balanced**.",
      "When magnesium burns, its mass increases because oxygen joins it."),
    book=BK(
        [("symbol equation", "an equation using chemical symbols and formulae"), ("balanced equation", "the same number of each atom on both sides"),
         ("reactant", "a substance at the start of a reaction"), ("product", "a substance made in a reaction")],
        [], [],
        [Ex("Write the word equation for: 2Cu + O₂ → 2CuO.", ans="copper + oxygen → copper oxide"),
         Ex("Count the atoms of each element on each side of: N₂ + 3H₂ → 2NH₃. Is it balanced?", ans="left: 2 N, 6 H; right: 2 N, 6 H – balanced"),
         Ex("Explain why the mass of the crucible and contents increased when magnesium burned.", ans="Oxygen from the air combined with the magnesium, adding mass."),
         Ex("A student says 'atoms were made in the reaction because the mass went up'. Correct this.", ans="No atoms were made – oxygen atoms from the air joined the magnesium; total mass is conserved.", think=True)],
        ["describe a reaction as a rearrangement of atoms", "write word and symbol equations", "check that a symbol equation is balanced"],
        look=["word and symbol equations", "the magnesium crucible results"],
        note="Read it after the video: rearranging atoms and word and symbol equations (answers at the back)."),
)

# =====================================================================================================
# 6.2 Displacement reactions · 9Cc.02, 9TWSp.01
# =====================================================================================================
READ["6.2"] = L(
    H("Cleaning poisoned water",
      "Water draining from an old mine is blue with dissolved copper compounds, which harm rivers. Workers add scrap iron to it.",
      "After a while the water is clearer and copper can be collected. What happened?"),
    I("The reactivity series and electrons",
      "The **reactivity series** lists metals from most to least reactive.",
      fig={"kind": "sciSeries"},
      then=["Metals react by **losing their outer electrons**. The more easily a metal loses them, the more reactive it is.",
            "Potassium is more reactive than sodium: it has more shells, so its outer electron is **further from the nucleus**, held less strongly and lost more easily."]),
    I("What is a displacement reaction?",
      "A **more reactive** metal **displaces** (pushes out) a **less reactive** metal from its compound: **A + BC → AC + B** (if A is more reactive than B).",
      table=[["Experiment", "Observation", "Equation"], ["copper wire in silver nitrate", "silver crystals grow; the solution turns blue", "copper + silver nitrate → copper nitrate + silver"],
             ["iron nail in copper sulfate", "brown copper coats the nail; blue fades to green", "iron + copper sulfate → iron sulfate + copper"], ["silver in copper nitrate", "no change", "no reaction – silver is less reactive"]]),
    Y("Predict",
      grid("s9u06r21", "Will a displacement reaction happen?", ["Yes", "No"],
           [("magnesium + copper sulfate", "Yes"), ("zinc + calcium chloride", "No"), ("iron + silver nitrate", "Yes"), ("copper + iron sulfate", "No")],
           "Is the free metal higher in the series?", "Mg and Fe are higher than Cu and Ag; Zn is lower than Ca and Cu is lower than Fe.")),
    I("Displacement reactions at work",
      "Displacement is used in industry and to protect the environment.",
      fig=CARD("Displacement at work", [{"icon": "flame", "t": "Thermite welding", "d": "aluminium + iron oxide → aluminium oxide + molten iron, welding rails"},
                                        {"icon": "factory", "t": "Mine waste", "d": "scrap iron displaces copper from waste solutions"},
                                        {"icon": "bottle", "t": "Cleaning water", "d": "a reactive metal displaces toxic metals so they can be removed"},
                                        {"icon": "heart", "t": "Gold jewellery", "d": "gold is so unreactive it is not displaced or attacked"}], 4)),
    Y("Thermite",
      mcq("s9u06r22", "In thermite welding, why does aluminium react with iron oxide?",
          [("Aluminium is more reactive than iron, so it takes the oxygen.", True, "Yes – it displaces the iron."), ("Iron is more reactive than aluminium.", False, "Aluminium is higher in the series."),
           ("Aluminium is a non-metal.", False, "Aluminium is a metal."), ("The rails are made of aluminium.", False, "The rails are steel; molten iron joins them.")],
          "Compare their positions in the series.", "The more reactive metal (aluminium) displaces the less reactive one (iron).")),
    K("Key points",
      "Reactivity depends on how easily a metal **loses outer electrons**; it increases with more shells in a group.",
      "**Displacement**: a more reactive metal displaces a less reactive metal from its compound.",
      "Uses: thermite welding, recovering copper, removing toxic metals from water."),
    book=BK(
        [("displacement reaction", "a more reactive element pushes a less reactive one out of its compound"), ("reactivity series", "metals listed from most to least reactive"),
         ("thermite reaction", "aluminium reacting with iron oxide to make molten iron")],
        [], [],
        [Ex("Predict and write word equations (or 'no reaction'): (a) zinc + copper sulfate (b) copper + zinc sulfate (c) magnesium + iron chloride.",
            ans="(a) zinc sulfate + copper (b) no reaction (c) magnesium chloride + iron"),
         Ex("Describe what you would see when an iron nail is left in copper sulfate solution.", ans="a brown coating of copper on the nail; the blue solution turns pale green"),
         Ex("Explain why potassium is more reactive than lithium.", ans="Potassium has more shells, so its outer electron is further from the nucleus and is lost more easily."),
         Ex("Quick quiz.", ("What are the substances at the start of a reaction called?", "reactants"), ("Balanced equation for magnesium burning?", "2Mg + O₂ → 2MgO"),
            ("Will copper displace iron from iron sulfate?", "no"), ("Name a use of displacement.", "thermite welding / recovering copper / cleaning water")),
         Ex("Explain how adding scrap iron to mine waste water recovers copper and cleans the water.", ans="Iron is more reactive, so it displaces copper from its compounds; copper metal can be collected and the water contains less copper.", think=True)],
        ["use the reactivity series to predict displacement", "explain reactivity in terms of losing electrons", "describe uses of displacement reactions"],
        look=["the displacement experiments", "displacement at work"],
        note="Read it after the video: the reactivity series and displacement reactions, plus a quick quiz (answers at the back)."),
)
