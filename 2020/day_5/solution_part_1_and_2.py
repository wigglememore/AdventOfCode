with open('C:/Users/matth/Documents/advent_of_code/2020/day_5/input_list.txt') as input_file:
	input_list = input_file.read().splitlines()
	
seat_ids = []
for seat in input_list:
	row = list(range(0, 128))
	col = list(range(0, 8))
	for index, letter in enumerate(seat):
		if index <= 6:
			if letter == 'F':
				row = row[:len(row)//2]
			else:
				row = row[len(row)//2:]
		else:
			if letter == 'L':
				col = col[:len(col)//2]
			else:
				col = col[len(col)//2:]
	seat_ids.append(row[0]* 8 + col[0])

for id in seat_ids:
	if id + 1 in seat_ids:
		continue
	elif id + 2 in seat_ids:
		your_seat_id = id + 1
	else:
		your_seat_id = 'I guess the challenge is wrong because your seat does not exist'

print(f'Max seat ID is {max(seat_ids)}, your seat is {your_seat_id}')