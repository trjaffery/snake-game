from turtle import Turtle, Screen
import random
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Tanzeel's Snake Game")
screen.tracer(0)

# TODO: #1 - Create a snake body

snake = Snake()

# TODO: #3 - Control the Snake

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")


# TODO: #2 - Move the snake
# created the snake class and now it can move with the method move()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()








screen.exitonclick()