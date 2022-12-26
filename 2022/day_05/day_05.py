from typing import Tuple

def parse_input() -> Tuple[list, list]:
    """parse the puzzle input, extract the rows of crate definitions and rows of instructions"""
    with open("input.txt", "r") as f:
        input_file = f.read()
    crate_list, instruction_list = input_file.split("\n\n")
    crate_list = crate_list.splitlines()
    instruction_list = instruction_list.splitlines()
    return crate_list, instruction_list


def create_stacks(crate_input) -> list:
    """create the list-of-lists of crates"""
    crate_numbers = [x for x in crate_input[-1] if x.strip()]
    no_stacks = max(list(map(int, crate_numbers)))
    stacks = [[] for _ in range(0, no_stacks)]
    for crate_row in crate_input[:-1]:
        for i in range(1, no_stacks + 1):
            if crate_row[-3 + 4*i].strip():
                stacks[i-1].append(crate_row[-3 + 4*i])
    stacks = [stack[::-1] for stack in stacks]
    return stacks


def parse_instructions(instruction) -> Tuple[int, int, int]:
    """parse instruction list to extract the useful parts"""
    numbers = [int(s) for s in instruction.split() if s.isdigit()]
    return numbers[0], numbers[1]-1, numbers[2]-1


def initialise() -> Tuple[list, list]:
    """initialise whatever is required to solve the day"""
    crate_input, instruction_list = parse_input()
    stacks = create_stacks(crate_input)
    return stacks, instruction_list


def part_1() -> None:
    """solution for part 1 - move one at a time"""
    stacks, instruction_list = initialise()
    for instruction in instruction_list:
        move_number, move_from, move_to = parse_instructions(instruction)
        for instruction in range(0, move_number):
            stacks[move_to].append(stacks[move_from].pop(len(stacks[move_from])-1))
    print("Solution for part 1: ", end="")
    [print(stack[-1], end="") for stack in stacks]
    print("")
    

def part_2() -> None:
    """solution for part 2 - move them together"""
    stacks, instruction_list = initialise()
    for instruction in instruction_list:
        move_number, move_from, move_to = parse_instructions(instruction)
        stacks[move_to].extend(stacks[move_from][-move_number:])
        stacks[move_from] = stacks[move_from][:-move_number]
    print("Solution for part 2: ", end="")
    [print(stack[-1], end="") for stack in stacks]


if __name__=="__main__":
    part_1()
    part_2()
    