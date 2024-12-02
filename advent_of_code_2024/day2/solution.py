# %%
from typing import Iterable, List

# %%


def load(file: str) -> Iterable[List[int]]:
    with open(file, "r") as f:
        for line in f.readlines():
            yield list(map(int, line.split()))


def is_safe(report: List[int]) -> bool:
    is_inc = None
    for i in range(1, len(report)):
        curr = report[i-1]
        next = report[i]
        diff = next - curr
        if is_inc is None:
            is_inc = diff > 0
        elif is_inc and diff <= 0:
            return False
        elif not is_inc and diff > 0:
            return False
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    return True


def solution1(file: str) -> int:
    checked_reports = filter(is_safe, load(file))
    return len(list(checked_reports))


# %%
solution1("example.txt")


# %%
solution1("input.txt")


# %%
def is_safe2(report: List[int]) -> bool:
    if is_safe(report):
        return True
    
    for i in range(len(report)):
        cpy = report.copy()
        cpy.pop(i)
        if is_safe(cpy):
            return True
        
    return False


def solution2(file: str) -> int:
    checked_reports = filter(is_safe2, load(file))
    return len(list(checked_reports))


# %%
solution2("example.txt")


# %%
solution2("input.txt")
