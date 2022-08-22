import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


walks = [0, 90, 180, 270]
timmy = Turtle()

timmy.speed(7)
timmy.pensize(15)


def random_walk(num):
    for _ in range(num):
        timmy.forward(30)
        timmy.pencolor(random_color())
        timmy.setheading(random.choice(walks))


random_walk(200)

screen = Screen()
screen.exitonclick()
