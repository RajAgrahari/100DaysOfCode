from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def anti_clockwise_turn():
    timmy_new_heading = timmy.heading()+10
    timmy.setheading(timmy_new_heading)


def clockwise_turn():
    timmy_new_heading = timmy.heading() - 10
    timmy.setheading(timmy_new_heading)


def clear_screen():
    timmy.home()
    timmy.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=anti_clockwise_turn)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=clockwise_turn)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
