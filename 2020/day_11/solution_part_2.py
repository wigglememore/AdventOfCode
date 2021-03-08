seat_list = {}
with open('C:/Users/matth/Documents/advent_of_code/2020/day_11/chair_grid.txt','r') as input_file:
    for row_index, line in enumerate(input_file):
        for col_index, seat in enumerate(line.rstrip()):
            seat_list[row_index, col_index] = seat

def count_occupied(seat_list):
    final_occupied_seats = 0
    for seat in seat_list.values():
        if seat == '#':
                final_occupied_seats = final_occupied_seats + 1
    return final_occupied_seats

def apply_rule(current_seat, number):
    if current_seat == 'L':
        if number == 0:
            return '#'
        else:
            return 'L'
    else:
        if number >= 5:
            return 'L'
        else:
            return '#'

def check_directions(seat_list, curent_row, current_col):
    temp_count = ''
    #i and j define the directions to check
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            #initialise the two checks and the current location
            seat_found = False
            check_number = 1
            check_row = curent_row
            check_col = current_col
            while seat_found == False and check_number <= 9:
                check_row = check_row - i
                check_col = check_col - j
                #if the index doesn't exist it just returns a .
                check_seat = seat_list.get((check_row, check_col), '.')
                check_number = check_number + 1
                #if it locates a seat it adds it to the temp variable to be counted and continues to the next direction
                if check_seat != '.':
                    temp_count = temp_count + check_seat
                    seat_found = True
    first_seat_number_occupied = temp_count.count('#')
    return first_seat_number_occupied

def check_seats(before_seats):
    change = False
    after_seats = {}
    for key in before_seats.keys():
        after_seats[key] = '.'
    for (row, col), seat in before_seats.items():
        if seat == '.':
            after_seats[row, col] = '.'
        else:
            num_occupied = check_directions(before_seats, row, col)
            after_seats[row, col] = apply_rule(seat, num_occupied)

    return after_seats, after_seats == before_seats

same = False
iterations = 0
while same == False:
    iterations = iterations + 1
    seat_list, same = check_seats(seat_list)
final_occupied = count_occupied(seat_list)
print(seat_list)
print(f'There are {final_occupied} occupied seats after {iterations} iterations')
