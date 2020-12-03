tree_map = []
with open('C:/code_advent/day_3/input_map.txt') as input_file:
    for line in input_file:
        tree_map.append(line.rstrip())
    
across = 7
down = 1
height = len(tree_map)
width = len(tree_map[0])
adding_iteration = 1
while width < height*across/down:
    for index, value in enumerate(tree_map):
        tree_map[index] = value + value[:len(value)//adding_iteration]
    adding_iteration = adding_iteration + 1
    width = len(tree_map[0])

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
tree_totals = []
for slope in slopes:
    tree_coordinate = [0, 0]
    trees = 0
    not_trees = 0
    while tree_coordinate[0] < len(tree_map[0]) and tree_coordinate[1] < height:
        if tree_map[tree_coordinate[1]][tree_coordinate[0]] == '#':
            trees = trees + 1
        else:
            not_trees = not_trees + 1
        tree_coordinate[0] = tree_coordinate[0] + slope[0]
        tree_coordinate[1] = tree_coordinate[1] + slope[1]
    tree_totals.append(trees)
solution = 1
for total in tree_totals:
    solution = solution * total
print(f'Mulitplying {tree_totals} gives {solution}')
