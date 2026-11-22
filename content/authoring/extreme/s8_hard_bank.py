"""Stage 8 Science — extra Hard (* Advanced) questions written by Atomic.
Coverage follows the challenge-level skills of the Stage 8 curriculum (data handling, planning, evaluating, multi-step
calculations); every context, number and wording here is Atomic's own. Charts are drawn by the Atomic figure library.
Edits content/src/stage8-unitNN.json in place; safe to run again. Then: node tools/build-content.mjs"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '..', 'src')
ADV = '* Advanced. '
F8 = 'The data show … For example … This is because … The results are / are not reliable because …'
PLAN = 'I will change … I will measure … I will keep … the same. I will repeat … I expect …'

def base(id, typ, obj, prompt, skill, diff='VH'):
    return {'id': id, 'type': typ, 'prompt': ADV + prompt, 'diff': diff, 'obj': obj, 'skill': skill, 'hint': '', 'reason': '', 'adv': True, 'source': 'Atomic original'}
def tbl(q, data):
    if data: q['data'] = {'head': data[0], 'rows': data[1:]}
    return q
def mcq(id, obj, prompt, right, wrong, reason='', data=None, fig=None, skill='Reasoning'):
    q = base(id, 'mcq', obj, prompt, skill); q['options'] = [{'t': right, 'ok': True, 'fb': 'Correct.'}] + [{'t': t, 'ok': False, 'fb': fb} for t, fb in wrong]
    q['reason'] = reason
    if fig: q['fig'] = fig
    return tbl(q, data)
def multi(id, obj, prompt, opts, reason='', data=None):
    q = base(id, 'multi', obj, prompt, 'Reasoning'); q['options'] = [{'t': t, 'ok': ok} for t, ok in opts]; q['reason'] = reason
    return tbl(q, data)
def num(id, obj, prompt, answer, unit, units, reason, data=None, fig=None, tol=0.0):
    q = base(id, 'num', obj, prompt, 'Application'); q.update({'answer': answer, 'unit': unit, 'tol': tol, 'units': units, 'errs': [], 'unitFb': '', 'reason': reason})
    if fig: q['fig'] = fig
    return tbl(q, data)
def order(id, obj, prompt, items, reason=''):
    q = base(id, 'order', obj, prompt, 'Knowledge', 'H'); q['items'] = items; q['reason'] = reason; return q
def graph(id, obj, prompt, x, y, pts, fprompt, fright, fwrong, reason=''):
    q = base(id, 'graph', obj, prompt, 'Data'); q.update({'x': x, 'y': y, 'pts': pts, 'reason': reason,
        'table_rows': [[str(a), str(b)] for a, b in pts],
        'follow': {'id': id + 'f', 'type': 'mcq', 'prompt': fprompt, 'diff': 'VH', 'obj': obj, 'skill': 'Data',
                   'options': [{'t': fright, 'ok': True, 'fb': 'Correct.'}] + [{'t': t, 'ok': False, 'fb': fb} for t, fb in fwrong]}})
    return q
def para(id, obj, prompt, rubric, need, model, data=None, frame=F8, words=40):
    q = base(id, 'para', obj, prompt, 'Reasoning'); q.update({'sentences': [4, 6], 'minWords': words, 'frame': frame,
        'rubric': [{'pt': p, 'kw': [k]} for p, k in rubric], 'need': need, 'model': model, 'partial': []})
    return tbl(q, data)
def line(xl, yl, x, y, series): return {'kind': 'linegraph', 'x': dict(zip(('min', 'max', 'step'), x), label=xl), 'y': dict(zip(('min', 'max', 'step'), y), label=yl), 'series': series}
def bars(labels, values, ymax, step, yl, xl=''): return {'kind': 'barchart', 'labels': labels, 'values': values, 'ymax': ymax, 'step': step, 'ylabel': yl, 'xlabel': xl}
def ax(label, lo, hi, step): return {'label': label, 'min': lo, 'max': hi, 'step': step}

B = {}   # (unit, section) -> questions
def add(u, sec, *qs): B.setdefault((u, sec), []).extend(qs)

# ---------------- Unit 1 Diet and Growth ----------------
add(1, '1.1',
  mcq('s8u01s1h01', 'O1', 'For a month, a nine-year-old eats mainly white rice, fried snacks and sweets. She eats no dairy foods, eggs, fish, beans or green vegetables. Which two problems are most likely?',
      'Slow growth and weak bones, because she lacks protein and calcium.',
      [('She will lack energy, because she eats no carbohydrate.', 'Rice, snacks and sweets give plenty of carbohydrate and fat.'),
       ('She will lose a lot of mass, because her diet has no fat.', 'Fried snacks contain a lot of fat.'),
       ('She will be dehydrated, because none of these foods contains water.', 'Water comes mainly from drinks; the question is about missing nutrients.')],
      'Check each nutrient: the diet has carbohydrate and fat, but no good source of protein (growth and repair) or calcium (bones and teeth).'))
add(1, '1.2',
  num('s8u01s2h01', 'O3', 'The bar chart shows the energy in 100 g of four foods. How much more energy is there in 50 g of peanuts than in 50 g of banana?', 1010, 'kJ', ['kJ', 'J', 'g'],
      '50 g is half of 100 g: peanuts 2400 ÷ 2 = 1200 kJ, banana 380 ÷ 2 = 190 kJ. Difference = 1200 − 190 = 1010 kJ.',
      fig=bars(['banana', 'bread', 'cheese', 'peanuts'], [380, 1000, 1700, 2400], 2500, 500, 'Energy in kJ per 100 g')),
  para('s8u01s2h02', 'O3', 'Plan the meals for one day for a nine-year-old who swims every evening. Name the foods and explain which nutrients they provide and why this child needs them.',
       [('Names a protein food and links it to growth or repair of muscles', 'protein'),
        ('Names a carbohydrate food and links it to energy for swimming', 'carbohydrate|energy'),
        ('Includes calcium or vitamin D for strong bones and teeth', 'calcium|vitamin D|bones'),
        ('Includes fruit or vegetables for vitamins, minerals or fibre', 'fruit|vegetable|vitamin|fibre'),
        ('Includes water to replace what is lost', 'water')], 4,
       'For breakfast she has porridge with milk and a banana, which gives carbohydrate for energy and calcium for strong bones. Lunch is rice with grilled fish and green vegetables, so she gets protein for growth and to repair her muscles after swimming. The vegetables and an orange give vitamins and fibre. Before swimming she eats a wholemeal sandwich for slow-release energy. She drinks water all day to replace the water she loses.',
       frame='For breakfast … because … For lunch … This gives … Before swimming … She also needs …'))
add(1, '1.3',
  graph('s8u01s3h01', 'O4', 'A town records the percentage of adults who smoke. Plot the results.', ax('Year', 2000, 2020, 5), ax('Adults who smoke (%)', 0, 30, 5),
        [[2000, 30], [2005, 26], [2010, 21], [2015, 17], [2020, 14]],
        'The town wants fewer than 10% of adults to smoke. Use the trend to choose the best conclusion.',
        'The percentage is falling by about 4 each five years, so it should drop below 10% soon after 2025.',
        [('The percentage is rising, so the target will never be met.', 'The values go down from 30 to 14.'),
         ('The percentage has already fallen below 10%.', 'The last value is 14%.'),
         ('There is no pattern, so no prediction can be made.', 'There is a steady fall of 3–5 each five years.')]),
  multi('s8u01s3h02', 'O4', 'Students model a leg bone with a paper tube and hang masses from the middle until it bends. Select the TWO hypotheses they can test with this model.',
        [('Wide tubes hold more mass than narrow tubes before bending.', True), ('Long tubes bend with less mass than short tubes.', True),
         ('People who drink milk have stronger bones.', False), ('Bones heal faster in children than in adults.', False)],
        'A model can only test things you can change on the model itself: its width and its length. Diet and healing need real people.'))

# ---------------- Unit 2 Human Body Systems ----------------
add(2, '2.2',
  order('s8u02s2h01', 'O2', 'Put these in order to show the path of an oxygen particle from the air into the blood.', ['nose', 'trachea', 'bronchus', 'bronchiole', 'air sac (alveolus)', 'blood capillary']),
  num('s8u02s2h02', 'O3', 'The graph shows the mean volume of air breathed out in one breath by swimmers and by non-swimmers. Calculate the difference between the two groups at age 40.', 0.8, 'dm³', ['dm³', 'cm³', 'm³'],
      'Read both lines at age 40: swimmers 4.2 dm³, non-swimmers 3.4 dm³. Difference = 4.2 − 3.4 = 0.8 dm³.', tol=0.05,
      fig=line('Age in years', 'Mean volume breathed out in dm³', (10, 70, 10), (0, 5, 1),
               [{'pts': [[10, 2.6], [20, 4.4], [30, 4.4], [40, 4.2], [50, 3.9], [60, 3.5], [70, 3.0]], 'label': 'swimmers'},
                {'pts': [[10, 2.4], [20, 3.8], [30, 3.6], [40, 3.4], [50, 3.1], [60, 2.7], [70, 2.3]], 'label': 'non-swimmers'}])),
  mcq('s8u02s2h03', 'O3', 'In a lung-volume study, the scientists measure 300 people in each age group instead of 5. What is the best reason?',
      'One unusual person changes the mean much less, so the mean is more reliable.',
      [('It makes each measurement more precise.', 'Precision depends on the measuring instrument, not on how many people are tested.'),
       ('It makes the test fair.', 'A fair test is about control variables, not sample size.'),
       ('It means the results do not need to be checked.', 'Large samples still need checking.')]),
  mcq('s8u02s2h04', 'O2', 'Use the data. Which conclusion and explanation is best?',
      'Larger mammals have a larger lung surface area, because they have more cells that need oxygen.',
      [('Larger mammals have a smaller lung surface area, because they breathe more slowly.', 'The area goes up as mass goes up.'),
       ('There is no link between body mass and lung surface area.', 'Every increase in mass comes with an increase in area.'),
       ('Lung surface area depends only on the habitat.', 'The table gives no habitat data, and the pattern follows mass.')],
      data=[['Mammal', 'Body mass in kg', 'Lung surface area in m²'], ['mouse', '0.02', '0.07'], ['rabbit', '3', '6'], ['dog', '20', '40'], ['human', '70', '75'], ['horse', '500', '2400']]),
  para('s8u02s2h05', 'O3', 'Yeast respires and makes carbon dioxide gas. Plan an investigation to test this hypothesis: “The more sugar yeast is given, the faster it respires.” You have bottles, balloons, yeast, sugar, warm water and a tape measure.',
       [('Change the mass of sugar (at least three values)', 'sugar'),
        ('Measure the gas made, e.g. the distance around the balloon after a set time', 'balloon|gas|carbon dioxide'),
        ('Keep the temperature, volume of water and mass of yeast the same', 'same'),
        ('Repeat each test and calculate a mean', 'repeat|mean|average'),
        ('States what result would support the hypothesis', 'support|bigger|more gas|larger')], 4,
       'I will change the mass of sugar, using 0 g, 2 g, 4 g and 6 g in four bottles. Each bottle will have the same mass of yeast and the same volume of water at the same temperature. I will fix a balloon on each bottle and measure the distance around the balloon after 20 minutes to compare the gas made. I will repeat each test three times and calculate a mean. If the balloons with more sugar are bigger, the results support the hypothesis.', frame=PLAN))
add(2, '2.3',
  graph('s8u02s3h01', 'O4', 'Climbers stay at a camp 4000 m above sea level. Their red blood cell count is measured. Plot the results.', ax('Days at high altitude', 0, 20, 5), ax('Red blood cells (millions per mm³)', 4, 7, 0.5),
        [[0, 5.0], [5, 5.5], [10, 6.0], [15, 6.0], [20, 6.5]],
        'What is the best explanation for the pattern?',
        'There is less oxygen in the air, so the body makes more red blood cells to carry enough oxygen.',
        [('There is more oxygen at altitude, so more cells are needed to store it.', 'There is less oxygen in each breath at altitude.'),
         ('Cold air makes red blood cells divide.', 'Red blood cells have no nucleus and cannot divide; they are made in bone marrow.'),
         ('The climbers ate more iron each day.', 'Diet was not changed in this study.')]))

# ---------------- Unit 3 Ecosystems ----------------
add(3, '3.1',
  num('s8u03s1h01', 'O1', 'Young fish shelter in seagrass beds before moving to a reef. Calculate the percentage increase in the mass of snapper on reefs that have seagrass nearby.', 40, '%', ['%', 'kg/km²'],
      'Increase = 2100 − 1500 = 600. Percentage increase = 600 ÷ 1500 × 100 = 40%.',
      data=[['Fish', 'Reef with no seagrass nearby (kg/km²)', 'Reef with seagrass nearby (kg/km²)'], ['snapper', '1500', '2100'], ['wrasse', '820', '860']]),
  mcq('s8u03s1h02', 'O2', 'A desert cactus grows very slowly and stores water in its stem. Why is it rarely found in nearby wet forests?',
      'Fast-growing plants shade it and take the space, so it cannot compete there.',
      [('Cacti cannot photosynthesise when it rains.', 'Rain does not stop photosynthesis.'),
       ('There are no animals in wet forests to spread its seeds.', 'Wet forests have many animals.'),
       ('Cacti need sand because sand contains food for the plant.', 'Plants make their own food; soil gives water and minerals.')],
      'Adaptations for one habitat can be a disadvantage in another: slow growth is no problem in a desert but loses the competition for light elsewhere.'))
add(3, '3.2',
  para('s8u03s2h01', 'O3', 'Golden apple snails are an invasive species that eat young rice plants. Some farmers release ducks into the rice fields to eat the snails. Plan an investigation to find out if the ducks reduce the number of snails.',
       [('Compare fields with ducks and fields without ducks (a control)', 'without|control|no ducks'),
        ('Count snails in a fixed area, e.g. inside a 1 m² quadrat', 'count|quadrat|number of snails'),
        ('Keep the field size, rice variety and time the same', 'same'),
        ('Use several fields or repeat counts and calculate a mean', 'repeat|several|mean|average'),
        ('Compare the results to decide if ducks reduce snails', 'compare|fewer|lower|reduce')], 4,
       'I will choose ten rice fields of the same size planted with the same rice on the same day. Ducks will be released into five fields and the other five will have no ducks as a control. After four weeks I will count the number of snails inside a 1 m² quadrat at ten places in each field. I will calculate the mean number of snails per square metre for each group. If the fields with ducks have fewer snails, the ducks reduce the snail population.', frame=PLAN),
  num('s8u03s2h02', 'O4', 'A pollutant cannot be broken down. Each plankton contains 0.02 units of it. A small fish eats 500 plankton, and a tuna eats 40 small fish. How many units of the pollutant end up in the tuna?', 400, 'units', ['units'],
      'One small fish: 500 × 0.02 = 10 units. Tuna: 40 × 10 = 400 units. The pollutant builds up along the food chain (bioaccumulation).'),
  mcq('s8u03s2h03', 'O4', 'A farmer wants to know if a new insect spray harms bees. Which source is likely to be the least biased?',
      'A study by university scientists who are not paid by the spray company.',
      [('The leaflet from the company that sells the spray.', 'The company earns money from sales, so it may leave out harmful results.'),
       ('A neighbour who has used the spray once.', 'One person\'s experience is not enough evidence.'),
       ('An advert for a rival spray.', 'The rival also wants to sell its own product.')]))

# ---------------- Unit 4 The Structure of an Atom ----------------
add(4, '4.2',
  mcq('s8u04s2h01', 'O4', 'Fast, positively charged particles are fired at very thin metal foil. Almost all pass straight through, but a few bounce back. What do these two results show?',
      'An atom is mostly empty space, with a tiny, dense, positive nucleus.',
      [('An atom is a solid ball with charge spread evenly through it.', 'Then no particles would bounce straight back.'),
       ('Electrons are heavy enough to knock the particles backwards.', 'Electrons have far too little mass.'),
       ('The foil has holes between its atoms.', 'The particles pass through the atoms themselves.')]),
  num('s8u04s2h02', 'O4', 'In a scattering experiment, 1 particle in every 8000 bounces back. 2 400 000 particles are fired. How many are expected to bounce back?', 300, 'particles', ['particles'],
      '2 400 000 ÷ 8000 = 300 particles.'))

# ---------------- Unit 5 Mixtures and Solubility ----------------
add(5, '5.1',
  num('s8u05s1h01', 'O1', 'Pure gold is 24 carat. An 18-carat ring is 18 ÷ 24 = 75% gold. What percentage of a 9-carat ring is gold?', 37.5, '%', ['%', 'carat'],
      '9 ÷ 24 × 100 = 37.5%.'),
  graph('s8u05s1h02', 'O2', 'Gold is mixed with other metals to make alloys. Plot the hardness of each alloy.', ax('Gold in the alloy (%)', 40, 100, 20), ax('Hardness (arbitrary units)', 0, 150, 25),
        [[40, 150], [60, 125], [80, 75], [100, 25]],
        'A jeweller says: “A ring with less gold in it is harder to scratch.” Does the graph support this?',
        'Yes: as the percentage of gold goes down, the hardness goes up.',
        [('No: pure gold is the hardest.', 'Pure gold (100%) has the lowest hardness, 25.'),
         ('No: hardness does not change.', 'Hardness changes from 25 to 150.'),
         ('Yes: because pure substances are always harder than mixtures.', 'The graph shows the mixture (alloy) is harder.')]))
add(5, '5.2',
  mcq('s8u05s2h01', 'O3', 'A student puts a spot of marker ink on chromatography paper and stands it in water. The water rises, but the ink spot stays on the pencil line. What should she do next?',
      'Repeat with a different solvent, such as ethanol, because the ink is insoluble in water.',
      [('Use a bigger spot of ink.', 'More ink will not help if it does not dissolve.'),
       ('Draw the line in pen instead of pencil.', 'Pen ink would dissolve and spoil the result.'),
       ('Leave it for a week.', 'An insoluble ink will not move however long it is left.')]))
add(5, '5.3',
  num('s8u05s3h01', 'O4', '15 g of sugar is stirred into 250 g of water until it has all dissolved. What is the mass of the solution?', 265, 'g', ['g', 'kg', 'cm³'],
      'Mass is conserved when a solute dissolves: 250 + 15 = 265 g.'),
  mcq('s8u05s3h02', 'O4', 'Solution X is copper sulfate solution. How can you make 200 cm³ of a solution that is one quarter as concentrated as X?',
      'Measure 50 cm³ of X and add water until the total volume is 200 cm³.',
      [('Measure 200 cm³ of X and add 50 cm³ of water.', 'This is only slightly less concentrated than X.'),
       ('Measure 100 cm³ of X and add 100 cm³ of water.', 'This is half as concentrated.'),
       ('Measure 25 cm³ of X and add water until the total is 200 cm³.', 'This is one eighth as concentrated.')],
      'A quarter of the concentration means a quarter of the final volume is X: 200 ÷ 4 = 50 cm³.'),
  num('s8u05s3h03', 'O4', 'The graph shows how the solubility of salt A and salt B changes with temperature. At what temperature do the two salts have the same solubility?', 40, '°C', ['°C', 'g'],
      'The lines cross at 40 °C, where both have a solubility of 40 g per 100 g of water.', tol=2,
      fig=line('Temperature in °C', 'Solubility in g per 100 g of water', (0, 80, 20), (0, 70, 10),
               [{'pts': [[0, 20], [20, 30], [40, 40], [60, 50], [80, 60]], 'label': 'salt A'}, {'pts': [[0, 36], [40, 40], [80, 44]], 'label': 'salt B'}])))

# ---------------- Unit 6 Chemical Reactivity ----------------
add(6, '6.1',
  para('s8u06s1h01', 'O1', 'Plan an investigation to find out whether iron nails rust more quickly when they are warm than when they are cold.',
       [('Change the temperature (e.g. fridge, room, warm cupboard)', 'temperature|fridge|warm'),
        ('Measure the rusting, e.g. time for rust to appear or change in mass', 'mass|time|rust'),
        ('Keep the nails, the volume of water and the air the same', 'same'),
        ('Repeat with several nails at each temperature', 'repeat|several|three'),
        ('Says what result would show warm nails rust faster', 'faster|first|more rust|sooner')], 4,
       'I will change the temperature by putting test tubes in a fridge, in the classroom and in a warm cupboard. Each tube will have the same type of clean iron nail, the same volume of water and be open to the air. Every day I will record how much of each nail is covered in rust. I will use three nails at each temperature to check the results are reliable. If the nails in the warm cupboard show rust first, then iron rusts more quickly when it is warm.', frame=PLAN))
add(6, '6.2',
  mcq('s8u06s2h01', 'O2', 'Hot-water pipes in houses are often made of copper, not iron. What is the best explanation?',
      'Copper does not react with water, but iron slowly reacts with water and oxygen and rusts.',
      [('Copper reacts with water to make a protective gas.', 'Copper does not react with water.'),
       ('Iron is too soft to make into pipes.', 'Iron is hard and strong; the problem is rusting.'),
       ('Iron reacts violently with cold water.', 'Iron reacts only slowly.')]))
add(6, '6.3',
  mcq('s8u06s3h01', 'O3', 'Equal masses of four metals are added to the same acid. Use the results to put the metals in order, most reactive first.',
      'P, R, Q, S',
      [('S, Q, R, P', 'This is least reactive first.'), ('Q, R, P, S', 'The longest time means the slowest reaction.'), ('P, Q, R, S', 'R (40 s) is faster than Q (95 s).')],
      'The more reactive the metal, the faster hydrogen is made, so the shorter the time. No gas means no reaction.',
      data=[['Metal', 'Time to collect 20 cm³ of hydrogen in s'], ['P', '12'], ['Q', '95'], ['R', '40'], ['S', 'no gas after 10 minutes']]),
  multi('s8u06s3h02', 'O3', 'In the metal and acid investigation, select ALL the variables that must be kept the same for a fair test.',
        [('the concentration of the acid', True), ('the volume of the acid', True), ('the mass and size of the pieces of metal', True), ('the type of metal', False), ('the time taken to collect the gas', False)],
        'The type of metal is what you change and the time is what you measure. Everything else that could affect the speed must stay the same.'))
add(6, '6.4',
  mcq('s8u06s4h01', 'O4', 'A student tests six metals with dilute acid and records the time to fill a test tube with hydrogen. She leaves the row for copper empty. Why?',
      'Copper is less reactive than hydrogen, so it does not react with dilute acid and no gas is made.',
      [('Copper reacts too quickly to time.', 'Copper does not react with dilute acid.'),
       ('Copper makes oxygen instead of hydrogen.', 'No gas is made.'),
       ('Copper dissolves without making a gas.', 'Copper does not dissolve in dilute hydrochloric acid.')]))

# ---------------- Unit 8 Forces and Motion ----------------
add(8, '8.1',
  num('s8u08s1h01', 'O1', 'A ferry travels at a constant speed of 12 m/s. How far does it travel in 5 minutes?', 3600, 'm', ['m', 'km', 'm/s'],
      '5 minutes = 300 s. Distance = speed × time = 12 × 300 = 3600 m.'),
  num('s8u08s1h02', 'O1', 'Lan runs at a constant 5 m/s. Minh cycles at a constant 8 m/s. They start together. How much further has Minh travelled after 2 minutes?', 360, 'm', ['m', 'km', 'm/s'],
      'In 120 s Lan travels 5 × 120 = 600 m and Minh travels 8 × 120 = 960 m. Difference = 360 m. (Or 3 m/s × 120 s.)'))
add(8, '8.2',
  graph('s8u08s2h01', 'O2', 'A delivery drone flies 600 m to a house in 2 minutes, hovers there for 1 minute, then flies back in 2 minutes. Plot its distance from the start.', ax('Time (minutes)', 0, 5, 1), ax('Distance from start (m)', 0, 600, 100),
        [[0, 0], [2, 600], [3, 600], [5, 0]],
        'What was the speed of the drone on the way to the house?', '5 m/s',
        [('300 m/s', '300 is the distance in metres each minute, not each second.'), ('120 m/s', 'Use only the first 2 minutes: 600 m in 120 s.'), ('2 m/s', 'Speed = distance ÷ time = 600 ÷ 120.')],
        '600 m in 2 minutes = 600 m in 120 s = 5 m/s.'))
add(8, '8.3',
  mcq('s8u08s3h01', 'O3', 'A hot-air balloon has a weight of 3000 N and an upthrust of 3000 N. A steady wind pushes it east with a force of 200 N. Air resistance is 200 N to the west. What happens to the balloon?',
      'It stays at the same height and moves at a constant speed.',
      [('It rises, because the upthrust is large.', 'Upthrust and weight are equal, so there is no change in height.'),
       ('It speeds up towards the east.', 'The wind force and air resistance are balanced.'),
       ('It must be stationary, because all the forces are balanced.', 'Balanced forces mean no change in motion; a moving object keeps moving at a constant speed.')]))
add(8, '8.4',
  num('s8u08s4h01', 'O4', 'A wheel nut needs a moment of 90 N m to turn it. A mechanic uses a wrench 0.3 m long. What force must she apply at the end of the wrench?', 300, 'N', ['N', 'N m', 'm'],
      'Force = moment ÷ distance = 90 ÷ 0.3 = 300 N.'),
  num('s8u08s4h02', 'O4', 'A child of weight 400 N sits 1.5 m from the pivot of a seesaw. How far from the pivot must a child of weight 300 N sit to balance it?', 2, 'm', ['m', 'N', 'N m'],
      'Moments must be equal: 400 × 1.5 = 600 N m. Distance = 600 ÷ 300 = 2 m.'))

# ---------------- Unit 9 Pressure and Diffusion ----------------
add(9, '9.1',
  num('s8u09s1h01', 'O1', 'A person of weight 600 N stands on snow in boots with a total area of 0.04 m². She puts on snowshoes with a total area of 0.25 m². By how much does the pressure on the snow decrease?', 12600, 'N/m²', ['N/m²', 'N', 'm²'],
      'Boots: 600 ÷ 0.04 = 15 000 N/m². Snowshoes: 600 ÷ 0.25 = 2400 N/m². Decrease = 15 000 − 2400 = 12 600 N/m².'))
add(9, '9.5',
  multi('s8u09s5h01', 'O5', 'A crystal of purple dye is placed at the bottom of a beaker of water. Select the TWO changes that make the colour spread faster.',
        [('using warmer water', True), ('stirring the water', True), ('using a larger beaker with more water', False), ('cooling the beaker in ice', False)],
        'Warmer particles move faster, and stirring moves the dye particles around. More water gives the particles further to travel.'),
  para('s8u09s5h02', 'O5', 'You can smell a bowl of hot soup from across the room, but you can hardly smell the same soup when it is cold. Use the particle model to explain why.',
       [('Some particles from the soup evaporate into the air', 'evaporat|escape|leave'),
        ('In hot soup the particles have more energy / move faster', 'faster|more energy'),
        ('The particles spread through the air by diffusion', 'diffus|spread'),
        ('They move from high concentration to low concentration, mixing with air particles', 'concentration|collid|air particles|random'),
        ('More particles reach your nose each second from the hot soup', 'nose|reach')], 4,
       'Some particles from the soup evaporate and escape into the air. In hot soup the particles have more energy and move faster, so many more of them leave the liquid. These particles spread through the air by diffusion, moving from where they are in high concentration to where they are in low concentration. Hot particles also move faster through the air. So more particles reach your nose each second from the hot soup, and the smell is stronger.',
       frame='Particles from the soup … In hot soup … They spread by … So …'))

# ---------------- Unit 10 Light ----------------
add(10, '10.2',
  num('s8u10s2h01', 'O2', 'A ray of light hits a plane mirror. The angle between the ray and the mirror surface is 35°. What is the angle of reflection?', 55, '°', ['°'],
      'Angles are measured from the normal. Angle of incidence = 90 − 35 = 55°, and the angle of reflection is equal to it.'),
  num('s8u10s2h02', 'O2', 'Two plane mirrors are fixed at 90° to each other. A ray hits the first mirror with an angle of incidence of 30° and reflects onto the second mirror. What is the angle of incidence at the second mirror?', 60, '°', ['°'],
      'The reflected ray leaves the first mirror at 30° to its normal. The two normals are at 90° to each other, so the angle at the second mirror is 90 − 30 = 60°.'))
add(10, '10.3',
  mcq('s8u10s3h01', 'O3', 'A ray of light passes from air through a rectangular glass block and out into air again. Which description is correct?',
      'It bends towards the normal entering the glass and away from the normal leaving it, so it comes out parallel to its first direction.',
      [('It bends away from the normal at both surfaces.', 'Entering glass, light slows down and bends towards the normal.'),
       ('It bends towards the normal at both surfaces.', 'Leaving glass, light speeds up and bends away from the normal.'),
       ('It passes straight through without bending, whatever the angle.', 'It only goes straight if it travels along the normal.')]))
add(10, '10.4',
  mcq('s8u10s4h01', 'O4', 'White light passes through a plastic prism and makes a spectrum. Violet light is bent the most and red the least. What does this show?',
      'Violet light is slowed down the most in the plastic, and red light the least.',
      [('Red light is slowed down the most.', 'The colour that slows the most bends the most.'),
       ('All colours travel at the same speed in the plastic.', 'Then they would all bend by the same amount and no spectrum would form.'),
       ('The prism adds colours to the white light.', 'White light already contains all the colours.')]))
add(10, '10.5',
  multi('s8u10s5h01', 'O5', 'A leaf looks green in white light. Select the TWO colours of light that would make the leaf look black.',
        [('red light', True), ('blue light', True), ('green light', False), ('white light', False)],
        'A green leaf reflects only green light. In red or blue light there is no green light to reflect, so it looks black.'))

# ---------------- Unit 11 Magnetism ----------------
add(11, '11.2',
  mcq('s8u11s2h01', 'O2', 'The pointed end of the nail in an electromagnet is a north pole. Which change makes the pointed end a south pole?',
      'Reverse the connections to the battery, so the current flows the other way.',
      [('Add more turns to the coil in the same direction.', 'This makes the magnet stronger but keeps the same poles.'),
       ('Use a larger current.', 'This makes the magnet stronger but keeps the same poles.'),
       ('Use a longer nail.', 'The length of the core does not swap the poles.')]),
  mcq('s8u11s2h02', 'O2', 'A student measures the strength of an electromagnet by counting how many paperclips it can hold. Should he use small or large paperclips?',
      'Small ones: each clip weighs less, so the count can show smaller differences in strength.',
      [('Large ones: they are easier to count.', 'A magnet holding 2 or 3 large clips cannot show small differences.'),
       ('It makes no difference.', 'The size of each step in the measurement matters.'),
       ('Large ones: they are more magnetic.', 'Both are steel; the mass per clip is what matters.')]),
  graph('s8u11s2h03', 'O2', 'A student changes the number of turns on an electromagnet and counts the paperclips it holds. Plot the results.', ax('Number of turns', 0, 50, 10), ax('Paperclips held', 0, 15, 3),
        [[10, 3], [20, 6], [30, 9], [40, 12], [50, 15]],
        'Use the pattern to predict the number of paperclips held with 60 turns.', '18',
        [('15', 'The number keeps rising by 3 for each extra 10 turns.'), ('20', 'Each extra 10 turns adds 3 clips, not 5.'), ('30', 'The clips are not half the number of turns.')]))
add(14, '14.3',
  mcq('s8u14s3h01', 'O4', 'Which piece of evidence shows that the Earth\'s magnetic field where you live is weaker than the field 1 cm from a bar magnet?',
      'A compass needle stops pointing north and points at the bar magnet when the magnet is brought close.',
      [('A compass needle always points north.', 'This shows the Earth has a field, not how strong it is.'),
       ('The Earth is much bigger than a bar magnet.', 'Size is not evidence of field strength at one place.'),
       ('Bar magnets are made of steel.', 'The material is not evidence about the strength of the field.')]))

# ---------------- Unit 13 Weather and Climate ----------------
add(13, '13.1',
  num('s8u13s1h01', 'O1', 'The temperature at a weather station is recorded every six hours. Calculate the mean temperature for 2 June.', 15, '°C', ['°C'],
      '(12 + 15 + 19 + 14) ÷ 4 = 60 ÷ 4 = 15 °C.',
      data=[['Date', '00:00', '06:00', '12:00', '18:00'], ['1 June', '11 °C', '13 °C', '18 °C', '15 °C'], ['2 June', '12 °C', '15 °C', '19 °C', '14 °C'], ['3 June', '10 °C', '12 °C', '16 °C', '13 °C']]),
  mcq('s8u13s1h02', 'O2', 'A student uses one week of temperature readings from one town to describe the climate of the whole country. Why is this not valid?',
      'Climate is the average weather over about 30 years and over a large area; one week in one town is only weather.',
      [('Thermometers cannot measure climate.', 'Temperature records are part of climate data.'),
       ('Climate only describes rainfall.', 'Climate includes temperature, rainfall, wind and more.'),
       ('A week is too long.', 'A week is far too short.')]))
add(13, '13.2',
  num('s8u13s2h01', 'O3', 'The graph shows the temperature at a site near the South Pole over the last 150 thousand years. A cold (glacial) period began when the temperature fell below −6 °C and ended when it rose above −6 °C again. For how long did it last?', 100, 'thousand years', ['thousand years', 'years'],
      'The line falls below −6 °C at 110 thousand years ago and rises above it at 10 thousand years ago: 110 − 10 = 100 thousand years.', tol=5,
      fig=line('Thousand years ago', 'Temperature in °C', (0, 150, 25), (-10, 0, 2),
               [{'pts': [[150, -8], [130, -2], [120, -3], [110, -6], [90, -8], [60, -8.5], [30, -9], [20, -9], [10, -6], [5, -2], [0, -2]]}])),
  para('s8u13s2h02', 'O4', 'Describe two pieces of evidence that the Earth\'s climate is changing, and explain why temperature records from the last 150 years are more reliable than evidence about the climate thousands of years ago.',
       [('Carbon dioxide in the atmosphere has risen (measured directly or in ice cores)', 'carbon dioxide|ice core'),
        ('Evidence of warming: rising global temperature, melting ice or rising sea level', 'melting|sea level|glacier|warmer|rising temperature'),
        ('Recent temperatures are measured directly with thermometers or satellites', 'thermometer|satellite|measured|instrument'),
        ('Older evidence is indirect (ice cores, tree rings, fossils), so it has to be interpreted', 'indirect|tree ring|fossil|estimate|interpret'),
        ('Recent records come from many places around the world', 'many places|around the world|stations')], 4,
       'Air bubbles trapped in ice cores show that there is more carbon dioxide in the atmosphere now than for hundreds of thousands of years. Glaciers and polar ice are melting and the sea level is rising, which shows the Earth is getting warmer. Records from the last 150 years are reliable because temperatures were measured directly with thermometers at many places around the world. Older evidence is indirect, because scientists have to estimate temperatures from ice cores, tree rings and fossils. This means the older values are less certain.',
       frame='One piece of evidence is … Another is … Recent records are reliable because … Older evidence …'))

# ---------------- Unit 14 Planetary Systems ----------------
add(14, '14.1',
  mcq('s8u14s1h01', 'O1', 'A single particle of dust in space has a tiny mass. How can a cloud of dust and gas have gravity strong enough to pull itself together and form stars?',
      'The cloud contains so many particles that its total mass is enormous.',
      [('Dust particles in space are magnetic.', 'Gravity, not magnetism, pulls the cloud together.'),
       ('Gravity is stronger in space than on Earth.', 'Gravity depends on mass and distance, not on being in space.'),
       ('Each dust particle is heavier than a planet.', 'Each particle has a tiny mass.')]))
add(14, '14.2',
  mcq('s8u14s2h01', 'O3', 'The total mass of all the asteroids in the asteroid belt is less than the mass of the Moon. How does this support the idea that asteroids are rocks left over from the formation of the Solar System?',
      'There was too little material there, pulled about by Jupiter\'s gravity, to join into a planet, so the pieces stayed separate.',
      [('It shows the asteroids are pieces of the Sun.', 'Asteroids are rock and metal, not hot gas.'),
       ('It shows that a planet exploded recently.', 'A broken planet would leave about a planet\'s mass of material.'),
       ('It shows that asteroids are growing into a planet now.', 'There is not enough mass, and Jupiter\'s gravity keeps them apart.')]),
  multi('s8u14s2h02', 'O2', 'Select the TWO features that asteroids and planets have in common.',
        [('They orbit the Sun.', True), ('They were formed from the same cloud of dust and gas.', True), ('They are all spherical.', False), ('They all have an atmosphere.', False)],
        'Most asteroids are too small for gravity to pull them into a sphere or to hold an atmosphere.'))

n = 0
for (u, sec), qs in sorted(B.items()):
    p = os.path.join(SRC, 'stage8-unit%02d.json' % u); d = json.load(open(p)); s = next(x for x in d['sections'] if x['id'] == sec)
    ids = {q['id'] for q in qs}; s['adv'] = [q for q in s['adv'] if q['id'] not in ids] + qs; n += len(qs)
    for q in qs: assert q['obj'] in d['objectives'], (q['id'], q['obj'])
    json.dump(d, open(p, 'w'), ensure_ascii=False)
print('Stage 8: added', n, 'Hard questions in', len(B), 'lessons')
