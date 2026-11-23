# -*- coding: utf-8 -*-
"""Stage 7 Unit 14 – Earth in Space. Written by the Atomic teaching team."""
from c_kit import *

STRAND = "Earth and Space"
BLURB = "The Solar System and how it formed, gravity and orbits, tides, eclipses, and how our models of space developed."

OBJECTIVES = {
    "O1": {"sec": "14.1", "code": "7ESs.01, 7ESs.02", "codeNote": "", "t": "Describe the Solar System, how planets stay in orbit, days, years and seasons, and how stars and planets form from dust and gas."},
    "O2": {"sec": "14.2", "code": "7ESs.03", "codeNote": "", "t": "Explain tides, including spring and neap tides, using the gravity of the Moon and Sun."},
    "O3": {"sec": "14.3", "code": "7ESs.04", "codeNote": "", "t": "Explain solar and lunar eclipses, including umbra and penumbra."},
    "O4": {"sec": "14.4", "code": "7SIC.01, 7TWSm.01", "codeNote": "", "t": "Describe how models of the Solar System and Universe developed as new evidence appeared."},
}

SECTIONS = [
    {"id": "14.1", "title": "The Solar System", "objs": ["O1"]},
    {"id": "14.2", "title": "Gravity and tides", "objs": ["O2"]},
    {"id": "14.3", "title": "Eclipses", "objs": ["O3"]},
    {"id": "14.4", "title": "Developing models of space", "objs": ["O4"]},
]

