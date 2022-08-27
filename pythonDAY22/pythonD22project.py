import time
from turtle import Screen
from pythonD22projectPaddle import Paddle
from pythonD22projectBall import Ball
from pythonDAY22projectScore import Score
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PINE BALL GAME")

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # detect collision with paddle
    if ball.xcor() >= 340 and ball.distance(r_paddle) < 50:
        ball.paddlebounce()
    if ball.xcor() <= -340 and ball.distance(l_paddle) < 50:
        ball.paddlebounce()
    if ball.xcor() > 380:
        ball.reset_position()
        score.update_lscore()
    if ball.xcor() < -380:
        ball.reset_position()
        score.update_rscore()


screen.exitonclick()
