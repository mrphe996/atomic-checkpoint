# -*- coding: utf-8 -*-
"""Stage 7 · Unit 15 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u15 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(15, "15.1")]["book"] = BK(
    keys=[("area", "the space a flat shape covers"), ("mm², cm², m²", "square units: 1 cm² = 100 mm², 1 m² = 10 000 cm²")],
    intro=[], examples=[],
    exercise=[
        Ex("Convert.", ("8 cm² to mm²", "800"), ("3.5 m² to cm²", "35 000"), ("900 mm² to cm²", "9"), ("12 000 cm² to m²", "1.2")),
        Ex("A window is 120 cm by 90 cm. Find its area in m².", ans="1.08 m²"),
        Ex("How many 10 cm × 10 cm tiles cover a 2 m × 1.5 m wall?", ans="300"),
        Ex("Explain to a friend why 1 m² is not 100 cm².", ans="1 m² is 100 cm by 100 cm = 10 000 cm².", think=True),
    ],
    check=["Can I convert between mm², cm² and m²?", "Can I use the same units before multiplying?"], look=[], note=NOTE)

N[(15, "15.2")]["book"] = BK(
    keys=[("hectare (ha)", "10 000 m², a 100 m by 100 m square")],
    intro=[], examples=[],
    exercise=[
        Ex("Convert.", ("70 000 m² to ha", "7"), ("1.8 ha to m²", "18 000"), ("4500 m² to ha", "0.45")),
        Ex("A field is 320 m by 250 m. Find its area in hectares.", ans="8 ha"),
        Ex("A 5 ha field is 400 m long. How wide is it?", ans="125 m"),
        Ex("Find the area of your school grounds (use a map) in hectares.", ans="Your own estimate.", think=True),
    ],
    check=["Can I convert between hectares and m²?", "Can I solve problems with land areas?"], look=[], note=NOTE)

N[(15, "15.3")]["book"] = BK(
    keys=[("perpendicular height", "the height at right angles to the base"), ("base", "the side the height is measured from")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the area of the triangle.", ("base 9 cm, height 8 cm", "36 cm²"), ("base 15 m, height 4 m", "30 m²"), ("base 6.4 cm, height 5 cm", "16 cm²")),
        Ex("Find the missing length.", ("area 42 cm², base 12 cm: height?", "7 cm"), ("area 27 m², height 6 m: base?", "9 m")),
        Ex("A triangle has corners (1, 1), (9, 1) and (4, 6). Find its area.", ans="20 square units"),
        Ex("Draw three different triangles each with area 12 cm².", ans="For example base 6 height 4; base 8 height 3; base 12 height 2.", think=True),
    ],
    check=["Can I use area = ½ × base × height?", "Can I identify the perpendicular height?", "Can I find a missing base or height?"], look=[], note=NOTE)

N[(15, "15.4")]["book"] = BK(
    keys=[("volume", "the space inside a 3D shape"), ("capacity", "how much a container holds"), ("cm³, m³", "cubic units; 1000 cm³ = 1 litre")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the volume.", ("cuboid 9 × 5 × 4 cm", "180 cm³"), ("cube of side 7 cm", "343 cm³"), ("cuboid 2 m × 1.5 m × 0.8 m", "2.4 m³")),
        Ex("A carton is 12 cm × 6 cm × 15 cm. What is its capacity in litres?", ans="1.08 litres"),
        Ex("A cuboid has volume 420 cm³, length 10 cm and width 7 cm. Find its height.", ans="6 cm"),
        Ex("Find three different cuboids with volume 36 cm³ (whole-number sides).", ans="For example 1 × 1 × 36, 2 × 3 × 6, 3 × 3 × 4.", think=True),
    ],
    check=["Can I find the volume of a cube and a cuboid?", "Can I convert cm³ to litres?", "Can I find a missing length?"], look=[], note=NOTE)

N[(15, "15.5")]["book"] = BK(
    keys=[("surface area", "the total area of all the faces"), ("net", "the flat shape that folds into the solid")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the surface area.", ("cube of side 6 cm", "216 cm²"), ("cuboid 8 × 3 × 2 cm", "92 cm²"), ("cuboid 5 × 5 × 10 cm", "250 cm²")),
        Ex("A box with no lid is 25 cm × 20 cm × 10 cm. How much card is needed?", ans="1400 cm²"),
        Ex("A cube has surface area 294 cm². Find its side length.", ans="7 cm"),
        Ex("Using 12 one-centimetre cubes, make the cuboid with the smallest surface area.", ans="2 × 2 × 3 (32 cm²).", think=True),
    ],
    check=["Can I find the surface area of cubes and cuboids?", "Can I tell surface area from volume?"], look=[], note=NOTE)
