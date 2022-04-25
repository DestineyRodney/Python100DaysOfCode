import random
from replit import clear

easy_level = 6
hard_level = 3


def diff(level):
    if level == "easy":
        return easy_level
    else:
        return hard_level


def check_guess(guess_num, chosen_num, guess_attempt):
    if guess_num > chosen_num:
        print("Too high")
        return guess_attempt - 1

    elif guess_num < chosen_num:
        print("Too low")
        return guess_attempt - 1
    else:
        print(f"Correct! The number was {chosen_num}")


def play():

    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    chosen_num = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

    guess_attempt = diff(difficulty)
    guess_num = 0

    while guess_num != chosen_num:
        print(f"You have {guess_attempt} attempts remaining to guess the number.")

        guess_num = int(input("Make a guess"))
        guess_attempt = check_guess(guess_num, chosen_num, guess_attempt)

        if guess_attempt == 0:
            print(f"You lose. You ran out of guesses. The number was {chosen_num}")
            return
        elif guess_num != chosen_num:
            print("Guess again")


while input("Do you want to play a guessing game? Type 'y' or 'n'") == "y":
    clear()
    play()








