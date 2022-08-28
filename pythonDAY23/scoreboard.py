from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.level += 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def score_reset(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
