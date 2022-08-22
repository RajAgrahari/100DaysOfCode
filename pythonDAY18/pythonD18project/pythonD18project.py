import random
import turtle

import colorgram
from turtle import Turtle, Screen

colors = colorgram.extract('hirst.jpg', 38)
rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tup = (r, g, b)
    rgb_color.append(tup)
turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.setheading(225)
timmy.penup()
timmy.fd(300)
timmy.pendown()
timmy.setheading(0)
timmy.hideturtle()

def draw_hirst_image():
    for _ in range(10):
        for _ in range(10):
            timmy.pencolor(random.choice(rgb_color))
            timmy.dot(30)
            timmy.penup()
            timmy.fd(50)
        timmy.backward(500)
        timmy.left(90)
        timmy.fd(50)
        timmy.right(90)


draw_hirst_image()
screen = Screen()
screen.exitonclick()