S1_REQ = [
    od("u14s1r1", "M", "O1", "Order the planets from the Sun outwards.", ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]),
    gd("u14s1r2", "M", "O1", "Rocky planet or gas giant?", ["Type"], [("Mars", ["Rocky"]), ("Jupiter", ["Gas giant"]), ("Venus", ["Rocky"]), ("Neptune", ["Gas giant"]), ("Earth", ["Rocky"])], skill="Data"),
    ex("u14s1r3", "H", "O1", "Explain why a planet stays in orbit around the Sun.",
       [("Sun's gravity pulls it", ["gravity|pull"]), ("balance with its speed / moving sideways", ["speed|balance|fast|sideways"])],
       "The Sun's gravity pulls the planet towards it, and the planet's speed carries it sideways. The balance keeps it in orbit: too slow and it falls in, too fast and it escapes.", need=2),
    mc("u14s1r4", "M", "O1", "One rotation of a planet on its axis is one…", ("day", "Correct."), [("year", "Revolution."), ("month", "No."), ("season", "No.")]),
    mc("u14s1r5", "H", "O1", "Earth has seasons because…", ("its axis is tilted", "Correct."), [("its distance from the Sun changes a lot", "Not the main reason."), ("the Sun switches off", "No."), ("the Moon blocks it", "No.")]),
    od("u14s1r6", "H", "O1", "Order how a star and planets form.", ["A nebula of gas and dust", "Gravity pulls it in and it spins into a disk", "A hot protostar forms at the centre", "Nuclear fusion starts – a star is born", "Leftover dust clumps into planets"]),
    tb("u14s1r7", "H", "O1", "Complete for Earth.", ["Motion", "Time"], [["Rotation (hours)", B(24)], ["Revolution (days)", B(365.25)]], skill="Data"),
    mc("u14s1r8", "VH", "O1", "Why did rocky planets form close to the Sun and gas giants further away?", ("Near the Sun it was too hot for gases to collect; further away it was colder.", "Correct."), [("Gas is heavier", "No."), ("Rock floats outwards", "No."), ("Random chance", "No.")], skill="Reasoning"),
]
S1_PRAC = [
    mc("u14s1p01", "M", "O1", "The Sun is…", "a star", [("a planet", "No."), ("a moon", "No."), ("a comet", "No.")]),
    mc("u14s1p02", "M", "O1", "Stars are shaped like…", "balls (spheres)", [("five-pointed stars", "No."), ("cubes", "No."), ("disks", "No.")]),
    mc("u14s1p03", "M", "O1", "The asteroid belt lies between…", "the inner and outer planets", [("Earth and the Moon", "No."), ("the Sun and Mercury", "No."), ("Neptune and Pluto", "No.")]),
    mc("u14s1p04", "M", "O1", "Planets shine because they…", "reflect sunlight", [("make their own light", "No."), ("burn", "No."), ("are stars", "No.")]),
    mc("u14s1p05", "M", "O1", "Planets orbit the Sun in…", "elliptical orbits", [("perfect squares", "No."), ("straight lines", "No."), ("zigzags", "No.")]),
    mc("u14s1p06", "M", "O1", "'Sol' is the Latin word for…", "Sun", [("star", "No."), ("planet", "No."), ("Moon", "No.")]),
    mc("u14s1p07", "H", "O1", "The Sun has more than ___ of the Solar System's mass.", "99%", [("50%", "No."), ("10%", "No."), ("1%", "No.")]),
    mc("u14s1p08", "M", "O1", "A moon is…", "a natural satellite", [("an artificial satellite", "Spacecraft."), ("a star", "No."), ("a planet", "No.")]),
    mc("u14s1p09", "H", "O1", "Which planets have no moons?", "Mercury and Venus", [("Earth and Mars", "No."), ("Jupiter and Saturn", "No."), ("Uranus and Neptune", "No.")]),
    mc("u14s1p10", "H", "O1", "Saturn's largest moon, Titan, is bigger than…", "the planet Mercury", [("Earth", "No."), ("Jupiter", "No."), ("the Sun", "No.")]),
    mc("u14s1p11", "M", "O1", "Gas giants are made of substances like…", "hydrogen, helium and methane", [("iron and nickel", "No."), ("rock and sand", "No."), ("water only", "No.")]),
    mc("u14s1p12", "H", "O1", "A planet moving too slowly would…", "fall into the Sun", [("escape into space", "Too fast."), ("stop", "No."), ("become a star", "No.")], skill="Reasoning"),
    mc("u14s1p13", "H", "O1", "Nuclear fusion is when…", "atoms fuse into larger atoms, releasing energy", [("atoms split into smaller ones only", "No."), ("gas cools", "No."), ("planets collide", "No.")]),
    mc("u14s1p14", "M", "O1", "The Solar System formed about…", "4.6 billion years ago", [("4600 years ago", "No."), ("46 million years ago", "No."), ("46 billion years ago", "No.")]),
    gd("u14s1p15", "M", "O1", "Day or year?", ["Time"], [("One rotation", ["Day"]), ("One revolution", ["Year"]), ("Earth: 365¼ days", ["Year"])], skill="Data"),
    mc("u14s1p16", "M", "O1", "Which planets can be seen without a telescope?", "Venus, Mars and Jupiter", [("Uranus and Neptune", "No."), ("Only Earth", "No."), ("None", "No.")]),
    mc("u14s1p17", "H", "O1", "In the hoop-and-cloth model, the heavy ball in the middle represents…", "the Sun", [("a planet", "Marbles."), ("the Moon", "No."), ("a comet", "No.")]),
    nm("u14s1p18", "H", "O1", "How many hours in 3 Earth days?", 72, "hours"),
]
S1_ADV = [
    adv(ex("u14s1a1", "VH", "O1", "Explain why it is summer in the UK when the northern half of Earth points towards the Sun.",
           [("tilted axis", ["tilt|axis"]), ("more direct sunlight / longer days", ["direct|longer|more sunlight|concentrated|higher"])],
           "Earth's axis is tilted. When the northern half points towards the Sun, sunlight hits it more directly and days are longer, so it is warmer – summer.", need=2)),
    adv(mc("u14s1a2", "VH", "O1", "If the Sun's mass suddenly doubled (same distance), Earth would…", ("be pulled more strongly and need to move faster to stay in orbit", "Correct."), [("drift away", "No."), ("feel no change", "No."), ("become a star", "No.")], skill="Reasoning")),
    adv(nm("u14s1a3", "VH", "O1", "Why do we add a leap day? Earth takes 365.25 days per orbit. After 4 years, how many extra days have built up?", 1, "day")),
    adv(mc("u14s1a4", "VH", "O1", "Why is the planet-forming model a 'model' and not an observation?", ("Nobody saw it happen; it is built from evidence such as disks around young stars.", "Correct."), [("It was filmed", "No."), ("It is a guess with no evidence", "No."), ("It is a law", "No.")], skill="Reasoning")),
]

