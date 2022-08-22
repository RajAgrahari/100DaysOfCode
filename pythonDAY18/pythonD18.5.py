import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed("fastest")

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_a_spirograph():
    for i in range(1, 361, 5):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.setheading(i)
        # timmy.left(i)


draw_a_spirograph()

screen = Screen()
screen.exitonclick()
