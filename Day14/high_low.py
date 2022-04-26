from game_data import data
from replit import clear
import random
from art import vs
from art import logo


def get_data():
    return random.choice(data)


def format_data(random_account):
    name = random_account["name"]
    description = random_account["description"]
    country = random_account["country"]
    return f"{name} from {country} and {description}"


def check_guess(a_follower, b_follower, guess):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


def play():
    score = 0
    game_continue = True

    a = get_data()

    b = get_data()

    while game_continue:
        a = b
        b = get_data()

        while a == b:
            b = get_data()
        print(f"Compare A: {format_data(a)}")
        print(vs)
        print(f"Against B: {format_data(b)}")

        guess_answer = input("Who has more followers? 'a' or 'b' ").lower()

        a_followers = a["follower_count"]
        print(a_followers)
        b_followers = b["follower_count"]
        print(b_followers)
        is_correct = check_guess(a_followers, b_followers, guess_answer)
        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You got it right. Your current score is: {score}")
        else:
            print(f"Wrong. final score: {score}")
            game_continue = False


play()