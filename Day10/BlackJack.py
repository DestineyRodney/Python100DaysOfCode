import random

user_hand = []
computer_hand = []


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


for _ in range(2):
    user_hand.append(deal_card())
    computer_hand.append(deal_card())



def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


user_score = calculate_score(cards=user_hand)
computer_score = calculate_score(cards=computer_hand)

def compare():

is_continue = False
while is_continue:
    print(user_hand)
    print(computer_hand)
    if user_score > 21 and computer_score > 21
        print("yp")




