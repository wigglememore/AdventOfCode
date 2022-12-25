def initialise() -> str:
    """reads the input file and returns it as a string"""
    with open("input.txt", "r") as f:
        input_file = f.read()
    return input_file
    

def chars_to_start_of_something(input_string: str, something_length: int) -> int:
    for index, character in enumerate(input_string[something_length-1:]):
        check_for_repeat_characters_in = input_string[index:index+something_length]
        has_repeated_chars = len(set(check_for_repeat_characters_in)) != len(check_for_repeat_characters_in)
        if not has_repeated_chars:
            number_of_chars = index + something_length
            break
    return number_of_chars


def part_1() -> None:
    """solution for part 1 - solve during parsing"""
    data_buffer = initialise()
    print(f"{chars_to_start_of_something(data_buffer, 4)} characters need to be processed before the first start-of-packet marker is detected")
            
            
def part_2() -> None:
    """solution for part 2 - solve during parsing"""
    data_buffer = initialise()
    print(f"{chars_to_start_of_something(data_buffer, 14)} characters need to be processed before the first start-of-packet marker is detected")
                

if __name__=="__main__":
    part_1()
    part_2()
    