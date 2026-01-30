import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)#letters in the word to guess
    alphabet = set(string.ascii_uppercase)
    used_letters = set()#what the user has guessed
    lives = 6
    
    #get user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print(f"You have {lives}. You have used this letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -=1
                print(f"Letter {user_letter} is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Guess another letter.")
        else:
            print("Invalid character. Please try again.")
    if lives ==0:
        print(f"Sorry, you died. The word was {word}")
    else:
        print(f"Good job!! You guessed the word {word}!!")
        

hangman()

