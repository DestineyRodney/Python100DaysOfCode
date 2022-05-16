import turtle as t
from random import random
from turtle import *
import random
tim = Turtle()

# Timmy makes a square

# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# dashed line jogging
# def jog():
#     for _ in range(15):
#         tim.pendown()
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#
# jog()


# def triangle():
#     for _ in range(3):
#         tim.forward(100)
#         tim.right(120)
#
#
# def square():
#     for _ in range(4):
#         tim.forward(100)
#         tim.right(90)
#
#
# def pentagon():
#     for _ in range(5):
#         tim.forward(100)
#         tim.right(72)
#
#
# def hexagon():
#     for _ in range(6):
#         tim.forward(100)
#         tim.right(60)
#
#
# def heptagon():
#     for _ in range(7):
#         tim.forward(100)
#         tim.right(51.42)
#
#
# def octagon():
#     for _ in range(8):
#         tim.forward(100)
#         tim.right(45)
#
#
# def nonagon():
#     for _ in range(9):
#         tim.forward(100)
#         tim.right(40)
#
#
# def decagon():
#     for _ in range(10):
#         tim.forward(100)
#         tim.right(36)
#
#
# triangle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# decagon()

colors = ["firebrick", "dark olive green", "peru", "light salmon", "dark slate blue", "magenta", "cyan", "gray"]


# def draw_shapes(num_sides,):
#     for _ in range(num_sides):
#         angle = 360/num_sides
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shapes(shape_side)
#
#

t.colormode(255)


def wall_checker(self):

    if self.xcor() > 300:
        self.goto(290, self.ycor())
    elif self.xcor() < -300:
        self.goto(-290, self.ycor())

    if self.ycor() > 300:
        self.goto(self.xcor(), 290)
    elif self.ycor() < -300:
        self.goto(self.xcor(), -290)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


direction = [0, 90, 180, 270]

for _ in range(200):
    tim.shape("turtle")
    tim.color(random_color())
    tim.pensize(10)
    tim.speed("fast")
    tim.forward(30)
    wall_checker(tim)
    tim.setheading(random.choice(direction))


# for _ in range(100):
#     tim.speed("fastest")
#     tim.color(random_color())
#     tim.circle(100)
#     current_heading = tim.heading()
#     tim.setheading(current_heading + 10)

screen = t.Screen()
screen.exitonclick()


# Draw Square


# Grapical User Interface - TKINTER - Turtle relies on interface


