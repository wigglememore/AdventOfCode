with open('C:/Users/matth/Desktop/codeAdvent/input_list.txt') as txt_file:
    input_list = txt_file.read().splitlines()
	
for i in range(0, len(input_list)): 
    input_list[i] = int(input_list[i])

for i in input_list:
	for j in input_list:
		for k in input_list:
			if i + j + k == 2020:
				sum = i + j + k
				solution = i * j * k
				print(f'Numbers are {i}, {j} and {k}, sum is {sum} and solution is {solution}')
				break
