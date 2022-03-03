from turtle import Turtle
from Food import Food

move_distance = 20


class Snake:

    def __init__(self):
        self.x = 0
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            new_turtle = Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.goto(self.x, 0)
            new_turtle.showturtle()
            self.x -= 20
            self.segment.append(new_turtle)

    def add_snake(self):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.segment[len(self.segment) - 1].xcor(), self.segment[len(self.segment) - 1].ycor())
        self.segment.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            self.segment[seg_num].goto(self.segment[seg_num - 1].pos())
        self.segment[0].forward(move_distance)

    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)

    def turn_left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def turn_right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)
