from science_v2.k import Unit
U = Unit("s8u10")

U.q("R", "10.1", "O1", "Why do we see lightning before we hear thunder?", ("Light travels much faster than sound", "Light reaches us almost instantly."), [("Sound travels faster than light", "Light is much faster."), ("Thunder happens later", "They happen together.")])
U.q("P", "10.2", "O2", "A light ray hits a mirror at 30° to the normal. At what angle is it reflected?", ("30° to the normal", "Angle of incidence = angle of reflection."), [("60°", "That is measured from the mirror surface."), ("90°", "The ray does not reflect straight back unless it hits along the normal.")])
U.q("E", "10.3", "O3", "A straw in water looks bent. Mo says the straw really bends. What is the correct explanation?", ("Light refracts as it passes from water to air", "The change of direction makes it look bent."), [("He is right", "The straw is straight."), ("The water reflects the straw", "It is refraction, not reflection.")])
U.q("R", "10.4", "O4", "Why does a prism split white light into colours?", ("Each colour refracts by a different amount", "Violet bends most, red least."), [("The prism adds colours", "The colours were already in white light."), ("Light is absorbed", "It is refraction, not absorption.")])
U.q("P", "10.5", "O5", "A red shirt is seen under pure blue light. What colour does it look?", ("Black", "A red object only reflects red, and there is no red light."), [("Red", "There is no red light to reflect."), ("Purple", "Colours of light do not mix on the shirt here.")])
V2 = U.V2
