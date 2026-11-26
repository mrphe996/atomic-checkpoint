# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 6 · Unit 3 Rocks, the rock cycle and soil. Written by the Camday teaching team."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kit6 import *
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'build', 'p6'))

OBJ = {
 'O1': {'sec': '3.1', 'code': 'Earth and space', 'codeNote': '', 't': 'Describe how igneous rocks form from magma and lava, and link crystal size to how fast the rock cooled.'},
 'O2': {'sec': '3.1', 'code': 'Working scientifically', 'codeNote': '', 't': 'Use a simple key and observations to identify rocks.'},
 'O3': {'sec': '3.2', 'code': 'Earth and space', 'codeNote': '', 't': 'Describe weathering, erosion and sedimentation, and how sedimentary rocks and fossils form.'},
 'O4': {'sec': '3.3', 'code': 'Earth and space', 'codeNote': '', 't': 'Describe how heat and pressure form metamorphic rocks, and describe the rock cycle.'},
 'O5': {'sec': '3.3', 'code': 'Science in context', 'codeNote': '', 't': 'Link the uses of rocks to their properties.'},
 'O6': {'sec': '3.4', 'code': 'Earth and space', 'codeNote': '', 't': 'Describe what soil is made of and compare sandy soil, clay soil and loam.'},
 'O7': {'sec': '3.4', 'code': 'Working scientifically', 'codeNote': '', 't': 'Carry out a fair test of how well soils drain, and describe how people can improve or harm soil.'},
}
U = Unit(3, 'Rocks, the rock cycle and soil', 'Earth and space: planet Earth', 'How igneous, sedimentary and metamorphic rocks form, how rocks keep changing, and what soil is made of.', OBJ)
from vocab_u3 import V, SAY as SAYW
core = core_for(V, SAYW)

# =====================================================================================  3.1
s = U.section('3.1', 'Igneous rocks', ['O1', 'O2']); s.words(V['3.1']); core(s, 'O1', 'O1')
s.stop(MC('What is lava?', 'Magma that has reached the Earth\'s surface', [('Rock that has never melted', 'Lava is melted rock.'), ('Hot water from a spring', 'Lava is melted rock, not water.'), ('Melted rock deep underground', 'Underground it is called magma.')], o='O1'),
       MC('What do we call melted rock under the ground?', 'Magma', [('Lava', 'Lava is on the surface.'), ('Sediment', 'Sediment is bits of broken rock.')], o='O1'))
s.stop(MC('Why does granite have big crystals?', 'It cooled slowly, deep underground, so the crystals had time to grow', [('It cooled quickly on the surface', 'Quick cooling makes small crystals.'), ('It was squashed by pressure', 'That makes metamorphic rock.'), ('It was made from shells', 'That is limestone.')], o='O1'),
       MC('Basalt formed when lava cooled quickly. What are its crystals like?', 'Very small', [('Very big', 'Big crystals need slow cooling.'), ('There are no crystals at all', 'Igneous rocks are made of crystals – in basalt they are tiny.')], o='O1'))
