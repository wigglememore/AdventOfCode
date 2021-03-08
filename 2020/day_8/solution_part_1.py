instructions = []
with open('C:/Projects/advent_of_code/2020/day_8/instruction_list.txt') as input_file:
    for line in input_file:
        split_list = line.split()
        temp_dict = {split_list[0]: split_list[1].rstrip()}
        instructions.append(temp_dict)

accumulator = 0
repeat = False
used_indices = []
i = 0

while not repeat:
    while i <= len(instructions) + 1:
        if i in used_indices:
            repeat = True
            break
        used_indices.append(i)
        key, val = next(iter(instructions[i].items()))
        if key == 'acc':
            if val[0] == '+':
                accumulator = accumulator + int(val[1:])
                i = i + 1
            else:
                accumulator = accumulator - int(val[1:])
                i = i + 1
        if key == 'nop':
            i = i + 1
        if key == 'jmp':
            if val[0] == '+':
                i = i + int(val[1:])
            else:
                i = i - int(val[1:])    

print(accumulator)