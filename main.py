from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard
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
food = Food()
scoreboard = Scoreboard()

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
    scoreboard.write_scoreboard()

    # TODO: #4 Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()

        # TODO: #5 Create a scoreboard

        scoreboard.increase_score()
        scoreboard.clear()
        scoreboard.write_scoreboard()

    # TODO: #6 Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # TODO: #7 Detect collision with tail

    # if head collides with any segment in the tail

    for segment in snake.all_segments[1:]:
         if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()