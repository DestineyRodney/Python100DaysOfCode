import random
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_score(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."

    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "You win with a BlackJack"
    elif computer_score == 0:
        return "You lose to a BlackJack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_hand = []
    computer_hand = []
    end_game = False

    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not end_game:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        if user_score == 0 or computer_score or user_score > 21:
            end_game = True
        else:
            cont = input("Would you like to draw another card? ( 'y' to continue 'n' to exit")
            if cont == "y":
                user_hand.append(deal_card())
            else:
                end_game = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"   Your final hand: {user_hand}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()











