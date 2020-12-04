passport_list = [{}]
list_index = 0
with open('C:/Users/matth/Documents/advent_of_code/2020/day_4/input_list.txt') as input_file:
	for line in input_file:
		if line == "\n":
			passport_list.append({})
			list_index = list_index + 1
			continue
		else:
			sections = line.split()
			for pair in sections:
				passport_list[list_index][pair.split(':')[0]] = pair.split(':')[1]

valid = 0
invalid = 0
for dict in passport_list:
	if len(dict) == 8:
		valid = valid + 1
	elif len(dict) == 7 and 'cid' not in dict.keys():
		valid = valid + 1
	else:
		invalid = invalid + 1

print(f'There are {valid} valid passports and check that {valid + invalid} is equal to {len(passport_list)}')
    
