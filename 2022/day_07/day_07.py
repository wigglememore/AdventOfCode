def initialise() -> list:
    """reads the input file and returns a list, with an item for each line"""
    with open("input.txt", "r") as f:
        input_file_list = f.readlines()
    return input_file_list


def get_size(input_file_list: list) -> dict:
    """reads through the input terminal output line-by-line and calculated the used storage"""
    directory_path = []
    size = {}
    for cmd_out in input_file_list:
        if cmd_out[:4] == "$ cd":
            #add directory name to the current directory path list
            if "/" in cmd_out:
                directory_path = ["/"]
            elif ".." not in cmd_out:
                directory_path.append(cmd_out.split()[-1])
            else:
                directory_path.pop()
            continue
        elif cmd_out[:4] == "$ ls" or cmd_out[:3] == "dir":
            #not a directory change and not a file size
            continue
        else:
            #add the file size to all directories in the current path
            #thanks to u/herpington for this part, realisation explanation in the readme
            for i in range(len(directory_path)):
                directory_total = "".join(directory_path[:i+1])
                if directory_total in size:
                    size[directory_total] += int(cmd_out.split()[0])
                else:
                    size[directory_total] = int(cmd_out.split()[0])
    return size
    

def part_1() -> None:
    """solution for part 1"""
    terminal_list = initialise()
    sizes = get_size(terminal_list)
    sum_of_small_directories = 0
    for total in sizes.values():
        if total < 100000:
            sum_of_small_directories += total
    print(f"The sum of the total sizes of the directories with a size of at most 100000 is {sum_of_small_directories}")
    
    
def part_2() -> None:
    """solution for part 2"""
    terminal_list = initialise()
    sizes = get_size(terminal_list)
    extra_size_required = 30000000 - 70000000 + sizes["/"]
    current_smallest_size_that_is_big_enough = 10000000000 #anything huge
    for total in sizes.values():
        if total > extra_size_required and total < current_smallest_size_that_is_big_enough:
            current_smallest_size_that_is_big_enough = total
    print(f"The total size of the smallest directory that is big enough to free enough space is {current_smallest_size_that_is_big_enough}")
    
    
if __name__=="__main__":
    part_1()
    part_2()
    