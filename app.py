# create a minigame that meets the following specifications:
# The console is used to interact with the player.
# The player can choose one of the three options: rock, paper, or scissors.
# The player can choose whether to play again.
# The player should be warned if they enter an invalid option.
# The player is shown their score at the end of the game.

import random

print("Welcome to Rock, Paper, Scissors!")
print("You'll be playing against the computer.")

options = ["rock", "paper", "scissors"]
player_wins = 0
computer_wins = 0

while True:
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    if player_choice not in options:
        print("Invalid option. Try again.")
        continue

    computer_choice = random.choice(options)

    print(f"\nYou chose {player_choice}, and the computer chose {computer_choice}.\n")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        player_wins += 1
    else:
        print("You lose!")
        computer_wins += 1

    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again != "y":
        break

print(f"\nYou won {player_wins} times and the computer won {computer_wins} times.")