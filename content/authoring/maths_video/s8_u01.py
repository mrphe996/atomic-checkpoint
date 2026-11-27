# -*- coding: utf-8 -*-
"""Stage 8 · Unit 1 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

INK = "#1F2A37"


def TREE(root, x=700, y=130, w=520, at=0):
    """a factor tree: root = ("252", child, child) with leaves ("2",); leaves (the primes) are circled in green"""
    leaves, pos, edges = [], {}, []
    def walk(n, d, path):
        if len(n) == 1: leaves.append(path); pos[path] = [len(leaves) - 1, d]; return pos[path][0]
        a = walk(n[1], d + 1, path + "0"); b = walk(n[2], d + 1, path + "1"); pos[path] = [(a + b) / 2, d]; edges.extend([(path, path + "0"), (path, path + "1")]); return pos[path][0]
    walk(root, 0, "r")
    depth = max(d for _, d in pos.values()); W = 560; H = 90 + 110 * depth
    px = lambda p: 50 + pos[p][0] * (W - 100) / max(1, len(leaves) - 1); py = lambda p: 50 + 110 * pos[p][1]
    lab = {}
    def names(n, path): lab[path] = n[0]; [names(c, path + k) for k, c in zip("01", n[1:])]
    names(root, "r")
    svg = "".join(f'<line x1="{px(a):.0f}" y1="{py(a) + 22}" x2="{px(b):.0f}" y2="{py(b) - 24}" stroke="{INK}" stroke-width="3"/>' for a, b in edges)
    for p in pos:
        leaf = p in leaves
        if leaf: svg += f'<circle cx="{px(p):.0f}" cy="{py(p)}" r="28" fill="#E3F6EC" stroke="{GREEN}" stroke-width="3.5"/>'
        svg += f'<text x="{px(p):.0f}" y="{py(p) + 11}" font-size="32" font-weight="700" text-anchor="middle" fill="{GREEN if leaf else INK}">{lab[p]}</text>'
    return T(f'<svg viewBox="0 0 {W} {H}" width="{w}" height="{w * H / W:.0f}">{svg}</svg>', x=x, y=y, at=at)


VIDEOS = {}

VIDEOS["1.1"] = [
    dict(kind="hook", title="Secret codes", steps=[
        dict(say="When you pay for something online, your card details are locked with a secret code. The lock is built from two very large prime numbers.",
             do=[E("🔐", 90, 170, 100), T("online codes use **two big primes**", x=230, y=200)]),
        dict(say="Multiplying the two primes is easy for a computer. But going backwards, and finding the two primes from the answer, is extremely hard. That keeps the code safe.",
             do=[T("multiply: **easy** · split back into primes: **very hard**", x=230, y=300)]),
        dict(say="Let's try a small one. 91 is made by multiplying two primes.", do=[B("91 = ? × ?", x=230, y=400, color=BLUE)]),
        PAUSE("1.1-k1", "Which two primes multiply to make 91? Pause the video and work it out.", "Which two primes multiply to make 91?"),
    ]),
    dict(kind="hook", title="Cracking 91", steps=[
        dict(say="Try the primes in order. 91 is odd, so 2 does not work. 9 plus 1 is 10, so 3 does not work. It does not end in 0 or 5, so 5 does not work.",
             do=TEST([("÷ 2", False), ("÷ 3", False), ("÷ 5", False), ("÷ 7", True)], 220, t0=0.6, gap=2.4)),
        dict(say="7 works. 91 divided by 7 is 13. So 91 equals 7 times 13. Both are prime.", do=[MATH("91 = 7 × 13", x=110, y=330, color=GREEN)]),
    ]),
    dict(kind="recall", title="Primes, HCF and LCM", steps=[
        dict(say="Remember: a prime number has exactly two factors, 1 and itself. 2, 3, 5, 7, 11 and 13 are prime. 1 is not prime, because it has only one factor.",
             do=[B("prime: exactly 2 factors", x=80, y=170), T("2, 3, 5, 7, 11, 13, 17, 19 … (1 is **not** prime)", x=80, y=270)]),
        dict(say="The highest common factor, or H C F, is the biggest number that divides into both numbers. The lowest common multiple, or L C M, is the smallest number that both divide into.",
             do=[T("**HCF**: biggest number that divides **into** both", x=80, y=370), T("**LCM**: smallest number both divide **into**", x=80, y=450, at=5)]),
    ]),
    dict(kind="idea", title="Products of prime factors", steps=[
        dict(say="Every whole number bigger than 1 is either prime, or it can be written as primes multiplied together. And there is only one way to do it.",
             do=[B("every number = a product of primes", x=80, y=170)]),
        dict(say="A factor tree finds them. Take 252. Split it into any factor pair, say 4 times 63.", do=[TREE(("252", ("4", ("2",), ("2",)), ("63", ("7",), ("9", ("3",), ("3",)))), y=215, at=0.3)]),
        dict(say="Keep splitting until every branch ends in a prime. 4 is 2 times 2. 63 is 7 times 9, and 9 is 3 times 3. The primes are circled.",
             do=[T("stop when every branch is **prime**", x=80, y=270)]),
        dict(say="Multiply them together and write it in index form. 252 equals 2 squared, times 3 squared, times 7.",
             do=[MATH("252 = 2 × 2 × 3 × 3 × 7", x=80, y=360), MATH("= 2² × 3² × 7", x=80, y=440, color=GREEN, at=3.6)]),
        PAUSE("1.1-k2", "Your turn. Write 100 as a product of primes, in index form. Pause the video and try it.", "Write 100 as a product of primes in index form."),
    ]),
    dict(kind="idea", title="Check: 100", steps=[
        dict(say="100 is 10 times 10, and each 10 is 2 times 5. That makes two 2s and two 5s. So 100 equals 2 squared, times 5 squared.",
             do=[TREE(("100", ("10", ("2",), ("5",)), ("10", ("2",), ("5",)))), MATH("100 = 2² × 5²", x=80, y=240, color=GREEN, at=5)]),
    ]),
    dict(kind="idea", title="HCF and LCM from the primes", steps=[
        dict(say="Prime factors make H C F and L C M quick. Look at 84 and 90. 84 is 2 squared, times 3, times 7. 90 is 2, times 3 squared, times 5.",
             do=[MATH("84 = 2² × 3 × 7", x=80, y=170), MATH("90 = 2 × 3² × 5", x=80, y=250)]),
        dict(say="For the H C F, take only the primes in both numbers, using the lower power. They share a 2 and a 3. So the H C F is 2 times 3, which is 6.",
             do=[TBL(["", "Rule", "84 and 90"], [["HCF", "primes in BOTH, lower power", "2 × 3 = 6"], ["LCM", "EVERY prime, higher power", "2² × 3² × 5 × 7 = 1260"]], y=340), ROW(0, at=0.4)]),
        dict(say="For the L C M, take every prime, using the higher power. 2 squared, times 3 squared, times 5, times 7, is 1,260.", do=[ROW(1, at=0.3)]),
    ]),
    dict(kind="method", title="How do I find the HCF and LCM?", steps=[
        dict(say="Here is the method. Step 1: write each number as a product of prime factors.", do=[T("1. Write each number as a product of **primes**", x=80, y=170)]),
        dict(say="Step 2: for the H C F, multiply the primes they share, using the lower power of each.", do=[T("2. **HCF**: shared primes, **lower** power", x=80, y=260)]),
        dict(say="Step 3: for the L C M, multiply every prime that appears, using the higher power of each.", do=[T("3. **LCM**: every prime, **higher** power", x=80, y=350)]),
        dict(say="Step 4: check. The H C F times the L C M equals the two numbers multiplied together.", do=[T("4. Check: HCF × LCM = the two numbers multiplied", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="HCF and LCM of 60 and 126", steps=[
        dict(say="Find the H C F and L C M of 60 and 126. 60 is 2 squared, times 3, times 5. 126 is 2, times 3 squared, times 7.",
             do=[MATH("60 = 2² × 3 × 5", x=80, y=170), MATH("126 = 2 × 3² × 7", x=80, y=250, at=4)]),
        dict(say="They share 2 and 3. The lower powers give 2 times 3. The H C F is 6.", do=[MATH("HCF = 2 × 3 = 6", x=80, y=350, color=GREEN)]),
        dict(say="Every prime with the higher power: 2 squared, times 3 squared, times 5, times 7. The L C M is 1,260.", do=[MATH("LCM = 2² × 3² × 5 × 7 = 1260", x=80, y=440, color=GREEN)]),
    ]),
    dict(kind="example", title="Straight from index form", steps=[
        dict(say="Sometimes the numbers are already in index form. A is 2 cubed, times 5 squared, times 7. B is 2, times 5 cubed, times 11. Find the H C F.",
             do=[MATH("A = 2³ × 5² × 7", x=80, y=170), MATH("B = 2 × 5³ × 11", x=80, y=250)]),
        dict(say="The shared primes are 2 and 5. The lower powers are 2 to the power 1, and 5 squared. 2 times 25 is 50.",
             do=[T("shared: **2** and **5** · lower powers: 2¹ and 5²", x=80, y=350), B("HCF = 2 × 25 = 50", x=80, y=440, color=GREEN, at=5)]),
        PAUSE("1.1-k3", "Your turn. Find the H C F of 2 squared, times 3, times 7, and 2, times 3 squared, times 7. Pause and work it out.", "HCF of 2² × 3 × 7 and 2 × 3² × 7?"),
    ]),
    dict(kind="example", title="Check: the HCF", steps=[
        dict(say="All three primes are shared: 2, 3 and 7. The lower powers are 2, 3 and 7. 2 times 3 times 7 is 42.",
             do=[MATH("2² × 3 × 7 and 2 × 3² × 7", x=80, y=180), MATH("HCF = 2 × 3 × 7 = 42", x=80, y=280, color=GREEN, at=3.4)]),
    ]),
    dict(kind="example", title="Two lighthouses", steps=[
        dict(say="One lighthouse flashes every 18 seconds. Another flashes every 24 seconds. They flash together at midnight. When do they next flash together?",
             do=[E("🗼", 90, 170, 100), T("flashes every **18 s** and every **24 s**", x=230, y=200)]),
        dict(say="We need the L C M of 18 and 24. 18 is 2 times 3 squared. 24 is 2 cubed times 3.", do=[MATH("18 = 2 × 3²", x=230, y=300), MATH("24 = 2³ × 3", x=600, y=300, at=2.6)]),
        dict(say="The higher powers give 2 cubed times 3 squared, which is 72. They flash together again after 72 seconds.",
             do=[MATH("LCM = 2³ × 3² = 72", x=230, y=390), B("72 seconds", x=230, y=480, color=GREEN, at=3.8)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Zara finds the H C F of 2 cubed, times 3, times 5 squared, and 2 squared, times 3 cubed. Which line goes wrong first?",
             do=LINES("Zara", "the HCF of 2³ × 3 × 5² and 2² × 3³", ["Shared primes: 2 and 3", "Use the higher powers: 2³ × 3³", "HCF = 216"])),
        dict(say="Line 2 is wrong. For the H C F, use the lower power of each shared prime. The higher powers are for the L C M.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="The lower powers are 2 squared and 3. So the H C F is 4 times 3, which is 12.", do=[B("HCF = 2² × 3 = 12", x=110, y=480, color=GREEN)]),
    ]),
    dict(kind="life", title="Cicadas", steps=[
        dict(say="Some cicadas in North America live underground for years, then all come out together. One kind comes out every 13 years, another every 17 years.",
             do=[E("🦗", 90, 170, 100), T("cicadas appear every **13** or **17** years", x=230, y=200)]),
        dict(say="13 and 17 are both prime, so their L C M is 13 times 17, which is 221. The two kinds come out in the same year only once every 221 years.",
             do=[MATH("LCM = 13 × 17 = 221", x=230, y=310, color=BLUE)]),
        dict(say="Scientists think prime cycles help the cicadas avoid predators that come and go in shorter cycles.", do=[T("a **prime** cycle rarely lines up with a predator's", x=230, y=420)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("1.1-k4", "One last question. What is the H C F times the L C M of 12 and 18? Pause the video and answer.", "HCF × LCM of 12 and 18 = ?"),
        dict(say="The H C F times the L C M always equals the two numbers multiplied. 12 times 18 is 216. Check: the H C F is 6, the L C M is 36, and 6 times 36 is 216.",
             do=[MATH("12 × 18 = 216", x=80, y=190, color=GREEN), MATH("HCF 6 × LCM 36 = 216", x=80, y=290, at=6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: every whole number bigger than 1 has just one product of prime factors.", do=[T("• Every number > 1 has **one** product of primes", x=80, y=170)]),
        dict(say="Use a factor tree, and write the answer in index form.", do=[T("• Factor tree → index form, like 2² × 3² × 7", x=80, y=250)]),
        dict(say="H C F: the shared primes, with the lower powers. L C M: all the primes, with the higher powers.", do=[T("• HCF: shared primes, lower powers · LCM: all primes, higher powers", x=80, y=330)]),
        dict(say="And the H C F times the L C M equals the two numbers multiplied together.", do=[T("• HCF × LCM = the two numbers multiplied", x=80, y=410)]),
    ]),
]

VIDEOS["1.2"] = [
    dict(kind="hook", title="Falling temperatures", steps=[
        dict(say="Overnight, the temperature on a mountain falls by 3 degrees every hour, for 6 hours. A scientist writes this as 6 times negative 3.",
             do=[E("🏔️", 90, 170, 100), T("falls **3 °C** every hour for **6 hours**", x=230, y=200), MATH("6 × (−3)", x=230, y=300, color=BLUE)]),
        PAUSE("1.2-k1", "What is 6 times negative 3? Pause the video and work it out.", "6 × (−3) = ?"),
    ]),
    dict(kind="hook", title="Six drops of 3", steps=[
        dict(say="Six drops of 3 degrees is a drop of 18 degrees. So 6 times negative 3 is negative 18.",
             do=[MATH("(−3) + (−3) + (−3) + (−3) + (−3) + (−3)", x=80, y=190), MATH("6 × (−3) = −18", x=80, y=290, color=GREEN, at=3)]),
        dict(say="But what could negative 3 times negative 6 mean? Can a negative times a negative ever be positive? Let's find out.", do=[B("(−3) × (−6) = ?", x=80, y=400, color=BLUE)]),
    ]),
    dict(kind="recall", title="Negative times positive", steps=[
        dict(say="Remember: 4 times negative 5 means four lots of negative 5. That is negative 20.", do=[MATH("4 × (−5) = −20", x=80, y=180)]),
        dict(say="And negative 7 times 6 is negative 42. A positive and a negative always give a negative answer.", do=[MATH("(−7) × 6 = −42", x=80, y=280), T("one negative → **negative**", x=80, y=380, color=RED)]),
    ]),
    dict(kind="idea", title="Why negative times negative is positive", steps=[
        dict(say="Look at this pattern. Each time, the first number goes down by 1.",
             do=[TBL(["Calculation", "Answer"], [["3 × (−4)", "−12"], ["2 × (−4)", "−8"], ["1 × (−4)", "−4"], ["0 × (−4)", "0"], ["(−1) × (−4)", "4"], ["(−2) × (−4)", "8"]], x=80, y=150), ROW(0, 0.3), ROW(1, 1.2), ROW(2, 2.1)]),
        dict(say="The answers go up by 4 each time. Negative 12, negative 8, negative 4, then 0.", do=[ROW(3, 0.3), T("answers go **up by 4**", x=720, y=300, color=BLUE)]),
        dict(say="Keep the pattern going. Negative 1 times negative 4 is 4. Negative 2 times negative 4 is 8. A negative times a negative is positive.",
             do=[ROW(4, 1.5), ROW(5, 3.4), B("− × − = +", x=720, y=420, color=GREEN, at=5)]),
        PAUSE("1.2-k2", "Your turn. What is negative 9 times negative 4? Pause the video and try it.", "(−9) × (−4) = ?"),
    ]),
    dict(kind="idea", title="Check: (−9) × (−4)", steps=[
        dict(say="9 times 4 is 36. The signs are the same, so the answer is positive. Negative 9 times negative 4 is 36.",
             do=[MATH("9 × 4 = 36", x=80, y=190), MATH("(−9) × (−4) = 36", x=80, y=290, color=GREEN, at=2.4)]),
    ]),
    dict(kind="idea", title="Sign rules", steps=[
        dict(say="The same sign rules work for dividing. Same signs give a positive answer. Different signs give a negative answer.",
             do=[TBL(["Signs", "Answer"], [["+ × +  or  − × −", "positive"], ["+ × −  or  − × +", "negative"]], y=160), ROW(0, 0.3), ROW(1, 2.4)]),
        dict(say="For longer calculations, the order of operations stays the same: brackets first, then indices, or powers, then times and divide, then add and subtract.",
             do=[T("Order: **brackets**, **indices**, × ÷, + −", x=80, y=380)]),
    ]),
    dict(kind="method", title="How do I multiply and divide integers?", steps=[
        dict(say="Here is the method. Step 1: work out the size of the answer, ignoring the signs.", do=[T("1. Work out the **size**, ignoring signs", x=80, y=170)]),
        dict(say="Step 2: same signs give a positive answer. Different signs give a negative answer.", do=[T("2. **Same** signs → +  ·  **different** signs → −", x=80, y=260)]),
        dict(say="Step 3: for longer calculations, follow the order of operations.", do=[T("3. Brackets, indices, × ÷, + −", x=80, y=350)]),
        dict(say="Step 4: when you multiply several numbers, count the negatives. An even number of negatives gives a positive answer. An odd number gives a negative.",
             do=[T("4. Count the negatives: **even** → +, **odd** → −", x=80, y=440), E("✅", 1100, 410, 90, at=3)]),
    ]),
    dict(kind="example", title="Dividing", steps=[
        dict(say="Work out negative 56 divided by negative 8, and 56 divided by negative 8.", do=[MATH("(−56) ÷ (−8)", x=80, y=170), MATH("56 ÷ (−8)", x=600, y=170)]),
        dict(say="56 divided by 8 is 7. In the first one, the signs are the same, so the answer is 7.", do=[MATH("= 7", x=80, y=270, color=GREEN)]),
        dict(say="In the second one, the signs are different, so the answer is negative 7.", do=[MATH("= −7", x=600, y=270, color=GREEN)]),
    ]),
    dict(kind="example", title="Three negatives", steps=[
        dict(say="Work out negative 2, times negative 3, times negative 5.", do=[MATH("(−2) × (−3) × (−5)", x=80, y=170)]),
        dict(say="Negative 2 times negative 3 is 6. Then 6 times negative 5 is negative 30.", do=[MATH("(−2) × (−3) = 6", x=80, y=270), MATH("6 × (−5) = −30", x=80, y=350, at=2.6, color=GREEN)]),
        dict(say="Check by counting: there are 3 negatives. 3 is odd, so the answer is negative.", do=[T("3 negatives → odd → **negative** ✓", x=80, y=450)]),
    ]),
    dict(kind="example", title="A power of a negative", steps=[
        dict(say="Work out 4, minus 3 times negative 2 squared. Indices come first. Negative 2 squared is negative 2 times negative 2, which is 4.",
             do=[MATH("4 − 3 × (−2)²", x=80, y=170), MATH("(−2)² = (−2) × (−2) = 4", x=80, y=260, at=4)]),
        dict(say="Then multiply. 3 times 4 is 12. Finally, 4 minus 12 is negative 8.", do=[MATH("4 − 3 × 4 = 4 − 12", x=80, y=350), B("= −8", x=80, y=440, color=GREEN, at=3)]),
        PAUSE("1.2-k3", "Your turn. What is negative 2 cubed? Pause and work it out.", "(−2)³ = ?"),
    ]),
    dict(kind="example", title="Check: (−2)³", steps=[
        dict(say="Negative 2 cubed is negative 2, times negative 2, times negative 2. That is 4 times negative 2, which is negative 8. Three negatives give a negative.",
             do=[MATH("(−2) × (−2) × (−2)", x=80, y=190), MATH("= 4 × (−2) = −8", x=80, y=280, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="Substituting", steps=[
        dict(say="Find the value of 2 A squared, minus 3 B, when A is negative 4 and B is negative 5.", do=[MATH("2a² − 3b,  a = −4,  b = −5", x=80, y=170)]),
        dict(say="A squared is negative 4 squared, which is 16. 2 times 16 is 32.", do=[MATH("2 × (−4)² = 2 × 16 = 32", x=80, y=260)]),
        dict(say="3 B is 3 times negative 5, which is negative 15. Then 32 minus negative 15 is 32 plus 15, which is 47.",
             do=[MATH("3 × (−5) = −15", x=80, y=340), MATH("32 − (−15) = 47", x=80, y=420, color=GREEN, at=4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Omar works out negative 5 squared, written without brackets, and negative 5 in brackets, squared. Which line is wrong?",
             do=LINES("Omar", "−5² and (−5)²", ["−5² = (−5) × (−5) = 25", "(−5)² = 25"])),
        dict(say="Line 1 is wrong. Without brackets, only the 5 is squared. The minus sign stays outside.", do=[dict(a="cross", id="l1")]),
        dict(say="So negative 5 squared, without brackets, is negative 25. With brackets, it is 25.", do=[B("−5² = −(5 × 5) = −25", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Below sea level", steps=[
        dict(say="Negative numbers describe heights below sea level. The shore of the Dead Sea is about 430 metres below sea level. We can write that as negative 430 metres.",
             do=[E("🌊", 90, 170, 100), T("Dead Sea shore: about **−430 m**", x=230, y=200)]),
        dict(say="A diver who goes down 12 metres a minute for 5 minutes changes depth by 5 times negative 12, which is negative 60 metres.",
             do=[E("🤿", 90, 320, 100), MATH("5 × (−12) = −60 m", x=230, y=350, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("1.2-k4", "One last question. What is 20 divided by negative 4, minus negative 3? Pause the video and answer.", "20 ÷ (−4) − (−3) = ?"),
        dict(say="Divide first. 20 divided by negative 4 is negative 5. Then negative 5 minus negative 3 is negative 5 plus 3, which is negative 2.",
             do=[MATH("20 ÷ (−4) = −5", x=80, y=190), MATH("−5 − (−3) = −5 + 3 = −2", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: when you multiply or divide, same signs give a positive answer, and different signs give a negative answer.", do=[T("• Same signs → **+** · different signs → **−**", x=80, y=170)]),
        dict(say="The pattern explains why a negative times a negative is positive.", do=[T("• The pattern shows why − × − = +", x=80, y=250)]),
        dict(say="Use the order of operations: brackets, indices, times and divide, add and subtract.", do=[T("• Brackets, indices, × ÷, + −", x=80, y=330)]),
        dict(say="Negative 5 in brackets, squared, is positive. Negative 5 squared, without brackets, is negative.", do=[T("• (−5)² = 25 but −5² = −25", x=80, y=410)]),
    ]),
]

SQR = lambda n, side, x, y, at=0, c=BLUE: T(f'<span style="display:inline-flex;align-items:center;justify-content:center;width:{side}px;height:{side}px;border:5px solid {c};background:#DCE8FF;border-radius:6px;font-weight:700">{n}</span>', x=x, y=y, at=at)

VIDEOS["1.3"] = [
    dict(kind="hook", title="A square garden", steps=[
        dict(say="A square vegetable patch has an area of 50 square metres. The gardener wants to put a fence along one side. How long is one side?",
             do=[E("🥕", 90, 170, 100), T("a square patch with area **50 m²**", x=230, y=200), SQR("50 m²", 240, 900, 140, at=1)]),
        dict(say="Is it 7 metres? 8 metres? Or somewhere in between?", do=[T("side: **7 m**? **8 m**? in between?", x=230, y=300)]),
        PAUSE("1.3-k1", "How long is the side of a 50 square metre square? Pause the video and decide.", "The side of a 50 m² square is …"),
    ]),
    dict(kind="hook", title="Between 7 and 8", steps=[
        dict(say="A 7 metre square has an area of 49. An 8 metre square has an area of 64. 50 is between them, so the side is between 7 metres and 8 metres.",
             do=[MATH("7² = 49", x=80, y=190), MATH("8² = 64", x=80, y=270), MATH("49 < 50 < 64", x=80, y=360, color=BLUE, at=4)]),
        dict(say="50 is very close to 49, so the side is just over 7 metres. In fact it is about 7.1 metres.", do=[B("side ≈ 7.1 m", x=80, y=460, color=GREEN)]),
    ]),
    dict(kind="recall", title="Squares and cubes", steps=[
        dict(say="Remember: 5 squared is 5 times 5, which is 25. 4 cubed is 4 times 4 times 4, which is 64.", do=[MATH("5² = 25", x=80, y=180), MATH("4³ = 64", x=400, y=180)]),
        dict(say="A square root undoes squaring. The square root of 25 is 5. A cube root undoes cubing. The cube root of 64 is 4.",
             do=[MATH("√25 = 5", x=80, y=290), MATH("∛64 = 4", x=400, y=290, at=3.6)]),
    ]),
    dict(kind="idea", title="Two square roots", steps=[
        dict(say="5 squared is 25. But negative 5 squared is also 25. So 25 has two square roots: 5 and negative 5. We write plus or minus 5.",
             do=[MATH("5² = 25", x=80, y=170), MATH("(−5)² = 25", x=400, y=170), B("roots of 25: ±5", x=80, y=270, color=BLUE, at=6)]),
        dict(say="The square root symbol on its own means the positive root. The square root of 25 is just 5. For a length, only the positive root makes sense.",
             do=[MATH("√25 = 5", x=80, y=380), T("√ means the **positive** root", x=420, y=388)]),
        dict(say="A cube root is different. Every number has exactly one cube root. Negative 3 cubed is negative 27, so the cube root of negative 27 is negative 3.",
             do=[MATH("∛(−27) = −3", x=80, y=470, color=GREEN), T("one cube root, **same sign**", x=420, y=478)]),
        PAUSE("1.3-k2", "Your turn. Write down the square roots of 144. Pause the video and try it.", "Write the square roots of 144."),
    ]),
    dict(kind="idea", title="Check: roots of 144", steps=[
        dict(say="12 squared is 144, and negative 12 squared is also 144. So the square roots of 144 are plus or minus 12.",
             do=[MATH("12² = 144 and (−12)² = 144", x=80, y=190), B("±12", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="idea", title="Estimating a root", steps=[
        dict(say="To estimate a square root, find the square numbers either side. For the square root of 90: 81 is less than 90, and 90 is less than 100.",
             do=[MATH("81 < 90 < 100", x=80, y=170)]),
        dict(say="So the square root of 90 is between 9 and 10.", do=[MATH("9 < √90 < 10", x=80, y=260, color=BLUE)]),
        dict(say="Numbers come in sets. Natural numbers are 1, 2, 3 and so on. Integers also include 0 and the negatives. Rational numbers are any numbers that can be written as a fraction.",
             do=[T("**natural**: 1, 2, 3 … · **integers**: … −2, −1, 0, 1, 2 …", x=80, y=360), T("**rational**: can be written as a fraction", x=80, y=440, at=6)]),
    ]),
    dict(kind="method", title="How do I find or estimate a root?", steps=[
        dict(say="Here is the method. Step 1: know your squares up to 15 squared, and your cubes up to 5 cubed, and 10 cubed.", do=[T("1. Know squares to **15²**, cubes to **5³** and **10³**", x=80, y=170)]),
        dict(say="Step 2: x squared equals a number has two roots, plus and minus. x cubed equals a number has one root, with the same sign.", do=[T("2. x² = n → **±√n** · x³ = n → **one** root", x=80, y=260)]),
        dict(say="Step 3: to estimate, find the square numbers either side, then decide which one it is closer to.", do=[T("3. Estimate: squares **either side**, which is closer?", x=80, y=350)]),
        dict(say="Step 4: check by squaring, or cubing, your answer.", do=[T("4. **Check**: square or cube your answer", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A negative cube root", steps=[
        dict(say="Find the cube root of negative 125. 5 cubed is 125. So negative 5 cubed is negative 125.",
             do=[MATH("5³ = 125", x=80, y=180), MATH("(−5)³ = −125", x=80, y=270, at=3)]),
        dict(say="The cube root of negative 125 is negative 5.", do=[B("∛(−125) = −5", x=80, y=380, color=GREEN)]),
        PAUSE("1.3-k3", "Your turn. What is the cube root of negative 8? Pause and work it out.", "∛(−8) = ?"),
    ]),
    dict(kind="example", title="Check: ∛(−8)", steps=[
        dict(say="2 cubed is 8, so negative 2 cubed is negative 8. The cube root of negative 8 is negative 2.",
             do=[MATH("(−2)³ = −8", x=80, y=190), B("∛(−8) = −2", x=80, y=290, color=GREEN, at=2.6)]),
    ]),
    dict(kind="example", title="Estimating √90", steps=[
        dict(say="Estimate the square root of 90, to 1 decimal place. We know it is between 9 and 10.", do=[MATH("9 < √90 < 10", x=80, y=170)]),
        dict(say="Try 9.5. 9.5 squared is 90.25. That is just above 90. Now try 9.4. 9.4 squared is 88.36, which is below.",
             do=[MATH("9.5² = 90.25", x=80, y=260), MATH("9.4² = 88.36", x=80, y=340, at=4.6)]),
        dict(say="90 is much closer to 90.25. So the square root of 90 is about 9.5.", do=[B("√90 ≈ 9.5", x=80, y=440, color=GREEN)]),
    ]),
    dict(kind="example", title="Solving x² + 7 = 56", steps=[
        dict(say="Solve x squared plus 7 equals 56. Subtract 7 from both sides. x squared equals 49.", do=[MATH("x² + 7 = 56", x=80, y=170), MATH("x² = 49", x=80, y=260, at=3)]),
        dict(say="There are two square roots. x equals 7, or x equals negative 7.", do=[B("x = 7 or x = −7", x=80, y=370, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ben solves x squared equals 36. Which line is wrong?", do=LINES("Ben", "x² = 36", ["x = √36", "x = 6"])),
        dict(say="Line 2 is not finished. Negative 6 squared is 36 as well, so there are two solutions.", do=[dict(a="cross", id="l2")]),
        dict(say="x equals 6, or x equals negative 6.", do=[B("x = 6 or x = −6", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Screen sizes", steps=[
        dict(say="Square roots are used to measure screens. A television's size is the length of its diagonal, across from corner to corner.",
             do=[E("📺", 90, 170, 100), T("screen size = the **diagonal**", x=230, y=200)]),
        dict(say="The diagonal is found by adding the squares of the width and the height, then taking the square root. A screen 48 inches wide and 27 inches high has a diagonal of about 55 inches.",
             do=[MATH("√(48² + 27²) = √3033 ≈ 55", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("1.3-k4", "One last question. Which is closest to the square root of 70: 8.4, 8.9, or 35? Pause the video and answer.", "√70 is closest to …"),
        dict(say="64 is less than 70, and 70 is less than 81, so the root is between 8 and 9. 8.4 squared is 70.56, very close to 70. The answer is 8.4.",
             do=[MATH("64 < 70 < 81", x=80, y=190), MATH("8.4² = 70.56", x=80, y=280, at=4), B("√70 ≈ 8.4", x=80, y=380, color=GREEN, at=6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a positive number has two square roots, plus and minus. The square root symbol alone means the positive one.", do=[T("• Two square roots: **±√n**; √ alone is the positive one", x=80, y=170)]),
        dict(say="Every number has exactly one cube root. The cube root of a negative number is negative.", do=[T("• One cube root; ∛ of a negative is **negative**", x=80, y=250)]),
        dict(say="Estimate a root using the squares, or cubes, either side.", do=[T("• Estimate with the squares either side", x=80, y=330)]),
        dict(say="Natural numbers, integers and rational numbers are sets of numbers, each one inside the next.", do=[T("• natural ⊂ integers ⊂ rational", x=80, y=410)]),
    ]),
]

VIDEOS["1.4"] = [
    dict(kind="hook", title="Doubling bacteria", steps=[
        dict(say="A colony of bacteria doubles every hour. It starts with 1 cell. After 1 hour there are 2 cells, after 2 hours 4, after 3 hours 8.",
             do=[E("🦠", 90, 170, 100), T("doubles **every hour**: 1, 2, 4, 8 …", x=230, y=200)]),
        dict(say="After 10 hours, there are 2 to the power 10 cells.", do=[B("after 10 hours: 2¹⁰ cells", x=230, y=300, color=BLUE)]),
        PAUSE("1.4-k1", "What is 2 to the power 10? Pause the video and work it out.", "2¹⁰ = ?"),
    ]),
    dict(kind="hook", title="2¹⁰", steps=[
        dict(say="Keep doubling: 16, 32, 64, 128, 256, 512, and 1,024. 2 to the power 10 is 1,024.", do=[T("16, 32, 64, 128, 256, 512, **1024**", x=80, y=190), B("2¹⁰ = 1024", x=80, y=290, color=GREEN, at=5)]),
        dict(say="After 5 more hours, the cells double another 5 times. That is 2 to the power 10, times 2 to the power 5. Can we write it as one power of 2?",
             do=[MATH("2¹⁰ × 2⁵ = 2<sup>?</sup>", x=80, y=400)]),
    ]),
    dict(kind="recall", title="Powers", steps=[
        dict(say="Remember: 3 to the power 4 means 3 times 3 times 3 times 3. That is 81. The small raised number is called the index, or the power.",
             do=[MATH("3⁴ = 3 × 3 × 3 × 3 = 81", x=80, y=180), T("the small number is the **index**", x=80, y=280, at=5)]),
        dict(say="2 to the power 5 is 2 times 2 times 2 times 2 times 2, which is 32.", do=[MATH("2⁵ = 32", x=80, y=380)]),
    ]),
    dict(kind="idea", title="Multiplying and dividing powers", steps=[
        dict(say="5 cubed times 5 squared is three 5s times two 5s. That is five 5s, so 5 to the power 5. When you multiply, the indices add. So for the bacteria, 2 to the power 10, times 2 to the power 5, is 2 to the power 15.",
             do=[MATH("5³ × 5² = (5 × 5 × 5) × (5 × 5) = 5⁵", x=80, y=170), T("multiply → **add** the indices", x=80, y=260, color=BLUE, at=6), MATH("2¹⁰ × 2⁵ = 2¹⁵", x=700, y=252, color=GREEN, at=8)]),
        dict(say="5 to the power 6, divided by 5 squared. Two of the six 5s cancel, which leaves four. So the answer is 5 to the power 4. When you divide, the indices subtract.",
             do=[MATH("5⁶ ÷ 5² = 5⁴", x=80, y=350), T("divide → **subtract** the indices", x=80, y=440, color=BLUE, at=6)]),
        PAUSE("1.4-k2", "Your turn. Simplify 10 to the power 4, times 10 cubed. Pause the video and try it.", "Simplify 10⁴ × 10³."),
    ]),
    dict(kind="idea", title="Check: 10⁴ × 10³", steps=[
        dict(say="Multiplying, so add the indices. 4 plus 3 is 7. The answer is 10 to the power 7, which is 10 million.",
             do=[MATH("10⁴ × 10³ = 10⁴⁺³ = 10⁷", x=80, y=190, color=GREEN), T("= 10 000 000", x=80, y=290, at=4)]),
    ]),
    dict(kind="idea", title="The zero index", steps=[
        dict(say="Look at this pattern. 5 cubed is 125. 5 squared is 25. 5 to the power 1 is 5. Each time, we divide by 5.",
             do=[TBL(["Power", "5³", "5²", "5¹", "5⁰"], [["Value", "125", "25", "5", "1"]], y=160), ROW(0, 1)]),
        dict(say="One more step: 5 divided by 5 is 1. So 5 to the power 0 is 1.", do=[B("5⁰ = 1", x=80, y=300, color=GREEN)]),
        dict(say="Another way to see it: 5 cubed divided by 5 cubed is 5 to the power 0. And any number divided by itself is 1. So any number, except 0, to the power 0 is 1.",
             do=[MATH("5³ ÷ 5³ = 5⁰ = 1", x=80, y=400), T("a⁰ = 1 (a ≠ 0)", x=80, y=480, color=BLUE, at=6)]),
    ]),
    dict(kind="method", title="How do I simplify powers?", steps=[
        dict(say="Here is the method. Step 1: check that the bases are the same. The rules only work for the same base.", do=[T("1. Check the **bases** are the same", x=80, y=170)]),
        dict(say="Step 2: when you multiply, add the indices. When you divide, subtract them.", do=[T("2. Multiply → **add** · divide → **subtract**", x=80, y=260)]),
        dict(say="Step 3: anything, except 0, to the power 0 is 1.", do=[T("3. Power **0** → 1", x=80, y=350)]),
        dict(say="Step 4: check by writing out a small case in full.", do=[T("4. **Check** with a small case written out", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Mixed", steps=[
        dict(say="Simplify 3 to the power 4, times 3 to the power 5, divided by 3 to the power 6.", do=[MATH("3⁴ × 3⁵ ÷ 3⁶", x=80, y=170)]),
        dict(say="Multiply first: 4 plus 5 is 9, so 3 to the power 9. Then divide: 9 minus 6 is 3, so 3 cubed.", do=[MATH("3⁴ × 3⁵ = 3⁹", x=80, y=260), MATH("3⁹ ÷ 3⁶ = 3³", x=80, y=340, at=3.6)]),
        dict(say="3 cubed is 27.", do=[B("= 27", x=80, y=440, color=GREEN)]),
    ]),
    dict(kind="example", title="A zero index", steps=[
        dict(say="Work out 7 to the power 0, plus 2 cubed. 7 to the power 0 is 1. 2 cubed is 8. 1 plus 8 is 9.",
             do=[MATH("7⁰ + 2³", x=80, y=170), MATH("= 1 + 8 = 9", x=80, y=260, color=GREEN, at=3)]),
        PAUSE("1.4-k3", "Your turn. What is 123 to the power 0? Pause and work it out.", "Work out 123⁰."),
    ]),
    dict(kind="example", title="Check: 123⁰", steps=[
        dict(say="Any number, except 0, to the power 0 is 1. So 123 to the power 0 is 1.", do=[B("123⁰ = 1", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="Letters", steps=[
        dict(say="The rules work with letters too. Simplify x to the power 5, times x squared, divided by x to the power 4.", do=[MATH("x⁵ × x² ÷ x⁴", x=80, y=170)]),
        dict(say="5 plus 2 is 7, so x to the power 7. Then 7 minus 4 is 3. The answer is x cubed.", do=[MATH("x⁵ × x² = x⁷", x=80, y=260), B("x⁷ ÷ x⁴ = x³", x=80, y=360, color=GREEN, at=3)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Lily simplifies 2 cubed times 2 to the power 4. Which line goes wrong first?", do=LINES("Lily", "2³ × 2⁴", ["2³ × 2⁴ = 2¹²", "because 3 × 4 = 12"])),
        dict(say="Line 1 is wrong. When you multiply powers of the same base, you add the indices. You do not multiply them.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="Three 2s times four 2s is seven 2s. So the answer is 2 to the power 7.", do=[B("2³ × 2⁴ = 2⁷", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Computer memory", steps=[
        dict(say="Computers count in powers of 2. 2 to the power 10 is 1,024, which is very close to 1,000.", do=[E("💾", 90, 170, 100), T("2¹⁰ = **1024** ≈ 1000", x=230, y=200)]),
        dict(say="That is why memory sizes are often powers of 2, like 8, 16, 32, 64, 128 and 256 gigabytes.", do=[T("memory: 64 GB, 128 GB, 256 GB = 2⁶, 2⁷, 2⁸", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("1.4-k4", "One last question. Simplify y to the power 9, divided by y to the power 9. Pause the video and answer.", "Simplify y⁹ ÷ y⁹."),
        dict(say="9 minus 9 is 0, so the answer is y to the power 0. And anything divided by itself is 1. So y to the power 0 equals 1.",
             do=[MATH("y⁹ ÷ y⁹ = y⁰", x=80, y=190), B("= 1", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: when you multiply powers of the same base, add the indices.", do=[T("• aᵐ × aⁿ = aᵐ⁺ⁿ", x=80, y=170)]),
        dict(say="When you divide powers of the same base, subtract the indices.", do=[T("• aᵐ ÷ aⁿ = aᵐ⁻ⁿ", x=80, y=250)]),
        dict(say="Any number, except 0, to the power 0 is 1.", do=[T("• a⁰ = 1 (a ≠ 0)", x=80, y=330)]),
        dict(say="And the rules only work when the bases are the same.", do=[T("• Only for the **same base**", x=80, y=410)]),
    ]),
]
