import replit


print("Welcome to the secret auction")

bidding_finished = False


def highest_bidder(bidders_log):
    highest_bid = 0
    winner = ""
    for bidder in bidders_log:
        bid = bidders_log[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder[highest_bid]

    print(f"The winner is {winner} with the bid of {highest_bid}")


while not bidding_finished:
    name = input("What is your name?")
    bid = int(input("What is your bid"))
    bid_log = {name: bid}
    more_bidders = input("Are there more bidders? (yes or no)")
    if more_bidders == "no":
        bidding_finished = True
        highest_bidder(bid_log)
    elif more_bidders == "yes":
        replit.clear()


