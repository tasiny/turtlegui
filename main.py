from turtle import Screen
from functions import one_line, reset_left


my_screen = Screen()
my_screen.colormode(255)
my_screen.setup(width=500, height=500)
my_screen.setworldcoordinates(-30, -20, my_screen.window_width() - 5, my_screen.window_height() - 5)

for _ in range(10):
    one_line()
    reset_left()


my_screen.exitonclick()

