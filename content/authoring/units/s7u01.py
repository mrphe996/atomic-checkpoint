# -*- coding: utf-8 -*-
"""Stage 7 Unit 1 – Introducing Science. Written by the Atomic teaching team."""
from c_kit import *

STRAND = "Thinking and Working Scientifically"
BLURB = "What science is, how scientists plan fair tests and handle data, how to stay safe in the laboratory, and how science and technology change our world."

OBJECTIVES = {
    "O1": {"sec": "1.1", "code": "7SIC.01", "codeNote": "", "t": "Describe what science is, its main areas of study, and how scientists build on each other's work."},
    "O2": {"sec": "1.2", "code": "7TWSp.01, 7TWSp.03", "codeNote": "", "t": "Follow the steps of scientific enquiry and decide whether a hypothesis is testable."},
    "O3": {"sec": "1.2", "code": "7TWSp.04", "codeNote": "", "t": "Identify independent, dependent and control variables and plan a fair test."},
    "O4": {"sec": "1.2", "code": "7TWSc.04, 7TWSa.03, 7TWSa.05", "codeNote": "", "t": "Explain accurate and precise measurements, present data and draw conclusions."},
    "O5": {"sec": "1.3", "code": "7TWSp.05, 7TWSc.02, 7TWSc.05", "codeNote": "", "t": "Work safely in the laboratory, recognise hazard symbols and choose suitable apparatus."},
    "O6": {"sec": "1.4", "code": "7SIC.02, 7SIC.05, 7TWSc.06", "codeNote": "", "t": "Describe how science and technology are used, their benefits and problems, and recognise bias."},
}

SECTIONS = [
    {"id": "1.1", "title": "What is science?", "objs": ["O1"]},
    {"id": "1.2", "title": "How do we do science?", "objs": ["O2", "O3", "O4"]},
    {"id": "1.3", "title": "Working in the laboratory", "objs": ["O5"]},
    {"id": "1.4", "title": "Using science", "objs": ["O6"]},
]

