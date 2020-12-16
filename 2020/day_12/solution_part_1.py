directions = []
with open('C:/Projects/advent_of_code/2020/day_12/direction_list.txt','r') as input_file:
    for line in input_file:
        directions.append(line.rstrip())

def move_nesw(current_location, move, distance):
    if move == 'N':
        temp = list(current_location)
        temp[1] += distance
        current_location = tuple(temp)
    elif move == 'E':
        temp = list(current_location)
        temp[0] += distance
        current_location = tuple(temp)
    elif move == 'S':
        temp = list(current_location)
        temp[1] -= distance
        current_location = tuple(temp)
    elif move == 'W':
        temp = list(current_location)
        temp[0] -= distance
        current_location = tuple(temp)
    return current_location

def move_forward(current_location, current_direction, distance):
    if current_direction == 'N':
        temp = list(current_location)
        temp[1] += distance
        current_location = tuple(temp)
    elif current_direction == 'E':
        temp = list(current_location)
        temp[0] += distance
        current_location = tuple(temp)
    elif current_direction == 'S':
        temp = list(current_location)
        temp[1] -= distance
        current_location = tuple(temp)
    elif current_direction == 'W':
        temp = list(current_location)
        temp[0] -= distance
        current_location = tuple(temp)
    return current_location

def move_rotation(current_direction, instruction):
    order = 'NESW'
    current = order.index(current_direction)
    if instruction[0] == 'R':
        current += int(instruction[1:])//90
    else:
        current -= int(instruction[1:])//90
    while current > len(order) -1:
        current -= 4
    new_direction = order[current]
    return new_direction

def move_boat(direction_list):
    location = [(0, 0), 'E']
    for direction in direction_list:
        if direction[0] in 'NESW':
            location[0] = move_nesw(location[0], direction[0], int(direction[1:]))
        if direction[0] == 'F':
            location[0] = move_forward(location[0], location[1], int(direction[1:]))
        else:
            location[1] = move_rotation(location[1], direction)
    return location

def manhattan_distance(location_list):
    return abs(location_list[0][0]) + abs(location_list[0][1])
		
print(f'Final location of {move_boat(directions)}, with a Manhattan distance of {manhattan_distance(move_boat(directions))}')
