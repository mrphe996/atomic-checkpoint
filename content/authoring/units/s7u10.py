# -*- coding: utf-8 -*-
"""Stage 7 Unit 10 – Forces. Written by the Atomic teaching team."""
from c_kit import *

STRAND = "Physics"
BLURB = "Contact and non-contact forces, force diagrams and newtons, gravity, the difference between mass and weight, and air resistance."

OBJECTIVES = {
    "O1": {"sec": "10.1", "code": "7TWSm.01", "codeNote": "force diagrams as models", "t": "Identify contact and non-contact forces, draw force diagrams and measure forces in newtons."},
    "O2": {"sec": "10.2", "code": "7Pf.03, 7ESs.02", "codeNote": "", "t": "Describe gravity as an attraction that depends on mass and distance and keeps objects in orbit."},
    "O3": {"sec": "10.3", "code": "7Pf.03", "codeNote": "mass and weight", "t": "Distinguish mass (kg) from weight (N) and explain why weight changes from place to place."},
    "O4": {"sec": "10.4", "code": "7Pf.04, 7SIC.01", "codeNote": "", "t": "Explain air resistance, why there is none in a vacuum, and how ideas about gravity developed."},
}

SECTIONS = [
    {"id": "10.1", "title": "Forces around us", "objs": ["O1"]},
    {"id": "10.2", "title": "Gravity", "objs": ["O2"]},
    {"id": "10.3", "title": "Mass and weight", "objs": ["O3"]},
    {"id": "10.4", "title": "Air resistance", "objs": ["O4"]},
]

