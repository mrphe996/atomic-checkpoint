from science_v2.k import Unit
U = Unit("s7u08")

U.q("E", "8.1", "O1", "Jo says all acids are dangerous. Which is the best reply?", ("Some acids, like lemon juice and vinegar, are weak and safe to eat", "Strong acids are dangerous; weak ones can be harmless."), [("She is right", "We eat citric acid in fruit."), ("No acid is dangerous", "Strong acids can burn skin.")])
U.q("R", "8.2", "O2", "Which household substance is most likely to be an alkali?", ("Soap or oven cleaner", "Many cleaners are alkaline."), [("Vinegar", "Vinegar is an acid."), ("Pure water", "Pure water is neutral.")])
U.q("P", "8.3", "O3", "Universal indicator is added to a solution with pH 2. What colour will it be?", ("Red", "Strong acids turn universal indicator red."), [("Purple", "Purple shows a strong alkali."), ("Green", "Green shows a neutral solution.")])
U.q("P", "8.4", "O4", "Alkali is added drop by drop to an acid with indicator. What happens to the pH?", ("It rises towards 7", "The alkali neutralises the acid."), [("It falls", "Adding alkali makes the solution less acidic."), ("It stays the same", "Neutralisation changes the pH.")])
U.q("R", "8.4", "O4", "Why is a bee sting (acidic) treated with bicarbonate of soda (alkaline)?", ("The alkali neutralises the acid", "Neutralisation reduces the sting."), [("The alkali kills the bee", "The bee is not involved any more."), ("It makes the sting more acidic", "An alkali raises the pH.")])
V2 = U.V2
