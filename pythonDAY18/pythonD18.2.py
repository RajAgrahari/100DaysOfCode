import turtle as t


timmy = t.Turtle()
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
screen = t.Screen()
screen.exitonclick()