S1_REQ = [
    gd("u10s1r1", "M", "O1", "Contact or non-contact force?", ["Type"],
       [("Friction", ["Contact"]), ("Gravity", ["Non-contact"]), ("Tension", ["Contact"]), ("Magnetic force", ["Non-contact"]), ("Normal force", ["Contact"])], skill="Data"),
    mc("u10s1r2", "M", "O1", "A force is…", ("a push or a pull", "Correct."), [("a type of energy", "No."), ("a mass", "No."), ("a speed", "No.")]),
    mc("u10s1r3", "M", "O1", "Force is measured in…", ("newtons (N)", "Correct."), [("kilograms", "Mass."), ("metres", "Length."), ("joules", "Energy.")]),
    mc("u10s1r4", "H", "O1", "In a force diagram, the length of the arrow shows…", ("the size of the force", "Correct."), [("the colour", "No."), ("the mass", "No."), ("the time", "No.")]),
    ms("u10s1r5", "M", "O1", "Select ALL the things a force can change.", ["Speed", "Direction", "Shape"], [("Mass", "No."), ("Colour", "No.")]),
    tb("u10s1r6", "H", "O1", "Gravity pulls about 1 N on every 100 g. Complete the table.", ["Mass (g)", "Weight on Earth (N)"],
       [["100", "1"], ["300", B(3)], ["550", B(5.5)]], skill="Data"),
    ex("u10s1r7", "H", "O1", "Explain how a force meter (newton meter) measures a force.",
       [("spring stretches", ["spring|stretch"]), ("pointer moves along a scale", ["pointer|scale|read"])],
       "When a force is applied, the spring inside stretches and moves a pointer along a scale, giving the force in newtons.", need=2),
    mc("u10s1r8", "VH", "O1", "A rope is pulled with 50 N to the left and 50 N to the right. What happens?", ("Nothing moves – the forces are equal and opposite.", "Correct."), [("It moves left", "No."), ("It moves right", "No."), ("It disappears", "No.")], skill="Reasoning"),
]
S1_PRAC = [
    mc("u10s1p01", "M", "O1", "Friction acts…", "against the motion", [("in the direction of motion", "No."), ("upwards always", "No."), ("only in space", "No.")]),
    mc("u10s1p02", "M", "O1", "The floor pushes up on a box with a…", "normal force", [("tension force", "No."), ("magnetic force", "No."), ("gravitational force", "Down.")]),
    mc("u10s1p03", "M", "O1", "A rope pulled tight has a…", "tension force", [("normal force", "No."), ("friction force", "No."), ("magnetic force", "No.")]),
    mc("u10s1p04", "M", "O1", "Which acts at a distance?", "Electrical force", [("Friction", "Contact."), ("Tension", "Contact."), ("Applied force", "Contact.")]),
    mc("u10s1p05", "M", "O1", "Like charges…", "repel", [("attract", "Opposites attract."), ("do nothing", "No."), ("melt", "No.")]),
    mc("u10s1p06", "M", "O1", "Forces always act in…", "pairs", [("threes", "No."), ("one direction only", "No."), ("a vacuum only", "No.")]),
    mc("u10s1p07", "H", "O1", "On a windsurfer, the wind in the sail gives…", "forward thrust", [("drag", "Backwards."), ("gravity", "Down."), ("lift", "Up.")]),
    mc("u10s1p08", "H", "O1", "Drag on a windsurfer acts…", "backwards", [("forwards", "Thrust."), ("up", "Lift."), ("down", "Gravity.")]),
    mc("u10s1p09", "M", "O1", "The unit 'newton' is named after…", "Sir Isaac Newton", [("Galileo", "No."), ("Einstein", "No."), ("Brahmagupta", "No.")]),
    mc("u10s1p10", "M", "O1", "A squashed spring exerts a…", "spring force", [("magnetic force", "No."), ("gravitational force", "No."), ("electrical force", "No.")]),
    gd("u10s1p11", "M", "O1", "Push or pull?", ["Type"], [("Opening a drawer", ["Pull"]), ("Kicking a ball", ["Push"]), ("Lifting a bag up by its handle", ["Pull"]), ("Pressing a button", ["Push"])], skill="Data"),
    mc("u10s1p12", "H", "O1", "A sliding box slows down because of…", "friction", [("tension", "No."), ("magnetism", "No."), ("lift", "No.")]),
    mc("u10s1p13", "H", "O1", "Magnetic force attracts…", "some metals", [("all materials", "No."), ("wood", "No."), ("plastic", "No.")]),
    nm("u10s1p14", "H", "O1", "About what force does gravity exert on a 2 kg bag on Earth (1 N per 100 g)?", 20, "N"),
    mc("u10s1p15", "H", "O1", "A force can start a still object moving or…", "stop a moving object", [("change its mass", "No."), ("create energy", "No."), ("change its colour", "No.")]),
    mc("u10s1p16", "M", "O1", "Gravity gives objects their…", "weight", [("mass", "No."), ("shape", "No."), ("colour", "No.")]),
    mc("u10s1p17", "H", "O1", "Why do cyclists pedal harder into the wind?", "Air pushes against them, increasing drag", [("Gravity is stronger", "No."), ("Bikes are heavier", "No."), ("Friction disappears", "No.")], skill="Reasoning"),
    od("u10s1p18", "M", "O1", "Order the forces from smallest to largest.", ["0.5 N", "1 N", "20 N", "700 N"]),
]
S1_ADV = [
    adv(ex("u10s1a1", "VH", "O1", "Describe the forces on a book resting on a table and explain why it doesn't move.",
           [("gravity / weight down", ["gravity|weight|down"]), ("normal force / table pushes up", ["normal|push.*up|up"]), ("forces equal and opposite / balanced", ["equal|balanc|opposite"])],
           "Gravity pulls the book down (its weight) and the table pushes up with a normal force. The two forces are equal and opposite (balanced), so the book stays still.", need=2)),
    adv(mc("u10s1a2", "VH", "O1", "A force meter reads 4.5 N when an apple hangs from it. About what is the apple's mass?", ("450 g", "Correct – 1 N per 100 g."), [("45 g", "No."), ("4.5 kg", "No."), ("4.5 g", "No.")], skill="Data")),
    adv(mc("u10s1a3", "VH", "O1", "Why are force arrows drawn starting from the object?", ("To show which object the force acts on and in what direction.", "Correct."), [("To look nice", "No."), ("Arrows show speed", "No."), ("To show mass", "No.")], skill="Reasoning")),
    adv(nm("u10s1a4", "VH", "O1", "A box is pushed with 30 N and friction is 12 N. What is the overall (resultant) force forwards?", 18, "N")),
]

