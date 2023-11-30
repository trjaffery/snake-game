from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.x_position = 0
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.all_segments.append(snake)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())
    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            position = self.all_segments[seg_num - 1].pos()
            self.all_segments[seg_num].goto(position)

        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)
