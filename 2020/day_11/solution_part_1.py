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
        if number >= 4:
            return 'L'
        else:
            return '#'
    
def check_seats(before_seats):
    change = False
    after_seats = {}
    for key in before_seats.keys():
        after_seats[key] = '.'
    for (row, col), seat in before_seats.items():
        if seat == '.':
            after_seats[row, col] = '.'
        else:
            temp_count = ''
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == j == 0:
                        continue
                    temp_count = temp_count + before_seats.get((row - i, col - j), '.')
            num_occupied = temp_count.count('#')
            after_seats[row, col] = apply_rule(seat, num_occupied)
                
    return after_seats, after_seats == before_seats

same = False
iterations = 0
while same == False:
    iterations = iterations + 1
    seat_list, same = check_seats(seat_list)
final_occupied = count_occupied(seat_list)

print(f'There are {final_occupied} occupied seats after {iterations} iterations')
