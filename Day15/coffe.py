# Print report
#  check resources sufficient
# process coins
#  check transaction succssful
#  make coffee

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 600,
    "coffee": 600,
    "milk": 600
}

def resource_sufficient(order_ingredients):
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
           print(f"Sorry there's not enough {item} to make your drink")
           return False
    return True

def pay():
    print("Please insert coins")
    total = int(input("Quarters:")) * 0.25
    total += int(input("Dimes:")) * 0.10
    total += int(input("Nickles:")) * 0.05
    total += int(input("Pennies:")) * 0.01
    return total

def transaction_success(money_paid, drink_cost):
    if money_paid >= drink_cost:
        change = round(money_paid - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is your change: {change}")
        return True

    elif money_paid < drink_cost:
        print(f"You did not insert enough. Here is you {money_paid} back")
        return False


def make_coffee(order_ingredients, drink_name):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    user_choice = input("What would you like? (expresso/latte/cappuccino)").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"water: {resources['water']} ml")
        print(f"coffee: {resources['coffee']} g")
        print(f"milk: {resources['milk']} ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if resource_sufficient(drink["ingredients"]):
            total_payment = pay()
            if transaction_success(total_payment, drink["cost"]):
                make_coffee(drink["ingredients"], user_choice)





