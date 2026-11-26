"""Stage 9 Science — extra Hard (* Advanced) questions written by Camday (original contexts, numbers and wording).
Edits content/src/stage9-unitNN.json in place; safe to run again. Then: node tools/build-content.mjs"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hardkit import *

B = {}
def add(u, sec, *qs): B.setdefault((u, sec), []).extend(qs)
CER = 'My claim is … The evidence is … This supports the claim because … However, a limitation is …'
def para9(*a, **k):   # Stage 9: 6–8 sentences
    k.setdefault('words', 60); q = para(*a, **k); q['sentences'] = [6, 8]; return q

# ---------------- Unit 1 Photosynthesis and Transport in Plants ----------------
add(1, '1.1',
  graph('s9u01s1h01', 'O2', 'A lamp is placed at different distances from pondweed in water. The bubbles of gas released in one minute are counted. Plot the results.', ax('Distance of lamp (cm)', 10, 50, 10), ax('Bubbles per minute', 0, 40, 10),
        [[10, 40], [20, 20], [30, 10], [40, 5], [50, 5]],
        'Which conclusion is best supported?', 'The closer the lamp, the higher the light intensity and the faster the rate of photosynthesis.',
        [('The closer the lamp, the slower photosynthesis is.', 'More bubbles means faster photosynthesis.'), ('Light has no effect on photosynthesis.', 'The rate changes from 40 to 5 bubbles per minute.'), ('The bubbles are carbon dioxide made by respiration.', 'In bright light the gas released is mostly oxygen from photosynthesis.')]),
  para9('s9u01s1h02', 'O2', 'Idea: carbon dioxide is a raw material for photosynthesis. Sodium hydrogencarbonate dissolves in water and adds carbon dioxide to it. Write a hypothesis and plan an investigation, using pondweed, to test this idea.',
        [('States a testable hypothesis linking carbon dioxide to the rate of photosynthesis', 'hypothesis|the more|faster|increase'),
         ('Changes the mass or concentration of sodium hydrogencarbonate', 'hydrogencarbonate|concentration|carbon dioxide'),
         ('Measures the rate, e.g. bubbles per minute or volume of oxygen', 'bubble|oxygen|volume'),
         ('Controls light intensity (lamp distance), temperature and the piece of pondweed', 'same'),
         ('Repeats and calculates a mean', 'repeat|mean|average'),
         ('Says what result would support the hypothesis', 'support')], 5,
        'My hypothesis is that the more carbon dioxide there is in the water, the faster the pondweed photosynthesises. I will change the mass of sodium hydrogencarbonate dissolved in the water, using 0 g, 1 g, 2 g and 3 g in the same volume. I will measure the rate by counting the bubbles of oxygen released in one minute. The lamp will stay at the same distance, and I will use the same piece of pondweed at the same temperature. I will repeat each count three times and calculate a mean. If the number of bubbles rises as the mass increases, the results support the hypothesis.',
        frame='My hypothesis is … I will change … I will measure … I will keep … the same. I will repeat … If … then …'))
add(1, '1.2',
  num('s9u01s2h01', 'O4', 'A potted plant has its soil covered with plastic so that water can leave only through the leaves. Its mass is 912 g on day 1 and 840 g on day 9. Calculate the mean loss of mass per day.', 9, 'g per day', ['g per day', 'g'],
      'Loss = 912 − 840 = 72 g over 8 days (day 1 to day 9). Mean = 72 ÷ 8 = 9 g per day.'),
  mcq('s9u01s2h02', 'O3', 'Three varieties of wheat are grown in the same dry field. A farmer in a region with little rain wants the best variety. Use the data to choose.',
      'Variety B: it gives nearly the same yield as A while using much less water.',
      [('Variety A: it takes up the most water.', 'In a dry region, needing more water is a disadvantage.'), ('Variety C: it uses the least water.', 'Its yield is much lower.'), ('It makes no difference.', 'The varieties differ in both water use and yield.')],
      data=[['Variety', 'Water taken up per plant in a season (dm³)', 'Grain yield (tonnes per hectare)'], ['A', '52', '4.1'], ['B', '36', '3.9'], ['C', '30', '2.2']], skill='Data'))

# ---------------- Unit 2 Excretion ----------------
add(2, '2.1', num('s9u02s1h01', 'O2', 'The concentration of urea is 0.4 g/dm³ in blood plasma and 20 g/dm³ in urine. How many times more concentrated is urea in urine than in blood plasma?', 50, 'times', ['times'],
    '20 ÷ 0.4 = 50 times. The kidneys filter urea out of the blood and reabsorb most of the water.'))

# ---------------- Unit 3 Variation and Inheritance ----------------
add(3, '3.1', mcq('s9u03s1h01', 'O1', 'Before a cell divides to make two new cells, all of its DNA is copied. Why is this important?',
    'Each new cell needs a complete set of genes, with all the instructions to work properly.',
    [('So that the new cells are twice as big.', 'Copying DNA does not control cell size.'), ('So that each new cell has half the genes.', 'Body cells need the full set; only gametes have half.'), ('Because DNA is used up as energy during division.', 'DNA is information, not an energy source.')]))
add(3, '3.2',
  mcq('s9u03s2h01', 'O3', 'Scientists recorded the mean birth mass of babies and how much the mothers smoked while pregnant. Which statement is the best conclusion?',
      'The more the mother smoked, the lower the mean birth mass; the large sample makes this pattern reliable, but other factors could also be involved.',
      [('Smoking has no effect on birth mass.', 'The mean falls by 250 g.'), ('Every baby of a smoker is lighter than every baby of a non-smoker.', 'These are means; individual babies vary.'), ('The data prove that smoking is the only cause of low birth mass.', 'A correlation alone does not rule out other causes.')],
      data=[['Cigarettes smoked per day', 'Number of mothers', 'Mean birth mass in g'], ['none', '41 200', '3200'], ['1 to 10', '6 800', '3080'], ['more than 10', '2 100', '2950']], skill='Data'),
  mcq('s9u03s2h02', 'O2', 'Which pair of adaptations is correctly explained?',
      'A sperm cell has a tail and many mitochondria to swim to the egg; an egg cell has a large food store for the first cell divisions.',
      [('A sperm cell has a food store; an egg cell has a tail.', 'These are the wrong way round.'), ('Both cells carry a full set of chromosomes.', 'Each carries half a set.'), ('An egg cell is small so that it can swim quickly.', 'Egg cells are large and cannot swim.')]))
add(3, '3.3', graph('s9u03s3h01', 'O4', 'A student opens 20 pea pods and counts the peas in each. Plot the number of pods for each number of peas.', ax('Number of peas in the pod', 3, 7, 1), ax('Number of pods', 0, 8, 2),
    [[3, 2], [4, 4], [5, 8], [6, 4], [7, 2]],
    'What does the shape of the results show?', 'Most pods have a middle number of peas, and few have very low or very high numbers.',
    [('All pods have the same number of peas.', 'The numbers range from 3 to 7.'), ('Pods with 7 peas are the most common.', 'Only 2 pods have 7 peas.'), ('There is no variation in this species.', 'The count varies from pod to pod.')]))
add(3, '3.4', para9('s9u03s4h01', 'O5', 'Arctic hares have thick white fur. Their ancestors, which lived in warmer places, had thinner brown fur. Use the theory of natural selection to explain how arctic hares came to have thick white fur.',
    [('There was variation in fur thickness and colour in the population', 'variation|varied|differen'),
     ('The variation is caused by genes / is inherited', 'gene|inherit'),
     ('In the cold, snowy habitat thicker, whiter fur gave better insulation and camouflage', 'insulat|camouflage|warm|predator'),
     ('These hares were more likely to survive', 'surviv'),
     ('They reproduced and passed the genes to their offspring', 'reproduc|offspring|pass'),
     ('Over many generations the whole population changed', 'generation')], 5,
    'In the ancestors of arctic hares there was variation in the thickness and colour of the fur. This variation was caused by differences in their genes. When hares lived in cold, snowy places, those with thicker and whiter fur were better insulated and better camouflaged from predators. These hares were more likely to survive the winter. They reproduced and passed the genes for thick white fur to their offspring. Over many generations, more and more of the population had thick white fur.',
    frame='There was variation in … This was caused by … In the cold … These hares … They passed … Over many generations …'))

# ---------------- Unit 4 The Periodic Table ----------------
add(4, '4.1', mcq('s9u04s1h01', 'O1', 'Moving from left to right along a period, and on to the start of the next period, how do the atomic number and the mass number change?',
    'The atomic number rises by exactly 1 each time; the mass number generally rises, but not by the same amount each time.',
    [('Both rise by exactly 1 each time.', 'Mass numbers increase by different amounts because the number of neutrons varies.'), ('The atomic number goes back to 1 at the start of each period.', 'It keeps increasing.'), ('The mass number stays the same along a period.', 'It generally increases.')]))
add(4, '4.2',
  mcq('s9u04s2h01', 'O4', 'Use the data for Group 1. Rubidium is the next element below potassium. Predict its melting point.', 'about 39 °C',
      [('about 180 °C', 'Melting points fall going down the group.'), ('about 98 °C', 'That is the value for sodium.'), ('about −60 °C', 'The fall from sodium to potassium is 35 °C, so a fall of over 120 °C is too big.')],
      data=[['Element', 'Camday number', 'Melting point in °C'], ['lithium', '3', '180'], ['sodium', '11', '98'], ['potassium', '19', '63']], skill='Data'),
  mcq('s9u04s2h02', 'O3', 'Going down Group 7, the boiling points are: fluorine −188 °C, chlorine −34 °C, bromine 59 °C. Iodine is next. What state is iodine at 20 °C, and why?',
      'Solid: boiling and melting points rise down the group, so iodine melts well above 20 °C.',
      [('Gas: all Group 7 elements are gases.', 'Bromine is a liquid at 20 °C.'), ('Liquid: it must be the same as bromine.', 'The trend continues upwards.'), ('It cannot be predicted from a trend.', 'Trends in groups are used to make predictions.')]))

# ---------------- Unit 5 Chemical Bonding ----------------
add(5, '5.3',
  mcq('s9u05s3h01', 'O3', 'Magnesium (2,8,2) reacts with chlorine (2,8,7) to form magnesium chloride, MgCl₂. What happens to the electrons?',
      'One magnesium atom loses two electrons; two chlorine atoms each gain one, forming Mg²⁺ and two Cl⁻ ions.',
      [('Magnesium and chlorine share two pairs of electrons.', 'Sharing is covalent bonding; a metal and a non-metal form ions.'), ('One chlorine atom gives two electrons to magnesium.', 'The metal loses electrons; the non-metal gains them.'), ('Magnesium gains two electrons from one chlorine atom.', 'Magnesium loses its two outer electrons.')]),
  num('s9u05s3h02', 'O3', 'Calcium has atomic number 20. How many electrons are there in a calcium ion, Ca²⁺?', 18, 'electrons', ['electrons'], 'A calcium atom has 20 electrons. It loses 2 to form Ca²⁺: 20 − 2 = 18.'))
add(5, '5.4', para9('s9u05s4h01', 'O4', 'Diamond and graphite are both made only of carbon atoms. Diamond is very hard and does not conduct electricity. Graphite is soft and conducts electricity. Explain these differences using ideas about structure and bonding.',
    [('Both are giant structures with strong covalent bonds', 'giant|covalent'),
     ('In diamond each carbon atom is bonded to four others', 'four'),
     ('This rigid structure makes diamond hard', 'rigid|hard'),
     ('In graphite each carbon atom is bonded to three others, in layers', 'three|layer'),
     ('Weak forces between layers let them slide, so graphite is soft', 'slide|weak'),
     ('Graphite has free electrons that can move and carry charge; diamond has none', 'free electron|delocalised|electrons (that )?(can )?move')], 5,
    'Diamond and graphite are both giant structures in which carbon atoms are joined by strong covalent bonds. In diamond, each carbon atom is bonded to four others. This makes a rigid structure in every direction, so diamond is very hard. In graphite, each carbon atom is bonded to only three others, forming flat layers. There are only weak forces between the layers, so they slide over each other and graphite is soft. Each carbon atom in graphite has one free electron that can move, so graphite conducts electricity, but diamond has no free electrons.',
    frame='Both are … In diamond … so … In graphite … so … Graphite conducts because …'))

# ---------------- Unit 6 Displacement Reactions ----------------
add(6, '6.2',
  mcq('s9u06s2h01', 'O3', 'Pieces of four metals are added to solutions of the salts of the other metals. Use the results to put the metals in order, most reactive first.', 'W, Z, Y, X',
      [('X, Y, Z, W', 'This is least reactive first.'), ('W, Y, Z, X', 'Z displaces Y, so Z is more reactive than Y.'), ('Z, W, Y, X', 'W displaces Z, so W is more reactive.')],
      'A metal displaces any metal below it from a salt solution. W displaces three, Z two, Y one and X none.',
      data=[['Metal added', 'Displaces the metal from the salts of …'], ['W', 'X, Y and Z'], ['X', 'none'], ['Y', 'X only'], ['Z', 'X and Y']], skill='Data'),
  mcq('s9u06s2h02', 'O2', 'Iron is extracted by heating iron oxide with carbon. Why can aluminium not be extracted from aluminium oxide in this way?',
      'Aluminium is more reactive than carbon, so carbon cannot displace it from its oxide.',
      [('Aluminium oxide does not contain aluminium.', 'It is a compound of aluminium and oxygen.'), ('Carbon is more reactive than aluminium.', 'Then the method would work.'), ('Aluminium oxide melts too easily.', 'It has a very high melting point; the reason is reactivity.')]),
  mcq('s9u06s2h03', 'O2', 'Railway workers join rails using a mixture of aluminium powder and iron oxide. When lit, it produces molten iron. Why does this work?',
      'Aluminium is more reactive than iron, so it displaces iron from iron oxide in a very exothermic reaction.',
      [('Iron is more reactive than aluminium.', 'Then no reaction would happen.'), ('The reaction is endothermic, so it melts the iron.', 'Melting the iron needs energy to be released.'), ('Aluminium melts and becomes iron.', 'Elements do not change into other elements in chemical reactions.')]))

# ---------------- Unit 7 Salts ----------------
add(7, '7.1', mcq('s9u07s1h01', 'O2', 'A green powder fizzes when dilute sulfuric acid is added. The gas turns limewater cloudy, and a blue solution is left. What is the powder?', 'copper carbonate',
    [('copper oxide', 'An oxide reacts with acid without fizzing.'), ('copper metal', 'Copper does not react with dilute sulfuric acid.'), ('sodium carbonate', 'It would fizz, but the solution would be colourless.')],
    'Fizzing with a gas that turns limewater cloudy means a carbonate; the blue solution shows a copper salt.'))
add(7, '7.2',
  order('s9u07s2h01', 'O3', 'Put the steps in order to make dry crystals of copper sulfate from copper oxide and dilute sulfuric acid.',
        ['warm the dilute sulfuric acid', 'add copper oxide and stir until no more reacts', 'filter to remove the excess copper oxide', 'heat the solution gently to evaporate some of the water', 'leave the solution to cool so that crystals form', 'pat the crystals dry with filter paper']),
  mcq('s9u07s2h02', 'O4', 'Why is copper chloride not made by adding copper metal to dilute hydrochloric acid?',
      'Copper is less reactive than hydrogen, so it does not react with dilute acids.',
      [('The reaction would be too violent.', 'There is no reaction.'), ('Copper chloride does not exist.', 'It does; it is made from copper oxide or copper carbonate.'), ('Copper reacts but makes copper sulfate instead.', 'There is no sulfate in hydrochloric acid, and copper does not react.')]))

# ---------------- Unit 8 Rate of Reaction ----------------
add(8, '8.2',
  graph('s9u08s2h01', 'O3', 'Magnesium ribbon reacts with excess dilute hydrochloric acid. The volume of hydrogen is measured every 30 s. Plot the results.', ax('Time (s)', 0, 120, 30), ax('Volume of hydrogen (cm³)', 0, 60, 10),
        [[0, 0], [30, 30], [60, 50], [90, 60], [120, 60]],
        'Why is the line flat after 90 s?', 'All the magnesium has reacted, so no more hydrogen is made.',
        [('The acid has become more concentrated.', 'The acid is used up as it reacts, not concentrated.'), ('The reaction is at its fastest.', 'A flat line means the rate is zero.'), ('The gas has dissolved back into the acid.', 'The volume stays constant; it does not fall.')]),
  num('s9u08s2h02', 'O2', 'In a reaction, 30 cm³ of gas is collected in the first 30 s and a further 20 cm³ in the next 30 s. How many times faster is the mean rate in the first 30 s than in the second 30 s?', 1.5, 'times', ['times'],
      'First: 30 ÷ 30 = 1.0 cm³/s. Second: 20 ÷ 30 = 0.67 cm³/s. 1.0 ÷ 0.67 = 1.5 times (or 30 ÷ 20).', tol=0.01))
add(8, '8.3',
  mcq('s9u08s3h01', 'O4', 'The same mass of zinc is used as lumps and then as powder with the same acid. How do the results compare, and why?',
      'The powder reacts faster because its larger surface area gives more frequent collisions, but the final volume of gas is the same.',
      [('The powder gives more gas in total.', 'The mass of zinc is the same, so the total gas is the same.'), ('The lumps react faster because they are heavier.', 'The mass is the same; lumps have less surface exposed.'), ('The powder reacts faster because its particles have more energy.', 'Energy depends on temperature, not on the size of the pieces.')]),
  para9('s9u08s3h02', 'O4', 'You have 20 g of marble chips and 50 cm³ of dilute hydrochloric acid. Plan how to collect 100 cm³ of carbon dioxide in the shortest possible time. Use collision theory to explain each decision.',
        [('Crush the marble to a powder to increase the surface area', 'surface area|powder|crush'),
         ('Warm the acid so particles move faster', 'warm|heat|temperature'),
         ('Higher temperature: more frequent and more energetic (successful) collisions', 'energy|successful|energetic'),
         ('Do not dilute the acid: more acid particles in the same volume', 'concentrat|dilute'),
         ('More frequent collisions give a faster rate', 'collision|collide'),
         ('Collect the gas in a gas syringe or measuring cylinder and time it', 'syringe|measuring cylinder|time')], 5,
        'First I would crush the marble chips into a powder to increase the surface area. This means more acid particles can collide with the marble every second. I would warm the acid, because at a higher temperature the particles move faster. They collide more often and with more energy, so more collisions are successful. I would not dilute the acid, because a concentrated acid has more particles in the same volume. I would collect the gas in a gas syringe and time how long it takes to reach 100 cm³.',
        frame='First I would … because … I would also … so that … I would collect …'))

# ---------------- Unit 9 Density ----------------
add(9, '9.1', num('s9u09s1h01', 'O2', 'A stone has a mass of 135 g. When it is lowered into a measuring cylinder, the water level rises from 50 cm³ to 100 cm³. Calculate the density of the stone.', 2.7, 'g/cm³', ['g/cm³', 'g', 'cm³'],
    'Volume = 100 − 50 = 50 cm³. Density = mass ÷ volume = 135 ÷ 50 = 2.7 g/cm³.'))
add(9, '9.3', mcq('s9u09s3h01', 'O4', 'Small pieces of four plastics are dropped into water (density 1.00 g/cm³) and into oil (density 0.90 g/cm³). Which plastic floats on water but sinks in oil?', 'A',
    [('B', 'B is denser than water, so it sinks in both.'), ('C', 'C is denser than water, so it sinks in both.'), ('D', 'D is less dense than oil, so it floats on both.')],
    'It must be less dense than water but denser than oil: between 0.90 and 1.00 g/cm³.',
    data=[['Plastic', 'Density in g/cm³'], ['A', '0.92'], ['B', '1.05'], ['C', '1.38'], ['D', '0.89']], skill='Data'))

# ---------------- Unit 10 Transfer of Thermal Energy ----------------
add(10, '10.2', num('s9u10s2h01', 'O2', 'A lamp takes in 600 J of electrical energy and wastes 510 J as thermal energy. What percentage of the energy is transferred as useful light?', 15, '%', ['%', 'J'],
    'Useful energy = 600 − 510 = 90 J. Percentage = 90 ÷ 600 × 100 = 15%.'))
add(10, '10.4',
  mcq('s9u10s4h01', 'O4', 'Your body is at 37 °C. Why do you feel cold in air at 5 °C but hot in air at 40 °C?',
      'Thermal energy transfers from hotter to colder: from your body to the air at 5 °C, and from the air to your body at 40 °C.',
      [('Cold flows from the air into your body at 5 °C.', 'Cold is not a thing that flows; thermal energy leaves your body.'), ('Your body stops making thermal energy at 40 °C.', 'It still releases energy from respiration.'), ('Air at 40 °C contains no thermal energy.', 'It contains more than air at 5 °C.')]),
  mcq('s9u10s4h02', 'O4', 'A cooking pot is made of steel with a wooden handle. Which explanation is correct?',
      'Steel is a good conductor, so energy reaches the food quickly; wood is an insulator, so the handle stays cool.',
      [('Wood conducts thermal energy away from your hand.', 'Wood is a poor conductor.'), ('Steel is an insulator that keeps the heat in.', 'Metals are good conductors.'), ('The handle is cooled by convection inside the wood.', 'Convection happens in liquids and gases.')]))
add(10, '10.5', mcq('s9u10s5h01', 'O5', 'Equal volumes of alcohol hand gel and water, both at room temperature, are put on your two hands. The gel feels colder. Why?',
    'The alcohol evaporates faster, so it takes thermal energy from your skin more quickly.',
    [('The gel was stored at a lower temperature.', 'Both were at room temperature.'), ('Alcohol is a better conductor than water.', 'The cooling comes from evaporation.'), ('Water evaporates faster than alcohol.', 'Alcohol evaporates faster.')]))

# ---------------- Unit 11 Sound ----------------
add(11, '11.2',
  num('s9u11s2h01', 'O2', 'A loudspeaker cone makes 1200 complete vibrations in 4 s. What is the frequency of the sound?', 300, 'Hz', ['Hz', 's', 'm/s'], 'Frequency = vibrations ÷ time = 1200 ÷ 4 = 300 Hz.'),
  mcq('s9u11s2h02', 'O3', 'In a sound wave, air particles move 0.5 mm forwards from their rest position, back through it, and 0.5 mm backwards. What is the amplitude?', '0.5 mm',
      [('1.0 mm', 'Amplitude is measured from the rest position, not from one extreme to the other.'), ('0.25 mm', 'The maximum displacement is 0.5 mm.'), ('It depends on the frequency.', 'Amplitude and frequency are independent.')]))
add(11, '11.4', mcq('s9u11s4h01', 'O4', 'Two sound waves of the same pitch meet and cancel completely, so there is silence. What must be true?',
    'They have equal amplitudes, and the peaks of one arrive with the troughs of the other.',
    [('They have equal amplitudes and their peaks arrive together.', 'Then they reinforce and the sound is louder.'), ('One has double the amplitude of the other.', 'Then they would only partly cancel.'), ('They travel at different speeds.', 'Sound of any pitch travels at the same speed in the same air.')]))

# ---------------- Unit 12 Electrical Circuits ----------------
add(12, '12.2', mcq('s9u12s2h01', 'O2', 'A lamp L1 is connected to a cell. A second identical lamp is added in series. What happens?',
    'The current in the circuit decreases and the voltage across L1 halves.',
    [('The current increases and the voltage across L1 stays the same.', 'More resistance in series gives less current.'), ('The current stays the same and the voltage across L1 doubles.', 'The cell voltage is shared between the two lamps.'), ('Nothing changes.', 'Both lamps become dimmer.')]))
add(12, '12.3', mcq('s9u12s3h01', 'O3', 'A lamp L1 is connected to a cell. A second identical lamp is added in parallel with L1. What happens?',
    'L1 stays the same brightness and the current from the cell doubles.',
    [('L1 becomes dimmer and the current from the cell halves.', 'That describes adding a lamp in series.'), ('L1 goes out.', 'Each branch still has the full cell voltage.'), ('The current from the cell stays the same.', 'Each branch carries its own current, so the total doubles.')]))
add(12, '12.5',
  num('s9u12s5h01', 'O5', 'The voltage across a resistor is 6 V and the current through it is 0.25 A. Calculate its resistance.', 24, 'Ω', ['Ω', 'V', 'A'], 'R = V ÷ I = 6 ÷ 0.25 = 24 Ω.'),
  graph('s9u12s5h02', 'O5', 'The voltage across a resistor is changed and the current is measured. Plot the results.', ax('Voltage (V)', 0, 8, 2), ax('Current (A)', 0, 0.4, 0.1),
        [[0, 0], [2, 0.1], [4, 0.2], [6, 0.3], [8, 0.4]],
        'What is the resistance of the resistor?', '20 Ω',
        [('0.05 Ω', 'That is current ÷ voltage; resistance is voltage ÷ current.'), ('3.2 Ω', 'That is 8 × 0.4; divide instead.'), ('It changes with the voltage.', 'A straight line through the origin means the resistance is constant.')]))

# ---------------- Unit 13 Earth and Climate Change ----------------
add(13, '13.1', mcq('s9u13s1h01', 'O1', 'What makes tectonic plates move?',
    'Slow convection currents in the hot mantle beneath the plates.',
    [('The spin of the Earth throws the plates outwards.', 'The spin does not drive plate movement.'), ('Ocean tides push the plates.', 'Tides move water, not plates.'), ('Wind blowing on the continents.', 'Wind cannot move rock plates.')]))
add(13, '13.2', mcq('s9u13s2h01', 'O2', 'A map shows the positions of thousands of earthquakes and volcanoes. How does it give evidence for tectonic plates?',
    'They lie along narrow bands, which mark the boundaries where plates meet and move.',
    [('They are spread evenly over the whole Earth.', 'They are concentrated in bands.'), ('They happen only on land.', 'Many are under the oceans.'), ('They happen only at the Equator.', 'They occur at all latitudes.')]))
add(13, '13.3', mcq('s9u13s3h01', 'O3', 'A green plant is sealed in a glass jar with a carbon dioxide sensor. In bright light the carbon dioxide concentration falls; in the dark it rises. What does this show about plants and the carbon cycle?',
    'In light, photosynthesis takes in more carbon dioxide than respiration releases, so plants help to keep the level in the atmosphere stable.',
    [('Plants only respire in the dark.', 'Plants respire all the time.'), ('Plants release carbon dioxide by photosynthesis.', 'Photosynthesis takes in carbon dioxide.'), ('Plants have no effect on carbon dioxide.', 'The concentration changes in both conditions.')]))
add(13, '13.4',
  num('s9u13s4h01', 'O4', 'The graph shows the area of Arctic sea ice each September. By how much did the area decrease between 1980 and 2020?', 3.5, 'million km²', ['million km²', 'km²'],
      '1980: 7.5 million km². 2020: 4.0 million km². Decrease = 3.5 million km².', tol=0.1,
      fig=line('Year', 'Sea ice area in million km²', (1980, 2020, 10), (0, 8, 1), [{'pts': [[1980, 7.5], [1990, 6.2], [2000, 6.3], [2010, 4.9], [2020, 4.0]]}])),
  multi('s9u13s4h02', 'O4', 'A graph shows the area of Arctic sea ice in September for five separate years. Select the TWO kinds of extra data that would make you more certain that the sea ice really is shrinking.',
        [('the area for every year, not just five', True), ('the area in other months of the year', True), ('the air temperature in one city on one day', False), ('the number of ships in the Arctic', False)],
        'More years show whether the change is a trend or natural variation; other months show whether it happens all year.'))

# ---------------- Unit 14 Astronomy ----------------
add(14, '14.2', multi('s9u14s2h01', 'O2', 'The collision theory says the Moon formed when a planet-sized object hit the young Earth. Select the TWO pieces of evidence that support it.',
    [('Moon rock has a very similar composition to the Earth\'s mantle.', True), ('The Moon is less dense than the Earth and has only a small iron core.', True), ('The Moon has craters.', False), ('The Moon reflects light from the Sun.', False)],
    'Material thrown out by the collision came mostly from the rocky outer layers, not the iron core.'))
add(14, '14.3', order('s9u14s3h01', 'O3', 'Put these stages in order to show how a star forms in a stellar nursery.',
    ['a cold cloud of dust and gas (a nebula)', 'gravity pulls part of the cloud together', 'the clump becomes denser and hotter (a protostar)', 'nuclear fusion starts in the core', 'the star gives out light and heat']))

apply(9, B)