S2_REQ = [
    mc("u10s2r1", "M", "O2", "Gravity is a force of…", ("attraction between objects", "Correct."), [("repulsion", "No."), ("friction", "No."), ("tension", "No.")]),
    mc("u10s2r2", "M", "O2", "Gravity keeps the planets in orbit around…", ("the Sun", "Correct."), [("the Moon", "No."), ("Earth", "No."), ("Mars", "No.")]),
    gd("u10s2r3", "H", "O2", "Does the gravitational force get stronger or weaker?", ["Change"],
       [("Masses get larger", ["Stronger"]), ("Objects move further apart", ["Weaker"]), ("Objects move closer", ["Stronger"]), ("Masses get smaller", ["Weaker"])], skill="Data"),
    ex("u10s2r4", "H", "O2", "Explain why the Moon doesn't fall onto Earth.",
       [("Moon moves sideways", ["sideways|moving|speed"]), ("keeps falling around / Earth curves away / orbit", ["around|curve|orbit"])],
       "The Moon is moving sideways. As Earth's gravity pulls it in, Earth's surface curves away, so the Moon keeps falling around Earth in an orbit.", need=2),
    mc("u10s2r5", "H", "O2", "Astronauts far out in space feel almost weightless because…", ("they are far from Earth, so gravity is weak", "Correct."), [("they have no mass", "No."), ("space has air", "No."), ("gravity is stronger in space", "No.")]),
    tb("u10s2r6", "H", "O2", "Data: weight of a 1 kg mass at different places (N). Complete the difference from Earth.", ["Place", "Weight (N)", "Less than Earth by (N)"],
       [["Earth", "9.8", "0"], ["Mars", "3.7", B(6.1)], ["Moon", "1.6", B(8.2)]], skill="Data"),
    mc("u10s2r7", "M", "O2", "We notice Earth's gravity easily because Earth…", ("has a very large mass", "Correct."), [("is very hot", "No."), ("spins", "No."), ("has air", "No.")]),
    mc("u10s2r8", "VH", "O2", "Why don't you feel pulled towards a friend standing next to you?", ("Your masses are tiny, so the gravitational force is far too small to notice.", "Correct."), [("Gravity only works on planets", "No – all masses."), ("People repel", "No."), ("Air blocks gravity", "No.")], skill="Reasoning"),
]
S2_PRAC = [
    mc("u10s2p01", "M", "O2", "Gravity keeps the Moon in orbit around…", "Earth", [("the Sun only", "No."), ("Mars", "No."), ("Jupiter", "No.")]),
    mc("u10s2p02", "M", "O2", "The bigger the masses, the…", "stronger the gravitational force", [("weaker the force", "No."), ("same the force", "No."), ("no force", "No.")]),
    mc("u10s2p03", "M", "O2", "The further apart two objects, the…", "weaker the gravitational force", [("stronger the force", "No."), ("same force", "No."), ("faster they fall", "No.")]),
    mc("u10s2p04", "M", "O2", "Gravity is a…", "non-contact force", [("contact force", "No."), ("friction force", "No."), ("tension force", "No.")]),
    mc("u10s2p05", "H", "O2", "Which has the strongest gravity at its surface?", "Jupiter", [("The Moon", "No."), ("Mars", "No."), ("A football", "No.")], skill="Reasoning"),
    mc("u10s2p06", "M", "O2", "Gravity keeps us…", "on the ground", [("floating", "No."), ("warm", "No."), ("awake", "No.")]),
    mc("u10s2p07", "H", "O2", "An orbit is…", "a curved path around another object", [("a straight line", "No."), ("a type of force", "No."), ("a star", "No.")]),
    mc("u10s2p08", "H", "O2", "If Earth's mass were bigger, your weight would be…", "bigger", [("smaller", "No."), ("the same", "No."), ("zero", "No.")], skill="Reasoning"),
    mc("u10s2p09", "M", "O2", "Gravity acts between…", "any two objects with mass", [("only planets", "No."), ("only magnets", "No."), ("only charged objects", "No.")]),
    gd("u10s2p10", "M", "O2", "What does gravity keep in orbit?", ["Orbits"], [("Earth", ["The Sun"]), ("The Moon", ["Earth"]), ("Mars", ["The Sun"])], skill="Data"),
    mc("u10s2p11", "H", "O2", "A satellite stays in orbit because…", "it moves sideways fast while gravity pulls it in", [("there is no gravity in space", "No."), ("it has an engine on all the time", "No."), ("it is very light", "No.")]),
    mc("u10s2p12", "H", "O2", "Why is gravity on the Moon weaker than on Earth?", "The Moon has a smaller mass", [("The Moon is further from the Sun", "No."), ("The Moon has no air", "Air isn't the reason."), ("The Moon is cold", "No.")]),
    nm("u10s2p13", "H", "O2", "Weight of 1 kg on Earth 9.8 N, on the Moon 1.6 N. About how many times weaker is the Moon's gravity? (1 d.p.)", 6.1, "times", tol=0.1),
    mc("u10s2p14", "M", "O2", "An apple falls from a tree because of…", "gravity", [("friction", "No."), ("tension", "No."), ("magnetism", "No.")]),
    mc("u10s2p15", "H", "O2", "Two spacecraft move further apart. The gravity between them…", "gets weaker", [("gets stronger", "No."), ("stays the same", "No."), ("becomes magnetic", "No.")]),
    mc("u10s2p16", "H", "O2", "Without gravity, the Moon would…", "move off in a straight line", [("stay still", "No."), ("fall onto Earth", "No."), ("orbit faster", "No.")], skill="Reasoning"),
    od("u10s2p17", "M", "O2", "Order by weight of 1 kg, smallest first.", ["Deep space (≈0 N)", "Moon (1.6 N)", "Mars (3.7 N)", "Earth (9.8 N)"], skill="Data"),
    mc("u10s2p18", "M", "O2", "Gravity is the force that…", "pulls objects towards each other", [("pushes objects apart", "No."), ("stops motion", "Friction."), ("only acts on Earth", "No.")]),
]
S2_ADV = [
    adv(ex("u10s2a1", "VH", "O2", "Use mass and distance to explain why the Sun's gravity controls the planets' orbits, not the Moon's.",
           [("Sun has a huge mass", ["mass|huge|massive"]), ("Moon has small mass / is far from other planets", ["moon|small|far|distance"])],
           "The Sun has a huge mass, so its gravitational pull on the planets is very strong. The Moon's mass is small and it is far from other planets, so its pull on them is tiny.", need=2)),
    adv(mc("u10s2a2", "VH", "O2", "A rocket travels from Earth to the Moon. How does Earth's pull on it change?", ("It gets weaker as distance increases.", "Correct."), [("It gets stronger", "No."), ("Stays the same", "No."), ("Turns into a push", "No.")], skill="Reasoning")),
    adv(nm("u10s2a3", "VH", "O2", "A 60 kg person weighs 588 N on Earth. What is her weight on Mars, where 1 kg weighs 3.7 N?", 222, "N")),
    adv(mc("u10s2a4", "VH", "O2", "Why do tides happen?", ("The Moon's gravity pulls on Earth's oceans.", "Correct."), [("Wind only", "No."), ("Earth's heat", "No."), ("Magnetism", "No.")], skill="Reasoning")),
]