s.prac(
 OD('Put the layers of the Earth in order, from the outside in.', ['crust', 'mantle', 'core'], o='O1'),
 MC('Where do we live?', 'On the crust', [('In the mantle', 'The mantle is below the crust.'), ('In the core', 'The core is the centre of the Earth.')], o='O1'),
 MT('Match each word to its meaning.', [('magma', 'melted rock under the ground'), ('lava', 'melted rock on the surface'), ('solidification', 'a liquid cooling and becoming solid'), ('volcano', 'an opening where lava comes out')], o='O1'),
 MC('What does "igneous" mean?', 'Made from fire', [('Made from water', 'Igneous rocks form from melted rock.'), ('Made from shells', 'That describes some limestone.')], o='O1'),
 MC('How does igneous rock form?', 'Magma or lava cools and becomes solid', [('Layers of sediment are squashed', 'That makes sedimentary rock.'), ('Rock is heated and squeezed without melting', 'That makes metamorphic rock.')], o='O1'),
 TK('Tick the properties of most igneous rocks.', ['True', 'False'], [('made of crystals that fit tightly', ['✓', '✗']), ('hard', ['✓', '✗']), ('lets water soak in easily', ['✗', '✓']), ('contains fossils', ['✗', '✓'])], o='O1'),
 GD('Is each rock intrusive (cooled underground) or extrusive (cooled on the surface)?', 'Type', [('granite', 'intrusive'), ('basalt', 'extrusive'), ('pumice', 'extrusive')], o='O1'),
 CZ('Complete the sentences.', 'Slow cooling makes {0} crystals. Quick cooling makes {1} crystals.', [['big', 'large'], ['small', 'tiny']], o='O1'),
 MC('Why can pumice float on water?', 'It is full of gas holes, so it is very light', [('It is made of wood', 'Pumice is a rock.'), ('It is hot', 'Cold pumice still floats.')], o='O1'),
 MC('What does a geologist study?', 'Rocks and the Earth', [('Stars and planets', 'That is an astronomer.'), ('Animals', 'That is a zoologist.')], o='O2'),
 MC('Using the key: "Can you see the crystals with your naked eye? Yes → granite. No → basalt." A rock has crystals you cannot see. What is it?', 'Basalt', [('Granite', 'Granite has crystals you can see.'), ('Pumice', 'Pumice is not in this key.')], o='O2'),
 MC('What does "with the naked eye" mean?', 'Without a microscope or magnifying glass', [('With your eyes closed', 'You need to look!'), ('Using a microscope', 'That is the opposite.')], o='O2'),
 MS('Select the things that help you identify a rock.', ['the size of its crystals', 'its colour', 'whether it has grains or layers'], ['how old the person holding it is', 'what day it is'], o='O2'),
 MT('Match each igneous rock to its use.', [('granite', 'kitchen tops and buildings'), ('crushed basalt', 'making roads'), ('pumice', 'rubbing hard skin off feet')], o='O2'),
 MC('Why is granite good for steps and kitchen tops?', 'It is hard and does not wear away easily', [('It is soft and bendy', 'Granite is hard.'), ('It soaks up water', 'Granite does not let water through.')], o='O2'),
 MC('A rock has big pink, white and black crystals. What is it most likely to be?', 'Granite', [('Basalt', 'Basalt is dark with tiny crystals.'), ('Sandstone', 'Sandstone has grains, not crystals.')], o='O2', d='H'),
 OD('Put the steps in order to show how an extrusive igneous rock forms.', ['rock melts in the mantle to make magma', 'magma rises up through the crust', 'lava comes out of a volcano', 'lava cools quickly and becomes solid'], o='O1'),
 MC('Which is the hottest?', 'Magma deep in the Earth', [('A cooled lump of basalt', 'It has already cooled.'), ('A granite kitchen top', 'It is at room temperature.')], o='O1'),
)
s.adv(
 EX('Explain why basalt has small crystals but granite has big crystals.', [('basalt cooled quickly on the surface', ['quick', 'fast', 'surface']), ('granite cooled slowly underground', ['slow', 'underground', 'deep']), ('crystals need time to grow', ['time', 'grow'])], 'Basalt formed from lava that cooled quickly on the surface, so its crystals had no time to grow. Granite cooled slowly underground, so its crystals grew big.', o='O1', d='H'),
 TB('A class measured crystal sizes in three rocks. For each one, write "slow" or "fast" for the cooling.', ['Rock', 'Biggest crystal (mm)', 'Cooling'], [['A', '12', B('slow')], ['B', '0.1', B('fast')], ['C', '8', B('slow')]], o='O1', d='H', reason='Big crystals = slow cooling; tiny crystals = fast cooling.'),
 MC('Salol (a chemical) is melted. One drop cools on a cold slide, one on a warm slide. Which forms bigger crystals?', 'The drop on the warm slide', [('The drop on the cold slide', 'Cold makes it cool quickly – small crystals.'), ('Both the same', 'Cooling speed changes crystal size.')], o='O1', d='VH'),
 MC('Why are there no fossils in igneous rocks?', 'Living things would be destroyed by the melted rock', [('Igneous rocks are too new', 'Some are very old.'), ('Fossils only form in the sea', 'Fossils form in sediment, not in melted rock.')], o='O1', d='H'),
)
s.labs('Crystal lab',
 {'kind': 'test', 'title': 'How does cooling speed change crystal size?', 'intro': 'Melted rock cools at different speeds. Use the scale to measure the biggest crystal in each rock.',
  'change': 'How fast the rock cooled', 'measure': 'Biggest crystal', 'unit': 'mm', 'max': 12, 'step': 1, 'instr': '🔍',
  'conds': [{'k': 'deep', 't': 'Very slow (deep underground)', 'emoji': '⛰️', 'val': 10}, {'k': 'mid', 't': 'Slow (just under the surface)', 'emoji': '🪨', 'val': 4}, {'k': 'fast', 't': 'Fast (lava on the surface)', 'emoji': '🌋', 'val': 0.5}],
  'qs': [MC('What happens to crystal size as cooling gets slower?', 'The crystals get bigger', [('The crystals get smaller', 'Look at your table again.'), ('Nothing changes', 'The sizes are very different.')], o='O1'),
         MC('Which rock in the lab is most like granite?', 'The one that cooled very slowly deep underground', [('The lava rock', 'That is more like basalt.'), ('None of them', 'Granite has big crystals.')], o='O1')]},
 {'title': 'Make crystals at home', 'intro': 'Grow sugar or salt crystals in a warm place and in a cold place and compare their size.',
  'need': ['2 jars or cups', 'warm water (from the tap)', 'salt or sugar', 'a spoon', 'a magnifying glass if you have one', 'a ruler with millimetres'],
  'safety': ['Use warm tap water, not boiling water.', 'Do not eat or drink your experiment.'],
  'steps': ['Stir salt into a cup of warm water until no more will dissolve.', 'Pour half into a second cup.', 'Put one cup somewhere warm and one in the fridge for 3 days.', 'Measure the biggest crystal in each cup in millimetres.'],
  'record': {'head': ['Place', 'Biggest crystal (mm)'], 'rows': [['Warm place (slow)', {'min': 0, 'max': 50}], ['Fridge (fast)', {'min': 0, 'max': 50}]], 'hint': 'Crystals are usually 0.5 to 10 mm.'},
  'qs': [MC('Which place made bigger crystals in most tests?', 'The warm place, where the water evaporated slowly', [('The fridge', 'Slower crystal growth gives bigger crystals.'), ('Always the same', 'Compare your measurements.')], o='O1', d='H')]})

