"""Pilot: Stage 8 Unit 7 (Exothermic and Endothermic Changes) — paragraph questions (4–6 sentences, data + data quality)
in Hard, an Extreme tier (VH) per lesson, and a 6-mark paragraph question in Unit Tests A and B (still 30 marks).
Edits content/src/stage8-unit07.json in place; safe to run again. Then: node tools/build-content.mjs && node tools/seal-keys.mjs"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '..', 'src', 'stage8-unit07.json')
S8 = [4, 6]
F8 = 'The data show … For example, at … the value was … This is because … The results are / are not reliable because …'

def para(id, obj, prompt, rubric, need, model, partial, data=None, adv=False, ext=False, words=40, sentences=S8, frame=F8, teacher=False, pts=None):
    q = {'id': id, 'type': 'para', 'prompt': ('* Advanced. ' if adv else '') + prompt, 'diff': 'VH', 'obj': obj, 'skill': 'Reasoning',
         'sentences': sentences, 'minWords': words, 'frame': frame, 'rubric': [{'pt': p, 'kw': [k]} for p, k in rubric], 'need': need,
         'model': model, 'partial': [{'text': t, 'score': s, 'why': w} for t, s, w in partial], 'hint': '', 'reason': ''}
    if data: q['data'] = {'head': data[0], 'rows': data[1:]}
    if adv: q['adv'] = True
    if ext: q['source'] = 'Camday original'
    if teacher: q['teacher'] = True; q['pts'] = pts
    return q

def mcq(id, obj, prompt, opts, data=None):
    q = {'id': id, 'type': 'mcq', 'prompt': prompt, 'diff': 'VH', 'obj': obj, 'skill': 'Reasoning',
         'options': [{'t': t, 'ok': ok, 'fb': fb} for t, ok, fb in opts], 'hint': '', 'reason': '', 'source': 'Camday original'}
    if data: q['data'] = {'head': data[0], 'rows': data[1:]}
    return q

def num(id, obj, prompt, answer, unit, units, reason, hint=''):
    return {'id': id, 'type': 'num', 'prompt': prompt, 'diff': 'VH', 'obj': obj, 'skill': 'Application', 'answer': answer, 'unit': unit, 'tol': 0.0,
            'units': units, 'errs': [], 'unitFb': '', 'hint': hint, 'reason': reason, 'source': 'Camday original'}

# ---------------- Lesson 7.1 Exothermic changes ----------------
H1 = [
  para('s8u07s1h01', 'O1', 'A student adds dilute hydrochloric acid, 5 cm³ at a time, to 25 cm³ of sodium hydroxide solution in an insulated cup. Use the data to describe and explain how the temperature changes. Comment on how reliable the conclusion is.',
       [('The temperature rises to a peak at 15 cm³', 'rise|peak|highest|maximum|increas'),
        ('Quotes data with units, e.g. 21.0 °C to 30.1 °C', '30\\.1|21\\.0|9\\.1'),
        ('Neutralisation is exothermic, so it releases energy', 'exothermic|releas|give[sn]? out'),
        ('After the peak the alkali is used up, and cooler acid / heat loss lowers the temperature', 'used up|no more|stops|cooler|cold acid|lost|surroundings'),
        ('Only one trial: repeat to check the results are reliable', 'repeat|reliab|only once|one trial|anomal')], 4,
       'As the acid is added the temperature rises from 21.0 °C to a peak of 30.1 °C at 15 cm³. The temperature rises because neutralisation is exothermic, so energy is released. After 15 cm³ all of the alkali has been used up, so no more energy is released. Adding more cooler acid and heat lost to the surroundings make the temperature fall to 27.6 °C. The results come from only one trial, so the experiment should be repeated to check they are reliable.',
       [('The temperature goes up from 21.0 °C to 30.1 °C and then goes down again. This is because the reaction is exothermic. Then it gets colder at the end of the experiment.', 3, 'Data, rise and exothermic, but no reason for the fall and no comment on reliability'),
        ('The temperature changes when you add the acid. It goes up and down because of the reaction. The acid and the alkali make a salt and water in the cup.', 1, 'Only the rise; no data, no energy idea')],
       data=[['Volume of acid added (cm³)', 'Temperature (°C)'], ['0', '21.0'], ['5', '24.5'], ['10', '27.8'], ['15', '30.1'], ['20', '29.0'], ['25', '27.6']], adv=True),
  para('s8u07s1h02', 'O2', 'A reusable hand warmer contains a solution of sodium ethanoate. When a metal disc inside is clicked, crystals form and the pack warms to 54 °C. Explain why the pack gets warm, and how it can be used again.',
       [('Crystals form / the solution crystallises', 'crystal|solid'),
        ('Crystallisation is exothermic and releases energy', 'exothermic|releas|give[sn]? out'),
        ('The energy is transferred to the hands / surroundings', 'hand|surroundings|transfer'),
        ('To reuse it, heat it in hot water so the crystals dissolve again', 'boil|hot water|dissolv|melt')], 3,
       'When the disc is clicked, the dissolved sodium ethanoate forms crystals. Crystallisation is an exothermic change, so it releases energy. This energy is transferred to your hands and the surroundings, so the pack feels warm. To reuse the pack, you put it in boiling water so the crystals dissolve again. This takes in energy, so the pack is ready to use next time.',
       [('When you click the disc the liquid turns into crystals. This makes the pack hot so your hands get warm. You can use it many times.', 2, 'Crystals and energy to the hands; no exothermic idea, no way to reuse'),
        ('The pack is exothermic because it gets hot when you click it. It is very useful in winter for keeping warm outside.', 1, 'Names exothermic but explains nothing else')],
       adv=True),
]
X1 = [
  para('s8u07s1x01', 'O1', 'A student burns three fuels under a can holding 100 cm³ of water and records the temperature rise. She claims: “Paraffin releases the most energy per gram.” Evaluate her claim using the data, and suggest two improvements to the experiment.',
       [('Works out wax per gram: 14 °C for 0.5 g ≈ 28 °C per gram', '28|per gram|divide|double'),
        ('Paraffin gives the largest rise (31 °C), so the data support the claim', '31|support|agree|largest|highest|most'),
        ('The difference from wax is small (about 3 °C), so the claim is uncertain', 'small|close|similar|not sure|uncertain|cannot be sure'),
        ('Energy is lost to the surroundings, so not all of it heats the water', 'lost|surroundings|escape'),
        ('Improvement: repeat each test and calculate an average', 'repeat|average|mean'),
        ('Improvement: burn the same mass, use a draught shield, lid or insulation', 'same mass|insulat|lid|shield|draught|same distance')], 5,
       'The data support the claim because paraffin gave the largest temperature rise, 31 °C for 1.0 g. Wax gave 14 °C for 0.5 g, so per gram it would give about 28 °C, which is close to paraffin. The difference is only about 3 °C, so we cannot be sure the claim is correct from one trial. Some energy is also lost to the surroundings, so the water does not take in all of it. The student should repeat each test three times and calculate an average. She should also burn the same mass of each fuel and use a shield to stop draughts.',
       [('Paraffin is the best fuel because it has the biggest number, 31 °C. Wax only made 14 °C so it is the worst fuel. She should repeat the experiment to make it better and fairer.', 3, 'Supports the claim and suggests repeats, but misses the per-gram comparison, the small difference and heat loss'),
        ('Paraffin gives 31 °C and ethanol gives 24 °C. Wax is 0.5 g, so it is double, 28 °C per gram, close to paraffin. So the claim might be wrong.', 3, 'Good per-gram reasoning but no improvements and no energy-loss idea')],
       data=[['Fuel', 'Mass burned (g)', 'Temperature rise (°C)'], ['Ethanol', '1.0', '24'], ['Paraffin', '1.0', '31'], ['Wax', '0.5', '14']], ext=True, words=50),
  mcq('s8u07s1x02', 'O1', 'An iron hand warmer (iron + oxygen → iron oxide) reaches 60 °C in air. The same pack sealed in a bag of nitrogen stays at 20 °C. Opened in pure oxygen, it reaches 60 °C in half the time. What is the best conclusion?',
      [('The reaction needs oxygen, is exothermic, and goes faster when there is more oxygen.', True, 'Yes – no oxygen, no temperature rise; more oxygen, faster rise.'),
       ('Nitrogen is endothermic, so it takes in the energy from the iron.', False, 'Nitrogen is just a gas that does not react with iron. The pack stays cold because there is no oxygen to react with.'),
       ('Iron releases energy by itself; oxygen only makes the pack look different.', False, 'In nitrogen there is no rise at all, so the iron cannot release the energy on its own.'),
       ('Oxygen is the fuel that burns, and iron only stores the heat.', False, 'Iron is the reactant that is oxidised. Oxygen is needed, but it is not a fuel.')]),
  num('s8u07s1x03', 'O2', 'Dissolving 5 g of calcium chloride in 50 cm³ of water raises the temperature by 8 °C. The same 5 g is dissolved in 100 cm³ of water instead. Predict the temperature rise.',
      4, '°C', ['°C', 'K'], 'The same amount of salt releases the same energy, but it is shared by twice as much water, so the rise is half: 8 ÷ 2 = 4 °C.', 'Same energy released, twice as much water to warm up.'),
  para('s8u07s1x04', 'O2', 'On frosty nights, fruit farmers spray their trees with water. Ice forms on the buds, but the buds are not damaged. Explain how spraying water protects the buds.',
       [('The water freezes into ice on the buds', 'freez|ice|solid'),
        ('Freezing is exothermic and releases energy', 'exothermic|releas|give[sn]? out'),
        ('The energy stops the bud falling below 0 °C', '0 ?°C|zero|below|stays'),
        ('Spraying continues all night, so freezing keeps releasing energy', 'keep|continu|all night|more water'),
        ('The layer of ice insulates the bud from the colder air', 'insulat|layer|cover|colder air|wind')], 4,
       'The sprayed water freezes into a layer of ice on the buds. Freezing is exothermic, so the water releases energy as it turns to ice. This energy stops the bud temperature from falling below 0 °C. The farmers keep spraying water all night, so freezing continues and keeps releasing energy. The ice layer also covers the buds and insulates them from the colder air.',
       [('The water turns to ice on the buds and the ice keeps them warm like a blanket. This stops the frost from killing the buds.', 2, 'Freezing and insulation, but no energy released and no link to 0 °C'),
        ('Freezing is exothermic, so it gives out energy. This energy warms the buds. So the buds are protected from the frost at night.', 2, 'Exothermic energy idea only')],
       ext=True),
]

# ---------------- Lesson 7.2 Endothermic changes ----------------
H2 = [
  para('s8u07s2h01', 'O3', 'Different masses of sodium hydrogencarbonate are added to citric acid solution. Describe the pattern, identify the anomalous result and explain why the temperature falls.',
       [('Pattern: more mass gives a bigger fall (about 3 °C per gram)', 'more|bigger|larger|increas|proportional'),
        ('The 4 g result (6.1 °C) is anomalous', '4 ?g|6\\.1|anomal'),
        ('It should be about 12 °C', '12'),
        ('The reaction is endothermic and takes in energy', 'endothermic|takes? in|absorb'),
        ('Energy comes from the water/solution, so it gets colder; repeat the 4 g test', 'from the (water|solution|surroundings)|repeat')], 4,
       'As the mass of sodium hydrogencarbonate increases, the temperature fall gets bigger, by about 3 °C for each gram. The result for 4 g is anomalous because the fall is only 6.1 °C. Following the pattern it should be about 12 °C, so this test should be repeated. The temperature falls because the reaction is endothermic. It takes in energy from the water in the solution, so the solution gets colder.',
       [('The more powder you add, the colder it gets. The 4 g one is wrong because it does not fit. The reaction is endothermic.', 3, 'Pattern, anomaly and endothermic; no expected value and no energy source'),
        ('The temperature goes down every time. This is because the reaction takes in energy. It is a chemical reaction.', 1, 'Only the energy idea; no pattern or anomaly')],
       data=[['Mass of sodium hydrogencarbonate (g)', 'Temperature fall (°C)'], ['1', '3.1'], ['2', '6.0'], ['3', '9.2'], ['4', '6.1'], ['5', '15.0']], adv=True),
  para('s8u07s2h02', 'O4', 'A dry thermometer reads 20.0 °C. A thermometer with a wet cloth around its bulb reads 17.5 °C in still air, and 14.0 °C when a fan blows on it. Use the particle model to explain both results.',
       [('Water evaporates from the wet cloth', 'evaporat'),
        ('Evaporation is endothermic: it takes in energy from the thermometer', 'endothermic|takes? in|absorb'),
        ('The particles with the most energy escape, leaving slower ones', 'most energy|fastest|escape|leav'),
        ('The fan moves air / vapour away, so evaporation is faster', 'fan|moving air|faster|quicker|more quickly'),
        ('Uses data: falls of 2.5 °C and 6.0 °C', '2\\.5|6\\.0|14\\.0|17\\.5')], 4,
       'Water evaporates from the wet cloth around the bulb. Evaporation is endothermic, so it takes in energy from the thermometer. The particles with the most energy escape from the liquid, leaving slower particles behind, so the reading falls by 2.5 °C. With the fan, moving air carries the water vapour away, so evaporation happens faster. More energy is taken in each minute, so the reading falls further, by 6.0 °C.',
       [('The water evaporates and makes the thermometer cold. The fan makes it even colder, 14.0 °C, because it blows cold air on it.', 2, 'Evaporation and data; the fan idea is wrong (the air is not colder) and no particle idea'),
        ('Evaporation takes in energy, so the wet thermometer is colder. The fan makes the water evaporate faster so it is the coldest of all.', 3, 'Energy, evaporation and fan; no particles or data')],
       adv=True),
]
X2 = [
  para('s8u07s2x01', 'O3', 'A student says: “Photosynthesis is endothermic, so a greenhouse full of plants should be colder than an empty greenhouse.” Evaluate this claim.',
       [('Photosynthesis takes in energy from light', 'light|sun'),
        ('The energy is stored as chemical energy in glucose', 'glucose|sugar|chemical (energy|store)'),
        ('The energy comes from light, not from the thermal energy of the air, so it does not cool the greenhouse', 'not from the (air|surroundings|thermal)|does not cool|doesn.t cool|not colder'),
        ('Plants also respire, which is exothermic', 'respir'),
        ('Conclusion: the claim is not supported (any cooling would be from evaporation or shade)', 'evaporat|transpir|shade|not supported|disagree|wrong|incorrect')], 4,
       'Photosynthesis is endothermic because plants take in energy from light. This energy is stored as chemical energy in glucose. However, the energy comes from light, not from the thermal energy of the air, so photosynthesis does not cool the greenhouse. Plants also respire, which is exothermic and releases some energy. Water evaporating from the leaves could cool the air a little, but that is not caused by photosynthesis, so the claim is not supported.',
       [('I agree because endothermic reactions take in heat, so the plants take heat from the air and the greenhouse gets colder.', 0, 'Confuses energy from light with thermal energy from the air'),
        ('Photosynthesis uses light energy to make glucose. Plants also respire and give out energy. So the greenhouse is not colder.', 4, 'Light, glucose, respiration and a conclusion; does not say why light energy does not cool the air')],
       ext=True),
  mcq('s8u07s2x02', 'O4', 'Dissolving 10 g of ammonium nitrate in 50 cm³ of water makes the temperature fall by 10 °C. Which change would give a BIGGER temperature fall?',
      [('Dissolve 20 g of ammonium nitrate in the same 50 cm³ of water.', True, 'Yes – twice the salt takes in twice the energy from the same amount of water.'),
       ('Dissolve 10 g of ammonium nitrate in 100 cm³ of water.', False, 'The same energy is taken from twice as much water, so the fall is smaller.'),
       ('Start with warmer water.', False, 'The energy taken in is about the same, so the fall is about the same.'),
       ('Stir the mixture faster.', False, 'Stirring makes it dissolve faster, but the total fall is the same.')]),
  num('s8u07s2x03', 'O3', 'Thermal decomposition of 2.0 g of copper carbonate takes in 1.8 kJ of energy. How much energy is needed to decompose 5.0 g?',
      4.5, 'kJ', ['kJ', 'J'], '1.8 kJ ÷ 2.0 g = 0.9 kJ per gram, so 5.0 g needs 0.9 × 5.0 = 4.5 kJ.', 'Find the energy for 1 g first.'),
  para('s8u07s2x04', 'O4', 'A company wants one salt for an instant cold pack and one for an instant hot pack. Use the data to choose a salt for each pack and explain your choices. Explain why one salt is no use for either pack, and comment on the quality of the data.',
       [('Cold pack: ammonium nitrate (biggest fall)', 'ammonium nitrate'),
        ('Dissolving it is endothermic: it takes in energy', 'endothermic|takes? in|absorb'),
        ('Hot pack: calcium chloride (rise of 12.0 °C)', 'calcium chloride'),
        ('Dissolving it is exothermic: it releases energy', 'exothermic|releas'),
        ('Sodium chloride changes too little (0.5 °C)', 'sodium chloride|0\\.5'),
        ('Each salt tested once: repeat with the same mass and volume', 'repeat|same mass|same volume|fair')], 5,
       'For the cold pack I would use ammonium nitrate, because it gives the biggest fall of 9.5 °C. Dissolving it is endothermic, so it takes in energy from the surroundings. For the hot pack I would use calcium chloride, because its temperature rises by 12.0 °C. Dissolving calcium chloride is exothermic, so it releases energy. Sodium chloride is no use for either pack because its change of 0.5 °C is too small. Each salt was tested only once, so the tests should be repeated with the same mass and volume of water.',
       [('Ammonium nitrate for cold and calcium chloride for hot because they change the most. Sodium chloride hardly changes at all.', 3, 'Correct choices and sodium chloride; no energy explanation, no data quality'),
        ('Ammonium nitrate is endothermic so it is good for a cold pack. Calcium chloride is exothermic so it is good for a hot pack. They should repeat it.', 5, 'Everything except the sodium chloride comparison')],
       data=[['Salt (10 g in 50 cm³ water)', 'Temperature change (°C)'], ['Ammonium nitrate', '−9.5'], ['Calcium chloride', '+12.0'], ['Sodium chloride', '−0.5'], ['Potassium chloride', '−5.0']], ext=True, words=50),
]

# Unit Test questions (with keys) live in the git-ignored content/private folder
import sys, importlib
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..', 'private'))
import s8u07_kit; s8u07_kit.para = para
_t = importlib.import_module('tests_stage8_unit07_para')
TA, TB, DROP = _t.TA, _t.TB, _t.DROP

PARTIAL = {'s8u07s1h01': [('The temperature goes up from 21.0 °C to 30.1 °C when the acid is added. This happens because the reaction between the acid and the alkali is exothermic. After that the temperature goes down again to 27.6 °C at the end. The cup is insulated so it keeps the energy in the mixture for longer.', 3, 'Data, rise and exothermic; no reason for the fall and no comment on reliability'), ('The temperature changes a lot when you add the acid to the alkali in the cup. It goes up and then it goes down again near the end of the experiment. The acid and the alkali react together and make a salt and water. The student used a polystyrene cup with a lid so that the test is fair.', 1, 'Only the rise and fall; no data and no energy idea')], 's8u07s1h02': [('When you click the disc, the liquid inside the pack turns into crystals. This makes the pack hot, so your hands get warm. The pack stays warm for quite a long time in your pocket. You can use the same pack many times in winter.', 2, 'Crystals and energy to the hands; no exothermic idea and no way to reuse it'), ('The pack is exothermic because it gets hot when you click the metal disc. It is very useful in winter for keeping warm outside. People take them when they go skiing or walking. It is better than a battery warmer because it has no wires.', 1, 'Names exothermic but explains nothing else')], 's8u07s1x01': [('Paraffin is the best fuel because it has the biggest temperature rise, which is 31 °C. Ethanol only made 24 °C and wax only made 14 °C, so wax is the worst fuel. I agree with the student that paraffin releases the most energy. She should repeat the experiment three times to make her results more reliable and fair.', 3, 'Supports the claim and suggests repeats, but misses the per-gram comparison, the small difference and heat loss'), ('Paraffin gives a rise of 31 °C and ethanol gives a rise of 24 °C for the same mass. Wax was only 0.5 g, so if we double it, wax would give about 28 °C per gram. This is very close to paraffin, so the claim might not be right. The student cannot be sure which fuel is really the best from these results.', 3, 'Good per-gram reasoning and the uncertainty, but no improvements and no energy-loss idea')], 's8u07s1x04': [('The water that the farmers spray turns to ice on the buds. The ice covers the buds and keeps them warm like a blanket. This stops the frost from getting to the buds. So the buds are not damaged and the fruit can still grow in the spring.', 2, 'Freezing and insulation, but no energy released and no link to 0 °C'), ('Freezing is an exothermic change, so it gives out energy. When the water freezes on the buds, this energy warms the buds a little. The buds are then protected from the frost at night. This is why the farmers spray the trees when it is very cold.', 2, 'The exothermic energy idea only; nothing about 0 °C, spraying all night or insulation')], 's8u07s2h01': [('The more sodium hydrogencarbonate you add, the colder the solution gets. The result for 4 g is wrong because it does not fit the pattern of the others. The reaction is endothermic, so the temperature goes down. The student should do the experiment carefully next time.', 3, 'Pattern, anomaly and endothermic; no expected value and no source of the energy'), ('The temperature goes down every time some powder is added to the acid. This is because the reaction takes in energy when it happens. It is a chemical reaction because a gas is made and it fizzes. The student measured the temperature with a thermometer.', 1, 'Only the energy idea; no pattern, no anomaly and no data')], 's8u07s2h02': [('The water in the cloth evaporates and this makes the thermometer colder. That is why it shows 17.5 °C instead of 20.0 °C. The fan makes it even colder, 14.0 °C, because it blows cold air onto the bulb. So the wet thermometer with the fan is the coldest one.', 2, 'Evaporation and data; the fan idea is wrong (the air is not colder) and there is no particle idea'), ('Evaporation takes in energy, so the wet thermometer is colder than the dry one. The water on the cloth slowly turns into a gas in the air. The fan makes the water evaporate faster, so the reading is the coldest of all. This is like when you feel cold after swimming.', 3, 'Energy, evaporation and the fan; no particle model and no data')], 's8u07s2x01': [('I agree with the student because photosynthesis is an endothermic reaction. Endothermic reactions take in heat from the surroundings. So the plants take heat from the air in the greenhouse. This means a greenhouse full of plants would be colder than an empty one.', 0, 'Confuses energy from light with thermal energy from the air'), ('Photosynthesis uses light energy from the Sun to make glucose. The energy is stored in the glucose as chemical energy. Plants also respire all the time and respiration gives out energy. So I do not think the greenhouse with plants would be colder, and the claim is wrong.', 4, 'Light, glucose, respiration and a conclusion; does not explain why light energy does not cool the air')], 's8u07s2x04': [('I would use ammonium nitrate for the cold pack and calcium chloride for the hot pack. This is because they change the temperature the most of all the salts. Sodium chloride is no good because it hardly changes the temperature at all. Potassium chloride could also be used for a cold pack but it is not as good.', 3, 'Correct choices and the sodium chloride point; no energy explanation and no comment on the data'), ('Ammonium nitrate is the best for a cold pack because its temperature falls by 9.5 °C. Dissolving it is endothermic, so it takes in energy. Calcium chloride is the best for a hot pack because dissolving it is exothermic and releases energy. The company should repeat each test to check the results.', 5, 'Everything except why sodium chloride is no use')]}
d = json.load(open(SRC))
PARTIAL.update(_t.PARTIAL)
for q in H1 + H2 + X1 + X2 + [TA, TB]:
    if q['type'] == 'para' and q['id'] in PARTIAL: q['partial'] = [{'text': t, 'score': sc, 'why': w} for t, sc, w in PARTIAL[q['id']]]
def put(lst, items):
    ids = {q['id'] for q in items}
    return [q for q in lst if q['id'] not in ids] + items
s1, s2 = d['sections']
s1['adv'] = put(s1['adv'], H1); s2['adv'] = put(s2['adv'], H2)
s1['ext'] = X1; s2['ext'] = X2
for f, new in (('A', TA), ('B', TB)):
    t = [q for q in d['tests'][f] if q['id'] not in DROP[f] and q['id'] != new['id']]
    t.append(new); d['tests'][f] = t
    assert sum(q['pts'] for q in t) == 30, (f, sum(q['pts'] for q in t))
json.dump(d, open(SRC, 'w'), ensure_ascii=False)
print('stage8-unit07: Hard +', len(H1) + len(H2), 'paragraph | Extreme', len(X1) + len(X2), '| tests A/B 30 marks with a 6-mark paragraph')
