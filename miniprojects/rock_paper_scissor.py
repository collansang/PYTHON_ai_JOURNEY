#rock  scissor game
    #ask the user to make a choice rps
    #if choice is not valid print erroe
    #let the computer make its choice and print the result
    #print the winner and break

import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"

choices = (ROCK, PAPER, SCISSORS)

def explanation():
    name = input("Enter your name: ")
    print(f"Hello {name} we are going to play rock, paper, scissors. "
        "Rock beats scissors, scissors beats paper and  paper beats rock. ")


def get_user_choice():
    while True:
        user_choice = input("Choose your guess (r/p/s): ").lower(). strip()
        if user_choice in choices:
            return user_choice                     
        else:
            print("invalid choice")      

def display_choices(user_choice, computer_choice):
    print(f"You chose {user_choice} and the computer chose {computer_choice}") 


def determine_winner(user_choice, computer_choice):   
    if (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)):
        print("You win")
    elif user_choice == computer_choice:
        print("Tie")
    else :
        print("You loose")
      

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        determine_winner(user_choice, computer_choice)
        display_choices(user_choice, computer_choice)
        
        while True:
            should_continue = input("continue?y/n: ").lower().strip()
            if should_continue == "n":
                print("thank you for playing")
                break            
            elif should_continue == "y":
                play_game()
            else:
                print("wrong choice")
        break
explanation()
play_game()