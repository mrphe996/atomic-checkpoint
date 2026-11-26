# -*- coding: utf-8 -*-
"""Word bank for the Camday word games (Stages 1-6, all subjects). Written by the Camday teaching team.
Science Stages 3-6 come from the lesson word banks (with recorded audio); everything else is authored here.
Usage: python3 game_words.py  -> web/content/game-words.json"""
import json, glob, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..')

# word | short child-friendly meaning | emoji       ('# Topic' starts a topic)
AUTHORED = {
('science', 1): """
# Living things
plant|a living thing that grows in the soil|🌱
animal|a living thing that can move about on its own|🐕
alive|living, like a cat or a tree|🐈
leaf|the flat green part of a plant|🍃
flower|the colourful part of a plant|🌸
seed|a tiny thing that grows into a new plant|🌰
root|the part of a plant under the soil|🪴
stem|the stalk that holds a plant up|🌿
# My body
eye|you see with it|👁️
ear|you hear with it|👂
nose|you smell with it|👃
tongue|you taste with it|👅
hand|you touch and hold with it|✋
sense|seeing, hearing, smelling, tasting or touching|🖐️
# Materials
wood|a material that comes from trees|🪵
metal|a hard, shiny material, like a spoon|🥄
plastic|a light material used for toys and bottles|🧴
glass|a material you can see through, like a window|🪟
soft|easy to squash, like a pillow|🧸
hard|not easy to squash, like a rock|🪨
# Forces and sound
push|to move something away from you|🫸
pull|to move something towards you|🫷
sound|something you can hear|🔊
loud|a big sound, like a drum|🥁
quiet|a small sound, like a whisper|🤫
# Earth and sky
sun|the bright star that gives us light|☀️
rain|water falling from clouds|🌧️
wind|moving air|🌬️
cloud|a white or grey shape in the sky|☁️
snow|soft white ice that falls in winter|❄️
""",
('science', 2): """
# Living things and habitats
habitat|the place where an animal or plant lives|🏞️
nest|a home that birds build|🪺
water|all living things need this to drink|💧
food|what living things eat to grow|🍎
grow|to get bigger|📏
healthy|well and strong|💪
exercise|moving your body to stay healthy|🏃
baby|a very young person or animal|👶
adult|a fully grown person or animal|🧑
# Materials
bend|to change shape into a curve|🌈
stretch|to pull to make longer|🎗️
twist|to turn round and round|🌀
squash|to press so it gets flatter|🥫
melt|to change from solid to liquid when warm|🍦
freeze|to change from liquid to solid when cold|🧊
waterproof|does not let water through|☔
# Light and electricity
light|what lets us see|💡
dark|when there is no light|🌑
shadow|a dark shape made when light is blocked|👤
torch|a light you can carry|🔦
battery|it stores electricity for a toy|🔋
switch|you press it to turn a light on or off|🎚️
# Earth
rock|a hard natural material from the ground|🪨
soil|the brown earth plants grow in|🟫
season|spring, summer, autumn or winter|🍂
weather|what it is like outside: sunny, rainy…|🌦️
temperature|how hot or cold something is|🌡️
""",
('maths', 1): """
# Number
number|tells you how many|🔢
count|to say numbers in order: 1, 2, 3…|👆
zero|the number for none at all|0️⃣
more|a bigger amount|➕
less|a smaller amount|➖
equal|the same amount|🟰
add|to put numbers together|➕
take away|to make a number smaller by removing some|🍪
double|two lots of the same number|👯
half|one of two equal parts|🌗
# Shape and measure
circle|a round flat shape|⚪
square|a shape with 4 equal sides|🟦
triangle|a shape with 3 sides|🔺
long|from one end far to the other|🐍
short|not long|🐛
heavy|hard to lift|🏋️
light|easy to lift|🪶
first|number 1 in a line|🥇
""",
('maths', 2): """
# Number
odd|a number like 1, 3, 5, 7|🧦
even|a number like 2, 4, 6, 8|👟
tens|groups of ten|🔟
ones|single units in a number|1️⃣
plus|another word for add|➕
minus|another word for take away|➖
total|all of them added together|🧮
difference|how much bigger one number is than another|↔️
multiply|to add equal groups again and again|✖️
share|to split into equal groups|🍕
# Shape and measure
rectangle|a shape with 4 sides and 4 right angles|▭
cube|a 3D shape with 6 square faces|🧊
sphere|a 3D shape like a ball|⚽
cylinder|a 3D shape like a can|🥫
centimetre|a small unit for measuring length|📏
clock|it shows the time|🕒
o'clock|the time when the long hand points to 12|🕛
pattern|something that repeats in a rule|🔁
""",
('maths', 3): """
# Number
hundreds|groups of a hundred|💯
estimate|a sensible guess about how many|🤔
round|to change to the nearest ten or hundred|🎯
fraction|a part of a whole|🍰
quarter|one of four equal parts|◔
division|sharing into equal groups|➗
array|objects in equal rows and columns|🍫
inverse|the opposite operation, like add and subtract|🔄
# Shape and measure
pentagon|a shape with 5 sides|⬠
hexagon|a shape with 6 sides|⬡
vertex|a corner of a shape|📐
symmetry|when one half matches the other half exactly|🦋
kilogram|a unit for measuring mass|⚖️
litre|a unit for measuring capacity|🥛
pictogram|a chart that uses pictures|📊
tally|marks used for counting in fives|🖊️
""",
('maths', 4): """
# Number
thousands|groups of a thousand|🏟️
negative|a number less than zero|🥶
multiple|a number in a times table|🔁
factor|a number that divides exactly into another|🧩
remainder|what is left over after dividing|🍬
decimal|a number with a decimal point, like 2.5|🔸
percentage|a part out of a hundred|💯
# Shape and measure
angle|the amount of turn between two lines|📐
right angle|a quarter turn, 90 degrees|∟
perimeter|the distance all the way round a shape|🔲
area|the space a flat shape covers|🟩
net|a flat shape that folds into a 3D shape|📦
probability|how likely something is to happen|🎲
likely|will probably happen|🌤️
impossible|cannot happen|🚫
coordinates|two numbers that give a position on a grid|📍
""",
('maths', 5): """
# Number
prime|a number with exactly two factors|🔑
square number|a number made by multiplying a number by itself|⏹️
equivalent|having the same value|⚖️
numerator|the top number of a fraction|⬆️
denominator|the bottom number of a fraction|⬇️
ratio|compares the sizes of two amounts|🍹
proportion|a part compared with the whole|🥧
# Shape and measure
acute|an angle smaller than a right angle|📌
obtuse|an angle between 90 and 180 degrees|🔓
parallel|lines that never meet|🛤️
perpendicular|lines that meet at a right angle|✚
reflection|a mirror image of a shape|🪞
translation|sliding a shape without turning it|➡️
mode|the value that appears most often|🔝
median|the middle value when the data is in order|🎯
range|the biggest value minus the smallest value|📏
""",
('maths', 6): """
# Number and algebra
integer|a whole number, positive, negative or zero|🔢
index|a small number that shows a power|🔼
formula|a rule written with letters|🧪
variable|a letter that stands for a number|❓
sequence|numbers in order that follow a rule|🔢
term|one number in a sequence|🔹
simplify|to write in the simplest way|✂️
# Shape and measure
radius|from the centre of a circle to the edge|⭕
diameter|a line across a circle through its centre|⌀
circumference|the distance around a circle|🔄
volume|the space a 3D shape takes up|📦
rotation|turning a shape about a point|🔃
quadrilateral|a shape with 4 sides|🔷
mean|the total shared equally between the values|➗
frequency|how many times something happens|📶
""",
('english', 1): """
# Family and home
mum|your mother|👩
dad|your father|👨
sister|a girl in your family|👧
brother|a boy in your family|👦
house|a building where people live|🏠
bed|you sleep in it|🛏️
# Animals
cat|a small furry pet that says miaow|🐱
dog|a pet that barks|🐶
fish|it swims in water|🐟
bird|it has wings and feathers|🐦
duck|a bird that swims and says quack|🦆
# Colours and food
red|the colour of a strawberry|🍓
blue|the colour of the sky|🔵
green|the colour of grass|🟢
yellow|the colour of a banana|🍌
apple|a round red or green fruit|🍎
bread|food made from flour, for sandwiches|🍞
milk|a white drink from cows|🥛
# Actions
run|to move very fast on your feet|🏃
jump|to push yourself up into the air|🦘
sing|to make music with your voice|🎤
sleep|to rest with your eyes closed|😴
""",
('english', 2): """
# People and places
teacher|a person who helps you learn|🧑‍🏫
friend|someone you like and play with|🤝
school|the place where you learn|🏫
park|an outdoor place to play|🛝
shop|a place where you buy things|🏪
farm|a place where food is grown and animals are kept|🚜
# Animals
rabbit|a small animal with long ears|🐰
horse|a big animal you can ride|🐴
frog|a green animal that jumps and lives near water|🐸
bee|an insect that makes honey|🐝
# Feelings
happy|feeling good|😊
sad|feeling unhappy|😢
angry|feeling cross|😠
scared|feeling afraid|😨
tired|needing to sleep|🥱
# Actions and describing
swim|to move through water|🏊
climb|to go up using hands and feet|🧗
read|to look at words and understand them|📖
write|to put words on paper|✍️
big|large in size|🐘
small|little in size|🐭
fast|quick|⚡
slow|not quick|🐢
""",
('english', 3): """
# Time and weather
morning|the early part of the day|🌅
evening|the late part of the day|🌇
yesterday|the day before today|⬅️
tomorrow|the day after today|➡️
sunny|full of sunshine|🌞
windy|with a lot of wind|🌬️
# Describing words
beautiful|very pretty|🌺
noisy|making a lot of noise|📢
brave|not afraid to do something difficult|🦁
careful|taking care not to make mistakes|🧐
hungry|wanting food|🍽️
thirsty|wanting a drink|🥤
# Things
bicycle|a vehicle with two wheels that you pedal|🚲
library|a place to borrow books|📚
kitchen|the room where food is cooked|🍳
garden|a place to grow flowers outside a house|🏡
present|a gift|🎁
# Actions
build|to make something by putting parts together|🧱
carry|to hold and take somewhere|🧺
share|to give part of something to others|🫶
listen|to pay attention to sounds|🎧
""",
('english', 4): """
# Describing words
enormous|very, very big|🐋
tiny|very, very small|🐜
ancient|very old|🏛️
delicious|tastes very good|😋
dangerous|could hurt you|⚠️
curious|wanting to know about things|🔍
# Stories
adventure|an exciting journey or experience|🗺️
character|a person or animal in a story|🦸
castle|a large strong building for kings and queens|🏰
treasure|gold, jewels and other precious things|💎
journey|travelling from one place to another|🧳
# Actions
explore|to travel around to find out about a place|🧭
discover|to find something for the first time|💡
whisper|to speak very quietly|🤫
shout|to say something very loudly|📣
celebrate|to do something happy for a special day|🎉
# Places
village|a small group of houses in the countryside|🏘️
island|land with water all around it|🏝️
forest|a large area full of trees|🌲
desert|a very dry place with little rain|🏜️
""",
('english', 5): """
# Describing words
fascinating|extremely interesting|🤩
furious|extremely angry|😡
exhausted|extremely tired|😩
generous|happy to give to others|🎁
confident|sure that you can do something|😎
mysterious|strange and hard to explain|🕵️
# Thinking and talking
describe|to say what something is like|🗣️
explain|to make something clear|💬
imagine|to make a picture in your mind|💭
suggest|to give an idea for others to think about|☝️
disagree|to have a different opinion|🙅
persuade|to make someone agree with you|🤝
# Science and world
environment|the world around us: air, land and water|🌍
invention|something new that someone has made|⚙️
pollution|harmful things in the air, water or land|🏭
recycle|to make used things into new things|♻️
volcano|a mountain that can throw out hot lava|🌋
""",
('english', 6): """
# Describing words
magnificent|very impressive and beautiful|👑
reluctant|not wanting to do something|😒
anxious|worried and nervous|😰
determined|not giving up|🏔️
ordinary|normal, not special|📎
remarkable|unusual and worth noticing|🌟
# Thinking and talking
conclude|to decide after thinking about the facts|🧠
compare|to look at how things are alike or different|⚖️
evidence|facts that show something is true|🔎
opinion|what someone thinks or believes|💭
summarise|to give the main points briefly|📝
predict|to say what you think will happen|🔮
# The world
community|people who live in one area|🏘️
population|the number of people living in a place|👥
technology|machines and tools made using science|💻
climate|the usual weather of a place over many years|🌡️
""",
}

