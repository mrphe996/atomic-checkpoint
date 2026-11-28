# -*- coding: utf-8 -*-
"""Science Stage 9 · Unit 7 Salts – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 9 (9Cc.03, 9TWSp.04)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}
CARD = lambda title, cards, cols=None: dict({"kind": "sciCards", "title": title, "cards": cards}, **({"cols": cols} if cols else {}))

# =====================================================================================================
# 7.1 What are salts? · 9Cc.03
# =====================================================================================================
READ["7.1"] = L(
    H("More than table salt",
      "Chemists use the word 'salt' for hundreds of different substances – in fertilisers, plaster casts, fireworks and baking powder.",
      "What do you think they all have in common?"),
    I("Salts around us",
      "Table salt (sodium chloride) is just one **salt**.",
      fig=CARD("Useful salts", [{"icon": "wheat", "t": "Ammonium nitrate", "d": "fertiliser"}, {"icon": "pill", "t": "Calcium sulfate", "d": "plaster casts"},
                                {"icon": "cup", "t": "Sodium hydrogencarbonate", "d": "baking soda"}, {"icon": "flame", "t": "Copper and strontium salts", "d": "colours in fireworks"}], 4),
      then=["A salt is an **ionic compound**. Every acid contains **hydrogen ions (H⁺)**; a salt forms when those hydrogen ions are **replaced by metal ions or ammonium ions**."]),
    I("Acid + base → salt + water",
      "**Bases** are metal oxides and metal hydroxides. Bases that dissolve in water are **alkalis** (e.g. sodium hydroxide); others, like copper oxide, are insoluble but still react with acids.",
      table=[["Acid", "Salts it makes", "Example"], ["hydrochloric acid", "**chlorides**", "hydrochloric acid + potassium hydroxide → potassium chloride + water"],
             ["sulfuric acid", "**sulfates**", "sulfuric acid + copper oxide → copper sulfate + water"], ["nitric acid", "**nitrates**", "nitric acid + sodium hydroxide → sodium nitrate + water"]],
      then=["The **metal** part of the salt's name comes from the **base**; the rest comes from the **acid**."]),
    Y("Name the salt",
      grid("s9u07r11", "Which salt is made?", ["magnesium chloride", "zinc sulfate", "calcium nitrate", "copper chloride"],
           [("hydrochloric acid + magnesium oxide", "magnesium chloride"), ("sulfuric acid + zinc oxide", "zinc sulfate"), ("nitric acid + calcium hydroxide", "calcium nitrate"),
            ("hydrochloric acid + copper oxide", "copper chloride")],
           "Metal from the base; chloride / sulfate / nitrate from the acid.", "Each salt name = metal of the base + the acid's ending.")),
    I("Predict, watch, explain: what is left after neutralisation?",
      "Hydrochloric acid is neutralised exactly with sodium hydroxide (Universal Indicator green, pH 7). The solution is heated gently in an evaporating dish.",
      then=["As the water evaporates, small white crystals are left: **sodium chloride**. The acid and alkali reacted to make a salt and water; evaporating removed the water."]),
    K("Key points",
      "A **salt** is an ionic compound formed when the H⁺ of an acid is replaced by a metal (or ammonium) ion.",
      "**acid + base → salt + water**; bases are metal oxides and hydroxides (alkalis are soluble bases).",
      "Hydrochloric → chlorides; sulfuric → sulfates; nitric → nitrates.",
      "Salts are used as fertilisers, in medicine, cooking and fireworks."),
    book=BK(
        [("salt", "an ionic compound formed when the hydrogen of an acid is replaced by a metal"), ("base", "a metal oxide or hydroxide that neutralises an acid"),
         ("alkali", "a base that dissolves in water"), ("neutralisation", "acid + base → salt + water")],
        [], [],
        [Ex("Write word equations: (a) sulfuric acid + sodium hydroxide (b) hydrochloric acid + zinc oxide.", ans="(a) sodium sulfate + water (b) zinc chloride + water"),
         Ex("Which acid and base would you use to make potassium nitrate?", ans="nitric acid and potassium hydroxide"),
         Ex("Give two uses of salts.", ans="e.g. ammonium nitrate – fertiliser; calcium sulfate – plaster casts"),
         Ex("Why must the acid be neutralised exactly before evaporating to get pure sodium chloride?", ans="Any leftover acid or alkali would contaminate the salt.", think=True)],
        ["describe what a salt is", "write word equations for acid + base", "name the salt each acid makes"],
        look=["the naming table", "evaporating the neutral solution"],
        note="Read it after the video: what salts are and acid + base reactions (answers at the back)."),
)

# =====================================================================================================
# 7.2 How are salts prepared? · 9Cc.03, 9TWSp.04
# =====================================================================================================
READ["7.2"] = L(
    H("Blue crystals",
      "Copper sulfate forms beautiful blue crystals. You can make them in the lab from a green powder and a colourless acid.",
      "What steps would you need to end up with dry, pure crystals?"),
    I("Predict, watch, explain: which gas is made?",
      "Magnesium ribbon is added to dilute hydrochloric acid in one tube, marble chips (calcium carbonate) in another. Both fizz.",
      table=[["Tube", "Gas test", "Gas", "Salt made"], ["magnesium", "lighted splint – squeaky pop", "hydrogen", "magnesium chloride"],
             ["marble chips", "limewater turns milky", "carbon dioxide", "calcium chloride"]]),
    I("Salts from carbonates and metals",
      "Two more general reactions make salts.",
      table=[["Reactants", "", "Products", "Example"], ["**acid + metal carbonate**", "→", "**salt + water + carbon dioxide**", "sulfuric acid + copper carbonate → copper sulfate + water + carbon dioxide"],
             ["**acid + metal**", "→", "**salt + hydrogen**", "hydrochloric acid + zinc → zinc chloride + hydrogen"]],
      then=["Only moderately reactive metals – magnesium, zinc, iron – are used. Copper, silver and gold do not react; sodium and potassium are too dangerous."]),
    Y("Which products?",
      mcq("s9u07r21", "What are the products when nitric acid reacts with calcium carbonate?",
          [("calcium nitrate, water and carbon dioxide", True, "Yes."), ("calcium nitrate and hydrogen", False, "Hydrogen comes from acid + metal."),
           ("calcium oxide and nitrogen", False, "No."), ("calcium nitrate only", False, "Water and carbon dioxide are also made.")],
          "acid + carbonate → ?", "salt + water + carbon dioxide.")),
    I("Making copper sulfate crystals",
      "Preparing a pure, dry sample of a soluble salt from an insoluble base or carbonate:",
      fig={"kind": "sciFlow", "title": "Making copper sulfate crystals", "steps": [{"t": "Warm the acid", "d": "dilute sulfuric acid"}, {"t": "Add excess", "d": "copper carbonate until no more reacts"},
                                                                                {"t": "Filter", "d": "remove unreacted solid"}, {"t": "Evaporate", "d": "until saturated"}, {"t": "Crystallise", "d": "cool, filter, dry"}]},
      table=[["Step", "Why"], ["add copper carbonate in **excess**", "makes sure **all the acid** is used up"], ["**filter**", "removes the leftover copper carbonate (residue); the blue filtrate is copper sulfate solution"],
             ["heat gently to a **saturated** solution, then leave to cool", "crystals form as the solution cools; slow cooling gives bigger crystals"], ["dry the crystals on filter paper", "gives a dry sample"]],
      then=["Wear goggles; heat gently and do not boil the solution dry. The same method makes zinc chloride from zinc and hydrochloric acid."]),
    Y("Why excess?",
      mcq("s9u07r22", "Why is copper carbonate added until some is left over?",
          [("To make sure all the acid reacts.", True, "Yes – leftover acid would contaminate the salt."), ("To make the crystals bigger.", False, "Cooling slowly does that."),
           ("Because copper carbonate is the product.", False, "It is a reactant."), ("To speed up filtering.", False, "Not the reason.")],
          "What must not be left in the solution?", "Excess solid guarantees the acid is used up, and the extra is easily filtered off.")),
    K("Key points",
      "acid + metal carbonate → salt + water + carbon dioxide (limewater milky).",
      "acid + metal → salt + hydrogen (squeaky pop).",
      "Soluble salt method: excess solid → filter → evaporate to saturation → cool to crystallise → dry."),
    book=BK(
        [("excess", "more than is needed to react completely"), ("saturated solution", "a solution that can dissolve no more solute"), ("crystallisation", "crystals forming as a saturated solution cools")],
        [], [],
        [Ex("Write word equations: (a) hydrochloric acid + magnesium (b) sulfuric acid + zinc carbonate.", ans="(a) magnesium chloride + hydrogen (b) zinc sulfate + water + carbon dioxide"),
         Ex("Describe how to make dry crystals of zinc sulfate from zinc oxide and sulfuric acid.", ans="warm acid, add zinc oxide in excess, filter, evaporate filtrate to saturation, cool, filter off crystals, dry"),
         Ex("Why is copper not used to make copper chloride with hydrochloric acid?", ans="Copper does not react with dilute acids."),
         Ex("Quick quiz.", ("What is a salt?", "an ionic compound where an acid's hydrogen is replaced by a metal"), ("Salt made by sulfuric acid?", "a sulfate"),
            ("Gas made by acid + carbonate?", "carbon dioxide"), ("Why filter after adding excess base?", "to remove the unreacted solid")),
         Ex("Why is the solution evaporated only until saturated, rather than boiled completely dry?", ans="Crystals form slowly as it cools, giving purer, well-formed crystals; boiling dry can spit and may damage the salt.", think=True)],
        ["write word equations for acids with carbonates and metals", "describe how to prepare a pure, dry soluble salt"],
        look=["the gas tests", "the five steps for copper sulfate crystals"],
        note="Read it after the video: preparing salts from carbonates and metals, plus a quick quiz (answers at the back)."),
)