S2_REQ = [
    mc("u14s2r1", "M", "O2", "Tides are mainly caused by…", ("the Moon's gravity pulling on the oceans", "Correct."), [("wind", "No."), ("Earth's core", "No."), ("rivers", "No.")]),
    mc("u14s2r2", "M", "O2", "How many high tides does a place usually get each day?", ("Two", "Correct."), [("One", "No."), ("Four", "No."), ("None", "No.")]),
    gd("u14s2r3", "H", "O2", "Spring or neap tide?", ["Tide"], [("Sun and Moon in line", ["Spring"]), ("Moon at right angles to Sun", ["Neap"]), ("Very high high tides", ["Spring"]), ("Smallest tidal range", ["Neap"])], skill="Figure"),
    ex("u14s2r4", "H", "O2", "Explain why there is a bulge of water on the side of Earth facing away from the Moon.",
       [("Earth's rotation", ["rotat|spin|turn"]), ("water flies outwards", ["outward|fly|swing|fling"])],
       "Earth's rotation makes the ocean on the far side fly outwards, like water swinging in a glass, forming a second bulge.", need=2),
    mc("u14s2r5", "H", "O2", "The Sun affects tides less than the Moon because…", ("the Sun is much further away", "Correct."), [("the Sun has less mass", "No – far more."), ("the Sun has no gravity", "No."), ("the Sun is hot", "No.")]),
    tb("u14s2r6", "H", "O2", "Tide table: heights (m). Complete the range.", ["Tide", "High (m)", "Low (m)", "Range (m)"],
       [["Spring", "5.8", "0.4", B(5.4)], ["Neap", "4.2", "1.8", B(2.4)]], skill="Data"),
    mc("u14s2r7", "M", "O2", "Spring tides happen…", ("twice every 28 days", "Correct."), [("only in spring", "No."), ("once a year", "No."), ("every day", "No.")]),
    mc("u14s2r8", "VH", "O2", "Why do ports publish tide tables?", ("Large ships can only enter some ports at high tide.", "Correct."), [("For swimming races only", "No."), ("To predict earthquakes", "No."), ("Tides are random", "No.")], skill="Reasoning"),
]
S2_PRAC = [
    mc("u14s2p01", "M", "O2", "Tides are the regular rise and fall of…", "sea level", [("air pressure", "No."), ("the Moon", "No."), ("rivers only", "No.")]),
    mc("u14s2p02", "M", "O2", "The ocean facing the Moon…", "bulges towards it", [("moves away", "No."), ("freezes", "No."), ("stays flat", "No.")]),
    mc("u14s2p03", "M", "O2", "Earth turns once every…", "24 hours", [("28 days", "Moon's orbit."), ("365 days", "Year."), ("12 hours", "No.")]),
    mc("u14s2p04", "M", "O2", "The Moon orbits Earth in about…", "28 days", [("24 hours", "No."), ("365 days", "No."), ("7 days", "No.")]),
    mc("u14s2p05", "H", "O2", "During neap tides, the Sun and Moon's pulls…", "partly cancel out", [("combine fully", "Spring."), ("disappear", "No."), ("reverse", "No.")]),
    mc("u14s2p06", "M", "O2", "Spring tides have…", "very high and very low tides", [("almost no change", "Neap."), ("no tides", "No."), ("only low tides", "No.")]),
    nm("u14s2p07", "H", "O2", "High tide 6.0 m, low tide 1.5 m. Tidal range?", 4.5, "m"),
    mc("u14s2p08", "H", "O2", "Why do coastal people need to know when very high tides are coming?", "To protect homes from flooding as sea levels rise", [("To go swimming", "No."), ("To plant crops", "No."), ("To see eclipses", "No.")]),
    gd("u14s2p09", "M", "O2", "Tide type", ["Tide"], [("Full Moon or new Moon (in line)", ["Spring"]), ("Half Moon (right angle)", ["Neap"])], skill="Figure"),
    mc("u14s2p10", "H", "O2", "The Moon orbits Earth because of…", "Earth's gravity", [("the Sun's light", "No."), ("tides", "No."), ("magnetism", "No.")]),
    mc("u14s2p11", "H", "O2", "Each place passes through two bulges a day because…", "Earth rotates once every 24 hours", [("the Moon orbits twice a day", "No."), ("the Sun moves", "No."), ("there are two Moons", "No.")]),
    mc("u14s2p12", "M", "O2", "The Moon's gravity pulls on…", "Earth, including its oceans", [("only rocks", "No."), ("only the Sun", "No."), ("nothing", "No.")]),
    nm("u14s2p13", "H", "O2", "High tides about every 12.4 h. If high tide is at 06:00, roughly when (hours after midnight) is the next? (1 d.p.)", 18.4, "hours", tol=0.1),
    mc("u14s2p14", "H", "O2", "How many spring tides happen in about 28 days?", "Two", [("One", "No."), ("Four", "No."), ("Twenty-eight", "No.")]),
    mc("u14s2p15", "H", "O2", "Which has more mass: the Sun or the Moon?", "The Sun", [("The Moon", "No."), ("Same", "No."), ("Can't tell", "No.")], skill="Reasoning"),
    od("u14s2p16", "M", "O2", "Order by tidal range, smallest first.", ["Neap tide", "Average tide", "Spring tide"]),
    mc("u14s2p17", "H", "O2", "Tidal power stations use…", "the movement of water as tides rise and fall", [("sunlight", "No."), ("wind only", "No."), ("magma", "No.")]),
    mc("u14s2p18", "M", "O2", "Which force causes tides?", "Gravity", [("Friction", "No."), ("Magnetism", "No."), ("Tension", "No.")]),
]
S2_ADV = [
    adv(ex("u14s2a1", "VH", "O2", "Explain why spring tides have a larger tidal range than neap tides.",
           [("spring: Sun and Moon in line, pulls combine", ["line|combine|together|add"]), ("neap: at right angles, partly cancel", ["right angle|cancel|90"])],
           "At spring tides the Sun and Moon are in line, so their pulls combine to give very high and very low tides. At neap tides they are at right angles and partly cancel, so the range is smaller.", need=2)),
    adv(mc("u14s2a2", "VH", "O2", "A ship needs 8 m of water. Low tide depth is 5 m; high tide 9 m. When can it enter?", ("Only around high tide", "Correct."), [("Only at low tide", "No."), ("Any time", "No."), ("Never", "No.")], skill="Data")),
    adv(nm("u14s2a3", "VH", "O2", "Sea level is rising 4 mm a year. How much higher in 25 years, in cm?", 10, "cm")),
    adv(mc("u14s2a4", "VH", "O2", "If Earth had no Moon, tides would…", ("be much smaller, caused only by the Sun", "Correct."), [("be bigger", "No."), ("stay the same", "No."), ("not change sea level at all ever", "Sun still causes small tides.")], skill="Reasoning")),
]

