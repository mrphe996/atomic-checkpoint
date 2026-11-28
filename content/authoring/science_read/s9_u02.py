# -*- coding: utf-8 -*-
"""Science Stage 9 · Unit 2 Excretion – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 9 (9Bs.02, 9TWSa.01, 9SIC.03)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}
CARD = lambda title, cards, cols=None: dict({"kind": "sciCards", "title": title, "cards": cards}, **({"cols": cols} if cols else {}))
LB = lambda base, *labels, **kw: dict({"kind": "sciLabel", "base": base, "labels": [list(l) for l in labels]}, **kw)

# =====================================================================================================
# 2.1 How does the human excretory system work? · 9Bs.02, 9TWSa.01, 9SIC.03
# =====================================================================================================
READ["2.1"] = L(
    H("Three days",
      "A person can survive for weeks without food but only about three days without water.",
      "We lose water all the time. Which organs control how much we lose? Write down any you can think of."),
    I("What is excretion?",
      "**Excretion** is removing waste products made by **metabolism** – the chemical reactions in our cells. It stops toxic substances building up.",
      table=[["Excretory organ", "What it removes"], ["**lungs**", "carbon dioxide and water vapour (in breathed-out air)"], ["**skin**", "water, salts and a little urea (in sweat)"],
             ["**kidneys**", "urea, excess water and excess salts (in urine)"]],
      then=["**Urea** is made in the liver when the body breaks down proteins it does not need. Eating more protein than we need means more urea to excrete.",
            "Do not confuse excretion with egestion: getting rid of undigested food (faeces) is not excretion, because that food was never part of the body's metabolism."]),
    I("Predict, watch, explain: breathing on a cold mirror",
      "A student breathes gently onto a mirror taken from the fridge. A misty patch of tiny water droplets appears, then fades.",
      then=["Breathed-out air contains **water vapour** made by respiration in our cells. It condenses on the cold glass. So the lungs excrete water as well as carbon dioxide."]),
    I("What is in urine?",
      "Urine is about **95% water**; the rest is mostly **urea** (about 2%) and salts (about 3%). These figures vary.",
      then=["Drink lots of water and the kidneys release more urine, which is pale. When you are **dehydrated** the kidneys save water, so you make less urine and it is darker yellow.",
            "Pale, straw-coloured urine is a simple sign that you are drinking enough."]),
    I("Data: how an adult loses water in one day",
      "Typical daily water loss for an adult resting in a cool place:",
      fig={"kind": "barchart", "labels": ["urine", "sweat", "breathed out", "faeces"], "values": [1.5, 0.5, 0.4, 0.1], "ymax": 2, "step": 0.5, "ylabel": "water lost (litres per day)", "xlabel": "route"},
      then=["On a hot day sweating rises, so the kidneys make less urine to keep the body's water balanced."]),
    Y("Total loss",
      num("s9u02r11", "Use the chart. What is the total water lost in a day, in litres?", 2.5, "Add all four bars.", "1.5 + 0.5 + 0.4 + 0.1 = 2.5 litres.")),
    I("The human excretory system",
      "The urinary part of the excretory system:",
      fig=LB("excretory", (161, 132, "kidney", "l"), (196, 186, "ureter", "l"), (240, 256, "bladder", "r"), (240, 306, "urethra", "r"), (240, 40, "artery (to kidney)", "r"), (226, 40, "vein (from kidney)", "l"), bo={"letters": False}, s=0.75),
      table=[["Part", "Job"], ["**kidneys** (two, in the lower back)", "filter the blood and make urine"], ["**ureters**", "carry urine from each kidney to the bladder"],
             ["**bladder**", "stores urine"], ["**urethra**", "carries urine out of the body"]]),
    I("How do the kidneys work?",
      "Blood enters each kidney through the **renal artery**. The kidney **filters** it: urea, excess water and excess salts form urine; useful substances such as glucose are kept. Clean blood leaves through the **renal vein**.",
      then=["Healthy kidneys filter about 180 litres of fluid a day – but return almost all of it to the blood.",
            "If kidneys fail, waste builds up. Patients may have **dialysis**, where a machine filters their blood several times a week, or a **kidney transplant**. People can live healthily with one kidney, so a living person can donate one."]),
    Y("Order the path",
      mcq("s9u02r12", "Which shows the path of urine in the correct order?",
          [("kidney → ureter → bladder → urethra", True, "Yes."), ("kidney → urethra → bladder → ureter", False, "The ureter comes before the bladder."),
           ("bladder → kidney → ureter → urethra", False, "Urine is made in the kidney."), ("ureter → kidney → urethra → bladder", False, "The bladder stores urine before it leaves through the urethra.")],
          "Where is urine made, stored and released?", "Made in the kidney, carried by the ureter, stored in the bladder, released through the urethra.")),
    K("Key points",
      "**Excretion** removes waste from metabolism: lungs (CO₂, water), skin (sweat), kidneys (urine).",
      "Urine is about 95% water plus urea and salts; dark urine shows dehydration.",
      "Path: **kidney → ureter → bladder → urethra**.",
      "Kidneys filter blood from the renal artery; dialysis or a transplant helps when kidneys fail."),
    book=BK(
        [("excretion", "removing waste products of metabolism"), ("urea", "a waste made when the body breaks down excess protein"), ("kidney", "an organ that filters blood and makes urine"),
         ("ureter", "tube from a kidney to the bladder"), ("urethra", "tube that carries urine out of the body"), ("dialysis", "a machine filtering the blood when the kidneys fail")],
        [], [],
        [Ex("Name the three excretory organs and what each removes.", ans="lungs – carbon dioxide and water; skin – water, salts, urea; kidneys – urea, water, salts"),
         Ex("What is urine mostly made of?", ans="water (about 95%), plus urea and salts"),
         Ex("Explain why urine is darker on a hot day when you have not drunk much.", ans="You lose water as sweat, so the kidneys save water; the urine has less water and is more concentrated."),
         Ex("Quick quiz.", ("Which tube carries urine from the kidney to the bladder?", "the ureter"), ("Where is urea made?", "in the liver"),
            ("What does dialysis do?", "filters waste and extra water from the blood"), ("Is getting rid of faeces excretion?", "no – it is egestion")),
         Ex("Why can a healthy person donate a kidney?", ans="One healthy kidney can filter enough blood to keep the body's water and waste in balance.", think=True)],
        ["explain what excretion is", "name the excretory organs", "describe the urinary system and the path of urine", "describe how kidneys, dialysis and transplants work"],
        look=["the excretory organs table", "the urinary system diagram"],
        note="Read it after the video: excretion, urine, the urinary system and kidney failure, plus a quick quiz (answers at the back)."),
)
