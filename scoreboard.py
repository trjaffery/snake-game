from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('courier', 16, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode='r') as high_score_file:
            self.high_score = int(high_score_file.read())

    def write_scoreboard(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def clear(self):
        super().clear()

    def increase_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode='w') as high_score_file:
                high_score_file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write_scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.penup()
    #     self.hideturtle()
    #     self.color("white")
    #     self.write("GAME OVER!", align = ALIGNMENT, font = FONT)