S3_REQ = [
    mc("u14s3r1", "M", "O3", "A solar eclipse happens when…", ("the Moon passes between the Sun and Earth", "Correct."), [("Earth passes between the Sun and Moon", "Lunar eclipse."), ("the Sun passes behind Earth", "No."), ("clouds cover the Sun", "No.")]),
    mc("u14s3r2", "M", "O3", "A lunar eclipse happens when…", ("the Moon passes through Earth's shadow", "Correct."), [("the Moon blocks the Sun", "Solar."), ("the Sun goes out", "No."), ("it is cloudy", "No.")]),
    gd("u14s3r3", "H", "O3", "Solar or lunar eclipse?", ["Eclipse"], [("Moon's shadow falls on Earth", ["Solar"]), ("Moon turns red", ["Lunar"]), ("Corona can be studied", ["Solar"]), ("Earth's shadow on the Moon", ["Lunar"])], skill="Figure"),
    mc("u14s3r4", "M", "O3", "In the umbra you see…", ("a total eclipse", "Correct."), [("a partial eclipse", "Penumbra."), ("nothing different", "No."), ("a rainbow", "No.")]),
    ex("u14s3r5", "H", "O3", "Explain why the Moon often looks red during a lunar eclipse.",
       [("Earth's atmosphere bends sunlight onto the Moon", ["atmosphere|bend"]), ("blue light removed, red left", ["blue|red"])],
       "Earth's atmosphere bends some sunlight onto the Moon and removes most of the blue light, so the light reaching the Moon is red.", need=2),
    mc("u14s3r6", "H", "O3", "Shadows form because…", ("light travels in straight lines", "Correct."), [("light bends round objects", "No."), ("light is a sound", "No."), ("shadows are made of gas", "No.")]),
    tb("u14s3r7", "H", "O3", "Count: in a list of 6 eclipses, 4 were lunar. Complete.", ["Eclipse", "Number"], [["Lunar", "4"], ["Solar", B(2)]], skill="Data"),
    mc("u14s3r8", "VH", "O3", "Why must you never look directly at the Sun, even during an eclipse?", ("It can permanently damage your eyes.", "Correct."), [("It is too dark", "No."), ("It is illegal", "No."), ("It causes tides", "No.")], skill="Reasoning"),
]
S3_PRAC = [
    mc("u14s3p01", "M", "O3", "The darkest part of a shadow is the…", "umbra", [("penumbra", "Lighter."), ("corona", "No."), ("axis", "No.")]),
    mc("u14s3p02", "M", "O3", "The lighter part of a shadow is the…", "penumbra", [("umbra", "Darker."), ("corona", "No."), ("orbit", "No.")]),
    mc("u14s3p03", "M", "O3", "In the penumbra you see…", "a partial eclipse", [("a total eclipse", "Umbra."), ("a lunar eclipse", "No."), ("nothing", "No.")]),
    mc("u14s3p04", "M", "O3", "The Sun's faint outer atmosphere is the…", "corona", [("umbra", "No."), ("core", "No."), ("crust", "No.")]),
    mc("u14s3p05", "H", "O3", "During a solar eclipse, the order is…", "Sun – Moon – Earth", [("Sun – Earth – Moon", "Lunar."), ("Moon – Sun – Earth", "No."), ("Earth – Sun – Moon", "No.")]),
    mc("u14s3p06", "H", "O3", "During a lunar eclipse, the order is…", "Sun – Earth – Moon", [("Sun – Moon – Earth", "Solar."), ("Moon – Sun – Earth", "No."), ("Earth – Moon – Sun", "No.")]),
    mc("u14s3p07", "M", "O3", "During a total solar eclipse, scientists can study…", "the corona", [("the Moon's core", "No."), ("Earth's core", "No."), ("tides", "No.")]),
    mc("u14s3p08", "H", "O3", "A lunar eclipse can only happen at…", "full Moon", [("new Moon", "Solar."), ("half Moon", "No."), ("any time", "No.")], skill="Reasoning"),
    mc("u14s3p09", "H", "O3", "A solar eclipse can only happen at…", "new Moon", [("full Moon", "Lunar."), ("half Moon", "No."), ("midnight", "No.")], skill="Reasoning"),
    gd("u14s3p10", "M", "O3", "What you see", ["View"], [("Standing in the umbra", ["Total eclipse"]), ("Standing in the penumbra", ["Partial eclipse"])], skill="Figure"),
    mc("u14s3p11", "M", "O3", "Which blocks light in a solar eclipse?", "The Moon", [("Earth", "No."), ("Clouds", "No."), ("The Sun", "No.")]),
    mc("u14s3p12", "M", "O3", "Which casts the shadow in a lunar eclipse?", "Earth", [("The Moon", "No."), ("The Sun", "No."), ("Mars", "No.")]),
    mc("u14s3p13", "H", "O3", "Why is a total solar eclipse seen only from a small area?", "The Moon's umbra on Earth is small", [("The Sun is small", "No."), ("Clouds", "No."), ("Only some people look", "No.")], skill="Reasoning"),
    mc("u14s3p14", "H", "O3", "Why can everyone on the night side of Earth see a lunar eclipse?", "The whole Moon is in Earth's shadow", [("The Moon is huge", "No."), ("It lasts years", "No."), ("Telescopes are needed", "No.")], skill="Reasoning"),
    od("u14s3p15", "M", "O3", "Order for a solar eclipse, from the light source.", ["Sun", "Moon", "Earth"]),
    mc("u14s3p16", "H", "O3", "Ancient Chinese astronomers could predict solar eclipses around…", "2300 BCE", [("2300 CE", "No."), ("1846", "No."), ("100 CE", "No.")]),
    nm("u14s3p17", "H", "O3", "A total eclipse lasts 4 min 30 s. How many seconds is that?", 270, "s"),
    mc("u14s3p18", "M", "O3", "Light travels in…", "straight lines", [("circles", "No."), ("zigzags", "No."), ("waves only around corners", "No.")]),
]
S3_ADV = [
    adv(ex("u14s3a1", "VH", "O3", "The Moon orbits Earth every 28 days, but we don't get eclipses every month. Suggest why.",
           [("Moon's orbit is tilted", ["tilt|angle|above|below"]), ("so Sun, Moon, Earth are rarely exactly in line", ["line|align"])],
           "The Moon's orbit is slightly tilted, so most months the Sun, Moon and Earth are not exactly in line and the shadow misses.", need=2)),
    adv(mc("u14s3a2", "VH", "O3", "How could you model a solar eclipse in class?", ("Torch (Sun), small ball (Moon), large ball (Earth) in a line", "Correct."), [("Use a mirror only", "No."), ("Use two torches", "No."), ("Use water", "No.")], skill="Reasoning")),
    adv(nm("u14s3a3", "VH", "O3", "The Sun is about 400 times wider than the Moon and about 400 times further away. What is 400 ÷ 400?", 1, "")),
    adv(mc("u14s3a4", "VH", "O3", "The answer above explains why…", ("the Moon can just cover the Sun in a total eclipse", "Correct."), [("the Moon is red", "No."), ("there are tides", "No."), ("planets orbit", "No.")], skill="Reasoning")),
]

