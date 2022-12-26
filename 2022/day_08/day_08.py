import numpy as np

def initialise() -> np.array:
    input_array = np.genfromtxt("input.txt", dtype=int, delimiter=1)
    return input_array


def check_top(array_map, row_check, column_check, height_check) -> bool:
    if row_check == 0:
        return True
    check_list = list(array_map[:,column_check]) #current column
    check_list = check_list[:row_check] #slice from one before above to the top
    for height in check_list:
        if height >= height_check:
            return False
    return True


def check_right(array_map, row_check, column_check, height_check) -> bool:
    if row_check == np.shape(array_map)[1]:
        return True
    check_list = list(array_map[row_check,:]) #current row
    check_list = check_list[column_check+1:] #slice from next one to the right to the end of the row
    for height in check_list:
        if height >= height_check:
            return False
    return True
    
    
def check_bottom(array_map, row_check, column_check, height_check) -> bool:
    if row_check == np.shape(array_map)[0]:
        return True
    check_list = list(array_map[:,column_check]) #current column
    check_list = check_list[row_check+1:] #slice from the next one below to the end of the column
    for height in check_list:
        if height >= height_check:
            return False
    return True
    

def check_left(array_map, row_check, column_check, height_check) -> bool:
    if column_check == 0:
        return True
    check_list = list(array_map[row_check,:]) #current row
    check_list = check_list[:column_check] #slice from the one before on the left to the start of the row
    for height in check_list:
        if height >= height_check:
            return False
    return True
        

def part_1_example_checker(array_map, row_check, column_check, height_check) -> None:
    if row_check == 1 and column_check == 1: #top left 5
        top = check_top(array_map, row_check, column_check, height_check)
        right = check_right(array_map, row_check, column_check, height_check)
        bottom = check_bottom(array_map, row_check, column_check, height_check)
        left = check_left(array_map, row_check, column_check, height_check)
        if (top == True and right == False and bottom == False and left == True):
            print("Passed")
        else:
            print("Failed")
    elif row_check == 1 and column_check == 2: # top middle 5
        top = check_top(array_map, row_check, column_check, height_check)
        right = check_right(array_map, row_check, column_check, height_check)
        bottom = check_bottom(array_map, row_check, column_check, height_check)
        left = check_left(array_map, row_check, column_check, height_check)
        if (top == True and right == True and bottom == False and left == False):
            print("Passed")
        else:
            print("Failed")
    elif row_check == 1 and column_check == 3: #top right 1
        top = check_top(array_map, row_check, column_check, height_check)
        right = check_right(array_map, row_check, column_check, height_check)
        bottom = check_bottom(array_map, row_check, column_check, height_check)
        left = check_left(array_map, row_check, column_check, height_check)
        if (top == False and right == False and bottom == False and left == False):
            print("Passed")
        else:
            print("Failed")
    elif row_check == 2 and column_check == 1: #left middle 5
        top = check_top(array_map, row_check, column_check, height_check)
        right = check_right(array_map, row_check, column_check, height_check)
        bottom = check_bottom(array_map, row_check, column_check, height_check)
        left = check_left(array_map, row_check, column_check, height_check)
        if (top == False and right == True and bottom == False and left == False):
            print("Passed")
        else:
            print("Failed")
    elif row_check == 2 and column_check == 2: #center 3
        top = check_top(array_map, row_check, column_check, height_check)
        right = check_right(array_map, row_check, column_check, height_check)
        bottom = check_bottom(array_map, row_check, column_check, height_check)
        left = check_left(array_map, row_check, column_check, height_check)
        if (top == False and right == False and bottom == False and left == False):
            print("Passed")
        else:
            print("Failed")
    elif row_check == 2 and column_check == 3: #right middle 3
        top = check_top(array_map, row_check, column_check, height_check)
        right = check_right(array_map, row_check, column_check, height_check)
        bottom = check_bottom(array_map, row_check, column_check, height_check)
        left = check_left(array_map, row_check, column_check, height_check)
        if (top == False and right == True and bottom == False and left == False):
            print("Passed")
        else:
            print("Failed")
    elif row_check == 3 and column_check == 2: #middle 5 on second bottom row
        top = check_top(array_map, row_check, column_check, height_check)
        right = check_right(array_map, row_check, column_check, height_check)
        bottom = check_bottom(array_map, row_check, column_check, height_check)
        left = check_left(array_map, row_check, column_check, height_check)
        if (top == False and right == False and bottom == True and left == True):
            print("Passed")
        else:
            print("Failed")


