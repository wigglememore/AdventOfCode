item_priority_sum = 0
badge_priority_sum = 0
three_counter = 1
first_save = ''
second_save = ''
badge_common = ''
badge_priority = 0

with open("input.txt") as packed_rucksacks:
    for item in packed_rucksacks:
        #part1
        common_type = ''.join(set(item[:int(len(item.strip())/2)]).intersection(set(item[int(len(item.strip())/2):])))
        if common_type.isupper():
            item_priority = ord(common_type) - 38
        else:
            item_priority = ord(common_type) - 96
        item_priority_sum += item_priority
    
        if three_counter == 1:
            first_save = item.strip()
            three_counter += 1
        elif three_counter == 2:
            second_save = item.strip()
            three_counter += 1
        else:
            badge_common = set(first_save) & set(second_save) & set(item.strip())
            badge_common = ''.join(badge_common)
            three_counter = 1
            if badge_common.isupper():
                badge_priority = ord(badge_common) - 38
            else:
                badge_priority = ord(badge_common) - 96
            badge_priority_sum += badge_priority

print(f"The sum of the incorrect item priorities is {item_priority_sum}")
print(f"The sum of the badge priorities is {badge_priority_sum}")
