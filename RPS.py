# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[], my_history=[], score_history=[]):

    if prev_play and len(my_history) > 0:
        if (prev_play == "R" and my_history[-1] == "P") or (prev_play == "S" and my_history[-1] == "R") or (prev_play == "P" and my_history[-1] == "S"):
            score_history.append("win")
        if (prev_play == "R" and my_history[-1] == "S") or (prev_play == "S" and my_history[-1] == "P") or (prev_play == "P" and my_history[-1] == "R"):
            score_history.append("lose")
    if prev_play:
        opponent_history.append(prev_play)

    randomize_flag = False
    if len(score_history) > 3:
        if score_history[-3] == "lose" and score_history[-2] == "lose" and score_history[-1] == "lose":
            randomize_flag = True

    if len(opponent_history) < 3 or randomize_flag:
        ran = random.randint(1, 99)
        if ran <= 33:
            my_history.append("R")
            return "R"
        elif ran <= 66:
            my_history.append("P")
            return "P"
        else:
            my_history.append("S")
            return "S"
    
    prev_prev_play = opponent_history[-2]
    prev_prev_my_play = my_history[-2]
    prev_my_play = my_history[-1]
    prediction = {"R": 0, "P": 0, "S": 0}
    latest_200 = max(0, len(opponent_history) - 200)
    latest_100 = max(0, len(opponent_history) - 100)
    latest_50 = max(0, len(opponent_history) - 50)
    for index in range(max(2, len(opponent_history) - 300), len(opponent_history) - 1):
        add_amount = 0
        if opponent_history[index - 2] == prev_prev_play and opponent_history[index - 1] == prev_play:
            if prev_prev_my_play == my_history[index - 2]:
                add_amount += 0
            if prev_my_play == my_history[index - 1]:
                add_amount += 0
            if prev_prev_my_play == my_history[index - 2] and prev_my_play == my_history[index - 1]:
                add_amount += 1
            if index > latest_50:
                add_amount += 3
            elif index > latest_100:
                add_amount += 2
            elif index > latest_200:
                add_amount += 1
            prediction[opponent_history[index]] += add_amount

    add_amount = 1
    if my_history[-1] == "R":
        prediction["P"] += add_amount
    elif my_history[-1] == "P":
        prediction["S"] += add_amount
    else:
        prediction["R"] += add_amount

    if prediction["R"] >= prediction["P"] and prediction["R"] >= prediction["S"]:
        guess = "P"
    elif prediction["S"] >= prediction["P"] and prediction["S"] >= prediction["R"]:
        guess = "R"
    else:
        guess = "S"

    my_history.append(guess)
    return guess
