num_min = []
num_max = []
letter = []
string_to_check = []
with open('C:/code_advent/day_2/input_list.txt') as input_file:
    for line in input_file:
        split_list = line.split()
        split_min_max = split_list[0].split('-')
        num_min.append(split_min_max[0])
        num_max.append(split_min_max[1])
        letter.append(split_list[1][0])
        string_to_check.append(split_list[2])

valid_passwords = 0
invalid_passwords = 0
for index, item in enumerate(string_to_check):
    occurances = item.count(letter[index])
    if int(num_min[index]) <= occurances and occurances <= int(num_max[index]):
        valid_passwords = valid_passwords + 1
    else:
        invalid_passwords = invalid_passwords + 1
        
print(f'{valid_passwords} valid passwords, check that {valid_passwords + invalid_passwords} equals {len(string_to_check)}')
