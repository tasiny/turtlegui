from turtle import Turtle
import random
from colors import color_list

timmy = Turtle()


def one_line():
    for _ in range(9):
        timmy.pencolor(random.choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.dot(20)


def reset_left():
    timmy.penup()
    timmy.left(90)
    timmy.forward(52)
    timmy.left(90)
    timmy.forward(450)
    timmy.right(180)



