# In python create a rock paper scissors game in the console that is played against the computer, it should keep going until the user says so, each round a counter will be incremented for the winner, one the game finishes the winner will be announced with the score.
import random

print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer.")
print("Type 'quit' at anytime to end the game.")

user_score = 0
computer_score = 0

while True:
    user_input = input("Rock, Paper, or Scissors? ").lower()
    if user_input == "quit":
        break
    if user_input != "rock" and user_input != "paper" and user_input != "scissors":
        print("Invalid input.")
        continue

    computer_input = random.randint(0, 2)
    if computer_input == 0:
        computer_input = "rock"
    elif computer_input == 1:
        computer_input = "paper"
    elif computer_input == 2:
        computer_input = "scissors"

    print("You chose " + user_input + ", the computer chose " + computer_input + ".")

    if user_input == computer_input:
        print("Tie!")
    elif user_input == "rock" and computer_input == "paper":
        print("Computer wins!")
        computer_score += 1
    elif user_input == "rock" and computer_input == "scissors":
        print("You win!")
        user_score += 1
    elif user_input == "paper" and computer_input == "rock":
        print("You win!")
        user_score += 1
    elif user_input == "paper" and computer_input == "scissors":
        print("Computer wins!")
        computer_score += 1
    elif user_input == "scissors" and computer_input == "rock":
        print("Computer wins!")
        computer_score += 1
    elif user_input == "scissors" and computer_input == "paper":
        print("You win!")
        user_score += 1

    print("Current score: You " + str(user_score) + ", Computer " + str(computer_score))
    print("")