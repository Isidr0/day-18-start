# # importing all with * isn't recommended
# from turtle import *
# # imports the turtle module, but you have to define where classes are coming from with
# # tim = turtle.Turtle()
# import turtle
# # import module as a shorter alias so it's easier to reference.
# import turtle as t
# from the turtle module, import the classes Turtle and Screen
import turtle
from turtle import Turtle, Screen
import random
import numpy as np

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

# draw a spirograph

# challenge 4 random walk
#
# tim.width(15)
# tim.speed('fastest')
# directions = [0, 90, 180, 270]
#
# for _ in range(300):
#     random_heading = random.choice(directions)
#     # random_color = list(np.random.choice(range(255), size=3))
#     tim.pencolor(random_color())
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random_heading)

# challenge 3
# from 3 through 11
# for i in range(3, 11):
#     random_color = random.choice(["green", "blue", "yellow", "pink", "orange"])
#     tim.color(random_color)
#     # run 3, 3 times, 4 4 times, and divide 360 by that number to get angle. this results in each shape.
#     for _ in range(i):
#         angles = 360 / i
#         tim.forward(100)
#         tim.right(angles)


# challenge 2
# for _ in range(15):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)

# challenge 1
# for _ in range(4):
#     tim.forward(50)
#     tim.right(90)

screen = Screen()
screen.exitonclick()

# import heroes
# print(heroes.gen())