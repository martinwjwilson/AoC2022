# get the input file contents into a variable
f = open('input.txt', 'r')
content = f.read()
list_of_rounds = content.split("\n")

# round outcome values
loss_value = 0
draw_value = 3
win_value = 6

# list of choices in order
possible_choices = {"R": 1,
                    "P": 2,
                    "S": 3}

def calculate_round_winner(your_choice, opponent_choice) -> int:
    # return "you", "opponent" or "draw" depending on who won
    if your_choice == opponent_choice:
        return draw_value

    if your_choice == "R":
        if opponent_choice == "P":
            return loss_value
        if opponent_choice == "S":
            return win_value
    if your_choice == "P":
        if opponent_choice == "S":
            return loss_value
        if opponent_choice == "R":
            return win_value
    if your_choice == "S":
        if opponent_choice == "R":
            return loss_value
        if opponent_choice == "P":
            return win_value


def calculate_choice_score(your_choice: str) -> int:
    return possible_choices[your_choice]


def calculate_your_choice(opponent_choice, outcome):
    if outcome == "Lose":
        if opponent_choice == "R":
            return "S"
        if opponent_choice == "P":
            return "R"
        if opponent_choice == "S":
            return "P"
    if outcome == "Draw":
        return opponent_choice
    if outcome == "Win":
        if opponent_choice == "R":
            return "P"
        if opponent_choice == "P":
            return "S"
        if opponent_choice == "S":
            return "R"


def convert_to_outcome(letter: str) -> str:
    if letter == "X":
        return "Lose"
    if letter == "Y":
        return "Draw"
    return "Win"


def convert_moves(choice: str) -> str:
    if choice in ("A", "X"):
        return "R"
    elif choice in ("B", "Y"):
        return "P"
    return "S"


# convert choices into strings
total_score = 0
for current_round in list_of_rounds:
    expected_outcome = convert_to_outcome(current_round[2])
    opponent_choice = convert_moves(current_round[0])
    # round winner
    your_choice = calculate_your_choice(opponent_choice, expected_outcome)
    round_outcome = calculate_round_winner(your_choice, opponent_choice)
    your_choice_score = calculate_choice_score(your_choice)

    print(f"Your choice {your_choice} and choice score {your_choice_score}")
    print(f"Round outcome was {round_outcome}")
    total_score += (round_outcome + your_choice_score)
    print(f"Total score {total_score}\n")

print(total_score)
