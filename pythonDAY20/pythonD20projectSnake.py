from turtle import Turtle, Screen
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for t in STARTING_POSITION:
            self.add_turtle(t)

    def add_turtle(self, t):
        timmy = Turtle(shape="circle")
        timmy.color("green")
        timmy.penup()
        timmy.goto(t)
        self.all_turtles.append(timmy)

    def extend(self):
        self.add_turtle(self.all_turtles[-1].position())

    def move(self):
        for t in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[t - 1].xcor()
            new_y = self.all_turtles[t - 1].ycor()
            self.all_turtles[t].goto(new_x, new_y)
        self.all_turtles[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

