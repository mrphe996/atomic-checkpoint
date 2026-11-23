# -*- coding: utf-8 -*-
"""Stage 7 Unit 3 (Cells) — revision v2 (Nov 2026). Atomic originals; harder questions marked with `src` were
adapted from an outside source (named under the question). Applied on top of content/src/stage7-unit03.json:
  python3 -m revise.s7u03            (from content/authoring)
- new video data (captions, chapters, stops) from build/video run_s7u03.py → revise/s7u03_video.json
- Practice: same-reasoning duplicates removed; diagram, data and experiment-set-up questions added
- Unit Test A and B rebuilt (keys stay in content/private)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from c_base import O, mcq, multi, num, label, order, match, explain, grid, table, graph, B
from c_video import STOPS as OLD_STOPS

SRC = os.path.join(HERE, '..', '..', 'src', 'stage7-unit03.json')

SOURCES = [
    {"id": "SRC6", "name": "NSTA — Page Keeley, formative assessment probe 'Cells and Size'", "url": "https://www.nsta.org/lesson-plan/cells-and-size", "objs": ["O1", "O2", "O4"], "use": "Sizes of a pin point, a grain of salt and typical cells; which things need a microscope (3.1 Hard)."},
    {"id": "SRC7", "name": "OpenStax Biology 2e — 4 Cell Structure: Studying Cells (surface area to volume)", "url": "https://openstax.org/books/biology-2e/pages/4-chapter-summary", "objs": ["O8"], "use": "Why cells stay small: surface area to volume ratio of cubes (3.3 Hard)."},
    {"id": "SRC8", "name": "AAAS Project 2061 Science Assessment — Cells (misconception items)", "url": "https://assess.bscs.org/science/pages/faq", "objs": ["O5", "O6"], "use": "Common misconception that plant cells do not need mitochondria because they make food (3.2 Hard)."},
    {"id": "SRC9", "name": "STEM Learning — 'Cells and organ systems' (KS3 resource list)", "url": "https://www.stem.org.uk/node/12273", "objs": ["O9"], "use": "Large organisms need organ systems to transport materials to cells deep inside (3.4 Hard)."},
    {"id": "SRC10", "name": "Oak National Academy — KS3 'Specialised cells are adapted for their functions'", "url": "https://www.thenational.academy/teachers/programmes/science-secondary-ks3/units/cells/lessons/specialised-cells-are-adapted-for-their-functions/downloads", "objs": ["O8"], "use": "Structure–function reasoning for unfamiliar specialised cells (3.3 Hard)."},
]
S = {s["id"]: s for s in SOURCES}
def src(k): return {"id": k, "name": S[k]["name"], "url": S[k]["url"]}
ADV = "* Advanced. "

# ---------------------------------------------------------------- new stops in the videos
NEW_STOPS = {
 "v31s": dict(note="Paused on the size ladder: cheek cell 0.06 mm, grain of salt 0.3 mm.",
   q=num("v31s_q", "PREDICT: a cheek cell is about 0.06 mm across and a grain of salt is about 0.3 mm. How many cheek cells side by side would be as wide as the grain of salt?", 5, "cells", "H", "O1", units=["cells"],
         hint="Divide the bigger width by the smaller width: 0.3 ÷ 0.06.", reason="0.3 ÷ 0.06 = 5, so about 5 cheek cells fit across one grain of salt."),
   twin=num("v31s_t", "A hair is 0.1 mm wide and a cell is 0.02 mm wide. How many cells fit across the hair?", 5, "cells", "M", "O1", units=["cells"])),
 "v32s": dict(note="Paused before the drop of methylene blue lands on the cheek cells.",
   q=mcq("v32s_q", "PREDICT: cheek cells on a slide are almost colourless. What will one drop of methylene blue stain do?", [
       O("Colour the cells so they – especially the nuclei – are easier to see", True, "Yes – the stain is taken up by the cell parts, most strongly by the nucleus."),
       O("Kill the cells so they disappear", False, "The cells do not disappear; the stain makes them easier to see."),
       O("Make the cells bigger", False, "A stain changes colour, not size. Magnification comes from the lenses."),
       O("Make the background blue but leave the cells colourless", False, "It is the cell parts that take up the stain.")], "H", "O5", "Prediction",
       hint="A stain is a coloured dye. Think about why we would want colour on a nearly clear specimen."),
   twin=mcq("v32s_t", "Which solution is often used to stain onion cells?", [O("Iodine solution", True, ""), O("Salt water", False, ""), O("Vinegar", False, ""), O("Sugar solution", False, "")], "M", "O5")),
 "v32e": dict(note="Paused after the stained cells appear – learners explain what they saw.",
   q=explain("v32e_q", "EXPLAIN what you observed: why are the stained cheek cells much easier to see than the unstained ones?", [
       ("The stain colours the cell / cell parts", ["stain.*(colour|color|dye|blue)", "(colour|color|dye)s? the (cell|part|nucle)", "turn.*blue"]),
       ("The nucleus takes up the most stain / looks darkest", ["nucle"]),
       ("So the cell stands out from the clear / colourless background (contrast)", ["background", "stand out", "contrast", "clear", "colourless|colorless|transparent"])],
     "Without stain the cells are almost colourless, like the background. Methylene blue colours the cell parts, especially the nucleus, so each cell stands out clearly from the clear background.", "H", "O5", need=2),
   twin=mcq("v32e_t", "Which part of a stained cheek cell looks darkest?", [O("Nucleus", True, ""), O("Cell membrane", False, ""), O("Cytoplasm", False, ""), O("Cell wall", False, "Cheek cells have no cell wall.")], "M", "O5")),
 "v32o": dict(note="Paused before the onion bulb cell is shown next to a leaf cell.",
   q=mcq("v32o_q", "PREDICT: you look at the thin layer from inside an onion BULB. Will you see chloroplasts?", [
       O("No – the bulb grows underground in the dark, so its cells do not photosynthesise", True, "Correct – no light, no photosynthesis, no chloroplasts."),
       O("Yes – every plant cell has chloroplasts", False, "Every plant cell has a cell wall, but not every plant cell has chloroplasts."),
       O("Yes – but only after staining with iodine", False, "Iodine stains starch and nuclei; it cannot create chloroplasts."),
       O("No – onion is not a plant", False, "An onion is a plant: its cells have cell walls.")], "H", "O6", "Prediction"),
   twin=mcq("v32o_t", "Which plant cell is MOST likely to contain chloroplasts?", [O("A cell near the top of a leaf", True, ""), O("A root hair cell", False, ""), O("A cell inside a potato", False, ""), O("An onion bulb cell", False, "")], "M", "O6")),
 "v33w": dict(note="Paused before the animation shows water moving into the root hair cell.",
   q=order("v33w_q", "PREDICT: put the parts in the order that water passes through them, from the soil into the sap vacuole.", ["cell wall", "cell membrane", "cytoplasm", "sap vacuole"], "H", "O8", "Prediction",
           hint="Start at the outside of the cell and move inwards.", reason="Outside → inside: the cell wall is outermost, then the membrane lining it, then the cytoplasm, and the vacuole is in the middle."),
   twin=mcq("v33w_t", "Which part does water pass through FIRST when it enters a root hair cell?", [O("Cell wall", True, ""), O("Cytoplasm", False, ""), O("Sap vacuole", False, ""), O("Nucleus", False, "")], "M", "O8")),
 "v33e": dict(note="Paused after the animation of still cilia and mucus building up.",
   q=explain("v33e_q", "EXPLAIN why people who smoke often cough and get more chest infections. Use the words cilia and mucus.", [
       ("Smoke stops the cilia beating / damages cilia", ["cilia.*(stop|not|damag|still|paralys)", "(stop|damag).*cilia"]),
       ("Mucus (with dust / bacteria) is not moved up / builds up", ["mucus.*(build|stay|not (moved|swept|cleared)|collect|stuck)", "build.*mucus"]),
       ("Bacteria / dust reach or stay in the lungs → infection; coughing tries to clear it", ["bacteri|germ|infect", "cough.*(clear|remove|get rid)"])],
     "Chemicals in smoke stop the cilia beating, so the mucus with trapped dust and bacteria is not swept up to the throat. It builds up in the airways, so smokers cough to clear it, and the bacteria can cause chest infections.", "VH", "O8", need=2),
   twin=mcq("v33e_t", "What do cilia normally do with mucus?", [O("Sweep it up towards the throat", True, ""), O("Make it", False, "Other cells in the lining make mucus."), O("Push it into the lungs", False, ""), O("Turn it into oxygen", False, "")], "M", "O8")),
 "v34l": dict(note="Paused on the leaf section before the layers are explained.",
   q=mcq("v34l_q", "PREDICT: why is the palisade layer found just below the TOP surface of a leaf?", [
       O("It receives the most light there, and its many chloroplasts absorb it for photosynthesis", True, "Correct – light enters from above."),
       O("It is closer to the roots, so it gets more water", False, "The top of the leaf is not closer to the roots."),
       O("It protects the leaf from insects", False, "Protection is a job of the epidermis."),
       O("It has air spaces for gases", False, "That describes the spongy layer.")], "H", "O9", "Prediction"),
   twin=mcq("v34l_t", "Which leaf tissue has the MOST chloroplasts?", [O("Palisade layer", True, ""), O("Upper epidermis", False, ""), O("Lower epidermis", False, ""), O("Xylem", False, "")], "M", "O9")),
}
def stop_q(sid):
    if sid in NEW_STOPS: x = NEW_STOPS[sid]; return {"id": sid, "note": x["note"], "q": x["q"], "twin": x["twin"]}
    for v in OLD_STOPS.values():
        for s in v:
            if s["id"] == sid: return {k: s[k] for k in ("id", "note", "q", "twin") if k in s}
    raise KeyError(sid)

# ---------------------------------------------------------------- Practice: duplicates out, new questions in
DROP = {
 "3.1": ["s31p03", "s31p04", "s31p16", "s31p13"],     # same calculation as s31r3 / definition already in s31p12
 "3.2": ["s32p11", "s32p17", "s32p08", "s32p10"],     # repeats of s32p01, s32r4 and s32r5
 "3.3": ["s33p02", "s33p10", "s33p13", "s33p12", "s33p17"],   # repeats of s33r3, s33r5/s33p18, s33r6, s33r7
 "3.4": ["s34p17", "s34p15", "s34p04", "s34p14"],     # repeats of s34r4/s34p11, s34r5, s34r6
}
FOV = {"kind": "linegraph", "x": {"min": 0, "max": 40, "step": 10, "label": "Objective lens magnification (×)"}, "y": {"min": 0, "max": 5, "step": 1, "label": "Width of field of view (mm)"},
       "series": [{"pts": [[4, 4.5], [10, 1.8], [40, 0.45]]}]}
STAINBARS = {"kind": "barchart", "labels": ["no stain", "iodine (1 drop)", "iodine (2 drops)"], "values": [3, 17, 18], "ymax": 20, "step": 5, "ylabel": "Cells seen clearly in one view", "xlabel": "Onion slide"}
ALT = {"kind": "linegraph", "x": {"min": 0, "max": 4, "step": 1, "label": "Height above sea level (km)"}, "y": {"min": 4.5, "max": 6.5, "step": 0.5, "label": "Red blood cells (millions per mm³)"},
       "series": [{"pts": [[0, 5.0], [1, 5.2], [2, 5.5], [3, 5.9], [4, 6.3]]}]}
NEW_PRAC = {
 "3.1": [
  mcq("s31p21", "The diagram shows three views down a microscope at an onion slide. View B is bright but blurred. What should the student do next?", [
      O("Slowly turn the focusing knob (coarse at low power) until the cells are sharp", True, "Bright but blurred = enough light, not in focus."),
      O("Open the diaphragm more", False, "That fixes a DARK view (A), not a blurred one."),
      O("Change straight to the highest-power lens", False, "Always focus at low power first."),
      O("Add another drop of water", False, "Water does not sharpen the image.")], "H", "O4", "Figure", fig={"kind": "microviews"},
      hint="Is the problem too little light, or a picture that is not sharp?", reason="A = too little light (open the diaphragm / check the light). B = light is fine but the image is not focused → focus. C = in focus."),
  num("s31p22", "The graph shows how wide the field of view (the circle you see) is for three objective lenses. Read the graph: how wide is the field of view with the ×10 objective?", 1.8, "mm", "H", "O4", "Data", tol=0.1, units=["mm"], fig=FOV,
      hint="Find 10 on the x-axis, go up to the line, then across.", reason="At ×10 the point is at 1.8 mm. Higher magnification → smaller field of view, so you see fewer cells but in more detail."),
  mcq("s31p23", "Use the same graph. A student changes from the ×10 to the ×40 objective. What happens to what she sees?", [
      O("She sees a smaller area, so fewer cells, but each looks bigger", True, "The field narrows from 1.8 mm to 0.45 mm."),
      O("She sees a bigger area with more cells", False, "The graph goes DOWN as magnification goes up."),
      O("Nothing changes except the brightness", False, "The width of the view changes a lot."),
      O("The cells become smaller", False, "Higher magnification makes the image bigger.")], "H", "O4", "Data", fig=FOV),
  explain("s31p24", "Kofi's onion slide shows lots of round black-edged circles instead of cells. His teacher says they are air bubbles. Explain how they got there and how Kofi can avoid them next time.", [
      ("The coverslip was lowered too quickly / flat, trapping air", ["(coverslip|cover slip).*(quick|fast|flat|drop)", "trap.*air", "air.*trap"]),
      ("Lower the coverslip slowly at an angle (e.g. with a mounted needle)", ["slow", "angle", "needle|tilt|edge"])],
    "The bubbles were trapped when the coverslip was put down too quickly or flat. Next time he should touch one edge of the coverslip to the water and lower it slowly at an angle, so the air is pushed out.", "H", "O4", need=2),
 ],
 "3.2": [
  mcq("s32p21", "Cell A and Cell B both come from the same plant. Which statement is correct?", [
      O("Cell A comes from a leaf, because it has chloroplasts", True, "Leaf cells in the light photosynthesise, so they have chloroplasts."),
      O("Cell B comes from a leaf, because it is smaller", False, "Size is not the clue – look for chloroplasts."),
      O("Cell B is an animal cell, because it has no chloroplasts", False, "Cell B has a cell wall, so it is a plant cell."),
      O("Both cells come from the root", False, "Root cells are in the dark and have no chloroplasts – only B fits.")], "H", "O6", "Figure", fig={"kind": "plantAB"},
      reason="Both cells have a cell wall and a sap vacuole → plant cells. Only A has chloroplasts → from a part in the light (a leaf). B is from a dark part such as a root."),
  label("s32p22", "The diagram shows how to stain cells under a coverslip without lifting it. Label the set-up.", "stainsetup",
        {"dropper": "Dropper of stain", "towel": "Paper towel", "coverslip": "Coverslip", "specimen": "Specimen"}, "H", "O5",
        confuse={"Coverslip|Specimen": "The coverslip is the thin glass on top; the specimen is the thin layer of cells under it."}),
  explain("s32p23", "Look at the staining set-up. Why is the paper towel placed at the OPPOSITE edge of the coverslip to the stain?", [
      ("The towel soaks up / draws liquid out", ["soak|absorb|draw|pull|suck|wick"]),
      ("So the stain is pulled under the coverslip, across the specimen", ["(under|across|through).*(coverslip|specimen|cells|slide)", "stain.*(move|flow|spread|pulled|drawn)"])],
    "The paper towel soaks up water from one edge. This pulls the stain from the dropper under the coverslip and across the specimen, so all the cells are stained without lifting the coverslip.", "VH", "O5", need=2),
  mcq("s32p24", "A class counted how many onion cells they could see clearly in one view, with and without iodine stain. What is the best conclusion?", [
      O("Staining makes many more cells easy to see; a second drop adds almost nothing", True, "3 → 17 is a big change; 17 → 18 is tiny."),
      O("The more drops of stain, the more cells there are", False, "Stain cannot make new cells – it makes them visible."),
      O("Iodine is not needed, because some cells can be seen without it", False, "Only 3 cells were clear without stain."),
      O("Two drops is five times better than one", False, "17 and 18 are almost the same.")], "H", "O5", "Data", fig=STAINBARS),
 ],
 "3.3": [
  label("s33p21", "Water moves from the soil into this root hair cell and on into the sap vacuole. Label the four parts it passes through.", "rootpath",
        {"wall": "Cell wall", "membrane": "Cell membrane", "cytoplasm": "Cytoplasm", "vacuole": "Sap vacuole"}, "H", "O8",
        confuse={"Cell wall|Cell membrane": "The cell wall is the thick outer layer; the membrane is the thin layer just inside it."}),
  mcq("s33p22", "The graph shows the average number of red blood cells in people who live at different heights above sea level. Which statement BEST explains the pattern?", [
      O("Higher up, each breath holds less oxygen, so the body makes more red blood cells to carry enough oxygen", True, "More cells → more haemoglobin → more oxygen carried."),
      O("Higher up, people need less oxygen, so they make more red blood cells", False, "The body needs the same oxygen; the air holds less."),
      O("Red blood cells are made in the mountains, not at sea level", False, "Red blood cells are made inside the body everywhere."),
      O("Height has no effect – the numbers stay the same", False, "The line rises from 5.0 to 6.3 million per mm³.")], "VH", "O8", "Data", fig=ALT,
      reason="Read the trend: the higher up, the more red blood cells. Link structure to function: red blood cells carry oxygen with haemoglobin, so more cells make up for thinner air."),
  num("s33p23", "Use the graph. By how many millions per mm³ does the red blood cell count rise from sea level (0 km) to 4 km?", 1.3, "million per mm³", "H", "O8", "Data", tol=0.05, units=["million per mm³", "millions per mm³"], fig=ALT,
      reason="6.3 − 5.0 = 1.3 million per mm³."),
  grid("s33p24", "Compare the two specialised plant cells. Choose the correct entry for each feature.", ["Root hair cell", "Palisade cell"], [
      ("Many chloroplasts?", ["no", "yes"]), ("Long thin extension?", ["yes", "no"]), ("Where found", ["outside of roots", "near top of leaves"]), ("Main job", ["absorb water and mineral salts", "photosynthesis"])], "H", "O8"),
  explain("s33p25", "A student says: 'Red blood cells have no nucleus, so they cannot be real cells.' Use what you know about structure and function to reply.", [
      ("Red blood cells are still cells (membrane, cytoplasm)", ["membrane|cytoplasm|still (a |real )?cell"]),
      ("No nucleus leaves more room for haemoglobin", ["room|space|more haemoglobin|more hemoglobin"]),
      ("So it carries more oxygen – adapted to its function", ["oxygen"])],
    "Red blood cells are still cells – they have a cell membrane and cytoplasm. Losing the nucleus leaves more space for haemoglobin, so each cell can carry more oxygen. It is a specialised cell adapted to its job.", "VH", "O8", need=2),
 ],
 "3.4": [
  label("s34p21", "The diagram shows a section through a leaf. Label the four tissues.", "leafsection",
        {"upper": "Upper epidermis", "palisade": "Palisade layer", "spongy": "Spongy layer", "lower": "Lower epidermis"}, "H", "O9",
        confuse={"Palisade layer|Spongy layer": "Palisade cells are tall and tightly packed near the top; spongy cells are rounder with air spaces."}),
  mcq("s34p22", "Look at the leaf section. The upper epidermis cells are clear and have no chloroplasts. How does this help the leaf?", [
      O("Light passes straight through to the palisade layer below", True, "The palisade cells can then absorb the light."),
      O("It lets the upper epidermis make more food", False, "Without chloroplasts it cannot photosynthesise."),
      O("It lets gases in through the top surface", False, "Pores are mainly in the lower epidermis."),
      O("It makes the leaf heavier and stronger", False, "Clear cells are about light, not weight.")], "H", "O9", "Figure", fig={"kind": "leafsection"}),
  match("s34p23", "The diagram shows a tiny pond animal. Match each part to its level of organisation.", [
      ("One cell from the outer layer", "cell"), ("The whole outer layer of similar cells", "tissue"), ("A tentacle (made of several tissues)", "organ"), ("The whole animal", "organism")], "H", "O9", fig={"kind": "polyp"}),
  mcq("s34p24", "Which statement uses the word 'tissue' in its SCIENTIFIC meaning?", [
      O("The lining of the windpipe is a tissue of ciliated cells.", True, "A group of similar cells working together."),
      O("She wiped her nose with a tissue.", False, "That is the everyday meaning."),
      O("The present was wrapped in tissue paper.", False, "Everyday meaning."),
      O("A tissue is a single cell with a special job.", False, "A tissue is a GROUP of similar cells.")], "M", "O9"),
 ],
}
NEW_ADV = {
 "3.1": [
  multi("s31a5", ADV + "Your eyes can just see something about 0.1 mm wide. Which of these could you see WITHOUT a microscope? Select ALL that apply.", [
      O("the point of a pin (about 1.5 mm)", True), O("a grain of salt (about 0.3 mm)", True), O("a human egg cell (about 0.12 mm)", True),
      O("a human cheek cell (about 0.06 mm)", False), O("a bacterium (about 0.002 mm)", False)], "VH", "O1", "Reasoning",
      reason="Compare each size with 0.1 mm. Bigger than 0.1 mm → visible (pin point, salt, an egg cell – the largest human cell). Smaller → needs a microscope.", src=src("SRC6")),
  num("s31a6", ADV + "A cheek cell is about 0.06 mm across. A bacterium is about 0.002 mm long. How many bacteria, end to end, would stretch across one cheek cell?", 30, "bacteria", "VH", "O2", units=["bacteria"],
      reason="0.06 ÷ 0.002 = 30.", hint="Divide the bigger length by the smaller one. Count the decimal places carefully.", src=src("SRC6")),
 ],
 "3.2": [
  mcq("s32a5", ADV + "A student claims: 'Plant cells make their own food by photosynthesis, so they do not need mitochondria.' Which reply is BEST?", [
      O("Wrong – plant cells must still release energy from food, and this happens in mitochondria, day and night, even in roots", True, "Photosynthesis MAKES food; respiration in mitochondria RELEASES its energy."),
      O("Right – chloroplasts do the job of mitochondria in plants", False, "Chloroplasts make food; they do not release energy from it."),
      O("Right – only animal cells move, so only they need energy", False, "All living cells need energy for their life processes."),
      O("Wrong – but only leaf cells have mitochondria", False, "Root cells have no chloroplasts but do have mitochondria.")], "VH", "O6", "Reasoning",
      reason="Making food (photosynthesis, chloroplasts) and releasing energy from food (respiration, mitochondria) are different jobs. Every plant cell needs energy, so every plant cell has mitochondria.", src=src("SRC8")),
 ],
 "3.3": [
  table("s33a5", ADV + "Model cells as cubes. Complete the table (surface area = 6 × side × side; volume = side × side × side).",
        ["Side of cube (µm)", "Surface area (µm²)", "Volume (µm³)", "Surface area ÷ volume"],
        [["1", "6", "1", B(6)], ["2", B(24), "8", B(3)], ["3", "54", B(27), "2"]], "VH", "O8", "Data",
        reason="2 µm: 6 × 2 × 2 = 24; 24 ÷ 8 = 3. 3 µm: 3 × 3 × 3 = 27. As the cube gets bigger, surface area ÷ volume gets SMALLER.", src=src("SRC7")),
  mcq("s33a6", ADV + "Use your table. Why do cells that need to take in a lot of substances (like root hair cells) have long, thin shapes instead of being large and round?", [
      O("A long, thin shape keeps the surface large compared with the volume, so substances can get in fast enough", True, "Large and round → small surface for its volume."),
      O("A large round cell would have too much surface area", False, "The table shows the opposite: bigger cubes have LESS surface for their volume."),
      O("Long cells have more nuclei", False, "Shape, not number of nuclei, is the point here."),
      O("Round cells cannot have cell walls", False, "Not true, and not related to surface area.")], "VH", "O8", "Reasoning", src=src("SRC7")),
  mcq("s33a7", ADV + "Unfamiliar cell: a guard cell sits in pairs around a pore on the underside of a leaf. The pair can change shape to open or close the pore. Guard cells have chloroplasts. What is their most likely job?", [
      O("Controlling how much gas (and water vapour) passes in and out of the leaf", True, "Opening and closing the pore controls gas exchange."),
      O("Absorbing water from the soil", False, "That is the root hair cell – guard cells are on the leaf."),
      O("Carrying electrical signals", False, "That is a neurone."),
      O("Sweeping mucus", False, "That is a ciliated cell (in animals).")], "VH", "O8", "Reasoning",
      reason="Use structure → function: position (around a pore) + ability to change shape → they control the opening.", src=src("SRC10")),
 ],
 "3.4": [
  mcq("s34a5", ADV + "A flatworm is very thin and flat and has no blood or heart. An earthworm is thick and round, and has blood vessels and hearts. What is the BEST explanation?", [
      O("In a thin animal every cell is close to the surface, so substances reach it without a transport system; a thick animal needs one", True, "Large, thick bodies need organ systems to carry materials to cells deep inside."),
      O("Flatworms do not need oxygen", False, "All their cells need oxygen; it simply reaches them through the thin body."),
      O("Earthworms are animals, but flatworms are plants", False, "Both are animals."),
      O("Flatworms have no cells deep inside them because they have no tissues", False, "Flatworms do have tissues; they are just thin.")], "VH", "O9", "Reasoning", src=src("SRC9")),
 ],
}

# ---------------------------------------------------------------- Unit Test A and B (keys: content/private)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'private'))
from tests_stage7_unit03_v2 import TEST_A, TEST_B


ORIG = os.path.join(HERE, 's7u03_orig.json')   # the unit before this revision


def apply(path=SRC, video_json=os.path.join(HERE, 's7u03_video.json')):
    d = json.load(open(path, encoding='utf-8'))
    vid = json.load(open(video_json)) if os.path.exists(video_json) else None
    orig = json.load(open(ORIG, encoding='utf-8')) if os.path.exists(ORIG) else None
    for s in d['sections']:
        k = s['id']
        # dropped questions stay as 'retired': hidden from practice, kept so review lists made earlier still open
        old = {q['id']: q for q in s['prac'] + s.get('retired', [])}
        if orig: old.update({q['id']: q for q in next(x for x in orig['sections'] if x['id'] == k)['prac'] if q['id'] not in old})
        s['retired'] = [old[i] for i in DROP[k] if i in old]
        s['prac'] = [q for q in s['prac'] if q['id'] not in DROP[k]]
        ids = {q['id'] for q in NEW_PRAC[k]}; s['prac'] = [q for q in s['prac'] if q['id'] not in ids] + NEW_PRAC[k]
        ids = {q['id'] for q in NEW_ADV[k]}; s['adv'] = [q for q in s['adv'] if q['id'] not in ids] + NEW_ADV[k]
        if vid and k in vid:
            v = vid[k]; n = k[-1]
            s['video'] = {"src": v.get('src', f"media/u3_s{n}.mp4"), "poster": v.get('poster', f"media/u3_s{n}_poster.jpg"), "offset": 0, "dur": round(v['dur'], 3), "range": ""}
            s['captions'] = v['captions']; s['chapters'] = v['chapters']
            s['stops'] = [dict(stop_q(x['id']), t=x['t'], review=x['review']) for x in v['stops']]
    have = {x['id'] for x in d.get('sources', [])}
    d['sources'] = d.get('sources', []) + [x for x in SOURCES if x['id'] not in have]
    for t in (TEST_A, TEST_B): assert sum(x['pts'] for x in t) == 30, sum(x['pts'] for x in t)
    d['tests'] = {"A": TEST_A, "B": TEST_B, "pass": d.get('tests', {}).get('pass', 0.7)}
    ids = [q['id'] for s in d['sections'] for k2 in ('req', 'prac', 'adv') for q in s[k2]] + [q['id'] for t in (TEST_A, TEST_B) for q in t]
    dup = {i for i in ids if ids.count(i) > 1}; assert not dup, dup
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('stage7-unit03 v2:', [(s['id'], len(s['req']), len(s['prac']), len(s['adv']), len(s['stops'])) for s in d['sections']])


if __name__ == '__main__':
    apply()
