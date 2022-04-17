word_list = ["aardvark", "baboon", "camel"]

import random

random_int = random.randint(0, len(word_list) - 1)

chosen_word = word_list[random_int]
print(chosen_word)
lives_left = 6

display = []
for space in range(len(chosen_word)):
    display += "_"
print(display)

end_game = False
while not end_game:
    chosen_letter = input("Choose a random letter").lower()

    for letter in range(len(chosen_word)):

        choice = chosen_word[letter]
        if choice == chosen_letter:
            display[letter] = chosen_letter
    if choice not in chosen_letter:
        lives_left -= 1
        print(lives_left)
        if lives_left == 0:
            end_game = True
            print("You lose")

    print(display)

    if "_" not in display:
        end_game = True
        print("You win")