# ---------------------------------------------------------------- 1.1
S1_REQ = [
    mc("u1s1r1", "M", "O1", "Which is the best description of science?", ("The study of how things work – what we know and how we find out more.", "Correct: knowledge plus processes."),
       [("A list of facts to memorise.", "Science also includes the processes used to find out."), ("Only experiments with chemicals.", "Science covers far more."), ("Guessing answers.", "Science uses evidence.")]),
    gd("u1s1r2", "M", "O1", "Which area of science studies each question?", ["Area"],
       [("Why does it rain more in some months?", ["Meteorology"]), ("How does a chick develop in an egg?", ["Biology"]), ("Why does bread dough rise?", ["Chemistry"]), ("Why does it get dark at night?", ["Astronomy"]), ("How does a switch make a lamp glow?", ["Physics"])], skill="Data"),
    mt("u1s1r3", "M", "O1", "Match each area of science to what it studies.", [("Physics", "energy, motion and forces"), ("Chemistry", "matter and how it changes"), ("Biology", "living things"), ("Astronomy", "planets, moons and stars")]),
    mt("u1s1r4", "H", "O1", "Match each scientist to their work.", [("Hypatia of Alexandria", "measuring the density of liquids"), ("Ibn Sina", "collecting evidence to test medical treatments"), ("Marie Curie", "radioactivity"), ("Rosalind Franklin", "X-ray images that helped reveal DNA's structure")]),
    mc("u1s1r5", "M", "O1", "What is a phenomenon?", ("Something we observe happening", "Correct – science tries to explain phenomena."), [("A type of scientist", "No."), ("A piece of apparatus", "No."), ("A wrong answer", "No.")]),
    ex("u1s1r6", "H", "O1", "Explain how scientific knowledge grows over time, using an example.",
       [("each discovery becomes a starting point for the next / build on earlier work", ["build|starting point|earlier|previous|next"]), ("gives an example", ["franklin|khorana|zhang|dna|curie|x-ray|newton"])],
       "Scientists build on each other's work. For example, Rosalind Franklin's X-ray images helped reveal DNA's structure, then Khorana worked out how the body uses DNA, and later Feng Zhang developed ways to change DNA to treat illness.", need=2),
    od("u1s1r7", "H", "O1", "Put these DNA discoveries in the order they built on each other.", ["Franklin's X-ray images reveal DNA's structure", "Khorana works out how the body uses DNA", "Zhang develops ways to change DNA to treat illness"]),
    tb("u1s1r8", "H", "O1", "Data: a class survey of which area of science pupils find most interesting. Complete the totals.", ["Area", "Class A", "Class B", "Total"],
       [["Biology", "9", "7", B(16)], ["Physics", "6", "8", B(14)], ["Chemistry", "5", "4", B(9)], ["Astronomy", "8", "9", B(17)]], skill="Data"),
]
S1_PRAC = [
    mc("u1s1p01", "M", "O1", "Meteorology is the study of…", "the weather", [("meteors only", "No – it means weather."), ("metals", "No."), ("medicine", "No.")]),
    mc("u1s1p02", "M", "O1", "Chemistry is the study of…", "matter – what things are made of and how they change", [("living things", "Biology."), ("space", "Astronomy."), ("forces", "Physics.")]),
    mc("u1s1p03", "M", "O1", "Which area of science studies how a cargo ship floats?", "Physics", [("Biology", "Not living."), ("Meteorology", "Weather."), ("Astronomy", "Space.")]),
    mc("u1s1p04", "M", "O1", "Synthetic materials are…", "made by people using science", [("always natural", "No."), ("only wood and cotton", "Those are natural."), ("living things", "No.")]),
    mc("u1s1p05", "M", "O1", "Global warming is…", "a rise in Earth's average temperature", [("a cold winter", "No."), ("only hot summers", "No."), ("a type of electricity", "No.")]),
    mc("u1s1p06", "H", "O1", "Science has two main parts. What are they?", "What we already know, and the processes used to find out more", [("Physics and biology only", "Many areas."), ("Questions and guesses", "Evidence is needed."), ("Teachers and students", "No.")]),
    mc("u1s1p07", "H", "O1", "Ibn Sina's idea of collecting evidence to check treatments matters because…", "it shows which treatments really work", [("it made medicines cheaper", "Not the point."), ("it stopped all disease", "No."), ("it replaced doctors", "No.")]),
    mc("u1s1p08", "M", "O1", "Which scientist's work led to X-rays and cancer treatments?", "Marie Curie", [("Hypatia", "Density of liquids."), ("Feng Zhang", "Changing DNA."), ("Ibn Sina", "Evidence in medicine.")]),
    mc("u1s1p09", "H", "O1", "Do scientists always work alone?", "No – some work alone and some in teams, and all build on others' work.", [("Yes, always alone.", "Many work together."), ("Yes, they must keep work secret.", "They share results."), ("No, only in pairs.", "No fixed rule.")]),
    mc("u1s1p10", "M", "O1", "Which question is a biology question?", "How do bees find flowers?", [("Why does iron rust?", "Chemistry."), ("How fast does a car accelerate?", "Physics."), ("When will it rain?", "Meteorology.")]),
    mc("u1s1p11", "M", "O1", "Which question is an astronomy question?", "Why does the Moon change shape in the sky?", [("Why do leaves change colour?", "Biology."), ("How do batteries work?", "Physics/chemistry."), ("Why does salt dissolve?", "Chemistry.")]),
    mc("u1s1p12", "H", "O1", "Our demand for electricity and transport has…", "helped cause global warming and climate change", [("cooled the Earth", "No."), ("had no effect", "No."), ("stopped pollution", "No.")]),
    mc("u1s1p13", "M", "O1", "Science has developed around the world for…", "thousands of years", [("about 10 years", "Far longer."), ("only since 2000", "No."), ("only in Europe", "Around the world.")]),
    mc("u1s1p14", "H", "O1", "Feng Zhang helped develop ways to…", "treat illness by changing a person's DNA", [("measure liquid density", "Hypatia."), ("study the weather", "No."), ("make X-ray images of DNA", "Franklin.")]),
    od("u1s1p15", "M", "O1", "Order these scientists by when they lived, earliest first.", ["Hypatia of Alexandria", "Ibn Sina", "Marie Curie", "Rosalind Franklin"]),
    mc("u1s1p16", "H", "O1", "Which is a phenomenon science explains?", "A chick hatching from an egg", [("A favourite colour", "Opinion."), ("A football score", "Not a natural phenomenon."), ("A poem", "No.")]),
    ms("u1s1p17", "M", "O1", "Select ALL the things developed using science.", ["Electricity supply", "Synthetic materials", "Aeroplanes"], [("Natural cotton growing on plants", "Natural, not invented."), ("Rain", "Natural.")]),
    mc("u1s1p18", "H", "O1", "Why is science split into areas such as physics and biology?", "Science is a very big subject, so areas focus on different questions.", [("Areas never overlap.", "They often overlap."), ("Only one area is real science.", "All are."), ("To make it harder.", "No.")]),
]
S1_ADV = [
    adv(ex("u1s1a1", "VH", "O1", "Choose ONE problem caused by electricity, transport or materials and explain how science could help reduce it.",
           [("names a problem", ["global warming|climate|pollution|plastic|carbon dioxide"]), ("names a scientific solution", ["solar|wind|electric car|recycl|biodegrad|renewable"]), ("explains how it helps", ["less|reduce|fewer|instead"])],
           "Burning fossil fuels for electricity adds carbon dioxide, causing global warming. Science has developed solar panels and wind turbines, which generate electricity without burning fuel, so less carbon dioxide is released.", need=2)),
    adv(mc("u1s1a2", "VH", "O1", "Which question CANNOT be answered by science?", ("Which painting is the most beautiful?", "Correct – this is an opinion, not testable."),
           [("Does fertiliser make beans grow taller?", "Testable."), ("How long does ice take to melt?", "Testable."), ("Which metal conducts heat best?", "Testable.")], skill="Reasoning")),
    adv(mc("u1s1a3", "VH", "O1", "A modern question: how do bees navigate? Which TWO areas of science might work together?", ("Biology and physics", "Correct – living things plus light/magnetism."),
           [("Meteorology and chemistry only", "Not the best pair."), ("Astronomy only", "No."), ("No science", "Science can study it.")], skill="Reasoning")),
    adv(od("u1s1a4", "VH", "O1", "Order these to show how a discovery becomes useful.", ["A scientist investigates and publishes results", "Other scientists check and repeat the work", "Engineers use the knowledge to design technology", "People use the new technology"])),
]

