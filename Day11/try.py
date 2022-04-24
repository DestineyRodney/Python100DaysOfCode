import random
import replit

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21:
        return"You went over. You lose"
    if computer_score > 21:
        return "Opponent went over. You win"

    if user_score == computer_score:
        return"draw"
    elif user_score == 0:
        return "You win with blackjack"
    elif computer_score == 0:
        return "You lose to a blackjack"
    elif computer_score > user_score:
        return "You lose"
    elif user_score > computer_score:
        return "you win"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "You win, oppenent went over"


def play_game():
    user_hand = []
    computer_hand = []
    is_game_over = False

    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your hand is: {user_hand} and score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            cont = input("Do you want to deal another card?('y' to continue 'n to exit)")
            if cont == "y":
                user_hand.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"   Your final hand: {user_hand}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack?('y' or 'n')") == "y":
    replit.clear()
    play_game()





