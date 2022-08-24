from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter the color of turtle which will win?")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_index = [-100, -60, -20, 20, 60, 100]
all_turtles = []
for i in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(x=-230, y=y_index[i])
    all_turtles.append(timmy)
if user_bet:
    is_race_on = True
while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won! Winning color is {winning_color}")
            else:
                print(f"You've lost! Winning color is {winning_color}")
            is_race_on = False
            break
        random_dis = random.randint(0, 10)
        t.forward(random_dis)


screen.exitonclick()
