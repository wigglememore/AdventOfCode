answer_list = [[]]
list_index = 0
with open('C:/advent_of_code/2020/day_6/input_list.txt') as input_file:
    for line in input_file:
        if line == "\n":
            answer_list.append([])
            list_index = list_index + 1
            continue
        else:
            answer_list[list_index].append(line.rstrip())

everyone_yes = []
for group_list in answer_list:
    if len(group_list) == 1:
        everyone_yes.append(len(group_list[0]))
    else:
        everyone_yes.append(len(set.intersection(*[set(item) for item in group_list])))
        
print(sum(everyone_yes))