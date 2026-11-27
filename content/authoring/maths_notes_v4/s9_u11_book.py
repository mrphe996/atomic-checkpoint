# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u11 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(11, "11.1")]["book"] = BK(
    keys=[("ratio", "a comparison of quantities, e.g. 3 : 4 : 8")],
    intro=[], examples=[],
    exercise=[
        Ex("Money is shared in the ratio 2 : 3 : 7.", ("The smallest share is $18. Find the total.", "$108"), ("The largest share is $84. Find the middle share.", "$36")),
        Ex("Red : green beads are 5 : 3 in a bag of 64. 10 green beads are added. Find the new ratio.", ans="40 : 34 = 20 : 17"),
    ],
    check=["Can I solve ratio problems from a share, total or difference?"], look=[], note=NOTE)

N[(11, "11.2")]["book"] = BK(
    keys=[("direct proportion", "quantities with a constant ratio"), ("inverse proportion", "quantities with a constant product")],
    intro=[], examples=[],
    exercise=[
        Ex("Direct or inverse? Then answer.", ("7 m of cloth cost $56. Cost of 12 m?", "direct; $96"), ("5 pumps empty a pond in 18 h. Time for 9 pumps?", "inverse; 10 h")),
        Ex("A journey takes 45 minutes at 80 km/h. How long at 60 km/h?", ans="60 minutes"),
    ],
    check=["Can I tell direct from inverse proportion?", "Can I solve both types?"], look=[], note=NOTE)