# ---------------------------------------------------------------- 1.2
S2_REQ = [
    od("u1s2r1", "M", "O2", "Put the steps of scientific enquiry in order.", ["Observation", "Question", "Hypothesis", "Prediction", "Investigation", "Conclusion"]),
    gd("u1s2r2", "H", "O2", "Testable hypothesis?", ["Testable?"],
       [("Plants grow faster under blue light than red light", ["Yes"]), ("Plants are happier under blue light", ["No"]), ("Sugar makes water freeze more slowly", ["Yes"]), ("Cats prefer music to silence", ["No"])], skill="Data"),
    gd("u1s2r3", "H", "O3", "Heating water: 'The temperature depends on how long it is heated.' Name each variable.", ["Variable"],
       [("Heating time", ["Independent"]), ("Temperature of the water", ["Dependent"]), ("Volume of water", ["Control"]), ("Type of beaker", ["Control"])], skill="Data"),
    mc("u1s2r4", "M", "O3", "What makes a test fair?", ("Only the independent variable is changed; all control variables stay the same.", "Correct."),
       [("Everyone gets a turn.", "Not the science meaning."), ("Changing many variables at once.", "Then you cannot tell which one caused the result."), ("Using the most expensive apparatus.", "No.")]),
    mc("u1s2r5", "H", "O4", "The true length of a pencil is 15.0 cm. Which set of results is precise but NOT accurate?", ("16.2, 16.3, 16.2 cm", "Correct: close together, but far from 15.0."),
       [("15.0, 15.1, 14.9 cm", "Accurate and precise."), ("13.5, 16.8, 15.2 cm", "Not precise."), ("15.0 cm once", "One reading cannot show precision.")], skill="Data"),
    gr("u1s2r6", "H", "O4", "Data: Huan's 100 m race times. Plot the points.", {"label": "Race number", "min": 0, "max": 6, "step": 1}, {"label": "Time (s)", "min": 0, "max": 24, "step": 2},
       [[1, 21], [2, 20], [3, 18], [4, 17], [5, 16], [6, 15]],
       follow=mc("u1s2r6f", "H", "O4", "What is the trend?", ("His time goes down – he is getting faster.", "Correct."), [("He is getting slower.", "Times fall."), ("No pattern.", "There is a clear trend."), ("Times go up then down.", "They fall steadily.")])),
    ex("u1s2r7", "H", "O4", "Huan's hypothesis was 'race time depends on the amount of training'. Write a conclusion using his results (21 s → 15 s).",
       [("time decreased from 21 s to 15 s", ["21", "15", "faster|decreas|fell|went down"]), ("supports the hypothesis / training leads to faster times", ["support|training"])],
       "His time fell from 21 s to 15 s as he trained, so training led to faster race times. The results support the hypothesis.", need=2),
    mc("u1s2r8", "VH", "O2", "In the ice-pop investigation, bags with more sugar took longer to freeze. What should happen next?", ("The evidence supports the hypothesis, so we state a conclusion (and could test further).", "Correct."),
       [("Change the hypothesis because it was right.", "Only change it if results disagree."), ("Ignore the results.", "Never ignore evidence."), ("Say sugar has no effect.", "The results show an effect.")], skill="Reasoning"),
]
S2_PRAC = [
    mc("u1s2p01", "M", "O2", "A hypothesis is…", "an idea that might explain an observation", [("a final answer", "It must be tested."), ("a piece of apparatus", "No."), ("a measurement", "No.")]),
    mc("u1s2p02", "M", "O2", "A prediction often uses the words…", "If … then …", [("Once upon a time", "No."), ("Maybe never", "No."), ("Always and never", "No.")]),
    mc("u1s2p03", "M", "O3", "A variable is…", "anything that can change", [("something that never changes", "No."), ("a result", "Not exactly."), ("a scientist", "No.")]),
    mc("u1s2p04", "M", "O3", "The independent variable is the one…", "we change on purpose", [("that changes as a result", "Dependent."), ("we keep the same", "Control."), ("we ignore", "No.")]),
    mc("u1s2p05", "M", "O3", "The dependent variable is the one…", "that changes as a result and is measured", [("we change on purpose", "Independent."), ("we keep the same", "Control."), ("that is never measured", "No.")]),
    mc("u1s2p06", "H", "O3", "In the ice-pop test, what was the independent variable?", "Amount of sugar", [("Freezing time", "Dependent."), ("Volume of liquid", "Control."), ("The freezer", "Control.")]),
    mc("u1s2p07", "H", "O3", "In the ice-pop test, why were the bags identical with the same volume of liquid?", "To keep control variables the same so the test is fair", [("To save money", "No."), ("To make it faster", "No."), ("Because sugar is heavy", "No.")]),
    mc("u1s2p08", "H", "O3", "How an animal burrows into the ground is best investigated by…", "careful observation", [("a fair test changing one variable", "Not every question needs a fair test."), ("guessing", "No."), ("a hazard symbol", "No.")]),
    mc("u1s2p09", "M", "O4", "A measurement close to the true value is…", "accurate", [("precise", "Precise = close to each other."), ("biased", "No."), ("a hypothesis", "No.")]),
    mc("u1s2p10", "M", "O4", "Repeated results that are close together are…", "precise", [("accurate", "Accurate = close to true value."), ("random", "No."), ("wrong", "Not necessarily.")]),
    mt("u1s2p11", "M", "O4", "Match each instrument to what it measures.", [("Thermometer", "temperature"), ("Stopwatch", "time"), ("Telescope", "faraway objects"), ("Hand lens", "tiny objects")]),
    mc("u1s2p12", "H", "O4", "Which way of presenting data best shows a trend over time?", "A line graph", [("A list of names", "No."), ("A photo", "No."), ("A single number", "No.")]),
    mc("u1s2p13", "M", "O4", "A good conclusion must…", "answer the question, be based on the results and support or disprove the hypothesis", [("agree with what you hoped", "Be objective."), ("ignore the results", "No."), ("be very long", "No.")]),
    mc("u1s2p14", "M", "O2", "Which attitude means asking questions instead of believing everything?", "Healthy scepticism", [("Perseverance", "Keeping going."), ("Co-operation", "Teamwork."), ("Curiosity", "Wanting to find out.")]),
    mt("u1s2p15", "H", "O2", "Match each attitude to its meaning.", [("Integrity", "always being truthful about results"), ("Perseverance", "keep going when it is difficult"), ("Open-mindedness", "listening to other ideas"), ("Objectivity", "accepting a result you do not like")]),
    mc("u1s2p16", "H", "O4", "Precise, repeatable results are also called…", "reliable", [("biased", "No."), ("accurate always", "Not always."), ("anomalous", "Anomalous = do not fit.")]),
    od("u1s2p17", "M", "O3", "Order the five planning steps.", ["Ask a question and make a hypothesis", "Identify the variables", "Decide what to measure and how to record it", "Choose materials and equipment", "Decide how to analyse the data"]),
    mc("u1s2p18", "H", "O2", "Every model has limitations. This means…", "no model shows the real world completely", [("models are useless", "They are very useful."), ("models are always wrong", "Not always wrong – just incomplete."), ("only computer models work", "No.")]),
]
S2_ADV = [
    adv(ex("u1s2a1", "VH", "O3", "Plan a fair test of the hypothesis 'The time for sugar to dissolve depends on the temperature of the water'. Name the three types of variable.",
           [("independent = temperature", ["independent.*temperat|temperat.*independent|change the temperature"]), ("dependent = time to dissolve", ["dependent.*time|time.*dissolv|measure the time"]), ("controls: same mass of sugar / volume / stirring", ["same|control"])],
           "Independent: water temperature. Dependent: time for the sugar to dissolve. Control: same mass and type of sugar, same volume of water, same container and same stirring.", need=2)),
    adv(mc("u1s2a2", "VH", "O4", "Results of 5 repeats: 12.1, 12.3, 15.8, 12.2, 12.0 s. What should you do with 15.8 s?", ("Treat it as anomalous: check it, and leave it out of the mean if it was a mistake.", "Correct."),
           [("Use it – it is the biggest.", "It does not fit the pattern."), ("Change all the other results.", "Never."), ("Stop the investigation.", "No.")], skill="Data")),
    adv(nm("u1s2a3", "VH", "O4", "Find the mean of 12.1, 12.3, 12.2 and 12.0 s.", 12.15, "s", tol=0.01, reason="(12.1 + 12.3 + 12.2 + 12.0) ÷ 4 = 48.6 ÷ 4 = 12.15 s.")),
    adv(mc("u1s2a4", "VH", "O2", "Computer models are used to forecast the weather. Why are forecasts sometimes wrong?", ("Models simplify the real atmosphere, so they have limitations.", "Correct."),
           [("Computers cannot do maths.", "No."), ("Weather never changes.", "No."), ("Scientists guess randomly.", "No.")], skill="Reasoning")),
]

