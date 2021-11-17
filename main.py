# # importing all with * isn't recommended
# from turtle import *
# # imports the turtle module, but you have to define where classes are coming from with
# # tim = turtle.Turtle()
# import turtle
# # import module as a shorter alias so it's easier to reference.
# import turtle as t
# from the turtle module, import the classes Turtle and Screen
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("deep pink")
tim.width(10)

# challenge 4 random walk



for _ in range(100):
    random_heading = random.randint(1, 270)
    random_color = random.randint(0, 255)
    tim.pencolor(240, 160, 80)
    tim.forward(10)
    tim.setheading(random_heading)
    tim.forward(10)

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