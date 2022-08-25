from pythonD20projectSnake import Snake
from turtle import Screen
from pythonD20projectFood import Food
from pythonD20projectScore import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    scoreboard.update_scoreboard()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()
    for timmy in snake.all_turtles[1:]:
        if snake.head.distance(timmy) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
