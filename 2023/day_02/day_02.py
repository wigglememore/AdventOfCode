import re

def read_input(input_file_name: str) -> dict:
    game_record = {}
    fname = input_file_name + ".txt"
    with open(fname) as fin:
        for line in fin:
            game_record[line.split("Game ")[1].split(":")[0]] = line.split(":")[1].split(";")
    print(game_record)
    return game_record

def possible_games_id_sum(input_file: dict) -> int:
    id_sum = 0
    for game_id, draws in input_file.items():
        for draw in draws:
            
    
    return id_sum

if __name__ == "__main__":
    read_input("input_example_p1")
    #print(f"Part 1 example test: ", possible_games_id_sum(read_input("input_example_p1")) == 8)
    #print(f"Part 1 answer: ", calibration_sum(read_input("input")))
    #print(f"Part 2 example test: ", calibration_spelled_sum(read_input("input_example_p2")) == 281)
    #print(f"Part 2 answer: ", calibration_spelled_sum(read_input("input")))

https://github.com/website11/My-Advent-Of-Code/blob/main/Python/2023/Day_2/Day_2.py