# -*- coding: utf-8 -*-
"""Stage 8 Unit 14 – Planetary Systems. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Earth and Space"
BLURB = "Galaxies and the Milky Way, how our Solar System formed from a nebula, asteroids, dwarf planets and comets, and Earth's magnetic shield."
OBJECTIVES = {
    "O1": {"sec": "14.1", "code": "8ESs.01", "codeNote": "", "t": "Describe a galaxy, the Milky Way and the main shapes of galaxies."},
    "O2": {"sec": "14.2", "code": "8ESs.02", "codeNote": "", "t": "Describe the Solar System, how it formed, and the asteroids, dwarf planets and comets in it."},
    "O3": {"sec": "14.2", "code": "8ESs.02", "codeNote": "asteroids", "t": "Explain why asteroids form a belt and why a comet's tail points away from the Sun."},
    "O4": {"sec": "14.3", "code": "8ESp.01", "codeNote": "", "t": "Describe how Earth's magnetic field is produced and how it protects life."},
}
SECTIONS = [
    {"id": "14.1", "title": "Galaxies", "objs": ["O1"]},
    {"id": "14.2", "title": "Planetary systems", "objs": ["O2", "O3"]},
    {"id": "14.3", "title": "The Earth's magnetic field", "objs": ["O4"]},
]
u = Unit(8, 14)

# ---------------------------------------------------------------- 14.1
u.sec("14.1", "O1")
u.gd("r", "Which galaxy shape is described?", "Shape", [("Has spinning arms like a pinwheel", "Spiral"), ("Oval, like a rugby ball", "Elliptical"), ("Lens-shaped with a central bulge", "Lenticular"), ("No defined shape", "Irregular")])
u.ms("r", "Select ALL the things a galaxy contains.", ["Stars", "Planetary systems", "Gas and stellar dust"], ["Only one star", "Nothing but empty space"])
u.tb("r", "Light travels about 9.5 million million km in one year. Complete the table.", ["Distance (light years)", "Distance (million million km)"], [["1", "9.5"], ["10", B(95)]])
u.ex("r", "Explain why looking at the night sky is like looking back in time.", [("starlight takes time / years to reach us", ["years|time|takes"]), ("we see stars as they were when the light left", ["as they were|in the past|left"])],
     "Light from stars takes years to travel to Earth, so we see each star as it was when the light left it, not as it is now.")
u.mc("r", "The Milky Way is…", "our home galaxy, a spiral of hundreds of billions of stars", [("a single star", "No."), ("a planet", "No."), ("a comet", "No.")])
u.mc("r", "Where is the Sun in the Milky Way?", "On one of the spiral arms", [("At the exact centre", "No, about 27 000 light years out."), ("Outside the galaxy", "No."), ("In Andromeda", "No.")], d="H")
u.mc("r", "Why is stellar dust important?", "It is the building block of new planetary systems.", ["It makes stars brighter.", "It is made of skin and hair.", "It causes light pollution."], d="H")
u.mc("r", "Galaxies on an inflating balloon model all move apart. This shows that the Universe is…", "expanding", ["shrinking", "standing still", "flat"], d="VH")
for p, r, w in [
    ("The Universe is…", "everything: all space, time, matter and energy", ["just the Solar System", "only the Milky Way", "only stars"]),
    ("A galaxy is…", "a huge group of stars, gas and dust held by gravity", ["one star", "one planet", "a moon"]),
    ("Light pollution…", "hides the stars", ["makes stars brighter", "makes new stars", "removes clouds"]),
    ("Our nearest major neighbour galaxy is…", "Andromeda", ["the Sun", "Mars", "the Moon"]),
    ("The Local Group is held together by…", "gravity", ["magnetism", "wind", "friction"]),
    ("How many galaxies are there?", "trillions", ["eight", "one", "about fifty"]),
    ("An elliptical galaxy is shaped like…", "a rugby ball", ["a pinwheel", "a lens", "nothing in particular"]),
    ("A lenticular galaxy is…", "lens-shaped with a bulge", ["oval", "spiral", "shapeless"]),
    ("An irregular galaxy…", "has no defined shape", ["has arms", "is lens-shaped", "is round"]),
    ("Stellar dust is made of tiny specks of…", "ice, carbon, silicon and metals", ["skin and hair", "water only", "sand only"]),
    ("Stellar dust affects astronomers because it…", "blocks their view", ["makes noise", "heats telescopes", "creates moons"]),
    ("A light year is a measure of…", "distance", ["time", "brightness", "mass"]),
    ("Andromeda will reach the Milky Way in about…", "four billion years", ["four years", "forty years", "four hundred years"]),
    ("The Sun is about … light years from the centre of the Milky Way.", "27 000", ["27", "2.7 million", "270"]),
    ("A star is…", "luminous – it gives out its own light", ["non-luminous", "a planet", "a moon"]),
]:
    u.mc("p", p, r, w)
u.mt("p", "Match the term to its meaning.", [("Universe", "everything that exists"), ("Galaxy", "billions of stars held by gravity"), ("Light year", "distance light travels in a year")])
u.od("p", "Order from smallest to largest.", ["Earth", "Solar System", "Milky Way", "Local Group", "Universe"])
u.gd("p", "True or false?", "Answer", [("The Milky Way is a spiral galaxy", "True"), ("The Sun is at the centre of the Milky Way", "False"), ("Galaxies are moving apart", "True")], extra=[])
u.ex("a", "* Advanced. A star is 100 light years away. Explain what this tells you about the light we see from it now.", [("light left 100 years ago", ["100 years"]), ("we see the star as it was then", ["as it was|past|then"]), ("it may have changed since", ["changed|may not|no longer"])],
     "The light left the star 100 years ago, so we see it as it was then. The star may have changed since, or might not exist in the same form now.")
u.nm("a", "Light travels about 9.5 million million km in a year. How many million million km is 4 light years?", 38, "million million km")
u.mc("a", "Why do astronomers see more stars in deserts and on mountains?", "There is less light pollution and less air to look through.", ["They are closer to the stars.", "Stars only shine there.", "There is more stellar dust."], skill="Reasoning")
u.mc("a", "In the balloon model, what do the dots and the balloon's surface represent?", "Dots are galaxies; the stretching surface is expanding space.", ["Dots are planets; the balloon is the Sun.", "Dots are moons; the balloon is Earth.", "Dots are comets; the balloon is a nebula."], skill="Models")
u.stop("light pollution is hiding the stars", "Why can starlight show us cosmic history?", "Starlight takes years to reach us", ["Stars are very small", "Stars move fast", "Stars are made of dust"])
u.stop("about 27 thousand light years from the centre", "The Milky Way is a…", "spiral galaxy", ["planet", "comet", "elliptical galaxy"])
u.stop("Irregular galaxies have no defined shape", "Which is NOT a galaxy shape?", "Triangular", ["Spiral", "Elliptical", "Irregular"])

# ---------------------------------------------------------------- 14.2
u.sec("14.2", "O2")
u.gd("r", "Rocky planet or gas planet?", "Type", [("Mars", "Rocky"), ("Jupiter", "Gas"), ("Venus", "Rocky"), ("Neptune", "Gas")])
u.od("r", "Order the stages in the formation of the Solar System.", ["A nebula of gas and dust", "Gravity pulls it in and it spins", "A protostar forms at the centre", "Protoplanets grow into planets"])
u.gd("r", "Which object is described?", "Object", [("Leftover rock, mostly between Mars and Jupiter", "Asteroid"), ("Ice, dust and rock on a long, thin orbit", "Comet"), ("Rounded but smaller than a planet", "Dwarf planet")])
u.ex("r", "Explain why a comet's tail always points away from the Sun.", [("ice turns to gas near the Sun", ["gas|ice|melt|heat"]), ("dust released", ["dust"]), ("Sun's radiation pushes it away", ["push|radiation|solar wind"])],
     "Near the Sun the comet's ice turns to gas, releasing dust. The Sun's radiation pushes this dust away, so the tail always points away from the Sun.", o="O3")
u.mc("r", "A planetary system is…", "one star and all the objects held in orbit around it by gravity", [("a group of galaxies", "No."), ("only planets", "No."), ("a cloud of gas", "That is a nebula.")])
u.mc("r", "The Solar System formed about…", "4.6 billion years ago", ["4.6 thousand years ago", "4.6 million years ago", "46 years ago"], d="H")
u.mc("r", "Why do planets shine with a steady light rather than twinkling?", "They reflect sunlight and are much closer than stars", [("They give out their own light", "No – they are non-luminous."), ("They are hotter than stars", "No."), ("They are made of gas", "No.")], d="H")
u.mc("r", "Why didn't the asteroids between Mars and Jupiter form a planet?", "Jupiter's strong gravity stopped them joining together", [("They were too hot", "No."), ("They are made of ice", "No."), ("The Sun pushed them away", "No.")], o="O3", d="VH")
for p, r, w, o in [
    ("The Sun is at the centre of the…", "Solar System", ["Milky Way", "Kuiper Belt", "asteroid belt"], "O2"),
    ("How many planets orbit the Sun?", "Eight", ["Nine", "Seven", "Ten"], "O2"),
    ("Planets orbit the Sun in…", "elliptical paths", ["straight lines", "squares", "random paths"], "O2"),
    ("Which planets have no moons?", "Mercury and Venus", ["Earth and Mars", "Jupiter and Saturn", "Uranus and Neptune"], "O2"),
    ("Planets around other stars are called…", "exoplanets", ["asteroids", "comets", "nebulae"], "O2"),
    ("A nebula is…", "a giant cloud of gas and dust", ["a type of planet", "a comet tail", "a moon"], "O2"),
    ("A protostar is…", "a hot young star forming at the centre of a spinning cloud", ["a dead planet", "an asteroid", "a moon"], "O2"),
    ("Protoplanets formed when…", "dust and rock stuck together", ["stars exploded", "comets melted", "moons collided"], "O2"),
    ("Pluto was reclassified as a dwarf planet in…", "2006", ["1906", "1996", "2016"], "O2"),
    ("The Kuiper Belt lies…", "beyond Neptune", ["between Earth and Mars", "inside the Sun", "between Mercury and Venus"], "O2"),
    ("Most asteroids orbit…", "between Mars and Jupiter", ["inside Mercury's orbit", "around the Moon", "beyond the Kuiper Belt"], "O3"),
    ("Comets are made of…", "ice, dust and rock", ["only gas", "only metal", "molten iron"], "O3"),
    ("A comet's orbit is…", "very long and thin", ["perfectly circular", "inside Earth", "fixed in one place"], "O3"),
    ("Planets and moons are…", "non-luminous", ["luminous", "stars", "galaxies"], "O2"),
    ("Dwarf planets have been rounded by…", "their own gravity", ["the wind", "water", "comets"], "O2"),
]:
    u.mc("p", p, r, w, o=o)
u.od("p", "Order the planets from the Sun.", ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
u.ms("p", "Select ALL the gas planets.", ["Jupiter", "Saturn", "Uranus", "Neptune"], ["Mars", "Earth"])
u.gd("p", "Where is each found?", "Location", [("Most asteroids", "Asteroid belt"), ("Icy objects beyond Neptune", "Kuiper Belt"), ("The Sun", "Centre of the Solar System")], o="O3")
u.ex("a", "* Advanced. Explain how gravity was important at each stage of forming the Solar System.", [("pulled the nebula inwards", ["pull|inward|collapse"]), ("formed the protostar / Sun", ["protostar|sun"]), ("held material together into planets and keeps them in orbit", ["planet|orbit|together"])],
     "Gravity pulled the nebula inwards so it spun and formed a hot protostar, which became the Sun. Gravity then pulled dust and rock together into protoplanets and keeps the planets in orbit.")
u.mc("a", "A newly found object is round, orbits the Sun, but shares its orbit with many other objects. It is most likely…", "a dwarf planet", ["a planet", "a star", "a galaxy"], skill="Reasoning")
u.mc("a", "A comet is moving away from the Sun. Which way does its tail point?", "Away from the Sun, so ahead of the comet", ["Behind the comet, towards the Sun", "Sideways always", "It has no tail at all"], o="O3", skill="Reasoning")
u.mc("a", "Why are the inner planets rocky and the outer planets gas giants?", "Near the hot young Sun only rock and metal could stay solid; further out, gas and ice collected.", ["The outer planets are older.", "The inner planets lost their moons.", "Comets made the inner planets."], skill="Reasoning")
u.stop("Ours is the Solar System, with the Sun at its centre", "A planetary system is a star and the objects held around it by…", "gravity", ["magnetism", "wind", "light"])
u.stop("which became the Sun", "The Solar System formed from a…", "nebula", ["comet", "galaxy", "black hole"])
u.stop("Beyond Neptune lies the Kuiper Belt", "Pluto is now classed as a…", "dwarf planet", ["planet", "comet", "star"])
u.stop("a comet's tail always points away from the Sun", "A comet's tail points…", "away from the Sun", ["towards the Sun", "towards Earth", "behind its path always"], o="O3")

# ---------------------------------------------------------------- 14.3
u.sec("14.3", "O4")
u.od("r", "Order how Earth's magnetic field is produced.", ["Molten iron and nickel moves in the outer core", "Electric currents are produced", "A magnetic field forms around Earth"])
u.gd("r", "Which term is described?", "Term", [("Charged particles from the Sun", "Solar wind"), ("Light when particles hit atoms in the air", "Aurora"), ("Liquid iron and nickel", "Outer core")])
u.tb("r", "The magnetic North pole moves about 10 km per year. Complete the table.", ["Years", "Distance moved (km)"], [["1", "10"], ["5", B(50)]])
u.ex("r", "Explain why Earth's magnetic field is important for life.", [("deflects the solar wind", ["deflect|solar wind|charged"]), ("protects the atmosphere from being stripped away", ["atmosphere|strip"]), ("protects living things from harm", ["life|harm|protect"])],
     "The magnetic field deflects the solar wind, which could otherwise strip away our atmosphere and harm living things.")
u.mc("r", "Earth's inner core is…", "solid", ["liquid", "gas", "empty"])
u.mc("r", "Earth's magnetic field is produced by…", "moving molten metal in the outer core", ["the Moon", "the solar wind", "the oceans"], d="H")
u.mc("r", "Is the magnetic North pole at the geographic North Pole?", "No, it is in a different place and slowly wanders", ["Yes, exactly", "It is at the South Pole", "It is at the equator"], d="H")
u.mc("r", "Auroras are caused when…", "solar wind particles collide with atoms in the atmosphere", ["the Moon reflects light", "volcanoes erupt", "clouds freeze"], d="VH")
for p, r, w in [
    ("Earth's outer core is made of molten…", "iron and nickel", ["rock and water", "gold and silver", "ice"]),
    ("Earth's core acts like a…", "giant magnet", ["giant battery", "light bulb", "mirror"]),
    ("The solar wind is…", "charged particles from the Sun", ["moving air on Earth", "light from the Moon", "a type of comet"]),
    ("The magnetic North pole moves about…", "10 km a year", ["10 m a year", "1000 km a year", "not at all"]),
    ("The northern lights are also called…", "the aurora", ["the Milky Way", "a comet", "the solar sail"]),
    ("Solar sails let spacecraft…", "be pushed by the solar wind", ["burn coal", "fly without any force", "pull towards Earth"]),
    ("Without a magnetic field, the solar wind could…", "strip away the atmosphere", ["cool the Sun", "add oceans", "create moons"]),
    ("Earth's magnetic field reaches…", "far into space", ["only to the clouds", "only the poles", "nowhere"]),
    ("A compass needle points to…", "Earth's magnetic north", ["the Sun", "the Moon", "the equator"]),
    ("Electric currents in the core are caused by…", "moving molten metal", ["rainfall", "the Moon's light", "earthquakes on the surface"]),
    ("Auroras are seen most near…", "the poles", ["the equator", "deserts only", "the Moon"]),
    ("The field around Earth is similar to that of a…", "bar magnet", ["horseshoe without poles", "battery", "wire with no current"]),
    ("Charged particles from the Sun are deflected by…", "Earth's magnetic field", ["the oceans", "mountains", "clouds"]),
    ("The layer of Earth that is liquid metal is the…", "outer core", ["crust", "inner core", "atmosphere"]),
    ("The magnetic field protects…", "living things and the atmosphere", ["only the Moon", "only satellites", "nothing"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the effects of the solar wind.", ["Auroras", "Pushing solar sails", "Could strip the atmosphere without a magnetic field"], ["Making the Moon shine", "Causing tides"])
u.gd("p", "Solid or liquid?", "State", [("Inner core", "Solid"), ("Outer core", "Liquid")], extra=[])
u.od("p", "Order the layers from the centre outwards.", ["Inner core", "Outer core", "Mantle", "Crust"])
u.ex("a", "* Advanced. Mars has almost no magnetic field and a very thin atmosphere. Suggest a link between these facts.", [("no field to deflect solar wind", ["deflect|solar wind|no field"]), ("solar wind stripped away atmosphere", ["strip|lost|removed"])],
     "Without a magnetic field, Mars could not deflect the solar wind, so over time the charged particles stripped away most of its atmosphere.")
u.mc("a", "Why must maps used for compass navigation be updated over time?", "The magnetic North pole slowly moves.", ["The geographic pole moves 10 km a year.", "Compasses wear out.", "Earth's core stops."], skill="Reasoning")
u.mc("a", "Why are auroras mostly seen near the poles?", "Earth's field guides charged particles towards the poles.", ["The poles are colder.", "The Sun is closer to the poles.", "There is no atmosphere at the equator."], skill="Reasoning")
u.mc("a", "Which evidence supports the idea that the outer core is liquid metal?", "Earth has a magnetic field that needs moving metal to produce it.", ["Earth's crust is solid rock.", "The Moon has craters.", "Comets have tails."], skill="Evidence")
u.stop("with a field reaching far into space", "Earth's magnetic field is produced by…", "moving molten iron and nickel in the outer core", ["the solar wind", "the Moon", "the crust"])
u.stop("could strip away our atmosphere and harm life", "Earth's magnetic field deflects…", "the solar wind", ["sunlight", "comets", "rain"])
u.stop("pushed by the solar wind, to travel through space", "Auroras are caused by…", "solar wind particles hitting atoms in the atmosphere", ["moonlight", "volcanoes", "lightning"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Planetary systems", "sec": None, "kids": [
    {"id": "un", "t": "Universe", "d": "Everything • Expanding • Light years", "obj": "O1", "sec": "14.1"},
    {"id": "ga", "t": "Galaxies", "d": "Milky Way – spiral • Spiral, elliptical, lenticular, irregular • Stars, gas, stellar dust", "obj": "O1", "sec": "14.1"},
    {"id": "ss", "t": "Solar System", "d": "Sun + 8 planets • Rocky and gas planets • Formed from a nebula 4.6 billion years ago", "obj": "O2", "sec": "14.2"},
    {"id": "sm", "t": "Smaller bodies", "d": "Asteroid belt • Dwarf planets • Kuiper Belt • Comets – tail away from the Sun", "obj": "O3", "sec": "14.2"},
    {"id": "mf", "t": "Magnetic field", "d": "Molten iron and nickel in outer core • Wandering magnetic pole", "obj": "O4", "sec": "14.3"},
    {"id": "sw", "t": "Solar wind", "d": "Deflected by the field • Auroras • Solar sails", "obj": "O4", "sec": "14.3"},
]}
