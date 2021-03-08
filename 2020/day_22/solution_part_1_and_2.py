import copy

def import_data():
    player_1 = []
    player_2 = []
    with open('card_deal.txt') as input_file:
        found_player_two_start = False
        for line in input_file:
            if line == '\n' or line.rstrip() == 'Player 1:':
                continue
            elif line.rstrip() == 'Player 2:':
                found_player_two_start = True
                continue
            elif found_player_two_start == False and line.rstrip().isdigit():
                player_1.append(int(line.rstrip()))
            else:
                player_2.append(int(line.rstrip()))
    return player_1, player_2

def play_game(player_1, player_2):
    won_len = len(player_1) + len(player_2)
    while len(player_1) != won_len and len(player_2) != won_len:
        if player_1[0] > player_2[0]:
            player_1.append(player_1[0])
            player_1.append(player_2[0])
            player_1 = player_1[1:]
            player_2 = player_2[1:]
        else:
            player_2.append(player_2[0])
            player_2.append(player_1[0])
            player_1 = player_1[1:]
            player_2 = player_2[1:]
    if len(player_1) == won_len:
        winner = player_1
    else:
        winner = player_2
    return winner


def play_recursive_game(player_1, player_2):    
    previous_player_1 = set()
    previous_player_2 = set()
    won_len = len(player_1) + len(player_2)
    while len(player_1) != won_len and len(player_2) != won_len:
        if tuple(player_1) in previous_player_1 and tuple(player_2) in previous_player_2:
            return 'player_1', player_1
        previous_player_1.add(tuple(player_1))
        previous_player_2.add(tuple(player_2))
        #check drawn card against remaining cards
        if player_1[0] <= (len(player_1) - 1) and player_2[0] <= (len(player_2) - 1):
            player_1_pass = copy.deepcopy(player_1[1:player_1[0] + 1])
            player_2_pass = copy.deepcopy(player_2[1:player_2[0] + 1])
            round_win, temp_list = play_recursive_game(player_1_pass, player_2_pass)
            if round_win == 'player_1':
                player_1.append(player_1[0])
                player_1.append(player_2[0])
                player_1 = player_1[1:]
                player_2 = player_2[1:]
            else:
                player_2.append(player_2[0])
                player_2.append(player_1[0])
                player_1 = player_1[1:]
                player_2 = player_2[1:]
        #original rules
        elif player_1[0] > player_2[0]:
            player_1.append(player_1[0])
            player_1.append(player_2[0])
            player_1 = player_1[1:]
            player_2 = player_2[1:]
        else:
            player_2.append(player_2[0])
            player_2.append(player_1[0])
            player_1 = player_1[1:]
            player_2 = player_2[1:]
    #return winner
    if len(player_1) == won_len:
        winner = 'player_1'
        final_hand = player_1
    else:
        winner = 'player_2'
        final_hand = player_2
    return winner, final_hand
    

def calculate_score(winning_cards):
    length = len(winning_cards)
    score = 0
    for index, card in enumerate(winning_cards):
        score += card * (length - index)
    return score

player_1_start, player_2_start = import_data()
print(f'Part 1 winning score: {calculate_score(play_game(player_1_start, player_2_start))}')
player_1_start, player_2_start = import_data()
print(f'Part 2 winning score: {calculate_score(play_recursive_game(player_1_start, player_2_start)[1])}')