S4_REQ = [
    mc("u14s4r1", "M", "O4", "A geocentric model has…", ("Earth at the centre", "Correct."), [("the Sun at the centre", "Heliocentric."), ("the Moon at the centre", "No."), ("no centre", "No.")]),
    mc("u14s4r2", "M", "O4", "Copernicus proposed a…", ("heliocentric model, with the Sun at the centre", "Correct."), [("geocentric model", "Ptolemy."), ("flat Earth", "No."), ("model of tides", "No.")]),
    mt("u14s4r3", "M", "O4", "Match the scientist to the discovery.", [("Ptolemy", "geocentric model; longitude and latitude"), ("Galileo", "moons of Jupiter, phases of Venus"), ("Hubble", "other galaxies; expanding Universe"), ("Jocelyn Bell Burnell", "pulsars"), ("Caroline Herschel", "comets and a catalogue")]),
    od("u14s4r4", "H", "O4", "Order these events by date.", ["Chinese astronomers predict eclipses (~2300 BCE)", "Ptolemy's geocentric model (~100 CE)", "Al-Tusi lists problems with Ptolemy (1261)", "Neptune discovered by prediction (1846)"], skill="Data"),
    ex("u14s4r5", "H", "O4", "Explain how Galileo's observations supported the heliocentric model.",
       [("moons orbiting Jupiter", ["jupiter|moons"]), ("not everything orbits Earth / phases of Venus", ["not everything|venus|phase"])],
       "Galileo saw moons orbiting Jupiter and the phases of Venus. This was evidence that not everything orbits Earth, supporting a Sun-centred model.", need=2),
    mc("u14s4r6", "H", "O4", "Choosing only evidence that suits your opinion is called…", ("bias", "Correct."), [("a hypothesis", "No."), ("a model", "No."), ("a fair test", "No.")]),
    tb("u14s4r7", "H", "O4", "Calculate the years between events.", ["Events", "Years between"],
       [["Al-Tusi (1261) → Neptune (1846)", B(585)], ["Newton's law (1687) → Neptune (1846)", B(159)]], skill="Data"),
    mc("u14s4r8", "VH", "O4", "Neptune was predicted with Newton's laws before it was seen. Why is this strong evidence for the laws?", ("A correct prediction of something new tests the theory.", "Correct."), [("It was a lucky guess", "No."), ("Newton saw it", "No."), ("It proves Ptolemy right", "No.")], skill="Reasoning"),
]
S4_PRAC = [
    mc("u14s4p01", "M", "O4", "Ptolemy built his model around…", "100 CE", [("1543", "No."), ("2300 BCE", "No."), ("1846", "No.")]),
    mc("u14s4p02", "M", "O4", "Ptolemy also gave us…", "longitude and latitude", [("the telescope", "No."), ("gravity laws", "No."), ("pulsars", "No.")]),
    mc("u14s4p03", "H", "O4", "In the 10th century, Al-Sijzi suggested…", "the Earth rotates", [("the Earth is flat", "No."), ("Neptune exists", "No."), ("the Universe expands", "No.")]),
    mc("u14s4p04", "H", "O4", "In 1261, al-Tusi…", "listed 16 problems with Ptolemy's model", [("discovered Uranus", "No."), ("built a telescope", "No."), ("found pulsars", "No.")]),
    mc("u14s4p05", "M", "O4", "Earth's spin explains why the Sun…", "appears to rise and set", [("is hot", "No."), ("causes tides", "No."), ("is a star", "No.")]),
    mc("u14s4p06", "M", "O4", "Newton's laws of gravity explained…", "how planets stay in orbit", [("why the sky is blue", "No."), ("eclipses only", "No."), ("pulsars", "No.")]),
    mc("u14s4p07", "M", "O4", "William Herschel found…", "Uranus", [("Neptune", "Predicted 1846."), ("Jupiter's moons", "Galileo."), ("pulsars", "No.")]),
    mc("u14s4p08", "M", "O4", "Edwin Hubble showed that the Universe is…", "expanding", [("shrinking", "No."), ("flat", "No."), ("Earth-centred", "No.")]),
    mc("u14s4p09", "H", "O4", "Stephen Hawking showed that black holes…", "give off radiation", [("are planets", "No."), ("are moons", "No."), ("are comets", "No.")]),
    mc("u14s4p10", "M", "O4", "Pulsars are…", "spinning remains of stars giving off radio waves", [("planets", "No."), ("comets", "No."), ("moons", "No.")]),
    gd("u14s4p11", "M", "O4", "Which model?", ["Model"], [("Earth at centre", ["Geocentric"]), ("Sun at centre", ["Heliocentric"])], skill="Data"),
    mc("u14s4p12", "H", "O4", "Why were some people slow to accept Copernicus's model?", "They chose evidence that suited their existing opinion", [("There was no evidence", "There was."), ("Telescopes didn't exist", "Galileo had them."), ("It was proven wrong", "No.")], skill="Reasoning"),
    mc("u14s4p13", "H", "O4", "How does science respond to new evidence?", "Old ideas are replaced or updated", [("Ideas never change", "No."), ("Evidence is ignored", "No."), ("Only famous people decide", "No.")]),
    nm("u14s4p14", "H", "O4", "How many years from 1846 (Neptune) to 2026?", 180, "years"),
    mc("u14s4p15", "M", "O4", "Which telescope discovery showed not everything orbits Earth?", "Moons orbiting Jupiter", [("Craters on the Moon", "Not this."), ("Sunspots", "Not this."), ("Rings of Saturn", "Not this.")]),
    mc("u14s4p16", "H", "O4", "Caroline Herschel's catalogue system is…", "still used today", [("lost", "No."), ("only for plants", "No."), ("a type of telescope", "No.")]),
    od("u14s4p17", "M", "O4", "Order these scientists by date.", ["Ptolemy", "Copernicus", "Galileo", "Newton", "Hubble"]),
    mc("u14s4p18", "H", "O4", "Scientists in the Islamic world…", "improved and questioned Ptolemy's ideas", [("invented the flat Earth", "No."), ("discovered Neptune", "No."), ("built rockets", "No.")]),
]
S4_ADV = [
    adv(ex("u14s4a1", "VH", "O4", "Use the history of Solar System models to explain how science works.",
           [("new evidence / observations", ["evidence|observ|telescope"]), ("models replaced or updated", ["replace|update|change|improv"]), ("scientists build on others' work", ["build|earlier|before|others"])],
           "Scientists build on earlier work. When new evidence appears – like Galileo's telescope observations – models are tested and replaced or updated, e.g. geocentric to heliocentric.", need=2)),
    adv(mc("u14s4a2", "VH", "O4", "Why can't a geocentric model easily explain the phases of Venus?", ("Venus's full set of phases needs it to orbit the Sun.", "Correct."), [("Venus doesn't have phases", "It does."), ("Earth is flat", "No."), ("Venus is a star", "No.")], skill="Reasoning")),
    adv(nm("u14s4a3", "VH", "O4", "Copernicus published in 1543 and Newton in 1687. How many years apart?", 144, "years")),
    adv(mc("u14s4a4", "VH", "O4", "A scientist ignores data that disagrees with her idea. Why is this a problem?", ("It is bias – the conclusion may be wrong.", "Correct."), [("It saves time, so it's good", "No."), ("Data is never wrong", "No."), ("It makes a fair test", "No.")], skill="Reasoning")),
]

