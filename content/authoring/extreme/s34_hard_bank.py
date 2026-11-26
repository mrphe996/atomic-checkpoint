"""Stage 3 and Stage 4 Science (young Primary) — extra Hard (* Advanced) questions written by Camday.
Learners aged 7–9 do not type: every answer is tapped (picture choices, sorting, matching, ordering).
Edits content/src/stage3-unitNN.json and stage4-unitNN.json in place; safe to run again."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hardkit import *

def pic(id, obj, prompt, right, wrong, fig=None, data=None, skill='Reasoning'):
    q = base(id, 'mcq', obj, prompt, skill, 'VH'); q['options'] = [{'t': right[0], 'ok': True, 'fb': 'Correct.', 'e': right[1]}] + [{'t': t, 'ok': False, 'fb': fb, 'e': e} for t, e, fb in wrong]
    if fig: q['fig'] = fig
    return tbl(q, data)
def sort(id, obj, prompt, cols, rows):
    q = base(id, 'grid', obj, prompt, 'Data', 'VH'); q.update({'cols': cols, 'rows': [{'l': l, 'a': [a]} for l, a in rows], 'mode': 'classify'}); return q
def pairs(id, obj, prompt, ps):
    q = base(id, 'match', obj, prompt, 'Knowledge', 'H'); q['pairs'] = [{'l': l, 'r': r} for l, r in ps]; return q
def seq(id, obj, prompt, items):
    q = base(id, 'order', obj, prompt, 'Reasoning', 'H'); q['items'] = items; return q

# =============================== STAGE 3 ===============================
B = {}
def add(u, sec, *qs): B.setdefault((u, sec), []).extend(qs)

add(1, '1.1', sort('p3u01s1h01', 'O1', 'Sort each thing: is it alive, was it once alive, or was it never alive?', ['alive', 'once alive', 'never alive'],
    [('🐸 frog eggs in a pond', 'alive'), ('🥄 a wooden spoon', 'once alive'), ('🌧️ rain', 'never alive'), ('🦀 a crab', 'alive'), ('🧱 a plastic brick', 'never alive'), ('📄 a sheet of paper', 'once alive')]))
add(1, '1.2', pic('p3u01s2h01', 'O2', 'A plant is pulled up and its roots are cut off. It is put back on top of the soil. What will happen?', ('It cannot take in water and it falls over', '🥀'),
    [('It grows faster', '🌿', 'Without roots it gets no water.'), ('It makes more flowers', '🌸', 'It cannot make flowers without water.')]))
add(1, '1.3', pic('p3u01s3h01', 'O3', 'Two bean plants get the same water. One is on a sunny windowsill. One is under a dark box. After two weeks, which looks healthy and green?', ('The plant on the sunny windowsill', '🪟'),
    [('The plant under the dark box', '📦', 'Plants need light to grow well.'), ('Both look the same', '🟰', 'Light makes a big difference.')]))
add(1, '1.4', pic('p3u01s4h01', 'O4', 'Two plants were the same height at the start. Look at the bar chart. How much taller is the watered plant after 10 days?', ('8 cm', '📏'),
    [('4 cm', '🌱', '4 cm is the height of the plant with no water.'), ('16 cm', '➕', 'Take away: 12 − 4.')],
    fig=bars(['watered', 'not watered'], [12, 4], 14, 2, 'Height in cm'), skill='Data'))

add(2, '2.1', pic('p3u02s1h01', 'O1', 'Honey moves slowly. When you pour it into a jar, it takes the shape of the jar. What is honey?', ('a liquid', '🍯'),
    [('a solid', '🧊', 'A solid keeps its own shape.'), ('a gas', '💨', 'A gas spreads out to fill all the space.')]))
add(2, '2.2', seq('p3u02s2h01', 'O2', 'A bag has stones, sand and salt all mixed up. Put the steps in order to get all three back.',
    ['sieve the mixture to take out the stones', 'add water and stir so the salt dissolves', 'filter to catch the sand', 'leave the salty water in a warm place until the water has gone']))
add(2, '2.3', pic('p3u02s3h01', 'O3', 'Children count how many spoons of sugar dissolve in a cup of water. Look at the bar chart. What does it show?', ('Warmer water dissolves more sugar', '♨️'),
    [('Colder water dissolves more sugar', '❄️', 'Cold water dissolved only 2 spoons.'), ('Temperature makes no difference', '🟰', 'The bars are different heights.')],
    fig=bars(['cold', 'warm', 'hot'], [2, 4, 7], 8, 1, 'Spoons of sugar dissolved', 'Water'), skill='Data'))
add(2, '2.4', sort('p3u02s4h01', 'O4', 'Can a filter separate each mixture?', ['yes', 'no'],
    [('sand and water', 'yes'), ('sugar dissolved in water', 'no'), ('rice and water', 'yes'), ('salt dissolved in water', 'no'), ('tea leaves and tea', 'yes')]))

add(3, '3.1', pic('p3u03s1h01', 'O1', 'A lamp is on the left of a toy tree. Where is the shadow of the tree?', ('On the right, away from the lamp', '➡️'),
    [('On the left, next to the lamp', '⬅️', 'A shadow forms on the side away from the light.'), ('There is no shadow', '🚫', 'The tree blocks the light, so there is a shadow.')]))
add(3, '3.2', pic('p3u03s2h01', 'O2', 'A puppet is moved away from a lamp. The shadow on the wall is measured. What does the table show?', ('The closer the puppet is to the lamp, the bigger the shadow', '🔦'),
    [('The closer the puppet is to the lamp, the smaller the shadow', '🤏', 'At 10 cm the shadow is the biggest.'), ('The shadow is always the same size', '🟰', 'The sizes are 30, 20 and 15 cm.')],
    data=[['Distance from the lamp', 'Height of the shadow'], ['10 cm', '30 cm'], ['20 cm', '20 cm'], ['30 cm', '15 cm']], skill='Data'))
add(3, '3.3', pic('p3u03s3h01', 'O3', 'A bus driver must see the road clearly but stay out of the wind and rain. Which material is best for the front window?', ('clear glass (transparent)', '🪟'),
    [('wood (opaque)', '🪵', 'You cannot see through wood.'), ('frosted glass (translucent)', '🌫️', 'You cannot see clearly through frosted glass.')]))
add(3, '3.4', pic('p3u03s4h01', 'O4', 'A bathroom window lets light in, but people outside cannot see clearly through it. What kind of material is it?', ('translucent', '🌫️'),
    [('transparent', '🪟', 'You can see clearly through transparent materials.'), ('opaque', '🚪', 'Opaque materials let no light through.')]))

add(4, '4.1', pairs('p3u04s1h01', 'O1', 'Match each organ to its job.', [('heart', 'pumps blood around the body'), ('lungs', 'take in air'), ('brain', 'controls the body'), ('stomach', 'breaks down food')]))
add(4, '4.2', seq('p3u04s2h01', 'O2', 'Put the life cycle of a sea turtle in order. Start with the egg.', ['an egg in the sand', 'a baby turtle hatches', 'the young turtle grows in the sea', 'the adult turtle lays eggs on the beach']))
add(4, '4.3', seq('p3u04s3h01', 'O3', 'Make a food chain. Start with the plant.', ['🍃 leaf', '🐛 caterpillar', '🐦 small bird', '🦅 hawk']))
add(4, '4.4', pic('p3u04s4h01', 'O4', 'A fossil shows a curled spiral shell. Part of it is missing. What kind of animal was it most likely to be?', ('a sea animal with a shell, like a snail', '🐚'),
    [('a bird', '🐦', 'Birds do not have spiral shells.'), ('a tree', '🌳', 'A tree is a plant and has no shell.')]))

add(5, '5.2', pic('p3u05s2h01', 'O2', 'People live all over the round Earth, even at the bottom of a globe. Why do they not fall off?', ('Gravity pulls everyone towards the centre of the Earth', '🌍'),
    [('The air holds them on', '💨', 'Gravity, not air, pulls us down.'), ('They hold on tightly', '✊', 'Nobody needs to hold on; gravity pulls everything towards the Earth.')]))
add(5, '5.3', pic('p3u05s3h01', 'O3', 'A child pulls the same shoe across four surfaces and measures the force. Look at the bar chart. Which surface has the most friction?', ('carpet', '🧶'),
    [('ice', '🧊', 'Ice needs the smallest force, so it has the least friction.'), ('wood', '🪵', 'Wood needs 3 N; another surface needs more.')],
    fig=bars(['ice', 'wood', 'grass', 'carpet'], [1, 3, 5, 6], 7, 1, 'Force to pull the shoe in N'), skill='Data'))
add(5, '5.4', pic('p3u05s4h01', 'O4', 'The ends of a magnet have no labels. One end is pushed away by the north pole of another magnet. What is that end?', ('a north pole', '🧲'),
    [('a south pole', '🔴', 'North and south pull together.'), ('not a pole at all', '❓', 'Only a pole of a magnet is pushed away.')]))
add(5, '5.5', sort('p3u05s5h01', 'O5', 'Will a magnet pull each object?', ['yes', 'no'],
    [('an iron nail', 'yes'), ('a plastic ruler', 'no'), ('a steel paperclip', 'yes'), ('an aluminium drinks can', 'no'), ('a wooden pencil', 'no')]))

add(6, '6.1', seq('p3u06s1h01', 'O1', 'Put these in order of size. Start with the smallest.', ['🌙 the Moon', '🌍 the Earth', '☀️ the Sun']))
add(6, '6.3',
  seq('p3u06s3h01', 'O3', 'Put the shapes of the Moon in order, starting with the new Moon.', ['🌑 new Moon', '🌒 thin crescent', '🌓 half Moon', '🌕 full Moon']),
  pic('p3u06s3h02', 'O3', 'Tonight there is a full Moon. About how long is it until the next full Moon?', ('about 4 weeks', '🗓️'),
      [('1 day', '☀️', 'The Moon changes shape slowly over many days.'), ('1 year', '🎂', 'A year is how long the Earth takes to go round the Sun.')]))
apply(3, B)

# =============================== STAGE 4 ===============================
B = {}
add(1, '1.1', pic('p4u01s1h01', 'O1', 'Mai measures the upper arm bone of four people in her family. Look at the bar chart. How much longer is Dad\'s bone than Mai\'s?', ('15 cm', '📏'),
    [('35 cm', '🦴', '35 cm is the length of Dad\'s bone.'), ('5 cm', '🤏', 'Take away: 35 − 20.')],
    fig=bars(['Mai', 'brother', 'Mum', 'Dad'], [20, 25, 30, 35], 40, 5, 'Length of bone in cm'), skill='Data'))
add(1, '1.3', pairs('p4u01s3h01', 'O3', 'Children make a model arm. Match each part of the model to the part of the body.', [('stretchy elastic band', 'muscle'), ('cardboard tube', 'bone'), ('split pin that lets the tubes turn', 'elbow joint')]))
add(1, '1.4', sort('p4u01s4h01', 'O4', 'Where is the skeleton of each animal?', ['inside the body', 'outside the body', 'no skeleton'],
    [('🐇 rabbit', 'inside the body'), ('🦀 crab', 'outside the body'), ('🐞 beetle', 'outside the body'), ('🐸 frog', 'inside the body'), ('🪱 earthworm', 'no skeleton')]))
add(1, '1.5', pic('p4u01s5h01', 'O5', 'Nam has a headache. He finds his mother\'s tablets and takes three. What should he have done?', ('Ask an adult, and only take medicine that is meant for him', '🧑‍⚕️'),
    [('Take more tablets to be sure', '💊', 'Too much medicine is dangerous.'), ('Share the tablets with a friend', '🤝', 'Never share medicines.')]))

add(2, '2.1', pairs('p4u02s1h01', 'O1', 'Match each thing to the main energy it gives out.', [('a drum being hit', 'sound'), ('a torch', 'light'), ('a hot kettle', 'heat'), ('a rolling ball', 'movement')]))
add(2, '2.2', pic('p4u02s2h01', 'O2', 'A bead is stuck to a metal spoon with butter. The spoon stands in water. Children time how long it takes for the bead to fall off. What does the bar chart show?', ('Hotter water makes the bead fall sooner, because heat travels along the spoon faster', '♨️'),
    [('Hotter water makes the bead stay on longer', '⏳', 'At 70 °C the time is the shortest.'), ('The water temperature makes no difference', '🟰', 'The times are 80, 40 and 20 seconds.')],
    fig=bars(['30 °C', '50 °C', '70 °C'], [80, 40, 20], 80, 10, 'Time for the bead to fall in s', 'Water temperature'), skill='Data'))
add(2, '2.3', pic('p4u02s3h01', 'O3', 'On a cold day you rub your hands together quickly and they feel warm. Which energy change is this?', ('movement energy to heat energy', '🙌'),
    [('light energy to sound energy', '💡', 'There is no light changing here.'), ('heat energy to movement energy', '🔥', 'It is the other way round.')]))
add(2, '2.4', seq('p4u02s4h01', 'O4', 'Show how energy passes along this food chain. Start with where the energy comes from.', ['☀️ Sun', '🌾 grass', '🦌 deer', '🐅 tiger']))

add(3, '3.1', pic('p4u03s1h01', 'O1', 'Which picture in your mind shows the particles in a solid?', ('Very close together in neat rows', '🧱'),
    [('Close together but sliding past each other', '💧', 'That is a liquid.'), ('Far apart and moving everywhere', '💨', 'That is a gas.')]))
add(3, '3.2', pic('p4u03s2h01', 'O2', 'Children time how long sand takes to flow through a funnel. Look at the bar chart. How long would 400 ml of sand take?', ('about 40 s', '⏱️'),
    [('about 20 s', '⌛', '20 s is the time for 200 ml.'), ('about 5 s', '⚡', '5 s is the time for 50 ml.')],
    fig=bars(['50 ml', '100 ml', '200 ml'], [5, 10, 20], 20, 5, 'Time in s', 'Volume of sand'), skill='Data'))
add(3, '3.3', pic('p4u03s3h01', 'O3', 'An ice cube is put into water at different temperatures. What does the table show?', ('The hotter the water, the faster the ice melts', '🔥'),
    [('The colder the water, the faster the ice melts', '❄️', 'In the coldest water it took the longest.'), ('Ice melts in the same time in all the cups', '🟰', 'The times are 12, 6 and 2 minutes.')],
    data=[['Water temperature', 'Time for the ice to melt'], ['10 °C', '12 minutes'], ['30 °C', '6 minutes'], ['50 °C', '2 minutes']], skill='Data'))
add(3, '3.4', pic('p4u03s4h01', 'O4', 'Three iron nails are left for a week. Nail A is in water and air. Nail B is in dry air. Nail C is under oil with no air. Only nail A goes rusty. What does iron need to rust?', ('both water and air', '💧'),
    [('only oil', '🛢️', 'The nail in oil did not rust.'), ('only dry air', '🌬️', 'The nail in dry air did not rust.')]))

add(4, '4.1', pic('p4u04s1h01', 'O1', 'Nobody has ever been to the centre of the Earth. How do scientists know what it is like inside?', ('They study how earthquake waves travel through the Earth', '📈'),
    [('They dig a hole to the centre', '⛏️', 'It is far too deep and hot to dig.'), ('They look with a telescope', '🔭', 'A telescope cannot see through rock.')]))
add(4, '4.2', seq('p4u04s2h01', 'O2', 'Put the steps of a volcano erupting in order.', ['hot magma rises under the volcano', 'the pressure builds up', 'lava, ash and gas burst out', 'the lava cools and becomes new rock']))
add(4, '4.3', pic('p4u04s3h01', 'O3', 'A town is in a place with many earthquakes. Which building is the safest?', ('A building with a strong frame that can bend a little', '🏢'),
    [('A tall building made of loose bricks', '🧱', 'Loose bricks fall when the ground shakes.'), ('A building with a heavy roof on thin walls', '🏚️', 'A heavy roof can fall in.')]))
add(4, '4.4', pic('p4u04s4h01', 'O4', 'Giraffes live on grassland with tall trees. How does a long neck help a giraffe to stay alive?', ('It can reach leaves that other animals cannot', '🦒'),
    [('It helps it to swim', '🏊', 'Giraffes live on dry grassland.'), ('It keeps it warm at night', '🧣', 'A long neck does not keep it warm.')]))

add(5, '5.1', pic('p4u05s1h01', 'O1', 'A box is inside a cupboard with the door shut. It is completely dark. Why can you not see the box?', ('No light bounces off the box into your eyes', '👁️'),
    [('Your eyes stop working in the dark', '😴', 'Your eyes still work; there is no light for them.'), ('The box is not there in the dark', '📦', 'The box is still there.')]))
add(5, '5.2', pic('p4u05s2h01', 'O2', 'You sit under a table. A friend puts a cup on top of the table. Why can you not see the cup?', ('Light travels in straight lines and cannot bend around the table', '➡️'),
    [('The cup gives out no light', '☕', 'We see most things by light that bounces off them.'), ('It is too far away', '🔭', 'It is very close; the table is in the way.')]))
add(5, '5.3', seq('p4u05s3h01', 'O3', 'A driver sees a car behind her in the mirror. Put the path of the light in order.', ['light from the Sun hits the car behind', 'the light bounces off the car', 'the light hits the mirror', 'the mirror reflects the light into the driver\'s eyes']))
add(5, '5.5', pic('p4u05s5h01', 'O5', 'A day is the time a planet takes to spin once. Use the table. Which planet has the shortest day?', ('Jupiter', '🟠'),
    [('Earth', '🌍', 'Earth takes 24 hours; another planet is faster.'), ('Venus', '🟡', 'Venus spins very slowly, so its day is the longest.')],
    data=[['Planet', 'Time to spin once'], ['Earth', '24 hours'], ['Jupiter', '10 hours'], ['Venus', '5832 hours']], skill='Data'))
add(5, '5.6', pic('p4u05s6h01', 'O6', 'The shadow of a tree is measured all day. When is the shadow shortest?', ('In the middle of the day, when the Sun is highest', '☀️'),
    [('Early in the morning', '🌅', 'The Sun is low then, so shadows are long.'), ('Late in the evening', '🌇', 'The Sun is low then, so shadows are long.')]))

add(6, '6.1', pic('p4u06s1h01', 'O1', 'You build a circuit with a gap to test if objects conduct electricity. What should you do first?', ('Touch the two loose wires together to check the lamp lights', '💡'),
    [('Test a plastic spoon', '🥄', 'First make sure the circuit works.'), ('Take out the battery', '🔋', 'Without the battery nothing will light.')]))
add(6, '6.2', pic('p4u06s2h01', 'O2', 'After a long run, Bao is wet with sweat. Why must he dry his hands before he touches a plug or a switch?', ('Water on the skin lets electricity pass into the body easily', '⚡'),
    [('Wet hands make the fan slower', '🌀', 'The danger is an electric shock.'), ('Sweat can break the plug', '🔌', 'The danger is to Bao, not to the plug.')]))
add(6, '6.3', pic('p4u06s3h01', 'O3', 'Thick cables carry electricity on tall metal towers. The cables hang from glass or ceramic discs. Why?', ('Glass and ceramic are insulators, so electricity cannot flow into the tower', '🗼'),
    [('Glass and ceramic are good conductors', '🔗', 'They are insulators.'), ('The discs make the electricity stronger', '💪', 'They only keep it in the cable.')]))
add(6, '6.5', pic('p4u06s5h01', 'O5', 'A lamp in a circuit is dim. Which change makes it brighter?', ('Add another battery', '🔋'),
    [('Add another lamp in the same loop', '💡', 'More lamps in one loop make each lamp dimmer.'), ('Open the switch', '🔘', 'An open switch stops the electricity.')]))
apply(4, B)
