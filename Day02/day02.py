# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
# The first column is what your opponent is going to play:
# A for Rock, B for Paper, and C for Scissors. The second column--
# The second column, you reason, must be what you should play in response:
# X for Rock, Y for Paper, and Z for Scissors

#The winner of the whole tournament is the player with the highest score.
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

### Part 1

key_shape = {
    'X':'Rock',
    'Y':'Paper',
    'Z':'Scissors',
    'A':'Rock',
    'B':'Paper',
    'C':'Scissors'
}

player_shape_beat = {
    'Z': 'B',
    'Y': 'A',
    'X': 'C'
}

shape_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

round_scoring = {
    'loss': 0,
    'draw': 3,
    'win': 6
}

# with open('input.txt') as file:
#     lines = [line.replace(str('\n'), "") for line in file]
#
# total_score = 0
# for play in lines:
#     round = play.split()
#     opponent = round[0]
#     player = round[1]
#
#     # draw
#     if key_shape[opponent] == key_shape[player]:
#         total_score += (round_scoring['draw'] + shape_score[player])
#     # win
#     elif player_shape_beat[player] == opponent:
#         total_score += (round_scoring['win'] + shape_score[player])
#     # lose
#     else:
#         total_score += (round_scoring['loss'] + shape_score[player])

# print(total_score)



##### Part 2

# In the first round, your opponent will choose Rock (A),
# and you need the round to end in a draw (Y), so you also choose Rock.
# This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B),
# and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

key_shape_2 = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

key_new_shape = {
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win',
}

player_shape_beat_2 = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

shape_score_2 = {
    'A': 1,
    'B': 2,
    'C': 3
}

round_scoring_2 = {
    'loss': 0,
    'draw': 3,
    'win': 6
}

with open('input.txt') as file:
    lines = [line.replace(str('\n'), "") for line in file]

total_score = 0
for play in lines:
    round = play.split()
    opponent = round[0]
    outcome = round[1]

    # Draw
    if key_new_shape[outcome] == 'draw':
        total_score += (round_scoring_2['draw'] + shape_score_2[opponent])

    # Win
    elif key_new_shape[outcome] == 'win':
        player_play = player_shape_beat_2[player_shape_beat_2[opponent]]
        total_score += (round_scoring_2['win'] + shape_score_2[player_play])

    # Loss
    else:
        player_play = player_shape_beat_2[opponent]
        total_score += (round_scoring_2['loss'] + shape_score_2[player_play])

print(total_score)