# =====================================================================================  3.2
s = U.section('3.2', 'Sedimentary rocks and fossils', ['O3']); s.words(V['3.2']); core(s, 'O3', 'O3')
s.stop(OD('Put the steps in order.', ['weathering', 'erosion', 'sedimentation'], o='O3', reason='First rock is broken (weathering), then carried away (erosion), then it settles in layers (sedimentation).'),
       MC('What is erosion?', 'Broken pieces of rock being carried away', [('Rock breaking into pieces', 'That is weathering.'), ('Sediment settling in layers', 'That is sedimentation.')], o='O3'))
s.stop(MC('In which type of rock do we find fossils?', 'Sedimentary rock', [('Igneous rock', 'Melted rock destroys living things.'), ('Metamorphic rock', 'Heat and pressure usually destroy fossils.')], o='O3'),
       MC('Which parts of an animal usually become fossils?', 'Hard parts like bones, teeth and shells', [('Soft parts like skin', 'Soft parts rot away.'), ('Only the eyes', 'Eyes are soft.')], o='O3'))
s.prac(
 MS('Select the things that can cause weathering.', ['rain', 'ice', 'plant roots', 'changes in temperature'], ['moonlight', 'music'], o='O3'),
 MT('Match each word to its meaning.', [('weathering', 'rock breaking into smaller pieces'), ('erosion', 'pieces being carried away'), ('sedimentation', 'sediment settling in layers'), ('sediment', 'bits of rock, sand and mud')], o='O3'),
 MC('Why do pebbles in a river become round?', 'They bump and rub together as the water carries them', [('Fish chew them', 'Fish do not shape pebbles.'), ('They melt', 'Pebbles do not melt in rivers.')], o='O3'),
 MC('Where does sediment settle?', 'Where the water slows down, like in a lake or the sea', [('At the top of a waterfall', 'Fast water keeps carrying sediment.'), ('Inside a volcano', 'That is where magma is.')], o='O3'),
 OD('Put the steps in order to show how sedimentary rock forms.', ['rock is weathered into small pieces', 'rivers carry the pieces away', 'the sediment settles in layers', 'the layers are squashed and stick together'], o='O3'),
 CZ('Complete the sentences.', 'Layers of {0} build up over millions of years. The top layers {1} the bottom layers, and they stick together to form {2} rock.', [['sediment'], ['squash', 'squeeze', 'press'], ['sedimentary']], o='O3'),
 MT('Match each sedimentary rock to what it is made of.', [('sandstone', 'sand grains stuck together'), ('shale', 'mud'), ('limestone', 'tiny shells')], o='O3'),
 TK('Tick the properties of most sedimentary rocks.', ['True', 'False'], [('has layers', ['✓', '✗']), ('made of grains', ['✓', '✗']), ('many let water soak in', ['✓', '✗']), ('made of big shiny crystals', ['✗', '✓'])], o='O3'),
 GD('Is each rock igneous or sedimentary?', 'Type', [('granite', 'igneous'), ('sandstone', 'sedimentary'), ('basalt', 'igneous'), ('limestone', 'sedimentary')], o='O3'),
 MC('What is a fossil?', 'The remains or trace of a living thing from long ago, kept in rock', [('A rock made by a volcano', 'That is an igneous rock.'), ('A very old living animal', 'Fossils are not alive.')], o='O3'),
 OD('Put the steps of fossil formation in order.', ['an animal dies', 'it is quickly covered by sediment', 'the soft parts rot away', 'minerals replace the bones and they turn to stone'], o='O3'),
 MC('Why must an animal be covered quickly to become a fossil?', 'So it is not eaten or rotted away first', [('So it stays warm', 'That is not the reason.'), ('So it can keep growing', 'The animal has died.')], o='O3'),
 MC('In the jar model, which pieces sink first?', 'The heaviest pieces, like gravel', [('The lightest pieces, like soil', 'They sink last.'), ('They all sink at the same time', 'They settle in layers.')], o='O3'),
 MC('In the jar model, what does the layering show us?', 'How layers form in sedimentary rock', [('How lava cools', 'That is igneous rock.'), ('How fossils are dug up', 'It is about how layers build up.')], o='O3'),
 MC('In a cliff, which layer is usually the oldest?', 'The bottom layer', [('The top layer', 'The top layer was put down last.'), ('The middle layer', 'Layers build up from the bottom.')], o='O3', d='H'),
 MC('Which of these could make a fossil footprint?', 'A dinosaur walking on soft mud that later became rock', [('A dinosaur walking on hard granite', 'Hard rock does not keep footprints.'), ('A bird flying overhead', 'It must touch the mud.')], o='O3', d='H'),
 MC('What do fossils tell us?', 'What living things were like long ago', [('What the weather is tomorrow', 'Fossils tell us about the past.'), ('How to make rocks', 'They tell us about life long ago.')], o='O3'),
 MC('How long does it take for sedimentary rock to form?', 'Millions of years', [('A few days', 'Much longer.'), ('About one year', 'Much longer.')], o='O3'),
)
s.adv(
 EX('Explain how a shell on the sea bed can become a fossil in limestone.', [('the shell is covered by sediment', ['sediment', 'covered', 'buried']), ('layers build up and squash it', ['layer', 'squash', 'pressure', 'press']), ('minerals replace the shell / it turns to stone', ['mineral', 'stone', 'rock'])], 'The shell is buried by sediment. More layers build up and squash it, and over millions of years minerals replace the shell and it turns to stone.', o='O3', d='H'),
 TB('Kim shook a jar of mixed sediment and measured the layers after it settled. Complete the total.', ['Layer', 'Thickness (cm)'], [['gravel (bottom)', '3'], ['sand', '4'], ['soil (top)', '2'], ['total', B(9)]], o='O3', d='M', skill='Data'),
 MC('Kim\'s layers were gravel at the bottom, then sand, then soil on top. Why?', 'The biggest, heaviest pieces sank first', [('Soil is heaviest', 'Soil settled last, so it is lightest.'), ('She put them in that order', 'She shook them all together first.')], o='O3', d='H'),
 MC('A fossil fish is found high up a mountain. What does it suggest?', 'The rock formed under water long ago', [('Fish once climbed mountains', 'Fish cannot climb.'), ('It fell from a plane', 'Fossils form inside rock.')], o='O3', d='VH'),
)
s.labs('Layers lab',
 {'kind': 'sort', 'title': 'Weathering, erosion or sedimentation?', 'intro': 'Sort each card into the right part of the story of sedimentary rock.',
  'groups': ['Weathering (breaking)', 'Erosion (carrying away)', 'Sedimentation (settling)'],
  'items': [{'t': 'ice cracks a rock', 'emoji': '🧊', 'g': 0, 'why': 'Ice breaking rock is weathering.'}, {'t': 'a river carries pebbles', 'emoji': '🏞️', 'g': 1, 'why': 'Moving pieces away is erosion.'},
            {'t': 'mud settles in a lake', 'emoji': '🏝️', 'g': 2, 'why': 'Settling is sedimentation.'}, {'t': 'roots split a rock', 'emoji': '🌳', 'g': 0, 'why': 'Roots break rock – weathering.'},
            {'t': 'wind blows sand across a desert', 'emoji': '🌬️', 'g': 1, 'why': 'Wind carrying sand is erosion.'}, {'t': 'sand sinks to the sea bed', 'emoji': '🌊', 'g': 2, 'why': 'Sinking and settling is sedimentation.'},
            {'t': 'hot days and cold nights crack a rock', 'emoji': '🌡️', 'g': 0, 'why': 'Temperature changes cause weathering.'}],
  'qs': [MC('Which comes first?', 'Weathering', [('Erosion', 'Rock must be broken before it is carried.'), ('Sedimentation', 'That is the last step.')], o='O3'),
         MC('What can carry sediment away?', 'Rivers, wind and ice', [('Only the Sun', 'Moving water, wind and ice carry it.'), ('Nothing', 'Erosion carries it.')], o='O3')]},
 {'title': 'Sediment in a jar', 'intro': 'Make your own layers, like sedimentary rock.',
  'need': ['a clear jar with a lid', 'a handful each of gravel or small stones, sand and garden soil', 'water', 'a ruler'],
  'safety': ['Wash your hands after handling soil.', 'Make sure the lid is tight before shaking.'],
  'steps': ['Put the gravel, sand and soil into the jar.', 'Fill the jar almost to the top with water and close the lid tightly.', 'Shake it well, then leave it to settle for one day.', 'Measure the thickness of each layer in centimetres.'],
  'record': {'head': ['Layer', 'Thickness (cm)'], 'rows': [['Bottom layer', {'min': 0.2, 'max': 20}], ['Middle layer', {'min': 0.2, 'max': 20}], ['Top layer', {'min': 0.2, 'max': 20}]], 'hint': 'Layers are usually 1 to 6 cm thick.'},
  'qs': [MC('What was in the bottom layer?', 'The gravel – the heaviest pieces', [('The soil', 'Fine soil settles last.'), ('Nothing settled', 'Look again after a day.')], o='O3')]})

