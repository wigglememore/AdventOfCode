def get_input():
    numbers = []
    numbers_strings = open('input_numbers.txt','r').read().rstrip().split(',')
    numbers = [int(n) for n in numbers_strings]
    return numbers

def get_num(list_location):
    number_list = get_input()
    initial_length = len(number_list) - 1
    for num in range(initial_length + 1, list_location):
        previous_number = number_list[num - 1]
        if previous_number not in number_list[:-1]:
            number_list.append(0)
        else:
            indices = []
            indices = [i for i, x in enumerate(number_list[:-1]) if x == previous_number]
            difference = num - 1 - max(indices)
            number_list.append(difference)
    return number_list[list_location - 1]

def part_two_needs_to_be_fast(list_location):
    number_list = get_input()
    numbers = {number:index for index, number in enumerate(number_list, start = 1)}
    num = len(numbers) + 1
    number_to_be_spoken = 0
    while num < list_location:
        number_list.append(number_to_be_spoken)
        if number_to_be_spoken in numbers.keys():
            next_number = num - numbers[number_to_be_spoken]
            numbers[number_to_be_spoken] = num
            number_to_be_spoken = next_number
        else:
            numbers[number_to_be_spoken] = num
            number_to_be_spoken = 0
        num += 1
    return number_to_be_spoken

print(f'Part 1: {get_num(2020)}')
print(f'Part 2: {part_two_needs_to_be_fast(30000000)}')
