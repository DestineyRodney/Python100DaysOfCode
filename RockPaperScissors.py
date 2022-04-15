rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

import random
random_int = random.randint(0,2)

user_choice = ""
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)

computer_choice = random_int

print(computer_choice)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)


if user_input == 0 and computer_choice == 1:
    print("You lose")
elif user_input == 0 and computer_choice == 2:
    print("You Win")
elif user_input == 1 and computer_choice == 0:
    print("You Win!")
elif user_input == 1 and computer_choice == 2:
    print("You lose")
elif user_input == computer_choice:
    print("Tie")
elif user_input == 2 and computer_choice == 0:
    print("You lose")
elif user_input == 2 and computer_choice == 1:
    print("You win")