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

def validation(dict_in):
	#check if passport is valid, now we know it has the correct parts
	c_byr = len(dict_in['byr']) == 4 and int(dict_in['byr']) <= 2002 and int(dict_in['byr']) >= 1920
	c_iyr = len(dict_in['iyr']) == 4 and int(dict_in['iyr']) <= 2020 and int(dict_in['iyr']) >= 2010
	c_eyr = len(dict_in['eyr']) == 4 and int(dict_in['eyr']) <= 2030 and int(dict_in['eyr']) >= 2020
	c_hgt_cm = 'cm' in dict_in['hgt'] and int(''.join(filter(str.isdigit, dict_in['hgt']))) <= 193 and int(''.join(filter(str.isdigit, dict_in['hgt']))) >= 150
	c_hgt_in = 'in' in dict_in['hgt'] and int(''.join(filter(str.isdigit, dict_in['hgt']))) <= 76 and int(''.join(filter(str.isdigit, dict_in['hgt']))) >= 59
	ok = "0123456789abcdefABCDEF"
	c_hcl = len(dict_in['hcl']) == 7 and dict_in['hcl'][0] == '#' and all(c in ok for c in dict_in['hcl'][-6:])
	eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	c_ecl = dict_in['ecl'] in eye_colours
	c_pid = len(dict_in['pid']) == 9
#return 1 to add to valid if everything is valid
	if c_byr and c_iyr and c_eyr and c_hgt_cm and c_hcl and c_ecl and c_pid:
		return 1
	elif c_byr and c_iyr and c_eyr and c_hgt_in and c_hcl and c_ecl and c_pid:
		return 1
	else:
		return 0

valid = 0
valid_list = []
for index, dict_iter in enumerate(passport_list):
	if len(dict_iter) == 8 or (len(dict_iter) == 7 and 'cid' not in dict_iter.keys()):
		print(dict_iter)
		valid = valid + validation(dict_iter)
		print(validation(dict_iter))

print(f'There are {valid} valid passports with valid data')
