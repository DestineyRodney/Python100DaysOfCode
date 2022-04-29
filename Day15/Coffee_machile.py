coffees_data = {
        "expresso": {
            "resources": {
                    "water_needed": 50,
                    "coffee_needed": 18,
                    "milk_needed": 0,
                    "price": 1.50
            },
        },
        "latte": {
            "resources": {
                    "water_needed": 200,
                    "coffee_needed": 24,
                    "milk_needed": 150,
                    "price": 2.50
                },
        },
        "cappuccino": {
            "resources":
                {
                    "water_needed": 250,
                    "coffee_needed": 24,
                    "milk_needed": 100,
                    "price": 3.00
                },
        },
}
profit = 0

resources = {
    "coffee_reserved": 300,
    "milk_reserved": 300,
    "water_reserved": 300
}
print(resources)


def reserved_materials(coffees, resource, user_coffee_type):
    for item in coffees_data:
        if item == user_coffee_type:
            resource["water_reserved"] -= coffees[user_coffee]["resources"]["water_needed"]
            resource["coffee_reserved"] -= coffees[user_coffee]["resources"]["coffee_needed"]
            resource["milk_reserved"] -= coffees[user_coffee]["resources"]["milk_needed"]
            global profit
            profit += coffees[user_coffee]["resources"]["price"]


def paid_amount():
    pennies = int(input("How many pennies?"))
    nickles = int(input("How many nickles?"))
    dimes = int(input("How many dimes?"))
    quarters = int(input("How many quarters?"))
    return (pennies * .01) + (nickles * .05) + (dimes * .10) + (quarters * .25)

# is_on = True
# while is_on:
user_coffee = input("Which coffee?")
    # if user_coffee == "off":
        # is_on = False
if user_coffee == "report":
    reserved_materials(coffees_data, resources, user_coffee)
    print(resources)
    print(f"Profit: {profit}")

total_paid = paid_amount()
if total_paid < coffees_data[user_coffee]["resources"]["price"]:
    print(f"You did not pay enough. Here's your {total_paid} back")
elif total_paid > coffees_data[user_coffee]["resources"]["price"]:
    refund = round(total_paid - coffees_data[user_coffee]["resources"]["price"], 2)
    print(f"Here's your {user_coffee} and your change: {refund}")
else:
    print(f"Here's your {user_coffee}")

