import random
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

is_game_over = False
chosen_num = random.randint(1, 100)
print(chosen_num)

while not is_game_over:

    guess_num = int(input("Make a guess: "))




    if guess_num > chosen_num:
        print("Too high")
    elif guess_num < chosen_num:
        print("Too low")

    if guess_num == chosen_num:
        is_game_over = True
        print("you win")


guess_attempts = 6


if guess_num != chosen_num:
    guess_attempts -= 1
    print(guess_attempts)

    if guess_attempts == 0:
        is_game_over = True
        print("You lose")




