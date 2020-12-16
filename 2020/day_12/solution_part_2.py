directions = []
with open('C:/Projects/advent_of_code/2020/day_12/direction_list.txt','r') as input_file:
    for line in input_file:
        directions.append(line.rstrip())

def move_waypoint_nesw(current_waypoint_location, move, distance):
    if move == 'N':
        temp = list(current_waypoint_location)
        temp[1] += distance
        current_waypoint_location = tuple(temp)
    elif move == 'E':
        temp = list(current_waypoint_location)
        temp[0] += distance
        current_waypoint_location = tuple(temp)
    elif move == 'S':
        temp = list(current_waypoint_location)
        temp[1] -= distance
        current_waypoint_location = tuple(temp)
    elif move == 'W':
        temp = list(current_waypoint_location)
        temp[0] -= distance
        current_waypoint_location = tuple(temp)
    return current_waypoint_location

def move_boat_forward(current_boat_location, current_waypoint_location, multiplier):
    distance_east = current_waypoint_location[0]
    distance_north = current_waypoint_location[1]
    temp = list(current_boat_location)
    temp[0] += distance_east * multiplier
    temp[1] += distance_north * multiplier
    current_boat_location = tuple(temp)
    return current_boat_location

def move_waypoint_rotation(current_boat_location, current_waypoint_location, instruction):
    if instruction[1:] == '180':
        new_waypoint_direction = (-current_waypoint_location[0], -current_waypoint_location[1])
    elif instruction == 'R90' or instruction == 'L270':
        new_waypoint_direction = (current_waypoint_location[1], -current_waypoint_location[0])
    else:
        new_waypoint_direction = (-current_waypoint_location[1], current_waypoint_location[0])
    return new_waypoint_direction

def move_both(direction_list):
    waypoint_location = (10, 1)
    boat_location = [(0, 0), 'E']
    for direction in direction_list:
        if direction[0] in 'NESW':
            waypoint_location = move_waypoint_nesw(waypoint_location, direction[0], int(direction[1:]))
        elif direction[0] == 'F':
            boat_location[0] = move_boat_forward(boat_location[0], waypoint_location, int(direction[1:]))
        else:
            waypoint_location = move_waypoint_rotation(boat_location[0], waypoint_location, direction)
    return boat_location

def manhattan_distance(location_list):
    return abs(location_list[0][0]) + abs(location_list[0][1])
		
print(f'Final location of {move_both(directions)}, with a Manhattan distance of {manhattan_distance(move_both(directions))}')