S3_REQ = [
    mc("u10s3r1", "M", "O3", "Mass is…", ("the amount of matter in an object", "Correct."), [("the pull of gravity", "Weight."), ("a force", "No."), ("measured in newtons", "No.")]),
    mc("u10s3r2", "M", "O3", "Weight is measured in…", ("newtons", "Correct."), [("kilograms", "Mass."), ("grams", "Mass."), ("metres", "No.")]),
    tb("u10s3r3", "H", "O3", "A 10 kg object. Complete the table.", ["Place", "Mass (kg)", "Weight (N)"],
       [["Earth", B(10), "98"], ["Moon", B(10), "16"], ["Outer space", B(10), "0"]], skill="Data"),
    gd("u10s3r4", "H", "O3", "Mass or weight?", ["Quantity"],
       [("Measured in kg", ["Mass"]), ("Changes on the Moon", ["Weight"]), ("A force", ["Weight"]), ("Same everywhere", ["Mass"]), ("Measured in N", ["Weight"])], skill="Data"),
    ex("u10s3r5", "H", "O3", "An astronaut has a mass of 70 kg on Earth. Explain what happens to her mass and weight on the Moon.",
       [("mass stays 70 kg", ["70|same|doesn't change|does not change"]), ("weight smaller because Moon's gravity weaker", ["weight.*(less|small|lower)|weaker"])],
       "Her mass stays 70 kg, because she has the same amount of matter. Her weight is less, because the Moon's gravity is weaker.", need=2),
    nm("u10s3r6", "H", "O3", "On Earth, 1 kg weighs about 9.8 N. Weight of a 5 kg bag?", 49, "N", skill="Data"),
    mc("u10s3r7", "M", "O3", "Which instrument measures weight?", ("A force meter", "Correct."), [("A ruler", "No."), ("A thermometer", "No."), ("A measuring cylinder", "No.")]),
    mc("u10s3r8", "VH", "O3", "A shop sign says 'Weight: 2 kg'. What would a scientist say?", ("That is mass; weight is in newtons (about 20 N).", "Correct."), [("Correct as written", "No."), ("Weight is in metres", "No."), ("Mass is in newtons", "No.")], skill="Reasoning"),
]
S3_PRAC = [
    mc("u10s3p01", "M", "O3", "Mass is measured in…", "kilograms or grams", [("newtons", "Weight."), ("metres", "No."), ("seconds", "No.")]),
    mc("u10s3p02", "M", "O3", "Weight is…", "the pull of gravity on an object", [("the amount of matter", "Mass."), ("its size", "No."), ("its colour", "No.")]),
    mc("u10s3p03", "M", "O3", "On the Moon, your mass is…", "the same as on Earth", [("smaller", "Weight is."), ("bigger", "No."), ("zero", "No.")]),
    mc("u10s3p04", "M", "O3", "On the Moon, your weight is…", "smaller than on Earth", [("the same", "No."), ("bigger", "No."), ("in kilograms", "No.")]),
    mc("u10s3p05", "H", "O3", "In deep space, a 10 kg object weighs about…", "0 N", [("98 N", "Earth."), ("16 N", "Moon."), ("10 N", "No.")]),
    nm("u10s3p06", "H", "O3", "A 10 kg object weighs 98 N on Earth. Weight of a 20 kg object?", 196, "N"),
    mc("u10s3p07", "H", "O3", "Which changes if you move from Earth to Mars?", "Weight", [("Mass", "No."), ("Both", "No."), ("Neither", "No.")]),
    mc("u10s3p08", "M", "O3", "A balance measures…", "mass", [("weight in newtons", "Force meter."), ("length", "No."), ("time", "No.")]),
    gd("u10s3p09", "M", "O3", "Correct unit?", ["Unit"], [("Mass", ["kg"]), ("Weight", ["N"]), ("Force", ["N"])], skill="Data"),
    mc("u10s3p10", "H", "O3", "Why does weight change from place to place?", "Gravity is different in different places", [("Matter changes", "No."), ("Mass changes", "No."), ("Air changes your atoms", "No.")]),
    mc("u10s3p11", "H", "O3", "A 70 kg astronaut floats in space. Her mass is…", "70 kg", [("0 kg", "No."), ("7 kg", "No."), ("686 kg", "No.")]),
    nm("u10s3p12", "H", "O3", "On the Moon, 1 kg weighs 1.6 N. Weight of a 50 kg rover?", 80, "N"),
    mc("u10s3p13", "M", "O3", "Which statement is correct?", "Mass stays the same everywhere", [("Weight stays the same everywhere", "No."), ("Mass is a force", "No."), ("Weight is in kg", "No.")]),
    mc("u10s3p14", "H", "O3", "Why is it easier to lift a rock on the Moon?", "Its weight is less", [("Its mass is less", "No."), ("It's smaller", "No."), ("The Moon is warmer", "No.")], skill="Reasoning"),
    mc("u10s3p15", "H", "O3", "Is it still hard to push a heavy cart sideways on the Moon?", "Yes – its mass (amount of matter) is unchanged", [("No – it weighs less", "Mass resists pushes."), ("No – there's no gravity", "There is."), ("Yes – gravity is stronger", "No.")], skill="Reasoning"),
    od("u10s3p16", "M", "O3", "Order the weight of a 10 kg mass, largest first.", ["Earth (98 N)", "Mars (37 N)", "Moon (16 N)", "Deep space (0 N)"]),
    mc("u10s3p17", "M", "O3", "People often mix up mass and…", "weight", [("volume", "No."), ("length", "No."), ("time", "No.")]),
    mc("u10s3p18", "H", "O3", "A force meter reads 49 N for a bag on Earth. Its mass is about…", "5 kg", [("49 kg", "No."), ("0.5 kg", "No."), ("490 kg", "No.")], skill="Data"),
]
S3_ADV = [
    adv(ex("u10s3a1", "VH", "O3", "A student says 'astronauts lose weight in space, so they lose mass too'. Explain the mistake.",
           [("mass is amount of matter / unchanged", ["matter|unchanged|same|doesn't change"]), ("weight depends on gravity", ["gravity"])],
           "Mass is the amount of matter, which does not change. Weight is the pull of gravity, which is tiny in deep space. So weight falls, but mass stays the same.", need=2)),
    adv(nm("u10s3a2", "VH", "O3", "A probe weighs 2450 N on Earth (9.8 N/kg). What is its mass?", 250, "kg")),
    adv(mc("u10s3a3", "VH", "O3", "Why can bathroom scales marked in kg be misleading on the Moon?", ("They measure the force (weight) and convert it using Earth's gravity.", "Correct."), [("They measure mass directly", "No."), ("Scales don't work there", "They do."), ("kg are different on the Moon", "No.")], skill="Reasoning")),
    adv(nm("u10s3a4", "VH", "O3", "A 60 kg person: weight on Earth (9.8 N/kg) minus weight on the Moon (1.6 N/kg)?", 492, "N")),
]

