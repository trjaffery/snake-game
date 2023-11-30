from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('courier', 16, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def write_scoreboard(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def clear(self):
        super().clear()

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(x=0, y=0)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write("GAME OVER!", align = ALIGNMENT, font = FONT)
