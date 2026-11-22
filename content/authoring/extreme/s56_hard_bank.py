"""Stage 5 and Stage 6 Science (Primary) — extra Hard (* Advanced) questions written by Atomic (original contexts and numbers).
Edits content/src/stage5-unitNN.json and stage6-unitNN.json in place; safe to run again. Then: node tools/build-content.mjs"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hardkit import *

def short_para(*a, **k):   # Stages 5–6: one or two full sentences
    q = para(*a, frame='I think … because …', words=10, **k); q['sentences'] = [1, 2]; q['diff'] = 'H'; return q

# =============================== STAGE 5 ===============================
B = {}
def add(u, sec, *qs): B.setdefault((u, sec), []).extend(qs)

add(1, '1.2', mcq('p5u01s2h01', 'O2', 'A pumpkin plant has two kinds of flower. Flower A has stamens covered in pollen but no stigma. Flower B has a stigma and a small swelling below the petals but no stamens. Which statement is correct?',
    'A is the male flower. A bee must carry pollen from A to the stigma of B before a pumpkin can grow.',
    [('B is the male flower, because it has a swelling.', 'The swelling is the ovary, a female part.'), ('Each flower can pollinate itself.', 'A has no stigma and B has no pollen.'), ('The pumpkin grows from flower A.', 'Fruits grow from the ovary, which is in flower B.')]))
add(1, '1.3',
  num('p5u01s3h01', 'O4', 'A winged seed is dropped three times from the same height. It stays in the air for 3.2 s, 3.6 s and 3.4 s. Calculate the average (mean) time.', 3.4, 's', ['s', 'm'],
      'Add the three times: 3.2 + 3.6 + 3.4 = 10.2. Divide by 3: 10.2 ÷ 3 = 3.4 s.'),
  mcq('p5u01s3h02', 'O3', 'Three seeds are dropped from the same height. Which seed is best adapted to be spread by the wind, and why?', 'Seed B: it stays in the air longest, so the wind can carry it furthest.',
      [('Seed A: it falls fastest.', 'A fast fall gives the wind no time to move it.'), ('Seed C: it is the heaviest.', 'Heavy seeds fall quickly near the parent plant.'), ('All three are the same.', 'Their times are very different.')],
      data=[['Seed', 'Average time in the air'], ['A (round and smooth)', '0.6 s'], ['B (with a thin wing)', '3.4 s'], ['C (large and heavy)', '0.5 s']], skill='Data'))
add(1, '1.4', graph('p5u01s4h01', 'O5', 'A bean seedling is measured every two days. Plot its height.', ax('Day', 2, 10, 2), ax('Height (mm)', 0, 50, 10),
    [[2, 0], [4, 10], [6, 30], [8, 40], [10, 50]],
    'Between which days did the seedling grow fastest?', 'Between day 4 and day 6',
    [('Between day 2 and day 4', 'It grew 10 mm then, but 20 mm between days 4 and 6.'), ('Between day 6 and day 8', 'It grew 10 mm then.'), ('Between day 8 and day 10', 'It grew 10 mm then.')]))

add(2, '2.1',
  num('p5u02s1h01', 'O1', 'A ticking clock is placed against different materials and the sound on the other side is measured. How much louder is the sound through metal than through air?', 30, 'dB', ['dB'],
      'Metal 70 dB, air 40 dB: 70 − 40 = 30 dB.', fig=bars(['air', 'water', 'wood', 'metal'], [40, 55, 60, 70], 80, 10, 'Loudness in dB')),
  mcq('p5u02s1h02', 'O1', 'In the clock test, sound was quietest through air and loudest through metal. What is the best explanation?',
      'In a solid the particles are close together, so vibrations pass from one to the next easily.',
      [('Sound cannot travel through gases.', 'We hear through air every day.'), ('Metal makes its own sound.', 'The metal only passes on the vibrations from the clock.'), ('Air particles are too heavy to vibrate.', 'They vibrate, but they are far apart.')]))
add(2, '2.3', mcq('p5u02s3h01', 'O3', 'You roll a sheet of card into a cone and hold the narrow end to your ear. Why do quiet sounds seem louder?',
    'The wide end collects more of the sound and directs it into your ear.',
    [('The card makes new sound.', 'The card only gathers sound that is already there.'), ('The cone makes the pitch higher.', 'The loudness changes, not the pitch.'), ('The cone stops vibrations.', 'It guides vibrations into the ear.')]))
add(2, '2.4', mcq('p5u02s4h01', 'O5', 'Five identical bottles hold different amounts of water. You blow across the top of each. Which bottle gives the highest note?',
    'The bottle with the most water, because it has the shortest column of air to vibrate.',
    [('The empty bottle, because it has the most air.', 'A long air column vibrates slowly and gives a low note.'), ('They all give the same note.', 'The length of the air column changes the pitch.'), ('The bottle with the most water, because water vibrates faster than air.', 'When you blow, it is the air that vibrates.')]))

add(3, '3.1', mcq('p5u03s1h01', 'O1', 'You block the end of a syringe full of air and push the plunger: it moves in. With a syringe full of water it does not move. Why?',
    'In a gas the particles are far apart and can be pushed closer; in a liquid they are already touching.',
    [('Air particles are softer than water particles.', 'Particles are not soft or hard; the spacing is different.'), ('Water particles are bigger.', 'Size is not the reason.'), ('Air leaks out through the plastic.', 'The end is blocked and no air escapes.')]))
add(3, '3.2', mcq('p5u03s2h01', 'O2', 'A class measures the temperature at which some liquids boil. What do the results show?',
    'Dissolving salt in water raises its boiling point, and more salt raises it more.',
    [('Salt lowers the boiling point.', 'The values go up from 100 °C.'), ('Salt makes no difference.', 'The boiling point changes from 100 °C to 104 °C.'), ('Only pure water can boil.', 'All three liquids boiled.')],
    data=[['Liquid', 'Boiling point'], ['pure water', '100 °C'], ['water with 1 spoon of salt', '102 °C'], ['water with 2 spoons of salt', '104 °C']], skill='Data'))
add(3, '3.3',
  graph('p5u03s3h01', 'O3', '250 ml of water is left in a wide dish on a sunny windowsill. Plot the volume left each day.', ax('Day', 1, 5, 1), ax('Volume of water (ml)', 0, 250, 50),
        [[1, 250], [2, 200], [3, 150], [4, 100], [5, 50]],
        'The same volume in a narrow jar lost only 10 ml each day. Why did the wide dish lose water faster?', 'It has a bigger surface, so more water particles can escape into the air.',
        [('The dish is hotter than the jar.', 'They are on the same windowsill.'), ('Water leaks through the dish.', 'The water evaporates; it does not leak.'), ('The jar has more water.', 'They started with the same volume.')]),
  num('p5u03s3h02', 'O4', 'A wide dish holds 250 ml of water and loses 50 ml by evaporation every day. After how many days will the dish be empty?', 5, 'days', ['days', 'ml'], '250 ÷ 50 = 5 days.'))
add(3, '3.4', short_para('p5u03s4h01', 'O5', 'Sugar is stirred into water until you cannot see it. How could you show that the sugar is still there, without tasting it?',
    [('Evaporate or boil away the water', 'evaporat|boil|heat|leave'), ('Sugar (crystals) is left behind', 'left|crystal|remain|sugar'), ('Or: the mass of the solution is more than the water alone', 'mass|weigh|heavier')], 2,
    'I would leave the solution in a warm place so the water evaporates. The sugar is left behind as crystals in the dish.'))

add(4, '4.1', mcq('p5u04s1h01', 'O2', 'Cooked rice is mixed with iodine in two beakers, and both turn blue-black. Saliva is added to beaker 1 and the same volume of water to beaker 2. After ten minutes only beaker 1 has lost its blue-black colour. What does this show?',
    'Saliva breaks down the starch in rice; beaker 2 shows that water alone does not.',
    [('Water breaks down starch.', 'Beaker 2 stayed blue-black.'), ('Iodine breaks down starch.', 'Iodine is in both beakers; it only shows that starch is there.'), ('Rice contains no starch.', 'Both turned blue-black at the start, so starch was there.')]))
add(4, '4.2',
  num('p5u04s2h01', 'O3', 'The label on a tin of beans says there are 5 g of protein in every 100 g. Minh eats 250 g of beans. How much protein does he eat?', 12.5, 'g', ['g', 'kg'],
      '250 g is 2.5 lots of 100 g: 2.5 × 5 = 12.5 g.'),
  mcq('p5u04s2h02', 'O4', 'Use the food labels. A growing child needs plenty of protein. Which is the better choice, and why?', 'Tuna: it has much more protein in every 100 g.',
      [('Beans: they have more carbohydrate.', 'Carbohydrate gives energy; protein is for growth.'), ('Beans: they have more protein.', 'Beans have 5 g; tuna has 25 g.'), ('They are the same.', 'The amounts are very different.')],
      data=[['In 100 g', 'Protein', 'Carbohydrate', 'Fat'], ['beans in tomato sauce', '5 g', '13 g', '0.5 g'], ['tuna in water', '25 g', '0 g', '1 g']], skill='Data'))

add(5, '5.1', mcq('p5u05s1h01', 'O1', 'A heavy box rests on a table and does not move. Which forces act on the box?',
    'Gravity pulls it down and the normal force from the table pushes up with the same size.',
    [('Only gravity, because nothing is pushing it.', 'With only gravity it would fall through the table.'), ('No forces, because it is not moving.', 'Balanced forces also give no movement.'), ('Friction pushes it up.', 'The upward force from a surface is the normal force.')]))
add(5, '5.2', mcq('p5u05s2h01', 'O2', 'A rocket launches a satellite, but the satellite ends up moving too slowly to stay in orbit. What happens to it?',
    'Gravity pulls it back down to the Earth.',
    [('It floats away into space.', 'It would need to be much faster to escape.'), ('It stays still above the Earth.', 'Gravity is still pulling it.'), ('It orbits lower but for ever.', 'Without enough speed it keeps falling.')]))
add(5, '5.3', multi('p5u05s3h01', 'O3', 'A dolphin moves very fast through the sea. Select the TWO features that reduce water resistance.',
    [('a smooth, pointed (streamlined) body', True), ('smooth skin with no fur', True), ('a large mass', False), ('big eyes', False)],
    'A streamlined shape and a smooth surface let the water flow past easily.'))
add(5, '5.4', mcq('p5u05s4h01', 'O4', 'A swimmer moves forwards at a steady speed across a pool. Which four forces act on her?',
    'weight down, upthrust up, her push forwards and water resistance backwards',
    [('weight, magnetism, air resistance and friction', 'Magnetism is not acting here.'), ('only her push forwards', 'Gravity, upthrust and water resistance also act.'), ('weight up, upthrust down, push backwards, water resistance forwards', 'All four directions are the wrong way round.')]))
add(5, '5.5', mcq('p5u05s5h01', 'O5', 'To make a compass, you stroke a steel needle many times in one direction with a bar magnet, then float it on a cork in water. Why does it work?',
    'Stroking makes the needle a magnet, and floating lets it turn freely to line up north–south.',
    [('The cork is magnetic.', 'Cork is not magnetic; it only lets the needle turn.'), ('The water pulls the needle north.', 'Water is not magnetic.'), ('Any piece of metal points north.', 'Only a magnet lines up with the Earth\'s magnetic field.')]))
add(5, '5.6', mcq('p5u05s6h01', 'O6', 'A maglev train floats a few centimetres above its track. How do magnets make this possible, and why is the train so fast?',
    'Like poles on the train and track repel and lift the train, so there is no friction with the track.',
    [('Opposite poles attract and lift the train.', 'Attraction would pull the train down onto the track.'), ('The magnets make the train lighter.', 'Its weight is the same; the magnetic force balances it.'), ('The magnets remove air resistance.', 'Air resistance still acts; friction with the track is removed.')]))

add(6, '6.1', mcq('p5u06s1h01', 'O1', 'The Earth is drawn at four places on its path around the Sun, three months apart. How long does the Earth take to move from one place to the place opposite?',
    'About six months (half a year)',
    [('About one day', 'One day is one spin of the Earth, not part of its orbit.'), ('About one month', 'One month is about one orbit of the Moon.'), ('About one year', 'A year is the whole orbit; opposite is halfway.')]))
add(6, '6.2',
  num('p5u06s2h01', 'O3', 'An Arctic tern flies about 40 000 km every year between the Arctic and the Antarctic. How far does it fly in a life of 30 years?', 1200000, 'km', ['km', 'm'],
      '40 000 × 30 = 1 200 000 km.'),
  mcq('p5u06s2h02', 'O2', 'Arctic terns raise chicks in the Arctic in June, then fly to the Antarctic for December. Why is this a good pattern for them?',
      'They have summer in both places, with long days and plenty of food.',
      [('They like cold, dark winters.', 'They leave each place before its winter.'), ('They are escaping from the Sun.', 'They follow the summer daylight.'), ('The Earth stops spinning in winter.', 'The Earth always spins.')]))
add(6, '6.3', mcq('p5u06s3h01', 'O4', 'A frog can stay under water for a long time without coming up to breathe. Which adaptation makes this possible?',
    'Its thin, moist skin lets oxygen dissolved in the water pass into its blood.',
    [('It has gills like a fish.', 'Adult frogs have lungs, not gills.'), ('It does not need oxygen.', 'All animals need oxygen.'), ('Its strong legs make oxygen.', 'Legs are for jumping and swimming.')]))
add(6, '6.4', short_para('p5u06s4h01', 'O5', 'An owl hunts mice at night. Describe one adaptation of the owl and explain how it helps the owl to catch its prey.',
    [('Names an adaptation: large eyes, soft silent feathers, sharp talons, hooked beak or good hearing', 'eye|feather|talon|claw|beak|hear|ear'), ('Explains how it helps: see or hear in the dark, fly silently, grip or kill', 'see|dark|silent|quiet|grip|grab|hold|hear')], 2,
    'An owl has soft feathers so it can fly silently. This helps because the mouse does not hear the owl coming.'))
apply(5, B)

# =============================== STAGE 6 ===============================
B = {}
add(1, '1.1',
  num('p6u01s1h01', 'O2', 'Linh measures her pulse during different activities. How many more times does her heart beat each minute when she plays football than when she sits still?', 80, 'beats per minute', ['beats per minute'],
      'Football 150, sitting 70: 150 − 70 = 80 beats per minute.', fig=bars(['sitting', 'walking', 'skipping', 'football'], [70, 95, 130, 150], 160, 20, 'Pulse in beats per minute')),
  graph('p6u01s1h02', 'O2', 'After a race, a runner sits down and measures her pulse every minute. Plot the results.', ax('Time after the race (minutes)', 0, 4, 1), ax('Pulse (beats per minute)', 60, 150, 10),
        [[0, 150], [1, 120], [2, 100], [3, 80], [4, 70]],
        'Her resting pulse is 70 beats per minute. What do the results show?', 'Her pulse falls quickly at first and is back to resting after 4 minutes.',
        [('Her pulse rises after exercise stops.', 'It falls from 150 to 70.'), ('Her pulse never returns to resting.', 'It reaches 70 at 4 minutes.'), ('Her pulse falls by the same amount each minute.', 'It falls 30, then 20, then 20, then 10.')]))
add(1, '1.2', mcq('p6u01s2h01', 'O4', 'Five children jog for three minutes. Their breathing rate and pulse are then measured. What pattern do the results show?',
    'Children with a higher pulse also have a higher breathing rate.',
    [('The higher the pulse, the lower the breathing rate.', 'Both go up together.'), ('There is no pattern.', 'The two sets of numbers rise together.'), ('Everyone has the same pulse.', 'The pulses range from 90 to 130.')],
    data=[['Child', 'Breaths per minute', 'Pulse in beats per minute'], ['A', '28', '90'], ['B', '32', '100'], ['C', '36', '110'], ['D', '40', '120'], ['E', '44', '130']], skill='Data'))
add(1, '1.3', num('p6u01s3h01', 'O5', 'A scientist asks 100 girls at what age they noticed the first signs of puberty. How many girls were aged 12 or older?', 50, 'girls', ['girls'],
    '25 + 15 + 10 = 50 girls.', fig=bars(['9', '10', '11', '12', '13', '14'], [5, 15, 30, 25, 15, 10], 30, 5, 'Number of girls', 'Age in years')))
add(1, '1.4', mcq('p6u01s4h01', 'O7', 'A clinic counts malaria cases each month. Malaria is spread by mosquitoes. What is the best explanation for the pattern?',
    'In the wet season there is more standing water where mosquitoes breed, so more people are bitten.',
    [('Rain water contains the malaria parasite.', 'The parasite is passed on by mosquito bites.'), ('People catch malaria from each other when they shelter from rain.', 'Malaria does not pass directly from person to person.'), ('Mosquitoes only live in dry places.', 'Their young grow in water.')],
    data=[['Months', 'Season', 'Malaria cases'], ['January to March', 'wet', '210'], ['April to June', 'dry', '60'], ['July to September', 'dry', '45'], ['October to December', 'wet', '190']], skill='Data'))

add(2, '2.1', mcq('p6u02s1h01', 'O1', '100 ml of each liquid is heated in the same way, starting at 20 °C. Which liquid starts to boil first?', 'liquid A',
    [('liquid B', 'B must reach 100 °C; A boils at only 78 °C.'), ('liquid C', 'C has the highest boiling point, so it boils last.'), ('They all boil at the same time.', 'They have different boiling points.')],
    'The liquid with the lowest boiling point reaches it first.',
    data=[['Liquid', 'Boiling point'], ['A', '78 °C'], ['B', '100 °C'], ['C', '180 °C']], skill='Data'))
add(2, '2.2', mcq('p6u02s2h01', 'O3', 'Two identical ice cubes are put in a warm room, one on a metal plate and one on a plastic plate. Which melts first, and why?',
    'The one on metal: metal is a good thermal conductor, so it carries heat from the room into the ice quickly.',
    [('The one on plastic: plastic is warmer.', 'Both plates are at room temperature.'), ('The one on metal: metal makes heat.', 'Metal does not make heat; it conducts it.'), ('They melt at the same time.', 'The plates conduct heat at different rates.')]))
add(2, '2.3', graph('p6u02s3h01', 'O6', 'A spoonful of sugar is stirred into water at different temperatures. The time to dissolve is measured. Plot the results.', ax('Water temperature (°C)', 20, 80, 20), ax('Time to dissolve (s)', 0, 80, 10),
    [[20, 80], [40, 40], [60, 20], [80, 10]],
    'Use the pattern to choose the best prediction for water at 50 °C.', 'about 30 s',
    [('about 80 s', 'That is the time for 20 °C.'), ('about 5 s', 'Even at 80 °C it takes 10 s.'), ('about 60 s', '50 °C is between 40 °C (40 s) and 60 °C (20 s).')]))
add(2, '2.4', mcq('p6u02s4h01', 'O7', 'Plants make food by a chemical reaction. Which line shows the reactants and the products correctly?',
    'reactants: carbon dioxide and water; products: glucose and oxygen',
    [('reactants: glucose and oxygen; products: carbon dioxide and water', 'This is the wrong way round.'), ('reactants: sunlight and soil; products: leaves', 'Light is the energy source, not a substance that reacts.'), ('reactants: oxygen and water; products: carbon dioxide', 'Plants take in carbon dioxide and give out oxygen.')]))

add(3, '3.1', mcq('p6u03s1h01', 'O2', 'On a volcanic island, the beach is covered in smooth black stones with crystals too small to see. What is their history?',
    'Lava cooled quickly to form igneous rock with tiny crystals; then the sea wore the pieces smooth.',
    [('Sand was pressed together under the sea.', 'That makes sedimentary rock with grains and layers.'), ('The stones cooled slowly deep underground.', 'Slow cooling makes large crystals.'), ('The stones are fossils.', 'Fossils are the remains of living things.')]))
add(3, '3.2', mcq('p6u03s2h01', 'O3', 'Miners find fossil bones of animals that no longer live in the area. In which type of rock are fossils usually found, and why?',
    'Sedimentary rock: the dead animals were buried by layers of sediment that slowly turned to rock.',
    [('Igneous rock: lava protects the bones.', 'Hot lava destroys remains.'), ('Metamorphic rock: heat and pressure make fossils.', 'Heat and pressure usually destroy fossils.'), ('Any rock: fossils grow inside rocks.', 'Fossils form only when remains are buried in sediment.')]))
add(3, '3.3', order('p6u03s3h01', 'O5', 'A piece of granite goes once round the rock cycle and ends as granite again. Put the stages in order.',
    ['granite is broken into small pieces by weathering', 'rivers carry the pieces to the sea, where they settle in layers', 'the layers are buried and pressed into sedimentary rock', 'heat and pressure change it into metamorphic rock', 'the rock melts to form magma', 'the magma cools slowly underground to form granite']))
add(3, '3.4', mcq('p6u03s4h01', 'O7', 'An organic farmer grows beans in a field one year, maize the next and carrots the year after. Why does this help the soil?',
    'Different crops take different nutrients, so the soil is not emptied of one kind, and pests of one crop do not build up.',
    [('It makes the soil deeper.', 'Changing crops does not add depth.'), ('Crops grow without any nutrients after rotation.', 'All crops need nutrients.'), ('It stops rain from falling on the field.', 'Rotation does not change the weather.')]))

add(4, '4.1', mcq('p6u04s1h01', 'O2', 'In a desert, beetles eat seeds blown in by the wind, lizards eat beetles and hawks eat lizards. A dry year means very few seeds arrive. What happens next?',
    'Beetle numbers fall, then lizards and hawks have less food, so their numbers fall too.',
    [('Lizard numbers rise because there are fewer beetles.', 'Lizards eat beetles, so they have less food.'), ('Only the hawks are affected.', 'Every link above the seeds is affected.'), ('Nothing changes, because animals do not need plants.', 'All the energy in the chain starts with plants.')]))
add(4, '4.2', mcq('p6u04s2h01', 'O5', 'A pesticide that does not break down is sprayed on a lake to kill insects. Years later, fish-eating birds lay eggs with thin shells that break. Why are the birds harmed more than the insects\' other predators lower down?',
    'The pesticide builds up at each step of the food chain, so the top predators have the most in their bodies.',
    [('The birds drink the most water.', 'The pesticide comes mainly from the food they eat.'), ('The pesticide was sprayed on the birds.', 'It was sprayed on the lake.'), ('Birds are the smallest animals in the chain.', 'They are the top predators.')]))

add(5, '5.1', num('p6u05s1h01', 'O2', 'An astronaut has a mass of 90 kg. On a planet where gravity pulls with 5 N on every kilogram, what is his weight?', 450, 'N', ['N', 'kg'],
    'Weight = mass × gravity = 90 × 5 = 450 N. His mass is still 90 kg.'))
add(5, '5.2', mcq('p6u05s2h01', 'O3', 'You roll a tennis ball across a smooth floor and then across a strip of sandpaper. What effect of a force does the sandpaper show?',
    'Friction slows the ball down.',
    [('Friction speeds the ball up.', 'Friction acts against the movement.'), ('Gravity changes the ball\'s shape.', 'The ball keeps its shape.'), ('The sandpaper removes gravity.', 'Gravity still acts on the ball.')]))
add(5, '5.3', mcq('p6u05s3h01', 'O5', 'A submarine has tanks that can be filled with sea water or with air. What should the crew do to make it sink, and why does this work?',
    'Fill the tanks with water: the submarine becomes heavier for the same size, so its weight is greater than the upthrust.',
    [('Fill the tanks with air to make it heavier.', 'Air is much lighter than water.'), ('Empty the tanks so the upthrust disappears.', 'Upthrust always acts on an object in water.'), ('Switch off gravity.', 'Gravity cannot be switched off.')]))
add(5, '5.4', mcq('p6u05s4h01', 'O6', 'Three lamps are connected to a cell, each on its own branch (a parallel circuit). One lamp is unscrewed. What happens to the other two?',
    'They stay on, because each has its own complete path to the cell.',
    [('They go out, because the circuit is broken.', 'That happens in a series circuit.'), ('They get much dimmer.', 'Each branch still has the full push of the cell.'), ('They flash on and off.', 'Nothing in the circuit is switching.')]))

add(6, '6.1',
  mcq('p6u06s1h01', 'O2', 'A periscope lets you see over a wall. How does it work?',
      'Two mirrors, each at 45°, reflect the light twice so it reaches your eye.',
      [('Lenses bend the light around the wall.', 'A simple periscope uses flat mirrors.'), ('One mirror reflects the light straight back.', 'One mirror would send the light back out.'), ('The tube makes its own light.', 'The light comes from the object.')]),
  num('p6u06s1h02', 'O1', 'A ray of light hits a flat mirror at an angle of incidence of 45°. Through what total angle is the ray turned?', 90, '°', ['°'],
      'The angle of reflection is also 45°, so the ray turns through 45 + 45 = 90°.'))
add(6, '6.2', mcq('p6u06s2h01', 'O4', 'A straw standing in a glass of water looks bent at the surface. Why?',
    'Light from the straw changes direction when it passes from water into air (refraction).',
    [('The water bends the straw.', 'The straw is straight when you take it out.'), ('Light is reflected by the straw.', 'Reflection lets us see the straw, but does not make it look bent.'), ('The glass makes a shadow.', 'A shadow would not shift the image of the straw.')]))
add(6, '6.3',
  num('p6u06s3h01', 'O6', 'Use the table. About how many Earth years does Jupiter take to orbit the Sun once? Give your answer to the nearest whole number.', 12, 'years', ['years', 'days'],
      '4333 ÷ 365 = 11.9, which is 12 years to the nearest whole number.', tol=0.2,
      data=[['Planet', 'Distance from the Sun (million km)', 'Time for one orbit (Earth days)'], ['Earth', '150', '365'], ['Mars', '228', '687'], ['Jupiter', '778', '4333']]),
  mcq('p6u06s3h02', 'O5', 'Use the same table of planets. What pattern does it show?', 'The further a planet is from the Sun, the longer it takes to orbit.',
      [('The further a planet is from the Sun, the shorter its orbit time.', 'The times get longer.'), ('All planets take the same time.', 'The times range from 365 to 4333 days.'), ('Bigger planets are always closer to the Sun.', 'Jupiter is the biggest and the furthest of the three.')],
      data=[['Planet', 'Distance from the Sun (million km)', 'Time for one orbit (Earth days)'], ['Earth', '150', '365'], ['Mars', '228', '687'], ['Jupiter', '778', '4333']], skill='Data'))
apply(6, B)
