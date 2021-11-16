# # importing all with * isn't recommended
# from turtle import *
# # imports the turtle module, but you have to define where classes are coming from with
# # tim = turtle.Turtle()
# import turtle
# # import module as a shorter alias so it's easier to reference.
# import turtle as t
# from the turtle module, import the classes Turtle and Screen
from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("deep pink")

for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()

import heroes
print(heroes.gen())