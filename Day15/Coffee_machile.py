coffees_data = [
    {
        "coffee_type": "expresso",
        "resources":
            {
                "water_needed": 50,
                "coffee_needed": 18,
                "milk_needed": 0,
                "price": 1.50
            }
    },
    {
        "coffee_type": "latte",
        "resources":
            {
                "water_needed": 200,
                "coffee_needed": 24,
                "milk_needed": 150,
                "price": 2.50
            }
    },
    {
        "coffee_type": "cappuccino",
        "resources":
            {
                "water_needed": 250,
                "coffee_needed": 24,
                "milk_needed": 100,
                "price": 3.00
            }
    }
]
# print(coffees_data[1]["coffee_type"])
# print(len(coffees_data))
resources = {
    "coffee_reserved": 300,
    "milk_reserved": 300,
    "water_reserved": 300
}

def reserved_materials(coffees, resource, user_coffee_type):

    for position in range(len(coffees)):
        if coffees[position]["coffee_type"] == user_coffee_type:
            water = resource["water_reserved"] - coffees[position]["resources"]["water_needed"]
            coffee = resource["coffee_reserved"] - coffees[position]["resources"]["coffee_needed"]
            milk = resource["milk_reserved"] - coffees[position]["resources"]["milk_needed"]
            return f"Milk : {milk} Coffee: {coffee} Water: {water}"



def paid_amount(pennies, nickles, dimes, quarters):

    return (pennies * .01) + (nickles * .05) + (dimes * .10) + (quarters * .25)





user_coffee = input("Which coffee?")
print(reserved_materials(coffees_data, resources, user_coffee))
for i in range(len(coffees_data)):
    print(i)
    pennies = int(input("How many pennies?"))
    nickles = int(input("How many nickles?"))
    dimes = int(input("How many dimes?"))
    quarters = int(input("How many quarters?"))
total_paid = paid_amount(pennies, nickles, dimes, quarters)
# if to != coffees_data[i]["resources"]["price"]:
#     print(f"You did not pay enough. Here's your {total_paid} back")

# #
