# %%
from functools import reduce

# %%
def load(file: str) -> (list[str], list[str]):
    left = []
    right = []

    lines = open(file, "r").readlines()
    for line in lines:
        s = line.split()
        left.append(int(s[0]))
        right.append(int(s[1]))

    return left, right


def solution1(file: str) -> int:
    left, right = load(file)

    sl = sorted(left)
    sr = sorted(right)

    zipped = zip(sl, sr)
    subbed = map(lambda t: t[1] - t[0], zipped)
    total = reduce(lambda acc, v: abs(v) + acc, subbed, 0)

    return total


# %%
solution1("example.txt")


# %%
solution1("input.txt")


# %%
def solution2(file: str) -> int:
    left, right = load(file)

    sl = sorted(left)
    sr = sorted(right)

    simil_score = 0
    curr_count = 0
    prev_value = None

    for lv in sl:
        if prev_value == lv:
            simil_score += lv * curr_count
            continue
        prev_value = lv
        curr_count = 0
        for rv in sr:
            if lv == rv:
                curr_count += 1
            elif lv < rv:
                break
        simil_score += lv * curr_count

    return simil_score


# %%
solution2("example.txt")


# %%
solution2("input.txt")
