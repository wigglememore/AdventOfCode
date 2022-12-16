current_calories = 0
max_calories = 0
top_1_cal = 0
top_2_cal = 0
top_3_cal = 0

with open("input.txt") as calorie_list:
    for line in calorie_list:
        if line != "\n":
            current_calories += int(line)
        else:    
            #single max calculation
            if current_calories > max_calories:
                max_calories = current_calories
            #top three calculation
            if current_calories > top_1_cal:
                top_3_cal = top_2_cal
                top_2_cal = top_1_cal
                top_1_cal = current_calories
            elif current_calories < top_1_cal and current_calories > top_2_cal:
                top_3_cal = top_2_cal
                top_2_cal = current_calories
            elif current_calories < top_2_cal and current_calories > top_3_cal:
                top_3_cal = current_calories
            #reset counter
            current_calories = 0

print(f"The elf carrying the most calories has a whopping {max_calories}")
print(f"The three elves carrying the most calories have a whopping {top_1_cal + top_2_cal + top_3_cal} combined!")