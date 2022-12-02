ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

WIN = "WIN"
DRAW = "DRAW"
LOSS = "LOSS"

shape_score = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}

moves_mapping = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

win_score = {"WIN": 6, "DRAW": 3, "LOSS": 0}


def calculate_result(opponent_move, player_move):
    """
    determines if the player won, loss or draw
    """
    if opponent_move == player_move:
        return win_score[DRAW]
    elif opponent_move == ROCK and (player_move == SCISSORS):
        return win_score[LOSS]
    elif opponent_move == ROCK and (player_move == PAPER):
        return win_score[WIN]
    elif opponent_move == PAPER and (player_move == ROCK):
        return win_score[LOSS]
    elif opponent_move == PAPER and (player_move == SCISSORS):
        return win_score[WIN]
    elif opponent_move == SCISSORS and (player_move == PAPER):
        return win_score[LOSS]
    else:
        # opponent move is scissors and player move is rock
        return win_score[WIN]


def calculate_round_score(opponent, player):
    """
    determines the score of the player
    """
    opponent_move = moves_mapping[opponent]
    player_move = moves_mapping[player]

    move_score = shape_score[player_move]
    round_score = calculate_result(opponent_move, player_move)

    return move_score + round_score


fhand = open("input.txt")

# answer for puzzle 1
player_score = 0

# mapping for puzzle 2
win_mapping = {"X": LOSS, "Y": DRAW, "Z": WIN}


def calculate_required_move(opponent_move, player_strategy):
    if player_strategy == DRAW:
        return opponent_move
    if opponent_move == ROCK and player_strategy == WIN:
        return PAPER
    if opponent_move == ROCK and player_strategy == LOSS:
        return SCISSORS
    if opponent_move == PAPER and player_strategy == WIN:
        return SCISSORS
    if opponent_move == PAPER and player_strategy == LOSS:
        return ROCK
    if opponent_move == SCISSORS and player_strategy == WIN:
        return ROCK
    if opponent_move == SCISSORS and player_strategy == LOSS:
        return PAPER


def calculate_new_score(opponent, player):
    opponent_move = moves_mapping[opponent]
    player_strategy = win_mapping[player]

    player_move = calculate_required_move(opponent_move, player_strategy)

    move_score = shape_score[player_move]
    round_score = calculate_result(opponent_move, player_move)

    return move_score + round_score


# answer for puzzle 2
player_strategy_score = 0

for line in fhand:
    moves = line.split()
    opponent_move = moves[0]
    player_move = moves[1]

    player_score += calculate_round_score(opponent_move, player_move)
    player_strategy_score += calculate_new_score(opponent_move, player_move)


print("Score of player for first puzzle", player_score)  # puzzle 1 answer
print("Score of player according to strategy", player_strategy_score)  # puzzle 2
