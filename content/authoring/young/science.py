# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stages 1 and 2 (ages 5-7) – Camday picture lessons and tap-only practice.
Topics follow the Cambridge Primary Science curriculum framework (0097) for Stages 1 and 2; every lesson, picture,
question and explanation is an Camday original. Written by the Camday teaching team."""
from qbank import *

EM = lambda *g: {"kind": "emojis", "groups": [list(x) for x in g]}


def build_sec(U, sid, title, obj, lesson, words, T, deep, ex):
    s = U.section(sid, title, [obj])
    for b in lesson:
        k = b[0]
        if k == "idea": s.idea(b[1], b[2], fig=b[3] if len(b) > 3 else None)
        elif k == "tip": s.tip(b[1], b[2])
        elif k == "mistake": s.mistake(b[1], b[2])
        elif k == "example": s.example(b[1], b[2], b[3], b[4], fig=b[5] if len(b) > 5 else None)
        elif k == "check": s.check(b[1])
    s.words(*words)
    s.young(T, ex, deep)
    return s


def objs(*ts, stage, strand):
    return {f"O{i + 1}": {"code": f"Stage {stage} {strand}", "sec": f"{{n}}.{i + 1}", "codeNote": "", "t": t} for i, t in enumerate(ts)}


def unit(n, title, strand, blurb, o1, o2, stage):
    O = {"O1": {"code": f"Stage {stage} · {strand}", "sec": f"{n}.1", "codeNote": "", "t": o1}, "O2": {"code": f"Stage {stage} · {strand}", "sec": f"{n}.2", "codeNote": "", "t": o2}}
    return YUnit(n, title, strand, blurb, O, stage, "science")


# ============================================================== STAGE 1
def stage1():
    U = []
    # ---------------------------------------------------------- 1 Living things
    u = unit(1, "Living Things", "Biology", "What is alive? Plants and animals grow, need food and water, and make new living things. The parts of a plant.",
             "Tell the difference between things that are alive and things that are not.", "Name the parts of a plant: root, stem, leaf and flower.", 1)
    LIV = [("dog", "🐶", "Alive"), ("tree", "🌳", "Alive"), ("bird", "🐦", "Alive"), ("fish", "🐟", "Alive"), ("flower", "🌸", "Alive"), ("cat", "🐱", "Alive"), ("frog", "🐸", "Alive"), ("baby", "👶", "Alive"),
           ("rock", "🪨", "Not alive"), ("car", "🚗", "Not alive"), ("ball", "⚽", "Not alive"), ("chair", "🪑", "Not alive"), ("cup", "🥤", "Not alive"), ("teddy", "🧸", "Not alive"), ("robot", "🤖", "Not alive"), ("phone", "📱", "Not alive")]
    W1 = [("alive", "living – it grows, eats and drinks", "🐶"), ("plant", "a living thing that grows in soil", "🌱"), ("animal", "a living thing that can move about", "🐕"), ("grow", "to get bigger", "📏")]
    build_sec(u, "1.1", "Alive or not alive?", "O1", [
        ("idea", "Living things", ["A dog is **alive**. It eats, drinks, breathes, moves and grows bigger. One day it can have puppies.", "A rock is **not alive**. It does not eat, it does not grow and it cannot make baby rocks."], EM(("🐶", 1), ("🪨", 1))),
        ("check", PIC("Look at the picture. Is a tree alive?", "Yes, it is alive", [("No, it is not alive", "A tree grows and needs water, so it is alive.")], pics={"Yes, it is alive": "👍", "No, it is not alive": "👎"}, pic="🌳", o="O1", hint="Does a tree grow?")),
        ("idea", "Plants are alive too", ["A plant cannot walk, but it is still **alive**. It grows, it needs water and light, and it makes seeds that grow into new plants."], EM(("🌱", 1), ("🌿", 1), ("🌳", 1))),
        ("tip", "Ask three questions", ["Does it grow? Does it need food or water? Can it make new living things? If the answer is yes, it is alive."]),
        ("mistake", "Moving is not enough", ["A car moves, but it is not alive: it does not grow or eat. A tree does not walk, but it is alive."]),
        ("check", PIC("Which one is NOT alive?", "car", [("cat", "A cat eats and grows."), ("flower", "A flower grows and needs water.")], pics={"car": "🚗", "cat": "🐱", "flower": "🌸"}, o="O1"))],
        W1,
        T=[k_sort(LIV, ["Alive", "Not alive"], "O1", "Is each one alive or not alive?"), k_count([("cat", "🐱", ""), ("fish", "🐟", ""), ("flower", "🌸", "")], "O1", "How many {name}s can you count?"),
           k_pick(LIV, "Alive", "O1", "Tap the one that is ALIVE."), k_pick(LIV, "Not alive", "O1", "Tap the one that is NOT alive."), k_word(W1, "O1")],
        deep=[k_all(LIV, "Alive", "O1", "Tap ALL the living things."), k_odd(LIV, "O1"),
              k_claim([("A car is alive because it moves.", False, "A car moves but it does not grow, eat or make baby cars, so it is not alive."), ("A tree is alive even though it cannot walk.", True, "A tree grows, needs water and makes seeds, so it is alive."),
                       ("A teddy bear is alive because it has eyes.", False, "A teddy does not grow or eat. Having eyes does not make it alive."), ("A baby grows, so it is alive.", True, "Growing is one sign of being alive.")], "O1")],
        ex=EXQ(k_pick(LIV, "Alive", "O1", "Which of these can grow?")))
    PL = [("root", "under the soil – drinks water", "🪴"), ("stem", "holds the plant up", "🌿"), ("leaf", "flat and green – makes food from light", "🍃"), ("flower", "colourful – makes seeds", "🌸")]
    PARTS = [("root", "🟫", "Under the ground"), ("stem", "🌿", "Above the ground"), ("leaf", "🍃", "Above the ground"), ("flower", "🌸", "Above the ground"), ("seed", "🌰", "Above the ground")]
    build_sec(u, "1.2", "Parts of a plant", "O2", [
        ("idea", "A plant has parts", ["The **roots** grow under the soil and take in water. The **stem** holds the plant up. The **leaves** use sunlight to make food. The **flower** makes seeds."], EM(("🌸", 1), ("🍃", 2), ("🌿", 1))),
        ("check", PIC("Which part of a plant is under the soil?", "root", [("flower", "The flower is at the top."), ("leaf", "Leaves grow in the light.")], pics={"root": "🟫", "flower": "🌸", "leaf": "🍃"}, o="O2")),
        ("example", "Why does a plant need roots?", "If you pull up a plant, what do you see at the bottom?", [("long thin roots", "they spread out in the soil"), ("roots take in water", "and hold the plant in the ground")], "Roots drink water and hold the plant still."),
        ("mistake", "Not every plant has big flowers", ["Grass is a plant too, with tiny flowers. Look for roots, a stem and leaves."]),
        ("check", PIC("Which part makes seeds?", "flower", [("root", "Roots take in water."), ("stem", "The stem holds the plant up.")], pics={"flower": "🌸", "root": "🟫", "stem": "🌿"}, o="O2"))],
        PL,
        T=[k_match([(p[0], p[1]) for p in PL], "O2", "Match each part to its job."), k_sort(PARTS, ["Under the ground", "Above the ground"], "O2", "Where is each part of the plant?"),
           k_word(PL, "O2"), k_order([(["seed", "seedling", "plant with leaves", "plant with a flower"], "A seed grows into a small seedling, then a bigger plant, then it flowers.")], "O2", "Put the pictures of a growing plant in order.")],
        deep=[k_claim([("Roots grow in the air.", False, "Roots grow down into the soil to find water."), ("Leaves need sunlight.", True, "Leaves use sunlight to make food for the plant."), ("A plant does not need water.", False, "Every plant needs water; the roots take it in.")], "O2"),
              lambda r: PIC("A plant is put in a dark cupboard for two weeks. What will happen to its leaves?", "They turn pale and weak", [("They grow bigger and greener", "Leaves need light to make food."), ("Nothing changes", "Without light the plant cannot make its food.")], o="O2", d="H", pic="🌑🪴", reason="Leaves need light to make food, so in the dark the plant becomes pale and weak."),
              lambda r: PIC("Which plant has a stem that is easy to see?", pick(r, ["sunflower", "tree"]), [("grass", "Grass has very short, thin stems."), ("moss", "Moss is tiny and flat.")], pics={"sunflower": "🌻", "tree": "🌳", "grass": "🌾", "moss": "🟩"}, o="O2", d="H")],
        ex=EXQ(k_match([(p[0], p[1]) for p in PL], "O2", "Match each part to its job.")))
    U.append(u)
    # ---------------------------------------------------------- 2 Ourselves
    u = unit(2, "Ourselves", "Biology", "The parts of the human body and our five senses: seeing, hearing, smelling, tasting and touching.",
             "Name the main parts of the human body.", "Know the five senses and the body part used for each.", 1)
    BODY = [("head", "on top of your body", "🙂"), ("arm", "you wave with it", "💪"), ("leg", "you walk with it", "🦵"), ("hand", "you hold things with it", "✋"), ("foot", "you stand on it", "🦶"), ("knee", "your leg bends here", "🦵")]
    build_sec(u, "2.1", "My body", "O1", [
        ("idea", "Parts of the body", ["We all have a **head**, two **arms**, two **hands**, two **legs** and two **feet**. Our arms bend at the **elbows** and our legs bend at the **knees**."], EM(("🙂", 1), ("💪", 2), ("🦵", 2))),
        ("check", PIC("Which part do you stand on?", "foot", [("hand", "You hold things with your hands."), ("head", "Your head is at the top.")], pics={"foot": "🦶", "hand": "✋", "head": "🙂"}, o="O1")),
        ("tip", "Count in pairs", ["Many body parts come in twos: two eyes, two ears, two arms, two legs."]),
        ("check", NUMS("How many legs do you have?", 2, [1, 4], o="O1", pic="🦵🦵"))],
        BODY,
        T=[k_word(BODY, "O1"), k_match([(b[0], b[1]) for b in BODY], "O1", "Match each body part to what it does."),
           k_sort([("eyes", "👀", "Two"), ("nose", "👃", "One"), ("legs", "🦵", "Two"), ("mouth", "👄", "One"), ("ears", "👂", "Two"), ("head", "🙂", "One")], ["One", "Two"], "O1", "Do we have one or two of each?"),
           k_count([("hand", "✋", "")], "O1", "How many {name}s are there?")],
        deep=[k_claim([("We have three arms.", False, "We have two arms."), ("Your leg bends at the knee.", True, "The knee is where the leg bends."), ("Your nose is on your foot.", False, "Your nose is on your face.")], "O1"),
              lambda r: PIC("Which part helps you kick a ball?", "leg", [("arm", "Arms throw, legs kick."), ("ear", "Ears hear.")], pics={"leg": "🦵", "arm": "💪", "ear": "👂"}, o="O1", d="H"),
              lambda r: MS("Tap ALL the parts you have two of.", ["eyes", "hands"], ["nose", "mouth"], o="O1", d="H", reason="Eyes and hands come in pairs; we have one nose and one mouth.")],
        ex=EXQ(k_word(BODY, "O1")))
    SEN = [("see", "eyes", "👀"), ("hear", "ears", "👂"), ("smell", "nose", "👃"), ("taste", "tongue", "👅"), ("touch", "skin", "✋")]
    SENI = [("rainbow", "🌈", "See"), ("drum", "🥁", "Hear"), ("flower smell", "🌸", "Smell"), ("lemon taste", "🍋", "Taste"), ("soft fur", "🐰", "Touch"), ("bell", "🔔", "Hear"), ("stars", "⭐", "See"), ("cake smell", "🎂", "Smell")]
    build_sec(u, "2.2", "My five senses", "O2", [
        ("idea", "Five senses", ["We find out about the world with our **senses**. We **see** with our eyes, **hear** with our ears, **smell** with our nose, **taste** with our tongue and **touch** with our skin."], EM(("👀", 1), ("👂", 1), ("👃", 1), ("👅", 1), ("✋", 1))),
        ("check", PIC("Which body part do you use to hear?", "ears", [("eyes", "Eyes are for seeing."), ("tongue", "The tongue is for tasting.")], pics={"ears": "👂", "eyes": "👀", "tongue": "👅"}, o="O2")),
        ("example", "Using more than one sense", "How can you tell an orange is an orange, with your eyes closed?", [("smell it", "it smells of orange"), ("touch it", "bumpy skin, round"), ("taste a piece", "sweet and juicy")], "You can use smell, touch and taste."),
        ("check", PIC("You eat a lemon. Which sense tells you it is sour?", "taste", [("see", "You cannot see sourness."), ("hear", "Lemons make no sound.")], pics={"taste": "👅", "see": "👀", "hear": "👂"}, o="O2"))],
        [("sense", "a way of finding out about the world", "🖐️"), ("see", "use your eyes", "👀"), ("hear", "use your ears", "👂"), ("smell", "use your nose", "👃"), ("taste", "use your tongue", "👅"), ("touch", "use your skin", "✋")],
        T=[k_match([(a, b) for a, b, _ in SEN], "O2", "Match each sense to the body part."), k_sort(SENI, ["See", "Hear", "Smell"], "O2", "Which sense do you use most for each one?"),
           k_pick(SENI, "Hear", "O2", "Which one do you find out about by HEARING?"), k_pick(SENI, "Touch", "O2", "Which one do you find out about by TOUCHING?")],
        deep=[k_claim([("You smell with your ears.", False, "You smell with your nose."), ("You can use two senses at once.", True, "You can see and hear a drum at the same time."), ("A blindfold stops you hearing.", False, "A blindfold covers your eyes; you can still hear.")], "O2"),
              lambda r: MS("A cake is in the oven. Tap ALL the senses that can tell you it is there.", ["smell", "see"], ["taste", "touch"], o="O2", d="H", reason="You can smell it and see it through the glass. You cannot taste or touch it while it is in the hot oven."),
              k_odd([("rainbow", "🌈", "See"), ("stars", "⭐", "See"), ("TV", "📺", "See"), ("drum", "🥁", "Hear"), ("bell", "🔔", "Hear"), ("whistle", "🎵", "Hear"), ("music", "🎶", "Hear")], "O2")],
        ex=EXQ(k_match([(a, b) for a, b, _ in SEN], "O2", "Match each sense to the body part.")))
    U.append(u)
    # ---------------------------------------------------------- 3 Materials
    u = unit(3, "Materials", "Chemistry", "Objects are made of materials such as wood, metal, plastic, glass and fabric. Sorting materials by how they feel and look.",
             "Name the material an object is made from.", "Describe and sort materials: hard or soft, rough or smooth, shiny or dull.", 1)
    MAT = [("spoon", "🥄", "Metal"), ("key", "🔑", "Metal"), ("coin", "🪙", "Metal"), ("table", "🪵", "Wood"), ("pencil", "✏️", "Wood"), ("chair", "🪑", "Wood"), ("bottle", "🧴", "Plastic"), ("toy brick", "🧱", "Plastic"),
           ("window", "🪟", "Glass"), ("glass jar", "🫙", "Glass"), ("T-shirt", "👕", "Fabric"), ("sock", "🧦", "Fabric")]
    build_sec(u, "3.1", "What is it made of?", "O1", [
        ("idea", "Objects and materials", ["An **object** is a thing, like a spoon. The **material** is what it is made of. A spoon can be made of **metal**, **wood** or **plastic**."], EM(("🥄", 1), ("🪵", 1), ("🧴", 1))),
        ("check", PIC("What is a window made of?", "glass", [("wood", "Wood is not see-through."), ("fabric", "Fabric is soft cloth.")], pics={"glass": "🪟", "wood": "🪵", "fabric": "👕"}, o="O1")),
        ("tip", "One object, different materials", ["A chair can be wood, metal or plastic. Look closely, and feel it if you can."]),
        ("check", PIC("Which object is made of fabric?", "sock", [("key", "A key is metal."), ("pencil", "A pencil is mostly wood.")], pics={"sock": "🧦", "key": "🔑", "pencil": "✏️"}, o="O1"))],
        [("material", "what an object is made of", "🧱"), ("metal", "hard and shiny, like a key", "🔑"), ("wood", "comes from trees", "🪵"), ("plastic", "light, used for bottles and toys", "🧴"), ("glass", "you can see through it", "🪟"), ("fabric", "soft cloth for clothes", "👕")],
        T=[k_sort(MAT, ["Metal", "Wood", "Plastic"], "O1", "What is each object made of?"), k_pick(MAT, "Metal", "O1", "Which object is made of metal?"), k_pick(MAT, "Wood", "O1", "Which object is made of wood?"),
           k_pick(MAT, "Glass", "O1", "Which object is made of glass?")],
        deep=[k_odd(MAT, "O1"), k_all(MAT, "Metal", "O1", "Tap ALL the objects made of metal."),
              k_claim([("All spoons are made of metal.", False, "Spoons can be metal, wood or plastic."), ("A window is made of glass so we can see through it.", True, "Glass is see-through."), ("Socks are made of wood.", False, "Socks are made of fabric.")], "O1")],
        ex=EXQ(k_pick(MAT, "Fabric", "O1", "Which object is made of fabric?")))
    PROP = [("pillow", "🛏️", "Soft"), ("teddy", "🧸", "Soft"), ("sock", "🧦", "Soft"), ("rock", "🪨", "Hard"), ("brick", "🧱", "Hard"), ("spoon", "🥄", "Hard"), ("key", "🔑", "Hard"), ("cotton wool", "☁️", "Soft")]
    build_sec(u, "3.2", "Sorting materials", "O2", [
        ("idea", "How does it feel? How does it look?", ["We describe materials with words like **hard** or **soft**, **rough** or **smooth**, **shiny** or **dull**. A rock is hard and rough. A pillow is soft. A new coin is shiny."], EM(("🪨", 1), ("🛏️", 1), ("🪙", 1))),
        ("check", PIC("Which one is soft?", "pillow", [("rock", "A rock is hard."), ("key", "A key is hard metal.")], pics={"pillow": "🛏️", "rock": "🪨", "key": "🔑"}, o="O2")),
        ("example", "Testing hard or soft", "How can you test if a material is soft?", [("press it gently", "with your finger"), ("does it squash?", "soft materials squash; hard ones do not")], "If it squashes when you press it, it is soft."),
        ("check", PIC("You press a brick and it does not squash. The brick is…", "hard", [("soft", "Soft things squash when you press them.")], pics={"hard": "🧱", "soft": "☁️"}, o="O2"))],
        [("hard", "does not squash when you press it", "🪨"), ("soft", "squashes when you press it", "🛏️"), ("rough", "bumpy to touch", "🌵"), ("smooth", "not bumpy, like glass", "🪟"), ("shiny", "it reflects light", "✨")],
        T=[k_sort(PROP, ["Hard", "Soft"], "O2", "Is each one hard or soft?"), k_pick(PROP, "Soft", "O2", "Which one would be nicest to sleep on?"), k_pick(PROP, "Hard", "O2", "Which one is HARD?"),
           k_word([("rough", "bumpy to touch", "🌵"), ("smooth", "not bumpy", "🪟"), ("shiny", "reflects light", "✨"), ("soft", "squashes easily", "☁️")], "O2")],
        deep=[k_all(PROP, "Soft", "O2", "Tap ALL the soft things."),
              lambda r: PIC("Which material would make the best pillow?", "cotton wool", [("rock", "A rock is too hard to rest on."), ("metal", "Metal is hard and cold.")], pics={"cotton wool": "☁️", "rock": "🪨", "metal": "🔩"}, o="O2", d="H", reason="A pillow should be soft, so cotton wool is the best choice."),
              k_claim([("A rock is soft.", False, "A rock does not squash, so it is hard."), ("Wet things can be slippery and smooth.", True, "Water makes a surface smooth and slippery."), ("A sponge squashes, so it is soft.", True, "Squashing when pressed means soft.")], "O2")],
        ex=EXQ(k_sort(PROP, ["Hard", "Soft"], "O2", "Is each one hard or soft?")))
    U.append(u)
    # ---------------------------------------------------------- 4 Pushes and pulls
    u = unit(4, "Pushes and Pulls", "Physics", "Pushing and pulling make things move, speed up, slow down, stop or change direction.",
             "Know that pushes and pulls make things move.", "Know that a push or pull can make something go faster, slower or change direction.", 1)
    PP = [("open a drawer", "🗄️", "Pull"), ("kick a ball", "⚽", "Push"), ("ring a doorbell", "🔔", "Push"), ("pull a wagon", "🛒", "Pull"), ("push a swing", "🎢", "Push"), ("tug of war", "🪢", "Pull"), ("close a door", "🚪", "Push"), ("pick an apple", "🍎", "Pull")]
    build_sec(u, "4.1", "Push or pull?", "O1", [
        ("idea", "Pushes and pulls", ["A **push** moves something away from you. A **pull** moves something towards you. You push a door to close it and pull a drawer to open it."], EM(("🫸", 1), ("🫷", 1))),
        ("check", PIC("You kick a ball. Is that a push or a pull?", "push", [("pull", "Kicking moves the ball away from you.")], pics={"push": "🫸", "pull": "🫷"}, o="O1", pic="⚽")),
        ("tip", "Away or towards?", ["Ask: is it moving away from me (push) or towards me (pull)?"]),
        ("check", PIC("You open a drawer. Is that a push or a pull?", "pull", [("push", "The drawer comes towards you.")], pics={"push": "🫸", "pull": "🫷"}, o="O1", pic="🗄️"))],
        [("push", "move something away from you", "🫸"), ("pull", "move something towards you", "🫷"), ("move", "go from one place to another", "🏃")],
        T=[k_sort(PP, ["Push", "Pull"], "O1", "Is each one a push or a pull?"), k_pick(PP, "Pull", "O1", "Which one is a PULL?"), k_pick(PP, "Push", "O1", "Which one is a PUSH?"),
           k_word([("push", "move something away from you", "🫸"), ("pull", "move something towards you", "🫷"), ("move", "go from one place to another", "🏃"), ("force", "a push or a pull", "💪")], "O1")],
        deep=[k_all(PP, "Push", "O1", "Tap ALL the pushes."), k_odd(PP, "O1"),
              k_claim([("Opening a drawer is a pull.", True, "The drawer moves towards you."), ("Kicking a ball is a pull.", False, "The ball moves away from you: a push."), ("Some things need a push AND a pull, like a door.", True, "You can push a door shut and pull it open.")], "O1")],
        ex=EXQ(k_sort(PP, ["Push", "Pull"], "O1", "Is each one a push or a pull?")))
    FST = [("kick a rolling ball forwards", "⚽", "Faster"), ("push a swing from behind", "🎢", "Faster"), ("pedal harder on a bike", "🚲", "Faster"), ("catch a ball", "🧤", "Slower"), ("put the brakes on a bike", "🛑", "Slower"),
           ("roll a ball up a hill", "⛰️", "Slower"), ("hit a ball to the side with a bat", "🏏", "Turns"), ("steer a go-kart", "🏎️", "Turns"), ("head a ball to a friend", "🤾", "Turns")]
    build_sec(u, "4.2", "Faster, slower, turn", "O2", [
        ("idea", "Changing how things move", ["A bigger push makes a ball go **faster** and further. A push against a moving ball can make it **slow down** or **stop**. A push from the side makes it **change direction**."], EM(("⚽", 1), ("💨", 2))),
        ("check", PIC("Which push makes a toy car go further: a gentle push or a big push?", "a big push", [("a gentle push", "A gentle push only moves it a little."), ("they are the same", "A bigger push makes it go further.")], o="O2")),
        ("example", "Testing pushes", "Push a toy car three times: gently, a bit harder, very hard. What happens?", [("gentle push", "it moves a little"), ("harder push", "it goes further"), ("very hard push", "it goes furthest")], "Bigger push → further."),
        ("check", PIC("A goalkeeper stops a ball. What did the push do?", "stopped it", [("made it faster", "The goalkeeper pushed against it."), ("made it bigger", "A push cannot change the size of a ball.")], o="O2", pic="🧤⚽"))],
        [("faster", "quicker", "⚡"), ("slower", "less quick", "🐢"), ("stop", "not move any more", "🛑"), ("direction", "the way something goes", "➡️")],
        T=[lambda r: PIC("Which push makes a swing go highest?", "a big push", [("a tiny push", "A tiny push moves it only a little."), ("no push", "Without a push it stays still.")], o="O2"),
           k_word([("faster", "quicker", "⚡"), ("slower", "less quick", "🐢"), ("stop", "not moving any more", "🛑"), ("turn", "change direction", "↩️")], "O2"),
           k_order([(["no push", "gentle push", "hard push"], "No push: the car stays still. A gentle push: it moves a little. A hard push: it goes furthest.")], "O2", "Put the pushes in order: the car goes least far first."),
           k_sort(FST, ["Faster", "Slower", "Turns"], "O2", "Does each push make it go faster, slower or turn?"), k_pick(FST, "Slower", "O2", "Which push makes something SLOW DOWN?"), k_pick(FST, "Turns", "O2", "Which push makes something CHANGE DIRECTION?")],
        deep=[k_claim([("A bigger push makes a ball go further.", True, "More push means it goes faster and further."), ("You cannot stop a rolling ball with a push.", False, "A push against it slows it down and stops it."), ("A push can make a ball change direction.", True, "A push from the side makes it turn.")], "O2"),
              k_all(FST, "Faster", "O2", "Tap ALL the pushes that make something go FASTER."), lambda r: PIC("Mia wants her toy car to go further. What should she change?", "push it harder", [("use a red car", "The colour does not change how far it goes."), ("push it more gently", "That makes it go less far.")], o="O2", d="H", reason="A bigger push makes the car go faster and further."),
              lambda r: PIC("Two children push a box from opposite sides with the same push. What happens?", "it does not move", [("it moves left", "The pushes are the same size."), ("it flies up", "Pushes from the sides do not lift it.")], o="O2", d="VH", reason="The two equal pushes cancel each other out, so the box stays still.")],
        ex=EXQ(lambda r: PIC("Which push makes a swing go highest?", "a big push", [("a tiny push", "A tiny push moves it only a little.")], o="O2")))
    U.append(u)
    # ---------------------------------------------------------- 5 Sound
    u = unit(5, "Sound", "Physics", "Sounds around us, which sense we use to hear them, loud and quiet sounds, and how sounds get quieter further away.",
             "Know that we hear sounds with our ears and name sounds around us.", "Compare loud and quiet sounds and know that sounds are quieter further away.", 1)
    LQ = [("drum", "🥁", "Loud"), ("thunder", "⛈️", "Loud"), ("fire engine", "🚒", "Loud"), ("whisper", "🤫", "Quiet"), ("cat purring", "🐱", "Quiet"), ("clock ticking", "⏰", "Quiet"), ("trumpet", "🎺", "Loud"), ("leaves rustling", "🍃", "Quiet")]
    build_sec(u, "5.1", "Sounds around us", "O1", [
        ("idea", "Listen!", ["We hear **sounds** with our **ears**. Sounds come from things around us: a bird singing, a car, a door closing, people talking."], EM(("👂", 1), ("🐦", 1), ("🚗", 1))),
        ("check", PIC("Which body part do we use to hear sounds?", "ears", [("eyes", "Eyes see."), ("nose", "Noses smell.")], pics={"ears": "👂", "eyes": "👀", "nose": "👃"}, o="O1")),
        ("tip", "Sound walk", ["Close your eyes for one minute and count how many different sounds you hear."]),
        ("check", PIC("Which one makes a sound you can hear?", "bell", [("rainbow", "A rainbow is silent."), ("picture", "A picture does not make sound.")], pics={"bell": "🔔", "rainbow": "🌈", "picture": "🖼️"}, o="O1"))],
        [("sound", "something you hear", "🔊"), ("hear", "use your ears", "👂"), ("listen", "try to hear", "🎧")],
        T=[k_pick([("bell", "🔔", "Sound"), ("drum", "🥁", "Sound"), ("rainbow", "🌈", "Silent"), ("picture", "🖼️", "Silent"), ("cloud", "☁️", "Silent"), ("dog barking", "🐶", "Sound")], "Sound", "O1", "Which one makes a sound?"),
           k_sort([("bell", "🔔", "Makes a sound"), ("drum", "🥁", "Makes a sound"), ("rainbow", "🌈", "Silent"), ("picture", "🖼️", "Silent"), ("dog barking", "🐶", "Makes a sound"), ("pencil on a table", "✏️", "Silent")], ["Makes a sound", "Silent"], "O1", "Does each one make a sound?"),
           k_count([("bell", "🔔", ""), ("drum", "🥁", "")], "O1", "How many {name}s can you see?"),
           k_word([("sound", "something you hear", "🔊"), ("hear", "use your ears", "👂"), ("listen", "try hard to hear", "🎧"), ("silent", "making no sound at all", "🤐")], "O1")],
        deep=[k_claim([("We hear with our eyes.", False, "We hear with our ears."), ("A drum makes a sound when you hit it.", True, "Hitting the drum makes it shake and make sound.")], "O1"),
              lambda r: MS("You are in a park. Tap ALL the things you might HEAR.", ["birds singing", "children playing"], ["a rainbow", "the sun shining"], o="O1", d="H", reason="Birds and children make sounds. Rainbows and sunshine are silent."),
              k_odd([("bell", "🔔", "Makes a sound"), ("drum", "🥁", "Makes a sound"), ("trumpet", "🎺", "Makes a sound"), ("dog barking", "🐶", "Makes a sound"), ("rainbow", "🌈", "Silent"), ("picture", "🖼️", "Silent"), ("cloud", "☁️", "Silent")], "O1")],
        ex=EXQ(k_sort(LQ, ["Loud", "Quiet"], "O1", "Is each sound loud or quiet?")))
    build_sec(u, "5.2", "Loud and quiet", "O2", [
        ("idea", "Loud and quiet sounds", ["Some sounds are **loud**, like a drum or thunder. Some are **quiet**, like a whisper. The same sound is **quieter** when you are **further away** from it."], EM(("🥁", 1), ("🤫", 1))),
        ("check", PIC("Which sound is LOUD?", "thunder", [("whisper", "A whisper is quiet."), ("cat purring", "Purring is quiet.")], pics={"thunder": "⛈️", "whisper": "🤫", "cat purring": "🐱"}, o="O2")),
        ("example", "Walking away", "A friend rings a bell and you walk away. What happens to the sound?", [("near the bell", "the sound is loud"), ("further away", "the sound is quieter"), ("very far", "you can hardly hear it")], "The further away, the quieter."),
        ("check", PIC("You walk away from a radio. The sound gets…", "quieter", [("louder", "Sounds get quieter further away."), ("the same", "Distance changes how loud it is.")], o="O2"))],
        [("loud", "a big sound", "📢"), ("quiet", "a small sound", "🤫"), ("near", "close to you", "👣"), ("far", "a long way away", "🏔️")],
        T=[k_sort(LQ, ["Loud", "Quiet"], "O2", "Is each sound loud or quiet?"), k_pick(LQ, "Quiet", "O2", "Which one makes a QUIET sound?"), k_pick(LQ, "Loud", "O2", "Which one makes a LOUD sound?"),
           k_order([(["whisper", "talking", "shouting"], "A whisper is quietest, then talking, then shouting.")], "O2", "Put the sounds in order from quietest to loudest.")],
        deep=[k_claim([("A sound is louder when you are further away.", False, "Sounds get quieter further away."), ("You can hear a drum better when you stand close to it.", True, "Closer means louder.")], "O2"),
              lambda r: PIC("Three children stand near, middle and far from a drum. Who hears it most quietly?", "the child who is far away", [("the child who is near", "Closest hears it loudest."), ("they all hear the same", "Distance changes loudness.")], o="O2", d="H"),
              k_odd(LQ, "O2")],
        ex=EXQ(k_pick(LQ, "Quiet", "O2", "Which one makes a QUIET sound?")))
    U.append(u)
    # ---------------------------------------------------------- 6 Earth and sky
    u = unit(6, "Earth and Sky", "Earth and Space", "Weather changes from day to day. The Sun gives us light, and it is day when our side of the Earth faces the Sun.",
             "Describe different kinds of weather.", "Know that the Sun gives light and that we have day and night.", 1)
    WX = [("sunny", "☀️", "Sunny"), ("rainy", "🌧️", "Rainy"), ("snowy", "❄️", "Snowy"), ("windy", "🌬️", "Windy"), ("cloudy", "☁️", "Cloudy")]
    WEAR = [("sun hat", "👒", "Sunny"), ("umbrella", "☂️", "Rainy"), ("wellies", "🥾", "Rainy"), ("scarf and gloves", "🧣", "Snowy"), ("sunglasses", "🕶️", "Sunny"), ("raincoat", "🧥", "Rainy"), ("snowman", "⛄", "Snowy")]
    build_sec(u, "6.1", "Weather", "O1", [
        ("idea", "What is the weather like?", ["The **weather** can be **sunny**, **rainy**, **cloudy**, **windy** or **snowy**. It changes from day to day, so we choose clothes to match."], EM(("☀️", 1), ("🌧️", 1), ("❄️", 1), ("🌬️", 1))),
        ("check", PIC("It is raining. What should you take outside?", "umbrella", [("sunglasses", "Sunglasses are for sunny days."), ("sun hat", "A sun hat is for sunny weather.")], pics={"umbrella": "☂️", "sunglasses": "🕶️", "sun hat": "👒"}, o="O1")),
        ("tip", "Weather chart", ["Draw the weather every day for a week. Which weather did you see most?"]),
        ("check", PIC("Which picture shows WINDY weather?", "windy", [("sunny", "That is the sun."), ("snowy", "That is snow.")], pics={"windy": "🌬️", "sunny": "☀️", "snowy": "❄️"}, o="O1"))],
        [("weather", "what it is like outside", "🌦️"), ("sunny", "the sun is shining", "☀️"), ("rainy", "rain is falling", "🌧️"), ("windy", "the air is moving", "🌬️"), ("snowy", "snow is falling", "❄️")],
        T=[k_sort(WEAR, ["Sunny", "Rainy", "Snowy"], "O1", "Which weather is each one for?"), k_pick(WEAR, "Snowy", "O1", "Which one is for SNOWY weather?"), k_word([(w[0], f"{w[0]} weather", w[1]) for w in WX], "O1"),
           lambda r: (lambda d: NUMS("The chart shows the weather for one week. How many days were sunny?", d.count("☀️"), [x for x in {d.count("☀️") + 1, max(1, d.count("☀️") - 1), 7} if x != d.count("☀️")][:2], o="O1", fig={"kind": "emojis", "groups": [[e, 1] for e in d], "per": 7}))([pick(r, ["☀️", "🌧️", "☁️"]) for _ in range(7)])],
        deep=[k_claim([("You need an umbrella on a sunny day.", False, "An umbrella keeps rain off you."), ("The weather can change in one day.", True, "A sunny morning can become a rainy afternoon.")], "O1"), k_odd(WEAR, "O1"),
              lambda r: MS("It is cold and snowy. Tap ALL the things you should wear.", ["scarf", "gloves"], ["sandals", "sun hat"], o="O1", d="H", reason="Scarf and gloves keep you warm. Sandals and a sun hat are for hot weather.")],
        ex=EXQ(k_sort(WEAR, ["Sunny", "Rainy", "Snowy"], "O1", "Which weather is each one for?")))
    DN = [("Sun in the sky", "☀️", "Day"), ("Moon and stars", "🌙", "Night"), ("having breakfast", "🥣", "Day"), ("going to bed", "🛏️", "Night"), ("playing in the park", "🛝", "Day"), ("owl hunting", "🦉", "Night")]
    build_sec(u, "6.2", "Day and night", "O2", [
        ("idea", "The Sun gives us light", ["The **Sun** is a star. It gives us **light** and warmth. In the **day** our part of the Earth faces the Sun, so it is light. At **night** our part faces away, so it is dark."], EM(("☀️", 1), ("🌍", 1), ("🌙", 1))),
        ("check", PIC("What gives us light in the daytime?", "the Sun", [("the Moon", "The Moon shines at night but is much dimmer."), ("a torch", "A torch is small; the Sun lights up the whole sky.")], pics={"the Sun": "☀️", "the Moon": "🌙", "a torch": "🔦"}, o="O2")),
        ("mistake", "Never look at the Sun", ["The Sun is so bright it can hurt your eyes. Never look straight at it."]),
        ("check", PIC("When can you usually see the stars?", "at night", [("in the day", "The Sun is too bright in the day.")], pics={"at night": "🌙", "in the day": "☀️"}, o="O2"))],
        [("Sun", "the star that gives us light", "☀️"), ("day", "when it is light", "🌞"), ("night", "when it is dark", "🌙"), ("star", "a tiny light in the night sky", "⭐")],
        T=[k_sort(DN, ["Day", "Night"], "O2", "Is each one in the day or at night?"), k_pick(DN, "Night", "O2", "Which one happens at NIGHT?"), k_pick(DN, "Day", "O2", "Which one happens in the DAY?"),
           k_order([(["morning", "afternoon", "evening", "night"], "The Sun rises in the morning, is high in the afternoon, sets in the evening, and then it is night.")], "O2", "Put the times of day in order."),
           k_word([("Sun", "the star that gives us light", "☀️"), ("day", "when it is light", "🌞"), ("night", "when it is dark", "🌙"), ("star", "a tiny light in the night sky", "⭐")], "O2")],
        deep=[k_claim([("It is dark at night because the Sun goes out.", False, "The Sun still shines; our side of the Earth is facing away from it."), ("You should never look straight at the Sun.", True, "It is so bright it can hurt your eyes."), ("Owls hunt at night.", True, "Many owls are awake at night.")], "O2"),
              k_all(DN, "Night", "O2", "Tap ALL the things that happen at night."), k_odd(DN, "O2")],
        ex=EXQ(k_sort(DN, ["Day", "Night"], "O2", "Is each one in the day or at night?")))
    U.append(u)
    return U



# ============================================================== STAGE 2
def stage2():
    U = []
    # ---------------------------------------------------------- 1 Living things and habitats
    u = unit(1, "Living Things and Habitats", "Biology", "Animals and plants live in different habitats that give them what they need. Grouping animals and what they eat.",
             "Know that a habitat gives a living thing food, water and shelter, and match animals to habitats.", "Sort animals into groups and know what some animals eat.", 2)
    HAB = [("fish", "🐟", "Water"), ("crab", "🦀", "Water"), ("octopus", "🐙", "Water"), ("whale", "🐋", "Water"), ("frog", "🐸", "Water"),
           ("camel", "🐫", "Desert"), ("scorpion", "🦂", "Desert"), ("lizard", "🦎", "Desert"),
           ("monkey", "🐒", "Forest"), ("owl", "🦉", "Forest"), ("deer", "🦌", "Forest"), ("squirrel", "🐿️", "Forest"), ("polar bear", "🐻‍❄️", "Ice"), ("penguin", "🐧", "Ice"), ("seal", "🦭", "Ice")]
    W1 = [("habitat", "the place where a plant or animal lives", "🏞️"), ("shelter", "a safe place to hide and rest", "🏠"), ("desert", "a very dry, hot place", "🏜️"), ("forest", "a place with lots of trees", "🌲"), ("pond", "a small area of still water", "🪷")]
    build_sec(u, "1.1", "Habitats", "O1", [
        ("idea", "A home with everything it needs", ["A **habitat** is the place where a plant or animal lives. A good habitat gives it **food**, **water** and **shelter**."], EM(("🐸", 1), ("🪷", 2))),
        ("check", PIC("Where does a fish live?", "in water", [("in a desert", "A fish needs water to breathe."), ("up a tree", "A fish cannot breathe in air.")], pics={"in water": "🌊", "in a desert": "🏜️", "up a tree": "🌳"}, pic="🐟", o="O1")),
        ("idea", "Fitting the habitat", ["A camel can go a long time without water, so it can live in the hot, dry **desert**. A polar bear has thick fur to keep warm on the **ice**."], EM(("🐫", 1), ("🐻‍❄️", 1))),
        ("mistake", "Zoo is not a habitat", ["A zoo keeps animals, but their natural habitat is where they live in the wild."]),
        ("check", PIC("Which animal is best suited to the cold ice?", "penguin", [("camel", "Camels live in hot deserts."), ("monkey", "Monkeys live in warm forests.")], pics={"penguin": "🐧", "camel": "🐫", "monkey": "🐒"}, o="O1"))],
        W1,
        T=[k_sort(HAB, ["Water", "Desert", "Forest", "Ice"], "O1", "Which habitat does each animal live in?"), k_pick(HAB, "Desert", "O1", "Which animal lives in the DESERT?"), k_pick(HAB, "Water", "O1", "Which animal lives in WATER?"),
           k_pick(HAB, "Ice", "O1", "Which animal lives on the ICE?"), k_word(W1, "O1")],
        deep=[k_odd(HAB, "O1"), k_all(HAB, "Forest", "O1", "Tap ALL the animals that live in a forest."),
              k_claim([("A camel would be happy living in the sea.", False, "A camel is suited to the dry desert, not water."), ("A habitat gives an animal food, water and shelter.", True, "That is what a habitat provides."), ("A polar bear's thick fur helps it live on the ice.", True, "Thick fur keeps it warm in the cold.")], "O1")],
        ex=EXQ(k_pick(HAB, "Forest", "O1", "Which animal lives in a FOREST?")))
    FOOD = [("rabbit", "🐰", "Plants"), ("cow", "🐄", "Plants"), ("giraffe", "🦒", "Plants"), ("panda", "🐼", "Plants"), ("lion", "🦁", "Meat"), ("shark", "🦈", "Meat"), ("eagle", "🦅", "Meat"), ("wolf", "🐺", "Meat"), ("bear", "🐻", "Both"), ("pig", "🐷", "Both")]
    GRP = [("dog", "🐶", "Mammal"), ("cow", "🐄", "Mammal"), ("whale", "🐋", "Mammal"), ("parrot", "🦜", "Bird"), ("eagle", "🦅", "Bird"), ("penguin", "🐧", "Bird"), ("salmon", "🐟", "Fish"), ("shark", "🦈", "Fish"), ("snake", "🐍", "Reptile"), ("turtle", "🐢", "Reptile"), ("lizard", "🦎", "Reptile")]
    build_sec(u, "1.2", "Animal groups and food", "O2", [
        ("idea", "Groups of animals", ["**Mammals** have hair or fur and feed their babies milk. **Birds** have feathers and lay eggs. **Fish** have scales and fins and live in water. **Reptiles** have dry, scaly skin."], EM(("🐶", 1), ("🦜", 1), ("🐟", 1), ("🐍", 1))),
        ("check", PIC("Which animal has feathers?", "parrot", [("dog", "A dog has fur."), ("snake", "A snake has scales.")], pics={"parrot": "🦜", "dog": "🐶", "snake": "🐍"}, o="O2")),
        ("idea", "What do animals eat?", ["Some animals eat only **plants**, like rabbits. Some eat **other animals**, like lions. Some eat **both**, like bears."], EM(("🐰", 1), ("🦁", 1), ("🐻", 1))),
        ("mistake", "A whale is not a fish", ["A whale lives in water, but it breathes air and feeds its baby milk, so it is a mammal."]),
        ("check", PIC("What does a rabbit eat?", "plants", [("meat", "Rabbits do not eat other animals."), ("stones", "Stones are not food.")], pics={"plants": "🥕", "meat": "🍖", "stones": "🪨"}, pic="🐰", o="O2"))],
        [("mammal", "has fur and feeds its babies milk", "🐶"), ("bird", "has feathers and lays eggs", "🐦"), ("fish", "has fins and lives in water", "🐟"), ("reptile", "has dry, scaly skin", "🦎"), ("feathers", "soft covering of a bird", "🪶")],
        T=[k_sort(GRP, ["Mammal", "Bird", "Fish", "Reptile"], "O2", "Which group is each animal in?"), k_pick(GRP, "Bird", "O2", "Which animal is a BIRD?"), k_pick(FOOD, "Meat", "O2", "Which animal eats MEAT?"),
           k_sort(FOOD, ["Plants", "Meat"], "O2", "Does each animal eat plants or meat?"), k_pick(GRP, "Reptile", "O2", "Which animal is a REPTILE?")],
        deep=[k_odd(GRP, "O2"), k_claim([("A whale is a fish because it lives in water.", False, "A whale breathes air and feeds its baby milk: it is a mammal."), ("A penguin is a bird even though it cannot fly.", True, "It has feathers and lays eggs, so it is a bird."), ("All animals eat meat.", False, "Rabbits and cows eat only plants.")], "O2"),
              k_all(GRP, "Mammal", "O2", "Tap ALL the mammals.")],
        ex=EXQ(k_pick(GRP, "Fish", "O2", "Which animal is a FISH?")))
    U.append(u)
    # ---------------------------------------------------------- 2 Growing up and staying healthy
    u = unit(2, "Growing Up and Staying Healthy", "Biology", "Animals, including humans, have young that grow into adults. Food, exercise, sleep and washing keep us healthy.",
             "Know that animals have young that grow into adults and match young to adults.", "Know what humans need to stay healthy.", 2)
    YA = [("puppy", "dog"), ("kitten", "cat"), ("calf", "cow"), ("chick", "hen"), ("tadpole", "frog"), ("lamb", "sheep"), ("foal", "horse"), ("baby", "adult person")]
    build_sec(u, "2.1", "Young and adults", "O1", [
        ("idea", "Growing up", ["Animals have **young**. The young grow into **adults**. A puppy grows into a dog. A baby grows into a child, then a teenager, then an adult."], EM(("🐶", 1), ("🐕", 1))),
        ("check", PIC("What does a kitten grow into?", "cat", [("dog", "A puppy grows into a dog."), ("hen", "A chick grows into a hen.")], pics={"cat": "🐈", "dog": "🐕", "hen": "🐔"}, pic="🐱", o="O1")),
        ("idea", "Some young look different", ["A **tadpole** does not look like a frog at first. It grows legs, loses its tail and becomes a frog. A caterpillar becomes a butterfly."], EM(("🐸", 1), ("🦋", 1))),
        ("check", PIC("What does a tadpole grow into?", "frog", [("fish", "A tadpole looks a bit like a fish but becomes a frog."), ("snake", "Snakes hatch from eggs as small snakes.")], pics={"frog": "🐸", "fish": "🐟", "snake": "🐍"}, o="O1"))],
        [("young", "a baby animal", "🐣"), ("adult", "a grown-up", "🧑"), ("grow", "to get bigger and older", "📏"), ("tadpole", "a young frog", "🐸")],
        T=[k_match(YA, "O1", "Match each young animal to its adult."), lambda r: (lambda y: PIC(f"What does a {y[0]} grow into?", y[1], [(x, "") for x in others(r, [a for _, a in YA], y[1])], o="O1"))(pick(r, YA)),
           k_order([(["baby", "child", "teenager", "adult"], "People grow from babies into children, teenagers and then adults."), (["egg", "tadpole", "froglet", "frog"], "A frog lays eggs; tadpoles hatch, grow legs (froglet), then become frogs."),
                    (["egg", "caterpillar", "chrysalis", "butterfly"], "A caterpillar hatches from an egg, makes a chrysalis and comes out as a butterfly.")], "O1", "Put the stages in order, youngest first."),
           k_word([("young", "a baby animal", "🐣"), ("adult", "a grown-up", "🧑"), ("tadpole", "a young frog", "🐸"), ("caterpillar", "a young butterfly", "🐛")], "O1")],
        deep=[k_claim([("A tadpole grows into a fish.", False, "A tadpole grows into a frog."), ("A puppy grows into a dog.", True, "Young dogs are called puppies."), ("All young animals look like their parents.", False, "A caterpillar looks very different from a butterfly.")], "O1"),
              lambda r: PIC("Which young animal looks LEAST like its parent?", "caterpillar", [("kitten", "A kitten looks like a small cat."), ("puppy", "A puppy looks like a small dog.")], pics={"caterpillar": "🐛", "kitten": "🐱", "puppy": "🐶"}, o="O1", d="H"),
              lambda r: (lambda y: PIC(f"Which is the young of a {y[1]}?", y[0], [(x, "") for x in others(r, [a for a, _ in YA], y[0])], o="O1", d="H"))(pick(r, YA))],
        ex=EXQ(k_match(YA, "O1", "Match each young animal to its adult.")))
    HL = [("apple", "🍎", "Healthy"), ("carrot", "🥕", "Healthy"), ("water", "💧", "Healthy"), ("broccoli", "🥦", "Healthy"), ("fish", "🐟", "Healthy"),
          ("sweets", "🍬", "Only sometimes"), ("cake", "🍰", "Only sometimes"), ("fizzy drink", "🥤", "Only sometimes"), ("crisps", "🍟", "Only sometimes"), ("doughnut", "🍩", "Only sometimes")]
    HH = [("brushing teeth", "🪥", "Healthy habit"), ("washing hands", "🧼", "Healthy habit"), ("sleeping well", "😴", "Healthy habit"), ("running and playing", "🏃", "Healthy habit"), ("staying up very late", "🌙", "Not healthy"), ("sweets every meal", "🍬", "Not healthy"), ("no exercise all week", "🛋️", "Not healthy")]
    build_sec(u, "2.2", "Staying healthy", "O2", [
        ("idea", "What keeps us healthy", ["To stay healthy we need to **eat** different kinds of food, **drink water**, **exercise**, **sleep** and keep **clean**."], EM(("🍎", 1), ("💧", 1), ("🏃", 1), ("😴", 1), ("🧼", 1))),
        ("check", PIC("Which drink is best for you every day?", "water", [("fizzy drink", "Fizzy drinks have lots of sugar."), ("milkshake", "Milkshake is a treat.")], pics={"water": "💧", "fizzy drink": "🥤", "milkshake": "🥛"}, o="O2")),
        ("tip", "Wash your hands", ["Wash your hands with soap before you eat and after the toilet. It washes away germs that can make you ill."]),
        ("check", PIC("Why do we wash our hands before eating?", "to wash away germs", [("to make them wet", "Water alone is not the point – soap removes germs."), ("to make them warm", "It is about germs, not warmth.")], o="O2"))],
        [("healthy", "well and strong", "💪"), ("exercise", "moving your body to keep fit", "🏃"), ("germs", "tiny living things that can make you ill", "🦠"), ("sleep", "rest your body at night", "😴")],
        T=[k_sort(HL, ["Healthy", "Only sometimes"], "O2", "Is each food good every day, or only sometimes?"), k_pick(HL, "Healthy", "O2", "Which food is the healthiest choice?"),
           k_sort(HH, ["Healthy habit", "Not healthy"], "O2", "Is each one healthy or not?"), k_pick(HH, "Healthy habit", "O2", "Which one is a HEALTHY habit?")],
        deep=[k_claim([("You only need to brush your teeth once a week.", False, "Brush twice every day to keep teeth healthy."), ("Exercise helps keep your body healthy.", True, "Moving makes your heart and muscles strong."), ("Cake is fine sometimes, as a treat.", True, "Treats are fine sometimes, not every day.")], "O2"),
              k_all(HL, "Healthy", "O2", "Tap ALL the foods that are good to eat every day."), k_odd(HH, "O2")],
        ex=EXQ(k_pick(HH, "Healthy habit", "O2", "Which one is a HEALTHY habit?")))
    U.append(u)
    # ---------------------------------------------------------- 3 Using materials
    u = unit(3, "Using Materials", "Chemistry", "Choosing a material for a job, and changing the shape of materials by squashing, bending, twisting and stretching.",
             "Choose a suitable material for a job and say why.", "Know that some materials change shape when squashed, bent, twisted or stretched.", 2)
    JOB = [("window", "glass – you can see through it", "🪟"), ("raincoat", "plastic – keeps water out", "🧥"), ("spoon", "metal – strong and hard", "🥄"), ("towel", "fabric – soaks up water", "🛁"), ("table", "wood – strong and stiff", "🪵")]
    build_sec(u, "3.1", "The right material for the job", "O1", [
        ("idea", "Why this material?", ["We choose a material because of what it can do. A window is made of **glass** because you can see through it. A raincoat is **waterproof** so rain cannot get in."], EM(("🪟", 1), ("🧥", 1))),
        ("check", PIC("Which material is best for a raincoat?", "plastic", [("paper", "Paper gets soggy and tears."), ("wool", "Wool soaks up the rain.")], pics={"plastic": "🧥", "paper": "📄", "wool": "🧶"}, o="O1")),
        ("example", "Testing a material", "Which cloth is best for drying a cup?", [("drop water on each cloth", "watch where it goes"), ("the towel soaks it up", "it is absorbent")], "A towel, because it soaks up water."),
        ("check", PIC("Why is a window made of glass?", "you can see through it", [("it is soft", "Glass is hard."), ("it bends easily", "Glass does not bend.")], o="O1"))],
        [("waterproof", "does not let water through", "☔"), ("transparent", "you can see through it", "🪟"), ("strong", "does not break easily", "💪"), ("absorbent", "soaks up water", "🧽")],
        T=[k_match([(a, b) for a, b, _ in JOB], "O1", "Match each object to the best material."), lambda r: (lambda j: PIC(f"What is the best material for a {j[0]}?", j[1].split(" – ")[0], [(x, "") for x in others(r, [b.split(" – ")[0] for _, b, _ in JOB], j[1].split(" – ")[0])], pic=j[2], o="O1"))(pick(r, JOB)),
           k_word([("waterproof", "does not let water through", "☔"), ("transparent", "you can see through it", "🪟"), ("strong", "does not break easily", "💪"), ("absorbent", "soaks up water", "🧽"), ("flexible", "bends without breaking", "🪢")], "O1"),
           k_sort([("umbrella", "☂️", "Waterproof"), ("wellies", "🥾", "Waterproof"), ("raincoat", "🧥", "Waterproof"), ("sponge", "🧽", "Soaks up water"), ("towel", "🛁", "Soaks up water"), ("kitchen roll", "🧻", "Soaks up water")], ["Waterproof", "Soaks up water"], "O1", "Is each one waterproof or does it soak up water?")],
        deep=[k_claim([("A chocolate teapot would work well.", False, "Chocolate melts when hot tea is poured in."), ("A paper umbrella would keep you dry.", False, "Paper is not waterproof; it gets soggy."), ("Metal is a good material for a saucepan.", True, "Metal is strong and does not melt on the cooker.")], "O1"),
              lambda r: PIC("Mia wants to make a window for her model house. Which material should she use?", "clear plastic", [("cardboard", "You cannot see through cardboard."), ("fabric", "Fabric is not see-through.")], o="O1", d="H", reason="It must be transparent so light comes in."),
              lambda r: MS("Tap ALL the materials that are waterproof.", ["plastic", "rubber"], ["paper", "cotton"], o="O1", d="H", reason="Plastic and rubber keep water out; paper and cotton soak it up.")],
        ex=EXQ(k_match([(a, b) for a, b, _ in JOB], "O1", "Match each object to the best material.")))
    SH = [("squash a sponge", "🧽", "Squash"), ("squash play dough", "🟣", "Squash"), ("bend a straw", "🥤", "Bend"), ("bend a pipe cleaner", "〰️", "Bend"), ("twist a towel", "🛁", "Twist"), ("twist a lid", "🫙", "Twist"), ("stretch an elastic band", "➰", "Stretch"), ("stretch a balloon", "🎈", "Stretch")]
    build_sec(u, "3.2", "Changing shape", "O2", [
        ("idea", "Squash, bend, twist, stretch", ["We can change the shape of some materials. We can **squash** play dough, **bend** a straw, **twist** a towel and **stretch** an elastic band."], EM(("🟣", 1), ("🥤", 1), ("➰", 1))),
        ("check", PIC("You pull an elastic band so it gets longer. What are you doing?", "stretching", [("squashing", "Squashing makes it flatter."), ("twisting", "Twisting turns it round.")], o="O2", pic="➰")),
        ("mistake", "Not every material changes shape", ["A stone or a glass will not squash or bend – if you push hard, it may break."]),
        ("check", PIC("Which one can you squash easily?", "sponge", [("rock", "A rock is hard."), ("spoon", "A metal spoon is hard.")], pics={"sponge": "🧽", "rock": "🪨", "spoon": "🥄"}, o="O2"))],
        [("squash", "press to make it flatter", "🤏"), ("bend", "make it curve", "↪️"), ("twist", "turn round and round", "🌀"), ("stretch", "pull to make it longer", "↔️")],
        T=[k_sort(SH, ["Squash", "Bend", "Twist", "Stretch"], "O2", "What is happening to each one?"), k_pick(SH, "Stretch", "O2", "Which one is being STRETCHED?"), k_pick(SH, "Bend", "O2", "Which one is being BENT?"),
           k_word([("squash", "press to make it flatter", "🤏"), ("bend", "make it curve", "↪️"), ("twist", "turn round and round", "🌀"), ("stretch", "pull to make it longer", "↔️")], "O2")],
        deep=[k_claim([("You can squash a stone with your hands.", False, "A stone is too hard to squash."), ("An elastic band goes back to its shape after stretching.", True, "That is why it is called elastic."), ("Play dough stays squashed when you let go.", True, "Play dough keeps its new shape.")], "O2"),
              k_all(SH, "Squash", "O2", "Tap ALL the pictures where something is being SQUASHED.", d="H"), lambda r: MS("Tap ALL the things you can bend without breaking.", ["a straw", "a pipe cleaner"], ["a glass", "a rock"], o="O2", d="H", reason="Straws and pipe cleaners bend; glass breaks and rock is too hard.")],
        ex=EXQ(k_pick(SH, "Twist", "O2", "Which one is being TWISTED?")))
    U.append(u)
    # ---------------------------------------------------------- 4 Light and dark
    u = unit(4, "Light and Dark", "Physics", "Light comes from light sources. We need light to see, and darkness is the absence of light. Shadows form when light is blocked.",
             "Name light sources and know that we need light to see.", "Know that a shadow forms when an object blocks light.", 2)
    LS = [("Sun", "☀️", "Light source"), ("torch", "🔦", "Light source"), ("candle", "🕯️", "Light source"), ("lamp", "💡", "Light source"), ("fire", "🔥", "Light source"), ("TV screen", "📺", "Light source"),
          ("mirror", "🪞", "Not a light source"), ("book", "📕", "Not a light source"), ("spoon", "🥄", "Not a light source"), ("ball", "⚽", "Not a light source"), ("cup", "☕", "Not a light source")]
    build_sec(u, "4.1", "Light sources", "O1", [
        ("idea", "Light sources make light", ["A **light source** gives out its own light. The **Sun**, a **torch**, a **candle** and a **lamp** are light sources. We need light to **see**."], EM(("☀️", 1), ("🔦", 1), ("🕯️", 1), ("💡", 1))),
        ("check", PIC("Which one is a light source?", "torch", [("mirror", "A mirror only reflects light."), ("book", "A book does not make light.")], pics={"torch": "🔦", "mirror": "🪞", "book": "📕"}, o="O1")),
        ("mistake", "A mirror is not a light source", ["A mirror looks bright, but it only bounces back light from somewhere else. In a dark room it does not shine."]),
        ("check", PIC("In a room with no light at all, what can you see?", "nothing", [("everything", "We need light to see."), ("only bright colours", "Without light even bright colours cannot be seen.")], o="O1", pic="🌑"))],
        [("light", "lets us see", "💡"), ("light source", "something that gives out light", "🔦"), ("dark", "when there is no light", "🌑"), ("reflect", "bounce light back", "🪞")],
        T=[k_sort(LS, ["Light source", "Not a light source"], "O1", "Is each one a light source?"), k_pick(LS, "Light source", "O1", "Which one is a LIGHT SOURCE?"), k_pick(LS, "Not a light source", "O1", "Which one is NOT a light source?"),
           k_word([("light", "lets us see", "💡"), ("light source", "something that gives out light", "🔦"), ("dark", "when there is no light", "🌑"), ("reflect", "bounce light back", "🪞")], "O1")],
        deep=[k_all(LS, "Light source", "O1", "Tap ALL the light sources."), k_odd(LS, "O1"),
              k_claim([("The Moon is a light source.", False, "The Moon reflects light from the Sun; it does not make its own."), ("We need light to see.", True, "Without light our eyes cannot see anything."), ("A mirror gives out its own light.", False, "A mirror only reflects light.")], "O1")],
        ex=EXQ(k_pick(LS, "Light source", "O1", "Which one gives out its own light?")))
    SHAD = [("wooden block", "🧱", "Dark shadow"), ("book", "📕", "Dark shadow"), ("teddy", "🧸", "Dark shadow"), ("hand", "✋", "Dark shadow"), ("cardboard box", "📦", "Dark shadow"), ("tree", "🌳", "Dark shadow"),
            ("clear glass", "🥛", "Little or no shadow"), ("window", "🪟", "Little or no shadow"), ("clear plastic bottle", "🧴", "Little or no shadow"), ("cling film", "🎞️", "Little or no shadow")]
    build_sec(u, "4.2", "Shadows", "O2", [
        ("idea", "Blocking the light", ["When something **blocks** light, a dark **shadow** forms behind it. Your body makes a shadow on a sunny day."], EM(("☀️", 1), ("🧍", 1), ("⬛", 1))),
        ("check", PIC("What do you need to make a shadow?", "light and an object to block it", [("only darkness", "With no light there is no shadow."), ("only water", "Water does not make shadows on its own.")], o="O2")),
        ("example", "Shadow puppets", "How does a shadow puppet work?", [("shine a torch at a wall", "the wall is lit"), ("put your hand in the way", "your hand blocks the light"), ("a dark shape appears", "that is the shadow")], "The hand blocks light, so a shadow forms."),
        ("check", PIC("Which object will make the darkest shadow?", "a wooden block", [("clear glass", "Light goes through clear glass."), ("a thin tissue", "Some light passes through a tissue.")], o="O2"))],
        [("shadow", "a dark shape where light is blocked", "👤"), ("block", "stop something getting through", "🧱"), ("torch", "a small light you can carry", "🔦")],
        T=[lambda r: PIC("Where does a shadow form?", "behind the object, away from the light", [("in front of the light", "The light is on the other side."), ("inside the torch", "Shadows form on surfaces behind objects.")], o="O2"),
           k_sort(SHAD, ["Dark shadow", "Little or no shadow"], "O2", "Will each one make a dark shadow?"), k_pick(SHAD, "Dark shadow", "O2", "Which one will make the DARKEST shadow?"), k_pick(SHAD, "Little or no shadow", "O2", "Which one lets light through, so it makes almost no shadow?"),
           k_word([("shadow", "a dark shape where light is blocked", "👤"), ("block", "stop something getting through", "🧱"), ("torch", "a small light you can carry", "🔦"), ("light", "lets us see", "💡")], "O2"),
           k_order([(["shine the torch", "put the object in the way", "see the shadow"], "Light first, then block it, then the shadow appears.")], "O2", "Put the steps for making a shadow in order.")],
        deep=[k_claim([("You can make a shadow in a completely dark room.", False, "A shadow needs light to be blocked."), ("Your shadow is the same shape as you.", True, "It has your outline because your body blocks the light."), ("Clear glass makes a dark shadow.", False, "Light passes through clear glass.")], "O2"),
              k_all(SHAD, "Dark shadow", "O2", "Tap ALL the things that make a dark shadow."), k_odd(SHAD, "O2"), lambda r: PIC("Zara moves her hand closer to the torch. What happens to the shadow on the wall?", "it gets bigger", [("it gets smaller", "Closer to the light blocks more light."), ("it disappears", "The hand still blocks the light.")], o="O2", d="VH", reason="The closer the object is to the light, the bigger the shadow."),
              lambda r: MS("Tap ALL the things that would make a good shadow puppet.", ["card", "your hand"], ["clear plastic", "glass"], o="O2", d="H", reason="Card and hands block light; clear materials let light through.")],
        ex=EXQ(lambda r: PIC("Where does a shadow form?", "behind the object, away from the light", [("in front of the light", "The light is on the other side.")], o="O2")))
    U.append(u)
    # ---------------------------------------------------------- 5 Electricity
    u = unit(5, "Electricity", "Physics", "Things that use electricity, staying safe with electricity, and making a simple circuit with a battery, wires and a bulb.",
             "Name things that use electricity and know how to stay safe.", "Know that a complete circuit is needed to light a bulb.", 2)
    EL = [("TV", "📺", "Uses electricity"), ("lamp", "💡", "Uses electricity"), ("fridge", "🧊", "Uses electricity"), ("computer", "💻", "Uses electricity"), ("phone", "📱", "Uses electricity"), ("toaster", "🍞", "Uses electricity"),
          ("bicycle", "🚲", "No electricity"), ("book", "📕", "No electricity"), ("scissors", "✂️", "No electricity"), ("spoon", "🥄", "No electricity"), ("skipping rope", "🪢", "No electricity")]
    build_sec(u, "5.1", "Using electricity safely", "O1", [
        ("idea", "Electricity makes things work", ["**Electricity** makes many things work: lights, TVs, fridges and computers. Some get it from the **mains** (a plug in the wall) and some from a **battery**."], EM(("🔌", 1), ("🔋", 1), ("💡", 1))),
        ("check", PIC("Which one uses electricity?", "TV", [("book", "A book needs no electricity."), ("bicycle", "You power a bicycle with your legs.")], pics={"TV": "📺", "book": "📕", "bicycle": "🚲"}, o="O1")),
        ("mistake", "Mains electricity is dangerous", ["Never put anything into a plug socket and never touch plugs with wet hands. Mains electricity can badly hurt you."]),
        ("check", PIC("Which is SAFE?", "asking an adult to plug things in", [("touching a plug with wet hands", "Water and electricity are dangerous together."), ("poking a socket with a pencil", "Never put anything into a socket.")], o="O1"))],
        [("electricity", "energy that makes things work", "⚡"), ("battery", "a small store of electricity", "🔋"), ("plug", "connects a machine to the mains", "🔌"), ("socket", "the place in the wall a plug goes in", "🔌")],
        T=[k_sort(EL, ["Uses electricity", "No electricity"], "O1", "Does each one use electricity?"), k_pick(EL, "Uses electricity", "O1", "Which one uses electricity?"), k_pick(EL, "No electricity", "O1", "Which one does NOT use electricity?"),
           k_sort([("ask an adult to plug it in", "🧑", "Safe"), ("keep drinks away from computers", "💻", "Safe"), ("touch a plug with wet hands", "💧", "Dangerous"), ("poke a socket", "🔌", "Dangerous"), ("fly a kite near power lines", "🪁", "Dangerous"), ("switch off at the wall when finished", "🖐️", "Safe")], ["Safe", "Dangerous"], "O1", "Is each one safe or dangerous?")],
        deep=[k_all(EL, "Uses electricity", "O1", "Tap ALL the things that use electricity."), k_odd(EL, "O1"),
              k_claim([("It is safe to touch a plug with wet hands.", False, "Water and electricity together are very dangerous."), ("A torch gets its electricity from a battery.", True, "Torches use batteries."), ("A book needs electricity.", False, "You can read a book without electricity.")], "O1")],
        ex=EXQ(k_pick(EL, "Uses electricity", "O1", "Which one needs electricity to work?")))
    CIR = [("loop with no gaps", "⭕", "Bulb lights"), ("wires joined to both ends of the battery", "🔋", "Bulb lights"), ("switch closed", "✅", "Bulb lights"), ("all clips tight", "📎", "Bulb lights"),
           ("one wire loose", "➖", "Bulb does not light"), ("no battery", "🚫", "Bulb does not light"), ("switch open", "⏸️", "Bulb does not light"), ("both wires on the same end of the battery", "↩️", "Bulb does not light"), ("a plastic straw in the loop", "🥤", "Bulb does not light")]
    build_sec(u, "5.2", "Making a circuit", "O2", [
        ("idea", "A complete loop", ["A **circuit** is a loop. Electricity flows from the **battery**, along a **wire**, through the **bulb** and back to the battery. If there is a **gap**, the bulb does not light."], {"kind": "circuit", "type": "series", "top": ["cell"], "bottom": ["lamp"]}),
        ("check", PIC("Will the bulb light if there is a gap in the circuit?", "No", [("Yes", "Electricity cannot jump across a gap.")], pics={"No": "👎", "Yes": "👍"}, o="O2")),
        ("tip", "Follow the loop", ["Put your finger on the battery and follow the wires. If you get back to the battery without a gap, the circuit is complete."]),
        ("check", PIC("Which part pushes electricity round the circuit?", "battery", [("bulb", "The bulb uses the electricity to make light."), ("wire", "The wire carries electricity.")], pics={"battery": "🔋", "bulb": "💡", "wire": "〰️"}, o="O2"))],
        [("circuit", "a complete loop for electricity", "⭕"), ("bulb", "lights up in a circuit", "💡"), ("wire", "carries electricity", "〰️"), ("gap", "a break in the loop", "↔️")],
        T=[k_match([("battery", "pushes electricity round"), ("wire", "carries electricity"), ("bulb", "gives out light"), ("switch", "opens and closes a gap")], "O2", "Match each part to its job."),
           k_word([("circuit", "a complete loop for electricity", "⭕"), ("bulb", "lights up in a circuit", "💡"), ("wire", "carries electricity", "〰️"), ("battery", "a small store of electricity", "🔋")], "O2"),
           k_sort(CIR, ["Bulb lights", "Bulb does not light"], "O2", "Will the bulb light?"), k_pick(CIR, "Bulb does not light", "O2", "In which circuit will the bulb NOT light?"), k_pick(CIR, "Bulb lights", "O2", "In which circuit WILL the bulb light?"),
           lambda r: PIC("A bulb, a battery and two wires make a complete loop. What happens?", "the bulb lights", [("nothing", "A complete circuit lets electricity flow."), ("the battery gets bigger", "Batteries do not grow.")], o="O2")],
        deep=[k_claim([("A bulb lights with only one wire.", False, "You need a complete loop, so at least two wires."), ("A switch makes a gap to turn a light off.", True, "Opening the switch breaks the loop."), ("Electricity can jump over a gap in the wire.", False, "A gap stops the flow.")], "O2"),
              k_all(CIR, "Bulb does not light", "O2", "Tap ALL the circuits where the bulb will NOT light."), k_odd(CIR, "O2"), lambda r: PIC("Leo's bulb does not light. The wires and battery look fine. What should he check first?", "that every wire is joined with no gaps", [("the colour of the wires", "Colour does not matter."), ("how big the table is", "The table does not affect the circuit.")], o="O2", d="H"),
              lambda r: MS("Tap ALL the things a simple circuit needs to light a bulb.", ["a battery", "wires"], ["a book", "water"], o="O2", d="H", reason="A battery pushes electricity through wires to the bulb.")],
        ex=EXQ(k_match([("battery", "pushes electricity round"), ("wire", "carries electricity"), ("bulb", "gives out light")], "O2", "Match each part to its job.")))
    U.append(u)
    # ---------------------------------------------------------- 6 Rocks, soil and weather
    u = unit(6, "Rocks, Soil and Weather", "Earth and Space", "Different kinds of rock and what we use them for; soil; and how the weather changes through the seasons.",
             "Describe rocks and soil and their uses.", "Describe weather in different seasons and how it changes.", 2)
    RK = [("hard", "not easily scratched", "🪨"), ("rock", "a hard natural material from the ground", "🪨"), ("soil", "the top layer of ground where plants grow", "🟫"), ("pebble", "a small smooth rock", "🫘"), ("sand", "tiny bits of rock", "🏖️")]
    USE = [("wall", "🧱", "Rock"), ("statue", "🗿", "Rock"), ("path", "🛤️", "Rock"), ("growing carrots", "🥕", "Soil"), ("flower bed", "🌷", "Soil"), ("plant pot", "🪴", "Soil")]
    build_sec(u, "6.1", "Rocks and soil", "O1", [
        ("idea", "Rocks are everywhere", ["**Rocks** are hard natural materials from the ground. Some are rough, some are smooth. We use rock for buildings, walls and statues."], EM(("🪨", 2), ("🧱", 1), ("🗿", 1))),
        ("check", PIC("Which is made from rock?", "statue", [("teddy", "A teddy is fabric."), ("T-shirt", "A T-shirt is fabric.")], pics={"statue": "🗿", "teddy": "🧸", "T-shirt": "👕"}, o="O1")),
        ("idea", "Soil", ["**Soil** is made of tiny bits of rock mixed with bits of dead plants. Plants grow in soil. Worms help to mix it."], EM(("🟫", 1), ("🪱", 1), ("🌱", 1))),
        ("check", PIC("What do plants grow in?", "soil", [("rock", "Roots cannot grow into solid rock."), ("glass", "Glass is not soil.")], pics={"soil": "🟫", "rock": "🪨", "glass": "🪟"}, o="O1"))],
        RK,
        T=[k_sort(USE, ["Rock", "Soil"], "O1", "Do we use rock or soil for each one?"), k_pick(USE, "Soil", "O1", "Which one needs SOIL?"), k_pick(USE, "Rock", "O1", "Which one is made of ROCK?"), k_word(RK, "O1")],
        deep=[k_claim([("Soil has tiny bits of rock in it.", True, "Soil is made from tiny bits of rock and dead plants."), ("Worms help to mix the soil.", True, "Worms dig and mix soil."), ("Rocks are soft and squashy.", False, "Rocks are hard.")], "O1"),
              lambda r: PIC("Which would be best for building a strong wall?", "stone", [("soil", "Soil crumbles."), ("sand", "Loose sand falls apart.")], pics={"stone": "🧱", "soil": "🟫", "sand": "🏖️"}, o="O1", d="H"), k_odd(USE + [("brick house", "🏠", "Rock")], "O1")],
        ex=EXQ(k_pick(USE, "Soil", "O1", "Which one needs SOIL?")))
    SEA = [("snowman", "⛄", "Winter"), ("building a sandcastle", "🏖️", "Summer"), ("falling leaves", "🍂", "Autumn"), ("new flowers", "🌷", "Spring"), ("ice on the pond", "🧊", "Winter"), ("ice lolly", "🍦", "Summer"), ("baby lambs", "🐑", "Spring"), ("conkers", "🌰", "Autumn")]
    build_sec(u, "6.2", "Weather and seasons", "O2", [
        ("idea", "Four seasons", ["In many places there are four **seasons**: **spring**, **summer**, **autumn** and **winter**. Summer is usually warmest. Winter is usually coldest. In some countries there is a **rainy season** and a **dry season**."], EM(("🌷", 1), ("☀️", 1), ("🍂", 1), ("⛄", 1))),
        ("check", PIC("In which season do leaves fall from many trees?", "autumn", [("summer", "Trees are full of leaves in summer."), ("spring", "New leaves grow in spring.")], pics={"autumn": "🍂", "summer": "☀️", "spring": "🌷"}, o="O2")),
        ("tip", "Measure the weather", ["A **thermometer** tells you how hot or cold it is. A **rain gauge** collects rain so you can see how much fell."]),
        ("check", PIC("What does a thermometer measure?", "how hot or cold it is", [("how much rain fell", "A rain gauge does that."), ("how windy it is", "A windsock shows wind.")], pics={"how hot or cold it is": "🌡️", "how much rain fell": "🌧️", "how windy it is": "🌬️"}, o="O2"))],
        [("season", "a part of the year with its own weather", "📅"), ("summer", "the warmest season", "☀️"), ("winter", "the coldest season", "⛄"), ("autumn", "when leaves fall", "🍂"), ("spring", "when new plants grow", "🌷"), ("thermometer", "measures how hot or cold", "🌡️")],
        T=[k_sort(SEA, ["Spring", "Summer", "Autumn", "Winter"], "O2", "Which season does each one belong to?"), k_pick(SEA, "Winter", "O2", "Which one do you see in WINTER?"), k_pick(SEA, "Summer", "O2", "Which one do you see in SUMMER?"),
           k_order([(["spring", "summer", "autumn", "winter"], "The seasons go spring, summer, autumn, winter, then spring again.")], "O2", "Put the seasons in order, starting with spring.")],
        deep=[k_claim([("Winter is usually the warmest season.", False, "Summer is usually warmest; winter is coldest."), ("A rain gauge measures how much rain falls.", True, "It collects the rain."), ("After winter comes spring.", True, "The seasons go round: winter, then spring.")], "O2"),
              k_all(SEA, "Winter", "O2", "Tap ALL the things you might see in WINTER.", d="H"), lambda r: PIC("Which season comes after summer?", "autumn", [("spring", "Spring comes before summer."), ("winter", "Winter comes after autumn.")], o="O2", d="H")],
        ex=EXQ(k_pick(SEA, "Autumn", "O2", "Which one do you see in AUTUMN?")))
    U.append(u)
    return U


def lambda_ex(f): return f(random.Random(99))


TITLES = {1: ["Living Things", "Ourselves", "Materials", "Pushes and Pulls", "Sound", "Earth and Sky"],
          2: ["Living Things and Habitats", "Growing Up and Staying Healthy", "Using Materials", "Light and Dark", "Electricity", "Rocks, Soil and Weather"]}