# ---------------------------------------------------------------- 1.3
S3_REQ = [
    ms("u1s3r1", "M", "O5", "Select ALL the safe behaviours in a laboratory.", ["Wear safety goggles when heating", "Read the instructions first", "Wash your hands after lab work", "Report spills straight away"],
       [("Eat your snack at the bench", "Never eat or drink in the lab."), ("Taste chemicals to identify them", "Never taste anything.")]),
    gd("u1s3r2", "H", "O5", "Match each hazard to the correct precaution.", ["Precaution"],
       [("Flammable", ["Keep away from flames"]), ("Corrosive", ["Avoid skin contact; wear gloves and goggles"]), ("Acutely toxic", ["Never breathe in or swallow"]), ("Hazardous to the environment", ["Never pour down the drain"])], skill="Data"),
    mc("u1s3r3", "M", "O5", "When heating a test tube, why point the open end away from people?", ("Hot liquid can spit out of the tube.", "Correct."), [("It heats faster.", "No."), ("To see better.", "No."), ("To keep it clean.", "No.")]),
    mt("u1s3r4", "M", "O5", "Match each piece of apparatus to its use.", [("Measuring cylinder", "measures the volume of a liquid"), ("Bunsen burner", "heats substances"), ("Test tube", "holds or heats small amounts"), ("Conical flask", "holds chemicals or collects liquids")]),
    mc("u1s3r5", "H", "O5", "To measure 20 cm³ of water, which is most accurate?", ("A 50 cm³ measuring cylinder", "Correct – smallest suitable scale."), [("A 500 cm³ beaker", "Much less accurate."), ("A test tube", "Not marked for volume."), ("A Bunsen burner", "Heats; does not measure.")], skill="Measurement"),
    ex("u1s3r6", "H", "O5", "A strong acid has a corrosive symbol. Describe the danger and two precautions.",
       [("destroys / burns skin and materials", ["destroy|burn|damag"]), ("wear goggles / gloves", ["goggles|gloves|eye"]), ("handle carefully / small amounts / clean spills", ["careful|small|spill|report|wash"])],
       "Corrosive substances destroy skin and other materials. Wear goggles (and gloves), use small amounts, and report and clean any spill straight away.", need=2),
    tb("u1s3r7", "H", "O5", "Choose the best measuring cylinder (10, 50 or 100 cm³) for each volume.", ["Volume to measure (cm³)", "Best cylinder (cm³)"], [["8", B(10)], ["35", B(50)], ["72", B(100)]], skill="Measurement",
       hint="Pick the smallest cylinder that can hold the volume."),
    mc("u1s3r8", "VH", "O5", "A bottle shows the flame symbol and the exclamation-mark symbol. What does this tell you?", ("It catches fire easily and is a moderate hazard if touched or breathed in.", "Correct."),
       [("It is safe to drink.", "Never."), ("It only harms plants.", "No."), ("It is corrosive.", "That is a different symbol.")], skill="Reasoning"),
]
S3_PRAC = [
    mc("u1s3p01", "M", "O5", "What should you wear when heating substances?", "Safety goggles", [("Sunglasses", "No."), ("Nothing extra", "Goggles protect eyes."), ("A hat", "No.")]),
    mc("u1s3p02", "M", "O5", "Flammable means…", "catches fire easily", [("poisonous", "Toxic."), ("destroys skin", "Corrosive."), ("harms the environment", "Different symbol.")]),
    mc("u1s3p03", "M", "O5", "Corrosive substances…", "destroy skin and other materials", [("catch fire easily", "Flammable."), ("are always safe", "No."), ("are only gases", "No.")]),
    mc("u1s3p04", "M", "O5", "What should you do before using any substance?", "Check the label and hazard symbol", [("Smell it closely", "Not safe."), ("Taste it", "Never."), ("Mix it with water", "Not without instructions.")]),
    mc("u1s3p05", "M", "O5", "Substances hazardous to the environment must never be…", "poured down the drain", [("labelled", "They must be labelled."), ("stored safely", "They should be."), ("used by teachers", "Teachers can use them safely.")]),
    mc("u1s3p06", "H", "O5", "Why must you never eat or drink in the lab?", "Food could be contaminated with harmful chemicals.", [("It is rude.", "Safety is the reason."), ("Food is not allowed anywhere.", "No."), ("It makes experiments slower.", "No.")]),
    mc("u1s3p07", "M", "O5", "What is apparatus?", "Scientific equipment", [("A hazard symbol", "No."), ("A type of chemical", "No."), ("A scientist", "No.")]),
    mc("u1s3p08", "M", "O5", "Which apparatus is used to heat substances?", "Bunsen burner", [("Measuring cylinder", "Measures."), ("Beaker only", "Holds; the burner heats."), ("Thermometer", "Measures temperature.")]),
    mc("u1s3p09", "H", "O5", "A health hazard symbol means the substance…", "can cause serious long-term damage", [("catches fire", "Flammable."), ("is safe to touch", "No."), ("only harms fish", "No.")]),
    mc("u1s3p10", "M", "O5", "What should you do if you break a beaker?", "Tell your teacher straight away", [("Hide it", "No."), ("Pick it up with bare hands", "Unsafe."), ("Keep working", "Report it.")]),
    mc("u1s3p11", "H", "O5", "A moderate hazard (exclamation mark) can…", "cause harm if touched or breathed in", [("explode always", "No."), ("never harm you", "No."), ("only damage metal", "No.")]),
    mc("u1s3p12", "H", "O5", "Why is a 500 cm³ beaker poor for measuring 20 cm³?", "Its scale is too large, so the reading is not accurate.", [("It is too small.", "It is too big."), ("Beakers cannot hold water.", "They can."), ("It is made of glass.", "Not the reason.")], skill="Measurement"),
    ms("u1s3p13", "M", "O5", "Select ALL the rules about heating a test tube.", ["Point the open end away from everyone", "Wear goggles", "Use a test-tube holder"], [("Look into the tube while heating", "Dangerous."), ("Fill it to the top", "Can spit out.")]),
    mc("u1s3p14", "M", "O5", "Acutely toxic substances are…", "poisonous even from a single contact", [("only slightly harmful", "Very dangerous."), ("flammable", "Different symbol."), ("good for plants", "No.")]),
    mc("u1s3p15", "H", "O5", "Why keep your work area clean and tidy?", "To avoid accidents such as knocking over chemicals", [("To finish faster", "Not the main reason."), ("Because teachers like it", "Safety is the reason."), ("It changes results", "Not the main reason.")]),
    mc("u1s3p16", "M", "O5", "After lab work you should…", "wash your hands thoroughly", [("lick your fingers", "Never."), ("leave everything out", "Tidy up."), ("taste the result", "Never.")]),
    od("u1s3p17", "M", "O5", "Order the safe steps for an experiment.", ["Read the instructions", "Put on goggles", "Check the labels", "Carry out the experiment", "Clean up and wash hands"]),
    mc("u1s3p18", "H", "O5", "Which is the most accurate way to measure 7.5 cm³ of liquid?", "A 10 cm³ measuring cylinder", [("A 100 cm³ beaker", "Too coarse."), ("A teaspoon", "Not accurate."), ("A conical flask", "Not for measuring.")], skill="Measurement"),
]
S3_ADV = [
    adv(ex("u1s3a1", "VH", "O5", "Write a risk assessment for heating salt water in a test tube until it boils.",
           [("hazard: hot liquid spitting / burns", ["spit|burn|hot"]), ("precaution: goggles, holder, point away", ["goggles|holder|point|away"]), ("precaution: heat gently / do not fill tube", ["gently|small|half|not fill"])],
           "Hazard: boiling salt water can spit out and burn skin or eyes. Precautions: wear goggles, use a test-tube holder, fill only a small amount, heat gently and point the open end away from everyone.", need=2)),
    adv(mc("u1s3a2", "VH", "O5", "A measuring cylinder has marks every 2 cm³. A student records 13 cm³. Is this a good reading?", ("It is an estimate between marks – a cylinder with smaller divisions would be more accurate.", "Correct."),
           [("Yes – it is exact.", "It lies between marks."), ("No – volume can't be measured.", "It can."), ("No – it should be 14 cm³.", "Not necessarily.")], skill="Measurement")),
    adv(mc("u1s3a3", "VH", "O5", "Why are hazard symbols pictures rather than words?", ("People who speak any language can understand them quickly.", "Correct."),
           [("Words are not allowed.", "No."), ("Pictures are cheaper.", "Not the reason."), ("Only for young children.", "For everyone.")], skill="Reasoning")),
    adv(nm("u1s3a4", "VH", "O5", "Measuring 20 cm³, a 500 cm³ beaker can be wrong by about ±25 cm³ and a 50 cm³ cylinder by about ±0.5 cm³. How many times smaller is the cylinder's possible error?", 50, "times", reason="25 ÷ 0.5 = 50.")),
]

