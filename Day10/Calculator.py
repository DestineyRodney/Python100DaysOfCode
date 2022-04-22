# print("Welcome to the calculator")
# number_one = int(input("Enter a number"))
# operation = input(f"Pick an operation: \n + \n - \n * \n /")
# number_two = int(input("Enter a number"))
#
#
# def multiply (num_one, num_two):
#     return num_one * num_two
#
#
# def divide (num_one, num_two):
#     return num_one / num_two
#
#
# def subtract (num_one, num_two):
#     return num_one - num_two
#
#
# def add (num_one, num_two):
#     return num_one + num_two
#
# if operation == "+":
#     print(add(num_one=number_one, num_two=number_two))
# elif operation == "-":
#     print(subtract(num_one=number_one, num_two=number_two))
# elif operation == "/":
#     print(divide(num_one=number_one, num_two=number_two))
# elif operation == "*":
#     print(multiply(num_one=number_one, num_two=number_two))

# Another way

def multiply(num_one, num_two):
    return num_one * num_two


def divide(num_one, num_two):
    return num_one / num_two


def subtract(num_one, num_two):
    return num_one - num_two


def add(num_one, num_two):
    return num_one + num_two


print("Welcome to the calculator")
num_one = int(input("Enter a number"))
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

for symbol in operations:
    print(symbol)

chosen_operator = input("Pick an operation from above")
num_two = int(input("Enter a number"))

calc_function = operations[chosen_operator]
answer = calc_function(num_one, num_two)


print(f"{num_one} {chosen_operator} {num_two} = {answer}")
