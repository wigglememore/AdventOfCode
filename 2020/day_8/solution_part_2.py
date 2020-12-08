import copy

instructions = []
with open('C:/Projects/advent_of_code/2020/day_8/instruction_list.txt') as input_file:
    for line in input_file:
        split_list = line.split()
        temp_dict = {split_list[0]: split_list[1].rstrip()}
        instructions.append(temp_dict)

def acc_calculator(instructions_list):
    accumulator = 0
    repeat = False
    used_indices = []
    i = 0

    while not repeat:
        while i <= len(instructions_list):
            #if len list then the index corresponds to the (nonexistant) instruction below the final instruction
            if i == len(instructions_list):
                return accumulator, True
            if i in used_indices:
                repeat = True
                break

            used_indices.append(i)
            key, val = next(iter(instructions_list[i].items()))
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
    return accumulator, False

for i in range(0, len(instructions) - 1):
    key, val = next(iter(instructions[i].items()))
    if key == 'acc':
        continue
    elif key == 'jmp':
        temp_instructions = copy.deepcopy(instructions)
        temp_instructions[i]['nop'] = temp_instructions[i].pop('jmp')
        temp_output = acc_calculator(temp_instructions)
        if temp_output[1]:
            accu = temp_output[0]
            break
    else:
        temp_instructions = copy.deepcopy(instructions)
        temp_instructions[i]['jmp'] = temp_instructions[i].pop('nop')
        temp_output = acc_calculator(temp_instructions)
        if temp_output[1]:
            accu = temp_output[0]
            break

print(f'The value of the accumulator when the instruction list if fixed is {accu}')