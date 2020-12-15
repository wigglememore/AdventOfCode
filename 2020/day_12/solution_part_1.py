directions = []
with open('C:/advent_of_code/2020/day_12/direction_list.txt','r') as input_file:
    for line in input_file:
        directions.append(line.rstrip())

def rotation_map()
    rotator = {}
    #dictionary of n + r90 = , n + r180 = etc...

def move_nesw(current_location, move, distance):
    if move == 'N':
        current_location[1] += distance
    elif move == 'E':
        current_location[0] += distance
    elif move == 'S':
        current_location[1] -= distance
    elif move == 'W':
        current_location[0] -= distance
    return current_location

def move_forward(current_location, current_direction, distance):
    #turn direction into vector
    #add vector
    return current_location

def move_rotation(current_direction, instruction):
    

def move_boat(direction_list):
    location = [(0, 0), 'E']
    for direction in direction_list:
        if direction[0] in 'NESW':
            location[0] = move_nesw(location[0], direction[0], direction[1:])
        if direction[0] == 'F':
            location[0] = move_forward(location[0], location[1], direction[1:])
        else:
            location[1] = move_rotation(location[1], direction)
    return location
		
move_boat(directions)