S4_REQ = [
    mc("u10s4r1", "M", "O4", "Air resistance is also called…", ("drag", "Correct."), [("thrust", "No."), ("lift", "No."), ("tension", "No.")]),
    ex("u10s4r2", "H", "O4", "Explain how a parachute slows a skydiver.",
       [("large surface area", ["surface area|large|big"]), ("increases air resistance / drag", ["air resistance|drag"])],
       "The open parachute has a large surface area, which greatly increases air resistance (drag) acting upwards, so the skydiver slows down.", need=2),
    gd("u10s4r3", "M", "O4", "Which lands first?", ["Result"], [("Ball and feather dropped in air", ["Ball first"]), ("Ball and feather dropped in a vacuum", ["Together"]), ("Crumpled and flat paper in air", ["Crumpled first"])], skill="Data"),
    mc("u10s4r4", "H", "O4", "In a vacuum, a feather and a bowling ball fall…", ("at the same rate", "Correct – no air resistance."), [("the ball faster", "No."), ("the feather faster", "No."), ("not at all", "No.")]),
    mt("u10s4r5", "M", "O4", "Match the scientist to the idea.", [("Brahmagupta", "objects fall because of Earth's attraction"), ("Galileo", "same shape and size fall at the same rate"), ("Newton", "Law of Universal Gravitation, 1687")]),
    tb("u10s4r6", "H", "O4", "Data: time to fall 2 m (s). Complete the difference.", ["Object", "Time (s)", "Slower than ball by (s)"],
       [["Ball", "0.6", "0"], ["Paper sheet", "1.8", B(1.2)], ["Feather", "3.0", B(2.4)]], skill="Data"),
    mc("u10s4r7", "H", "O4", "A spacecraft switches off its engine in outer space. It…", ("keeps moving at the same speed", "Correct – no air resistance."), [("stops at once", "No."), ("slows down", "No drag."), ("falls back to Earth", "No.")]),
    mc("u10s4r8", "VH", "O4", "Why do vehicle designers test in wind tunnels?", ("Less drag means less fuel is needed.", "Correct."), [("To make cars heavier", "No."), ("To add drag", "No."), ("For colour", "No.")], skill="Reasoning"),
]
S4_PRAC = [
    mc("u10s4p01", "M", "O4", "Air resistance acts…", "against the motion", [("with the motion", "No."), ("only upwards", "No."), ("only in space", "No.")]),
    mc("u10s4p02", "M", "O4", "A vacuum is…", "a space with no matter, not even air", [("full of air", "No."), ("very cold air", "No."), ("water", "No.")]),
    mc("u10s4p03", "M", "O4", "Racing cyclists crouch low to…", "reduce drag", [("increase drag", "No."), ("increase gravity", "No."), ("rest", "No.")]),
    mc("u10s4p04", "M", "O4", "Outer space is almost…", "a vacuum", [("full of air", "No."), ("water", "No."), ("solid", "No.")]),
    mc("u10s4p05", "H", "O4", "Before the parachute opens, a skydiver falls fast because…", "small surface area gives small drag", [("gravity is smaller", "No."), ("there's no air", "No."), ("mass increases", "No.")]),
    mc("u10s4p06", "M", "O4", "Newton published the Law of Universal Gravitation in…", "1687", [("1066", "No."), ("1969", "No."), ("2013", "No.")]),
    mc("u10s4p07", "H", "O4", "Brahmagupta lived about how long before Newton?", "About a thousand years", [("About 10 years", "No."), ("About 100 years", "No."), ("After Newton", "No.")]),
    mc("u10s4p08", "H", "O4", "Newton said he could see further by 'standing on the shoulders of giants'. He meant…", "he built on earlier scientists' work", [("he was tall", "No."), ("he used ladders", "No."), ("he worked alone", "No.")]),
    gd("u10s4p09", "M", "O4", "More or less air resistance?", ["Drag"], [("Opening a parachute", ["More"]), ("Crouching on a bike", ["Less"]), ("Streamlined car shape", ["Less"]), ("Holding a sheet of card flat", ["More"])], skill="Data"),
    mc("u10s4p10", "H", "O4", "A feather falls slowly in air because of its…", "shape and large surface area", [("large mass", "No."), ("colour", "No."), ("magnetism", "No.")]),
    mc("u10s4p11", "H", "O4", "Galileo showed objects of the same shape and size…", "fall at the same rate whatever their weight", [("fall faster if heavier", "No."), ("float", "No."), ("fall slower if heavier", "No.")]),
    mc("u10s4p12", "M", "O4", "Less drag on a vehicle means…", "less fuel is needed", [("more fuel", "No."), ("more noise", "No."), ("more friction", "No.")]),
    mc("u10s4p13", "H", "O4", "Which falls fastest in air?", "A crumpled paper ball", [("A flat sheet of the same paper", "More drag."), ("An open parachute", "Lots of drag."), ("A feather", "Lots of drag.")], skill="Reasoning"),
    mc("u10s4p14", "H", "O4", "Why can't a parachute work on the Moon?", "There is no air, so no air resistance", [("Gravity is too strong", "No."), ("It's too cold", "No."), ("Parachutes need water", "No.")], skill="Reasoning"),
    nm("u10s4p15", "H", "O4", "A skydiver falls at 55 m/s and the parachute slows him to 5 m/s. By how much did the speed drop?", 50, "m/s"),
    mc("u10s4p16", "M", "O4", "Drag and gravity on a falling skydiver act in…", "opposite directions", [("the same direction", "No."), ("sideways", "No."), ("no direction", "No.")]),
    od("u10s4p17", "M", "O4", "Order by date.", ["Brahmagupta", "Galileo", "Newton (1687)"]),
    mc("u10s4p18", "H", "O4", "Fish and fast cars have similar streamlined shapes because…", "it reduces resistance as they move", [("it looks nice", "No."), ("it adds weight", "No."), ("it increases drag", "No.")], skill="Reasoning"),
]
S4_ADV = [
    adv(ex("u10s4a1", "VH", "O4", "Plan a fair test to see how the size of a paper parachute affects its fall time.",
           [("change only canopy area/size", ["size|area"]), ("same mass/height/string", ["same|height|mass"]), ("measure fall time / repeat", ["time|repeat|stopwatch"])],
           "Change only the canopy area. Keep the mass, string length and drop height the same. Time each fall with a stopwatch and repeat three times to take an average.", need=2)),
    adv(gr("u10s4a2", "VH", "O4", "* Advanced. Data: parachute area and fall time. Plot the points.", {"label": "Area (cm²)", "min": 0, "max": 500, "step": 100}, {"label": "Fall time (s)", "min": 0, "max": 5, "step": 1},
           [[100, 1.5], [200, 2.2], [300, 2.9], [400, 3.5]], skill="Data")),
    adv(mc("u10s4a3", "VH", "O4", "An astronaut on the Moon dropped a hammer and a feather together. What happened, and why?", ("They landed together – there is no air on the Moon.", "Correct."), [("The hammer landed first", "No air resistance there."), ("The feather floated away", "No."), ("Neither fell", "No.")], skill="Reasoning")),
    adv(nm("u10s4a4", "VH", "O4", "How many years passed between Newton's 1687 law and the year 2026?", 339, "years")),
]

