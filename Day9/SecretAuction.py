from replit import clear
import random
#HINT: You can call clear() to clear the output in the console.
# from art import logo

print("Welcome to the secret auction")

bids = {}

def highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of {highest_bid}")


bidding_finished = False

while not bidding_finished:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    #
    bids[name] = bid
    more_bidders = input("Are there any other bidders?(yes or no)").lower()
    if more_bidders == "no":
        bidding_finished = True
        highest_bid(bids)
    elif more_bidders == "yes":
        clear()






