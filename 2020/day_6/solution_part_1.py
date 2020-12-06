answer_list = ['']
list_index = 0
with open('C:/advent_of_code/2020/day_6/input_list.txt') as input_file:
    for line in input_file:
        if line == "\n":
            answer_list.append('')
            list_index = list_index + 1
            continue
        else:
            answer_list[list_index] = answer_list[list_index] + line.rstrip()

independent_yes = []
for answer_total in answer_list: 
    found_list = ''
    for index, answer in enumerate(answer_total):
        if answer in found_list:
            continue
        else:
            found_list = found_list + answer
    independent_yes.append(len(found_list))

print(sum(independent_yes))
