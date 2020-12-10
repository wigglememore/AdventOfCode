jolt_list = []
with open('C:/Projects/advent_of_code/2020/day_10/input_list.txt','r') as input_file:
    for line in input_file:
        jolt_list.append(int(line.rstrip()))
    #add the input joltage rating
    jolt_list.append(0)
    #add the joltage rating of the device
    jolt_list.append(max(jolt_list) + 3)
    #sort the list smallest to largest
    jolt_list.sort()

def list_of_differences(list_of_numbers):
    differences = []
    for i in range(0, len(list_of_numbers) - 1):
        differences.append(list_of_numbers[i + 1] - list_of_numbers[i])
    return differences    

def histogram_dict(list_of_numbers):
    occurances = {}
    for number in list_of_numbers:
        if number in occurances.keys():
            occurances[number] = occurances[number] + 1
        else:
            occurances[number] = 1
    return occurances

def part_1(histogram_list):
    return histogram_list[1] * histogram_list[3]

def distinct_arrangements(list_of_numbers):
    list_of_numbers = list_of_numbers[1:]
    ans = {}
    ans[0] = 1
    for a in list_of_numbers:
        ans[a] = ans.get(a - 1, 0) + ans.get(a - 2, 0) + ans.get(a - 3, 0)
    return ans[list_of_numbers[-1]]

print(f'The number of 1-jolt differences multiplied by the number of 3-jolt differences is {part_1(histogram_dict(list_of_differences(jolt_list)))}')
print(f'Total number of distinct ways to arrange is {distinct_arrangements(jolt_list)}')