POOLS = {"14.1": (S1_REQ, S1_PRAC, S1_ADV), "14.2": (S2_REQ, S2_PRAC, S2_ADV), "14.3": (S3_REQ, S3_PRAC, S3_ADV), "14.4": (S4_REQ, S4_PRAC, S4_ADV)}

STOPS = {
    "14.1": [stop("u14v1a", "the Latin word for Sun", mc("u14v1a_q", "M", "O1", "Jupiter, Saturn, Uranus and Neptune are…", "gas giants", [("rocky planets", "Inner."), ("stars", "No."), ("moons", "No.")])),
             stop("u14v1b", "Venus, Mars and Jupiter without a telescope!", mc("u14v1b_q", "M", "O1", "Planets shine because they…", "reflect sunlight", [("make light", "No."), ("burn gas", "No."), ("are stars", "No.")])),
             stop("u14v1c", "This gives us the seasons", mc("u14v1c_q", "H", "O1", "One complete orbit of the Sun is one…", "year", [("day", "Rotation."), ("month", "No."), ("week", "No.")])),
             stop("u14v1d", "about 4.6 billion years ago", mc("u14v1d_q", "H", "O1", "Stars and planets form from…", "a nebula of gas and dust", [("lava", "No."), ("water", "No."), ("comets", "No.")]))],
    "14.2": [stop("u14v2a", "two high tides and two low tides each day", mc("u14v2a_q", "M", "O2", "Tides are mainly caused by the gravity of the…", "Moon", [("Sun only", "Less."), ("Mars", "No."), ("wind", "No.")])),
             stop("u14v2b", "These are neap tides", mc("u14v2b_q", "H", "O2", "Spring tides happen when the Sun and Moon are…", "in line", [("at right angles", "Neap."), ("far apart", "No."), ("behind Earth only", "No.")]))],
    "14.3": [stop("u14v3a", "the corona", mc("u14v3a_q", "M", "O3", "In a solar eclipse, which body is in the middle?", "The Moon", [("Earth", "Lunar."), ("The Sun", "No."), ("Mars", "No.")]))],
    "14.4": [stop("u14v4a", "That's called bias", mc("u14v4a_q", "M", "O4", "Who proposed a Sun-centred model?", "Copernicus", [("Ptolemy", "Earth-centred."), ("Hubble", "No."), ("Hawking", "No.")])),
             stop("u14v4b", "the Universe is expanding", mc("u14v4b_q", "H", "O4", "Neptune was discovered in 1846 by…", "a prediction using Newton's laws", [("Ptolemy", "No."), ("chance only", "No."), ("Galileo", "No.")]))],
}

MINDMAP = {"id": "root", "t": "Earth in space", "sec": None, "kids": [
    {"id": "ss", "t": "Solar System", "d": "Sun (star) • 4 rocky + 4 gas giants • asteroid belt • orbits = gravity + speed • day, year, seasons (tilt) • nebula → protostar → fusion → planets.", "obj": "O1", "sec": "14.1"},
    {"id": "td", "t": "Tides", "d": "Moon's gravity → bulges • two high tides a day • spring (in line) vs neap (right angles) • tide tables.", "obj": "O2", "sec": "14.2"},
    {"id": "ec", "t": "Eclipses", "d": "Solar: Sun–Moon–Earth • lunar: Sun–Earth–Moon (red Moon) • umbra = total, penumbra = partial • never look at the Sun.", "obj": "O3", "sec": "14.3"},
    {"id": "md", "t": "Models of space", "d": "Ptolemy (geocentric) → Islamic scholars → Copernicus (heliocentric) → Galileo → Newton → Herschels → Hubble, Hawking, Bell Burnell • bias.", "obj": "O4", "sec": "14.4"},
]}
