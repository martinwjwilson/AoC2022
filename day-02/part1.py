# get the input file contents into a variable
f = open('input.txt', 'r')
content = f.read()
list_of_rounds = content.split("\n")

# Constants
outcome_values = {"loss": 0,
                  "draw": 3,
                  "win": 6}
possible_choices = {"R": 1,
                    "P": 2,
                    "S": 3}


def calculate_round_winner(your_choice, opponent_choice) -> int:
    # return "you", "opponent" or "draw" depending on who won
    if your_choice == opponent_choice:
        return draw_value

    if your_choice == "R":
        if opponent_choice == "P":
            return outcome_values["loss"]
        if opponent_choice == "S":
            return outcome_values["win"]
    if your_choice == "P":
        if opponent_choice == "S":
            return outcome_values["loss"]
        if opponent_choice == "R":
            return outcome_values["win"]
    if your_choice == "S":
        if opponent_choice == "R":
            return outcome_values["loss"]
        if opponent_choice == "P":
            return outcome_values["win"]


def calculate_choice_score(your_choice: str) -> int:
    return possible_choices[your_choice]


def convert_moves(choice: str) -> str:
    if choice in ("A", "X"):
        return "R"
    elif choice in ("B", "Y"):
        return "P"
    return "S"


# convert choices into strings
total_score = 0
for current_round in list_of_rounds:
    your_choice = convert_moves(current_round[2])
    opponent_choice = convert_moves(current_round[0])
    # round winner
    round_outcome = calculate_round_winner(your_choice, opponent_choice)
    your_choice_score = calculate_choice_score(your_choice)

    total_score += (round_outcome + your_choice_score)

print(total_score)
