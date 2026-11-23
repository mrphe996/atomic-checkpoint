# -*- coding: utf-8 -*-
"""Stage 8 Unit 10 – Light. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Physics"
BLURB = "Luminous and non-luminous objects, how light travels, reflection and plane mirrors, refraction, dispersion by a prism, and coloured light."
OBJECTIVES = {
    "O1": {"sec": "10.1", "code": "8Ps.04, 8SIC.02", "codeNote": "", "t": "Describe light sources, beams and rays, the speed of light, and how materials transmit, reflect or absorb light."},
    "O2": {"sec": "10.2", "code": "8Ps.01", "codeNote": "", "t": "Describe reflection at a plane surface, use the law of reflection and describe images in a plane mirror."},
    "O3": {"sec": "10.3", "code": "8Ps.02", "codeNote": "", "t": "Describe refraction at air–glass and air–water boundaries in terms of the change in speed of light."},
    "O4": {"sec": "10.4", "code": "8Ps.03", "codeNote": "", "t": "Show that white light is made of many colours by dispersing it with a prism, and explain rainbows."},
    "O5": {"sec": "10.5", "code": "8Ps.04", "codeNote": "", "t": "Explain the colours of objects, and how coloured light can be added, subtracted, absorbed and reflected."},
}
SECTIONS = [
    {"id": "10.1", "title": "Properties of light", "objs": ["O1"]},
    {"id": "10.2", "title": "Reflection", "objs": ["O2"]},
    {"id": "10.3", "title": "Refraction", "objs": ["O3"]},
    {"id": "10.4", "title": "Dispersion of white light", "objs": ["O4"]},
    {"id": "10.5", "title": "Coloured lights", "objs": ["O5"]},
]
u = Unit(8, 10)

# ---------------------------------------------------------------- 10.1
u.sec("10.1", "O1")
u.gd("r", "Luminous or non-luminous?", "Type", [("The Sun", "Luminous"), ("The Moon", "Non-luminous"), ("A firefly", "Luminous"), ("A book", "Non-luminous")])
u.gd("r", "Transparent, translucent or opaque?", "Material", [("Clear glass", "Transparent"), ("Frosted glass", "Translucent"), ("Wood", "Opaque"), ("Metal", "Opaque")])
u.mc("r", "We see a non-luminous object because…", "it reflects light from a source into our eyes", [("it makes its own light", "That is luminous."), ("our eyes send out light", "No."), ("it absorbs all light", "Then it would look black.")])
u.ex("r", "Explain how a shadow forms.", [("light travels in straight lines", ["straight"]), ("opaque object blocks the light", ["block|opaque|stop"]), ("dark area behind where no light reaches", ["behind|no light|dark"])],
     "Light travels in straight lines, so an opaque object blocks it. Behind the object is an area that no light can reach – the shadow.")
u.nm("r", "Light travels about 300 000 000 m/s. Light from the Moon takes 1.28 s to reach us. About how far away is the Moon in km?", 384000, "km", tol=1000, d="H")
u.mc("r", "Why do we see lightning before we hear thunder?", "Light travels much faster than sound", [("Sound is faster", "No."), ("Thunder happens later", "They happen together."), ("Our eyes are closer to the storm", "No.")])
u.mc("r", "A magnifying glass makes a converging beam. Where the rays meet is the…", "focus", ["normal", "shadow", "spectrum"], d="H")
u.mc("r", "Why are solar panels dark in colour?", "Dark colours absorb light well", [("Dark colours reflect light", "No."), ("To look nice", "No."), ("Dark panels are lighter", "No.")], d="VH")
for p, r, w in [
    ("Light is part of the…", "electromagnetic spectrum", ["sound spectrum", "food chain", "periodic table"]),
    ("The colour of light depends on its…", "frequency", ["mass", "temperature only", "loudness"]),
    ("Which colour has the lowest frequency?", "Red", ["Violet", "Blue", "Green"]),
    ("Mixing all colours of light gives…", "white light", ["black", "brown", "no light"]),
    ("The Sun is powered by…", "nuclear reactions", ["burning coal", "electricity", "reflection"]),
    ("Fireflies glow by…", "bioluminescence", ["reflection", "refraction", "dispersion"]),
    ("A laser beam is…", "parallel", ["diverging", "converging", "curved"]),
    ("A torch beam is…", "diverging", ["parallel", "converging", "zero"]),
    ("Light from the Sun reaches us in about…", "8 minutes", ["1 second", "8 hours", "8 days"]),
    ("A light year is a measure of…", "distance", ["time", "brightness", "mass"]),
    ("A light year is about…", "9.5 trillion km", ["9.5 km", "1 year of time", "300 km"]),
    ("Light that is absorbed turns into…", "heat", ["sound", "mass", "electricity always"]),
    ("Light passing through a material is…", "transmitted", ["absorbed", "reflected", "diffused"]),
    ("Unlike sound, light can travel through…", "a vacuum", ["only air", "only water", "only solids"]),
    ("Sunglasses are…", "translucent", ["opaque", "luminous", "transparent like clear glass"]),
]:
    u.mc("p", p, r, w)
u.od("p", "Order the frequencies of light colours, lowest first.", ["Red", "Green", "Blue", "Violet"])
u.mt("p", "Match the beam to an example.", [("Parallel", "laser"), ("Diverging", "torch"), ("Converging", "magnifying glass")])
u.ms("p", "Select ALL the luminous objects.", ["A candle flame", "An LED", "Lightning"], ["A mirror", "The Moon"])
u.ex("a", "* Advanced. Describe an experiment using three cards with holes to show that light travels in straight lines.", [("line up holes and look at candle – see it", ["line|row|see"]), ("move one card out of line – candle disappears", ["move|out of line|disappear"]), ("light cannot bend round the card", ["straight|block"])],
     "Line up the holes in three cards and look through them at a candle – you can see it. Move one card out of line and the candle disappears, because light travels in straight lines and is blocked.")
u.nm("a", "A star is 4 light years away. How many km is that (1 light year ≈ 9.5 trillion km)? Give your answer in trillions of km.", 38, "trillion km")
u.mc("a", "Why can a magnifying glass start a fire?", "It converges the Sun's rays to a focus, concentrating energy in one spot.", ["It makes its own heat.", "It reflects all the light away.", "It produces a parallel beam."], skill="Reasoning")
u.mc("a", "Why can't you read a book in a completely dark room?", "No light reaches the book to be reflected into your eyes.", ["Books are luminous.", "Eyes need sound.", "Dark rooms have no air."], skill="Reasoning")
u.stop("Mix all the colours together, and you get white light", "Which colour of light has the highest frequency?", "Violet", ["Red", "Orange", "Yellow"])
u.stop("That's why you can't read in the dark", "The Moon is…", "non-luminous", ["luminous", "a light source", "a star"])
u.stop("hot enough to start a fire", "A torch makes a…", "diverging beam", ["parallel beam", "converging beam", "single ray"])
u.stop("Opaque materials, like wood and metal, let no light through", "Frosted glass is…", "translucent", ["transparent", "opaque", "luminous"])

# ---------------------------------------------------------------- 10.2
u.sec("10.2", "O2")
u.nm("r", "A ray hits a mirror at 35° to the normal. What is the angle of reflection?", 35, "°")
u.gd("r", "Label the parts of a reflection diagram.", "Part", [("Ray hitting the mirror", "Incident ray"), ("Ray bouncing off", "Reflected ray"), ("Line at 90° to the mirror", "Normal")])
u.tb("r", "Angle of incidence and angle of reflection. Complete the table.", ["Angle of incidence (°)", "Angle of reflection (°)"], [["20", B(20)], ["50", B(50)], ["0", B(0)]])
u.ex("r", "Describe the image you see in a plane mirror.", [("virtual – cannot be put on a screen", ["virtual|screen"]), ("upright, same size", ["upright|same size"]), ("same distance behind / laterally inverted", ["behind|same distance|inverted|left|right"])],
     "The image is virtual (it can't be caught on a screen), upright and the same size as the object. It is the same distance behind the mirror as the object is in front, and laterally inverted.")
u.mc("r", "The law of reflection says…", "the angle of incidence equals the angle of reflection", [("the angle of reflection is always 90°", "No."), ("light bends towards the normal", "That is refraction."), ("angles are measured from the mirror surface", "Measured from the normal.")])
u.mc("r", "A rough surface like paper gives…", "diffuse reflection", ["specular reflection", "refraction", "dispersion"])
u.mc("r", "Why does the image in a plane mirror seem to be behind the mirror?", "The brain traces the reflected rays back in straight lines", [("Light really comes from behind the mirror", "No."), ("Mirrors are transparent", "No."), ("The image is real", "It is virtual.")], d="H")
u.mc("r", "Raise your right hand in front of a mirror. Your image raises…", "its left hand", ["its right hand", "both hands", "no hand"], d="VH")
for p, r, w in [
    ("Reflection is when light…", "bounces off a surface", ["bends", "splits into colours", "is absorbed"]),
    ("The normal is…", "a line at right angles to the mirror", ["the mirror surface", "the incident ray", "the reflected ray"]),
    ("Angles in reflection are measured from the…", "normal", ["mirror surface", "floor", "light source"]),
    ("Smooth shiny surfaces give…", "specular reflection", ["diffuse reflection", "no reflection", "refraction"]),
    ("Specular reflection makes…", "a sharp image", ["no image", "a blurry glow", "colours"]),
    ("Diffuse reflection scatters rays…", "in different directions", ["in one direction", "into colours", "into the normal"]),
    ("A flat mirror is called a…", "plane mirror", ["curved mirror", "prism", "lens"]),
    ("A virtual image…", "cannot be caught on a screen", ["can be caught on a screen", "is upside down always", "is bigger"]),
    ("An image in a plane mirror is…", "upright", ["upside down", "smaller", "coloured"]),
    ("Lateral inversion means…", "left and right are swapped", ["up and down swapped", "the image is bigger", "the image is real"]),
    ("If you stand 2 m in front of a mirror, your image is…", "2 m behind the mirror", ["4 m behind", "1 m behind", "on the mirror surface"]),
    ("Incident ray, reflected ray and normal are…", "in the same plane", ["at random angles", "always parallel", "the same line"]),
    ("A ray along the normal is reflected…", "straight back", ["at 90°", "sideways", "not at all"]),
    ("Ambulances have 'AMBULANCE' written backwards so that…", "drivers read it correctly in their mirrors", ["it looks unusual", "it is cheaper", "it reflects light"]),
    ("We see paper from any angle because of…", "diffuse reflection", ["specular reflection", "refraction", "dispersion"]),
]:
    u.mc("p", p, r, w)
u.nm("p", "A ray strikes a mirror at 25° to the mirror surface. What is the angle of incidence (from the normal)?", 65, "°")
u.ms("p", "Select ALL the features of an image in a plane mirror.", ["Virtual", "Upright", "Same size"], ["Real", "Upside down"])
u.gd("p", "Specular or diffuse reflection?", "Reflection", [("Mirror", "Specular"), ("Paper", "Diffuse"), ("Still water", "Specular"), ("Wall paint", "Diffuse")])
u.ex("a", "* Advanced. A periscope uses two mirrors at 45°. Explain how it lets you see over a wall.", [("light reflects off top mirror down", ["top|first|down"]), ("reflects off bottom mirror into eye", ["bottom|second|eye"]), ("angle of incidence = reflection, turns 90° each time", ["45|90|angle"])],
     "Light from above hits the top mirror at 45° and reflects straight down the tube. It hits the bottom mirror at 45° and reflects into your eye, so you see over the wall.")
u.nm("a", "The angle between the incident ray and the reflected ray is 110°. What is the angle of incidence?", 55, "°")
u.mc("a", "Why is a road sign easier to read at night than a matt sign?", "It uses special reflective materials that send light back towards the driver.", ["It makes its own light.", "It absorbs headlights.", "It refracts light into colours."], skill="Reasoning")
u.mc("a", "You stand 3 m from a mirror and walk 1 m towards it. How far are you now from your image?", "4 m", ["2 m", "6 m", "3 m"], skill="Reasoning")
u.stop("at right angles to the mirror", "The line at right angles to the mirror is the…", "normal", ["incident ray", "reflected ray", "focus"])
u.stop("it's reflected at 35 degrees", "The angle of incidence equals…", "the angle of reflection", ["90°", "the angle of refraction", "zero"])
u.stop("your image raises its left", "An image in a plane mirror is…", "virtual", ["real", "upside down", "smaller"])

# ---------------------------------------------------------------- 10.3
u.sec("10.3", "O3")
u.gd("r", "Towards or away from the normal?", "Bends", [("Light going from air into glass", "Towards the normal"), ("Light going from water into air", "Away from the normal"), ("Light going from air into water", "Towards the normal")])
u.mc("r", "Refraction happens because…", "light travels at different speeds in different materials", [("light bounces off surfaces", "That is reflection."), ("light is absorbed", "No."), ("light splits into colours only", "That is dispersion.")])
u.tb("r", "Optical density order: 1 = least dense (fastest light). Complete the table.", ["Material", "Rank"], [["Air", "1"], ["Water", B(2)], ["Glass", B(3)]])
u.ex("r", "Explain why a pencil in a glass of water looks bent.", [("light from the pencil refracts at the water surface", ["refract|bend"]), ("speeds up / bends away from normal into air", ["speed|away"]), ("brain assumes straight lines – appears in a different place", ["straight|brain|appears"])],
     "Light from the underwater part of the pencil speeds up and bends away from the normal as it leaves the water. Our brain assumes light travels in straight lines, so that part appears in a different place.")
u.mc("r", "A ray hitting a glass block along the normal…", "does not bend", [("bends towards the normal", "Only at an angle."), ("is reflected back", "No."), ("splits into colours", "No.")])
u.mc("r", "Why does a fish look closer to the surface than it really is?", "Light from the fish bends away from the normal as it leaves the water", [("Water magnifies everything", "No."), ("Fish swim upwards", "No."), ("Light speeds up in water", "It slows in water.")], d="H")
u.mc("r", "In the go-kart analogy, the kart turns because…", "the wheel reaching the grass first slows down", [("both wheels speed up", "No."), ("grass is slippery", "No."), ("the kart stops", "No.")], d="H")
u.mc("r", "Why do stars twinkle?", "Their light is refracted again and again by the changing air", [("Stars switch on and off", "No."), ("Space has clouds", "No."), ("Our eyes blink", "No.")], d="VH")
for p, r, w in [
    ("Refraction means light…", "bends as it passes into another material", ["bounces back", "is absorbed", "stops"]),
    ("Light is fastest in…", "air", ["water", "glass", "diamond"]),
    ("Light is slowest in…", "glass", ["air", "water", "a vacuum"]),
    ("Glass has a higher…", "optical density than water", ["temperature than air", "speed of light", "colour"]),
    ("When light slows down it bends…", "towards the normal", ["away from the normal", "not at all", "back"]),
    ("When light speeds up it bends…", "away from the normal", ["towards the normal", "not at all", "upwards"]),
    ("A ray entering a glass block bends…", "once on the way in and again on the way out", ["only once", "never", "three times"]),
    ("A camera lens is made of…", "curved glass or plastic", ["a flat mirror", "metal", "paper"]),
    ("A camera lens bends light so that rays meet on the…", "sensor", ["shutter", "battery", "screen outside"]),
    ("Refraction makes swimming pools look…", "shallower than they are", ["deeper than they are", "the same depth", "empty"]),
    ("Light going from air to water…", "slows down", ["speeds up", "stops", "turns into sound"]),
    ("Which shows refraction?", "A straw looking bent in a drink", ["A mirror image", "A shadow", "An echo"]),
    ("Spearing a fish is hard because of…", "refraction", ["reflection", "absorption", "diffusion"]),
    ("Lenses in glasses work by…", "refraction", ["reflection", "absorption", "diffusion"]),
    ("A boundary is where…", "two materials meet", ["light starts", "the normal ends", "colours mix"]),
]:
    u.mc("p", p, r, w)
u.od("p", "Order the materials by the speed of light, fastest first.", ["Air", "Water", "Glass"])
u.ms("p", "Select ALL the effects caused by refraction.", ["A pencil looking bent in water", "Stars twinkling", "A pool looking shallow"], ["Seeing yourself in a mirror", "A shadow"])
u.mt("p", "Match the boundary to how light bends.", [("Air → glass", "towards the normal"), ("Glass → air", "away from the normal"), ("Along the normal", "no bending")])
u.ex("a", "* Advanced. Use the go-kart analogy to explain why light bends towards the normal when it enters glass at an angle.", [("one side of the beam reaches glass first", ["one side|first|edge"]), ("that side slows down first", ["slow"]), ("beam turns towards the normal", ["turn|towards|bend"])],
     "When light hits glass at an angle, one side of the beam enters first and slows down while the other side is still fast. Like a go-kart wheel hitting grass, this turns the beam towards the normal.")
u.mc("a", "A ray of light enters water at 0° to the normal. What happens?", "It slows down but does not change direction.", ["It bends towards the normal.", "It bends away from the normal.", "It is totally reflected."], skill="Reasoning")
u.mc("a", "Why does a diamond sparkle more than glass?", "It has a higher optical density, so it bends light more.", ["It is luminous.", "It is opaque.", "It absorbs all light."], skill="Reasoning")
u.gd("a", "Speeds up, slows down or no change?", "Speed", [("Air → water", "Slows down"), ("Glass → air", "Speeds up"), ("Air → air", "No change")])
u.stop("bends once on the way in, and again on the way out", "When light passes from one material into another and bends, this is…", "refraction", ["reflection", "dispersion", "absorption"])
u.stop("When it speeds up, it bends away", "When light slows down entering glass, it bends…", "towards the normal", ["away from the normal", "back", "not at all"])
u.stop("which makes it hard to catch", "A pencil looks bent in water because of…", "refraction", ["reflection", "absorption", "diffusion"])

# ---------------------------------------------------------------- 10.4
u.sec("10.4", "O4")
u.od("r", "Put the colours of the spectrum in order from least bent to most bent.", ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"])
u.gd("r", "Bent most or least by a prism?", "Bending", [("Red light", "Least"), ("Violet light", "Most")])
u.mc("r", "Splitting white light into a spectrum is called…", "dispersion", ["reflection", "diffusion", "absorption"])
u.ex("r", "Explain why a prism splits white light into colours.", [("white light is a mixture of colours", ["mixture|all colours"]), ("each colour travels at a different speed in glass", ["different speed"]), ("so each bends by a different amount", ["different amount|bend"])],
     "White light is a mixture of colours. In glass each colour travels at a slightly different speed, so each is refracted by a different amount and the colours spread out.")
u.tb("r", "Number of times sunlight is refracted or reflected in a raindrop to make a rainbow.", ["Process", "Number of times"], [["Refracted", B(2)], ["Reflected", B(1)]])
u.mc("r", "White light is…", "a mixture of all colours", [("one colour", "No."), ("only red and blue", "No."), ("colourless and empty", "No.")])
u.mc("r", "In a raindrop, sunlight is refracted on entering, reflected off the back and…", "refracted again as it leaves", [("absorbed", "No."), ("reflected again only", "No."), ("not refracted", "No.")], d="H")
u.mc("r", "To see a rainbow, where must the Sun be?", "Behind you, shining on the rain in front of you", [("In front of you", "No."), ("Below the horizon", "No."), ("Directly overhead always", "No.")], d="VH")
for p, r, w in [
    ("A spectrum is…", "the band of colours from white light", ["a mirror image", "a shadow", "a sound"]),
    ("Which colour bends least in a prism?", "Red", ["Violet", "Blue", "Green"]),
    ("Which colour bends most in a prism?", "Violet", ["Red", "Orange", "Yellow"]),
    ("A prism is made of…", "glass or clear plastic", ["metal", "wood", "paper"]),
    ("Rainbows form in…", "raindrops", ["clouds of dust", "mirrors", "the Sun"]),
    ("Light entering a prism…", "slows down and bends", ["speeds up", "stops", "turns to heat"]),
    ("Each colour travels in glass at…", "a slightly different speed", ["exactly the same speed", "no speed", "the speed of sound"]),
    ("How many main colours are there in the spectrum?", "Seven", ["Three", "Two", "Twelve"]),
    ("A rainbow shows that sunlight is…", "made of many colours", ["one colour", "only white", "only red"]),
    ("Dispersion is caused by…", "refraction", ["reflection only", "absorption", "diffusion"]),
    ("Who first showed white light is a mix of colours using prisms?", "Isaac Newton", ["Charles Darwin", "Marie Curie", "Galileo"]),
    ("Putting a spectrum back through a second prism makes…", "white light again", ["black", "only red", "nothing"]),
    ("Blue light bends…", "more than red light", ["less than red light", "the same as red", "not at all"]),
    ("Soap bubbles shimmer with colours because…", "white light is split into colours", ["they are luminous", "they absorb all light", "they are opaque"]),
    ("The colour in the middle of the spectrum is…", "green", ["red", "violet", "black"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the colours in the visible spectrum.", ["Red", "Green", "Violet"], ["Black", "Brown"])
u.mt("p", "Match the term to its meaning.", [("Dispersion", "splitting white light into colours"), ("Spectrum", "the band of colours"), ("Prism", "a glass block that disperses light")])
u.gd("p", "True or false?", "Answer", [("Red light bends least in a prism", "True"), ("White light is one colour", "False"), ("Rainbows need sunlight and raindrops", "True")])
u.ex("a", "* Advanced. Explain why you never see a rainbow at midday with the Sun high overhead in a clear sky.", [("need raindrops / rain", ["rain|drop"]), ("Sun must be behind the observer and low", ["behind|low"]), ("light must reflect back towards eyes at the right angle", ["angle|reflect|back"])],
     "A rainbow needs raindrops in front of you and the Sun behind you, fairly low, so that light is refracted and reflected back towards your eyes at the right angle. A clear sky at midday has neither.")
u.mc("a", "If only red light shines into a prism, what comes out?", "Only red light, bent", ["A full spectrum", "White light", "No light"], skill="Reasoning")
u.mc("a", "Why does violet light bend more than red light in glass?", "Violet light slows down more in glass.", ["Violet light speeds up.", "Red light is heavier.", "Violet light is reflected."], skill="Reasoning")
u.od("a", "* Advanced. Order what happens to sunlight in a raindrop.", ["Refracted as it enters", "Reflected off the back of the drop", "Refracted again as it leaves", "Colours spread out"])
u.stop("This is called dispersion", "Which colour bends most in a prism?", "Violet", ["Red", "Orange", "Yellow"])
u.stop("splitting white light into a spectrum of colours", "Rainbows form when sunlight is refracted and reflected by…", "raindrops", ["mirrors", "clouds of dust", "the Moon"])

# ---------------------------------------------------------------- 10.5
u.sec("10.5", "O5")
u.gd("r", "What colour does each object look in white light?", "Looks", [("Reflects only red light", "Red"), ("Reflects all colours", "White"), ("Absorbs all colours", "Black")])
u.gd("r", "Additive mixing: what colour do these lights make?", "Result", [("Red + green", "Yellow"), ("Red + green + blue", "White"), ("Red + blue", "Magenta"), ("Green + blue", "Cyan")])
u.mc("r", "A blue object under red light looks…", "black", [("blue", "There is no blue light to reflect."), ("red", "It absorbs red."), ("purple", "No.")])
u.ex("r", "Explain why a red apple looks red in white light.", [("white light contains all colours", ["all colours|white light"]), ("apple reflects red light", ["reflect.*red"]), ("absorbs the other colours", ["absorb"])],
     "White light contains all colours. The apple reflects red light into our eyes and absorbs all the other colours, so it looks red.")
u.mc("r", "The primary colours of light are…", "red, green and blue", ["red, yellow and blue", "cyan, magenta and yellow", "black and white"])
u.mc("r", "A green filter…", "lets green light through and absorbs other colours", [("adds green to white light", "No – it removes colours."), ("reflects all colours", "No."), ("makes everything white", "No.")], d="H")
u.mc("r", "Printers use which primary colours?", "Cyan, magenta and yellow", ["Red, green and blue", "Black and white only", "Orange and violet"], d="H")
u.mc("r", "A white shirt under green light looks…", "green", ["white", "black", "red"], d="VH")
for p, r, w in [
    ("A non-luminous object's colour depends on…", "the light it reflects", ["the light it makes", "its mass", "its temperature"]),
    ("White objects…", "reflect all colours", ["absorb all colours", "make light", "reflect only white"]),
    ("Black objects…", "absorb all colours", ["reflect all colours", "make light", "reflect black light"]),
    ("Adding coloured lights together is…", "additive colour mixing", ["subtractive mixing", "dispersion", "refraction"]),
    ("Red and green light make…", "yellow", ["brown", "white", "black"]),
    ("Red, green and blue light together make…", "white", ["black", "brown", "grey"]),
    ("Screens make colours using tiny…", "pixels of red, green and blue light", ["mirrors", "prisms", "black dots only"]),
    ("Filters work by…", "absorbing (subtracting) colours", ["adding colours", "reflecting all light", "making light"]),
    ("Subtractive primary colours are…", "cyan, magenta and yellow", ["red, green and blue", "red, orange and violet", "black and white"]),
    ("A red object under green light looks…", "black", ["red", "green", "yellow"]),
    ("A red filter lets through…", "red light", ["green light", "blue light", "all light"]),
    ("Light shining through a red then a green filter gives…", "no light (black)", ["yellow", "white", "red"]),
    ("Blue and green light make…", "cyan", ["magenta", "yellow", "white"]),
    ("Red and blue light make…", "magenta", ["cyan", "yellow", "white"]),
    ("Stage lights use filters to…", "make coloured light", ["make white light", "make sound", "cool the stage"]),
]:
    u.mc("p", p, r, w)
u.gd("p", "What colour does each object look under red light?", "Looks", [("Red car", "Red"), ("Blue book", "Black"), ("White paper", "Red")])
u.ms("p", "Select ALL the primary colours of light.", ["Red", "Green", "Blue"], ["Yellow", "Magenta"])
u.mt("p", "Match the mixing type to its primary colours.", [("Additive (light)", "red, green, blue"), ("Subtractive (printing)", "cyan, magenta, yellow")])
u.ex("a", "* Advanced. A green leaf is seen under blue light. Predict its colour and explain.", [("looks black / very dark", ["black|dark"]), ("blue light absorbed", ["absorb"]), ("no green light to reflect", ["no green|green light"])],
     "It looks black (very dark). The leaf absorbs the blue light, and there is no green light shining on it to reflect, so no light reaches our eyes from it.")
u.mc("a", "Why do some shops use special lighting on meat counters?", "Red-rich light makes meat reflect more red and look fresher.", ["It makes meat heavier.", "It cools the meat.", "It removes colour."], skill="Reasoning")
u.mc("a", "A yellow object reflects red and green light. How does it look under blue light?", "Black", ["Yellow", "Blue", "White"], skill="Reasoning")
u.gd("a", "What colour comes out of each filter combination (white light first)?", "Result", [("Red filter only", "Red"), ("Red filter then blue filter", "Black"), ("Yellow filter then red filter", "Red")])
u.stop("black objects absorb them all", "A red apple reflects red light and…", "absorbs other colours", ["reflects all colours", "makes its own light", "absorbs red"])
u.stop("so it looks black", "A blue object under red light looks…", "black", ["blue", "red", "white"])
u.stop("used in printing and photography", "Red and green light make…", "yellow", ["white", "brown", "cyan"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Light", "sec": None, "kids": [
    {"id": "lu", "t": "Sources and beams", "d": "Luminous vs non-luminous • Parallel, diverging, converging beams • Straight lines", "obj": "O1", "sec": "10.1"},
    {"id": "ma", "t": "Materials", "d": "Transparent • Translucent • Opaque • Absorb, reflect, transmit", "obj": "O1", "sec": "10.1"},
    {"id": "re", "t": "Reflection", "d": "Angle i = angle r • Normal • Specular vs diffuse • Virtual image", "obj": "O2", "sec": "10.2"},
    {"id": "rf", "t": "Refraction", "d": "Speed changes • Slows → towards normal • Bent pencil, lenses", "obj": "O3", "sec": "10.3"},
    {"id": "di", "t": "Dispersion", "d": "Prism splits white light • Violet bends most • Rainbows", "obj": "O4", "sec": "10.4"},
    {"id": "co", "t": "Colour", "d": "Reflect one colour, absorb others • RGB additive • CMY subtractive • Filters", "obj": "O5", "sec": "10.5"},
]}
