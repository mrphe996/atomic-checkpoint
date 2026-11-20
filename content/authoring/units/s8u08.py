# -*- coding: utf-8 -*-
"""Stage 8 Unit 8 – Forces and Motion. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Physics"
BLURB = "Calculating speed and average speed, reading and drawing distance–time graphs, balanced and unbalanced forces, and moments."
OBJECTIVES = {
    "O1": {"sec": "8.1", "code": "8Pf.01, 8TWSc.04", "codeNote": "", "t": "Calculate speed, distance and time, find average speed and compare ways of measuring speed."},
    "O2": {"sec": "8.2", "code": "8Pf.02", "codeNote": "", "t": "Interpret and draw distance–time graphs."},
    "O3": {"sec": "8.3", "code": "8Pf.03", "codeNote": "", "t": "Work out resultant forces and describe how balanced and unbalanced forces affect motion."},
    "O4": {"sec": "8.4", "code": "8Pf.04", "codeNote": "", "t": "Calculate moments (moment = force × distance) and identify levers and pivots."},
}
SECTIONS = [
    {"id": "8.1", "title": "Speed", "objs": ["O1"]},
    {"id": "8.2", "title": "Distance–time graphs", "objs": ["O2"]},
    {"id": "8.3", "title": "Characteristics of forces", "objs": ["O3"]},
    {"id": "8.4", "title": "Turning effect of a force", "objs": ["O4"]},
]
u = Unit(8, 8)

# ---------------------------------------------------------------- 8.1
u.sec("8.1", "O1")
u.nm("r", "An athlete runs 100 m in 10 s. What is her speed?", 10, "m/s")
u.nm("r", "A car travels 150 km at 50 km/h. How long does the journey take?", 3, "h")
u.tb("r", "Use speed = distance ÷ time. Complete the table.", ["Distance (m)", "Time (s)", "Speed (m/s)"], [["600", "120", B(5)], ["90", "30", B(3)], ["1000", "40", B(25)]])
u.gd("r", "About how fast does each move?", "Typical speed", [("Walking person", "1 m/s"), ("Car in town", "15 m/s"), ("Train", "30 m/s"), ("Plane", "250 m/s")])
u.ex("r", "Explain why electronic timing gates give a more accurate speed than a stopwatch.", [("stopwatch depends on human reaction time", ["reaction"]), ("gates start and stop automatically / beam", ["beam|automatic|infrared|electronic"]), ("more precise times", ["precise|accurate|thousandth"])],
     "A stopwatch depends on human reaction time, which adds error. Timing gates start and stop automatically when a card breaks an infrared beam, giving very precise times.")
u.nm("r", "An athlete covers 5 m, 6 m and 7 m in the first three seconds. What is her average speed?", 6, "m/s", d="H")
u.mc("r", "Why did the Mars Climate Orbiter crash in 1999?", "Two teams used different units for thrust", [("It ran out of fuel", "No."), ("It hit an asteroid", "No."), ("It was too slow", "No.")], d="H")
u.mc("r", "A two-point speed camera measures…", "the average speed between two points", [("the top speed only", "No."), ("the mass of the car", "No."), ("the driver's reaction time", "No.")], d="VH")
for p, r, w in [
    ("Speed is the distance travelled in each…", "unit of time", ["unit of mass", "kilogram", "metre squared"]),
    ("The SI unit of speed is…", "metres per second", ["kilograms", "newtons", "metres"]),
    ("Which formula gives speed?", "distance ÷ time", ["time ÷ distance", "distance × time", "mass × time"]),
    ("Distance =", "speed × time", ["speed ÷ time", "time ÷ speed", "speed + time"]),
    ("Which formula gives time taken?", "distance ÷ speed", ["speed × distance", "speed ÷ distance", "distance + speed"]),
    ("An object that is not moving has a speed of…", "zero", ["1 m/s", "it depends", "10 m/s"]),
    ("For long journeys we often use…", "km/h", ["mm/s", "N", "kg"]),
    ("Speeding up is called…", "accelerating", ["decelerating", "balancing", "pivoting"]),
    ("Slowing down is called…", "decelerating", ["accelerating", "terminal speed", "turning"]),
    ("Average speed =", "total distance ÷ total time", ["top speed ÷ 2", "distance × time", "time ÷ distance"]),
    ("A radar speed camera sends out…", "radio waves", ["sound only", "light beams only", "magnets"]),
    ("Timing gates use…", "an infrared beam", ["a stopwatch", "a ruler", "a magnet"]),
    ("Races are timed electronically to…", "a thousandth of a second", ["a minute", "an hour", "a tenth of a minute"]),
    ("A runner covers 200 m in 25 s. Speed?", "8 m/s", ["5000 m/s", "0.125 m/s", "225 m/s"]),
    ("A cyclist goes at 5 m/s for 60 s. Distance?", "300 m", ["12 m", "65 m", "0.08 m"]),
]:
    u.mc("p", p, r, w)
u.nm("p", "A train goes 90 km in 1.5 h. Speed in km/h?", 60, "km/h")
u.od("p", "Order from slowest to fastest.", ["Walking (1 m/s)", "Running (3 m/s)", "Car (15 m/s)", "Plane (250 m/s)"])
u.mt("p", "Match the quantity to its unit.", [("Speed", "m/s"), ("Distance", "m"), ("Time", "s")])
u.nm("a", "A car travels at 20 m/s. How far does it go in 2 minutes?", 2400, "m")
u.nm("a", "Two cameras 1.2 km apart record a car taking 40 s between them. What is the average speed in m/s?", 30, "m/s")
u.ex("a", "* Advanced. A speed limit is 25 m/s. A car's average speed between two cameras is 24 m/s. Explain why the driver may still have broken the limit.", [("average speed only", ["average"]), ("speed changes / may have gone faster at times", ["faster|varied|changed|sometimes|top speed"])],
     "The cameras only measure average speed. The car could have gone faster than 25 m/s for part of the journey and slower for another part, giving an average of 24 m/s.")
u.mc("a", "Why is it important to state units with every measurement?", "Mixing units gives wrong answers, as the Mars orbiter crash showed.", ["Units make numbers bigger.", "Units are optional.", "Only teachers need units."], skill="Reasoning")
u.stop("a plane about 250 metres per second", "Which moves fastest?", "A plane", ["A walking person", "A car", "A train"])
u.stop("10 metres per second", "Speed is calculated by…", "distance ÷ time", ["time ÷ distance", "distance × time", "mass ÷ time"])
u.stop("an average speed of 6 metres per second", "Average speed =", "total distance ÷ total time", ["top speed", "distance × time", "time ÷ distance"])
u.stop("which depends on human reaction time", "Timing gates are more accurate than stopwatches because…", "they don't depend on reaction time", ["they are bigger", "they use sound", "they are cheaper"])

# ---------------------------------------------------------------- 8.2
u.sec("8.2", "O2")
u.gd("r", "What does each line on a distance–time graph show?", "Motion", [("Horizontal line", "Not moving"), ("Straight sloping line", "Constant speed"), ("Curve getting steeper", "Speeding up")])
u.gr("r", "Lee runs 8 km in 1 h, rests 0.5 h, then runs 8 km more in 1.5 h. Plot his distance–time graph.", {"label": "Time (h)", "min": 0, "max": 3, "step": 0.5}, {"label": "Distance (km)", "min": 0, "max": 16, "step": 4}, [[0, 0], [1, 8], [1.5, 8], [3, 16]])
u.mc("r", "On a distance–time graph, a steeper line means…", "faster motion", [("slower motion", "No."), ("not moving", "That is flat."), ("going backwards", "No.")])
u.ex("r", "Lee's graph has two sloping parts, A–B and C–D. Explain why C–D is less steep.", [("C–D slower", ["slow"]), ("same distance in more time", ["more time|longer|1.5"])],
     "He ran the same 8 km but took 1.5 hours instead of 1 hour, so he was running more slowly, and the line is less steep.")
u.nm("r", "Lee runs 8 km in 1.5 h on the last part. What is his speed (1 decimal place)?", 5.3, "km/h", tol=0.05, d="H")
u.mc("r", "Where the cheetah's and man's lines cross, the man…", "overtakes the cheetah", [("stops", "No."), ("is faster than ever", "No."), ("turns back", "No.")], d="H")
u.mc("r", "The cheetah's line goes flat after about 20 s. This shows it has…", "stopped", ["sped up", "slowed slightly", "turned round"])
u.mc("r", "A line curving and becoming less steep shows the object is…", "slowing down", ["speeding up", "stopped", "at constant speed"], d="VH")
for p, r, w in [
    ("On a distance–time graph, time goes on the…", "horizontal axis", ["vertical axis", "diagonal", "key"]),
    ("Distance goes on the…", "vertical axis", ["horizontal axis", "title", "key"]),
    ("A flat horizontal line means…", "the object is not moving", ["constant speed", "speeding up", "slowing"]),
    ("A straight line sloping upwards means…", "constant speed", ["stopped", "speeding up", "going back"]),
    ("A curved line means…", "the speed is changing", ["constant speed", "not moving", "no time passing"]),
    ("Lee's resting part of the graph is…", "horizontal", ["very steep", "curved up", "vertical"]),
    ("Lee's first run: 8 km in 1 h. Speed?", "8 km/h", ["1 km/h", "16 km/h", "0.125 km/h"]),
    ("The cheetah stopped after running…", "400 m", ["800 m", "40 m", "4000 m"]),
    ("The man ran on to…", "800 m", ["400 m", "100 m", "2000 m"]),
    ("Which lesson does the cheetah and man race show?", "Endurance matters as well as speed", ["Cheetahs always win", "Humans are faster", "Speed is everything"]),
    ("A steeper straight line than another means…", "higher constant speed", ["lower speed", "stopped", "speeding up"]),
    ("The gradient of a distance–time graph shows…", "speed", ["mass", "force", "time only"]),
    ("Two runners with parallel lines have…", "the same speed", ["different speeds", "stopped", "the same distance always"]),
    ("A line from (0,0) to (10 s, 50 m) shows a speed of…", "5 m/s", ["50 m/s", "500 m/s", "0.2 m/s"]),
    ("If a graph line goes back down towards zero distance, the object is…", "returning towards the start", ["stopped", "speeding up away", "flying"]),
]:
    u.mc("p", p, r, w)
u.gd("p", "Which runner is faster?", "Faster", [("A: 100 m in 20 s or B: 100 m in 25 s", "A"), ("A: 50 m in 10 s or B: 80 m in 10 s", "B")])
u.nm("p", "A graph line goes from 0 m at 0 s to 120 m at 40 s. What is the speed?", 3, "m/s")
u.ms("p", "Select ALL the parts of Lee's run where he was moving.", ["A to B", "C to D"], ["B to C"])
u.gr("a", "* Advanced. A cyclist: 0 m at 0 s, 100 m at 20 s, 100 m at 40 s, 300 m at 80 s. Plot the graph.", {"label": "Time (s)", "min": 0, "max": 80, "step": 20}, {"label": "Distance (m)", "min": 0, "max": 300, "step": 100}, [[0, 0], [20, 100], [40, 100], [80, 300]])
u.nm("a", "Using the cyclist's graph, what is the speed between 40 s and 80 s?", 5, "m/s")
u.nm("a", "What is the cyclist's average speed for the whole 80 s?", 3.75, "m/s", tol=0.01)
u.ex("a", "* Advanced. Describe how a distance–time graph for a car pulling away from traffic lights would look, and explain why.", [("starts flat / at zero", ["flat|zero|start"]), ("curve getting steeper", ["curve|steeper"]), ("because it is accelerating", ["accelerat|speeding up"])],
     "The line starts at zero and curves upwards, getting steeper, because the car is accelerating – it covers more distance every second.")
u.stop("its distance stays the same", "A horizontal line on a distance–time graph means…", "not moving", ["constant speed", "speeding up", "slowing down"])
u.stop("the faster the object is moving", "A steeper line means…", "faster", ["slower", "stopped", "backwards"])
u.stop("because he's running more slowly", "Lee rests for half an hour. That part of the graph is…", "horizontal", ["steep", "curved", "vertical"])

# ---------------------------------------------------------------- 8.3
u.sec("8.3", "O3")
u.nm("r", "A ball is pushed right with 12 N and left with 5 N. What is the resultant force to the right?", 7, "N")
u.gd("r", "Balanced or unbalanced forces?", "Forces", [("Lorry at constant speed", "Balanced"), ("Car speeding up", "Unbalanced"), ("Skydiver at terminal speed", "Balanced"), ("Book sliding to a stop", "Unbalanced")])
u.tb("r", "Work out the resultant force (right is positive).", ["Forces right (N)", "Forces left (N)", "Resultant (N)"], [["20", "8", B(12)], ["100 + 50", "180", B(-30)]])
u.ex("r", "Explain why a skydiver reaches a steady terminal speed.", [("air resistance increases with speed", ["air resistance|drag"]), ("air resistance equals weight / gravity", ["equal|balance"]), ("balanced forces – no change in speed", ["balanced|steady|constant"])],
     "As he falls faster, air resistance increases until it equals his weight. The forces are then balanced, so his speed stays the same – terminal speed.")
u.mc("r", "Balanced forces on a moving object…", "keep it moving at the same speed and direction", [("always stop it", "No."), ("make it speed up", "That needs unbalanced forces."), ("make it turn", "No.")])
u.mc("r", "Forces are drawn as arrows because they have…", "size and direction", [("only size", "No."), ("only colour", "No."), ("mass and volume", "No.")])
u.mc("r", "Which three effects can unbalanced forces have?", "Speed up, slow down or change direction", [("Only speed up", "No."), ("Change mass", "No."), ("Change colour", "No.")], d="H")
u.mc("r", "Why do streamlined shapes help vehicles save fuel?", "They reduce air resistance, so less engine force is needed", [("They make vehicles heavier", "No."), ("They increase friction", "No."), ("They add drag", "No.")], d="VH")
for p, r, w in [
    ("In a tug of war with 5 N each way, the resultant force is…", "0 N", ["10 N", "5 N", "25 N"]),
    ("When the resultant force is zero, the forces are…", "balanced", ["unbalanced", "turning", "missing"]),
    ("A lorry at constant speed: engine force is balanced by…", "friction and air resistance", ["gravity only", "magnetism", "nothing"]),
    ("Terminal speed is when air resistance equals…", "weight", ["mass", "friction on the ground", "zero"]),
    ("Unbalanced forces cause…", "a change in motion", ["no change", "balanced motion", "zero resultant"]),
    ("A bat hitting a ball changes the ball's…", "direction and speed", ["mass", "colour", "material"]),
    ("Friction slowing a sliding book is an…", "unbalanced force", ["balanced force", "moment", "speed"]),
    ("Air resistance grows with…", "speed and surface area", ["mass only", "colour", "temperature only"]),
    ("Forces are measured in…", "newtons", ["metres", "joules", "seconds"]),
    ("Resultant force means…", "the overall force when all forces are combined", ["the biggest force", "the smallest force", "the weight only"]),
    ("30 N left and 10 N right gives…", "20 N left", ["40 N right", "20 N right", "0 N"]),
    ("A car accelerating has a resultant force…", "forwards", ["backwards", "of zero", "upwards"]),
    ("Lower speeds help vehicles use less fuel because…", "air resistance is smaller", ["engines are bigger", "mass is less", "friction is zero"]),
    ("If forces on a still object are balanced, it…", "stays still", ["starts moving", "spins", "falls through the floor"]),
    ("Counting right as positive, a force to the left is…", "negative", ["positive", "zero", "a moment"]),
]:
    u.mc("p", p, r, w)
u.nm("p", "Forces of 25 N right and 40 N left act on a box. What is the size of the resultant force?", 15, "N")
u.ms("p", "Select ALL the situations with unbalanced forces.", ["A rocket lifting off", "A car braking", "A ball being kicked"], ["A book resting on a table", "A car at constant speed"])
u.od("p", "Order the skydiver's fall.", ["Jumps – weight bigger than air resistance", "Speeds up – air resistance increases", "Air resistance equals weight", "Falls at terminal speed"])
u.nm("a", "A box has 60 N and 45 N pushing right and 70 N and 20 N pushing left. What is the resultant force to the right?", 15, "N")
u.ex("a", "* Advanced. A skydiver opens a parachute. Explain what happens to the forces and her speed.", [("air resistance increases suddenly", ["air resistance.*(increase|bigger)|more air resistance"]), ("unbalanced – resultant upwards – slows down", ["unbalanced|slow|decelerat"]), ("new lower terminal speed when balanced again", ["lower terminal|balanced again|new terminal|steady"])],
     "The large parachute suddenly increases air resistance, so it is bigger than her weight. The forces are unbalanced and she slows down until they balance again at a new, lower terminal speed.")
u.mc("a", "A spacecraft in deep space with its engine off keeps moving at a steady speed. Why?", "There are no unbalanced forces to change its motion.", ["Its engine pushes it.", "Gravity pushes it forward.", "Space has strong friction."], skill="Reasoning")
u.mc("a", "Why do cyclists crouch low when racing?", "To reduce their surface area and air resistance", ["To increase air resistance", "To change their mass", "To balance friction"], skill="Reasoning")
u.stop("and the rope doesn't move", "When opposite forces are equal, they are…", "balanced", ["unbalanced", "turning", "zero mass"])
u.stop("called the terminal speed", "At terminal speed, air resistance equals…", "the weight", ["zero", "the mass", "friction"])
u.stop("and the box moves left", "Push right 12 N and left 5 N. The resultant is…", "7 N right", ["17 N right", "7 N left", "0 N"])

# ---------------------------------------------------------------- 8.4
u.sec("8.4", "O4")
u.nm("r", "A motorist pushes on a wrench with 70 N, 0.4 m from the nut. What is the moment?", 28, "Nm")
u.tb("r", "Moment = force × distance. Complete the table.", ["Force (N)", "Distance (m)", "Moment (Nm)"], [["50", "0.2", B(10)], ["30", "0.5", B(15)], ["120", "0.25", B(30)]])
u.gd("r", "Clockwise or anticlockwise moment? (seesaw pivot in the middle)", "Turning", [("Weight on the right side", "Clockwise"), ("Weight on the left side", "Anticlockwise")])
u.ex("r", "Explain why a door is easier to open if you push near the handle, far from the hinges.", [("moment = force × distance", ["force.*distance|moment"]), ("bigger distance from pivot / hinge", ["distance|far|further"]), ("so less force needed for same moment", ["less force|easier|smaller force"])],
     "Moment = force × distance from the pivot. Pushing far from the hinges gives a bigger distance, so a smaller force gives the same turning effect.")
u.mc("r", "The pivot point of a lever is called the…", "fulcrum", [("load", "No."), ("effort", "No."), ("moment", "No.")])
u.mc("r", "The unit of moment is…", "newton metres (Nm)", [("newtons", "That is force."), ("metres", "No."), ("joules", "No.")])
u.mc("r", "Why does a long spanner make a tight nut easier to loosen?", "The bigger distance gives a bigger moment for the same force", [("It is heavier", "No."), ("It reduces friction", "No."), ("It makes the nut smaller", "No.")], d="H")
u.mc("r", "Galileo found that a lever's balance depends on…", "both the weights and their distances from the pivot", [("only the weights", "No."), ("only the distances", "No."), ("the colour of the lever", "No.")], d="VH")
for p, r, w in [
    ("The turning effect of a force is a…", "moment", ["speed", "pressure", "mass"]),
    ("Moment =", "force × distance from the pivot", ["force ÷ distance", "mass × speed", "distance ÷ time"]),
    ("A door turns about its…", "hinges", ["handle", "lock", "floor"]),
    ("Pushing near the hinges makes a door…", "very hard to open", ["easier to open", "open faster", "lighter"]),
    ("Which is a lever?", "Scissors", ["A balloon", "A glass of water", "A magnet"]),
    ("A wheelbarrow is a…", "lever", ["pulley", "magnet", "spring"]),
    ("Bones and joints in our bodies act as…", "levers", ["magnets", "batteries", "springs only"]),
    ("A force of 10 N at 2 m gives a moment of…", "20 Nm", ["5 Nm", "12 Nm", "0.2 Nm"]),
    ("A force of 50 N at 0.2 m gives…", "10 Nm", ["250 Nm", "50.2 Nm", "2.5 Nm"]),
    ("Moments, like forces, have…", "direction", ["colour", "temperature", "mass"]),
    ("Turning the same way as clock hands is…", "clockwise", ["anticlockwise", "balanced", "resultant"]),
    ("A seesaw is a…", "lever", ["pulley", "gear", "wheel"]),
    ("A stapler is a…", "lever", ["spring only", "magnet", "battery"]),
    ("Pressing a light switch uses a…", "moment", ["chemical reaction", "magnetic field", "sound wave"]),
    ("To get a bigger moment with the same force you can…", "push further from the pivot", ["push nearer the pivot", "push with less force", "remove the pivot"]),
]:
    u.mc("p", p, r, w)
u.nm("p", "What force is needed at 0.5 m from a pivot to make a moment of 20 Nm?", 40, "N")
u.ms("p", "Select ALL the levers.", ["Pliers", "Wheelbarrow", "Seesaw"], ["Balloon", "Thermometer"])
u.mt("p", "Match the word to its meaning.", [("Fulcrum", "the pivot"), ("Moment", "turning effect"), ("Lever", "simple machine that turns about a pivot")])
u.nm("a", "A girl weighing 400 N sits 1.5 m from a seesaw pivot. How far from the pivot must a 600 N boy sit to balance it?", 1, "m")
u.ex("a", "* Advanced. Explain how you could balance a seesaw when one child is much heavier than the other.", [("heavier child sits nearer the pivot", ["heavier.*(near|closer)|closer.*heav"]), ("lighter child further away", ["lighter.*(further|far)"]), ("moments equal: force × distance same each side", ["equal|same moment|balance"])],
     "The heavier child sits nearer the pivot and the lighter child further away, so that force × distance is the same on both sides and the moments balance.")
u.nm("a", "A 30 N force acts 0.6 m from a pivot clockwise, and a 20 N force acts 0.8 m anticlockwise. What is the overall moment (clockwise positive)?", 2, "Nm")
u.mc("a", "Why are door handles placed on the side away from the hinges?", "It gives the largest distance from the pivot, so the door opens with the least force.", ["It looks better.", "It reduces the door's mass.", "It makes the hinges stronger."], skill="Reasoning")
u.stop("called the fulcrum", "The pivot point of a lever is the…", "fulcrum", ["load", "moment", "handle"])
u.stop("measured in newton metres", "Moment =", "force × distance", ["force ÷ distance", "mass × speed", "distance ÷ time"])
u.stop("That's why a long spanner makes nuts easier to loosen", "70 N acting 0.4 m from a nut gives a moment of…", "28 Nm", ["70.4 Nm", "175 Nm", "17.5 Nm"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Forces and motion", "sec": None, "kids": [
    {"id": "sp", "t": "Speed", "d": "Speed = distance ÷ time • m/s, km/h • Average speed", "obj": "O1", "sec": "8.1"},
    {"id": "ms", "t": "Measuring speed", "d": "Radar cameras • Two-point cameras • Timing gates", "obj": "O1", "sec": "8.1"},
    {"id": "dt", "t": "Distance–time graphs", "d": "Flat – stopped • Straight slope – constant speed • Steeper – faster", "obj": "O2", "sec": "8.2"},
    {"id": "bf", "t": "Balanced forces", "d": "Resultant = 0 • No change in motion • Terminal speed", "obj": "O3", "sec": "8.3"},
    {"id": "uf", "t": "Unbalanced forces", "d": "Speed up • Slow down • Change direction", "obj": "O3", "sec": "8.3"},
    {"id": "mo", "t": "Moments", "d": "Moment = force × distance • Nm • Clockwise and anticlockwise", "obj": "O4", "sec": "8.4"},
    {"id": "lv", "t": "Levers", "d": "Fulcrum • Seesaw, scissors, wheelbarrow • Bones", "obj": "O4", "sec": "8.4"},
]}
