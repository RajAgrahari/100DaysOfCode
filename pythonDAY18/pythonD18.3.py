import random
from turtle import Turtle, Screen

colors = ["aquamarine", "cyan", "maroon", "gold", "magenta", "indigo", "crimson"]
timmy = Turtle()
timmy.speed(10)


def draw_polygon(i):
    for x in range(i):
        timmy.forward(100)
        timmy.right((360 / i))


for i in range(3, 10):
    timmy.color(random.choice(colors))
    draw_polygon(i)

screen = Screen()
screen.exitonclick()