# =====================================================================================  3.3
s = U.section('3.3', 'Metamorphic rocks and the rock cycle', ['O4', 'O5']); s.words(V['3.3']); core(s, 'O4', 'O4')
s.stop(MC('What two things change rocks into metamorphic rocks?', 'Heat and pressure', [('Wind and rain', 'They cause weathering.'), ('Water and sunlight', 'These do not make metamorphic rock.'), ('Melting and cooling', 'That makes igneous rock.')], o='O4'),
       MC('Limestone is heated and squeezed. What does it become?', 'Marble', [('Slate', 'Slate comes from shale.'), ('Granite', 'Granite is igneous.')], o='O4'))
s.stop(MC('What happens when a metamorphic rock melts?', 'It becomes magma, which can cool to make igneous rock', [('It becomes sedimentary rock straight away', 'Melting makes magma.'), ('It turns into soil', 'Soil comes from weathering.'), ('Nothing – it cannot melt', 'Any rock can melt if hot enough.')], o='O4'),
       MC('In the rock cycle, what does sediment become?', 'Sedimentary rock', [('Magma', 'Sediment is squashed, not melted.'), ('Metamorphic rock straight away', 'First it becomes sedimentary rock.')], o='O4'))
s.prac(
 MC('What does "metamorphic" mean?', 'Changed in shape', [('Made from fire', 'That is igneous.'), ('Made in layers', 'That describes sedimentary rock.')], o='O4'),
 MC('When a rock becomes metamorphic, does it melt?', 'No – its crystals change and line up, but it does not melt', [('Yes – it melts completely', 'If it melted it would become magma.'), ('Yes – but only a little', 'It does not melt.')], o='O4'),
 MT('Match each rock to the metamorphic rock it can become.', [('limestone', 'marble'), ('shale', 'slate'), ('granite', 'gneiss')], o='O4'),
 GD('Is each rock igneous, sedimentary or metamorphic?', 'Type', [('marble', 'metamorphic'), ('sandstone', 'sedimentary'), ('basalt', 'igneous'), ('slate', 'metamorphic'), ('shale', 'sedimentary')], o='O4'),
 MC('What is the rock cycle?', 'Rocks slowly changing from one type to another, again and again', [('Rocks rolling down a hill', 'That is not the rock cycle.'), ('A bicycle made of rock', 'It is about rocks changing type.')], o='O4'),
 OD('Follow the rock cycle from igneous rock.', ['igneous rock is weathered and eroded', 'sediment settles and becomes sedimentary rock', 'buried rock is heated and squeezed into metamorphic rock', 'the rock melts into magma, which cools into igneous rock'], o='O4'),
 CZ('Complete the sentences.', 'Melted rock is called {0}. When it cools it makes {1} rock. Heat and {2} make metamorphic rock.', [['magma'], ['igneous'], ['pressure']], o='O4'),
 MC('How long does the rock cycle take?', 'Millions of years', [('A few weeks', 'Much, much longer.'), ('About 100 years', 'Much longer.')], o='O4'),
 MC('In the crayon model, what does grating the crayons show?', 'Weathering', [('Melting', 'Melting shows how magma forms.'), ('Pressure', 'Pressing hard shows pressure.')], o='O4'),
 MT('Match each step of the crayon model to the rock cycle.', [('grating into shavings', 'weathering'), ('pressing shavings together', 'forming sedimentary rock'), ('warming and pressing hard', 'forming metamorphic rock'), ('melting and cooling', 'forming igneous rock')], o='O4'),
 MC('Why is slate used for roofs?', 'It splits into thin, flat sheets and does not let water through', [('It is soft and soaks up rain', 'A roof must keep rain out.'), ('It is very light, like pumice', 'Slate is chosen because it splits flat.')], o='O5'),
 MC('Why is marble used for statues?', 'It is beautiful and can be carved', [('It is very soft and squashy', 'Marble is hard but can be carved.'), ('It floats', 'Marble does not float.')], o='O5'),
 MT('Match each rock to a use.', [('slate', 'roof tiles'), ('marble', 'statues and floors'), ('granite', 'steps and kitchen tops'), ('limestone', 'building walls')], o='O5'),
 MC('Why do builders choose a rock for a job?', 'Because of its properties, such as hardness or how it splits', [('Because of its name', 'Properties matter, not names.'), ('Because it is the cheapest colour', 'It is about properties.')], o='O5'),
 MC('Which property makes granite good for steps?', 'It is very hard and wears away slowly', [('It splits into thin sheets', 'That is slate.'), ('It soaks up water', 'That would be bad for steps.')], o='O5'),
 MC('Why might a limestone statue wear away faster than a granite one?', 'Limestone is softer and is worn away by rain', [('Limestone is harder', 'Granite is harder.'), ('Granite is newer', 'It is about hardness.')], o='O5', d='H'),
 MC('Gneiss has stripes of crystals. Why?', 'Pressure made the crystals line up', [('It was painted', 'The stripes are natural.'), ('It cooled on the surface', 'It formed deep underground.')], o='O4', d='H'),
 MC('Where do metamorphic rocks form?', 'Deep underground, where it is hot and the pressure is high', [('On the sea bed, in mud', 'That is where sediment settles.'), ('In the air', 'Rocks form in the Earth.')], o='O4'),
)
s.adv(
 EX('Describe how a piece of granite could become part of a sandstone rock.', [('granite is weathered into grains', ['weather', 'break']), ('the grains are carried away (erosion)', ['erosion', 'carried', 'river']), ('they settle and are squashed into sandstone', ['settle', 'layer', 'squash', 'sediment'])], 'The granite is weathered into small grains, which rivers carry away (erosion). The grains settle in layers and are squashed together to form sandstone.', o='O4', d='H'),
 MC('Which path is NOT part of the rock cycle?', 'Metamorphic rock turns directly into sediment without being weathered', [('Igneous rock is weathered into sediment', 'This is part of the cycle.'), ('Sedimentary rock is heated and squeezed', 'This makes metamorphic rock.'), ('Magma cools to make igneous rock', 'This is part of the cycle.')], o='O4', d='VH'),
 TB('A builder tested three rocks by scratching them with a steel nail. Complete the table.', ['Rock', 'Scratched by the nail?', 'Good for steps? (yes or no)'], [['granite', 'no', B('yes')], ['chalk', 'yes', B('no')], ['marble', 'only a little', 'quite good']], o='O5', d='H', reason='A rock that a nail cannot scratch is hard-wearing, so it is good for steps.'),
 MC('Why are there very few fossils in metamorphic rocks?', 'Heat and pressure usually destroy them', [('Animals never lived there', 'The rock may once have been sedimentary.'), ('Metamorphic rocks form in the sky', 'They form underground.')], o='O4', d='H'),
)
s.labs('Rock cycle lab',
 {'kind': 'sort', 'title': 'Sort the rocks', 'intro': 'Sort each rock into its type: igneous, sedimentary or metamorphic.',
  'groups': ['Igneous', 'Sedimentary', 'Metamorphic'],
  'items': [{'t': 'granite', 'emoji': '🪨', 'g': 0, 'why': 'Granite forms from cooled magma.'}, {'t': 'basalt', 'emoji': '⬛', 'g': 0, 'why': 'Basalt forms from cooled lava.'},
            {'t': 'sandstone', 'emoji': '🟫', 'g': 1, 'why': 'Sandstone is sand grains stuck together.'}, {'t': 'limestone', 'emoji': '🐚', 'g': 1, 'why': 'Limestone is made from shells and sediment.'},
            {'t': 'marble', 'emoji': '🗿', 'g': 2, 'why': 'Marble is limestone changed by heat and pressure.'}, {'t': 'slate', 'emoji': '🏠', 'g': 2, 'why': 'Slate is shale changed by heat and pressure.'},
            {'t': 'shale', 'emoji': '📚', 'g': 1, 'why': 'Shale is made from mud.'}, {'t': 'pumice', 'emoji': '🧽', 'g': 0, 'why': 'Pumice is frothy lava that cooled fast.'}],
  'qs': [MC('Which rock type forms from melted rock?', 'Igneous', [('Sedimentary', 'That forms from sediment.'), ('Metamorphic', 'That forms from heat and pressure without melting.')], o='O4'),
         MC('Which rocks are changed forms of sedimentary rocks?', 'Marble and slate', [('Granite and basalt', 'They are igneous.'), ('Sandstone and shale', 'They are sedimentary themselves.')], o='O4')]},
 {'title': 'Rock hunt', 'intro': 'Look for rocks used around your home and street, and think about why each one was chosen.',
  'need': ['a notebook or the table below', 'an adult to go with you'],
  'safety': ['Stay with an adult and away from roads.', 'Do not climb walls or roofs.'],
  'steps': ['Look for stone floors, steps, walls, roofs, kitchen tops or statues.', 'Guess the rock: granite (crystals), marble (smooth, swirly), slate (thin dark sheets), sandstone or limestone (grainy).', 'Count how many things you find made of each rock.', 'Think about why that rock was chosen.'],
  'record': {'head': ['Rock', 'Number of things I found'], 'rows': [['Granite', {'min': 0, 'max': 100}], ['Marble', {'min': 0, 'max': 100}], ['Slate', {'min': 0, 'max': 100}], ['Sandstone or limestone', {'min': 0, 'max': 100}]], 'hint': 'Write 0 if you did not find any.'},
  'qs': [MC('Why are kitchen tops often made of granite?', 'It is hard and does not soak up water', [('It is soft and easy to scratch', 'Granite is hard.'), ('It is light enough to float', 'That is pumice.')], o='O5')]})

