# -*- coding: utf-8 -*-
"""Stage 7 · Unit 6 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

VIDEOS = {}

VIDEOS["6.1"] = [
    dict(kind="hook", title="Is the school bus late?", steps=[
        dict(say="Some students say: the school bus is late more often on rainy days. The head teacher wants evidence before she phones the bus company.",
             do=[E("🚌", 90, 170, 100), E("🌧️", 200, 170, 80, at=0.6), T("“The bus is late more often on **rainy days**.”", x=320, y=200)]),
        PAUSE("6.1-k1", "Which data would best test this prediction? Pause the video and choose.", "Which data would best test the prediction that the bus is late more often on rainy days?"),
    ]),
    dict(kind="hook", title="Two things for every day", steps=[
        dict(say="You need two facts for every school day: what the weather was, and whether the bus was late.",
             do=[TBL(["Date", "Weather", "Late?"], [["Mon", "rainy", "yes"], ["Tue", "dry", "no"], ["Wed", "dry", "yes"], ["Thu", "rainy", "yes"]], y=170), ROW(0, 0.4), ROW(1, 1), ROW(2, 1.6), ROW(3, 2.2)]),
        dict(say="Recording only the rainy days would not be enough. You could not compare them with the dry days.", do=[T("Only rainy days? Then there is nothing to **compare**.", x=560, y=250, color=RED, w=560)]),
    ]),
    dict(kind="recall", title="Tally marks", steps=[
        dict(say="Remember tally marks. They are grouped in fives: four strokes, and a fifth one across them.", do=[B("卌", x=80, y=160), T("= 5", x=170, y=178)]),
        dict(say="Two groups of five, and three more, make 13.", do=[B("卌 卌 |||", x=80, y=290), T("= 13", x=330, y=308, color=GREEN, at=2)]),
    ]),
    dict(kind="idea", title="Statistical questions", steps=[
        dict(say="A statistical question is answered by collecting data, and the answers can vary.", do=[T("A **statistical question** needs **data**, and the answers **vary**", x=80, y=160)]),
        dict(say="How many minutes late is the bus? That is a statistical question. It changes from day to day.", do=[T("“How many minutes late is the bus?”", x=80, y=260), E("✅", 640, 246, 50, at=2.4)]),
        dict(say="What time is the bus supposed to leave? That is not statistical. It has one fixed answer.", do=[T("“What time should the bus leave?”", x=80, y=350), E("❌", 640, 336, 50, at=2.4)]),
        dict(say="A prediction is a statement you can test with data, such as: the bus is late more often on rainy days.", do=[T("A **prediction** can be tested with data", x=80, y=460, color=BLUE)]),
    ]),
    dict(kind="idea", title="Types of data", steps=[
        dict(say="There are three types of data. Categorical data is words or categories, like the weather: sunny, rainy or cloudy.",
             do=[TBL(["Type", "What it is", "Example"], [["**categorical**", "words or categories", "weather: sunny, rainy, cloudy"], ["**discrete**", "numbers you **count**", "number of late buses: 0, 1, 2 …"], ["**continuous**", "numbers you **measure**", "minutes late: 3.5, 12.25 …"]], y=170), ROW(0, 2)]),
        dict(say="Discrete data is numbers that you count. Only certain values are possible. You cannot have 2 and a half late buses.", do=[ROW(1, 0.3)]),
        dict(say="Continuous data is numbers that you measure, such as time, length or mass. Any value in a range is possible.", do=[ROW(2, 0.3)]),
        PAUSE("6.1-k2", "Your turn. Sort each piece of data into the correct type. Pause the video and try it.", "Sort the data: categorical, discrete or continuous?"),
    ]),
    dict(kind="idea", title="Check: which type?", steps=[
        dict(say="Ask yourself: is it a word, a count, or a measurement? Words are categorical. Counts are discrete. Measurements are continuous.",
             do=[T("a word → **categorical**", x=80, y=190, color=BLUE), T("a count → **discrete**", x=80, y=280, color=GREEN, at=3.4), T("a measurement → **continuous**", x=80, y=370, color=RED, at=5.4)]),
    ]),
    dict(kind="method", title="Planning an investigation", steps=[
        dict(say="Here is the method. Step 1: write a clear question or prediction.", do=[T("1. A clear **question** or prediction", x=80, y=170)]),
        dict(say="Step 2: decide which data you need, what type it is, and how to collect it.", do=[T("2. Which **data**? What type? How to collect it?", x=80, y=260)]),
        dict(say="Step 3: design a data collection sheet, and collect the data.", do=[T("3. Design a **collection sheet**; collect", x=80, y=350)]),
        dict(say="Step 4: present the data, and decide whether your prediction was right.", do=[T("4. Present it and reach a **conclusion**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A frequency table", steps=[
        dict(say="Sam counts the people in 20 cars at a crossing. He uses tallies, then writes the total for each number. The total is called the frequency.",
             do=[TBL(["People in car", "Tally", "Frequency"], [["1", "卌 ||||", "9"], ["2", "卌 |", "6"], ["3", "||", "2"], ["4", "||", "2"], ["5", "|", "1"]], y=160), ROW(0, 3), ROW(1, 3.5), ROW(2, 4), ROW(3, 4.5), ROW(4, 5)]),
        dict(say="Check by adding the frequencies. 9 plus 6 plus 2 plus 2 plus 1 is 20. That matches the 20 cars.", do=[MATH("9 + 6 + 2 + 2 + 1 = 20", x=700, y=260, color=GREEN), E("✅", 1130, 246, 50, at=4)]),
    ]),
    dict(kind="example", title="Grouping continuous data", steps=[
        dict(say="Students time their walk to school in minutes. Time is continuous, so we record it in groups, called classes.", do=[E("🚶", 90, 160, 90), T("time is **continuous** → use **groups**", x=210, y=190)]),
        dict(say="The first group is from 0, up to but not including 5. We write it with inequality signs.", do=[MATH("0 ≤ t < 5", x=80, y=310)]),
        dict(say="Then 5 up to 10, then 10 up to 15, and so on. There are no gaps and no overlaps.", do=[MATH("5 ≤ t < 10", x=380, y=310), MATH("10 ≤ t < 15", x=700, y=310, at=1.4), T("no gaps, no overlaps", x=80, y=420, color=BLUE, at=3)]),
        dict(say="A time of exactly 5 minutes goes in the second group, because that group starts at 5.", do=[T("exactly 5 minutes → **5 ≤ t < 10**", x=80, y=510, color=GREEN)]),
        PAUSE("6.1-k3", "Your turn. Which group does a time of 15 minutes go in? Pause and choose.", "A time of 15 minutes goes in which group?"),
    ]),
    dict(kind="example", title="Check: 15 minutes", steps=[
        dict(say="15 is not less than 15, so it cannot go in 10 up to 15. It goes in the group that starts at 15: 15 up to 20.", do=[MATH("10 ≤ t < 15", x=80, y=190, color=RED), E("❌", 420, 176, 50, at=1.6), MATH("15 ≤ t < 20", x=80, y=300, color=GREEN, at=3.4), E("✅", 420, 286, 50, at=4)]),
    ]),
    dict(kind="example", title="How to collect the data", steps=[
        dict(say="Choose the right method. To find the favourite school lunch, ask people. That is a survey.", do=[E("🍱", 90, 160, 80), T("favourite lunch → a **survey**", x=200, y=185)]),
        dict(say="To find how high a ball bounces, drop it and measure. That is an experiment.", do=[E("🏀", 90, 280, 80), T("bounce height → an **experiment**", x=200, y=305)]),
        dict(say="To find last year's rainfall, look it up. That is using existing records.", do=[E("☔", 90, 400, 80), T("last year's rainfall → **existing records**", x=200, y=425)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="In one month there were 15 dry days, and the bus was late on 6 of them. There were 5 rainy days, and it was late on 3. Here is Tara's conclusion. Which line is wrong?",
             do=LINES("Tara", "dry: late 6 of 15 · rainy: late 3 of 5", ["Late on 6 dry days and 3 rainy days", "6 is more than 3, so the bus is late more on dry days"])),
        dict(say="Line 2 is wrong. There were many more dry days, so comparing the counts is not fair. Compare the fractions.", do=[dict(a="cross", id="l2")]),
        dict(say="On dry days it was late 6 times out of 15, which is 40 percent. On rainy days, 3 out of 5, which is 60 percent. So the bus really is late more often on rainy days.",
             do=[MATH("dry: 6 ÷ 15 = 40%", x=110, y=420, color=BLUE), MATH("rainy: 3 ÷ 5 = 60%", x=110, y=500, color=RED, at=4.4)]),
    ]),
    dict(kind="life", title="Counting a whole country", steps=[
        dict(say="The biggest investigation of all is a census. A census collects data about every person in a country.", do=[E("🌍", 90, 170, 100), T("A **census** counts **everyone** in a country", x=230, y=200)]),
        dict(say="Many countries hold one every 10 years. It records categorical data, like the language people speak, and discrete data, like the number of people in each home.",
             do=[T("usually every **10 years**", x=230, y=300), T("language → categorical · people in a home → discrete", x=230, y=390, color=BLUE, at=4)]),
        dict(say="Governments use the results to plan new schools, hospitals and roads.", do=[E("🏫", 230, 470, 70), E("🏥", 330, 470, 70, at=0.4), E("🛣️", 430, 470, 70, at=0.8)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("6.1-k4", "One last question. What is the capital of Peru? Is that a statistical question? Pause the video and choose.", "“What is the capital of Peru?” is …"),
        dict(say="It is not a statistical question. It has one fixed answer, and you do not need to collect data that varies.", do=[B("not a statistical question", x=80, y=190, color=RED), T("one fixed answer – no varying data", x=80, y=300, at=2)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a statistical question is answered with data that can vary.", do=[T("• Statistical question: data that **varies**", x=80, y=170)]),
        dict(say="Categorical means words. Discrete means counted. Continuous means measured.", do=[T("• Categorical = words; discrete = counted; continuous = measured", x=80, y=250)]),
        dict(say="Plan: question, data, collect, present, conclude.", do=[T("• Question → data → collect → present → conclude", x=80, y=330)]),
        dict(say="Use tallies and frequency tables, and compare fairly, with fractions or percentages.", do=[T("• Tallies, frequency tables, fair comparisons", x=80, y=410)]),
    ]),
]

VIDEOS["6.2"] = [
    dict(kind="hook", title="Testing the soup", steps=[
        dict(say="A cook makes a huge pot of soup. To check the salt, she does not drink the whole pot. She stirs it, and tastes one spoonful.",
             do=[E("🍲", 90, 170, 120), E("🥄", 250, 190, 80, at=4.4), T("stir, then taste **one spoonful**", x=380, y=215, at=4.4)]),
        PAUSE("6.2-k1", "Why does she stir the soup first? Pause the video and choose.", "Why does the cook stir the soup before tasting it?"),
    ]),
    dict(kind="hook", title="A spoonful like the whole pot", steps=[
        dict(say="She stirs so that the spoonful is like the whole pot. If she only tasted the top, the salt might all be at the bottom.", do=[T("stirred → the spoonful is **like the whole pot**", x=80, y=180, color=GREEN), T("not stirred → the spoonful could be **misleading**", x=80, y=280, color=RED, at=4)]),
        dict(say="The pot of soup is the population. The spoonful is the sample.", do=[E("🍲", 80, 380, 90), B("population", x=190, y=400, color=BLUE), E("🥄", 560, 380, 90, at=2), B("sample", x=670, y=400, color=RED, at=2)]),
    ]),
    dict(kind="recall", title="Fractions of an amount", steps=[
        dict(say="Remember how to find a fraction of an amount. One tenth of 300 is 300 divided by 10, which is 30.", do=[MATH("$$\\tfrac{1}{10}$$ of 300 = 300 ÷ 10 = 30", x=80, y=180)]),
        dict(say="So if a school has 840 students, and a survey asks 1 in every 10, it asks 84 students.", do=[MATH("840 ÷ 10 = 84 students", x=80, y=320, color=GREEN)]),
    ]),
    dict(kind="idea", title="Population and sample", steps=[
        dict(say="The population is everyone, or everything, that your question is about.", do=[T("**Population**: everyone the question is about", x=80, y=160, color=BLUE)]),
        dict(say="A sample is the smaller group that you actually collect data from.", do=[T("**Sample**: the smaller group you collect data from", x=80, y=240, color=RED)]),
        dict(say="For example: how do students at our school travel? The population is all the students. A sample could be 60 of them.",
             do=[TBL(["Question", "Population", "A possible sample"], [["How do our students travel?", "all students at the school", "60 students"], ["How long do the bulbs last?", "every bulb the factory makes", "100 bulbs"]], y=340), ROW(0, 3)]),
        dict(say="A factory wants to know how long its light bulbs last. The population is every bulb. A sample could be 100 bulbs.", do=[ROW(1, 0.3)]),
        PAUSE("6.2-k2", "Your turn. What if the factory tested every single bulb until it failed? Pause the video and choose.", "Testing every light bulb a factory makes until it fails would be …"),
    ]),
    dict(kind="idea", title="Check: test every bulb?", steps=[
        dict(say="That would be impossible. Every bulb would be used up, so there would be nothing left to sell. That is why we need samples.", do=[E("💡", 90, 170, 100), T("every bulb used up → **nothing left to sell**", x=230, y=200, color=RED), B("So we use a sample", x=80, y=340, color=GREEN, at=4.6)]),
    ]),
    dict(kind="idea", title="A good sample", steps=[
        dict(say="A sample is only useful if it represents the population. It should be like a mini version of the whole group.", do=[T("A good sample **represents** the population", x=80, y=160, color=GREEN)]),
        dict(say="A sample is biased if some members are more likely to be chosen than others.", do=[T("**Biased**: some members are more likely to be chosen", x=80, y=250, color=RED)]),
        dict(say="For example, if you ask only your friends, the sample is biased. Your friends may be similar to you.", do=[E("👫", 80, 330, 80), T("asking only your friends → biased", x=190, y=355)]),
        dict(say="The fairest way is a random sample. Everyone has an equal chance of being chosen, like pulling names out of a hat.", do=[E("🎩", 80, 440, 80), T("**Random**: everyone has an **equal chance**", x=190, y=465, color=BLUE)]),
    ]),
    dict(kind="method", title="How do I choose a good sample?", steps=[
        dict(say="Here is the method. Step 1: identify the population.", do=[T("1. Identify the **population**", x=80, y=170)]),
        dict(say="Step 2: choose a sample size that is big enough, but practical.", do=[T("2. A sample **big enough**, but practical", x=80, y=260)]),
        dict(say="Step 3: choose the members randomly, or make sure every group is included fairly.", do=[T("3. Choose **randomly**, or include every group fairly", x=80, y=350)]),
        dict(say="Step 4: check for bias. Ask: is anyone left out, or more likely to be picked?", do=[T("4. Check for **bias**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Spotting bias", steps=[
        dict(say="Amina wants to know how students travel to school. She asks the 30 students waiting at the bus stop. Is her sample biased?", do=[E("🚏", 90, 160, 90), T("asks **30 students at the bus stop**", x=210, y=190)]),
        dict(say="The population is all the students at the school. But everyone in her sample uses the bus.", do=[T("population: all students · sample: all bus users", x=80, y=310)]),
        dict(say="Walkers, cyclists and students who come by car had no chance of being chosen. So yes, the sample is biased.", do=[B("biased", x=80, y=410, color=RED), E("🚶", 300, 396, 60, at=0.4), E("🚲", 380, 396, 60, at=0.7), E("🚗", 460, 396, 60, at=1)]),
    ]),
    dict(kind="example", title="Choosing a sample size", steps=[
        dict(say="A school has 600 students. For a quick survey, which sample size is most sensible: 6, 60 or 600?", do=[B("6,  60  or  600 ?", x=80, y=160)]),
        dict(say="6 is too few. The results could be very different from the whole school.", do=[T("6 → too few", x=80, y=280, color=RED)]),
        dict(say="600 is the whole population. That is not a sample, and it would take too long.", do=[T("600 → that is everyone, not a sample", x=80, y=360, color=RED)]),
        dict(say="60 is big enough to be reliable, and small enough to manage.", do=[T("60 → big enough, and practical", x=80, y=440, color=GREEN), E("✅", 560, 426, 50, at=1.6)]),
        PAUSE("6.2-k3", "Your turn. Which sample is least biased for finding the favourite sport of Year 8? Pause and choose.", "Which sample is least biased for “favourite sport of Year 8”?"),
    ]),
    dict(kind="example", title="Check: the least biased sample", steps=[
        dict(say="The best choice is 20 Year 8 students picked randomly from the register. Everyone in Year 8 has an equal chance, and nobody outside Year 8 is included.",
             do=[E("📋", 90, 170, 100), T("**20 Year 8 students**, picked **randomly** from the register", x=230, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="A fair sample across groups", steps=[
        dict(say="A school has 300 students in Years 7, 8 and 9, with 100 in each year. You want a sample of 30. How many from each year?", do=[T("Years 7, 8, 9: **100** each.  Sample: **30**", x=80, y=170)]),
        dict(say="30 is one tenth of 300. So take one tenth of each year.", do=[MATH("30 is $$\\tfrac{1}{10}$$ of 300", x=80, y=270)]),
        dict(say="One tenth of 100 is 10. Choose 10 students from each year, at random.", do=[B("10 from each year", x=80, y=400, color=GREEN)]),
    ]),
    dict(kind="example", title="Small sample, large sample", steps=[
        dict(say="A coin is flipped 10 times, and lands on heads 7 times. That is 70 percent heads. Is the coin unfair?", do=[E("🪙", 90, 160, 90), T("10 flips: 7 heads = **70%**", x=210, y=190)]),
        dict(say="Then it is flipped 1000 times, and lands on heads 508 times. That is 50.8 percent.", do=[T("1000 flips: 508 heads = **50.8%**", x=210, y=300)]),
        dict(say="The large sample is very close to 50 percent, so the coin looks fair. A small sample can be misleading, just by chance.", do=[T("A **larger** sample is more **reliable**", x=80, y=430, color=BLUE)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Do people in our town want a new sports centre? Here is Jo's plan. Which line is wrong?",
             do=LINES("Jo", "Do people want a new sports centre?", ["Population: everyone in the town", "Sample: 50 people at the swimming pool on Saturday", "This is a good sample"])),
        dict(say="Line 3 is wrong. People at the swimming pool already like sport, so they are more likely to say yes. The sample is biased.", do=[dict(a="cross", id="l3")]),
        dict(say="A better sample would be 50 people chosen at random from across the whole town.", do=[T("Better: 50 people chosen **at random** from the whole town", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Opinion polls", steps=[
        dict(say="Before an election, opinion polls try to predict the result for a whole country, with millions of voters.", do=[E("🗳️", 90, 170, 100), T("millions of voters", x=230, y=200)]),
        dict(say="They do not ask everyone. A typical poll asks only about one or two thousand people.", do=[T("a poll asks about **1 000 to 2 000** people", x=230, y=300, color=BLUE)]),
        dict(say="That works only if the sample is chosen carefully, so that it represents the whole country: young and old, city and countryside.", do=[T("…if the sample **represents** everyone", x=230, y=400), E("👵", 230, 470, 70, at=3), E("🧑", 320, 470, 70, at=3.3), E("🏙️", 410, 470, 70, at=3.8), E("🌾", 500, 470, 70, at=4.2)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("6.2-k4", "One last question. A school has 250 boys and 250 girls. A sample of 50 should keep the same mix. How many girls should be in it? Pause the video and answer.",
              "250 boys and 250 girls; a sample of 50 with the same mix. How many girls?"),
        dict(say="Half of the students are girls, so half of the sample should be girls. Half of 50 is 25.", do=[MATH("half of 50 = 25", x=80, y=190), B("25 girls", x=80, y=300, color=GREEN, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: the population is everyone the question is about. The sample is the group you collect data from.", do=[T("• Population = everyone; sample = those you ask", x=80, y=170)]),
        dict(say="A good sample represents the population. A biased sample favours some members.", do=[T("• Good sample **represents**; biased sample **favours**", x=80, y=250)]),
        dict(say="Random sampling gives everyone an equal chance.", do=[T("• Random = equal chance for everyone", x=80, y=330)]),
        dict(say="Larger samples are more reliable, but they take more time.", do=[T("• Larger samples are more reliable", x=80, y=410)]),
    ]),
]
