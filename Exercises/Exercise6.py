"""
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.

"""

import random

# Define choices
choices = ["Snake", "Water", "Gun"]

# Create a 2D list for outcomes
# Row: User's choice, Column: Computer's choice
# 1 = Win, -1 = Loss, 0 = Tie
outcome_matrix = [
    [0, 1, -1],  # Snake: Tie, Wins against Water, Loses to Gun
    [-1, 0, 1],  # Water: Loses to Snake, Tie, Wins against Gun
    [1, -1, 0]   # Gun: Wins against Snake, Loses to Water, Tie
]

# Initialize scores
player_score = 0
computer_score = 0

# Function to play the game
def play_snake_water_gun():
    global player_score, computer_score
    print("Welcome to Snake, Water, Gun!")
    print("Choices: 0 = Snake, 1 = Water, 2 = Gun")
    
    while True:
        # User input
        try:
            user_choice = int(input("Enter your choice (0/1/2) or -1 to quit: "))
            if user_choice == -1:
                print("Game Over!")
                break
            if user_choice not in [0, 1, 2]:
                print("Invalid choice. Try again!")
                continue
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        # Computer's random choice
        computer_choice = random.randint(0, 2)
        
        # Display choices
        print(f"You chose: {choices[user_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")
        
        # Determine the outcome
        result = outcome_matrix[user_choice][computer_choice]
        if result == 1:
            print("You win this round!")
            player_score += 1
        elif result == -1:
            print("You lose this round!")
            computer_score += 1
        else:
            print("This round is a tie!")
        
        # Display current scores
        print(f"Current Scores -> You: {player_score}, Computer: {computer_score}")
        print("-" * 30)

    # Final scores
    print("Final Scores:")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Sorry, the computer won the game!")
    else:
        print("It's a tie overall!")

# Play the game
play_snake_water_gun()
