# %%
import re


def read_input(file: str) -> str:
    puzzleInput = ""
    with open(file, "r") as f:
        for line in f.readlines():
            puzzleInput += line.strip()

    return puzzleInput.strip()


def solve_input(input: str) -> int:
    matches = re.findall(r"mul\(\d+,\d+\)", input)
    total = 0
    for m in matches:
        vals = m[4:-1].split(",")
        total += int(vals[0]) * int(vals[1])

    return total


def solution1(file: str) -> int:
    return solve_input(read_input(file))


solution1("input.txt")


def solution2(file: str) -> int:
    current_input = read_input(file)
    total = 0
    enabled = True
    
    while current_input:
        next_instruction = current_input.find("don't()" if enabled else "do()")
        
        if enabled:
            chunk = current_input[:next_instruction] \
                if next_instruction != -1 \
                else current_input
            total += solve_input(chunk)
            print(chunk)
        
        skip_chars = 7 if enabled else 4
        current_input = current_input[next_instruction+skip_chars:] \
            if next_instruction != -1 \
            else ""
        enabled = not enabled
        
    return total


solution2("input.txt")