# =====================================================================================  3.4
s = U.section('3.4', 'Soil', ['O6', 'O7']); s.words(V['3.4']); core(s, 'O6', 'O6')
s.stop(MC('Which soil is best for most plants?', 'Loam', [('Sandy soil', 'It dries out too quickly.'), ('Clay soil', 'It can become waterlogged.'), ('Gravel', 'Gravel holds very little water or nutrients.')], o='O6'),
       MC('What is loam made of?', 'A mixture of sand, clay and humus', [('Only sand', 'That is sandy soil.'), ('Only clay', 'That is clay soil.')], o='O6'))
s.stop(MC('What does compost add to soil?', 'Humus and nutrients that help plants grow', [('Plastic', 'Compost is made from rotted plants.'), ('Pesticides', 'Compost is natural.'), ('Sand only', 'Compost adds humus.')], o='O7'),
       MC('What can too much artificial fertiliser do?', 'Harm living things in the soil and in rivers', [('Make soil into rock', 'It does not do that.'), ('Nothing at all', 'Too much can cause harm.')], o='O7'))
s.prac(
 MS('Select what soil is made of.', ['tiny pieces of weathered rock', 'humus', 'air', 'water'], ['plastic', 'metal'], o='O6'),
 MC('Where does humus come from?', 'Dead and rotting plants and animals', [('Melted rock', 'That is magma.'), ('The air', 'Humus is organic matter.')], o='O6'),
 MT('Match each soil to its description.', [('sandy soil', 'big grains; water drains quickly'), ('clay soil', 'tiny grains; sticky; holds water'), ('loam', 'a mix of sand, clay and humus')], o='O6'),
 GD('Which soil is each one?', 'Soil', [('dries out fast after rain', 'sandy soil'), ('can become waterlogged', 'clay soil'), ('best for most plants', 'loam')], o='O6'),
 MC('What does "waterlogged" mean?', 'So full of water that air cannot get in', [('Completely dry', 'That is the opposite.'), ('Made of logs', 'It is about too much water.')], o='O6'),
 MC('Why does water drain quickly through sandy soil?', 'The big grains leave big gaps for water to pass through', [('Sand is sticky', 'Clay is sticky.'), ('Sand soaks up all the water', 'Water passes straight through.')], o='O6'),
 CZ('Complete the sentence.', 'Soil is made of weathered {0} mixed with {1}, air and water.', [['rock', 'rocks'], ['humus', 'organic matter']], o='O6'),
 MC('Why is soil important?', 'Plants grow in it, and many animals live in it', [('It makes rocks melt', 'Soil does not melt rocks.'), ('It makes the weather', 'Soil does not make weather.')], o='O6'),
 MC('Which animal helps to mix soil and break down dead leaves?', 'The earthworm', [('The shark', 'Sharks live in the sea.'), ('The eagle', 'Eagles live in the air and trees.')], o='O6'),
 MC('In the drainage test, what did we CHANGE?', 'The type of soil', [('The amount of water', 'That stayed the same.'), ('The time', 'Each test lasted 5 minutes.')], o='O7'),
 MC('In the drainage test, what did we MEASURE?', 'How much water dripped through in 5 minutes', [('The colour of the soil', 'That is not measured.'), ('The type of soil', 'That is what we changed.')], o='O7'),
 MS('Which must stay the SAME to keep the drainage test fair?', ['the amount of soil', 'the amount of water poured in', 'the time we wait'], ['the type of soil'], o='O7'),
 TB('Read the results from the video and complete the table.', ['Soil', 'Water through in 5 minutes (mL)'], [['sandy', B(80)], ['loam', B(50)], ['clay', B(15)]], o='O7', skill='Data', hint='Sandy soil let the most water through; clay soil the least.'),
 MC('How much more water drained through sandy soil than through clay?', '65 mL', [('15 mL', 'That is how much went through clay.'), ('95 mL', 'Take away, do not add: 80 − 15.'), ('80 mL', 'That is the sandy amount only.')], o='O7', skill='Data'),
 MC('What should a gardener add to make clay soil better?', 'Compost (humus) and some sand', [('More clay', 'That makes it stickier.'), ('Plastic', 'Plastic harms soil.')], o='O7'),
 MC('Why is it bad to put too much pesticide on soil?', 'It can kill useful animals, like earthworms, and wash into rivers', [('It makes soil too wet', 'That is not the problem.'), ('It turns soil into sand', 'It does not change soil type.')], o='O7'),
 MC('Which is a good way to look after soil?', 'Add compost made from kitchen and garden waste', [('Pour oil on it', 'Oil harms soil.'), ('Cover it in concrete', 'Plants cannot grow then.')], o='O7'),
 MC('What do we call the measuring cup we use to measure water in mL?', 'A measuring cylinder', [('A thermometer', 'That measures temperature.'), ('A forcemeter', 'That measures force.')], o='O7'),
)
s.adv(
 GR('Plot the drainage results as points.', {'label': 'Soil (1 = sandy, 2 = loam, 3 = clay)', 'min': 0, 'max': 4, 'step': 1}, {'label': 'Water through (mL)', 'min': 0, 'max': 100, 'step': 20}, [[1, 80], [2, 50], [3, 15]], o='O7', d='H', table_rows=[[1, 80], [2, 50], [3, 15]]),
 EX('A farmer\'s field is sandy and plants keep drying out. What should she do, and why?', [('add compost / humus / organic matter', ['compost', 'humus', 'organic']), ('so the soil holds more water', ['hold', 'keep', 'water'])], 'Add compost (humus): it helps the soil hold more water and adds nutrients, so plants do not dry out.', o='O7', d='H'),
 MC('Ali poured 100 mL into each soil and collected 80 mL from sandy soil. Where did the other 20 mL go?', 'It stayed in the soil', [('It disappeared', 'Water does not disappear.'), ('It turned into sand', 'Water does not become sand.')], o='O7', d='H'),
 MC('Why might a plant in clay soil die in a very wet season?', 'The soil becomes waterlogged, so the roots get no air', [('Clay soil drains too fast', 'Clay holds water.'), ('Clay has too much air', 'Waterlogged soil has very little air.')], o='O6', d='VH'),
)
s.labs('Soil drainage lab',
 {'kind': 'test', 'title': 'Which soil drains fastest?', 'intro': '100 mL of water was poured onto the same amount of each soil. Read the measuring cylinder to see how much water dripped through in 5 minutes.',
  'change': 'The type of soil', 'measure': 'Water through in 5 minutes', 'unit': 'mL', 'max': 100, 'step': 10, 'instr': '🧪',
  'conds': [{'k': 'sand', 't': 'Sandy soil', 'emoji': '🏖️', 'val': 80}, {'k': 'loam', 't': 'Loam', 'emoji': '🌱', 'val': 50}, {'k': 'clay', 't': 'Clay soil', 'emoji': '🏺', 'val': 15}],
  'qs': [MC('Which soil let the most water through?', 'Sandy soil', [('Clay soil', 'Clay held most of its water.'), ('Loam', 'Loam was in the middle.')], o='O7'),
         MC('Which soil would stay wettest after rain?', 'Clay soil', [('Sandy soil', 'Water drained quickly through sand.'), ('Loam', 'Clay held more water.')], o='O6'),
         MC('Why did we use the same amount of water for each soil?', 'To keep the test fair', [('To make the soil heavier', 'That is not the reason.'), ('Because soil likes 100 mL', 'Fair tests change only one thing.')], o='O7')]},
 {'title': 'Soil drainage test', 'intro': 'Compare how well two soils drain.',
  'need': ['2 plastic bottles with the bottoms cut off (ask an adult)', '2 coffee filters or pieces of cloth', 'two different soils (e.g. sand and garden soil)', 'a measuring jug', 'two cups', 'a timer'],
  'safety': ['Ask an adult to cut the bottles.', 'Wash your hands after touching soil.'],
  'steps': ['Put a filter in the neck of each upside-down bottle and stand each one in a cup.', 'Put the same amount of each soil into the bottles.', 'Pour 100 mL of water into each at the same time and start the timer.', 'After 5 minutes, measure how much water is in each cup.'],
  'record': {'head': ['Soil', 'Water through in 5 minutes (mL)'], 'rows': [['Soil 1', {'min': 0, 'max': 100}], ['Soil 2', {'min': 0, 'max': 100}]], 'hint': 'You poured 100 mL, so each answer is between 0 and 100.'},
  'qs': [MC('A soil let 70 mL through and another let 20 mL through. Which drains better?', 'The one that let 70 mL through', [('The one that let 20 mL through', 'Less water came through.'), ('They are the same', '70 is much more than 20.')], o='O7')]})

U.mindmap(('Igneous rocks', 'Magma or lava cools; slow cooling = big crystals.', 'O1', '3.1'), ('Identifying rocks', 'Use keys and observations.', 'O2', '3.1'),
          ('Sedimentary rocks', 'Weathering, erosion, sedimentation; fossils.', 'O3', '3.2'), ('Metamorphic rocks', 'Heat and pressure; the rock cycle.', 'O4', '3.3'),
          ('Uses of rocks', 'Chosen for their properties.', 'O5', '3.3'), ('Soil', 'Weathered rock + humus; sandy, clay, loam.', 'O6', '3.4'), ('Caring for soil', 'Compost helps; too much chemicals harm.', 'O7', '3.4'))
