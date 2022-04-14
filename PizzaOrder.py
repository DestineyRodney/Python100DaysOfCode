print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_cost = 15
medium_cost = 20
large_cost = 25
pep_charge = 2
cheese_charge = 1
bill = 0

if size == "S":
    bill = small_cost
elif size == "M":
    bill = medium_cost
elif size == "L":
    bill = large_cost

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f" Your final bill is: ${bill}")