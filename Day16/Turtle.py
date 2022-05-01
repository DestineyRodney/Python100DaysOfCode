import turtle
# import another_module
# print(another_module.another_variable)

# New turtle object
# timmy = turtle.Turtle()
# print(timmy)
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chocolate4", "cornsilk4")
# timmy.forward(100)
#
# #  what object has : Object Attributes  object.attribute
# # screen is where turtle will show up
# my_screen = Screen()
# print(my_screen.canvheight)
# # Allowes program to keep screen open until we click
# my_screen.exitonclick()

# what it can do : Methods

# Adding Packages
# Create a table of Pokemon
# search pypi.org

from prettytable import PrettyTable

table = PrettyTable()
print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

