'''
Stone, Paper, Scissor Game
------------------------------------
Mapping:
1  -> Stone
-1 -> Paper
0  -> Scissor
------------------------------------
MADE BY SAMEER PATRA
'''

import random  # Import the random module for computer's choice
# ---------------- Computer's Choice ----------------
# Computer randomly picks one option: Stone(1), Paper(-1), Scissor(0)
computer = random.choice([-1, 0, 1])

# ---------------- User's Choice ----------------
# Take input as 's' (stone), 'p' (paper), or 'sc' (scissor)
youstr = input("Enter your choice (s for Stone, p for Paper, sc for Scissor): ")

# Dictionary to map user input to numeric value
youDict = {"s": 1, "p": -1, "sc": 0}

# Dictionary to map numeric values back to words (for display)
reversedDict = {1: "Stone", -1: "Paper", 0: "Scissor"}

# ---------------- Input Validation ----------------
if youstr not in youDict:  
    print("Invalid input!")   # If user types something wrong
else:
    # Convert user's string choice into numeric value
    you = youDict[youstr]

    # Show both choices
    print(f"You chose {reversedDict[you]}")
    print(f"Computer chose {reversedDict[computer]}")

    # ---------------- Game Logic ----------------
    if computer == you:
        print("It's a Draw!")   # Same choice → draw

    elif computer == -1 and you == 1:   # Paper beats Stone
        print("You Lose!")

    elif computer == -1 and you == 0:   # Scissor beats Paper
        print("You Win!")

    elif computer == 1 and you == -1:   # Paper beats Stone
        print("You Win!")

    elif computer == 1 and you == 0:    # Stone beats Scissor
        print("You Lose!")

    elif computer == 0 and you == 1:    # Stone beats Scissor
        print("You Win!")

    elif computer == 0 and you == -1:   # Scissor beats Paper
        print("You Lose!")

    else:  
        # This block should never run if logic is correct
        print("Something went wrong")