#Dice rolling game
#Ask the user. Role the dice?
    #if yes/y generate two random numbers
    #print them
    #if no/n thank the user and terminate
    #if the print something else, tell them invalid choice and reprompt them

import random

name = input("Should i call you mista or misis?????:  ").capitalize()
while True:
    message = input(f"Hello {name} .Do you wanna roll a dice? (y/n)").lower()
    if message == "y":
        random_number1 = random.randint(1,6)# this generates a random number between 1 and 6
        random_number2 = random.randint(1,6)
        print(f"Your two lucky numbers are: {random_number1} , {random_number2}")
    elif message == "n":
        print("Thank you for playing")
        break
    else:
        print("Invalid choice, try again") 