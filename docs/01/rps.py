
import random

# Note: this program is not very good, because a tie is counted as a win

wins = 0
losses = 0

while True: # repeat forever
    user = input("Rock, Paper, or Scissors? ").lower() # get user input and convert to lowercase
    if user not in ["rock", "paper", "scissors"]: # check if user input is valid
        print("Invalid input")
        continue # go to next iteration of loop
    computer = random.choice(["rock", "paper", "scissors"]) # choose a random option
    
    if user == computer:
        print("Tie!")
    elif user == "rock":
        if computer == "paper":
            print("You lose!")
            losses += 1
        else:
            print("You win!")
            wins += 1
    elif user == "paper":
        if computer == "scissors":
            print("You lose!")
            losses += 1
        else:
            print("You win!")
            wins += 1
    elif user == "scissors":
        if computer == "rock":
            print("You lose!")
            losses += 1
        else:
            print("You win!")
            wins += 1
    else:
        print("Invalid input")
    
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    print("Score: " + str(wins - losses))
    if input("Play again? (y/n) ").lower() != "y": # ask user if they want to play again
        break # exit loop