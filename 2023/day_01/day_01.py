

#print(f"The elf carrying the most calories has a whopping {max_calories}")
#print(f"The three elves carrying the most calories have a whopping {top_1_cal + top_2_cal + top_3_cal} combined!")


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
        
print(f"Part 1 example test: ", calibration_sum(read_input("input_example")) == 142)
print(f"Part 1 answer: ", calibration_sum(read_input("input")))