# ---------------------------------------------------------------- 1.4
S4_REQ = [
    mc("u1s4r1", "M", "O6", "What is the difference between science and technology?", ("Science develops new knowledge; technology applies it to solve problems.", "Correct."),
       [("They are exactly the same.", "Related but different."), ("Technology comes first, then science.", "Usually knowledge comes first."), ("Science only uses computers.", "No.")]),
    mc("u1s4r2", "M", "O6", "What is peer review?", ("Other scientists check a report's method and conclusions.", "Correct."), [("Pupils marking each other's homework.", "Not in science."), ("A type of experiment.", "No."), ("Checking spelling only.", "No.")]),
    gd("u1s4r3", "H", "O6", "Benefit or problem of science and technology?", ["Type"],
       [("Antibiotics cure deadly infections", ["Benefit"]), ("Overused antibiotics lead to resistant bacteria", ["Problem"]), ("Solar panels generate electricity", ["Benefit"]), ("Plastic waste harms sea life", ["Problem"]), ("Weather technology improves forecasts", ["Benefit"])], skill="Data"),
    mc("u1s4r4", "H", "O6", "What does 'bias' mean when you read information online?", ("Telling only one side of the story", "Correct."), [("Being very accurate", "No."), ("Using lots of data", "No."), ("Written by a scientist", "Scientists can be biased too.")]),
    ms("u1s4r5", "H", "O6", "Select ALL good questions to ask when checking an online source for bias.", ["Who wrote it?", "Do they want to persuade me?", "Do other sources agree?"], [("Does it have nice pictures?", "Not a check of bias."), ("Is it long?", "Length does not matter.")]),
    ex("u1s4r6", "H", "O6", "Explain what Newton meant by 'standing on the shoulders of giants'.",
       [("built on the work of earlier scientists", ["earlier|previous|before|other scientists|built"]), ("so he could see further / discover more", ["further|more|new"])],
       "He meant that his discoveries were built on the work of earlier scientists, which let him see further and discover more than he could alone.", need=2),
    tb("u1s4r7", "H", "O6", "Data: a city's electricity sources. Complete the percentages (total must be 100%).", ["Source", "Percentage"],
       [["Coal", "45"], ["Gas", "25"], ["Solar", "18"], ["Wind", B(12)]], skill="Data", hint="100 − 45 − 25 − 18 = ?"),
    mc("u1s4r8", "VH", "O6", "Science cannot stop floods. How can it still help?", ("Early warnings, flood barriers and stronger buildings reduce the damage.", "Correct."),
       [("It can make rain stop.", "No."), ("It cannot help at all.", "It can reduce damage."), ("By moving rivers to space.", "No.")], skill="Reasoning"),
]
S4_PRAC = [
    mc("u1s4p01", "M", "O6", "ICT stands for…", "information and communications technology", [("internet and computer toys", "No."), ("ice-cream technology", "No."), ("international chemical testing", "No.")]),
    mc("u1s4p02", "M", "O6", "Driverless vehicles use ___ to track cars and read traffic lights.", "cameras and sensors", [("magnets only", "No."), ("thermometers", "No."), ("hazard symbols", "No.")]),
    mc("u1s4p03", "M", "O6", "Burning coal adds which gas that traps heat?", "Carbon dioxide", [("Oxygen", "No."), ("Nitrogen", "No."), ("Helium", "No.")]),
    mc("u1s4p04", "H", "O6", "Why can overusing antibiotics be a problem?", "Bacteria can become resistant so antibiotics stop working.", [("Antibiotics become stronger.", "No."), ("Viruses grow bigger.", "No."), ("It cures all diseases.", "No.")]),
    mc("u1s4p05", "M", "O6", "Which is an example of misusing technology?", "Cyber-bullying", [("Video-calling family", "Normal use."), ("Checking the weather", "Normal use."), ("Learning online", "Normal use.")]),
    mc("u1s4p06", "M", "O6", "If you are cyber-bullied you should…", "tell a teacher, parent or trusted adult", [("keep it secret", "Tell someone."), ("bully back", "No."), ("delete your account and say nothing", "Tell someone.")]),
    mc("u1s4p07", "H", "O6", "To evaluate means…", "list positive and negative points, then judge using the evidence", [("only list good points", "Both."), ("guess", "No."), ("copy someone else's opinion", "No.")]),
    mc("u1s4p08", "M", "O6", "Fertilisers and pesticides help farmers but too much can…", "pollute the environment", [("make crops invisible", "No."), ("stop the rain", "No."), ("cure diseases", "No.")]),
    mc("u1s4p09", "M", "O6", "Which generate electricity without burning fuel?", "Solar panels and wind turbines", [("Coal power stations", "Burn fuel."), ("Gas power stations", "Burn fuel."), ("Car engines", "Burn fuel.")]),
    mc("u1s4p10", "H", "O6", "How does technology help science?", "Computers let scientists handle huge amounts of data.", [("It replaces all experiments.", "No."), ("It makes science unnecessary.", "No."), ("It stops peer review.", "No.")]),
    mc("u1s4p11", "M", "O6", "Medical technology improves…", "how illnesses are diagnosed and treated", [("weather forecasts", "Weather technology."), ("crop growth", "Food technology."), ("internet speed", "ICT.")]),
    mc("u1s4p12", "H", "O6", "Is there a drug that completely prevents or cures cancer?", "No – science has found many treatments but not a complete cure yet.", [("Yes, it is sold everywhere.", "No."), ("Yes, but it is secret.", "No."), ("Science has given up.", "Research continues.")]),
    mc("u1s4p13", "H", "O6", "Why are scientific reports shared?", "So others can check and build on the results", [("To keep them secret", "No."), ("To make money only", "No."), ("Because it is a rule for pupils", "No.")]),
    mc("u1s4p14", "M", "O6", "Plastic is very useful, but overusing it has…", "polluted our planet", [("cleaned the oceans", "No."), ("stopped global warming", "No."), ("had no effect", "No.")]),
    mc("u1s4p15", "H", "O6", "A website selling a cream says 'scientists prove it works', with no evidence. You should…", "be sceptical and check other, independent sources", [("believe it", "It may be biased."), ("buy two", "No."), ("share it with everyone", "Check first.")], skill="Reasoning"),
    mc("u1s4p16", "M", "O6", "Food technology helps farmers…", "grow more, healthier crops", [("predict earthquakes", "No."), ("make phones", "No."), ("cure cancer", "No.")]),
    mt("u1s4p17", "M", "O6", "Match each technology to its area.", [("Better forecasts", "weather technology"), ("Faster messaging", "ICT"), ("New medicines", "medical technology"), ("Higher crop yields", "food technology")]),
    mc("u1s4p18", "H", "O6", "Dubai plans for about what share of its transport to be driverless by 2030?", "A quarter", [("All of it", "No."), ("None", "No."), ("Half", "No.")]),
]
S4_ADV = [
    adv(ex("u1s4a1", "VH", "O6", "Evaluate driverless cars: give one advantage, one disadvantage and your judgement.",
           [("advantage", ["safer|fewer accidents|convenient|elderly|disab|traffic"]), ("disadvantage", ["fault|hack|jobs|expensive|error|bug|sensor"]), ("judgement", ["overall|i think|judge|so|therefore"])],
           "Advantage: sensors react quickly and could reduce accidents. Disadvantage: sensors or software could fail, and drivers may lose jobs. Overall they could be useful if tested carefully and safety rules are strict.", need=2)),
    adv(mc("u1s4a2", "VH", "O6", "Two websites disagree about whether a food is healthy. One is written by the company that sells it. Which is more likely to be biased?", ("The company's site – it wants to persuade you to buy.", "Correct."),
           [("The independent site.", "Less reason to persuade."), ("Both equally.", "The seller has a clear motive."), ("Neither – websites are never biased.", "They can be.")], skill="Reasoning")),
    adv(mc("u1s4a3", "VH", "O6", "Why does peer review make scientific results more trustworthy?", ("Independent experts check the method and conclusions for mistakes before others rely on them.", "Correct."),
           [("It makes reports longer.", "No."), ("It guarantees results are always right.", "It reduces errors but cannot guarantee."), ("Only friends review.", "Reviewers are independent.")], skill="Reasoning")),
    adv(nm("u1s4a4", "VH", "O6", "A town gets 20% of its electricity from solar and plans to double it. What percentage will be solar then?", 40, "%")),
]

