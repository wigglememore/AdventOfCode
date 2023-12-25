def read_input(input_file_name: str) -> dict:
    game_record = {}
    fname = input_file_name + ".txt"
    with open(fname) as fin:
        for line in fin:
            game_record[int(line.split("Game ")[1].split(":")[0])] = line.split(":")[1].split(";")
    return game_record


def get_max_values(strings_of_draws: list) -> dict:
#input is list of string, each string is a draw
    max_colours = {"red": 0, "green": 0, "blue": 0}
    for draw in strings_of_draws:
        #parse the string (because for some reason it is a string
        for each in draw.split(","):
            colour = "".join(char for char in each if char.isalpha())
            index = each.index(colour)
            colour_value = int(each[:index].strip())
            if max_colours[colour] < colour_value:
                max_colours[colour] = colour_value
    return max_colours


def check_game(game_max_values: dict) -> bool:
    threshold = {"red": 12, "green": 13, "blue": 14}
    #not_possible = {k,v for k,v in game_max_values.items() if k in threshold and v > threshold[k]}
    
    not_possible = {k: game_max_values[k] for k in game_max_values if game_max_values[k] > threshold[k]}
    if not_possible:
        return False
    else:
        return True


def possible_games_id_sum(input_file: dict) -> int:
    id_sum = 0
    for game_id, draws in input_file.items():
        max_values = get_max_values(draws)
        if check_game(max_values):
            id_sum += game_id
    return id_sum


def sum_of_powers(input_file: dict) -> int:
    power_sum = 0
    for game_id, draws in input_file.items():
        game_power = 1
        max_values = get_max_values(draws)
        for i in max_values:
            game_power = game_power*max_values[i]
        power_sum += game_power
    return power_sum


if __name__ == "__main__":
    print(f"Part 1 example test: ", possible_games_id_sum(read_input("input_example")) == 8)
    print(f"Part 1 answer: ", possible_games_id_sum(read_input("input")))
    print(f"Part 2 example test: ", sum_of_powers(read_input("input_example")) == 2286)
    print(f"Part 2 answer: ", sum_of_powers(read_input("input")))
