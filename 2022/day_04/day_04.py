fully_contains = 0
partially_contains = 0

with open("input.txt") as pair_assignments:
    for item in pair_assignments:
        first, second = item.split(",")
        first_small, first_large = first.split("-")
        second_small, second_large = second.split("-")
        #logic for part 1
        first_in_second = int(first_small) >= int(second_small) and int(first_large) <= int(second_large)
        second_in_first = int(second_small) >= int(first_small) and int(second_large) <= int(first_large)
        if first_in_second or second_in_first:
            fully_contains += 1
        
        #logic for part 2
        first_set = set(range(int(first_small), int(first_large) + 1))
        second_set = set(range(int(second_small), int(second_large) + 1))
        if first_set & second_set:
            partially_contains += 1
        
print(f"The number of assignment pairs who's range fully contain the other is {fully_contains}")
print(f"The number of assignment pairs which overlap at all is {partially_contains}")