POOLS = {"1.1": (S1_REQ, S1_PRAC, S1_ADV), "1.2": (S2_REQ, S2_PRAC, S2_ADV), "1.3": (S3_REQ, S3_PRAC, S3_ADV), "1.4": (S4_REQ, S4_PRAC, S4_ADV)}

STOPS = {
    "1.1": [stop("u1v1a", "can be explained by science", mc("u1v1a_q", "M", "O1", "Science is…", "the study of how things work", [("a list of rules", "No."), ("only maths", "No."), ("guessing", "No.")])),
            stop("u1v1b", "Meteorology is the study of the weather", mc("u1v1b_q", "M", "O1", "Which area studies living things?", "Biology", [("Physics", "Forces and energy."), ("Chemistry", "Matter."), ("Astronomy", "Space.")])),
            stop("u1v1c", "That is how our knowledge grows", mc("u1v1c_q", "H", "O1", "How does scientific knowledge grow?", "Each discovery becomes a starting point for the next.", [("One person discovers everything.", "No."), ("By keeping results secret.", "No."), ("By guessing.", "No.")]))],
    "1.2": [stop("u1v2a", "Science is a cycle", mc("u1v2a_q", "M", "O2", "What comes straight after the hypothesis?", "A prediction", [("A conclusion", "Later."), ("An observation", "Before."), ("Nothing", "No.")])),
            stop("u1v2b", "how long it is heated", mc("u1v2b_q", "H", "O3", "'Temperature depends on heating time.' The dependent variable is…", "the temperature", [("the heating time", "Independent."), ("the beaker", "Control."), ("the burner", "Control.")])),
            stop("u1v2c", "we call it a fair test", mc("u1v2c_q", "H", "O3", "Variables kept the same are called…", "control variables", [("dependent variables", "No."), ("independent variables", "No."), ("anomalies", "No.")])),
            stop("u1v2d", "Precise, repeatable results are also called reliable", mc("u1v2d_q", "H", "O4", "Results close to the true value are…", "accurate", [("precise", "Close to each other."), ("biased", "No."), ("anomalous", "No.")]))],
    "1.3": [stop("u1v3a", "wash your hands thoroughly after lab work", mc("u1v3a_q", "M", "O5", "When heating a test tube you should point the open end…", "away from everyone", [("at yourself", "No."), ("at your partner", "No."), ("upwards into your face", "No.")])),
            stop("u1v3b", "avoid handling it", mc("u1v3b_q", "M", "O5", "A flame symbol means…", "flammable – keep away from flames", [("corrosive", "No."), ("toxic", "No."), ("safe", "No.")])),
            stop("u1v3c", "more accurate than a 500 cubic centimetre beaker", mc("u1v3c_q", "H", "O5", "To measure 20 cm³ accurately, choose…", "a 50 cm³ measuring cylinder", [("a 500 cm³ beaker", "Less accurate."), ("a test tube", "No scale."), ("a Bunsen burner", "No.")]))],
    "1.4": [stop("u1v4a", "make a judgement based on the evidence", mc("u1v4a_q", "M", "O6", "Peer review means…", "other scientists check the method and conclusions", [("pupils check homework", "No."), ("you check your own work only", "No."), ("a vote", "No.")])),
            stop("u1v4b", "Would you ride in one", mc("u1v4b_q", "M", "O6", "Technology is…", "using scientific knowledge to solve problems", [("the same as science", "Related, not the same."), ("only computers", "No."), ("a hazard", "No.")])),
            stop("u1v4c", "whether other sources agree", mc("u1v4c_q", "H", "O6", "Bias means…", "telling only one side of the story", [("telling the truth", "No."), ("using lots of data", "No."), ("being a scientist", "No.")]))],
}

MINDMAP = {"id": "root", "t": "Introducing science", "sec": None, "kids": [
    {"id": "what", "t": "What is science?", "d": "The study of how things work: knowledge + processes. Physics, chemistry, biology, astronomy, meteorology.", "obj": "O1", "sec": "1.1"},
    {"id": "enq", "t": "Scientific enquiry", "d": "Observation → question → hypothesis → prediction → investigation → conclusion. Hypotheses must be testable.", "obj": "O2", "sec": "1.2"},
    {"id": "vars", "t": "Variables & fair tests", "d": "Independent (changed) • dependent (measured) • control (kept the same).", "obj": "O3", "sec": "1.2"},
    {"id": "data", "t": "Data", "d": "Accurate = close to true value • precise = close together • tables, bar charts, line graphs • conclusions.", "obj": "O4", "sec": "1.2"},
    {"id": "lab", "t": "Lab safety", "d": "Goggles • read labels • hazard symbols: flammable, corrosive, toxic… • choose accurate apparatus.", "obj": "O5", "sec": "1.3"},
    {"id": "use", "t": "Using science", "d": "Science → technology • peer review • benefits and problems • check for bias.", "obj": "O6", "sec": "1.4"},
]}