def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def main():
    words = []
    for (subj, stage), txt in AUTHORED.items():
        topic = 'General'
        for line in txt.strip().splitlines():
            line = line.strip()
            if not line: continue
            if line.startswith('#'): topic = line[1:].strip(); continue
            w, d, e = [x.strip() for x in line.split('|')]
            words.append({'w': w, 'def': d, 'emoji': e, 'stage': stage, 'subj': subj, 'topic': topic})
    # word banks of the course units: Science Stages 1–6 (keys 1–6) and Mathematics Stages 1–2 (keys 11, 12)
    for key in (1, 2, 3, 4, 5, 6, 11, 12, 22, 23, 24, 25, 26):
        stage, subj = (key - 20, 'english') if key > 20 else (key - 10, 'maths') if key > 10 else (key, 'science')
        for f in sorted(glob.glob(os.path.join(ROOT, f'web/content/stage{key}-unit*.json'))):
            u = json.load(open(f)); topic = u['unit']['title']
            for s in u['sections']:
                for v in s.get('vocab') or []:
                    x = {'w': v['w'], 'def': v.get('def', ''), 'emoji': v.get('emoji', '📘'), 'stage': stage, 'subj': subj, 'topic': topic}
                    if v.get('audio') and os.path.exists(os.path.join(ROOT, 'web', v['audio'])): x['audio'] = v['audio']
                    words.append(x)
    seen, out = set(), []
    for x in words:
        k = (x['subj'], x['w'].lower())
        if k in seen or not x['def']: continue
        seen.add(k); out.append(x)
    for i, x in enumerate(out): x['id'] = f"{x['subj'][0]}{x['stage']}-{slug(x['w'])}"
    assert len({x['id'] for x in out}) == len(out)
    json.dump({'words': out, 'note': 'Camday word games – written by the Camday teaching team'}, open(os.path.join(ROOT, 'web/content/game-words.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    from collections import Counter
    print(len(out), 'words'); print(sorted(Counter((x['subj'], x['stage']) for x in out).items()))

if __name__ == '__main__':
    main()