def count_top(array_map, row_check, column_check, height_check) -> int:
    if row_check == 0:
        return 0
    check_list = list(array_map[:,column_check]) #current column
    check_list = check_list[:row_check] #slice from one before above to the top
    check_list.reverse() #reverse because we are counting away from the tree
    viewing_distance = 0
    stopped = False
    for height in check_list:
        if height < height_check:
            viewing_distance += 1
        else:
            stopped = True
            break
    if stopped:
        return viewing_distance + 1
    else:
        return viewing_distance


def count_right(array_map, row_check, column_check, height_check) -> int:
    if row_check == np.shape(array_map)[1]:
        return 0
    check_list = list(array_map[row_check,:]) #current row
    check_list = check_list[column_check+1:] #slice from next one to the right to the end of the row
    viewing_distance = 0
    stopped = False
    for height in check_list:
        if height < height_check:
            viewing_distance += 1
        else:
            stopped = True
            break
    if stopped:
        return viewing_distance + 1
    else:
        return viewing_distance


def count_bottom(array_map, row_check, column_check, height_check) -> int:
    if row_check == np.shape(array_map)[0]:
        return 0
    check_list = list(array_map[:,column_check]) #current column
    check_list = check_list[row_check+1:] #slice from the next one below to the end of the column
    viewing_distance = 0
    stopped = False
    for height in check_list:
        if height < height_check:
            viewing_distance += 1
        else:
            stopped = True
            break
    if stopped:
        return viewing_distance + 1
    else:
        return viewing_distance


def count_left(array_map, row_check, column_check, height_check) -> int:
    if column_check == 0:
        return 0
    check_list = list(array_map[row_check,:]) #current row
    check_list = check_list[:column_check] #slice from the one before on the left to the start of the row
    check_list.reverse()
    viewing_distance = 0
    stopped = False
    for height in check_list:
        if height < height_check:
            viewing_distance += 1
        else:
            stopped = True
            break
    if stopped:
        return viewing_distance + 1
    else:
        return viewing_distance


def part_2_example_checker(array_map, row_check, column_check, height_check) -> None:
    if row_check == 1 and column_check == 2: #top middle 5
        top = count_top(array_map, row_check, column_check, height_check)
        right = count_right(array_map, row_check, column_check, height_check)
        bottom = count_bottom(array_map, row_check, column_check, height_check)
        left = count_left(array_map, row_check, column_check, height_check)
        if (top == 1 and right == 2 and bottom == 2 and left == 1):
            print("Passed")
        else:
            print("Failed")
    if row_check == 3 and column_check == 2: #second from bottom middle 5
        top = count_top(array_map, row_check, column_check, height_check)
        right = count_right(array_map, row_check, column_check, height_check)
        bottom = count_bottom(array_map, row_check, column_check, height_check)
        left = count_left(array_map, row_check, column_check, height_check)
        if (top == 2 and right == 2 and bottom == 1 and left == 2):
            print("Passed")
        else:
            print("Failed")
            

def part_1() -> None:
    """solution for part 1"""
    tree_map = initialise()
    visible_trees = 0
    currently_visible = False
    for index, height in np.ndenumerate(tree_map):
        #part_1_example_checker(tree_map, index[0], index[1], height)
        if check_top(tree_map, index[0], index[1], height):
            visible_trees += 1
            continue
        elif check_right(tree_map, index[0], index[1], height):
            visible_trees += 1
            continue
        elif check_bottom(tree_map, index[0], index[1], height):
            visible_trees += 1
            continue
        elif check_left(tree_map, index[0], index[1], height):
            visible_trees += 1
    print(f"Number of visible trees: {visible_trees}") 


def part_2() -> None:
    """solution for part 2"""
    tree_map = initialise()
    senic_score = 0
    for index, height in np.ndenumerate(tree_map):
        #part_2_example_checker(tree_map, index[0], index[1], height)
        top_visibility = count_top(tree_map, index[0], index[1], height)
        right_visibility = count_right(tree_map, index[0], index[1], height)
        bottom_visibility = count_bottom(tree_map, index[0], index[1], height)
        left_visibility = count_left(tree_map, index[0], index[1], height)
        current_senic_score = top_visibility * right_visibility * bottom_visibility * left_visibility
        if current_senic_score > senic_score:
            senic_score = current_senic_score        
    print(f"Highest possible senic score is: {senic_score}") 
    
    
if __name__=="__main__":
    part_1()
    part_2()
