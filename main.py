from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
color = ["red", "white", "white"]

snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="d", fun=snake.turn_right)
game_on = True
score.current_score = 0
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segment[0].distance(food) < 15:
        snake.add_snake()
        food.refresh()
        score.add_score()

    if snake.segment[0].xcor() > 290 or snake.segment[0].xcor() < -290 or\
            snake.segment[0].ycor() > 290 or snake.segment[0].ycor() < -290:
        game_on = False
        score.game_over()
    y = 1
    for tail in range(1, len(snake.segment)):
        if snake.segment[0].distance(snake.segment[tail]) < 19:
            game_on = False
            score.game_over()


screen.exitonclick()
