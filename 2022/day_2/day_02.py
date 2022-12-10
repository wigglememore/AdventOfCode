score = 0
score_incorrect = 0

choice_points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

outcome_points = {
    "win": 6,
    "lose": 0,
    "draw": 3,
}

def evaluate_round(opponent_choice, my_choice) -> str:
    if (
        (opponent_choice == 'A' and my_choice == 'X') 
        or (opponent_choice == 'B' and my_choice == 'Y')
        or (opponent_choice == 'C' and my_choice == 'Z')
    ):
        return "draw"
    elif (
        (opponent_choice == 'A' and my_choice == 'Z') 
        or (opponent_choice == 'B' and my_choice == 'X')
        or (opponent_choice == 'C' and my_choice == 'Y')
    ):
        return "lose"
    else:
        return "win"
        
def calculate_hand(opponent_choice, round_outcome) -> str:
    if (
        (opponent_choice == 'A' and round_outcome == 'X') 
        or (opponent_choice == 'B' and round_outcome == 'Z')
        or (opponent_choice == 'C' and round_outcome == 'Y')
    ):
        return "Z"
    elif (
        (opponent_choice == 'A' and round_outcome == 'Y') 
        or (opponent_choice == 'B' and round_outcome == 'X')
        or (opponent_choice == 'C' and round_outcome == 'Z')
    ):
        return "X"
    else:
        return "Y"
        
with open("input.txt") as strategy:
    for line in strategy:
        #opponents = index 0, mine  = index 1
        choice = line.split()
        #part1
        score_incorrect += choice_points[choice[1]] + outcome_points[evaluate_round(choice[0], choice[1])]
        #part2
        my_choice = calculate_hand(choice[0], choice[1])
        score += choice_points[my_choice] + outcome_points[evaluate_round(choice[0], my_choice)]
        
print(f"The score with your incorrect rules assumption is {score_incorrect}")
print(f"The actual score is {score}")
