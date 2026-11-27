# -*- coding: utf-8 -*-
"""Stage 7 · Unit 8 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
import math
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES, FIG
from .s7_u04 import TBL, ROW
from .s7_u05 import BIG, SHAPE

INK, FILL = "#1F2A37", "#DCE8FB"
# own little drawings in a 320 × 320 box (the app's figures cannot draw symmetry lines, chords or turned copies)
SVG = lambda inner, x, y, w=320, at=0: T(f'<svg viewBox="0 0 320 320" width="{w}" height="{w}">{inner}</svg>', x=x, y=y, at=at)
POLY = lambda pts, fill=FILL: f'<polygon points="{" ".join(f"{px:.1f},{py:.1f}" for px, py in pts)}" fill="{fill}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
DASH = lambda x1, y1, x2, y2, c=RED: f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="3.5" stroke-dasharray="10 7"/>'
LINE = lambda x1, y1, x2, y2, c=INK: f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="3.5"/>'
DOT = lambda x, y, c=RED, r=9: f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
TXT = lambda x, y, s, c=INK, size=24: f'<text x="{x}" y="{y}" font-size="{size}" font-weight="700" text-anchor="middle" fill="{c}">{s}</text>'
REG = lambda n, r=120, rot=-90: [(160 + r * math.cos(math.radians(rot + 360 * k / n)), 160 + r * math.sin(math.radians(rot + 360 * k / n))) for k in range(n)]
def AX(n, ks=None, rot=-90, r=150):
    """Lines of symmetry of the regular n-gon drawn by REG: one every 180/n degrees through the centre."""
    out = ""
    for k in (range(n) if ks is None else ks):
        a = math.radians(rot + 180 * k / n); out += DASH(160 - r * math.cos(a), 160 - r * math.sin(a), 160 + r * math.cos(a), 160 + r * math.sin(a))
    return out
RECT = [(40, 90), (280, 90), (280, 230), (40, 230)]
PARA = [(30, 230), (220, 230), (290, 90), (100, 90)]
KITE = [(160, 20), (250, 110), (160, 300), (70, 110)]
CELLS = lambda cells, x=700, y=130, w=520, at=0, **k: FIG(x, y, w, at, kind="cells", cells=cells, grid=True, **k)
SOLID = lambda solid, x=700, y=130, w=520, at=0, **k: FIG(x, y, w, at, kind="solid", solid=solid, **k)
G = "#BFE8CF"

VIDEOS = {}

VIDEOS["8.1"] = [
    dict(kind="hook", title="Signs and shapes", steps=[
        dict(say="Many road signs are symmetrical. A stop sign is a regular octagon, and a warning sign is often a triangle.",
             do=[E("🛑", 90, 170, 100), E("⚠️", 250, 170, 100), T("Many signs are **symmetrical**", x=80, y=330)]),
        dict(say="Here is a regular hexagon. All 6 sides are equal, and all 6 angles are equal.", do=[SVG(POLY(REG(6)), 800, 150), T("a **regular hexagon**", x=80, y=420)]),
        PAUSE("8.1-k1", "How many lines of symmetry does a regular hexagon have? Pause the video and count them.", "How many lines of symmetry does a regular hexagon have?"),
    ]),
    dict(kind="hook", title="Fold lines of a hexagon", steps=[
        dict(say="A line of symmetry is a fold line. 3 of them join opposite corners.", do=[SVG(POLY(REG(6)) + AX(6, [0, 2, 4]), 800, 150), T("3 lines through **opposite corners**", x=80, y=180)]),
        dict(say="3 more join the middles of opposite sides. That makes 6 lines of symmetry.",
             do=[SVG(POLY(REG(6), "none") + AX(6, [1, 3, 5]), 800, 150), T("3 lines through **middles of sides**", x=80, y=270), B("6 lines of symmetry", x=80, y=380, color=GREEN, at=3.4)]),
    ]),
    dict(kind="recall", title="Reflection", steps=[
        dict(say="Remember: in a reflection, every point and its image are the same distance from the mirror line.", do=[T("point and image: **same distance** from the mirror line", x=80, y=170)]),
        dict(say="The capital letter A has a vertical line of symmetry. The left half is the mirror image of the right half.",
             do=[SVG(TXT(160, 270, "A", INK, 300) + DASH(160, 10, 160, 310), 800, 230, 300)]),
    ]),
    dict(kind="idea", title="Line symmetry", steps=[
        dict(say="A shape has line symmetry if a line cuts it into two halves that are mirror images. Fold along the line, and the halves match exactly.",
             do=[T("**Line symmetry**: two halves are **mirror images**", x=80, y=160), CELLS([[0, 0], [1, 0], [2, 0], [1, 1], [1, 2]], x=760, y=200, w=440, cols=3, rows=3, mirror={"x": 1.5})]),
        dict(say="This T shape has 1 line of symmetry. We draw it as a dashed line.", do=[B("1 line of symmetry", x=80, y=280, color=BLUE)]),
        dict(say="A rectangle has 2 lines of symmetry: one vertical and one horizontal.", do=[SVG(POLY(RECT) + DASH(160, 60, 160, 260) + DASH(10, 160, 310, 160), 150, 370, 300), T("rectangle: **2 lines**", x=480, y=500)]),
        PAUSE("8.1-k2", "Your turn. How many lines of symmetry does an equilateral triangle have? Pause the video and try it.", "How many lines of symmetry does an equilateral triangle have?"),
    ]),
    dict(kind="idea", title="Check: equilateral triangle", steps=[
        dict(say="Each line goes from a corner to the middle of the opposite side. There are 3 corners, so there are 3 lines of symmetry.",
             do=[SVG(POLY(REG(3, 130)) + AX(3), 780, 150, 360), T("corner → middle of the opposite side", x=80, y=200), B("3 lines of symmetry", x=80, y=310, color=GREEN, at=4)]),
    ]),
    dict(kind="idea", title="Rotational symmetry", steps=[
        dict(say="Now turn a shape about its centre. A shape has rotational symmetry if it looks exactly the same more than once during a full turn.",
             do=[T("**Rotational symmetry**: looks the same **more than once** in a full turn", x=80, y=160)]),
        dict(say="The order of rotational symmetry is the number of times it looks the same in one full turn.", do=[T("**order** = how many times it fits in **360°**", x=80, y=240)]),
        dict(say="Follow the red corner of this square. After each quarter turn, the square looks the same. It fits 4 times, so the order is 4.",
             do=[SVG(POLY(REG(4, 110, -135)) + DOT(82, 82), 80, 350, 200), SVG(POLY(REG(4, 110, -135)) + DOT(238, 82), 330, 350, 200, at=3), SVG(POLY(REG(4, 110, -135)) + DOT(238, 238), 580, 350, 200, at=4.2),
                 SVG(POLY(REG(4, 110, -135)) + DOT(82, 238), 830, 350, 200, at=5.4), B("order 4", x=1070, y=420, color=GREEN, at=8)]),
        PAUSE("8.1-k3", "Your turn. What is the order of rotational symmetry of a rectangle? Pause the video and think about it.", "What is the order of rotational symmetry of a rectangle?"),
    ]),
    dict(kind="idea", title="Check: turning a rectangle", steps=[
        dict(say="After a quarter turn, the rectangle stands upright, so it does not fit. After a half turn, it fits. After a full turn, it fits again.",
             do=[SVG(POLY(RECT) + DOT(52, 102), 80, 170, 260), SVG(POLY([(90, 40), (230, 40), (230, 280), (90, 280)], "#F3F4F6") + DOT(218, 52), 400, 170, 260, at=1),
                 SVG(POLY(RECT) + DOT(268, 218), 720, 170, 260, at=5), T("quarter turn ✗", x=450, y=450, color=RED, at=2), T("half turn ✓", x=790, y=450, color=GREEN, at=6)]),
        dict(say="It fits 2 times in a full turn. The order of rotational symmetry is 2.", do=[B("order 2", x=1040, y=280, color=GREEN)]),
        dict(say="If a shape only fits once, after the full turn, its order is 1. We say it has no rotational symmetry.", do=[T("order 1 = **no** rotational symmetry", x=80, y=540)]),
    ]),
    dict(kind="method", title="How do I find the symmetry of a shape?", steps=[
        dict(say="Here is the method. Step 1: look for fold lines. Test vertical, horizontal and diagonal lines.", do=[T("1. **Fold lines**: vertical, horizontal, diagonal", x=80, y=170)]),
        dict(say="Step 2: turn the shape about its centre, and count how many times it fits in a full turn.", do=[T("2. **Turn** it: count the fits in 360°", x=80, y=260)]),
        dict(say="Step 3: write both answers: the number of lines, and the order.", do=[T("3. Write the number of **lines** and the **order**", x=80, y=350)]),
        dict(say="A useful fact: a regular polygon with n sides has n lines of symmetry, and rotational symmetry of order n.", do=[T("Regular polygon, n sides → **n lines**, **order n**", x=80, y=440, color=BLUE), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A parallelogram", steps=[
        dict(say="Describe the symmetry of a parallelogram.", do=[SVG(POLY(PARA), 800, 150, 360)]),
        dict(say="Try folding it. No fold line works, because the slanted sides do not line up. It has no lines of symmetry.", do=[B("0 lines of symmetry", x=80, y=190, color=RED)]),
        dict(say="Now turn it. After a half turn, it fits onto itself. So it has rotational symmetry of order 2.", do=[B("order 2", x=80, y=320, color=GREEN), T("half turn ✓", x=80, y=420)]),
    ]),
    dict(kind="example", title="A kite", steps=[
        dict(say="Describe the symmetry of a kite.", do=[SVG(POLY(KITE), 800, 150, 360)]),
        dict(say="A kite has 1 line of symmetry. It goes through the two corners where the equal sides meet.", do=[SVG(DASH(160, 0, 160, 320), 800, 150, 360), B("1 line of symmetry", x=80, y=190, color=GREEN)]),
        dict(say="No turn fits it onto itself, except a full turn. So the order is 1: no rotational symmetry.", do=[B("order 1", x=80, y=320, color=RED), T("no rotational symmetry", x=80, y=420)]),
    ]),
    dict(kind="example", title="Completing a pattern", steps=[
        dict(say="2 squares are shaded on this grid. Shade more squares, so that the pattern has 2 lines of symmetry: the vertical line and the horizontal line.",
             do=[CELLS([[0, 0], [1, 1]], cols=4, rows=4, mirror={"x": 2, "y": 2}), T("make **2 lines** of symmetry", x=80, y=180)]),
        dict(say="First, reflect each shaded square in the vertical line. That gives 2 new squares.", do=[CELLS([[3, 0, G], [2, 1, G]], cols=4, rows=4), T("1. reflect in the **vertical** line", x=80, y=290)]),
        dict(say="Then reflect all 4 squares in the horizontal line. That gives 4 more. We shaded 6 extra squares.",
             do=[CELLS([[0, 3, G], [1, 2, G], [3, 3, G], [2, 2, G]], cols=4, rows=4), T("2. reflect in the **horizontal** line", x=80, y=380), B("6 extra squares", x=80, y=480, color=GREEN, at=5)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="How many lines of symmetry does a rectangle have? Here is Sam's working. Which line goes wrong first?",
             do=LINES("Sam", "the lines of symmetry of a rectangle", ["vertical line ✓ and horizontal line ✓", "both diagonals ✓", "so 4 lines"])),
        dict(say="Line 2 is wrong. Fold a rectangle along a diagonal, and the corners do not meet. A diagonal is not a line of symmetry.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="A rectangle has only 2 lines of symmetry. A square is special: it has 4.", do=[B("rectangle: 2 lines", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Symmetry in nature", steps=[
        dict(say="Nature is full of symmetry. A snowflake has 6 lines of symmetry, and rotational symmetry of order 6.", do=[E("❄️", 90, 160, 100), T("snowflake: **6 lines**, **order 6**", x=230, y=190)]),
        dict(say="Most starfish have 5 arms, so they have rotational symmetry of order 5.", do=[E("⭐", 90, 300, 100), T("starfish: **order 5**", x=230, y=330)]),
        dict(say="And the recycling symbol has 3 arrows. It has rotational symmetry of order 3, but no lines of symmetry at all.", do=[E("♻️", 90, 440, 100), T("recycling symbol: **order 3**, no lines", x=230, y=470)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.1-k4", "One last question. Which shape has rotational symmetry, but no lines of symmetry: a parallelogram, an isosceles triangle, or a square? Pause the video and answer.",
              "Which has rotational symmetry but no lines of symmetry: a parallelogram, an isosceles triangle or a square?"),
        dict(say="It is the parallelogram. It has no fold lines, but it fits onto itself after a half turn.", do=[SVG(POLY(PARA), 800, 150, 360), B("parallelogram", x=80, y=190, color=GREEN), T("0 lines · order 2", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a line of symmetry is a fold line. The two halves match exactly.", do=[T("• Line symmetry: the shape **folds** onto itself", x=80, y=170)]),
        dict(say="The order of rotational symmetry is the number of times a shape fits in one full turn.", do=[T("• **Order** = number of fits in a full turn", x=80, y=250)]),
        dict(say="Order 1 means no rotational symmetry.", do=[T("• Order 1 = no rotational symmetry", x=80, y=330)]),
        dict(say="A regular polygon with n sides has n lines of symmetry, and order n.", do=[T("• Regular polygon, n sides: **n lines**, **order n**", x=80, y=410)]),
    ]),
]

CIRC = f'<circle cx="160" cy="160" r="120" fill="{FILL}" stroke="{INK}" stroke-width="3"/>' + DOT(160, 160, INK, 5)

VIDEOS["8.2"] = [
    dict(kind="hook", title="A bicycle wheel", steps=[
        dict(say="Look at a bicycle wheel. There is a hub in the middle. Thin spokes go from the hub out to the rim.", do=[E("🚲", 90, 160, 120), T("**hub** in the middle · **spokes** · **rim**", x=260, y=200)]),
        PAUSE("8.2-k1", "A spoke goes from the hub to the rim. Is it most like a radius, a diameter, or a chord? Pause the video and decide.", "A spoke from the hub to the rim is most like a radius, a diameter or a chord?"),
    ]),
    dict(kind="hook", title="The wheel is a circle", steps=[
        dict(say="A spoke is a radius. It goes from the centre of the circle to the edge.", do=[BIG(FIG(700, 130, 520, 0, kind="circle", r="radius")), B("spoke = radius", x=80, y=180, color=GREEN)]),
        dict(say="The hub is the centre, and the rim is the circumference: the distance all the way round.", do=[T("hub = **centre**", x=80, y=300), T("rim = **circumference**", x=80, y=380, at=2)]),
    ]),
    dict(kind="recall", title="Radius and diameter", steps=[
        dict(say="Remember: the diameter goes right across the circle, through the centre. It is 2 times the radius.", do=[BIG(FIG(700, 130, 520, 0, kind="circle", d="17 cm")), B("diameter = 2 × radius", x=80, y=180)]),
        dict(say="If the radius is 8.5 centimetres, the diameter is 2 times 8.5, which is 17 centimetres.", do=[MATH("2 × 8.5 = 17 cm", x=80, y=310, color=GREEN)]),
    ]),
    dict(kind="idea", title="More parts of a circle", steps=[
        dict(say="Two more words. A chord is a straight line that joins 2 points on the circumference.",
             do=[SVG(CIRC + LINE(62, 90, 270, 112, BLUE) + TXT(170, 88, "chord", BLUE), 800, 150, 400), T("**chord**: joins 2 points on the circle", x=80, y=180)]),
        dict(say="A tangent is a straight line that touches the circle at exactly 1 point. A flat road is a tangent to a wheel.",
             do=[SVG(LINE(20, 280, 300, 280, RED) + TXT(250, 310, "tangent", RED), 800, 150, 400), T("**tangent**: touches at exactly 1 point", x=80, y=280)]),
        dict(say="A diameter is a special chord. It is the chord that goes through the centre.", do=[SVG(LINE(40, 160, 280, 160, GREEN) + TXT(110, 190, "diameter", GREEN), 800, 150, 400), T("**diameter**: a chord through the centre", x=80, y=380)]),
        PAUSE("8.2-k2", "Your turn. The longest chord of a circle is called the what? Pause the video and decide.", "The longest chord of a circle is the …"),
    ]),
    dict(kind="idea", title="Check: the longest chord", steps=[
        dict(say="The longest chord is the diameter. A chord gets longer as it moves towards the centre, and it is longest when it passes through the centre.",
             do=[SVG(CIRC + LINE(75, 75, 245, 75, GREY) + LINE(48, 115, 272, 115, GREY) + LINE(40, 160, 280, 160, GREEN), 800, 150, 400), B("longest chord = diameter", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Polygons", steps=[
        dict(say="A polygon is a closed 2D shape with straight sides. We name a polygon by its number of sides.", do=[T("**Polygon**: closed shape, **straight sides**", x=80, y=150)]),
        dict(say="3 sides: a triangle. 4 sides: a quadrilateral. 5 sides: a pentagon.",
             do=[TBL(["Sides", "Name"], [["3", "triangle"], ["4", "quadrilateral"], ["5", "pentagon"], ["6", "hexagon"], ["8", "octagon"], ["10", "decagon"]], y=220), ROW(0, 0.3), ROW(1, 2.2), ROW(2, 4.4)]),
        dict(say="6 sides: a hexagon. 8 sides: an octagon. 10 sides: a decagon.", do=[ROW(3, 0.3), ROW(4, 2.2), ROW(5, 4.2), SVG(POLY(REG(5)), 560, 230, 200), SVG(POLY(REG(8, 120, -67.5)), 800, 230, 200, at=2.2), SVG(POLY(REG(10)), 1040, 230, 200, at=4.2)]),
        PAUSE("8.2-k3", "One is missing from the table. What is the name of a polygon with 7 sides? Pause the video and try it.", "Name a polygon with 7 sides."),
    ]),
    dict(kind="idea", title="Check: 7 sides", steps=[
        dict(say="A polygon with 7 sides is a heptagon.", do=[SVG(POLY(REG(7)), 800, 150, 360), B("7 sides: heptagon", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="idea", title="Regular polygons", steps=[
        dict(say="A regular polygon has all its sides equal, and all its angles equal. It needs both.", do=[T("**Regular**: all sides equal **and** all angles equal", x=80, y=150)]),
        dict(say="A square is regular: 4 equal sides, and 4 right angles.", do=[SVG(POLY(REG(4, 130, -135)), 80, 250, 240), T("square ✓", x=140, y=520, color=GREEN)]),
        dict(say="A rhombus has 4 equal sides, but its angles are not all equal. So it is irregular.", do=[SVG(POLY([(160, 80), (300, 160), (160, 240), (20, 160)]), 480, 250, 240), T("rhombus ✗", x=540, y=520, color=RED)]),
        dict(say="A rectangle has 4 equal angles, but its sides are not all equal. It is irregular too.", do=[SVG(POLY(RECT), 880, 250, 240), T("rectangle ✗", x=930, y=520, color=RED)]),
    ]),
    dict(kind="method", title="How do I describe a shape?", steps=[
        dict(say="Here is the method. Step 1: count the sides, to name the polygon.", do=[T("1. **Count** the sides → name", x=80, y=170)]),
        dict(say="Step 2: check whether all the sides, and all the angles, are equal. If so, it is regular.", do=[T("2. All sides **and** all angles equal? → **regular**", x=80, y=260)]),
        dict(say="Step 3: for a triangle, compare the sides. 3 equal sides is equilateral, 2 equal sides is isosceles, and no equal sides is scalene.",
             do=[T("3. Triangle: **equilateral** (3) · **isosceles** (2) · **scalene** (0)", x=80, y=350)]),
        dict(say="Step 4: look for a right angle.", do=[T("4. Is there a **right angle**?", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Chords and the diameter", steps=[
        dict(say="A circle has a radius of 7 centimetres. One chord is 10 centimetres long. Could another chord be 15 centimetres long?",
             do=[BIG(FIG(760, 150, 440, 0, kind="circle", r="7 cm")), T("radius **7 cm** · a chord of 15 cm?", x=80, y=170)]),
        dict(say="The longest chord is the diameter. The diameter is 2 times 7, which is 14 centimetres.", do=[MATH("diameter = 2 × 7 = 14 cm", x=80, y=280)]),
        dict(say="15 is more than 14. So no: a chord of 15 centimetres is impossible.", do=[MATH("15 > 14", x=80, y=370), B("No: impossible", x=80, y=460, color=RED, at=2.4)]),
    ]),
    dict(kind="example", title="Naming triangles", steps=[
        dict(say="A triangle has sides of 6 centimetres, 6 centimetres and 9 centimetres. Name it.", do=[SHAPE([[0, 0], [9, 0], [4.5, 3.97]], x=700, y=110, w=440, s=["9 cm", "6 cm", "6 cm"]), T("sides 6 cm, 6 cm, 9 cm", x=80, y=170)]),
        dict(say="2 sides are equal, so it is an isosceles triangle.", do=[B("isosceles", x=80, y=260, color=GREEN)]),
        dict(say="Another triangle has angles of 90 degrees, 40 degrees and 50 degrees. It has a right angle, and all 3 angles are different. So it is a right-angled scalene triangle.",
             do=[T("angles 90°, 40°, 50°", x=80, y=390), B("right-angled scalene", x=80, y=480, color=GREEN, at=6)]),
    ]),
    dict(kind="example", title="A regular decagon", steps=[
        dict(say="A regular decagon has a perimeter of 45 centimetres. How long is each side?", do=[SVG(POLY(REG(10)), 800, 150, 360), T("regular decagon, perimeter **45 cm**", x=80, y=170)]),
        dict(say="A decagon has 10 sides, and in a regular polygon they are all equal. 45 divided by 10 is 4.5. Each side is 4.5 centimetres.", do=[MATH("45 ÷ 10 = 4.5", x=80, y=290, at=3), B("4.5 cm", x=80, y=390, color=GREEN, at=6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Is a rhombus with sides of 4 centimetres a regular polygon? Here is Aya's working. Which line goes wrong first?",
             do=LINES("Aya", "is a rhombus regular?", ["All 4 sides are 4 cm", "So it is regular"])),
        dict(say="Line 2 is wrong. Regular means equal sides and equal angles. The angles of a rhombus are not all equal, so it is not regular.", do=[dict(a="cross", id="l2")]),
        dict(say="Equal sides are not enough. Always check the angles too.", do=[B("not regular", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Polygons around you", steps=[
        dict(say="You can find polygons everywhere. Bees build their honeycomb from hexagons, which fit together with no gaps.", do=[E("🐝", 90, 160, 100), T("honeycomb: **hexagons**, no gaps", x=230, y=190)]),
        dict(say="A stop sign is a regular octagon, so drivers can recognise it by its shape alone.", do=[E("🛑", 90, 300, 100), T("stop sign: a regular **octagon**", x=230, y=330)]),
        dict(say="And the British 50 pence coin has 7 sides. The sides are slightly curved, so that the coin rolls smoothly inside a machine.", do=[E("🪙", 90, 440, 100), T("50p coin: **7** curved sides", x=230, y=470)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.2-k4", "One last question. A regular quadrilateral is a square, a rhombus, or a rectangle? Pause the video and answer.", "A regular quadrilateral is a square, a rhombus or a rectangle?"),
        dict(say="It is a square. Only a square has 4 equal sides and 4 equal angles.", do=[SVG(POLY(REG(4, 130, -135)), 800, 150, 360), B("square", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the parts of a circle are the centre, radius, diameter, circumference, chord and tangent.", do=[T("• Circle: centre, radius, diameter, circumference, **chord**, **tangent**", x=80, y=170)]),
        dict(say="The diameter is 2 times the radius, and it is the longest chord.", do=[T("• Diameter = 2 × radius = the longest chord", x=80, y=250)]),
        dict(say="Polygons are named by their number of sides.", do=[T("• Polygons are named by their **sides**", x=80, y=330)]),
        dict(say="Regular means all sides equal, and all angles equal.", do=[T("• **Regular**: all sides and all angles equal", x=80, y=410)]),
    ]),
]

TRI = lambda v, s, x, y, w=420, at=0, pts=((0, 0), (4, 0), (0, 3)), right=(0,): SHAPE([list(p) for p in pts], x=x, y=y, w=w, at=at, v=v, s=s, right=list(right))

VIDEOS["8.3"] = [
    dict(kind="hook", title="A broken tile", steps=[
        dict(say="One floor tile is broken, and a builder needs a new one. The new tile must fit the gap exactly.", do=[E("🧱", 90, 160, 100), T("a new tile must **fit exactly**", x=230, y=190)]),
        PAUSE("8.3-k1", "A tile is the same shape as the old one, but bigger. Will it fit? Pause the video and decide.", "A tile the same shape but bigger – will it fit?"),
    ]),
    dict(kind="hook", title="Same shape and same size", steps=[
        dict(say="No. To fit the gap, the tile must be the same shape, and also the same size.", do=[B("No", x=80, y=170, color=RED), T("same **shape** and same **size**", x=80, y=280)]),
        dict(say="It can be turned round or flipped over, and it will still fit.", do=[SVG(POLY(RECT), 640, 170, 240), SVG(POLY([(90, 40), (230, 40), (230, 280), (90, 280)], G), 940, 170, 240, at=1), T("turned: still fits ✓", x=80, y=390, color=GREEN)]),
    ]),
    dict(kind="recall", title="Naming angles", steps=[
        dict(say="Remember how we name angles. Angle ABC is the angle at B, the middle letter. It is between the lines BA and BC.",
             do=[TRI(["A", "B", "C"], [], 700, 120, 480, pts=((0, 3), (0, 0), (4, 0)), right=()), B("angle ABC is at B", x=80, y=190), T("the **middle** letter", x=80, y=300)]),
    ]),
    dict(kind="idea", title="Congruent shapes", steps=[
        dict(say="Two shapes are congruent if they are exactly the same shape and the same size. One fits exactly on top of the other.",
             do=[T("**Congruent**: same shape **and** same size", x=80, y=150), TRI(["A", "B", "C"], ["4 cm", "5 cm", "3 cm"], 40, 210, 540)]),
        dict(say="You may need to turn it, or flip it over. This second triangle is turned, but its sides are still 3, 4 and 5 centimetres. The triangles are congruent.",
             do=[TRI(["X", "Z", "Y"], ["3 cm", "5 cm", "4 cm"], 640, 210, 540, pts=((0, 0), (3, 0), (0, 4))), B("congruent ✓", x=900, y=136, color=GREEN, at=7)]),
        dict(say="Shapes that are the same shape, but a different size, are not congruent.", do=[T("same shape, different size → **not** congruent", x=80, y=612, color=RED)]),
        PAUSE("8.3-k2", "Your turn. A shape and its mirror image: are they congruent, or not congruent? Pause the video and decide.", "A shape and its mirror image are congruent or not congruent?"),
    ]),
    dict(kind="idea", title="Check: a mirror image", steps=[
        dict(say="They are congruent. A reflection flips the shape, but it does not change any length or any angle.",
             do=[SVG(POLY([(40, 260), (280, 260), (40, 80)]), 560, 170, 280), SVG(DASH(160, 10, 160, 310), 760, 170, 280), SVG(POLY([(280, 260), (40, 260), (280, 80)], G), 960, 170, 280, at=1.4), B("congruent", x=80, y=200, color=GREEN),
                 T("lengths and angles stay the same", x=80, y=310)]),
    ]),
    dict(kind="idea", title="Corresponding sides and angles", steps=[
        dict(say="In congruent shapes, the matching parts are called corresponding sides and corresponding angles.", do=[T("matching parts are **corresponding**", x=80, y=150)]),
        dict(say="We write the letters in matching order. If triangle ABC is congruent to triangle XYZ, then A matches X, B matches Y, and C matches Z.",
             do=[B("ABC ≅ XYZ", x=80, y=240, color=BLUE), T("A ↔ X · B ↔ Y · C ↔ Z", x=80, y=340, at=5)]),
        dict(say="Corresponding sides are equal: AB equals XY. Corresponding angles are equal: angle B equals angle Y.", do=[MATH("AB = XY", x=80, y=440), MATH("angle B = angle Y", x=420, y=440, at=4)]),
        PAUSE("8.3-k3", "Your turn. Triangle KLM is congruent to triangle RST. Angle L is 72 degrees. What is angle S? Pause the video and try it.", "Triangles KLM ≅ RST. Angle L = 72°. Angle S = ?"),
    ]),
    dict(kind="idea", title="Check: KLM and RST", steps=[
        dict(say="L and S are both the second letter, so they are corresponding angles. Angle S is 72 degrees.", do=[B("KLM ≅ RST", x=80, y=180, color=BLUE), T("L ↔ S (second letters)", x=80, y=290), B("angle S = 72°", x=80, y=380, color=GREEN, at=4)]),
    ]),
    dict(kind="method", title="How do I decide if shapes are congruent?", steps=[
        dict(say="Here is the method. Step 1: check that the shapes are the same type, with the same number of sides.", do=[T("1. Same **type** of shape?", x=80, y=170)]),
        dict(say="Step 2: match up the corresponding sides and angles. Turn or flip the shape in your head.", do=[T("2. **Match** sides and angles (turn or flip)", x=80, y=260)]),
        dict(say="Step 3: if every matching side and angle is equal, the shapes are congruent.", do=[T("3. All equal → **congruent**", x=80, y=350)]),
        dict(say="If the shape is the same but the size is different, they are not congruent.", do=[T("4. Different size → **not** congruent", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Finding missing lengths", steps=[
        dict(say="Quadrilateral ABCD is congruent to quadrilateral EFGH. AB is 7 centimetres, BC is 5 centimetres, and EH is 4.5 centimetres. Find FG and AD.",
             do=[B("ABCD ≅ EFGH", x=80, y=150, color=BLUE), T("AB = 7 cm · BC = 5 cm · EH = 4.5 cm", x=80, y=250)]),
        dict(say="F matches B, and G matches C. So FG equals BC, which is 5 centimetres.", do=[T("F ↔ B, G ↔ C", x=80, y=350), B("FG = BC = 5 cm", x=420, y=340, color=GREEN, at=3)]),
        dict(say="A matches E, and D matches H. So AD equals EH, which is 4.5 centimetres.", do=[T("A ↔ E, D ↔ H", x=80, y=460), B("AD = EH = 4.5 cm", x=420, y=450, color=GREEN, at=3)]),
    ]),
    dict(kind="example", title="Finding an angle", steps=[
        dict(say="Triangle PQR is congruent to triangle UVW. Angle P is 45 degrees and angle Q is 75 degrees. Find angle W.", do=[B("PQR ≅ UVW", x=80, y=150, color=BLUE), T("angle P = 45° · angle Q = 75° · angle W = ?", x=80, y=250)]),
        dict(say="W is the third letter, so it matches R. First find angle R. The angles in a triangle add up to 180 degrees.", do=[T("W ↔ R (third letters)", x=80, y=340)]),
        dict(say="180 minus 45 minus 75 is 60. Angle R is 60 degrees, so angle W is 60 degrees too.", do=[MATH("180 − 45 − 75 = 60", x=80, y=430), B("angle W = 60°", x=80, y=520, color=GREEN, at=5)]),
    ]),
    dict(kind="example", title="Spot the odd one out", steps=[
        dict(say="Triangle A has sides 5, 12 and 13. Triangle B has sides 12, 13 and 5. Triangle C has sides 10, 24 and 26. Which are congruent?",
             do=[TBL(["Triangle", "Sides (cm)"], [["A", "5, 12, 13"], ["B", "12, 13, 5"], ["C", "10, 24, 26"]], y=170), ROW(0, 0.3), ROW(1, 3.4), ROW(2, 6.6)]),
        dict(say="A and B have the same 3 lengths. The order does not matter, so A and B are congruent.", do=[B("A and B: congruent ✓", x=560, y=220, color=GREEN)]),
        dict(say="Every side of C is 2 times as long. C is the same shape, but bigger. It is not congruent to the others.", do=[B("C: bigger ✗", x=560, y=340, color=RED)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Two equilateral triangles have sides of 3 centimetres and 5 centimetres. Are they congruent? Here is Noor's working. Which line goes wrong first?",
             do=LINES("Noor", "equilateral triangles, sides 3 cm and 5 cm", ["Both have angles of 60°", "Same shape, so they are congruent"])),
        dict(say="Line 2 is wrong. Congruent needs the same shape and the same size. These triangles have different side lengths.", do=[dict(a="cross", id="l2")]),
        dict(say="So they are not congruent.", do=[B("not congruent", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Made to match", steps=[
        dict(say="Factories depend on congruent shapes. Every screen protector for one model of phone is congruent, so it fits any phone of that model.", do=[E("📱", 90, 160, 100), T("every screen protector: **congruent**", x=230, y=190)]),
        dict(say="A copy of a key must be congruent to the original. If it is even slightly different, the lock will not open.", do=[E("🔑", 90, 300, 100), T("a copied key must **match exactly**", x=230, y=330)]),
        dict(say="And in a jigsaw, each piece fits only one hole: the hole that is congruent to it.", do=[E("🧩", 90, 440, 100), T("jigsaw piece ↔ its own hole", x=230, y=470)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.3-k4", "One last question. One rectangle is 4 by 6. Another is 6 by 4. Are they congruent, or not congruent? Pause the video and answer.", "Rectangles 4 × 6 and 6 × 4 are congruent or not congruent?"),
        dict(say="They are congruent. The second rectangle is the first one, turned a quarter turn.",
             do=[SVG(POLY([(40, 100), (280, 100), (280, 260), (40, 260)]), 620, 170, 260), SVG(POLY([(80, 40), (240, 40), (240, 280), (80, 280)], G), 920, 170, 260, at=1.4), B("congruent", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: congruent shapes are identical in shape and in size.", do=[T("• **Congruent**: same shape and same size", x=80, y=170)]),
        dict(say="They may be turned or flipped.", do=[T("• They may be **turned** or **flipped**", x=80, y=250)]),
        dict(say="Corresponding sides are equal, and corresponding angles are equal.", do=[T("• **Corresponding** sides and angles are equal", x=80, y=330)]),
        dict(say="Write the letters of congruent shapes in matching order.", do=[T("• Write the letters in **matching order**", x=80, y=410)]),
    ]),
]

NET = [[1, 0], [0, 1], [1, 1], [2, 1], [3, 1], [1, 2]]

VIDEOS["8.4"] = [
    dict(kind="hook", title="Boxes and tubes", steps=[
        dict(say="Look at packaging in a shop. Cereal comes in a cuboid. Tennis balls come in a cylinder. And some chocolate bars come in a triangular prism.",
             do=[E("📦", 90, 160, 100), T("cuboid · cylinder · **triangular prism**", x=230, y=190), SOLID("triprism", at=5)]),
        PAUSE("8.4-k1", "How many faces does a triangular prism have? Pause the video and count them.", "How many faces does a triangular prism have?"),
    ]),
    dict(kind="hook", title="Faces of a triangular prism", steps=[
        dict(say="There is a triangle at each end. That is 2 faces. Between them there are 3 rectangles. 2 plus 3 makes 5 faces.",
             do=[SOLID("triprism"), T("2 **triangles**", x=80, y=180), T("3 **rectangles**", x=80, y=270, at=3), MATH("2 + 3 = 5 faces", x=80, y=380, color=GREEN, at=6)]),
    ]),
    dict(kind="recall", title="Faces, edges and vertices", steps=[
        dict(say="Remember 3 words. A face is a surface of the shape. An edge is a line where 2 faces meet. A vertex is a corner.",
             do=[SOLID("cuboid"), T("**face**: a surface", x=80, y=170), T("**edge**: where 2 faces meet", x=80, y=250, at=2.6), T("**vertex**: a corner", x=80, y=330, at=5.6)]),
        dict(say="A cube has 6 faces, 12 edges and 8 vertices.", do=[B("cube: 6 faces, 12 edges, 8 vertices", x=80, y=450, color=BLUE)]),
    ]),
    dict(kind="idea", title="Prisms and pyramids", steps=[
        dict(say="A prism has the same cross-section all the way along. A triangular prism has a triangle at both ends.", do=[T("**Prism**: the same cross-section all along", x=80, y=160), SOLID("triprism", x=80, y=260, w=400)]),
        dict(say="A pyramid has a flat base, and triangle faces that meet at one point, called the apex.", do=[T("**Pyramid**: a base, and triangles meeting at the **apex**", x=600, y=230), SOLID("pyramid", x=700, y=300, w=400)]),
        PAUSE("8.4-k2", "Your turn. How many vertices does a square-based pyramid have? Pause the video and count them.", "How many vertices does a square-based pyramid have?"),
    ]),
    dict(kind="idea", title="Check: vertices of a pyramid", steps=[
        dict(say="The square base has 4 corners. Then there is 1 more at the apex. 4 plus 1 makes 5 vertices.", do=[SOLID("pyramid"), T("4 on the **base**", x=80, y=180), T("1 at the **apex**", x=80, y=270, at=2.6), MATH("4 + 1 = 5 vertices", x=80, y=380, color=GREEN, at=5)]),
    ]),
    dict(kind="idea", title="Counting faces, edges and vertices", steps=[
        dict(say="Here are the numbers for some common shapes. A cuboid has 6 faces, 12 edges and 8 vertices, the same as a cube.",
             do=[TBL(["Shape", "Faces", "Edges", "Vertices"], [["cuboid", "6", "12", "8"], ["triangular prism", "5", "9", "6"], ["square-based pyramid", "5", "8", "5"], ["tetrahedron", "4", "6", "4"]], y=160), ROW(0, 3)]),
        dict(say="A triangular prism has 5 faces, 9 edges and 6 vertices. A square-based pyramid has 5 faces, 8 edges and 5 vertices.", do=[ROW(1, 0.3), ROW(2, 5)]),
        dict(say="A tetrahedron is a pyramid with a triangle base. It has 4 faces, 6 edges and 4 vertices.", do=[ROW(3, 0.3)]),
        dict(say="Here is a check for shapes with flat faces. Faces plus vertices, minus edges, always equals 2. For the cuboid: 6 plus 8 minus 12 is 2.",
             do=[B("F + V − E = 2", x=80, y=440, color=BLUE), MATH("6 + 8 − 12 = 2", x=520, y=446, at=6), E("✅", 860, 436, 50, at=9)]),
    ]),
    dict(kind="idea", title="Views", steps=[
        dict(say="We can draw a 3D shape from different directions: the front view, the side view, and the top view, which is also called the plan.", do=[T("**front** view · **side** view · **top** view (plan)", x=80, y=160)]),
        dict(say="Stand a cylinder upright. From the front it looks like a rectangle. From the top it looks like a circle.",
             do=[SOLID("cylinder", x=80, y=240, w=400), SVG(POLY([(90, 60), (230, 60), (230, 260), (90, 260)]) + TXT(160, 300, "front"), 560, 260, 260, at=2.6),
                 SVG(f'<circle cx="160" cy="150" r="90" fill="{FILL}" stroke="{INK}" stroke-width="3"/>' + TXT(160, 300, "top"), 880, 260, 260, at=5.4)]),
        PAUSE("8.4-k3", "Your turn. A cone stands on its base. What does its top view look like? Pause the video and decide.", "The top view of a cone standing on its base is a …"),
    ]),
    dict(kind="idea", title="Check: a cone from above", steps=[
        dict(say="From above, you see the round base as a circle, and the apex as a dot at the centre.", do=[SOLID("cone", x=80, y=170, w=440), SVG(CIRC, 760, 180, 340, at=1.6), B("a circle with a dot", x=660, y=560, color=GREEN, at=3)]),
    ]),
    dict(kind="idea", title="Nets", steps=[
        dict(say="A net is a flat shape that folds up to make a 3D shape. This cross is made of 6 squares.", do=[CELLS(NET, cols=4, rows=3), T("**Net**: a flat shape that **folds up**", x=80, y=170)]),
        dict(say="The row of 4 squares wraps round to make 4 sides. The other 2 squares fold over, to make the top and the bottom. It is a net of a cube.",
             do=[CELLS([[1, 0, G], [1, 2, G]], cols=4, rows=3, at=5), T("row of 4 → the **sides**", x=80, y=280), T("2 more → **top** and **bottom**", x=80, y=370, at=5), B("a net of a cube", x=80, y=470, color=GREEN, at=9)]),
    ]),
    dict(kind="method", title="How do I describe a 3D shape?", steps=[
        dict(say="Here is the method. Step 1: decide if it is a prism or a pyramid, and name the shape of its base.", do=[T("1. **Prism** or **pyramid**? Which base?", x=80, y=170)]),
        dict(say="Step 2: count the faces, then the edges, then the vertices. Work in order: top, bottom, then around the sides.", do=[T("2. Count **faces**, **edges**, **vertices** in order", x=80, y=260)]),
        dict(say="Step 3: check with faces plus vertices minus edges equals 2.", do=[T("3. Check: **F + V − E = 2**", x=80, y=350)]),
        dict(say="Step 4: for a view, imagine looking straight at the shape from that direction.", do=[T("4. Views: look **straight at** the shape", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A hexagonal pyramid", steps=[
        dict(say="Count the faces, edges and vertices of a pyramid with a hexagon as its base.", do=[SVG(POLY(REG(6, 120, 0)) + "".join(LINE(160, 160, round(px), round(py), GREY) for px, py in REG(6, 120, 0)) + DOT(160, 160, RED, 7) + TXT(160, 310, "top view", GREY, 20), 860, 140, 340)]),
        dict(say="Faces: 1 hexagon and 6 triangles. That is 7 faces.", do=[MATH("faces: 1 + 6 = 7", x=80, y=170)]),
        dict(say="Edges: 6 around the base, and 6 going up to the apex. That is 12 edges.", do=[MATH("edges: 6 + 6 = 12", x=80, y=260)]),
        dict(say="Vertices: 6 on the base, and 1 apex. That is 7 vertices.", do=[MATH("vertices: 6 + 1 = 7", x=80, y=350)]),
        dict(say="Check: 7 plus 7 minus 12 equals 2. Correct.", do=[MATH("7 + 7 − 12 = 2", x=80, y=460, color=GREEN), E("✅", 420, 450, 50, at=3)]),
    ]),
    dict(kind="example", title="Which shape is it?", steps=[
        dict(say="A shape has a triangle as its front view. Its side view is a rectangle, and its top view is a rectangle. What is it?",
             do=[SVG(POLY([(60, 250), (260, 250), (160, 70)]) + TXT(160, 300, "front"), 80, 170, 240), SVG(POLY(RECT) + TXT(160, 300, "side"), 360, 170, 240, at=3), SVG(POLY(RECT) + TXT(160, 300, "top"), 640, 170, 240, at=5.4)]),
        dict(say="It is a triangle from one direction, and rectangles from the others. It is a triangular prism, lying on one of its rectangle faces.", do=[SOLID("triprism", x=900, y=150, w=340), B("triangular prism", x=80, y=500, color=GREEN, at=4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="How many edges does a square-based pyramid have? Here is Omar's working. Which line goes wrong first?",
             do=LINES("Omar", "the edges of a square-based pyramid", ["4 edges around the base", "plus 1 going up to the apex", "total 5"]) + [SOLID("pyramid", x=860, y=180, w=360)]),
        dict(say="Line 2 is wrong. There is an edge from every corner of the base up to the apex. That is 4 edges, not 1.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="4 plus 4 is 8. A square-based pyramid has 8 edges.", do=[B("4 + 4 = 8 edges", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Shapes that work", steps=[
        dict(say="The Great Pyramid in Egypt is a square-based pyramid. It was built about 4,500 years ago, and it is about 139 metres tall.", do=[E("🏜️", 90, 160, 100), T("Great Pyramid: about **139 m** tall", x=230, y=190)]),
        dict(say="Drink cans are cylinders. A cylinder is strong, it is easy to hold, and cans stack neatly on top of each other.", do=[E("🥫", 90, 300, 100), T("cans: **cylinders** that stack", x=230, y=330)]),
        dict(say="And a classic football is stitched from 32 flat panels: 12 pentagons and 20 hexagons.", do=[E("⚽", 90, 440, 100), T("football: **12** pentagons + **20** hexagons", x=230, y=470)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("8.4-k4", "One last question. A shape with flat faces has 7 faces and 10 vertices. How many edges does it have? Pause the video and work it out.", "A shape has 7 faces and 10 vertices. How many edges?"),
        dict(say="Faces plus vertices minus edges equals 2. 7 plus 10 is 17, and 17 minus 2 is 15. It has 15 edges. It is a prism with a pentagon at each end.",
             do=[B("F + V − E = 2", x=80, y=170, color=BLUE), MATH("7 + 10 = 17", x=80, y=280, at=3), MATH("17 − 2 = 15 edges", x=80, y=370, color=GREEN, at=5.4), T("a pentagonal prism", x=80, y=480, at=9)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a prism has the same cross-section all along. A pyramid comes to a point, the apex.", do=[T("• **Prism**: same cross-section · **Pyramid**: an apex", x=80, y=170)]),
        dict(say="Count faces, edges and vertices in order.", do=[T("• Count **faces**, **edges**, **vertices** in order", x=80, y=250)]),
        dict(say="For flat-faced shapes, faces plus vertices minus edges equals 2.", do=[T("• **F + V − E = 2**", x=80, y=330)]),
        dict(say="The front, side and top views show a shape from 3 directions, and a net folds up to make it.", do=[T("• **Views** from 3 directions · a **net** folds up", x=80, y=410)]),
    ]),
]
