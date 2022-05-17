import turtle
import colorgram
from turtle import Turtle, Screen
import random

# Imported rgb from image using colorgram
# colors = colorgram.extract("img.jpeg", 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple = (r, g, b)
#     rgb_colors.append(new_tuple)
#
#
# print(rgb_colors)

color_list = [(236, 225, 83), (202, 5, 72), (198, 164, 10), (235, 51, 129), (206, 76, 11), (108, 179, 218), (219, 162, 103), (234, 225, 6), (30, 188, 108), (23, 106, 173), (13, 23, 64), (17, 28, 175), (213, 135, 176), (9, 185, 214), (205, 29, 142), (125, 189, 162), (8, 49, 28), (37, 132, 73), (125, 219, 233), (67, 22, 8), (61, 11, 26), (111, 89, 211), (142, 216, 201), (238, 63, 31)]


tim = Turtle()
tim.penup()
tim.speed("fastest")
turtle.colormode(255)
tim.setheading(225)
tim.forward(400)
tim.setheading(0)

dot_count = 100

for dots in range(1, dot_count + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()
screen = Screen()
screen.exitonclick()

