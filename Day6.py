# Functions

# def greeting(name):
#     last_name = "Rodney"
#     full_name = name + " " + last_name
#     print(f"Hello {full_name}")
#
# greeting("Destiney")



# Maze https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# Makes sure robot hits a wall
# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

















# import random
# random_int = random.randint(0, (len(word_list) - 1))
# # print(random_int)
#
# chosen_word = word_list[random_int]
# print(chosen_word)
# end_of_game = False
# while not end_of_game:
#     lives_left = 7
#
#     guess = input("Choose a random letter ").lower()
#     print(f"Your guess is:  {guess}")
#     #  Prints out empy list
#     display = []
#     for space in range(len(chosen_word)):
#         display += "_"
#     print(f"Before guess \n{display}")
#
#     for char in range(len(chosen_word)):
#         letter = chosen_word[char]
#         if guess == letter:
#             display[char] = letter
#
#     print(f"After guess \n{display}")
#
#     if "_" not in display:
#         end_of_game = True
#         print("You win")


# if guess in chosen_word:
#     print("Right")
# else:
#     print("Wrong")
