xmas_list = []
with open('C:/Projects/advent_of_code/2020/day_9/data_input.txt','r') as input_file:
    for line in input_file:
        xmas_list.append(int(line.rstrip()))

def is_last_25_sum(target, search_list):
    for a in search_list:
        for b in search_list:
            if a + b == target:
                return True
    return False

def find_first_invalid(num_list):
    found = False
    i = 25
    while (i <= len(num_list) + 1) and (found == False):
        found = not is_last_25_sum(num_list[i], num_list[i - 25: i])
        i = i + 1
    return i - 1, num_list[i - 1]

def find_weakness(invalid_number, invalid_index, num_list):
    found_sum = False
    i = 0
    while (i <= len(num_list) + 1) and (found_sum == False):
        temp_check = []
        for number in num_list[i:]:
            temp_check.append(number)
            if sum(temp_check) == invalid_number:
                found_sum = True
                break
            elif sum(temp_check) > invalid_number:
                break
            else:
                continue
        i = i + 1
    return min(temp_check) + max(temp_check)

part_1_index, part_1_value = find_first_invalid(xmas_list)
weakness = find_weakness(part_1_value, part_1_index, xmas_list)
print(f'First invalid number is {part_1_value} at index {part_1_index}')
print(f'Encryption weakness is {weakness}')