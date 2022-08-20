from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red", "green")
count = 100
while count > 0:
    timmy.forward(count)
    timmy.left(90)
    count -= 1
count = 100
while count > 0:
    timmy.circle(count)
    count -= 5
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