POOLS = {"10.1": (S1_REQ, S1_PRAC, S1_ADV), "10.2": (S2_REQ, S2_PRAC, S2_ADV), "10.3": (S3_REQ, S3_PRAC, S3_ADV), "10.4": (S4_REQ, S4_PRAC, S4_ADV)}

STOPS = {
    "10.1": [stop("u10v1a", "and slows things down", mc("u10v1a_q", "M", "O1", "Friction acts…", "against the motion", [("with the motion", "No."), ("only upwards", "No."), ("at a distance", "Contact.")])),
             stop("u10v1b", "Magnetic force attracts some metals", mc("u10v1b_q", "M", "O1", "Which force acts at a distance?", "Gravity", [("Friction", "Contact."), ("Tension", "Contact."), ("Normal force", "Contact.")])),
             stop("u10v1c", "named after the scientist Sir Isaac Newton", mc("u10v1c_q", "H", "O1", "In a force diagram, a longer arrow means…", "a bigger force", [("a heavier object", "No."), ("a slower object", "No."), ("a smaller force", "No.")]))],
    "10.2": [stop("u10v2a", "feel almost weightless", mc("u10v2a_q", "M", "O2", "Gravitational force gets weaker when objects…", "move further apart", [("get bigger", "Stronger."), ("move closer", "Stronger."), ("touch", "No.")]))],
    "10.3": [stop("u10v3a", "it changes depending on where you are", mc("u10v3a_q", "M", "O3", "A 10 kg object on the Moon has a mass of…", "10 kg", [("16 kg", "No."), ("0 kg", "No."), ("98 kg", "No.")]))],
    "10.4": [stop("u10v4a", "which is better for the environment", mc("u10v4a_q", "M", "O4", "A parachute increases air resistance because of its…", "large surface area", [("large mass", "No."), ("colour", "No."), ("strings", "No.")])),
             stop("u10v4b", "it just keeps moving forward at the same speed", mc("u10v4b_q", "H", "O4", "In a vacuum, a feather and a ball…", "fall at the same rate", [("ball falls faster", "No."), ("feather falls faster", "No."), ("float", "No.")])),
             stop("u10v4c", "he built on the work of scientists before him", mc("u10v4c_q", "H", "O4", "Who first described objects falling because of Earth's attraction?", "Brahmagupta", [("Newton", "Later."), ("Galileo", "Later."), ("Einstein", "No.")]))],
}

MINDMAP = {"id": "root", "t": "Forces", "sec": None, "kids": [
    {"id": "f", "t": "Forces around us", "d": "Push or pull • contact: normal, applied, friction, spring, tension • non-contact: gravity, electrical, magnetic • force diagrams • newtons, force meter.", "obj": "O1", "sec": "10.1"},
    {"id": "g", "t": "Gravity", "d": "Attraction between masses • bigger mass → stronger • further apart → weaker • orbits.", "obj": "O2", "sec": "10.2"},
    {"id": "mw", "t": "Mass and weight", "d": "Mass: matter, kg, same everywhere • Weight: pull of gravity, N, changes (Earth 98 N, Moon 16 N for 10 kg).", "obj": "O3", "sec": "10.3"},
    {"id": "ar", "t": "Air resistance", "d": "Drag opposes motion • parachutes, crouching cyclists, wind tunnels • none in a vacuum • Brahmagupta, Galileo, Newton.", "obj": "O4", "sec": "10.4"},
]}
