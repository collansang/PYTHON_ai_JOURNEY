#generate a ran#if not a valid number  print error
#if number is < than guess 
#rint too high
#ele print excellent

import random

guess_no = random.randint(1, 100)

while True:
    try:
        number = int(input("Guess the number: "))
        if number > guess_no:
            print("Too high")
        elif number < guess_no:
            print("Too low")
        else:
            print("Excellent!! You got it right")
        break
    except ValueError:
        print("Please enter a valid number")
   
