import regex as re
from word2number import w2n

def read_input(input_file_name: str) -> list:
    amended_list = []
    fname = input_file_name + ".txt"
    with open(fname) as fin:
        for line in fin:
            amended_list.append(line.strip())
    return amended_list


def calibration_sum(input_file: list) -> int:
    num_sum = 0
    for line in input_file: 
        for character in line:
            if character.isdigit():
                first_num = character
                break
        for character in line[::-1]:
            if character.isdigit():
                last_num = character
                break
        num_sum += int(first_num + last_num)
    return num_sum

def calibration_spelled_sum(input_file: list) -> int:
    pattern = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    regex = re.compile(r'(' + '|'.join(pattern) + r')')
    num_sum = 0
    for line in input_file: 
        instances = regex.findall(line, overlapped=True)
        if instances[0].isdigit():
            first_num = instances[0]
        else:
            first_num = str(w2n.word_to_num(instances[0]))
        if instances[-1].isdigit():
            last_num = instances[-1]
        else:
            last_num = str(w2n.word_to_num(instances[-1]))
        num_sum += int(first_num + last_num)
    return num_sum

print(f"Part 1 example test: ", calibration_sum(read_input("input_example_p1")) == 142)
print(f"Part 1 answer: ", calibration_sum(read_input("input")))
print(f"Part 2 example test: ", calibration_spelled_sum(read_input("input_example_p2")) == 281)
print(f"Part 2 answer: ", calibration_spelled_sum(read_input("input")))
