"""Stage 7 Science — extra Hard (* Advanced) questions written by Camday (original contexts, numbers and wording).
Edits content/src/stage7-unitNN.json in place; safe to run again. Then: node tools/build-content.mjs"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hardkit import *

B = {}
def add(u, sec, *qs): B.setdefault((u, sec), []).extend(qs)
F7 = 'First … This causes … As a result …'

# ---------------- Unit 4 Classifying Living Things ----------------
add(4, '4.1', mcq('s7u04s1h01', 'O1', 'A dry bean seed has been in a paper packet for a year. It does not move, feed or grow. Which statement is correct?',
    'It is alive but dormant: when it gets water and warmth it will respire faster, grow and show the other characteristics.',
    [('It is not alive, because living things show all seven characteristics all the time.', 'Living things do not have to show every characteristic at every moment.'),
     ('It is not alive, because seeds are only made of stored food.', 'A seed contains a living embryo plant as well as a food store.'),
     ('It is alive only after it has been planted.', 'Planting does not create life; the embryo is already alive.')]))
add(4, '4.2', mcq('s7u04s2h01', 'O2', 'You are researching how viruses were discovered. Which source should you trust most, and why?',
    'A university or science museum website, because it is written and checked by experts and names its sources.',
    [('An anonymous blog, because it is written in simple words.', 'Easy to read does not mean accurate; you cannot check who wrote it.'),
     ('A video with millions of views, because many people have seen it.', 'Popularity is not evidence of accuracy.'),
     ('An advert for a medicine, because companies know about viruses.', 'An advert is trying to sell something, so it may be biased.')]))
add(4, '4.3', mcq('s7u04s3h01', 'O3', 'Scientists find tiny brown frogs on two islands. The frogs look the same. What is the best evidence that they belong to the same species?',
    'Frogs from the two islands can breed together and their offspring are fertile.',
    [('They are the same colour and size.', 'Different species can look alike.'),
     ('They eat the same insects.', 'Many different species share the same food.'),
     ('They live in the same type of habitat.', 'Many different species share a habitat.')]))
add(4, '4.5', mcq('s7u04s5h01', 'O6', 'Use the key. A small animal has six legs and no wings. What is it?', 'ant',
    [('spider', 'Follow 1a to 2: a spider has eight legs.'), ('fly', 'Follow 2a to 3: a fly has wings.'), ('worm', 'A worm has no legs.')],
    data=[['Step', 'Feature', 'Result'], ['1a', 'has legs', 'go to 2'], ['1b', 'has no legs', 'worm'], ['2a', 'has six legs', 'go to 3'], ['2b', 'has eight legs', 'spider'], ['3a', 'has wings', 'fly'], ['3b', 'has no wings', 'ant']], skill='Data'))

# ---------------- Unit 5 Food Chains and Food Webs ----------------
add(5, '5.1',
  graph('s7u05s1h01', 'O2', 'Pieces of damp bread are kept at different temperatures for five days. The area covered by mould is measured. Plot the results.', ax('Temperature (°C)', 5, 45, 10), ax('Bread covered by mould (%)', 0, 40, 10),
        [[5, 0], [15, 10], [25, 30], [35, 40], [45, 10]],
        'Which conclusion do the results support?', 'Mould grows fastest at about 35 °C; it grows slowly when it is cold and when it is too hot.',
        [('The hotter it is, the faster mould grows.', 'At 45 °C the growth falls to 10%.'), ('Mould cannot grow below 25 °C.', 'There is 10% cover at 15 °C.'), ('Temperature has no effect on mould.', 'The cover changes from 0% to 40%.')]),
  para('s7u05s1h02', 'O2', 'Plan an investigation to find out whether bread goes mouldy faster when it is damp or when it is dry.',
       [('Change only the dampness: some bread damp, some dry', 'damp|dry|water'),
        ('Measure the mould, e.g. days until it appears or the area covered', 'area|days|measure|cover'),
        ('Keep the type and size of bread, the temperature and the time the same', 'same'),
        ('Use several pieces for each condition (repeats)', 'repeat|several|three|five'),
        ('Work safely: keep the bags sealed and do not open them', 'seal|closed|do not open|safely')], 4,
       'I will take ten pieces of the same bread, all cut to the same size. I will add the same small volume of water to five pieces and leave the other five dry. Each piece will go in its own sealed bag, and all the bags will be kept at the same temperature. Every day I will measure the area of each piece that is covered by mould without opening the bags. Using five pieces for each condition lets me check that the results are reliable.', frame=PLAN))
add(5, '5.2',
  mcq('s7u05s2h01', 'O3', 'Use the feeding information. A disease kills most of the lizards. What is most likely to happen first?',
      'The number of locusts rises, because fewer are eaten.',
      [('The number of locusts falls, because they have less food.', 'Locusts eat grass, not lizards.'), ('The amount of grass rises.', 'More locusts would eat more grass.'), ('The number of hawks rises.', 'Hawks lose one of their foods.')],
      data=[['Animal', 'What it eats'], ['locust', 'grass'], ['mouse', 'grass seeds'], ['lizard', 'locusts'], ['snake', 'mice and lizards'], ['hawk', 'snakes and lizards']], skill='Data'),
  mcq('s7u05s2h02', 'O4', 'Why would a food web soon stop working if there were no decomposers?',
      'Minerals would stay locked in dead bodies and waste, so producers would run out of the minerals they need to grow.',
      [('Producers would have no light.', 'Decomposers do not provide light.'), ('Predators would have nothing to hunt.', 'Predators hunt other consumers, not decomposers.'), ('There would be too much oxygen.', 'The problem is the supply of minerals.')]))

# ---------------- Unit 6 Materials and Their Structure ----------------
add(6, '6.1', mcq('s7u06s1h01', 'O1', 'Dry sand can be poured and takes the shape of its container. Why is sand still classified as a solid?',
    'Each grain keeps its own fixed shape and volume; the sand flows only because the grains are small and separate.',
    [('Sand is really a liquid at room temperature.', 'Each grain is a hard solid.'), ('The particles inside each grain slide past each other.', 'In a solid the particles only vibrate about fixed positions.'), ('Sand can be squashed into a much smaller volume, like a gas.', 'Only the air gaps between the grains get smaller.')]))
add(6, '6.2',
  graph('s7u06s2h01', 'O3', 'Crushed ice is heated steadily and its temperature is recorded. Plot the results.', ax('Time (minutes)', 0, 14, 2), ax('Temperature (°C)', -20, 100, 20),
        [[0, -20], [2, 0], [6, 0], [10, 40], [14, 80]],
        'Why does the temperature stay at 0 °C between 2 and 6 minutes?', 'The energy is used to overcome the forces holding the particles in place, so the ice melts instead of getting hotter.',
        [('The heater was switched off.', 'The ice was heated steadily the whole time.'), ('Ice cannot take in energy.', 'It takes in energy all the time; that is why it melts.'), ('The thermometer stops working at 0 °C.', 'It works again as soon as the ice has melted.')]),
  para('s7u06s2h02', 'O3', 'On a cold morning, water droplets form on the inside of a kitchen window while a pan of water is boiling. Use the particle model to explain how the droplets form.',
       [('Water particles leave the pan as a gas (steam / water vapour)', 'gas|steam|vapour'),
        ('Gas particles move fast and are far apart', 'fast|far apart|quickly'),
        ('At the cold window the particles lose energy and slow down', 'lose energy|slow|cool'),
        ('The particles move closer together and forces of attraction hold them', 'closer|attract|together'),
        ('This change of state is condensation, forming a liquid', 'condens|liquid')], 4,
       'First, particles of water leave the boiling pan as a gas called water vapour. In a gas the particles move fast and are far apart. When they hit the cold window they lose energy and slow down. This causes the particles to move closer together, and the forces of attraction hold them near each other. As a result the gas condenses into droplets of liquid water on the glass.', frame=F7, words=35))
add(6, '6.5',
  num('s7u06s5h01', 'O6', 'The formula of glucose is C₆H₁₂O₆. How many hydrogen atoms are there in 3C₆H₁₂O₆ (three molecules)?', 36, 'atoms', ['atoms'], 'Each molecule has 12 hydrogen atoms: 3 × 12 = 36.'),
  mcq('s7u06s5h02', 'O6', 'A student writes the formula of sodium carbonate as NA2Co3. Which is the correct way to write it, and why?',
      'Na₂CO₃ — a symbol has one capital letter followed by a small letter if needed; Co would mean cobalt.',
      [('NA₂CO₃ — every letter in a symbol is a capital.', 'NA is not a symbol; sodium is Na.'), ('na₂co₃ — symbols use small letters.', 'Every symbol starts with a capital letter.'), ('Na₂Co₃ — carbon and oxygen join to make Co.', 'Co is the symbol for the metal cobalt.')]))
add(6, '6.6', mcq('s7u06s6h01', 'O7', 'Iron filings are mixed with yellow sulfur powder. Some of the mixture is then heated until it glows and forms a black solid, iron sulfide. Which statement is correct?',
    'A magnet removes the iron from the mixture but not from iron sulfide, because in the compound the atoms are chemically joined.',
    [('A magnet removes the iron from both.', 'Iron sulfide is a new substance with different properties.'), ('Both are mixtures, because both contain iron and sulfur.', 'Heating made a compound.'), ('Iron sulfide is yellow and grey like the mixture.', 'The compound is a black solid with its own properties.')]))

# ---------------- Unit 7 Properties of Materials ----------------
add(7, '7.3', mcq('s7u07s3h01', 'O3', 'Use the data. Which substance is a metal that is a liquid at 20 °C?', 'A',
    [('B', 'B melts at 114 °C, so it is a solid at 20 °C, and it does not conduct.'), ('C', 'C melts at 1538 °C, so it is a solid at 20 °C.'), ('D', 'D is a liquid at 20 °C but does not conduct, so it is a non-metal.')],
    'A liquid at 20 °C has a melting point below 20 °C and a boiling point above it. A metal conducts electricity.',
    data=[['Substance', 'Melting point in °C', 'Boiling point in °C', 'Conducts electricity?', 'Appearance'], ['A', '−39', '357', 'yes', 'shiny'], ['B', '114', '184', 'no', 'dull'], ['C', '1538', '2862', 'yes', 'shiny'], ['D', '−7', '59', 'no', 'dull']], skill='Data'))
add(7, '7.4', num('s7u07s4h01', 'O4', 'Brass is an alloy of copper and zinc. The bar chart shows the force needed to break wires of the same size. How much more force does the brass wire need than the copper wire?', 140, 'N', ['N', 'kg'],
    'Brass 350 N, copper 210 N: 350 − 210 = 140 N. The alloy is stronger than either pure metal.',
    fig=bars(['zinc', 'copper', 'brass'], [110, 210, 350], 400, 50, 'Force needed to break the wire in N')))

# ---------------- Unit 8 Acids and Alkalis ----------------
add(8, '8.3', mcq('s7u08s3h01', 'O3', 'A liquid turns methyl orange yellow and leaves phenolphthalein colourless. Use the table. What can you say about its pH?',
    'It is between pH 4 and pH 9.',
    [('It is below pH 4.', 'Below pH 4 methyl orange would be red.'), ('It is above pH 9.', 'Above pH 9 phenolphthalein would be pink.'), ('It is exactly pH 7.', 'These two indicators only narrow it to a range; universal indicator is needed.')],
    data=[['Indicator', 'Colour change'], ['methyl orange', 'red below pH 4, yellow above pH 4'], ['phenolphthalein', 'colourless below pH 9, pink above pH 9']], skill='Data'))
add(8, '8.4',
  graph('s7u08s4h01', 'O4', 'An indigestion powder is added, 1 g at a time, to 25 cm³ of acid. The pH is measured each time. Plot the results.', ax('Mass of powder added (g)', 0, 4, 1), ax('pH', 0, 8, 1),
        [[0, 2], [1, 3], [2, 5], [3, 7], [4, 7]],
        'What mass of powder is needed to neutralise the acid?', '3 g',
        [('1 g', 'At 1 g the pH is 3, still acidic.'), ('2 g', 'At 2 g the pH is 5, still acidic.'), ('4 g', 'The acid is already neutral at 3 g; the extra gram is not needed.')]),
  mcq('s7u08s4h02', 'O4', 'Three indigestion powders are tested in the same way. Which is the best choice, and why?',
      'A: it reaches pH 7 with the smallest mass and does not make the mixture alkaline.',
      [('B: it needs the most powder.', 'Needing more powder means it is less effective.'), ('C: it gives the highest pH.', 'pH 10 is alkaline, which could also be harmful.'), ('All three are equally good.', 'They need different masses and end at different pH values.')],
      data=[['Powder', 'Mass needed to reach pH 7', 'pH after adding 4 g'], ['A', '2 g', '7'], ['B', '4 g', '7'], ['C', '2 g', '10']], skill='Data'))

# ---------------- Unit 9 Chemical Reactions ----------------
add(9, '9.2', graph('s7u09s2h01', 'O2', 'Different masses of magnesium are added to 20 cm³ of the same acid. The volume of hydrogen made is measured. Plot the results.', ax('Mass of magnesium (g)', 0, 0.5, 0.1), ax('Volume of hydrogen (cm³)', 0, 500, 100),
    [[0.1, 100], [0.2, 200], [0.3, 300], [0.4, 400], [0.5, 400]],
    'Why is the volume the same for 0.4 g and 0.5 g?', 'All the acid has reacted, so the extra magnesium has nothing to react with.',
    [('The magnesium stopped being a metal.', 'It is still magnesium; some is left over.'), ('The measuring cylinder was full.', 'Nothing in the data suggests this; the pattern is caused by the acid running out.'), ('Hydrogen stops forming above 300 cm³.', '400 cm³ was collected.')]))
add(9, '9.4', para('s7u09s4h01', 'O4', 'Four unlabelled test tubes contain air, oxygen, hydrogen and carbon dioxide. Describe the tests you would do to find out which is which, and the result for each gas.',
    [('Oxygen relights a glowing splint', 'glowing|relight'),
     ('Hydrogen burns with a squeaky pop with a lighted splint', 'pop'),
     ('Carbon dioxide turns limewater cloudy (or puts out a lighted splint)', 'limewater|cloudy|milky|goes out|puts out'),
     ('In air a lighted splint keeps burning normally / a glowing splint does not relight', 'air'),
     ('Safety: eye protection or small volumes', 'safety|goggles|eye')], 4,
    'First I would put on safety goggles. I would put a glowing splint into each tube, and the tube where it relights contains oxygen. Next I would hold a lighted splint at the mouth of the other tubes, and the one that burns with a squeaky pop is hydrogen. The gas that puts out the lighted splint and turns limewater cloudy is carbon dioxide. In the tube of air the lighted splint just keeps burning normally.', frame='First I would … The tube where … Next … The last tube …'))

# ---------------- Unit 10 Forces ----------------
add(10, '10.2',
  mcq('s7u10s2h01', 'O2', 'Four people stand at the North Pole, the South Pole and two places on the Equator. In which direction does gravity pull each of them?',
      'Towards the centre of the Earth, so “down” is a different direction for each person.',
      [('Towards the South Pole, because that is the bottom of the Earth.', 'There is no bottom; gravity acts towards the centre.'), ('In the same direction for all four people.', 'Each is pulled towards the centre from a different side.'), ('Away from the Earth at the Equator.', 'Gravity always attracts.')]),
  mcq('s7u10s2h02', 'O2', 'Which statement correctly compares the force of gravity with the force between two magnets?',
      'Both act without contact and get weaker with distance, but gravity only attracts while magnets can attract or repel.',
      [('Both can attract and repel.', 'Gravity never repels.'), ('Gravity needs contact but magnetic force does not.', 'Both act at a distance.'), ('Both act only on iron and steel.', 'Gravity acts on every object that has mass.')]))
add(10, '10.3', num('s7u10s3h01', 'O3', 'An astronaut has a mass of 60 kg. Gravity is 10 N/kg on Earth and 1.6 N/kg on the Moon. How much less does she weigh on the Moon than on Earth?', 504, 'N', ['N', 'kg', 'N/kg'],
    'Earth: 60 × 10 = 600 N. Moon: 60 × 1.6 = 96 N. Difference = 504 N. Her mass stays 60 kg.'))
add(10, '10.4', mcq('s7u10s4h01', 'O4', 'A space capsule returning to Earth slows from 7800 m/s to 100 m/s before its parachutes open, and its heat shield glows. What causes this?',
    'Air resistance from the atmosphere acts against its motion, and its kinetic energy is transferred to thermal energy.',
    [('Gravity pushes it upwards as it gets close to the Earth.', 'Gravity pulls it down and would speed it up.'), ('It runs out of fuel.', 'It is not using engines to keep moving; a force must slow it.'), ('There is no force; objects slow down by themselves.', 'A change of speed always needs an unbalanced force.')]))

# ---------------- Unit 11 Energy ----------------
add(11, '11.1', mcq('s7u11s1h01', 'O1', 'Careful measurements show that the water at the bottom of a high waterfall is slightly warmer than at the top. What is the best explanation?',
    'Gravitational potential energy becomes kinetic energy as the water falls, and then thermal energy when it hits the bottom.',
    [('The Sun heats the bottom more than the top.', 'The pattern is found even in the shade.'), ('Falling water takes in thermal energy from the air.', 'The energy comes from the fall itself.'), ('Energy is created when water hits rock.', 'Energy cannot be created; it is transferred.')]))
add(11, '11.2', order('s7u11s2h01', 'O2', 'A toy has a spring inside. You push it down, let go, and it jumps up and lands. Put the main energy stores in order, starting when the toy is pushed down.',
    ['elastic energy in the squashed spring', 'kinetic energy as the toy leaves the table', 'gravitational potential energy at the top of the jump', 'kinetic energy as the toy falls', 'thermal energy and sound when it lands']))
add(11, '11.3',
  num('s7u11s3h01', 'O3', 'An electric motor is supplied with 800 J of energy. 280 J is wasted as thermal energy and sound. What percentage of the energy is transferred usefully?', 65, '%', ['%', 'J'],
      'Useful energy = 800 − 280 = 520 J. Percentage = 520 ÷ 800 × 100 = 65%.'),
  num('s7u11s3h02', 'O3', 'Each lamp is supplied with 100 J of energy. The bar chart shows how much is transferred as light. How many times more light does the LED lamp give than the filament lamp?', 8, 'times', ['times'],
      'LED 40 J, filament 5 J: 40 ÷ 5 = 8 times.', fig=bars(['filament lamp', 'fluorescent lamp', 'LED lamp'], [5, 20, 40], 50, 10, 'Light energy from 100 J supplied, in J')))
add(11, '11.4', num('s7u11s4h01', 'O4', 'A girl stands 170 m from a cliff and claps. The speed of sound in air is 340 m/s. How long is it before she hears the echo?', 1, 's', ['s', 'm', 'm/s'],
    'The sound travels to the cliff and back: 2 × 170 = 340 m. Time = distance ÷ speed = 340 ÷ 340 = 1 s.'))

# ---------------- Unit 12 Electricity ----------------
add(12, '12.1', mcq('s7u12s1h01', 'O1', 'Copper is an excellent conductor and glass is an excellent insulator. What is the best explanation?',
    'Copper has electrons that are free to move through the metal; in glass the electrons are held in place.',
    [('Copper has electrons but glass has none.', 'All atoms have electrons.'), ('Glass is too hard for electricity to pass.', 'Hardness is not the reason; hard metals conduct.'), ('Copper is shiny, and shiny materials conduct.', 'Shininess does not carry current; moving electrons do.')]))
add(12, '12.3', graph('s7u12s3h01', 'O3', 'Cells are added one at a time to a series circuit with one lamp. The current is measured. Plot the results.', ax('Number of cells', 0, 4, 1), ax('Current (A)', 0, 1, 0.2),
    [[1, 0.2], [2, 0.4], [3, 0.6], [4, 0.8]],
    'Predict the current with 5 cells, if the lamp does not break.', '1.0 A',
    [('0.8 A', 'The current rises by 0.2 A for every extra cell.'), ('1.2 A', 'That would be the value for 6 cells.'), ('5.0 A', 'The current is 0.2 A per cell, not 1 A per cell.')]))
add(12, '12.4', mcq('s7u12s4h01', 'O4', 'Why does adding more cells in series make the current in a circuit larger?',
    'Together the cells give a bigger push to the electrons, so more charge flows past each point every second.',
    [('The extra cells add more electrons to the wires.', 'The electrons are already in the wires; cells push them round.'), ('The wires become shorter.', 'Adding cells does not shorten the wires.'), ('The lamp uses up less current.', 'Current is not used up; it is the same all round a series circuit.')]))

# ---------------- Unit 13 Earth Processes ----------------
add(13, '13.2',
  num('s7u13s2h01', 'O2', 'Each step of 1 on the earthquake magnitude scale means the shaking is 10 times bigger. How many times bigger is the shaking in a magnitude 7 earthquake than in a magnitude 4 earthquake?', 1000, 'times', ['times'],
      '7 − 4 = 3 steps: 10 × 10 × 10 = 1000 times.'),
  mcq('s7u13s2h02', 'O2', 'Which evidence best supports the idea that South America and Africa were once joined?',
      'Their coastlines fit together, and the same fossils and rock types are found on both sides of the ocean.',
      [('Both continents have mountains.', 'Every continent has mountains.'), ('Both are in the southern half of the world.', 'Position today does not show they were joined.'), ('Both have rivers that flow to the sea.', 'All continents do.')]))
add(13, '13.4', mcq('s7u13s4h01', 'O4', 'Precipitation can fall as rain, snow or hail. Which conditions give snow rather than rain?',
    'The air is below 0 °C all the way from the cloud to the ground, so the ice crystals do not melt.',
    [('The cloud is very high.', 'Height alone does not decide; the temperature of the air below matters.'), ('The wind is very strong.', 'Wind does not turn rain into snow.'), ('The air near the ground is warm.', 'Warm air melts the crystals into rain.')]))

# ---------------- Unit 14 Earth and Beyond ----------------
add(14, '14.1', mcq('s7u14s1h01', 'O1', 'No scientist has ever watched one star and its planets form from start to finish. How do scientists still know the stages?',
    'Formation takes millions of years, so they observe many different systems at different stages and put them in order.',
    [('They speed up time with telescopes.', 'Telescopes cannot change how fast things happen.'), ('They watched the Sun form.', 'The Sun formed about 4.6 billion years ago.'), ('It is only a guess with no evidence.', 'It is based on many observations and models.')]))
add(14, '14.2', mcq('s7u14s2h01', 'O2', 'Point A on the Earth is directly facing the Moon. What is the tide at A, and where else is the tide the same at that moment?',
    'High tide at A, and also on the opposite side of the Earth.',
    [('Low tide at A, and high tide on the opposite side.', 'The Moon pulls the water towards A.'), ('High tide at A only.', 'There are two bulges of water, on opposite sides.'), ('High tide everywhere on Earth.', 'Between the two bulges the tide is low.')]))
add(14, '14.3', mcq('s7u14s3h01', 'O3', 'Someone says: “I watched a lunar eclipse at midday.” Why can this not be true?',
    'In a lunar eclipse the Earth is between the Sun and the Moon, so the Moon is only above the night side of the Earth.',
    [('Lunar eclipses happen only in winter.', 'They can happen in any season.'), ('The Moon is never in the sky during the day.', 'The Moon is often visible by day, but not at full moon opposite the Sun.'), ('The Sun blocks the Moon at midday.', 'That describes a solar eclipse arrangement, and the Sun is far behind the Moon.')]))

apply(7, B)
