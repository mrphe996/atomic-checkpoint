from science_v2.k import Unit
U = Unit("s8u02")

U.q("R", "2.1", "O1", "Why are muscles found in pairs, such as the biceps and triceps?", ("Muscles can only pull, so one moves a bone and the other moves it back", "They are antagonistic pairs."), [("Muscles can only push", "Muscles contract and pull."), ("One muscle is a spare", "Both are used.")])
U.q("P", "2.1", "O1", "When the biceps contracts, what happens to the arm?", ("The lower arm is raised (the elbow bends)", "The biceps pulls the lower arm up."), [("The arm straightens", "That happens when the triceps contracts."), ("Nothing", "Contracting muscles move bones.")])
U.q("P", "2.2", "O2", "When you breathe in, what happens to the volume of your chest?", ("It increases, so air moves in", "The ribs move up and out and the diaphragm flattens."), [("It decreases", "That happens when you breathe out."), ("It stays the same", "Breathing changes the chest volume.")])
U.q("E", "2.2", "O3", "Kai says we breathe in oxygen and breathe out only carbon dioxide. What is wrong?", ("Exhaled air still contains a lot of oxygen (about 16%) and mostly nitrogen", "Only part of the oxygen is absorbed."), [("Nothing", "Exhaled air is not pure carbon dioxide."), ("We breathe out only nitrogen", "Exhaled air contains several gases.")])
U.q("R", "2.3", "O4", "Why does the heart rate rise during exercise?", ("Muscles need more oxygen and glucose, so blood must be pumped faster", "Faster delivery supports faster respiration."), [("To cool the body", "Sweating cools the body."), ("Because the heart gets tired", "A tired heart does not speed up.")])
U.q("P", "2.3", "O4", "Which blood vessels carry blood away from the heart at high pressure?", ("Arteries", "Arteries have thick walls for high pressure."), [("Veins", "Veins return blood to the heart."), ("Capillaries", "Capillaries have very thin walls.")])
V2 = U.V2
