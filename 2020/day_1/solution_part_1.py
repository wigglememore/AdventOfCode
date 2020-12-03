with open('C:/Users/matth/Desktop/codeAdvent/input_list.txt') as txt_file:
    input_list = txt_file.read().splitlines()
	
for i in range(0, len(input_list)): 
    input_list[i] = int(input_list[i])

for i in input_list:
	for j in input_list:
		if i + j == 2020:
			sum = i + j
			solution = i * j
			print(f'Numbers are {i} and {j}, sum is {sum} and solution is {solution}')
			break