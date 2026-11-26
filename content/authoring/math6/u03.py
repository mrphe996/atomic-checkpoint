# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 3 Averages (3.1 Mode, median, mean and range). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(3, "Averages", "Statistics and probability",
         "Finding the mode, median, mean and range of a set of data, and choosing which average to use.",
         {"O1": {"code": "6Ss.03", "sec": "3.1", "codeNote": "", "t": "Find and interpret the mode, median, mean and range of a set of data."},
          "O2": {"code": "6Ss.04", "sec": "3.1", "codeNote": "", "t": "Compare two sets of data using an average and the range."}})
NAMES = ["Ava", "Ben", "Chen", "Dina", "Eli", "Femi", "Gita", "Hugo", "Iris", "Jack"]


def mean_set(r, n=5, lo=1, hi=20):
    while True:
        xs = [r.randint(lo, hi) for _ in range(n)]
        if sum(xs) % n == 0: return xs


s = U.section("3.1", "Mode, median, mean and range", ["O1", "O2"])
s.idea("Three averages", ["An **average** is one number that represents a set of data.",
       "The **mode** is the value that appears most often. The **median** is the middle value when the data are in order. The **mean** is the total divided by how many values there are."],
       table={"head": ["Data", "3, 5, 5, 6, 11"], "rows": [["Mode", "5"], ["Median", "5"], ["Mean", "30 ÷ 5 = 6"], ["Range", "11 − 3 = 8"]]})
s.check(N("Find the mean of 4, 6, 8, 10 and 12.", 8, o="O1"))
s.idea("Range", ["The **range** is the biggest value minus the smallest value. It shows how **spread out** the data are. A small range means the data are close together."])
s.example("Median of an even set", "Find the median of 3, 9, 4, 7.", [("Order: 3, 4, 7, 9", "write the data in order"), ("Middle two are 4 and 7: (4 + 7) ÷ 2 = 5.5", "halfway between them")], "5.5")
s.idea("Which average to use", ["The mode is the most common value. The median is the middle value when the data is in order. The mean shares the total out equally.",
       "One very big or very small value changes the mean a lot but the median only a little."])
s.check(MC("Before you read on: the values 2, 3, 3, 4, 50 – which average is most typical?", "The median, 3", [("The mean, 12.4", "The 50 pulls the mean up."), ("The range, 48", "The range is a spread, not an average.")], o="O1"))
s.mistake("Order first", ["Always put the data in order before finding the median."])


def a1(r):
    xs = r.sample(range(1, 30), 4); m = pick(r, xs); xs = xs + [m]; r.shuffle(xs)
    return N(f"Find the mode of {', '.join(map(str, xs))}.", m, o="O1")
def a2(r):
    xs = r.sample(range(1, 40), 5)
    return N(f"Find the median of {', '.join(map(str, xs))}.", sorted(xs)[2], o="O1")
def a3(r):
    xs = mean_set(r)
    return N(f"Find the mean of {', '.join(map(str, xs))}.", sum(xs) // 5, o="O1")
def a4(r):
    xs = r.sample(range(1, 60), 6)
    return N(f"Find the range of {', '.join(map(str, xs))}.", max(xs) - min(xs), o="O1")
def a5(r):
    nm = r.sample(NAMES, 5); xs = mean_set(r, 5, 2, 15)
    return N("The table shows how many books each child read. Find the mean number of books.", sum(xs) // 5, "books", units=["books"], o="O1", data={"head": ["Child", *nm], "rows": [["Books", *map(str, xs)]]})
def a6(r):
    lab = ["Red", "Blue", "Green", "Yellow"]; v = r.sample([3, 5, 7, 9, 11], 4)
    k = v.index(max(v))
    return S("The bar chart shows favourite colours. What is the mode?", [lab[k], lab[k].lower()], o="O1", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 12, "step": 2, "ylabel": "Children"})
def a7(r):
    xs = r.sample(range(1, 30), 4)
    s_ = sorted(xs); md = (s_[1] + s_[2]) / 2
    return N(f"Find the median of {', '.join(map(str, xs))}.", md, o="O1", d="H")
def a8(r):
    xs = mean_set(r, 4, 5, 20)
    return TB(f"Complete the table for the data {', '.join(map(str, xs))}.", ["Statistic", "Value"], [["Mean", B(sum(xs) // 4)], ["Range", B(max(xs) - min(xs))]], o="O1")
def a9(r):
    n, m = r.randint(4, 6), r.randint(5, 12)
    return N(f"The mean of {n} numbers is {m}. What is their total?", n * m, o="O1", d="H")
def a10(r):
    a = r.sample(range(10, 30), 5); b = r.sample(range(10, 30), 5)
    ra, rb = max(a) - min(a), max(b) - min(b)
    if ra == rb: return None
    return MC(f"Team A scored {', '.join(map(str, a))}. Team B scored {', '.join(map(str, b))}. Which team's scores are more consistent?", "Team A" if ra < rb else "Team B", ["Team B" if ra < rb else "Team A"], o="O2", reason=f"The smaller range ({min(ra, rb)}) shows scores closer together.", d="H")


def c1_1(r):
    v = sorted(r.sample(range(2, 15), 4)); m = r.randint(5, 10); x = 5 * m - sum(v)
    if not 0 < x < 40: return None
    return N(f"The mean of five numbers is {m}. Four of them are {', '.join(map(str, v))}. What is the fifth?", x, o="O1", d="H", reason=f"Total = 5 × {m} = {5 * m}; {5 * m} − {sum(v)} = {x}.")


s.std([a5, a6, a1, a2, a3, a4, a8, a7, a9], EX("Explain how to find the median of 8, 2, 6, 9, 5.", [("put the numbers in order: 2, 5, 6, 8, 9", "order|2, ?5, ?6"), ("the middle number is 6", "middle|\\b6\\b")], "Put the numbers in order: 2, 5, 6, 8, 9. The middle value is 6, so the median is 6.", o="O1"), adv=[a7, a9, a10, a8],
      deep=[c1_1])

U.mindmap(("Mode", "Most common value", "O1", "3.1"), ("Median", "Middle value in order", "O1", "3.1"), ("Mean", "Total ÷ number of values", "O1", "3.1"), ("Range", "Biggest − smallest; shows spread", "O2", "3.1"))
