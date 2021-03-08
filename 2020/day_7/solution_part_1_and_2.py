bags_in_bags = {}
with open('C:/advent_of_code/2020/day_7/input_rules.txt') as input_file:
    for line in input_file:
        split = line.split()
        current_top_key = split[0] + ' ' + split[1]
        bags_in_bags[current_top_key] = {}
        if split[4].isdigit():
            fi = 4
            while fi < len(split):
                bags_in_bags[current_top_key][split[fi + 1] + ' ' + split[fi + 2]] = int(split[fi])
                fi = fi + 4

#---------- part 1 ----------#
my_bag = 'shiny gold'
bag_carriers = []
for bag, sub_bags in bags_in_bags.items():
    if my_bag in sub_bags.keys():
        bag_carriers.append(bag)

levels_deep = 0
new_bag_carriers = []
final_bags = bag_carriers
while levels_deep < len(bags_in_bags):
    for carry_bag in bag_carriers:
        #print(carry_bag)
        for bag, sub_bags in bags_in_bags.items():
            if carry_bag in sub_bags.keys():
                new_bag_carriers.append(bag)
    levels_deep = levels_deep + 1
    final_bags.extend(new_bag_carriers)
    bag_carriers = list(dict.fromkeys(new_bag_carriers))
    new_bag_carriers = []
    #print(levels_deep)
final_bags = list(dict.fromkeys(final_bags)) 

#---------- part 2 ----------#
bags_in_gold = bags_in_bags['shiny gold']
contained_bags = [[]]
contained_bags[0].append(bags_in_gold)
new_bag_search = []
new_bag_search = bags_in_gold.keys()
extra_bags = []
extra_bags_level = 1
cond = True
while cond:
    extra_bags = []
    for bag in new_bag_search:
        if bag == 'posh yellow':
            print(bags_in_bags[bag])
        if bags_in_bags[bag]:
            contained_bags.append([])
            contained_bags[extra_bags_level].append(bags_in_bags[bag])
            extra_bags = extra_bags + list(bags_in_bags[bag].keys())
            extra_bags_level = extra_bags_level + 1
        else:
            contained_bags.append([])
            contained_bags[extra_bags_level].append(bags_in_bags[bag])
            extra_bags_level = extra_bags_level + 1
    new_bag_search = list(dict.fromkeys(extra_bags))
    if not new_bag_search:
        cond = False

#start with 0 of length x
#take the next x items (1 to x)
#list 0th[0] and 
        
#---------- answers ----------#        
print(f'{len(final_bags)} bag colours can contain at least one shiny gold bag')
print(f'{contained_bags} individual bags are required inside a shiny gold bag')