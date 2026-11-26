# -*- coding: utf-8 -*-
"""Camday ESL Stage 2 (ages 6–7). Original texts and questions written by the Camday teaching team."""
from ekit import parse

UNITS = [
("My Family and Home", "Listening and reading", "Family words, rooms in a house, ‘this is’ and ‘my / your’, and a short text about a family.", parse("""
L 1.1 | My family | Name family members and say who they are.
W mother | the woman who is your mum | 👩
W father | the man who is your dad | 👨
W sister | a girl in your family, like you | 👧
W brother | a boy in your family, like you | 👦
W baby | a very young child | 👶
W grandma | your mum's or dad's mother | 👵
G This is… / These are… | Use ‘this is’ for one person and ‘these are’ for two or more people. | This is my sister. / These are my brothers.
g ___ is my mother. | This | These, They | One person: this is.
g ___ are my grandparents. | These | This, He | Two or more people: these are.
g This ___ my baby brother. | is | are, am | This is…
g These ___ my sisters. | are | is, am | These are…
g ___ is my father. His name is Sam. | This | These, We | One person.
g These are my ___. | cousins | cousin, cousin's | ‘These are’ needs a plural word.
g This is my ___. | aunt | aunts, auntes | ‘This is’ needs one person.
T Meet Lin's family | text
> Hello! I am Lin. I am six.
> This is my mother. She is a teacher.
> This is my father. He is a cook.
> These are my brothers, Tao and Ben. They are eight.
> This is our baby, Mei. She is very small!
q How old is Lin? | six | eight, seven | Lin says: I am six.
q What is Lin's mother? | a teacher | a cook, a doctor | My mother is a teacher.
q Who is a cook? | Lin's father | Lin's mother, Tao | My father is a cook.
q How many brothers has Lin got? | two | one, three | Tao and Ben.
q Who is the baby? | Mei | Lin, Ben | Our baby, Mei.
t Lin is eight. | F | Lin is six. Her brothers are eight.
t Lin's father is a cook. | T | He is a cook.
t The baby is big. | F | She is very small.
t Tao and Ben are brothers. | T | These are my brothers, Tao and Ben.
o This is my mother.
o These are my brothers.
o She is very small.
s mother | muther, mothr
s sister | sistor, sisster
s brother | bruther, brothr
s family | famly, familly
s baby | babby, bayby

L 1.2 | Rooms in my home | Name rooms and things at home and say where things are.
W kitchen | the room where you cook | 🍳
W bedroom | the room where you sleep | 🛏️
W bathroom | the room where you wash | 🛁
W garden | a place outside with grass and flowers | 🌷
W door | you open it to go into a room | 🚪
W window | glass in a wall – you can see out | 🪟
G in / on / under | Use ‘in’, ‘on’ and ‘under’ to say where something is. | The cat is on the bed. / The ball is under the table.
g The cat is ___ the bed. (on top) | on | in, under | On top means on.
g The shoes are ___ the bed. (below it) | under | on, in | Below means under.
g The milk is ___ the fridge. (inside) | in | on, under | Inside means in.
g The book is ___ the table. (on top) | on | under, in | On top: on.
g The dog is ___ the garden. | in | on, under | We say in the garden.
g The ball is ___ the chair. (below it) | under | on, in | Below: under.
g The toys are ___ the box. (inside) | in | on, under | Inside: in.
T Where is Teddy? | text
> Sam can't find Teddy.
> Is Teddy in the kitchen? No.
> Is Teddy in the bathroom? No.
> Sam goes into the bedroom.
> Teddy is under the bed! Now Teddy is on the bed with Sam.
q Who can't find Teddy? | Sam | Teddy, Mum | Sam can't find Teddy.
q Is Teddy in the kitchen? | No | Yes, We don't know | Is Teddy in the kitchen? No.
q Where is Teddy? | under the bed | in the bathroom, in the garden | Teddy is under the bed!
q Which room is Teddy in? | the bedroom | the kitchen, the bathroom | Sam goes into the bedroom.
q Where is Teddy at the end? | on the bed | under the bed, in the kitchen | Now Teddy is on the bed.
t Teddy is in the bathroom. | F | Teddy is in the bedroom.
t Teddy is under the bed. | T | Teddy is under the bed!
t Sam finds Teddy in the garden. | F | Sam finds him in the bedroom.
o The cat is on the bed.
o The ball is under the table.
o Teddy is in the bedroom.
s kitchen | kichen, kitchin
s window | windo, windou
s garden | gardin, gaden
s bedroom | bedrom, bedroome
"""),),
("At School", "Speaking and reading", "Classroom things, numbers, ‘a’ and ‘an’, ‘I have got…’ and a school day.", parse("""
L 2.1 | My classroom | Name classroom things and use ‘a’ and ‘an’.
W pencil | you write and draw with it | ✏️
W ruler | you draw straight lines with it | 📏
W rubber | it takes away pencil marks | 🧽
W bag | you carry your books in it | 🎒
W book | it has pages to read | 📕
W desk | a table where you work at school | 🪑
G a / an | Use ‘an’ before a, e, i, o, u sounds. Use ‘a’ before other sounds. | a pencil / an eraser
g I have got ___ apple. | an | a, the | Apple starts with a: an apple.
g This is ___ ruler. | a | an, two | Ruler starts with r: a ruler.
g It is ___ orange pencil. | an | a, some | Orange starts with o: an orange.
g I have got ___ bag. | a | an, two | Bag starts with b: a bag.
g There is ___ egg in my lunchbox. | an | a, some | Egg starts with e: an egg.
g She has got ___ book. | a | an, some | Book starts with b: a book.
g He has got ___ umbrella. | an | a, two | Umbrella starts with u: an umbrella.
T My bag | text
> Look in my school bag!
> I have got a red pencil and a blue pencil.
> I have got a ruler and a rubber.
> I have got a book about animals.
> I have got an apple for lunch. Yum!
q What colour are the pencils? | red and blue | green and blue, red and yellow | a red pencil and a blue pencil
q What is the book about? | animals | food, cars | a book about animals
q What is for lunch? | an apple | a banana, a sandwich | an apple for lunch
q How many pencils are there? | two | one, three | A red one and a blue one.
q What has the child got for drawing lines? | a ruler | an apple, a bag | a ruler
t There is an apple in the bag. | T | I have got an apple for lunch.
t The book is about cars. | F | It is about animals.
t There is a green pencil. | F | The pencils are red and blue.
o I have got a red pencil.
o This is an apple.
o Look in my bag.
s pencil | pensil, pencel
s ruler | rular, ruller
s school | scool, skool
s apple | aple, appel
s book | buk, boock

L 2.2 | My school day | Use numbers and ‘I have got / I haven't got’.
W teacher | the person who helps you learn | 🧑‍🏫
W friend | a person you like to play with | 🤝
W lunch | the meal in the middle of the day | 🥪
W playground | a place outside to play at school | 🛝
W read | look at words and understand them | 📖
W write | put words on paper | ✍️
G have got / haven't got | Say ‘I have got’ for things you own. Say ‘I haven't got’ for things you do not own. | I have got a sister. / I haven't got a dog.
g I ___ got a new bag. | have | has, am | I have got…
g She ___ got a pet cat. | has | have, is | She has got…
g We ___ got a big playground. | have | has, are | We have got…
g He ___ got a ruler. He needs one! | hasn't | haven't, isn't | He has not got → hasn't got.
g I ___ got a pen. I've got a pencil. | haven't | hasn't, am not | I have not got → haven't got.
g They ___ got two teachers. | have | has, is | They have got…
g It ___ got four legs. | has | have, are | It has got…
T Ana's school day | text
> Ana goes to school at eight o'clock.
> First, she reads a book with her teacher.
> Then she writes her name and the date.
> At twelve o'clock she has lunch with her friend Omar.
> After lunch they play in the playground. Ana loves school!
q When does Ana go to school? | at eight o'clock | at twelve o'clock, at ten o'clock | at eight o'clock
q What does Ana do first? | She reads a book. | She has lunch., She plays. | First, she reads a book.
q Who is Ana's friend? | Omar | Ben, her teacher | her friend Omar
q When is lunch? | at twelve o'clock | at eight o'clock, at three o'clock | At twelve o'clock she has lunch.
q Where do they play after lunch? | in the playground | in the kitchen, in the garden | They play in the playground.
t Ana writes her name. | T | She writes her name and the date.
t Ana has lunch at eight o'clock. | F | Lunch is at twelve o'clock.
t Ana doesn't like school. | F | Ana loves school!
o Ana loves school.
o I have got a friend.
o They play in the playground.
s teacher | teecher, techer
s friend | freind, frend
s write | rite, writ
s lunch | lunsh, lanch
s twelve | twelv, tweleve
"""),),
("Animals We Love", "Reading and speaking", "Pets and wild animals, ‘can / can't’, describing words and animal riddles.", parse("""
L 3.1 | Pets | Name pets and say what they can and can't do.
W rabbit | a small animal with long ears | 🐰
W parrot | a bird that can copy words | 🦜
W tortoise | a slow animal with a hard shell | 🐢
W hamster | a small furry pet that lives in a cage | 🐹
W fur | the soft hair on an animal | 🧶
W cage | a box with bars for a pet | 🏠
G can / can't | Use ‘can’ when someone is able to do something. Use ‘can't’ (cannot) when they are not able to. | A bird can fly. / A fish can't walk.
g A parrot ___ fly. | can | can't, cans | Parrots have wings: can.
g A tortoise ___ run fast. | can't | can, cans | Tortoises are slow: can't.
g A fish ___ swim. | can | can't, is | Fish swim: can.
g A rabbit ___ fly. | can't | can, does | Rabbits have no wings: can't.
g My dog ___ jump very high! | can | can't, cans | It is able to: can.
g A hamster ___ talk. | can't | can, is | Hamsters can't talk.
g Parrots ___ copy words. | can | can't, is | They are able to: can.
T Kim's pets | text
> Kim has got three pets.
> Pip is a parrot. He is green. He can fly and he can say ‘Hello!’
> Toby is a tortoise. He is old and slow. He can't run, but he can swim.
> Fluff is a hamster. She has got soft brown fur. She sleeps all day!
q How many pets has Kim got? | three | two, four | Kim has got three pets.
q What colour is Pip? | green | brown, red | He is green.
q What can Pip say? | Hello | Goodbye, Thank you | he can say ‘Hello!’
q What can Toby do? | swim | run, fly | he can swim
q What does Fluff do all day? | sleeps | swims, talks | She sleeps all day!
t Toby can run fast. | F | He can't run.
t Fluff has got brown fur. | T | soft brown fur
t Pip is a hamster. | F | Pip is a parrot.
o A parrot can fly.
o The tortoise is old.
o She sleeps all day.
s rabbit | rabit, rabbet
s parrot | parot, parrut
s hamster | hamstur, hamsta
s green | grean, gren
s slow | slo, sloe
"""),
"""
L 3.2 | Wild animals | Use describing words for wild animals and answer riddles.
W lion | a big wild cat that roars | 🦁
W elephant | a very big animal with a long trunk | 🐘
W monkey | an animal that climbs trees | 🐒
W crocodile | a long animal with big teeth that lives in rivers | 🐊
W tall | very high from the bottom to the top | 📏
W strong | able to lift heavy things | 💪
G Describing words (adjectives) | Describing words tell us more about a noun. They usually go before the noun. | a big elephant / a tall giraffe
g A giraffe has got a ___ neck. | long | longs, longly | Describing word before neck.
g An elephant is a ___ animal. | big | bigs, bigly | Describing word: big.
g A mouse is a ___ animal. | small | big, tall | A mouse is small.
g A lion has got ___ teeth. | sharp | sharply, sharps | Describing word: sharp.
g A tortoise is ___. | slow | fast, quick | Tortoises are slow.
g A cheetah is ___. | fast | slow, sleepy | Cheetahs run fast.
g Monkeys have got ___ tails. | long | longs, longest | Describing word: long.
T Who am I? | riddles
> I am very big and grey. I have got big ears and a long trunk. Who am I?
> I am an elephant!
> I live in trees. I have got a long tail. I love bananas. Who am I?
> I am a monkey!
> I am green and long. I swim in the river. I have got lots of sharp teeth. Who am I?
> I am a crocodile!
q Which animal is big and grey? | elephant | monkey, crocodile | big and grey, with a long trunk
q Which animal loves bananas? | monkey | elephant, crocodile | I love bananas.
q Where does the crocodile swim? | in the river | in a tree, in the sea | I swim in the river.
q What has the elephant got? | a long trunk | a long tail, sharp teeth | a long trunk
q What colour is the crocodile? | green | grey, brown | I am green and long.
t The monkey lives in trees. | T | I live in trees.
t The elephant has got small ears. | F | It has got big ears.
t The crocodile has got sharp teeth. | T | lots of sharp teeth
o The elephant is big.
o The monkey lives in trees.
o I have got a long tail.
s elephant | elefant, elephent
s monkey | monky, munkey
s tiger | tigre, tyger
s grey | grei, gray-y
s river | rivor, rivver
"""),
("Food and Shopping", "Speaking and writing", "Food words, ‘like / don't like’, ‘some / any’, and buying things at a market.", parse("""
L 4.1 | Food I like | Say what food you like and don't like.
W bread | food made from flour, often for sandwiches | 🍞
W rice | small white grains you cook and eat | 🍚
W egg | hens lay them; you can boil or fry them | 🥚
W banana | a long yellow fruit | 🍌
W carrot | an orange vegetable | 🥕
W soup | hot food you eat with a spoon | 🍲
G like / don't like / likes | Say ‘I like’ and ‘I don't like’. For he and she, say ‘likes’ and ‘doesn't like’. | I like rice. / She doesn't like eggs.
g I ___ bananas. They are yummy! | like | likes, liking | I like…
g She ___ carrots. She eats them every day. | likes | like, liking | She likes…
g I ___ like soup. It's too hot! | don't | doesn't, not | I don't like…
g He ___ like eggs. | doesn't | don't, not | He doesn't like…
g We ___ rice. | like | likes, liking | We like…
g My dad ___ bread with jam. | likes | like, liking | He likes…
g They ___ like fish. | don't | doesn't, isn't | They don't like…
T Breakfast at Grandma's | text
> It is Sunday. Tom and Mia have breakfast at Grandma's house.
> Tom likes eggs and bread. Mia doesn't like eggs.
> Mia likes bananas and milk.
> Grandma makes rice soup. Tom and Mia like Grandma's soup best!
q Where do Tom and Mia have breakfast? | at Grandma's house | at school, at a café | at Grandma's house
q What day is it? | Sunday | Monday, Saturday | It is Sunday.
q What does Tom like? | eggs and bread | bananas and milk, rice and fish | Tom likes eggs and bread.
q What doesn't Mia like? | eggs | bananas, milk | Mia doesn't like eggs.
q What do they like best? | Grandma's soup | bananas, eggs | They like Grandma's soup best!
t Mia likes bananas. | T | Mia likes bananas and milk.
t Tom doesn't like eggs. | F | Tom likes eggs.
t Grandma makes soup. | T | Grandma makes rice soup.
o I like bananas.
o She doesn't like eggs.
o Grandma makes soup.
s banana | bananna, banan
s carrot | carot, carrut
s bread | bred, braed
s breakfast | brekfast, breakfest
s yellow | yelow, yello
"""),
"""
L 4.2 | At the market | Ask for things at a market using ‘some’ and ‘any’.
W market | a place where people buy and sell food | 🧺
W apples | round fruit, red or green | 🍎
W tomato | a red fruit we eat in salads | 🍅
W fish | an animal that lives in water; we can eat it | 🐟
W buy | get something with money | 💰
W please | a kind word when you ask for something | 🙏
G some / any | Use ‘some’ in sentences. Use ‘any’ in questions and with ‘not’. | I've got some apples. / Have you got any eggs?
g I've got ___ tomatoes. | some | any, a | Sentence: some.
g Have you got ___ apples? | any | some, a | Question: any.
g I haven't got ___ bread. | any | some, a | With not: any.
g Can I have ___ fish, please? | some | any, an | Asking for something: some.
g There aren't ___ bananas. | any | some, a | With not: any.
g We need ___ eggs. | some | any, an | Sentence: some.
g Are there ___ carrots? | any | some, a | Question: any.
T At the market | dialogue
> Mum: Good morning! Have you got any tomatoes?
> Seller: Yes, I have. They are very red today.
> Mum: Can I have six tomatoes, please?
> Seller: Here you are. Anything else?
> Mum: Some apples, please. Have you got any fish?
> Seller: Sorry, I haven't got any fish today.
> Mum: That's OK. Thank you!
q What does Mum buy first? | tomatoes | apples, fish | Have you got any tomatoes?
q How many tomatoes does Mum want? | six | two, ten | six tomatoes, please
q What colour are the tomatoes? | red | green, yellow | They are very red today.
q What hasn't the seller got? | fish | apples, tomatoes | I haven't got any fish today.
q What does Mum say at the end? | Thank you! | Goodbye!, Hello! | That's OK. Thank you!
t The seller has got some fish. | F | Sorry, I haven't got any fish today.
t Mum buys some apples. | T | Some apples, please.
t Mum is polite. | T | She says please and thank you.
o Can I have some apples, please?
o Have you got any fish?
o I haven't got any eggs.
s please | pleese, plese
s tomato | tomatoe, tamato
s market | markit, marcket
s thank | thenk, thanc
s money | muney, mony
"""),
("Weather and Clothes", "Listening and writing", "Weather words, clothes, the present continuous (‘I am wearing…’) and a postcard.", parse("""
L 5.1 | What's the weather like? | Talk about the weather and use ‘It is…’.
W sunny | the sun is shining | ☀️
W rainy | water falls from the clouds | 🌧️
W windy | the air is moving fast | 🌬️
W cloudy | there are lots of clouds | ☁️
W hot | very warm | 🥵
W cold | not warm at all | 🥶
G It is… / It isn't… | We talk about the weather with ‘It is’ (It's) and ‘It isn't’. | It is sunny today. / It isn't cold.
g ___ sunny today. | It's | It, Is | It is → It's.
g It ___ raining. Take your umbrella! | is | are, am | It is…
g It ___ cold. Wear a T-shirt. | isn't | is, aren't | Not cold → isn't.
g Is it windy? Yes, it ___. | is | isn't, are | Short answer: yes, it is.
g Is it hot? No, it ___. | isn't | is, aren't | Short answer: no, it isn't.
g It ___ cloudy and grey today. | is | are, be | It is…
g Look outside! ___ snowing! | It's | Its, Is | It is → It's.
T The weather this week | text
> On Monday it is sunny and hot. We go to the beach.
> On Tuesday it is rainy. We play inside.
> On Wednesday it is windy. We fly a kite in the park.
> On Thursday it is cloudy and cold. We wear our coats.
q What is the weather like on Monday? | sunny and hot | rainy, windy | On Monday it is sunny and hot.
q Where do they go on Monday? | to the beach | to the park, to school | We go to the beach.
q When do they play inside? | on Tuesday | on Monday, on Thursday | On Tuesday it is rainy.
q What do they fly on Wednesday? | a kite | a plane, a bird | We fly a kite.
q Why do they wear coats on Thursday? | It is cold. | It is hot., It is sunny. | cloudy and cold
t It is windy on Wednesday. | T | On Wednesday it is windy.
t It is hot on Thursday. | F | It is cold on Thursday.
t They go to the beach on Tuesday. | F | They go on Monday.
o It is sunny today.
o We fly a kite.
o It isn't cold.
s sunny | suny, sonny
s windy | windi, windey
s cloudy | cloudi, clowdy
s weather | wether, weathr
s cold | colde, kold
"""),
"""
L 5.2 | What are you wearing? | Name clothes and say what people are wearing now.
W coat | a warm thing you wear outside | 🧥
W hat | you wear it on your head | 👒
W boots | strong shoes for rain or snow | 🥾
W scarf | you wear it round your neck | 🧣
W dress | a girl's or woman's clothes in one piece | 👗
W shorts | short trousers for hot days | 🩳
G I am wearing… (present continuous) | Use am / is / are + a verb with -ing for things happening now. | I am wearing a hat. / She is wearing boots.
g I ___ wearing a coat. | am | is, are | I am…
g She ___ wearing a red dress. | is | am, are | She is…
g They ___ wearing boots. | are | is, am | They are…
g He is ___ shorts. | wearing | wear, wears | is + wearing
g We are ___ scarves. It's cold! | wearing | wear, wore | are + wearing
g You ___ wearing a nice hat! | are | is, am | You are…
g It is cold, so I am wearing ___ scarf. | a | an, some | A scarf.
T A postcard from the mountains | postcard
> Dear Grandpa,
> We are in the mountains. It is snowing!
> I am wearing my blue coat, my boots and a hat.
> Dad is wearing a big scarf. Mum is making a snowman.
> See you soon!
> Love, Zara
q Who is the postcard to? | Grandpa | Mum, Zara | Dear Grandpa
q Where is Zara? | in the mountains | at the beach, at school | We are in the mountains.
q What is the weather like? | It is snowing. | It is sunny., It is hot. | It is snowing!
q What colour is Zara's coat? | blue | red, green | my blue coat
q What is Mum doing? | making a snowman | wearing a scarf, writing a postcard | Mum is making a snowman.
t Dad is wearing a scarf. | T | Dad is wearing a big scarf.
t Zara is wearing shorts. | F | She is wearing a coat, boots and a hat.
t The postcard is from Zara. | T | Love, Zara
o I am wearing a hat.
o She is wearing boots.
o It is snowing.
s scarf | scarff, scaf
s boots | bootes, buts
s dress | dres, dresse
s wearing | wearring, waring
s snowing | snowwing, snoing
"""),
("Fun and Games", "Speaking and reading", "Toys and games, actions, ‘Let's…’ and instructions for a simple game.", parse("""
L 6.1 | My toys | Name toys and say what is yours with ‘my / your / his / her’.
W kite | a toy that flies in the wind | 🪁
W doll | a toy that looks like a person | 🪆
W ball | a round toy you kick or throw | ⚽
W train | a toy with carriages on a track | 🚂
W robot | a machine toy that can move | 🤖
W puzzle | a game where you put pieces together | 🧩
G my / your / his / her | These words say who something belongs to. | This is my kite. / That is her doll.
g Ben has got a train. It's ___ train. | his | her, my | Ben is a boy: his.
g Lina has got a doll. It's ___ doll. | her | his, your | Lina is a girl: her.
g I have got a robot. It's ___ robot. | my | your, his | I → my.
g Is this ___ ball, Sam? | your | my, her | Talking to Sam: your.
g Mum has got a hat. It's ___ hat. | her | his, my | Mum: her.
g Dad has got a puzzle. It's ___ puzzle. | his | her, your | Dad: his.
g We have got a kite. It's ___ kite. | our | my, their | We → our.
T The toy box | text
> Leo and his sister Noor open the toy box.
> ‘Here is my robot!’ says Leo. His robot can walk and talk.
> ‘Here is my puzzle!’ says Noor. Her puzzle has got a hundred pieces.
> ‘Where is our ball?’ asks Leo. It is under the box!
> They play with the ball in the garden.
q Who is Leo's sister? | Noor | Lina, Mia | his sister Noor
q What can Leo's robot do? | walk and talk | fly and swim, jump and sing | His robot can walk and talk.
q How many pieces has the puzzle got? | a hundred | ten, fifty | a hundred pieces
q Where is the ball? | under the box | in the box, on the bed | It is under the box!
q Where do they play with the ball? | in the garden | in the kitchen, at school | in the garden
t The puzzle is Leo's. | F | It is Noor's (her puzzle).
t The robot can talk. | T | His robot can walk and talk.
t They play in the garden. | T | They play with the ball in the garden.
o This is my robot.
o Her puzzle is big.
o Where is our ball?
s puzzle | puzle, puzzel
s robot | robbot, robut
s train | trane, trein
s sister | sistar, sisster
s hundred | hundrid, hunderd
"""),
"""
L 6.2 | Let's play a game! | Follow and give simple instructions.
W jump | push off the ground with your legs | 🦘
W run | move very fast on your legs | 🏃
W throw | send something through the air with your hand | 🤾
W catch | take something that is flying in the air | 🧤
W turn | it is your time to play | 🔄
W win | be the best in a game | 🏆
G Instructions | Instructions start with a doing word (verb). We use ‘Let's’ to make a suggestion. | Throw the ball. / Let's play!
g ___ the ball to me! | Throw | Throws, Throwing | Instructions start with the verb.
g ___ play a game! | Let's | Lets, Let | Let's = let us.
g ___ three times. | Jump | Jumps, Jumped | Start with the verb.
g Don't ___! Walk, please. | run | runs, running | Don't + verb.
g ___ the ball with two hands. | Catch | Catches, Catching | Start with the verb.
g It's your turn. ___ the dice. | Roll | Rolls, Rolling | Start with the verb.
g ___ go to the playground! | Let's | Lets, Let us to | Let's go…
T How to play ‘Animal Statues’ | instructions
> You need: music and three or more friends.
> 1. Play some music.
> 2. Dance like an animal – a monkey, a frog or a bird!
> 3. When the music stops, stop! Be a statue.
> 4. Don't move! If you move, you are out.
> 5. The last player in the game is the winner.
q What do you need? | music and friends | a ball and a bat, a kite | music and three or more friends
q How do you dance? | like an animal | like a robot, very slowly | Dance like an animal.
q What do you do when the music stops? | stop and be a statue | jump, run away | When the music stops, stop!
q What happens if you move? | You are out. | You win., You dance again. | If you move, you are out.
q Who is the winner? | the last player in the game | the first player, the fastest runner | The last player is the winner.
t You need a ball for this game. | F | You need music and friends.
t You must not move when the music stops. | T | Don't move!
t You can dance like a frog. | T | a monkey, a frog or a bird
o Let's play a game.
o Throw the ball to me.
o Don't move!
s music | musik, musick
s dance | danse, dans
s winner | winer, winnor
s statue | stachoo, statu
s friends | freinds, frends
"""),
]
